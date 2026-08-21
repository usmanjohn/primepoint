# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-24 … PR-26.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_24_26.py --master=prime \\
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
# PR-24 — Kelasi zamon: буду + infinitiv
# =====================================================================

Q_PR24 = [
    # 1–5 tanish
    {
        "text": "<p>Rus tilida kelasi zamon qanday yasaladi?</p>",
        "choices": ["Feʼlga -бу qoʻshiladi", "бу́ду + infinitiv",
                    "бу́ду + oʻtgan zamon", "Hozirgi zamon shakli ishlatiladi"],
        "correct": "бу́ду + infinitiv",
        "explanation": "<p>Ikki soʻz, bitta zamon: tuslanadigan yordamchi feʼl "
                       "<strong>бу́ду</strong> va oʻzgarmagan <strong>infinitiv</strong>. "
                       "Faqat birinchi soʻz egaga moslashadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ чита́ть.</strong></p>",
        "choices": ["бу́ду", "бу́дет", "бу́дем", "бу́дут"],
        "correct": "бу́дем",
        "explanation": "<p>«Мы» uchun <strong>бу́дем</strong>. Yordamchi feʼl aynan "
                       "<em>идти́</em> naqshi boʻyicha tuslanadi: <em>бу́ду, бу́дешь, "
                       "бу́дет, бу́дем, бу́дете, бу́дут</em> — faqat urgʻu oʻzakda, "
                       "shuning uchun Ё emas, Е.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я бу́ду ___ ру́сский "
                "язы́к.</strong> (учи́ть)</p>",
        "choices": ["учу́", "у́чит", "учи́ть", "учи́л"],
        "correct": "учи́ть",
        "explanation": "<p>Ikkinchi feʼl <strong>hech qachon</strong> tuslanmaydi — u "
                       "infinitivda qoladi. Bu PR-19 dagi qoidaning oʻsha oʻzi: gapda "
                       "faqat birinchi feʼl shaxsga moslashadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>За́втра ___ дождь.</strong></p>",
        "choices": ["бу́дет", "бу́дут", "бу́ду", "был"],
        "correct": "бу́дет",
        "explanation": "<p><em>Дождь</em> — uchinchi shaxs birligi, demak "
                       "<strong>бу́дет</strong>. Bu yerda infinitiv kerak emas: "
                       "<em>бу́дет</em> ning oʻzi «boʻladi» degani. Solishtiring: "
                       "<em>Вчера́ был дождь. Сего́дня дождь. За́втра бу́дет дождь.</em></p>",
    },
    {
        "text": "<p>Kelasi zamonni inkor qilish uchun НЕ qayerga qoʻyiladi?</p>",
        "choices": ["Infinitivning oldiga", "бу́ду ning oldiga",
                    "Gap oxiriga", "Ikkalasining ham oldiga"],
        "correct": "бу́ду ning oldiga",
        "explanation": "<p>Inkor har doim <strong>tuslanadigan</strong> feʼlga tegadi: "
                       "<em>Я <strong>не бу́ду</strong> рабо́тать</em>. "
                       "<em>«Я бу́ду не рабо́тать»</em> — xato.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ жить в "
                "Москве́.</strong></p>",
        "choices": ["бу́дут", "бу́дет", "бу́дете", "бу́дем"],
        "correct": "бу́дут",
        "explanation": "<p>«Они́» uchun <strong>бу́дут</strong> — <em>-ут</em>, xuddi "
                       "<em>иду́т</em> kabi. Infinitiv <em>жить</em> oʻz holida "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Bu gapni kelasi zamonga oʻtkazing.</p><p><strong>Вчера́ я был "
                "до́ма.</strong></p>",
        "choices": ["За́втра я бу́ду до́ма.", "За́втра я бу́ду быть до́ма.",
                    "За́втра я до́ма.", "За́втра я бу́дет до́ма."],
        "correct": "За́втра я бу́ду до́ма.",
        "explanation": "<p><em>Бу́ду</em> ning oʻzi allaqachon «boʻlaman» degani, "
                       "shuning uchun yoniga yana <em>быть</em> qoʻshilmaydi. Va "
                       "hozirgi zamon (<em>я до́ма</em>) kelasi zamon oʻrniga "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ___ спеши́ть?</strong> "
                "(inkor shakli)</p>",
        "choices": ["бу́дешь не", "не бу́дешь", "не бу́дет", "бу́дет не"],
        "correct": "не бу́дешь",
        "explanation": "<p><strong>Не бу́дешь</strong> — НЕ yordamchi feʼlning oldida, "
                       "«ты» uchun esa <em>бу́дешь</em>. Oʻzbek oʻquvchi koʻpincha "
                       "inkorni infinitivga yopishtiradi, chunki oʻzbekchada inkor "
                       "feʼlning ichida boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ле́том мы ___ в "
                "Самарка́нде.</strong></p>",
        "choices": ["бу́дем", "бу́дем быть", "бу́дут", "бы́ли"],
        "correct": "бу́дем",
        "explanation": "<p>Yolgʻiz <strong>бу́дем</strong> — «boʻlamiz». <em>Ле́том</em> "
                       "(yozda) kelasi zamonni koʻrsatib turibdi. Bu qurilish juda koʻp "
                       "ishlatiladi: <em>Я бу́ду до́ма. Он бу́дет здесь.</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вы ___ есть пло́в?</strong></p>",
        "choices": ["бу́дут", "бу́дете", "бу́дем", "бу́дешь"],
        "correct": "бу́дете",
        "explanation": "<p>«Вы» uchun <strong>бу́дете</strong>. Kundalik nutqda bu savol "
                       "«olasizmi, yeysizmi?» degan taklif boʻlib ishlatiladi, va qisqa "
                       "javob ham shu shaklda beriladi: <em>Да, бу́ду</em>.</p>",
    },
    {
        "text": "<p>Bu gapni kelasi zamonga oʻtkazing.</p><p><strong>Он говори́т "
                "по-ру́сски.</strong></p>",
        "choices": ["Он бу́дет говори́ть по-ру́сски.", "Он бу́дет говори́т по-ру́сски.",
                    "Он бу́дут говори́ть по-ру́сски.", "Он говори́л по-ру́сски."],
        "correct": "Он бу́дет говори́ть по-ру́сски.",
        "explanation": "<p>Tuslangan feʼl <em>говори́т</em> infinitivga qaytadi "
                       "(<em>говори́ть</em>), va uning oldiga egaga mos yordamchi feʼl "
                       "qoʻyiladi (<em>бу́дет</em>).</p>",
    },
    {
        "text": "<p>Qaysi qatorda uchala zamon toʻgʻri berilgan?</p><p><strong>чита́ть, "
                "он</strong></p>",
        "choices": ["чита́л · чита́ет · бу́дет чита́ть",
                    "чита́л · чита́ет · бу́дет чита́ет",
                    "чита́ла · чита́ет · бу́ду чита́ть",
                    "чита́ет · чита́л · бу́дет чита́ть"],
        "correct": "чита́л · чита́ет · бу́дет чита́ть",
        "explanation": "<p>Kecha — <strong>чита́л</strong> (jinsga qarab, PR-23). Bugun "
                       "— <strong>чита́ет</strong> (shaxsga qarab, PR-20). Ertaga — "
                       "<strong>бу́дет чита́ть</strong> (yordamchi shaxsga qarab, "
                       "infinitiv oʻzgarmaydi).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi gapda kelasi zamon kerak?</p>",
        "choices": ["Сейча́с я чита́ю.", "Вчера́ я чита́л.",
                    "За́втра я чита́ю кни́гу.", "Ка́ждый день я чита́ю."],
        "correct": "За́втра я чита́ю кни́гу.",
        "explanation": "<p>Toʻgʻrisi — <strong>За́втра я бу́ду чита́ть кни́гу</strong>. "
                       "Oʻzbekchada «oʻqiyman» ham hozir, ham ertaga uchun ishlaydi; "
                       "ruschada esa <em>чита́ю</em> faqat <strong>hozir</strong>ni "
                       "bildiradi. Ertaga uchun <em>бу́ду</em> ni aytish shart.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я бу́ду до́ма. · "
                "Я бу́ду чита́ть.</strong></p>",
        "choices": ["Birinchisida infinitiv yoʻq — «boʻlaman» degani",
                    "Birinchisi oʻtgan zamon", "Ikkinchisi xato",
                    "Hech qanday farq yoʻq"],
        "correct": "Birinchisida infinitiv yoʻq — «boʻlaman» degani",
        "explanation": "<p>Gapda boshqa feʼl boʻlsa, <em>бу́ду</em> yordamchi boʻladi "
                       "(<em>бу́ду чита́ть</em>). Boshqa feʼl boʻlmasa, u kesimning "
                       "oʻzi boʻladi (<em>бу́ду до́ма</em> = «uyda boʻlaman»).</p>",
    },
    {
        "text": "<p><strong>бу́ду</strong> feʼlining tuslanishi qaysi tanish feʼlga "
                "oʻxshaydi?</p>",
        "choices": ["чита́ть", "говори́ть", "идти́", "есть"],
        "correct": "идти́",
        "explanation": "<p><em>Иду́, идёшь, идёт, идём, идёте, иду́т</em> — <em>бу́ду, "
                       "бу́дешь, бу́дет, бу́дем, бу́дете, бу́дут</em>. Bitta farq: "
                       "<em>идти́</em> da urgʻu qoʻshimchada (shuning uchun <strong>Ё</strong>), "
                       "<em>быть</em> da esa oʻzakda (shuning uchun <strong>Е</strong>).</p>",
    },
    {
        "text": "<p>Hozirgi zamonda «быть» feʼli nima boʻladi?</p>",
        "choices": ["есть shaklida keladi", "бу́ду shaklida keladi",
                    "Umuman aytilmaydi", "был shaklida keladi"],
        "correct": "Umuman aytilmaydi",
        "explanation": "<p>Rus tilining mashhur «teshigi»: <em>Я студе́нт. Он до́ма.</em> "
                       "— feʼlsiz (PR-11). Lekin oʻtgan zamonda u qaytadi "
                       "(<em>был</em>, PR-23) va kelasi zamonda ham (<em>бу́дет</em>). "
                       "Faqat hozirgi zamon boʻsh qoladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мы бу́дем гуля́ть ве́чером.", "Ты бу́дешь до́ма?",
                    "Они́ бу́дут рабо́тать.", "Я бу́ду чита́ю кни́гу."],
        "correct": "Я бу́ду чита́ю кни́гу.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я бу́ду чита́ть кни́гу</strong>. Ikkinchi "
                       "feʼl infinitivda boʻlishi kerak. Bir gapda ikkita tuslangan "
                       "feʼl turolmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["За́втра бу́дет тру́дно.", "За́втра бу́дут тру́дно.",
                    "За́втра бу́ду тру́дно.", "За́втра бу́дет быть тру́дно."],
        "correct": "За́втра бу́дет тру́дно.",
        "explanation": "<p><em>Э́то бу́дет тру́дно</em>, <em>за́втра бу́дет тру́дно</em> "
                       "— shaxssiz qurilish, har doim uchinchi shaxs birligida: "
                       "<strong>бу́дет</strong>. Oʻtgan zamonda ham shunday: "
                       "<em>бы́ло тру́дно</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты бу́дешь чай?</strong></p>",
        "choices": ["— Да, бу́ду. Спаси́бо.", "— Да, бу́дешь.",
                    "— Да, был.", "— Да, бу́ду быть."],
        "correct": "— Да, бу́ду. Спаси́бо.",
        "explanation": "<p>Qisqa javobda infinitiv tushib qoladi, chunki u tushunarli. "
                       "Javob «я» dan keladi, demak <strong>бу́ду</strong>. Bu — rus "
                       "tilida choy taklif qilishning eng oddiy yoʻli.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ertaga ishlamayman — "
                "uyda boʻlaman.</strong></p>",
        "choices": ["За́втра я не рабо́таю — я до́ма.",
                    "За́втра я бу́ду не рабо́тать — я бу́ду до́ма.",
                    "За́втра я не бу́ду рабо́тать — я бу́ду до́ма.",
                    "За́втра я не бу́ду рабо́тать — я бу́ду быть до́ма."],
        "correct": "За́втра я не бу́ду рабо́тать — я бу́ду до́ма.",
        "explanation": "<p>Uchta narsa toʻgʻri boʻlishi kerak: <strong>не</strong> "
                       "yordamchi feʼl oldida, ikkinchi feʼl <strong>infinitiv</strong>da, "
                       "va ikkinchi qismda <em>быть</em> qoʻshilmaydi — "
                       "<strong>бу́ду до́ма</strong> yetarli.</p>",
    },
]


