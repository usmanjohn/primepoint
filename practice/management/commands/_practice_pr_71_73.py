# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-71 … PR-73.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_71_73.py --master=prime \\
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
# PR-71 — Страдательные причастия
# =====================================================================

Q_PR71 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Страда́тельное "
                "прича́стие</strong> nimani bildiradi?</p>",
        "choices": ["Ot ishni oʻzi qiladi", "Ish ot ustida bajariladi",
                    "Ish hali boshlanmagan", "Ish takrorlanadi"],
        "correct": "Ish ot ustida bajariladi",
        "explanation": "<p><em>кни́га, прочи́танная студе́нтом</em> — kitobni "
                       "oʻqishdi. Oʻzbekcha <strong>-il-</strong> qoʻshimchasi "
                       "kabi: «oʻqi<strong>l</strong>gan kitob».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qisqa shaklda nechta "
                "<strong>Н</strong> yoziladi?</p>",
        "choices": ["Ikkita", "Bitta", "Uchta", "Jinsga qarab"],
        "correct": "Bitta",
        "explanation": "<p><em>прочи́та<strong>нн</strong>ая кни́га</em> → "
                       "<em>кни́га прочи́та<strong>н</strong>а</em>. Toʻliqda "
                       "ikkita, qisqada bitta — bu rus imlosining eng koʻp "
                       "tekshiriladigan qoidalaridan biri.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дом ___ в 1980 "
                "году́.</strong> (постро́ить)</p>",
        "choices": ["постро́енный", "постро́ена", "постро́ен", "постро́ить"],
        "correct": "постро́ен",
        "explanation": "<p>Bu yerda <strong>kesim</strong> kerak, demak qisqa "
                       "shakl. <em>Дом</em> — erkak jinsida, shuning uchun "
                       "<em>постро́ен</em>. Bu PR-61 dagi majhul nisbatning "
                       "oʻzi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>«Kim tomonidan» degan maʼno "
                "qaysi kelishik bilan beriladi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Предло́жный", "Твори́тельный"],
        "correct": "Твори́тельный",
        "explanation": "<p><em>кни́га, напи́санная <strong>Толсты́м</strong></em> "
                       "— «Tolstoy tomonidan yozilgan kitob». Predlog "
                       "qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Закры́тая дверь</strong> "
                "va <strong>дверь закры́та</strong> — farqi nimada?</p>",
        "choices": ["Farqi yoʻq", "Birinchisi koʻplik", "Ikkinchisi savol gap",
                    "Birinchisi aniqlovchi, ikkinchisi kesim"],
        "correct": "Birinchisi aniqlovchi, ikkinchisi kesim",
        "explanation": "<p>Toʻliq shakl otni <strong>aniqlaydi</strong> "
                       "(«qanday eshik?»), qisqa shakl esa gapning "
                       "<strong>kesimi</strong> boʻladi («eshik nima "
                       "boʻldi?»).</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻliq shaklni yasang.</p><p><strong>написа́ть</strong></p>",
        "choices": ["напи́шенный", "напи́санный", "написа́нный", "напи́сатый"],
        "correct": "напи́санный",
        "explanation": "<p><em>-ать</em> bilan tugagani uchun "
                       "<strong>-анн-</strong>. Diqqat: urgʻu bir boʻgʻin "
                       "orqaga qaytadi — <em>напис<strong>а́</strong>ть</em> → "
                       "<em>нап<strong>и́</strong>санный</em>.</p>",
    },
    {
        "text": "<p>Toʻliq shaklni yasang.</p><p><strong>закры́ть</strong></p>",
        "choices": ["закры́тый", "закры́нный", "закро́енный", "закры́вший"],
        "correct": "закры́тый",
        "explanation": "<p><em>-ыть</em> bilan tugaydigan feʼllar "
                       "<strong>-т-</strong> oladi: <em>закры́тый, забы́тый, "
                       "откры́тый</em>. <em>Закры́вший</em> — действительное "
                       "prichastiye (PR-70).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Все зада́чи уже́ "
                "___.</strong> (реши́ть)</p>",
        "choices": ["решены́", "решённые", "решена́", "решён"],
        "correct": "решены́",
        "explanation": "<p><em>Зада́чи</em> — koʻplik, demak qisqa shaklning "
                       "<strong>-ы</strong> varianti. <em>Решённые</em> toʻliq "
                       "shakl boʻlardi, lekin bu yerda kesim kerak.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́та пе́сня "
                "напи́сана ___.</strong> (молодо́й компози́тор)</p>",
        "choices": ["молодо́го компози́тора", "молодо́му компози́тору",
                    "молоды́м компози́тором", "молодо́й компози́тор"],
        "correct": "молоды́м компози́тором",
        "explanation": "<p>«Kim tomonidan» — <strong>Твори́тельный</strong>. "
                       "Sifat ham otga moslashadi: <em>молоды́м "
                       "компози́тором</em>.</p>",
    },
    {
        "text": "<p>Nechta <strong>Н</strong>?</p><p><strong>Пи́сьма уже́ "
                "напи́са__ы.</strong></p>",
        "choices": ["напи́саны — bitta", "напи́санны — ikkita",
                    "напи́саннны — uchta", "Farqi yoʻq"],
        "correct": "напи́саны — bitta",
        "explanation": "<p>Bu qisqa shakl (kesim), demak <strong>bitta "
                       "Н</strong>. Toʻliq shaklda ikkita boʻlardi: "
                       "<em>напи́са<strong>нн</strong>ые пи́сьма</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́дел дверь, ___ "
                "на ключ.</strong> (закры́ть)</p>",
        "choices": ["закры́тый", "закры́та", "закры́тую", "закры́тым"],
        "correct": "закры́тую",
        "explanation": "<p>Sifatdosh <em>дверь</em> ga moslashadi, u esa "
                       "<strong>Вини́тельный</strong> da (<em>ви́дел что?</em>) va "
                       "ayol jinsida: <em>закры́тую</em>.</p>",
    },
    {
        "text": "<p>Qaysi feʼldan страда́тельное прича́стие yasab "
                "boʻlmaydi?</p>",
        "choices": ["прочита́ть", "постро́ить", "идти́", "закры́ть"],
        "correct": "идти́",
        "explanation": "<p><em>Идти́</em> obyekt olmaydi — «kimni? nimani?» degan "
                       "savol berib boʻlmaydi. Shuning uchun <s>идённый</s> "
                       "degan soʻz yoʻq. Majhul sifatdosh faqat obyekt "
                       "oladigan feʼllardan yasaladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu ikkisining farqi nimada?</p>"
                "<p><strong>студе́нт, прочита́вший кни́гу · кни́га, прочи́танная "
                "студе́нтом</strong></p>",
        "choices": ["Birinchisida talaba oʻqidi, ikkinchisida kitob oʻqildi",
                    "Ikkalasi bir xil",
                    "Birinchisi kelasi zamon",
                    "Ikkinchisida xato bor"],
        "correct": "Birinchisida talaba oʻqidi, ikkinchisida kitob oʻqildi",
        "explanation": "<p>Birinchisi — <strong>действительное</strong> (ot ishni "
                       "oʻzi qiladi), ikkinchisi — <strong>страдательное</strong> "
                       "(ish ot ustida bajariladi). Oʻzbekcha «oʻqigan» ↔ "
                       "«oʻqilgan».</p>",
    },
    {
        "text": "<p>Qaysi gapda qisqa shakl kerak?</p>",
        "choices": ["___ дверь никто́ не тро́гал.", "Он вошёл в ___ ко́мнату.",
                    "Мы нашли́ ___ письмо́.", "Магази́н ___ до девяти́."],
        "correct": "Магази́н ___ до девяти́.",
        "explanation": "<p>Faqat bu gapda boʻsh joy <strong>kesim</strong> "
                       "oʻrnida turibdi: <em>Магази́н <strong>закры́т</strong> до "
                       "девяти́</em>. Qolganlarida sifatdosh otni aniqlaydi, "
                       "demak toʻliq shakl kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дом стро́ится</strong> "
                "va <strong>дом постро́ен</strong> — farqi nimada?</p>",
        "choices": ["Birinchisi jarayon, ikkinchisi natija",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi savol gap",
                    "Farqi faqat uslubda"],
        "correct": "Birinchisi jarayon, ikkinchisi natija",
        "explanation": "<p>Bu PR-61 dagi majhul nisbat. <em>Стро́ится</em> — hozir "
                       "qurilyapti (jarayon), <em>постро́ен</em> — qurib "
                       "boʻlingan (natija, qisqa sifatdosh).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sifatdosh oborotdan oldin va "
                "keyin vergul qachon qoʻyiladi?</p>",
        "choices": ["Har doim", "Hech qachon", "Oborot otdan keyin turganda",
                    "Oborot otdan oldin turganda"],
        "correct": "Oborot otdan keyin turganda",
        "explanation": "<p><em>Кни́га<strong>,</strong> напи́санная в "
                       "тюрьме́<strong>,</strong> ста́ла знамени́той.</em> Otdan "
                       "oldin tursa (oʻzbekcha tartib) — vergul "
                       "qoʻyilmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Дом постро́ен в 1980 году́.",
                    "Пи́сьма напи́санны.",
                    "Все зада́чи решены́.",
                    "Магази́н закры́т."],
        "correct": "Пи́сьма напи́санны.",
        "explanation": "<p><s>напи́санны</s> → <strong>напи́саны</strong>. Qisqa "
                       "shaklda har doim <strong>bitta Н</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Кни́га, напи́санная Толсто́го.", "Кни́га, напи́санная Толсто́му.",
                    "Кни́га, напи́санная Толсты́м.", "Кни́га, напи́санная о Толсто́м."],
        "correct": "Кни́га, напи́санная Толсты́м.",
        "explanation": "<p>«Kim tomonidan» — <strong>Твори́тельный</strong>, "
                       "predlogsiz. <em>О Толсто́м</em> «Tolstoy haqida» degan "
                       "butunlay boshqa maʼno berardi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Мо́жно войти́ в "
                "библиоте́ку?</strong></p>",
        "choices": ["— Нет, она́ закры́тая до девяти́.",
                    "— Нет, она́ закры́та до девяти́.",
                    "— Нет, она́ закры́тую до девяти́.",
                    "— Нет, она́ закры́той до девяти́."],
        "correct": "— Нет, она́ закры́та до девяти́.",
        "explanation": "<p>Bu yerda kesim kerak — «yopiq (holatda)». Demak qisqa "
                       "shakl, ayol jinsida: <strong>закры́та</strong>.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Qamoqda "
                "yozilgan kitob koʻp tillarga tarjima qilingan.</strong></p>",
        "choices": ["Кни́га, написа́вшая в тюрьме́, переведена́ на мно́гие языки́.",
                    "Кни́га, напи́санная в тюрьме́, переводи́т на мно́гие языки́.",
                    "Кни́га, напи́санная в тюрьме́, переведена́ на мно́гие языки́.",
                    "Кни́га, напи́санной в тюрьме́, переведена́ на мно́гие языки́."],
        "correct": "Кни́га, напи́санная в тюрьме́, переведена́ на мно́гие языки́.",
        "explanation": "<p>Birinchi qism — toʻliq shakl (aniqlovchi, ikki tomondan "
                       "vergul), ikkinchisi — qisqa shakl (kesim). "
                       "<em>Написа́вшая</em> «kitob yozgan» degan notoʻgʻri "
                       "maʼno berardi.</p>",
    },
]


