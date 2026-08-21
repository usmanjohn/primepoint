# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-27 … PR-28.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_27_28.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Russian",
    "description": "Rus tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#b91c1c",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PR-27 — Нужно, надо, можно, нельзя, должен
# =====================================================================

Q_PR27 = [
    # 1–5 tanish
    {
        "text": "<p><strong>на́до</strong> nima degani?</p>",
        "choices": ["mumkin", "kerak", "mumkin emas", "albatta"],
        "correct": "kerak",
        "explanation": "<p><strong>На́до</strong> va <strong>ну́жно</strong> — «kerak». "
                       "Farqi juda kichik: <em>на́до</em> soʻzlashuvroq, <em>ну́жно</em> "
                       "biroz rasmiyroq va yozuvda koʻproq uchraydi.</p>",
    },
    {
        "text": "<p><strong>нельзя́</strong> nima degani?</p>",
        "choices": ["kerak emas", "mumkin", "mumkin emas", "qiyin"],
        "correct": "mumkin emas",
        "explanation": "<p><strong>Нельзя́</strong> — <em>мо́жно</em> ning inkori va u "
                       "<strong>bitta soʻz</strong>. «Не мо́жно» degan shakl rus tilida "
                       "umuman yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ на́до рабо́тать.</strong> "
                "(«menga» maʼnosida)</p>",
        "choices": ["Я", "Мне", "Мой", "Меня́"],
        "correct": "Мне",
        "explanation": "<p><strong>Мне</strong> — oʻzbekchadagi «men<strong>ga</strong>» "
                       "ning oʻzi. <em>На́до</em> shaxssiz qurilishda ishlaydi va yonida "
                       "ega turmaydi, shuning uchun <em>«Я на́до»</em> — xato.</p>",
    },
    {
        "text": "<p>Bu shakllardan qaysi biri «unga (ayol)» degani?</p>",
        "choices": ["ему́", "ей", "им", "вам"],
        "correct": "ей",
        "explanation": "<p>Yettita shakl: <em>мне, тебе́, ему́ (erkak), <strong>ей</strong> "
                       "(ayol), нам, вам, им</em>. Bularni hozircha lugʻat sifatida "
                       "yodlang — kelishikning oʻzi PR-37 da.</p>",
    },
    {
        "text": "<p><strong>до́лжен</strong> boshqa soʻzlardan nimasi bilan farq "
                "qiladi?</p>",
        "choices": ["U hech qachon oʻzgarmaydi",
                    "U yonida haqiqiy ega boʻladi va jinsga moslashadi",
                    "U faqat oʻtgan zamonda ishlatiladi",
                    "U infinitiv talab qilmaydi"],
        "correct": "U yonida haqiqiy ega boʻladi va jinsga moslashadi",
        "explanation": "<p><em>На́до, ну́жно, мо́жно, нельзя́</em> — hech qachon "
                       "oʻzgarmaydi va ega olmaydi. <strong>До́лжен</strong> esa sifat "
                       "kabi ishlaydi: <em>я до́лжен, она́ должна́, мы должны́</em>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Афсо́на ___ идти́ "
                "домо́й.</strong> (до́лжен)</p>",
        "choices": ["до́лжен", "должно́", "должна́", "должны́"],
        "correct": "должна́",
        "explanation": "<p>Afsona — qiz, demak <strong>должна́</strong>, urgʻu oxirida. "
                       "Toʻrtta shakl: <em>до́лжен / должна́ / должно́ / должны́</em> — "
                       "xuddi sifat kabi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь ___ кури́ть.</strong> "
                "(«mumkin emas» maʼnosida)</p>",
        "choices": ["не мо́жно", "нельзя́", "не на́до бы́ло", "не ну́жно"],
        "correct": "нельзя́",
        "explanation": "<p><strong>Нельзя́</strong> — taqiq. <em>«Не мо́жно»</em> degan "
                       "soʻz yoʻq, va oʻzbek oʻquvchi aynan shu xatoni qiladi, chunki "
                       "«mumkin emas» ni soʻzma-soʻz oʻgiradi.</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Мне на́до "
                "рабо́тать.</strong></p>",
        "choices": ["Мне на́до был рабо́тать.", "Мне на́до была́ рабо́тать.",
                    "Мне на́до бы́ло рабо́тать.", "Я на́до бы́ло рабо́тать."],
        "correct": "Мне на́до бы́ло рабо́тать.",
        "explanation": "<p>Shaxssiz gapda ega yoʻq, shuning uchun <em>быть</em> har doim "
                       "<strong>oʻrta jinsda</strong> qoladi: <strong>бы́ло</strong>. "
                       "Xuddi shunday: <em>мо́жно бы́ло, нельзя́ бы́ло, ну́жно "
                       "бы́ло</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ ну́жно спеши́ть.</strong> "
                "(«bizga» maʼnosida)</p>",
        "choices": ["Мы", "Нам", "Наш", "Нас"],
        "correct": "Нам",
        "explanation": "<p><strong>Нам</strong> = «biz<strong>ga</strong>». Yana bir bor: "
                       "<em>ну́жно</em> yonida ega turmaydi, shuning uchun <em>«Мы "
                       "ну́жно»</em> boʻlmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы ___ ждать.</strong> "
                "(до́лжен)</p>",
        "choices": ["до́лжен", "должна́", "должны́", "должно́"],
        "correct": "должны́",
        "explanation": "<p>Koʻplik uchun <strong>должны́</strong>, urgʻu oxirida. "
                       "<em>До́лжен</em> jinsga <strong>va songa</strong> moslashadi, "
                       "chunki uning yonida haqiqiy ega bor — <em>мы</em>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bu yerda ovqatlanish "
                "mumkin.</strong></p>",
        "choices": ["Здесь мо́жно есть.", "Здесь на́до есть.",
                    "Здесь до́лжен есть.", "Здесь нельзя́ есть."],
        "correct": "Здесь мо́жно есть.",
        "explanation": "<p><strong>Мо́жно</strong> — ruxsat. <em>На́до</em> «kerak» "
                       "degani va butunlay boshqa maʼno berardi: «bu yerda ovqatlanish "
                       "kerak».</p>",
    },
    {
        "text": "<p>Bu gapni oʻtgan zamonga oʻtkazing.</p><p><strong>Она́ должна́ "
                "рабо́тать.</strong></p>",
        "choices": ["Она́ должна́ была́ рабо́тать.", "Она́ должна́ бы́ло рабо́тать.",
                    "Ей должна́ была́ рабо́тать.", "Она́ до́лжен был рабо́тать."],
        "correct": "Она́ должна́ была́ рабо́тать.",
        "explanation": "<p>Bu yerda ega bor (<em>она́</em>), shuning uchun <em>быть</em> "
                       "ham unga moslashadi: <strong>должна́ была́</strong>. Shaxssiz "
                       "gapdan farqi shu — u yerda har doim <em>бы́ло</em> boʻlardi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Не на́до спеши́ть. · "
                "Нельзя́ спеши́ть.</strong></p>",
        "choices": ["Shoshish shart emas · shoshish taqiqlangan",
                    "Ikkalasi bir xil", "Shoshish taqiqlangan · shoshish shart emas",
                    "Birinchisi savol"],
        "correct": "Shoshish shart emas · shoshish taqiqlangan",
        "explanation": "<p><strong>Не на́до</strong> = kerak emas (lekin xohlasangiz "
                       "mumkin). <strong>Нельзя́</strong> = mumkin emas (taqiq). Bu "
                       "farqni bilmaslik gapni ancha qattiqroq qilib yuboradi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda ikkalasi ham toʻgʻri?</p>",
        "choices": ["Мне на́до · Я до́лжен", "Я на́до · Мне до́лжен",
                    "Мне на́до · Мне до́лжен", "Я на́до · Я до́лжен"],
        "correct": "Мне на́до · Я до́лжен",
        "explanation": "<p>Ikkita qoida, ikkita shakl: <em>на́до</em> yonida "
                       "<strong>мне</strong> (ega yoʻq), <em>до́лжен</em> yonida "
                       "<strong>я</strong> (haqiqiy ega). Ularni almashtirib "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Rus tilidagi shaxssiz gapda («На́до рабо́тать») ega qayerda?</p>",
        "choices": ["Gap oxirida", "Umuman yoʻq — bu shaxssiz gap",
                    "Infinitiv ega boʻladi", "«На́до» ega boʻladi"],
        "correct": "Umuman yoʻq — bu shaxssiz gap",
        "explanation": "<p>Ega umuman yoʻq va u yetishmayotgandek tuyulmaydi — "
                       "oʻzbekchada ham «Ishlash kerak» degan gap toʻliq. Bunday "
                       "gaplarni <strong>безли́чное предложе́ние</strong> deyiladi.</p>",
    },
    {
        "text": "<p><strong>мне, тебе́, нам</strong> shakllari oʻzbek tilidagi qaysi "
                "kelishikka toʻgʻri keladi?</p>",
        "choices": ["Qaratqich kelishigi (-ning)", "Tushum kelishigi (-ni)",
                    "Joʻnalish kelishigi (-ga)", "Oʻrin kelishigi (-da)"],
        "correct": "Joʻnalish kelishigi (-ga)",
        "explanation": "<p><em>Men<strong>ga</strong> kerak</em> → <strong>мне</strong> "
                       "на́до. <em>Biz<strong>ga</strong> kerak</em> → <strong>нам</strong> "
                       "на́до. Rus tilida bu <strong>да́тельный паде́ж</strong> deb "
                       "ataladi va PR-37 da toʻliq koʻriladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Тебе́ на́до отдыха́ть.", "Здесь мо́жно чита́ть.",
                    "Жасу́р должна́ идти́.", "Им ну́жно ждать."],
        "correct": "Жасу́р должна́ идти́.",
        "explanation": "<p>Toʻgʻrisi — <strong>Жасу́р до́лжен идти́</strong>. Jasur — "
                       "yigit, demak erkak shakli. <em>До́лжен</em> sifat kabi jinsga "
                       "moslashadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Мне не мо́жно кури́ть.", "Мне нельзя́ кури́ть.",
                    "Я нельзя́ кури́ть.", "Мне до́лжен не кури́ть."],
        "correct": "Мне нельзя́ кури́ть.",
        "explanation": "<p><strong>Нельзя́</strong> — bitta soʻz, va u <em>мне</em> "
                       "bilan ishlaydi (shaxssiz qurilish). <em>«Не мо́жно»</em> mavjud "
                       "emas, <em>«Я нельзя́»</em> — ega qoʻyilgan, <em>«Мне "
                       "до́лжен»</em> — ikkita qoida aralashtirilgan.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Мо́жно чай?</strong></p>",
        "choices": ["— Коне́чно, мо́жно.", "— Коне́чно, на́до.",
                    "— Коне́чно, до́лжен.", "— Коне́чно, нельзя́."],
        "correct": "— Коне́чно, мо́жно.",
        "explanation": "<p>Yolgʻiz <em>мо́жно?</em> — ruxsat soʻrashning eng qisqa "
                       "yoʻli, va javob ham shu soʻz bilan beriladi. <em>«Коне́чно, "
                       "нельзя́»</em> — ichki ziddiyat: «albatta, mumkin emas».</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring. Gapirayotgan odam — "
                "<strong>qiz</strong>.</p><p><strong>Men ketishim kerak — kech "
                "boʻldi.</strong></p>",
        "choices": ["Я на́до идти́ — уже́ по́здно.",
                    "Мне на́до идти́ — уже́ по́здно.",
                    "Мне до́лжен идти́ — уже́ по́здно.",
                    "Мне на́до была́ идти́ — уже́ по́здно."],
        "correct": "Мне на́до идти́ — уже́ по́здно.",
        "explanation": "<p><strong>Мне на́до идти́</strong> — rus tilida xayrlashishning "
                       "eng koʻp ishlatiladigan boshlanishi. Eʼtibor bering: gapirayotgan "
                       "odam qiz boʻlsa ham hech narsa oʻzgarmaydi, chunki shaxssiz "
                       "gapda jins koʻrinmaydi. Jins faqat <em>должна́</em> bilan "
                       "aytilganda paydo boʻlardi.</p>",
    },
]


