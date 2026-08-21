# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-47 … PR-49.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_47_49.py --master=prime \\
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
# PR-47 — Soʻroq soʻzlarining kelishiklari
# =====================================================================

Q_PR47 = [
    # 1–5 tanish
    {
        "text": "<p>Soʻroq soʻzining kelishigini nima belgilaydi?</p>",
        "choices": ["Savolning uzunligi", "Javob kutilayotgan kelishik",
                    "Gapdagi oʻrni", "Feʼlning zamoni"],
        "correct": "Javob kutilayotgan kelishik",
        "explanation": "<p><em>Кому́ ты пи́шешь? — Бра́ту.</em> Savol va javob bir xil "
                       "kelishikda. Shaklni bilmasangiz, savolni ayting va uning "
                       "shaklini koʻchiring.</p>",
    },
    {
        "text": "<p><strong>кто</strong> soʻzining Вини́тельный shakli qaysi?</p>",
        "choices": ["кто", "кого́", "кому́", "кем"],
        "correct": "кого́",
        "explanation": "<p><em>Кто</em> jonli otlar kabi turlanadi: Р.п. = В.п. = "
                       "<strong>кого́</strong>. <em>Что</em> esa jonsizlar kabi: Р.п. "
                       "<em>чего́</em>, lekin В.п. <em>что</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ты пи́шешь?</strong> "
                "(javob: бра́ту)</p>",
        "choices": ["Кто", "Кого́", "Кому́", "Кем"],
        "correct": "Кому́",
        "explanation": "<p>Javob <em>бра́ту</em> — Да́тельный, demak savol ham: "
                       "<strong>кому́</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ты идёшь?</strong> "
                "(javob: с бра́том)</p>",
        "choices": ["Кто", "Кем", "С кем", "О ком"],
        "correct": "С кем",
        "explanation": "<p>Predlog ham savoldan javobga koʻchadi: <em>с кем? — с "
                       "бра́том</em>. Faqat <em>кем</em> boʻlsa, predlog "
                       "yetishmasdi.</p>",
    },
    {
        "text": "<p><strong>чей</strong> nima degani?</p>",
        "choices": ["qanday?", "kimniki?", "qancha?", "qayerda?"],
        "correct": "kimniki?",
        "explanation": "<p><em>Чей э́то дом?</em> — «Bu kimning uyi?» U otga jins va "
                       "son boʻyicha moslashadi: <em>чей, чья, чьё, чьи</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu javobga savol tuzing.</p><p><strong>— О бра́те.</strong></p>",
        "choices": ["Кто?", "Кого́?", "О ком?", "Кому́?"],
        "correct": "О ком?",
        "explanation": "<p>Javob Предло́жный'da va predlog bilan, demak savol ham: "
                       "<strong>о ком?</strong></p>",
    },
    {
        "text": "<p>Bu javobga savol tuzing.</p><p><strong>— У бра́та.</strong></p>",
        "choices": ["У кого́?", "Кому́?", "Кого́?", "С кем?"],
        "correct": "У кого́?",
        "explanation": "<p>Javob <em>у</em> + Роди́тельный, demak savol ham: "
                       "<strong>у кого́?</strong> Bu «kimda bor?» degan savol.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ э́та кни́га?</strong> "
                "(javob: о дру́жбе)</p>",
        "choices": ["О чём", "О ком", "Что", "Чего́"],
        "correct": "О чём",
        "explanation": "<p>Javob narsa haqida (<em>о дру́жбе</em>), demak "
                       "<strong>о чём</strong>. Odam haqida boʻlsa — <em>о "
                       "ком</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ э́то ключи́?</strong></p>",
        "choices": ["Чей", "Чья", "Чьё", "Чьи"],
        "correct": "Чьи",
        "explanation": "<p><em>Ключи́</em> — koʻplik, demak <strong>чьи</strong>. "
                       "<em>Чей</em> otga moslashadi, xuddi <em>мой</em> kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ книг ты "
                "чита́ешь?</strong></p>",
        "choices": ["Ско́лько", "Каки́е", "Чьи", "Что"],
        "correct": "Ско́лько",
        "explanation": "<p><strong>Ско́лько</strong> dan keyin Роди́тельный keladi — "
                       "va bu yerda koʻplik: <em>книг</em> (PR-36).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>С ___ ты "
                "рабо́таешь?</strong></p>",
        "choices": ["кто", "кого́", "кем", "кому́"],
        "correct": "кем",
        "explanation": "<p><em>С</em> Твори́тельный oladi (PR-39), <em>кто</em> ning "
                       "Твори́тельный shakli — <strong>кем</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ты ждёшь?</strong> "
                "(javob: Афсо́ну)</p>",
        "choices": ["Кто", "Кого́", "Кому́", "Кем"],
        "correct": "Кого́",
        "explanation": "<p>Javob Вини́тельный'da (<em>Афсо́ну</em>), demak savol ham: "
                       "<strong>кого́</strong>. <em>«Кто ты ждёшь?»</em> — eng koʻp "
                       "uchraydigan xato.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega <strong>кто</strong> va <strong>что</strong> boshqacha "
                "turlanadi?</p>",
        "choices": ["Кто jonli, что jonsiz — PR-32 dagi qoida",
                    "Кто koʻplik, что birlik",
                    "Кто erkak jinsida",
                    "Ular bir xil turlanadi"],
        "correct": "Кто jonli, что jonsiz — PR-32 dagi qoida",
        "explanation": "<p><em>Кто</em>: Р.п. = В.п. = <em>кого́</em>. <em>Что</em>: "
                       "Р.п. <em>чего́</em>, lekin В.п. <em>что</em>. Jonlilik "
                       "qoidasi soʻroq soʻzlarida ham ishlaydi.</p>",
    },
    {
        "text": "<p><strong>како́й</strong> qanday turlanadi?</p>",
        "choices": ["Ot kabi", "Sifat kabi", "Feʼl kabi", "Turlanmaydi"],
        "correct": "Sifat kabi",
        "explanation": "<p><em>како́го, како́му, каки́м, о како́м</em> — bu sifat "
                       "qoʻshimchalari. Va ayol jinsida <em>како́й</em> toʻrtta "
                       "kelishikda ishlatiladi, xuddi <em>но́вой</em> kabi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida soʻroq soʻzlari turlanadimi?</p>",
        "choices": ["Yoʻq", "Ha — kim, kimning, kimga, kimni, kimda, kimdan",
                    "Faqat koʻplikda", "Faqat «nima» soʻzi"],
        "correct": "Ha — kim, kimning, kimga, kimni, kimda, kimdan",
        "explanation": "<p>Va eng muhimi: oʻzbekchada ham savol va javob bir xil "
                       "kelishikda boʻladi. «Kim<strong>ga</strong> yozding?» — "
                       "«Aka<strong>mga</strong>». Bugungi qoida siz uchun "
                       "tabiiy.</p>",
    },
    {
        "text": "<p>Bu ikki savolning farqi nima?</p><p><strong>О ком? · О чём?</strong></p>",
        "choices": ["Odam haqida · narsa haqida", "Narsa haqida · odam haqida",
                    "Ikkalasi bir xil", "Birinchisi koʻplik"],
        "correct": "Odam haqida · narsa haqida",
        "explanation": "<p><em>О ком ты ду́маешь? — О ба́бушке.</em> <em>О чём э́та "
                       "кни́га? — О дру́жбе.</em> Farq jonlilikda.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi savolda xato bor?</p>",
        "choices": ["Кому́ ты звони́шь?", "О чём вы говори́те?",
                    "Кто ты ждёшь?", "С кем она́ рабо́тает?"],
        "correct": "Кто ты ждёшь?",
        "explanation": "<p>Toʻgʻrisi — <strong>Кого́ ты ждёшь?</strong> Javob "
                       "Вини́тельный'da boʻlardi (<em>бра́та</em>), demak savol ham "
                       "shu kelishikda.</p>",
    },
    {
        "text": "<p>Qaysi savol toʻgʻri?</p>",
        "choices": ["Чей э́то кни́га?", "Чья э́то кни́га?",
                    "Чьё э́то кни́га?", "Чьи э́то кни́га?"],
        "correct": "Чья э́то кни́га?",
        "explanation": "<p><em>Кни́га</em> — ayol jinsida, demak "
                       "<strong>чья</strong>. <em>Чей</em> otga jins va son boʻyicha "
                       "moslashadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu javobga savol tuzing.</p><p><strong>— Ру́чкой.</strong></p>",
        "choices": ["Чем?", "Что?", "Чего́?", "О чём?"],
        "correct": "Чем?",
        "explanation": "<p>Javob Твори́тельный'da va predlogsiz (asbob, PR-39), demak "
                       "savol <strong>чем?</strong> — «nima bilan?»</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Kim bilan ishlaysan va "
                "kimga yozasan?</strong></p>",
        "choices": ["Кто ты рабо́таешь и кто ты пи́шешь?",
                    "С кем ты рабо́таешь и кому́ ты пи́шешь?",
                    "Кем ты рабо́таешь и кому́ ты пи́шешь?",
                    "С кем ты рабо́таешь и кого́ ты пи́шешь?"],
        "correct": "С кем ты рабо́таешь и кому́ ты пи́шешь?",
        "explanation": "<p>Ikkita boshqa kelishik: <em>рабо́тать с кем</em> — "
                       "Твори́тельный predlog bilan; <em>писа́ть кому́</em> — "
                       "Да́тельный. Oʻzbekcha «kim <strong>bilan</strong>» va "
                       "«kim<strong>ga</strong>» ikkalasini ham koʻrsatib "
                       "turibdi.</p>",
    },
]


