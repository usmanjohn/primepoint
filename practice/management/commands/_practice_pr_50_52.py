# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-50 … PR-52.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.

PR-50 — kelishiklar blokining yakuniy testi: butun blokdan aralash savollar.
PR-51, PR-52 — Block E boshi: вид.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_50_52.py --master=prime \\
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
# PR-50 — Kelishiklar: umumiy takror
# =====================================================================

Q_PR50 = [
    # 1–5 tanish
    {
        "text": "<p>Kelishikni tanlashning birinchi qadami nima?</p>",
        "choices": ["Jinsni aniqlash", "Predlog bor-yoʻqligini tekshirish",
                    "Feʼlning zamonini aniqlash", "Soʻz tartibiga qarash"],
        "correct": "Predlog bor-yoʻqligini tekshirish",
        "explanation": "<p>Predlog bor boʻlsa, <strong>u tanlaydi</strong> — boshqa "
                       "hech narsa oʻylanmaydi. Faqat predlog yoʻq boʻlsa soʻzning "
                       "gapdagi ishiga qaraladi.</p>",
    },
    {
        "text": "<p>Qaysi kelishik hech qachon predlog bilan kelmaydi?</p>",
        "choices": ["Имени́тельный", "Роди́тельный", "Твори́тельный", "Да́тельный"],
        "correct": "Имени́тельный",
        "explanation": "<p>Bosh kelishik gapning egasi. Aksincha — "
                       "<strong>Предло́жный</strong> hech qachon predlogsiz "
                       "kelmaydi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida qaysi ruscha kelishikning aniq juftligi "
                "<strong>yoʻq</strong>?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Твори́тельный",
        "explanation": "<p>Oʻzbekchada bu maʼno <strong>«bilan»</strong> soʻzi bilan "
                       "beriladi, alohida kelishik bilan emas. Qolgan beshtasining "
                       "juftligi bor: -ning, -ga, -ni, -da, -dan.</p>",
    },
    {
        "text": "<p>Bu gapda <strong>бра́ту</strong> qaysi kelishikda?</p>"
                "<p><strong>Ве́чером я пишу́ бра́ту письмо́.</strong></p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p>«Kimga yozyapman?» — <strong>Да́тельный</strong>. Va "
                       "<em>письмо́</em> — Вини́тельный (nimani), <em>ве́чером</em> — "
                       "Твори́тельный (kun qismi).</p>",
    },
    {
        "text": "<p>Egalik olmoshi, sifat va ot qanday oʻzgaradi?</p>",
        "choices": ["Har biri alohida", "Uchalasi birga — bitta guruh",
                    "Faqat ot oʻzgaradi", "Faqat sifat oʻzgaradi"],
        "correct": "Uchalasi birga — bitta guruh",
        "explanation": "<p><em>мое́й но́вой кни́ги</em> — uchtasi ham bir xil "
                       "kelishikda. Otning kelishigini bilsangiz, qolgan ikkitasi "
                       "oʻz-oʻzidan chiqadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я говорю́ с ___ ___ "
                "___.</strong> (мой ста́рый друг)</p>",
        "choices": ["мой ста́рый друг", "моего́ ста́рого дру́га",
                    "мои́м ста́рым дру́гом", "моему́ ста́рому дру́гу"],
        "correct": "мои́м ста́рым дру́гом",
        "explanation": "<p><em>С</em> Твори́тельный oladi. Uchta soʻz birga "
                       "oʻzgaradi: olmosh <strong>-им</strong>, sifat "
                       "<strong>-ым</strong>, ot <strong>-ом</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У меня́ нет ___.</strong> "
                "(вре́мя)</p>",
        "choices": ["вре́мя", "вре́мени", "вре́менем", "вре́мени́"],
        "correct": "вре́мени",
        "explanation": "<p>«Нет» dan keyin Роди́тельный, va <em>вре́мя</em> "
                       "<strong>-мя</strong> guruhidan: <strong>вре́мени</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я помога́ю ___.</strong> "
                "(сестра́)</p>",
        "choices": ["сестра́", "сестру́", "сестре́", "сестро́й"],
        "correct": "сестре́",
        "explanation": "<p><em>Помога́ть</em> Да́тельный oladi — oʻzbekcha «singlim"
                       "<strong>ga</strong> yordam beraman» toʻgʻri javobni "
                       "koʻrsatadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы бы́ли ___.</strong> "
                "(на рабо́та)</p>",
        "choices": ["на рабо́ту", "на рабо́те", "на рабо́ты", "на рабо́той"],
        "correct": "на рабо́те",
        "explanation": "<p><em>Быть</em> harakat emas, demak joy — Предло́жный. Va "
                       "<em>рабо́та</em> НА oladi (PR-30 roʻyxati).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___.</strong> "
                "(врач — «shifokorga»)</p>",
        "choices": ["в врача́", "к врачу́", "на врача́", "о враче́"],
        "correct": "к врачу́",
        "explanation": "<p>Manzil <strong>odam</strong> boʻlsa — <em>к</em> + "
                       "Да́тельный. Joy boʻlganda <em>в</em> yoki <em>на</em> + "
                       "Вини́тельный boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь мно́го "
                "___.</strong> (лю́ди)</p>",
        "choices": ["лю́ди", "люде́й", "лю́дям", "людьми́"],
        "correct": "люде́й",
        "explanation": "<p><em>Мно́го</em> koʻplik Роди́тельный talab qiladi, va "
                       "<em>челове́к</em> ning koʻpligi <strong>лю́ди → "
                       "люде́й</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я пишу́ ___ "
                "друзья́м.</strong> (ста́рые)</p>",
        "choices": ["ста́рые", "ста́рых", "ста́рым", "ста́рыми"],
        "correct": "ста́рым",
        "explanation": "<p>Koʻplik Да́тельный: sifat <strong>-ым</strong>, ot "
                       "<strong>-ям</strong>. Koʻplikda jins yoʻqoladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega bu ikki gap boshqa kelishik oladi?</p><p><strong>Я рабо́таю "
                "в магази́не. · Я иду́ в магази́н.</strong></p>",
        "choices": ["Feʼl hal qiladi: harakat yoʻq → П.п., harakat bor → В.п.",
                    "Predlog boshqa", "Birinchisi oʻtgan zamon",
                    "Ikkinchisi koʻplik"],
        "correct": "Feʼl hal qiladi: harakat yoʻq → П.п., harakat bor → В.п.",
        "explanation": "<p>Predlog ikkala gapda ham bir xil. <em>Рабо́тать</em> — "
                       "harakat emas, <em>идти́</em> — harakat.</p>",
    },
    {
        "text": "<p>Qaysi feʼl Да́тельный talab qiladi?</p>",
        "choices": ["ждать", "ви́деть", "помога́ть", "чита́ть"],
        "correct": "помога́ть",
        "explanation": "<p><em>Помога́ть, звони́ть, отвеча́ть, меша́ть, дать, "
                       "сказа́ть, писа́ть</em> — Да́тельный. Qolgan uchtasi "
                       "Вини́тельный oladi.</p>",
    },
    {
        "text": "<p>Butun blokda oʻzbek oʻquvchi uchun uchta qiyinchilik nima "
                "edi?</p>",
        "choices": ["Jins, predloglar, urgʻuning koʻchishi",
                    "Alifbo, soʻz tartibi, inkor",
                    "Zamon, son, shaxs",
                    "Feʼl, sifat, ravish"],
        "correct": "Jins, predloglar, urgʻuning koʻchishi",
        "explanation": "<p>Kelishik tushunchasining oʻzi tanish edi. Yangi narsa "
                       "uchta: jins (oʻzbekchada umuman yoʻq), predloglar (soʻzdan "
                       "oldin turadi va kelishikni tanlaydi), va urgʻuning "
                       "koʻchishi.</p>",
    },
    {
        "text": "<p>Bu iborada nechta soʻz kelishikka kirgan?</p><p><strong>в на́шей "
                "ста́рой шко́ле</strong></p>",
        "choices": ["Bittasi", "Ikkitasi", "Uchtasi", "Hech qaysi"],
        "correct": "Uchtasi",
        "explanation": "<p><em>На́шей</em> (olmosh), <em>ста́рой</em> (sifat), "
                       "<em>шко́ле</em> (ot) — uchalasi ham Предло́жный padejida. Ular "
                       "doim birga oʻzgaradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Кни́га бра́та но́вая.", "Я иду́ в шко́лу.",
                    "Я помога́ю бра́та.", "У него́ есть маши́на."],
        "correct": "Я помога́ю бра́та.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я помога́ю бра́ту</strong>. "
                       "<em>Помога́ть</em> Да́тельный oladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Бра́та кни́га но́вая.", "Кни́га бра́т но́вая.",
                    "Кни́га бра́та но́вая.", "Кни́ге бра́та но́вая."],
        "correct": "Кни́га бра́та но́вая.",
        "explanation": "<p>Egalik bildiruvchi soʻz <strong>orqada</strong> turadi va "
                       "faqat u kelishikka kiradi — oʻzbekchaning teskarisi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ertalab maktabga "
                "boraman va oʻqituvchi bilan yangi kitob haqida "
                "gaplashaman.</strong></p>",
        "choices": ["У́тром я иду́ в шко́ле и говорю́ с учи́телем о но́вой кни́ге.",
                    "У́тром я иду́ в шко́лу и говорю́ с учи́телем о но́вой кни́ге.",
                    "У́тром я иду́ в шко́лу и говорю́ с учи́телю о но́вой кни́ге.",
                    "У́тром я иду́ в шко́лу и говорю́ с учи́телем о но́вая кни́га."],
        "correct": "У́тром я иду́ в шко́лу и говорю́ с учи́телем о но́вой кни́ге.",
        "explanation": "<p>Toʻrtta kelishik bir gapda: <em>у́тром</em> (Т.п.), "
                       "<em>в шко́лу</em> (В.п., harakat), <em>с учи́телем</em> (Т.п., "
                       "hamroh), <em>о но́вой кни́ге</em> (П.п., mavzu).</p>",
    },
    {
        "text": "<p>Keyingi blokda nima oʻrganiladi?</p>",
        "choices": ["Вид — feʼlning tugallangan yoki tugallanmaganligi",
                    "Yangi alifbo", "Koʻproq kelishiklar", "Sonlar"],
        "correct": "Вид — feʼlning tugallangan yoki tugallanmaganligi",
        "explanation": "<p>Kelishik <strong>otga</strong> tegishli edi va soʻzning "
                       "gapdagi ishini koʻrsatardi. <strong>Вид</strong> esa "
                       "<strong>feʼlga</strong> tegishli va harakatning "
                       "tugagan-tugamaganini koʻrsatadi.</p>",
    },
]


