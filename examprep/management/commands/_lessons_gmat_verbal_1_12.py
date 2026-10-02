# -*- coding: utf-8 -*-
"""
GMAT Verbal Reasoning — lessons 1, 2 (strategy) and 10, 11, 12 (Critical Reasoning core).
See toc_gmat_verbal.txt and STYLE_GUIDE_GMAT_VERBAL.md (on top of STYLE_GUIDE_SAT_RW.md).

Language: explanations in Uzbek, exam material in English. Five answer choices on every
question, as on the real test. Choices are shuffled on screen, so explanations name choices
by their opening words, never by letter.
"""

TRACK = {
    "name":    "GMAT",
    "summary": "GMAT Focus Edition — Verbal Reasoning: Critical Reasoning va Reading Comprehension. "
               "Quant va Data Insights — Prime GMAT kursida.",
    "icon":    "bi-briefcase",
    "color":   "#0f766e",
    "order":   4,
}

TOPIC_STRATEGY = {
    "title":   "Strategiya va format (Verbal: qanday tuzilgan)",
    "summary": "GMAT Verbal boʻlimi qanday tuzilgan, qanday baholanadi va har bir savolga qanday yondashish kerak.",
    "icon":    "bi-compass",
    "order":   1,
}
TOPIC_CR = {
    "title":   "Critical Reasoning: argument tuzilishi",
    "summary": "Argumentning xulosasi, dalillari va yashirin taxmini — hamda uni zaiflashtirish va kuchaytirish.",
    "icon":    "bi-diagram-3",
    "order":   2,
}

TIP  = ('<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;'
        'border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> {}</div>')
WARN = ('<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;'
        'border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> {}</div>')
NOTE = ('<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;'
        'border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> {}</div>')
EXAMP = ('<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> {}</div>')


def _open(text, n=7):
    words = text.split()
    return ' '.join(words[:n]) + ('…' if len(words) > n else '')


def why(rows):
    out = ['<div class="sr-why">']
    for ok, choice, reason in rows:
        kind, tag = ('ok', 'TO‘G‘RI') if ok else ('no', 'TUZOQ')
        out.append(f'<div class="sr-why__row sr-why__row--{kind}"><span class="sr-why__tag">{tag}</span>'
                   f'<span class="sr-why__text"><b>{_open(choice)}</b> — {reason}</span></div>')
    out.append('</div>')
    return ''.join(out)


def cr(passage, stem, rows, lead, time="⏱ ~2 daqiqa"):
    """One Critical Reasoning question. rows = [(is_key, choice_text, uzbek_reason)] × 5."""
    return {
        "rich_text": (f'<div class="sr-passage"><p>{passage}</p></div>'
                      f'<p><strong>{stem}</strong></p><span class="sr-time">{time}</span>'),
        "choices": [{"text": t, "is_correct": ok} for ok, t, _ in rows],
        "explanation": f"<p>{lead}</p>" + why(rows),
    }


def ask(stem, rows, lead):
    """A question ABOUT the test — the teacher speaking, so stem and choices are Uzbek."""
    return {
        "rich_text": f"<p><strong>{stem}</strong></p>",
        "choices": [{"text": t, "is_correct": ok} for ok, t, _ in rows],
        "explanation": f"<p>{lead}</p>" + why(rows),
    }


def cards(pairs):
    body = ''.join(f'<div class="pp-card"><div class="pp-card-front">{a}</div><div class="pp-card-back">{b}</div></div>'
                   for a, b in pairs)
    return f'<div class="pp-flashcards" data-pp-flashcards>{body}</div>'