# =====================================================================
# PR-48 — Predlog xaritasi
# =====================================================================

Q_PR48 = [
    # 1–5 tanish
    {
        "text": "<p>Qaysi kelishik eng koʻp predlog oladi?</p>",
        "choices": ["Да́тельный", "Роди́тельный", "Вини́тельный", "Предло́жный"],
        "correct": "Роди́тельный",
        "explanation": "<p>Toʻqqizta: <em>из, с, от, до, у, без, для, о́коло, "
                       "по́сле</em>. Shuning uchun u rus tilidagi eng koʻp "
                       "uchraydigan kelishik.</p>",
    },
    {
        "text": "<p><strong>Да́тельный</strong> qaysi predloglarni oladi?</p>",
        "choices": ["в va на", "к va по", "из va от", "над va под"],
        "correct": "к va по",
        "explanation": "<p>Faqat ikkitasi — bu roʻyxatni yodlash bir daqiqa vaqt "
                       "oladi: <em>к бра́ту</em>, <em>по у́лице</em>.</p>",
    },
    {
        "text": "<p>Qaysi kelishik hech qachon predlog bilan kelmaydi?</p>",
        "choices": ["Имени́тельный", "Роди́тельный", "Твори́тельный", "Предло́жный"],
        "correct": "Имени́тельный",
        "explanation": "<p>Bosh kelishik gapning egasi, va ega predlog olmaydi. "
                       "Aksincha — <strong>Предло́жный</strong> hech qachon predlogsiz "
                       "kelmaydi (shuning uchun uning nomi shunday).</p>",
    },
    {
        "text": "<p>Bu ikki iboraning farqi nima?</p><p><strong>за до́мом · за "
                "дом</strong></p>",
        "choices": ["Uy orqasida · uy orqasiga", "Uy orqasiga · uy orqasida",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Uy orqasida · uy orqasiga",
        "explanation": "<p><em>За до́мом</em> — Твори́тельный, harakat yoʻq. "
                       "<em>За дом</em> — Вини́тельный, harakat bor. Bir xil predlog, "
                       "ikki kelishik.</p>",
    },
    {
        "text": "<p><strong>по</strong> qaysi kelishikni oladi?</p>",
        "choices": ["Предло́жный", "Вини́тельный", "Да́тельный", "Роди́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>по у́лице, по го́роду, по телефо́ну</em> — hammasi "
                       "Да́тельный. Bu <em>к</em> bilan birga ikkita Да́тельный "
                       "predlogidan biri.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu iboraning antonimini toping.</p><p><strong>в шко́лу</strong></p>",
        "choices": ["с шко́лы", "из шко́лы", "от шко́лы", "по шко́ле"],
        "correct": "из шко́лы",
        "explanation": "<p><em>Шко́ла</em> В oladi, demak «dan» uchun "
                       "<strong>из</strong>. Antonim juftlik: <em>в ↔ из</em>.</p>",
    },
    {
        "text": "<p>Bu iboraning antonimini toping.</p><p><strong>на рабо́ту</strong></p>",
        "choices": ["из рабо́ты", "с рабо́ты", "от рабо́ты", "до рабо́ты"],
        "correct": "с рабо́ты",
        "explanation": "<p><em>Рабо́та</em> НА oladi, demak «dan» uchun "
                       "<strong>с</strong>. Antonim juftlik: <em>на ↔ с</em>.</p>",
    },
    {
        "text": "<p>Bu iboraning antonimini toping.</p><p><strong>к врачу́</strong></p>",
        "choices": ["из врача́", "с врача́", "от врача́", "по врачу́"],
        "correct": "от врача́",
        "explanation": "<p>Odam tomon — <em>к</em> (Д.п.), odamdan — <strong>от</strong> "
                       "(Р.п.). Uchinchi antonim juftlik.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Кни́га лежи́т ___ "
                "столо́м.</strong></p>",
        "choices": ["на", "в", "под", "за"],
        "correct": "под",
        "explanation": "<p><em>Столо́м</em> — Твори́тельный shakli, demak predlog ham "
                       "shu kelishikni oladigan boʻlishi kerak: <em>под, над, за, "
                       "пе́ред</em>. Mantiqan <strong>под</strong> — «stol "
                       "tagida».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___ "
                "мост.</strong> («koʻprikdan oʻtib» maʼnosida)</p>",
        "choices": ["в", "на", "че́рез", "по"],
        "correct": "че́рез",
        "explanation": "<p><strong>Че́рез</strong> Вини́тельный oladi va «kesib "
                       "oʻtish» maʼnosini beradi: <em>че́рез мост, че́рез "
                       "у́лицу</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я живу́ в ___.</strong> "
                "(го́род)</p>",
        "choices": ["го́род", "го́рода", "го́роде", "го́родом"],
        "correct": "го́роде",
        "explanation": "<p><em>Жить</em> harakat emas, demak joy kelishigi — "
                       "Предло́жный: <strong>в го́роде</strong>. <em>В го́род</em> "
                       "harakat bilan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Магази́н ___ "
                "ры́нком.</strong></p>",
        "choices": ["за", "в", "из", "до"],
        "correct": "за",
        "explanation": "<p><em>Ры́нком</em> — Твори́тельный, demak predlog "
                       "<strong>за</strong> (yoki <em>над, под, пе́ред</em>). Maʼno "
                       "boʻyicha: «bozor orqasida».</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Uchta predlog ikki kelishik oladi. Qaysilar?</p>",
        "choices": ["в, на, за", "к, по, о", "из, от, до", "над, под, пе́ред"],
        "correct": "в, на, за",
        "explanation": "<p>Farqni <strong>harakat</strong> hal qiladi: harakat yoʻq → "
                       "joy kelishigi (<em>в шко́ле, за до́мом</em>), harakat bor → "
                       "Вини́тельный (<em>в шко́лу, за дом</em>).</p>",
    },
    {
        "text": "<p>Predloglarni qanday yodlash tavsiya qilinadi?</p>",
        "choices": ["Yakka soʻz sifatida", "Butun ibora bilan va juftlab",
                    "Alifbo tartibida", "Faqat jadval boʻyicha"],
        "correct": "Butun ibora bilan va juftlab",
        "explanation": "<p><em>В шко́ле</em>, <em>на рабо́ту</em>, <em>под "
                       "столо́м</em> — butun boʻlak. Va juftlab: <em>в ↔ из</em>, "
                       "<em>на ↔ с</em>, <em>к ↔ от</em>.</p>",
    },
    {
        "text": "<p>Oʻzbekcha va ruscha predloglarning farqi nima?</p>",
        "choices": ["Oʻzbekchada soʻzdan keyin, ruschada oldin — va ruschada ot ham oʻzgaradi",
                    "Oʻzbekchada predlog umuman yoʻq",
                    "Ruschada ot oʻzgarmaydi",
                    "Farq yoʻq"],
        "correct": "Oʻzbekchada soʻzdan keyin, ruschada oldin — va ruschada ot ham oʻzgaradi",
        "explanation": "<p><em>maktab<strong>ga</strong></em> · <em><strong>в</strong> "
                       "шко́л<strong>у</strong></em>. Ruscha maʼlumotni ikki joyda "
                       "koʻrsatadi — shuning uchun xato qilish qiyinroq.</p>",
    },
    {
        "text": "<p>Qaysi feʼl «joy kelishigi» ni talab qiladi?</p>",
        "choices": ["идти́", "е́хать", "жить", "класть"],
        "correct": "жить",
        "explanation": "<p><em>Жить, быть, рабо́тать, стоя́ть, лежа́ть</em> — harakat "
                       "emas, demak joy kelishigi. <em>Идти́, е́хать, класть</em> — "
                       "harakat, demak Вини́тельный.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я живу́ в го́роде.", "Я иду́ в го́род.",
                    "Кни́га лежи́т под стол.", "Мы идём к врачу́."],
        "correct": "Кни́га лежи́т под стол.",
        "explanation": "<p>Toʻgʻrisi — <strong>под столо́м</strong>. "
                       "<em>Лежа́ть</em> harakat emas, demak Твори́тельный kerak.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я иду́ по у́лицу.", "Я иду́ по у́лице.",
                    "Я иду́ по у́лицы.", "Я иду́ по у́лицей."],
        "correct": "Я иду́ по у́лице.",
        "explanation": "<p><strong>По</strong> har doim Да́тельный oladi, ayol jinsi "
                       "esa <strong>-е</strong>. Bu predlog boshqa kelishik "
                       "olmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Отку́да вы?</strong></p>",
        "choices": ["— Из Ташке́нта.", "— В Ташке́нте.",
                    "— К Ташке́нту.", "— По Ташке́нту."],
        "correct": "— Из Ташке́нта.",
        "explanation": "<p><em>Отку́да?</em> — «qayerdan?». Shahar В oladi, demak "
                       "«dan» uchun <strong>из</strong> + Роди́тельный.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ishdan uyga metroda "
                "boraman.</strong></p>",
        "choices": ["Из рабо́ты домо́й я е́ду на метро́.",
                    "С рабо́ты домо́й я е́ду на метро́.",
                    "С рабо́ты до́ма я е́ду в метро́.",
                    "От рабо́ты домо́й я е́ду на метро́."],
        "correct": "С рабо́ты домо́й я е́ду на метро́.",
        "explanation": "<p>Uchta qaror: <em>рабо́та</em> НА oladi → <strong>с "
                       "рабо́ты</strong>; «uyga» → <strong>домо́й</strong> (ravish); "
                       "vosita → <strong>на метро́</strong>.</p>",
    },
]


