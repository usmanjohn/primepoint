# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-80 … PR-82.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_80_82.py --master=prime \\
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
# PR-80 — Sana, vaqt, yosh, davomiylik
# =====================================================================

Q_PR80 = [
    # 1–5 tanish
    {
        "text": "<p>Soat necha?</p><p><strong>полпя́того</strong></p>",
        "choices": ["5:30", "4:30", "5:15", "4:15"],
        "correct": "4:30",
        "explanation": "<p>Rus tili soatni <strong>kelayotgan</strong> soat "
                       "ichida sanaydi: «beshinchi soatning yarmi» = "
                       "<strong>4:30</strong>. Ruscha son har doim bittaga "
                       "katta koʻrinadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ два́дцать "
                "лет.</strong> (men yigirma yoshdaman)</p>",
        "choices": ["Я", "Меня́", "Мной", "Мне"],
        "correct": "Мне",
        "explanation": "<p>Yosh aytilganda odam <strong>Да́тельный</strong> da "
                       "turadi — bu PR-38 dagi <em>мне хо́лодно</em> bilan bir "
                       "oila. <s>Я два́дцать лет</s> deyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>без че́тверти "
                "пять</strong> — soat necha?</p>",
        "choices": ["5:15", "5:45", "4:45", "4:15"],
        "correct": "4:45",
        "explanation": "<p>«Beshga chorak qoldi» = <strong>4:45</strong>. "
                       "30 daqiqadan keyin rus tili <em>без</em> bilan "
                       "ayirishga oʻtadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ему́ два́дцать "
                "два ___.</strong></p>",
        "choices": ["го́да", "лет", "года́м", "год"],
        "correct": "го́да",
        "explanation": "<p>Oxirgi raqam <strong>2</strong>, demak "
                       "<em>го́да</em>. Qoida: 1 → год, 2–4 → го́да, 5–20 → "
                       "лет.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Davomiylik («uch yil "
                "yashadim») qanday beriladi?</p>",
        "choices": ["за + В.п.", "на + В.п.", "че́рез + В.п.",
                    "Predlogsiz Вини́тельный"],
        "correct": "Predlogsiz Вини́тельный",
        "explanation": "<p><em>Я жил там <strong>три го́да</strong></em> — "
                       "hech qanday predlog kerak emas, vaqt oddiy "
                       "Вини́тельный da turadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Soat necha?</p><p><strong>полсе́дьмого</strong></p>",
        "choices": ["7:30", "6:15", "7:15", "6:30"],
        "correct": "6:30",
        "explanation": "<p>«Yettinchi soatning yarmi» = <strong>6:30</strong>. "
                       "Yodda tuting: yettiga <strong>yetmadi</strong>, yarim "
                       "soat qoldi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я прочита́л "
                "кни́гу ___ два дня.</strong> (ikki kunda oʻqib chiqdim)</p>",
        "choices": ["че́рез", "на", "в", "за"],
        "correct": "за",
        "explanation": "<p><strong>За</strong> = ish shuncha vaqt "
                       "<strong>ichida</strong> bajarildi — oʻzbekcha «ikki "
                       "kun<strong>da</strong>». <em>Че́рез два дня</em> «ikki "
                       "kundan keyin» boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я прие́хал сюда́ "
                "___ неде́лю и в суббо́ту уезжа́ю.</strong></p>",
        "choices": ["на", "че́рез", "за", "в"],
        "correct": "на",
        "explanation": "<p><strong>На</strong> = moʻljallangan muddat — "
                       "oʻzbekcha «hafta<strong>ga</strong>». Shanbada "
                       "ketaman, demak bir haftaga kelganman.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ два часа́ я "
                "верну́сь.</strong> (ikki soatdan keyin)</p>",
        "choices": ["За", "Че́рез", "В", "На"],
        "correct": "Че́рез",
        "explanation": "<p><strong>Че́рез</strong> = «…dan keyin». Uchlik: "
                       "<em>за</em> — …da bajarildi, <em>че́рез</em> — …dan "
                       "keyin, <em>на</em> — …ga (muddatga).</p>",
    },
    {
        "text": "<p>«Qachon?» savoliga javob bering.</p><p><strong>Он "
                "прие́дет ___ ма́рта.</strong> (5-mart)</p>",
        "choices": ["пя́тое", "пя́того", "пя́тому", "пя́тым"],
        "correct": "пя́того",
        "explanation": "<p>«Qachon?» — <strong>Роди́тельный</strong>: "
                       "<em>пя́того ма́рта</em>. «Bugun nechanchi?» degan "
                       "savolga esa <em>пя́тое ма́рта</em> (И.п.) javob "
                       "beriladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он роди́лся в две "
                "ты́сячи ___ году́.</strong> (2008)</p>",
        "choices": ["восьмо́й", "во́семь", "восьмо́м", "восьмы́м"],
        "correct": "восьмо́м",
        "explanation": "<p><em>В како́м году́?</em> — Предло́жный, va "
                       "<strong>faqat oxirgi soʻz</strong> tartib songa "
                       "aylanadi: <em>две ты́сячи восьмо́м</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я хожу́ в бассе́йн "
                "два ра́за ___ .</strong> (haftasiga)</p>",
        "choices": ["неде́ли", "неде́ле", "в неде́лю", "на неде́лю"],
        "correct": "в неде́лю",
        "explanation": "<p>Qolip: <strong>N раз в</strong> + Вини́тельный. "
                       "«Bir marta» uchun <em>оди́н</em> aytilmaydi — "
                       "shunchaki <em>раз в ме́сяц</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я прие́хал на "
                "неде́лю. · Я прие́хал че́рез неде́лю.</strong></p>",
        "choices": ["Farqi umuman yoʻq",
                    "Birinchisi kelasi zamonda",
                    "«На» — haftaga, «че́рез» — haftadan keyin",
                    "Ikkinchisida xato bor"],
        "correct": "«На» — haftaga, «че́рез» — haftadan keyin",
        "explanation": "<p><em>На</em> — qancha vaqtga kelganim. <em>Че́рез</em> "
                       "— qachon kelganim. Ikkinchi gapda men allaqachon shu "
                       "yerdaman.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega ruscha soat oʻzbekchadan "
                "bittaga katta koʻrinadi?</p>",
        "choices": ["Chunki rus vaqti boshqa mintaqada",
                    "Chunki rus tili kelayotgan soat ichida sanaydi",
                    "Chunki tartib son ishlatiladi",
                    "Chunki oʻzbekcha 24 soatlik tizimda"],
        "correct": "Chunki rus tili kelayotgan soat ichida sanaydi",
        "explanation": "<p>«Uch yarim» — tugagan soat. <em>Полчетвёртого</em> — "
                       "«toʻrtinchining yarmi», yaʼni boshlangan soat "
                       "ichida.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Soat 2:00 da nima "
                "deysiz?</p>",
        "choices": ["в два часа́ но́чи", "в два часа́ утра́",
                    "в два часа́ дня", "в два часа́ ве́чера"],
        "correct": "в два часа́ но́чи",
        "explanation": "<p>Kun qismlari: <strong>но́чи</strong> (00–03), "
                       "<em>утра́</em> (04–11), <em>дня</em> (12–17), "
                       "<em>ве́чера</em> (18–23).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nechta yosh <strong>лет</strong> "
                "shaklini oladi?</p>",
        "choices": ["21", "22", "24", "13"],
        "correct": "13",
        "explanation": "<p><strong>11–14 har doim лет</strong>, oxirgi "
                       "raqamiga qaramay. <em>21 → год</em>, <em>22, 24 → "
                       "го́да</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мне два́дцать лет.", "Ему́ бы́ло три́дцать.",
                    "Я два́дцать лет.", "Ей бу́дет со́рок."],
        "correct": "Я два́дцать лет.",
        "explanation": "<p>Yosh aytilganda odam <strong>Да́тельный</strong> da "
                       "turadi: <strong>Мне</strong> два́дцать лет.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он придёт в без че́тверти пять.",
                    "Он придёт без че́тверти пять.",
                    "Он придёт без че́тверть пять.",
                    "Он придёт на без че́тверти пять."],
        "correct": "Он придёт без че́тверти пять.",
        "explanation": "<p><em>Без</em> dan oldin <strong>в qoʻyilmaydi</strong>. "
                       "Aniq soatda esa kerak: <em>в пять часо́в</em>. "
                       "<em>Че́тверти</em> — Роди́тельный.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Ско́лько тебе́ "
                "лет?</strong></p>",
        "choices": ["— Я два́дцать оди́н год.", "— Мне два́дцать оди́н лет.",
                    "— Мне два́дцать оди́н го́да.", "— Мне два́дцать оди́н год."],
        "correct": "— Мне два́дцать оди́н год.",
        "explanation": "<p>Odam <strong>Да́тельный</strong> da, oxirgi raqam "
                       "<strong>1</strong> — demak <strong>год</strong>.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Ishni uch "
                "soatda tugatdim va ikki soatdan keyin uyga qaytdim.</strong></p>",
        "choices": ["Я зако́нчил рабо́ту че́рез три часа́ и за два часа́ верну́лся домо́й.",
                    "Я зако́нчил рабо́ту на три часа́ и че́рез два часа́ верну́лся домо́й.",
                    "Я зако́нчил рабо́ту за три часа́ и че́рез два часа́ верну́лся домо́й.",
                    "Я зако́нчил рабо́ту за три часа́ и за два часа́ верну́лся домо́й."],
        "correct": "Я зако́нчил рабо́ту за три часа́ и че́рез два часа́ верну́лся домо́й.",
        "explanation": "<p>«Uch soat<strong>da</strong>» → <em>за</em> (ish "
                       "shuncha vaqt ichida bajarildi). «Ikki soat<strong>dan "
                       "keyin</strong>» → <em>че́рез</em>.</p>",
    },
]


