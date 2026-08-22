# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-56 … PR-58.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_56_58.py --master=prime \\
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
# PR-56 — Harakat feʼllari 2
# =====================================================================

Q_PR56 = [
    # 1–5 tanish
    {
        "text": "<p><strong>е́хать</strong> ning koʻp yoʻnalishli jufti qaysi?</p>",
        "choices": ["е́здить", "ходи́ть", "пое́хать", "уе́хать"],
        "correct": "е́здить",
        "explanation": "<p><em>Е́хать ↔ е́здить</em> — xuddi <em>идти́ ↔ ходи́ть</em> "
                       "kabi. Ikkalasi ham НСВ; farq yoʻnalishda.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ка́ждый день я ___ на "
                "рабо́ту.</strong></p>",
        "choices": ["е́ду", "е́зжу", "е́хал", "пое́ду"],
        "correct": "е́зжу",
        "explanation": "<p>«Ка́ждый день» — takror, demak koʻp yoʻnalish. Oʻzbekcha: "
                       "«borib turaman».</p>",
    },
    {
        "text": "<p><strong>носи́ть</strong> ning ikkinchi maʼnosi nima?</p>",
        "choices": ["yugurmoq", "kiymoq", "haydamoq", "uchmoq"],
        "correct": "kiymoq",
        "explanation": "<p><em>Она́ но́сит очки́</em> — koʻzoynak taqadi. Bu mantiqiy: "
                       "kiyim — doim oʻzing bilan olib yuradigan narsa. "
                       "<em>Нести́</em> bu maʼnoda ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Rus tilida nechta harakat feʼli juftligi bor?</p>",
        "choices": ["Ikkita", "Toʻrtta", "Sakkizta", "Oʻn ikkita"],
        "correct": "Sakkizta",
        "explanation": "<p><em>идти́/ходи́ть, е́хать/е́здить, бежа́ть/бе́гать, "
                       "лете́ть/лета́ть, плыть/пла́вать, нести́/носи́ть, "
                       "везти́/вози́ть, вести́/води́ть</em>. Mantiq hammasida bir "
                       "xil.</p>",
    },
    {
        "text": "<p><strong>вожу́</strong> qaysi ikki feʼlga tegishli?</p>",
        "choices": ["вози́ть va води́ть", "вести́ va везти́",
                    "ходи́ть va е́здить", "носи́ть va вози́ть"],
        "correct": "вози́ть va води́ть",
        "explanation": "<p><em>Вожу́ дете́й в шко́лу</em> (tashiyman — вози́ть) va "
                       "<em>вожу́ маши́ну</em> (haydayman — води́ть). Farqni gap "
                       "koʻrsatadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ле́том я ___ в "
                "дере́вню.</strong> («borib keldim» maʼnosida)</p>",
        "choices": ["е́хал", "е́здил", "е́ду", "е́зжу"],
        "correct": "е́здил",
        "explanation": "<p>Borib-kelish — koʻp yoʻnalish. <em>Е́хал</em> boʻlsa, gap "
                       "yoʻl haqida boʻlardi: «ketayotgan edim».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Зимо́й я ___ "
                "ша́пку.</strong></p>",
        "choices": ["несу́", "ношу́", "вожу́", "везу́"],
        "correct": "ношу́",
        "explanation": "<p>Kiyim uchun har doim <em>носи́ть</em>. <em>Несу́</em> "
                       "«qoʻlimda olib ketyapman» degan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Самолёт ___ в "
                "Москву́.</strong> (hozir)</p>",
        "choices": ["лета́ет", "лети́т", "лета́л", "полети́т"],
        "correct": "лети́т",
        "explanation": "<p>Hozir, bir tomonga — <em>лете́ть</em>. <em>Лета́ет</em> "
                       "muntazam qatnovni bildirardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ ка́ждое "
                "у́тро.</strong> (sport)</p>",
        "choices": ["бежи́т", "бе́гает", "бежа́л", "побежи́т"],
        "correct": "бе́гает",
        "explanation": "<p>«Ка́ждое у́тро» — takror, demak koʻp yoʻnalish: "
                       "<em>бе́гать</em>. Bu sport maʼnosi.</p>",
    },
    {
        "text": "<p><strong>бежа́ть</strong> feʼlining «они́» shakli qaysi?</p>",
        "choices": ["бежа́т", "бегу́т", "бежу́т", "бе́гают"],
        "correct": "бегу́т",
        "explanation": "<p><em>Бежа́ть</em> aralash tuslanadi: <em>бегу́, бежи́шь, "
                       "бежи́т, бежи́м, бежи́те, <strong>бегу́т</strong></em> — "
                       "Г chetlarda, Ж oʻrtada, xuddi <em>мочь</em> kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ хлеб на ры́нок "
                "ка́ждое у́тро.</strong></p>",
        "choices": ["вёз", "во́зит", "везёт", "но́сит"],
        "correct": "во́зит",
        "explanation": "<p>«Ка́ждое у́тро» — takror, va transport bilan — demak "
                       "<em>вози́ть</em>. <em>Вёз</em> bir marta boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Сейча́с я ___ "
                "кни́ги в библиоте́ку.</strong></p>",
        "choices": ["ношу́", "несу́", "вожу́", "везу́"],
        "correct": "несу́",
        "explanation": "<p>«Сейча́с» — hozir, bir tomonga, qoʻlda: <em>нести́</em>. "
                       "<em>Ношу́</em> muntazam boʻlardi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>е́хал</strong> va <strong>е́здил</strong> — farqi "
                "nima?</p>",
        "choices": ["Yoʻlda edim · borib keldim", "Borib keldim · yoʻlda edim",
                    "НСВ · СВ", "Ikkalasi bir xil"],
        "correct": "Yoʻlda edim · borib keldim",
        "explanation": "<p>Xuddi <em>шёл ↔ ходи́л</em> kabi. Ikkalasi ham НСВ — farq "
                       "vid emas, yoʻnalish.</p>",
    },
    {
        "text": "<p>Harakat juftliklarining ikkala shakli qaysi vidda?</p>",
        "choices": ["Birinchisi СВ, ikkinchisi НСВ", "Ikkalasi ham НСВ",
                    "Ikkalasi ham СВ", "Birinchisi НСВ, ikkinchisi СВ"],
        "correct": "Ikkalasi ham НСВ",
        "explanation": "<p>Bu muhim: <em>ходи́л</em> tugagan safarni bildirsa ham, u "
                       "<strong>СВ emas</strong>. Farq vidda emas, "
                       "yoʻnalishda.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida bu farq qanday koʻrsatiladi?</p>",
        "choices": ["Qoʻshimcha feʼl bilan: ketyapman · borib turaman · borib keldim",
                    "Koʻrsatilmaydi",
                    "Prefiks bilan",
                    "Faqat ohang bilan"],
        "correct": "Qoʻshimcha feʼl bilan: ketyapman · borib turaman · borib keldim",
        "explanation": "<p>Ikkala tilda ham farq bor — faqat vosita boshqa: "
                       "oʻzbekchada qoʻshimcha feʼl, ruschada alohida soʻz.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda obyekt (nimadir olib yuriladi) bor?</p>",
        "choices": ["идти́ / ходи́ть", "лете́ть / лета́ть",
                    "нести́ / носи́ть", "плыть / пла́вать"],
        "correct": "нести́ / носи́ть",
        "explanation": "<p><em>Нести́/носи́ть</em>, <em>везти́/вози́ть</em>, "
                       "<em>вести́/води́ть</em> — bu turkumda har doim nimadir yoki "
                       "kimdir olib yuriladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Самолёт лети́т в Москву́.", "Ка́ждый день я е́ду на рабо́ту.",
                    "Он бе́гает по утра́м.", "Она́ но́сит очки́."],
        "correct": "Ка́ждый день я е́ду на рабо́ту.",
        "explanation": "<p>Toʻgʻrisi — <strong>я е́зжу на рабо́ту</strong>. «Ка́ждый "
                       "день» takrorni bildiradi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Она́ несёт очки́.", "Она́ но́сит очки́.",
                    "Она́ во́зит очки́.", "Она́ везёт очки́."],
        "correct": "Она́ но́сит очки́.",
        "explanation": "<p>Kiyim va aksessuarlar uchun faqat <em>носи́ть</em>. "
                       "<em>Несёт</em> «qoʻlida olib ketyapti» degan boʻlardi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Где ты был ле́том?</strong></p>",
        "choices": ["— Я е́здил в Самарка́нд.", "— Я е́хал в Самарка́нд.",
                    "— Я е́ду в Самарка́нд.", "— Я е́зжу в Самарка́нд."],
        "correct": "— Я е́здил в Самарка́нд.",
        "explanation": "<p>Savol butun safar haqida, demak borib-kelish: "
                       "<strong>е́здил</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Hozir ishga "
                "ketyapman, lekin odatda metroda borib turaman.</strong></p>",
        "choices": ["Сейча́с я е́зжу на рабо́ту, но обы́чно е́ду на метро́.",
                    "Сейча́с я е́ду на рабо́ту, но обы́чно е́зжу на метро́.",
                    "Сейча́с я е́ду на рабо́ту, но обы́чно е́ду на метро́.",
                    "Сейча́с я е́хал на рабо́ту, но обы́чно е́зжу на метро́."],
        "correct": "Сейча́с я е́ду на рабо́ту, но обы́чно е́зжу на метро́.",
        "explanation": "<p>«Hozir» — bir tomonga (<strong>е́ду</strong>), «odatda» — "
                       "takror (<strong>е́зжу</strong>).</p>",
    },
]


