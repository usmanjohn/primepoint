# -*- coding: utf-8 -*-
"""IELTS grammar bank — Comparison & degree (qiyoslash).

Order decade 800-899. Task 1's second half is comparison: nobody scores well
by listing figures, only by saying which is bigger, by how much, and how that
compares with the rest. Task 2's "advantages outweigh disadvantages" essays
run on the same structures.
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
        "pattern":   "comparative",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "qiyosiy daraja — «... roq, ... dan ko‘ra»",
        "attach":    "adj-er / more + adj + than",
        "form_rule": "Bir bo‘g‘inli sifat → <b>-er</b> (high<b>er</b>, larg<b>er</b>, "
                     "big<b>ger</b>) · ikki va undan ko‘p bo‘g‘in → <b>more</b> "
                     "(<b>more</b> expensive). <i>-y</i> bilan tugasa: happ<b>ier</b>. "
                     "Noto‘g‘ri shakllar: good → <b>better</b>, bad → <b>worse</b>, "
                     "far → <b>further</b>.",
        "note":      "<p>Task 1 da raqamlarni sanab chiqish emas, <b>solishtirish</b> ball beradi: "
                     "<i>Spending on housing was <b>considerably higher than</b> spending on "
                     "transport throughout the period.</i></p>",
        "mistake":   "<p>❌ <i><u>more higher</u></i> → ✅ <i>higher</i> (ikki marta qiyoslamang) · "
                     "❌ <i>higher <u>then</u></i> → ✅ <i>higher <b>than</b></i> "
                     "(<i>then</i> = keyin, <i>than</i> = dan).</p>",
        "examples": [
            ("Rural households consumed far less electricity than urban ones.",
             "Qishloq xonadonlari shahar xonadonlariga qaraganda ancha kam elektr iste’mol qildi."),
        ],
        "synonyms": [
            ("superlative", "comparative = ikkitasini solishtiradi; superlative = hammasidan eng"),
            ("as … as", "as…as = tenglik; comparative = farq"),
            ("significantly / slightly + comparative", "bu ravishlar farqning HAJMINI aytadi"),
        ],
        "order": 800,
    },
    {
        "pattern":   "superlative",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "orttirma daraja — «eng ...»",
        "attach":    "the + adj-est / the most + adj",
        "form_rule": "<b>the</b> majburiy: <i><b>the</b> highest</i>, <i><b>the most</b> "
                     "significant</i>. Keyin ko‘pincha <b>of</b> yoki <b>in</b>: "
                     "<i>the highest <b>of</b> the four countries</i>, "
                     "<i>the largest city <b>in</b> the region</i>.",
        "note":      "<p>Task 1 ning umumiy xulosasi (overview) deyarli doim superlativ bilan "
                     "yoziladi: <i>Overall, China recorded <b>the highest</b> level of "
                     "consumption, while Brazil saw <b>the sharpest</b> decline.</i></p>"
                     "<p>«Ikkinchi o‘rin» uchun: <b>the second-highest</b>, "
                     "<b>the next largest</b>.</p>",
        "mistake":   "<p>❌ <i>Japan had <u>highest</u> figure</i> → ✅ <i><b>the highest</b> "
                     "figure</i> — superlativda <i>the</i> tushib qolmaydi.</p>",
        "examples": [
            ("The most striking feature of the graph is the sharp rise after 2010.",
             "Grafikning eng ko‘zga tashlanadigan jihati — 2010-yildan keyingi keskin o‘sish."),
        ],
        "synonyms": [
            ("comparative", "superlative = eng; comparative = ikkisidan biri"),
            ("most / most of / the most", "the most = «eng»; most = «aksariyat» — chalkashtirmang"),
        ],
        "order": 801,
    },
    {
        "pattern":   "as … as",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     3,
        "freq":      2,
        "register":  "both",
        "meaning":   "tenglik — «... kabi, ... darajada»",
        "attach":    "as + adj/adv + as",
        "form_rule": "<b>as</b> + sifat/ravish (asl shakl) + <b>as</b>. Inkor: "
                     "<b>not as … as</b> yoki <b>not so … as</b>. Miqdor bilan: "
                     "<b>as many … as</b> (sanaladigan), <b>as much … as</b> (sanalmas).",
        "note":      "<p>Karra bilan birga Task 1 ning eng kuchli qolipini beradi: "
                     "<i>Germany consumed <b>twice as much</b> energy <b>as</b> Italy.</i></p>"
                     "<p>Yaqin, lekin teng bo‘lmagan raqamlar uchun: <b>almost as … as</b>, "
                     "<b>just as … as</b>, <b>nearly as … as</b>.</p>",
        "mistake":   "<p>❌ <i>as <u>higher</u> as</i> → ✅ <i>as <b>high</b> as</i> — orasida "
                     "qiyosiy shakl ishlatilmaydi.</p>",
        "examples": [
            ("Solar power was almost as widespread as wind power by the end of the period.",
             "Davr oxiriga kelib quyosh energiyasi shamol energiyasi kabi keng tarqalgan edi."),
        ],
        "synonyms": [
            ("comparative", "as…as = teng; comparative = farqli"),
            ("twice / three times as many as", "karrali tenglik — as…as ning miqdorli shakli"),
        ],
        "order": 802,
    },
    {
        "pattern":   "twice / three times as many as",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "karrali qiyos — «ikki baravar ko‘p, uch baravar»",
        "attach":    "twice/three times + as many/much + as",
        "form_rule": "<b>twice</b> (2×) · <b>three times</b> (3×) · <b>half</b> (½) + "
                     "<b>as many/much … as</b>. Muqobil shakl: <b>double</b> / <b>triple</b> "
                     "(fe’l), <b>a threefold increase</b> (ot birikmasi).",
        "note":      "<p>Bir xil raqamni turlicha aytishning uch yo‘li — Task 1 da uchalasini "
                     "aralashtiring:</p>"
                     "<p><i>France produced <b>twice as much as</b> Spain.</i><br>"
                     "<i>Output in France was <b>double that of</b> Spain.</i><br>"
                     "<i>France recorded <b>a twofold</b> advantage over Spain.</i></p>",
        "mistake":   "<p>❌ <i>twice <u>more than</u></i> → ✅ <i>twice <b>as much as</b></i> "
                     "yoki ✅ <i><b>twice</b> the amount</i>.</p>",
        "examples": [
            ("By 2015, three times as many households had broadband as in 2005.",
             "2015-yilga kelib keng polosali internetga ega xonadonlar 2005-yildagidan uch baravar ko‘p edi."),
        ],
        "synonyms": [
            ("as … as", "bu — as…as ning karrali varianti"),
            ("comparative", "comparative = qancha farq; karrali qiyos = necha baravar"),
        ],
        "order": 803,
    },
    {
        "pattern":   "significantly / slightly + comparative",
        "category":  "en_compare",
        "function":  "degree",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "farqning hajmi — «ancha ko‘proq, biroz kamroq»",
        "attach":    "much/far/slightly + comparative + than",
        "form_rule": "Katta farq: <b>far</b> · <b>much</b> · <b>considerably</b> · "
                     "<b>significantly</b> · <b>substantially</b> + qiyosiy shakl. "
                     "Kichik farq: <b>slightly</b> · <b>marginally</b> · <b>a little</b>. "
                     "⚠️ <i>very</i> qiyosiy shakl bilan <u>ishlatilmaydi</u>: ❌ very higher.",
        "note":      "<p>Bu ravishlarsiz Task 1 quruq bo‘ladi. Ular tekshiruvchiga siz "
                     "raqamlarni <b>talqin qila olishingizni</b> ko‘rsatadi: "
                     "<i>The figure for Japan was <b>marginally higher</b> than that for Korea, "
                     "whereas China’s was <b>far greater</b> than both.</i></p>",
        "mistake":   "<p>❌ <i>very more expensive</i> → ✅ <i><b>much</b> more expensive</i>.</p>",
        "examples": [
            ("Wages rose slightly faster in the private sector than in the public sector.",
             "Ish haqi xususiy sektorda davlat sektoridagiga qaraganda biroz tezroq o‘sdi."),
        ],
        "synonyms": [
            ("comparative", "bu ravishlar qiyosiy shaklga «qancha» ma’nosini qo‘shadi"),
            ("adverbs of degree (Task 1)", "bir oila: biri qiyos bilan, biri fe’l bilan"),
        ],
        "order": 804,
    },
    {
        "pattern":   "adverbs of degree (Task 1)",
        "category":  "en_compare",
        "function":  "degree",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "o‘zgarish tezligi va hajmi — «keskin, barqaror, sekin»",
        "attach":    "verb + adverb · adjective + noun",
        "form_rule": "Ikki xil aytiladi, ma’no bir xil: "
                     "<b>fe’l + ravish</b> — <i>rose <b>sharply</b></i> · "
                     "<b>sifat + ot</b> — <i>a <b>sharp</b> rise</i>. "
                     "Juftlar: sharp/sharply · dramatic/dramatically · steady/steadily · "
                     "gradual/gradually · slight/slightly · rapid/rapidly.",
        "note":      "<p>Task 1 da bir xil so‘zni takrorlamaslikning eng oson yo‘li — ikki "
                     "qolipni almashtirib turish: <i>Sales <b>increased sharply</b> in 2005, "
                     "followed by <b>a gradual decline</b> over the next five years.</i></p>",
        "mistake":   "<p>❌ <i>increased <u>sharp</u></i> → ✅ <i>increased <b>sharply</b></i> "
                     "(fe’lga ravish kerak) · ❌ <i>a <u>sharply</u> increase</i> → "
                     "✅ <i>a <b>sharp</b> increase</i> (otga sifat).</p>",
        "examples": [
            ("The number of visitors fell dramatically after 2008 before recovering gradually.",
             "Tashrif buyuruvchilar soni 2008-yildan keyin keskin tushdi, so‘ng asta-sekin tiklandi."),
        ],
        "synonyms": [
            ("significantly / slightly + comparative", "biri fe’lni, biri qiyosni o‘lchaydi"),
        ],
        "order": 805,
    },
    {
        "pattern":   "compared with / in comparison with",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "qiyoslash iborasi — «... bilan solishtirganda»",
        "attach":    "Compared with X, Y + V",
        "form_rule": "<b>compared with / to</b> + ot · <b>in comparison with</b> + ot · "
                     "<b>by comparison</b> (yolg‘iz, jumla boshida). "
                     "Gap boshida kelsa vergul qo‘yiladi.",
        "note":      "<p>Task 1 da uchinchi xatboshini boshlashning tabiiy yo‘li: "
                     "<i><b>Compared with</b> European countries, Asian economies showed a far "
                     "steeper rise.</i></p>",
        "mistake":   "<p>❌ <i>Compared with <u>Japan is higher</u></i> → ✅ <i>Compared with "
                     "<b>Japan</b>, the figure is higher</i> — <i>compared with</i> ot oladi.</p>",
        "examples": [
            ("In comparison with 1990, energy use per household has fallen by a fifth.",
             "1990-yil bilan solishtirganda, har bir xonadonning energiya sarfi beshdan birga kamaydi."),
        ],
        "synonyms": [
            ("whereas / while", "whereas = gap ichida bog‘laydi; compared with = ot bilan"),
            ("in contrast / on the other hand", "in contrast = qarama-qarshilikni ta’kidlaydi"),
        ],
        "order": 806,
    },
    {
        "pattern":   "the more … the more",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     6,
        "freq":      1,
        "register":  "both",
        "meaning":   "parallel o‘zgarish — «qancha ... shuncha ...»",
        "attach":    "The + comparative …, the + comparative …",
        "form_rule": "Ikkala qismda ham <b>the</b> + qiyosiy shakl: "
                     "<i><b>The more</b> people commute by car, <b>the worse</b> congestion "
                     "becomes.</i> Ikkinchi qismdan oldin <b>vergul</b>.",
        "note":      "<p>Sabab-natijani ixcham va ta’sirchan qilib beradi — Task 2 tanasida "
                     "bitta shunday gap Grammatical Range uchun yaxshi dalil.</p>",
        "mistake":   "<p>❌ <i>More people work from home, less traffic there is</i> — "
                     "<b>the</b> tushib qolgan: ✅ <i><b>The more</b> people work from home, "
                     "<b>the less</b> traffic there is.</i></p>",
        "examples": [
            ("The higher the level of education, the lower the unemployment rate tends to be.",
             "Ta’lim darajasi qanchalik yuqori bo‘lsa, ishsizlik darajasi shunchalik past bo‘ladi."),
        ],
        "synonyms": [
            ("comparative", "bu — qiyosiy shaklning juftlangan, ta’sirchan varianti"),
        ],
        "order": 807,
    },
    {
        "pattern":   "outweigh",
        "category":  "en_compare",
        "function":  "comparison",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "ustun kelmoq — «foydasi zararidan ko‘p»",
        "attach":    "X outweigh(s) Y",
        "form_rule": "<b>outweigh</b> — fe’l, to‘g‘ridan-to‘g‘ri to‘ldiruvchi oladi "
                     "(predlogsiz): <i>The benefits <b>outweigh</b> the drawbacks.</i> "
                     "Kuchaytirish: <b>far outweigh</b>, <b>clearly outweigh</b>.",
        "note":      "<p>«Advantages and disadvantages» tipidagi savolning xulosasi aynan shu "
                     "so‘z bilan yoziladi — savol matnining o‘zi ham shuni so‘raydi. "
                     "Tayyor qolip: <i>In my view, the advantages of X <b>far outweigh</b> its "
                     "disadvantages, provided that …</i></p>",
        "mistake":   "<p>❌ <i>The benefits outweigh <u>than</u> the drawbacks</i> → "
                     "✅ <i>outweigh <b>the drawbacks</b></i>.</p>",
        "examples": [
            ("The long-term environmental benefits far outweigh the initial financial costs.",
             "Uzoq muddatli ekologik foyda dastlabki moliyaviy xarajatlardan ancha ustun."),
        ],
        "synonyms": [
            ("comparative", "outweigh = «ustun kelmoq» ma’nosini bitta fe’lda beradi"),
        ],
        "order": 808,
    },
]
