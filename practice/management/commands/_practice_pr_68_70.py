# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-68 … PR-70.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_68_70.py --master=prime \\
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
# PR-68 — Ли va bilvosita savol
# =====================================================================

Q_PR68 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ruscha <strong>ли</strong> "
                "oʻzbekchadagi nimaga toʻgʻri keladi?</p>",
        "choices": ["«agar»", "«-mi»", "«-ki»", "«esa»"],
        "correct": "«-mi»",
        "explanation": "<p><strong>Ли</strong> — savol zarrachasi, oʻzbekcha "
                       "<strong>-mi</strong> ning aynan oʻzi: <em>Придёт "
                       "ли он?</em> = «Keladimi?». «Agar» — bu <em>е́сли</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ли</strong> gapda "
                "qayerda turadi?</p>",
        "choices": ["Gapning eng oxirida", "Har doim birinchi soʻz sifatida",
                    "Soʻralayotgan soʻzdan keyin", "Feʼldan oldin"],
        "correct": "Soʻralayotgan soʻzdan keyin",
        "explanation": "<p><em>Ли</em> hech qachon birinchi soʻz boʻlmaydi. U "
                       "soʻralayotgan soʻzning orqasida turadi — xuddi oʻzbekcha "
                       "<strong>-mi</strong> kabi: <em>Придёт ли он?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я не зна́ю, придёт "
                "___ он.</strong></p>",
        "choices": ["е́сли", "что", "ли", "и́ли"],
        "correct": "ли",
        "explanation": "<p>Bu <strong>bilvosita savol</strong>: «keladimi, "
                       "bilmayman». <em>Е́сли</em> — shart bogʻlovchisi va bu "
                       "yerda ishlamaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Вряд ли</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Albatta", "Tez orada", "Umuman emas", "Dargumon"],
        "correct": "Dargumon",
        "explanation": "<p>— Он позвони́т? — <strong>Вряд ли.</strong> «Dargumon», "
                       "«qayoqda». Bu ibora ichida ham <em>ли</em> turibdi, lekin "
                       "u qotib qolgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Gapda savol soʻzi "
                "(<strong>где, когда́, кто</strong>) boʻlsa, <strong>ли</strong> "
                "qoʻyiladimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq, qoʻyilmaydi", "Faqat yozma nutqda",
                    "Faqat inkor gaplarda"],
        "correct": "Yoʻq, qoʻyilmaydi",
        "explanation": "<p><em>Я не зна́ю, <strong>когда́</strong> он "
                       "придёт</em> — <em>ли</em> ortiqcha. Oʻzbekchada ham "
                       "hech kim <s>«qachon keladimi»</s> demaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я не зна́ю, е́сли он до́ма.", "Я не зна́ю, ли он до́ма.",
                    "Я не зна́ю, до́ма ли он.", "Я не зна́ю, что ли он до́ма."],
        "correct": "Я не зна́ю, до́ма ли он.",
        "explanation": "<p>Soʻralayotgan soʻz — <em>до́ма</em> — oldinga chiqadi, "
                       "<em>ли</em> undan keyin turadi. <em>Е́сли</em> shart "
                       "bildiradi, <em>ли</em> esa hech qachon birinchi "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Bu gap nimani soʻrayapti?</p><p><strong>Жасу́р ли "
                "придёт?</strong></p>",
        "choices": ["Jasur keladimi yoki yoʻqmi", "Jasur qachon keladi",
                    "Jasurmi keladi (aynan u boʻladimi)", "Jasur qayerga keladi"],
        "correct": "Jasurmi keladi (aynan u boʻladimi)",
        "explanation": "<p><em>Ли</em> oʻzidan <strong>oldingi</strong> soʻzni "
                       "soʻroq ostiga oladi. Bu yerda u <em>Жасу́р</em> dan keyin "
                       "turibdi, demak kimdir keladi — lekin aynan Jasurmi? "
                       "«Keladimi?» boʻlishi uchun <em>Придёт ли Жасу́р?</em> "
                       "deyilardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он спроси́л, ___ "
                "ли у меня́ вре́мя.</strong></p>",
        "choices": ["был", "есть", "бу́дь", "быть"],
        "correct": "есть",
        "explanation": "<p><em>Он спроси́л, <strong>есть</strong> ли у меня́ "
                       "вре́мя</em> — «vaqtim bormi, deb soʻradi». <em>Есть</em> "
                       "oldinga chiqdi, chunki savol aynan shu haqda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Не зна́ю, придёт ли "
                "он ___ нет.</strong></p>",
        "choices": ["и́ли", "и", "но", "а"],
        "correct": "и́ли",
        "explanation": "<p><em>Ли … и́ли</em> — ikki variantni sanaydi. Diqqat: "
                       "<em>ли</em> <strong>bir marta</strong> qoʻyiladi, "
                       "oʻzbekchadagidek ikki marta emas "
                       "(<s>придёт ли он и́ли ли нет</s>).</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>ли</strong> kerak emas?</p>",
        "choices": ["Я не зна́ю, придёт он за́втра.",
                    "Я не зна́ю, где он живёт.",
                    "Спроси́, рабо́тает по́чта.",
                    "Прове́рь, есть биле́ты."],
        "correct": "Я не зна́ю, где он живёт.",
        "explanation": "<p>Bu gapda savol soʻzi <strong>где</strong> bor, demak "
                       "<em>ли</em> qoʻyilmaydi. Qolgan uchtasida savol soʻzi "
                       "yoʻq, shuning uchun ularga <em>ли</em> kerak: "
                       "<em>придёт ли он</em>, <em>рабо́тает ли по́чта</em>, "
                       "<em>есть ли биле́ты</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Не по́мню, ___ ли "
                "я дверь.</strong> (закры́ть)</p>",
        "choices": ["закры́ть", "закрыва́ю", "закры́л", "закро́ю"],
        "correct": "закры́л",
        "explanation": "<p><em>Не по́мню, <strong>закры́л</strong> ли я "
                       "дверь</em> — «eshikni yopdimmi, esimda yoʻq». Voqea "
                       "oʻtmishda boʻlgan, shuning uchun oʻtgan zamon.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>То ли дождь, то ли "
                "снег.</strong> — bu nimani bildiradi?</p>",
        "choices": ["Yomgʻir ham, qor ham yogʻdi", "Yo yomgʻir, yo qor — aniq emas",
                    "Yomgʻir qorga aylandi", "Na yomgʻir, na qor"],
        "correct": "Yo yomgʻir, yo qor — aniq emas",
        "explanation": "<p><strong>То ли … то ли</strong> — soʻzlovchi aniq "
                       "bilmaydi. Bu <em>ли</em> ning yana bir qotib qolgan "
                       "iborasi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Е́сли</strong> bilan "
                "<strong>ли</strong> ning farqi nimada?</p>",
        "choices": ["Farqi yoʻq, ikkalasi ham «-mi»",
                    "«Е́сли» yozma, «ли» ogʻzaki",
                    "«Ли» faqat oʻtgan zamonda ishlatiladi",
                    "«Е́сли» shart, «ли» savol"],
        "correct": "«Е́сли» shart, «ли» savol",
        "explanation": "<p>Oʻzbekchada ham «agar» bilan «-mi» hech qachon "
                       "aralashmaydi. <em>Е́сли он придёт</em> — «agar kelsa». "
                       "<em>Придёт ли он</em> — «keladimi».</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Е́сли он придёт, "
                "я ска́жу. · Я не зна́ю, придёт ли он.</strong></p>",
        "choices": ["Birinchisi shart, ikkinchisi bilvosita savol",
                    "Birinchisi savol, ikkinchisi buyruq",
                    "Farqi faqat uslubda",
                    "Birinchisi kelasi, ikkinchisi oʻtgan zamon"],
        "correct": "Birinchisi shart, ikkinchisi bilvosita savol",
        "explanation": "<p>Birinchisi: «agar u kelsa, aytaman» — <em>е́сли</em> "
                       "(PR-65). Ikkinchisi: «u keladimi, bilmayman» — "
                       "<em>ли</em>. Ikkala qismda ham feʼl kelasi zamonda, "
                       "lekin maʼno butunlay boshqa.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>ли</strong> toʻgʻri qoʻyilgan?</p>",
        "choices": ["За́втра ли он придёт?", "Ли за́втра он придёт?",
                    "Он придёт за́втра ли?", "Ли он придёт за́втра?"],
        "correct": "За́втра ли он придёт?",
        "explanation": "<p><em>Ли</em> soʻralayotgan soʻzdan keyin turadi va hech "
                       "qachon gapni boshlamaydi. Bu gap «Ertagami u keladi?» "
                       "degan maʼno beradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Не так ли?</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Nega unday emas?", "Shunday emasmi?", "Bu shart emas",
                    "Umuman boshqacha"],
        "correct": "Shunday emasmi?",
        "explanation": "<p><em>Вы из Ташке́нта, <strong>не так ли?</strong></em> "
                       "— «Toshkentdansiz, shunday emasmi?». Suhbatdoshdan "
                       "tasdiq soʻraydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я не зна́ю, когда́ ли он придёт.",
                    "Я не зна́ю, придёт ли он.",
                    "Я не зна́ю, когда́ он придёт.",
                    "Спроси́, до́ма ли она́."],
        "correct": "Я не зна́ю, когда́ ли он придёт.",
        "explanation": "<p>Gapda savol soʻzi <strong>когда́</strong> bor, demak "
                       "<em>ли</em> ortiqcha. Toʻgʻrisi — <em>Я не зна́ю, когда́ "
                       "он придёт</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Спроси́ до́ма ли он.", "Спроси́, ли он до́ма.",
                    "Спроси́, е́сли он до́ма.", "Спроси́, до́ма ли он."],
        "correct": "Спроси́, до́ма ли он.",
        "explanation": "<p>Uchta narsa bir vaqtda toʻgʻri boʻlishi kerak: "
                       "ergash gapdan oldin <strong>vergul</strong>, "
                       "soʻralayotgan soʻz oldinda, <em>ли</em> undan keyin. "
                       "<em>Е́сли</em> esa bu yerda umuman ishlamaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Ты ду́маешь, он сда́ст "
                "экза́мен без подгото́вки?</strong></p>",
        "choices": ["— Е́сли ли.", "— То ли.", "— Не так ли.", "— Вряд ли."],
        "correct": "— Вряд ли.",
        "explanation": "<p><strong>Вряд ли</strong> = «dargumon». Bu savolga eng "
                       "tabiiy qisqa javob. Qolganlari mustaqil ibora sifatida "
                       "ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Chiptalar "
                "bormi, bilib kel.</strong></p>",
        "choices": ["Узна́й, е́сли есть биле́ты.", "Узна́й, ли есть биле́ты.",
                    "Узна́й, где есть биле́ты.", "Узна́й, есть ли биле́ты."],
        "correct": "Узна́й, есть ли биле́ты.",
        "explanation": "<p>Oʻzbekcha <em>-mi</em> «bor» soʻziga yopishgan, demak "
                       "ruschada ham <em>ли</em> <strong>есть</strong> dan keyin "
                       "turadi. Uchinchi variant «qayerda chipta bor» degan "
                       "boshqa savol.</p>",
    },
]


