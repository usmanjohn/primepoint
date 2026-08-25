# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-83 … PR-85.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_83_85.py --master=prime \\
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
# PR-83 — Predlog xaritasi 2
# =====================================================================

Q_PR83 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Несмотря́ на ___, "
                "матч не отмени́ли.</strong> (дождь)</p>",
        "choices": ["дождя́", "дождю́", "дождём", "дождь"],
        "correct": "дождь",
        "explanation": "<p><strong>Несмотря́ на</strong> Вини́тельный oladi, "
                       "chunki ichida <em>на</em> bor. Jonsiz otda В.п. И.п. "
                       "bilan bir xil: <em>дождь</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Несмотря́</strong> "
                "soʻzi soʻzma-soʻz nimani anglatadi?</p>",
        "choices": ["Koʻrmay", "Bilmay", "Qaramay", "Aytmay"],
        "correct": "Qaramay",
        "explanation": "<p><em>не</em> + <em>смотря́</em> = «qaramay» — "
                       "oʻzbekcha <em>qara + -may</em> ning aynan nusxasi. "
                       "Ikkala til ham «yomgʻirga qaramay» deydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>По</strong> odatda "
                "qaysi kelishikni oladi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>по у́лице, по телефо́ну, по расписа́нию</em> — "
                       "hammasi <strong>Да́тельный</strong>. Qiyinligi "
                       "kelishikda emas, maʼnolarining koʻpligida.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Спаси́бо ___ "
                "по́мощь!</strong></p>",
        "choices": ["для", "по", "о", "за"],
        "correct": "за",
        "explanation": "<p>«Uchun, evaziga» maʼnosida <strong>за</strong> + "
                       "Вини́тельный. <s>Спаси́бо для по́мощи</s> — koʻp "
                       "uchraydigan xato.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Вме́сто</strong> va "
                "<strong>кро́ме</strong> qaysi kelishikni oladi?</p>",
        "choices": ["Ikkalasi Роди́тельный", "Ikkalasi Да́тельный",
                    "Вме́сто — Р.п., кро́ме — Д.п.", "Ikkalasi Вини́тельный"],
        "correct": "Ikkalasi Роди́тельный",
        "explanation": "<p><em>вме́сто ча́я</em>, <em>кро́ме меня́</em> — "
                       "ikkalasi ham <strong>Роди́тельный</strong>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма посла́ла "
                "меня́ ___ .</strong> (non olib kelgani)</p>",
        "choices": ["за хлеб", "за хле́бом", "по хлеб", "для хле́ба"],
        "correct": "за хле́бом",
        "explanation": "<p>«Olib kelgani» maʼnosida <strong>за</strong> + "
                       "<strong>Твори́тельный</strong>. <em>За хлеб</em> «non "
                       "orqasiga» degan kulgili maʼno berardi.</p>",
    },
    {
        "text": "<p><strong>По</strong> ning qaysi maʼnosi?</p><p><strong>Мы "
                "получи́ли по два биле́та.</strong></p>",
        "choices": ["Boʻylab", "Orqali", "Taqsimlash — ikkitadan", "Sabab"],
        "correct": "Taqsimlash — ikkitadan",
        "explanation": "<p>«Ikkitadan chipta oldik» — har birimizga ikkitadan. "
                       "Oʻzbekcha <em>-tadan</em> qoʻshimchasi shuni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он вы́пил ко́фе "
                "вме́сто ___ .</strong> (чай)</p>",
        "choices": ["чай", "ча́ю", "ча́ем", "ча́я"],
        "correct": "ча́я",
        "explanation": "<p><strong>Вме́сто</strong> Роди́тельный oladi: "
                       "<em>вме́сто ча́я</em>, <em>вме́сто меня́</em>.</p>",
    },
    {
        "text": "<p>Uchtasini toʻgʻri kelishikka qoʻying.</p><p><strong>из-за "
                "(дождь) · благодаря́ (учи́тель)</strong></p>",
        "choices": ["из-за дождю́ · благодаря́ учи́теля",
                    "из-за дождя́ · благодаря́ учи́теля",
                    "из-за дождя́ · благодаря́ учи́телю",
                    "из-за дождь · благодаря́ учи́телем"],
        "correct": "из-за дождя́ · благодаря́ учи́телю",
        "explanation": "<p><strong>Из-за</strong> + Роди́тельный, "
                       "<strong>благодаря́</strong> + Да́тельный. "
                       "<em>Благодаря́</em> ichida «rahmat aytmoq» bor, rahmat "
                       "esa kimga aytiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Кот сиди́т ___ "
                ".</strong> (uy orqasida)</p>",
        "choices": ["за дом", "за до́ма", "за до́му", "за до́мом"],
        "correct": "за до́мом",
        "explanation": "<p>Joy — harakat yoʻq, demak <strong>за</strong> + "
                       "<strong>Твори́тельный</strong>. Harakat boʻlsa: "
                       "<em>кот побежа́л за дом</em> (В.п.).</p>",
    },
    {
        "text": "<p><strong>Кро́ме</strong> ning qaysi maʼnosi?</p>"
                "<p><strong>Кро́ме ру́сского, он зна́ет коре́йский.</strong></p>",
        "choices": ["Istisno — ruschani bilmaydi", "Qoʻshimcha — ikkalasini ham biladi",
                    "Solishtirish", "Sabab"],
        "correct": "Qoʻshimcha — ikkalasini ham biladi",
        "explanation": "<p><em>Кро́ме</em> ikki maʼnoli, xuddi oʻzbekcha «…dan "
                       "tashqari» kabi. Bu yerda qoʻshimcha maʼnosi: rus tilidan "
                       "tashqari koreyschani <strong>ham</strong> biladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы опозда́ли ___ "
                ".</strong> (xato bilan)</p>",
        "choices": ["с оши́бкой", "за оши́бку", "по оши́бке", "из оши́бки"],
        "correct": "по оши́бке",
        "explanation": "<p><strong>По</strong> ning sabab maʼnosi: <em>по "
                       "оши́бке</em>, <em>по боле́зни</em>, <em>по "
                       "привы́чке</em>. Rasmiyroq uslub.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu uch predlog qaysi "
                "kelishiklarni oladi?</p><p><strong>из-за · благодаря́ · "
                "несмотря́ на</strong></p>",
        "choices": ["Р.п. · Д.п. · В.п.", "Д.п. · Р.п. · В.п.",
                    "Р.п. · В.п. · Д.п.", "Hammasi Р.п."],
        "correct": "Р.п. · Д.п. · В.п.",
        "explanation": "<p>Uch predlog — uch kelishik, va aynan shu "
                       "adashtiriladi. Yodda tuting: <em>несмотря́ "
                       "<strong>на</strong></em> ichidagi <em>на</em> "
                       "Вини́тельный talab qiladi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Кот сиди́т за "
                "до́мом. · Кот побежа́л за дом.</strong></p>",
        "choices": ["Farqi yoʻq",
                    "Birinchisi joy (Т.п.), ikkinchisi yoʻnalish (В.п.)",
                    "Ikkinchisi kelasi zamon",
                    "Birinchisida xato bor"],
        "correct": "Birinchisi joy (Т.п.), ikkinchisi yoʻnalish (В.п.)",
        "explanation": "<p><strong>За</strong> kelishikka qarab maʼnosini "
                       "oʻzgartiradi: Твори́тельный — turgan joyi, "
                       "Вини́тельный — qayerga borgani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«boʻylab, "
                "orqali, koʻra»</strong> ruschada odatda nimaga tushadi?</p>",
        "choices": ["за", "из-за", "вме́сто", "по"],
        "correct": "по",
        "explanation": "<p>Oʻzbekchada toʻrtta alohida soʻz, ruschada esa "
                       "hammasi bitta <strong>по + Да́тельный</strong> ga "
                       "yigʻilgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Несмотря́ ___ , "
                "что шёл дождь, матч не отмени́ли.</strong></p>",
        "choices": ["на то", "на том", "на тем", "того́"],
        "correct": "на то",
        "explanation": "<p>Butun gap bilan kelganda <strong>несмотря́ на то, "
                       "что</strong> boʻladi — xuddi PR-66 dagi <em>из-за "
                       "того́ что</em> kabi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Несмотря́ на дождя́, мы пошли́.", "Несмотря́ на дождь, мы пошли́.",
                    "Из-за дождя́ мы не пошли́.", "Благодаря́ дру́гу я нашёл рабо́ту."],
        "correct": "Несмотря́ на дождя́, мы пошли́.",
        "explanation": "<p><s>дождя́</s> → <strong>дождь</strong>. "
                       "<em>Несмотря́ на</em> Вини́тельный oladi, Роди́тельный "
                       "esa <em>из-за</em> niki.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я иду́ за хлеб.", "Я иду́ по хлеб.",
                    "Я иду́ за хле́бом.", "Я иду́ для хле́ба."],
        "correct": "Я иду́ за хле́бом.",
        "explanation": "<p>«Olib kelgani» — <strong>за</strong> + "
                       "Твори́тельный. Bu kundalik nutqda juda koʻp "
                       "ishlatiladigan qurilish.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Почему́ ты не пришёл "
                "на трениро́вку?</strong></p>",
        "choices": ["— Из-за боле́зни.", "— Благодаря́ боле́зни.",
                    "— Несмотря́ на боле́знь.", "— Вме́сто боле́зни."],
        "correct": "— Из-за боле́зни.",
        "explanation": "<p>Natija yomon (kelmadim), demak "
                       "<strong>из-за</strong> + Роди́тельный. "
                       "<em>Благодаря́</em> yaxshi natijaga ishlatiladi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Kasalligiga "
                "qaramay, u mendan tashqari hammaga xat yozdi.</strong></p>",
        "choices": ["Из-за боле́зни он написа́л всем, кро́ме меня́.",
                    "Несмотря́ на боле́знь, он написа́л всем, кро́ме меня́.",
                    "Несмотря́ на боле́зни, он написа́л всем, вме́сто меня́.",
                    "Благодаря́ боле́зни он написа́л всем, кро́ме меня́."],
        "correct": "Несмотря́ на боле́знь, он написа́л всем, кро́ме меня́.",
        "explanation": "<p>«Qaramay» → <em>несмотря́ на</em> + В.п.; «dan "
                       "tashqari» → <em>кро́ме</em> + Р.п.; «hammaga» → "
                       "<em>всем</em> (Д.п.).</p>",
    },
]


