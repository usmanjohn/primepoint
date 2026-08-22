# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-62 … PR-64.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_62_64.py --master=prime \\
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
# PR-62 — -ся ning oltita maʼnosi
# =====================================================================

Q_PR62 = [
    # 1–5 tanish
    {
        "text": "<p><strong>-ся</strong> qachon <strong>-сь</strong> boʻlib "
                "yoziladi?</p>",
        "choices": ["Unlidan keyin", "Undoshdan keyin",
                    "Koʻplikda", "Oʻtgan zamonda"],
        "correct": "Unlidan keyin",
        "explanation": "<p><em>учу́<strong>сь</strong>, у́чите<strong>сь</strong>, "
                       "учи́ла<strong>сь</strong></em> — unlidan keyin. "
                       "<em>у́чит<strong>ся</strong>, у́чат<strong>ся</strong></em> — "
                       "undoshdan keyin.</p>",
    },
    {
        "text": "<p><strong>-ся</strong> feʼli hech qachon qaysi kelishikni "
                "olmaydi?</p>",
        "choices": ["Роди́тельный", "Да́тельный", "Вини́тельный", "Твори́тельный"],
        "correct": "Вини́тельный",
        "explanation": "<p>Bu darsning bitta qatʼiy qoidasi. Gapda «nimani?» degan "
                       "obyekt boʻlsa, <strong>-ся ni olib tashlang</strong>: "
                       "<em>он мо́ет маши́ну</em>.</p>",
    },
    {
        "text": "<p>Qaysi maʼno? <strong>Они́ встреча́ются ка́ждую суббо́ту.</strong></p>",
        "choices": ["Oʻziga qaytish", "Bir-biriga", "Majhul nisbat", "Shaxssiz holat"],
        "correct": "Bir-biriga",
        "explanation": "<p>Uchrashish uchun kamida ikki kishi kerak. Oʻzbekchada bu "
                       "<em>-ish-</em>: <strong>koʻrishmoq, uchrashmoq</strong>.</p>",
    },
    {
        "text": "<p>Qaysi feʼl <strong>-ся</strong> siz umuman ishlatilmaydi?</p>",
        "choices": ["мыть", "учи́ть", "смея́ться", "открыва́ть"],
        "correct": "смея́ться",
        "explanation": "<p><em>«Смеять»</em> degan soʻz rus tilida yoʻq. Shu guruhda "
                       "yana <em>боя́ться, наде́яться, улыба́ться, "
                       "стара́ться</em>.</p>",
    },
    {
        "text": "<p>Qaysi maʼno? <strong>Мне не спи́тся.</strong></p>",
        "choices": ["Shaxssiz holat", "Oʻziga qaytish", "Bir-biriga", "Majhul nisbat"],
        "correct": "Shaxssiz holat",
        "explanation": "<p>Gapda ega yoʻq, odam esa <strong>Да́тельный</strong> "
                       "kelishigida: <em>мне</em>. Shu oilada <em>хо́чется, "
                       "ка́жется</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я гото́влю___ к "
                "экза́мену.</strong></p>",
        "choices": ["-ся", "-сь", "-се", "hech narsa"],
        "correct": "-сь",
        "explanation": "<p><em>гото́влю</em> unli bilan tugaydi — demak "
                       "<strong>-сь</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Моя́ сестра́ ___ в "
                "университе́те.</strong></p>",
        "choices": ["у́чит", "у́чится", "учи́ть", "у́чатся"],
        "correct": "у́чится",
        "explanation": "<p><em>Учи́ть</em> — «oʻrgatmoq» yoki «yodlamoq», u obyekt "
                       "talab qiladi. «Universitetda oʻqimoq» — "
                       "<strong>учи́ться</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Библиоте́ка ___ в "
                "це́нтре го́рода.</strong></p>",
        "choices": ["нахо́дит", "нахо́дится", "найдёт", "найдена́"],
        "correct": "нахо́дится",
        "explanation": "<p><em>Находи́ть</em> — «topmoq», <em>находи́ться</em> — "
                       "«joylashmoq». Bu 6-guruh: -ся maʼnoni butunlay "
                       "oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я занима́юсь "
                "___.</strong> (спорт)</p>",
        "choices": ["спорт", "спо́рта", "спо́ртом", "спо́рту"],
        "correct": "спо́ртом",
        "explanation": "<p><em>Занима́ться</em> <strong>Твори́тельный</strong> "
                       "talab qiladi. Qoida buzilmayapti — bu Вини́тельный "
                       "emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он бои́тся "
                "___.</strong> (соба́ки)</p>",
        "choices": ["соба́ки", "соба́к", "соба́ками", "соба́кам"],
        "correct": "соба́к",
        "explanation": "<p><em>Боя́ться</em> <strong>Роди́тельный</strong> talab "
                       "qiladi, koʻplikda esa <em>соба́к</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ сы́на "
                "ка́ждое у́тро.</strong> (одева́ть / одева́ться)</p>",
        "choices": ["одева́ется", "одева́ет", "одева́ться", "оде́лся"],
        "correct": "одева́ет",
        "explanation": "<p><em>Сы́на</em> — obyekt, demak <strong>-ся yoʻq</strong>. "
                       "<em>Он одева́ется</em> «u kiyinyapti» boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Магази́н ___ в "
                "де́вять часо́в.</strong></p>",
        "choices": ["открыва́ет", "открыва́ется", "откры́л", "открыва́ть"],
        "correct": "открыва́ется",
        "explanation": "<p>Kim ochishi muhim emas — bu 3-maʼno, majhul nisbat. "
                       "Faqat НСВ va faqat uchinchi shaxsda.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он мо́ет маши́ну. · "
                "Он мо́ется.</strong></p>",
        "choices": ["Obyekt bor · obyekt yoʻq, harakat oʻziga qaytadi",
                    "Obyekt yoʻq · obyekt bor", "Ikkalasi bir xil",
                    "Ikkinchisi majhul nisbat"],
        "correct": "Obyekt bor · obyekt yoʻq, harakat oʻziga qaytadi",
        "explanation": "<p>Ikkinchi gapda obyekt — odamning oʻzi. Oʻzbekchada bu "
                       "<em>-in-</em>: <strong>yuvinmoq</strong>.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida <strong>-ся</strong> ning vazifalariga nechta "
                "qoʻshimcha toʻgʻri keladi?</p>",
        "choices": ["Bitta", "Uchta: -in-, -ish-, -il-", "Ikkita", "Hech qanaqasi"],
        "correct": "Uchta: -in-, -ish-, -il-",
        "explanation": "<p><em>yuv<b>in</b>moq</em> (oʻziga), <em>koʻr<b>ish</b>moq</em> "
                       "(bir-biriga), <em>qur<b>il</b>moq</em> (majhul). Oʻzbekcha "
                       "aniqroq, ruscha tejamkor.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он нашёл ключи́. · "
                "Ключи́ нахо́дятся в су́мке.</strong></p>",
        "choices": ["Topdi · turibdi (joylashuv)", "Turibdi · topdi",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Topdi · turibdi (joylashuv)",
        "explanation": "<p>6-maʼno: -ся qoʻshilgach feʼl butunlay boshqa maʼno "
                       "oldi.</p>",
    },
    {
        "text": "<p>Majhul nisbat maʼnosidagi <strong>-ся</strong> qaysi feʼllardan "
                "yasaladi?</p>",
        "choices": ["Faqat НСВ feʼllardan", "Faqat СВ feʼllardan",
                    "Ikkalasidan ham", "Faqat harakat feʼllaridan"],
        "correct": "Faqat НСВ feʼllardan",
        "explanation": "<p><em>Стро́ится, открыва́ется, чита́ется</em> — hammasi НСВ. "
                       "СВ da bu maʼno qisqa sifatdosh bilan beriladi: "
                       "<em>постро́ен</em> (PR-61).</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Он мо́ется.", "Он одева́ется сы́на.",
                    "Он у́чится в шко́ле.", "Он бои́тся соба́к."],
        "correct": "Он одева́ется сы́на.",
        "explanation": "<p><em>Сы́на</em> — Вини́тельный, lekin -ся feʼli obyekt "
                       "olmaydi. Toʻgʻrisi: <strong>Он одева́ет сы́на</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я учу́ся в шко́ле.", "Я учу́сь в шко́ле.",
                    "Я учу́сь матема́тику.", "Я учи́сь в шко́ле."],
        "correct": "Я учу́сь в шко́ле.",
        "explanation": "<p>Unlidan keyin <strong>-сь</strong>, va -ся feʼli obyekt "
                       "olmaydi — shuning uchun <em>«учу́сь матема́тику»</em> ham "
                       "xato.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Чем ты занима́ешься?</strong></p>",
        "choices": ["— Я занима́юсь му́зыкой.", "— Я занима́юсь му́зыку.",
                    "— Я занима́ю му́зыкой.", "— Я занима́юсь му́зыки."],
        "correct": "— Я занима́юсь му́зыкой.",
        "explanation": "<p>Savolning oʻzi kelishikni aytib turibdi: <em>чем?</em> — "
                       "<strong>Твори́тельный</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ular har hafta "
                "uchrashadi va hech qachon urushmaydi.</strong></p>",
        "choices": ["Они́ встреча́ются ка́ждую неде́лю и никогда́ не ссо́рятся.",
                    "Они́ встреча́ют ка́ждую неде́лю и никогда́ не ссо́рят.",
                    "Они́ встреча́ются ка́ждую неде́лю и никогда́ не ссо́рят.",
                    "Они́ встреча́ют ка́ждую неде́лю и никогда́ не ссо́рятся."],
        "correct": "Они́ встреча́ются ка́ждую неде́лю и никогда́ не ссо́рятся.",
        "explanation": "<p>Ikkala feʼl ham 2-maʼnoda — bir-biriga. Oʻzbekchada "
                       "ikkalasi ham <em>-ish-</em> bilan: "
                       "<strong>uchrashmoq, urushmoq</strong>.</p>",
    },
]


