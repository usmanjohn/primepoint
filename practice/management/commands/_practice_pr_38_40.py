# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-38 … PR-40.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_38_40.py --master=prime \\
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
# PR-38 — Дательный 2: holat, yosh, К, ПО
# =====================================================================

Q_PR38 = [
    # 1–5 tanish
    {
        "text": "<p>«Menga sovuq» ruschada qanday boʻladi?</p>",
        "choices": ["Я хо́лодно.", "Мне хо́лодно.", "Меня́ хо́лодно.", "Я хо́лодный."],
        "correct": "Мне хо́лодно.",
        "explanation": "<p>Shaxssiz gap: ega yoʻq, olmosh Да́тельный'da. Oʻzbekcha "
                       "«men<strong>ga</strong> sovuq» ning aynan oʻzi.</p>",
    },
    {
        "text": "<p>Rus tilida yosh qaysi kelishik bilan aytiladi?</p>",
        "choices": ["Bosh kelishik", "Роди́тельный", "Да́тельный", "Твори́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>Мне два́дцать лет</em> — soʻzma-soʻz «menga yigirma "
                       "yil». Oʻzbekchada esa ega bor: «men yigirma yoshdaman». "
                       "Ikkalasi ham gʻalati, lekin boshqacha.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___ врачу́.</strong></p>",
        "choices": ["в", "на", "к", "по"],
        "correct": "к",
        "explanation": "<p><strong>К</strong> + Да́тельный = odam tomon. Uning jufti "
                       "<em>от</em> (PR-35): <em>к врачу́ → от врача́</em>.</p>",
    },
    {
        "text": "<p><strong>ПО</strong> predlogi qaysi kelishikni oladi?</p>",
        "choices": ["Предло́жный", "Да́тельный", "Вини́тельный", "Роди́тельный"],
        "correct": "Да́тельный",
        "explanation": "<p><em>По у́лице, по го́роду, по телефо́ну</em> — hammasi "
                       "Да́тельный. Maʼnosi: «boʻylab» yoki «orqali».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ де́сять лет.</strong> "
                "(Бекзо́д)</p>",
        "choices": ["Бекзо́д", "Бекзо́да", "Бекзо́ду", "Бекзо́дом"],
        "correct": "Бекзо́ду",
        "explanation": "<p>Yosh Да́тельный bilan aytiladi — otlarda ham. Erkak jins "
                       "<strong>-у</strong> oladi: «Bekzod<strong>ga</strong> oʻn "
                       "yil».</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Мне "
                "хо́лодно.</strong></p>",
        "choices": ["Мне был хо́лодно.", "Мне была́ хо́лодно.",
                    "Мне бы́ло хо́лодно.", "Я был хо́лодно."],
        "correct": "Мне бы́ло хо́лодно.",
        "explanation": "<p>Shaxssiz gapda <em>быть</em> har doim oʻrta jinsda — "
                       "<strong>бы́ло</strong>, gapirayotgan odamning jinsidan qatʼi "
                       "nazar. Bu PR-27 dagi qoidaning oʻsha oʻzi.</p>",
    },
    {
        "text": "<p><strong>в</strong> yoki <strong>к</strong>?</p><p><strong>Я иду́ "
                "___ шко́лу.</strong></p>",
        "choices": ["в", "к", "на", "по"],
        "correct": "в",
        "explanation": "<p>Maktab — <strong>joy</strong>, demak <em>в</em> + "
                       "Вини́тельный (PR-33). <em>К</em> faqat odam yoki narsa "
                       "<strong>tomon</strong> ishlatiladi.</p>",
    },
    {
        "text": "<p><strong>в</strong> yoki <strong>к</strong>?</p><p><strong>Я иду́ "
                "___ бра́ту.</strong></p>",
        "choices": ["в", "на", "к", "по"],
        "correct": "к",
        "explanation": "<p>Aka — <strong>odam</strong>, demak <em>к</em> + "
                       "Да́тельный. Oʻzbekcha ikkala gapda ham <em>-ga</em>, lekin "
                       "ruschada tanlov bor: joy → В/НА, odam → К.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы гуля́ем по "
                "___.</strong> (го́род)</p>",
        "choices": ["го́род", "го́рода", "го́роду", "го́роде"],
        "correct": "го́роду",
        "explanation": "<p><em>ПО</em> Да́тельный oladi, erkak jins esa "
                       "<strong>-у</strong>: <em>по го́роду</em> — «shahar "
                       "boʻylab».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я говорю́ по "
                "___.</strong> (телефо́н)</p>",
        "choices": ["телефо́н", "телефо́на", "телефо́ну", "телефо́не"],
        "correct": "телефо́ну",
        "explanation": "<p><strong>По телефо́ну</strong> — «telefonda, telefon "
                       "orqali». Bu <em>по</em> ning ikkinchi maʼnosi: vosita "
                       "orqali.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Иди́ ___.</strong> "
                "(«mening oldimga» maʼnosida)</p>",
        "choices": ["к мне", "ко мне", "к меня́", "ко меня́"],
        "correct": "ко мне",
        "explanation": "<p><strong>Ко мне</strong> — predlogga unli qoʻshiladi, xuddi "
                       "<em>обо мне</em> (PR-31) va <em>со мной</em> (PR-39) "
                       "kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ гру́стно.</strong> "
                "(она́)</p>",
        "choices": ["Она́", "Её", "Ей", "Ею"],
        "correct": "Ей",
        "explanation": "<p><strong>Ей</strong> — Да́тельный. Shaxssiz gapda ega "
                       "boʻlmaydi, shuning uchun <em>она́</em> ishlatilmaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Oʻzbekcha <strong>-GA</strong> ruschada qanday boʻlinadi?</p>",
        "choices": ["Har doim К + Да́тельный",
                    "Joy → в/на + Вини́тельный · odam → к + Да́тельный",
                    "Har doim в + Вини́тельный",
                    "Boʻlinmaydi"],
        "correct": "Joy → в/на + Вини́тельный · odam → к + Да́тельный",
        "explanation": "<p><em>maktab<strong>ga</strong></em> → <em>в шко́лу</em>; "
                       "<em>aka<strong>mga</strong></em> → <em>к бра́ту</em>. Bu "
                       "darsning eng muhim farqi.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я иду́ в шко́лу. · Я "
                "иду́ к шко́ле.</strong></p>",
        "choices": ["Maktabga (ichiga) · maktab tomon (yoniga)",
                    "Ikkalasi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Maktabga (ichiga) · maktab tomon (yoniga)",
        "explanation": "<p>Ikkalasi ham mumkin, lekin maʼnosi boshqa. <em>В шко́лу</em> "
                       "— binoning ichiga kiraman. <em>К шко́ле</em> — binoning "
                       "yoniga boraman, ichkariga emas.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi Да́тельный?</p>",
        "choices": ["к бра́ту · по у́лице · мне хо́лодно",
                    "к бра́ту · в шко́лу · мне хо́лодно",
                    "от бра́та · по у́лице · мне хо́лодно",
                    "к бра́ту · по у́лице · я хо́лодно"],
        "correct": "к бра́ту · по у́лице · мне хо́лодно",
        "explanation": "<p><em>К</em> va <em>по</em> Да́тельный oladi, shaxssiz "
                       "gapdagi olmosh ham. <em>В шко́лу</em> — Вини́тельный, "
                       "<em>от бра́та</em> — Роди́тельный.</p>",
    },
    {
        "text": "<p>Nega <strong>ко мне</strong>, <strong>обо мне</strong>, "
                "<strong>со мной</strong> — hammasida qoʻshimcha unli bor?</p>",
        "choices": ["Talaffuzni yengillashtirish uchun",
                    "Chunki bular istisno soʻzlar",
                    "Chunki bular koʻplik",
                    "Bu grammatik xato"],
        "correct": "Talaffuzni yengillashtirish uchun",
        "explanation": "<p><em>Мне</em> va <em>мной</em> dan oldin predlogga unli "
                       "qoʻshiladi: <em>к → ко</em>, <em>о → обо</em>, <em>с → со</em>. "
                       "Uchtasini birga yodlang.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ей ску́чно.", "Мне два́дцать три го́да.",
                    "Я иду́ в бра́та.", "Мы говори́м по телефо́ну."],
        "correct": "Я иду́ в бра́та.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я иду́ к бра́ту</strong>. Manzil odam "
                       "boʻlsa, <em>к</em> + Да́тельный ishlatiladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я два́дцать лет.", "Мне два́дцать лет.",
                    "Меня́ два́дцать лет.", "Мной два́дцать лет."],
        "correct": "Мне два́дцать лет.",
        "explanation": "<p>Yosh Да́тельный bilan aytiladi va gapda ega boʻlmaydi. "
                       "<em>«Я два́дцать лет»</em> — oʻzbekcha tuzilishni ruschaga "
                       "koʻchirishdan kelib chiqadigan xato.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ско́лько тебе́ лет?</strong></p>",
        "choices": ["— Мне два́дцать оди́н год.", "— Я два́дцать оди́н год.",
                    "— Меня́ два́дцать оди́н год.", "— Мне два́дцать оди́н лет."],
        "correct": "— Мне два́дцать оди́н год.",
        "explanation": "<p>Ikkita qoida birga: yosh Да́тельный bilan "
                       "(<strong>мне</strong>), va oxirgi raqam 1 boʻlgani uchun bosh "
                       "kelishik birlik (<strong>год</strong>, PR-36).</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Kecha menga sovuq edi, "
                "bugun esa akamning oldiga boraman.</strong></p>",
        "choices": ["Вчера́ я был хо́лодно, а сего́дня иду́ в бра́та.",
                    "Вчера́ мне бы́ло хо́лодно, а сего́дня иду́ к бра́ту.",
                    "Вчера́ мне был хо́лодно, а сего́дня иду́ к бра́ту.",
                    "Вчера́ мне бы́ло хо́лодно, а сего́дня иду́ в бра́та."],
        "correct": "Вчера́ мне бы́ло хо́лодно, а сего́дня иду́ к бра́ту.",
        "explanation": "<p>Ikkita qoida: shaxssiz gapda <strong>бы́ло</strong> (oʻrta "
                       "jins), va odam manzil boʻlgani uchun <strong>к бра́ту</strong> "
                       "(Да́тельный).</p>",
    },
]


