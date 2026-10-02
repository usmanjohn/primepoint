# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — lessons 40, 41 (mixed Verbal drills: one RC passage + four CR
arguments, under time) and 42 (strategy review). The last batch of the track.
See toc_gmat_verbal.txt and STYLE_GUIDE_GMAT_VERBAL.md.

Helpers are loaded by path from the earlier batch files: cr/ask/steps/cards from 1_12,
crf (full-label autopsy for boldface) from 23_26, passage() from 30_32.
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
_b3 = _load("_lessons_gmat_verbal_23_26.py")
_rc = _load("_lessons_gmat_verbal_30_32.py")

TRACK = _b1.TRACK
TIP, WARN, NOTE = _b1.TIP, _b1.WARN, _b1.NOTE
cr, ask, steps, cards = _b1.cr, _b1.ask, _b1.steps, _b1.cards
crf = _b3.crf
passage = _rc.passage

TOPIC_DRILL = {
    "title":   "Aralash mashq (Verbal section drills)",
    "summary": "Critical Reasoning va Reading Comprehension birga, vaqt bilan — imtihondagidek; va butun Verbal strategiyasining takrori.",
    "icon":    "bi-stopwatch",
    "order":   5,
}


# ── Passages ─────────────────────────────────────────────────────────────────
P_ROAD_PRICING = [
    "In 1975 Singapore became the first city to charge drivers for entering its busiest streets. Under the Area Licensing "
    "Scheme, cars entering the central business district during the morning rush hour had to display a paper licence bought in "
    "advance, and traffic in the zone fell sharply. In 1998 the paper licences were replaced by Electronic Road Pricing: charges "
    "are deducted automatically as vehicles pass under gantries, and the rates vary by place and time of day. The authorities "
    "review the rates regularly, raising them where traffic is too slow and lowering them where roads are underused, so the "
    "charge works less like a tax than like a price that responds to demand.",
    "For years, other cities treated Singapore as a special case — a small, wealthy city-state whose government faced little "
    "opposition. Stockholm's experience suggested otherwise. In 2006 the Swedish capital ran a seven-month trial of congestion "
    "charging, despite polls showing that most residents opposed it. Traffic across the charging cordon fell by roughly 20 "
    "percent, and when residents voted in a referendum after the trial, a majority supported keeping the charge, which became "
    "permanent in 2007.",
    "The Stockholm result points to a political lesson that may matter as much as the economic one. Before a charge is "
    "introduced, its costs are obvious and its benefits are hypothetical; once people have experienced shorter journeys, the "
    "balance looks different. Opposition to congestion pricing, in other words, may say less about the policy than about the "
    "difficulty of imagining its effects.",
]

P_MPESA = [
    "In 2007 the Kenyan mobile network Safaricom launched M-Pesa, a service that let people store money on their mobile phones "
    "and send it to others by text message. Customers turned cash into electronic money, and back again, at small shops that "
    "acted as agents. The service required neither a bank account nor a smartphone, which mattered in a country where most adults "
    "had neither but many had a basic phone. Within a few years, a large majority of Kenyan households were using it.",
    "Its most obvious use was sending money home. Workers in cities could transfer part of their wages to relatives in the "
    "countryside in seconds, instead of sending cash with travellers or bus drivers. But economists were interested in a less "
    "visible effect. When a household suffered a shock — an illness, a failed harvest — those with access to M-Pesa could "
    "quickly receive small amounts from a wide network of relatives and friends, and they were better able to keep up their "
    "spending on food than households without it.",
    "In a study published in 2016, the economists Tavneet Suri and William Jack estimated that access to M-Pesa had lifted about "
    "2 percent of Kenyan households out of extreme poverty, with especially large effects for households headed by women, partly "
    "because some women moved from farming into business. The service did not create income directly. What it did was make "
    "existing money move more easily — and, for poor households, that turned out to be worth a great deal.",
]


