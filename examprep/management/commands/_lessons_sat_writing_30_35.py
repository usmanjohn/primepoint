# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 30-35.

"Gap chegaralari (Boundaries — sentence boundaries)" — the first half of the
Standard English Conventions domain and the single most tested thing in it.

Every question here is decided by ONE test, set up in W3: is each side of the
blank an independent clause? Get that right and the punctuation follows from a
four-row table. Three of the four choices always break a nameable rule.

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

TOPIC_BOUND = {
    "title":   "Gap chegaralari (Boundaries — sentence boundaries)",
    "summary": "Gapni qayerda tugatish va ikki bo'lakni qanday bog'lash: vergul, "
               "nuqta, nuqtali vergul va bog'lovchilarning qat'iy qoidalari.",
    "icon":    "bi-slash-square",
    "order":   4,
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
# Writing 30
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W30: Independent Clause, Dependent Clause, and Why It Decides the Punctuation",
    "summary": "Butun mavzuning yagona savoli: bo'sh joyning har ikki tomoni mustaqil "
               "gapmi? Javob to'rt qatorli jadvaldan chiqadi.",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta savol, to'rt javob</h2>"
            "<p><strong>Boundaries</strong> — Standard English Conventions "
            "domenining eng katta bo'lagi va imtihonda eng ko'p "
            "sinaladigan grammatik mavzu. Yaxshi yangilik shuki, u "
            "<mark>bitta savolga</mark> qisqaradi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Bo'sh joyning "
                "chap tomoni mustaqil gapmi? O'ng tomoni-chi?</strong></p>")
            + "<p>Javobga qarab to'rt holat chiqadi, va har holatda "
            "ruxsat etilgan belgilar aniq. Bu qoida, did emas — shuning "
            "uchun bu savollarda ikkilanish bo'lmasligi kerak.</p>"
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Mustaqil gap nima?</h3>"
            "<p><strong>Mustaqil gap</strong> (independent clause) — "
            "o'zi yolg'iz turib to'liq gap bo'la oladigan bo'lak. "
            "Unda ikki narsa bo'lishi shart:</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Ega</strong> — kim yoki "
              "nima. <em>The dam · She · Three surveys</em>.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Shaxsli kesim</strong> "
              "(finite verb) — zamon ko'rsatadigan fe'l. "
              "<em>was · collapsed · have shown</em>.</p>"
              "<p>⚠️ <em>-ing</em> va <em>to + fe'l</em> shakllari "
              "<u>kesim emas</u>: <em>the dam collapsing</em>, "
              "<em>the dam to collapse</em> — ikkovi ham gap emas.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Va boshida "
              "bo'ysundiruvchi so'z bo'lmasin.</strong> "
              "<em>Because · Although · When · If · Since · While · After · "
              "Before · Unless · Whereas</em> — bu so'zlardan biri "
              "qo'shilsa, gap <u>ergash gapga</u> aylanadi va yolg'iz "
              "turolmaydi.</p></div>"
            + '</div>'
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The bridge was closed.</em> — "
                "mustaqil ✓<br>"
                "<em>Because the bridge was closed.</em> — ergash ✗ "
                "(bir so'z qo'shildi, gap yo'qoldi)<br>"
                "<em>The bridge closing.</em> — gap emas ✗ (shaxsli kesim "
                "yo'q)</p>")
        )},

        {"rich_text": (
            "<h3>To'rt qatorli jadval</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Chap</th><th>O'ng</th><th>Ruxsat etilgan</th>"
              "<th>Taqiqlangan</th></tr></thead>"
              "<tbody>"
              "<tr><td>mustaqil</td><td>mustaqil</td>"
              "<td><strong>.</strong> · <strong>;</strong> · "
              "<strong>,</strong> + <em>and/but/so/or/yet/for/nor</em></td>"
              "<td>yolg'iz vergul · belgisiz</td></tr>"
              "<tr><td>mustaqil</td><td>ergash yoki bo'lak</td>"
              "<td><strong>,</strong> · <strong>:</strong> · "
              "<strong>—</strong></td>"
              "<td><strong>;</strong> · <strong>.</strong></td></tr>"
              "<tr><td>ergash</td><td>mustaqil</td>"
              "<td><strong>,</strong></td>"
              "<td><strong>;</strong> · <strong>:</strong> · "
              "<strong>.</strong></td></tr>"
              "<tr><td>bo'lak</td><td>bo'lak</td>"
              "<td>odatda belgisiz</td><td>deyarli hammasi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Birinchi qator imtihonda eng ko'p uchraydi, va uning "
                "«taqiqlangan» ustuni bitta xatoni nomlaydi: "
                "<strong>vergul splaysi</strong>. U 31-darsning butun "
                "mavzusi va bu domendagi eng ko'p sinaladigan xato.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The salt marsh behind the sea wall was drained for pasture in the "
                "1840s and has been grazed ever since. Recent surveys have found the "
                "ground behind the wall sinking about a centimetre a "
                "<span class=\"sr-blank\"></span> the marsh outside it, still flooded "
                "twice a day, has risen slightly over the same period.</p>")
            + choices_html([
                "year, while",
                "year, ",
                "year while",
                "year; while",
            ])
            + "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Recent surveys "
            "have found the ground behind the wall sinking about a centimetre "
            "a year</em> — ega (<em>surveys</em>), kesim "
            "(<em>have found</em>): <mark>mustaqil</mark>.</p>"
            "<p>O'ng: <em>while the marsh outside it … has risen slightly</em> "
            "— <em>while</em> bo'ysundiruvchi so'z, shuning uchun bu "
            "<mark>ergash gap</mark>.</p>"
            "<p><strong>Mustaqil + ergash</strong> → jadvalning ikkinchi "
            "qatori: vergul, ikki nuqta yoki tire. Nuqtali vergul va nuqta "
            "taqiqlangan.</p>"
            + why([
                (True, "year, while",
                 "vergul + ergash gap. Ikkinchi qatorning aynan yechimi, va "
                 "<em>while</em> qarama-qarshilikni ham to'g'ri "
                 "bildiradi."),
                (False, "year; while",
                 "<strong>nuqtali vergul ikki mustaqil gap orasida "
                 "bo'ladi.</strong> O'ng tomon <em>while</em> bilan "
                 "boshlangani uchun mustaqil emas — nuqtali vergul "
                 "taqiqlangan."),
                (False, "year, ",
                 "vergul o'zi to'g'ri, lekin <em>while</em> tushib qolgan — "
                 "unda o'ng tomon mustaqil gapga aylanadi va biz "
                 "<strong>vergul splaysi</strong>ga tushamiz."),
                (False, "year while",
                 "belgisiz: uzun ergash gap oldidan vergul kerak. Bu "
                 "yerda vergulsiz gap o'qib bo'lmaydigan holga keladi."),
            ])
            + NOTE.format(
                "E'tibor bering: to'rtala variant ham <u>bir xil "
                "so'zlardan</u> tuzilgan. Faqat vergul va "
                "<em>while</em> o'ynaydi. Bu Conventions savollarining "
                "odatiy ko'rinishi — va shuning uchun variantlar "
                "orasidagi farq savolning mavzusini darrov "
                "aytadi (W1).")
        )},

        {
            "rich_text": conv_q(
                "<p>Glass sponges build skeletons of silica in water close to freezing, "
                "and a single specimen from the deep North Pacific has been dated at "
                "well over a thousand <span class=\"sr-blank\"></span> making it among "
                "the longest-lived animals known.</p>"),
            "choices": [
                {"text": "years,", "is_correct": True},
                {"text": "years;", "is_correct": False},
                {"text": "years.", "is_correct": False},
                {"text": "years", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Glass sponges "
                "build … and a single specimen … has been dated at well over "
                "a thousand years</em> — mustaqil.</p>"
                "<p>O'ng: <em>making it among the longest-lived animals "
                "known</em> — <mark>gap emas</mark>. <em>making</em> — "
                "<em>-ing</em> shakli, shaxsli kesim emas, va ega ham "
                "yo'q.</p>"
                "<p><strong>Mustaqil + bo'lak</strong> → vergul.</p>"
                + why([
                    (True, "years,",
                     "vergul <em>-ing</em> bilan boshlangan qo'shimcha "
                     "bo'lakni asosiy gapga ulaydi. Jadvalning ikkinchi "
                     "qatori."),
                    (False, "years;",
                     "nuqtali vergul ikki <u>mustaqil</u> gap talab qiladi. "
                     "<em>making…</em> mustaqil emas."),
                    (False, "years.",
                     "nuqta ham ikki mustaqil gap talab qiladi. Bu yerda u "
                     "<strong>fragment</strong> yasaydi: "
                     "<em>Making it among the longest-lived animals "
                     "known.</em> — kesimi yo'q."),
                    (False, "years",
                     "belgisiz: <em>-ing</em> bo'lagi oldidan vergul "
                     "qo'yiladi, aks holda u <em>a thousand years</em> ga "
                     "yopishib, boshqa ma'no beradi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Although the manuscript had been catalogued in 1907 and shelved "
                "under the wrong century for eighty <span class=\"sr-blank\"></span> "
                "the librarian who rediscovered it recognised the hand within "
                "minutes.</p>"),
            "choices": [
                {"text": "years,", "is_correct": True},
                {"text": "years;", "is_correct": False},
                {"text": "years", "is_correct": False},
                {"text": "years:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: "
                "<em><u>Although</u> the manuscript had been catalogued … for "
                "eighty years</em> — <em>Although</em> bo'ysundiruvchi "
                "so'z, demak butun bo'lak <mark>ergash gap</mark>.</p>"
                "<p>O'ng: <em>the librarian … recognised the hand within "
                "minutes</em> — mustaqil.</p>"
                "<p><strong>Ergash + mustaqil</strong> → jadvalning uchinchi "
                "qatori: <u>faqat vergul</u>.</p>"
                + why([
                    (True, "years,",
                     "boshda kelgan ergash gapdan keyin vergul — bu qat'iy "
                     "qoida (34-dars)."),
                    (False, "years;",
                     "nuqtali vergul chap tomondan mustaqil gap talab "
                     "qiladi. <em>Although</em> uni ergashga "
                     "aylantirgan."),
                    (False, "years:",
                     "ikki nuqtadan <u>oldin</u> ham to'liq gap turishi "
                     "shart. Bu yerda turmaydi."),
                    (False, "years",
                     "belgisiz: boshda kelgan ergash gap vergulsiz asosiy "
                     "gapga yopishib qoladi."),
                ])
                + TIP.format(
                    "Gapning <u>birinchi so'zi</u>ga qarang. "
                    "<em>Although · Because · When · If · Since · While · "
                    "After · Unless</em> bilan boshlangan gapda chap tomon "
                    "deyarli har doim <strong>ergash</strong> bo'ladi — va "
                    "javob vergul.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The engineer who designed the roof had never built anything larger "
                "than a barn, and the commission came to her only because two better-"
                "known firms had turned it <span class=\"sr-blank\"></span> the span she "
                "proposed was wider than any then standing in the country.</p>"),
            "choices": [
                {"text": "down;", "is_correct": True},
                {"text": "down,", "is_correct": False},
                {"text": "down", "is_correct": False},
                {"text": "down, and;", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>The engineer … "
                "had never built … and the commission came to her only because "
                "two better-known firms had turned it down</em> — mustaqil "
                "(ichida ergash gap bor, lekin butun bo'lak o'zi "
                "turadi).</p>"
                "<p>O'ng: <em>the span she proposed was wider than any then "
                "standing in the country</em> — ega (<em>the span</em>), "
                "kesim (<em>was</em>): <mark>mustaqil</mark>.</p>"
                "<p><strong>Mustaqil + mustaqil</strong> → birinchi qator: "
                "nuqta, nuqtali vergul yoki vergul + bog'lovchi.</p>"
                + why([
                    (True, "down;",
                     "nuqtali vergul ikki mustaqil gapni ulashning "
                     "qonuniy usuli, va u ikki fikrning zich bog'liqligini "
                     "ham saqlaydi."),
                    (False, "down,",
                     "<strong>vergul splaysi</strong> — bu domendagi eng "
                     "ko'p sinaladigan xato (31-dars)."),
                    (False, "down",
                     "belgisiz — <em>run-on</em>, ikki gap qo'shilib "
                     "ketgan."),
                    (False, "down, and;",
                     "ikkita belgi birga: vergul + bog'lovchi o'zi to'g'ri "
                     "bo'lardi, lekin ustiga nuqtali vergul qo'yilgan. "
                     "W3'dagi «to'g'ri belgi + keraksiz ikkinchi belgi» "
                     "tuzog'i."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Bamboo scaffolding has carried builders up the sides of tall "
                "buildings in southern China for centuries, and it is still put up by "
                "hand and lashed with plastic tie. Its usefulness rests on one property "
                "above <span class=\"sr-blank\"></span> its extraordinary strength when "
                "pulled along its length.</p>"),
            "choices": [
                {"text": "all:", "is_correct": True},
                {"text": "all;", "is_correct": False},
                {"text": "all.", "is_correct": False},
                {"text": "all, and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Its usefulness "
                "rests on one property above all</em> \u2014 mustaqil.</p>"
                "<p>O\u2018ng: <em>its extraordinary strength when pulled along "
                "its length</em> \u2014 <mark>ot birikmasi</mark>, gap emas: "
                "shaxsli kesim yo\u2018q.</p>"
                "<p><strong>Mustaqil + bo\u2018lak</strong> \u2192 ikkinchi qator. Va "
                "chap tomon <em>one property</em> deb <u>e\u2019lon "
                "qilyapti</u> \u2014 bu ikki nuqtaning aynan vazifasi.</p>"
                + why([
                    (True, "all:",
                     "ikki nuqtadan oldin to\u2018liq gap turibdi (shart "
                     "bajarilgan), va undan keyin e\u2019lon qilingan narsa "
                     "keladi. <em>one property above all</em> \u2192 "
                     "\u00abqaysi xususiyat?\u00bb \u2014 ikki nuqta javob beradi."),
                    (False, "all;",
                     "nuqtali vergul <u>ikki mustaqil gap</u> orasida "
                     "bo\u2018ladi. O\u2018ng tomon ot birikmasi \u2014 "
                     "taqiqlangan."),
                    (False, "all.",
                     "nuqta ham mustaqil gap talab qiladi va bu yerda "
                     "<strong>fragment</strong> yasaydi: "
                     "<em>Its extraordinary strength when pulled along its "
                     "length.</em>"),
                    (False, "all, and",
                     "<em>and</em> dan keyin gap yoki bir jinsli bo\u2018lak "
                     "kutiladi, va u <em>rests on</em> fe\u2019liga "
                     "ulanmaydi \u2014 gap buziladi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an independent clause</div><div class="pp-card-back">mustaqil gap (ega + shaxsli kesim, o\'zi turadi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a dependent clause</div><div class="pp-card-back">ergash gap (bo\'ysundiruvchi so\'z bilan boshlanadi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a finite verb</div><div class="pp-card-back">shaxsli kesim (zamon ko\'rsatadi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a subordinator</div><div class="pp-card-back">bo\'ysundiruvchi so\'z (because, although…)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a comma splice</div><div class="pp-card-back">ikki mustaqil gapni yolg\'iz vergul bilan bog\'lash</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a run-on sentence</div><div class="pp-card-back">belgisiz qo\'shilib ketgan ikki gap</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a salt marsh</div><div class="pp-card-back">sho\'r botqoq (dengiz bo\'yida)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a span (of a roof)</div><div class="pp-card-back">oraliq, tayanchlar orasidagi masofa</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Yagona savol: <strong>chap mustaqilmi? o'ng "
              "mustaqilmi?</strong></li>"
              "<li>Mustaqil gap = ega + <u>shaxsli</u> kesim, va boshida "
              "bo'ysundiruvchi so'z yo'q.</li>"
              "<li><em>-ing</em> va <em>to + fe'l</em> kesim emas.</li>"
              "<li>Mustaqil + mustaqil → <strong>. ; ,+and</strong>. "
              "Ergash + mustaqil → <strong>faqat vergul</strong>.</li>"
              "<li>Ikkita belgi birga qo'yilgan variant — doimiy "
              "tuzoq.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 31
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W31: The Comma Splice — The Single Most Tested Error",
    "summary": "Ikki mustaqil gapni yolg'iz vergul bog'lay olmaydi. Va however, "
               "therefore, moreover — bular bog'lovchi emas, shuning uchun ular ham "
               "yordam bermaydi.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>Vergul ikki gapni ko'tara olmaydi</h2>"
            "<p>Bu — Standard English Conventions domenidagi eng ko'p "
            "sinaladigan bitta xato, va uning qoidasi bitta jumlaga "
            "sig'adi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Ikki mustaqil "
                "gapni yolg'iz vergul bilan bog'lab bo'lmaydi. Hech "
                "qachon. Istisnosiz.</strong></p>")
            + "<p>Ingliz tilida bu xatoning nomi bor: "
            "<strong>comma splice</strong>. O'zbek tilida vergulning "
            "qoidalari yumshoqroq, shuning uchun o'zbek quloqqa splays "
            "<u>umuman g'alati eshitilmaydi</u> — va aynan shuning uchun "
            "u sizni tez-tez yiqitadi.</p>"
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch tuzatish</h3>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\">✗ <em>The tide was falling, the "
                "boat could not clear the bar.</em></p>"
                "<p style=\"margin:0;\">✓ <em>The tide was falling<strong>.</strong> "
                "The boat could not clear the bar.</em><br>"
                "✓ <em>The tide was falling<strong>;</strong> the boat could "
                "not clear the bar.</em><br>"
                "✓ <em>The tide was falling<strong>, so</strong> the boat "
                "could not clear the bar.</em><br>"
                "✓ <em><strong>Because</strong> the tide was falling, the boat "
                "could not clear the bar.</em></p>")
            + "<p>To'rtinchi yechimga e'tibor bering: "
            "<em>Because</em> qo'shilishi bilan birinchi bo'lak "
            "<u>ergash gapga</u> aylanadi — va endi vergul to'g'ri, "
            "chunki bu boshqa qator (jadvalning uchinchisi).</p>"
        )},

        {"rich_text": (
            "<h3>Eng katta tuzoq: <em>however</em> bog'lovchi emas</h3>"
            "<p>Bu qism imtihonda eng ko'p ball yeydi. "
            "<em>However · therefore · moreover · nevertheless · "
            "consequently · furthermore · instead · in fact</em> — bular "
            "<mark>bog'lovchi emas</mark>. Ular <strong>ravish</strong> "
            "(conjunctive adverb), va ular ikki gapni "
            "<u>bog'lay olmaydi</u>.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>So'z</th><th>Turi</th><th>Ikki gapni "
              "bog'laydimi?</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>and · but · so · or · yet · for · nor</em></td>"
              "<td>bog'lovchi (FANBOYS)</td>"
              "<td>✓ ha — vergul bilan birga</td></tr>"
              "<tr><td><em>however · therefore · moreover · "
              "nevertheless</em></td><td>ravish</td>"
              "<td>✗ yo'q — nuqtali vergul yoki nuqta kerak</td></tr>"
              "<tr><td><em>because · although · when · if · since</em></td>"
              "<td>bo'ysundiruvchi</td>"
              "<td>✓ ha — lekin gapni ergashga aylantirib</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "✗ <em>It rained all week, <u>however</u> the match went "
                "ahead.</em> — bu <strong>splays</strong>, chunki "
                "<em>however</em> bog'lay olmaydi.<br>"
                "✓ <em>It rained all week<strong>;</strong> however, the "
                "match went ahead.</em><br>"
                "✓ <em>It rained all week<strong>, but</strong> the match "
                "went ahead.</em>")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The observatory's dome was designed to rotate on a ring of iron "
                "balls, a system that worked for sixty years without attention. The "
                "balls have now worn flat on one side "
                "<span class=\"sr-blank\"></span> the dome sticks at the same three "
                "points every night.</p>")
            + choices_html([
                "and, therefore",
                "; therefore,",
                ", therefore",
                "therefore",
            ])
            + "<p><strong>Ikki gap sinovi.</strong> Chap: <em>The balls have "
            "now worn flat on one side</em> — mustaqil. O'ng: <em>the dome "
            "sticks at the same three points every night</em> — "
            "mustaqil.</p>"
            "<p><strong>Mustaqil + mustaqil</strong>, va bog'lovchi so'z "
            "<em>therefore</em> — ravish. Demak unga "
            "<mark>nuqtali vergul yoki nuqta</mark> kerak.</p>"
            + why([
                (True, "; therefore,",
                 "nuqtali vergul ikki gapni ajratadi, <em>therefore</em> esa "
                 "ikkinchi gapning ichida ravish sifatida turadi va "
                 "vergul bilan ajratiladi. Bu yagona to'g'ri shakl."),
                (False, ", therefore",
                 "<strong>vergul splaysi</strong> — darsning asosiy xatosi. "
                 "<em>therefore</em> bog'lovchi emas, shuning uchun vergul "
                 "yolg'iz qoladi va ikki gapni ko'tara olmaydi."),
                (False, "therefore",
                 "belgisiz: <em>run-on</em>. Ravish qo'shilgani hech nimani "
                 "o'zgartirmaydi."),
                (False, "and, therefore",
                 "<em>and</em> haqiqiy bog'lovchi, lekin undan "
                 "<u>oldin</u> vergul kerak: <em>…on one side, and "
                 "therefore the dome sticks…</em>. Bu variantda vergul "
                 "noto'g'ri tomonda va <em>and</em> oldida hech nima "
                 "yo'q."),
            ])
        )},

        {
            "rich_text": conv_q(
                "<p>Ravens will drop a nut on a road and wait for a car to crack it, and "
                "the same birds have been recorded waiting at pedestrian crossings for "
                "the traffic to stop before retrieving <span class=\"sr-blank\"></span> "
                "the behaviour appears in some populations and not in "
                "others.</p>"),
            "choices": [
                {"text": "it. Curiously,", "is_correct": True},
                {"text": "it, curiously", "is_correct": False},
                {"text": "it curiously", "is_correct": False},
                {"text": "it, curiously,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Ravens will "
                "drop … before retrieving it</em> — mustaqil. O'ng: "
                "<em>the behaviour appears in some populations and not in "
                "others</em> — mustaqil.</p>"
                "<p><em>Curiously</em> — ravish, bog'lovchi emas. Demak "
                "<mark>nuqta yoki nuqtali vergul</mark> kerak.</p>"
                + why([
                    (True, "it. Curiously,",
                     "nuqta ikki mustaqil gapni ajratadi, va "
                     "<em>Curiously,</em> ikkinchi gapning boshida ravish "
                     "sifatida vergul bilan turadi."),
                    (False, "it, curiously,",
                     "<strong>vergul splaysi</strong> — ravishni ikki "
                     "tomondan vergul bilan o'rash uni bog'lovchiga "
                     "aylantirmaydi. Eng ko'p tanlanadigan noto'g'ri "
                     "javob, chunki u eng «tartibli» ko'rinadi."),
                    (False, "it, curiously",
                     "yana splays, va ustiga ravish yarim ajratilgan."),
                    (False, "it curiously",
                     "belgisiz <em>run-on</em>, va <em>curiously</em> "
                     "<em>retrieving</em> ga yopishib boshqa ma'no "
                     "beradi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Tea plants and camellias grown for their flowers belong to the same "
                "genus, and a gardener can graft one onto the "
                "<span class=\"sr-blank\"></span> the leaves of the ornamental varieties "
                "make a bitter and disappointing drink.</p>"),
            "choices": [
                {"text": "other, but", "is_correct": True},
                {"text": "other, however", "is_correct": False},
                {"text": "other but", "is_correct": False},
                {"text": "other; but", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi:</strong> ikkala tomon ham "
                "mustaqil. Ma'no — qarama-qarshilik.</p>"
                "<p><strong>Mustaqil + mustaqil</strong> uchun uchta qonuniy "
                "yechim bor, va ulardan biri "
                "<mark>vergul + FANBOYS</mark>.</p>"
                + why([
                    (True, "other, but",
                     "<em>but</em> — haqiqiy bog'lovchi (FANBOYS), va undan "
                     "oldin vergul turadi. Ikki mustaqil gap qonuniy "
                     "ulangan."),
                    (False, "other, however",
                     "<strong>vergul splaysi:</strong> <em>however</em> "
                     "ravish, bog'lovchi emas. Ma'nosi <em>but</em> bilan "
                     "bir xil bo'lsa ham, grammatikasi boshqa — bu "
                     "darsning asosiy nuqtasi."),
                    (False, "other; but",
                     "nuqtali vergul o'zi yetadi; undan keyin "
                     "<em>but</em> ortiqcha. Ikkita ulash vositasi birga "
                     "qo'yilgan."),
                    (False, "other but",
                     "bog'lovchi bor, vergul yo'q. Ikki mustaqil gapni "
                     "ulaganda FANBOYS oldidan vergul qo'yiladi."),
                ])
                + TIP.format(
                    "<strong><em>however</em> va <em>but</em> ma'nosi bir "
                    "xil, grammatikasi boshqa.</strong> Bu SAT'ning "
                    "sevimli sinovi: ikki variant bir xil ma'no beradi va "
                    "faqat bittasi grammatik jihatdan mumkin. "
                    "Ma'noga qarab tanlagan o'quvchi yiqiladi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The lighthouse was automated in 1988 and the last keeper left that "
                "autumn, taking with him the logbooks that had recorded the weather at "
                "fixed hours since <span class=\"sr-blank\"></span> the series is "
                "unbroken from 1873 to the day the door was locked.</p>"),
            "choices": [
                {"text": "1873;", "is_correct": True},
                {"text": "1873,", "is_correct": False},
                {"text": "1873", "is_correct": False},
                {"text": "1873, and;", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>The lighthouse "
                "was automated … since 1873</em> — mustaqil (uzun, lekin "
                "bitta gap). O'ng: <em>the series is unbroken from 1873 to "
                "the day the door was locked</em> — ega (<em>the "
                "series</em>), kesim (<em>is</em>): mustaqil.</p>"
                + why([
                    (True, "1873;",
                     "nuqtali vergul — ikki mustaqil gapni ulashning "
                     "qonuniy usuli, va u ikki fikrning zich "
                     "bog'liqligini saqlaydi."),
                    (False, "1873,",
                     "<strong>vergul splaysi.</strong> Chap tomon uzun "
                     "bo'lgani uchun o'quvchi uning tugaganini sezmay "
                     "qoladi — bu tuzoqning odatiy shakli."),
                    (False, "1873",
                     "belgisiz <em>run-on</em>, va ustiga <em>since 1873 "
                     "the series</em> bo'lib o'qiladi, ya'ni ma'no ham "
                     "buziladi."),
                    (False, "1873, and;",
                     "ikkita ulash vositasi birga. Har belgini alohida "
                     "tekshiring."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Roman roads were laid out in straight sections running between fixed "
                "points rather than curving to follow the contours of the "
                "<span class=\"sr-blank\"></span> this made them longer and more "
                "expensive to build but far easier to survey and to repair.</p>"),
            "choices": [
                {"text": "land;", "is_correct": True},
                {"text": "land,", "is_correct": False},
                {"text": "land, moreover", "is_correct": False},
                {"text": "land", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Roman roads "
                "were laid out … contours of the land</em> \u2014 mustaqil. "
                "O\u2018ng: <em>this made them longer … but far easier to "
                "survey and to repair</em> \u2014 ega (<em>this</em>), kesim "
                "(<em>made</em>): mustaqil.</p>"
                "<p>Diqqat: o\u2018ng tomon ichida <em>but</em> bor, lekin u "
                "<u>ikki sifatni</u> bog\u2018layapti "
                "(<em>longer … but easier</em>), ikki gapni emas \u2014 "
                "shuning uchun u chegara masalasini hal qilmaydi.</p>"
                + why([
                    (True, "land;",
                     "nuqtali vergul ikki mustaqil gapni ulaydi. Nuqta ham "
                     "to\u2018g\u2018ri bo\u2018lardi, lekin variantlar orasida "
                     "yo\u2018q."),
                    (False, "land,",
                     "<strong>vergul splaysi</strong> \u2014 sof holda."),
                    (False, "land, moreover",
                     "<strong>splays + ravish:</strong> <em>moreover</em> "
                     "bog\u2018lovchi emas, shuning uchun u vergulga yordam "
                     "bermaydi. Va ma\u2019nosi ham noto\u2018g\u2018ri \u2014 bu "
                     "qo\u2018shimcha emas, oqibat."),
                    (False, "land",
                     "belgisiz <em>run-on</em>."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a comma splice</div><div class="pp-card-back">ikki mustaqil gapni yolg\'iz vergul bilan bog\'lash</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a conjunctive adverb</div><div class="pp-card-back">bog\'lovchi-ravish (however, therefore…) — bog\'lay olmaydi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a coordinating conjunction</div><div class="pp-card-back">teng bog\'lovchi (FANBOYS) — bog\'lay oladi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">FANBOYS</div><div class="pp-card-back">for, and, nor, but, or, yet, so</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to graft</div><div class="pp-card-back">payvand qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">ornamental</div><div class="pp-card-back">bezak uchun o\'stiriladigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to retrieve</div><div class="pp-card-back">olib kelmoq, qaytarib olmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unbroken (of a series)</div><div class="pp-card-back">uzilmagan (yozuvlar qatori)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Ikki mustaqil gap + yolg'iz vergul = xato.</strong> "
              "Istisnosiz.</li>"
              "<li>Uch tuzatish: <strong>.</strong> · <strong>;</strong> · "
              "<strong>,</strong> + FANBOYS. To'rtinchisi: birini ergash "
              "gapga aylantirish.</li>"
              "<li><em>however · therefore · moreover · nevertheless</em> — "
              "<strong>ravish, bog'lovchi emas</strong>.</li>"
              "<li><em>however</em> = <em>but</em> ma'noda, lekin "
              "grammatikasi boshqa — SAT aynan shuni sinaydi.</li>"
              "<li>O'zbek quloqqa splays g'alati eshitilmaydi: "
              "<u>tekshiring, eshitmang</u>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 32
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W32: Full Stop, Semicolon, or Comma + FANBOYS — Three Legal Joins",
    "summary": "Ikki mustaqil gapni ulashning aynan uch usuli bor. Ular grammatik "
               "jihatdan teng, shuning uchun SAT hech qachon ikkitasini birga bermaydi.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Uchta qonuniy ulash</h2>"
            "<p>31-darsda nima <u>mumkin emasligini</u> ko'rdik. Bu dars "
            "nima <u>mumkinligi</u> haqida — va u qisqa ro'yxat.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Usul</th><th>Shakli</th><th>Qachon</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Nuqta</strong></td>"
              "<td><em>… side. The dome …</em></td>"
              "<td>Ikki fikr mustaqil o'qilsa</td></tr>"
              "<tr><td><strong>Nuqtali vergul</strong></td>"
              "<td><em>… side; the dome …</em></td>"
              "<td>Ikki fikr zich bog'liq bo'lsa</td></tr>"
              "<tr><td><strong>Vergul + FANBOYS</strong></td>"
              "<td><em>… side, so the dome …</em></td>"
              "<td>Munosabatni <u>nomlash</u> kerak bo'lsa</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Muhim "
                "natija:</strong> uchalasi ham grammatik jihatdan "
                "<u>bir xil darajada to'g'ri</u>. Shuning uchun SAT hech "
                "qachon ikkitasini bitta savolda javob sifatida "
                "bermaydi — aks holda ikkita to'g'ri javob bo'lardi "
                "(W15'dagi sinonim qoidasi).</p>")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Demak variantlar nimani ko'rsatadi</h3>"
            "<p>Agar variantlar orasida <em>nuqta</em> ham, "
            "<em>nuqtali vergul</em> ham bo'lsa — <mark>ikkovi ham javob "
            "emas</mark>, chunki ular teng. Javob qolgan ikkitasidan "
            "biri: odatda vergul (ergash gap uchun) yoki "
            "vergul + FANBOYS.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Variantlarni "
              "guruhlang.</strong> Nechtasi «mustaqil + mustaqil» yechimi? "
              "Ikkitasi bo'lsa — ikkovini ham o'chiring.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Qolganlarini ikki gap "
              "sinovi bilan tekshiring</strong> (30-dars).</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. FANBOYS tanlansa, "
              "ma'nosini ham tekshiring:</strong> <em>and</em> qo'shadi, "
              "<em>but</em> qarshi qo'yadi, <em>so</em> natija, "
              "<em>for</em> sabab. Noto'g'ri bog'lovchi — noto'g'ri "
              "javob, grammatikasi joyida bo'lsa ham.</p></div>"
            + '</div>'
            + WARN.format(
                "Ikki belgi birga qo'yilgan variant har doim xato: "
                "<em>; and</em> · <em>, and;</em> · <em>. But,</em> · "
                "<em>; however but</em>. Bitta ulash yetadi va ikkinchisi "
                "ortiqcha. Bu tuzoq bu mavzuda har bir darsda "
                "uchraydi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The dye known as Tyrian purple was extracted from a sea snail, and "
                "several thousand animals were needed for enough dye to colour the hem "
                "of a single <span class=\"sr-blank\"></span> the colour was reserved by "
                "law for the highest offices in Rome.</p>")
            + choices_html([
                "garment. Consequently,",
                "garment; the",
                "garment, so",
                "garment, and so;",
            ])
            + "<p><strong>Ikki gap sinovi:</strong> ikkala tomon ham "
            "mustaqil.</p>"
            "<p><strong>Variantlarni guruhlaymiz.</strong> Birinchi variant "
            "nuqta, ikkinchisi nuqtali vergul — ikkovi ham «mustaqil + "
            "mustaqil» ning teng yechimlari. <mark>Ikkovi ham javob "
            "emas</mark>: agar biri to'g'ri bo'lsa, ikkinchisi ham "
            "to'g'ri bo'lardi.</p>"
            "<p>Qoldi: <em>garment, so</em> va <em>garment, and so;</em>.</p>"
            + why([
                (True, "garment, so",
                 "vergul + FANBOYS. Va <em>so</em> ma'noni to'g'ri beradi: "
                 "bo'yoq juda qimmatga tushgani <u>uchun</u> u qonun bilan "
                 "cheklangan."),
                (False, "garment, and so;",
                 "ikkita ulash birga: vergul + bog'lovchi <u>va</u> nuqtali "
                 "vergul. Bittasi ortiqcha."),
                (False, "garment. Consequently,",
                 "grammatik jihatdan <u>to'g'ri</u> — lekin nuqtali vergulli "
                 "variant ham to'g'ri bo'lardi, va imtihonda ikkita javob "
                 "bo'lmaydi. Demak ikkovi ham chiqarib tashlanadi."),
                (False, "garment; the",
                 "yuqoridagining juftligi — xuddi shu sababdan javob "
                 "emas."),
            ])
            + NOTE.format(
                "Bu savolda grammatika <u>ikkita</u> variantni ham "
                "qabul qilardi. Ularni ajratgan narsa grammatika emas, "
                "<strong>imtihonning tuzilishi</strong>: bitta to'g'ri "
                "javob qoidasi. Bu W15'dagi sinonim usulining "
                "grammatikadagi ko'rinishi.")
        )},

        {
            "rich_text": conv_q(
                "<p>The two towers were built forty years apart and by different "
                "masons, and the join between them is visible from inside as a hairline "
                "crack running the full height of the "
                "<span class=\"sr-blank\"></span> the building has never moved along "
                "it.</p>"),
            "choices": [
                {"text": "wall, but", "is_correct": True},
                {"text": "wall, and", "is_correct": False},
                {"text": "wall, so", "is_correct": False},
                {"text": "wall, for", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar to'rtala variant ham <u>bir xil grammatik "
                "shaklda</u>: vergul + FANBOYS. Demak grammatika hech "
                "nimani ajratmaydi — <mark>ma'no ajratadi</mark>.</p>"
                "<p>Chap: devorda yoriq ko'rinadi. O'ng: bino u bo'ylab "
                "hech qachon qimirlamagan. Yoriq bor, lekin xavf yo'q — "
                "bu <strong>qarama-qarshilik</strong>.</p>"
                + why([
                    (True, "wall, but",
                     "qarshilik bog'lovchisi: yoriq ko'rinadi-yu, harakat "
                     "yo'q. Kutilgan xavotir rad etiladi."),
                    (False, "wall, and",
                     "qo'shimcha: ikkinchi gap birinchisini "
                     "quvvatlashi kerak edi. U esa uni yumshatadi."),
                    (False, "wall, so",
                     "natija: yoriqning ko'rinishi binoning qimirlamasligiga "
                     "sabab bo'lmaydi. Mantiq teskari."),
                    (False, "wall, for",
                     "<em>for</em> — «chunki» ma'nosidagi kitobiy bog'lovchi. "
                     "Bu o'ng tomonni <u>sabab</u> qilib qo'yadi: bino "
                     "qimirlamagani uchun yoriq ko'rinadi — ma'nosiz."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A stradivarius violin sold at auction is usually described by the "
                "year it was made and by the name of a former owner, and the second of "
                "these can matter more to the "
                "<span class=\"sr-blank\"></span> a documented chain of owners is the "
                "clearest evidence that the instrument is what it is said to be.</p>"),
            "choices": [
                {"text": "price:", "is_correct": True},
                {"text": "price,", "is_correct": False},
                {"text": "price, and", "is_correct": False},
                {"text": "price and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi:</strong> ikkala tomon ham "
                "mustaqil. Demak uchta qonuniy yechim bor — lekin "
                "variantlar orasida ulardan faqat bittasi to'liq "
                "shaklda.</p>"
                "<p>Va ma'noga qarang: o'ng tomon chap tomondagi da'voni "
                "<mark>tushuntiradi</mark> («nega narxga ta'sir qiladi?»). "
                "Ikki nuqtaning aynan vazifasi.</p>"
                + why([
                    (True, "price:",
                     "ikki nuqtadan oldin to'liq gap turibdi, va undan "
                     "keyin tushuntirish keladi. Ikki mustaqil gap "
                     "orasida ikki nuqta — <u>izoh</u> munosabati "
                     "bo'lganda qonuniy."),
                    (False, "price,",
                     "<strong>vergul splaysi.</strong>"),
                    (False, "price, and",
                     "grammatik jihatdan to'g'ri, lekin <em>and</em> "
                     "shunchaki qo'shadi — u ikkinchi gapning "
                     "<u>izoh</u> ekanini ko'rsatmaydi. Ikki nuqta "
                     "aniqroq, va SAT bu yerda aniqlikni "
                     "tanlaydi."),
                    (False, "price and",
                     "bog'lovchi bor, vergul yo'q — ikki mustaqil gap "
                     "ulanganda FANBOYS oldidan vergul kerak."),
                ])
                + NOTE.format(
                    "Ikki nuqta ikki mustaqil gap orasida ham turishi "
                    "mumkin — lekin faqat ikkinchisi birinchisini "
                    "<u>izohlaganda</u>. Bu 40-darsning mavzusi; hozircha "
                    "shuni eslang: <strong>ikki nuqtadan oldin har doim "
                    "to'liq gap</strong>.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Peat cutters in the west of Ireland worked a bank from the top down "
                "and stacked the turves to dry in low walls, and the whole year's fuel "
                "had to be cut in a few weeks in early "
                "<span class=\"sr-blank\"></span> a wet June could leave a household "
                "without heat the following winter.</p>"),
            "choices": [
                {"text": "summer, and", "is_correct": True},
                {"text": "summer, but", "is_correct": False},
                {"text": "summer, or", "is_correct": False},
                {"text": "summer, yet", "is_correct": False},
            ],
            "explanation": (
                "<p>Yana to'rtala variant bir xil shaklda — vergul + "
                "FANBOYS. <mark>Faqat ma'no ajratadi.</mark></p>"
                "<p>Chap: yoqilg'ini bir necha hafta ichida kesish kerak. "
                "O'ng: nam iyun oilani qishda issiqsiz qoldirishi mumkin. "
                "Ikkinchisi birinchisining <strong>oqibati</strong> — va "
                "u xuddi shu yo'nalishda: ikkovi ham bu ishning "
                "xavfliligini ko'rsatadi.</p>"
                + why([
                    (True, "summer, and",
                     "qo'shimcha va davomiylik: qisqa muddat, "
                     "<u>va</u> shuning oqibati. Ikki gap bir yo'nalishda."),
                    (False, "summer, but",
                     "qarshilik: ikkinchi gap birinchisiga zid emas — u "
                     "undan kelib chiqadi."),
                    (False, "summer, or",
                     "muqobil: ikki variant taklif qilinmayapti."),
                    (False, "summer, yet",
                     "<em>yet</em> ham qarshilik bildiradi "
                     "(<em>but</em> kabi) — xuddi shu sababdan "
                     "noto'g'ri. Va e'tibor bering: <em>but</em> va "
                     "<em>yet</em> bu yerda <u>sinonim juftlik</u>, "
                     "ya'ni ikkovi ham javob bo'lolmaydi (W15)."),
                ])
                + TIP.format(
                    "FANBOYS variantlari berilganda W15'dagi sinonim "
                    "usulini qo'llang: <em>but</em> va <em>yet</em> bir xil "
                    "ishlaydi, <em>so</em> va <em>therefore</em> ham. "
                    "Juftlikni topsangiz — ikkovi ham tushadi va savol "
                    "yarmiga qisqaradi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Sled dogs pull best in temperatures well below freezing, and teams "
                "entered in unusually mild weather begin to overheat within a few "
                "<span class=\"sr-blank\"></span> which is why the longest races are "
                "run in February and March rather than at the end of the "
                "season.</p>"),
            "choices": [
                {"text": "hours,", "is_correct": True},
                {"text": "hours;", "is_correct": False},
                {"text": "hours.", "is_correct": False},
                {"text": "hours", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki gap sinovi.</strong> Chap: <em>Sled dogs pull "
                "best … begin to overheat within a few hours</em> \u2014 "
                "mustaqil.</p>"
                "<p>O\u2018ng: <em>which is why the longest races are run …</em> "
                "\u2014 <em>which</em> bilan boshlangan "
                "<mark>nisbiy ergash gap</mark>. U mustaqil emas.</p>"
                "<p>Demak bu <strong>mustaqil + ergash</strong> holati, va "
                "uchta \u00abqonuniy ulash\u00bb yechimidan ikkitasi shu yerda "
                "<u>taqiqlangan</u>.</p>"
                + why([
                    (True, "hours,",
                     "vergul \u2014 qo\u2018shimcha izoh beruvchi "
                     "<em>which</em>-gapi oldidan qo\u2018yiladigan yagona "
                     "belgi."),
                    (False, "hours;",
                     "nuqtali vergul <u>ikki mustaqil</u> gap orasida "
                     "bo\u2018ladi. Bu yerda o\u2018ng tomon mustaqil emas."),
                    (False, "hours.",
                     "nuqta ham mustaqil gap talab qiladi \u2014 va bu yerda u "
                     "<strong>fragment</strong> yasaydi: <em>Which is why "
                     "the longest races are run in February and March.</em>"),
                    (False, "hours",
                     "belgisiz: <em>which</em> qo\u2018shimcha izoh berayotgani "
                     "uchun vergul shart. Vergulsiz u "
                     "<em>a few hours</em> ni aniqlab qolgandek "
                     "o\u2018qiladi."),
                ])
                + NOTE.format(
                    "Bu savolda nuqta va nuqtali vergul birga berilgan \u2014 "
                    "va bu safar ular <u>ikkovi ham noto\u2018g\u2018ri</u>, chunki "
                    "o\u2018ng tomon mustaqil emas. W32\u2019dagi \u00abteng juftlik\u00bb "
                    "qoidasi ularni baribir birga chiqarib tashlaydi: "
                    "usul har ikki holatda ham ishlaydi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">for (bog\'lovchi)</div><div class="pp-card-back">chunki (kitobiy; sabab beradi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">yet (bog\'lovchi)</div><div class="pp-card-back">lekin (= but)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hairline crack</div><div class="pp-card-back">juda ingichka yoriq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hem (of a garment)</div><div class="pp-card-back">kiyimning etagi, chekkasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">provenance / chain of owners</div><div class="pp-card-back">egalar zanjiri, asarning tarixi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">peat / a turf</div><div class="pp-card-back">torf / kesilgan torf bo\'lagi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to reserve by law</div><div class="pp-card-back">qonun bilan cheklab qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a mason</div><div class="pp-card-back">tosh usta</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Uch qonuniy ulash: <strong>.</strong> · <strong>;</strong> "
              "· <strong>,</strong> + FANBOYS. Ular grammatik jihatdan "
              "teng.</li>"
              "<li>Shuning uchun <strong>nuqta va nuqtali vergul birga "
              "berilsa — ikkovi ham javob emas</strong>.</li>"
              "<li>To'rtala variant bir xil shaklda bo'lsa — javobni "
              "<u>ma'no</u> beradi: <em>and · but · so · for</em>.</li>"
              "<li>FANBOYS orasida ham sinonim juftlik bo'ladi: "
              "<em>but</em> ↔ <em>yet</em>.</li>"
              "<li>Ikkita ulash birga qo'yilgan variant — har doim "
              "xato.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 33
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W33: Fragments — Sentences With No Main Verb",
    "summary": "Uzun va batafsil bo'lak ham gap bo'lmasligi mumkin. Shaxsli kesimni "
               "qidiring — <em>-ing</em> va <em>to + fe'l</em> hisoblanmaydi.",
    "order": 33,
    "blocks": [
        {"rich_text": (
            "<h2>Uzunlik gap yasamaydi</h2>"
            "<p><strong>Fragment</strong> — nuqta bilan tugatilgan, lekin "
            "aslida gap bo'lmagan bo'lak. SAT uni ataylab "
            "<mark>uzun va batafsil</mark> qilib beradi, chunki uzun "
            "bo'lak to'liq tuyuladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>A method of repairing broken "
                "ceramics with lacquer mixed with powdered gold, developed in "
                "Japan and still practised there today.</em></p>"
                "<p style=\"margin:8px 0 0;\">Yigirma so'zdan ortiq, aniq, "
                "chiroyli — va <strong>gap emas</strong>. Bu yerda "
                "shaxsli kesim yo'q: <em>developed</em> va "
                "<em>practised</em> sifatdosh, kesim emas.</p>")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Fragmentning to'rt shakli</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Namuna</th><th>Nega gap emas</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>-ing</em> bilan</td>"
              "<td><em>Making it the oldest bridge in the city.</em></td>"
              "<td><em>-ing</em> shaxsli kesim emas</td></tr>"
              "<tr><td><em>to + fe'l</em></td>"
              "<td><em>To reach the summit before dark.</em></td>"
              "<td>infinitiv kesim bo'lolmaydi</td></tr>"
              "<tr><td>Bo'ysundiruvchi so'z bilan</td>"
              "<td><em>Although the dome had been rebuilt twice.</em></td>"
              "<td>ergash gap yolg'iz turolmaydi</td></tr>"
              "<tr><td>Ot birikmasi (appozitsiya)</td>"
              "<td><em>A discovery that changed the field.</em></td>"
              "<td>ot + aniqlovchi, kesim yo'q</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Sinov bitta savolga qisqaradi: <strong>bu bo'lakda "
                "zamon ko'rsatadigan fe'l bormi?</strong> "
                "<em>was · has · built · shows</em> — ha. "
                "<em>building · to build · built</em> (sifatdosh sifatida) "
                "— yo'q. Ega ham bo'lishi kerak.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The Pantheon's dome has stood unreinforced for nineteen centuries "
                "and is still the largest of its kind. Its builders reduced the weight "
                "of the concrete as they went up, using heavy basalt at the base and "
                "light volcanic pumice near the "
                "<span class=\"sr-blank\"></span> a solution that no one improved on for "
                "more than a thousand years.</p>")
            + choices_html([
                "top. Being",
                "top,",
                "top. It was",
                "top and",
            ])
            + "<p><strong>O'ng tomonni tekshiramiz:</strong> "
            "<em>a solution that no one improved on for more than a thousand "
            "years</em> — ot birikmasi. <em>improved</em> bor, lekin u "
            "<em>that</em>-gapining ichida; butun bo'lakning o'z egasi va "
            "kesimi yo'q. <mark>Gap emas.</mark></p>"
            "<p><strong>Mustaqil + bo'lak</strong> → vergul.</p>"
            + why([
                (True, "top,",
                 "vergul appozitsiyani asosiy gapga ulaydi: "
                 "<em>…near the top, a solution that no one improved "
                 "on…</em>. Bo'lak endi mustaqil turishga majbur "
                 "emas."),
                (False, "top. It was",
                 "grammatik jihatdan bu <u>to'g'ri</u> gap yasaydi — lekin "
                 "u ikkinchi gapni <em>It was</em> bilan boshlab, "
                 "keraksiz so'z qo'shadi. SAT bunday holatda eng qisqa "
                 "to'g'ri variantni tanlaydi; va bu yerda vergulli "
                 "variant ham to'g'ri, ya'ni ikkita javob bo'lardi. "
                 "<u>Lekin</u> asosiy sabab boshqa: <em>It</em> nimaga "
                 "ishora qilishi noaniq — og'irlikni kamaytirishgami, "
                 "pemzagami?"),
                (False, "top. Being",
                 "<strong>fragment yasaydi:</strong> <em>Being a solution "
                 "that no one improved on for more than a thousand "
                 "years.</em> — <em>-ing</em> kesim emas."),
                (False, "top and",
                 "<em>and</em> dan keyin gap yoki bir jinsli bo'lak "
                 "kutiladi. <em>a solution…</em> ot birikmasi "
                 "<em>using</em> ga ham, <em>reduced</em> ga ham "
                 "ulanmaydi — gap buziladi."),
            ])
            + NOTE.format(
                "Uchinchi variant («<em>top. It was</em>») bu turdagi "
                "eng nozik holat: u grammatik jihatdan xato emas, lekin "
                "aniqlik jihatdan yomonroq. SAT Conventions savollarida "
                "bunday variantni kamdan-kam beradi — odatda uchtasi "
                "<u>aniq xato</u> bo'ladi. Shubhalansangiz, "
                "<strong>xatoni qidiring</strong>, yaxshiroqni emas.")
        )},

        {
            "rich_text": conv_q(
                "<p>Cuneiform tablets were normally left to dry rather than fired, and "
                "the archives that survive are largely ones that a burning building "
                "happened to bake. <span class=\"sr-blank\"></span> preserving them by "
                "the same accident that destroyed everything around them.</p>"),
            "choices": [
                {"text": "The fire hardened the clay,", "is_correct": True},
                {"text": "The fire hardening the clay,", "is_correct": False},
                {"text": "With the fire hardening the clay,", "is_correct": False},
                {"text": "The fire, which hardened the clay,", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar bo'sh joy <u>gapning boshida</u>. "
                "O'ng tomon: <em>preserving them by the same accident…</em> "
                "— <em>-ing</em> bo'lagi, gap emas. Demak chap tomon "
                "<mark>mustaqil gap bo'lishi shart</mark>, aks holda "
                "butun jumla fragment bo'lib qoladi.</p>"
                + why([
                    (True, "The fire hardened the clay,",
                     "ega (<em>The fire</em>) + shaxsli kesim "
                     "(<em>hardened</em>) = mustaqil gap. Vergul "
                     "<em>-ing</em> bo'lagini unga ulaydi."),
                    (False, "The fire hardening the clay,",
                     "<strong>fragment:</strong> <em>hardening</em> shaxsli "
                     "kesim emas. Butun jumlada birorta kesim qolmaydi."),
                    (False, "With the fire hardening the clay,",
                     "yana <strong>fragment</strong>, va bu safar ikki "
                     "barobar: <em>With</em> predlogi ham, "
                     "<em>hardening</em> ham gap yasamaydi."),
                    (False, "The fire, which hardened the clay,",
                     "<em>which hardened the clay</em> nisbiy gap ichida "
                     "kesim bor, lekin <u>asosiy</u> gapning kesimi "
                     "yo'q: <em>The fire … preserving them</em>. "
                     "Fragment."),
                ])
                + TIP.format(
                    "Uzun bo'lakda kesim qidirganda <u>nisbiy gap "
                    "ichidagi</u> fe'lni hisobga olmang. "
                    "<em>The fire, which hardened the clay, preserving "
                    "them</em> — <em>hardened</em> bor, lekin u "
                    "<em>which</em> ga tegishli, <em>the fire</em> ga "
                    "emas.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The mountain observatory\u2019s weather records run without a break "
                "from the day it opened in 1873 to the day it was automated in "
                "<span class=\"sr-blank\"></span> a span of one hundred and fifteen "
                "years and one of the longest continuous series kept anywhere by a "
                "single institution.</p>"),
            "choices": [
                {"text": "1988,", "is_correct": True},
                {"text": "1988.", "is_correct": False},
                {"text": "1988;", "is_correct": False},
                {"text": "1988", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>O\u2018ng tomonni tekshiring:</strong> <em>a span of "
                "one hundred and fifteen years and one of the longest "
                "continuous series kept anywhere by a single institution</em> "
                "\u2014 uzun, batafsil, va <mark>ot birikmasi</mark>. Shaxsli "
                "kesim yo\u2018q.</p>"
                "<p><strong>Mustaqil + bo\u2018lak</strong> \u2192 vergul.</p>"
                + why([
                    (True, "1988,",
                     "vergul appozitsiyani asosiy gapga ulaydi. Bo\u2018lak "
                     "endi mustaqil turishga majbur emas."),
                    (False, "1988.",
                     "<strong>fragment yasaydi:</strong> <em>A span of one "
                     "hundred and fifteen years and one of the longest "
                     "continuous series kept anywhere by a single "
                     "institution.</em> \u2014 yigirma so\u2018zdan ortiq, va "
                     "baribir gap emas."),
                    (False, "1988;",
                     "nuqtali vergul <u>ikki mustaqil</u> gap orasida "
                     "bo\u2018ladi."),
                    (False, "1988",
                     "belgisiz: <em>in 1988 a span of…</em> bo\u2018lib "
                     "o\u2018qiladi va ma\u2019no buziladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p><span class=\"sr-blank\"></span> the surveyors were able to fix the "
                "position of the pass to within a few metres, a precision that had been "
                "impossible with the instruments of the previous decade.</p>"),
            "choices": [
                {"text": "Working through three consecutive summers,", "is_correct": True},
                {"text": "They worked through three consecutive summers,", "is_correct": False},
                {"text": "They worked through three consecutive summers and", "is_correct": False},
                {"text": "Working through three consecutive summers and", "is_correct": False},
            ],
            "explanation": (
                "<p>O\u2018ng tomon <em>the surveyors were able to fix…</em> \u2014 "
                "mustaqil gap. Demak chap tomon "
                "<mark>mustaqil gap BO\u2018LMASLIGI</mark> kerak: aks holda "
                "vergul splaysi chiqadi.</p>"
                "<p>Ya\u2019ni bu yerda <em>-ing</em> bo\u2018lagi \u2014 "
                "<u>afzallik</u>, kamchilik emas.</p>"
                + why([
                    (True, "Working through three consecutive summers,",
                     "sifatdosh bo\u2018lagi + vergul + mustaqil gap. Bo\u2018lak "
                     "gap emas, shuning uchun splays bo\u2018lmaydi \u2014 va u "
                     "<em>the surveyors</em> ga to\u2018g\u2018ri ishora qiladi."),
                    (False, "They worked through three consecutive summers,",
                     "<strong>vergul splaysi:</strong> ikkala tomon ham "
                     "mustaqil gap bo\u2018lib qoladi."),
                    (False, "They worked through three consecutive summers and",
                     "ikki mustaqil gap <em>and</em> bilan ulangan, lekin "
                     "undan oldin vergul yo\u2018q. Va <em>They</em> bilan "
                     "<em>the surveyors</em> takrorlanadi."),
                    (False, "Working through three consecutive summers and",
                     "<em>and</em> hech nimani bog\u2018lamaydi: chap tomonda "
                     "gap yo\u2018q. Butun jumla buziladi."),
                ])
                + TIP.format(
                    "<em>-ing</em> bo\u2018lagi <u>o\u2018z-o\u2018zicha</u> yomon emas. "
                    "U yolg\u2018iz turganda fragment yasaydi; asosiy gapga "
                    "vergul bilan ulanganda esa aynan to\u2018g\u2018ri yechim. "
                    "Savol har doim bitta: <strong>jumlada kamida bitta "
                    "shaxsli kesim bormi?</strong>")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The county history society was founded in 1931 with a single purpose "
                "in <span class=\"sr-blank\"></span> to record every surviving watermill "
                "in the county before the last of them was pulled down.</p>"),
            "choices": [
                {"text": "mind:", "is_correct": True},
                {"text": "mind.", "is_correct": False},
                {"text": "mind;", "is_correct": False},
                {"text": "mind and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>O\u2018ng tomon:</strong> <em>to record every "
                "surviving watermill in the county before the last of them "
                "was pulled down</em> \u2014 infinitiv bilan boshlangan "
                "bo\u2018lak. Ichida <em>was pulled down</em> bor, lekin u "
                "<em>before</em>-gapiga tegishli; butun bo\u2018lakning o\u2018z "
                "egasi va kesimi <mark>yo\u2018q</mark>.</p>"
                "<p>Va chap tomon <em>a single purpose</em> deb "
                "<u>e\u2019lon qilyapti</u> \u2014 ikki nuqtaning vazifasi.</p>"
                + why([
                    (True, "mind:",
                     "ikki nuqtadan oldin to\u2018liq gap bor, va undan keyin "
                     "e\u2019lon qilingan maqsad keladi. <em>a single "
                     "purpose</em> \u2192 \u00abqaysi maqsad?\u00bb"),
                    (False, "mind.",
                     "<strong>fragment:</strong> <em>To record every "
                     "surviving watermill in the county before the last of "
                     "them was pulled down.</em> \u2014 uzun, lekin gap emas."),
                    (False, "mind;",
                     "nuqtali vergul ikki mustaqil gap orasida bo\u2018ladi."),
                    (False, "mind and",
                     "<em>and</em> bir jinsli bo\u2018laklarni bog\u2018laydi; "
                     "<em>in mind and to record</em> bir-biriga "
                     "ulanmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a fragment</div><div class="pp-card-back">to\'liqsiz gap (kesimi yoki egasi yo\'q)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a participle</div><div class="pp-card-back">sifatdosh (-ing, -ed) — kesim emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an infinitive</div><div class="pp-card-back">infinitiv (to + fe\'l) — kesim emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a relative clause</div><div class="pp-card-back">nisbiy ergash gap (which, that, who)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">unreinforced</div><div class="pp-card-back">armaturasiz, mustahkamlagichsiz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">pumice</div><div class="pp-card-back">pemza (yengil vulqon toshi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to plot (data)</div><div class="pp-card-back">(ma\'lumotni) nuqta qilib tushirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to happen to ~</div><div class="pp-card-back">tasodifan ~ bo\'lib qolmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Uzunlik gap yasamaydi.</strong> Yigirma so'zli "
              "bo'lak ham fragment bo'lishi mumkin.</li>"
              "<li>Bitta sinov: <strong>zamon ko'rsatadigan fe'l "
              "bormi?</strong> Va egasi bormi?</li>"
              "<li><em>-ing · to + fe'l · sifatdosh</em> — kesim emas.</li>"
              "<li>Nisbiy gap ichidagi fe'lni asosiy kesim deb "
              "hisoblamang.</li>"
              "<li>Fragmentni tuzatish: vergul bilan ulash yoki kesim "
              "berish.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 34
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W34: Dependent Clause First, Independent Second (and the Comma Between)",
    "summary": "Ergash gap oldinda kelsa — vergul shart. Orqada kelsa — odatda vergul "
               "qo'yilmaydi. Tartib qoidani o'zgartiradi.",
    "order": 34,
    "blocks": [
        {"rich_text": (
            "<h2>Tartib qoidani o'zgartiradi</h2>"
            "<p>Bu dars bitta juftlikni o'rgatadi, va u imtihonda "
            "muntazam sinaladi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✓ <em><strong>Because</strong> the "
                "tide was falling<strong>,</strong> the boat could not clear "
                "the bar.</em><br>"
                "✓ <em>The boat could not clear the bar "
                "<strong>because</strong> the tide was falling.</em></p>"
                "<p style=\"margin:8px 0 0;\">Bir xil ma'no, bir xil "
                "so'zlar — <mark>lekin faqat birinchisida vergul "
                "bor</mark>.</p>")
            + "<p>Qoida: <strong>ergash gap oldinda</strong> kelsa, undan "
            "keyin vergul <u>shart</u>. <strong>Orqada</strong> kelsa, "
            "vergul <u>odatda qo'yilmaydi</u>.</p>"
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Nega shunday</h3>"
            "<p>Vergul o'quvchiga «asosiy gap hali boshlanmadi» deb "
            "signal beradi. Ergash gap oldinda kelganda o'quvchi qayerda "
            "tugaganini bilishi kerak — vergul shuni "
            "ko'rsatadi.</p>"
            "<p>Orqada kelganda esa asosiy gap allaqachon "
            "o'qib bo'lingan: signal keraksiz.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Tartib</th><th>Vergul</th><th>Namuna</th></tr></thead>"
              "<tbody>"
              "<tr><td>Ergash → mustaqil</td><td><strong>shart</strong></td>"
              "<td><em>When the kiln cooled, they opened it.</em></td></tr>"
              "<tr><td>Mustaqil → ergash</td><td><strong>odatda "
              "yo'q</strong></td>"
              "<td><em>They opened it when the kiln cooled.</em></td></tr>"
              "<tr><td>Kirish bo'lagi → mustaqil</td>"
              "<td><strong>shart</strong> (uzun bo'lsa)</td>"
              "<td><em>After two hours in the dark, the plates were "
              "developed.</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Istisno: <em>although · whereas · while</em> qarshilik "
                "bildirganda, orqada kelsa ham vergul qo'yilishi mumkin "
                "— <em>The kiln was cool, although the bricks were "
                "still warm.</em> SAT bu nozik holatni kamdan-kam "
                "sinaydi; asosiy juftlikni mustahkam biling.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>Because the ink used in the earliest printed books was made with "
                "linseed oil rather than "
                "<span class=\"sr-blank\"></span> it sat on the surface of the paper "
                "instead of sinking into it, and the letters still stand slightly "
                "proud of the page five centuries later.</p>")
            + choices_html([
                "water,",
                "water;",
                "water",
                "water:",
            ])
            + "<p><strong>Birinchi so'zga qarang:</strong> "
            "<em>Because</em>. Demak chap tomon "
            "<mark>ergash gap</mark>, va u <u>oldinda</u> kelyapti.</p>"
            "<p>O'ng tomon: <em>it sat on the surface … and the letters "
            "still stand …</em> — mustaqil.</p>"
            "<p><strong>Ergash → mustaqil</strong> = jadvalning birinchi "
            "qatori: vergul shart, boshqa hech narsa mumkin emas.</p>"
            + why([
                (True, "water,",
                 "boshda kelgan ergash gapdan keyingi vergul. Yagona "
                 "to'g'ri belgi."),
                (False, "water;",
                 "nuqtali vergul <u>ikki mustaqil gap</u> orasida "
                 "bo'ladi. <em>Because…</em> mustaqil emas."),
                (False, "water:",
                 "ikki nuqtadan <u>oldin</u> to'liq gap turishi shart. "
                 "Bu yerda turmaydi."),
                (False, "water",
                 "belgisiz: o'quvchi ergash gapning qayerda tugaganini "
                 "bilmaydi, va <em>rather than water it sat</em> bo'lib "
                 "o'qiladi."),
            ])
        )},

        {
            "rich_text": conv_q(
                "<p>The glassmakers of Murano were forbidden to leave the island on "
                "pain of severe penalty, and the ban held for three hundred years "
                "<span class=\"sr-blank\"></span> the techniques they had developed were "
                "worth more to the republic than the men themselves.</p>"),
            "choices": [
                {"text": "because", "is_correct": True},
                {"text": "because,", "is_correct": False},
                {"text": ", because,", "is_correct": False},
                {"text": "; because", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar ergash gap <u>orqada</u>: "
                "<em>because the techniques … were worth more …</em>.</p>"
                "<p><strong>Mustaqil → ergash</strong> = jadvalning ikkinchi "
                "qatori: vergul <mark>odatda qo'yilmaydi</mark>.</p>"
                + why([
                    (True, "because",
                     "orqada kelgan sabab ergash gapi vergulsiz ulanadi. "
                     "Asosiy gap allaqachon o'qib bo'lingan — signal "
                     "kerak emas."),
                    (False, "because,",
                     "<em>because</em> dan <u>keyin</u> vergul hech qachon "
                     "qo'yilmaydi: u ergash gapni boshlaydi, tugatmaydi."),
                    (False, ", because,",
                     "ikki tomondan vergul — <em>because</em>-gapi kirish "
                     "bo'lagi emas, uni o'rab bo'lmaydi."),
                    (False, "; because",
                     "nuqtali vergul ikki mustaqil gap talab qiladi; "
                     "<em>because…</em> ergash."),
                ])
                + TIP.format(
                    "<strong><em>because</em> dan keyin hech qachon vergul "
                    "qo'yilmaydi.</strong> Bu bir soniyalik tekshiruv va "
                    "u bitta variantni darrov o'chiradi. Xuddi shu "
                    "<em>although · when · if · since · while</em> uchun "
                    "ham amal qiladi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p><span class=\"sr-blank\"></span> the flooded northern basin began to "
                "refill within a year, and fish that had not been recorded there for "
                "two decades were caught again in the shallows.</p>"),
            "choices": [
                {"text": "Once the dam had closed the strait,", "is_correct": True},
                {"text": "Once the dam had closed the strait", "is_correct": False},
                {"text": "The dam closed the strait,", "is_correct": False},
                {"text": "The dam closed the strait and,", "is_correct": False},
            ],
            "explanation": (
                "<p>O'ng tomon <em>the flooded northern basin began to "
                "refill…</em> — mustaqil gap. Chap tomon "
                "<u>ergash</u> bo'lishi kerak, aks holda splays "
                "chiqadi.</p>"
                + why([
                    (True, "Once the dam had closed the strait,",
                     "<em>Once</em> bo'ysundiruvchi so'z \\u2014 chap tomon "
                     "ergash gapga aylanadi, va boshda kelgani uchun "
                     "vergul shart. Ikkala qoida ham bajarilgan."),
                    (False, "The dam closed the strait,",
                     "<strong>vergul splaysi:</strong> chap tomon endi "
                     "mustaqil gap va vergul ikkovini ko'tara "
                     "olmaydi."),
                    (False, "Once the dam had closed the strait",
                     "ergash gap to'g'ri, lekin vergul yo'q — boshda "
                     "kelgan ergash gapdan keyin vergul shart."),
                    (False, "The dam closed the strait and,",
                     "<em>and</em> dan keyin vergul asossiz, va "
                     "<em>and</em> oldida vergul yo'q — ikki xato "
                     "birga."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Ships carrying grain were loaded to a mark painted on the hull, and "
                "an overloaded vessel rode so low that a moderate sea could break over "
                "the deck. <span class=\"sr-blank\"></span> the mark became compulsory "
                "in British ships, losses in winter crossings fell sharply.</p>"),
            "choices": [
                {"text": "After", "is_correct": True},
                {"text": "After,", "is_correct": False},
                {"text": "Afterward,", "is_correct": False},
                {"text": "After that,", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyingi qism: <em>the mark became "
                "compulsory in British ships<u>,</u> losses in winter "
                "crossings fell sharply</em>. Vergul allaqachon "
                "qo'yilgan — demak undan oldingi bo'lak "
                "<mark>ergash gap bo'lishi kerak</mark>.</p>"
                "<p>Ergash gap yasash uchun bo'ysundiruvchi so'z "
                "kerak.</p>"
                + why([
                    (True, "After",
                     "<em>After</em> \\u2014 bo'ysundiruvchi so'z: "
                     "<em>After the mark became compulsory,</em> ergash "
                     "gap bo'lib, keyingi mustaqil gapga vergul bilan "
                     "ulanadi."),
                    (False, "Afterward,",
                     "<em>Afterward</em> \\u2014 <strong>ravish</strong>, "
                     "bo'ysundiruvchi emas. U <em>the mark became "
                     "compulsory</em> ni mustaqil gap holida qoldiradi, "
                     "va keyingi vergul splays yasaydi."),
                    (False, "After that,",
                     "yana ravish birikmasi — xuddi shu sababdan splays. "
                     "<em>After</em> va <em>After that</em> orasidagi farq "
                     "aynan bu darsning mavzusi."),
                    (False, "After,",
                     "<em>After</em> dan keyin vergul qo'yilmaydi \\u2014 u "
                     "ergash gapni boshlaydi."),
                ])
                + NOTE.format(
                    "Bu savol 31-darsdagi qoidani boshqa tomondan "
                    "ko'rsatadi: <em>however · therefore · afterward · "
                    "consequently</em> ravish, shuning uchun ular gapni "
                    "<u>ergashga aylantira olmaydi</u>. Faqat "
                    "bo'ysundiruvchi so'zlar buni qiladi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p><span class=\"sr-blank\"></span> the photographic plates were "
                "developed in a shed behind the observatory, and the astronomer who had "
                "exposed them never saw them printed at full size.</p>"),
            "choices": [
                {"text": "After two hours in a tank of cold developer,", "is_correct": True},
                {"text": "After two hours in a tank of cold developer", "is_correct": False},
                {"text": "Two hours passed in a tank of cold developer,", "is_correct": False},
                {"text": "Two hours passed in a tank of cold developer and", "is_correct": False},
            ],
            "explanation": (
                "<p>O\u2018ng tomon <em>the photographic plates were developed "
                "\u2026</em> \u2014 mustaqil gap. Chap tomon mustaqil "
                "<u>bo\u2018lmasligi</u> kerak.</p>"
                "<p>Diqqat: bu safar chap tomon ergash <u>gap</u> emas, "
                "<mark>kirish bo\u2018lagi</mark> (predlogli birikma). Qoida "
                "bir xil: boshda kelgan uzun bo\u2018lakdan keyin vergul "
                "qo\u2018yiladi.</p>"
                + why([
                    (True, "After two hours in a tank of cold developer,",
                     "predlogli kirish bo\u2018lagi + vergul + mustaqil gap. "
                     "Bo\u2018lakda kesim yo\u2018q, shuning uchun splays "
                     "bo\u2018lmaydi."),
                    (False, "Two hours passed in a tank of cold developer,",
                     "<strong>vergul splaysi:</strong> <em>Two hours "
                     "passed</em> \u2014 ega + kesim, ya\u2019ni mustaqil gap."),
                    (False, "Two hours passed in a tank of cold developer and",
                     "ikki mustaqil gap <em>and</em> bilan ulangan, lekin "
                     "undan oldin vergul yo\u2018q."),
                    (False, "After two hours in a tank of cold developer",
                     "bo\u2018lak to\u2018g\u2018ri, lekin vergul yo\u2018q \u2014 boshda "
                     "kelgan uzun kirish bo\u2018lagidan keyin u shart."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an introductory clause</div><div class="pp-card-back">boshda kelgan ergash gap (→ vergul shart)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">once (bog\'lovchi)</div><div class="pp-card-back">~ bo\'lgach (bo\'ysundiruvchi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">afterward</div><div class="pp-card-back">keyin (RAVISH — bog\'lay olmaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">on pain of ~</div><div class="pp-card-back">~ jazosi ostida</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">linseed oil</div><div class="pp-card-back">zig\'ir moyi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to stand proud of ~</div><div class="pp-card-back">~ dan biroz bo\'rtib turmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">compulsory</div><div class="pp-card-back">majburiy</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the shallows</div><div class="pp-card-back">sayozlik</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Ergash oldinda → vergul shart.</strong> "
              "<strong>Ergash orqada → vergul yo'q.</strong></li>"
              "<li><em>because · although · when · if · since · once</em> "
              "<u>dan keyin</u> hech qachon vergul qo'yilmaydi.</li>"
              "<li>Bo'sh joydan keyin vergul turgan bo'lsa — chap tomon "
              "ergash bo'lishi kerak.</li>"
              "<li>Ravish (<em>afterward · however · therefore</em>) gapni "
              "ergashga <u>aylantira olmaydi</u>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 35
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_BOUND,
    "title": "SAT R&W W35: Sentence Boundaries — Mixed Practice",
    "summary": "Oltita savol, barcha chegara holatlari aralash, imtihon tezligida: "
               "30–34-darslarni soatga qarshi mustahkamlash.",
    "order": 35,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol. Har birida bir xil boshlanish:</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Har savolda shu "
                "tartib:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li><strong>Variantlar orasidagi farqqa qarang</strong> — "
                "u savolning mavzusini aytadi (W1).</li>"
                "<li><strong>Ikki gap sinovi:</strong> chap mustaqilmi? "
                "o'ng mustaqilmi? (30-dars)</li>"
                "<li>Jadvaldan ruxsat etilgan belgilarni oling.</li>"
                "<li>Ikki belgi birga qo'yilgan variantni "
                "o'chiring.</li>"
                "</ol>")
            + "<p>Bu tur imtihonda eng tez yechiladiganlardan. Taymer: "
            "<strong>3 daqiqa</strong> (6 × 30 soniya).</p>"
            + '<span class="sr-time">⏱ 6 savol · 3 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Boundaries") + conv_q(
                "<p>The cathedral's west front was left unfinished when the money ran "
                "out in 1348, and the two towers reach different "
                "<span class=\"sr-blank\"></span> the shorter one carries a temporary "
                "roof that has now stood for six hundred years.</p>"),
            "choices": [
                {"text": "heights;", "is_correct": True},
                {"text": "heights,", "is_correct": False},
                {"text": "heights", "is_correct": False},
                {"text": "heights, and;", "is_correct": False},
            ],
            "explanation": (
                "<p>Chap mustaqil, o'ng mustaqil (<em>the shorter one "
                "carries…</em>). Birinchi qator: <strong>.</strong> · "
                "<strong>;</strong> · <strong>,</strong>+FANBOYS.</p>"
                + why([
                    (True, "heights;",
                     "nuqtali vergul — ikki zich bog'liq mustaqil gap "
                     "uchun."),
                    (False, "heights,",
                     "<strong>vergul splaysi.</strong>"),
                    (False, "heights",
                     "<em>run-on</em>."),
                    (False, "heights, and;",
                     "ikkita ulash birga."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Boundaries") + conv_q(
                "<p>Although the recipe survives in three manuscripts and each names the "
                "same five <span class=\"sr-blank\"></span> none of them gives a quantity "
                "for any of them.</p>"),
            "choices": [
                {"text": "ingredients,", "is_correct": True},
                {"text": "ingredients;", "is_correct": False},
                {"text": "ingredients", "is_correct": False},
                {"text": "ingredients:", "is_correct": False},
            ],
            "explanation": (
                "<p>Birinchi so'z <em>Although</em> — chap tomon "
                "<mark>ergash gap</mark>. O'ng mustaqil.</p>"
                "<p><strong>Ergash → mustaqil</strong> = faqat vergul.</p>"
                + why([
                    (True, "ingredients,",
                     "boshda kelgan ergash gapdan keyingi vergul "
                     "(34-dars)."),
                    (False, "ingredients;",
                     "nuqtali vergul chapdan mustaqil gap talab qiladi."),
                    (False, "ingredients:",
                     "ikki nuqtadan oldin ham to'liq gap kerak."),
                    (False, "ingredients",
                     "belgisiz: ergash gapning tugagani "
                     "ko'rinmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Boundaries") + conv_q(
                "<p>Wooden ships were fastened with iron until the eighteenth century, "
                "when it was noticed that iron and copper together corrode far faster "
                "than either does <span class=\"sr-blank\"></span> a discovery that sent "
                "shipwrights back to wooden pegs for another fifty years.</p>"),
            "choices": [
                {"text": "alone,", "is_correct": True},
                {"text": "alone.", "is_correct": False},
                {"text": "alone;", "is_correct": False},
                {"text": "alone", "is_correct": False},
            ],
            "explanation": (
                "<p>O'ng tomon: <em>a discovery that sent shipwrights "
                "back to wooden pegs</em> — <mark>ot birikmasi</mark>, "
                "gap emas.</p>"
                "<p><strong>Mustaqil + bo'lak</strong> → vergul.</p>"
                + why([
                    (True, "alone,",
                     "vergul appozitsiyani ulaydi."),
                    (False, "alone.",
                     "<strong>fragment</strong> yasaydi (33-dars)."),
                    (False, "alone;",
                     "nuqtali vergul o'ngdan mustaqil gap talab "
                     "qiladi."),
                    (False, "alone",
                     "belgisiz: <em>either does alone a discovery</em> "
                     "bo'lib o'qiladi."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Boundaries") + conv_q(
                "<p>Wax cylinders capture a narrower range of frequencies than modern "
                "recording and wear a little with every playing, "
                "<span class=\"sr-blank\"></span> they remain the only record of how "
                "certain songs were actually sung before 1900.</p>"),
            "choices": [
                {"text": "but", "is_correct": True},
                {"text": "however", "is_correct": False},
                {"text": "and", "is_correct": False},
                {"text": "so", "is_correct": False},
            ],
            "explanation": (
                "<p>Vergul allaqachon qo'yilgan, va ikkala tomon ham "
                "mustaqil. Demak bo'sh joyga <mark>FANBOYS</mark> kerak "
                "— ravish emas.</p>"
                "<p>Ma'no: kamchilik ↔ qiymat. "
                "<strong>Qarama-qarshilik.</strong></p>"
                + why([
                    (True, "but",
                     "haqiqiy bog'lovchi, va ma'nosi to'g'ri: "
                     "kamchiliklariga qaramay qimmatli."),
                    (False, "however",
                     "<strong>ravish, bog'lovchi emas</strong> (31-dars). "
                     "Ma'nosi <em>but</em> bilan bir xil, grammatikasi "
                     "boshqa — savolning butun mohiyati shu."),
                    (False, "and",
                     "bog'lovchi, lekin ma'no noto'g'ri: ikkinchi gap "
                     "birinchisiga qarshi turadi."),
                    (False, "so",
                     "natija: silindrlarning eskirishi ularning yagona "
                     "yozuv ekaniga sabab bo'lmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Boundaries") + conv_q(
                "<p><span class=\"sr-blank\"></span> the surveyors marked the boundary "
                "with cairns of loose stone, and several of those cairns are still "
                "standing where the fence line later ran.</p>"),
            "choices": [
                {"text": "Having no timber and no wire,", "is_correct": True},
                {"text": "They had no timber and no wire,", "is_correct": False},
                {"text": "Having no timber and no wire", "is_correct": False},
                {"text": "They had no timber and no wire and", "is_correct": False},
            ],
            "explanation": (
                "<p>O'ng tomon mustaqil. Chap tomon mustaqil "
                "<u>bo'lmasligi</u> kerak.</p>"
                + why([
                    (True, "Having no timber and no wire,",
                     "sifatdosh bo'lagi + vergul + mustaqil gap "
                     "(33-dars). <em>Having</em> kesim emas, shuning "
                     "uchun splays bo'lmaydi."),
                    (False, "They had no timber and no wire,",
                     "<strong>vergul splaysi:</strong> <em>They had</em> — "
                     "ega + kesim."),
                    (False, "They had no timber and no wire and",
                     "ikki mustaqil gap <em>and</em> bilan, lekin vergulsiz."),
                    (False, "Having no timber and no wire",
                     "bo'lak to'g'ri, vergul yo'q — boshda kelgan "
                     "bo'lakdan keyin u shart (34-dars)."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Boundaries") + conv_q(
                "<p>A well-made scythe blade is not sharpened on a stone in the field "
                "but hammered thin along its edge on a small "
                "<span class=\"sr-blank\"></span> a process that takes twenty minutes and "
                "must be repeated every few days of mowing.</p>"),
            "choices": [
                {"text": "anvil:", "is_correct": True},
                {"text": "anvil;", "is_correct": False},
                {"text": "anvil. A", "is_correct": False},
                {"text": "anvil and", "is_correct": False},
            ],
            "explanation": (
                "<p>O'ng tomon: <em>a process that takes twenty minutes "
                "and must be repeated…</em> — <mark>ot birikmasi</mark>. "
                "Chap tomon mustaqil, va u <em>hammered thin … on a small "
                "anvil</em> deb usulni <u>tasvirlab</u> tugaydi.</p>"
                "<p><strong>Mustaqil + bo'lak</strong> → vergul, ikki "
                "nuqta yoki tire. Bu yerda o'ng tomon chapni "
                "<u>nomlaydi</u> (<em>a process</em>) — ikki nuqta "
                "aniqroq.</p>"
                + why([
                    (True, "anvil:",
                     "ikki nuqtadan oldin to'liq gap bor, va undan "
                     "keyin uni nomlaydigan bo'lak keladi."),
                    (False, "anvil;",
                     "nuqtali vergul ikki mustaqil gap orasida "
                     "bo'ladi."),
                    (False, "anvil. A",
                     "<strong>fragment:</strong> <em>A process that takes "
                     "twenty minutes and must be repeated every few days of "
                     "mowing.</em>"),
                    (False, "anvil and",
                     "<em>and</em> ot birikmasini fe'lga ulay olmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Qaysi darsga qaytish</th></tr></thead>"
              "<tbody>"
              "<tr><td>Vergul splaysini sezmadim</td><td>31-dars</td></tr>"
              "<tr><td><em>however</em> ni bog'lovchi deb oldim</td>"
              "<td>31-dars — ravish va bog'lovchi</td></tr>"
              "<tr><td>Fragmentni gap deb oldim</td><td>33-dars — shaxsli "
              "kesim bormi?</td></tr>"
              "<tr><td>Boshda kelgan ergash gapdan keyin vergul "
              "qo'ymadim</td><td>34-dars</td></tr>"
              "<tr><td>Ikki belgi birga qo'yilgan variantni "
              "tanladim</td><td>30-dars, 32-dars</td></tr>"
              "<tr><td>To'g'ri belgini topdim, lekin ma'nosi noto'g'ri "
              "bog'lovchi edi</td><td>32-dars — FANBOYS ma'nosi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu turdagi savollarni 30 soniyadan uzoq yechayotgan "
                "bo'lsangiz, deyarli har doim bitta sabab bor: "
                "<strong>ikki gap sinovini bajarmadingiz</strong> va "
                "variantlarni «quloqqa» solishtirdingiz. Quloq bu "
                "savollarni yecholmaydi — o'zbek quloq esa "
                "ayniqsa.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a cairn</div><div class="pp-card-back">tosh uyumi (belgi sifatida)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a shipwright</div><div class="pp-card-back">kema ustasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a scythe</div><div class="pp-card-back">o\'roq, chalg\'i</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an anvil</div><div class="pp-card-back">sandon</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to corrode</div><div class="pp-card-back">yemirilmoq, zanglamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a peg</div><div class="pp-card-back">yog\'och mix, qoziq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the west front</div><div class="pp-card-back">g\'arbiy peshtoq (soborda)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">mowing</div><div class="pp-card-back">o\'rish, o\'t o\'rish</div></div>'
            + "</div>"
            + "<h3>Xulosa — Boundaries mavzusi yakuni</h3>"
            + "<ul>"
              "<li>Yagona savol: <strong>chap mustaqilmi? o'ng "
              "mustaqilmi?</strong> (30-dars)</li>"
              "<li><strong>Vergul splaysi</strong> — bu domendagi eng ko'p "
              "sinaladigan xato (31-dars).</li>"
              "<li>Uch qonuniy ulash teng, shuning uchun ikkitasi birga "
              "berilsa — ikkovi ham javob emas (32-dars).</li>"
              "<li><em>-ing</em> va <em>to + fe'l</em> kesim emas "
              "(33-dars).</li>"
              "<li>Ergash oldinda → vergul; orqada → vergul yo'q "
              "(34-dars).</li>"
              "</ul>"
        )},
    ],
},

]
