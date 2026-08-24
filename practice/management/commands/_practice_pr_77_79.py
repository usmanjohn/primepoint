# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-77 … PR-79.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_77_79.py --master=prime \\
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
# PR-77 — Каждый, все, весь, любой, другой
# =====================================================================

Q_PR77 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я хожу́ туда́ ___ "
                "день.</strong> (har kuni)</p>",
        "choices": ["весь", "всё", "любо́й", "ка́ждый"],
        "correct": "ка́ждый",
        "explanation": "<p>«Har kuni» — <strong>takror</strong>, demak "
                       "<em>ка́ждый день</em>. <em>Весь день</em> «kun boʻyi» "
                       "degan boshqa maʼno berardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он рабо́тал ___ "
                "день и о́чень уста́л.</strong> (kun boʻyi)</p>",
        "choices": ["ка́ждый", "любо́й", "весь", "друго́й"],
        "correct": "весь",
        "explanation": "<p>«Kun boʻyi» — <strong>bitta uzluksiz boʻlak</strong>, "
                       "demak <em>весь день</em>. Savol: «necha marta?» emas, "
                       "«qancha vaqt?».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ гото́во, "
                "мо́жно начина́ть.</strong></p>",
        "choices": ["Все", "Весь", "Вся", "Всё"],
        "correct": "Всё",
        "explanation": "<p>Feʼl <em>гото́во</em> — birlik, oʻrta jins, demak "
                       "gap <strong>hamma narsa</strong> haqida: "
                       "<strong>Всё</strong>. <em>Все гото́вы</em> «hamma "
                       "tayyor» (odamlar) boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ка́ждый</strong> "
                "qaysi sonda ishlatiladi?</p>",
        "choices": ["Faqat koʻplikda", "Faqat birlikda", "Ikkalasida ham",
                    "Faqat oʻrta jinsda"],
        "correct": "Faqat birlikda",
        "explanation": "<p><em>Ка́ждый студе́нт</em>, <em>ка́ждая кни́га</em> — "
                       "har doim birlik. <s>Ка́ждые студе́нты</s> deyilmaydi; "
                       "koʻplik uchun <strong>все</strong> ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Любо́й</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Har bir, birma-bir", "Qolganlari", "Butun, boshdan-oxir",
                    "Istalgan, qaysi biri boʻlsa ham"],
        "correct": "Istalgan, qaysi biri boʻlsa ham",
        "explanation": "<p><em>Возьми́ <strong>любу́ю</strong> кни́гу</em> — "
                       "«istalgan kitobni ol». <em>Ка́ждый</em> esa "
                       "«hammasi birma-bir» degani.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он рабо́тал ___ "
                "ночь.</strong> (весь)</p>",
        "choices": ["весь", "всей", "всю", "всё"],
        "correct": "всю",
        "explanation": "<p><em>Ночь</em> — ayol jinsida, vaqt davomiyligi "
                       "Вини́тельный bilan beriladi (PR-49): "
                       "<strong>всю ночь</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Спаси́бо ___ за "
                "по́мощь!</strong> (весь, koʻplik)</p>",
        "choices": ["всех", "все", "все́ми", "всем"],
        "correct": "всем",
        "explanation": "<p><em>Спаси́бо <strong>кому́?</strong></em> — "
                       "Да́тельный, koʻplik: <strong>всем</strong>. "
                       "«Hammaga rahmat!»</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы говори́ли ___ "
                "два часа́.</strong> (hamma narsa haqida)</p>",
        "choices": ["о всех", "обо всём", "о все", "обо всей"],
        "correct": "обо всём",
        "explanation": "<p>Предло́жный, oʻrta jins: <strong>обо всём</strong>. "
                       "Diqqat — predlog <em>о</em> emas, <em>обо</em> "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Restoranda choy yoqmadi. Nima deysiz?</p>",
        "choices": ["Принеси́те ещё оди́н чай.", "Принеси́те ка́ждый чай.",
                    "Принеси́те весь чай.", "Принеси́те друго́й чай."],
        "correct": "Принеси́те друго́й чай.",
        "explanation": "<p>«Boshqa» — <strong>друго́й</strong>. <em>Ещё оди́н "
                       "чай</em> desangiz, xuddi shunaqasidan yana bitta "
                       "keltiriladi.</p>",
    },
    {
        "text": "<p>Choy yoqdi, yana xohladingiz. Nima deysiz?</p>",
        "choices": ["Принеси́те друго́й чай.", "Принеси́те ещё оди́н чай.",
                    "Принеси́те любо́й чай.", "Принеси́те остально́й чай."],
        "correct": "Принеси́те ещё оди́н чай.",
        "explanation": "<p>«Yana bitta» — <strong>ещё оди́н</strong>, xuddi "
                       "shunaqasidan. <em>Друго́й</em> desangiz, birinchisini "
                       "olib ketishadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Три студе́нта "
                "оста́лись, ___ ушли́.</strong></p>",
        "choices": ["остально́е", "все", "остальны́е", "любы́е"],
        "correct": "остальны́е",
        "explanation": "<p><strong>Остальны́е</strong> — «qolganlar» (odamlar, "
                       "koʻplik). <em>Остально́е</em> esa «qolgan qism» (oʻrta "
                       "jins).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Приходи́ в ___ "
                "вре́мя, я всегда́ до́ма.</strong></p>",
        "choices": ["ка́ждое", "всё", "друго́е", "любо́е"],
        "correct": "любо́е",
        "explanation": "<p>«Istalgan vaqtda» — <strong>в любо́е вре́мя</strong>. "
                       "Bu tayyor ibora va uni yodlab olish kerak.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Ка́ждый день · "
                "весь день</strong></p>",
        "choices": ["Birinchisi takror, ikkinchisi davomiylik",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi koʻplik",
                    "Farqi yoʻq"],
        "correct": "Birinchisi takror, ikkinchisi davomiylik",
        "explanation": "<p><em>Ка́ждый день</em> = «har kuni» (necha marta?). "
                       "<em>Весь день</em> = «kun boʻyi» (qancha vaqt?). "
                       "Oʻzbekchada ham shu ikki ibora bor.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>все</strong> (е bilan) kerak?</p>",
        "choices": ["___ гото́во к экза́мену.", "Я ___ по́нял.",
                    "___ уже́ пришли́ и ждут.", "___ бы́ло о́чень вку́сно."],
        "correct": "___ уже́ пришли́ и ждут.",
        "explanation": "<p>Feʼl <em>пришли́</em> — koʻplikda, demak gap "
                       "<strong>odamlar</strong> haqida: <em>Все уже́ "
                       "пришли́</em>. Qolgan uchtasida feʼl birlikda — "
                       "<strong>всё</strong> kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ка́ждый</strong> "
                "bilan <strong>любо́й</strong> ning farqi nimada?</p>",
        "choices": ["«Ка́ждый» koʻplik, «любо́й» birlik",
                    "«Ка́ждый» — hammasi, «любо́й» — istalgan bittasi",
                    "«Любо́й» faqat savolda ishlatiladi",
                    "Farqi umuman yoʻq"],
        "correct": "«Ка́ждый» — hammasi, «любо́й» — istalgan bittasi",
        "explanation": "<p><em>Ка́ждый студе́нт получи́л кни́гу</em> — hammasi "
                       "oldi. <em>Возьми́ любу́ю кни́гу</em> — bittasini ol, "
                       "qaysi biri boʻlsa ham.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Пре́жде "
                "всего́</strong> nimani bildiradi?</p>",
        "choices": ["Oxirida", "Har holda", "Hammasi birga", "Avvalo"],
        "correct": "Avvalo",
        "explanation": "<p><em>Пре́жде всего́</em> — «avvalo, eng birinchi "
                       "navbatda». <em>В любо́м слу́чае</em> esa «har "
                       "holda».</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ка́ждые студе́нты пришли́.", "Все студе́нты пришли́.",
                    "Ка́ждый студе́нт пришёл.", "Весь класс пришёл."],
        "correct": "Ка́ждые студе́нты пришли́.",
        "explanation": "<p><em>Ка́ждый</em> koʻplikda ishlatilmaydi. Koʻplik "
                       "uchun <strong>все</strong>: <em>все студе́нты "
                       "пришли́</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Все гото́во, начина́ем.", "Всё гото́вы, начина́ем.",
                    "Всё гото́во, начина́ем.", "Весь гото́во, начина́ем."],
        "correct": "Всё гото́во, начина́ем.",
        "explanation": "<p>«Hamma narsa tayyor» — <strong>всё</strong> (oʻrta "
                       "jins, birlik) va feʼl ham birlikda: "
                       "<strong>гото́во</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Ты ходи́л в бассе́йн "
                "в э́том году́?</strong></p>",
        "choices": ["— Да, ка́ждое у́тро, весь год.", "— Да, весь у́тро, ка́ждый год.",
                    "— Да, все у́тро, всё год.", "— Да, любо́е у́тро, друго́й год."],
        "correct": "— Да, ка́ждое у́тро, весь год.",
        "explanation": "<p><em>Ка́ждое у́тро</em> — takror (har ertalab), "
                       "<em>весь год</em> — davomiylik (yil boʻyi). Bitta "
                       "javobda ikkala soʻz ham oʻz oʻrnida.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Har kuni bir "
                "xil edi. Yil boʻyi esa — yoʻq.</strong></p>",
        "choices": ["Весь день был одина́ковым. А ка́ждый год — нет.",
                    "Ка́ждый день был одина́ковым. А весь год — нет.",
                    "Все дни был одина́ковым. А всё год — нет.",
                    "Любо́й день был одина́ковым. А друго́й год — нет."],
        "correct": "Ка́ждый день был одина́ковым. А весь год — нет.",
        "explanation": "<p><em>Ка́ждый день</em> takrorni, <em>весь год</em> "
                       "butun davrni bildiradi. <em>А</em> ishlatilgan, chunki "
                       "bu solishtirish (PR-67).</p>",
    },
]


