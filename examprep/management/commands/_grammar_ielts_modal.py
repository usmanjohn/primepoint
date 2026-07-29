# -*- coding: utf-8 -*-
"""IELTS grammar bank — Modals & hedging (modal fe'llar).

Order decade 200-299. Half of this group is ordinary modality (must, should,
can); the other half is the band-7 skill of NOT overstating — `tend to`,
`may well`, `be likely to`. An essay that hedges its claims reads as reasoned;
one that does not reads as a slogan, and the examiner marks it accordingly.
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
        "pattern":   "must / have to",
        "category":  "en_modal",
        "function":  "obligation",
        "level":     2,
        "freq":      2,
        "register":  "both",
        "meaning":   "majburiyat — «shart, kerak»",
        "attach":    "S + must + V · S + have/has to + V",
        "form_rule": "<b>must</b> + yalang‘och fe’l (❌ must to go). <b>have to</b> esa zamonga "
                     "qarab o‘zgaradi: had to, will have to, has to. Shuning uchun o‘tgan yoki "
                     "kelasi zamonda <u>faqat</u> <b>have to</b> ishlaydi.",
        "note":      "<p>Farqi: <b>must</b> = ichki, so‘zlovchidan chiqqan majburiyat; "
                     "<b>have to</b> = tashqi qoida yoki vaziyat talabi.</p>"
                     "<p>⚠️ <b>mustn’t ≠ don’t have to.</b> <i>mustn’t</i> = taqiqlangan; "
                     "<i>don’t have to</i> = shart emas (lekin mumkin). Bu farq Listening’da "
                     "ham savol bo‘lib keladi.</p>",
        "mistake":   "<p>❌ Governments <u>must to</u> invest → ✅ Governments <b>must</b> invest.</p>"
                     "<p>❌ Task 2 da har jumlada <i>must</i> — juda buyruqona jaranglaydi. "
                     "Tavsiya bersangiz <b>should</b> yoki <b>ought to</b> ishlating.</p>",
        "examples": [
            ("Applicants must submit their documents before the deadline.",
             "Arizachilar hujjatlarini muddatdan oldin topshirishlari shart."),
            ("Students have to wear a uniform in most state schools.",
             "Ko‘pchilik davlat maktablarida o‘quvchilar forma kiyishi kerak."),
        ],
        "synonyms": [
            ("should / ought to", "must = majburiyat; should = tavsiya — insho uchun "
                                  "should xavfsizroq"),
            ("be required to", "be required to = rasmiy, majhul ohang: akademik yozuvda tabiiy"),
        ],
        "order": 200,
    },
    {
        "pattern":   "should / ought to",
        "category":  "en_modal",
        "function":  "obligation",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "tavsiya — «kerak, ma’qul bo‘lardi»",
        "attach":    "S + should + V · S + ought to + V",
        "form_rule": "<b>should</b> + yalang‘och fe’l · <b>ought to</b> + fe’l (yagona "
                     "<i>to</i> oladigan modal). O‘tmish uchun: <b>should have</b> + V3 "
                     "(«qilishi kerak edi, lekin qilmadi»).",
        "note":      "<p><b>Task 2 ning yechim (solution) qismidagi asosiy modal.</b> "
                     "Tayyor qolip: <i>Governments <b>should</b> invest more heavily in public "
                     "transport, and individuals <b>ought to</b> reconsider their daily habits.</i></p>"
                     "<p>Xilma-xillik uchun aralashtiring: should · ought to · it would be "
                     "advisable to · the best approach would be to.</p>",
        "mistake":   "<p>❌ I think government <u>should to</u> ban it → ✅ <b>should</b> ban it.</p>",
        "examples": [
            ("Schools should place greater emphasis on practical skills.",
             "Maktablar amaliy ko‘nikmalarga ko‘proq e’tibor qaratishi kerak."),
            ("Policymakers ought to consider the long-term consequences.",
             "Siyosat ishlab chiquvchilar uzoq muddatli oqibatlarni hisobga olishlari lozim."),
        ],
        "synonyms": [
            ("must / have to", "should = tavsiya, yumshoq; must = majburiyat, qat’iy"),
            ("had better", "had better = ogohlantirish ohangi bor («aks holda yomon bo‘ladi») "
                           "— insho uchun juda og‘zaki"),
        ],
        "order": 201,
    },
    {
        "pattern":   "can / could / be able to",
        "category":  "en_modal",
        "function":  "ability",
        "level":     2,
        "freq":      2,
        "register":  "both",
        "meaning":   "imkoniyat va qobiliyat — «... oladi, mumkin»",
        "attach":    "S + can/could + V · S + be able to + V",
        "form_rule": "<b>can</b> (hozir) · <b>could</b> (o‘tmishdagi umumiy qobiliyat yoki "
                     "yumshoq hozir) · <b>was able to</b> (o‘tmishda <u>bir marta</u> uddaladi) · "
                     "<b>will be able to</b> (kelajak — ❌ will can).",
        "note":      "<p>O‘tmishda bir martalik muvaffaqiyat uchun <b>was able to</b> kerak: "
                     "<i>The team <b>was able to</b> reduce costs by 20%</i> (❌ could reduce, "
                     "chunki <i>could</i> bu yerda «imkoni bor edi, ammo qildimi — noma’lum» "
                     "degan ma’no beradi).</p>",
        "mistake":   "<p>❌ In the future people <u>will can</u> work from home → "
                     "✅ <b>will be able to</b> work from home.</p>",
        "examples": [
            ("Renewable energy can significantly reduce carbon emissions.",
             "Qayta tiklanuvchi energiya uglerod chiqindilarini sezilarli kamaytira oladi."),
            ("Thanks to the scholarship, Sherbek was able to continue his studies.",
             "Stipendiya tufayli Sherbek o‘qishini davom ettira oldi."),
        ],
        "synonyms": [
            ("may / might / could (possibility)", "can = umumiy imkoniyat; may/might = "
                                                  "aniq bir holatning ehtimoli"),
        ],
        "order": 202,
    },
    {
        "pattern":   "may / might / could (possibility)",
        "category":  "en_modal",
        "function":  "hedging",
        "level":     4,
        "freq":      3,
        "register":  "both",
        "meaning":   "ehtimollik — «bo‘lishi mumkin»",
        "attach":    "S + may/might/could + V",
        "form_rule": "Uchalasi ham yalang‘och fe’l oladi. Ishonch darajasi: "
                     "<b>may</b> (~50%) > <b>might</b> (~40%) > <b>could</b> (nazariy imkoniyat). "
                     "O‘tmish uchun: <b>may/might have</b> + V3.",
        "note":      "<p><b>Band 7 ga chiqishning eng arzon yo‘li.</b> Har bir dalilni "
                     "«har doim shunday» deb emas, ehtimollik sifatida bering:</p>"
                     "<p>❌ <i>Banning cars solves air pollution.</i> → "
                     "✅ <i>Banning cars in city centres <b>may</b> significantly reduce air "
                     "pollution.</i> — ikkinchisi tekshiruvchiga o‘ylab yozilgandek ko‘rinadi.</p>",
        "mistake":   "<p>❌ <i>Maybe governments should…</i> — <i>maybe</i> og‘zaki. Insho uchun: "
                     "<b>may</b>, <b>possibly</b>, <b>it is possible that</b>.</p>",
        "examples": [
            ("Higher fuel taxes may discourage unnecessary car journeys.",
             "Yoqilg‘i solig‘ining oshirilishi keraksiz avtosafarlarni kamaytirishi mumkin."),
            ("Such a policy might have unintended consequences for low-income families.",
             "Bunday siyosat kam ta’minlangan oilalar uchun kutilmagan oqibatlarga olib kelishi mumkin."),
        ],
        "synonyms": [
            ("be likely to", "be likely to = ehtimol yuqoriroq va o‘lchovli; may = ochiq ehtimol"),
            ("can / could / be able to", "can = umuman mumkin; may = shu holatda ehtimol"),
        ],
        "order": 203,
    },
    {
        "pattern":   "be likely to",
        "category":  "en_modal",
        "function":  "hedging",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "ehtimoli yuqori — «... bo‘lishi ehtimoli katta»",
        "attach":    "S + be likely to + V · It is likely that + gap",
        "form_rule": "<b>be likely to</b> + fe’l, yoki <b>It is (highly/increasingly) likely "
                     "that</b> + to‘liq gap. Teskarisi: <b>be unlikely to</b>. "
                     "Kuchaytirish: <b>highly likely</b>, <b>far more likely</b>.",
        "note":      "<p>Akademik yozuvda <i>will</i> ning eng yaxshi o‘rinbosari: bashoratni "
                     "aytadi, lekin uni haqiqat sifatida da’vo qilmaydi. Task 2 xulosasi uchun "
                     "tayyor qolip: <i>Without decisive action, the problem <b>is likely to</b> "
                     "worsen over the coming decades.</i></p>",
        "mistake":   "<p>❌ It is likely <u>to happen that</u>… → ✅ It is likely <b>that</b> it "
                     "will happen · yoki ✅ It <b>is likely to</b> happen. Ikkovini aralashtirmang.</p>",
        "examples": [
            ("Cities with poor public transport are likely to suffer from congestion.",
             "Jamoat transporti yomon shaharlar tirbandlikdan aziyat chekishi ehtimoli katta."),
            ("It is highly unlikely that these measures will succeed on their own.",
             "Bu choralar yolg‘iz o‘zi muvaffaqiyat qozonishi ehtimoli juda past."),
        ],
        "synonyms": [
            ("may / might / could (possibility)", "may = ochiq ehtimol; be likely to = "
                                                  "ehtimoli yuqori, o‘lchangan"),
            ("will", "will = qat’iy bashorat; be likely to = ehtiyotkor bashorat"),
            ("tend to", "tend to = hozirgi tendensiya (kuzatilgan); be likely to = kelajak ehtimoli"),
        ],
        "order": 204,
    },
    {
        "pattern":   "tend to",
        "category":  "en_modal",
        "function":  "hedging",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "tendensiya — «odatda ... qiladi, moyil»",
        "attach":    "S + tend to + V · There is a tendency for X to + V",
        "form_rule": "<b>tend to</b> + fe’l · ot shakli: <b>a tendency to/for</b>. "
                     "Kuchaytirish: <b>tend to be far more…</b>",
        "note":      "<p>Umumlashtirishni xavfsiz qiladi. Har qanday «people are…» gapini "
                     "shu bilan yumshating:</p>"
                     "<p>❌ <i>Young people are addicted to social media.</i> → "
                     "✅ <i>Young people <b>tend to</b> spend considerably more time on social "
                     "media than older generations.</i></p>"
                     "<p>Task 1 da ham ishlaydi: <i>Figures for both countries <b>tended to</b> "
                     "fluctuate throughout the period.</i></p>",
        "examples": [
            ("Wealthier countries tend to consume far more energy per capita.",
             "Boyroq davlatlar aholi jon boshiga ancha ko‘p energiya iste’mol qilishga moyil."),
        ],
        "synonyms": [
            ("be likely to", "tend to = kuzatilgan hozirgi moyillik; be likely to = kelajak ehtimoli"),
            ("in general / on the whole", "bular ravish; tend to esa fe’lning o‘ziga singadi"),
        ],
        "order": 205,
    },
    {
        "pattern":   "it may well be that",
        "category":  "en_modal",
        "function":  "hedging",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "ehtiyotkor tan olish — «ehtimol, ... to‘g‘ridir»",
        "attach":    "It may well be that + to‘liq gap",
        "form_rule": "<b>It may well be that</b> + gap. Qisqaroq varianti: <b>may well</b> + fe’l "
                     "(<i>this may well explain…</i>).",
        "note":      "<p>Discussion (both views) inshosida qarshi tomonni tan olish uchun elegant "
                     "qolip: <i><b>It may well be that</b> online learning suits independent "
                     "students; <b>however</b>, it cannot replace laboratory work.</i></p>"
                     "<p>Bir insho ichida bir marta ishlating — bu «bezak» qolip.</p>",
        "examples": [
            ("It may well be that stricter penalties deter some offenders.",
             "Ehtimol, qattiqroq jazolar ba’zi huquqbuzarlarni qaytarar."),
        ],
        "synonyms": [
            ("may / might / could (possibility)", "bir xil ma’no, lekin bu qolip butun gapni "
                                                  "yumshatadi va rasmiyroq"),
            ("admittedly", "admittedly = ochiq tan olish; it may well be that = ehtimollik bilan tan olish"),
        ],
        "order": 206,
    },
    {
        "pattern":   "would",
        "category":  "en_modal",
        "function":  "hedging",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "farazli natija va muloyimlik — «... bo‘lardi»",
        "attach":    "S + would + V · S + would have + V3",
        "form_rule": "<b>would</b> + yalang‘och fe’l (hozir/kelajak farazi) · "
                     "<b>would have</b> + V3 (o‘tmish farazi). Speaking’da qisqaradi: <i>I’d</i>.",
        "note":      "<p>Ikki vazifasi IELTS uchun muhim:</p>"
                     "<ol><li><b>Taklifning natijasini aytish</b> — Task 2 yechim qismining "
                     "yuragi: <i>Such a policy <b>would</b> encourage more people to cycle.</i></li>"
                     "<li><b>Fikrni yumshatish</b> — <i>I <b>would</b> argue that…</i> "
                     "«men da’vo qilaman» dan ancha akademikroq.</li></ol>",
        "mistake":   "<p>❌ If governments <u>would</u> invest more, … → ✅ If governments "
                     "<b>invested</b> more, … — <i>if</i> tarafida <i>would</i> kelmaydi.</p>",
        "examples": [
            ("Investing in rail networks would reduce road congestion considerably.",
             "Temir yo‘l tarmog‘iga sarmoya kiritish yo‘l tirbandligini sezilarli kamaytirardi."),
            ("I would argue that the benefits outweigh the drawbacks.",
             "Menimcha, foydasi kamchiligidan ustun keladi."),
        ],
        "synonyms": [
            ("the second conditional", "second conditional aynan shu <i>would</i> ni "
                                       "<i>if</i>-gap bilan to‘ldiradi"),
            ("will", "will = haqiqiy bashorat; would = farazga bog‘liq natija"),
        ],
        "order": 207,
    },
    {
        "pattern":   "be expected to / be projected to",
        "category":  "en_modal",
        "function":  "guess",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "bashorat qilinmoqda — «... kutilmoqda, prognoz qilingan»",
        "attach":    "S + is/are expected to + V",
        "form_rule": "<b>be expected to</b> / <b>be projected to</b> / <b>be forecast to</b> + fe’l. "
                     "Majhul shakl — kim bashorat qilgani aytilmaydi, bu akademik uslubga mos.",
        "note":      "<p><b>Task 1 ning bashorat grafiklari uchun aynan shu kerak.</b> "
                     "Grafikda «projected», «forecast», «estimated» so‘zi yoki kelajak yili bo‘lsa: "
                     "<i>The urban population <b>is projected to</b> reach 70% by 2050.</i></p>",
        "mistake":   "<p>❌ The population <u>will reach</u> 70% by 2050 — grafik shunchaki "
                     "prognoz bo‘lsa, buni haqiqat sifatida aytmang.</p>",
        "examples": [
            ("Global demand for electricity is expected to rise by a third over the next decade.",
             "Elektr energiyasiga jahon talabi keyingi o‘n yilda uchdan birga oshishi kutilmoqda."),
        ],
        "synonyms": [
            ("will", "will = to‘g‘ridan-to‘g‘ri bashorat; be expected to = manbaga tayangan prognoz"),
            ("be likely to", "likely = ehtimol; expected/projected = rasmiy prognoz"),
        ],
        "order": 208,
    },
    {
        "pattern":   "it is said that / X is thought to",
        "category":  "en_modal",
        "function":  "quote",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "manbasi aytilmagan da’vo — «aytilishicha, hisoblanadi»",
        "attach":    "It is said/believed/thought that + gap · S + is said to + V",
        "form_rule": "Ikki shakl bir ma’noni beradi: <b>It is believed that</b> smoking causes… = "
                     "<b>Smoking is believed to</b> cause…. Ikkinchisi ixchamroq va akademikroq.",
        "note":      "<p>«Odamlar aytishadi» degan gapni akademik qiladi. Task 2 da umumiy qarashni "
                     "keltirib, keyin unga qarshi chiqish uchun qulay: <i>Homework <b>is widely "
                     "believed to</b> improve results, <b>yet</b> research suggests otherwise.</i></p>",
        "mistake":   "<p>❌ <i>People say that…</i> / <i>Some people think that…</i> — bu Band 5-6 "
                     "darajasidagi ifoda. Majhul shaklga o‘ting.</p>",
        "examples": [
            ("Air travel is widely believed to be the fastest-growing source of emissions.",
             "Havo transporti chiqindilarning eng tez o‘sib borayotgan manbai deb hisoblanadi."),
        ],
        "synonyms": [
            ("the passive", "bu — majhul nisbatning ko‘chirma gapdagi maxsus qolipi"),
            ("it is often argued that", "argued = bahsli fikr; believed/thought = keng tarqalgan qarash"),
        ],
        "order": 209,
    },
    {
        "pattern":   "need to / needn't",
        "category":  "en_modal",
        "function":  "obligation",
        "level":     3,
        "freq":      2,
        "register":  "both",
        "meaning":   "zaruriyat — «kerak; shart emas»",
        "attach":    "S + need to + V · S + needn’t + V",
        "form_rule": "Oddiy fe’l sifatida: <b>need to</b> + fe’l (needs to, needed to). "
                     "Modal sifatida faqat inkorda: <b>needn’t</b> + yalang‘och fe’l. "
                     "❌ needn’t to.",
        "note":      "<p>Task 2 da <i>must</i> dan ko‘ra tabiiyroq: <i>Policymakers <b>need to</b> "
                     "strike a balance between growth and sustainability.</i></p>"
                     "<p>⚠️ <b>needn’t have done</b> = «qilish shart emas edi, lekin qildingiz» — "
                     "Listening’da tuzoq sifatida keladi.</p>",
        "examples": [
            ("Universities need to adapt their courses to a changing job market.",
             "Universitetlar kurslarini o‘zgarayotgan mehnat bozoriga moslashtirishi kerak."),
        ],
        "synonyms": [
            ("must / have to", "need to = zaruriyat, neytral; must = majburiyat, qat’iy"),
        ],
        "order": 210,
    },
    {
        "pattern":   "modal + passive",
        "category":  "en_modal",
        "function":  "obligation",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "majhul modal — «... qilinishi kerak / mumkin»",
        "attach":    "S + modal + be + V3",
        "form_rule": "<b>modal</b> + <b>be</b> + 3-shakl: should <b>be introduced</b>, "
                     "must <b>be addressed</b>, can <b>be reduced</b>. "
                     "O‘tmish: modal + <b>have been</b> + V3.",
        "note":      "<p>Yechim taklif qilishning eng akademik shakli — kim qilishini aytmasdan "
                     "nima qilinishi kerakligini aytadi: <i>Stricter regulations <b>should be "
                     "introduced</b>, and public transport <b>must be made</b> more affordable.</i></p>"
                     "<p>Bitta insho ichida 2-3 marta — undan ko‘pi matnni sovuq qiladi.</p>",
        "mistake":   "<p>❌ This problem should <u>be solve</u> → ✅ should <b>be solved</b> — "
                     "<i>be</i> dan keyin doim 3-shakl.</p>",
        "examples": [
            ("Subsidies for fossil fuels should be phased out over the next decade.",
             "Qazib olinadigan yoqilg‘iga beriladigan subsidiyalar keyingi o‘n yilda bekor qilinishi kerak."),
        ],
        "synonyms": [
            ("the passive", "bu — passive’ning modal bilan birikkan shakli"),
            ("should / ought to", "should + be + V3 = tavsiyani shaxssiz qiladi"),
        ],
        "order": 211,
    },
]
