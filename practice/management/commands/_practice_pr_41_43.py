# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-41 … PR-43.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_41_43.py --master=prime \\
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
# PR-41 — Olmoshlarning turlanishi
# =====================================================================

Q_PR41 = [
    # 1–5 tanish
    {
        "text": "<p>Olmoshlarda qaysi ikki kelishik har doim bir xil?</p>",
        "choices": ["Р.п. va В.п.", "Д.п. va П.п.",
                    "В.п. va Т.п.", "И.п. va В.п."],
        "correct": "Р.п. va В.п.",
        "explanation": "<p><em>меня́ / меня́</em>, <em>тебя́ / тебя́</em>, <em>его́ / "
                       "его́</em>, <em>нас / нас</em>. Bu jonli otlardagi qoidaning "
                       "oʻsha oʻzi (PR-32) — shuning uchun oltita emas, beshta shakl "
                       "yodlanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У ___ есть "
                "соба́ка.</strong> (она́)</p>",
        "choices": ["её", "ей", "неё", "ней"],
        "correct": "неё",
        "explanation": "<p><em>У</em> — predlog, demak <strong>Н</strong> qoʻshiladi: "
                       "<em>её → неё</em>. Predlogsiz esa <em>её</em> qolardi: "
                       "<em>я ви́жу её</em>.</p>",
    },
    {
        "text": "<p>«Men bilan» ruschada qanday boʻladi?</p>",
        "choices": ["с меня́", "со мной", "с мне", "с мной"],
        "correct": "со мной",
        "explanation": "<p>Твори́тельный shakli <strong>мной</strong>, va predlogga "
                       "unli qoʻshiladi: <strong>со</strong>. Xuddi <em>обо мне</em> "
                       "va <em>ко мне</em> kabi.</p>",
    },
    {
        "text": "<p><strong>Н</strong> qoidasi qaysi olmoshlarga tegishli?</p>",
        "choices": ["Hammasiga", "Faqat он / она́ / они́ ga",
                    "Faqat я va ты ga", "Faqat koʻplikka"],
        "correct": "Faqat он / она́ / они́ ga",
        "explanation": "<p><em>Меня́, тебя́, нас, вас</em> predlogdan keyin ham "
                       "oʻzgarmaydi. Faqat uchinchi shaxs Н oladi: <em>у него́, о "
                       "ней, с ни́ми</em>.</p>",
    },
    {
        "text": "<p>Bu uch shakl bitta olmoshdan. Qaysi olmosh?</p><p><strong>её · "
                "ей · о ней</strong></p>",
        "choices": ["он", "она́", "они́", "оно́"],
        "correct": "она́",
        "explanation": "<p><em>Её</em> — Р.п. va В.п.; <em>ей</em> — Д.п. va Т.п.; "
                       "<em>о ней</em> — П.п. Bu olmoshda ikkita shakl ikki martadan "
                       "ishlatiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю ___.</strong> "
                "(«men haqimda» emas — «u haqida», erkak)</p>",
        "choices": ["о его́", "о нём", "о ему́", "о он"],
        "correct": "о нём",
        "explanation": "<p>Предло́жный shakli <strong>нём</strong> — va u har doim "
                       "predlog bilan keladi, shuning uchun Н doim bor.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы идём ___.</strong> "
                "(«ular bilan» maʼnosida)</p>",
        "choices": ["с и́ми", "с ни́ми", "с их", "с им"],
        "correct": "с ни́ми",
        "explanation": "<p>Твори́тельный shakli <em>и́ми</em>, predlogdan keyin "
                       "<strong>Н</strong> qoʻshiladi: <strong>с ни́ми</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Дай ___ кни́гу.</strong> "
                "(они́)</p>",
        "choices": ["их", "им", "ним", "и́ми"],
        "correct": "им",
        "explanation": "<p>«Kimga bermoq?» — Да́тельный, demak <strong>им</strong>. "
                       "Predlog yoʻq, shuning uchun Н ham yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Он ду́мает ___.</strong> "
                "(«men haqimda» maʼnosida)</p>",
        "choices": ["о мне", "обо мне", "о меня́", "о я"],
        "correct": "обо мне",
        "explanation": "<p><strong>Обо мне</strong> — <em>мне</em> dan oldin "
                       "<em>о</em> predlogi <em>обо</em> boʻladi. Bu uchta holatdan "
                       "biri: <em>обо мне, ко мне, со мной</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я жду ___.</strong> "
                "(он)</p>",
        "choices": ["он", "его́", "него́", "ему́"],
        "correct": "его́",
        "explanation": "<p>Вини́тельный — <strong>его́</strong>. Predlog yoʻq, demak "
                       "Н qoʻshilmaydi. <em>Него́</em> faqat predlog bilan: <em>у "
                       "него́</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ пришла́ ___.</strong> "
                "(«uning oldiga», ayol)</p>",
        "choices": ["к её", "к ней", "к ей", "к неё"],
        "correct": "к ней",
        "explanation": "<p><em>К</em> Да́тельный oladi (PR-38), shakl <em>ей</em>, va "
                       "predlogdan keyin Н: <strong>к ней</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ хо́лодно.</strong> "
                "(мы)</p>",
        "choices": ["Мы", "Нас", "Нам", "На́ми"],
        "correct": "Нам",
        "explanation": "<p>Shaxssiz gapda olmosh Да́тельный'da (PR-38): "
                       "<strong>нам хо́лодно</strong>. Ega boʻlmaydi, shuning uchun "
                       "<em>мы</em> ishlatilmaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapning farqi nima?</p><p><strong>Его́ нет до́ма. · У "
                "него́ есть дом.</strong></p>",
        "choices": ["Birinchisida predlog yoʻq, ikkinchisida bor — shuning uchun Н",
                    "Ikkalasi bir xil",
                    "Birinchisi oʻtgan zamon",
                    "Ikkinchisi xato"],
        "correct": "Birinchisida predlog yoʻq, ikkinchisida bor — shuning uchun Н",
        "explanation": "<p>Bitta olmosh, ikkita shakl. Qoida oddiy: <strong>predlog "
                       "bor — Н bor; predlog yoʻq — Н yoʻq</strong>.</p>",
    },
    {
        "text": "<p>Qaysi olmosh eng kam shaklga ega?</p>",
        "choices": ["я", "она́", "мы", "он"],
        "correct": "мы",
        "explanation": "<p><em>Мы, нас, нам, нас, на́ми, о нас</em> — atigi "
                       "<strong>toʻrtta</strong> boshqa shakl, va Р.п. bilan В.п. bir "
                       "xil. <em>Вы</em> ham xuddi shunday.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida olmoshlar turlanadimi?</p>",
        "choices": ["Yoʻq, hech qachon",
                    "Ha — men, mening, menga, meni, menda, mendan",
                    "Faqat koʻplikda",
                    "Faqat egalik maʼnosida"],
        "correct": "Ha — men, mening, menga, meni, menda, mendan",
        "explanation": "<p>Oltita shakl — oltita shakl. Tushuncha bir xil. Farq "
                       "shundaki, oʻzbekchada oʻzak turadi va faqat qoʻshimcha "
                       "almashadi; ruschada esa shakllar bir-biriga oʻxshamaydi "
                       "(<em>я → меня́ → мне → мной</em>).</p>",
    },
    {
        "text": "<p>Nega bu darsda yangi shakl yoʻq deyiladi?</p>",
        "choices": ["Chunki oʻquvchi ularning hammasini oldingi darslarda uchratgan",
                    "Chunki olmoshlar turlanmaydi",
                    "Chunki ular faqat yozuvda ishlatiladi",
                    "Chunki ular oʻzbekcha bilan bir xil"],
        "correct": "Chunki oʻquvchi ularning hammasini oldingi darslarda uchratgan",
        "explanation": "<p><em>Меня́</em> PR-32 da, <em>мне</em> PR-27 da, <em>обо "
                       "мне</em> PR-31 da, <em>мной</em> PR-39 da, <em>у меня́</em> "
                       "PR-14 da. Bu dars ularni bitta jadvalga yigʻadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я ду́маю о нём.", "У его́ есть маши́на.",
                    "Дай им кни́гу.", "Пойдём со мной."],
        "correct": "У его́ есть маши́на.",
        "explanation": "<p>Toʻgʻrisi — <strong>У него́ есть маши́на</strong>. "
                       "Predlogdan keyin uchinchi shaxs olmoshi Н oladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я ви́жу него́.", "Я ви́жу его́.",
                    "Я ви́жу ему́.", "Я ви́жу он."],
        "correct": "Я ви́жу его́.",
        "explanation": "<p>Вини́тельный — <em>его́</em>, va predlog yoʻq, demak Н "
                       "ham yoʻq. <em>Него́</em> faqat predlogdan keyin "
                       "ishlatiladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ты зна́ешь Афсо́ну?</strong></p>",
        "choices": ["— Да, я ча́сто говорю́ с ней.", "— Да, я ча́сто говорю́ с ей.",
                    "— Да, я ча́сто говорю́ с её.", "— Да, я ча́сто говорю́ с она́."],
        "correct": "— Да, я ча́сто говорю́ с ней.",
        "explanation": "<p><em>С</em> Твори́тельный oladi, shakl <em>ей</em>, va "
                       "predlogdan keyin Н: <strong>с ней</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>U menga qoʻngʻiroq "
                "qilmadi, men esa u haqida oʻyladim.</strong></p>",
        "choices": ["Она́ не звони́ла меня́, а я ду́мал о ней.",
                    "Она́ не звони́ла мне, а я ду́мал о ней.",
                    "Она́ не звони́ла мне, а я ду́мал о её.",
                    "Она́ не звони́ла мне, а я ду́мал об ней."],
        "correct": "Она́ не звони́ла мне, а я ду́мал о ней.",
        "explanation": "<p><em>Звони́ть</em> Да́тельный oladi (PR-37) → "
                       "<strong>мне</strong>. <em>Ду́мать о</em> Предло́жный oladi "
                       "(PR-31) → <strong>о ней</strong>, predlogdan keyin Н "
                       "bilan.</p>",
    },
]


