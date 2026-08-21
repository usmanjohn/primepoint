# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-29 … PR-31.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.

PR-29 — xarita darsi, shuning uchun uning mashqi ham TANISH mashqi: savol va
oʻzbekcha muqobilini topish, shakl yasash emas. Haqiqiy shakl yasash PR-30 dan
boshlanadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_29_31.py --master=prime \\
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
# PR-29 — Kelishik xaritasi
# =====================================================================

Q_PR29 = [
    # 1–5 tanish
    {
        "text": "<p>Kelishik (паде́ж) nima qiladi?</p>",
        "choices": ["Feʼlning zamonini koʻrsatadi",
                    "Otning oxirini oʻzgartirib, uning gapdagi ishini koʻrsatadi",
                    "Soʻzning jinsini oʻzgartiradi",
                    "Urgʻuning joyini belgilaydi"],
        "correct": "Otning oxirini oʻzgartirib, uning gapdagi ishini koʻrsatadi",
        "explanation": "<p>Oʻzbekchada ham xuddi shu ish qilinadi: <em>kitob → "
                       "kitob<strong>ni</strong> → kitob<strong>ga</strong></em>. "
                       "Qoʻshimcha soʻzning gapdagi rolini aytib turadi.</p>",
    },
    {
        "text": "<p>Rus tilida nechta kelishik bor?</p>",
        "choices": ["Toʻrtta", "Beshta", "Oltita", "Sakkizta"],
        "correct": "Oltita",
        "explanation": "<p>Oltita: Имени́тельный, Роди́тельный, Да́тельный, "
                       "Вини́тельный, Твори́тельный, Предло́жный. Oʻzbek tilida ham "
                       "oltita — shuning uchun tushuncha yangi emas.</p>",
    },
    {
        "text": "<p>Qaysi ruscha kelishik oʻzbekcha <strong>-ni</strong> (tushum) ga "
                "toʻgʻri keladi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Вини́тельный",
        "explanation": "<p><em>kitob<strong>ni</strong> oʻqidim</em> → <em>я чита́л "
                       "кни́г<strong>у</strong></em>. Savoli: <em>кого́? что?</em></p>",
    },
    {
        "text": "<p>Qaysi ruscha kelishik oʻzbekcha <strong>-ga</strong> (joʻnalish) ga "
                "toʻgʻri keladi?</p>",
        "choices": ["Да́тельный", "Предло́жный", "Роди́тельный", "Имени́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>men<strong>ga</strong> kerak</em> → <em><strong>мне</strong> "
                       "на́до</em>. Siz bu shakllarni PR-27 va PR-28 da allaqachon "
                       "ishlatgansiz — endi ularning nomi ham bor.</p>",
    },
    {
        "text": "<p>Nega <strong>Предло́жный</strong> shunday nomlanadi?</p>",
        "choices": ["Chunki u eng oxirgi kelishik",
                    "Chunki u faqat gap boshida keladi",
                    "Chunki u hech qachon predlogsiz ishlatilmaydi",
                    "Chunki uni birinchi boʻlib oʻrganiladi"],
        "correct": "Chunki u hech qachon predlogsiz ishlatilmaydi",
        "explanation": "<p><em>Предло́г</em> = predlog. Bu kelishik har doim "
                       "<strong>в</strong>, <strong>на</strong> yoki <strong>о</strong> "
                       "bilan keladi: <em>в шко́ле, на рабо́те, о кни́ге</em>. Bu uni "
                       "tanishni osonlashtiradi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu gapda <strong>кни́гу</strong> qaysi kelishikda?</p>"
                "<p><strong>Афсо́на чита́ет кни́гу.</strong></p>",
        "choices": ["Имени́тельный", "Вини́тельный", "Роди́тельный", "Предло́жный"],
        "correct": "Вини́тельный",
        "explanation": "<p>Savol: Afsona <em>nimani</em> oʻqiyapti? — <em>кни́гу</em>. "
                       "Bu toʻldiruvchi, demak Вини́тельный. Oʻzbekchada: "
                       "«kitob<strong>ni</strong>».</p>",
    },
    {
        "text": "<p>Bu iboraga qaysi savol beriladi?</p><p><strong>кни́га "
                "бра́та</strong></p>",
        "choices": ["кому́?", "чей? кого́?", "чем?", "где?"],
        "correct": "чей? кого́?",
        "explanation": "<p><em>Кни́га бра́та</em> = «akaning kitobi» — egalik, demak "
                       "<strong>Роди́тельный</strong>. Oʻzbekchada qaratqich kelishigi: "
                       "<em>aka<strong>ning</strong></em>.</p>",
    },
    {
        "text": "<p>Bu qatorda qaysi shakl <strong>Имени́тельный</strong>'da?</p>"
                "<p><strong>кни́ги · кни́ге · кни́га · кни́гу</strong></p>",
        "choices": ["кни́ги", "кни́ге", "кни́га", "кни́гу"],
        "correct": "кни́га",
        "explanation": "<p><strong>Кни́га</strong> — lugʻatdagi shakl, ega shakli. "
                       "Savoli <em>кто? что?</em> Boshqa beshta shakl shundan "
                       "yasaladi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nimada?</p><p><strong>Я в шко́ле. · Я иду́ в "
                "шко́лу.</strong></p>",
        "choices": ["Qayerda · qayerga — bitta predlog, ikki kelishik",
                    "Ikkalasi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Qayerda · qayerga — bitta predlog, ikki kelishik",
        "explanation": "<p><em>В шко́л<strong>е</strong></em> — Предло́жный (qayerda). "
                       "<em>В шко́л<strong>у</strong></em> — Вини́тельный (qayerga). "
                       "Rus tilida predlogning oʻzi yetarli emas: qoʻshimcha ham maʼno "
                       "beradi.</p>",
    },
    {
        "text": "<p>Bu jadvalda qaysi ikki jins deyarli bir xil turlanadi?</p>",
        "choices": ["Erkak va ayol", "Ayol va oʻrta",
                    "Erkak va oʻrta", "Uchalasi ham har xil"],
        "correct": "Erkak va oʻrta",
        "explanation": "<p><em>стол<strong>а́</strong> / окн<strong>а́</strong></em>, "
                       "<em>стол<strong>у́</strong> / окн<strong>у́</strong></em>, "
                       "<em>стол<strong>о́м</strong> / окн<strong>о́м</strong></em> — "
                       "amalda uchta emas, <strong>ikkita</strong> naqsh bor. Bu "
                       "yodlashni ancha yengillashtiradi.</p>",
    },
    {
        "text": "<p>Qaysi kelishikning oʻzbek tilida aniq juftligi <strong>yoʻq</strong>?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Твори́тельный",
        "explanation": "<p>Oʻzbekchada bu maʼno alohida kelishik bilan emas, "
                       "<strong>«bilan»</strong> soʻzi bilan beriladi: <em>ruchka bilan "
                       "yozdim</em> → <em>я писа́л ру́чк<strong>ой</strong></em>. "
                       "Shuning uchun u kursda oxirida (PR-39, PR-40) keladi.</p>",
    },
    {
        "text": "<p>Bu gapda <strong>бра́ту</strong> qaysi kelishikda?</p>"
                "<p><strong>Я дам кни́гу бра́ту.</strong></p>",
        "choices": ["Да́тельный", "Роди́тельный", "Предло́жный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p>Savol: kimga beraman? — <em>бра́ту</em>. Oʻzbekchada "
                       "<em>aka<strong>ga</strong></em>, joʻnalish kelishigi. Savoli: "
                       "<em>кому́?</em></p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Rus tilida oʻzbek tilidan farqli uch qiyinchilik nima?</p>",
        "choices": ["Jins, predloglar, urgʻuning koʻchishi",
                    "Alifbo, soʻz tartibi, inkor",
                    "Zamon, jins, koʻplik",
                    "Feʼl, sifat, ravish"],
        "correct": "Jins, predloglar, urgʻuning koʻchishi",
        "explanation": "<p>Kelishik tushunchasining oʻzi tanish. Yangi narsa uchta: "
                       "shakl <strong>jinsga</strong> bogʻliq; koʻpincha predlog "
                       "<strong>va</strong> qoʻshimcha birga kerak; va urgʻu joyini "
                       "almashtirishi mumkin (<em>стол → на столе́</em>).</p>",
    },
    {
        "text": "<p>Bu ikki shakl bir xil koʻrinadi. Ular qaysi kelishiklarda?</p>"
                "<p><strong>кни́ге</strong> (Мне нра́вится… / о…)</p>",
        "choices": ["Faqat Да́тельный", "Faqat Предло́жный",
                    "Да́тельный va Предло́жный", "Роди́тельный va Да́тельный"],
        "correct": "Да́тельный va Предло́жный",
        "explanation": "<p>Ayol jinsidagi otlarda bu ikki kelishik bir xil koʻrinadi: "
                       "<em>дать кни́г<strong>е</strong></em> (Д.п.) va <em>о "
                       "кни́г<strong>е</strong></em> (П.п.). Shunday takrorlanishlar "
                       "koʻp — shuning uchun 36 ta shakl emas, ancha kam narsa "
                       "yodlanadi.</p>",
    },
    {
        "text": "<p>Nega kursda Предло́жный birinchi oʻrgatiladi?</p>",
        "choices": ["Chunki u jadvalda birinchi turadi",
                    "Chunki qoʻshimchasi eng oddiy va «qayerda?» darrov kerak",
                    "Chunki u eng kam ishlatiladi",
                    "Chunki u oʻzbekchada yoʻq"],
        "correct": "Chunki qoʻshimchasi eng oddiy va «qayerda?» darrov kerak",
        "explanation": "<p>Kelishiklar jadval tartibida emas, <strong>foydalilik "
                       "tartibida</strong> oʻrganiladi. Предло́жный'ning qoʻshimchasi "
                       "deyarli har doim <strong>-Е</strong>, va «qayerda?» degan savol "
                       "birinchi kundanoq kerak boʻladi.</p>",
    },
    {
        "text": "<p>Bu gapda nima notoʻgʻri?</p><p><strong>Кни́га брат.</strong> "
                "(«akaning kitobi» maʼnosida)</p>",
        "choices": ["Ega yoʻq", "«Брат» kelishikka kirmagan",
                    "Feʼl yetishmayapti", "Predlog yetishmayapti"],
        "correct": "«Брат» kelishikka kirmagan",
        "explanation": "<p>Toʻgʻrisi — <strong>кни́га бра́та</strong>. «Kimniki?» degan "
                       "savolga javob beruvchi soʻz Роди́тельный'da boʻlishi kerak. "
                       "Oʻzbekchada ham: <em>aka<strong>ning</strong> kitobi</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Афсо́на чита́ет кни́гу.", "Мы живём в Ташке́нте.",
                    "Я иду́ в шко́ле.", "Мне на́до идти́."],
        "correct": "Я иду́ в шко́ле.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я иду́ в шко́лу</strong>. Harakat "
                       "«qayerga?» degan savolga javob beryapti, demak Вини́тельный. "
                       "<em>В шко́ле</em> «maktabdaman» degan boʻlardi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я в шко́ла.", "Я в шко́ле.", "Я в шко́лу.", "Я шко́ле."],
        "correct": "Я в шко́ле.",
        "explanation": "<p>Predlog bor, demak qoʻshimcha ham kerak — ikkalasi birga "
                       "ishlaydi. <em>«Я в шко́ла»</em> — qoʻshimcha unutilgan, "
                       "<em>«Я в шко́лу»</em> — harakat maʼnosi, <em>«Я шко́ле»</em> — "
                       "predlog yoʻq.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu oltita shaklni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>кни́га — кто? что?</strong> dan boshlanadi.</p>",
        "choices": ["кни́га · кни́ги · кни́ге · кни́гу · кни́гой · о кни́ге",
                    "кни́га · кни́ге · кни́ги · кни́гу · о кни́ге · кни́гой",
                    "кни́гу · кни́га · кни́ги · кни́ге · кни́гой · о кни́ге",
                    "кни́га · кни́гу · кни́ги · кни́гой · кни́ге · о кни́ге"],
        "correct": "кни́га · кни́ги · кни́ге · кни́гу · кни́гой · о кни́ге",
        "explanation": "<p>Ruscha maktab tartibi: Имени́тельный, Роди́тельный, "
                       "Да́тельный, Вини́тельный, Твори́тельный, Предло́жный. Bu "
                       "tartib har bir rus lugʻatida va jadvalida ishlatiladi — "
                       "yodlab qoʻysangiz asqotadi.</p>",
    },
    {
        "text": "<p>Bu gapni oʻzbekchaga oʻgiring.</p><p><strong>Мы говори́м о "
                "кни́ге.</strong></p>",
        "choices": ["Biz kitobni oʻqiyapmiz.", "Biz kitob haqida gapiryapmiz.",
                    "Biz kitobga yozyapmiz.", "Kitob bizga gapiryapti."],
        "correct": "Biz kitob haqida gapiryapmiz.",
        "explanation": "<p><strong>О кни́ге</strong> — Предло́жный, «haqida» maʼnosida. "
                       "Bu kelishikning ikkinchi vazifasi va u PR-31 da alohida "
                       "koʻriladi.</p>",
    },
]


# =====================================================================
# PR-30 — Предложный 1: где?
# =====================================================================

Q_PR30 = [
    # 1–5 tanish
    {
        "text": "<p>Предло́жный padejining asosiy qoʻshimchasi qaysi?</p>",
        "choices": ["-а", "-у", "-е", "-ой"],
        "correct": "-е",
        "explanation": "<p>Jinsdan qatʼi nazar — <strong>-Е</strong>: <em>в шко́л<strong>е</strong>, "
                       "в до́м<strong>е</strong>, в окн<strong>е́</strong></em>. Aynan "
                       "shuning uchun bu kelishik birinchi oʻrgatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на сейча́с в "
                "___.</strong> (шко́ла)</p>",
        "choices": ["шко́ла", "шко́лу", "шко́ле", "шко́лы"],
        "correct": "шко́ле",
        "explanation": "<p><em>Шко́ла → шко́л- → шко́л<strong>е</strong></em>. Predlog "
                       "<em>в</em> bor, demak qoʻshimcha ham kerak — ikkalasi birga "
                       "ishlaydi.</p>",
    },
    {
        "text": "<p><strong>в</strong> yoki <strong>на</strong>?</p><p><strong>Ма́ма ___ "
                "рабо́те.</strong></p>",
        "choices": ["в", "на", "о", "из"],
        "correct": "на",
        "explanation": "<p><strong>На рабо́те</strong> — yodlanadigan roʻyxatdan. Unda "
                       "mantiq yoʻq, faqat odat: <em>на рабо́те, на уро́ке, на ры́нке, "
                       "на по́чте, на вокза́ле, на экза́мене</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мой брат живёт в "
                "___.</strong> (Росси́я)</p>",
        "choices": ["Росси́е", "Росси́и", "Росси́ю", "Росси́я"],
        "correct": "Росси́и",
        "explanation": "<p>Birinchi istisno: <strong>-ия / -ие / -ий</strong> ga "
                       "tugagan soʻzlar <strong>-ИИ</strong> oladi. Xuddi shunday: "
                       "<em>на ле́кции, в общежи́тии, в Ита́лии</em>.</p>",
    },
    {
        "text": "<p>«Uydaman» ruschada qanday boʻladi?</p>",
        "choices": ["Я в до́ме.", "Я до́ма.", "Я на до́ме.", "Я в дом."],
        "correct": "Я до́ма.",
        "explanation": "<p><strong>До́ма</strong> — ravish, u kelishik olmaydi. "
                       "<em>В до́ме</em> «bino <strong>ichida</strong>» degani va uni "
                       "koʻchada turgan odam aytadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ключи́ на ___.</strong> "
                "(стол)</p>",
        "choices": ["сто́ле", "столе́", "столу́", "стола́"],
        "correct": "столе́",
        "explanation": "<p><strong>На столе́</strong> — qoʻshimcha oddiy <em>-е</em>, "
                       "lekin <strong>urgʻu koʻchgan</strong>: <em>сто́л → на "
                       "стол<strong>е́</strong></em>. Bir boʻgʻinli erkak otlarda bu "
                       "tez-tez boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Телефо́н в ___.</strong> "
                "(су́мка)</p>",
        "choices": ["су́мку", "су́мки", "су́мке", "су́мка"],
        "correct": "су́мке",
        "explanation": "<p>Sumkaning ichi bor, demak <strong>в</strong>; qoʻshimcha "
                       "<strong>-е</strong>. Urgʻu bu soʻzda joyida qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д игра́ет на "
                "___.</strong> (пол)</p>",
        "choices": ["по́ле", "полу́", "по́ла", "пол"],
        "correct": "полу́",
        "explanation": "<p>Uchinchi istisno — <strong>-У́</strong> yopiq roʻyxati: "
                       "<em>в лесу́, в саду́, на полу́, в шкафу́, на берегу́, в "
                       "аэропорту́</em>. Urgʻu har doim qoʻshimchada.</p>",
    },
    {
        "text": "<p><strong>в</strong> yoki <strong>на</strong>?</p><p><strong>Мы бы́ли "
                "___ ры́нке и ___ магази́не.</strong></p>",
        "choices": ["в · на", "на · в", "в · в", "на · на"],
        "correct": "на · в",
        "explanation": "<p><strong>На ры́нке</strong> — ochiq maydon va yodlanadigan "
                       "roʻyxatdan. <strong>В магази́не</strong> — bino, ichi bor. "
                       "Ikkalasida ham qoʻshimcha bir xil: <em>-е</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́ю в ___.</strong> "
                "(авто́бус)</p>",
        "choices": ["авто́бусе", "авто́бус", "авто́буса", "авто́бусу"],
        "correct": "авто́бусе",
        "explanation": "<p>Avtobus — ichi bor, demak <strong>в авто́бусе</strong>. "
                       "Qoʻshimcha oddiy <em>-е</em>, urgʻu joyida qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ба́бушка живёт в "
                "___.</strong> (дере́вня)</p>",
        "choices": ["дере́вню", "дере́вни", "дере́вне", "дере́вня"],
        "correct": "дере́вне",
        "explanation": "<p><em>Дере́вня → дере́вн- → дере́вн<strong>е</strong></em>. "
                       "Soʻz <em>-ня</em> ga tugasa ham (<em>-ия</em> emas), oddiy "
                       "<strong>-е</strong> oladi. Istisno faqat <em>-ия</em> "
                       "uchun.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он живёт на пя́том "
                "___.</strong> (эта́ж)</p>",
        "choices": ["этаже́", "эта́же", "этажу́", "этажа́"],
        "correct": "этаже́",
        "explanation": "<p><strong>На этаже́</strong> — qavat «yuza» deb qaraladi, "
                       "shuning uchun <em>на</em>; qoʻshimcha <em>-е</em> va urgʻu "
                       "koʻchgan.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega «в су́мке», lekin «на столе́»?</p>",
        "choices": ["Sumkaning ichi bor (В), stol esa yuza (НА)",
                    "Chunki bu ikki xil kelishik",
                    "Chunki «стол» erkak jinsida",
                    "Chunki «су́мка» ayol jinsida"],
        "correct": "Sumkaning ichi bor (В), stol esa yuza (НА)",
        "explanation": "<p>Kelishik bitta va qoʻshimcha ham bir xil (<em>-е</em>). "
                       "Faqat predlog boshqa. Jins bu tanlovga umuman "
                       "taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>Qaysi soʻz <strong>-ИИ</strong> oladi?</p>",
        "choices": ["шко́ла", "дере́вня", "ле́кция", "ко́мната"],
        "correct": "ле́кция",
        "explanation": "<p><em>Ле́кция → на ле́кци<strong>и</strong></em>. Faqat "
                       "<strong>-ия / -ие / -ий</strong> ga tugagan soʻzlar bunday. "
                       "<em>Дере́вня</em> — <em>-ня</em>, demak oddiy <em>-е</em>.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["в шко́ле · на рабо́те · в Росси́и",
                    "в шко́ла · на рабо́те · в Росси́и",
                    "в шко́ле · в рабо́те · в Росси́е",
                    "на шко́ле · на рабо́те · в Росси́и"],
        "correct": "в шко́ле · на рабо́те · в Росси́и",
        "explanation": "<p>Uchta boshqa qoida: oddiy <strong>-е</strong>, "
                       "<strong>НА</strong>-roʻyxat, va <strong>-ии</strong> istisnosi. "
                       "Qolgan variantlarda bittasi har doim buziladi.</p>",
    },
    {
        "text": "<p>Oʻzbekchadagi qaysi qoʻshimcha Предло́жный'ga toʻgʻri keladi?</p>",
        "choices": ["-ni", "-ga", "-da", "-ning"],
        "correct": "-da",
        "explanation": "<p><em>maktab<strong>da</strong></em> → <em>в шко́ле</em>, "
                       "<em>ish<strong>da</strong></em> → <em>на рабо́те</em>. "
                       "Oʻrin-payt kelishigi. Farqi shuki, ruschada qoʻshimchadan "
                       "tashqari predlog ham kerak va u ikki xil.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мы живём в го́роде.", "Он в рабо́те.",
                    "Кни́га на столе́.", "Я был на ры́нке."],
        "correct": "Он в рабо́те.",
        "explanation": "<p>Toʻgʻrisi — <strong>Он на рабо́те</strong>. "
                       "<em>Рабо́та</em> НА oladigan yodlanadigan roʻyxatda. "
                       "Qoʻshimcha esa toʻgʻri edi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Ве́чером мы бу́дем в до́ме.", "Ве́чером мы бу́дем до́ма.",
                    "Ве́чером мы бу́дем на до́ме.", "Ве́чером мы бу́дем в дом."],
        "correct": "Ве́чером мы бу́дем до́ма.",
        "explanation": "<p><strong>До́ма</strong> — ravish va u kelishik olmaydi. "
                       "<em>В до́ме</em> grammatik jihatdan toʻgʻri, lekin maʼnosi "
                       "boshqa: «bino ichida».</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Где Афсо́на?</strong></p>",
        "choices": ["— Она́ на рабо́те.", "— Она́ в рабо́ту.",
                    "— Она́ рабо́те.", "— Она́ в рабо́та."],
        "correct": "— Она́ на рабо́те.",
        "explanation": "<p>Savol <em>где?</em> — demak Предло́жный. <em>Рабо́та</em> "
                       "НА oladi, qoʻshimcha esa <em>-е</em>. Qolgan variantlarda yo "
                       "predlog, yo qoʻshimcha buzilgan.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Kalitlar stolda, telefon "
                "esa sumkada.</strong></p>",
        "choices": ["Ключи́ в столе́, а телефо́н на су́мке.",
                    "Ключи́ на столе́, а телефо́н в су́мке.",
                    "Ключи́ на стол, а телефо́н в су́мку.",
                    "Ключи́ на столу́, а телефо́н в су́мке."],
        "correct": "Ключи́ на столе́, а телефо́н в су́мке.",
        "explanation": "<p>Stol — yuza (<strong>на</strong>), sumka — ichi bor "
                       "(<strong>в</strong>). Ikkalasida ham <em>-е</em>. "
                       "<em>«На столу́»</em> — <em>стол</em> <strong>-у́</strong> "
                       "roʻyxatida yoʻq.</p>",
    },
]


