# -*- coding: utf-8 -*-
"""IELTS vocab bank — Task 1: data & trend language (grafik tili).

Order decade 400-499. Writing Task 1 is written almost entirely out of this
list: a verb of movement, an adverb of degree, a noun for the shape of the
line, and a way of saying a proportion without repeating the number. The
antonym pairs (soar/plummet, majority/minority) matter as much as the words.

⚠️ Imported FOURTH — uses roots from files 1-3. See toc_ielts_vocab.txt.
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
        "word":        "soar",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "keskin ko‘tarilmoq — juda tez va baland o‘smoq",
        "collocation": "prices soared · soaring demand · soar to a peak",
        "note":        "<p>Eng kuchli o‘sish fe’li — faqat <u>haqiqatan keskin</u> ko‘tarilish "
                       "uchun ishlating. Kichik o‘sishga qo‘llasangiz, ma’lumotni noto‘g‘ri "
                       "talqin qilgan bo‘lasiz va ball yo‘qotasiz.</p>",
        "examples":    [("House prices soared between 2003 and 2007 before collapsing.",
                         "Uy narxlari 2003-2007 yillarda keskin ko‘tarildi, so‘ng qulab tushdi.")],
        "synonyms":    [("surge", "surge = to‘lqinsimon keskin o‘sish (ko‘pincha qisqa muddatli); "
                                  "soar = uzoq va baland ko‘tarilish")],
        "antonyms":    [("plummet", "soar = keskin KO‘TARILISH; plummet = keskin PASAYISH")],
    },
    {
        "word":        "plummet",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "keskin pasaymoq — tik tushmoq",
        "collocation": "sales plummeted · plummet to a low of · a plummeting share",
        "note":        "<p><i>plunge</i>, <i>collapse</i>, <i>slump</i> bilan bir oila. "
                       "Yumshoqroq varianti — <b>decline</b>, o‘rtacha — <b>drop</b>.</p>",
        "examples":    [("Newspaper circulation plummeted after the arrival of online news.",
                         "Onlayn yangiliklar paydo bo‘lgach, gazeta tirajlari keskin tushib ketdi.")],
        "antonyms":    [("soar", "plummet = tik pasayish; soar = tik ko‘tarilish")],
    },
    {
        "word":        "surge",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       5,
        "freq":        1,
        "meaning":     "to‘satdan keskin o‘sish — «to‘lqin»",
        "collocation": "a surge in demand · a sudden surge · surge to a record high",
        "note":        "<p>Ot va fe’l sifatida ishlaydi. <i>a <b>surge in</b> …</i> — predlogi "
                       "<b>in</b>, xuddi <i>an increase in</i> kabi.</p>",
        "examples":    [("There was a surge in online shopping during the pandemic.",
                         "Pandemiya davrida onlayn xaridda keskin o‘sish kuzatildi.")],
        "synonyms":    [("soar", "surge = qisqa va to‘satdan; soar = uzoq va baland")],
    },
    {
        "word":        "fluctuate",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        3,
        "meaning":     "tebranmoq — goh ko‘tarilib, goh tushib turmoq",
        "collocation": "fluctuate between X and Y · considerable fluctuation · fluctuate wildly",
        "note":        "<p><b>Notekis chiziq uchun yagona to‘g‘ri fe’l.</b> Chiziq bir necha marta "
                       "yuqoriga-pastga ketsa, uni «o‘sdi» yoki «tushdi» deb aytmang: "
                       "<i>The figure <b>fluctuated between</b> 20 and 30 units.</i> "
                       "Oti — <b>fluctuation</b>.</p>",
        "examples":    [("Oil prices fluctuated considerably throughout the decade.",
                         "Neft narxlari o‘n yillik davomida sezilarli tebranib turdi.")],
        "antonyms":    [("remain stable", "fluctuate = tebranadi; remain stable = o‘zgarmaydi")],
    },
    {
        "word":        "level off",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "barqarorlashmoq — o‘sib/tushib kelib, tekislanmoq",
        "collocation": "level off at 40% · then levelled off · plateau",
        "note":        "<p>Chiziq o‘zgarishdan to‘xtab, tekis ketganda: <i>Growth <b>levelled "
                       "off at</b> around 60%.</i> Sinonimlari: <b>plateau</b> (fe’l ham), "
                       "<b>stabilise</b>, <b>remain steady</b>.</p>",
        "examples":    [("After rising sharply, the figure levelled off at just under 50%.",
                         "Keskin ko‘tarilgandan so‘ng ko‘rsatkich 50% dan bir oz pastda barqarorlashdi.")],
        "synonyms":    [("remain stable", "level off = o‘zgarishdan keyin tekislanish; "
                                          "remain stable = boshidan o‘zgarmaslik")],
    },
    {
        "word":        "remain stable",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "data",
        "level":       3,
        "freq":        3,
        "meaning":     "o‘zgarmay qolmoq — barqaror turmoq",
        "collocation": "remain stable · remain unchanged · hold steady at",
        "note":        "<p>Tekis chiziq uchun: <i>The figure for Germany <b>remained stable</b> "
                       "at around 30%.</i> Muqobillar: <i>remained unchanged</i>, "
                       "<i>showed little change</i>, <i>stayed constant</i>.</p>",
        "examples":    [("Spending on education remained stable throughout the period.",
                         "Ta’limga sarflangan mablag‘ davr davomida o‘zgarmay qoldi.")],
        "antonyms":    [("fluctuate", "remain stable = tekis; fluctuate = tebranuvchan")],
    },
    {
        "word":        "peak",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "cho‘qqi — eng yuqori nuqta",
        "collocation": "reach a peak of · peak at 80% · a peak in 2010",
        "note":        "<p>Ham ot, ham fe’l: <i>reached <b>a peak of</b> 80 million</i> = "
                       "<i><b>peaked at</b> 80 million</i>. Ikkinchisi ixchamroq — "
                       "Task 1 da shuni ishlating.</p>",
        "examples":    [("Visitor numbers peaked at 3 million in 2015 before falling back.",
                         "Tashrif buyuruvchilar soni 2015-yilda 3 millionga chiqib, so‘ng pasaydi.")],
        "antonyms":    [("trough", "peak = eng yuqori nuqta; trough = eng past nuqta")],
    },
    {
        "word":        "trough",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       6,
        "freq":        1,
        "meaning":     "eng past nuqta — chuqurlik",
        "collocation": "hit a trough · a low of · reach its lowest point",
        "note":        "<p>Kamroq ishlatiladi; xavfsizroq muqobil — <b>a low of</b> yoki "
                       "<b>its lowest point</b>: <i>The figure fell to <b>a low of</b> 12%.</i></p>",
        "examples":    [("Production reached a trough in 2009 and recovered slowly thereafter.",
                         "Ishlab chiqarish 2009-yilda eng past nuqtaga tushdi va keyin sekin tiklandi.")],
        "antonyms":    [("peak", "trough = eng past; peak = eng yuqori")],
    },
    {
        "word":        "marginal",
        "roots":       [],
        "pos":         "adj",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "arzimas, juda kichik — sezilmas darajadagi",
        "collocation": "a marginal increase · marginally higher · only marginal change",
        "note":        "<p>Kichik o‘zgarishni aniq aytish uchun: <i>a <b>marginal</b> rise of "
                       "just 2%</i>. Ravishi — <b>marginally</b>: <i>marginally higher than</i>.</p>",
        "examples":    [("The figure for Spain showed only a marginal increase over the period.",
                         "Ispaniya ko‘rsatkichi davr davomida faqat arzimas o‘sishni ko‘rsatdi.")],
        "antonyms":    [("substantial", "marginal = arzimas; substantial = salmoqli")],
    },
    {
        "word":        "considerable",
        "roots":       [],
        "pos":         "adj",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "sezilarli, anchagina — katta miqdordagi",
        "collocation": "a considerable increase · considerably higher · considerable variation",
        "note":        "<p>Task 1 va Task 2 da <i>very big</i> ni almashtiradi. Ravishi "
                       "<b>considerably</b> qiyosiy shakl bilan juda yaxshi ishlaydi: "
                       "<i><b>considerably</b> higher than</i>.</p>",
        "examples":    [("There was considerable variation between the four countries.",
                         "To‘rt mamlakat orasida sezilarli tafovut bor edi.")],
        "synonyms":    [("substantial", "ikkalasi bir xil ma’noda — matnda navbat bilan ishlating")],
    },
    {
        "word":        "proportion",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "ulush, nisbat — butunning qismi",
        "collocation": "a large proportion of · the proportion of X rose · in proportion to",
        "note":        "<p>Foizni so‘z bilan aytishning eng akademik yo‘li: <i>a <b>significant "
                       "proportion of</b> households</i>. ⚠️ Fe’l <i>proportion</i> ga emas, "
                       "ma’noga qarab moslashadi — imtihonda birlik xavfsizroq.</p>",
        "examples":    [("The proportion of households with internet access rose from 20% to 85%.",
                         "Internetga ega xonadonlar ulushi 20% dan 85% gacha oshdi.")],
        "synonyms":    [("percentage", "percentage = aniq foiz raqami; proportion = umumiy ulush")],
    },
    {
        "word":        "account for",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "data",
        "level":       5,
        "freq":        3,
        "meaning":     "tashkil qilmoq — «... foizni tashkil etadi»",
        "collocation": "account for 40% of · account for the majority of",
        "note":        "<p><b>Pie chart uchun eng kerakli ibora.</b> <i>Coal <b>accounted for</b> "
                       "just over a third of total output.</i> Ikkinchi ma’nosi — «izohlab bermoq»: "
                       "<i>This <b>accounts for</b> the sharp rise.</i></p>",
        "examples":    [("Transport accounted for nearly a quarter of total emissions.",
                         "Transport umumiy chiqindilarning deyarli chorak qismini tashkil qildi.")],
        "synonyms":    [("make up", "make up = neytral/og‘zakiroq; account for = akademik")],
    },
    {
        "word":        "respectively",
        "roots":       [],
        "pos":         "adv",
        "topic":       "data",
        "level":       6,
        "freq":        2,
        "meaning":     "tegishlicha — sanalgan tartibda",
        "collocation": "45% and 30% respectively · rose and fell respectively",
        "note":        "<p>Ikki raqamni bitta gapda berish imkonini beradi — Task 1 uchun oltin: "
                       "<i>The figures for France and Italy were 45% and 30% <b>respectively</b>.</i> "
                       "⚠️ Tartib mos kelishi shart, aks holda gap yolg‘on bo‘ladi.</p>",
        "examples":    [("Spending rose in Japan and fell in Korea, by 12% and 8% respectively.",
                         "Xarajatlar Yaponiyada oshdi va Koreyada kamaydi — tegishlicha 12% va 8% ga.")],
        "related":     [("proportion", "ikkalasi ham raqamlarni ixcham bayon qiladi")],
    },
    {
        "word":        "threefold",
        "roots":       [],
        "pos":         "adj",
        "topic":       "data",
        "level":       6,
        "freq":        1,
        "meaning":     "uch karra — «uch baravar»",
        "collocation": "a threefold increase · rise threefold · a twofold rise",
        "note":        "<p><i>three times as much</i> ning ixcham shakli: <i>a <b>threefold</b> "
                       "increase in demand</i>. Oilasi: <b>twofold</b>, <b>fourfold</b>, "
                       "<b>tenfold</b>. Fe’l bilan ham: <i>rose <b>threefold</b></i>.</p>",
        "examples":    [("The country recorded a threefold increase in solar capacity.",
                         "Mamlakat quyosh quvvatining uch karra oshganini qayd etdi.")],
        "related":     [("double", "double = ikki baravar (fe’l ham); threefold = uch karra (sifat)")],
    },
    {
        "word":        "double",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       3,
        "freq":        3,
        "meaning":     "ikki baravar oshmoq / oshirmoq",
        "collocation": "more than doubled · double the number of · double that of",
        "note":        "<p>Ham fe’l, ham sifat: <i>The figure <b>doubled</b></i> · "
                       "<i>output was <b>double that of</b> Spain</i>. "
                       "Juftlari: <b>triple</b>, <b>quadruple</b>, <b>halve</b> (yarmiga tushmoq).</p>",
        "examples":    [("The number of car owners more than doubled between 1990 and 2010.",
                         "Avtomobil egalari soni 1990-2010 yillarda ikki baravardan ko‘proq oshdi.")],
        "antonyms":    [("halve", "double = ikki baravar oshmoq; halve = yarmiga tushmoq")],
    },
    {
        "word":        "halve",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        1,
        "meaning":     "yarmiga tushmoq / kamaytirmoq",
        "collocation": "halve emissions · numbers halved · fall by half",
        "note":        "<p>Talaffuzi «hav» — <i>l</i> o‘qilmaydi (Speaking uchun). "
                       "Muqobil: <b>fall by half</b>, <b>drop to half</b>.</p>",
        "examples":    [("The government aims to halve carbon emissions within a decade.",
                         "Hukumat o‘n yil ichida uglerod chiqindilarini ikki barobar qisqartirishni maqsad qilgan.")],
        "antonyms":    [("double", "halve = yarmiga; double = ikki baravarga")],
    },
    {
        "word":        "percentage",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       3,
        "freq":        3,
        "meaning":     "foiz ko‘rsatkichi",
        "collocation": "the percentage of · a high percentage · percentage points",
        "note":        "<p>⚠️ <b>percentage</b> (ot, «foiz ko‘rsatkichi») va <b>percent / %</b> "
                       "(raqam bilan) farq qiladi: ❌ <i>20 percentage</i> → ✅ <i>20 <b>percent</b></i> "
                       "yoki ✅ <i>the <b>percentage</b> of students</i>.</p>"
                       "<p>Foizlar orasidagi farq — <b>percentage points</b>, foiz emas.</p>",
        "examples":    [("The percentage of women in higher education rose steadily.",
                         "Oliy ta’limdagi ayollar ulushi barqaror o‘sdi.")],
        "synonyms":    [("proportion", "proportion = umumiy ulush (so‘z bilan); percentage = aniq foiz")],
    },
    {
        "word":        "per capita",
        "roots":       [],
        "pos":         "phrase",
        "topic":       "data",
        "level":       6,
        "freq":        1,
        "meaning":     "jon boshiga — har bir odamga to‘g‘ri keladigan",
        "collocation": "per capita income · consumption per capita · GDP per capita",
        "note":        "<p>Lotincha ibora («har bosh uchun»). Diagramma sarlavhasida uchrasa, "
                       "uni javobda takrorlash o‘rniga <i>per person</i> deb ham berish mumkin.</p>",
        "examples":    [("Water consumption per capita was highest in the United States.",
                         "Jon boshiga suv iste’moli AQSHda eng yuqori bo‘ldi.")],
        "related":     [("consumption", "diagrammalarda deyarli doim birga keladi")],
    },
    {
        "word":        "overtake",
        "roots":       ["over-"],
        "pos":         "verb",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "ortda qoldirmoq — ilgarilab ketmoq",
        "collocation": "overtake in 2005 · was overtaken by · surpass",
        "note":        "<p>Ikki chiziq kesishgan joyni tasvirlaydi — Task 1 da bu nuqtani "
                       "albatta aytish kerak: <i>Solar power <b>overtook</b> coal in 2018.</i></p>",
        "examples":    [("By 2012 China had overtaken the United States as the largest emitter.",
                         "2012-yilga kelib Xitoy eng yirik chiqindi manbai sifatida AQShni ortda qoldirdi.")],
        "synonyms":    [("exceed", "exceed = chegaradan oshmoq; overtake = boshqasini ortda qoldirmoq")],
    },
    {
        "word":        "gap",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       3,
        "freq":        2,
        "meaning":     "tafovut, farq — ikki ko‘rsatkich orasidagi bo‘shliq",
        "collocation": "the gap widened · a narrowing gap · the gap between rich and poor",
        "note":        "<p>Ikki chiziqning bir-biridan uzoqlashishi yoki yaqinlashishi: "
                       "<i>The <b>gap</b> between the two <b>widened</b> after 2000</i> · "
                       "<i>the gap <b>narrowed</b></i>.</p>",
        "examples":    [("The gap between urban and rural incomes widened throughout the period.",
                         "Shahar va qishloq daromadlari orasidagi tafovut davr davomida kengaydi.")],
        "related":     [("inequality", "gap = raqamli farq; inequality = ijtimoiy tengsizlik")],
    },
    {
        "word":        "outnumber",
        "roots":       [],
        "pos":         "verb",
        "topic":       "data",
        "level":       6,
        "freq":        1,
        "meaning":     "soni jihatidan ko‘p bo‘lmoq — «... dan ko‘proq»",
        "collocation": "outnumber men by two to one · far outnumbered",
        "note":        "<p>Ixcham qiyoslash: <i>Female students <b>outnumbered</b> male students "
                       "by three to one.</i> — bitta fe’lda butun jumla ma’nosi.</p>",
        "examples":    [("In 2010, mobile subscriptions outnumbered landlines for the first time.",
                         "2010-yilda mobil obunalar birinchi marta uyali bo‘lmagan liniyalardan ko‘p bo‘ldi.")],
        "related":     [("overtake", "outnumber = miqdoran ko‘p; overtake = vaqt ichida ortda qoldirish")],
    },
    {
        "word":        "expenditure",
        "roots":       [],
        "pos":         "noun",
        "topic":       "data",
        "level":       5,
        "freq":        2,
        "meaning":     "xarajat — sarflangan mablag‘",
        "collocation": "household expenditure · public expenditure · expenditure on health",
        "note":        "<p><i>spending</i> ning rasmiy varianti; Task 1 diagrammalarida ko‘p "
                       "uchraydi. Predlogi <b>on</b>: <i>expenditure <b>on</b> education</i>.</p>",
        "examples":    [("Household expenditure on food fell steadily as incomes rose.",
                         "Daromadlar oshgani sari xonadonlarning oziq-ovqatga xarajati barqaror kamaydi.")],
        "related":     [("consumption", "expenditure = sarflangan pul; consumption = sarflangan miqdor")],
    },
    {
        "word":        "revenue",
        "roots":       [],
        "pos":         "noun",
        "topic":       "economy",
        "level":       5,
        "freq":        2,
        "meaning":     "daromad — tushum (davlat yoki kompaniya)",
        "collocation": "tax revenue · generate revenue · revenue from tourism",
        "note":        "<p>Shaxsiy daromad emas — u <b>income</b>. <i>Revenue</i> = tashkilot yoki "
                       "davlat tushumi: <i>tax <b>revenue</b></i>.</p>",
        "examples":    [("Tourism generates substantial revenue for coastal regions.",
                         "Turizm sohil mintaqalari uchun katta daromad keltiradi.")],
        "synonyms":    [("income", "income = shaxs/oila daromadi; revenue = tashkilot yoki davlat tushumi")],
    },
    {
        "word":        "steadily",
        "roots":       [],
        "pos":         "adv",
        "topic":       "data",
        "level":       3,
        "freq":        3,
        "meaning":     "barqaror ravishda — bir tekis, uzluksiz",
        "collocation": "rise steadily · steadily declining · a steady increase",
        "note":        "<p>Tekis va uzluksiz o‘zgarish uchun. Sifat shakli — <b>steady</b>: "
                       "<i>a <b>steady</b> rise</i>. Ikkalasini almashtirib ishlatish "
                       "takrorlanishdan qutqaradi.</p>",
        "examples":    [("The number of international students has risen steadily since 2000.",
                         "Xalqaro talabalar soni 2000-yildan beri barqaror o‘sib bormoqda.")],
        "related":     [("remain stable", "steadily = tekis o‘zgarish; remain stable = o‘zgarmaslik")],
    },
    {
        "word":        "dramatically",
        "roots":       [],
        "pos":         "adv",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "keskin, sezilarli darajada",
        "collocation": "fell dramatically · a dramatic rise · change dramatically",
        "note":        "<p>Kuchli o‘zgarish ravishi — <i>sharply</i>, <i>significantly</i>, "
                       "<i>markedly</i> bilan bir qatorda. Bir insho ichida bir xilini "
                       "takrorlamang.</p>",
        "examples":    [("Attitudes towards remote work have changed dramatically since 2020.",
                         "Masofaviy ishga munosabat 2020-yildan beri keskin o‘zgardi.")],
        "synonyms":    [("steadily", "dramatically = keskin; steadily = bir tekis")],
    },
]


# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 400 + _i)
