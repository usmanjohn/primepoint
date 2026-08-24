# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-65 … PR-67.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_65_67.py --master=prime \\
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
# PR-65 — Если va когда
# =====================================================================

Q_PR65 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ за́втра бу́дет "
                "дождь, мы оста́немся до́ма.</strong></p>",
        "choices": ["Пока́", "Когда́", "Е́сли", "Как то́лько"],
        "correct": "Е́сли",
        "explanation": "<p><strong>Е́сли</strong> — bu <strong>shart</strong>: yomgʻir "
                       "yogʻishi ham, yogʻmasligi ham mumkin. <em>Когда́</em> deyilsa, "
                       "yomgʻir albatta yogʻadi degan maʼno chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Когда́</strong> "
                "bogʻlovchisi nimani bildiradi?</p>",
        "choices": ["Vaqt", "Shart", "Sabab", "Maqsad"],
        "correct": "Vaqt",
        "explanation": "<p><strong>Когда́</strong> — <strong>vaqt</strong> bogʻlovchisi: "
                       "voqea albatta boʻladi, faqat qachonligi aytilyapti. Shart uchun "
                       "<em>е́сли</em>, sabab uchun <em>потому́ что</em> ishlatiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ergash gap bilan asosiy gap "
                "orasida nima turadi?</p>",
        "choices": ["Nuqta", "Tire", "Vergul", "Hech narsa"],
        "correct": "Vergul",
        "explanation": "<p><strong>Vergul har doim majburiy</strong> — ergash gap "
                       "oldinda tursa ham, keyinda tursa ham: <em>Когда́ он "
                       "пришёл<strong>,</strong> мы у́жинали</em> · <em>Мы "
                       "у́жинали<strong>,</strong> когда́ он пришёл</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>То</strong> soʻzi "
                "qachon qoʻyilishi mumkin?</p>",
        "choices": ["Ergash gap oldinda turganda", "Ergash gap keyinda turganda",
                    "Har doim majburiy", "Faqat inkor gaplarda"],
        "correct": "Ergash gap oldinda turganda",
        "explanation": "<p><em>Е́сли бу́дет дождь, <strong>то</strong> мы оста́немся "
                       "до́ма.</em> <strong>То</strong> ixtiyoriy va faqat ergash gap "
                       "birinchi kelganda ishlatiladi — u gapni ikkiga aniq "
                       "ajratadi. Oʻzbekcha «u holda» ning aynan oʻzi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Пока́ не</strong> "
                "nimani bildiradi?</p>",
        "choices": ["…gani uchun", "…sa ham", "…ganda", "…gunicha"],
        "correct": "…gunicha",
        "explanation": "<p><em>Жди, пока́ я <strong>не</strong> верну́сь</em> — "
                       "«qaytmagunimcha kut». Bu yerdagi <strong>не</strong> inkor "
                       "emas, qurilishning bir qismi — xuddi oʻzbekcha "
                       "«qayt<strong>ma</strong>gunimcha» dagi <em>-ma-</em> "
                       "kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Когда́ я ___ на "
                "рабо́ту, я напишу́ тебе́.</strong> (прийти́)</p>",
        "choices": ["прихожу́", "пришёл", "приду́", "приходи́л"],
        "correct": "приду́",
        "explanation": "<p>Gap <strong>kelajak</strong> haqida (<em>напишу́</em>), "
                       "shuning uchun <em>когда́</em> dan keyin ham <strong>kelasi "
                       "zamon</strong> turadi: <strong>приду́</strong>. Oʻzbekcha "
                       "«bor<strong>ganimda</strong>» zamonsiz, ruschada esa zamon "
                       "aytilishi shart.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Е́сли за́втра ___ "
                "хоро́шая пого́да, мы пое́дем за́ город.</strong> (быть)</p>",
        "choices": ["была́", "быть", "бу́дет", "есть"],
        "correct": "бу́дет",
        "explanation": "<p><strong>Бу́дет</strong> — kelasi zamon. Bu darsdagi eng "
                       "koʻp uchraydigan xato: <s>Е́сли за́втра хоро́шая пого́да</s> "
                       "deb yozib qoʻyish. Rus tilida voqea kelajakda boʻlsa, feʼl "
                       "ham kelasi zamonda boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Когда́ я ___ "
                "письмо́, я сра́зу всё по́нял.</strong> (чита́ть / прочита́ть)</p>",
        "choices": ["чита́л", "прочита́л", "чита́ю", "бу́ду чита́ть"],
        "correct": "прочита́л",
        "explanation": "<p><strong>Прочита́л</strong> — <strong>СВ</strong>. Avval "
                       "xat oʻqib boʻlindi, <em>keyin</em> tushunish keldi — bu "
                       "ketma-ketlik. <em>Чита́л</em> (НСВ) deyilsa «oʻqiyotgan "
                       "paytimda tushundim» degan boshqa manzara chiqadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Когда́ Дилно́за ___ "
                "у́жин, Жасу́р накрыва́л на стол.</strong> (гото́вить / "
                "пригото́вить)</p>",
        "choices": ["пригото́вила", "гото́вила", "гото́вит", "пригото́вит"],
        "correct": "гото́вила",
        "explanation": "<p><strong>Гото́вила</strong> — <strong>НСВ</strong>, chunki "
                       "ikkala ish <strong>bir vaqtda</strong> ketyapti: biri ovqat "
                       "tayyorlayapti, ikkinchisi dasturxon yozyapti. "
                       "<em>Пригото́вила</em> (СВ) deyilsa «tayyorlab boʻlgach» "
                       "degan ketma-ketlik chiqardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Как то́лько</strong> "
                "nimani bildiradi?</p>",
        "choices": ["…dan oldin", "…gunicha", "…sa ham", "…ishi bilanoq"],
        "correct": "…ishi bilanoq",
        "explanation": "<p><em>Как то́лько он придёт, мы начнём</em> — «u kelishi "
                       "bilanoq boshlaymiz». Bu <em>когда́</em> ning tezroq, "
                       "aniqroq varianti.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Жди меня́ здесь, "
                "пока́ я ___.</strong> (верну́ться)</p>",
        "choices": ["верну́сь", "не верну́сь", "верну́лся", "возвраща́юсь"],
        "correct": "не верну́сь",
        "explanation": "<p>«Qaytmagunimcha» maʼnosi uchun <strong>пока́ не</strong> "
                       "kerak. <em>Не</em> siz gap «men qaytayotgan payt kut» degan "
                       "boshqa maʼno berardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Пе́ред тем как ___, "
                "вы́ключи свет.</strong> (вы́йти)</p>",
        "choices": ["вы́йдешь", "вы́шел", "вы́йти", "выхожу́"],
        "correct": "вы́йти",
        "explanation": "<p>Ikkala qismda ham ega bitta (<em>ты</em>), shuning uchun "
                       "<strong>пе́ред тем как</strong> dan keyin <strong>infinitiv</strong> "
                       "turadi: <em>пе́ред тем как вы́йти</em>. Bu <em>что́бы</em> "
                       "ning qoidasiga oʻxshaydi (PR-64).</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi gapda soʻzlovchi uning "
                "kelishiga <strong>ishonchi komil</strong>?</p>",
        "choices": ["Е́сли он придёт, мы начнём.", "Ikkalasida ham bir xil",
                    "Hech qaysisida", "Когда́ он придёт, мы начнём."],
        "correct": "Когда́ он придёт, мы начнём.",
        "explanation": "<p><strong>Когда́</strong> — u albatta keladi, faqat qachonligi "
                       "nomaʼlum. <strong>Е́сли</strong> — kelmasligi ham mumkin. "
                       "Bitta soʻz butun maʼnoni oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Е́сли бы у меня́ бы́ло "
                "вре́мя, я бы пришёл.</strong> — bu gap nimani bildiradi?</p>",
        "choices": ["Vaqti bor va keladi", "Ertaga keladi", "Kelishini bilmaydi",
                    "Vaqti yoʻq, shuning uchun kelmadi"],
        "correct": "Vaqti yoʻq, shuning uchun kelmadi",
        "explanation": "<p><strong>Е́сли бы</strong> — <strong>noreal</strong> shart "
                       "(PR-60). Ikkala qismda ham <em>бы</em> va oʻtgan zamon "
                       "turibdi, demak bu sodir boʻlmagan narsa.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Е́сли бы за́втра бу́дет вре́мя, я приду́.",
                    "Е́сли за́втра бу́дет вре́мя, я приду́.",
                    "Е́сли за́втра есть вре́мя, я приду́.",
                    "Е́сли бы за́втра есть вре́мя, я бы приду́."],
        "correct": "Е́сли за́втра бу́дет вре́мя, я приду́.",
        "explanation": "<p>Bu <strong>real</strong> shart: vaqt boʻlishi mumkin. "
                       "Demak <em>бы</em> keraksiz, feʼl esa <strong>kelasi "
                       "zamonda</strong> — <em>бу́дет</em>. <em>Бы</em> bilan "
                       "<em>бу́дет</em> bir gapda hech qachon uchrashmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Пока́ ты "
                "гото́вишь</strong> va <strong>пока́ ты не пригото́вишь</strong> "
                "— farqi nimada?</p>",
        "choices": ["Farqi umuman yoʻq",
                    "Zamon farqi: hozirgi ↔ oʻtgan",
                    "«tayyorlayotganingda» ↔ «tayyorlamaguningcha»",
                    "Ikkinchisi inkor gap"],
        "correct": "«tayyorlayotganingda» ↔ «tayyorlamaguningcha»",
        "explanation": "<p><strong>Пока́</strong> — ish davom etayotgan payt. "
                       "<strong>Пока́ не</strong> — ish tugagunicha. Ikkinchisi "
                       "inkor gap emas: <em>не</em> shu qurilishning qismi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Е́сли за́втра идёт дождь, я оста́нусь до́ма.",
                    "Когда́ он придёт, мы начнём.",
                    "Е́сли бу́дет вре́мя, я позвоню́.",
                    "Как то́лько я верну́сь, я напишу́."],
        "correct": "Е́сли за́втра идёт дождь, я оста́нусь до́ма.",
        "explanation": "<p><s>идёт</s> → <strong>бу́дет</strong>. Gap ertangi kun "
                       "haqida, demak feʼl kelasi zamonda boʻlishi kerak: "
                       "<em>Е́сли за́втра <strong>бу́дет</strong> дождь…</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Когда́ он пришёл мы уже́ у́жинали.",
                    "Когда́ я приду́ домо́й, я звоню́ тебе́.",
                    "Когда́ он пришёл, мы уже́ у́жинали.",
                    "Когда́ бы он придёт, мы начнём."],
        "correct": "Когда́ он пришёл, мы уже́ у́жинали.",
        "explanation": "<p>Vergul majburiy — birinchi variantda u yoʻq. Ikkinchisida "
                       "asosiy gap kelajakda boʻlishi kerak edi (<em>позвоню́</em>). "
                       "Toʻrtinchisida <em>бы</em> ortiqcha: <em>когда́</em> real "
                       "vaqtni bildiradi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Ты придёшь за́втра на "
                "трениро́вку?</strong></p>",
        "choices": ["— Да, е́сли я бу́ду свобо́ден.",
                    "— Да, е́сли я свобо́ден бу́ду был.",
                    "— Да, е́сли бы я бу́ду свобо́ден.",
                    "— Да, когда́ бы я свобо́ден."],
        "correct": "— Да, е́сли я бу́ду свобо́ден.",
        "explanation": "<p>Real shart, kelajak haqida: <strong>е́сли + бу́ду</strong>. "
                       "<em>Бы</em> bu yerda keraksiz, chunki hali hech narsa hal "
                       "boʻlmagan.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Uyga "
                "borganimda senga qoʻngʻiroq qilaman.</strong></p>",
        "choices": ["Когда́ я прихожу́ домо́й, я тебе́ звоню́.",
                    "Е́сли бы я пришёл домо́й, я бы тебе́ позвони́л.",
                    "Когда́ я пришёл домо́й, я тебе́ позвони́л.",
                    "Когда́ я приду́ домо́й, я тебе́ позвоню́."],
        "correct": "Когда́ я приду́ домо́й, я тебе́ позвоню́.",
        "explanation": "<p>Voqea <strong>kelajakda</strong>, demak ikkala feʼl ham "
                       "kelasi zamonda: <em>приду́ … позвоню́</em>. Birinchi variant "
                       "«har safar uyga kelganimda qoʻngʻiroq qilaman» degan odat, "
                       "uchinchisi esa oʻtmish.</p>",
    },
]