# =====================================================================
# PR-42 — Egalik olmoshlarining turlanishi
# =====================================================================

Q_PR42 = [
    # 1–5 tanish
    {
        "text": "<p>Qaysi egalik olmoshlari <strong>umuman turlanmaydi</strong>?</p>",
        "choices": ["мой, твой", "наш, ваш", "его́, её, их", "Hammasi turlanadi"],
        "correct": "его́, её, их",
        "explanation": "<p><em>Его́ дом, в его́ до́ме, с его́ бра́том</em> — har doim "
                       "bir xil. Va ular predlogdan keyin <strong>Н ham "
                       "olmaydi</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то дом ___ "
                "бра́та.</strong> (мой)</p>",
        "choices": ["мой", "моего́", "моему́", "мои́м"],
        "correct": "моего́",
        "explanation": "<p><em>Бра́та</em> — Роди́тельный, demak egalik olmoshi ham "
                       "Роди́тельный'da: <strong>моего́</strong>. Ikkala soʻz birga "
                       "oʻzgaradi.</p>",
    },
    {
        "text": "<p><strong>моего́</strong> qanday oʻqiladi?</p>",
        "choices": ["[маего́]", "[маиво́]", "[моего́]", "[майго́]"],
        "correct": "[маиво́]",
        "explanation": "<p><strong>-ОГО</strong> har doim <strong>[ово]</strong> "
                       "boʻlib oʻqiladi — <em>его́</em> [йиво́] dagi qoidaning oʻsha "
                       "oʻzi (PR-32).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>В ___ дворе́ игра́ют "
                "де́ти.</strong> (наш)</p>",
        "choices": ["наш", "на́шего", "на́шем", "на́шим"],
        "correct": "на́шем",
        "explanation": "<p><em>Во дворе́</em> — Предло́жный, demak egalik olmoshi ham: "
                       "<strong>на́шем</strong>.</p>",
    },
    {
        "text": "<p>Ayol jinsidagi <strong>моя́</strong> nechta kelishikda "
                "<strong>мое́й</strong> boʻladi?</p>",
        "choices": ["Bitta", "Ikkita", "Toʻrtta", "Oltita"],
        "correct": "Toʻrtta",
        "explanation": "<p>Роди́тельный, Да́тельный, Твори́тельный va Предло́жный — "
                       "toʻrttasida ham <strong>мое́й</strong>. Faqat <em>моя́</em> "
                       "(И.п.) va <em>мою́</em> (В.п.) boshqacha.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я был в ___ "
                "до́ме.</strong> (его́)</p>",
        "choices": ["его́", "него́", "ему́", "им"],
        "correct": "его́",
        "explanation": "<p><strong>Его́</strong> — oʻzgarmaydi, va egalik maʼnosida "
                       "predlogdan keyin Н ham qoʻshilmaydi. Faqat ot oʻzgardi: "
                       "<em>до́м<strong>е</strong></em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то кни́га ___ "
                "сестры́.</strong> (моя́)</p>",
        "choices": ["моя́", "мою́", "мое́й", "мои́х"],
        "correct": "мое́й",
        "explanation": "<p><em>Сестры́</em> — Роди́тельный, ayol jinsi, demak "
                       "<strong>мое́й</strong>. Bu shakl toʻrtta kelishikda "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я говорю́ с ___ "
                "дру́гом.</strong> (мой)</p>",
        "choices": ["моего́", "моему́", "мои́м", "моём"],
        "correct": "мои́м",
        "explanation": "<p><em>С дру́гом</em> — Твори́тельный (PR-39), demak egalik "
                       "olmoshi ham: <strong>мои́м</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю о ___ "
                "бра́те.</strong> (мой)</p>",
        "choices": ["моего́", "моём", "мои́м", "мое́й"],
        "correct": "моём",
        "explanation": "<p><em>О бра́те</em> — Предло́жный, erkak jins, demak "
                       "<strong>о моём</strong>. Erkak va oʻrta jins bu yerda bir "
                       "xil.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___ "
                "дом.</strong> (его́)</p>",
        "choices": ["его́", "него́", "ему́", "их"],
        "correct": "его́",
        "explanation": "<p><strong>Его́</strong> oʻzgarmaydi, va <em>дом</em> jonsiz "
                       "boʻlgani uchun u ham oʻzgarmaydi. Butun ibora bosh kelishik "
                       "bilan bir xil koʻrinadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Му́зыка ___ "
                "двора́.</strong> (наш)</p>",
        "choices": ["наш", "на́шего", "на́шем", "на́шим"],
        "correct": "на́шего",
        "explanation": "<p><em>Двора́</em> — Роди́тельный (egalik, PR-34), demak "
                       "<strong>на́шего</strong>. Egasi orqada turibdi: «hovlimizning "
                       "musiqasi».</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́ю ___ "
                "кни́гу.</strong> (твоя́)</p>",
        "choices": ["твоя́", "твою́", "твое́й", "твои́х"],
        "correct": "твою́",
        "explanation": "<p><em>Кни́гу</em> — Вини́тельный, ayol jinsi, demak "
                       "<strong>твою́</strong>. <em>Твой</em> aynan <em>мой</em> kabi "
                       "turlanadi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapda <strong>его́</strong> nima farq qiladi?</p>"
                "<p><strong>У него́ есть дом. · Я был в его́ до́ме.</strong></p>",
        "choices": ["Birinchisi olmosh («u»), ikkinchisi egalik («uning»)",
                    "Ikkalasi bir xil",
                    "Birinchisi xato",
                    "Ikkinchisi koʻplik"],
        "correct": "Birinchisi olmosh («u»), ikkinchisi egalik («uning»)",
        "explanation": "<p>Olmosh predlogdan keyin <strong>Н</strong> oladi — "
                       "<em>него́</em>. Egalik esa hech qachon oʻzgarmaydi — "
                       "<em>его́</em>. Bu farqni ajratish muhim.</p>",
    },
    {
        "text": "<p>Egalik olmoshlari qanday turlanadi?</p>",
        "choices": ["Ot kabi", "Sifat kabi", "Feʼl kabi", "Turlanmaydi"],
        "correct": "Sifat kabi",
        "explanation": "<p><em>Моего́, моему́, мои́м, о моём</em> — bu sifat "
                       "qoʻshimchalari. Shuning uchun bu dars keyingi dars (PR-43, "
                       "sifatlar) uchun tayyorgarlik ham.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida egalik qanday koʻrsatiladi?</p>",
        "choices": ["Alohida soʻz bilan", "Otga qoʻshimcha bilan: kitobim, kitobing",
                    "Feʼl bilan", "Koʻrsatilmaydi"],
        "correct": "Otga qoʻshimcha bilan: kitobim, kitobing",
        "explanation": "<p>Oʻzbekchada bitta soʻz va ikkita qoʻshimcha: "
                       "<em>kitob-im-<strong>ni</strong></em>. Ruschada esa ikkita "
                       "alohida soʻz va ikkalasi ham oʻzgaradi: <em>мою́ "
                       "кни́гу</em>.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["моего́ бра́та · в на́шем дворе́ · в его́ до́ме",
                    "мой бра́та · в на́шем дворе́ · в его́ до́ме",
                    "моего́ бра́та · в наш дворе́ · в его́ до́ме",
                    "моего́ бра́та · в на́шем дворе́ · в него́ до́ме"],
        "correct": "моего́ бра́та · в на́шем дворе́ · в его́ до́ме",
        "explanation": "<p>Uchta qoida: <em>мой</em> otga ergashadi, <em>наш</em> ham "
                       "ergashadi, <em>его́</em> esa hech qachon oʻzgarmaydi va Н "
                       "olmaydi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Э́то дом моего́ бра́та.", "В на́шем дворе́ ти́хо.",
                    "Я был в него́ до́ме.", "Я говорю́ с мои́м дру́гом."],
        "correct": "Я был в него́ до́ме.",
        "explanation": "<p>Toʻgʻrisi — <strong>в его́ до́ме</strong>. Bu yerda "
                       "<em>его́</em> egalik («uning»), demak Н qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я ду́маю о мой брат.", "Я ду́маю о моём бра́те.",
                    "Я ду́маю о моего́ бра́та.", "Я ду́маю о мои́м бра́том."],
        "correct": "Я ду́маю о моём бра́те.",
        "explanation": "<p><em>Ду́мать о</em> Предло́жный oladi, demak ikkala soʻz "
                       "ham shu kelishikda: <strong>о моём бра́те</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Чья э́то кни́га?</strong></p>",
        "choices": ["— Мое́й сестры́.", "— Моя́ сестры́.",
                    "— Мою́ сестру́.", "— Мои́м сестра́м."],
        "correct": "— Мое́й сестры́.",
        "explanation": "<p>Egalik — Роди́тельный (PR-34), ayol jinsi, demak "
                       "<strong>мое́й сестры́</strong>. Ikkala soʻz ham "
                       "oʻzgargan.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Bizning hovlimizda "
                "uning iti yashaydi.</strong></p>",
        "choices": ["В наш дворе́ живёт его́ соба́ка.",
                    "В на́шем дворе́ живёт его́ соба́ка.",
                    "В на́шем дворе́ живёт него́ соба́ка.",
                    "В на́шего дворе́ живёт его́ соба́ка."],
        "correct": "В на́шем дворе́ живёт его́ соба́ка.",
        "explanation": "<p>Ikkita qoida bir gapda: <em>наш</em> ot bilan birga "
                       "oʻzgaradi (<strong>на́шем дворе́</strong>), <em>его́</em> esa "
                       "hech qachon oʻzgarmaydi va Н olmaydi.</p>",
    },
]


