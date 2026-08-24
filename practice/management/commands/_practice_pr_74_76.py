# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-74 … PR-76.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_74_76.py --master=prime \\
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
# PR-74 — Sifat darajalari
# =====================================================================

Q_PR74 = [
    # 1–5 tanish
    {
        "text": "<p>Qiyosiy shaklni tanlang.</p><p><strong>интере́сный</strong></p>",
        "choices": ["интере́сее", "интере́сше", "бо́лее интере́снее", "интере́снее"],
        "correct": "интере́снее",
        "explanation": "<p>Oddiy sifatlar <strong>-ее</strong> qoʻshimchasini "
                       "oladi. <em>Бо́лее интере́снее</em> — ikki marta daraja, "
                       "bunday qilinmaydi.</p>",
    },
    {
        "text": "<p>Qiyosiy shaklni tanlang.</p><p><strong>хоро́ший</strong></p>",
        "choices": ["хоро́шее", "хороши́е", "лу́чше", "бо́лее хоро́ший"],
        "correct": "лу́чше",
        "explanation": "<p>Bu beshta notoʻgʻri shakldan biri, yodlash kerak: "
                       "<em>хоро́ший → <strong>лу́чше</strong></em>, "
                       "<em>плохо́й → ху́же</em>, <em>большо́й → бо́льше</em>, "
                       "<em>ма́ленький → ме́ньше</em>, <em>ста́рый → "
                       "ста́рше</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«eng»</strong> "
                "ruschada nima boʻladi?</p>",
        "choices": ["чем", "бо́лее", "са́мый", "гора́здо"],
        "correct": "са́мый",
        "explanation": "<p><em><strong>са́мый</strong> большо́й го́род</em> — «eng "
                       "katta shahar». Bitta farq: oʻzbekcha «eng» oʻzgarmaydi, "
                       "ruscha <em>са́мый</em> esa sifat kabi turlanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Чем</strong> dan "
                "oldin nima qoʻyiladi?</p>",
        "choices": ["Vergul", "Tire", "Ikki nuqta", "Hech narsa"],
        "correct": "Vergul",
        "explanation": "<p><em>Москва́ бо́льше<strong>,</strong> чем "
                       "Ташке́нт.</em> Vergul majburiy va uni tashlab ketish — "
                       "eng koʻp uchraydigan xatolardan biri.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ста́рше</strong> "
                "bilan <strong>старе́е</strong> ning farqi nimada?</p>",
        "choices": ["Farqi yoʻq", "«Ста́рше» — odam, «старе́е» — narsa haqida",
                    "«Старе́е» faqat koʻplikda", "«Ста́рше» eskirgan shakl"],
        "correct": "«Ста́рше» — odam, «старе́е» — narsa haqida",
        "explanation": "<p><em>Он <strong>ста́рше</strong> меня́</em> — mendan "
                       "katta. <em>Э́тот дом <strong>старе́е</strong></em> — bu "
                       "uy eskiroq. Oʻzbekchada ham odam «katta», narsa "
                       "«eski».</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Qiyosiy shaklni tanlang.</p><p><strong>дорого́й</strong></p>",
        "choices": ["дорого́е", "доро́гее", "дорожа́е", "доро́же"],
        "correct": "доро́же",
        "explanation": "<p>Oʻzak <strong>-г</strong> bilan tugagan, demak "
                       "<strong>-е</strong> qoʻshimchasi va undosh almashinadi: "
                       "<em>г → ж</em>. Shu guruhda <em>молодо́й → моло́же</em>, "
                       "<em>бли́зкий → бли́же</em>.</p>",
    },
    {
        "text": "<p>Qiyosiy shaklni tanlang.</p><p><strong>высо́кий</strong></p>",
        "choices": ["вы́ше", "высо́чее", "высоке́е", "вы́сше"],
        "correct": "вы́ше",
        "explanation": "<p><em>к → ш</em>: <strong>вы́ше</strong>. Juftlari: "
                       "<em>ни́зкий → ни́же</em>, <em>широ́кий → ши́ре</em>, "
                       "<em>у́зкий → у́же</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Москва́ бо́льше "
                "___.</strong> (Ташке́нт, «чем» siz)</p>",
        "choices": ["Ташке́нту", "Ташке́нтом", "Ташке́нта", "Ташке́нт"],
        "correct": "Ташке́нта",
        "explanation": "<p><em>Чем</em> siz solishtirilganda "
                       "<strong>Роди́тельный</strong> ishlatiladi — bu "
                       "oʻzbekcha <strong>-dan</strong> ning aynan oʻzi: "
                       "«Toshkent<strong>dan</strong> katta».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Брат ___ ста́рше "
                "меня́.</strong> (uch yosh)</p>",
        "choices": ["три го́да", "на три го́да", "за три го́да", "с трёх лет"],
        "correct": "на три го́да",
        "explanation": "<p>Farq <strong>на</strong> + Вини́тельный bilan "
                       "beriladi. Oʻzbekchada hech qanday belgi yoʻq («uch yosh "
                       "katta»), ruschada esa <em>на</em> qoʻyilishi shart.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дай мне ___ "
                "кни́гу.</strong> (qiziqarliroq)</p>",
        "choices": ["интере́снее", "бо́лее интере́сную", "са́мую интере́снее",
                    "бо́лее интере́снее"],
        "correct": "бо́лее интере́сную",
        "explanation": "<p>Oddiy qiyosiy shakl (<em>интере́снее</em>) faqat "
                       "<strong>kesim</strong> boʻla oladi. Otni aniqlash kerak "
                       "boʻlsa — <strong>бо́лее</strong> + toʻliq sifat.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он бе́гает "
                "быстре́е ___.</strong> (hammadan)</p>",
        "choices": ["всего́", "все", "всем", "всех"],
        "correct": "всех",
        "explanation": "<p><strong>Всех</strong> — odamlar bilan solishtirilganda. "
                       "<em>Всего́</em> esa ish yoki narsalar bilan: "
                       "<em>бо́льше всего́ я люблю́ ле́то</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бо́льше ___ я "
                "люблю́ чита́ть.</strong></p>",
        "choices": ["всех", "все́ми", "всего́", "всем"],
        "correct": "всего́",
        "explanation": "<p>Bu yerda ish (<em>чита́ть</em>) boshqa ishlar bilan "
                       "solishtirilyapti, odamlar bilan emas — demak "
                       "<strong>всего́</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«-dan»</strong> "
                "(«Toshkentdan katta») ruschada qaysi kelishikka toʻgʻri "
                "keladi?</p>",
        "choices": ["Да́тельный", "Твори́тельный", "Предло́жный", "Роди́тельный"],
        "correct": "Роди́тельный",
        "explanation": "<p><em>бо́льше Ташке́нт<strong>а</strong></em>, "
                       "<em>моло́же мен<strong>я́</strong></em>. Ikkala tilda "
                       "ham solishtiriladigan narsa qoʻshimcha oladi — bu "
                       "darsning eng foydali mosligi.</p>",
    },
    {
        "text": "<p>Qaysi ikki gap bir xil maʼnoni beradi?</p>",
        "choices": ["«Он ста́рше меня́» va «он ста́рше, чем я»",
                    "«Он ста́рше меня́» va «он ста́рше, чем меня́»",
                    "«Он ста́рше меня́» va «он бо́лее ста́рше»",
                    "«Он ста́рше меня́» va «он са́мый ста́рый»"],
        "correct": "«Он ста́рше меня́» va «он ста́рше, чем я»",
        "explanation": "<p>Ikki yoʻl: <strong>Роди́тельный</strong> "
                       "(<em>меня́</em>) yoki <strong>чем + "
                       "Имени́тельный</strong> (<em>чем я</em>). "
                       "<em>Чем меня́</em> — xato: <em>чем</em> dan keyin "
                       "И.п. turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <s>«интере́снее "
                "кни́га»</s> deb boʻlmaydi?</p>",
        "choices": ["Chunki «кни́га» ayol jinsida",
                    "Chunki oddiy qiyosiy shakl otdan oldin turolmaydi",
                    "Chunki «интере́снее» eskirgan shakl",
                    "Chunki vergul yetishmayapti"],
        "correct": "Chunki oddiy qiyosiy shakl otdan oldin turolmaydi",
        "explanation": "<p>U faqat kesim boʻla oladi: <em>э́та кни́га "
                       "интере́снее</em>. Aniqlovchi kerak boʻlsa — "
                       "<strong>бо́лее интере́сная кни́га</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Са́мый</strong> "
                "oʻzbekcha «eng» dan nimasi bilan farq qiladi?</p>",
        "choices": ["Maʼnosi boshqa", "U turlanadi — jins, son, kelishikda",
                    "U faqat yozma nutqda ishlatiladi", "U otdan keyin turadi"],
        "correct": "U turlanadi — jins, son, kelishikda",
        "explanation": "<p><em>в <strong>са́мом</strong> большо́м го́роде</em>, "
                       "<em>о <strong>са́мой</strong> дли́нной реке́</em>. "
                       "Oʻzbekcha «eng» esa hech qachon oʻzgarmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Москва́ бо́льше, чем Ташке́нт.", "Москва́ бо́льше Ташке́нта.",
                    "Он на два го́да ста́рше меня́.", "Он бо́лее ста́рше меня́."],
        "correct": "Он бо́лее ста́рше меня́.",
        "explanation": "<p>Ikki marta qiyosiy daraja qoʻyilgan. Toʻgʻrisi — "
                       "<strong>Он ста́рше меня́</strong>. <em>Бо́лее</em> dan "
                       "keyin faqat toʻliq sifat keladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Э́та река́ длинне́е чем та.", "Э́та река́ длинне́е той.",
                    "Э́та река́ длинне́е чем той.", "Э́та река́ бо́лее длинне́е."],
        "correct": "Э́та река́ длинне́е той.",
        "explanation": "<p><em>Чем</em> siz — <strong>Роди́тельный</strong>: "
                       "<em>той</em>. Birinchi variantda vergul yetishmayapti, "
                       "uchinchisida <em>чем</em> dan keyin Р.п. qoʻyilgan, "
                       "toʻrtinchisida ikki marta daraja.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Како́й го́род тебе́ "
                "понра́вился бо́льше?</strong></p>",
        "choices": ["— Самарка́нд. Он краси́вее, чем Бухара́.",
                    "— Самарка́нд. Он бо́лее краси́вее Бухары́.",
                    "— Самарка́нд. Он краси́вее чем Бухара́.",
                    "— Самарка́нд. Он са́мый краси́вее."],
        "correct": "— Самарка́нд. Он краси́вее, чем Бухара́.",
        "explanation": "<p>Vergul <em>чем</em> dan oldin, undan keyin esa "
                       "Имени́тельный — <em>Бухара́</em>. <em>Краси́вее "
                       "Бухары́</em> ham toʻgʻri boʻlardi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Bu yoʻl "
                "ancha qisqaroq.</strong></p>",
        "choices": ["Э́тот путь гора́здо коро́че.", "Э́тот путь чуть коро́че.",
                    "Э́тот путь са́мый коро́че.", "Э́тот путь бо́лее коро́че."],
        "correct": "Э́тот путь гора́здо коро́че.",
        "explanation": "<p>«Ancha» — <strong>гора́здо</strong> yoki "
                       "<em>намно́го</em>. <em>Чуть</em> «biroz» degani, "
                       "qolgan ikkitasi esa grammatik xato.</p>",
    },
]