# =====================================================================
# PR-39 — Творительный 1: asbob va hamroh
# =====================================================================

Q_PR39 = [
    # 1–5 tanish
    {
        "text": "<p>Твори́тельный padeji oʻzbekchadagi qaysi soʻzga toʻgʻri "
                "keladi?</p>",
        "choices": ["uchun", "bilan", "haqida", "keyin"],
        "correct": "bilan",
        "explanation": "<p><em>pichoq <strong>bilan</strong></em> → <em>ножо́м</em>, "
                       "<em>akam <strong>bilan</strong></em> → <em>с бра́том</em>. "
                       "Maʼno tanish — qiyinchilik faqat shundaki, ruscha «bilan» ni "
                       "ikkiga boʻladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я пишу́ ___.</strong> "
                "(ру́чка)</p>",
        "choices": ["ру́чка", "ру́чку", "ру́чкой", "с ру́чкой"],
        "correct": "ру́чкой",
        "explanation": "<p>Ruchka — <strong>asbob</strong>, demak predlogsiz. "
                       "<em>«С ру́чкой»</em> ruscha quloqqa «ruchka bilan birga "
                       "yozyapman, ikkalamiz» boʻlib eshitiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___.</strong> "
                "(брат)</p>",
        "choices": ["бра́том", "с бра́том", "бра́та", "к бра́ту"],
        "correct": "с бра́том",
        "explanation": "<p>Aka — <strong>hamroh</strong>, u ham ketyapti, demak "
                       "<strong>с</strong> kerak. Bu asbobdan farqi.</p>",
    },
    {
        "text": "<p>Erkak jinsidagi ot Твори́тельный'da qanday tugaydi?</p>",
        "choices": ["-ой / -ей", "-ом / -ем", "-у / -ю", "-а / -я"],
        "correct": "-ом / -ем",
        "explanation": "<p><em>стол → столо́м</em>, <em>учи́тель → учи́телем</em>. "
                       "Oʻrta jins ham xuddi shunday. Ayol jinsi esa <strong>-ой / "
                       "-ей</strong> oladi.</p>",
    },
    {
        "text": "<p>«Men bilan» ruschada qanday boʻladi?</p>",
        "choices": ["с я", "с мной", "со мной", "со мне"],
        "correct": "со мной",
        "explanation": "<p><strong>Со мной</strong> — ikkita narsa: olmoshning "
                       "alohida shakli (<em>мной</em>) va predlogga qoʻshilgan unli "
                       "(<em>со</em>), xuddi <em>обо мне</em> va <em>ко мне</em> "
                       "kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p><strong>с</strong> kerakmi?</p><p><strong>Я ре́жу хлеб ___.</strong> "
                "(нож)</p>",
        "choices": ["ножо́м", "с ножо́м", "нож", "с ножа́"],
        "correct": "ножо́м",
        "explanation": "<p>Pichoq — asbob, u qoʻlingizda. Tekshiruv savoli: «u ham "
                       "men bilan birga kesyaptimi?» — yoʻq, demak predlogsiz.</p>",
    },
    {
        "text": "<p><strong>с</strong> kerakmi?</p><p><strong>Я говорю́ ___.</strong> "
                "(ма́ма)</p>",
        "choices": ["ма́мой", "с ма́мой", "ма́ме", "с ма́ме"],
        "correct": "с ма́мой",
        "explanation": "<p>Ona — hamroh, u ham gapiryapti. Demak <strong>с</strong> "
                       "kerak, va ayol jinsi qoʻshimchasi <strong>-ой</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Те́сто де́лают "
                "___.</strong> (ру́ки)</p>",
        "choices": ["ру́ки", "рука́ми", "с рука́ми", "рук"],
        "correct": "рука́ми",
        "explanation": "<p>Qoʻl — asbob, demak predlogsiz. <em>Рука́ми</em> — koʻplik "
                       "Твори́тельный shakli.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Чай ___.</strong> "
                "(са́хар)</p>",
        "choices": ["са́харом", "с са́харом", "са́хара", "с са́хара"],
        "correct": "с са́харом",
        "explanation": "<p>Bu yerda shakar <strong>qoʻshiladigan narsa</strong> — "
                       "asbob emas. Demak <strong>с</strong>: <em>чай с "
                       "са́харом</em>, <em>хлеб с сы́ром</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ ___.</strong> "
                "(она́)</p>",
        "choices": ["с её", "с ей", "с ней", "с неё"],
        "correct": "с ней",
        "explanation": "<p><strong>С ней</strong> — Твори́тельный shakli <em>ей</em>, "
                       "va predlogdan keyin <strong>Н</strong> qoʻshiladi. Bu qoida "
                       "hamma kelishikda ishlaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ем ___.</strong> "
                "(ло́жка)</p>",
        "choices": ["ло́жка", "ло́жкой", "с ло́жкой", "ло́жку"],
        "correct": "ло́жкой",
        "explanation": "<p>Qoshiq — asbob, demak predlogsiz. <em>«Я ем с "
                       "ло́жкой»</em> ruscha quloqqa gʻalati eshitiladi: «qoshiq bilan "
                       "birga ovqatlanyapman».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы говори́м с "
                "___.</strong> (учи́тель)</p>",
        "choices": ["учи́тель", "учи́теля", "учи́телем", "учи́телю"],
        "correct": "учи́телем",
        "explanation": "<p>Erkak jins <strong>-ем</strong> oladi (<em>-ь</em> ga "
                       "tugagani uchun). Predlogdan keyin ham qoʻshimcha "
                       "shart.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Он ре́жет ножо́м. · Он "
                "пришёл с ножо́м.</strong></p>",
        "choices": ["Pichoq bilan kesyapti · pichoq koʻtarib keldi",
                    "Ikkalasi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Pichoq bilan kesyapti · pichoq koʻtarib keldi",
        "explanation": "<p>Bitta soʻz, bitta kelishik — lekin predlog butun maʼnoni "
                       "oʻzgartiradi. Birinchisi asbob, ikkinchisi yonida olib "
                       "yurgan narsa.</p>",
    },
    {
        "text": "<p>Oʻzbekcha «bilan» ni ruschaga oʻgirishda qanday tekshiruv "
                "ishlatiladi?</p>",
        "choices": ["Bu asbobmi (qoʻlimda) yoki hamrohmi (u ham qilyaptimi)?",
                    "Bu jonlimi yoki jonsizmi?",
                    "Bu birlikmi yoki koʻplikmi?",
                    "Bu erkakmi yoki ayolmi?"],
        "correct": "Bu asbobmi (qoʻlimda) yoki hamrohmi (u ham qilyaptimi)?",
        "explanation": "<p>Asbob — predlogsiz (<em>ножо́м</em>). Hamroh yoki "
                       "qoʻshiladigan narsa — <strong>с</strong> bilan (<em>с "
                       "бра́том, с са́харом</em>).</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["пишу́ ру́чкой · иду́ с бра́том · чай с са́харом",
                    "пишу́ с ру́чкой · иду́ с бра́том · чай с са́харом",
                    "пишу́ ру́чкой · иду́ бра́том · чай са́харом",
                    "пишу́ с ру́чкой · иду́ бра́том · чай с са́харом"],
        "correct": "пишу́ ру́чкой · иду́ с бра́том · чай с са́харом",
        "explanation": "<p>Ruchka — asbob (predlogsiz). Aka — hamroh (С). Shakar — "
                       "qoʻshiladigan narsa (С). Uchta qaror, uchta toʻgʻri "
                       "javob.</p>",
    },
    {
        "text": "<p>Nega Твори́тельный kursda eng oxirida oʻrgatiladi?</p>",
        "choices": ["Chunki uning oʻzbekchada aniq juftligi yoʻq",
                    "Chunki u eng kam ishlatiladi",
                    "Chunki uning qoʻshimchalari eng qiyin",
                    "Chunki u faqat yozuvda uchraydi"],
        "correct": "Chunki uning oʻzbekchada aniq juftligi yoʻq",
        "explanation": "<p>Qolgan beshta kelishikning oʻzbekchada juftligi bor "
                       "(<em>-ning, -ga, -ni, -da, -dan</em>). Tvoritelniy esa "
                       "alohida kelishik emas, «bilan» soʻzi bilan beriladi — shuning "
                       "uchun u eng oxirida keladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мы говори́м с учи́телем.", "Я пишу́ с ру́чкой.",
                    "Чай с са́харом.", "Он е́дет авто́бусом."],
        "correct": "Я пишу́ с ру́чкой.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я пишу́ ру́чкой</strong>. Ruchka — "
                       "asbob, demak predlogsiz. Bu oʻzbek oʻquvchining eng koʻp "
                       "qiladigan xatosi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Пойдём с я.", "Пойдём со мной.",
                    "Пойдём с мной.", "Пойдём со мне."],
        "correct": "Пойдём со мной.",
        "explanation": "<p>Olmoshning Твори́тельный shakli <strong>мной</strong>, va "
                       "predlogga unli qoʻshiladi: <strong>со</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— С кем ты идёшь?</strong></p>",
        "choices": ["— С Афсо́ной.", "— Афсо́ной.", "— С Афсо́на.", "— К Афсо́не."],
        "correct": "— С Афсо́ной.",
        "explanation": "<p>Savol <em>с кем?</em> — hamroh haqida, demak javobda ham "
                       "<strong>с</strong> boʻladi. Ayol jinsi qoʻshimchasi "
                       "<strong>-ой</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Onam bilan pichoq bilan "
                "goʻsht kesyapmiz.</strong></p>",
        "choices": ["Мы ре́жем мя́со с ма́мой с ножо́м.",
                    "Мы ре́жем мя́со с ма́мой ножо́м.",
                    "Мы ре́жем мя́со ма́мой ножо́м.",
                    "Мы ре́жем мя́со ма́мой с ножо́м."],
        "correct": "Мы ре́жем мя́со с ма́мой ножо́м.",
        "explanation": "<p>Bitta gapda ikkala «bilan» ham bor: ona — hamroh "
                       "(<strong>с ма́мой</strong>), pichoq — asbob "
                       "(<strong>ножо́м</strong>, predlogsiz). Aynan shu gap darsning "
                       "butun mazmunini sinaydi.</p>",
    },
]


