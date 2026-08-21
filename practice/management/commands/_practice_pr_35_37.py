# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-35 … PR-37.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_35_37.py --master=prime \\
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
# PR-35 — Родительный 2: predloglar bilan
# =====================================================================

Q_PR35 = [
    # 1–5 tanish
    {
        "text": "<p>Bu predloglardan qaysi biri Роди́тельный talab qilmaydi?</p>",
        "choices": ["без", "для", "в", "по́сле"],
        "correct": "в",
        "explanation": "<p><strong>В</strong> Предло́жный (в шко́ле) yoki Вини́тельный "
                       "(в шко́лу) bilan ishlaydi. <em>Без, для, по́сле, из, от, до, "
                       "у, о́коло</em> esa har doim Роди́тельный oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___ шко́лы.</strong> "
                "(«maktabdan» maʼnosida)</p>",
        "choices": ["с", "из", "от", "до"],
        "correct": "из",
        "explanation": "<p><em>Шко́ла</em> В oladi (<em>в шко́ле</em>), demak «dan» "
                       "uchun <strong>из</strong>. Bu PR-30 dagi roʻyxatning uchinchi "
                       "ishlatilishi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ве́чером я иду́ ___ "
                "рабо́ты.</strong></p>",
        "choices": ["из", "с", "от", "о́коло"],
        "correct": "с",
        "explanation": "<p><em>Рабо́та</em> НА oladi (<em>на рабо́те</em>), demak "
                       "«dan» uchun <strong>с</strong>. <em>«Из рабо́ты»</em> — "
                       "oʻzbek oʻquvchining klassik xatosi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то письмо́ ___ "
                "ма́мы.</strong></p>",
        "choices": ["из", "с", "от", "для"],
        "correct": "от",
        "explanation": "<p><strong>ОТ</strong> — odam uchun ishlatiladigan «dan». "
                       "Joydan chiqsangiz <em>из</em> yoki <em>с</em>, odamdan bir "
                       "narsa olsangiz — <em>от</em>.</p>",
    },
    {
        "text": "<p>Oʻzbekcha <strong>-siz</strong> qoʻshimchasi ruschada qaysi "
                "predlog?</p>",
        "choices": ["для", "без", "от", "до"],
        "correct": "без",
        "explanation": "<p><em>shakar<strong>siz</strong></em> → <em><strong>без</strong> "
                       "са́хара</em>. Farq faqat joyda: oʻzbekchada qoʻshimcha soʻzdan "
                       "keyin, ruschada predlog soʻzdan oldin.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то пода́рок для "
                "___.</strong> (ты)</p>",
        "choices": ["ты", "тебе́", "тебя́", "тобо́й"],
        "correct": "тебя́",
        "explanation": "<p>Роди́тельный olmoshlari Вини́тельный bilan bir xil: "
                       "<em>меня́, тебя́, его́, её, нас, вас, их</em>. Yaʼni yangi "
                       "narsa yodlash kerak emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У ___ есть маши́на.</strong> "
                "(он)</p>",
        "choices": ["его́", "него́", "ему́", "он"],
        "correct": "него́",
        "explanation": "<p>Predlogdan keyin <em>он/она́/они́</em> ga <strong>Н</strong> "
                       "qoʻshiladi. Predlogsiz esa Н yoʻq: <em>его́ нет до́ма</em>. Bu "
                       "qoidani PR-31 da ham koʻrgansiz: <em>о нём</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Чай без ___.</strong> "
                "(са́хар)</p>",
        "choices": ["са́хар", "са́хара", "са́хару", "са́харе"],
        "correct": "са́хара",
        "explanation": "<p>Predlogdan keyin ot Роди́тельный'ga kiradi. Erkak jins → "
                       "<strong>-а</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>По́сле ___ мы идём "
                "домо́й.</strong> (уро́к)</p>",
        "choices": ["уро́к", "уро́ка", "уро́ку", "уро́ке"],
        "correct": "уро́ка",
        "explanation": "<p><em>По́сле</em> Роди́тельный oladi. Oʻzbekchada «dars<strong>dan</strong> "
                       "keyin» — <em>-dan</em> bor, lekin ruschada hech qanday «dan» "
                       "predlogi qoʻshilmaydi, faqat <em>по́сле</em> + Р.п.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>О́коло ___ есть "
                "магази́н.</strong> (дом)</p>",
        "choices": ["дом", "до́ма", "до́му", "до́ме"],
        "correct": "до́ма",
        "explanation": "<p><em>О́коло</em> Роди́тельный oladi: <strong>о́коло "
                       "до́ма</strong> — «uy yaqinida». Shakl <em>до́ма</em> "
                       "(ravish, «uyda») bilan bir xil koʻrinadi, lekin urgʻu ham, "
                       "vazifa ham boshqa.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы е́дем ___ "
                "Москвы́.</strong> («Moskvadan» maʼnosida)</p>",
        "choices": ["с", "от", "из", "до"],
        "correct": "из",
        "explanation": "<p>Shahar В oladi (<em>в Москве́</em>), demak «dan» uchun "
                       "<strong>из</strong>: <em>из Москвы́</em>. Xuddi shunday: "
                       "<em>из Ташке́нта, из Сиби́ри</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ шко́лы недалеко́.</strong> "
                "(«maktabgacha» maʼnosida)</p>",
        "choices": ["До", "От", "Из", "У"],
        "correct": "До",
        "explanation": "<p><strong>До</strong> = oʻzbekcha <em>-gacha</em>. U ham "
                       "Роди́тельный oladi: <em>до шко́лы, до ве́чера, до "
                       "за́втра</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Oʻzbekcha <strong>-dan</strong> ruschada nechta predlogga "
                "boʻlinadi?</p>",
        "choices": ["Bitta — из", "Ikkita — из va с",
                    "Uchta — из, с va от", "Toʻrtta"],
        "correct": "Uchta — из, с va от",
        "explanation": "<p><strong>ИЗ</strong> — В oladigan joydan; <strong>С</strong> "
                       "— НА oladigan joydan; <strong>ОТ</strong> — odamdan. "
                       "Oʻzbekchada bittagina qoʻshimcha bu uch ishni bajaradi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda predlog toʻgʻri tanlangan?</p>",
        "choices": ["из шко́лы · с рабо́ты · от бра́та",
                    "с шко́лы · из рабо́ты · от бра́та",
                    "из шко́лы · из рабо́ты · из бра́та",
                    "от шко́лы · с рабо́ты · из бра́та"],
        "correct": "из шко́лы · с рабо́ты · от бра́та",
        "explanation": "<p>Uchta boshqa qoida: <em>шко́ла</em> В oladi → ИЗ; "
                       "<em>рабо́та</em> НА oladi → С; <em>брат</em> — odam → "
                       "ОТ.</p>",
    },
    {
        "text": "<p><strong>у меня́ есть</strong> iborasida <em>меня́</em> nega shu "
                "shaklda?</p>",
        "choices": ["Chunki у predlogi Роди́тельный talab qiladi",
                    "Chunki bu Вини́тельный",
                    "Chunki bu egalik olmoshi",
                    "Bu istisno, qoidasi yoʻq"],
        "correct": "Chunki у predlogi Роди́тельный talab qiladi",
        "explanation": "<p>PR-14 da bu ibora butun boʻlak sifatida berilgan edi. Endi "
                       "izohi bor: <strong>у</strong> + Роди́тельный. Xuddi shunday "
                       "<em>у бра́та, у окна́, у врача́</em>.</p>",
    },
    {
        "text": "<p>Oʻzbekcha va ruscha predloglarning asosiy farqi nima?</p>",
        "choices": ["Oʻzbekchada soʻzdan keyin, ruschada soʻzdan oldin turadi",
                    "Ruschada ular umuman ishlatilmaydi",
                    "Oʻzbekchada ular otni oʻzgartiradi",
                    "Farq yoʻq"],
        "correct": "Oʻzbekchada soʻzdan keyin, ruschada soʻzdan oldin turadi",
        "explanation": "<p><em>shakar-siz</em>, <em>maktab-gacha</em>, <em>onam "
                       "uchun</em> — hammasi orqada. Ruschada esa <em>без са́хара</em>, "
                       "<em>до шко́лы</em>, <em>для ма́мы</em> — hammasi oldinda, va "
                       "ot ham kelishikka kiradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["По́сле уро́ка мы идём домо́й.", "Э́то пода́рок для тебя́.",
                    "Я иду́ из рабо́ты.", "О́коло до́ма есть магази́н."],
        "correct": "Я иду́ из рабо́ты.",
        "explanation": "<p>Toʻgʻrisi — <strong>с рабо́ты</strong>. <em>Рабо́та</em> "
                       "НА oladigan roʻyxatda, shuning uchun «dan» uchun С "
                       "kerak.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["У его́ есть брат.", "У него́ есть брат.",
                    "У ему́ есть брат.", "У он есть брат."],
        "correct": "У него́ есть брат.",
        "explanation": "<p>Predlogdan keyin <strong>Н</strong> qoʻshiladi: "
                       "<em>у него́</em>. <em>Его́</em> predlogsiz ishlatiladi: "
                       "<em>его́ нет</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Отку́да ты?</strong></p>",
        "choices": ["— Из Ташке́нта.", "— В Ташке́нте.",
                    "— С Ташке́нта.", "— От Ташке́нта."],
        "correct": "— Из Ташке́нта.",
        "explanation": "<p><em>Отку́да?</em> — «qayerdan?». Shahar В oladi, demak "
                       "javobda <strong>из</strong>. Bu savol tanishuvda deyarli har "
                       "safar beriladi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ertalab uydan chiqaman, "
                "kechqurun ishdan qaytaman.</strong></p>",
        "choices": ["У́тром я иду́ с до́ма, ве́чером — из рабо́ты.",
                    "У́тром я иду́ из до́ма, ве́чером — с рабо́ты.",
                    "У́тром я иду́ из до́ма, ве́чером — из рабо́ты.",
                    "У́тром я иду́ от до́ма, ве́чером — от рабо́ты."],
        "correct": "У́тром я иду́ из до́ма, ве́чером — с рабо́ты.",
        "explanation": "<p>Bitta gapda ikkala «dan» ham bor: <em>дом</em> В oladi → "
                       "<strong>из до́ма</strong>; <em>рабо́та</em> НА oladi → "
                       "<strong>с рабо́ты</strong>.</p>",
    },
]