# =====================================================================
# PR-49 — Vaqt ifodalari
# =====================================================================

Q_PR49 = [
    # 1–5 tanish
    {
        "text": "<p>Hafta kuni qaysi kelishikda aytiladi?</p>",
        "choices": ["Предло́жный", "Вини́тельный", "Твори́тельный", "Роди́тельный"],
        "correct": "Вини́тельный",
        "explanation": "<p><em>в понеде́льник, в суббо́ту</em> — <em>в</em> + "
                       "Вини́тельный. Qisqa vaqt nuqta kabi koʻriladi.</p>",
    },
    {
        "text": "<p>Oy qaysi kelishikda aytiladi?</p>",
        "choices": ["Вини́тельный", "Предло́жный", "Твори́тельный", "Да́тельный"],
        "correct": "Предло́жный",
        "explanation": "<p><em>в ма́е, в январе́</em> — <em>в</em> + Предло́жный. "
                       "Uzun vaqt joy kabi koʻriladi: «uning ichida».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ здесь о́чень "
                "хо́лодно.</strong> (зима́)</p>",
        "choices": ["В зиме́", "В зи́му", "Зимо́й", "Зимы́"],
        "correct": "Зимо́й",
        "explanation": "<p>Fasllar predlogsiz, Твори́тельный'da: <em>зимо́й, "
                       "весно́й, ле́том, о́сенью</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он роди́лся в 2001 "
                "___.</strong> (год)</p>",
        "choices": ["год", "го́да", "го́де", "году́"],
        "correct": "году́",
        "explanation": "<p><em>Год</em> — PR-30 dagi <strong>-У́</strong> "
                       "roʻyxatidan, xuddi <em>в лесу́, на полу́</em> kabi. "
                       "<em>«В го́де»</em> — xato.</p>",
    },
    {
        "text": "<p>Nega <strong>во вто́рник</strong>, <em>«в вто́рник»</em> "
                "emas?</p>",
        "choices": ["Keyingi soʻz ikki undosh bilan boshlanadi",
                    "Chunki bu ikkinchi kun",
                    "Chunki «вто́рник» erkak jinsida",
                    "Bu istisno, qoidasi yoʻq"],
        "correct": "Keyingi soʻz ikki undosh bilan boshlanadi",
        "explanation": "<p><em>Вт-</em> — ikki undosh, shuning uchun predlogga unli "
                       "qoʻshiladi. Xuddi <em>во дворе́</em>, <em>со мной</em>, "
                       "<em>ко мне</em> kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Экза́мен ___.</strong> "
                "(суббо́та)</p>",
        "choices": ["в суббо́те", "в суббо́ту", "суббо́той", "в суббо́ты"],
        "correct": "в суббо́ту",
        "explanation": "<p>Hafta kuni — <em>в</em> + Вини́тельный, ayol jinsi "
                       "<strong>-у</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы е́дем в дере́вню "
                "___.</strong> (ию́ль)</p>",
        "choices": ["в ию́ль", "в ию́ле", "ию́лем", "ию́ля"],
        "correct": "в ию́ле",
        "explanation": "<p>Oy — <em>в</em> + Предло́жный: <strong>в ию́ле</strong>. "
                       "Hafta kuni boʻlganda Вини́тельный olardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ я рабо́таю, "
                "___ отдыха́ю.</strong> (у́тро · ве́чер)</p>",
        "choices": ["В у́тре · в ве́чере", "У́тром · ве́чером",
                    "В у́тро · в ве́чер", "У́тра · ве́чера"],
        "correct": "У́тром · ве́чером",
        "explanation": "<p>Kun qismlari predlogsiz, Твори́тельный'da: <em>у́тром, "
                       "днём, ве́чером, но́чью</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Уро́к ___.</strong> "
                "(два часа́ — «soat ikkida»)</p>",
        "choices": ["в двух часа́х", "в два часа́", "двумя́ часа́ми", "двух часо́в"],
        "correct": "в два часа́",
        "explanation": "<p>Soat — <em>в</em> + Вини́тельный: <strong>в два "
                       "часа́</strong>. Va <em>час</em> PR-36 qoidasi boʻyicha: "
                       "<em>час, два часа́, пять часо́в</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Экза́мен ___ "
                "ма́я.</strong> («beshinchi mayda»)</p>",
        "choices": ["пя́тое", "пя́того", "пя́тому", "пя́тым"],
        "correct": "пя́того",
        "explanation": "<p>«Qaysi kuni» — <strong>Роди́тельный</strong>: <em>пя́того "
                       "ма́я</em>. Sanani aytish esa bosh kelishikda: <em>Сего́дня "
                       "пя́тое ма́я</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ мы бы́ли в "
                "дере́вне.</strong> (ле́то)</p>",
        "choices": ["В ле́те", "В ле́то", "Ле́том", "Ле́та"],
        "correct": "Ле́том",
        "explanation": "<p>Fasl — predlogsiz Твори́тельный. <em>«В ле́те»</em> degan "
                       "shakl ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он придёт "
                "___.</strong> (среда́)</p>",
        "choices": ["в среде́", "в сре́ду", "средо́й", "в среду́"],
        "correct": "в сре́ду",
        "explanation": "<p>Hafta kuni — Вини́тельный, va <em>среда́</em> da urgʻu "
                       "<strong>koʻchadi</strong>: <em>сред<strong>а́</strong> → в "
                       "<strong>сре́</strong>ду</em>. Bu yagona shunday kun.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega hafta kuni Вини́тельный, oy esa Предло́жный oladi?</p>",
        "choices": ["Qisqa vaqt nuqta kabi, uzun vaqt joy kabi koʻriladi",
                    "Bu tasodifiy",
                    "Chunki oylar uzunroq soʻzlar",
                    "Chunki kunlar erkak jinsida"],
        "correct": "Qisqa vaqt nuqta kabi, uzun vaqt joy kabi koʻriladi",
        "explanation": "<p>Rus tili vaqtni joy kabi koʻradi: kichkina joyga "
                       "<strong>kirasiz</strong> (В.п.), katta joy <strong>ichida</strong> "
                       "turasiz (П.п.).</p>",
    },
    {
        "text": "<p>Oʻzbek tilida vaqt ifodalari qanday yasaladi?</p>",
        "choices": ["Deyarli hammasi -DA bilan", "Toʻrtta boshqa qurilish bilan",
                    "Predloglar bilan", "Faqat ravishlar bilan"],
        "correct": "Deyarli hammasi -DA bilan",
        "explanation": "<p><em>dushanbada, mayda, yozda, soat ikkida</em>. Ruschada "
                       "esa toʻrtta boshqa qurilish. Lekin bu iboralar "
                       "<strong>yopiq roʻyxat</strong> — yigirma yettitasi, "
                       "tamom.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["в понеде́льник · в ма́е · ле́том",
                    "в понеде́льнике · в ма́е · ле́том",
                    "в понеде́льник · в май · в ле́те",
                    "в понеде́льник · в ма́е · в ле́том"],
        "correct": "в понеде́льник · в ма́е · ле́том",
        "explanation": "<p>Uchta boshqa qurilish: hafta kuni <strong>В.п.</strong>, oy "
                       "<strong>П.п.</strong>, fasl esa <strong>predlogsiz "
                       "Т.п.</strong></p>",
    },
    {
        "text": "<p><strong>Сего́дня пя́тое ма́я</strong> va <strong>Экза́мен "
                "пя́того ма́я</strong> — farqi nima?</p>",
        "choices": ["Sanani aytish — bosh kelishik; «qaysi kuni» — Роди́тельный",
                    "Ikkalasi bir xil",
                    "Birinchisi xato",
                    "Ikkinchisi koʻplik"],
        "correct": "Sanani aytish — bosh kelishik; «qaysi kuni» — Роди́тельный",
        "explanation": "<p><em>Како́е сего́дня число́? — Пя́тое ма́я.</em> Lekin "
                       "«qachon?» degan savolga <strong>пя́того ма́я</strong> deb "
                       "javob beriladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Экза́мен в суббо́ту.", "Мы е́дем в ию́ле.",
                    "В ле́те здесь жа́рко.", "Он роди́лся в 2001 году́."],
        "correct": "В ле́те здесь жа́рко.",
        "explanation": "<p>Toʻgʻrisi — <strong>Ле́том здесь жа́рко</strong>. Fasllar "
                       "predlogsiz, Твори́тельный'da ishlatiladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он придёт в вто́рник.", "Он придёт во вто́рник.",
                    "Он придёт во вто́рнике.", "Он придёт вто́рником."],
        "correct": "Он придёт во вто́рник.",
        "explanation": "<p>Hafta kuni — Вини́тельный (jonsiz erkak, oʻzgarmaydi), va "
                       "predlog <strong>во</strong>, chunki <em>вт-</em> ikki "
                       "undosh.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Когда́ у тебя́ экза́мен?</strong></p>",
        "choices": ["— В пя́тницу, в де́сять часо́в.", "— В пя́тнице, в де́сять часо́в.",
                    "— Пя́тницей, в де́сять часа́.", "— В пя́тницу, в де́сять часа́."],
        "correct": "— В пя́тницу, в де́сять часо́в.",
        "explanation": "<p>Hafta kuni — <em>в</em> + Вини́тельный "
                       "(<strong>пя́тницу</strong>); soat 10 — 5 dan yuqori, demak "
                       "koʻplik Роди́тельный (<strong>часо́в</strong>, PR-36).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Yozda qishloqda "
                "boʻlamiz, sentyabrda esa maktabda.</strong></p>",
        "choices": ["В ле́те бу́дем в дере́вне, а в сентябре́ в шко́ле.",
                    "Ле́том бу́дем в дере́вне, а в сентябре́ в шко́ле.",
                    "Ле́том бу́дем в дере́вне, а в сентя́брь в шко́ле.",
                    "Ле́том бу́дем в дере́вне, а сентябрём в шко́ле."],
        "correct": "Ле́том бу́дем в дере́вне, а в сентябре́ в шко́ле.",
        "explanation": "<p>Ikkita boshqa qurilish: fasl — predlogsiz Твори́тельный "
                       "(<strong>ле́том</strong>), oy — <em>в</em> + Предло́жный "
                       "(<strong>в сентябре́</strong>).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-47 Mashq: Soʻroq soʻzlarining kelishiklari: кто, что, какой, чей, сколько",
        "description": (
            "Bitta qoida: savol javob kutilayotgan kelishikda beriladi. Кто/что "
            "ning oltita shakli, како́й va чей ning moslashuvi."
        ),
        "tutorial": "PR-47:",
        "questions": Q_PR47,
    },
    {
        "title": "PR-48 Mashq: Predlog xaritasi: qaysi predlog qaysi kelishikni talab qiladi",
        "description": (
            "Butun predlog xaritasi bir joyda: qaysi kelishik nechta predlog "
            "oladi, ikki kelishikli predloglar va antonim juftliklar."
        ),
        "tutorial": "PR-48:",
        "questions": Q_PR48,
    },
    {
        "title": "PR-49 Mashq: Sonlarning kelishigi va vaqt ifodalari: в понедельник, в мае, в 2026 году",
        "description": (
            "Toʻrtta kelishik bir mavzuda: hafta kuni (В.п.), oy va yil (П.п.), "
            "fasl va kun qismi (Т.п.), sana (Р.п.)."
        ),
        "tutorial": "PR-49:",
        "questions": Q_PR49,
    },
]