# =====================================================================
# PR-63 — который
# =====================================================================

Q_PR63 = [
    # 1–5 tanish
    {
        "text": "<p><strong>Который</strong> ning jinsi va soni qayerdan "
                "olinadi?</p>",
        "choices": ["Ergash gapdagi feʼldan", "Aniqlanayotgan otdan",
                    "Gapning egasidan", "Kelishikdan"],
        "correct": "Aniqlanayotgan otdan",
        "explanation": "<p><em>кни́га, кото́р<b>ая</b></em> · <em>челове́к, "
                       "кото́р<b>ый</b></em> · <em>лю́ди, кото́р<b>ые</b></em>.</p>",
    },
    {
        "text": "<p><strong>Который</strong> ning kelishigi qayerdan olinadi?</p>",
        "choices": ["Aniqlanayotgan otdan", "Uning oʻz gapidagi vazifasidan",
                    "Bosh gapdan", "Har doim Имени́тельный boʻladi"],
        "correct": "Uning oʻz gapidagi vazifasidan",
        "explanation": "<p>Bu darsning yuragi. <em>Кни́га, кото́р<b>ую</b> я "
                       "чита́ю</em> — «я чита́ю кни́г<b>у</b>», demak "
                       "Вини́тельный.</p>",
    },
    {
        "text": "<p>Rus tilida predlog <strong>кото́рый</strong> ga nisbatan "
                "qayerda turadi?</p>",
        "choices": ["Undan oldin", "Ergash gap oxirida",
                    "Bosh gap oxirida", "Predlog ishlatilmaydi"],
        "correct": "Undan oldin",
        "explanation": "<p><em>дом, <b>в</b> кото́ром мы жи́ли</em>. Predlog hech "
                       "qachon ergash gap oxirida qolmaydi.</p>",
    },
    {
        "text": "<p><strong>Который</strong> dan oldin vergul qoʻyiladimi?</p>",
        "choices": ["Har doim", "Hech qachon",
                    "Faqat gap oxirida boʻlsa", "Faqat odam haqida boʻlsa"],
        "correct": "Har doim",
        "explanation": "<p>Istisnosiz. Agar ergash gap oʻrtada boʻlsa, ikki "
                       "tomondan ajratiladi: <em>Кни́га, кото́рую я чита́ю, "
                       "интере́сная.</em></p>",
    },
    {
        "text": "<p>Odam va narsa uchun <strong>кото́рый</strong> boshqacha "
                "boʻladimi?</p>",
        "choices": ["Ha, odamga boshqa soʻz ishlatiladi",
                    "Yoʻq, ikkalasi uchun bir xil",
                    "Ha, narsaga vergul qoʻyilmaydi",
                    "Ha, odamga faqat koʻplik shakli"],
        "correct": "Yoʻq, ikkalasi uchun bir xil",
        "explanation": "<p><em>челове́к, кото́рый рабо́тает</em> va <em>маши́на, "
                       "кото́рая рабо́тает</em> — oʻzbekcha <em>-gan</em> "
                       "kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то кни́га, ___ я "
                "купи́л вчера́.</strong></p>",
        "choices": ["кото́рый", "кото́рая", "кото́рую", "кото́рой"],
        "correct": "кото́рую",
        "explanation": "<p>«Я купи́л <strong>кни́гу</strong>» — Вини́тельный, ayol "
                       "jinsi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то дом, ___ живёт "
                "моя́ ба́бушка.</strong></p>",
        "choices": ["кото́рый", "в кото́ром", "кото́рого", "кото́рому"],
        "correct": "в кото́ром",
        "explanation": "<p>«Ба́бушка живёт <strong>в до́ме</strong>» — Предло́жный, "
                       "va predlog кото́рый bilan birga keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то друг, ___ я "
                "давно́ не ви́дел.</strong></p>",
        "choices": ["кото́рый", "кото́рого", "кото́рому", "кото́рым"],
        "correct": "кото́рого",
        "explanation": "<p>«Я не ви́дел <strong>дру́га</strong>» — jonli otda "
                       "Вини́тельный Роди́тельный bilan bir xil (PR-33).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то учи́тель, ___ я "
                "написа́л письмо́.</strong></p>",
        "choices": ["кото́рый", "кото́рого", "кото́рому", "кото́рым"],
        "correct": "кото́рому",
        "explanation": "<p>«Я написа́л письмо́ <strong>учи́телю</strong>» — «kimga?», "
                       "Да́тельный.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то сосе́д, ___ есть "
                "маши́на.</strong></p>",
        "choices": ["у кото́рого", "кото́рый", "с кото́рым", "кото́рому"],
        "correct": "у кото́рого",
        "explanation": "<p>«<strong>У сосе́да</strong> есть маши́на» — «у» + "
                       "Роди́тельный (PR-14).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то лю́ди, ___ "
                "рабо́тают здесь давно́.</strong></p>",
        "choices": ["кото́рый", "кото́рые", "кото́рых", "кото́рым"],
        "correct": "кото́рые",
        "explanation": "<p>Koʻplik va ergash gapda ega — demak "
                       "<strong>кото́рые</strong>, Имени́тельный.</p>",
    },
    {
        "text": "<p>Bu ikki gapni bittaga birlashtiring.</p><p><strong>Я зна́ю "
                "э́того челове́ка. Он рабо́тает в шко́ле.</strong></p>",
        "choices": ["Я зна́ю челове́ка, кото́рый рабо́тает в шко́ле.",
                    "Я зна́ю челове́ка, кото́рого рабо́тает в шко́ле.",
                    "Кото́рый рабо́тает в шко́ле, я зна́ю челове́ка.",
                    "Я зна́ю челове́ка кото́рый рабо́тает в шко́ле."],
        "correct": "Я зна́ю челове́ка, кото́рый рабо́тает в шко́ле.",
        "explanation": "<p>Ikkinchi gapda <em>он</em> ega edi — demak "
                       "<strong>кото́рый</strong>, Имени́тельный. Va vergul "
                       "majburiy.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Oʻzbekcha aniqlovchi gap otga nisbatan qayerda turadi?</p>",
        "choices": ["Otdan oldin: «men oʻqiyotgan kitob»",
                    "Otdan keyin, ruschadagi kabi",
                    "Gap oxirida", "Farqi yoʻq"],
        "correct": "Otdan oldin: «men oʻqiyotgan kitob»",
        "explanation": "<p>Ruschada esa teskari: <em>кни́га, кото́рую я чита́ю</em>. "
                       "Shuning uchun tarjima qilganda gapni "
                       "<strong>agʻdarish</strong> kerak.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>стол, кото́рый я "
                "купи́л · друг, кото́рого я встре́тил</strong></p>",
        "choices": ["Jonsiz ot · jonli ot — tushum kelishigi boshqacha",
                    "Birinchisi koʻplik", "Ikkinchisida xato bor",
                    "Farqi faqat jinsda"],
        "correct": "Jonsiz ot · jonli ot — tushum kelishigi boshqacha",
        "explanation": "<p>Jonli otlarda Вини́тельный Роди́тельный bilan bir xil "
                       "(PR-33), shuning uchun <em>кото́рого</em>.</p>",
    },
    {
        "text": "<p><strong>Который</strong> qanday tuslanadi?</p>",
        "choices": ["Sifat kabi — «но́вый» singari", "Ot kabi",
                    "Tuslanmaydi", "Olmosh «он» kabi"],
        "correct": "Sifat kabi — «но́вый» singari",
        "explanation": "<p>Shuning uchun uni alohida yodlash shart emas: "
                       "<em>кото́рого, кото́рому, кото́рым, о кото́ром</em> — "
                       "hammasi tanish qoʻshimchalar (PR-42).</p>",
    },
    {
        "text": "<p><strong>Vergul qayerga qoʻyiladi?</strong></p>"
                "<p>дом ___ в кото́ром мы жи́ли</p>",
        "choices": ["Predlogdan oldin: дом, в кото́ром…",
                    "Кото́рый dan oldin: дом в, кото́ром…",
                    "Vergul kerak emas", "Gap oxirida"],
        "correct": "Predlogdan oldin: дом, в кото́ром…",
        "explanation": "<p>Vergul butun ergash gapni ajratadi, predlog esa "
                       "ergash gapning bir qismi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Кни́га, кото́рую я чита́ю, интере́сная.",
                    "Дом, кото́рый мы жи́ли, ста́рый.",
                    "Друг, кото́рому я написа́л, отве́тил.",
                    "Лю́ди, кото́рые ждут, устали́."],
        "correct": "Дом, кото́рый мы жи́ли, ста́рый.",
        "explanation": "<p>Toʻgʻrisi — <strong>в кото́ром</strong>: «мы жи́ли в "
                       "до́ме», Предло́жный predlog bilan.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Кото́рую я чита́ю кни́га интере́сная.",
                    "Кни́га кото́рую я чита́ю интере́сная.",
                    "Кни́га, кото́рую я чита́ю, интере́сная.",
                    "Кни́га, кото́рый я чита́ю, интере́сная."],
        "correct": "Кни́га, кото́рую я чита́ю, интере́сная.",
        "explanation": "<p>Avval ot, keyin vergul, keyin кото́рый — va u ayol "
                       "jinsida, Вини́тельный'da.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Кака́я э́то у́лица?</strong></p>",
        "choices": ["— Э́то у́лица, на кото́рой я вы́рос.",
                    "— Э́то у́лица, кото́рой я вы́рос.",
                    "— Э́то у́лица, кото́рую я вы́рос.",
                    "— Э́то у́лица, на кото́рый я вы́рос."],
        "correct": "— Э́то у́лица, на кото́рой я вы́рос.",
        "explanation": "<p>«Я вы́рос <strong>на у́лице</strong>» — Предло́жный, "
                       "predlog <em>на</em> bilan, ayol jinsida.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Men aytgan "
                "oʻqituvchi bugun kelmadi.</strong></p>",
        "choices": ["Учи́тель, о кото́ром я говори́л, сего́дня не пришёл.",
                    "Учи́тель, кото́рого я говори́л, сего́дня не пришёл.",
                    "Кото́рого я говори́л учи́тель сего́дня не пришёл.",
                    "Учи́тель, кото́рый я говори́л, сего́дня не пришёл."],
        "correct": "Учи́тель, о кото́ром я говори́л, сего́дня не пришёл.",
        "explanation": "<p>«Я говори́л <strong>об учи́теле</strong>» — Предло́жный "
                       "<em>о</em> predlogi bilan. Va oʻzbekchada aniqlovchi "
                       "oldinda, ruschada keyinda.</p>",
    },
]


