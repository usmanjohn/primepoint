# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — Reading Comprehension, lessons 30 (how RC works), 31 (main idea and
primary purpose) and 32 (detail questions). See toc_gmat_verbal.txt and
STYLE_GUIDE_GMAT_VERBAL.md §1: an RC passage (200–350 words) sits in its OWN block and the
question blocks after it refer to "the passage above".

Every passage is about something real, and every fact in it is true as written — the
pupil will remember these passages, so they must not remember errors.
"""
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("_gmatv_base", os.path.join(_HERE, "_lessons_gmat_verbal_1_12.py"))
_b1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_b1)

TRACK = _b1.TRACK
TIP, WARN, NOTE = _b1.TIP, _b1.WARN, _b1.NOTE
ask, steps, cards = _b1.ask, _b1.steps, _b1.cards

TOPIC_RC = {
    "title":   "Reading Comprehension",
    "summary": "Uzun matn va unga bir nechta savol: asosiy fikr, tafsilot, xulosa, tuzilish, qoʻllash va muallif ohangi.",
    "icon":    "bi-book",
    "order":   4,
}


def passage(title, paras, time="⏱ Matn: ~3 daqiqa"):
    """An RC passage in its own block. title is an Uzbek heading above the pane."""
    body = ''.join(f'<p>{p}</p>' for p in paras)
    return {"rich_text": f'<h3>{title}</h3><div class="sr-passage">{body}</div><span class="sr-time">{time}</span>'}


# ── Passages ─────────────────────────────────────────────────────────────────
P_ULUGH_BEG = [
    "In the 1420s, Ulugh Beg, the ruler of Samarkand and a grandson of Timur, built one of the largest observatories of the "
    "medieval world on a hill outside the city. Its central instrument was not a telescope — telescopes would not be invented "
    "for nearly two centuries — but an enormous meridian arc: a curved track cut into the hillside along the north–south line, "
    "with a radius of roughly 40 metres. The size was the point. On an instrument that large, a single degree of arc stretched "
    "across a long section of the track, so observers could read the position of the Sun or a star far more finely than on the "
    "small brass instruments of the time.",
    "The results justified the effort. The astronomers working with Ulugh Beg produced the Zij-i Sultani, a set of astronomical "
    "tables that included a catalogue of about a thousand stars. Their measurement of the length of the year differed from the "
    "modern value by less than a minute.",
    "The observatory did not long outlive its founder. After Ulugh Beg was killed in 1449, the building was abandoned and "
    "gradually destroyed, and its location was forgotten. Only in 1908 did the archaeologist Vasily Vyatkin, guided by a "
    "historical document, uncover the remains of the arc, which visitors to Samarkand can still see today. The tables had "
    "travelled further than the building: copies circulated widely, and a Latin translation of the star catalogue was published "
    "in Oxford in 1665.",
]

P_CONTAINER = [
    "Before the mid-1950s, loading a cargo ship was slow and costly work. Goods arrived at the docks in sacks, barrels and crates "
    "of every size, and teams of dockworkers carried them aboard piece by piece, a process that could keep a ship in port for "
    "days. Theft and damage were common, and the cost of handling cargo at both ends of a voyage often exceeded the cost of the "
    "voyage itself.",
    "In 1956 a trucking entrepreneur named Malcolm McLean sent a converted tanker, the Ideal X, from Newark to Houston carrying "
    "58 metal containers that could be lifted directly from truck to ship. The idea was simple: rather than handling each item, "
    "handle one standard box. McLean later estimated that loading the Ideal X had cost about 16 cents per ton, compared with "
    "roughly $5.86 per ton for loose cargo.",
    "The savings did not arrive all at once. Containers paid off only when ports, ships, trucks and railways were all built to "
    "handle the same box, and agreeing on standard sizes took years of negotiation. Many ports that refused to invest in cranes "
    "and storage yards lost their trade to rivals that did. But once the system was in place, the cost of moving goods between "
    "continents fell so far that it became practical to make a product's parts in several countries — one reason economists "
    "often list the container among the inventions that made modern globalisation possible.",
]

P_ANCHORING = [
    "Ask people whether the population of a city is more or less than five million, then ask them to estimate it, and their "
    "estimates will be pulled toward five million — even if they know the number was chosen at random. Psychologists call this "
    "effect anchoring. In a well-known experiment published in 1974, Amos Tversky and Daniel Kahneman spun a wheel of fortune "
    "that was rigged to stop at either 10 or 65, and then asked participants to estimate the percentage of African countries in "
    "the United Nations. Those who had seen 10 gave a median estimate of 25 percent; those who had seen 65 gave a median estimate "
    "of 45 percent. A number that participants could see was meaningless still moved their answers by twenty points.",
    "Anchoring matters well beyond the laboratory. In negotiations, the first price mentioned tends to shape the final "
    "agreement, which is why many negotiators advise making the first offer rather than waiting for one. Retailers display a "
    "high original price beside a sale price for a similar reason: the higher figure makes the discount look larger.",
    "Yet the effect is not unlimited. Later research has found that anchors work best when people are uncertain; an expert who "
    "knows a market well is harder to move than a newcomer, though rarely immune. For managers, the practical lesson is less "
    "that anchors can be avoided than that they should be noticed — and that the first number on the table deserves more "
    "scrutiny than it usually receives.",
]

P_MICROCREDIT = [
    "When Muhammad Yunus began lending small sums to poor villagers in Bangladesh in the 1970s, conventional banks considered "
    "such borrowers too risky to serve: they had no collateral and no credit history. Yunus's answer, developed into the Grameen "
    "Bank, was to lend to small groups, mostly of women, whose members met regularly and whose access to future loans depended "
    "on the group's repayment record. Repayment rates were high, and in 2006 Yunus and the bank shared the Nobel Peace Prize.",
    "By then, microcredit had become one of the most celebrated ideas in development, and many supporters claimed that it could "
    "lift millions of families out of poverty. Careful evaluation told a more modest story. In the 2010s, randomised studies in "
    "six countries, which compared areas that gained access to microloans with similar areas that did not, found that borrowers "
    "often started or expanded small businesses but that, on average, household income and consumption did not rise substantially.",
    "None of this means that microcredit failed. The same studies suggested that loans gave many households more freedom in how "
    "to spend and invest, and that a minority of borrowers who already ran businesses gained a great deal. What the evidence did "
    "undermine was the claim that a small loan is, by itself, a reliable route out of poverty.",
]

P_ARAL = [
    "Until the 1960s, the Aral Sea, which lies between Kazakhstan and Uzbekistan, was the fourth-largest lake in the world. It "
    "was fed by two great rivers, the Amu Darya and the Syr Darya. Then Soviet planners, seeking to turn the surrounding desert "
    "into cotton fields, diverted much of the rivers' water into irrigation canals. The sea began to shrink, and the shrinking "
    "accelerated. By the 2000s it had split into separate bodies of water and had lost most of its former area.",
    "The consequences reached far beyond the shoreline. As the water retreated, the fishing industry that had employed tens of "
    "thousands of people collapsed, and former ports were left many kilometres from the water. The exposed seabed became a new "
    "desert, now called the Aralkum, from which winds carry dust laden with salt and agricultural chemicals across the region.",
    "The story has not been one of loss alone. In 2005 Kazakhstan, with support from the World Bank, completed the Kok-Aral dam, "
    "which holds the water of the Syr Darya in the northern part of the sea. The North Aral's level rose, its water became less "
    "salty, and fish catches recovered enough to revive some local fishing. The much larger southern part, which depends on the "
    "heavily used Amu Darya, has continued to shrink. The contrast suggests that the sea's decline was not irreversible "
    "everywhere — but also that recovery depends on how much water people are prepared to leave in the rivers.",
]

P_PENICILLIN = [
    "The discovery of penicillin is often told as the story of a lucky accident, and it began as one. In 1928 the Scottish "
    "bacteriologist Alexander Fleming noticed that a mould growing on one of his culture plates had killed the bacteria around "
    "it. He named the active substance penicillin and published his findings, but he was unable to purify it in useful amounts, "
    "and for about a decade it attracted little attention.",
    "The work that turned the observation into a medicine was done at Oxford, where Howard Florey and Ernst Chain led a team "
    "that, from 1939, developed methods to extract and purify penicillin and tested it, first in mice and then in patients. "
    "Their first patient, a policeman treated in 1941, improved dramatically, but the supply of the drug ran out and he died. "
    "The question was no longer whether penicillin worked but how to make enough of it.",
    "That problem was solved largely in the United States, where government laboratories and drug companies developed methods "
    "to grow the mould in large tanks. By 1944 production had risen to levels that allowed penicillin to be supplied widely to "
    "Allied forces. In 1945 Fleming, Florey and Chain shared the Nobel Prize in Physiology or Medicine — a recognition that the "
    "discovery had required not one accident but years of deliberate work by many people.",
]


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 30 — how RC works
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 30: How Reading Comprehension Works — Passages, Question Sets and a Reading Map",
    "summary": "Reading Comprehension qanday tuzilgan: matn va unga bir nechta savol, oʻqish xaritasi va savol turlari bilan birinchi tanishuv.",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Uzun matn, bir nechta savol</h2>"
            "<p>Reading Comprehension (RC) savolida ekranning bir tomonida 200–350 soʻzli matn turadi, ikkinchi tomonida esa savollar "
            "<b>birin-ketin</b> chiqadi — bitta matnga odatda bir nechta savol. GMAC rasmiy taʼrifiga koʻra, bu savollar "
            "<mark>asosiy fikr, tafsilot, xulosa, qoʻllash, mantiqiy tuzilish va uslub</mark>ni tekshiradi.</p>"
            "<p>Critical Reasoningʼda har bir soʻz muhim edi. RCʼda esa aksincha: hamma tafsilotni eslab qolish shart emas. "
            "Muhimi — matnning <b>skeleti</b>: muallif nima demoqchi va har bir abzas bu maqsadga qanday xizmat qiladi.</p>"
            '<span class="sr-time">⏱ Matnga 2–3 daqiqa, har savolga ~1–1.5 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: oʻqish xaritasi</h3>"
            + steps([
                "<p><strong>1. Birinchi abzas:</strong> mavzu va (agar bor boʻlsa) muallifning asosiy daʼvosi. Sekin oʻqing.</p>",
                "<p><strong>2. Har bir abzas:</strong> uning <b>vazifasini</b> 3–5 soʻz bilan belgilang: «tarix», «natija», «cheklov», «qarshi fikr».</p>",
                "<p><strong>3. Burilish soʻzlari:</strong> <i>but, yet, however, not … but</i> — muallifning fikri koʻpincha shu yerda.</p>",
                "<p><strong>4. Tafsilotlarni yodlamang</strong> — raqam va ismlar kerak boʻlsa, xarita sizni kerakli abzasga olib boradi.</p>",
                "<p><strong>5. Savol:</strong> javobni xotiradan emas, <b>matndan</b> tasdiqlang.</p>",
            ])
        )},
        passage("1-matn: Ulugʻbek rasadxonasi", P_ULUGH_BEG),
        {"rich_text": (
            "<h3>Ishlangan namuna: shu matnning xaritasi</h3>"
            "<p><b>1-abzas:</b> rasadxona va uning ulkan yoyi — <i>nima uchun katta?</i> (aniqlik). "
            "<b>2-abzas:</b> natija — jadvallar, yil uzunligi. <b>3-abzas:</b> rasadxonaning taqdiri — vayron boʻldi, 1908-yilda topildi, "
            "jadvallar esa Yevropaga yetdi.</p>"
            "<p>Matnning skeleti: <mark>katta asbob → aniq natija → bino yoʻqoldi, natija qoldi</mark>. Endi savollarga shu xarita bilan javob beramiz.</p>"
            + TIP.format("Xaritani qogʻozga yozish shart emas — har abzasdan keyin bir soniya toʻxtab, uning vazifasini ichingizda ayting.")
        )},
        ask("The primary purpose of the passage above is to", [
            (True, "describe the achievement of a medieval observatory and what became of it", "uchala abzas: asbob, natija, taqdir."),
            (False, "explain why telescopes replaced instruments such as meridian arcs", "teleskop faqat qavs ichida eslatilgan."),
            (False, "argue that Ulugh Beg's measurements were more accurate than modern ones", "matnda farq «bir daqiqadan kam» — zamonaviy qiymat aniqroq."),
            (False, "compare Ulugh Beg's observatory with observatories in Europe", "taqqoslash yoʻq."),
            (False, "trace the history of Samarkand under Timur's descendants", "juda keng — matn bitta rasadxona haqida."),
        ], "Asosiy maqsad savoli butun matnni qamrashi kerak — bitta abzasni emas."),
        ask("According to the passage, the great size of the meridian arc allowed observers to", [
            (True, "read the positions of the Sun and stars more finely than on small instruments", "1-abzas: «far more finely than on the small brass instruments»."),
            (False, "see stars too faint to be seen with the naked eye", "bu teleskopning ishi — matnda yoʻq."),
            (False, "use the arc as a sundial during the day", "aytilmagan."),
            (False, "work on the instrument in large groups at the same time", "aytilmagan."),
            (False, "keep the observatory standing after Ulugh Beg's death", "aksincha, u vayron boʻldi."),
        ], "Tafsilot savoli: javob matnning aniq bir joyida turadi — xarita sizni 1-abzasga olib boradi."),
        ask("It can be inferred from the passage that the star catalogue of the Zij-i Sultani", [
            (True, "was available to readers in Europe more than two centuries after the observatory was built", "1420-yillar → Oksford, 1665: 240 yildan ortiq."),
            (False, "was compiled after Ulugh Beg's death", "uning bilan ishlagan astronomlar tuzgan."),
            (False, "was translated into Latin by Vasily Vyatkin", "Vyatkin — 1908-yildagi arxeolog; tarjimon aytilmagan."),
            (False, "contained observations made with a telescope", "teleskop hali ixtiro qilinmagan edi."),
            (False, "was lost until the remains of the arc were found in 1908", "yoʻqolgan — bino; jadvallar keng tarqalgan."),
        ], "Xulosa savoli: matnda toʻgʻridan-toʻgʻri yozilmagan, lekin ikki faktdan albatta kelib chiqadigan narsa."),
        passage("2-matn: konteyner", P_CONTAINER),
        ask("Which of the following best describes the main point of the passage above?", [
            (True, "A simple change in how cargo was handled transformed shipping, although its benefits took years to appear.", "uchala abzas shu fikrga xizmat qiladi."),
            (False, "Dockworkers opposed the introduction of containers because it cost them their jobs.", "matnda bunday gap yoʻq."),
            (False, "Malcolm McLean built a successful career as a trucking entrepreneur.", "juda tor — matn uning karyerasi haqida emas."),
            (False, "Shipping goods by sea has always been cheaper than shipping them by rail.", "taqqoslash yoʻq."),
            (False, "Ports that invested in cranes and storage yards made a costly mistake.", "aksincha, ular yutgan."),
        ], "Asosiy fikrda ikki qism bor: oʻzgarish va uning sekin kelgan foydasi (3-abzasdagi «did not arrive all at once»)."),
        ask("According to the passage, which of the following was necessary before containers could pay off?", [
            (True, "Ports, ships, trucks and railways all being built to handle the same standard box", "3-abzas: «paid off only when…»."),
            (False, "Dockworkers being trained to carry heavier crates", "konteyner aynan qoʻlda tashishni yoʻqotdi."),
            (False, "Governments lowering taxes on imported goods", "aytilmagan."),
            (False, "Tankers being replaced by ships built only for containers", "aytilmagan — Ideal X oʻzi qayta jihozlangan tanker edi."),
            (False, "Factories moving the production of parts to several countries", "bu natija, shart emas."),
        ], "«Only when» — zarur shartning belgisi. Natija va shartni adashtirmang."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Juda tor</b> (bitta abzasning mavzusi — butun matn deb). <b>Juda keng</b> (Samarqand tarixi). "
                          "<b>Matnda yoʻq, lekin rost</b> — teleskop yulduzlarni yaqinlashtiradi; bu rost, ammo matn bu haqda gapirmaydi. "
                          "<b>Natija ↔ shart</b> — «parts in several countries» natija edi, shart emas.")
            + NOTE.format("Ulugʻbek haqidagi matnni oʻqiganda, bizning nomzodlar oʻzlari bilgan tarixdan javob tanlashi mumkin. "
                          "RCʼda faqat <b>matndagi</b> maʼlumot hisoblanadi — bilganingiz toʻgʻri boʻlsa ham.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("passage", "matn"), ("primary purpose", "asosiy maqsad"), ("main point", "asosiy fikr"),
                     ("according to the passage", "matnga koʻra"), ("it can be inferred", "xulosa qilish mumkin"),
                     ("reading map", "oʻqish xaritasi"), ("meridian arc", "meridian yoyi")])
            + "<h3>Xulosa</h3><ul><li>Matnni bir marta, xarita bilan oʻqing.</li><li>Har abzasning vazifasini belgilang.</li>"
            "<li>Javobni xotiradan emas, matndan tasdiqlang.</li><li>Bilganingiz emas — matnda yozilgani hisoblanadi.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 31 — main idea and primary purpose
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 31: Main Idea and Primary Purpose",
    "summary": "Asosiy fikr va asosiy maqsad savollari: «juda tor», «juda keng» va «juda kuchli» variantlarni ajratish, abzasning vazifasini topish.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>Matn nima haqida — va nima uchun yozilgan?</h2>"
            "<p>Ikki savol oʻxshaydi, lekin farqi bor. <mark>Main idea</mark> — muallif nimani aytadi («microcredit has real benefits but…»). "
            "<mark>Primary purpose</mark> — muallif nima qiladi: tasvirlaydi, tushuntiradi, baholaydi, rad etadi. Shuning uchun purpose "
            "variantlari <b>feʼl</b> bilan boshlanadi: <i>describe, explain, argue, assess, challenge</i>.</p>"
            '<span class="sr-time">⏱ Asosiy fikr savoli — ~1 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: Goldilocks testi</h3>"
            + steps([
                "<p><strong>1.</strong> Xaritangizdan foydalanib, matnni <b>bir jumlada</b> ayting — oʻqish tugashi bilan, variantlarga qaramay.</p>",
                "<p><strong>2. Juda tor?</strong> Variant faqat bitta abzasni qamraydimi? (Grameen qanday qarz bergani — faqat 1-abzas.)</p>",
                "<p><strong>3. Juda keng?</strong> Matndan tashqariga chiqadimi? («rivojlanish dasturlarini baholash usullari»)</p>",
                "<p><strong>4. Feʼl toʻgʻrimi?</strong> Muallif neytral tasvirlaydimi yoki baho beradimi? «Argue» kuchli; «describe» neytral. "
                "Matnning ohangiga mos feʼlni tanlang.</p>",
                "<p><strong>5. Oxirgi abzasga qarang</strong> — koʻp GMAT matnlarida muallifning xulosasi shu yerda.</p>",
            ])
        )},
        passage("1-matn: langar effekti (anchoring)", P_ANCHORING),
        {"rich_text": (
            "<h3>Ishlangan namuna: bir jumlada</h3>"
            "<p><b>1-abzas:</b> effekt + tajriba. <b>2-abzas:</b> laboratoriyadan tashqarida (muzokara, chakana savdo). "
            "<b>3-abzas:</b> «Yet» — cheklov va menejerlar uchun saboq.</p>"
            "<p>Bir jumlada: <mark>langar effekti — isbotlangan va amalda muhim, lekin noaniqlik kam boʻlganda kuchsizroq</mark>. "
            "Eʼtibor bering: uchinchi abzasdagi «Yet» butun matnning ohangini yumshatadi — toʻgʻri javob ham shu yumshoqlikni saqlaydi.</p>"
            + TIP.format("Matnni bir jumlada aytolmasangiz, savollarga oʻtmang — 10 soniya qaytib, birinchi va oxirgi abzasni qayta qarang.")
        )},
        ask("Which of the following best states the main idea of the passage above?", [
            (True, "Anchoring is a well-documented effect that influences real decisions, though it is weaker when people are less uncertain.", "uchala abzasni qamraydi, cheklov bilan."),
            (False, "Experts are immune to the anchoring effect.", "matn «rarely immune» deydi — zid."),
            (False, "Retailers deliberately deceive customers by inventing original prices.", "juda kuchli va tor — 2-abzasdagi bitta misol."),
            (False, "The 1974 experiment was flawed because the wheel of fortune was rigged.", "tajriba tanqid qilinmagan; «rigged» — dizaynning bir qismi."),
            (False, "Negotiators should wait for the other side to make the first offer.", "teskari — matn birinchi taklifni tavsiya qiladi."),
        ], "Toʻgʻri javob ham effektni, ham uning chegarasini aytadi — matnning oʻzi kabi."),
        ask("The primary purpose of the passage above is to", [
            (True, "describe a psychological effect, illustrate its practical importance, and note a limit on it", "uch abzas — uch harakat."),
            (False, "challenge a widely accepted theory of decision-making", "muallif effektni qabul qiladi."),
            (False, "compare two competing explanations of the anchoring effect", "tushuntirishlar solishtirilmagan."),
            (False, "recount the careers of two well-known psychologists", "ular faqat tajriba muallifi sifatida eslatilgan."),
            (False, "argue that anchoring should be banned in retail advertising", "taqiq haqida gap yoʻq."),
        ], "Purpose — feʼllar ketma-ketligi: tasvirlaydi → koʻrsatadi → cheklaydi."),
        ask("The third paragraph of the passage above serves primarily to", [
            (True, "qualify the earlier claims by noting when the effect is weaker", "«Yet the effect is not unlimited» — cheklov."),
            (False, "present new evidence that the anchoring effect does not exist", "juda kuchli — effekt bor, faqat kuchsizroq."),
            (False, "explain how the 1974 experiment was carried out", "bu 1-abzasda."),
            (False, "give an example of anchoring in negotiations", "bu 2-abzasda."),
            (False, "argue that managers can easily avoid the influence of anchors", "teskari: «less that anchors can be avoided»."),
        ], "Abzasning vazifasi — xaritangizdagi belgi: «cheklov»."),
        passage("2-matn: mikrokredit", P_MICROCREDIT),
        ask("The primary purpose of the passage above is to", [
            (True, "assess how well the evidence supports the strongest claims made for microcredit", "2–3-abzaslar: daʼvolar va dalillar."),
            (False, "argue that microcredit has failed and should be abandoned", "«None of this means that microcredit failed» — zid."),
            (False, "explain how the Grameen Bank selected its borrowers", "juda tor — faqat 1-abzas."),
            (False, "praise Muhammad Yunus for winning the Nobel Peace Prize", "mukofot — bitta fakt, maqsad emas."),
            (False, "compare microcredit in Bangladesh with banking in wealthy countries", "taqqoslash yoʻq."),
        ], "«Assess» — baholash: muallif daʼvoni dalillar bilan solishtiradi."),
        ask("The author of the passage above would most likely agree with which of the following?", [
            (True, "Microcredit has real benefits but has not proved to be the reliable route out of poverty that some supporters claimed.", "3-abzasning xulosasi."),
            (False, "Randomised studies are the only reliable way to evaluate development programmes.", "juda kuchli — matn bunday demaydi."),
            (False, "Conventional banks were right to refuse to lend to poor villagers.", "matnda bunday baho yoʻq."),
            (False, "Microcredit benefits only women.", "juda kuchli va matnda yoʻq."),
            (False, "The Nobel Peace Prize should not have been awarded to Yunus.", "muallif mukofotni baholamaydi."),
        ], "Muallifning pozitsiyasi oxirgi abzasda: foyda bor, lekin «by itself» yechim emas."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Juda tor</b> — bitta abzasning mavzusi. <b>Juda keng</b> — butun bir soha. <b>Juda kuchli feʼl yoki baho</b> — "
                          "«failed», «immune», «banned», «only». <b>Teskari</b> — muallif rad etgan fikr («microcredit failed»).")
            + NOTE.format("GMAT mualliflari kamdan-kam hollarda keskin gapiradi: «not unlimited», «more modest», «rarely immune». "
                          "Bizdagi nomzodlar keskin, «aniq» javobni afzal koʻradi — RCʼda esa koʻpincha <b>yumshoq</b> variant toʻgʻri.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("main idea", "asosiy fikr"), ("qualify a claim", "daʼvoni cheklamoq, yumshatmoq"), ("assess", "baholamoq"),
                     ("anchoring", "langar effekti"), ("collateral", "garov"), ("randomised study", "tasodifiy tanlovli tadqiqot"),
                     ("scrutiny", "sinchiklab tekshirish")])
            + "<h3>Xulosa</h3><ul><li>Main idea — nima deydi; purpose — nima qiladi (feʼl).</li><li>Matnni bir jumlada ayting, keyin variantlarga qarang.</li>"
            "<li>Tor, keng, kuchli — uch tuzoq.</li><li>Oxirgi abzas koʻpincha muallifning pozitsiyasi.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 32 — detail questions
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_RC,
    "title": "GMAT Verbal 32: Detail Questions — Answering From the Line",
    "summary": "Tafsilot savollari: «according to the passage» — javobni xotiradan emas, matnning aniq qatoridan topish va soʻzma-soʻz tuzoqlardan saqlanish.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Javob matnda yozilgan — uni toping</h2>"
            "<p>Tafsilot savoli eng «oson» koʻrinadi: <i>According to the passage…</i>, <i>The passage states that…</i>. Javob haqiqatan matnda "
            "yozilgan. Lekin aynan shu yerda nomzodlar xato qiladi: <b>xotiradan</b> javob beradi, yoki matndagi soʻzlarni takrorlaydigan, "
            "ammo <mark>boshqa narsani</mark> aytadigan variantni tanlaydi.</p>"
            '<span class="sr-time">⏱ Tafsilot savoli — ~1 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: qatordan javob</h3>"
            + steps([
                "<p><strong>1.</strong> Savoldagi <b>kalit soʻzni</b> toping (Kok-Aral, Fleming, dust).</p>",
                "<p><strong>2.</strong> Xaritangiz bilan kerakli abzasga boring va <b>oʻsha gapni qayta oʻqing</b> — oldingi va keyingi gap bilan.</p>",
                "<p><strong>3.</strong> Javobni oʻz soʻzingiz bilan ayting, keyin variantlarga qarang.</p>",
                "<p><strong>4.</strong> Toʻgʻri javob koʻpincha matnni <b>boshqa soʻzlar bilan</b> aytadi (parafraz). Matn soʻzlarini aynan takrorlagan "
                "variant esa koʻpincha tuzoq: soʻzlar toʻgʻri, munosabat notoʻgʻri.</p>",
            ])
        )},
        passage("1-matn: Orol dengizi", P_ARAL),
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            "<p>Savol: «Nima uchun Orol qisqara boshladi?» Kalit soʻz — <i>began to shrink</i>. 1-abzasda: «Soviet planners… diverted much of "
            "the rivers' water into irrigation canals. The sea began to shrink…» Javob oʻz soʻzimiz bilan: <mark>daryolar suvi paxta "
            "dalalariga burildi</mark>. Variantlar orasida «Aralkum choʻli dengizga yoyildi» kabi matndagi soʻzlarni ishlatgan, lekin sabab va "
            "natijani almashtirgan variant boʻladi — Aralkum qisqarishning <b>natijasi</b>.</p>"
            + TIP.format("Sana va raqamlarga ehtiyot boʻling: Kok-Aral 2005-yilda <b>shimoliy</b> qismda qurildi. Janubiy qism haqidagi variant — "
                         "matndagi soʻzlarni ishlatgan tuzoq.")
        )},
        ask("According to the passage above, the Aral Sea began to shrink because", [
            (True, "much of the water of the rivers that fed it was diverted to irrigate cotton fields", "1-abzas: «diverted much of the rivers' water»."),
            (False, "the climate of the region became drier", "iqlim haqida gap yoʻq."),
            (False, "the Kok-Aral dam held back the water of the Syr Darya", "toʻgʻon 2005-yilda — qisqarishdan ancha keyin va shimolni tikladi."),
            (False, "the Aralkum desert spread into the sea", "sabab va natija almashtirilgan."),
            (False, "fishing fleets polluted the water of the sea", "aytilmagan."),
        ], "Sabab savolida vaqt tartibini tekshiring: sabab natijadan oldin keladi."),
        ask("According to the passage above, which of the following happened after the Kok-Aral dam was completed?", [
            (True, "The water of the North Aral became less salty.", "3-abzas: «its water became less salty»."),
            (False, "The southern part of the sea began to grow again.", "teskari — «has continued to shrink»."),
            (False, "The Amu Darya was diverted into the northern part of the sea.", "toʻgʻon Sirdaryo suvini ushlaydi."),
            (False, "The Aralkum desert disappeared.", "aytilmagan."),
            (False, "Fishing employed more people than it had before the 1960s.", "faqat «revive some local fishing»."),
        ], "Qaysi qism haqida gap ketayotganini kuzating: shimol ≠ janub."),
        ask("The passage above states that the dust carried from the Aralkum", [
            (True, "contains salt and agricultural chemicals", "2-abzas: «dust laden with salt and agricultural chemicals»."),
            (False, "stopped once the Kok-Aral dam was built", "aytilmagan."),
            (False, "is the main cause of the sea's decline", "sabab — suvning burilishi."),
            (False, "falls mainly on cotton fields in Kazakhstan", "«across the region» — aniq joy aytilmagan."),
            (False, "consists mostly of the remains of fish", "aytilmagan."),
        ], "«States that» — matnda toʻgʻridan-toʻgʻri yozilgan narsa."),
        passage("2-matn: penitsillin", P_PENICILLIN),
        ask("According to the passage above, Fleming's own work on penicillin was limited by", [
            (True, "his inability to purify the substance in useful amounts", "1-abzas: «unable to purify it in useful amounts»."),
            (False, "his failure to publish his findings", "u natijalarni chop etgan."),
            (False, "a shortage of patients willing to be treated", "aytilmagan."),
            (False, "the outbreak of war in 1939", "urush Flemingning ishiga bogʻlanmagan."),
            (False, "the death of the first patient treated with penicillin", "bu Oksford jamoasining tarixi, 1941."),
        ], "Kim nima qilganini adashtirmang: Fleming — kashfiyot; Florey va Chain — tozalash; AQSh — ishlab chiqarish."),
        ask("According to the passage above, after the first patient was treated in 1941, the main remaining problem was", [
            (True, "producing penicillin in large enough quantities", "2-abzas oxiri: «how to make enough of it»."),
            (False, "proving that penicillin worked in human patients", "«no longer whether penicillin worked»."),
            (False, "finding a mould that could kill bacteria", "bu 1928-yilda topilgan."),
            (False, "persuading the Nobel committee to recognise the work", "mukofot natija sifatida eslatilgan."),
            (False, "testing the drug on mice", "bu bemorlardan oldin qilingan."),
        ], "«No longer A but B» — bitta gapda ikkala javob bor; savol qaysi birini soʻrayotganiga qarang."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Soʻzma-soʻz tuzoq</b> — matndagi soʻzlar, notoʻgʻri munosabat (Aralkum sabab emas, natija). <b>Notoʻgʻri qism</b> — "
                          "shimol oʻrniga janub, Fleming oʻrniga Oksford jamoasi. <b>Rost, lekin matnda yoʻq</b> — iqlim oʻzgarishi haqiqatan muhim, "
                          "ammo bu matn uni aytmaydi.")
            + NOTE.format("Orol dengizi haqida koʻpchiligimiz oʻzimiz biladigan narsalarni eslaymiz — Moʻynoqdagi kemalar, tuzli boʻronlar. "
                          "Savolda faqat <b>matndagi</b> maʼlumot hisoblanadi. Bilganingizni chetga qoʻyib, qatorni oʻqing.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("according to the passage", "matnga koʻra"), ("the passage states", "matnda aytilgan"), ("divert", "burmoq (suvni)"),
                     ("irrigation", "sugʻorish"), ("laden with", "… bilan toʻla"), ("purify", "tozalamoq"), ("paraphrase", "boshqa soʻzlar bilan aytish")])
            + "<h3>Xulosa</h3><ul><li>Kalit soʻz → abzas → gap → oʻz soʻzingiz → variant.</li><li>Xotiradan javob bermang.</li>"
            "<li>Soʻzma-soʻz takror — koʻpincha tuzoq; parafraz — koʻpincha toʻgʻri.</li><li>Kim, qayer, qachon — aniqligini tekshiring.</li></ul>"
        )},
    ],
},
]