# =====================================================================
# PR-75 — Свой
# =====================================================================

Q_PR75 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Свой</strong> "
                "oʻzbekchada nima?</p>",
        "choices": ["uning", "har bir", "shu", "oʻz"],
        "correct": "oʻz",
        "explanation": "<p><em>Он взял <strong>свою́</strong> кни́гу</em> = «U "
                       "<strong>oʻz</strong> kitobini oldi». Oʻzbekchada bu "
                       "farq bor, ingliz tilida esa umuman yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Свой</strong> kimga "
                "tegishli narsani bildiradi?</p>",
        "choices": ["Gapning egasiga", "Gapning toʻldiruvchisiga",
                    "Soʻzlovchiga", "Tinglovchiga"],
        "correct": "Gapning egasiga",
        "explanation": "<p>Shuning uchun u gapning egasi boʻla olmaydi — kimga "
                       "qarashi qolmaydi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он взял свою́ "
                "кни́гу. · Он взял его́ кни́гу.</strong></p>",
        "choices": ["Farqi yoʻq",
                    "Birinchisi koʻplik",
                    "Ikkinchisi savol gap",
                    "Birinchisida kitob oʻzining, ikkinchisida boshqa odamning"],
        "correct": "Birinchisida kitob oʻzining, ikkinchisida boshqa odamning",
        "explanation": "<p>Bitta soʻz butun voqeani oʻzgartiradi. Ikkinchi "
                       "gapda u begona kitobni olib ketgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Свой</strong> qanday "
                "turlanadi?</p>",
        "choices": ["Мой kabi", "Э́тот kabi", "Umuman turlanmaydi", "Себя́ kabi"],
        "correct": "Мой kabi",
        "explanation": "<p><em>свой, своя́, своё, свои́, своего́, свое́й, "
                       "свои́м…</em> — <em>мой</em> bilan bir xil "
                       "namunada.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он взял свою́ кни́гу.", "Свой брат прие́хал.",
                    "Она́ лю́бит свою́ рабо́ту.", "Мы горди́мся свои́м го́родом."],
        "correct": "Свой брат прие́хал.",
        "explanation": "<p><strong>Свой ega boʻla olmaydi.</strong> Toʻgʻrisi — "
                       "<em>Мой брат прие́хал</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д потеря́л "
                "___ ключи́.</strong> (oʻzinikini)</p>",
        "choices": ["его́", "их", "свой", "свои́"],
        "correct": "свои́",
        "explanation": "<p>Kalitlar Bekzodniki, u esa gapning egasi — demak "
                       "<strong>свои́</strong> (koʻplik). <em>Его́ ключи́</em> "
                       "boshqa odamning kalitlari boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он помога́ет ___ "
                "роди́телям.</strong> (свой)</p>",
        "choices": ["свои́", "свои́х", "свои́м", "свои́ми"],
        "correct": "свои́м",
        "explanation": "<p><em>Помога́ть <strong>кому́?</strong></em> — "
                       "Да́тельный, koʻplik: <strong>свои́м</strong>. "
                       "<em>Свой</em> ham xuddi sifat kabi turlanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ горди́тся ___ "
                "до́черью.</strong> (свой)</p>",
        "choices": ["свое́й", "свою́", "своя́", "своего́"],
        "correct": "свое́й",
        "explanation": "<p><em>Горди́ться</em> <strong>Твори́тельный</strong> "
                       "talab qiladi (PR-40), <em>дочь</em> esa ayol jinsida: "
                       "<strong>свое́й</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он рассказа́л о ___ "
                "рабо́те.</strong> (oʻzining ishi haqida)</p>",
        "choices": ["его́", "свою́", "свое́й", "свой"],
        "correct": "свое́й",
        "explanation": "<p>Предло́жный, ayol jinsi — <strong>свое́й</strong>. "
                       "<em>О его́ рабо́те</em> deyilsa, boshqa odamning ishi "
                       "haqida gapirgan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У них тепе́рь ___ "
                "дом.</strong> (ijara emas, oʻziniki)</p>",
        "choices": ["их", "свои́", "своё", "свой"],
        "correct": "свой",
        "explanation": "<p><em>Свой</em> ning ikkinchi maʼnosi — "
                       "«<strong>oʻziniki, ijara emas</strong>». <em>Дом</em> "
                       "erkak jinsida, И.п.: <strong>свой</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi shaxsda "
                "<strong>свой</strong> MAJBURIY?</p>",
        "choices": ["я va ты", "мы va вы", "он, она́, они́", "Hamma shaxsda"],
        "correct": "он, она́, они́",
        "explanation": "<p>1- va 2-shaxsda <em>мой/свой</em> ikkalasi ham "
                       "toʻgʻri. 3-shaxsda esa <em>его́/её/их</em> "
                       "<strong>boshqa odamni</strong> koʻrsatadi, shuning "
                       "uchun <em>свой</em> dan boshqa yoʻl yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне нра́вится ___ "
                "рабо́та.</strong></p>",
        "choices": ["своя́", "свое́й", "моя́", "свой"],
        "correct": "моя́",
        "explanation": "<p>Bu gapda ega — <em>рабо́та</em> ning oʻzi, odam esa "
                       "Да́тельный da turibdi. <em>Свой</em> egaga qarashi "
                       "kerak edi, shuning uchun bu yerda "
                       "<strong>моя́</strong> qoʻyiladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>По-сво́ему</strong> "
                "nimani bildiradi?</p>",
        "choices": ["oʻz vaqtida", "oʻzicha", "oʻz-oʻzidan", "oʻz odami"],
        "correct": "oʻzicha",
        "explanation": "<p><em>Он всё де́лает <strong>по-сво́ему</strong></em> — "
                       "«hammasini oʻzicha qiladi». <em>В своё вре́мя</em> — "
                       "«oʻz vaqtida».</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>его́</strong> toʻgʻri?</p>",
        "choices": ["Оле́г взял ___ маши́ну и уе́хал домо́й. (oʻzinikini)",
                    "Оле́г лю́бит ___ рабо́ту. (oʻzinikini)",
                    "Оле́г взял ___ маши́ну без спро́са. (Dmitriynikini)",
                    "Оле́г потеря́л ___ ключи́. (oʻzinikini)"],
        "correct": "Оле́г взял ___ маши́ну без спро́са. (Dmitriynikini)",
        "explanation": "<p>Faqat shu gapda narsa <strong>boshqa odamniki</strong>. "
                       "Qolgan uchtasida egasi Olegning oʻzi, demak "
                       "<em>свой</em> kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <strong>свой</strong> "
                "3-shaxsda ayniqsa muhim?</p>",
        "choices": ["Chunki u qisqaroq",
                    "Chunki «его́/её/их» boshqa odamni bildiradi",
                    "Chunki u yozma tilda ishlatiladi",
                    "Chunki u koʻplikda turadi"],
        "correct": "Chunki «его́/её/их» boshqa odamni bildiradi",
        "explanation": "<p>1-shaxsda chalkashlik boʻlmaydi: <em>я взял мою́ "
                       "кни́гу</em> baribir menikini bildiradi. 3-shaxsda esa "
                       "maʼno butunlay oʻzgaradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>У меня́ своя́ "
                "ко́мната</strong> nimani taʼkidlaydi?</p>",
        "choices": ["Xona kichkina", "Xona chiroyli",
                    "Xona ijaraga olingan", "Xona faqat meniki — boshqa bilan boʻlishilmaydi"],
        "correct": "Xona faqat meniki — boshqa bilan boʻlishilmaydi",
        "explanation": "<p><em>Свой</em> bu yerda «<strong>oʻziniki</strong>, "
                       "begona emas, boʻlishilmaydi» degan maʼnoni beradi. "
                       "<em>Моя́ ко́мната</em> deyilsa, bu taʼkid "
                       "yoʻqoladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Она́ забы́ла свою́ су́мку.", "Он помога́ет свои́ роди́телям.",
                    "Мы горди́мся свои́м го́родом.", "Я взял свою́ кни́гу."],
        "correct": "Он помога́ет свои́ роди́телям.",
        "explanation": "<p><s>свои́</s> → <strong>свои́м</strong>. "
                       "<em>Помога́ть</em> Да́тельный talab qiladi, "
                       "<em>свой</em> esa turlanishi kerak.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Свои́ друзья́ пришли́ ко мне.", "Мои́ друзья́ пришли́ ко мне.",
                    "Свой друзья́ пришли́ ко мне.", "Свое́й друзья́ пришли́ ко мне."],
        "correct": "Мои́ друзья́ пришли́ ко мне.",
        "explanation": "<p>Bu yerda soʻz gapning <strong>egasi</strong> oʻrnida "
                       "turibdi, <em>свой</em> esa ega boʻla olmaydi. "
                       "Demak <strong>мои́</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Вы всё ещё снима́ете "
                "кварти́ру?</strong></p>",
        "choices": ["— Нет, у нас тепе́рь свой дом.", "— Нет, у нас тепе́рь их дом.",
                    "— Нет, у нас тепе́рь свои́ дом.", "— Нет, у нас тепе́рь наш свой дом."],
        "correct": "— Нет, у нас тепе́рь свой дом.",
        "explanation": "<p>Savol ijara haqida, javob esa «endi oʻz uyimiz bor» "
                       "degani — bu aynan <strong>свой</strong> ning ikkinchi "
                       "maʼnosi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Dilnoza oʻz "
                "ishi haqida gapirdi.</strong></p>",
        "choices": ["Дилно́за рассказа́ла о её рабо́те.",
                    "Дилно́за рассказа́ла о свою́ рабо́ту.",
                    "Дилно́за рассказа́ла о свое́й рабо́те.",
                    "Дилно́за рассказа́ла о свой рабо́те."],
        "correct": "Дилно́за рассказа́ла о свое́й рабо́те.",
        "explanation": "<p>Oʻzbekcha «oʻz» → <strong>свой</strong>, "
                       "Предло́жный va ayol jinsi → <strong>свое́й</strong>. "
                       "<em>О её рабо́те</em> boshqa ayolning ishi boʻlardi.</p>",
    },
]


