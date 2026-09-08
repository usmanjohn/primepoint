# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 20-25.

"Qaydlardan jumla qurish (Rhetorical Synthesis)" — the second half of the
Expression of Ideas domain. A student's research notes are given, then a GOAL,
and the four choices are all accurate: only one serves the goal.

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

TOPIC_SYNTH = {
    "title":   "Qaydlardan jumla qurish (Rhetorical Synthesis)",
    "summary": "O'quvchining qaydlari va aniq maqsad beriladi: to'rtala variant ham "
               "rost, lekin faqat bittasi maqsadni bajaradi.",
    "icon":    "bi-journal-check",
    "order":   3,
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
# Writing 20
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W20: Rhetorical Synthesis — The Notes, the Goal, and Why the Goal Decides Everything",
    "summary": "To'rtala variant ham qaydlarga to'g'ri keladi. Yagona mezon — "
               "maqsad jumlasi, va uni birinchi o'qish kerak.",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Hammasi rost — bittasi mos</h2>"
            "<p><strong>Rhetorical Synthesis</strong> — <em>Expression of "
            "Ideas</em> domenining ikkinchi turi va butun imtihondagi eng "
            "o'ziga xos savoli. U shunday ko'rinadi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><em>While researching a topic, a "
                "student has taken the following notes:</em></p>"
                "<p style=\"margin:0 0 6px;\">— to'rt-olti dona qayd, "
                "belgilangan ro'yxatda —</p>"
                "<p style=\"margin:0;\"><em>The student wants to "
                "<u>[MAQSAD]</u>. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?</em></p>")
            + "<p>Va mana asosiy fakt: <mark>to'rtala variant ham "
            "qaydlardagi rost ma'lumotni ishlatadi</mark>. Ularning hech "
            "birida xato yo'q. Shuning uchun «qaysi biri to'g'ri?» degan "
            "savol bu yerda ma'nosiz.</p>"
            "<p>Yagona savol: <strong>qaysi biri maqsadni bajaradi?</strong></p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Usul — uch qadam</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Maqsad jumlasini birinchi "
              "o'qing</strong> — qaydlardan ham oldin. U ekranda pastda "
              "turadi, lekin u savolning kaliti. Qaydlarni maqsadsiz o'qish "
              "— xaritasiz yurish.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Maqsad qanday jumlani "
              "talab qilishini ayting.</strong> «Tanish bo'lmagan "
              "o'quvchiga tanishtirish» → ta'rif kerak. «Ikki narsani "
              "solishtirish» → ikkovi ham va farq/o'xshashlik "
              "kerak.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Endi qaydlarni "
              "o'qing</strong> — va aynan o'sha ma'lumotni qidiring. "
              "Ko'p qayd keraksiz bo'lib chiqadi, va bu normal: ular "
              "chalg'itish uchun turibdi.</p></div>"
            + '</div>'
            + WARN.format(
                "<strong>Eng ko'p uchraydigan xato:</strong> qaydlarni "
                "diqqat bilan o'qib, keyin «eng qiziqarli» faktni "
                "o'z ichiga olgan variantni tanlash. Qiziqarlilik mezon "
                "emas. Ba'zan to'g'ri javob eng zerikarli variant "
                "bo'ladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Kintsugi is a Japanese method of repairing broken ceramics.",
                 "The broken pieces are rejoined with lacquer that has been mixed with "
                 "powdered gold.",
                 "The repair is left visible rather than disguised.",
                 "Some repaired bowls are valued more highly than they were before they "
                 "broke."],
                "The student wants to introduce kintsugi to an audience unfamiliar "
                "with it. Which choice most effectively uses relevant information from "
                "the notes to accomplish this goal?")
            + choices_html([
                "Some bowls repaired by kintsugi are valued more highly than they were "
                "before they broke.",
                "Kintsugi is a Japanese method of repairing broken ceramics in which the "
                "pieces are rejoined with gold-flecked lacquer.",
                "In kintsugi, the repair is left visible rather than disguised.",
                "Powdered gold is mixed into the lacquer that kintsugi uses.",
            ])
            + "<p><strong>1-qadam — maqsad:</strong> "
            "<em>introduce kintsugi to an audience <u>unfamiliar with "
            "it</u></em>.</p>"
            "<p><strong>2-qadam — bu qanday jumlani talab qiladi?</strong> "
            "Tanish bo'lmagan o'quvchi <u>nima ekanini bilmaydi</u>. Demak "
            "jumla <mark>ta'rif berishi</mark> kerak: bu nima, qayerdan, "
            "nima qiladi.</p>"
            + why([
                (True, "Kintsugi is a Japanese method of repairing broken ceramics in which the pieces are rejoined with gold-flecked lacquer",
                 "yagona variant <u>ta'rif</u> beradi: nima ekani, qayerdan "
                 "va qanday ishlashi. Notanish o'quvchi shu jumladan keyin "
                 "kintsugi nimaligini biladi."),
                (False, "In kintsugi, the repair is left visible rather than disguised",
                 "rost va qiziqarli — lekin u <u>kintsugi nimaligini "
                 "biladigan</u> o'quvchi uchun. Notanish odam «ta'mir "
                 "ko'rinib turadi» degandan nima ekanini "
                 "tushunmaydi."),
                (False, "Some bowls repaired by kintsugi are valued more highly than they were before they broke",
                 "eng jozibali fakt — va aynan shuning uchun tuzoq. U "
                 "kintsugining <u>oqibati</u>, ta'rifi emas."),
                (False, "Powdered gold is mixed into the lacquer that kintsugi uses",
                 "bitta texnik tafsilot. Uni bilgan odam ham kintsugi nima "
                 "ekanini bilmaydi."),
            ])
            + NOTE.format(
                "Uchala noto'g'ri variant ham qaydlardan <strong>so'zma-so'z "
                "olingan</strong> va hech qanday xato qilmagan. Bu turning "
                "butun mohiyati: rostlik yetarli emas.")
        )},

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["The Aral Sea was once the fourth-largest lake in the world.",
                 "From the 1960s the rivers feeding it were diverted to irrigate cotton.",
                 "By 2010 the southern basin had largely dried out.",
                 "A dam completed in 2005 separated the northern basin from the southern "
                 "one.",
                 "The northern basin has since partly refilled and fish have returned to "
                 "it."],
                "The student wants to emphasise a positive development. Which choice "
                "most effectively uses relevant information from the notes to accomplish "
                "this goal?"),
            "choices": [
                {"text": "Since a dam separated it from the southern basin in 2005, the northern basin has partly refilled and fish have returned.", "is_correct": True},
                {"text": "The Aral Sea, once the fourth-largest lake in the world, had largely dried out in its southern basin by 2010.", "is_correct": False},
                {"text": "From the 1960s onward, the rivers feeding the Aral Sea were diverted in order to irrigate cotton.", "is_correct": False},
                {"text": "A dam completed in 2005 separated the northern basin of the Aral Sea from the southern one.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>emphasise a <u>positive</u> "
                "development</em>. Demak jumla yaxshi xabarni "
                "<mark>oldinga chiqarishi</mark> kerak.</p>"
                + why([
                    (True, "Since a dam separated it from the southern basin in 2005, the northern basin has partly refilled and fish have returned",
                     "yagona ijobiy natijani beradi — to'lish va baliqlarning "
                     "qaytishi — va sababni ham qo'shadi."),
                    (False, "A dam completed in 2005 separated the northern basin of the Aral Sea from the southern one",
                     "rost, lekin <u>neytral</u>: to'g'on qurilgani o'z-o'zicha "
                     "ijobiy rivojlanish emas. Natijasiz u shunchaki "
                     "voqea."),
                    (False, "The Aral Sea, once the fourth-largest lake in the world, had largely dried out in its southern basin by 2010",
                     "<strong>to'g'ridan-to'g'ri teskari:</strong> bu salbiy "
                     "xabar."),
                    (False, "From the 1960s onward, the rivers feeding the Aral Sea were diverted in order to irrigate cotton",
                     "yana salbiy tomon — muammoning sababi."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Sourdough bread rises without added yeast.",
                 "Flour and water left together collect wild yeasts and bacteria.",
                 "Bakers have kept such cultures alive for generations.",
                 "Sequencing studies have identified the organisms only in the last "
                 "twenty years.",
                 "No two cultures, even in the same bakery, contain quite the same "
                 "mixture."],
                "The student wants to present a recent research finding. Which choice "
                "most effectively uses relevant information from the notes to accomplish "
                "this goal?"),
            "choices": [
                {"text": "Sequencing studies carried out over the last twenty years have found that no two sourdough cultures contain quite the same mixture of organisms.", "is_correct": True},
                {"text": "Sourdough bread rises without added yeast, because flour and water left together collect wild yeasts and bacteria.", "is_correct": False},
                {"text": "Bakers have kept sourdough cultures alive for generations without knowing what was in them.", "is_correct": False},
                {"text": "Flour and water left together will collect wild yeasts and bacteria from the grain and the air.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>present a <u>recent research "
                "finding</u></em>. Ikki talab: (1) tadqiqot natijasi bo'lsin, "
                "(2) <u>yaqinda</u> bo'lsin.</p>"
                + why([
                    (True, "Sequencing studies carried out over the last twenty years have found that no two sourdough cultures contain quite the same mixture of organisms",
                     "ikkala talabni ham bajaradi: sekvenatsiya tadqiqoti "
                     "(natija) va so'nggi yigirma yil (yaqinda)."),
                    (False, "Bakers have kept sourdough cultures alive for generations without knowing what was in them",
                     "<strong>eng jozibali tuzoq:</strong> u tadqiqot mavzusiga "
                     "yaqin va qaydlardan to'g'ri yig'ilgan. Lekin bu "
                     "tadqiqot <u>natijasi</u> emas — bu tarixiy fon."),
                    (False, "Sourdough bread rises without added yeast, because flour and water left together collect wild yeasts and bacteria",
                     "umumiy tushuntirish, tadqiqot natijasi emas — va u "
                     "ko'p asrlardan beri ma'lum."),
                    (False, "Flour and water left together will collect wild yeasts and bacteria from the grain and the air",
                     "yana umumiy fakt; «yaqinda» ham, «topilma» ham "
                     "yo'q."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Bioluminescence is light produced by a living organism.",
                 "It occurs in fireflies, in some fungi, and very widely in the deep "
                 "ocean.",
                 "The chemical reaction involves a molecule called luciferin.",
                 "Most deep-sea species that glow do so in blue-green light.",
                 "Blue-green light travels furthest through seawater."],
                "The student wants to explain why deep-sea bioluminescence is usually "
                "blue-green. Which choice most effectively uses relevant information "
                "from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Most deep-sea species that glow do so in blue-green light, which is the colour that travels furthest through seawater.", "is_correct": True},
                {"text": "Bioluminescence is light produced by a living organism, and it occurs in fireflies, some fungi and many deep-sea species.", "is_correct": False},
                {"text": "The chemical reaction that produces bioluminescence involves a molecule called luciferin.", "is_correct": False},
                {"text": "Blue-green light travels furthest through seawater.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>explain <u>why</u> deep-sea "
                "bioluminescence is usually blue-green</em>. Tushuntirish "
                "degani <mark>ikki qismni bog'lash</mark>: hodisa va uning "
                "sababi.</p>"
                + why([
                    (True, "Most deep-sea species that glow do so in blue-green light, which is the colour that travels furthest through seawater",
                     "ikkala qaydni bir jumlada bog'laydi: hodisa "
                     "(ko'k-yashil) + sabab (eng uzoq tarqaladi). "
                     "<em>which</em> bog'lanishni yasaydi."),
                    (False, "Blue-green light travels furthest through seawater",
                     "<strong>sababning yarmi</strong> — lekin u nimani "
                     "tushuntirayotgani aytilmagan. Yolg'iz o'zi bu jumla "
                     "bioluminessensiya haqida emas."),
                    (False, "Bioluminescence is light produced by a living organism, and it occurs in fireflies, some fungi and many deep-sea species",
                     "bu <u>ta'rif</u> — boshqa maqsad uchun mukammal javob "
                     "bo'lardi (tanishtirish). Bu yerda esa savol "
                     "«nega ko'k-yashil?» edi."),
                    (False, "The chemical reaction that produces bioluminescence involves a molecule called luciferin",
                     "mexanizmning boshqa tomoni — rang haqida hech nima "
                     "demaydi."),
                ])
                + TIP.format(
                    "<strong>Maqsaddagi fe'lga qarang.</strong> "
                    "<em>explain why</em> → sabab bog'lanishi kerak; "
                    "<em>introduce</em> → ta'rif; <em>emphasise</em> → bitta "
                    "narsani oldinga chiqarish; <em>compare</em> → ikkovi ham. "
                    "Fe'l javobning <u>shaklini</u> belgilaydi.")
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Ulugh Beg built an observatory in Samarkand in the 1420s.",
                 "Its main instrument was a huge arc set into the ground.",
                 "The observatory produced a catalogue of more than a thousand stars.",
                 "The catalogue's positions differ from modern values by only a few "
                 "minutes of arc.",
                 "The observatory was destroyed within a few decades of his death."],
                "The student wants to emphasise the accuracy of the catalogue. Which "
                "choice most effectively uses relevant information from the notes to "
                "accomplish this goal?"),
            "choices": [
                {"text": "The catalogue's star positions differ from modern values by only a few minutes of arc.", "is_correct": True},
                {"text": "Ulugh Beg's observatory in Samarkand, built in the 1420s, produced a catalogue of more than a thousand stars.", "is_correct": False},
                {"text": "The observatory's main instrument was a huge arc set into the ground.", "is_correct": False},
                {"text": "The observatory was destroyed within a few decades of Ulugh Beg's death.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>emphasise the <u>accuracy</u> "
                "of the catalogue</em>. Faqat bitta qayd aniqlik haqida "
                "gapiradi.</p>"
                + why([
                    (True, "The catalogue's star positions differ from modern values by only a few minutes of arc",
                     "aniqlikni <u>o'lchov bilan</u> ko'rsatadi — "
                     "<em>only a few minutes of arc</em>. Maqsadga to'g'ridan-"
                     "to'g'ri javob."),
                    (False, "Ulugh Beg's observatory in Samarkand, built in the 1420s, produced a catalogue of more than a thousand stars",
                     "<strong>miqdor ≠ aniqlik.</strong> Ming yulduz "
                     "ta'sirli, lekin ular qanchalik to'g'ri o'lchanganini "
                     "aytmaydi. Eng ko'p tanlanadigan noto'g'ri javob."),
                    (False, "The observatory's main instrument was a huge arc set into the ground",
                     "asbob aniqlikning <u>sababi</u> bo'lishi mumkin, lekin "
                     "qaydlar bu bog'lanishni bermaydi — va maqsad "
                     "sababni emas, aniqlikni ta'kidlashni so'raydi."),
                    (False, "The observatory was destroyed within a few decades of Ulugh Beg's death",
                     "butunlay boshqa mavzu."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to accomplish a goal</div><div class="pp-card-back">maqsadni bajarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">relevant information</div><div class="pp-card-back">maqsadga tegishli ma\'lumot</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to introduce ~ to an audience unfamiliar with it</div><div class="pp-card-back">bilmaydigan o\'quvchiga tanishtirmoq (= ta\'rif)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to emphasise</div><div class="pp-card-back">ta\'kidlamoq, oldinga chiqarmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a recent finding</div><div class="pp-card-back">yaqinda olingan tadqiqot natijasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">lacquer</div><div class="pp-card-back">lak (yopishtiruvchi qoplama)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">minutes of arc</div><div class="pp-card-back">yoy daqiqasi (burchak o\'lchovi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">bioluminescence</div><div class="pp-card-back">tirik organizm chiqaradigan yorug\'lik</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>To'rtala variant ham rost.</strong> Rostlik mezon "
              "emas.</li>"
              "<li><strong>Maqsad jumlasini birinchi o'qing</strong> — "
              "qaydlardan ham oldin.</li>"
              "<li>Maqsaddagi <u>fe'l</u> javobning shaklini belgilaydi: "
              "<em>introduce · emphasise · explain why · compare</em>.</li>"
              "<li>Ko'p qayd keraksiz bo'ladi — ular chalg'itish "
              "uchun.</li>"
              "<li>Ba'zan to'g'ri javob eng <u>zerikarli</u> variant "
              "bo'ladi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 21
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W21: Reading the Goal Sentence Like a Contract",
    "summary": "Maqsad jumlasidagi shartlarni sanang: nechta talab bo'lsa, to'g'ri "
               "javob shuncha talabni bajaradi — noto'g'rilari bittasini tashlab ketadi.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Maqsadni bo'laklarga ajrating</h2>"
            "<p>20-darsda ko'rdik: maqsad yagona mezon. Endi undan aniqroq "
            "ishlatishni o'rganamiz.</p>"
            "<p>Maqsad jumlasi <mark>shartnoma kabi</mark> o'qilishi kerak: "
            "unda bir nechta talab bo'ladi, va to'g'ri javob "
            "<u>hammasini</u> bajaradi. Noto'g'ri variantlar odatda "
            "bittasini bajaradi va bittasini tashlab ketadi — shuning uchun "
            "ular yarim to'g'ri tuyuladi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><em>The student wants to "
                "<u>explain the difference</u> between the two methods "
                "<u>to an audience unfamiliar with either</u>.</em></p>"
                "<p style=\"margin:0;\"><strong>Talablar:</strong> "
                "(1) ikkala usul nomlansin; (2) ular orasidagi farq "
                "aytilsin; (3) o'quvchi bilmaydi — demak ular nima ekani "
                "ham tushuntirilsin. <strong>Uchta.</strong></p>")
            + TIP.format(
                "Amaliy odat: maqsadni o'qib, barmoq bilan talablarni "
                "<strong>sanang</strong> — bir, ikki, uch. Keyin har "
                "variantni shu sanoq bo'yicha tekshiring. Ikkitasini "
                "bajarib, uchinchisini tashlab ketgan variant — javob "
                "emas.")
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Talab yasaydigan iboralar</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Maqsaddagi ibora</th><th>Qanday talab qo'yadi</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>to an audience unfamiliar with ~</em></td>"
              "<td>Ta'rif bo'lishi shart</td></tr>"
              "<tr><td><em>to an audience already familiar with ~</em></td>"
              "<td>Ta'rif <u>kerak emas</u> — u joyni behuda egallaydi</td></tr>"
              "<tr><td><em>the difference between A and B</em></td>"
              "<td>Ikkovi ham nomlansin va farq aytilsin</td></tr>"
              "<tr><td><em>a similarity between A and B</em></td>"
              "<td>Ikkovi ham va umumiy jihat</td></tr>"
              "<tr><td><em>using data / a statistic</em></td>"
              "<td>Raqam bo'lishi shart</td></tr>"
              "<tr><td><em>and its significance</em></td>"
              "<td>Fakt yetarli emas — <u>nega muhimligi</u> ham kerak</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<em>already familiar with</em> — eng ko'p e'tibordan chetda "
                "qoladigan ibora, va u <strong>teskari</strong> ishlaydi: "
                "ta'rif bergan variant endi <u>noto'g'ri</u> bo'ladi, "
                "chunki o'quvchi buni allaqachon biladi va maqsad boshqa "
                "narsa edi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Fresco is painting done on wet plaster.",
                 "The pigment sinks into the plaster and dries as part of the wall.",
                 "Secco is painting done on plaster that has already dried.",
                 "In secco the pigment sits on the surface and is held by a binder.",
                 "Secco can be retouched later; fresco cannot."],
                "The student wants to explain the difference between fresco and secco "
                "to an audience unfamiliar with either. Which choice most effectively "
                "uses relevant information from the notes to accomplish this goal?")
            + choices_html([
                "Secco can be retouched later, whereas fresco cannot.",
                "Fresco is painted on wet plaster, so the pigment dries as part of the "
                "wall; secco is painted on dry plaster, so the pigment sits on the "
                "surface.",
                "In secco the pigment sits on the surface of the plaster and is held "
                "there by a binder.",
                "Fresco is painting done on wet plaster, and the pigment sinks in and "
                "dries as part of the wall.",
            ])
            + "<p><strong>Talablarni sanaymiz:</strong> (1) ikkala usul "
            "nomlansin; (2) farq aytilsin; (3) o'quvchi bilmaydi — demak "
            "har biri nima ekani ham ochilsin. <strong>Uch.</strong></p>"
            + why([
                (True, "Fresco is painted on wet plaster, so the pigment dries as part of the wall; secco is painted on dry plaster, so the pigment sits on the surface",
                 "uchala talabni ham bajaradi: ikkovi nomlangan, ikkovi "
                 "ta'riflangan, va farq (ho'l ↔ quruq, ichiga ↔ ustiga) "
                 "aniq ko'rsatilgan."),
                (False, "Secco can be retouched later, whereas fresco cannot",
                 "<strong>farq bor, ta'rif yo'q.</strong> Ikkovi nomlangan "
                 "(1-talab), farq aytilgan (2-talab), lekin notanish "
                 "o'quvchi ularning <u>nima</u> ekanini bilmaydi "
                 "(3-talab bajarilmagan). Ikki uchdan — yetarli emas."),
                (False, "Fresco is painting done on wet plaster, and the pigment sinks in and dries as part of the wall",
                 "faqat <u>bitta</u> usul. Farq ham yo'q, ikkinchi "
                 "usul ham yo'q."),
                (False, "In secco the pigment sits on the surface of the plaster and is held there by a binder",
                 "yana faqat bitta usul, va freska umuman eslatilmaydi."),
            ])
            + NOTE.format(
                "Ikkinchi variantga alohida e'tibor bering: u <u>eng "
                "qiziqarli</u> farqni beradi (tuzatib bo'ladimi yoki "
                "yo'q). Agar o'quvchi ikkovini bilganida, bu javob "
                "bo'lardi. Maqsaddagi bitta ibora — "
                "<em>unfamiliar with either</em> — uni yiqitadi.")
        )},

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["The Silk Road is usually pictured as a single route from China to the "
                 "Mediterranean.",
                 "Goods in fact moved in short relays between neighbouring markets.",
                 "A merchant buying silk in Samarkand had often never seen where it was "
                 "made.",
                 "Ideas, techniques and diseases travelled along the same relays.",
                 "The name 'Silk Road' was coined by a German geographer in 1877."],
                "The student wants to correct a common misunderstanding for an audience "
                "already familiar with the term 'Silk Road'. Which choice most "
                "effectively uses relevant information from the notes to accomplish this "
                "goal?"),
            "choices": [
                {"text": "Rather than a single route, the Silk Road was a chain of short relays between neighbouring markets, so a merchant buying silk in Samarkand had often never seen where it was made.", "is_correct": True},
                {"text": "The Silk Road, a trading network linking China with the Mediterranean, carried goods, ideas, techniques and diseases.", "is_correct": False},
                {"text": "The name 'Silk Road' was coined by a German geographer in 1877.", "is_correct": False},
                {"text": "Ideas, techniques and diseases travelled along the Silk Road alongside goods.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Talablar:</strong> (1) noto'g'ri tushunchani "
                "tuzatsin; (2) o'quvchi atamani <u>allaqachon biladi</u> — "
                "demak ta'rif kerak emas.</p>"
                + why([
                    (True, "Rather than a single route, the Silk Road was a chain of short relays between neighbouring markets, so a merchant buying silk in Samarkand had often never seen where it was made",
                     "ikkala talab ham: <em>Rather than a single route</em> "
                     "aynan noto'g'ri tasavvurni nomlaydi va tuzatadi, va u "
                     "ta'rifga vaqt sarflamaydi."),
                    (False, "The Silk Road, a trading network linking China with the Mediterranean, carried goods, ideas, techniques and diseases",
                     "<strong>ta'rif beradi</strong> — lekin o'quvchi buni "
                     "biladi (<em>already familiar</em>). Va u hech qanday "
                     "noto'g'ri tushunchani tuzatmaydi."),
                    (False, "Ideas, techniques and diseases travelled along the Silk Road alongside goods",
                     "qiziqarli qo'shimcha, lekin bu tuzatish emas — "
                     "u odatiy tasavvurga zid emas."),
                    (False, "The name 'Silk Road' was coined by a German geographer in 1877",
                     "atamaning tarixi — mavzuga aloqador, lekin savolda "
                     "so'ralgan tuzatish emas."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["A green roof is a layer of soil and plants on top of a building.",
                 "Green roofs hold rainwater that would otherwise run into the drains.",
                 "A trial in one city measured runoff from ten green roofs and ten "
                 "conventional ones.",
                 "The green roofs released 58 percent less water in the hour after a "
                 "storm.",
                 "Green roofs cost roughly twice as much to install as a conventional "
                 "roof."],
                "The student wants to support a claim about green roofs using a "
                "statistic. Which choice most effectively uses relevant information from "
                "the notes to accomplish this goal?"),
            "choices": [
                {"text": "Green roofs hold rainwater effectively: in one city's trial they released 58 percent less water than conventional roofs in the hour after a storm.", "is_correct": True},
                {"text": "Green roofs hold rainwater that would otherwise run straight into the city's drains.", "is_correct": False},
                {"text": "A green roof is a layer of soil and plants placed on top of a building.", "is_correct": False},
                {"text": "Green roofs cost roughly twice as much to install as conventional roofs do.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Talablar:</strong> (1) da'voni qo'llab-quvvatlasin; "
                "(2) <u>raqam</u> bo'lsin. Ikkinchisi qattiq talab: "
                "<em>using a statistic</em>.</p>"
                + why([
                    (True, "Green roofs hold rainwater effectively: in one city's trial they released 58 percent less water than conventional roofs in the hour after a storm",
                     "da'vo + raqam. Ikki nuqtadan keyin aniq statistika "
                     "keladi (58%), va u da'voni to'g'ridan-to'g'ri "
                     "ko'taradi."),
                    (False, "Green roofs cost roughly twice as much to install as conventional roofs do",
                     "<strong>raqam bor, lekin da'voga qarshi:</strong> "
                     "«ikki barobar qimmat» yashil tomni qo'llab-quvvatlamaydi. "
                     "Ikkinchi talab bajarilgan, birinchisi buzilgan."),
                    (False, "Green roofs hold rainwater that would otherwise run straight into the city's drains",
                     "da'vo bor, <strong>raqam yo'q</strong>. Birinchi talab "
                     "bajarilgan, ikkinchisi yo'q."),
                    (False, "A green roof is a layer of soil and plants placed on top of a building",
                     "ta'rif — na da'vo, na raqam."),
                ])
                + TIP.format(
                    "<em>using a statistic</em> yoki <em>using data</em> "
                    "ko'rsangiz, birinchi harakat: <strong>raqamsiz "
                    "variantlarni o'chiring</strong>. Odatda ikkitasi "
                    "darrov tushadi.")
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Radiocarbon dating measures the decay of carbon-14 in organic "
                 "material.",
                 "It works on material up to about 50,000 years old.",
                 "Dendrochronology dates wood by counting and matching tree rings.",
                 "Dendrochronology can give a date to the exact year.",
                 "Tree-ring sequences reach back about 12,000 years in some regions."],
                "The student wants to present a similarity between the two dating "
                "methods and its significance for archaeologists. Which choice most "
                "effectively uses relevant information from the notes to accomplish this "
                "goal?"),
            "choices": [
                {"text": "Both radiocarbon dating and dendrochronology date organic material rather than stone or metal, which is why an archaeologist working on a site without wood, bone or charcoal can use neither.", "is_correct": True},
                {"text": "Dendrochronology can give a date to the exact year, while radiocarbon dating cannot.", "is_correct": False},
                {"text": "Radiocarbon dating works on material up to about 50,000 years old, and tree-ring sequences reach back about 12,000 years.", "is_correct": False},
                {"text": "Both methods are used by archaeologists to establish the age of the material they excavate.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Talablar:</strong> (1) <u>o'xshashlik</u> (farq "
                "emas); (2) ikkala usul ham; (3) <u>ahamiyati</u> — "
                "arxeolog uchun nega muhim.</p>"
                "<p>Uchinchi talab — <em>and its significance</em> — "
                "eng ko'p tashlab ketiladigani.</p>"
                + why([
                    (True, "Both radiocarbon dating and dendrochronology date organic material rather than stone or metal, which is why an archaeologist working on a site without wood, bone or charcoal can use neither",
                     "uchala talab: o'xshashlik (ikkovi ham organik "
                     "materialga), ikkala usul nomlangan, va ahamiyati "
                     "(<em>which is why…</em>)."),
                    (False, "Both methods are used by archaeologists to establish the age of the material they excavate",
                     "<strong>o'xshashlik bor, ahamiyat yo'q.</strong> "
                     "Va o'xshashlik juda umumiy — u ikkovi ham "
                     "«sana aniqlaydi» deyishdan nariga o'tmaydi."),
                    (False, "Dendrochronology can give a date to the exact year, while radiocarbon dating cannot",
                     "<strong>bu farq</strong>, o'xshashlik emas — birinchi "
                     "talabni to'g'ridan-to'g'ri buzadi."),
                    (False, "Radiocarbon dating works on material up to about 50,000 years old, and tree-ring sequences reach back about 12,000 years",
                     "ikki fakt yonma-yon qo'yilgan, lekin bu ham "
                     "<u>farq</u> (50,000 ↔ 12,000), va ahamiyati "
                     "aytilmagan."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["The Mediterranean monk seal is among the rarest seals in the world.",
                 "Fewer than 800 are thought to remain.",
                 "The species once bred on open beaches.",
                 "It now breeds almost only in sea caves.",
                 "The shift is thought to follow the human use of the coastline."],
                "The student wants to describe a change in the species\u2019 behaviour and "
                "its likely cause. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "The Mediterranean monk seal, which once bred on open beaches, now breeds almost only in sea caves, a shift thought to follow the human use of the coastline.", "is_correct": True},
                {"text": "The Mediterranean monk seal once bred on open beaches but now breeds almost only in sea caves.", "is_correct": False},
                {"text": "Fewer than 800 Mediterranean monk seals are thought to remain, making the species among the rarest seals in the world.", "is_correct": False},
                {"text": "The human use of the coastline is thought to explain why the Mediterranean monk seal is now among the rarest seals in the world.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Talablar:</strong> (1) xatti-harakatdagi "
                "o\u2018zgarish; (2) uning <u>ehtimoliy sababi</u>. "
                "Ikkita \u2014 va ikkinchisi eng ko\u2018p tashlab "
                "ketiladigani.</p>"
                + why([
                    (True, "The Mediterranean monk seal, which once bred on open beaches, now breeds almost only in sea caves, a shift thought to follow the human use of the coastline",
                     "ikkala talab ham: o\u2018zgarish (plyaj \u2192 g\u2018or) va sabab "
                     "(<em>a shift thought to follow…</em>). "
                     "<em>thought to</em> qaydlardagi ehtiyotkorlikni ham "
                     "saqlaydi."),
                    (False, "The Mediterranean monk seal once bred on open beaches but now breeds almost only in sea caves",
                     "<strong>o\u2018zgarish bor, sabab yo\u2018q.</strong> Birinchi "
                     "talab bajarilgan, ikkinchisi tashlab ketilgan \u2014 "
                     "bu darsning asosiy tuzog\u2018i."),
                    (False, "The human use of the coastline is thought to explain why the Mediterranean monk seal is now among the rarest seals in the world",
                     "<strong>qaydlarni buzadi:</strong> matnda inson "
                     "faoliyati <u>ko\u2018payish joyining o\u2018zgarishiga</u> "
                     "bog\u2018langan, turning kamayishiga emas. Sabab boshqa "
                     "narsaga ulangan."),
                    (False, "Fewer than 800 Mediterranean monk seals are thought to remain, making the species among the rarest seals in the world",
                     "kamyoblik haqida \u2014 na o\u2018zgarish, na sabab. "
                     "Butunlay maqsaddan tashqarida."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">unfamiliar with ~</div><div class="pp-card-back">~ ni bilmaydigan (→ ta\'rif kerak)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">already familiar with ~</div><div class="pp-card-back">~ ni allaqachon biladigan (→ ta\'rif kerak emas)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">and its significance</div><div class="pp-card-back">va uning ahamiyati (qo\'shimcha talab)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">using a statistic</div><div class="pp-card-back">raqam bilan (raqamsiz javob yaramaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">fresco / secco</div><div class="pp-card-back">ho\'l suvoqqa / quruq suvoqqa rasm solish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to retouch</div><div class="pp-card-back">keyinchalik tuzatmoq, ustidan ishlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">runoff</div><div class="pp-card-back">oqib ketadigan suv</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">dendrochronology</div><div class="pp-card-back">daraxt halqalari bo\'yicha sana aniqlash</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Maqsadni <strong>shartnoma</strong> kabi o'qing va "
              "talablarni <u>sanang</u>.</li>"
              "<li>To'g'ri javob <strong>hammasini</strong> bajaradi; "
              "tuzoqlar bittasini tashlab ketadi.</li>"
              "<li><em>unfamiliar with</em> → ta'rif shart. "
              "<em>already familiar</em> → ta'rif ortiqcha.</li>"
              "<li><em>using a statistic</em> → raqamsiz variantlarni "
              "darrov o'chiring.</li>"
              "<li><em>and its significance</em> → fakt yetarli emas, "
              "«nega muhim» ham kerak.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 22
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W22: Goals That Compare, Goals That Emphasise, Goals That Introduce",
    "summary": "Uch eng ko'p uchraydigan maqsad oilasi va ularning har biri javobdan "
               "talab qiladigan aniq shakl.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Uch oila, uch shakl</h2>"
            "<p>Maqsad jumlalari cheksiz xilma-xil ko'rinadi, lekin amalda "
            "ular <mark>uchta oiladan</mark> biriga tushadi. Har oila "
            "javobdan aniq bir shaklni talab qiladi — va shakl mos "
            "kelmasa, mazmun qanchalik rost bo'lmasin, javob "
            "emas.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Oila</th><th>Maqsaddagi fe'l</th>"
              "<th>Javobning shakli</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Tanishtirish</strong></td>"
              "<td><em>introduce · explain … to an audience unfamiliar</em></td>"
              "<td>«X — bu …» ta'rifi; bitta narsa haqida</td></tr>"
              "<tr><td><strong>Ta'kidlash</strong></td>"
              "<td><em>emphasise · highlight · underscore</em></td>"
              "<td>Bitta narsani oldinga chiqaradi; ko'pincha o'lchov "
              "yoki qiyoslash bilan</td></tr>"
              "<tr><td><strong>Solishtirish</strong></td>"
              "<td><em>compare · contrast · a similarity · a difference</em></td>"
              "<td><u>Ikkovi ham</u> jumlada, va aloqa aytilgan</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Eng tez tekshiruv <strong>solishtirish</strong> oilasida: "
                "javobda <u>ikkala</u> narsa nomlanganmi? Bitta narsa haqida "
                "gapirgan variant darrov tushadi, mazmuni qanday "
                "bo'lishidan qat'i nazar. Bu odatda ikki variantni "
                "besh soniyada o'chiradi.")
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna — ta'kidlash</h3>"
            + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["The Voyager 1 probe was launched in 1977.",
                 "It carries a gold-plated record of sounds and images from Earth.",
                 "It left the region influenced by the Sun's wind in 2012.",
                 "Its radio signal now takes over twenty hours to reach Earth.",
                 "Its instruments are powered by a slowly decaying source and will fall "
                 "silent in the 2030s."],
                "The student wants to emphasise how far from Earth the probe now is. "
                "Which choice most effectively uses relevant information from the notes "
                "to accomplish this goal?")
            + choices_html([
                "Voyager 1, launched in 1977, carries a gold-plated record of sounds and "
                "images from Earth.",
                "Voyager 1's radio signal now takes over twenty hours to reach Earth.",
                "Voyager 1's instruments are powered by a slowly decaying source and "
                "will fall silent in the 2030s.",
                "Voyager 1 left the region influenced by the Sun's wind in 2012.",
            ])
            + "<p><strong>Maqsad oilasi:</strong> ta'kidlash — "
            "<em>emphasise <u>how far</u></em>. Demak javob masofani "
            "<mark>his qildiradigan</mark> bo'lishi kerak, ideal holda "
            "o'lchov bilan.</p>"
            + why([
                (True, "Voyager 1's radio signal now takes over twenty hours to reach Earth",
                 "masofani bevosita o'lchaydi, va uni tasavvur qilinadigan "
                 "shaklda beradi: yorug'lik tezligida yigirma soat. "
                 "Ta'kidlash oilasi aynan shuni so'raydi."),
                (False, "Voyager 1 left the region influenced by the Sun's wind in 2012",
                 "<strong>eng jozibali tuzoq:</strong> u ham uzoqlikni "
                 "bildiradi. Lekin u <u>chegara</u> haqida, masofa haqida "
                 "emas — va o'quvchi o'sha chegara qanchalik uzoq ekanini "
                 "bilmaydi."),
                (False, "Voyager 1's instruments are powered by a slowly decaying source and will fall silent in the 2030s",
                 "vaqt va quvvat haqida — masofani umuman "
                 "ko'rsatmaydi."),
                (False, "Voyager 1, launched in 1977, carries a gold-plated record of sounds and images from Earth",
                 "eng qiziqarli fakt, va shuning uchun xavfli. Lekin u "
                 "tanishtirish oilasining javobi — bu yerda maqsad "
                 "boshqa."),
            ])
        )},

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Adobe is a building material of earth, sand and straw, dried in the "
                 "sun.",
                 "Fired brick is the same clay baked in a kiln.",
                 "Adobe walls absorb heat slowly and release it at night.",
                 "Fired brick is stronger and resists rain far better.",
                 "Adobe needs replastering after heavy rain; fired brick does not."],
                "The student wants to present a difference between adobe and fired brick "
                "to an audience already familiar with both. Which choice most "
                "effectively uses relevant information from the notes to accomplish this "
                "goal?"),
            "choices": [
                {"text": "Fired brick resists rain far better than adobe, which needs replastering after a heavy storm.", "is_correct": True},
                {"text": "Adobe is a building material of earth, sand and straw dried in the sun, while fired brick is the same clay baked in a kiln.", "is_correct": False},
                {"text": "Adobe walls absorb heat slowly and release it again at night.", "is_correct": False},
                {"text": "Fired brick is stronger than adobe and does not need replastering.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki talab:</strong> (1) solishtirish oilasi — "
                "ikkovi ham jumlada bo'lsin va farq aytilsin; "
                "(2) <em>already familiar with both</em> — ta'rif "
                "<u>kerak emas</u>.</p>"
                + why([
                    (True, "Fired brick resists rain far better than adobe, which needs replastering after a heavy storm",
                     "ikkovi nomlangan, farq aniq (yomg'irga chidamlilik), "
                     "va ta'rifga vaqt sarflanmagan."),
                    (False, "Adobe is a building material of earth, sand and straw dried in the sun, while fired brick is the same clay baked in a kiln",
                     "<strong>ta'rif beradi</strong> — lekin o'quvchi ikkovini "
                     "ham biladi. Bu 21-darsdagi <em>already familiar</em> "
                     "tuzog'i."),
                    (False, "Fired brick is stronger than adobe and does not need replastering",
                     "<strong>juda yaqin va shuning uchun xavfli.</strong> "
                     "Ikkovi nomlangan va farq bor. Lekin qaydlarga ko'ra "
                     "<em>replastering</em> yomg'irdan keyin kerak bo'ladi; "
                     "bu variant sababni tushirib qoldirib, umumiy da'vo "
                     "qiladi. To'g'ri javob esa <em>after a heavy storm</em> "
                     "shartini saqlaydi."),
                    (False, "Adobe walls absorb heat slowly and release it again at night",
                     "faqat bitta material — solishtirish yo'q."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Espalier is the practice of training a fruit tree flat against a wall.",
                 "The branches are tied to a frame and pruned to a single plane.",
                 "A wall stores heat during the day and releases it at night.",
                 "Espaliered trees in cool climates ripen fruit that free-standing trees "
                 "of the same variety do not.",
                 "The practice was common in northern European gardens from the "
                 "seventeenth century."],
                "The student wants to introduce espalier to an audience unfamiliar with "
                "the term. Which choice most effectively uses relevant information from "
                "the notes to accomplish this goal?"),
            "choices": [
                {"text": "Espalier is the practice of training a fruit tree flat against a wall, its branches tied to a frame and pruned to a single plane.", "is_correct": True},
                {"text": "Espaliered trees in cool climates ripen fruit that free-standing trees of the same variety do not.", "is_correct": False},
                {"text": "The practice was common in northern European gardens from the seventeenth century onward.", "is_correct": False},
                {"text": "A wall stores heat during the day and releases it again at night.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad oilasi:</strong> tanishtirish. Notanish "
                "o'quvchi <em>espalier</em> so'zini birinchi marta "
                "ko'ryapti — javob <mark>«X — bu …»</mark> shaklida "
                "bo'lishi shart.</p>"
                + why([
                    (True, "Espalier is the practice of training a fruit tree flat against a wall, its branches tied to a frame and pruned to a single plane",
                     "aniq ta'rif: nima ekani va qanday qilinishi. Notanish "
                     "o'quvchi shu jumladan keyin tushunadi."),
                    (False, "Espaliered trees in cool climates ripen fruit that free-standing trees of the same variety do not",
                     "eng qiziqarli natija — va aynan shuning uchun tuzoq. "
                     "U <u>espalier nima ekanini biladigan</u> o'quvchi uchun "
                     "yozilgan."),
                    (False, "A wall stores heat during the day and releases it again at night",
                     "mexanizmning bir bo'lagi; <em>espalier</em> so'zi hatto "
                     "uchramaydi ham."),
                    (False, "The practice was common in northern European gardens from the seventeenth century onward",
                     "tarixiy fon — ta'rif emas."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Both octopuses and cuttlefish can change the colour of their skin.",
                 "Octopuses have a single visual pigment and are probably colour-blind.",
                 "Cuttlefish also have a single visual pigment.",
                 "Both animals match backgrounds they cannot, as far as is known, see in "
                 "colour.",
                 "Light-sensitive proteins have been found in the skin of both."],
                "The student wants to present a similarity between the two animals and "
                "the puzzle it raises. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Octopuses and cuttlefish both match backgrounds in colour, although each has only a single visual pigment and is probably unable to see colour at all.", "is_correct": True},
                {"text": "Both octopuses and cuttlefish are able to change the colour of their skin.", "is_correct": False},
                {"text": "Light-sensitive proteins have been found in the skin of both octopuses and cuttlefish.", "is_correct": False},
                {"text": "Octopuses have a single visual pigment and are probably colour-blind.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki talab:</strong> (1) o'xshashlik — ikkala "
                "hayvon ham; (2) <em>the puzzle it raises</em> — "
                "u tug'diradigan <u>jumboq</u>.</p>"
                + why([
                    (True, "Octopuses and cuttlefish both match backgrounds in colour, although each has only a single visual pigment and is probably unable to see colour at all",
                     "ikkala talab: o'xshashlik (ikkovi ham rang moslaydi) "
                     "va jumboq (<em>although … unable to see colour</em>). "
                     "<em>although</em> ziddiyatni ochib beradi."),
                    (False, "Both octopuses and cuttlefish are able to change the colour of their skin",
                     "<strong>o'xshashlik bor, jumboq yo'q.</strong> Ikkinchi "
                     "talab tashlab ketilgan — 21-darsdagi doimiy "
                     "tuzoq."),
                    (False, "Octopuses have a single visual pigment and are probably colour-blind",
                     "faqat bitta hayvon — o'xshashlik yo'q."),
                    (False, "Light-sensitive proteins have been found in the skin of both octopuses and cuttlefish",
                     "ikkovi haqida, lekin bu <u>ehtimoliy yechim</u>, "
                     "jumboqning o'zi emas. Maqsad jumboqni qo'yishni "
                     "so'raydi."),
                ])
                + TIP.format(
                    "<strong>Maqsadning ikkinchi yarmiga alohida "
                    "e'tibor:</strong> <em>and the puzzle it raises</em>, "
                    "<em>and its significance</em>, <em>and why it "
                    "matters</em>. Bu qo'shimchalar deyarli har doim "
                    "javobni bitta variantga qisqartiradi — chunki "
                    "faqat bittasi ikkinchi yarmini ham bajaradi.")
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["A suspension bridge hangs its deck from cables strung between towers.",
                 "A cantilever bridge supports its deck on arms projecting from piers.",
                 "Suspension bridges span greater distances than any other type.",
                 "Cantilever bridges can be built outward from each pier without "
                 "temporary supports beneath.",
                 "A suspension bridge needs its cables in place before any deck can be "
                 "hung."],
                "The student wants to emphasise a strength of suspension bridges. Which "
                "choice most effectively uses relevant information from the notes to "
                "accomplish this goal?"),
            "choices": [
                {"text": "Suspension bridges span greater distances than any other type of bridge.", "is_correct": True},
                {"text": "A suspension bridge needs its cables in place before any deck can be hung.", "is_correct": False},
                {"text": "A suspension bridge hangs its deck from cables strung between two towers.", "is_correct": False},
                {"text": "Cantilever bridges can be built outward from each pier without temporary supports beneath.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad oilasi:</strong> ta\u2019kidlash, va aniq "
                "yo\u2018nalish bilan \u2014 <em>a <u>strength</u> of "
                "<u>suspension</u> bridges</em>. Ikki cheklov: ijobiy "
                "jihat, va aynan osma ko\u2018prik haqida.</p>"
                + why([
                    (True, "Suspension bridges span greater distances than any other type of bridge",
                     "yagona variant osma ko\u2018prikning <u>ustunligini</u> "
                     "beradi, va <em>than any other type</em> uni yanada "
                     "kuchaytiradi."),
                    (False, "A suspension bridge needs its cables in place before any deck can be hung",
                     "<strong>to\u2018g\u2018ri ko\u2018prik, noto\u2018g\u2018ri yo\u2018nalish:</strong> "
                     "bu cheklov, ustunlik emas. Eng ko\u2018p tanlanadigan "
                     "noto\u2018g\u2018ri javob."),
                    (False, "Cantilever bridges can be built outward from each pier without temporary supports beneath",
                     "<strong>noto\u2018g\u2018ri ko\u2018prik:</strong> bu konsol "
                     "ko\u2018prikning ustunligi. Maqsad osma ko\u2018prik haqida "
                     "edi."),
                    (False, "A suspension bridge hangs its deck from cables strung between two towers",
                     "ta\u2019rif \u2014 tanishtirish oilasining javobi. Bu yerda "
                     "maqsad ta\u2019kidlash edi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to underscore</div><div class="pp-card-back">ta\'kidlamoq, tagini chizmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the puzzle it raises</div><div class="pp-card-back">u tug\'diradigan jumboq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">adobe</div><div class="pp-card-back">quyoshda quritilgan tuproq g\'isht</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a kiln</div><div class="pp-card-back">o\'choq, pech (g\'isht pishirish uchun)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to replaster</div><div class="pp-card-back">qayta suvamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">espalier</div><div class="pp-card-back">devorga yassilab o\'stirilgan meva daraxti</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to prune</div><div class="pp-card-back">butamoq, shoxlarini kesmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">free-standing</div><div class="pp-card-back">alohida, mustaqil turgan</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Uch oila: <strong>tanishtirish · ta'kidlash · "
              "solishtirish</strong>.</li>"
              "<li>Tanishtirish → «X — bu …» ta'rifi.</li>"
              "<li>Ta'kidlash → bitta narsa, ko'pincha o'lchov bilan.</li>"
              "<li>Solishtirish → <strong>ikkovi ham jumlada</strong>; bitta "
              "narsali variantni darrov o'chiring.</li>"
              "<li>Maqsadning ikkinchi yarmi (<em>and its significance</em>) "
              "javobni bitta variantga qisqartiradi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 23
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W23: Accurate but Off-Goal — The Most Common Wrong Choice",
    "summary": "Bu turdagi deyarli har bir noto'g'ri javob rost bo'ladi. Rostlikni "
               "tekshirish behuda mehnat — maqsadga moslikni tekshiring.",
    "order": 23,
    "blocks": [
        {"rich_text": (
            "<h2>Rostlikni tekshirmang</h2>"
            "<p>Bu dars bitta odatni sindiradi. Ko'p o'quvchi Rhetorical "
            "Synthesis savolini shunday yechadi: har variantni o'qib, "
            "qaydlarga qaytib, «bu rostmi?» deb tekshiradi.</p>"
            "<p>Bu mehnat butunlay <mark>behuda</mark>. To'rtala variant "
            "ham rost bo'ladi — SAT bu turda soxta ma'lumot "
            "bermaydi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\">Rostlikni tekshirish — "
                "<u>nol</u> ma'lumot beradi va vaqtingizning yarmini "
                "yeydi. Maqsadga moslikni tekshirish — savolni "
                "yechadi.</p>")
            + "<p>Ba'zan bitta variant qaydlarni <u>buzadi</u> "
            "(24-darsning mavzusi), lekin bu kamdan-kam. Odatiy savolda "
            "to'rtta rost jumla bor va ulardan uchtasi noto'g'ri "
            "joyda.</p>"
            + '<span class="sr-time">⏱ ~70 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Off-goal javobning to'rt ko'rinishi</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Ko'rinish</th><th>Nima qiladi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Boshqa maqsadning javobi</strong></td>"
              "<td>Ta'rif so'ralganda natijani, natija so'ralganda ta'rifni "
              "beradi</td></tr>"
              "<tr><td><strong>Yarim maqsad</strong></td>"
              "<td>Ikki talabdan bittasini bajaradi (21-dars)</td></tr>"
              "<tr><td><strong>Noto'g'ri subyekt</strong></td>"
              "<td>Maqsad A haqida, javob B haqida</td></tr>"
              "<tr><td><strong>Noto'g'ri yo'nalish</strong></td>"
              "<td>Ustunlik so'ralganda kamchilikni, ijobiy so'ralganda "
              "salbiyni beradi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Amaliy tartib: variantni o'qib bo'lgach, "
                "<strong>qaydlarga qaramang</strong> — maqsad jumlasiga "
                "qarang. Ko'zingiz variant bilan maqsad orasida yursin, "
                "qaydlar bilan emas. Qaydlar faqat "
                "<u>bir marta</u>, boshida o'qiladi.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Qanats are underground channels that carry water from a hillside "
                 "aquifer to a settlement.",
                 "The channel runs on a very shallow gradient, so the water moves "
                 "without pumping.",
                 "Vertical shafts along its length were used for digging and are still "
                 "used for maintenance.",
                 "Because the water travels underground, very little is lost to "
                 "evaporation.",
                 "Some qanats in Iran have been in continuous use for more than two "
                 "thousand years."],
                "The student wants to emphasise the durability of the system. Which "
                "choice most effectively uses relevant information from the notes to "
                "accomplish this goal?")
            + choices_html([
                "A qanat is an underground channel carrying water from a hillside "
                "aquifer to a settlement.",
                "Some qanats in Iran have carried water continuously for more than two "
                "thousand years.",
                "Because a qanat runs underground, very little of its water is lost to "
                "evaporation.",
                "Vertical shafts along a qanat's length were dug for construction and "
                "are still used for maintenance.",
            ])
            + "<p><strong>Maqsad:</strong> <em>emphasise the "
            "<u>durability</u></em> — tizim qanchalik uzoq "
            "chidashini.</p>"
            "<p>Endi to'rtala variantni <u>faqat maqsadga</u> "
            "solishtiramiz. Qaydlarni qayta o'qish shart emas — hammasi "
            "rost.</p>"
            + why([
                (True, "Some qanats in Iran have carried water continuously for more than two thousand years",
                 "yagona variant vaqtni beradi — va ikki ming yil "
                 "chidamlilikning eng kuchli o'lchovi. "
                 "<em>continuously</em> so'zi ham ishlaydi."),
                (False, "Because a qanat runs underground, very little of its water is lost to evaporation",
                 "<strong>boshqa maqsadning javobi.</strong> Bu "
                 "<u>samaradorlik</u> — «nega qanat foydali» degan savolga "
                 "mukammal javob bo'lardi. Lekin chidamlilik haqida hech "
                 "nima demaydi."),
                (False, "Vertical shafts along a qanat's length were dug for construction and are still used for maintenance",
                 "<strong>eng nozik tuzoq:</strong> <em>still used</em> "
                 "chidamlilikka ishora qilgandek tuyuladi. Lekin jumlaning "
                 "mavzusi — shaxtalarning vazifasi, tizimning umri "
                 "emas."),
                (False, "A qanat is an underground channel carrying water from a hillside aquifer to a settlement",
                 "ta'rif — tanishtirish oilasining javobi (22-dars). "
                 "Maqsad ta'kidlash edi."),
            ])
            + NOTE.format(
                "Qanat (koriz) tizimlari Eron, Afg'oniston va O'zbekiston "
                "hududlarida ming yillar davomida ishlatilgan yer osti suv "
                "kanallari. Mavzu tanish bo'lishi mumkin — lekin javob "
                "baribir faqat maqsaddan chiqadi.")
        )},

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Lacquer is a resin tapped from a tree that grows in East Asia.",
                 "It hardens by absorbing moisture from the air rather than by drying "
                 "out.",
                 "A finished piece may carry more than thirty separate coats.",
                 "Each coat must harden fully before the next is applied.",
                 "A single bowl can therefore take a year to complete."],
                "The student wants to explain why lacquerwork is slow to produce. Which "
                "choice most effectively uses relevant information from the notes to "
                "accomplish this goal?"),
            "choices": [
                {"text": "A finished piece may carry more than thirty coats, and because each must harden fully before the next is applied, a single bowl can take a year.", "is_correct": True},
                {"text": "Lacquer is a resin tapped from a tree that grows in East Asia.", "is_correct": False},
                {"text": "Lacquer hardens by absorbing moisture from the air rather than by drying out.", "is_correct": False},
                {"text": "A single lacquered bowl can take a year to complete.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>explain <u>why</u> it is "
                "slow</em>. Tushuntirish — ya'ni sabab kerak, natija "
                "emas.</p>"
                + why([
                    (True, "A finished piece may carry more than thirty coats, and because each must harden fully before the next is applied, a single bowl can take a year",
                     "sababni ham (o'ttiz qatlam × to'liq qotish), natijani "
                     "ham (bir yil) beradi. <em>because</em> ularni "
                     "bog'laydi."),
                    (False, "A single lacquered bowl can take a year to complete",
                     "<strong>natija, sabab emas.</strong> Bu «qancha vaqt "
                     "oladi?» degan savolga javob — «nega?» degan savolga "
                     "emas. Eng ko'p tanlanadigan noto'g'ri javob."),
                    (False, "Lacquer hardens by absorbing moisture from the air rather than by drying out",
                     "qiziqarli kimyoviy fakt, lekin u sekinlikni "
                     "tushuntirmaydi — namlik yutish o'z-o'zicha sekin "
                     "degani emas."),
                    (False, "Lacquer is a resin tapped from a tree that grows in East Asia",
                     "ta'rif — boshqa maqsadning javobi."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Ballast water is taken on by a ship to keep it stable when it is "
                 "lightly loaded.",
                 "It is pumped in at one port and discharged at another.",
                 "Organisms drawn in with the water can survive the voyage.",
                 "A single species of mussel spread across four continents this way "
                 "within forty years.",
                 "Modern rules require ballast water to be exchanged or treated at sea."],
                "The student wants to illustrate the scale of the problem. Which choice "
                "most effectively uses relevant information from the notes to accomplish "
                "this goal?"),
            "choices": [
                {"text": "One species of mussel spread across four continents in ballast water within forty years.", "is_correct": True},
                {"text": "Modern rules require ballast water to be exchanged or treated at sea.", "is_correct": False},
                {"text": "Ballast water is taken on to keep a lightly loaded ship stable and is discharged at the next port.", "is_correct": False},
                {"text": "Organisms drawn in with ballast water can survive the voyage between ports.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>illustrate the "
                "<u>scale</u></em> — muammoning kattaligini "
                "ko'rsatish. Demak son, masofa yoki qamrov kerak.</p>"
                + why([
                    (True, "One species of mussel spread across four continents in ballast water within forty years",
                     "yagona variant miqyosni beradi: to'rt qit'a, qirq yil, "
                     "bitta tur. Konkret raqamlar ko'lamni "
                     "his qildiradi."),
                    (False, "Organisms drawn in with ballast water can survive the voyage between ports",
                     "<strong>muammoning mexanizmi</strong>, ko'lami emas. "
                     "U «bu qanday sodir bo'ladi?» degan savolga javob "
                     "berardi."),
                    (False, "Modern rules require ballast water to be exchanged or treated at sea",
                     "<strong>yechim</strong>, muammoning ko'lami emas — va "
                     "yo'nalishi ham teskari."),
                    (False, "Ballast water is taken on to keep a lightly loaded ship stable and is discharged at the next port",
                     "ta'rif."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Chess engines now defeat the strongest human players consistently.",
                 "An engine evaluates positions by searching millions of continuations.",
                 "Human players search perhaps two or three dozen.",
                 "Grandmasters still recognise the right move in most positions within "
                 "seconds.",
                 "Engines and humans agree on the best move in the great majority of "
                 "positions."],
                "The student wants to emphasise how differently the two arrive at the "
                "same answer. Which choice most effectively uses relevant information "
                "from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Engines and humans agree on the best move in most positions, though the engine reaches it by searching millions of continuations and the grandmaster by recognising it within seconds.", "is_correct": True},
                {"text": "Chess engines now defeat even the strongest human players consistently.", "is_correct": False},
                {"text": "A chess engine evaluates a position by searching millions of possible continuations.", "is_correct": False},
                {"text": "Grandmasters recognise the right move in most positions within seconds.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad ikki qismli:</strong> (1) ular "
                "<u>bir xil javobga</u> keladi; (2) <u>boshqacha "
                "yo'l bilan</u>. Ikkovi ham jumlada bo'lishi kerak.</p>"
                + why([
                    (True, "Engines and humans agree on the best move in most positions, though the engine reaches it by searching millions of continuations and the grandmaster by recognising it within seconds",
                     "ikkala qism ham: kelishuv (<em>agree … in most "
                     "positions</em>) va usuldagi farq (millionlab ↔ bir "
                     "necha soniya). <em>though</em> qarama-qarshilikni "
                     "ochadi."),
                    (False, "A chess engine evaluates a position by searching millions of possible continuations",
                     "<strong>yarim maqsad:</strong> faqat bir tomonning "
                     "usuli. Grossmeyster ham, kelishuv ham yo'q."),
                    (False, "Grandmasters recognise the right move in most positions within seconds",
                     "yana yarim: ikkinchi tomon, birinchisisiz."),
                    (False, "Chess engines now defeat even the strongest human players consistently",
                     "<strong>noto'g'ri yo'nalish:</strong> bu <u>farq "
                     "natijasi</u> haqida (kim yutadi), maqsad esa "
                     "<u>bir xil javobga turli yo'l bilan kelish</u> "
                     "haqida edi."),
                ])
                + TIP.format(
                    "Bu darsdagi to'rtala savolda ham to'g'ri javob "
                    "<u>eng uzun</u> variant bo'ldi. Bu tez-tez shunday: "
                    "maqsadda ikki talab bo'lsa, ikkovini ham bajargan "
                    "jumla uzunroq bo'ladi. Lekin buni "
                    "<strong>qoida qilib olmang</strong> — uzunlik dalil "
                    "emas, faqat naqsh.")
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Nightingales sing at night mainly in spring.",
                 "Only unpaired males sing at night.",
                 "Once a male has attracted a mate he sings almost entirely at dawn.",
                 "The dawn song is quieter and more varied than the night song.",
                 "The night song carries much further."],
                "The student wants to explain why only some nightingales sing at night. "
                "Which choice most effectively uses relevant information from the notes "
                "to accomplish this goal?"),
            "choices": [
                {"text": "Only unpaired males sing at night; once a male has attracted a mate he sings almost entirely at dawn.", "is_correct": True},
                {"text": "The night song of the nightingale carries much further than the dawn song does.", "is_correct": False},
                {"text": "The dawn song of the nightingale is quieter and more varied than its night song.", "is_correct": False},
                {"text": "Nightingales sing at night mainly during the spring.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> nega <u>faqat ba\u2019zilari</u> "
                "tunda sayraydi. Ya\u2019ni savol <mark>qaysi qushlar</mark> "
                "haqida, na tovushning xususiyati haqida.</p>"
                + why([
                    (True, "Only unpaired males sing at night; once a male has attracted a mate he sings almost entirely at dawn",
                     "aynan «faqat ba\u2019zilari» ni tushuntiradi: juftini "
                     "topmagan erkaklar. Va nuqtali vergul o\u2018zgarishni "
                     "ham qo\u2018shadi."),
                    (False, "The night song of the nightingale carries much further than the dawn song does",
                     "<strong>noto\u2018g\u2018ri subyekt:</strong> bu tungi "
                     "sayrashning <u>foydasi</u> \u2014 nega u ish beradi. "
                     "Savol esa <u>kim</u> sayraydi degan edi."),
                    (False, "The dawn song of the nightingale is quieter and more varied than its night song",
                     "yana noto\u2018g\u2018ri subyekt, va bu safar butunlay "
                     "boshqa sayrash haqida."),
                    (False, "Nightingales sing at night mainly during the spring",
                     "<u>qachon</u> degan savolga javob \u2014 <u>kim</u> "
                     "degan savolga emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">off-goal</div><div class="pp-card-back">maqsaddan chetda (rost, lekin mos emas)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">durability</div><div class="pp-card-back">chidamlilik, uzoq xizmat qilish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to illustrate the scale</div><div class="pp-card-back">ko\'lamini ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an aquifer</div><div class="pp-card-back">yer osti suv qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a shallow gradient</div><div class="pp-card-back">juda kichik nishablik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">ballast water</div><div class="pp-card-back">kemani muvozanatlash uchun olinadigan suv</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a coat (of lacquer)</div><div class="pp-card-back">(lak) qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a continuation (chess)</div><div class="pp-card-back">davomi, variant (shaxmatda)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Rostlikni tekshirmang</strong> — to'rttasi ham "
              "rost. Bu nol ma'lumot beradi.</li>"
              "<li>Ko'zingiz <u>variant ↔ maqsad</u> orasida yursin, "
              "qaydlar bilan emas.</li>"
              "<li>Off-goal to'rt ko'rinishi: boshqa maqsadning javobi · "
              "yarim maqsad · noto'g'ri subyekt · noto'g'ri "
              "yo'nalish.</li>"
              "<li><em>explain why</em> → sabab kerak, "
              "<u>natija emas</u>.</li>"
              "<li>Qaydlarni <strong>bir marta</strong>, boshida "
              "o'qing.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 24
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W24: Using Two Notes in One Sentence Without Distorting Either",
    "summary": "Ikki qaydni bir jumlaga birlashtirganda qo'shilib qoladigan narsalar: "
               "qaydlarda bo'lmagan sabab, kuchaytirilgan da'vo, ag'darilgan bog'lanish.",
    "order": 24,
    "blocks": [
        {"rich_text": (
            "<h2>Birlashtirish — lekin qo'shmasdan</h2>"
            "<p>Ko'p maqsad ikki talab qo'yadi, va to'g'ri javob "
            "<u>ikki qaydni bitta jumlaga</u> birlashtiradi. Bu yerda "
            "yangi xavf paydo bo'ladi: birlashtirish paytida "
            "<mark>qaydlarda bo'lmagan narsa qo'shilib qolishi</mark> "
            "mumkin.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><strong>Qaydlar:</strong><br>"
                "— Shahar 2015-yilda velosiped yo'laklarini qurdi.<br>"
                "— Velosipedchilar soni 2015 dan 2020 gacha ikki barobar "
                "oshdi.</p>"
                "<p style=\"margin:0;\"><strong>Buzilgan birlashtirish:</strong> "
                "<em>«Yo'laklar qurilgani <u>uchun</u> velosipedchilar soni "
                "ikki barobar oshdi.»</em> — qaydlar bu sababni "
                "aytmagan. Ular faqat ikki faktni yonma-yon "
                "qo'ygan.</p>")
            + "<p>To'g'ri birlashtirish: <em>«Shahar 2015-yilda yo'laklar "
            "qurdi, va o'sha yildan 2020 gacha velosipedchilar soni ikki "
            "barobar oshdi.»</em> — bog'lanish "
            "<u>vaqt bo'yicha</u>, sabab bo'yicha emas.</p>"
            + '<span class="sr-time">⏱ ~75 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch xil buzilish</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Buzilish</th><th>Belgisi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Sabab qo'shish</strong></td>"
              "<td><em>because · so · therefore · as a result</em> — qaydlar "
              "faqat ikki faktni bergan bo'lsa</td></tr>"
              "<tr><td><strong>Kuchaytirish</strong></td>"
              "<td><em>all · always · never · only · proves</em> — qaydda "
              "<em>some</em> yoki <em>often</em> turgan bo'lsa</td></tr>"
              "<tr><td><strong>Bog'lanishni ag'darish</strong></td>"
              "<td>Qaydda A → B, javobda B → A; yoki sabab boshqa narsaga "
              "ulangan</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Bu variantlar <u>eng ishonarli</u> ko'rinadi, chunki ular "
                "hikoyani <strong>tugal</strong> qiladi. Sabab qo'shilgan "
                "jumla yaxshiroq o'qiladi — va aynan shuning uchun "
                "xavfli. <mark>Qaydlar sizga ruxsat bermagan bog'lanishni "
                "yozmang.</mark>")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Peregrine falcons vanished from most European cities by the 1960s.",
                 "A pesticide widely used at the time thinned the shells of their eggs.",
                 "The pesticide was banned across most of Europe during the 1970s.",
                 "Peregrines began nesting on city buildings again from the 1990s.",
                 "City ledges resemble the cliff sites the birds use in the wild."],
                "The student wants to describe the return of the peregrine to cities and "
                "one reason cities suit it. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?")
            + choices_html([
                "Peregrines began nesting on city buildings again from the 1990s, "
                "because the pesticide that had thinned their eggshells was banned in "
                "the 1970s.",
                "Peregrines began nesting on city buildings again from the 1990s, and "
                "the ledges they use resemble the cliff sites they occupy in the wild.",
                "A pesticide widely used in the 1960s thinned peregrine eggshells and "
                "was banned across most of Europe in the 1970s.",
                "Peregrines vanished from most European cities by the 1960s and did not "
                "return until the 1990s.",
            ])
            + "<p><strong>Maqsad ikki qismli:</strong> (1) qaytishni "
            "tasvirlash; (2) <u>shaharlar nega mos kelishining</u> bitta "
            "sababi.</p>"
            + why([
                (True, "Peregrines began nesting on city buildings again from the 1990s, and the ledges they use resemble the cliff sites they occupy in the wild",
                 "ikkala talab: qaytish (1990-yillar) va shaharning mosligi "
                 "(peshtoqlar qoyalarga o'xshaydi). Va ikki qayd "
                 "<em>and</em> bilan bog'langan — qaydlar bergan darajada, "
                 "ortiqchasiz."),
                (False, "Peregrines began nesting on city buildings again from the 1990s, because the pesticide that had thinned their eggshells was banned in the 1970s",
                 "<strong>sabab qo'shilgan.</strong> Bu juda ishonarli va "
                 "ehtimol rost ham — lekin qaydlar taqiq bilan qaytishni "
                 "<u>bog'lamagan</u>, ular faqat ikki sanani bergan. Va "
                 "ustiga u maqsadning ikkinchi qismini (shahar nega mos "
                 "keladi) bajarmaydi."),
                (False, "Peregrines vanished from most European cities by the 1960s and did not return until the 1990s",
                 "qaytish bor, lekin shaharning mosligi yo'q — yarim "
                 "maqsad."),
                (False, "A pesticide widely used in the 1960s thinned peregrine eggshells and was banned across most of Europe in the 1970s",
                 "yo'qolish sababi haqida — maqsadning ikkala qismiga ham "
                 "tegmaydi."),
            ])
            + NOTE.format(
                "Diqqat: birinchi variant <u>dunyoda rost</u> bo'lishi "
                "mumkin — pestitsid taqiqi lochinlarning tiklanishida "
                "haqiqatan rol o'ynagan. Lekin savol dunyo haqida emas, "
                "<strong>qaydlar</strong> haqida. Qaydlar bu bog'lanishni "
                "bermagan.")
        )},

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Some fungi form networks that connect the roots of separate trees.",
                 "Sugars made by one tree have been detected days later in a "
                 "neighbouring one.",
                 "Seedlings in deep shade survive at higher rates than their own "
                 "photosynthesis would predict.",
                 "Whether the transfer benefits the donor tree is disputed.",
                 "Some researchers describe the transfer as leakage the fungus "
                 "mediates."],
                "The student wants to present a finding and note that its interpretation "
                "is contested. Which choice most effectively uses relevant information "
                "from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Sugars made by one tree have been detected days later in a neighbour, though whether the transfer benefits the donor is disputed.", "is_correct": True},
                {"text": "Because fungi connect the roots of separate trees, sugars are shared between them for the benefit of the whole woodland.", "is_correct": False},
                {"text": "Sugars made by one tree have been detected days later in a neighbouring tree.", "is_correct": False},
                {"text": "Some researchers describe the transfer of sugars as leakage that the fungus merely mediates.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad ikki qismli:</strong> topilma + uning "
                "talqini <u>bahsli</u> ekani.</p>"
                + why([
                    (True, "Sugars made by one tree have been detected days later in a neighbour, though whether the transfer benefits the donor is disputed",
                     "ikkala qism: topilma (shakar ko'chgan) va bahs "
                     "(<em>is disputed</em>). <em>though</em> ikkovini "
                     "to'g'ri bog'laydi."),
                    (False, "Because fungi connect the roots of separate trees, sugars are shared between them for the benefit of the whole woodland",
                     "<strong>ikki barobar buzilgan:</strong> sabab "
                     "qo'shilgan (<em>Because</em>) va da'vo kuchaytirilgan "
                     "(<em>for the benefit of the whole woodland</em>) — "
                     "qaydlar aynan buni <u>bahsli</u> deb aytadi. Eng "
                     "ishonarli va eng noto'g'ri variant."),
                    (False, "Sugars made by one tree have been detected days later in a neighbouring tree",
                     "topilma bor, bahs yo'q — yarim maqsad."),
                    (False, "Some researchers describe the transfer of sugars as leakage that the fungus merely mediates",
                     "bahsning bir tomoni, lekin topilmaning o'zi "
                     "keltirilmagan."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["A study followed 240 households that installed water meters.",
                 "Average consumption fell by 12 percent in the first year.",
                 "Consumption in the second year was 9 percent below the original level.",
                 "Households in the study volunteered to take part.",
                 "The researchers note that volunteers may differ from other "
                 "households."],
                "The student wants to report the study's result together with a "
                "limitation the researchers themselves raise. Which choice most "
                "effectively uses relevant information from the notes to accomplish this "
                "goal?"),
            "choices": [
                {"text": "Consumption fell by 12 percent in the first year and remained 9 percent below the original level in the second, though the households had volunteered and may differ from others.", "is_correct": True},
                {"text": "Water meters cut household consumption by 12 percent in the first year and 9 percent in the second.", "is_correct": False},
                {"text": "The study followed 240 households that had volunteered to install water meters.", "is_correct": False},
                {"text": "Because the households volunteered, the fall in consumption proves that water meters reduce demand.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad ikki qismli:</strong> natija + "
                "<u>tadqiqotchilarning o'zi aytgan</u> cheklov.</p>"
                + why([
                    (True, "Consumption fell by 12 percent in the first year and remained 9 percent below the original level in the second, though the households had volunteered and may differ from others",
                     "ikkala qism ham, va cheklov aynan qaydlardagi shaklda "
                     "(<em>may differ</em>) — kuchaytirilmagan."),
                    (False, "Because the households volunteered, the fall in consumption proves that water meters reduce demand",
                     "<strong>uchta buzilish birdan:</strong> sabab "
                     "ag'darilgan (ixtiyoriylik cheklov edi, dalil emas), "
                     "da'vo kuchaytirilgan (<em>proves</em>), va cheklov "
                     "quvvatga aylantirilgan. Mantiqan ham teskari."),
                    (False, "Water meters cut household consumption by 12 percent in the first year and 9 percent in the second",
                     "natija bor, cheklov yo'q — va ustiga sabab "
                     "qo'shilgan (<em>Water meters cut</em>), qaydlar esa "
                     "faqat pasayishni qayd etgan."),
                    (False, "The study followed 240 households that had volunteered to install water meters",
                     "usul haqida; natija ham, cheklovning ma'nosi ham "
                     "yo'q."),
                ])
                + TIP.format(
                    "Cheklovni keltirganda qaydlardagi <strong>ehtiyotkor "
                    "so'zlarni saqlang</strong>: <em>may · appears · is "
                    "disputed · thought to</em>. Ularni tashlab ketgan "
                    "variant qaydni kuchaytirgan bo'ladi.")
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Cuneiform was written by pressing a reed stylus into wet clay.",
                 "Tablets were often left to dry rather than fired.",
                 "Unfired tablets dissolve if they get wet.",
                 "Many surviving tablets were baked accidentally when a building burned "
                 "down.",
                 "The largest archives found so far come from sites destroyed by fire."],
                "The student wants to explain why so many surviving tablets come from "
                "destroyed sites. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Tablets were usually left unfired and dissolve if they get wet, so those that survive are largely ones a burning building happened to bake.", "is_correct": True},
                {"text": "The largest cuneiform archives found so far come from sites that were destroyed by fire.", "is_correct": False},
                {"text": "Cuneiform was written by pressing a reed stylus into wet clay, and the tablets were often left to dry rather than fired.", "is_correct": False},
                {"text": "Because scribes knew that fire preserved clay, important archives were deliberately baked before storage.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>explain <u>why</u></em> — "
                "sabab kerak, va u ikki qaydni bog'lashni talab "
                "qiladi: pishirilmagan lavhalar eriydi + yong'in ularni "
                "tasodifan pishirgan.</p>"
                + why([
                    (True, "Tablets were usually left unfired and dissolve if they get wet, so those that survive are largely ones a burning building happened to bake",
                     "ikki qaydni to'g'ri bog'laydi, va "
                     "<em>happened to</em> tasodifiylikni saqlaydi — qaydlar "
                     "aynan shunday aytgan."),
                    (False, "Because scribes knew that fire preserved clay, important archives were deliberately baked before storage",
                     "<strong>butunlay o'ylab topilgan:</strong> qaydlar "
                     "pishirish <u>tasodifiy</u> bo'lganini aytadi. Bu "
                     "variant niyat qo'shadi va bog'lanishni "
                     "ag'daradi."),
                    (False, "The largest cuneiform archives found so far come from sites that were destroyed by fire",
                     "<strong>bu tushuntiriladigan hodisaning o'zi</strong>, "
                     "tushuntirish emas. Savolni qaytarib beradi."),
                    (False, "Cuneiform was written by pressing a reed stylus into wet clay, and the tablets were often left to dry rather than fired",
                     "sababning yarmi — erish ham, yong'in ham yo'q."),
                ])
            ),
        },

        {
            "rich_text": notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["An icebreaker does not cut through ice with a sharp bow.",
                 "Its hull is shaped so that the bow rides up on top of the ice.",
                 "The ship\u2019s weight then breaks the ice from above.",
                 "The bow is rounded and heavily reinforced.",
                 "For this method the ship\u2019s displacement matters more than its "
                 "speed."],
                "The student wants to correct a common assumption about how icebreakers "
                "work. Which choice most effectively uses relevant information from the "
                "notes to accomplish this goal?"),
            "choices": [
                {"text": "An icebreaker does not cut through ice with a sharp bow: its rounded hull rides up onto the ice, and the ship\u2019s weight breaks the ice from above.", "is_correct": True},
                {"text": "Because an icebreaker\u2019s bow is rounded, it can travel faster through ice than a ship with a sharp bow can.", "is_correct": False},
                {"text": "The bow of an icebreaker is rounded and heavily reinforced.", "is_correct": False},
                {"text": "An icebreaker\u2019s displacement matters more than its speed when it is breaking ice.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> keng tarqalgan tasavvurni "
                "<u>tuzatish</u>. Demak javob noto\u2018g\u2018ri tasavvurni "
                "nomlashi <u>va</u> to\u2018g\u2018risini berishi kerak.</p>"
                + why([
                    (True, "An icebreaker does not cut through ice with a sharp bow: its rounded hull rides up onto the ice, and the ship\u2019s weight breaks the ice from above",
                     "ikkala qism: <em>does not cut … with a sharp bow</em> "
                     "(noto\u2018g\u2018ri tasavvur) va mexanizm (ustiga chiqadi, "
                     "og\u2018irligi sindiradi)."),
                    (False, "Because an icebreaker\u2019s bow is rounded, it can travel faster through ice than a ship with a sharp bow can",
                     "<strong>sabab qo\u2018shilgan va qaydga zid:</strong> "
                     "qaydlar tezlik haqida aynan aksini aytadi "
                     "(<em>displacement matters more than speed</em>). "
                     "Jumla ishonarli o\u2018qiladi \u2014 va shuning uchun "
                     "xavfli."),
                    (False, "The bow of an icebreaker is rounded and heavily reinforced",
                     "rost fakt, lekin hech qanday tasavvurni tuzatmaydi \u2014 "
                     "u nima <u>noto\u2018g\u2018ri</u> ekanini aytmaydi."),
                    (False, "An icebreaker\u2019s displacement matters more than its speed when it is breaking ice",
                     "rost va hatto qiziqarli, lekin bu mexanizmning "
                     "oqibati \u2014 tuzatilayotgan tasavvurning o\u2018zi emas."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to distort a source</div><div class="pp-card-back">manbani buzib ko\'rsatmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">is disputed</div><div class="pp-card-back">bahsli (ehtiyotkor so\'z — saqlang)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to mediate</div><div class="pp-card-back">vositachilik qilmoq, o\'tkazmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a limitation</div><div class="pp-card-back">cheklov, kamchilik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to volunteer (for a study)</div><div class="pp-card-back">(tadqiqotga) ixtiyoriy qatnashmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ledge</div><div class="pp-card-back">peshtoq, tor javon (binoda yoki qoyada)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a stylus</div><div class="pp-card-back">yozuv tayoqchasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to happen to ~</div><div class="pp-card-back">tasodifan ~ bo\'lib qolmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Ikki qaydni bog'laganda <strong>qaydlar bermagan "
              "narsani qo'shmang</strong>.</li>"
              "<li>Uch buzilish: <strong>sabab qo'shish · kuchaytirish · "
              "bog'lanishni ag'darish</strong>.</li>"
              "<li><em>because · so · proves · all · always</em> — "
              "ogohlantirish belgilari.</li>"
              "<li>Qaydlardagi <u>ehtiyotkor so'zlarni saqlang</u>: "
              "<em>may · thought to · is disputed</em>.</li>"
              "<li>Sabab qo'shilgan jumla <u>yaxshiroq o'qiladi</u> — "
              "aynan shuning uchun xavfli.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 25
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_SYNTH,
    "title": "SAT R&W W25: Rhetorical Synthesis — Mixed Practice",
    "summary": "Oltita savol, barcha maqsad oilalari va tuzoq turlari aralash, "
               "imtihon tezligida: 20–24-darslarni mustahkamlash.",
    "order": 25,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol. Maqsad oilalari aralash, va tuzoqlar ham: "
            "off-goal, yarim maqsad, buzilgan birlashtirish.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 8px;\"><strong>Har savolda shu "
                "tartib:</strong></p>"
                "<ol style=\"margin:0;\">"
                "<li><strong>Maqsadni birinchi o'qing</strong> va talablarni "
                "sanang (21-dars).</li>"
                "<li>Qaydlarni <u>bir marta</u> o'qing.</li>"
                "<li>Variantlarni maqsadga solishtiring — "
                "<u>qaydlarga qaytmang</u> (23-dars).</li>"
                "<li>Qo'shilib qolgan sabab yoki kuchaytirishni tekshiring "
                "(24-dars).</li>"
                "</ol>")
            + "<p>Taymer: <strong>7 daqiqa</strong> (6 × 70 soniya).</p>"
            + '<span class="sr-time">⏱ 6 savol · 7 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Damascus steel blades were made from a crucible steel imported from "
                 "South Asia.",
                 "Their surfaces show a banded pattern that reappears after "
                 "sharpening.",
                 "The pattern comes from bands of carbide within the metal itself.",
                 "The technique was lost by about 1800.",
                 "Modern reproductions match the pattern but not the original alloy."],
                "The student wants to explain why the pattern survives sharpening. Which "
                "choice most effectively uses relevant information from the notes to "
                "accomplish this goal?"),
            "choices": [
                {"text": "The banded pattern reappears after sharpening because it comes from bands of carbide running through the metal itself, not from the surface.", "is_correct": True},
                {"text": "Damascus steel blades were made from a crucible steel imported from South Asia.", "is_correct": False},
                {"text": "The technique for making Damascus steel was lost by about 1800.", "is_correct": False},
                {"text": "Modern reproductions match the banded pattern but not the original alloy.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <em>explain <u>why</u> the "
                "pattern survives sharpening</em> — sabab kerak.</p>"
                + why([
                    (True, "The banded pattern reappears after sharpening because it comes from bands of carbide running through the metal itself, not from the surface",
                     "hodisa + sabab. <em>not from the surface</em> "
                     "qo'shimchasi sababni yanada aniq qiladi."),
                    (False, "Modern reproductions match the banded pattern but not the original alloy",
                     "<strong>off-goal:</strong> bugungi nusxalar haqida, "
                     "naqshning saqlanishi haqida emas."),
                    (False, "Damascus steel blades were made from a crucible steel imported from South Asia",
                     "kelib chiqishi — sabab emas."),
                    (False, "The technique for making Damascus steel was lost by about 1800",
                     "tarixiy fakt, savolga aloqasiz."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["A community orchard is land planted with fruit trees and managed "
                 "collectively.",
                 "Members share the work of pruning and picking.",
                 "One orchard in a northern city has 60 registered members.",
                 "Its trees produced 1.4 tonnes of apples last season.",
                 "Most of the fruit was given away rather than sold."],
                "The student wants to introduce community orchards to an audience "
                "unfamiliar with them. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "A community orchard is a piece of land planted with fruit trees and managed collectively, its members sharing the work of pruning and picking.", "is_correct": True},
                {"text": "One community orchard in a northern city has 60 registered members and produced 1.4 tonnes of apples last season.", "is_correct": False},
                {"text": "Most of the fruit grown by one community orchard was given away rather than sold.", "is_correct": False},
                {"text": "Members of a community orchard share the work of pruning and picking the trees.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> tanishtirish oilasi — "
                "<em>unfamiliar with them</em>. Ta'rif shart.</p>"
                + why([
                    (True, "A community orchard is a piece of land planted with fruit trees and managed collectively, its members sharing the work of pruning and picking",
                     "«X — bu …» shakli, va u ikkala asosiy qaydni "
                     "birlashtiradi."),
                    (False, "One community orchard in a northern city has 60 registered members and produced 1.4 tonnes of apples last season",
                     "<strong>eng jozibali:</strong> aniq raqamlar. Lekin "
                     "notanish o'quvchi bu jumladan «jamoa bog'i» nima "
                     "ekanini bilmaydi."),
                    (False, "Members of a community orchard share the work of pruning and picking the trees",
                     "ta'rifning yarmi — nima ekani aytilmagan."),
                    (False, "Most of the fruit grown by one community orchard was given away rather than sold",
                     "bitta tafsilot, ta'rif emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["A city introduced a deposit on drink containers in 2019.",
                 "Containers returned rose from 34 percent to 88 percent within two "
                 "years.",
                 "Litter counts on the city's streets fell over the same period.",
                 "A neighbouring city with no deposit recorded a similar fall in "
                 "litter.",
                 "Researchers say the litter figures cannot be attributed to the deposit "
                 "alone."],
                "The student wants to report the scheme's clearest result while noting "
                "what it cannot be credited with. Which choice most effectively uses "
                "relevant information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Container returns rose from 34 percent to 88 percent within two years, though the fall in street litter cannot be credited to the deposit alone.", "is_correct": True},
                {"text": "Because the city introduced a deposit in 2019, both container returns and street litter improved markedly.", "is_correct": False},
                {"text": "Container returns rose from 34 percent to 88 percent within two years of the deposit's introduction.", "is_correct": False},
                {"text": "A neighbouring city with no deposit scheme recorded a similar fall in street litter.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad ikki qismli:</strong> eng aniq natija + "
                "<u>nimaga bog'lab bo'lmasligi</u>.</p>"
                + why([
                    (True, "Container returns rose from 34 percent to 88 percent within two years, though the fall in street litter cannot be credited to the deposit alone",
                     "ikkala qism: aniq natija (34% → 88%) va cheklov "
                     "(<em>cannot be credited … alone</em>), va u qaydlarning "
                     "ehtiyotkorligini saqlaydi."),
                    (False, "Because the city introduced a deposit in 2019, both container returns and street litter improved markedly",
                     "<strong>buzilgan birlashtirish</strong> (24-dars): "
                     "sabab qo'shilgan va u qaydlar aynan rad etgan "
                     "narsaga ulangan — chiqindi kamayishi."),
                    (False, "Container returns rose from 34 percent to 88 percent within two years of the deposit's introduction",
                     "natija bor, cheklov yo'q — yarim maqsad."),
                    (False, "A neighbouring city with no deposit scheme recorded a similar fall in street litter",
                     "cheklovning dalili, lekin sxemaning natijasi "
                     "keltirilmagan."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Cochineal is a red dye made from an insect that lives on cactus pads.",
                 "It takes roughly 70,000 insects to produce one kilogram of dye.",
                 "It was among the most valuable exports from the Americas after "
                 "silver.",
                 "Synthetic red dyes replaced it for most uses after the 1870s.",
                 "It is still used where a natural colourant is required."],
                "The student wants to emphasise how labour-intensive the dye is to "
                "produce. Which choice most effectively uses relevant information from "
                "the notes to accomplish this goal?"),
            "choices": [
                {"text": "Producing a single kilogram of cochineal takes roughly 70,000 insects.", "is_correct": True},
                {"text": "Cochineal was among the most valuable exports from the Americas after silver.", "is_correct": False},
                {"text": "Cochineal is a red dye obtained from an insect that lives on cactus pads.", "is_correct": False},
                {"text": "Synthetic red dyes replaced cochineal for most uses after the 1870s.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> ta'kidlash — <em>how "
                "labour-intensive</em>. Miqdor kerak.</p>"
                + why([
                    (True, "Producing a single kilogram of cochineal takes roughly 70,000 insects",
                     "yagona variant mehnat hajmini o'lchaydi, va 70,000 "
                     "raqami uni his qildiradi."),
                    (False, "Cochineal was among the most valuable exports from the Americas after silver",
                     "<strong>off-goal:</strong> qiymat — mehnat emas. "
                     "Qimmatlik mehnatdan kelib chiqqan bo'lishi mumkin, "
                     "lekin maqsad mehnatni ta'kidlashni so'raydi."),
                    (False, "Cochineal is a red dye obtained from an insect that lives on cactus pads",
                     "ta'rif — boshqa oila."),
                    (False, "Synthetic red dyes replaced cochineal for most uses after the 1870s",
                     "tarix; mehnat haqida hech nima."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Terracing cuts a hillside into level steps for planting.",
                 "Contour ploughing follows the natural curve of the slope without "
                 "cutting steps.",
                 "Terracing holds soil best on steep ground.",
                 "Contour ploughing costs far less to establish.",
                 "Both reduce the amount of soil washed downhill in heavy rain."],
                "The student wants to present a similarity between the two techniques to "
                "an audience already familiar with both. Which choice most effectively "
                "uses relevant information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Terracing and contour ploughing both reduce the amount of soil washed downhill in heavy rain.", "is_correct": True},
                {"text": "Terracing cuts a hillside into level steps, while contour ploughing follows the natural curve of the slope.", "is_correct": False},
                {"text": "Terracing holds soil best on steep ground, whereas contour ploughing costs far less to establish.", "is_correct": False},
                {"text": "Contour ploughing costs far less to establish than terracing does.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki talab:</strong> (1) <u>o'xshashlik</u> "
                "(farq emas); (2) <em>already familiar</em> — ta'rif "
                "ortiqcha.</p>"
                + why([
                    (True, "Terracing and contour ploughing both reduce the amount of soil washed downhill in heavy rain",
                     "ikkovi nomlangan, umumiy jihat aytilgan, va ta'rifga "
                     "vaqt sarflanmagan."),
                    (False, "Terracing holds soil best on steep ground, whereas contour ploughing costs far less to establish",
                     "<strong>bu farq</strong>, o'xshashlik emas — "
                     "<em>whereas</em> buni ochiq ko'rsatadi."),
                    (False, "Terracing cuts a hillside into level steps, while contour ploughing follows the natural curve of the slope",
                     "ikki ta'rif — va o'quvchi ikkovini biladi. "
                     "Ustiga bu ham farq."),
                    (False, "Contour ploughing costs far less to establish than terracing does",
                     "yana farq, va faqat bir tomondan."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Rhetorical Synthesis") + notes_q(
                "While researching a topic, a student has taken the following notes:",
                ["Beavers build dams that flood the ground behind them.",
                 "The flooded ground holds water through a dry summer.",
                 "Streams with beaver dams keep flowing in droughts that dry out "
                 "neighbouring streams.",
                 "The dams also raise the water level in nearby wells.",
                 "Landowners have historically removed beavers to protect farmland from "
                 "flooding."],
                "The student wants to present a benefit of beaver dams and acknowledge "
                "why they have been removed. Which choice most effectively uses relevant "
                "information from the notes to accomplish this goal?"),
            "choices": [
                {"text": "Streams with beaver dams keep flowing through droughts that dry neighbouring streams, though landowners have historically removed beavers to protect farmland from flooding.", "is_correct": True},
                {"text": "Beaver dams flood the ground behind them, and the flooded ground holds water through a dry summer.", "is_correct": False},
                {"text": "Because beaver dams raise the water level in nearby wells, landowners have historically removed them.", "is_correct": False},
                {"text": "Landowners have historically removed beavers in order to protect their farmland from flooding.", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ikki talab:</strong> foyda + olib tashlanish "
                "sababi. Ikkovi ham bo'lishi shart.</p>"
                + why([
                    (True, "Streams with beaver dams keep flowing through droughts that dry neighbouring streams, though landowners have historically removed beavers to protect farmland from flooding",
                     "ikkala qism, va <em>though</em> ularni to'g'ri "
                     "qarama-qarshi qo'yadi."),
                    (False, "Because beaver dams raise the water level in nearby wells, landowners have historically removed them",
                     "<strong>bog'lanish ag'darilgan</strong> (24-dars): "
                     "qaydlarga ko'ra olib tashlash sababi "
                     "<u>ekin maydonlarining suv bosishi</u>, quduq "
                     "sathining ko'tarilishi emas — va quduq sathi bu "
                     "yerda foyda edi."),
                    (False, "Beaver dams flood the ground behind them, and the flooded ground holds water through a dry summer",
                     "faqat foyda — olib tashlanish yo'q."),
                    (False, "Landowners have historically removed beavers in order to protect their farmland from flooding",
                     "faqat ikkinchi qism — foyda yo'q."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Qaysi darsga qaytish</th></tr></thead>"
              "<tbody>"
              "<tr><td>Rost, lekin maqsaddan chetda</td><td>23-dars</td></tr>"
              "<tr><td>Ikki talabdan bittasini bajardim</td><td>21-dars — "
              "talablarni sanang</td></tr>"
              "<tr><td>Ta'rif so'ralmaganda ta'rif tanladim</td>"
              "<td>21-dars — <em>already familiar</em></td></tr>"
              "<tr><td>Solishtirishda bitta narsani tanladim</td>"
              "<td>22-dars — ikkovi ham jumlada</td></tr>"
              "<tr><td>Qo'shilib qolgan sababni sezmadim</td><td>24-dars — "
              "<em>because · proves</em></td></tr>"
              "<tr><td>O'xshashlik so'ralganda farq tanladim</td>"
              "<td>22-dars — maqsaddagi otga qarang</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu turda vaqt yo'qotishning bitta sababi bor: "
                "<strong>qaydlarga qayta-qayta qaytish</strong>. Qaydlarni "
                "bir marta o'qing, keyin faqat maqsad bilan variantlar "
                "orasida ishlang. 70 soniyadan oshsa — deyarli har doim "
                "shu.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to be credited with ~</div><div class="pp-card-back">~ ning hisobiga yozilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">labour-intensive</div><div class="pp-card-back">ko\'p mehnat talab qiladigan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a deposit (on containers)</div><div class="pp-card-back">(idish uchun) qaytariladigan garov puli</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a crucible</div><div class="pp-card-back">tigel (metall eritiladigan idish)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">terracing</div><div class="pp-card-back">qiyalikni zinapoyalarga bo\'lish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">contour ploughing</div><div class="pp-card-back">nishab bo\'ylab haydash</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a colourant</div><div class="pp-card-back">bo\'yoq moddasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to acknowledge</div><div class="pp-card-back">tan olmoq, e\'tirof etmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa — Rhetorical Synthesis mavzusi yakuni</h3>"
            + "<ul>"
              "<li>To'rtala variant ham rost: <strong>maqsad yagona "
              "mezon</strong> (20-dars).</li>"
              "<li>Maqsadni shartnoma kabi o'qing va talablarni "
              "<u>sanang</u> (21-dars).</li>"
              "<li>Uch oila: tanishtirish · ta'kidlash · solishtirish "
              "(22-dars).</li>"
              "<li>Ko'zingiz variant ↔ maqsad orasida yursin, qaydlar bilan "
              "emas (23-dars).</li>"
              "<li>Birlashtirganda <strong>sabab qo'shmang</strong> va "
              "ehtiyotkor so'zlarni saqlang (24-dars).</li>"
              "</ul>"
        )},
    ],
},

]