# =====================================================================
# PR-31 — Предложный 2: о чём? о ком?
# =====================================================================

Q_PR31 = [
    # 1–5 tanish
    {
        "text": "<p><strong>о</strong> predlogi qanday maʼno beradi?</p>",
        "choices": ["qayerda", "haqida", "bilan", "uchun"],
        "correct": "haqida",
        "explanation": "<p><em>О кни́ге</em> = «kitob haqida». Kelishik oʻsha "
                       "Предло́жный, qoʻshimcha ham oʻsha — faqat predlog va savol "
                       "boshqa: <em>о чём? о ком?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы говори́м о ___.</strong> "
                "(фильм)</p>",
        "choices": ["фильм", "фи́льме", "фи́льму", "фи́льма"],
        "correct": "фи́льме",
        "explanation": "<p>Qoʻshimcha PR-30 dagining oʻzi — <strong>-е</strong>. "
                       "Predlog bor, demak qoʻshimcha ham kerak.</p>",
    },
    {
        "text": "<p><strong>о</strong> yoki <strong>об</strong>?</p><p><strong>___ "
                "уро́ке</strong></p>",
        "choices": ["о", "об", "обо", "оба"],
        "correct": "об",
        "explanation": "<p><em>Уро́к</em> unli tovush <strong>У</strong> bilan "
                       "boshlanadi, demak <strong>об</strong>. Qoida: об — а, э, и, о, "
                       "у dan oldin.</p>",
    },
    {
        "text": "<p>«Men haqimda» ruschada qanday boʻladi?</p>",
        "choices": ["о мне", "об мне", "обо мне", "о я"],
        "correct": "обо мне",
        "explanation": "<p><strong>Обо мне</strong> — rus tilidagi ikkita "
                       "<em>обо</em> holatidan biri. Ikkinchisi — <em>обо всём</em>. "
                       "Boshqa hech qayerda <em>обо</em> ishlatilmaydi.</p>",
    },
    {
        "text": "<p>«Bu kitob nima haqida?» ruschada qanday soʻraladi?</p>",
        "choices": ["Что э́та кни́га?", "О чём э́та кни́га?",
                    "О ком э́та кни́га?", "Где э́та кни́га?"],
        "correct": "О чём э́та кни́га?",
        "explanation": "<p>Savol soʻzining oʻzi ham kelishikka kiradi: <em>что → о "
                       "чём</em>, <em>кто → о ком</em>. Narsa haqida — <strong>о "
                       "чём</strong>, odam haqida — <strong>о ком</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю о ___.</strong> "
                "(ты)</p>",
        "choices": ["ты", "тебя́", "тебе́", "тобо́й"],
        "correct": "тебе́",
        "explanation": "<p>Olmosh ham kelishikka kiradi: <strong>о тебе́</strong>. "
                       "Toʻliq roʻyxat: <em>обо мне, о тебе́, о нём, о ней, о нас, о "
                       "вас, о них</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Что ты зна́ешь о "
                "___?</strong> (он)</p>",
        "choices": ["он", "его́", "нём", "ему́"],
        "correct": "нём",
        "explanation": "<p><strong>О нём</strong>. Predlogdan keyin "
                       "<em>он / она́ / они́</em> olmoshlari <strong>Н</strong> bilan "
                       "boshlanadi — bu qoida hamma kelishikda ishlaydi: <em>у "
                       "него́, к ней, с ни́ми</em>.</p>",
    },
    {
        "text": "<p><strong>о</strong> yoki <strong>об</strong>?</p><p><strong>___ "
                "Евро́пе</strong></p>",
        "choices": ["о", "об", "обо", "оба"],
        "correct": "о",
        "explanation": "<p>Qoida <strong>tovushga</strong> qaraydi, harfga emas. "
                       "<em>Е</em> soʻz boshida [йэ] boʻlib oʻqiladi — yaʼni undosh "
                       "tovushdan boshlanadi. Shuning uchun <strong>о Евро́пе</strong>, "
                       "xuddi <em>о я́блоке</em> kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́л о ___.</strong> "
                "(Росси́я)</p>",
        "choices": ["Росси́е", "Росси́и", "Росси́ю", "Росси́я"],
        "correct": "Росси́и",
        "explanation": "<p>PR-30 dagi <strong>-ии</strong> istisnosi bu yerda ham "
                       "ishlaydi — kelishik oʻsha, faqat predlog boshqa: <em>в "
                       "Росси́и</em> va <em>о Росси́и</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ба́бушка ча́сто говори́т о "
                "___.</strong> (ле́то)</p>",
        "choices": ["ле́то", "ле́та", "ле́те", "ле́том"],
        "correct": "ле́те",
        "explanation": "<p>Oʻrta jinsdagi ot ham <strong>-е</strong> oladi: "
                       "<em>ле́то → о ле́т<strong>е</strong></em>. Bu kelishikda "
                       "uchala jins ham bir xil ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ спра́шивает о "
                "___.</strong> (мы)</p>",
        "choices": ["нам", "нас", "мы", "на́ми"],
        "correct": "нас",
        "explanation": "<p><strong>О нас</strong>. Eʼtibor bering: birinchi va ikkinchi "
                       "shaxs koʻplikda Н qoʻshilmaydi — u faqat "
                       "<em>он / она́ / они́</em> ga tegishli.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы говори́ли об ___.</strong> "
                "(окно́)</p>",
        "choices": ["окно́", "окне́", "окна́", "окну́"],
        "correct": "окне́",
        "explanation": "<p><strong>Об окне́</strong> — <em>окно́</em> unli "
                       "<strong>О</strong> bilan boshlanadi, demak <em>об</em>; "
                       "qoʻshimcha esa <em>-е</em> va urgʻu koʻchgan.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega bu shakllarda <strong>Н</strong> bor?</p><p><strong>о нём · о "
                "ней · о них</strong></p>",
        "choices": ["Chunki predlogdan keyin он/она́/они́ ga Н qoʻshiladi",
                    "Chunki bular koʻplik",
                    "Chunki bu Предло́жный padeji",
                    "Bu shunchaki istisno soʻzlar"],
        "correct": "Chunki predlogdan keyin он/она́/они́ ga Н qoʻshiladi",
        "explanation": "<p>Predlogsiz Н yoʻq: <em>его́, её, их</em>. Predlog bilan esa "
                       "bor: <em>о нём, у него́, к ней, с ни́ми</em>. Bitta qoida — "
                       "hamma kelishikda ishlaydi.</p>",
    },
    {
        "text": "<p>Bu ikki ibora qanday farq qiladi?</p><p><strong>в кни́ге · о "
                "кни́ге</strong></p>",
        "choices": ["Kitobda · kitob haqida",
                    "Kitob haqida · kitobda",
                    "Ikkalasi bir xil",
                    "Birinchisi xato"],
        "correct": "Kitobda · kitob haqida",
        "explanation": "<p>Kelishik ikkalasida ham bir xil va qoʻshimcha ham "
                       "(<em>-е</em>). Maʼnoni <strong>predlog</strong> hal qiladi: "
                       "<em>в</em> — joy, <em>о</em> — mavzu.</p>",
    },
    {
        "text": "<p>Bu feʼllardan qaysi biri <strong>о</strong> talab qilmaydi?</p>",
        "choices": ["ду́мать", "мечта́ть", "говори́ть", "чита́ть кни́гу"],
        "correct": "чита́ть кни́гу",
        "explanation": "<p><em>Чита́ть</em> ikki xil ishlaydi: <em>чита́ть "
                       "кни́г<strong>у</strong></em> (kitobni oʻqimoq — Вини́тельный) "
                       "va <em>чита́ть <strong>о</strong> кни́ге</em> (kitob haqida "
                       "oʻqimoq). Qolgan uchtasi har doim <em>о</em> oladi.</p>",
    },
    {
        "text": "<p>Oʻzbekcha «haqida» va ruscha «о» ning ikkita farqi nima?</p>",
        "choices": ["«Haqida» otdan keyin turadi va ot oʻzgarmaydi",
                    "«Haqida» otdan oldin turadi va ot oʻzgaradi",
                    "Hech qanday farq yoʻq",
                    "«Haqida» faqat odamlar uchun ishlatiladi"],
        "correct": "«Haqida» otdan keyin turadi va ot oʻzgarmaydi",
        "explanation": "<p><em>kitob haqida</em> — soʻz orqada, ot oʻz holida. "
                       "<em>о кни́г<strong>е</strong></em> — predlog oldinda va ot ham "
                       "oʻzgargan. Shuning uchun ruschada ikkita narsani birga "
                       "eslash kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я чита́ю о Росси́и.", "Он ду́мает о мне.",
                    "Мы говори́м об уро́ке.", "Что ты зна́ешь о них?"],
        "correct": "Он ду́мает о мне.",
        "explanation": "<p>Toʻgʻrisi — <strong>обо мне</strong>. Bu ikkita "
                       "<em>обо</em> holatidan biri (ikkinchisi <em>обо всём</em>). "
                       "Qolgan uchtasi toʻgʻri.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я чита́л об кни́ге.", "Я чита́л о кни́ге.",
                    "Я чита́л обо кни́ге.", "Я чита́л о кни́га."],
        "correct": "Я чита́л о кни́ге.",
        "explanation": "<p><em>Кни́га</em> undosh <strong>К</strong> bilan boshlanadi, "
                       "demak oddiy <strong>о</strong>; qoʻshimcha esa "
                       "<strong>-е</strong>. <em>Об</em> faqat unlidan oldin, "
                       "<em>обо</em> esa faqat ikkita soʻz bilan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— О ком ты ду́маешь?</strong></p>",
        "choices": ["— О ба́бушке.", "— О ба́бушка.",
                    "— Об ба́бушке.", "— О ба́бушку."],
        "correct": "— О ба́бушке.",
        "explanation": "<p>Savol <em>о ком?</em> — odam haqida. <em>Ба́бушка → о "
                       "ба́бушк<strong>е</strong></em>, predlog oddiy <em>о</em> "
                       "(Б — undosh).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Men sen haqingda "
                "oʻylayapman.</strong></p>",
        "choices": ["Я ду́маю о ты.", "Я ду́маю о тебя́.",
                    "Я ду́маю о тебе́.", "Я ду́маю обо тебе́."],
        "correct": "Я ду́маю о тебе́.",
        "explanation": "<p><strong>О тебе́</strong>. Oddiy oʻzbekchada bu gap «seni "
                       "oʻylayapman» ham boʻladi — <em>ду́мать о</em> ikkala maʼnoni "
                       "beradi. <em>Обо</em> faqat <em>мне</em> bilan ishlatiladi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-29 Mashq: Kelishik nima? Olti падеж'ning umumiy xaritasi",
        "description": (
            "Xarita darsining mashqi: oltita kelishik, ularning savollari va "
            "oʻzbekcha kelishiklar bilan mosligi. Shakl yasash emas — tanish."
        ),
        "tutorial": "PR-29:",
        "questions": Q_PR29,
    },
    {
        "title": "PR-30 Mashq: Предложный 1: где? — в школе, на работе, в Ташкенте",
        "description": (
            "Asosiy qoʻshimcha -Е va uchta istisno (-ИИ, -И, -У́); В va НА "
            "tanlovi hamda yodlanadigan НА-roʻyxat."
        ),
        "tutorial": "PR-30:",
        "questions": Q_PR30,
    },
    {
        "title": "PR-31 Mashq: Предложный 2: о чём? о ком? — о фильме, о тебе",
        "description": (
            "О / об / обо tanlovi, «о» talab qiladigan feʼllar, olmoshlar "
            "(обо мне, о тебе́, о нём) va predlogdan keyingi Н qoidasi."
        ),
        "tutorial": "PR-31:",
        "questions": Q_PR31,
    },
]