# =====================================================================
# PR-40 — Творительный 2: кем стать, joy predloglari
# =====================================================================

Q_PR40 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ма́ма рабо́тает "
                "___.</strong> (врач)</p>",
        "choices": ["врач", "врача́", "врачо́м", "врачу́"],
        "correct": "врачо́м",
        "explanation": "<p><em>Рабо́тать</em> + Твори́тельный = «kim boʻlib "
                       "ishlaydi». Oʻzbekchada bu «shifokor <strong>boʻlib</strong> "
                       "ishlaydi».</p>",
    },
    {
        "text": "<p>«Kim boʻlmoqchisan?» ruschada qanday soʻraladi?</p>",
        "choices": ["Кто ты хо́чешь стать?", "Кем ты хо́чешь стать?",
                    "Кого́ ты хо́чешь стать?", "Кому́ ты хо́чешь стать?"],
        "correct": "Кем ты хо́чешь стать?",
        "explanation": "<p>Savol soʻzining oʻzi ham kelishikka kiradi: <em>кто → "
                       "<strong>кем</strong></em>. Bu savol rus maktablarida har yili "
                       "beriladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Он учи́тель.", "Он учи́телем.",
                    "Он есть учи́телем.", "Он есть учи́тель."],
        "correct": "Он учи́тель.",
        "explanation": "<p>Hozirgi zamonda <em>быть</em> aytilmaydi (PR-11), demak "
                       "feʼl yoʻq — va kelishik ham kerak emas. Qoida: <strong>feʼl "
                       "bor — Твори́тельный, feʼl yoʻq — bosh kelishik</strong>.</p>",
    },
    {
        "text": "<p><strong>под</strong> predlogi qaysi kelishikni oladi?</p>",
        "choices": ["Предло́жный", "Вини́тельный", "Твори́тельный", "Роди́тельный"],
        "correct": "Твори́тельный",
        "explanation": "<p>Joy predloglari — <em>над, под, за, пе́ред, ме́жду, "
                       "ря́дом с</em> — hammasi Твори́тельный oladi: <em>под "
                       "столо́м</em>.</p>",
    },
    {
        "text": "<p><strong>над</strong> nima degani?</p>",
        "choices": ["tagida", "ustida (tegmasdan, havoda)",
                    "orqasida", "oldida"],
        "correct": "ustida (tegmasdan, havoda)",
        "explanation": "<p><em>Ла́мпа над столо́м</em> — lampa stol tepasida osilgan. "
                       "<em>НА</em> esa tegib turgan narsa uchun: <em>кни́га на "
                       "столе́</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Он "
                "учи́тель.</strong></p>",
        "choices": ["Он был учи́тель.", "Он был учи́телем.",
                    "Он была́ учи́телем.", "Он есть учи́телем."],
        "correct": "Он был учи́телем.",
        "explanation": "<p>Oʻtgan zamonda feʼl paydo boʻladi (<em>был</em>) — va u "
                       "bilan birga Твори́тельный ham keladi. Hozirgi zamonda esa "
                       "ikkalasi ham yoʻq edi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я хочу́ стать "
                "___.</strong> (инжене́р)</p>",
        "choices": ["инжене́р", "инжене́ра", "инжене́ром", "инжене́ру"],
        "correct": "инжене́ром",
        "explanation": "<p><em>Стать</em> — feʼl, demak Твори́тельный. Erkak jins "
                       "<strong>-ом</strong> oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ко́шка спит под "
                "___.</strong> (стол)</p>",
        "choices": ["стол", "стола́", "столу́", "столо́м"],
        "correct": "столо́м",
        "explanation": "<p><em>Под</em> Твори́тельный oladi. Urgʻu qoʻshimchada: "
                       "<em>стол → стол<strong>о́м</strong></em>.</p>",
    },
    {
        "text": "<p><strong>на</strong> yoki <strong>над</strong>?</p><p><strong>Кни́га "
                "___ столе́.</strong></p>",
        "choices": ["на", "над", "под", "за"],
        "correct": "на",
        "explanation": "<p>Kitob stolga <strong>tegib</strong> turibdi, demak "
                       "<em>на</em> + Предло́жный (<em>столе́</em>). Qoʻshimcha ham "
                       "buni koʻrsatib turibdi: <em>над</em> boʻlganda "
                       "<em>столо́м</em> boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Магази́н за "
                "___.</strong> (дом)</p>",
        "choices": ["дом", "до́ма", "до́му", "до́мом"],
        "correct": "до́мом",
        "explanation": "<p><em>За</em> + Твори́тельный = «orqasida». Erkak jins "
                       "<strong>-ом</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы стои́м пе́ред "
                "___.</strong> (шко́ла)</p>",
        "choices": ["шко́ла", "шко́лу", "шко́лой", "шко́ле"],
        "correct": "шко́лой",
        "explanation": "<p><em>Пе́ред</em> + Твори́тельный = «oldida». Ayol jinsi "
                       "<strong>-ой</strong> oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дед был ___.</strong> "
                "(стро́итель)</p>",
        "choices": ["стро́итель", "стро́ителя", "стро́ителем", "стро́ителю"],
        "correct": "стро́ителем",
        "explanation": "<p><em>Был</em> — feʼl, demak Твори́тельный. Soʻz "
                       "<strong>-ь</strong> ga tugagani uchun <strong>-ем</strong> "
                       "oladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qachon kasb bosh kelishikda, qachon Твори́тельный'da "
                "boʻladi?</p>",
        "choices": ["Feʼl bor — Твори́тельный, feʼl yoʻq — bosh kelishik",
                    "Har doim Твори́тельный",
                    "Erkak jinsida Твори́тельный, ayolda bosh kelishik",
                    "Oʻtgan zamonda bosh kelishik"],
        "correct": "Feʼl bor — Твори́тельный, feʼl yoʻq — bosh kelishik",
        "explanation": "<p><em>Он учи́тель</em> (feʼl yoʻq) — <em>Он был "
                       "учи́телем</em> / <em>рабо́тает учи́телем</em> / <em>хо́чет "
                       "стать учи́телем</em> (feʼl bor).</p>",
    },
    {
        "text": "<p><strong>на столе́</strong> va <strong>над столо́м</strong> "
                "farqi?</p>",
        "choices": ["Stol ustida (tegib) · stol tepasida (havoda)",
                    "Ikkalasi bir xil",
                    "Stol tagida · stol ustida",
                    "Ikkinchisi xato"],
        "correct": "Stol ustida (tegib) · stol tepasida (havoda)",
        "explanation": "<p>Bitta harf farq — <em>на</em> va <em>над</em> — lekin "
                       "kelishik ham boshqa: Предло́жный va Твори́тельный. "
                       "Oʻzbekchada ikkalasi ham «ustida» boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Oʻzbekchada «kim boʻlib» maʼnosi qanday beriladi?</p>",
        "choices": ["«boʻlib» soʻzi bilan", "«bilan» soʻzi bilan",
                    "«uchun» soʻzi bilan", "Hech qanday belgi qoʻyilmaydi"],
        "correct": "«boʻlib» soʻzi bilan",
        "explanation": "<p><em>oʻqituvchi <strong>boʻlib</strong> ishlaydi</em> → "
                       "<em>рабо́тает учи́телем</em>. Ikkala til ham bu yerda maxsus "
                       "belgi qoʻyadi — oʻzbekcha alohida soʻz bilan, ruscha "
                       "qoʻshimcha bilan.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi Твори́тельный?</p>",
        "choices": ["под столо́м · за до́мом · рабо́тает врачо́м",
                    "под столо́м · на столе́ · рабо́тает врачо́м",
                    "под столо́м · за до́мом · он врач",
                    "в шко́ле · за до́мом · рабо́тает врачо́м"],
        "correct": "под столо́м · за до́мом · рабо́тает врачо́м",
        "explanation": "<p><em>Под</em> va <em>за</em> Твори́тельный oladi, "
                       "<em>рабо́тать</em> ham. <em>На столе́</em> va <em>в "
                       "шко́ле</em> — Предло́жный, <em>он врач</em> — bosh "
                       "kelishik.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ко́шка спит под столо́м.", "Дед был стро́ителем.",
                    "Он рабо́тает инжене́р.", "Магази́н за до́мом."],
        "correct": "Он рабо́тает инжене́р.",
        "explanation": "<p>Toʻgʻrisi — <strong>Он рабо́тает инжене́ром</strong>. "
                       "<em>Рабо́тать</em> feʼli Твори́тельный talab qiladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я хочу́ стать врач.", "Я хочу́ стать врача́.",
                    "Я хочу́ стать врачо́м.", "Я хочу́ стать врачу́."],
        "correct": "Я хочу́ стать врачо́м.",
        "explanation": "<p><em>Стать</em> Твори́тельный oladi. Savolni ham eslang: "
                       "<em>Кем ты хо́чешь стать?</em> — savol soʻzi ham shu "
                       "kelishikda.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Кем рабо́тает твой оте́ц?</strong></p>",
        "choices": ["— Стро́ителем.", "— Стро́итель.",
                    "— Стро́ителя.", "— Стро́ителю."],
        "correct": "— Стро́ителем.",
        "explanation": "<p>Savol <em>кем?</em> — Твори́тельный, demak javob ham shu "
                       "shaklda. <em>Стро́итель</em> faqat feʼlsiz gapda boʻlardi: "
                       "<em>Мой оте́ц — стро́итель</em>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Hozir u oʻquvchi, keyin "
                "esa arxitektor boʻladi.</strong></p>",
        "choices": ["Сейча́с он учени́к, а пото́м бу́дет архите́ктор.",
                    "Сейча́с он учеником, а пото́м бу́дет архите́ктором.",
                    "Сейча́с он учени́к, а пото́м бу́дет архите́ктором.",
                    "Сейча́с он ученика́, а пото́м бу́дет архите́ктора."],
        "correct": "Сейча́с он учени́к, а пото́м бу́дет архите́ктором.",
        "explanation": "<p>Aynan shu gap darsning qoidasini koʻrsatadi: hozirgi "
                       "zamonda feʼl yoʻq → <strong>bosh kelishik</strong> "
                       "(<em>учени́к</em>); kelasi zamonda feʼl bor → "
                       "<strong>Твори́тельный</strong> (<em>архите́ктором</em>).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-38 Mashq: Дательный 2: мне холодно, ему нравится, по улице, к другу",
        "description": (
            "Holat (мне хо́лодно), yosh (мне два́дцать лет), К va ПО predloglari — "
            "va oʻzbekcha -GA ning chegarasi: joy → в/на, odam → к."
        ),
        "tutorial": "PR-38:",
        "questions": Q_PR38,
    },
    {
        "title": "PR-39 Mashq: Творительный 1: чем? — vosita va «с кем?» birgalik",
        "description": (
            "Oʻzbekcha «bilan» ning ikki tomoni: asbob predlogsiz (ножо́м), hamroh "
            "esa С bilan (с бра́том). Olmoshlar: со мной, с тобо́й, с ним."
        ),
        "tutorial": "PR-39:",
        "questions": Q_PR39,
    },
    {
        "title": "PR-40 Mashq: Творительный 2: быть/стать/работать + Т.п., над, под, за, перед, между",
        "description": (
            "Кем рабо́тать / стать, «feʼl bor — Т.п., feʼl yoʻq — bosh kelishik» "
            "qoidasi, va beshta joy predlogi. Oltita kelishik yakuni."
        ),
        "tutorial": "PR-40:",
        "questions": Q_PR40,
    },
]
