# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 50-55.

"Fe'l shakllari (Form, Structure and Sense — verbs)" — the second skill inside
Standard English Conventions. Boundaries asked where marks go; this asks which
FORM a word takes.

Two questions carry the whole topic: which word is the subject (agreement), and
what does the rest of the passage say about when this happened (tense). Both are
answered by looking OUTSIDE the blank — at the subject hidden behind a
prepositional phrase, or at the other verbs in the paragraph.

⚠️ This is the OTHER half of the same 54-question section. Its two domains are
Standard English Conventions (~26%) and Expression of Ideas (~20%). There is no
essay and nothing is written by the pupil — every question is a four-choice MCQ,
exactly as in the reading half. See toc_sat_writing.txt and STYLE_GUIDE_SAT_RW.md.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_VERBS = {
    "title":   "Fe'l shakllari (Form, Structure and Sense — verbs)",
    "summary": "Fe'lning shakli: ega bilan moslashuv, zamon tanlash va shaxsli "
               "kesimning o'rnini sifatdosh bilan almashtirib yuborish xatosi.",
    "icon":    "bi-arrow-repeat",
    "order":   6,
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
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def conv_q(passage):
    """Standard English Conventions: the stem never varies."""
    return q(passage, "Which choice completes the text so that it conforms to the "
                      "conventions of Standard English?")


def trans_q(passage):
    """Transitions: the stem never varies either."""
    return q(passage, "Which choice completes the text with the most logical "
                      "transition?")


def notes_q(head, bullets, goal):
    """Rhetorical Synthesis: the research-notes card, then the goal sentence."""
    items = ''.join(f'<li>{b}</li>' for b in bullets)
    return ('<div class="sr-notes">'
            f'<p class="sr-notes__head">{head}</p><ul>{items}</ul></div>'
            f'<p><strong>{goal}</strong></p>')


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def qnum(n, kind):
    return (f'<p style="margin:0 0 4px;"><span style="background:#ede9fe;color:#5b21b6;'
            f'border-radius:999px;padding:2px 10px;font-size:.82rem;font-weight:600;">'
            f'{n}-savol · {kind}</span></p>')


LESSONS = [
# ═══════════════════════════════════════════════════════════════════════════
# Writing 50
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W50: Subject-Verb Agreement — Finding the Real Subject",
    "summary": "Fe'l egaga moslashadi, o'ziga eng yaqin otga emas. Butun tur shu bitta "
               "jumlaga sig'adi — qolgani egani topish mashqi.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>Fe'l egaga moslashadi</h2>"
            "<p>Ega-kesim moslashuvi <em>Form, Structure and Sense</em> "
            "skilining eng ko'p sinaladigan qismi, va uning qoidasi "
            "maktabdan tanish:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Birlikdagi "
                "ega — birlikdagi fe'l. Ko'plikdagi ega — ko'plikdagi "
                "fe'l.</strong></p>")
            + "<p>Unda nega bu savollar yo'qotiladi? Chunki "
            "<mark>SAT egani yashiradi</mark>. U fe'l bilan ega orasiga "
            "o'n so'z qo'yadi, va o'sha so'zlarning oxirgisi "
            "<u>boshqa songa</u> ega bo'ladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✗ <em>The <u>box</u> of iron nails "
                "<strong>were</strong> too heavy to lift.</em><br>"
                "✓ <em>The <u>box</u> of iron nails <strong>was</strong> too "
                "heavy to lift.</em></p>"
                "<p style=\"margin:8px 0 0;\">Ega — <em>box</em> (birlik). "
                "<em>nails</em> — predlogli birikma ichida, va u ega "
                "bo'lolmaydi.</p>")
            + '<span class="sr-time">⏱ ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Egani topish usuli</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Fe'lni toping</strong> — "
              "bo'sh joyda turgan so'z.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. So'rang: kim yoki nima "
              "[fe'l]?</strong> <em>Nima og'ir edi?</em> → "
              "<em>the box</em>. Javob — ega.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ega birlikmi yoki "
              "ko'plikmi?</strong> Faqat shu muhim. Oradagi barcha "
              "so'zlarni <u>o'chirib tashlang</u>.</p></div>"
            + '</div>'
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Son</th><th>Namuna</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>each · every · either · neither</em></td>"
              "<td><strong>birlik</strong></td>"
              "<td><em>Each of the surveys was repeated.</em></td></tr>"
              "<tr><td><em>the number of</em></td><td><strong>birlik</strong></td>"
              "<td><em>The number of visitors has risen.</em></td></tr>"
              "<tr><td><em>a number of</em></td><td><strong>ko'plik</strong></td>"
              "<td><em>A number of visitors have complained.</em></td></tr>"
              "<tr><td>ega + <em>and</em> + ega</td><td><strong>ko'plik</strong></td>"
              "<td><em>The dome and the tower were rebuilt.</em></td></tr>"
              "<tr><td>ega + <em>or / nor</em> + ega</td>"
              "<td><u>yaqinrog'iga</u> moslashadi</td>"
              "<td><em>Neither the towers nor the dome was rebuilt.</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<em>The number of</em> va <em>a number of</em> — SAT'ning "
                "sevimli juftligi, va ular <u>teskari</u> ishlaydi. "
                "<em>The number</em> — bu bitta raqam (birlik). "
                "<em>A number of X</em> — bu «bir necha X» (ko'plik).")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The collection of ledgers, letters and photographs that the firm "
                "deposited with the county archive in 1961 "
                "<span class=\"sr-blank\"></span> nearly two hundred boxes and has never "
                "been catalogued in full.</p>")
            + choices_html([
                "fill",
                "fills",
                "have filled",
                "were filling",
            ])
            + "<p><strong>1-qadam:</strong> fe'l — bo'sh joyda.</p>"
            "<p><strong>2-qadam — kim yoki nima to'ldiradi?</strong> "
            "<em>The collection</em>. Bu <mark>birlik</mark>.</p>"
            "<p><strong>3-qadam — oradagi so'zlarni o'chiramiz:</strong> "
            "<em>of ledgers, letters and photographs</em> — predlogli "
            "birikma; <em>that the firm deposited … in 1961</em> — nisbiy "
            "gap. Ikkovi ham ega bo'lolmaydi.</p>"
            "<p>Qoladi: <em>The collection … fills nearly two hundred "
            "boxes.</em></p>"
            + why([
                (True, "fills",
                 "birlikdagi ega uchun birlikdagi fe'l. Va zamon ham "
                 "to'g'ri: gapning ikkinchi yarmi "
                 "(<em>has never been catalogued</em>) hozirgi holatdan "
                 "gapiryapti."),
                (False, "fill",
                 "ko'plik shakli — u <em>photographs</em> ga moslashgan, "
                 "ya'ni <u>eng yaqin otga</u>. Bu darsning bosh xatosi."),
                (False, "have filled",
                 "yana ko'plik (<em>have</em>), va ustiga zamon "
                 "o'zgargan."),
                (False, "were filling",
                 "ko'plik va o'tgan davomli zamon — ikkovi ham "
                 "noto'g'ri."),
            ])
            + NOTE.format(
                "Ega bilan fe'l orasida <u>o'n olti so'z</u> bor, va "
                "ularning ichida uchta ko'plik ot: <em>ledgers · letters · "
                "photographs</em>. SAT ularni ataylab shu tartibda "
                "qo'yadi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Each of the eleven winters for which the road authority still holds "
                "records <span class=\"sr-blank\"></span> at least three weeks in which "
                "the pass was closed by snow, and in two of those winters the closure "
                "lasted from the middle of December until the first week of March.</p>"),
            "choices": [
                {"text": "includes", "is_correct": True},
                {"text": "include", "is_correct": False},
                {"text": "have included", "is_correct": False},
                {"text": "were including", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>Each</em>. "
                "<em>of the eleven winters for which records survive</em> — "
                "predlogli birikma va nisbiy gap, ikkovi ham "
                "o'chiriladi.</p>"
                "<p><mark><em>Each</em> har doim birlik</mark> — hatto "
                "undan keyin ko'plikdagi ot kelsa ham.</p>"
                + why([
                    (True, "includes",
                     "<em>Each … includes</em>. Birlik."),
                    (False, "include",
                     "<em>winters</em> ga moslashgan — lekin u predlogli "
                     "birikma ichida."),
                    (False, "have included",
                     "ko'plik yordamchi fe'l (<em>have</em>), va "
                     "<em>Each</em> uchun <em>has</em> kerak bo'lardi."),
                    (False, "were including",
                     "ko'plik va davomli zamon; qayd etilgan fakt uchun "
                     "oddiy hozirgi zamon kerak."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The number of households in the district reporting a vegetable garden of "
                "any size <span class=\"sr-blank\"></span> by about a fifth since the "
                "survey began in 1998, and the sharpest part of the decline came in the five "
                "years after the largest allotment site was sold for housing.</p>"),
            "choices": [
                {"text": "has fallen", "is_correct": True},
                {"text": "have fallen", "is_correct": False},
                {"text": "are falling", "is_correct": False},
                {"text": "fall", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The number</em> — birlik. "
                "<em>of households in the district reporting a vegetable "
                "garden</em> — hammasi predlogli birikma va sifatdosh "
                "bo'lagi.</p>"
                "<p><em>The number</em> = bitta raqam. Bu "
                "<mark>birlik</mark> — <em>a number of</em> dan farqli "
                "o'laroq.</p>"
                "<p>Zamon: <em>since the survey began</em> — o'tmishda "
                "boshlanib bugungacha davom etgan, ya'ni "
                "<strong>present perfect</strong> (53-dars).</p>"
                + why([
                    (True, "has fallen",
                     "birlik + present perfect. <em>since</em> ikkinchi "
                     "shartni belgilaydi."),
                    (False, "have fallen",
                     "zamon to'g'ri, son noto'g'ri: <em>households</em> ga "
                     "moslashgan."),
                    (False, "are falling",
                     "ko'plik va davomli zamon; <em>since</em> perfect "
                     "talab qiladi."),
                    (False, "fall",
                     "ko'plik va oddiy hozirgi zamon — <em>since the "
                     "survey began</em> bilan mos kelmaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Neither the two rural districts surveyed in the spring nor the suburban "
                "one surveyed in the autumn <span class=\"sr-blank\"></span> a rise in "
                "the share of journeys made on foot, although all three reported one "
                "in each of the three previous surveys.</p>"),
            "choices": [
                {"text": "records", "is_correct": True},
                {"text": "record", "is_correct": False},
                {"text": "have recorded", "is_correct": False},
                {"text": "were recording", "is_correct": False},
            ],
            "explanation": (
                "<p><em>Neither … nor …</em> qurilishida fe'l "
                "<mark>o'ziga yaqinroq turgan egaga</mark> moslashadi.</p>"
                "<p>Bu yerda yaqinrog'i — <em>the suburban one</em>, "
                "<u>birlik</u>. Demak fe'l ham birlik.</p>"
                + why([
                    (True, "records",
                     "yaqin ega birlik (<em>the suburban one</em>), demak "
                     "birlikdagi fe'l."),
                    (False, "record",
                     "<em>the two rural districts</em> ga moslashgan — "
                     "lekin u <u>uzoqroq</u> ega. <em>nor</em> "
                     "qurilishida yaqinrog'i hal qiladi."),
                    (False, "have recorded",
                     "ko'plik yordamchi, va yaqin ega birlik."),
                    (False, "were recording",
                     "ko'plik va davomli zamon; <em>last year</em> oddiy "
                     "o'tgan zamon talab qilardi, lekin son baribir "
                     "noto'g'ri."),
                ])
                + TIP.format(
                    "<em>or</em> va <em>nor</em> qurilishida SAT ataylab "
                    "<strong>ko'plikni oldinga, birlikni orqaga</strong> "
                    "qo'yadi — chunki quloq birinchi eshitgan songa "
                    "moslashadi. Fe'lga <u>eng yaqin</u> egani "
                    "qidiring.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A number of the tablets recovered from the burnt archive "
                "<span class=\"sr-blank\"></span> still unread, and the script on two of "
                "them has not been matched to any known language.</p>"),
            "choices": [
                {"text": "remain", "is_correct": True},
                {"text": "remains", "is_correct": False},
                {"text": "has remained", "is_correct": False},
                {"text": "was remaining", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu <em>the number of</em> ning juftligi, va u "
                "<mark>teskari</mark> ishlaydi.</p>"
                "<p><em>A number of the tablets</em> = «bir nechta lavha» — "
                "ega aslida <u>lavhalar</u>, ya'ni <strong>ko'plik</strong>. "
                "<em>A number of</em> bu yerda miqdor bildiruvchi ibora, "
                "ega emas.</p>"
                + why([
                    (True, "remain",
                     "ko'plik. Gapning ikkinchi yarmi ham buni tasdiqlaydi: "
                     "<em>two of them</em>."),
                    (False, "remains",
                     "birlik — <em>a number</em> ni ega deb olgan. Lekin "
                     "<em>a number of X</em> = «bir necha X»."),
                    (False, "has remained",
                     "birlik yordamchi, va zamon ham o'zgargan."),
                    (False, "was remaining",
                     "birlik va davomli zamon; holat fe'li "
                     "(<em>remain</em>) davomli shaklda "
                     "ishlatilmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">subject-verb agreement</div><div class="pp-card-back">ega-kesim moslashuvi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a prepositional phrase</div><div class="pp-card-back">predlogli birikma (ega bo\'lolmaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the number of ~</div><div class="pp-card-back">~ ning soni (BIRLIK)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a number of ~</div><div class="pp-card-back">bir nechta ~ (KO\'PLIK)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">each / every / neither</div><div class="pp-card-back">har doim birlik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">neither … nor …</div><div class="pp-card-back">fe\'l yaqinroq egaga moslashadi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to deposit (records)</div><div class="pp-card-back">(hujjatlarni) topshirib qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a script (writing)</div><div class="pp-card-back">yozuv tizimi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Fe'l egaga moslashadi</strong>, eng yaqin otga "
              "emas.</li>"
              "<li>Usul: fe'lni top → «kim/nima [fe'l]?» → oradagi "
              "so'zlarni <u>o'chir</u>.</li>"
              "<li><em>each · every · neither</em> — birlik. "
              "<em>X and Y</em> — ko'plik.</li>"
              "<li><em>the number of</em> = birlik; "
              "<em>a number of</em> = ko'plik.</li>"
              "<li><em>or / nor</em> — fe'l <strong>yaqinroq</strong> egaga "
              "moslashadi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 51
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W51: Prepositional Phrases and Other Words Hiding the Subject",
    "summary": "SAT egani to'rt usul bilan yashiradi: predlogli birikma, nisbiy gap, "
               "«along with» iboralari va teskari tartib. Har biriga o'z hiylasi bor.",
    "order": 51,
    "blocks": [
        {"rich_text": (
            "<h2>Egani yashirishning to'rt usuli</h2>"
            "<p>50-darsda qoidani ko'rdik. Bu dars — <mark>SAT egani "
            "qanday yashirishi</mark> haqida, chunki qoidani bilgan "
            "o'quvchi baribir yiqilishi mumkin: u shunchaki noto'g'ri "
            "so'zni ega deb oladi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Yashirish usuli</th><th>Namuna</th>"
              "<th>Hiyla</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Predlogli birikma</strong></td>"
              "<td><em>The box <u>of nails</u> is…</em></td>"
              "<td><em>of · in · with · from</em> dan keyingi ot ega "
              "bo'lolmaydi</td></tr>"
              "<tr><td><strong>Nisbiy gap</strong></td>"
              "<td><em>The ledger <u>that the clerks kept</u> is…</em></td>"
              "<td><em>that/which/who</em> ichidagi ot ham ega "
              "emas</td></tr>"
              "<tr><td><strong><em>along with</em> iboralari</strong></td>"
              "<td><em>The dome, <u>along with the towers</u>, was…</em></td>"
              "<td>Sonni <u>o'zgartirmaydi</u> — <em>and</em> emas</td></tr>"
              "<tr><td><strong>Teskari tartib</strong></td>"
              "<td><em>Behind the wall <u>stand</u> three towers.</em></td>"
              "<td>Ega fe'ldan <u>keyin</u> keladi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Uchinchi qator eng ayyor: <em>along with · as well as · "
                "together with · in addition to · including</em> "
                "<strong>egani ko'plik qilmaydi</strong>. "
                "<em>The dome, along with the towers, <u>was</u> "
                "rebuilt.</em> — <em>and</em> bo'lganda "
                "<em>were</em> bo'lardi, lekin bu <em>and</em> emas.")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The mechanism of the cathedral clock, together with the two bells it "
                "was built to strike and the wooden frame that carries them, "
                "<span class=\"sr-blank\"></span> been in place since the fourteenth "
                "century.</p>")
            + choices_html([
                "have",
                "has",
                "were",
                "are",
            ])
            + "<p><strong>Egani toping.</strong> «Nima o'z joyida "
            "turibdi?» → <em>The mechanism</em>. Birlik.</p>"
            "<p><strong>Oradagilarni o'chiramiz:</strong> "
            "<em>of the cathedral clock</em> (predlogli birikma), "
            "<em>together with the two bells … and the wooden frame that "
            "carries them</em> (<mark><em>together with</em> — sonni "
            "o'zgartirmaydi</mark>).</p>"
            "<p>Qoladi: <em>The mechanism … has been in place…</em></p>"
            + why([
                (True, "has",
                 "birlik ega uchun birlik yordamchi fe'l. Va "
                 "<em>since the fourteenth century</em> present perfect "
                 "talab qiladi — <em>has been</em>."),
                (False, "have",
                 "ko'plik. <em>together with</em> ni <em>and</em> deb "
                 "o'qigan o'quvchi shuni tanlaydi — bu darsning bosh "
                 "tuzog'i."),
                (False, "were",
                 "ko'plik va oddiy o'tgan zamon; <em>since</em> perfect "
                 "talab qiladi."),
                (False, "are",
                 "ko'plik va hozirgi zamon; <em>been</em> bilan birga "
                 "kelmaydi."),
            ])
            + NOTE.format(
                "Diqqat: <em>bells</em> va <em>frame</em> — ikkovi ham "
                "vergullar orasidagi qo'shimcha bo'lakda. 42-darsdagi "
                "olib tashlash sinovi bu yerda ham ishlaydi: "
                "qo'shimchani olsak, <em>The mechanism has been in place "
                "since the fourteenth century</em> qoladi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Along the ridge above the old drove road <span class=\"sr-blank\"></span> six "
                "stone cairns, built by the surveyors who had neither timber nor wire to "
                "mark the boundary with.</p>"),
            "choices": [
                {"text": "stand", "is_correct": True},
                {"text": "stands", "is_correct": False},
                {"text": "has stood", "is_correct": False},
                {"text": "was standing", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Teskari tartib.</strong> Gap predlogli birikma "
                "bilan boshlanadi (<em>Along the ridge above the pass</em>), "
                "va ega fe'ldan <u>keyin</u> keladi.</p>"
                "<p>«Nima turibdi?» → <em>six stone cairns</em>. "
                "<mark>Ko'plik.</mark></p>"
                + why([
                    (True, "stand",
                     "ko'plik ega uchun ko'plik fe'l. Gapni to'g'ri "
                     "tartibga solsak: <em>Six stone cairns stand along the "
                     "ridge…</em>"),
                    (False, "stands",
                     "birlik — <em>the pass</em> ga moslashgan, lekin u "
                     "predlogli birikma ichida va ega emas."),
                    (False, "has stood",
                     "birlik yordamchi, va zamon ham o'zgargan."),
                    (False, "was standing",
                     "birlik va davomli zamon; doimiy holat uchun oddiy "
                     "hozirgi zamon kerak."),
                ])
                + TIP.format(
                    "Gap predlog bilan boshlansa (<em>Along · Behind · "
                    "Among · In</em>) yoki <em>There</em> bilan, "
                    "<strong>ega fe'ldan keyin</strong> bo'lishi mumkin. "
                    "Gapni xayolan to'g'ri tartibga soling.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The three sketchbooks that the conservator found in a crate beneath the "
                "studio stairs and that no one had opened since 1907 "
                "<span class=\"sr-blank\"></span> a second signature in a hand quite "
                "unlike the artist's own.</p>"),
            "choices": [
                {"text": "carry", "is_correct": True},
                {"text": "carries", "is_correct": False},
                {"text": "has carried", "is_correct": False},
                {"text": "is carrying", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The three sketchbooks</em> — "
                "ko'plik. Ikkita nisbiy gap "
                "(<em>that the conservator found…</em> va "
                "<em>that no one had opened…</em>) uni fe'ldan uzoqlashtiradi "
                "va ichlarida birlik otlar bor "
                "(<em>the conservator · a crate · no one · "
                "1907</em>).</p>"
                + why([
                    (True, "carry",
                     "ko'plik ega — ko'plik fe'l."),
                    (False, "carries",
                     "birlik — nisbiy gap ichidagi <em>no one</em> yoki "
                     "<em>the conservator</em> ga moslashgan."),
                    (False, "has carried",
                     "birlik yordamchi va perfect zamon; gapda buni "
                     "talab qiladigan vaqt belgisi yo'q."),
                    (False, "is carrying",
                     "birlik va davomli zamon; doimiy fakt uchun "
                     "yaramaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The report's conclusion, as well as the two appendices that set out "
                "the raw counts and the method used to collect them, "
                "<span class=\"sr-blank\"></span> available on the council's website.</p>"),
            "choices": [
                {"text": "is", "is_correct": True},
                {"text": "are", "is_correct": False},
                {"text": "have been", "is_correct": False},
                {"text": "were", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The report's conclusion</em> — "
                "birlik.</p>"
                "<p><em>as well as the two appendices…</em> — bu "
                "<mark>vergullar orasidagi qo'shimcha</mark>, va "
                "<em>as well as</em> <u>egani ko'paytirmaydi</u>. "
                "Agar <em>and</em> bo'lganida <em>are</em> to'g'ri "
                "bo'lardi.</p>"
                + why([
                    (True, "is",
                     "birlik ega — birlik fe'l. Olib tashlash sinovi: "
                     "<em>The report's conclusion is available…</em> ✓"),
                    (False, "are",
                     "<strong>bu darsning bosh tuzog'i:</strong> "
                     "<em>as well as</em> ni <em>and</em> deb o'qish. "
                     "Ular ma'noda yaqin, grammatikada boshqa."),
                    (False, "have been",
                     "ko'plik yordamchi va perfect zamon."),
                    (False, "were",
                     "ko'plik va o'tgan zamon; hujjatlar hozir mavjud."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>There <span class=\"sr-blank\"></span> in the archive four ledgers "
                "from the mill, and the one kept by the owner's daughter is the only "
                "one to record wages as well as output.</p>"),
            "choices": [
                {"text": "are", "is_correct": True},
                {"text": "is", "is_correct": False},
                {"text": "has been", "is_correct": False},
                {"text": "was", "is_correct": False},
            ],
            "explanation": (
                "<p><em>There</em> hech qachon ega bo'lmaydi — u shunchaki "
                "gapni boshlaydi. <strong>Haqiqiy ega fe'ldan keyin "
                "keladi:</strong> <em>four ledgers</em>. "
                "<mark>Ko'plik.</mark></p>"
                + why([
                    (True, "are",
                     "ko'plik ega (<em>four ledgers</em>) uchun ko'plik "
                     "fe'l."),
                    (False, "is",
                     "birlik — <em>There</em> ni ega deb olgan, yoki "
                     "<em>the archive</em> ga moslashgan."),
                    (False, "has been",
                     "birlik yordamchi va perfect; gapning ikkinchi yarmi "
                     "hozirgi zamonda (<em>is the only one</em>)."),
                    (False, "was",
                     "birlik va o'tgan zamon."),
                ])
                + TIP.format(
                    "<strong><em>There</em> va <em>Here</em> hech qachon "
                    "ega emas.</strong> Ular bilan boshlangan gapda "
                    "fe'ldan keyingi otni qidiring — son o'sha yerda "
                    "hal bo'ladi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">along with / together with</div><div class="pp-card-back">~ bilan birga (sonni O\'ZGARTIRMAYDI)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">as well as</div><div class="pp-card-back">shuningdek (and EMAS — son o\'zgarmaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">inverted order</div><div class="pp-card-back">teskari tartib (ega fe\'ldan keyin)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">There is / There are</div><div class="pp-card-back">There ega emas — keyingi otga qarang</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an appendix (appendices)</div><div class="pp-card-back">ilova (ilovalar)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cairn</div><div class="pp-card-back">tosh uyumi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">raw counts</div><div class="pp-card-back">qayta ishlanmagan sanoq ma\'lumotlari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">varnish</div><div class="pp-card-back">lak</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>To'rt yashirish usuli: <strong>predlogli birikma · "
              "nisbiy gap · <em>along with</em> · teskari tartib</strong>.</li>"
              "<li><em>along with · as well as · together with · "
              "including</em> — <strong>sonni o'zgartirmaydi</strong>.</li>"
              "<li><em>There</em> va <em>Here</em> hech qachon ega "
              "emas.</li>"
              "<li>Predlog bilan boshlangan gapda egani "
              "<u>fe'ldan keyin</u> qidiring.</li>"
              "<li>Har doim so'rang: <strong>kim yoki nima "
              "[fe'l]?</strong></li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 52
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W52: Verb Tense From Context — The Timeline in the Passage",
    "summary": "Zamon bo'sh joyli gapdan emas, atrofdagi fe'llar va vaqt "
               "belgilaridan chiqadi. Javob har doim bo'sh joydan tashqarida.",
    "order": 52,
    "blocks": [
        {"rich_text": (
            "<h2>Zamon gapdan emas, matndan chiqadi</h2>"
            "<p>Ega-kesim savolida javob gapning <u>ichida</u> edi. Zamon "
            "savolida esa u <mark>tashqarida</mark>: bo'sh joyli gapning "
            "o'zi ko'pincha ikki-uch zamonni ham qabul qiladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The society "
                "<span style=\"border-bottom:2px solid #7c3aed;\">&nbsp;&nbsp;&nbsp;&nbsp;</span> "
                "every surviving watermill in the county.</em></p>"
                "<p style=\"margin:8px 0 0;\"><em>records · recorded · has "
                "recorded · had recorded</em> — to'rttasi ham gapga "
                "tushadi. Javobni faqat <u>atrofdagi jumlalar</u> "
                "beradi.</p>")
            + "<p>Demak usul oddiy: <strong>bo'sh joydan tashqaridagi "
            "fe'llarni va vaqt belgilarini o'qing</strong>.</p>"
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki manba</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Manba</th><th>Nima beradi</th><th>Namuna</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Vaqt belgilari</strong></td>"
              "<td>Zamonni to'g'ridan-to'g'ri</td>"
              "<td><em>in 1890 · last winter · today · currently · now · "
              "since 1873 · over the past decade</em></td></tr>"
              "<tr><td><strong>Boshqa fe'llar</strong></td>"
              "<td>Izchillikni</td>"
              "<td>Atrofdagi jumlalar o'tgan zamonda bo'lsa, bo'sh joy ham "
              "odatda o'tgan zamonda</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Izchillik qoida emas, moyillik.</strong> Matn "
                "o'tmishdan bugunga o'tishi mumkin: "
                "<em>The mill closed in 1962. The building now houses a "
                "museum.</em> Vaqt belgisi (<em>now</em>) izchillikdan "
                "<u>kuchliroq</u> — u bor bo'lsa, unga ishoning.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The lighthouse was automated in 1988, and the last keeper left that "
                "autumn. He took the logbooks with him, and for thirty years nobody knew "
                "where they were. In 2019 his daughter "
                "<span class=\"sr-blank\"></span> the whole series to the county "
                "archive.</p>")
            + choices_html([
                "gives",
                "gave",
                "has given",
                "will give",
            ])
            + "<p><strong>Vaqt belgisi:</strong> <em>In 2019</em> — "
            "tugagan o'tmish nuqtasi.</p>"
            "<p><strong>Boshqa fe'llar:</strong> <em>was automated · "
            "left · took · knew</em> — hammasi oddiy o'tgan zamon.</p>"
            "<p>Ikkala manba ham bir xil javobni beradi.</p>"
            + why([
                (True, "gave",
                 "oddiy o'tgan zamon. <em>In 2019</em> aniq tugagan "
                 "nuqta, va matnning butun zanjiri o'tgan zamonda."),
                (False, "has given",
                 "present perfect aniq o'tmish sanasi bilan "
                 "<u>ishlatilmaydi</u>: <em>has given in 2019</em> "
                 "noto'g'ri. Perfect «qachon» degan savolga javob "
                 "bermaydi."),
                (False, "gives",
                 "hozirgi zamon — 2019-yilgi bir martalik voqea uchun "
                 "yaramaydi."),
                (False, "will give",
                 "kelasi zamon; voqea allaqachon bo'lgan."),
            ])
            + NOTE.format(
                "<strong>Aniq sana + present perfect = har doim "
                "xato.</strong> <em>in 1988 · in 2019 · last autumn · "
                "two years ago</em> — bularning yonida "
                "<em>has/have + V3</em> kelmaydi. Bu bitta qoida "
                "ko'p savolni yechadi.")
        )},

        {
            "rich_text": conv_q(
                "<p>The mill ground flour for the village until the river was diverted "
                "in 1931. The wheel was taken out a few years later and the building "
                "stood empty for half a century. Today the ground floor "
                "<span class=\"sr-blank\"></span> a small museum of local "
                "trades.</p>"),
            "choices": [
                {"text": "houses", "is_correct": True},
                {"text": "housed", "is_correct": False},
                {"text": "had housed", "is_correct": False},
                {"text": "was housing", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Vaqt belgisi:</strong> <em>Today</em>. Bu "
                "matnning o'tmishdan bugunga <mark>o'tish nuqtasi</mark>.</p>"
                "<p>Oldingi jumlalar o'tgan zamonda — lekin vaqt belgisi "
                "izchillikdan kuchliroq (yuqoridagi ogohlantirish).</p>"
                + why([
                    (True, "houses",
                     "hozirgi zamon. <em>Today</em> buni to'g'ridan-to'g'ri "
                     "talab qiladi."),
                    (False, "housed",
                     "o'tgan zamon — atrofdagi fe'llarga moslashgan, "
                     "lekin <em>Today</em> ga zid. Izchillikka "
                     "ko'r-ko'rona ergashish bu darsning bosh "
                     "xatosi."),
                    (False, "had housed",
                     "past perfect ikkita o'tgan voqeani talab qiladi "
                     "(53-dars), va <em>Today</em> bilan umuman mos "
                     "kelmaydi."),
                    (False, "was housing",
                     "o'tgan davomli zamon; <em>Today</em> ga zid, va "
                     "doimiy holat uchun davomli shakl ham "
                     "yaramaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Volunteers have kept rain gauges in their gardens across the county "
                "since the 1880s, and the network they maintain is denser than any "
                "official one. Meteorologists ignored these records for decades. They "
                "<span class=\"sr-blank\"></span> them routinely now, and two national "
                "series have been corrected against them.</p>"),
            "choices": [
                {"text": "use", "is_correct": True},
                {"text": "used", "is_correct": False},
                {"text": "had used", "is_correct": False},
                {"text": "were using", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Vaqt belgisi:</strong> <em>now</em>, va u "
                "bo'sh joyning o'z gapida turibdi.</p>"
                "<p>Matn qarama-qarshilik quryapti: "
                "<em>ignored … for decades</em> (o'tmish) ↔ "
                "<em>use them routinely now</em> (bugun).</p>"
                + why([
                    (True, "use",
                     "hozirgi zamon. <em>now</em> va oxirgi bo'lakdagi "
                     "<em>have been corrected</em> ikkovi ham bugungi "
                     "holatni ko'rsatadi."),
                    (False, "used",
                     "o'tgan zamon — oldingi jumlaning "
                     "<em>ignored</em> iga moslashgan, lekin "
                     "<em>now</em> ga zid va qarama-qarshilikni "
                     "yo'q qiladi."),
                    (False, "had used",
                     "past perfect: ikkinchi o'tgan voqea yo'q, va "
                     "<em>now</em> bilan mos kelmaydi."),
                    (False, "were using",
                     "o'tgan davomli zamon — yana <em>now</em> ga "
                     "zid."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Ulugh Beg's astronomers compiled their catalogue in the 1430s from "
                "measurements taken with a single enormous arc set into the ground. The "
                "observatory <span class=\"sr-blank\"></span> within a few decades of his "
                "death, and the catalogue survived only because copies had already "
                "travelled west.</p>"),
            "choices": [
                {"text": "was destroyed", "is_correct": True},
                {"text": "is destroyed", "is_correct": False},
                {"text": "has been destroyed", "is_correct": False},
                {"text": "will have been destroyed", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshqa fe'llar:</strong> <em>compiled · "
                "survived · had already travelled</em> — matn butunlay "
                "XV asrda.</p>"
                "<p><strong>Vaqt belgisi:</strong> <em>within a few decades "
                "of his death</em> — tugagan o'tmish davri.</p>"
                + why([
                    (True, "was destroyed",
                     "oddiy o'tgan zamon, majhul nisbatda. Matnning "
                     "zanjiriga to'liq mos."),
                    (False, "has been destroyed",
                     "present perfect bugungi holatga bog'laydi — lekin "
                     "voqea besh asr oldin, aniq davrda bo'lgan."),
                    (False, "is destroyed",
                     "hozirgi zamon — XV asr voqeasi uchun yaramaydi."),
                    (False, "will have been destroyed",
                     "kelasi perfect — matnda kelajak umuman yo'q."),
                ])
                + TIP.format(
                    "Zamon savolida <strong>bo'sh joyni oxirgi</strong> "
                    "o'qing. Avval atrofdagi ikki-uch fe'lni va vaqt "
                    "belgilarini toping — javob deyarli har doim shu "
                    "yerda hal bo'ladi, va variantlarni ochish "
                    "faqat tasdiqlash bo'lib qoladi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The library bought an iron hand press in 1893 and printed its own "
                "catalogue cards on it until the last of the card drawers was "
                "retired. The machine <span class=\"sr-blank\"></span> in the "
                "basement ever since, and the staff have twice brought it upstairs "
                "for an open day.</p>"),
            "choices": [
                {"text": "has stood", "is_correct": True},
                {"text": "stood", "is_correct": False},
                {"text": "stands", "is_correct": False},
                {"text": "had stood", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Vaqt belgisi:</strong> <em>ever since</em>. "
                "<em>since</em> — o‘tmishda boshlanib bugungacha davom "
                "etayotgan holatning belgisi, va u "
                "<mark>present perfect</mark> talab qiladi.</p>"
                "<p><strong>Tasdiq:</strong> gapning ikkinchi yarmi ham "
                "perfect — <em>the staff have twice brought it</em>.</p>"
                + why([
                    (True, "has stood",
                     "present perfect: kartochkalar tugaganidan beri "
                     "boshlangan va hali davom etayotgan holat. "
                     "<em>since</em> ning standart juftligi."),
                    (False, "stood",
                     "oddiy o‘tgan zamon — u holatning "
                     "<u>tugaganini</u> bildiradi, matn esa uning davom "
                     "etayotganini aytadi."),
                    (False, "stands",
                     "hozirgi zamon <em>since</em> bilan kelmaydi: "
                     "<em>stands ever since</em> noto‘g‘ri."),
                    (False, "had stood",
                     "past perfect ikkinchi o‘tgan voqeani talab qiladi "
                     "(53-dars), va u bugungacha davom etishni "
                     "bildirmaydi."),
                ])
                + TIP.format(
                    "<strong><em>since</em> va <em>for</em> — present "
                    "perfect ning eng ishonchli belgilari.</strong> "
                    "<em>since 1893 · for thirty years · over the past "
                    "decade</em> ko‘rsangiz, <em>has/have + V3</em> "
                    "ni qidiring.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a time marker</div><div class="pp-card-back">vaqt belgisi (in 1890, today, since…)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">tense consistency</div><div class="pp-card-back">zamon izchilligi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to divert a river</div><div class="pp-card-back">daryoni boshqa yo\'nalishga burmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rain gauge</div><div class="pp-card-back">yog\'in o\'lchagich</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">routinely</div><div class="pp-card-back">muntazam, odatiy tarzda</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hand press</div><div class="pp-card-back">qo\'l bosmaxona dastgohi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to compile a catalogue</div><div class="pp-card-back">katalog tuzmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">local trades</div><div class="pp-card-back">mahalliy hunarlar</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Zamon <strong>bo'sh joydan tashqarida</strong> hal "
              "bo'ladi: vaqt belgilari va boshqa fe'llar.</li>"
              "<li>Vaqt belgisi izchillikdan <strong>kuchliroq</strong>: "
              "<em>Today · now</em> bo'lsa, atrof o'tgan zamonda "
              "bo'lsa ham hozirgi zamon.</li>"
              "<li><strong>Aniq sana + present perfect = xato.</strong> "
              "<em>has given in 2019</em> bo'lmaydi.</li>"
              "<li>Bo'sh joyni <u>oxirgi</u> o'qing — avval atrofni.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 53
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W53: Past Perfect and Present Perfect — When the SAT Wants Them",
    "summary": "Past perfect ikkita o'tgan voqeani talab qiladi; present perfect esa "
               "bugungacha davom etgan holatni. Ikkovi ham shartsiz ishlatilmaydi.",
    "order": 53,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki perfect, ikki shart</h2>"
            "<p>Perfect zamonlar o'zbek o'quvchi uchun qiyin, chunki ular "
            "o'zbek tilida bir xil shaklda tarjima qilinadi. Lekin ingliz "
            "tilida ularning har biri <mark>aniq bir shart</mark> talab "
            "qiladi, va shart bo'lmasa — ular xato.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Sharti</th><th>Belgisi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Past perfect</strong><br><em>had + V3</em></td>"
              "<td>Matnda <u>ikkita</u> o'tgan voqea bor, va bu "
              "<u>erta</u>rog'i</td>"
              "<td><em>by the time · before · already · when X happened, Y "
              "had…</em></td></tr>"
              "<tr><td><strong>Present perfect</strong><br>"
              "<em>has/have + V3</em></td>"
              "<td>O'tmishda boshlanib <u>bugungacha</u> davom etgan yoki "
              "bugun ahamiyatli</td>"
              "<td><em>since · for · over the past · so far · already · "
              "never</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Ikki eng ko'p uchraydigan xato:</strong><br>"
                "1. Past perfect <u>bitta</u> o'tgan voqea bilan: "
                "<em>The mill had closed in 1962.</em> ✗ — ikkinchi voqea "
                "yo'q, oddiy o'tgan zamon kerak.<br>"
                "2. Present perfect <u>aniq sana</u> bilan: "
                "<em>has closed in 1962</em> ✗ — 52-darsdagi qoida.")
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Past perfect: zanjirning ertarog'i</h3>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>When the box was opened in 1948, "
                "every page <strong>was</strong> legible.</em><br>"
                "→ ikki voqea bir vaqtda: ochildi va o'qildi.</p>"
                "<p style=\"margin:8px 0 0;\"><em>When the box was opened in "
                "1948, the cellar <strong>had stood</strong> open to the "
                "weather for two winters.</em><br>"
                "→ ikki voqea, va turish "
                "<u>ochilishdan oldin</u> bo'lgan. Past perfect.</p>")
            + "<p>Sinov: <strong>matnda ikkinchi o'tgan voqea bormi, va "
            "bu undan oldinmi?</strong> Ikkala javob ham «ha» bo'lsa — "
            "past perfect. Aks holda oddiy o'tgan zamon.</p>"
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The cuneiform tablets in the palace archive were baked hard by the "
                "fire that destroyed the building in about 1200 BCE. Ordinary tablets "
                "were left to dry rather than fired, and by the time the fire reached "
                "the room the clay <span class=\"sr-blank\"></span> for perhaps forty "
                "years without hardening at all.</p>")
            + choices_html([
                "sat",
                "had sat",
                "has sat",
                "sits",
            ])
            + "<p><strong>Ikki o'tgan voqea bormi?</strong> Ha: "
            "(1) yong'in xonaga yetdi; (2) loy qirq yil turdi.</p>"
            "<p><strong>Qaysi biri erta?</strong> Turish — yong'indan "
            "<u>oldin</u>. Va matn buni ochiq aytadi: "
            "<mark><em>by the time the fire reached the room</em></mark>.</p>"
            + why([
                (True, "had sat",
                 "past perfect: <em>by the time</em> ikki voqeani "
                 "tartibga soladi, va loyning turishi ertaroq. Ikkala "
                 "shart ham bajarilgan."),
                (False, "sat",
                 "oddiy o'tgan zamon — ikki voqeani bir vaqtga qo'yadi va "
                 "<em>by the time</em> ning ma'nosini yo'q qiladi."),
                (False, "has sat",
                 "present perfect bugungacha davom etishni bildiradi — "
                 "lekin loy 1200-yilda pishib bo'lgan."),
                (False, "sits",
                 "hozirgi zamon; matn butunlay o'tmishda."),
            ])
            + NOTE.format(
                "<em>by the time · before · after · already · when</em> — "
                "bu so'zlar ikki o'tgan voqeani <u>tartibga soladi</u>, "
                "va ular past perfect ning eng ishonchli belgilaridir. "
                "Ular bo'lmasa, past perfect ga shubha bilan qarang.")
        )},

        {
            "rich_text": conv_q(
                "<p>Tram wires were taken down in the city centre in 1962 and the rails "
                "tarred over. The transport museum <span class=\"sr-blank\"></span> "
                "for the return of a single line for more than a decade, and it now "
                "has a working car waiting in a shed for the day.</p>"),
            "choices": [
                {"text": "has campaigned", "is_correct": True},
                {"text": "campaigned", "is_correct": False},
                {"text": "had campaigned", "is_correct": False},
                {"text": "campaigns", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Belgi:</strong> <em>for more than a decade</em> — "
                "o'tmishda boshlanib bugungacha davom etayotgan. "
                "<mark>Present perfect.</mark></p>"
                "<p><strong>Tasdiq:</strong> gapning davomi hozirgi "
                "zamonda — <em>it <u>now</u> has a working car waiting</em>.</p>"
                + why([
                    (True, "has campaigned",
                     "present perfect: <em>for + davomiylik</em> ning "
                     "standart juftligi, va u bugungacha yetadi."),
                    (False, "campaigned",
                     "oddiy o'tgan zamon harakat <u>tugaganini</u> "
                     "bildiradi, matn esa u davom etayotganini "
                     "aytadi."),
                    (False, "had campaigned",
                     "past perfect ikkinchi o'tgan voqeani talab qiladi — "
                     "gapda u yo'q, va <em>now</em> bilan umuman mos "
                     "kelmaydi."),
                    (False, "campaigns",
                     "hozirgi zamon <em>for more than a decade</em> bilan "
                     "kelmaydi — davomiylik perfect talab qiladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Marie Tharp finished the first sheet of her ocean-floor map in 1957. "
                "By then she <span class=\"sr-blank\"></span> more than ten thousand "
                "separate depth soundings by hand, and she was not permitted aboard a "
                "research ship until 1965.</p>"),
            "choices": [
                {"text": "had plotted", "is_correct": True},
                {"text": "plotted", "is_correct": False},
                {"text": "has plotted", "is_correct": False},
                {"text": "plots", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Belgi:</strong> <em>By then</em> — bu "
                "<mark>ikki o'tgan voqeani tartibga soladi</mark>: xaritani "
                "tugatish (1957) va undan oldingi nuqta qo'yish "
                "ishi.</p>"
                "<p>Chizish tugatishdan <u>oldin</u> bo'lgan → past "
                "perfect.</p>"
                + why([
                    (True, "had plotted",
                     "past perfect: <em>By then</em> aniq belgi, va ish "
                     "1957-yilgi nuqtadan oldin bajarilgan."),
                    (False, "plotted",
                     "oddiy o'tgan zamon ikki voqeani bir vaqtga "
                     "qo'yadi va <em>By then</em> ning ma'nosini "
                     "yo'qotadi."),
                    (False, "has plotted",
                     "present perfect bugungacha yetadi; matn butunlay "
                     "o'tmishda, va Tharp ishi 1957-da tugagan."),
                    (False, "plots",
                     "hozirgi zamon."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The dye works closed in 1948 when the last of the family died "
                "without an apprentice. Its recipes "
                "<span class=\"sr-blank\"></span> in a book that nobody outside the "
                "household was allowed to open, and the book has never been "
                "found.</p>"),
            "choices": [
                {"text": "were kept", "is_correct": True},
                {"text": "had been kept", "is_correct": False},
                {"text": "have been kept", "is_correct": False},
                {"text": "are kept", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikkinchi o'tgan voqea bormi?</strong> "
                "Yopilish bor (1948), lekin retseptlarning saqlanishi "
                "undan <u>oldin</u> deb ko'rsatilmagan — matnda "
                "<em>by then · before · already</em> kabi tartiblovchi "
                "so'z yo'q.</p>"
                "<p>Demak past perfect ning sharti "
                "<mark>bajarilmagan</mark>: oddiy o'tgan zamon.</p>"
                + why([
                    (True, "were kept",
                     "oddiy o'tgan zamon, majhul nisbat. Tugagan "
                     "o'tmishdagi holat, tartiblovchi so'zsiz."),
                    (False, "had been kept",
                     "<strong>bu darsning bosh xatosi:</strong> past "
                     "perfect shartsiz ishlatilgan. Matn ikki voqeani "
                     "tartibga solmayapti — u shunchaki ketma-ket "
                     "hikoya qilyapti."),
                    (False, "have been kept",
                     "present perfect bugungacha davom etishni bildiradi; "
                     "korxona 1948-da yopilgan."),
                    (False, "are kept",
                     "hozirgi zamon — korxona yo'q."),
                ])
                + TIP.format(
                    "<strong>Past perfect ni shubha bilan qarang.</strong> "
                    "U «ko'proq o'tgan» degani emas va «rasmiyroq» ham "
                    "emas. U faqat <u>ikki o'tgan voqeani tartibga "
                    "solish</u> uchun. Tartiblovchi so'z "
                    "(<em>by the time · before · already · by then</em>) "
                    "yo'q bo'lsa, javob deyarli har doim oddiy "
                    "o'tgan zamon.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Fewer than eight hundred Mediterranean monk seals are thought to "
                "survive. The species <span class=\"sr-blank\"></span> on an open beach "
                "since the 1980s, and every birth recorded in the past twenty years has "
                "taken place inside a sea cave.</p>"),
            "choices": [
                {"text": "has not bred", "is_correct": True},
                {"text": "did not breed", "is_correct": False},
                {"text": "had not bred", "is_correct": False},
                {"text": "does not breed", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Belgi:</strong> <em>since the 1980s</em> — "
                "o‘tmishdan bugungacha cho‘zilgan holat. "
                "<mark>Present perfect.</mark></p>"
                "<p><strong>Tasdiq:</strong> gapning ikkinchi yarmi ham "
                "perfect — <em>every birth recorded in the past twenty "
                "years <u>has taken place</u></em>.</p>"
                + why([
                    (True, "has not bred",
                     "present perfect: <em>since</em> ning standart "
                     "juftligi, va holat bugun ham davom etyapti."),
                    (False, "did not breed",
                     "oddiy o‘tgan zamon <em>since</em> bilan kelmaydi: "
                     "u tugagan davrni bildiradi, <em>since</em> esa "
                     "bugungacha cho‘ziladi."),
                    (False, "had not bred",
                     "past perfect ikkinchi o‘tgan voqeani talab qiladi — "
                     "gapda tartiblovchi so‘z yo‘q."),
                    (False, "does not breed",
                     "hozirgi zamon <em>since</em> bilan ishlamaydi — "
                     "u davomiylikni ko‘rsatmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">past perfect (had + V3)</div><div class="pp-card-back">ikki o\'tgan voqeaning ertarog\'i</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">present perfect (has/have + V3)</div><div class="pp-card-back">o\'tmishda boshlanib bugungacha davom etgan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">by the time / by then</div><div class="pp-card-back">~ ga kelib (past perfect belgisi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">since / for</div><div class="pp-card-back">~ dan beri / ~ davomida (present perfect belgisi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a depth sounding</div><div class="pp-card-back">chuqurlik o\'lchovi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to campaign for ~</div><div class="pp-card-back">~ uchun kurash olib bormoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an apprentice</div><div class="pp-card-back">shogird</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to tar over</div><div class="pp-card-back">asfalt bilan yopib tashlamoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Past perfect:</strong> matnda ikkita o'tgan "
              "voqea bor va bu ertarog'i.</li>"
              "<li><strong>Present perfect:</strong> bugungacha davom "
              "etgan — <em>since · for · over the past</em>.</li>"
              "<li>Tartiblovchi so'z yo'q bo'lsa, past perfect "
              "<u>xato</u>: oddiy o'tgan zamon.</li>"
              "<li><strong>Aniq sana + present perfect = xato</strong> "
              "(52-dars).</li>"
              "<li>Perfect «rasmiyroq» degani emas — u shartli "
              "shakl.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 54
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W54: Non-Finite Forms — -ing, to + verb, and the Missing Main Verb",
    "summary": "Sifatdosh va infinitiv kesim bo'lolmaydi. SAT ularni asosiy fe'l "
               "o'rniga qo'yib, butun gapni fragmentga aylantiradi.",
    "order": 54,
    "blocks": [
        {"rich_text": (
            "<h2>Gapga bitta shaxsli kesim kerak</h2>"
            "<p>Bu dars W33'dagi fragment mavzusini fe'l tomonidan "
            "ko'radi. Qoida bir xil:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Har gapda "
                "kamida bitta shaxsli kesim bo'lishi shart. "
                "<em>-ing</em>, <em>to + fe'l</em> va sifatdosh — kesim "
                "emas.</strong></p>")
            + "<p>SAT bu qoidani tanish shaklda sinaydi: bo'sh joyda "
            "gapning <mark>yagona kesimi</mark> turadi, va uch variant "
            "uni shaxlsiz shakl bilan almashtiradi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✓ <em>The dome <strong>rests</strong> "
                "on eight piers.</em><br>"
                "✗ <em>The dome <strong>resting</strong> on eight "
                "piers.</em> — gap emas<br>"
                "✗ <em>The dome <strong>to rest</strong> on eight "
                "piers.</em> — gap emas<br>"
                "✗ <em>The dome, <strong>having rested</strong> on eight "
                "piers.</em> — gap emas</p>")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki tomonlama tekshiruv</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Gapda boshqa shaxsli "
              "kesim bormi?</strong> Bo'lsa — bo'sh joyga sifatdosh "
              "kelishi <u>mumkin</u> (u qo'shimcha bo'lak "
              "yasaydi).</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Bo'lmasa</strong> — "
              "bo'sh joyga <u>albatta</u> shaxsli kesim kerak, aks holda "
              "butun gap fragment bo'lib qoladi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Nisbiy gap ichidagi "
              "fe'lni sanamang.</strong> <em>The manuscript "
              "<u>that the conservator found</u> …</em> — "
              "<em>found</em> nisbiy gapga tegishli, asosiy kesim "
              "hali kerak.</p></div>"
            + '</div>'
            + WARN.format(
                "<em>-ing</em> shakli o'z-o'zicha yomon emas. "
                "<em>The dome, <u>rebuilt twice</u>, still stands</em> — "
                "bu to'g'ri, chunki <em>stands</em> asosiy kesim. "
                "Savol har doim bitta: <strong>gapda shaxsli kesim "
                "bormi?</strong>")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>Espaliered fruit trees, trained flat against a wall and pruned every "
                "winter to a single plane so that no branch shades another, "
                "<span class=\"sr-blank\"></span> fruit in climates where the same "
                "variety grown free-standing would not ripen at all.</p>")
            + choices_html([
                "ripening",
                "ripen",
                "to ripen",
                "having ripened",
            ])
            + "<p><strong>1-qadam — gapda boshqa shaxsli kesim bormi?</strong> "
            "<em>trained</em> va <em>pruned</em> — sifatdosh, kesim emas. "
            "<em>shades</em> — <em>so that</em> ergash gapiga tegishli. "
            "<em>would not ripen</em> — <em>where</em> ergash gapiga "
            "tegishli.</p>"
            "<p>Asosiy gapning kesimi <mark>yo'q</mark> — u bo'sh joyda "
            "bo'lishi kerak.</p>"
            "<p><strong>Ega:</strong> <em>Espaliered fruit trees</em> — "
            "ko'plik.</p>"
            + why([
                (True, "ripen",
                 "shaxsli kesim, ko'plik shaklda. Endi gapda asosiy kesim "
                 "bor va u egaga mos."),
                (False, "ripening",
                 "<em>-ing</em> kesim emas — butun gap fragment "
                 "bo'lib qoladi. Va u vergullar orasidagi uzun "
                 "qo'shimchadan keyin ayniqsa jozibali "
                 "ko'rinadi."),
                (False, "to ripen",
                 "infinitiv ham kesim emas."),
                (False, "having ripened",
                 "sifatdoshning perfect shakli — yana kesim emas, va "
                 "ma'nosi ham noto'g'ri (ular hali pishmagan)."),
            ])
            + NOTE.format(
                "Bu gapda <u>uchta</u> fe'lsimon so'z bor "
                "(<em>trained · pruned · shades</em>) va yana bittasi "
                "ergash gapda (<em>would not ripen</em>). Ularning "
                "birortasi ham <strong>asosiy</strong> kesim emas — "
                "shuning uchun bo'sh joy uni bermasa, gap "
                "yiqiladi.")
        )},

        {
            "rich_text": conv_q(
                "<p>The fire that swept through the palace in about 1200 BCE, destroying "
                "the roof and bringing down two of the four walls, "
                "<span class=\"sr-blank\"></span> the clay tablets in the archive room "
                "hard enough to survive three thousand years in the ground.</p>"),
            "choices": [
                {"text": "baked", "is_correct": True},
                {"text": "baking", "is_correct": False},
                {"text": "to bake", "is_correct": False},
                {"text": "having baked", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshqa kesim bormi?</strong> <em>swept</em> — "
                "<em>that</em> nisbiy gapiga tegishli. <em>destroying</em> "
                "va <em>bringing</em> — sifatdosh. "
                "<mark>Asosiy kesim yo'q.</mark></p>"
                "<p><strong>Ega:</strong> <em>The fire</em> — birlik.</p>"
                + why([
                    (True, "baked",
                     "shaxsli kesim, o'tgan zamon — matnning zamoniga "
                     "(<em>swept · destroying</em>) mos."),
                    (False, "baking",
                     "sifatdosh — gap fragment bo'lib qoladi. Bu "
                     "variant ayniqsa jozibali, chunki gapda allaqachon "
                     "ikkita <em>-ing</em> bor."),
                    (False, "to bake",
                     "infinitiv kesim emas."),
                    (False, "having baked",
                     "yana sifatdosh shakli."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Sled dogs pull best well below freezing, and a team entered in mild "
                "weather begins to overheat within hours, "
                "<span class=\"sr-blank\"></span> the longest races to February and "
                "March rather than to the end of the season.</p>"),
            "choices": [
                {"text": "confining", "is_correct": True},
                {"text": "confines", "is_correct": False},
                {"text": "confine", "is_correct": False},
                {"text": "is confined", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol qoidani <u>teskari tomondan</u> sinaydi. "
                "<strong>Gapda kesim bormi?</strong> Ha, ikkita: "
                "<em>pull</em> va <em>begins</em>. Ikkala mustaqil gap "
                "<em>and</em> bilan ulangan.</p>"
                "<p>Demak bo'sh joyga <mark>yana bir kesim kerak "
                "emas</mark> — u uchinchi mustaqil gap yasab, vergul "
                "splaysini keltirib chiqarardi (W31).</p>"
                + why([
                    (True, "confining",
                     "sifatdosh bo'lagi: vergul bilan ulanadi va "
                     "oldingi gapning oqibatini bildiradi. Yangi gap "
                     "yasamaydi."),
                    (False, "confines",
                     "shaxsli kesim → vergul bilan ulangan uchinchi "
                     "mustaqil gap → <strong>vergul splaysi</strong>."),
                    (False, "confine",
                     "yana shaxsli kesim, va ustiga son ham noto'g'ri."),
                    (False, "is confined",
                     "shaxsli kesim va majhul nisbat — <em>the longest "
                     "races</em> to'ldiruvchisi bilan mos kelmaydi."),
                ])
                + TIP.format(
                    "Savol har doim bitta: <strong>gapda allaqachon "
                    "shaxsli kesim bormi?</strong> Yo'q bo'lsa — bo'sh "
                    "joyga kesim kerak. Bor bo'lsa — ko'pincha "
                    "<u>sifatdosh</u> kerak, chunki ikkinchi kesim "
                    "splays yasaydi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The society that was founded in 1931 to record every surviving "
                "watermill in the county before the last of them was pulled down "
                "<span class=\"sr-blank\"></span> photographs of one hundred and "
                "forty-two mills, of which fewer than twenty are still standing.</p>"),
            "choices": [
                {"text": "holds", "is_correct": True},
                {"text": "holding", "is_correct": False},
                {"text": "hold", "is_correct": False},
                {"text": "to hold", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kesim bormi?</strong> <em>was founded</em> — "
                "<em>that</em> nisbiy gapiga tegishli. <em>was pulled "
                "down</em> — <em>before</em> ergash gapiga tegishli. "
                "<em>to record</em> — infinitiv. "
                "<mark>Asosiy kesim yo'q.</mark></p>"
                "<p><strong>Ega:</strong> <em>The society</em> — birlik "
                "(nisbiy gap uni fe'ldan o'n uch so'z "
                "uzoqlashtiradi).</p>"
                + why([
                    (True, "holds",
                     "shaxsli kesim, birlik. Ikkala talab ham: gapga "
                     "kesim beradi va egaga mos keladi."),
                    (False, "hold",
                     "kesim, lekin ko'plik — <em>mills</em> yoki "
                     "<em>them</em> ga moslashgan (W50)."),
                    (False, "holding",
                     "sifatdosh — gap fragment bo'lib qoladi."),
                    (False, "to hold",
                     "infinitiv — yana kesim emas."),
                ])
                + NOTE.format(
                    "Bu savol ikki mavzuni birga sinaydi: "
                    "<strong>shaxsli kesim</strong> (54-dars) va "
                    "<strong>ega-kesim moslashuvi</strong> (50-dars). "
                    "Imtihonda shunday bo'ladi — ikki variant "
                    "kesim bo'lmagani uchun, bittasi son bo'yicha "
                    "tushadi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p><span class=\"sr-blank\"></span> the surface of the wing so that air "
                "stays attached to it a fraction of a second longer, the comb-like ridges "
                "along the leading feathers of an owl reduce the noise of its flight to a "
                "level no other bird of comparable size can match.</p>"),
            "choices": [
                {"text": "Roughening", "is_correct": True},
                {"text": "Roughens", "is_correct": False},
                {"text": "They roughen", "is_correct": False},
                {"text": "It roughens", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joy gapning <mark>boshida</mark>, vergulgacha. "
                "Verguldan keyin to'liq gap turibdi: ega <em>the "
                "comb-like ridges</em>, kesim <em>reduce</em>.</p>"
                "<p>Demak gapda asosiy kesim allaqachon bor — boshidagi "
                "bo'lak faqat <strong>sifatdosh bo'lagi</strong> "
                "bo'lishi mumkin.</p>"
                + why([
                    (True, "Roughening",
                     "sifatdosh bo'lagi. U verguldan keyingi egani "
                     "(<em>the ridges</em>) izohlaydi — aynan qirralar "
                     "yuzani g'adir-budur qiladi."),
                    (False, "Roughens",
                     "shaxsli kesim, lekin egasi yo'q — bo'lak o'zi "
                     "gap bo'lolmaydi va vergul bilan ham "
                     "ulanmaydi."),
                    (False, "They roughen",
                     "ega + kesim = mustaqil gap. Vergul bilan ikkinchi "
                     "mustaqil gapga ulansa — <strong>vergul "
                     "splaysi</strong> (W31)."),
                    (False, "It roughens",
                     "yana mustaqil gap, ustiga <em>it</em> ko'plikdagi "
                     "<em>ridges</em> ga ishora qilolmaydi."),
                ])
                + TIP.format(
                    "Gap boshidagi bo'sh joy + verguldan keyin to'liq "
                    "gap = deyarli har doim <strong>-ing yoki "
                    "sifatdosh</strong>. Va u verguldan keyingi "
                    "<u>egani</u> izohlashi shart (W74'dagi osilib "
                    "qolgan aniqlovchi).")
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a finite verb</div><div class="pp-card-back">shaxsli kesim (zamon ko\'rsatadi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a non-finite form</div><div class="pp-card-back">shaxssiz shakl (-ing, to + fe\'l, sifatdosh)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a participial phrase</div><div class="pp-card-back">sifatdosh bo\'lagi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to espalier</div><div class="pp-card-back">devorga yassilab o\'stirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">free-standing</div><div class="pp-card-back">alohida, tayanchsiz turgan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to confine ~ to …</div><div class="pp-card-back">~ ni … bilan cheklamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to sweep through</div><div class="pp-card-back">(yong\'in) yoyilib o\'tmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to pull down</div><div class="pp-card-back">buzmoq, qulatmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Har gapda kamida <strong>bitta shaxsli kesim</strong> "
              "bo'lishi shart.</li>"
              "<li><em>-ing · to + fe'l · sifatdosh</em> kesim "
              "emas.</li>"
              "<li>Nisbiy gap va ergash gap ichidagi fe'lni "
              "<u>sanamang</u>.</li>"
              "<li>Gapda kesim <u>bor</u> bo'lsa — bo'sh joyga ko'pincha "
              "<strong>sifatdosh</strong> kerak, aks holda splays.</li>"
              "<li>Kesim tanlagach, <strong>sonini ham tekshiring</strong> "
              "(50-dars).</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 55
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_VERBS,
    "title": "SAT R&W W55: Verbs — Mixed Practice",
    "summary": "Olti savol, oltitasi ham aralash: ega qayerda, zamon qaysi, "
               "bo'sh joyga shaxsli kesim kerakmi. Har biri imtihon uzunligida.",
    "order": 55,
    "blocks": [
        {"rich_text": (
            "<h2>Aralash mashq</h2>"
            "<p>50-54-darslar bitta-bittadan o'rgatdi. Imtihonda esa "
            "savol o'z turini aytmaydi — shuning uchun bu yerda oltitasi "
            "aralash keladi.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Variantlar bir-biridan "
              "nima bilan farq qiladi?</strong> Son bilanmi "
              "(<em>was/were</em>) — moslashuv savoli. Zamon bilanmi "
              "(<em>has/had/will have</em>) — vaqt savoli. "
              "Shaxslilik bilanmi (<em>holds/holding</em>) — kesim "
              "savoli.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Moslashuv bo'lsa</strong> — "
              "old ko'makchili bo'laklarni o'chirib, haqiqiy egani "
              "toping.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Zamon bo'lsa</strong> — "
              "abzatsdagi <u>boshqa</u> fe'llarni va vaqt so'zlarini "
              "(<em>in 1904 · since · by the time</em>) "
              "o'qing.</p></div>"
            + "<div class=\"pp-step\"><p><strong>4. Shaxslilik bo'lsa</strong> — "
              "gapda boshqa asosiy kesim bormi? Yo'q bo'lsa kesim "
              "kerak, bor bo'lsa sifatdosh.</p></div>"
            + '</div>'
            + '<span class="sr-time">⏱ 6 savol · ~7 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Moslashuv") + conv_q(
                "<p>The collection of seed samples that the institute keeps in a tunnel "
                "cut into a frozen mountainside on an island north of the Arctic Circle "
                "<span class=\"sr-blank\"></span> duplicates of crops held in more than "
                "seventeen hundred smaller banks around the world.</p>"),
            "choices": [
                {"text": "contains", "is_correct": True},
                {"text": "contain", "is_correct": False},
                {"text": "have contained", "is_correct": False},
                {"text": "were containing", "is_correct": False},
            ],
            "explanation": (
                "<p>Old ko'makchili bo'laklarni o'chiring: <em>The "
                "collection</em> <s>of seed samples</s> <s>that the "
                "institute keeps…</s> <s>into a frozen "
                "mountainside</s> <s>on an island</s> <s>north of the "
                "Arctic Circle</s>.</p>"
                "<p>Qoladi: <mark>The collection … contains</mark> — "
                "birlik.</p>"
                + why([
                    (True, "contains",
                     "birlik, hozirgi zamon — <em>keeps</em> bilan bir "
                     "vaqtda."),
                    (False, "contain",
                     "ko'plik — eng yaqin ot <em>samples</em> yoki "
                     "<em>banks</em> ga moslashib qolgan (W51)."),
                    (False, "have contained",
                     "ko'plik yordamchi fe'l, va perfect zamon uchun "
                     "hech qanday asos yo'q."),
                    (False, "were containing",
                     "davomli o'tgan zamon — <em>contain</em> holat "
                     "fe'li, davomli shaklda ishlatilmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Zamon") + conv_q(
                "<p>Radiocarbon dating gave the wooden posts a date of about 800 BCE, but "
                "the pottery lying beside them belonged to a style that potters in the "
                "region <span class=\"sr-blank\"></span> two centuries earlier. The "
                "excavators concluded that the posts had been driven through an older "
                "layer.</p>"),
            "choices": [
                {"text": "had abandoned", "is_correct": True},
                {"text": "have abandoned", "is_correct": False},
                {"text": "abandon", "is_correct": False},
                {"text": "will have abandoned", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikki o'tgan voqea: sopol uslubi <u>tashlab "
                "yuborilgan</u> — keyin ustunlar qo'yilgan (800-yil). "
                "Oldingisi uchun <mark>past perfect</mark> (W53).</p>"
                "<p><em>two centuries earlier</em> — aynan shu "
                "belgi: o'tgan nuqtadan <u>oldinroq</u>.</p>"
                + why([
                    (True, "had abandoned",
                     "past perfect: o'tgan zamondagi nuqtadan oldingi "
                     "ish."),
                    (False, "have abandoned",
                     "present perfect hozirga bog'laydi — bu yerda "
                     "hamma narsa tugagan o'tmishda."),
                    (False, "abandon",
                     "hozirgi zamon — miloddan avvalgi kulollar hozir "
                     "hech narsa qilmayapti."),
                    (False, "will have abandoned",
                     "kelasi zamon — abzatsda hech qanday kelajak "
                     "yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Shaxsli kesim") + conv_q(
                "<p>A bridge whose deck is hung from cables that pass over two towers and "
                "are anchored in blocks of concrete at either end "
                "<span class=\"sr-blank\"></span> far less material than a bridge of the "
                "same span carried on arches.</p>"),
            "choices": [
                {"text": "requires", "is_correct": True},
                {"text": "requiring", "is_correct": False},
                {"text": "to require", "is_correct": False},
                {"text": "require", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Asosiy kesim bormi?</strong> <em>is hung</em>, "
                "<em>pass</em>, <em>are anchored</em> — hammasi "
                "<em>whose</em> va <em>that</em> nisbiy gaplariga "
                "tegishli. <em>carried</em> — sifatdosh. "
                "<mark>Asosiy kesim yo'q.</mark></p>"
                "<p><strong>Ega:</strong> <em>A bridge</em> — "
                "birlik.</p>"
                + why([
                    (True, "requires",
                     "shaxsli kesim va birlik — ikkala shart ham "
                     "bajarildi."),
                    (False, "require",
                     "kesim, lekin ko'plik: <em>cables</em>, "
                     "<em>towers</em> yoki <em>blocks</em> ga "
                     "moslashib qolgan."),
                    (False, "requiring",
                     "sifatdosh — butun gap fragmentga aylanadi."),
                    (False, "to require",
                     "infinitiv — yana kesim emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Sifatdosh") + conv_q(
                "<p>Sourdough rises without commercial yeast, and the wild organisms that "
                "raise it also acidify the dough as they work, "
                "<span class=\"sr-blank\"></span> the loaf a keeping quality that a "
                "yeasted bread of the same flour does not have.</p>"),
            "choices": [
                {"text": "giving", "is_correct": True},
                {"text": "gives", "is_correct": False},
                {"text": "give", "is_correct": False},
                {"text": "it gives", "is_correct": False},
            ],
            "explanation": (
                "<p>Gapda ikkita mustaqil gap bor: <em>Sourdough "
                "rises…</em> <strong>and</strong> <em>the wild "
                "organisms … acidify…</em>. Uchinchisiga o'rin "
                "yo'q — verguldan keyin faqat "
                "<mark>sifatdosh</mark> kelishi mumkin.</p>"
                + why([
                    (True, "giving",
                     "sifatdosh bo'lagi: oldingi gapning natijasini "
                     "bildiradi, yangi gap yasamaydi."),
                    (False, "gives",
                     "shaxsli kesim, egasi yo'q — bo'lak "
                     "osilib qoladi."),
                    (False, "give",
                     "yana kesim, va son ham noto'g'ri."),
                    (False, "it gives",
                     "ega + kesim = uchinchi mustaqil gap, faqat "
                     "vergul bilan ulangan → <strong>vergul "
                     "splaysi</strong>."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Moslashuv") + conv_q(
                "<p>Neither the two surviving letters nor the ledger kept by the workshop "
                "<span class=\"sr-blank\"></span> a price for the altarpiece, so how much "
                "the guild actually paid for it remains unknown.</p>"),
            "choices": [
                {"text": "records", "is_correct": True},
                {"text": "record", "is_correct": False},
                {"text": "have recorded", "is_correct": False},
                {"text": "were recording", "is_correct": False},
            ],
            "explanation": (
                "<p><em>Neither … nor …</em> qurilishida fe'l "
                "<mark>o'ziga eng yaqin turgan ot</mark> bilan "
                "moslashadi. Eng yaqini — <em>the ledger</em>, "
                "birlik.</p>"
                + why([
                    (True, "records",
                     "birlik — <em>the ledger</em> ga mos, chunki u "
                     "fe'lga yaqinroq."),
                    (False, "record",
                     "ko'plik — <em>letters</em> ga qarab tanlangan, "
                     "lekin u <em>neither</em> tomonida, fe'ldan "
                     "uzoqda."),
                    (False, "have recorded",
                     "ko'plik yordamchi, va perfect zamon uchun asos "
                     "yo'q."),
                    (False, "were recording",
                     "ko'plik va davomli o'tgan zamon — ikkalasi ham "
                     "noto'g'ri."),
                ])
                + NOTE.format(
                    "Xuddi shu qoida <em>either … or …</em> va "
                    "<em>not only … but also …</em> uchun ham "
                    "ishlaydi: <strong>fe'l yaqin tomonga "
                    "qaraydi</strong>.")
            ),
        },

        {
            "rich_text": qnum(6, "Zamon") + conv_q(
                "<p>The observatory has kept an unbroken record of sunspot counts since "
                "1874. Because the instrument and the observing routine "
                "<span class=\"sr-blank\"></span> essentially unchanged since the very "
                "first count was made, the series is one of the few in astronomy "
                "that can be compared directly across its whole span.</p>"),
            "choices": [
                {"text": "have remained", "is_correct": True},
                {"text": "remained", "is_correct": False},
                {"text": "had remained", "is_correct": False},
                {"text": "will remain", "is_correct": False},
            ],
            "explanation": (
                "<p>Birinchi gap <em>has kept … since 1874</em> "
                "deydi — ish o'tmishda boshlanib "
                "<mark>hozirgacha davom etmoqda</mark>. Ikkinchi gap "
                "ham xuddi shu davrni tasvirlaydi "
                "(<em>since the very first count</em>).</p>"
                "<p>Bu — present perfect belgisining o'zi (W53).</p>"
                + why([
                    (True, "have remained",
                     "present perfect: o'tmishda boshlanib bugungacha "
                     "davom etadi — <em>since …</em> va birinchi "
                     "gapdagi <em>has kept</em> bilan mos."),
                    (False, "remained",
                     "oddiy o'tgan zamon — asbob endi o'zgargandek "
                     "eshitiladi, matn esa aksini aytadi."),
                    (False, "had remained",
                     "past perfect uchun ikkinchi, keyinroq turgan "
                     "o'tgan voqea kerak — bu yerda unday voqea "
                     "yo'q."),
                    (False, "will remain",
                     "kelasi zamon — <em>since …</em> o'tmishdan "
                     "bugungacha bo'lgan davrni bildiradi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Mavzu yakuni — Fe'l shakllari</h3>"
            "<p>Variantlar orasidagi farq sizga savol turini "
            "aytadi:</p>"
            "<ul>"
            "<li><em>contains / contain</em> → <strong>moslashuv</strong>: "
            "old ko'makchili bo'laklarni o'chiring, haqiqiy egani "
            "toping (W50, W51).</li>"
            "<li><em>had abandoned / have abandoned / abandoned</em> → "
            "<strong>zamon</strong>: abzatsdagi vaqt so'zlarini va "
            "boshqa fe'llarni o'qing (W52, W53).</li>"
            "<li><em>requires / requiring</em> → <strong>shaxsli "
            "kesim</strong>: gapda boshqa asosiy kesim bormi "
            "(W54).</li>"
            "</ul>"
            + TIP.format(
                "Ikki so'rov ko'pincha bitta savolda birga keladi: "
                "avval shaxssiz shakllarni chiqarib tashlang, keyin "
                "qolgan ikkitasidan <u>sonini</u> tanlang. Shu "
                "tartib deyarli har doim ishlaydi.")
            + "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to acidify</div><div class="pp-card-back">nordonlashtirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ledger</div><div class="pp-card-back">hisob daftari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an altarpiece</div><div class="pp-card-back">mehrob ustidagi rasm</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a span (bridge)</div><div class="pp-card-back">oraliq, ochiq masofa</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to anchor</div><div class="pp-card-back">mahkamlamoq, langar solmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a keeping quality</div><div class="pp-card-back">uzoq saqlanish xususiyati</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unbroken</div><div class="pp-card-back">uzluksiz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to excavate</div><div class="pp-card-back">qazishma ishlarini olib bormoq</div></div>'
            + "</div>"
        )},
    ],
},
]
