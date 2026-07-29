# -*- coding: utf-8 -*-
"""IELTS vocab bank — Root family 1: action & direction (harakat o'zaklari).

Order decade 100-199. The English answer to Hanja: ten Latin roots of motion
and transfer that between them build several hundred academic words. Learn
`spect` once and inspect / spectator / perspective / prospect stop being four
separate words.

⚠️ Import order: this file is FIRST and self-contained — see toc_ielts_vocab.txt.
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
        "syllable": "spect",
        "hanja":    "specere (lat.) — qaramoq",
        "meaning":  "qaramoq — ko‘rmoq, kuzatmoq",
        "note":     "<p>Old qo‘shimcha qarash yo‘nalishini belgilaydi: <b>in-</b> (ichiga) → "
                    "inspect, <b>pro-</b> (oldinga) → prospect, <b>retro-</b> (orqaga) → "
                    "retrospective, <b>per-</b> (orqali) → perspective.</p>",
        "order":    100,
    },
    {
        "syllable": "duc/duct",
        "hanja":    "ducere (lat.) — yetaklamoq",
        "meaning":  "yetaklamoq — olib bormoq, boshqarmoq",
        "note":     "<p>Ikki xil yoziladi: fe’llarda ko‘pincha <b>-duce</b> (introduce, reduce), "
                    "ot va sifatlarda <b>-duct</b> (conduct, production).</p>",
        "order":    101,
    },
    {
        "syllable": "port",
        "hanja":    "portare (lat.) — tashimoq",
        "meaning":  "tashimoq — olib yurmoq, ko‘tarmoq",
        "note":     "<p>Jismoniy tashish (transport, export) dan mavhum «ko‘tarish» ga o‘tadi: "
                    "sup<b>port</b> = «ostidan ko‘tarmoq» → qo‘llab-quvvatlamoq.</p>",
        "order":    102,
    },
    {
        "syllable": "mit/miss",
        "hanja":    "mittere (lat.) — yubormoq",
        "meaning":  "yubormoq — jo‘natmoq, qo‘yib yubormoq",
        "note":     "<p>Fe’lda <b>-mit</b>, otda <b>-mission</b>: emit → emission, "
                    "transmit → transmission, permit → permission.</p>",
        "order":    103,
    },
    {
        "syllable": "ject",
        "hanja":    "iacere (lat.) — otmoq",
        "meaning":  "otmoq — irg‘itmoq, tashlamoq",
        "note":     "<p>Yo‘nalish old qo‘shimchada: <b>re-</b> (orqaga) → reject (rad etmoq), "
                    "<b>pro-</b> (oldinga) → project (loyiha, prognoz), <b>ob-</b> (qarshi) → "
                    "object (e’tiroz bildirmoq).</p>",
        "order":    104,
    },
    {
        "syllable": "tract",
        "hanja":    "trahere (lat.) — tortmoq",
        "meaning":  "tortmoq — sudramoq, cho‘zmoq",
        "note":     "<p>at<b>tract</b> (o‘ziga tortmoq), ex<b>tract</b> (tortib olmoq), "
                    "con<b>tract</b> (birga tortmoq → shartnoma; qisqarmoq), "
                    "dis<b>tract</b> (chalg‘itmoq).</p>",
        "order":    105,
    },
    {
        "syllable": "vert/vers",
        "hanja":    "vertere (lat.) — burmoq",
        "meaning":  "burmoq — aylantirmoq, o‘girmoq",
        "note":     "<p>Fe’lda <b>-vert</b>, ot va sifatda <b>-vers</b>: convert → conversion, "
                    "divert → diversion, reverse, adverse, versatile.</p>",
        "order":    106,
    },
    {
        "syllable": "ced/cess",
        "hanja":    "cedere (lat.) — yurmoq, chekinmoq",
        "meaning":  "yurmoq — bormoq, o‘tmoq",
        "note":     "<p>pro<b>ceed</b> (davom etmoq), ex<b>ceed</b> (oshib ketmoq), "
                    "ac<b>cess</b> (kirish), pro<b>cess</b> (jarayon), re<b>cession</b> "
                    "(«orqaga yurish» → tanazzul).</p>",
        "order":    107,
    },
    {
        "syllable": "fer",
        "hanja":    "ferre (lat.) — olib kelmoq",
        "meaning":  "olib kelmoq — ko‘chirmoq, keltirmoq",
        "note":     "<p>trans<b>fer</b> (ko‘chirmoq), in<b>fer</b> (xulosa chiqarmoq — "
                    "«fikrni olib kelmoq»), re<b>fer</b> (murojaat qilmoq), "
                    "dif<b>fer</b>ence (farq).</p>",
        "order":    108,
    },
    {
        "syllable": "pel/puls",
        "hanja":    "pellere (lat.) — turtmoq",
        "meaning":  "turtmoq — haydamoq, itarmoq",
        "note":     "<p>com<b>pel</b> (majburlamoq), ex<b>pel</b> (haydab chiqarmoq), "
                    "im<b>puls</b>e (turtki), com<b>puls</b>ory (majburiy), "
                    "re<b>puls</b>ive (jirkanch).</p>",
        "order":    109,
    },
]

WORDS = [
    # ── spect ───────────────────────────────────────────────────────────────
    {
        "word":        "perspective",
        "hanja":       "per- + spect + -ive",
        "roots":       ["spect"],
        "pos":         "noun",
        "topic":       "academic",
        "level":       4,
        "freq":        3,
        "meaning":     "nuqtai nazar — qarash burchagi",
        "collocation": "from a different perspective · a global perspective · put into perspective",
        "note":        "<p>«Orqali qarash» — <b>per-</b> (orqali) + <b>spect</b> (qarash). "
                       "Task 2 da <i>opinion</i> so‘zining eng yaxshi o‘rinbosari: "
                       "<i>from an economic <b>perspective</b></i>.</p>",
        "examples":    [("From an environmental perspective, the policy is difficult to justify.",
                         "Ekologik nuqtai nazardan bu siyosatni oqlash qiyin.")],
        "synonyms":    [("viewpoint", "viewpoint = shaxsning qarashi; perspective = butun bir "
                                      "yo‘nalish yoki soha nuqtai nazari")],
        "related":     [("prospect", "bir ildiz: perspective = qarash burchagi; prospect = istiqbol")],
    },
    {
        "word":        "prospect",
        "hanja":       "pro- + spect",
        "roots":       ["spect"],
        "pos":         "noun",
        "topic":       "work",
        "level":       4,
        "freq":        2,
        "meaning":     "istiqbol — kelajakdagi imkoniyat, «oldinga qarash»",
        "collocation": "career prospects · the prospect of · prospects for growth",
        "note":        "<p>Ko‘plikda (<b>prospects</b>) = kelajakdagi imkoniyatlar, ayniqsa ish "
                       "sohasida: <i>job <b>prospects</b></i>. Sifati <b>prospective</b> "
                       "(bo‘lg‘usi): <i>prospective students</i>.</p>",
        "examples":    [("A degree no longer guarantees good career prospects.",
                         "Diplom endi yaxshi martaba istiqbolini kafolatlamaydi.")],
        "related":     [("perspective", "bir ildiz, boshqa ma’no — chalkashtirmang")],
    },
    {
        "word":        "spectator",
        "hanja":       "spect + -ator",
        "roots":       ["spect"],
        "pos":         "noun",
        "topic":       "culture",
        "level":       3,
        "freq":        1,
        "meaning":     "tomoshabin — qarab turuvchi",
        "collocation": "spectator sport · thousands of spectators",
        "note":        "<p><b>spectator sport</b> — o‘ynaladigan emas, tomosha qilinadigan sport: "
                       "Speaking Part 3 da sport mavzusida foydali.</p>",
        "examples":    [("Football remains the most popular spectator sport worldwide.",
                         "Futbol dunyodagi eng ommabop tomoshabop sport bo‘lib qolmoqda.")],
        "synonyms":    [("audience", "audience = tinglovchi/tomoshabin jamoasi (yaxlit); "
                                     "spectator = alohida tomoshabin")],
    },
    {
        "word":        "inspect",
        "hanja":       "in- + spect",
        "roots":       ["spect"],
        "pos":         "verb",
        "topic":       "work",
        "level":       4,
        "freq":        2,
        "meaning":     "sinchiklab tekshirmoq, ko‘zdan kechirmoq",
        "collocation": "inspect a site · a routine inspection · a health inspector",
        "note":        "<p>Rasmiy, qoidaga muvofiqlikni tekshirish. Oti — <b>inspection</b>, "
                       "kasbi — <b>inspector</b>.</p>",
        "examples":    [("Officials inspect food factories at least twice a year.",
                         "Rasmiylar oziq-ovqat zavodlarini yiliga kamida ikki marta tekshiradi.")],
        "synonyms":    [("examine", "examine = umumiy o‘rganish/tekshirish; inspect = rasmiy nazorat")],
    },
    # ── duc/duct ────────────────────────────────────────────────────────────
    {
        "word":        "conduct",
        "hanja":       "con- + duct",
        "roots":       ["duc/duct"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       4,
        "freq":        3,
        "meaning":     "o‘tkazmoq (tadqiqot, so‘rov) — «birga yetaklamoq»",
        "collocation": "conduct research · conduct a survey · conduct an experiment",
        "note":        "<p>Akademik yozuvda <i>do a research</i> ❌ o‘rniga aynan shu ishlatiladi: "
                       "<b>conduct research</b> ✅. Ot sifatida urg‘u o‘zgaradi: "
                       "<i>CONduct</i> = xulq-atvor.</p>",
        "examples":    [("The study was conducted over a period of five years.",
                         "Tadqiqot besh yil davomida o‘tkazildi.")],
        "related":     [("productivity", "bir ildiz: conduct = olib bormoq; produce = ishlab chiqarmoq")],
    },
    {
        "word":        "productivity",
        "hanja":       "pro- + duct + -ivity",
        "roots":       ["duc/duct"],
        "pos":         "noun",
        "topic":       "economy",
        "level":       4,
        "freq":        3,
        "meaning":     "unumdorlik — mehnat samaradorligi",
        "collocation": "boost productivity · a rise in productivity · labour productivity",
        "note":        "<p>Task 2 da ish va iqtisod mavzusining kalit so‘zi: <i>flexible working "
                       "hours can <b>boost productivity</b></i>. Sifati — <b>productive</b>.</p>",
        "examples":    [("Remote work has been shown to increase productivity in some sectors.",
                         "Masofaviy ish ba’zi sohalarda unumdorlikni oshirishi ko‘rsatilgan.")],
        "related":     [("conduct", "bir ildiz — «yetaklamoq» ma’nosidan")],
    },
    {
        "word":        "reduce",
        "hanja":       "re- + duce",
        "roots":       ["duc/duct"],
        "pos":         "verb",
        "topic":       "data",
        "level":       2,
        "freq":        3,
        "meaning":     "kamaytirmoq — «orqaga yetaklamoq»",
        "collocation": "reduce emissions · a sharp reduction · reduce costs by 20%",
        "note":        "<p>Task 1 va Task 2 ning eng ko‘p kerak bo‘ladigan fe’li. Oti — "
                       "<b>reduction</b> (<i>a significant reduction <b>in</b> waste</i>).</p>",
        "examples":    [("Congestion charges have reduced traffic in the city centre by a third.",
                         "Tirbandlik yig‘imlari shahar markazidagi transport oqimini uchdan birga kamaytirdi.")],
        "antonyms":    [("increase", "reduce = kamaytirmoq; increase = ko‘paytirmoq")],
    },
    # ── port ────────────────────────────────────────────────────────────────
    {
        "word":        "sustainable",
        "hanja":       "sus- (ostidan) + tain (ushlamoq)",
        "roots":       [],
        "pos":         "adj",
        "topic":       "environment",
        "level":       4,
        "freq":        3,
        "meaning":     "barqaror — uzoq muddat davom etadigan, tabiatga zarar bermaydigan",
        "collocation": "sustainable development · sustainable energy · environmentally sustainable",
        "note":        "<p>Ekologiya mavzusining eng markaziy so‘zi. Oti — <b>sustainability</b>, "
                       "teskarisi — <b>unsustainable</b>. Ikkinchi ma’nosi ham bor: "
                       "«iqtisodiy jihatdan davom ettirib bo‘ladigan».</p>",
        "examples":    [("Cities must find sustainable ways of managing waste.",
                         "Shaharlar chiqindini boshqarishning barqaror yo‘llarini topishi kerak.")],
        "antonyms":    [("unsustainable", "un- old qo‘shimchasi ma’noni teskari qiladi")],
    },
    {
        "word":        "export",
        "hanja":       "ex- + port",
        "roots":       ["port"],
        "pos":         "noun",
        "topic":       "economy",
        "level":       3,
        "freq":        2,
        "meaning":     "eksport — tashqariga sotish, «tashqariga tashish»",
        "collocation": "export earnings · exports rose · a major exporter of",
        "note":        "<p>Ot va fe’l urg‘usi farq qiladi: <i>EXport</i> (ot) — <i>exPORT</i> "
                       "(fe’l). Task 1 diagrammalarida tez-tez uchraydi.</p>",
        "examples":    [("Oil exports accounted for nearly half of the country’s revenue.",
                         "Neft eksporti mamlakat daromadining deyarli yarmini tashkil qildi.")],
        "antonyms":    [("import", "ex- = tashqariga; im- = ichkariga")],
    },
    {
        "word":        "import",
        "hanja":       "im- + port",
        "roots":       ["port"],
        "pos":         "noun",
        "topic":       "economy",
        "level":       3,
        "freq":        2,
        "meaning":     "import — chetdan olib kirish",
        "collocation": "import tariffs · rely on imports · imported goods",
        "note":        "<p><b>rely on imports</b> — Task 2 da oziq-ovqat xavfsizligi va energiya "
                       "mavzularida kerak bo‘ladigan birikma.</p>",
        "examples":    [("The country still relies heavily on imported energy.",
                         "Mamlakat hamon chetdan keltirilgan energiyaga qattiq tayanadi.")],
        "antonyms":    [("export", "im- = ichkariga; ex- = tashqariga")],
    },
    {
        "word":        "support",
        "hanja":       "sup- + port",
        "roots":       ["port"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       3,
        "freq":        3,
        "meaning":     "qo‘llab-quvvatlamoq; dalil bilan tasdiqlamoq",
        "collocation": "support an argument · financial support · evidence supports",
        "note":        "<p>«Ostidan ko‘tarmoq» ma’nosidan. Akademik yozuvda ikkinchi ma’nosi "
                       "muhimroq: <i>These findings <b>support</b> the view that…</i></p>",
        "examples":    [("Recent data support the claim that remote work reduces commuting.",
                         "So‘nggi ma’lumotlar masofaviy ish qatnovni kamaytiradi degan fikrni tasdiqlaydi.")],
        "synonyms":    [("advocate", "support = umumiy qo‘llash; advocate = ochiq targ‘ib qilish")],
    },
    # ── mit/miss ────────────────────────────────────────────────────────────
    {
        "word":        "emission",
        "hanja":       "e- + miss + -ion",
        "roots":       ["mit/miss"],
        "pos":         "noun",
        "topic":       "environment",
        "level":       4,
        "freq":        3,
        "meaning":     "chiqindi gaz, emissiya — «tashqariga yuborish»",
        "collocation": "carbon emissions · cut emissions · greenhouse gas emissions",
        "note":        "<p>Deyarli doim ko‘plikda: <b>emissions</b>. Ekologiya inshosining "
                       "birinchi darajali so‘zi — <i>reduce/cut/curb <b>emissions</b></i>.</p>",
        "examples":    [("The country pledged to halve its carbon emissions by 2035.",
                         "Mamlakat 2035-yilga qadar uglerod chiqindilarini ikki barobar qisqartirishga va’da berdi.")],
        "related":     [("transmit", "bir ildiz: emit = tashqariga yubormoq; transmit = uzatmoq")],
    },
    {
        "word":        "transmit",
        "hanja":       "trans- + mit",
        "roots":       ["mit/miss"],
        "pos":         "verb",
        "topic":       "science",
        "level":       5,
        "freq":        1,
        "meaning":     "uzatmoq — bir joydan boshqasiga yubormoq (signal, kasallik, bilim)",
        "collocation": "transmit data · transmit a disease · transmission of knowledge",
        "note":        "<p>Uch sohada ishlaydi: texnologiya (<i>transmit data</i>), tibbiyot "
                       "(<i>transmitted through contact</i>) va madaniyat "
                       "(<i>transmit traditions to the next generation</i>).</p>",
        "examples":    [("Traditions are transmitted from one generation to the next.",
                         "An’analar bir avloddan ikkinchisiga o‘tkaziladi.")],
        "related":     [("emission", "bir ildiz — «yubormoq»")],
    },
    # ── ject ────────────────────────────────────────────────────────────────
    {
        "word":        "project",
        "hanja":       "pro- + ject",
        "roots":       ["ject"],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "prognoz qilmoq — «oldinga tashlamoq»",
        "collocation": "projected to rise · projected figures · population projections",
        "note":        "<p><b>Task 1 uchun juda muhim:</b> grafik kelajakni ko‘rsatsa, "
                       "<i>is <b>projected to</b> reach…</i> deb yozing. Ot sifatida urg‘u "
                       "boshqa: <i>PROject</i> = loyiha.</p>",
        "examples":    [("The urban population is projected to double by 2050.",
                         "Shahar aholisi 2050-yilga borib ikki baravar ko‘payishi prognoz qilinmoqda.")],
        "synonyms":    [("forecast", "forecast = rasmiy bashorat (ob-havo, iqtisod); "
                                     "project = mavjud tendensiyani davom ettirib hisoblash")],
    },
    {
        "word":        "reject",
        "hanja":       "re- + ject",
        "roots":       ["ject"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       3,
        "freq":        2,
        "meaning":     "rad etmoq — «orqaga otmoq»",
        "collocation": "reject a proposal · reject the argument · outright rejection",
        "note":        "<p>Task 2 da qarshi fikrni rad etish uchun: <i>This argument should be "
                       "<b>rejected</b> on two grounds.</i></p>",
        "examples":    [("Parliament rejected the proposal by a narrow margin.",
                         "Parlament taklifni oz farq bilan rad etdi.")],
        "antonyms":    [("advocate", "reject = rad etmoq; advocate = yoqlamoq")],
    },
    # ── tract ───────────────────────────────────────────────────────────────
    {
        "word":        "attract",
        "hanja":       "at- + tract",
        "roots":       ["tract"],
        "pos":         "verb",
        "topic":       "tourism",
        "level":       3,
        "freq":        2,
        "meaning":     "jalb qilmoq — o‘ziga tortmoq",
        "collocation": "attract tourists · attract investment · a major attraction",
        "note":        "<p>Turizm va iqtisod mavzularida kerak: <i><b>attract</b> foreign "
                       "investment</i>. Oti — <b>attraction</b>, sifati — <b>attractive</b>.</p>",
        "examples":    [("The city attracts millions of visitors every summer.",
                         "Shahar har yozda millionlab tashrif buyuruvchini jalb qiladi.")],
        "related":     [("extract", "bir ildiz: attract = o‘ziga tortmoq; extract = tortib olmoq")],
    },
    {
        "word":        "extract",
        "hanja":       "ex- + tract",
        "roots":       ["tract"],
        "pos":         "verb",
        "topic":       "science",
        "level":       5,
        "freq":        1,
        "meaning":     "qazib olmoq, ajratib olmoq — «tashqariga tortmoq»",
        "collocation": "extract minerals · extract data · extraction of resources",
        "note":        "<p>Tabiiy resurslar mavzusida: <i><b>extract</b> fossil fuels</i>. "
                       "Reading’da esa matndan ma’lumot «ajratib olish» ma’nosida uchraydi.</p>",
        "examples":    [("Extracting minerals on this scale damages fragile ecosystems.",
                         "Bunday miqyosda qazilma qazib olish nozik ekotizimlarga zarar yetkazadi.")],
        "related":     [("attract", "bir ildiz — «tortmoq»")],
    },
    # ── vert/vers ───────────────────────────────────────────────────────────
    {
        "word":        "convert",
        "hanja":       "con- + vert",
        "roots":       ["vert/vers"],
        "pos":         "verb",
        "topic":       "science",
        "level":       4,
        "freq":        2,
        "meaning":     "aylantirmoq — bir holatdan boshqasiga o‘tkazmoq",
        "collocation": "convert waste into energy · convert land · the conversion of",
        "note":        "<p>Ekologiya diagrammalarida ko‘p uchraydi: <i>waste is <b>converted "
                       "into</b> biogas</i>. Predlogi — <b>into</b>.</p>",
        "examples":    [("Farmland is increasingly being converted into housing.",
                         "Ekin maydonlari tobora ko‘proq uy-joyga aylantirilmoqda.")],
        "related":     [("diverse", "bir ildiz — «burmoq» dan: diverse = turli tomonga burilgan")],
    },
    {
        "word":        "diverse",
        "hanja":       "di- + vers",
        "roots":       ["vert/vers"],
        "pos":         "adj",
        "topic":       "society",
        "level":       4,
        "freq":        3,
        "meaning":     "xilma-xil, rang-barang",
        "collocation": "a diverse population · cultural diversity · biodiversity",
        "note":        "<p>Oti — <b>diversity</b>, bu esa jamiyat va ekologiya mavzularining "
                       "kalit so‘zi: <i>cultural <b>diversity</b></i>, <i>bio<b>diversity</b></i>.</p>",
        "examples":    [("Large cities tend to have far more diverse populations.",
                         "Yirik shaharlarda aholi tarkibi ancha xilma-xil bo‘ladi.")],
        "related":     [("convert", "bir ildiz — «burmoq»")],
    },
    # ── ced/cess ────────────────────────────────────────────────────────────
    {
        "word":        "access",
        "hanja":       "ac- + cess",
        "roots":       ["ced/cess"],
        "pos":         "noun",
        "topic":       "society",
        "level":       3,
        "freq":        3,
        "meaning":     "kirish imkoni, foydalanish imkoniyati",
        "collocation": "access to education · have access to · limited access",
        "note":        "<p><b>Predlogi doim <i>to</i></b>: <i>access <b>to</b> clean water</i> "
                       "(❌ access of). Sanalmaydigan ot — ❌ <i>accesses</i>. "
                       "Sifati <b>accessible</b>.</p>",
        "examples":    [("Millions of people still lack access to safe drinking water.",
                         "Millionlab odam hamon xavfsiz ichimlik suvidan foydalana olmaydi.")],
        "related":     [("exceed", "bir ildiz — «yurmoq»: exceed = chegaradan o‘tib ketmoq")],
    },
    {
        "word":        "exceed",
        "hanja":       "ex- + ceed",
        "roots":       ["ced/cess"],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "oshib ketmoq — belgilangan chegaradan yuqori bo‘lmoq",
        "collocation": "exceed the limit · exceed expectations · exceed 50%",
        "note":        "<p>Task 1 da raqamni takrorlamasdan berish uchun: <i>The figure "
                       "<b>exceeded</b> 60% for the first time in 2010.</i></p>",
        "examples":    [("Pollution levels regularly exceed international safety limits.",
                         "Ifloslanish darajasi muntazam ravishda xalqaro xavfsizlik chegarasidan oshib ketadi.")],
        "synonyms":    [("surpass", "surpass = boshqasidan ustun chiqmoq (poyga ohangi); "
                                    "exceed = belgilangan chegaradan oshmoq")],
    },
    {
        "word":        "recession",
        "hanja":       "re- + cess + -ion",
        "roots":       ["ced/cess"],
        "pos":         "noun",
        "topic":       "economy",
        "level":       5,
        "freq":        1,
        "meaning":     "tanazzul, iqtisodiy pasayish — «orqaga yurish»",
        "collocation": "a deep recession · during the recession · slide into recession",
        "note":        "<p>Task 1 grafiklaridagi keskin pasayishlarni izohlashda foydali: "
                       "<i>The drop after 2008 coincided with a global <b>recession</b>.</i></p>",
        "examples":    [("Unemployment rose sharply during the recession.",
                         "Tanazzul davrida ishsizlik keskin oshdi.")],
        "antonyms":    [("boom", "recession = pasayish; boom = jadal o‘sish")],
    },
    # ── fer ─────────────────────────────────────────────────────────────────
    {
        "word":        "transfer",
        "hanja":       "trans- + fer",
        "roots":       ["fer"],
        "pos":         "verb",
        "topic":       "work",
        "level":       4,
        "freq":        2,
        "meaning":     "ko‘chirmoq, o‘tkazmoq — bir joydan boshqasiga",
        "collocation": "transfer money · transfer skills · a transfer of power",
        "note":        "<p><b>transferable skills</b> — ish mavzusidagi juda foydali birikma: "
                       "«bir sohadan boshqasiga o‘tadigan ko‘nikmalar».</p>",
        "examples":    [("Communication is a transferable skill valued in every profession.",
                         "Muloqot — har bir kasbda qadrlanadigan, ko‘chib o‘tuvchi ko‘nikma.")],
        "related":     [("infer", "bir ildiz: transfer = ko‘chirmoq; infer = xulosa chiqarmoq")],
    },
    {
        "word":        "infer",
        "hanja":       "in- + fer",
        "roots":       ["fer"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "xulosa chiqarmoq — bevosita aytilmagan narsani anglab olmoq",
        "collocation": "infer from the data · it can be inferred that · make an inference",
        "note":        "<p><b>Reading’ning kalit so‘zi.</b> «True/False/Not Given» va «Yes/No/"
                       "Not Given» savollari aynan shu ko‘nikmani tekshiradi: matnda "
                       "yozilmagan, lekin mantiqan kelib chiqadigan narsa.</p>",
        "examples":    [("It can be inferred from the data that demand will continue to fall.",
                         "Ma’lumotlardan talab pasayishda davom etadi degan xulosa chiqarish mumkin.")],
        "synonyms":    [("imply", "infer = O‘QUVCHI xulosa chiqaradi; imply = MUALLIF ishora qiladi")],
    },
    {
        "word":        "imply",
        "hanja":       "im- + ply (buklamoq)",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "ishora qilmoq, nazarda tutmoq — ochiq aytmasdan bildirmoq",
        "collocation": "this implies that · the implications of · far-reaching implications",
        "note":        "<p>Oti — <b>implication</b> (oqibat, ma’no): <i>the policy has serious "
                       "<b>implications for</b> low-income families</i> — bu Task 2 uchun juda "
                       "kuchli birikma.</p>",
        "examples":    [("These findings imply that current policies are inadequate.",
                         "Bu natijalar hozirgi siyosat yetarli emasligiga ishora qiladi.")],
        "synonyms":    [("infer", "imply = muallif ishora qiladi; infer = o‘quvchi xulosa chiqaradi")],
    },
    # ── pel/puls ────────────────────────────────────────────────────────────
    {
        "word":        "compulsory",
        "hanja":       "com- + puls + -ory",
        "roots":       ["pel/puls"],
        "pos":         "adj",
        "topic":       "school",
        "level":       4,
        "freq":        3,
        "meaning":     "majburiy — qonun bilan talab qilinadigan",
        "collocation": "compulsory education · compulsory military service · make it compulsory",
        "note":        "<p>Ta’lim mavzusidagi eng ko‘p uchraydigan savol: <i>Should sport be "
                       "<b>compulsory</b> at school?</i> Sinonimi <b>mandatory</b>, "
                       "teskarisi <b>optional</b> / <b>voluntary</b>.</p>",
        "examples":    [("In most countries, education is compulsory until the age of sixteen.",
                         "Ko‘pchilik davlatlarda ta’lim o‘n olti yoshgacha majburiy."),
                        ("Some argue that voting should be made compulsory.",
                         "Ba’zilar ovoz berishni majburiy qilish kerak deb hisoblaydi.")],
        "synonyms":    [("mandatory", "ma’nosi bir xil; mandatory rasmiy hujjatlarda ko‘proq")],
        "antonyms":    [("voluntary", "compulsory = majburiy; voluntary = ixtiyoriy")],
    },
    {
        "word":        "compel",
        "hanja":       "com- + pel",
        "roots":       ["pel/puls"],
        "pos":         "verb",
        "topic":       "society",
        "level":       6,
        "freq":        1,
        "meaning":     "majburlamoq — chora qoldirmaslik",
        "collocation": "compel somebody to do · feel compelled to · a compelling argument",
        "note":        "<p>Sifati <b>compelling</b> = «ishonarli, e’tiborni tortadigan» — "
                       "Task 2 uchun juda foydali: <i>a <b>compelling</b> argument for reform</i>.</p>",
        "examples":    [("Rising costs have compelled many families to reduce their spending.",
                         "Narxlarning oshishi ko‘p oilalarni xarajatlarini qisqartirishga majbur qildi.")],
        "synonyms":    [("oblige", "oblige = qoida/majburiyat yuklaydi; compel = kuch bilan majbur qiladi")],
    },
]


# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 100 + _i)
