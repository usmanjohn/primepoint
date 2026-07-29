# -*- coding: utf-8 -*-
"""IELTS grammar bank — Advanced structures (murakkab tuzilmalar).

Order decade 1100-1199. The band-7.5+ group: inversion, cleft sentences,
participle clauses, the subjunctive. Every entry carries the same warning —
one well-placed example lifts an answer, three forced ones sink it, because
an examiner reads memorised structures as memorised.
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
        "pattern":   "inversion",
        "category":  "en_advanced",
        "function":  "emphasis",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "teskari tartib — ta’kid uchun ega va yordamchi fe’l o‘rin almashadi",
        "attach":    "Negative adverb + auxiliary + S + V",
        "form_rule": "Inkor yoki cheklov ma’nosidagi ravish gap boshiga chiqsa, <u>so‘roq "
                     "tartibi</u> keladi: <b>Rarely / Seldom / Never / Not only / Little / "
                     "Under no circumstances / Only when / No sooner</b> + <b>do/does/did/has/is</b> "
                     "+ ega + fe’l.",
        "note":      "<p>Ta’sirchan, lekin xavfli. <b>Bir inshoda bittadan ko‘p ishlatmang</b> va "
                     "faqat haqiqatan ta’kid kerak bo‘lgan joyda:</p>"
                     "<p><i><b>Rarely has</b> a single technology transformed daily life so "
                     "rapidly.</i><br><i><b>Only when</b> governments act together <b>will</b> "
                     "emissions fall.</i></p>",
        "mistake":   "<p>❌ <i>Never I <u>have seen</u>…</i> → ✅ <i>Never <b>have I</b> seen…</i> — "
                     "yordamchi fe’l egadan OLDIN turadi.</p>",
        "examples": [
            ("Not only does recycling reduce waste, but it also creates local employment.",
             "Qayta ishlash nafaqat chiqindini kamaytiradi, balki mahalliy ish o‘rinlari ham yaratadi."),
            ("Under no circumstances should safety standards be relaxed.",
             "Hech qanday holatda xavfsizlik standartlari yumshatilmasligi kerak."),
        ],
        "synonyms": [
            ("not only … but also", "gap boshida kelganda aynan shu inversiyani talab qiladi"),
            ("cleft sentence (It is … that)", "ikkalasi ham ta’kid vositasi — biri tartib, "
                                              "biri tuzilma orqali"),
            ("if it were not for", "Were it not for … = shart gapdagi inversiya"),
        ],
        "order": 1100,
    },
    {
        "pattern":   "cleft sentence (It is … that)",
        "category":  "en_advanced",
        "function":  "emphasis",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "ajratma gap — bir bo‘lakni ajratib ta’kidlaydi",
        "attach":    "It is X that/who + V · What … is …",
        "form_rule": "Ikki shakl: <b>It is</b> + ta’kidlanayotgan bo‘lak + <b>that/who</b> + "
                     "qolgan gap · <b>What</b> + gap + <b>is</b> + ta’kid. "
                     "<i>Governments must act</i> → <i><b>It is</b> governments <b>that</b> must "
                     "act</i> / <i><b>What</b> governments must do <b>is</b> act.</i>",
        "note":      "<p>Xulosada asosiy fikringizni ta’kidlash uchun juda mos: "
                     "<i><b>What is needed is</b> not more legislation but stricter enforcement.</i></p>",
        "mistake":   "<p>❌ <i>What is needed <u>are</u> stricter rules</i> → rasmiy yozuvda "
                     "✅ <i><b>is</b></i> (What = birlik).</p>",
        "examples": [
            ("It is the lack of enforcement, rather than the law itself, that causes the problem.",
             "Muammoni qonunning o‘zi emas, balki uning ijro etilmasligi keltirib chiqaradi."),
        ],
        "synonyms": [
            ("inversion", "ikkalasi ham ta’kid uchun — cleft xavfsizroq va tabiiyroq"),
            ("it is + adjective + that/to", "shakli o‘xshash, lekin vazifasi boshqa — u baho beradi"),
        ],
        "order": 1101,
    },
    {
        "pattern":   "participle clause",
        "category":  "en_advanced",
        "function":  "time",
        "level":     6,
        "freq":      2,
        "register":  "written",
        "meaning":   "ravishdosh oboroti — «... qilib; ... bo‘lgani uchun»",
        "attach":    "V-ing/V3 + …, S + V",
        "form_rule": "Aniq nisbat: <b>-ing</b> (<i><b>Having considered</b> both views, …</i>) · "
                     "Majhul: <b>V3</b> (<i><b>Faced with</b> rising costs, firms …</i>). "
                     "⚠️ <b>Ega bir xil bo‘lishi shart</b> — aks holda «dangling participle» "
                     "xatosi chiqadi.",
        "note":      "<p>Ikki gapni bittaga siqadi va matnni akademik qiladi:</p>"
                     "<p><i>Because the government had reduced subsidies, prices rose.</i> → "
                     "<i><b>Having reduced</b> subsidies, the government saw prices rise.</i></p>"
                     "<p>Sabab ma’nosida: <i><b>Given</b> the scale of the problem, …</i> — "
                     "bu tayyor va juda ishonchli qolip.</p>",
        "mistake":   "<p>❌ <i>Walking into the room, the lights were on.</i> — chiroqlar yurmaydi! "
                     "✅ <i>Walking into the room, <b>I</b> saw that the lights were on.</i></p>",
        "examples": [
            ("Given the rising cost of housing, many young people continue to live with their parents.",
             "Uy-joy narxining oshib borishini hisobga olsak, ko‘p yoshlar ota-onasi bilan yashashda davom etmoqda."),
            ("Having examined both sides, this essay argues that the benefits are greater.",
             "Ikkala tomonni ko‘rib chiqqach, ushbu insho foyda ko‘proq degan fikrni ilgari suradi."),
        ],
        "synonyms": [
            ("reduced relative clause", "reduced relative OTni aniqlaydi; participle clause "
                                        "butun gapga bog‘lanadi"),
            ("because / since / as", "participle clause = shu sababni ixchamroq aytish yo‘li"),
        ],
        "order": 1102,
    },
    {
        "pattern":   "the subjunctive (It is essential that …)",
        "category":  "en_advanced",
        "function":  "obligation",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "buyruq maylining rasmiy shakli — «... bo‘lishi shart»",
        "attach":    "It is essential that + S + V (yalang‘och)",
        "form_rule": "<b>essential / vital / imperative / crucial</b> yoki "
                     "<b>recommend / suggest / demand / insist</b> dan keyin <b>that</b> + ega + "
                     "<u>yalang‘och fe’l</u> — <i>-s</i> ham, <i>should</i> ham yo‘q: "
                     "<i>It is essential that every school <b>have</b> a library.</i> "
                     "(Britaniya uslubida <b>should have</b> ham to‘g‘ri.)",
        "note":      "<p>Eng rasmiy tavsiya shakli. Agar ishonchingiz komil bo‘lmasa, xavfsiz "
                     "varianti — <b>should</b> qo‘shish: <i>It is vital that governments "
                     "<b>should</b> act.</i> Ikkalasi ham qabul qilinadi.</p>",
        "mistake":   "<p>❌ <i>The committee recommended that he <u>goes</u></i> → "
                     "✅ <i>recommended that he <b>go</b></i> (yoki <b>should go</b>).</p>",
        "examples": [
            ("It is imperative that action be taken before the situation deteriorates further.",
             "Vaziyat yanada yomonlashishidan oldin chora ko‘rilishi shart."),
        ],
        "synonyms": [
            ("should / ought to", "should = oddiy tavsiya; subjunctive = eng rasmiy shakl"),
            ("it is + adjective + that/to", "shu qolipning oddiy, xavfsiz varianti"),
        ],
        "order": 1103,
    },
    {
        "pattern":   "emphatic do",
        "category":  "en_advanced",
        "function":  "emphasis",
        "level":     6,
        "freq":      1,
        "register":  "both",
        "meaning":   "ta’kidlovchi do — «haqiqatan ham ... qiladi»",
        "attach":    "S + do/does/did + V (yalang‘och)",
        "form_rule": "Tasdiq gapga <b>do/does/did</b> qo‘shiladi va asosiy fe’l yalang‘och "
                     "qoladi: <i>Technology <b>does</b> offer real benefits.</i>",
        "note":      "<p>Qarshi tomonni tan olib, keyin o‘z fikringizga qaytish uchun juda mos: "
                     "<i>Online learning <b>does</b> provide flexibility; <b>however</b>, it "
                     "cannot replicate classroom interaction.</i> — bu «muvozanatli fikr» "
                     "taassurotini beradi.</p>",
        "mistake":   "<p>❌ <i>It does <u>offers</u></i> → ✅ <i>It does <b>offer</b></i>.</p>",
        "examples": [
            ("Stricter penalties do deter some offenders, but they do not address the root cause.",
             "Qattiqroq jazolar ba’zi huquqbuzarlarni qaytaradi, biroq ular asosiy sababni hal qilmaydi."),
        ],
        "synonyms": [
            ("cleft sentence (It is … that)", "ikkalasi ham ta’kid — do fe’lni, cleft bo‘lakni ta’kidlaydi"),
            ("admittedly", "admittedly = tan olishni ochiq aytadi; emphatic do = uni fe’l bilan beradi"),
        ],
        "order": 1104,
    },
    {
        "pattern":   "admittedly",
        "category":  "en_advanced",
        "function":  "concession",
        "level":     5,
        "freq":      1,
        "register":  "written",
        "meaning":   "tan olish — «tan olish kerakki, ...»",
        "attach":    "Admittedly, + S + V",
        "form_rule": "<b>Admittedly,</b> jumla boshida vergul bilan. Shu oiladagilar: "
                     "<b>Granted,</b> · <b>It is true that</b> · <b>While it is true that</b> · "
                     "<b>Of course,</b>. Keyin deyarli doim <b>however</b> yoki <b>nevertheless</b> keladi.",
        "note":      "<p>«Tan olish → rad etish» — Band 7 ning eng ishonchli xatboshi tuzilmasi:</p>"
                     "<p><i><b>Admittedly</b>, private cars offer unmatched convenience. "
                     "<b>Nevertheless</b>, the environmental cost of mass car ownership is "
                     "difficult to justify.</i></p>",
        "examples": [
            ("Admittedly, such reforms would be expensive in the short term.",
             "Tan olish kerakki, bunday islohotlar qisqa muddatda qimmatga tushardi."),
        ],
        "synonyms": [
            ("although / though / even though", "although = bir gap ichida; admittedly = "
                                                "butun xatboshini boshlaydi"),
            ("it may well be that", "ikkalasi ham qarshi tomonni tan oladi — biri ehtimol bilan"),
        ],
        "order": 1105,
    },
    {
        "pattern":   "far from being",
        "category":  "en_advanced",
        "function":  "contrast",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "kutilganning aksi — «... bo‘lish o‘rniga, aksincha»",
        "attach":    "Far from + V-ing, S + V",
        "form_rule": "<b>Far from</b> + <b>-ing</b> (yoki ot), keyin vergul va asosiy gap: "
                     "<i><b>Far from solving</b> the problem, this policy made it worse.</i>",
        "note":      "<p>Kuchli rad etish qolipi — qarshi fikrni faqat inkor qilibgina qolmay, "
                     "uni teskarisiga aylantiradi. Xulosada yoki eng kuchli dalilingizda "
                     "bir marta ishlating.</p>",
        "examples": [
            ("Far from reducing inequality, the reform widened the gap between rich and poor.",
             "Tengsizlikni kamaytirish o‘rniga, islohot boy va kambag‘al orasidagi tafovutni kengaytirdi."),
        ],
        "synonyms": [
            ("participle clause", "shakli bir xil (-ing), lekin ma’nosi «aksincha»"),
            ("in contrast / on the other hand", "far from = kutilgan natijaning teskarisini ta’kidlaydi"),
        ],
        "order": 1106,
    },
    {
        "pattern":   "whereby / thereby",
        "category":  "en_advanced",
        "function":  "result",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "vosita va natija — «shu orqali; shu yo‘l bilan»",
        "attach":    "…, thereby + V-ing · a system whereby + clause",
        "form_rule": "<b>thereby</b> + <b>-ing</b> — natijani qo‘shadi "
                     "(<i>…, <b>thereby reducing</b> costs</i>) · "
                     "<b>whereby</b> = «unga ko‘ra» — tizim yoki tartibni tavsiflaydi "
                     "(<i>a scheme <b>whereby</b> firms pay for emissions</i>).",
        "note":      "<p><b>thereby + -ing</b> ikkinchi gapni boshlamasdan natijani qo‘shadi — "
                     "juda zich va akademik: <i>Congestion charges discourage driving, "
                     "<b>thereby improving</b> air quality.</i></p>",
        "mistake":   "<p>❌ <i>thereby <u>it reduces</u> costs</i> → ✅ <i>thereby <b>reducing</b> "
                     "costs</i> — <i>thereby</i> dan keyin -ing.</p>",
        "examples": [
            ("Governments could introduce a system whereby households are rewarded for recycling.",
             "Hukumatlar xonadonlar qayta ishlash uchun rag‘batlantiriladigan tizim joriy qilishi mumkin."),
        ],
        "synonyms": [
            ("therefore / consequently", "therefore = yangi jumla; thereby = shu gapga qo‘shiladi"),
            ("participle clause", "thereby + -ing — natija bildiruvchi ravishdosh oboroti"),
        ],
        "order": 1107,
    },
]
