# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-21 … PR-23.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_21_23.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-21 — II tuslanish: говорить, смотреть, любить
# =====================================================================

Q_PR21 = [
    # 1–5 tanish
    {
        "text": "<p>II tuslanishning odatiy koʻplik (они́) qoʻshimchasi qaysi?</p>",
        "choices": ["-ют", "-ят", "-ут", "-ем"],
        "correct": "-ят",
        "explanation": "<p>II tuslanish: <strong>-ю, -ишь, -ит, -им, -ите, -ят</strong> — "
                       "«И qatori, oxirida Я». I tuslanishda esa koʻplik <em>-ют/-ут</em> "
                       "boʻladi. Aynan «они́» shakli feʼl qaysi guruhda ekanini eng "
                       "ishonchli koʻrsatadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ по-ру́сски.</strong> "
                "(говори́ть)</p>",
        "choices": ["говорю́", "говори́ю", "говоря́", "говори́т"],
        "correct": "говорю́",
        "explanation": "<p>Oʻzak <strong>говор-</strong> (infinitivdan <em>-ить</em> olib "
                       "tashlanadi — unli ham ketadi), «я» qoʻshimchasi <strong>-ю</strong>. "
                       "Natija: <strong>говорю́</strong>. Eʼtibor bering, «я» shakli "
                       "ikkala tuslanishda ham <em>-ю</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ фильм.</strong> "
                "(смотре́ть)</p>",
        "choices": ["смотре́ет", "смотри́т", "смо́трит", "смотря́т"],
        "correct": "смо́трит",
        "explanation": "<p>Oʻzak <strong>смотр-</strong>, uchinchi shaxs birligi "
                       "<strong>-ит</strong>. Urgʻu «я» shaklidan keyin oʻzakka qaytadi: "
                       "<em>смотрю́ — смо́тришь — смо́трит</em>. <em>Смотре́ть</em> — "
                       "<em>-еть</em> bilan tugasa ham II tuslanishdagi sakkizta "
                       "«xoin»dan biri.</p>",
    },
    {
        "text": "<p>Qaysi feʼl II tuslanishda?</p>",
        "choices": ["чита́ть", "рабо́тать", "люби́ть", "гуля́ть"],
        "correct": "люби́ть",
        "explanation": "<p><strong>Люби́ть</strong> — <em>-ить</em> bilan tugaydi va "
                       "koʻplikda <em>лю́бят</em> boʻladi, demak II tuslanish. Qolgan "
                       "uchtasi I tuslanish: <em>чита́ют, рабо́тают, гуля́ют</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ пло́в.</strong> "
                "(люби́ть)</p>",
        "choices": ["любю́", "лю́бю", "люблю́", "лю́бит"],
        "correct": "люблю́",
        "explanation": "<p>«Я» shaklida <strong>Б → БЛ</strong> almashinuvi boʻladi, "
                       "chunki Б — lab undoshi (Б, В, М, П, Ф oʻziga Л qoʻshib oladi). "
                       "Qolgan beshta shaklda hech narsa oʻzgarmaydi: <em>лю́бишь, "
                       "лю́бит, лю́бим, лю́бите, лю́бят</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ фильм ка́ждый "
                "ве́чер.</strong> (смотре́ть)</p>",
        "choices": ["смо́трим", "смотре́ем", "смо́трем", "смотри́м"],
        "correct": "смо́трим",
        "explanation": "<p>«Мы» qoʻshimchasi <strong>-им</strong>, oʻzak "
                       "<strong>смотр-</strong>, urgʻu oʻzakda. Xato koʻpincha oʻzakni "
                       "notoʻgʻri ajratishdan chiqadi: <em>смотре́ть</em> dan "
                       "<em>-еть</em> ketadi, faqat <em>-ть</em> emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ по-англи́йски.</strong> "
                "(говори́ть)</p>",
        "choices": ["говорю́т", "говоря́т", "говоря́ют", "говори́т"],
        "correct": "говоря́т",
        "explanation": "<p>II tuslanishda koʻplik <strong>-ят</strong>. <em>Говорю́т</em> "
                       "— eng koʻp uchraydigan xato: I tuslanish qoʻshimchasi II "
                       "tuslanish feʼliga yopishtirilgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ в шко́лу ка́ждый "
                "день.</strong> (ходи́ть)</p>",
        "choices": ["ходю́", "хожу́", "хо́жу", "хо́дю"],
        "correct": "хожу́",
        "explanation": "<p>«Я» shaklida <strong>Д → Ж</strong>: <em>ходи́ть → хожу́</em>. "
                       "Boshqa shakllarda oʻzak butun qoladi: <em>хо́дишь, хо́дит, "
                       "хо́дят</em>. Xuddi shunday <em>ви́деть → ви́жу</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ___ му́зыку?</strong> "
                "(слы́шать)</p>",
        "choices": ["слы́шашь", "слы́шишь", "слы́шаешь", "слыши́шь"],
        "correct": "слы́шишь",
        "explanation": "<p><em>Слы́шать</em> — <em>-ать</em> bilan tugasa ham II "
                       "tuslanishdagi sakkizta «xoin»dan biri, shuning uchun "
                       "<strong>-ишь</strong>. Ular bir maʼno guruhida: "
                       "<em>смотрю́, ви́жу, слы́шу, сижу́, лежу́, стою́, сплю, "
                       "держу́</em> — tananing sezgilari va holati.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ ру́сский "
                "язы́к.</strong> (учи́ть)</p>",
        "choices": ["у́чят", "у́чут", "у́чат", "учу́т"],
        "correct": "у́чат",
        "explanation": "<p>Oʻzak <strong>уч-</strong> shivirlovchiga tugaydi, "
                       "shivirlovchidan keyin esa <strong>Я yozilmaydi</strong> (PR-4). "
                       "Shuning uchun <em>-ят</em> emas, <strong>-ат</strong>. Bu imlo "
                       "qoidasi: talaffuzda farq deyarli sezilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ пло́в ка́ждую "
                "суббо́ту.</strong> (гото́вить)</p>",
        "choices": ["гото́влю", "гото́вю", "готовлю́", "гото́вит"],
        "correct": "гото́влю",
        "explanation": "<p>В ham lab undoshi, demak «я» shaklida <strong>В → ВЛ</strong>: "
                       "<em>гото́влю</em>. Bu — <em>люблю́</em> bilan bir xil qoida. "
                       "Urgʻu bu feʼlda oʻzakda qoladi.</p>",
    },
    {
        "text": "<p>Bu feʼlning oʻzagi qaysi?</p><p><strong>звони́ть</strong></p>",
        "choices": ["звони́-", "звон-", "зво-", "звони́т-"],
        "correct": "звон-",
        "explanation": "<p>II tuslanishda infinitivdan <strong>-ить</strong> butunlay "
                       "ketadi — unli ham. Oʻzak <strong>звон-</strong>, natija: "
                       "<em>звоню́, звони́шь, звони́т, звоня́т</em>. I tuslanishda esa "
                       "faqat <em>-ть</em> ketardi (<em>чита́ть → чита́-</em>).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki feʼl qaysi tuslanishda?</p><p><strong>рабо́тают · "
                "у́чат</strong></p>",
        "choices": ["Ikkalasi I", "Ikkalasi II", "I va II", "II va I"],
        "correct": "I va II",
        "explanation": "<p><em>Рабо́тают</em> — <strong>-ют</strong>, demak I tuslanish. "
                       "<em>У́чат</em> — <strong>-ат</strong>, demak II. Yangi feʼlni "
                       "yodlaganda uni ikki shaklda yozib qoʻying: <em>учи́ть — "
                       "у́чат</em> — shunda guruhini hech qachon adashtirmaysiz.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda almashinuv toʻgʻri koʻrsatilgan?</p>",
        "choices": ["проси́ть → прошу́ (с → ш)", "проси́ть → прожу́ (с → ж)",
                    "проси́ть → прочу́ (с → ч)", "проси́ть → просю́ (almashinuv yoʻq)"],
        "correct": "проси́ть → прошу́ (с → ш)",
        "explanation": "<p>«Я» shaklidagi almashinuvlar: <strong>д → ж</strong> (хожу́), "
                       "<strong>с → ш</strong> (прошу́), <strong>т → ч</strong> "
                       "(плачу́), va lab undoshlariga <strong>Л</strong> qoʻshiladi "
                       "(люблю́). Bu faqat «я» shaklida sodir boʻladi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hamma shakl toʻgʻri?</p>",
        "choices": ["слы́шат · лежа́т · спеша́т", "слы́шят · лежя́т · спешя́т",
                    "слы́шут · лежу́т · спешу́т", "слы́шат · лежя́т · спеша́т"],
        "correct": "слы́шат · лежа́т · спеша́т",
        "explanation": "<p>Uchalasining ham oʻzagi <strong>Ш yoki Ж</strong> ga tugaydi, "
                       "shuning uchun koʻplikda <strong>-ат</strong>. Qolgan "
                       "variantlarda yo shivirlovchidan keyin Я yozilgan (imlo xatosi), "
                       "yo I tuslanish qoʻshimchasi qoʻyilgan.</p>",
    },
    {
        "text": "<p>Nega bu ikki shaklda urgʻu boshqa joyda?</p><p><strong>люблю́ — "
                "лю́бишь</strong></p>",
        "choices": ["Bu xato, urgʻu bir xil boʻlishi kerak",
                    "«Я» shaklida urgʻu qoʻshimchada, keyin oʻzakka qaytadi",
                    "Chunki birinchisi koʻplik",
                    "Chunki ikkinchisi oʻtgan zamon"],
        "correct": "«Я» shaklida urgʻu qoʻshimchada, keyin oʻzakka qaytadi",
        "explanation": "<p>Bu II tuslanishning juda koʻp uchraydigan naqshi: "
                       "<em>люблю́ — лю́бишь</em>, <em>смотрю́ — смо́тришь</em>, "
                       "<em>учу́ — у́чишь</em>, <em>хожу́ — хо́дишь</em>. Lekin "
                       "<em>говорю́ — говори́шь — говоря́т</em> da urgʻu hamma joyda "
                       "oxirida qoladi. Urgʻuni soʻz bilan birga yodlang.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я любю́ ко́фе.", "Я люблю́ ко́фе.",
                    "Я лю́бит ко́фе.", "Я люблю́т ко́фе."],
        "correct": "Я люблю́ ко́фе.",
        "explanation": "<p>«Я» shaklida <strong>люблю́</strong> — Б ga Л qoʻshiladi. "
                       "<em>Любю́</em> — almashinuvni unutish; <em>лю́бит</em> — "
                       "uchinchi shaxs shakli «я» ga qoʻyilgan; <em>люблю́т</em> — "
                       "ikki qoʻshimcha bir soʻzda.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Она́ звони́т ка́ждый день.", "Мы смо́трим фильм.",
                    "Они́ говорю́т по-ру́сски.", "Я ви́жу шко́лу."],
        "correct": "Они́ говорю́т по-ру́сски.",
        "explanation": "<p>Toʻgʻrisi — <strong>Они́ говоря́т</strong>. "
                       "<em>Говори́ть</em> II tuslanishda, demak koʻplikda "
                       "<strong>-ят</strong>. Qolgan uchtasi toʻgʻri: <em>звони́т</em> "
                       "(II), <em>смо́трим</em> (II), <em>ви́жу</em> (д→ж "
                       "almashinuvi).</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Вы говори́те по-ру́сски?</strong></p>",
        "choices": ["— Да, немно́го говорю́.", "— Да, немно́го говори́те.",
                    "— Да, немно́го говоря́т.", "— Да, немно́го говори́ть."],
        "correct": "— Да, немно́го говорю́.",
        "explanation": "<p>Savol «вы» ga berilgan, javob esa <strong>«я»</strong> dan "
                       "keladi — demak <strong>говорю́</strong>. Rus tilida qisqa "
                       "javobda olmoshni tushirib qoldirish mumkin, chunki qoʻshimcha "
                       "kimligini aytib turibdi.</p>",
    },
    {
        "text": "<p>Qaysi soʻz tartibi tabiiy?</p><p><strong>ру́сский язы́к / у́чим / "
                "мы</strong></p>",
        "choices": ["Ру́сский язы́к мы у́чим.", "Мы у́чим ру́сский язы́к.",
                    "У́чим мы ру́сский язы́к.", "Мы ру́сский язы́к у́чим."],
        "correct": "Мы у́чим ру́сский язы́к.",
        "explanation": "<p>Odatdagi tartib: <strong>ega → feʼl → toʻldiruvchi</strong>. "
                       "Oʻzbekchada feʼl oxirda boʻlardi («Biz rus tilini "
                       "oʻrganamiz») — ruschada uni oldinga suring. Qolgan variantlar "
                       "grammatik jihatdan mumkin, lekin ular alohida urgʻu "
                       "beradi va oddiy gapda gʻalati eshitiladi.</p>",
    },
]


