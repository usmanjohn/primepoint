# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-32 … PR-34.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_32_34.py --master=prime \\
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
# PR-32 — Винительный 1: jonli va jonsiz
# =====================================================================

Q_PR32 = [
    # 1–5 tanish
    {
        "text": "<p>Вини́тельный padeji oʻzbekchadagi qaysi qoʻshimchaga toʻgʻri "
                "keladi?</p>",
        "choices": ["-ning", "-ga", "-ni", "-da"],
        "correct": "-ni",
        "explanation": "<p><em>kitob<strong>ni</strong> oʻqiyman</em> → <em>чита́ю "
                       "кни́г<strong>у</strong></em>. Savoli: <em>кого́? что?</em> — "
                       "bu toʻldiruvchi kelishigi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́ю ___.</strong> "
                "(кни́га)</p>",
        "choices": ["кни́га", "кни́ги", "кни́гу", "кни́ге"],
        "correct": "кни́гу",
        "explanation": "<p>Ayol jinsi Вини́тельный'da har doim <strong>-у</strong> "
                       "oladi: <em>-а → -у</em>. Jonli/jonsiz bu yerda umuman "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>Oʻrta jinsdagi ot Вини́тельный'da qanday oʻzgaradi?</p>",
        "choices": ["-о → -у", "-о → -а", "Umuman oʻzgarmaydi", "-о → -е"],
        "correct": "Umuman oʻzgarmaydi",
        "explanation": "<p><em>окно́ → окно́</em>, <em>письмо́ → письмо́</em>, "
                       "<em>мо́ре → мо́ре</em>. Oʻrta jins bu kelishikda hech qanday "
                       "holatda oʻzgarmaydi — bu tekin beriladigan qism.</p>",
    },
    {
        "text": "<p>Grammatikada <strong>jonli</strong> (одушевлённое) nima "
                "hisoblanadi?</p>",
        "choices": ["Faqat odam", "Odam va hayvon",
                    "Odam, hayvon va oʻsimlik", "Harakat qiladigan hamma narsa"],
        "correct": "Odam va hayvon",
        "explanation": "<p>Chegara sof grammatik: <em>кот, соба́ка, ры́ба</em> — "
                       "jonli. Oʻsimlik, mashina, poyezd — jonsiz. <em>Наро́д</em> va "
                       "<em>класс</em> odamlardan iborat boʻlsa ham grammatik jihatdan "
                       "jonsiz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я жду ___.</strong> "
                "(ты)</p>",
        "choices": ["ты", "тебе́", "тебя́", "тобо́й"],
        "correct": "тебя́",
        "explanation": "<p>Olmoshlar ham kelishikka kiradi: <em>меня́, тебя́, его́, "
                       "её, нас, вас, их</em>. <em>«Я жду ты»</em> — xato.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д ждёт ___.</strong> "
                "(Жасу́р)</p>",
        "choices": ["Жасу́р", "Жасу́ра", "Жасу́ру", "Жасу́ре"],
        "correct": "Жасу́ра",
        "explanation": "<p>Jasur — odam, demak <strong>jonli erkak</strong>, demak "
                       "<strong>-а</strong>. Agar avtobus kutayotgan boʻlsa, hech "
                       "narsa qoʻshilmasdi: <em>ждёт авто́бус</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Оле́г ждёт ___.</strong> "
                "(по́езд)</p>",
        "choices": ["по́езд", "по́езда", "по́езду", "по́езде"],
        "correct": "по́езд",
        "explanation": "<p>Poyezd — narsa, demak <strong>jonsiz erkak</strong>, va "
                       "uning shakli bosh kelishik bilan bir xil qoladi. Solishtiring: "
                       "<em>ждёт бра́та</em> (jonli).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы слу́шаем ___.</strong> "
                "(му́зыка)</p>",
        "choices": ["му́зыка", "му́зыки", "му́зыку", "му́зыке"],
        "correct": "му́зыку",
        "explanation": "<p>Ayol jinsi — <strong>-у</strong>. <em>Му́зыка</em> jonsiz, "
                       "lekin bu ahamiyatsiz: ayol jinsida jonlilik hech qachon "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он пи́шет ___.</strong> "
                "(письмо́)</p>",
        "choices": ["письмо́", "письма́", "письму́", "письме́"],
        "correct": "письмо́",
        "explanation": "<p>Oʻrta jins — hech narsa qilinmaydi. <em>Пи́сьма</em> "
                       "koʻplik boʻlardi, bu esa bitta xat.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы зна́ем ___.</strong> "
                "(учи́тель)</p>",
        "choices": ["учи́тель", "учи́теля", "учи́телю", "учи́теле"],
        "correct": "учи́теля",
        "explanation": "<p>Oʻqituvchi — odam, demak jonli. Soʻz <strong>-ь</strong> ga "
                       "tugaydi, shuning uchun <strong>-я</strong> oladi: "
                       "<em>учи́тел<strong>я</strong></em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___.</strong> "
                "(оте́ц)</p>",
        "choices": ["оте́ц", "отеца́", "отца́", "отцу́"],
        "correct": "отца́",
        "explanation": "<p>Jonli erkak, demak <strong>-а</strong>. Va bu soʻzda "
                       "<strong>Е tushib qoladi</strong>: <em>оте́ц → отца́</em>. "
                       "Bunday «qochoq unli» rus tilida koʻp uchraydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ лю́бит ___.</strong> "
                "(кот)</p>",
        "choices": ["кот", "кота́", "коту́", "коте́"],
        "correct": "кота́",
        "explanation": "<p>Mushuk — hayvon, demak <strong>jonli</strong>. "
                       "Grammatikada jonli = odam <strong>yoki hayvon</strong>, shuning "
                       "uchun <em>кот → кота́</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega bu ikki gapda bir xil jinsdagi ot boshqacha koʻrinadi?</p>"
                "<p><strong>Я ви́жу стол. · Я ви́жу бра́та.</strong></p>",
        "choices": ["Jonlilik farqi: стол — jonsiz, брат — jonli",
                    "Bu ikki xil kelishik",
                    "Chunki «брат» qisqaroq",
                    "Bu gaplardan biri xato"],
        "correct": "Jonlilik farqi: стол — jonsiz, брат — jonli",
        "explanation": "<p>Ikkalasi ham erkak jinsida va ikkalasi ham Вини́тельный'da. "
                       "Farqni faqat jonlilik hal qildi: jonsiz — oʻzgarmaydi, jonli — "
                       "<strong>-а</strong> oladi.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda ikkalasi ham <strong>oʻzgarmaydi</strong>?</p>",
        "choices": ["кни́га va ма́ма", "окно́ va авто́бус",
                    "брат va учи́тель", "Ка́тя va Афсо́на"],
        "correct": "окно́ va авто́бус",
        "explanation": "<p><em>Окно́</em> — oʻrta jins (hech qachon oʻzgarmaydi), "
                       "<em>авто́бус</em> — jonsiz erkak (u ham oʻzgarmaydi). Qolgan "
                       "juftliklarning hammasi qoʻshimcha oladi.</p>",
    },
    {
        "text": "<p>Oʻzbekcha va ruscha toʻldiruvchining eng muhim farqi nima?</p>",
        "choices": ["Oʻzbekchada -ni ni tushirib qoldirish mumkin, ruschada yoʻq",
                    "Oʻzbekchada toʻldiruvchi gap boshida turadi",
                    "Ruschada toʻldiruvchi umuman belgilanmaydi",
                    "Farq yoʻq"],
        "correct": "Oʻzbekchada -ni ni tushirib qoldirish mumkin, ruschada yoʻq",
        "explanation": "<p><em>Kitob oʻqiyapman</em> va <em>kitobni oʻqiyapman</em> — "
                       "ikkalasi ham toʻgʻri oʻzbekcha. Ruschada esa <em>«Я чита́ю "
                       "кни́га»</em> hech qanday holatda toʻgʻri emas. Oʻzbek oʻquvchi "
                       "aynan shu odat tufayli qoʻshimchani unutadi.</p>",
    },
    {
        "text": "<p><strong>его́</strong> qanday oʻqiladi?</p>",
        "choices": ["[его́]", "[йиво́]", "[эго́]", "[йего́]"],
        "correct": "[йиво́]",
        "explanation": "<p><strong>Г</strong> harfi bu yerda <strong>[в]</strong> "
                       "tovushini beradi — bu eski qoidaning qoldigʻi. Xuddi shunday: "
                       "<em>сего́дня</em> [сиво́дня], <em>ничего́</em> "
                       "[ничиво́].</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я чита́ю письмо́.", "Она́ лю́бит кота́.",
                    "Мы ждём по́езда.", "Он зна́ет Ка́тю."],
        "correct": "Мы ждём по́езда.",
        "explanation": "<p>Toʻgʻrisi — <strong>Мы ждём по́езд</strong>. Poyezd jonsiz, "
                       "demak shakl oʻzgarmaydi. <em>По́езда</em> shakli Роди́тельный "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Жасу́р ждёт Афсо́на.", "Жасу́р ждёт Афсо́ну.",
                    "Жасу́р ждёт Афсо́ны.", "Жасу́р ждёт Афсо́не."],
        "correct": "Жасу́р ждёт Афсо́ну.",
        "explanation": "<p>Afsona — ayol jinsi, demak <strong>-а → -у</strong>. "
                       "Ismlar ham oddiy otlar kabi kelishikka kiradi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Кого́ ты ждёшь?</strong></p>",
        "choices": ["— Бра́та.", "— Брат.", "— Бра́ту.", "— О бра́те."],
        "correct": "— Бра́та.",
        "explanation": "<p>Savol <em>кого́?</em> — Вини́тельный, jonli. Javob ham shu "
                       "shaklda: <strong>бра́та</strong>. Agar savol <em>что "
                       "ждёшь?</em> boʻlganda javob <em>авто́бус</em> boʻlardi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Men onamni yaxshi "
                "koʻraman va akamni kutyapman.</strong></p>",
        "choices": ["Я люблю́ ма́ма и жду брат.",
                    "Я люблю́ ма́му и жду бра́та.",
                    "Я люблю́ ма́му и жду брат.",
                    "Я люблю́ ма́ма и жду бра́та."],
        "correct": "Я люблю́ ма́му и жду бра́та.",
        "explanation": "<p>Ikkita ot, ikkita boshqa qoida: <em>ма́ма</em> ayol jinsi → "
                       "<strong>ма́му</strong>; <em>брат</em> jonli erkak → "
                       "<strong>бра́та</strong>. Ikkalasi ham Вини́тельный.</p>",
    },
]