def steps(items):
    body = ''.join(f'<div class="pp-step">{s}</div>' for s in items)
    return f'<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">{body}</div>'


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 1 — the section
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "GMAT Verbal 1: How the Verbal Section Works — 23 Questions, 45 Minutes",
    "summary": "GMAT Focus Editionʼning Verbal boʻlimi: 23 savol, 45 daqiqa, ikki savol turi, besh variant va Sentence Correction yoʻqligi.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>Verbal boʻlimi qanday ishlaydi?</h2>"
            "<p>Prime GMAT kursida siz imtihonning ikki boʻlimini — <strong>Quant</strong> va "
            "<strong>Data Insights</strong>ni oʻrgandingiz. Bu kurs — uchinchisi: <mark>Verbal Reasoning</mark>. "
            "Bu yerda matematika yoʻq; bu yerda <strong>ingliz tilidagi argument va matnni</strong> "
            "toʻgʻri oʻqish tekshiriladi. Biznes maktablari uchun bu koʻnikma juda muhim: rahbar har kuni "
            "hisobot, taklif va xatlarni oʻqib, ularning qayeri mustahkam, qayeri boʻsh ekanini koʻrishi kerak.</p>"
            "<p>Birinchi darsda <strong>oʻyin maydonini</strong> bilib olamiz: nechta savol, qancha vaqt, "
            "qanday savol turlari. Formatni bilmasdan strategiya qurib boʻlmaydi.</p>"
            '<span class="sr-time">⏱ Bir savolga oʻrtacha ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Asosiy raqamlar</h3>"
            + steps([
                "<p><strong>23 ta savol, 45 daqiqa.</strong> Bir savolga oʻrtacha <mark>1 daqiqa 57 soniya</mark> — "
                "Quantʼdagidan (2 daqiqa 8 soniya) biroz kam.</p>",
                "<p><strong>Ikki savol turi:</strong> <em>Critical Reasoning</em> (qisqa argument — odatda "
                "<strong>100 soʻzdan kam</strong> — va bitta savol) hamda <em>Reading Comprehension</em> "
                "(uzunroq matn va unga bir nechta savol).</p>",
                "<p><strong>Har savolda besh variant.</strong> SATʼdagidan bitta koʻp — demak bitta tuzoq ham koʻp.</p>",
                "<p><strong>Sentence Correction yoʻq.</strong> Eski GMATʼda gap tuzilishini tuzatish savollari "
                "bor edi; GMAT Focus Editionʼda ular olib tashlangan. Grammatika jadvallarini yodlash shart emas.</p>",
                "<p><strong>Ball:</strong> boʻlim uchun 60–90; umumiy ball 205–805, uch boʻlim teng hissa qoʻshadi. "
                "Boʻlimlar tartibini oʻzingiz tanlaysiz, va boʻlim ichida koʻpi bilan <strong>3 ta</strong> javobni "
                "oxirida oʻzgartirish mumkin (Question Review &amp; Edit).</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Critical Reasoning qanday koʻrinadi</h3>"
            "<p>Ekranda qisqa argument va bitta savol chiqadi. Argument — biznes, iqtisod, fan yoki "
            "jamiyat haqidagi bir necha gap:</p>"
            '<div class="sr-passage"><p>Since the bank opened a branch inside the Samarkand shopping centre, '
            "the number of new accounts opened in the city has doubled. The branch should therefore stay open "
            "on Sundays, when the shopping centre is busiest.</p></div>"
            "<p><strong>Which of the following, if true, most strengthens the argument?</strong></p>"
            + NOTE.format("Savol argumentni <b>kuchaytirish</b>, <b>zaiflashtirish</b>, uning <b>yashirin taxmini</b>ni "
                          "topish yoki undan <b>xulosa</b> chiqarishni soʻraydi. Bu turlarning har biriga alohida dars bor.")
            + "<h3>Reading Comprehension qanday koʻrinadi</h3>"
            "<p>Ekranning bir tomonida 200–350 soʻzli matn, ikkinchi tomonida savollar ketma-ket chiqadi. "
            "Bitta matnga odatda bir nechta savol beriladi: asosiy fikr, tafsilot, xulosa, muallifning maqsadi.</p>"
            + TIP.format("Reading Comprehensionʼda matnni bir marta diqqat bilan oʻqish keyingi savollarning har birida "
                         "vaqtni qaytaradi. Critical Reasoningʼda esa aksincha — <b>avval savolni</b> oʻqing "
                         "(keyingi dars shu haqda).")
        )},
        ask("GMAT Focus Editionʼning Verbal boʻlimida nechta savol bor?", [
            (False, "20 ta", "bu Data Insights boʻlimidagi savollar soni."),
            (False, "21 ta", "bu Quant boʻlimidagi savollar soni."),
            (True, "23 ta", "Verbal — 23 savol, 45 daqiqa."),
            (False, "27 ta", "bu SAT Reading and Writingʼning bitta moduli."),
            (False, "36 ta", "eski GMATʼning Verbal boʻlimiga yaqin son — Focus Editionʼda emas."),
        ], "Uchta boʻlimning har biri 45 daqiqa, lekin savollar soni har xil."),
        ask("Quyidagilardan qaysi savol turi GMAT Focus Editionʼning Verbal boʻlimida YOʻQ?", [
            (False, "Critical Reasoning — qisqa argument va bitta savol", "Verbalʼning ikki asosiy turidan biri."),
            (False, "Reading Comprehension — uzun matn va bir nechta savol", "Verbalʼning ikkinchi asosiy turi."),
            (True, "Sentence Correction — gap tuzilishini tuzatish", "Focus Editionʼda olib tashlangan."),
            (False, "Assumption — argumentning yashirin taxminini topish", "bu Critical Reasoning ichidagi savol turi, bor."),
            (False, "Inference — matndan kelib chiqadigan xulosa", "Reading Comprehension va Critical Reasoningʼda bor."),
        ], "GMAT Focus Edition grammatika tuzatish savollarini olib tashlagan — Verbal faqat oʻqish va mulohaza."),
        ask("Verbal boʻlimida bir savolga oʻrtacha qancha vaqt toʻgʻri keladi?", [
            (False, "1 daqiqa 15 soniya", "bu juda kam: 45 ÷ 23 ≈ 1.96 daqiqa."),
            (False, "1 daqiqa 30 soniya", "hali ham kam."),
            (True, "Taxminan 2 daqiqa", "45 ÷ 23 ≈ 1 daqiqa 57 soniya."),
            (False, "2 daqiqa 30 soniya", "bu 23 savolga 57 daqiqa boʻlardi."),
            (False, "3 daqiqa", "bu 69 daqiqa talab qilardi."),
        ], "45 daqiqa ÷ 23 savol ≈ 1 daqiqa 57 soniya."),
        ask("Critical Reasoning argumenti odatda qancha uzunlikda boʻladi?", [
            (True, "100 soʻzdan kam", "GMAC rasmiy taʼrifi: qisqa matn, odatda 100 soʻzdan kam."),
            (False, "200–350 soʻz", "bu Reading Comprehension matni uzunligi."),
            (False, "500 soʻz atrofida", "bunday uzun matn Verbalʼda yoʻq."),
            (False, "Bir sahifa", "juda uzun."),
            (False, "Matn yoʻq — faqat savol", "har bir CR savoli argumentga tayanadi."),
        ], "Qisqa argument — har bir soʻzi muhim degani."),
        ask("Question Review & Edit bilan boʻlim oxirida nechta javobni oʻzgartirish mumkin?", [
            (False, "Bittasini ham", "imkoniyat bor — vaqt qolsa."),
            (False, "1 tagacha", "koʻproq mumkin."),
            (True, "3 tagacha", "har bir boʻlimda koʻpi bilan uchta javob."),
            (False, "5 tagacha", "chegarasi uchta."),
            (False, "Istalgan miqdorda", "chegara bor — uchta."),
        ], "Uchta tahrir — faqat aniq xatoni tuzatish uchun saqlang."),
        {"rich_text": (
            "<h3>Bilib qoʻying</h3>"
            + WARN.format("Bizning nomzodlar koʻpincha Verbalʼni «ingliz tili imtihoni» deb oʻylaydi va lugʻat "
                          "yodlaydi. Aslida bu <b>mantiq imtihoni</b>: soʻzlar oddiy, lekin argumentning qaysi "
                          "qismi dalil, qaysi qismi xulosa va qayerda boʻshliq borligini koʻrish kerak.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("Verbal Reasoning", "ogʻzaki mulohaza boʻlimi"), ("Critical Reasoning", "tanqidiy fikrlash savollari"),
                     ("Reading Comprehension", "matnni tushunish"), ("argument", "dalil + xulosa"),
                     ("passage", "matn"), ("answer choice", "javob varianti")])
            + "<h3>Xulosa</h3><ul>"
            "<li>23 savol, 45 daqiqa — bir savolga taxminan 2 daqiqa.</li>"
            "<li>Ikki tur: Critical Reasoning (qisqa argument) va Reading Comprehension (uzun matn).</li>"
            "<li>Har savolda besh variant; Sentence Correction yoʻq.</li>"
            "<li>Review &amp; Edit — koʻpi bilan 3 ta tahrir.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 2 — the method
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "GMAT Verbal 2: Read the Question First — One Method for Every Verbal Question",
    "summary": "Critical Reasoning uchun toʻrt qadamli usul: avval savol, keyin argument, javobni oldindan taxmin qilish va beshta variantdan toʻrttasini chiqarib tashlash.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Avval savolni oʻqing</h2>"
            "<p>Critical Reasoningʼda argument qisqa, lekin uni <b>nima uchun</b> oʻqiyotganingizni bilmasangiz, "
            "ikki-uch marta qayta oʻqishga toʻgʻri keladi. Savol argumentni qanday oʻqishni aytadi: "
            "«weaken» desa — boʻshliq qidirasiz, «conclusion» desa — asosiy daʼvoni, «must be true» desa — "
            "faqat matndagi faktlarni.</p>"
            '<span class="sr-time">⏱ Usul bilan bir savol — 1.5–2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Toʻrt qadam</h3>"
            + steps([
                "<p><strong>1. Savolni oʻqing</strong> va turini aniqlang: conclusion, assumption, weaken, strengthen, inference.</p>",
                "<p><strong>2. Argumentni oʻqing</strong> va uni ikki qismga ajrating: <mark>xulosa</mark> (muallif nimani daʼvo qiladi) "
                "va <mark>dalil</mark> (nimaga tayanadi).</p>",
                "<p><strong>3. Javobni oldindan taxmin qiling.</strong> Dalil va xulosa orasidagi <b>boʻshliq</b> qayerda? "
                "Variantlarga qaramasdan oʻz soʻzingiz bilan ayting.</p>",
                "<p><strong>4. Chiqarib tashlang.</strong> Beshta variantdan toʻrttasi tuzoq; ularni turi boʻyicha taniying: "
                "mavzudan tashqari, teskari, juda kuchli, dalilni takrorlaydigan.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>Our city should extend its bike-sharing program to the suburbs. In its first year, '
            "the program cut car trips in the city centre by 8 percent, and surveys show that most suburban residents "
            "commute fewer than ten kilometres — a distance easily covered by bicycle.</p></div>"
            "<p><strong>Which of the following, if true, most seriously weakens the argument?</strong></p>"
            "<p><b>1-qadam:</b> weaken — boʻshliqni qidiramiz. <b>2-qadam:</b> xulosa — dasturni shahar atrofiga kengaytirish kerak; "
            "dalil — markazda ishladi, va masofa qisqa. <b>3-qadam:</b> boʻshliq — markazdagi natija shahar atrofida ham "
            "takrorlanadimi? Masalan, u yerda velosiped yoʻllari yoʻq boʻlsa-chi? <b>4-qadam:</b> shu fikrni beradigan variant — "
            "«Most suburban roads have no bicycle lanes, and residents say they feel unsafe cycling on them» — toʻgʻri javob.</p>"
            + TIP.format("Oldindan taxmin aniq soʻz boʻlishi shart emas — yoʻnalish yetarli: «markaz va chekka farq qiladi». "
                         "Variantlar orasida shu yoʻnalishdagisini qidirasiz.")
        )},
        cr("Our city's new bike-sharing program should be extended to the suburbs. In its first year, the program reduced car trips "
           "in the city centre by 8 percent, and surveys show that most suburban residents commute fewer than ten kilometres — "
           "a distance easily covered by bicycle.",
           "Which of the following best states the main conclusion of the argument?", [
            (True, "The bike-sharing program should be extended to the suburbs.", "muallif aynan shuni daʼvo qiladi; qolgan hammasi unga dalil."),
            (False, "The program reduced car trips in the city centre by 8 percent.", "bu dalil — xulosani qoʻllab-quvvatlash uchun keltirilgan."),
            (False, "Most suburban residents commute fewer than ten kilometres.", "bu ham dalil."),
            (False, "Bicycles are the best way to reduce traffic in any city.", "juda kuchli — argument bunday daʼvo qilmaydi."),
            (False, "Suburban residents prefer cycling to driving.", "matnda yoʻq: ular qisqa masofani bosadi, xolos."),
        ], "Xulosani topish uchun soʻrang: «muallif meni nimaga ishontirmoqchi?» Qolgan gaplar — «nima uchun?» degan savolga javob."),
        cr("A café owner noticed that her sales rose 20 percent in the month after she began playing music in the café. "
           "She concluded that playing music caused the increase in sales.",
           "Which of the following, if true, most seriously weakens the owner's conclusion?", [
            (True, "The month in which she began playing music was the start of the tourist season, when sales at every café on her street rose by about 20 percent.",
             "boshqa sabab: oʻsish musiqasiz kafelarda ham boʻlgan — demak musiqa sabab boʻlmasligi mumkin."),
            (False, "Several customers told the owner that they enjoyed the music.", "biroz kuchaytiradi — teskari yoʻnalish."),
            (False, "The café's prices did not change during that month.", "bitta muqobil sababni yoʻqqa chiqaradi — kuchaytiradi."),
            (False, "Music is played in many successful restaurants.", "mavzudan tashqari — bu kafe haqida hech narsa demaydi."),
            (False, "The owner chose songs that are popular with young people.", "musiqaning turi sabab-natija bogʻlanishini oʻzgartirmaydi."),
        ], "«X dan keyin Y boʻldi, demak X sabab» — eng koʻp uchraydigan zaif argument. Uni boshqa sabab bilan zaiflashtiramiz."),
        cr("A delivery company plans to cut its delivery times by moving its warehouse from the city's outskirts to a site near the "
           "central market. Since most of its customers are shops in the central market area, the move will shorten the distance "
           "its vans travel on most deliveries.",
           "The company's plan to cut delivery times depends on which of the following assumptions?", [
            (True, "Traffic near the central market is not so heavy that the shorter trips will take longer than the current ones.",
             "masofa qisqarsa ham, vaqt qisqarmasligi mumkin — inkor qilsak, reja yiqiladi."),
            (False, "The new site costs less to rent than the current warehouse.", "narx — boshqa masala; reja vaqt haqida."),
            (False, "Most customers are satisfied with the current delivery times.", "rejaning ishlashiga taʼsir qilmaydi."),
            (False, "The company will hire more drivers after the move.", "shart emas — vaqt masofa orqali qisqarishi kerak."),
            (False, "No other company has a warehouse near the central market.", "raqobat — mavzudan tashqari."),
        ], "Dalil — «masofa qisqaradi», xulosa — «vaqt qisqaradi». Boʻshliq: masofa = vaqt deb olinyapti."),
        cr("At Firm Z, every employee who completed the advanced training course this year received a year-end bonus. Dilnoza, who works in the firm's sales department, did not receive a bonus this year.",
           "If the statements above are true, which of the following must also be true?", [
            (True, "Dilnoza did not complete the advanced training course this year.", "kursni tugatganlarning hammasi bonus oldi; Dilnoza olmadi — demak tugatmagan."),
            (False, "Dilnoza did not enrol in the advanced training course.", "roʻyxatdan oʻtgan, lekin tugatmagan boʻlishi mumkin."),
            (False, "Only employees who completed the course received bonuses.", "teskarisi — boshqalar ham bonus olgan boʻlishi mumkin."),
            (False, "Dilnoza will complete the course next year.", "kelajak haqida hech narsa aytilmagan."),
            (False, "Most employees received a bonus this year.", "nechta xodim kursni tugatgani nomaʼlum."),
        ], "«Must be true» — faqat matndan qatʼiy kelib chiqadigan narsa. «Hamma A — B; Dilnoza B emas → Dilnoza A emas.»"),
        cr("A hotel chain claims that adding a free breakfast raised its customer ratings. After free breakfast was introduced at its "
           "Bukhara hotel, the hotel's average rating rose from 3.9 to 4.4.",
           "Which of the following, if true, most strengthens the chain's claim?", [
            (True, "At the chain's Khiva hotel, which did not add free breakfast during the same period, the average rating stayed at 3.9.",
             "taqqoslash guruhi: nonushtasiz mehmonxonada oʻsish yoʻq — sabab nonushta ekani kuchayadi."),
            (False, "Many guests at the Bukhara hotel are foreign tourists.", "mehmonlar kimligi sababni koʻrsatmaydi."),
            (False, "The Bukhara hotel also renovated all its rooms during the same period.", "boshqa sabab — zaiflashtiradi."),
            (False, "Free breakfast costs the hotel about $4 per guest.", "xarajat — baho haqidagi daʼvoga taʼsir qilmaydi."),
            (False, "Some guests rated the hotel before eating breakfast.", "noaniq — kuchaytirmaydi."),
        ], "Kuchaytirishning eng kuchli usuli — sabab yoʻq joyda natija ham yoʻqligini koʻrsatish."),
        {"rich_text": (
            "<h3>Toʻrtta tuzoq shakli</h3>"
            + WARN.format("<b>Mavzudan tashqari</b> (rost, lekin boʻshliq haqida emas) · <b>teskari</b> (zaiflashtirish oʻrniga kuchaytiradi) · "
                          "<b>juda kuchli</b> («always», «all», «best») · <b>dalilni takrorlash</b> (xulosa oʻrniga). "
                          "Beshta variantning toʻrttasi odatda shu toʻrt shakldan biri.")
            + NOTE.format("Bizda koʻpchilik variantlarni «qaysi biri toʻgʻri gap?» deb oʻqiydi. Toʻrtta tuzoqning koʻpi — rost gaplar. "
                          "Savol «qaysi biri rost?» emas, «qaysi biri <b>savolga javob beradi</b>?»")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("conclusion", "xulosa — asosiy daʼvo"), ("premise / evidence", "dalil"), ("assumption", "yashirin taxmin"),
                     ("weaken", "zaiflashtirmoq"), ("strengthen", "kuchaytirmoq"), ("must be true", "albatta toʻgʻri"),
                     ("prephrase", "javobni oldindan taxmin qilmoq")])
            + "<h3>Xulosa</h3><ul><li>Avval savol, keyin argument.</li><li>Xulosa va dalilni ajrating, boʻshliqni toping.</li>"
            "<li>Variantlardan oldin javobni oʻz soʻzingiz bilan ayting.</li><li>Toʻrtta tuzoq shaklini taniying.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 10 — anatomy of an argument
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR,
    "title": "GMAT Verbal 10: Anatomy of an Argument — Conclusion, Premises, Background",
    "summary": "Argumentning qismlari: asosiy xulosa, oraliq xulosa, dalillar, tan olingan qarshi fikr va fon maʼlumoti.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Argument nimadan iborat?</h2>"
            "<p>Har bir Critical Reasoning savolining poydevori bitta koʻnikma: argumentni <b>qismlarga ajratish</b>. "
            "<mark>Xulosa</mark> — muallif sizni nimaga ishontirmoqchi. <mark>Dalil</mark> (premise) — u nimaga tayanadi. "
            "<mark>Fon</mark> — vaziyatni tushuntiradi, lekin hech narsani isbotlamaydi. Baʼzan argumentda "
            "<mark>tan olingan qarshi fikr</mark> ham boʻladi: «Although…», «Admittedly…».</p>"
            '<span class="sr-time">⏱ Xulosa savoli — ~1.5 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: «nima uchun?» testi</h3>"
            + steps([
                "<p><strong>1.</strong> Gaplardan birini «xulosa» deb taxmin qiling.</p>",
                "<p><strong>2.</strong> Qolgan gaplarning har biri «<b>nima uchun?</b>» degan savolga javob beradimi? "
                "Bersa — ular dalil, taxminingiz toʻgʻri.</p>",
                "<p><strong>3.</strong> Signal soʻzlar: <em>therefore, so, thus, clearly, should</em> — koʻpincha xulosa; "
                "<em>because, since, given that, for</em> — dalil; <em>although, admittedly, despite</em> — tan olingan qarshi fikr.</p>",
                "<p><strong>4.</strong> Ehtiyot boʻling: «so» <b>oraliq xulosani</b> ham boshlashi mumkin — u yana kattaroq xulosaga dalil boʻlib xizmat qiladi.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>The city should not build the proposed parking garage downtown. The garage would '
            "encourage more people to drive into the city centre, so traffic downtown would get worse. And worse traffic "
            "would undo the progress the city has made in reducing air pollution.</p></div>"
            "<p>«<i>so traffic downtown would get worse</i>» — «so» bilan boshlanadi, lekin bu <b>oraliq xulosa</b>: u oʻzi "
            "«nima uchun garaj qurmaslik kerak?» savoliga javob beradi. Asosiy xulosa — birinchi gap: "
            "<mark>The city should not build the proposed parking garage downtown.</mark></p>"
            + TIP.format("Asosiy xulosa koʻpincha <b>tavsiya</b> («should») yoki <b>baho</b> («has failed», «is a mistake») shaklida boʻladi, "
                         "va u argumentning <b>boshida</b> ham turishi mumkin.")
        )},
        cr("Despite its higher price, the electric delivery van will save our company money. Its fuel and maintenance costs are about "
           "half those of our diesel vans, and over the eight years we usually keep a van, those savings exceed the difference in purchase price.",
           "Which of the following best states the main conclusion of the argument?", [
            (True, "The electric delivery van will save the company money.", "qolgan hammasi shuni isbotlash uchun."),
            (False, "The electric van's fuel and maintenance costs are about half those of diesel vans.", "dalil."),
            (False, "The company usually keeps a van for eight years.", "dalil — hisob uchun vaqt oraligʻi."),
            (False, "Electric vans cost more to buy than diesel vans.", "«Despite…» — tan olingan qarshi fikr, xulosa emas."),
            (False, "The company should replace all its diesel vans immediately.", "argumentdan tashqariga chiqadi."),
        ], "«Despite» bilan boshlangan qism — muallif tan oladigan, lekin yengib oʻtadigan fikr."),
        cr("The bank's new mobile app has been downloaded by fewer than 5 percent of its customers. Clearly, the marketing campaign for "
           "the app has failed, since the campaign's stated goal was to have 20 percent of customers using the app within six months, "
           "and those six months are over.",
           "Which of the following best states the main conclusion of the argument?", [
            (True, "The marketing campaign for the app has failed.", "«Clearly» bilan kelgan baho — qolgan gaplar «nima uchun?» ga javob."),
            (False, "Fewer than 5 percent of customers have downloaded the app.", "dalil."),
            (False, "The campaign aimed to have 20 percent of customers using the app within six months.", "dalil — maqsad."),
            (False, "The bank's customers do not like mobile apps.", "matnda yoʻq va juda kuchli."),
            (False, "The bank should end the marketing campaign.", "tavsiya — argument buni aytmaydi."),
        ], "Xulosa argumentning oʻrtasida ham turishi mumkin — signal soʻzga («Clearly») qarang."),
        cr("Some managers argue that open-plan offices improve teamwork. However, a two-year study at a large insurance firm found that "
           "after it moved to an open-plan office, face-to-face conversations between employees fell by about 70 percent. So open-plan "
           "offices may reduce, rather than increase, the interaction that teamwork depends on.",
           "The study at the insurance firm plays which of the following roles in the argument?", [
            (True, "It is evidence offered in support of the argument's conclusion.", "tadqiqot — xulosaga («interaction kamayishi mumkin») asosiy dalil."),
            (False, "It is the argument's main conclusion.", "xulosa — «So…» dan keyingi gap."),
            (False, "It is a view that the argument sets out to reject.", "rad etilayotgan fikr — menejerlarning daʼvosi."),
            (False, "It is a consideration that the argument concedes weakens its conclusion.", "aksincha — xulosani qoʻllab-quvvatlaydi."),
            (False, "It is background information that has no bearing on the conclusion.", "xulosa aynan shunga tayanadi."),
        ], "Rol savolida avval xulosani toping, keyin soʻralgan qismning unga munosabatini aniqlang."),
        cr("The city should not build the proposed parking garage downtown. The garage would encourage more people to drive into the city "
           "centre, so traffic downtown would get worse. And worse traffic would undo the progress the city has made in reducing air pollution.",
           "Which of the following best states the main conclusion of the argument?", [
            (True, "The city should not build the proposed downtown parking garage.", "asosiy tavsiya — qolganlari unga dalil."),
            (False, "Traffic in the city centre would get worse.", "oraliq xulosa — u oʻzi asosiy xulosaga dalil."),
            (False, "The garage would encourage more people to drive into the city centre.", "dalil."),
            (False, "The city has made progress in reducing air pollution.", "dalil."),
            (False, "Air pollution downtown is caused mainly by traffic.", "matnda aytilmagan."),
        ], "«So» har doim asosiy xulosani boshlamaydi — «nima uchun?» testini qoʻllang."),
        cr("Although the new training program costs more per employee than the old one, the firm should adopt it. In a trial, employees who "
           "completed the new program made 40 percent fewer errors, and each error costs the firm far more to fix than the extra training costs.",
           "The statement that the new program costs more per employee functions in the argument as", [
            (True, "a consideration the author acknowledges but argues is outweighed", "«Although» — tan olinadi, keyin xatolar tejami bilan yengiladi."),
            (False, "the main conclusion of the argument", "xulosa — «the firm should adopt it»."),
            (False, "evidence that the new program should be adopted", "aksincha — dasturga qarshi fikr."),
            (False, "an assumption the argument depends on but does not state", "u ochiq aytilgan."),
            (False, "a claim the author argues is false", "muallif uni rad etmaydi — tan oladi."),
        ], "Tan olingan qarshi fikr — muallif uni toʻgʻri deb biladi, lekin xulosani oʻzgartirmaydi deydi."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("Eng koʻp tanlanadigan xato — <b>oraliq xulosa</b> yoki <b>eng ishonchli dalil</b>ni asosiy xulosa deb olish. "
                          "Ikkinchi xato — matndan tashqariga chiquvchi «yaxshi» tavsiya («should end the campaign»).")
            + NOTE.format("Oʻzbek tilida xulosa koʻpincha gap oxirida keladi, shuning uchun bizda «oxirgi gap — xulosa» degan odat bor. "
                          "GMATʼda xulosa boshida, oʻrtasida yoki oxirida boʻlishi mumkin — joyiga emas, roliga qarang.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("main conclusion", "asosiy xulosa"), ("intermediate conclusion", "oraliq xulosa"), ("premise", "dalil"),
                     ("concession", "tan olingan qarshi fikr"), ("background", "fon maʼlumoti"), ("role", "vazifa, rol")])
            + "<h3>Xulosa</h3><ul><li>Xulosa — «nimaga ishontirmoqchi?»; dalil — «nima uchun?».</li>"
            "<li>Signal soʻzlar yordam beradi, lekin «so» oraliq xulosani ham boshlaydi.</li>"
            "<li>«Although / despite» — tan olingan qarshi fikr.</li><li>Xulosa matnning istalgan joyida boʻlishi mumkin.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 11 — assumptions
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR,
    "title": "GMAT Verbal 11: The Gap — Finding What the Argument Assumes",
    "summary": "Zaruriy taxmin: dalil va xulosa orasidagi boʻshliqni topish va variantni «inkor qilish testi» bilan tekshirish.",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Argument nimani aytmay qoʻyadi?</h2>"
            "<p>Har bir argumentda dalil va xulosa orasida <mark>boʻshliq</mark> bor — muallif oʻzi isbotlamagan, lekin "
            "toʻgʻri deb hisoblayotgan narsa. Bu <b>yashirin taxmin</b> (assumption). «The argument depends on which of "
            "the following assumptions?» savoli aynan shu boʻshliqni soʻraydi.</p>"
            '<span class="sr-time">⏱ Taxmin savoli — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Usul: inkor qilish testi</h3>"
            + steps([
                "<p><strong>1.</strong> Xulosa va dalilni yozing. Dalilda boʻlmagan, lekin xulosada paydo boʻlgan <b>yangi tushuncha</b>ni toping.</p>",
                "<p><strong>2.</strong> Boʻshliqni oʻz soʻzingiz bilan ayting: «muallif X va Y bir xil deb hisoblayapti».</p>",
                "<p><strong>3.</strong> Variantni <b>inkor qiling</b>. Inkor qilingan variant bilan argument yiqilsa — bu zaruriy taxmin.</p>",
                "<p><strong>4.</strong> Juda kuchli variantlardan saqlaning: taxmin odatda «hech boʻlmaganda», «asosan» kabi yumshoq boʻladi.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>A city plans to reduce the number of accidents at a busy intersection by installing a '
            "traffic light there. Most accidents at the intersection happen when drivers misjudge the gaps in oncoming traffic.</p></div>"
            "<p>Xulosa — svetofor avariyalarni kamaytiradi. Dalil — avariyalar haydovchilar boʻshliqni notoʻgʻri baholaganda boʻladi. "
            "Boʻshliq: svetofor boʻlsa, haydovchilar boʻshliqni baholamaydi — <b>ular svetoforga boʻysunsa</b>. "
            "Variant «Drivers will generally obey the traffic light» — inkor qilsak: «haydovchilar svetoforga boʻysunmaydi» → "
            "reja ishlamaydi. Demak bu zaruriy taxmin.</p>"
            + TIP.format("Inkor qilishda variantning eng kichik qarama-qarshisini oling: «generally obey» → «generally do not obey», "
                         "«never obey» emas.")
        )},
        cr("A bakery in Samarkand plans to raise the price of its bread by 10 percent in order to increase its revenue from bread. "
           "The bakery's managers point out that even after the increase, its bread will still be cheaper than that of other bakeries nearby.",
           "The managers' plan to increase revenue depends on which of the following assumptions?", [
            (True, "The price increase will not cause the bakery to sell so much less bread that its revenue from bread falls.",
             "inkor qilsak: savdo shunchalik tushadiki tushum kamayadi — reja yiqiladi."),
            (False, "The other bakeries nearby will not lower their prices.", "ular narxni tushirsa ham, tushum oshishi mumkin — zaruriy emas."),
            (False, "Customers prefer this bakery's bread to that of the other bakeries.", "shart emas — narx arzonligicha qoladi."),
            (False, "The bakery's costs of making bread will not rise.", "xarajat — foydaga taʼsir qiladi, tushumga emas."),
            (False, "Most of the bakery's customers buy bread every day.", "mavzudan tashqari."),
        ], "Tushum = narx × miqdor. Narx oshsa, tushum oshishi uchun miqdor juda koʻp tushmasligi kerak — bu yashirin taxmin."),
        cr("Employees at Firm X who work from home two days a week report higher job satisfaction than those who work in the office "
           "every day. Therefore, if Firm X allowed all its employees to work from home two days a week, their job satisfaction would rise.",
           "The argument depends on which of the following assumptions?", [
            (True, "The employees who work from home two days a week were not already more satisfied with their jobs before they began doing so.",
             "inkor qilsak: ular avvaldan mamnunroq edi — farq uydan ishlashdan emas; argument yiqiladi."),
            (False, "Working from home reduces the cost of running the office.", "xarajat — mavzudan tashqari."),
            (False, "Job satisfaction is the most important factor in productivity.", "argument mahsuldorlik haqida emas."),
            (False, "Employees who work in the office every day are dissatisfied with their jobs.", "juda kuchli — kamroq mamnun boʻlishi yetarli."),
            (False, "Firm X's competitors already allow employees to work from home.", "mavzudan tashqari."),
        ], "Bogʻliqlik → sabab: muallif mamnunlikni uydan ishlash keltirib chiqargan deb oladi. Teskari sabab yoʻqligi — taxmin."),
        cr("A city plans to reduce the number of accidents at a busy intersection by installing a traffic light there. Most accidents at "
           "the intersection happen when drivers misjudge the gaps in oncoming traffic.",
           "The city's plan depends on which of the following assumptions?", [
            (True, "Drivers will generally obey the traffic light.", "inkor qilsak — svetofor hech narsani oʻzgartirmaydi."),
            (False, "The traffic light will be installed within a year.", "vaqt — reja ishlashiga taʼsir qilmaydi."),
            (False, "Traffic lights are expensive to install.", "xarajat — mavzudan tashqari."),
            (False, "No accidents will happen at the intersection after the light is installed.", "juda kuchli — kamayish yetarli."),
            (False, "Other intersections in the city have fewer accidents.", "boshqa chorrahalar haqida — mavzudan tashqari."),
        ], "Reja savolida taxmin — rejaning maqsadga yetishi uchun nima toʻgʻri boʻlishi kerak."),
        cr("Attendance at the city museum fell last year. The museum's director concludes that the admission fee introduced at the start "
           "of last year caused the fall.",
           "The director's conclusion depends on which of the following assumptions?", [
            (True, "Attendance did not fall mainly because of some other change, such as a reduction in the number of exhibitions.",
             "inkor qilsak: boshqa sabab asosiy — xulosa yiqiladi."),
            (False, "The admission fee is higher than the fees at other museums.", "shart emas — har qanday toʻlov taʼsir qilishi mumkin."),
            (False, "Attendance will rise again if the fee is removed.", "kelajak haqida — sabab haqidagi xulosa uchun shart emas."),
            (False, "Most visitors complained about the fee.", "shart emas."),
            (False, "The museum's costs rose last year.", "mavzudan tashqari."),
        ], "Sabab haqidagi har bir xulosa «boshqa sabab yoʻq» degan taxminga tayanadi."),
        cr("The number of applications to the university's business program rose by 30 percent this year. The admissions office "
           "concludes that the program has become more popular among students.",
           "The admissions office's conclusion depends on which of the following assumptions?", [
            (True, "The rise in applications does not mostly reflect each student applying to more programs than in previous years.",
             "inkor qilsak: talabalar soni oʻzgarmagan, faqat har biri koʻproq ariza bergan — mashhurlik oshmagan."),
            (False, "The business program is the university's largest program.", "hajm — mavzudan tashqari."),
            (False, "Applications to the university's other programs fell this year.", "shart emas."),
            (False, "Most of the applicants will be admitted.", "qabul — xulosaga taʼsir qilmaydi."),
            (False, "The quality of the program improved this year.", "sabab haqida — xulosa uchun shart emas."),
        ], "«Arizalar» va «mashhurlik» — har xil narsa. Boʻshliq: ariza soni = qiziquvchilar soni deb olinyapti."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Juda kuchli</b> variant («No accidents will happen…») — argument bunchalik koʻp narsaga muhtoj emas. "
                          "<b>Xarajat</b> varianti — reja qimmat boʻlishi uning ishlamasligini koʻrsatmaydi. "
                          "<b>Kuchaytiruvchi, lekin zaruriy emas</b> variant — inkor qilinganda argument baribir turadi.")
            + NOTE.format("Assumption va strengthen savollari oʻxshaydi, lekin farq bor: taxmin <b>zarur</b> (inkori argumentni yiqitadi), "
                          "kuchaytiruvchi esa faqat <b>yordam beradi</b>. Inkor qilish testi aynan shu farqni ajratadi.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("assumption", "yashirin taxmin"), ("necessary", "zaruriy"), ("negation test", "inkor qilish testi"),
                     ("gap", "boʻshliq"), ("depends on", "… ga tayanadi"), ("causation", "sabab-natija")])
            + "<h3>Xulosa</h3><ul><li>Taxmin — dalil va xulosa orasidagi boʻshliq.</li><li>Xulosadagi yangi tushunchani qidiring.</li>"
            "<li>Inkor qiling: argument yiqilsa — zaruriy taxmin.</li><li>Sabab xulosalari «boshqa sabab yoʻq» ga tayanadi.</li></ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 12 — weaken and strengthen
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_CR,
    "title": "GMAT Verbal 12: Weaken and Strengthen — Attacking and Supporting the Gap",
    "summary": "Zaiflashtirish va kuchaytirish: boshqa sabab, taqqoslash guruhi, vakillik va rejaning maqsadga yetishi.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Boʻshliqqa hujum va boʻshliqni yopish</h2>"
            "<p>Oldingi darsda boʻshliqni topdik. Endi u bilan ishlaymiz: <mark>weaken</mark> savoli boʻshliqni "
            "kengaytiradigan yangi faktni, <mark>strengthen</mark> savoli uni yopadiganini soʻraydi. Ikkalasida ham "
            "«<b>if true</b>» degan iborani unutmang: variant toʻgʻri deb qabul qilinadi — uning rostligini muhokama qilmaysiz.</p>"
            '<span class="sr-time">⏱ Weaken / strengthen — ~2 daqiqa</span>'
        )},
        {"rich_text": (
            "<h3>Toʻrt koʻp uchraydigan shakl</h3>"
            + steps([
                "<p><strong>Boshqa sabab.</strong> «X dan keyin Y» — Y ni boshqa narsa keltirib chiqargan boʻlsa-chi? Weaken shunday ishlaydi; "
                "strengthen esa boshqa sababni yoʻqqa chiqaradi.</p>",
                "<p><strong>Taqqoslash guruhi.</strong> X boʻlmagan joyda Y ham boʻlmadi — kuchaytiradi; X boʻlmagan joyda ham Y boʻldi — zaiflashtiradi.</p>",
                "<p><strong>Vakillik.</strong> Soʻrovnoma yoki tajriba butun guruhni aks ettiradimi? Faqat shanba kungi xaridorlar — barcha xaridorlar emas.</p>",
                "<p><strong>Reja.</strong> Reja maqsadga yetadimi? Maqsadga yetishga toʻsqinlik qiladigan fakt — weaken; xarajat esa odatda emas.</p>",
            ])
        )},
        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            '<div class="sr-passage"><p>To reduce the time customers spend waiting in line, a bank plans to open two more teller windows '
            "during lunchtime, when lines are longest.</p></div>"
            "<p>Maqsad — kutish vaqtini qisqartirish. Reja — koʻproq kassa oynasi. Boʻshliq: kutish aynan kassa oynasida boʻladimi? "
            "Agar navbatning asosiy qismi hamma oʻtishi shart boʻlgan <b>xavfsizlik nuqtasida</b> boʻlsa, qoʻshimcha oynalar "
            "kutishni kamaytirmaydi — bu weaken. «Oynalar uchun qoʻshimcha kassir yollash kerak» esa rejaning <b>narxi</b>, "
            "maqsadga yetishini rad etmaydi.</p>"
            + TIP.format("Reja savolida doim maqsadni bir jumlada yozing va har bir variantni «bu maqsadga yetishni toʻxtatadimi?» deb tekshiring.")
        )},
        cr("Since a new manager arrived at the company's Andijan branch, the branch's monthly sales have risen by 15 percent. The regional "
           "director concludes that the new manager's leadership is responsible for the increase.",
           "Which of the following, if true, most seriously weakens the director's conclusion?", [
            (True, "During the same period, a large factory opened near the branch and the local population grew sharply.",
             "boshqa sabab — savdo menejersiz ham oshgan boʻlishi mumkin."),
            (False, "The new manager has ten years of experience in retail banking.", "biroz kuchaytiradi — teskari yoʻnalish."),
            (False, "Employees at the branch say they like working with the new manager.", "mamnunlik — savdoga sabab ekanini rad etmaydi."),
            (False, "Sales at the company's other branches did not change during the same period.", "taqqoslash guruhi — kuchaytiradi."),
            (False, "The new manager plans to hire two more salespeople next year.", "kelajak — oʻtgan oʻsishga taʼsir qilmaydi."),
        ], "Boshqa sabab — sabab haqidagi xulosani zaiflashtirishning eng toʻgʻri yoʻli."),
        cr("A delivery company found that drivers who completed a defensive-driving course had 30 percent fewer accidents in the following year "
           "than drivers who did not. The company concludes that the course reduces accidents.",
           "Which of the following, if true, most strengthens the company's conclusion?", [
            (True, "Before the course, the drivers who later took it had about the same accident rate as the drivers who did not.",
             "guruhlar avval teng edi — farq kursdan keyin paydo boʻlgan."),
            (False, "The course takes two days to complete.", "mavzudan tashqari."),
            (False, "Drivers who took the course were, on average, more experienced than those who did not.", "boshqa sabab — zaiflashtiradi."),
            (False, "Some drivers who took the course still had accidents.", "30% kamayish bilan mos keladi — hech narsa qoʻshmaydi."),
            (False, "Other companies offer similar courses to their drivers.", "mavzudan tashqari."),
        ], "Kuchaytirish: guruhlar boshqa jihatdan farq qilmasligini koʻrsatish."),
        cr("To reduce the time customers spend waiting in line, a bank branch in Tashkent plans to open two more teller windows during lunchtime, when its lines are longest.",
           "Which of the following, if true, most strongly suggests that the bank's plan will NOT achieve its goal?", [
            (True, "Most of the waiting time at lunchtime is spent at the single security desk that every customer must pass before reaching a teller.",
             "navbat oynalarda emas — qoʻshimcha oyna kutishni qisqartirmaydi."),
            (False, "Opening the extra windows will require hiring part-time tellers.", "xarajat — maqsadga yetishni rad etmaydi."),
            (False, "Customers are often impatient at lunchtime.", "rejaning ishlashiga taʼsir qilmaydi."),
            (False, "Lines at the bank are shortest in the early morning.", "ertalab — mavzudan tashqari."),
            (False, "Other banks in the area have more teller windows.", "taqqoslash — rejaning natijasini koʻrsatmaydi."),
        ], "Reja savolida «narx» tuzogʻi: qimmat reja ham maqsadga yetishi mumkin."),
        cr("In a survey of customers leaving our Chilonzor store on a Saturday, 85 percent said they would like the store to open on Sundays. "
           "So most of our customers want the store to open on Sundays.",
           "Which of the following, if true, most seriously weakens the argument?", [
            (True, "Customers who shop on Saturdays are much more likely than the store's weekday customers to prefer shopping at weekends.",
             "namuna vakil emas — soʻrov aynan dam olish kunini afzal koʻradiganlardan olingan; boshqa xaridorlar boshqacha javob berishi mumkin."),
            (False, "The survey asked customers only five questions.", "savollar soni — vakillikka taʼsir qilmaydi."),
            (False, "Opening on Sundays would increase the store's costs.", "xarajat — xaridorlar nimani xohlashini rad etmaydi."),
            (False, "Some other stores in Tashkent already open on Sundays.", "mavzudan tashqari."),
            (False, "The 85 percent figure is higher than the result of a similar survey last year.", "xulosani zaiflashtirmaydi."),
        ], "Soʻrovnoma xulosasi — namuna butun guruhni aks ettiradi degan taxminga tayanadi."),
        cr("When a supermarket moved its fresh bread from the back of the store to the entrance, sales of bread rose by 25 percent. "
           "The store's manager concludes that the new location caused the rise.",
           "Which of the following, if true, most strengthens the manager's conclusion?", [
            (True, "During the same period, the price of the bread and the number of shoppers at the store did not change.",
             "ikki muqobil sabab yoʻqqa chiqdi — joy sabab ekani kuchayadi."),
            (False, "The bread is baked fresh every morning.", "oldin ham shunday edi — farqni tushuntirmaydi."),
            (False, "Customers often buy bread together with milk.", "mavzudan tashqari."),
            (False, "The store's sales of other products also rose by 25 percent during the same period.", "umumiy oʻsish — zaiflashtiradi."),
            (False, "The manager had suggested moving the bread a year earlier.", "tarix — sababni koʻrsatmaydi."),
        ], "Kuchaytirish koʻpincha muqobil sabablarni yoʻqqa chiqarish orqali ishlaydi."),
        {"rich_text": (
            "<h3>Tuzoqlar</h3>"
            + WARN.format("<b>Teskari yoʻnalish</b> — weaken soʻralganda kuchaytiruvchi variant (koʻpincha taqqoslash guruhi). "
                          "<b>Xarajat</b> — reja savollarida. <b>«Kimdir hali ham…»</b> — «some drivers still had accidents» "
                          "30% kamayishni rad etmaydi.")
            + NOTE.format("«If true» — variantning rostligini tekshirmang. Bizda koʻpchilik «bu rostmi?» deb shubha qiladi va vaqt "
                          "yoʻqotadi. Variant toʻgʻri deb qabul qilinadi; savol faqat uning argumentga <b>taʼsiri</b> haqida.")
            + "<h3>Kalit soʻzlar</h3>"
            + cards([("weaken", "zaiflashtirmoq"), ("strengthen", "kuchaytirmoq"), ("alternative cause", "boshqa sabab"),
                     ("comparison group", "taqqoslash guruhi"), ("representative sample", "vakil namuna"), ("goal of the plan", "rejaning maqsadi")])
            + "<h3>Xulosa</h3><ul><li>Weaken — boʻshliqni kengaytiradi; strengthen — yopadi.</li>"
            "<li>Boshqa sabab, taqqoslash guruhi, vakillik, rejaning maqsadi — toʻrt asosiy shakl.</li>"
            "<li>Xarajat rejaning ishlamasligini koʻrsatmaydi.</li><li>«If true» — rostligini muhokama qilmang.</li></ul>"
        )},
    ],
},
]