# =====================================================================
# PR-84 — Yuklamalar
# =====================================================================

Q_PR84 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Yuklamalar gapga nima "
                "qoʻshadi?</p>",
        "choices": ["Yangi maʼno", "Kelishik", "Zamon", "Munosabat, ohang"],
        "correct": "Munosabat, ohang",
        "explanation": "<p><em>Я говори́л</em> va <em>Я <strong>же</strong> "
                       "говори́л</em> — maʼnosi bir xil, lekin ikkinchisida "
                       "ovoz bor. Yuklamalar nutqni jonlantiradi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Aytdim-ku!</strong></p>",
        "choices": ["Я говори́л же!", "Же я говори́л!",
                    "Я говори́л ли!", "Я же говори́л!"],
        "correct": "Я же говори́л!",
        "explanation": "<p>Oʻzbekcha <strong>-ku</strong> = ruscha "
                       "<strong>же</strong>, va u taʼkidlanayotgan soʻzdan "
                       "keyin turadi. <em>Же</em> gapni boshlamaydi va gap "
                       "oxirida turmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Неуже́ли</strong> "
                "oʻzbekchada nima?</p>",
        "choices": ["Albatta", "Faqat", "Nahotki", "Hatto"],
        "correct": "Nahotki",
        "explanation": "<p><em>Неуже́ли пра́вда?</em> — «Nahotki rost boʻlsa?» "
                       "Ikkalasi ham kuchli hayrat va ishonmaslikni bildiradi, "
                       "ikkalasi ham gap boshida turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Да́же</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Faqat", "Shunchaki", "Hatto", "Axir"],
        "correct": "Hatto",
        "explanation": "<p><em>Да́же он не знал</em> — «Hatto u ham "
                       "bilmasdi». <em>То́лько</em> — faqat, "
                       "<em>про́сто</em> — shunchaki.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir gapda odatda nechta "
                "yuklama boʻladi?</p>",
        "choices": ["Bitta, kamdan-kam ikkita", "Kamida uchta",
                    "Qancha boʻlsa shuncha yaxshi", "Hech qachon boʻlmaydi"],
        "correct": "Bitta, kamdan-kam ikkita",
        "explanation": "<p>Yuklamalar tuz kabi: ozi taomni ochadi, koʻpi "
                       "buzadi. <s>Ну вот я же ведь про́сто уж говори́л "
                       "же!</s> — bunday gapirilmaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ___ зна́ешь "
                "его́, пра́вда?</strong></p>",
        "choices": ["ведь", "лишь", "да́же", "ра́зве"],
        "correct": "ведь",
        "explanation": "<p><strong>Ведь</strong> tinglovchining allaqachon "
                       "biladigan narsasiga murojaat qiladi — «axir, oʻzing "
                       "bilasan». <em>Же</em> ham mumkin edi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ он сдал "
                "экза́мен без подгото́вки?!</strong> (juda hayronman)</p>",
        "choices": ["Ра́зве", "Ведь", "Неуже́ли", "Же"],
        "correct": "Неуже́ли",
        "explanation": "<p><strong>Неуже́ли</strong> — kuchli hayrat, "
                       "«nahotki». <em>Ра́зве</em> yumshoqroq boʻlardi: "
                       "«rostdanmi?».</p>",
    },
    {
        "text": "<p>Javob bering.</p><p><strong>— Он опозда́л на де́сять "
                "мину́т.</strong> (sizga farqi yoʻq)</p>",
        "choices": ["— Ну и что?", "— Неуже́ли?", "— Вот и всё.", "— Ра́зве?"],
        "correct": "— Ну и что?",
        "explanation": "<p><em>Ну и что?</em> — «Nima boʻpti?», eʼtirozsiz "
                       "befarqlik. <em>Ну ла́дно</em> yumshoqroq variant "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ не сего́дня, "
                "я о́чень уста́л.</strong></p>",
        "choices": ["Да́же", "Ведь", "Же", "То́лько"],
        "correct": "То́лько",
        "explanation": "<p><em>То́лько не сего́дня</em> — «Faqat bugun "
                       "emas». <strong>То́лько</strong> = faqat; kitobiy "
                       "varianti <em>лишь</em>.</p>",
    },
    {
        "text": "<p>Bu ikki gapdagi <strong>-то</strong> bir xilmi?</p>"
                "<p><strong>Кто́-то звони́л. · Я-то зна́ю.</strong></p>",
        "choices": ["Ha, ikkalasi noaniqlik",
                    "Yoʻq: birinchisi noaniqlik, ikkinchisi taʼkid",
                    "Ha, ikkalasi taʼkid",
                    "Ikkinchisida xato bor"],
        "correct": "Yoʻq: birinchisi noaniqlik, ikkinchisi taʼkid",
        "explanation": "<p>Savol soʻziga yopishsa — <strong>noaniqlik</strong> "
                       "(PR-78). Oddiy soʻzga yopishsa — "
                       "<strong>taʼkid</strong>: «men-ku bilaman».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ уста́л, "
                "ничего́ стра́шного.</strong></p>",
        "choices": ["да́же", "про́сто", "лишь", "уж"],
        "correct": "про́сто",
        "explanation": "<p><strong>Про́сто</strong> = «shunchaki» — sababni "
                       "kichraytiradi, tinchlantiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Вот и всё.</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Mana, hammasi — tugadi", "Bu hammasi emas",
                    "Nima boʻpti?", "Mayli boʻlmasa"],
        "correct": "Mana, hammasi — tugadi",
        "explanation": "<p><em>Вот и всё</em> ishni yakunlaydi. <em>Ну и "
                       "что?</em> — «nima boʻpti», <em>ну ла́дно</em> — "
                       "«mayli boʻlmasa».</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Же</strong> gapda "
                "qayerda turadi?</p>",
        "choices": ["Gap boshida", "Gap oxirida",
                    "Taʼkidlanayotgan soʻzdan keyin", "Feʼldan oldin"],
        "correct": "Taʼkidlanayotgan soʻzdan keyin",
        "explanation": "<p><em>Я <strong>же</strong> говори́л</em> · <em>Ты "
                       "<strong>же</strong> зна́ешь</em>. Oʻzbekcha "
                       "<em>-ku</em> ham xuddi shu soʻzga yopishadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ра́зве</strong> "
                "bilan <strong>неуже́ли</strong> ning farqi nimada?</p>",
        "choices": ["Farqi yoʻq",
                    "«Ра́зве» yumshoqroq, «неуже́ли» kuchliroq hayrat",
                    "«Ра́зве» faqat yozma nutqda",
                    "«Неуже́ли» faqat inkor gaplarda"],
        "correct": "«Ра́зве» yumshoqroq, «неуже́ли» kuchliroq hayrat",
        "explanation": "<p><em>Ра́зве он уе́хал?</em> — «rostdanmi?», men "
                       "boshqacha oʻylagandim. <em>Неуже́ли пра́вда?</em> — "
                       "«nahotki», ishonishim qiyin.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ты же зна́ешь.", "Же ты зна́ешь.",
                    "Ведь ты зна́ешь.", "Ты ведь зна́ешь."],
        "correct": "Же ты зна́ешь.",
        "explanation": "<p><strong>Же gapni boshlamaydi.</strong> "
                       "<em>Ведь</em> esa boshlashi mumkin — ana shu ularning "
                       "farqi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«axir»</strong> "
                "ruschada nimaga tushadi?</p>",
        "choices": ["то́лько", "да́же", "ведь yoki же", "лишь"],
        "correct": "ведь yoki же",
        "explanation": "<p>Ikkalasi ham «axir, oʻzing bilasan» maʼnosini "
                       "beradi. <em>Ведь</em> yumshoqroq, <em>же</em> "
                       "taʼkidliroq.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gap tabiiy eshitiladi?</p>",
        "choices": ["Ну вот я же ведь про́сто уж говори́л же!",
                    "Я же говори́л!",
                    "Же говори́л я!",
                    "Говори́л я же ведь!"],
        "correct": "Я же говори́л!",
        "explanation": "<p>Bitta gapda <strong>bitta</strong> yuklama yetarli. "
                       "Koʻp qoʻyilsa, gap gʻalati va sunʼiy "
                       "eshitiladi.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Неуже́ли он придёт ли?", "Неуже́ли он придёт?",
                    "Придёт ли он?", "Ра́зве он придёт?"],
        "correct": "Неуже́ли он придёт ли?",
        "explanation": "<p><em>Неуже́ли</em> va <em>ли</em> (PR-68) birga "
                       "ishlatilmaydi — ikkalasi ham savolni belgilaydi, "
                       "bittasi yetarli.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Я забы́л "
                "ключи́.</strong></p>",
        "choices": ["— Ну вот… Я же тебе́ говори́л.", "— Вот и всё, я же тебе́ говори́л.",
                    "— Неуже́ли, я же тебе́ говори́л.", "— То́лько я тебе́ говори́л же."],
        "correct": "— Ну вот… Я же тебе́ говори́л.",
        "explanation": "<p><em>Ну вот…</em> — «mana koʻrdingmi», «men "
                       "aytgandim» maʼnosida. Undan keyin <em>же</em> bilan "
                       "eslatish juda tabiiy chiqadi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Axir sen uni "
                "bilasan-ku. Hatto men ham bilaman.</strong></p>",
        "choices": ["Ты ли его́ зна́ешь. То́лько я зна́ю.",
                    "Же ты его́ зна́ешь. Да́же я зна́ю.",
                    "Ты его́ зна́ешь ведь. Про́сто я зна́ю.",
                    "Ты же его́ зна́ешь. Да́же я зна́ю."],
        "correct": "Ты же его́ зна́ешь. Да́же я зна́ю.",
        "explanation": "<p>«Axir…-ku» → <em>же</em> (yoki <em>ведь</em>), va u "
                       "gapni boshlamaydi. «Hatto» → <em>да́же</em>, va u "
                       "taʼkidlanayotgan soʻzdan <strong>oldin</strong> "
                       "turadi.</p>",
    },
]