# =====================================================================
# PR-72 — Деепричастие
# =====================================================================

Q_PR72 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Дееприча́стие</strong> "
                "oʻzbekchada nimaga toʻgʻri keladi?</p>",
        "choices": ["Sifatdosh: -gan, -ayotgan", "Ravishdosh: -ib, -gach",
                    "Kelishik qoʻshimchasi", "Buyruq mayli"],
        "correct": "Ravishdosh: -ib, -gach",
        "explanation": "<p><em>чита́я</em> = «oʻqib», <em>прочита́в</em> = «oʻqib "
                       "boʻlgach». Sifatdosh (<em>-gan</em>) — bu "
                       "<strong>причастие</strong>, PR-70.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ravishdosh qanday "
                "oʻzgaradi?</p>",
        "choices": ["Jins boʻyicha", "Kelishik boʻyicha", "Son boʻyicha",
                    "Hech qanday — u oʻzgarmaydi"],
        "correct": "Hech qanday — u oʻzgarmaydi",
        "explanation": "<p>Причастие sifat kabi moslashadi "
                       "(<em>чита́ющий, чита́ющая, чита́ющего</em>), "
                       "деепричастие esa <strong>hech qachon</strong> "
                       "oʻzgarmaydi: <em>чита́я</em> — har doim "
                       "<em>чита́я</em>.</p>",
    },
    {
        "text": "<p>Ravishdosh yasang.</p><p><strong>рабо́тать</strong> (НСВ)</p>",
        "choices": ["рабо́тав", "рабо́тающи", "рабо́тая", "рабо́тавши"],
        "correct": "рабо́тая",
        "explanation": "<p>НСВ feʼli <strong>-я</strong> oladi. «Они́» shakli "
                       "<em>рабо́таю[т]</em>, qoʻshimcha olib tashlanadi: "
                       "<em>рабо́тая</em> — «ishlab, ishlayotib».</p>",
    },
    {
        "text": "<p>Ravishdosh yasang.</p><p><strong>прочита́ть</strong> (СВ)</p>",
        "choices": ["прочита́я", "прочита́вши", "прочита́вший", "прочита́в"],
        "correct": "прочита́в",
        "explanation": "<p>СВ feʼli <strong>-в</strong> oladi: «oʻqib boʻlgach». "
                       "<em>Прочита́вши</em> — eskirgan shakl, "
                       "<em>прочита́вший</em> esa причастие (PR-70).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ravishdosh oborot vergul bilan "
                "qachon ajratiladi?</p>",
        "choices": ["Faqat gap boshida", "Faqat gap oxirida",
                    "Har doim, oʻrnidan qatʼi nazar", "Hech qachon"],
        "correct": "Har doim, oʻrnidan qatʼi nazar",
        "explanation": "<p>Bu причастие dan osonroq: u yerda vergul oʻringa "
                       "bogʻliq edi, bu yerda esa <strong>har doim</strong> "
                       "qoʻyiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Ravishdosh yasang.</p><p><strong>верну́ться</strong> (СВ)</p>",
        "choices": ["верну́в", "верну́вши", "верну́вшись", "возвраща́ясь"],
        "correct": "верну́вшись",
        "explanation": "<p><em>-ся</em> feʼllari <strong>-вшись</strong> oladi. "
                       "<em>Возвраща́ясь</em> — НСВ shakli («qaytayotib»), bu "
                       "esa СВ («qaytgach»).</p>",
    },
    {
        "text": "<p>Ravishdosh yasang.</p><p><strong>вы́йти</strong> (СВ)</p>",
        "choices": ["вы́шедши", "вы́шев", "выходя́", "вы́йдя"],
        "correct": "вы́йдя",
        "explanation": "<p>Harakat feʼllarining bir qismi СВ boʻlsa ham "
                       "<strong>-я</strong> oladi: <em>вы́йти → вы́йдя</em>, "
                       "<em>прийти́ → придя́</em>, <em>принести́ → "
                       "принеся́</em>. Bularni yodlash kerak.</p>",
    },
    {
        "text": "<p><strong>Чита́я</strong> yoki <strong>прочита́в</strong>?</p>"
                "<p><strong>___ письмо́, он сра́зу позвони́л сестре́.</strong></p>",
        "choices": ["Чита́я", "Чита́вши", "Прочи́тав", "Прочита́в"],
        "correct": "Прочита́в",
        "explanation": "<p>Avval xat oʻqib boʻlindi, <strong>keyin</strong> "
                       "qoʻngʻiroq qildi — ketma-ketlik, demak СВ. "
                       "<em>Чита́я</em> «oʻqiyotib qoʻngʻiroq qildi» degan "
                       "boshqa manzara berardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ домо́й, я "
                "встре́тил ста́рого дру́га.</strong> (возвраща́ться)</p>",
        "choices": ["Возвраща́вшись", "Возвраща́ясь", "Возвраща́ющий", "Возврати́в"],
        "correct": "Возвраща́ясь",
        "explanation": "<p>«Qaytayotib» — davom etayotgan ish, demak "
                       "<strong>НСВ</strong> va <em>-ясь</em>. Ikkala qismda ham "
                       "ega <em>я</em> — qoida bajarildi.</p>",
    },
    {
        "text": "<p>Qaysi feʼlning <strong>-я</strong> ravishdoshi "
                "yoʻq?</p>",
        "choices": ["чита́ть", "рабо́тать", "говори́ть", "писа́ть"],
        "correct": "писа́ть",
        "explanation": "<p><s>Пиша́</s> degan shakl ishlatilmaydi. Shu guruhda "
                       "yana <em>пить, бить, петь, ждать, спать, есть, "
                       "бежа́ть</em>. Ular oʻrniga <em>когда́ я писа́л…</em> "
                       "deyiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega bu gap kulgili?</p>"
                "<p><strong>Подъезжа́я к ста́нции, у меня́ слете́ла "
                "шля́па.</strong></p>",
        "choices": ["Chunki shlyapa stansiyaga yaqinlashib kelyapti",
                    "Chunki «шля́па» ayol jinsida",
                    "Chunki vergul notoʻgʻri qoʻyilgan",
                    "Chunki «подъезжа́я» eskirgan shakl"],
        "correct": "Chunki shlyapa stansiyaga yaqinlashib kelyapti",
        "explanation": "<p>Ravishdoshning egasi asosiy feʼlning egasi bilan bir "
                       "xil boʻlishi shart. Bu yerda ega — <em>шля́па</em>, "
                       "demak shlyapa yaqinlashyapti. Bu Chexovning mashhur "
                       "hazili.</p>",
    },
    {
        "text": "<p>Vergul kerakmi?</p><p><strong>Он ушёл не "
                "попроща́вшись.</strong></p>",
        "choices": ["Yoʻq, kerak emas", "Ha, «ушёл» dan keyin",
                    "Ha, «не» dan keyin", "Ha, gap oxirida"],
        "correct": "Ha, «ушёл» dan keyin",
        "explanation": "<p><em>Он ушёл<strong>,</strong> не попроща́вшись.</em> "
                       "Ravishdosh oborot har doim vergul bilan ajratiladi. "
                       "<em>Не</em> esa ravishdoshdan alohida yoziladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Чита́я письмо́, он "
                "улыба́лся. · Прочита́в письмо́, он улыбну́лся.</strong></p>",
        "choices": ["Birinchisida ikki ish bir vaqtda, ikkinchisida ketma-ket",
                    "Birinchisi kelasi zamon",
                    "Ikkinchisida xato bor",
                    "Farqi faqat uslubda"],
        "correct": "Birinchisida ikki ish bir vaqtda, ikkinchisida ketma-ket",
        "explanation": "<p><strong>-я</strong> (НСВ) — bir vaqtda: oʻqiyotib "
                       "jilmayardi. <strong>-в</strong> (СВ) — avval oʻqidi, "
                       "keyin jilmaydi. Oʻzbekcha «-ib» ikkala maʼnoni ham "
                       "bergani uchun bu yerda ehtiyot boʻlish kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Причастие</strong> "
                "bilan <strong>деепричастие</strong> ning asosiy farqi?</p>",
        "choices": ["Biri hozirgi, ikkinchisi oʻtgan zamon",
                    "Biri sifat (qanday?), ikkinchisi ravish (qachon?)",
                    "Biri НСВ, ikkinchisi СВ",
                    "Biri ogʻzaki, ikkinchisi yozma"],
        "correct": "Biri sifat (qanday?), ikkinchisi ravish (qachon?)",
        "explanation": "<p>Причастие otni aniqlaydi va unga moslashadi. "
                       "Деепричастие feʼlni aniqlaydi va oʻzgarmaydi. Ikkalasida "
                       "ham zamon va vid bor.</p>",
    },
    {
        "text": "<p>Qaysi gapda vergul kerak EMAS?</p>",
        "choices": ["Он рабо́тал не спеша́.", "Прочита́в письмо́ он позвони́л.",
                    "Он ушёл не попроща́вшись.", "Возвраща́ясь домо́й я встре́тил дру́га."],
        "correct": "Он рабо́тал не спеша́.",
        "explanation": "<p><strong>Не спеша́</strong> endi oddiy ravish boʻlib "
                       "qolgan («shoshilmasdan») va vergul olmaydi. Shu guruhda "
                       "yana <em>мо́лча</em>, <em>не дыша́</em>. Qolgan uch "
                       "gapda vergul yetishmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Мо́лча</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Sekin", "Shoshilmasdan", "Jim, indamay", "Nafas olmay"],
        "correct": "Jim, indamay",
        "explanation": "<p><em>Он сиде́л <strong>мо́лча</strong>.</em> — «Jim "
                       "oʻtirdi». Kelib chiqishi ravishdosh "
                       "(<em>молча́ть</em>), lekin endi oddiy ravish — vergul "
                       "olmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Возвраща́ясь домо́й, я попа́л под дождь.",
                    "Прочита́в письмо́, он позвони́л.",
                    "Чита́я кни́гу, мне ста́ло гру́стно.",
                    "Уви́дев нас, она́ улыбну́лась."],
        "correct": "Чита́я кни́гу, мне ста́ло гру́стно.",
        "explanation": "<p>Gapda ega yoʻq — <em>мне</em> Да́тельный da turibdi. "
                       "Toʻgʻrisi: <em>Чита́я кни́гу, <strong>я "
                       "загрусти́л</strong>.</em> Ravishdoshning egasi asosiy "
                       "feʼlning egasi bilan bir xil boʻlishi shart.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Верну́вши домо́й, я поу́жинал.", "Верну́в домо́й, я поу́жинал.",
                    "Верну́вшись домо́й, я поу́жинал.", "Верну́вшийся домо́й, я поу́жинал."],
        "correct": "Верну́вшись домо́й, я поу́жинал.",
        "explanation": "<p><em>Верну́ться</em> — <em>-ся</em> feʼli, demak "
                       "<strong>-вшись</strong>. <em>Верну́вшийся</em> esa "
                       "причастие — u otni aniqlashi kerak edi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni ravishdosh bilan qisqartiring.</p><p><strong>Когда́ "
                "он уви́дел нас, он останови́лся.</strong></p>",
        "choices": ["Ви́дя нас, он останови́лся.", "Уви́дев нас, он останови́лся.",
                    "Уви́девши нас, он останови́лся.", "Уви́девший нас, он останови́лся."],
        "correct": "Уви́дев нас, он останови́лся.",
        "explanation": "<p><em>Уви́дел</em> — СВ, demak <strong>уви́дев</strong>. "
                       "Ikkala qismda ham ega <em>он</em> — qoida bajarildi. "
                       "<em>Ви́дя</em> НСВ boʻlardi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Manzilni "
                "bilmagani uchun uyni uzoq qidirdi.</strong></p>",
        "choices": ["Не зна́я а́дреса, он до́лго иска́л дом.",
                    "Незна́я а́дреса, он до́лго иска́л дом.",
                    "Не знав а́дреса, он до́лго иска́л дом.",
                    "Не зна́я а́дрес, он до́лго иска́л дом."],
        "correct": "Не зна́я а́дреса, он до́лго иска́л дом.",
        "explanation": "<p><em>Не</em> alohida yoziladi. <em>Знать</em> — НСВ, "
                       "demak <strong>зна́я</strong>. Inkor gapda obyekt "
                       "Роди́тельный ga oʻtadi: <em>не зна́я "
                       "а́дрес<strong>а</strong></em>.</p>",
    },
]


