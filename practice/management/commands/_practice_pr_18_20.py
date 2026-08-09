# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-18 … PR-20.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_18_20.py --master=prime \\
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
# PR-18 — Ravishlar va тоже / также / ещё / уже
# =====================================================================

Q_PR18 = [
    # 1–5 tanish
    {
        "text": "<p>Ravish (наре́чие) otga moslashadimi?</p>",
        "choices": ["Ha, jinsga qarab", "Ha, songa qarab",
                    "Yoʻq — u hech qachon oʻzgarmaydi", "Faqat koʻplikda"],
        "correct": "Yoʻq — u hech qachon oʻzgarmaydi",
        "explanation": "<p>Ravish — oʻn ikki darsdan keyin birinchi <strong>hech nimaga "
                       "moslashmaydigan</strong> soʻz turkumi. Bitta shakl, hamma "
                       "joyda.</p>",
    },
    {
        "text": "<p><strong>бы́стрый</strong> dan ravish yasang.</p>",
        "choices": ["бы́страя", "бы́стро", "бы́строе", "бы́стрые"],
        "correct": "бы́стро",
        "explanation": "<p>Qoida: <strong>-ый → -о</strong>. Xuddi shunday "
                       "<em>ти́хий → ти́хо</em>, <em>краси́вый → краси́во</em>, "
                       "<em>хоро́ший → хорошо́</em>.</p>",
    },
    {
        "text": "<p><strong>уже́</strong> nima degani?</p>",
        "choices": ["allaqachon", "hali", "yana", "hech qachon"],
        "correct": "allaqachon",
        "explanation": "<p><strong>Уже́</strong> — allaqachon. Uning jufti "
                       "<strong>ещё</strong> — hali, yana. Inkor shakllari ham juftlik: "
                       "<em>ещё не</em> (hali … emas) va <em>уже́ не</em> (endi … "
                       "emas).</p>",
    },
    {
        "text": "<p><strong>о́чень</strong> nima degani?</p>",
        "choices": ["juda", "faqat", "koʻp", "doim"],
        "correct": "juda",
        "explanation": "<p><strong>О́чень</strong> sifat va ravishga qoʻshiladi va hech "
                       "qachon oʻzgarmaydi: <em>о́чень большо́й, о́чень больша́я, "
                       "о́чень хорошо́</em>.</p>",
    },
    {
        "text": "<p>Kundalik nutqda “men ham” deyish uchun qaysi soʻz ishlatiladi?</p>",
        "choices": ["та́кже", "то́же", "ещё", "уже́"],
        "correct": "то́же",
        "explanation": "<p><strong>Я то́же.</strong> <em>Тоже</em> yangi <strong>ega</strong> "
                       "qoʻshadi. <em>Также</em> esa yangi narsa qoʻshadi va kitobiyroq — "
                       "u koʻproq yozuvda uchraydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>Здесь ___.</strong> (yaxshi)</p>",
        "choices": ["хоро́ший", "хоро́шая", "хорошо́", "хоро́шие"],
        "correct": "хорошо́",
        "explanation": "<p><strong>Здесь хорошо́.</strong> Gapda ot yoʻq — bu "
                       "<em>holat</em>, demak ravish. Ot boʻlganda sifat kerak boʻlardi: "
                       "<em>хоро́шее ме́сто</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Э́то ___ окно́.</strong> (yaxshi)</p>",
        "choices": ["хорошо́", "хоро́шее", "хоро́ший", "хоро́шая"],
        "correct": "хоро́шее",
        "explanation": "<p><strong>Э́то хоро́шее окно́.</strong> Bu yerda ot bor "
                       "(<em>окно́</em>), demak sifat kerak — va u oʻrta jinsga "
                       "moslashadi. Oldingi savol bilan yonma-yon qoʻying: butun farq "
                       "shu ikki gapda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Он ___ здесь — приди́ за́втра.</strong> "
                "(hali emas)</p>",
        "choices": ["уже́ не", "ещё не", "не ещё", "уже́"],
        "correct": "ещё не",
        "explanation": "<p><strong>Он ещё не здесь</strong> — hali kelmagan, lekin "
                       "keladi. <em>Уже́ не здесь</em> boʻlsa — kelgan edi, ketdi. "
                       "Tartib qatʼiy: <strong>ещё не</strong>, <em>не ещё</em> "
                       "emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>— Я студе́нт. — Я ___.</strong></p>",
        "choices": ["та́кже", "то́же", "ещё", "о́чень"],
        "correct": "то́же",
        "explanation": "<p><strong>Я то́же.</strong> Yangi ega qoʻshilyapti. "
                       "<em>Также</em> bu yerda kitobiy va gʻalati eshitiladi — u "
                       "roʻyxatga narsa qoʻshadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>___ раз, пожа́луйста.</strong> (yana bir marta)</p>",
        "choices": ["Уже́", "Ещё", "То́же", "О́чень"],
        "correct": "Ещё",
        "explanation": "<p><strong>Ещё раз, пожа́луйста.</strong> <em>Ещё</em> “yana, "
                       "koʻproq” maʼnosida ham ishlatiladi: <em>Ещё чай?</em> — darsda "
                       "va dasturxonda har kuni eshitasiz.</p>",
    },
    {
        "text": "<p><strong>лёгкий</strong> dan ravish yasang.</p>",
        "choices": ["лёгко", "легко́", "лёгкое", "лёгкая"],
        "correct": "легко́",
        "explanation": "<p><strong>легко́</strong> — bu kichik istisno: urgʻu koʻchadi va "
                       "<em>ё</em> <em>е</em> ga aylanadi. Qolgan ravishlarda qoida oddiy: "
                       "<em>-ый → -о</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Мы ___ гуля́ем.</strong> (tez-tez)</p>",
        "choices": ["всегда́", "ча́сто", "ре́дко", "никогда́"],
        "correct": "ча́сто",
        "explanation": "<p><strong>ча́сто</strong> — tez-tez. Bu qatordagi boshqalar: "
                       "<em>всегда́</em> (doim), <em>ре́дко</em> (kamdan-kam), "
                       "<em>иногда́</em> (baʼzan).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Oʻzbek va rus tilidagi sifat/ravish farqi nima?</p>",
        "choices": ["Oʻzbekchada koʻpincha bir xil soʻz, ruschada oxiri oʻzgaradi",
                    "Ruschada bir xil soʻz, oʻzbekchada oʻzgaradi",
                    "Ikkala tilda ham bir xil", "Ruschada ravish umuman yoʻq"],
        "correct": "Oʻzbekchada koʻpincha bir xil soʻz, ruschada oxiri oʻzgaradi",
        "explanation": "<p><em>yaxshi kitob</em> — <em>yaxshi oʻqiydi</em>: oʻzbekcha soʻz "
                       "qimirlamaydi. Ruschada esa <em>хоро́ш<strong>ий</strong></em> — "
                       "<em>хорош<strong>о́</strong></em>. Har safar soʻrang: "
                       "<strong>otni</strong> taʼriflayapmanmi yoki "
                       "<strong>harakatni</strong>?</p>",
    },
    {
        "text": "<p><strong>Он ещё не здесь</strong> va <strong>Он уже́ не здесь</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi — hali kelmagan; ikkinchisi — kelgan edi, ketdi",
                    "Birinchisi — ketdi; ikkinchisi — kelmagan",
                    "Farqi yoʻq", "Ikkinchisi notoʻgʻri"],
        "correct": "Birinchisi — hali kelmagan; ikkinchisi — kelgan edi, ketdi",
        "explanation": "<p>Vaqt chizigʻi: <strong>ещё не → уже́ → ещё → уже́ не</strong>. "
                       "Hali boshlanmagan → boshlangan → davom etyapti → tugagan.</p>",
    },
    {
        "text": "<p><strong>Тоже</strong> va <strong>также</strong> — qaysi biri "
                "kitobiyroq?</p>",
        "choices": ["то́же", "та́кже", "Ikkalasi bir xil", "Ikkalasi ham soʻzlashuv"],
        "correct": "та́кже",
        "explanation": "<p><strong>Также</strong> kitobiy va rasmiyroq, u roʻyxatga narsa "
                       "qoʻshadi: <em>Здесь шко́ла, а та́кже библиоте́ка.</em> "
                       "Kundalik nutqda deyarli har doim <strong>тоже</strong>.</p>",
    },
    {
        "text": "<p>Nega <strong>хорошо́</strong> ham sifat, ham ravish boʻlib "
                "koʻrinadi?</p>",
        "choices": ["Chunki oʻrta jinsdagi sifat va ravish bir xil shaklga ega",
                    "Chunki bu istisno soʻz",
                    "Chunki urgʻu ikki joyda", "Chunki u chet soʻz"],
        "correct": "Chunki oʻrta jinsdagi sifat va ravish bir xil shaklga ega",
        "explanation": "<p><em>Э́то хоро́шее окно́</em> (sifat, otga qaraydi) va "
                       "<em>Здесь хорошо́</em> (ravish, holatga qaraydi). Chalkashmaslik "
                       "oson: <strong>ot bormi?</strong> Bor boʻlsa — sifat.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́то о́чень интере́сно.", "Здесь ти́хо.", "Э́то хорошо́ кни́га.",
                    "Он уже́ до́ма."],
        "correct": "Э́то хорошо́ кни́га.",
        "explanation": "<p>Ot bor (<em>кни́га</em>), demak sifat kerak: <strong>хоро́шая "
                       "кни́га</strong>. Ravish otni taʼriflay olmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он не ещё здесь.", "Он ещё не здесь.", "Он ещё здесь не.",
                    "Не он ещё здесь."],
        "correct": "Он ещё не здесь.",
        "explanation": "<p>Tartib qatʼiy: <strong>ещё не</strong> va <strong>уже́ "
                       "не</strong>. Ularni ajratib boʻlmaydi va oʻrinlarini "
                       "almashtirib ham boʻlmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>хорошо́ / о́чень / "
                "здесь</strong></p>",
        "choices": ["Здесь о́чень хорошо́.", "О́чень здесь хорошо́.",
                    "Хорошо́ здесь о́чень.", "О́чень хорошо́ здесь."],
        "correct": "Здесь о́чень хорошо́.",
        "explanation": "<p><strong>Здесь о́чень хорошо́.</strong> <em>О́чень</em> har "
                       "doim oʻzi kuchaytirayotgan soʻzning <strong>oldida</strong> "
                       "turadi — bu yerda <em>хорошо́</em> ning oldida.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Жасу́р ___ здесь?<br>"
                "— Нет, ___ не здесь.</strong></p>",
        "choices": ["уже́ … ещё", "ещё … уже́", "то́же … та́кже", "о́чень … ещё"],
        "correct": "уже́ … ещё",
        "explanation": "<p><strong>— Жасу́р уже́ здесь? — Нет, ещё не здесь.</strong> "
                       "Savol “allaqachon keldimi?”, javob “hali kelmadi”. Bu juftlik "
                       "kundalik nutqda juda tez-tez uchraydi.</p>",
    },
]


