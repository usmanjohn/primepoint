# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-53 … PR-55.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_53_55.py --master=prime \\
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
# PR-53 — Vid uch zamonda
# =====================================================================

Q_PR53 = [
    # 1–5 tanish
    {
        "text": "<p>НСВ da nechta zamon bor?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Uchta",
        "explanation": "<p><em>чита́л · чита́ю · бу́ду чита́ть</em>. СВ da esa "
                       "faqat ikkita: <em>прочита́л</em> va <em>прочита́ю</em>.</p>",
    },
    {
        "text": "<p><strong>прочита́ю</strong> — bu qaysi zamon?</p>",
        "choices": ["Hozirgi", "Oʻtgan", "Kelasi", "Zamonsiz"],
        "correct": "Kelasi",
        "explanation": "<p>СВ da hozirgi zamon yoʻq. Shakl hozirgi zamon kabi "
                       "tuslansa ham (<em>прочита́ю, прочита́ешь…</em>), u "
                       "<strong>kelasi zamon</strong>ni bildiradi.</p>",
    },
    {
        "text": "<p>Nega СВ da hozirgi zamon yoʻq?</p>",
        "choices": ["Chunki tugagan ish hozir boʻla olmaydi",
                    "Chunki СВ faqat yozuvda ishlatiladi",
                    "Chunki СВ shakllari juda uzun",
                    "Bu shunchaki istisno"],
        "correct": "Chunki tugagan ish hozir boʻla olmaydi",
        "explanation": "<p>Hozir davom etayotgan ish tugamagan; tugagan ish esa hozir "
                       "emas. Ikkalasi bir vaqtda boʻlishi mumkin emas — shuning "
                       "uchun oʻrtada boʻshliq.</p>",
    },
    {
        "text": "<p>СВ kelasi zamoni qanday yasaladi?</p>",
        "choices": ["бу́ду + infinitiv", "Bir soʻz — hozirgi zamon kabi tuslanadi",
                    "Oʻtgan zamon + -у", "Yasalmaydi"],
        "correct": "Bir soʻz — hozirgi zamon kabi tuslanadi",
        "explanation": "<p><em>прочита́ю, напишу́, скажу́, сде́лаю</em>. СВ bilan "
                       "<strong>бу́ду ishlatilmaydi</strong>.</p>",
    },
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>За́втра я бу́ду "
                "чита́ть. · За́втра я прочита́ю кни́гу.</strong></p>",
        "choices": ["Jarayon (vaʼda yoʻq) · natija (vaʼda bor)",
                    "Ikkalasi bir xil", "Birinchisi oʻtgan zamon",
                    "Ikkinchisi hozirgi zamon"],
        "correct": "Jarayon (vaʼda yoʻq) · natija (vaʼda bor)",
        "explanation": "<p><em>Бу́ду чита́ть</em> — nima qilishimni aytadi, tugatish "
                       "haqida hech narsa vaʼda qilmaydi. <em>Прочита́ю</em> — kitob "
                       "ertaga tugaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>За́втра я ___ "
                "письмо́.</strong> («yozib boʻlaman» maʼnosida)</p>",
        "choices": ["бу́ду писа́ть", "напишу́", "бу́ду написа́ть", "пишу́"],
        "correct": "напишу́",
        "explanation": "<p>СВ oʻzi kelasi zamonni bildiradi — <em>бу́ду</em> "
                       "qoʻshilmaydi. <em>«Бу́ду написа́ть»</em> — xato.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Сейча́с я ___ "
                "кни́гу.</strong></p>",
        "choices": ["прочита́ю", "чита́ю", "прочита́л", "бу́ду чита́ть"],
        "correct": "чита́ю",
        "explanation": "<p>«Сейча́с» hozirgi zamon talab qiladi, СВ da esa hozirgi "
                       "zamon yoʻq. <em>Прочита́ю</em> kelasi zamon boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>За́втра он ___ ка́ждый "
                "день.</strong></p>",
        "choices": ["прочита́ет", "бу́дет чита́ть", "чита́л", "прочита́л"],
        "correct": "бу́дет чита́ть",
        "explanation": "<p>«Ка́ждый день» — takror, demak <strong>НСВ</strong>. "
                       "Kelasi zamonda НСВ ikki soʻz bilan yasaladi.</p>",
    },
    {
        "text": "<p><strong>сказа́ть</strong> feʼlining kelasi zamon «я» shakli "
                "qaysi?</p>",
        "choices": ["бу́ду сказа́ть", "скажу́", "говорю́", "сказа́л"],
        "correct": "скажу́",
        "explanation": "<p>СВ kelasi zamoni bir soʻz: <strong>скажу́, ска́жешь, "
                       "ска́жет…</strong> Bu <em>говори́ть — сказа́ть</em> "
                       "juftligidan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вчера́ я ___ весь "
                "ве́чер, но не ___.</strong> (чита́ть / прочита́ть)</p>",
        "choices": ["прочита́л … чита́л", "чита́л … прочита́л",
                    "чита́л … чита́л", "прочита́л … прочита́л"],
        "correct": "чита́л … прочита́л",
        "explanation": "<p>Jarayon boʻldi (НСВ), natija boʻlmadi (СВ). Bu ziddiyat "
                       "emas — bu vid tizimining butun kuchi.</p>",
    },
    {
        "text": "<p><strong>взять</strong> feʼlining kelasi zamon «я» shakli "
                "qaysi?</p>",
        "choices": ["бу́ду взять", "беру́", "возьму́", "взял"],
        "correct": "возьму́",
        "explanation": "<p><em>Брать — взять</em> juftligi. СВ kelasi zamoni bir "
                       "soʻz: <strong>возьму́, возьмёшь, возьмёт…</strong></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>За́втра мы ___ "
                "фильм.</strong> («koʻramiz, tugatamiz» maʼnosida)</p>",
        "choices": ["бу́дем смотре́ть", "посмо́трим", "смо́трим", "смотре́ли"],
        "correct": "посмо́трим",
        "explanation": "<p>Natija — <strong>СВ</strong>, va u bir soʻz bilan kelasi "
                       "zamonni bildiradi: <em>посмотре́ть → посмо́трим</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi shakl bilan <strong>бу́ду</strong> ishlatilmaydi?</p>",
        "choices": ["НСВ infinitiv", "СВ infinitiv", "Ikkalasi bilan", "Hech qaysi"],
        "correct": "СВ infinitiv",
        "explanation": "<p><em>Бу́ду чита́ть</em> ✓ (НСВ), <em>«бу́ду прочита́ть»</em> "
                       "✗ (СВ). СВ oʻzi kelasi zamonni bildiradi.</p>",
    },
    {
        "text": "<p><strong>чита́ю</strong> va <strong>прочита́ю</strong> — nima "
                "farq qiladi?</p>",
        "choices": ["Hozir · ertaga", "Ertaga · hozir",
                    "Ikkalasi hozir", "Ikkalasi ertaga"],
        "correct": "Hozir · ertaga",
        "explanation": "<p>Shakl juda oʻxshaydi, farq faqat prefiksda — lekin maʼno "
                       "butunlay boshqa: <em>чита́ю</em> hozirgi zamon, "
                       "<em>прочита́ю</em> kelasi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida nechta kelasi zamon bor deb aytish mumkin?</p>",
        "choices": ["Bitta — oʻqiyman", "Ikkita — oʻqiyman va oʻqib chiqaman",
                    "Uchta", "Kelasi zamon yoʻq"],
        "correct": "Ikkita — oʻqiyman va oʻqib chiqaman",
        "explanation": "<p>Farq ikkala tilda ham bir xil: birinchisi nima "
                       "qilishingizni aytadi, ikkinchisi nima tugashini. Faqat "
                       "oʻzbekchada tanlov ixtiyoriy, ruschada majburiy.</p>",
    },
    {
        "text": "<p>СВ da qaysi ikkita zamon bor?</p>",
        "choices": ["Hozirgi va kelasi", "Oʻtgan va hozirgi",
                    "Oʻtgan va kelasi", "Faqat oʻtgan"],
        "correct": "Oʻtgan va kelasi",
        "explanation": "<p><em>Прочита́л</em> (tugadi) va <em>прочита́ю</em> "
                       "(tugaydi). Oʻrtada — hech narsa, chunki tugagan ish hozir "
                       "boʻla olmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Вчера́ я чита́л два часа́.", "За́втра я бу́ду прочита́ть.",
                    "Сейча́с я чита́ю.", "За́втра я прочита́ю."],
        "correct": "За́втра я бу́ду прочита́ть.",
        "explanation": "<p>СВ bilan <em>бу́ду</em> ishlatilmaydi. Toʻgʻrisi — "
                       "<strong>За́втра я прочита́ю</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Сейча́с я прочита́ю кни́гу.", "Сейча́с я чита́ю кни́гу.",
                    "Сейча́с я прочита́л кни́гу.", "Сейча́с я бу́ду прочита́ть."],
        "correct": "Сейча́с я чита́ю кни́гу.",
        "explanation": "<p>«Сейча́с» — hozirgi zamon, va u faqat <strong>НСВ</strong> "
                       "da mavjud.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Когда́ ты прочита́ешь кни́гу?</strong></p>",
        "choices": ["— За́втра прочита́ю.", "— За́втра бу́ду прочита́ть.",
                    "— За́втра прочита́л.", "— За́втра чита́ю."],
        "correct": "— За́втра прочита́ю.",
        "explanation": "<p>Savol СВ kelasi zamonda, javob ham shunday. "
                       "<em>Прочита́ю</em> — bir soʻz, <em>бу́ду</em> siz.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Ertaga kechqurun "
                "oʻqiyman, lekin kitobni oʻqib chiqmayman.</strong></p>",
        "choices": ["За́втра ве́чером я прочита́ю, но не бу́ду чита́ть кни́гу.",
                    "За́втра ве́чером я бу́ду чита́ть, но не прочита́ю кни́гу.",
                    "За́втра ве́чером я чита́ю, но не прочита́л кни́гу.",
                    "За́втра ве́чером я бу́ду прочита́ть, но не чита́ю кни́гу."],
        "correct": "За́втра ве́чером я бу́ду чита́ть, но не прочита́ю кни́гу.",
        "explanation": "<p>Jarayon — <strong>бу́ду чита́ть</strong> (НСВ kelasi). "
                       "Natija boʻlmaydi — <strong>не прочита́ю</strong> (СВ "
                       "kelasi).</p>",
    },
]


