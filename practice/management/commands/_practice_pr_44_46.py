# -*- coding: utf-8 -*-
"""Prime Russian mashqlar — PR-44 … PR-46.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PR_PRACTICE.md · lesson list in toc_pr_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pr_44_46.py --master=prime \\
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
# PR-44 — Sifatlarning turlanishi 2
# =====================================================================

Q_PR44 = [
    # 1–5 tanish
    {
        "text": "<p>Sifat Предло́жный'da erkak jinsida qanday tugaydi?</p>",
        "choices": ["-ому", "-ым", "-ом", "-ого"],
        "correct": "-ом",
        "explanation": "<p><em>в но́в<strong>ом</strong> до́ме</em>, <em>о "
                       "ста́р<strong>ом</strong> го́роде</em>. Tekshiruv: <em>о "
                       "как<strong>о́м</strong>? — о но́в<strong>ом</strong></em>.</p>",
    },
    {
        "text": "<p>Ayol jinsidagi sifat nechta kelishikda <strong>-ОЙ</strong> "
                "boʻladi?</p>",
        "choices": ["Bitta", "Ikkita", "Toʻrtta", "Oltita"],
        "correct": "Toʻrtta",
        "explanation": "<p>Роди́тельный, Да́тельный, Твори́тельный, Предло́жный — "
                       "hammasida <strong>но́вой</strong>. Boshqacha shakl faqat "
                       "<em>но́вая</em> (И.п.) va <em>но́вую</em> (В.п.).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я живу́ в ___ "
                "го́роде.</strong> (большо́й)</p>",
        "choices": ["большо́й", "большо́го", "большо́му", "большо́м"],
        "correct": "большо́м",
        "explanation": "<p>Предло́жный, erkak jins → <strong>-ом</strong>. "
                       "<em>Большо́й</em> — urgʻusi oxirda boʻlgan tur, lekin naqsh "
                       "oʻsha.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ к ___ "
                "до́му.</strong> (но́вый)</p>",
        "choices": ["но́вого", "но́вому", "но́вым", "но́вом"],
        "correct": "но́вому",
        "explanation": "<p><em>К</em> Да́тельный oladi (PR-38), erkak jins sifat esa "
                       "<strong>-ому</strong>. Tekshiruv: <em>к "
                       "как<strong>о́му</strong>?</em></p>",
    },
    {
        "text": "<p>Sifatning kelishigini eslash uchun qanday hiyla bor?</p>",
        "choices": ["Savol soʻzining oxiri sifatning oxiri bilan bir xil",
                    "Sifat har doim -ый bilan tugaydi",
                    "Sifat otdan oldin turadi",
                    "Hiyla yoʻq, faqat yodlash"],
        "correct": "Savol soʻzining oxiri sifatning oxiri bilan bir xil",
        "explanation": "<p><em>как<strong>о́му</strong>? → но́в<strong>ому</strong></em>, "
                       "<em>как<strong>и́м</strong>? → но́в<strong>ым</strong></em>, "
                       "<em>о как<strong>о́м</strong>? → о но́в<strong>ом</strong></em>. "
                       "Shaklni unutsangiz, savolni ayting.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я иду́ по ___ "
                "у́лице.</strong> (широ́кая)</p>",
        "choices": ["широ́кая", "широ́кую", "широ́кой", "широ́ким"],
        "correct": "широ́кой",
        "explanation": "<p><em>По</em> Да́тельный oladi, ayol jinsi esa "
                       "<strong>-ой</strong> — bu shakl toʻrtta kelishikda "
                       "ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я говорю́ с ___ "
                "дру́гом.</strong> (ста́рый)</p>",
        "choices": ["ста́рого", "ста́рому", "ста́рым", "ста́ром"],
        "correct": "ста́рым",
        "explanation": "<p>Твори́тельный, erkak jins → <strong>-ым</strong>. "
                       "Tekshiruv: <em>с как<strong>и́м</strong>?</em></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы в ___ "
                "кафе́.</strong> (ма́ленькое)</p>",
        "choices": ["ма́ленькое", "ма́ленького", "ма́ленькому", "ма́леньком"],
        "correct": "ма́леньком",
        "explanation": "<p>Предло́жный, oʻrta jins → <strong>-ом</strong>, erkak jins "
                       "bilan bir xil. <em>Кафе́</em> oʻzi turlanmaydi, lekin sifat "
                       "turlanadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю о ___ "
                "шко́ле.</strong> (ста́рая)</p>",
        "choices": ["ста́рая", "ста́рую", "ста́рой", "ста́рым"],
        "correct": "ста́рой",
        "explanation": "<p>Предло́жный, ayol jinsi → <strong>-ой</strong>. Oʻsha "
                       "toʻrtta kelishikdagi bitta shakl.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Мы в ___ "
                "до́ме.</strong> (большо́й)</p>",
        "choices": ["большы́м", "большо́м", "больши́м", "большо́го"],
        "correct": "большо́м",
        "explanation": "<p>Предло́жный → <strong>-ом</strong>. <em>Больши́м</em> "
                       "Твори́тельный boʻlardi, <em>«большы́м»</em> esa umuman mavjud "
                       "emas — Ш dan keyin Ы yozilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я пишу́ ___ "
                "друзья́м.</strong> (ста́рые)</p>",
        "choices": ["ста́рые", "ста́рых", "ста́рым", "ста́рыми"],
        "correct": "ста́рым",
        "explanation": "<p>Koʻplik Да́тельный → sifat <strong>-ым</strong>. Koʻplikda "
                       "jins umuman ishlamaydi.</p>",
    },
    {
        "text": "<p><strong>больши́м</strong> nega <em>«большы́м»</em> emas?</p>",
        "choices": ["Ш dan keyin Ы yozilmaydi", "Chunki bu koʻplik",
                    "Chunki urgʻu oxirda", "Chunki bu ayol jinsi"],
        "correct": "Ш dan keyin Ы yozilmaydi",
        "explanation": "<p>PR-4 dagi imlo qoidasi: Г, К, Х, Ж, Ш, Щ, Ч dan keyin "
                       "<strong>И</strong> yoziladi. Xuddi shunday <em>ру́сским, "
                       "хоро́шим, ма́леньким</em>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki shaklning farqi nima?</p><p><strong>но́вому · "
                "но́вым</strong></p>",
        "choices": ["Да́тельный · Твори́тельный", "Твори́тельный · Да́тельный",
                    "Ikkalasi bir xil", "Роди́тельный · Да́тельный"],
        "correct": "Да́тельный · Твори́тельный",
        "explanation": "<p><em>К но́в<strong>ому</strong> до́му</em> (kimga/nimaga) va "
                       "<em>с но́в<strong>ым</strong> дру́гом</em> (kim bilan). Savol "
                       "soʻzi farqni koʻrsatadi: <em>како́му?</em> va "
                       "<em>каки́м?</em></p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi ayol jinsida?</p>",
        "choices": ["но́вой шко́ле · широ́кой у́лице · ста́рой кни́ге",
                    "но́вом до́ме · широ́кой у́лице · ста́рой кни́ге",
                    "но́вой шко́ле · широ́ким у́лицам · ста́рой кни́ге",
                    "но́вому до́му · широ́кой у́лице · ста́рой кни́ге"],
        "correct": "но́вой шко́ле · широ́кой у́лице · ста́рой кни́ге",
        "explanation": "<p>Uchtasi ham <strong>-ой</strong> bilan — ayol jinsidagi "
                       "sifat toʻrtta kelishikda shu shaklda turadi.</p>",
    },
    {
        "text": "<p>Koʻplikda sifat jinsga qaraydimi?</p>",
        "choices": ["Ha, uchta jins uchun uchta shakl", "Yoʻq — bitta shakl",
                    "Faqat Роди́тельный'da", "Faqat jonli otlarda"],
        "correct": "Yoʻq — bitta shakl",
        "explanation": "<p><em>но́вым, но́выми, но́вых</em> — erkak, ayol va oʻrta "
                       "uchun bir xil. Koʻplikda jins yoʻqoladi, va bu keyingi darsda "
                       "otlarda ham shunday boʻladi.</p>",
    },
    {
        "text": "<p>Nega ruscha maʼlumotni ikki marta aytadi (sifat + ot)?</p>",
        "choices": ["Bu ortiqcha, maʼnosi yoʻq",
                    "Shuning uchun soʻz tartibi erkin boʻla oladi",
                    "Chunki sifat otdan uzoq turadi",
                    "Bu faqat yozuvda shunday"],
        "correct": "Shuning uchun soʻz tartibi erkin boʻla oladi",
        "explanation": "<p>Oʻzbekchada sifat har doim otdan oldin turadi — bogʻlanishni "
                       "<strong>tartib</strong> koʻrsatadi. Ruschada esa buni "
                       "<strong>qoʻshimcha</strong> koʻrsatadi, shuning uchun soʻzlar "
                       "gapda erkin joylashadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я живу́ в большо́м до́ме.", "Я иду́ к но́вому учи́телю.",
                    "Я говорю́ с молодо́й води́телем.", "Я ду́маю о ста́рой шко́ле."],
        "correct": "Я говорю́ с молодо́й води́телем.",
        "explanation": "<p>Toʻgʻrisi — <strong>с молоды́м води́телем</strong>. "
                       "<em>Води́тель</em> erkak jinsida, shuning uchun sifat ham "
                       "erkak jinsida boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я иду́ по широ́кому у́лице.", "Я иду́ по широ́кой у́лице.",
                    "Я иду́ по широ́кая у́лице.", "Я иду́ по широ́ких у́лице."],
        "correct": "Я иду́ по широ́кой у́лице.",
        "explanation": "<p><em>У́лица</em> — ayol jinsida, demak sifat "
                       "<strong>-ой</strong>. <em>Широ́кому</em> erkak jins "
                       "boʻlardi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Где ты живёшь?</strong></p>",
        "choices": ["— В большо́м го́роде.", "— В большо́й го́роде.",
                    "— В большо́го го́рода.", "— В большо́му го́роду."],
        "correct": "— В большо́м го́роде.",
        "explanation": "<p>Savol <em>где?</em> — Предло́жный, erkak jins: sifat "
                       "<strong>-ом</strong>, ot <strong>-е</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Yosh haydovchi bilan "
                "eski shahar haqida gaplashyapman.</strong></p>",
        "choices": ["Я говорю́ с молодо́м води́телем о ста́ром го́роде.",
                    "Я говорю́ с молоды́м води́телем о ста́ром го́роде.",
                    "Я говорю́ с молоды́м води́телем о ста́рым го́роде.",
                    "Я говорю́ с молодо́й води́телем о ста́ром го́роде."],
        "correct": "Я говорю́ с молоды́м води́телем о ста́ром го́роде.",
        "explanation": "<p>Ikkita kelishik: Твори́тельный (<strong>-ым</strong>) va "
                       "Предло́жный (<strong>-ом</strong>). Ikkalasi ham erkak "
                       "jinsida.</p>",
    },
]


# =====================================================================
# PR-45 — Koʻplik И.п. va Р.п.
# =====================================================================

Q_PR45 = [
    # 1–5 tanish
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>дом → ___</strong> "
                "(koʻplik)</p>",
        "choices": ["до́мы", "дома́", "домо́в", "до́ма"],
        "correct": "дома́",
        "explanation": "<p><em>Дом</em> — <strong>-А́</strong> roʻyxatidan, va urgʻu "
                       "oxirida. Bu roʻyxatda yana: <em>города́, учителя́, вечера́, "
                       "поезда́, глаза́</em>.</p>",
    },
    {
        "text": "<p><strong>челове́к</strong> ning koʻpligi qaysi?</p>",
        "choices": ["челове́ки", "челове́ка", "лю́ди", "челове́ков"],
        "correct": "лю́ди",
        "explanation": "<p>Butunlay boshqa soʻz — <strong>лю́ди</strong>, va uning "
                       "Роди́тельный shakli <em>люде́й</em>. Bunday soʻzlar qoida "
                       "bilan emas, yodlab olinadi.</p>",
    },
    {
        "text": "<p><strong>друг</strong> ning koʻpligi qaysi?</p>",
        "choices": ["дру́ги", "друзья́", "дру́гов", "дру́га"],
        "correct": "друзья́",
        "explanation": "<p><strong>Друзья́</strong>, Роди́тельный shakli "
                       "<em>друзе́й</em>. Xuddi shunday: <em>брат → бра́тья</em>, "
                       "<em>сын → сыновья́</em>, <em>де́рево → дере́вья</em>.</p>",
    },
    {
        "text": "<p>Ayol jinsidagi ot koʻplik Роди́тельный'da qanday tugaydi?</p>",
        "choices": ["-ов", "-ей", "Qoʻshimchasiz qoladi", "-ы"],
        "correct": "Qoʻshimchasiz qoladi",
        "explanation": "<p><em>кни́га → книг</em>, <em>шко́ла → школ</em>, "
                       "<em>мину́та → мину́т</em>. Soʻz «yalangʻoch» qoladi — bu "
                       "aslida eng oson shakl.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>пять ___</strong> "
                "(день)</p>",
        "choices": ["день", "дня", "дней", "дни"],
        "correct": "дней",
        "explanation": "<p>5 dan boshlab koʻplik Роди́тельный. <em>День → дни → "
                       "дней</em> — bu shakl ham alohida yodlanadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>У меня́ мно́го "
                "___.</strong> (друг)</p>",
        "choices": ["дру́гов", "друзе́й", "друзья́", "дру́га"],
        "correct": "друзе́й",
        "explanation": "<p>Ikki qadam: koʻplik <em>друзья́</em>, keyin "
                       "Роди́тельный <strong>друзе́й</strong>. <em>Мно́го</em> koʻplik "
                       "Роди́тельный talab qiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Во дворе́ мно́го "
                "___.</strong> (де́рево)</p>",
        "choices": ["дере́во", "дере́ва", "дере́вьев", "дере́вья"],
        "correct": "дере́вьев",
        "explanation": "<p><em>Де́рево → дере́вья → дере́вьев</em>. <strong>-ЬЯ</strong> "
                       "guruhi Роди́тельный'da <strong>-ЬЕВ</strong> oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Здесь мно́го "
                "___.</strong> (челове́к)</p>",
        "choices": ["челове́к", "челове́ков", "люде́й", "лю́ди"],
        "correct": "люде́й",
        "explanation": "<p><em>Мно́го</em> bilan <strong>люде́й</strong>. Lekin "
                       "<strong>son</strong> bilan boshqacha: <em>пять "
                       "челове́к</em> (PR-36).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>В кла́ссе два́дцать "
                "___.</strong> (учени́к)</p>",
        "choices": ["учени́к", "ученика́", "ученики́", "ученико́в"],
        "correct": "ученико́в",
        "explanation": "<p>Erkak jins, undosh bilan tugaydi → <strong>-ов</strong>. "
                       "20 — 5 dan yuqori, demak koʻplik Роди́тельный.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>пять ___</strong> "
                "(кни́га)</p>",
        "choices": ["кни́ги", "книг", "кни́гов", "кни́га"],
        "correct": "книг",
        "explanation": "<p>Ayol jinsi koʻplik Роди́тельный'da qoʻshimchasini "
                       "yoʻqotadi: <strong>книг</strong>.</p>",
    },
    {
        "text": "<p>Koʻplikka qoʻying: <strong>окно́</strong></p>",
        "choices": ["окны́", "окни́", "о́кна", "окно́в"],
        "correct": "о́кна",
        "explanation": "<p>Oʻrta jins koʻplikda <strong>-А / -Я</strong> oladi: "
                       "<em>окно́ → о́кна</em>, <em>сло́во → слова́</em>, "
                       "<em>мо́ре → моря́</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>де́сять ___</strong> "
                "(год)</p>",
        "choices": ["год", "го́да", "лет", "годо́в"],
        "correct": "лет",
        "explanation": "<p>5 dan boshlab <em>год</em> ning oʻrniga <strong>лет</strong> "
                       "ishlatiladi. Bu shakl alohida yodlanadi — yosh haqida "
                       "gapirganda har kuni kerak.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu ikki gapda nega har xil shakl?</p><p><strong>три дру́га · "
                "мно́го друзе́й</strong></p>",
        "choices": ["2-3-4 dan keyin Р.п. birlik, мно́го bilan Р.п. koʻplik",
                    "Ikkalasi bir xil",
                    "Birinchisi xato",
                    "Chunki «друг» jonli"],
        "correct": "2-3-4 dan keyin Р.п. birlik, мно́го bilan Р.п. koʻplik",
        "explanation": "<p>PR-36 qoidasi. <em>Три дру́га</em> — Роди́тельный "
                       "<strong>birlik</strong>; <em>мно́го друзе́й</em> — "
                       "Роди́тельный <strong>koʻplik</strong>.</p>",
    },
    {
        "text": "<p>Oʻzbek tilida koʻplik qanday yasaladi?</p>",
        "choices": ["Bitta qoʻshimcha: -lar, deyarli istisnosiz",
                    "Uchta qoʻshimcha, jinsga qarab",
                    "Soʻz butunlay oʻzgaradi",
                    "Koʻplik yasalmaydi"],
        "correct": "Bitta qoʻshimcha: -lar, deyarli istisnosiz",
        "explanation": "<p><em>kitoblar, uylar, odamlar, bolalar</em> — bitta qoida. "
                       "Ruschada esa koʻplik baʼzan butun soʻzni qayta yasaydi "
                       "(<em>челове́к → лю́ди</em>). Shuning uchun bu yerda qoidani "
                       "emas, <strong>soʻzlarni</strong> yodlash kerak.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["дома́ · друзья́ · де́ти", "до́мы · друзья́ · де́ти",
                    "дома́ · дру́ги · ребёнки", "дома́ · друзья́ · ребёнки"],
        "correct": "дома́ · друзья́ · де́ти",
        "explanation": "<p>Uchtasi ham notoʻgʻri koʻplik: <em>дом → дома́</em> "
                       "(-А́ roʻyxati), <em>друг → друзья́</em>, <em>ребёнок → "
                       "де́ти</em>.</p>",
    },
    {
        "text": "<p>Nega bu dars kursning eng qiyin joyi deb ataladi?</p>",
        "choices": ["Chunki koʻplik Роди́тельный eng koʻp istisnoga ega",
                    "Chunki qoidalar juda uzun",
                    "Chunki oʻzbekchada koʻplik yoʻq",
                    "Chunki bu oxirgi dars"],
        "correct": "Chunki koʻplik Роди́тельный eng koʻp istisnoga ega",
        "explanation": "<p>Qoidalar bor, lekin istisnolar ham koʻp: <em>лю́ди, де́ти, "
                       "друзья́, дома́, лет</em>. Yaxshi xabar — keyingi dars butun "
                       "blokdagi <strong>eng osoni</strong>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["У меня́ мно́го книг.", "Здесь мно́го челове́ков.",
                    "Во дворе́ мно́го дере́вьев.", "Мне два́дцать лет."],
        "correct": "Здесь мно́го челове́ков.",
        "explanation": "<p>Toʻgʻrisi — <strong>мно́го люде́й</strong>. "
                       "<em>Челове́к</em> ning koʻpligi butunlay boshqa soʻz. Son "
                       "bilan esa <em>пять челове́к</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Э́то мои́ до́мы.", "Э́то мои́ дома́.",
                    "Э́то мои́ домо́в.", "Э́то мои́ до́ма."],
        "correct": "Э́то мои́ дома́.",
        "explanation": "<p><em>Дом</em> koʻplikda <strong>дома́</strong> boʻladi, "
                       "urgʻu oxirida. <em>До́ма</em> (urgʻu boshida) — «uyda» degan "
                       "ravish yoki Роди́тельный birlik.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Ско́лько у тебя́ друзе́й?</strong></p>",
        "choices": ["— Три дру́га.", "— Три друзе́й.",
                    "— Три друзья́.", "— Три дру́гов."],
        "correct": "— Три дру́га.",
        "explanation": "<p>3 dan keyin Роди́тельный <strong>birlik</strong> — "
                       "<em>дру́га</em>. Savolda esa <em>друзе́й</em>, chunki "
                       "<em>ско́лько</em> koʻplik talab qiladi.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Hovlida koʻp daraxt va "
                "bola bor.</strong></p>",
        "choices": ["Во дворе́ мно́го дере́во и ребёнок.",
                    "Во дворе́ мно́го дере́вьев и дете́й.",
                    "Во дворе́ мно́го дере́вья и де́ти.",
                    "Во дворе́ мно́го дере́вьев и ребёнков."],
        "correct": "Во дворе́ мно́го дере́вьев и дете́й.",
        "explanation": "<p>Ikkala soʻz ham notoʻgʻri koʻplik: <em>де́рево → "
                       "дере́вья → дере́вьев</em>, <em>ребёнок → де́ти → "
                       "дете́й</em>.</p>",
    },
]


# =====================================================================
# PR-46 — Koʻplik Д./В./Т./П.
# =====================================================================

Q_PR46 = [
    # 1–5 tanish
    {
        "text": "<p>Koʻplik Да́тельный qanday tugaydi?</p>",
        "choices": ["-ах", "-ам", "-ами", "-ов"],
        "correct": "-ам",
        "explanation": "<p><em>дома́м, кни́гам, о́кнам</em> — uchala jins uchun bir "
                       "xil. Yumshoq oʻzakda <strong>-ям</strong>: "
                       "<em>друзья́м</em>.</p>",
    },
    {
        "text": "<p>Koʻplikda sifat va ot jinsga qaraydimi?</p>",
        "choices": ["Ha, uchta shakl bor", "Yoʻq — jins yoʻqoladi",
                    "Faqat jonli otlarda", "Faqat Твори́тельный'da"],
        "correct": "Yoʻq — jins yoʻqoladi",
        "explanation": "<p>Butun blok davomida jins bilan kurashildi — koʻplikda u "
                       "<strong>umuman yoʻqoladi</strong>. Uchta qoʻshimcha: "
                       "<strong>-АМ, -АМИ, -АХ</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я говорю́ с "
                "___.</strong> (лю́ди)</p>",
        "choices": ["лю́дями", "людьми́", "лю́дям", "люде́й"],
        "correct": "людьми́",
        "explanation": "<p>Butun tizimdagi ikkita istisnodan biri — "
                       "<strong>людьми́</strong>, <em>«лю́дями»</em> emas. Ikkinchisi "
                       "— <em>детьми́</em>. Ular qofiyalanadi.</p>",
    },
    {
        "text": "<p>Koʻplik Предло́жный qanday tugaydi?</p>",
        "choices": ["-ам", "-ами", "-ах", "-ых"],
        "correct": "-ах",
        "explanation": "<p><em>о дома́х, о кни́гах, об о́кнах</em>. Yumshoq oʻzakda "
                       "<strong>-ях</strong>: <em>о друзья́х</em>. Sifat esa "
                       "<strong>-ых</strong> oladi.</p>",
    },
    {
        "text": "<p>Koʻplik Вини́тельный qanday tanlanadi?</p>",
        "choices": ["Har doim -ам", "Jonsiz = И.п., jonli = Р.п.",
                    "Har doim Р.п.", "Har doim И.п."],
        "correct": "Jonsiz = И.п., jonli = Р.п.",
        "explanation": "<p><em>Я ви́жу дома́</em> (jonsiz) va <em>я ви́жу друзе́й</em> "
                       "(jonli). Bu PR-32 dagi qoidaning oʻsha oʻzi — Вини́тельный "
                       "yangi shakl yaratmaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я пишу́ ___.</strong> "
                "(друзья́)</p>",
        "choices": ["друзе́й", "друзья́м", "друзья́ми", "друзья́х"],
        "correct": "друзья́м",
        "explanation": "<p><em>Писа́ть</em> Да́тельный oladi (PR-37), koʻplik "
                       "Да́тельный esa yumshoq oʻzakda <strong>-ям</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю о "
                "___.</strong> (де́ти)</p>",
        "choices": ["де́тям", "детьми́", "де́тях", "дете́й"],
        "correct": "де́тях",
        "explanation": "<p>Предло́жный → <strong>-ях</strong>. Diqqat: "
                       "<em>детьми́</em> faqat Твори́тельный'da ishlatiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Она́ рабо́тает с "
                "___.</strong> (де́ти)</p>",
        "choices": ["де́тями", "детьми́", "де́тям", "де́тях"],
        "correct": "детьми́",
        "explanation": "<p>Ikkinchi istisno. <em>Детьми́</em> va <em>людьми́</em> — "
                       "faqat shu ikkitasi <strong>-ЬМИ</strong> oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я жил в двух "
                "___.</strong> (города́)</p>",
        "choices": ["города́м", "города́ми", "города́х", "городо́в"],
        "correct": "города́х",
        "explanation": "<p><em>В</em> + Предло́жный → koʻplikda "
                       "<strong>-ах</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ду́маю о ___ "
                "друзья́х.</strong> (ста́рые)</p>",
        "choices": ["ста́рым", "ста́рыми", "ста́рых", "ста́рые"],
        "correct": "ста́рых",
        "explanation": "<p>Koʻplik Предло́жный'da sifat <strong>-ых</strong> oladi. "
                       "Sifat va ot birga oʻzgaradi: <em>о ста́рых "
                       "друзья́х</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___.</strong> "
                "(друзья́)</p>",
        "choices": ["друзья́", "друзе́й", "друзья́м", "друзья́ми"],
        "correct": "друзе́й",
        "explanation": "<p>Doʻstlar — <strong>jonli</strong>, demak Вини́тельный "
                       "Роди́тельный shaklini oladi: <em>друзе́й</em>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Я ви́жу ___.</strong> "
                "(но́вые дома́)</p>",
        "choices": ["но́вых домо́в", "но́вые дома́",
                    "но́вым дома́м", "но́выми дома́ми"],
        "correct": "но́вые дома́",
        "explanation": "<p>Uylar — <strong>jonsiz</strong>, demak Вини́тельный bosh "
                       "kelishik bilan bir xil qoladi: sifat ham, ot ham.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Bu uch shakl bitta soʻzdan. Kelishiklarini toping.</p>"
                "<p><strong>друзья́м · друзья́ми · о друзья́х</strong></p>",
        "choices": ["Д.п. · Т.п. · П.п.", "Р.п. · Д.п. · Т.п.",
                    "В.п. · Т.п. · П.п.", "Д.п. · П.п. · Т.п."],
        "correct": "Д.п. · Т.п. · П.п.",
        "explanation": "<p>Bitta oʻzak (<em>друзь-</em>) va uchta qoʻshimcha: "
                       "<strong>-ЯМ, -ЯМИ, -ЯХ</strong>. Koʻplikda hech qanday jins "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Oʻzbek tili bu darsda qanday yordam beradi?</p>",
        "choices": ["Umuman yordam bermaydi",
                    "Toʻliq: oʻzbekchada ham koʻplik va kelishik alohida qoʻshimchalar",
                    "Faqat jonli otlarda",
                    "Faqat Твори́тельный'da"],
        "correct": "Toʻliq: oʻzbekchada ham koʻplik va kelishik alohida qoʻshimchalar",
        "explanation": "<p><em>doʻst-<strong>lar</strong>-<strong>ga</strong></em> · "
                       "<em>друзь-<strong>я́м</strong></em>. Ikkala tilda ham koʻplik "
                       "oʻzagi bir marta yasaladi, keyin kelishik qoʻshiladi. "
                       "Koʻplikda ruscha oʻzbekchaga eng yaqin turadi.</p>",
    },
    {
        "text": "<p>Nechta istisno bor koʻplik Твори́тельный'da?</p>",
        "choices": ["Bitta", "Ikkita: детьми́ va людьми́",
                    "Beshta", "Hech qanday"],
        "correct": "Ikkita: детьми́ va людьми́",
        "explanation": "<p>Qolgan hamma soʻz <strong>-АМИ / -ЯМИ</strong> oladi. Bu "
                       "ikkitasi juda koʻp ishlatiladi, shuning uchun ularni birga "
                       "yodlash kerak.</p>",
    },
    {
        "text": "<p>Qaysi qatorda hammasi toʻgʻri?</p>",
        "choices": ["друзья́м · с людьми́ · о де́тях",
                    "друзьёв · с лю́дями · о де́тях",
                    "друзья́м · с лю́дями · о де́тям",
                    "друзья́ми · с людьми́ · о де́тей"],
        "correct": "друзья́м · с людьми́ · о де́тях",
        "explanation": "<p>Д.п. <strong>-ям</strong>, Т.п. istisno "
                       "<strong>людьми́</strong>, П.п. <strong>-ях</strong>. Uchta "
                       "boshqa kelishik, uchta toʻgʻri shakl.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Я пишу́ ста́рым друзья́м.", "Я ду́маю о де́тях.",
                    "Я говорю́ с лю́дями.", "Я ви́жу но́вые дома́."],
        "correct": "Я говорю́ с лю́дями.",
        "explanation": "<p>Toʻgʻrisi — <strong>с людьми́</strong>. Bu ikkita "
                       "istisnodan biri; ikkinchisi — <em>детьми́</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Я ду́маю о друзья́м.", "Я ду́маю о друзья́х.",
                    "Я ду́маю о друзья́ми.", "Я ду́маю о друзе́й."],
        "correct": "Я ду́маю о друзья́х.",
        "explanation": "<p><em>Ду́мать о</em> Предло́жный oladi (PR-31), koʻplikda "
                       "esa <strong>-ях</strong>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni davom ettiring. Qaysi javob tabiiy?</p>"
                "<p><strong>— Кому́ ты пи́шешь?</strong></p>",
        "choices": ["— Ста́рым друзья́м.", "— Ста́рых друзе́й.",
                    "— Ста́рыми друзья́ми.", "— О ста́рых друзья́х."],
        "correct": "— Ста́рым друзья́м.",
        "explanation": "<p>Savol <em>кому́?</em> — Да́тельный, koʻplikda sifat "
                       "<strong>-ым</strong> va ot <strong>-ям</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni ruschaga oʻgiring.</p><p><strong>Turli odamlar bilan "
                "ishlayman va eski doʻstlar haqida oʻylayman.</strong></p>",
        "choices": ["Рабо́таю с ра́зными лю́дями и ду́маю о ста́рых друзья́х.",
                    "Рабо́таю с ра́зными людьми́ и ду́маю о ста́рых друзья́х.",
                    "Рабо́таю с ра́зными людьми́ и ду́маю о ста́рым друзья́м.",
                    "Рабо́таю с ра́зные людьми́ и ду́маю о ста́рых друзья́х."],
        "correct": "Рабо́таю с ра́зными людьми́ и ду́маю о ста́рых друзья́х.",
        "explanation": "<p>Ikkita kelishik: Твори́тельный (sifat "
                       "<strong>-ыми</strong> + istisno <strong>людьми́</strong>) va "
                       "Предло́жный (<strong>-ых … -ях</strong>).</p>",
    },
]


PRACTICES = [
    {
        "title": "PR-44 Mashq: Sifatlarning turlanishi 2 — Дательный, Творительный, Предложный",
        "description": (
            "Uchta yangi qoʻshimcha (-ому, -ым, -ом), ayol jinsidagi -ОЙ ning "
            "toʻrtta ishi va savol soʻzi bilan tekshirish usuli."
        ),
        "tutorial": "PR-44:",
        "questions": Q_PR44,
    },
    {
        "title": "PR-45 Mashq: Koʻplik kelishiklari 1 — Именительный va Родительный",
        "description": (
            "Kursning eng koʻp istisnoli darsi: -А́ roʻyxati (дома́, города́), "
            "notoʻgʻri koʻpliklar (лю́ди, де́ти, друзья́) va koʻplik Р.п."
        ),
        "tutorial": "PR-45:",
        "questions": Q_PR45,
    },
    {
        "title": "PR-46 Mashq: Koʻplik kelishiklari 2 — Дательный, Винительный, Творительный, Предложный",
        "description": (
            "Blokdagi eng oson dars: -АМ, -АМИ, -АХ va jinsning yoʻqolishi. "
            "Ikkita istisno — детьми́ va людьми́."
        ),
        "tutorial": "PR-46:",
        "questions": Q_PR46,
    },
]