# =====================================================================
# PR-78 — Noaniq olmoshlar
# =====================================================================

Q_PR78 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>-то</strong> "
                "zarrachasi nimani bildiradi?</p>",
        "choices": ["Odam yoʻq", "Kim boʻlsa ham, farqi yoʻq",
                    "Bilaman, lekin aytmayman", "Odam bor, lekin kimligi nomaʼlum"],
        "correct": "Odam bor, lekin kimligi nomaʼlum",
        "explanation": "<p><em>Кто́-то звони́л</em> — qoʻngʻiroq qilgan odam "
                       "<strong>bor</strong>, faqat biz kimligini "
                       "bilmaymiz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ звони́л, пока́ "
                "тебя́ не́ было.</strong></p>",
        "choices": ["Кто́-нибудь", "Ко́е-кто", "Кто́-то", "Никто́"],
        "correct": "Кто́-то",
        "explanation": "<p>Bu <strong>xabar</strong> va voqea allaqachon "
                       "boʻlgan, demak <em>-то</em>. Savol boʻlganda "
                       "<em>-нибудь</em> kelardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ звони́л?</strong> "
                "(savol)</p>",
        "choices": ["Кто́-то", "Кто́-нибудь", "Ко́е-кто", "Никто́"],
        "correct": "Кто́-нибудь",
        "explanation": "<p><strong>Savolda har doim -нибудь.</strong> Chunki "
                       "qoʻngʻiroq boʻlgan-boʻlmagani hali nomaʼlum.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ко́е-кто</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Hech kim", "Hamma", "Kim boʻlsa ham",
                    "Bir kishi — soʻzlovchi biladi, lekin aytmayapti"],
        "correct": "Bir kishi — soʻzlovchi biladi, lekin aytmayapti",
        "explanation": "<p><em>Ко́е-кто мне сказа́л</em> — «bir kishi menga "
                       "aytdi». <em>Кто́-то</em> dan farqi: bu yerda men "
                       "bilaman, siz bilmaysiz.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu zarrachalar qanday "
                "yoziladi?</p>",
        "choices": ["Defis bilan", "Alohida", "Qoʻshib", "Qavs ichida"],
        "correct": "Defis bilan",
        "explanation": "<p><em>кто́-то, что́-нибудь, ко́е-кто</em> — uchalasi "
                       "ham <strong>defis</strong> bilan. Yagona istisno — "
                       "<em>ко́е-</em> predlog bilan kelganda: <em>ко́е с "
                       "кем</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Расскажи́ нам ___ "
                "интере́сное.</strong> (buyruq)</p>",
        "choices": ["что́-то", "ко́е-что", "ничего́", "что́-нибудь"],
        "correct": "что́-нибудь",
        "explanation": "<p><strong>Buyruqda har doim -нибудь.</strong> Nima "
                       "boʻlishi farqi yoʻq — «biror qiziq narsa».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ушёл ___ и не "
                "сказа́л куда́.</strong></p>",
        "choices": ["куда́-нибудь", "никуда́", "ко́е-куда", "куда́-то"],
        "correct": "куда́-то",
        "explanation": "<p>Voqea <strong>boʻlib oʻtgan</strong> — u allaqachon "
                       "ketdi. Joy aniq bor, faqat biz bilmaymiz, demak "
                       "<em>-то</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Е́сли ___ спро́сит, "
                "скажи́, что я в библиоте́ке.</strong></p>",
        "choices": ["кто́-то", "ко́е-кто", "кто́-нибудь", "никто́"],
        "correct": "кто́-нибудь",
        "explanation": "<p><strong>Shart gapida -нибудь.</strong> Hali hech kim "
                       "soʻragani yoʻq. Oʻzbekcha «birortasi» ham shuni "
                       "koʻrsatib turibdi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>За́втра я ___ "
                "позвоню́ и всё узна́ю.</strong></p>",
        "choices": ["кому́-нибудь", "кому́-то", "ко́е-кому", "никому́"],
        "correct": "кому́-нибудь",
        "explanation": "<p><strong>Kelasi zamonda -нибудь.</strong> Kimga "
                       "qoʻngʻiroq qilishim hali hal boʻlmagan.</p>",
    },
    {
        "text": "<p>Toʻgʻri shaklni qoʻying.</p><p><strong>Она́ до́лго "
                "говори́ла ___ по телефо́ну.</strong> (кто́-то)</p>",
        "choices": ["с кто́-то", "с ке́м-то", "ке́м-то", "с ко́м-то"],
        "correct": "с ке́м-то",
        "explanation": "<p>Твори́тельный — <strong>с ке́м-то</strong>. "
                       "Zarracha oʻzgarmaydi, turlanadigan narsa — asosiy "
                       "soʻz. Predlog <em>-то</em> da oldinda qoladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri yozing.</p><p><strong>Мне ну́жно поговори́ть ___ "
                "об э́том.</strong> (ко́е-кто + с)</p>",
        "choices": ["с ко́е-кем", "ко́е-с-кем", "ко́е с кем", "ко́е-кем с"],
        "correct": "ко́е с кем",
        "explanation": "<p><strong>Ко́е-</strong> da predlog zarracha va soʻz "
                       "<strong>orasiga</strong> tushadi, uchalasi alohida "
                       "yoziladi: <em>ко́е с кем</em>, <em>ко́е о чём</em>.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Когда́-то я жил "
                "в Москве́. · Когда́-нибудь я пое́ду в Москву́.</strong></p>",
        "choices": ["Birinchisi oʻtmish, ikkinchisi kelajak",
                    "Birinchisi savol", "Ikkinchisida xato bor", "Farqi yoʻq"],
        "correct": "Birinchisi oʻtmish, ikkinchisi kelajak",
        "explanation": "<p><strong>Когда́-то</strong> — «bir paytlar» "
                       "(oʻtmishda). <strong>Когда́-нибудь</strong> — "
                       "«qachondir» (kelajakda). Bu juftlikni yodlab olish "
                       "kerak.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekcha "
                "<strong>«birorta»</strong> ruschada odatda nimaga toʻgʻri "
                "keladi?</p>",
        "choices": ["-то", "-нибудь", "ко́е-", "ни-"],
        "correct": "-нибудь",
        "explanation": "<p>«Birorta odam qoʻngʻiroq qildimi?» → <em>Кто́-нибудь "
                       "звони́л?</em> Oʻzbekcha <strong>«…dir»</strong> esa "
                       "<em>-то</em> ga toʻgʻri keladi: «kimdir» → "
                       "<em>кто́-то</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega bu gapda "
                "<strong>-нибудь</strong> turibdi?</p><p><strong>Ка́ждый день "
                "кто́-нибудь опа́здывает.</strong></p>",
        "choices": ["Chunki gap savol",
                    "Chunki har kuni boshqa odam kechikadi",
                    "Chunki gap kelasi zamonda",
                    "Bu matndagi xato"],
        "correct": "Chunki har kuni boshqa odam kechikadi",
        "explanation": "<p>Takrorlanadigan ishda odam har safar oʻzgaradi, "
                       "shuning uchun <em>-нибудь</em> keladi — garchi gap "
                       "oʻtgan yoki hozirgi zamonda boʻlsa ham.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi holatda "
                "<strong>-то</strong> ishlatiladi?</p>",
        "choices": ["Savolda", "Buyruqda", "Shart gapida", "Boʻlib oʻtgan voqea haqida"],
        "correct": "Boʻlib oʻtgan voqea haqida",
        "explanation": "<p>Savol, buyruq, kelasi zamon va shart — hammasi "
                       "<strong>-нибудь</strong> oladi. <em>-то</em> esa "
                       "allaqachon boʻlgan yoki boʻlayotgan narsa uchun.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Почему́-то</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Nega?", "Negadir", "Hech qachon", "Shuning uchun"],
        "correct": "Negadir",
        "explanation": "<p><em>Он <strong>почему́-то</strong> не "
                       "отвеча́ет</em> — «u negadir javob bermayapti». Sabab "
                       "bor, lekin biz bilmaymiz.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Позвони́ кому́-то ве́чером.", "Вчера́ кто́-то приходи́л.",
                    "Кто́-нибудь зна́ет отве́т?", "Он что́-то пи́шет."],
        "correct": "Позвони́ кому́-то ве́чером.",
        "explanation": "<p>Bu <strong>buyruq</strong>, demak "
                       "<strong>кому́-нибудь</strong> kerak. Kimga qoʻngʻiroq "
                       "qilish hali hal boʻlmagan.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я говори́л с кто́-то.", "Я говори́л ке́м-то.",
                    "Я говори́л с ке́м-то.", "Я говори́л с кого́-то."],
        "correct": "Я говори́л с ке́м-то.",
        "explanation": "<p>Predlog <em>с</em> Твори́тельный talab qiladi, va "
                       "turlanadigan narsa — asosiy soʻz: "
                       "<strong>ке́м-то</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— У тебя́ есть что́-нибудь "
                "почита́ть?</strong></p>",
        "choices": ["— Да, я тебе́ ко́е-что дам.", "— Да, я тебе́ ничего́ дам.",
                    "— Да, я тебе́ кто́-то дам.", "— Да, я тебе́ никако́й дам."],
        "correct": "— Да, я тебе́ ко́е-что дам.",
        "explanation": "<p><strong>Ко́е-что</strong> — «bir narsa bor, aniq "
                       "bilaman». Savolda <em>что́-нибудь</em> edi, javobda esa "
                       "aniq narsa paydo boʻldi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Bu yuzni "
                "qayerdadir koʻrganman.</strong></p>",
        "choices": ["Я где́-нибудь ви́дел э́то лицо́.", "Я нигде́ ви́дел э́то лицо́.",
                    "Я ко́е-где ви́дел э́то лицо́.", "Я где́-то ви́дел э́то лицо́."],
        "correct": "Я где́-то ви́дел э́то лицо́.",
        "explanation": "<p>Voqea <strong>boʻlib oʻtgan</strong> va joy bor, "
                       "faqat esimda yoʻq — demak <em>-то</em>. Oʻzbekcha "
                       "«qayerda<strong>dir</strong>» ham shuni "
                       "koʻrsatadi.</p>",
    },
]


