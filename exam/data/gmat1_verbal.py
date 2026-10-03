# -*- coding: utf-8 -*-
"""GMAT Focus Edition — PrimePoint Mock 1 — Verbal Reasoning (23 questions, 45 min).

Rules: exam/data/STYLE_GUIDE_GMAT_MOCK.md. Five choices; English material, Uzbek
explanations (result page only). Critical Reasoning 1–11, Reading Comprehension 12–23
(four passages, three questions each; each RC question carries its passage so it shows
beside the question, as on the real screen).

RC subjects (true facts): the honeybee waggle dance (von Frisch; robotic-bee and
harmonic-radar studies; Nobel 1973) · QWERTY and path dependence (Paul David 1985;
Liebowitz & Margolis 1990; the 1940s Navy study supervised by Dvorak) · the marshmallow
test (Mischel, Stanford; Watts et al. 2018, about 900 children) · Kodak and the first
digital camera (Sasson 1975: about 3.6 kg, 0.01 megapixels, 23 seconds per image;
Chapter 11 in January 2012). CR settings are invented and say so by their names.
Answer gate: verify_gmat_mock1_verbal.py (scratchpad).

    python manage.py load_mock exam/data/gmat1_verbal.py --expect-questions=23
"""

EXAM_META = {
    'title': 'GMAT Focus Edition — PrimePoint Mock 1',
    'language': 'english',
    'exam_format': 'gmat',
    'exam_number': 301,
    'is_published': True,
}

MODULES = [
    {'code': 'quant', 'kind': 'quant', 'stage': 1, 'order': 1, 'minutes': 45,
     'label': 'Quantitative Reasoning', 'label_uz': 'Miqdoriy mulohaza'},
    {'code': 'verbal', 'kind': 'verbal', 'stage': 1, 'order': 2, 'minutes': 45,
     'label': 'Verbal Reasoning', 'label_uz': 'Ogʻzaki mulohaza'},
    {'code': 'di', 'kind': 'di', 'stage': 1, 'order': 3, 'minutes': 45, 'calculator': True,
     'label': 'Data Insights', 'label_uz': 'Maʼlumotlar tahlili'},
]

CR_SA = 'CR — Structure and Assumptions'
CR_SW = 'CR — Strengthen and Weaken'
CR_IP = 'CR — Inference and Paradox'
RC_MS = 'RC — Main Idea and Structure'
RC_D = 'RC — Detail'
RC_IA = 'RC — Inference and Application'


def why(rows):
    """rows: (is_key, choice_text, uzbek_reason). The key is named by its opening words."""
    out = []
    for ok, text, reason in rows:
        words = text.split()
        opening = ' '.join(words[:8]) + ('…' if len(words) > 8 else '')
        mark = '✔' if ok else '✘'
        out.append(f'<li>{mark} <strong>{opening}</strong> — {reason}</li>')
    return '<ul>' + ''.join(out) + '</ul>'


# Where each key sits (1 = A … 5 = E). The exam engine shows choices in file order, so the
# key's position is set here, spread evenly across A–E and never the same three times running.
KEY_POS = [3, 1, 4, 2, 5, 2, 4, 1, 3, 5, 1, 4, 2, 5, 3, 2, 5, 1, 4, 3, 5, 2, 4]


def item(number, skill, difficulty, passage, stem, rows, lead):
    key = next(r for r in rows if r[0])
    others = [r for r in rows if not r[0]]
    rows = others[:KEY_POS[number - 1] - 1] + [key] + others[KEY_POS[number - 1] - 1:]
    choices = [t for _, t, _ in rows]
    correct = next(i for i, (ok, _, _) in enumerate(rows, start=1) if ok)
    return {'section': 'verbal', 'number': number, 'skill': skill, 'difficulty': difficulty,
            'passage': passage, 'question_text': f'<p><strong>{stem}</strong></p>',
            'choices': choices, 'correct': correct,
            'explanation': f'<p>{lead}</p>' + why(rows)}


def para(*ps):
    return ''.join(f'<p>{p}</p>' for p in ps)