# =====================================================================
# PR-81 — Shaxssiz gaplar
# =====================================================================

Q_PR81 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Shaxssiz gapning asosiy "
                "belgisi nima?</p>",
        "choices": ["Feʼl koʻplikda turadi", "Gapda inkor boʻladi",
                    "Имени́тельный da ega yoʻq", "Gap savol boʻladi"],
        "correct": "Имени́тельный da ega yoʻq",
        "explanation": "<p><em>Темне́ет</em> — kim qorongʻilashtiryapti? Hech "
                       "kim. Gapda bosh kelishikda turgan soʻz umuman "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ о́чень "
                "хо́лодно.</strong> (menga sovuq)</p>",
        "choices": ["Я", "Меня́", "Мной", "Мне"],
        "correct": "Мне",
        "explanation": "<p>Holat gapida odam <strong>Да́тельный</strong> da "
                       "turadi. Oʻzbekcha «men<strong>ga</strong> sovuq» "
                       "dagi <em>-ga</em> shuni koʻrsatib turibdi.</p>",
    },
    {
        "text": "<p>Dilnoza gapiryapti. Toʻgʻri shaklni tanlang.</p>"
                "<p><strong>Мне ___ хо́лодно в по́езде.</strong></p>",
        "choices": ["была́", "был", "бы́ли", "бы́ло"],
        "correct": "бы́ло",
        "explanation": "<p>Shaxssiz gapda moslashadigan ega yoʻq, shuning uchun "
                       "feʼl <strong>har doim oʻrta jinsda</strong> — kim "
                       "gapirayotganidan qatʼi nazar.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Мне не "
                "спи́тся</strong> nimani bildiradi?</p>",
        "choices": ["Uxlashni xohlamayman", "Uyqum kelmayapti",
                    "Uxlab qoldim", "Uxlash mumkin emas"],
        "correct": "Uyqum kelmayapti",
        "explanation": "<p>Bu <strong>istak emas, holat</strong>. "
                       "<em>Я не хочу́ спать</em> — xohlamayman. <em>Мне не "
                       "спи́тся</em> — xohlayman, lekin uxlay "
                       "olmayapman.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Говоря́т, зима́ "
                "бу́дет холо́дной</strong> — «говоря́т» kim?</p>",
        "choices": ["Aniq bir guruh odamlar", "Soʻzlovchining oʻzi",
                    "Ob-havo xizmati", "Aytilmaydi — nomaʼlum shaxs"],
        "correct": "Aytilmaydi — nomaʼlum shaxs",
        "explanation": "<p>Feʼl <em>они́</em> shaklida turadi, lekin «ular» kim "
                       "ekani aytilmaydi. Oʻzbekchada bu "
                       "<strong>-ishdi / -isharmish</strong> bilan "
                       "beriladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ гру́стно "
                "сего́дня.</strong> (unga — erkak)</p>",
        "choices": ["Он", "Его́", "Ему́", "Им"],
        "correct": "Ему́",
        "explanation": "<p>Да́тельный, erkak — <strong>ему́</strong>. Ayol "
                       "boʻlsa <em>ей</em>, koʻplik <em>им</em>, «bizga» "
                       "<em>нам</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У меня́ нет "
                "___.</strong> (vaqt)</p>",
        "choices": ["вре́мя", "вре́мени", "вре́менем", "вре́мена"],
        "correct": "вре́мени",
        "explanation": "<p><em>Нет</em> dan keyin ot <strong>Роди́тельный</strong> "
                       "da turadi. <em>Вре́мя</em> — oʻrta jinsdagi maxsus "
                       "ot: <em>вре́мени, вре́менем</em>.</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻgiring.</p><p><strong>Вре́мени "
                "нет.</strong></p>",
        "choices": ["Вре́мени не бы́ло.", "Вре́мени не́ было.",
                    "Вре́мя не́ было.", "Вре́мени не была́."],
        "correct": "Вре́мени не́ было.",
        "explanation": "<p><strong>Не́ было</strong> — alohida yoziladi va urgʻu "
                       "<em>не</em> ga tushadi. Ot esa Роди́тельный da "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ "
                "ча́ю.</strong> (choy ichgim kelyapti)</p>",
        "choices": ["хочу́", "хо́чется", "хоте́л", "хоти́те"],
        "correct": "хо́чется",
        "explanation": "<p><strong>Хо́чется</strong> — yumshoq, «ichsam yomon "
                       "boʻlmasdi». <em>Я хочу́ чай</em> esa qatʼiy istak va "
                       "u shaxssiz gap emas.</p>",
    },
    {
        "text": "<p>Bu gapni shaxssiz qiling.</p><p><strong>Ве́тер сорва́л "
                "кры́шу.</strong></p>",
        "choices": ["Кры́шу сорва́л ве́тер.", "Кры́ша сорвала́сь ве́тром.",
                    "Кры́шу сорва́ло ве́тром.", "Кры́ше сорва́ло ве́тер."],
        "correct": "Кры́шу сорва́ло ве́тром.",
        "explanation": "<p>Obyekt <strong>Вини́тельный</strong> da qoladi "
                       "(<em>кры́шу</em>), kuch <strong>Твори́тельный</strong> "
                       "ga oʻtadi (<em>ве́тром</em>), feʼl esa oʻrta "
                       "jinsga.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Доро́гу ___ "
                "сне́гом.</strong></p>",
        "choices": ["занесла́", "занёс", "занесли́", "занесло́"],
        "correct": "занесло́",
        "explanation": "<p>Shaxssiz gapda feʼl <strong>oʻrta jinsda</strong>. "
                       "Bu qurilish havo xabarlarida doim uchraydi: "
                       "<em>занесло́ сне́гом</em>, <em>унесло́ "
                       "тече́нием</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Меня́ пригласи́ли "
                "на сва́дьбу</strong> — kim taklif qildi?</p>",
        "choices": ["Aytilmagan — muhim emas", "Men oʻzim", "Toʻy egasi", "Hech kim"],
        "correct": "Aytilmagan — muhim emas",
        "explanation": "<p>Feʼl koʻplikda, lekin ega yoʻq. Oʻzbekchada aynan "
                       "shunday: «meni taklif qil<strong>ishdi</strong>» — "
                       "kim qilgani aytilmaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я не хочу́ "
                "спать. · Мне не спи́тся.</strong></p>",
        "choices": ["Farqi umuman yoʻq",
                    "Ikkinchisi kelasi zamonda",
                    "Birinchisida xato bor",
                    "Birinchisi istak, ikkinchisi holat"],
        "correct": "Birinchisi istak, ikkinchisi holat",
        "explanation": "<p>«Uxlashni xohlamayman» ↔ «uxlay olmayapman». "
                       "Ikkinchisida men hech narsa qilmayapman — holat "
                       "oʻz-oʻzidan shunday.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«-ga»</strong> "
                "(menga sovuq) ruschada qaysi kelishikka toʻgʻri keladi?</p>",
        "choices": ["Роди́тельный", "Твори́тельный", "Да́тельный", "Предло́жный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>men<strong>ga</strong> sovuq</em> → <em><strong>мне</strong> "
                       "хо́лодно</em>. Bu PR-38 da boshlangan chiziq va "
                       "shaxssiz gaplarning oʻzagi.</p>",
    },
    {
        "text": "<p>Qaysi gap shaxssiz EMAS?</p>",
        "choices": ["Темне́ет ра́но.", "Мне хо́лодно.",
                    "Со́лнце сади́тся ра́но.", "Ну́жно идти́."],
        "correct": "Со́лнце сади́тся ра́но.",
        "explanation": "<p>Bu gapda <strong>ega bor</strong> — <em>со́лнце</em>, "
                       "Имени́тельный da. Qolgan uchtasida ega umuman "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega ruslar «Кры́шу "
                "сорва́ло ве́тром» deyishni afzal koʻradi?</p>",
        "choices": ["Chunki bu qisqaroq",
                    "Chunki shamol ayblanmaydi — voqea oʻzi sodir boʻlgandek",
                    "Chunki «ве́тер» ega boʻla olmaydi",
                    "Chunki bu kelasi zamon"],
        "correct": "Chunki shamol ayblanmaydi — voqea oʻzi sodir boʻlgandek",
        "explanation": "<p><em>Ве́тер сорва́л кры́шу</em> ham toʻgʻri. Lekin "
                       "shaxssiz shakl tabiat hodisasini javobgarsiz "
                       "koʻrsatadi — rus tili buni yaxshi koʻradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мне хо́лодно.", "Я хо́лодно.",
                    "Нам ску́чно.", "Ему́ гру́стно."],
        "correct": "Я хо́лодно.",
        "explanation": "<p>Odam <strong>Да́тельный</strong> da turishi kerak: "
                       "<strong>Мне</strong> хо́лодно.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Доро́гу занесла́ снег.", "Доро́га занесло́ сне́гом.",
                    "Доро́гу занесло́ сне́гом.", "Доро́ге занесло́ снег."],
        "correct": "Доро́гу занесло́ сне́гом.",
        "explanation": "<p>Uchta narsa bir vaqtda: obyekt Вини́тельный da, kuch "
                       "Твори́тельный da, feʼl oʻrta jinsda.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Почему́ ты не "
                "спишь?</strong></p>",
        "choices": ["— Не зна́ю, мне не спи́тся.", "— Не зна́ю, я не спи́тся.",
                    "— Не зна́ю, мне не сплю.", "— Не зна́ю, меня́ не спи́тся."],
        "correct": "— Не зна́ю, мне не спи́тся.",
        "explanation": "<p>Odam <strong>Да́тельный</strong> da, feʼl esa "
                       "<em>-ся</em> bilan oʻrta shaklda. Bu holat, "
                       "ixtiyor emas.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Kechqurun "
                "qorongʻi tushdi va bizga sovuq boʻldi.</strong></p>",
        "choices": ["Ве́чером стемне́ло, и нам ста́ло хо́лодно.",
                    "Ве́чером стемне́л, и мы ста́ли хо́лодно.",
                    "Ве́чером стемне́ло, и мы ста́ло хо́лодно.",
                    "Ве́чером стемне́ла, и нам ста́ла хо́лодно."],
        "correct": "Ве́чером стемне́ло, и нам ста́ло хо́лодно.",
        "explanation": "<p>Ikkala qism ham shaxssiz: birinchisida ega umuman "
                       "yoʻq, ikkinchisida odam <em>нам</em> shaklida chetda. "
                       "Feʼllar oʻrta jinsda.</p>",
    },
]