# =====================================================================
# PR-19 — Feʼl, infinitiv, ikkita tuslanish
# =====================================================================

Q_PR19 = [
    # 1–5 tanish
    {
        "text": "<p>Infinitiv koʻpincha qaysi harflar bilan tugaydi?</p>",
        "choices": ["-ть", "-ет", "-ю", "-ый"],
        "correct": "-ть",
        "explanation": "<p><strong>-ть</strong> — feʼllarning katta koʻpchiligi "
                       "(<em>чита́ть, рабо́тать</em>). Kamroq: <strong>-ти</strong> "
                       "(<em>идти́</em>) va <strong>-чь</strong> (<em>мочь</em>). "
                       "PR-4 dagi kuzatish shu yerda toʻliq maʼnoga ega boʻldi.</p>",
    },
    {
        "text": "<p>Infinitiv oʻzbekchadagi qaysi shaklga toʻgʻri keladi?</p>",
        "choices": ["-moq", "-man", "-di", "-lar"],
        "correct": "-moq",
        "explanation": "<p><em>чита́<strong>ть</strong></em> = <em>oʻqi<strong>moq</strong></em>. "
                       "Ikkala tilda ham bu shakl <strong>hech kimga tegishli emas</strong> — "
                       "u shunchaki harakatning nomi, lugʻat shakli.</p>",
    },
    {
        "text": "<p>Rus tilida feʼl nechta shaxs boʻyicha oʻzgaradi?</p>",
        "choices": ["Toʻrtta", "Oltita", "Uchta", "Ikkita"],
        "correct": "Oltita",
        "explanation": "<p>Oltita: <strong>я, ты, он/она́/оно́, мы, вы, они́</strong> — "
                       "PR-10 dagi olmoshlarning har biri uchun bittadan.</p>",
    },
    {
        "text": "<p>Rus tilida nechta tuslanish (спряже́ние) bor?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Oltita"],
        "correct": "Ikkita",
        "explanation": "<p>Ikkita: <strong>I</strong> (belgisi <strong>Е</strong>: "
                       "чита́<em>ешь</em>) va <strong>II</strong> (belgisi "
                       "<strong>И</strong>: говор<em>и́шь</em>). Guruh qoʻshimchalar "
                       "toʻplamini hal qiladi.</p>",
    },
    {
        "text": "<p>Tuslanishni aniqlashning eng ishonchli yoʻli qaysi?</p>",
        "choices": ["Infinitiv oxiriga qarash", "«Ты» shakliga qarash",
                    "Urgʻuga qarash", "Soʻz uzunligiga qarash"],
        "correct": "«Ты» shakliga qarash",
        "explanation": "<p><strong>-ешь</strong> → I tuslanish, <strong>-ишь</strong> → "
                       "II tuslanish. Infinitiv faqat maslahat beradi: masalan "
                       "<em>смотре́ть</em> <em>-еть</em> bilan tugaydi, lekin II "
                       "tuslanishda (<em>смотри́шь</em>).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>говори́шь</strong> — qaysi tuslanish?</p>",
        "choices": ["I", "II", "Ikkalasi ham", "Aniqlab boʻlmaydi"],
        "correct": "II",
        "explanation": "<p><strong>II</strong> — «ты» shaklida <strong>-ишь</strong> "
                       "turibdi. I tuslanishda <strong>-ешь</strong> boʻlardi: "
                       "<em>чита́ешь</em>.</p>",
    },
    {
        "text": "<p><strong>рабо́тать</strong> soʻzining oʻzagi qaysi?</p>",
        "choices": ["рабо́т-", "рабо́та-", "рабо́тать-", "-ать"],
        "correct": "рабо́та-",
        "explanation": "<p>Oʻzak = infinitiv minus <strong>-ть</strong>: "
                       "<em>рабо́тать → рабо́та-</em>. Unga oltita qoʻshimcha "
                       "navbat bilan qoʻshiladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я чита́ть кни́гу.", "Я чита́ю кни́гу.", "Я кни́гу чита́ть.",
                    "Чита́ть я кни́гу."],
        "correct": "Я чита́ю кни́гу.",
        "explanation": "<p>Infinitiv gapda kesim boʻla olmaydi — uni tuslash kerak. "
                       "Va soʻz tartibi: <strong>ega → feʼl → toʻldiruvchi</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Он ___.</strong> (чита́ть)</p>",
        "choices": ["чита́ю", "чита́ешь", "чита́ет", "чита́ют"],
        "correct": "чита́ет",
        "explanation": "<p><strong>чита́ет</strong> — 3-shaxs birlik uchun "
                       "<strong>-ет</strong>. Qoʻshimcha har doim <strong>egaga</strong> "
                       "moslashadi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Jasur ishlamaydi.</strong></p>",
        "choices": ["Жасу́р рабо́тает не.", "Жасу́р не рабо́тает.",
                    "Жасу́р нет рабо́тает.", "Не Жасу́р рабо́тает."],
        "correct": "Жасу́р не рабо́тает.",
        "explanation": "<p><strong>Не</strong> feʼlning <strong>oldida</strong> turadi "
                       "(PR-17). Oʻzbekchada inkor qoʻshimcha ichiga kiradi "
                       "(<em>ishla-MA-ydi</em>), ruschada esa alohida soʻz "
                       "boʻlib oldinda turadi.</p>",
    },
    {
        "text": "<p>Yangi feʼlni lugʻatdan koʻchirayotganda nechta shaklni yozish "
                "kerak?</p>",
        "choices": ["Bittani — infinitivni", "Ikkitani — infinitiv va «ты» shakli",
                    "Oltitani", "Uchtani"],
        "correct": "Ikkitani — infinitiv va «ты» shakli",
        "explanation": "<p>«Ты» shakli tuslanishni aytib beradi, va undan qolgan beshta "
                       "shakl oʻz-oʻzidan kelib chiqadi. Bu yodlashning eng arzon "
                       "yoʻli.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Мы ___.</strong> (знать)</p>",
        "choices": ["зна́ю", "зна́ешь", "зна́ем", "зна́ют"],
        "correct": "зна́ем",
        "explanation": "<p><strong>зна́ем</strong> — <em>мы</em> uchun I tuslanish "
                       "qoʻshimchasi <strong>-ем</strong>. Oʻzak <strong>зна́-</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Rus va oʻzbek feʼl tizimining <strong>asosiy farqi</strong> nima?</p>",
        "choices": ["Soʻz tartibi: oʻzbekchada feʼl oxirida, ruschada oʻrtada",
                    "Ruschada qoʻshimcha yoʻq",
                    "Oʻzbekchada shaxs koʻrsatilmaydi",
                    "Farqi yoʻq"],
        "correct": "Soʻz tartibi: oʻzbekchada feʼl oxirida, ruschada oʻrtada",
        "explanation": "<p>Qoʻshimcha tizimi ikkala tilda ham bir xil ishlaydi (oʻzak + "
                       "shaxs qoʻshimchasi). Lekin <em>Men kitob <strong>oʻqiyman</strong></em> "
                       "→ <em>Я <strong>чита́ю</strong> кни́гу</em>. Har bir gapda feʼlni "
                       "oldinga suring.</p>",
    },
    {
        "text": "<p>Nega rus feʼl tizimi oʻzbek oʻquvchisi uchun ingliz tilini "
                "oʻrganganga qaraganda osonroq?</p>",
        "choices": ["Chunki oʻzbekchada ham oʻzak + shaxs qoʻshimchasi tizimi bor",
                    "Chunki rus feʼllari oʻzgarmaydi",
                    "Chunki oʻzbekchada ham ikkita tuslanish bor",
                    "Chunki soʻz tartibi bir xil"],
        "correct": "Chunki oʻzbekchada ham oʻzak + shaxs qoʻshimchasi tizimi bor",
        "explanation": "<p><em>oʻqi-y-<strong>man</strong> / oʻqi-y-<strong>san</strong></em> "
                       "= <em>чита́-<strong>ю</strong> / чита́-<strong>ешь</strong></em>. "
                       "Ingliz tilida bunday tizim yoʻq (<em>I read, you read</em>), "
                       "shuning uchun bu joyda siz oldindasiz.</p>",
    },
    {
        "text": "<p><strong>смотре́ть</strong> <em>-еть</em> bilan tugaydi. Bu qaysi "
                "tuslanish?</p>",
        "choices": ["I — chunki -еть", "II — buni «ты» shakli koʻrsatadi: смо́тришь",
                    "Aniqlab boʻlmaydi", "Uchinchi tuslanish"],
        "correct": "II — buni «ты» shakli koʻrsatadi: смо́тришь",
        "explanation": "<p>Aynan shuning uchun infinitivga ishonib boʻlmaydi. "
                       "<em>Смотре́ть</em> <em>-еть</em> bilan tugasa ham II "
                       "tuslanishda. Ishonchli belgi — <strong>«ты» shakli</strong>.</p>",
    },
    {
        "text": "<p>Rus tilida olmoshni tushirib qoldirish mumkinmi?</p>",
        "choices": ["Mumkin, lekin odatda saqlanadi", "Yoʻq, hech qachon",
                    "Ha, har doim tushiriladi", "Faqat koʻplikda"],
        "correct": "Mumkin, lekin odatda saqlanadi",
        "explanation": "<p>Oʻzbekchada <em>“Oʻqiyman”</em> — “men” aytilmaydi. Ruschada "
                       "esa <em>Я чита́ю</em> deyish odatiy; olmoshsiz shakl soʻzlashuv "
                       "uslubi hisoblanadi. Boshida har doim olmosh bilan "
                       "gapiring.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi shakl notoʻgʻri?</p>",
        "choices": ["чита́ешь", "говори́шь", "говори́ешь", "зна́ешь"],
        "correct": "говори́ешь",
        "explanation": "<p>Toʻgʻrisi <strong>говори́шь</strong>. <em>Говори́ть</em> II "
                       "tuslanishda, demak <strong>-ишь</strong>. <strong>-ешь</strong> "
                       "faqat I tuslanish uchun.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он чита́ет.", "Мы рабо́таем.", "Он чита́ю.", "Они́ зна́ют."],
        "correct": "Он чита́ю.",
        "explanation": "<p>Toʻgʻrisi <strong>Он чита́ет</strong>. Qoʻshimcha "
                       "<strong>-ю</strong> faqat <em>я</em> uchun. Feʼl har doim egaga "
                       "moslashadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tabiiy tartibga soling.</p><p><strong>кни́гу / чита́ю / "
                "я</strong></p>",
        "choices": ["Я чита́ю кни́гу.", "Я кни́гу чита́ю.", "Кни́гу я чита́ю.",
                    "Чита́ю я кни́гу."],
        "correct": "Я чита́ю кни́гу.",
        "explanation": "<p><strong>Ega → feʼl → toʻldiruvchi.</strong> Oʻzbekchada feʼl "
                       "oxirda boʻlardi (<em>Men kitob oʻqiyman</em>) — ruschada uni "
                       "oldinga suring. Qolgan variantlar grammatik jihatdan mumkin, "
                       "lekin ular taʼkidli va oddiy gap uchun gʻalati.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Ты ___ по-ру́сски?<br>"
                "— Да, немно́го.</strong> (говори́ть)</p>",
        "choices": ["говори́ешь", "говори́шь", "говорю́", "говоря́т"],
        "correct": "говори́шь",
        "explanation": "<p><strong>говори́шь</strong> — <em>ты</em> shakli, II tuslanish "
                       "(<strong>-ишь</strong>). Bu savol tanishuvda deyarli har doim "
                       "beriladi, shuning uchun uni tayyor holda yodlang.</p>",
    },
]