# =====================================================================
# PR-51 — Вид: НСВ va СВ
# =====================================================================

Q_PR51 = [
    # 1–5 tanish
    {
        "text": "<p><strong>НСВ</strong> qaysi savolga javob beradi?</p>",
        "choices": ["что сде́лать?", "что де́лать?", "как де́лать?", "кому́ де́лать?"],
        "correct": "что де́лать?",
        "explanation": "<p><strong>НСВ</strong> (несоверше́нный вид) — "
                       "<em>что де́лать?</em> — jarayon, takror, odat. "
                       "<strong>СВ</strong> esa <em>что <b>с</b>де́лать?</em></p>",
    },
    {
        "text": "<p>Bu feʼl qaysi vidda?</p><p><strong>прочита́ть</strong></p>",
        "choices": ["НСВ", "СВ", "Ikkalasi", "Hech qaysi"],
        "correct": "СВ",
        "explanation": "<p>«Что <strong>с</strong>де́лать? — прочита́ть». Va koʻz "
                       "bilan ham koʻrinadi: oldida <strong>про-</strong> prefiksi "
                       "bor.</p>",
    },
    {
        "text": "<p><strong>СВ</strong> da qaysi zamon <strong>yoʻq</strong>?</p>",
        "choices": ["Oʻtgan zamon", "Hozirgi zamon", "Kelasi zamon", "Hammasi bor"],
        "correct": "Hozirgi zamon",
        "explanation": "<p>Bu mantiqiy: tugagan ish <strong>hozir</strong> boʻla "
                       "olmaydi. Shuning uchun <em>прочита́ю</em> hozirgi zamonga "
                       "oʻxshasa ham, u <strong>kelasi zamon</strong>.</p>",
    },
    {
        "text": "<p><strong>чита́л</strong> nimani bildiradi?</p>",
        "choices": ["Kitob tugadi", "Jarayon — tugagani nomaʼlum",
                    "Kitob tugamadi", "Kelasi zamon"],
        "correct": "Jarayon — tugagani nomaʼlum",
        "explanation": "<p>НСВ natija haqida hech narsa aytmaydi. Kitob tugadimi — "
                       "matn bu haqda jim. Natija kerak boʻlsa, <em>прочита́л</em> "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida tugallanganlik qanday koʻrsatiladi?</p>",
        "choices": ["Ikkinchi feʼl bilan: oʻqib chiqdim, yozib qoʻydim",
                    "Prefiks bilan", "Qoʻshimcha bilan", "Koʻrsatilmaydi"],
        "correct": "Ikkinchi feʼl bilan: oʻqib chiqdim, yozib qoʻydim",
        "explanation": "<p>Tushuncha bor, lekin u feʼlning <strong>yonida</strong> "
                       "turadi — alohida soʻz. Ruschada esa u feʼlning "
                       "<strong>ichiga</strong> kiradi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>чита́л</strong> yoki <strong>прочита́л</strong>?</p>"
                "<p><strong>Вчера́ я ___ три часа́.</strong></p>",
        "choices": ["чита́л", "прочита́л", "чита́ю", "прочита́ю"],
        "correct": "чита́л",
        "explanation": "<p>«Uch soat» — davomiylik, jarayon → <strong>НСВ</strong>. "
                       "Vaqt davomiyligi deyarli har doim НСВ talab qiladi.</p>",
    },
    {
        "text": "<p><strong>чита́л</strong> yoki <strong>прочита́л</strong>?</p>"
                "<p><strong>Вчера́ я ___ кни́гу до конца́.</strong></p>",
        "choices": ["чита́л", "прочита́л", "чита́ю", "бу́ду чита́ть"],
        "correct": "прочита́л",
        "explanation": "<p>«До конца́» — natija → <strong>СВ</strong>. Kitob "
                       "tugadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ка́ждый ве́чер я "
                "___.</strong></p>",
        "choices": ["чита́ю", "прочита́ю", "прочита́л", "прочита́ть"],
        "correct": "чита́ю",
        "explanation": "<p>«Ка́ждый ве́чер» — takror, odat → <strong>НСВ</strong>. Va "
                       "hozirgi zamon faqat НСВ da mavjud.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Сейча́с я ___ "
                "кни́гу.</strong></p>",
        "choices": ["прочита́ю", "чита́ю", "прочита́л", "прочита́ть"],
        "correct": "чита́ю",
        "explanation": "<p>«Сейча́с» — hozir, va <strong>СВ da hozirgi zamon "
                       "yoʻq</strong>. <em>Прочита́ю</em> kelasi zamon boʻlardi.</p>",
    },
    {
        "text": "<p><strong>прочита́ю</strong> — bu qaysi zamon?</p>",
        "choices": ["Hozirgi", "Oʻtgan", "Kelasi", "Zamonsiz"],
        "correct": "Kelasi",
        "explanation": "<p>СВ da hozirgi zamon yoʻq, shuning uchun bu shakl "
                       "<strong>kelasi zamon</strong>ni bildiradi. Bu PR-24 da vaʼda "
                       "qilingan «ikkinchi kelasi zamon».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ пи́сьма два "
                "ра́за.</strong> (писа́ть / написа́ть)</p>",
        "choices": ["написа́л", "писа́л", "напишу́", "пишу́"],
        "correct": "писа́л",
        "explanation": "<p>«Два ра́за» — takror → <strong>НСВ</strong>. Takror va "
                       "davomiylik har doim НСВ talab qiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Наконе́ц он ___ "
                "письмо́.</strong> (писа́ть / написа́ть)</p>",
        "choices": ["писа́л", "написа́л", "пи́шет", "бу́дет писа́ть"],
        "correct": "написа́л",
        "explanation": "<p>«Наконе́ц» — kutilgan natija → <strong>СВ</strong>. Bu soʻz "
                       "vidni deyarli har doim aytib turadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki savolning farqi nima?</p><p><strong>Ты чита́л кни́гу? · "
                "Ты прочита́л кни́гу?</strong></p>",
        "choices": ["Tanishmisan? · Oxirigacha oʻqidingmi?",
                    "Ikkalasi bir xil", "Birinchisi kelasi zamon",
                    "Ikkinchisi koʻplik"],
        "correct": "Tanishmisan? · Oxirigacha oʻqidingmi?",
        "explanation": "<p>Birinchisiga «ha», ikkinchisiga «yoʻq» deb javob berish "
                       "mumkin — va bu ziddiyat emas. НСВ faktni, СВ natijani "
                       "soʻraydi.</p>",
    },
    {
        "text": "<p>Rus tilida «neytral» feʼl shakli bormi?</p>",
        "choices": ["Ha, uchinchi vid bor", "Yoʻq — har safar tanlash shart",
                    "Faqat oʻtgan zamonda", "Faqat infinitivda"],
        "correct": "Yoʻq — har safar tanlash shart",
        "explanation": "<p>Oʻzbekcha <em>oʻqidim</em> neytral — u tugagan-tugamaganini "
                       "aytmaydi. Ruschada bunday shakl yoʻq. Aynan shu narsa vidni "
                       "qiyin qiladi: qoida emas, <strong>majburiy tanlov</strong>.</p>",
    },
    {
        "text": "<p>Qaysi soʻz odatda <strong>СВ</strong> ni talab qiladi?</p>",
        "choices": ["ка́ждый день", "до́лго", "наконе́ц", "два часа́"],
        "correct": "наконе́ц",
        "explanation": "<p>«Наконе́ц» — kutilgan natija. Qolgan uchtasi davomiylik yoki "
                       "takror bildiradi va <strong>НСВ</strong> talab qiladi.</p>",
    },
    {
        "text": "<p>Rus lugʻatlarida feʼllar nega juftlab yoziladi?</p>",
        "choices": ["Chunki har bir feʼl ikki vidga ega juftlikda yashaydi",
                    "Chunki ular sinonim", "Chunki bittasi eski shakl",
                    "Chunki bittasi kitobiy"],
        "correct": "Chunki har bir feʼl ikki vidga ega juftlikda yashaydi",
        "explanation": "<p><em>чита́ть — прочита́ть</em>, <em>писа́ть — "
                       "написа́ть</em>. Yangi feʼlni juft holda yodlash keyin vaqtni "
                       "tejaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Вчера́ я чита́л два часа́.", "Сейча́с я прочита́ю кни́гу.",
                    "Ка́ждый день я чита́ю.", "Наконе́ц он написа́л письмо́."],
        "correct": "Сейча́с я прочита́ю кни́гу.",
        "explanation": "<p>«Сейча́с» hozirgi zamon talab qiladi, СВ da esa hozirgi "
                       "zamon yoʻq. Toʻgʻrisi — <strong>Сейча́с я чита́ю "
                       "кни́гу</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Ка́ждый день я прочита́л кни́гу.",
                    "Ка́ждый день я чита́л кни́гу.",
                    "Ка́ждый день я прочита́ю кни́гу.",
                    "Ка́ждый день я прочита́ть кни́гу."],
        "correct": "Ка́ждый день я чита́л кни́гу.",
        "explanation": "<p>«Ка́ждый день» — takror, demak <strong>НСВ</strong>. СВ bir "
                       "marta tugagan ishni bildiradi va takror bilan mos "
                       "kelmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты прочита́л э́ту кни́гу?</strong></p>",
        "choices": ["— Нет, ещё чита́ю.", "— Нет, ещё прочита́ю.",
                    "— Нет, ещё прочита́л.", "— Нет, ещё прочита́ть."],
        "correct": "— Нет, ещё чита́ю.",
        "explanation": "<p>Savol natijani soʻraydi (СВ), javob esa jarayon davom "
                       "etayotganini aytadi — demak <strong>НСВ</strong> va hozirgi "
                       "zamon.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ikki soat oʻqidim va "
                "nihoyat kitobni oʻqib chiqdim.</strong></p>",
        "choices": ["Я прочита́л два часа́ и наконе́ц чита́л кни́гу.",
                    "Я чита́л два часа́ и наконе́ц прочита́л кни́гу.",
                    "Я чита́л два часа́ и наконе́ц чита́л кни́гу.",
                    "Я прочита́л два часа́ и наконе́ц прочита́л кни́гу."],
        "correct": "Я чита́л два часа́ и наконе́ц прочита́л кни́гу.",
        "explanation": "<p>«Ikki soat» — davomiylik (<strong>НСВ</strong>), «nihoyat "
                       "oʻqib chiqdim» — natija (<strong>СВ</strong>). Oʻzbekchada ham "
                       "ikki xil: «oʻqidim» va «oʻqib chiqdim».</p>",
    },
]