# =====================================================================
# PR-36 — Родительный 3: sonlar
# =====================================================================

Q_PR36 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>два ___</strong> (дом)</p>",
        "choices": ["дом", "до́ма", "домо́в", "до́му"],
        "correct": "до́ма",
        "explanation": "<p>2, 3, 4 — <strong>Роди́тельный birlik</strong>: <em>два "
                       "до́ма</em>. Bu PR-34 da oʻrgangan shakl.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>пять ___</strong> (дом)</p>",
        "choices": ["дом", "до́ма", "домо́в", "дома́"],
        "correct": "домо́в",
        "explanation": "<p>5 va undan yuqori — <strong>Роди́тельный koʻplik</strong>. "
                       "Erkak jins <strong>-ов</strong> oladi: <em>домо́в</em>.</p>",
    },
    {
        "text": "<p><strong>два</strong> yoki <strong>две</strong>?</p><p><strong>___ "
                "кни́ги</strong></p>",
        "choices": ["два", "две", "двое", "двух"],
        "correct": "две",
        "explanation": "<p><em>Кни́га</em> — ayol jinsi, demak <strong>две</strong>. "
                       "Faqat <em>оди́н</em> va <em>два</em> jinsga qaraydi; "
                       "<em>три, четы́ре, пять</em> — yoʻq.</p>",
    },
    {
        "text": "<p>Ayol jinsidagi ot koʻplik Роди́тельный'da qanday tugaydi?</p>",
        "choices": ["-ов", "-ей", "Qoʻshimchasiz qoladi", "-ы"],
        "correct": "Qoʻshimchasiz qoladi",
        "explanation": "<p><em>кни́га → книг</em>, <em>шко́ла → школ</em>, "
                       "<em>мину́та → мину́т</em>. Soʻz «yalangʻoch» qoladi — aslida "
                       "bu eng oson shakl.</p>",
    },
    {
        "text": "<p><strong>мно́го</strong> qaysi kelishikni talab qiladi?</p>",
        "choices": ["Bosh kelishik", "Вини́тельный", "Роди́тельный", "Да́тельный"],
        "correct": "Роди́тельный",
        "explanation": "<p><em>Мно́го книг, ма́ло воды́, ско́лько вре́мени</em> — "
                       "miqdor soʻzlari ham Роди́тельный oladi. Sanaladigan narsa — "
                       "koʻplik, sanalmaydigani — birlik.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне два́дцать оди́н "
                "___.</strong> (год)</p>",
        "choices": ["год", "го́да", "лет", "года́м"],
        "correct": "год",
        "explanation": "<p>Oxirgi raqam <strong>1</strong>, demak bosh kelishik, "
                       "birlik: <em>два́дцать оди́н год</em>. Solishtiring: "
                       "<em>два́дцать два го́да</em>, <em>два́дцать пять "
                       "лет</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне два́дцать пять "
                "___.</strong> (год)</p>",
        "choices": ["год", "го́да", "лет", "го́ды"],
        "correct": "лет",
        "explanation": "<p>Oxiri 5, demak koʻplik Роди́тельный — va <em>год</em> bu "
                       "shaklda <strong>лет</strong> boʻladi. Bu istisnoni alohida "
                       "yodlang: yosh haqida gapirganda u har kuni kerak.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>В кла́ссе двена́дцать "
                "___.</strong> (учени́к)</p>",
        "choices": ["учени́к", "ученика́", "ученико́в", "ученики́"],
        "correct": "ученико́в",
        "explanation": "<p><strong>11–14</strong> — yagona istisno: ular «2» ga "
                       "tugasa ham har doim koʻplik Роди́тельный oladi. Erkak jins → "
                       "<strong>-ов</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Пять ___</strong> "
                "(челове́к)</p>",
        "choices": ["челове́к", "челове́ка", "челове́ков", "люде́й"],
        "correct": "челове́к",
        "explanation": "<p>Son bilan <em>челове́к</em> shakli oʻzgarmaydi: <strong>пять "
                       "челове́к</strong>. Lekin <em>мно́го</em> bilan boshqa shakl "
                       "kerak: <em>мно́го люде́й</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>В до́ме пять ___.</strong> "
                "(окно́)</p>",
        "choices": ["окно́", "окна́", "о́кон", "о́кна"],
        "correct": "о́кон",
        "explanation": "<p>Oʻrta jins koʻplik Роди́тельный'da qoʻshimchasini "
                       "yoʻqotadi, lekin talaffuz uchun ichkariga <strong>О</strong> "
                       "qoʻshiladi: <em>окно́ → о́кон</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь мно́го ___.</strong> "
                "(кни́га)</p>",
        "choices": ["кни́га", "кни́ги", "книг", "кни́гам"],
        "correct": "книг",
        "explanation": "<p><em>Мно́го</em> koʻplik Роди́тельный talab qiladi, ayol "
                       "jinsi esa qoʻshimchasiz qoladi: <strong>книг</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Три ___</strong> "
                "(мину́та)</p>",
        "choices": ["мину́та", "мину́ты", "мину́т", "мину́те"],
        "correct": "мину́ты",
        "explanation": "<p>3 — Роди́тельный <strong>birlik</strong>: <em>три "
                       "мину́ты</em>. <em>Мину́т</em> esa 5 dan boshlab kerak: "
                       "<em>пять мину́т</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Katta sonlarda qaysi raqamga qaraladi?</p>",
        "choices": ["Birinchi raqamga", "Oxirgi raqamga",
                    "Butun songa", "Raqamlar yigʻindisiga"],
        "correct": "Oxirgi raqamga",
        "explanation": "<p><em>Два́дцать <strong>оди́н</strong> дом</em>, "
                       "<em>два́дцать <strong>два</strong> до́ма</em>, "
                       "<em>два́дцать <strong>пять</strong> домо́в</em>. Istisno — "
                       "11 dan 14 gacha, ular har doim koʻplik oladi.</p>",
    },
    {
        "text": "<p>Nega <strong>одиннадцать</strong> istisno hisoblanadi?</p>",
        "choices": ["Chunki u «1» ga tugasa ham koʻplik oladi",
                    "Chunki u jinsga qaraydi",
                    "Chunki u bosh kelishik oladi",
                    "U istisno emas"],
        "correct": "Chunki u «1» ga tugasa ham koʻplik oladi",
        "explanation": "<p><em>Оди́ннадцать домо́в</em>, <em>«оди́ннадцать дом»</em> "
                       "emas. 11–14 — yagona guruh, unda oxirgi raqam qoidasi "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>Oʻzbek tili bu mavzuda qanday yordam beradi?</p>",
        "choices": ["Toʻliq yordam beradi — qoida bir xil",
                    "Yarim yordam: son bilan ot koʻplikka kirmaydi, lekin oʻzgarmaydi ham",
                    "Umuman yordam bermaydi",
                    "Oʻzbekchada ham uchta guruh bor"],
        "correct": "Yarim yordam: son bilan ot koʻplikka kirmaydi, lekin oʻzgarmaydi ham",
        "explanation": "<p><em>Besh kitob</em> — «besh kitoblar» emas, va bu instinkt "
                       "toʻgʻri. Lekin oʻzbekchada ot <strong>umuman</strong> "
                       "oʻzgarmaydi, ruschada esa uchta guruh bor. Shuning uchun bu "
                       "dars sof qoʻshimcha ish.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["две кни́ги · пять книг · мно́го книг",
                    "два кни́ги · пять кни́ги · мно́го книг",
                    "две кни́ги · пять кни́ги · мно́го кни́ги",
                    "две кни́га · пять книг · мно́го кни́ги"],
        "correct": "две кни́ги · пять книг · мно́го книг",
        "explanation": "<p>Uchta qoida ketma-ket: 2 + ayol jinsi → <em>две "
                       "кни́ги</em>; 5+ → koʻplik Роди́тельный <em>книг</em>; miqdor "
                       "soʻzi ham koʻplik <em>книг</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["У меня́ две сестры́.", "В до́ме пять окон.",
                    "Мне два́дцать оди́н лет.", "Здесь мно́го люде́й."],
        "correct": "Мне два́дцать оди́н лет.",
        "explanation": "<p>Toʻgʻrisi — <strong>два́дцать оди́н год</strong>. Oxirgi "
                       "raqam 1, demak bosh kelishik birlik. <em>Лет</em> faqat 5 dan "
                       "boshlab kerak.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["В кла́ссе пять люде́й.", "В кла́ссе пять челове́к.",
                    "В кла́ссе пять челове́ка.", "В кла́ссе пять челове́ков."],
        "correct": "В кла́ссе пять челове́к.",
        "explanation": "<p>Son bilan — <strong>челове́к</strong>. <em>Люде́й</em> "
                       "shakli <em>мно́го</em>, <em>ма́ло</em>, <em>ско́лько</em> "
                       "bilan ishlatiladi: <em>мно́го люде́й</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ско́лько тебе́ лет?</strong></p>",
        "choices": ["— Мне два́дцать три го́да.", "— Мне два́дцать три лет.",
                    "— Мне два́дцать три год.", "— Мне два́дцать три го́ды."],
        "correct": "— Мне два́дцать три го́да.",
        "explanation": "<p>Oxirgi raqam <strong>3</strong>, demak Роди́тельный "
                       "birlik — <em>го́да</em>. Savolda esa <em>лет</em>, chunki "
                       "<em>ско́лько</em> koʻplik talab qiladi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bizning uyimizda besh "
                "qavat va qirq xonadon bor.</strong></p>",
        "choices": ["В на́шем до́ме пять этажа́ и со́рок кварти́ры.",
                    "В на́шем до́ме пять этаже́й и со́рок кварти́р.",
                    "В на́шем до́ме пять этаже́й и со́рок кварти́ры.",
                    "В на́шем до́ме пять эта́ж и со́рок кварти́р."],
        "correct": "В на́шем до́ме пять этаже́й и со́рок кварти́р.",
        "explanation": "<p>Ikkalasi ham 5 dan yuqori, demak koʻplik Роди́тельный. "
                       "<em>Эта́ж</em> Ж ga tugaydi → <strong>-ей</strong>; "
                       "<em>кварти́ра</em> ayol jinsi → <strong>qoʻshimchasiz</strong>.</p>",
    },
]