# =====================================================================
# PR-73 — Sifatning qisqa shakli
# =====================================================================

Q_PR73 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qisqa sifat gapda qanday "
                "vazifa bajaradi?</p>",
        "choices": ["Aniqlovchi", "Toʻldiruvchi", "Hol", "Kesim"],
        "correct": "Kesim",
        "explanation": "<p><em>дом краси́в</em> — «uy chiroyli». Qisqa sifat "
                       "otdan oldin <strong>hech qachon</strong> turmaydi: "
                       "<s>краси́в дом</s> deyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Ра́дый»</strong> "
                "soʻzi haqida nima toʻgʻri?</p>",
        "choices": ["Bunday soʻz rus tilida yoʻq", "U eskirgan soʻz",
                    "U faqat koʻplikda ishlatiladi", "U «рад» ning ayol shakli"],
        "correct": "Bunday soʻz rus tilida yoʻq",
        "explanation": "<p><strong>Рад</strong> ning toʻliq shakli umuman mavjud "
                       "emas — faqat <em>рад, ра́да, ра́ды</em>. Bu "
                       "<em>смея́ться</em> (PR-62) kabi bir tomonlama "
                       "soʻz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ "
                "по́мощь.</strong> (ну́жный)</p>",
        "choices": ["ну́жен", "ну́жно", "нужна́", "нужны́"],
        "correct": "нужна́",
        "explanation": "<p><em>По́мощь</em> — ayol jinsida (yumshoq belgi bilan "
                       "tugagan ot). <strong>Ну́жен</strong> kerak boʻlgan "
                       "<strong>narsaga</strong> moslashadi, odamga emas.</p>",
    },
    {
        "text": "<p>Qisqa shaklni yasang.</p><p><strong>у́мный</strong> (erkak)</p>",
        "choices": ["умна́", "умны́", "у́мен", "умён"],
        "correct": "умён",
        "explanation": "<p>Oʻzak <em>умн-</em> ikkita undosh bilan tugagan, "
                       "shuning uchun ular orasiga <strong>-ё-</strong> chiqadi. "
                       "Ayol shaklida u yoʻqoladi: <em>умна́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>До́лжен</strong> "
                "nimaga moslashadi?</p>",
        "choices": ["Ega boʻlgan odamga", "Infinitivga", "Kerak boʻlgan narsaga",
                    "Hech nimaga — oʻzgarmaydi"],
        "correct": "Ega boʻlgan odamga",
        "explanation": "<p><em>Я до́лжен идти́</em> (erkak) · <em>Она́ должна́ "
                       "идти́</em> (ayol) · <em>Мы должны́ идти́</em> "
                       "(koʻplik). <strong>Ну́жен</strong> esa aksincha — "
                       "narsaga moslashadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ "
                "де́ньги.</strong> (ну́жный)</p>",
        "choices": ["ну́жен", "нужны́", "нужна́", "ну́жно"],
        "correct": "нужны́",
        "explanation": "<p><em>Де́ньги</em> — faqat koʻplikda ishlatiladigan ot, "
                       "demak <strong>нужны́</strong>.</p>",
    },
    {
        "text": "<p>Dilnoza gapiryapti. Toʻgʻri shaklni tanlang.</p>"
                "<p><strong>Я ___ верну́ться до восьми́.</strong> (до́лжен)</p>",
        "choices": ["до́лжен", "должно́", "должны́", "должна́"],
        "correct": "должна́",
        "explanation": "<p>Dilnoza — ayol, <em>до́лжен</em> esa gapirayotgan "
                       "<strong>odamga</strong> moslashadi. Oʻzbekchada bu farq "
                       "eshitilmaydi, ruschada esa darrov bilinadi.</p>",
    },
    {
        "text": "<p>Qisqa shaklni yasang.</p><p><strong>свобо́дный</strong> "
                "(erkak)</p>",
        "choices": ["свобо́ден", "свобо́дн", "свобо́дный", "свобо́дна"],
        "correct": "свобо́ден",
        "explanation": "<p>Oʻzak <em>свободн-</em> ikki undosh bilan tugagan, "
                       "orasiga <strong>-е-</strong> chiqadi. Ayol shaklida "
                       "yoʻqoladi: <em>свобо́дна</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— Ты ___ в "
                "суббо́ту? — Нет, я ___.</strong> (свобо́дный / за́нятый)</p>",
        "choices": ["свобо́дный … за́нятый", "свобо́ден … за́нят",
                    "свобо́дна … занята́", "свобо́ден … за́нятый"],
        "correct": "свобо́ден … за́нят",
        "explanation": "<p>Ikkalasi ham <strong>kesim</strong>, demak qisqa "
                       "shakl. <em>Ты</em> erkakka murojaat qilinsa — "
                       "<em>свобо́ден</em> va <em>за́нят</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Обе́д уже́ "
                "___.</strong> (гото́вый)</p>",
        "choices": ["гото́вый", "гото́ва", "гото́вы", "гото́в"],
        "correct": "гото́в",
        "explanation": "<p><em>Обе́д</em> — erkak jinsida, gapda kesim kerak, "
                       "demak <strong>гото́в</strong>. «Tushlik tayyor».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на ___ с "
                "тобо́й.</strong> (согла́сный)</p>",
        "choices": ["согла́сная", "согла́сен", "согла́сны", "согла́сна"],
        "correct": "согла́сна",
        "explanation": "<p>Afsona — ayol, gapda kesim: <strong>согла́сна</strong>. "
                       "<em>Согла́сная</em> toʻliq shakl boʻlib, grammatikada "
                       "«undosh harf» degan butunlay boshqa maʼnoni "
                       "beradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ту́фли малы́.</strong> "
                "— bu nimani bildiradi?</p>",
        "choices": ["Tuflilar arzon", "Tuflilar kichkina oʻlchamli",
                    "Tuflilar oyoqqa kichiklik qilyapti", "Tuflilar eski"],
        "correct": "Tuflilar oyoqqa kichiklik qilyapti",
        "explanation": "<p>Oʻlchov haqidagi qisqa shakl «<strong>keragidan "
                       "ortiq</strong>» degan maʼnoni beradi. <em>Ма́ленькие "
                       "ту́фли</em> — kichik tuflilar (oʻlcham), <em>ту́фли "
                       "малы́</em> — menga kichiklik qilyapti.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он больно́й. · Он "
                "бо́лен.</strong></p>",
        "choices": ["Birinchisi — doimiy belgi, ikkinchisi — hozirgi holat",
                    "Birinchisida xato bor",
                    "Ikkinchisi kelasi zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — doimiy belgi, ikkinchisi — hozirgi holat",
        "explanation": "<p><em>Больно́й</em> — kasalmand odam (doimo). "
                       "<em>Бо́лен</em> — hozir kasal, ertaga tuzaladi. Qisqa "
                       "shakl vaqtinchalik holatni bildiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ну́жен</strong> bilan "
                "<strong>до́лжен</strong> ikki xil tomonga qaraydi. Qanday?</p>",
        "choices": ["Ikkalasi ham odamga qaraydi",
                    "Ikkalasi ham narsaga qaraydi",
                    "«Ну́жен» narsaga, «до́лжен» odamga",
                    "«Ну́жен» odamga, «до́лжен» narsaga"],
        "correct": "«Ну́жен» narsaga, «до́лжен» odamga",
        "explanation": "<p><em>Мне <strong>нужна́</strong> кни́га</em> — kitob "
                       "ayol jinsida. <em>Она́ <strong>должна́</strong> "
                       "рабо́тать</em> — u ayol. Bu darsning eng koʻp "
                       "adashtiriladigan juftligi.</p>",
    },
    {
        "text": "<p>Qaysi gapda toʻliq shakl kerak?</p>",
        "choices": ["Дом ___ .", "Я ___ вас ви́деть.", "Обе́д ___ .",
                    "Мы вошли́ в ___ дом."],
        "correct": "Мы вошли́ в ___ дом.",
        "explanation": "<p>Faqat bu gapda sifat <strong>otni aniqlaydi</strong> "
                       "(<em>краси́вый дом</em>). Qolgan uchtasida u kesim "
                       "oʻrnida turibdi, demak qisqa shakl kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ogʻzaki nutqda «uy chiroyli» "
                "qanday aytiladi?</p>",
        "choices": ["Faqat «дом краси́в»", "Koʻpincha «дом краси́вый»",
                    "«Краси́в дом»", "«Дом краси́вому»"],
        "correct": "Koʻpincha «дом краси́вый»",
        "explanation": "<p>Qisqa shakl <em>краси́в</em> — kitobiy. Kundalik "
                       "nutqda ruslar toʻliq shaklni ishlatadi. Lekin "
                       "<em>рад, до́лжен, ну́жен, гото́в, прав, за́нят</em> "
                       "bundan mustasno — ular har doim qisqa.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я рад вас ви́деть.", "Мне ну́жно кни́га.",
                    "Она́ должна́ идти́.", "Обе́д гото́в."],
        "correct": "Мне ну́жно кни́га.",
        "explanation": "<p><s>ну́жно</s> → <strong>нужна́</strong>. "
                       "<em>Кни́га</em> ayol jinsida, <em>ну́жен</em> esa kerak "
                       "boʻlgan narsaga moslashadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Дилно́за до́лжен идти́.", "Дилно́за должно́ идти́.",
                    "Дилно́за должна́ идти́.", "Дилно́за должны́ идти́."],
        "correct": "Дилно́за должна́ идти́.",
        "explanation": "<p>Dilnoza — ayol, birlikda. <em>До́лжен</em> egaga "
                       "moslashadi: <strong>должна́</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Извини́, я вчера́ был "
                "не прав.</strong></p>",
        "choices": ["— Я то́же винова́т. Я рад, что ты написа́л.",
                    "— Я то́же винова́тый. Я ра́дый, что ты написа́л.",
                    "— Я то́же винова́та́я. Я ра́дая, что ты написа́л.",
                    "— Я то́же винова́ту. Я ра́ду, что ты написа́л."],
        "correct": "— Я то́же винова́т. Я рад, что ты написа́л.",
        "explanation": "<p>Ikkalasi ham qisqa shakl. <s>Винова́тый</s> bu "
                       "kontekstda gʻalati, <s>ра́дый</s> esa umuman mavjud "
                       "emas.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Sen haq "
                "eding, men esa aybdorman.</strong></p>",
        "choices": ["Ты был пра́вый, а я винова́тый.", "Ты был прав, но я винова́т.",
                    "Ты был пра́во, а я винова́то.", "Ты был прав, а я винова́т."],
        "correct": "Ты был прав, а я винова́т.",
        "explanation": "<p>Ikkalasi ham qisqa shakl. <strong>А</strong> "
                       "ishlatiladi, chunki bu solishtirish (PR-67) — "
                       "oʻzbekcha «men <strong>esa</strong>».</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-71 Mashq: Причастие 2 — страдательные",
        "description": (
            "Прочи́танный / прочи́тан yasalishi, «toʻliqda ikkita Н, qisqada "
            "bitta Н» qoidasi va «kim tomonidan» — Твори́тельный."
        ),
        "tutorial": "PR-71:",
        "questions": Q_PR71,
    },
    {
        "title": "PR-72 Mashq: Деепричастие — читая va прочитав",
        "description": (
            "Oʻzbekcha «-ib» va «-gach». Yasalish, vergul va darsning yagona "
            "qatʼiy qoidasi: ega bir xil boʻlishi shart."
        ),
        "tutorial": "PR-72:",
        "questions": Q_PR72,
    },
    {
        "title": "PR-73 Mashq: Sifatning qisqa shakli",
        "description": (
            "Рад, до́лжен, ну́жен, гото́в, прав — kundalik nutqning oʻzagi. "
            "Ну́жен narsaga, до́лжен odamga moslashadi."
        ),
        "tutorial": "PR-73:",
        "questions": Q_PR73,
    },
]