# =====================================================================
# PR-54 — Vidni tanlash
# =====================================================================

Q_PR54 = [
    # 1–5 tanish
    {
        "text": "<p>Bu soʻz qaysi vidni chaqiradi?</p><p><strong>ка́ждый день</strong></p>",
        "choices": ["НСВ", "СВ", "Ikkalasi", "Hech qaysi"],
        "correct": "НСВ",
        "explanation": "<p>Takror — <strong>НСВ</strong>. Xuddi shunday: <em>ча́сто, "
                       "ре́дко, иногда́, всегда́, обы́чно</em>.</p>",
    },
    {
        "text": "<p>Bu soʻz qaysi vidni chaqiradi?</p><p><strong>наконе́ц</strong></p>",
        "choices": ["НСВ", "СВ", "Ikkalasi", "Hech qaysi"],
        "correct": "СВ",
        "explanation": "<p>Kutilgan natija — <strong>СВ</strong>. Xuddi shunday: "
                       "<em>вдруг, уже́, сра́зу, за час</em>.</p>",
    },
    {
        "text": "<p><strong>два часа́</strong> va <strong>за два часа́</strong> — "
                "farqi nima?</p>",
        "choices": ["Davomiylik (НСВ) · muddat (СВ)", "Muddat (СВ) · davomiylik (НСВ)",
                    "Ikkalasi bir xil", "Ikkinchisi xato"],
        "correct": "Davomiylik (НСВ) · muddat (СВ)",
        "explanation": "<p><em>Чита́л два часа́</em> — qancha vaqt ketgani. "
                       "<em>Прочита́л за два часа́</em> — qancha vaqtda tugagani. "
                       "Bitta predlog butun maʼnoni oʻzgartiradi.</p>",
    },
    {
        "text": "<p>Ketma-ketlik (u keldi, oʻtirdi, yozdi) qaysi vidni talab "
                "qiladi?</p>",
        "choices": ["НСВ", "СВ", "Aralash", "Farqi yoʻq"],
        "correct": "СВ",
        "explanation": "<p><em>Пришёл, сел и написа́л</em> — uchta tugagan ish, "
                       "birin-ketin. НСВ boʻlsa, ular bir vaqtda davom etayotgan "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Inkor buyruqda qaysi vid ishlatiladi?</p>",
        "choices": ["СВ", "НСВ", "Ikkalasi teng", "Buyruqda vid yoʻq"],
        "correct": "НСВ",
        "explanation": "<p><em>Не чита́й, не де́лай, не говори́</em> — deyarli har "
                       "doim НСВ. Buyruq shakli PR-59 da toʻliq koʻriladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ка́ждый день он ___ "
                "ма́ме.</strong> (звони́ть / позвони́ть)</p>",
        "choices": ["позвони́л", "звони́л", "позвони́т", "позвони́ть"],
        "correct": "звони́л",
        "explanation": "<p>«Ка́ждый день» — takror, demak <strong>НСВ</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Наконе́ц он "
                "___.</strong> (звони́ть / позвони́ть)</p>",
        "choices": ["звони́л", "позвони́л", "звони́т", "бу́дет звони́ть"],
        "correct": "позвони́л",
        "explanation": "<p>«Наконе́ц» — kutilgan natija, demak "
                       "<strong>СВ</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ кни́гу два "
                "часа́.</strong></p>",
        "choices": ["прочита́л", "чита́л", "прочита́ет", "прочита́ть"],
        "correct": "чита́л",
        "explanation": "<p>«Два часа́» — davomiylik, demak <strong>НСВ</strong>. Agar "
                       "«за два часа́» boʻlsa, СВ kerak boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ___ кни́гу за два "
                "часа́.</strong></p>",
        "choices": ["чита́л", "прочита́л", "чита́ет", "бу́дет чита́ть"],
        "correct": "прочита́л",
        "explanation": "<p>«За два часа́» — muddat, demak <strong>СВ</strong>. Bitta "
                       "predlog vidni oʻzgartirdi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___. Вдруг он "
                "___.</strong> (чита́ть / прийти́)</p>",
        "choices": ["прочита́л … шёл", "чита́л … пришёл",
                    "чита́л … приходи́л", "прочита́л … пришёл"],
        "correct": "чита́л … пришёл",
        "explanation": "<p><strong>Fon va hodisa</strong>: uzun jarayon (НСВ) va "
                       "uning ichida sodir boʻlgan bir narsa (СВ). «Вдруг» СВ ni "
                       "chaqiradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ра́ньше я ___ в теа́тр "
                "ча́сто.</strong> (ходи́ть)</p>",
        "choices": ["пошёл", "ходи́л", "пойду́", "схожу́"],
        "correct": "ходи́л",
        "explanation": "<p>«Ра́ньше» va «ча́сто» — ikkalasi ham НСВ signali: takror "
                       "va odat.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Не ___ э́ту "
                "кни́гу!</strong></p>",
        "choices": ["прочита́й", "чита́й", "прочита́ть", "чита́ть"],
        "correct": "чита́й",
        "explanation": "<p>Inkor buyruqda deyarli har doim <strong>НСВ</strong>: "
                       "<em>не чита́й, не де́лай, не говори́</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi qatorda hammasi НСВ signali?</p>",
        "choices": ["ка́ждый день · до́лго · ча́сто",
                    "наконе́ц · вдруг · уже́",
                    "ка́ждый день · наконе́ц · вдруг",
                    "за час · сра́зу · до конца́"],
        "correct": "ка́ждый день · до́лго · ча́сто",
        "explanation": "<p>Takror va davomiylik — НСВ. Ikkinchi va toʻrtinchi "
                       "qatorlar СВ signallari; uchinchisi aralash.</p>",
    },
    {
        "text": "<p>«Fon va hodisa» qurilishi qanday ishlaydi?</p>",
        "choices": ["НСВ (uzun jarayon) + СВ (ichida sodir boʻlgan ish)",
                    "СВ + СВ", "НСВ + НСВ", "СВ (fon) + НСВ (hodisa)"],
        "correct": "НСВ (uzun jarayon) + СВ (ichida sodir boʻlgan ish)",
        "explanation": "<p><em>Я чита́л. Вдруг он пришёл.</em> Bu naqsh hikoyalarda "
                       "doim uchraydi va vidni oʻzi tanlaydi.</p>",
    },
    {
        "text": "<p>Signal soʻzlar oʻzbek tilida ham xuddi shunday ishlaydimi?</p>",
        "choices": ["Ha — «har kuni oʻqirdim», «nihoyat oʻqib chiqdim»",
                    "Yoʻq, oʻzbekchada signal soʻzlar yoʻq",
                    "Faqat oʻtgan zamonda",
                    "Faqat yozuvda"],
        "correct": "Ha — «har kuni oʻqirdim», «nihoyat oʻqib chiqdim»",
        "explanation": "<p>Tanlov mantigʻi bir xil. Farq faqat shundaki, oʻzbekchada "
                       "tanlov ixtiyoriy (<em>oʻqidim</em> deb qoʻyaverish mumkin), "
                       "ruschada esa majburiy.</p>",
    },
    {
        "text": "<p>Bu ikki buyruqning farqi nima?</p><p><strong>Чита́й! · "
                "Прочита́й э́то!</strong></p>",
        "choices": ["Umumiy taklif · aniq vazifa", "Aniq vazifa · umumiy taklif",
                    "Ikkalasi bir xil", "Birinchisi xato"],
        "correct": "Umumiy taklif · aniq vazifa",
        "explanation": "<p><em>Чита́й</em> (НСВ) — «oʻqi, oʻqib tur». <em>Прочита́й "
                       "э́то</em> (СВ) — «buni oxirigacha oʻqib chiq».</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Ка́ждый день он звони́л ма́ме.", "Наконе́ц он позвони́л.",
                    "Он прочита́л кни́гу два часа́.", "Он пришёл, сел и написа́л."],
        "correct": "Он прочита́л кни́гу два часа́.",
        "explanation": "<p>«Два часа́» — davomiylik, demak НСВ: <strong>чита́л</strong>. "
                       "СВ bilan faqat «за два часа́» ishlaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Не прочита́й э́ту кни́гу!", "Не чита́й э́ту кни́гу!",
                    "Не прочита́ть э́ту кни́гу!", "Не чита́ть э́ту кни́гу!"],
        "correct": "Не чита́й э́ту кни́гу!",
        "explanation": "<p>Inkor buyruqda <strong>НСВ</strong> ishlatiladi. Va buyruq "
                       "shakli infinitiv emas.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты ча́сто хо́дишь в теа́тр?</strong></p>",
        "choices": ["— Ра́ньше ходи́л ча́сто, тепе́рь ре́дко.",
                    "— Ра́ньше пошёл ча́сто, тепе́рь ре́дко.",
                    "— Ра́ньше схожу́ ча́сто, тепе́рь ре́дко.",
                    "— Ра́ньше ходи́ть ча́сто, тепе́рь ре́дко."],
        "correct": "— Ра́ньше ходи́л ча́сто, тепе́рь ре́дко.",
        "explanation": "<p>«Ра́ньше» va «ча́сто» — НСВ signallari: takror va odat. "
                       "Bu yerda СВ mos kelmaydi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Uzoq qidirdim va "
                "nihoyat topdim.</strong></p>",
        "choices": ["Я до́лго нашёл и наконе́ц иска́л.",
                    "Я до́лго иска́л и наконе́ц нашёл.",
                    "Я до́лго иска́л и наконе́ц иска́л.",
                    "Я до́лго нашёл и наконе́ц нашёл."],
        "correct": "Я до́лго иска́л и наконе́ц нашёл.",
        "explanation": "<p>«До́лго» — davomiylik (НСВ <em>иска́л</em>), «наконе́ц» — "
                       "natija (СВ <em>нашёл</em>). Ikkita signal soʻz, ikkita "
                       "vid.</p>",
    },
]