# =====================================================================
# PR-43 — Sifatlarning turlanishi 1
# =====================================================================

Q_PR43 = [
    # 1–5 tanish
    {
        "text": "<p>Sifat Роди́тельный'da erkak jinsida qanday tugaydi?</p>",
        "choices": ["-ый", "-ого", "-ому", "-ым"],
        "correct": "-ого",
        "explanation": "<p><em>но́вый дом → но́в<strong>ого</strong> до́ма</em>. Oʻrta "
                       "jins ham xuddi shunday. Ayol jinsi esa <strong>-ой</strong> "
                       "oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́ю ___ "
                "кни́гу.</strong> (но́вая)</p>",
        "choices": ["но́вая", "но́вой", "но́вую", "но́вые"],
        "correct": "но́вую",
        "explanation": "<p>Вини́тельный, ayol jinsi → <strong>-ую</strong>. Bu bugungi "
                       "darsdagi yagona haqiqiy yangi qoʻshimcha.</p>",
    },
    {
        "text": "<p><strong>но́вого</strong> qanday oʻqiladi?</p>",
        "choices": ["[но́вого]", "[но́вава]", "[навого́]", "[но́вога]"],
        "correct": "[но́вава]",
        "explanation": "<p><strong>-ОГО</strong> har doim <strong>[ово]</strong> "
                       "boʻlib oʻqiladi — <em>его́</em> [йиво́] va <em>моего́</em> "
                       "[маиво́] dagi qoida.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___ "
                "дом.</strong> (но́вый)</p>",
        "choices": ["но́вый", "но́вого", "но́вому", "но́вым"],
        "correct": "но́вый",
        "explanation": "<p>Uy — <strong>jonsiz</strong>, demak Вини́тельный bosh "
                       "kelishik bilan bir xil qoladi: sifat ham, ot ham "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___ "
                "учи́теля.</strong> (но́вый)</p>",
        "choices": ["но́вый", "но́вого", "но́вому", "но́вую"],
        "correct": "но́вого",
        "explanation": "<p>Oʻqituvchi — <strong>jonli</strong>, demak Вини́тельный "
                       "Роди́тельный shaklini oladi. Jonlilik sifatga ham "
                       "tegadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Э́то дом ___ "
                "сосе́да.</strong> (ста́рый)</p>",
        "choices": ["ста́рый", "ста́рого", "ста́рому", "ста́рым"],
        "correct": "ста́рого",
        "explanation": "<p>Egalik — Роди́тельный (PR-34), demak sifat "
                       "<strong>-ого</strong> oladi va ot <strong>-а</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У ___ доро́ги нет "
                "и́мени.</strong> (но́вая)</p>",
        "choices": ["но́вая", "но́вую", "но́вой", "но́вых"],
        "correct": "но́вой",
        "explanation": "<p><em>У</em> Роди́тельный oladi (PR-35), ayol jinsi sifat "
                       "esa <strong>-ой</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь нет ___ "
                "домо́в.</strong> (но́вые)</p>",
        "choices": ["но́вые", "но́вых", "но́вым", "но́вой"],
        "correct": "но́вых",
        "explanation": "<p>Koʻplik Роди́тельный'da sifat <strong>-ых / -их</strong> "
                       "oladi. Koʻplikda jins yoʻqoladi — bitta shakl.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У ___ книг "
                "интере́сные назва́ния.</strong> (ру́сские)</p>",
        "choices": ["ру́сскых", "ру́сских", "ру́сские", "ру́сской"],
        "correct": "ру́сских",
        "explanation": "<p>Imlo qoidasi (PR-4): <strong>К</strong> dan keyin Ы "
                       "yozilmaydi, uning oʻrniga <strong>И</strong>. Shuning uchun "
                       "<em>ру́сских</em>, <em>«ру́сскых»</em> emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я чита́ю ___ "
                "журна́л.</strong> (ста́рый)</p>",
        "choices": ["ста́рый", "ста́рого", "ста́рую", "ста́рым"],
        "correct": "ста́рый",
        "explanation": "<p>Jurnal jonsiz, demak Вини́тельный oʻzgarmaydi. Sifat ham, "
                       "ot ham bosh kelishik shaklida qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ моста́ бо́льше "
                "нет.</strong> (ста́рый)</p>",
        "choices": ["Ста́рый", "Ста́рого", "Ста́рому", "Ста́рым"],
        "correct": "Ста́рого",
        "explanation": "<p><em>Нет</em> dan keyin Роди́тельный (PR-34) — va sifat "
                       "ham unga ergashadi: <strong>ста́рого моста́</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я жду ___ "
                "сестру́.</strong> (ста́ршая)</p>",
        "choices": ["ста́ршая", "ста́ршую", "ста́ршей", "ста́рших"],
        "correct": "ста́ршую",
        "explanation": "<p>Ayol jinsi Вини́тельный'da har doim <strong>-ую</strong> "
                       "oladi — jonli boʻlsa ham, jonsiz boʻlsa ham. Jonlilik faqat "
                       "erkak jinsida ishlaydi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Sifat Вини́тельный'da nechta yangi shakl yaratadi?</p>",
        "choices": ["Bittasi: ayol jinsidagi -УЮ", "Toʻrttasi",
                    "Oltitasi", "Hech qanday"],
        "correct": "Bittasi: ayol jinsidagi -УЮ",
        "explanation": "<p>Qolgan hamma holatda Вини́тельный yo bosh kelishikni, yo "
                       "Роди́тельный'ni takrorlaydi — jonlilikka qarab. Yagona yangi "
                       "qoʻshimcha — <strong>-ую</strong>.</p>",
    },
    {
        "text": "<p>Bu ikki gapda nega sifat har xil?</p><p><strong>Я ви́жу но́вый "
                "дом. · Я ви́жу но́вого учи́теля.</strong></p>",
        "choices": ["Jonlilik farqi: дом jonsiz, учи́тель jonli",
                    "Bu ikki xil kelishik",
                    "Chunki «учи́тель» uzunroq",
                    "Bu gaplardan biri xato"],
        "correct": "Jonlilik farqi: дом jonsiz, учи́тель jonli",
        "explanation": "<p>Ikkalasi ham Вини́тельный va ikkalasi ham erkak jinsida. "
                       "PR-32 dagi jonlilik qoidasi endi <strong>sifatga ham</strong> "
                       "qoʻllanadi.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida sifat oʻzgaradimi?</p>",
        "choices": ["Ha, kelishikka qarab", "Ha, jinsga qarab",
                    "Yoʻq, hech qachon", "Faqat koʻplikda"],
        "correct": "Yoʻq, hech qachon",
        "explanation": "<p><em>yangi kitob, yangi kitobni, yangi kitobda, yangi "
                       "kitoblar</em> — bitta shakl. Ruschada esa sifat jins, son va "
                       "kelishik boʻyicha moslashadi. Bu sof qoʻshimcha ish — lekin "
                       "istisnosiz.</p>",
    },
    {
        "text": "<p>Sifatning kelishigini nima belgilaydi?</p>",
        "choices": ["Ot — sifat unga ergashadi", "Feʼl",
                    "Gapdagi oʻrni", "Sifatning oʻzi"],
        "correct": "Ot — sifat unga ergashadi",
        "explanation": "<p>Sifat oʻz qaroriga ega emas. Otning kelishigini bilsangiz, "
                       "sifatniki oʻz-oʻzidan chiqadi. Shuning uchun bu darsni "
                       "yodlash emas, <strong>mashq qilish</strong> kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я чита́ю но́вую кни́гу.", "Э́то дом ста́рого сосе́да.",
                    "Я ви́жу но́вого до́ма.", "У ру́сских книг."],
        "correct": "Я ви́жу но́вого до́ма.",
        "explanation": "<p>Toʻgʻrisi — <strong>Я ви́жу но́вый дом</strong>. Uy "
                       "jonsiz, demak Вини́тельный bosh kelishik bilan bir xil "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я чита́ю но́вая кни́гу.", "Я чита́ю но́вой кни́гу.",
                    "Я чита́ю но́вую кни́гу.", "Я чита́ю но́вую кни́га."],
        "correct": "Я чита́ю но́вую кни́гу.",
        "explanation": "<p>Ikkala soʻz ham Вини́тельный'da boʻlishi kerak: sifat "
                       "<strong>-ую</strong>, ot <strong>-у</strong>. Ular birga "
                       "oʻzgaradi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Чей э́то дом?</strong></p>",
        "choices": ["— Ста́рого сосе́да.", "— Ста́рый сосе́д.",
                    "— Ста́рому сосе́ду.", "— Ста́рым сосе́дом."],
        "correct": "— Ста́рого сосе́да.",
        "explanation": "<p>Savol <em>чей?</em> — egalik, demak Роди́тельный. Sifat "
                       "<strong>-ого</strong>, ot <strong>-а</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Yangi oʻqituvchini va "
                "yangi maktabni koʻryapman.</strong></p>",
        "choices": ["Я ви́жу но́вый учи́тель и но́вая шко́ла.",
                    "Я ви́жу но́вого учи́теля и но́вую шко́лу.",
                    "Я ви́жу но́вого учи́теля и но́вая шко́ла.",
                    "Я ви́жу но́вый учи́теля и но́вую шко́лу."],
        "correct": "Я ви́жу но́вого учи́теля и но́вую шко́лу.",
        "explanation": "<p>Ikkita boshqa qoida bir gapda: oʻqituvchi jonli erkak → "
                       "<strong>но́вого учи́теля</strong>; maktab ayol jinsi → "
                       "<strong>но́вую шко́лу</strong>.</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-41 Mashq: Olmoshlarning turlanishi: меня, мне, мной, обо мне",
        "description": (
            "Butun olmosh jadvali bir joyda: Р.п. = В.п., predlogdan keyingi Н "
            "qoidasi va обо мне / ко мне / со мной uchligi."
        ),
        "tutorial": "PR-41:",
        "questions": Q_PR41,
    },
    {
        "title": "PR-42 Mashq: Egalik olmoshlarining turlanishi: моего, моей, моим, о моём",
        "description": (
            "Мой, твой, наш, ваш sifat kabi turlanadi — его́, её, их esa hech "
            "qachon oʻzgarmaydi. Va -ОГО ning [ово] talaffuzi."
        ),
        "tutorial": "PR-42:",
        "questions": Q_PR42,
    },
    {
        "title": "PR-43 Mashq: Sifatlarning turlanishi 1 — Родительный va Винительный",
        "description": (
            "Sifat otga ergashadi: -ОГО / -ОЙ / -ЫХ, va Вини́тельный'dagi yagona "
            "yangi shakl -УЮ. Jonlilik sifatga ham tegadi."
        ),
        "tutorial": "PR-43:",
        "questions": Q_PR43,
    },
]