# =====================================================================
# PR-37 — Дательный 1: кому?
# =====================================================================

Q_PR37 = [
    # 1–5 tanish
    {
        "text": "<p>Да́тельный padeji oʻzbekchadagi qaysi qoʻshimchaga toʻgʻri "
                "keladi?</p>",
        "choices": ["-ni", "-ga", "-da", "-ning"],
        "correct": "-ga",
        "explanation": "<p><em>aka<strong>ga</strong> aytdim</em> → <em>сказа́л "
                       "бра́т<strong>у</strong></em>. Bu blokdagi eng aniq moslik — "
                       "hech qanday tuzoq yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я дам ___ кни́гу.</strong> "
                "(брат)</p>",
        "choices": ["брат", "бра́та", "бра́ту", "бра́те"],
        "correct": "бра́ту",
        "explanation": "<p>Erkak jins Да́тельный'da <strong>-у</strong> oladi. Savol: "
                       "kimga beraman? — <em>бра́ту</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я звоню́ ___.</strong> "
                "(ма́ма)</p>",
        "choices": ["ма́ма", "ма́му", "ма́мы", "ма́ме"],
        "correct": "ма́ме",
        "explanation": "<p>Ayol jinsi Да́тельный'da <strong>-е</strong> oladi. Va "
                       "<em>звони́ть</em> aynan shu kelishikni talab qiladi — "
                       "oʻzbekcha «onam<strong>ga</strong> qoʻngʻiroq qilaman» toʻgʻri "
                       "javobni koʻrsatadi.</p>",
    },
    {
        "text": "<p><strong>мне, тебе́, ему́, ей</strong> — bu qaysi kelishik?</p>",
        "choices": ["Роди́тельный", "Вини́тельный", "Да́тельный", "Предло́жный"],
        "correct": "Да́тельный",
        "explanation": "<p>Siz bu shakllarni PR-27 (<em>мне на́до</em>) va PR-28 "
                       "(<em>мне нра́вится</em>) da ishlatgansiz. Endi ularning nomi "
                       "bor.</p>",
    },
    {
        "text": "<p><strong>помога́ть</strong> qaysi kelishikni oladi?</p>",
        "choices": ["Вини́тельный", "Да́тельный", "Роди́тельный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>Помога́ть бра́т<strong>у</strong></em>. Oʻzbekcha "
                       "«aka<strong>ga</strong> yordam bermoq» toʻgʻri javobni "
                       "beradi. Ingliz tilini biladiganlar bu yerda xato qiladi, "
                       "chunki «help» toʻgʻridan-toʻgʻri toʻldiruvchi oladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бекзо́д помога́ет "
                "___.</strong> (ба́бушка)</p>",
        "choices": ["ба́бушка", "ба́бушку", "ба́бушке", "ба́бушки"],
        "correct": "ба́бушке",
        "explanation": "<p>Ayol jinsi → <strong>-е</strong>, va <em>помога́ть</em> "
                       "Да́тельный oladi. Ikkala qoida bir vaqtda ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он отвеча́ет ___.</strong> "
                "(учи́тель)</p>",
        "choices": ["учи́тель", "учи́теля", "учи́телю", "учи́теле"],
        "correct": "учи́телю",
        "explanation": "<p>Erkak jins, <strong>-ь</strong> ga tugaydi, demak "
                       "<strong>-ю</strong>. <em>Отвеча́ть</em> ham Да́тельный "
                       "oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на пи́шет ___ "
                "письмо́.</strong> (ба́бушка)</p>",
        "choices": ["ба́бушку", "ба́бушке", "ба́бушки", "ба́бушка"],
        "correct": "ба́бушке",
        "explanation": "<p>Ikkita toʻldiruvchi: <strong>ба́бушке</strong> — kimga "
                       "(Да́тельный), <strong>письмо́</strong> — nimani (Вини́тельный, "
                       "oʻrta jins, oʻzgarmaydi).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Учи́тель объясня́ет "
                "___.</strong> (класс)</p>",
        "choices": ["класс", "кла́сса", "кла́ссу", "кла́ссе"],
        "correct": "кла́ссу",
        "explanation": "<p>Erkak jins → <strong>-у</strong>. Oʻzbekcha «sinf<strong>ga</strong> "
                       "tushuntiradi» — <em>-ga</em> bor, demak Да́тельный.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Что ты сказа́л "
                "___?</strong> (Афсо́на)</p>",
        "choices": ["Афсо́на", "Афсо́ну", "Афсо́не", "Афсо́ны"],
        "correct": "Афсо́не",
        "explanation": "<p>Ayol jinsi → <strong>-е</strong>. Ismlar oddiy otlar kabi "
                       "turlanadi. <em>Афсо́ну</em> — Вини́тельный shakli, u bu feʼl "
                       "bilan ishlamaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я дам ___ кни́гу.</strong> "
                "(она́)</p>",
        "choices": ["её", "ей", "ему́", "неё"],
        "correct": "ей",
        "explanation": "<p><strong>Ей</strong> — Да́тельный. PR-27 va PR-28 dan "
                       "tanish: <em>ей на́до, ей нра́вится</em>. <em>Её</em> esa "
                       "Вини́тельный / Роди́тельный.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Не меша́й ___.</strong> "
                "(сестра́)</p>",
        "choices": ["сестра́", "сестру́", "сестре́", "сестры́"],
        "correct": "сестре́",
        "explanation": "<p><em>Меша́ть</em> Да́тельный oladi — «singlim<strong>ga</strong> "
                       "xalaqit berma». Ayol jinsi → <strong>-е</strong>, urgʻu "
                       "oxirda.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega <strong>ма́ме</strong> ikkita kelishikda bir xil "
                "koʻrinadi?</p>",
        "choices": ["Ayol jinsida Да́тельный va Предло́жный shakllari bir xil",
                    "Bu xato",
                    "Chunki «ма́ма» istisno soʻz",
                    "Chunki bu koʻplik"],
        "correct": "Ayol jinsida Да́тельный va Предло́жный shakllari bir xil",
        "explanation": "<p><em>дать ма́ме</em> (Д.п.) va <em>о ма́ме</em> (П.п.). "
                       "Farqni <strong>predlog</strong> koʻrsatadi. PR-29 da aytilgan "
                       "edi: shakllar takrorlanadi, shuning uchun yodlanadigan narsa "
                       "kutilganidan kam.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я жду сестру́. · Я "
                "помога́ю сестре́.</strong></p>",
        "choices": ["Birinchisi Вини́тельный, ikkinchisi Да́тельный",
                    "Ikkalasi bir xil kelishik",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Birinchisi Вини́тельный, ikkinchisi Да́тельный",
        "explanation": "<p>Feʼl kelishikni tanlaydi. <em>Ждать</em> toʻldiruvchi "
                       "oladi («singlimni kutaman»), <em>помога́ть</em> esa "
                       "Да́тельный («singlim<strong>ga</strong> yordam beraman»). "
                       "Oʻzbekcha ikkalasini ham toʻgʻri koʻrsatadi.</p>",
    },
    {
        "text": "<p><strong>дать</strong> feʼli nechta toʻldiruvchi oladi?</p>",
        "choices": ["Bitta", "Ikkita: kimga (Д.п.) va nimani (В.п.)",
                    "Uchta", "Hech qanday"],
        "correct": "Ikkita: kimga (Д.п.) va nimani (В.п.)",
        "explanation": "<p><em>Я дам <strong>бра́ту</strong> "
                       "<strong>кни́гу</strong></em>. Xuddi shunday <em>сказа́ть</em> "
                       "va <em>писа́ть</em>. Oʻzbekchadagi tartib ham shunday: "
                       "«akamga kitobni beraman».</p>",
    },
    {
        "text": "<p>Qaysi feʼl Да́тельный <strong>olmaydi</strong>?</p>",
        "choices": ["помога́ть", "звони́ть", "ждать", "объясня́ть"],
        "correct": "ждать",
        "explanation": "<p><em>Ждать</em> Вини́тельный oladi: <em>жду бра́та, жду "
                       "авто́бус</em>. Qolgan uchtasi Да́тельный oladi — va "
                       "oʻzbekchada ularning hammasida <em>-ga</em> bor.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он отвеча́ет учи́телю.", "Я помога́ю сестру́.",
                    "Афсо́на пи́шет ба́бушке.", "Мне на́до идти́."],
        "correct": "Я помога́ю сестру́.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я помога́ю сестре́</strong>. "
                       "<em>Помога́ть</em> Да́тельный oladi, ayol jinsi esa "
                       "<strong>-е</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я звоню́ ма́му.", "Я звоню́ ма́ме.",
                    "Я звоню́ ма́мы.", "Я звоню́ о ма́ме."],
        "correct": "Я звоню́ ма́ме.",
        "explanation": "<p><em>Звони́ть</em> + Да́тельный. Oʻzbekcha tekshiruv har "
                       "safar ishlaydi: «onam<strong>ga</strong> qoʻngʻiroq "
                       "qilaman».</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Кому́ ты пи́шешь?</strong></p>",
        "choices": ["— Ба́бушке.", "— Ба́бушку.", "— Ба́бушки.", "— О ба́бушке."],
        "correct": "— Ба́бушке.",
        "explanation": "<p>Savol <em>кому́?</em> — Да́тельный, demak javob ham shu "
                       "shaklda. <em>О ба́бушке</em> boshqa savolga javob boʻlardi: "
                       "<em>о ком?</em></p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bekzod buvisiga yordam "
                "beradi va onasiga qoʻngʻiroq qiladi.</strong></p>",
        "choices": ["Бекзо́д помога́ет ба́бушку и звони́т ма́му.",
                    "Бекзо́д помога́ет ба́бушке и звони́т ма́ме.",
                    "Бекзо́д помога́ет ба́бушке и звони́т ма́му.",
                    "Бекзо́д помога́ет ба́бушки и звони́т ма́ме."],
        "correct": "Бекзо́д помога́ет ба́бушке и звони́т ма́ме.",
        "explanation": "<p>Ikkala feʼl ham Да́тельный oladi va ikkala ot ham ayol "
                       "jinsida → <strong>-е</strong>. Oʻzbekchadagi ikkita "
                       "<em>-ga</em> toʻgʻri javobni koʻrsatib turibdi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-35 Mashq: Родительный 2: predloglar bilan — из, от, до, у, без, для, около, после",
        "description": (
            "Sakkizta predlog, uchta «-dan» (из / с / от) va PR-30 dagi В/НА "
            "roʻyxatining uchinchi ishlatilishi."
        ),
        "tutorial": "PR-35:",
        "questions": Q_PR35,
    },
    {
        "title": "PR-36 Mashq: Родительный 3: sonlar va miqdor bilan — два дома, пять домов, много книг",
        "description": (
            "Uchta guruh (1 / 2-3-4 / 5+), koʻplik Роди́тельный qoʻshimchalari, "
            "11–14 istisnosi va мно́го / ма́ло / ско́лько."
        ),
        "tutorial": "PR-36:",
        "questions": Q_PR36,
    },
    {
        "title": "PR-37 Mashq: Дательный 1: кому? — дать, сказать, написать, помочь",
        "description": (
            "Oʻzbekcha -GA ning aynan oʻzi: -у/-ю va -е qoʻshimchalari, "
            "Да́тельный oladigan feʼllar va ikki toʻldiruvchili gaplar."
        ),
        "tutorial": "PR-37:",
        "questions": Q_PR37,
    },
]