# =====================================================================
# PR-55 — идти va ходить
# =====================================================================

Q_PR55 = [
    # 1–5 tanish
    {
        "text": "<p><strong>идти́</strong> va <strong>ходи́ть</strong> — farqi "
                "nima?</p>",
        "choices": ["Vid farqi: НСВ va СВ", "Yoʻnalish farqi: bir tomonga ↔ muntazam",
                    "Zamon farqi", "Farqi yoʻq"],
        "correct": "Yoʻnalish farqi: bir tomonga ↔ muntazam",
        "explanation": "<p>Ikkalasi ham <strong>НСВ</strong>. <em>Идти́</em> — hozir, "
                       "bir tomonga. <em>Ходи́ть</em> — muntazam yoki "
                       "borib-kelish.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ___ в шко́лу ка́ждый "
                "день.</strong></p>",
        "choices": ["иду́", "хожу́", "шёл", "пойду́"],
        "correct": "хожу́",
        "explanation": "<p>«Ка́ждый день» — takror, demak koʻp yoʻnalish. Oʻzbekcha "
                       "tekshiruv: «borib turaman».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Сейча́с я ___ "
                "домо́й.</strong></p>",
        "choices": ["хожу́", "иду́", "ходи́л", "хо́дит"],
        "correct": "иду́",
        "explanation": "<p>«Сейча́с» — aynan hozir, yoʻldaman. Oʻzbekcha: "
                       "«ketyapman».</p>",
    },
    {
        "text": "<p><strong>ходи́л</strong> nimani anglatadi?</p>",
        "choices": ["Yoʻlda edim", "Bordim va qaytdim",
                    "Boraman", "Bormoqchi edim"],
        "correct": "Bordim va qaytdim",
        "explanation": "<p><em>Ходи́л</em> — <strong>borib-kelish</strong>, tugagan "
                       "safar. Oʻzbekcha: «borib keldim». <em>Шёл</em> esa «yoʻlda "
                       "edim».</p>",
    },
    {
        "text": "<p><strong>идти́</strong> va <strong>ходи́ть</strong> qanday "
                "harakat uchun ishlatiladi?</p>",
        "choices": ["Faqat oyoq bilan yurish", "Faqat transportda",
                    "Ikkalasi ham", "Faqat uzoq masofaga"],
        "correct": "Faqat oyoq bilan yurish",
        "explanation": "<p>Transport uchun boshqa juftlik bor: <strong>е́хать ↔ "
                       "е́здить</strong> (PR-56). Yagona istisno — transportning "
                       "oʻzi: <em>авто́бус идёт</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Вчера́ я ___ в магази́н "
                "и купи́л хлеб.</strong></p>",
        "choices": ["шёл", "ходи́л", "иду́", "хожу́"],
        "correct": "ходи́л",
        "explanation": "<p>Bordim va qaytdim — borib-kelish. <em>Шёл</em> boʻlsa, gap "
                       "faqat yoʻl haqida boʻlardi: «ketayotgan edim».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У́тром я ___ в шко́лу и "
                "ду́мал о ба́бушке.</strong></p>",
        "choices": ["ходи́л", "шёл", "хожу́", "иду́"],
        "correct": "шёл",
        "explanation": "<p>Yoʻlda edim va oʻylab bordim — bir tomonga, jarayon. "
                       "<em>Ходи́л</em> butun safarni bildirardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ребёнок уже́ "
                "___.</strong> («yura oladi» maʼnosida)</p>",
        "choices": ["идёт", "хо́дит", "шёл", "ходи́л"],
        "correct": "хо́дит",
        "explanation": "<p>Umumiy qobiliyat — <em>ходи́ть</em> ning uchinchi ishi. "
                       "<em>Идёт</em> «hozir ketyapti» degan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ дождь.</strong></p>",
        "choices": ["Хо́дит", "Идёт", "Ходи́л", "Хожу́"],
        "correct": "Идёт",
        "explanation": "<p>Ob-havo <em>идти́</em> bilan: <strong>идёт дождь, идёт "
                       "снег</strong>. Bu PR-23 dan tanish ibora.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ты ча́сто ___ в "
                "теа́тр?</strong></p>",
        "choices": ["идёшь", "хо́дишь", "шёл", "ходи́л"],
        "correct": "хо́дишь",
        "explanation": "<p>«Ча́сто» — takror, demak koʻp yoʻnalish. Bu «teatrga borib "
                       "turasanmi?» degan savol.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Куда́ ты "
                "___?</strong> (hozir)</p>",
        "choices": ["хо́дишь", "идёшь", "ходи́л", "шёл"],
        "correct": "идёшь",
        "explanation": "<p>«Куда́?» va hozirgi payt — bir tomonga, aynan hozir. "
                       "<em>Хо́дишь</em> «qayerga borib turasan?» degan gʻalati savol "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Авто́бус ___ в "
                "центр.</strong></p>",
        "choices": ["хо́дит", "идёт", "ходи́л", "шёл"],
        "correct": "идёт",
        "explanation": "<p>Transport marshruti — <em>идти́</em>. Bu yagona istisno: "
                       "transportning oʻzi «yuradi» deb qaraladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Я шёл в магази́н. · Я "
                "ходи́л в магази́н.</strong></p>",
        "choices": ["Yoʻlda edim · borib keldim", "Borib keldim · yoʻlda edim",
                    "Ikkalasi bir xil", "Birinchisi kelasi zamon"],
        "correct": "Yoʻlda edim · borib keldim",
        "explanation": "<p><em>Шёл</em> — bir tomonga, jarayon; yetib bordimmi "
                       "nomaʼlum. <em>Ходи́л</em> — bordim va qaytdim, tugagan "
                       "safar.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida bu farq qanday koʻrsatiladi?</p>",
        "choices": ["boryapman · borib turaman · borib keldim",
                    "Koʻrsatilmaydi",
                    "Faqat «bordim» bilan",
                    "Faqat ohang bilan"],
        "correct": "boryapman · borib turaman · borib keldim",
        "explanation": "<p>Uchta maʼno — uchta shakl, ikkala tilda ham. Faqat "
                       "oʻzbekcha <em>bordim</em> neytral boʻlib, uchala maʼnoda ham "
                       "ishlatilishi mumkin.</p>",
    },
    {
        "text": "<p><strong>ходи́ть</strong> ning uchta ishi nima?</p>",
        "choices": ["Takror · borib-kelish · qobiliyat",
                    "Hozir · kecha · ertaga",
                    "Piyoda · transportda · uchib",
                    "НСВ · СВ · neytral"],
        "correct": "Takror · borib-kelish · qobiliyat",
        "explanation": "<p><em>Хожу́ ка́ждый день</em> (takror), <em>вчера́ ходи́л</em> "
                       "(borib-kelish), <em>ребёнок хо́дит</em> (qobiliyat).</p>",
    },
    {
        "text": "<p><strong>идти́</strong> yana qaysi maʼnolarda ishlatiladi?</p>",
        "choices": ["Ob-havo, tadbir, transport, vaqt",
                    "Faqat odam yurishi", "Faqat transport", "Faqat ob-havo"],
        "correct": "Ob-havo, tadbir, transport, vaqt",
        "explanation": "<p><em>Идёт дождь · идёт фильм · авто́бус идёт · вре́мя "
                       "идёт</em>. Bu iboralar butunligicha yodlanadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Сейча́с я иду́ домо́й.", "Я хожу́ в теа́тр ре́дко.",
                    "Я иду́ в шко́лу ка́ждый день.", "Идёт дождь."],
        "correct": "Я иду́ в шко́лу ка́ждый день.",
        "explanation": "<p>«Ка́ждый день» takrorni bildiradi, demak koʻp yoʻnalish "
                       "kerak: <strong>Я хожу́ в шко́лу ка́ждый день</strong>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Вчера́ я шёл к врачу́ и верну́лся.",
                    "Вчера́ я ходи́л к врачу́.",
                    "Вчера́ я хожу́ к врачу́.",
                    "Вчера́ я иду́ к врачу́."],
        "correct": "Вчера́ я ходи́л к врачу́.",
        "explanation": "<p>Bordim va qaytdim — <strong>ходи́л</strong>. Birinchi "
                       "variantda «шёл … и верну́лся» ziddiyatli: <em>шёл</em> faqat "
                       "yoʻlni bildiradi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Где ты был вчера́?</strong></p>",
        "choices": ["— Я ходи́л к врачу́.", "— Я шёл к врачу́.",
                    "— Я иду́ к врачу́.", "— Я хожу́ к врачу́."],
        "correct": "— Я ходи́л к врачу́.",
        "explanation": "<p>Savol butun safar haqida («qayerda eding?»), demak "
                       "<strong>ходи́л</strong> — bordim va qaytdim.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Har kuni maktabga "
                "boraman, lekin bugun sekin ketyapman.</strong></p>",
        "choices": ["Ка́ждый день я иду́ в шко́лу, но сего́дня хожу́ ме́дленно.",
                    "Ка́ждый день я хожу́ в шко́лу, но сего́дня иду́ ме́дленно.",
                    "Ка́ждый день я хожу́ в шко́лу, но сего́дня хожу́ ме́дленно.",
                    "Ка́ждый день я шёл в шко́лу, но сего́дня иду́ ме́дленно."],
        "correct": "Ка́ждый день я хожу́ в шко́лу, но сего́дня иду́ ме́дленно.",
        "explanation": "<p>«Har kuni» — takror (<strong>хожу́</strong>), «bugun "
                       "ketyapman» — aynan hozir, bir tomonga "
                       "(<strong>иду́</strong>).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-53 Mashq: Vid uch zamonda: hozirgi zamonda СВ nega yoʻq?",
        "description": (
            "Ikkita kelasi zamon: бу́ду чита́ть (vaʼda yoʻq) va прочита́ю (vaʼda "
            "bor). СВ kelasi zamoni bir soʻz — бу́ду ishlatilmaydi."
        ),
        "tutorial": "PR-53:",
        "questions": Q_PR53,
    },
    {
        "title": "PR-54 Mashq: Vidni tanlash: takror, jarayon, natija, bir marta, buyruq",
        "description": (
            "Signal soʻzlar: ка́ждый день va до́лго (НСВ), наконе́ц va за час "
            "(СВ). Ketma-ketlik, fon-hodisa va inkor buyruq."
        ),
        "tutorial": "PR-54:",
        "questions": Q_PR54,
    },
    {
        "title": "PR-55 Mashq: Harakat feʼllari 1: идти va ходить",
        "description": (
            "Bir yoʻnalish ↔ koʻp yoʻnalish: иду́ (hozir), хожу́ (muntazam), "
            "ходи́л (borib-kelish), хо́дит (qobiliyat)."
        ),
        "tutorial": "PR-55:",
        "questions": Q_PR55,
    },
]