# =====================================================================
# PR-66 — Sabab va natija
# =====================================================================

Q_PR66 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Потому́ что</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Shuning uchun", "Chunki", "Shunga qaramay", "Agar"],
        "correct": "Chunki",
        "explanation": "<p><strong>Потому́ что</strong> = <strong>chunki</strong>, "
                       "yaʼni <strong>sabab</strong>. «Shuning uchun» — bu "
                       "<em>поэ́тому</em>, yaʼni natija.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Бы́ло хо́лодно, ___ "
                "мы вы́звали такси́.</strong></p>",
        "choices": ["потому́ что", "так как", "поэ́тому", "поско́льку"],
        "correct": "поэ́тому",
        "explanation": "<p>Birinchi qism — <strong>sabab</strong> (sovuq edi), "
                       "ikkinchisi — <strong>natija</strong> (taksi chaqirdik). "
                       "Natija <em>поэ́тому</em> bilan keladi. Qolgan uchtasi sabab "
                       "bogʻlovchilari.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы оста́лись до́ма, "
                "___ бы́ло о́чень хо́лодно.</strong></p>",
        "choices": ["потому́ что", "зна́чит", "поэ́тому", "сле́довательно"],
        "correct": "потому́ что",
        "explanation": "<p>Bu safar tartib teskari: oldin <strong>natija</strong>, "
                       "keyin <strong>sabab</strong>. Sabab <em>потому́ что</em> "
                       "bilan keladi. <em>Зна́чит</em> va <em>сле́довательно</em> "
                       "xulosa chiqaradi, sabab aytmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Из-за</strong> "
                "predlogi qaysi kelishikni oladi?</p>",
        "choices": ["Да́тельный", "Вини́тельный", "Твори́тельный", "Роди́тельный"],
        "correct": "Роди́тельный",
        "explanation": "<p><em>из-за дожд<strong>я́</strong></em>, <em>из-за "
                       "боле́зн<strong>и</strong></em> — <strong>Роди́тельный</strong> "
                       "(кого́? чего́?).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Благодаря́</strong> "
                "predlogi qaysi kelishikni oladi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Предло́жный", "Вини́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><strong>Да́тельный</strong> (кому́? чему́?), chunki "
                       "soʻzning ichida <em>благодари́ть</em> — «rahmat aytmoq» "
                       "turibdi, rahmat esa <strong>kimga</strong> aytiladi: "
                       "<em>благодаря́ учи́тел<strong>ю</strong></em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Благодаря́ ___ я "
                "по́нял э́ту те́му.</strong> (учи́тель)</p>",
        "choices": ["учи́теля", "учи́телем", "учи́телю", "учи́теле"],
        "correct": "учи́телю",
        "explanation": "<p><strong>Учи́телю</strong> — Да́тельный. Bu darsning eng "
                       "koʻp uchraydigan xatosi <s>благодаря́ учи́теля</s> deb "
                       "Роди́тельный qoʻyish.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Из-за ___ мы "
                "опозда́ли на по́езд.</strong> (дождь)</p>",
        "choices": ["дождю́", "дождя́", "дождём", "дождь"],
        "correct": "дождя́",
        "explanation": "<p><strong>Дождя́</strong> — Роди́тельный, chunki "
                       "<em>из-за</em> shu kelishikni oladi. Natija yomon "
                       "(kechikdik), demak <em>благодаря́</em> emas, "
                       "<em>из-за</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Vergul qayerga qoʻyiladi?</p>"
                "<p><strong>Он опозда́л ___ потому́ что проспа́л.</strong></p>",
        "choices": ["Vergul kerak emas", "«что» dan keyin",
                    "«потому́» va «что» orasiga", "«потому́» dan oldin"],
        "correct": "«потому́» dan oldin",
        "explanation": "<p><em>Он опозда́л<strong>,</strong> потому́ что "
                       "проспа́л.</em> Vergul butun bogʻlovchidan oldin turadi — bu "
                       "99% holat.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi bogʻlovchi bilan gapni "
                "<strong>boshlash</strong> mumkin?</p>",
        "choices": ["Так как", "Потому́ что", "Поэ́тому", "Зна́чит"],
        "correct": "Так как",
        "explanation": "<p><em><strong>Так как</strong> бы́ло хо́лодно, мы оста́лись "
                       "до́ма.</em> <em>Потому́ что</em> gapni boshlamaydi (faqat "
                       "«Почему́?» savoliga javob berganda). <em>Поэ́тому</em> va "
                       "<em>зна́чит</em> natija bildiradi, sabab emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Из-за того́ что</strong> "
                "dan keyin nima keladi?</p>",
        "choices": ["Faqat bitta ot", "Butun gap", "Infinitiv", "Sifat"],
        "correct": "Butun gap",
        "explanation": "<p><em>Из-за <strong>дождя́</strong></em> — ot bilan. "
                       "<em>Из-за того́ что <strong>шёл дождь</strong></em> — butun "
                       "gap bilan. <em>Того́ что</em> predlogni bogʻlovchiga "
                       "aylantiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Сле́довательно</strong> "
                "qaysi uslubga tegishli?</p>",
        "choices": ["Ogʻzaki, doʻstona", "Bolalar tili", "Rasmiy va ilmiy",
                    "Faqat sheʼriyat"],
        "correct": "Rasmiy va ilmiy",
        "explanation": "<p><strong>Сле́довательно</strong> — «binobarin». Ilmiy va "
                       "rasmiy matnlarda ishlatiladi. Ogʻzaki nutqda uning oʻrniga "
                       "<em>зна́чит</em> deyiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на мно́го "
                "чита́ет, ___ она́ хорошо́ говори́т по-ру́сски.</strong></p>",
        "choices": ["поэ́тому", "потому́ что", "из-за того́ что", "так как"],
        "correct": "поэ́тому",
        "explanation": "<p>Koʻp oʻqish — <strong>sabab</strong>, yaxshi gapirish — "
                       "<strong>natija</strong>. Natija <em>поэ́тому</em> bilan "
                       "keladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ по́мощи сосе́дей "
                "мы бы́стро сде́лали ремо́нт.</strong></p>",
        "choices": ["Из-за", "Благодаря́", "Поэ́тому", "Так как"],
        "correct": "Благодаря́",
        "explanation": "<p>Natija <strong>yaxshi</strong> — remont tez bitdi. Demak "
                       "<em>благодаря́</em> + Да́тельный: <strong>благодаря́ "
                       "по́мощи</strong>. <em>Из-за</em> yomon natijaga ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ пло́хой пого́ды "
                "матч отмени́ли.</strong></p>",
        "choices": ["Благодаря́", "Поэ́тому", "Из-за", "Зна́чит"],
        "correct": "Из-за",
        "explanation": "<p>Natija <strong>yomon</strong> — oʻyin bekor qilindi. "
                       "Demak <em>из-за</em> + Роди́тельный: <strong>из-за пло́хой "
                       "пого́ды</strong>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Потому́ что</strong> "
                "bilan <strong>так как</strong> ning asosiy farqi nimada?</p>",
        "choices": ["Maʼnosi butunlay boshqa",
                    "«Так как» faqat savolga javobda",
                    "«Потому́ что» vergul olmaydi",
                    "«Так как» gapni boshlay oladi"],
        "correct": "«Так как» gapni boshlay oladi",
        "explanation": "<p>Maʼnosi deyarli bir xil — farq <strong>oʻrnida</strong>. "
                       "<em>Так как</em> sababni oldinga chiqaradi, "
                       "<em>потому́ что</em> esa faqat asosiy gapdan keyin "
                       "turadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Зна́чит</strong> "
                "nima qiladi?</p>",
        "choices": ["Sababni aytadi", "Shartni aytadi", "Zidlikni koʻrsatadi",
                    "Xulosa chiqaradi"],
        "correct": "Xulosa chiqaradi",
        "explanation": "<p><strong>Зна́чит</strong> = «demak». U yangi sabab "
                       "aytmaydi, aytilganidan <strong>xulosa</strong> chiqaradi: "
                       "<em>Свет не гори́т — зна́чит, никого́ нет до́ма.</em></p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Так как бы́ло хо́лодно, мы оста́лись до́ма.",
                    "Поэ́тому что бы́ло хо́лодно, мы оста́лись до́ма.",
                    "Бы́ло хо́лодно, поэ́тому мы оста́лись до́ма.",
                    "Мы оста́лись до́ма, потому́ что бы́ло хо́лодно."],
        "correct": "Поэ́тому что бы́ло хо́лодно, мы оста́лись до́ма.",
        "explanation": "<p>Rus tilida <s>«поэ́тому что»</s> degan bogʻlovchi "
                       "<strong>yoʻq</strong>. Bu <em>поэ́тому</em> bilan "
                       "<em>потому́ что</em> ning aralashib ketishidan chiqadigan "
                       "eng mashhur xato.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Благодаря́ дру́га я нашёл рабо́ту.",
                    "Из-за дру́гу я нашёл рабо́ту.",
                    "Благодаря́ дру́гу я нашёл рабо́ту.",
                    "Благодаря́ дру́гом я нашёл рабо́ту."],
        "correct": "Благодаря́ дру́гу я нашёл рабо́ту.",
        "explanation": "<p><em>Благодаря́</em> + <strong>Да́тельный</strong> = "
                       "<strong>дру́гу</strong>. Natija yaxshi (ish topdim), demak "
                       "<em>из-за</em> ham toʻgʻri kelmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Почему́ ты вчера́ не "
                "пришёл?</strong></p>",
        "choices": ["— Поэ́тому я заболе́л.", "— Так как заболе́л.",
                    "— Потому́ что заболе́л.", "— Из-за заболе́л."],
        "correct": "— Потому́ что заболе́л.",
        "explanation": "<p>Bu <em>потому́ что</em> gapni boshlaydigan yagona "
                       "holat: <strong>«Почему́?» savoliga javob</strong>. "
                       "<em>Из-за</em> dan keyin ot kerak, feʼl emas.</p>",
    },
    {
        "text": "<p>Bu gapni teskarisidan ayting.</p><p><strong>Авто́бус "
                "слома́лся, поэ́тому мы шли пешко́м.</strong></p>",
        "choices": ["Авто́бус слома́лся, потому́ что мы шли пешко́м.",
                    "Мы шли пешко́м, поэ́тому авто́бус слома́лся.",
                    "Из-за того́ что мы шли пешко́м, авто́бус слома́лся.",
                    "Мы шли пешко́м, потому́ что авто́бус слома́лся."],
        "correct": "Мы шли пешко́м, потому́ что авто́бус слома́лся.",
        "explanation": "<p>Sabab — avtobus buzilgani, natija — piyoda ketganimiz. "
                       "Natijani oldinga chiqarsak, sabab <em>потому́ что</em> "
                       "bilan keladi. Qolgan variantlarda sabab bilan natija "
                       "oʻrin almashib, gap maʼnosiz boʻlib qolgan.</p>",
    },
]


