# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-6 … PR-8 (birinchi grammatika testlari).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_06_08.py --master=prime \\
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
# PR-6 — Это. Кто это? Что это?
# =====================================================================

Q_PR6 = [
    # 1–5 tanish
    {
        "text": "<p>Bu gapni oʻzbekchaga oʻgiring.</p><p><strong>Э́то дом.</strong></p>",
        "choices": ["Bu — uy.", "Uy bor.", "Uyda.", "Bu uyning ichi."],
        "correct": "Bu — uy.",
        "explanation": "<p><strong>Э́то дом</strong> — “Bu — uy”. Ikkita soʻz va bu "
                       "toʻliq ruscha gap. Orasiga hech qanday feʼl qoʻyilmaydi — "
                       "xuddi oʻzbekchadagidek.</p>",
    },
    {
        "text": "<p>Rus tilida hozirgi zamonda “boʻlmoq” feʼli ishlatiladimi?</p>",
        "choices": ["Ha, har doim", "Ha, faqat savolda",
                    "Yoʻq — u tushirib qoldiriladi", "Faqat koʻplikda"],
        "correct": "Yoʻq — u tushirib qoldiriladi",
        "explanation": "<p><strong>Быть</strong> feʼli bor, lekin hozirgi zamonda "
                       "ishlatilmaydi. Uning oʻrnida hech nima turmaydi yoki yozuvda "
                       "tire (—) qoʻyiladi. Oʻzbek tilida ham xuddi shunday: “Bu — uy”, "
                       "“Bu uydir” emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ э́то? — Э́то "
                "учи́тель.</strong></p>",
        "choices": ["Что", "Кто", "Где", "Как"],
        "correct": "Кто",
        "explanation": "<p><strong>Кто э́то?</strong> — javobda odam turibdi "
                       "(учи́тель — oʻqituvchi). КТО odam va hayvon uchun, ЧТО esa "
                       "buyum, joy va tushuncha uchun.</p>",
    },
    {
        "text": "<p><strong>да</strong> va <strong>нет</strong> nima degani?</p>",
        "choices": ["Ha va yoʻq", "Bu va anavi", "Kim va nima", "Shu yerda va u yerda"],
        "correct": "Ha va yoʻq",
        "explanation": "<p><strong>Да</strong> — ha, <strong>нет</strong> — yoʻq. "
                       "Diqqat: <strong>нет</strong> bu javob, <strong>не</strong> esa "
                       "inkor qilinayotgan soʻz oldida turadigan zarracha. Ular ikki "
                       "xil soʻz.</p>",
    },
    {
        "text": "<p><strong>э́то</strong> soʻzi otning jinsiga qarab oʻzgaradimi?</p>",
        "choices": ["Ha, uch xil shakli bor", "Yoʻq — bitta shakl, hamma holat uchun",
                    "Faqat koʻplikda oʻzgaradi", "Faqat savolda oʻzgaradi"],
        "correct": "Yoʻq — bitta shakl, hamma holat uchun",
        "explanation": "<p>Mustaqil turgan <strong>э́то</strong> oʻzgarmaydi: "
                       "<em>Э́то дом. Э́то кни́га. Э́то окно́.</em> Otning oldida "
                       "turadigan <strong>э́тот / э́та / э́то</strong> esa oʻzgaradi — "
                       "lekin bu boshqa soʻz, uni PR-16 da koʻramiz.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri savolni tanlang.</p><p><strong>___ — Э́то кот.</strong></p>",
        "choices": ["Что э́то?", "Кто э́то?", "Где кот?", "Как кот?"],
        "correct": "Кто э́то?",
        "explanation": "<p><strong>Кто э́то?</strong> Mushuk — jonli mavjudot, va rus "
                       "tilida hayvon <strong>КТО</strong> tomonda turadi. Bu oʻzbek "
                       "oʻquvchisi koʻp adashadigan yagona joy, chunki oʻzbekchada "
                       "hayvon haqida “bu nima?” deb ham soʻrash mumkin.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bu — maktab.</strong></p>",
        "choices": ["Э́то есть шко́ла.", "Шко́ла э́то.", "Э́то шко́ла.", "Э́то в шко́ле."],
        "correct": "Э́то шко́ла.",
        "explanation": "<p><strong>Э́то шко́ла.</strong> <em>Есть</em> ortiqcha — hozirgi "
                       "zamonda “boʻlmoq” qoʻyilmaydi. Soʻz tartibi ham oʻzgarmaydi: "
                       "avval <strong>э́то</strong>, keyin ot.</p>",
    },
    {
        "text": "<p>Rad javobini tanlang.</p><p><strong>— Э́то соба́ка? — ___</strong></p>",
        "choices": ["Нет, э́то соба́ка не.", "Нет, э́то не соба́ка.",
                    "Не, э́то нет соба́ка.", "Нет соба́ка э́то."],
        "correct": "Нет, э́то не соба́ка.",
        "explanation": "<p><strong>Нет</strong> — javob (“yoʻq”), <strong>не</strong> — "
                       "inkor qilinayotgan soʻzning <strong>oldida</strong>. "
                       "Oʻzbekchadagi “emas” gap oxirida keladi, ruschada esa oldinda — "
                       "shu farq eng koʻp xatoga sabab boʻladi.</p>",
    },
    {
        "text": "<p>Bu darak gapni savolga aylantiring.</p><p><strong>Э́то Ташке́нт.</strong></p>",
        "choices": ["Ташке́нт э́то?", "Э́то ли Ташке́нт?", "Э́то Ташке́нт?",
                    "Ли э́то Ташке́нт?"],
        "correct": "Э́то Ташке́нт?",
        "explanation": "<p>Soʻz tartibi <strong>oʻzgarmaydi</strong> — faqat ohang "
                       "koʻtariladi va savol belgisi qoʻyiladi. Ruschada oʻzbekchadagi "
                       "<em>-mi</em> kabi maxsus vosita yoʻq. (<em>Ли</em> zarrachasi "
                       "bor, lekin u boshqa vaziyatda ishlatiladi — PR-68.)</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то ___ кни́га. Э́то "
                "тетра́дь.</strong></p>",
        "choices": ["не", "нет", "да", "и"],
        "correct": "не",
        "explanation": "<p><strong>Э́то не кни́га</strong> — “Bu kitob emas”. Gap ichida, "
                       "otning oldida <strong>не</strong> turadi. <strong>Нет</strong> "
                       "esa savolga javob sifatida, gap boshida ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Кто э́то? — ___</strong></p>",
        "choices": ["Э́то окно́.", "Э́то Ташке́нт.", "Э́то Дилно́за.", "Э́то шко́ла."],
        "correct": "Э́то Дилно́за.",
        "explanation": "<p><strong>Кто</strong> odam haqida soʻraydi, shuning uchun "
                       "javobda odam boʻlishi kerak — <strong>Дилно́за</strong>. "
                       "Qolgan uchtasi (deraza, shahar, maktab) <strong>Что э́то?</strong> "
                       "savoliga javob boʻladi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bu it emas.</strong></p>",
        "choices": ["Э́то не соба́ка.", "Э́то соба́ка нет.", "Не э́то соба́ка.",
                    "Э́то соба́ка не."],
        "correct": "Э́то не соба́ка.",
        "explanation": "<p><strong>Э́то не соба́ка.</strong> <strong>Не</strong> aynan "
                       "inkor qilinayotgan soʻzning oldida turadi — bu yerda "
                       "<em>соба́ка</em> ning oldida. Uni gap boshiga ham, oxiriga ham "
                       "qoʻyib boʻlmaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>нет</strong> va <strong>не</strong> — farqi nima?</p>",
        "choices": ["Farqi yoʻq, ikkalasi bir xil",
                    "Нет — javob “yoʻq”; не — inkor qilinayotgan soʻz oldidagi zarracha",
                    "Нет — otlar bilan, не — feʼllar bilan",
                    "Нет — rasmiy, не — norasmiy"],
        "correct": "Нет — javob “yoʻq”; не — inkor qilinayotgan soʻz oldidagi zarracha",
        "explanation": "<p>Ular bitta gapda birga ishlaydi: <em>«<strong>Нет</strong>, "
                       "э́то <strong>не</strong> соба́ка»</em> — birinchisi savolga "
                       "javob, ikkinchisi soʻzni inkor qiladi.</p>",
    },
    {
        "text": "<p>Qaysi soʻz haqida <strong>Что э́то?</strong> deb soʻraladi?</p>",
        "choices": ["кот", "Афсо́на", "слова́рь", "учи́тель"],
        "correct": "слова́рь",
        "explanation": "<p><strong>Слова́рь</strong> (lugʻat) — buyum, demak "
                       "<strong>ЧТО</strong>. Qolganlari jonli: <em>кот</em> (hayvon), "
                       "<em>Афсо́на</em> va <em>учи́тель</em> (odamlar) — ular "
                       "<strong>КТО</strong> tomonda.</p>",
    },
    {
        "text": "<p>Rus tilida savol va darak gapni nima ajratadi?</p>",
        "choices": ["Soʻz tartibi", "Maxsus zarracha", "Faqat ohang va savol belgisi",
                    "Feʼlning shakli"],
        "correct": "Faqat ohang va savol belgisi",
        "explanation": "<p><em>Э́то шко́ла.</em> va <em>Э́то шко́ла?</em> — bir xil "
                       "soʻzlar, bir xil tartib. Savolda ovoz eng muhim soʻzda "
                       "koʻtariladi va keyin pasayadi; darak gapda esa oxirigacha bir "
                       "tekis pasayadi.</p>",
    },
    {
        "text": "<p>Mushuk haqida rus tilida qaysi savol beriladi?</p>",
        "choices": ["Кто э́то?", "Что э́то?", "Ikkalasi ham toʻgʻri", "Где э́то?"],
        "correct": "Кто э́то?",
        "explanation": "<p><strong>Кто э́то?</strong> — rus tilida hayvon jonli "
                       "hisoblanadi va <strong>КТО</strong> tomonda turadi. Oʻzbekchada "
                       "bu chegara biroz erkinroq, shuning uchun bu bitta detalni "
                       "alohida eslab qolish kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́то окно́.", "Э́то есть кни́га.", "Э́то не стол.", "Кто э́то?"],
        "correct": "Э́то есть кни́га.",
        "explanation": "<p><strong>Есть</strong> ortiqcha. Toʻgʻrisi — <strong>Э́то "
                       "кни́га.</strong> Rus tilida hozirgi zamonda “boʻlmoq” feʼli "
                       "qoʻyilmaydi. (<em>Есть</em> soʻzining boshqa vazifasi bor — "
                       "egalikni bildiradi, PR-14 da koʻramiz.)</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Э́то соба́ка не.", "Не э́то соба́ка.", "Э́то не соба́ка.",
                    "Э́то нет соба́ка."],
        "correct": "Э́то не соба́ка.",
        "explanation": "<p><strong>Не</strong> inkor qilinayotgan soʻzning bevosita "
                       "oldida turadi. Gap oxiriga qoʻyish — oʻzbekchadagi “emas” ning "
                       "taʼsiri; <em>нет</em> esa bu yerda umuman notoʻgʻri, u faqat "
                       "javob sifatida ishlatiladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>шко́ла / э́то / не</strong></p>",
        "choices": ["Э́то не шко́ла.", "Не шко́ла э́то.", "Шко́ла не э́то.",
                    "Э́то шко́ла не."],
        "correct": "Э́то не шко́ла.",
        "explanation": "<p><strong>Э́то не шко́ла</strong> — “Bu maktab emas”. Tartib "
                       "har doim bir xil: <em>э́то</em> → <em>не</em> → ot.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Э́то кни́га?<br>— Нет, э́то не "
                "кни́га. ___</strong></p>",
        "choices": ["Э́то тетра́дь.", "Кни́га не э́то.", "Да, кни́га.", "Не кни́га э́то."],
        "correct": "Э́то тетра́дь.",
        "explanation": "<p>Tabiiy javob — inkordan keyin <strong>toʻgʻri javobni "
                       "aytish</strong>: <em>Нет, э́то не кни́га. Э́то тетра́дь.</em> "
                       "(daftar). Rus suhbatida rad javobidan keyin deyarli har doim "
                       "aniqlik kiritiladi.</p>",
    },
]