# =====================================================================
# PR-82 — Jamlovchi va tartib sonlar
# =====================================================================

Q_PR82 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri variantni tanlang.</p><p><strong>3</strong> ning "
                "tartib soni</p>",
        "choices": ["тро́е", "тре́тий", "три́жды", "тройно́й"],
        "correct": "тре́тий",
        "explanation": "<p><strong>Тре́тий</strong> — tartib son. <em>Тро́е</em> "
                       "esa jamlovchi son («uchalasi»).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Uzun tartib sonda nechta "
                "soʻz oʻzgaradi?</p>",
        "choices": ["Hammasi", "Faqat birinchisi", "Faqat oxirgisi", "Ikkitasi"],
        "correct": "Faqat oxirgisi",
        "explanation": "<p><em>в две ты́сячи восьмо́м году́</em> — faqat "
                       "<strong>восьмо́м</strong> turlandi, qolgani qotib "
                       "qoldi. Sanalarda ham shunday: <em>три́дцать пе́рвое "
                       "ма́я</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Вдвоём</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Ikki marta", "Ikkinchi", "Ikki baravar", "Ikkovlashib"],
        "correct": "Ikkovlashib",
        "explanation": "<p><em>Мы пошли́ <strong>вдвоём</strong></em> — "
                       "«ikkalamiz bordik». Oʻzbekcha «-ovlashib» ga aynan "
                       "toʻgʻri keladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri variantni tanlang.</p><p><strong>___ де́вушки</strong> "
                "(uchta qiz)</p>",
        "choices": ["тро́е", "тре́тьи", "трои́х", "три"],
        "correct": "три",
        "explanation": "<p>Ayol kishilarga <strong>jamlovchi son "
                       "qoʻyilmaydi</strong>: <s>тро́е де́вушек</s> → "
                       "<strong>три де́вушки</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ сестры́ "
                "прие́хали.</strong> (ikkala singil ham)</p>",
        "choices": ["О́ба", "О́бе", "Дво́е", "Вдвоём"],
        "correct": "О́бе",
        "explanation": "<p><em>Сестра́</em> ayol jinsida, demak "
                       "<strong>о́бе</strong>. Eslatma: <em>о́б<strong>е</strong></em> "
                       "ichidagi <strong>е</strong> — «жЕнский» dagi "
                       "<strong>е</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он роди́лся в две "
                "ты́сячи ___ году́.</strong> (2010)</p>",
        "choices": ["де́сять", "деся́тый", "деся́том", "деся́тым"],
        "correct": "деся́том",
        "explanation": "<p><em>В како́м году́?</em> — Предло́жный. Faqat "
                       "oxirgi soʻz tartib songa aylanadi va "
                       "turlanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы живём на ___ "
                "этаже́.</strong> (uchinchi)</p>",
        "choices": ["тре́тьем", "тре́тий", "тре́тьим", "тре́тього"],
        "correct": "тре́тьем",
        "explanation": "<p><strong>Тре́тий</strong> yumshoq namunada "
                       "turlanadi: <em>тре́тьего, тре́тьему, тре́тьим, о "
                       "тре́тьем</em>. Bu yagona istisno tartib son.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У них ___ "
                "дете́й.</strong> (ikkita bola)</p>",
        "choices": ["две", "о́ба", "два", "дво́е"],
        "correct": "дво́е",
        "explanation": "<p>Bolalar bilan <strong>jamlovchi son</strong> "
                       "ishlatiladi: <em>дво́е дете́й</em>. Ot esa "
                       "Роди́тельный koʻplikda turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Нас бы́ло "
                "___.</strong> (beshtamiz edik)</p>",
        "choices": ["пять", "пя́теро", "пя́тый", "впятеро́м"],
        "correct": "пя́теро",
        "explanation": "<p>«Bizlar» haqida gapirilganda jamlovchi son "
                       "ishlatiladi: <em>нас бы́ло <strong>пя́теро</strong></em>. "
                       "<em>Впятеро́м</em> esa «beshovlashib» — feʼl bilan "
                       "keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́дел там "
                "___.</strong> (uchtasini)</p>",
        "choices": ["тро́е", "трои́м", "трои́х", "тре́тьих"],
        "correct": "трои́х",
        "explanation": "<p>Jamlovchi son ham turlanadi. Вини́тельный, jonli — "
                       "<strong>трои́х</strong>. Д.п. esa "
                       "<em>трои́м</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы е́хали ___ "
                "су́ток.</strong> (ikki kecha-kunduz)</p>",
        "choices": ["две", "два", "дво́е", "о́ба"],
        "correct": "дво́е",
        "explanation": "<p><em>Су́тки</em> — faqat koʻplikda ishlatiladigan ot, "
                       "va bunday otlar bilan <strong>jamlovchi son</strong> "
                       "kerak: <em>дво́е су́ток</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он съел ___ "
                "лепёшки.</strong> (bir yarim)</p>",
        "choices": ["полтора́", "полови́на", "полторы́", "полтора́м"],
        "correct": "полторы́",
        "explanation": "<p><em>Лепёшка</em> ayol jinsida, demak "
                       "<strong>полторы́</strong>. Erkak va oʻrta jins uchun "
                       "<em>полтора́</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Пришли́ два "
                "бра́та. · Пришли́ о́ба бра́та.</strong></p>",
        "choices": ["Farqi yoʻq",
                    "Ikkinchisi savol gap",
                    "Birinchisida xato bor",
                    "«О́ба» — ikkalasi HAM, biri ham qolmadi"],
        "correct": "«О́ба» — ikkalasi HAM, biri ham qolmadi",
        "explanation": "<p><em>Два</em> shunchaki sonini aytadi. <em>О́ба</em> "
                       "esa «ikkalasi <strong>ham</strong>» degan taʼkid — "
                       "oʻzbekchada «ham» soʻzi eshitilsa, <em>о́ба/о́бе</em> "
                       "qoʻying.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi holatda jamlovchi son "
                "ishlatilmaydi?</p>",
        "choices": ["Erkaklar guruhi bilan", "Bolalar bilan",
                    "Ayol kishilar bilan", "«Bizlar» haqida gapirilganda"],
        "correct": "Ayol kishilar bilan",
        "explanation": "<p>Bu darsning yagona qatʼiy taqiqi: <s>дво́е "
                       "де́вушек</s> → <strong>две де́вушки</strong>. "
                       "Aralash guruh boʻlsa — jamlovchi mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дво́е</strong> bilan "
                "<strong>вдвоём</strong> ning farqi nimada?</p>",
        "choices": ["Farqi yoʻq",
                    "«Дво́е» — son (ikkitasi), «вдвоём» — ravish (ikkovlashib)",
                    "«Вдвоём» faqat ayollar haqida",
                    "«Дво́е» kelasi zamonda ishlatiladi"],
        "correct": "«Дво́е» — son (ikkitasi), «вдвоём» — ravish (ikkovlashib)",
        "explanation": "<p><em>Пришли́ <strong>дво́е</strong></em> — ikkitasi "
                       "keldi. <em>Мы пошли́ <strong>вдвоём</strong></em> — "
                       "ikkovlashib bordik. Ikkinchisi feʼlni "
                       "aniqlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi soʻz "
                "<strong>notoʻgʻri</strong>?</p>",
        "choices": ["дво́е су́ток", "тро́е дете́й", "дво́е часо́в", "че́тверо котя́т"],
        "correct": "дво́е часо́в",
        "explanation": "<p><s>Дво́е часо́в</s> → <strong>два часа́</strong>. "
                       "Jamlovchi son faqat beshta holatda ishlatiladi; "
                       "oddiy vaqt oʻlchovi ularga kirmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Тро́е рабо́чих зако́нчили рабо́ту.",
                    "Дво́е де́вушек стоя́ли у окна́.",
                    "У них дво́е дете́й.",
                    "Нас бы́ло че́тверо."],
        "correct": "Дво́е де́вушек стоя́ли у окна́.",
        "explanation": "<p>Ayol kishilarga jamlovchi son qoʻyilmaydi: "
                       "<strong>две де́вушки стоя́ли</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["О́ба сестры́ прие́хали.", "О́бе сестры́ прие́хали.",
                    "Дво́е сестёр прие́хали.", "О́бои сестры́ прие́хали."],
        "correct": "О́бе сестры́ прие́хали.",
        "explanation": "<p>Ayol jinsida <strong>о́бе</strong>. <em>Дво́е "
                       "сестёр</em> ham notoʻgʻri — ayollarga jamlovchi son "
                       "qoʻyilmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Вы пое́дете "
                "вме́сте?</strong></p>",
        "choices": ["— Да, мы пое́дем вдвоём.", "— Да, мы пое́дем дво́е.",
                    "— Да, мы пое́дем о́ба.", "— Да, мы пое́дем второ́й."],
        "correct": "— Да, мы пое́дем вдвоём.",
        "explanation": "<p>Feʼlni aniqlaydigan shakl — <strong>вдвоём</strong> "
                       "(«ikkovlashib»). <em>Дво́е</em> son sifatida "
                       "ishlatilardi: <em>нас дво́е</em>.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Bizlar uchta "
                "edik va ikkala qayiq ham kichkina edi.</strong></p>",
        "choices": ["Нас бы́ло три, и о́ба ло́дки бы́ли ма́ленькие.",
                    "Нас бы́ло тро́е, и о́бе ло́дки бы́ли ма́ленькие.",
                    "Нас бы́ло тро́е, и о́ба ло́дки бы́ли ма́ленькие.",
                    "Нас бы́ли трои́х, и о́бе ло́дки бы́ли ма́ленькие."],
        "correct": "Нас бы́ло тро́е, и о́бе ло́дки бы́ли ма́ленькие.",
        "explanation": "<p>«Bizlar uchta» — jamlovchi son <strong>тро́е</strong>. "
                       "<em>Ло́дка</em> ayol jinsida, demak "
                       "<strong>о́бе</strong>.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-80 Mashq: Sana, vaqt, yosh va davomiylik",
        "description": (
            "Полпя́того = 4:30 — rus tili kelayotgan soat ichida sanaydi. Sana, "
            "yosh (Да́тельный bilan) va за / че́рез / на uchligi."
        ),
        "tutorial": "PR-80:",
        "questions": Q_PR80,
    },
    {
        "title": "PR-81 Mashq: Shaxssiz gaplar",
        "description": (
            "Egasi yoʻq gaplar: мне хо́лодно, темне́ет, мне не спи́тся, "
            "говоря́т. Plus kuchni Твори́тельный bilan aytadigan qurilish."
        ),
        "tutorial": "PR-81:",
        "questions": Q_PR81,
    },
    {
        "title": "PR-82 Mashq: Jamlovchi va tartib sonlar",
        "description": (
            "Дво́е, тро́е, вдвоём, о́ба / о́бе va tartib sonlar. Ayollarga "
            "jamlovchi son qoʻyilmaydi; uzun sonda faqat oxirgi soʻz oʻzgaradi."
        ),
        "tutorial": "PR-82:",
        "questions": Q_PR82,
    },
]
