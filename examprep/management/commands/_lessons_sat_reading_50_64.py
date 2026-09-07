# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 50-54 and 60-64.

Covers "Matndan dalil (Command of Evidence — Textual)" (50-54) and
"Grafik va jadvaldan dalil (Command of Evidence — Quantitative)" (60-64).
See toc_sat_reading.txt and STYLE_GUIDE_SAT_RW.md.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_COE_T = {
    "title":   "Matndan dalil (Command of Evidence — Textual)",
    "summary": "Berilgan da'voni qaysi iqtibos isbotlaydi, va qaysi topilma "
               "gipotezani kuchaytiradi yoki kuchsizlantiradi.",
    "icon":    "bi-quote",
    "order":   6,
}

TOPIC_COE_Q = {
    "title":   "Grafik va jadvaldan dalil (Command of Evidence — Quantitative)",
    "summary": "Jadval yoki grafikdan to'g'ri raqamni olib, uni da'voga bog'lash — "
               "va aniq raqamning da'voni isbotlamasligini payqash.",
    "icon":    "bi-bar-chart",
    "order":   7,
}

TIP   = ('<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> {}</div>')
WARN  = ('<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> {}</div>')
NOTE  = ('<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> {}</div>')
EXAMP = ('<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> {}</div>')


def why(rows):
    """Build an .sr-why choice autopsy. rows = [(ok, choice_text, uzbek_reason), ...]

    The choice text MUST start with the choice's own opening words — the pupil finds
    the row by scanning it against a shuffled list (guide §6).
    """
    out = ['<div class="sr-why">']
    for ok, choice, reason in rows:
        kind = 'ok' if ok else 'no'
        tag = "TO‘G‘RI" if ok else "TUZOQ"
        out.append(
            f'<div class="sr-why__row sr-why__row--{kind}">'
            f'<span class="sr-why__tag">{tag}</span>'
            f'<span class="sr-why__text"><b>{choice}</b> — {reason}</span></div>'
        )
    out.append('</div>')
    return ''.join(out)


def q(passage, stem):
    """Single passage pane + a bolded exam stem."""
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def data_q(title, table_html, passage, stem):
    """A Quantitative question: figure card, then the text, then the stem.

    The table lives inside .sr-data__scroll so a wide one scrolls itself on a phone
    instead of pushing the page sideways (guide §3).
    """
    return (f'<div class="sr-data"><p class="sr-data__title">{title}</p>'
            f'<div class="sr-data__scroll">{table_html}</div></div>'
            f'<div class="sr-passage">{passage}</div>'
            f'<p><strong>{stem}</strong></p>')


