# -*- coding: utf-8 -*-
"""IELTS grammar bank — Passive, causative & nominalisation (majhul nisbat).

Order decade 500-599. This is the group that makes writing sound academic
rather than conversational: the passive removes the personal agent, and
nominalisation packs a whole clause into a noun phrase. Process diagrams in
Task 1 are written almost entirely in the present simple passive.
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
        "pattern":   "the passive",
        "category":  "en_passive",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "majhul nisbat — «... qilinadi, qilindi» (bajaruvchi aytilmaydi)",
        "attach":    "S + be + V3 (+ by …)",
        "form_rule": "<b>be</b> ning kerakli zamondagi shakli + <b>3-shakl</b>: "
                     "is <b>built</b> · was <b>built</b> · has been <b>built</b> · "
                     "is being <b>built</b> · will be <b>built</b>. "
                     "Bajaruvchi muhim bo‘lsagina <b>by</b> qo‘shiladi.",
        "note":      "<p>Nima uchun IELTS uni yaxshi ko‘radi: akademik yozuvda <b>ish muhim, "
                     "kim qilgani emas</b>. <i>People built the bridge in 1990</i> → "
                     "<i>The bridge <b>was built</b> in 1990.</i></p>"
                     "<p>⚠️ Butun inshoni passive’da yozmang — matn og‘ir va noaniq bo‘ladi. "
                     "Har xatboshida 1-2 ta yetadi.</p>",
        "mistake":   "<p>❌ The problem <u>is discuss</u> in this essay → ✅ <b>is discussed</b>.</p>"
                     "<p>❌ <i>be</i> ni tushirib qoldirish: The report <u>published</u> last year "
                     "(«hisobot nashr qildi») → ✅ The report <b>was published</b> last year.</p>",
        "examples": [
            ("Stricter regulations were introduced after the accident.",
             "Baxtsiz hodisadan keyin qattiqroq qoidalar joriy etildi."),
            ("The beans are harvested, dried and then transported to the factory.",
             "Doni yig‘iladi, quritiladi va so‘ng zavodga tashiladi."),
        ],
        "synonyms": [
            ("the process passive (Task 1)", "process passive = jarayon diagrammasidagi "
                                             "present simple passive qolipi"),
            ("modal + passive", "modal + be + V3 = tavsiyani shaxssiz aytadi"),
            ("nominalisation", "ikkalasi ham shaxsni yashiradi; nominalisation buni OT orqali qiladi"),
        ],
        "order": 500,
    },
    {
        "pattern":   "the process passive (Task 1)",
        "category":  "en_passive",
        "function":  "time",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "jarayon diagrammasi tili — «avval ... qilinadi, so‘ng ... qilinadi»",
        "attach":    "First, X is + V3. Then it is + V3.",
        "form_rule": "<b>present simple passive</b> + ketma-ketlik ravishlari: "
                     "<i>First · Next · Then · After that · Subsequently · Finally</i>. "
                     "Bir xil egani takrorlamaslik uchun <b>it</b> va <b>which</b> ishlating.",
        "note":      "<p>Process diagram (Task 1) uchun tayyor tuzilma — bu turdagi topshiriq "
                     "deyarli butunlay shu qolipdan iborat:</p>"
                     "<p><i><b>First</b>, raw materials <b>are collected</b>. They <b>are then "
                     "crushed</b> and <b>washed</b>, <b>after which</b> the mixture <b>is heated</b> "
                     "to 200°C. <b>Finally</b>, the product <b>is packaged</b> for distribution.</i></p>",
        "mistake":   "<p>❌ <i>They collect the materials, then they crush them…</i> — «they» kim? "
                     "Jarayonda bajaruvchi noma’lum, shuning uchun passive kerak.</p>",
        "examples": [
            ("Once the glass has been sorted, it is melted at high temperature.",
             "Shisha saralanganidan so‘ng, u yuqori haroratda eritiladi."),
        ],
        "synonyms": [
            ("the passive", "bu — passive’ning Task 1 jarayoni uchun maxsus qolipi"),
            ("the tense of the chart (Task 1)", "jarayon diagrammasi doim present simple da yoziladi"),
        ],
        "order": 501,
    },
    {
        "pattern":   "have / get something done",
        "category":  "en_passive",
        "function":  "case",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "birovga qildirish — «... qildirmoq»",
        "attach":    "S + have/get + object + V3",
        "form_rule": "<b>have</b> (neytral) yoki <b>get</b> (og‘zakiroq) + ot + <b>3-shakl</b>: "
                     "<i>have a house <b>built</b></i>, <i>get the car <b>repaired</b></i>. "
                     "Ega ishni o‘zi bajarmaydi — boshqaga qildiradi.",
        "note":      "<p>Speaking’da juda tabiiy: <i>I had my documents translated.</i> "
                     "Writing’da esa xizmatlar haqida gapirganda: <i>Wealthier families "
                     "<b>have</b> their children <b>tutored</b> privately.</i></p>",
        "mistake":   "<p>❌ I <u>repaired</u> my laptop — bu «o‘zim ta’mirladim» degani. "
                     "Ustaga bergan bo‘lsangiz: ✅ I <b>had</b> my laptop <b>repaired</b>.</p>",
        "examples": [
            ("Many companies have their products manufactured overseas.",
             "Ko‘p kompaniyalar mahsulotini chet elda ishlab chiqartiradi."),
        ],
        "synonyms": [
            ("make / let / have (causative)", "have something done = ish natijasi; "
                                              "make somebody do = odamga majburlash"),
        ],
        "order": 502,
    },
    {
        "pattern":   "make / let / have (causative)",
        "category":  "en_passive",
        "function":  "obligation",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "majburlash va ruxsat — «majbur qilmoq, ruxsat bermoq»",
        "attach":    "make/let/have + somebody + V (yalang‘och)",
        "form_rule": "<b>make</b> / <b>let</b> / <b>have</b> + odam + <u>yalang‘och fe’l</u> "
                     "(❌ make him <u>to</u> study). Ammo <b>allow</b> va <b>force</b> "
                     "<i>to</i> oladi: <i>allow him <b>to</b> study</i>. "
                     "Majhul shaklda <b>make</b> ham <i>to</i> oladi: <i>be made <b>to</b> pay</i>.",
        "note":      "<p>Task 2 da bahsli mavzu (majburiy ta’lim, majburiy harbiy xizmat) "
                     "haqida yozganda kerak bo‘ladi. Rasmiyroq muqobillar: "
                     "<b>compel</b>, <b>oblige</b>, <b>require somebody to</b>, <b>permit</b>.</p>",
        "mistake":   "<p>❌ Schools should <u>make students to wear</u> uniforms → "
                     "✅ <b>make students wear</b> uniforms.</p>",
        "examples": [
            ("Some countries make voting compulsory for all adult citizens.",
             "Ba’zi mamlakatlar barcha voyaga yetgan fuqarolar uchun ovoz berishni majburiy qiladi."),
            ("Parents should let children choose at least some of their activities.",
             "Ota-onalar bolalarga hech bo‘lmaganda ba’zi mashg‘ulotlarni tanlashga ruxsat berishi kerak."),
        ],
        "synonyms": [
            ("have / get something done", "make somebody do = odamni majburlash; "
                                          "have something done = xizmatni bajartirish"),
            ("must / have to", "make = boshqaga majburlash; must = o‘ziga majburiyat"),
        ],
        "order": 503,
    },
    {
        "pattern":   "nominalisation",
        "category":  "en_passive",
        "function":  "case",
        "level":     6,
        "freq":      2,
        "register":  "written",
        "meaning":   "otlashtirish — fe’lni otga aylantirib, akademik uslub yasash",
        "attach":    "verb → noun (decide → the decision)",
        "form_rule": "Fe’l yoki sifatni otga aylantiring va uni gapning egasi qiling: "
                     "<i>The government <u>decided</u> to cut spending, which <u>affected</u> "
                     "schools.</i> → <i><b>The government’s decision</b> to cut spending had "
                     "<b>a significant impact</b> on schools.</i>",
        "note":      "<p><b>Akademik uslubning eng ko‘zga ko‘rinadigan belgisi.</b> Ko‘p "
                     "ishlatiladigan juftlar: decide → <i>decision</i> · grow → <i>growth</i> · "
                     "reduce → <i>reduction</i> · consume → <i>consumption</i> · "
                     "pollute → <i>pollution</i> · unemployed → <i>unemployment</i>.</p>"
                     "<p>Foydasi ikki karra: matn zichlashadi va gapni ot bilan boshlash "
                     "imkonini beradi — <i><b>The rapid expansion of cities</b> has placed "
                     "enormous pressure on infrastructure.</i></p>",
        "mistake":   "<p>❌ Haddan tashqari otlashtirish gapni o‘qib bo‘lmas qiladi: "
                     "<i>The implementation of the reduction of the utilisation of…</i> — "
                     "bitta gapda 1-2 ta ot yetarli.</p>",
        "examples": [
            ("The introduction of congestion charges led to a marked reduction in traffic.",
             "Tirbandlik yig‘imining joriy etilishi transport oqimining sezilarli kamayishiga olib keldi."),
        ],
        "synonyms": [
            ("the passive", "ikkalasi ham shaxsni yashiradi — biri fe’l orqali, biri ot orqali"),
            ("the fact that", "the fact that = gapni ot qiladi; nominalisation = fe’lni ot qiladi"),
        ],
        "order": 504,
    },
    {
        "pattern":   "there is / there are",
        "category":  "en_passive",
        "function":  "case",
        "level":     2,
        "freq":      2,
        "register":  "both",
        "meaning":   "mavjudlik — «bor, mavjud»",
        "attach":    "There + is/are + noun",
        "form_rule": "Fe’l <u>keyingi</u> otga qarab moslashadi: <i>There <b>is</b> a reason</i> · "
                     "<i>There <b>are</b> several reasons</i>. Boshqa zamonlar: "
                     "<i>there was / there have been / there will be</i>.",
        "note":      "<p>Foydali, lekin <b>haddan ortiq ishlatilgan</b> qolip. Band 7 uchun "
                     "ba’zilarini kuchliroq fe’lga almashtiring:</p>"
                     "<p><i>There are many people who think…</i> → <i><b>Many people argue</b> that…</i><br>"
                     "<i>There is an increase in…</i> → <i><b>X has increased</b> …</i></p>",
        "mistake":   "<p>❌ <i>There <u>are</u> a lot of pollution</i> → ✅ <i>There <b>is</b> a "
                     "lot of pollution</i> — <i>pollution</i> sanalmaydigan ot.</p>"
                     "<p>❌ <i>In the graph <u>have</u> three lines</i> → ✅ <i>There <b>are</b> "
                     "three lines</i>.</p>",
        "examples": [
            ("There are several reasons why young people migrate to cities.",
             "Yoshlarning shaharga ko‘chishining bir necha sababi bor."),
        ],
        "synonyms": [
            ("nominalisation", "there is + ot o‘rniga otni ega qiling — matn kuchliroq bo‘ladi"),
        ],
        "order": 505,
    },
    {
        "pattern":   "it is + adjective + that/to",
        "category":  "en_passive",
        "function":  "emphasis",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "shaxssiz baho — «... ekani aniq/muhim»",
        "attach":    "It is + adj + that + clause · It is + adj + to + V",
        "form_rule": "<b>It is</b> + sifat (<i>clear, evident, essential, difficult, unrealistic</i>) "
                     "+ <b>that</b> + gap, yoki + <b>to</b> + fe’l. "
                     "Bu yerdagi <i>it</i> — «bu» emas, shunchaki o‘rin to‘ldiruvchi ega.",
        "note":      "<p>«Men o‘ylaymanki» ni akademik qiladi: <i><b>It is evident that</b> "
                     "urbanisation has accelerated.</i> · <i><b>It is difficult to</b> justify "
                     "such spending.</i></p>"
                     "<p>Hedging bilan birlashtiring: <i>It is <b>arguably</b> the most effective "
                     "measure available.</i></p>",
        "mistake":   "<p>❌ <i><u>Is</u> clear that…</i> — ingliz tilida ega tushib qolmaydi, "
                     "<b>It</b> majburiy.</p>",
        "examples": [
            ("It is essential that governments coordinate their climate policies.",
             "Hukumatlarning iqlim siyosatini muvofiqlashtirishi zarur."),
        ],
        "synonyms": [
            ("it is often argued that", "argued = boshqalarning fikri; it is clear that = "
                                        "sizning bahoyingiz"),
            ("cleft sentence (It is … that)", "cleft = gapning bir bo‘lagini ajratib ta’kidlaydi"),
        ],
        "order": 506,
    },
    {
        "pattern":   "it is often argued that",
        "category":  "en_passive",
        "function":  "quote",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "boshqalarning qarashini keltirish — «ko‘pincha aytiladiki»",
        "attach":    "It is often argued/claimed that + clause",
        "form_rule": "<b>It is (often/widely/commonly)</b> + argued / claimed / assumed / "
                     "acknowledged + <b>that</b> + to‘liq gap.",
        "note":      "<p>Discussion inshosining kirish jumlasi uchun tayyor qolip: qarshi fikrni "
                     "keltirasiz, keyin <i>however</i> bilan o‘z fikringizga o‘tasiz:</p>"
                     "<p><i><b>It is often argued that</b> examinations are the fairest way to "
                     "assess students. <b>However</b>, this view overlooks…</i></p>",
        "mistake":   "<p>❌ <i>Some people say that…</i> — bu Band 5-6 ifodasi. Majhul qolipga o‘ting.</p>",
        "examples": [
            ("It is widely assumed that economic growth automatically reduces poverty.",
             "Iqtisodiy o‘sish qashshoqlikni o‘z-o‘zidan kamaytiradi, deb keng tarqalgan fikr bor."),
        ],
        "synonyms": [
            ("it is said that / X is thought to", "bir oila: argued = bahsli fikr, "
                                                  "believed = keng qabul qilingan qarash"),
            ("it is + adjective + that/to", "biri boshqalarning fikri, biri sizning bahoyingiz"),
        ],
        "order": 507,
    },
]