# =====================================================================
# PR-57 — Harakat feʼllarining prefikslari
# =====================================================================

Q_PR57 = [
    # 1–5 tanish
    {
        "text": "<p>Prefiks <strong>идти́</strong> ga qoʻshilsa, qaysi vid "
                "chiqadi?</p>",
        "choices": ["НСВ", "СВ", "Ikkalasi", "Vid oʻzgarmaydi"],
        "correct": "СВ",
        "explanation": "<p><em>Прийти́, уйти́, войти́</em> — hammasi СВ. "
                       "<em>Ходи́ть</em> ga qoʻshilsa esa НСВ: <em>приходи́ть, "
                       "уходи́ть</em>.</p>",
    },
    {
        "text": "<p><strong>при-</strong> prefiksi nimani bildiradi?</p>",
        "choices": ["ketmoq", "kelmoq", "kirmoq", "chiqmoq"],
        "correct": "kelmoq",
        "explanation": "<p><em>Прийти́, прие́хать, прилете́ть</em> — yetib kelish. "
                       "Uning teskarisi — <strong>у-</strong>: <em>уйти́, "
                       "уе́хать</em>.</p>",
    },
    {
        "text": "<p><strong>вы́йти</strong> soʻzida urgʻu qayerda?</p>",
        "choices": ["вы-", "-й-", "-ти", "Urgʻu yoʻq"],
        "correct": "вы-",
        "explanation": "<p>СВ feʼllarda <strong>вы-</strong> har doim urgʻuli: "
                       "<em>вы́йти, вы́шел, вы́йду, вы́учить, вы́брать</em>. НСВ da "
                       "esa oddiy: <em>выходи́ть</em>.</p>",
    },
    {
        "text": "<p><strong>прийти́</strong> ning НСВ jufti qaysi?</p>",
        "choices": ["прие́хать", "приходи́ть", "приезжа́ть", "пойти́"],
        "correct": "приходи́ть",
        "explanation": "<p>СВ <em>идти́</em> dan, НСВ esa <em>ходи́ть</em> dan "
                       "yasaladi. Shuning uchun <em>прийти́ ↔ приходи́ть</em>.</p>",
    },
    {
        "text": "<p><strong>е́хать</strong> ning prefiksli НСВ shakli nimadan "
                "yasaladi?</p>",
        "choices": ["-е́здить", "-езжа́ть", "-е́хать", "-е́ду"],
        "correct": "-езжа́ть",
        "explanation": "<p><em>Приезжа́ть, уезжа́ть, выезжа́ть</em> — "
                       "<em>«приездить»</em> emas. Bu kichkina, lekin muhim "
                       "tafsilot.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ ка́ждый день в "
                "во́семь.</strong> (прийти́ / приходи́ть)</p>",
        "choices": ["пришёл", "прихо́дит", "придёт", "прийти́"],
        "correct": "прихо́дит",
        "explanation": "<p>«Ка́ждый день» — takror, demak НСВ: "
                       "<strong>приходи́ть</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вчера́ он ___ в "
                "де́вять.</strong></p>",
        "choices": ["приходи́л", "пришёл", "прихо́дит", "придёт"],
        "correct": "пришёл",
        "explanation": "<p>«Вчера́ … в де́вять» — bir marta, aniq vaqt, tugagan ish. "
                       "Demak <strong>СВ</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он вы́шел ___ "
                "до́ма.</strong></p>",
        "choices": ["в", "из", "к", "до"],
        "correct": "из",
        "explanation": "<p>Prefiks va predlog juftlashadi: <em><strong>вы</strong>йти "
                       "<strong>из</strong></em>, <em><strong>в</strong>ойти "
                       "<strong>в</strong></em>, <em><strong>до</strong>йти "
                       "<strong>до</strong></em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ к окну́.</strong> "
                "(«yaqinlashdi» maʼnosida)</p>",
        "choices": ["отошёл", "подошёл", "перешёл", "дошёл"],
        "correct": "подошёл",
        "explanation": "<p><strong>Под-</strong> — yaqinlashish, va u <em>к</em> "
                       "predlogi bilan juftlashadi. Teskarisi — <em>отойти́ "
                       "от</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ у́лицу.</strong> "
                "(«kesib oʻtdi» maʼnosida)</p>",
        "choices": ["дошёл", "вошёл", "перешёл", "подошёл"],
        "correct": "перешёл",
        "explanation": "<p><strong>Пере-</strong> — kesib oʻtish: <em>перейти́ "
                       "у́лицу, перейти́ мост</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ за́втра.</strong> "
                "(приезжа́ть)</p>",
        "choices": ["приезди́м", "приезжа́ем", "прие́хаем", "прие́здим"],
        "correct": "приезжа́ем",
        "explanation": "<p>НСВ <em>-езжа́ть</em> dan yasaladi: <em>приезжа́ю, "
                       "приезжа́ешь, приезжа́ем</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ до "
                "шко́лы.</strong></p>",
        "choices": ["вошёл", "дошёл", "отошёл", "вы́шел"],
        "correct": "дошёл",
        "explanation": "<p><strong>До-</strong> — maqsadga yetib borish, va u "
                       "<em>до</em> predlogi bilan keladi: <em>дойти́ до "
                       "шко́лы</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega prefikslar tizimi PR-52 va PR-55 ni birlashtiradi?</p>",
        "choices": ["Chunki prefiks + идти́ = СВ, prefiks + ходи́ть = НСВ",
                    "Chunki prefikslar vidni oʻzgartirmaydi",
                    "Chunki harakat feʼllari СВ boʻlmaydi",
                    "Ular birlashmaydi"],
        "correct": "Chunki prefiks + идти́ = СВ, prefiks + ходи́ть = НСВ",
        "explanation": "<p>Bitta prefiks — bitta tayyor vid juftligi. Vid (PR-52) va "
                       "harakat (PR-55) tizimlari shu yerda bir joyga "
                       "keladi.</p>",
    },
    {
        "text": "<p>Qaysi juftlikda prefiks va predlog mos keladi?</p>",
        "choices": ["подойти́ … к", "подойти́ … из", "подойти́ … до", "подойти́ … в"],
        "correct": "подойти́ … к",
        "explanation": "<p><em>Подойти́ <strong>к</strong> окну́</em>. Prefiksni "
                       "bilsangiz, predlogni ham deyarli bilasiz — ularni juftlab "
                       "yodlang.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida bu maʼnolar qanday beriladi?</p>",
        "choices": ["Alohida feʼllar bilan: kelmoq, ketmoq, kirmoq, chiqmoq",
                    "Prefikslar bilan",
                    "Faqat bitta feʼl bilan",
                    "Qoʻshimchalar bilan"],
        "correct": "Alohida feʼllar bilan: kelmoq, ketmoq, kirmoq, chiqmoq",
        "explanation": "<p>Oʻzbekchada yettita boshqa-boshqa oʻzak; ruschada bitta "
                       "oʻzak va sakkizta prefiks. Ruscha tizim boshda qiyinroq, "
                       "lekin keyin tejamkorroq.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он пришёл. · Он "
                "приходи́л.</strong></p>",
        "choices": ["Bir marta keldi · muntazam kelib turardi",
                    "Muntazam · bir marta", "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Bir marta keldi · muntazam kelib turardi",
        "explanation": "<p><em>Пришёл</em> — СВ (<em>идти́</em> dan), bir marta. "
                       "<em>Приходи́л</em> — НСВ (<em>ходи́ть</em> dan), "
                       "takror.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он вошёл в дом.", "Он вы́шел из до́ма.",
                    "Мы приезди́м за́втра.", "Он подошёл к окну́."],
        "correct": "Мы приезди́м за́втра.",
        "explanation": "<p>Toʻgʻrisi — <strong>Мы приезжа́ем за́втра</strong>. "
                       "Prefiksli НСВ <em>-езжа́ть</em> dan yasaladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он вышёл из до́ма.", "Он вы́шел из до́ма.",
                    "Он вы́шел в до́ма.", "Он выхо́дил из до́ма вчера́ в во́семь."],
        "correct": "Он вы́шел из до́ма.",
        "explanation": "<p><strong>Вы-</strong> СВ da urgʻuli: <em>вы́шел</em>. Va "
                       "predlog <em>из</em>. Oxirgi variant НСВ ni bir martalik "
                       "vaqt bilan qoʻshgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Когда́ он прихо́дит?</strong></p>",
        "choices": ["— Обы́чно в во́семь.", "— Вчера́ в во́семь.",
                    "— Оди́н раз в во́семь.", "— Наконе́ц в во́семь."],
        "correct": "— Обы́чно в во́семь.",
        "explanation": "<p>Savol НСВ da (<em>прихо́дит</em> — takror), demak javob "
                       "ham odat haqida: <strong>обы́чно</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>U koʻchani kesib "
                "oʻtdi va bozorgacha yetib bordi.</strong></p>",
        "choices": ["Он вошёл у́лицу и вы́шел до ры́нка.",
                    "Он перешёл у́лицу и дошёл до ры́нка.",
                    "Он перешёл у́лицу и вошёл до ры́нка.",
                    "Он подошёл у́лицу и дошёл до ры́нка."],
        "correct": "Он перешёл у́лицу и дошёл до ры́нка.",
        "explanation": "<p><strong>Пере-</strong> — kesib oʻtish, <strong>до-</strong> "
                       "— yetib borish (<em>до</em> predlogi bilan).</p>",
    },
]