# =====================================================================
# PR-64 — что / чтобы
# =====================================================================

Q_PR64 = [
    # 1–5 tanish
    {
        "text": "<p><strong>Что</strong> va <strong>что́бы</strong> — asosiy farqi "
                "nima?</p>",
        "choices": ["Fakt · istak yoki maqsad", "Istak · fakt",
                    "Ikkalasi bir xil", "Birinchisi faqat savolda"],
        "correct": "Fakt · istak yoki maqsad",
        "explanation": "<p><em>Я зна́ю, <b>что</b> он придёт</em> — axborot. "
                       "<em>Я хочу́, <b>что́бы</b> он пришёл</em> — istak.</p>",
    },
    {
        "text": "<p><strong>Что́бы</strong> dan keyin (ega boshqa boʻlsa) qanday "
                "shakl keladi?</p>",
        "choices": ["Hozirgi zamon", "Oʻtgan zamon", "Kelasi zamon", "Buyruq shakli"],
        "correct": "Oʻtgan zamon",
        "explanation": "<p><em>Я хочу́, что́бы ты <b>пришёл</b></em>. Bu oʻtmish "
                       "emas — <em>что́бы</em> = <em>что</em> + <em>бы</em>, va "
                       "<em>бы</em> har doim oʻtgan zamon talab qiladi "
                       "(PR-60).</p>",
    },
    {
        "text": "<p>Ikkala qismda ham ega bir xil boʻlsa, <strong>что́бы</strong> "
                "dan keyin nima keladi?</p>",
        "choices": ["Oʻtgan zamon", "Infinitiv", "Buyruq shakli", "Hozirgi zamon"],
        "correct": "Infinitiv",
        "explanation": "<p><em>Я пришёл, что́бы <b>поговори́ть</b></em> — oʻzbekcha "
                       "«gaplashish uchun».</p>",
    },
    {
        "text": "<p>Qaysi feʼl <strong>что́бы</strong> talab qiladi?</p>",
        "choices": ["знать", "ду́мать", "проси́ть", "ви́деть"],
        "correct": "проси́ть",
        "explanation": "<p>Soʻrash — istak. Shu guruhda <em>хоте́ть, тре́бовать, "
                       "сове́товать, ну́жно</em>. Bilish va oʻylash esa "
                       "<em>что</em> oladi.</p>",
    },
    {
        "text": "<p>Ikkalasidan oldin vergul qoʻyiladimi?</p>",
        "choices": ["Ha, ikkalasidan ham", "Faqat что dan oldin",
                    "Faqat что́бы dan oldin", "Yoʻq"],
        "correct": "Ha, ikkalasidan ham",
        "explanation": "<p><em>Я зна́ю<b>,</b> что…</em> · <em>Я хочу́<b>,</b> "
                       "что́бы…</em></p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю, ___ э́то "
                "хоро́шая иде́я.</strong></p>",
        "choices": ["что", "что́бы", "е́сли", "кото́рый"],
        "correct": "что",
        "explanation": "<p><em>Ду́мать</em> — fikr bildirish, yaʼni fakt. Istak "
                       "emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я хочу́, что́бы ты ___ "
                "мне.</strong> (помо́чь)</p>",
        "choices": ["помо́жешь", "помо́г", "помога́ешь", "помо́чь"],
        "correct": "помо́г",
        "explanation": "<p>Ega boshqa (<em>я</em> ↔ <em>ты</em>), demak oʻtgan "
                       "zamon. Bu oʻtmish haqida emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он прие́хал в Москву́, "
                "что́бы ___.</strong> (учи́ться)</p>",
        "choices": ["учи́лся", "учи́ться", "у́чится", "учи́сь"],
        "correct": "учи́ться",
        "explanation": "<p>Ikkala qismda ham ega <em>он</em> — demak "
                       "<strong>infinitiv</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма проси́ла, ___ мы "
                "помы́ли посу́ду.</strong></p>",
        "choices": ["что", "что́бы", "е́сли", "как"],
        "correct": "что́бы",
        "explanation": "<p><em>Проси́ть</em> — iltimos, demak <strong>что́бы</strong> "
                       "va oʻtgan zamon.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я слы́шал, ___ он "
                "уже́ прие́хал.</strong></p>",
        "choices": ["что", "что́бы", "что́бы не", "кото́рый"],
        "correct": "что",
        "explanation": "<p>Eshitish — axborot olish. Bu allaqachon sodir boʻlgan "
                       "fakt.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ вы́учить язы́к, "
                "ну́жно говори́ть ка́ждый день.</strong></p>",
        "choices": ["Что", "Что́бы", "Е́сли бы", "Кото́рый"],
        "correct": "Что́бы",
        "explanation": "<p>Maqsad, va ega koʻrsatilmagan — demak "
                       "<strong>что́бы</strong> + infinitiv. Gap boshida turgani "
                       "uchun vergul oʻrtada.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он сли́шком уста́л, "
                "что́бы ___ в кино́.</strong> (идти́)</p>",
        "choices": ["шёл", "идти́", "идёт", "иди́"],
        "correct": "идти́",
        "explanation": "<p><em>Сли́шком … что́бы</em> qurilishida infinitiv keladi: "
                       "«kinoga borish uchun juda charchagan».</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я сказа́л, что он "
                "пришёл. · Я сказа́л, что́бы он пришёл.</strong></p>",
        "choices": ["Xabar · iltimos yoki buyruq", "Iltimos · xabar",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Xabar · iltimos yoki buyruq",
        "explanation": "<p><em>Сказа́ть</em> ikkala bogʻlovchini ham oladi, va maʼno "
                       "butunlay oʻzgaradi: «u kelganini aytdim» ↔ «kelsin "
                       "dedim».</p>",
    },
    {
        "text": "<p><strong>Что́бы</strong> dan keyingi oʻtgan zamon nimani "
                "bildiradi?</p>",
        "choices": ["Oʻtmishni", "Hech qanday zamonni — bu shunchaki shakl",
                    "Kelasi zamonni", "Takrorlanuvchi harakatni"],
        "correct": "Hech qanday zamonni — bu shunchaki shakl",
        "explanation": "<p><em>Я хочу́, что́бы ты пришёл <b>за́втра</b></em> — "
                       "ertaga haqida. <em>Бы</em> shunchaki oʻtgan zamon "
                       "shaklini talab qiladi.</p>",
    },
    {
        "text": "<p>Rus tilida inkor «Menimcha, u kelmaydi» gapida qayerga "
                "qoʻyiladi?</p>",
        "choices": ["Birinchi feʼlga: Не ду́маю, что он придёт",
                    "Ikkinchi feʼlga: Ду́маю, что он не придёт",
                    "Ikkalasiga ham", "Inkor ishlatilmaydi"],
        "correct": "Birinchi feʼlga: Не ду́маю, что он придёт",
        "explanation": "<p>Oʻzbekchada «yoʻq» ikkinchi feʼlda (<em>kelmaydi</em>), "
                       "ruschada esa birinchisiga koʻchadi. Tarjimada buni "
                       "esdan chiqarmang.</p>",
    },
    {
        "text": "<p>Oʻzbekcha «kelishini» shakli nima uchun chalgʻitadi?</p>",
        "choices": ["U ham fakt, ham istak gapida ishlatiladi",
                    "U faqat istakda ishlatiladi",
                    "U faqat faktda ishlatiladi",
                    "U ruschaga oʻgirilmaydi"],
        "correct": "U ham fakt, ham istak gapida ishlatiladi",
        "explanation": "<p><em>Kelishini bilaman</em> → <b>что</b>, <em>kelishini "
                       "xohlayman</em> → <b>что́бы</b>. Shuning uchun feʼlga "
                       "qarang, qoʻshimchaga emas.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я зна́ю, что он рабо́тает здесь.",
                    "Я хочу́, что́бы ты придёшь.",
                    "Я пришёл, что́бы поговори́ть.",
                    "Ма́ма проси́ла, что́бы мы помы́ли посу́ду."],
        "correct": "Я хочу́, что́бы ты придёшь.",
        "explanation": "<p>Toʻgʻrisi — <strong>что́бы ты пришёл</strong>. Что́бы dan "
                       "keyin oʻtgan zamon.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я пришёл, что́бы я поговори́л.",
                    "Я пришёл, что́бы поговори́ть.",
                    "Я пришёл, что поговори́ть.",
                    "Я пришёл, что́бы поговорю́."],
        "correct": "Я пришёл, что́бы поговори́ть.",
        "explanation": "<p>Ikkala qismda ham ega <em>я</em> — demak infinitiv, "
                       "takroriy <em>я</em> siz.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Заче́м ты встал так ра́но?</strong></p>",
        "choices": ["— Что́бы не опозда́ть.", "— Что́бы я не опозда́л.",
                    "— Что я не опозда́л.", "— Что́бы не опозда́ю."],
        "correct": "— Что́бы не опозда́ть.",
        "explanation": "<p>Ega bitta (<em>я</em>), demak infinitiv. Va <em>заче́м?</em> "
                       "savoli maqsad soʻrayapti — <em>что́бы</em>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Oyim uyga erta "
                "qaytishimni xohlaydi.</strong></p>",
        "choices": ["Ма́ма хо́чет, что я верну́сь домо́й ра́но.",
                    "Ма́ма хо́чет, что́бы я верну́лся домо́й ра́но.",
                    "Ма́ма хо́чет, что́бы я верну́сь домо́й ра́но.",
                    "Ма́ма хо́чет верну́ться домо́й ра́но."],
        "correct": "Ма́ма хо́чет, что́бы я верну́лся домо́й ра́но.",
        "explanation": "<p>Ega boshqa (<em>ма́ма</em> ↔ <em>я</em>), demak "
                       "<strong>что́бы</strong> + oʻtgan zamon. Oxirgi variant "
                       "«oyimning oʻzi qaytmoqchi» degan boshqa maʼno "
                       "berardi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-62 Mashq: -ся feʼlining oltita maʼnosi",
        "description": (
            "-ся / -сь imlosi, oltita maʼno, «obyekt olmaydi» qoidasi va "
            "-ся feʼllari talab qiladigan kelishiklar."
        ),
        "tutorial": "PR-62:",
        "questions": Q_PR62,
    },
    {
        "title": "PR-63 Mashq: Который — rus tilining «-gan» sifatdosh gapi",
        "description": (
            "Jins va son otdan, kelishik esa oʻz gapidagi vazifadan. Predlog "
            "кото́рый dan oldin, vergul majburiy."
        ),
        "tutorial": "PR-63:",
        "questions": Q_PR63,
    },
    {
        "title": "PR-64 Mashq: Что va чтобы — fakt va maqsad",
        "description": (
            "Что — fakt, что́бы — istak yoki maqsad. Ega boshqa boʻlsa oʻtgan "
            "zamon, bir xil boʻlsa infinitiv."
        ),
        "tutorial": "PR-64:",
        "questions": Q_PR64,
    },
]