# =====================================================================
# PR-33 — Винительный 2: yoʻnalish
# =====================================================================

Q_PR33 = [
    # 1–5 tanish
    {
        "text": "<p><strong>Куда́?</strong> degan savolga qaysi kelishik javob "
                "beradi?</p>",
        "choices": ["Предло́жный", "Вини́тельный", "Роди́тельный", "Да́тельный"],
        "correct": "Вини́тельный",
        "explanation": "<p>Oʻsha PR-32 dagi kelishik, ikkinchi ishi: <strong>manzil</strong>. "
                       "<em>Я иду́ в шко́л<strong>у</strong></em>. «Где?» esa "
                       "Предло́жный: <em>в шко́л<strong>е</strong></em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ в ___.</strong> "
                "(шко́ла)</p>",
        "choices": ["шко́ла", "шко́ле", "шко́лу", "шко́лы"],
        "correct": "шко́лу",
        "explanation": "<p>Feʼl <em>иду́</em> — harakat, demak «qayerga». Ayol jinsi → "
                       "<strong>-у</strong>. <em>В шко́ле</em> «maktabdaman» degan "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>«Qayerga?» maʼnosida predlog oʻzgaradimi?</p>",
        "choices": ["Ha, В har doim НА ga aylanadi",
                    "Yoʻq — PR-30 dagi predlog oʻz kuchida qoladi",
                    "Ha, predlog umuman tushib qoladi",
                    "Faqat ayol jinsida oʻzgaradi"],
        "correct": "Yoʻq — PR-30 dagi predlog oʻz kuchida qoladi",
        "explanation": "<p><em>на рабо́т<strong>е</strong> → на рабо́т<strong>у</strong></em>, "
                       "<em>в шко́л<strong>е</strong> → в шко́л<strong>у</strong></em>. "
                       "Yangi roʻyxat yodlash kerak emas — faqat qoʻshimcha "
                       "almashadi.</p>",
    },
    {
        "text": "<p><strong>до́ма</strong> ning «qayerga?» juftligi qaysi?</p>",
        "choices": ["в дом", "домо́й", "до́му", "на дом"],
        "correct": "домо́й",
        "explanation": "<p>Ravishlar juftligi: <em>до́ма ↔ домо́й</em>, <em>здесь ↔ "
                       "сюда́</em>, <em>там ↔ туда́</em>. Ular kelishik olmaydi va "
                       "hech qachon aralashmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он идёт в ___.</strong> "
                "(магази́н)</p>",
        "choices": ["магази́н", "магази́на", "магази́ну", "магази́не"],
        "correct": "магази́н",
        "explanation": "<p><em>Магази́н</em> — jonsiz erkak, shuning uchun "
                       "Вини́тельный'da <strong>oʻzgarmaydi</strong>. Faqat predlog "
                       "qoʻshiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма е́дет ___.</strong> "
                "(рабо́та)</p>",
        "choices": ["в рабо́ту", "на рабо́ту", "на рабо́те", "в рабо́те"],
        "correct": "на рабо́ту",
        "explanation": "<p>Ikkita narsa toʻgʻri boʻlishi kerak: predlog "
                       "<strong>на</strong> (PR-30 dagi roʻyxatdan) va qoʻshimcha "
                       "<strong>-у</strong> (harakat bor).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он идёт ___.</strong> "
                "(ры́нок)</p>",
        "choices": ["на ры́нке", "на ры́нок", "в ры́нок", "на ры́нка"],
        "correct": "на ры́нок",
        "explanation": "<p><em>Ры́нок</em> НА oladi va jonsiz erkak boʻlgani uchun "
                       "<strong>oʻzgarmaydi</strong>. Solishtiring: <em>на "
                       "ры́нк<strong>е</strong></em> — qayerda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы е́дем в ___.</strong> "
                "(Москва́)</p>",
        "choices": ["Москве́", "Москву́", "Москвы́", "Москва́"],
        "correct": "Москву́",
        "explanation": "<p>Ayol jinsi → <strong>-у</strong>, va urgʻu ham oxirda: "
                       "<em>Москв<strong>у́</strong></em>. <em>В Москве́</em> "
                       "«Moskvadamiz» degan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>В суббо́ту мы е́дем в "
                "___.</strong> (дере́вня)</p>",
        "choices": ["дере́вне", "дере́вню", "дере́вни", "дере́вня"],
        "correct": "дере́вню",
        "explanation": "<p><em>-я</em> ga tugagan ayol jinsi <strong>-ю</strong> "
                       "oladi: <em>дере́вн<strong>ю</strong></em>. Xuddi <em>Ка́тя → "
                       "Ка́тю</em> kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___.</strong> "
                "(уро́к)</p>",
        "choices": ["на уро́ке", "на уро́к", "в уро́к", "на уро́ка"],
        "correct": "на уро́к",
        "explanation": "<p><em>Уро́к</em> НА oladi (PR-30 roʻyxati) va jonsiz erkak "
                       "boʻlgani uchun oʻzgarmaydi. <em>«Я иду́ на уро́ке»</em> — eng "
                       "koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>По́здно. Я иду́ "
                "___.</strong></p>",
        "choices": ["до́ма", "домо́й", "в до́ме", "на дом"],
        "correct": "домо́й",
        "explanation": "<p>Feʼl <em>иду́</em> — harakat, demak «qayerga» kerak. "
                       "<em>До́ма</em> esa «qayerda»: <em>Я до́ма</em> — "
                       "uydaman.</p>",
    },
    {
        "text": "<p>Bu ibora qaysi kelishikda?</p><p><strong>в суббо́ту</strong></p>",
        "choices": ["Предло́жный", "Вини́тельный", "Роди́тельный", "Да́тельный"],
        "correct": "Вини́тельный",
        "explanation": "<p>Xuddi shu qurilish <strong>vaqt</strong> uchun ham "
                       "ishlatiladi: <em>суббо́та → в суббо́т<strong>у</strong></em>. "
                       "<em>Понеде́льник</em> jonsiz erkak boʻlgani uchun oʻzgarmaydi: "
                       "<em>в понеде́льник</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapni ajrating.</p><p><strong>Я в Москве́. · Я е́ду в "
                "Москву́.</strong></p>",
        "choices": ["Moskvadaman · Moskvaga ketyapman",
                    "Moskvaga ketyapman · Moskvadaman",
                    "Ikkalasi bir xil",
                    "Ikkinchisi xato"],
        "correct": "Moskvadaman · Moskvaga ketyapman",
        "explanation": "<p>Predlog bir xil, feʼl boshqa — va butun maʼnoni oxirgi "
                       "harf hal qiladi: <strong>-е</strong> = joy, <strong>-у</strong> "
                       "= manzil.</p>",
    },
    {
        "text": "<p>Qaysi feʼl «qayerga?» ni talab qiladi?</p>",
        "choices": ["жить", "рабо́тать", "е́хать", "учи́ться"],
        "correct": "е́хать",
        "explanation": "<p><em>Е́хать, идти́, ходи́ть</em> — harakat feʼllari, ular "
                       "manzil oladi. <em>Жить, рабо́тать, учи́ться, быть</em> — joy "
                       "feʼllari, ular Предло́жный oladi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida bu farq qayerda koʻrsatiladi?</p>",
        "choices": ["Feʼlda", "Otning oxirida: -DA va -GA",
                    "Soʻz tartibida", "Hech qayerda"],
        "correct": "Otning oxirida: -DA va -GA",
        "explanation": "<p><em>maktab<strong>da</strong></em> ↔ "
                       "<em>maktab<strong>ga</strong></em> — xuddi ruschadagi "
                       "<em>-Е</em> ↔ <em>-У</em> kabi. Ikkala tilda ham qoʻshimcha "
                       "ishlaydi; ruschadagi predlog esa qoʻshimcha shovqin.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi «qayerga?» maʼnosida?</p>",
        "choices": ["в шко́лу · на рабо́ту · домо́й",
                    "в шко́ле · на рабо́ту · домо́й",
                    "в шко́лу · на рабо́те · до́ма",
                    "в шко́ле · на рабо́те · до́ма"],
        "correct": "в шко́лу · на рабо́ту · домо́й",
        "explanation": "<p>Uchalasi ham manzil: ikkita ot Вини́тельный'da "
                       "(<em>-у</em>) va bitta ravish (<em>домо́й</em>). Oxirgi "
                       "variant esa butunlay «qayerda».</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он рабо́тает в магази́не.", "В суббо́ту мы е́дем в дере́вню.",
                    "Я иду́ на уро́ке.", "Ба́бушка живёт в дере́вне."],
        "correct": "Я иду́ на уро́ке.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я иду́ на уро́к</strong>. Feʼl "
                       "<em>иду́</em> harakatni bildiradi, demak manzil kerak; "
                       "<em>уро́к</em> jonsiz erkak, shuning uchun shakl "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я иду́ до́ма.", "Я иду́ в до́ме.",
                    "Я иду́ домо́й.", "Я иду́ на дом."],
        "correct": "Я иду́ домо́й.",
        "explanation": "<p><strong>Домо́й</strong> — «uyga». <em>До́ма</em> «uyda» "
                       "degani va harakat feʼli bilan kelmaydi. Ikkalasi ham ravish, "
                       "shuning uchun predlog ham kerak emas.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Куда́ ты идёшь?</strong></p>",
        "choices": ["— В библиоте́ку.", "— В библиоте́ке.",
                    "— В библиоте́ки.", "— О библиоте́ке."],
        "correct": "— В библиоте́ку.",
        "explanation": "<p>Savol <em>куда́?</em> — manzil, demak Вини́тельный. Ayol "
                       "jinsi → <strong>-у</strong>. Agar savol <em>где?</em> "
                       "boʻlganda javob <em>в библиоте́ке</em> boʻlardi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ertalab maktabga "
                "boraman, kechqurun esa doʻkonda ishlayman.</strong></p>",
        "choices": ["У́тром я иду́ в шко́ле, а ве́чером рабо́таю в магази́н.",
                    "У́тром я иду́ в шко́лу, а ве́чером рабо́таю в магази́не.",
                    "У́тром я иду́ в шко́лу, а ве́чером рабо́таю в магази́н.",
                    "У́тром я иду́ в шко́ле, а ве́чером рабо́таю в магази́не."],
        "correct": "У́тром я иду́ в шко́лу, а ве́чером рабо́таю в магази́не.",
        "explanation": "<p>Bitta gapda ikkala kelishik ham bor. Feʼllarga qarang: "
                       "<em>иду́</em> — harakat, demak <strong>в шко́лу</strong>; "
                       "<em>рабо́таю</em> — harakat emas, demak <strong>в "
                       "магази́не</strong>.</p>",
    },
]


