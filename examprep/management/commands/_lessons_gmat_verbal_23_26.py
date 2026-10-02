# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — lessons 23 (Explain the Discrepancy), 24 (Role and Boldface),
25 (Plans and Methods of Reasoning) and 26 (Critical Reasoning mixed practice II).
See toc_gmat_verbal.txt and STYLE_GUIDE_GMAT_VERBAL.md.

TRACK, the topics and the helpers are loaded by path from the earlier batch files
(TOPIC_CR2 was first defined in _lessons_gmat_verbal_3_22.py).

Boldface / role answer choices share their first half ("The first is …; the second is …"),
so their autopsies name each choice IN FULL — crf() below instead of cr(), whose labels
stop at seven words and would leave two rows looking identical.
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
_b2 = _load("_lessons_gmat_verbal_3_22.py")

TRACK = _b1.TRACK
TOPIC_CR, TOPIC_CR2 = _b1.TOPIC_CR, _b2.TOPIC_CR2
TIP, WARN, NOTE = _b1.TIP, _b1.WARN, _b1.NOTE
cr, steps, cards = _b1.cr, _b1.steps, _b1.cards


def why_full(rows):
    out = ['<div class="sr-why">']
    for ok, choice, reason in rows:
        kind, tag = ('ok', 'TO‘G‘RI') if ok else ('no', 'TUZOQ')
        out.append(f'<div class="sr-why__row sr-why__row--{kind}"><span class="sr-why__tag">{tag}</span>'
                   f'<span class="sr-why__text"><b>{choice}</b> — {reason}</span></div>')
    out.append('</div>')
    return ''.join(out)