# =====================================================================
# PR-25 — Qaytim feʼllar -ся / -сь
# =====================================================================

Q_PR25 = [
    # 1–5 tanish
    {
        "text": "<p>Qaytim qoʻshimchasi feʼlning qayerida turadi?</p>",
        "choices": ["Oʻzakdan oldin", "Oʻzak va qoʻshimcha oʻrtasida",
                    "Eng oxirida, shaxs qoʻshimchasidan ham keyin", "Gap oxirida, alohida soʻz sifatida"],
        "correct": "Eng oxirida, shaxs qoʻshimchasidan ham keyin",
        "explanation": "<p><em>Уч + у́ + сь</em> — avval oʻzak, keyin shaxs qoʻshimchasi, "
                       "eng oxirida <strong>-ся/-сь</strong>. Oʻzbekchada esa u oʻrtada "
                       "boʻladi: <em>yuv-<strong>in</strong>-a-man</em>.</p>",
    },
    {
        "text": "<p>Qachon <strong>-сь</strong>, qachon <strong>-ся</strong> "
                "yoziladi?</p>",
        "choices": ["Unlidan keyin -сь, undoshdan keyin -ся",
                    "Undoshdan keyin -сь, unlidan keyin -ся",
                    "Har doim -ся", "Birlikda -сь, koʻplikda -ся"],
        "correct": "Unlidan keyin -сь, undoshdan keyin -ся",
        "explanation": "<p><em>Учу́</em> unli bilan tugaydi → <strong>учу́сь</strong>. "
                       "<em>У́чит</em> undosh bilan → <strong>у́чится</strong>. Bu "
                       "talaffuz uchun qilingan qoida. Yodlash uchun: <strong>-сь</strong> "
                       "faqat «я» va «вы» shakllarida.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ в шко́ле.</strong> "
                "(учи́ться)</p>",
        "choices": ["учу́ся", "учу́сь", "у́чится", "учи́сь"],
        "correct": "учу́сь",
        "explanation": "<p><em>Учу́</em> unli <strong>У</strong> bilan tugaydi, demak "
                       "<strong>-сь</strong>: <em>учу́сь</em>. <em>Учу́ся</em> — eng "
                       "koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p><strong>у́чится</strong> qanday oʻqiladi?</p>",
        "choices": ["[у́читса]", "[у́чится]", "[у́чица]", "[учи́ца]"],
        "correct": "[у́чица]",
        "explanation": "<p><strong>-тся</strong> va <strong>-ться</strong> har doim "
                       "<strong>[ца]</strong> boʻlib oʻqiladi. Shuning uchun "
                       "<em>у́чится</em> va <em>учи́ться</em> deyarli bir xil "
                       "eshitiladi — farqni faqat gapdan bilib olasiz.</p>",
    },
    {
        "text": "<p>Bu feʼllarning qaysi biri <strong>-ся</strong> siz umuman "
                "mavjud emas?</p>",
        "choices": ["учи́ться", "встреча́ться", "одева́ться", "смея́ться"],
        "correct": "смея́ться",
        "explanation": "<p><em>Смея́ться</em> — uchinchi guruhdan: <em>«он смеёт»</em> "
                       "degan shakl yoʻq. Xuddi shunday <em>боя́ться, стара́ться, "
                       "находи́ться</em>. Qolgan uchtasining <em>-ся</em> siz varianti "
                       "bor: <em>учи́ть, встреча́ть, надева́ть</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вы ___ в "
                "университе́те?</strong> (учи́ться)</p>",
        "choices": ["у́читеся", "у́читесь", "у́чится", "у́чатся"],
        "correct": "у́читесь",
        "explanation": "<p><em>У́чите</em> unli <strong>Е</strong> bilan tugaydi, demak "
                       "<strong>-сь</strong>. «Вы» — <em>-сь</em> oladigan ikkita "
                       "shakldan biri; ikkinchisi «я».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Они́ ___ ка́ждую "
                "суббо́ту.</strong> (встреча́ться)</p>",
        "choices": ["встреча́ются", "встреча́ють", "встреча́ютсь", "встреча́ет"],
        "correct": "встреча́ются",
        "explanation": "<p><em>Встреча́ют</em> undosh <strong>Т</strong> bilan tugaydi, "
                       "demak <strong>-ся</strong>. <em>Встреча́ться</em> ikkinchi "
                       "guruhdan: harakat <strong>bir-biriga</strong> qaratilgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дилно́за ___ "
                "пла́вать.</strong> (учи́ться, oʻtgan zamon)</p>",
        "choices": ["учи́лся", "учи́лась", "учи́лись", "учи́лся́"],
        "correct": "учи́лась",
        "explanation": "<p>Ikki qadam: avval oʻtgan zamon va jins — <em>учи́ла-</em> "
                       "(Dilnoza qiz, PR-23); keyin qoʻshimcha — oxirida unli "
                       "<strong>А</strong>, demak <strong>-сь</strong>. Natija: "
                       "<strong>учи́лась</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Жасу́р ___ воды́.</strong> "
                "(боя́ться, oʻtgan zamon)</p>",
        "choices": ["боя́лась", "боя́лись", "боя́лся", "бо́ялся"],
        "correct": "боя́лся",
        "explanation": "<p>Jasur — yigit, demak <em>боя́л-</em>; oxirida undosh "
                       "<strong>Л</strong>, demak <strong>-ся</strong>. Erkak shaklida "
                       "har doim <em>-ся</em> boʻladi, chunki <em>-л</em> undosh.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Где ___ шко́ла?</strong> "
                "(находи́ться)</p>",
        "choices": ["нахо́дится", "нахо́дятся", "нахожу́сь", "нахо́дит"],
        "correct": "нахо́дится",
        "explanation": "<p><em>Шко́ла</em> — birlik, demak <strong>нахо́дится</strong>. "
                       "Bu savol rus tilida joyni soʻrashning eng koʻp ishlatiladigan "
                       "yoʻli: <em>Где нахо́дится…?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ ру́сским "
                "языко́м.</strong> (занима́ться)</p>",
        "choices": ["занима́емся", "занима́емсь", "занима́ются", "занима́ем"],
        "correct": "занима́емся",
        "explanation": "<p><em>Занима́ем</em> undosh <strong>М</strong> bilan tugaydi, "
                       "demak <strong>-ся</strong>. <em>Занима́ться</em> — «shugʻullanmoq», "
                       "sport va til oʻrganish haqida juda koʻp ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Уро́к ___ в во́семь "
                "часо́в.</strong> (начина́ться)</p>",
        "choices": ["начина́ет", "начина́ются", "начина́ется", "начина́ю"],
        "correct": "начина́ется",
        "explanation": "<p><em>Уро́к</em> — birlik, demak <strong>начина́ется</strong> "
                       "(«boshlanadi»). <em>-Ся</em> siz shakli boshqa maʼno berardi: "
                       "<em>начина́ет</em> — «boshlaydi», yaʼni kimdir nimanidir "
                       "boshlaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>учи́ть</strong> yoki <strong>учи́ться</strong>?</p>"
                "<p><strong>Я ___ но́вые слова́ ка́ждый день.</strong></p>",
        "choices": ["учу́", "учу́сь", "у́чится", "учи́ться"],
        "correct": "учу́",
        "explanation": "<p>Gapda «nimani?» degan savolga javob bor — <em>но́вые слова́</em>. "
                       "<strong>Учи́ть</strong> yoniga narsa oladi. <strong>Учи́ться</strong> "
                       "esa olmaydi — u «talaba boʻlmoq» degani.</p>",
    },
    {
        "text": "<p><strong>учи́ть</strong> yoki <strong>учи́ться</strong>?</p>"
                "<p><strong>Афсо́на ___ в шко́ле №5.</strong></p>",
        "choices": ["у́чит", "учи́ла", "у́чится", "учи́ть"],
        "correct": "у́чится",
        "explanation": "<p>Gapda «nimani?» yoʻq — faqat joy bor. Demak "
                       "<strong>у́чится</strong>. <em>«Афсо́на у́чит в шко́ле»</em> "
                       "degan gap javobsiz savol qoldiradi: maktabda <strong>nimani</strong> "
                       "yodlayapti?</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Мы встреча́ем Ни́ну. · "
                "Мы встреча́емся.</strong></p>",
        "choices": ["Ninani kutib olamiz · bir-birimiz bilan uchrashamiz",
                    "Ikkalasi bir xil", "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Ninani kutib olamiz · bir-birimiz bilan uchrashamiz",
        "explanation": "<p><strong>-Ся</strong> ning ikkinchi guruhi: harakat "
                       "<strong>bir-biriga</strong> qaratiladi. <em>Встреча́ть</em> "
                       "yoniga kimni kutib olayotganingiz yoziladi; "
                       "<em>встреча́ться</em> esa oʻzi yetarli.</p>",
    },
    {
        "text": "<p><strong>-ся</strong> qoʻshimchasi oʻzbek tilidagi qaysi "
                "qoʻshimchaga oʻxshaydi?</p>",
        "choices": ["-lar (koʻplik)", "-(i)n- : yuvinmoq, kiyinmoq",
                    "-di (oʻtgan zamon)", "-moq (infinitiv)"],
        "correct": "-(i)n- : yuvinmoq, kiyinmoq",
        "explanation": "<p><em>Yuv-moq → yuv<strong>in</strong>-moq</em> = <em>мыть → "
                       "мы́ться</em>. Tushuncha siz uchun yangi emas: harakat oʻz "
                       "egasiga qaytadi. Faqat rus tilida bu qoʻshimcha eng oxirida "
                       "turadi va koʻproq ish bajaradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я учу́сь в шко́ле.", "Он бои́тся.",
                    "Они́ смею́т гро́мко.", "Мы встреча́емся в суббо́ту."],
        "correct": "Они́ смею́т гро́мко.",
        "explanation": "<p>Toʻgʻrisi — <strong>Они́ смею́тся</strong>. "
                       "<em>Смея́ться</em> <strong>-ся</strong> siz umuman mavjud emas, "
                       "xuddi <em>боя́ться, стара́ться, находи́ться</em> kabi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Афсо́на учи́лся в Москве́.", "Афсо́на учи́лась в Москве́.",
                    "Афсо́на учи́лись в Москве́.", "Афсо́на училась в Москве́."],
        "correct": "Афсо́на учи́лась в Москве́.",
        "explanation": "<p>Afsona — qiz, demak <em>учи́ла-</em>, va oxirida unli А, "
                       "demak <strong>-сь</strong>: <strong>учи́лась</strong>. Bu yerda "
                       "ikkita qoida ketma-ket ishlaydi — avval jins (PR-23), keyin "
                       "qaytim qoʻshimchasi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Где ты у́чишься?</strong></p>",
        "choices": ["— Я учу́сь в университе́те.", "— Я учу́ в университе́те.",
                    "— Я у́чится в университе́те.", "— Я учу́ся в университе́те."],
        "correct": "— Я учу́сь в университе́те.",
        "explanation": "<p>Savol <em>где?</em> — joy haqida, demak "
                       "<strong>учи́ться</strong>. «Я» uchun <strong>учу́сь</strong>: "
                       "unlidan keyin <em>-сь</em>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring. Gapirayotgan odam — "
                "<strong>yigit</strong>.</p><p><strong>Men suzishni oʻrgandim va endi "
                "qoʻrqmayman.</strong></p>",
        "choices": ["Я учи́лась пла́вать и тепе́рь не бою́сь.",
                    "Я учи́лся пла́вать и тепе́рь не бою́сь.",
                    "Я учи́лся пла́вать и тепе́рь не боя́лся.",
                    "Я учи́л пла́вать и тепе́рь не бою́сь."],
        "correct": "Я учи́лся пла́вать и тепе́рь не бою́сь.",
        "explanation": "<p>Yigit gapiryapti — <strong>учи́лся</strong> (erkak + undosh Л "
                       "→ -ся). Ikkinchi feʼl hozirgi zamonda va «я» shaklida — "
                       "<strong>бою́сь</strong> (unli Ю → -сь). <em>«Я учи́л "
                       "пла́вать»</em> boshqa maʼno berardi: «suzishni "
                       "oʻrgatardim».</p>",
    },
]


