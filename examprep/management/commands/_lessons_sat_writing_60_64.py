# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 60-64.

"Olmoshlar va moslashuv (Pronouns & agreement)" — the third skill inside Standard
English Conventions. The verb topic asked which word is the subject; this one asks
which word the pronoun POINTS AT, and whether the pronoun's form matches it.

Three faults carry the whole topic: a pronoun that disagrees in number with the noun
it replaces, the its/it’s · their/they’re/there spelling set, and a pronoun that could
honestly point at two nouns. Uzbek has no grammatical gender and marks possession on
the noun, so this whole topic is machinery the pupil has never needed before.

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

TOPIC_PRON = {
    "title":   "Olmoshlar va moslashuv (Pronouns & agreement)",
    "summary": "Olmosh qaysi otga ishora qilyapti va shakli unga mos keladimi: son "
               "bo'yicha moslashuv, its/it's oilasi va ikki ma'noli olmosh.",
    "icon":    "bi-people",
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
# Writing 60
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PRON,
    "title": "SAT R&W W60: Pronoun-Antecedent Agreement — Singular Nouns Take Singular Pronouns",
    "summary": "Olmosh o'zi almashtirayotgan otga son bo'yicha mos kelishi shart. "
               "Avval o'sha otni toping — u ko'pincha bo'sh joydan uzoqda turadi.",
    "order": 60,
    "blocks": [
        {"rich_text": (
            "<h2>Olmosh qaysi otni almashtiryapti?</h2>"
            "<p>Olmosh — otning o'rnini bosuvchi so'z. U almashtirgan ot "
            "<strong>antecedent</strong> deyiladi, va qoida bitta:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Olmosh o'zining "
                "antecedent'i bilan son bo'yicha mos kelishi "
                "shart.</strong><br>Birlik ot → <em>it · its</em>. "
                "Ko'plik ot → <em>they · them · their</em>.</p>")
            + "<p>O'zbek tilida bu muammo umuman yo'q: <em>u</em> ham "
            "kishiga, ham narsaga, ham birlikka ishlatiladi. Shuning "
            "uchun bu mavzu bizning quloq uchun "
            "<mark>butunlay yangi mashina</mark> — uni faqat ko'z bilan "
            "tekshirib o'rganish mumkin."
            "</p>"
            + '<span class="sr-time">⏱ ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Olmoshni toping</strong> — "
              "bo'sh joyda <em>its/their/it/them</em> turibdi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Barmog'ingizni antecedent'ga "
              "qo'ying.</strong> «Nima <em>its</em>? Nima "
              "<em>their</em>?» deb so'rang va javob bo'lgan otni "
              "aniq ko'rsating.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Sonini sanang.</strong> "
              "O'sha otning o'zi birlikmi yoki ko'plikmi — yonidagi "
              "boshqa otlar emas.</p></div>"
            + '</div>'
            + WARN.format(
                "Uchta ot doim adashtiradi:<br>"
                "• <em>each · every · either · neither + ot</em> → "
                "<strong>birlik</strong> (<em>each of the museums … "
                "<u>its</u></em>);<br>"
                "• jamoa otlari (<em>the committee · the company · the "
                "team</em>) amerikacha yozuvda → "
                "<strong>birlik</strong>;<br>"
                "• predlogli birikma ichidagi ko'plik ot "
                "(<em>a list <u>of names</u></em>) — u antecedent "
                "<u>emas</u>.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The county's twelve smallest museums have agreed to mount a single "
                "joint exhibition next spring, the first they have ever attempted "
                "together. Each of them will send <span class=\"sr-blank\"></span> "
                "best piece, and the twelve objects will travel as one collection to "
                "four towns before returning home in the autumn.</p>")
            + choices_html([
                "their",
                "its",
                "them",
                "theirs",
            ])
            + "<p><strong>1-qadam:</strong> bo'sh joyda egalik olmoshi "
            "turibdi — <em>___ best piece</em>.</p>"
            "<p><strong>2-qadam:</strong> kimning eng yaxshi asari? "
            "<em>Each</em> ning. Ya'ni antecedent — "
            "<mark><em>Each</em> (of them)</mark>, "
            "<em>museums</em> emas.</p>"
            "<p><strong>3-qadam:</strong> <em>each</em> har doim "
            "<strong>birlik</strong> — «har biri», bittalab.</p>"
            + why([
                (True, "its",
                 "birlik egalik olmoshi — <em>each</em> ga mos. "
                 "«Har bir muzey <u>o'zining</u> eng yaxshi asarini "
                 "yuboradi.»"),
                (False, "their",
                 "<strong>bu darsning bosh tuzog'i:</strong> "
                 "<em>museums</em> yoki <em>them</em> ga moslashgan. "
                 "Ular gapda bor, lekin egalik <em>each</em> "
                 "ga tegishli."),
                (False, "them",
                 "to'ldiruvchi shakli — otdan oldin egalikni "
                 "bildira olmaydi (<em>them best piece</em> "
                 "yo'q)."),
                (False, "theirs",
                 "mustaqil egalik olmoshi: u otsiz turadi "
                 "(<em>the piece is theirs</em>), otdan oldin "
                 "emas."),
            ])
            + NOTE.format(
                "<em>each · every · either · neither · one · another</em> — "
                "beshovi ham birlik, ulardan keyin nechta ot kelishidan "
                "qat'i nazar. <em>Each of the twelve museums</em> hali "
                "ham «bitta muzey, o'n ikki marta».")
        )},

        {
            "rich_text": conv_q(
                "<p>A wind turbine's blades are hollow shells of glass fibre, each one as "
                "long as a tennis court and stiffened inside by a spar that runs almost the "
                "whole length. When a blade cracks near the root, "
                "<span class=\"sr-blank\"></span> has to be lifted down by a crane taller "
                "than the tower itself, and the repair is often done on the grass "
                "below.</p>"),
            "choices": [
                {"text": "it", "is_correct": True},
                {"text": "they", "is_correct": False},
                {"text": "them", "is_correct": False},
                {"text": "those", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima ko'tarib tushiriladi?</strong> "
                "<em>a blade</em> — <mark>birlik</mark>, va u bo'sh "
                "joydan atigi olti so'z narida turibdi.</p>"
                "<p>Kesim ham buni tasdiqlaydi: <em>has to be "
                "lifted</em> — birlik.</p>"
                + why([
                    (True, "it",
                     "birlik olmosh, ega o'rnida — <em>a blade</em> ga "
                     "mos, va <em>has</em> bilan ham mos."),
                    (False, "they",
                     "ko'plik: abzats boshidagi <em>blades</em> ga "
                     "moslashgan. Lekin gap bitta yorilgan parrak "
                     "haqida."),
                    (False, "them",
                     "ko'plik va to'ldiruvchi shakli — ega o'rnida "
                     "tura olmaydi."),
                    (False, "those",
                     "ko'rsatish olmoshi, ko'plik; bu yerda hech "
                     "narsani ko'rsatmayapti."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Neither of the two rivers that meet below the town carries much silt "
                "on its own, and in a dry summer both run almost clear. Where they join, "
                "however, <span class=\"sr-blank\"></span> combined load is enough to "
                "close the navigation channel every few years, and a dredger is kept "
                "moored at the confluence for that reason.</p>"),
            "choices": [
                {"text": "their", "is_correct": True},
                {"text": "its", "is_correct": False},
                {"text": "theirs", "is_correct": False},
                {"text": "them", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kimning yuki?</strong> Qo'shilgan "
                "<u>ikkala</u> daryoning — antecedent "
                "<em>they</em> (<em>the two rivers</em>), "
                "<mark>ko'plik</mark>.</p>"
                "<p>Diqqat: gapning boshida <em>its own</em> to'g'ri "
                "ishlatilgan, chunki u yerda antecedent "
                "<em>Neither</em> — birlik. <strong>Bir gapda ikki xil "
                "antecedent bo'lishi mumkin.</strong></p>"
                + why([
                    (True, "their",
                     "ko'plik egalik olmoshi — <em>they</em> ga mos."),
                    (False, "its",
                     "birlik: yuqoridagi <em>Neither … its own</em> ga "
                     "qarab takrorlangan. Lekin bu yerda antecedent "
                     "<em>they</em>, ya'ni ikkovi birga."),
                    (False, "theirs",
                     "mustaqil egalik olmoshi — otdan oldin "
                     "turmaydi."),
                    (False, "them",
                     "to'ldiruvchi shakli — <em>them combined "
                     "load</em> degan birikma yo'q."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>A leafcutter colony may have fifty separate entrance holes scattered "
                "over half a hectare of forest floor. Workers move between "
                "<span class=\"sr-blank\"></span> along trails that they clear of leaf "
                "litter and keep open for years, and a large trail can be worn two "
                "centimetres deep into the soil.</p>"),
            "choices": [
                {"text": "them", "is_correct": True},
                {"text": "it", "is_correct": False},
                {"text": "its", "is_correct": False},
                {"text": "that", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ishchilar nimalar orasida yuradi?</strong> "
                "<em>fifty separate entrance holes</em> — "
                "<mark>ko'plik</mark>.</p>"
                "<p>Va bo'sh joy <em>between</em> predlogidan keyin "
                "turibdi, demak <u>to'ldiruvchi</u> shakl kerak.</p>"
                + why([
                    (True, "them",
                     "ko'plik va to'ldiruvchi shakli — ikkala talab "
                     "ham bajarildi."),
                    (False, "it",
                     "birlik: gap boshidagi <em>A colony</em> ga "
                     "moslashgan. Lekin ishchilar koloniya orasida "
                     "emas, <u>teshiklar</u> orasida yuradi."),
                    (False, "its",
                     "egalik olmoshi — predlogdan keyin otsiz "
                     "turolmaydi."),
                    (False, "that",
                     "birlik ko'rsatish olmoshi; <em>between "
                     "that</em> ma'nosiz, chunki <em>between</em> "
                     "kamida ikkitani talab qiladi."),
                ])
                + TIP.format(
                    "Barmoqni antecedent'ga qo'yish — bu darsning "
                    "butun mahorati. Uni topsangiz, javob "
                    "<u>sanashdan</u> iborat: bitta narsa "
                    "<em>it/its</em>, bir nechtasi "
                    "<em>they/them/their</em>.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The orchestra now rehearses in a converted chapel, the market hall it "
                "had used for forty years having been sold to a supermarket chain in 2019. "
                "<span class=\"sr-blank\"></span> has since raised half the money needed "
                "to buy the chapel outright, almost all of it from households within a "
                "mile of the building.</p>"),
            "choices": [
                {"text": "It", "is_correct": True},
                {"text": "They", "is_correct": False},
                {"text": "Them", "is_correct": False},
                {"text": "Those", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kim pul yig'di?</strong> "
                "<em>The orchestra</em>.</p>"
                "<p><em>Orchestra</em> — <mark>jamoa oti</mark>: "
                "ma'nosi ko'p kishi, shakli birlik. Amerikacha "
                "yozuvda (SAT ham shunday) jamoa otlari "
                "<strong>birlik</strong> sanaladi.</p>"
                "<p>Kesim buni ochiq aytib turibdi: <em>___ "
                "<u>has</u> raised</em>, <em>have</em> emas.</p>"
                + why([
                    (True, "It",
                     "birlik olmosh — jamoa oti va <em>has</em> "
                     "bilan mos."),
                    (False, "They",
                     "<strong>bu darsning ikkinchi tuzog'i:</strong> "
                     "orkestrni «ko'p kishi» deb o'ylash. Ma'nosi "
                     "shunday, grammatikasi boshqa — va "
                     "<em>has</em> buni rad qiladi."),
                    (False, "Them",
                     "ko'plik va to'ldiruvchi shakli — ega o'rnida "
                     "turmaydi."),
                    (False, "Those",
                     "ko'plik ko'rsatish olmoshi; bu yerda hech "
                     "narsani ko'rsatmaydi."),
                ])
                + NOTE.format(
                    "Britaniya yozuvida <em>the orchestra have</em> "
                    "ham uchraydi. SAT amerikacha me'yorda "
                    "yoziladi — imtihonda jamoa otini "
                    "<u>doim birlik</u> deb oling: <em>the company "
                    "<strong>is</strong> · the team "
                    "<strong>its</strong> · the committee "
                    "<strong>has</strong></em>.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">an antecedent</div><div class="pp-card-back">olmosh almashtirayotgan ot</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a possessive pronoun</div><div class="pp-card-back">egalik olmoshi (its, their)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a collective noun</div><div class="pp-card-back">jamoa oti (committee, team)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a confluence</div><div class="pp-card-back">ikki daryo qo\'shilgan joy</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">silt</div><div class="pp-card-back">loyqa, cho\'kindi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to dredge</div><div class="pp-card-back">tubini qazib tozalamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">leaf litter</div><div class="pp-card-back">to\'kilgan barglar qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hectare</div><div class="pp-card-back">gektar</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Olmoshni ko'rdingizmi — <strong>antecedent'ni "
              "ko'rsating</strong>, keyin sanang.</li>"
              "<li><em>each · every · either · neither</em> → "
              "<strong>birlik</strong>, keyin nechta ot kelishidan "
              "qat'i nazar.</li>"
              "<li>Predlogli birikma ichidagi ot antecedent "
              "<u>emas</u>.</li>"
              "<li>Bir gapda ikki xil antecedent bo'lishi mumkin — "
              "har birini alohida tekshiring.</li>"
              "<li>Shakl ham muhim: <em>its</em> otdan oldin, "
              "<em>theirs</em> otsiz, <em>them</em> predlogdan "
              "keyin.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 61
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PRON,
    "title": "SAT R&W W61: its / it's / their / they're / there — the Five That Cost Marks",
    "summary": "Beshta so'z bir xil eshitiladi va butunlay boshqa narsani "
               "anglatadi. Ularni yechishning bitta ishonchli sinovi bor.",
    "order": 61,
    "blocks": [
        {"rich_text": (
            "<h2>Beshta so'z, bitta sinov</h2>"
            "<p>Bular ingliz tilida <u>eng ko'p</u> xato qilinadigan "
            "beshlik, va SAT ularni har modulda so'raydi. Yaxshi "
            "xabar: qoida qisqa va istisnosiz.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>So'z</th><th>Nima u</th><th>Sinov</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>its</strong></td><td>egalik: uning</td>"
              "<td>otdan oldin turadi — <em>its walls</em></td></tr>"
              "<tr><td><strong>it's</strong></td><td>qisqartma: "
              "<em>it is / it has</em></td>"
              "<td>yoyib ko'ring: <em>it is</em> to'g'ri chiqsa — "
              "shu</td></tr>"
              "<tr><td><strong>their</strong></td><td>egalik: ularning</td>"
              "<td>otdan oldin turadi — <em>their walls</em></td></tr>"
              "<tr><td><strong>they're</strong></td><td>qisqartma: "
              "<em>they are</em></td>"
              "<td>yoyib ko'ring: <em>they are</em></td></tr>"
              "<tr><td><strong>there</strong></td><td>joy yoki "
              "<em>there is/are</em></td>"
              "<td>«u yerda» yoki «bor» ma'nosi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Apostrof "
                "hech qachon egalikni bildirmaydi — olmoshlarda "
                "apostrof faqat <u>qisqartma</u> degani.</strong></p>")
            + '<span class="sr-time">⏱ ~15 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Yoyib ko'rish sinovi</h3>"
            "<p>Bitta harakat, uch soniya: apostrofli variantni "
            "<u>to'liq yozib</u> o'qing.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><em>The kiln and "
              "<strong>it's</strong> walls</em> → "
              "<em>The kiln and <strong>it is</strong> walls</em> — "
              "ma'nosiz. Demak <strong>its</strong>.</p></div>"
            + "<div class=\"pp-step\"><p><em><strong>It's</strong> been "
              "firing since Monday</em> → <em><strong>It has</strong> "
              "been firing</em> — to'g'ri. Demak "
              "<strong>it's</strong>.</p></div>"
            + "<div class=\"pp-step\"><p><em><strong>They're</strong> "
              "visible from the sea</em> → <em><strong>They are</strong> "
              "visible</em> — to'g'ri.</p></div>"
            + "<div class=\"pp-step\"><p><em><strong>There</strong> are "
              "four ways in</em> — «bor» ma'nosi; yoyib bo'lmaydi, "
              "chunki qisqartma emas.</p></div>"
            + '</div>'
            + WARN.format(
                "O'zbek quloq uchun beshovi ham <u>bir xil</u> "
                "eshitiladi, shuning uchun ovoz chiqarib o'qish "
                "yordam bermaydi. Bu mavzu faqat <strong>ko'z "
                "bilan</strong> yechiladi — yoyib yozing.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>A glassblower's furnace runs day and night for months at a time, "
                "because letting it cool would crack the clay pot inside. "
                "<span class=\"sr-blank\"></span> walls are almost a metre thick, and the "
                "door is opened for only a few seconds at a time, long enough for a "
                "gather of glass to be drawn out on the end of a rod.</p>")
            + choices_html([
                "It's",
                "Its",
                "Their",
                "They're",
            ])
            + "<p><strong>Yoyib ko'ring:</strong> <em>It is walls are "
            "almost a metre thick</em> — ma'nosiz. Demak apostrofli "
            "variant tushdi.</p>"
            "<p><strong>Sanang:</strong> devorlar kimning? "
            "<em>the furnace</em> ning — <mark>birlik</mark>.</p>"
            + why([
                (True, "Its",
                 "birlik egalik olmoshi, apostrofsiz. Otdan oldin "
                 "turibdi — aynan shu o'rin."),
                (False, "It's",
                 "<strong>eng ko'p qilinadigan xato:</strong> "
                 "apostrofni egalik deb o'ylash. Bu <em>it is</em> "
                 "yoki <em>it has</em> degani."),
                (False, "Their",
                 "egalik, lekin ko'plik — antecedent "
                 "<em>furnace</em>, birlik."),
                (False, "They're",
                 "<em>they are</em> — ham ko'plik, ham qisqartma; "
                 "ikki jihatdan noto'g'ri."),
            ])
            + NOTE.format(
                "Otlarda apostrof <u>egalikni</u> bildiradi "
                "(<em>the glassblower<strong>'s</strong> furnace</em>), "
                "olmoshlarda esa <u>qisqartmani</u>. Xuddi shu ziddiyat "
                "butun chalkashlikning sababi.")
        )},

        {
            "rich_text": conv_q(
                "<p>The two lighthouses at the mouth of the estuary were built by the "
                "same engineer within a year of each other, one on the sand spit and one "
                "on the rock opposite. <span class=\"sr-blank\"></span> still visible from "
                "each other on a clear night, and pilots waiting for the tide line the "
                "two lights up to check their position in the channel.</p>"),
            "choices": [
                {"text": "They're", "is_correct": True},
                {"text": "Their", "is_correct": False},
                {"text": "There", "is_correct": False},
                {"text": "Theirs", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yoyib ko'ring:</strong> <em>They are still "
                "visible from each other</em> — to'g'ri va aynan "
                "ma'noga mos.</p>"
                "<p>Gapda kesim yo'qligiga ham e'tibor bering: "
                "<em>still visible…</em> o'zi gap emas. Bo'sh joyga "
                "<mark>ega + kesim</mark> kerak, va faqat bitta "
                "variant buni beradi.</p>"
                + why([
                    (True, "They're",
                     "<em>they are</em> — ega va kesimni birdan "
                     "beradi, va ko'plik <em>lighthouses</em> ga "
                     "mos."),
                    (False, "Their",
                     "egalik olmoshi: undan keyin ot kerak "
                     "(<em>their light</em>), sifat emas."),
                    (False, "There",
                     "<em>There visible…</em> — <em>There</em> dan "
                     "keyin <em>is/are</em> kerak edi."),
                    (False, "Theirs",
                     "mustaqil egalik olmoshi — bu yerda kesim ham, "
                     "ma'no ham chiqmaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The cave was surveyed twice in the 1930s and the two plans do not "
                "agree. <span class=\"sr-blank\"></span> are four ways into the system "
                "according to the later survey, but only one of them is wide enough for a "
                "person to pass without crawling, and the earlier plan marks that entrance "
                "in a different field altogether.</p>"),
            "choices": [
                {"text": "There", "is_correct": True},
                {"text": "Their", "is_correct": False},
                {"text": "They're", "is_correct": False},
                {"text": "Theirs", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu <em>there is / there are</em> qurilishi: "
                "<mark>«bor»</mark> degan ma'noni beradi va gapning "
                "haqiqiy egasi fe'ldan <u>keyin</u> turadi "
                "(<em>four ways</em>) — 51-darsdagi teskari tartib.</p>"
                "<p>Yoyish sinovi bu yerda ishlamaydi, chunki "
                "<em>there</em> qisqartma emas: u shunchaki "
                "<u>boshqa so'z</u>.</p>"
                + why([
                    (True, "There",
                     "<em>There are four ways…</em> — «to'rtta yo'l "
                     "bor». Standart qurilish."),
                    (False, "Their",
                     "egalik olmoshi: <em>Their are…</em> degan "
                     "birikma ingliz tilida yo'q."),
                    (False, "They're",
                     "<em>They are four ways</em> — <em>they</em> "
                     "hech narsaga ishora qilmayapti, chunki "
                     "oldingi gapda ko'plik antecedent yo'q."),
                    (False, "Theirs",
                     "mustaqil egalik olmoshi — bu o'ringa umuman "
                     "tushmaydi."),
                ])
                + TIP.format(
                    "Uchtasini bir jumlada eslab qoling: "
                    "<em><strong>They're</strong> over "
                    "<strong>there</strong> with "
                    "<strong>their</strong> dogs.</em> "
                    "Qisqartma · joy · egalik.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The dye is made from a lichen that grows only on north-facing rock, "
                "and <span class=\"sr-blank\"></span> taken three seasons of collecting to "
                "gather enough for a single vat. The colour it gives is a deep "
                "blue-purple that no plant dye can match, which is why the recipe was worth "
                "keeping secret for eight hundred years.</p>"),
            "choices": [
                {"text": "it's", "is_correct": True},
                {"text": "its", "is_correct": False},
                {"text": "their", "is_correct": False},
                {"text": "they're", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yoyib ko'ring:</strong> <em><u>it has</u> "
                "taken three seasons of collecting</em> — to'g'ri. "
                "Demak bu safar javob <mark>apostrofli</mark> "
                "variant.</p>"
                "<p>Diqqat: <em>it's</em> ikki narsaning qisqartmasi — "
                "<em>it is</em> va <em>it has</em>. Bu yerda ikkinchisi, "
                "chunki keyin <em>taken</em> (V3) turibdi.</p>"
                + why([
                    (True, "it's",
                     "<em>it has taken…</em> — present perfect uchun "
                     "kerakli yordamchi fe'lni beradi."),
                    (False, "its",
                     "egalik olmoshi: undan keyin ot kerak, "
                     "<em>taken</em> esa fe'l shakli."),
                    (False, "their",
                     "egalik va ko'plik — ikki jihatdan "
                     "noto'g'ri."),
                    (False, "they're",
                     "<em>they are taken</em> — majhul nisbat "
                     "chiqadi va ma'no buziladi; ustiga ko'plik."),
                ])
                + NOTE.format(
                    "Bu savol darsning teskari tomonini sinaydi. "
                    "Ko'p o'quvchi «apostrof har doim xato» degan "
                    "soddalashtirilgan qoidani yodlab oladi va shu "
                    "yerda tushadi. To'g'ri qoida — "
                    "<strong>yoyib ko'rish</strong>, yodlash "
                    "emas.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Bracket-clock makers of the eighteenth century signed "
                "<span class=\"sr-blank\"></span> work on the back plate, where it would "
                "be seen only by the next person to open the case. A signature there is "
                "worth more to a collector than the dial, because dials were often "
                "replaced and back plates almost never were.</p>"),
            "choices": [
                {"text": "their", "is_correct": True},
                {"text": "they're", "is_correct": False},
                {"text": "there", "is_correct": False},
                {"text": "its", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kimning ishi?</strong> "
                "<em>clockmakers</em> ning — <mark>ko'plik</mark>. "
                "Va bo'sh joydan keyin darrov ot turibdi "
                "(<em>work</em>), demak <u>egalik</u> shakli "
                "kerak.</p>"
                + why([
                    (True, "their",
                     "ko'plik egalik olmoshi, otdan oldin — ikkala "
                     "talab ham bajarildi."),
                    (False, "they're",
                     "<em>they are work</em> — yoyish sinovi darrov "
                     "rad qiladi."),
                    (False, "there",
                     "joy so'zi. Diqqat: keyingi gapda <em>A "
                     "signature <u>there</u></em> — o'sha so'z "
                     "to'g'ri o'rnida ishlatilgan, va aynan shu "
                     "yaqinlik uni jozibali qiladi."),
                    (False, "its",
                     "egalik, lekin birlik — antecedent ko'plik "
                     "<em>clockmakers</em>."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a contraction</div><div class="pp-card-back">qisqartma (it\'s, they\'re)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an apostrophe</div><div class="pp-card-back">apostrof (\')</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a kiln</div><div class="pp-card-back">pech (sopol/gisht kuydiradigan)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an estuary</div><div class="pp-card-back">daryoning dengizga quyilish og\'zi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a sand spit</div><div class="pp-card-back">qumli til (dengizga cho\'zilgan)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a lichen</div><div class="pp-card-back">lishaynik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a vat</div><div class="pp-card-back">katta idish, chan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to fade</div><div class="pp-card-back">rangi o\'chmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Olmoshda apostrof = <strong>qisqartma</strong>, hech "
              "qachon egalik.</li>"
              "<li><em>it's</em> → <em>it is</em> yoki "
              "<em>it has</em>; <em>they're</em> → <em>they "
              "are</em>. Yoyib o'qing.</li>"
              "<li><em>its · their</em> — egalik, ulardan keyin "
              "<u>ot</u> keladi.</li>"
              "<li><em>there</em> — joy yoki «bor»; qisqartma "
              "emas.</li>"
              "<li>Bu mavzu quloq bilan emas, <strong>ko'z bilan</strong> "
              "yechiladi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 62
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PRON,
    "title": "SAT R&W W62: Ambiguous Pronouns — When \"it\" Could Mean Two Things",
    "summary": "Olmosh ikkita otga barobar ishora qilsa, gap noaniq bo'ladi. "
               "SAT buni olmoshni otga almashtirib tuzatadi.",
    "order": 62,
    "blocks": [
        {"rich_text": (
            "<h2>Grammatik to'g'ri, lekin baribir xato</h2>"
            "<p>60-dars son haqida edi. Bu dars boshqa nuqson haqida: "
            "olmosh soni bo'yicha <u>to'g'ri</u> bo'lishi mumkin va "
            "gap baribir buzilgan bo'ladi — chunki u "
            "<mark>ikkita otga barobar</mark> ishora qiladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><em>The council sent the report to "
                "the contractor, but <strong>it</strong> was never "
                "published.</em><br>"
                "<span style=\"color:#7c3aed;\">Nima nashr etilmagan — "
                "hisobotmi, kengashning qarorimi? "
                "<em>report</em> ham, <em>council</em> ham, "
                "<em>contractor</em> ham birlik. Grammatika "
                "jim, ma'no esa ikkiga bo'lingan.</span></p>")
            + "<p>Bu savol imtihonda boshqa savol bo'lib keladi. "
            "Uning shakli — <strong>«Which choice completes the text "
            "with the most logical and precise word or "
            "phrase?»</strong> — va to'g'ri javob deyarli har doim "
            "olmosh emas, <u>otning o'zi</u>.</p>"
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Nomzodlarni "
              "sanang.</strong> Bo'sh joydan oldingi gapda nechta ot "
              "shu o'ringa tushishi mumkin? Ikkitadan ko'p bo'lsa, "
              "olmosh bilan tugaydigan har qanday variant "
              "tushadi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Qolgan otli "
              "variantlardan <u>to'g'ri</u> otni tanlang.</strong> "
              "Ular ataylab boshqa-boshqa narsalarni nomlaydi — "
              "gapning davomi qaysi biri ekanini aytib "
              "beradi.</p></div>"
            + '</div>'
            + WARN.format(
                "<em>it · this · that · they</em> — to'rttasi ham "
                "«noaniq» sifatida variantlar ichida turadi. "
                "<strong>Ular hech qachon javob emas</strong> — "
                "shu savol turida. Boshqa savol turlarida olmosh "
                "javob bo'lishi mumkin, shuning uchun avval "
                "<u>savol matnini</u> o'qing: "
                "<em>most logical and precise</em> so'zlari "
                "bu turning imzosi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + precise_q(
                "<p>In 1953 a federal court held that the company had to publish the "
                "output figures it had kept private for a decade. "
                "<span class=\"sr-blank\"></span> was reversed on appeal four years later, "
                "but by then three newspapers had already printed the tables in full, and "
                "the numbers could not be taken back.</p>")
            + choices_html([
                "It",
                "The ruling",
                "The company",
                "The publication",
            ])
            + "<p><strong>1-qadam — nomzodlar:</strong> birinchi gapda "
            "birlikdagi uchta ot bor: <em>a federal court</em>, "
            "<em>the company</em>, <em>the decade</em>, va yana "
            "butun <em>held that…</em> qarori. "
            "<mark>Bittadan ko'p</mark> — demak olmosh "
            "tushadi.</p>"
            "<p><strong>2-qadam — qaysi ot?</strong> Apellyatsiyada "
            "<u>qaror</u> bekor qilinadi. Kompaniya ham, nashr ham "
            "emas.</p>"
            + why([
                (True, "The ruling",
                 "sudning qarorini aniq nomlaydi, va aynan qaror "
                 "bekor qilinadi. Gapning davomi ham buni "
                 "tasdiqlaydi: gazetalar jadvallarni allaqachon "
                 "chop etib bo'lgan edi."),
                (False, "It",
                 "<strong>bu savol turining bosh tuzog'i:</strong> "
                 "grammatik jihatdan benuqson, ma'no jihatdan "
                 "noaniq — sud, kompaniya yoki qaror."),
                (False, "The company",
                 "kompaniya bekor qilinmaydi. Bu ot gapda bor, "
                 "lekin bu o'ringa tushmaydi."),
                (False, "The publication",
                 "nashr etish sudning buyrug'i edi; bekor qilingan "
                 "narsa buyruqning o'zi, ya'ni qaror."),
            ])
            + NOTE.format(
                "E'tibor bering: noto'g'ri otli variantlar "
                "<u>tasodifiy</u> emas. Ular matnda bor bo'lgan "
                "otlarni oladi va sizni «tanish so'z» hissi bilan "
                "tortadi. Har birini bo'sh joyga qo'yib, "
                "gapni oxirigacha o'qing.")
        )},

        {
            "rich_text": precise_q(
                "<p>The new bridge carries the road across the river and, clamped beneath "
                "the deck, the water main that used to run under the ford. "
                "<span class=\"sr-blank\"></span> burst twice in the first winter, and on "
                "both occasions the carriageway above had to be closed while the joint "
                "was remade.</p>"),
            "choices": [
                {"text": "The main", "is_correct": True},
                {"text": "The bridge", "is_correct": False},
                {"text": "The ford", "is_correct": False},
                {"text": "It", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nomzodlar:</strong> <em>the bridge</em>, "
                "<em>the road</em>, <em>the river</em>, "
                "<em>the water main</em>, <em>the ford</em> — "
                "beshtasi ham birlik.</p>"
                "<p><strong>Qaysi biri yorilishi mumkin?</strong> "
                "Faqat quvur. Va davomi ham buni aytadi: yo'l "
                "<u>tepada</u> yopilgan, ya'ni yorilgan narsa "
                "<mark>pastda</mark> turgan.</p>"
                + why([
                    (True, "The main",
                     "suv quvurini nomlaydi — yoriladigan yagona "
                     "narsa, va u ko'prik ostida, yo'lning tagida "
                     "turibdi."),
                    (False, "It",
                     "beshta birlik otdan qaysi biri ekani "
                     "noma'lum — savol aynan shuni "
                     "taqiqlaydi."),
                    (False, "The bridge",
                     "ko'prik yorilmaydi, va ko'prik yorilganda "
                     "ustidagi yo'lni «yopish» bilan cheklanib "
                     "bo'lmasdi."),
                    (False, "The ford",
                     "kechuv ko'prik qurilgunga qadar ishlatilgan "
                     "eski o'tish joyi; u endi umuman ishlamaydi."),
                ])
            ),
        },

        {
            "rich_text": precise_q(
                "<p>The railway tried the new signalling system on two lines at once, one "
                "running through the tunnels north of the city and one along the open "
                "coast. <span class=\"sr-blank\"></span> was abandoned after four months "
                "because salt spray corroded the trackside relay boxes faster than they "
                "could be replaced, while the other ran for eleven years.</p>"),
            "choices": [
                {"text": "The coastal trial", "is_correct": True},
                {"text": "The tunnel trial", "is_correct": False},
                {"text": "The system", "is_correct": False},
                {"text": "It", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nomzodlar:</strong> ikkita sinov, ustiga "
                "<em>the system</em> va <em>the railway</em>. "
                "Olmosh bu yerda hech narsani hal qilmaydi.</p>"
                "<p><strong>Sabab qaysi birini ko'rsatadi?</strong> "
                "<em>salt spray</em> — <mark>dengiz</mark> "
                "bo'yidagi liniya. Va gapning oxiri "
                "(<em>while the other ran for eleven years</em>) "
                "ikkitadan faqat bittasi to'xtaganini "
                "aytadi.</p>"
                + why([
                    (True, "The coastal trial",
                     "sho'r purkash faqat sohilda bo'ladi, va bu "
                     "«ikkitadan biri» degan ma'noni ham "
                     "beradi."),
                    (False, "The tunnel trial",
                     "tunnelda dengiz sho'ri yo'q — sabab bilan "
                     "to'g'ridan-to'g'ri ziddiyat."),
                    (False, "The system",
                     "juda keng: tizim to'xtatilmagan, uning "
                     "<u>bitta</u> sinovi to'xtatilgan. Oxirgi "
                     "bo'lak buni ochiq aytadi."),
                    (False, "It",
                     "noaniq — ikkala sinov ham, tizim ham, temir "
                     "yo'l ham birlik."),
                ])
            ),
        },

        {
            "rich_text": precise_q(
                "<p>A twelfth-century Latin translation of an Arabic book on calculation "
                "survives in nine copies, and in four of them the translator's own name "
                "stands at the head of the text where the author's should be. "
                "<span class=\"sr-blank\"></span> is why a good deal of the work was "
                "credited to the wrong man for three hundred years.</p>"),
            "choices": [
                {"text": "That misattribution", "is_correct": True},
                {"text": "The translation", "is_correct": False},
                {"text": "The book", "is_correct": False},
                {"text": "This", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima sababchi?</strong> Kitob ham, "
                "tarjima ham emas — <mark>tarjimonning ismi muallif "
                "o'rnida turgani</mark>. Bu bir butun "
                "<u>hodisa</u>, va uni bitta ot bilan nomlash "
                "kerak.</p>"
                + why([
                    (True, "That misattribution",
                     "oldingi gapdagi butun hodisani bitta nom bilan "
                     "atadi: asar noto'g'ri odamga nisbat berilgan. "
                     "Sabab ham, oqibat ham to'g'ri "
                     "bog'landi."),
                    (False, "This",
                     "eng jozibali tuzoq: <em>this</em> «yuqoridagi "
                     "narsa» degani, lekin qaysi narsa — tarjimami, "
                     "ism turgan joymi, kitobmi? Aniq emas."),
                    (False, "The translation",
                     "tarjimaning o'zi xato emas edi; xato — unga "
                     "qo'yilgan ism. Sabab noto'g'ri "
                     "ko'rsatilgan."),
                    (False, "The book",
                     "kitob asrlar bo'yi to'g'ri kitob bo'lib "
                     "qoldi; muallifning nomi almashib "
                     "ketdi."),
                ])
                + TIP.format(
                    "Bu savol turida to'g'ri javob ko'pincha "
                    "<strong>«sifat + ot»</strong> shaklida bo'ladi: "
                    "<em>that misattribution · the coastal trial · "
                    "this delay · the earlier estimate</em>. U "
                    "yolg'iz olmoshga qaraganda uzunroq — va aynan "
                    "shu uzunlik uning aniqligi.")
            ),
        },

        {
            "rich_text": precise_q(
                "<p>Beekeepers in the valley lost most of their hives in the cold spring "
                "of 2018, and the almond growers who rent hives from them had to bring "
                "colonies in by lorry from three hundred miles away. "
                "<span class=\"sr-blank\"></span> cost about four dollars a mile and "
                "added roughly a fifth to the price of that year's crop.</p>"),
            "choices": [
                {"text": "Those lorry journeys", "is_correct": True},
                {"text": "The cold spring", "is_correct": False},
                {"text": "The growers", "is_correct": False},
                {"text": "They", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima bir milga to'rt dollar turadi?</strong> "
                "Faqat yuk mashinasi yo'li. Narx <mark>masofaga "
                "qarab</mark> hisoblangan — bu bitta narsani "
                "ko'rsatadi.</p>"
                + why([
                    (True, "Those lorry journeys",
                     "uch yuz millik tashishni nomlaydi, va «bir "
                     "milga to'rt dollar» aynan shunga tegishli."),
                    (False, "They",
                     "noaniq: asalarichilarmi, bog'bonlarmi, "
                     "uyalarmi, oilalarmi? To'rttasi ham ko'plik va "
                     "to'rttasi ham yaqin turibdi."),
                    (False, "The cold spring",
                     "sovuq bahor — sababning boshlanishi, lekin u "
                     "«bir milga to'rt dollar» turmaydi."),
                    (False, "The growers",
                     "bog'bonlar to'ladi, o'zlari narx emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">ambiguous</div><div class="pp-card-back">ikki ma\'noli, noaniq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ruling</div><div class="pp-card-back">sud qarori</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to reverse on appeal</div><div class="pp-card-back">apellyatsiyada bekor qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a water main</div><div class="pp-card-back">asosiy suv quvuri</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ford</div><div class="pp-card-back">kechuv (daryodan o\'tish joyi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to corrode</div><div class="pp-card-back">yemirmoq, zanglatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a misattribution</div><div class="pp-card-back">asarni noto\'g\'ri odamga nisbat berish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to credit ~ to …</div><div class="pp-card-back">~ ni … ning hisobiga yozmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Savol matnida <em>most logical and precise</em> "
              "bo'lsa — bu <strong>shu</strong> savol turi.</li>"
              "<li>Bo'sh joydan oldingi gapda mos keladigan ot "
              "<strong>ikkitadan ko'p</strong> bo'lsa, olmoshli "
              "variant tushadi.</li>"
              "<li><em>it · this · that · they</em> bu turda javob "
              "bo'lmaydi.</li>"
              "<li>Qolgan otlardan gapning davomiga mos keladiganini "
              "tanlang — sabab, oqibat va zamon aytib "
              "beradi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 63
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PRON,
    "title": "SAT R&W W63: who / whom / which / that in Relative Clauses",
    "summary": "Nisbiy olmosh ikki savolga javob beradi: ishora qilayotgani "
               "odammi yoki narsami, va u ergash gapda ega yoki to'ldiruvchimi.",
    "order": 63,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki savol, to'rt so'z</h2>"
            "<p>Nisbiy olmosh — ergash gapni otga ulab turadigan so'z. "
            "Qaysi birini tanlash faqat ikki savolga bog'liq:</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th></th><th>Odam</th><th>Narsa</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Ergash gapda EGA</strong></td>"
              "<td><em>who</em></td><td><em>which / that</em></td></tr>"
              "<tr><td><strong>Ergash gapda TO'LDIRUVCHI</strong></td>"
              "<td><em>whom</em></td><td><em>which / that</em></td></tr>"
              "<tr><td><strong>EGALIK</strong></td>"
              "<td><em>whose</em></td><td><em>whose</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + NOTE.format(
                "<em>whose</em> narsalar uchun ham ishlaydi — "
                "<em>the observatory <u>whose</u> dome…</em> "
                "to'g'ri va tabiiy. Ingliz tilida <em>of "
                "which</em> dan boshqa varianti yo'q, va u "
                "og'ir eshitiladi.")
            + '<span class="sr-time">⏱ ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>who yoki whom — almashtirish sinovi</h3>"
            "<p>Ergash gapni alohida gap qilib o'qing va nisbiy "
            "olmosh o'rniga <em>he/she</em> yoki <em>him/her</em> "
            "qo'ying.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><em>The clerk <strong>who</strong> "
              "copied the register…</em> → <em><strong>He</strong> "
              "copied the register</em> ✓ — <strong>who</strong> "
              "(ega).</p></div>"
            + "<div class=\"pp-step\"><p><em>The engineer "
              "<strong>whom</strong> the company sent…</em> → "
              "<em>The company sent <strong>him</strong></em> ✓ — "
              "<strong>whom</strong> (to'ldiruvchi).</p></div>"
            + "<div class=\"pp-step\"><p><strong>Predlogdan keyin har "
              "doim <em>whom</em>:</strong> <em>to whom · for whom · "
              "with whom</em>. Istisnosiz.</p></div>"
            + '</div>'
            + WARN.format(
                "<strong>Vergul qoidasi:</strong> vergul bilan "
                "ajratilgan qo'shimcha ergash gapda "
                "<em>that</em> <u>ishlatilmaydi</u> — faqat "
                "<em>which</em> (narsa) yoki <em>who/whom</em> "
                "(odam). Bu 42-darsdagi qo'shimcha bo'lak "
                "qoidasining aynan davomi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The engineer <span class=\"sr-blank\"></span> the water board sent to "
                "inspect the dam in 1928 spent a fortnight walking the crest with a spirit "
                "level and reported that the eastern end had settled by four inches. His "
                "report was filed without comment and found again only after the "
                "flood.</p>")
            + choices_html([
                "who",
                "whom",
                "which",
                "whose",
            ])
            + "<p><strong>1-savol — odammi?</strong> Ha, "
            "<em>The engineer</em>. Demak <em>which</em> "
            "tushdi.</p>"
            "<p><strong>2-savol — ega yoki to'ldiruvchi?</strong> "
            "Ergash gapni yozib ko'ring: <em>the water board sent "
            "___ to inspect the dam</em>. Ega — "
            "<em>the water board</em>; muhandis "
            "<mark>yuborilgan</mark>, ya'ni to'ldiruvchi.</p>"
            "<p>Almashtirish sinovi: <em>The board sent "
            "<strong>him</strong></em> ✓ — <em>him</em> chiqsa, "
            "javob <em>whom</em>.</p>"
            + why([
                (True, "whom",
                 "odam va to'ldiruvchi — jadvalning aynan shu "
                 "katagi. <em>him</em> sinovi tasdiqlaydi."),
                (False, "who",
                 "odam, lekin ega shakli: <em>He the water board "
                 "sent…</em> — chiqmaydi."),
                (False, "which",
                 "narsalar uchun. Odam haqida yozganda SAT buni "
                 "har doim xato deb belgilaydi."),
                (False, "whose",
                 "egalik: undan keyin ot kerak bo'lardi "
                 "(<em>whose report…</em>), bu yerda esa darrov "
                 "ega keladi."),
            ])
            + TIP.format(
                "<em>whom</em> imtihonda kam uchraydi, lekin uchraganda "
                "deyarli har doim <u>predlogdan keyin</u> yoki "
                "<u>ega allaqachon bor</u> ergash gapda keladi. "
                "Ergash gapning o'z egasini toping — bor bo'lsa, "
                "javob <em>whom</em>.")
        )},

        {
            "rich_text": conv_q(
                "<p>The sea wall, <span class=\"sr-blank\"></span> was finished in 1931 and "
                "raised twice afterwards, has never been inspected from the inside. The "
                "single inspection gallery running through the base was sealed during the "
                "second raising, and no drawing of it survives in the board's own "
                "files.</p>"),
            "choices": [
                {"text": "which", "is_correct": True},
                {"text": "that", "is_correct": False},
                {"text": "who", "is_correct": False},
                {"text": "whose", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Odammi yoki narsami?</strong> "
                "<em>The sea wall</em> — narsa.</p>"
                "<p><strong>Vergul bormi?</strong> Ha — ergash gap "
                "ikki tomondan vergul bilan ajratilgan, ya'ni u "
                "<mark>qo'shimcha ma'lumot</mark> (42-dars). Bunday "
                "gapda <em>that</em> ishlatilmaydi.</p>"
                + why([
                    (True, "which",
                     "narsa + vergulli qo'shimcha bo'lak — bu "
                     "birikmaning yagona to'g'ri varianti."),
                    (False, "that",
                     "<strong>bu darsning bosh tuzog'i:</strong> "
                     "<em>that</em> hech qachon verguldan keyin "
                     "kelmaydi. U faqat vergulsiz, ma'noni "
                     "cheklovchi ergash gaplarda ishlaydi."),
                    (False, "who",
                     "odamlar uchun; devor odam emas."),
                    (False, "whose",
                     "egalik — undan keyin ot kerak, bu yerda esa "
                     "<em>was finished</em> kesimi keladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The observatory, <span class=\"sr-blank\"></span> dome has not been "
                "opened since 1974, still holds the original silvered mirror in its "
                "mounting. A local society raises money for the roof each summer, and the "
                "mirror is uncovered once a year so that visitors can see their own faces "
                "in it.</p>"),
            "choices": [
                {"text": "whose", "is_correct": True},
                {"text": "which", "is_correct": False},
                {"text": "that", "is_correct": False},
                {"text": "who's", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin darrov <mark>ot</mark> turibdi "
                "(<em>dome</em>). Nisbiy olmosh otdan oldin "
                "turganda, u <u>egalik</u> shaklida bo'lishi "
                "shart.</p>"
                "<p>Ma'no: <em>the dome <u>of the "
                "observatory</u></em> — rasadxonaning gumbazi.</p>"
                + why([
                    (True, "whose",
                     "yagona egalik shakli, va u narsalarga ham "
                     "ishlaydi. <em>The observatory's dome</em> "
                     "degan ma'noni beradi."),
                    (False, "which",
                     "<em>which dome</em> — savol so'zi bo'lib "
                     "eshitiladi, egalikni bildirmaydi."),
                    (False, "that",
                     "verguldan keyin kelmaydi, va egalik ham "
                     "bildirmaydi — ikki jihatdan noto'g'ri."),
                    (False, "who's",
                     "<em>who is</em> yoki <em>who has</em> ning "
                     "qisqartmasi (61-dars) — otdan oldin "
                     "turolmaydi, ustiga rasadxona odam emas."),
                ])
                + NOTE.format(
                    "<em>whose</em> va <em>who's</em> — 61-darsdagi "
                    "<em>its / it's</em> juftining aynan o'zi. "
                    "Apostrof qisqartma degani, egalik emas.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The clerk <span class=\"sr-blank\"></span> copied the parish register "
                "in 1841 wrote a clear round hand and expanded every abbreviation he "
                "found. It is his copy, not the original, that genealogists now work from, "
                "because the original was stored in a damp vestry for sixty years and is "
                "illegible in places.</p>"),
            "choices": [
                {"text": "who", "is_correct": True},
                {"text": "whom", "is_correct": False},
                {"text": "which", "is_correct": False},
                {"text": "whose", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Odammi?</strong> Ha — <em>The "
                "clerk</em>.</p>"
                "<p><strong>Ega yoki to'ldiruvchi?</strong> Ergash "
                "gapda boshqa ega <u>yo'q</u>: <em>___ copied the "
                "register</em>. Nusxa ko'chirgan — o'sha kotibning "
                "o'zi, ya'ni <mark>ega</mark>.</p>"
                "<p>Almashtirish sinovi: <em><strong>He</strong> "
                "copied the register</em> ✓.</p>"
                + why([
                    (True, "who",
                     "odam + ega — <em>he</em> sinovi tasdiqlaydi."),
                    (False, "whom",
                     "to'ldiruvchi shakli. <em>Him copied the "
                     "register</em> chiqmaydi. <em>whom</em> ni "
                     "«rasmiyroq who» deb o'ylash — eng keng "
                     "tarqalgan xato."),
                    (False, "which",
                     "narsalar uchun."),
                    (False, "whose",
                     "egalik: undan keyin ot kerak, bu yerda esa "
                     "kesim keladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The mill leat is a channel a mile long, cut by hand along the "
                "hillside, through <span class=\"sr-blank\"></span> the whole of the river ran "
                "for six months of the year. The farmers downstream "
                "complained for two centuries, and the case was settled only when the "
                "wheel was taken out.</p>"),
            "choices": [
                {"text": "which", "is_correct": True},
                {"text": "that", "is_correct": False},
                {"text": "whom", "is_correct": False},
                {"text": "what", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joy <mark>predlogdan keyin</mark> turibdi: "
                "<em>through ___</em>. Bu o'rinda tanlov keskin "
                "torayadi.</p>"
                "<p><strong>Nima orqali?</strong> <em>a channel</em> "
                "— narsa.</p>"
                + why([
                    (True, "which",
                     "narsalar uchun yagona shakl, va predlogdan "
                     "keyin tura oladi: <em>through which · in "
                     "which · from which</em>."),
                    (False, "that",
                     "<em>that</em> hech qachon predlogdan keyin "
                     "kelmaydi — <em>through that the river "
                     "ran</em> ingliz tilida yo'q."),
                    (False, "whom",
                     "predlogdan keyin to'g'ri shakl, lekin faqat "
                     "<u>odamlar</u> uchun; kanal odam emas."),
                    (False, "what",
                     "<em>what</em> otga ulanmaydi — u o'zi «narsa» "
                     "degan ma'noni olib yuradi "
                     "(<em>what he saw</em>)."),
                ])
                + TIP.format(
                    "Predlog + nisbiy olmosh juftini shunday eslang: "
                    "<strong>narsa → <em>which</em>, odam → "
                    "<em>whom</em></strong>, va boshqa hech "
                    "nima. <em>that</em> ham, <em>who</em> ham "
                    "predlogdan keyin turolmaydi.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a relative clause</div><div class="pp-card-back">nisbiy ergash gap</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">non-essential (with commas)</div><div class="pp-card-back">qo\'shimcha, vergul bilan ajratilgan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a spirit level</div><div class="pp-card-back">suvpuflagich, nivelir</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to settle (foundation)</div><div class="pp-card-back">cho\'kmoq (poydevor haqida)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a parish register</div><div class="pp-card-back">cherkov qayd daftari</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a genealogist</div><div class="pp-card-back">nasabnoma tadqiqotchisi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">illegible</div><div class="pp-card-back">o\'qib bo\'lmaydigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a mounting</div><div class="pp-card-back">o\'rnatma, ramka</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Odam → <em>who / whom</em>. Narsa → "
              "<em>which / that</em>. Egalik → <em>whose</em> "
              "(ikkovi uchun ham).</li>"
              "<li><em>who</em> yoki <em>whom</em>: ergash gapning "
              "<strong>o'z egasi</strong> bormi? Bor bo'lsa — "
              "<em>whom</em>.</li>"
              "<li>Predlogdan keyin har doim <em>whom</em>.</li>"
              "<li><strong>Verguldan keyin <em>that</em> "
              "kelmaydi</strong> — faqat <em>which</em> yoki "
              "<em>who</em>.</li>"
              "<li><em>who's</em> = <em>who is/has</em>, egalik "
              "emas.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 64
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PRON,
    "title": "SAT R&W W64: Pronouns and Agreement — Mixed Practice",
    "summary": "Olti savol aralash: son, apostrof, noaniqlik va nisbiy olmosh. "
               "Savol turi aytilmaydi — variantlar aytadi.",
    "order": 64,
    "blocks": [
        {"rich_text": (
            "<h2>Aralash mashq</h2>"
            "<p>Bu mavzuning to'rt darsi to'rt xil nuqsonni "
            "o'rgatdi. Imtihonda ular aralash keladi va savol "
            "o'z turini aytmaydi — <strong>variantlar "
            "aytadi</strong>.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Variantlar shunday farq qilsa</th>"
              "<th>Savol shu haqda</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>its · their · them · theirs</em></td>"
              "<td>son va shakl</td><td>60</td></tr>"
              "<tr><td><em>its · it's</em> · "
              "<em>their · they're · there</em></td>"
              "<td>apostrof — yoyib ko'ring</td><td>61</td></tr>"
              "<tr><td>olmosh va <em>ot</em> birikmalari aralash, "
              "savolda <em>precise</em></td>"
              "<td>noaniq olmosh</td><td>62</td></tr>"
              "<tr><td><em>who · whom · which · whose · that</em></td>"
              "<td>nisbiy olmosh</td><td>63</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + '<span class="sr-time">⏱ 6 savol · ~5 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Son") + conv_q(
                "<p>Each of the four boatyards still working on the river builds to "
                "<span class=\"sr-blank\"></span> own set of moulds, so a hull laid down "
                "in one yard cannot be finished in another. The moulds are cut from "
                "plywood and kept in a loft above the shed, and none has ever been "
                "measured or drawn.</p>"),
            "choices": [
                {"text": "its", "is_correct": True},
                {"text": "their", "is_correct": False},
                {"text": "theirs", "is_correct": False},
                {"text": "them", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kimning qoliplari?</strong> "
                "<em>Each</em> ning — va <em>each</em> har doim "
                "<mark>birlik</mark> (60-dars), keyin nechta ot "
                "kelishidan qat'i nazar.</p>"
                + why([
                    (True, "its",
                     "birlik egalik olmoshi, otdan oldin."),
                    (False, "their",
                     "<em>boatyards</em> ga moslashgan. Lekin "
                     "egalik <em>Each</em> ga tegishli."),
                    (False, "theirs",
                     "mustaqil egalik olmoshi — otdan oldin "
                     "turmaydi."),
                    (False, "them",
                     "to'ldiruvchi shakli — egalikni "
                     "bildirmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Apostrof") + conv_q(
                "<p>A cast-iron cooking range weighs a third of a tonne, and "
                "<span class=\"sr-blank\"></span> the weight rather than the heat that "
                "eventually cracks the floor beneath it. Most surviving ranges have been "
                "moved at least once, and the crack usually shows in the room below "
                "before anyone notices it upstairs.</p>"),
            "choices": [
                {"text": "it's", "is_correct": True},
                {"text": "its", "is_correct": False},
                {"text": "there", "is_correct": False},
                {"text": "theirs", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Yoyib ko'ring:</strong> <em><u>it is</u> "
                "the weight rather than the heat that cracks the "
                "floor</em> — to'g'ri, va bu tanish "
                "<em>it is … that …</em> qurilishi.</p>"
                + why([
                    (True, "it's",
                     "<em>it is</em> ning qisqartmasi — gapga kerak "
                     "bo'lgan kesimni beradi."),
                    (False, "its",
                     "egalik: undan keyin ot kerak edi, lekin "
                     "gapda kesim yo'q qolardi."),
                    (False, "there",
                     "<em>there the weight … that cracks</em> — "
                     "kesim yo'q, ma'no yo'q."),
                    (False, "theirs",
                     "mustaqil egalik olmoshi va ko'plik; ikki "
                     "jihatdan noto'g'ri."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Nisbiy olmosh") + conv_q(
                "<p>The chapel, <span class=\"sr-blank\"></span> roof was rebuilt in oak "
                "after the fire of 1908, is the only building on the street to have kept "
                "its original floor. The stone flags were laid over sand and have moved "
                "very little in three hundred years.</p>"),
            "choices": [
                {"text": "whose", "is_correct": True},
                {"text": "which", "is_correct": False},
                {"text": "that", "is_correct": False},
                {"text": "who's", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin darrov ot turibdi "
                "(<em>roof</em>) — demak <mark>egalik</mark> shakli "
                "kerak (63-dars). Va <em>whose</em> narsalar uchun "
                "ham ishlaydi.</p>"
                + why([
                    (True, "whose",
                     "yagona egalik shakli: «cherkovning tomi»."),
                    (False, "which",
                     "<em>which roof</em> savol so'zi bo'lib "
                     "eshitiladi; egalikni bildirmaydi."),
                    (False, "that",
                     "verguldan keyin umuman kelmaydi, va egalik "
                     "ham emas."),
                    (False, "who's",
                     "<em>who is</em> ning qisqartmasi — cherkov "
                     "odam emas, va otdan oldin "
                     "turolmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Aniqlik") + precise_q(
                "<p>The town replaced its gas lamps with electric ones in 1912 and sold "
                "the old lamp posts for scrap, keeping four as a curiosity in the yard "
                "behind the town hall. <span class=\"sr-blank\"></span> are the only ones "
                "left of about six hundred, and two of them now stand outside the "
                "museum.</p>"),
            "choices": [
                {"text": "Those four posts", "is_correct": True},
                {"text": "The electric ones", "is_correct": False},
                {"text": "The gas lamps", "is_correct": False},
                {"text": "They", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima olti yuztadan qolgan to'rtta?</strong> "
                "Saqlab qolingan <mark>eski ustunlar</mark>.</p>"
                "<p>Oldingi gapda ko'plikdagi to'rtta nomzod bor: "
                "<em>gas lamps · electric ones · lamp posts · "
                "four</em> — olmosh ularning birortasini ham "
                "ajratmaydi.</p>"
                + why([
                    (True, "Those four posts",
                     "aynan saqlab qolingan to'rttani nomlaydi, va "
                     "«olti yuztadan to'rttasi» hisobiga mos "
                     "keladi."),
                    (False, "They",
                     "to'rtta ko'plik ot orasida noaniq — bu savol "
                     "turining bosh tuzog'i."),
                    (False, "The electric ones",
                     "yangi chiroqlar 1912-yilda o'rnatilgan; ular "
                     "«qolgan» emas, ular almashtirgan."),
                    (False, "The gas lamps",
                     "chiroqlarning o'zi emas, <u>ustunlar</u> "
                     "saqlangan — matn ikkisini ataylab "
                     "ajratadi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Son") + conv_q(
                "<p>The company of surveyors kept a single set of standard measuring chains "
                "in a locked case and lent <span class=\"sr-blank\"></span> only to members "
                "who had finished an apprenticeship. Two chains went missing in the 1840s "
                "and were replaced by copies that were never checked against the "
                "originals.</p>"),
            "choices": [
                {"text": "them", "is_correct": True},
                {"text": "it", "is_correct": False},
                {"text": "its", "is_correct": False},
                {"text": "they", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Nima qarzga berilgan?</strong> "
                "<em>measuring chains</em> — <mark>ko'plik</mark>. "
                "Keyingi gap ham buni tasdiqlaydi: "
                "<em>Two chains went missing</em>.</p>"
                "<p>Va bo'sh joy <em>lent</em> fe'lidan keyin "
                "turibdi, ya'ni <u>to'ldiruvchi</u> shakl "
                "kerak.</p>"
                + why([
                    (True, "them",
                     "ko'plik va to'ldiruvchi shakli — ikkala talab "
                     "ham bajarildi."),
                    (False, "it",
                     "birlik: <em>a single set</em> ga moslashgan. "
                     "Lekin qarzga berilgan narsa to'plam emas, "
                     "zanjirlarning o'zi — ikkitasi alohida "
                     "yo'qolgani buni ko'rsatadi."),
                    (False, "its",
                     "egalik olmoshi — fe'ldan keyin otsiz "
                     "turolmaydi."),
                    (False, "they",
                     "ega shakli: <em>lent they</em> "
                     "chiqmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Nisbiy olmosh") + conv_q(
                "<p>The apprentice <span class=\"sr-blank\"></span> the guild fined for "
                "casting a bell out of tune in 1783 went on to run the largest foundry in "
                "the county. His own bells were tested three times before they left the "
                "yard, and none was ever returned.</p>"),
            "choices": [
                {"text": "whom", "is_correct": True},
                {"text": "who", "is_correct": False},
                {"text": "which", "is_correct": False},
                {"text": "whose", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Odammi?</strong> Ha — <em>The "
                "apprentice</em>.</p>"
                "<p><strong>Ergash gapning o'z egasi bormi?</strong> "
                "Ha: <em>the guild fined ___</em>. Jarima solgan — "
                "gildiya; shogird esa <mark>to'ldiruvchi</mark>.</p>"
                "<p>Almashtirish sinovi: <em>the guild fined "
                "<strong>him</strong></em> ✓.</p>"
                + why([
                    (True, "whom",
                     "odam + to'ldiruvchi. <em>him</em> sinovi "
                     "tasdiqlaydi."),
                    (False, "who",
                     "ega shakli — lekin ergash gapda ega "
                     "allaqachon bor (<em>the guild</em>)."),
                    (False, "which",
                     "narsalar uchun."),
                    (False, "whose",
                     "egalik: undan keyin ot kerak edi, bu yerda "
                     "esa ega keladi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Mavzu yakuni — Olmoshlar va moslashuv</h3>"
            + TIP.format(
                "Bitta savol bilan boshlang: <strong>«Bu olmosh "
                "qaysi otni almashtiryapti?»</strong> Barmog'ingizni "
                "o'sha otga qo'ying. Topolmasangiz — bu 62-dars "
                "savoli va javob otning o'zi. Topsangiz — sanang "
                "(60-dars), keyin shaklini tekshiring: apostrof "
                "(61-dars) yoki nisbiy olmoshning o'rni "
                "(63-dars).")
            + "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a boatyard</div><div class="pp-card-back">qayiq ustaxonasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a mould</div><div class="pp-card-back">qolip</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a hull</div><div class="pp-card-back">kema tanasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cooking range</div><div class="pp-card-back">cho\'yan oshxona pechi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a stone flag</div><div class="pp-card-back">yassi tosh plita (pol uchun)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">scrap</div><div class="pp-card-back">metallolom</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a measuring chain</div><div class="pp-card-back">o\'lchov zanjiri</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a foundry</div><div class="pp-card-back">quyish zavodi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><em>its · their · them</em> farqi → "
              "<strong>son va shakl</strong>.</li>"
              "<li>Apostrof ko'rsangiz → <strong>yoyib "
              "o'qing</strong>.</li>"
              "<li>Savolda <em>precise</em> so'zi bo'lsa → "
              "<strong>otni tanlang, olmoshni emas</strong>.</li>"
              "<li><em>who/whom</em> → ergash gapda ega bormi. "
              "Verguldan keyin <em>that</em> yo'q.</li>"
              "</ul>"
        )},
    ],
},
]
