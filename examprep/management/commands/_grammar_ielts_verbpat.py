# -*- coding: utf-8 -*-
"""IELTS grammar bank — Gerunds, infinitives & verb patterns (fe'l qoliplari).

Order decade 900-999. Uzbek uses one verbal noun where English chooses between
`-ing` and `to`, so this group is pure memorisation with a few meaning-changing
pairs (stop doing / stop to do) that Listening likes to test.
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
        "pattern":   "verb + -ing (gerund)",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "-ing oladigan fe’llar — «... ishni qilishni»",
        "attach":    "verb + V-ing",
        "form_rule": "Shu fe’llardan keyin doim <b>-ing</b>: <b>avoid, suggest, involve, "
                     "consider, risk, deny, admit, recommend, practise, mind, enjoy, "
                     "keep, finish, delay</b>.",
        "note":      "<p>Task 2 uchun eng kerakli uchtasi: <b>involve</b> "
                     "(<i>The solution <b>involves reducing</b> subsidies</i>), "
                     "<b>suggest</b> (<i>Research <b>suggests investing</b> earlier</i>), "
                     "<b>avoid</b> (<i>to <b>avoid causing</b> further damage</i>).</p>",
        "mistake":   "<p>❌ <i>I suggest <u>to build</u> more schools</i> → "
                     "✅ <i>I suggest <b>building</b> more schools</i> yoki "
                     "✅ <i>I suggest <b>that</b> the government <b>build</b> more schools</i>.</p>",
        "examples": [
            ("Governments should avoid relying on a single source of energy.",
             "Hukumatlar bitta energiya manbaiga tayanishdan qochishi kerak."),
        ],
        "synonyms": [
            ("verb + to-infinitive", "ikki ro‘yxat — qaysi fe’l qaysi shaklni olishini yodlang"),
            ("preposition + -ing", "predlogdan keyin ham doim -ing"),
        ],
        "order": 900,
    },
    {
        "pattern":   "verb + to-infinitive",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "to + fe’l oladigan fe’llar — «... qilishga»",
        "attach":    "verb + to + V",
        "form_rule": "Shu fe’llardan keyin doim <b>to</b> + fe’l: <b>aim, tend, fail, "
                     "manage, decide, hope, expect, refuse, agree, offer, seem, appear, "
                     "afford, learn</b>.",
        "note":      "<p>Akademik yozuvda eng foydalilari: <b>tend to</b> (hedging), "
                     "<b>fail to</b> (<i>Policies that <b>fail to</b> address the root cause…</i>), "
                     "<b>aim to</b> (<i>This essay <b>aims to</b> examine…</i>).</p>",
        "mistake":   "<p>❌ <i>They decided <u>building</u> a new line</i> → ✅ <i>decided "
                     "<b>to build</b></i> · ❌ <i>manage <u>doing</u></i> → ✅ <i>manage <b>to do</b></i>.</p>",
        "examples": [
            ("Many countries have failed to meet their emissions targets.",
             "Ko‘p mamlakatlar chiqindilar bo‘yicha maqsadlarini bajara olmadi."),
        ],
        "synonyms": [
            ("verb + -ing (gerund)", "boshqa ro‘yxat — bir xil ma’noda ikkalasini ishlatib bo‘lmaydi"),
            ("verb + object + to-infinitive", "oradagi to‘ldiruvchi bilan qolip o‘zgaradi"),
        ],
        "order": 901,
    },
    {
        "pattern":   "verb + object + to-infinitive",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "birovga nimadir qildirish — «... ni ... qilishga undamoq»",
        "attach":    "verb + somebody + to + V",
        "form_rule": "<b>encourage / allow / enable / persuade / force / require / advise / "
                     "expect / want</b> + <u>to‘ldiruvchi</u> + <b>to</b> + fe’l: "
                     "<i>encourage people <b>to recycle</b></i>. "
                     "⚠️ <b>make</b> va <b>let</b> bu qolipga kirmaydi — ular <i>to</i> siz.",
        "note":      "<p>Task 2 yechim jumlalarining asosiy qolipi: "
                     "<i>Tax incentives would <b>encourage companies to invest</b> in cleaner "
                     "technology and <b>enable households to reduce</b> their bills.</i></p>",
        "mistake":   "<p>❌ <i>allow <u>to students</u> to choose</i> → ✅ <i>allow <b>students</b> "
                     "to choose</i> · ❌ <i>suggest <u>me to</u> study</i> → ✅ <i>advise <b>me to</b> "
                     "study</i> (<i>suggest</i> bu qolipni olmaydi).</p>",
        "examples": [
            ("Free public transport would encourage commuters to leave their cars at home.",
             "Bepul jamoat transporti qatnovchilarni mashinasini uyda qoldirishga undardi."),
        ],
        "synonyms": [
            ("verb + to-infinitive", "bu variantda o‘rtada to‘ldiruvchi bor"),
            ("make / let / have (causative)", "make/let = to SIZ; encourage/allow = to BILAN"),
        ],
        "order": 902,
    },
    {
        "pattern":   "stop / remember / regret + -ing or to",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "ma’no o‘zgaradigan juftlar — shakl ma’noni o‘zgartiradi",
        "attach":    "verb + V-ing / verb + to + V",
        "form_rule": "<b>stop <u>doing</u></b> = ishni tugatdi · <b>stop <u>to do</u></b> = "
                     "boshqa ish uchun to‘xtadi<br>"
                     "<b>remember <u>doing</u></b> = qilganini eslaydi · "
                     "<b>remember <u>to do</u></b> = qilishni unutmadi<br>"
                     "<b>regret <u>doing</u></b> = qilganidan afsus · "
                     "<b>regret <u>to say</u></b> = afsus bilan xabar bermoq",
        "note":      "<p>Listening Section 3-4 da bu farq to‘g‘ridan-to‘g‘ri javobni hal qiladi: "
                     "<i>He stopped <b>smoking</b></i> (tashladi) va <i>He stopped <b>to smoke</b></i> "
                     "(chekish uchun to‘xtadi) — butunlay boshqa ma’no.</p>",
        "mistake":   "<p>❌ <i>I stopped <u>to use</u> plastic bags</i> (agar «tashladim» demoqchi "
                     "bo‘lsangiz) → ✅ <i>I stopped <b>using</b> plastic bags</i>.</p>",
        "examples": [
            ("The company stopped using single-use plastics in 2020.",
             "Kompaniya 2020-yilda bir martalik plastikdan foydalanishni to‘xtatdi."),
        ],
        "synonyms": [
            ("verb + -ing (gerund)", "bu fe’llar ikkala shaklni ham oladi — lekin ma’no o‘zgaradi"),
        ],
        "order": 903,
    },
    {
        "pattern":   "-ing as subject",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "-ing shakli ega o‘rnida — «... qilish (foydali)»",
        "attach":    "V-ing + verb (singular)",
        "form_rule": "<b>-ing</b> birikmasi ega bo‘lganda fe’l <u>birlikda</u>: "
                     "<i><b>Investing</b> in education <b>is</b> the most effective strategy.</i> "
                     "Muqobil: <b>To invest</b> in education is… (rasmiyroq, kamroq tabiiy).",
        "note":      "<p>Gapni fe’ldan boshlash — insho jumlalarini xilma-xil qilishning oson "
                     "yo‘li. Ketma-ket uchta gap <i>The government…</i> bilan boshlansa, "
                     "bittasini shunga aylantiring.</p>",
        "mistake":   "<p>❌ <i><u>Reduce</u> emissions is essential</i> → ✅ <i><b>Reducing</b> "
                     "emissions is essential</i>.</p>"
                     "<p>❌ <i>Building new roads <u>are</u> expensive</i> → ✅ <i><b>is</b> "
                     "expensive</i> — ega birlik.</p>",
        "examples": [
            ("Encouraging cycling has proved cheaper than expanding the road network.",
             "Velosipedni rag‘batlantirish yo‘l tarmog‘ini kengaytirishdan arzonroq bo‘lib chiqdi."),
        ],
        "synonyms": [
            ("it is + adjective + that/to", "It is essential to invest = shu fikrning "
                                            "boshqa, shaxssiz shakli"),
            ("nominalisation", "-ing = fe’lni ega qiladi; nominalisation = uni otga aylantiradi"),
        ],
        "order": 904,
    },
    {
        "pattern":   "there is no point in -ing",
        "category":  "en_verbpat",
        "function":  "case",
        "level":     5,
        "freq":      1,
        "register":  "both",
        "meaning":   "foydasizlik — «... qilishning ma’nosi yo‘q»",
        "attach":    "There is no point in + V-ing",
        "form_rule": "<b>There is no point in</b> + <b>-ing</b>. Shu oiladagi boshqalar: "
                     "<b>It is worth</b> + -ing · <b>It is no use</b> + -ing · "
                     "<b>have difficulty (in)</b> + -ing · <b>spend time</b> + -ing.",
        "note":      "<p>Qarshi dalilni rad etishning ixcham yo‘li: <i><b>There is little point "
                     "in</b> building more roads if public transport remains unreliable.</i> "
                     "<i>no</i> o‘rniga <b>little</b> qo‘ysangiz — yumshoqroq va akademikroq.</p>",
        "mistake":   "<p>❌ <i>It is worth <u>to invest</u></i> → ✅ <i>It is worth <b>investing</b></i>.</p>",
        "examples": [
            ("It is worth noting that the trend reversed after 2012.",
             "Shuni ta’kidlash joizki, tendensiya 2012-yildan keyin teskari o‘zgardi."),
        ],
        "synonyms": [
            ("preposition + -ing", "in + -ing — shu qolipdagi predlog ham -ing talab qiladi"),
        ],
        "order": 905,
    },
    {
        "pattern":   "in order to / so as to",
        "category":  "en_verbpat",
        "function":  "purpose",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "maqsad — «... qilish uchun»",
        "attach":    "in order to + V · so as to + V",
        "form_rule": "<b>to</b> + fe’l (eng oddiy) · <b>in order to</b> + fe’l (rasmiy) · "
                     "<b>so as to</b> + fe’l (rasmiy). Inkor shakli faqat uzun variantlarda: "
                     "<b>in order not to</b> / <b>so as not to</b> (❌ <i>not to</i> yolg‘iz).",
        "note":      "<p>Ega bir xil bo‘lsa — <b>in order to</b>; ega o‘zgarsa — <b>so that</b> + gap. "
                     "Bu ikkisini to‘g‘ri tanlash Band 7 belgisi:</p>"
                     "<p><i>The city introduced a toll <b>in order to</b> reduce traffic.</i> (bir ega)<br>"
                     "<i>The city introduced a toll <b>so that residents could</b> breathe cleaner "
                     "air.</i> (ega o‘zgardi)</p>",
        "mistake":   "<p>❌ <i>for reduce congestion</i> / ❌ <i>for reducing congestion</i> "
                     "(maqsad ma’nosida) → ✅ <i><b>to reduce</b> congestion</i>.</p>",
        "examples": [
            ("Many governments subsidise renewables in order to cut their dependence on imports.",
             "Ko‘p hukumatlar importga qaramlikni kamaytirish uchun qayta tiklanuvchi energiyani subsidiyalaydi."),
        ],
        "synonyms": [
            ("so that / in order that", "in order to + FE’L; so that + GAP (ega boshqa bo‘lsa)"),
        ],
        "order": 906,
    },
    {
        "pattern":   "it takes + time + to",
        "category":  "en_verbpat",
        "function":  "degree",
        "level":     4,
        "freq":      1,
        "register":  "both",
        "meaning":   "vaqt yoki resurs talab qilish — «... uchun ... kerak bo‘ladi»",
        "attach":    "It takes + (somebody) + time + to + V",
        "form_rule": "<b>It takes</b> (+ odam) + vaqt/resurs + <b>to</b> + fe’l: "
                     "<i>It takes years <b>to build</b> a reliable network.</i> "
                     "O‘tmish: <b>It took</b> …",
        "note":      "<p>Yechimning «tez emas» ekanini aytish uchun qulay — muvozanatli xulosa "
                     "yozishda foydali: <i><b>It takes</b> considerable time and investment "
                     "<b>to change</b> established habits.</i></p>",
        "examples": [
            ("It takes decades to restore a forest that was cleared in a single season.",
             "Bir mavsumda kesilgan o‘rmonni tiklash uchun o‘nlab yil kerak bo‘ladi."),
        ],
        "synonyms": [
            ("it is + adjective + that/to", "bir oila: <i>it</i> bilan boshlanadigan shaxssiz qoliplar"),
        ],
        "order": 907,
    },
]
