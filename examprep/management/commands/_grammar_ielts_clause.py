# -*- coding: utf-8 -*-
"""IELTS grammar bank — Clauses (ergash gaplar).

Order decade 300-399. "Complex sentences" in the band descriptors means these:
relative, noun and adverbial clauses. A candidate who can attach a which-clause
and an although-clause correctly is already writing band-6.5 sentences.
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
        "pattern":   "defining relative clause",
        "category":  "en_clause",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "aniqlovchi ergash gap — qaysi narsa haqida ketayotganini belgilaydi",
        "attach":    "noun + who/which/that + verb",
        "form_rule": "Odam → <b>who</b> (yoki that) · narsa → <b>which</b> yoki <b>that</b> · "
                     "egalik → <b>whose</b>. <u>Vergul qo‘yilmaydi.</u> "
                     "Agar <i>who/which</i> to‘ldiruvchi bo‘lsa, tushirib qoldirsa ham bo‘ladi: "
                     "<i>the skills (that) employers value</i>.",
        "note":      "<p>Ergash gapsiz ikkita qisqa gap bo‘lardi; u bilan bitta murakkab gap "
                     "chiqadi — Grammatical Range aynan shuni izlaydi:</p>"
                     "<p><i>Students <b>who</b> take a gap year often return more motivated.</i></p>",
        "mistake":   "<p>❌ Students <u>who they</u> take a gap year → ✅ Students <b>who</b> take… "
                     "— <i>who</i> ning o‘zi ega, ikkinchi olmosh keraksiz.</p>"
                     "<p>❌ People <u>which</u> live in cities → ✅ People <b>who</b> live in cities.</p>",
        "examples": [
            ("Countries which invest in education tend to grow faster.",
             "Ta’limga sarmoya kiritadigan davlatlar tezroq rivojlanishga moyil."),
            ("The graph shows the number of people who used public transport.",
             "Grafik jamoat transportidan foydalangan odamlar sonini ko‘rsatadi."),
        ],
        "synonyms": [
            ("non-defining relative clause", "defining = vergulsiz, MAJBURIY ma’lumot; "
                                             "non-defining = vergul bilan, qo‘shimcha ma’lumot"),
            ("reduced relative clause", "reduced = who/which tushib, -ing yoki V3 qoladi"),
        ],
        "order": 300,
    },
    {
        "pattern":   "non-defining relative clause",
        "category":  "en_clause",
        "function":  "case",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "izohlovchi ergash gap — qo‘shimcha ma’lumot beradi (vergul bilan)",
        "attach":    ", which/who + verb ,",
        "form_rule": "Har doim <b>vergul</b> bilan ajratiladi va <b>that</b> ISHLATILMAYDI: "
                     "❌ Tashkent, that is the capital… → ✅ Tashkent, <b>which</b> is the capital…. "
                     "Butun gapga ishora qilishi ham mumkin: <i>…, <b>which</b> explains the rise.</i>",
        "note":      "<p>Task 1 uchun ajoyib vosita — raqamga izoh qo‘shadi: "
                     "<i>The figure peaked in 2008, <b>which</b> coincided with the financial crisis.</i></p>"
                     "<p>Bu «gapga ishora qiluvchi which» Band 7 belgisi, lekin faqat vergul "
                     "bilan to‘g‘ri ishlatilsa.</p>",
        "mistake":   "<p>❌ The number rose sharply <u>which</u> was surprising → vergul qo‘ying: "
                     "✅ rose sharply<b>,</b> which was surprising.</p>",
        "examples": [
            ("Online courses, which have grown rapidly since 2020, reach students in remote areas.",
             "2020-yildan beri jadal o‘sgan onlayn kurslar chekka hududlardagi talabalarga yetib boradi."),
        ],
        "synonyms": [
            ("defining relative clause", "non-defining = vergul + qo‘shimcha izoh; "
                                         "defining = vergulsiz va ma’noni belgilaydi"),
        ],
        "order": 301,
    },
    {
        "pattern":   "preposition + which",
        "category":  "en_clause",
        "function":  "case",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "predlogli ergash gap — «... bo‘lgan/qilinadigan»",
        "attach":    "noun + in/for/to + which + clause",
        "form_rule": "Predlog <b>which/whom</b> dan oldin keladi: <i>the rate <b>at which</b> "
                     "forests disappear</i> · <i>the extent <b>to which</b> …</i> · "
                     "<i>the way <b>in which</b> …</i>. Odam bilan: <b>whom</b> "
                     "(❌ for who → ✅ for <b>whom</b>).",
        "note":      "<p><b>«The extent to which»</b> — IELTS savol matnining o‘zida uchraydigan "
                     "ibora («To what extent do you agree?»), shuning uchun uni javobda "
                     "qaytarish juda tabiiy: <i>This essay will examine <b>the extent to which</b> "
                     "technology has reshaped education.</i></p>",
        "examples": [
            ("The speed at which the population is ageing has alarmed policymakers.",
             "Aholining qarish tezligi siyosat ishlab chiquvchilarni tashvishga solmoqda."),
        ],
        "synonyms": [
            ("defining relative clause", "bu — o‘sha ergash gapning predlogli, rasmiyroq varianti"),
        ],
        "order": 302,
    },
    {
        "pattern":   "reduced relative clause",
        "category":  "en_clause",
        "function":  "case",
        "level":     6,
        "freq":      1,
        "register":  "written",
        "meaning":   "qisqargan ergash gap — «who/which + be» tushirilgan shakl",
        "attach":    "noun + V-ing / V3 (+ …)",
        "form_rule": "Aniq nisbat → <b>-ing</b>: <i>students <u>who study</u> abroad</i> = "
                     "<i>students <b>studying</b> abroad</i>. "
                     "Majhul → <b>V3</b>: <i>the policy <u>which was introduced</u> in 2019</i> = "
                     "<i>the policy <b>introduced</b> in 2019</i>.",
        "note":      "<p>Ixchamlik — akademik uslubning belgisi. Bitta insho ichida 2-3 marta "
                     "ishlatilsa, matn zich va yetuk ko‘rinadi.</p>"
                     "<p>Task 1 da ayniqsa qulay: <i>the figure <b>recorded</b> in 2010</i>, "
                     "<i>countries <b>experiencing</b> rapid growth</i>.</p>",
        "mistake":   "<p>❌ People <u>lived</u> in rural areas have less access… → "
                     "✅ People <b>living</b> in rural areas… (odamlar o‘zi yashaydi — aniq nisbat).</p>",
        "examples": [
            ("The measures introduced last year have already reduced traffic by 10%.",
             "O‘tgan yili joriy etilgan choralar tirbandlikni allaqachon 10% ga kamaytirdi."),
        ],
        "synonyms": [
            ("defining relative clause", "reduced = who/which + be tushirilgan, ixchamroq"),
            ("participle clause", "participle clause butun gapga bog‘lanadi; reduced relative "
                                  "faqat otni aniqlaydi"),
        ],
        "order": 303,
    },
    {
        "pattern":   "that-clause",
        "category":  "en_clause",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "to‘ldiruvchi ergash gap — «... ligini/ekanligini»",
        "attach":    "verb/adjective + that + clause",
        "form_rule": "<b>that</b> + to‘liq gap. Ba’zi fe’llardan keyin tushib qolishi mumkin "
                     "(<i>I think (that) …</i>), lekin akademik yozuvda <b>saqlang</b>. "
                     "Sifatlardan keyin ham keladi: <i>it is clear <b>that</b>…</i>",
        "note":      "<p>Fikr bildirishning asosiy quroli. Xilma-xillik uchun boshqa fe’llarga "
                     "o‘ting: <i>argue / maintain / suggest / demonstrate / indicate <b>that</b></i>. "
                     "<i>I think that</i> ni butun insho bo‘yi takrorlamang.</p>",
        "mistake":   "<p>❌ <i>I agree with that education is important.</i> → "
                     "✅ <i>I agree <b>that</b> education is important.</i> — <i>agree that</i>, "
                     "<i>agree with + ot</i>.</p>",
        "examples": [
            ("Research suggests that early intervention produces the best results.",
             "Tadqiqotlar shuni ko‘rsatadiki, erta aralashuv eng yaxshi natija beradi."),
        ],
        "synonyms": [
            ("the fact that", "the fact that = shu gapni OT sifatida ishlatadi (ega bo‘la oladi)"),
            ("wh-clause", "wh-clause = qanday/nima/nega degan savolni ichiga oladi"),
        ],
        "order": 304,
    },
    {
        "pattern":   "the fact that",
        "category":  "en_clause",
        "function":  "case",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«... ligi» — butun gapni ot qilib ishlatish",
        "attach":    "The fact that + clause + verb",
        "form_rule": "<b>The fact that</b> + to‘liq gap — natijada butun birikma <u>ot</u> bo‘lib, "
                     "ega yoki to‘ldiruvchi bo‘la oladi: <i><b>The fact that</b> wages have "
                     "stagnated <u>explains</u> the fall in demand.</i>",
        "note":      "<p>Predloglardan keyin gap kelolmaydi — shu yerda <i>the fact that</i> "
                     "qutqaradi: ❌ <i>despite <u>he is young</u></i> → "
                     "✅ <i>despite <b>the fact that</b> he is young</i>.</p>",
        "mistake":   "<p>❌ Har jumlada takrorlash matnni og‘irlashtiradi. Bitta inshoda 1-2 marta.</p>",
        "examples": [
            ("The fact that fees have risen has deterred many applicants.",
             "To‘lovlarning oshgani ko‘p arizachilarni chekintirdi."),
            ("Despite the fact that the law was passed, enforcement remains weak.",
             "Qonun qabul qilinganiga qaramay, uning ijrosi hamon zaif."),
        ],
        "synonyms": [
            ("that-clause", "the fact that = gapni OT qiladi; that-clause = fe’lga bog‘lanadi"),
            ("despite / in spite of", "despite + the fact that = predlogdan keyin gap qo‘yishning yo‘li"),
        ],
        "order": 305,
    },
    {
        "pattern":   "wh-clause",
        "category":  "en_clause",
        "function":  "case",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "so‘roq so‘zli ergash gap — «nima/qanday/nega ... ligi»",
        "attach":    "verb + what/how/why/whether + S + V",
        "form_rule": "⚠️ Ichkarida <b>so‘roq tartibi ISHLATILMAYDI</b>: "
                     "❌ I don’t know <u>where is it</u> → ✅ I don’t know <b>where it is</b>. "
                     "<i>do/does/did</i> ham tushadi: ❌ how <u>does it work</u> → "
                     "✅ how <b>it works</b>.",
        "note":      "<p>Task 1 kirishini qayta yozishning eng qulay usuli: "
                     "<i>The chart shows <b>how much</b> electricity each country produced.</i> — "
                     "savol matnini ko‘chirmasdan boshqacha aytasiz.</p>",
        "mistake":   "<p>❌ The graph shows <u>what is the number of</u> students → "
                     "✅ shows <b>what the number of students is</b>, yoki soddaroq: "
                     "✅ shows <b>the number of</b> students.</p>",
        "examples": [
            ("The table illustrates how many hours people spent online each week.",
             "Jadval odamlar har hafta internetda necha soat o‘tkazganini ko‘rsatadi."),
            ("It is unclear whether stricter laws would reduce crime.",
             "Qattiqroq qonunlar jinoyatchilikni kamaytirar-kamaytirmasligi noaniq."),
        ],
        "synonyms": [
            ("that-clause", "that = tasdiqni uzatadi; wh-clause = savolni uzatadi"),
        ],
        "order": 306,
    },
    {
        "pattern":   "although / though / even though",
        "category":  "en_clause",
        "function":  "concession",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "qarshi qo‘yish — «garchi ... bo‘lsa-da»",
        "attach":    "Although + S + V, S + V",
        "form_rule": "<b>although/though/even though</b> + <u>to‘liq gap</u> (ega + kesim). "
                     "Gap boshida kelsa, ikkinchi qismdan oldin <b>vergul</b>. "
                     "<b>even though</b> kuchliroq, <b>though</b> og‘zakiroq.",
        "note":      "<p>Task 2 da qarshi fikrni tan olib, keyin o‘z fikringizga qaytish uchun "
                     "asosiy qolip: <i><b>Although</b> online learning is convenient, it cannot "
                     "replace face-to-face interaction.</i></p>",
        "mistake":   "<p>❌ <i>Although the cost is high, <u>but</u> it is worth it.</i> → "
                     "ingliz tilida <b>although</b> va <b>but</b> birga kelmaydi. Bittasini tanlang.</p>"
                     "<p>❌ <i>Although <u>the high cost</u></i> → ✅ <i>Although <b>the cost is high</b></i>.</p>",
        "examples": [
            ("Although the population has grown, water consumption has fallen.",
             "Aholi ko‘paygan bo‘lsa-da, suv iste’moli kamaydi."),
        ],
        "synonyms": [
            ("despite / in spite of", "although + GAP; despite + ot yoki -ing"),
            ("whereas / while", "whereas = ikki narsani solishtiradi; although = kutilmagan qarshilik"),
            ("however", "however = yangi jumla boshlaydi; although = bitta gap ichida bog‘laydi"),
        ],
        "order": 307,
    },
    {
        "pattern":   "whereas / while",
        "category":  "en_clause",
        "function":  "contrast",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "solishtirma qarama-qarshilik — «... bo‘lsa, ... esa»",
        "attach":    "S + V, whereas + S + V",
        "form_rule": "<b>whereas</b> / <b>while</b> + to‘liq gap. Odatda oldidan vergul qo‘yiladi. "
                     "<b>while</b> ning ikkinchi ma’nosi ham bor («davomida»), shuning uchun "
                     "aniq solishtirma uchun <b>whereas</b> xavfsizroq.",
        "note":      "<p><b>Task 1 ning eng kerakli bog‘lovchisi</b> — ikki ustunni bitta gapda "
                     "solishtiradi: <i>Spending on housing rose steadily, <b>whereas</b> spending "
                     "on food remained flat.</i></p>"
                     "<p>Har bir Task 1 tanasida kamida ikkita shunday gap bo‘lsin.</p>",
        "mistake":   "<p>❌ <i>Whereas, the figure for Japan was higher.</i> — <i>whereas</i> "
                     "yangi jumla boshlamaydi; u ikki qismni ichkaridan bog‘laydi.</p>",
        "examples": [
            ("In 2000, 40% of homes had internet access, whereas by 2015 the figure had reached 90%.",
             "2000-yilda uylarning 40% da internet bor edi, 2015-yilga kelib esa bu ko‘rsatkich 90% ga yetdi."),
        ],
        "synonyms": [
            ("although / though / even though", "whereas = sof solishtirish; although = "
                                                "kutilmaganlik ohangi bor"),
            ("in contrast / on the other hand", "bular jumla boshida; whereas gap ichida"),
        ],
        "order": 308,
    },
    {
        "pattern":   "because / since / as",
        "category":  "en_clause",
        "function":  "reason",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "sabab — «chunki, ... sababli»",
        "attach":    "because/since/as + S + V",
        "form_rule": "Uchalasi ham <u>to‘liq gap</u> oladi. <b>because</b> — eng kuchli va aniq; "
                     "<b>since</b>/<b>as</b> — ma’lum sababni eslatadi va rasmiyroq, odatda gap "
                     "boshida: <i><b>Since</b> resources are limited, …</i>",
        "note":      "<p>❗ Otdan oldin ular ishlamaydi — <b>because of</b> / <b>due to</b> kerak: "
                     "<i>because <u>the rain</u></i> ❌ → <i><b>because of</b> the rain</i> ✅.</p>",
        "mistake":   "<p>❌ <i>Because of the government failed to act…</i> → "
                     "✅ <i><b>Because</b> the government failed to act…</i> "
                     "(gap keldi — <i>of</i> keraksiz).</p>",
        "examples": [
            ("Air quality has deteriorated because more people commute by car.",
             "Havo sifati yomonlashdi, chunki ko‘proq odam ishga mashinada qatnaydi."),
        ],
        "synonyms": [
            ("due to / owing to / because of", "bular OT oladi; because/since/as GAP oladi"),
            ("therefore / consequently", "sabab emas — NATIJANI bog‘laydi (teskari yo‘nalish)"),
        ],
        "order": 309,
    },
    {
        "pattern":   "so that / in order that",
        "category":  "en_clause",
        "function":  "purpose",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "maqsad — «... bo‘lishi uchun»",
        "attach":    "S + V + so that + S + can/will + V",
        "form_rule": "<b>so that</b> + to‘liq gap, odatda ichida <b>can / could / will / would</b>: "
                     "<i>…<b>so that</b> people <b>can</b> access services.</i> "
                     "❌ so that <u>to access</u>.",
        "note":      "<p>Maqsadni ikki xil ayting va takrorlanishdan qoching: "
                     "<b>to</b> + fe’l (ixcham) · <b>in order to</b> (rasmiy) · "
                     "<b>so that</b> + gap (ega o‘zgarganda majburiy).</p>"
                     "<p>Ega o‘zgarsa faqat <b>so that</b> ishlaydi: <i>The city built cycle "
                     "lanes <b>so that residents could</b> commute safely.</i></p>",
        "mistake":   "<p>❌ <i>Governments should subsidise buses <u>for reduce</u> congestion.</i> → "
                     "✅ <b>to reduce</b> / <b>in order to reduce</b> congestion.</p>",
        "examples": [
            ("Schools provide free meals so that no child studies on an empty stomach.",
             "Maktablar bepul ovqat beradi, toki hech bir bola och qorinda o‘qimasin."),
        ],
        "synonyms": [
            ("in order to / so as to", "in order to + FE’L; so that + GAP (ega boshqa bo‘lsa)"),
        ],
        "order": 310,
    },
    {
        "pattern":   "as soon as / by the time / once",
        "category":  "en_clause",
        "function":  "time",
        "level":     4,
        "freq":      1,
        "register":  "both",
        "meaning":   "vaqt ergash gaplari — «... bilanoq, ... ga qadar, bir marta ... bo‘lsa»",
        "attach":    "As soon as + S + V(present), S + will + V",
        "form_rule": "⚠️ <b>Vaqt ergash gapida kelasi zamon ishlatilmaydi</b>: "
                     "❌ as soon as he <u>will arrive</u> → ✅ as soon as he <b>arrives</b>. "
                     "<b>by the time</b> ko‘pincha perfect bilan: <i>by the time they acted, "
                     "the damage <b>had been done</b></i>.",
        "note":      "<p>Speaking Part 3 da kelajak haqida gapirganda bu qoida tez-tez buziladi — "
                     "shuning uchun uni yodda saqlang: <i>when / as soon as / once / until / "
                     "before / after</i> dan keyin present, asosiy gapda <i>will</i>.</p>",
        "examples": [
            ("Once renewable energy becomes cheaper, adoption will accelerate.",
             "Qayta tiklanuvchi energiya arzonlashishi bilan uning joriy etilishi tezlashadi."),
        ],
        "synonyms": [
            ("the tense of the chart (Task 1)", "ikkalasi ham zamon tanlash qoidasi — "
                                                "biri grafikda, biri ergash gapda"),
        ],
        "order": 311,
    },
]