# =====================================================================
# PR-26 — Мочь va уметь
# =====================================================================

Q_PR26 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ пла́вать — я "
                "учи́лся два го́да.</strong></p>",
        "choices": ["могу́", "уме́ю", "мо́гут", "уме́ет"],
        "correct": "уме́ю",
        "explanation": "<p>Gapda oʻrganish haqida aytilgan — demak bu "
                       "<strong>mahorat</strong>, <em>уме́ть</em>. Oʻzbekcha tekshiruv: "
                       "«suzish<strong>ni bilaman</strong>» toʻgʻri kelyapti.</p>",
    },
    {
        "text": "<p><strong>мочь</strong> feʼlining «я» shakli qaysi?</p>",
        "choices": ["мо́жу", "мо́гу", "могу́", "мо́жет"],
        "correct": "могу́",
        "explanation": "<p><strong>Могу́</strong> — <strong>Г</strong> bilan va urgʻu "
                       "<strong>oxirida</strong>. Qolgan shakllarda urgʻu oʻzakka "
                       "qaytadi: <em>мо́жешь, мо́жет, мо́жем, мо́жете, мо́гут</em>.</p>",
    },
    {
        "text": "<p><strong>мочь</strong> feʼlining «они́» shakli qaysi?</p>",
        "choices": ["мо́жут", "мо́гут", "мо́жат", "могу́т"],
        "correct": "мо́гут",
        "explanation": "<p>Naqsh: «<strong>Г — ikki chetda, Ж — oʻrtada</strong>». "
                       "<em>Мо<strong>г</strong>у́ … мо́<strong>ж</strong>ешь, "
                       "мо́<strong>ж</strong>ет, мо́<strong>ж</strong>ем, "
                       "мо́<strong>ж</strong>ете … мо́<strong>г</strong>ут</em>. "
                       "<em>Мо́жут</em> — eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p><strong>уме́ть</strong> feʼli qanday tuslanadi?</p>",
        "choices": ["Oddiy I tuslanish: уме́ю, уме́ешь, уме́ет",
                    "II tuslanish: уме́ю, уми́шь, уми́т",
                    "Notoʻgʻri feʼl, alohida shakllar bilan",
                    "Birlikda I, koʻplikda II tuslanishda"],
        "correct": "Oddiy I tuslanish: уме́ю, уме́ешь, уме́ет",
        "explanation": "<p><em>Уме́ть</em> da hech qanday hiyla yoʻq — u <em>чита́ть</em> "
                       "bilan bir xil ishlaydi: <em>уме́ю, уме́ешь, уме́ет, уме́ем, "
                       "уме́ете, уме́ют</em>.</p>",
    },
    {
        "text": "<p><strong>мо́жет быть</strong> nima degani?</p>",
        "choices": ["albatta", "balki", "mumkin emas", "hech qachon"],
        "correct": "balki",
        "explanation": "<p>Bu ikki soʻz birga <strong>«balki»</strong> degani va u har "
                       "kuni ishlatiladi. Uni butun ibora sifatida yodlang — bu yerda "
                       "<em>мо́жет</em> tuslanmaydi: <em>Мо́жет быть, за́втра бу́дет "
                       "дождь.</em></p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ помога́ть.</strong> "
                "(мочь)</p>",
        "choices": ["мо́жем", "мо́гем", "мо́гут", "могу́"],
        "correct": "мо́жем",
        "explanation": "<p>«Мы» — oʻrtadagi shakllardan, demak <strong>Ж</strong>: "
                       "<em>мо́жем</em>. Va ikkinchi feʼl infinitivda qoladi — "
                       "<em>помога́ть</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д ___ бы́стро "
                "бе́гать.</strong> (уме́ть)</p>",
        "choices": ["уме́ю", "уме́ет", "уме́ют", "уме́ешь"],
        "correct": "уме́ет",
        "explanation": "<p>Uchinchi shaxs birligi — <strong>уме́ет</strong>. Tez yugurish "
                       "— oʻrganilgan va doim bor mahorat, shuning uchun aynan "
                       "<em>уме́ть</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Сего́дня я не ___ "
                "рабо́тать — я бо́лен.</strong></p>",
        "choices": ["уме́ю", "могу́", "мо́гут", "уме́ет"],
        "correct": "могу́",
        "explanation": "<p>Gapda <em>сего́дня</em> va sabab bor — demak vaziyatga "
                       "bogʻliq <strong>imkoniyat</strong>. <em>«Не уме́ю "
                       "рабо́тать»</em> butunlay boshqa maʼno berardi: «ishlashni "
                       "bilmayman».</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Она́ не мо́жет "
                "говори́ть.</strong></p>",
        "choices": ["Она́ не мог говори́ть.", "Она́ не мочи́ла говори́ть.",
                    "Она́ не могла́ говори́ть.", "Она́ не мо́жела говори́ть."],
        "correct": "Она́ не могла́ говори́ть.",
        "explanation": "<p>Ayol jinsi — <strong>могла́</strong>, urgʻu oxirida (xuddi "
                       "<em>была́</em> kabi). Erkak shaklida esa Л umuman boʻlmaydi: "
                       "<em>он не мог</em>.</p>",
    },
    {
        "text": "<p><strong>мочь</strong> feʼlining oʻtgan zamon erkak shakli "
                "qaysi?</p>",
        "choices": ["мочи́л", "мог", "мо́жил", "могл"],
        "correct": "мог",
        "explanation": "<p><strong>Мог</strong> — <strong>-л yoʻq</strong>. Bu rus "
                       "tilidagi bir nechta shunday feʼldan biri. Ayol va koʻplikda Л "
                       "qaytadi: <em>могла́, могли́</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ба́бушка ___ шить и "
                "гото́вить.</strong></p>",
        "choices": ["мо́жет", "уме́ет", "уме́ют", "могу́"],
        "correct": "уме́ет",
        "explanation": "<p>Tikish va ovqat pishirish — bir marta oʻrganilgan mahoratlar. "
                       "«Buvim tikish<strong>ni biladi</strong>» — «bilaman» toʻgʻri "
                       "kelyapti, demak <strong>уме́ть</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ___ говори́ть "
                "ме́дленно?</strong></p>",
        "choices": ["уме́ешь", "мо́жешь", "мо́гешь", "мо́жет"],
        "correct": "мо́жешь",
        "explanation": "<p>Bu iltimos: «sekinroq gapira olasizmi?» — vaziyatga bogʻliq, "
                       "demak <strong>мо́жешь</strong>. <em>«Уме́ешь говори́ть "
                       "ме́дленно?»</em> gʻalati eshitilardi: «sekin gapirishni "
                       "bilasanmi?»</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gap bir xil narsani anglatadimi?</p><p><strong>Я уме́ю "
                "води́ть маши́ну. · Я могу́ води́ть маши́ну.</strong></p>",
        "choices": ["Yoʻq: mahorat · shu ondagi imkoniyat",
                    "Ha, toʻliq bir xil",
                    "Yoʻq: birinchisi oʻtgan zamon",
                    "Yoʻq: ikkinchisi xato"],
        "correct": "Yoʻq: mahorat · shu ondagi imkoniyat",
        "explanation": "<p>Birinchisi — «mashina haydashni bilaman, oʻrganganman». "
                       "Ikkinchisi — «hozir haydashimga hech narsa xalaqit bermaydi». "
                       "Bir odam <em>уме́ет</em> boʻlib, bugun <em>не мо́жет</em> "
                       "boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Oʻzbekchadagi qaysi juftlik bu farqni koʻrsatadi?</p>",
        "choices": ["oʻqiyman · oʻqidim", "kitob · kitoblar",
                    "suzishni bilaman · suza olaman", "boraman · bormayman"],
        "correct": "suzishni bilaman · suza olaman",
        "explanation": "<p>Farq oʻzbekchada ham bor, faqat sezilmaydi: "
                       "«-ni <strong>bilaman</strong>» → <strong>уме́ть</strong>, "
                       "«-a <strong>olaman</strong>» → <strong>мочь</strong>. "
                       "Tarjima qilishdan oldin oʻzingizga shu savolni bering.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>уме́ть</strong> kerak, <strong>мочь</strong> "
                "emas?</p>",
        "choices": ["Сего́дня я не ___ — я рабо́таю.",
                    "Ба́бушка ___ чита́ть по-ара́бски.",
                    "Ты ___ помо́чь?",
                    "Мы не ___ — по́здно."],
        "correct": "Ба́бушка ___ чита́ть по-ара́бски.",
        "explanation": "<p>Arabcha oʻqish — bir marta oʻrganilgan mahorat, demak "
                       "<strong>уме́ет</strong>. Qolgan uchtasida vaqt, band boʻlish "
                       "yoki iltimos bor — hammasi vaziyatga bogʻliq, demak "
                       "<em>мочь</em>.</p>",
    },
    {
        "text": "<p><strong>мочь</strong> va <strong>уме́ть</strong> yonidagi ikkinchi "
                "feʼl qanday shaklda boʻladi?</p>",
        "choices": ["Hozirgi zamonda tuslanadi", "Infinitivda qoladi",
                    "Oʻtgan zamonda boʻladi", "Qaytim shaklida boʻladi"],
        "correct": "Infinitivda qoladi",
        "explanation": "<p>PR-19 dan beri oʻzgarmayotgan qoida: gapda faqat birinchi "
                       "feʼl tuslanadi. <em>Уме́ю чита́ть</em>, <em>не могу́ "
                       "рабо́тать</em>. <em>«Уме́ю чита́ю»</em> — xato.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я могу́ помога́ть.", "Она́ уме́ет шить.",
                    "Они́ мо́жут говори́ть по-ру́сски.", "Мы не мо́жем сего́дня."],
        "correct": "Они́ мо́жут говори́ть по-ру́сски.",
        "explanation": "<p>Toʻgʻrisi — <strong>Они́ мо́гут</strong>. Koʻplikda "
                       "<strong>Г</strong> qaytadi: «Г — ikki chetda, Ж — "
                       "oʻrtada».</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Ба́бушка мог гото́вить пло́в.", "Ба́бушка могла́ гото́вить пло́в.",
                    "Ба́бушка могли́ гото́вить пло́в.", "Ба́бушка мочи́ла гото́вить пло́в."],
        "correct": "Ба́бушка могла́ гото́вить пло́в.",
        "explanation": "<p>Buvi — ayol, demak <strong>могла́</strong>, urgʻu oxirida. "
                       "<em>Мог</em> — erkak shakli, <em>могли́</em> — koʻplik, "
                       "<em>мочи́ла</em> esa umuman mavjud emas.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты уме́ешь пла́вать?</strong></p>",
        "choices": ["— Да, уме́ю. Но сего́дня не могу́ — вода́ холо́дная.",
                    "— Да, могу́. Но сего́дня не уме́ю.",
                    "— Да, уме́ю пла́ваю.",
                    "— Да, я бу́ду уме́ть."],
        "correct": "— Да, уме́ю. Но сего́дня не могу́ — вода́ холо́дная.",
        "explanation": "<p>Aynan shu javob ikki feʼlning farqini eng aniq koʻrsatadi: "
                       "mahorat joyida (<strong>уме́ю</strong>), lekin bugun imkoniyat "
                       "yoʻq (<strong>не могу́</strong>). Ikkinchi variant teskari va "
                       "maʼnosiz.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Buvim biladi, lekin "
                "bugun qila olmaydi.</strong></p>",
        "choices": ["Ба́бушка мо́жет, но сего́дня не уме́ет.",
                    "Ба́бушка уме́ет, но сего́дня не мо́жет.",
                    "Ба́бушка уме́ет, но сего́дня не уме́ет.",
                    "Ба́бушка могла́, но сего́дня не мо́жет."],
        "correct": "Ба́бушка уме́ет, но сего́дня не мо́жет.",
        "explanation": "<p>«Biladi» → <strong>уме́ет</strong> (mahorat). «Bugun qila "
                       "olmaydi» → <strong>не мо́жет</strong> (imkoniyat). Bu gap butun "
                       "darsni bitta jumlaga jamlaydi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-24 Mashq: Kelasi zamon: буду + infinitiv",
        "description": (
            "Бу́ду, бу́дешь, бу́дет… + oʻzgarmagan infinitiv. Yolgʻiz «бу́ду», "
            "inkor «не бу́ду» va uchala zamon yonma-yon."
        ),
        "tutorial": "PR-24:",
        "questions": Q_PR24,
    },
    {
        "title": "PR-25 Mashq: Qaytim feʼllar -ся / -сь: учиться, находиться, нравиться",
        "description": (
            "Qachon -СЯ, qachon -СЬ; oʻtgan zamonda учи́лся / учи́лась; toʻrtta "
            "maʼno guruhi va учи́ть ↔ учи́ться farqi."
        ),
        "tutorial": "PR-25:",
        "questions": Q_PR25,
    },
    {
        "title": "PR-26 Mashq: Мочь va уметь — «-a olmoq» ning ikki xil turi",
        "description": (
            "Уме́ть — oʻrganilgan mahorat, мочь — shu ondagi imkoniyat. "
            "Мочь ning Г/Ж naqshi va «мог» ning yoʻqolgan Л si."
        ),
        "tutorial": "PR-26:",
        "questions": Q_PR26,
    },
]
