# -*- coding: utf-8 -*-
"""IELTS grammar bank — Tenses & aspect (zamonlar).

Order decade 100-199. The foundation group: Task 1 lives or dies on choosing
the right tense for the chart's dates, and Speaking Part 1-2 is marked on
past/present accuracy before anything fancier is even looked at.
See STYLE_GUIDE_GRAMMAR_IELTS.md.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "Ingliz tili imtihoniga tayyorgarlik (Academic).",
    "icon":    "bi-globe2",
    "color":   "#059669",
}

POINTS = [
    {
        "pattern":   "present simple",
        "category":  "en_tense",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "register":  "both",
        "meaning":   "hozirgi oddiy zamon — umumiy haqiqat, odat, doimiy holat",
        "attach":    "S + V(s/es) · S + do/does not + V",
        "form_rule": "3-shaxs birlikda <b>-s</b> qo‘shiladi: he work<b>s</b>, it depend<b>s</b>. "
                     "Inkor va so‘roqda <b>do/does</b> keladi, asosiy fe’l esa yalang‘och qoladi: "
                     "he do<b>es</b>n’t <u>work</u> (❌ doesn’t works).",
        "note":      "<p><b>Task 2 inshosining asosiy zamoni shu.</b> Umumiy haqiqat va hozirgi "
                     "holat haqida yozasiz: <i>Many countries face a shortage of teachers.</i></p>"
                     "<p>Shuningdek diagramma <b>jarayonini</b> (process diagram) tasvirlashda "
                     "ham present simple + passive ishlatiladi: <i>The beans are dried and packed.</i></p>",
        "mistake":   "<p>❌ The government <u>have</u> to act → ✅ The government <b>has</b> to act "
                     "(rasmiy Britaniya inglizchasida <i>have</i> ham to‘g‘ri, lekin imtihonda "
                     "bittasini tanlab, oxirigacha shuni ishlating).</p>"
                     "<p>❌ Everyone <u>have</u> a phone → ✅ Everyone <b>has</b> a phone — "
                     "<i>everyone, each, every</i> birlik.</p>",
        "examples": [
            ("Air pollution affects millions of people in large cities.",
             "Havo ifloslanishi yirik shaharlarda millionlab odamga ta’sir qiladi."),
            ("The chart shows how much water each region consumes.",
             "Diagramma har bir mintaqa qancha suv iste’mol qilishini ko‘rsatadi."),
        ],
        "synonyms": [
            ("present continuous", "present simple = doimiy holat/odat; present continuous = "
                                   "aynan hozir davom etayotgan yoki vaqtinchalik jarayon"),
        ],
        "order": 100,
    },
    {
        "pattern":   "present continuous",
        "category":  "en_tense",
        "function":  "time",
        "level":     1,
        "freq":      2,
        "register":  "both",
        "meaning":   "hozirgi davomiy zamon — hozir davom etayotgan, vaqtinchalik yoki o‘zgarib borayotgan",
        "attach":    "S + am/is/are + V-ing",
        "form_rule": "<b>am/is/are</b> + fe’l<b>-ing</b>. Holat fe’llari (know, believe, own, "
                     "consist, contain) odatda bu shaklda <u>kelmaydi</u>: ❌ I am knowing.",
        "note":      "<p>IELTS’da eng foydali vazifasi — <b>o‘zgarib borayotgan tendensiya</b>: "
                     "<i>The population is ageing rapidly.</i> Bu Task 2 kirish qismida juda "
                     "yaxshi ishlaydi.</p>"
                     "<p>Speaking Part 1 da esa hozirgi hayotingiz haqida: "
                     "<i>I’m studying engineering at the moment.</i></p>",
        "mistake":   "<p>❌ Nowadays people <u>use</u> smartphones more and more → ✅ people "
                     "<b>are using</b> … — o‘zgarish bo‘lsa continuous tabiiyroq.</p>",
        "examples": [
            ("The climate is changing faster than previously predicted.",
             "Iqlim ilgari bashorat qilinganidan tezroq o‘zgarmoqda."),
            ("More and more students are choosing to study abroad.",
             "Tobora ko‘proq talaba chet elda o‘qishni tanlamoqda."),
        ],
        "synonyms": [
            ("present simple", "continuous = vaqtinchalik va o‘zgaruvchan; simple = doimiy haqiqat"),
        ],
        "order": 101,
    },
    {
        "pattern":   "past simple",
        "category":  "en_tense",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "register":  "both",
        "meaning":   "o‘tgan oddiy zamon — tugagan va vaqti aytilgan ish",
        "attach":    "S + V-ed / V2 · S + did not + V",
        "form_rule": "To‘g‘ri fe’llar <b>-ed</b>, noto‘g‘ri fe’llar 2-shakl (rise → <b>rose</b>, "
                     "fall → <b>fell</b>, begin → <b>began</b>). Inkorda <b>did not</b> + yalang‘och "
                     "fe’l: ❌ didn’t rose → ✅ didn’t <b>rise</b>.",
        "note":      "<p><b>Task 1 ning asosiy zamoni</b>, agar grafikdagi yillar o‘tib bo‘lgan "
                     "bo‘lsa: <i>Between 1990 and 2005, car ownership rose sharply.</i> "
                     "Yillar berilgan — demak past simple, present perfect emas.</p>"
                     "<p>Speaking Part 2 (hikoya) ham deyarli butunlay shu zamonda.</p>",
        "mistake":   "<p>❌ In 2010 the number <u>has increased</u> → ✅ <b>increased</b> — "
                     "aniq vaqt aytilgan joyda present perfect ishlatilmaydi.</p>",
        "examples": [
            ("The figure for renewable energy doubled between 2005 and 2015.",
             "Qayta tiklanuvchi energiya ko‘rsatkichi 2005-2015 yillarda ikki baravar oshdi."),
            ("Last year I took the test for the first time.",
             "O‘tgan yili men imtihonni birinchi marta topshirdim."),
        ],
        "synonyms": [
            ("present perfect", "past simple = vaqt AYTILGAN (in 2010, last year); "
                                "present perfect = vaqt aytilmagan, natijasi hozir muhim"),
            ("past continuous", "past simple = tugagan voqea; past continuous = o‘sha paytda "
                                "davom etayotgan fon"),
        ],
        "order": 102,
    },
    {
        "pattern":   "past continuous",
        "category":  "en_tense",
        "function":  "time",
        "level":     3,
        "freq":      2,
        "register":  "both",
        "meaning":   "o‘tgan davomiy zamon — o‘sha paytda davom etayotgan fon harakati",
        "attach":    "S + was/were + V-ing",
        "form_rule": "<b>was</b> (I/he/she/it) yoki <b>were</b> (you/we/they) + <b>-ing</b>. "
                     "Ko‘pincha <b>when</b> (past simple) yoki <b>while</b> (past continuous) "
                     "bilan juftlashadi.",
        "note":      "<p>Speaking Part 2 hikoyasini jonlantiradigan zamon: fonni continuous, "
                     "voqeani simple bilan bering — <i>I <b>was waiting</b> for the bus when "
                     "I <b>met</b> my old teacher.</i></p>",
        "mistake":   "<p>❌ While I <u>studied</u>, the phone rang → ✅ While I <b>was studying</b>, "
                     "the phone rang.</p>",
        "examples": [
            ("Afsona was preparing for the exam when the power went out.",
             "Afsona imtihonga tayyorlanayotganda elektr o‘chib qoldi."),
        ],
        "synonyms": [
            ("past simple", "continuous = davom etayotgan fon; simple = uni bo‘lgan voqea"),
        ],
        "order": 103,
    },
    {
        "pattern":   "present perfect",
        "category":  "en_tense",
        "function":  "time",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "hozirgi tugallangan zamon — o‘tmishda bo‘lgan, natijasi hozir muhim",
        "attach":    "S + have/has + V3",
        "form_rule": "<b>have/has</b> + 3-shakl (been, done, risen, fallen). "
                     "Belgilar: <b>since</b> (boshlanish nuqtasi), <b>for</b> (davomiylik), "
                     "<b>already, yet, just, recently, over the past decade</b>.",
        "note":      "<p><b>Band 6 dan 7 ga o‘tishning eng oddiy yo‘li</b> — Task 2 da hozirgi "
                     "holatning tarixini ko‘rsatish: <i>Over the past two decades, "
                     "governments <b>have invested</b> heavily in renewable energy.</i></p>"
                     "<p>Task 1 da esa faqat grafik <u>bugungi kunga qadar</u> davom etsa "
                     "ishlatiladi (masalan 2015-present).</p>",
        "mistake":   "<p>❌ I have finished it <u>yesterday</u> → ✅ I <b>finished</b> it yesterday. "
                     "Aniq o‘tgan vaqt bo‘lsa — past simple.</p>"
                     "<p>❌ I have <u>went</u> → ✅ I have <b>gone</b> — 3-shakl kerak, 2-shakl emas.</p>",
        "examples": [
            ("The cost of housing has risen sharply since 2010.",
             "Uy-joy narxi 2010-yildan beri keskin oshdi."),
            ("Technology has transformed the way we work.",
             "Texnologiya ishlash usulimizni tubdan o‘zgartirdi."),
        ],
        "synonyms": [
            ("past simple", "present perfect = vaqt aytilmaydi, natija hozir; past simple = "
                            "vaqt aytilgan va tugagan"),
            ("present perfect continuous", "perfect = natija/miqdor muhim; perfect continuous = "
                                           "jarayonning davomiyligi muhim"),
        ],
        "order": 104,
    },
    {
        "pattern":   "present perfect continuous",
        "category":  "en_tense",
        "function":  "time",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "hozirgi tugallangan davomiy — o‘tmishda boshlanib, hozir ham davom etayotgan jarayon",
        "attach":    "S + have/has been + V-ing",
        "form_rule": "<b>have/has been</b> + <b>-ing</b>. Odatda <b>for</b> / <b>since</b> bilan. "
                     "Holat fe’llari (know, believe) bilan ishlatilmaydi.",
        "note":      "<p>Davomiylikning o‘zini ta’kidlaydi: <i>Scientists <b>have been warning</b> "
                     "about this for decades.</i> — «yillar davomida ogohlantirib kelishmoqda». "
                     "Bitta yaxshi joyda ishlatilgan bu shakl Grammatical Range bahosini oshiradi.</p>",
        "mistake":   "<p>❌ I am living here since 2019 → ✅ I <b>have been living</b> here since 2019 "
                     "— o‘zbekcha «yashayapman» present continuous’ni tortadi, lekin ingliz tilida "
                     "<i>since</i> bo‘lsa perfect kerak.</p>",
        "examples": [
            ("Researchers have been studying this phenomenon since the 1980s.",
             "Tadqiqotchilar bu hodisani 1980-yillardan beri o‘rganib kelmoqda."),
        ],
        "synonyms": [
            ("present perfect", "perfect = qancha/qanday natija; perfect continuous = "
                                "qancha VAQTDAN beri davom etayotgani"),
        ],
        "order": 105,
    },
    {
        "pattern":   "past perfect",
        "category":  "en_tense",
        "function":  "time",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "o‘tgan zamondan oldingi zamon — «undan ham oldin bo‘lgan» ish",
        "attach":    "S + had + V3",
        "form_rule": "<b>had</b> + 3-shakl — barcha shaxslarda bir xil. Ko‘pincha <b>by</b> "
                     "(by 2000), <b>before</b>, <b>after</b>, <b>already</b> bilan keladi.",
        "note":      "<p>Ikki o‘tgan voqeaning <b>qaysi biri oldin</b> bo‘lganini ko‘rsatadi. "
                     "Task 1 da juda foydali: <i>By 2010, the figure <b>had reached</b> its peak.</i> "
                     "— «2010-yilga kelib allaqachon cho‘qqiga chiqqan edi».</p>"
                     "<p>Third conditional ham shu shaklda quriladi (<i>If they had acted…</i>).</p>",
        "mistake":   "<p>❌ Har bir o‘tgan gapga <i>had</i> qo‘shib chiqmang. Voqealar tartib bilan "
                     "aytilsa, oddiy past simple yetarli.</p>",
        "examples": [
            ("By 2005 the number of subscribers had exceeded ten million.",
             "2005-yilga kelib obunachilar soni o‘n milliondan oshgan edi."),
            ("The factory had already closed before the new law was passed.",
             "Yangi qonun qabul qilinishidan oldin zavod allaqachon yopilgan edi."),
        ],
        "synonyms": [
            ("past simple", "past perfect = ikki o‘tgan ishning OLDINGISI; past simple = "
                            "oddiy ketma-ketlik"),
            ("the third conditional", "third conditional shu shaklni <i>if</i> bilan ishlatadi"),
        ],
        "order": 106,
    },
    {
        "pattern":   "will",
        "category":  "en_tense",
        "function":  "guess",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "kelasi zamon — bashorat, qaror, va’da",
        "attach":    "S + will + V (yalang‘och)",
        "form_rule": "<b>will</b> + fe’lning asosiy shakli, barcha shaxslarda bir xil. "
                     "❌ will to go · ❌ will goes. Inkor: <b>will not / won’t</b>.",
        "note":      "<p>Task 2 xulosasida deyarli har doim kerak bo‘ladi: <i>Unless action is "
                     "taken, the situation <b>will</b> deteriorate further.</i></p>"
                     "<p>⚠️ Yolg‘iz <i>will</i> juda qat’iy jaranglaydi. Band 7 uchun uni "
                     "yumshating: <b>will probably</b>, <b>is likely to</b>, <b>may well</b>.</p>",
        "mistake":   "<p>❌ If it <u>will</u> rain, we will stay → ✅ If it <b>rains</b>, we will stay "
                     "— <i>if</i> ergash gapida <i>will</i> ishlatilmaydi.</p>",
        "examples": [
            ("The demand for water will double over the next thirty years.",
             "Suvga bo‘lgan talab keyingi o‘ttiz yilda ikki baravar oshadi."),
        ],
        "synonyms": [
            ("be going to", "will = shu topda qaror yoki umumiy bashorat; be going to = "
                            "oldindan qilingan reja yoki hozirgi dalilga asoslangan bashorat"),
            ("be likely to", "be likely to = ehtiyotkorroq va akademikroq — Task 2 uchun xavfsizroq"),
        ],
        "order": 107,
    },
    {
        "pattern":   "be going to",
        "category":  "en_tense",
        "function":  "guess",
        "level":     2,
        "freq":      2,
        "register":  "polite",
        "meaning":   "kelasi zamon — oldindan qilingan reja yoki ko‘rinib turgan natija",
        "attach":    "S + am/is/are going to + V",
        "form_rule": "<b>am/is/are going to</b> + asosiy fe’l. Og‘zaki nutqda <i>gonna</i> "
                     "eshitiladi — Speaking’da tabiiy, <b>Writing’da hech qachon</b>.",
        "note":      "<p>Speaking Part 1-2 da rejalar haqida gapirganda eng tabiiy shakl: "
                     "<i>I’m going to apply for a master’s next year.</i></p>",
        "mistake":   "<p>❌ Task 2 inshosida <i>gonna</i> yoki <i>I’m going to talk about…</i> — "
                     "bu og‘zaki uslub, insho uchun mos emas.</p>",
        "examples": [
            ("Jasur is going to take the test in September.",
             "Jasur imtihonni sentyabrda topshirmoqchi."),
        ],
        "synonyms": [
            ("will", "going to = reja allaqachon bor; will = shu topda qaror qilingan"),
        ],
        "order": 108,
    },
    {
        "pattern":   "future continuous",
        "category":  "en_tense",
        "function":  "time",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "kelasi davomiy — kelajakning ma’lum bir paytida davom etayotgan bo‘ladi",
        "attach":    "S + will be + V-ing",
        "form_rule": "<b>will be</b> + <b>-ing</b>.",
        "note":      "<p>Speaking Part 3 da kelajak haqidagi savolga o‘zgacha javob beradi: "
                     "<i>In ten years’ time, most people <b>will be working</b> remotely.</i> "
                     "Bitta shunday jumla Grammatical Range uchun yaxshi dalil.</p>",
        "examples": [
            ("By 2040, millions of drivers will be using electric vehicles.",
             "2040-yilga borib millionlab haydovchi elektromobildan foydalanayotgan bo‘ladi."),
        ],
        "synonyms": [
            ("will", "will = oddiy bashorat; will be doing = o‘sha paytda davom etayotgan holat"),
            ("future perfect", "future perfect = o‘sha paytga qadar TUGAGAN bo‘ladi"),
        ],
        "order": 109,
    },
    {
        "pattern":   "future perfect",
        "category":  "en_tense",
        "function":  "time",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "kelasi tugallangan — kelajakdagi bir vaqtga qadar tugagan bo‘ladi",
        "attach":    "S + will have + V3 (+ by 2030)",
        "form_rule": "<b>will have</b> + 3-shakl. Deyarli doim <b>by</b> + sana bilan: "
                     "<i>by 2050</i>, <i>by the end of the decade</i>.",
        "note":      "<p>Bashoratli grafiklar (projection) uchun tayyor qolip: "
                     "<i>By 2050, the urban population <b>will have overtaken</b> the rural one.</i></p>",
        "mistake":   "<p>❌ <i>By 2050 the population will overtake…</i> — noto‘g‘ri emas, lekin "
                     "<i>by</i> bilan future perfect aniqroq va band-ballga foydaliroq.</p>",
        "examples": [
            ("By 2030, the country will have cut its emissions by half.",
             "2030-yilga borib mamlakat chiqindilarini ikki baravar qisqartirgan bo‘ladi."),
        ],
        "synonyms": [
            ("future continuous", "future continuous = davom etayotgan bo‘ladi; "
                                  "future perfect = tugagan bo‘ladi"),
        ],
        "order": 110,
    },
    {
        "pattern":   "used to",
        "category":  "en_tense",
        "function":  "contrast",
        "level":     3,
        "freq":      2,
        "register":  "both",
        "meaning":   "o‘tmishdagi odat yoki holat — «ilgari ... edi, endi yo‘q»",
        "attach":    "S + used to + V (yalang‘och)",
        "form_rule": "<b>used to</b> + asosiy fe’l. Inkor va so‘roqda <b>use to</b> "
                     "(did<b>n’t use to</b>). ⚠️ <b>be used to + -ing</b> butunlay boshqa narsa: "
                     "«ko‘nikkan».",
        "note":      "<p>Hozir va o‘tmishni qarama-qarshi qo‘yish uchun eng ixcham vosita — "
                     "Speaking Part 3 va Task 2 uchun juda foydali: <i>People <b>used to</b> read "
                     "newspapers; now they scroll through feeds.</i></p>",
        "mistake":   "<p>❌ I am used to <u>live</u> here → ✅ I am used to <b>living</b> here "
                     "(ko‘nikkanman) · ❌ I used to <b>living</b> → ✅ I used to <b>live</b> "
                     "(ilgari yashardim).</p>",
        "examples": [
            ("Families used to spend their evenings together.",
             "Oilalar ilgari kechqurunlarini birga o‘tkazardi."),
            ("This area used to be farmland.",
             "Bu hudud ilgari qishloq xo‘jaligi yeri edi."),
        ],
        "synonyms": [
            ("would (past habit)", "used to = odat HAM, holat ham; would = faqat takrorlangan "
                                   "harakat (❌ would be farmland)"),
        ],
        "order": 111,
    },
    {
        "pattern":   "would (past habit)",
        "category":  "en_tense",
        "function":  "time",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "o‘tmishda takrorlangan harakat — «... qilib turardi»",
        "attach":    "S + would + V (yalang‘och)",
        "form_rule": "<b>would</b> + asosiy fe’l. Faqat <u>harakat</u> fe’llari bilan; "
                     "holat fe’llari (be, have, know) bilan <b>used to</b> ishlatiladi.",
        "note":      "<p>Speaking Part 2 (bolalik haqidagi kartochkalar) uchun tayyor vosita: "
                     "avval <i>used to</i> bilan fonni bering, keyin <i>would</i> bilan davom eting "
                     "— takrorlanish bo‘lmaydi va imtihon oluvchi buni sezadi.</p>",
        "mistake":   "<p>❌ My village <u>would be</u> very small → ✅ <b>used to be</b> — "
                     "holat fe’li bilan <i>would</i> ishlamaydi.</p>",
        "examples": [
            ("Every summer we would visit my grandparents in the village.",
             "Har yozda buvim va bobomnikiga qishloqqa borar edik."),
        ],
        "synonyms": [
            ("used to", "used to = ham odat, ham holat; would = faqat takrorlangan harakat"),
        ],
        "order": 112,
    },
    {
        "pattern":   "the tense of the chart (Task 1)",
        "category":  "en_tense",
        "function":  "time",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "Task 1 zamon tanlash qoidasi — sana o‘tganmi, hozirmi yoki bashoratmi",
        "attach":    "past simple / present simple / will + V",
        "form_rule": "<b>O‘tgan yillar</b> (1990-2010) → past simple · "
                     "<b>Sanasiz yoki hozirgi holat</b> → present simple · "
                     "<b>Kelajak, «projected», «forecast»</b> → will yoki be expected to · "
                     "<b>Jarayon diagrammasi</b> → present simple passive.",
        "note":      "<p>Bu alohida grammatika emas, <b>qoida</b> — lekin Task 1 da eng ko‘p ball "
                     "yo‘qotiladigan joy shu. Yozishdan oldin grafikning sanalariga qarang va "
                     "zamonni <u>bir marta</u> tanlab, butun matnda saqlang.</p>"
                     "<p>Aralash grafik (2000-2030) bo‘lsa: o‘tgan qismga past simple, "
                     "bashorat qismiga <i>is projected to</i> / <i>will</i>.</p>",
        "mistake":   "<p>❌ The graph <u>showed</u> … → ✅ The graph <b>shows</b> … — grafik "
                     "hozir ko‘rsatib turibdi, uning ma’lumoti esa o‘tmishda bo‘lishi mumkin.</p>",
        "examples": [
            ("The graph shows the changes that took place between 1980 and 2000.",
             "Grafik 1980-2000 yillarda ro‘y bergan o‘zgarishlarni ko‘rsatadi."),
            ("Consumption is projected to rise steadily until 2040.",
             "Iste’mol 2040-yilgacha barqaror o‘sishi kutilmoqda."),
        ],
        "synonyms": [
            ("past simple", "grafikdagi yillar o‘tgan bo‘lsa — past simple"),
            ("present perfect", "grafik bugungi kunga qadar davom etsa — present perfect"),
        ],
        "order": 113,
    },
]
