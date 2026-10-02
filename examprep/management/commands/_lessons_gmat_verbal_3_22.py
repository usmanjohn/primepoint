# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — lessons 3 (pacing), 13 (CR mixed practice I), 20 (Evaluate),
21 (Flaw) and 22 (Inference). See toc_gmat_verbal.txt and STYLE_GUIDE_GMAT_VERBAL.md.

TRACK, the two first topics and the cr()/ask()/why()/steps()/cards() helpers are loaded
from the first batch file by path (import_examprep loads data files by path, so a
relative import would not work) — one definition, no drift between batches.
"""
import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    "_gmatv_base", os.path.join(os.path.dirname(os.path.abspath(__file__)), "_lessons_gmat_verbal_1_12.py"))
_base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_base)

TRACK = _base.TRACK
TOPIC_STRATEGY, TOPIC_CR = _base.TOPIC_STRATEGY, _base.TOPIC_CR
TIP, WARN, NOTE, EXAMP = _base.TIP, _base.WARN, _base.NOTE, _base.EXAMP
cr, ask, steps, cards = _base.cr, _base.ask, _base.steps, _base.cards

TOPIC_CR2 = {
    "title":   "Critical Reasoning: boshqa savol turlari",
    "summary": "Evaluate, Flaw, Inference, paradoks, rol va reja savollari — har birining oʻz usuli va oʻz tuzoqlari.",
    "icon":    "bi-puzzle",
    "order":   3,
}


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 3 — pacing
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "GMAT Verbal 3: Pacing Verbal — Reading Comprehension Sets and Critical Reasoning",
    "summary": "45 daqiqani 23 savolga taqsimlash: nazorat nuqtalari, Reading Comprehension matnini bir marta oʻqish, taxmin qilish va Review & Edit.",
    "order": 3,
    "blocks": [
        {"rich_text": (
            "<h2>Vaqt — Verbalʼdagi eng jim dushman</h2>"
            "<p>Verbal boʻlimida savollar qiyin boʻlgani uchun emas, <b>bitta savolga yopishib qolgani</b> uchun ball yoʻqotiladi. "
            "Bir argumentga besh daqiqa sarflagan nomzod oxirida toʻrtta savolni oʻqimay belgilaydi. Bu darsda vaqtni "
            "<mark>nazorat nuqtalari</mark> bilan boshqarishni oʻrganamiz.</p>"
            '<span class="sr-time">⏱ 45 daqiqa ÷ 23 savol ≈ 1 daqiqa 57 soniya</span>'
        )},
        {"rich_text": (
            "<h3>Usul: uchta nazorat nuqtasi</h3>"
            + steps([
                "<p><strong>15-daqiqa:</strong> taxminan <mark>8 ta</mark> savol tugagan boʻlsin (15 × 23 ÷ 45 ≈ 7.7).</p>",
                "<p><strong>30-daqiqa:</strong> taxminan <mark>15 ta</mark> savol (30 × 23 ÷ 45 ≈ 15.3).</p>",
                "<p><strong>45-daqiqa:</strong> hammasi javob berilgan. GMAC rasmiy maʼlumotiga koʻra, <b>tugallanmagan boʻlim uchun "
                "ball kamaytiriladi</b> — shuning uchun oxirgi daqiqada qolgan savollarni boʻsh qoldirmang, taxmin bilan belgilang.</p>",
                "<p><strong>Reading Comprehension:</strong> matnni bir marta, lekin diqqat bilan oʻqing va har bir abzasning "
                "<b>vazifasini</b> bir-ikki soʻz bilan eslab qoling (oʻqish xaritasi). Bitta matnga bir nechta savol beriladi — "
                "matnga sarflangan vaqt har bir savolda qaytadi.</p>",
                "<p><strong>Review &amp; Edit:</strong> ikkilangan savolni belgilab (bookmark) keting. Oxirida vaqt qolsa, "
                "koʻpi bilan <b>3 ta</b> javobni oʻzgartirishingiz mumkin — faqat aniq xato topilsa.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna: ikki daqiqa qoidasi</h3>"
            "<p>Siz 9-savoldasiz, soat 2 daqiqa 30 soniyani koʻrsatyapti, va ikkita variant orasida ikkilanyapsiz. Nima qilish kerak?</p>"
            "<p>1) Ikkalasini <b>savol turi</b> bilan yana bir bor solishtiring: «weaken» soʻralganmi — qaysi biri boʻshliqni kengaytiradi? "
            "2) 20 soniyada farq topilmasa, <b>yaxshiroq koʻringanini</b> tanlang va <b>bookmark</b> qiling. 3) Keyingi savolga oʻting. "
            "Bu savolga yana bir daqiqa sarflash, boshqa ikki savolni shoshib yechishga olib keladi.</p>"
            + TIP.format("Har bir savolga «2 daqiqa» chegara qoʻyish shart emas: oson savol 1 daqiqada tugaydi va qiyiniga vaqt beradi. "
                         "Muhimi — nazorat nuqtalarida jadvaldan ortda qolmaslik.")
        )},
        ask("Verbal boʻlimini boshladingiz. 15 daqiqa oʻtganda taxminan nechta savol tugagan boʻlishi kerak?", [
            (False, "Taxminan 3 ta", "juda kam — bu tezlikda boʻlim tugamaydi."),
            (False, "Taxminan 5 ta", "hali ham kam: 5 ta savolga 15 daqiqa — bittasiga 3 daqiqa."),
            (True, "Taxminan 8 ta", "15 × 23 ÷ 45 ≈ 7.7 — demak 8 ga yaqin."),
            (False, "Taxminan 12 ta", "juda tez — bu boʻlimning yarmidan koʻpi."),
            (False, "Taxminan 15 ta", "bu 30-daqiqaning nazorat nuqtasi."),
        ], "Nazorat nuqtasi = oʻtgan daqiqa × 23 ÷ 45."),
        ask("30 daqiqa oʻtdi va siz 12 ta savolga javob berdingiz. Holatingiz qanday?", [
            (True, "Ortdasiz — qolgan 11 savolga bittasiga taxminan 1.4 daqiqa qoldi", "15 ÷ 11 ≈ 1.36 daqiqa; jadval boʻyicha 15 ta tugashi kerak edi."),
            (False, "Jadvaldasiz — hammasi joyida", "30-daqiqada taxminan 15 ta tugagan boʻlishi kerak."),
            (False, "Oldindasiz — sekinlashtirsangiz boʻladi", "aksincha, ortdasiz."),
            (False, "Qolgan savollarni boʻsh qoldirish kerak", "tugallanmagan boʻlim uchun jarima bor."),
            (False, "Hech qanday farqi yoʻq — vaqt ballga taʼsir qilmaydi", "tugallanmagan boʻlim ballni kamaytiradi."),
        ], "Ortda qolganingizni 30-daqiqada bilish — oxirgi 5 daqiqada bilishdan ancha yaxshi."),
        ask("Boʻlim tugashiga 1 daqiqa qoldi, 3 ta savolni hali oʻqimadingiz. Eng toʻgʻri harakat qaysi?", [
            (False, "Birinchisini diqqat bilan yechib, qolgan ikkitasini boʻsh qoldirish", "boʻsh qolgan savollar jarimaga olib keladi."),
            (True, "Uchalasiga ham tez taxmin bilan javob belgilash", "tugallanmagan boʻlim uchun jarima bor; taxmin hech boʻlmasa imkoniyat beradi."),
            (False, "Vaqt tugashini kutish", "eng yomon variant — uchala savol ham javobsiz qoladi."),
            (False, "Oldingi savollarga qaytib, javoblarni oʻzgartirish", "bu vaqtda yangi savollarga javob berish muhimroq."),
            (False, "Boʻlimni qaytadan boshlashni soʻrash", "bunday imkoniyat yoʻq."),
        ], "GMAT Focusʼda javobsiz qolgan savol taxmin bilan belgilangan savoldan qimmatroq turadi."),
        ask("Reading Comprehension matniga yondashishning eng samarali usuli qaysi?", [
            (False, "Matnni oʻqimay, darhol savollarga oʻtish", "bir nechta savol bitta matnga tayanadi — har birida qayta qidirib vaqt yoʻqotasiz."),
            (False, "Har bir soʻzni tarjima qilib, matnni ikki marta oʻqish", "juda sekin."),
            (True, "Matnni bir marta diqqat bilan oʻqib, har abzasning vazifasini qisqa eslab qolish", "bu oʻqish xaritasi — keyingi savollarda kerakli joyni tez topasiz."),
            (False, "Faqat birinchi va oxirgi gapni oʻqish", "tafsilot va xulosa savollarida yetmaydi."),
            (False, "Matnni oxiridan boshiga qarab oʻqish", "mantiqiy tuzilish yoʻqoladi."),
        ], "Matnga sarflangan vaqt — investitsiya: u har bir savolda qaytadi."),
        ask("Question Review & Editʼdan qanday foydalanish kerak?", [
            (False, "Har bir savolga qaytib, javoblarni qayta koʻrib chiqish", "vaqt yetmaydi va faqat 3 ta tahrir mumkin."),
            (True, "Ikkilangan savollarni belgilab, oxirida aniq xato topilsa tuzatish", "3 ta tahrir — faqat aniq xato uchun."),
            (False, "Barcha qiyin savollarni boʻsh qoldirib, oxirida yechish", "har bir savolga javob berib oʻtish kerak."),
            (False, "Undan umuman foydalanmaslik", "foydali vosita — toʻgʻri ishlatilsa."),
            (False, "Faqat birinchi savolga qaytish", "tanlov sizning belgilaringizga bogʻliq."),
        ], "Ikkilanish — sabab emas; aniq xato — sabab."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Mukammallik tuzogʻi</b> — bitta savolni «albatta toʻgʻri» yechish uchun 4 daqiqa sarflash. "
                          "<b>Oxirgi daqiqa vahima</b> — qolgan savollarni boʻsh qoldirish. <b>Qayta oʻqish</b> — RC matnini har savolda boshidan oʻqish.")
            + NOTE.format("Bizdagi koʻp nomzodlar maktab imtihonlaridagi «bilmasang — tashlab ket» odatini olib keladi. "
                          "GMAT Focusʼda bu odat qimmatga tushadi: tashlab ketilgan savol — jarima.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("pacing", "vaqtni taqsimlash"), ("checkpoint", "nazorat nuqtasi"), ("bookmark", "belgilab qoʻymoq"),
                     ("educated guess", "asosli taxmin"), ("reading map", "oʻqish xaritasi"), ("penalty", "jarima")])
            + "<h3>Xulosa</h3><ul><li>15-daqiqa ≈ 8 savol, 30-daqiqa ≈ 15 savol.</li><li>Hech bir savolni boʻsh qoldirmang.</li>"
            "<li>RC matnini bir marta, xarita bilan oʻqing.</li><li>Ikkilansangiz — belgilang va davom eting.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 13 — CR mixed practice I
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR,
    "title": "GMAT Verbal 13: Critical Reasoning — Mixed Practice I",
    "summary": "Birinchi blok boʻyicha aralash mashq: xulosa, taxmin, zaiflashtirish, kuchaytirish, albatta toʻgʻri va rol savollari ketma-ket.",
    "order": 13,
    "blocks": [
        {"rich_text": (
            "<h2>Aralash mashq: savol turini oʻzingiz aniqlang</h2>"
            "<p>Oldingi uch darsda har bir savol turini alohida oʻrgandik. Imtihonda esa ular aralash keladi va birinchi ish — "
            "<b>savol nima soʻrayotganini</b> aniqlash. Quyidagi oltita savol tasodifiy tartibda: har biridan oldin toʻxtab, "
            "turini oʻzingizga ayting.</p>"
            '<span class="sr-time">⏱ Maqsad: 6 savol — 12 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Eslatma: toʻrt qadam</h3>"
            + steps([
                "<p><strong>1.</strong> Savol turi: conclusion · assumption · weaken · strengthen · must be true · role.</p>",
                "<p><strong>2.</strong> Xulosa va dalilni ajrating.</p>",
                "<p><strong>3.</strong> Boʻshliqni oʻz soʻzingiz bilan ayting.</p>",
                "<p><strong>4.</strong> Beshta tuzoq shaklini chiqarib tashlang: mavzudan tashqari, teskari, juda kuchli, dalilni takrorlash, xarajat.</p>",
            ])
            + TIP.format("Har savoldan keyin tahlilni oʻqing — hatto toʻgʻri topgan boʻlsangiz ham. Toʻgʻri javobga <b>toʻgʻri sabab bilan</b> "
                         "kelganingizni tekshirish — keyingi safar ham topishning kafolati.")
        )},
        cr("Many economists argue that raising the minimum wage reduces employment. Yet when the region of Westvale raised its minimum "
           "wage by 15 percent, employment in the region rose slightly over the next two years. The economists' claim, at least in its "
           "general form, is therefore too strong.",
           "Which of the following best states the main conclusion of the argument?", [
            (True, "The economists' general claim that raising the minimum wage reduces employment is too strong.", "«therefore» bilan kelgan baho — qolganlari unga dalil."),
            (False, "Raising the minimum wage increases employment.", "juda kuchli — muallif faqat umumiy daʼvo haddan oshganini aytadi."),
            (False, "Employment in Westvale rose after the minimum wage was raised.", "dalil."),
            (False, "Westvale raised its minimum wage by 15 percent.", "dalil."),
            (False, "Economists should stop studying the minimum wage.", "mavzudan tashqari."),
        ], "Muallif qarshi misol keltirib, umumiy daʼvoni yumshatadi — u teskarisini isbotlamaydi."),
        cr("A software company plans to cut its costs by replacing its customer-support staff with an automated chatbot. The chatbot costs "
           "far less per year than the support team's salaries.",
           "The company's plan to cut its costs depends on which of the following assumptions?", [
            (True, "Using the chatbot will not lead to losses, such as customers leaving, that cost more than the salaries saved.",
             "inkor qilsak: yoʻqotishlar tejamdan katta — umumiy xarajat kamaymaydi, reja yiqiladi."),
            (False, "The chatbot can answer every question that customers ask.", "juda kuchli — koʻp savolga javob bersa ham yetarli boʻlishi mumkin."),
            (False, "Customers prefer chatbots to human support staff.", "shart emas — mijozlar ketmasa yetarli."),
            (False, "Other software companies already use chatbots for customer support.", "mavzudan tashqari."),
            (False, "The support staff can be retrained for other jobs at the company.", "rejaga bogʻliq emas; qayta oʻqitish hatto xarajatni oshiradi."),
        ], "«Arzonroq» va «xarajatni kamaytiradi» — har xil narsa: yashirin yoʻqotishlar boʻshliqda yashaydi."),
        cr("Restaurants that display calorie counts on their menus sell fewer high-calorie dishes than restaurants that do not. So requiring "
           "all restaurants to display calorie counts would reduce the number of high-calorie dishes that restaurant customers order.",
           "Which of the following, if true, most seriously weakens the argument?", [
            (True, "The restaurants that chose to display calorie counts were mostly ones whose customers were already trying to eat fewer calories.",
             "farq kaloriya yozuvidan emas, mijozlardan boʻlishi mumkin — majburiy qilish natija bermasligi mumkin."),
            (False, "Displaying calorie counts costs restaurants very little.", "xarajat — argumentning sabab qismiga taʼsir qilmaydi."),
            (False, "Some customers ignore the calorie counts on menus.", "«baʼzilari» — umumiy kamayish bilan mos keladi."),
            (False, "High-calorie dishes are usually the most profitable dishes for restaurants.", "foyda — mavzudan tashqari."),
            (False, "Calorie counts are already required on menus in some countries.", "boshqa mamlakatlar natijasi aytilmagan — mavzudan tashqari."),
        ], "Ixtiyoriy guruh — vakil emas: oʻzi tanlagan restoranlar boshqalardan farq qilishi mumkin."),
        cr("A city found that on streets where it planted trees, reported burglaries fell by 15 percent the following year. City officials "
           "concluded that the trees helped to deter burglary.",
           "Which of the following, if true, most strengthens the officials' conclusion?", [
            (True, "On streets where no trees were planted, reported burglaries did not fall during the same year.", "taqqoslash guruhi: daraxtsiz koʻchalarda kamayish yoʻq."),
            (False, "The tree planting was paid for by a national grant.", "pul manbasi — mavzudan tashqari."),
            (False, "Residents of the tree-lined streets also installed more security cameras that year.", "boshqa sabab — zaiflashtiradi."),
            (False, "Trees take several years to grow to their full size.", "kuchaytirmaydi — kichik daraxtlar haqida savol tugʻdiradi."),
            (False, "Some of the streets that got trees had very few burglaries to begin with.", "kuchaytirmaydi."),
        ], "Kuchaytirish: sabab yoʻq joyda natija ham yoʻq."),
        cr("At an investment firm, every project manager speaks English, and some project managers also speak Korean. No one at the firm "
           "who speaks Korean works in the accounting department.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "Some project managers do not work in the accounting department.", "koreyscha gapiradigan menejerlar buxgalteriyada ishlamaydi — demak hech boʻlmaganda baʼzilari u yerda emas."),
            (False, "No project manager works in the accounting department.", "koreyscha bilmaydigan menejer u yerda ishlashi mumkin."),
            (False, "Everyone at the firm who speaks English is a project manager.", "teskari yoʻnalish — aytilmagan."),
            (False, "Some people in the accounting department speak Korean.", "matnga zid."),
            (False, "Most project managers speak Korean.", "«some» — «most» emas."),
        ], "«Some» — kamida bitta. Zanjir: baʼzi menejerlar → koreyscha → buxgalteriyada emas."),
        cr("Some say the city's new metro line has failed because it carries fewer riders than planners predicted. But the line opened only "
           "eight months ago, and new metro lines typically take two to three years to reach their full ridership. So it is too early to call "
           "the line a failure.",
           "The claim that new metro lines typically take two to three years to reach their full ridership plays which role in the argument?", [
            (True, "It is offered as support for the argument's conclusion.", "u «hali erta» degan xulosaga dalil."),
            (False, "It is the argument's main conclusion.", "xulosa — «too early to call the line a failure»."),
            (False, "It is the view that the argument opposes.", "qarshi fikr — «the line has failed»."),
            (False, "It is a consideration that the argument concedes weakens its conclusion.", "aksincha — xulosani qoʻllaydi."),
            (False, "It is evidence offered for the view that the line has failed.", "teskari yoʻnalish."),
        ], "Avval xulosani toping, keyin bu gap unga yordam beradimi yoki qarshi turadimi — tekshiring."),
        {"rich_text": (
            "<h3>Natijangizni tahlil qiling</h3>"
            + WARN.format("Agar xato qilgan boʻlsangiz, sababini yozing: <b>savol turini notoʻgʻri oʻqidim</b>, <b>xulosani adashtirdim</b> "
                          "yoki <b>tuzoqqa tushdim</b> (qaysi biriga?). Bir xil sabab ikki marta takrorlansa — oʻsha darsga qayting.")
            + NOTE.format("Oltita savoldan beshtasi — imtihondagi oʻrtacha darajadan yuqori natija. Lekin vaqtga ham qarang: "
                          "12 daqiqadan koʻp ketgan boʻlsa, 2-darsdagi toʻrt qadamni tezlashtirish ustida ishlang.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("too strong", "juda kuchli (haddan oshgan)"), ("self-selected", "oʻzi tanlagan (ixtiyoriy) guruh"),
                     ("counterexample", "qarshi misol"), ("deter", "toʻxtatmoq, qaytarmoq"), ("ridership", "yoʻlovchilar soni")])
            + "<h3>Xulosa</h3><ul><li>Imtihonda savol turlari aralash keladi — avval turini aniqlang.</li>"
            "<li>Har tahlilni oʻqing, toʻgʻri javobda ham.</li><li>Xatolarni sababi boʻyicha guruhlang.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 20 — Evaluate
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 20: Evaluate the Argument — The Question That Would Decide It",
    "summary": "Evaluate savollari: argumentni baholash uchun eng foydali savolni topish va «ha / yoʻq» testi.",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Qaysi savolga javob argumentni hal qiladi?</h2>"
            "<p>Evaluate savolida sizdan argumentni zaiflashtirish ham, kuchaytirish ham soʻralmaydi. Soʻraladi: "
            "«<i>Which of the following would it be most useful to know in order to evaluate the argument?</i>» — yaʼni, "
            "<mark>qaysi maʼlumot</mark> argument toʻgʻri yoki notoʻgʻri ekanini koʻrsatib beradi?</p>"
            "<p>Toʻgʻri javob har doim <b>boʻshliq haqidagi savol</b>. Uning bir javobi argumentni kuchaytiradi, ikkinchisi — zaiflashtiradi.</p>"
            '<span class="sr-time">⏱ Evaluate — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: «ha / yoʻq» testi</h3>"
            + steps([
                "<p><strong>1.</strong> Xulosa, dalil va boʻshliqni toping — oddiy CR savoli kabi.</p>",
                "<p><strong>2.</strong> Har bir variantni savolga aylantiring: «Whether…» → «…mi?»</p>",
                "<p><strong>3.</strong> Ikkala javobni sinang: <b>«ha»</b> boʻlsa argumentga nima boʻladi? <b>«yoʻq»</b> boʻlsa-chi?</p>",
                "<p><strong>4.</strong> Toʻgʻri variantda ikki javob argumentni <mark>qarama-qarshi tomonlarga</mark> suradi. "
                "Ikkala javobda ham argument oʻzgarmasa — variant befoyda.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>To reduce litter in Central Park, the town council plans to double the number of rubbish bins there. '
            "Council members point out that the park's paths are often covered with wrappers and bottles.</p></div>"
            "<p>Variant: «Whether most of the litter is dropped by people who are far from any existing bin». "
            "<b>Ha</b> — odamlar axlat qutisi uzoq boʻlgani uchun tashlaydi → koʻproq quti yordam beradi (kuchayadi). "
            "<b>Yoʻq</b> — ular quti yonida ham tashlaydi → qutilar soni muammo emas (zaiflashadi). Ikki tomonga suradi — toʻgʻri javob.</p>"
            "<p>Variant: «How much the new bins will cost». Qimmat yoki arzon — axlat kamayishiga taʼsir qilmaydi. Befoyda.</p>"
            + TIP.format("Evaluate variantlari koʻpincha «Whether…», «How many…», «What percentage…» bilan boshlanadi. "
                         "Har birini qisqa savolga aylantirib, ikki javobni tez sinang.")
        )},
        cr("A gym chain found that members who attend its yoga classes renew their memberships at a higher rate than members who do not. "
           "The chain's managers conclude that offering more yoga classes would increase the overall renewal rate.",
           "Which of the following would it be most useful to know in order to evaluate the managers' conclusion?", [
            (True, "Whether members who take yoga classes differ from other members in ways, such as how often they visit the gym, that are themselves linked to renewing",
             "«ha» — farq boshqa sababdan (zaiflashadi); «yoʻq» — yoga sabab boʻlishi ehtimoli oshadi (kuchayadi)."),
            (False, "Whether yoga classes are more popular than spinning classes at the gym", "mashhurlik — sababni hal qilmaydi."),
            (False, "How much the chain pays its yoga instructors", "xarajat — yangilanish darajasiga taʼsir qilmaydi."),
            (False, "Whether some members who never attend yoga classes renew their memberships", "albatta baʼzilari yangilaydi — hech narsani hal qilmaydi."),
            (False, "Whether yoga has health benefits that other forms of exercise lack", "salomatlik — mavzudan tashqari."),
        ], "Bogʻliqlikdan sabab chiqarilgan joyda eng foydali savol: «guruhlar boshqa jihatdan farq qiladimi?»"),
        cr("To reduce litter in Central Park, the town council plans to double the number of rubbish bins there. Council members point out "
           "that the park's paths are often covered with wrappers and bottles.",
           "Which of the following would it be most useful to know in order to evaluate the council's plan?", [
            (True, "Whether most of the litter in the park is dropped by people who are far from any existing bin", "«ha» — reja ishlaydi; «yoʻq» — qutilar muammo emas."),
            (False, "Whether the bins will be emptied by city workers or by volunteers", "kim boʻshatishi — reja natijasini hal qilmaydi."),
            (False, "How much the new bins will cost", "xarajat — maqsadga yetishni koʻrsatmaydi."),
            (False, "Whether the park is busier in summer than in winter", "mavsum — ikkala javob ham rejaga taʼsir qilmaydi."),
            (False, "Whether parks in other towns are larger than Central Park", "boshqa shaharlar — mavzudan tashqari."),
        ], "Reja + evaluate: «rejaning taxmini toʻgʻrimi?» degan savolni qidiring."),
        cr("Our new interview process selects better employees. Of the 40 people hired under it, 90 percent received a good first-year review, "
           "compared with 70 percent of the people hired under the old process.",
           "Which of the following would it be most useful to know in order to evaluate the argument?", [
            (True, "Whether the standards used in first-year reviews were the same for both groups of employees",
             "«yoʻq» — baholash yumshagan boʻlsa farq jarayondan emas (zaiflashadi); «ha» — taqqoslash adolatli (kuchayadi)."),
            (False, "Whether the new interview process takes longer than the old one", "vaqt — sifatni hal qilmaydi."),
            (False, "Who designed the new interview process", "kim ishlab chiqqani — natijani baholamaydi."),
            (False, "Whether the interviewers enjoyed using the new process", "mavzudan tashqari."),
            (False, "Whether the company plans to use the new process in its overseas offices", "kelajak rejasi — argumentni baholamaydi."),
        ], "Ikki guruh solishtirilganda: «oʻlchov bir xilmi?» — klassik evaluate savoli."),
        cr("In one farming region, farmers who switched to drip irrigation saw their water use fall by 30 percent. Therefore, if every farmer in "
           "the region switched, the region's total agricultural water use would fall by about 30 percent.",
           "Which of the following would it be most useful to know in order to evaluate the argument?", [
            (True, "Whether the farmers who have already switched grow the same kinds of crops, on similar land, as the farmers who have not",
             "«ha» — natijani umumlashtirish mumkin; «yoʻq» — qolganlarda tejam boshqacha boʻlishi mumkin."),
            (False, "Whether drip irrigation systems are manufactured in the region", "ishlab chiqarish joyi — mavzudan tashqari."),
            (False, "Whether the price of drip irrigation equipment has fallen recently", "narx — tejam miqdorini hal qilmaydi."),
            (False, "Whether some farmers who switched were unhappy with the new system", "noroziliq — suv sarfiga taʼsir qilmaydi."),
            (False, "Whether the region exports most of its crops", "eksport — mavzudan tashqari."),
        ], "Bir guruhdan butun hududga umumlashtirish — vakillik savoli."),
        cr("Since the city introduced a fee for plastic bags, the number of bags handed out by its supermarkets has fallen by 60 percent. The fee "
           "has therefore greatly reduced the amount of plastic waste the city produces.",
           "Which of the following would it be most useful to know in order to evaluate the argument?", [
            (True, "Whether shoppers have replaced the free bags with other plastic products, such as thicker bags or bin liners, that they now buy",
             "«ha» — plastik chiqindi kamaymagan boʻlishi mumkin; «yoʻq» — xulosa kuchayadi."),
            (False, "Whether the fee is the same in every supermarket in the city", "narx farqi — umumiy chiqindini hal qilmaydi."),
            (False, "How the money collected from the fee is spent", "pulning ishlatilishi — mavzudan tashqari."),
            (False, "Whether the city's supermarkets supported the introduction of the fee", "qoʻllab-quvvatlash — natijaga taʼsir qilmaydi."),
            (False, "Whether bag fees have been introduced in other countries", "boshqa mamlakatlar — mavzudan tashqari."),
        ], "Dalil — «paketlar kamaydi», xulosa — «plastik chiqindi kamaydi». Boʻshliq: oʻrnini boshqa plastik egallamadimi?"),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Bir tomonlama savol</b> — javobi qanday boʻlmasin argument oʻzgarmaydi (xarajat, mashhurlik, boshqa shaharlar). "
                          "<b>«Some» savoli</b> — «baʼzilari … mi?» deyarli har doim «ha», shuning uchun hech narsani hal qilmaydi.")
            + NOTE.format("Evaluate — weaken va strengthenʼning birlashmasi. Agar variantning «yoʻq» javobi argumentni zaiflashtirsa va "
                          "«ha» javobi kuchaytirsa, siz toʻgʻri yoʻldasiz.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("evaluate", "baholamoq"), ("most useful to know", "bilish eng foydali boʻlgan"), ("whether", "… -mi (yoki yoʻqmi)"),
                     ("generalise", "umumlashtirmoq"), ("comparable", "solishtirsa boʻladigan"), ("drip irrigation", "tomchilatib sugʻorish")])
            + "<h3>Xulosa</h3><ul><li>Evaluate — boʻshliq haqidagi savol.</li><li>Har variantni «ha / yoʻq» bilan sinang.</li>"
            "<li>Ikkala javob argumentni qarama-qarshi tomonga sursa — toʻgʻri javob.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 21 — Flaw
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 21: Flaw Questions — The Classic Reasoning Errors",
    "summary": "Mantiqiy xatolar: bogʻliqlik va sabab, foiz va son, zarur va yetarli shart, vakil boʻlmagan namuna, shaxsga hujum.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Argument qayerda xato qiladi?</h2>"
            "<p>Flaw savoli: «<i>The argument is most vulnerable to criticism on the grounds that it…</i>». Bu yerda boʻshliqni "
            "faqat topish emas, uni <b>abstrakt tilda nomlash</b> kerak. Variantlar «It takes for granted that…», «It fails to consider…», "
            "«It treats … as …» kabi umumiy iboralar bilan yoziladi. Bir necha klassik xato qayta-qayta keladi — ularni tanib olsangiz, "
            "savol tez yechiladi.</p>"
            '<span class="sr-time">⏱ Flaw — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Beshta klassik xato</h3>"
            + steps([
                "<p><strong>Bogʻliqlik → sabab.</strong> Ikki narsa birga uchraydi, demak biri ikkinchisini keltirib chiqaradi.</p>",
                "<p><strong>Foiz → son.</strong> «200% oʻsdi» — lekin boshlangʻich son kichik boʻlsa, natija ham kichik.</p>",
                "<p><strong>Zarur → yetarli.</strong> «Lavozim uchun X kerak; unda X bor — demak lavozimni oladi.» Zarur shart kafolat emas.</p>",
                "<p><strong>Vakil boʻlmagan namuna.</strong> Velosiped jurnali oʻquvchilari — butun aholi emas.</p>",
                "<p><strong>Shaxsga hujum.</strong> Fikrni emas, uni aytgan odamni tanqid qilish.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>Sales of electric cars in Country P rose by 200 percent last year, while sales of petrol cars rose by '
            "only 5 percent. Clearly, more electric cars than petrol cars were sold in Country P last year.</p></div>"
            "<p>Agar oʻtgan yili 1,000 ta elektromobil va 100,000 ta benzinli mashina sotilgan boʻlsa: elektromobillar 3,000 ga yetadi "
            "(+200%), benzinli mashinalar 105,000 ga (+5%). Foiz katta, son esa kichik. Xato — <mark>faqat foiz oʻzgarishidan sonlar haqida "
            "xulosa chiqarish</mark>.</p>"
            + TIP.format("Avval xatoni <b>oʻz soʻzingiz</b> bilan ayting («foizdan son chiqardi»), keyin variantlarni abstrakt tildan oʻz "
                         "tilingizga tarjima qilib solishtiring.")
        )},
        cr("Cities with more coffee shops per resident have higher average incomes than cities with fewer. So opening more coffee shops would "
           "be a good way for a city to raise its residents' incomes.",
           "The argument is most vulnerable to criticism on the grounds that it", [
            (True, "takes for granted that because two things occur together, one of them causes the other",
             "bogʻliqlik → sabab: balki yuqori daromad koʻproq qahvaxonani keltirib chiqargan."),
            (False, "relies on a sample of cities that is too small to be meaningful", "namuna hajmi aytilmagan — asos yoʻq."),
            (False, "assumes that what is true of a city as a whole is true of each resident", "argument oʻrtacha daromad haqida gapiradi."),
            (False, "attacks the people who hold a view rather than the view itself", "hech kimga hujum yoʻq."),
            (False, "treats a necessary condition for higher incomes as a sufficient one", "zarur shart haqida gap yoʻq."),
        ], "Teskari sabab ham mumkin: boy shaharlarda qahvaxonalar koʻp ochiladi."),
        cr("Sales of electric cars in Country P rose by 200 percent last year, while sales of petrol cars rose by only 5 percent. Clearly, more "
           "electric cars than petrol cars were sold in Country P last year.",
           "The reasoning in the argument is flawed because the argument", [
            (True, "infers a conclusion about numbers of cars from information only about percentage changes", "boshlangʻich sonlar nomaʼlum."),
            (False, "takes for granted that rising sales of one product cause falling sales of another", "benzinli mashina savdosi tushmagan."),
            (False, "draws a conclusion about a country from a sample of only a few buyers", "namuna haqida gap yoʻq."),
            (False, "rejects a claim because of who made it", "shaxsga hujum yoʻq."),
            (False, "assumes the very conclusion it sets out to prove", "dalil va xulosa har xil narsa."),
        ], "Foiz oʻzgarishi — nisbiy; son haqida xulosa uchun boshlangʻich son kerak."),
        cr("To be promoted to senior analyst at the firm, an employee must have passed the CFA Level I exam. Aziz has passed the CFA Level I exam, "
           "so he will be promoted to senior analyst.",
           "Which of the following most accurately describes a flaw in the argument?", [
            (True, "It treats a requirement for promotion as though it guaranteed promotion.", "zarur shart → yetarli shart."),
            (False, "It takes for granted that two things that occur together are causally related.", "bogʻliqlik haqida gap yoʻq."),
            (False, "It infers a number from a percentage.", "foiz yoʻq."),
            (False, "It generalises from one employee to all employees of the firm.", "aksincha — umumiy qoidadan bitta odamga."),
            (False, "It relies on a source that may be biased.", "manba keltirilmagan."),
        ], "«Must have» — zarur shart. Imtihondan oʻtish eshikni ochadi, lekin kafolat bermaydi."),
        cr("An online poll on the website of a cycling magazine found that 78 percent of respondents support building more bike lanes. So most "
           "of the country's residents support building more bike lanes.",
           "The argument is most vulnerable to criticism on the grounds that it", [
            (True, "draws a conclusion about a whole population from a group that is unlikely to be typical of it", "velosiped jurnali oʻquvchilari — vakil emas."),
            (False, "confuses a percentage of respondents with a number of respondents", "xulosa ham ulush haqida — «most»."),
            (False, "takes for granted that bike lanes are inexpensive to build", "narx haqida hech narsa taxmin qilinmagan."),
            (False, "treats a necessary condition as a sufficient one", "shart haqida gap yoʻq."),
            (False, "fails to state how many bike lanes the country already has", "bu maʼlumot xulosani hal qilmaydi."),
        ], "Soʻrovnoma xulosasi — namuna aholiga oʻxshaydi degan taxminga tayanadi."),
        cr("The consultant's report recommends closing the company's factory in Fergana. But the consultant has never run a factory herself, so "
           "the recommendation should be rejected.",
           "The reasoning in the argument is flawed because it", [
            (True, "rejects a recommendation because of a fact about the person who made it rather than the reasons given for it", "shaxsga hujum."),
            (False, "takes for granted that the factory is profitable", "foyda haqida taxmin yoʻq."),
            (False, "generalises from too few cases", "umumlashtirish yoʻq."),
            (False, "infers a number from a percentage", "foiz yoʻq."),
            (False, "assumes that two events that occur together are causally linked", "bogʻliqlik yoʻq."),
        ], "Tavsiyani uning dalillari bilan baholash kerak — muallifning tajribasi bilan emas."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Rost, lekin xato emas</b> — «it fails to state how many bike lanes…» — argument haqiqatan aytmaydi, lekin "
                          "bu uning xatosi emas. Flaw varianti argument <b>qilgan</b> notoʻgʻri qadamni nomlashi kerak. "
                          "<b>Boshqa xato</b> — boshqa argumentga mos keladigan, bu yerda yoʻq xato.")
            + NOTE.format("Abstrakt tildagi variantlarni oʻqishda bizdagi nomzodlar koʻp qiynaladi. Har birini argumentning oʻz soʻzlariga "
                          "«qaytaring»: «a requirement» — CFA imtihoni, «guaranteed» — lavozimni olishi. Mos kelsa — toʻgʻri.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("flaw", "mantiqiy xato"), ("vulnerable to criticism", "tanqidga ochiq"), ("takes for granted", "isbotsiz qabul qiladi"),
                     ("necessary condition", "zarur shart"), ("sufficient condition", "yetarli shart"), ("ad hominem", "shaxsga hujum"),
                     ("representative", "vakil, tipik")])
            + "<h3>Xulosa</h3><ul><li>Beshta klassik xatoni yod biling.</li><li>Xatoni avval oʻz soʻzingiz bilan ayting.</li>"
            "<li>Abstrakt variantni argumentning oʻz soʻzlariga qaytaring.</li><li>Rost, lekin xato boʻlmagan variantdan saqlaning.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 22 — Inference
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 22: Inference — What Must Be True",
    "summary": "Inference savollari: faqat matndagi faktlardan albatta kelib chiqadigan xulosa; «some / all», foiz va son tuzoqlari.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Matndan nima albatta kelib chiqadi?</h2>"
            "<p>Inference savolida argument yoʻq — faqat <b>faktlar</b>. Savol: «<i>If the statements above are true, which of the following "
            "must also be true?</i>» yoki yumshoqroq «<i>most strongly supported</i>». Bu yerda boshqa savol turlarining qoidasi teskari ishlaydi: "
            "<mark>eng ehtiyotkor, eng tor</mark> variant gʻolib chiqadi.</p>"
            '<span class="sr-time">⏱ Inference — ~1.5–2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>1.</strong> Faktlarni qisqa yozing va ularni <b>bogʻlang</b>: qaysi ikki fakt birga yangi narsa beradi?</p>",
                "<p><strong>2.</strong> «All», «some», «no», «only» soʻzlariga qarang — ular nimani aytadi va nimani aytmaydi.</p>",
                "<p><strong>3.</strong> Foiz va son farqi: <b>son oshdi, ulush tushdi</b> → umumiy son oshgan boʻlishi shart.</p>",
                "<p><strong>4.</strong> Har bir variantga savol: «Faktlar rost, bu esa yolgʻon boʻlishi mumkinmi?» Mumkin boʻlsa — chiqarib tashlang.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>Last year, Company R\'s revenue rose by 10 percent, while its profit fell.</p></div>'
            "<p>Foyda = tushum − xarajat. Tushum oshdi, foyda tushdi — demak xarajat <b>tushumdan koʻproq miqdorda</b> oshgan. "
            "Bu albatta toʻgʻri. «Kompaniya kamroq mahsulot sotdi» esa shart emas: narx oshgan boʻlishi mumkin. "
            "«Kompaniya zarar koʻrdi» — ham shart emas: foyda kamaygan, lekin musbat qolgan boʻlishi mumkin.</p>"
            + TIP.format("Inferenceʼda «juda kuchli» variant — eng koʻp uchraydigan tuzoq. «Must be true» uchun «some», «at least», "
                         "«not all» kabi yumshoq soʻzlar koʻpincha toʻgʻri javob belgisi.")
        )},
        cr("Every branch of Bank Q that opened before 2015 offers safe-deposit boxes to its customers. Bank Q's branch in Namangan does not offer "
           "safe-deposit boxes to its customers.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "Bank Q's Namangan branch opened in 2015 or later.", "2015 dan oldin ochilgan boʻlsa, qutilar boʻlardi — demak 2015 yoki undan keyin."),
            (False, "The Namangan branch opened sometime after 2020.", "juda aniq — 2015–2020 ham mumkin."),
            (False, "No branch of Bank Q that opened after 2015 offers safe-deposit boxes.", "yangi filiallar haqida hech narsa aytilmagan."),
            (False, "Most branches of Bank Q offer safe-deposit boxes.", "filiallar soni nomaʼlum."),
            (False, "The Namangan branch is Bank Q's newest branch.", "aytilmagan."),
        ], "«Hamma A — B; bu B emas → bu A emas». A = «2015 dan oldin ochilgan»."),
        cr("Last year, Company R's revenue rose by 10 percent, while its profit fell. Company R's profit is the difference between its revenue and "
           "its costs.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "Company R's costs rose last year by a larger amount than its revenue did.", "foyda = tushum − xarajat; tushum oshib, foyda tushsa — xarajat koʻproq oshgan."),
            (False, "Company R sold fewer products last year than the year before.", "narx oshgan boʻlishi mumkin — shart emas."),
            (False, "Company R made a loss last year.", "foyda kamaygan, lekin musbat qolishi mumkin."),
            (False, "Company R raised the prices of its products last year.", "shart emas — koʻproq sotgan boʻlishi mumkin."),
            (False, "Company R's competitors also saw their profits fall last year.", "raqobatchilar haqida maʼlumot yoʻq."),
        ], "Formula bilan oʻylang: ΔFoyda = ΔTushum − ΔXarajat < 0 → ΔXarajat > ΔTushum."),
        cr("In the city of Termez, every bus that runs after 10 p.m. is an electric bus. Some of the buses on Route 7 run after 10 p.m., and the "
           "rest run only during the day.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "Some of the buses on Route 7 are electric.", "kechqurun yuradiganlari elektr — ular 7-yoʻnalishda bor."),
            (False, "All of the buses on Route 7 are electric.", "kunduzgilari haqida hech narsa aytilmagan."),
            (False, "Some buses that run only during the day are not electric.", "mumkin, lekin shart emas."),
            (False, "Route 7 has more electric buses than any other route.", "boshqa yoʻnalishlar haqida maʼlumot yoʻq."),
            (False, "No buses on other routes run after 10 p.m.", "aytilmagan."),
        ], "«All» kechki avtobuslar haqida; «some» 7-yoʻnalish haqida. Ikkalasining kesishmasi — «some … are electric»."),
        cr("A survey of 2,000 small businesses found that firms that accepted card payments had, on average, higher monthly sales than firms that "
           "accepted only cash. However, firms that began accepting cards during the survey period saw no change in their sales.",
           "The statements above most strongly support which of the following?", [
            (True, "Accepting card payments was not, by itself, the main reason the card-accepting firms had higher sales.",
             "karta qabul qila boshlaganlarda savdo oʻzgarmadi — farq boshqa sababdan."),
            (False, "Accepting card payments reduces a firm's sales.", "savdo oʻzgarmagan — kamaymagan."),
            (False, "Most small businesses accept card payments.", "ulush aytilmagan."),
            (False, "Customers prefer to pay in cash rather than by card.", "afzallik haqida maʼlumot yoʻq."),
            (False, "Firms that accept card payments will see their sales fall if they stop.", "kelajak haqida — qoʻllab-quvvatlanmaydi."),
        ], "«Most strongly supported» — ham faktlarga tayanish kerak, lekin biroz yumshoqroq. Eng ehtiyotkor variant gʻolib."),
        cr("This year, the number of students at Samarkand Business School who chose the finance major rose, while the share of the school's "
           "students who chose finance fell.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "The total number of students at the school rose this year.", "son oshdi, ulush tushdi — umumiy son oshgan boʻlishi shart."),
            (False, "Fewer students chose finance than chose marketing.", "marketing haqida maʼlumot yoʻq."),
            (False, "The number of students choosing majors other than finance fell.", "aksincha — ular oshgan boʻlishi kerak."),
            (False, "The school added new majors this year.", "mumkin, lekin shart emas."),
            (False, "Most students at the school chose finance.", "ulush aytilmagan."),
        ], "Ulush = son ÷ jami. Surat oshib, kasr kichraysa — maxraj oshgan."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Juda kuchli</b> («all», «most», «after 2020»). <b>Mumkin, lekin shart emas</b> — «some buses that run only during "
                          "the day are not electric». <b>Tashqi bilim</b> — «customers prefer cash» — dunyoda rost boʻlishi mumkin, matnda yoʻq.")
            + NOTE.format("Oʻzbek tilida «baʼzi» koʻpincha «hammasi emas» degan maʼnoni ham beradi. GMAT mantiqida <b>some = kamida bitta</b>, "
                          "va «some» hammasini ham qamrab olishi mumkin. Shu farq koʻp savolni hal qiladi.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("inference", "xulosa (matndan)"), ("must be true", "albatta toʻgʻri"), ("most strongly supported", "eng kuchli qoʻllab-quvvatlangan"),
                     ("share", "ulush"), ("revenue", "tushum"), ("profit", "foyda"), ("at least one", "kamida bitta")])
            + "<h3>Xulosa</h3><ul><li>Faqat matndagi faktlar — tashqi bilim yoʻq.</li><li>Faktlarni bogʻlang: yangi narsa ikki fakt kesishmasida.</li>"
            "<li>Son va ulush farqini kuzating.</li><li>Eng ehtiyotkor variant koʻpincha toʻgʻri.</li></ul>"
        )},
    ],
},
]