# ── Reading Comprehension passages ───────────────────────────────────────────
P_BEES = para(
    "In the 1940s the Austrian zoologist Karl von Frisch set out to answer a question that beekeepers had asked "
    "for centuries: how does a honeybee that has found a rich patch of flowers tell other bees in its colony where "
    "the flowers are? By marking bees with paint and watching them on glass-walled hives, he found that a returning "
    "forager performs a “waggle dance” on the vertical comb. The bee runs a short straight line while shaking its "
    "abdomen, loops back, and repeats. The angle of the straight run relative to vertical matches the angle between "
    "the direction of the food and the direction of the sun, and the duration of each waggle run increases with the "
    "distance to the food.",
    "The claim met resistance. Some researchers argued that bees found food by smell alone and that the dance, "
    "however striking, carried no information that other bees actually used. The debate lasted decades. It was "
    "largely settled by experiments that separated the dance from other cues: studies in which a robotic bee "
    "performed a dance that researchers could control, and, later, studies that tracked individual bees with "
    "harmonic radar and showed that bees that had followed a dance flew toward the location it indicated.",
    "Von Frisch shared the 1973 Nobel Prize in Physiology or Medicine with Konrad Lorenz and Nikolaas Tinbergen. "
    "His work is often cited as one of the clearest cases of symbolic communication outside humans: the dance does "
    "not point at the food; it encodes the food's position in a convention that the audience must interpret.",
)

P_QWERTY = para(
    "The QWERTY keyboard, named after the first six letters of its top row of letters, was developed for "
    "typewriters in the 1870s. In 1985 the economist Paul David used it to illustrate an idea he called path "
    "dependence: a technology that becomes standard early can remain standard long after better alternatives "
    "appear, because users, manufacturers and training schools have all invested in it. As evidence that QWERTY was "
    "inferior, David cited the Dvorak keyboard, patented in 1936, and a 1940s United States Navy study reporting "
    "that typists retrained on Dvorak became far faster.",
    "In 1990 the economists Stan Liebowitz and Stephen Margolis challenged the story. They pointed out that the "
    "Navy study had been supervised by August Dvorak himself, the inventor of the rival layout, and that later, "
    "more carefully controlled studies found little or no advantage for Dvorak. If the alternative was not clearly "
    "better, they argued, QWERTY's survival showed not that markets become trapped by early accidents but simply "
    "that switching was not worth its cost.",
    "The disagreement is about more than keyboards. Path dependence remains a useful idea — few economists doubt "
    "that early choices can shape later ones — but the QWERTY case shows how easily a vivid example can carry an "
    "argument further than its evidence. A story that everyone knows deserves the same scrutiny as any other claim.",
)

P_MARSHMALLOW = para(
    "In the late 1960s and early 1970s, the psychologist Walter Mischel and his colleagues at Stanford University "
    "offered young children a choice: one treat now, or two treats if they could wait, alone, for up to about "
    "fifteen to twenty minutes. Follow-up studies years later reported that the children who had waited longer "
    "tended, as teenagers, to have higher test scores and to be described by their parents as more competent. The "
    "“marshmallow test” became one of the best-known experiments in psychology, often cited as evidence that "
    "self-control in early childhood shapes success later in life.",
    "The original follow-up samples, however, were small and drawn mainly from the children of Stanford staff and "
    "students. In 2018 a team led by Tyler Watts repeated the analysis with a larger and more varied group of about "
    "900 children. They found that the link between waiting and later achievement was about half as strong as in "
    "the original reports, and that it shrank much further, and was no longer statistically significant, once they "
    "took account of factors such as family background and the children's early cognitive ability.",
    "The replication does not show that self-control is unimportant. It suggests something narrower: that a few "
    "minutes of waiting at age four may reveal less about a particular child's future than the famous version of "
    "the story implied, and that some of what the test seemed to measure may reflect the circumstances in which "
    "children grow up.",
)