# =====================================================================
# PR-52 — Vid juftliklarini yasash
# =====================================================================

Q_PR52 = [
    # 1–5 tanish
    {
        "text": "<p><strong>де́лать</strong> feʼlining СВ jufti qaysi?</p>",
        "choices": ["де́лывать", "сде́лать", "поде́лать", "заде́лать"],
        "correct": "сде́лать",
        "explanation": "<p>Prefiks <strong>с-</strong>. Qaysi prefiks kerakligini "
                       "taxmin qilib boʻlmaydi — shuning uchun feʼl juftlab "
                       "yodlanadi.</p>",
    },
    {
        "text": "<p><strong>откры́ть</strong> feʼlining НСВ jufti qaysi?</p>",
        "choices": ["откры́вить", "открыва́ть", "пооткры́ть", "откры́вать"],
        "correct": "открыва́ть",
        "explanation": "<p>Ikkinchi guruh: СВ dan НСВ <strong>suffiks</strong> bilan "
                       "yasaladi. Bu yerda uzunroq shakl — НСВ.</p>",
    },
    {
        "text": "<p><strong>говори́ть</strong> feʼlining СВ jufti qaysi?</p>",
        "choices": ["поговори́ть", "сказа́ть", "проговори́ть", "договори́ть"],
        "correct": "сказа́ть",
        "explanation": "<p>Uchinchi guruh: butunlay boshqa oʻzak. Oʻzbekchada ham "
                       "ikkita boshqa feʼl — «gapirmoq» va «aytmoq».</p>",
    },
    {
        "text": "<p>Vid juftliklari necha yoʻl bilan yasaladi?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Beshta"],
        "correct": "Uchta",
        "explanation": "<p><strong>Prefiks</strong> (НСВ → СВ), <strong>suffiks</strong> "
                       "(СВ → НСВ) va <strong>butunlay boshqa oʻzak</strong>. "
                       "Birinchi ikkitasi qoidali.</p>",
    },
    {
        "text": "<p><strong>брать</strong> feʼlining СВ jufti qaysi?</p>",
        "choices": ["побра́ть", "взять", "забра́ть", "набра́ть"],
        "correct": "взять",
        "explanation": "<p>Butunlay boshqa oʻzak — bu guruhda qoida yoʻq, faqat "
                       "yodlash. Lekin bunday juftliklar kam: <em>говори́ть — "
                       "сказа́ть</em>, <em>брать — взять</em>, <em>иска́ть — "
                       "найти́</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu juftlikda qaysi biri НСВ?</p><p><strong>рассказа́ть · "
                "расска́зывать</strong></p>",
        "choices": ["рассказа́ть", "расска́зывать", "Ikkalasi", "Hech qaysi"],
        "correct": "расска́зывать",
        "explanation": "<p>Unda <strong>-ыва-</strong> suffiksi bor. Yoʻnalishga "
                       "qarang: suffiks qoʻshilsa — НСВ tomonga; prefiks qoʻshilsa — "
                       "СВ tomonga.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он до́лго ___ ключи́ и "
                "наконе́ц ___ их.</strong> (иска́ть / найти́)</p>",
        "choices": ["нашёл … иска́л", "иска́л … нашёл",
                    "иска́л … иска́л", "нашёл … нашёл"],
        "correct": "иска́л … нашёл",
        "explanation": "<p>«До́лго» — davomiylik (НСВ), «наконе́ц» — natija (СВ). Bu "
                       "ikki soʻz vidni deyarli har doim aytib turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма ___ у́жин два "
                "часа́.</strong> (гото́вить / пригото́вить)</p>",
        "choices": ["пригото́вила", "гото́вила", "пригото́вит", "гото́вит"],
        "correct": "гото́вила",
        "explanation": "<p>«Два часа́» — davomiylik → <strong>НСВ</strong>. Natija "
                       "boʻlganda <em>пригото́вила</em> boʻlardi.</p>",
    },
    {
        "text": "<p><strong>реши́ть</strong> feʼlining НСВ jufti qaysi?</p>",
        "choices": ["реша́ть", "поре́шить", "реши́вать", "разреши́ть"],
        "correct": "реша́ть",
        "explanation": "<p>Suffiks guruhi: <strong>-ить → -ать</strong>. Xuddi shunday "
                       "<em>получи́ть → получа́ть</em>, <em>отве́тить → "
                       "отвеча́ть</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Па́па ___ сте́ны два "
                "дня.</strong> (кра́сить / покра́сить)</p>",
        "choices": ["покра́сил", "кра́сил", "кра́сит", "покра́сит"],
        "correct": "кра́сил",
        "explanation": "<p>«Два дня» — davomiylik → НСВ <strong>кра́сил</strong>. "
                       "Uchinchi kuni tugatganda <em>покра́сил</em> boʻladi.</p>",
    },
    {
        "text": "<p><strong>класть</strong> feʼlining СВ jufti qaysi?</p>",
        "choices": ["покла́сть", "положи́ть", "закла́сть", "накла́сть"],
        "correct": "положи́ть",
        "explanation": "<p>Butunlay boshqa oʻzak. Bu juftlik juda koʻp ishlatiladi, "
                       "shuning uchun alohida yodlanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ до́лго, но ___ "
                "одно́ сло́во.</strong> (говори́ть / сказа́ть)</p>",
        "choices": ["сказа́л … говори́л", "говори́л … сказа́л",
                    "говори́л … говори́л", "сказа́л … сказа́л"],
        "correct": "говори́л … сказа́л",
        "explanation": "<p>«До́лго» — jarayon (НСВ), «одно́ сло́во» — natija (СВ). Bu "
                       "juftlik oʻzbekchada ham ikkita boshqa feʼl: «gapirdi» va "
                       "«aytdi».</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Prefiks qaysi tomonga oʻzgartiradi?</p>",
        "choices": ["НСВ → СВ", "СВ → НСВ", "Hech qaysi tomonga", "Ikkala tomonga"],
        "correct": "НСВ → СВ",
        "explanation": "<p><em>чита́ть → <strong>про</strong>чита́ть</em>. Suffiks esa "
                       "teskari ishlaydi: <em>откры́ть → открыв<strong>а́</strong>ть</em> "
                       "(СВ → НСВ).</p>",
    },
    {
        "text": "<p>Nima uchun uzunlikka qarab vidni aniqlab boʻlmaydi?</p>",
        "choices": ["Chunki prefiksda uzun shakl СВ, suffiksda esa НСВ",
                    "Chunki hamma shakl bir xil uzunlikda",
                    "Chunki uzunlik hech narsa bildirmaydi",
                    "Uzunlikka qarab aniqlash mumkin"],
        "correct": "Chunki prefiksda uzun shakl СВ, suffiksda esa НСВ",
        "explanation": "<p><em>прочита́ть</em> uzun va СВ; <em>открыва́ть</em> uzun va "
                       "НСВ. Shuning uchun <strong>yoʻnalishga</strong> qarash "
                       "kerak.</p>",
    },
    {
        "text": "<p>Oʻzbekchada tugallanganlikni koʻrsatuvchi yordamchi feʼllar "
                "roʻyxati qanday?</p>",
        "choices": ["Ochiq — juda koʻp", "Yopiq — qoʻymoq, chiqmoq, bermoq, olmoq…",
                    "Bittagina feʼl", "Bunday feʼllar yoʻq"],
        "correct": "Yopiq — qoʻymoq, chiqmoq, bermoq, olmoq…",
        "explanation": "<p>Oltitacha yordamchi feʼl. Ruschada ham shunday yopiq "
                       "roʻyxat bor, faqat prefikslardan: <strong>про-, на-, с-, по-, "
                       "вы-, при-, у-</strong>.</p>",
    },
    {
        "text": "<p>Har bir prefiks faqat vidni oʻzgartiradimi?</p>",
        "choices": ["Ha, har doim", "Yoʻq — baʼzilari maʼnoni ham oʻzgartiradi",
                    "Faqat oʻtgan zamonda", "Faqat qisqa feʼllarda"],
        "correct": "Yoʻq — baʼzilari maʼnoni ham oʻzgartiradi",
        "explanation": "<p><em>чита́ть → <strong>пере</strong>чита́ть</em> (qayta "
                       "oʻqimoq), <em>писа́ть → <strong>под</strong>писа́ть</em> "
                       "(imzolamoq). Bunday prefikslar PR-57 va PR-58 da "
                       "koʻriladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он говори́л до́лго.", "Он сказа́л одно́ сло́во.",
                    "Ка́ждый день он сказа́л пра́вду.", "Наконе́ц он нашёл ключи́."],
        "correct": "Ка́ждый день он сказа́л пра́вду.",
        "explanation": "<p>«Ка́ждый день» — takror, demak <strong>НСВ</strong>: "
                       "<em>говори́л</em>. СВ bir marta tugagan ishni bildiradi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Ма́ма выбира́ла ла́мпу и вы́брала.",
                    "Ма́ма вы́брала ла́мпу и выбира́ла.",
                    "Ма́ма выбира́ла ла́мпу и выбира́ла.",
                    "Ма́ма вы́брала ла́мпу и вы́брала."],
        "correct": "Ма́ма выбира́ла ла́мпу и вы́брала.",
        "explanation": "<p>Avval jarayon (<strong>выбира́ла</strong> — НСВ), keyin "
                       "natija (<strong>вы́брала</strong> — СВ). Bu tabiiy "
                       "ketma-ketlik.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Вы сде́лали стол?</strong></p>",
        "choices": ["— Мы де́лали его́ четы́ре часа́, но не сде́лали.",
                    "— Мы сде́лали его́ четы́ре часа́.",
                    "— Мы де́лали его́ четы́ре часа́, но не де́лали.",
                    "— Мы сде́лали его́, но не сде́лали."],
        "correct": "— Мы де́лали его́ четы́ре часа́, но не сде́лали.",
        "explanation": "<p>Jarayon bor edi (<strong>де́лали</strong>), natija yoʻq "
                       "(<strong>не сде́лали</strong>). Aynan shu juftlik vidning "
                       "butun maʼnosini koʻrsatadi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Onam ikki soat ovqat "
                "tayyorladi va soat sakkizda tayyorlab boʻldi.</strong></p>",
        "choices": ["Ма́ма пригото́вила два часа́ и в во́семь гото́вила.",
                    "Ма́ма гото́вила два часа́ и в во́семь пригото́вила.",
                    "Ма́ма гото́вила два часа́ и в во́семь гото́вила.",
                    "Ма́ма пригото́вила два часа́ и в во́семь пригото́вила."],
        "correct": "Ма́ма гото́вила два часа́ и в во́семь пригото́вила.",
        "explanation": "<p>«Ikki soat» — davomiylik (НСВ <strong>гото́вила</strong>), "
                       "«tayyorlab boʻldi» — natija (СВ <strong>пригото́вила</strong>). "
                       "Oʻzbekcha ham ikki xil aytadi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-50 Mashq: Kelishiklar — umumiy takror va tirik gaplarda mashq",
        "description": (
            "Butun blokdan aralash test: predlog xaritasi, feʼl talab qiladigan "
            "kelishiklar, uch soʻzning birga oʻzgarishi va eng koʻp xatolar."
        ),
        "tutorial": "PR-50:",
        "questions": Q_PR50,
    },
    {
        "title": "PR-51 Mashq: Вид — tugallanmagan va tugallangan feʼl",
        "description": (
            "НСВ (что де́лать?) va СВ (что сде́лать?): jarayon ↔ natija, "
            "СВ da hozirgi zamonning yoʻqligi va neytral shaklning yoʻqligi."
        ),
        "tutorial": "PR-51:",
        "questions": Q_PR51,
    },
    {
        "title": "PR-52 Mashq: Vid juftliklarini yasash: prefiks, suffiks va butunlay boshqa oʻzak",
        "description": (
            "Uch yoʻl: prefiks (НСВ → СВ), suffiks (СВ → НСВ) va boshqa oʻzak. "
            "Yoʻnalishga qarash — uzunlikka emas."
        ),
        "tutorial": "PR-52:",
        "questions": Q_PR52,
    },
]
