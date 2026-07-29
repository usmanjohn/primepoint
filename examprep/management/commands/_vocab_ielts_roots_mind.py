# -*- coding: utf-8 -*-
"""IELTS vocab bank — Root family 2: knowledge, speech & people.

Order decade 200-299. The roots behind the abstract nouns that fill Reading
passages: graph, dict, log, vis, cogn, gen. Self-contained (defines its own
roots), imported second — see toc_ielts_vocab.txt.
See STYLE_GUIDE_VOCAB_IELTS.md.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "Ingliz tili imtihoniga tayyorgarlik (Academic).",
    "icon":    "bi-globe2",
    "color":   "#059669",
}

ROOTS = [
    {
        "syllable": "graph",
        "hanja":    "graphein (yun.) — yozmoq",
        "meaning":  "yozmoq — chizmoq, tasvirlamoq",
        "note":     "<p>Yozuv va tasvir: <b>graph</b>ic, photo<b>graph</b>, bio<b>graph</b>y, "
                    "<b>graph</b>. Old qo‘shimcha mavzuni beradi: bio- (hayot), geo- (yer), "
                    "photo- (yorug‘lik).</p>",
        "order":    200,
    },
    {
        "syllable": "scrib/script",
        "hanja":    "scribere (lat.) — yozmoq",
        "meaning":  "yozmoq — qayd qilmoq",
        "note":     "<p>Fe’lda <b>-scribe</b>, otda <b>-scription</b>: describe → description, "
                    "prescribe → prescription, subscribe → subscription.</p>",
        "order":    201,
    },
    {
        "syllable": "dict",
        "hanja":    "dicere (lat.) — aytmoq",
        "meaning":  "aytmoq — so‘zlamoq, buyurmoq",
        "note":     "<p>pre<b>dict</b> (oldindan aytmoq), contra<b>dict</b> (qarshi aytmoq), "
                    "<b>dict</b>ionary, <b>dict</b>ator (buyuruvchi).</p>",
        "order":    202,
    },
    {
        "syllable": "log/logy",
        "hanja":    "logos (yun.) — so‘z, fan",
        "meaning":  "so‘z, fikr — fan, ta’limot",
        "note":     "<p><b>-logy</b> so‘ng qo‘shimchasi «... haqidagi fan» degani: "
                    "techno<b>logy</b>, eco<b>logy</b>, psycho<b>logy</b>, socio<b>logy</b>. "
                    "Mutaxassis — <b>-logist</b>.</p>",
        "order":    203,
    },
    {
        "syllable": "aud",
        "hanja":    "audire (lat.) — eshitmoq",
        "meaning":  "eshitmoq — tinglamoq",
        "note":     "<p><b>aud</b>ience (tinglovchilar), <b>aud</b>io, <b>aud</b>ible "
                    "(eshitiladigan), <b>aud</b>it (moliyaviy «tinglash» → tekshiruv).</p>",
        "order":    204,
    },
    {
        "syllable": "vid/vis",
        "hanja":    "videre (lat.) — ko‘rmoq",
        "meaning":  "ko‘rmoq — nazar solmoq",
        "note":     "<p>e<b>vid</b>ence (ko‘z oldidagi narsa → dalil), <b>vis</b>ible, "
                    "super<b>vis</b>e (ustidan qaramoq), re<b>vis</b>e (qayta ko‘rmoq).</p>",
        "order":    205,
    },
    {
        "syllable": "cogn/sci",
        "hanja":    "cognoscere / scire (lat.) — bilmoq",
        "meaning":  "bilmoq — anglamoq, tanimoq",
        "note":     "<p>re<b>cogn</b>ise (qayta tanimoq), <b>cogn</b>itive (bilish bilan bog‘liq), "
                    "<b>sci</b>ence, con<b>sci</b>ous (ongli).</p>",
        "order":    206,
    },
    {
        "syllable": "phon",
        "hanja":    "phone (yun.) — ovoz",
        "meaning":  "ovoz — tovush",
        "note":     "<p>tele<b>phon</b>e (uzoqdagi ovoz), <b>phon</b>etics, sym<b>phon</b>y "
                    "(ovozlarning uyg‘unligi).</p>",
        "order":    207,
    },
    {
        "syllable": "path",
        "hanja":    "pathos (yun.) — his, azob",
        "meaning":  "his-tuyg‘u — kasallik, azob",
        "note":     "<p>sym<b>path</b>y (birga his qilish), em<b>path</b>y (ichdan his qilish), "
                    "<b>path</b>ology. ⚠️ <i>path</i> (yo‘lak) so‘zi bilan aloqasi yo‘q.</p>",
        "order":    208,
    },
    {
        "syllable": "gen",
        "hanja":    "genus (lat.) — tug‘ilish, tur",
        "meaning":  "tug‘ilish — kelib chiqish, avlod, tur",
        "note":     "<p><b>gen</b>eration (avlod), <b>gen</b>etic, <b>gen</b>erate (yaratmoq), "
                    "indi<b>gen</b>ous (tub joyli).</p>",
        "order":    209,
    },
]

WORDS = [
    # ── graph / scrib ───────────────────────────────────────────────────────
    {
        "word":        "demographic",
        "hanja":       "demos (xalq) + graph + -ic",
        "roots":       ["graph"],
        "pos":         "adj",
        "topic":       "society",
        "level":       5,
        "freq":        2,
        "meaning":     "demografik — aholi tarkibiga oid",
        "collocation": "demographic change · demographic shift · an ageing demographic",
        "note":        "<p>«Xalqni yozish» — aholi statistikasi. <b>demographic change</b> "
                       "Task 2 da qarish, migratsiya va shaharlashuv mavzularining umumiy nomi.</p>",
        "examples":    [("Japan faces the most severe demographic challenges in the developed world.",
                         "Yaponiya rivojlangan dunyodagi eng og‘ir demografik muammolarga duch kelmoqda.")],
        "related":     [("urbanisation", "ikkalasi ham aholi o‘zgarishi haqida")],
    },
    {
        "word":        "describe",
        "hanja":       "de- + scribe",
        "roots":       ["scrib/script"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       2,
        "freq":        2,
        "meaning":     "tasvirlamoq, ta’riflamoq",
        "collocation": "describe a trend · as described above · a detailed description",
        "note":        "<p>Task 1 topshirig‘ining o‘zida turadi: <i>Summarise the information "
                       "and report the main features</i> — ya’ni <b>describe</b> qiling, "
                       "izohlamang.</p>",
        "examples":    [("The chart describes changes in household spending over two decades.",
                         "Diagramma ikki o‘n yillikdagi uy xarajatlari o‘zgarishini tasvirlaydi.")],
        "related":     [("illustrate", "describe = so‘z bilan tasvirlash; illustrate = misol/grafik bilan ko‘rsatish")],
    },
    {
        "word":        "illustrate",
        "hanja":       "il- + lustrare (yoritmoq)",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "ko‘rsatmoq, misol bilan yoritmoq",
        "collocation": "the graph illustrates · to illustrate this point · as illustrated by",
        "note":        "<p><b>Task 1 kirish jumlasi uchun eng qulay fe’l</b> — savoldagi "
                       "<i>shows</i> so‘zini takrorlamaslik uchun: <i>The bar chart "
                       "<b>illustrates</b> …</i> Muqobillar: <i>depicts, compares, gives "
                       "information about</i>.</p>",
        "examples":    [("The diagram illustrates the process by which glass is recycled.",
                         "Diagramma shishaning qayta ishlanish jarayonini ko‘rsatadi.")],
        "synonyms":    [("describe", "illustrate = ko‘rsatib beradi; describe = so‘z bilan tavsiflaydi")],
    },
    # ── dict ────────────────────────────────────────────────────────────────
    {
        "word":        "predict",
        "hanja":       "pre- + dict",
        "roots":       ["dict"],
        "pos":         "verb",
        "topic":       "data",
        "level":       3,
        "freq":        2,
        "meaning":     "oldindan aytmoq, bashorat qilmoq",
        "collocation": "predict a rise · as predicted · unpredictable",
        "note":        "<p>Sifati <b>predictable</b> (kutilgan) va <b>unpredictable</b> "
                       "(oldindan aytib bo‘lmaydigan) — ikkalasi ham Task 2 da foydali.</p>",
        "examples":    [("Economists predict that demand will slow over the next decade.",
                         "Iqtisodchilar keyingi o‘n yilda talab sekinlashishini bashorat qilmoqda.")],
        "synonyms":    [("forecast", "forecast = rasmiy, raqamli prognoz; predict = umumiy bashorat")],
    },
    {
        "word":        "contradict",
        "hanja":       "contra- + dict",
        "roots":       ["dict"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "zid kelmoq, rad etmoq — «qarshi aytmoq»",
        "collocation": "contradict the evidence · a contradiction · contradictory findings",
        "note":        "<p>Bahsli dalillarni taqqoslashda: <i>These results <b>contradict</b> "
                       "earlier studies.</i> Oti — <b>contradiction</b>.</p>",
        "examples":    [("The latest data contradict the assumption that rural incomes are falling.",
                         "So‘nggi ma’lumotlar qishloq daromadlari kamayyapti degan taxminga zid keladi.")],
        "antonyms":    [("support", "contradict = zid kelmoq; support = tasdiqlamoq")],
    },
    # ── log/logy ────────────────────────────────────────────────────────────
    {
        "word":        "technology",
        "hanja":       "techne (hunar) + -logy",
        "roots":       ["log/logy"],
        "pos":         "noun",
        "topic":       "science",
        "level":       2,
        "freq":        3,
        "meaning":     "texnologiya — texnik bilim va vositalar",
        "collocation": "advances in technology · technological change · digital technology",
        "note":        "<p>⚠️ Odatda <b>sanalmaydigan</b>: ❌ <i>technologies are…</i> emas, "
                       "✅ <i>technology <b>is</b>…</i> (aniq turlari haqida gapirilsa "
                       "<i>technologies</i> ham bo‘ladi). Sifati — <b>technological</b>.</p>",
        "examples":    [("Rapid advances in technology have transformed the workplace.",
                         "Texnologiyadagi jadal yutuqlar ish joyini tubdan o‘zgartirdi.")],
        "related":     [("innovation", "technology = vosita; innovation = yangilik joriy etish")],
    },
    {
        "word":        "psychological",
        "hanja":       "psyche (ruh) + -logy + -ical",
        "roots":       ["log/logy"],
        "pos":         "adj",
        "topic":       "health",
        "level":       5,
        "freq":        2,
        "meaning":     "psixologik — ruhiy holat bilan bog‘liq",
        "collocation": "psychological effects · psychological wellbeing · mental health",
        "note":        "<p>Sog‘liq va ta’lim mavzularida jismoniy va ruhiy tomonni ajratish "
                       "uchun: <i>the <b>psychological</b> as well as physical benefits of "
                       "exercise</i>.</p>",
        "examples":    [("Long working hours can have serious psychological effects.",
                         "Uzoq ish soatlari jiddiy psixologik oqibatlarga olib kelishi mumkin.")],
        "related":     [("wellbeing", "wellbeing = umumiy farovonlik holati")],
    },
    # ── aud ─────────────────────────────────────────────────────────────────
    {
        "word":        "audience",
        "hanja":       "aud + -ience",
        "roots":       ["aud"],
        "pos":         "noun",
        "topic":       "media",
        "level":       3,
        "freq":        2,
        "meaning":     "tomoshabinlar, tinglovchilar, auditoriya",
        "collocation": "a wide audience · reach an audience · target audience",
        "note":        "<p>Yaxlit ot: fe’l ham birlikda, ham ko‘plikda kelishi mumkin, lekin "
                       "imtihonda <b>birlik</b> xavfsizroq: <i>The audience <b>was</b> larger "
                       "than expected.</i></p>",
        "examples":    [("Streaming platforms have given independent films a global audience.",
                         "Strimning platformalari mustaqil filmlarga global auditoriya berdi.")],
        "related":     [("spectator", "audience = tinglovchi/tomoshabin jamoasi; spectator = alohida odam")],
    },
    # ── vid/vis ─────────────────────────────────────────────────────────────
    {
        "word":        "evidence",
        "hanja":       "e- + vid + -ence",
        "roots":       ["vid/vis"],
        "pos":         "noun",
        "topic":       "academic",
        "level":       4,
        "freq":        3,
        "meaning":     "dalil, isbot — «ko‘z oldida turgan narsa»",
        "collocation": "strong evidence · there is little evidence · evidence suggests",
        "note":        "<p>⚠️ <b>Sanalmaydigan ot</b>: ❌ <i>an evidence</i>, ❌ <i>evidences</i> → "
                       "✅ <i><b>a piece of</b> evidence</i>, <i><b>much</b> evidence</i>. "
                       "Task 2 da dalilni kiritishning eng akademik yo‘li: "
                       "<i>There is <b>growing evidence that</b>…</i></p>",
        "examples":    [("There is little evidence that stricter penalties reduce crime.",
                         "Qattiqroq jazolar jinoyatchilikni kamaytirishiga dalil kam."),
                        ("Recent evidence suggests a link between air quality and school performance.",
                         "So‘nggi dalillar havo sifati bilan o‘quv natijalari orasida bog‘liqlik borligini ko‘rsatadi.")],
        "related":     [("visible", "bir ildiz — «ko‘rmoq» dan")],
    },
    {
        "word":        "visible",
        "hanja":       "vis + -ible",
        "roots":       ["vid/vis"],
        "pos":         "adj",
        "topic":       "academic",
        "level":       3,
        "freq":        1,
        "meaning":     "ko‘rinadigan, sezilarli",
        "collocation": "clearly visible · a visible improvement · visibility",
        "note":        "<p>Task 1 da tendensiyani izohlashda: <i>a <b>visible</b> upward trend</i>. "
                       "Teskarisi — <b>invisible</b>.</p>",
        "examples":    [("The effects of the policy became visible within two years.",
                         "Siyosatning ta’siri ikki yil ichida ko‘zga tashlana boshladi.")],
        "related":     [("evidence", "bir ildiz — «ko‘rmoq»")],
    },
    {
        "word":        "supervise",
        "hanja":       "super- + vis",
        "roots":       ["vid/vis"],
        "pos":         "verb",
        "topic":       "work",
        "level":       5,
        "freq":        1,
        "meaning":     "nazorat qilmoq — ustidan qarab turmoq",
        "collocation": "supervise students · under supervision · a supervisor",
        "note":        "<p>Bolalar va texnologiya mavzusida kerak: <i>children should be "
                       "<b>supervised</b> online</i>. Oti — <b>supervision</b>.</p>",
        "examples":    [("Young children should be supervised when using the internet.",
                         "Yosh bolalar internetdan foydalanayotganda nazorat ostida bo‘lishi kerak.")],
        "synonyms":    [("monitor", "monitor = muntazam kuzatib borish; supervise = mas’ul bo‘lib qarash")],
    },
    {
        "word":        "monitor",
        "hanja":       "monere (lat.) — ogohlantirmoq",
        "roots":       [],
        "pos":         "verb",
        "topic":       "science",
        "level":       4,
        "freq":        2,
        "meaning":     "kuzatib bormoq — muntazam nazorat qilmoq",
        "collocation": "monitor progress · closely monitored · monitoring systems",
        "note":        "<p>Ekologiya va texnologiya mavzularida: <i><b>monitor</b> air quality</i>, "
                       "<i><b>monitor</b> employees</i> — ikkinchisi maxfiylik bahsini ochadi.</p>",
        "examples":    [("Satellites monitor deforestation in real time.",
                         "Sun’iy yo‘ldoshlar o‘rmon kesilishini real vaqtda kuzatib boradi.")],
        "synonyms":    [("supervise", "supervise = odamlarga mas’ullik; monitor = holatni kuzatish")],
    },
    # ── cogn/sci ────────────────────────────────────────────────────────────
    {
        "word":        "cognitive",
        "hanja":       "cogn + -itive",
        "roots":       ["cogn/sci"],
        "pos":         "adj",
        "topic":       "school",
        "level":       6,
        "freq":        2,
        "meaning":     "kognitiv — bilish, fikrlash jarayonlariga oid",
        "collocation": "cognitive development · cognitive skills · cognitive decline",
        "note":        "<p>Ta’lim va sog‘liq mavzularida band-7 so‘zi: <i>early bilingualism "
                       "supports <b>cognitive development</b></i>, <i><b>cognitive decline</b> "
                       "in old age</i>.</p>",
        "examples":    [("Reading regularly is linked to stronger cognitive skills in later life.",
                         "Muntazam o‘qish keyingi hayotda kuchliroq kognitiv ko‘nikmalar bilan bog‘liq.")],
        "related":     [("recognise", "bir ildiz — «bilmoq» dan")],
    },
    {
        "word":        "recognise",
        "hanja":       "re- + cogn + -ise",
        "roots":       ["cogn/sci"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       3,
        "freq":        2,
        "meaning":     "tan olmoq; tanimoq",
        "collocation": "widely recognised · recognise the importance of · recognition",
        "note":        "<p>Britaniya imlosi <b>-ise</b>, amerikacha <b>-ize</b> — imtihonda "
                       "bittasini tanlab, oxirigacha shuni saqlang. Oti — <b>recognition</b>.</p>",
        "examples":    [("Governments increasingly recognise the value of vocational training.",
                         "Hukumatlar kasbiy ta’limning qadrini tobora ko‘proq tan olmoqda.")],
        "related":     [("cognitive", "bir ildiz — «bilmoq»")],
    },
    # ── path ────────────────────────────────────────────────────────────────
    {
        "word":        "empathy",
        "hanja":       "em- + path + -y",
        "roots":       ["path"],
        "pos":         "noun",
        "topic":       "person",
        "level":       5,
        "freq":        1,
        "meaning":     "hamdardlik, o‘zgani his qila olish",
        "collocation": "develop empathy · a lack of empathy · empathetic",
        "note":        "<p>Ta’lim mavzusida: adabiyot va san’at nima beradi degan savolga eng "
                       "yaxshi javob — <i>reading fiction develops <b>empathy</b></i>.</p>",
        "examples":    [("Studying literature helps young people develop empathy.",
                         "Adabiyot o‘qish yoshlarda hamdardlik tuyg‘usini rivojlantiradi.")],
        "synonyms":    [("sympathy", "sympathy = achinish, birovga rahm; empathy = uning o‘rnida "
                                     "his qila olish")],
    },
    # ── gen ─────────────────────────────────────────────────────────────────
    {
        "word":        "generate",
        "hanja":       "gen + -ate",
        "roots":       ["gen"],
        "pos":         "verb",
        "topic":       "economy",
        "level":       4,
        "freq":        3,
        "meaning":     "hosil qilmoq, keltirib chiqarmoq (daromad, energiya, ish o‘rni)",
        "collocation": "generate income · generate electricity · generate employment",
        "note":        "<p>Task 2 yechim qismida <i>create</i> ning akademik o‘rinbosari: "
                       "<i>Tourism <b>generates</b> substantial revenue for local communities.</i></p>",
        "examples":    [("Wind farms now generate a fifth of the country’s electricity.",
                         "Shamol elektr stansiyalari hozir mamlakat elektr energiyasining beshdan birini ishlab chiqaradi.")],
        "related":     [("generation", "bir ildiz — «tug‘ilish» dan")],
    },
    {
        "word":        "generation",
        "hanja":       "gen + -ation",
        "roots":       ["gen"],
        "pos":         "noun",
        "topic":       "society",
        "level":       3,
        "freq":        3,
        "meaning":     "avlod — bir vaqtda tug‘ilgan odamlar guruhi",
        "collocation": "the younger generation · from generation to generation · generation gap",
        "note":        "<p><b>the generation gap</b> — avlodlar orasidagi tafovut: oila va "
                       "texnologiya mavzularida tayyor ibora.</p>",
        "examples":    [("Traditional skills are passed from one generation to the next.",
                         "An’anaviy hunarlar bir avloddan ikkinchisiga o‘tadi.")],
        "related":     [("generate", "bir ildiz — «tug‘ilish, hosil bo‘lish»")],
    },
    {
        "word":        "indigenous",
        "hanja":       "indi- + gen + -ous",
        "roots":       ["gen"],
        "pos":         "adj",
        "topic":       "culture",
        "level":       6,
        "freq":        1,
        "meaning":     "tub joyli, mahalliy — o‘sha yerda tug‘ilgan",
        "collocation": "indigenous people · indigenous languages · indigenous species",
        "note":        "<p>Madaniyat va ekologiya mavzularida: <i><b>indigenous</b> languages "
                       "are disappearing</i>, <i><b>indigenous</b> species</i> (mahalliy turlar).</p>",
        "examples":    [("Many indigenous languages are at risk of disappearing within a generation.",
                         "Ko‘p tub joyli tillar bir avlod ichida yo‘q bo‘lib ketish xavfi ostida.")],
        "antonyms":    [("foreign", "indigenous = tub joyli; foreign = chetdan kelgan")],
    },
    {
        "word":        "phenomenon",
        "hanja":       "phainomenon (yun.) — ko‘rinadigan narsa",
        "roots":       [],
        "pos":         "noun",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "hodisa — kuzatiladigan voqelik",
        "collocation": "a global phenomenon · a recent phenomenon · this phenomenon",
        "note":        "<p>⚠️ <b>Ko‘pligi noto‘g‘ri yasaladi:</b> one <i>phenomenon</i> → "
                       "two <b>phenomena</b> (❌ phenomenons). Ishora oti sifatida juda foydali: "
                       "<i>This <b>phenomenon</b> is not confined to developing countries.</i></p>",
        "examples":    [("Remote working is no longer a temporary phenomenon.",
                         "Masofaviy ish endi vaqtinchalik hodisa emas.")],
        "related":     [("trend", "trend = uzoq davom etadigan yo‘nalish; phenomenon = hodisaning o‘zi")],
    },
    {
        "word":        "concept",
        "hanja":       "con- + cept (olmoq)",
        "roots":       [],
        "pos":         "noun",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "tushuncha, g‘oya",
        "collocation": "the concept of · a difficult concept · conceptual",
        "note":        "<p>Mavhum mavzuni kiritishning oson yo‘li: <i>The <b>concept of</b> "
                       "work-life balance is relatively new.</i></p>",
        "examples":    [("The concept of lifelong learning has gained ground in recent decades.",
                         "Umrbod o‘rganish tushunchasi so‘nggi o‘n yilliklarda ommalashdi.")],
        "synonyms":    [("notion", "notion = qarash, taxmin (biroz shubha ohangi); concept = "
                                   "aniq shakllangan tushuncha")],
    },
    {
        "word":        "phonetic",
        "hanja":       "phon + -etic",
        "roots":       ["phon"],
        "pos":         "adj",
        "topic":       "academic",
        "level":       5,
        "freq":        1,
        "meaning":     "fonetik — nutq tovushlariga oid",
        "collocation": "the phonetic alphabet · phonetic transcription · phonetics",
        "note":        "<p>Speaking uchun amaliy foyda: lug‘atdagi <b>phonetic transcription</b> "
                       "(/ˈdetəmɪn/ kabi yozuv) urg‘uni ko‘rsatadi, urg‘u esa Pronunciation "
                       "bahosining bir qismi. Yangi so‘zni yozib olayotganda transkripsiyasini "
                       "ham ko‘chiring.</p>",
        "examples":    [("Learning the phonetic alphabet helps students place word stress correctly.",
                         "Fonetik alifboni o‘rganish talabalarga so‘z urg‘usini to‘g‘ri qo‘yishga yordam beradi.")],
        "related":     [("audience", "bir soha: phon = ovoz chiqarish, aud = uni eshitish")],
    },
    {
        "word":        "criteria",
        "hanja":       "kriterion (yun.) — o‘lchov",
        "roots":       [],
        "pos":         "noun",
        "topic":       "academic",
        "level":       5,
        "freq":        1,
        "meaning":     "mezonlar — baholash o‘lchovlari",
        "collocation": "meet the criteria · selection criteria · a key criterion",
        "note":        "<p>⚠️ <b>criteria</b> — KO‘PLIK; birligi <b>criterion</b>. "
                       "❌ <i>an important criteria</i> → ✅ <i>an important <b>criterion</b></i>.</p>",
        "examples":    [("Universities should not rely on examination results as the sole criterion.",
                         "Universitetlar imtihon natijalarini yagona mezon sifatida olmasligi kerak.")],
        "related":     [("phenomenon", "ikkalasi ham noto‘g‘ri ko‘plik yasaydi: criteria, phenomena")],
    },
]


# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 200 + _i)