P_KODAK = para(
    "In 1975 Steve Sasson, a young engineer at Eastman Kodak, built what is often described as the first digital "
    "camera. It weighed about 3.6 kilograms, recorded black-and-white images of 0.01 megapixels, and took 23 seconds "
    "to store a single picture on a cassette tape. Kodak's managers were interested but cautious. The company earned "
    "most of its profits not from cameras but from film, paper and processing, and a camera that needed no film "
    "threatened that business.",
    "It is tempting to tell the story of Kodak's later decline as one of managers who failed to see the future. "
    "The record is more complicated. Kodak did invest in digital technology: it held many important digital-imaging "
    "patents, and in the mid-2000s it was for a time one of the largest sellers of digital cameras in the United "
    "States. Its difficulty was less a failure to see digital photography coming than the absence of a digital "
    "business that could replace the profits of film. Digital cameras sold at thin margins, and once photographs "
    "moved to phones and the internet, few people printed them at all.",
    "Kodak filed for bankruptcy protection in January 2012. Business schools still teach the case, but its most "
    "useful lesson is not simply to invent the future, because Kodak did. The harder lesson is that a company can "
    "see a new technology clearly and still have no profitable way to live in the world it creates.",
)


QUESTIONS = [
    # ═══ Critical Reasoning ═══════════════════════════════════════════════
    item(1, CR_SA, 'easy',
         para("Orders at FreshCart, an online grocer, rose by 40 percent after the company began offering free "
              "delivery on orders over $30. FreshCart's managers therefore conclude that offering free delivery on all "
              "orders, whatever their size, will increase the company's profits."),
         "The managers' conclusion depends on which of the following assumptions?", [
            (True, "The profit earned on the additional small orders will be greater than the cost of delivering them free.",
             "inkor qilsak: kichik buyurtmalarni bepul yetkazish ulardan keladigan foydadan qimmat — foyda oshmaydi."),
            (False, "Most of FreshCart's customers already place orders larger than $30.",
             "shart emas — xulosa kichik buyurtmalar haqida."),
            (False, "FreshCart's competitors do not offer free delivery.",
             "raqobatchilar — mavzudan tashqari."),
            (False, "Free delivery is the main reason customers choose FreshCart.",
             "juda kuchli — asosiy sabab boʻlishi shart emas."),
            (False, "The 40 percent rise in orders came mostly from new customers.",
             "buyurtma kimdan kelgani foyda haqidagi xulosani hal qilmaydi."),
         ], "Dalil — buyurtmalar soni oshgan; xulosa — <b>foyda</b> oshadi. Boʻshliq: koʻproq buyurtma = koʻproq foyda deb olinyapti."),

    item(2, CR_SA, 'easy',
         para("To reduce absences, a hospital will pay a bonus to every nurse who misses no shifts in a three-month "
              "period. Since most of the hospital's nurses say that pay is their main concern at work, the hospital's "
              "managers expect the bonus to reduce absences substantially."),
         "The managers' expectation depends on which of the following assumptions?", [
            (True, "Most absences at the hospital are not caused by illnesses or emergencies that nurses cannot avoid.",
             "inkor qilsak: yoʻqliklar asosan oldini olib boʻlmaydigan sabablardan — bonus ularni kamaytira olmaydi."),
            (False, "The bonus will be larger than the bonuses paid by other hospitals.",
             "boshqa kasalxonalar bilan solishtirish shart emas."),
            (False, "Nurses who miss shifts are paid less than other nurses.",
             "mavzudan tashqari."),
            (False, "The hospital can afford to pay the bonus to every nurse.",
             "xarajat — rejaning maqsadga yetishini hal qilmaydi."),
            (False, "Some nurses will still miss shifts after the bonus is introduced.",
             "bu xulosaga zid emas — «sezilarli kamayish» bilan mos keladi; zaruriy taxmin emas."),
         ], "Reja yoʻqlikni <b>ixtiyoriy</b> deb hisoblaydi: pul tanlovga taʼsir qiladi, kasallikka emas."),

    item(3, CR_SA, 'medium',
         para("Every one of the five fastest-growing technology startups in the city last year rented office space in "
              "the new co-working center on Navoi Street. Clearly, any startup in the city that wants to grow quickly "
              "should rent space there."),
         "The argument is most vulnerable to criticism on the grounds that it", [
            (True, "fails to consider whether many slow-growing startups also rent space in the co-working center",
             "taqqoslash guruhi yoʻq: markazda sekin oʻsayotganlar ham koʻp boʻlsa, markaz sabab emas."),
            (False, "assumes that rents at the co-working center will remain affordable",
             "argument narx haqida emas."),
            (False, "relies on the opinions of the startups' founders",
             "matnda fikr soʻrovi yoʻq."),
            (False, "draws a conclusion about all cities from evidence about one city",
             "xulosa faqat shu shahar haqida."),
            (False, "assumes that the five startups will keep growing next year",
             "kelajakdagi oʻsish xulosaga kerak emas."),
         ], "Faqat muvaffaqiyatlilarga qarash — klassik xato: umumiy xususiyat sabab ekanini isbotlamaydi."),

    item(4, CR_SA, 'medium',
         para("<b>Some economists argue that raising the tax on cigarettes will not reduce smoking among adults, "
              "because adult smokers are addicted and will pay whatever cigarettes cost.</b> Yet when Country R raised "
              "its cigarette tax by a third, adult cigarette purchases fell by nearly a tenth within a year, and "
              "surveys found that fewer adults were smoking. <b>Price, it seems, does matter even to addicted smokers.</b>"),
         "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is a position that the argument rejects; the second is the argument's main conclusion.",
             "birinchisi — muallif qarshi chiqqan iqtisodchilar fikri; ikkinchisi — «it seems» bilan kelgan xulosa."),
            (False, "The first is the argument's main conclusion; the second is evidence that supports it.",
             "teskari — muallif birinchi fikrga qarshi."),
            (False, "The first is a position that the argument rejects; the second is evidence offered against that position.",
             "ikkinchisi dalil emas — R mamlakati maʼlumotidan chiqarilgan xulosa."),
            (False, "The first is evidence that the argument accepts; the second qualifies that evidence.",
             "muallif birinchi fikrni qabul qilmaydi."),
            (False, "The first and the second are both conclusions that the argument rejects.",
             "ikkinchisi muallifning oʻz xulosasi."),
         ], "Avval muallifning xulosasini toping: «Yet…» dan keyingi dalil va «Price… does matter» — xulosa."),

    item(5, CR_SA, 'hard',
         para("A city plans to reduce accidents on its ring road by lowering the speed limit there from 80 to 60 "
              "kilometers per hour. City officials point out that on a similar road in a neighboring city, accidents "
              "fell by a quarter in the year after its speed limit was lowered in the same way."),
         "Which of the following would it be most useful to know in order to evaluate the officials' plan?", [
            (True, "Whether other changes that could reduce accidents, such as new lighting or traffic cameras, were introduced on the neighboring city's road at the same time",
             "«ha» — kamayish boshqa sababdan, dalil zaiflashadi; «yoʻq» — tezlik chegarasi sabab boʻlishi ehtimoli oshadi."),
            (False, "Whether the ring road is longer than the neighboring city's road",
             "uzunlik avariyalar ulushining kamayishini hal qilmaydi."),
            (False, "How many residents of the city own cars",
             "javobi qanday boʻlmasin reja baholanmaydi."),
            (False, "Whether the new speed limit will be announced in local newspapers",
             "eʼlon usuli — mavzudan tashqari."),
            (False, "How much the new speed-limit signs will cost",
             "xarajat — maqsadga yetishni koʻrsatmaydi."),
         ], "Evaluate: «ha» va «yoʻq» javoblari argumentni qarama-qarshi tomonga suradigan savol."),

    item(6, CR_SW, 'easy',
         para("Sales of electric scooters in Tashkent tripled last year. A scooter-rental company concludes that "
              "demand for scooter rentals in the city will grow strongly next year."),
         "Which of the following, if true, most seriously weakens the company's conclusion?", [
            (True, "Most of the scooters sold last year were bought by people who had regularly rented scooters and no longer need to.",
             "sotib olganlar — ijarachilar edi; ijaraga talab kamayishi mumkin."),
            (False, "Electric scooters are much cheaper to run than cars.",
             "umumiy qiziqish — zaiflashtirmaydi."),
            (False, "Several cities in Europe have banned scooters from pavements.",
             "boshqa shaharlar — mavzudan tashqari."),
            (False, "The rental company plans to add 200 scooters to its fleet.",
             "kompaniya rejasi talabni koʻrsatmaydi."),
            (False, "Sales of electric scooters also rose in Samarkand last year.",
             "boshqa shahar — xulosaga taʼsir qilmaydi."),
         ], "Sotuv oʻsishi = ijaraga talab oʻsishi degan boʻshliq: sotib olgan odam ijaraga olmaydi."),

    item(7, CR_SW, 'medium',
         para("In a study, office workers who took a fifteen-minute walk after lunch made fewer errors in afternoon "
              "tasks than workers who stayed at their desks. The researchers concluded that a short walk after lunch "
              "improves accuracy in the afternoon."),
         "Which of the following, if true, most strengthens the researchers' conclusion?", [
            (True, "The workers in the study were randomly assigned either to walk or to stay at their desks.",
             "tasodifiy taqsimlash — guruhlar avvaldan farq qilmaydi; farq yurishdan."),
            (False, "Walking regularly is known to be good for the heart.",
             "yurak salomatligi — aniqlik haqidagi xulosaga taʼsir qilmaydi."),
            (False, "Some workers who walked still made errors in the afternoon.",
             "«baʼzilari» — oʻrtacha farqni rad ham, tasdiq ham etmaydi."),
            (False, "Workers who stayed at their desks said that they preferred to rest after lunch.",
             "afzallik — sabab haqida hech narsa demaydi."),
            (False, "The study was carried out during the summer.",
             "fasl — mavzudan tashqari."),
         ], "Bogʻliqlikdan sabab chiqarilganda eng kuchli dalil — guruhlar oʻzi tanlamagani."),

    item(8, CR_SW, 'hard',
         para("To attract more young customers, a bank plans to open a branch inside the city's largest university, "
              "where 30,000 students study. Most of the university's students do not yet have an account with any bank."),
         "Which of the following, if true, most strongly suggests that the bank's plan will NOT achieve its goal?", [
            (True, "Students at the university can open an account with any of several banks entirely through a phone app, and most students who open accounts do it this way.",
             "talabalar filialga kelmaydi — filial yoshlarni jalb qilish vositasi boʻlmaydi."),
            (False, "Renting space at the university will cost more than renting space for the bank's other branches.",
             "xarajat — maqsadga yetishni rad etmaydi."),
            (False, "Some students at the university already have accounts with other banks.",
             "«baʼzilari» — koʻpchilikda hisob yoʻq."),
            (False, "The university is closed for two months every summer.",
             "vaqtinchalik — maqsadni rad etmaydi."),
            (False, "Young people often keep the same bank for many years.",
             "aksincha, rejani kuchaytiradi."),
         ], "Reja savolida: maqsadga yetishni toʻsadigan fakt — xarajat yoki «baʼzilar» emas."),

    item(9, CR_IP, 'medium',
         para("At Firm T, every employee in the research department has a doctorate. No employee of Firm T who has a "
              "doctorate is paid less than $90,000 a year. Some employees in Firm T's sales department are paid less "
              "than $90,000 a year."),
         "If the statements above are true, which of the following must also be true?", [
            (True, "Some employees in the sales department do not have a doctorate.",
             "90,000 dan kam olayotgan sotuvchilarda doktorlik boʻlishi mumkin emas."),
            (False, "No employee in the sales department has a doctorate.",
             "juda kuchli — koʻp maosh oladigan sotuvchida doktorlik boʻlishi mumkin."),
            (False, "Every employee paid more than $90,000 works in the research department.",
             "teskari yoʻnalish — aytilmagan."),
            (False, "Employees in the research department are paid more than employees in the sales department.",
             "barcha sotuvchilar haqida maʼlumot yoʻq."),
            (False, "Most employees with a doctorate work in the research department.",
             "ulush aytilmagan."),
         ], "Zanjir: doktorlik → kamida 90,000. Demak 90,000 dan kam → doktorlik yoʻq."),

    item(10, CR_IP, 'medium',
         para("Last year a supermarket chain cut the prices of its own-brand products by 10 percent, and its sales of "
              "those products, measured in units, rose by 25 percent. Yet the chain's total profit from its own-brand "
              "products fell."),
         "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "Before the price cut, most own-brand products were sold at a margin so small that the 10 percent cut made them unprofitable.",
             "har bir sotuv zarar keltirsa, koʻproq sotuv — koʻproq zarar: ikkala fakt ham toʻgʻri."),
            (False, "Shoppers buy more own-brand products when their prices fall.",
             "faqat savdo oʻsishini tushuntiradi."),
            (False, "The chain also cut the prices of the branded products it sells.",
             "brendli mahsulotlar — oʻz brendi foydasini tushuntirmaydi."),
            (False, "Sales of branded products at the chain fell last year.",
             "boshqa mahsulot — mavzudan tashqari."),
            (False, "The chain's own-brand products are made by outside suppliers.",
             "kim ishlab chiqarishi — foydani tushuntirmaydi."),
         ], "Paradoks: savdo oshdi, foyda tushdi — har bir birlikdan keladigan foyda haqida fakt kerak."),

    item(11, CR_IP, 'hard',
         para("On the Riverline railway, every train that leaves Port Elm for Hilltown before 9 a.m. is an express. "
              "Every express on that route stops only at Hilltown. Last Tuesday, the 8:15 train from Port Elm stopped "
              "at Millbrook."),
         "If the statements above are true, which of the following must also be true?", [
            (True, "Last Tuesday's 8:15 train from Port Elm was not a train to Hilltown.",
             "Hilltownga 9 dan oldin ketadigan har bir poyezd — ekspress, ekspress faqat Hilltownda toʻxtaydi; Millbrookda toʻxtagani — u Hilltown poyezdi emas."),
            (False, "The 8:15 train from Port Elm is an express.",
             "teskari — ekspress boshqa joyda toʻxtamaydi."),
            (False, "No express on the Riverline railway stops at Millbrook.",
             "faqat shu yoʻnalishdagi ekspresslar haqida aytilgan."),
            (False, "Some trains from Port Elm to Hilltown leave after 9 a.m.",
             "aytilmagan."),
            (False, "The 8:15 train from Port Elm was late last Tuesday.",
             "kechikish haqida maʼlumot yoʻq."),
         ], "«Hamma A — B; B faqat X da toʻxtaydi; bu poyezd Y da toʻxtadi» → u A emas."),

    # ═══ Reading Comprehension — passage 1: the waggle dance ═════════════════
    item(12, RC_MS, 'medium', P_BEES, "The primary purpose of the passage is to", [
            (True, "describe a discovery about animal communication and explain how a challenge to it was resolved",
             "uchala abzas: kashfiyot, eʼtiroz va uning hal qilinishi, ahamiyati."),
            (False, "argue that honeybees rely mainly on smell to find food",
             "bu rad etilgan qarash."),
            (False, "compare the work of three winners of the Nobel Prize",
             "Lorenz va Tinbergen faqat eslatilgan."),
            (False, "explain how harmonic radar works",
             "juda tor — bitta tafsilot."),
            (False, "criticize the methods von Frisch used in his experiments",
             "muallif tanqid qilmaydi."),
         ], "Asosiy maqsad butun matnni qamraydi: kashfiyot → bahs → hal qilinishi."),

    item(13, RC_D, 'easy', P_BEES, "According to the passage, the duration of each waggle run indicates", [
            (True, "how far away the food is",
             "1-abzas: «duration… increases with the distance to the food»."),
            (False, "the direction of the food relative to the sun",
             "bu yugurish burchagi bilan bildiriladi."),
            (False, "how much food the patch of flowers contains",
             "aytilmagan."),
            (False, "how many bees should fly to the food",
             "aytilmagan."),
            (False, "the time of day at which the food was found",
             "aytilmagan."),
         ], "Tafsilot: burchak — yoʻnalish, davomiylik — masofa."),

    item(14, RC_IA, 'hard', P_BEES,
         "It can be inferred from the passage that the robotic-bee experiments helped to settle the debate because they", [
            (True, "allowed researchers to change the dance while other cues, such as smell, stayed the same",
             "«experiments that separated the dance from other cues» — raqsni boshqarish mumkin edi."),
            (False, "proved that honeybees cannot detect smells",
             "juda kuchli — hid qobiliyati rad etilmagan."),
            (False, "showed that bees dance only on vertical combs",
             "aytilmagan."),
            (False, "were the first experiments that von Frisch carried out",
             "von Frisch 1940-yillarda boshqa usul bilan ishlagan."),
            (False, "persuaded the Nobel committee to award von Frisch the prize",
             "mukofot 1973-yilda, robot tajribalari keyinroq."),
         ], "Xulosa: raqsni boshqa belgilardan ajratish — bahsni hal qilgan narsa."),

    # ═══ Reading Comprehension — passage 2: QWERTY ═══════════════════════════
    item(15, RC_IA, 'medium', P_QWERTY,
         "The author mentions that the Navy study was supervised by August Dvorak primarily in order to", [
            (True, "suggest that the study's findings may have been biased",
             "raqobatdosh klaviatura ixtirochisi oʻz ixtirosini sinagan."),
            (False, "show that the Navy preferred the Dvorak keyboard",
             "dengiz floti afzalligi aytilmagan."),
            (False, "explain how the Dvorak layout was designed",
             "dizayn tasvirlanmagan."),
            (False, "support Paul David's claim that QWERTY was inferior",
             "aksincha — Davidning dalilini zaiflashtiradi."),
            (False, "illustrate the idea of path dependence",
             "bu tafsilot dalilning ishonchliligi haqida."),
         ], "Funksiya: tafsilot qaysi daʼvoga xizmat qiladi — Liebowitz va Margolis eʼtiroziga."),

    item(16, RC_MS, 'medium', P_QWERTY, "Which of the following best describes the organization of the passage?", [
            (True, "An example used to support a theory is described, a challenge to the example is presented, and a lesson about evidence is drawn.",
             "1-abzas — misol, 2-abzas — eʼtiroz, 3-abzas — saboq."),
            (False, "A theory is proposed, tested, and then rejected entirely.",
             "nazariya rad etilmagan — «remains a useful idea»."),
            (False, "Two keyboard designs are compared, and one of them is recommended.",
             "tavsiya yoʻq."),
            (False, "A historical event is described, and its causes are listed in order of importance.",
             "sabablar roʻyxati yoʻq."),
            (False, "A study is summarized, and its methods are praised.",
             "aksincha — usullar shubha ostiga olinadi."),
         ], "Tuzilish: har abzas vazifasini ketma-ket ayting."),

    item(17, RC_IA, 'hard', P_QWERTY, "Liebowitz and Margolis would most likely agree with which of the following?", [
            (True, "When an alternative technology offers little or no advantage, continuing to use the existing standard can be a sensible choice.",
             "«switching was not worth its cost» — ularning asosiy fikri."),
            (False, "The Dvorak keyboard is significantly faster than QWERTY.",
             "ular aksincha deydi."),
            (False, "Markets are often trapped by early accidents.",
             "bu Davidning tezisiga yaqin — ular rad etadi."),
            (False, "No technology should become a standard early in its history.",
             "aytilmagan va juda kuchli."),
            (False, "The Navy study was more reliable than the later studies.",
             "teskari."),
         ], "Qoʻllash: ularning dalilidan umumiy tamoyil — almashtirish foydadan qimmat boʻlsa, eski standart oqilona."),

    # ═══ Reading Comprehension — passage 3: the marshmallow test ═════════════
    item(18, RC_D, 'easy', P_MARSHMALLOW,
         "According to the passage, the 2018 study differed from the original follow-up studies in that it", [
            (True, "used a larger and more varied group of children",
             "2-abzas: «a larger and more varied group of about 900 children»."),
            (False, "offered the children a choice among three treats",
             "aytilmagan."),
            (False, "tested the children when they were teenagers",
             "aytilmagan."),
            (False, "was carried out at Stanford University",
             "aytilmagan — Stanford asl tadqiqot."),
            (False, "found no link at all between waiting and achievement before any adjustment",
             "aksincha — dastlab bogʻliqlik yarim kuchda bor edi."),
         ], "Tafsilot: farqni bevosita aytgan gapni toping."),

    item(19, RC_IA, 'medium', P_MARSHMALLOW,
         "It can be inferred from the passage that the original follow-up studies may have overstated the link between waiting and later success partly because", [
            (True, "the children in them came from similar backgrounds that could themselves affect later achievement",
             "asosan Stanford xodimlari farzandlari + oila sharoiti hisobga olinganda bogʻliqlik kichraydi."),
            (False, "the children were too young to understand the choice",
             "aytilmagan."),
            (False, "the treats were not attractive enough to tempt the children",
             "aytilmagan."),
            (False, "the follow-up studies were carried out too soon after the test",
             "aytilmagan — oʻsmirlik yoshida."),
            (False, "the researchers did not record how long each child waited",
             "kutish vaqti aynan oʻlchangan."),
         ], "Ikki faktni birlashtiramiz: tor tanlov + oila sharoiti hisobga olinganda taʼsir yoʻqolishi."),

    item(20, RC_MS, 'hard', P_MARSHMALLOW,
         "The author's attitude toward the famous conclusion drawn from the marshmallow test can best be described as", [
            (True, "qualified skepticism",
             "«does not show that self-control is unimportant… something narrower» — cheklangan shubha."),
            (False, "complete acceptance",
             "muallif xulosani toraytiradi."),
            (False, "outright rejection",
             "juda kuchli — oʻzini nazorat qilish muhim emas demaydi."),
            (False, "indifference",
             "muallif aniq pozitsiyada."),
            (False, "uncritical enthusiasm",
             "teskari."),
         ], "Ohang: baho soʻzlari va cheklovlar — «narrower», «may reveal less»."),

    # ═══ Reading Comprehension — passage 4: Kodak ════════════════════════════
    item(21, RC_MS, 'medium', P_KODAK, "Which of the following best states the main point of the passage?", [
            (True, "Kodak's decline came less from failing to foresee digital photography than from lacking a profitable business in it.",
             "2-abzas va oxirgi gap — matnning asosiy fikri."),
            (False, "Kodak's managers refused to invest in digital technology.",
             "matnga zid — Kodak sarmoya kiritgan."),
            (False, "Steve Sasson's camera was too heavy to be sold.",
             "juda tor."),
            (False, "Business schools no longer teach the Kodak case.",
             "matnga zid."),
            (False, "Phones had made digital cameras unnecessary by the mid-1970s.",
             "xato vaqt — telefonlar ancha keyin."),
         ], "Asosiy fikr mashhur hikoyani («kelajakni koʻrmadi») tuzatadi."),

    item(22, RC_D, 'easy', P_KODAK,
         "According to the passage, why were Kodak's managers cautious about the digital camera in 1975?", [
            (True, "Most of the company's profits came from film, paper and processing, which a filmless camera threatened.",
             "1-abzas oxiri."),
            (False, "The camera could record only color images.",
             "aksincha — oq-qora."),
            (False, "Sasson left the company soon after building it.",
             "aytilmagan."),
            (False, "Kodak had already sold its digital-imaging patents.",
             "aytilmagan."),
            (False, "Digital cameras were already common at the time.",
             "matnga zid — birinchi kamera."),
         ], "Tafsilot: «cautious» soʻzidan keyingi gapda sabab."),

    item(23, RC_IA, 'hard', P_KODAK,
         "Which of the following situations is most similar to Kodak's difficulty as the author describes it?", [
            (True, "A newspaper builds a popular free website but cannot earn from it what its printed edition used to earn.",
             "yangi texnologiyani koʻrdi va qurdi, lekin daromadi eski biznesni almashtira olmadi."),
            (False, "A firm ignores a new technology until a rival has taken its customers.",
             "bu muallif rad etgan mashhur hikoya."),
            (False, "A company invents a product that is too heavy for customers to carry.",
             "mavzuga oʻxshash, tamoyil boshqa."),
            (False, "A bank opens branches in a city with too few customers.",
             "boshqa tamoyil."),
            (False, "An inventor patents a device but never builds it.",
             "Kodak qurgan va sotgan."),
         ], "Qoʻllash: tamoyil — «koʻrish yetarli emas, foydali biznes kerak»."),
]