def table(headers, rows):
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 50
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_T,
    "title": "SAT R&W 50: Command of Evidence — Which Quotation Proves the Claim?",
    "summary": "Da'vo beriladi, to'rtta iqtibos beriladi: qaysi biri aynan o'sha "
               "da'voni ko'taradi. Mavzuga mos kelish yetarli emas — isbot kerak.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>Da'vo va uni ko'taradigan iqtibos</h2>"
            "<p><strong>Command of Evidence</strong> — <em>Information and Ideas</em> "
            "domenining ikkinchi turi, va uning ikki yarmi bor: "
            "<u>matndan dalil</u> (bu mavzu) va <u>grafikdan dalil</u> "
            "(60-darsdan boshlab).</p>"
            "<p>Matndan dalil savolining shakli doim bir xil: bir talaba biror "
            "asar haqida <mark>da'vo</mark> yozgan, va sizdan o'sha da'voni "
            "<mark>isbotlaydigan iqtibos</mark>ni tanlash so'raladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><em>While researching a topic, a student "
                "has written the following claim: …</em></p>"
                "<p style=\"margin:0;\"><em>Which quotation from the story most "
                "effectively illustrates the claim?</em></p>")
            + "<p>To'rtta variant — asardan olingan to'rtta haqiqiy iqtibos. "
            "Hammasi asarda bor. Faqat bittasi da'voni <u>isbotlaydi</u>.</p>"
            + '<span class="sr-time">⏱ ~60 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Bu savolning butun siri</h3>"
            + EXAMP.format(
                "<p style=\"font-size:1.08em;margin:0;\"><strong>Iqtibos da'voning "
                "MAVZUSIGA emas, uning ICHIDAGI FIKRGA mos kelishi kerak.</strong></p>")
            + "<p>Misol bilan tushuntiraman. Da'vo shunday bo'lsin:</p>"
            + "<p style=\"padding-left:16px;border-left:3px solid #cbd5e1;\">"
            "<em>The narrator's memory of the house grows less reliable as the story "
            "goes on.</em></p>"
            + "<p>Bu da'voda uchta element bor: <strong>(1)</strong> xotira, "
            "<strong>(2)</strong> uy haqida, <strong>(3)</strong> "
            "<u>ishonchliligi pasayadi</u>.</p>"
            + "<p>Uy haqidagi iqtibos — mavzuga mos, lekin yetarli emas. Xotira "
            "haqidagi iqtibos ham yetarli emas. Kerakli iqtibos "
            "<mark>xotiraning noaniqlashuvini ko'rsatishi</mark> shart — masalan "
            "hikoyachi ikki xil narsani eslasa, yoki o'zining eslaganiga shubha "
            "qilsa.</p>"
            + WARN.format(
                "Bu turning bosh tuzog'i: <strong>mavzuga mos, da'voga mos "
                "emas</strong>. To'rtta iqtibosning ikki-uchtasi da'vo bilan bir "
                "mavzuda bo'ladi. Ular sizni «tanish so'z» bilan tortadi. "
                "Da'voning <u>fe'liga</u> qarang — u nima "
                "<u>bo'layotganini</u> aytadi.")
        )},

        {"rich_text": (
            "<h3>Usul — uch qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Da'voni bo'laklarga "
              "ajrating.</strong> Kim? Nima? Va eng muhimi — <u>qanday "
              "o'zgarish yoki qanday xususiyat</u>? Oxirgisi javobni "
              "belgilaydi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. O'zingizga ayting: qanday "
              "iqtibos buni isbotlardi?</strong> Variantlarni ochmasdan. "
              "«Hikoyachi o'zining eslaganiga shubha qilayotgan jumla "
              "kerak.»</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Har iqtibosni sinang:</strong> "
              "«agar men bu iqtibosni ko'rsatsam, da'vo isbotlanadimi?» "
              "Javob «ha, lekin qisman» bo'lsa — bu <u>yo'q</u> degani.</p></div>"
            + '</div>'
            + NOTE.format(
                "Haqiqiy imtihonda iqtiboslar <u>haqiqiy</u> asarlardan olinadi va "
                "muallif nomi beriladi. Bu darsda hikoyalar biz yozganimiz — savol "
                "shakli va ko'nikma aynan bir xil, faqat hech kimga noto'g'ri gap "
                "yopishtirmaymiz.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + '<div class="sr-passage">'
            + "<p>While studying a short story about a man returning to a village he "
              "left as a child, a student has written the following claim:</p>"
            + "<p><em>The narrator treats the changes he finds in the village as though "
              "they were done to him personally.</em></p>"
            + '</div>'
            + "<p><strong>Which quotation from the story most effectively illustrates "
              "the claim?</strong></p>"
            + choices_html([
                "&ldquo;The road had been widened at some point, and a line of young "
                "trees ran along the far side of it.&rdquo;",
                "&ldquo;They had taken down the gate, he thought, and said nothing to "
                "anybody, and expected him to walk past the gap as if he had never "
                "known it.&rdquo;",
                "&ldquo;He had been away for nineteen years, and for eleven of them he "
                "had not written.&rdquo;",
                "&ldquo;The new houses at the edge of the village were larger than the "
                "old ones and stood further apart.&rdquo;",
            ])
            + '<span class="sr-time">⏱ ~60 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — da'voni bo'laklarga ajratamiz:</strong></p>"
            "<ul>"
            "<li><u>Kim:</u> hikoyachi.</li>"
            "<li><u>Nima:</u> qishloqdagi o'zgarishlar.</li>"
            "<li><u>Qanday munosabat:</u> <mark>o'ziga qarshi qilingandek</mark> "
            "qabul qiladi (<em>as though they were done to him personally</em>).</li>"
            "</ul>"
            "<p>Uchinchi bo'lak — javobning kaliti. Bizga o'zgarish tasviri emas, "
            "hikoyachining <u>shaxsiy ranjishi</u> kerak.</p>"
            "<p><strong>2-qadam — bashorat:</strong> «kimdir mendan so'ramay qildi», "
            "«mendan yashirishdi», «meni hisobga olishmadi» ma'nosidagi jumla.</p>"
            + why([
                (True, "&ldquo;They had taken down the gate, he thought, and said nothing to anybody, and expected him to walk past the gap&rdquo;",
                 "uchala bo'lakni ham qamraydi. <em>They</em> — nomsiz aybdorlar; "
                 "<em>said nothing to anybody</em> — go'yo unga xabar berish kerak "
                 "edi; <em>expected him to</em> — o'zgarish shaxsan unga qaratilgan. "
                 "Bu shaxsiy ranjishning aniq tasviri."),
                (False, "&ldquo;The road had been widened at some point, and a line of young trees ran along the far side&rdquo;",
                 "<strong>mavzuga mos, da'voga mos emas</strong> — bu darsning bosh "
                 "tuzog'i. O'zgarish bor, lekin hikoyachining munosabati yo'q: "
                 "jumla xolis, hatto <em>at some point</em> — befarq."),
                (False, "&ldquo;The new houses at the edge of the village were larger than the old ones&rdquo;",
                 "yana o'zgarish tasviri, yana munosabatsiz. Ikkita bir xil "
                 "tuzoqning bo'lishi tasodif emas: SAT sizni mavzu bilan "
                 "to'ldiradi."),
                (False, "&ldquo;He had been away for nineteen years, and for eleven of them he had not written&rdquo;",
                 "bu hikoyachining <u>o'z aybi</u> haqida — da'voning teskarisiga "
                 "ishora qiladi. Qishloqdagi o'zgarish ham, unga munosabat ham "
                 "yo'q."),
            ])
            + TIP.format(
                "E'tibor bering: to'g'ri iqtibos <u>eng uzuni</u> edi va uchta fe'l "
                "olib yurardi. Bu tez-tez shunday bo'ladi — da'vo bir necha "
                "elementdan iborat bo'lsa, ularning hammasini bitta qisqa jumla "
                "ko'tara olmaydi. Lekin buni qoida qilib olmang: "
                "<strong>uzunlik dalil emas</strong>, shunchaki tez-tez "
                "uchraydigan naqsh.")
        )},

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a young woman who has taken a job in a "
                "town where she knows nobody, a student has written the following "
                "claim:</p>"
                "<p><em>Malika measures her progress in the new town by the small "
                "routines she is able to establish, rather than by the work she came "
                "for.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“By the second month the man at the bread shop had begun putting hers aside, and she found she counted that as an achievement bigger than the contract she had signed.”", "is_correct": True},
                {"text": "“The office was on the fourth floor of a building with no lift, and the stairwell smelled of paint all through October.”", "is_correct": False},
                {"text": "“She had been hired to reorganise a filing system that three people before her had abandoned.”", "is_correct": False},
                {"text": "“She wrote to her mother once a week and described the town as pleasant.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo bo'laklari:</strong> (1) Malika o'z "
                "muvaffaqiyatini o'lchaydi, (2) <u>kichik odatlar</u> bilan, "
                "(3) <u>ish o'rniga</u>. Uchinchi bo'lak — solishtirish — javobda "
                "bo'lishi shart.</p>"
                + why([
                    (True, "“By the second month the man at the bread shop had begun putting hers aside, and she found she counted that as an achievement bigger than the contract she had signed.”",
                     "uchala bo'lak ham bor: kichik odat (non do'koni), o'lchov "
                     "(<em>counted that as an achievement</em>) va ish bilan "
                     "solishtirish (<em>bigger than the contract</em>)."),
                    (False, "“She had been hired to reorganise a filing system that three people before her had abandoned.”",
                     "<strong>mavzuga mos, da'voga mos emas</strong>: ish haqida, "
                     "lekin Malikaning o'lchovi haqida hech nima demaydi."),
                    (False, "“The office was on the fourth floor of a building with no lift, and the stairwell smelled of paint all through October.”",
                     "atmosfera tasviri. Kundalik hayot tafsiloti bor, lekin u "
                     "<u>odat</u> ham emas, <u>yutuq</u> ham emas."),
                    (False, "“She wrote to her mother once a week and described the town as pleasant.”",
                     "<strong>eng jozibali tuzoq</strong>: haftalik xat — bu odat! "
                     "Lekin da'vo odatni <u>muvaffaqiyat o'lchovi</u> deb aytadi, "
                     "va bu iqtibosda hech qanday o'lchov yo'q. Yarim bo'lak "
                     "yetarli emas."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story told by an elderly man about his years as a "
                "railway signalman, a student has written the following claim:</p>"
                "<p><em>The narrator's account of his working life is more precise about "
                "equipment than about the people he worked beside.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“The lever for the down home signal took a half turn and a push, never a pull; there was a fellow on the late shift with me for six years, a tall man, and I could not tell you his name now.”", "is_correct": True},
                {"text": "“The box had eleven levers, of which nine were in use, and a stove that drew badly whenever the wind came from the east.”", "is_correct": False},
                {"text": "“We were four men to a box in those days, and we saw more of each other than of our families.”", "is_correct": False},
                {"text": "“I was on the railway for thirty-one years and never once missed a shift through illness.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo bo'laklari:</strong> hikoyachi asboblarni "
                "<u>aniq</u>, odamlarni esa <u>noaniq</u> tasvirlaydi. Bu "
                "<mark>taqqoslash</mark> — demak iqtibosda <u>ikkalasi ham</u> "
                "bo'lishi kerak.</p>"
                + why([
                    (True, "“The lever for the down home signal took a half turn and a push, never a pull; there was a fellow on the late shift with me for six years, a tall man, and I could not tell you his name now.”",
                     "yagona iqtibos ikkala tomonni ham ko'rsatadi: richag haqida "
                     "juda aniq (<em>a half turn and a push, never a pull</em>) va "
                     "olti yillik hamkasb haqida — hatto ismi ham yodida yo'q. "
                     "Taqqoslash bitta jumlaning ichida."),
                    (False, "“The box had eleven levers, of which nine were in use, and a stove that drew badly…”",
                     "<strong>yarim to'g'ri</strong> va eng ko'p tanlanadigan: "
                     "aniqlik bor (o'n bitta, to'qqiztasi). Lekin odamlar umuman "
                     "yo'q, ya'ni taqqoslashning ikkinchi yarmi yetishmaydi."),
                    (False, "“We were four men to a box in those days, and we saw more of each other than of our families.”",
                     "odamlar haqida, va hatto raqam ham bor — lekin bu "
                     "<u>noaniqlik</u> emas. Da'vo odamlar haqida "
                     "gapirilmasligini emas, <u>noaniq</u> gapirilishini "
                     "aytyapti."),
                    (False, "“I was on the railway for thirty-one years and never once missed a shift through illness.”",
                     "hikoyachining o'zi haqida — na asbob, na hamkasblar. "
                     "Raqam bor, lekin da'vo bilan aloqasi yo'q."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about two sisters who inherit a shop, a "
                "student has written the following claim:</p>"
                "<p><em>The younger sister avoids stating her disagreement directly and "
                "expresses it through what she chooses to do instead.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“She said the new sign was a good idea, and she said it twice, and on Thursday she painted the old one and hung it in the back room where the deliveries came.”", "is_correct": True},
                {"text": "“She told her sister plainly that the new sign was a waste of money they did not have.”", "is_correct": False},
                {"text": "“The two of them had run the shop together since their father's illness and had never once quarrelled in front of a customer.”", "is_correct": False},
                {"text": "“She was six years younger than her sister and had always been the quieter of the two.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo bo'laklari:</strong> (1) ochiq aytmaydi, "
                "(2) <u>o'rniga</u> — harakat bilan bildiradi. Ikkovi ham "
                "kerak.</p>"
                + why([
                    (True, "“She said the new sign was a good idea, and she said it twice, and on Thursday she painted the old one and hung it in the back room…”",
                     "birinchi yarmi — ochiq rozilik (hatto ikki marta, ya'ni "
                     "shubhali darajada); ikkinchi yarmi — eski taxtani bo'yab "
                     "osib qo'yish, ya'ni haqiqiy fikri. Ikki bo'lak ham bitta "
                     "jumlada."),
                    (False, "“She told her sister plainly that the new sign was a waste of money they did not have.”",
                     "<strong>to'g'ridan-to'g'ri teskari</strong>: <em>plainly</em> "
                     "— aynan da'vo rad etayotgan narsa. Mavzu to'g'ri, yo'nalish "
                     "noto'g'ri."),
                    (False, "“The two of them had run the shop together since their father's illness and had never once quarrelled in front of a customer.”",
                     "janjal qilmaslik — bu <u>ochiq aytmaslik</u> emas, va bu "
                     "yerda hech qanday harakat orqali ifoda yo'q. Fon "
                     "ma'lumoti."),
                    (False, "“She was six years younger than her sister and had always been the quieter of the two.”",
                     "<strong>xarakter tavsifi, dalil emas</strong>. «Kamgap» "
                     "bo'lish da'voni tushuntiradi, lekin uni ko'rsatmaydi — "
                     "da'vo aniq bir <u>xatti-harakat</u> haqida."),
                ])
                + TIP.format(
                    "To'rtala savolda ham to'g'ri javob <u>ikki bo'lakni bitta "
                    "jumlada</u> birlashtirgan iqtibos bo'ldi. Bu tasodif emas: "
                    "da'vo ikki elementdan iborat bo'lsa, uni faqat ikkovini ham "
                    "ko'rsatgan iqtibos isbotlaydi. Da'vodagi "
                    "<em>rather than</em>, <em>instead</em>, <em>more … than</em> "
                    "iboralarini qidiring — ular «ikki bo'lak kerak» degan "
                    "signal.")
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story in which an old man describes the covered "
                "market of his childhood, a student has written the following claim:</p>"
                "<p><em>The narrator's fondness for the old market survives his "
                "recognition that it was inconvenient.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "\u201cIt took forty minutes to buy what a supermarket now sells you in six, and I have not enjoyed shopping since.\u201d", "is_correct": True},
                {"text": "\u201cThe stalls were arranged to no system at all, so that the man selling knives stood between two women selling apricots.\u201d", "is_correct": False},
                {"text": "\u201cI went there every week from the age of nine until the year they cleared the ground.\u201d", "is_correct": False},
                {"text": "\u201cThe market had stood on that corner since before the road outside it was paved.\u201d", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da\u2019vo bo\u2018laklari:</strong> (1) noqulay ekanini "
                "<u>tan oladi</u>, (2) shunga qaramay <u>mehri qolgan</u>. "
                "<em>survives</em> fe\u2019li ikki bo\u2018lakni talab qiladi \u2014 "
                "50-darsning asosiy qoidasi.</p>"
                + why([
                    (True, "\u201cIt took forty minutes to buy what a supermarket now sells you in six, and I have not enjoyed shopping since.\u201d",
                     "ikkala bo\u2018lak bitta jumlada: qirq daqiqa ↔ olti daqiqa "
                     "(noqulaylik ochiq tan olingan) va <em>have not enjoyed "
                     "shopping since</em> (mehr saqlanib qolgan)."),
                    (False, "\u201cThe stalls were arranged to no system at all, so that the man selling knives stood between two women selling apricots.\u201d",
                     "faqat <u>noqulaylik</u> \u2014 va u yerda mehr ham, baho ham "
                     "yo\u2018q. <strong>Yarim bo\u2018lak yetarli emas.</strong>"),
                    (False, "\u201cI went there every week from the age of nine until the year they cleared the ground.\u201d",
                     "muntazam borish bog\u2018lanishni <u>taxmin qildiradi</u>, lekin "
                     "uni aytmaydi \u2014 va noqulaylikni umuman eslatmaydi. "
                     "Bu odat, mehr emas."),
                    (False, "\u201cThe market had stood on that corner since before the road outside it was paved.\u201d",
                     "bozorning yoshi haqida fakt: na mehr, na noqulaylik. "
                     "Da\u2019vodagi ikki bo\u2018lakning ham biri yo\u2018q."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a claim</div><div class="pp-card-back">da\'vo</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to illustrate a claim</div><div class="pp-card-back">da\'voni misol bilan ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a quotation</div><div class="pp-card-back">iqtibos, ko\'chirma</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">rather than ~</div><div class="pp-card-back">~ o\'rniga (ikki bo\'lak kerakligi signali)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to establish a routine</div><div class="pp-card-back">odat, tartib o\'rnatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">plainly</div><div class="pp-card-back">ochiq, to\'g\'ridan-to\'g\'ri</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to set aside</div><div class="pp-card-back">ajratib qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an account of ~</div><div class="pp-card-back">~ haqidagi hikoya, bayon</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Iqtibos da'voning <strong>mavzusiga</strong> emas, uning "
              "<strong>ichidagi fikrga</strong> mos kelishi kerak.</li>"
              "<li>Da'voni <u>bo'laklarga ajrating</u>; oxirgi bo'lak "
              "(o'zgarish yoki xususiyat) javobni belgilaydi.</li>"
              "<li>Da'voda <em>rather than · instead · more … than</em> bo'lsa — "
              "javob <strong>ikki bo'lakni ham</strong> ko'rsatishi kerak.</li>"
              "<li>«Ha, lekin qisman» = <u>yo'q</u>.</li>"
              "<li>Xarakter tavsifi dalil emas: da'vo xatti-harakat haqida bo'lsa, "
              "iqtibos ham harakat ko'rsatsin.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 51
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_T,
    "title": "SAT R&W 51: Matching the Claim Word for Word Before You Read the Choices",
    "summary": "Da'vodagi kichik so'zlar — only, without, more than, never, begins to — "
               "javobni belgilaydi; ularni oldindan belgilash butun savolni yechadi.",
    "order": 51,
    "blocks": [
        {"rich_text": (
            "<h2>Da'vodagi kichik so'zlar</h2>"
            "<p>50-darsda ko'rdik: iqtibos da'voning <u>ichidagi fikrga</u> mos "
            "kelishi kerak. Endi shu ish qanday qilinishini aniqlashtiramiz.</p>"
            "<p>Da'voni o'qiyotganda ko'zingiz katta so'zlarga tushadi — "
            "<em>narrator</em>, <em>village</em>, <em>memory</em>. Lekin javobni "
            "deyarli har doim <mark>kichik so'zlar</mark> belgilaydi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>So'z</th><th>Nimani talab qiladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>only</em></td><td>Boshqa hech narsa emasligi ham "
              "ko'rinishi kerak</td></tr>"
              "<tr><td><em>without</em></td><td>Nimanidir <u>yo'qligi</u> "
              "iqtibosda sezilishi kerak</td></tr>"
              "<tr><td><em>begins to · comes to</em></td><td>O'zgarish: oldin "
              "boshqacha edi</td></tr>"
              "<tr><td><em>more … than · rather than</em></td><td>Ikki tomon "
              "ham iqtibosda bo'lsin</td></tr>"
              "<tr><td><em>despite · even though</em></td><td>Ikki qarama-qarshi "
              "narsa yonma-yon</td></tr>"
              "<tr><td><em>never · always</em></td><td>Bitta holat yetarli emas; "
              "takror yoki umumiy gap kerak</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul: da'voni belgilab chiqing</h3>"
            "<p>Variantlarni ochishdan oldin da'voni xayolan uch qismga bo'ling:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. EGA</strong> — kim yoki nima "
              "haqida? (hikoyachi? qahramon? matn?)</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. FE'L</strong> — u nima "
              "qilyapti? Bu odatda da'voning yuragi: <em>avoids · measures · "
              "treats · survives · grows less</em>.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. SHART</strong> — kichik "
              "so'zlar: <em>only · without · rather than · despite</em>. "
              "Ular <u>nechta bo'lak</u> kerakligini aytadi.</p></div>"
            + '</div>'
            + TIP.format(
                "Amaliy qoida: <strong>da'voda nechta shart so'zi bo'lsa, "
                "to'g'ri iqtibosda shuncha bo'lak bo'ladi.</strong> "
                "Shart so'zi yo'q bo'lsa — bir bo'lakli iqtibos yetadi. "
                "<em>rather than</em> bo'lsa — ikki bo'lak. Bu bitta qoida "
                "50-darsdagi to'rt savolning to'rttasini ham yechardi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + '<div class="sr-passage">'
            + "<p>While studying a story about a woman who has come back to teach in "
              "the school she attended as a child, a student has written the following "
              "claim:</p>"
            + "<p><em>Dilbar comes to see her old teachers differently without ever "
              "saying so to them.</em></p>"
            + '</div>'
            + "<p><strong>Which quotation from the story most effectively illustrates "
              "the claim?</strong></p>"
            + choices_html([
                "&ldquo;She had been frightened of Mahfuza Opa at nine and was still a "
                "little frightened of her at thirty-four.&rdquo;",
                "&ldquo;It had not occurred to her at nine that a teacher might be "
                "tired; she thought of it now every time she passed the staff room, and "
                "she said nothing about it to anyone.&rdquo;",
                "&ldquo;She told Mahfuza Opa that she had always admired her and that "
                "she hoped to teach as well one day.&rdquo;",
                "&ldquo;The staff room had the same three chairs and the same kettle it "
                "had had twenty-five years before.&rdquo;",
            ])
            + '<span class="sr-time">⏱ ~55 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim — da'voni belgilaymiz</h3>"
            "<ul>"
            "<li><strong>EGA:</strong> Dilbar.</li>"
            "<li><strong>FE'L:</strong> <em>comes to see … differently</em> — "
            "ya'ni <mark>o'zgarish</mark>: oldin boshqacha ko'rardi.</li>"
            "<li><strong>SHART:</strong> <em>without ever saying so to them</em> — "
            "<mark>ikkinchi bo'lak</mark>: aytmaydi.</li>"
            "</ul>"
            "<p>Ikkita shart bor, demak iqtibosda ikkita narsa ko'rinishi kerak: "
            "<u>qarash o'zgargani</u> va <u>indamagani</u>.</p>"
            + why([
                (True, "&ldquo;It had not occurred to her at nine that a teacher might be tired; she thought of it now every time she passed the staff room, and she said nothing about it to anyone.&rdquo;",
                 "ikkala shart ham bor: <em>at nine … now</em> (o'zgarish) va "
                 "<em>said nothing about it to anyone</em> (aytmaslik). "
                 "Nuqtali vergul ikki vaqtni yonma-yon qo'yadi."),
                (False, "&ldquo;She had been frightened of Mahfuza Opa at nine and was still a little frightened of her at thirty-four.&rdquo;",
                 "<em>at nine … at thirty-four</em> ikki vaqtni ko'rsatadi va "
                 "shuning uchun juda ishonarli. Lekin <em>still</em> — bu "
                 "<u>o'zgarmaslik</u>. Da'voning fe'li (<em>differently</em>) "
                 "aynan teskarisini talab qilyapti."),
                (False, "&ldquo;She told Mahfuza Opa that she had always admired her and that she hoped to teach as well one day.&rdquo;",
                 "ikkinchi shartni buzadi: u <u>aytyapti</u>. Va <em>always "
                 "admired</em> ham o'zgarishni inkor qiladi. Bitta iqtibos ikkala "
                 "shartga ham zid."),
                (False, "&ldquo;The staff room had the same three chairs and the same kettle it had had twenty-five years before.&rdquo;",
                 "vaqt o'tgani bor, lekin bu <u>xonaning</u> o'zgarmagani — "
                 "Dilbarning qarashi haqida hech nima demaydi. "
                 "<strong>Mavzuga mos, da'voga mos emas.</strong>"),
            ])
        )},

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a man who repairs musical instruments, "
                "a student has written the following claim:</p>"
                "<p><em>Tohir judges his own work by a standard nobody else in the shop "
                "applies.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“The customer was delighted and the foreman signed it off, and Tohir took it apart again that evening because the join showed under the lamp.”", "is_correct": True},
                {"text": "“He had repaired instruments for twenty-two years and had trained four of the six people who now worked beside him.”", "is_correct": False},
                {"text": "“The foreman told him more than once that the shop could not afford the hours he spent on a single violin.”", "is_correct": False},
                {"text": "“He kept his tools in the order his own teacher had kept them, and would not lend them.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'voni belgilaymiz:</strong> EGA — Tohir; "
                "FE'L — <em>judges his own work</em>; "
                "SHART — <em>by a standard <u>nobody else</u> applies</em>. "
                "Shart bitta, lekin kuchli: iqtibosda <mark>boshqalar rozi, u "
                "rozi emas</mark> ko'rinishi kerak.</p>"
                + why([
                    (True, "“The customer was delighted and the foreman signed it off, and Tohir took it apart again that evening because the join showed under the lamp.”",
                     "ikkala tomon ham bir jumlada: mijoz va usta rozi "
                     "(boshqalarning me'yori bajarildi), Tohir esa qayta ochdi "
                     "(o'z me'yori bajarilmadi)."),
                    (False, "“The foreman told him more than once that the shop could not afford the hours he spent on a single violin.”",
                     "<strong>eng jozibali tuzoq</strong>: ziddiyat bor va u "
                     "boshqalar bilan. Lekin bu <u>vaqt va pul</u> haqidagi "
                     "nizo — Tohirning ishni qanday <u>baholashi</u> haqida emas. "
                     "Da'voning fe'li <em>judges</em>, <em>argues</em> emas."),
                    (False, "“He had repaired instruments for twenty-two years and had trained four of the six people who now worked beside him.”",
                     "tajriba va mavqe haqida — me'yor haqida hech nima. "
                     "Xarakter foni."),
                    (False, "“He kept his tools in the order his own teacher had kept them, and would not lend them.”",
                     "shaxsiy odat, hatto o'jarlik — lekin bu <u>ishni "
                     "baholash</u> emas. Da'vo asboblar haqida emas, "
                     "<u>bajarilgan ish</u> haqida."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a boy sent to stay with relatives for a "
                "summer, a student has written the following claim:</p>"
                "<p><em>Sardor understands the household's rules by watching rather than "
                "by being told them.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“Nobody had said which chair was his uncle's; he worked it out on the second evening from the way the others left a space around it.”", "is_correct": True},
                {"text": "“His aunt explained on the first morning that the water was heated only in the evenings.”", "is_correct": False},
                {"text": "“He was eleven that summer and had never before slept a night outside his mother's house.”", "is_correct": False},
                {"text": "“The household kept different hours from his own: they ate late and rose late.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>SHART:</strong> <em>by watching <u>rather than</u> by "
                "being told</em> — 51-darsning qoidasi: <em>rather than</em> = "
                "<mark>ikki bo'lak</mark>. Iqtibosda <u>aytilmagani</u> ham, "
                "<u>o'zi payqagani</u> ham bo'lishi shart.</p>"
                + why([
                    (True, "“Nobody had said which chair was his uncle's; he worked it out on the second evening from the way the others left a space around it.”",
                     "<em>Nobody had said</em> (birinchi bo'lak) va <em>worked it "
                     "out … from the way the others</em> (ikkinchi bo'lak). "
                     "Nuqtali vergul ikkovini birlashtiradi."),
                    (False, "“His aunt explained on the first morning that the water was heated only in the evenings.”",
                     "<strong>to'g'ridan-to'g'ri teskari</strong>: bu qoida "
                     "unga <u>aytilgan</u>. Mavzu to'g'ri (uy qoidasi), yo'nalish "
                     "noto'g'ri."),
                    (False, "“The household kept different hours from his own: they ate late and rose late.”",
                     "qoida bor, lekin Sardor uni qanday bilib olgani yo'q — "
                     "na kuzatish, na aytilish. <strong>Yarim bo'lak "
                     "ham emas.</strong>"),
                    (False, "“He was eleven that summer and had never before slept a night outside his mother's house.”",
                     "fon ma'lumoti: yosh va tajriba. Da'voning hech qaysi "
                     "bo'lagiga tegmaydi."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about an interpreter working at a border "
                "post, a student has written the following claim:</p>"
                "<p><em>Nilufar is aware that her choice of words changes the outcome for "
                "the people she interprets for, and she never lets that awareness show in "
                "her voice.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“She knew that ‘he refused’ and ‘he declined’ would send the man to different queues, and she said the second one in exactly the tone she had used for the weather.”", "is_correct": True},
                {"text": "“She had interpreted at the post for three winters and could tell from a passport photograph which language a traveller would answer in.”", "is_correct": False},
                {"text": "“The officer asked her twice whether she was certain of the translation, and she said that she was.”", "is_correct": False},
                {"text": "“At the end of a shift her jaw ached from holding her face still.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>SHART ikkita:</strong> <em>is aware that … changes the "
                "outcome</em> (biladi) va <em><u>never</u> lets that awareness show "
                "in her voice</em> (bildirmaydi). Ikki bo'lak, va ikkinchisi aynan "
                "<u>ovoz</u> haqida.</p>"
                + why([
                    (True, "“She knew that ‘he refused’ and ‘he declined’ would send the man to different queues, and she said the second one in exactly the tone she had used for the weather.”",
                     "birinchi bo'lak: ikki so'z ikki xil natija berishini biladi. "
                     "Ikkinchi bo'lak: <em>in exactly the tone she had used for the "
                     "weather</em> — ovozda hech nima sezilmaydi. Aniq juftlik."),
                    (False, "“At the end of a shift her jaw ached from holding her face still.”",
                     "<strong>eng nozik tuzoq</strong>: yashirish bor, va u juda "
                     "ta'sirli. Lekin bu <u>yuz</u> haqida, <u>ovoz</u> haqida "
                     "emas — va birinchi bo'lak (nima bilishini) umuman yo'q. "
                     "Da'vodagi aniq so'zga (<em>voice</em>) sodiq qoling."),
                    (False, "“She had interpreted at the post for three winters and could tell from a passport photograph which language a traveller would answer in.”",
                     "mahorat va tajriba — lekin so'z tanlashning "
                     "<u>oqibati</u> haqida hech nima."),
                    (False, "“The officer asked her twice whether she was certain of the translation, and she said that she was.”",
                     "boshqa odamning shubhasi haqida. Nilufarning bilishi ham, "
                     "ovozini boshqarishi ham ko'rinmaydi."),
                ])
                + TIP.format(
                    "Oxirgi savolda ikki variant «yashirish» haqida edi, lekin "
                    "da'vo <em>in her voice</em> deb aniq aytgan. "
                    "<strong>Da'voning aniq so'zlaridan chetga chiqmang</strong> — "
                    "«yuz» va «ovoz» bir xil emas, va SAT aynan shu farqni "
                    "sinaydi.")
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a woman running a family printing shop, "
                "a student has written the following claim:</p>"
                "<p><em>Kamola keeps up the appearance of the business despite knowing "
                "it will not last the year.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "\u201cShe ordered the new letterhead in September, and she knew as she signed for it that there would be no January.\u201d", "is_correct": True},
                {"text": "\u201cThe shop had been on that street since her grandfather bought the first press.\u201d", "is_correct": False},
                {"text": "\u201cShe told her brother frankly that the accounts would not carry them past December.\u201d", "is_correct": False},
                {"text": "\u201cTakings in the last quarter were lower than in any quarter she could remember.\u201d", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>SHART:</strong> <em>despite</em> \u2014 51-darsning "
                "jadvaliga ko\u2018ra bu <mark>ikki qarama-qarshi narsa "
                "yonma-yon</mark> degani: tashqi ko\u2018rinishni saqlaydi "
                "<u>va</u> tugashini biladi.</p>"
                + why([
                    (True, "\u201cShe ordered the new letterhead in September, and she knew as she signed for it that there would be no January.\u201d",
                     "ikkala bo\u2018lak bitta jumlada, hatto bitta lahzada: yangi "
                     "blank buyurtma qilish (ko\u2018rinish) va imzolayotib "
                     "yanvar bo\u2018lmasligini bilish. <em>as she signed</em> "
                     "ikkovini bir vaqtga bog\u2018laydi."),
                    (False, "\u201cShe told her brother frankly that the accounts would not carry them past December.\u201d",
                     "faqat <u>bilish</u> bo\u2018lagi, va u ochiq aytilgan \u2014 "
                     "ya\u2019ni ko\u2018rinishni saqlash bo\u2018lagiga zid ishlaydi."),
                    (False, "\u201cTakings in the last quarter were lower than in any quarter she could remember.\u201d",
                     "biznesning yomon ahvoli haqida fakt, lekin Kamolaning "
                     "<u>bilishi</u> ham, <u>ko\u2018rinishni saqlashi</u> ham yo\u2018q. "
                     "<strong>Hech qaysi bo\u2018lak.</strong>"),
                    (False, "\u201cThe shop had been on that street since her grandfather bought the first press.\u201d",
                     "fon ma\u2019lumoti. <em>despite</em> ning ikki tomonidan "
                     "birortasi ham yo\u2018q."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to come to see ~ differently</div><div class="pp-card-back">~ ga boshqacha qaray boshlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">without ever ~ing</div><div class="pp-card-back">hech qachon ~ qilmasdan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to apply a standard</div><div class="pp-card-back">me\'yor qo\'llamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to sign off (work)</div><div class="pp-card-back">(ishni) qabul qilib tasdiqlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to work something out</div><div class="pp-card-back">o\'zi tushunib, aniqlab olmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to let something show</div><div class="pp-card-back">bildirib qo\'ymoq, sezdirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the outcome</div><div class="pp-card-back">natija, oqibat</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to take something apart</div><div class="pp-card-back">qismlarga ajratmoq, ochmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Da'voni uch qismga ajrating: <strong>EGA · FE'L · SHART</strong>.</li>"
              "<li><strong>Nechta shart so'zi — shuncha bo'lak</strong> to'g'ri "
              "iqtibosda.</li>"
              "<li><em>rather than · without · never</em> — ikki bo'lak talab "
              "qiladi.</li>"
              "<li>Fe'l o'zgarishni bildirsa (<em>comes to</em>), "
              "<u>o'zgarmaslik</u> ko'rsatgan iqtibos — tuzoq.</li>"
              "<li>Da'voning <strong>aniq so'zidan</strong> chetga chiqmang: "
              "<em>voice</em> ≠ <em>face</em>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 52
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_T,
    "title": "SAT R&W 52: “Which Finding, If True, Would Support or Weaken the Hypothesis?”",
    "summary": "Ikkinchi shakl: tadqiqot tasvirlanadi va to'rtta farazi topilma "
               "beriladi. Gipotezaning mexanizmini toping — javob o'sha yerda.",
    "order": 52,
    "blocks": [
        {"rich_text": (
            "<h2>Ikkinchi shakl — farazi topilmalar</h2>"
            "<p>Command of Evidence ning ikkinchi shakli ilmiy matnlarda keladi va "
            "birinchisidan butunlay boshqacha ishlaydi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>Which finding, if true, would most directly "
                "<u>support</u> the researchers' hypothesis?</em><br>"
                "<em>Which finding, if true, would most directly "
                "<u>weaken</u> the team's conclusion?</em></p>")
            + "<p>Bu yerda variantlar matndan olingan iqtiboslar emas — ular "
            "<mark>hali topilmagan, farazi natijalar</mark>. "
            "<em>If true</em> iborasi shuni anglatadi: «faraz qiling, bu rost "
            "chiqdi — u holda nima bo'ladi?»</p>"
            "<p>Ya'ni sizdan <u>matnni eslash</u> emas, <u>mantiqiy o'ylash</u> "
            "so'ralyapti. Bu Reading bo'limidagi eng «matematik» savol turi.</p>"
            + '<span class="sr-time">⏱ ~75 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Gipotezaning mexanizmini toping</h3>"
            "<p>Har gipoteza <strong>X → Y</strong> shaklida bo'ladi: biror sabab "
            "biror natijani keltirib chiqaradi. Javobni topish uchun o'sha strelkani "
            "aniq nomlash kerak.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><strong>Gipoteza:</strong> "
                "«Qushlar shaharda balandroq sayraydi, chunki past ovoz "
                "transport shovqiniga yutiladi.»</p>"
                "<p style=\"margin:0;\"><strong>Mexanizm:</strong> "
                "shovqin (X) → balandroq sayrash (Y). "
                "Strelkaning <u>sababi</u> — eshitilish.</p>")
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Kuchaytirish (support):</strong> "
              "A ko'p bo'lgan joyda B ham ko'p; yoki A ni yo'q qilsangiz B ham "
              "yo'qoladi; yoki mexanizmning oraliq bo'g'ini topiladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Kuchsizlantirish (weaken):</strong> "
              "A bor, B yo'q; yoki A yo'q, B bor; yoki Y ni tushuntiradigan "
              "<u>boshqa</u> sabab topiladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Aloqasiz (irrelevant):</strong> "
              "topilma rost bo'lsa ham X va Y orasidagi strelkaga tegmaydi. "
              "Variantlarning yarmi shunday bo'ladi.</p></div>"
            + '</div>'
            + WARN.format(
                "<strong>Eng ko'p uchraydigan xato:</strong> «qiziqarli» yoki "
                "«ilmiy eshitiladigan» topilmani tanlash. Savol qiziqarlilikni "
                "so'ramaydi. Yagona savol: <u>bu topilma X → Y strelkasiga "
                "tegadimi?</u> Tegmasa — u qanchalik ta'sirli bo'lmasin, javob "
                "emas.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + q(
                "<p>Leafcutter ants carry cut leaves to their nest but do not eat them. "
                "The leaves are chewed to a paste and used to grow a fungus, and the "
                "fungus is what the colony feeds on. Researchers noticed that colonies "
                "reject certain leaves after a few days of collecting them, and "
                "hypothesised that the ants detect the fungus growing badly on that "
                "species and change their cutting in response.</p>",
                "Which finding, if true, would most directly support the researchers' "
                "hypothesis?")
            + choices_html([
                "Colonies that were prevented from cutting any leaves for a week showed "
                "reduced fungus growth.",
                "When a harmless substance that slows the fungus was added to one "
                "species of leaf, colonies stopped cutting that species within days.",
                "Leafcutter ants are found in a wide range of forest types across "
                "Central and South America.",
                "The ants' jaws are strong enough to cut leaves many times their own "
                "body weight.",
            ])
            + '<span class="sr-time">⏱ ~75 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Mexanizmni nomlaymiz.</strong> Gipoteza: chumolilar "
            "<u>zamburug'ning yomon o'sayotganini sezadi</u> (X) → shu bargni "
            "kesishni to'xtatadi (Y).</p>"
            "<p>Strelkaning yuragi — <mark>sezish</mark>. Chumoli bargning o'zini "
            "emas, <u>zamburug'ning holatini</u> o'qiydi degan da'vo.</p>"
            "<p><strong>Kuchaytirish uchun nima kerak?</strong> Bargni "
            "o'zgartirmasdan, faqat zamburug'ning o'sishini buzsak va chumoli "
            "baribir o'sha bargdan voz kechsa — bu strelkani deyarli "
            "isbotlaydi.</p>"
            + why([
                (True, "When a harmless substance that slows the fungus was added to one species of leaf, colonies stopped cutting that species within days",
                 "aynan kerakli tajriba. Modda <em>harmless</em> — demak chumoliga "
                 "to'g'ridan-to'g'ri zarar yo'q; o'zgargan yagona narsa — "
                 "zamburug'ning o'sishi; va chumoli reaksiya bergan. Sezish "
                 "strelkasi tasdiqlandi."),
                (False, "Colonies that were prevented from cutting any leaves for a week showed reduced fungus growth",
                 "<strong>strelkaga tegmaydi.</strong> Bu barg yo'qligida "
                 "zamburug' yomon o'sishini ko'rsatadi — matn allaqachon aytgan "
                 "narsa (barg zamburug' uchun). Gipoteza esa chumolining "
                 "<u>sezishi</u> haqida, va bu topilma sezish haqida hech nima "
                 "demaydi."),
                (False, "Leafcutter ants are found in a wide range of forest types across Central and South America",
                 "<strong>aloqasiz.</strong> Tarqalish geografiyasi rost bo'lishi "
                 "mumkin, lekin u X ham, Y ham emas. Bu «ilmiy eshitiladigan» "
                 "tuzoq."),
                (False, "The ants' jaws are strong enough to cut leaves many times their own body weight",
                 "yana <strong>aloqasiz</strong>, va yana ta'sirli eshitiladi. "
                 "Jag' kuchi kesish <u>qobiliyati</u> haqida; gipoteza esa kesish "
                 "<u>tanlovi</u> haqida."),
            ])
            + TIP.format(
                "Diqqat qiling: to'g'ri javobdagi <em>harmless</em> so'zi bekorga "
                "turmagan. U <u>muqobil tushuntirishni o'ldiradi</u> — «balki "
                "modda chumoliga yoqmagandir». Kuchaytiruvchi topilmalar ko'pincha "
                "shunday bitta ehtiyot so'zi bilan keladi: "
                "<em>harmless · otherwise identical · with all else unchanged</em>. "
                "Ularni qidiring.")
        )},

        {
            "rich_text": q(
                "<p>Sea otters were hunted almost to extinction along a stretch of "
                "coast, and the kelp forests there disappeared over the following "
                "decades. Otters eat sea urchins, and urchins graze on the base of kelp "
                "stalks. A team studying the coast proposed that the loss of the kelp "
                "followed from the loss of the otters, by way of an urchin population "
                "left unchecked.</p>",
                "Which finding, if true, would most directly support the team's "
                "proposal?"),
            "choices": [
                {"text": "Urchin numbers on that coast rose sharply in the decades after the otters were hunted out and fell again where otters were later reintroduced.", "is_correct": True},
                {"text": "Kelp grows more slowly in water that is warmer than its usual range.", "is_correct": False},
                {"text": "Sea otters have unusually dense fur, which is why they were hunted.", "is_correct": False},
                {"text": "Kelp forests provide shelter for many species of juvenile fish.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Mexanizm:</strong> otterlar yo'q (X) → dengiz "
                "kirpilari ko'payadi (<u>oraliq bo'g'in</u>) → kelp yo'qoladi (Y).</p>"
                "<p>Bu gipotezada uchta emas, <mark>ikki strelka</mark> bor, va "
                "ularning o'rtasida kirpi turadi. Eng kuchli dalil — aynan o'sha "
                "oraliq bo'g'inni ko'rsatish.</p>"
                + why([
                    (True, "Urchin numbers on that coast rose sharply in the decades after the otters were hunted out and fell again where otters were later reintroduced",
                     "oraliq bo'g'inni <u>ikki yo'nalishda</u> ham tasdiqlaydi: "
                     "otter yo'qolganda kirpi ko'paygan, otter qaytganda kirpi "
                     "kamaygan. Ikki tomonlama dalil har doim eng kuchlisi."),
                    (False, "Kelp grows more slowly in water that is warmer than its usual range",
                     "<strong>muqobil tushuntirish</strong> — ya'ni bu gipotezani "
                     "<u>kuchaytirmaydi</u>, aksincha kuchsizlantiradi. Savolni "
                     "shoshib o'qigan o'quvchi «kelp haqida, demak mos» deb "
                     "tanlaydi."),
                    (False, "Sea otters have unusually dense fur, which is why they were hunted",
                     "<strong>aloqasiz</strong>: ovning sababi haqida, zanjirning "
                     "o'zi haqida emas."),
                    (False, "Kelp forests provide shelter for many species of juvenile fish",
                     "<strong>aloqasiz</strong> va boshqa yo'nalishga qaragan: "
                     "kelpning <u>oqibatlari</u> haqida, uning yo'qolish "
                     "<u>sababi</u> haqida emas."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Patients recovering in rooms with a window facing trees were "
                "discharged on average a day earlier than patients in rooms facing a "
                "brick wall. The hospital's report attributed the difference to the view "
                "itself, suggesting that looking at greenery lowers stress and so speeds "
                "recovery.</p>",
                "Which finding, if true, would most directly weaken the report's "
                "explanation?"),
            "choices": [
                {"text": "The rooms facing trees are on the quieter side of the building, away from the ambulance entrance.", "is_correct": True},
                {"text": "Patients in the rooms facing trees reported feeling calmer than those facing the wall.", "is_correct": False},
                {"text": "The trees outside the windows are of a species that keeps its leaves all year.", "is_correct": False},
                {"text": "Hospitals in other cities have since planted trees outside patient wings.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Mexanizm:</strong> yashillik manzarasi (X) → stress "
                "kamayadi → tezroq tuzalish (Y).</p>"
                "<p><strong>Kuchsizlantirish uchun</strong> eng ishonchli yo'l — "
                "<mark>Y ni tushuntiradigan boshqa sabab topish</mark>. Agar "
                "daraxtga qaragan xonalar bir vaqtning o'zida "
                "<u>tinchroq</u> ham bo'lsa, tezroq tuzalishning sababi manzara "
                "emas, shovqinning yo'qligi bo'lishi mumkin.</p>"
                + why([
                    (True, "The rooms facing trees are on the quieter side of the building, away from the ambulance entrance",
                     "klassik <strong>uchinchi o'zgaruvchi</strong>: ikki guruh "
                     "manzara bilan emas, shovqin bilan ham farq qiladi. Endi "
                     "farqni nima keltirib chiqargani noma'lum."),
                    (False, "Patients in the rooms facing trees reported feeling calmer than those facing the wall",
                     "<strong>teskari</strong>: bu hisobotni <u>kuchaytiradi</u>, "
                     "chunki stressning kamayishi — mexanizmning oraliq bo'g'ini. "
                     "Savol <em>weaken</em> deb so'ragan; yo'nalishni shoshib "
                     "o'qish bu turdagi eng qimmat xato."),
                    (False, "The trees outside the windows are of a species that keeps its leaves all year",
                     "<strong>aloqasiz</strong>, va agar biror ta'siri bo'lsa ham "
                     "u gipotezaga foydali (yil bo'yi yashillik)."),
                    (False, "Hospitals in other cities have since planted trees outside patient wings",
                     "<strong>aloqasiz</strong>: boshqalarning ishonishi dalil "
                     "emas. Bu topilma tushuntirishning to'g'riligiga hech nima "
                     "qo'shmaydi."),
                ])
                + WARN.format(
                    "<strong>Yo'nalishni belgilang.</strong> <em>support</em> va "
                    "<em>weaken</em> savollari bir xil variantlar bilan keladi — "
                    "faqat qaysinisi to'g'ri bo'lishi o'zgaradi. Savoldagi "
                    "fe'lni barmoq bilan ko'rsating, xuddi Cross-Text dagi "
                    "yo'nalish kabi.")
            ),
        },

        {
            "rich_text": q(
                "<p>A team excavating a hill fort found no cooking hearths inside the "
                "walls, though there are hearths in the settlement below. They proposed "
                "that the fort was not lived in but used only as a refuge during "
                "attacks, occupied for days at a time and then abandoned again.</p>",
                "Which finding, if true, would most directly weaken the team's "
                "proposal?"),
            "choices": [
                {"text": "The fort's interior contains storage pits holding grain in quantities that would take a household a year to consume.", "is_correct": True},
                {"text": "The fort's walls were rebuilt at least twice during the period the settlement was occupied.", "is_correct": False},
                {"text": "Similar hill forts elsewhere in the region also lack cooking hearths.", "is_correct": False},
                {"text": "The settlement below the fort was larger than most others in the valley.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> qal'a — yashash joyi emas, faqat "
                "<u>bir necha kunlik boshpana</u>. Dalil: o'choq yo'q.</p>"
                "<p><strong>Kuchsizlantirish uchun</strong> uzoq yashashning boshqa "
                "izini topish kerak — o'choqsiz ham bo'ladigan iz. Bir yillik "
                "g'alla zaxirasi aynan shunday: <mark>bir necha kun uchun bir yillik "
                "g'alla saqlanmaydi</mark>.</p>"
                + why([
                    (True, "The fort's interior contains storage pits holding grain in quantities that would take a household a year to consume",
                     "gipotezaning <u>vaqt shkalasi</u>ga to'g'ridan-to'g'ri "
                     "ziddir: «bir necha kun» bilan «bir yillik zaxira» bir joyga "
                     "sig'maydi."),
                    (False, "Similar hill forts elsewhere in the region also lack cooking hearths",
                     "<strong>eng jozibali tuzoq</strong>: u gipotezani "
                     "<u>kuchaytiradi</u>, kuchsizlantirmaydi — o'choqsizlik "
                     "naqshga aylanadi. Yo'nalish xatosi."),
                    (False, "The fort's walls were rebuilt at least twice during the period the settlement was occupied",
                     "<strong>aloqasiz</strong>: ta'mirlash uzoq yashashni ham, "
                     "vaqtinchalik boshpanani ham bir xilda qo'llab-quvvatlaydi. "
                     "Ikkala tomonni ham qo'llab-quvvatlaydigan dalil — dalil "
                     "emas."),
                    (False, "The settlement below the fort was larger than most others in the valley",
                     "<strong>aloqasiz</strong>: quyi qishloqning kattaligi "
                     "qal'aning nima uchun ishlatilganini aytmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Bread made with a long, slow rise is tolerated by some people who "
                "report discomfort after eating ordinary bread. A baker proposed that the "
                "long rise gives the bacteria in the dough time to break down the "
                "particular carbohydrates that cause the discomfort, so that less of them "
                "remains in the finished loaf.</p>",
                "Which finding, if true, would most directly support the baker's "
                "proposal?"),
            "choices": [
                {"text": "Loaves given a long rise contain measurably lower quantities of those carbohydrates than loaves given a short one.", "is_correct": True},
                {"text": "People who report discomfort after ordinary bread also report it after some other wheat products.", "is_correct": False},
                {"text": "Bread given a long rise is generally judged to have a better flavour.", "is_correct": False},
                {"text": "The bacteria involved are present in flour before any water is added.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Mexanizm:</strong> uzoq achish (X) → bakteriyalar "
                "uglevodni parchalaydi → nonda kamroq uglevod qoladi → noqulaylik "
                "kam (Y).</p>"
                "<p>Bu zanjirda tekshirish oson bo'lgan bitta bo'g'in bor: "
                "<mark>tayyor nondagi uglevod miqdori</mark>. Uni o'lchash "
                "gipotezaning yuragini bevosita sinaydi.</p>"
                + why([
                    (True, "Loaves given a long rise contain measurably lower quantities of those carbohydrates than loaves given a short one",
                     "gipoteza aynan shuni bashorat qiladi (<em>less of them "
                     "remains in the finished loaf</em>), va bu topilma uni "
                     "bevosita o'lchaydi."),
                    (False, "People who report discomfort after ordinary bread also report it after some other wheat products",
                     "<strong>aloqasiz</strong>: bu noqulaylikning bug'doyga "
                     "bog'liqligini ko'rsatadi, lekin uzoq achish uni kamaytiradimi "
                     "degan savolga hech nima qo'shmaydi."),
                    (False, "Bread given a long rise is generally judged to have a better flavour",
                     "<strong>aloqasiz</strong> va chalg'ituvchi darajada yoqimli: "
                     "ta'm gipotezaning zanjirida umuman yo'q."),
                    (False, "The bacteria involved are present in flour before any water is added",
                     "bakteriyalarning <u>kelib chiqishi</u> haqida — qiziq, "
                     "lekin ular uglevodni parchalaydimi degan savolga javob "
                     "bermaydi. <strong>Mavzuga mos, mexanizmga mos emas.</strong>"),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a hypothesis</div><div class="pp-card-back">gipoteza, faraz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a finding</div><div class="pp-card-back">topilma, tadqiqot natijasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to support / to weaken</div><div class="pp-card-back">kuchaytirmoq / kuchsizlantirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">if true</div><div class="pp-card-back">agar rost bo\'lsa (faraziy topilma signali)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unchecked</div><div class="pp-card-back">to\'sqinliksiz, nazoratsiz (ko\'payish)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to attribute X to Y</div><div class="pp-card-back">X ni Y ga bog\'lamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">otherwise identical</div><div class="pp-card-back">qolgan hamma jihatdan bir xil</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a refuge</div><div class="pp-card-back">boshpana, panoh joy</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Gipotezani <strong>X → Y</strong> shaklida nomlang; javob "
              "strelkaga tegishi shart.</li>"
              "<li><u>Kuchaytirish:</u> X bor → Y bor; A ni yo'qotsang B "
              "yo'qoladi; oraliq bo'g'in topiladi.</li>"
              "<li><u>Kuchsizlantirish:</u> A bor, B yo'q; yoki B ni "
              "tushuntiradigan <strong>boshqa sabab</strong>.</li>"
              "<li>Variantlarning yarmi <strong>aloqasiz</strong> bo'ladi — "
              "«ilmiy eshitilishi» dalil emas.</li>"
              "<li>Savoldagi <em>support</em> / <em>weaken</em> ni "
              "<u>belgilang</u>: bir xil variantlar, boshqa javob.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 53
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_T,
    "title": "SAT R&W 53: Support vs Weaken vs Irrelevant — the Three-Way Sort",
    "summary": "To'rt variantni tanlashdan oldin uch qutiga ajrating: kuchaytiradi, "
               "kuchsizlantiradi, tegmaydi. Ko'pchiligi uchinchi qutiga tushadi.",
    "order": 53,
    "blocks": [
        {"rich_text": (
            "<h2>Tanlashdan oldin — saralang</h2>"
            "<p>52-darsda gipotezani <strong>X → Y</strong> shaklida nomlashni "
            "o'rgandik. Endi variantlar bilan ishlashning eng tez usulini "
            "qo'shamiz.</p>"
            "<p>Ko'p o'quvchi to'rt variantni o'qib, «qaysinisi eng yaxshi?» deb "
            "solishtiradi. Bu sekin va xato. Tezroq yo'l: har variantni "
            "<mark>uch qutidan biriga</mark> tashlang, ketma-ket, "
            "solishtirmasdan.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Quti</th><th>Sinov savoli</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>KUCHAYTIRADI</strong></td>"
              "<td>Bu rost bo'lsa, gipotezaga ishonchim <u>ortadimi</u>?</td></tr>"
              "<tr><td><strong>KUCHSIZLANTIRADI</strong></td>"
              "<td>Bu rost bo'lsa, ishonchim <u>kamayadimi</u>?</td></tr>"
              "<tr><td><strong>TEGMAYDI</strong></td>"
              "<td>Rost bo'lsa ham, X → Y strelkasi <u>o'zgarmaydimi</u>?</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Amalda variantlarning <strong>ikki yoki uchtasi</strong> uchinchi "
                "qutiga tushadi. Ya'ni bu savol turi ko'rinishidan qiyin, "
                "aslida esa ko'pincha <u>bitta</u> haqiqiy raqobatchi bo'ladi — "
                "faqat siz uni topa olishingiz kerak.")
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>«Tegmaydi» qutisining uch ko'rinishi</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Fon fakti.</strong> Mavzu "
              "haqida rost gap, lekin gipotezaning strelkasiga aloqasi yo'q "
              "(«chumolilar Janubiy Amerikada uchraydi»).</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Matnning takrori.</strong> "
              "Matn allaqachon aytgan narsa. Yangi ma'lumot bo'lmasa, u "
              "gipotezaga hech nima qo'shmaydi — «if true» degani "
              "<u>yangi</u> topilma degani.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ikki tomonga ham "
              "yaraydigan.</strong> Gipoteza to'g'ri bo'lsa ham, noto'g'ri bo'lsa "
              "ham kutiladigan narsa. Bu eng nozigi: u dalilga o'xshaydi, lekin "
              "hech nimani ajratmaydi.</p></div>"
            + '</div>'
            + WARN.format(
                "Uchinchi ko'rinish uchun oddiy sinov bor: <strong>«gipoteza "
                "noto'g'ri bo'lganda ham shu topilma bo'lishi mumkinmi?»</strong> "
                "Javob «ha» bo'lsa — u dalil emas. Qal'a devorlari ikki marta "
                "ta'mirlangani doimiy yashash uchun ham, vaqtinchalik boshpana "
                "uchun ham bir xilda kutiladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna — to'rttasini ham saralaymiz</h3>"
            + q(
                "<p>Nurses on a ward were asked to wash their hands at a sink placed "
                "beside the door, and compliance was measured at under half of "
                "opportunities. After a second sink was installed in the middle of the "
                "ward, compliance rose to nearly four fifths. The ward manager concluded "
                "that the original failure was a matter of distance rather than of "
                "attitude: staff had not been unwilling, only far away.</p>",
                "Which finding, if true, would most directly support the manager's "
                "conclusion?")
            + choices_html([
                "Handwashing compliance on the ward is now higher than the hospital "
                "average.",
                "On the three wards where a second sink was later added, compliance rose "
                "by a similar amount, and on the two where staff attended a hygiene talk "
                "instead, it did not.",
                "Nurses on the ward reported that they understood the importance of "
                "handwashing.",
                "The new sink was installed during a week when the ward was unusually "
                "quiet.",
            ])
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim — saralash</h3>"
            "<p><strong>Gipoteza:</strong> masofa (X) → qo'l yuvmaslik (Y). "
            "Munosabat emas, <u>masofa</u>.</p>"
            "<p>Endi har variantni qutiga tashlaymiz — solishtirmasdan:</p>"
            + why([
                (True, "On the three wards where a second sink was later added, compliance rose by a similar amount, and on the two where staff attended a hygiene talk instead, it did not",
                 "<strong>KUCHAYTIRADI.</strong> Ikki tomonlama: rakovina "
                 "qo'shilgan joyda o'sish bor, <u>munosabatga</u> ta'sir "
                 "qiladigan chora (suhbat) qo'llangan joyda esa yo'q. Bu "
                 "gipotezaning «masofa, munosabat emas» degan aniq da'vosini "
                 "sinaydi."),
                (False, "Handwashing compliance on the ward is now higher than the hospital average",
                 "<strong>TEGMAYDI</strong> (fon fakti). Boshqa bo'limlar bilan "
                 "solishtiruv yangi ko'rsatkich beradi, lekin o'sishning "
                 "<u>sababi</u> haqida hech nima demaydi."),
                (False, "Nurses on the ward reported that they understood the importance of handwashing",
                 "<strong>TEGMAYDI</strong> (ikki tomonga ham yaraydigan). "
                 "Ahamiyatni tushunish — masofa nazariyasida ham, munosabat "
                 "nazariyasida ham kutiladi: munosabat muammosi bilim "
                 "yetishmasligi degani emas."),
                (False, "The new sink was installed during a week when the ward was unusually quiet",
                 "<strong>KUCHSIZLANTIRADI.</strong> Bu muqobil tushuntirish "
                 "beradi — balki o'sish tinch haftadan. Savol "
                 "<em>support</em> so'ragan, demak bu javob emas; lekin uni "
                 "«aloqasiz» deb tashlab yubormang — uni to'g'ri qutiga "
                 "solish muhim."),
            ])
            + TIP.format(
                "Saralash tugagach hisob shunday chiqdi: <u>1 kuchaytiradi · "
                "1 kuchsizlantiradi · 2 tegmaydi</u>. Savol "
                "<em>support</em> so'ragani uchun javob o'z-o'zidan qoldi — "
                "<strong>hech qanday solishtirish kerak bo'lmadi</strong>. "
                "Bu usulning butun foydasi shunda.")
        )},

        {
            "rich_text": q(
                "<p>Fireflies in a valley flash in unison for part of each summer night. "
                "A researcher proposed that the synchrony arises without any leader: each "
                "insect simply shifts its own rhythm slightly toward the flashes it sees "
                "nearby, and with enough insects doing this the whole valley falls into "
                "step.</p>",
                "Which finding, if true, would most directly support the researcher's "
                "proposal?"),
            "choices": [
                {"text": "Mechanical lights programmed to shift their timing toward neighbouring lights fall into synchrony without any central signal.", "is_correct": True},
                {"text": "Firefly synchrony has been recorded in several valleys on more than one continent.", "is_correct": False},
                {"text": "Fireflies flash more brightly on warmer nights than on cooler ones.", "is_correct": False},
                {"text": "Individual fireflies removed from the valley continue to flash at a regular rhythm.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> rahbarsiz mahalliy moslashuv (X) → "
                "umumiy sinxronlik (Y). Da'voning yuragi — "
                "<mark>markaziy signalsiz</mark>.</p>"
                + why([
                    (True, "Mechanical lights programmed to shift their timing toward neighbouring lights fall into synchrony without any central signal",
                     "<strong>KUCHAYTIRADI.</strong> Mexanizmni "
                     "<u>chumolisiz</u> qayta tiklaydi: agar shunchaki qoida "
                     "sinxronlik bersa, hasharotda ham shu bo'lishi ehtimoli "
                     "ortadi. Modelni takrorlash — bu turdagi eng kuchli dalil."),
                    (False, "Firefly synchrony has been recorded in several valleys on more than one continent",
                     "<strong>TEGMAYDI</strong> (fon fakti): hodisaning keng "
                     "tarqalgani uning <u>mexanizmi</u> haqida hech nima "
                     "demaydi."),
                    (False, "Individual fireflies removed from the valley continue to flash at a regular rhythm",
                     "<strong>TEGMAYDI</strong> (ikki tomonga ham yaraydigan): "
                     "har bir hasharotning o'z ritmi bo'lishi ikkala nazariyada "
                     "ham kerak — hatto rahbar bo'lgan taqdirda ham."),
                    (False, "Fireflies flash more brightly on warmer nights than on cooler ones",
                     "<strong>TEGMAYDI</strong>: yorqinlik va harorat "
                     "sinxronlikning sababi haqida gapirmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Shops that play slow music report that customers stay longer and "
                "spend more. A consultant concluded that the tempo itself slows "
                "customers' movement through the shop, and recommended slow music to "
                "retailers generally.</p>",
                "Which finding, if true, would most directly weaken the consultant's "
                "conclusion?"),
            "choices": [
                {"text": "The shops that had chosen slow music were, on average, larger and stocked more expensive goods than those that had not.", "is_correct": True},
                {"text": "Customers in shops playing slow music walked measurably more slowly between displays.", "is_correct": False},
                {"text": "Slow music is more expensive to license than fast music in some markets.", "is_correct": False},
                {"text": "Some customers said they had not noticed what music was playing.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> sekin musiqa (X) → sekin harakat → "
                "ko'proq xarid (Y).</p>"
                "<p><strong>Kuchsizlantirish uchun</strong> eng ishonchli yo'l — "
                "<mark>uchinchi o'zgaruvchi</mark>. Agar sekin musiqa tanlagan "
                "do'konlar kattaroq va qimmatroq bo'lsa, ko'proq xarid "
                "musiqadan emas, do'konning o'zidan bo'lishi mumkin.</p>"
                + why([
                    (True, "The shops that had chosen slow music were, on average, larger and stocked more expensive goods than those that had not",
                     "<strong>KUCHSIZLANTIRADI.</strong> Ikki guruh musiqadan "
                     "boshqa jihatlar bilan ham farq qiladi — endi farqni nima "
                     "keltirib chiqargani noma'lum."),
                    (False, "Customers in shops playing slow music walked measurably more slowly between displays",
                     "<strong>KUCHAYTIRADI</strong> — bu mexanizmning oraliq "
                     "bo'g'ini. Savol <em>weaken</em> so'ragan; yo'nalishni "
                     "shoshib o'qish bu turdagi eng qimmat xato."),
                    (False, "Some customers said they had not noticed what music was playing",
                     "<strong>TEGMAYDI</strong> (ikki tomonga ham yaraydigan): "
                     "gipoteza ongli e'tiborni talab qilmaydi — sekin musiqa "
                     "sezilmasdan ham ta'sir qilishi mumkin."),
                    (False, "Slow music is more expensive to license than fast music in some markets",
                     "<strong>TEGMAYDI</strong> (fon fakti): xarajat tavsiyaning "
                     "amaliyligiga tegishli, uning <u>to'g'riligiga</u> emas."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A museum found that visitors spent longer at objects displayed alone "
                "in a case than at objects displayed in groups of six or more. The "
                "curator concluded that isolation signals importance, and that visitors "
                "read the display as an instruction about where to look.</p>",
                "Which finding, if true, would most directly weaken the curator's "
                "conclusion?"),
            "choices": [
                {"text": "The objects displayed alone were also the largest in the collection and the only ones visible from the doorway.", "is_correct": True},
                {"text": "Visitors given a printed guide spent longer at every object than visitors without one.", "is_correct": False},
                {"text": "Museums in other cities also display their most valuable objects alone.", "is_correct": False},
                {"text": "The grouped objects were of the same period as the isolated ones.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> yolg'iz qo'yish (X) → «bu muhim» "
                "signali → uzoqroq qarash (Y).</p>"
                + why([
                    (True, "The objects displayed alone were also the largest in the collection and the only ones visible from the doorway",
                     "<strong>KUCHSIZLANTIRADI</strong> — va ikki barobar: "
                     "kattalik ham, ko'rinib turish ham uzoq qarashni "
                     "tushuntira oladi. Yolg'izlik endi yagona farq emas."),
                    (False, "Visitors given a printed guide spent longer at every object than visitors without one",
                     "<strong>TEGMAYDI</strong>: qo'llanma <u>hamma</u> "
                     "buyumga ta'sir qiladi, demak yolg'iz va guruhdagilar "
                     "orasidagi <u>farqni</u> o'zgartirmaydi."),
                    (False, "The grouped objects were of the same period as the isolated ones",
                     "<strong>TEGMAYDI</strong> — aksincha, bu bitta muqobil "
                     "tushuntirishni yopadi, ya'ni gipotezaga biroz foydali. "
                     "Har holda u kuchsizlantirmaydi."),
                    (False, "Museums in other cities also display their most valuable objects alone",
                     "<strong>TEGMAYDI</strong> (fon fakti): boshqalarning "
                     "amaliyoti tashrifchining nega uzoq qaraganini "
                     "tushuntirmaydi."),
                ])
                + TIP.format(
                    "Uch darsdagi naqshni payqadingizmi? <strong>Kuchsizlantirish "
                    "javoblarining deyarli hammasi bitta shaklda edi: "
                    "«ikki guruh yana bir jihat bilan ham farq qilardi».</strong> "
                    "Bu SAT ning eng sevimli kuchsizlantirish harakati — "
                    "uni birinchi bo'lib qidiring.")
            ),
        },

        {
            "rich_text": q(
                "<p>Villages that installed a communal water pump saw childhood illness "
                "fall over the following two years. Two explanations were offered: that "
                "the pump water was cleaner than the river water it replaced, and that "
                "families no longer spent hours a day carrying water and could spend the "
                "time on other things. The engineers who ran the programme concluded that "
                "the water quality was doing the work.</p>",
                "Which finding, if true, would most directly support the engineers\u2019 "
                "conclusion?"),
            "choices": [
                {"text": "In villages where a pump was installed but its water was later found to be contaminated, childhood illness did not fall.", "is_correct": True},
                {"text": "Households in villages with a pump spent about two hours less each day collecting water.", "is_correct": False},
                {"text": "Each pump was maintained by a committee elected by the village it served.", "is_correct": False},
                {"text": "Childhood illness in the region is generally more common in the dry season than in the wet one.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu yerda <u>ikkita</u> raqib tushuntirish bor \u2014 suv sifati va "
                "tejalgan vaqt \u2014 va muhandislar birinchisini tanlagan. Demak "
                "kuchaytiruvchi topilma <mark>ikkovini bir-biridan "
                "ajratishi</mark> kerak.</p>"
                + why([
                    (True, "In villages where a pump was installed but its water was later found to be contaminated, childhood illness did not fall",
                     "<strong>KUCHAYTIRADI</strong>, va aynan kerakli tarzda: "
                     "nasos bor (demak vaqt baribir tejalgan), lekin suv iflos \u2014 "
                     "va kasallik kamaymagan. Ikkinchi tushuntirish "
                     "chetlashtirildi."),
                    (False, "Households in villages with a pump spent about two hours less each day collecting water",
                     "<strong>KUCHSIZLANTIRADI</strong>: bu <u>raqib</u> "
                     "tushuntirishni oziqlantiradi. Savol <em>support</em> "
                     "so\u2018ragan \u2014 yo\u2018nalishni belgilang."),
                    (False, "Each pump was maintained by a committee elected by the village it served",
                     "<strong>TEGMAYDI</strong> (fon fakti): boshqaruv tuzilmasi "
                     "kasallikning kamayish sababini ajratmaydi."),
                    (False, "Childhood illness in the region is generally more common in the dry season than in the wet one",
                     "<strong>TEGMAYDI</strong> (ikki tomonga ham yaraydigan): "
                     "mavsumiylik ikkala tushuntirishda ham bir xil ishlaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">compliance</div><div class="pp-card-back">qoidaga rioya qilish darajasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fall into step / into synchrony</div><div class="pp-card-back">bir maromga tushmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a confounding factor</div><div class="pp-card-back">chalkashtiruvchi omil (uchinchi o\'zgaruvchi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">irrelevant</div><div class="pp-card-back">aloqasiz, mavzuga daxlsiz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to arise without ~</div><div class="pp-card-back">~ siz paydo bo\'lmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on average</div><div class="pp-card-back">o\'rtacha hisobda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">tempo</div><div class="pp-card-back">sur\'at, temp (musiqada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to signal importance</div><div class="pp-card-back">muhimlikni bildirmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Solishtirmang — <strong>saralang</strong>: kuchaytiradi · "
              "kuchsizlantiradi · tegmaydi.</li>"
              "<li>Odatda ikki-uchtasi <u>tegmaydi</u> qutisiga tushadi.</li>"
              "<li>«Tegmaydi» ning uch ko'rinishi: fon fakti · matnning takrori · "
              "<strong>ikki tomonga ham yaraydigan</strong>.</li>"
              "<li>Sinov: «gipoteza noto'g'ri bo'lganda ham bu topilma bo'lardimi?» "
              "Ha bo'lsa — dalil emas.</li>"
              "<li>Kuchsizlantirishning eng ko'p shakli: <strong>ikki guruh yana "
              "bir jihat bilan ham farq qilardi</strong>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 54
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_T,
    "title": "SAT R&W 54: Command of Evidence (Textual) — Mixed Practice",
    "summary": "Ikkala shakl aralash — qaysi iqtibos da'voni isbotlaydi va qaysi "
               "topilma gipotezani kuchaytiradi/kuchsizlantiradi — imtihon tezligida.",
    "order": 54,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol: uchtasi <strong>iqtibos</strong> shaklida, uchtasi "
            "<strong>farazi topilma</strong> shaklida, aralash tartibda — "
            "imtihondagi kabi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>7 daqiqa</strong> (6 × 70 soniya).</li>"
                "<li>Iqtibos savolida — da'voni <u>EGA · FE'L · SHART</u> ga "
                "ajrating (51-dars).</li>"
                "<li>Topilma savolida — gipotezani <u>X → Y</u> deb nomlang va "
                "uch qutiga <u>saralang</u> (52, 53-darslar).</li>"
                "<li>Savoldagi <em>support</em> / <em>weaken</em> ni "
                "belgilang.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 7 daqiqa</span>'
        )},

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a man who has retired from driving "
                "long-distance lorries, a student has written the following claim:</p>"
                "<p><em>Botir organises his days around a schedule he no longer has any "
                "reason to keep.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“He still ate at half past four and was in bed by nine, though there was nothing now that had to be anywhere by morning.”", "is_correct": True},
                {"text": "“He had driven the northern route for nineteen years and could name every town on it in order.”", "is_correct": False},
                {"text": "“His wife said the house was easier to run now that he was in it.”", "is_correct": False},
                {"text": "“He sold the lorry in the spring to a young man from the next district.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> EGA — Botir; FE'L — <em>organises his "
                "days</em>; SHART — <em>no longer has any reason to keep</em>. "
                "Ikki bo'lak: <mark>tartib saqlanadi</mark> va "
                "<mark>sababi yo'q</mark>.</p>"
                + why([
                    (True, "“He still ate at half past four and was in bed by nine, though there was nothing now that had to be anywhere by morning.”",
                     "<em>still</em> (tartib saqlanmoqda) va <em>though there was "
                     "nothing now</em> (sabab yo'q) — ikki bo'lak bitta jumlada."),
                    (False, "“He had driven the northern route for nineteen years and could name every town on it in order.”",
                     "o'tmish va xotira haqida. Bugungi tartib ham, uning "
                     "sababsizligi ham yo'q."),
                    (False, "“He sold the lorry in the spring to a young man from the next district.”",
                     "faqat ikkinchi bo'lakning foni (endi ish yo'q), lekin "
                     "tartib haqida hech nima. <strong>Yarim bo'lak "
                     "ham emas.</strong>"),
                    (False, "“His wife said the house was easier to run now that he was in it.”",
                     "boshqa odamning bahosi. Botirning kun tartibi "
                     "ko'rinmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Crows in a city park were seen dropping walnuts onto a road and "
                "waiting for cars to crack them. A researcher proposed that the birds are "
                "not simply dropping nuts from a height but using the traffic "
                "deliberately, timing the drop so that a vehicle arrives.</p>",
                "Which finding, if true, would most directly support the researcher's "
                "proposal?"),
            "choices": [
                {"text": "The crows drop nuts onto the road far more often when a car is approaching than when the road is empty.", "is_correct": True},
                {"text": "Walnut shells are harder than the shells of the other nuts available in the park.", "is_correct": False},
                {"text": "Crows in the park also drop nuts onto paved paths where no vehicles travel.", "is_correct": False},
                {"text": "Crows are among the birds most often observed using objects as tools.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> balandlikdan tashlash emas, "
                "<u>mashinani ataylab ishlatish</u> (X) → yong'oq yorilishi (Y). "
                "Da'voning yuragi — <mark>vaqtni moslashtirish</mark>.</p>"
                + why([
                    (True, "The crows drop nuts onto the road far more often when a car is approaching than when the road is empty",
                     "<strong>KUCHAYTIRADI</strong> va aynan strelkaga tegadi: "
                     "tashlash mashinaning kelishiga bog'langan. Bu "
                     "«ataylab» degan so'zning o'lchanadigan ko'rinishi."),
                    (False, "Crows in the park also drop nuts onto paved paths where no vehicles travel",
                     "<strong>KUCHSIZLANTIRADI</strong>: bu shunchaki "
                     "balandlikdan tashlash gipotezasini oziqlantiradi. Savol "
                     "<em>support</em> so'ragan."),
                    (False, "Walnut shells are harder than the shells of the other nuts available in the park",
                     "<strong>TEGMAYDI</strong> (fon fakti): po'stning qattiqligi "
                     "nima uchun yo'lga tashlanishini tushuntiradi, lekin "
                     "vaqt moslashtirish haqida hech nima demaydi."),
                    (False, "Crows are among the birds most often observed using objects as tools",
                     "<strong>TEGMAYDI</strong>: umumiy qobiliyat haqida. "
                     "«Aqlli qush» ekani bu aniq xatti-harakatni isbotlamaydi."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a woman who has agreed to look after a "
                "neighbour's garden for a summer, a student has written the following "
                "claim:</p>"
                "<p><em>Gulnora becomes attached to the garden through the work it "
                "demands rather than through any interest in the plants.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“She still could not have named half of what grew there, but by August she was reluctant to leave for a week in case the watering was done badly.”", "is_correct": True},
                {"text": "“The garden had eleven kinds of rose, which her neighbour had listed for her on a card.”", "is_correct": False},
                {"text": "“She had agreed to it in April without much thought, as a favour.”", "is_correct": False},
                {"text": "“Her own balcony held two pots of basil that she remembered to water perhaps once a week.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>SHART:</strong> <em>rather than</em> — ikki bo'lak. "
                "Bog'lanish <u>mehnat orqali</u> paydo bo'lishi va o'simliklarga "
                "qiziqish <u>yo'qligi</u> ko'rinishi kerak.</p>"
                + why([
                    (True, "“She still could not have named half of what grew there, but by August she was reluctant to leave for a week in case the watering was done badly.”",
                     "<em>could not have named half of what grew there</em> "
                     "(qiziqish yo'q) va <em>reluctant to leave … in case the "
                     "watering was done badly</em> (mehnat orqali bog'lanish). "
                     "<em>but</em> ikkovini bog'laydi."),
                    (False, "“Her own balcony held two pots of basil that she remembered to water perhaps once a week.”",
                     "<strong>eng jozibali tuzoq</strong>: bu o'simliklarga "
                     "qiziqmasligini ko'rsatadi — ya'ni <u>bir bo'lak</u>. "
                     "Lekin bog'lanish umuman ko'rinmaydi."),
                    (False, "“The garden had eleven kinds of rose, which her neighbour had listed for her on a card.”",
                     "bog'ning tavsifi. Gulnoraning munosabati yo'q."),
                    (False, "“She had agreed to it in April without much thought, as a favour.”",
                     "boshlanish nuqtasi — bog'lanishdan <u>oldingi</u> holat. "
                     "Da'vo esa o'zgarish haqida."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>A school moved its start time an hour later and recorded a fall in "
                "absence over the following year. The head teacher attributed the change "
                "to sleep: teenagers, on this account, were arriving having rested "
                "enough, and rested pupils get ill less often.</p>",
                "Which finding, if true, would most directly weaken the head teacher's "
                "explanation?"),
            "choices": [
                {"text": "Pupils at the school went to bed on average an hour later after the change, sleeping no longer than before.", "is_correct": True},
                {"text": "Pupils reported feeling less tired in morning lessons after the change.", "is_correct": False},
                {"text": "Two other schools in the district made the same change in the same year.", "is_correct": False},
                {"text": "Absence at the school had been slightly above the district average before the change.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> kechroq boshlanish (X) → "
                "<u>ko'proq uyqu</u> → kam kasallik (Y). Zanjirning "
                "o'rtasidagi bo'g'in — uyquning <u>uzayishi</u>.</p>"
                "<p>Kuchsizlantirishning eng to'g'ridan-to'g'ri yo'li — "
                "<mark>o'sha oraliq bo'g'inni sindirish</mark>.</p>"
                + why([
                    (True, "Pupils at the school went to bed on average an hour later after the change, sleeping no longer than before",
                     "<strong>KUCHSIZLANTIRADI.</strong> Agar uyqu uzaymagan "
                     "bo'lsa, tushuntirishning butun mexanizmi qulaydi — "
                     "davomat baribir yaxshilangan bo'lsa ham, sababi uyqu "
                     "emas."),
                    (False, "Pupils reported feeling less tired in morning lessons after the change",
                     "<strong>KUCHAYTIRADI</strong> — charchoqning kamayishi "
                     "mexanizmga mos. Yo'nalish xatosi."),
                    (False, "Two other schools in the district made the same change in the same year",
                     "<strong>TEGMAYDI</strong> (fon fakti): boshqalarning "
                     "qilgani bu maktabdagi sababni ajratmaydi."),
                    (False, "Absence at the school had been slightly above the district average before the change",
                     "<strong>TEGMAYDI</strong>: boshlang'ich daraja "
                     "pasayishning <u>sababi</u> haqida hech nima demaydi."),
                ])
            ),
        },

        {
            "rich_text": (
                '<div class="sr-passage">'
                "<p>While studying a story about a young man who has taken over his "
                "father's beehives, a student has written the following claim:</p>"
                "<p><em>Jasur trusts what he can observe over what he has been "
                "told.</em></p>"
                "</div>"
                "<p><strong>Which quotation from the story most effectively illustrates "
                "the claim?</strong></p>"
            ),
            "choices": [
                {"text": "“His father had said never to open a hive before the tenth of April; Jasur opened one on the second, because the bees had been flying for a week.”", "is_correct": True},
                {"text": "“He had kept bees at his father's side every summer since he was seven.”", "is_correct": False},
                {"text": "“He read two books on the subject that winter and made notes in the margins.”", "is_correct": False},
                {"text": "“His father had thirty hives at the height of it and never lost a colony to cold.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>SHART:</strong> <em>over</em> — bu ham "
                "<mark>ikki bo'lak</mark> signali: kuzatish <u>va</u> "
                "aytilgan qoida, va ikkovi to'qnashishi kerak.</p>"
                + why([
                    (True, "“His father had said never to open a hive before the tenth of April; Jasur opened one on the second, because the bees had been flying for a week.”",
                     "to'qnashuv bitta jumlada: aytilgan qoida (10-apreldan "
                     "oldin emas) va kuzatuv (asalarilar bir haftadan beri "
                     "uchmoqda) — va Jasur kuzatuvni tanlaydi."),
                    (False, "“He read two books on the subject that winter and made notes in the margins.”",
                     "kitob — bu <u>aytilgan</u> bilim, kuzatuv emas. Va hech "
                     "qanday to'qnashuv yo'q. Bu da'voning teskarisiga "
                     "yaqinroq."),
                    (False, "“He had kept bees at his father's side every summer since he was seven.”",
                     "tajriba foni. Ikki manba orasidagi tanlov ko'rinmaydi."),
                    (False, "“His father had thirty hives at the height of it and never lost a colony to cold.”",
                     "otaning obro'si haqida — bu Jasurning tanlovini "
                     "<u>qiyinlashtiradi</u>, lekin tanlovni ko'rsatmaydi."),
                ])
            ),
        },

        {
            "rich_text": q(
                "<p>Bilingual children in one study named objects a fraction of a second "
                "more slowly than children who spoke a single language, and the "
                "researchers proposed that the delay comes from the work of suppressing "
                "the language not being used: both words arrive, and one must be held "
                "back.</p>",
                "Which finding, if true, would most directly support the researchers' "
                "proposal?"),
            "choices": [
                {"text": "The delay is longest for objects whose names in the child's two languages sound very similar to each other.", "is_correct": True},
                {"text": "Bilingual children in the study had smaller vocabularies in each single language than the other children did.", "is_correct": False},
                {"text": "Bilingual children were on average two months older than the children they were compared with.", "is_correct": False},
                {"text": "Children who speak three languages are more common in cities than in rural areas.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipoteza:</strong> ikkinchi tilni <u>bostirish "
                "ishi</u> (X) → sekinroq nomlash (Y). Yurak — "
                "<mark>raqobat</mark>: ikkala so'z ham kelib qoladi.</p>"
                + why([
                    (True, "The delay is longest for objects whose names in the child's two languages sound very similar to each other",
                     "<strong>KUCHAYTIRADI</strong>: raqobat kuchliroq bo'lgan "
                     "joyda kechikish ham kattaroq. Bu mexanizmning "
                     "o'lchanadigan bashorati — eng ishonchli dalil turi."),
                    (False, "Bilingual children in the study had smaller vocabularies in each single language than the other children did",
                     "<strong>KUCHSIZLANTIRADI</strong>: bu muqobil "
                     "tushuntirish beradi — balki so'z kamroq mashq "
                     "qilingandir, bostirish emas."),
                    (False, "Bilingual children were on average two months older than the children they were compared with",
                     "<strong>KUCHSIZLANTIRADI</strong> (uchinchi o'zgaruvchi), "
                     "lekin baribir <em>support</em> emas."),
                    (False, "Children who speak three languages are more common in cities than in rural areas",
                     "<strong>TEGMAYDI</strong>: demografiya mexanizmga "
                     "tegmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Mavzuga mos iqtibosni tanladim</td>"
              "<td>50-dars. Iqtibos da'voning <u>fikriga</u> mos kelsin.</td></tr>"
              "<tr><td>Yarim bo'lakli iqtibosni tanladim</td>"
              "<td>51-dars. <em>rather than · without · over · despite</em> = ikki "
              "bo'lak.</td></tr>"
              "<tr><td><em>support</em> o'rniga kuchsizlantiruvchini tanladim</td>"
              "<td>52-dars. Savol fe'lini belgilang.</td></tr>"
              "<tr><td>«Ilmiy eshitiladigan» aloqasiz topilmani tanladim</td>"
              "<td>53-dars. Uch qutiga saralang.</td></tr>"
              "<tr><td>Ikki tomonga ham yaraydigan topilmani dalil deb oldim</td>"
              "<td>53-dars. «Gipoteza noto'g'ri bo'lsa ham bu bo'lardimi?»</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu mavzuda eng foydali bitta odat: <strong>topilma savolida "
                "gipotezaning zanjirini ovoz chiqarmasdan aytib chiqing</strong> "
                "— «kechroq boshlanish → ko'proq uyqu → kam kasallik». Zanjirni "
                "aytgan odam qaysi bo'g'inga tegish kerakligini darrov "
                "ko'radi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to attribute a change to ~</div><div class="pp-card-back">o\'zgarishni ~ ga bog\'lamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">deliberately</div><div class="pp-card-back">ataylab, ongli ravishda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to suppress</div><div class="pp-card-back">bostirmoq, ushlab turmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">reluctant to ~</div><div class="pp-card-back">~ qilishni istamaydigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to hold back</div><div class="pp-card-back">ushlab qolmoq, chiqarmaslik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a fraction of a second</div><div class="pp-card-back">soniyaning bir ulushi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on this account</div><div class="pp-card-back">bu tushuntirishga ko\'ra</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">at the height of it</div><div class="pp-card-back">eng gullab-yashnagan payti</div></div>'
            + "</div>"
            + "<h3>Xulosa — Command of Evidence (Textual) mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Iqtibos <strong>mavzuga emas, da'voning fikriga</strong> mos "
              "kelsin (50-dars).</li>"
              "<li>Da'voni <strong>EGA · FE'L · SHART</strong> ga ajrating; nechta "
              "shart — shuncha bo'lak (51-dars).</li>"
              "<li>Gipotezani <strong>X → Y</strong> zanjiri deb ayting "
              "(52-dars).</li>"
              "<li>Variantlarni solishtirmang — <strong>uch qutiga saralang</strong> "
              "(53-dars).</li>"
              "<li>Kuchsizlantirishning eng ko'p shakli: <u>ikki guruh yana bir "
              "jihat bilan ham farq qilardi</u>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 60
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_Q,
    "title": "SAT R&W 60: Reading the Table or Graph Before You Read the Text",
    "summary": "Grafikli savolda tartib muhim: avval sarlavha, birlik va ustunlarni "
               "o'qing, keyin matnni — shunda tuzoqlarning yarmi o'z-o'zidan tushadi.",
    "order": 60,
    "blocks": [
        {"rich_text": (
            "<h2>Raqamlar bilan keladigan savol</h2>"
            "<p><strong>Command of Evidence</strong> ning ikkinchi yarmi — "
            "<u>grafik va jadvaldan dalil</u>. Ekranda jadval yoki diagramma "
            "bo'ladi, uning ostida qisqa matn, va savol:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>Which choice most effectively uses data "
                "from the table to complete the text?</em><br>"
                "<em>Which choice most effectively uses data from the graph to "
                "support the student's claim?</em></p>")
            + "<p>Yaxshi yangilik: <mark>bu matematika savoli emas</mark>. "
            "Hisob-kitob deyarli kerak emas — ko'pi bilan ikkita sonni ayirish "
            "yoki solishtirish. Qiyinligi boshqa joyda: <u>to'g'ri raqamni "
            "to'g'ri da'voga bog'lash</u>.</p>"
            + '<span class="sr-time">⏱ ~85 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Tartib: avval jadval, keyin matn</h3>"
            "<p>Ko'p o'quvchi matnni birinchi o'qiydi, keyin jadvalga qaraydi va "
            "unda adashadi. To'g'ri tartib teskari:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Sarlavhani o'qing.</strong> "
              "Nima o'lchangan? <em>Average daily screen time</em>? "
              "<em>Number of species</em>? Sarlavhasiz raqamlar ma'nosiz.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Birlikni toping.</strong> "
              "Daqiqami, foizmi, donami, gektarmi? "
              "<u>Foiz bilan sonni adashtirish</u> — bu turdagi eng katta "
              "tuzoq (61-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ustun va qatorlarni "
              "o'qing.</strong> Nima nima bilan solishtirilishi mumkin? "
              "Ikki yilmi? Ikki guruhmi? Jadval nimani "
              "<u>solishtira olmaydi</u> — buni ham bilib qo'ying.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Endi matnni o'qing</strong> va "
              "da'voni toping. Matn odatda qisqa: bir-ikki jumla "
              "kontekst, keyin da'vo yoki bo'sh joy.</p></div>"
            + "<div class=\"pp-step\"><p><strong>5. Bashorat qiling:</strong> "
              "«bu da'voni isbotlaydigan raqam qanday ko'rinardi?» "
              "Ko'pincha bu <u>ikkita son va ular orasidagi munosabat</u> "
              "bo'ladi.</p></div>"
            + '</div>'
            + TIP.format(
                "5-qadam bu turdagi eng foydali odat. Da'vo <u>solishtiruv</u> "
                "bo'lsa (kattaroq, tezroq, ko'proq), javobda ham "
                "<strong>ikkita son</strong> bo'lishi kerak. Bitta son "
                "keltirgan variant solishtiruvni isbotlay olmaydi — "
                "qanchalik to'g'ri bo'lmasin.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + data_q(
                "Average Daily Screen Time Reported by Pupils, by Year Group (minutes)",
                table(["Year group", "2019", "2023"],
                      [["Year 7", "118", "164"],
                       ["Year 9", "142", "201"],
                       ["Year 11", "155", "188"]]),
                "<p>A school surveyed its pupils about screen time in 2019 and again in "
                "2023. Reported screen time rose in every year group over the period. "
                "The head of pastoral care suggested that the rise had been steepest "
                "among the youngest pupils surveyed, but the survey data do not bear "
                "this out: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?")
            + choices_html([
                "Year 7 pupils reported 164 minutes in 2023, more than they had reported "
                "in 2019.",
                "screen time among Year 9 pupils rose by 59 minutes over the period, "
                "more than the 46-minute rise reported by Year 7 pupils.",
                "Year 11 pupils reported the highest screen time of any group in both "
                "years surveyed.",
                "screen time among Year 7 pupils fell between 2019 and 2023.",
            ])
            + '<span class="sr-time">⏱ ~85 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1–3-qadam — jadval.</strong> O'lchangan narsa: kunlik ekran "
            "vaqti. Birlik: <u>daqiqa</u>. Ustunlar: ikki yil, ya'ni "
            "<mark>o'sishni hisoblash mumkin</mark>. Qatorlar: uch sinf, ya'ni "
            "guruhlarni solishtirish mumkin.</p>"
            "<p><strong>4-qadam — matn.</strong> Da'vo: o'sish "
            "<u>eng yoshlarda eng keskin</u> bo'lgan. Va matn buni rad etadi "
            "(<em>do not bear this out</em>). Demak bo'sh joyga <u>rad etuvchi</u> "
            "dalil kerak.</p>"
            "<p><strong>5-qadam — bashorat.</strong> Da'vo solishtiruv, demak javobda "
            "ikkita o'sish bo'lishi kerak: 7-sinfniki va undan kattarog'i. "
            "Hisoblaymiz: 7-sinf 164 − 118 = <strong>46</strong>; "
            "9-sinf 201 − 142 = <strong>59</strong>; "
            "11-sinf 188 − 155 = <strong>33</strong>.</p>"
            + why([
                (True, "screen time among Year 9 pupils rose by 59 minutes over the period, more than the 46-minute rise reported by Year 7 pupils",
                 "ikkita o'sish, ikkovi ham to'g'ri hisoblangan, va ular aynan "
                 "da'voni rad etadi: eng yoshlar (7-sinf, 46) eng keskin "
                 "o'smagan."),
                (False, "Year 7 pupils reported 164 minutes in 2023, more than they had reported in 2019",
                 "<strong>rost, lekin da'voga tegmaydi.</strong> Bitta guruhning "
                 "o'sgani jadvalda bor, lekin da'vo <u>guruhlar orasidagi</u> "
                 "solishtiruv haqida edi. Bitta son solishtiruvni rad etolmaydi."),
                (False, "Year 11 pupils reported the highest screen time of any group in both years surveyed",
                 "<strong>jadvalga zid.</strong> 2019-yilda ha (155 eng katta), "
                 "lekin 2023-yilda 11-sinf 188, 9-sinf esa 201. "
                 "<em>in both years</em> iborasini tekshirmagan o'quvchi "
                 "yiqiladi."),
                (False, "screen time among Year 7 pupils fell between 2019 and 2023",
                 "<strong>jadvalga zid</strong> va matnga ham zid: matn "
                 "<em>rose in every year group</em> deb aytib turibdi. "
                 "Yo'nalishni teskari qilgan tuzoq."),
            ])
            + NOTE.format(
                "Diqqat qiling: to'rtta variantdan <u>ikkitasi</u> jadvalga "
                "to'g'ridan-to'g'ri zid edi. Bu shu turda odatiy hol — va shuning "
                "uchun jadvalni birinchi o'qigan odam ularni bir zumda o'chiradi.")
        )},

        {
            "rich_text": data_q(
                "Germination Rate of Stored Seeds (percent of seeds sprouting)",
                table(["Storage temperature", "After 1 year", "After 5 years"],
                      [["−18 °C", "96", "91"],
                       ["4 °C", "94", "72"],
                       ["20 °C", "89", "31"]]),
                "<p>A seed bank compared three storage temperatures by testing how many "
                "stored seeds would still sprout. Freezing is far more expensive to "
                "maintain than refrigeration, and the bank's report argued that the "
                "advantage of freezing over refrigeration only becomes clear over longer "
                "storage periods.</p>",
                "Which choice most effectively uses data from the table to support the "
                "report's argument?"),
            "choices": [
                {"text": "After 1 year the two temperatures differed by only 2 percentage points, but after 5 years the difference had grown to 19.", "is_correct": True},
                {"text": "Seeds stored at 20 °C sprouted at a rate of 31 percent after 5 years.", "is_correct": False},
                {"text": "Seeds stored at −18 °C sprouted at a rate of 96 percent after 1 year.", "is_correct": False},
                {"text": "After 5 years, seeds stored at 4 °C sprouted at a higher rate than seeds stored at −18 °C.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> muzlatishning sovutishdan "
                "<u>ustunligi faqat uzoq muddatda</u> ko'rinadi. Bu ikki qismli "
                "solishtiruv: qisqa muddatda farq kichik, uzoq muddatda katta.</p>"
                "<p><strong>Hisob:</strong> 1 yil — 96 − 94 = <strong>2</strong>; "
                "5 yil — 91 − 72 = <strong>19</strong>.</p>"
                + why([
                    (True, "After 1 year the two temperatures differed by only 2 percentage points, but after 5 years the difference had grown to 19",
                     "ikkala qismni ham beradi va ikkala son ham to'g'ri. "
                     "<em>only … but</em> qurilishi da'voning «faqat uzoq muddatda» "
                     "qismini aynan ifodalaydi."),
                    (False, "Seeds stored at 20 °C sprouted at a rate of 31 percent after 5 years",
                     "<strong>rost, lekin da'voga tegmaydi</strong>: 20 °C "
                     "solishtiruvda umuman qatnashmaydi. Da'vo faqat muzlatish va "
                     "sovutish haqida."),
                    (False, "Seeds stored at −18 °C sprouted at a rate of 96 percent after 1 year",
                     "rost, lekin <u>bitta son</u>. Da'vo ikki muddatni "
                     "solishtiryapti — bitta qiymat buni ko'rsatolmaydi."),
                    (False, "After 5 years, seeds stored at 4 °C sprouted at a higher rate than seeds stored at −18 °C",
                     "<strong>jadvalga zid</strong>: 5 yildan keyin 4 °C da 72, "
                     "−18 °C da 91. Yo'nalish teskari qilingan."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Bird Species Recorded in Forest Patches of Different Sizes",
                table(["Patch size (hectares)", "Species recorded"],
                      [["1", "14"], ["5", "29"], ["25", "41"], ["125", "49"]]),
                "<p>An ecologist surveying forest fragments recorded how many bird "
                "species appeared in patches of four different sizes. She proposed that "
                "although larger patches always hold more species, each step up in size "
                "adds fewer new species than the step before it.</p>",
                "Which choice most effectively uses data from the table to support the "
                "ecologist's proposal?"),
            "choices": [
                {"text": "Going from 1 to 5 hectares added 15 species, while going from 25 to 125 hectares added only 8.", "is_correct": True},
                {"text": "The 125-hectare patch recorded 49 species, more than any other patch surveyed.", "is_correct": False},
                {"text": "The 25-hectare patch recorded 41 species.", "is_correct": False},
                {"text": "Each step up in patch size added more species than the step before it.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo ikki qismli:</strong> (1) kattaroq maydonda "
                "har doim ko'proq tur, (2) lekin har qadam <u>kamroq</u> "
                "qo'shadi. Ikkinchi qism isbot talab qiladi.</p>"
                "<p><strong>Hisob — har qadamning qo'shgani:</strong> "
                "1→5: 29 − 14 = <strong>15</strong>; "
                "5→25: 41 − 29 = <strong>12</strong>; "
                "25→125: 49 − 41 = <strong>8</strong>. "
                "Ketma-ketlik kamayib boryapti.</p>"
                + why([
                    (True, "Going from 1 to 5 hectares added 15 species, while going from 25 to 125 hectares added only 8",
                     "birinchi va oxirgi qadamni solishtiradi — kamayishni "
                     "ko'rsatishning eng qisqa yo'li. Ikkala son ham to'g'ri."),
                    (False, "The 125-hectare patch recorded 49 species, more than any other patch surveyed",
                     "<strong>rost, lekin faqat birinchi qismni</strong> "
                     "isbotlaydi (kattaroq maydon = ko'proq tur). Da'voning "
                     "isbot talab qiladigan ikkinchi qismiga tegmaydi."),
                    (False, "The 25-hectare patch recorded 41 species",
                     "bitta son, hech qanday solishtiruvsiz. Kamayish "
                     "<u>ikki qadamni</u> yonma-yon qo'yganda ko'rinadi."),
                    (False, "Each step up in patch size added more species than the step before it",
                     "<strong>jadvalga zid</strong>: 15 → 12 → 8, ya'ni kamayib "
                     "boryapti. Da'voning aynan teskarisi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Applications and Offers, Two University Departments, 2024",
                table(["Department", "Applications received", "Offers made"],
                      [["Physics", "420", "84"], ["History", "180", "45"]]),
                "<p>A university published the number of applications each department "
                "received in 2024 and the number of offers it made. Reading the figures, "
                "a student claimed that History had been the harder of the two "
                "departments to receive an offer from. The published figures do not "
                "support that claim: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "History made offers to 25 percent of its applicants, while Physics made offers to 20 percent of its own.", "is_correct": True},
                {"text": "Physics received 420 applications, more than twice as many as History received.", "is_correct": False},
                {"text": "Physics made 84 offers, nearly twice the 45 offers made by History.", "is_correct": False},
                {"text": "History made offers to a smaller share of its applicants than Physics did.", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol butun mavzuning eng muhim darsini beradi: "
                "<mark>son va ulush bir narsa emas</mark>.</p>"
                "<p><strong>Da'vo:</strong> Tarix bo'limidan taklif olish "
                "<u>qiyinroq</u>. «Qiyinlik» — bu ariza soniga nisbatan taklif "
                "ulushi, taklifning <u>soni</u> emas.</p>"
                "<p><strong>Hisob:</strong> Fizika 84 ÷ 420 = 0.20 = "
                "<strong>20%</strong>; Tarix 45 ÷ 180 = 0.25 = "
                "<strong>25%</strong>. Tarixdan taklif olish "
                "<u>osonroq</u> ekan.</p>"
                + why([
                    (True, "History made offers to 25 percent of its applicants, while Physics made offers to 20 percent of its own",
                     "ikkala ulushni ham beradi va da'voni aynan rad etadi. "
                     "Faqat shu variant «qiyinlik» tushunchasini to'g'ri "
                     "o'lchaydi."),
                    (False, "Physics made 84 offers, nearly twice the 45 offers made by History",
                     "<strong>rost, lekin noto'g'ri o'lchov</strong> — va bu eng "
                     "ko'p tanlanadigan variant. Fizika ko'proq taklif qildi, "
                     "chunki unga ko'proq ariza kelgan. Sonlar ulushni "
                     "almashtira olmaydi."),
                    (False, "Physics received 420 applications, more than twice as many as History received",
                     "rost (420 ÷ 180 ≈ 2.3), lekin ariza <u>soni</u> qiyinlik "
                     "haqida hech nima demaydi."),
                    (False, "History made offers to a smaller share of its applicants than Physics did",
                     "<strong>jadvalga zid</strong>: 25% > 20%. Bu variant "
                     "to'g'ri o'lchovni ishlatadi-yu, natijani teskari aytadi."),
                ])
                + WARN.format(
                    "<strong>Foiz va son.</strong> Jadvalda ikkala ustun ham "
                    "berilgan bo'lsa, SAT deyarli har doim shu farqni sinaydi. "
                    "Da'voda <em>rate · share · proportion · more likely · "
                    "harder</em> so'zlari bo'lsa — javob "
                    "<u>bo'linma</u> bo'lishi kerak, xom son emas.")
            ),
        },

        {
            "rich_text": data_q(
                "Annual Rainfall and Reservoir Level, City Catchment",
                table(["Year", "Rainfall (mm)", "Reservoir on 1 September (percent full)"],
                      [["2020", "410", "62"],
                       ["2021", "395", "51"],
                       ["2022", "430", "44"],
                       ["2023", "405", "33"]]),
                "<p>The reservoir supplying a city has stood lower on 1 September in "
                "each of the last four years. The water utility attributed the decline "
                "to falling rainfall in the surrounding catchment. The recorded figures "
                "do not support that explanation: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "rainfall in 2022 was the highest of the four years recorded, yet the reservoir fell again that September.", "is_correct": True},
                {"text": "the reservoir stood at 33 percent full in 2023, its lowest level in the period.", "is_correct": False},
                {"text": "rainfall fell in every year between 2020 and 2023.", "is_correct": False},
                {"text": "the reservoir level rose in the year that recorded the highest rainfall.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da\u2019vo:</strong> suv omborining pasayishi "
                "<u>yog\u2018inning kamayishidan</u>. Uni rad etish uchun "
                "yog\u2018in va sathning <mark>birga harakat qilmasligini</mark> "
                "ko\u2018rsatish kerak.</p>"
                "<p><strong>Jadvalni o\u2018qiymiz.</strong> Yog\u2018in: 410 \u2192 395 "
                "\u2192 <strong>430</strong> \u2192 405 \u2014 pasayib bormaydi, 2022-yilda "
                "eng yuqori. Sath: 62 \u2192 51 \u2192 44 \u2192 33 \u2014 har yili "
                "pasaygan. Ikki ustun bir yo\u2018nalishda yurmayapti.</p>"
                + why([
                    (True, "rainfall in 2022 was the highest of the four years recorded, yet the reservoir fell again that September",
                     "eng aniq zarba: yog\u2018in eng ko\u2018p bo\u2018lgan yili ham sath "
                     "tushgan (51 \u2192 44). Bitta yil tushuntirishni buzish uchun "
                     "yetarli."),
                    (False, "the reservoir stood at 33 percent full in 2023, its lowest level in the period",
                     "<strong>rost, lekin da\u2019voga tegmaydi</strong>: sathning "
                     "pasaygani allaqachon matnda aytilgan. Savol "
                     "<u>sababi</u> haqida, va bu variantda yog\u2018in umuman "
                     "yo\u2018q."),
                    (False, "rainfall fell in every year between 2020 and 2023",
                     "<strong>jadvalga zid</strong>: 395 \u2192 430 \u2014 o\u2018sgan. Va bu "
                     "variant kommunal xizmatning tushuntirishini "
                     "<u>qo\u2018llab-quvvatlardi</u>, rad etmasdi."),
                    (False, "the reservoir level rose in the year that recorded the highest rainfall",
                     "<strong>jadvalga zid</strong>: eng ko\u2018p yog\u2018in 2022-yilda "
                     "(430), o\u2018sha yili sath 51 dan 44 ga <u>tushgan</u>."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to bear out a claim</div><div class="pp-card-back">da\'voni tasdiqlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a percentage point</div><div class="pp-card-back">foiz punkti (foizlar ayirmasi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a share / a proportion</div><div class="pp-card-back">ulush, nisbat</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">germination rate</div><div class="pp-card-back">unib chiqish darajasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">steepest rise</div><div class="pp-card-back">eng keskin o\'sish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a step up in size</div><div class="pp-card-back">o\'lchamdagi keyingi bosqich</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">applicants</div><div class="pp-card-back">ariza topshirganlar</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">over the period</div><div class="pp-card-back">shu davr mobaynida</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Tartib: <strong>sarlavha → birlik → ustunlar → matn → "
              "bashorat</strong>.</li>"
              "<li>Da'vo solishtiruv bo'lsa — javobda <strong>ikkita son</strong> "
              "bo'lishi kerak.</li>"
              "<li>Variantlarning ikkitasi odatda jadvalga <u>zid</u> bo'ladi — "
              "ularni darrov o'chiring.</li>"
              "<li><strong>Son ≠ ulush.</strong> <em>rate · share · harder · more "
              "likely</em> bo'lsa, bo'linma kerak.</li>"
              "<li>Hisob-kitob deyarli yo'q: ayirish yoki oddiy bo'lish.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 61
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_Q,
    "title": "SAT R&W 61: Choices That Misread the Figure — The Four Data Traps",
    "summary": "Noto'g'ri variantlarning ko'pi jadvalni noto'g'ri o'qiydi: qator "
               "almashtirilgan, yo'nalish teskari, birlik chalkash yoki qiymat umuman yo'q.",
    "order": 61,
    "blocks": [
        {"rich_text": (
            "<h2>Jadvalga zid variantlar</h2>"
            "<p>60-darsda ko'rdik: to'rt variantdan odatda <u>ikkitasi</u> jadvalga "
            "to'g'ridan-to'g'ri zid bo'ladi. Bu ajoyib yangilik — chunki ularni "
            "o'chirish uchun hech qanday fikrlash kerak emas, faqat "
            "<mark>tekshirish</mark> kerak.</p>"
            "<p>Bu dars o'sha ikkitasini tanib olish haqida. Ular to'rtta shakldan "
            "biriga tushadi.</p>"
            + '<span class="sr-time">⏱ ~80 soniya</span>'
        )},

        {"rich_text": (
            "<h3>To'rt shakl</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tuzoq</th><th>Qanday ko'rinadi</th><th>Tekshirish</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>1. Yo'nalish teskari</strong></td>"
              "<td><em>rose</em> deyilgan joyda jadval tushganini ko'rsatadi</td>"
              "<td>Ikki sonni solishtiring: qaysi biri katta?</td></tr>"
              "<tr><td><strong>2. Qator/ustun almashgan</strong></td>"
              "<td>Boshqa guruhning yoki boshqa yilning raqami</td>"
              "<td>Barmog'ingizni qatorga qo'ying va yuring</td></tr>"
              "<tr><td><strong>3. Birlik chalkash</strong></td>"
              "<td>Foizni songa, jamini o'sishga, mingni birga aylantiradi</td>"
              "<td>Sarlavhadagi birlikni qayta o'qing</td></tr>"
              "<tr><td><strong>4. Qiymat umuman yo'q</strong></td>"
              "<td>Jadvalda bo'lmagan yosh guruhi, yil yoki toifa</td>"
              "<td>O'sha satr jadvalda bormi?</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "To'rttasi ham <u>o'qish</u> bilan hal qilinadi, "
                "<u>fikrlash</u> bilan emas. Shuning uchun ularni birinchi "
                "o'chiring: jadvalga zid variantni topish 5 soniya oladi, "
                "«qaysi biri da'voni yaxshiroq isbotlaydi» degan savol esa "
                "30 soniya.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + data_q(
                "Households With Home Internet Access, by Region (percent of households)",
                table(["Region", "2015", "2023"],
                      [["North", "48", "79"],
                       ["Central", "61", "88"],
                       ["South", "34", "71"]]),
                "<p>A national statistics office recorded home internet access in three "
                "regions in 2015 and again in 2023. Access rose in all three. A report "
                "on the figures argued that the distance between the best-connected and "
                "the least-connected region had narrowed over the period: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?")
            + choices_html([
                "the gap between the Central and South regions fell from 27 percentage "
                "points in 2015 to 17 in 2023.",
                "access in the Central region reached 88 percent in 2023, the highest of "
                "any region.",
                "the gap between the Central and South regions grew from 27 percentage "
                "points to 17.",
                "access in the North was lower than in the South in both years recorded.",
            ])
            + '<span class="sr-time">⏱ ~80 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim — avval zid variantlarni o'chiramiz</h3>"
            "<p><strong>Jadval:</strong> birlik — <u>foiz</u>. Eng yuqori: Central "
            "(61 va 88). Eng past: South (34 va 71).</p>"
            "<p><strong>Farqlar:</strong> 2015-yil 61 − 34 = <strong>27</strong>; "
            "2023-yil 88 − 71 = <strong>17</strong>. Farq "
            "<mark>qisqargan</mark>, demak hisobot to'g'ri.</p>"
            + why([
                (True, "the gap between the Central and South regions fell from 27 percentage points in 2015 to 17 in 2023",
                 "ikkala farq ham to'g'ri hisoblangan, va <em>fell</em> "
                 "yo'nalishi ham to'g'ri. Da'vo (<em>narrowed</em>) aynan shu."),
                (False, "the gap between the Central and South regions grew from 27 percentage points to 17",
                 "<strong>1-tuzoq: yo'nalish teskari.</strong> Sonlar to'g'ri, "
                 "lekin 27 dan 17 ga o'tish — bu <u>qisqarish</u>, o'sish emas. "
                 "Variantning oxirigacha o'qimagan odam bu ikkisini "
                 "adashtiradi."),
                (False, "access in the North was lower than in the South in both years recorded",
                 "<strong>2-tuzoq: qator almashgan.</strong> Aksincha: North 48, "
                 "South 34 (2015); North 79, South 71 (2023). Har ikki yilda ham "
                 "North yuqori."),
                (False, "access in the Central region reached 88 percent in 2023, the highest of any region",
                 "jadvalga <u>zid emas</u> — bu rost. Lekin da'vo "
                 "<u>farqning qisqarishi</u> haqida, va bitta son farqni "
                 "ko'rsata olmaydi. Bu boshqa turdagi tuzoq — 62-darsning "
                 "mavzusi."),
            ])
            + NOTE.format(
                "Diqqat qiling: to'rttadan <u>ikkitasi</u> jadvalga zid edi "
                "(yo'nalish va qator), bittasi rost-lekin-yetarli-emas, va "
                "faqat bittasi javob. Bu bu turdagi eng ko'p uchraydigan "
                "taqsimot.")
        )},

        {
            "rich_text": data_q(
                "Recyclable Material Collected per Household per Week (kilograms)",
                table(["Material", "2018", "2023"],
                      [["Paper", "4.1", "2.6"],
                       ["Glass", "2.8", "3.0"],
                       ["Plastic", "1.9", "3.4"]]),
                "<p>A council publishes the average weight of each material its "
                "collection service takes from a household each week. A councillor "
                "remarked that the move away from printed newspapers and magazines could "
                "be read directly off these figures: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the weight of paper collected fell from 4.1 kilograms to 2.6 kilograms per household per week.", "is_correct": True},
                {"text": "the weight of plastic collected rose from 1.9 kilograms to 3.4 kilograms per household per week.", "is_correct": False},
                {"text": "the weight of paper collected rose from 2.6 kilograms to 4.1 kilograms per household per week.", "is_correct": False},
                {"text": "the weight of glass collected fell between 2018 and 2023.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> bosma gazeta va jurnallardan voz "
                "kechish. Jadvalda buni ko'rsatadigan yagona qator — "
                "<mark>qog'oz</mark>.</p>"
                + why([
                    (True, "the weight of paper collected fell from 4.1 kilograms to 2.6 kilograms per household per week",
                     "to'g'ri qator, to'g'ri yo'nalish, to'g'ri sonlar "
                     "(4.1 → 2.6). Va bu aynan bosma mahsulotning kamayishi."),
                    (False, "the weight of paper collected rose from 2.6 kilograms to 4.1 kilograms per household per week",
                     "<strong>1-tuzoq: yo'nalish teskari.</strong> Sonlar "
                     "jadvalda bor, lekin yillar almashtirilgan: 2018-yil 4.1, "
                     "2023-yil 2.6."),
                    (False, "the weight of plastic collected rose from 1.9 kilograms to 3.4 kilograms per household per week",
                     "<strong>2-tuzoq: qator almashgan.</strong> Sonlar to'g'ri, "
                     "lekin plastik gazeta emas. Da'voga aloqasi yo'q."),
                    (False, "the weight of glass collected fell between 2018 and 2023",
                     "<strong>1-tuzoq yana:</strong> shisha 2.8 dan 3.0 ga "
                     "<u>ko'tarilgan</u>."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Annual Visitors to Three Museums (thousands)",
                table(["Museum", "2022", "2023"],
                      [["City Museum", "412", "386"],
                       ["Maritime Museum", "96", "121"],
                       ["Textile Museum", "58", "65"]]),
                "<p>Combined attendance at a city's three museums was almost unchanged "
                "between 2022 and 2023, but the change was not shared evenly among them. "
                "A trustee observed that the two smaller museums had grown while the "
                "largest had not: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the City Museum lost 26 thousand visitors, while the Maritime and Textile museums together gained 32 thousand.", "is_correct": True},
                {"text": "the Maritime Museum received 121 more visitors in 2023 than it had in 2022.", "is_correct": False},
                {"text": "the City Museum received 386 thousand visitors in 2023.", "is_correct": False},
                {"text": "the Textile Museum was the largest of the three museums in 2023.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Birlikni o'qing:</strong> sarlavhada "
                "<em>(thousands)</em> — ya'ni 412 degani 412 000.</p>"
                "<p><strong>Hisob:</strong> City 386 − 412 = <strong>−26</strong> "
                "ming; Maritime 121 − 96 = <strong>+25</strong> ming; "
                "Textile 65 − 58 = <strong>+7</strong> ming. Ikki kichigi "
                "birgalikda 25 + 7 = <strong>32</strong> ming qo'shgan.</p>"
                + why([
                    (True, "the City Museum lost 26 thousand visitors, while the Maritime and Textile museums together gained 32 thousand",
                     "uchala son ham to'g'ri, birlik ham to'g'ri saqlangan, va "
                     "da'voning ikkala yarmini ham beradi: kattasi yo'qotdi, "
                     "kichiklari qo'shdi."),
                    (False, "the Maritime Museum received 121 more visitors in 2023 than it had in 2022",
                     "<strong>3-tuzoq: birlik chalkash — va ikki barobar.</strong> "
                     "Birinchidan, 121 — bu <u>jami</u>, o'sish emas (o'sish 25). "
                     "Ikkinchidan, birlik <u>ming</u>, ya'ni 121 ta tashrifchi "
                     "emas. Eng ko'p tanlanadigan noto'g'ri javob."),
                    (False, "the Textile Museum was the largest of the three museums in 2023",
                     "<strong>jadvalga zid:</strong> 65 eng kichigi, 386 esa eng "
                     "kattasi."),
                    (False, "the City Museum received 386 thousand visitors in 2023",
                     "rost va birligi ham to'g'ri, lekin bitta son "
                     "solishtiruvni ko'rsatmaydi. Da'vo ikki tomonli."),
                ])
                + WARN.format(
                    "<strong>«Thousands» so'zi sarlavhada turadi va oson "
                    "o'tkazib yuboriladi.</strong> Har jadval sarlavhasini "
                    "oxirigacha o'qing — qavs ichidagi birlik ko'pincha butun "
                    "savolning kaliti.")
            ),
        },

        {
            "rich_text": data_q(
                "Time Spent in Deep Sleep per Night, by Age Group (minutes)",
                table(["Age group", "Men", "Women"],
                      [["20–29", "82", "91"],
                       ["40–49", "54", "68"],
                       ["60–69", "31", "44"]]),
                "<p>A sleep laboratory measured how long participants of different ages "
                "spent in deep sleep each night. Deep sleep declined with age in both "
                "groups measured, but a researcher reviewing the results noted that the "
                "decline had been steeper in one of them: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "deep sleep among men fell by 51 minutes between the youngest and oldest groups, compared with 47 minutes among women.", "is_correct": True},
                {"text": "women aged 30–39 recorded 79 minutes of deep sleep per night.", "is_correct": False},
                {"text": "men in the 40–49 group recorded 54 minutes, fewer than women of the same age.", "is_correct": False},
                {"text": "deep sleep among women fell more steeply than among men.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Hisob:</strong> erkaklar 82 − 31 = "
                "<strong>51</strong> daqiqa; ayollar 91 − 44 = "
                "<strong>47</strong> daqiqa. Pasayish erkaklarda keskinroq.</p>"
                + why([
                    (True, "deep sleep among men fell by 51 minutes between the youngest and oldest groups, compared with 47 minutes among women",
                     "ikkala pasayish ham to'g'ri hisoblangan va yonma-yon "
                     "qo'yilgan — da'vo (<em>steeper in one of them</em>) aynan "
                     "shuni talab qiladi."),
                    (False, "women aged 30–39 recorded 79 minutes of deep sleep per night",
                     "<strong>4-tuzoq: jadvalda bunday qator yo'q.</strong> "
                     "Yosh guruhlari 20–29, 40–49 va 60–69. 30–39 o'lchanmagan, "
                     "va 79 soni jadvalning hech qayerida uchramaydi. Bu "
                     "tuzoqning eng oson tanilishi — faqat qarash kerak."),
                    (False, "men in the 40–49 group recorded 54 minutes, fewer than women of the same age",
                     "rost (54 < 68), lekin bu <u>bitta yoshdagi farq</u> — "
                     "da'vo esa <u>yosh bo'yicha pasayishning tezligi</u> "
                     "haqida. Boshqa savolga to'g'ri javob."),
                    (False, "deep sleep among women fell more steeply than among men",
                     "<strong>1-tuzoq: yo'nalish teskari.</strong> 47 < 51, "
                     "ya'ni ayollarda pasayish sekinroq."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Electricity Generated by Source, National Grid (terawatt-hours)",
                table(["Source", "2016", "2023"],
                      [["Coal", "74", "12"],
                       ["Gas", "118", "96"],
                       ["Wind", "21", "83"],
                       ["Solar", "4", "19"]]),
                "<p>Total generation on the national grid fell slightly between 2016 and "
                "2023, but the mix of sources changed a great deal. An analyst reviewing "
                "the figures observed that the fall in coal generation had been matched "
                "almost exactly by the rise in wind: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "coal generation fell by 62 terawatt-hours over the period, while wind generation rose by 62.", "is_correct": True},
                {"text": "coal generation fell by 12 terawatt-hours over the period.", "is_correct": False},
                {"text": "wind generation reached 83 terawatt-hours in 2023, more than any other source.", "is_correct": False},
                {"text": "gas generation rose between 2016 and 2023.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Hisob:</strong> ko\u2018mir 74 \u2212 12 = "
                "<strong>62</strong> pasaygan; shamol 83 \u2212 21 = "
                "<strong>62</strong> ko\u2018tarilgan. Ikkovi aynan teng \u2014 "
                "analitikning gapi shu.</p>"
                + why([
                    (True, "coal generation fell by 62 terawatt-hours over the period, while wind generation rose by 62",
                     "ikkala <u>o\u2018zgarish</u> ham to\u2018g\u2018ri hisoblangan va "
                     "yonma-yon qo\u2018yilgan \u2014 <em>matched almost exactly</em> "
                     "aynan shuni talab qiladi."),
                    (False, "coal generation fell by 12 terawatt-hours over the period",
                     "<strong>3-tuzoq: jami \u2260 o\u2018zgarish.</strong> 12 \u2014 bu "
                     "ko\u2018mirning 2023-yildagi <u>qiymati</u>, pasayish miqdori "
                     "emas. Pasayish 62."),
                    (False, "wind generation reached 83 terawatt-hours in 2023, more than any other source",
                     "<strong>jadvalga zid:</strong> gaz 96, ya\u2019ni shamoldan "
                     "yuqori. Va bu solishtiruv da\u2019voga ham tegmaydi."),
                    (False, "gas generation rose between 2016 and 2023",
                     "<strong>1-tuzoq: yo\u2018nalish teskari.</strong> Gaz 118 dan "
                     "96 ga tushgan."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to narrow (of a gap)</div><div class="pp-card-back">(farq) qisqarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to be read off the figures</div><div class="pp-card-back">raqamlardan bevosita ko\'rinmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">combined attendance</div><div class="pp-card-back">umumiy tashrifchilar soni</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">evenly shared</div><div class="pp-card-back">teng taqsimlangan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">steeper decline</div><div class="pp-card-back">keskinroq pasayish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">(thousands)</div><div class="pp-card-back">ming hisobida (jadval sarlavhasida)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">per household per week</div><div class="pp-card-back">har xonadonga, har haftada</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the largest of the three</div><div class="pp-card-back">uchtasining eng kattasi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Jadvalga zid variantlarni <strong>birinchi</strong> o'chiring — "
              "bu 5 soniya oladi.</li>"
              "<li>To'rt shakl: <strong>yo'nalish teskari · qator almashgan · "
              "birlik chalkash · qiymat yo'q</strong>.</li>"
              "<li>Sarlavhadagi qavsni o'qing: <em>(thousands)</em>, "
              "<em>(percent)</em>, <em>(minutes)</em>.</li>"
              "<li><strong>Jami ≠ o'sish.</strong> Jadvaldagi son ustunning "
              "qiymati, ikki yil orasidagi farq emas.</li>"
              "<li>Jadvalda bo'lmagan toifa yoki yil — eng oson tanaladigan "
              "tuzoq.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 62
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_Q,
    "title": "SAT R&W 62: Data That Is Accurate but Does Not Support the Claim",
    "summary": "Jadvalni to'g'ri o'qigan variant ham javob bo'lmasligi mumkin: raqam "
               "da'voga tegishi shart, va ba'zan u da'vodan oldin ham rost bo'lgan.",
    "order": 62,
    "blocks": [
        {"rich_text": (
            "<h2>Rost, lekin isbot emas</h2>"
            "<p>61-darsda jadvalga <u>zid</u> variantlarni o'chirishni o'rgandik. "
            "Ular ketgach odatda ikkitasi qoladi, va ikkalasi ham "
            "<mark>jadvalga to'liq mos</mark> bo'ladi.</p>"
            "<p>Endi ikkinchi savol boshlanadi, va u qiyinroq: "
            "<strong>bu raqam da'voni isbotlaydimi?</strong></p>"
            + EXAMP.format(
                "<p style=\"font-size:1.06em;margin:0;\">Jadvaldan to'g'ri o'qilgan "
                "raqam <u>uch sababdan</u> javob bo'lmasligi mumkin:<br>"
                "<strong>1.</strong> solishtiruvning faqat bir tomonini beradi;<br>"
                "<strong>2.</strong> da'voda umuman yo'q toifa haqida;<br>"
                "<strong>3.</strong> da'vodan <u>oldin ham</u> rost bo'lgan — "
                "ya'ni hech nimani isbotlamaydi.</p>")
            + "<p>Uchinchisi eng nozigi va SAT uni juda yaxshi ko'radi.</p>"
            + '<span class="sr-time">⏱ ~85 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uchinchi shakl: «bu avval ham shunday edi»</h3>"
            "<p>Ko'p savolda da'vo biror <u>o'zgarish</u> yoki <u>ta'sir</u> haqida "
            "bo'ladi: yangi yo'lak velosipedchilarni ko'paytirdi, yangi dori "
            "kasallikni kamaytirdi.</p>"
            "<p>Bunday da'voni isbotlash uchun raqam <mark>oldin va keyin</mark> ni "
            "solishtirishi kerak — yoki <mark>ta'sir bor va yo'q joyni</mark>. "
            "Faqat «keyin» ni ko'rsatgan raqam hech nimani isbotlamaydi.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Sinov savoli:</strong> «bu raqam "
              "o'zgarishdan <u>oldin</u> ham rost bo'lgan bo'lishi "
              "mumkinmi?»</p></div>"
            + "<div class=\"pp-step\"><p>Javob «ha» bo'lsa — u dalil emas. "
              "Riverside yo'lida velosipedchilar High Street'dan ko'p bo'lgani "
              "yangi yo'lakni isbotlamaydi, chunki ular <u>yo'lak "
              "qurilishidan oldin ham</u> ko'p edi.</p></div>"
            + "<div class=\"pp-step\"><p>Bu 53-darsdagi «ikki tomonga ham "
              "yaraydigan» sinovining raqamli ko'rinishi. Bir xil "
              "fikrlash — boshqa material.</p></div>"
            + '</div>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + data_q(
                "Cycle Journeys Recorded at Two Counters (thousands per year)",
                table(["Year", "Riverside path", "High Street"],
                      [["2019", "88", "34"],
                       ["2021", "141", "39"],
                       ["2023", "152", "41"]]),
                "<p>The city built a protected cycle lane along the Riverside path in "
                "2020 and made no change to High Street, where cyclists share the road "
                "with traffic. A transport officer argued that the protected lane, "
                "rather than a general rise in cycling across the city, accounts for the "
                "growth recorded on Riverside: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?")
            + choices_html([
                "journeys on Riverside rose by about 60 percent between 2019 and 2021, "
                "while journeys on the unchanged High Street rose by about 15 percent.",
                "journeys on Riverside reached 152 thousand in 2023, the highest figure "
                "recorded at either counter.",
                "journeys on Riverside were higher than journeys on High Street in every "
                "year recorded.",
                "journeys on High Street rose in every period recorded.",
            ])
            + '<span class="sr-time">⏱ ~85 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>Da'vo:</strong> o'sishni <u>yo'lak</u> keltirdi, "
            "<u>umumiy moda</u> emas. Bu ikki tushuntirish orasidagi tanlov — "
            "demak raqam ularni <mark>bir-biridan ajratishi</mark> kerak.</p>"
            "<p>Ajratuvchi narsa nima? <u>High Street</u> — u o'zgarmagan, ya'ni "
            "u nazorat guruhi. Agar o'sish faqat Riverside'da bo'lsa, sabab "
            "yo'lak; ikkalasida ham bir xil bo'lsa, sabab umumiy moda.</p>"
            "<p><strong>Hisob (2019 → 2021, ya'ni yo'lak qurilgan davr):</strong> "
            "Riverside 141 − 88 = 53, ya'ni 53 ÷ 88 ≈ <strong>60%</strong>; "
            "High Street 39 − 34 = 5, ya'ni 5 ÷ 34 ≈ <strong>15%</strong>.</p>"
            + why([
                (True, "journeys on Riverside rose by about 60 percent between 2019 and 2021, while journeys on the unchanged High Street rose by about 15 percent",
                 "ikkala yo'lni ham, o'sish davrini ham qamraydi. Riverside "
                 "to'rt barobar tezroq o'sgan — bu aynan «yo'lak, umumiy moda "
                 "emas» degan da'voni ko'taradi."),
                (False, "journeys on Riverside were higher than journeys on High Street in every year recorded",
                 "<strong>3-shakl: bu 2019-yilda ham rost edi</strong> — yo'lak "
                 "qurilishidan bir yil oldin (88 va 34). Yo'lak qurilishidan "
                 "oldin ham rost bo'lgan fakt yo'lakning ta'sirini isbotlay "
                 "olmaydi. Bu darsning asosiy tuzog'i."),
                (False, "journeys on Riverside reached 152 thousand in 2023, the highest figure recorded at either counter",
                 "<strong>1-shakl: solishtiruvning bir tomoni.</strong> Rost, "
                 "lekin High Street'siz bu raqam ikki tushuntirishni "
                 "ajratmaydi — umumiy moda ham xuddi shu raqamni berardi."),
                (False, "journeys on High Street rose in every period recorded",
                 "rost (34 → 39 → 41), lekin bu <u>raqib</u> tushuntirishni "
                 "oziqlantiradi: umumiy o'sish bor ekan. O'zi holda u "
                 "ofitserning da'vosiga qarshi ishlaydi."),
            ])
            + TIP.format(
                "Jadvalda <strong>o'zgarmagan ustun</strong> bo'lsa — "
                "High Street, nazorat guruhi, «boshqa bo'lim» — javob deyarli "
                "har doim <u>o'sha ustunni ham ishlatadi</u>. SAT uni bekorga "
                "qo'ymaydi.")
        )},

        {
            "rich_text": data_q(
                "Pupils Reaching the Expected Reading Standard (percent)",
                table(["School", "2021", "2024"],
                      [["Oq Tepa (new programme)", "58", "74"],
                       ["Chinor (new programme)", "61", "79"],
                       ["Bogʻishamol (no change)", "63", "77"]]),
                "<p>Two schools in a district introduced a new reading programme in 2022; "
                "a third continued as before. The district's report claimed that the new "
                "programme was responsible for the improvement at the two schools that "
                "adopted it. The figures give little support to that claim: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the school that made no change improved by 14 percentage points, close to the 16 and 18 points recorded at the two programme schools.", "is_correct": True},
                {"text": "Chinor recorded 79 percent in 2024, the highest figure of the three schools.", "is_correct": False},
                {"text": "all three schools recorded a higher figure in 2024 than in 2021.", "is_correct": False},
                {"text": "Oq Tepa recorded the lowest figure of the three schools in 2021.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> yaxshilanish <u>dasturdan</u>. "
                "Rad etish uchun dastursiz maktabning ham xuddi shunday "
                "yaxshilanganini ko'rsatish kerak.</p>"
                "<p><strong>Hisob:</strong> Oq Tepa 74 − 58 = <strong>16</strong>; "
                "Chinor 79 − 61 = <strong>18</strong>; Bogʻishamol (dastursiz) "
                "77 − 63 = <strong>14</strong>. Uchalasi ham deyarli bir xil.</p>"
                + why([
                    (True, "the school that made no change improved by 14 percentage points, close to the 16 and 18 points recorded at the two programme schools",
                     "uchala o'zgarishni ham beradi va nazorat maktabini "
                     "markazga qo'yadi — bu da'voni rad etishning yagona yo'li."),
                    (False, "all three schools recorded a higher figure in 2024 than in 2021",
                     "<strong>rost, lekin yetarli emas.</strong> Bu "
                     "yaxshilanish borligini aytadi, lekin <u>qanchaligini</u> "
                     "emas — va aynan miqdorlar da'voni rad etadi. Yarim "
                     "qadam."),
                    (False, "Chinor recorded 79 percent in 2024, the highest figure of the three schools",
                     "<strong>1-shakl: bir tomon.</strong> Bitta maktabning "
                     "bitta yildagi qiymati dasturning ta'sirini ko'rsatolmaydi."),
                    (False, "Oq Tepa recorded the lowest figure of the three schools in 2021",
                     "<strong>3-shakl: bu dasturdan oldin ham rost edi.</strong> "
                     "2021 — dastur joriy etilishidan bir yil oldin. Boshlang'ich "
                     "daraja dasturning ta'siri haqida hech nima demaydi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Nesting Pairs Recorded on Two Islands",
                table(["Year", "Kichik Orol (rats removed 2019)", "Katta Orol (rats present)"],
                      [["2017", "310", "540"],
                       ["2022", "590", "560"]]),
                "<p>Introduced rats eat the eggs of ground-nesting seabirds. A "
                "conservation team removed the rats from one island in 2019 and left a "
                "neighbouring island untreated. The team reported that the removal, and "
                "not some wider change in the region's seabird population, explains what "
                "happened next: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to support the "
                "team's report?"),
            "choices": [
                {"text": "nesting pairs on the treated island rose by 280 between 2017 and 2022, while the untreated island gained only 20.", "is_correct": True},
                {"text": "the treated island recorded 590 nesting pairs in 2022, more than the untreated island.", "is_correct": False},
                {"text": "the untreated island recorded more nesting pairs than the treated island in 2017.", "is_correct": False},
                {"text": "both islands recorded more nesting pairs in 2022 than in 2017.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> o'sish <u>kalamush olib "
                "tashlanganidan</u>, mintaqaviy o'zgarishdan emas. Ikkinchi "
                "orol — nazorat.</p>"
                "<p><strong>Hisob:</strong> Kichik Orol 590 − 310 = "
                "<strong>280</strong>; Katta Orol 560 − 540 = "
                "<strong>20</strong>.</p>"
                + why([
                    (True, "nesting pairs on the treated island rose by 280 between 2017 and 2022, while the untreated island gained only 20",
                     "ikkala o'zgarishni yonma-yon qo'yadi. Mintaqaviy sabab "
                     "bo'lganda ikkala orol ham o'sardi — 280 va 20 esa buni "
                     "rad etadi."),
                    (False, "the treated island recorded 590 nesting pairs in 2022, more than the untreated island",
                     "<strong>1-shakl: faqat «keyin».</strong> 2022-yildagi "
                     "solishtiruv boshlang'ich holatni hisobga olmaydi — va u "
                     "faqat ozgina farq (590 va 560)."),
                    (False, "the untreated island recorded more nesting pairs than the treated island in 2017",
                     "<strong>3-shakl: bu aralashuvdan oldin ham rost edi</strong> "
                     "(540 > 310, 2017-yil). Boshlang'ich farq kalamush olib "
                     "tashlashning ta'siri haqida hech nima demaydi."),
                    (False, "both islands recorded more nesting pairs in 2022 than in 2017",
                     "rost, lekin bu <u>raqib</u> tushuntirishga xizmat qiladi: "
                     "ikkala orolda ham o'sish bo'lgani mintaqaviy sababni "
                     "eslatadi. Da'voni kuchsizlantiradi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Average Yield of Two Wheat Varieties (tonnes per hectare)",
                table(["Rainfall in season", "Variety A", "Variety B"],
                      [["Below average", "2.1", "2.9"],
                       ["Average", "4.4", "4.6"],
                       ["Above average", "6.8", "5.2"]]),
                "<p>An agronomist compared two wheat varieties across seasons of "
                "different rainfall. She advised farmers without irrigation to plant "
                "Variety B, on the grounds that its advantage appears precisely in the "
                "seasons those farmers most need protection from: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to support the "
                "agronomist's advice?"),
            "choices": [
                {"text": "in a below-average season Variety B yielded 2.9 tonnes per hectare against Variety A's 2.1.", "is_correct": True},
                {"text": "in an above-average season Variety A yielded 6.8 tonnes per hectare, the highest figure in the table.", "is_correct": False},
                {"text": "in an average season the two varieties yielded 4.4 and 4.6 tonnes per hectare respectively.", "is_correct": False},
                {"text": "Variety B yielded more than Variety A in every season recorded.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> B ning ustunligi <u>quruq "
                "mavsumda</u> — sug'ormaydigan dehqon eng qo'rqadigan holat. "
                "Demak javob <mark>below-average</mark> qatoriga tegishi "
                "kerak.</p>"
                + why([
                    (True, "in a below-average season Variety B yielded 2.9 tonnes per hectare against Variety A's 2.1",
                     "aynan kerakli qator, ikkala navning qiymati bilan. "
                     "2.9 va 2.1 — B ning ustunligi eng kerakli sharoitda."),
                    (False, "in an average season the two varieties yielded 4.4 and 4.6 tonnes per hectare respectively",
                     "<strong>2-shakl: da'voda yo'q toifa.</strong> Rost, lekin "
                     "o'rtacha mavsum maslahat qaratilgan holat emas, va farq "
                     "arzimas (0.2)."),
                    (False, "in an above-average season Variety A yielded 6.8 tonnes per hectare, the highest figure in the table",
                     "rost, lekin bu <u>A ning</u> foydasiga ishlaydi va "
                     "sug'ormaydigan dehqon uchun eng kam ahamiyatli qator. "
                     "Maslahatga qarshi dalil."),
                    (False, "Variety B yielded more than Variety A in every season recorded",
                     "<strong>jadvalga zid</strong> — ko'p yog'inli mavsumda A "
                     "6.8, B esa 5.2. Bu variant to'g'ri tuyuladi, chunki u "
                     "maslahatni kuchaytirardi; lekin jadval uni rad etadi."),
                ])
                + WARN.format(
                    "Oxirgi variant bu turdagi eng ayyor tuzoq: u da'voni "
                    "<u>kerakligidan ham kuchliroq</u> qilib aytadi. "
                    "«Har doim yaxshiroq» — agronom bunday demagan, va jadval "
                    "ham buni ko'tarmaydi. <strong>Da'vodan kuchliroq "
                    "variantga ishonmang.</strong>")
            ),
        },

        {
            "rich_text": data_q(
                "Median Time From Graduation to First Job Offer (weeks)",
                table(["Field of study", "2018", "2023"],
                      [["Engineering", "9", "7"],
                       ["Nursing", "5", "4"],
                       ["Law", "14", "19"],
                       ["Design", "16", "21"]]),
                "<p>A university careers service announced that its graduates were "
                "finding work faster than they had five years earlier. The figures it "
                "published show a more divided picture than the announcement suggests: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "waiting times fell in engineering and nursing but rose in law and design.", "is_correct": True},
                {"text": "nursing graduates waited less time than graduates in any other field in both years.", "is_correct": False},
                {"text": "design graduates waited 21 weeks in 2023, longer than graduates in any other field.", "is_correct": False},
                {"text": "waiting times rose in every field between 2018 and 2023.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da\u2019vo:</strong> manzara <u>bo\u2018lingan</u> \u2014 ya\u2019ni "
                "bir qismida yaxshilanish, bir qismida yomonlashish. Javob "
                "<mark>ikkala yo\u2018nalishni ham</mark> ko\u2018rsatishi kerak.</p>"
                "<p><strong>Jadval:</strong> muhandislik 9 \u2192 7 va hamshiralik "
                "5 \u2192 4 (tushgan); huquq 14 \u2192 19 va dizayn 16 \u2192 21 "
                "(ko\u2018tarilgan).</p>"
                + why([
                    (True, "waiting times fell in engineering and nursing but rose in law and design",
                     "to\u2018rtala sohani ham qamraydi va <em>but</em> orqali "
                     "bo\u2018linishni ko\u2018rsatadi \u2014 da\u2019vo aynan shu."),
                    (False, "nursing graduates waited less time than graduates in any other field in both years",
                     "<strong>3-shakl: bu 2018-yilda ham rost edi.</strong> "
                     "Hamshiralikning eng tez ekani o\u2018zgarish haqida hech nima "
                     "demaydi \u2014 va bo\u2018linishni umuman ko\u2018rsatmaydi."),
                    (False, "design graduates waited 21 weeks in 2023, longer than graduates in any other field",
                     "<strong>1-shakl: bir tomon.</strong> Yomonlashgan tomonni "
                     "beradi, yaxshilangan tomonni emas \u2014 \u00abbo\u2018lingan\u00bb "
                     "so\u2018zi ikkovini ham talab qiladi."),
                    (False, "waiting times rose in every field between 2018 and 2023",
                     "<strong>jadvalga zid:</strong> muhandislik va hamshiralikda "
                     "tushgan."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to account for ~</div><div class="pp-card-back">~ ni tushuntirmoq, sababi bo\'lmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a control group</div><div class="pp-card-back">nazorat guruhi (o\'zgartirilmagan)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">untreated</div><div class="pp-card-back">aralashuvsiz qoldirilgan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on the grounds that ~</div><div class="pp-card-back">~ degan asosda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a wider change</div><div class="pp-card-back">kengroq, umumiy o\'zgarish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">nesting pairs</div><div class="pp-card-back">uya quruvchi juftliklar</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">yield (tonnes per hectare)</div><div class="pp-card-back">hosildorlik (gektariga tonna)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">respectively</div><div class="pp-card-back">mos ravishda, tartib bilan</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Jadvalga mos bo'lgan variant ham javob bo'lmasligi mumkin.</li>"
              "<li>Uch shakl: <strong>bir tomon · da'voda yo'q toifa · "
              "«oldin ham rost edi»</strong>.</li>"
              "<li>Sinov: «bu raqam o'zgarishdan <u>oldin</u> ham rost "
              "bo'larmidi?» Ha bo'lsa — dalil emas.</li>"
              "<li>Jadvalda <strong>o'zgarmagan ustun</strong> bo'lsa, javob "
              "uni ham ishlatadi.</li>"
              "<li>Da'vodan <u>kuchliroq</u> variant («har doim», «hech qachon») "
              "deyarli har doim tuzoq.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 63
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_Q,
    "title": "SAT R&W 63: Completing a Sentence With a Number From the Figure",
    "summary": "Bo'sh joydan oldingi bir-ikki so'z — since, although, yet, more than — "
               "javobning yo'nalishini va shaklini oldindan belgilaydi.",
    "order": 63,
    "blocks": [
        {"rich_text": (
            "<h2>Bo'sh joy atrofidagi so'zlar</h2>"
            "<p>Bu turdagi savollarning ko'pi <em>complete the text</em> shaklida "
            "keladi: matn bo'sh joy bilan tugaydi va siz uni raqam bilan "
            "to'ldirasiz.</p>"
            "<p>Muhim narsa shuki, bo'sh joy <mark>gapning o'rtasida</mark> turadi, "
            "va undan oldingi so'zlar javobga <u>ikki xil cheklov</u> qo'yadi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Bog'lovchi</th><th>Javob nima qilishi kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>since · because · as</em></td>"
              "<td>Oldingi gapning <u>sababini</u> berish</td></tr>"
              "<tr><td><em>although · yet · but · however</em></td>"
              "<td>Oldingi gapga <u>qarshi</u> raqam berish</td></tr>"
              "<tr><td><em>do not support · give little support to</em></td>"
              "<td>Da'voni <u>rad etuvchi</u> raqam</td></tr>"
              "<tr><td><em>for example · indeed · in fact</em></td>"
              "<td>Oldingi gapni <u>tasdiqlovchi</u> raqam</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "12-darsdagi signal so'zlar shu yerda ham ishlaydi — faqat "
                "materiali raqam. <strong>Bo'sh joydan oldingi ikki so'zni "
                "o'qing</strong>, keyin jadvalga qarang. Ko'p savolda o'sha ikki "
                "so'z ikkita variantni darrov o'chiradi.")
            + '<span class="sr-time">⏱ ~80 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikkinchi cheklov: shakl</h3>"
            "<p>Bo'sh joy gapning bir bo'lagi, ya'ni javob "
            "<u>grammatik jihatdan</u> ham o'tirishi kerak. Bu bepul yordam:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>…, since <span class=\"sr-blank\"></span></em> "
                "— to'liq gap kerak («X rose by 12 while Y fell by 3»).<br>"
                "<em>…, a difference of <span class=\"sr-blank\"></span></em> — "
                "faqat son kerak («14 percentage points»).<br>"
                "<em>…, which is <span class=\"sr-blank\"></span> than …</em> — "
                "solishtiruv so'zi kerak («more», «fewer»).</p>")
            + "<p>Grammatika Words in Context'dagi kabi hal qiluvchi emas — bu yerda "
            "to'rt variant odatda bir xil shaklda bo'ladi — lekin u ba'zan bitta "
            "variantni bepul o'chiradi. Tekshirib qo'ying.</p>"
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + data_q(
                "Passengers Carried on Two Rail Lines (millions per year)",
                table(["Year", "Northern line", "Coastal line"],
                      [["2019", "12.4", "3.1"],
                       ["2023", "10.9", "4.6"]]),
                "<p>A rail operator has proposed closing the Coastal line and putting the "
                "money into the Northern line, which carries far more passengers each "
                "year. Critics of the proposal accept the totals but argue that the "
                "decision looks different if the direction of travel rather than the "
                "size of each line is considered, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?")
            + choices_html([
                "the Northern line carried 10.9 million passengers in 2023, more than "
                "twice the 4.6 million carried on the Coastal line.",
                "the Northern line lost 1.5 million passengers over the period while the "
                "Coastal line gained 1.5 million.",
                "the Coastal line carried 3.1 million passengers in 2019.",
                "both lines carried fewer passengers in 2023 than they had in 2019.",
            ])
            + '<span class="sr-time">⏱ ~80 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yechim</h3>"
            "<p><strong>1-qadam — bo'sh joydan oldingi so'zlar.</strong> "
            "<em>…the decision looks different if the <u>direction of travel</u> "
            "rather than the <u>size</u> is considered, <mark>since</mark></em>.</p>"
            "<p>Ikkita cheklov darrov chiqadi: (1) <em>since</em> — javob "
            "tanqidchilarning <u>sababi</u> bo'lishi kerak; (2) "
            "<em>direction rather than size</em> — javob <u>o'zgarish</u> "
            "haqida bo'lishi kerak, jami haqida emas. Matn buni "
            "o'zi aytib turibdi.</p>"
            "<p><strong>2-qadam — hisob:</strong> Northern 10.9 − 12.4 = "
            "<strong>−1.5</strong> million; Coastal 4.6 − 3.1 = "
            "<strong>+1.5</strong> million.</p>"
            + why([
                (True, "the Northern line lost 1.5 million passengers over the period while the Coastal line gained 1.5 million",
                 "aynan <u>yo'nalish</u> haqida, va ikkala liniyani ham beradi. "
                 "<em>since</em> talab qilgan sabab — bu."),
                (False, "the Northern line carried 10.9 million passengers in 2023, more than twice the 4.6 million carried on the Coastal line",
                 "rost, lekin bu <u>jami</u> — ya'ni matn aynan chetga surgan "
                 "o'lchov (<em>rather than the size</em>). Va u operatorning "
                 "foydasiga ishlaydi, tanqidchilarning emas. "
                 "<strong>Bo'sh joydan oldingi so'zlar buni bir zumda "
                 "o'chiradi.</strong>"),
                (False, "the Coastal line carried 3.1 million passengers in 2019",
                 "bitta son, yo'nalish yo'q. <em>since</em> dan keyin sabab "
                 "kerak edi — bu esa shunchaki fakt."),
                (False, "both lines carried fewer passengers in 2023 than they had in 2019",
                 "<strong>jadvalga zid:</strong> Coastal 3.1 dan 4.6 ga "
                 "<u>ko'tarilgan</u>."),
            ])
            + NOTE.format(
                "Bu savolda matnning o'zi javobning turini aytib berdi: "
                "<em>direction … rather than size</em>. SAT ko'pincha shunday "
                "qiladi — <strong>bo'sh joydan oldingi jumla javobning "
                "ta'rifini beradi</strong>. Uni o'qish jadvalni "
                "o'qishdan ham foydaliroq.")
        )},

        {
            "rich_text": data_q(
                "Cost of a Bus Journey and Number of Journeys Taken, City Network",
                table(["Year", "Single fare (soʻm)", "Journeys (millions)"],
                      [["2020", "1,400", "212"],
                       ["2022", "1,700", "204"],
                       ["2024", "2,000", "231"]]),
                "<p>The city raised the single bus fare twice between 2020 and 2024. A "
                "councillor argued that fare increases inevitably drive passengers away. "
                "The network's own figures complicate that argument, however, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "journeys rose from 204 million to 231 million after the second increase, to a fare of 2,000 soʻm.", "is_correct": True},
                {"text": "the single fare rose from 1,400 soʻm in 2020 to 2,000 soʻm in 2024.", "is_correct": False},
                {"text": "journeys fell from 212 million to 204 million after the first increase.", "is_correct": False},
                {"text": "journeys fell after both of the fare increases.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>complicate that argument, however, <mark>since</mark></em>. "
                "Ikkita signal: <em>complicate</em> va <em>however</em> — javob "
                "kengashchining fikriga <u>qarshi</u> bo'lishi kerak.</p>"
                "<p>Kengashchi: narx oshsa — yo'lovchi kamayadi. Qarshi dalil: "
                "narx oshgan, lekin yo'lovchi <mark>ko'paygan</mark> holat.</p>"
                + why([
                    (True, "journeys rose from 204 million to 231 million after the second increase, to a fare of 2,000 soʻm",
                     "aynan qarshi holat: ikkinchi qimmatlashuvdan keyin "
                     "sayohatlar 27 million ko'paygan. Kengashchining "
                     "<em>inevitably</em> so'zini sindirish uchun bitta holat "
                     "yetarli."),
                    (False, "journeys fell from 212 million to 204 million after the first increase",
                     "rost, lekin bu kengashchining fikrini "
                     "<u>qo'llab-quvvatlaydi</u>. <em>however</em> teskari "
                     "yo'nalish talab qilyapti."),
                    (False, "journeys fell after both of the fare increases",
                     "<strong>jadvalga zid:</strong> ikkinchisidan keyin "
                     "ko'tarilgan (204 → 231)."),
                    (False, "the single fare rose from 1,400 soʻm in 2020 to 2,000 soʻm in 2024",
                     "rost, lekin bu faqat narx — yo'lovchilar haqida hech nima "
                     "demaydi, ya'ni bahsga umuman tegmaydi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Snow Cover on a Mountain Pass, First and Last Recorded Day",
                table(["Decade", "First snow (average day)", "Last snow (average day)"],
                      [["1970s", "12 October", "28 April"],
                       ["1990s", "24 October", "19 April"],
                       ["2010s", "6 November", "9 April"]]),
                "<p>A mountain station has recorded the first and last day of snow cover "
                "on a pass since the 1960s. The snow season has become shorter over the "
                "period, and it has done so at both ends, although "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the first snow has moved later by about twenty-five days, while the last snow has moved earlier by about nineteen.", "is_correct": True},
                {"text": "the snow season in the 2010s ran from 6 November to 9 April.", "is_correct": False},
                {"text": "the first snow has arrived later in each decade recorded.", "is_correct": False},
                {"text": "the last snow has moved later in each decade recorded.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>at both ends, <mark>although</mark></em>. "
                "<em>although</em> — qarshi qo'yish: ikki uchi ham qisqargan, "
                "<u>lekin</u> bir xil emas. Javob ikkalasini "
                "<mark>solishtirishi</mark> kerak.</p>"
                "<p><strong>Hisob:</strong> birinchi qor 12-oktabrdan "
                "6-noyabrga — oktyabr 31 kun, ya'ni 12-oktabrdan 31-oktabrgacha "
                "19 kun, ustiga 6 kun = <strong>25 kun</strong> kechikkan. "
                "Oxirgi qor 28-apreldan 9-aprelga — <strong>19 kun</strong> "
                "erta.</p>"
                + why([
                    (True, "the first snow has moved later by about twenty-five days, while the last snow has moved earlier by about nineteen",
                     "ikkala uchni ham beradi va ular teng emasligini "
                     "ko'rsatadi — <em>although</em> aynan shu "
                     "notekislikni talab qiladi."),
                    (False, "the first snow has arrived later in each decade recorded",
                     "rost (12 okt → 24 okt → 6 noy), lekin bu faqat "
                     "<u>bir uchi</u>. <em>both ends</em> ikkovini talab "
                     "qiladi, va <em>although</em> ham solishtiruv kutadi."),
                    (False, "the snow season in the 2010s ran from 6 November to 9 April",
                     "rost, lekin bu <u>bitta o'n yillik</u> — hech qanday "
                     "o'zgarish ko'rsatilmagan."),
                    (False, "the last snow has moved later in each decade recorded",
                     "<strong>jadvalga zid:</strong> 28 apr → 19 apr → 9 apr, "
                     "ya'ni <u>erta</u>lashib boryapti."),
                ])
                + TIP.format(
                    "Sanalar bilan ishlaganda ehtiyot bo'ling: <u>kechroq "
                    "birinchi qor</u> va <u>erta oxirgi qor</u> — ikkovi ham "
                    "mavsumni <strong>qisqartiradi</strong>. «Kechroq» "
                    "avtomatik «ko'proq» degani emas.")
            ),
        },

        {
            "rich_text": data_q(
                "Share of Journeys Under Two Kilometres Made on Foot (percent)",
                table(["Neighbourhood", "Before crossing installed", "After crossing installed"],
                      [["Yashnabod", "31", "48"],
                       ["Qoratosh", "44", "52"],
                       ["Mirobod (no crossing)", "38", "40"]]),
                "<p>Two neighbourhoods received a new pedestrian crossing on their main "
                "road; a third did not. Officials expected walking to increase most where "
                "it had been least common, and the survey bears this out, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "Yashnabod, which started at 31 percent, gained 17 points, while Qoratosh, which started at 44, gained 8.", "is_correct": True},
                {"text": "Qoratosh recorded the highest share of journeys made on foot after the crossing was installed.", "is_correct": False},
                {"text": "Mirobod, which received no crossing, gained 2 points over the same period.", "is_correct": False},
                {"text": "Yashnabod recorded the lowest share of journeys made on foot before the crossing was installed.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>bears this out, <mark>since</mark></em> — javob "
                "kutilgan narsani <u>tasdiqlashi</u> kerak.</p>"
                "<p><strong>Kutilgan narsa:</strong> yurish eng kam bo'lgan "
                "joyda eng ko'p o'sadi. Demak javob "
                "<mark>boshlang'ich daraja</mark> bilan "
                "<mark>o'sish</mark> ni bog'lashi shart — ikkita "
                "mahalla uchun.</p>"
                "<p><strong>Hisob:</strong> Yashnabod 48 − 31 = "
                "<strong>17</strong> (past boshlangan); Qoratosh 52 − 44 = "
                "<strong>8</strong> (yuqori boshlangan).</p>"
                + why([
                    (True, "Yashnabod, which started at 31 percent, gained 17 points, while Qoratosh, which started at 44, gained 8",
                     "boshlang'ich darajani ham, o'sishni ham, ikkala mahallani "
                     "ham beradi — kutilgan naqshni ko'rsatish uchun "
                     "kerakli hamma narsa."),
                    (False, "Yashnabod recorded the lowest share of journeys made on foot before the crossing was installed",
                     "rost, lekin bu faqat <u>boshlang'ich daraja</u> — "
                     "o'sish yo'q. Kutilgan narsa ikki o'lchovni bog'laydi."),
                    (False, "Qoratosh recorded the highest share of journeys made on foot after the crossing was installed",
                     "rost (52 eng yuqori), lekin bu kutilgan naqshga "
                     "<u>tegmaydi</u> — u o'sish haqida emas, yakuniy daraja "
                     "haqida."),
                    (False, "Mirobod, which received no crossing, gained 2 points over the same period",
                     "rost va foydali — lekin boshqa savol uchun. Nazorat "
                     "mahallasi o'tish joyi <u>ishlaganini</u> ko'rsatadi, "
                     "ammo bu yerdagi kutish «eng kam bo'lgan joyda eng ko'p» "
                     "degan <u>taqsimot</u> haqida edi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Average Nightly Temperature Difference, City Centre Minus Surrounding "
                "Countryside (degrees Celsius)",
                table(["Month", "2005", "2023"],
                      [["January", "1.8", "2.4"],
                       ["April", "2.2", "3.1"],
                       ["July", "3.4", "5.2"],
                       ["October", "2.0", "2.9"]]),
                "<p>A city centre stays warmer at night than the countryside around it, "
                "and that difference has widened over the past two decades. The widening "
                "has not been spread evenly across the year, however: it has been "
                "greatest in the month where the effect was already strongest, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the July difference grew by 1.8 degrees, twice the 0.9-degree growth recorded in April.", "is_correct": True},
                {"text": "the July difference reached 5.2 degrees in 2023, the largest figure anywhere in the table.", "is_correct": False},
                {"text": "the January difference was the smallest of the four months in both years recorded.", "is_correct": False},
                {"text": "the difference grew in every month except January.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo\u2018sh joydan oldingi so\u2018zlar:</strong> "
                "<em>greatest in the month where the effect was already strongest, "
                "<mark>since</mark></em>. Javob ikkita narsani bog\u2018lashi kerak: "
                "<u>eng katta o\u2018sish</u> va u <u>eng kuchli oy</u>da "
                "bo\u2018lgani.</p>"
                "<p><strong>Hisob \u2014 o\u2018sishlar:</strong> yanvar 2.4 \u2212 1.8 = "
                "0.6; aprel 3.1 \u2212 2.2 = 0.9; iyul 5.2 \u2212 3.4 = "
                "<strong>1.8</strong>; oktabr 2.9 \u2212 2.0 = 0.9. Iyul eng ko\u2018p "
                "o\u2018sgan \u2014 va u 2005-yilda ham eng katta bo\u2018lgan (3.4).</p>"
                + why([
                    (True, "the July difference grew by 1.8 degrees, twice the 0.9-degree growth recorded in April",
                     "ikkita <u>o\u2018sish</u>ni solishtiradi va iyulning ustunligini "
                     "ko\u2018rsatadi. Da\u2019vo o\u2018sishlarning notekisligi haqida edi, "
                     "va faqat shu variant o\u2018sishlarni beradi."),
                    (False, "the July difference reached 5.2 degrees in 2023, the largest figure anywhere in the table",
                     "rost, lekin bu <u>daraja</u>, <u>o\u2018sish</u> emas. Da\u2019vo "
                     "kengayishning qayerda eng katta bo\u2018lgani haqida."),
                    (False, "the January difference was the smallest of the four months in both years recorded",
                     "rost (1.8 va 2.4 \u2014 ikkovi ham eng kichigi), lekin yanvar "
                     "da\u2019voda umuman qatnashmaydi va bu ham o\u2018sish emas."),
                    (False, "the difference grew in every month except January",
                     "<strong>jadvalga zid:</strong> yanvarda ham o\u2018sgan "
                     "(1.8 \u2192 2.4)."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">since (bog\'lovchi)</div><div class="pp-card-back">chunki (sabab talab qiladi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to complicate an argument</div><div class="pp-card-back">dalilni qiyinlashtirmoq, oddiy emasligini ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">inevitably</div><div class="pp-card-back">muqarrar ravishda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the direction of travel</div><div class="pp-card-back">o\'zgarishning yo\'nalishi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">at both ends</div><div class="pp-card-back">ikkala uchidan ham</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to bear something out</div><div class="pp-card-back">tasdiqlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a single fare</div><div class="pp-card-back">bir martalik yo\'l haqi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a pedestrian crossing</div><div class="pp-card-back">piyodalar o\'tish joyi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Bo'sh joydan oldingi ikki so'zni o'qing</strong> — "
              "ular yo'nalishni belgilaydi.</li>"
              "<li><em>since · because</em> = sabab; <em>although · however · "
              "yet</em> = qarshi dalil; <em>bears this out</em> = tasdiq.</li>"
              "<li>Matn ko'pincha javobning <u>turini</u> ham aytadi "
              "(<em>direction rather than size</em>).</li>"
              "<li>Sanalarda: <u>kechroq boshlanish</u> + <u>ertaroq tugash</u> = "
              "qisqarish.</li>"
              "<li>Da'vo ikki o'lchovni bog'lasa (boshlang'ich daraja ↔ o'sish), "
              "javob ikkovini ham keltirsin.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 64
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_COE_Q,
    "title": "SAT R&W 64: Command of Evidence (Quantitative) — Mixed Practice",
    "summary": "Oltita jadvalli savol, barcha tuzoq turlari aralash, imtihon "
               "tezligida: 60–63-darslarni soatga qarshi mustahkamlash.",
    "order": 64,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol, oltita jadval, barcha tuzoq turlari aralash.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Har savolda shu tartib:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Jadval sarlavhasi va <u>birligi</u> (60-dars).</li>"
                "<li>Bo'sh joydan oldingi ikki so'z (63-dars).</li>"
                "<li>Jadvalga <u>zid</u> variantlarni o'chiring (61-dars).</li>"
                "<li>Qolganlaridan: qaysi biri da'voga <u>tegadi</u>? (62-dars)</li>"
                "</ol>")
            + "<p>Taymer: <strong>8 daqiqa</strong> (6 × 80 soniya).</p>"
            + '<span class="sr-time">⏱ 6 savol · 8 daqiqa</span>'
        )},

        {
            "rich_text": data_q(
                "Injuries Recorded at Two Factories, 2024",
                table(["Factory", "Workers", "Injuries recorded"],
                      [["Almazar plant", "1,250", "75"],
                       ["Sergeli plant", "400", "16"]]),
                "<p>An inspector reviewing two factories was told by the management at "
                "Almazar that its plant had the better safety record of the two. The "
                "published figures do not support that description: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "Almazar recorded 6 injuries per 100 workers, while Sergeli recorded 4.", "is_correct": True},
                {"text": "Almazar recorded 75 injuries against Sergeli's 16, more than four times as many.", "is_correct": False},
                {"text": "Sergeli recorded 6 injuries per 100 workers, while Almazar recorded 4.", "is_correct": False},
                {"text": "Almazar employs more than three times as many workers as Sergeli does.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>\u00abYaxshiroq xavfsizlik ko\u2018rsatkichi\u00bb</strong> \u2014 bu "
                "ishchi soniga nisbatan jarohat, xom son emas. Katta zavodda "
                "jarohat ko\u2018p bo\u2018lishi tabiiy.</p>"
                "<p><strong>Hisob:</strong> Almazar 75 \u00f7 1,250 = 0.06 = "
                "<strong>100 ishchiga 6 ta</strong>; Sergeli 16 \u00f7 400 = 0.04 = "
                "<strong>100 ishchiga 4 ta</strong>. Almazarning ko\u2018rsatkichi "
                "<mark>yomonroq</mark> \u2014 rahbariyatning gapi noto\u2018g\u2018ri.</p>"
                + why([
                    (True, "Almazar recorded 6 injuries per 100 workers, while Sergeli recorded 4",
                     "yagona variant ikkala <u>nisbatni</u> ham to\u2018g\u2018ri beradi va "
                     "Almazarni yomonroq ko\u2018rsatadi \u2014 ya\u2019ni da\u2019voni rad "
                     "etadi."),
                    (False, "Sergeli recorded 6 injuries per 100 workers, while Almazar recorded 4",
                     "nisbatlar <strong>almashtirilgan</strong>. Usul to\u2018g\u2018ri, "
                     "natija teskari \u2014 va bu variant Almazarning gapini "
                     "tasdiqlardi."),
                    (False, "Almazar recorded 75 injuries against Sergeli's 16, more than four times as many",
                     "<strong>xom son.</strong> 75 \u00f7 16 \u2248 4.7, rost \u2014 lekin "
                     "Almazarda ishchi ham uch baravardan ko\u2018p. Jarohat "
                     "<u>soni</u> xavfsizlikni o\u2018lchamaydi."),
                    (False, "Almazar employs more than three times as many workers as Sergeli does",
                     "rost (1,250 \u00f7 400 = 3.125), lekin bu faqat zavod "
                     "kattaligini aytadi \u2014 xavfsizlik haqida hech nima."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Weeds Recorded per Square Metre After Two Growing Seasons",
                table(["Plot", "Before treatment", "After two seasons"],
                      [["Cover crop sown", "42", "11"],
                       ["Mulch applied", "39", "18"],
                       ["Left bare (control)", "44", "40"]]),
                "<p>A research farm compared two ways of suppressing weeds without "
                "herbicide, alongside a plot left untreated. The farm reported that "
                "sowing a cover crop had been the more effective of the two treatments "
                "tested, and the counts support this: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the cover-crop plot fell by 31 weeds per square metre, against 21 on the mulched plot.", "is_correct": True},
                {"text": "the untreated plot fell by only 4 weeds per square metre over the same period.", "is_correct": False},
                {"text": "the cover-crop plot recorded 11 weeds per square metre after two seasons, the lowest count in the table.", "is_correct": False},
                {"text": "the mulched plot began with 39 weeds per square metre, fewer than either of the other two plots.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo:</strong> <u>ikki usuldan</u> qaysi biri "
                "yaxshiroq. Nazorat uchastkasi bu savolda emas — u boshqa "
                "savolga (usullar umuman ishlaydimi) javob berardi.</p>"
                "<p><strong>Hisob:</strong> qoplama ekin 42 − 11 = "
                "<strong>31</strong>; mulcha 39 − 18 = <strong>21</strong>.</p>"
                + why([
                    (True, "the cover-crop plot fell by 31 weeds per square metre, against 21 on the mulched plot",
                     "ikkala usulning <u>o'zgarishini</u> solishtiradi — "
                     "«qaysi biri samaraliroq» degan savolga yagona to'g'ri "
                     "javob shakli."),
                    (False, "the cover-crop plot recorded 11 weeds per square metre after two seasons, the lowest count in the table",
                     "<strong>bir tomon.</strong> Yakuniy son past, lekin "
                     "boshlang'ich darajalar har xil edi (42 va 39) — "
                     "solishtiruv o'zgarish bo'yicha bo'lishi kerak."),
                    (False, "the untreated plot fell by only 4 weeds per square metre over the same period",
                     "rost va foydali — lekin <u>boshqa da'vo</u> uchun. "
                     "Nazorat usullarning ishlaganini ko'rsatadi, ikkovini "
                     "bir-biri bilan solishtirmaydi."),
                    (False, "the mulched plot began with 39 weeds per square metre, fewer than either of the other two plots",
                     "rost, lekin bu faqat <u>boshlang'ich</u> holat — "
                     "samaradorlik haqida hech nima demaydi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Fish Landed at a Port (tonnes)",
                table(["Species", "2015", "2023"],
                      [["Herring", "8,400", "5,100"],
                       ["Mackerel", "3,200", "4,900"],
                       ["Cod", "1,900", "700"]]),
                "<p>Total landings at the port fell between 2015 and 2023, and a local "
                "newspaper described the decline as affecting every part of the fleet. "
                "The port's own records show otherwise: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "mackerel landings rose from 3,200 tonnes to 4,900 tonnes over the same period.", "is_correct": True},
                {"text": "herring landings fell from 8,400 tonnes to 5,100 tonnes over the period.", "is_correct": False},
                {"text": "cod landings fell by 700 tonnes over the period.", "is_correct": False},
                {"text": "mackerel landings fell from 4,900 tonnes to 3,200 tonnes over the period.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'sh joydan oldingi so'zlar:</strong> "
                "<em>show <mark>otherwise</mark></em> — gazetaning gapini "
                "(«hamma qismga ta'sir qilgan») rad etuvchi raqam kerak. "
                "Ya'ni <u>ko'tarilgan</u> tur.</p>"
                + why([
                    (True, "mackerel landings rose from 3,200 tonnes to 4,900 tonnes over the same period",
                     "yagona ko'tarilgan tur — «hamma tushdi» degan gapni "
                     "bitta misol bilan sindiradi."),
                    (False, "herring landings fell from 8,400 tonnes to 5,100 tonnes over the period",
                     "rost, lekin bu gazetaning gapini "
                     "<u>qo'llab-quvvatlaydi</u>. <em>otherwise</em> teskari "
                     "yo'nalish talab qiladi."),
                    (False, "mackerel landings fell from 4,900 tonnes to 3,200 tonnes over the period",
                     "<strong>yo'nalish teskari:</strong> yillar almashtirilgan. "
                     "2015-yil 3,200; 2023-yil 4,900."),
                    (False, "cod landings fell by 700 tonnes over the period",
                     "<strong>jami ≠ o'zgarish:</strong> 700 — bu 2023-yildagi "
                     "qiymat. Pasayish 1,900 − 700 = 1,200 tonna. "
                     "Va u ham gazetani qo'llab-quvvatlardi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Households Reporting a Vegetable Garden (percent of households surveyed)",
                table(["District", "2019", "2024"],
                      [["Rural district A", "71", "66"],
                       ["Rural district B", "68", "64"],
                       ["Suburban district C", "22", "38"]]),
                "<p>A survey of three districts found that the practice of growing "
                "vegetables at home is changing, though not in one direction. A "
                "researcher summarised the pattern by noting that the practice is "
                "spreading where it was rare and receding where it was common, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the suburban district rose from 22 to 38 percent while both rural districts fell by 4 or 5 points.", "is_correct": True},
                {"text": "rural district A recorded the highest share of households with a garden in both years.", "is_correct": False},
                {"text": "the suburban district recorded 38 percent in 2024, still below either rural district.", "is_correct": False},
                {"text": "all three districts recorded a lower share in 2024 than in 2019.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo ikki qismli:</strong> kam bo'lgan joyda "
                "<u>tarqalyapti</u>, ko'p bo'lgan joyda <u>chekinyapti</u>. "
                "Javob ikkala tomonni ham berishi shart.</p>"
                "<p><strong>Hisob:</strong> C 38 − 22 = <strong>+16</strong>; "
                "A 66 − 71 = <strong>−5</strong>; B 64 − 68 = "
                "<strong>−4</strong>.</p>"
                + why([
                    (True, "the suburban district rose from 22 to 38 percent while both rural districts fell by 4 or 5 points",
                     "ikkala yo'nalishni ham beradi va boshlang'ich darajalarni "
                     "(22 past, 71 va 68 baland) ham ko'rsatadi."),
                    (False, "rural district A recorded the highest share of households with a garden in both years",
                     "<strong>«bu avval ham rost edi»</strong> — 2019-yilda "
                     "ham eng yuqori edi. O'zgarish haqida hech nima "
                     "demaydi."),
                    (False, "the suburban district recorded 38 percent in 2024, still below either rural district",
                     "rost, lekin bu <u>daraja</u>, o'zgarish emas — va u "
                     "da'vodagi «tarqalyapti» qismini yashiradi."),
                    (False, "all three districts recorded a lower share in 2024 than in 2019",
                     "<strong>jadvalga zid:</strong> C 22 dan 38 ga "
                     "ko'tarilgan."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Average Wait for a Routine Appointment (days)",
                table(["Clinic", "Before online booking", "After online booking"],
                      [["Clinic 1 (online booking added)", "17", "11"],
                       ["Clinic 2 (online booking added)", "21", "14"],
                       ["Clinic 3 (no change)", "19", "12"]]),
                "<p>Two clinics in a district introduced online booking; a third kept its "
                "telephone system. The district's press release credited online booking "
                "with the shorter waits recorded afterwards. The figures give little "
                "support to that claim: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the clinic that made no change cut its wait by 7 days, as much as either clinic that added online booking.", "is_correct": True},
                {"text": "Clinic 2 recorded the longest wait of the three clinics before the change.", "is_correct": False},
                {"text": "Clinic 1 cut its average wait from 17 days to 11 days.", "is_correct": False},
                {"text": "all three clinics recorded a shorter wait after the change than before it.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Hisob:</strong> Klinika 1: 17 − 11 = "
                "<strong>6</strong>; Klinika 2: 21 − 14 = <strong>7</strong>; "
                "Klinika 3 (o'zgarishsiz): 19 − 12 = <strong>7</strong>.</p>"
                "<p>Nazorat klinikasi ikkalasidan kam emas — demak "
                "onlayn bandlov hech nimani tushuntirmaydi.</p>"
                + why([
                    (True, "the clinic that made no change cut its wait by 7 days, as much as either clinic that added online booking",
                     "nazorat guruhini markazga qo'yadi — da'voni rad etishning "
                     "yagona yo'li. 7 ≥ 6 va 7 = 7."),
                    (False, "all three clinics recorded a shorter wait after the change than before it",
                     "<strong>yarim qadam:</strong> rost va to'g'ri yo'nalishda, "
                     "lekin <u>qanchaligini</u> aytmaydi — aynan miqdorlar "
                     "da'voni rad etadi."),
                    (False, "Clinic 1 cut its average wait from 17 days to 11 days",
                     "rost, lekin bu da'voni <u>qo'llab-quvvatlaydi</u>: "
                     "onlayn bandlov qo'shgan klinikada qisqarish bor. "
                     "Rad etish uchun nazorat kerak."),
                    (False, "Clinic 2 recorded the longest wait of the three clinics before the change",
                     "<strong>«bu o'zgarishdan oldin ham rost edi»</strong> — "
                     "boshlang'ich daraja onlayn bandlovning ta'siri haqida "
                     "hech nima demaydi."),
                ])
            ),
        },

        {
            "rich_text": data_q(
                "Solar Panels Installed and Electricity Generated, Two Provinces, 2024",
                table(["Province", "Panels installed (thousands)", "Electricity generated (gigawatt-hours)"],
                      [["Province A", "480", "624"],
                       ["Province B", "150", "225"]]),
                "<p>Two provinces published their solar figures for 2024. Province A "
                "announced that it was making better use of its installed panels than "
                "its neighbour. The published figures point the other way, since "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "Province B generated 1.5 gigawatt-hours per thousand panels against Province A's 1.3.", "is_correct": True},
                {"text": "Province A generated 624 gigawatt-hours, nearly three times Province B's 225.", "is_correct": False},
                {"text": "Province A installed 480 thousand panels, more than three times as many as Province B.", "is_correct": False},
                {"text": "Province A generated 1.5 gigawatt-hours per thousand panels against Province B's 1.3.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>«Yaxshiroq foydalanish»</strong> — bu panel soniga "
                "nisbatan ishlab chiqarish, ya'ni <mark>bo'linma</mark>.</p>"
                "<p><strong>Hisob:</strong> A: 624 ÷ 480 = <strong>1.3</strong> "
                "GWh har ming panelga; B: 225 ÷ 150 = <strong>1.5</strong>. "
                "Ya'ni B samaraliroq — A ning e'loni noto'g'ri.</p>"
                + why([
                    (True, "Province B generated 1.5 gigawatt-hours per thousand panels against Province A's 1.3",
                     "to'g'ri bo'linma, va tartibi ham to'g'ri: B oldinda "
                     "qo'yilgan, ya'ni <em>point the other way</em> talabi "
                     "bajarilgan."),
                    (False, "Province A generated 1.5 gigawatt-hours per thousand panels against Province B's 1.3",
                     "usul to'g'ri, natija <strong>almashtirilgan</strong>: "
                     "624 ÷ 480 = 1.3, 225 ÷ 150 = 1.5. Bu tanlov Province A ni "
                     "samaraliroq ko'rsatadi, ya'ni e'lonni rad etish o'rniga "
                     "tasdiqlaydi."),
                    (False, "Province A generated 624 gigawatt-hours, nearly three times Province B's 225",
                     "<strong>xom son:</strong> 624 ÷ 225 ≈ 2.8, rost. Lekin "
                     "A ko'proq ishlab chiqargani ko'proq paneli borligidan — "
                     "samaradorlik haqida hech nima demaydi."),
                    (False, "Province A installed 480 thousand panels, more than three times as many as Province B",
                     "rost (480 ÷ 150 = 3.2), lekin bu faqat kirish — "
                     "natijaga nisbatan olinmagan."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Nima qilish kerak</th></tr></thead>"
              "<tbody>"
              "<tr><td>Xom sonni nisbat o'rniga oldim</td>"
              "<td>60-dars. <em>rate · share · better use · harder</em> = "
              "bo'linma.</td></tr>"
              "<tr><td>Jadvaldagi qiymatni o'zgarish deb oldim</td>"
              "<td>61-dars. Jami ≠ o'sish. Ayirishni bajaring.</td></tr>"
              "<tr><td>Yo'nalishni teskari o'qidim</td>"
              "<td>61-dars. Ikki sonni solishtiring.</td></tr>"
              "<tr><td>Nazorat ustunini e'tiborsiz qoldirdim</td>"
              "<td>62-dars. O'zgarmagan ustun bekorga qo'yilmaydi.</td></tr>"
              "<tr><td>O'zgarishdan oldin ham rost bo'lgan faktni tanladim</td>"
              "<td>62-dars. «Bu avval ham shunday edimi?»</td></tr>"
              "<tr><td>Bo'sh joydan oldingi bog'lovchini o'qimadim</td>"
              "<td>63-dars. <em>since · however · otherwise · bears this "
              "out</em>.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu mavzuda eng ko'p ball yeydigan bitta xato bor va u "
                "matematik emas: <strong>xom sonni nisbat o'rniga olish</strong>. "
                "Jadvalda «soni» va «umumiy soni» ustunlari birga tursa — "
                "SAT deyarli har doim bo'linmani so'rayapti.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">per 100 workers</div><div class="pp-card-back">har 100 ishchiga (nisbat)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rate</div><div class="pp-card-back">nisbat, daraja (bo\'linma)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to credit X with Y</div><div class="pp-card-back">Y ni X ning hisobiga yozmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to point the other way</div><div class="pp-card-back">aksini ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to recede</div><div class="pp-card-back">chekinmoq, kamayib bormoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">landings (of fish)</div><div class="pp-card-back">portga tushirilgan baliq miqdori</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to suppress weeds</div><div class="pp-card-back">begona o\'tlarni bostirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">show otherwise</div><div class="pp-card-back">aksini ko\'rsatmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa — Command of Evidence (Quantitative) mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Tartib: <strong>sarlavha → birlik → bog'lovchi → zid "
              "variantlar → da'voga tegishmi</strong>.</li>"
              "<li><strong>Son ≠ ulush.</strong> Bu mavzudagi eng qimmat xato.</li>"
              "<li>Jadvaldagi qiymat <u>o'zgarish emas</u> — ayirishni "
              "bajaring.</li>"
              "<li>O'zgarmagan ustun (nazorat) bo'lsa — javob uni ishlatadi.</li>"
              "<li>«Bu o'zgarishdan oldin ham rost edimi?» — ha bo'lsa, dalil "
              "emas.</li>"
              "</ul>"
        )},
    ],
},

]