# =====================================================================
# PR-67 — Qarama-qarshilik
# =====================================================================

Q_PR67 = [
    # 1–5 tanish
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Зато́</strong> nimani "
                "bildiradi?</p>",
        "choices": ["Shuning uchun — natija", "Chunki — sabab",
                    "Buning evaziga — kamchilik oʻrnini bosadi",
                    "Agar — shart"],
        "correct": "Buning evaziga — kamchilik oʻrnini bosadi",
        "explanation": "<p><em>Кварти́ра ма́ленькая, <strong>зато́</strong> "
                       "дешёвая.</em> Avval kamchilik, keyin uning oʻrnini bosadigan "
                       "yaxshi tomon. Oʻzbekchada bunga bitta soʻzli tarjima "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Хотя́ бы</strong> "
                "nimani bildiradi?</p>",
        "choices": ["Hech boʻlmaganda", "Garchi …sa ham", "Shunga qaramay",
                    "Buning evaziga"],
        "correct": "Hech boʻlmaganda",
        "explanation": "<p><em>Позвони́ <strong>хотя́ бы</strong> ве́чером</em> — "
                       "«hech boʻlmaganda kechqurun qoʻngʻiroq qil». Bu "
                       "<em>хотя́</em> bogʻlovchisi emas, butunlay boshqa ibora.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на чита́ет, ___ "
                "Бекзо́д пи́шет.</strong></p>",
        "choices": ["но", "зато́", "хотя́", "а"],
        "correct": "а",
        "explanation": "<p><strong>А</strong> — <strong>solishtirish</strong>. "
                       "Oʻzbekchada «Bekzod <strong>esa</strong> yozyapti» — «esa» "
                       "bor joyda ruschada <em>а</em> turadi. Bu yerda hech qanday "
                       "zidlik yoʻq.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Одна́ко</strong> qaysi "
                "uslubga tegishli?</p>",
        "choices": ["Faqat bolalar tili", "Kitobiy va yozma", "Ogʻzaki, doʻstona",
                    "Faqat savol gaplarda"],
        "correct": "Kitobiy va yozma",
        "explanation": "<p><strong>Одна́ко</strong> — <em>но</em> ning kitobiy "
                       "varianti. Ogʻzaki nutqda u gʻalati eshitiladi; u yerda "
                       "<em>но</em> deyiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>А, но, зато́, "
                "хотя́</strong> — bu soʻzlarning oldiga nima qoʻyiladi?</p>",
        "choices": ["Vergul", "Tire", "Ikki nuqta", "Hech narsa"],
        "correct": "Vergul",
        "explanation": "<p>Hammasining oldiga <strong>vergul</strong>: <em>Дом "
                       "ста́рый<strong>,</strong> но кре́пкий</em> · <em>Мы "
                       "пошли́<strong>,</strong> хотя́ бы́ло по́здно</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он до́лго учи́лся, "
                "___ экза́мен не сдал.</strong></p>",
        "choices": ["а", "зато́", "и", "но"],
        "correct": "но",
        "explanation": "<p>Uzoq oʻqigan odam imtihondan oʻtishi <strong>kutiladi</strong> "
                       "— ikkinchi qism shu kutishni buzyapti. Bu <em>а</em> emas, "
                       "chunki gap solishtirish haqida emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Кварти́ра "
                "ма́ленькая, ___ дешёвая.</strong></p>",
        "choices": ["зато́", "а", "одна́ко", "хотя́"],
        "correct": "зато́",
        "explanation": "<p>Kamchilik (kichkina) aytildi, keyin uning oʻrnini "
                       "bosadigan yaxshilik (arzon) kelyapti — bu aynan "
                       "<strong>зато́</strong>. <em>Но</em> ham mumkin, lekin "
                       "kompensatsiya maʼnosi yoʻqoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ бы́ло по́здно, "
                "мы пошли́ гуля́ть.</strong></p>",
        "choices": ["Но", "Зато́", "Одна́ко", "Хотя́"],
        "correct": "Хотя́",
        "explanation": "<p>Faqat <strong>хотя́</strong> ergash gap boshlab, undan "
                       "keyin asosiy gapni olib kela oladi. <em>Но</em>, "
                       "<em>зато́</em> va <em>одна́ко</em> ikki gapni bogʻlaydi, "
                       "ergash gap qurmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я о́чень за́нят. "
                "Позвони́ мне ___ ве́чером.</strong></p>",
        "choices": ["хотя́", "хотя́ бы", "зато́", "одна́ко"],
        "correct": "хотя́ бы",
        "explanation": "<p>«Hech boʻlmaganda kechqurun qoʻngʻiroq qil» — "
                       "<strong>хотя́ бы</strong>. <em>Хотя́</em> ning oʻzi bu yerda "
                       "ishlamaydi, chunki undan keyin butun gap kelishi kerak "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi? (kitobiy uslub)</p><p><strong>Он "
                "обеща́л прийти́, ___ не пришёл.</strong></p>",
        "choices": ["зато́", "а", "одна́ко", "хотя́ бы"],
        "correct": "одна́ко",
        "explanation": "<p>Yozma, kitobiy uslubda <em>но</em> ning oʻrniga "
                       "<strong>одна́ко</strong> ishlatiladi. <em>Зато́</em> "
                       "toʻgʻri kelmaydi, chunki kelmaganlik — yaxshi tomon "
                       "emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Он всё-таки "
                "пришёл.</strong> — bu nimani bildiradi?</p>",
        "choices": ["Umuman kelmadi", "Har doim keladi",
                    "Baribir keldi — kutilmaganda",
                    "Juda erta keldi"],
        "correct": "Baribir keldi — kutilmaganda",
        "explanation": "<p><strong>Всё-таки</strong> = «baribir». U kutilmagan, "
                       "lekin sodir boʻlgan narsani taʼkidlaydi. Ogʻzaki nutqda "
                       "juda koʻp ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы живём в "
                "Ташке́нте, ___ на́ши роди́тели — в Наманга́не.</strong></p>",
        "choices": ["но", "а", "зато́", "хотя́"],
        "correct": "а",
        "explanation": "<p>Ikkala gap ham toʻgʻri, ular shunchaki solishtirilyapti: "
                       "«ota-onamiz <strong>esa</strong> Namanganda». Demak "
                       "<strong>а</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻzbekchadagi qaysi soʻz "
                "ruscha <strong>а</strong> ga toʻgʻri keladi?</p>",
        "choices": ["lekin", "chunki", "garchi", "esa"],
        "correct": "esa",
        "explanation": "<p>Bu butun darsni hal qiladigan sinov: oʻzbekcha "
                       "<strong>«esa»</strong> → <strong>а</strong>, oʻzbekcha "
                       "<strong>«lekin / ammo»</strong> → <strong>но</strong>. "
                       "«Chunki» — <em>потому́ что</em>, «garchi» — "
                       "<em>хотя́</em>.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Го́род ма́ленький, но "
                "ти́хий</strong> va <strong>Го́род ма́ленький, зато́ ти́хий</strong> "
                "— farqi nimada?</p>",
        "choices": ["Farqi umuman yoʻq",
                    "«Зато́» kompensatsiyani taʼkidlaydi",
                    "«Зато́» gapni inkorga aylantiradi",
                    "«Но» faqat yozma nutqda ishlatiladi"],
        "correct": "«Зато́» kompensatsiyani taʼkidlaydi",
        "explanation": "<p>Ikkalasi ham toʻgʻri, lekin <em>но</em> shunchaki ikki "
                       "belgini bogʻlaydi, <strong>зато́</strong> esa "
                       "<strong>kompensatsiya</strong> qiladi: «kichkina — buning "
                       "evaziga tinch».</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Qaysi soʻz ergash gap boshlab, "
                "undan keyin vergul va asosiy gap kela oladi?</p>",
        "choices": ["Хотя́", "Но", "Зато́", "Всё-таки"],
        "correct": "Хотя́",
        "explanation": "<p><em><strong>Хотя́</strong> бы́ло по́здно, мы пошли́.</em> "
                       "Qolganlari faqat ikki gapni bogʻlaydi va gap boshida shunday "
                       "ishlata olmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Тем не ме́нее</strong> "
                "qayerda ishlatiladi?</p>",
        "choices": ["Doʻstlar bilan suhbatda", "Bolalar ertagida",
                    "Rasmiy va yozma matnda", "Faqat savollarda"],
        "correct": "Rasmiy va yozma matnda",
        "explanation": "<p><strong>Тем не ме́нее</strong> = «shunga qaramasdan». Bu "
                       "eng rasmiy variant. Ogʻzaki nutqda uning oʻrniga "
                       "<em>но</em> yoki <em>всё-таки</em> deyiladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я хоте́л пойти́, а не смог.",
                    "Я люблю́ ко́фе, а Жасу́р лю́бит чай.",
                    "Бы́ло тру́дно, но интере́сно.",
                    "Хотя́ бы́ло по́здно, мы пошли́."],
        "correct": "Я хоте́л пойти́, а не смог.",
        "explanation": "<p><s>а</s> → <strong>но</strong>. Bu solishtirish emas: "
                       "«bormoqchi edim» dan keyin «bordim» kutiladi, «bora "
                       "olmadim» esa shu kutishni buzadi.</p>",
    },
    {
        "text": "<p>Qaysi gap tabiiy eshitiladi?</p>",
        "choices": ["Кварти́ра ма́ленькая, зато́ ста́рая.",
                    "Кварти́ра ма́ленькая, зато́ дешёвая.",
                    "Кварти́ра ма́ленькая, зато́ далеко́ от це́нтра.",
                    "Кварти́ра ма́ленькая, зато́ шу́мная."],
        "correct": "Кварти́ра ма́ленькая, зато́ дешёвая.",
        "explanation": "<p><strong>Зато́</strong> dan keyin har doim "
                       "<strong>ijobiy</strong> tomon keladi. Eskilik, uzoqlik va "
                       "shovqin — bularning hammasi yana kamchilik, shuning uchun "
                       "qolgan uch gap gʻalati chiqadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Qaysi javob tabiiy?</p><p><strong>— Ну как но́вая "
                "рабо́та?</strong></p>",
        "choices": ["— Далеко́ от до́ма, хотя́ зарпла́та хоро́шая.",
                    "— Далеко́ от до́ма, а зарпла́та хоро́шая.",
                    "— Далеко́ от до́ма, зато́ зарпла́та хоро́шая.",
                    "— Далеко́ от до́ма, потому́ что зарпла́та хоро́шая."],
        "correct": "— Далеко́ от до́ма, зато́ зарпла́та хоро́шая.",
        "explanation": "<p>Kamchilik (uzoq) aytildi, keyin uning oʻrnini bosadigan "
                       "yaxshilik (yaxshi maosh) kelyapti — bu <strong>зато́</strong> "
                       "uchun ideal oʻrin. Oxirgi variant sababni notoʻgʻri "
                       "bogʻlaydi.</p>",
    },
    {
        "text": "<p>Bu gapning ruschasi qaysi biri?</p><p><strong>Kech boʻlsa "
                "ham, biz sayr qilgani chiqdik.</strong></p>",
        "choices": ["Зато́ бы́ло по́здно, мы пошли́ гуля́ть.",
                    "Хотя́ бы́ло по́здно, мы пошли́ гуля́ть.",
                    "Потому́ что бы́ло по́здно, мы пошли́ гуля́ть.",
                    "Одна́ко бы́ло по́здно, мы пошли́ гуля́ть."],
        "correct": "Хотя́ бы́ло по́здно, мы пошли́ гуля́ть.",
        "explanation": "<p>Oʻzbekcha «…<strong>sa ham</strong>» = "
                       "<strong>хотя́</strong>. Ruschada asosiy gapda hech narsa "
                       "kerak emas — <em>хотя́</em> ning oʻzi yetarli (istasangiz "
                       "<em>но</em> yoki <em>всё же</em> qoʻshsangiz ham "
                       "boʻladi).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-65 Mashq: Если va когда — shart va vaqt",
        "description": (
            "Когда́ — aniq boʻladigan narsa, е́сли — boʻlishi mumkin narsa. "
            "Kelasi zamon qoidasi, feʼl turi va vaqt bogʻlovchilari."
        ),
        "tutorial": "PR-65:",
        "questions": Q_PR65,
    },
    {
        "title": "PR-66 Mashq: Sabab va natija — потому что, поэтому, так как",
        "description": (
            "Потому́ что sababni, поэ́тому natijani aytadi. Vergul, так как ning "
            "oʻrni va из-за + Р.п. / благодаря́ + Д.п."
        ),
        "tutorial": "PR-66:",
        "questions": Q_PR66,
    },
    {
        "title": "PR-67 Mashq: Хотя, но, зато — qarama-qarshilik",
        "description": (
            "Oʻzbekcha «esa» — А, «lekin» — НО. Зато́ ning tartibi, хотя́ ning "
            "oʻrni va одна́ко / тем не ме́нее uslubi."
        ),
        "tutorial": "PR-67:",
        "questions": Q_PR67,
    },
]