# =====================================================================
# PR-22 — Notoʻgʻri feʼllar: хотеть, есть, дать, идти, ехать, жить, писать
# =====================================================================

Q_PR22 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ в Ташке́нте.</strong> "
                "(жить)</p>",
        "choices": ["жию́", "живу́", "жи́ю", "живю́"],
        "correct": "живу́",
        "explanation": "<p><em>Жить</em> ning oʻzagi tuslanganda <strong>жив-</strong> "
                       "boʻladi — infinitivda yoʻq boʻlgan <strong>В</strong> paydo "
                       "boʻladi. Qoʻshimchalar esa oddiy I tuslanish: <em>живу́, "
                       "живёшь, живёт, живём, живёте, живу́т</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ чай.</strong> "
                "(хоте́ть)</p>",
        "choices": ["хочу́", "хотю́", "хоте́ю", "хоти́м"],
        "correct": "хочу́",
        "explanation": "<p><em>Хоте́ть</em> birlikda <strong>Ч</strong> bilan boradi: "
                       "<em>хочу́, хо́чешь, хо́чет</em>. Koʻplikda esa <strong>Т</strong>: "
                       "<em>хоти́м, хоти́те, хотя́т</em>. Bu — rus tilidagi deyarli "
                       "yagona feʼl, u guruhini gap oʻrtasida almashtiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ пло́в.</strong> "
                "(есть)</p>",
        "choices": ["е́дут", "естя́т", "е́сят", "едя́т"],
        "correct": "едя́т",
        "explanation": "<p><em>Есть</em> (yemoq) — alohida turadigan feʼl: <em>ем, ешь, "
                       "ест, еди́м, еди́те, едя́т</em>. <strong>Е́дут</strong> esa "
                       "butunlay boshqa feʼl — <em>е́хать</em> (transportda ketmoq). "
                       "Ovoz chiqarib ayting: [йидя́т] — [йе́дут].</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ письмо́.</strong> "
                "(писа́ть)</p>",
        "choices": ["писа́ет", "пи́шет", "пи́шит", "писа́т"],
        "correct": "пи́шет",
        "explanation": "<p>Oʻzakda <strong>С → Ш</strong> almashinuvi boʻladi va u "
                       "<em>hamma</em> shaklda saqlanadi: <em>пишу́, пи́шешь, пи́шет, "
                       "пи́шем, пи́шете, пи́шут</em>. Bu PR-21 dagi «faqat я shaklida» "
                       "almashinuvdan farq qiladi.</p>",
    },
    {
        "text": "<p><strong>дать</strong> feʼlining «я» shakli qaysi?</p>",
        "choices": ["даю́", "да́ю", "дам", "да́ю́т"],
        "correct": "дам",
        "explanation": "<p><em>Дать</em> — <em>есть</em> ning jufti va shu bilan birga "
                       "yodlanadi: <em>дам/ем, дашь/ешь, даст/ест, дади́м/еди́м, "
                       "дади́те/еди́те, даду́т/едя́т</em>. <em>Даю́</em> boshqa feʼlga "
                       "tegishli — <em>дава́ть</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ в Самарка́нде.</strong> "
                "(жить)</p>",
        "choices": ["живе́м", "живём", "жи́вем", "живя́м"],
        "correct": "живём",
        "explanation": "<p>Urgʻu qoʻshimchaga tushgani uchun <strong>Е → Ё</strong> "
                       "boʻladi (PR-2). Solishtiring: <em>чит<strong>а́</strong>ем</em> "
                       "— urgʻu oʻzakda, Е qoladi; <em>жив<strong>ём</strong></em> — "
                       "urgʻu qoʻshimchada, Ё boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ ко́фе.</strong> "
                "(хоте́ть)</p>",
        "choices": ["хо́чут", "хочу́т", "хотя́т", "хо́чат"],
        "correct": "хотя́т",
        "explanation": "<p>Koʻplikda <em>хоте́ть</em> II tuslanishga oʻtadi: "
                       "<strong>хотя́т</strong>. <em>Хо́чут</em> — ruslar ham baʼzan "
                       "qiladigan xato, lekin u adabiy tilda notoʻgʻri. Chegarani "
                       "yodlang: birlik = Ч, koʻplik = Т.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ___ чай и́ли "
                "ко́фе?</strong> (пить)</p>",
        "choices": ["пие́шь", "пьёшь", "пьешь", "пи́шешь"],
        "correct": "пьёшь",
        "explanation": "<p><em>Пить</em> → <em>пью, пьёшь, пьёт, пьём, пьёте, пьют</em>. "
                       "Oʻzakda <strong>Ь</strong> paydo boʻladi va urgʻu qoʻshimchada, "
                       "demak <strong>Ё</strong>. <em>Пи́шешь</em> — boshqa feʼl "
                       "(<em>писа́ть</em>), ehtiyot boʻling.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Куда́ вы ___?</strong> "
                "(идти́)</p>",
        "choices": ["идёте", "иде́те", "иду́ете", "идти́те"],
        "correct": "идёте",
        "explanation": "<p>Oʻzak <strong>ид-</strong>, urgʻu qoʻshimchada — demak "
                       "<strong>Ё</strong>: <em>иду́, идёшь, идёт, идём, идёте, иду́т</em>. "
                       "<em>Куда́?</em> — «qayerga?» degani, va u harakat feʼli bilan "
                       "keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ пло́в ка́ждую "
                "суббо́ту.</strong> (есть)</p>",
        "choices": ["е́дем", "еди́м", "е́сем", "ем"],
        "correct": "еди́м",
        "explanation": "<p>Koʻplikda <em>есть</em> ning oʻzagi uzayadi: "
                       "<strong>ед-</strong> — <em>еди́м, еди́те, едя́т</em>. "
                       "<em>Е́дем</em> esa <em>е́хать</em> dan — «biz ketyapmiz». "
                       "Bu ikki feʼl doim yonma-yon tekshiriladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на ___ в Москву́.</strong> "
                "(idish: piyoda emas, poyezdda)</p>",
        "choices": ["идёт", "хо́дит", "е́дет", "е́дит"],
        "correct": "е́дет",
        "explanation": "<p>Transportda ketish — <strong>е́хать</strong>: <em>е́ду, "
                       "е́дешь, е́дет…</em>. Moskva uzoq, u yerga piyoda borilmaydi. "
                       "<em>Идти́</em> faqat oyoq bilan yurish uchun — oʻzbekchada "
                       "ikkalasi ham «bormoq» boʻlgani uchun bu farq oson "
                       "unutiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Жасу́р ___ есть.</strong> "
                "(хоте́ть)</p>",
        "choices": ["хо́чет", "хотя́т", "хо́чит", "хоти́т"],
        "correct": "хо́чет",
        "explanation": "<p><em>Жасу́р</em> — uchinchi shaxs birligi, demak "
                       "<strong>хо́чет</strong> (birlik = Ч). Ikkinchi feʼl esa "
                       "<strong>infinitiv</strong>da qoladi: <em>есть</em>. Gapda "
                       "faqat birinchi feʼl tuslanadi (PR-19).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Они́ едя́т. · Они́ "
                "е́дут.</strong></p>",
        "choices": ["Yeyaptilar · ketyaptilar", "Ketyaptilar · yeyaptilar",
                    "Ikkalasi «yeyaptilar»", "Ikkalasi «ketyaptilar»"],
        "correct": "Yeyaptilar · ketyaptilar",
        "explanation": "<p><strong>Едя́т</strong> — <em>есть</em> dan (yemoq), urgʻu "
                       "oxirida. <strong>Е́дут</strong> — <em>е́хать</em> dan "
                       "(transportda ketmoq), urgʻu boshida. Bitta harf va urgʻu "
                       "butun maʼnoni oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я иду́ в Москву́.", "Я е́ду в шко́лу пешко́м.",
                    "Я иду́ в шко́лу.", "Я е́ду пешко́м."],
        "correct": "Я иду́ в шко́лу.",
        "explanation": "<p>Maktab yaqin — piyoda, demak <strong>идти́</strong>. "
                       "«Я иду́ в Москву́» ruscha quloqqa «Moskvaga piyoda ketyapman» "
                       "boʻlib eshitiladi. <em>Пешко́м</em> = piyoda, shuning uchun u "
                       "<em>е́хать</em> bilan qoʻshilmaydi.</p>",
    },
    {
        "text": "<p><strong>хоте́ть</strong> feʼli haqida qaysi gap toʻgʻri?</p>",
        "choices": ["U har doim I tuslanishda", "U har doim II tuslanishda",
                    "Birlikda I, koʻplikda II tuslanishda", "U umuman tuslanmaydi"],
        "correct": "Birlikda I, koʻplikda II tuslanishda",
        "explanation": "<p><em>Хочу́, хо́чешь, хо́чет</em> — I tuslanish "
                       "qoʻshimchalari. <em>Хоти́м, хоти́те, хотя́т</em> — II "
                       "tuslanish. Shuning uchun uni «ikki guruhli feʼl» deb "
                       "ataydilar; rus tilida bunday feʼl deyarli bitta.</p>",
    },
    {
        "text": "<p>Nega bu shakllarda Е oʻrniga Ё yozilgan?</p><p><strong>живёшь · "
                "идёт · пьём</strong></p>",
        "choices": ["Chunki bu notoʻgʻri feʼllar", "Chunki urgʻu qoʻshimchaga tushgan",
                    "Chunki oʻzak yumshoq", "Chunki bu koʻplik"],
        "correct": "Chunki urgʻu qoʻshimchaga tushgan",
        "explanation": "<p>Yangi qoʻshimcha emas — bu oʻsha I tuslanish. PR-2 dagi qoida "
                       "ishlayapti: <strong>urgʻu ostida Е → Ё</strong> boʻladi. "
                       "Solishtiring: <em>чита́ешь</em> (urgʻu oʻzakda) — "
                       "<em>живёшь</em> (urgʻu qoʻshimchada).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мы живём в Ташке́нте.", "Он пи́шет письмо́.",
                    "Ты пьёшь чай.", "Они́ хо́чут пло́в."],
        "correct": "Они́ хо́чут пло́в.",
        "explanation": "<p>Toʻgʻrisi — <strong>Они́ хотя́т пло́в</strong>. Koʻplikda "
                       "<em>хоте́ть</em> II tuslanishga oʻtadi va <strong>Т</strong> "
                       "bilan boradi. Qolgan uchtasi toʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я дам кни́гу.", "Я даст кни́гу.",
                    "Я дади́м кни́гу.", "Я дашь кни́гу."],
        "correct": "Я дам кни́гу.",
        "explanation": "<p><em>Дать</em>: <strong>дам</strong>, дашь, даст, дади́м, "
                       "дади́те, даду́т. «Я» uchun — <strong>дам</strong>. Qolganlarida "
                       "boshqa shaxsning shakli «я» ga qoʻyilgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Куда́ ты идёшь?</strong></p>",
        "choices": ["— Я иду́ домо́й.", "— Я иду́ до́ма.",
                    "— Я е́ду пешко́м.", "— Я идёшь домо́й."],
        "correct": "— Я иду́ домо́й.",
        "explanation": "<p><strong>Домо́й</strong> = «uyga» (harakat), <strong>до́ма</strong> "
                       "= «uyda» (joy). Savol <em>куда́?</em> — yaʼni harakat haqida, "
                       "demak <em>домо́й</em>. Ikkalasi ham ravish va hech qachon "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ular choy ichishni "
                "xohlaydilar.</strong></p>",
        "choices": ["Они́ хотя́т пить чай.", "Они́ хотя́т пьют чай.",
                    "Они́ хо́чет пить чай.", "Они́ хоти́м пить чай."],
        "correct": "Они́ хотя́т пить чай.",
        "explanation": "<p>Birinchi feʼl tuslanadi — <strong>хотя́т</strong> (koʻplik, "
                       "demak Т). Ikkinchisi <strong>infinitiv</strong>da qoladi — "
                       "<em>пить</em>, xuddi oʻzbekchadagi «ich<strong>ish</strong>ni "
                       "xohlaydilar» kabi.</p>",
    },
]