# =====================================================================
# PR-85 — Jonli soʻzlashuv
# =====================================================================

Q_PR85 = [
    # 1–5 tanish
    {
        "text": "<p>Bu qanday yoziladi?</p><p><strong>[щас]</strong></p>",
        "choices": ["щас", "счас", "сейча́с", "сича́с"],
        "correct": "сейча́с",
        "explanation": "<p>Ogʻzaki nutqda ikki boʻgʻin bittaga siqiladi, lekin "
                       "yozganda har doim toʻliq shakl — "
                       "<strong>сейча́с</strong>.</p>",
    },
    {
        "text": "<p>Bu qanday yoziladi?</p><p><strong>[здра́сьте]</strong></p>",
        "choices": ["здра́вствуйте", "здра́сьте", "здра́ствуйте", "здравству́йте"],
        "correct": "здра́вствуйте",
        "explanation": "<p>Kundalik nutqda [здра́сьте] deyiladi, lekin rasmiy "
                       "holatda va yozganda — <strong>здра́вствуйте</strong>, "
                       "toʻliq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Doʻstingiz telefonda "
                "«<strong>Ну всё, дава́й!</strong>» dedi. Nima demoqchi?</p>",
        "choices": ["Menga ber", "Xayr!", "Boshla", "Kutib tur"],
        "correct": "Xayr!",
        "explanation": "<p><em>Дава́й</em> bu yerda «ber» emas, "
                       "<strong>norasmiy xayrlashuv</strong>. Javoban siz ham "
                       "<em>«Дава́й, пока́!»</em> deysiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Коро́че</strong> "
                "nutqda nimani bildiradi?</p>",
        "choices": ["Qisqaroq oʻlchamda", "Tezroq", "Qisqasi", "Keyinroq"],
        "correct": "Qisqasi",
        "explanation": "<p>Soʻzma-soʻz «qisqaroq» (qiyosiy daraja, PR-74), "
                       "lekin nutqda u uzun hikoyani yakunlaydi: "
                       "<em>Коро́че, мы опозда́ли</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ogʻzaki qisqarishlarni "
                "([щас], [што]) qayerda yozish mumkin?</p>",
        "choices": ["Ish xatida", "Xabarda", "Deyarli hech qayerda — faqat badiiy dialogda",
                    "Har joyda"],
        "correct": "Deyarli hech qayerda — faqat badiiy dialogda",
        "explanation": "<p>Bu shakllar faqat ogʻzaki. Xat yoki ishdagi "
                       "yozishmada <s>щас</s> deb yozish savodsizlik belgisi. "
                       "Yagona istisno — badiiy matndagi dialog.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Javob bering.</p><p><strong>— Извини́, я разби́л твою́ "
                "ча́шку.</strong></p>",
        "choices": ["— Дава́й!", "— Коро́че.", "— То́чно!", "— Ничего́!"],
        "correct": "— Ничего́!",
        "explanation": "<p><em>Ничего́!</em> yoki <em>Ничего́ "
                       "стра́шного</em> — «Hechqisi yoʻq» (PR-79). Uzr "
                       "soʻraganga eng koʻp beriladigan javob.</p>",
    },
    {
        "text": "<p>Javob bering.</p><p><strong>— Я вчера́ встре́тил Афсо́ну "
                "в Москве́!</strong></p>",
        "choices": ["— Договори́лись.", "— Я́сно.", "— Да ла́дно! Серьёзно?", "— Вот и всё."],
        "correct": "— Да ла́дно! Серьёзно?",
        "explanation": "<p>Hayratni bildiradigan javob: <em>Да ла́дно!</em> "
                       "(«Qoʻysang-chi!») yoki <em>Ничего́ себе́!</em> "
                       "(«Voy-boʻy!»).</p>",
    },
    {
        "text": "<p>Koʻchada notanish odamdan yoʻl soʻramoqchisiz. Qaysi biri "
                "yaxshiroq?</p>",
        "choices": ["Где вокза́л?", "Скажи́ где вокза́л.",
                    "Вокза́л где?", "Извини́те, вы не подска́жете, где вокза́л?"],
        "correct": "Извини́те, вы не подска́жете, где вокза́л?",
        "explanation": "<p>Birinchisi grammatik toʻgʻri, lekin quruq "
                       "eshitiladi. <em>Извини́те</em> va inkor shakli "
                       "(<em>не подска́жете</em>) soʻrovni "
                       "yumshatadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— ___, а ты "
                "за́втра свобо́ден?</strong> (yangi mavzu boshlanyapti)</p>",
        "choices": ["Коро́че", "Слу́шай", "Вот и всё", "Договори́лись"],
        "correct": "Слу́шай",
        "explanation": "<p><strong>Слу́шай</strong> — «eshit, qara», yangi mavzu "
                       "boshlashda ishlatiladi. <em>Коро́че</em> esa aksincha, "
                       "yakunlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Договори́лись.</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Kelishdik.", "Gaplashdik.", "Xayr.", "Tushunarli."],
        "correct": "Kelishdik.",
        "explanation": "<p>Rejani tasdiqlaydi: <em>— За́втра в семь? — "
                       "Договори́лись.</em> «Tushunarli» esa "
                       "<em>Я́сно</em>.</p>",
    },
    {
        "text": "<p>Rasmiy idorada nima deysiz?</p>",
        "choices": ["Здра́сьте!", "Приве́т!", "Здра́вствуйте!", "Дава́й!"],
        "correct": "Здра́вствуйте!",
        "explanation": "<p>Rasmiy holatda toʻliq shakl. <em>Приве́т</em> va "
                       "<em>дава́й</em> faqat doʻstlar bilan, [здра́сьте] esa "
                       "aytiladi-yu, yozilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>— ___, так. "
                "Снача́ла в банк, пото́м на по́чту.</strong></p>",
        "choices": ["Зна́чит", "Да ла́дно", "Ничего́ себе́", "Пока́"],
        "correct": "Зна́чит",
        "explanation": "<p><strong>Зна́чит</strong> = «demak» — tushuntirish "
                       "yoki rejani boshlashda. Kundalik nutqda juda koʻp "
                       "eshitiladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega oʻzbek oʻquvchisi "
                "ruscha qisqarishlardan qoʻrqmasligi kerak?</p>",
        "choices": ["Chunki ular kam uchraydi",
                    "Chunki oʻzbekchada ham shunday: kelayapti → kevotti",
                    "Chunki ularni yozib boʻladi",
                    "Chunki ular faqat Moskvada ishlatiladi"],
        "correct": "Chunki oʻzbekchada ham shunday: kelayapti → kevotti",
        "explanation": "<p>Har ikkala tilda ham tez gapirganda soʻz siqiladi, "
                       "lekin yozilishi oʻzgarmaydi. Vazifa — tanib olish, "
                       "ishlatish shart emas.</p>",
    },
    {
        "text": "<p>Qaysi juftlik notoʻgʻri?</p>",
        "choices": ["Приве́т — Пока́", "Здра́вствуйте — До свида́ния",
                    "Приве́т — Дава́й", "Здра́вствуйте — Дава́й"],
        "correct": "Здра́вствуйте — Дава́й",
        "explanation": "<p><em>Здра́вствуйте</em> rasmiy, <em>дава́й</em> esa "
                       "norasmiy — ular bir suhbatda uchrashmaydi. "
                       "Direktorga <em>«Дава́й!»</em> deb boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ничего́ себе́!</strong> "
                "iborasini qanday yodlash kerak?</p>",
        "choices": ["Soʻzma-soʻz tarjima qilib", "Butun holda — u hayrat undovi",
                    "Faqat inkor gaplarda", "Grammatik tahlil qilib"],
        "correct": "Butun holda — u hayrat undovi",
        "explanation": "<p>Soʻzma-soʻz «oʻziga hech narsa» degani va bu hech "
                       "narsani tushuntirmaydi. U shunchaki «Voy-boʻy!» — "
                       "butun holda yodlanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha <strong>«xoʻp, "
                "boʻpti, mayli»</strong> ruschada koʻpincha nimaga tushadi?</p>",
        "choices": ["коро́че", "ла́дно", "зна́чит", "то́чно"],
        "correct": "ла́дно",
        "explanation": "<p>Uchala oʻzbekcha soʻz ham bitta <strong>ла́дно</strong> "
                       "ga yigʻiladi: <em>Ну ла́дно</em> — «mayli "
                       "boʻlmasa».</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Bu gaplar <strong>yozma</strong> xabarda ishlatilgan. "
                "Qaysi birida xato bor?</p>",
        "choices": ["Я сейча́с приду́.",
                    "Здра́вствуйте, я хочу́ пода́ть заявле́ние.",
                    "Приве́т! Ну что, идём?",
                    "Я щас приду́."],
        "correct": "Я щас приду́.",
        "explanation": "<p>[щас] — faqat ogʻzaki shakl. Yozganda "
                       "<strong>сейча́с</strong>.</p>",
    },
    {
        "text": "<p>Qaysi javob rasmiy holatga toʻgʻri kelmaydi?</p>",
        "choices": ["До свида́ния.", "Всего́ до́брого.", "Дава́й!", "Спаси́бо, до свида́ния."],
        "correct": "Дава́й!",
        "explanation": "<p><em>Дава́й</em> faqat doʻstlar va tengdoshlar bilan. "
                       "Rasmiy holatda <em>до свида́ния</em> yoki <em>всего́ "
                       "до́брого</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi suhbat tabiiy?</p>",
        "choices": ["— Приве́т! — Здра́вствуйте, до свида́ния.",
                    "— Приве́т! Ну что, идём? — Ну ла́дно, дава́й.",
                    "— Здра́сьте! — Дава́й, пока́, всего́ до́брого.",
                    "— Приве́т! — Коро́че, я́сно, договори́лись."],
        "correct": "— Приве́т! Ну что, идём? — Ну ла́дно, дава́й.",
        "explanation": "<p>Ikkala tomon ham <strong>norasmiy</strong> uslubda va "
                       "iboralar oʻz oʻrnida. Qolgan variantlarda rasmiy va "
                       "norasmiy shakllar aralashib ketgan.</p>",
    },
    {
        "text": "<p>Bu suhbatning ruschasi qaysi biri?</p><p><strong>— Qisqasi, "
                "poyezdga kechikdik. — Voy-boʻy! Hechqisi yoʻq, ertaga "
                "borasizlar.</strong></p>",
        "choices": ["— Коро́че, мы опозда́ли на по́езд. — Ничего́ себе́! Ничего́, за́втра пое́дете.",
                    "— Дава́й, мы опозда́ли на по́езд. — Я́сно! Коро́че, за́втра пое́дете.",
                    "— Зна́чит, мы опозда́ли на по́езд. — Договори́лись! Ничего́, за́втра пое́дете.",
                    "— Слу́шай, мы опозда́ли на по́езд. — Пока́! Ничего́, за́втра пое́дете."],
        "correct": "— Коро́че, мы опозда́ли на по́езд. — Ничего́ себе́! Ничего́, за́втра пое́дете.",
        "explanation": "<p>«Qisqasi» → <em>коро́че</em>, «Voy-boʻy!» → "
                       "<em>Ничего́ себе́!</em>, «Hechqisi yoʻq» → "
                       "<em>Ничего́</em>. Uchalasi ham oʻz oʻrnida.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-83 Mashq: Predlog xaritasi 2",
        "description": (
            "Несмотря́ на = oʻzbekcha «qaramay». По ning oltita maʼnosi, за ning "
            "ikki kelishigi va из-за / благодаря́ / несмотря́ на uchligi."
        ),
        "tutorial": "PR-83:",
        "questions": Q_PR83,
    },
    {
        "title": "PR-84 Mashq: Yuklamalar (частицы)",
        "description": (
            "Же = «-ku», неуже́ли = «nahotki». Ведь, ра́зве, да́же, то́лько va "
            "taʼkid uchun ishlatiladigan -то."
        ),
        "tutorial": "PR-84:",
        "questions": Q_PR84,
    },
    {
        "title": "PR-85 Mashq: Jonli soʻzlashuv nutqi",
        "description": (
            "Yozilishi va aytilishi: сейча́с → [щас]. Коро́че, слу́шай, "
            "Да ла́дно!, Ничего́ себе́! va «Дава́й!» — xayr maʼnosida."
        ),
        "tutorial": "PR-85:",
        "questions": Q_PR85,
    },
]