# =====================================================================
# PR-76 — Себя va сам
# =====================================================================

Q_PR76 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Себя́</strong> ning "
                "qaysi kelishigi YOʻQ?</p>",
        "choices": ["Да́тельный", "Твори́тельный", "Предло́жный", "Имени́тельный"],
        "correct": "Имени́тельный",
        "explanation": "<p><strong>Себя́</strong> hech qachon gapning egasi "
                       "boʻlmaydi — u har doim egaga qaytadi. Shakllar: "
                       "<em>себя́, себе́, себя́, собо́й, о себе́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Себя́</strong> bilan "
                "<strong>сам</strong> ning farqi nimada?</p>",
        "choices": ["Себя́ — toʻldiruvchi, сам — taʼkid",
                    "Себя́ — yozma, сам — ogʻzaki",
                    "Себя́ — koʻplik, сам — birlik",
                    "Farqi yoʻq"],
        "correct": "Себя́ — toʻldiruvchi, сам — taʼkid",
        "explanation": "<p><em>Купи́л <strong>себе́</strong></em> — kimga? "
                       "<em><strong>Сам</strong> купи́л</em> — kim? Oʻzbekchada "
                       "ikkalasi ham «oʻzim», ruschada esa ikki soʻz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я купи́л ___ "
                "кни́гу.</strong> (oʻzimga)</p>",
        "choices": ["мне", "себя́", "собо́й", "себе́"],
        "correct": "себе́",
        "explanation": "<p>Ega bilan bir odam boʻlgani uchun "
                       "<strong>себе́</strong> — Да́тельный. <s>Купи́л "
                       "мне</s> bunday holatda ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus tilida <strong>себе́</strong> "
                "nechta shaxs uchun ishlaydi?</p>",
        "choices": ["Faqat «я» uchun", "Faqat 3-shaxs uchun",
                    "Hamma shaxs uchun bitta shakl", "Har shaxsga alohida shakl bor"],
        "correct": "Hamma shaxs uchun bitta shakl",
        "explanation": "<p><em>Я / ты / он / мы купи́л(и) <strong>себе́</strong></em> "
                       "— bitta soʻz. Oʻzbekchada esa toʻrt shakl: "
                       "<em>oʻzimga, oʻzingga, oʻziga, oʻzimizga</em>. Bu "
                       "yerda rus tili osonroq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Eshikda «<strong>От "
                "себя́</strong>» yozilgan. Nima qilasiz?</p>",
        "choices": ["Itarasiz", "Tortasiz", "Yon tomonga surasiz", "Kutasiz"],
        "correct": "Itarasiz",
        "explanation": "<p><em>От себя́</em> — «oʻzingizdan nariga», yaʼni "
                       "itarasiz. <em>К себе́</em> — «oʻzingizga tomon», "
                       "yaʼni tortasiz.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Расскажи́ немно́го "
                "о ___.</strong> (себя́)</p>",
        "choices": ["себе́", "себя́", "собо́й", "сам"],
        "correct": "себе́",
        "explanation": "<p>Предло́жный — <strong>о себе́</strong>. Bu tanishuv "
                       "suhbatining eng koʻp uchraydigan iborasi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Как ты ___ "
                "чу́вствуешь?</strong></p>",
        "choices": ["себе́", "собо́й", "сам", "себя́"],
        "correct": "себя́",
        "explanation": "<p><em>Чу́вствовать <strong>себя́</strong></em> — bu "
                       "ibora Вини́тельный oladi. <s>Как ты себе́ "
                       "чу́вствуешь</s> — koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ ___ "
                "почини́ла кран.</strong> (oʻzi, hech kim yordam bermadi)</p>",
        "choices": ["сам", "себя́", "себе́", "сама́"],
        "correct": "сама́",
        "explanation": "<p>Bu <strong>taʼkid</strong>, demak <em>сам</em> "
                       "oilasi. Ayol jinsida — <strong>сама́</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он недово́лен "
                "___.</strong> (oʻzidan)</p>",
        "choices": ["себя́", "себе́", "собо́й", "сам"],
        "correct": "собо́й",
        "explanation": "<p><em>Недово́лен <strong>кем?</strong></em> — "
                       "Твори́тельный, demak <strong>собо́й</strong>. "
                       "«Oʻzidan norozi».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Взять себя́ в "
                "ру́ки</strong> nimani bildiradi?</p>",
        "choices": ["Yordam soʻramoq", "Qoʻlini yuvmoq",
                    "Oʻzini qoʻlga olmoq", "Ketmoq"],
        "correct": "Oʻzini qoʻlga olmoq",
        "explanation": "<p>Oʻzbekchaga soʻzma-soʻz tushadi. Qarama-qarshisi — "
                       "<em>вы́йти из себя́</em>, «jahli chiqmoq».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дире́ктор у "
                "себя́</strong> nimani bildiradi?</p>",
        "choices": ["Direktor uyda", "Direktor oʻz xonasida",
                    "Direktor kasal", "Direktor ketdi"],
        "correct": "Direktor oʻz xonasida",
        "explanation": "<p><em>У себя́</em> — «oʻz joyida, oʻz xonasida». "
                       "Idorada bu ibora har kuni eshitiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дверь откры́лась "
                "___.</strong> (oʻz-oʻzidan)</p>",
        "choices": ["себе́", "себя́", "сам", "сама́ собо́й"],
        "correct": "сама́ собо́й",
        "explanation": "<p><em>Сам собо́й / сама́ собо́й / само́ собо́й</em> — "
                       "«oʻz-oʻzidan». <em>Дверь</em> ayol jinsida, shuning "
                       "uchun <strong>сама́ собо́й</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он купи́л себе́ "
                "телефо́н. · Он сам купи́л телефо́н.</strong></p>",
        "choices": ["Birinchisi — kimga oldi, ikkinchisi — kim oldi",
                    "Farqi yoʻq",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisida xato bor"],
        "correct": "Birinchisi — kimga oldi, ikkinchisi — kim oldi",
        "explanation": "<p><em>Себе́</em> «oʻziga» degan "
                       "<strong>toʻldiruvchi</strong>, <em>сам</em> esa «hech "
                       "kim yordam bermadi» degan <strong>taʼkid</strong>. "
                       "Bir gapda ikkalasi ham boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Сам</strong> bilan "
                "<strong>са́мый</strong> ning farqi nimada?</p>",
        "choices": ["Сам — «oʻzi», са́мый — «eng»",
                    "Сам — erkak, са́мый — ayol",
                    "Сам — ogʻzaki, са́мый — yozma",
                    "Farqi yoʻq"],
        "correct": "Сам — «oʻzi», са́мый — «eng»",
        "explanation": "<p><em>Дире́ктор <strong>сам</strong> пришёл</em> — "
                       "direktorning oʻzi keldi. <em><strong>Са́мый</strong> "
                       "большо́й дом</em> — eng katta uy (PR-74).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Он мо́ется</strong> "
                "va <strong>он уви́дел себя́ в зе́ркале</strong> — nega "
                "ikki xil?</p>",
        "choices": ["Birinchisi kelasi zamon",
                    "Ikkinchisida xato bor",
                    "Birinchisi — odatiy ish (-ся), ikkinchisi — alohida obyekt (себя́)",
                    "Farqi faqat uslubda"],
        "correct": "Birinchisi — odatiy ish (-ся), ikkinchisi — alohida obyekt (себя́)",
        "explanation": "<p>Har kungi oddiy ish uchun <strong>-ся</strong> "
                       "yetarli (PR-62). Aynan «oʻzini» taʼkidlash kerak "
                       "boʻlsa — alohida soʻz <strong>себя́</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Чита́й про "
                "себя́</strong> nimani bildiradi?</p>",
        "choices": ["Oʻzing haqingda oʻqi", "Ichingda oʻqi, ovoz chiqarma",
                    "Sekin oʻqi", "Yana bir marta oʻqi"],
        "correct": "Ichingda oʻqi, ovoz chiqarma",
        "explanation": "<p><em>Про себя́</em> — «ichida, ovozsiz». «Oʻzing "
                       "haqingda» esa <em>о себе́</em> boʻlardi — predlog "
                       "oʻzgarishi bilan maʼno butunlay oʻzgaradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я купи́л себе́ кни́гу.", "Как ты себе́ чу́вствуешь?",
                    "Расскажи́ о себе́.", "Он недово́лен собо́й."],
        "correct": "Как ты себе́ чу́вствуешь?",
        "explanation": "<p><s>себе́</s> → <strong>себя́</strong>. "
                       "<em>Чу́вствовать себя́</em> Вини́тельный oladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Она́ сам пришла́.", "Себя пришла́ она́.",
                    "Она́ сама́ пришла́.", "Она́ себе́ пришла́."],
        "correct": "Она́ сама́ пришла́.",
        "explanation": "<p><em>Сам</em> jinsga moslashadi — ayol uchun "
                       "<strong>сама́</strong>. <em>Себя́</em> esa ega boʻla "
                       "olmaydi, chunki uning Имени́тельный shakli yoʻq.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Кто тебе́ помо́г с "
                "ремо́нтом?</strong></p>",
        "choices": ["— Никто́, я себя́ сде́лал.", "— Никто́, я сам всё сде́лал.",
                    "— Никто́, я себе́ сде́лал всё.", "— Никто́, я са́мый сде́лал."],
        "correct": "— Никто́, я сам всё сде́лал.",
        "explanation": "<p>Savol «kim?» haqida, javob ham taʼkid — demak "
                       "<strong>сам</strong>. <em>Себя́/себе́</em> bu yerda "
                       "«kimni? kimga?» degan boshqa savolga javob "
                       "berardi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Oʻzingizni "
                "qoʻlga oling va oʻzingiz hal qiling.</strong></p>",
        "choices": ["Возьми́те сами́ в ру́ки и реши́те себя́.",
                    "Возьми́те себе́ в ру́ки и реши́те са́ми.",
                    "Возьми́те себя́ в ру́ки и реши́те себе́.",
                    "Возьми́те себя́ в ру́ки и реши́те са́ми."],
        "correct": "Возьми́те себя́ в ру́ки и реши́те са́ми.",
        "explanation": "<p>Birinchi qismda <strong>себя́</strong> — "
                       "toʻldiruvchi («kimni?»), ikkinchisida "
                       "<strong>са́ми</strong> — taʼkid («kim?»). Bitta gapda "
                       "ikkala soʻz ham oʻz oʻrnida.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-74 Mashq: Sifat darajalari",
        "description": (
            "Интере́снее, доро́же, лу́чше. Ikki xil solishtirish — чем va "
            "Роди́тельный (oʻzbekcha «-dan»), hamda са́мый = «eng»."
        ),
        "tutorial": "PR-74:",
        "questions": Q_PR74,
    },
    {
        "title": "PR-75 Mashq: Свой — «oʻz» olmoshi",
        "description": (
            "Oʻzbekcha «oʻz» ruschada «свой». Gapning egasiga tegishli narsa, "
            "3-shaxsda majburiy, va u hech qachon ega boʻlmaydi."
        ),
        "tutorial": "PR-75:",
        "questions": Q_PR75,
    },
    {
        "title": "PR-76 Mashq: Себя va сам",
        "description": (
            "Себя́ — toʻldiruvchi, сам — taʼkid. Beshta shakl hamma shaxs uchun, "
            "plus чу́вствовать себя́, у себя́, к себе́ / от себя́."
        ),
        "tutorial": "PR-76:",
        "questions": Q_PR76,
    },
]