# =====================================================================
# PR-23 — Oʻtgan zamon: -л, -ла, -ло, -ли
# =====================================================================

Q_PR23 = [
    # 1–5 tanish
    {
        "text": "<p>Oʻtgan zamon qanday yasaladi?</p>",
        "choices": ["Infinitiv + -л/-ла/-ло/-ли", "Infinitiv minus -ть + -л/-ла/-ло/-ли",
                    "Oʻzak + -ю/-ешь/-ет", "Feʼl oldiga «был» qoʻyiladi"],
        "correct": "Infinitiv minus -ть + -л/-ла/-ло/-ли",
        "explanation": "<p><em>Чита́ть → чита́- → чита́л</em>. Oʻsha oʻzak, PR-20 dagi. "
                       "Shundan keyin egaga qarab unli qoʻshiladi: erkak "
                       "<strong>-л</strong>, ayol <strong>-ла</strong>, oʻrta "
                       "<strong>-ло</strong>, koʻplik <strong>-ли</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на ___ вчера́.</strong> "
                "(рабо́тать)</p>",
        "choices": ["рабо́тал", "рабо́тала", "рабо́тало", "рабо́тали"],
        "correct": "рабо́тала",
        "explanation": "<p>Afsona — qiz, demak <strong>-ла</strong>. Rus tilida oʻtgan "
                       "zamon feʼli <strong>jinsga</strong> qaraydi. Oʻzbek oʻquvchi "
                       "eng koʻp shu yerda xato qiladi, chunki oʻzbekchada feʼl jinsni "
                       "hech qachon koʻrsatmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ до́ма.</strong> "
                "(быть)</p>",
        "choices": ["был", "была́", "бы́ло", "бы́ли"],
        "correct": "бы́ли",
        "explanation": "<p>Koʻplik uchun har doim <strong>-ли</strong>, jinsdan qatʼi "
                       "nazar. Va eʼtibor bering: hozirgi zamonda «быть» aytilmaydi "
                       "(<em>Мы до́ма</em>), oʻtgan zamonda esa u majburiy "
                       "(<em>Мы бы́ли до́ма</em>).</p>",
    },
    {
        "text": "<p><strong>идти́</strong> feʼlining oʻtgan zamon shakli qaysi?</p>",
        "choices": ["идёл", "и́дл", "шёл", "идти́л"],
        "correct": "шёл",
        "explanation": "<p><strong>Шёл — шла — шло — шли</strong>: infinitiv bilan "
                       "bitta ham umumiy harfi yoʻq, shuning uchun alohida yodlanadi. "
                       "Bu rus tilidagi eng koʻp uchraydigan notoʻgʻri shakl.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вчера́ ___ дождь.</strong></p>",
        "choices": ["шёл", "шла", "шли", "ходи́л"],
        "correct": "шёл",
        "explanation": "<p>Ruschada yomgʻir «yogʻmaydi» — u <strong>yuradi</strong>: "
                       "<em>шёл дождь</em>, <em>шёл снег</em>. <em>Дождь</em> undosh "
                       "bilan tugaydi, demak erkak jinsi — <strong>шёл</strong>. Bu "
                       "iborani butunligicha yodlang.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Жасу́р ___ фильм.</strong> "
                "(смотре́ть)</p>",
        "choices": ["смотре́ла", "смотре́л", "смо́трил", "смотре́ли"],
        "correct": "смотре́л",
        "explanation": "<p>Jasur — yigit, demak <strong>-л</strong>. Va diqqat qiling: "
                       "hozirgi zamondagi ikki tuslanish farqi oʻtgan zamonda "
                       "<strong>umuman yoʻq</strong> — oʻzak infinitivdagidek qoladi: "
                       "<em>смотре́-л</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дилно́за ___ чай.</strong> "
                "(пить)</p>",
        "choices": ["пил", "пи́ла", "пила́", "пи́ли"],
        "correct": "пила́",
        "explanation": "<p>Dilnoza — qiz, demak <strong>-ла</strong>, va urgʻu "
                       "<strong>oxirida</strong>: <em>пила́</em>. Bu qadimiy feʼllarning "
                       "naqshi: <em>была́, жила́, дала́, пила́</em> — ayol jinsi urgʻuni "
                       "oxiriga tortadi, erkak va koʻplikda esa urgʻu joyida qoladi "
                       "(<em>пил, пи́ли</em>).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ пло́в вме́сте.</strong> "
                "(есть)</p>",
        "choices": ["е́ли", "едя́ли", "е́хали", "ел"],
        "correct": "е́ли",
        "explanation": "<p><em>Есть</em> ning oʻtgan zamoni qisqa, lekin qoidali: "
                       "<em>ел, е́ла, е́ло, е́ли</em>. <strong>Е́хали</strong> esa "
                       "boshqa feʼl — «ketishardi». Hozirgi zamonda ular "
                       "<em>едя́т / е́дут</em> boʻlib chalkashadi, oʻtgan zamonda "
                       "<em>е́ли / е́хали</em> boʻlib.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мари́на Оле́говна, вы "
                "___ э́ту кни́гу?</strong> (чита́ть)</p>",
        "choices": ["чита́ла", "чита́л", "чита́ли", "чита́ло"],
        "correct": "чита́ли",
        "explanation": "<p>Gap bitta ayolga aytilyapti, lekin <strong>вы</strong> har "
                       "doim koʻplik shaklini oladi — demak <strong>-ли</strong>. Bu "
                       "hurmat shakli, PR-7 dagi qoida oʻtgan zamonda ham "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то ___ о́чень "
                "интере́сно.</strong> (быть)</p>",
        "choices": ["был", "была́", "бы́ло", "бы́ли"],
        "correct": "бы́ло",
        "explanation": "<p><em>Э́то</em> — oʻrta jins, demak <strong>бы́ло</strong>. "
                       "Oʻrta jins shakli kamdan-kam kerak boʻladi, lekin aynan "
                       "<em>э́то бы́ло…</em> iborasi juda koʻp uchraydi: "
                       "<em>Э́то бы́ло тру́дно. Э́то бы́ло вчера́.</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д ___ до́ма и не "
                "___.</strong> (быть · спать)</p>",
        "choices": ["был · спал", "была́ · спала́", "бы́ли · спа́ли", "был · спа́ли"],
        "correct": "был · спал",
        "explanation": "<p>Bekzod — bola, demak ikkala feʼl ham <strong>-л</strong>. "
                       "Bitta gapdagi hamma oʻtgan zamon feʼli bitta egaga qaraydi va "
                       "bir xil jinsda boʻladi — buni tekshirish yaxshi odat.</p>",
    },
    {
        "text": "<p>Bu feʼlning oʻtgan zamon shakli qaysi?</p><p><strong>хоте́ть</strong>, "
                "ega — <strong>Катя</strong></p>",
        "choices": ["хо́чела", "хоте́ла", "хоти́ла", "хотя́ла"],
        "correct": "хоте́ла",
        "explanation": "<p>Hozirgi zamondagi <em>хочу́ / хо́чешь / хотя́т</em> chalkashligi "
                       "oʻtgan zamonda butunlay yoʻqoladi: oʻzak infinitivdagidek "
                       "qoladi — <em>хоте́л, хоте́ла, хоте́ли</em>. Oʻtgan zamon rus "
                       "feʼl tizimining eng osoni.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Rus tilida oʻtgan zamon feʼli nimani koʻrsatadi?</p>",
        "choices": ["Shaxsni (men / sen / u)", "Jinsni va sonni",
                    "Ikkalasini ham", "Hech narsani"],
        "correct": "Jinsni va sonni",
        "explanation": "<p>Bu oʻzbekchaning <strong>teskarisi</strong>. Oʻzbekcha "
                       "<em>oʻqi<strong>di</strong>m / oʻqi<strong>di</strong>ng</em> — "
                       "shaxs koʻrinadi, jins koʻrinmaydi. Ruscha <em>чита́л / "
                       "чита́ла</em> — jins koʻrinadi, shaxs koʻrinmaydi. Shuning uchun "
                       "ruschada olmoshni tushirib qoldirmaslik kerak.</p>",
    },
    {
        "text": "<p>Bu ikki shaklning farqi nima?</p><p><strong>шёл · шла</strong></p>",
        "choices": ["Erkak · ayol", "Ayol · erkak",
                    "Birlik · koʻplik", "Hozirgi · oʻtgan zamon"],
        "correct": "Erkak · ayol",
        "explanation": "<p><em>Идти́</em> ning oʻtgan zamoni: <strong>шёл</strong> "
                       "(erkak), <strong>шла</strong> (ayol), <em>шло</em> (oʻrta), "
                       "<strong>шли</strong> (koʻplik). Erkak shaklidagi <strong>Ё</strong> "
                       "faqat shu yerda paydo boʻladi — qolganlarida oddiy "
                       "<em>ш-</em>.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda urgʻu toʻgʻri qoʻyilgan?</p>",
        "choices": ["был — бы́ла", "бы́л — была́", "был — была́", "бы́л — бы́ла"],
        "correct": "был — была́",
        "explanation": "<p><strong>Был</strong> bir boʻgʻinli — urgʻu belgisi umuman "
                       "qoʻyilmaydi. <strong>Была́</strong> da urgʻu oxirida. "
                       "Bu naqsh <em>бы́ло, бы́ли</em> da yana boshiga qaytadi — faqat "
                       "ayol jinsi shakli urgʻuni tortadi.</p>",
    },
    {
        "text": "<p>Qaysi gapda oʻtgan zamon kerak?</p>",
        "choices": ["Сейча́с я до́ма.", "Ка́ждый день я рабо́таю.",
                    "Вчера́ я не рабо́тал.", "Я хорошо́ понима́ю."],
        "correct": "Вчера́ я не рабо́тал.",
        "explanation": "<p><em>Вчера́</em> — «kecha», va u oʻtgan zamon talab qiladi. "
                       "Oʻzbek oʻquvchi koʻpincha «Вчера́ я не рабо́таю» deb yozadi, "
                       "chunki oʻzbekchada vaqt soʻzi feʼlga bunchalik qattiq bogʻlanmaydi. "
                       "Vaqt soʻzi va feʼl zamoni doim mos boʻlishi kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Жасу́р чита́л кни́гу.", "Мы бы́ли в шко́ле.",
                    "Афсо́на чита́л кни́гу.", "Она́ была́ до́ма."],
        "correct": "Афсо́на чита́л кни́гу.",
        "explanation": "<p>Toʻgʻrisi — <strong>Афсо́на чита́ла</strong>. Afsona qiz, "
                       "demak <strong>-ла</strong>. Bu Prime Russian'dagi eng koʻp "
                       "uchraydigan xato: oʻzbek oʻquvchi jinsni umuman payqamaydi. "
                       "Har safar soʻrang: <strong>ega erkakmi, ayolmi, "
                       "koʻplikmi?</strong></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Она́ идла́ домо́й.", "Она́ ходи́ла домо́й вчера́ у́тром.",
                    "Она́ шла домо́й.", "Она́ шёл домо́й."],
        "correct": "Она́ шла домо́й.",
        "explanation": "<p><em>Идти́</em> ning oʻtgan zamoni — <strong>шёл / шла / "
                       "шли</strong>. <em>Идла́</em> degan shakl umuman yoʻq. "
                       "<em>Шёл</em> — erkak shakli, «она́» ga toʻgʻri kelmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Javob beruvchi — <strong>qiz</strong>.</p>"
                "<p><strong>— Ты была́ вчера́ в шко́ле?</strong></p>",
        "choices": ["— Да, я был.", "— Да, я была́.",
                    "— Да, я бы́ли.", "— Да, я есть."],
        "correct": "— Да, я была́.",
        "explanation": "<p>Javob beruvchi qiz, demak <strong>была́</strong> — urgʻu "
                       "oxirida. Savolning oʻzi ham buni koʻrsatib turibdi: «Ты "
                       "<strong>была́</strong>?» degan savol qizga berilgan.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring. Gapirayotgan odam — "
                "<strong>qiz</strong>.</p><p><strong>Kecha uyda edim va kitob "
                "oʻqidim.</strong></p>",
        "choices": ["Вчера́ я до́ма и чита́ла кни́гу.",
                    "Вчера́ я был до́ма и чита́л кни́гу.",
                    "Вчера́ я была́ до́ма и чита́ла кни́гу.",
                    "Вчера́ я была́ до́ма и чита́л кни́гу."],
        "correct": "Вчера́ я была́ до́ма и чита́ла кни́гу.",
        "explanation": "<p>Uchta narsa bir vaqtda toʻgʻri boʻlishi kerak: "
                       "<strong>быть</strong> tushirilmaydi (oʻtgan zamonda u "
                       "majburiy), ikkala feʼl ham <strong>-ла</strong> (gapirayotgan "
                       "odam qiz), va <em>была́</em> da urgʻu oxirida.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-21 Mashq: II tuslanish: говорить, смотреть, любить",
        "description": (
            "Ikkinchi tuslanish qoʻshimchalari, «я» shaklidagi harf almashinuvi "
            "(люблю́, хожу́, ви́жу) va feʼl qaysi guruhda ekanini aniqlash."
        ),
        "tutorial": "PR-21:",
        "questions": Q_PR21,
    },
    {
        "title": "PR-22 Mashq: Notoʻgʻri feʼllar: хотеть, есть, дать, идти, ехать, жить, писать",
        "description": (
            "Rus tilining eng koʻp ishlatiladigan — va eng notoʻgʻri — feʼllari. "
            "Есть/дать juftligi, хоте́ть ning ikki guruhi, идти́ va е́хать farqi."
        ),
        "tutorial": "PR-22:",
        "questions": Q_PR22,
    },
    {
        "title": "PR-23 Mashq: Oʻtgan zamon — jinsga qarab -л, -ла, -ло, -ли",
        "description": (
            "Oʻtgan zamonning toʻrtta shakli, был/была́/бы́ло/бы́ли, шёл/шла/шли "
            "va oʻzbek oʻquvchi uchun eng qiyin joyi — jinsga moslashish."
        ),
        "tutorial": "PR-23:",
        "questions": Q_PR23,
    },
]