# =====================================================================
# PR-69 — Тот, кто… / то, что…
# =====================================================================

Q_PR69 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Тот, кто</strong> "
                "qurilishi nima haqida ishlatiladi?</p>",
        "choices": ["Narsa haqida", "Odam haqida", "Joy haqida", "Vaqt haqida"],
        "correct": "Odam haqida",
        "explanation": "<p><em>Тот, кто и́щет, нахо́дит</em> — «Qidirgan "
                       "topadi». Narsa haqida esa <strong>то, что</strong> "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я не по́нял ___, "
                "что ты сказа́л.</strong></p>",
        "choices": ["тот", "тем", "тому́", "то"],
        "correct": "то",
        "explanation": "<p>Gap <strong>narsa</strong> haqida (aytilgan soʻz), "
                       "demak <em>то, что</em>. <em>Поня́ть что?</em> — "
                       "Вини́тельный, u yerda <em>то</em> shakli oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Кото́рый</strong> "
                "bilan <strong>тот, кто</strong> ning farqi nimada?</p>",
        "choices": ["«Кото́рый» faqat koʻplikda ishlatiladi",
                    "«Тот, кто» faqat savol gaplarda keladi",
                    "Farqi yoʻq — ikkalasi ham bir xil",
                    "«Кото́рый» ga ot kerak, «тот, кто» ga emas"],
        "correct": "«Кото́рый» ga ot kerak, «тот, кто» ga emas",
        "explanation": "<p><em><strong>Челове́к</strong>, кото́рый чита́ет…</em> "
                       "— ot bor. <em><strong>Тот</strong>, кто чита́ет…</em> — "
                       "ot yoʻq, shuning uchun <em>тот</em> uning oʻrnida "
                       "turibdi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Де́ло в том, "
                "что…</strong> nimani bildiradi?</p>",
        "choices": ["Ish tugadi", "Gap shundaki…", "Buning evaziga…", "Shunga qaramay…"],
        "correct": "Gap shundaki…",
        "explanation": "<p>Bu oʻzbekcha <strong>«Gap shundaki…»</strong> "
                       "iborasining soʻzma-soʻz oʻzi va ikkala tilda ham "
                       "tushuntirishni boshlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Все, кто</strong> dan "
                "keyin feʼl qaysi sonda turadi?</p>",
        "choices": ["Koʻplikda", "Birlikda", "Farqi yoʻq", "Faqat oʻtgan zamonda"],
        "correct": "Birlikda",
        "explanation": "<p><em>Все, кто <strong>пришёл</strong>, получи́ли "
                       "кни́гу.</em> Feʼl <em>кто</em> ga tegishli, demak "
                       "birlikda. Asosiy gapdagi <em>получи́ли</em> esa "
                       "<em>все</em> ga tegishli — u koʻplikda.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я помога́ю ___, кто "
                "про́сит.</strong></p>",
        "choices": ["тот", "того́", "тому́", "тем"],
        "correct": "тому́",
        "explanation": "<p><em>Помога́ть <strong>кому́?</strong></em> — "
                       "Да́тельный, demak <strong>тому́</strong>. "
                       "<em>Кто</em> esa oʻz gapida ega, shuning uchun И.п. da "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю ___, что "
                "ты сказа́л.</strong></p>",
        "choices": ["о том", "о то", "о тот", "о тому́"],
        "correct": "о том",
        "explanation": "<p><em>Ду́мать <strong>о чём?</strong></em> — "
                       "Предло́жный, demak <strong>о том</strong>. Predlogdan "
                       "keyin <em>то</em> hech qachon tushib qolmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Спаси́бо ___, что "
                "вы пришли́.</strong></p>",
        "choices": ["о том", "за то", "к тому́", "с тем"],
        "correct": "за то",
        "explanation": "<p><em>Спаси́бо <strong>за что?</strong></em> — "
                       "Вини́тельный, demak <strong>за то</strong>. Bu tayyor "
                       "ibora: <em>спаси́бо за то, что…</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___, кого́ мы "
                "жда́ли, не пришёл.</strong></p>",
        "choices": ["Того́", "Тому́", "Тем", "Тот"],
        "correct": "Тот",
        "explanation": "<p>Asosiy gapda bu soʻz <strong>ega</strong> "
                       "(<em>не пришёл</em> — kim?), demak <strong>И.п. — "
                       "тот</strong>. <em>Кого́</em> esa oʻz gapida "
                       "<em>ждать</em> ning obyekti — В.п.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Все, кто ___, "
                "оста́лись до конца́.</strong> (хоте́ть)</p>",
        "choices": ["хоте́ли", "хоте́л", "хо́чет", "хотя́т"],
        "correct": "хоте́л",
        "explanation": "<p><em>Кто</em> dan keyingi feʼl <strong>birlikda</strong> "
                       "turadi, hatto <em>все</em> bilan ham: <em>Все, кто "
                       "<strong>хоте́л</strong>, оста́лись</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ мно́го "
                "рабо́тает, тот мно́го зна́ет.</strong></p>",
        "choices": ["Кто", "Кото́рый", "Что", "Тот"],
        "correct": "Кто",
        "explanation": "<p>Maqollarda tartib teskari boʻlishi mumkin: avval "
                       "<em>кто</em>, keyin <em>тот</em>. Gapda ot yoʻq, "
                       "shuning uchun <em>кото́рый</em> ishlamaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bu gapda <strong>то</strong> "
                "nega <strong>том</strong> shaklida?</p><p><strong>Я не "
                "сомнева́юсь в том, что он придёт.</strong></p>",
        "choices": ["Chunki gap oʻtgan zamonda",
                    "Chunki «что» koʻplikda",
                    "Chunki «сомнева́ться в чём?» — Предло́жный",
                    "Chunki «он» erkak jinsida"],
        "correct": "Chunki «сомнева́ться в чём?» — Предло́жный",
        "explanation": "<p><em>То</em> ning kelishigi <strong>asosiy "
                       "gapdan</strong> keladi. Bu yerda feʼl <em>в</em> "
                       "predlogi bilan Предло́жный talab qiladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>Тот, кто</strong> yoki <strong>то, что</strong>?</p>"
                "<p><strong>___ он сказа́л, бы́ло пра́вдой.</strong></p>",
        "choices": ["Тот, кто", "Тот, что", "То, кто", "То, что"],
        "correct": "То, что",
        "explanation": "<p>Gap <strong>aytilgan narsa</strong> haqida, odam "
                       "haqida emas: «Aytgan gapi rost edi». Demak "
                       "<em>то, что</em>.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>кото́рый</strong> toʻgʻri keladi?</p>",
        "choices": ["___ мно́го чита́ет, хорошо́ пи́шет.",
                    "Я не по́нял ___, что ты сказа́л.",
                    "Челове́к, ___ мно́го чита́ет, хорошо́ пи́шет.",
                    "Спаси́бо за ___, что помогли́."],
        "correct": "Челове́к, ___ мно́го чита́ет, хорошо́ пи́шет.",
        "explanation": "<p>Faqat shu gapda <strong>ot</strong> bor — "
                       "<em>челове́к</em>. Qolganlarida ot yoʻq, shuning uchun "
                       "u yerda <em>тот, кто</em> yoki <em>то, что</em> "
                       "kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Тот</strong> ning "
                "kelishigi qayerdan keladi?</p>",
        "choices": ["Ergash gapdagi vazifasidan", "«Кто» ning kelishigidan",
                    "Har doim И.п. da qoladi", "Asosiy gapdagi vazifasidan"],
        "correct": "Asosiy gapdagi vazifasidan",
        "explanation": "<p>Xuddi PR-63 dagi <em>кото́рый</em> kabi: "
                       "<strong>тот</strong> asosiy gapdan, <strong>кто/что</strong> "
                       "esa oʻz gapidan kelishik oladi. Ikkita alohida savol "
                       "berish kerak.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я ду́маю, что ты "
                "прав. · Я ду́маю о том, что ты сказа́л.</strong></p>",
        "choices": ["Birinchisi fikr bildiradi, ikkinchisi «… haqida oʻylayapman»",
                    "Ikkalasi bir xil",
                    "Birinchisida xato bor",
                    "Ikkinchisi savol gap"],
        "correct": "Birinchisi fikr bildiradi, ikkinchisi «… haqida oʻylayapman»",
        "explanation": "<p><em>Ду́мать, что…</em> — «…deb hisoblayman». "
                       "<em>Ду́мать <strong>о том</strong>, что…</em> — «… "
                       "haqida oʻylamoq». Predlog paydo boʻlishi bilan "
                       "<em>то</em> ham majburiy boʻladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Тот, кто мно́го чита́ет, хорошо́ пи́шут.",
                    "Тот, кто мно́го чита́ет, хорошо́ пи́шет.",
                    "Я помога́ю тому́, кто про́сит.",
                    "Все, кто пришёл, получи́ли кни́гу."],
        "correct": "Тот, кто мно́го чита́ет, хорошо́ пи́шут.",
        "explanation": "<p><s>пи́шут</s> → <strong>пи́шет</strong>. Asosiy "
                       "gapning egasi <em>тот</em> — birlikda, demak feʼl ham "
                       "birlikda.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я ду́маю о что ты сказа́л.", "Я ду́маю то, что ты сказа́л.",
                    "Я ду́маю о том, что ты сказа́л.", "Я ду́маю о тот, что ты сказа́л."],
        "correct": "Я ду́маю о том, что ты сказа́л.",
        "explanation": "<p>Predlog otsiz turolmaydi — <em>о</em> dan keyin "
                       "albatta <strong>том</strong> kerak. Bu darsning eng "
                       "koʻp uchraydigan xatosi shu <em>то</em> ni tashlab "
                       "ketish.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Почему́ ты не "
                "позвони́л?</strong></p>",
        "choices": ["— Де́ло в тот, что у меня́ сел телефо́н.",
                    "— Де́ло то, что у меня́ сел телефо́н.",
                    "— Де́ло в том, что у меня́ сел телефо́н.",
                    "— Де́ло в то, что у меня́ сел телефо́н."],
        "correct": "— Де́ло в том, что у меня́ сел телефо́н.",
        "explanation": "<p><strong>Де́ло в том, что…</strong> = «Gap shundaki…». "
                       "<em>В</em> predlogi Предло́жный talab qiladi, demak "
                       "<em>в том</em> — shakl hech qachon oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Kim koʻp "
                "qidirsa, oʻsha topadi.</strong></p>",
        "choices": ["Кото́рый и́щет, нахо́дит.", "Тот, кто и́щет, нахо́дит.",
                    "То, что и́щет, нахо́дит.", "Тот, кото́рый и́щет, нахо́дит."],
        "correct": "Тот, кто и́щет, нахо́дит.",
        "explanation": "<p>Oʻzbekcha <strong>«kim … oʻsha»</strong> juftligi "
                       "ruschada <strong>тот, кто</strong> boʻladi. Gapda ot "
                       "yoʻq, shuning uchun <em>кото́рый</em> ishlamaydi, "
                       "<em>то, что</em> esa narsaga tegishli.</p>",
    },
]


