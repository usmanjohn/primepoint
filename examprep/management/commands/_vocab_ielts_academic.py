# -*- coding: utf-8 -*-
"""IELTS vocab bank — Academic language (essay uchun universal so'zlar).

Order decade 500-599. Subject-neutral words: whatever the Task 2 topic turns
out to be, these are the verbs, adjectives and adverbs that hold the argument
together. Weighted towards adjectives, adverbs and verbs over nouns, per the
user's method (§13 of the style guide).

⚠️ Imported FIFTH — uses roots from files 1-3. See toc_ielts_vocab.txt.
See STYLE_GUIDE_VOCAB_IELTS.md.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "Ingliz tili imtihoniga tayyorgarlik (Academic).",
    "icon":    "bi-globe2",
    "color":   "#059669",
}

WORDS = [
    {
        "word":        "analyse",
        "hanja":       "analysis (yun.) — qismlarga ajratish",
        "roots":       ["-ise/-ify"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "tahlil qilmoq — qismlarga ajratib o‘rganmoq",
        "collocation": "analyse the data · a detailed analysis · analytical skills",
        "note":        "<p>Britaniyacha <b>analyse</b>, amerikacha <i>analyze</i>. "
                       "Oti — <b>analysis</b>, ko‘pligi <b>analyses</b>.</p>",
        "examples":    [("Researchers analysed data from over fifty countries.",
                         "Tadqiqotchilar ellikdan ortiq mamlakat ma’lumotlarini tahlil qildi.")],
        "related":     [("evaluate", "analyse = qismlarga ajratish; evaluate = qiymatini baholash")],
    },
    {
        "word":        "evaluate",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "baholamoq — qiymatini yoki samarasini o‘lchamoq",
        "collocation": "evaluate the effectiveness of · a thorough evaluation",
        "note":        "<p>Task 2 da chorani baholashda: <i>It is difficult to <b>evaluate</b> "
                       "the effectiveness of such policies.</i></p>",
        "examples":    [("Governments rarely evaluate the long-term impact of these schemes.",
                         "Hukumatlar bunday dasturlarning uzoq muddatli ta’sirini kamdan-kam baholaydi.")],
        "related":     [("analyse", "analyse = tahlil; evaluate = baho")],
    },
    {
        "word":        "constitute",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "tashkil etmoq — «... hisoblanadi»",
        "collocation": "constitute a threat · constitute the majority · this constitutes",
        "note":        "<p>Ikki ma’no: miqdor (<i>Women <b>constitute</b> 60% of graduates</i>) "
                       "va baho (<i>This <b>constitutes</b> a serious threat</i>). "
                       "Ikkinchisi Task 2 uchun kuchli.</p>",
        "examples":    [("Air pollution constitutes the single greatest health risk in many cities.",
                         "Havo ifloslanishi ko‘p shaharlarda eng katta yagona sog‘liq xavfini tashkil etadi.")],
        "synonyms":    [("account for", "account for = foizni aytadi; constitute = ta’rif beradi")],
    },
    {
        "word":        "attribute",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        2,
        "meaning":     "bog‘lamoq, sabab qilib ko‘rsatmoq — «... ga bog‘liq deb bilmoq»",
        "collocation": "attribute X to Y · can be attributed to · widely attributed to",
        "note":        "<p>Sababni ehtiyotkorlik bilan aytadi: <i>The decline <b>can be attributed "
                       "to</b> falling birth rates.</i> — «sabab shu» deb qat’iy da’vo qilmaydi, "
                       "shuning uchun Band 7 uchun ideal.</p>",
        "examples":    [("The improvement is largely attributed to investment in teacher training.",
                         "Yaxshilanish asosan o‘qituvchilarni tayyorlashga sarmoya kiritilgani bilan bog‘lanadi.")],
        "related":     [("stem from", "attribute to = biz bog‘laymiz; stem from = o‘zi kelib chiqadi")],
    },
    {
        "word":        "stem from",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "kelib chiqmoq — ildizi shunda bo‘lmoq",
        "collocation": "stem from poverty · problems stemming from",
        "note":        "<p><i>result from</i> ning obrazli varianti: <i>Many social problems "
                       "<b>stem from</b> inadequate housing.</i></p>",
        "examples":    [("Much of the resistance stems from a lack of reliable information.",
                         "Qarshilikning katta qismi ishonchli ma’lumot yetishmasligidan kelib chiqadi.")],
        "related":     [("attribute", "stem from = sabab tomondan; attribute to = xulosa tomondan")],
    },
    {
        "word":        "advocate",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        2,
        "meaning":     "yoqlab chiqmoq, targ‘ib qilmoq",
        "collocation": "advocate reform · advocates of the policy · strongly advocate",
        "note":        "<p>Ot sifatida ham: <i><b>advocates of</b> free education argue that…</i> "
                       "— bu Task 2 da qarashni kimga tegishli ekanini aytishning tabiiy yo‘li.</p>",
        "examples":    [("Some economists advocate raising taxes on high-carbon industries.",
                         "Ba’zi iqtisodchilar yuqori uglerodli tarmoqlarga solig‘ni oshirishni yoqlab chiqadi.")],
        "antonyms":    [("oppose", "advocate = yoqlamoq; oppose = qarshi chiqmoq")],
    },
    {
        "word":        "oppose",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "qarshi chiqmoq",
        "collocation": "oppose the plan · strongly opposed to · opposition to",
        "note":        "<p>Sifat shakli predlog oladi: <b>be opposed to</b> + ot/-ing — "
                       "<i>Residents are strongly <b>opposed to</b> the development.</i></p>",
        "examples":    [("Local communities opposed the construction of the new airport.",
                         "Mahalliy aholi yangi aeroport qurilishiga qarshi chiqdi.")],
        "antonyms":    [("advocate", "oppose = qarshi; advocate = tarafdor")],
    },
    {
        "word":        "arguably",
        "roots":       [],
        "pos":         "adv",
        "topic":       "academic",
        "level":       6,
        "freq":        2,
        "meaning":     "ehtimol, bahsli ravishda — «aytish mumkinki»",
        "collocation": "arguably the most important · this is arguably",
        "note":        "<p>Kuchli da’voni bahsga ochiq qoldiradi — hedging’ning eng ixcham shakli: "
                       "<i>Education is <b>arguably</b> the most effective long-term solution.</i></p>",
        "examples":    [("Automation is arguably the greatest challenge facing the labour market.",
                         "Avtomatlashtirish, aytish mumkinki, mehnat bozori oldidagi eng katta muammo.")],
        "related":     [("undoubtedly", "arguably = bahsli; undoubtedly = shubhasiz (teskari kuch)")],
    },
    {
        "word":        "undoubtedly",
        "roots":       [],
        "pos":         "adv",
        "topic":       "academic",
        "level":       5,
        "freq":        1,
        "meaning":     "shubhasiz — aniq, inkor qilib bo‘lmaydigan",
        "collocation": "undoubtedly true · has undoubtedly improved",
        "note":        "<p>Qarshi tomonning haqiqiy tomonini tan olish uchun juda mos: "
                       "<i>Technology has <b>undoubtedly</b> improved access to information; "
                       "<b>however</b>, …</i></p>",
        "examples":    [("Vaccination has undoubtedly saved millions of lives.",
                         "Emlash shubhasiz millionlab hayotni saqlab qoldi.")],
        "antonyms":    [("arguably", "undoubtedly = shubhasiz; arguably = bahsli")],
    },
    {
        "word":        "significant",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       3,
        "freq":        3,
        "meaning":     "sezilarli, muhim — e’tiborga loyiq darajadagi",
        "collocation": "a significant increase · significantly higher · of great significance",
        "note":        "<p>Task 1 va Task 2 ning eng ko‘p kerak bo‘ladigan sifati. Aynan shuning "
                       "uchun uni <b>considerable</b>, <b>substantial</b>, <b>marked</b> bilan "
                       "almashtirib turing.</p>",
        "examples":    [("There has been a significant shift in public attitudes since 2010.",
                         "2010-yildan beri jamoatchilik qarashlarida sezilarli o‘zgarish yuz berdi.")],
        "synonyms":    [("considerable", "ma’nosi yaqin; significant «muhim» ma’nosini ham beradi")],
    },
    {
        "word":        "widespread",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "keng tarqalgan",
        "collocation": "widespread use of · widespread concern · become widespread",
        "note":        "<p><i>Many people…</i> gapini bir so‘zga siqadi: <i>There is "
                       "<b>widespread</b> concern about screen time among children.</i></p>",
        "examples":    [("The widespread use of smartphones has changed how families communicate.",
                         "Smartfonlarning keng tarqalishi oilalar muloqot qilish tarzini o‘zgartirdi.")],
        "synonyms":    [("prevalent", "prevalent = ayni bir joyda/guruhda keng tarqalgan; "
                                      "widespread = umuman hamma joyda")],
    },
    {
        "word":        "prevalent",
        "roots":       [],
        "pos":         "adj",
        "topic":       "health",
        "level":       6,
        "freq":        1,
        "meaning":     "keng tarqalgan, hukmron — ayniqsa muammo yoki kasallik haqida",
        "collocation": "particularly prevalent among · the prevalence of obesity",
        "note":        "<p>Oti — <b>prevalence</b>: <i>the <b>prevalence of</b> diabetes among "
                       "young adults</i>. Sog‘liq mavzusida band-7 birikma.</p>",
        "examples":    [("Obesity is becoming increasingly prevalent among schoolchildren.",
                         "Semizlik maktab o‘quvchilari orasida tobora keng tarqalmoqda.")],
        "synonyms":    [("widespread", "prevalent = ma’lum guruh ichida; widespread = umuman")],
    },
    {
        "word":        "crucial",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "hal qiluvchi, o‘ta muhim",
        "collocation": "play a crucial role · crucial to success · it is crucial that",
        "note":        "<p><b>play a crucial role in</b> + -ing — Task 2 uchun tayyor birikma: "
                       "<i>Schools <b>play a crucial role in</b> shaping attitudes.</i></p>",
        "examples":    [("Access to clean water is crucial to public health.",
                         "Toza suvdan foydalanish jamoat salomatligi uchun hal qiluvchi ahamiyatga ega.")],
        "synonyms":    [("essential", "ma’nosi bir xil — takrorlanmaslik uchun almashtiring")],
    },
    {
        "word":        "essential",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       3,
        "freq":        2,
        "meaning":     "zarur, muhim — usiz bo‘lmaydigan",
        "collocation": "essential for · it is essential that · essential services",
        "note":        "<p>Predlogi: <b>essential for/to</b>. Subjunctive bilan: "
                       "<i>It is <b>essential that</b> every child <b>have</b> access to education.</i></p>",
        "examples":    [("Practical experience is essential for graduates entering the job market.",
                         "Amaliy tajriba mehnat bozoriga kirayotgan bitiruvchilar uchun zarur.")],
        "synonyms":    [("crucial", "crucial biroz kuchliroq — «hal qiluvchi»")],
    },
    {
        "word":        "controversial",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "bahsli, munozarali — qarama-qarshi fikr uyg‘otadigan",
        "collocation": "a controversial issue · remains controversial · controversy",
        "note":        "<p>Kirish xatboshi uchun tayyor boshlanma: <i>The question of whether "
                       "X should be banned remains <b>controversial</b>.</i> Oti — <b>controversy</b>.</p>",
        "examples":    [("Compulsory military service remains a controversial issue in many countries.",
                         "Majburiy harbiy xizmat ko‘p mamlakatlarda hamon bahsli masala bo‘lib qolmoqda.")],
        "related":     [("contradict", "bir ildizdan emas, lekin ikkalasi ham qarama-qarshilik haqida")],
    },
    {
        "word":        "beneficial",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "foydali — naf keltiradigan",
        "collocation": "beneficial to health · mutually beneficial · the benefits of",
        "note":        "<p>Predlogi <b>to</b> yoki <b>for</b>: <i>beneficial <b>to</b> the "
                       "economy</i>. <i>Good for</i> ning akademik varianti.</p>",
        "examples":    [("Bilingual education has proved beneficial to cognitive development.",
                         "Ikki tilli ta’lim kognitiv rivojlanish uchun foydali ekani isbotlandi.")],
        "antonyms":    [("detrimental", "beneficial = foydali; detrimental = zararli")],
    },
    {
        "word":        "detrimental",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       6,
        "freq":        2,
        "meaning":     "zararli — salbiy ta’sir ko‘rsatadigan",
        "collocation": "detrimental to health · a detrimental effect on",
        "note":        "<p><i>bad for</i> ning akademik varianti — Task 2 da juda ko‘p kerak "
                       "bo‘ladi: <i>Excessive screen time can be <b>detrimental to</b> children’s "
                       "sleep.</i></p>",
        "examples":    [("Long commutes have a detrimental effect on family life.",
                         "Uzoq qatnov oila hayotiga salbiy ta’sir ko‘rsatadi.")],
        "antonyms":    [("beneficial", "detrimental = zararli; beneficial = foydali")],
    },
    {
        "word":        "viable",
        "roots":       ["-able"],
        "pos":         "adj",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "hayotga tatbiq etsa bo‘ladigan — amalda ishlaydigan",
        "collocation": "a viable alternative · economically viable · viable solution",
        "note":        "<p><b>a viable alternative</b> — yechim taklif qilishda eng foydali "
                       "birikmalardan: <i>Rail travel is a <b>viable alternative</b> to short-haul "
                       "flights.</i></p>",
        "examples":    [("Wind power has become an economically viable option for many countries.",
                         "Shamol energiyasi ko‘p mamlakatlar uchun iqtisodiy jihatdan maqbul variantga aylandi.")],
        "synonyms":    [("feasible", "feasible = amalga oshirsa bo‘ladigan; viable = uzoq muddat "
                                     "yashab keta oladigan")],
    },
    {
        "word":        "feasible",
        "roots":       [],
        "pos":         "adj",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "amalga oshirsa bo‘ladigan — imkoni bor",
        "collocation": "technically feasible · a feasible solution · feasibility",
        "note":        "<p>Taklifning kuchsiz tomonini tan olishda: <i>Such a scheme may not be "
                       "<b>feasible</b> in poorer regions.</i></p>",
        "examples":    [("Free public transport is feasible only in relatively wealthy cities.",
                         "Bepul jamoat transporti faqat nisbatan boy shaharlarda amalga oshsa bo‘ladi.")],
        "synonyms":    [("viable", "feasible = qilib bo‘ladi; viable = davom ettirib bo‘ladi")],
    },
    {
        "word":        "implement",
        "roots":       [],
        "pos":         "verb",
        "topic":       "government",
        "level":       5,
        "freq":        3,
        "meaning":     "amalga oshirmoq, joriy etmoq (siyosat, chora)",
        "collocation": "implement a policy · implementation of · fully implemented",
        "note":        "<p>Task 2 yechim qismining asosiy fe’li: <i>Governments should "
                       "<b>implement</b> stricter emissions standards.</i> "
                       "Oti — <b>implementation</b>.</p>",
        "examples":    [("The measures were implemented gradually over a five-year period.",
                         "Choralar besh yillik davr mobaynida bosqichma-bosqich joriy etildi.")],
        "synonyms":    [("introduce", "introduce = birinchi marta kiritish; implement = to‘liq "
                                      "amalga oshirish")],
    },
    {
        "word":        "address",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        3,
        "meaning":     "hal qilishga kirishmoq — muammo bilan shug‘ullanmoq",
        "collocation": "address the problem · address the root cause · needs to be addressed",
        "note":        "<p>«Manzil» emas! Task 2 da muammoga qaratilgan harakat: <i>These "
                       "policies fail to <b>address</b> the root cause of the problem.</i> — "
                       "qarshi dalilni tanqid qilishning eng qulay yo‘li.</p>",
        "examples":    [("Any lasting solution must address the underlying economic causes.",
                         "Har qanday barqaror yechim asosdagi iqtisodiy sabablarni hal qilishi kerak.")],
        "synonyms":    [("tackle", "tackle = biroz og‘zakiroq va faolroq; address = akademik")],
    },
    {
        "word":        "tackle",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       4,
        "freq":        2,
        "meaning":     "kurashmoq, hal qilishga urinmoq",
        "collocation": "tackle climate change · tackle crime · tackle the issue",
        "note":        "<p>Sport ma’nosidan kelib chiqqan, lekin siyosat tilida butunlay tabiiy: "
                       "<i>measures to <b>tackle</b> air pollution</i>.</p>",
        "examples":    [("Cities are using congestion charges to tackle traffic and pollution.",
                         "Shaharlar tirbandlik va ifloslanishga qarshi kurashish uchun yig‘imlardan foydalanmoqda.")],
        "synonyms":    [("address", "address = rasmiyroq; tackle = jonliroq")],
    },
    {
        "word":        "alleviate",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "yengillashtirmoq — muammoni qisman kamaytirmoq",
        "collocation": "alleviate poverty · alleviate pressure on · help alleviate",
        "note":        "<p>«Hal qilmaydi, lekin yengillashtiradi» — ehtiyotkor va aniq: "
                       "<i>Subsidies can <b>alleviate</b> the pressure on low-income families.</i></p>",
        "examples":    [("New housing would alleviate overcrowding in the city centre.",
                         "Yangi uy-joylar shahar markazidagi tig‘izlikni yengillashtirardi.")],
        "synonyms":    [("tackle", "tackle = muammoga hujum; alleviate = og‘riqni kamaytirish")],
    },
    {
        "word":        "distinguish",
        "roots":       [],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        1,
        "meaning":     "farqlamoq — bir-biridan ajratmoq",
        "collocation": "distinguish between X and Y · a clear distinction",
        "note":        "<p>Qolipi: <b>distinguish between A and B</b>. Oti — <b>distinction</b>: "
                       "<i>It is important to draw a <b>distinction between</b> …</i></p>",
        "examples":    [("It is important to distinguish between correlation and causation.",
                         "Bog‘liqlik bilan sababiyatni farqlash muhim.")],
        "related":     [("compare", "distinguish = farqni ko‘rsatish; compare = ikkalasini qiyoslash")],
    },
    {
        "word":        "compare",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       2,
        "freq":        2,
        "meaning":     "solishtirmoq, qiyoslamoq",
        "collocation": "compare X with Y · compared with 2010 · in comparison",
        "note":        "<p>Britaniya uslubida <b>compare with</b> (aniq taqqoslash), "
                       "<i>compare to</i> (o‘xshatish). Task 1 kirishida: <i>The chart "
                       "<b>compares</b> …</i></p>",
        "examples":    [("The table compares energy consumption in five European countries.",
                         "Jadval besh Yevropa mamlakatidagi energiya iste’molini solishtiradi.")],
        "related":     [("distinguish", "compare = yonma-yon qo‘yish; distinguish = farqni ajratish")],
    },
    {
        "word":        "notion",
        "roots":       [],
        "pos":         "noun",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "qarash, taxmin — asoslanmagan bo‘lishi mumkin bo‘lgan fikr",
        "collocation": "the notion that · reject the notion · a popular notion",
        "note":        "<p>Ichida yengil shubha bor — shuning uchun qarshi fikrni kiritishda "
                       "juda mos: <i>The <b>notion that</b> money buys happiness is widely "
                       "challenged.</i></p>",
        "examples":    [("The notion that young people are less engaged politically is questionable.",
                         "Yoshlar siyosatga kamroq qiziqadi degan qarash bahsli.")],
        "synonyms":    [("concept", "concept = shakllangan tushuncha; notion = shubhali qarash")],
    },
]

# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 500 + _i)
