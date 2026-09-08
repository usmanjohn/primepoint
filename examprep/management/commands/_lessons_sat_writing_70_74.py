# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 70-74.

"Ko'plik, egalik va aniqlovchilar (Plurals, possessives & modifiers)" — the last
skill inside Standard English Conventions, and the last teaching topic of the whole
course before the final mixed practice.

Two unrelated faults share the topic because both are about a word landing in the
wrong place. The apostrophe half (70-71) is pure spelling: -s, -'s and -s' sound
identical and mean three different things. The modifier half (72-73) is about order:
an opening phrase describes whatever noun comes next, and a list must repeat one
shape throughout.

Uzbek marks possession with a suffix on BOTH nouns (kitob-ning muqova-si), so an
apostrophe that floats between the noun and its -s is genuinely new machinery.

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

TOPIC_PLUR = {
    "title":   "Ko'plik, egalik va aniqlovchilar (Plurals, possessives & modifiers)",
    "summary": "Apostrof qayerga tushadi va aniqlovchi qaysi otga tegishli: "
               "-s / -'s / -s' farqi, osilib qolgan bo'lak va parallel qurilish.",
    "icon":    "bi-type",
    "order":   8,
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


def precise_q(passage):
    """Word Choice / precision: the stem the exam uses when a vague pronoun is the fault."""
    return q(passage, "Which choice completes the text with the most logical and precise "
                      "word or phrase?")


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
# Writing 70
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PLUR,
    "title": "SAT R&W W70: Plural or Possessive? students / student's / students'",
    "summary": "Uch shakl bir xil eshitiladi va uch xil narsani anglatadi. "
               "Ularni ajratish uchun ikkita savol yetarli.",
    "order": 70,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta tovush, uchta ma'no</h2>"
            "<p>Ingliz tilida <em>students</em>, <em>student's</em> va "
            "<em>students'</em> <u>bir xil</u> eshitiladi. Yozuvda esa "
            "ular bir-biriga umuman o'xshamaydi:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Shakl</th><th>Nima u</th><th>Ma'nosi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>student<strong>s</strong></em></td>"
              "<td>ko'plik</td><td>talabalar (bir nechta)</td></tr>"
              "<tr><td><em>student<strong>'s</strong></em></td>"
              "<td>bitta egasi</td><td>bitta talabaning</td></tr>"
              "<tr><td><em>students<strong>'</strong></em></td>"
              "<td>ko'p egasi</td><td>talabalarning</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>Three <strong>students</strong> "
                "waited.</em> — nechta? uchta.<br>"
                "<em>The <strong>student's</strong> notebook was "
                "missing.</em> — kimning? bitta talabaning.<br>"
                "<em>The <strong>students'</strong> notebooks were "
                "collected.</em> — kimning? bir nechta "
                "talabaning.</p>")
            + '<span class="sr-time">⏱ ~20 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki savol</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Egalik bormi?</strong> "
              "So'zdan keyin darrov <u>boshqa ot</u> keladimi, va "
              "orasiga «ning» qo'ysa bo'ladimi? Yo'q bo'lsa — "
              "apostrof <u>kerak emas</u>, gap oddiy "
              "ko'plik.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Egasi nechta?</strong> "
              "Bitta bo'lsa <em>-'s</em>, bir nechta bo'lsa "
              "<em>-s'</em>. Egalik qilingan narsa nechta ekani "
              "<u>ahamiyatsiz</u>.</p></div>"
            + '</div>'
            + WARN.format(
                "Eng ko'p uchraydigan xato — oddiy ko'plikka apostrof "
                "qo'yish: <em>The <s>museum's</s> opened at ten</em>. "
                "«Nechta muzey?» degan javob apostrof "
                "talab qilmaydi. Apostrof faqat <strong>«kimning?»</strong> "
                "savoliga javob berganda tushadi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The archive holds the working papers of eleven nineteenth-century "
                "bridge engineers, and the calculations in them are done in pencil on "
                "squared paper. The <span class=\"sr-blank\"></span> arithmetic is "
                "correct almost everywhere, which is remarkable given that every square "
                "root had to be looked up in a printed table and copied out by "
                "hand.</p>")
            + choices_html([
                "engineers",
                "engineer's",
                "engineers'",
                "engineers's",
            ])
            + "<p><strong>1-savol — egalik bormi?</strong> Bo'sh joydan "
            "keyin <em>arithmetic</em> keladi, va «muhandislar<u>ning</u> "
            "hisob-kitobi» ma'nosi chiqadi. Ha, "
            "<mark>egalik</mark>.</p>"
            "<p><strong>2-savol — egasi nechta?</strong> "
            "<em>eleven … bridge engineers</em> — o'n bitta. "
            "<mark>Ko'plik.</mark></p>"
            "<p>Ko'plikda so'z allaqachon <em>-s</em> bilan tugagan, "
            "shuning uchun apostrof <u>oxiriga</u> qo'yiladi va yana "
            "bir <em>s</em> qo'shilmaydi.</p>"
            + why([
                (True, "engineers'",
                 "ko'p egali egalik shakli — o'n bir muhandisning "
                 "hisob-kitobi."),
                (False, "engineers",
                 "oddiy ko'plik: egalikni umuman bildirmaydi. "
                 "«Muhandislar hisob-kitobi» degan birikma "
                 "yasalmaydi."),
                (False, "engineer's",
                 "bitta muhandisning — matn esa o'n bittasi "
                 "haqida."),
                (False, "engineers's",
                 "bunday shakl yo'q: <em>-s</em> bilan tugagan "
                 "ko'plikka faqat apostrof qo'shiladi."),
            ])
            + NOTE.format(
                "Diqqat: <u>egalik qilingan narsa</u> nechta ekani "
                "hech narsani o'zgartirmaydi. "
                "<em>the engineers' <strong>notebook</strong></em> "
                "(bitta daftar) ham, "
                "<em>the engineers' <strong>notebooks</strong></em> "
                "ham bir xil apostrof oladi — apostrofni "
                "<strong>egasi</strong> boshqaradi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Fifteen <span class=\"sr-blank\"></span> stand along the two miles of "
                "the old sea front, each one built to house a single family and later "
                "divided into flats. The ground floors were shops within thirty years, "
                "and only three of the original staircases survive.</p>"),
            "choices": [
                {"text": "houses", "is_correct": True},
                {"text": "house's", "is_correct": False},
                {"text": "houses'", "is_correct": False},
                {"text": "houses's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Bo'sh joydan keyin "
                "darrov <em>stand</em> — <u>kesim</u> keladi, ot "
                "emas. Hech kim hech narsaga ega emas.</p>"
                "<p>Bo'sh joy shunchaki <mark>eganing o'zi</mark>: "
                "«o'n beshta uy turibdi».</p>"
                + why([
                    (True, "houses",
                     "oddiy ko'plik, apostrofsiz — <em>Fifteen</em> "
                     "so'raganidek."),
                    (False, "house's",
                     "<strong>bu darsning bosh xatosi:</strong> "
                     "ko'plikka apostrof qo'yish. Ustiga bu birlik "
                     "shakli, <em>Fifteen</em> esa ko'plik "
                     "talab qiladi."),
                    (False, "houses'",
                     "egalik shakli, lekin egalik qilinadigan ot "
                     "yo'q — undan keyin kesim keladi."),
                    (False, "houses's",
                     "ingliz tilida bunday shakl umuman yo'q."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The company kept one clock in the gatehouse and set every other clock "
                "in the works by it each Monday morning. That "
                "<span class=\"sr-blank\"></span> pendulum was two inches longer than the "
                "standard, so the whole factory ran four minutes slow for eleven years "
                "without anyone noticing.</p>"),
            "choices": [
                {"text": "clock's", "is_correct": True},
                {"text": "clocks", "is_correct": False},
                {"text": "clocks'", "is_correct": False},
                {"text": "clocks's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Ha — "
                "<em>___ pendulum</em>, «soat<u>ning</u> mayatnigi».</p>"
                "<p><strong>Egasi nechta?</strong> <em>That</em> "
                "ko'rsatib turibdi: <mark>bitta</mark> soat — "
                "darvozaxonadagisi.</p>"
                + why([
                    (True, "clock's",
                     "bitta egali egalik shakli — <em>That</em> "
                     "bilan mos, va undan keyin ot keladi."),
                    (False, "clocks",
                     "ko'plik: egalikni bildirmaydi, va "
                     "<em>That</em> bilan ham mos "
                     "kelmaydi."),
                    (False, "clocks'",
                     "ko'p egali shakl — matn esa aynan bitta "
                     "soatni ko'rsatyapti."),
                    (False, "clocks's",
                     "bunday shakl yo'q."),
                ])
                + TIP.format(
                    "<strong><em>That · this · a · one</em> so'zlari "
                    "birlikni ochiq aytadi</strong>, "
                    "<em>these · those · both · several</em> esa "
                    "ko'plikni. Bo'sh joydan oldingi so'z ko'pincha "
                    "javobning yarmini bepul beradi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A parish was allowed one licensed alehouse for every hundred people, and "
                "the licence was attached to the building rather than to the keeper. A "
                "<span class=\"sr-blank\"></span> list of licences therefore doubles as a "
                "list of its larger houses, and the same addresses appear on it for a "
                "century at a time.</p>"),
            "choices": [
                {"text": "parish's", "is_correct": True},
                {"text": "parishes", "is_correct": False},
                {"text": "parishes'", "is_correct": False},
                {"text": "parish", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Ha — <em>a ___ list "
                "of licences</em>, «prixod<u>ning</u> ro'yxati».</p>"
                "<p><strong>Egasi nechta?</strong> Oldida "
                "<em>a</em> artikli turibdi — u faqat "
                "<mark>birlik</mark> bilan keladi. Va davomidagi "
                "<em><u>its</u> larger houses</em> ham birlikni "
                "tasdiqlaydi.</p>"
                + why([
                    (True, "parish's",
                     "birlik egalik shakli — <em>a</em> artikli, "
                     "keyingi ot va <em>its</em> uchalasiga ham "
                     "mos."),
                    (False, "parishes",
                     "ko'plik va egaliksiz: <em>a parishes list</em> "
                     "ikki jihatdan buzuq."),
                    (False, "parishes'",
                     "ko'p egali shakl — <em>a</em> va <em>its</em> "
                     "bilan birga kelolmaydi."),
                    (False, "parish",
                     "egalikni umuman bildirmaydi: <em>a parish "
                     "list</em> boshqa narsani anglatadi."),
                ])
                + NOTE.format(
                    "<em>parish</em> ning ko'pligi <em>parishes</em> — "
                    "<em>-sh</em> bilan tugagan otlarga <em>-es</em> "
                    "qo'shiladi. Egalikda esa u allaqachon "
                    "<em>s</em> bilan tugaganidan faqat apostrof "
                    "oladi: <em>parishes'</em>.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Rope used to be laid in a walk a quarter of a mile long, because the "
                "strands had to be stretched their full length before they were twisted "
                "together. Most surviving <span class=\"sr-blank\"></span> are now roads "
                "or long terraces of houses, and the street name is often the only sign "
                "of what once stood there.</p>"),
            "choices": [
                {"text": "walks", "is_correct": True},
                {"text": "walk's", "is_correct": False},
                {"text": "walks'", "is_correct": False},
                {"text": "walk", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Bo'sh joydan keyin "
                "<em>are</em> keladi — kesim, ot emas. Hech kim "
                "hech narsaga ega emas.</p>"
                "<p>Va <em>Most surviving …</em> ko'plikni talab "
                "qiladi; <em>are</em> ham buni "
                "tasdiqlaydi.</p>"
                + why([
                    (True, "walks",
                     "oddiy ko'plik, apostrofsiz — <em>Most</em> va "
                     "<em>are</em> bilan mos."),
                    (False, "walk's",
                     "apostrof egalik demak, lekin egalik "
                     "qilinadigan ot yo'q; ustiga bu birlik "
                     "shakli."),
                    (False, "walks'",
                     "ko'p egali egalik shakli — yana ot kerak "
                     "bo'lardi."),
                    (False, "walk",
                     "birlik: <em>Most … are</em> bilan mos "
                     "kelmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a possessive</div><div class="pp-card-back">egalik shakli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a plural</div><div class="pp-card-back">ko\'plik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">squared paper</div><div class="pp-card-back">katakli qog\'oz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a pendulum</div><div class="pp-card-back">mayatnik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cooper</div><div class="pp-card-back">bochkasoz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a stave</div><div class="pp-card-back">bochka taxtasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a gatehouse</div><div class="pp-card-back">darvozaxona</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">output</div><div class="pp-card-back">ishlab chiqarilgan mahsulot</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Apostrof faqat <strong>«kimning?»</strong> savoliga "
              "javob berganda tushadi.</li>"
              "<li>Bo'sh joydan keyin <u>ot</u> kelmasa — apostrof "
              "kerak emas.</li>"
              "<li>Bitta egasi → <em>-'s</em>. Ko'p egasi (allaqachon "
              "<em>-s</em> bilan tugagan) → <em>-s'</em>.</li>"
              "<li>Egalik qilingan narsa nechta ekani "
              "<u>ahamiyatsiz</u>.</li>"
              "<li><em>a · that · one</em> = birlik; "
              "<em>these · both · several</em> = ko'plik.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 71
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PLUR,
    "title": "SAT R&W W71: Possessive Nouns With Irregular Plurals (children's, women's)",
    "summary": "Ko'pligi -s bilan tugamagan otlar egalikda -'s oladi. Bitta "
               "qoida, ikkita qadam, hech qanday istisno.",
    "order": 71,
    "blocks": [
        {"rich_text": (
            "<h2>Avval ko'plikni yasang, keyin apostrofni qo'ying</h2>"
            "<p>70-darsdagi qoida to'liq emas edi. To'lig'i shunday, va "
            "u istisnosiz ishlaydi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>1. Avval "
                "kerakli shaklni yozing (birlik yoki ko'plik).<br>"
                "2. Agar u <em>-s</em> bilan tugagan bo'lsa — faqat "
                "apostrof. Tugamagan bo'lsa — "
                "<em>-'s</em>.</strong></p>")
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Birlik</th><th>Ko'plik</th>"
              "<th>Ko'plik egalik</th></tr></thead>"
              "<tbody>"
              "<tr><td>student</td><td>student<strong>s</strong></td>"
              "<td>students<strong>'</strong></td></tr>"
              "<tr><td>child</td><td>child<strong>ren</strong></td>"
              "<td>children<strong>'s</strong></td></tr>"
              "<tr><td>woman</td><td>wom<strong>e</strong>n</td>"
              "<td>women<strong>'s</strong></td></tr>"
              "<tr><td>man</td><td>m<strong>e</strong>n</td>"
              "<td>men<strong>'s</strong></td></tr>"
              "<tr><td>mouse</td><td>m<strong>i</strong>ce</td>"
              "<td>mice<strong>'s</strong></td></tr>"
              "<tr><td>goose</td><td>g<strong>ee</strong>se</td>"
              "<td>geese<strong>'s</strong></td></tr>"
              "<tr><td>person</td><td>people</td>"
              "<td>people<strong>'s</strong></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + '<span class="sr-time">⏱ ~20 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Nega bu chalkash tuyuladi</h3>"
            "<p>Chunki apostrof <u>ko'plikni</u> emas, "
            "<u>tovushni</u> kuzatadi. Qoida aslida quloq uchun "
            "yozilgan: <strong>oxirida <em>s</em> tovushi bormi?</strong></p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><em>children</em> — oxirida "
              "<em>s</em> yo'q → <em>children<strong>'s</strong> "
              "books</em>.</p></div>"
            + "<div class=\"pp-step\"><p><em>students</em> — oxirida "
              "<em>s</em> bor → <em>students<strong>'</strong> "
              "books</em>.</p></div>"
            + "<div class=\"pp-step\"><p><strong><em>childrens'</em> "
              "degan so'z yo'q</strong>, chunki <em>childrens</em> "
              "degan ko'plik ham yo'q. Xato shu yerdan boshlanadi: "
              "noto'g'ri ko'plikdan.</p></div>"
            + '</div>'
            + WARN.format(
                "SAT bu qoidani deyarli har doim <u>bitta</u> shaklda "
                "so'raydi: variantlar orasida <em>children's</em> va "
                "<em>childrens'</em> yonma-yon turadi. Ikkinchisi "
                "har doim xato — ingliz tilida bunday so'z "
                "yo'q.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The shoes found under the floor of the farmhouse were not a pair. Two "
                "were adult sizes and four were small, and the wear on all six was "
                "different. The <span class=\"sr-blank\"></span> shoes had been mended at "
                "the toe more than once, which is why the archaeologists think the house "
                "was occupied for at least a generation.</p>")
            + choices_html([
                "childrens",
                "children's",
                "childrens'",
                "childs'",
            ])
            + "<p><strong>1-qadam — kerakli shakl:</strong> bir nechta "
            "bola, ya'ni ko'plik. <em>child</em> ning ko'pligi — "
            "<mark>children</mark>.</p>"
            "<p><strong>2-qadam — oxirida <em>s</em> bormi?</strong> "
            "<em>children</em> <em>n</em> bilan tugaydi. Demak "
            "<em>-'s</em>.</p>"
            + why([
                (True, "children's",
                 "to'g'ri ko'plik + <em>-'s</em>. Ikki qadam ham "
                 "bajarildi."),
                (False, "childrens'",
                 "<strong>eng ko'p tanlanadigan xato:</strong> u "
                 "<em>childrens</em> degan so'z bordek "
                 "ko'rsatadi. Bunday so'z yo'q."),
                (False, "childrens",
                 "ham noto'g'ri ko'plik, ham egaliksiz."),
                (False, "childs'",
                 "<em>childs</em> degan ko'plik ham yo'q — "
                 "<em>child</em> tartibsiz otlardan."),
            ])
            + NOTE.format(
                "Diqqat: matn <u>egalik qilingan narsani</u> "
                "ko'plikda beradi (<em>shoes</em>), lekin bu javobga "
                "ta'sir qilmaydi. Apostrofni har doim "
                "<strong>egasi</strong> boshqaradi — 70-darsdagi "
                "o'sha qoida.")
        )},

        {
            "rich_text": conv_q(
                "<p>The guild ran one almshouse for retired members and a second for their "
                "widows, and kept a separate account book for each. The "
                "<span class=\"sr-blank\"></span> book records eight shillings a week for "
                "bread and one for coal, and the amounts do not change between 1804 and "
                "1839 even though prices did.</p>"),
            "choices": [
                {"text": "women's", "is_correct": True},
                {"text": "womens'", "is_correct": False},
                {"text": "womans'", "is_correct": False},
                {"text": "womens", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'plik:</strong> <em>woman</em> → "
                "<mark>women</mark> (unlisi o'zgaradi, "
                "<em>-s</em> qo'shilmaydi).</p>"
                "<p><strong>Oxirida <em>s</em> bormi?</strong> "
                "Yo'q — <em>n</em> bilan tugaydi. Demak "
                "<em>-'s</em>.</p>"
                + why([
                    (True, "women's",
                     "to'g'ri ko'plik + <em>-'s</em>."),
                    (False, "womens'",
                     "<em>womens</em> degan so'z yo'q, shuning "
                     "uchun undan yasalgan egalik ham yo'q."),
                    (False, "womans'",
                     "<em>womans</em> ham ko'plik emas — "
                     "<em>woman</em> tartibsiz ot."),
                    (False, "womens",
                     "noto'g'ri ko'plik va apostrofsiz."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Barn owls hunt by ear rather than by eye, and one ear opening sits "
                "slightly higher than the other so that a sound reaches the two at "
                "different moments. Much of what they catch is never seen at all before it "
                "is taken. The <span class=\"sr-blank\"></span> tunnels under a hayfield "
                "give them away in complete darkness.</p>"),
            "choices": [
                {"text": "mice's", "is_correct": True},
                {"text": "mices", "is_correct": False},
                {"text": "mices'", "is_correct": False},
                {"text": "mouses'", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'plik:</strong> <em>mouse</em> → "
                "<mark>mice</mark>.</p>"
                "<p><strong>Oxirida <em>s</em> bormi?</strong> Yo'q — "
                "<em>e</em> bilan tugaydi. Demak "
                "<em>-'s</em>.</p>"
                + why([
                    (True, "mice's",
                     "to'g'ri ko'plik + <em>-'s</em>. Yozuvda "
                     "g'alati ko'rinadi, lekin qoida bo'yicha "
                     "aynan shunday."),
                    (False, "mices",
                     "<em>mices</em> degan so'z yo'q: "
                     "<em>mice</em> allaqachon ko'plik."),
                    (False, "mices'",
                     "yana o'sha yo'q so'zdan yasalgan."),
                    (False, "mouses'",
                     "<em>mouses</em> ham ko'plik emas — "
                     "<em>mouse</em> tartibsiz ot."),
                ])
                + TIP.format(
                    "Shakl g'alati ko'rinsa ham unga ishoning: "
                    "<em>mice's · geese's · oxen's · people's</em> — "
                    "to'rttasi ham to'g'ri. Qoida ko'zga emas, "
                    "<u>oxirgi harfga</u> qaraydi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Sanitary inspectors in the 1890s measured a street by counting the "
                "taps and drains per house rather than the rooms in it. A single tap in a "
                "court of thirty houses counted as thirty taps in the returns, and the "
                "<span class=\"sr-blank\"></span> figures therefore make the street look far "
                "healthier than the notes the same men wrote up the same "
                "evening.</p>"),
            "choices": [
                {"text": "inspectors'", "is_correct": True},
                {"text": "inspector's", "is_correct": False},
                {"text": "inspectors", "is_correct": False},
                {"text": "inspectors's", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol qoidaning <u>ikkinchi yarmini</u> "
                "sinaydi. <strong>Ko'plik:</strong> "
                "<em>inspectors</em> — muntazam ot, "
                "<em>-s</em> bilan tugaydi.</p>"
                "<p><strong>Oxirida <em>s</em> bor</strong> → faqat "
                "<mark>apostrof</mark>, yana bir <em>s</em> "
                "qo'shilmaydi.</p>"
                "<p>Matn ko'plikni ochiq aytadi: "
                "<em>the same inspectors described</em>.</p>"
                + why([
                    (True, "inspectors'",
                     "muntazam ko'plik + apostrof — hisobotlar bir "
                     "nechta inspektorniki."),
                    (False, "inspector's",
                     "bitta inspektorniki; matn esa ko'plikda "
                     "gapiradi."),
                    (False, "inspectors",
                     "egalikni bildirmaydi, keyin esa ot "
                     "(<em>figures</em>) keladi."),
                    (False, "inspectors's",
                     "<em>-s</em> bilan tugagan ko'plikka ikkinchi "
                     "<em>s</em> qo'shilmaydi."),
                ])
                + NOTE.format(
                    "Ikki dars bitta qoidaning ikki yarmi: "
                    "<strong>avval to'g'ri ko'plikni yozing, keyin "
                    "oxirgi harfga qarang.</strong> "
                    "<em>children</em> → <em>-'s</em>; "
                    "<em>inspectors</em> → <em>'</em>.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A workhouse of the 1840s was really two buildings joined by a wall "
                "with a single door in it, and the two halves were run as separate "
                "institutions with separate accounts. The "
                "<span class=\"sr-blank\"></span> yard held a stone-breaking shed and the "
                "other a laundry, and the door between them was unlocked twice a "
                "year.</p>"),
            "choices": [
                {"text": "men's", "is_correct": True},
                {"text": "mens'", "is_correct": False},
                {"text": "mans'", "is_correct": False},
                {"text": "mens", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'plik:</strong> <em>man</em> → "
                "<mark>men</mark>. Unli o'zgaradi, "
                "<em>-s</em> qo'shilmaydi.</p>"
                "<p><strong>Oxirida <em>s</em> bormi?</strong> Yo'q. "
                "Demak <em>-'s</em>.</p>"
                + why([
                    (True, "men's",
                     "to'g'ri ko'plik + <em>-'s</em>."),
                    (False, "mens'",
                     "<em>mens</em> degan so'z yo'q — bu shakl "
                     "yo'q so'zdan yasalgan."),
                    (False, "mans'",
                     "<em>mans</em> ham ko'plik emas."),
                    (False, "mens",
                     "noto'g'ri ko'plik va apostrofsiz; "
                     "keyin esa ot (<em>yard</em>) keladi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an irregular plural</div><div class="pp-card-back">tartibsiz ko\'plik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an almshouse</div><div class="pp-card-back">kambag\'allar boshpanasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a shilling</div><div class="pp-card-back">shilling (eski ingliz puli)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to mend</div><div class="pp-card-back">yamamoq, tuzatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hayfield</div><div class="pp-card-back">pichanzor</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a sanitary inspector</div><div class="pp-card-back">sanitariya nazoratchisi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the returns (report)</div><div class="pp-card-back">rasmiy hisobot ma\'lumotlari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a court (of houses)</div><div class="pp-card-back">hovli atrofidagi uylar guruhi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Avval ko'plikni to'g'ri yozing</strong> — "
              "xatolarning aksariyati shu yerda "
              "boshlanadi.</li>"
              "<li>Oxirida <em>s</em> bo'lmasa → <em>-'s</em>: "
              "<em>children's · women's · men's · mice's · "
              "people's</em>.</li>"
              "<li>Oxirida <em>s</em> bo'lsa → faqat apostrof: "
              "<em>students' · inspectors'</em>.</li>"
              "<li><em>childrens' · womens' · mices'</em> — "
              "<strong>uchtasi ham mavjud emas</strong>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 72
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PLUR,
    "title": "SAT R&W W72: The Dangling Modifier — Whoever Is Doing It Must Come Next",
    "summary": "Vergulgacha turgan bo'lak verguldan keyingi egani izohlaydi. "
               "Noto'g'ri ega kelsa, gap kulgili yoki ma'nosiz bo'ladi.",
    "order": 72,
    "blocks": [
        {"rich_text": (
            "<h2>Verguldan keyingi birinchi ot</h2>"
            "<p>Ingliz tilida gapning boshida turgan bo'lak "
            "(<em>-ing</em>, <em>-ed</em>, <em>to + fe'l</em> yoki "
            "sifatdosh birikma) "
            "<strong>verguldan keyin darrov keladigan otni</strong> "
            "izohlaydi. Boshqa hech qaysi otni emas.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✓ <em><u>Walking the line at "
                "dawn</u>, <strong>the inspector</strong> found the "
                "broken rail.</em> — kim yurdi? inspektor. "
                "To'g'ri.<br>"
                "✗ <em><u>Walking the line at dawn</u>, "
                "<strong>the broken rail</strong> was easy to "
                "see.</em> — kim yurdi? "
                "<span style=\"color:#dc2626;\">rels</span>. "
                "Kulgili.</p>")
            + "<p>Bu xato <mark>osilib qolgan aniqlovchi</mark> "
            "(dangling modifier) deyiladi, va SAT uni har modulda "
            "bir marta so'raydi.</p>"
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Bir qadamlik sinov</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Bo'lakni o'qing va "
              "«KIM?» deb so'rang.</strong> <em>Trained as a "
              "surveyor…</em> — kim o'qigan?</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Har bir variantning "
              "birinchi otiga qarang.</strong> Javob shu ot bo'lishi "
              "shart. Boshqasi bo'lsa — variant "
              "tushadi.</p></div>"
            + '</div>'
            + WARN.format(
                "SAT bu savolni deyarli har doim shu shaklda beradi: "
                "bo'lak berilgan, bo'sh joy verguldan keyin, va "
                "to'rtta variant to'rt xil ot bilan boshlanadi. "
                "<strong>Variantlarni oxirigacha o'qish shart "
                "emas</strong> — birinchi ot hal qiladi.")
            + TIP.format(
                "Majhul nisbat bu xatoning eng keng tarqalgan "
                "yashirinish joyi: <em>Having been repaired, "
                "<u>the engineer</u> tested the pump</em> — "
                "ta'mirlangani nasos edi, muhandis emas. Variantda "
                "<em>was/were</em> ko'rsangiz, «kim?» savolini yana "
                "bir marta so'rang.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>Trained as a wheelwright and never as an architect, "
                "<span class=\"sr-blank\"></span> He worked entirely from full-size "
                "drawings chalked on the floor of the barn, and no plan of the roof was "
                "ever put on paper.</p>")
            + choices_html([
                "the roof of the tithe barn was designed by Samuel Hall.",
                "Samuel Hall designed the roof of the tithe barn.",
                "the tithe barn's roof shows Samuel Hall's training.",
                "it was Samuel Hall who was asked to design the roof.",
            ])
            + "<p><strong>Bo'lak:</strong> <em>Trained as a "
            "wheelwright and never as an architect…</em></p>"
            "<p><strong>KIM o'qigan?</strong> Samuel Hall — bir "
            "odam. Demak verguldan keyin darrov "
            "<mark>Samuel Hall</mark> turishi kerak.</p>"
            + why([
                (True, "Samuel Hall designed",
                 "verguldan keyingi birinchi ot — Samuel Hall, "
                 "ya'ni g'ildiraksoz bo'lib o'qigan odamning "
                 "o'zi."),
                (False, "the roof of the tithe barn was designed",
                 "tom g'ildiraksoz bo'lib o'qimagan. Majhul nisbat "
                 "asl bajaruvchini gap oxiriga surib "
                 "yuboradi."),
                (False, "the tithe barn's roof shows",
                 "yana tom birinchi o'rinda. Egalik shakli "
                 "(<em>Samuel Hall's</em>) ismni gapga kiritadi, "
                 "lekin uni <u>ega</u> qilmaydi."),
                (False, "it was Samuel Hall who",
                 "verguldan keyingi birinchi so'z — <em>it</em>, "
                 "va u hech kimni izohlamaydi. Ism gapda bor, "
                 "lekin noto'g'ri o'rinda."),
            ])
            + NOTE.format(
                "Uchinchi variant bu savol turining eng nozik "
                "tuzog'i: <em>Samuel Hall<u>'s</u></em> — bu "
                "aniqlovchi, ega emas. Bo'lak <strong>ega</strong>ni "
                "izohlashi kerak, gapda ism qayerdadir "
                "uchraganini emas.")
        )},

        {
            "rich_text": conv_q(
                "<p>Cut off from the mainland for nine months of the year, "
                "<span class=\"sr-blank\"></span> The nearest doctor was a day away in "
                "good weather, and every household kept a chest of remedies that was "
                "restocked once a year from a list agreed at the September meeting.</p>"),
            "choices": [
                {"text": "the islanders learned to set a broken bone themselves.",
                 "is_correct": True},
                {"text": "setting a broken bone was something the islanders learned.",
                 "is_correct": False},
                {"text": "there was no choice but to set a broken bone themselves.",
                 "is_correct": False},
                {"text": "a broken bone had to be set by the islanders themselves.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'lak:</strong> <em>Cut off from the "
                "mainland for nine months of the year…</em></p>"
                "<p><strong>KIM uzilib qolgan?</strong> "
                "<mark>Orol aholisi.</mark> Suyak ham, tanlov ham, "
                "«there» ham emas.</p>"
                + why([
                    (True, "the islanders learned",
                     "verguldan keyingi birinchi ot — "
                     "<em>the islanders</em>. To'qqiz oy uzilib "
                     "qolgan aynan ular."),
                    (False, "setting a broken bone was",
                     "ega — <em>setting</em>, ya'ni «suyak "
                     "solish». Bu jarayon materikdan uzilib "
                     "qolmaydi."),
                    (False, "there was no choice",
                     "<em>there</em> hech kimni bildirmaydi, "
                     "shuning uchun bo'lak hech narsaga "
                     "ulanmaydi."),
                    (False, "a broken bone had to be set",
                     "majhul nisbat: ega — <em>a broken bone</em>. "
                     "Suyak uzilib qolgani ma'nosiz."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Fitted with a second rudder at the stern in 1911, "
                "<span class=\"sr-blank\"></span> The change cost as much as a new engine "
                "and was never repeated on her sister ships, two of which were broken up "
                "within a decade.</p>"),
            "choices": [
                {"text": "the ferry could turn inside her own length.",
                 "is_correct": True},
                {"text": "the harbour master allowed the ferry into the inner basin.",
                 "is_correct": False},
                {"text": "turning inside her own length was suddenly possible.",
                 "is_correct": False},
                {"text": "it became possible for the ferry to turn in the basin.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'lak:</strong> <em>Fitted with a second "
                "rudder at the stern in 1911…</em></p>"
                "<p><strong>NIMAGA ikkinchi rul o'rnatilgan?</strong> "
                "<mark>Parom</mark>ga. Port boshlig'iga ham, "
                "burilishga ham emas.</p>"
                + why([
                    (True, "the ferry could turn",
                     "verguldan keyingi birinchi ot — "
                     "<em>the ferry</em>. Rul unga "
                     "o'rnatilgan."),
                    (False, "the harbour master allowed",
                     "port boshlig'iga rul o'rnatilmagan. Bu "
                     "variant ma'noda mantiqiy tuyuladi, "
                     "grammatikada esa kulgili."),
                    (False, "turning inside her own length was",
                     "ega — <em>turning</em>; burilishga rul "
                     "o'rnatilmaydi."),
                    (False, "it became possible",
                     "<em>it</em> bo'lakni hech qaysi otga "
                     "ulamaydi."),
                ])
                + TIP.format(
                    "Ma'no jihatdan to'g'ri tuyulgan variant "
                    "grammatik jihatdan xato bo'lishi mumkin — bu "
                    "savolning butun mohiyati. Faqat "
                    "<strong>birinchi otga</strong> qarang.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Having sat in a damp cellar for sixty years, "
                "<span class=\"sr-blank\"></span> Nothing else in the collection had "
                "suffered at all, because the rest of the boxes were on shelves two feet "
                "off the floor and the cellar flooded only to the depth of a hand.</p>"),
            "choices": [
                {"text": "the glass negatives had lost their emulsion in patches.",
                 "is_correct": True},
                {"text": "the curator found that the glass negatives had lost their emulsion.",
                 "is_correct": False},
                {"text": "there was serious damage to the glass negatives.",
                 "is_correct": False},
                {"text": "damp had removed the emulsion from the glass negatives in patches.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'lak:</strong> <em>Having sat in a damp "
                "cellar for sixty years…</em></p>"
                "<p><strong>NIMA oltmish yil yotgan?</strong> "
                "<mark>Shisha negativlar.</mark> Kurator ham, namlik "
                "ham emas.</p>"
                + why([
                    (True, "the glass negatives had lost",
                     "verguldan keyingi birinchi ot — "
                     "<em>the glass negatives</em>, ya'ni "
                     "yerto'lada yotgan narsaning o'zi."),
                    (False, "the curator found that",
                     "kurator oltmish yil nam yerto'lada "
                     "o'tirmagan. Negativlar gapda bor, lekin "
                     "ergash gap ichida."),
                    (False, "there was serious damage",
                     "<em>there</em> hech narsani bildirmaydi."),
                    (False, "damp had removed the emulsion",
                     "ega — <em>damp</em>. Namlik yerto'lada "
                     "o'tirmagan; u yerto'laning o'zida "
                     "edi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Working from a single measured drawing and a box of photographs taken "
                "the week before the fire, <span class=\"sr-blank\"></span> The plaster "
                "ceiling took eleven months on its own, and the moulds cut for it are "
                "still stored in the crypt in case the work has to be done again.</p>"),
            "choices": [
                {"text": "a team of six rebuilt the interior over four years.",
                 "is_correct": True},
                {"text": "the interior was rebuilt over four years by a team of six.",
                 "is_correct": False},
                {"text": "four years were needed to rebuild the interior.",
                 "is_correct": False},
                {"text": "rebuilding the interior took a team of six four years.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Bo'lak:</strong> <em>Working from a single "
                "measured drawing and a box of photographs…</em></p>"
                "<p><strong>KIM ishlagan?</strong> "
                "<mark>Olti kishilik guruh.</mark> Ichki bezak ham, "
                "to'rt yil ham, «qayta tiklash» ham ishlay "
                "olmaydi.</p>"
                + why([
                    (True, "a team of six rebuilt",
                     "verguldan keyingi birinchi ot — "
                     "<em>a team of six</em>, ya'ni chizma bilan "
                     "ishlagan odamlar."),
                    (False, "the interior was rebuilt",
                     "majhul nisbat: ega — <em>the interior</em>. "
                     "Ichki bezak fotosuratlar bilan "
                     "ishlamaydi."),
                    (False, "four years were needed",
                     "ega — <em>four years</em>. Yillar chizmadan "
                     "foydalanmaydi."),
                    (False, "rebuilding the interior took",
                     "ega — <em>rebuilding</em>, ya'ni jarayonning "
                     "o'zi. Bu ham chizma bilan "
                     "ishlamaydi."),
                ])
                + NOTE.format(
                    "To'rtta variantning to'rttasi ham bir xil "
                    "faktni aytadi. Farq faqat <strong>kim ega "
                    "bo'lganida</strong> — va aynan shu farq "
                    "javobni belgilaydi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a dangling modifier</div><div class="pp-card-back">osilib qolgan aniqlovchi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a wheelwright</div><div class="pp-card-back">g\'ildiraksoz</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a tithe barn</div><div class="pp-card-back">ushr omboriy (o\'rta asr ombori)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a rudder</div><div class="pp-card-back">rul (kema)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the stern</div><div class="pp-card-back">kemaning orqa qismi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to break up (a ship)</div><div class="pp-card-back">kemani qismlarga ajratmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a glass negative</div><div class="pp-card-back">shisha fotonegativ</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">emulsion</div><div class="pp-card-back">emulsiya (foto qatlam)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Gap boshidagi bo'lak <strong>verguldan keyingi "
              "birinchi otni</strong> izohlaydi.</li>"
              "<li>Bo'lakni o'qing va <strong>«KIM?»</strong> yoki "
              "<strong>«NIMA?»</strong> deb so'rang.</li>"
              "<li>Variantlarning faqat <u>birinchi otiga</u> "
              "qarang — qolgani ahamiyatsiz.</li>"
              "<li>Majhul nisbat va <em>there was…</em> — bu "
              "xatoning ikki asosiy yashirinish joyi.</li>"
              "<li>Egalik shakli (<em>Hall's</em>) ismni ega "
              "qilmaydi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 73
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PLUR,
    "title": "SAT R&W W73: Parallel Structure in Lists and Comparisons",
    "summary": "Ro'yxatdagi bo'laklar bir xil shaklda bo'lishi kerak, va "
               "taqqoslashda faqat bir turdagi narsalar solishtiriladi.",
    "order": 73,
    "blocks": [
        {"rich_text": (
            "<h2>Bir shakl, oxirigacha</h2>"
            "<p>Ro'yxat boshlangan shaklda tugashi kerak. "
            "Ikkinchi bo'lak qanday shaklda bo'lsa, uchinchisi ham "
            "shunday bo'ladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✓ <em>The survey involved "
                "<u>measuring</u> the walls, <u>photographing</u> the "
                "roof and <u>recording</u> every crack.</em><br>"
                "✗ <em>The survey involved <u>measuring</u> the walls, "
                "<u>photographing</u> the roof and "
                "<span style=\"color:#dc2626;\"><u>they "
                "recorded</u></span> every crack.</em></p>")
            + "<p>Xuddi shu qoida taqqoslashda ham ishlaydi, faqat "
            "boshqa nom bilan: <strong>faqat bir turdagi narsalar "
            "solishtiriladi</strong>.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✗ <em>The rainfall in Cardiff is "
                "higher than <u>Norwich</u>.</em> — yog'in shahar "
                "bilan solishtirilyapti.<br>"
                "✓ <em>The rainfall in Cardiff is higher than "
                "<u>that in Norwich</u>.</em></p>")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki turdagi savol</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>Ro'yxat.</strong> "
              "Ro'yxatning <u>oldingi</u> bo'laklariga barmoq "
              "qo'ying. Ular <em>-ing</em> bilan boshlansa, javob "
              "ham <em>-ing</em>. <em>to + fe'l</em> bo'lsa, javob "
              "ham shunday. Ot bo'lsa — ot.</p></div>"
            + "<div class=\"pp-step\"><p><strong>Taqqoslash.</strong> "
              "<em>than · as · like · compared with</em> so'zlarini "
              "qidiring, keyin ikki tomonda <u>nima</u> turganini "
              "ayting. Ikkovi bir turdagi bo'lishi "
              "shart.</p></div>"
            + '</div>'
            + TIP.format(
                "Taqqoslashni <em>that of</em> yoki <em>those of</em> "
                "tuzatadi: <em>higher than <strong>that of</strong> "
                "Norwich</em>, <em>older than <strong>those "
                "of</strong> the north aisle</em>. "
                "<strong><em>that</em> = birlik, <em>those</em> = "
                "ko'plik.</strong>")
            + WARN.format(
                "<em>not only … but also …</em>, <em>either … or …</em>, "
                "<em>both … and …</em> — bu juftliklarning ikki "
                "tomoni ham bir xil shaklda bo'lishi kerak: "
                "<em>not only <u>in the archive</u> but also "
                "<u>in the library</u></em>, "
                "<em>not only <s>in the archive</s> but also "
                "<s>the library holds</s></em> emas.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>A hedge is laid by cutting each stem most of the way through near the "
                "ground, bending it over at an angle of about thirty degrees and "
                "<span class=\"sr-blank\"></span> it between stakes driven every "
                "half-metre. The stems go on growing, and within three years the hedge is "
                "thick enough to hold a bullock.</p>")
            + choices_html([
                "weaving",
                "to weave",
                "the weaving of",
                "then it is woven",
            ])
            + "<p><strong>Ro'yxatning oldingi bo'laklari:</strong> "
            "<em>by <u>cutting</u> …, <u>bending</u> … and ___</em>. "
            "Ikkovi ham <mark><em>-ing</em></mark>.</p>"
            "<p>Uchalasi ham <em>by</em> predlogiga bog'langan, va "
            "predlogdan keyin fe'l faqat <em>-ing</em> shaklida "
            "keladi.</p>"
            + why([
                (True, "weaving",
                 "<em>-ing</em> — ro'yxatning boshqa ikki bo'lagi "
                 "bilan aynan bir shaklda."),
                (False, "to weave",
                 "infinitiv: ro'yxat <em>to cut, to bend, to "
                 "weave</em> bo'lib boshlanganida to'g'ri "
                 "bo'lardi. Bu ro'yxat esa boshqacha "
                 "boshlangan."),
                (False, "the weaving of",
                 "ot birikmasi — shakl ham buziladi, "
                 "<em>it</em> to'ldiruvchisi ham "
                 "osilib qoladi."),
                (False, "then it is woven",
                 "butun boshli gap: ro'yxatning uchinchi bo'lagi "
                 "o'rniga mustaqil gap qo'yilgan."),
            ])
            + NOTE.format(
                "Parallellikni tekshirishning eng tez usuli — "
                "ro'yxatning har bir bo'lagini <u>boshidagi "
                "so'zga ulab</u> alohida o'qish: "
                "<em>by cutting… · by bending… · by weaving…</em> "
                "Uchalasi ham to'g'ri eshitilsa, parallellik "
                "joyida.")
        )},

        {
            "rich_text": conv_q(
                "<p>The three surviving letters describe the winter of 1740 in almost the "
                "same words: the ground froze to a depth of a metre, the mill wheel stood "
                "in solid ice for eleven weeks and <span class=\"sr-blank\"></span>. Hay "
                "was being carried in from two counties away by the end of January, and "
                "two of the three writers mention the same carter by name.</p>"),
            "choices": [
                {"text": "the price of hay doubled twice", "is_correct": True},
                {"text": "doubling twice the price of hay", "is_correct": False},
                {"text": "with the price of hay doubling twice", "is_correct": False},
                {"text": "the price of hay having doubled twice", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ro'yxatning oldingi bo'laklari:</strong> "
                "<em>the ground <u>froze</u> …, the mill wheel "
                "<u>stood</u> … and ___</em>.</p>"
                "<p>Ikkovi ham <mark>ega + shaxsli kesim</mark> — "
                "ya'ni to'liq gap. Uchinchisi ham shunday bo'lishi "
                "kerak.</p>"
                + why([
                    (True, "the price of hay doubled twice",
                     "ega (<em>the price</em>) + shaxsli kesim "
                     "(<em>doubled</em>) — oldingi ikkitasi bilan "
                     "bir shaklda."),
                    (False, "doubling twice the price of hay",
                     "sifatdosh bo'lagi — ro'yxatning shakli "
                     "buziladi."),
                    (False, "with the price of hay doubling twice",
                     "predlogli birikma: ro'yxatning uchinchi "
                     "a'zosi bo'lolmaydi."),
                    (False, "the price of hay having doubled twice",
                     "ega bor, lekin <em>having doubled</em> "
                     "shaxsli kesim emas (54-dars)."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The two aisles of the church were built two hundred years apart, and "
                "the difference shows in the stone. The columns of the south aisle are "
                "noticeably heavier than <span class=\"sr-blank\"></span>, and they carry "
                "a wall that was raised twice.</p>"),
            "choices": [
                {"text": "those of the north aisle", "is_correct": True},
                {"text": "the north aisle", "is_correct": False},
                {"text": "that of the north aisle", "is_correct": False},
                {"text": "those of the north aisle's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima solishtirilyapti?</strong> "
                "<em>The columns of the south aisle</em> — "
                "<mark>ustunlar</mark>. Demak ikkinchi tomonda ham "
                "ustunlar turishi kerak, nef emas.</p>"
                "<p><strong>Son:</strong> ustunlar ko'plikda → "
                "<em>those</em>.</p>"
                + why([
                    (True, "those of the north aisle",
                     "<em>those</em> = <em>the columns</em>. "
                     "Ustun ustun bilan solishtirildi, va son "
                     "ham to'g'ri."),
                    (False, "the north aisle",
                     "<strong>bu darsning bosh tuzog'i:</strong> "
                     "ustunlar butun nef bilan "
                     "solishtirilyapti."),
                    (False, "that of the north aisle",
                     "tuzatish to'g'ri yo'nalishda, lekin "
                     "<em>that</em> birlik — <em>columns</em> "
                     "esa ko'plik."),
                    (False, "those of the north aisle's",
                     "<em>of</em> va egalik apostrofi bir vaqtda "
                     "ishlatilgan — bunday qo'sh egalik "
                     "yasalmaydi."),
                ])
                + TIP.format(
                    "Taqqoslash savollarida <em>than</em> dan keyingi "
                    "so'zni o'qing va <strong>«bu nima bilan "
                    "solishtirilyapti?»</strong> deb so'rang. "
                    "Javob «shahar bilan», «bino bilan» chiqsa-yu, "
                    "gapning boshida «yog'in», «ustunlar» tursa — "
                    "<em>that of</em> yoki <em>those of</em> "
                    "kerak.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A parish clerk was expected not only to keep the register but also "
                "<span class=\"sr-blank\"></span> the church clock, and in many villages "
                "he was paid separately for each. The two duties were often split between "
                "two men after 1850, when clocks with a longer going period made the "
                "second job a weekly one rather than a daily one.</p>"),
            "choices": [
                {"text": "to wind", "is_correct": True},
                {"text": "winding", "is_correct": False},
                {"text": "he wound", "is_correct": False},
                {"text": "the winding of", "is_correct": False},
            ],
            "explanation": (
                "<p><em>not only … but also …</em> — juftlikning ikki "
                "tomoni bir xil shaklda bo'lishi shart.</p>"
                "<p><strong>Birinchi tomon:</strong> <em>not only "
                "<u>to keep</u> the register</em> — infinitiv. "
                "Demak ikkinchi tomon ham "
                "<mark>infinitiv</mark>.</p>"
                + why([
                    (True, "to wind",
                     "infinitiv — <em>to keep</em> bilan aynan bir "
                     "shaklda."),
                    (False, "winding",
                     "<em>-ing</em>: ro'yxat <em>not only keeping … "
                     "but also winding</em> bo'lganida to'g'ri "
                     "bo'lardi, lekin birinchi tomon "
                     "boshqacha."),
                    (False, "he wound",
                     "ega + kesim: juftlikning bir tomoniga to'liq "
                     "gap qo'yilgan."),
                    (False, "the winding of",
                     "ot birikmasi — shakl mos kelmaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Rainfall on the western slope of the range is roughly three times "
                "<span class=\"sr-blank\"></span>, and almost all of the difference falls "
                "between October and March. Farms on the two sides grow entirely "
                "different crops, and the boundary between them is visible from the "
                "air.</p>"),
            "choices": [
                {"text": "that on the eastern slope", "is_correct": True},
                {"text": "the eastern slope", "is_correct": False},
                {"text": "those on the eastern slope", "is_correct": False},
                {"text": "the eastern one", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima solishtirilyapti?</strong> "
                "<em>Rainfall on the western slope</em> — "
                "<mark>yog'in</mark>. Demak ikkinchi tomonda ham "
                "yog'in turishi kerak, yonbag'ir emas.</p>"
                "<p><strong>Son:</strong> <em>rainfall</em> — "
                "sanalmaydigan, ya'ni birlik → <em>that</em>.</p>"
                + why([
                    (True, "that on the eastern slope",
                     "<em>that</em> = <em>the rainfall</em>. Yog'in "
                     "yog'in bilan solishtirildi."),
                    (False, "the eastern slope",
                     "yog'in miqdori butun yonbag'ir bilan "
                     "solishtirilyapti — «yog'in yonbag'irdan uch "
                     "baravar ko'p» degan ma'nosizlik."),
                    (False, "those on the eastern slope",
                     "tuzatish to'g'ri yo'nalishda, lekin "
                     "<em>those</em> ko'plik; <em>rainfall</em> "
                     "sanalmaydigan ot."),
                    (False, "the eastern one",
                     "yana o'sha xato: yog'in miqdori yonbag'ir "
                     "bilan solishtirilyapti, faqat qisqaroq "
                     "shaklda."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">parallel structure</div><div class="pp-card-back">parallel qurilish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to lay a hedge</div><div class="pp-card-back">jonli devorni yotqizib o\'stirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a stake</div><div class="pp-card-back">qoziq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a bullock</div><div class="pp-card-back">yosh buqa</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an aisle</div><div class="pp-card-back">yon nef (cherkovda)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a column</div><div class="pp-card-back">ustun</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to wind a clock</div><div class="pp-card-back">soatni burab qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a going period</div><div class="pp-card-back">soatning bir burashda yurish muddati</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Ro'yxatning oldingi bo'laklariga qarang — javob "
              "<strong>o'sha shaklda</strong>.</li>"
              "<li>Har bir bo'lakni boshidagi so'zga ulab alohida "
              "o'qing.</li>"
              "<li>Taqqoslashda ikki tomon <strong>bir "
              "turdagi</strong> bo'lishi shart.</li>"
              "<li><em>that of</em> = birlik, <em>those of</em> = "
              "ko'plik.</li>"
              "<li><em>not only … but also · either … or · both … "
              "and</em> — ikki tomoni bir "
              "shaklda.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 74
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PLUR,
    "title": "SAT R&W W74: Plurals, Possessives and Modifiers — Mixed Practice",
    "summary": "Olti savol aralash: apostrof, tartibsiz ko'plik, osilib qolgan "
               "bo'lak va parallellik. Bu mavzuning yakuni.",
    "order": 74,
    "blocks": [
        {"rich_text": (
            "<h2>Aralash mashq</h2>"
            "<p>Bu mavzu ikki xil nuqsonni birga o'rgatdi: "
            "<strong>apostrof</strong> (qayerga tushadi) va "
            "<strong>o'rin</strong> (qaysi so'z qaysi otga "
            "tegishli). Variantlar qaysi biri ekanini darrov "
            "aytadi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Variantlar shunday farq qilsa</th>"
              "<th>Savol shu haqda</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>-s · -'s · -s'</em></td>"
              "<td>ko'plik yoki egalik</td><td>70</td></tr>"
              "<tr><td><em>children's · childrens'</em></td>"
              "<td>tartibsiz ko'plik</td><td>71</td></tr>"
              "<tr><td>butun gaplar, har biri boshqa ot bilan "
              "boshlanadi</td>"
              "<td>osilib qolgan bo'lak</td><td>72</td></tr>"
              "<tr><td><em>-ing · to + fe'l · that of · those "
              "of</em></td>"
              "<td>parallellik yoki taqqoslash</td><td>73</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + '<span class="sr-time">⏱ 6 savol · ~5 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Apostrof") + conv_q(
                "<p>Nine <span class=\"sr-blank\"></span> were sunk along the same seam "
                "between 1861 and 1884, and only two of them ever paid. The rest struck "
                "water before they reached coal, and the pumping engines cost more each "
                "year than the coal was worth.</p>"),
            "choices": [
                {"text": "pits", "is_correct": True},
                {"text": "pit's", "is_correct": False},
                {"text": "pits'", "is_correct": False},
                {"text": "pits's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Bo'sh joydan keyin "
                "<em>were sunk</em> — kesim keladi, ot emas. "
                "Apostrof kerak emas.</p>"
                "<p><em>Nine</em> ko'plikni talab qiladi.</p>"
                + why([
                    (True, "pits",
                     "oddiy ko'plik, apostrofsiz."),
                    (False, "pit's",
                     "apostrof egalik demak — lekin egalik "
                     "qilinadigan ot yo'q, va bu birlik "
                     "shakli."),
                    (False, "pits'",
                     "ko'p egali egalik shakli; yana ot kerak "
                     "bo'lardi."),
                    (False, "pits's",
                     "bunday shakl yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Osilib qolgan bo'lak") + conv_q(
                "<p>Rebuilt after the flood of 1852 with the arches a foot higher than "
                "before, <span class=\"sr-blank\"></span> The two older piers were left "
                "standing and can still be told from the rest by the colour of the "
                "stone.</p>"),
            "choices": [
                {"text": "the bridge has never been overtopped since.",
                 "is_correct": True},
                {"text": "the county has never had to close the bridge since.",
                 "is_correct": False},
                {"text": "there has been no flooding of the bridge since.",
                 "is_correct": False},
                {"text": "flooding has not reached the bridge since.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>NIMA qayta qurilgan?</strong> "
                "<mark>Ko'prik.</mark> Grafliksiz ham, toshqin ham "
                "qayta qurilmagan.</p>"
                "<p>Demak verguldan keyin darrov "
                "<em>the bridge</em> turishi kerak (72-dars).</p>"
                + why([
                    (True, "the bridge has never been overtopped",
                     "verguldan keyingi birinchi ot — "
                     "<em>the bridge</em>."),
                    (False, "the county has never had to close",
                     "graflik qayta qurilmagan; ko'prik gapda "
                     "bor, lekin to'ldiruvchi "
                     "o'rnida."),
                    (False, "there has been no flooding",
                     "<em>there</em> hech narsani "
                     "bildirmaydi."),
                    (False, "flooding has not reached",
                     "ega — <em>flooding</em>; toshqin qayta "
                     "qurilmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Tartibsiz ko'plik") + conv_q(
                "<p>The hospital kept its two wards on different floors and its accounts "
                "in different books. The <span class=\"sr-blank\"></span> ward was on the "
                "ground floor because the beds had to be carried out into the garden in "
                "hot weather, and the ledger for it stops abruptly in 1871.</p>"),
            "choices": [
                {"text": "children's", "is_correct": True},
                {"text": "childrens'", "is_correct": False},
                {"text": "childrens", "is_correct": False},
                {"text": "childs", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ko'plik:</strong> <em>child</em> → "
                "<mark>children</mark>. <strong>Oxirida "
                "<em>s</em> bormi?</strong> Yo'q → "
                "<em>-'s</em>.</p>"
                + why([
                    (True, "children's",
                     "to'g'ri ko'plik + <em>-'s</em>."),
                    (False, "childrens'",
                     "<em>childrens</em> degan so'z yo'q, "
                     "shuning uchun bu shakl ham yo'q."),
                    (False, "childrens",
                     "noto'g'ri ko'plik va egaliksiz."),
                    (False, "childs",
                     "<em>child</em> tartibsiz ot — "
                     "<em>childs</em> degan ko'plik yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Parallellik") + conv_q(
                "<p>A thatcher works from the eaves upwards, laying each course so that "
                "it covers the fixings of the one below, driving the spars in at an angle "
                "and <span class=\"sr-blank\"></span> the whole surface flat with a "
                "wooden bat. The last course at the ridge is the only one that shows any "
                "fixing at all.</p>"),
            "choices": [
                {"text": "beating", "is_correct": True},
                {"text": "to beat", "is_correct": False},
                {"text": "he beats", "is_correct": False},
                {"text": "the beating of", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ro'yxatning oldingi bo'laklari:</strong> "
                "<em><u>laying</u> each course …, <u>driving</u> the "
                "spars … and ___</em> — ikkovi ham "
                "<mark><em>-ing</em></mark>.</p>"
                + why([
                    (True, "beating",
                     "<em>-ing</em> — boshqa ikki bo'lak bilan bir "
                     "shaklda."),
                    (False, "to beat",
                     "infinitiv: ro'yxat boshqacha "
                     "boshlangan."),
                    (False, "he beats",
                     "ega + kesim — ro'yxatning uchinchi a'zosi "
                     "o'rniga mustaqil gap."),
                    (False, "the beating of",
                     "ot birikmasi; shakl mos "
                     "kelmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Taqqoslash") + conv_q(
                "<p>The bells of the older tower are heavier than "
                "<span class=\"sr-blank\"></span> by about a hundredweight each, which is "
                "why the two rings have never been used together. A single ringer can "
                "manage either, but nobody has found a way of matching the "
                "speeds.</p>"),
            "choices": [
                {"text": "those of the newer one", "is_correct": True},
                {"text": "the newer one", "is_correct": False},
                {"text": "that of the newer one", "is_correct": False},
                {"text": "the newer towers", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima solishtirilyapti?</strong> "
                "<em>The bells</em> — <mark>qo'ng'iroqlar</mark>. "
                "Demak ikkinchi tomonda ham qo'ng'iroqlar turishi "
                "kerak, minora emas.</p>"
                "<p><strong>Son:</strong> ko'plik → "
                "<em>those</em>.</p>"
                + why([
                    (True, "those of the newer one",
                     "<em>those</em> = <em>the bells</em>; ko'plik "
                     "ham to'g'ri."),
                    (False, "the newer one",
                     "qo'ng'iroqlar butun minora bilan "
                     "solishtirilyapti."),
                    (False, "that of the newer one",
                     "to'g'ri yo'nalish, noto'g'ri son: "
                     "<em>bells</em> ko'plik."),
                    (False, "the newer towers",
                     "minoralar bilan solishtirish ham xato, va "
                     "matnda ikkinchi minora bitta — ko'plik "
                     "ham noto'g'ri."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Apostrof") + conv_q(
                "<p>Brickyards dug their clay from the field next to them and burned it in "
                "a kiln on the same site, so the colour of a wall is a fair guide to how "
                "far the bricks travelled. The <span class=\"sr-blank\"></span> output was "
                "sold within four miles, and a red terrace beside a yellow one usually "
                "means a change of supplier rather than a change of fashion.</p>"),
            "choices": [
                {"text": "yards'", "is_correct": True},
                {"text": "yard's", "is_correct": False},
                {"text": "yards", "is_correct": False},
                {"text": "yards's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Egalik bormi?</strong> Ha — <em>___ "
                "output</em>, «zavodlar<u>ning</u> "
                "mahsuloti».</p>"
                "<p><strong>Egasi nechta?</strong> Matn butun "
                "hunar haqida gapiryapti, va gapning davomi "
                "<em>a change of supplier</em> deydi — demak "
                "<mark>bir nechta</mark> zavod. Muntazam ko'plik "
                "<em>-s</em> bilan tugagani uchun faqat "
                "apostrof.</p>"
                + why([
                    (True, "yards'",
                     "ko'p egali egalik shakli — ko'plab "
                     "g'ishtxonalarning mahsuloti."),
                    (False, "yard's",
                     "bitta zavodniki; matn esa umumiy "
                     "amaliyotni tasvirlaydi va bir nechta "
                     "yetkazib beruvchini nazarda "
                     "tutadi."),
                    (False, "yards",
                     "egalikni bildirmaydi, keyin esa ot "
                     "(<em>output</em>) keladi."),
                    (False, "yards's",
                     "<em>-s</em> bilan tugagan ko'plikka "
                     "ikkinchi <em>s</em> qo'shilmaydi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Mavzu yakuni — Ko'plik, egalik va aniqlovchilar</h3>"
            + TIP.format(
                "Ikkita savol butun mavzuni yopadi. Apostrof uchun: "
                "<strong>«Kimning?» degan savol bormi, va egasi "
                "nechta?»</strong> O'rin uchun: <strong>«Bu bo'lak "
                "qaysi otga tegishli, va u verguldan keyin darrov "
                "turibdimi?»</strong>")
            + "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a seam (coal)</div><div class="pp-card-back">ko\'mir qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to sink a pit</div><div class="pp-card-back">shaxta qazimoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a pier (bridge)</div><div class="pp-card-back">ko\'prik tayanchi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to overtop</div><div class="pp-card-back">(suv) ustidan oshib o\'tmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ward</div><div class="pp-card-back">kasalxona bo\'limi, palata</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a thatcher</div><div class="pp-card-back">somon tom yopuvchi usta</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the eaves</div><div class="pp-card-back">tomning pastki cheti</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a brickyard</div><div class="pp-card-back">g\'isht zavodi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Apostrof faqat <strong>«kimning?»</strong> savoliga "
              "javob berganda.</li>"
              "<li>Avval to'g'ri ko'plikni yozing, keyin oxirgi "
              "harfga qarang.</li>"
              "<li>Gap boshidagi bo'lak <strong>verguldan keyingi "
              "birinchi otni</strong> izohlaydi.</li>"
              "<li>Ro'yxat bir shaklda tugaydi; taqqoslashda "
              "<em>that of</em> yoki <em>those of</em>.</li>"
              "</ul>"
        )},
    ],
},
]