# =====================================================================
# PR-70 — Действительные причастия
# =====================================================================

Q_PR70 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Причастие</strong> "
                "oʻzbekchada nimaga toʻgʻri keladi?</p>",
        "choices": ["Ravishdosh: -b, -gach", "Sifatdosh: -gan, -ayotgan, -adigan",
                    "Kelishik qoʻshimchasi", "Buyruq mayli"],
        "correct": "Sifatdosh: -gan, -ayotgan, -adigan",
        "explanation": "<p><em>чита́ющий</em> = «oʻqiyotgan», <em>чита́вший</em> = "
                       "«oʻqigan». Feʼl sifat kiyimini kiyib, otni "
                       "aniqlaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Hozirgi zamon sifatdoshi "
                "qaysi shakldan yasaladi?</p>",
        "choices": ["Infinitivdan", "«Я» shaklidan", "«Они́» shaklidan",
                    "Oʻtgan zamondan"],
        "correct": "«Они́» shaklidan",
        "explanation": "<p><em>чита́ю<strong>т</strong></em> → <strong>-т</strong> "
                       "olib tashlanadi, <strong>-щ-</strong> va sifat "
                       "qoʻshimchasi qoʻshiladi: <em>чита́ющий</em>. Xuddi "
                       "buyruq mayli kabi (PR-59), tayanch — «они́» "
                       "shakli.</p>",
    },
    {
        "text": "<p>Sifatdosh yasang.</p><p><strong>рабо́тать</strong> → hozirgi "
                "zamon</p>",
        "choices": ["рабо́таящий", "рабо́тавший", "рабо́тающий", "рабо́тущий"],
        "correct": "рабо́тающий",
        "explanation": "<p>«Они́» shakli — <em>рабо́таю<strong>т</strong></em>, "
                       "demak <strong>-ющ-</strong>: <em>рабо́тающий</em> "
                       "(«ishlayotgan»). <em>Рабо́тавший</em> — oʻtgan zamon "
                       "shakli.</p>",
    },
    {
        "text": "<p>Sifatdosh yasang.</p><p><strong>чита́ть</strong> → oʻtgan "
                "zamon</p>",
        "choices": ["чита́вший", "чита́ющий", "чита́ший", "чита́нный"],
        "correct": "чита́вший",
        "explanation": "<p>Oʻtgan zamon erkak shakli — <em>чита́<strong>л</strong></em>. "
                       "<strong>-л</strong> oʻrniga <strong>-вш-</strong> "
                       "qoʻyiladi: <em>чита́вший</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sifatdoshda "
                "<strong>-ся</strong> qanday yoziladi?</p>",
        "choices": ["Unlidan keyin -сь boʻladi", "Har doim -ся boʻlib qoladi",
                    "Umuman tushib qoladi", "Koʻplikda -сь boʻladi"],
        "correct": "Har doim -ся boʻlib qoladi",
        "explanation": "<p><em>верну́вший<strong>ся</strong></em>, "
                       "<em>улыба́ющий<strong>ся</strong></em> — sifatdoshda "
                       "<strong>-ся hech qachon -сь boʻlmaydi</strong>, garchi "
                       "undan oldin unli tursa ham.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Sifatdosh yasang.</p><p><strong>жить</strong> → hozirgi "
                "zamon</p>",
        "choices": ["жи́вший", "живя́щий", "жи́ющий", "живу́щий"],
        "correct": "живу́щий",
        "explanation": "<p>«Они́» shakli — <em>живу́<strong>т</strong></em>, demak "
                       "<em>живу́ + щ + ий</em> = <strong>живу́щий</strong> "
                       "(«yashayotgan»).</p>",
    },
    {
        "text": "<p>Sifatdosh yasang.</p><p><strong>говори́ть</strong> → hozirgi "
                "zamon</p>",
        "choices": ["говоря́щий", "говору́щий", "говори́вший", "говоря́ющий"],
        "correct": "говоря́щий",
        "explanation": "<p>«Они́» shakli — <em>говоря́<strong>т</strong></em> "
                       "(II tuslanish), demak <strong>-ящ-</strong>: "
                       "<em>говоря́щий</em>.</p>",
    },
    {
        "text": "<p>Sifatdosh yasang.</p><p><strong>прийти́</strong> → oʻtgan "
                "zamon</p>",
        "choices": ["приходя́щий", "приши́вший", "прише́дший", "прийти́вший"],
        "correct": "прише́дший",
        "explanation": "<p>Oʻtgan zamon erkak shakli — <em>пришёл</em>, unda "
                       "<strong>-л</strong> yoʻq, shuning uchun "
                       "<strong>-ш-</strong> qoʻshiladi. Bu soʻzni yodlab "
                       "qoʻyish maʼqul.</p>",
    },
    {
        "text": "<p>Nega bu shakl mavjud emas?</p><p><s><strong>прочита́ющий</strong></s></p>",
        "choices": ["Chunki «прочита́ть» — СВ feʼl, uning hozirgi zamoni yoʻq",
                    "Chunki bu feʼl -ся bilan ishlatiladi",
                    "Chunki oʻzagi unli bilan tugaydi",
                    "Chunki u II tuslanishga kiradi"],
        "correct": "Chunki «прочита́ть» — СВ feʼl, uning hozirgi zamoni yoʻq",
        "explanation": "<p>СВ feʼllarida hozirgi zamon umuman yoʻq (PR-51), demak "
                       "hozirgi zamon sifatdoshi ham yoʻq. Toʻgʻri shakl — "
                       "<strong>прочита́вший</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́дел ма́льчика, "
                "___ кни́гу.</strong> (чита́ть)</p>",
        "choices": ["чита́ющий", "чита́ющем", "чита́ющие", "чита́ющего"],
        "correct": "чита́ющего",
        "explanation": "<p>Sifatdosh <em>ма́льчика</em> ga moslashadi, u esa "
                       "<strong>Вини́тельный</strong> da (jonli ot, shuning "
                       "uchun Р.п. bilan bir xil): <em>чита́ющего</em>.</p>",
    },
    {
        "text": "<p>Vergul kerakmi?</p><p><strong>Стоя́щий на углу́ челове́к "
                "посмотре́л на нас.</strong></p>",
        "choices": ["Ha, «челове́к» dan keyin", "Ha, ikki tomondan",
                    "Yoʻq, kerak emas", "Ha, «углу́» dan keyin"],
        "correct": "Yoʻq, kerak emas",
        "explanation": "<p>Oborot otdan <strong>oldin</strong> turibdi — bu "
                       "oʻzbekcha tartib va u vergulsiz yoziladi. Otdan keyinga "
                       "koʻchirilsa, vergul paydo boʻladi: <em>Челове́к, стоя́щий "
                       "на углу́, посмотре́л…</em></p>",
    },
    {
        "text": "<p>Bu sifatdoshni <strong>кото́рый</strong> bilan yozing.</p>"
                "<p><strong>Лю́ди, живу́щие на Се́вере…</strong></p>",
        "choices": ["Лю́ди, кото́рый живёт на Се́вере…",
                    "Лю́ди, кото́рые жи́ли на Се́вере…",
                    "Лю́ди, кото́рых живу́т на Се́вере…",
                    "Лю́ди, кото́рые живу́т на Се́вере…"],
        "correct": "Лю́ди, кото́рые живу́т на Се́вере…",
        "explanation": "<p><em>Живу́щие</em> — koʻplik, hozirgi zamon. Demak "
                       "<strong>кото́рые живу́т</strong>. Notanish sifatdoshni "
                       "shunday yoyib tushunish mumkin.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki shaklning farqi nima?</p><p><strong>чита́ющий "
                "· чита́вший</strong></p>",
        "choices": ["Birinchisi koʻplik, ikkinchisi birlik",
                    "Birinchisi hozirgi («oʻqiyotgan»), ikkinchisi oʻtgan («oʻqigan»)",
                    "Birinchisi erkak, ikkinchisi ayol jinsi",
                    "Farqi faqat uslubda"],
        "correct": "Birinchisi hozirgi («oʻqiyotgan»), ikkinchisi oʻtgan («oʻqigan»)",
        "explanation": "<p><strong>-ющ-</strong> — hozirgi zamon, "
                       "<strong>-вш-</strong> — oʻtgan zamon. Oʻzbekchada bu "
                       "<em>-ayotgan</em> ↔ <em>-gan</em> farqi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sifatdosh qaysi uslubga "
                "xos?</p>",
        "choices": ["Yozma til: kitob, gazeta, hujjat", "Faqat ogʻzaki nutq",
                    "Faqat sheʼriyat", "Faqat bolalar tili"],
        "correct": "Yozma til: kitob, gazeta, hujjat",
        "explanation": "<p>Ogʻzaki nutqda ruslar deyarli har doim "
                       "<em>кото́рый</em> deydi. Maslahat: oʻqiganda taniy oling, "
                       "yozganda ishlating, gapirganda <em>кото́рый</em> "
                       "deng.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Nega <strong>прочита́вший</strong> "
                "bor, lekin <strong>прочита́ющий</strong> yoʻq?</p>",
        "choices": ["Chunki «прочита́ть» — СВ: hozirgi zamoni yoʻq",
                    "Chunki oʻzagi juda uzun",
                    "Chunki u prefiks bilan boshlanadi",
                    "Chunki «прочита́ть» notoʻgʻri feʼl"],
        "correct": "Chunki «прочита́ть» — СВ: hozirgi zamoni yoʻq",
        "explanation": "<p><strong>НСВ</strong> feʼlida ikkala shakl ham bor "
                       "(<em>чита́ющий, чита́вший</em>). <strong>СВ</strong> "
                       "feʼlida esa faqat oʻtgan zamon shakli.</p>",
    },
    {
        "text": "<p>Qaysi soʻz endi oddiy sifat boʻlib qolgan?</p>",
        "choices": ["чита́ющий", "живу́щий", "прише́дший", "настоя́щий"],
        "correct": "настоя́щий",
        "explanation": "<p><em>Настоя́щий друг</em> — «haqiqiy doʻst». Yasalishi "
                       "sifatdoshniki, lekin hech kim uni feʼl deb "
                       "oʻylamaydi. Shu guruhda yana <em>бу́дущий, блестя́щий, "
                       "подходя́щий</em>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ма́льчик, чита́ющий кни́гу, — мой брат.",
                    "Чита́ющий кни́гу ма́льчик — мой брат.",
                    "Я ви́дел ма́льчика, чита́ющий кни́гу.",
                    "Я ви́дел ма́льчика, чита́ющего кни́гу."],
        "correct": "Я ви́дел ма́льчика, чита́ющий кни́гу.",
        "explanation": "<p><s>чита́ющий</s> → <strong>чита́ющего</strong>. "
                       "Sifatdosh <em>ма́льчика</em> ga moslashishi kerak — u "
                       "Вини́тельный da. Bu oʻzbek oʻquvchisining eng koʻp "
                       "uchraydigan xatosi, chunki oʻzbekchada sifatdosh umuman "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri yozilgan?</p>",
        "choices": ["Ма́льчик чита́ющий кни́гу мой брат.",
                    "Ма́льчик, чита́ющий кни́гу — мой брат.",
                    "Ма́льчик чита́ющий, кни́гу — мой брат.",
                    "Ма́льчик, чита́ющий кни́гу, — мой брат."],
        "correct": "Ма́льчик, чита́ющий кни́гу, — мой брат.",
        "explanation": "<p>Oborot otdan <strong>keyin</strong> turgani uchun "
                       "<strong>ikki tomondan</strong> vergul bilan "
                       "ajratiladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni sifatdosh bilan qisqartiring.</p><p><strong>Студе́нт, "
                "кото́рый прочита́л кни́гу, отве́тил на все вопро́сы.</strong></p>",
        "choices": ["Студе́нт, чита́ющий кни́гу, отве́тил на все вопро́сы.",
                    "Студе́нт, прочита́вший кни́гу, отве́тил на все вопро́сы.",
                    "Студе́нт, прочита́ющий кни́гу, отве́тил на все вопро́сы.",
                    "Студе́нт, чита́вший кни́гу, отве́тил на все вопро́сы."],
        "correct": "Студе́нт, прочита́вший кни́гу, отве́тил на все вопро́сы.",
        "explanation": "<p><em>Кото́рый прочита́л</em> → <strong>прочита́вший</strong>: "
                       "СВ, oʻtgan zamon. <em>Чита́вший</em> НСВ boʻlardi "
                       "(«oʻqib yurgan»), <em>прочита́ющий</em> esa umuman "
                       "mavjud emas.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Shimolda "
                "yashaydigan odamlar sovuqqa oʻrganib qolgan.</strong></p>",
        "choices": ["Лю́ди, живу́щий на Се́вере, привы́кли к хо́лоду.",
                    "Лю́ди, жи́вшие на Се́вере, привы́кли к хо́лоду.",
                    "Лю́ди, живу́щие на Се́вере, привы́кли к хо́лоду.",
                    "Лю́ди, живу́щим на Се́вере, привы́кли к хо́лоду."],
        "correct": "Лю́ди, живу́щие на Се́вере, привы́кли к хо́лоду.",
        "explanation": "<p><em>Лю́ди</em> — koʻplik, И.п., demak "
                       "<strong>живу́щие</strong>. Ular hozir ham u yerda "
                       "yashaydi, shuning uchun hozirgi zamon shakli — "
                       "<em>жи́вшие</em> emas.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-68 Mashq: Ли va bilvosita savol",
        "description": (
            "Ли — oʻzbekcha «-mi» ning oʻzi va u ham soʻralayotgan soʻzga "
            "yopishadi. Bilvosita savol, «е́сли» tuzogʻi va вряд ли."
        ),
        "tutorial": "PR-68:",
        "questions": Q_PR68,
    },
    {
        "title": "PR-69 Mashq: Тот, кто… / то, что…",
        "description": (
            "Ot boʻlmasa который ishlamaydi. Тот asosiy gapdan, кто/что oʻz "
            "gapidan kelishik oladi; predlogdan keyin то majburiy."
        ),
        "tutorial": "PR-69:",
        "questions": Q_PR69,
    },
    {
        "title": "PR-70 Mashq: Причастие 1 — действительные",
        "description": (
            "Чита́ющий / чита́вший yasalishi, otga moslashuvi va vergul qoidasi. "
            "СВ feʼlida hozirgi zamon sifatdoshi yoʻq."
        ),
        "tutorial": "PR-70:",
        "questions": Q_PR70,
    },
]
