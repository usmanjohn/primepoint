# -*- coding: utf-8 -*-
"""IELTS grammar bank — Articles, determiners & countability.

Order decade 600-699. Uzbek has no articles, so this group is where the most
marks are quietly lost: an otherwise band-7 essay with `the government should
ban car` reads as inaccurate. Every row here is written from that angle.
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
        "pattern":   "a / an",
        "category":  "en_article",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "register":  "both",
        "meaning":   "noaniq artikl — «bittasi, qandaydir» (birinchi marta tilga olinganda)",
        "attach":    "a/an + sanaladigan ot (birlik)",
        "form_rule": "Undosh <u>tovush</u> oldidan <b>a</b>, unli tovush oldidan <b>an</b> — "
                     "harf emas, <u>talaffuz</u> muhim: <b>a</b> university (yu-), "
                     "<b>an</b> hour (au-), <b>an</b> MBA (em-).",
        "note":      "<p>Sanaladigan otning birligi <b>hech qachon artiklsiz turmaydi</b> — "
                     "yo <i>a/an</i>, yo <i>the</i>, yo <i>this/my/each</i> bo‘lishi shart.</p>"
                     "<p>Kasb va misol keltirishda: <i>as <b>a</b> result</i>, "
                     "<i>She works as <b>an</b> engineer</i>.</p>",
        "mistake":   "<p>❌ <i>He is <u>engineer</u></i> → ✅ <i>He is <b>an</b> engineer</i>.</p>"
                     "<p>❌ <i><u>A</u> pollution is a problem</i> → ✅ <i>Pollution is a problem</i> "
                     "— sanalmaydigan otga <i>a</i> qo‘yilmaydi.</p>",
        "examples": [
            ("The chart shows a steady increase in energy consumption.",
             "Diagramma energiya iste’molining barqaror o‘sishini ko‘rsatadi."),
        ],
        "synonyms": [
            ("the", "a/an = birinchi marta yoki qaysi biri muhim emas; the = ma’lum, aniq narsa"),
            ("zero article", "zero article = umumiy ma’noda ko‘plik yoki sanalmaydigan ot"),
        ],
        "order": 600,
    },
    {
        "pattern":   "the",
        "category":  "en_article",
        "function":  "case",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "aniq artikl — «o‘sha, ma’lum bo‘lgan»",
        "attach":    "the + ot (birlik, ko‘plik yoki sanalmaydigan)",
        "form_rule": "<b>the</b> qo‘yiladi: ikkinchi marta eslatilganda · yagona narsa "
                     "(<i>the sun, the government, the environment</i>) · superlativ bilan "
                     "(<i>the highest</i>) · <i>of</i> birikmasi bilan (<i>the number <b>of</b> "
                     "students</i>) · Task 1 da <i>the figure, the period, the chart</i>.",
        "note":      "<p><b>Task 1 uchun oltin qoida:</b> grafik, davr va ko‘rsatkichlar doim "
                     "aniq — shuning uchun <i><b>the</b> chart</i>, <i><b>the</b> period</i>, "
                     "<i><b>the</b> figure for Japan</i>, <i><b>the</b> highest proportion</i>.</p>"
                     "<p>Foizlar bilan esa artikl yo‘q: <i>20% <b>of</b> households</i> "
                     "(❌ the 20%).</p>",
        "mistake":   "<p>❌ <i><u>The</u> education is important</i> → ✅ <i>Education is "
                     "important</i> — umumiy ma’noda <i>the</i> kerak emas.</p>"
                     "<p>❌ <i>number of students <u>are</u> rising</i> → ✅ <i><b>The</b> number "
                     "of students <b>is</b> rising</i>.</p>",
        "examples": [
            ("The number of vehicles on the road doubled during the period.",
             "Yo‘llardagi transport vositalari soni davr davomida ikki baravar oshdi."),
            ("The government has introduced a new tax on plastic packaging.",
             "Hukumat plastik qadoq uchun yangi soliq joriy qildi."),
        ],
        "synonyms": [
            ("a / an", "the = ma’lum; a/an = noma’lum yoki birinchi marta"),
            ("zero article", "the = aniq guruh; artiklsiz = umuman shu turdagi narsalar"),
        ],
        "order": 601,
    },
    {
        "pattern":   "zero article",
        "category":  "en_article",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "artiklsiz shakl — umumiy, turdosh ma’no",
        "attach":    "∅ + ko‘plik ot / sanalmaydigan ot",
        "form_rule": "Artikl <b>qo‘yilmaydi</b>: umumiy ma’nodagi ko‘plik (<i>Cars pollute…</i>), "
                     "sanalmaydigan otlar (<i>water, information, advice, research</i>), "
                     "mavhum tushunchalar (<i>education, technology, poverty</i>), "
                     "ko‘pchilik mamlakat nomlari (<i>Uzbekistan</i>, lekin <b>the</b> USA, "
                     "<b>the</b> UK, <b>the</b> Netherlands).",
        "note":      "<p><b>Task 2 da umumlashtirishning to‘g‘ri yo‘li shu.</b> Uch xil "
                     "umumlashtirish bor, lekin eng xavfsizi — artiklsiz ko‘plik:</p>"
                     "<p>✅ <i><b>Cars</b> are a major source of pollution.</i> (eng tabiiy)<br>"
                     "✅ <i><b>The car</b> is a major source of pollution.</i> (rasmiy, ilmiy)<br>"
                     "⚠️ <i><b>A car</b> is a major source of pollution.</i> (kamdan-kam)</p>",
        "mistake":   "<p>❌ <i>The technology has changed the society</i> → "
                     "✅ <i>Technology has changed society</i>.</p>"
                     "<p>❌ <i>I have many <u>informations</u></i> → ✅ <i>much <b>information</b></i>.</p>",
        "examples": [
            ("Governments should invest more in renewable energy.",
             "Hukumatlar qayta tiklanuvchi energiyaga ko‘proq sarmoya kiritishi kerak."),
        ],
        "synonyms": [
            ("the", "artiklsiz = umumiy tur; the = aniq, ma’lum narsa"),
            ("uncountable nouns", "sanalmaydigan otlar deyarli doim artiklsiz keladi"),
        ],
        "order": 602,
    },
    {
        "pattern":   "uncountable nouns",
        "category":  "en_article",
        "function":  "degree",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "sanalmaydigan otlar — ko‘plik shakli yo‘q",
        "attach":    "much/a great deal of + uncountable",
        "form_rule": "IELTS’da eng ko‘p adashtiradiganlari: <b>information, advice, research, "
                     "knowledge, equipment, furniture, traffic, pollution, money, work, "
                     "progress, evidence</b> — ularda <u>-s yo‘q</u> va fe’l <u>birlikda</u>.",
        "note":      "<p>Sanash uchun o‘lchov so‘zi qo‘shiladi: <i><b>a piece of</b> advice</i>, "
                     "<i><b>two pieces of</b> equipment</i>, <i><b>a great deal of</b> research</i>.</p>"
                     "<p>Ba’zi otlar ikki xil ishlaydi: <i>experience</i> (tajriba — sanalmas) "
                     "vs <i>an experience</i> (bir voqea — sanaladi).</p>",
        "mistake":   "<p>❌ <i>many <u>researches</u></i> → ✅ <i><b>much research</b></i> / "
                     "<i><b>many studies</b></i><br>"
                     "❌ <i>Traffics <u>are</u> heavy</i> → ✅ <i>Traffic <b>is</b> heavy</i><br>"
                     "❌ <i>a lot of <u>works</u></i> → ✅ <i>a lot of <b>work</b></i> / "
                     "<i>a lot of <b>jobs</b></i>.</p>",
        "examples": [
            ("Recent research suggests that early bilingualism has lasting benefits.",
             "So‘nggi tadqiqotlar erta ikki tillilik uzoq muddatli foyda berishini ko‘rsatadi."),
        ],
        "synonyms": [
            ("much / many / a lot of", "much = sanalmas; many = sanaladigan"),
            ("zero article", "sanalmaydigan otlar umumiy ma’noda artiklsiz keladi"),
        ],
        "order": 603,
    },
    {
        "pattern":   "much / many / a lot of",
        "category":  "en_article",
        "function":  "degree",
        "level":     2,
        "freq":      3,
        "register":  "both",
        "meaning":   "miqdor — «ko‘p»",
        "attach":    "much + uncountable · many + plural",
        "form_rule": "<b>many</b> + sanaladigan ko‘plik · <b>much</b> + sanalmaydigan · "
                     "<b>a lot of / plenty of</b> — ikkalasi bilan ham. "
                     "Akademik yozuvda <i>a lot of</i> o‘rniga: <b>a large number of</b> "
                     "(sanaladigan), <b>a great deal of</b> (sanalmas), <b>numerous</b>, "
                     "<b>considerable</b>.",
        "note":      "<p>Tasdiq gapda yolg‘iz <i>much</i> g‘alati eshitiladi — "
                     "<i>There is <u>much</u> pollution</i> ❌ → <i>There is <b>a great deal of</b> "
                     "pollution</i> ✅. Inkor va so‘roqda esa <i>much</i> normal: "
                     "<i>not much progress</i>.</p>",
        "mistake":   "<p>❌ <i>much people</i> → ✅ <i><b>many</b> people</i> · "
                     "❌ <i>many money</i> → ✅ <i><b>much</b> money</i> / "
                     "<i><b>a great deal of</b> money</i>.</p>",
        "examples": [
            ("A large number of graduates now work in fields unrelated to their degree.",
             "Ko‘p sonli bitiruvchilar hozir mutaxassisligiga aloqasi yo‘q sohalarda ishlaydi."),
        ],
        "synonyms": [
            ("uncountable nouns", "much/many tanlash sanaladigan-sanalmasligiga bog‘liq"),
            ("few / a few / little / a little", "few/little = OZ; many/much = KO‘P"),
        ],
        "order": 604,
    },
    {
        "pattern":   "few / a few / little / a little",
        "category":  "en_article",
        "function":  "degree",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "oz miqdor — «bir oz» yoki «juda kam» (ohangi qarama-qarshi)",
        "attach":    "few + plural · little + uncountable",
        "form_rule": "<b>a few</b> / <b>a little</b> = <u>ijobiy</u> ohang, «bir oz bor». "
                     "<b>few</b> / <b>little</b> (artiklsiz) = <u>salbiy</u> ohang, "
                     "«deyarli yo‘q». Sanash: <b>few</b> + ko‘plik, <b>little</b> + sanalmas.",
        "note":      "<p>Bitta <i>a</i> ma’noni teskari qiladi — bu Reading’da ham savol bo‘ladi:</p>"
                     "<p><i><b>A few</b> countries have met the target.</i> = bir nechtasi "
                     "uddaladi (ijobiy)<br>"
                     "<i><b>Few</b> countries have met the target.</i> = deyarli hech biri "
                     "uddalamadi (salbiy)</p>",
        "mistake":   "<p>❌ <i>a few information</i> → ✅ <i><b>a little</b> information</i>.</p>",
        "examples": [
            ("Few developing countries can afford such large-scale investment.",
             "Kam sonli rivojlanayotgan davlat bunday yirik sarmoyani ko‘tara oladi."),
        ],
        "synonyms": [
            ("much / many / a lot of", "few/little = oz; many/much = ko‘p"),
        ],
        "order": 605,
    },
    {
        "pattern":   "most / most of / the most",
        "category":  "en_article",
        "function":  "degree",
        "level":     4,
        "freq":      3,
        "register":  "both",
        "meaning":   "ko‘pchilik — «aksariyat» (va «eng» bilan chalkashmasin)",
        "attach":    "most + noun · most of + the/my + noun",
        "form_rule": "<b>most</b> + ot (umuman): <i>most students</i> · "
                     "<b>most of</b> + <u>aniqlovchi</u> + ot: <i>most of <b>the</b> students "
                     "in the survey</i> · <b>the most</b> = superlativ: <i>the most effective "
                     "solution</i>.",
        "note":      "<p>Task 1 da eng ko‘p ishlatiladigan uchlik shu: "
                     "<i><b>Most</b> respondents preferred…</i> · <i><b>Most of the</b> increase "
                     "occurred after 2010</i> · <i>Japan recorded <b>the most</b> significant "
                     "growth</i>.</p>",
        "mistake":   "<p>❌ <i><u>The most of</u> people</i> → ✅ <i><b>Most</b> people</i> "
                     "yoki <i><b>Most of the</b> people in the survey</i>.</p>"
                     "<p>❌ <i>Almost people</i> → ✅ <i><b>Most</b> people</i> / "
                     "<i><b>Almost all</b> people</i> — <i>almost</i> yolg‘iz ot oldida kelmaydi.</p>",
        "examples": [
            ("Most of the electricity in the country is generated from natural gas.",
             "Mamlakatdagi elektr energiyasining aksariyati tabiiy gazdan ishlab chiqariladi."),
        ],
        "synonyms": [
            ("the majority of", "the majority of = rasmiyroq va Task 1 uchun tabiiyroq"),
            ("superlative", "the most = «eng» — bu butunlay boshqa vazifa"),
        ],
        "order": 606,
    },
    {
        "pattern":   "the majority of",
        "category":  "en_article",
        "function":  "degree",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "ko‘pchilik — «katta qismi» (rasmiy)",
        "attach":    "The majority of + plural/uncountable + verb",
        "form_rule": "<b>The (vast/overwhelming) majority of</b> + ot. Fe’l odatda "
                     "<u>ko‘plikda</u>: <i>The majority of respondents <b>were</b> female.</i> "
                     "Teskarisi: <b>a minority of</b>, <b>a small proportion of</b>.",
        "note":      "<p>Task 1 uchun foizni so‘z bilan aytishning eng qulay yo‘li — bir xil "
                     "raqamni ikki marta takrorlamaslik kerak:</p>"
                     "<p>62% → <i><b>the majority of</b></i> · 51% → <i>just over half</i> · "
                     "25% → <i>a quarter</i> · 12% → <i><b>a small minority</b></i> · "
                     "5% → <i>a negligible proportion</i>.</p>",
        "examples": [
            ("The vast majority of households now own at least one mobile phone.",
             "Xonadonlarning katta ko‘pchiligida endi kamida bitta mobil telefon bor."),
        ],
        "synonyms": [
            ("most / most of / the most", "the majority of = rasmiy; most = neytral va qisqa"),
        ],
        "order": 607,
    },
    {
        "pattern":   "all / every / each",
        "category":  "en_article",
        "function":  "degree",
        "level":     3,
        "freq":      2,
        "register":  "both",
        "meaning":   "hamma — «barchasi, har biri»",
        "attach":    "all + plural · every/each + singular",
        "form_rule": "<b>all</b> + ko‘plik ot + ko‘plik fe’l · "
                     "<b>every</b> / <b>each</b> + <u>birlik</u> ot + <u>birlik</u> fe’l. "
                     "<i>each</i> alohida-alohida qaraydi, <i>every</i> guruhni yaxlit oladi.",
        "note":      "<p>⚠️ Task 2 da <i>all</i> juda xavfli so‘z — bitta istisno butun da’voingizni "
                     "yiqitadi. Uni hedging bilan almashtiring: <b>most</b>, <b>the majority of</b>, "
                     "<b>almost all</b>.</p>",
        "mistake":   "<p>❌ <i>Every students <u>have</u> a laptop</i> → ✅ <i><b>Every student "
                     "has</b> a laptop</i> yoki <i><b>All students have</b> laptops</i>.</p>",
        "examples": [
            ("Each of the four countries showed a different pattern of consumption.",
             "To‘rt mamlakatning har biri boshqacha iste’mol manzarasini ko‘rsatdi."),
        ],
        "synonyms": [
            ("most / most of / the most", "all = 100% (xavfli); most = aksariyat (xavfsiz)"),
            ("both / either / neither", "these are for TWO items only"),
        ],
        "order": 608,
    },
    {
        "pattern":   "both / either / neither",
        "category":  "en_article",
        "function":  "listing",
        "level":     4,
        "freq":      2,
        "register":  "both",
        "meaning":   "ikkitalik — «ikkalasi, ikkisidan biri, ikkalasi ham emas»",
        "attach":    "both + plural · either/neither + singular",
        "form_rule": "<b>both</b> + ko‘plik (<i>both countries <b>are</b></i>) · "
                     "<b>either</b> / <b>neither</b> + birlik (<i>neither country <b>is</b></i>) · "
                     "juftlangan shakl: <b>both … and</b> · <b>either … or</b> · "
                     "<b>neither … nor</b>.",
        "note":      "<p>Task 1 da ikki chiziqni bitta gapda birlashtirish uchun ideal: "
                     "<i><b>Both</b> figures rose steadily, <b>although neither</b> reached "
                     "the 2005 level.</i></p>",
        "mistake":   "<p>❌ <i>Neither of them <u>are</u> correct</i> → rasmiy yozuvda "
                     "✅ <i><b>is</b> correct</i>.</p>"
                     "<p>❌ <i>Both of the two countries</i> → ✅ <i><b>Both</b> countries</i> — "
                     "<i>both</i> ning o‘zida «ikkala» bor.</p>",
        "examples": [
            ("Both urban and rural areas experienced a decline in population.",
             "Ham shahar, ham qishloq hududlarida aholi soni kamaydi."),
        ],
        "synonyms": [
            ("all / every / each", "both = faqat IKKITA; all/every = ikkitadan ko‘p"),
        ],
        "order": 609,
    },
    {
        "pattern":   "subject-verb agreement",
        "category":  "en_article",
        "function":  "case",
        "level":     3,
        "freq":      3,
        "register":  "both",
        "meaning":   "ega bilan kesimning moslashuvi — birlikmi yoki ko‘plikmi",
        "attach":    "S(singular) + V(s) · S(plural) + V",
        "form_rule": "Fe’l <u>bosh ot</u>ga moslashadi, oradagi so‘zlarga emas: "
                     "<i><b>The number</b> of students <b>is</b> rising</i> (number = birlik) "
                     "vs <i><b>A number</b> of students <b>are</b> waiting</i> (= «bir necha»). "
                     "<i>Each, every, everyone, neither</i> → birlik.",
        "note":      "<p>Uzun ega bilan yozganda eng ko‘p sodir bo‘ladigan xato. Yozgandan keyin "
                     "tekshiring: egadan predlogli qismni <u>o‘chirib</u> o‘qing — "
                     "<i>The <b>impact</b> (of rising temperatures on coastal cities) <b>is</b>…</i></p>",
        "mistake":   "<p>❌ <i>The <u>number</u> of cars <u>have</u> increased</i> → "
                     "✅ <i>The number of cars <b>has</b> increased</i>.</p>"
                     "<p>❌ <i>Everyone <u>know</u> that…</i> → ✅ <i>Everyone <b>knows</b> that…</i></p>",
        "examples": [
            ("The percentage of adults working from home has tripled since 2019.",
             "Uydan ishlaydigan kattalar ulushi 2019-yildan beri uch baravar oshdi."),
        ],
        "synonyms": [
            ("uncountable nouns", "sanalmaydigan ot doim birlik fe’l oladi"),
            ("all / every / each", "every/each doim birlik fe’l bilan"),
        ],
        "order": 610,
    },
]
