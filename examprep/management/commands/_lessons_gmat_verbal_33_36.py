# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — Reading Comprehension, lessons 33 (inference), 34 (function and
structure), 35 (application and tone) and 36 (RC mixed practice).
See toc_gmat_verbal.txt and STYLE_GUIDE_GMAT_VERBAL.md §1.0: two real passages per lesson,
every fact true as written, questions answerable from the passage alone.

TRACK, TOPIC_RC and passage() come from _lessons_gmat_verbal_30_32.py (by path).
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name):
    spec = importlib.util.spec_from_file_location("_gmatv_" + name, os.path.join(_HERE, name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_b1 = _load("_lessons_gmat_verbal_1_12.py")
_rc = _load("_lessons_gmat_verbal_30_32.py")

TRACK = _b1.TRACK
TOPIC_RC = _rc.TOPIC_RC
TIP, WARN, NOTE = _b1.TIP, _b1.WARN, _b1.NOTE
ask, steps, cards = _b1.ask, _b1.steps, _b1.cards
passage = _rc.passage


# ── Passages ─────────────────────────────────────────────────────────────────
P_STINK = [
    "In the hot summer of 1858, the smell rising from the River Thames became so foul that newspapers called it the Great "
    "Stink. For decades London's sewers and drains had emptied straight into the river, which also supplied much of the city's "
    "drinking water. Most doctors at the time believed that diseases such as cholera were spread by bad air, or miasma, so the "
    "stench seemed not merely unpleasant but dangerous. Within weeks, Parliament, whose new building stood beside the river, "
    "approved a plan by the engineer Joseph Bazalgette for a vast system of intercepting sewers that would carry the city's waste "
    "far downstream, east of London.",
    "The miasma theory was wrong. Four years earlier, the physician John Snow had traced an outbreak of cholera in Soho to a "
    "single contaminated water pump on Broad Street, and he argued that the disease spread through water, not air. His view won "
    "few converts at first. Yet Bazalgette's sewers, built to remove a smell, also removed the contamination that actually "
    "spread the disease.",
    "The results were striking. When cholera returned to London in 1866, the deaths were concentrated in the East End, in an "
    "area whose water was drawn from a polluted stretch of river not yet protected by the completed system. After that outbreak, "
    "cholera never again struck London on a large scale. A project justified by a false theory had delivered exactly what the "
    "true theory would have recommended.",
]

P_TULIP = [
    "The Dutch tulip mania of the 1630s is one of the most famous stories in economics. In the version popularised by the "
    "Scottish writer Charles Mackay in 1841, prices for rare tulip bulbs rose to absurd heights — a single bulb was said to be "
    "worth a house — before collapsing in February 1637 and ruining thousands of ordinary people across the Dutch Republic. The "
    "episode has been cited ever since as the first great speculative bubble and as a warning about the madness of crowds.",
    "Historians who have gone back to the archives tell a different story. The prices themselves were real: some rare bulbs did "
    "change hands for very large sums. But in her 2007 study, the historian Anne Goldgar found little evidence of widespread "
    "ruin. The trade was concentrated among a fairly small group of merchants and skilled craftsmen, many contracts made in the "
    "final weeks were never honoured, and she could identify almost no one who went bankrupt because of tulips. Much of the "
    "moralising tone of the popular account, she argues, came from pamphlets published after the crash, which were themselves "
    "a form of entertainment and religious instruction.",
    "None of this means that nothing happened in 1637. Prices did collapse, and people did lose money and trust. But the gap "
    "between the evidence and the legend is a reminder that a story told often enough can become more vivid than the events it "
    "describes.",
]

P_WEGENER = [
    "In 1912 the German scientist Alfred Wegener proposed that the continents had once been joined in a single landmass and had "
    "since drifted apart. His evidence was varied. The coastlines of South America and Africa fit together like pieces of a "
    "puzzle; fossils of the same ancient reptile, Mesosaurus, are found on both sides of the South Atlantic; and rock formations "
    "on separate continents match in age and type. To Wegener, these coincidences were too many to be accidents.",
    "Most geologists rejected the idea for decades. Their objection was not chiefly to the evidence, which many admitted was "
    "suggestive, but to the absence of a mechanism: Wegener could not explain what force could push entire continents through "
    "the solid rock of the ocean floor, and the forces he proposed were shown to be far too weak. A theory that described what "
    "had happened without explaining how seemed to them less a scientific claim than a guess.",
    "The missing mechanism came from the sea floor itself. In the 1950s and 1960s, surveys revealed long ridges running through "
    "the oceans and, on either side of them, matching stripes of rock that recorded reversals in the Earth's magnetic field. The "
    "pattern showed that new ocean floor was forming at the ridges and spreading outward. Within a few years, the theory of plate "
    "tectonics, which incorporated Wegener's central insight, had become the foundation of modern geology. Wegener, who died on "
    "an expedition to Greenland in 1930, did not live to see it.",
]

P_ANDON = [
    "For much of the twentieth century, car factories treated the assembly line as something that must never stop. A stopped "
    "line meant idle workers and lost output, so defects were usually passed along and fixed at the end, if at all. Toyota took "
    "the opposite view. In its factories, any worker who noticed a problem could pull a cord, known as an andon, that called a "
    "team leader and, if the problem could not be fixed quickly, halted the line. Stopping the line was costly, but it forced "
    "problems to be solved where they began rather than multiplied further down the line.",
    "The most striking test of the approach came in California. In 1982 General Motors closed its plant in Fremont, which had a "
    "reputation for some of the worst quality and labour relations in the company. Two years later the plant reopened as NUMMI, "
    "a joint venture between GM and Toyota run on Toyota's methods — and it rehired many of the same workers. Within a short "
    "time, the plant's quality was among the best in GM's system.",
    "The lesson that many observers drew was not that the Fremont workers had changed, but that the system around them had. "
    "Copying that system proved harder than admiring it: techniques such as the andon cord depended on trust between managers "
    "and workers, and plants that installed the cords without building that trust often found that nobody pulled them.",
]

P_KHWARIZMI = [
    "In the early ninth century, Muhammad ibn Musa al-Khwarizmi, a scholar from Khorezm in Central Asia, worked in Baghdad at "
    "the House of Wisdom, the great centre of learning supported by the Abbasid caliphs. Two of his books changed mathematics. "
    "The first, usually known by a short form of its title, al-Jabr, presented systematic methods for solving linear and "
    "quadratic equations. Its purpose was practical: al-Khwarizmi wrote that he had confined himself to what people constantly "
    "need in matters such as inheritance, trade, land measurement and lawsuits. The word algebra comes from al-jabr, one of the "
    "operations the book describes.",
    "The second book explained the Indian system of writing numbers with nine digits and a zero, in which the value of a digit "
    "depends on its place. The Arabic original is lost, but Latin translations made in the twelfth century circulated in Europe, "
    "where the method gradually replaced Roman numerals for calculation. Medieval Latin writers rendered the author's name as "
    "Algoritmi, and from that form came the word algorithm.",
    "It would be easy to treat al-Khwarizmi as a lone genius. Yet his work drew on Indian, Greek and Babylonian traditions, and "
    "its influence depended on translators, copyists and merchants across several centuries. What makes his achievement "
    "remarkable is less that he invented everything in his books than that he organised existing knowledge so clearly that "
    "others could use it — and his name, transformed, still marks the step-by-step methods that every computer follows.",
]

P_DEFAULTS = [
    "When a choice comes with a pre-selected option, most people keep it. Economists call this the default effect, and its size "
    "can be startling. In a study published in 2003, Eric Johnson and Daniel Goldstein compared consent to organ donation in "
    "European countries. In Germany, where citizens had to sign up to become donors, about 12 percent had consented; in "
    "neighbouring Austria, where citizens were donors unless they opted out, the figure was above 99 percent. The two countries "
    "are similar in culture and wealth; what differed was the form people faced.",
    "Defaults matter in finance too. When some American employers began enrolling new workers in retirement savings plans "
    "automatically, letting them opt out if they wished, participation rose sharply compared with plans that required workers "
    "to sign up. Many workers who would never have joined on their own stayed in, often at whatever contribution rate had been "
    "pre-set.",
    "The effect is easy to explain and hard to escape. Changing a default takes effort, a default can look like a "
    "recommendation, and keeping it feels safer than choosing. For anyone who designs forms — governments, banks, employers — "
    "the lesson is uncomfortable but clear: there is no neutral design. Every form has some default, even if it is only the "
    "option listed first, and whoever chooses it is shaping decisions, whether or not they intend to.",
]

P_TEA = [
    "For two centuries Britain's growing appetite for tea depended on a single supplier: China, which guarded both its tea "
    "plants and the knowledge of how to process them. In 1848 the East India Company sent the Scottish botanist Robert Fortune "
    "into China's interior to change that. Dressed in local clothing and travelling with Chinese guides, Fortune visited "
    "tea-growing districts, collected thousands of seeds and young plants, and persuaded experienced tea workers to travel to India.",
    "Moving living plants across oceans had long been nearly impossible; most died on the voyage. Fortune relied on a recent "
    "invention, the Wardian case, a sealed glass box in which plants could survive for months in their own moist air. Many of "
    "his shipments reached India alive, and with them came the practical knowledge of the workers he had recruited. Among other "
    "things, Fortune's travels showed that green and black tea came from the same plant, processed in different ways — a fact "
    "that had been widely misunderstood in Britain.",
    "The tea industry of British India, which this transfer helped to build, eventually broke China's dominance of the world "
    "tea trade. Fortune's journey is often told as an adventure story, but it was also an act of industrial espionage on behalf "
    "of a commercial company, and its consequences for China's economy were lasting.",
]

P_BORLAUG = [
    "In the 1940s and 1950s, the American plant scientist Norman Borlaug worked in Mexico to breed wheat that resisted disease. "
    "His most important varieties were semi-dwarf: shorter, sturdier plants that could carry heavy heads of grain without "
    "falling over. Taller varieties given large amounts of fertiliser grew so heavy that they collapsed before harvest; the "
    "semi-dwarfs turned fertiliser into grain instead.",
    "In the mid-1960s, with famine feared in South Asia, India and Pakistan imported large quantities of Borlaug's seed. "
    "Combined with irrigation and fertiliser, the new wheat raised yields dramatically, and within a few years both countries "
    "were producing far more grain than before. Similar high-yielding rice varieties spread through Asia in the same period. The "
    "changes became known as the Green Revolution, and in 1970 Borlaug received the Nobel Peace Prize.",
    "The Green Revolution's critics do not dispute that it produced more food. Their concern is with how it did so. The new "
    "varieties delivered their gains only with plenty of water and fertiliser, which favoured farmers who could afford them and "
    "placed heavy demands on groundwater and soil. Defenders reply that without the higher yields far more land would have had "
    "to be cleared to feed growing populations. Both sides can point to evidence; the argument is now less about whether the "
    "Green Revolution worked than about what a second one should look like.",
]


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 33 — inference in RC
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 33: Inference in Reading Comprehension",
    "summary": "RCʼdagi xulosa savollari: matnda toʻgʻridan-toʻgʻri yozilmagan, lekin undan albatta kelib chiqadigan fikrni topish — bir qadam, ikki qadam emas.",
    "order": 33,
    "blocks": [
        {"rich_text": (
            "<h2>Bir qadam narida</h2>"
            "<p>RCʼdagi inference savoli — <i>It can be inferred…</i>, <i>The passage suggests…</i>, <i>The author implies…</i> — "
            "matnda yozilmagan narsani soʻraydi. Lekin bu «taxmin qiling» degani emas. Toʻgʻri javob matndan <mark>bir qadam</mark> "
            "narida turadi: ikki faktni birlashtirsangiz yoki gapni boshqa tomondan oʻqisangiz, u <b>albatta</b> chiqadi.</p>"
            "<p>22-darsdagi CR inference qoidasi shu yerda ham ishlaydi: eng ehtiyotkor, eng tor variant koʻpincha gʻolib.</p>"
            '<span class="sr-time">⏱ Inference — ~1–1.5 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>1.</strong> Savol qaysi mavzu haqida? Xarita bilan kerakli abzasni toping.</p>",
                "<p><strong>2.</strong> Oʻsha joyni qayta oʻqing va <b>ikki faktni</b> birlashtiring: «A boʻldi; B boʻldi → demak…»</p>",
                "<p><strong>3.</strong> Har bir variantga: «Matn rost boʻlsa, bu yolgʻon boʻlishi mumkinmi?» Mumkin boʻlsa — chiqarib tashlang.</p>",
                "<p><strong>4.</strong> Ikki-uch qadamli «mantiqiy» hikoya qurishga majbur qilgan variant — tuzoq.</p>",
            ])
        )},
        passage("1-matn: Buyuk sasish (Great Stink)", P_STINK),
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            "<p>Savol: 1866-yilgi epidemiya haqida nima xulosa qilish mumkin? Fakt 1: oʻlimlar ifloslangan suv olingan, tizim hali himoya "
            "qilmagan hududda toʻplangan. Fakt 2 (2-abzas): Snow kasallik suv orqali tarqaladi degan. Birlashtiramiz: <mark>1866-yil "
            "epidemiyasi Snowning nazariyasiga mos keladi</mark>. Bu bir qadam. «1866-yilda 1854-yildagidan koʻp odam oʻldi» esa — "
            "matnda hech qayerda yoʻq, demak xulosa ham emas.</p>"
            + TIP.format("Inference variantida yangi raqam, yangi ism yoki yangi taqqoslash paydo boʻlsa — ehtiyot boʻling: matn uni bermagan boʻlsa, javob ham emas.")
        )},
        ask("It can be inferred from the passage above that Parliament approved Bazalgette's plan quickly at least in part because", [
            (True, "the smell from the river was thought to be a danger to health and not merely a nuisance", "miasma nazariyasi: hid xavfli deb hisoblangan."),
            (False, "John Snow had persuaded its members that cholera spread through water", "Snowning fikri «few converts» — qabul qilinmagan."),
            (False, "an outbreak of cholera had begun among its members", "aytilmagan."),
            (False, "Bazalgette's plan was cheaper than any alternative", "narx aytilmagan."),
            (False, "the river no longer supplied drinking water to the city", "matnga zid — ichimlik suvi ham daryodan."),
        ], "Matn sababni toʻgʻridan-toʻgʻri aytmaydi, lekin «dangerous» va «within weeks» ni birlashtirsak, xulosa chiqadi."),
        ask("The passage above suggests that, at the time Bazalgette's plan was approved, most doctors", [
            (True, "did not accept Snow's explanation of how cholera spread", "koʻpchilik miasmaga ishongan; Snowning fikri qabul qilinmagan."),
            (False, "had studied the outbreak on Broad Street themselves", "aytilmagan."),
            (False, "opposed Bazalgette's plan for intercepting sewers", "aksincha, ularning nazariyasi rejani qoʻllaydi."),
            (False, "believed that cholera had disappeared from London", "aytilmagan."),
            (False, "worked for the companies that supplied London's water", "aytilmagan."),
        ], "«Most doctors believed miasma» + «few converts» → Snowni qabul qilmagan."),
        ask("Which of the following can be inferred about the cholera outbreak of 1866, as it is described in the passage above?", [
            (True, "Its pattern was consistent with Snow's view of how cholera spreads.", "oʻlimlar ifloslangan suv olingan joyda — suv nazariyasiga mos."),
            (False, "It killed more people than the outbreak of 1854.", "solishtirish yoʻq."),
            (False, "It began in the same part of Soho as the outbreak of 1854.", "East Endʼda toʻplangan."),
            (False, "It showed that Bazalgette's sewers had failed.", "himoyalanmagan hududda — tizim tugallangan joyda emas."),
            (False, "It persuaded most doctors that the miasma theory was correct.", "aytilmagan va mantiqqa zid."),
        ], "Ikki abzasni birlashtirish — RC inferenceʼning eng koʻp uchraydigan shakli."),
        passage("2-matn: lola isitmasi", P_TULIP),
        ask("It can be inferred from the passage above that Mackay's account of the tulip mania", [
            (True, "drew partly on material that, according to Goldgar, was written to entertain and instruct", "«moralising tone of the popular account… came from pamphlets»."),
            (False, "was based on a careful study of Dutch bankruptcy records", "aynan bankrotlik yozuvlari uning hikoyasini tasdiqlamaydi."),
            (False, "was the first written description of the tulip trade", "pamfletlar undan oldin, 1637-yildan keyin chop etilgan."),
            (False, "denied that tulip prices had ever been high", "u narxlarni «absurd heights» deb tasvirlagan."),
            (False, "was written in the Dutch Republic shortly after 1637", "1841-yil, shotlandiyalik yozuvchi."),
        ], "«The popular account» — Mackayʼning versiyasi. Pamfletlar unga ohang bergan."),
        ask("Which of the following can be inferred from the passage above?", [
            (True, "Some people who agreed to buy tulip bulbs early in 1637 never paid for them.", "«many contracts made in the final weeks were never honoured»."),
            (False, "No one lost any money when tulip prices collapsed.", "«people did lose money» — zid."),
            (False, "Most citizens of the Dutch Republic traded in tulips during the 1630s.", "«fairly small group» — zid."),
            (False, "Goldgar found that tulip prices never rose above ordinary levels.", "«the prices themselves were real»."),
            (False, "Tulip mania caused more bankruptcies than any other event of the 1630s.", "aytilmagan."),
        ], "Kontrakt bajarilmagan → kimdir toʻlamagan. Bir qadam."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Ikki qadam</b> — «hukumat qoʻrqdi → demak shifokorlar…» kabi uzun zanjir. <b>Yangi maʼlumot</b> — matnda yoʻq "
                          "raqam yoki taqqoslash. <b>Juda kuchli</b> — «no one lost money», «most citizens». <b>Teskari</b> — matndagi faktning qarshisi.")
            + NOTE.format("Ikkala matn ham bir xil saboq beradi: mashhur hikoya va dalil har doim ham mos kelmaydi. RC savollari aynan shu "
                          "farqni koʻrishni tekshiradi — kim nima deydi (Mackay, Goldgar, muallif) va qaysi dalil bilan.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("it can be inferred", "xulosa qilish mumkin"), ("suggests", "ishora qiladi"), ("implies", "nazarda tutadi"),
                     ("miasma", "«yomon havo» nazariyasi"), ("honour a contract", "shartnomani bajarmoq"), ("contamination", "ifloslanish")])
            + "<h3>Xulosa</h3><ul><li>Inference — matndan bir qadam.</li><li>Ikki faktni birlashtiring.</li>"
            "<li>«Yolgʻon boʻlishi mumkinmi?» testi.</li><li>Kim gapirayotganini kuzating: muallifmi, tarixchimi, mashhur hikoyami.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 34 — function and structure
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 34: Function and Structure — Why the Author Says It",
    "summary": "Funksiya va tuzilish savollari: muallif biror misolni nima uchun keltirgan, abzas nima vazifani bajaradi va matn qanday tartiblangan.",
    "order": 34,
    "blocks": [
        {"rich_text": (
            "<h2>Nima emas — nima uchun</h2>"
            "<p>Funksiya savoli tafsilotning <b>mazmunini</b> emas, uning <b>vazifasini</b> soʻraydi: «<i>The author mentions X primarily in "
            "order to…</i>», «<i>The second paragraph serves primarily to…</i>». Tuzilish savoli esa butun matnning skeletini: "
            "«<i>Which of the following best describes the organisation of the passage?</i>»</p>"
            "<p>Bu savollar uchun oʻqish xaritasi — tayyor javob. Har bir abzasga qoʻygan belgingiz («dalil», «rad etish sababi», "
            "«yechim») aynan shu savollarga kerak.</p>"
            '<span class="sr-time">⏱ Funksiya savoli — ~1 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>1.</strong> X ni matnda toping va <b>oldingi gapni</b> oʻqing — koʻpincha X uning daʼvosiga misol yoki dalil.</p>",
                "<p><strong>2.</strong> Savol: «X boʻlmasa, muallifning qaysi fikri zaiflashadi?» — oʻsha fikr X ning vazifasi.</p>",
                "<p><strong>3.</strong> Variantlardagi <b>feʼlga</b> qarang: <i>illustrate, support, explain, contrast, qualify</i>. "
                "Toʻgʻri feʼl + toʻgʻri obyekt kerak.</p>",
                "<p><strong>4. Tuzilish:</strong> abzas belgilaringizni ketma-ket ayting: «nazariya → rad etildi → isbotlandi». "
                "Variant shu tartibni aynan takrorlashi kerak — bitta qism ortiqcha yoki kam boʻlsa, notoʻgʻri.</p>",
            ])
        )},
        passage("1-matn: kontinentlar siljishi", P_WEGENER),
        {"rich_text": (
            "<h3>Ishlangan namuna: xarita → tuzilish</h3>"
            "<p><b>1-abzas:</b> nazariya + dalillar. <b>2-abzas:</b> nima uchun rad etildi (mexanizm yoʻq). <b>3-abzas:</b> mexanizm topildi → qabul qilindi.</p>"
            "<p>Tuzilish bir jumlada: <mark>nazariya taklif qilinadi, rad etilish sababi tushuntiriladi, keyin qabul qilinishiga olib kelgan "
            "kashfiyot keltiriladi</mark>. Mesosaurus esa 1-abzasdagi «his evidence was varied» gapining misollaridan biri — uning vazifasi shu.</p>"
            + TIP.format("Funksiya savolida X haqidagi <b>rost</b> gap koʻpincha tuzoq boʻladi: «Mesosaurus — qadimgi sudralib yuruvchi» rost, "
                         "lekin savol nima uchun eslatilganini soʻraydi.")
        )},
        ask("The author of the passage above mentions Mesosaurus primarily in order to", [
            (True, "give an example of the evidence Wegener offered for his theory", "«His evidence was varied» — Mesosaurus shu dalillardan biri."),
            (False, "explain the mechanism that moves the continents", "mexanizm 3-abzasda — dengiz tubi."),
            (False, "illustrate how reversals of the Earth's magnetic field are recorded", "bu 3-abzasdagi tosh chiziqlari."),
            (False, "suggest that Wegener's evidence was weaker than he believed", "muallif dalilni zaif demaydi."),
            (False, "show that geologists accepted the fossil evidence immediately", "geologlar nazariyani oʻnlab yillar rad etgan."),
        ], "Misolning vazifasi — u xizmat qilgan daʼvo."),
        ask("The second paragraph of the passage above serves primarily to", [
            (True, "explain why most geologists did not accept Wegener's theory", "mexanizm yoʻqligi — asosiy eʼtiroz."),
            (False, "present new evidence in support of Wegener's theory", "yangi dalil yoʻq."),
            (False, "describe how new ocean floor forms and spreads", "bu 3-abzasda."),
            (False, "argue that Wegener's evidence had been fabricated", "aksincha — «suggestive» deb tan olingan."),
            (False, "compare Wegener with the scientists who later confirmed his idea", "taqqoslash yoʻq."),
        ], "Abzasning vazifasi = xaritadagi belgisi: «rad etish sababi»."),
        ask("Which of the following best describes the organisation of the passage above?", [
            (True, "A theory is described, the reason for its rejection is explained, and the discovery that led to its acceptance is presented.", "uch abzas — uch qism."),
            (False, "Two competing theories are compared, and one is shown to be false.", "ikkinchi nazariya yoʻq."),
            (False, "A problem is described, and several possible solutions are evaluated.", "yechimlar baholanmagan."),
            (False, "A discovery is described, and its effects on later research are criticised.", "tanqid yoʻq."),
            (False, "A scientist's life is recounted from his early career to his death.", "matn biografiya emas — nazariya haqida."),
        ], "Tuzilish varianti abzaslar tartibini aniq takrorlashi kerak."),
        passage("2-matn: andon arqoni", P_ANDON),
        ask("The first paragraph of the passage above serves primarily to", [
            (True, "contrast two approaches to dealing with defects on an assembly line", "anʼanaviy usul va Toyota usuli."),
            (False, "describe the history of the plant in Fremont", "bu 2-abzasda."),
            (False, "argue that stopping the line is always cheaper than fixing defects later", "juda kuchli — matn «costly» deydi."),
            (False, "explain why General Motors closed the Fremont plant", "bu 2-abzasda va qisqa."),
            (False, "criticise Toyota for the cost of stopping its lines", "muallif tanqid qilmaydi."),
        ], "«Toyota took the opposite view» — qarama-qarshilik belgisi."),
        ask("The author of the passage above mentions that NUMMI rehired many of the same workers most likely in order to", [
            (True, "suggest that the improvement in quality came from the system rather than from a change of workforce", "3-abzas: «not that the workers had changed, but that the system… had»."),
            (False, "show that Toyota preferred to hire experienced workers", "Toyotaning afzalligi haqida gap yoʻq."),
            (False, "explain why labour relations at Fremont had been poor", "sabab aytilmagan."),
            (False, "illustrate how difficult it was to copy Toyota's methods", "bu 3-abzasdagi boshqa fikr."),
            (False, "emphasise how expensive it was to reopen the plant", "narx aytilmagan."),
        ], "Tafsilotning vazifasini keyingi xulosa ochib beradi: ishchilar bir xil → farq tizimda."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Rost, lekin vazifa emas</b> — X haqida toʻgʻri tasvir. <b>Boshqa abzasning vazifasi</b> — 3-abzasdagi fikrni "
                          "2-abzasga bogʻlash. <b>Notoʻgʻri feʼl</b> — muallif tasvirlaydi, variant esa «criticise» yoki «argue» deydi. "
                          "<b>Ortiqcha qism</b> — tuzilish variantida matnda yoʻq bosqich.")
            + NOTE.format("Bizning maktablarda matn odatda «nima deyilgan?» savoli bilan oʻqiladi. GMAT esa «<b>nima uchun</b> deyilgan?» deb soʻraydi. "
                          "Har abzasdan keyin «bu nima uchun shu yerda?» deb soʻrash — bir haftalik odat, butun RC uchun foyda.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("primarily in order to", "asosan … uchun"), ("serves to", "… vazifasini bajaradi"), ("organisation", "tuzilish, tartib"),
                     ("mechanism", "mexanizm"), ("assembly line", "yigʻuv konveyeri"), ("joint venture", "qoʻshma korxona"), ("illustrate", "misol bilan koʻrsatmoq")])
            + "<h3>Xulosa</h3><ul><li>Funksiya — nima uchun, mazmun emas.</li><li>X dan oldingi gap koʻpincha javob.</li>"
            "<li>Feʼl va obyekt ikkalasi toʻgʻri boʻlsin.</li><li>Tuzilish = xarita belgilari ketma-ketligi.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 35 — application and tone
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 35: Application, Tone and the Author's Attitude",
    "summary": "Qoʻllash savollari (matndagi tamoyilga oʻxshash yangi holat) va ohang savollari (muallif nimaga qanday munosabatda).",
    "order": 35,
    "blocks": [
        {"rich_text": (
            "<h2>Matndan tashqariga — ehtiyotkorlik bilan</h2>"
            "<p><b>Qoʻllash</b> (application) savoli matndagi gʻoyani yangi holatga koʻchiradi: «<i>Which of the following is most similar "
            "to…?</i>», «<i>…most closely illustrates…?</i>». <b>Ohang</b> (tone) savoli muallifning munosabatini soʻraydi: "
            "«<i>The author's attitude toward X can best be described as…</i>».</p>"
            "<p>Ikkalasida ham kalit — <mark>abstraksiya</mark>: matndagi aniq hikoyadan umumiy tamoyilni ajratib olish va uni boshqa "
            "holatda tanib olish.</p>"
            '<span class="sr-time">⏱ Qoʻllash / ohang — ~1–1.5 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>Qoʻllash 1.</strong> Matndagi holatni <b>mavzusiz</b> ayting: «tayyor tanlov qoldiriladi, chunki uni oʻzgartirish kuch talab qiladi».</p>",
                "<p><strong>Qoʻllash 2.</strong> Har bir variantni ham mavzusiz ayting va solishtiring. Mavzusi oʻxshash (bank, soliq), lekin "
                "tamoyili boshqa variant — eng koʻp uchraydigan tuzoq.</p>",
                "<p><strong>Ohang 1.</strong> Muallifning <b>baho soʻzlarini</b> yigʻing: <i>remarkable, startling, uncomfortable, it would be easy to…</i></p>",
                "<p><strong>Ohang 2.</strong> GMAT mualliflari kamdan-kam keskin: ohang odatda <b>mulohazali</b> — «admiring but measured», "
                "«critical but fair». «Hostile», «worshipful» kabi oʻta kuchli soʻzlar deyarli har doim tuzoq.</p>",
            ])
        )},
        passage("1-matn: al-Xorazmiy", P_KHWARIZMI),
        {"rich_text": (
            "<h3>Ishlangan namuna: ohang</h3>"
            "<p>Baho soʻzlari: «changed mathematics», «remarkable» — hurmat. Lekin: «It would be easy to treat al-Khwarizmi as a lone genius. Yet…» "
            "— muallif mubolagʻadan saqlanadi. Ohang: <mark>hayrat, lekin oʻlchovli</mark>. Ikkala qism ham javobda boʻlishi kerak.</p>"
            + TIP.format("Al-Xorazmiy haqida biz koʻp narsa bilamiz va undan faxrlanamiz. Ohang savolida esa <b>bizning</b> munosabatimiz emas, "
                         "<b>muallifning</b> munosabati soʻraladi — va bu muallif ataylab oʻlchovli yozgan.")
        )},
        ask("The author's attitude toward al-Khwarizmi's achievement, as expressed in the passage above, can best be described as", [
            (True, "admiring, but careful not to exaggerate it", "«remarkable» + «it would be easy to treat… as a lone genius. Yet…»."),
            (False, "sceptical of its importance", "«changed mathematics» — muallif ahamiyatini tan oladi."),
            (False, "uncritically enthusiastic", "muallif «lone genius» qarashini aynan tanqid qiladi."),
            (False, "indifferent", "baho soʻzlari bor — befarq emas."),
            (False, "openly hostile", "hech qanday dushmanlik yoʻq."),
        ], "Ohang = baho soʻzlari + cheklovlar. Ikkalasini ham hisobga oling."),
        ask("According to the last paragraph of the passage above, which of the following would be most similar to al-Khwarizmi's achievement?", [
            (True, "A teacher who writes a clear textbook that organises existing methods so that many students can use them", "«organised existing knowledge so clearly that others could use it»."),
            (False, "A scientist who makes a discovery that no one before had imagined", "muallif aynan «hammasini oʻzi ixtiro qilgan» qarashini rad etadi."),
            (False, "A merchant who becomes rich by trading in rare books", "mavzu oʻxshash, tamoyil boshqa."),
            (False, "A translator who renders a famous novel into another language", "tarjimonlar tarqatgan — lekin yutuq al-Xorazmiyniki."),
            (False, "A ruler who builds a great library and pays scholars to work in it", "bu Abbosiylar roli, al-Xorazmiyniki emas."),
        ], "Tamoyil: mavjud bilimni boshqalar foydalana oladigan qilib tartiblash."),
        ask("The author of the passage above mentions translators, copyists and merchants primarily in order to", [
            (True, "show that al-Khwarizmi's influence depended on many people besides himself", "«lone genius» qarashiga qarshi dalil."),
            (False, "explain how the word algebra entered European languages", "bu 1-abzasda."),
            (False, "suggest that al-Khwarizmi's books contained many errors", "aytilmagan."),
            (False, "describe daily life in ninth-century Baghdad", "aytilmagan."),
            (False, "argue that the Latin translations were more important than the originals", "solishtirish yoʻq."),
        ], "Funksiya: oldingi gap («lone genius… Yet») — ular shu fikrga dalil."),
        passage("2-matn: standart tanlov effekti", P_DEFAULTS),
        ask("Which of the following situations most closely illustrates the default effect as it is described in the passage above?", [
            (True, "A phone company sends paper bills unless customers ask for email, and most customers keep paper bills although switching takes one click.",
             "tayyor tanlov + oʻzgartirish oson boʻlsa ham qoldirilgan — aynan tamoyil."),
            (False, "A bank offers a higher interest rate, and many customers move their savings to it.", "bu ragʻbat, standart tanlov emas."),
            (False, "A government bans the sale of a product, and its sales fall to zero.", "taqiq — tanlov yoʻq."),
            (False, "A shop lowers its prices, and its sales rise.", "narx — boshqa tamoyil."),
            (False, "A company publishes its salaries, and some employees ask for a raise.", "maʼlumot — standart emas."),
        ], "Mavzu emas, tamoyil: oldindan belgilangan variant + uni oʻzgartirmaslik."),
        ask("In the passage above, the author's attitude toward the idea that a form could be designed neutrally is best described as", [
            (True, "firm rejection", "«there is no neutral design»."),
            (False, "cautious acceptance", "muallif uni qabul qilmaydi."),
            (False, "enthusiastic support", "teskari."),
            (False, "uncertainty, because the evidence is mixed", "muallif «clear» deydi."),
            (False, "indifference", "muallif bu haqda aniq fikr bildiradi."),
        ], "Bu yerda muallif haqiqatan keskin — «uncomfortable but clear». Ohang har doim yumshoq emas; matnga qarang."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Mavzu oʻxshash, tamoyil boshqa</b> — bank haqidagi variant, lekin ragʻbat haqida. <b>Oʻta kuchli ohang</b> — "
                          "«hostile», «worshipful». <b>Faqat yarim ohang</b> — «admiring» toʻgʻri, lekin cheklovsiz toʻliq emas. "
                          "<b>Bizning munosabatimiz</b> — muallifniki oʻrniga.")
            + NOTE.format("Ohang savollarida bitta istisno bor: muallif aniq va keskin gapirsa («there is no neutral design»), keskin variant "
                          "toʻgʻri boʻladi. Qoida — «yumshoq» emas, «<b>matndagi kuchga mos</b>».")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("most closely illustrates", "eng yaxshi misol boʻladi"), ("attitude", "munosabat"), ("tone", "ohang"),
                     ("default", "standart (oldindan belgilangan) tanlov"), ("opt out", "voz kechmoq"), ("lone genius", "yolgʻiz daho"),
                     ("measured", "oʻlchovli, vazmin")])
            + "<h3>Xulosa</h3><ul><li>Qoʻllash: tamoyilni mavzusiz ayting va solishtiring.</li><li>Ohang: baho soʻzlari + cheklovlar.</li>"
            "<li>Javobning kuchi matnning kuchiga mos boʻlsin.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 36 — RC mixed practice
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 36: Reading Comprehension — Mixed Practice",
    "summary": "Reading Comprehension boʻyicha aralash mashq: ikki matn, oltita savol — asosiy maqsad, tafsilot, funksiya, xulosa, qoʻllash va tuzilish.",
    "order": 36,
    "blocks": [
        {"rich_text": (
            "<h2>Imtihondagidek: matn va savollar toʻplami</h2>"
            "<p>Ikki matn, har biriga uchta savol — imtihondagi RC toʻplamiga yaqin. Har bir matnni bir marta, xarita bilan oʻqing; "
            "savollarda savol turini aniqlang va kerakli abzasga qayting.</p>"
            '<span class="sr-time">⏱ Maqsad: har matn uchun ~3 daqiqa oʻqish + 3–4 daqiqa savollar</span>'
        )},
        {"rich_text": (
            "<h3>Eslatma: RC savol turlari</h3>"
            + steps([
                "<p><strong>Asosiy fikr / maqsad (31):</strong> bir jumla; tor, keng, kuchli — chiqarib tashlang.</p>",
                "<p><strong>Tafsilot (32):</strong> kalit soʻz → gap → parafraz.</p>",
                "<p><strong>Xulosa (33):</strong> bir qadam; «yolgʻon boʻlishi mumkinmi?»</p>",
                "<p><strong>Funksiya / tuzilish (34):</strong> nima uchun — oldingi gap; xarita belgilari.</p>",
                "<p><strong>Qoʻllash / ohang (35):</strong> mavzusiz tamoyil; baho soʻzlari.</p>",
            ])
            + TIP.format("Xato qilgan savolni dars raqami bilan belgilang (31–35) — bir xil raqam ikki marta chiqsa, oʻsha darsga qayting.")
        )},
        passage("1-matn: Robert Fortune va choy", P_TEA),
        ask("The primary purpose of the passage above is to", [
            (True, "describe how tea plants and knowledge were taken out of China and the lasting effects of that transfer", "uchala abzasni qamraydi."),
            (False, "explain how the Wardian case was invented", "juda tor — faqat 2-abzasdagi bir tafsilot."),
            (False, "argue that Fortune's journey should no longer be remembered", "muallif uni boshqacha koʻrishni taklif qiladi, unutishni emas."),
            (False, "compare the quality of Chinese and Indian tea", "taqqoslash yoʻq."),
            (False, "describe the daily lives of Chinese tea workers", "ular faqat eslatilgan."),
        ], "Asosiy maqsad — butun matn: voqea + oqibat."),
        ask("According to the passage above, the Wardian case was important to Fortune's work because it", [
            (True, "allowed living plants to survive long sea voyages", "2-abzas: «plants could survive for months in their own moist air»."),
            (False, "hid the plants from Chinese officials", "aytilmagan."),
            (False, "was used to process green and black tea", "aytilmagan."),
            (False, "had been invented by Fortune himself", "«a recent invention» — muallifi aytilmagan."),
            (False, "allowed seeds to be stored for many years", "«for months» va tirik oʻsimliklar haqida."),
        ], "Tafsilot — qatorning parafrazi."),
        ask("The last sentence of the passage above serves primarily to", [
            (True, "add a critical perspective to the popular view of Fortune's journey", "«often told as an adventure story, but… industrial espionage»."),
            (False, "summarise the evidence that Fortune was a skilled botanist", "baho emas, malaka haqida emas."),
            (False, "deny that Fortune's journey ever took place", "voqea rad etilmagan."),
            (False, "explain why the Wardian case was needed", "bu 2-abzasda."),
            (False, "praise the business methods of the East India Company", "aksincha, tanqidiy."),
        ], "«Often told as… but» — muallif mashhur qarashga boshqa nuqtai nazar qoʻshadi."),
        passage("2-matn: Yashil inqilob", P_BORLAUG),
        ask("It can be inferred from the passage above that Borlaug's semi-dwarf wheat was most valuable to farmers who", [
            (True, "could supply their crops with plenty of water and fertiliser", "«delivered their gains only with plenty of water and fertiliser»."),
            (False, "farmed in dry regions without irrigation", "teskari."),
            (False, "wanted to stop using fertiliser altogether", "teskari — oʻgʻitni donga aylantirgan."),
            (False, "grew rice rather than wheat", "guruch navlari boshqa."),
            (False, "lived only in Mexico", "Hindiston va Pokiston ham."),
        ], "Ikki faktni birlashtiramiz: oʻgʻit + suv kerak → ularni bera oladiganlar yutadi."),
        ask("Which of the following, if true, would most support the defenders' reply described in the third paragraph of the passage above?", [
            (True, "Without the higher yields, millions of additional hectares of forest and grassland would have had to be turned into farmland.",
             "himoyachilarning daʼvosi — koʻproq yer ochilishi kerak boʻlardi."),
            (False, "Many small farmers could not afford the fertiliser the new varieties needed.", "bu tanqidchilarning dalili."),
            (False, "Groundwater levels fell in parts of India after irrigation expanded.", "tanqidchilarniki."),
            (False, "Borlaug worked in Mexico for many years before the varieties reached India.", "mavzudan tashqari."),
            (False, "High-yielding rice varieties spread through Asia in the same period.", "himoyachilar daʼvosiga taʼsir qilmaydi."),
        ], "RC ichida ham CR savoli keladi: avval kimning daʼvosi ekanini aniqlang."),
        ask("Which of the following best describes the organisation of the passage above?", [
            (True, "An innovation is described, its spread and results are reported, and a debate about its costs is summarised.", "uch abzas — uch qism."),
            (False, "A problem is described, several solutions are rejected, and one is recommended.", "tavsiya yoʻq."),
            (False, "A theory is presented and then shown to be false.", "nazariya rad etilmagan."),
            (False, "The careers of two scientists are compared.", "faqat bitta olim."),
            (False, "A historical event is described, and historians' disagreement about its causes is explained.", "bahs sabab haqida emas — narx haqida."),
        ], "Oxirgi variant yaqin, lekin bitta soʻz — «causes» — uni notoʻgʻri qiladi."),
        {"rich_text": (
            "<h3>Natijani tahlil qiling</h3>"
            + WARN.format("Bu toʻplamdagi eng nozik tuzoq — oxirgi savoldagi «causes»: tuzilish toʻgʻri, bitta soʻz notoʻgʻri. RCʼda variantni "
                          "<b>oxirigacha</b> oʻqing — notoʻgʻri soʻz koʻpincha oxirida turadi.")
            + NOTE.format("Critical Reasoning va Reading Comprehension bloklarini tugatdingiz. Keyingi qadam — aralash Verbal mashqlari: "
                          "CR va RC birga, vaqt bilan.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("industrial espionage", "sanoat josusligi"), ("semi-dwarf", "yarim pakana (nav)"), ("yield", "hosildorlik"),
                     ("fertiliser", "oʻgʻit"), ("groundwater", "yer osti suvi"), ("dominance", "hukmronlik")])
            + "<h3>Xulosa</h3><ul><li>Har matnni bir marta, xarita bilan.</li><li>Savol turini aniqlang, kerakli abzasga qayting.</li>"
            "<li>Variantni oxirigacha oʻqing.</li><li>Xatolarni dars raqami bilan belgilang.</li></ul>"
        )},
    ],
},
]