# =====================================================================
# PR-7 — Salomlashish, tanishuv, ты / вы
# =====================================================================

Q_PR7 = [
    # 1–5 tanish
    {
        "text": "<p><strong>Здра́вствуйте</strong> qanday oʻqiladi?</p>",
        "choices": ["[здра́вствуйт'е]", "[здра́ствуйт'е]", "[здара́ствуйт'е]",
                    "[здра́вуйт'е]"],
        "correct": "[здра́ствуйт'е]",
        "explanation": "<p>Oʻrtadagi <strong>в</strong> aytilmaydi: "
                       "<strong>[здра́ствуйт'е]</strong>. Bu birinchi haftaning eng qiyin "
                       "soʻzi — uni boʻlaklab mashq qiling: здра́ — ствуй — те.</p>",
    },
    {
        "text": "<p><strong>Приве́т</strong> kimga aytiladi?</p>",
        "choices": ["Doʻstga, tengdoshga", "Oʻqituvchiga", "Notanish odamga",
                    "Katta yoshdagi qoʻshniga"],
        "correct": "Doʻstga, tengdoshga",
        "explanation": "<p><strong>Приве́т</strong> — norasmiy salom, <strong>ты</strong> "
                       "darajasi. Qolgan uchta holatda <strong>Здра́вствуйте</strong> "
                       "aytiladi, chunki ular <strong>вы</strong> darajasi.</p>",
    },
    {
        "text": "<p><strong>Меня́ зову́т Афсо́на</strong> nima degani?</p>",
        "choices": ["Mening ismim Afsona", "Men Afsonani chaqiraman",
                    "Afsona meni chaqirdi", "Afsona bu yerda"],
        "correct": "Mening ismim Afsona",
        "explanation": "<p>Soʻzma-soʻz: “meni Afsona deb chaqirishadi”. Shuning uchun "
                       "bu iborada “ism” degan soʻz umuman yoʻq — bu turgʻun ibora, "
                       "uni butunlaligicha yodlash kerak.</p>",
    },
    {
        "text": "<p><strong>Как дела́?</strong> ga eng oddiy javob qaysi?</p>",
        "choices": ["Пожа́луйста", "Хорошо́", "До свида́ния", "Извини́те"],
        "correct": "Хорошо́",
        "explanation": "<p><strong>Хорошо́</strong> — “yaxshi”. Yana ishlaydigan "
                       "javoblar: <em>Норма́льно</em> (normal), <em>Непло́хо</em> "
                       "(yomon emas). Javobdan keyin savolni qaytarish odat: "
                       "<em>А вы? / А ты?</em></p>",
    },
    {
        "text": "<p>Rus tilida <strong>вы</strong> nechta vazifani bajaradi?</p>",
        "choices": ["Bitta — faqat hurmat",
                    "Ikkita — hurmat va koʻplik",
                    "Bitta — faqat koʻplik",
                    "Uchta"],
        "correct": "Ikkita — hurmat va koʻplik",
        "explanation": "<p><strong>Вы</strong> ham bitta odamga hurmat bilan murojaat "
                       "(oʻzbekchadagi <em>siz</em>), ham bir nechta odamga murojaat "
                       "(<em>sizlar</em>). Shuning uchun uch nafar doʻstingizga birdan "
                       "gapirsangiz ham <strong>вы</strong> deysiz.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi? Sinfdoshingizga.</p>"
                "<p><strong>Как ___ зову́т?</strong></p>",
        "choices": ["вас", "тебя́", "меня́", "вы"],
        "correct": "тебя́",
        "explanation": "<p>Tengdosh — <strong>ты</strong> darajasi, va bu iborada uning "
                       "shakli <strong>тебя́</strong> boʻladi. Hurmat bilan boʻlsa — "
                       "<strong>вас</strong>. <em>Меня́</em> esa oʻzingiz haqida: "
                       "<em>Меня́ зову́т …</em></p>",
    },
    {
        "text": "<p>Doʻkonda notanish sotuvchiga nima deysiz?</p>",
        "choices": ["Здра́вствуйте!", "Приве́т!", "Пока́!", "Здоро́во!"],
        "correct": "Здра́вствуйте!",
        "explanation": "<p>Notanish odam — <strong>вы</strong> darajasi, demak "
                       "<strong>Здра́вствуйте</strong>. <em>Приве́т</em> va "
                       "<em>Здоро́во</em> bu yerda qoʻpol eshitiladi, <em>Пока́</em> esa "
                       "xayrlashish soʻzi.</p>",
    },
    {
        "text": "<p><strong>Спаси́бо!</strong> ga qanday javob beriladi?</p>",
        "choices": ["Извини́те", "Пожа́луйста", "О́чень прия́тно", "До свида́ния"],
        "correct": "Пожа́луйста",
        "explanation": "<p><strong>Пожа́луйста</strong> ikkita ish qiladi: soʻrovda u "
                       "“iltimos”, rahmatga javobda esa “arzimaydi”. Talaffuzda "
                       "oʻrtasi yutiladi: <strong>[пажа́лустъ]</strong>.</p>",
    },
    {
        "text": "<p>Oʻqituvchingiz bilan xayrlashyapsiz. Nima deysiz?</p>",
        "choices": ["Пока́!", "До свида́ния!", "Приве́т!", "Здоро́во!"],
        "correct": "До свида́ния!",
        "explanation": "<p><strong>До свида́ния</strong> — rasmiy xayrlashish, "
                       "<strong>Здра́вствуйте</strong> ning jufti. <em>Пока́</em> "
                       "doʻstlar orasida ishlatiladi va oʻqituvchiga aytilsa, "
                       "suhbat darajasi birdan tushib ketadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— Как вас зову́т?<br>"
                "— ___ зову́т Жасу́р.</strong></p>",
        "choices": ["Тебя́", "Вас", "Меня́", "Вы"],
        "correct": "Меня́",
        "explanation": "<p><strong>Меня́ зову́т …</strong> — oʻzingiz haqida gapirganda "
                       "har doim shu shakl. U suhbatdoshning kimligiga bogʻliq emas: "
                       "doʻstga ham, oʻqituvchiga ham <strong>меня́</strong>.</p>",
    },
    {
        "text": "<p>Yangi qoʻshningiz sizdan bir oz katta. <strong>Ты</strong> mi yoki "
                "<strong>вы</strong> mi?</p>",
        "choices": ["Вы — ikkilanganda har doim вы", "Ты — u qoʻshni-ku",
                    "Farqi yoʻq", "Ты, chunki u bir oz katta xolos"],
        "correct": "Вы — ikkilanganda har doim вы",
        "explanation": "<p>Qoida oddiy: <strong>ikkilansang — вы</strong>. Ortiqcha hurmat "
                       "hech kimni xafa qilmaydi, oʻrinsiz <strong>ты</strong> esa "
                       "qilishi mumkin. Oʻtishni odatda katta yoshdagi odam taklif "
                       "qiladi: <em>«Дава́й на ты»</em>.</p>",
    },
    {
        "text": "<p>Tanishuv oxirida nima aytiladi?</p>",
        "choices": ["Пожа́луйста", "Как дела́?", "О́чень прия́тно", "Извини́те"],
        "correct": "О́чень прия́тно",
        "explanation": "<p><strong>О́чень прия́тно</strong> — “tanishganimdan xursandman”. "
                       "Har qanday darajada ishlaydi va tanishuvni chiroyli yakunlaydi. "
                       "Suhbatdosh odatda xuddi shu soʻzni qaytaradi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi juftlik bir darajada?</p>",
        "choices": ["Здра́вствуйте — Пока́", "Приве́т — До свида́ния",
                    "Приве́т — Пока́", "Здоро́во — До свида́ния"],
        "correct": "Приве́т — Пока́",
        "explanation": "<p>Ikkalasi ham norasmiy — <strong>ты</strong> darajasi. Rasmiy "
                       "juftlik esa <strong>Здра́вствуйте — До свида́ния</strong>. "
                       "Bir suhbatda bitta darajada qolish kerak.</p>",
    },
    {
        "text": "<p>Rus oilasida ota-onaga qanday murojaat qilinadi?</p>",
        "choices": ["Ты — bu yaqinlik belgisi, qoʻpollik emas",
                    "Вы — har doim, hurmat sifatida",
                    "Вы, faqat bayramlarda ты",
                    "Umuman olmosh ishlatilmaydi"],
        "correct": "Ты — bu yaqinlik belgisi, qoʻpollik emas",
        "explanation": "<p>Bu oʻzbek tilidan farq qiladigan joy: oʻzbek oilasida "
                       "ota-onaga odatda <em>siz</em> deyiladi, rus oilasida esa "
                       "ota-onaga ham, buvi-buvaga ham deyarli doim "
                       "<strong>ты</strong> — bu yaqinlikni bildiradi.</p>",
    },
    {
        "text": "<p><strong>Извини́те</strong> va <strong>Прости́те</strong> — farqi "
                "nima?</p>",
        "choices": ["Farqi yoʻq", "Извини́те — kichik holat va murojaat; Прости́те — "
                    "jiddiyroq uzr", "Извини́те — rasmiy, Прости́те — norasmiy",
                    "Прости́те faqat yozuvda ishlatiladi"],
        "correct": "Извини́те — kichik holat va murojaat; Прости́те — jiddiyroq uzr",
        "explanation": "<p><strong>Извини́те</strong> koʻcha-koʻyda odamga murojaat "
                       "qilishda ham ishlatiladi (“kechirasiz, ...”). "
                       "<strong>Прости́те</strong> esa haqiqiy aybni tan olganda "
                       "kuchliroq eshitiladi.</p>",
    },
    {
        "text": "<p><strong>Пожа́луйста</strong> soʻzining ikkita maʼnosi qaysi?</p>",
        "choices": ["“Iltimos” va “arzimaydi”", "“Rahmat” va “kechirasiz”",
                    "“Ha” va “yoʻq”", "“Salom” va “xayr”"],
        "correct": "“Iltimos” va “arzimaydi”",
        "explanation": "<p>Soʻrovda: <em>Кни́гу, пожа́луйста</em> — “kitob bering, "
                       "iltimos”. Rahmatga javobda: <em>— Спаси́бо! — Пожа́луйста!</em> — "
                       "“arzimaydi”. Bitta soʻz, ikkita vazifa.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor? Oʻqituvchiga murojaat.</p>",
        "choices": ["Здра́вствуйте! Как вас зову́т?", "Здра́вствуйте, Серге́й Петро́вич!",
                    "Приве́т! Как тебя́ зову́т?", "До свида́ния!"],
        "correct": "Приве́т! Как тебя́ зову́т?",
        "explanation": "<p>Oʻqituvchiga <strong>ты</strong> darajasi ishlatilmaydi. "
                       "Toʻgʻrisi: <strong>Здра́вствуйте! Как вас зову́т?</strong> "
                       "Bu yerda ikkita xato birdan — salom ham, olmosh ham noto‘g‘ri "
                       "darajada.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Как зову́т вас?", "Как вас зову́т?", "Как вас зову́т имя?",
                    "Что вас зову́т?"],
        "correct": "Как вас зову́т?",
        "explanation": "<p>Bu <strong>turgʻun ibora</strong> — soʻz tartibi hech qachon "
                       "oʻzgarmaydi va unga “ism” (<em>и́мя</em>) soʻzi qoʻshilmaydi. "
                       "Uni butunlaligicha yodlang.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>зову́т / Дилно́за / "
                "меня́</strong></p>",
        "choices": ["Зову́т меня́ Дилно́за.", "Меня́ зову́т Дилно́за.",
                    "Дилно́за меня́ зову́т.", "Меня́ Дилно́за зову́т."],
        "correct": "Меня́ зову́т Дилно́за.",
        "explanation": "<p><strong>Меня́ зову́т Дилно́за.</strong> Tartib qatʼiy: "
                       "<em>меня́ / тебя́ / вас</em> → <em>зову́т</em> → ism.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring. Notanish ayol bilan.</p>"
                "<p><strong>— Здра́вствуйте! Меня́ зову́т Мари́на. А вас?<br>"
                "— Афсо́на. ___</strong></p>",
        "choices": ["О́чень прия́тно.", "Пока́!", "Как тебя́ зову́т?", "Норма́льно."],
        "correct": "О́чень прия́тно.",
        "explanation": "<p>Tanishuv <strong>О́чень прия́тно</strong> bilan yakunlanadi. "
                       "<em>Пока́</em> bu yerda daraja jihatidan notoʻgʻri (rasmiy "
                       "suhbat), <em>Как тебя́ зову́т?</em> esa ikki marta xato: ism "
                       "allaqachon aytilgan va <strong>ты</strong> darajasi "
                       "oʻrinsiz.</p>",
    },
]


