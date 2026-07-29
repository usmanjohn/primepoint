# -*- coding: utf-8 -*-
"""IELTS grammar bank — Linking & cohesion (bog'lash vositalari).

Order decade 1000-1099. This is a whole quarter of the Writing mark
(Coherence & Cohesion) and the group candidates most often get half-right:
they memorise `Moreover` and `Furthermore` and then overuse them, while never
using referencing (`this trend`, `such measures`), which is what the descriptor
actually rewards.
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
        "pattern":   "however",
        "category":  "en_cohesion",
        "function":  "contrast",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "qarama-qarshilik — «biroq, lekin» (yangi jumla boshida)",
        "attach":    "However, + S + V",
        "form_rule": "<b>However</b> — ravish, gaplarni <u>bog‘lamaydi</u>, balki yangi jumlani "
                     "boshlaydi va <b>vergul</b> oladi. Gap o‘rtasida ishlatilsa ikki tomondan "
                     "vergul: <i>The policy, <b>however</b>, was abandoned.</i>",
        "note":      "<p>Task 2 ning eng ko‘p ishlatiladigan bog‘lovchisi — aynan shuning uchun "
                     "har xatboshida takrorlamang. Muqobillar: <b>nevertheless</b>, "
                     "<b>nonetheless</b>, <b>on the other hand</b>, <b>that said</b>, "
                     "<b>by contrast</b>.</p>",
        "mistake":   "<p>❌ <i>The plan was expensive <u>however</u> it worked.</i> — "
                     "<i>however</i> ikki gapni ulay olmaydi. ✅ <i>… expensive<b>;</b> however, "
                     "it worked.</i> yoki ✅ <i>… expensive, <b>but</b> it worked.</i></p>",
        "examples": [
            ("Online courses are convenient. However, they cannot replace laboratory work.",
             "Onlayn kurslar qulay. Biroq ular laboratoriya ishining o‘rnini bosa olmaydi."),
        ],
        "synonyms": [
            ("although / though / even though", "although = bitta gap ICHIDA; however = "
                                                "yangi jumla boshida"),
            ("in contrast / on the other hand", "on the other hand = ikkinchi TOMONNI kiritadi; "
                                                "however = oddiy qarshilik"),
            ("despite / in spite of", "despite + ot; however + yangi gap"),
        ],
        "order": 1000,
    },
    {
        "pattern":   "in contrast / on the other hand",
        "category":  "en_cohesion",
        "function":  "contrast",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "qarama-qarshi tomon — «aksincha; boshqa tomondan»",
        "attach":    "In contrast, + S + V",
        "form_rule": "<b>In contrast,</b> / <b>By contrast,</b> / <b>On the other hand,</b> — "
                     "jumla boshida, vergul bilan. <i>On the one hand … on the other hand …</i> "
                     "juft holda ishlatiladi.",
        "note":      "<p><b>Task 1 da</b> ikki guruh raqamni ajratadi: <i>Consumption rose in "
                     "Europe. <b>In contrast</b>, Asian figures fell steadily.</i></p>"
                     "<p><b>Task 2 (discussion) da</b> ikkinchi qarashga o‘tish signali. "
                     "⚠️ <i>On the other hand</i> ni faqat ikki tomon haqida yozayotganda "
                     "ishlating — bir tomonlama inshoda o‘rinsiz.</p>",
        "mistake":   "<p>❌ <i>In the other hand</i> → ✅ <i><b>On</b> the other hand</i>.</p>",
        "examples": [
            ("Spending on healthcare doubled. By contrast, the education budget remained flat.",
             "Sog‘liqni saqlashga sarflangan mablag‘ ikki baravar oshdi. Aksincha, ta’lim byudjeti o‘zgarmadi."),
        ],
        "synonyms": [
            ("however", "however = umumiy qarshilik; in contrast = ikki narsani qarshi qo‘yadi"),
            ("whereas / while", "whereas = bitta gap ichida; in contrast = alohida jumla"),
            ("compared with / in comparison with", "compared with + ot; in contrast = jumla boshida"),
        ],
        "order": 1001,
    },
    {
        "pattern":   "despite / in spite of",
        "category":  "en_cohesion",
        "function":  "concession",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "qaramaslik — «... ga qaramay»",
        "attach":    "Despite + noun / -ing, S + V",
        "form_rule": "<b>despite</b> / <b>in spite of</b> + <u>ot yoki -ing</u> — "
                     "<b>hech qachon to‘liq gap emas</b>. Gap kerak bo‘lsa: "
                     "<b>despite the fact that</b> + gap, yoki <b>although</b> + gap. "
                     "⚠️ ❌ <i>despite <u>of</u></i> — <i>of</i> faqat <i>in spite of</i> da bor.",
        "note":      "<p>Uchtasini bir-biriga aylantira olish Band 7 mashqi:</p>"
                     "<p><i><b>Although</b> costs rose, demand remained strong.</i><br>"
                     "<i><b>Despite</b> the rise in costs, demand remained strong.</i><br>"
                     "<i>Costs rose<b>; nevertheless,</b> demand remained strong.</i></p>",
        "mistake":   "<p>❌ <i>Despite <u>the costs increased</u></i> → ✅ <i>Despite <b>the "
                     "increase in costs</b></i> yoki ✅ <i><b>Although</b> the costs increased</i>.</p>",
        "examples": [
            ("Despite substantial investment, the network remains unreliable.",
             "Katta sarmoyaga qaramay, tarmoq hamon ishonchsizligicha qolmoqda."),
        ],
        "synonyms": [
            ("although / though / even though", "despite + OT; although + GAP"),
            ("the fact that", "despite the fact that = despite bilan gap ishlatishning yo‘li"),
            ("however", "despite = bir gap ichida; however = ikki jumla orasida"),
        ],
        "order": 1002,
    },
    {
        "pattern":   "therefore / consequently",
        "category":  "en_cohesion",
        "function":  "result",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "natija — «shuning uchun, natijada»",
        "attach":    "Therefore, + S + V",
        "form_rule": "<b>Therefore</b> / <b>Consequently</b> / <b>As a result</b> / "
                     "<b>Thus</b> / <b>Hence</b> — jumla boshida vergul bilan, yoki nuqta-vergul "
                     "bilan: <i>…<b>;</b> therefore, …</i> "
                     "<i>Thus</i> va <i>hence</i> rasmiyroq va ixchamroq.",
        "note":      "<p>Sabab-natija zanjirini ko‘rsatish Task 2 ning yuragi. Xilma-xillik "
                     "uchun jumla ichidagi variantlarga ham o‘ting: <b>which is why</b>, "
                     "<b>as a consequence</b>, <b>this has led to</b>.</p>",
        "mistake":   "<p>❌ <i>Therefore <u>of</u> this…</i> → ✅ <i><b>Therefore,</b> …</i> yoki "
                     "✅ <i><b>Because of</b> this, …</i></p>",
        "examples": [
            ("Fuel prices rose sharply. Consequently, demand for public transport increased.",
             "Yoqilg‘i narxi keskin oshdi. Natijada jamoat transportiga talab ortdi."),
        ],
        "synonyms": [
            ("because / since / as", "because = SABABNI kiritadi; therefore = NATIJANI (teskari yo‘nalish)"),
            ("result in / result from", "result in = gap ichida; therefore = jumlalar orasida"),
        ],
        "order": 1003,
    },
    {
        "pattern":   "moreover / furthermore",
        "category":  "en_cohesion",
        "function":  "listing",
        "level":     3,
        "freq":      2,
        "register":  "written",
        "meaning":   "qo‘shimcha dalil — «bundan tashqari, qolaversa»",
        "attach":    "Moreover, + S + V",
        "form_rule": "<b>Moreover</b> / <b>Furthermore</b> / <b>In addition</b> / "
                     "<b>What is more</b> — jumla boshida vergul bilan. "
                     "<b>In addition to</b> + ot/-ing (bu — predlogli shakl, boshqa qolip).",
        "note":      "<p>⚠️ <b>Eng ko‘p suiiste’mol qilinadigan bog‘lovchilar shu.</b> Tekshiruvchi "
                     "har xatboshi <i>Moreover</i> bilan boshlanganini darrov sezadi va buni "
                     "«mexanik» deb baholaydi. Bitta inshoda 1-2 marta yetadi; qolganida "
                     "gapni mazmun bilan bog‘lang (<i>This is not the only concern…</i>).</p>",
        "mistake":   "<p>❌ <i>In addition <u>of</u> the cost</i> → ✅ <i>In addition <b>to</b> "
                     "the cost</i> · ❌ <i>Beside, …</i> → ✅ <i><b>Besides</b>, …</i></p>",
        "examples": [
            ("Furthermore, congestion charges generate revenue for public transport.",
             "Qolaversa, tirbandlik yig‘imlari jamoat transporti uchun daromad keltiradi."),
        ],
        "synonyms": [
            ("firstly / secondly / finally", "bular tartibni; moreover = qo‘shimchani bildiradi"),
            ("not only … but also", "not only…but also = bir gap ichida ikki dalilni bog‘laydi"),
        ],
        "order": 1004,
    },
    {
        "pattern":   "for instance / such as",
        "category":  "en_cohesion",
        "function":  "example",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "misol keltirish — «masalan, ... kabi»",
        "attach":    "For instance, + gap · noun + such as + noun",
        "form_rule": "<b>For example / For instance,</b> + <u>to‘liq gap</u> (vergul bilan) · "
                     "<b>such as</b> / <b>like</b> + <u>ot</u>, vergulsiz: "
                     "<i>renewable sources <b>such as</b> wind and solar</i>. "
                     "<b>e.g.</b> — qavs ichida, insho matnida emas.",
        "note":      "<p>Task 2 da har bir dalilni misol bilan mustahkamlash kerak — Task Response "
                     "bahosi shuni talab qiladi. Misol o‘ylab topilgan bo‘lishi ham mumkin, "
                     "lekin aniq bo‘lsin: <i>countries <b>such as</b> Norway and Denmark</i>.</p>",
        "mistake":   "<p>❌ <i>such as <u>the government invests</u></i> → ✅ <i>such as "
                     "<b>Norway</b></i> (ot) yoki ✅ <i><b>For instance,</b> the government "
                     "invests…</i> (gap).</p>",
        "examples": [
            ("Practical subjects such as cooking and budgeting are rarely taught at school.",
             "Ovqat pishirish va byudjet tuzish kabi amaliy fanlar maktabda kam o‘qitiladi."),
        ],
        "synonyms": [
            ("in particular / notably", "notably = ayni bir misolni ajratib ko‘rsatadi"),
        ],
        "order": 1005,
    },
    {
        "pattern":   "in particular / notably",
        "category":  "en_cohesion",
        "function":  "emphasis",
        "level":     5,
        "freq":      1,
        "register":  "written",
        "meaning":   "ajratib ko‘rsatish — «xususan, ayniqsa»",
        "attach":    "…, in particular, … · notably + noun",
        "form_rule": "<b>in particular</b> — otdan keyin yoki jumla boshida · "
                     "<b>notably</b> / <b>particularly</b> — otdan oldin · "
                     "<b>especially</b> — og‘zakiroq, lekin ishlaydi.",
        "note":      "<p>Task 1 da eng keskin raqamni ajratib ko‘rsatish uchun ideal: "
                     "<i>All four countries saw growth, <b>notably</b> Vietnam, whose figure "
                     "tripled.</i></p>",
        "examples": [
            ("Young people, in particular, rely on social media for news.",
             "Ayniqsa yoshlar yangiliklar uchun ijtimoiy tarmoqlarga tayanadi."),
        ],
        "synonyms": [
            ("for instance / such as", "such as = umumiy misol; notably = eng muhim misolni ajratadi"),
        ],
        "order": 1006,
    },
    {
        "pattern":   "firstly / secondly / finally",
        "category":  "en_cohesion",
        "function":  "listing",
        "level":     2,
        "freq":      2,
        "register":  "written",
        "meaning":   "tartib bilan sanash — «birinchidan, ikkinchidan, nihoyat»",
        "attach":    "Firstly, + S + V",
        "form_rule": "<b>Firstly / Secondly / Thirdly / Finally</b> — jumla boshida vergul bilan. "
                     "<i>Lastly</i> ham to‘g‘ri; <i>At last</i> — ❌ (u «nihoyat, kutib» degani).",
        "note":      "<p>Ikki dalilli xatboshida bu ketma-ketlik strukturani aniq qiladi. "
                     "Lekin butun insho <i>Firstly… Secondly… Thirdly…</i> bo‘lib qolsa, matn "
                     "ro‘yxatga aylanadi — Coherence bahosi tushadi. Ba’zilarini mazmuniy "
                     "o‘tish bilan almashtiring: <i>A further concern is…</i></p>",
        "mistake":   "<p>❌ <i><u>At first</u>, education is important</i> → ✅ <i><b>Firstly</b>, …</i> "
                     "(<i>at first</i> = «dastlab, keyin o‘zgardi»).</p>",
        "examples": [
            ("Firstly, urban expansion destroys farmland; secondly, it increases commuting times.",
             "Birinchidan, shaharlarning kengayishi ekin maydonlarini yo‘q qiladi; ikkinchidan, qatnov vaqtini oshiradi."),
        ],
        "synonyms": [
            ("moreover / furthermore", "firstly/secondly = tartib; moreover = qo‘shimcha dalil"),
            ("in conclusion / overall", "finally = oxirgi dalil; in conclusion = xulosa qismi"),
        ],
        "order": 1007,
    },
    {
        "pattern":   "in conclusion / overall",
        "category":  "en_cohesion",
        "function":  "summary",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "yakun — «xulosa qilib aytganda; umuman olganda»",
        "attach":    "In conclusion, + S + V",
        "form_rule": "<b>Task 2</b> xulosasi: <b>In conclusion,</b> / <b>To conclude,</b> / "
                     "<b>To sum up,</b> · <b>Task 1</b> umumiy manzarasi: <b>Overall,</b> / "
                     "<b>In general,</b> / <b>It is clear that</b>.",
        "note":      "<p>⚠️ <b>Ikkalasi bir xil emas.</b> Task 1 da <i>In conclusion</i> emas, "
                     "<b>Overall</b> yozing — Task 1 da fikr bildirilmaydi, faqat umumiy manzara "
                     "beriladi. Va u <u>ikkinchi xatboshi</u> bo‘lishi mumkin, oxirida bo‘lishi shart emas.</p>"
                     "<p>Xulosada yangi dalil kiritmang — bu Task Response bahosini tushiradi.</p>",
        "mistake":   "<p>❌ Task 1 da: <i>In conclusion, I think this graph is interesting.</i> → "
                     "✅ <i><b>Overall</b>, consumption rose in all four countries, with the "
                     "sharpest increase in Vietnam.</i></p>",
        "examples": [
            ("Overall, the figures for both countries followed a similar upward trend.",
             "Umuman olganda, ikkala mamlakat ko‘rsatkichlari o‘xshash o‘sish tendensiyasini kuzatdi."),
        ],
        "synonyms": [
            ("firstly / secondly / finally", "finally = oxirgi dalil; in conclusion = butun inshoning yakuni"),
        ],
        "order": 1008,
    },
    {
        "pattern":   "this / such + noun (referencing)",
        "category":  "en_cohesion",
        "function":  "reference",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "ishora bilan bog‘lash — «bu tendensiya, bunday choralar»",
        "attach":    "This/These/Such + summarising noun",
        "form_rule": "<b>this</b> / <b>these</b> / <b>such</b> + <u>umumlashtiruvchi ot</u>: "
                     "<i><b>this trend</b>, <b>this shift</b>, <b>these measures</b>, "
                     "<b>such policies</b>, <b>this phenomenon</b></i>. "
                     "⚠️ Yolg‘iz <i>This is…</i> noaniq — otni albatta qo‘shing.",
        "note":      "<p><b>Coherence & Cohesion bahosining eng kam ishlatiladigan quroli.</b> "
                     "Bog‘lovchi so‘z qo‘shmasdan xatboshilarni ulaydi va bir vaqtning o‘zida "
                     "oldingi fikrni umumlashtiradi:</p>"
                     "<p><i>More families are moving to the suburbs. <b>This trend</b> has "
                     "placed pressure on rural infrastructure.</i></p>",
        "mistake":   "<p>❌ <i>It is a big problem</i> (nima «it»?) → ✅ <i><b>This shortage</b> "
                     "is a serious problem.</i></p>",
        "examples": [
            ("Cities have banned older vehicles. Such measures have cut emissions considerably.",
             "Shaharlar eski transport vositalarini taqiqladi. Bunday choralar chiqindilarni sezilarli kamaytirdi."),
        ],
        "synonyms": [
            ("the former / the latter", "former/latter = ikkitadan qaysi birini aniqlaydi"),
            ("nominalisation", "ishora oti ko‘pincha nominalizatsiyadan olinadi (shift, increase)"),
        ],
        "order": 1009,
    },
    {
        "pattern":   "the former / the latter",
        "category":  "en_cohesion",
        "function":  "reference",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "avvalgisi / keyingisi — ikkitadan qaysi biriga ishora",
        "attach":    "the former … the latter …",
        "form_rule": "<b>the former</b> = birinchi tilga olingani · <b>the latter</b> = "
                     "ikkinchisi. <u>Faqat ikkita</u> narsa bo‘lganda ishlaydi; uchta bo‘lsa "
                     "<b>the first</b> / <b>the last</b> deyiladi.",
        "note":      "<p>Otni takrorlamaslikning eng akademik yo‘li: <i>Students can choose "
                     "between vocational and academic courses; <b>the former</b> leads to "
                     "employment more quickly, while <b>the latter</b> offers broader options.</i></p>"
                     "<p>Bir inshoda bir marta — noto‘g‘ri ishlatilsa, o‘quvchi adashadi.</p>",
        "examples": [
            ("Both nuclear and solar power were expanded, though the latter grew far faster.",
             "Ham yadro, ham quyosh energiyasi kengaytirildi, biroq ikkinchisi ancha tez o‘sdi."),
        ],
        "synonyms": [
            ("this / such + noun (referencing)", "such + ot = umumlashtiradi; the former/latter = "
                                                 "ikkitadan birini tanlaydi"),
        ],
        "order": 1010,
    },
    {
        "pattern":   "not only … but also",
        "category":  "en_cohesion",
        "function":  "listing",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "ikki dalilni birlashtirish — «nafaqat ..., balki ... ham»",
        "attach":    "not only + X but also + Y",
        "form_rule": "Ikki tarafda <b>bir xil turdagi</b> bo‘lak turishi shart: "
                     "ot + ot, fe’l + fe’l (❌ <i>not only <u>cheap</u> but also <u>it saves "
                     "time</u></i>). Gap boshida kelsa <b>inversiya</b> talab qiladi: "
                     "<i><b>Not only does</b> it save money, <b>but</b> it <b>also</b> reduces "
                     "emissions.</i>",
        "note":      "<p>Ikki foydani bitta gapda berish — ixcham va ta’sirchan. Inversiyali "
                     "shakli Band 7.5+ belgisi, lekin <b>does/did/is</b> ni to‘g‘ri qo‘yish shart.</p>",
        "mistake":   "<p>❌ <i>Not only <u>it saves</u> money…</i> → ✅ <i>Not only <b>does it "
                     "save</b> money…</i></p>",
        "examples": [
            ("Cycling not only reduces congestion but also improves public health.",
             "Velosipedda yurish nafaqat tirbandlikni kamaytiradi, balki jamoat salomatligini ham yaxshilaydi."),
        ],
        "synonyms": [
            ("moreover / furthermore", "moreover = alohida jumla; not only…but also = bitta gap"),
            ("inversion", "gap boshida kelganda inversiya majburiy bo‘ladi"),
        ],
        "order": 1011,
    },
]