def _drill_intro(title, minutes, note):
    return {"rich_text": (
        f"<h2>{title}</h2>"
        "<p>Bu dars — imtihonning kichik nusxasi: <b>bitta Reading Comprehension matni</b> (uchta savol) va <b>toʻrtta Critical Reasoning</b> "
        "argumenti. Hech qanday yangi qoida yoʻq — faqat siz oʻrgangan usullar, aralash tartibda va vaqt bilan.</p>"
        f"<p>{note}</p>"
        f'<span class="sr-time">⏱ Maqsad: 7 savol — {minutes} daqiqa</span>'
    )}


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 40 — Verbal drill I
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_DRILL,
    "title": "GMAT Verbal 40: Verbal Drill I — Mixed Critical Reasoning and Reading Comprehension",
    "summary": "Birinchi aralash mashq: bitta RC matni (yoʻl haqi) va toʻrtta CR argumenti — taxmin, paradoks, zaiflashtirish, inference.",
    "order": 40,
    "blocks": [
        _drill_intro("Verbal Drill I", 15,
                     "Soatni yoqing. 15 daqiqa — imtihondagi tezlikdan biroz bemalol: matnni oʻqishga ~3 daqiqa, har savolga ~1.5–2 daqiqa."),
        {"rich_text": (
            "<h3>Tez eslatma</h3>"
            + steps([
                "<p><strong>RC:</strong> bir marta oʻqing, abzas vazifalarini belgilang, javobni matndan tasdiqlang.</p>",
                "<p><strong>CR:</strong> avval savol turi → xulosa va dalil → boʻshliq → toʻrt tuzoqni chiqarib tashlash.</p>",
                "<p><strong>Vaqt:</strong> bitta savol 3 daqiqadan oshsa — eng yaxshi koʻringanini tanlab, davom eting.</p>",
            ])
            + TIP.format("Mashqdan keyin har xatoni dars raqami bilan belgilang (11 — taxmin, 23 — paradoks, 33 — RC inference…). "
                         "Shu roʻyxat — keyingi haftadagi takrorlash rejangiz.")
        )},
        passage("RC: yoʻl haqi (congestion pricing)", P_ROAD_PRICING),
        ask("The primary purpose of the passage above is to", [
            (True, "describe how congestion charging has worked in two cities and draw a lesson about public opposition to it", "uchala abzas: Singapur, Stokgolm, siyosiy saboq."),
            (False, "argue that every city should adopt Singapore's system immediately", "juda kuchli — tavsiya yoʻq."),
            (False, "explain how electronic gantries deduct charges from vehicles", "juda tor — 1-abzasdagi tafsilot."),
            (False, "compare the economies of Singapore and Sweden", "iqtisodlar solishtirilmagan."),
            (False, "criticise Stockholm's government for ignoring opinion polls", "muallif tanqid qilmaydi."),
        ], "Maqsadda oxirgi abzas — muallifning oʻz saboqi — albatta boʻlishi kerak."),
        ask("It can be inferred from the passage above that some residents of Stockholm", [
            (True, "changed their view of congestion charging between the start of the trial and the referendum", "avval koʻpchilik qarshi, keyin koʻpchilik tarafdor."),
            (False, "stopped driving altogether during the trial", "aytilmagan — harakat 20% kamaygan."),
            (False, "voted against the charge because traffic did not fall", "harakat kamaygan va koʻpchilik tarafdor."),
            (False, "had driven under Singapore's scheme before 2006", "aytilmagan."),
            (False, "paid higher charges than drivers in Singapore", "solishtirish yoʻq."),
        ], "Ikki faktni birlashtiring: «most residents opposed» + «a majority supported»."),
        ask("The author of the passage above mentions that Singapore's rates are raised and lowered according to traffic primarily in order to", [
            (True, "show that the charge behaves more like a price that responds to demand than like a tax", "gapning oʻzi: «less like a tax than like a price»."),
            (False, "suggest that Singapore's drivers pay too much", "baho yoʻq."),
            (False, "explain why the paper licences were replaced", "almashtirish sababi aytilmagan."),
            (False, "argue that Stockholm should have copied Singapore exactly", "aytilmagan."),
            (False, "illustrate the opposition Singapore's government faced", "aksincha — «faced little opposition»."),
        ], "Funksiya: tafsilot qaysi xulosaga xizmat qiladi — oʻsha gapning oxiriga qarang."),
        cr("A university plans to reduce the number of students who drop out by assigning every first-year student a faculty mentor. Last year, "
           "students who chose to meet regularly with a mentor dropped out at half the rate of other students.",
           "The university's plan depends on which of the following assumptions?", [
            (True, "The students who chose to meet with mentors last year were not already much less likely than other students to drop out.",
             "inkor qilsak: farq tanlovdan — reja natija bermasligi mumkin."),
            (False, "Faculty members will be paid extra for acting as mentors.", "xarajat — rejaning ishlashiga taʼsir qilmaydi."),
            (False, "Every first-year student will meet with a mentor every week.", "juda kuchli — muntazam uchrashuv yetarli boʻlishi mumkin."),
            (False, "Dropout rates at other universities are higher than at this one.", "mavzudan tashqari."),
            (False, "Most students who drop out do so after their first year.", "rejaga zarur emas."),
        ], "«Chose to» — ixtiyoriy guruh. 11 va 13-darslardagi boʻshliq."),
        cr("In the year after a city made its buses free to ride, the number of bus trips taken in the city rose by 30 percent. Yet the amount of car "
           "traffic in the city did not fall at all during that year.",
           "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "Most of the additional bus trips were made by people who had previously walked or cycled.", "yangi yoʻlovchilar mashinadan emas — mashinalar soni oʻzgarmaydi."),
            (False, "The city's population did not change during the year.", "ziddiyatni chuqurlashtiradi."),
            (False, "The wages of the city's bus drivers rose during the year.", "mavzudan tashqari."),
            (False, "Many residents said that they liked the free buses.", "faqat birinchi faktni tasdiqlaydi."),
            (False, "Car traffic fell in several neighbouring cities.", "boshqa shaharlar — tushuntirmaydi."),
        ], "Paradoks: «yangi avtobus yoʻlovchilari kim?» — javob ikkala faktni bogʻlaydi."),
        cr("A long-term study found that people who drink coffee every day live longer, on average, than people who drink no coffee. The researchers "
           "concluded that drinking coffee extends life.",
           "Which of the following, if true, most seriously weakens the researchers' conclusion?", [
            (True, "Many of the people in the study who drank no coffee had stopped drinking it on their doctors' advice because of existing health problems.",
             "kofe ichmaydiganlar orasida avvaldan kasallar koʻp — farq kofedan emas."),
            (False, "Coffee contains caffeine, which many people find stimulating.", "mavzudan tashqari."),
            (False, "Some people who drank coffee every day died young.", "«baʼzilari» — oʻrtacha natijani rad etmaydi."),
            (False, "The price of coffee rose during the years of the study.", "mavzudan tashqari."),
            (False, "The study included people from ten different countries.", "zaiflashtirmaydi — hatto kuchaytirishi mumkin."),
        ], "Teskari sabab va boshqa sabab — bogʻliqlik → sabab xulosasini zaiflashtirishning ikki yoʻli."),
        cr("Every product the company launched last year was tested with customers before launch. Only products that passed customer testing were "
           "advertised on television. The company's new water bottle was advertised on television.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "The new water bottle passed customer testing.", "faqat sinovdan oʻtganlar reklama qilingan; shisha reklama qilingan."),
            (False, "The new water bottle was launched last year.", "shart emas — boshqa yili chiqarilgan boʻlishi mumkin."),
            (False, "Every product that passed customer testing was advertised on television.", "teskari yoʻnalish — «only» bunday demaydi."),
            (False, "Some products launched last year failed customer testing.", "aytilmagan."),
            (False, "Most of the company's products are advertised on television.", "aytilmagan."),
        ], "«Only A are B» = «B boʻlsa — A». Reklama qilingan → sinovdan oʻtgan."),
        {"rich_text": (
            "<h3>Natijangiz</h3>"
            + WARN.format("Bu mashqdagi eng koʻp tanlanadigan xato — oxirgi savolda «launched last year»: u argumentdagi birinchi gapga yopishib "
                          "qoladi, lekin shishaga hech qanday zanjir bilan bogʻlanmaydi.")
            + NOTE.format("15 daqiqadan koʻp ketdimi? Vaqtni qayerda yoʻqotganingizni toping: matnni ikki marta oʻqidingizmi yoki bitta CRʼda "
                          "ikkilanib qoldingizmi? Ikkalasining davosi har xil (3 va 30-darslar).")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("congestion charge", "tirbandlik toʻlovi"), ("cordon", "chegara chizigʻi"), ("referendum", "referendum"),
                     ("mentor", "ustoz, maslahatchi"), ("drop out", "oʻqishni tashlamoq")])
            + "<h3>Xulosa</h3><ul><li>Aralash tartibda ham usul bir xil.</li><li>Xatolarni dars raqami bilan belgilang.</li>"
            "<li>Vaqtni qayerda yoʻqotganingizni aniqlang.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 41 — Verbal drill II
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_DRILL,
    "title": "GMAT Verbal 41: Verbal Drill II — Mixed, Under Time",
    "summary": "Ikkinchi aralash mashq, imtihon tezligida: bitta RC matni (M-Pesa) va toʻrtta CR — evaluate, reja, boldface, method.",
    "order": 41,
    "blocks": [
        _drill_intro("Verbal Drill II — imtihon tezligida", 13,
                     "Bu safar 13 daqiqa — imtihondagi oʻrtacha tezlikka yaqin (7 savol × ~1 daqiqa 57 soniya ≈ 13.7 daqiqa)."),
        {"rich_text": (
            "<h3>Tez eslatma</h3>"
            + steps([
                "<p><strong>Evaluate:</strong> «ha / yoʻq» — ikki tomonga suradigan savol (20).</p>",
                "<p><strong>Reja:</strong> maqsadni yozing; xarajat ≠ muvaffaqiyatsizlik (25).</p>",
                "<p><strong>Boldface:</strong> avval muallifning xulosasi, keyin rollar (24).</p>",
                "<p><strong>Method:</strong> argumentning harakatini abstrakt tasvirlang (25).</p>",
            ])
            + TIP.format("RC matnini oʻqishdan oldin birinchi savolga bir nazar tashlash mumkin — lekin barcha savollarni oldindan oʻqimang: "
                         "ular ekranda birin-ketin chiqadi va xotirani band qiladi.")
        )},
        passage("RC: M-Pesa", P_MPESA),
        ask("According to the passage above, M-Pesa was especially well suited to Kenya because it", [
            (True, "required neither a bank account nor a smartphone", "1-abzas: «required neither… which mattered in a country where…»."),
            (False, "was free for customers to use", "narx aytilmagan."),
            (False, "was designed for people who already had bank accounts", "teskari."),
            (False, "was operated by the Kenyan government", "Safaricom — mobil tarmoq."),
            (False, "paid interest on the money that customers stored", "aytilmagan."),
        ], "Tafsilot: «which mattered» — muallif sababni oʻzi koʻrsatgan."),
        ask("It can be inferred from the passage above that households without access to M-Pesa that suffered a shock", [
            (True, "were less able than households with access to keep up their spending on food", "2-abzasdagi taqqoslashning ikkinchi tomoni."),
            (False, "received no help at all from relatives and friends", "juda kuchli — kamroq yoki sekinroq boʻlishi mumkin."),
            (False, "were mostly headed by women", "aytilmagan."),
            (False, "moved from farming into business", "bu M-Pesaʼga ega baʼzi ayollar haqida."),
            (False, "lived only in cities", "aytilmagan."),
        ], "«Better able… than households without it» — teskari tomondan oʻqing."),
        ask("Which of the following is most similar to the way, according to the passage above, M-Pesa helped poor households?", [
            (True, "A new bridge that does not increase a village's harvest but lets its farmers sell their existing crops in a larger market",
             "yangi daromad emas — mavjud resurs osonroq harakatlanadi."),
            (False, "A government grant that gives each poor household a sum of money every month", "bu yangi daromad — matn «did not create income» deydi."),
            (False, "A new seed variety that doubles the size of farmers' harvests", "yangi daromad."),
            (False, "A tax cut for the country's largest companies", "mavzu ham, tamoyil ham boshqa."),
            (False, "A school that teaches children in the countryside to read", "boshqa tamoyil."),
        ], "Qoʻllash: tamoyilni mavzusiz ayting — «yangi narsa yaratmaydi, mavjudini harakatlantiradi»."),
        cr("A restaurant chain added a children's menu at ten of its branches, and sales at those branches rose by 12 percent over the next six months. "
           "The chain concludes that the children's menu caused the increase.",
           "Which of the following would it be most useful to know in order to evaluate the chain's conclusion?", [
            (True, "How sales changed over the same six months at the chain's branches that did not add a children's menu",
             "ular ham 12% oshgan boʻlsa — menyu sabab emas; oshmagan boʻlsa — xulosa kuchayadi."),
            (False, "Whether the children's menu includes desserts", "tarkib — sababni hal qilmaydi."),
            (False, "How much it cost to print the new menus", "xarajat — mavzudan tashqari."),
            (False, "Whether some children prefer the regular menu", "«baʼzilari» — hal qilmaydi."),
            (False, "Whether the chain plans to open new branches next year", "kelajak rejasi — mavzudan tashqari."),
        ], "Taqqoslash guruhi — evaluateʼning eng toʻgʻri savoli."),
        cr("Each month, about one in six patients at a clinic misses an appointment without warning. To reduce this number, the clinic plans to send "
           "every patient a text-message reminder on the day before each appointment.",
           "Which of the following, if true, most strongly suggests that the plan will succeed?", [
            (True, "Most patients who miss appointments at the clinic say that they simply forgot about them.", "sabab — unutish; eslatma aynan shunga qarshi."),
            (False, "Sending text messages costs the clinic very little.", "xarajat — natijani koʻrsatmaydi."),
            (False, "Some of the clinic's patients do not own mobile phones.", "rejani zaiflashtiradi."),
            (False, "Other clinics remind their patients by post.", "mavzudan tashqari."),
            (False, "Missed appointments cost the clinic a great deal of money.", "rejaning sababi, natijasi emas."),
        ], "Reja kuchayadi, agar muammoning sababi aynan reja hal qiladigan narsa boʻlsa."),
        crf("Critics say that the city's new metro line was badly managed, pointing out that <b>it cost twice as much per kilometre as the city's previous "
            "line</b>. But the new line runs entirely underground through the historic centre, where construction is far more difficult than on the "
            "surface. <b>Its cost per kilometre is therefore no evidence that it was badly managed.</b>",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is evidence used to support a view that the argument rejects; the second is the argument's main conclusion.", "tanqidchilar dalili va muallifning xulosasi."),
            (False, "The first is the argument's main conclusion; the second is evidence for that conclusion.", "teskari rollar."),
            (False, "The first is a fact that the argument disputes; the second is the argument's main conclusion.", "muallif narx faktini rad etmaydi — talqinini rad etadi."),
            (False, "The first is evidence used to support a view that the argument rejects; the second is further evidence for that view.", "ikkinchisi tanqidchilarga qarshi."),
            (False, "The first and the second are both evidence offered for the argument's main conclusion.", "birinchisi tanqidchilarniki."),
        ], "Fakt va talqin: muallif «ikki barobar qimmat» faktini qabul qiladi, undan chiqarilgan «yomon boshqarilgan» xulosani rad etadi."),
        cr("Rustam: Our company should stop advertising in newspapers, because fewer people read newspapers every year. Dilfuza: Fewer people read them, "
           "but the people who still do are mostly the older, wealthier customers who buy our most expensive products.",
           "Dilfuza responds to Rustam by", [
            (True, "conceding his premise but arguing that the remaining readers are the customers who matter most", "dalilni qabul qiladi, uning ahamiyatini rad etadi."),
            (False, "denying that newspaper readership is falling", "u buni tan oladi."),
            (False, "questioning Rustam's motives for making his proposal", "motiv haqida gap yoʻq."),
            (False, "arguing that the company should advertise only in newspapers", "juda kuchli."),
            (False, "pointing out that his conclusion contradicts his own evidence", "ziddiyat koʻrsatilmagan."),
        ], "«Fewer people read them, but…» — 25-darsdagi shakl: dalil qabul, xulosa rad."),
        {"rich_text": (
            "<h3>Natijangiz</h3>"
            + WARN.format("13 daqiqa ichida 6–7 toʻgʻri javob — imtihonga tayyor tezlik va aniqlik. 4 va undan kam boʻlsa, vaqtni emas, "
                          "<b>usulni</b> mustahkamlang: tezlik usul ishonchli boʻlganda keladi.")
            + NOTE.format("M-Pesa matni — biznes maktablari yaxshi koʻradigan mavzu: texnologiya, kambagʻallik va bozor birga. "
                          "Bunday matnlarda raqam (2 percent) koʻp joy egallamaydi, lekin savol aynan shunga tushishi mumkin.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("mobile money", "mobil pul"), ("agent", "agent (pul qabul qiluvchi doʻkon)"), ("shock", "kutilmagan zarba"),
                     ("extreme poverty", "oʻta qashshoqlik"), ("concede", "tan olmoq"), ("premise", "dalil, asos")])
            + "<h3>Xulosa</h3><ul><li>Imtihon tezligi — bir savolga ~2 daqiqa.</li><li>Tezlik usuldan keladi.</li>"
            "<li>Fakt va uning talqinini farqlang.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 42 — strategy review
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_DRILL,
    "title": "GMAT Verbal 42: Verbal Strategy Review — Pacing, Guessing and Review & Edit",
    "summary": "Butun Verbal kursining takrori: har bir savol turining bir qatorlik usuli, vaqt rejasi, taxmin qilish va imtihon kuni.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>Butun Verbal — bir sahifada</h2>"
            "<p>Siz Critical Reasoningʼning barcha asosiy turlarini va Reading Comprehensionʼning oltita savol turini oʻrgandingiz. Bu dars — "
            "imtihon oldidan oʻqiladigan <b>bir sahifalik takror</b>: har bir tur uchun bitta qoida, vaqt rejasi va oxirgi kun uchun maslahatlar.</p>"
            '<span class="sr-time">⏱ Takror — 10 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Har bir tur — bir qator</h3>"
            "<table class=\"table table-sm\"><thead><tr><th>Savol turi</th><th>Bir qatorlik usul</th></tr></thead><tbody>"
            "<tr><td>Conclusion / role (10, 24)</td><td>«Nimaga ishontirmoqchi?» — qolganlari «nima uchun?»</td></tr>"
            "<tr><td>Assumption (11)</td><td>Inkor qiling — argument yiqilsa, toʻgʻri.</td></tr>"
            "<tr><td>Weaken / strengthen (12)</td><td>Boshqa sabab, taqqoslash guruhi, vakillik, reja maqsadi.</td></tr>"
            "<tr><td>Evaluate (20)</td><td>«Ha» va «yoʻq» argumentni qarama-qarshi tomonga suradi.</td></tr>"
            "<tr><td>Flaw (21)</td><td>Xatoni oʻz soʻzingiz bilan ayting, keyin abstrakt variantga qaytaring.</td></tr>"
            "<tr><td>Inference (22, 33)</td><td>Eng ehtiyotkor; «yolgʻon boʻlishi mumkinmi?»</td></tr>"
            "<tr><td>Paradox (23)</td><td>Ikkala faktni ham tushuntiradi.</td></tr>"
            "<tr><td>Plan / method (25)</td><td>Maqsadni yozing; xarajat ≠ muvaffaqiyatsizlik.</td></tr>"
            "<tr><td>RC main idea (31)</td><td>Bir jumla; tor, keng, kuchli — chiqarib tashlang.</td></tr>"
            "<tr><td>RC detail (32)</td><td>Kalit soʻz → gap → parafraz.</td></tr>"
            "<tr><td>RC function (34)</td><td>Nima uchun — oldingi gap.</td></tr>"
            "<tr><td>RC application / tone (35)</td><td>Mavzusiz tamoyil; baho soʻzlari.</td></tr>"
            "</tbody></table>"
        )},
        {"rich_text": (
            "<h3>Imtihon kuni</h3>"
            + steps([
                "<p><strong>Boʻlimlar tartibi:</strong> GMAT Focusʼda uch boʻlim tartibini <b>oʻzingiz tanlaysiz</b>. Verbalʼni charchamagan paytda "
                "yechish uchun koʻpchilik uni birinchi yoki ikkinchi qoʻyadi — oʻzingizga mosini mock imtihonda sinab koʻring.</p>",
                "<p><strong>Tanaffus:</strong> imtihonda bitta ixtiyoriy 10 daqiqalik tanaffus bor — uni rejalashtiring.</p>",
                "<p><strong>Nazorat nuqtalari:</strong> 15-daqiqa ≈ 8 savol, 30-daqiqa ≈ 15 savol (3-dars).</p>",
                "<p><strong>Javobsiz qoldirmang:</strong> tugallanmagan boʻlim uchun jarima bor — oxirida taxmin bilan belgilang.</p>",
                "<p><strong>Review &amp; Edit:</strong> ikkilangan savolni belgilang; oxirida koʻpi bilan 3 ta javobni faqat aniq xato uchun oʻzgartiring.</p>",
            ])
            + TIP.format("Quant va Data Insights — Prime GMAT kursida (GMAT-1…35). Uchala boʻlim teng ogʻirlikka ega, shuning uchun Verbalʼga "
                         "ham ular kabi jiddiy tayyorlaning.")
        )},
        ask("Assumption savolida variant toʻgʻri ekanini tekshirishning eng ishonchli usuli qaysi?", [
            (True, "Variantni inkor qilib, argument yiqilishini tekshirish", "zaruriy taxmin inkor qilinganda argument yiqiladi (11-dars)."),
            (False, "Variant argumentni qanchalik kuchaytirishini baholash", "kuchaytiruvchi har doim zaruriy emas."),
            (False, "Matndagi soʻzlarni eng koʻp takrorlagan variantni tanlash", "soʻzma-soʻz takror koʻpincha tuzoq."),
            (False, "Eng uzun variantni tanlash", "uzunlik — mezon emas."),
            (False, "Variant haqiqatda rost ekanini tekshirish", "«if true» — rostligi muhokama qilinmaydi."),
        ], "Inkor qilish testi — assumption savolining kaliti."),
        ask("Paradoks (discrepancy) savolida toʻgʻri javob nima qiladi?", [
            (True, "Ikki faktning ikkalasi ham toʻgʻri boʻlishiga imkon beradi", "ikkala tomonni tushuntiradi (23-dars)."),
            (False, "Faktlardan birini notoʻgʻri deb isbotlaydi", "faktlar toʻgʻri deb qabul qilinadi."),
            (False, "Faqat birinchi faktni tushuntiradi", "bir tomonlama — tuzoq."),
            (False, "Ziddiyatni yanada kuchliroq qiladi", "chuqurlashtiruvchi — tuzoq."),
            (False, "Muallifning asosiy xulosasini takrorlaydi", "paradoksda xulosa yoʻq."),
        ], "Ikki faktni bogʻlaydigan yangi fakt."),
        ask("Inference savollarida qaysi turdagi variant koʻpincha toʻgʻri boʻladi?", [
            (False, "Eng kuchli, eng umumiy daʼvoni aytgan variant", "juda kuchli — eng koʻp uchraydigan tuzoq."),
            (True, "Matndan albatta kelib chiqadigan, ehtiyotkor variant", "«some», «at least», «not all» — ehtiyotkor soʻzlar (22, 33)."),
            (False, "Haqiqiy hayotda rost boʻlgan variant", "tashqi bilim hisoblanmaydi."),
            (False, "Matnda yoʻq yangi raqamni keltirgan variant", "matn bermagan maʼlumot."),
            (False, "Muallifning tavsiyasini aytgan variant", "inference faktlardan chiqadi."),
        ], "Eng ehtiyotkor — eng xavfsiz."),
        ask("Boldface savolida birinchi qadam qaysi?", [
            (True, "Muallifning oʻz asosiy xulosasini topish", "rollar xulosaga nisbatan aniqlanadi (24-dars)."),
            (False, "Variantlarni toʻliq oʻqib chiqish", "avval xulosa, keyin variantlar."),
            (False, "Birinchi qalin qismni xulosa deb olish", "koʻpincha u boshqalarning fikri."),
            (False, "Eng uzun qalin qismni topish", "uzunlik — mezon emas."),
            (False, "Argumentdagi raqamlarni yozib olish", "boldfaceʼda raqam muhim emas."),
        ], "«Some critics argue…» — boshqalarniki; «But…» — muallifniki."),
        ask("GMAT Focus Editionʼda boʻlimlar tartibi qanday belgilanadi?", [
            (True, "Nomzod uch boʻlim tartibini oʻzi tanlaydi", "mba.com rasmiy maʼlumoti."),
            (False, "Doim Quant birinchi, Verbal oxirgi", "tartib belgilanmagan."),
            (False, "Doim Verbal birinchi", "tartib belgilanmagan."),
            (False, "Kompyuter tasodifiy tanlaydi", "nomzod tanlaydi."),
            (False, "Nomzod hujjat topshirgan universitet tanlaydi", "universitet tanlamaydi."),
        ], "Tartibni oʻzingiz tanlaysiz — mock imtihonda sinab, oʻzingizga mosini toping."),
        ask("Reading Comprehension matnida «not unlimited», «more modest», «rarely immune» kabi iboralar koʻp. Bu ohang savollari uchun nimani bildiradi?", [
            (True, "Toʻgʻri ohang varianti odatda oʻlchovli boʻladi — matnning kuchiga mos", "35-dars: javobning kuchi matnning kuchiga mos."),
            (False, "Muallif fikrini yashiryapti — ohangni aniqlab boʻlmaydi", "iboralar aynan ohangni koʻrsatadi."),
            (False, "Eng keskin variant toʻgʻri", "keskin variant faqat muallif keskin gapirganda toʻgʻri."),
            (False, "Muallif oʻz fikriga qarshi", "cheklov — qarshilik emas."),
            (False, "Bu iboralar ohang savollariga taʼsir qilmaydi", "taʼsir qiladi."),
        ], "Yumshoq iboralar — oʻlchovli ohang."),
        {"rich_text": (
            "<h3>Oxirgi soʻz</h3>"
            + WARN.format("Imtihondan oldingi kechada yangi narsa oʻrganmang. Shu sahifani oʻqing, bitta Verbal Drillʼni (40 yoki 41) qayta yeching "
                          "va uxlang. Verbalʼda charchoq — eng qimmat xato manbai.")
            + NOTE.format("Bu kursdagi barcha matnlar va argumentlar inglizcha, tushuntirishlar esa oʻzbekcha — imtihonda tushuntirish boʻlmaydi. "
                          "Oxirgi haftada har kuni 15–20 daqiqa inglizcha biznes yoki ilmiy-ommabop maqola oʻqing: RC tezligi shunda oshadi.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("section order", "boʻlimlar tartibi"), ("optional break", "ixtiyoriy tanaffus"), ("Review & Edit", "koʻrib chiqish va tahrir"),
                     ("educated guess", "asosli taxmin"), ("mock exam", "sinov imtihoni")])
            + "<h3>Xulosa</h3><ul><li>Har tur — bitta qoida (jadval).</li><li>Tartibni oʻzingiz tanlang; nazorat nuqtalarini kuzating.</li>"
            "<li>Javobsiz qoldirmang; 3 ta tahrirni aniq xato uchun saqlang.</li><li>Oxirgi kechada — takror va uyqu.</li></ul>"
        )},
    ],
},
]