def crf(passage, stem, rows, lead, time="⏱ ~2 daqiqa"):
    """cr() with every choice named in full in the autopsy (for boldface/role choices)."""
    return {
        "rich_text": (f'<div class="sr-passage"><p>{passage}</p></div>'
                      f'<p><strong>{stem}</strong></p><span class="sr-time">{time}</span>'),
        "choices": [{"text": t, "is_correct": ok} for ok, t, _ in rows],
        "explanation": f"<p>{lead}</p>" + why_full(rows),
    }


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 23 — Explain the discrepancy
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 23: Explain the Discrepancy — Resolving a Paradox",
    "summary": "Paradoks savollari: bir-biriga zid koʻringan ikki faktni birdaniga tushuntiradigan variantni topish.",
    "order": 23,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki fakt bir-biriga zid koʻrinadi</h2>"
            "<p>Bu savol turida argument yoʻq — <b>ikki fakt</b> bor, va ular birga kutilmagan manzara beradi: kampaniya chekuvchilarni "
            "kamaytirdi, lekin sigaret savdosi oshdi. Savol: «<i>Which of the following, if true, most helps to resolve the apparent "
            "discrepancy?</i>» Sizning vazifangiz — <mark>ikkala fakt ham toʻgʻri boʻlishiga</mark> imkon beradigan yangi faktni topish.</p>"
            '<span class="sr-time">⏱ Paradoks — ~1.5–2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>1.</strong> Ikki faktni alohida yozing: «A boʻldi» va «lekin B boʻldi».</p>",
                "<p><strong>2.</strong> Nima uchun ular zid koʻrinishini oʻzingizga ayting: «A boʻlsa, B ning teskarisini kutardik, chunki…»</p>",
                "<p><strong>3.</strong> Shu «chunki» dagi yashirin taxminni toping — toʻgʻri javob odatda aynan uni buzadi.</p>",
                "<p><strong>4.</strong> Har bir variantni tekshiring: u <b>ikkala</b> faktni tushuntiradimi? Faqat bittasini tushuntirsa yoki "
                "ziddiyatni chuqurlashtirsa — tuzoq.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>Company W\'s sales rose by 25 percent last year, but its share of the market fell.</p></div>'
            "<p>Nima uchun zid koʻrinadi? Savdo oshsa, ulush ham oshadi deb kutamiz — <b>bozor oʻzgarmagan</b> deb taxmin qilsak. "
            "Shu taxminni buzadigan fakt: «Bozor bir yilda 25 foizdan koʻproq oʻsdi.» Endi ikkala fakt ham toʻgʻri: Company W oʻsdi, "
            "lekin bozor undan tezroq oʻsdi.</p>"
            + TIP.format("Paradoks savollarida «if true» yana muhim: variant gʻalati boʻlsa ham, uni rost deb olib, ikki faktni tushuntirishini tekshiring.")
        )},
        cr("Despite a national campaign that persuaded many people in Country K to quit smoking, the number of cigarettes sold in Country K rose last year.",
           "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "Among people in Country K who continued to smoke, the average number of cigarettes smoked per day rose sharply last year.",
             "chekuvchilar kamaydi, lekin har biri koʻproq chekdi — ikkala fakt ham toʻgʻri."),
            (False, "The campaign was the most successful anti-smoking campaign in Country K's history.", "ziddiyatni chuqurlashtiradi."),
            (False, "Many people who quit smoking said that the campaign had influenced their decision.", "faqat birinchi faktni tasdiqlaydi."),
            (False, "Cigarette prices in Country K are set by the government.", "narx kim belgilashi — savdo oʻsishini tushuntirmaydi."),
            (False, "Some smokers in Country K buy their cigarettes in neighbouring countries.", "chetdan sotib olish ichki savdoni kamaytiradi — ziddiyat chuqurlashadi."),
        ], "«Kamroq odam» va «koʻproq mahsulot» — ikkalasini «bir kishiga koʻproq» birlashtiradi."),
        cr("Bank V introduced a mobile app that lets its customers deposit cheques without visiting a branch. Yet in the year after the app was "
           "introduced, the number of customer visits to Bank V's branches rose.",
           "Which of the following, if true, most helps to explain the rise in branch visits?", [
            (True, "The app attracted many new customers to Bank V, and every new customer must visit a branch once to verify their identity.",
             "yangi mijozlar oqimi — ilova ishlasa ham, tashriflar oshadi."),
            (False, "Most of the customers who use the app are under 40 years old.", "yosh — tashriflar oshishini tushuntirmaydi."),
            (False, "Other banks have introduced similar apps.", "boshqa banklar — mavzudan tashqari."),
            (False, "The app makes depositing a cheque much faster than visiting a branch.", "ziddiyatni chuqurlashtiradi."),
            (False, "Branch staff were trained to tell customers about the app.", "tashriflar oshishini tushuntirmaydi."),
        ], "Paradoksni koʻpincha «yangi guruh» hal qiladi: eski mijozlar kamroq keldi, yangilari esa kelishga majbur."),
        cr("In Region M, the number of reported cases of a certain disease rose by 40 percent in the two years after a new hospital opened there, "
           "even though doctors agree that the disease itself did not become more common in the region.",
           "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "The new hospital offers a test for the disease that was not previously available anywhere in Region M.",
             "kasallik koʻpaymagan — faqat koʻproq aniqlanmoqda."),
            (False, "The new hospital employs many doctors who trained in other regions.", "shifokorlar kelib chiqishi — tushuntirmaydi."),
            (False, "The disease is more common among older people than among younger people.", "yosh tarkibi oʻzgargani aytilmagan."),
            (False, "The new hospital cost more to build than was originally planned.", "narx — mavzudan tashqari."),
            (False, "The disease can be treated effectively if it is diagnosed early.", "davolash — qayd etilgan holatlar sonini tushuntirmaydi."),
        ], "«Qayd etilgan holat» va «haqiqiy holat» — har xil narsa. Ular orasidagi farq — aniqlash imkoniyati."),
        cr("Company W makes kitchen appliances and sells them in several countries. Its sales rose by 25 percent last year, but its share of the market for kitchen appliances fell.",
           "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "The total market for kitchen appliances grew by more than 25 percent last year.", "bozor kompaniyadan tezroq oʻsdi — ulush tushdi."),
            (False, "Company W raised the prices of its products last year.", "narx oshishi ulush tushishini tushuntirmaydi."),
            (False, "Sales at Company W's largest competitor fell last year.", "ziddiyatni chuqurlashtiradi."),
            (False, "Company W spent more on advertising last year than the year before.", "faqat savdo oʻsishini tushuntiradi."),
            (False, "Company W's profits also rose last year.", "foyda — ulush haqida hech narsa demaydi."),
        ], "Ulush = kompaniya savdosi ÷ bozor. Surat 25% oshdi, kasr tushdi — maxraj koʻproq oshgan."),
        cr("Studies show that people who work at standing desks burn more calories during the working day than people who sit. Yet employees at Firm D "
           "who switched to standing desks did not, on average, lose any weight over the following year.",
           "Which of the following, if true, most helps to explain why the employees did not lose weight?", [
            (True, "After switching to standing desks, the employees tended to eat more and exercise less outside working hours than they had before.",
             "ish vaqtida koʻproq kaloriya, ishdan tashqarida kamroq — muvozanat saqlandi."),
            (False, "Standing desks cost more than ordinary desks.", "narx — mavzudan tashqari."),
            (False, "Some employees at Firm D chose not to switch to standing desks.", "ular tahlilda emas — oʻtganlar haqida gap."),
            (False, "Standing burns more calories than sitting does.", "birinchi faktni takrorlaydi — ziddiyat qoladi."),
            (False, "Employees who switched said they liked the standing desks.", "yoqishi — vaznni tushuntirmaydi."),
        ], "Bir joyda yoqilgan kaloriya boshqa joyda qaytarilsa — natija oʻzgarmaydi."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Chuqurlashtiruvchi</b> — ziddiyatni yana kuchliroq qiladi («kampaniya eng muvaffaqiyatlisi edi»). "
                          "<b>Bir tomonlama</b> — faqat bitta faktni tushuntiradi («reklama koʻpaydi» → savdo oshdi, lekin ulush?). "
                          "<b>Takrorlovchi</b> — faktlardan birini qaytadan aytadi.")
            + NOTE.format("Bu savol turida «nega?» deb soʻrash tabiiy, va bizning nomzodlar koʻpincha oʻzlari bilgan «haqiqiy» sababni "
                          "variantlardan qidiradi. GMATʼda toʻgʻri javob koʻpincha kutilmagan, lekin <b>mantiqan yetarli</b> fakt.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("discrepancy", "nomuvofiqlik, ziddiyat"), ("paradox", "paradoks"), ("resolve", "hal qilmoq"),
                     ("market share", "bozor ulushi"), ("reported cases", "qayd etilgan holatlar"), ("apparent", "koʻrinadigan, zohiriy")])
            + "<h3>Xulosa</h3><ul><li>Ikki faktni yozing va ularning ziddiyatini oʻz soʻzingiz bilan ayting.</li>"
            "<li>Ziddiyat ortidagi yashirin taxminni toping.</li><li>Toʻgʻri javob ikkala faktni ham tushuntiradi.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 24 — Role and boldface
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 24: Role and Boldface Questions",
    "summary": "Qalin harf (boldface) savollari: argumentning ikki qismi qanday rol oʻynashini aniqlash — xulosa, dalil, qarshi fikr, tushuntirish.",
    "order": 24,
    "blocks": [
        {"rich_text": (
            "<h2>Har bir gap nima ish qiladi?</h2>"
            "<p>Boldface savolida argumentning bir yoki ikki qismi <b>qalin harf</b> bilan ajratilgan, va variantlar ularning "
            "<mark>rolini</mark> tasvirlaydi: «The first is … ; the second is …». 10-darsdagi argument anatomiyasi shu yerda toʻliq ishga tushadi.</p>"
            "<p>Bu savollar uzun va abstrakt koʻrinadi, lekin aslida ularning kaliti bitta: <b>muallifning asosiy xulosasi qaysi?</b> "
            "Uni topsangiz, har bir qismni unga nisbatan joylashtirasiz.</p>"
            '<span class="sr-time">⏱ Boldface — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>1.</strong> Qalin qismlarga qaramay, argumentni oʻqing va <b>muallifning</b> asosiy xulosasini toping. "
                "Ehtiyot boʻling: argument boshida koʻpincha <i>boshqalarning</i> fikri turadi («Some analysts predict…»).</p>",
                "<p><strong>2.</strong> Har bir qalin qismni belgilang: <mark>X</mark> — muallifning xulosasi, <mark>D</mark> — unga dalil, "
                "<mark>Q</mark> — muallif qarshi chiqqan fikr yoki uning dalili, <mark>T</mark> — tushuntirish.</p>",
                "<p><strong>3.</strong> Avval <b>birinchi</b> qism boʻyicha variantlarni chiqarib tashlang, keyin qolganlarini <b>ikkinchi</b> qism boʻyicha.</p>",
                "<p><strong>4.</strong> «Fact» va «view» farqiga qarang: muallif faktni rad etmaydi — undan boshqalar chiqargan xulosani rad etadi.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p><b>A new study claims that drinking two cups of green tea a day lowers the risk of heart disease.</b> '
            "The study, however, compared tea drinkers with people who drink no tea without considering that the tea drinkers in its sample "
            "also exercised more. <b>So the study does not show that green tea itself lowers the risk.</b></p></div>"
            "<p>Muallifning xulosasi — «So…» dan keyingi gap: tadqiqot isbotlamaydi. Demak <b>ikkinchi</b> qism = X. "
            "<b>Birinchi</b> qism — tadqiqotning daʼvosi, muallif uni shubha ostiga qoʻyadi = Q. Toʻgʻri variant: "
            "«The first is a claim that the argument calls into question; the second is the argument's main conclusion.»</p>"
            + TIP.format("Variantlarni toʻliq oʻqimang: avval «The first is…» qismini tekshirib, ikki-uchtasini chiqarib tashlang. "
                         "Qolganlarini faqat ikkinchi yarmi boʻyicha solishtiring.")
        )},
        crf("Some analysts predict that the opening of a large discount store will drive the small shops on Bobur Street out of business. "
            "<b>This prediction is likely to prove mistaken.</b> The small shops on Bobur Street sell mostly handmade goods that the discount store "
            "does not stock, and <b>in other cities, specialised shops near new discount stores have often gained customers from the extra foot traffic.</b>",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is the main conclusion of the argument; the second is evidence offered in support of that conclusion.", "X va D."),
            (False, "The first is the main conclusion of the argument; the second is a consideration that weighs against that conclusion.", "ikkinchisi xulosani qoʻllaydi, qarshi emas."),
            (False, "The first is a prediction that the argument rejects; the second is evidence for that prediction.", "birinchisi bashoratning oʻzi emas — uni rad etish."),
            (False, "The first is evidence offered for the main conclusion; the second is that conclusion.", "teskari tartib."),
            (False, "The first is an intermediate conclusion; the second is the main conclusion.", "asosiy xulosa — birinchi qism."),
        ], "Boshidagi «Some analysts predict» — boshqalarning fikri; muallifniki — «This prediction is likely to prove mistaken»."),
        crf("<b>Many economists expected that lowering interest rates would quickly raise business investment.</b> Yet in the year after the central "
            "bank cut rates, investment hardly changed. The reason is that firms were already operating well below capacity: <b>with idle factories, "
            "few firms needed to build new ones, whatever the cost of borrowing.</b>",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is an expectation that the argument says was not met; the second is the argument's explanation of why it was not met.",
             "kutilma bajarilmadi; ikkinchi qism — sababi."),
            (False, "The first is the argument's main conclusion; the second is evidence for that conclusion.", "muallif iqtisodchilar kutilmasini qabul qilmaydi."),
            (False, "The first is an expectation that the argument says was met; the second explains why it was met.", "investitsiya deyarli oʻzgarmadi — bajarilmagan."),
            (False, "The first is evidence that the argument uses against the economists; the second is a view that the argument rejects.", "ikkala rol ham notoʻgʻri."),
            (False, "The first and the second are both evidence offered for the same conclusion.", "birinchisi dalil emas — rad etilgan kutilma."),
        ], "Tushuntirish argumentlarida asosiy maqsad — «nima uchun?» degan savolga javob; ikkinchi qism aynan shu javob."),
        crf("The city's plan to raise parking fees downtown will reduce traffic congestion there. <b>Many drivers who now park downtown say they would "
            "take the bus if parking cost more</b>, and the bus routes into downtown currently run well below capacity, so they can absorb the extra riders.",
            "The portion in boldface plays which of the following roles in the argument?", [
            (True, "It is evidence offered in support of the argument's main conclusion.", "haydovchilar avtobusga oʻtishi — tirbandlik kamayishiga dalil."),
            (False, "It is the argument's main conclusion.", "xulosa — birinchi gap: reja tirbandlikni kamaytiradi."),
            (False, "It is an objection that the argument goes on to answer.", "eʼtiroz emas — qoʻllab-quvvatlash."),
            (False, "It is evidence that the argument says is unreliable.", "muallif unga ishonadi."),
            (False, "It is an intermediate conclusion supported by the claim about the bus routes.", "avtobus yoʻnalishlari haqidagi gap boshqa narsani — sigʻimni — qoʻllaydi."),
        ], "Bitta qalin qism boʻlsa ham usul oʻsha: avval xulosani toping."),
        crf("<b>A new study claims that drinking two cups of green tea a day lowers the risk of heart disease.</b> The study, however, compared tea drinkers "
            "with people who drink no tea without considering that the tea drinkers in its sample also exercised more. <b>So the study does not show that "
            "green tea itself lowers the risk.</b>",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is a claim that the argument calls into question; the second is the argument's main conclusion.", "Q va X."),
            (False, "The first is the argument's main conclusion; the second is evidence for that conclusion.", "muallif birinchisiga qarshi."),
            (False, "The first is evidence for the argument's main conclusion; the second is that conclusion.", "birinchisi dalil emas — shubha ostidagi daʼvo."),
            (False, "The first is a claim that the argument accepts as true; the second is a consideration that weighs against it.", "muallif uni qabul qilmaydi; ikkinchisi — xulosa."),
            (False, "The first and the second are both conclusions that the argument rejects.", "ikkinchisi — muallifning oʻz xulosasi."),
        ], "«So» bilan boshlangan qalin qism — koʻpincha asosiy xulosa (lekin har doim tekshiring)."),
        crf("<b>Online retailers' share of clothing sales has grown every year for a decade.</b> Some conclude from this that physical clothing stores will soon "
            "disappear. But <b>many shoppers still want to try clothes on before they buy them</b>, and online retailers' return rates for clothing remain high. "
            "So physical stores are likely to remain important for years to come.",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is a fact that others use to support a view the argument rejects; the second is evidence for the argument's main conclusion.",
             "fakt toʻgʻri, lekin undan chiqarilgan xulosa rad etiladi; ikkinchisi — D."),
            (False, "The first is evidence for the argument's main conclusion; the second is that conclusion.", "xulosa — oxirgi gap."),
            (False, "The first is a view that the argument rejects; the second is the argument's main conclusion.", "birinchisi fikr emas, fakt; ikkinchisi xulosa emas."),
            (False, "The first is the argument's main conclusion; the second is an objection to that conclusion.", "ikkala rol ham notoʻgʻri."),
            (False, "The first is a fact that the argument disputes; the second is evidence for the argument's main conclusion.", "muallif faktni rad etmaydi."),
        ], "Fact va view farqi: muallif onlayn ulush oʻsganini tan oladi — faqat undan chiqarilgan xulosani rad etadi."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Boshqalarning xulosasi</b> — «Some conclude…» dan keyingi gap muallifniki emas. <b>Teskari tartib</b> — toʻgʻri "
                          "rollar, notoʻgʻri ketma-ketlik. <b>«Disputes» vs «rejects the view»</b> — faktni rad etish va undan chiqarilgan "
                          "xulosani rad etish — har xil.")
            + NOTE.format("Oʻzbek tilida «lekin» va «biroq» koʻpincha gap ichidagi kichik burilish; inglizcha <i>But</i>, <i>However</i>, "
                          "<i>Yet</i> esa boldface argumentlarida koʻpincha <b>muallifning oʻz pozitsiyasi</b> boshlanadigan joy.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("boldface", "qalin harf bilan ajratilgan"), ("calls into question", "shubha ostiga qoʻyadi"), ("weighs against", "… ga qarshi turadi"),
                     ("expectation", "kutilma"), ("intermediate conclusion", "oraliq xulosa"), ("objection", "eʼtiroz")])
            + "<h3>Xulosa</h3><ul><li>Avval muallifning xulosasini toping.</li><li>Har qismni X / D / Q / T bilan belgilang.</li>"
            "<li>Variantlarni avval birinchi yarmi, keyin ikkinchi yarmi boʻyicha chiqarib tashlang.</li><li>Faktni va undan chiqarilgan fikrni farqlang.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 25 — Plans and methods of reasoning
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 25: Plans and Methods of Reasoning",
    "summary": "Reja savollari (reja maqsadga yetadimi?) va method savollari (argument qanday yoʻl bilan isbotlaydi?).",
    "order": 25,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki savol turi, bitta savol: «qanday?»</h2>"
            "<p><b>Reja savoli</b> soʻraydi: bu reja <mark>oʻz maqsadiga</mark> yetadimi? Biznes maktablari bu turni yaxshi koʻradi — "
            "menejer har kuni rejalarni baholaydi. <b>Method savoli</b> esa soʻraydi: argument <mark>qanday usul bilan</mark> "
            "isbotlaydi? «The argument proceeds by…», «Malika responds to Anvar by…».</p>"
            '<span class="sr-time">⏱ Reja / method — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul</h3>"
            + steps([
                "<p><strong>Reja:</strong> maqsadni bitta jumlada yozing — aniq raqam bilan, agar bor boʻlsa («yarmiga kamaytirish»). "
                "Keyin har bir variantga: «bu reja maqsadga <b>yetishini</b> oʻzgartiradimi?» Narx va qoʻshimcha nojoʻya taʼsirlar odatda — yoʻq.</p>",
                "<p><strong>Method:</strong> argumentni bir jumlada <b>abstrakt</b> tasvirlang: «qarshi misol keltiradi», «boshqa sabab koʻrsatadi», "
                "«oʻxshatish qiladi», «dalilni qabul qilib, uni boshqa omil bilan tortadi».</p>",
                "<p><strong>Tekshirish:</strong> variantning har bir soʻzi argumentda bormi? «Shows that the data are inaccurate» — "
                "argument maʼlumotni rad etadimi, yoki faqat boshqacha talqin qiladimi?</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>Some say that the new drug causes headaches, since 30 percent of the patients who took it in a trial reported '
            "headaches. But 29 percent of the patients in the same trial who were given a sugar pill also reported headaches. So the trial gives no "
            "reason to think that the drug causes headaches.</p></div>"
            "<p>Muallif nima qildi? U dalilni rad etmadi (30% rost), manbani tanqid qilmadi. U <b>sabab yoʻq joyda ham natija borligini</b> "
            "koʻrsatdi — taqqoslash guruhi. Abstrakt: «pointing out that a result attributed to one cause also occurred where that cause was absent».</p>"
            + TIP.format("Method variantlari koʻpincha toʻgʻri boshlanib, notoʻgʻri tugaydi: «questions the size of the trial» — tadqiqot haqida, "
                         "lekin argument hajm haqida gapirmaydi.")
        )},
        cr("Some say that the new drug causes headaches, since 30 percent of the patients who took it in a trial reported headaches. But 29 percent of "
           "the patients in the same trial who were given a sugar pill also reported headaches. So the trial gives no reason to think that the drug "
           "causes headaches.",
           "The argument proceeds by", [
            (True, "pointing out that a result attributed to one cause also occurred where that cause was absent", "dori yoʻq guruhda ham bosh ogʻrigʻi bor."),
            (False, "showing that the evidence for a claim came from a biased source", "manba tanqid qilinmagan."),
            (False, "arguing that a claim must be false because it has not been proven true", "muallif «yolgʻon» demaydi — «asos yoʻq» deydi."),
            (False, "offering an analogy between two different drugs", "ikkinchi dori yoʻq — shakar tabletka."),
            (False, "questioning the size of the trial", "hajm haqida gap yoʻq."),
        ], "Method — argumentning harakati, mazmuni emas."),
        cr("Anvar: Our firm should move its headquarters to Tashkent, because office rents there have fallen by 20 percent. Malika: Rents in Tashkent "
           "have fallen, but salaries there are higher, and salaries are a far larger share of our costs than rent is.",
           "Malika responds to Anvar by", [
            (True, "accepting his evidence but arguing that it is outweighed by another consideration", "ijara tushganini tan oladi, lekin maosh omili kuchliroq."),
            (False, "denying that office rents in Tashkent have fallen", "u buni tan oladi."),
            (False, "questioning Anvar's motives for proposing the move", "motiv haqida gap yoʻq."),
            (False, "arguing that the firm should never move its headquarters anywhere", "juda kuchli — u faqat Toshkent haqida."),
            (False, "showing that his conclusion contradicts his own evidence", "Anvarning dalili va xulosasi bir-biriga zid emas."),
        ], "«Rents have fallen, but…» — dalilni qabul qilib, tarozining ikkinchi pallasiga kattaroq yuk qoʻyish."),
        cr("To increase the number of tourists who visit in winter, the city of Khiva plans to cut its hotel taxes by half from November to February.",
           "Which of the following, if true, most strongly suggests that the plan will achieve its goal?", [
            (True, "Surveys of tour operators show that hotel prices are the main reason they do not offer winter trips to Khiva.",
             "rejaning asosiy taxmini — narx toʻsiq — tasdiqlandi."),
            (False, "Khiva's hotels are fully booked every summer.", "yoz — qishki maqsadga taʼsir qilmaydi."),
            (False, "The hotel tax provides only a small share of the city's revenue.", "xarajat — maqsadga yetishni koʻrsatmaydi."),
            (False, "Winter temperatures in Khiva are often below freezing.", "aksincha, rejaga toʻsiq boʻlishi mumkin."),
            (False, "Several other cities have also cut their hotel taxes.", "boshqa shaharlar natijasi aytilmagan — hatto raqobat boʻlishi mumkin."),
        ], "Reja kuchayishi: rejaning yashirin taxmini («muammo — narx») rost ekanini koʻrsatish."),
        cr("A supermarket chain aims to cut by half the amount of fruit and vegetables it throws away. Its plan is to sell produce that is close to its "
           "sell-by date at half price in a special section of each store.",
           "Which of the following, if true, most strongly suggests that the plan will NOT achieve its goal?", [
            (True, "Over 80 percent of the fruit and vegetables the chain throws away are damaged during delivery and are never put on sale at all.",
             "reja faqat 20% dan kamiga taʼsir qiladi — yarmiga kamaytirib boʻlmaydi."),
            (False, "The special section will take up shelf space now used for other products.", "nojoʻya taʼsir — maqsadni rad etmaydi."),
            (False, "Some customers prefer to buy only the freshest produce.", "«baʼzilar» — boshqalar arzonini oladi."),
            (False, "Other supermarket chains already use this method.", "mavzudan tashqari."),
            (False, "Half-price produce earns the chain less money per item.", "daromad — chiqindi maqsadiga taʼsir qilmaydi."),
        ], "Maqsadda raqam boʻlsa («yarmiga»), toʻgʻri javob koʻpincha rejaning yetish chegarasini koʻrsatadi."),
        cr("The mayor claims that the new bus lanes have made traffic worse, pointing to longer car journey times on Amir Temur Avenue. But journey "
           "times rose just as much on streets that got no bus lanes, after a major bridge was closed for repairs. So the bus lanes are not to blame.",
           "The argument responds to the mayor's claim by", [
            (True, "identifying another cause for the change that the mayor attributes to the bus lanes", "koʻprik yopilgani — boshqa sabab; taqqoslash ham buni tasdiqlaydi."),
            (False, "showing that the mayor's figures on journey times are inaccurate", "raqamlar qabul qilingan."),
            (False, "arguing that the bus lanes have reduced traffic", "juda kuchli — faqat «aybdor emas»."),
            (False, "attacking the mayor's motives for making the claim", "motiv haqida gap yoʻq."),
            (False, "drawing an analogy between the bus lanes and the closed bridge", "oʻxshatish yoʻq — koʻprik sabab sifatida keltirilgan."),
        ], "Method: muallif dalilni rad etmaydi — uni boshqa sabab bilan tushuntiradi."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("Reja savolida — <b>xarajat va nojoʻya taʼsir</b>, <b>«baʼzilar»</b>. Method savolida — <b>argumentda yoʻq harakat</b> "
                          "(«attacks motives», «shows data inaccurate») va <b>juda kuchli</b> tavsif («never», «has reduced»).")
            + NOTE.format("Method variantlari uzun abstrakt iboralar. Ularni argumentga «qaytaring»: «a result» — bosh ogʻrigʻi, "
                          "«one cause» — dori, «where that cause was absent» — shakar tabletka guruhi. Hammasi mos kelsa — toʻgʻri.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("proceeds by", "… yoʻli bilan isbotlaydi"), ("responds by", "… bilan javob beradi"), ("outweighed", "ustun keladi, bosib ketadi"),
                     ("achieve its goal", "maqsadiga yetmoq"), ("attributes to", "… ga bogʻlaydi"), ("analogy", "oʻxshatish")])
            + "<h3>Xulosa</h3><ul><li>Rejada maqsadni aniq yozing — raqami bilan.</li><li>Xarajat ≠ muvaffaqiyatsizlik.</li>"
            "<li>Method — argumentning harakatini abstrakt tasvirlash.</li><li>Variantni argumentning oʻz soʻzlariga qaytarib tekshiring.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 26 — CR mixed practice II
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR2,
    "title": "GMAT Verbal 26: Critical Reasoning — Mixed Practice II",
    "summary": "Ikkinchi blok boʻyicha aralash mashq: paradoks, evaluate, flaw, inference, boldface, reja va method savollari.",
    "order": 26,
    "blocks": [
        {"rich_text": (
            "<h2>Aralash mashq II</h2>"
            "<p>Critical Reasoningʼning barcha asosiy savol turlarini oʻrgandingiz. Quyidagi yettita savol — ikkinchi blokning hamma turlari aralash. "
            "Har biridan oldin <b>savol turini</b> oʻzingizga ayting va toʻrt qadamni qoʻllang.</p>"
            '<span class="sr-time">⏱ Maqsad: 7 savol — 14 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Har bir tur uchun bitta savol</h3>"
            + steps([
                "<p><strong>Paradoks:</strong> ikkala faktni ham tushuntiradigan variant.</p>",
                "<p><strong>Evaluate:</strong> «ha / yoʻq» — ikki tomonga suradigan savol.</p>",
                "<p><strong>Flaw:</strong> xatoni oʻz soʻzingiz bilan ayting, keyin abstrakt variantni qidiring.</p>",
                "<p><strong>Inference:</strong> eng ehtiyotkor, matndan albatta kelib chiqadigan variant.</p>",
                "<p><strong>Boldface / method / reja:</strong> avval xulosa yoki maqsad, keyin rollar va harakat.</p>",
            ])
            + TIP.format("Xato qilgan savolingizni tegishli darsga bogʻlang: paradoks — 23, evaluate — 20, flaw — 21, inference — 22, "
                         "boldface — 24, reja va method — 25.")
        )},
        cr("Over the past five years, the number of bookshops in the city has fallen by a third, yet the number of books bought by the city's residents has risen.",
           "Which of the following, if true, most helps to resolve the apparent discrepancy?", [
            (True, "Online retailers, which deliver to customers in the city, now account for a large and growing share of the books bought there.",
             "doʻkonlar kamaydi, lekin kitoblar onlayn sotib olinmoqda — ikkala fakt toʻgʻri."),
            (False, "Most of the bookshops that closed were small, independent shops.", "qaysilari yopilgani — savdo oʻsishini tushuntirmaydi."),
            (False, "Rents for shops in the city centre have risen sharply.", "faqat yopilishni tushuntiradi."),
            (False, "The city's population has stayed about the same over the past five years.", "aholi oʻzgarmagan — ziddiyat saqlanadi, hatto kuchayadi."),
            (False, "The city's libraries have also reduced their opening hours.", "kutubxonalar — mavzudan tashqari."),
        ], "«Bir tomonlama» tuzoq: ijara oshgani yopilishni tushuntiradi, lekin savdo oʻsishini emas."),
        cr("A company found that teams that hold a short meeting every morning complete their projects faster than teams that do not. The company "
           "therefore plans to require morning meetings for all of its teams in order to speed up its projects.",
           "Which of the following would it be most useful to know in order to evaluate the company's plan?", [
            (True, "Whether the teams that already hold morning meetings are working on simpler projects than the other teams",
             "«ha» — tezlik loyihadan, majlisdan emas; «yoʻq» — reja ishlashi ehtimoli oshadi."),
            (False, "Whether employees enjoy attending the morning meetings", "yoqishi — tezlikni hal qilmaydi."),
            (False, "Whether the company's competitors hold morning meetings", "raqobatchilar — mavzudan tashqari."),
            (False, "How many teams the company has in total", "jamoalar soni — sababni hal qilmaydi."),
            (False, "Whether the company plans to hire more managers next year", "kelajak rejasi — mavzudan tashqari."),
        ], "Ixtiyoriy guruh va sabab — evaluateʼning eng sevimli boʻshligʻi."),
        cr("Every one of the company's ten best-performing salespeople last year used the new customer-tracking software. Therefore, using the "
           "software is what makes a salesperson successful.",
           "The argument is most vulnerable to criticism on the grounds that it", [
            (True, "fails to consider whether many less successful salespeople also used the software", "taqqoslash guruhi yoʻq — hamma ishlatgan boʻlishi mumkin."),
            (False, "assumes that the top ten salespeople will remain at the company", "kelajak — argumentda yoʻq."),
            (False, "treats a percentage as though it were a number", "foiz yoʻq."),
            (False, "attacks the people who designed the software", "hujum yoʻq."),
            (False, "relies on the testimony of a source that may be biased", "manba keltirilmagan."),
        ], "Faqat muvaffaqiyatlilarga qarash — dasturni hamma ishlatgan boʻlsa, u farq yaratmaydi."),
        cr("All of the firm's interns this summer are university students, and none of the university students who work at the firm work more than "
           "20 hours a week.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "None of the firm's interns this summer work more than 20 hours a week.", "amaliyotchilar — talabalar; talabalar 20 soatdan koʻp ishlamaydi."),
            (False, "All of the university students at the firm are interns.", "teskari yoʻnalish — aytilmagan."),
            (False, "Some of the firm's interns work more than 20 hours a week.", "matnga zid."),
            (False, "Most of the firm's employees work fewer than 20 hours a week.", "boshqa xodimlar haqida maʼlumot yoʻq."),
            (False, "The firm hires only university students as interns in every season.", "faqat «this summer» haqida."),
        ], "Zanjir: amaliyotchi → talaba → ≤ 20 soat."),
        crf("<b>Some critics argue that the city's new recycling programme has failed, since the amount of waste sent to landfill has not fallen.</b> "
            "But the city's population grew by 12 percent over the same period. <b>Given that growth, keeping landfill waste level is itself "
            "evidence that the programme is working.</b>",
            "In the argument, the two portions in boldface play which of the following roles?", [
            (True, "The first is a view that the argument opposes; the second is the argument's main conclusion.", "Q va X."),
            (False, "The first is the argument's main conclusion; the second is evidence for that conclusion.", "muallif tanqidchilarga qarshi."),
            (False, "The first is evidence that the argument accepts; the second is a view that the argument opposes.", "teskari rollar."),
            (False, "The first is a view that the argument opposes; the second is evidence that supports that view.", "ikkinchisi tanqidchilarga qarshi."),
            (False, "The first and the second are both evidence for the argument's main conclusion.", "birinchisi — rad etilgan fikr."),
        ], "«Some critics argue» — boshqalarning fikri; «But» dan keyin muallifning pozitsiyasi boshlanadi."),
        cr("Each year, a call centre in Tashkent loses about half of its new employees within six months. To reduce this staff turnover, the centre plans to raise the starting salaries of new employees by 10 percent.",
           "Which of the following, if true, most strongly suggests that the plan will NOT achieve its goal?", [
            (True, "In exit interviews, nearly all departing employees say that stressful working conditions, not pay, were their reason for leaving.",
             "ketish sababi maosh emas — maosh oshirish uni toʻxtatmaydi."),
            (False, "The raise will increase the call centre's costs.", "xarajat — maqsadni rad etmaydi."),
            (False, "Some employees have worked at the call centre for over five years.", "«baʼzilari» — kadrlar almashinuvi haqida hech narsa demaydi."),
            (False, "The call centre plans to open a new office next year.", "mavzudan tashqari."),
            (False, "Starting salaries were last raised three years ago.", "tarix — rejaning natijasini koʻrsatmaydi."),
        ], "Reja sababga qaratilgan boʻlishi kerak: sabab boshqa boʻlsa, reja ishlamaydi."),
        cr("Critics claim that the new tax on sugary drinks will hurt small shops. But the same claim was made when the country introduced a tax on "
           "tobacco, and small shops' sales did not fall then. So the critics' claim is probably mistaken.",
           "The argument proceeds by", [
            (True, "drawing an analogy between the new tax and an earlier one whose predicted effect did not occur", "tamaki soligʻi — oʻxshash holat."),
            (False, "showing that the critics have a financial interest in opposing the tax", "motiv haqida gap yoʻq."),
            (False, "providing statistics about the sales of sugary drinks", "shirin ichimliklar statistikasi yoʻq."),
            (False, "pointing out that the critics' claim contradicts itself", "ichki ziddiyat koʻrsatilmagan."),
            (False, "questioning whether small shops sell sugary drinks", "bunday savol yoʻq."),
        ], "Oʻxshatish argumentining zaif joyi: ikki holat haqiqatan oʻxshashmi? (Tamaki va shirin ichimlik — har xil mahsulot.)"),
        {"rich_text": (
            "<h3>Natijani tahlil qiling</h3>"
            + WARN.format("Eng koʻp takrorlanadigan xato bu blokda — <b>bir tomonlama</b> variant (paradoksda) va <b>boshqalarning fikrini</b> "
                          "muallifniki deb olish (boldfaceʼda). Ikkalasi ham tez oʻqishdan keladi.")
            + NOTE.format("Critical Reasoning blokini tugatdingiz. Keyingi blok — <b>Reading Comprehension</b>: uzun matn va bir nechta savol. "
                          "CRʼda oʻrgangan koʻnikmalar (xulosa, rol, inference) u yerda ham ishlaydi.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("turnover", "kadrlar almashinuvi"), ("exit interview", "ketayotgan xodim bilan suhbat"), ("landfill", "chiqindi poligoni"),
                     ("recycling", "qayta ishlash"), ("best-performing", "eng yaxshi natija koʻrsatgan")])
            + "<h3>Xulosa</h3><ul><li>Avval tur, keyin usul.</li><li>Xatolarni darslar boʻyicha guruhlang.</li>"
            "<li>CR koʻnikmalari Reading Comprehensionʼga oʻtadi.</li></ul>"
        )},
    ],
},
]