# =====================================================================
# PR-20 — I tuslanish
# =====================================================================

Q_PR20 = [
    # 1–5 tanish
    {
        "text": "<p>I tuslanishning oltita qoʻshimchasi qaysi?</p>",
        "choices": ["-ю, -ешь, -ет, -ем, -ете, -ют", "-ю, -ишь, -ит, -им, -ите, -ят",
                    "-у, -ашь, -ат, -ам, -ате, -ают", "-ый, -ая, -ое, -ые, -ий, -ие"],
        "correct": "-ю, -ешь, -ет, -ем, -ете, -ют",
        "explanation": "<p>“<strong>Е</strong> qatori, ikki tomonida <strong>Ю</strong>”. "
                       "Ikkinchi variant — II tuslanish qoʻshimchalari.</p>",
    },
    {
        "text": "<p><strong>чита́ть</strong> soʻzining oʻzagi qaysi?</p>",
        "choices": ["чит-", "чита́-", "чита́т-", "-ать"],
        "correct": "чита́-",
        "explanation": "<p>Oʻzak = infinitiv minus <strong>-ть</strong>: "
                       "<em>чита́ть → чита́-</em>. Keyin oltita qoʻshimcha "
                       "qoʻshiladi.</p>",
    },
    {
        "text": "<p><strong>я</strong> uchun I tuslanish qoʻshimchasi qaysi?</p>",
        "choices": ["-ю", "-ешь", "-ет", "-ют"],
        "correct": "-ю",
        "explanation": "<p><strong>-ю</strong>: <em>чита́ю, рабо́таю, зна́ю</em>. "
                       "Diqqat: <em>они́</em> uchun ham <strong>Ю</strong> bor, lekin u "
                       "<strong>-ют</strong>.</p>",
    },
    {
        "text": "<p><strong>они́</strong> uchun I tuslanish qoʻshimchasi qaysi?</p>",
        "choices": ["-ет", "-ют", "-ем", "-ят"],
        "correct": "-ют",
        "explanation": "<p><strong>-ют</strong>: <em>чита́ют, рабо́тают, гуля́ют</em>. "
                       "<strong>-ят</strong> esa II tuslanish uchun "
                       "(<em>говоря́т</em>).</p>",
    },
    {
        "text": "<p>Bu darsdagi feʼllarda urgʻu qayerda?</p>",
        "choices": ["Oʻzakda va u qimirlamaydi", "Qoʻshimchada", "Har safar boshqa joyda",
                    "Urgʻu yoʻq"],
        "correct": "Oʻzakda va u qimirlamaydi",
        "explanation": "<p><em>чита́ю, чита́ешь, чита́ет…</em> — urgʻu <strong>чита́-</strong> "
                       "da qoladi. Ba'zi I tuslanish feʼllarida urgʻu qoʻshimchaga "
                       "tushadi (<em>живу́, живёшь</em>) — ular PR-22 da.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga: <strong>Мы ___.</strong> (рабо́тать)</p>",
        "choices": ["рабо́таю", "рабо́таешь", "рабо́таем", "рабо́тают"],
        "correct": "рабо́таем",
        "explanation": "<p><strong>рабо́таем</strong>. Oʻzak <strong>рабо́та-</strong>, "
                       "<em>мы</em> uchun qoʻshimcha <strong>-ем</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Они́ ___ ка́ждый день.</strong> (гуля́ть)</p>",
        "choices": ["гуля́ет", "гуля́ю", "гуля́ем", "гуля́ют"],
        "correct": "гуля́ют",
        "explanation": "<p><strong>гуля́ют</strong>. <em>Они́</em> — 3-shaxs koʻplik, "
                       "demak <strong>-ют</strong>. Oʻzak <strong>гуля́-</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Вы ___ по-ру́сски?</strong> (понима́ть)</p>",
        "choices": ["понима́ешь", "понима́ете", "понима́ем", "понима́ют"],
        "correct": "понима́ете",
        "explanation": "<p><strong>понима́ете</strong> — <em>вы</em> uchun "
                       "<strong>-ете</strong>. Bu shakl hurmat bilan murojaatda ham, "
                       "koʻplikda ham ishlatiladi (PR-7).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring: <strong>Bilmayman.</strong></p>",
        "choices": ["Я не знать.", "Я нет зна́ю.", "Я зна́ю не.", "Я не зна́ю."],
        "correct": "Я не зна́ю.",
        "explanation": "<p><strong>Я не зна́ю.</strong> <em>Не</em> feʼlning oldida "
                       "(PR-17), va infinitiv kesim boʻla olmaydi. Bu rus tilidagi eng "
                       "koʻp aytiladigan gaplardan biri.</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Жасу́р ___ бы́стро.</strong> (рабо́тать)</p>",
        "choices": ["рабо́таю", "рабо́тает", "рабо́таем", "рабо́тают"],
        "correct": "рабо́тает",
        "explanation": "<p><strong>рабо́тает</strong> — <em>Жасу́р</em> = <em>он</em>, "
                       "3-shaxs birlik, demak <strong>-ет</strong>. <em>Бы́стро</em> — "
                       "ravish, u harakatni taʼriflaydi (PR-18).</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Ты ___ му́зыку?</strong> (слу́шать)</p>",
        "choices": ["слу́шаю", "слу́шаешь", "слу́шает", "слу́шают"],
        "correct": "слу́шаешь",
        "explanation": "<p><strong>слу́шаешь</strong> — <em>ты</em> uchun "
                       "<strong>-ешь</strong>. Bu <strong>-ешь</strong> aynan I "
                       "tuslanishning belgisi (PR-19).</p>",
    },
    {
        "text": "<p>Boʻsh joyga: <strong>Я ___, что э́то легко́.</strong> (ду́мать)</p>",
        "choices": ["ду́маю", "ду́маешь", "ду́мает", "ду́мают"],
        "correct": "ду́маю",
        "explanation": "<p><strong>Я ду́маю…</strong> — <em>я</em> uchun "
                       "<strong>-ю</strong>. Bu ibora fikr bildirishda doim "
                       "ishlatiladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>Он чита́ет</strong> va <strong>Они́ чита́ют</strong> — bu "
                "juftlikda nima adashtiriladi?</p>",
        "choices": ["3-shaxs birlik (-ет) va koʻplik (-ют)",
                    "1-shaxs va 2-shaxs", "Oʻtgan va hozirgi zamon", "Jins"],
        "correct": "3-shaxs birlik (-ет) va koʻplik (-ют)",
        "explanation": "<p>Bu eng koʻp uchraydigan xato. <strong>-ет</strong> — bitta "
                       "odam, <strong>-ют</strong> — bir nechta. Oʻzbekchada bu farq "
                       "kuchsizroq (<em>oʻqiydi</em> ikkalasiga ham yetadi), shuning "
                       "uchun quloq uni sezmaydi.</p>",
    },
    {
        "text": "<p>Oʻzbek va rus feʼl qoʻshimchalari nima bilan oʻxshash?</p>",
        "choices": ["Ikkalasida ham oʻzak qimirlamaydi, faqat oxiri almashadi",
                    "Ikkalasida ham qoʻshimcha soʻz oldida turadi",
                    "Ikkalasida ham bitta shakl bor",
                    "Hech nima bilan"],
        "correct": "Ikkalasida ham oʻzak qimirlamaydi, faqat oxiri almashadi",
        "explanation": "<p><em>ishla-y-<strong>man</strong> / ishla-y-<strong>san</strong></em> "
                       "= <em>рабо́та-<strong>ю</strong> / рабо́та-<strong>ешь</strong></em>. "
                       "Shuning uchun bu dars siz uchun yangi tushuncha emas — yangi "
                       "qoʻshimchalar roʻyxati.</p>",
    },
    {
        "text": "<p><strong>жить</strong> feʼli nega bu darsga kirmaydi?</p>",
        "choices": ["Chunki uning oʻzagi oʻzgaradi: живу́, живёшь",
                    "Chunki u II tuslanishda", "Chunki u kam ishlatiladi",
                    "Chunki u infinitiv emas"],
        "correct": "Chunki uning oʻzagi oʻzgaradi: живу́, живёшь",
        "explanation": "<p><em>Жить</em> I tuslanishda, lekin oʻzagi "
                       "<strong>жи- → жив-</strong> boʻlib oʻzgaradi va urgʻu "
                       "qoʻshimchaga tushadi. Bunday feʼllar PR-22 da.</p>",
    },
    {
        "text": "<p>Nega <strong>живёшь</strong> da <strong>-ёшь</strong>, "
                "<strong>-ешь</strong> emas?</p>",
        "choices": ["Chunki urgʻu qoʻshimchaga tushgan, va urgʻuli Е → Ё",
                    "Chunki bu II tuslanish", "Chunki oʻzak Ж bilan tugaydi",
                    "Bu xato"],
        "correct": "Chunki urgʻu qoʻshimchaga tushgan, va urgʻuli Е → Ё",
        "explanation": "<p>PR-2 dagi qoida: <strong>ё har doim urgʻuli</strong>. Urgʻu "
                       "qoʻshimchaga tushganda <em>-ешь</em> <strong>-ёшь</strong> "
                       "boʻlib yoziladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi shakl notoʻgʻri?</p>",
        "choices": ["вы зна́ете", "она́ де́лает", "они́ ду́мает", "мы слу́шаем"],
        "correct": "они́ ду́мает",
        "explanation": "<p>Toʻgʻrisi <strong>они́ ду́мают</strong>. <strong>-ет</strong> "
                       "faqat <em>он / она́ / оно́</em> uchun; koʻplik "
                       "<strong>-ют</strong> oladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я хорошо́ рабо́тает.", "Я хорошо́ рабо́таю.", "Я хоро́ший рабо́таю.",
                    "Я рабо́тать хорошо́."],
        "correct": "Я хорошо́ рабо́таю.",
        "explanation": "<p>Uchta narsa toʻgʻri: feʼl <strong>egaga</strong> moslashadi "
                       "(<em>я → -ю</em>), harakatni <strong>ravish</strong> taʼriflaydi "
                       "(<em>хорошо́</em>, <em>хоро́ший</em> emas), va infinitiv kesim "
                       "boʻla olmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni tartibga soling.</p><p><strong>ка́ждый день / игра́ет / "
                "Шербе́к</strong></p>",
        "choices": ["Шербе́к игра́ет ка́ждый день.",
                    "Шербе́к ка́ждый день игра́ет.",
                    "Ка́ждый день Шербе́к игра́ет.",
                    "Игра́ет Шербе́к ка́ждый день."],
        "correct": "Шербе́к игра́ет ка́ждый день.",
        "explanation": "<p><strong>Ega → feʼl → qolgani.</strong> Vaqt ifodasi odatda "
                       "oxirida turadi. Ikkinchi variant — oʻzbekcha tartib, u ruschada "
                       "taʼkidli va gʻalati eshitiladi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p><p><strong>— Вы понима́ете?<br>"
                "— Да, ___. Но ме́дленно.</strong></p>",
        "choices": ["понима́ю", "понима́ешь", "понима́ет", "понима́ем"],
        "correct": "понима́ю",
        "explanation": "<p><strong>понима́ю</strong> — javob bergan odam oʻzi haqida "
                       "gapiryapti (<em>я</em>). Qisqa javobda olmoshni tushirish "
                       "mumkin: qoʻshimcha <strong>-ю</strong> allaqachon “men” ni "
                       "aytib turibdi.</p>",
    },
]


# =====================================================================

PRACTICES = [
    {
        "title": "PR-18 Mashq: Ravishlar va тоже / также / ещё / уже",
        "description": "20 savol — sifatdan ravish yasash, sifat va ravish farqi, "
                       "тоже/также, ещё/уже́ va ularning inkori.",
        "tutorial": "PR-18:",
        "questions": Q_PR18,
    },
    {
        "title": "PR-19 Mashq: Feʼl nima? Infinitiv va ikkita tuslanish (спряжение)",
        "description": "20 savol — infinitiv, oltita shaxs, I va II tuslanishni ajratish "
                       "va rus soʻz tartibi.",
        "tutorial": "PR-19:",
        "questions": Q_PR19,
    },
    {
        "title": "PR-20 Mashq: I tuslanish: читать, работать, знать",
        "description": "20 savol — oltita qoʻshimcha, oʻzakni topish, oʻnga yaqin "
                       "kundalik feʼl, inkor va soʻz tartibi.",
        "tutorial": "PR-20:",
        "questions": Q_PR20,
    },
]
