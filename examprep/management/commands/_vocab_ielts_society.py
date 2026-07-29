# -*- coding: utf-8 -*-
"""IELTS vocab bank — Society: education, work, crime & government.

Order decade 600-699. The four Task 2 topics that come back most often. Each
word carries the collocation it actually appears in, because Lexical Resource
is marked on collocation rather than on rare words.

⚠️ Imported SIXTH — uses roots from files 1-3. See toc_ielts_vocab.txt.
See STYLE_GUIDE_VOCAB_IELTS.md.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "Ingliz tili imtihoniga tayyorgarlik (Academic).",
    "icon":    "bi-globe2",
    "color":   "#059669",
}

WORDS = [
    # ── Ta'lim ──────────────────────────────────────────────────────────────
    {
        "word":        "curriculum",
        "roots":       [],
        "pos":         "noun",
        "topic":       "school",
        "level":       5,
        "freq":        2,
        "meaning":     "o‘quv dasturi — maktabda o‘qitiladigan fanlar majmui",
        "collocation": "the school curriculum · add to the curriculum · a national curriculum",
        "note":        "<p>⚠️ Ko‘pligi <b>curricula</b>. Ta’lim inshosining kalit so‘zi: "
                       "<i>Practical subjects should be added to the <b>curriculum</b>.</i></p>",
        "examples":    [("Financial literacy should be part of the school curriculum.",
                         "Moliyaviy savodxonlik maktab o‘quv dasturining bir qismi bo‘lishi kerak.")],
        "related":     [("literacy", "curriculum = nima o‘qitiladi; literacy = natijada nima bilinadi")],
    },
    {
        "word":        "literacy",
        "roots":       [],
        "pos":         "noun",
        "topic":       "school",
        "level":       5,
        "freq":        2,
        "meaning":     "savodxonlik — o‘qish-yozish (yoki bir sohani bilish) darajasi",
        "collocation": "adult literacy · literacy rates · digital literacy",
        "note":        "<p>Kengaygan ma’nosi ham bor: <b>digital literacy</b>, "
                       "<b>financial literacy</b> — «o‘sha sohani bilish». "
                       "Teskarisi — <b>illiteracy</b>.</p>",
        "examples":    [("Literacy rates have risen sharply in the region since 1990.",
                         "Mintaqada savodxonlik darajasi 1990-yildan beri keskin oshdi.")],
        "related":     [("curriculum", "o‘quv dasturi savodxonlikning natijasini belgilaydi")],
    },
    {
        "word":        "vocational",
        "roots":       [],
        "pos":         "adj",
        "topic":       "school",
        "level":       5,
        "freq":        2,
        "meaning":     "kasb-hunarga oid — amaliy kasbga tayyorlaydigan",
        "collocation": "vocational training · vocational courses · vocational qualifications",
        "note":        "<p>Ta’lim mavzusining eng ko‘p qaytariladigan qarama-qarshiligi: "
                       "<b>vocational</b> (kasb-hunar) va <b>academic</b> (nazariy) ta’lim.</p>",
        "examples":    [("Vocational training often leads to employment more quickly than a degree.",
                         "Kasb-hunar ta’limi ko‘pincha diplomdan ko‘ra tezroq ish topishga olib keladi.")],
        "antonyms":    [("academic", "vocational = amaliy kasb; academic = nazariy o‘qish")],
    },
    {
        "word":        "tuition fees",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "school",
        "level":       4,
        "freq":        2,
        "meaning":     "o‘qish to‘lovi — universitet kontrakt puli",
        "collocation": "rising tuition fees · abolish tuition fees · pay tuition fees",
        "note":        "<p>«Oliy ta’lim bepul bo‘lishi kerakmi?» — eng tez-tez uchraydigan "
                       "Task 2 savollaridan biri; javob shu ibora atrofida quriladi.</p>",
        "examples":    [("Rising tuition fees deter students from low-income families.",
                         "O‘qish to‘lovining oshishi kam daromadli oilalardan chiqqan talabalarni chekintiradi.")],
        "related":     [("affordable", "to‘lov masalasi doim «arzonlik» bahsiga ulanadi")],
    },
    {
        "word":        "academic",
        "roots":       [],
        "pos":         "adj",
        "topic":       "school",
        "level":       3,
        "freq":        2,
        "meaning":     "akademik — nazariy, ilmiy ta’limga oid",
        "collocation": "academic performance · academic achievement · academic pressure",
        "note":        "<p><b>academic performance</b> va <b>academic pressure</b> — ta’lim "
                       "inshosining ikki tayyor birikmasi.</p>",
        "examples":    [("Excessive academic pressure can harm children’s mental health.",
                         "Haddan ortiq o‘quv bosimi bolalarning ruhiy salomatligiga zarar yetkazishi mumkin.")],
        "antonyms":    [("vocational", "academic = nazariy; vocational = amaliy")],
    },
    # ── Ish va iqtisod ──────────────────────────────────────────────────────
    {
        "word":        "unemployment",
        "roots":       ["un-/in-"],
        "pos":         "noun",
        "topic":       "work",
        "level":       3,
        "freq":        3,
        "meaning":     "ishsizlik",
        "collocation": "high unemployment · youth unemployment · the unemployment rate",
        "note":        "<p>⚠️ <b>Sanalmaydigan</b>: ❌ <i>unemployments</i>. Odam haqida "
                       "<b>the unemployed</b> (ko‘plik ma’noda): <i>the unemployed <b>are</b>…</i></p>",
        "examples":    [("Youth unemployment remains stubbornly high in several regions.",
                         "Yoshlar orasidagi ishsizlik bir necha mintaqada hamon o‘jarlik bilan yuqori.")],
        "related":     [("workforce", "unemployment = ishsizlar; workforce = ishlayotganlar")],
    },
    {
        "word":        "workforce",
        "roots":       [],
        "pos":         "noun",
        "topic":       "work",
        "level":       5,
        "freq":        2,
        "meaning":     "ishchi kuchi — ishlayotganlar jamlanmasi",
        "collocation": "enter the workforce · a skilled workforce · an ageing workforce",
        "note":        "<p><b>an ageing workforce</b> — demografiya va nafaqa yoshi mavzularida "
                       "tayyor birikma.</p>",
        "examples":    [("More women have entered the workforce over the past three decades.",
                         "So‘nggi uch o‘n yillikda ishchi kuchi safiga ko‘proq ayol qo‘shildi.")],
        "related":     [("unemployment", "ikkalasi ham mehnat bozori haqida")],
    },
    {
        "word":        "productive",
        "roots":       ["duc/duct"],
        "pos":         "adj",
        "topic":       "work",
        "level":       4,
        "freq":        2,
        "meaning":     "samarali, unumli — ko‘p natija beradigan",
        "collocation": "a productive workforce · more productive · counterproductive",
        "note":        "<p>⚠️ <b>counterproductive</b> — «foyda o‘rniga zarar keltiradigan» — "
                       "Task 2 da chorani tanqid qilishda juda foydali: <i>Longer hours are "
                       "often <b>counterproductive</b>.</i></p>",
        "examples":    [("Shorter working weeks have made some teams noticeably more productive.",
                         "Qisqaroq ish haftasi ba’zi jamoalarni sezilarli darajada unumliroq qildi.")],
        "related":     [("productivity", "sifat va ot — bir ildizdan")],
    },
    {
        "word":        "incentive",
        "roots":       [],
        "pos":         "noun",
        "topic":       "economy",
        "level":       5,
        "freq":        2,
        "meaning":     "rag‘bat — nimadir qilishga undovchi foyda",
        "collocation": "financial incentives · provide an incentive to · tax incentives",
        "note":        "<p>Yechim taklif qilishning eng amaliy so‘zi: <i><b>Tax incentives</b> "
                       "would encourage firms to invest in clean technology.</i></p>",
        "examples":    [("Governments could offer incentives for households to install solar panels.",
                         "Hukumatlar xonadonlarni quyosh panellari o‘rnatishga rag‘batlantirishi mumkin.")],
        "antonyms":    [("deterrent", "incentive = qilishga undaydi; deterrent = qilishdan qaytaradi")],
    },
    {
        "word":        "subsidy",
        "roots":       ["sub-"],
        "pos":         "noun",
        "topic":       "economy",
        "level":       5,
        "freq":        2,
        "meaning":     "subsidiya — davlat tomonidan beriladigan moliyaviy yordam",
        "collocation": "government subsidies · fuel subsidies · subsidise public transport",
        "note":        "<p>Fe’li — <b>subsidise</b> (BrE) / subsidize (AmE). Ko‘pligi "
                       "<b>subsidies</b>.</p>",
        "examples":    [("Fuel subsidies encourage consumption and slow the shift to renewables.",
                         "Yoqilg‘i subsidiyalari iste’molni rag‘batlantiradi va qayta tiklanuvchi manbalarga o‘tishni sekinlashtiradi.")],
        "related":     [("incentive", "subsidy = pul yordami; incentive = umumiy rag‘bat")],
    },
    {
        "word":        "living standards",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "society",
        "level":       4,
        "freq":        2,
        "meaning":     "turmush darajasi",
        "collocation": "raise living standards · a decline in living standards · the cost of living",
        "note":        "<p>Yonidagi ibora — <b>the cost of living</b> (yashash qiymati): "
                       "<i>the rising <b>cost of living</b></i>. Ikkalasi iqtisod inshosida "
                       "juftlashib keladi.</p>",
        "examples":    [("Economic growth has raised living standards but widened inequality.",
                         "Iqtisodiy o‘sish turmush darajasini ko‘tardi, lekin tengsizlikni kengaytirdi.")],
        "related":     [("inequality", "turmush darajasi haqidagi bahs doim tengsizlikka ulanadi")],
    },
    # ── Jinoyat va qonun ────────────────────────────────────────────────────
    {
        "word":        "deterrent",
        "roots":       [],
        "pos":         "noun",
        "topic":       "crime",
        "level":       6,
        "freq":        2,
        "meaning":     "qaytaruvchi chora — jinoyatdan qo‘rqitib to‘xtatuvchi omil",
        "collocation": "an effective deterrent · act as a deterrent · deter offenders",
        "note":        "<p><b>Jinoyat mavzusining markaziy tushunchasi:</b> qattiq jazo "
                       "<i>act as a <b>deterrent</b></i> qiladimi yoki yo‘qmi — savol shu. "
                       "Fe’li — <b>deter (somebody from doing)</b>.</p>",
        "examples":    [("There is little evidence that long sentences act as an effective deterrent.",
                         "Uzoq muddatli qamoq jazosi samarali qaytaruvchi omil bo‘lishiga dalil kam.")],
        "antonyms":    [("incentive", "deterrent = qaytaradi; incentive = undaydi")],
    },
    {
        "word":        "rehabilitation",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "crime",
        "level":       6,
        "freq":        1,
        "meaning":     "qayta tarbiyalash — jinoyatchini jamiyatga qaytarish",
        "collocation": "focus on rehabilitation · rehabilitation programmes · rehabilitate offenders",
        "note":        "<p>Jinoyat inshosining ikkinchi tomoni: <b>punishment</b> (jazo) yoki "
                       "<b>rehabilitation</b> (qayta tarbiya) — muvozanatli javob ikkalasini "
                       "ham qamrab oladi.</p>",
        "examples":    [("Prison systems that focus on rehabilitation report lower reoffending rates.",
                         "Qayta tarbiyaga urg‘u beradigan qamoq tizimlarida qayta jinoyat qilish darajasi pastroq.")],
        "antonyms":    [("punishment", "rehabilitation = tuzatish; punishment = jazolash")],
    },
    {
        "word":        "punishment",
        "roots":       [],
        "pos":         "noun",
        "topic":       "crime",
        "level":       3,
        "freq":        2,
        "meaning":     "jazo",
        "collocation": "harsh punishment · capital punishment · a form of punishment",
        "note":        "<p><b>capital punishment</b> = o‘lim jazosi (o‘z-o‘zidan tayyor insho "
                       "mavzusi). Fe’li — <b>punish</b>.</p>",
        "examples":    [("Many argue that harsher punishment does not reduce crime rates.",
                         "Ko‘pchilik qattiqroq jazo jinoyatchilik darajasini kamaytirmaydi deb hisoblaydi.")],
        "antonyms":    [("rehabilitation", "punishment = jazo; rehabilitation = qayta tarbiya")],
    },
    {
        "word":        "legislation",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "government",
        "level":       6,
        "freq":        2,
        "meaning":     "qonunchilik — qabul qilingan qonunlar majmui",
        "collocation": "introduce legislation · strict legislation · anti-smoking legislation",
        "note":        "<p>⚠️ <b>Sanalmaydigan</b>: ❌ <i>legislations</i> → ✅ <i><b>a piece of</b> "
                       "legislation</i>. <i>Law</i> ning rasmiy varianti.</p>",
        "examples":    [("Anti-smoking legislation has significantly reduced consumption.",
                         "Chekishga qarshi qonunchilik iste’molni sezilarli kamaytirdi.")],
        "related":     [("regulation", "legislation = qonunlar; regulation = qoidalar va nazorat")],
    },
    {
        "word":        "regulation",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "government",
        "level":       5,
        "freq":        2,
        "meaning":     "tartibga solish, qoida — davlat nazorati",
        "collocation": "stricter regulation · government regulation · regulate the industry",
        "note":        "<p>Fe’li — <b>regulate</b>. Bahsning ikki qutbi: <b>regulation</b> "
                       "(nazorat) va <b>deregulation</b> (erkinlashtirish).</p>",
        "examples":    [("Stricter regulation of social media has been proposed in several countries.",
                         "Bir necha mamlakatda ijtimoiy tarmoqlarni qattiqroq tartibga solish taklif qilindi.")],
        "related":     [("legislation", "regulation = qoida/nazorat; legislation = qonun")],
    },
    {
        "word":        "enforce",
        "roots":       [],
        "pos":         "verb",
        "topic":       "government",
        "level":       6,
        "freq":        2,
        "meaning":     "ijrosini ta’minlamoq — qonunni amalda qo‘llamoq",
        "collocation": "enforce the law · difficult to enforce · law enforcement",
        "note":        "<p>Kuchli dalil: qonun bor, lekin <i>difficult to <b>enforce</b></i> — "
                       "Task 2 da har qanday taqiq taklifining zaif tomonini ko‘rsatadi.</p>",
        "examples":    [("Such a ban would be extremely difficult to enforce in practice.",
                         "Bunday taqiqni amalda qo‘llash nihoyatda qiyin bo‘lardi.")],
        "related":     [("legislation", "qonun qabul qilinadi, keyin ijro etiladi")],
    },
    # ── Jamiyat ─────────────────────────────────────────────────────────────
    {
        "word":        "welfare",
        "roots":       [],
        "pos":         "noun",
        "topic":       "government",
        "level":       5,
        "freq":        2,
        "meaning":     "ijtimoiy ta’minot; farovonlik",
        "collocation": "the welfare state · welfare benefits · child welfare",
        "note":        "<p>Ikki ma’no: davlat yordami (<b>welfare benefits</b>) va umumiy "
                       "farovonlik (<b>animal welfare</b>).</p>",
        "examples":    [("An ageing population places growing pressure on the welfare system.",
                         "Aholining qarishi ijtimoiy ta’minot tizimiga tobora ko‘proq bosim o‘tkazadi.")],
        "related":     [("wellbeing", "welfare = tizim/yordam; wellbeing = shaxsning holati")],
    },
    {
        "word":        "wellbeing",
        "roots":       [],
        "pos":         "noun",
        "topic":       "health",
        "level":       5,
        "freq":        2,
        "meaning":     "farovonlik — jismoniy va ruhiy yaxshi holat",
        "collocation": "mental wellbeing · improve wellbeing · a sense of wellbeing",
        "note":        "<p>Sog‘liq, ish va ta’lim mavzularining umumiy so‘zi: <i>flexible hours "
                       "improve employees’ <b>wellbeing</b></i>.</p>",
        "examples":    [("Access to green space has a measurable effect on mental wellbeing.",
                         "Yashil hududlardan foydalanish ruhiy farovonlikka o‘lchanadigan ta’sir ko‘rsatadi.")],
        "related":     [("welfare", "wellbeing = shaxsiy holat; welfare = davlat yordami")],
    },
    {
        "word":        "integration",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "society",
        "level":       6,
        "freq":        1,
        "meaning":     "integratsiya — jamiyatga qo‘shilib ketish",
        "collocation": "social integration · integrate into society · successful integration",
        "note":        "<p>Migratsiya mavzusining kalit so‘zi. Fe’li — <b>integrate into</b>. "
                       "Teskarisi — <b>segregation</b>.</p>",
        "examples":    [("Language classes play a crucial role in the integration of migrants.",
                         "Til kurslari migrantlarning integratsiyasida hal qiluvchi rol o‘ynaydi.")],
        "related":     [("diverse", "integratsiya xilma-xil jamiyatda muhim masala")],
    },
    {
        "word":        "discrimination",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "society",
        "level":       5,
        "freq":        2,
        "meaning":     "kamsitish — noqonuniy farq qilish",
        "collocation": "age discrimination · discrimination against · anti-discrimination laws",
        "note":        "<p>Predlogi <b>against</b>: <i>discrimination <b>against</b> older "
                       "workers</i>. Fe’li — <b>discriminate against</b>.</p>",
        "examples":    [("Age discrimination remains common in hiring decisions.",
                         "Yosh bo‘yicha kamsitish ishga qabul qilishda hamon keng tarqalgan.")],
        "related":     [("inequality", "kamsitish tengsizlikning sabablaridan biri")],
    },
    {
        "word":        "the gap between rich and poor",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "society",
        "level":       4,
        "freq":        2,
        "meaning":     "boy va kambag‘al orasidagi tafovut",
        "collocation": "widen the gap between rich and poor · narrow the gap",
        "note":        "<p>Tayyor ibora — lekin bir inshoda bir marta ishlating va keyin "
                       "<b>income inequality</b> ga o‘ting: bir xil fikrni ikki xil aytish "
                       "Lexical Resource uchun aynan shu.</p>",
        "examples":    [("Unregulated growth tends to widen the gap between rich and poor.",
                         "Tartibga solinmagan o‘sish boy va kambag‘al orasidagi tafovutni kengaytirishga moyil.")],
        "synonyms":    [("inequality", "bir ma’no, ikki uslub: ibora — jonli, inequality — akademik")],
    },
    {
        "word":        "rural",
        "roots":       [],
        "pos":         "adj",
        "topic":       "society",
        "level":       3,
        "freq":        3,
        "meaning":     "qishloqqa oid — shahar tashqarisidagi",
        "collocation": "rural areas · rural communities · rural depopulation",
        "note":        "<p>Task 1 xaritalari va Task 2 shaharlashuv mavzusida doimiy juftlik: "
                       "<b>urban</b> — <b>suburban</b> — <b>rural</b>.</p>",
        "examples":    [("Young people continue to leave rural areas in search of work.",
                         "Yoshlar ish izlab qishloq hududlarini tark etishda davom etmoqda.")],
        "antonyms":    [("suburban", "rural = qishloq; suburban = shahar chekkasi")],
    },
    {
        "word":        "congestion",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "society",
        "level":       5,
        "freq":        3,
        "meaning":     "tirbandlik — yo‘llardagi tiqilinch",
        "collocation": "traffic congestion · ease congestion · congestion charges",
        "note":        "<p>⚠️ Sanalmaydigan. <b>congestion charge</b> — shahar markaziga kirish "
                       "uchun to‘lov; transport mavzusidagi eng ko‘p keltiriladigan yechim.</p>",
        "examples":    [("Congestion charges have significantly eased traffic in central London.",
                         "Tirbandlik yig‘imlari Londonning markazidagi transport oqimini sezilarli yengillashtirdi.")],
        "related":     [("overcrowded", "congestion = yo‘lda; overcrowding = joyda")],
    },
    {
        "word":        "infrastructure",
        "roots":       [],
        "pos":         "noun",
        "topic":       "government",
        "level":       5,
        "freq":        3,
        "meaning":     "infratuzilma — yo‘l, transport, tarmoq va inshootlar",
        "collocation": "invest in infrastructure · transport infrastructure · ageing infrastructure",
        "note":        "<p>⚠️ Sanalmaydigan: ❌ <i>infrastructures</i>. Yechim jumlalarida "
                       "deyarli har doim kerak: <i>invest in public transport <b>infrastructure</b></i>.</p>",
        "examples":    [("Rapid population growth has outpaced investment in infrastructure.",
                         "Aholining tez o‘sishi infratuzilmaga sarmoyadan o‘zib ketdi.")],
        "related":     [("urbanisation", "shaharlashuv infratuzilmaga bosim o‘tkazadi")],
    },
]

# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 600 + _i)