# =====================================================================
# PR-28 — Мне нравится
# =====================================================================

Q_PR28 = [
    # 1–5 tanish
    {
        "text": "<p>Bu gapda ega qaysi soʻz?</p><p><strong>Мне нра́вится э́тот "
                "фильм.</strong></p>",
        "choices": ["мне", "нра́вится", "э́тот фильм", "Ega yoʻq"],
        "correct": "э́тот фильм",
        "explanation": "<p>Ega — <strong>фильм</strong>, chunki u bosh kelishikda "
                       "turibdi va feʼl aynan unga moslashgan. Soʻzma-soʻz: «menga bu "
                       "film yoqadi» — <strong>film</strong> yoqyapti.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ э́ти "
                "кни́ги.</strong></p>",
        "choices": ["нра́вится", "нра́вятся", "нра́влюсь", "нра́вился"],
        "correct": "нра́вятся",
        "explanation": "<p>Ega — <em>кни́ги</em>, koʻplik, demak "
                       "<strong>нра́вятся</strong>. «Мне» ga qaramang — u hech qachon "
                       "feʼlga taʼsir qilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне нра́вится ___.</strong> "
                "(«oʻqish» maʼnosida)</p>",
        "choices": ["чита́ю", "чита́ть", "чита́л", "чита́ет"],
        "correct": "чита́ть",
        "explanation": "<p>Infinitiv — <strong>чита́ть</strong>. Va infinitiv bilan feʼl "
                       "har doim <strong>birlikda</strong> qoladi, hatto bir nechta "
                       "harakat sanalsa ham: <em>Мне нра́вится чита́ть, гуля́ть и "
                       "спать.</em></p>",
    },
    {
        "text": "<p>«Senga yoqadimi?» ruschada qanday boʻladi?</p>",
        "choices": ["Ты нра́вишься?", "Тебе́ нра́вится?",
                    "Тебя́ нра́вится?", "Твой нра́вится?"],
        "correct": "Тебе́ нра́вится?",
        "explanation": "<p><strong>Тебе́ нра́вится?</strong> — bu savol har kuni "
                       "ishlatiladi va javob ham qisqa: <em>Да, нра́вится</em> yoki "
                       "<em>Не о́чень</em>. <em>«Ты нра́вишься»</em> boshqa maʼno "
                       "berardi: «sen (kimgadir) yoqasan».</p>",
    },
    {
        "text": "<p><strong>Мне хо́лодно</strong> qanday tarjima qilinadi?</p>",
        "choices": ["Men sovuqman", "Menga sovuq", "Men sovuqni yoqtiraman", "Sovuq"],
        "correct": "Menga sovuq",
        "explanation": "<p>Bu <em>нра́вится</em> bilan bir xil mantiq: ega yoʻq, holat "
                       "esa senga tegishli. <em>«Я хо́лодно»</em> degan gap rus tilida "
                       "yoʻq, xuddi «men sovuq» degan oʻzbekcha gap gʻalati boʻlgani "
                       "kabi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ей ___ ко́шки.</strong></p>",
        "choices": ["нра́вится", "нра́вятся", "нра́вилась", "нра́вишься"],
        "correct": "нра́вятся",
        "explanation": "<p>Ega — <em>ко́шки</em> (mushuklar), koʻplik, demak "
                       "<strong>нра́вятся</strong>. <em>Ей</em> — «unga (ayol)», u ega "
                       "emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ э́та кни́га.</strong> "
                "(oʻtgan zamon)</p>",
        "choices": ["нра́вился", "нра́вилась", "нра́вилось", "нра́вились"],
        "correct": "нра́вилась",
        "explanation": "<p>Ega — <em>кни́га</em>, ayol jinsida, demak "
                       "<strong>нра́вилась</strong>. Bu gapni yigit ham aytadi: "
                       "qoʻshimcha <strong>kitobga</strong> qaraydi, gapirayotgan "
                       "odamga emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мне ___ э́тот "
                "фильм.</strong> (oʻtgan zamon)</p>",
        "choices": ["нра́вилась", "нра́вились", "нра́вился", "нра́вилось"],
        "correct": "нра́вился",
        "explanation": "<p><em>Фильм</em> — erkak jinsida (undosh bilan tugaydi), demak "
                       "<strong>нра́вился</strong>. Toʻrtta shakl narsaning jinsi va "
                       "soniga qarab tanlanadi: <em>нра́вился / нра́вилась / "
                       "нра́вилось / нра́вились</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ нра́вится "
                "Ташке́нт?</strong> («sizga» maʼnosida)</p>",
        "choices": ["Вы", "Вам", "Ваш", "Вас"],
        "correct": "Вам",
        "explanation": "<p><strong>Вам</strong> = «siz<strong>ga</strong>». PR-27 dagi "
                       "oʻsha yettita shakl bu yerda ham oʻzgarishsiz ishlaydi: "
                       "<em>мне, тебе́, ему́, ей, нам, вам, им</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ра́ньше мне ___ "
                "коме́дии.</strong> (oʻtgan zamon)</p>",
        "choices": ["нра́вился", "нра́вилась", "нра́вились", "нра́вилось"],
        "correct": "нра́вились",
        "explanation": "<p><em>Коме́дии</em> — koʻplik, demak "
                       "<strong>нра́вились</strong>. Oʻtgan zamonda ham feʼl yoqqan "
                       "NARSAGA moslashadi, gapirayotgan odamga emas.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Menga bu yer "
                "yoqadi.</strong></p>",
        "choices": ["Я нра́влюсь здесь.", "Мне нра́вится здесь.",
                    "Мне нра́вятся здесь.", "Меня́ нра́вится здесь."],
        "correct": "Мне нра́вится здесь.",
        "explanation": "<p><strong>Мне нра́вится здесь</strong> — «bu yer menga "
                       "yoqadi». Koʻplik yoʻq, shuning uchun birlik shakli. "
                       "<em>«Я нра́влюсь»</em> butunlay boshqa maʼno berardi: «men "
                       "(kimgadir) yoqaman».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Им нра́вится ___.</strong> "
                "(«oʻynash» maʼnosida)</p>",
        "choices": ["игра́ют", "игра́ть", "игра́ли", "игра́ет"],
        "correct": "игра́ть",
        "explanation": "<p>Infinitiv — <strong>игра́ть</strong>. Yodda tuting: "
                       "<em>нра́виться</em> yonidagi harakat har doim infinitivda "
                       "boʻladi va feʼl birlikda qoladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Мне нра́вится э́тот "
                "фильм. · Я люблю́ э́тот фильм.</strong></p>",
        "choices": ["Birinchisida ega — фильм, ikkinchisida — я",
                    "Ikkalasi bir xil qurilish",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Birinchisida ega — фильм, ikkinchisida — я",
        "explanation": "<p>Grammatik farq: <em>нра́виться</em> da ega — narsa, "
                       "<em>люби́ть</em> da ega — odam (oddiy qurilish, PR-21). Maʼno "
                       "farqi ham bor: <em>нра́вится</em> yengilroq baho, "
                       "<em>люблю́</em> chuqurroq va doimiyroq.</p>",
    },
    {
        "text": "<p>Odam haqida aytilganda bu ikki gap qanday farq qiladi?</p>"
                "<p><strong>Ты мне нра́вишься. · Я тебя́ люблю́.</strong></p>",
        "choices": ["«Sen menga yoqasan» · «Men seni sevaman»",
                    "Ikkalasi ham «seni sevaman»",
                    "«Men seni sevaman» · «sen menga yoqasan»",
                    "Ikkalasi ham «sen menga yoqasan»"],
        "correct": "«Sen menga yoqasan» · «Men seni sevaman»",
        "explanation": "<p>Bu farq amalda juda muhim. <em>Ты мне нра́вишься</em> — "
                       "samimiy, lekin yengil. <em>Я тебя́ люблю́</em> — sevgi izhori. "
                       "Eʼtibor bering, birinchi gapda feʼl <strong>ты</strong> ga "
                       "moslashgan — <em>нра́вишься</em>, chunki ega — sen.</p>",
    },
    {
        "text": "<p>Qaysi gapda feʼl toʻgʻri tanlangan?</p>",
        "choices": ["Мне нра́вятся э́тот фильм.", "Мне нра́вится э́ти фи́льмы.",
                    "Мне нра́вятся э́ти фи́льмы.", "Мне нра́влюсь э́ти фи́льмы."],
        "correct": "Мне нра́вятся э́ти фи́льмы.",
        "explanation": "<p>Feʼl va ega bir xil sonda boʻlishi kerak: "
                       "<em>фи́льмы</em> (koʻplik) + <strong>нра́вятся</strong> "
                       "(koʻplik). Birinchi ikki variantda ular mos kelmayapti.</p>",
    },
    {
        "text": "<p>Nega bu qurilish oʻzbek oʻquvchi uchun oson?</p>",
        "choices": ["Chunki oʻzbekchada ham «menga … yoqadi» deyiladi",
                    "Chunki rus tilida ega yoʻq",
                    "Chunki bu feʼl tuslanmaydi",
                    "Chunki oʻzbekchada bunday qurilish umuman yoʻq"],
        "correct": "Chunki oʻzbekchada ham «menga … yoqadi» deyiladi",
        "explanation": "<p><em>Men<strong>ga</strong> bu film <strong>yoqadi</strong></em> "
                       "— oʻzbekchada ham joʻnalish kelishigi ishlatiladi va feʼl "
                       "yoqayotgan narsaga qaraydi. Ingliz oʻquvchi bu yerda butun "
                       "tushunchani qaytadan quradi, siz esa faqat soʻzlarni "
                       "almashtirasiz.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Мне нра́вится му́зыка.", "Я нра́влюсь э́тот фильм.",
                    "Нам нра́вятся э́ти пе́сни.", "Ему́ нра́вится футбо́л."],
        "correct": "Я нра́влюсь э́тот фильм.",
        "explanation": "<p>Toʻgʻrisi — <strong>Мне нра́вится э́тот фильм</strong>. Bu "
                       "ingliz oʻquvchining klassik xatosi (<em>I like the film</em>), "
                       "lekin oʻzbek oʻquvchi ham shoshib qilib qoʻyadi. Ega — "
                       "<em>фильм</em>, «я» emas.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я хо́лодно.", "Мне хо́лодная.",
                    "Мне хо́лодно.", "Меня́ хо́лодно."],
        "correct": "Мне хо́лодно.",
        "explanation": "<p><strong>Мне хо́лодно</strong> — «menga sovuq». Bu shaxssiz "
                       "qurilish: ega yoʻq, <em>хо́лодно</em> — ravish va u "
                       "oʻzgarmaydi. Xuddi shunday: <em>мне жа́рко, мне интере́сно, "
                       "мне ску́чно</em>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Тебе́ нра́вится э́тот чай?</strong></p>",
        "choices": ["— Да, мне о́чень нра́вится.", "— Да, я о́чень нра́влюсь.",
                    "— Да, тебе́ нра́вится.", "— Да, мне нра́вятся."],
        "correct": "— Да, мне о́чень нра́вится.",
        "explanation": "<p>Javob «я» dan keladi, demak <strong>мне</strong>; ega — "
                       "<em>чай</em>, birlik, demak <strong>нра́вится</strong>. "
                       "Yanada qisqaroq javob ham mumkin: <em>Да, нра́вится</em>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Menga oʻqish va sayr "
                "qilish yoqadi.</strong></p>",
        "choices": ["Мне нра́вятся чита́ть и гуля́ть.",
                    "Мне нра́вится чита́ть и гуля́ть.",
                    "Я нра́влюсь чита́ть и гуля́ть.",
                    "Мне нра́вится чита́ю и гуля́ю."],
        "correct": "Мне нра́вится чита́ть и гуля́ть.",
        "explanation": "<p>Ikkita harakat sanaldi, lekin feʼl baribir "
                       "<strong>birlikda</strong> — infinitiv hech qachon koʻplik "
                       "boʻlmaydi. Va ikkala harakat ham infinitivda qoladi.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-27 Mashq: Нужно, надо, можно, нельзя, должен — kerak va mumkin",
        "description": (
            "Shaxssiz qurilish: мне / тебе́ / ему́ + на́до, ну́жно, мо́жно, нельзя́. "
            "«Не мо́жно» nega yoʻq, «не на́до» va «нельзя́» farqi, va до́лжен ning "
            "jinsga moslashishi."
        ),
        "tutorial": "PR-27:",
        "questions": Q_PR27,
    },
    {
        "title": "PR-28 Mashq: Мне нравится — teskari qurilish va uning mantigʻi",
        "description": (
            "КОМУ + нра́вится + ЧТО. Feʼl narsaga moslashadi (нра́вится ↔ "
            "нра́вятся), oʻtgan zamonda ham; нра́виться va люби́ть farqi; "
            "мне хо́лодно turkumi."
        ),
        "tutorial": "PR-28:",
        "questions": Q_PR28,
    },
]