# =====================================================================
# PR-58 — Maʼnoni oʻzgartiradigan prefikslar
# =====================================================================

Q_PR58 = [
    # 1–5 tanish
    {
        "text": "<p><strong>по-</strong> prefiksi harakat feʼliga nima "
                "qoʻshadi?</p>",
        "choices": ["Tugash", "Boshlanish — yoʻlga chiqish",
                    "Takror", "Yoʻnalish oʻzgarishi"],
        "correct": "Boshlanish — yoʻlga chiqish",
        "explanation": "<p><em>Он пошёл в шко́лу</em> — maktabga joʻnadi. <em>Я "
                       "пошёл!</em> — men ketdim. <em>Пое́хали!</em> — ketdik.</p>",
    },
    {
        "text": "<p><strong>зайти́</strong> nimani bildiradi?</p>",
        "choices": ["kirmoq (umuman)", "kirib oʻtmoq (qisqa vaqtga)",
                    "chiqmoq", "yetib bormoq"],
        "correct": "kirib oʻtmoq (qisqa vaqtga)",
        "explanation": "<p><em>По доро́ге домо́й я зашёл в магази́н</em> — asosiy "
                       "yoʻlni buzmasdan, qisqa vaqtga. <em>Войти́</em> shunchaki "
                       "«kirmoq» degan boʻlardi.</p>",
    },
    {
        "text": "<p><strong>найти́</strong> qaysi ikki qismdan tuzilgan?</p>",
        "choices": ["на + идти́", "най + ти", "на + йти", "на + ходи́ть"],
        "correct": "на + идти́",
        "explanation": "<p>Soʻzma-soʻz «yurib borib ustiga tushmoq». Shuning uchun u "
                       "<em>идти́</em> kabi turlanadi: <em>найду́, нашёл, "
                       "нашла́</em>.</p>",
    },
    {
        "text": "<p><strong>раз- + -ся</strong> nimani bildiradi?</p>",
        "choices": ["yigʻilmoq", "tarqalmoq", "kirmoq", "boshlamoq"],
        "correct": "tarqalmoq",
        "explanation": "<p><em>По́сле уро́ка все разошли́сь</em> — hamma tarqaldi. "
                       "Teskarisi — <em>с- + -ся</em>: <em>сошли́сь</em> "
                       "(yigʻilishdi).</p>",
    },
    {
        "text": "<p>Bu soʻzlarning oʻtgan zamon naqshi qanday?</p>"
                "<p><strong>прийти́ · уйти́ · пойти́ · найти́</strong></p>",
        "choices": ["-ил / -ила / -или", "-шёл / -шла / -шли",
                    "-ал / -ала / -али", "-ёл / -ёла / -ёли"],
        "correct": "-шёл / -шла / -шли",
        "explanation": "<p><em>Пришёл, ушёл, пошёл, нашёл</em> — hammasi <em>шёл — "
                       "шла — шли</em> naqshida, chunki ularning oʻzagi "
                       "bitta.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>По доро́ге домо́й я ___ "
                "в магази́н.</strong></p>",
        "choices": ["вошёл", "зашёл", "пришёл", "дошёл"],
        "correct": "зашёл",
        "explanation": "<p><strong>За-</strong> — yoʻl-yoʻlakay, qisqa vaqtga "
                       "kirish.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___!</strong> "
                "(«ketdim, xayr» maʼnosida)</p>",
        "choices": ["иду́", "пошёл", "ушёл", "хожу́"],
        "correct": "пошёл",
        "explanation": "<p><em>Я пошёл!</em> — yoʻlga chiqdim. Bu rus tilida eng koʻp "
                       "ishlatiladigan xayrlashuvlardan biri.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он до́лго иска́л и "
                "наконе́ц ___ ключи́.</strong></p>",
        "choices": ["находи́л", "нашёл", "найдёт", "найти́"],
        "correct": "нашёл",
        "explanation": "<p>«Наконе́ц» — natija, demak СВ. Va <em>найти́</em> "
                       "<em>идти́</em> kabi turlanadi: <em>нашёл</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>По́сле уро́ка все "
                "___.</strong> («tarqalishdi» maʼnosida)</p>",
        "choices": ["сошли́сь", "разошли́сь", "пришли́", "вошли́"],
        "correct": "разошли́сь",
        "explanation": "<p><em>Раз- + -ся</em> — tarqalish. <em>Сошли́сь</em> "
                       "teskarisi: yigʻilishdi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ ми́мо и не "
                "уви́дел меня́.</strong></p>",
        "choices": ["пришёл", "прошёл", "подошёл", "вошёл"],
        "correct": "прошёл",
        "explanation": "<p><strong>Про-</strong> — oʻtib ketish. <em>Пройти́ "
                       "ми́мо</em> — yonidan oʻtib ketmoq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Кот ___ с кры́ши "
                "вниз.</strong></p>",
        "choices": ["вошёл", "сошёл", "зашёл", "перешёл"],
        "correct": "сошёл",
        "explanation": "<p><strong>С-</strong> — pastga tushish: <em>сойти́ с "
                       "кры́ши, сойти́ с ле́стницы</em>.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я иду́ в шко́лу. · Я "
                "пошёл в шко́лу.</strong></p>",
        "choices": ["Hozir yoʻldaman · yoʻlga chiqdim",
                    "Yoʻlga chiqdim · hozir yoʻldaman",
                    "Ikkalasi bir xil", "Ikkinchisi kelasi zamon"],
        "correct": "Hozir yoʻldaman · yoʻlga chiqdim",
        "explanation": "<p><strong>По-</strong> harakatning <b>boshlanishini</b> "
                       "bildiradi. <em>Иду́</em> — jarayon, <em>пошёл</em> — "
                       "boshlanish.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Nega <strong>найти́</strong> «topmoq» degani?</p>",
        "choices": ["Chunki topish — yurishning natijasi: yurib borib ustiga tushmoq",
                    "Chunki «най» qadimgi oʻzak",
                    "Bu tasodifiy oʻxshashlik",
                    "Chunki u ходи́ть dan yasalgan"],
        "correct": "Chunki topish — yurishning natijasi: yurib borib ustiga tushmoq",
        "explanation": "<p><em>На + идти́</em>. Siz qidirasiz, yurasiz — va bir joyda "
                       "ustiga chiqasiz. Shuning uchun u <em>идти́</em> kabi "
                       "turlanadi.</p>",
    },
    {
        "text": "<p><strong>войти́</strong> va <strong>зайти́</strong> — farqi "
                "nima?</p>",
        "choices": ["Kirmoq · kirib chiqmoq (qisqa vaqtga)",
                    "Kirib chiqmoq · kirmoq", "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Kirmoq · kirib chiqmoq (qisqa vaqtga)",
        "explanation": "<p><em>Войти́ в дом</em> — kirmoq. <em>Зайти́ в магази́н</em> "
                       "— yoʻl-yoʻlakay kirib oʻtmoq.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida bu maʼnolar qanday quriladi?</p>",
        "choices": ["Qoʻshma feʼllar bilan: kirib chiqmoq, oʻtib ketmoq",
                    "Prefikslar bilan",
                    "Faqat bitta feʼl bilan",
                    "Qurilmaydi"],
        "correct": "Qoʻshma feʼllar bilan: kirib chiqmoq, oʻtib ketmoq",
        "explanation": "<p>Ikkala tilda ham maʼno ikki qismdan quriladi. Farq: "
                       "oʻzbekchada ikkinchi qism orqada va alohida feʼl; ruschada "
                       "oldinda va soʻzning bir qismi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi bitta oʻzakdan?</p>",
        "choices": ["прийти́ · уйти́ · найти́ · пойти́",
                    "прийти́ · прие́хать · прилете́ть · принести́",
                    "идти́ · ходи́ть · е́хать · е́здить",
                    "найти́ · иска́ть · ви́деть · знать"],
        "correct": "прийти́ · уйти́ · найти́ · пойти́",
        "explanation": "<p>Hammasi <em>-йти</em> oʻzagidan va oʻtgan zamonda "
                       "<em>-шёл</em> beradi. Ikkinchi qatorda bitta prefiks, lekin "
                       "toʻrtta boshqa oʻzak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я пошёл!", "Он зашёл в магази́н.",
                    "Он найди́л ключи́.", "Все разошли́сь."],
        "correct": "Он найди́л ключи́.",
        "explanation": "<p>Toʻgʻrisi — <strong>Он нашёл ключи́</strong>. "
                       "<em>Найти́</em> <em>идти́</em> kabi turlanadi: "
                       "<em>нашёл, нашла́, нашли́</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я вошёл в магази́н на пять мину́т.",
                    "Я зашёл в магази́н на пять мину́т.",
                    "Я пришёл в магази́н на пять мину́т.",
                    "Я дошёл в магази́н на пять мину́т."],
        "correct": "Я зашёл в магази́н на пять мину́т.",
        "explanation": "<p>Qisqa tashrif — <strong>за-</strong>. «На пять мину́т» bu "
                       "maʼnoni tasdiqlaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты до́лго иска́л ключи́?</strong></p>",
        "choices": ["— Да, но наконе́ц нашёл.", "— Да, но наконе́ц находи́л.",
                    "— Да, но наконе́ц иска́л.", "— Да, но наконе́ц найти́."],
        "correct": "— Да, но наконе́ц нашёл.",
        "explanation": "<p>«Наконе́ц» — natija, demak СВ <strong>нашёл</strong>. "
                       "<em>Находи́л</em> takroriy boʻlardi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Uyga ketayotib "
                "doʻkonga kirib oʻtdim va non oldim.</strong></p>",
        "choices": ["По доро́ге домо́й я вошёл в магази́н и купи́л хлеб.",
                    "По доро́ге домо́й я зашёл в магази́н и купи́л хлеб.",
                    "По доро́ге домо́й я пришёл в магази́н и купи́л хлеб.",
                    "По доро́ге домо́й я прошёл в магази́н и купи́л хлеб."],
        "correct": "По доро́ге домо́й я зашёл в магази́н и купи́л хлеб.",
        "explanation": "<p>«Kirib oʻtdim» — yoʻl-yoʻlakay qisqa tashrif, demak "
                       "<strong>зашёл</strong>.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-56 Mashq: Harakat feʼllari 2: ехать/ездить, бежать/бегать, лететь/летать, нести/носить",
        "description": (
            "Sakkizta juftlik, bitta mantiq. Е́хал ↔ е́здил, носи́ть ning "
            "«kiymoq» maʼnosi va вожу́ ning ikki manbai."
        ),
        "tutorial": "PR-56:",
        "questions": Q_PR56,
    },
    {
        "title": "PR-57 Mashq: Harakat feʼllarining prefikslari: при-, у-, вы-, в-, до-, пере-, под-, от-",
        "description": (
            "Sakkizta prefiks va asosiy qoida: prefiks + идти́ = СВ, prefiks + "
            "ходи́ть = НСВ. Prefiks va predlogning juftlashuvi."
        ),
        "tutorial": "PR-57:",
        "questions": Q_PR57,
    },
    {
        "title": "PR-58 Mashq: Prefikslar maʼnoni qanday oʻzgartiradi: по-, за-, про-, раз-, с-, на-",
        "description": (
            "По- boshlanish, за- qisqa tashrif, про- oʻtib ketish, раз- tarqalish "
            "— va найти́ = на + идти́."
        ),
        "tutorial": "PR-58:",
        "questions": Q_PR58,
    },
]
