# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — Reading lessons 90-93.

"Yakuniy aralash amaliyot (Full Mixed Practice)" — the last topic of the reading
skill. Every question type from topics 2-8 appears here mixed, at exam pace, so
this file carries the full helper set rather than one topic's worth.
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

TOPIC_MIX = {
    "title":   "Yakuniy aralash amaliyot (Full Mixed Practice)",
    "summary": "Barcha savol turlari aralash, imtihon tartibida va imtihon "
               "tezligida — to'liq yarim modulgacha.",
    "icon":    "bi-flag-fill",
    "order":   9,
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


# ── question shapes, one per exam question type ────────────────────────────

def q(passage, stem):
    """Single passage pane + any bolded exam stem."""
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def blank_q(passage):
    return q(passage, "Which choice completes the text with the most logical and "
                      "precise word or phrase?")


def means_q(passage, word):
    return q(passage, f"As used in the text, what does the word “{word}” most nearly "
                      f"mean?")


def inf_q(passage):
    return q(passage, "Which choice most logically completes the text?")


def cross_q(text1, text2, stem):
    """Two stacked panes, labelled as the exam labels them."""
    return (f'<div class="sr-passage"><p><strong>Text 1</strong></p>{text1}</div>'
            f'<div class="sr-passage"><p><strong>Text 2</strong></p>{text2}</div>'
            f'<p><strong>{stem}</strong></p>')


def data_q(title, table_html, passage, stem):
    """A Quantitative question: figure card, then the text, then the stem."""
    return (f'<div class="sr-data"><p class="sr-data__title">{title}</p>'
            f'<div class="sr-data__scroll">{table_html}</div></div>'
            f'<div class="sr-passage">{passage}</div>'
            f'<p><strong>{stem}</strong></p>')


def table(headers, rows):
    head = ''.join(f'<th>{h}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def qnum(n, kind):
    """The little header that opens each practice question in a mixed set."""
    return (f'<p style="margin:0 0 4px;"><span style="background:#ede9fe;color:#5b21b6;'
            f'border-radius:999px;padding:2px 10px;font-size:.82rem;font-weight:600;">'
            f'{n}-savol · {kind}</span></p>')


LESSONS = [

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 90
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_MIX,
    "title": "SAT R&W 90: Mixed Module Practice 1 — Craft and Structure Under Time",
    "summary": "Craft and Structure domenining uchala turi aralash: so'z ma'nosi, "
               "matn tuzilishi va ikki matn — imtihondagi tartibda va tezlikda.",
    "order": 90,
    "blocks": [
        {"rich_text": (
            "<h2>Birinchi guruh — imtihondagidek</h2>"
            "<p>Bu yerdan yakuniy amaliyot boshlanadi. Endi savollar mavzu bo'yicha "
            "guruhlanmaydi — ular <mark>imtihondagi kabi aralash</mark> keladi, va "
            "har birida siz avval <u>qaysi tur ekanini</u> aniqlashingiz kerak.</p>"
            "<p>Bu dars <strong>Craft and Structure</strong> domeni — Bluebook mashq "
            "testlarida modulning boshida keladigan guruh. Uchta tur:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tur</th><th>Savol matni</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td>Words in Context</td>"
              "<td><em>…most logical and precise word…</em> / "
              "<em>…most nearly mean?</em></td><td>10–16</td></tr>"
              "<tr><td>Text Structure and Purpose</td>"
              "<td><em>…overall structure…</em> / <em>…main purpose…</em></td>"
              "<td>20–24</td></tr>"
              "<tr><td>Cross-Text Connections</td>"
              "<td><em>Based on the texts, how would…</em></td><td>30–33</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>7 daqiqa</strong> — 6 savol, o'rtacha 70 "
                "soniya. Cross-Text sekinroq, Words in Context tezroq: "
                "vaqtni o'zingiz taqsimlang.</li>"
                "<li>To'xtamasdan yeching. Qiynalsangiz — belgilang va "
                "keting.</li>"
                "<li>Keyin tushuntirishlarni o'qing.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 7 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Words in Context") + blank_q(
                "<p>The first maps of the sea floor drawn from sonar data were published "
                "as shaded relief, so that ridges and trenches appeared to be lit from "
                "one side. The convention was borrowed from land cartography and had no "
                "basis in anything a diver could see, since no light reaches those "
                "depths. It was adopted because a reader's eye reads shadow as shape "
                "without being taught to, making the maps immediately "
                "<span class=\"sr-blank\"></span> to people who had never handled "
                "sonar.</p>"),
            "choices": [
                {"text": "legible", "is_correct": True},
                {"text": "accurate", "is_correct": False},
                {"text": "affordable", "is_correct": False},
                {"text": "controversial", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Signal:</strong> <em>because a reader's eye reads shadow as "
                "shape without being taught to</em> — sabab beriladi, va u "
                "<mark>tushunish osonligi</mark> haqida.</p>"
                + why([
                    (True, "legible",
                     "«o'qish oson, tushunarli» — sabab ergash gapining aynan "
                     "natijasi, va <em>to people who had never handled sonar</em> "
                     "buni tasdiqlaydi."),
                    (False, "accurate",
                     "«aniq» — matn soyaning <u>haqiqiy emasligini</u> aytadi "
                     "(<em>no basis in anything a diver could see</em>). Aniqlik "
                     "aynan qurbon qilingan narsa."),
                    (False, "affordable",
                     "narx umuman muhokama qilinmaydi."),
                    (False, "controversial",
                     "<em>The convention was borrowed</em> va <em>It was "
                     "adopted</em> — hech qanday bahs yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Words in Context") + means_q(
                "<p>The court records give the miller's holding as three acres and a "
                "<span class=\"sr-focus\">mean</span> house by the water, and value the "
                "whole at less than the smith's tools alone. The clerk who wrote them "
                "used the same word for the holdings of four other families in the same "
                "entry.</p>", "mean"),
            "choices": [
                {"text": "modest", "is_correct": True},
                {"text": "unkind", "is_correct": False},
                {"text": "average", "is_correct": False},
                {"text": "intended", "is_correct": False},
            ],
            "explanation": (
                "<p>Eski hujjat — 15-darsning shubha rejimi. <em>mean</em> ning "
                "bugungi ma'nosi («qo'pol») uyga tegishli bo'lolmaydi.</p>"
                "<p><strong>Isbot:</strong> <em>value the whole at less than the "
                "smith's tools alone</em> — mulk juda arzon. Demak uy "
                "<mark>kamtarona, oddiy</mark>.</p>"
                + why([
                    (True, "modest",
                     "«oddiy, kamtarona» — <em>mean</em> ning eski ma'nosi, va "
                     "qiymat haqidagi bo'lak buning isboti."),
                    (False, "unkind",
                     "bugungi asosiy ma'no, shuning uchun eng kuchli tuzoq. "
                     "Lekin uy mehribon yoki qo'pol bo'lolmaydi."),
                    (False, "average",
                     "<em>mean</em> matematikada «o'rtacha» degani, va bu "
                     "ma'no real. Lekin uy arzimas darajada arzon — "
                     "o'rtacha emas."),
                    (False, "intended",
                     "<em>to mean</em> fe'lining ma'nosi; bu yerda "
                     "<em>mean</em> sifat."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Text Structure and Purpose") + q(
                "<p>Traffic engineers once judged a junction by how many vehicles it "
                "could pass in an hour, and the safest-looking designs were those with "
                "the clearest sightlines. Collision records at junctions rebuilt on that "
                "principle did not improve, and at some of them worsened. The "
                "explanation now offered is that a driver who can see far ahead drives "
                "faster, and that the margin gained by the sightline is spent on "
                "speed.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It states a design principle, reports that the results contradicted it, and gives the explanation now accepted.", "is_correct": True},
                {"text": "It compares two junction designs and recommends one of them.", "is_correct": False},
                {"text": "It criticises traffic engineers for ignoring collision records.", "is_correct": False},
                {"text": "It describes a method of counting vehicles and explains its limitations.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Besh so'zli bashorat</strong> (21-dars): «qoida, keyin "
                "teskari natija, keyin izoh». Uch jumla, uch harakat.</p>"
                + why([
                    (True, "It states a design principle, reports that the results contradicted it, and gives the explanation now accepted",
                     "uchala harakatni ham to'g'ri tartibda nomlaydi."),
                    (False, "It criticises traffic engineers for ignoring collision records",
                     "<strong>yarim to'g'ri:</strong> muhandislar xato qilgan. "
                     "Lekin matn ularni ayblamaydi va ular yozuvlarni "
                     "e'tiborsiz qoldirgan ham emas — yozuvlar aynan "
                     "tekshirilgan."),
                    (False, "It compares two junction designs and recommends one of them",
                     "ikkinchi loyiha ham, tavsiya ham yo'q."),
                    (False, "It describes a method of counting vehicles and explains its limitations",
                     "<strong>doirasi juda tor:</strong> sanoq birinchi "
                     "jumlaning yarmi, matnning mavzusi emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Text Structure and Purpose") + q(
                "<p>Every guidebook to the old quarter reproduces the same photograph of "
                "the covered bridge, taken from the eastern bank at about four in the "
                "afternoon. <span class=\"sr-focus\">A visitor standing on the western "
                "bank at nine in the morning will not recognise the place.</span> The "
                "bridge is the same; what the photograph records is one hour of one kind "
                "of light, repeated until it has become the thing itself.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It gives the concrete case that the final sentence then explains.", "is_correct": True},
                {"text": "It suggests that the guidebooks' photograph has been altered.", "is_correct": False},
                {"text": "It advises visitors to see the bridge in the afternoon.", "is_correct": False},
                {"text": "It establishes that the bridge has changed since the photograph was taken.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>O'chirish sinovi</strong> (22-dars): jumlani olib "
                "tashlasak, oxirgi jumladagi izoh (<em>one hour of one kind of "
                "light</em>) <u>nimani</u> tushuntirayotgani noma'lum bo'lib "
                "qoladi.</p>"
                + why([
                    (True, "It gives the concrete case that the final sentence then explains",
                     "tanish bo'lmagan manzara — bu kuzatuv; oxirgi jumla esa "
                     "uning sababini aytadi. Jumlaning vazifasi shu "
                     "juftlikda."),
                    (False, "It establishes that the bridge has changed since the photograph was taken",
                     "<strong>matnga zid:</strong> <em>The bridge is the "
                     "same.</em>"),
                    (False, "It suggests that the guidebooks' photograph has been altered",
                     "<strong>yangi ma'lumot:</strong> tahrir yoki soxtalik "
                     "haqida hech nima yo'q — masala yorug'likda."),
                    (False, "It advises visitors to see the bridge in the afternoon",
                     "matn tavsiya bermaydi, va bu jumla ogohlantirish emas, "
                     "misol."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Cross-Text Connections") + cross_q(
                "<p>Folk songs collected in the nineteenth century were written down by "
                "editors who heard them sung. Where a singer's line did not scan, the "
                "editor mended it. The printed collections are therefore a record of what "
                "educated collectors thought a folk song ought to sound like.</p>",
                "<p>Wax-cylinder recordings made a generation later can be compared with "
                "printed texts of the same songs taken from the same villages. The "
                "recorded singers depart from regular metre constantly — and they depart "
                "in the same places from one village to the next, which is not what "
                "careless singing looks like.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the claim made in the last sentence of Text 1?"),
            "choices": [
                {"text": "By arguing that the irregularities the editors removed were themselves part of the tradition.", "is_correct": True},
                {"text": "By agreeing that the printed collections record the editors' taste rather than the singers'.", "is_correct": False},
                {"text": "By denying that nineteenth-century editors made any changes to what they heard.", "is_correct": False},
                {"text": "By claiming that wax-cylinder recordings are too poor in quality to be compared with printed texts.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi</strong> (31-dars) — Text 2 ning oxirgi "
                "jumlasi: <em>they depart in the same places from one village to "
                "the next, which is not what careless singing looks like</em>.</p>"
                "<p>Ya'ni notekislik <u>xato emas</u> — u naqsh, demak "
                "an'ananing bir qismi. Muharrirlar tuzatgan narsa aslida "
                "<mark>asl material</mark> edi.</p>"
                + why([
                    (True, "By arguing that the irregularities the editors removed were themselves part of the tradition",
                     "Text 2 ning dalili aynan shu xulosani ko'taradi: bir xil "
                     "joyda takrorlanadigan chetlanish tasodif emas."),
                    (False, "By agreeing that the printed collections record the editors' taste rather than the singers'",
                     "<strong>Text 1 ning fikrini takrorlaydi</strong> (32-dars). "
                     "Text 2 unga qarshi turmaydi, lekin shunchaki rozi ham "
                     "bo'lmaydi — u <u>yangi narsa</u> qo'shadi."),
                    (False, "By denying that nineteenth-century editors made any changes to what they heard",
                     "<strong>Text 2 ning dalili buni talab qilmaydi</strong> — "
                     "aksincha, uning butun mantiqi muharrirlar "
                     "o'zgartirgan degan taxminga tayanadi."),
                    (False, "By claiming that wax-cylinder recordings are too poor in quality to be compared with printed texts",
                     "Text 2 aynan o'sha yozuvlarga tayanadi — ularni rad "
                     "etish o'z dalilini yo'q qilardi."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Words in Context") + blank_q(
                "<p>A conductor rehearsing an unfamiliar orchestra spends the first hour "
                "not on the difficult passages but on a simple chord, played and replayed "
                "until the players are listening to one another rather than to him. The "
                "hour looks wasted to anyone watching the clock. What it buys is a "
                "habit that makes the remaining rehearsals "
                "<span class=\"sr-blank\"></span>: the difficult passages then take "
                "half the time they would otherwise have taken.</p>"),
            "choices": [
                {"text": "far quicker", "is_correct": True},
                {"text": "less frequent", "is_correct": False},
                {"text": "more enjoyable", "is_correct": False},
                {"text": "unnecessary", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki nuqta sovg'a qiladi</strong> (12-dars): "
                "<em>the difficult passages then take half the time</em>. "
                "Bo'sh joyning ma'nosi shundoq yozib qo'yilgan.</p>"
                + why([
                    (True, "far quicker",
                     "«yarim vaqt» — bu tezlik. Ikki nuqtadan keyingi izoh "
                     "boshqa hech qanday variantga to'g'ri kelmaydi."),
                    (False, "unnecessary",
                     "<strong>haddan tashqari kuchli:</strong> mashqlar tezroq "
                     "bo'ladi, lekin baribir kerak. Va bu matnning "
                     "mantiqini buzardi — birinchi soat aynan ular uchun "
                     "sarflangan."),
                    (False, "more enjoyable",
                     "zavq muhokama qilinmaydi, va u yarim vaqtni "
                     "tushuntirmaydi."),
                    (False, "less frequent",
                     "mashqlarning <u>soni</u> emas, ularning tezligi haqida "
                     "gap ketyapti. Ikki nuqtadan keyingi izohga mos "
                     "kelmaydi."),
                ])
                + TIP.format(
                    "Oltita savoldan to'rttasida javobni <strong>bo'sh joydan "
                    "keyingi yoki oldingi izoh</strong> berdi (ikki nuqta, "
                    "<em>because</em>, tire). Vaqt kam bo'lsa — birinchi "
                    "bo'lib shu belgilarni qidiring.")
            ),
        },

        {"rich_text": (
            "<h3>Natijangizni o'qing</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Natija</th><th>Ma'nosi</th></tr></thead>"
              "<tbody>"
              "<tr><td>6/6 yoki 5/6</td><td>Craft and Structure bo'yicha tayyorsiz — "
              "91-darsga o'ting.</td></tr>"
              "<tr><td>4/6</td><td>Yaxshi. Xato qilgan turingizning mavzusiga "
              "qayting (10–16, 20–24 yoki 30–33).</td></tr>"
              "<tr><td>3/6 yoki kamroq</td><td>Xatolar bitta turga yig'ilganmi? "
              "Deyarli har doim shunday bo'ladi. O'sha bitta mavzuni qayta "
              "o'qing — hammasini emas.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "Vaqt yetmagan bo'lsa, bu ham ma'lumot. Craft and Structure "
                "savollari imtihonda <u>eng tez</u> yechiladiganlardan: "
                "Words in Context ~40 soniya, Cross-Text ~90. Agar siz "
                "hammasiga bir xil vaqt sarflagan bo'lsangiz — muammo "
                "bilimda emas, taqsimotda.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">legible</div><div class="pp-card-back">o\'qish oson, tushunarli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a mean house (eski ma\'no)</div><div class="pp-card-back">oddiy, kamtarona uy</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a sightline</div><div class="pp-card-back">ko\'rish masofasi, ko\'rinish chizig\'i</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to scan (of a line)</div><div class="pp-card-back">(she\'r satri) vaznga tushmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to depart from ~</div><div class="pp-card-back">~ dan chetlashmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">shaded relief</div><div class="pp-card-back">soyali relyef (xaritada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a convention</div><div class="pp-card-back">qabul qilingan usul, an\'ana</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to mend a line</div><div class="pp-card-back">satrni tuzatmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Craft and Structure — uch tur, va savol matni turni "
              "<u>darrov</u> aytadi.</li>"
              "<li>Vaqtni turga qarab taqsimlang: Words in Context tez, "
              "Cross-Text sekin.</li>"
              "<li>Bo'sh joyli savolda birinchi bo'lib <strong>: ; —</strong> va "
              "<em>because</em> ni qidiring.</li>"
              "<li>Xatolar deyarli har doim <u>bitta</u> turga yig'iladi — "
              "shuni tuzating.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 91
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_MIX,
    "title": "SAT R&W 91: Mixed Module Practice 2 — Information and Ideas Under Time",
    "summary": "Information and Ideas domenining to'rt turi aralash: asosiy fikr, "
               "tafsilot, matndan va grafikdan dalil, mantiqiy xulosa.",
    "order": 91,
    "blocks": [
        {"rich_text": (
            "<h2>Ikkinchi guruh</h2>"
            "<p>90-dars Craft and Structure edi. Bu dars — "
            "<strong>Information and Ideas</strong>: matnning mazmuni bilan "
            "ishlaydigan guruh, imtihonning ~26 foizi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tur</th><th>Savol matni</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td>Central Ideas and Details</td>"
              "<td><em>…main idea…</em> / <em>According to the text…</em></td>"
              "<td>40–44</td></tr>"
              "<tr><td>Command of Evidence (Textual)</td>"
              "<td><em>Which quotation…</em> / <em>Which finding, if true…</em></td>"
              "<td>50–54</td></tr>"
              "<tr><td>Command of Evidence (Quantitative)</td>"
              "<td><em>…uses data from the table…</em></td><td>60–64</td></tr>"
              "<tr><td>Inferences</td>"
              "<td><em>…most logically completes the text?</em></td><td>70–74</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Qanday ishlash kerak:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>8 daqiqa</strong> — bu guruh birinchisidan "
                "sekinroq, ayniqsa jadvalli savol.</li>"
                "<li>To'xtamasdan yeching.</li>"
                "<li>Keyin tushuntirishlarni o'qing.</li>"
                "</ol>")
            + '<span class="sr-time">⏱ 6 savol · 8 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Central Ideas and Details") + q(
                "<p>A bicycle wheel stays upright not because of the spinning mass, as is "
                "usually said, but because of how the front fork is angled. Wheels built "
                "with counter-rotating discs, which cancel the spinning effect entirely, "
                "still balance and steer. Wheels with the fork angle reversed fall over "
                "at once, whatever the spin. The effect that gets the credit and the "
                "effect that does the work are not the same one.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "A bicycle's stability comes from the geometry of its steering rather than from the spin of its wheels.", "is_correct": True},
                {"text": "Wheels built with counter-rotating discs are able to balance and steer.", "is_correct": False},
                {"text": "The spinning mass of a bicycle wheel has no effect of any kind on the machine.", "is_correct": False},
                {"text": "Cyclists would ride more safely if they understood how their bicycles stay upright.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi, va u matnning "
                "butun shaklini bir gapda beradi: maqtov oladigan sabab bilan "
                "ish qiladigan sabab boshqa-boshqa.</p>"
                + why([
                    (True, "A bicycle's stability comes from the geometry of its steering rather than from the spin of its wheels",
                     "ikkala tomonni ham qamraydi (nima emas / nima), va ikkita "
                     "tajriba ham shu xulosaga xizmat qiladi."),
                    (False, "Wheels built with counter-rotating discs are able to balance and steer",
                     "<strong>doirasi tor:</strong> bu ikki dalildan biri, "
                     "xulosa emas (41-dars)."),
                    (False, "The spinning mass of a bicycle wheel has no effect of any kind on the machine",
                     "<strong>haddan tashqari kuchli:</strong> matn aylanish "
                     "muvozanatni <u>tushuntirmasligini</u> aytadi, hech qanday "
                     "ta'siri yo'qligini emas."),
                    (False, "Cyclists would ride more safely if they understood how their bicycles stay upright",
                     "<strong>matnda yo'q tavsiya.</strong>"),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Inferences") + inf_q(
                "<p>A species of ant farms a fungus and feeds it cut leaves. The fungus "
                "produces small nutrient-rich bodies that the ants eat, and it produces "
                "them only where ants are grazing. Fungi of the same genus growing "
                "without ants produce none. Since the bodies cost the fungus energy and "
                "are of no use to it, their production "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "appears to be a response to the presence of the ants rather than a normal feature of the fungus.", "is_correct": True},
                {"text": "shows that the fungus is unable to survive without the ants.", "is_correct": False},
                {"text": "explains why the ants prefer this fungus to others available to them.", "is_correct": False},
                {"text": "must have evolved before the ants began farming the fungus.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Faktlar:</strong> tanachalar faqat chumolilar "
                "yaylovlagan joyda ishlab chiqariladi; chumolisiz zamburug'lar "
                "ularni umuman qilmaydi; ular zamburug'ning o'ziga foydasiz.</p>"
                "<p>Uchtasi birga: ishlab chiqarish <mark>chumolining "
                "borligiga javob</mark>.</p>"
                + why([
                    (True, "appears to be a response to the presence of the ants rather than a normal feature of the fungus",
                     "uchala faktni ham ishlatadi va <em>appears to be</em> "
                     "bilan kuchni to'g'ri saqlaydi (73-dars)."),
                    (False, "shows that the fungus is unable to survive without the ants",
                     "<strong>matnga zid:</strong> chumolisiz zamburug'lar "
                     "<u>o'sib turibdi</u> — ular shunchaki tanacha "
                     "qilmaydi."),
                    (False, "must have evolved before the ants began farming the fungus",
                     "<strong>haddan tashqari kuchli</strong> va vaqt tartibi "
                     "matnda umuman yo'q."),
                    (False, "explains why the ants prefer this fungus to others available to them",
                     "<strong>yangi ma'lumot:</strong> chumolining tanlovi va "
                     "boshqa zamburug'lar muhokama qilinmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Command of Evidence — Quantitative") + data_q(
                "Loaves Sold and Loaves Unsold at Close of Trading, One Bakery",
                table(["Week", "Loaves baked", "Loaves unsold"],
                      [["Before change", "600", "96"],
                       ["After change", "450", "36"]]),
                "<p>A bakery cut the number of loaves it baked each week after its owner "
                "concluded that too many were going to waste. She reported afterwards "
                "that the change had reduced waste not only in total but as a share of "
                "what she produced: <span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "the unsold share fell from 16 percent of loaves baked to 8 percent.", "is_correct": True},
                {"text": "the number of unsold loaves fell from 96 to 36.", "is_correct": False},
                {"text": "the bakery baked 150 fewer loaves each week after the change.", "is_correct": False},
                {"text": "the unsold share rose from 8 percent of loaves baked to 16 percent.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit ibora:</strong> <em>not only in total but as a "
                "<u>share</u> of what she produced</em> — 60-darsning qoidasi: "
                "<mark>ulush kerak, xom son emas</mark>.</p>"
                "<p><strong>Hisob:</strong> avval 96 ÷ 600 = 0.16 = "
                "<strong>16%</strong>; keyin 36 ÷ 450 = 0.08 = "
                "<strong>8%</strong>.</p>"
                + why([
                    (True, "the unsold share fell from 16 percent of loaves baked to 8 percent",
                     "yagona variant ulushni beradi, va u da'voning aynan "
                     "isbotlanishi kerak bo'lgan qismi."),
                    (False, "the number of unsold loaves fell from 96 to 36",
                     "rost, lekin bu <u>jami</u> — matn buni "
                     "«<em>not only</em>» deb allaqachon tan olgan. Isbot "
                     "talab qiladigan qism — ulush."),
                    (False, "the bakery baked 150 fewer loaves each week after the change",
                     "rost (600 − 450), lekin bu isrof haqida emas, ishlab "
                     "chiqarish haqida."),
                    (False, "the unsold share rose from 8 percent of loaves baked to 16 percent",
                     "<strong>yo'nalish teskari</strong> (61-dars): ulush "
                     "tushgan, ko'tarilmagan."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Command of Evidence — Textual") + q(
                "<p>While studying a story about a man who has returned to sea after "
                "twenty years ashore, a student has written the following claim:</p>"
                "<p><em>Rashid discovers that the skill he expected to have lost is the "
                "one thing that has stayed with him.</em></p>",
                "Which quotation from the story most effectively illustrates the "
                "claim?"),
            "choices": [
                {"text": "“He could not remember the name of the second mate, nor which locker was his, but his hands found the knot before he had decided which knot it was.”", "is_correct": True},
                {"text": "“He had been twenty-three when he last stood a watch, and the ship had been a third the size of this one.”", "is_correct": False},
                {"text": "“The sea was rougher that first week than he had known it in all his years on the coast.”", "is_correct": False},
                {"text": "“He told nobody aboard how long it had been since he had sailed.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'voni bo'laklarga ajratamiz</strong> (51-dars): "
                "(1) yo'qotgan deb <u>kutgan</u> ko'nikma, (2) aslida "
                "<u>saqlanib qolgan</u>. Ikki bo'lak — demak iqtibosda "
                "ikkovi ham bo'lishi kerak.</p>"
                + why([
                    (True, "“He could not remember the name of the second mate, nor which locker was his, but his hands found the knot before he had decided which knot it was.”",
                     "ikkala bo'lak bitta jumlada: yo'qolgan narsalar "
                     "(ismlar, shkaf) va saqlangan narsa (qo'llar tugunni "
                     "o'zi topadi). <em>but</em> ikkovini bog'laydi."),
                    (False, "“He had been twenty-three when he last stood a watch, and the ship had been a third the size of this one.”",
                     "faqat fon: qancha vaqt o'tgani. Ko'nikma haqida hech "
                     "nima."),
                    (False, "“He told nobody aboard how long it had been since he had sailed.”",
                     "yashirish haqida — bu boshqa da'vo bo'lardi. Ko'nikmaning "
                     "saqlanishi ko'rinmaydi."),
                    (False, "“The sea was rougher that first week than he had known it in all his years on the coast.”",
                     "sharoit tavsifi. Rashidning qo'li nimani eslab qolgani "
                     "haqida emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Command of Evidence — Textual") + q(
                "<p>Glass eels arriving on a European coast each spring have crossed the "
                "Atlantic from a spawning area thousands of kilometres away. Numbers "
                "arriving have fallen sharply since the 1980s. Researchers proposed that "
                "the fall is caused by changes in the ocean current the larvae drift on, "
                "which would lengthen the crossing beyond what their energy reserves "
                "allow.</p>",
                "Which finding, if true, would most directly support the researchers' "
                "proposal?"),
            "choices": [
                {"text": "Larvae caught mid-ocean in recent years are lighter for their length than those caught in the 1980s.", "is_correct": True},
                {"text": "Eel populations in rivers along the coast have declined at the same rate as arrivals.", "is_correct": False},
                {"text": "Glass eels have been harvested commercially on several European coasts.", "is_correct": False},
                {"text": "The spawning area has been mapped more precisely than it had been in the 1980s.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Gipotezaning zanjiri</strong> (52-dars): oqim "
                "o'zgardi → suzish uzoqroq → energiya yetmaydi → kamroq "
                "yetib keladi. Kuchaytirish uchun <mark>o'rtadagi "
                "bo'g'inga</mark> tegish kerak.</p>"
                + why([
                    (True, "Larvae caught mid-ocean in recent years are lighter for their length than those caught in the 1980s",
                     "aynan energiya bo'g'ini: bugungi lichinkalar yo'lda "
                     "ko'proq zaxira sarflagan. Bu gipotezaning o'lchanadigan "
                     "bashorati."),
                    (False, "Eel populations in rivers along the coast have declined at the same rate as arrivals",
                     "<strong>TEGMAYDI</strong> (53-dars): daryodagi pasayish "
                     "kelganlar sonining oqibati bo'lishi mumkin — u sababni "
                     "ajratmaydi."),
                    (False, "Glass eels have been harvested commercially on several European coasts",
                     "<strong>raqib tushuntirish</strong> — ovlash "
                     "pasayishning boshqa sababi bo'lardi, ya'ni gipotezani "
                     "kuchsizlantiradi."),
                    (False, "The spawning area has been mapped more precisely than it had been in the 1980s",
                     "<strong>TEGMAYDI:</strong> bilimimizning yaxshilanishi "
                     "lichinkalarning holatiga ta'sir qilmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Central Ideas and Details") + q(
                "<p>The reading room's rule against bringing in bags was introduced to "
                "prevent theft, and the manuscripts have not been stolen since. Readers "
                "now carry their notes in loose sheets, and the librarians report that "
                "loose sheets are left behind, mixed into volumes and occasionally "
                "shelved inside them. Nothing has been taken from the collection; things "
                "have been added to it.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "A rule succeeded at what it was designed to stop and created a different problem in its place.", "is_correct": True},
                {"text": "Manuscripts have not been stolen from the reading room since the rule was introduced.", "is_correct": False},
                {"text": "The rule against bags should be withdrawn so that readers may carry notebooks.", "is_correct": False},
                {"text": "Librarians are unable to keep the collection in good order.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'vo jumlasi</strong> — oxirgisi, va u qisqa "
                "hamda g'alati: <em>Nothing has been taken from the collection; "
                "things have been added to it.</em> Bu 43-darsdagi qoida — "
                "qisqa va g'alati oxirgi jumla deyarli har doim "
                "javobdir.</p>"
                + why([
                    (True, "A rule succeeded at what it was designed to stop and created a different problem in its place",
                     "ikkala tomonni ham oladi: o'g'rilik to'xtadi, lekin "
                     "yangi tartibsizlik paydo bo'ldi."),
                    (False, "Manuscripts have not been stolen from the reading room since the rule was introduced",
                     "<strong>doirasi tor:</strong> bu birinchi yarmi, va "
                     "matn undan keyin boshlanadi."),
                    (False, "The rule against bags should be withdrawn so that readers may carry notebooks",
                     "<strong>matnda yo'q tavsiya</strong> (41-dars)."),
                    (False, "Librarians are unable to keep the collection in good order",
                     "<strong>ayblov, matnda yo'q:</strong> kutubxonachilar "
                     "muammoni <u>xabar qilyapti</u>, ya'ni ular uni "
                     "ko'rmoqda."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Natijangizni o'qing</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Qaysi savolda xato</th><th>Qaysi mavzuga qaytish</th></tr></thead>"
              "<tbody>"
              "<tr><td>1 yoki 6 (asosiy fikr)</td><td>40–41: da'vo jumlasini "
              "topish, uch noto'g'ri shakl</td></tr>"
              "<tr><td>2 (xulosa)</td><td>72–73: barmoq sinovi va kuch "
              "shkalasi</td></tr>"
              "<tr><td>3 (jadval)</td><td>60: son ≠ ulush</td></tr>"
              "<tr><td>4 (iqtibos)</td><td>51: da'vodagi shart so'zlari = "
              "bo'laklar soni</td></tr>"
              "<tr><td>5 (topilma)</td><td>52–53: zanjir va uch qutiga "
              "saralash</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu ikki dars (90 va 91) birgalikda o'n ikki savol berdi — "
                "imtihondagi yarim modulning deyarli yarmi. 92-darsda "
                "to'liq yarim modulni (13 savol) bir o'tirishda yechasiz.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to get the credit</div><div class="pp-card-back">maqtovni olmoq (aslida boshqasi ish qilsa ham)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">counter-rotating</div><div class="pp-card-back">qarama-qarshi aylanuvchi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to graze</div><div class="pp-card-back">o\'tlamoq, terib yemoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">energy reserves</div><div class="pp-card-back">energiya zaxirasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to drift on a current</div><div class="pp-card-back">oqim bilan suzib bormoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a share of ~</div><div class="pp-card-back">~ ning ulushi (foizda)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to stand a watch</div><div class="pp-card-back">navbatchilikda turmoq (kemada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">in its place</div><div class="pp-card-back">uning o\'rniga</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Information and Ideas — to'rt tur, va ular Craft and "
              "Structure'dan <u>sekinroq</u>.</li>"
              "<li>Asosiy fikrda: <strong>da'vo jumlasi odatda oxirida</strong>, "
              "ayniqsa u qisqa va g'alati bo'lsa.</li>"
              "<li>Jadvalda: da'voda <em>share · rate</em> bo'lsa — "
              "<strong>bo'linma</strong>.</li>"
              "<li>Topilma savolida: gipotezaning <u>zanjirini</u> ayting, keyin "
              "o'rtadagi bo'g'inni qidiring.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 92
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_MIX,
    "title": "SAT R&W 92: A Full Reading Half-Module — 13 Questions Under Time",
    "summary": "To'liq yarim modul: 13 savol, imtihon tartibida (Craft and Structure "
               "→ Information and Ideas), qiyinlik ortib boradi, 15 daqiqa.",
    "order": 92,
    "blocks": [
        {"rich_text": (
            "<h2>To'liq yarim modul</h2>"
            "<p>Haqiqiy modulda 27 ta savol bor: taxminan 13 tasi o'qish "
            "domenlaridan (Craft and Structure va Information and Ideas), qolgani "
            "grammatika va uslub. Bu dars — <mark>o'sha o'qish yarmi, "
            "to'liq</mark>.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savollar</th><th>Domen</th></tr></thead>"
              "<tbody>"
              "<tr><td>1–5</td><td>Craft and Structure</td></tr>"
              "<tr><td>6–13</td><td>Information and Ideas</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<p>Har guruh ichida savollar <u>oson → qiyin</u> tartibida. "
            "Bu imtihondagi haqiqiy tartib, va uni sezish o'zi bir "
            "ko'nikma: guruh boshida tezlashing, oxirida sekinlashing.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Shartlar — jiddiy "
                "bajaring:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li>Taymer: <strong>15 daqiqa</strong>. 13 savol × ~70 "
                "soniya.</li>"
                "<li>To'xtamasdan, boshidan oxirigacha. Telefon boshqa "
                "oynada emas.</li>"
                "<li>Bilmagan savolga ham <u>javob belgilang</u> — imtihonda "
                "bo'sh katak 0 ball.</li>"
                "<li>Vaqt tugagach to'xtang, keyin tushuntirishlarni "
                "o'qing.</li>"
                "</ol>")
            + WARN.format(
                "Bu darsni <u>bo'lib-bo'lib</u> yechish uni mashqdan "
                "chiqaradi. 15 daqiqa uzluksiz vaqtingiz bo'lmasa, keyinroq "
                "qayting — natija shundagina haqiqiy ma'lumot beradi.")
            + '<span class="sr-time">⏱ 13 savol · 15 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Words in Context") + blank_q(
                "<p>The workshop that made the town's clock in 1690 also made its "
                "weathervane, its bell frame and the iron gates of the church. Nothing in "
                "the accounts distinguishes one commission from another; all are entered "
                "as work in iron, at rates that vary with the weight of metal and not "
                "with the difficulty of the job. To the men who paid for them, the clock "
                "and the gates were <span class=\"sr-blank\"></span> kinds of work.</p>"),
            "choices": [
                {"text": "equivalent", "is_correct": True},
                {"text": "unfamiliar", "is_correct": False},
                {"text": "competing", "is_correct": False},
                {"text": "decorative", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikkinchi jumla javobni beradi: <em>Nothing … distinguishes "
                "one commission from another</em>, va narx og'irlik bilan "
                "belgilanadi, murakkablik bilan emas. Ya'ni ular "
                "<mark>bir xil toifadagi</mark> ish.</p>"
                + why([
                    (True, "equivalent",
                     "«teng qiymatli, bir xil» — <em>Nothing distinguishes</em> "
                     "ning aynan natijasi."),
                    (False, "competing",
                     "ustaxona ikkovini ham o'zi qilgan — raqobat yo'q."),
                    (False, "unfamiliar",
                     "buyurtmalar odatiy edi; notanishlik haqida hech nima "
                     "yo'q."),
                    (False, "decorative",
                     "soat bezak emas, va matn bezaklilik haqida "
                     "gapirmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Words in Context") + means_q(
                "<p>The engineer's report on the bridge is four pages long and contains "
                "no recommendation. It <span class=\"sr-focus\">rehearses</span> the "
                "history of the crossing, lists the loads the deck has carried since "
                "1954, and stops. The council that commissioned it had asked whether the "
                "bridge should be closed.</p>", "rehearses"),
            "choices": [
                {"text": "recounts", "is_correct": True},
                {"text": "practises", "is_correct": False},
                {"text": "questions", "is_correct": False},
                {"text": "shortens", "is_correct": False},
            ],
            "explanation": (
                "<p><em>rehearses the history … lists the loads</em> — ikki fe'l "
                "juftlashib turibdi, va ikkinchisi («sanaydi») birinchisining "
                "ma'nosini ochadi: hisobot faktlarni "
                "<mark>bayon qiladi</mark>.</p>"
                + why([
                    (True, "recounts",
                     "«bayon qilmoq, so'zlab bermoq» — <em>rehearse</em> ning "
                     "kitobiy ma'nosi, va <em>lists</em> bilan bir qatorda "
                     "turadi."),
                    (False, "practises",
                     "eng mashhur ma'no (repetitsiya), shuning uchun eng "
                     "kuchli tuzoq. Lekin hisobot tarixni «mashq "
                     "qilolmaydi»."),
                    (False, "questions",
                     "matn hisobotda <u>hech qanday</u> baho yo'qligini "
                     "aytadi — shubha ham baho bo'lardi."),
                    (False, "shortens",
                     "qisqartirish emas: hisobot to'rt sahifa va "
                     "batafsil."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Text Structure and Purpose") + q(
                "<p>Museums label a fossil with the place it was found, and visitors read "
                "the label as though it named the animal's home. Most fossils formed "
                "where a carcass came to rest, which for a river system may be many "
                "kilometres downstream of where the animal lived and in a habitat it "
                "never entered. The label is accurate about the rock and silent about "
                "the animal.</p>",
                "Which choice best describes the overall structure of the text?"),
            "choices": [
                {"text": "It identifies a common misreading, explains why it is mistaken, and states what the label actually reports.", "is_correct": True},
                {"text": "It argues that museums should change the wording of their fossil labels.", "is_correct": False},
                {"text": "It describes the process by which a carcass becomes a fossil.", "is_correct": False},
                {"text": "It compares fossils found in rivers with fossils found elsewhere.", "is_correct": False},
            ],
            "explanation": (
                "<p>Uch jumla, uch harakat: noto'g'ri o'qish → nega noto'g'ri "
                "→ yorliq aslida nima haqida.</p>"
                + why([
                    (True, "It identifies a common misreading, explains why it is mistaken, and states what the label actually reports",
                     "uchala harakat, to'g'ri tartibda. Oxirgi jumla "
                     "(<em>accurate about the rock and silent about the "
                     "animal</em>) uchinchisining aniq isboti."),
                    (False, "It argues that museums should change the wording of their fossil labels",
                     "<strong>tavsiya yo'q</strong> — matn yorliqni "
                     "<u>noto'g'ri</u> ham demaydi, u <em>accurate</em> "
                     "deydi."),
                    (False, "It describes the process by which a carcass becomes a fossil",
                     "<strong>doirasi tor:</strong> jarayon bir bo'lakda, "
                     "izoh sifatida."),
                    (False, "It compares fossils found in rivers with fossils found elsewhere",
                     "daryo faqat misol; taqqoslash yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Text Structure and Purpose") + q(
                "<p>The choir had sung the piece for thirty years and knew it too well. "
                "At the first rehearsal the new director handed out a version with the "
                "bar lines removed. <span class=\"sr-focus\">Half the singers could not "
                "begin at all, and those who could sang more slowly than they ever had "
                "with the bars in place.</span> By the third week they were phrasing the "
                "line by its words rather than by its beats, which was what he had "
                "wanted.</p>",
                "What is the main purpose of the underlined sentence?"),
            "choices": [
                {"text": "It records the immediate difficulty that the director's method produced before it worked.", "is_correct": True},
                {"text": "It suggests that the choir's singers lacked the training to read music.", "is_correct": False},
                {"text": "It shows that the director's method had failed and was abandoned.", "is_correct": False},
                {"text": "It explains why the choir had sung the piece for thirty years.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>O'chirish sinovi:</strong> jumlani olib tashlasak, "
                "<em>By the third week</em> nimadan keyin ekani yo'qoladi — "
                "va usulning <u>og'ir boshlangani</u> ko'rinmaydi.</p>"
                + why([
                    (True, "It records the immediate difficulty that the director's method produced before it worked",
                     "<em>By the third week … which was what he had wanted</em> "
                     "bilan juftlashadi: avval qiyinchilik, keyin natija."),
                    (False, "It shows that the director's method had failed and was abandoned",
                     "<strong>matnga zid:</strong> uchinchi haftada usul "
                     "ishladi."),
                    (False, "It suggests that the choir's singers lacked the training to read music",
                     "<strong>ayblov, matnda yo'q:</strong> ular o'ttiz yil "
                     "kuylagan — muammo mahoratda emas, odatda."),
                    (False, "It explains why the choir had sung the piece for thirty years",
                     "sabab-oqibat teskari: bu jumla o'ttiz yildan "
                     "<u>keyingi</u> voqea."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Cross-Text Connections") + cross_q(
                "<p>Anonymous medieval building accounts rarely name a designer, and "
                "historians have taken this to mean that the master mason of a cathedral "
                "was regarded as a craftsman among others rather than as an author of the "
                "work.</p>",
                "<p>The accounts name nobody at all — not the glazier, not the carpenter, "
                "not the man who supplied the lead. They are records of payment, kept for "
                "auditors, and a name appears in them only where a debt had to be chased. "
                "Silence in such a document is evidence about the document.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the inference drawn in Text 1?"),
            "choices": [
                {"text": "By pointing out that the absence of names reflects the kind of record being kept rather than how masons were regarded.", "is_correct": True},
                {"text": "By arguing that master masons were in fact regarded as authors of the buildings they designed.", "is_correct": False},
                {"text": "By denying that medieval building accounts have survived in sufficient numbers to study.", "is_correct": False},
                {"text": "By agreeing that the master mason was one craftsman among many.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Tegish nuqtasi</strong> — Text 2 ning oxirgi jumlasi: "
                "<em>Silence in such a document is evidence about the "
                "document.</em> Ya'ni sukut hisobotning <u>turi</u> haqida "
                "gapiradi, ustalarning maqomi haqida emas.</p>"
                + why([
                    (True, "By pointing out that the absence of names reflects the kind of record being kept rather than how masons were regarded",
                     "Text 2 ning butun dalili shu: hech kim nomlanmagan, "
                     "chunki bu to'lov daftari."),
                    (False, "By arguing that master masons were in fact regarded as authors of the buildings they designed",
                     "<strong>matndan kuchliroq:</strong> Text 2 teskarisini "
                     "isbotlamaydi — u faqat Text 1 ning dalilini "
                     "yaroqsiz qiladi. Dalil yo'qolgani teskari xulosani "
                     "bermaydi."),
                    (False, "By agreeing that the master mason was one craftsman among many",
                     "bu <strong>Text 1 ning xulosasi</strong> — Text 2 unga "
                     "qarshi turibdi."),
                    (False, "By denying that medieval building accounts have survived in sufficient numbers to study",
                     "Text 2 aynan o'sha hisobotlarni o'qib chiqqan."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Central Ideas and Details") + q(
                "<p>Bees returning to a hive perform a movement whose angle encodes the "
                "direction of a food source. The angle is measured against gravity inside "
                "the dark hive and read by the watching bees as an angle against the sun "
                "outside. Since the sun moves, a dance performed an hour after the "
                "forager returned would send its audience to the wrong place — and a bee "
                "kept waiting adjusts the angle as it waits.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "The dance translates between two frames of reference, and the dancer corrects for the time that has passed.", "is_correct": True},
                {"text": "Bees measure the angle of their dance against gravity rather than against the sun.", "is_correct": False},
                {"text": "A bee kept waiting inside the hive will send other bees to the wrong place.", "is_correct": False},
                {"text": "The sun's movement across the sky makes navigation difficult for insects generally.", "is_correct": False},
            ],
            "explanation": (
                "<p>Matn ikki narsa quradi: (1) burchak <u>ikki tizim</u> "
                "orasida o'giriladi (tortishish ↔ quyosh); (2) vaqt o'tsa, "
                "raqqosa <u>tuzatish kiritadi</u>. Asosiy fikr ikkovini ham "
                "olishi kerak.</p>"
                + why([
                    (True, "The dance translates between two frames of reference, and the dancer corrects for the time that has passed",
                     "ikkala qismni ham qamraydi, va oxirgi bo'lak "
                     "(<em>adjusts the angle as it waits</em>) ikkinchisining "
                     "isboti."),
                    (False, "Bees measure the angle of their dance against gravity rather than against the sun",
                     "<strong>yarim to'g'ri va yarim noto'g'ri:</strong> "
                     "ikkovi ham ishlatiladi — ichkarida tortishish, "
                     "tashqarida quyosh. <em>rather than</em> buni buzadi."),
                    (False, "A bee kept waiting inside the hive will send other bees to the wrong place",
                     "<strong>matnga zid:</strong> kutgan asalari burchakni "
                     "<u>tuzatadi</u>, shuning uchun adashtirmaydi."),
                    (False, "The sun's movement across the sky makes navigation difficult for insects generally",
                     "<strong>doirasi juda keng:</strong> boshqa hasharotlar "
                     "muhokama qilinmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(7, "Central Ideas and Details") + q(
                "<p>Feruza had planned the argument on the way over and delivered it at "
                "the door, and her brother heard it out without interrupting, which she "
                "had not expected and had no answer for. When he finally said that she "
                "was probably right, she found she was still holding the second half of "
                "what she had prepared, and that she was not going to be able to put it "
                "down.</p>",
                "Which choice best states the main idea of the text?"),
            "choices": [
                {"text": "Feruza wins the argument and finds that winning has left her with no way to stop.", "is_correct": True},
                {"text": "Feruza's brother refuses to engage with the argument she has prepared.", "is_correct": False},
                {"text": "Feruza realises that her argument was weaker than she had believed.", "is_correct": False},
                {"text": "Feruza and her brother have a long history of disagreement.", "is_correct": False},
            ],
            "explanation": (
                "<p>Adabiy parcha — «<strong>Nima o'zgardi?</strong>» (43-dars). "
                "Tashqarida: u yutdi. Ichkarida: tayyorgarligining yarmi "
                "qo'lida qolib ketdi va u to'xtay olmaydi.</p>"
                + why([
                    (True, "Feruza wins the argument and finds that winning has left her with no way to stop",
                     "ikkala qismni ham oladi: <em>you are probably right</em> "
                     "(g'alaba) va <em>not going to be able to put it down</em> "
                     "(to'xtay olmaslik)."),
                    (False, "Feruza's brother refuses to engage with the argument she has prepared",
                     "<strong>matnga zid:</strong> u oxirigacha tingladi va "
                     "rozi bo'ldi."),
                    (False, "Feruza realises that her argument was weaker than she had believed",
                     "<strong>yangi ma'lumot:</strong> dalilning kuchi "
                     "muhokama qilinmaydi — u yutdi."),
                    (False, "Feruza and her brother have a long history of disagreement",
                     "<strong>fon to'qish:</strong> matn bitta suhbat haqida."),
                ])
            ),
        },

        {
            "rich_text": qnum(8, "Central Ideas and Details") + q(
                "<p>A survey of household water use fitted meters to individual taps in "
                "forty homes for a year. The largest single use was not bathing, cooking "
                "or laundry but the cold tap at the kitchen sink, run while waiting for "
                "the water to reach drinking temperature. Households with a chilled tap "
                "or a jug in the refrigerator used, on average, a fifth less water in "
                "total than those without.</p>",
                "According to the text, what accounted for the largest single share of "
                "household water use?"),
            "choices": [
                {"text": "Water run from the kitchen cold tap while it cooled.", "is_correct": True},
                {"text": "Water used for laundry.", "is_correct": False},
                {"text": "Water used for bathing.", "is_correct": False},
                {"text": "Water stored in refrigerator jugs.", "is_correct": False},
            ],
            "explanation": (
                "<p>Tafsilot savoli — matnga qayting (42-dars). "
                "<em>The largest single use was <u>not</u> bathing, cooking or "
                "laundry <u>but</u> the cold tap</em>.</p>"
                + why([
                    (True, "Water run from the kitchen cold tap while it cooled",
                     "so'zma-so'z: <em>not … but the cold tap at the kitchen "
                     "sink, run while waiting</em>."),
                    (False, "Water used for bathing",
                     "matn buni <u>ataylab</u> istisno qiladi — <em>not "
                     "bathing</em>. <em>not … but</em> qurilishining birinchi "
                     "yarmini o'qib to'xtagan o'quvchi shuni tanlaydi."),
                    (False, "Water used for laundry",
                     "yana istisno qilinganlar ro'yxatidan."),
                    (False, "Water stored in refrigerator jugs",
                     "ko'za — <u>yechim</u>, sarf emas: unga ega uylar kamroq "
                     "suv ishlatgan."),
                ])
            ),
        },

        {
            "rich_text": qnum(9, "Command of Evidence — Textual") + q(
                "<p>While studying a story about a woman who has taken over her mother's "
                "seed business, a student has written the following claim:</p>"
                "<p><em>Zebo keeps her mother's methods not because she believes in them "
                "but because she has not yet found the moment to change them.</em></p>",
                "Which quotation from the story most effectively illustrates the "
                "claim?"),
            "choices": [
                {"text": "“She sorted the seed by hand, as her mother had, and thought each spring that next year she would buy the machine, and each spring the sorting was finished before she had ordered it.”", "is_correct": True},
                {"text": "“Her mother had run the business for thirty-one years and had never once bought on credit.”", "is_correct": False},
                {"text": "“She told the buyer from the cooperative that hand-sorted seed was cleaner, and she believed it.”", "is_correct": False},
                {"text": "“The machine she had been considering cost more than the business earned in a season.”", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Da'voning shart so'zi:</strong> <em>not because … "
                "but because</em> — ikki bo'lak (51-dars). Iqtibosda ishonch "
                "<u>yo'qligi</u> va o'zgartirish <u>kechikayotgani</u> ikkovi "
                "ham ko'rinishi kerak.</p>"
                + why([
                    (True, "“She sorted the seed by hand, as her mother had, and thought each spring that next year she would buy the machine, and each spring the sorting was finished before she had ordered it.”",
                     "ikkala bo'lak: mashina olmoqchi (ishonmaydi) va har bahor "
                     "ulgurmaydi (moment topilmaydi)."),
                    (False, "“She told the buyer from the cooperative that hand-sorted seed was cleaner, and she believed it.”",
                     "<strong>to'g'ridan-to'g'ri teskari:</strong> "
                     "<em>and she believed it</em> — da'vo aynan ishonmasligini "
                     "aytadi."),
                    (False, "“The machine she had been considering cost more than the business earned in a season.”",
                     "<u>boshqa</u> sabab beradi — pul. Da'vo esa sababni "
                     "«moment topilmagani» deb aytadi."),
                    (False, "“Her mother had run the business for thirty-one years and had never once bought on credit.”",
                     "onaning tavsifi; Zeboning sababi haqida hech nima."),
                ])
            ),
        },

        {
            "rich_text": qnum(10, "Command of Evidence — Textual") + q(
                "<p>Soils under old hedgerows hold more carbon per cubic metre than soils "
                "in the middle of the same fields. Researchers proposed that the "
                "difference is built up by the hedge itself — by roots and leaf litter "
                "adding carbon year after year — rather than reflecting ground that was "
                "always richer and was left as hedge for that reason.</p>",
                "Which finding, if true, would most directly support the researchers' "
                "proposal?"),
            "choices": [
                {"text": "In fields where a hedge was planted forty years ago on ground previously ploughed, soil carbon under the hedge now exceeds that of the field.", "is_correct": True},
                {"text": "Soil carbon under hedgerows varies with the species of shrub the hedge is made of.", "is_correct": False},
                {"text": "Hedgerows support a greater number of insect species than open field margins.", "is_correct": False},
                {"text": "Fields with hedgerows on all four sides hold more carbon overall than fields with none.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki raqib tushuntirish:</strong> (1) to'siq "
                "uglerodni <u>to'playdi</u>; (2) yer allaqachon boy edi, "
                "shuning uchun to'siq qoldirilgan. Kuchaytiruvchi topilma "
                "ikkovini <mark>ajratishi</mark> kerak.</p>"
                + why([
                    (True, "In fields where a hedge was planted forty years ago on ground previously ploughed, soil carbon under the hedge now exceeds that of the field",
                     "ajratuvchi tajriba: boshlang'ich yer <u>bir xil</u> edi "
                     "(haydalgan), va farq keyin paydo bo'ldi. Ikkinchi "
                     "tushuntirish chetlashtirildi."),
                    (False, "Fields with hedgerows on all four sides hold more carbon overall than fields with none",
                     "<strong>TEGMAYDI:</strong> ikkala tushuntirishga ham mos "
                     "keladi — boy yerlarda ko'proq to'siq qolgan bo'lishi "
                     "mumkin."),
                    (False, "Soil carbon under hedgerows varies with the species of shrub the hedge is made of",
                     "qiziq, lekin bu <u>to'siqlar orasidagi</u> farq — "
                     "to'siq va dala orasidagi farqning sababini "
                     "ajratmaydi."),
                    (False, "Hedgerows support a greater number of insect species than open field margins",
                     "<strong>TEGMAYDI:</strong> hasharotlar uglerod "
                     "manbasining savoliga aloqasiz."),
                ])
            ),
        },

        {
            "rich_text": qnum(11, "Command of Evidence — Quantitative") + data_q(
                "Nesting Attempts and Successful Fledgings in Two Woodlands",
                table(["Woodland", "Nesting attempts", "Attempts producing fledglings"],
                      [["Fenced (deer excluded)", "240", "144"],
                       ["Unfenced", "180", "72"]]),
                "<p>Deer browse the low shrubs in which several woodland birds nest. One "
                "woodland was fenced to keep deer out; a neighbouring one was left open. "
                "The survey team reported that fencing had improved not just the number "
                "of successful nests but the proportion of attempts that succeeded: "
                "<span class=\"sr-blank\"></span></p>",
                "Which choice most effectively uses data from the table to complete the "
                "text?"),
            "choices": [
                {"text": "60 percent of attempts in the fenced woodland produced fledglings, against 40 percent in the unfenced one.", "is_correct": True},
                {"text": "144 attempts in the fenced woodland produced fledglings, exactly twice the 72 in the unfenced one.", "is_correct": False},
                {"text": "the fenced woodland recorded 240 nesting attempts, more than the 180 recorded in the unfenced one.", "is_correct": False},
                {"text": "40 percent of attempts in the fenced woodland produced fledglings, against 60 percent in the unfenced one.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kalit ibora:</strong> <em>not just the number … but "
                "the <u>proportion</u></em> — ulush so'ralyapti (60-dars).</p>"
                "<p><strong>Hisob:</strong> to'siqli 144 ÷ 240 = 0.60 = "
                "<strong>60%</strong>; to'siqsiz 72 ÷ 180 = 0.40 = "
                "<strong>40%</strong>.</p>"
                + why([
                    (True, "60 percent of attempts in the fenced woodland produced fledglings, against 40 percent in the unfenced one",
                     "yagona variant ulushni beradi va tartibi ham to'g'ri."),
                    (False, "144 attempts in the fenced woodland produced fledglings, exactly twice the 72 in the unfenced one",
                     "rost (144 = 2 × 72), lekin bu <u>son</u> — matn buni "
                     "«<em>not just the number</em>» deb allaqachon tan olgan."),
                    (False, "the fenced woodland recorded 240 nesting attempts, more than the 180 recorded in the unfenced one",
                     "urinishlar soni muvaffaqiyat ulushini ko'rsatmaydi."),
                    (False, "40 percent of attempts in the fenced woodland produced fledglings, against 60 percent in the unfenced one",
                     "<strong>ulushlar almashtirilgan</strong> — usul to'g'ri, "
                     "natija teskari."),
                ])
            ),
        },

        {
            "rich_text": qnum(12, "Inferences") + inf_q(
                "<p>A library digitised its card catalogue and kept the cards. Within a "
                "year the staff had returned to the cards for one purpose: the cards carry "
                "pencil annotations, added by librarians over decades, recording which "
                "books were asked for together. The database holds every field the cards "
                "held. What it does not hold is <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "the informal record that was never part of the catalogue's official contents.", "is_correct": True},
                {"text": "the full bibliographic description of each book in the collection.", "is_correct": False},
                {"text": "any information about which books the library owns.", "is_correct": False},
                {"text": "a record of how often each book has been borrowed.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Matn o'zi chegara qo'yadi:</strong> <em>The database "
                "holds <u>every field the cards held</u></em>. Demak yo'qolgan "
                "narsa maydonlarda emas — u <mark>qalam bilan qo'shilgan "
                "yozuvlar</mark>, ya'ni rasmiy katalogning qismi "
                "bo'lmagan.</p>"
                + why([
                    (True, "the informal record that was never part of the catalogue's official contents",
                     "qalam yozuvlari aynan shunday: rasmiy maydon emas, "
                     "lekin kutubxonachilar uchun qimmatli."),
                    (False, "the full bibliographic description of each book in the collection",
                     "<strong>matnga zid:</strong> ma'lumotlar bazasi hamma "
                     "maydonni saqlaydi."),
                    (False, "any information about which books the library owns",
                     "yana matnga zid, va haddan tashqari kuchli."),
                    (False, "a record of how often each book has been borrowed",
                     "<strong>yaqin, lekin noto'g'ri:</strong> yozuvlar "
                     "kitoblarning <u>birga</u> so'ralganini qayd etadi, "
                     "har birining <u>necha marta</u> olinganini emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(13, "Inferences") + inf_q(
                "<p>Two clocks of the same design, one kept at sea level and one carried "
                "to the top of a mountain, disagree by a few billionths of a second a day, "
                "the higher clock running faster. The disagreement is the same whichever "
                "pair of clocks is used and whichever mountain, and it matches in size "
                "what the theory predicts for that difference in altitude. Since the "
                "clocks are identical and the effect follows the height rather than the "
                "instrument, the difference <span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "is a property of the conditions the clocks are in rather than of the clocks themselves.", "is_correct": True},
                {"text": "shows that clocks of this design become less accurate at altitude.", "is_correct": False},
                {"text": "could be removed by calibrating the higher clock before each measurement.", "is_correct": False},
                {"text": "proves that time passes at a constant rate everywhere on Earth.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chetlashtirish:</strong> soatlar bir xil "
                "(<em>identical</em>), har juftlikda va har tog'da bir xil "
                "natija. Demak sabab asbobda emas — u "
                "<mark>balandlikda</mark>.</p>"
                + why([
                    (True, "is a property of the conditions the clocks are in rather than of the clocks themselves",
                     "matnning oxirgi jumlasi buni deyarli aytib beradi: "
                     "<em>follows the height rather than the instrument</em>."),
                    (False, "shows that clocks of this design become less accurate at altitude",
                     "<strong>«aniqlik» noto'g'ri so'z:</strong> ikkala soat ham "
                     "to'g'ri ishlayapti — nazariya bashorat qilgan farqni "
                     "ko'rsatyapti. Nosozlik emas."),
                    (False, "could be removed by calibrating the higher clock before each measurement",
                     "<strong>yangi ma'lumot:</strong> kalibrlash muhokama "
                     "qilinmaydi, va farq baribir qayta paydo bo'lardi."),
                    (False, "proves that time passes at a constant rate everywhere on Earth",
                     "<strong>to'g'ridan-to'g'ri teskari</strong> — va "
                     "<em>proves</em> ham haddan tashqari kuchli (73-dars)."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Natijangizni o'qing</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>To'g'ri</th><th>Ma'nosi</th></tr></thead>"
              "<tbody>"
              "<tr><td>12–13</td><td>O'qish yarmi bo'yicha tayyorsiz. Endi "
              "<strong>writing</strong> yarmiga o'ting.</td></tr>"
              "<tr><td>10–11</td><td>Kuchli daraja. Xatolaringizni 93-darsdagi "
              "to'rt sabab bo'yicha ajrating.</td></tr>"
              "<tr><td>7–9</td><td>Asos bor. Xatolar odatda ikki turga "
              "yig'iladi — o'sha ikki mavzuni qayta o'qing.</td></tr>"
              "<tr><td>6 va kamroq</td><td>Vaqt yetmadimi yoki tur "
              "tanilmadimi? 93-dars aynan shu farqni ajratishga "
              "o'rgatadi.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "<strong>Vaqtni ham yozib qo'ying.</strong> 15 daqiqada "
                "ulgurmagan bo'lsangiz, nechta savol qolgani — ballning o'zi "
                "kabi muhim ma'lumot. Imtihonda ulgurmaslik bilmaslik bilan "
                "bir xil natija beradi, lekin butunlay boshqa yechimni talab "
                "qiladi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a commission (of work)</div><div class="pp-card-back">buyurtma (ish)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to rehearse (facts)</div><div class="pp-card-back">(faktlarni) bayon qilmoq, sanab bermoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a frame of reference</div><div class="pp-card-back">sanoq tizimi, o\'lchov asosi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">leaf litter</div><div class="pp-card-back">to\'kilgan barglar qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fledge / a fledgling</div><div class="pp-card-back">uchishga tayyor bo\'lmoq / uchar jo\'ja</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an annotation</div><div class="pp-card-back">chetga yozilgan izoh</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to browse (of deer)</div><div class="pp-card-back">(kiyik) shox-barg yemoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a bar line (music)</div><div class="pp-card-back">takt chizig\'i (notada)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Yarim modul: <strong>5 ta Craft and Structure + 8 ta "
              "Information and Ideas</strong>, har guruh ichida oson → "
              "qiyin.</li>"
              "<li>Guruh boshida <u>tezlashing</u>, oxirida "
              "<u>sekinlashing</u>.</li>"
              "<li>Ball bilan birga <strong>vaqtni ham</strong> yozib qo'ying — "
              "ular boshqa-boshqa muammolarni ko'rsatadi.</li>"
              "<li>Keyingi dars xatolarni to'rt sababga ajratadi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Lesson 93
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "reading",
    "topic": TOPIC_MIX,
    "title": "SAT R&W 93: Diagnosing Your Own Mistakes — The Four Reasons You Missed It",
    "summary": "Xato qilish yetarli emas — nega xato qilganingizni bilish kerak. "
               "To'rt sabab, to'rt xil yechim, va xato daftari.",
    "order": 93,
    "blocks": [
        {"rich_text": (
            "<h2>«Xato qildim» — bu tashxis emas</h2>"
            "<p>Bu o'qish yarmining oxirgi darsi, va u yangi savol turi "
            "o'rgatmaydi. U <mark>mashqni foydali qiladigan</mark> ko'nikmani "
            "o'rgatadi.</p>"
            "<p>Ko'p o'quvchi mashq testini yechadi, ballni ko'radi, "
            "«keyingi safar diqqatliroq bo'laman» deb o'ylaydi va yana o'sha "
            "ballni oladi. Sabab oddiy: <strong>«diqqatliroq bo'lish» yechim "
            "emas</strong>, chunki u qaysi muammoni yechayotganini "
            "aytmaydi.</p>"
            "<p>Har bir noto'g'ri javob to'rt sababdan biriga tegishli, va "
            "ularning yechimlari butunlay boshqacha.</p>"
            + '<span class="sr-time">⏱ ~60 soniya (savollar), keyin tahlil</span>'
        )},

        {"rich_text": (
            "<h3>To'rt sabab</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>№</th><th>Sabab</th><th>Qanday biladi</th><th>Yechim</th></tr></thead>"
              "<tbody>"
              "<tr><td>1</td><td><strong>Savolni noto'g'ri o'qidim</strong></td>"
              "<td>Javobni ko'rganda «men boshqa narsa qidirgan ekanman» "
              "deysiz</td>"
              "<td>Savolni ovoz chiqarmasdan takrorlang; "
              "<em>support/weaken</em>, <em>Text 1/Text 2</em> ni "
              "belgilang</td></tr>"
              "<tr><td>2</td><td><strong>Matnni noto'g'ri o'qidim</strong></td>"
              "<td>Qayta o'qiganingizda matn siz o'ylagandan boshqa narsa "
              "deydi</td>"
              "<td>Sekinroq o'qing — bu <u>vaqt</u> muammosi, bilim "
              "emas</td></tr>"
              "<tr><td>3</td><td><strong>Ikkovini to'g'ri o'qidim, lekin "
              "tuzoqni tanladim</strong></td>"
              "<td>Tushuntirishni o'qigach «ha, endi ko'rdim» deysiz</td>"
              "<td>Tuzoqning <u>nomini</u> yozing; shu tur takrorlanadi</td></tr>"
              "<tr><td>4</td><td><strong>Vaqt yetmadi</strong></td>"
              "<td>Javob tasodifiy edi yoki umuman belgilanmadi</td>"
              "<td>Bilim muammosi emas — taqsimot muammosi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>3 va 4-sabab eng ko'p aralashtiriladi.</strong> "
                "Shoshib tanlangan javob «tuzoqqa tushdim» kabi ko'rinadi, "
                "aslida esa vaqt muammosi. Farqni bilish uchun bitta savol: "
                "<u>agar cheksiz vaqt bo'lganda to'g'ri topardimmi?</u> "
                "Ha bo'lsa — 4-sabab; yo'q bo'lsa — 3-sabab.")
        )},

        {"rich_text": (
            "<h3>Xato daftari</h3>"
            "<p>Har mashqdan keyin faqat noto'g'ri javoblarni yozing — "
            "to'rt ustunda, uch daqiqada:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savol turi</th><th>Sabab (1–4)</th>"
              "<th>Tuzoqning nomi</th><th>Keyingi safar</th></tr></thead>"
              "<tbody>"
              "<tr><td>Inferences</td><td>3</td><td>tashqi bilim</td>"
              "<td>barmoq sinovi</td></tr>"
              "<tr><td>Quantitative</td><td>1</td><td>ulush o'rniga son</td>"
              "<td><em>share</em> so'zini belgilash</td></tr>"
              "<tr><td>Cross-Text</td><td>4</td><td>—</td>"
              "<td>90 soniyada to'xtash</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Ikki-uch mashqdan keyin daftar sizga bir narsani "
                "ko'rsatadi: <strong>xatolaringiz tasodifiy emas</strong>. "
                "Deyarli har bir o'quvchida bitta tur va bitta tuzoq "
                "boshqalardan ko'ra ko'proq takrorlanadi. O'sha ikkitasini "
                "tuzatish — butun kursni qayta o'qishdan ancha samarali.")
        )},

        {
            "rich_text": qnum(1, "1-sabab: savolni noto'g'ri o'qish") + cross_q(
                "<p>Cities that widened their main roads recorded, within five years, "
                "traffic volumes as high as before the widening and journey times no "
                "shorter. The extra capacity, on this account, was filled by journeys "
                "that had not previously been made at all.</p>",
                "<p>Traffic counts in the widened corridors do rise to fill the space. "
                "Counts on the parallel side streets, however, fall by roughly the amount "
                "the main road gains, and total movement across the district changes "
                "little. Much of what looks like new traffic is traffic that has moved.</p>",
                "Based on the texts, how would the author of Text 2 most likely respond "
                "to the explanation offered in Text 1?"),
            "choices": [
                {"text": "By arguing that much of the additional traffic has been drawn from nearby streets rather than newly created.", "is_correct": True},
                {"text": "By agreeing that widening roads generates journeys that would not otherwise have been made.", "is_correct": False},
                {"text": "By denying that traffic volumes on widened roads return to their earlier levels.", "is_correct": False},
                {"text": "By arguing that journey times on widened roads do in fact improve.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bu savol 1-sababni sinaydi.</strong> Yo'nalish: "
                "<u>Text 2</u> gapiradi, <u>Text 1</u> ga. Shoshib o'qigan "
                "o'quvchi teskarisini qiladi va Text 1 ning fikrini "
                "qidiradi.</p>"
                + why([
                    (True, "By arguing that much of the additional traffic has been drawn from nearby streets rather than newly created",
                     "Text 2 ning oxirgi jumlasi: <em>traffic that has "
                     "moved</em> — ko'chgan, yaratilgan emas."),
                    (False, "By agreeing that widening roads generates journeys that would not otherwise have been made",
                     "<strong>Text 1 ning fikri.</strong> Agar siz shuni "
                     "tanlagan bo'lsangiz — bu 1-sabab, 3-sabab emas: siz "
                     "matnni to'g'ri o'qidingiz, lekin kim javob "
                     "berayotganini adashtirdingiz."),
                    (False, "By denying that traffic volumes on widened roads return to their earlier levels",
                     "Text 2 buni tasdiqlaydi (<em>do rise to fill the "
                     "space</em>), inkor qilmaydi."),
                    (False, "By arguing that journey times on widened roads do in fact improve",
                     "Text 2 sayohat vaqti haqida hech nima demaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "2-sabab: matnni noto'g'ri o'qish") + q(
                "<p>The stone circle's tallest stone stands on the line between the "
                "circle's centre and the point where the sun rises at midwinter — but "
                "only if the observer stands at the centre, which the circle's own bank "
                "and ditch make impossible to do from outside. Three smaller stones, "
                "however, mark that line from the entrance, where anyone arriving would "
                "naturally stop.</p>",
                "According to the text, from where is the midwinter alignment visible to "
                "an arriving visitor?"),
            "choices": [
                {"text": "From the entrance, where three smaller stones mark the line.", "is_correct": True},
                {"text": "From the centre of the circle, on the line to the tallest stone.", "is_correct": False},
                {"text": "From outside the bank and ditch, looking towards the tallest stone.", "is_correct": False},
                {"text": "From the point on the horizon where the midwinter sun rises.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bu savol 2-sababni sinaydi.</strong> Matn uzun "
                "jumla bilan boshlanadi va tire ichida shartni beradi "
                "(<em>but only if the observer stands at the centre, which … "
                "make impossible</em>). Tez o'qigan odam markazni "
                "javob deb oladi.</p>"
                + why([
                    (True, "From the entrance, where three smaller stones mark the line",
                     "oxirgi jumla: <em>Three smaller stones … mark that line "
                     "from the entrance</em>. Savol aynan "
                     "<u>kelayotgan tashrifchi</u> haqida."),
                    (False, "From the centre of the circle, on the line to the tallest stone",
                     "<strong>matn buni istisno qiladi:</strong> markazga "
                     "tashqaridan chiqib bo'lmaydi. Bu javobni tanlagan "
                     "o'quvchi <u>shartni o'qimagan</u> — 2-sabab."),
                    (False, "From outside the bank and ditch, looking towards the tallest stone",
                     "eng baland tosh chizig'i faqat markazdan ko'rinadi."),
                    (False, "From the point on the horizon where the midwinter sun rises",
                     "quyosh chiqadigan nuqta — <u>maqsad</u>, kuzatuv joyi "
                     "emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "3-sabab: tuzoqni tanlash") + inf_q(
                "<p>A study of second-hand bookshops found that shops which allow "
                "browsing without pressure keep customers in the shop three times as long "
                "as shops whose staff approach every visitor, and sell about a third more "
                "per opening hour. Staff at the second kind of shop were, on average, "
                "more knowledgeable about the stock. The finding therefore suggests that "
                "<span class=\"sr-blank\"></span></p>"),
            "choices": [
                {"text": "expertise in the staff does not compensate for an approach that shortens the visit.", "is_correct": True},
                {"text": "customers prefer shops whose staff know less about the books on sale.", "is_correct": False},
                {"text": "second-hand bookshops should employ fewer members of staff.", "is_correct": False},
                {"text": "the length of a visit is the only factor that determines how much a shop sells.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bu savol 3-sababni sinaydi</strong> — matn ham, "
                "savol ham qiyin emas, lekin uchta tuzoq juda "
                "ishonarli.</p>"
                "<p>Matn ikki narsani beradi: erkin ko'rish → uzoq qolish → "
                "ko'proq savdo; va ikkinchi turdagi do'konlarda xodimlar "
                "<u>bilimliroq</u>. Ya'ni bilim bor, natija yo'q.</p>"
                + why([
                    (True, "expertise in the staff does not compensate for an approach that shortens the visit",
                     "ikkala faktni ham ishlatadi va ulardan tashqariga "
                     "chiqmaydi."),
                    (False, "customers prefer shops whose staff know less about the books on sale",
                     "<strong>tuzoq: sababni ag'darish.</strong> Mijozlar "
                     "bilimsizlikni <u>afzal ko'rmaydi</u> — ular bosimni "
                     "yoqtirmaydi. Bilim tasodifan ikkinchi turga to'g'ri "
                     "kelgan."),
                    (False, "second-hand bookshops should employ fewer members of staff",
                     "<strong>tuzoq: tavsiya.</strong> Matn xodim sonini "
                     "emas, uslubini muhokama qiladi."),
                    (False, "the length of a visit is the only factor that determines how much a shop sells",
                     "<strong>tuzoq: haddan tashqari kuchli.</strong> "
                     "<em>only factor</em> — matn boshqa omillarni "
                     "istisno qilmaydi."),
                ])
                + NOTE.format(
                    "Agar siz bu savolda xato qilgan bo'lsangiz, "
                    "tushuntirishni o'qigach «ha, endi ko'rdim» dedingizmi? "
                    "Bu 3-sababning belgisi. Daftaringizga tuzoqning "
                    "<u>nomini</u> yozing — «sababni ag'darish», «tavsiya», "
                    "«haddan tashqari kuchli» — chunki aynan o'sha nom "
                    "keyingi mashqda yana chiqadi.")
            ),
        },

        {
            "rich_text": qnum(4, "4-sabab: vaqt") + q(
                "<p>A conservator cleaning a seventeenth-century panel found, beneath the "
                "varnish, a second signature in a different hand from the one on the "
                "frame. Frames were often replaced, and a frame's signature records "
                "whoever owned the panel when the frame was made, not who painted it. The "
                "panel's own signature had been covered by varnish applied at some later "
                "date, and no record survives of when that varnish was put on.</p>",
                "According to the text, what does a signature on a frame record?"),
            "choices": [
                {"text": "The owner of the panel at the time the frame was made.", "is_correct": True},
                {"text": "The painter of the panel the frame surrounds.", "is_correct": False},
                {"text": "The conservator who last cleaned the panel.", "is_correct": False},
                {"text": "The date on which the varnish was applied.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bu savol 4-sababni sinaydi</strong> — u aslida "
                "oson. Javob matnda so'zma-so'z turibdi: <em>a frame's "
                "signature records whoever owned the panel when the frame was "
                "made, not who painted it</em>.</p>"
                "<p>Agar siz bunda xato qilgan yoki uni tashlab ketgan "
                "bo'lsangiz, muammo bilimda emas: siz oldingi savollarga "
                "haddan ortiq vaqt sarflagansiz. "
                "<mark>Oson savolni yo'qotish — eng qimmat xato</mark>, "
                "chunki hamma savol bir xil ball turadi.</p>"
                + why([
                    (True, "The owner of the panel at the time the frame was made",
                     "matndan to'g'ridan-to'g'ri, hech qanday xulosasiz."),
                    (False, "The painter of the panel the frame surrounds",
                     "matn buni <u>ataylab</u> inkor qiladi: <em>not who "
                     "painted it</em>."),
                    (False, "The conservator who last cleaned the panel",
                     "restavrator hikoyani boshlaydi, lekin imzo qo'ymaydi."),
                    (False, "The date on which the varnish was applied",
                     "matn bu sana <u>noma'lum</u> ekanini aytadi."),
                ])
                + TIP.format(
                    "Imtihonda <strong>hamma savol bir xil ball</strong>. "
                    "Qiyin savolga uch daqiqa sarflab, oxiridagi ikki oson "
                    "savolni yo'qotish — sof zarar. 90 soniyada javob "
                    "topilmasa: bitta variant belgilang, savolni belgilab "
                    "qo'ying va keting.")
            ),
        },

        {"rich_text": (
            "<h3>O'qish yarmi tugadi</h3>"
            "<p>Siz endi Reading and Writing bo'limining <strong>o'qish "
            "yarmini</strong> to'liq o'tdingiz — sakkizta savol turi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Domen</th><th>Tur</th><th>Darslar</th></tr></thead>"
              "<tbody>"
              "<tr><td rowspan=\"3\">Craft and Structure</td>"
              "<td>Words in Context</td><td>10–16</td></tr>"
              "<tr><td>Text Structure and Purpose</td><td>20–24</td></tr>"
              "<tr><td>Cross-Text Connections</td><td>30–33</td></tr>"
              "<tr><td rowspan=\"4\">Information and Ideas</td>"
              "<td>Central Ideas and Details</td><td>40–44</td></tr>"
              "<tr><td>Command of Evidence — Textual</td><td>50–54</td></tr>"
              "<tr><td>Command of Evidence — Quantitative</td><td>60–64</td></tr>"
              "<tr><td>Inferences</td><td>70–74</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<p>Bu ikki domen imtihonning taxminan <strong>54 foizini</strong> "
            "tashkil qiladi. Qolgan 46 foiz — grammatika va uslub "
            "(<em>Standard English Conventions</em> va <em>Expression of "
            "Ideas</em>), va u <u>writing</u> bo'limida.</p>"
            + NOTE.format(
                "Ko'p o'quvchi grammatika yarmini «keyinroq» qoldiradi. Bu "
                "xato: grammatika savollari <strong>eng tez yechiladigan</strong> "
                "va qoidalari <u>aniq</u> — ular bo'yicha ball ko'tarish "
                "o'qishga qaraganda ancha tez. Agar vaqtingiz cheklangan "
                "bo'lsa, writing yarmidan boshlang.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to diagnose</div><div class="pp-card-back">tashxis qo\'ymoq, sababini aniqlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to compensate for ~</div><div class="pp-card-back">~ ni qoplamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to browse (in a shop)</div><div class="pp-card-back">bemalol ko\'zdan kechirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an alignment</div><div class="pp-card-back">bir chiziqda joylashuv</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a conservator</div><div class="pp-card-back">restavrator, asarni saqlovchi mutaxassis</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">varnish</div><div class="pp-card-back">lak</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to draw traffic from ~</div><div class="pp-card-back">~ dan harakatni tortib olmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an error log</div><div class="pp-card-back">xato daftari</div></div>'
            + "</div>"
            + "<h3>Xulosa — o'qish yarmi yakuni</h3>"
            + "<ul>"
              "<li>«Diqqatliroq bo'laman» yechim emas. Har xatoni "
              "<strong>to'rt sabab</strong>dan biriga ajrating.</li>"
              "<li>3 va 4-sababni ajratuvchi savol: <u>cheksiz vaqt bo'lganda "
              "topardimmi?</u></li>"
              "<li>Tuzoqning <strong>nomini</strong> yozing — u keyingi "
              "mashqda yana chiqadi.</li>"
              "<li>Hamma savol bir xil ball: <strong>oson savolni "
              "yo'qotmang</strong>.</li>"
              "<li>Keyingi qadam — <strong>writing</strong> yarmi: grammatika "
              "va uslub, imtihonning 46 foizi.</li>"
              "</ul>"
        )},
    ],
},

]