# =====================================================================
# PR-79 — Ikki inkor
# =====================================================================

Q_PR79 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Gapda <strong>никто́</strong> "
                "boʻlsa, feʼl oldida nima turishi kerak?</p>",
        "choices": ["Hech narsa", "Ни", "Не", "Нет"],
        "correct": "Не",
        "explanation": "<p><em>Никто́ <strong>не</strong> пришёл.</em> Rus "
                       "tilida ikki inkor <strong>majburiy</strong> — xuddi "
                       "oʻzbekchada «hech kim kel<strong>ma</strong>di» "
                       "kabi.</p>",
    },
    {
        "text": "<p>Xatoni tuzating.</p><p><strong>Никто́ зна́ет "
                "отве́т.</strong></p>",
        "choices": ["Никто́ не зна́ет отве́т.", "Никто́ зна́ет не отве́т.",
                    "Не никто́ зна́ет отве́т.", "Никто́ нет зна́ет отве́т."],
        "correct": "Никто́ не зна́ет отве́т.",
        "explanation": "<p><em>Не</em> feʼlning <strong>oldiga</strong> "
                       "qoʻyiladi. Bu qoida hech qachon buzilmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Никогда́</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Hech qayerda", "Hech qanday", "Hech kim", "Hech qachon"],
        "correct": "Hech qachon",
        "explanation": "<p><em>Он <strong>никогда́</strong> не "
                       "опа́здывает</em> — «u hech qachon kechikmaydi». "
                       "«Hech qayerda» — <em>нигде́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir gapda nechta inkor soʻzi "
                "boʻlishi mumkin?</p>",
        "choices": ["Faqat bitta", "Ikkitagacha", "Uchtagacha", "Istagancha"],
        "correct": "Istagancha",
        "explanation": "<p><em>Никто́ никогда́ никому́ ничего́ не "
                       "говори́л</em> — beshta inkor, va gap "
                       "<strong>toʻgʻri</strong>. Oʻzbekchasi ham xuddi "
                       "shunday uzun.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Kundalik nutqda qaysi shakl "
                "koʻproq ishlatiladi?</p>",
        "choices": ["Ничто́", "Ничего́", "Ikkalasi teng", "Ниче́м"],
        "correct": "Ничего́",
        "explanation": "<p><strong>Ничего́</strong> — 95% holat (toʻldiruvchi "
                       "boʻlganda). <em>Ничто́</em> faqat gapning egasi "
                       "boʻlganda va kitobiy: <em>Ничто́ не ве́чно</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻgʻri yozing.</p><p><strong>Я ___ не говори́л об "
                "э́том.</strong> (никто́ + с)</p>",
        "choices": ["никем", "с нике́м", "ни с кем", "ни-с-кем"],
        "correct": "ни с кем",
        "explanation": "<p>Predlog <em>ни</em> bilan <em>кем</em> "
                       "<strong>orasiga</strong> tushadi va uchalasi "
                       "<strong>alohida</strong> yoziladi: "
                       "<em>ни с кем</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri yozing.</p><p><strong>Он ___ не ду́мает.</strong> "
                "(ничто́ + о)</p>",
        "choices": ["о ниче́м", "ни о чём", "ничём", "ни-о-чём"],
        "correct": "ни о чём",
        "explanation": "<p>Xuddi shu qoida: <strong>ни о чём</strong> — uchta "
                       "alohida soʻz. «U hech narsa haqida oʻylamaydi».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ его́ не "
                "нашёл.</strong> (hech qayerda)</p>",
        "choices": ["никуда́", "никогда́", "никако́й", "нигде́"],
        "correct": "нигде́",
        "explanation": "<p><strong>Нигде́</strong> — «hech qayerda» (joy). "
                       "<em>Никуда́</em> «hech qayerga» (yoʻnalish) degan "
                       "boshqa soʻz.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ не пошли́, "
                "оста́лись до́ма.</strong></p>",
        "choices": ["нигде́", "никуда́", "никогда́", "ниче́м"],
        "correct": "никуда́",
        "explanation": "<p>Bu <strong>yoʻnalish</strong> — «hech qayerga "
                       "bormadik», demak <em>никуда́</em>. <em>Нигде́</em> "
                       "joyni bildiradi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я ничего́ не "
                "де́лаю. · Мне не́чего де́лать.</strong></p>",
        "choices": ["Farqi yoʻq",
                    "Birinchisi «qilmayapman», ikkinchisi «qiladigan ish yoʻq»",
                    "Ikkinchisida xato bor",
                    "Birinchisi kelasi zamon"],
        "correct": "Birinchisi «qilmayapman», ikkinchisi «qiladigan ish yoʻq»",
        "explanation": "<p><strong>Ни-</strong> (urgʻusiz) inkor qiladi. "
                       "<strong>Не́-</strong> (urgʻuli) imkoniyat yoʻqligini "
                       "bildiradi va infinitiv bilan keladi; odam esa "
                       "Да́тельный da turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ему́ ___ "
                "помо́чь — все уе́хали.</strong></p>",
        "choices": ["никто́ не", "ничего́", "никого́", "не́кому"],
        "correct": "не́кому",
        "explanation": "<p>«Yordam beradigan odam yoʻq» — imkoniyat yoʻqligi, "
                       "demak <strong>не́кому</strong> + infinitiv. "
                       "<em>Никто́ не помо́г</em> «hech kim yordam bermadi» "
                       "degan boshqa gap boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ни за что!</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Hechqisi yoʻq", "Aslo!", "Bir narsa uchun", "Hech narsa haqida"],
        "correct": "Aslo!",
        "explanation": "<p><em>Ни за что!</em> — qatʼiy rad javob. "
                       "«Hechqisi yoʻq» esa <em>Ничего́ стра́шного</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Rus tilidagi ikki inkor "
                "qoidasi oʻzbek tiliga qanday tushadi?</p>",
        "choices": ["Oʻzbekchada ham ikki belgi bor: «hech kim kelmadi»",
                    "Oʻzbekchada faqat bitta belgi boʻladi",
                    "Oʻzbekchada bunday qurilish yoʻq",
                    "Oʻzbekchada uchta belgi boʻladi"],
        "correct": "Oʻzbekchada ham ikki belgi bor: «hech kim kelmadi»",
        "explanation": "<p>«Hech kim» soʻzida va feʼldagi "
                       "<strong>-ma-</strong> qoʻshimchasida — ikkita belgi, "
                       "xuddi ruschadagi <em>никто́</em> va <em>не</em> "
                       "kabi. Shuning uchun bu dars oʻzbek oʻquvchisiga "
                       "oson.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ни-</strong> bilan "
                "<strong>не́-</strong> ni qanday ajratasiz?</p>",
        "choices": ["Yozilishiga qarab", "Jinsiga qarab", "Soniga qarab",
                    "Urgʻuga qarab: ни urgʻu olmaydi, не́ har doim oladi"],
        "correct": "Urgʻuga qarab: ни urgʻu olmaydi, не́ har doim oladi",
        "explanation": "<p><em>ничего́</em> — urgʻu oxirida. <em>не́чего</em> — "
                       "urgʻu boshida. Maʼnosi ham boshqa: biri inkor, "
                       "ikkinchisi imkoniyat yoʻqligi.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>ничто́</strong> (ничего́ emas) "
                "toʻgʻri?</p>",
        "choices": ["Я ___ не по́нял.", "Он ___ не бои́тся.",
                    "___ не ве́чно в э́том ми́ре.", "Мы ___ не купи́ли."],
        "correct": "___ не ве́чно в э́том ми́ре.",
        "explanation": "<p>Faqat shu gapda soʻz <strong>ega</strong> oʻrnida "
                       "turibdi, demak Имени́тельный — <em>Ничто́ не "
                       "ве́чно</em>. Qolganlarida toʻldiruvchi, demak "
                       "<em>ничего́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Kimdir oyogʻingizni bosib "
                "uzr soʻradi. Nima deysiz?</p>",
        "choices": ["Ни за что!", "Никогда́!", "Ничего́ подо́бного.",
                    "Ничего́ стра́шного."],
        "correct": "Ничего́ стра́шного.",
        "explanation": "<p><em>Ничего́!</em> yoki <em>Ничего́ "
                       "стра́шного</em> — «hechqisi yoʻq». Bu rus tilidagi "
                       "eng koʻp eshitiladigan javoblardan biri.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Никто́ не пришёл.", "Я ничего́ зна́ю.",
                    "Он никогда́ не спо́рит.", "Мы никуда́ не пошли́."],
        "correct": "Я ничего́ зна́ю.",
        "explanation": "<p><em>Не</em> tushib qolgan. Toʻgʻrisi — <strong>Я "
                       "ничего́ не зна́ю</strong>. Ikki inkor "
                       "majburiy.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri yozilgan?</p>",
        "choices": ["Я никем не говори́л.", "Я с нике́м не говори́л.",
                    "Я ни с кем не говори́л.", "Я ни-с-кем не говори́л."],
        "correct": "Я ни с кем не говори́л.",
        "explanation": "<p>Predlog soʻzni ikkiga boʻladi va uchalasi alohida "
                       "yoziladi: <strong>ни с кем</strong>. Feʼl oldida esa "
                       "<em>не</em> saqlanadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Hech kim "
                "hech qachon hech narsa soʻramadi.</strong></p>",
        "choices": ["Никто́ никогда́ ничего́ спроси́л.",
                    "Кто́-то когда́-то что́-то не спроси́л.",
                    "Никто́ никогда́ ничего́ не спроси́л.",
                    "Никто́ не никогда́ не ничего́ не спроси́л."],
        "correct": "Никто́ никогда́ ничего́ не спроси́л.",
        "explanation": "<p>Uchta inkor soʻzi va <strong>bitta</strong> "
                       "<em>не</em> feʼl oldida. <em>Не</em> har bir soʻzdan "
                       "oldin takrorlanmaydi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Menda "
                "qiladigan ish yoʻq edi.</strong></p>",
        "choices": ["Я ничего́ не де́лал.", "Мне ничего́ де́лать.",
                    "Мне не́чего бы́ло де́лать.", "Мне не́чего не де́лал."],
        "correct": "Мне не́чего бы́ло де́лать.",
        "explanation": "<p>«Qiladigan ish yoʻq» — imkoniyat yoʻqligi, demak "
                       "<strong>не́чего</strong> + infinitiv, odam esa "
                       "Да́тельный da: <em>мне</em>. Birinchi variant «hech "
                       "narsa qilmadim» degan boshqa maʼno.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-77 Mashq: Каждый, все, весь, любой, другой",
        "description": (
            "«Har kuni» ↔ «kun boʻyi» = ка́ждый день ↔ весь день. Bir harf farq: "
            "все (odamlar) ↔ всё (narsalar). Plus любо́й va ещё оди́н ↔ друго́й."
        ),
        "tutorial": "PR-77:",
        "questions": Q_PR77,
    },
    {
        "title": "PR-78 Mashq: Кто-то / кто-нибудь / кое-кто",
        "description": (
            "-то — voqea boʻlgan; -нибудь — savol, buyruq, kelasi zamon, shart; "
            "ко́е- — bilaman, aytmayman. Plus turlanish va ко́е с кем."
        ),
        "tutorial": "PR-78:",
        "questions": Q_PR78,
    },
    {
        "title": "PR-79 Mashq: Ikki inkor — никто, ничего, никогда",
        "description": (
            "Ни- soʻzi bor joyda feʼl oldida «не» shart — xuddi oʻzbekchadagi "
            "«hech kim kelmadi» kabi. Plus ни с кем va не́чего де́лать."
        ),
        "tutorial": "PR-79:",
        "questions": Q_PR79,
    },
]