# =====================================================================
# PR-8 — Jins (род)
# =====================================================================

Q_PR8 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida nechta grammatik jins bor?</p>",
        "choices": ["Ikkita", "Uchta", "Toʻrtta", "Jins tushunchasi yoʻq"],
        "correct": "Uchta",
        "explanation": "<p>Uchta: <strong>мужско́й</strong> (erkak), "
                       "<strong>же́нский</strong> (ayol), <strong>сре́дний</strong> "
                       "(oʻrta). Oʻzbek tilida grammatik jins umuman yoʻq — shuning "
                       "uchun bu kursdagi birinchi haqiqatan yangi gʻoya.</p>",
    },
    {
        "text": "<p><strong>кни́га</strong> qaysi jinsda?</p>",
        "choices": ["Erkak", "Ayol", "Oʻrta", "Jinsi yoʻq"],
        "correct": "Ayol",
        "explanation": "<p><strong>-а</strong> bilan tugagan ot — ayol jinsi "
                       "(же́нский род). Olmoshi <strong>она́</strong>, sifat bilan "
                       "<em>но́вая кни́га</em>.</p>",
    },
    {
        "text": "<p><strong>окно́</strong> qaysi olmosh bilan almashtiriladi?</p>",
        "choices": ["он", "она́", "оно́", "они́"],
        "correct": "оно́",
        "explanation": "<p><strong>-о</strong> bilan tugagan ot — oʻrta jins, olmoshi "
                       "<strong>оно́</strong>. Bu shakl oʻzbek oʻquvchisi eng koʻp "
                       "unutadigan shakl, chunki oʻzbekchada uchinchi variant yoʻq.</p>",
    },
    {
        "text": "<p>Otning jinsini eng oson qanday aniqlaysiz?</p>",
        "choices": ["Oxirgi harfiga qarab", "Birinchi harfiga qarab",
                    "Soʻzning uzunligiga qarab", "Urgʻuning joyiga qarab"],
        "correct": "Oxirgi harfiga qarab",
        "explanation": "<p>Undosh → erkak, <strong>-а/-я</strong> → ayol, "
                       "<strong>-о/-е</strong> → oʻrta. Bu qoida soʻzlarning katta "
                       "koʻpchiligida ishlaydi; istisnolar oz va ular ham "
                       "tartibli.</p>",
    },
    {
        "text": "<p>Rus tilida <strong>стол</strong> haqida qaysi olmosh ishlatiladi?</p>",
        "choices": ["он", "она́", "оно́", "э́то"],
        "correct": "он",
        "explanation": "<p><strong>Он</strong> — <em>стол</em> undosh bilan tugaydi, "
                       "demak erkak jinsi. Diqqat: <strong>он</strong> faqat “u (erkak "
                       "kishi)” degani emas — u <strong>har qanday</strong> erkak "
                       "jinsdagi otning oʻrniga turadi, jonsiz buyum boʻlsa ham.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>ко́мната</strong> (xona) qaysi jinsda?</p>",
        "choices": ["Erkak", "Oʻrta", "Ayol", "Ikki xil boʻlishi mumkin"],
        "correct": "Ayol",
        "explanation": "<p><strong>-а</strong> bilan tugaydi → ayol jinsi. Olmoshi "
                       "<strong>она́</strong>: <em>— Где ко́мната? — Она́ здесь.</em></p>",
    },
    {
        "text": "<p><strong>па́па</strong> qaysi jinsda va nega?</p>",
        "choices": ["Ayol — chunki -а bilan tugaydi",
                    "Erkak — chunki maʼno shaklni yutadi",
                    "Oʻrta — chunki bu qarindoshlik soʻzi",
                    "Ikki xil boʻlishi mumkin"],
        "correct": "Erkak — chunki maʼno shaklni yutadi",
        "explanation": "<p>Bu istisno: <strong>tabiiy jins shaklni yutadi</strong>. "
                       "<em>Па́па, де́душка, дя́дя, мужчи́на</em> — hammasi "
                       "<strong>-а</strong> bilan tugaydi, lekin erkak jinsida qoladi, "
                       "chunki ular erkakni bildiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— Где кни́га?<br>"
                "— ___ здесь.</strong></p>",
        "choices": ["Он", "Она́", "Оно́", "Э́то"],
        "correct": "Она́",
        "explanation": "<p><em>Кни́га</em> — ayol jinsi (-а), demak "
                       "<strong>Она́</strong>. Oʻzbekchaga ikkalasi ham “u” deb "
                       "tarjima qilinadi, lekin ruschada tanlov otning jinsiga "
                       "bogʻliq.</p>",
    },
    {
        "text": "<p><strong>мо́ре</strong> (dengiz) qaysi jinsda?</p>",
        "choices": ["Erkak", "Ayol", "Oʻrta", "Jinsi yoʻq"],
        "correct": "Oʻrta",
        "explanation": "<p><strong>-е</strong> bilan tugaydi → oʻrta jins (сре́дний). "
                       "Xuddi shunday: <em>зда́ние</em> (bino), <em>по́ле</em> (dala), "
                       "<em>со́лнце</em> (quyosh).</p>",
    },
    {
        "text": "<p>Qaysi soʻz <strong>ayol</strong> jinsida?</p>",
        "choices": ["слова́рь", "учи́тель", "но́вость", "день"],
        "correct": "но́вость",
        "explanation": "<p><strong>-ость</strong> bilan tugagan ot <strong>har "
                       "doim</strong> ayol jinsida: <em>но́вость, ра́дость, "
                       "мо́лодость</em>. Qolgan uchtasi erkak jinsida: "
                       "<em>слова́рь</em> (-арь), <em>учи́тель</em> (-тель), "
                       "<em>день</em>.</p>",
    },
    {
        "text": "<p><strong>учи́тель</strong> qaysi jinsda?</p>",
        "choices": ["Erkak — -тель bilan tugagan ot har doim erkak jinsida",
                    "Ayol — chunki -ь bilan tugaydi",
                    "Oʻrta", "Kontekstga bogʻliq"],
        "correct": "Erkak — -тель bilan tugagan ot har doim erkak jinsida",
        "explanation": "<p><strong>-тель</strong> va <strong>-арь</strong> — ikkita "
                       "ishonchli belgi: bunday <strong>-ь</strong> li otlar doim erkak "
                       "jinsida. <em>Учи́тель, води́тель, слова́рь, календа́рь.</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— Где окно́?<br>"
                "— ___ здесь.</strong></p>",
        "choices": ["Он", "Она́", "Оно́", "Они́"],
        "correct": "Оно́",
        "explanation": "<p><em>Окно́</em> — oʻrta jins (-о), demak "
                       "<strong>Оно́</strong>. Bu uchinchi shaklni unutmaslik kerak: "
                       "oʻzbekchada faqat bitta “u” bor, ruschada esa uchta.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>дверь</strong> va <strong>слова́рь</strong> — ikkalasi ham "
                "-ь bilan tugaydi. Jinsi bir xilmi?</p>",
        "choices": ["Ha, ikkalasi ayol jinsida", "Ha, ikkalasi erkak jinsida",
                    "Yoʻq: дверь — ayol, слова́рь — erkak",
                    "Yoʻq: дверь — erkak, слова́рь — ayol"],
        "correct": "Yoʻq: дверь — ayol, слова́рь — erkak",
        "explanation": "<p><strong>-ь</strong> bilan tugagan otlarning jinsini oxirgi "
                       "harf <strong>aytmaydi</strong>. Ularni jinsi bilan birga "
                       "yodlash kerak — xuddi urgʻu kabi. Daftaringizga "
                       "<em>дверь (ж.)</em>, <em>слова́рь (м.)</em> deb yozing.</p>",
    },
    {
        "text": "<p>Nega jinsni bilish kerak?</p>",
        "choices": ["Sifat, egalik olmoshi va oʻtgan zamon feʼli unga qarab oʻzgaradi",
                    "Faqat lugʻat uchun kerak", "Faqat yozuvda kerak",
                    "Talaffuzni oʻzgartiradi"],
        "correct": "Sifat, egalik olmoshi va oʻtgan zamon feʼli unga qarab oʻzgaradi",
        "explanation": "<p><em>Но́в<strong>ый</strong> дом — но́в<strong>ая</strong> "
                       "кни́га — но́в<strong>ое</strong> окно́</em>; "
                       "<em>мой / моя́ / моё</em>; <em>был / была́ / бы́ло</em>. "
                       "Uchala qatorda ham bir xil uchlik takrorlanadi — rus tilining "
                       "yarmi shu uchlikdan iborat.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hamma soʻz <strong>oʻrta</strong> jinsda?</p>",
        "choices": ["окно́, мо́ре, сло́во", "стол, дом, брат", "кни́га, шко́ла, ла́мпа",
                    "день, дверь, ночь"],
        "correct": "окно́, мо́ре, сло́во",
        "explanation": "<p>Uchalasi ham <strong>-о</strong> yoki <strong>-е</strong> "
                       "bilan tugaydi → oʻrta jins. Ikkinchi qator erkak, uchinchisi "
                       "ayol, toʻrtinchisi esa aralash (день — erkak, дверь va ночь — "
                       "ayol).</p>",
    },
    {
        "text": "<p>Rus tilida buyumning jinsi bormi?</p>",
        "choices": ["Ha, har bir buyumning haqiqiy jinsi bor",
                    "Yoʻq — jins buyumga emas, SOʻZGA tegishli",
                    "Faqat katta buyumlarning", "Faqat jonli narsalarning"],
        "correct": "Yoʻq — jins buyumga emas, SOʻZGA tegishli",
        "explanation": "<p>Bu muhim farq. <em>Стол</em> — <strong>он</strong>, "
                       "<em>кни́га</em> — <strong>она́</strong>, lekin bu stol yoki "
                       "kitobning oʻziga hech qanday aloqasi yoʻq. Bu shunchaki "
                       "soʻzlarning grammatik guruhlari — xuddi papkalar kabi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Где стол? — Он здесь.", "Где кни́га? — Он здесь.",
                    "Где окно́? — Оно́ здесь.", "Где ла́мпа? — Она́ здесь."],
        "correct": "Где кни́га? — Он здесь.",
        "explanation": "<p><em>Кни́га</em> — ayol jinsi (-а), demak "
                       "<strong>Она́ здесь</strong>. Bu oʻzbek oʻquvchisining eng koʻp "
                       "uchraydigan xatosi: oʻzbekchada bitta “u” bor, shuning uchun "
                       "olmosh oʻz-oʻzidan “он” boʻlib chiqib ketadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Па́па — она́.", "Па́па — оно́.", "Па́па — он.",
                    "Па́па ning jinsi yoʻq."],
        "correct": "Па́па — он.",
        "explanation": "<p><strong>Па́па — он.</strong> Soʻz <strong>-а</strong> bilan "
                       "tugasa ham, u erkakni bildiradi, va bu yerda "
                       "<strong>maʼno shaklni yutadi</strong>. Xuddi shunday: "
                       "<em>де́душка, дя́дя, мужчи́на</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Toʻgʻri juftlikni tanlang.</p><p><strong>тетра́дь — ?</strong></p>",
        "choices": ["он", "она́", "оно́", "э́то"],
        "correct": "она́",
        "explanation": "<p><strong>Тетра́дь</strong> (daftar) — ayol jinsi, olmoshi "
                       "<strong>она́</strong>. Bu <strong>-ь</strong> li otlardan, "
                       "shuning uchun uni jinsi bilan birga yodlash kerak: "
                       "<em>тетра́дь (ж.)</em>.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Что э́то? Э́то дверь?<br>"
                "— Да, э́то дверь. ___ здесь.</strong></p>",
        "choices": ["Он", "Оно́", "Она́", "Они́"],
        "correct": "Она́",
        "explanation": "<p><strong>Она́</strong> — <em>дверь</em> ayol jinsida. "
                       "Diqqat: <em>слова́рь</em> ham <strong>-ь</strong> bilan "
                       "tugaydi, lekin u erkak jinsida (<em>он</em>) — shuning uchun "
                       "bu ikki soʻzni yonma-yon yodlash foydali.</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-6 Mashq: Это — birinchi gapingiz. «Кто это? Что это?»",
        "description": "20 savol — Э́то bilan gap tuzish, Кто/Что farqi, savol ohangi va "
                       "«Нет, э́то не …» rad javobi.",
        "tutorial": "PR-6:",
        "questions": Q_PR6,
    },
    {
        "title": "PR-7 Mashq: Salomlashish, tanishuv va murojaat: ты yoki вы?",
        "description": "20 savol — rasmiy va norasmiy salomlashish, ты/вы tanlovi, "
                       "tanishuv iboralari va xushmuomalalik soʻzlari.",
        "tutorial": "PR-7:",
        "questions": Q_PR7,
    },
    {
        "title": "PR-8 Mashq: Jins (род) — otlarning uch jinsi va uni oxiridan aniqlash",
        "description": "20 savol — uch jins, jinsni oxirgi harfdan aniqlash, он/она́/оно́ "
                       "va -ь bilan tugagan otlar.",
        "tutorial": "PR-8:",
        "questions": Q_PR8,
    },
]