# =====================================================================
# PR-34 — Родительный 1: egalik va yoʻqlik
# =====================================================================

Q_PR34 = [
    # 1–5 tanish
    {
        "text": "<p>Роди́тельный padeji oʻzbekchadagi qaysi qoʻshimchaga toʻgʻri "
                "keladi?</p>",
        "choices": ["-ni", "-ga", "-da", "-ning"],
        "correct": "-ning",
        "explanation": "<p><em>aka<strong>ning</strong> kitobi</em> → <em>кни́га "
                       "бра́т<strong>а</strong></em>. Savoli: <em>кого́? чего́?</em> — "
                       "qaratqich kelishigi.</p>",
    },
    {
        "text": "<p>Erkak va oʻrta jinsdagi otlar Роди́тельный'da qaysi qoʻshimchani "
                "oladi?</p>",
        "choices": ["-ы / -и", "-а / -я", "-у / -ю", "-е"],
        "correct": "-а / -я",
        "explanation": "<p><em>брат → бра́та</em>, <em>окно́ → окна́</em>, "
                       "<em>учи́тель → учи́теля</em>. Erkak va oʻrta jins bu yerda "
                       "ham bir xil — amalda ikkita naqsh bor.</p>",
    },
    {
        "text": "<p>Bu iborani ruschaga oʻgiring.</p><p><strong>Akaning "
                "kitobi</strong></p>",
        "choices": ["Бра́та кни́га", "Кни́га бра́та", "Кни́га брат", "Бра́т кни́ги"],
        "correct": "Кни́га бра́та",
        "explanation": "<p>Egasi <strong>har doim orqada</strong> — bu oʻzbekchaning "
                       "teskarisi. Va faqat egasi kelishikka kiradi: <em>кни́га</em> "
                       "bosh kelishikda qoladi.</p>",
    },
    {
        "text": "<p><strong>нет</strong> dan keyin ot qaysi kelishikda boʻladi?</p>",
        "choices": ["Bosh kelishikda", "Вини́тельный", "Роди́тельный", "Предло́жный"],
        "correct": "Роди́тельный",
        "explanation": "<p><em>есть кни́г<strong>а</strong></em> → <em>нет "
                       "кни́г<strong>и</strong></em>. Bu qoida qatʼiy. Oʻzbekchada esa "
                       "ot oʻzgarmaydi («kitob bor / kitob yoʻq») — shuning uchun uni "
                       "alohida yodlash kerak.</p>",
    },
    {
        "text": "<p><strong>вре́мя</strong> soʻzining Роди́тельный shakli qaysi?</p>",
        "choices": ["вре́ма", "вре́мя", "вре́мени", "вре́мы"],
        "correct": "вре́мени",
        "explanation": "<p><em>Вре́мя</em> — <strong>-мя</strong> ga tugaydigan kichik "
                       "guruhdan (<em>вре́мя, и́мя, зна́мя</em>). <em>Нет "
                       "вре́мени</em> — rus tilida eng koʻp aytiladigan iboralardan "
                       "biri.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У меня́ нет ___.</strong> "
                "(маши́на)</p>",
        "choices": ["маши́на", "маши́ны", "маши́ну", "маши́не"],
        "correct": "маши́ны",
        "explanation": "<p>Ayol jinsi <strong>-ы</strong> oladi (Н dan keyin oddiy Ы). "
                       "Solishtiring: <em>У меня́ есть маши́на</em> — bosh "
                       "kelishikda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь нет ___.</strong> "
                "(магази́н)</p>",
        "choices": ["магази́н", "магази́на", "магази́ну", "магази́не"],
        "correct": "магази́на",
        "explanation": "<p>Erkak jins → <strong>-а</strong>. «Нет» dan keyin jonlilik "
                       "ahamiyatsiz: jonli ham, jonsiz ham Роди́тельный'ga "
                       "kiradi.</p>",
    },
    {
        "text": "<p><strong>-ы</strong> yoki <strong>-и</strong>?</p><p><strong>кни́га "
                "→ нет ___</strong></p>",
        "choices": ["кни́гы", "кни́ги", "кни́гу", "кни́ге"],
        "correct": "кни́ги",
        "explanation": "<p>Oʻzak <strong>К</strong> ga tugaydi, К dan keyin esa Ы "
                       "yozilmaydi — demak <strong>-и</strong>. Bu PR-4 dagi imlo "
                       "qoidasi: Г, К, Х, Ж, Ш, Щ, Ч dan keyin И.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то дом ___.</strong> "
                "(оте́ц)</p>",
        "choices": ["оте́ц", "отца́", "отцу́", "отце́"],
        "correct": "отца́",
        "explanation": "<p>Erkak jins → <strong>-а</strong>, va <strong>Е tushib "
                       "qoladi</strong>: <em>оте́ц → отца́</em>. Bu shakl "
                       "Вини́тельный'da ham xuddi shunday (PR-32).</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Сего́дня нет "
                "дождя́.</strong></p>",
        "choices": ["Вчера́ не́ был дождь.", "Вчера́ не́ было дождя́.",
                    "Вчера́ не́ была́ дождя́.", "Вчера́ нет был дождя́."],
        "correct": "Вчера́ не́ было дождя́.",
        "explanation": "<p>Shaxssiz gap, shuning uchun <em>быть</em> har doim oʻrta "
                       "jinsda — <strong>не́ было</strong>, hatto <em>дождь</em> erkak "
                       "jinsida boʻlsa ham. Ot esa Роди́тельный'da qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Окно́ ___ смо́трит на "
                "восто́к.</strong> (ку́хня)</p>",
        "choices": ["ку́хня", "ку́хню", "ку́хни", "ку́хне"],
        "correct": "ку́хни",
        "explanation": "<p><em>-я</em> ga tugagan ayol jinsi <strong>-и</strong> "
                       "oladi: <em>ку́хн<strong>и</strong></em>. Va egasi orqada "
                       "turibdi — <em>окно́</em> bosh kelishikda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то кни́га ___.</strong> "
                "(Афсо́на)</p>",
        "choices": ["Афсо́на", "Афсо́ну", "Афсо́ны", "Афсо́не"],
        "correct": "Афсо́ны",
        "explanation": "<p>Ayol jinsi <strong>-ы</strong> oladi (Н dan keyin). Ismlar "
                       "ham oddiy otlar kabi turlanadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Oʻzbekcha va ruscha egalikning ikkita farqi nima?</p>",
        "choices": ["Ruschada egasi orqada va faqat bitta soʻz belgilanadi",
                    "Ruschada egasi oldinda va ikkala soʻz belgilanadi",
                    "Ruschada egalik umuman belgilanmaydi",
                    "Farq yoʻq"],
        "correct": "Ruschada egasi orqada va faqat bitta soʻz belgilanadi",
        "explanation": "<p>Oʻzbekcha: <em>aka-NING kitob-I</em> — egasi oldinda, "
                       "ikkala soʻz belgilangan. Ruscha: <em>кни́га бра́т-А</em> — "
                       "egasi orqada, faqat u belgilangan. Shuning uchun oʻzbek "
                       "oʻquvchi <em>«бра́та кни́га»</em> deb yozib yuboradi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>У меня́ есть кни́га. · "
                "У меня́ нет кни́ги.</strong></p>",
        "choices": ["Bor · yoʻq — va ikkinchisida ot Роди́тельный'ga kiradi",
                    "Ikkalasi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi koʻplik"],
        "correct": "Bor · yoʻq — va ikkinchisida ot Роди́тельный'ga kiradi",
        "explanation": "<p>Oʻzbekchada ot ikkala gapda ham bir xil qoladi. Ruschada "
                       "esa <em>есть кни́га</em> (bosh kelishik) va <em>нет кни́ги</em> "
                       "(Роди́тельный). Bu qoidani <em>нет</em> bilan bitta boʻlak "
                       "qilib yodlash osonroq.</p>",
    },
    {
        "text": "<p>Nega jonli erkak otlarning Вини́тельный va Роди́тельный shakllari "
                "bir xil?</p>",
        "choices": ["Bu tasodif", "Ikkalasi ham -А / -Я oladi",
                    "Bu xato", "Faqat ismlarda shunday"],
        "correct": "Ikkalasi ham -А / -Я oladi",
        "explanation": "<p><em>Я ви́жу бра́та</em> (В.п.) va <em>кни́га бра́та</em> "
                       "(Р.п.) — shakl bir xil. PR-32 da aytilgan edi: jonli erkak "
                       "Вини́тельный'da <strong>Роди́тельный shaklini</strong> oladi. "
                       "Bu ikkita kelishikni bir shaklda yodlash imkonini "
                       "beradi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["нет кни́ги · нет вре́мени · нет воды́",
                    "нет кни́га · нет вре́мени · нет воды́",
                    "нет кни́ги · нет вре́мя · нет вода́",
                    "нет кни́гы · нет вре́мени · нет воды́"],
        "correct": "нет кни́ги · нет вре́мени · нет воды́",
        "explanation": "<p>Uchta boshqa qoida: <em>кни́ги</em> (К dan keyin И), "
                       "<em>вре́мени</em> (-мя guruhi), <em>воды́</em> (oddiy -ы, urgʻu "
                       "oxirida).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́то дом отца́.", "У нас нет вре́мени.",
                    "Бра́та маши́на но́вая.", "Здесь нет магази́на."],
        "correct": "Бра́та маши́на но́вая.",
        "explanation": "<p>Toʻgʻrisi — <strong>Маши́на бра́та но́вая</strong>. Egalik "
                       "bildiruvchi soʻz har doim orqada turadi. Oʻzbekcha tartibni "
                       "ruschaga koʻchirish — bu darsdagi eng koʻp uchraydigan "
                       "xato.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["У меня́ нет вре́мя.", "У меня́ нет вре́мени.",
                    "У меня́ не́ту вре́мя.", "У меня́ нет вре́ма."],
        "correct": "У меня́ нет вре́мени.",
        "explanation": "<p><em>Вре́мя</em> <strong>-мя</strong> guruhidan va "
                       "Роди́тельный'da <strong>вре́мени</strong> boʻladi. Bu iborani "
                       "butunligicha yodlang — u juda koʻp kerak boʻladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— У тебя́ есть маши́на?</strong></p>",
        "choices": ["— Нет, у меня́ нет маши́ны.", "— Нет, у меня́ нет маши́на.",
                    "— Нет, у меня́ нет маши́ну.", "— Нет, у меня́ не маши́на."],
        "correct": "— Нет, у меня́ нет маши́ны.",
        "explanation": "<p>Savol bosh kelishikda (<em>есть маши́на</em>), javob esa "
                       "Роди́тельный'da (<em>нет маши́ны</em>). Aynan shu almashinuv "
                       "bu darsning yuragi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bu bobomning uyi. "
                "U yerda internet yoʻq.</strong></p>",
        "choices": ["Э́то де́да дом. Там нет интерне́т.",
                    "Э́то дом де́да. Там нет интерне́та.",
                    "Э́то дом дед. Там нет интерне́та.",
                    "Э́то де́да дом. Там нет интерне́та."],
        "correct": "Э́то дом де́да. Там нет интерне́та.",
        "explanation": "<p>Ikkita qoida bir gapda: egasi <strong>orqada</strong> va "
                       "kelishikda (<em>дом де́да</em>), va «нет» dan keyin "
                       "Роди́тельный (<em>нет интерне́та</em>).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-32 Mashq: Винительный 1: кого? что? — jonli va jonsiz farqi",
        "description": (
            "Toʻldiruvchi kelishigi: ayol jinsi -У, oʻrta jins oʻzgarmaydi, erkak "
            "jinsi esa jonlilikka qaraydi. Olmoshlar: меня́, тебя́, его́, её."
        ),
        "tutorial": "PR-32:",
        "questions": Q_PR32,
    },
    {
        "title": "PR-33 Mashq: Винительный 2: yoʻnalish — в школу, на работу, куда?",
        "description": (
            "«Где?» va «куда́?» qarama-qarshiligi, predlogning oʻzgarmasligi, "
            "jonsiz erkak otlarning oʻzgarmasligi va до́ма ↔ домо́й juftligi."
        ),
        "tutorial": "PR-33:",
        "questions": Q_PR33,
    },
    {
        "title": "PR-34 Mashq: Родительный 1: egalik va yoʻqlik — книга брата, нет времени",
        "description": (
            "Qoʻshimchalar -а/-я va -ы/-и, egalikdagi teskari soʻz tartibi, "
            "«нет» dan keyingi Роди́тельный va uchala zamon."
        ),
        "tutorial": "PR-34:",
        "questions": Q_PR34,
    },
]
