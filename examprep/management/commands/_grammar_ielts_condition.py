# -*- coding: utf-8 -*-
"""IELTS grammar bank — Conditionals & unreal past (shart gaplar).

Order decade 400-499. Task 2's whole "what would happen if we did X" machinery
lives here, and so does Speaking Part 3, where every third question is
hypothetical. The Uzbek learner's classic error — `if ... would` on both sides —
gets its own warning on nearly every row.
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
        "pattern":   "the zero conditional",
        "category":  "en_condition",
        "function":  "condition",
        "level":     2,
        "freq":      2,
        "register":  "both",
        "meaning":   "umumiy haqiqat sharti — «agar ... bo‘lsa, doim ... bo‘ladi»",
        "attach":    "If + present simple, present simple",
        "form_rule": "Ikkala tarafda ham <b>present simple</b>. Bu yerda <b>if</b> ni "
                     "<b>when</b> bilan almashtirsa ham ma’no o‘zgarmaydi — shu belgi orqali "
                     "zero conditional ekanini bilasiz.",
        "note":      "<p>Ilmiy va umumiy haqiqatlar uchun — Task 2 ning tushuntirish qismida "
                     "sabab-oqibat mexanizmini ko‘rsatadi: <i><b>If</b> demand rises, prices "
                     "<b>increase</b>.</i></p>",
        "examples": [
            ("If forests are cleared, soil erosion accelerates.",
             "Agar o‘rmonlar kesilsa, tuproq eroziyasi tezlashadi."),
        ],
        "synonyms": [
            ("the first conditional", "zero = doimiy haqiqat; first = kelajakdagi aniq bir holat"),
        ],
        "order": 400,
    },
    {
        "pattern":   "the first conditional",
        "category":  "en_condition",
        "function":  "condition",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "real shart — «agar ... bo‘lsa, ... bo‘ladi» (kelajakda mumkin)",
        "attach":    "If + present simple, will + V",
        "form_rule": "<b>If</b> + <u>present</u> (❌ if it will rain), asosiy gapda "
                     "<b>will / may / can / should</b>. <i>will</i> o‘rniga boshqa modal ham "
                     "bo‘lishi mumkin: <i>If costs fall, more people <b>may</b> switch.</i>",
        "note":      "<p>Task 2 ogohlantirish jumlasi uchun tayyor qolip: "
                     "<i><b>If</b> governments fail to act now, the problem <b>will</b> become "
                     "far harder to solve.</i></p>"
                     "<p><b>Unless</b> bilan ham xuddi shu ma’no: <i><b>Unless</b> governments act, …</i></p>",
        "mistake":   "<p>❌ If the government <u>will invest</u> more, … → ✅ If the government "
                     "<b>invests</b> more, … — bu eng ko‘p uchraydigan xato.</p>",
        "examples": [
            ("If cities expand without planning, congestion will worsen.",
             "Agar shaharlar rejasiz kengaysa, tirbandlik yomonlashadi."),
        ],
        "synonyms": [
            ("the second conditional", "first = real ehtimol; second = xayoliy yoki ehtimoli past"),
            ("unless", "unless = «agar ... bo‘lmasa» — inkorli first conditional"),
        ],
        "order": 401,
    },
    {
        "pattern":   "the second conditional",
        "category":  "en_condition",
        "function":  "condition",
        "level":     4,
        "freq":      3,
        "register":  "both",
        "meaning":   "xayoliy shart — «agar ... bo‘lganida, ... bo‘lardi» (hozir/kelajak)",
        "attach":    "If + past simple, would + V",
        "form_rule": "<b>If</b> + <u>past simple</u>, asosiy gapda <b>would / could / might</b> + "
                     "yalang‘och fe’l. Rasmiy uslubda <i>be</i> ning shakli <b>were</b> bo‘ladi: "
                     "<i>If the policy <b>were</b> adopted…</i> (❌ was — Writing’da).",
        "note":      "<p><b>Task 2 yechim qismining eng kuchli qolipi</b> — taklifning natijasini "
                     "ko‘rsatadi: <i><b>If</b> public transport <b>were</b> free, far fewer people "
                     "<b>would</b> drive to work.</i></p>"
                     "<p>Speaking Part 3 dagi «What would happen if…» savollari ham aynan shu "
                     "shaklni kutadi.</p>",
        "mistake":   "<p>❌ If I <u>would have</u> more time, I would travel → "
                     "✅ If I <b>had</b> more time, I would travel. "
                     "<u>if</u> tarafida hech qachon <i>would</i> yo‘q.</p>",
        "examples": [
            ("If universities lowered their fees, more students would enrol.",
             "Agar universitetlar to‘lovni kamaytirsa, ko‘proq talaba o‘qishga kirardi."),
            ("If I were the mayor, I would invest in cycling infrastructure.",
             "Agar men hokim bo‘lganimda, velosiped infratuzilmasiga sarmoya kiritardim."),
        ],
        "synonyms": [
            ("the first conditional", "second = xayoliy/ehtimoli past; first = real ehtimol"),
            ("the third conditional", "second = hozir yoki kelajak; third = o‘tmish, o‘zgartirib bo‘lmaydi"),
            ("would", "second conditional — <i>would</i> ning shart bilan to‘ldirilgan shakli"),
        ],
        "order": 402,
    },
    {
        "pattern":   "the third conditional",
        "category":  "en_condition",
        "function":  "condition",
        "level":     5,
        "freq":      2,
        "register":  "both",
        "meaning":   "o‘tmishdagi xayoliy shart — «agar ... bo‘lganida edi, ... bo‘lardi»",
        "attach":    "If + past perfect, would have + V3",
        "form_rule": "<b>If</b> + <b>had</b> + V3, asosiy gapda <b>would/could/might have</b> + V3. "
                     "Ikki tarafda ham «perfect» bor — shuni yodda tuting.",
        "note":      "<p>O‘tmishdagi xatoni tahlil qiladi — Task 2 da tarixiy misol keltirganda "
                     "ishlaydi: <i><b>If</b> stricter rules <b>had been introduced</b> in the 1990s, "
                     "emissions <b>would have peaked</b> far earlier.</i></p>"
                     "<p>Speaking Part 2 da afsus bildirish uchun ham tabiiy.</p>",
        "mistake":   "<p>❌ If I <u>would have known</u> → ✅ If I <b>had known</b>. "
                     "<i>would have</i> faqat ikkinchi tarafda.</p>",
        "examples": [
            ("If the factory had installed filters earlier, the river would not have been polluted.",
             "Agar zavod filtrlarni ertaroq o‘rnatganida, daryo ifloslanmagan bo‘lardi."),
        ],
        "synonyms": [
            ("the second conditional", "third = o‘tmish (o‘zgarmas); second = hozir/kelajak"),
            ("the mixed conditional", "mixed = o‘tmishdagi shart, hozirgi natija"),
            ("past perfect", "third conditional shart tarafida aynan past perfect turadi"),
        ],
        "order": 403,
    },
    {
        "pattern":   "the mixed conditional",
        "category":  "en_condition",
        "function":  "condition",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "aralash shart — o‘tmishdagi shart, hozirgi natija",
        "attach":    "If + past perfect, would + V (hozir)",
        "form_rule": "<b>If</b> + had + V3 (o‘tmish sharti), asosiy gapda <b>would</b> + "
                     "yalang‘och fe’l (hozirgi natija) — «have» yo‘q.",
        "note":      "<p>Band 7.5+ belgisi, chunki ikki vaqtni bitta gapda ushlab turadi: "
                     "<i><b>If</b> the government <b>had invested</b> in rail in the 1980s, "
                     "the country <b>would have</b> a modern network today.</i></p>"
                     "<p>Bir marta, o‘rniga tushib ishlatilsa — juda kuchli. Zo‘rlab tiqilsa — xato.</p>",
        "examples": [
            ("If she had studied medicine, she would be a doctor now.",
             "Agar u tibbiyotni o‘qiganida, hozir shifokor bo‘lardi."),
        ],
        "synonyms": [
            ("the third conditional", "third = natija ham o‘tmishda; mixed = natija hozirda"),
        ],
        "order": 404,
    },
    {
        "pattern":   "unless",
        "category":  "en_condition",
        "function":  "condition",
        "level":     4,
        "freq":      3,
        "register":  "both",
        "meaning":   "«agar ... bo‘lmasa» — inkor shart",
        "attach":    "Unless + S + V (tasdiq), S + will + V",
        "form_rule": "<b>unless</b> ning o‘zi «if not» degani — shuning uchun ichida "
                     "<u>yana inkor kelmaydi</u>: ❌ unless we <u>don’t</u> act → "
                     "✅ <b>unless we act</b>.",
        "note":      "<p>Task 2 xulosasining eng ishonchli jumlasi: <i><b>Unless</b> urgent "
                     "measures are taken, these problems will only intensify.</i></p>",
        "mistake":   "<p>❌ <i>Unless the government doesn’t act, the crisis will deepen.</i> — "
                     "ikkita inkor ma’noni teskari qiladi. ✅ <i>Unless the government acts…</i></p>",
        "examples": [
            ("Unless recycling becomes compulsory, landfill waste will keep rising.",
             "Agar qayta ishlash majburiy qilinmasa, poligon chiqindilari o‘sishda davom etadi."),
        ],
        "synonyms": [
            ("the first conditional", "unless = «if not» — first conditional’ning inkor shakli"),
            ("provided that / as long as", "provided that = ijobiy shart; unless = inkor shart"),
        ],
        "order": 405,
    },
    {
        "pattern":   "provided that / as long as",
        "category":  "en_condition",
        "function":  "condition",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "shart bilan rozilik — «... shart bilan, toki ... ekan»",
        "attach":    "S + V, provided that + S + V",
        "form_rule": "<b>provided (that)</b> / <b>providing that</b> / <b>as long as</b> / "
                     "<b>on condition that</b> + present simple. Ma’nosi <i>if</i> ga yaqin, "
                     "lekin «faqat shu shart bajarilsa» degan cheklovni qo‘shadi.",
        "note":      "<p>Muvozanatli xulosa yozishning eng oson yo‘li — bir tomonni to‘liq "
                     "rad etmasdan shart qo‘yasiz: <i>Tourism can benefit local communities, "
                     "<b>provided that</b> profits are reinvested locally.</i></p>"
                     "<p>Bu «to what extent do you agree» tipidagi savollar uchun juda mos.</p>",
        "examples": [
            ("Technology improves education, as long as teachers are properly trained.",
             "Texnologiya ta’limni yaxshilaydi, toki o‘qituvchilar yetarli tayyorgarlikka ega bo‘lsa."),
        ],
        "synonyms": [
            ("unless", "provided that = ijobiy shart; unless = inkor shart"),
            ("the first conditional", "provided that = if, lekin cheklov ohangi kuchliroq"),
        ],
        "order": 406,
    },
    {
        "pattern":   "in case",
        "category":  "en_condition",
        "function":  "purpose",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "ehtiyot chorasi — «... bo‘lib qolsa deb, oldindan»",
        "attach":    "S + V + in case + S + V (present)",
        "form_rule": "<b>in case</b> + present simple — kelasi zamon ishlatilmaydi. "
                     "⚠️ <b>in case ≠ if</b>: <i>if</i> = shart bajarilgach qilamiz; "
                     "<i>in case</i> = shart bajarilishi <u>mumkinligi uchun oldindan</u> qilamiz.",
        "note":      "<p><i>Take an umbrella <b>in case</b> it rains</i> = yomg‘ir yog‘masidan "
                     "OLDIN olib chiqasiz. <i>Take an umbrella <b>if</b> it rains</i> = yog‘gandan "
                     "keyin olasiz. Bu farq Listening’da savol bo‘lib keladi.</p>",
        "examples": [
            ("Cities are building flood defences in case sea levels rise faster than expected.",
             "Shaharlar dengiz sathi kutilganidan tez ko‘tarilishi ehtimoliga qarshi to‘g‘onlar qurmoqda."),
        ],
        "synonyms": [
            ("the first conditional", "if = shart bajarilsa; in case = shart ehtimoliga qarshi oldindan"),
        ],
        "order": 407,
    },
    {
        "pattern":   "I wish / if only",
        "category":  "en_condition",
        "function":  "feeling",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "afsus va orzu — «... bo‘lganida edi»",
        "attach":    "I wish + past simple / past perfect",
        "form_rule": "Hozirgi holatga afsus: <b>wish</b> + <u>past simple</u> "
                     "(<i>I wish I <b>had</b> more time</i>) · "
                     "O‘tmishga afsus: <b>wish</b> + <u>past perfect</u> "
                     "(<i>I wish I <b>had studied</b> harder</i>) · "
                     "Boshqa odamning xatti-harakatidan norozilik: <b>wish</b> + <b>would</b>.",
        "note":      "<p>Speaking Part 2 da hikoyani chuqurlashtiradi: <i>I <b>wish</b> I <b>had "
                     "known</b> about the scholarship earlier.</i> Writing’da esa kam ishlating — "
                     "shaxsiy ohangi bor.</p>",
        "mistake":   "<p>❌ I wish I <u>would have</u> studied → ✅ I wish I <b>had</b> studied.</p>",
        "examples": [
            ("If only more people had taken the warnings seriously.",
             "Koshki ko‘proq odam ogohlantirishlarni jiddiy qabul qilganida."),
        ],
        "synonyms": [
            ("the third conditional", "ikkalasi ham o‘tmishdagi xayoliy holat — biri afsus, "
                                      "biri sabab-natija"),
        ],
        "order": 408,
    },
    {
        "pattern":   "it's time + past simple",
        "category":  "en_condition",
        "function":  "obligation",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "kechikkan zaruriyat — «endi ... qiladigan vaqt keldi»",
        "attach":    "It is (high) time + S + past simple",
        "form_rule": "<b>It is time</b> / <b>It is high time</b> + ega + <u>past simple</u> "
                     "(shakli o‘tmish, ma’nosi hozir): <i>It is high time governments <b>took</b> "
                     "this seriously.</i> Muqobil: <b>It is time to</b> + fe’l.",
        "note":      "<p>Xulosaga kuch beradigan, lekin kam ishlatiladigan qolip. Bir insho ichida "
                     "bir marta — va faqat da’vongiz qat’iy bo‘lsa.</p>",
        "mistake":   "<p>❌ It is high time governments <u>take</u> action → ✅ <b>took</b> action.</p>",
        "examples": [
            ("It is high time schools reconsidered the amount of homework they set.",
             "Maktablar beradigan uy vazifasi hajmini qayta ko‘rib chiqish vaqti allaqachon keldi."),
        ],
        "synonyms": [
            ("should / ought to", "should = neytral tavsiya; it's high time = kechikkanini ta’kidlaydi"),
        ],
        "order": 409,
    },
    {
        "pattern":   "if it were not for",
        "category":  "en_condition",
        "function":  "condition",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "«... bo‘lmaganida edi» — bitta omilga bog‘liq natija",
        "attach":    "If it were not for + noun, S + would + V",
        "form_rule": "Hozir: <b>If it were not for</b> + ot · O‘tmish: <b>If it had not been "
                     "for</b> + ot. Rasmiy inversiya shakli: <b>Were it not for</b> … / "
                     "<b>Had it not been for</b> …",
        "note":      "<p>Bitta omilning hal qiluvchi rolini ta’kidlaydi: <i><b>Were it not for</b> "
                     "government subsidies, the industry would have collapsed.</i> — inversiya "
                     "bilan Band 7.5+ ohangini beradi.</p>",
        "examples": [
            ("If it were not for remittances, many rural households would struggle.",
             "Chetdan kelayotgan pul o‘tkazmalari bo‘lmaganida, ko‘p qishloq xonadonlari qiynalgan bo‘lardi."),
        ],
        "synonyms": [
            ("the second conditional", "bu — second/third conditional’ning «bitta omil» varianti"),
            ("inversion", "Were it not for … = shu qolipning inversiyali shakli"),
        ],
        "order": 410,
    },
]
