# -*- coding: utf-8 -*-
"""IELTS grammar bank — Prepositions & data language (predloglar).

Order decade 700-799. Half of this group is Task 1 machinery (`increase BY`
vs `increase TO`), the other half is the dependent prepositions that decide
whether a sentence is accurate: `result in` vs `result from`, `impact on`,
`responsible for`. Uzbek's case endings map onto none of them, so these are
learned as fixed pairs.
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
        "pattern":   "increase by / increase to",
        "category":  "en_prep",
        "function":  "change",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "o‘sish miqdori va yakuniy nuqtasi — «... ga oshdi» va «... gacha yetdi»",
        "attach":    "rise/increase by + farq · rise/increase to + natija",
        "form_rule": "<b>by</b> = qancha <u>o‘zgardi</u> (farq) · <b>to</b> = qayerga "
                     "<u>yetdi</u> (yakuniy raqam): <i>Sales rose <b>by</b> 20% (o‘sish "
                     "miqdori) <b>to</b> 60 million (yakuniy raqam).</i>",
        "note":      "<p><b>Task 1 dagi eng ko‘p uchraydigan xato aynan shu ikkisining "
                     "chalkashishi.</b> Bitta gapda ikkalasini birga ishlatsangiz, ekspert "
                     "darajasida ko‘rinadi: <i>The figure increased <b>by</b> 15 percentage "
                     "points, <b>from</b> 45% <b>to</b> 60%.</i></p>"
                     "<p>⚠️ <b>percent</b> va <b>percentage point</b> farq qiladi: 45% dan 60% ga "
                     "o‘sish = <b>15 percentage points</b>, lekin ~33% o‘sish.</p>",
        "mistake":   "<p>❌ <i>The number increased <u>to</u> 20%</i> — agar 20% o‘sish "
                     "miqdori bo‘lsa: ✅ <i>increased <b>by</b> 20%</i>.</p>",
        "examples": [
            ("Car ownership rose by 30% between 2000 and 2010.",
             "Avtomobilga egalik 2000-2010 yillarda 30% ga oshdi."),
            ("The proportion of renewable energy climbed to almost a quarter of total output.",
             "Qayta tiklanuvchi energiya ulushi umumiy ishlab chiqarishning deyarli chorak qismiga yetdi."),
        ],
        "synonyms": [
            ("from … to …", "from … to = boshlang‘ich va yakuniy nuqta; by = farq"),
            ("at (a rate / a level of)", "at = qayd etilgan daraja, o‘zgarish emas"),
        ],
        "order": 700,
    },
    {
        "pattern":   "from … to …",
        "category":  "en_prep",
        "function":  "change",
        "level":     2,
        "freq":      3,
        "register":  "written",
        "meaning":   "boshlang‘ich va yakuniy nuqta — «... dan ... gacha»",
        "attach":    "from X to Y (raqam yoki sana)",
        "form_rule": "<b>from … to …</b> raqamlar bilan ham, sanalar bilan ham ishlaydi. "
                     "Sana uchun muqobil: <b>between … and …</b> · <b>over the period …</b>. "
                     "Ikkalasini aralashtirmang: ❌ <i>between 1990 <u>to</u> 2000</i>.",
        "note":      "<p>Task 1 kirish va tana qismida takrorlanishdan qochish uchun uch xil "
                     "ayting: <i><b>from</b> 1990 <b>to</b> 2000</i> · <i><b>between</b> 1990 "
                     "<b>and</b> 2000</i> · <i><b>over the following decade</b></i>.</p>",
        "mistake":   "<p>❌ <i>The figure fell from 40% <u>until</u> 25%</i> → ✅ <i>fell "
                     "<b>from</b> 40% <b>to</b> 25%</i>.</p>",
        "examples": [
            ("Between 1995 and 2015, the figure for coal fell from 40% to just 12%.",
             "1995-2015 yillar oralig‘ida ko‘mir ko‘rsatkichi 40% dan atigi 12% gacha tushdi."),
        ],
        "synonyms": [
            ("increase by / increase to", "from…to = ikkala nuqta; by = ular orasidagi farq"),
        ],
        "order": 701,
    },
    {
        "pattern":   "at (a rate / a level of)",
        "category":  "en_prep",
        "function":  "degree",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "qayd etilgan daraja — «... darajasida, ... tezlikda»",
        "attach":    "stood at / peaked at / at a rate of",
        "form_rule": "<b>stand at</b> · <b>peak at</b> · <b>remain at</b> · <b>at a rate of</b> "
                     "— hammasi <b>at</b> oladi, chunki bu <u>nuqta</u>, harakat emas.",
        "note":      "<p>Task 1 da raqamni takrorlamasdan kiritishning eng qulay yo‘li: "
                     "<i>Consumption <b>stood at</b> 40 units in 2000 and <b>peaked at</b> "
                     "75 units a decade later.</i></p>",
        "examples": [
            ("Unemployment remained at around 5% throughout the period.",
             "Ishsizlik butun davr davomida taxminan 5% darajasida qoldi."),
        ],
        "synonyms": [
            ("increase by / increase to", "at = qimmatning o‘zi; by/to = o‘zgarish"),
        ],
        "order": 702,
    },
    {
        "pattern":   "in / on / at (time)",
        "category":  "en_prep",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "register":  "both",
        "meaning":   "vaqt predloglari — yil, kun, soat",
        "attach":    "in 2010 · on Monday · at 8 a.m.",
        "form_rule": "<b>in</b> — yil, oy, fasl, asr, «uzun» davr (<i>in the 1990s, in June, "
                     "in the future</i>) · <b>on</b> — aniq kun va sana (<i>on 5 May, on Friday</i>) · "
                     "<b>at</b> — aniq vaqt nuqtasi (<i>at 6 p.m., at night, at the weekend</i>).",
        "note":      "<p>Task 1 uchun kerakli qo‘shimchalar: <b>during</b> the period · "
                     "<b>throughout</b> the decade · <b>by</b> 2010 (shu vaqtga qadar) · "
                     "<b>over</b> the next five years · <b>within</b> a decade.</p>",
        "mistake":   "<p>❌ <i><u>In</u> 5 May</i> → ✅ <i><b>on</b> 5 May</i> · "
                     "❌ <i><u>In</u> the weekend</i> → ✅ <i><b>at</b> the weekend</i> (BrE).</p>",
        "examples": [
            ("In 2008 the figure peaked, and by 2012 it had fallen back to its earlier level.",
             "2008-yilda ko‘rsatkich cho‘qqiga chiqdi, 2012-yilga kelib esa avvalgi darajasiga qaytdi."),
        ],
        "synonyms": [
            ("from … to …", "in/on/at = bitta nuqta; from…to = oraliq"),
        ],
        "order": 703,
    },
    {
        "pattern":   "result in / result from",
        "category":  "en_prep",
        "function":  "result",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "sabab yo‘nalishi — «... ga olib keladi» va «... dan kelib chiqadi»",
        "attach":    "X results in Y · Y results from X",
        "form_rule": "<b>result in</b> = sabab → natija (<i>Deforestation results <b>in</b> "
                     "soil erosion</i>) · <b>result from</b> = natija ← sabab "
                     "(<i>Soil erosion results <b>from</b> deforestation</i>). "
                     "Yo‘nalish teskari — predlog buni hal qiladi.",
        "note":      "<p>Sabab-oqibatni ikki yo‘nalishda ayta olish Task 2 uchun juda foydali. "
                     "Shu oiladagi boshqalar: <b>lead to</b> · <b>give rise to</b> · "
                     "<b>bring about</b> · <b>stem from</b> · <b>arise from</b> · "
                     "<b>be attributed to</b>.</p>",
        "mistake":   "<p>❌ <i>The problem results <u>to</u> …</i> → ✅ <i>results <b>in</b></i>. "
                     "❌ <i>lead <u>into</u></i> → ✅ <i>lead <b>to</b></i>.</p>",
        "examples": [
            ("Rapid urbanisation has resulted in a severe shortage of affordable housing.",
             "Tez urbanizatsiya arzon uy-joyning keskin tanqisligiga olib keldi."),
            ("Much of the pollution results from outdated industrial equipment.",
             "Ifloslanishning katta qismi eskirgan sanoat uskunalaridan kelib chiqadi."),
        ],
        "synonyms": [
            ("due to / owing to / because of", "due to + OT (sabab); result in + OT (natija)"),
            ("therefore / consequently", "bular jumlalarni bog‘laydi; result in gap ichida ishlaydi"),
        ],
        "order": 704,
    },
    {
        "pattern":   "due to / owing to / because of",
        "category":  "en_prep",
        "function":  "reason",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "sabab — «... tufayli, ... sababli» (otdan oldin)",
        "attach":    "due to / because of + noun / -ing",
        "form_rule": "Uchalasi ham <u>ot yoki -ing</u> oladi, <b>gap emas</b>: "
                     "✅ <i>due to <b>the increase</b> in fuel prices</i> · "
                     "❌ <i>due to <u>fuel prices increased</u></i>. "
                     "Gap kerak bo‘lsa: <b>because</b> / <b>since</b> / "
                     "<b>due to the fact that</b>.",
        "note":      "<p>Nozik farq: <b>due to</b> qat’iy grammatikada <i>be</i> dan keyin keladi "
                     "(<i>The delay was <b>due to</b> heavy rain</i>), <b>owing to</b> esa butun "
                     "gapga bog‘lanadi. Imtihonda ikkalasi ham qabul qilinadi, lekin "
                     "<b>owing to</b> yozma uslubda ko‘proq ball beradi.</p>",
        "mistake":   "<p>❌ <i>Because of <u>the traffic is heavy</u>, I was late</i> → "
                     "✅ <i><b>Because</b> the traffic was heavy…</i> yoki "
                     "✅ <i><b>Because of</b> the heavy traffic…</i></p>",
        "examples": [
            ("Owing to a lack of investment, the rail network deteriorated steadily.",
             "Sarmoya yetishmagani tufayli temir yo‘l tarmog‘i asta-sekin yomonlashdi."),
        ],
        "synonyms": [
            ("because / since / as", "because + GAP; because of / due to + OT"),
            ("result in / result from", "due to = sababni kiritadi; result in = natijani kiritadi"),
            ("thanks to", "thanks to = faqat IJOBIY sabab uchun"),
        ],
        "order": 705,
    },
    {
        "pattern":   "an increase in / an impact on",
        "category":  "en_prep",
        "function":  "case",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "ot + predlog juftlari — «... dagi o‘sish», «... ga ta’sir»",
        "attach":    "noun + in/on/of/to + noun",
        "form_rule": "Yodlanadigan juftlar: an increase / a rise / a fall / a decline "
                     "<b>in</b> · an impact / an effect / pressure <b>on</b> · "
                     "a solution / an approach / access <b>to</b> · the cause / the number / "
                     "the proportion <b>of</b> · a reason <b>for</b>.",
        "note":      "<p>Nominalizatsiya bilan birga ishlatiladi va Task 1 ni takrorlanishdan "
                     "qutqaradi: <i>There was <b>a sharp increase in</b> demand</i> = "
                     "<i>Demand increased sharply</i> — bir xil ma’no, boshqa tuzilma.</p>",
        "mistake":   "<p>❌ <i>an increase <u>of</u> tourists</i> → ✅ <i>an increase <b>in</b> "
                     "the number of tourists</i> (<i>an increase of 20%</i> — bu miqdor, boshqa narsa).</p>"
                     "<p>❌ <i>impact <u>to</u> the environment</i> → ✅ <i>impact <b>on</b> "
                     "the environment</i>.</p>",
        "examples": [
            ("The policy had a significant impact on air quality in the city centre.",
             "Bu siyosat shahar markazidagi havo sifatiga sezilarli ta’sir ko‘rsatdi."),
        ],
        "synonyms": [
            ("nominalisation", "ot + predlog juftlari nominalizatsiyaning amaliy tomoni"),
            ("adjective + preposition", "bir oila: sifatning ham o‘z predlogi bor"),
        ],
        "order": 706,
    },
    {
        "pattern":   "adjective + preposition",
        "category":  "en_prep",
        "function":  "case",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "sifat + predlog juftlari — «... uchun javobgar», «... dan xabardor»",
        "attach":    "adj + of/for/to/with/in",
        "form_rule": "Eng kerakli juftlar: responsible <b>for</b> · aware <b>of</b> · "
                     "capable <b>of</b> · similar <b>to</b> · different <b>from</b> · "
                     "familiar <b>with</b> · dependent <b>on</b> · essential <b>to/for</b> · "
                     "interested <b>in</b> · concerned <b>about</b>.",
        "note":      "<p>Bularni qoida bilan chiqarib bo‘lmaydi — <b>juft holda yodlanadi</b>. "
                     "Lug‘at daftaringizga sifatni yolg‘iz emas, predlogi bilan yozing.</p>",
        "mistake":   "<p>❌ <i>different <u>than</u></i> (amerikacha) → Britaniya imtihonida "
                     "✅ <i>different <b>from</b></i> · ❌ <i>responsible <u>of</u></i> → "
                     "✅ <i>responsible <b>for</b></i>.</p>",
        "examples": [
            ("Industry is responsible for nearly a third of total emissions.",
             "Sanoat umumiy chiqindilarning deyarli uchdan bir qismi uchun javobgar."),
        ],
        "synonyms": [
            ("an increase in / an impact on", "bir oila — otning predlogi"),
            ("verb + preposition", "bir oila — fe’lning predlogi"),
        ],
        "order": 707,
    },
    {
        "pattern":   "verb + preposition",
        "category":  "en_prep",
        "function":  "case",
        "level":     4,
        "freq":      3,
        "register":  "both",
        "meaning":   "fe’l + predlog juftlari — «... ga bog‘liq», «... dan iborat»",
        "attach":    "verb + on/of/to/for/with",
        "form_rule": "depend <b>on</b> · consist <b>of</b> · contribute <b>to</b> · "
                     "lead <b>to</b> · account <b>for</b> · benefit <b>from</b> · "
                     "cope <b>with</b> · rely <b>on</b> · focus <b>on</b> · "
                     "invest <b>in</b> · suffer <b>from</b>. "
                     "⚠️ Predlogdan keyin fe’l kelsa — <b>-ing</b> shaklida.",
        "note":      "<p><b>account for</b> Task 1 uchun alohida muhim: <i>Coal <b>accounted "
                     "for</b> 40% of total output.</i> — foizni aytishning eng akademik yo‘li.</p>",
        "mistake":   "<p>❌ <i>discuss <u>about</u> the problem</i> → ✅ <i><b>discuss</b> the "
                     "problem</i> (predlog kerak emas) · ❌ <i>emphasise <u>on</u></i> → "
                     "✅ <i><b>emphasise</b> something</i>.</p>",
        "examples": [
            ("Renewable sources accounted for just under a fifth of electricity generation.",
             "Qayta tiklanuvchi manbalar elektr ishlab chiqarishning beshdan biriga yaqinini tashkil qildi."),
            ("The success of the scheme depends largely on public awareness.",
             "Loyihaning muvaffaqiyati ko‘p jihatdan aholining xabardorligiga bog‘liq."),
        ],
        "synonyms": [
            ("adjective + preposition", "bir oila — sifatning predlogi"),
            ("preposition + -ing", "predlogdan keyingi fe’l doim -ing shaklida"),
        ],
        "order": 708,
    },
    {
        "pattern":   "in terms of / with regard to",
        "category":  "en_prep",
        "function":  "reference",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "mavzuni belgilash — «... jihatdan, ... ga kelsak»",
        "attach":    "In terms of + noun, S + V",
        "form_rule": "<b>in terms of</b> / <b>with regard to</b> / <b>as far as X is concerned</b> "
                     "+ <u>ot yoki -ing</u>. Odatda gap boshida, vergul bilan.",
        "note":      "<p>Task 1 da bir ustundan ikkinchisiga o‘tishning tabiiy yo‘li: "
                     "<i><b>In terms of</b> energy consumption, the pattern was rather different.</i></p>"
                     "<p>Task 2 da esa yangi jihatga o‘tish uchun: <i><b>With regard to</b> cost, "
                     "the argument is less convincing.</i></p>",
        "mistake":   "<p>❌ <i>In terms of <u>the education is expensive</u></i> → "
                     "✅ <i>In terms of <b>cost</b>, education…</i> — faqat ot keladi.</p>",
        "examples": [
            ("In terms of overall spending, the two countries followed similar paths.",
             "Umumiy xarajatlar jihatidan ikki mamlakat o‘xshash yo‘ldan bordi."),
        ],
        "synonyms": [
            ("in contrast / on the other hand", "in terms of = mavzuni belgilaydi; "
                                                "in contrast = qarama-qarshi qo‘yadi"),
        ],
        "order": 709,
    },
    {
        "pattern":   "preposition + -ing",
        "category":  "en_prep",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "predlogdan keyingi fe’l — doim -ing shaklida",
        "attach":    "preposition + V-ing",
        "form_rule": "Har qanday predlogdan keyin fe’l <b>-ing</b> bo‘ladi: "
                     "<i>instead of <b>building</b></i> · <i>by <b>investing</b></i> · "
                     "<i>after <b>graduating</b></i> · <i>without <b>considering</b></i> · "
                     "<i>capable of <b>solving</b></i>. "
                     "⚠️ <b>to</b> ba’zan predlog: <i>look forward <b>to seeing</b></i>, "
                     "<i>be used <b>to living</b></i>.",
        "note":      "<p><b>by + -ing</b> — Task 2 yechim qismining eng ixcham qolipi: "
                     "<i><b>By investing</b> in public transport, cities can cut emissions "
                     "considerably.</i></p>",
        "mistake":   "<p>❌ <i>instead of <u>to build</u> new roads</i> → ✅ <i>instead of "
                     "<b>building</b> new roads</i>.</p>",
        "examples": [
            ("By raising fuel taxes, the government hopes to discourage unnecessary journeys.",
             "Yoqilg‘i solig‘ini oshirish orqali hukumat keraksiz safarlarni kamaytirmoqchi."),
        ],
        "synonyms": [
            ("verb + -ing (gerund)", "bir qoidaning ikki tomoni: fe’ldan keyin ham, "
                                     "predlogdan keyin ham -ing"),
            ("verb + preposition", "predlogli fe’ldan keyin ham -ing keladi"),
        ],
        "order": 710,
    },
]
