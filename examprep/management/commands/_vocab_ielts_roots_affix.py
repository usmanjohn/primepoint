# -*- coding: utf-8 -*-
"""IELTS vocab bank — Root family 3: prefixes & suffixes (qo'shimchalar).

Order decade 300-399. Affixes are roots too on an English track: `over-`
against `under-`, `un-` against nothing, `-ion` turning a verb into the noun
an academic sentence needs. This file defines them and shows the pairs where
one letter flips the meaning (sustainable / unsustainable).

⚠️ Imported THIRD — may reference roots from files 1-2. See toc_ielts_vocab.txt.
See STYLE_GUIDE_VOCAB_IELTS.md.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "Ingliz tili imtihoniga tayyorgarlik (Academic).",
    "icon":    "bi-globe2",
    "color":   "#059669",
}

ROOTS = [
    {
        "syllable": "re-",
        "hanja":    "re- (lat.) — qayta, orqaga",
        "meaning":  "qayta — yana, orqaga",
        "note":     "<p><b>re</b>cycle, <b>re</b>new, <b>re</b>form, <b>re</b>duce, "
                    "<b>re</b>store. Ekologiya inshosining yarmi shu qo‘shimcha bilan yoziladi.</p>",
        "order":    300,
    },
    {
        "syllable": "pre-",
        "hanja":    "prae- (lat.) — oldin",
        "meaning":  "oldin — oldindan, oldingi",
        "note":     "<p><b>pre</b>dict, <b>pre</b>vent (oldini olmoq), <b>pre</b>vious, "
                    "<b>pre</b>school, <b>pre</b>requisite.</p>",
        "order":    301,
    },
    {
        "syllable": "sub-",
        "hanja":    "sub- (lat.) — ost",
        "meaning":  "ost — ostida, quyi",
        "note":     "<p><b>sub</b>urban (shahar chekkasi), <b>sub</b>sidy, <b>sub</b>stantial "
                    "(«ostida asos bor» → salmoqli), <b>sub</b>merge.</p>",
        "order":    302,
    },
    {
        "syllable": "inter-",
        "hanja":    "inter- (lat.) — orasida",
        "meaning":  "orasida — o‘zaro",
        "note":     "<p><b>inter</b>national, <b>inter</b>act, <b>inter</b>vention "
                    "(aralashuv), <b>inter</b>connected.</p>",
        "order":    303,
    },
    {
        "syllable": "trans-",
        "hanja":    "trans- (lat.) — orqali, narigi tomon",
        "meaning":  "orqali — bir tomondan ikkinchisiga",
        "note":     "<p><b>trans</b>port, <b>trans</b>fer, <b>trans</b>form (shaklini "
                    "o‘zgartirmoq), <b>trans</b>parent (ochiq-oydin).</p>",
        "order":    304,
    },
    {
        "syllable": "over-",
        "hanja":    "over- (ing.) — ortiqcha",
        "meaning":  "ortiqcha — haddan tashqari, ustidan",
        "note":     "<p><b>over</b>crowded, <b>over</b>estimate, <b>over</b>look "
                    "(e’tibordan chetda qoldirmoq), <b>over</b>whelming. "
                    "Juftligi — <b>under-</b>.</p>",
        "order":    305,
    },
    {
        "syllable": "under-",
        "hanja":    "under- (ing.) — yetarli emas",
        "meaning":  "kam — yetarli emas, ostida",
        "note":     "<p><b>under</b>estimate, <b>under</b>mine (asosini yemirmoq), "
                    "<b>under</b>go (boshdan kechirmoq), <b>under</b>privileged, "
                    "<b>under</b>funded.</p>",
        "order":    306,
    },
    {
        "syllable": "un-/in-",
        "hanja":    "un- / in- — inkor",
        "meaning":  "inkor — «...siz, ...emas»",
        "note":     "<p>Ma’noni teskari qiladi: <b>un</b>sustainable, <b>un</b>employment, "
                    "<b>in</b>equality, <b>in</b>evitable, <b>im</b>possible (p, b oldidan "
                    "<b>im-</b>), <b>ir</b>relevant (r oldidan <b>ir-</b>), "
                    "<b>il</b>legal (l oldidan <b>il-</b>).</p>",
        "order":    307,
    },
    {
        "syllable": "-ion",
        "hanja":    "-tio (lat.) — ot yasovchi",
        "meaning":  "ot yasovchi — fe’lni otga aylantiradi",
        "note":     "<p>Akademik uslubning motori (nominalizatsiya): pollute → pollu<b>tion</b>, "
                    "educate → educa<b>tion</b>, consume → consump<b>tion</b>, "
                    "reduce → reduc<b>tion</b>.</p>",
        "order":    308,
    },
    {
        "syllable": "-able",
        "hanja":    "-abilis (lat.) — sifat yasovchi",
        "meaning":  "sifat yasovchi — «... qilsa bo‘ladigan»",
        "note":     "<p>sustain<b>able</b>, afford<b>able</b>, renew<b>able</b>, "
                    "avoid<b>able</b>, access<b>ible</b> (-ible varianti). "
                    "Ot shakli — <b>-ability</b>.</p>",
        "order":    309,
    },
    {
        "syllable": "-ise/-ify",
        "hanja":    "-izein (yun.) / -ficare (lat.) — fe’l yasovchi",
        "meaning":  "fe’l yasovchi — «... ga aylantirmoq»",
        "note":     "<p>modern<b>ise</b>, industrial<b>ise</b>, urban<b>ise</b>, "
                    "just<b>ify</b>, simpl<b>ify</b>. ⚠️ Britaniyacha <b>-ise</b>, "
                    "amerikacha <b>-ize</b> — bittasini tanlab, oxirigacha saqlang.</p>",
        "order":    310,
    },
]

WORDS = [
    {
        "word":        "renewable",
        "hanja":       "re- + new + -able",
        "roots":       ["re-", "-able"],
        "pos":         "adj",
        "topic":       "environment",
        "level":       3,
        "freq":        3,
        "meaning":     "qayta tiklanuvchi — tugamaydigan (energiya haqida)",
        "collocation": "renewable energy · renewable sources · switch to renewables",
        "note":        "<p>Ekologiya va energiya diagrammalarining asosiy so‘zi. Otlashgan "
                       "ko‘plik shakli ham bor: <i>invest in <b>renewables</b></i>.</p>",
        "examples":    [("Renewable sources accounted for a quarter of total electricity output.",
                         "Qayta tiklanuvchi manbalar umumiy elektr ishlab chiqarishning chorak qismini tashkil qildi.")],
        "antonyms":    [("fossil fuels", "renewable = tiklanadi; fossil fuels = tugaydi")],
    },
    {
        "word":        "recycle",
        "hanja":       "re- + cycle",
        "roots":       ["re-"],
        "pos":         "verb",
        "topic":       "environment",
        "level":       2,
        "freq":        3,
        "meaning":     "qayta ishlamoq — chiqindini yangidan foydalanishga yaroqli qilmoq",
        "collocation": "recycle waste · recycling rates · recyclable materials",
        "note":        "<p>Task 1 jarayon diagrammalarida ham, Task 2 yechimlarida ham kerak. "
                       "Oti — <b>recycling</b>, sifati — <b>recyclable</b>.</p>",
        "examples":    [("Only a third of household plastic is currently recycled.",
                         "Hozirda maishiy plastikning atigi uchdan biri qayta ishlanadi.")],
        "related":     [("renewable", "bir qo‘shimcha (re-) — «qayta»")],
    },
    {
        "word":        "prevent",
        "hanja":       "pre- + vent (kelmoq)",
        "roots":       ["pre-"],
        "pos":         "verb",
        "topic":       "health",
        "level":       3,
        "freq":        3,
        "meaning":     "oldini olmoq — sodir bo‘lishiga yo‘l qo‘ymaslik",
        "collocation": "prevent disease · prevent somebody from doing · preventive measures",
        "note":        "<p>⚠️ Qolipi: <b>prevent somebody FROM doing</b> — ❌ prevent him "
                       "<u>to do</u>. Oti — <b>prevention</b>: <i><b>prevention</b> is better "
                       "than cure</i> (sog‘liq inshosi uchun tayyor fikr).</p>",
        "examples":    [("Regular exercise helps prevent a range of chronic illnesses.",
                         "Muntazam jismoniy mashq bir qator surunkali kasalliklarning oldini olishga yordam beradi.")],
        "synonyms":    [("deter", "deter = qo‘rqitib qaytarish (jazo); prevent = imkoniyatni yo‘qotish")],
    },
    {
        "word":        "suburban",
        "hanja":       "sub- + urban",
        "roots":       ["sub-"],
        "pos":         "adj",
        "topic":       "society",
        "level":       4,
        "freq":        1,
        "meaning":     "shahar atrofi — chekkadagi turar joy hududiga oid",
        "collocation": "suburban areas · move to the suburbs · suburban sprawl",
        "note":        "<p>Uch qatlamni ajratishni biling: <b>urban</b> (shahar) — "
                       "<b>suburban</b> (shahar atrofi) — <b>rural</b> (qishloq). "
                       "Task 1 xaritalari va Task 2 shaharlashuv mavzusida kerak.</p>",
        "examples":    [("Many families move to suburban areas in search of cheaper housing.",
                         "Ko‘p oilalar arzonroq uy-joy izlab shahar atrofiga ko‘chadi.")],
        "antonyms":    [("rural", "suburban = shahar chekkasi; rural = qishloq joy")],
    },
    {
        "word":        "substantial",
        "hanja":       "sub- + stant (turmoq) + -ial",
        "roots":       ["sub-"],
        "pos":         "adj",
        "topic":       "data",
        "level":       5,
        "freq":        3,
        "meaning":     "salmoqli, sezilarli — katta miqdordagi",
        "collocation": "a substantial increase · substantial evidence · substantially higher",
        "note":        "<p>Task 1 da <i>big</i> so‘zining eng yaxshi o‘rinbosari: "
                       "<i>a <b>substantial</b> rise</i>, <i><b>substantially</b> higher</i>. "
                       "⚠️ <b>substantial</b> (katta) ≠ <b>substantive</b> (mazmunli).</p>",
        "examples":    [("There was a substantial increase in energy consumption after 2005.",
                         "2005-yildan keyin energiya iste’molida sezilarli o‘sish kuzatildi.")],
        "synonyms":    [("considerable", "ma’nosi deyarli bir xil — takrorlanmaslik uchun almashtiring")],
        "antonyms":    [("marginal", "substantial = katta; marginal = arzimas")],
    },
    {
        "word":        "intervention",
        "hanja":       "inter- + vent + -ion",
        "roots":       ["inter-", "-ion"],
        "pos":         "noun",
        "topic":       "government",
        "level":       6,
        "freq":        2,
        "meaning":     "aralashuv — hukumat yoki tashkilotning chora ko‘rishi",
        "collocation": "government intervention · early intervention · intervene in",
        "note":        "<p>Task 2 da «davlat aralashuvi kerakmi?» tipidagi savollarda markaziy "
                       "so‘z. Fe’li — <b>intervene (in)</b>.</p>",
        "examples":    [("Early intervention in childhood produces the greatest long-term benefits.",
                         "Bolalikdagi erta aralashuv eng katta uzoq muddatli foyda beradi.")],
        "related":     [("regulation", "intervention = aralashuv harakati; regulation = qoida orqali nazorat")],
    },
    {
        "word":        "transform",
        "hanja":       "trans- + form",
        "roots":       ["trans-"],
        "pos":         "verb",
        "topic":       "science",
        "level":       4,
        "freq":        2,
        "meaning":     "tubdan o‘zgartirmoq — shaklini butunlay almashtirmoq",
        "collocation": "transform the way we work · a complete transformation · transform into",
        "note":        "<p><i>change</i> so‘zining kuchli o‘rinbosari — Task 2 kirish qismida "
                       "ideal: <i>Technology has <b>transformed</b> the way people communicate.</i></p>",
        "examples":    [("The internet has transformed higher education over the past decade.",
                         "Internet so‘nggi o‘n yilda oliy ta’limni tubdan o‘zgartirdi.")],
        "synonyms":    [("alter", "alter = qisman o‘zgartirish; transform = tubdan o‘zgartirish")],
    },
    {
        "word":        "overcrowded",
        "hanja":       "over- + crowd + -ed",
        "roots":       ["over-"],
        "pos":         "adj",
        "topic":       "society",
        "level":       4,
        "freq":        2,
        "meaning":     "haddan tashqari gavjum — sig‘imidan ortiq to‘lgan",
        "collocation": "overcrowded cities · overcrowded classrooms · overcrowding",
        "note":        "<p>Shaharlashuv va ta’lim mavzularida: <i><b>overcrowded</b> "
                       "classrooms</i> — sinf o‘lchami haqidagi savolga tayyor dalil. "
                       "Oti — <b>overcrowding</b>.</p>",
        "examples":    [("Overcrowded public transport discourages people from leaving their cars.",
                         "Haddan tashqari gavjum jamoat transporti odamlarni mashinasidan voz kechishdan qaytaradi.")],
        "related":     [("congestion", "congestion = yo‘l tirbandligi; overcrowding = joyning to‘lib ketishi")],
    },
    {
        "word":        "overlook",
        "hanja":       "over- + look",
        "roots":       ["over-"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        1,
        "meaning":     "e’tibordan chetda qoldirmoq — sezmay o‘tib ketmoq",
        "collocation": "overlook the fact that · an often overlooked factor · easily overlooked",
        "note":        "<p>Qarshi fikrning kamchiligini ko‘rsatishning eng ixcham yo‘li: "
                       "<i>This argument <b>overlooks</b> the cost to rural communities.</i></p>",
        "examples":    [("Such policies overlook the needs of families on low incomes.",
                         "Bunday siyosat kam daromadli oilalarning ehtiyojlarini e’tibordan chetda qoldiradi.")],
        "related":     [("undermine", "overlook = e’tibor bermaslik; undermine = asosini yemirish")],
    },
    {
        "word":        "undermine",
        "hanja":       "under- + mine (qazmoq)",
        "roots":       ["under-"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       6,
        "freq":        2,
        "meaning":     "asosini yemirmoq, kuchsizlantirmoq",
        "collocation": "undermine confidence · undermine the argument · seriously undermined",
        "note":        "<p>«Ostidan qazimoq» — sekin-asta zaiflashtirish. Bahsda juda kuchli: "
                       "<i>Cheap imports <b>undermine</b> local producers.</i></p>",
        "examples":    [("Excessive testing can undermine students’ motivation to learn.",
                         "Haddan ortiq imtihon o‘quvchilarning o‘rganish ishtiyoqini yemirishi mumkin.")],
        "related":     [("overlook", "juftlik: over- va under- qo‘shimchalari")],
    },
    {
        "word":        "underestimate",
        "hanja":       "under- + estimate",
        "roots":       ["under-"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        1,
        "meaning":     "past baholamoq — haqiqiy qiymatidan kam deb hisoblamoq",
        "collocation": "should not be underestimated · widely underestimated",
        "note":        "<p>Tayyor qolip: <i>The importance of early education <b>should not be "
                       "underestimated</b>.</i> — xulosada juda yaxshi ishlaydi.</p>",
        "examples":    [("The environmental cost of air travel is often underestimated.",
                         "Havo transportining ekologik narxi ko‘pincha past baholanadi.")],
        "antonyms":    [("overestimate", "over- = ortiqcha baholash; under- = kam baholash")],
    },
    {
        "word":        "inequality",
        "hanja":       "in- + equal + -ity",
        "roots":       ["un-/in-"],
        "pos":         "noun",
        "topic":       "society",
        "level":       4,
        "freq":        3,
        "meaning":     "tengsizlik — imkoniyat yoki daromaddagi tafovut",
        "collocation": "income inequality · widen inequality · social inequality",
        "note":        "<p>Jamiyat mavzusining markaziy so‘zi: <i>the gap between rich and poor</i> "
                       "ni bitta so‘z bilan aytadi. Sifati — <b>unequal</b>.</p>",
        "examples":    [("Unequal access to the internet has widened educational inequality.",
                         "Internetdan teng bo‘lmagan foydalanish ta’limdagi tengsizlikni kengaytirdi.")],
        "antonyms":    [("equality", "in- qo‘shimchasi ma’noni teskari qiladi")],
    },
    {
        "word":        "inevitable",
        "hanja":       "in- + evitare (qochmoq) + -able",
        "roots":       ["un-/in-", "-able"],
        "pos":         "adj",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "muqarrar — oldini olib bo‘lmaydigan",
        "collocation": "an inevitable consequence · it is inevitable that · inevitably",
        "note":        "<p>Ravishi <b>inevitably</b> — jumla boshida juda foydali: "
                       "<i><b>Inevitably</b>, such measures will meet resistance.</i></p>",
        "examples":    [("Some job losses are an inevitable consequence of automation.",
                         "Ba’zi ish o‘rinlarining yo‘qolishi avtomatlashtirishning muqarrar oqibati.")],
        "synonyms":    [("unavoidable", "ma’nosi bir xil; inevitable akademikroq eshitiladi")],
    },
    {
        "word":        "consumption",
        "hanja":       "con- + sumpt + -ion",
        "roots":       ["-ion"],
        "pos":         "noun",
        "topic":       "data",
        "level":       4,
        "freq":        3,
        "meaning":     "iste’mol — sarflash miqdori",
        "collocation": "energy consumption · consumption per capita · household consumption",
        "note":        "<p><b>Task 1 ning eng ko‘p uchraydigan otlaridan biri.</b> Fe’li — "
                       "<b>consume</b>, iste’molchi — <b>consumer</b>. "
                       "<i>per capita</i> («jon boshiga») bilan juftlanadi.</p>",
        "examples":    [("Energy consumption per capita fell steadily throughout the period.",
                         "Aholi jon boshiga energiya iste’moli davr davomida barqaror kamaydi.")],
        "related":     [("expenditure", "consumption = sarflangan miqdor; expenditure = sarflangan pul")],
    },
    {
        "word":        "affordable",
        "hanja":       "afford + -able",
        "roots":       ["-able"],
        "pos":         "adj",
        "topic":       "economy",
        "level":       4,
        "freq":        2,
        "meaning":     "arzon, ko‘tara oladigan — narxi qo‘ldan keladigan",
        "collocation": "affordable housing · affordable healthcare · make it affordable",
        "note":        "<p><b>affordable housing</b> — shahar va tengsizlik mavzularida tayyor "
                       "birikma. Fe’li: <i>cannot <b>afford</b> to</i> (moliyaviy imkoni yo‘q).</p>",
        "examples":    [("A shortage of affordable housing has forced young people to live with parents.",
                         "Arzon uy-joy tanqisligi yoshlarni ota-onasi bilan yashashga majbur qildi.")],
        "related":     [("accessible", "affordable = narxi ko‘tarsa bo‘ladigan; accessible = "
                                       "yetib borish/foydalanish mumkin bo‘lgan")],
    },
    {
        "word":        "urbanisation",
        "hanja":       "urban + -ise + -ation",
        "roots":       ["-ise/-ify", "-ion"],
        "pos":         "noun",
        "topic":       "society",
        "level":       5,
        "freq":        3,
        "meaning":     "urbanizatsiya — aholining shaharga ko‘chishi",
        "collocation": "rapid urbanisation · the pace of urbanisation · urban sprawl",
        "note":        "<p>Task 2 ning eng ko‘p qaytariladigan mavzularidan biri. Yonidagi "
                       "so‘zlar: <b>urban sprawl</b> (shaharning tartibsiz kengayishi), "
                       "<b>rural depopulation</b> (qishloqning bo‘shashi).</p>",
        "examples":    [("Rapid urbanisation has placed enormous strain on public services.",
                         "Jadal urbanizatsiya jamoat xizmatlariga ulkan yuk tushirdi.")],
        "related":     [("demographic", "urbanisation — demografik o‘zgarishning bir turi")],
    },
    {
        "word":        "justify",
        "hanja":       "just + -ify",
        "roots":       ["-ise/-ify"],
        "pos":         "verb",
        "topic":       "academic",
        "level":       5,
        "freq":        2,
        "meaning":     "asoslamoq, oqlamoq — sababini ko‘rsatib to‘g‘riligini isbotlamoq",
        "collocation": "difficult to justify · justify the cost · justification for",
        "note":        "<p>Bahsda kuchli tuzilma: <i>Such spending is <b>difficult to justify</b> "
                       "when hospitals are underfunded.</i> Oti — <b>justification</b>.</p>",
        "examples":    [("It is hard to justify subsidising an industry that pollutes so heavily.",
                         "Shunchalik ko‘p ifloslantiruvchi tarmoqni subsidiyalashni oqlash qiyin.")],
        "related":     [("advocate", "justify = sababini ko‘rsatish; advocate = yoqlab chiqish")],
    },
]


# The list is already in the order the table should show, so stamp this group's
# `order` decade on it here rather than repeating a number in every dict.
# Decades are allocated in toc_ielts_vocab.txt — keep them unique per file, or
# two groups interleave in the table.
for _i, _word in enumerate(WORDS):
    _word.setdefault("order", 300 + _i)
