# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 40-46.

"Tinish belgilari (Boundaries — punctuation within the sentence)" — the second
half of the Boundaries skill. W30-W35 asked where one sentence ends; this asks
how the inside of a sentence is punctuated: colons, dashes, supplements, and the
commas that must NOT be there.

The two-sentence test from W30 still does most of the work, and two new rules
join it: a colon or single dash needs a complete sentence in front of it, and a
supplement must be removable and must open and close with the SAME mark.

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

TOPIC_PUNCT = {
    "title":   "Tinish belgilari (Boundaries — punctuation within the sentence)",
    "summary": "Gap ichidagi belgilar: ikki nuqta, tire, qavs va qo'shimcha "
               "bo'laklarni ajratuvchi vergullar — hamda qo'yilmasligi kerak "
               "bo'lgan vergullar.",
    "icon":    "bi-three-dots",
    "order":   5,
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
# Writing 40
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W40: The Colon — One Rule, Always the Same",
    "summary": "Ikki nuqtaning yagona qoidasi: undan OLDIN to'liq gap turishi shart. "
               "Undan keyin nima kelishi muhim emas.",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Bitta qoida, istisnosiz</h2>"
            "<p>Ikki nuqta (<strong>:</strong>) imtihonda muntazam sinaladi, "
            "va uning qoidasi shu qadar oddiyki, uni bilgan o'quvchi bu "
            "savollarni <mark>o'n soniyada</mark> yechadi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Ikki nuqtadan "
                "OLDIN to'liq gap turishi shart. Undan KEYIN nima kelishi "
                "muhim emas.</strong></p>")
            + "<p>Keyin ro'yxat kelishi mumkin, bitta so'z, ot birikmasi, "
            "yoki butun boshqa gap — hammasi mumkin. Tekshirish faqat "
            "<u>chap tomonda</u>.</p>"
            + '<span class="sr-time">⏱ ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Chap tomonni tekshirish</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Namuna</th><th>Chap tomon</th><th>Ikki nuqta "
              "mumkinmi?</th></tr></thead>"
              "<tbody>"
              "<tr><td><em>The kit contains three tools:</em></td>"
              "<td>to'liq gap ✓</td><td><strong>ha</strong></td></tr>"
              "<tr><td><em>The kit contains:</em></td>"
              "<td>ega + kesim bor, lekin <em>contains</em> to'ldiruvchi "
              "kutyapti — gap tugamagan</td><td><strong>yo'q</strong></td></tr>"
              "<tr><td><em>The kit includes tools such as:</em></td>"
              "<td><em>such as</em> dan keyin ro'yxat kutiladi</td>"
              "<td><strong>yo'q</strong></td></tr>"
              "<tr><td><em>The kit is made up of:</em></td>"
              "<td>predlog bilan tugagan</td><td><strong>yo'q</strong></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "Uchta doimiy tuzoq: ikki nuqta <strong>fe'ldan keyin</strong> "
                "(<em>contains:</em>), <strong>predlogdan keyin</strong> "
                "(<em>of:</em>), va <strong><em>such as</em> / "
                "<em>including</em> / <em>for example</em> dan keyin</strong>. "
                "Uchalasida ham chap tomon gap emas — ikki nuqta "
                "taqiqlangan.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>A traditional Uzbek suzani is worked by several hands at once, and "
                "the division of labour is fixed by long custom. The pattern is drawn in "
                "ink by one woman, the panels are embroidered separately by "
                "<span class=\"sr-blank\"></span> and the finished cloth is assembled by "
                "a third.</p>")
            + choices_html([
                "others:",
                "others,",
                "others;",
                "others",
            ])
            + "<p><strong>Diqqat:</strong> bu ikki nuqta savoli emas — u "
            "shunday <u>ko'rinadi</u>, chunki variantlar orasida ikki "
            "nuqta bor. Chap tomonni tekshiramiz: <em>The pattern is drawn "
            "… the panels are embroidered separately by others</em> — "
            "to'liq gap. Demak ikki nuqta "
            "<u>mumkin</u>.</p>"
            "<p>Lekin o'ng tomonga qarang: <em>and the finished cloth is "
            "assembled by a third</em> — <em>and</em> bilan boshlangan "
            "uchinchi bo'lak. Bu <mark>uch a'zoli ro'yxat</mark>ning "
            "oxirgi a'zosi.</p>"
            + why([
                (True, "others,",
                 "uch a'zoli ro'yxat vergul bilan ajratiladi: "
                 "<em>The pattern is drawn…, the panels are embroidered…, "
                 "and the finished cloth is assembled…</em>. Bu yerda "
                 "vergullar mustaqil gaplarni emas, ro'yxat a'zolarini "
                 "ajratyapti — va <em>and</em> uchinchisini ulaydi."),
                (False, "others:",
                 "chap tomon to'liq gap, ya'ni ikki nuqta grammatik "
                 "jihatdan mumkin — lekin ikki nuqta "
                 "<u>e'lon qiladi</u>, va bu yerda e'lon qilinadigan hech "
                 "nima yo'q: uchinchi bo'lak ro'yxatning davomi, izoh "
                 "emas."),
                (False, "others;",
                 "nuqtali vergul ro'yxat a'zolarini ajratish uchun faqat "
                 "a'zolar ichida vergul bo'lganda ishlatiladi. Bu yerda "
                 "unday emas — va u <em>and</em> bilan birga "
                 "kelmaydi."),
                (False, "others",
                 "belgisiz uch a'zoli ro'yxat qo'shilib ketadi."),
            ])
            + NOTE.format(
                "Bu savol bir narsani ko'rsatadi: <strong>chap tomon "
                "to'liq bo'lishi ikki nuqtani <u>mumkin</u> qiladi, "
                "lekin <u>to'g'ri</u> qilmaydi.</strong> Qoida shartni "
                "beradi, ma'no esa tanlaydi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Every part of a qanat is shaped by one constraint above all "
                "<span class=\"sr-blank\"></span> the water has to move without a pump, "
                "so the channel may fall only a few centimetres in a kilometre.</p>"),
            "choices": [
                {"text": ":", "is_correct": True},
                {"text": ",", "is_correct": False},
                {"text": ";", "is_correct": False},
                {"text": " and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>Every part of a qanat is "
                "shaped by one constraint above all</em> — to'liq gap ✓. "
                "Ikki nuqta mumkin.</p>"
                "<p>Va ma'no ham talab qiladi: <em>one constraint</em> "
                "<mark>e'lon qilyapti</mark> — «qaysi cheklov?» Ikki nuqta "
                "javob beradi.</p>"
                + why([
                    (True, ":",
                     "chap tomon to'liq, va o'ng tomon e'lon qilingan "
                     "narsani ochadi. Ikki nuqtaning aynan vazifasi."),
                    (False, ",",
                     "o'ng tomon mustaqil gap (<em>the water has to "
                     "move…</em>), demak bu <strong>vergul splaysi</strong> "
                     "(W31)."),
                    (False, ";",
                     "nuqtali vergul grammatik jihatdan mumkin — ikkala "
                     "tomon ham mustaqil. Lekin u ikki fikrni "
                     "<u>tenglashtiradi</u>; bu yerda ikkinchisi "
                     "birinchisini <u>izohlaydi</u>, va ikki nuqta "
                     "buni ko'rsatadi."),
                    (False, " and",
                     "vergulsiz <em>and</em> ikki mustaqil gapni ulay "
                     "olmaydi, va u izoh munosabatini ham "
                     "ko'rsatmaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The instrument case supplied with the survey theodolite contained "
                "<span class=\"sr-blank\"></span> a plumb bob, two spare levelling "
                "screws, a brass sunshade and a folded canvas cover for the "
                "tripod.</p>"),
            "choices": [
                {"text": "", "is_correct": True},
                {"text": ":", "is_correct": False},
                {"text": ";", "is_correct": False},
                {"text": ", including:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>The instrument case "
                "supplied with the survey theodolite contained</em> — "
                "<mark>to'liq gap emas</mark>. <em>contained</em> "
                "to'ldiruvchi kutyapti: nimani saqlagan? Gap "
                "tugamagan.</p>"
                "<p>Demak ikki nuqta ham, nuqtali vergul ham "
                "<u>taqiqlangan</u>. Ro'yxat fe'lga to'g'ridan-to'g'ri "
                "ulanadi.</p>"
                + why([
                    (True, "",
                     "belgisiz: <em>contained a plumb bob, two spare "
                     "levelling screws…</em> — fe'l va uning to'ldiruvchisi "
                     "orasiga hech qanday belgi qo'yilmaydi."),
                    (False, ":",
                     "<strong>fe'ldan keyin ikki nuqta</strong> — bu "
                     "darsning bosh tuzog'i. Ro'yxat kelayotgani ikki "
                     "nuqtani oqlamaydi; chap tomon to'liq gap "
                     "bo'lishi shart."),
                    (False, ";",
                     "nuqtali vergul ikki mustaqil gap orasida "
                     "bo'ladi."),
                    (False, ", including:",
                     "ikki xato birga: <em>including</em> dan keyin ikki "
                     "nuqta qo'yilmaydi, va <em>contained … including</em> "
                     "ortiqcha takror."),
                ])
                + TIP.format(
                    "Tez tekshiruv: bo'sh joyni yopib, chap tomonni "
                    "o'qing va <u>nuqta qo'ying</u>. "
                    "«<em>The instrument case contained.</em>» — bu gapmi? "
                    "Yo'q. Demak ikki nuqta mumkin emas. Bir soniya, "
                    "va uchta variant tushadi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Lacquer hardens by taking moisture from the air rather than by "
                "drying out, and a workshop in a dry climate has to add water to the "
                "room. The craft therefore travelled badly for centuries, and it took "
                "hold in only a few places outside its "
                "<span class=\"sr-blank\"></span> Kyoto, Wajima and a handful of towns "
                "along the same wet coast.</p>"),
            "choices": [
                {"text": "homeland:", "is_correct": True},
                {"text": "homeland,", "is_correct": False},
                {"text": "homeland; such as", "is_correct": False},
                {"text": "homeland such as:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>…it took hold in only a "
                "few places outside its homeland</em> — to'liq gap ✓.</p>"
                "<p><strong>O'ng tomon:</strong> uch joy nomi — "
                "<mark>ro'yxat</mark>. Chap to'liq + ro'yxat e'lon "
                "qilinyapti = ikki nuqta.</p>"
                + why([
                    (True, "homeland:",
                     "to'liq gapdan keyin ro'yxatni e'lon qiladi — ikki "
                     "nuqtaning asosiy vazifasi."),
                    (False, "homeland such as:",
                     "<strong><em>such as</em> dan keyin ikki nuqta hech "
                     "qachon qo'yilmaydi.</strong> <em>such as</em> "
                     "o'zi ro'yxatni kiritadi; ikkinchi kirituvchi "
                     "ortiqcha."),
                    (False, "homeland; such as",
                     "nuqtali vergul mustaqil gap talab qiladi, "
                     "<em>such as Kyoto…</em> esa gap emas."),
                    (False, "homeland,",
                     "vergul grammatik jihatdan halokatli emas, lekin "
                     "ro'yxat ichida allaqachon vergullar bor va u "
                     "ro'yxatni <u>e'lon qilmaydi</u> — bu yerda ikki "
                     "nuqta aniqroq."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The tuning of a Javanese gamelan is set for the individual orchestra "
                "rather than to any external standard, and instruments from two "
                "different sets cannot usually be played "
                "<span class=\"sr-blank\"></span> each instrument is tuned to its own "
                "companions and to nothing outside them.</p>"),
            "choices": [
                {"text": "together:", "is_correct": True},
                {"text": "together, and", "is_correct": False},
                {"text": "together, such as", "is_correct": False},
                {"text": "together", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>…instruments from two "
                "different sets cannot usually be played together</em> — "
                "to'liq gap ✓.</p>"
                "<p><strong>O'ng tomon:</strong> <em>each instrument is tuned "
                "to its own companions…</em> — mustaqil gap, va u chap "
                "tomonning <mark>sababini beradi</mark>. Ikki nuqta izoh "
                "uchun ham ishlaydi (W32).</p>"
                + why([
                    (True, "together:",
                     "chap to'liq, va o'ng tomon uni izohlaydi — «nega "
                     "birga chalinmaydi?» Ikki nuqta shu javobni e'lon "
                     "qiladi."),
                    (False, "together, and",
                     "grammatik jihatdan to'g'ri (vergul + FANBOYS), lekin "
                     "<em>and</em> shunchaki qo'shadi — u ikkinchi gapning "
                     "<u>sabab</u> ekanini ko'rsatmaydi. Ikki nuqta "
                     "aniqroq."),
                    (False, "together, such as",
                     "<em>such as</em> dan keyin ro'yxat kutiladi, gap "
                     "emas."),
                    (False, "together",
                     "belgisiz — ikki mustaqil gap qo'shilib ketadi "
                     "(<em>run-on</em>)."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a colon ( : )</div><div class="pp-card-back">ikki nuqta — oldidan to\'liq gap shart</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to announce a list</div><div class="pp-card-back">ro\'yxatni e\'lon qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">such as / including</div><div class="pp-card-back">masalan, jumladan (o\'zi ro\'yxat kiritadi — ikki nuqta kerak emas)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an object (of a verb)</div><div class="pp-card-back">to\'ldiruvchi (fe\'ldan keyin belgi qo\'yilmaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a plumb bob</div><div class="pp-card-back">shovun (tik chiziq uchun og\'irlik)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a theodolite</div><div class="pp-card-back">teodolit (burchak o\'lchash asbobi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to take hold</div><div class="pp-card-back">ildiz otmoq, o\'rnashmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a gamelan</div><div class="pp-card-back">gamelan (Yava an\'anaviy orkestri)</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Ikki nuqtadan oldin to'liq gap.</strong> Undan "
              "keyin — nima bo'lsa ham mayli.</li>"
              "<li>Tez tekshiruv: chap tomonga <u>nuqta qo'ying</u> — gap "
              "chiqadimi?</li>"
              "<li>Uch tuzoq: fe'ldan keyin · predlogdan keyin · "
              "<em>such as</em> dan keyin.</li>"
              "<li>Chap tomon to'liq bo'lishi ikki nuqtani "
              "<u>mumkin</u> qiladi, <u>to'g'ri</u> emas — ma'no "
              "tanlaydi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 41
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W41: The Dash — A Louder Comma, and the Pair Rule",
    "summary": "Yolg'iz tire ikki nuqta kabi ishlaydi; juft tire esa qo'shimcha "
               "bo'lakni qavsga oladi. Ikkovining qoidasi boshqa.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>Tire ikki xil ishlaydi</h2>"
            "<p>Tire (<strong>—</strong>) imtihonda ikki xil vazifada "
            "keladi, va ular <mark>butunlay boshqa qoidalarga</mark> "
            "bo'ysunadi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Vazifa</th><th>Shakli</th><th>Qoidasi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Yolg'iz tire</strong></td>"
              "<td><em>… anvil — twenty minutes of work.</em></td>"
              "<td>Ikki nuqta kabi: <u>oldidan to'liq gap</u></td></tr>"
              "<tr><td><strong>Juft tire</strong></td>"
              "<td><em>The dome — rebuilt twice — still stands.</em></td>"
              "<td>Qo'shimcha bo'lakni ikki tomondan o'raydi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0;\">Yolg'iz tire va ikki nuqta "
                "<u>deyarli</u> bir xil ishlaydi. Farqi ohangda: ikki "
                "nuqta rasmiy va e'lon qiladi, tire "
                "<strong>keskinroq</strong> va kutilmaganroq. Grammatik "
                "jihatdan ikkovi ham chapdan to'liq gap talab "
                "qiladi.</p>")
            + '<span class="sr-time">⏱ ~30 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Muhim natija</h3>"
            "<p>Yolg'iz tire va ikki nuqta bir xil ishlaganidan "
            "<mark>W15'dagi sinonim qoidasi</mark> kelib chiqadi: agar "
            "variantlar orasida <u>ikkovi ham</u> bo'lsa va ikkovi ham "
            "grammatik jihatdan to'g'ri bo'lsa — "
            "<strong>ikkovi ham javob emas</strong>.</p>"
            + TIP.format(
                "Demak tire ko'rgan zahotingizda birinchi savol: "
                "<strong>bu yolg'iz tiremi yoki juftning bir "
                "yarmimi?</strong> Gapning boshqa joyida ikkinchi tire "
                "bormi? Bor bo'lsa — bu juft, va qoida butunlay "
                "boshqa (42 va 43-darslar).")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The dye works kept its recipes in a book that nobody outside the "
                "family was allowed to open, and the last of the family died in 1948 "
                "without an apprentice. What was lost was not a colour but a "
                "<span class=\"sr-blank\"></span> the exact order in which eight "
                "ordinary substances had to be added.</p>")
            + choices_html([
                "method —",
                "method,",
                "method;",
                "method — the",
            ])
            + "<p><strong>Chap tomon:</strong> <em>What was lost was not a "
            "colour but a method</em> — to'liq gap ✓. "
            "<strong>O'ng tomon:</strong> <em>the exact order in which eight "
            "ordinary substances had to be added</em> — "
            "<mark>ot birikmasi</mark>, gap emas.</p>"
            "<p>To'liq gap + bo'lak → vergul, ikki nuqta yoki tire. Va "
            "o'ng tomon chapni <u>aniqlashtiryapti</u> — «qaysi usul?»</p>"
            + why([
                (True, "method —",
                 "yolg'iz tire: chapdan to'liq gap bor, va u kutilmagan "
                 "aniqlashtirishni keskin kiritadi. Ikki nuqta ham "
                 "to'g'ri bo'lardi, lekin variantlar orasida yo'q."),
                (False, "method;",
                 "nuqtali vergul <u>ikki mustaqil gap</u> orasida "
                 "bo'ladi. O'ng tomon gap emas."),
                (False, "method — the",
                 "tire bor, lekin <em>the</em> ikki marta chiqadi: "
                 "<em>— the the exact order</em>. Variantni gapga qo'yib "
                 "o'qish bu xatoni darrov ochadi."),
                (False, "method,",
                 "vergul grammatik jihatdan mumkin, lekin gapda "
                 "allaqachon <em>not a colour but a method</em> qarshi "
                 "qo'yish bor — tire aniqlashtirishni ajratib "
                 "ko'rsatadi. SAT bu yerda tireni tanlaydi."),
            ])
            + NOTE.format(
                "Uchinchi variantga e'tibor bering: xato belgida emas, "
                "<u>takrorlangan so'zda</u>. Conventions savolida "
                "variantni har doim <strong>gapga qo'yib o'qing</strong> — "
                "ba'zi tuzoqlar faqat shunda ko'rinadi.")
        )},

        {
            "rich_text": conv_q(
                "<p>The bridge carries a single track and was built for locomotives a "
                "third the weight of today's, and the engineers who inspect it each "
                "spring look first at one thing "
                "<span class=\"sr-blank\"></span> the six wrought-iron ties that hold "
                "the deck to the arch.</p>"),
            "choices": [
                {"text": "—", "is_correct": True},
                {"text": ",", "is_correct": False},
                {"text": ";", "is_correct": False},
                {"text": " and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>…look first at one "
                "thing</em> — to'liq gap ✓, va u <em>one thing</em> deb "
                "<mark>e'lon qilyapti</mark>.</p>"
                "<p><strong>O'ng tomon:</strong> <em>the six wrought-iron "
                "ties…</em> — ot birikmasi.</p>"
                + why([
                    (True, "—",
                     "yolg'iz tire: chapdan to'liq gap, va u e'lon "
                     "qilingan narsani keskin ochadi. (Ikki nuqta ham "
                     "to'g'ri bo'lardi — variantlar orasida yo'q.)"),
                    (False, ";",
                     "nuqtali vergul o'ngdan mustaqil gap talab qiladi."),
                    (False, ",",
                     "vergul mumkin, lekin <em>one thing</em> e'loni "
                     "ochilishini kutyapti — tire yoki ikki nuqta "
                     "aniqroq. Va vergul bu yerda ro'yxat boshlanayotgandek "
                     "o'qiladi."),
                    (False, " and",
                     "<em>and</em> <em>one thing</em> ni ot birikmasiga "
                     "ulay olmaydi — gap buziladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Peat bogs hold more carbon than all the world's forests together, "
                "and they do it in ground so waterlogged that dead plants cannot rot. "
                "Draining a bog does not merely stop the "
                "<span class=\"sr-blank\"></span> it starts a release, as centuries of "
                "undecayed material meets air for the first time.</p>"),
            "choices": [
                {"text": "storage —", "is_correct": True},
                {"text": "storage,", "is_correct": False},
                {"text": "storage — it,", "is_correct": False},
                {"text": "storage", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikkala tomon ham mustaqil gap. Demak jadvalning birinchi "
                "qatori (W30): nuqta, nuqtali vergul, vergul+FANBOYS — "
                "yoki <mark>tire</mark>, chunki tire ham ikki mustaqil "
                "gapni ulay oladi <u>keskin qarshi qo'yishda</u>.</p>"
                "<p>Va ma'no aynan shunday: <em>not merely stop … it "
                "starts</em> — kutilgan narsa emas, aksi.</p>"
                + why([
                    (True, "storage —",
                     "tire keskin burilishni ko'rsatadi, va "
                     "<em>not merely … it starts</em> qurilishi buni "
                     "talab qiladi."),
                    (False, "storage,",
                     "<strong>vergul splaysi:</strong> ikki mustaqil gap "
                     "yolg'iz vergul bilan bog'lanmaydi (W31)."),
                    (False, "storage — it,",
                     "tire to'g'ri, lekin <em>it</em> takrorlanadi: "
                     "<em>— it, it starts a release</em>. Variantni gapga "
                     "qo'yib o'qing."),
                    (False, "storage",
                     "belgisiz <em>run-on</em>."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Espaliered fruit trees are trained flat against a wall and pruned to "
                "a single plane, and gardeners in cool climates use them for a reason "
                "that has nothing to do with <span class=\"sr-blank\"></span> a brick "
                "wall stores the day's heat and gives it back through the night.</p>"),
            "choices": [
                {"text": "appearance:", "is_correct": True},
                {"text": "appearance,", "is_correct": False},
                {"text": "appearance — because", "is_correct": False},
                {"text": "appearance;  —", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Chap tomon:</strong> <em>…for a reason that has "
                "nothing to do with appearance</em> — to'liq gap ✓, va u "
                "<em>a reason</em> deb e'lon qilyapti.</p>"
                "<p><strong>O'ng tomon:</strong> <em>a brick wall stores the "
                "day's heat…</em> — mustaqil gap, va u "
                "<mark>o'sha sababni ochadi</mark>.</p>"
                + why([
                    (True, "appearance:",
                     "ikki nuqta e'lon qilingan sababni ochadi. Tire ham "
                     "mumkin bo'lardi — lekin variantlar orasida yolg'iz "
                     "tire yo'q."),
                    (False, "appearance — because",
                     "tire <u>va</u> <em>because</em> — ikkita kirituvchi "
                     "birga. Bittasi ortiqcha (W32'dagi «ikki belgi "
                     "birga» tuzog'ining so'zli ko'rinishi)."),
                    (False, "appearance;  —",
                     "nuqtali vergul va tire birga — yana ikkita "
                     "belgi."),
                    (False, "appearance,",
                     "<strong>vergul splaysi:</strong> o'ng tomon mustaqil "
                     "gap."),
                ])
                + TIP.format(
                    "Bu darsning eng foydali odati: <strong>variantni "
                    "gapga qo'yib, boshidan oxirigacha o'qing</strong>. "
                    "To'rt savoldan uchtasida tuzoq belgida emas, "
                    "takrorlangan so'zda yoki ikkinchi kirituvchida "
                    "edi — va ular faqat o'qiganda ko'rinadi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The observatory\u2019s founder \u2014 a brewer who had never studied "
                "<span class=\"sr-blank\"></span> paid for the dome, the telescope and "
                "the salaries of two assistants for thirty years, and asked only that "
                "his name be kept off the building.</p>"),
            "choices": [
                {"text": "astronomy —", "is_correct": True},
                {"text": "astronomy,", "is_correct": False},
                {"text": "astronomy", "is_correct": False},
                {"text": "astronomy)", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar tire <u>yolg\u2018iz emas</u>. Gapning boshida "
                "allaqachon bittasi bor: <em>The observatory\u2019s founder "
                "<strong>\u2014</strong> a brewer who had never studied "
                "astronomy \u2026</em></p>"
                "<p>Demak bu <mark>juft tire</mark>, va u qo\u2018shimcha "
                "bo\u2018lakni (<em>a brewer who had never studied "
                "astronomy</em>) o\u2018rab turibdi. Bo\u2018sh joy uni "
                "<strong>yopishi</strong> kerak.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> qo\u2018shimchani "
                "olsak \u2014 <em>The observatory\u2019s founder paid for the "
                "dome\u2026</em> \u2014 gap butun qoladi ✓</p>"
                + why([
                    (True, "astronomy —",
                     "juftning ikkinchi yarmi. Ochilgan belgi bilan "
                     "yopilgan belgi bir xil bo\u2018lishi shart."),
                    (False, "astronomy,",
                     "<strong>juftni aralashtirish:</strong> tire bilan "
                     "ochilib, vergul bilan yopilyapti. Bu 43-darsning "
                     "mavzusi va bu yerdagi eng ko\u2018p tanlanadigan "
                     "noto\u2018g\u2018ri javob."),
                    (False, "astronomy)",
                     "yana aralashgan juft \u2014 bu safar qavs bilan. Qavs "
                     "ham qo\u2018shimchani o\u2018raydi, lekin u "
                     "<u>qavs bilan</u> ochilishi kerak edi."),
                    (False, "astronomy",
                     "juft yopilmagan: birinchi tire ochilgan-u, ikkinchisi "
                     "yo\u2018q. O\u2018quvchi qo\u2018shimcha qayerda tugaganini "
                     "bilmaydi."),
                ])
                + TIP.format(
                    "Tire ko\u2018rgan zahotingizda <strong>gapning boshiga "
                    "qarang</strong>: u yerda ham tire bormi? Bor bo\u2018lsa \u2014 "
                    "siz juftning ikkinchi yarmini tanlayapsiz, va javob "
                    "deyarli har doim tire.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a dash ( — )</div><div class="pp-card-back">tire</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a single dash</div><div class="pp-card-back">yolg\'iz tire (ikki nuqta kabi ishlaydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a pair of dashes</div><div class="pp-card-back">juft tire (qo\'shimcha bo\'lakni o\'raydi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">wrought iron</div><div class="pp-card-back">bolg\'alangan temir</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a tie (in a bridge)</div><div class="pp-card-back">tortqi, bog\'lovchi element</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">waterlogged</div><div class="pp-card-back">suvga to\'yingan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">undecayed</div><div class="pp-card-back">chirimagan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an apprentice</div><div class="pp-card-back">shogird</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Yolg'iz tire = ikki nuqta: <strong>oldidan to'liq "
              "gap</strong>, lekin keskinroq ohangda.</li>"
              "<li>Juft tire = qo'shimcha bo'lakni o'raydi — boshqa "
              "qoida (42, 43-darslar).</li>"
              "<li>Tire ko'rsangiz birinchi savol: <strong>yolg'izmi yoki "
              "juftning yarmimi?</strong></li>"
              "<li>Tire va ikki nuqta birga berilsa va ikkovi ham "
              "to'g'ri bo'lsa — ikkovi ham javob emas.</li>"
              "<li><strong>Variantni gapga qo'yib o'qing</strong> — "
              "takrorlangan so'z tuzog'i faqat shunda ko'rinadi.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 42
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W42: Supplements — Commas, Dashes and Parentheses Around Extra Information",
    "summary": "Qo'shimcha bo'lak olib tashlanadigan bo'lishi kerak, va gap "
               "o'rtasida turgan bo'lsa — IKKI tomondan belgi qo'yiladi.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>Olib tashlash sinovi</h2>"
            "<p><strong>Supplement</strong> — gapga qo'shimcha ma'lumot "
            "beruvchi, lekin gapning tuzilishiga kirmaydigan bo'lak. "
            "Uning ta'rifi bitta sinovga qisqaradi:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Bo'lakni "
                "olib tashlang. Gap butun va to'g'ri qoladimi?</strong><br>"
                "Ha → bu qo'shimcha, va u belgi bilan ajratiladi.<br>"
                "Yo'q → bu gapning kerakli qismi, belgi "
                "qo'yilmaydi.</p>")
            + "<p>Uch belgi bir xil ish qiladi: <strong>vergul</strong>, "
            "<strong>tire</strong>, <strong>qavs</strong>. Farq faqat "
            "ohangda — vergul neytral, tire keskin, qavs pichirlab "
            "aytilgan.</p>"
            + '<span class="sr-time">⏱ ~35 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki tomondan qoidasi</h3>"
            "<p>Qo'shimcha gapning <u>o'rtasida</u> tursa, u "
            "<mark>ikki tomondan</mark> belgilanadi. Bitta belgi "
            "yetmaydi.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\">✓ <em>The dome<strong>,</strong> "
                "rebuilt twice<strong>,</strong> still stands.</em><br>"
                "✗ <em>The dome<strong>,</strong> rebuilt twice still "
                "stands.</em><br>"
                "✗ <em>The dome rebuilt twice<strong>,</strong> still "
                "stands.</em></p>"
                "<p style=\"margin:8px 0 0;\">Oxirgi ikkisi "
                "<u>yarim ochilgan</u> qo'shimcha: o'quvchi qayerda "
                "boshlanib qayerda tugaganini bilmaydi.</p>")
            + "<p>Qo'shimcha gapning <u>oxirida</u> tursa, bitta belgi "
            "yetadi — chunki gapning nuqtasi ikkinchi belgi vazifasini "
            "bajaradi.</p>"
            + WARN.format(
                "44-darsda ko'ramiz: ega bilan kesim orasiga vergul "
                "qo'yilmaydi. Yarim ochilgan qo'shimcha aynan shu xatoni "
                "yasaydi — <em>The dome rebuilt twice, still stands</em> "
                "da vergul egadan kesimni ajratib qo'ygan.")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The Antonine Wall, built of turf rather than stone and abandoned "
                "within a <span class=\"sr-blank\"></span> has left far less above ground "
                "than the stone wall to the south, though the ditch beside it can still "
                "be traced for kilometres.</p>")
            + choices_html([
                "generation",
                "generation,",
                "generation —",
                "generation;",
            ])
            + "<p><strong>Qo'shimchani toping.</strong> Gapning boshida "
            "vergul bor: <em>The Antonine Wall<strong>,</strong> built of "
            "turf rather than stone and abandoned within a "
            "generation…</em></p>"
            "<p>Demak vergul bilan <mark>qo'shimcha ochilgan</mark> — va "
            "bo'sh joy uni yopishi kerak, <u>xuddi shu belgi</u> "
            "bilan.</p>"
            "<p><strong>Olib tashlash sinovi:</strong> <em>The Antonine "
            "Wall has left far less above ground than the stone wall to the "
            "south</em> — gap butun ✓</p>"
            + why([
                (True, "generation,",
                 "juftning ikkinchi vergul, ochilgani bilan bir xil. "
                 "Qo'shimcha endi ikki tomondan yopiq."),
                (False, "generation —",
                 "<strong>juftni aralashtirish:</strong> vergul bilan "
                 "ochilib, tire bilan yopilyapti (43-dars)."),
                (False, "generation;",
                 "nuqtali vergul ikki mustaqil gap orasida bo'ladi, va u "
                 "qo'shimchani yopa olmaydi."),
                (False, "generation",
                 "juft yopilmagan. Va natijada vergul egani "
                 "(<em>The Antonine Wall</em>) kesimidan "
                 "(<em>has left</em>) ajratib qo'yadi — 44-darsdagi "
                 "xato."),
            ])
            + NOTE.format(
                "Antonin devori — Rimliklar hozirgi Shotlandiya hududida "
                "II asrda qurgan chegara istehkomi; u toshdan emas, "
                "chimdan qurilgan va Hadrian devoridan ancha erta tashlab "
                "ketilgan. Lekin bu bilim savolga yordam bermaydi — javobni "
                "faqat birinchi vergul beradi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Marie Tharp — the geologist who drew the first map of the ocean "
                "<span class=\"sr-blank\"></span> was not allowed aboard a research ship "
                "for the first eighteen years of the work and plotted every sounding from "
                "figures brought back by others.</p>"),
            "choices": [
                {"text": "floor —", "is_correct": True},
                {"text": "floor,", "is_correct": False},
                {"text": "floor", "is_correct": False},
                {"text": "floor;", "is_correct": False},
            ],
            "explanation": (
                "<p>Gapning boshida tire bor: <em>Marie Tharp "
                "<strong>—</strong> the geologist who drew the first map of "
                "the ocean floor…</em>. Juft ochilgan.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>Marie Tharp "
                "was not allowed aboard a research ship…</em> — gap "
                "butun ✓</p>"
                + why([
                    (True, "floor —",
                     "juftning ikkinchi tiresi. Ochilgan belgi bilan bir "
                     "xil."),
                    (False, "floor,",
                     "<strong>aralashgan juft:</strong> tire ochdi, vergul "
                     "yopyapti."),
                    (False, "floor;",
                     "nuqtali vergul qo'shimchani yopa olmaydi, va o'ng "
                     "tomon mustaqil gap ham emas."),
                    (False, "floor",
                     "juft yopilmagan — qo'shimcha qayerda tugagani "
                     "noma'lum."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The oldest bell in the tower was cast in 1584 and has been rehung "
                "three times, most recently in 1971 when the frame was "
                "<span class=\"sr-blank\"></span> It is rung only on the two days a year "
                "the church is open to visitors.</p>"),
            "choices": [
                {"text": "replaced.", "is_correct": True},
                {"text": "replaced,", "is_correct": False},
                {"text": "replaced —", "is_correct": False},
                {"text": "replaced;", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu safar qo'shimcha gapning <u>oxirida</u>: "
                "<em>most recently in 1971 when the frame was replaced</em>. "
                "U vergul bilan ochilgan.</p>"
                "<p>Qo'shimcha gap oxirida tursa, "
                "<mark>ikkinchi belgi kerak emas</mark> — gapning nuqtasi "
                "uni yopadi.</p>"
                "<p>Va o'ng tomon: <em>It is rung only on the two days…</em> "
                "— <u>mustaqil gap</u>. Demak bu yerda gap tugashi "
                "kerak.</p>"
                + why([
                    (True, "replaced.",
                     "nuqta gapni tugatadi va shu bilan qo'shimchani ham "
                     "yopadi. Keyingi mustaqil gap yangi jumla sifatida "
                     "boshlanadi."),
                    (False, "replaced,",
                     "<strong>vergul splaysi</strong> (W31): keyingi bo'lak "
                     "mustaqil gap."),
                    (False, "replaced —",
                     "tire ham splays yasaydi bu yerda, va ustiga u "
                     "vergul bilan ochilgan juftni aralashtiradi."),
                    (False, "replaced;",
                     "<strong>eng nozik variant:</strong> nuqtali vergul "
                     "ikki mustaqil gapni ulash uchun grammatik jihatdan "
                     "to'g'ri. Lekin u <u>vergul bilan ochilgan "
                     "qo'shimchaning ichida</u> qolib ketadi va o'quvchi "
                     "qo'shimcha qayerda tugaganini bilmaydi. Nuqta "
                     "aniqroq."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Cast iron is strong in compression and weak in "
                "<span class=\"sr-blank\"></span> a property that suits it to columns "
                "and rules it out for beams, and nineteenth-century builders who "
                "forgot the second half of that sentence left behind the mill floors "
                "that failed.</p>"),
            "choices": [
                {"text": "tension,", "is_correct": True},
                {"text": "tension", "is_correct": False},
                {"text": "tension;", "is_correct": False},
                {"text": "tension, and", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Olib tashlash sinovi.</strong> Qo'shimcha: "
                "<em>a property that suits it to columns and rules it out "
                "for beams</em>. Uni olib tashlaymiz: <em>Cast iron is "
                "strong in compression and weak in tension, and "
                "nineteenth-century builders … left behind the mill "
                "floors that failed.</em> — gap butun ✓</p>"
                "<p>Demak bu qo'shimcha, va u vergul bilan "
                "ochiladi. (Ikkinchi vergul gapda allaqachon bor: "
                "<em>…for beams<strong>,</strong> and nineteenth-century…</em>)</p>"
                + why([
                    (True, "tension,",
                     "vergul appozitsiyani ochadi, va u gapda "
                     "<em>beams</em> dan keyingi vergul bilan "
                     "yopiladi."),
                    (False, "tension;",
                     "nuqtali vergul o'ngdan mustaqil gap talab qiladi; "
                     "<em>a property that…</em> ot birikmasi."),
                    (False, "tension, and",
                     "<em>and</em> ot birikmasini fe'lga ulay olmaydi, va "
                     "gapda allaqachon <em>and</em> bor — ikki marta "
                     "chiqadi."),
                    (False, "tension",
                     "belgisiz: <em>weak in tension a property that…</em> "
                     "bo'lib o'qiladi."),
                ])
                + TIP.format(
                    "<strong>Olib tashlash sinovi</strong> bu mavzudagi eng "
                    "ishonchli quroling. Bo'lakni olib gapni o'qing: "
                    "butun qolsa — belgi kerak; buzilsa — belgi "
                    "qo'yilmaydi. Bu 45-darsdagi «kerakli / keraksiz» "
                    "farqining ham asosi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The cathedral clock (installed in 1386 and still driven by falling "
                "<span class=\"sr-blank\"></span> has no face and no hands: it was built "
                "to strike the hours, not to be looked at.</p>"),
            "choices": [
                {"text": "weights)", "is_correct": True},
                {"text": "weights,", "is_correct": False},
                {"text": "weights —", "is_correct": False},
                {"text": "weights", "is_correct": False},
            ],
            "explanation": (
                "<p>Qavs ham qo\u2018shimchani o\u2018raydi \u2014 vergul va tire "
                "kabi. Va u ham <mark>juft</mark>: gapda ochilgan qavs "
                "bor (<em>clock <strong>(</strong>installed in 1386\u2026</em>), "
                "demak bo\u2018sh joy uni yopishi kerak.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>The cathedral "
                "clock has no face and no hands\u2026</em> \u2014 gap butun ✓</p>"
                + why([
                    (True, "weights)",
                     "juftning ikkinchi qavsi. Qavs bilan ochilgan "
                     "qo\u2018shimcha qavs bilan yopiladi."),
                    (False, "weights,",
                     "<strong>aralashgan juft:</strong> qavs ochdi, vergul "
                     "yopyapti (43-dars)."),
                    (False, "weights —",
                     "yana aralashgan juft \u2014 bu safar tire bilan."),
                    (False, "weights",
                     "qavs yopilmagan. Bu \u2014 bu turdagi eng ko\u2018p "
                     "e\u2019tibordan chetda qoladigan xato, chunki ochilgan "
                     "qavs gapning boshida turadi va o\u2018quvchi uni "
                     "unutadi."),
                ])
                + TIP.format(
                    "Bo\u2018sh joyda vergul, tire yoki qavs ko\u2018rsangiz, "
                    "<strong>gapning boshiga qaytib qarang</strong>: u yerda "
                    "ochilgan belgi bormi? Bor bo\u2018lsa \u2014 siz juftning "
                    "ikkinchi yarmini tanlayapsiz va javob "
                    "<u>xuddi o\u2018sha belgi</u>.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a supplement</div><div class="pp-card-back">qo\'shimcha bo\'lak (olib tashlansa gap butun qoladi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">parentheses ( )</div><div class="pp-card-back">qavs</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to set off (a phrase)</div><div class="pp-card-back">(bo\'lakni) belgi bilan ajratmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an appositive</div><div class="pp-card-back">appozitsiya — otni izohlovchi qo\'shimcha</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">turf</div><div class="pp-card-back">chim (o\'t bilan tuproq qatlami)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to rehang (a bell)</div><div class="pp-card-back">(qo\'ng\'iroqni) qayta osmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">compression / tension</div><div class="pp-card-back">siqilish / cho\'zilish</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to rule out</div><div class="pp-card-back">yaroqsiz qilmoq, istisno qilmoq</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Olib tashlash sinovi:</strong> bo'lakni oling — "
              "gap butun qoladimi?</li>"
              "<li>Uch belgi bir xil ish qiladi: <strong>vergul · tire · "
              "qavs</strong>.</li>"
              "<li>Gap <u>o'rtasidagi</u> qo'shimcha — "
              "<strong>ikki tomondan</strong> belgilanadi.</li>"
              "<li>Gap <u>oxiridagi</u> qo'shimcha — bitta belgi yetadi, "
              "nuqta ikkinchisini bajaradi.</li>"
              "<li>Yarim ochilgan qo'shimcha egani kesimidan ajratib "
              "qo'yadi — 44-darsdagi xato.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 43
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W43: Never Mix the Pair — A Dash Cannot Close What a Comma Opened",
    "summary": "Bir qatorli qoida, imtihonda muntazam sinaladi: qo'shimcha qaysi belgi "
               "bilan ochilgan bo'lsa, o'sha belgi bilan yopiladi.",
    "order": 43,
    "blocks": [
        {"rich_text": (
            "<h2>Ochilgan belgi bilan yopiladi</h2>"
            "<p>42-darsda ko'rdik: qo'shimcha bo'lakni vergul, tire yoki "
            "qavs ajratadi. Endi ular haqidagi eng qat'iy qoida:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Qo'shimcha "
                "qaysi belgi bilan ochilgan bo'lsa, aynan o'sha belgi "
                "bilan yopiladi. Aralashtirish mumkin emas.</strong></p>")
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Ochilgan</th><th>Yopilishi kerak</th>"
              "<th>Namuna</th></tr></thead>"
              "<tbody>"
              "<tr><td>vergul</td><td>vergul</td>"
              "<td><em>The dome, rebuilt twice, still stands.</em></td></tr>"
              "<tr><td>tire</td><td>tire</td>"
              "<td><em>The dome — rebuilt twice — still stands.</em></td></tr>"
              "<tr><td>qavs</td><td>qavs</td>"
              "<td><em>The dome (rebuilt twice) still stands.</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<p>Va taqiqlangan: <em>The dome, rebuilt twice — still "
            "stands.</em> · <em>The dome — rebuilt twice, still "
            "stands.</em> · <em>The dome (rebuilt twice, still "
            "stands.</em></p>"
            + '<span class="sr-time">⏱ ~20 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Nega bu shu qadar foydali</h3>"
            "<p>Bu qoida imtihondagi eng <mark>arzon</mark> ballardan "
            "birini beradi, chunki uni tekshirish uchun gapni tushunish "
            "shart emas.</p>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. Bo'sh joyda vergul, "
              "tire yoki qavs bormi?</strong></p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Gapning boshiga qaytib "
              "qarang</strong> — o'sha belgilardan biri ochilganmi?</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Ochilgan bo'lsa — "
              "javob o'sha belgi.</strong> Ikkinchi qadamda "
              "gapning ma'nosi umuman kerak emas.</p></div>"
            + '</div>'
            + WARN.format(
                "SAT bu tuzoqni ataylab <u>uzoq</u> qo'shimcha bilan "
                "qo'yadi: ochilgan belgi bilan bo'sh joy orasida "
                "o'n-o'n besh so'z bo'ladi, va o'quvchi boshidagi "
                "vergulni unutadi. <strong>Har doim boshiga "
                "qayting.</strong>")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>Cochineal, a red dye obtained from an insect that lives on cactus "
                "pads and once among the most valuable exports from the "
                "<span class=\"sr-blank\"></span> takes roughly seventy thousand insects "
                "to produce a single kilogram.</p>")
            + choices_html([
                "Americas —",
                "Americas,",
                "Americas",
                "Americas;",
            ])
            + "<p><strong>1-qadam:</strong> bo'sh joyda ajratuvchi belgi "
            "kerakmi? Ha — undan keyin <em>takes</em> kelyapti, ya'ni "
            "gapning kesimi.</p>"
            "<p><strong>2-qadam — boshiga qaytamiz:</strong> "
            "<em>Cochineal<strong>,</strong> a red dye obtained from…</em> "
            "— <mark>vergul bilan ochilgan</mark>.</p>"
            "<p><strong>3-qadam:</strong> javob — vergul. Gapning "
            "mazmunini o'ylab ko'rish shart emas.</p>"
            + why([
                (True, "Americas,",
                 "ochilgan vergul bilan bir xil. Qo'shimcha "
                 "(<em>a red dye … Americas</em>) endi ikki tomondan "
                 "yopiq, va ega <em>Cochineal</em> kesimi "
                 "<em>takes</em> ga ulanadi."),
                (False, "Americas —",
                 "<strong>aralashgan juft:</strong> vergul ochdi, tire "
                 "yopyapti. Bu darsning bosh tuzog'i — va u eng ko'p "
                 "tanlanadi, chunki tire «kuchliroq» tuyuladi."),
                (False, "Americas;",
                 "nuqtali vergul qo'shimchani yopa olmaydi, va u ikki "
                 "mustaqil gap talab qiladi."),
                (False, "Americas",
                 "juft yopilmagan — va natijada birinchi vergul egani "
                 "kesimidan ajratib qo'yadi (44-dars)."),
            ])
            + NOTE.format(
                "Ochilgan vergul bilan bo'sh joy orasida "
                "<u>o'n to'rt so'z</u> bor. SAT masofani ataylab "
                "uzaytiradi — boshiga qaytish odati aynan shuning uchun "
                "kerak.")
        )},

        {
            "rich_text": conv_q(
                "<p>The Voyager 1 probe — launched in 1977, still returning data and now "
                "far beyond the region shaped by the Sun's "
                "<span class=\"sr-blank\"></span> takes more than twenty hours to send a "
                "signal home.</p>"),
            "choices": [
                {"text": "wind —", "is_correct": True},
                {"text": "wind,", "is_correct": False},
                {"text": "wind", "is_correct": False},
                {"text": "wind)", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qaytamiz:</strong> <em>The Voyager 1 "
                "probe <strong>—</strong> launched in 1977…</em> — "
                "<mark>tire bilan ochilgan</mark>.</p>"
                "<p>Diqqat: qo'shimchaning ichida ikkita vergul bor "
                "(<em>1977, still returning data and…</em>) — lekin ular "
                "ro'yxat vergullari, juftning bir qismi emas.</p>"
                + why([
                    (True, "wind —",
                     "tire bilan ochilgan juft tire bilan yopiladi."),
                    (False, "wind,",
                     "<strong>aralashgan juft.</strong> Va ichkaridagi "
                     "vergullar bu tanlovni yanada jozibali qiladi — "
                     "aynan shuning uchun tuzoq."),
                    (False, "wind)",
                     "qavs bilan yopish — juft qavs bilan ochilmagan."),
                    (False, "wind",
                     "juft yopilmagan; ega kesimidan uzilib qoladi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Kintsugi (a Japanese method of repairing broken ceramics in which the "
                "pieces are rejoined with lacquer mixed with powdered "
                "<span class=\"sr-blank\"></span> leaves the repair visible rather than "
                "hiding it.</p>"),
            "choices": [
                {"text": "gold)", "is_correct": True},
                {"text": "gold,", "is_correct": False},
                {"text": "gold —", "is_correct": False},
                {"text": "gold", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qaytamiz:</strong> <em>Kintsugi "
                "<strong>(</strong>a Japanese method…</em> — qavs bilan "
                "ochilgan.</p>"
                "<p>Qavs — bu turdagi eng oson holat, chunki ochilgan qavs "
                "<u>ko'zga tashlanadi</u>. Lekin uzun qo'shimchada "
                "o'quvchi baribir unutadi.</p>"
                + why([
                    (True, "gold)",
                     "qavs bilan ochilgan qo'shimcha qavs bilan "
                     "yopiladi."),
                    (False, "gold,",
                     "<strong>aralashgan juft.</strong>"),
                    (False, "gold —",
                     "yana aralashgan juft."),
                    (False, "gold",
                     "yopilmagan qavs. Gap grammatik jihatdan "
                     "tugamaydi."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The seed vault cut into a mountainside inside the Arctic Circle — a "
                "backup for collections kept elsewhere and opened only when one of them "
                "has been <span class=\"sr-blank\"></span> is designed to be entered as "
                "seldom as possible.</p>"),
            "choices": [
                {"text": "lost —", "is_correct": True},
                {"text": "lost,", "is_correct": False},
                {"text": "lost;", "is_correct": False},
                {"text": "lost:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qaytamiz:</strong> <em>…inside the Arctic "
                "Circle <strong>—</strong> a backup for collections…</em> — "
                "tire bilan ochilgan.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>The seed vault "
                "cut into a mountainside inside the Arctic Circle is "
                "designed to be entered as seldom as possible.</em> — gap "
                "butun ✓</p>"
                + why([
                    (True, "lost —",
                     "juftning ikkinchi tiresi."),
                    (False, "lost,",
                     "<strong>aralashgan juft.</strong>"),
                    (False, "lost:",
                     "ikki nuqta qo'shimchani yopa olmaydi — u "
                     "e'lon qiladi, ochilgan bo'lakni "
                     "tugatmaydi."),
                    (False, "lost;",
                     "nuqtali vergul ham juftni yopa olmaydi, va "
                     "o'ng tomon mustaqil gap emas "
                     "(<em>is designed…</em> — egasi ochilgan "
                     "qo'shimchadan oldin)."),
                ])
                + TIP.format(
                    "Uch savolda ham javobni <strong>gapning birinchi "
                    "belgisi</strong> berdi. Bu bu mavzudagi eng tez "
                    "yechiladigan savol turi — yigirma soniyadan "
                    "oshmasin.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The engineers who inspect the bridge each spring look first at the "
                "six wrought-iron ties that hold the deck to the "
                "<span class=\"sr-blank\"></span> and only afterwards at the masonry of "
                "the piers.</p>"),
            "choices": [
                {"text": "arch", "is_correct": True},
                {"text": "arch,", "is_correct": False},
                {"text": "arch —", "is_correct": False},
                {"text": "arch;", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol qoidani <u>teskari tomondan</u> sinaydi. "
                "<strong>Boshiga qaytamiz:</strong> gapda ochilgan vergul "
                "ham, tire ham, qavs ham <mark>yo\u2018q</mark>. Demak "
                "yopiladigan hech narsa yo\u2018q.</p>"
                "<p><strong>O\u2018ng tomon:</strong> <em>and only afterwards at "
                "the masonry of the piers</em> \u2014 bu mustaqil gap emas, "
                "u <em>look first at\u2026</em> ning ikkinchi yarmi: "
                "<em>look first at X and only afterwards at Y</em>. Ikki "
                "predlogli birikma <em>and</em> bilan ulangan.</p>"
                + why([
                    (True, "arch",
                     "belgisiz. Bir jinsli ikki bo\u2018lakni <em>and</em> "
                     "ulaganda vergul qo\u2018yilmaydi \u2014 vergul faqat ikki "
                     "<u>mustaqil gap</u> ulanganda kerak (W32)."),
                    (False, "arch,",
                     "<strong>eng ko\u2018p tanlanadigan noto\u2018g\u2018ri javob:</strong> "
                     "o\u2018quvchi \u00abvergul + and\u00bb qoidasini avtomatik "
                     "qo\u2018llaydi. Lekin o\u2018ng tomon gap emas."),
                    (False, "arch —",
                     "tire hech nimani yopmaydi \u2014 ochilgan juft yo\u2018q \u2014 va "
                     "yolg\u2018iz tire sifatida ham o\u2018rinsiz: undan keyin "
                     "izoh emas, ro\u2018yxatning davomi keladi."),
                    (False, "arch;",
                     "nuqtali vergul ikki mustaqil gap talab qiladi."),
                ])
                + TIP.format(
                    "Bu savol darsning qoidasini <strong>ishonchli</strong> "
                    "qiladi: \u00abboshiga qara\u00bb qadami \u00abbelgi qo\u2018y\u00bb degani "
                    "emas. Ochilgan belgi <u>yo\u2018q</u> bo\u2018lsa, javob "
                    "ko\u2018pincha <u>belgisiz</u> variant.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to open / close a supplement</div><div class="pp-card-back">qo\'shimchani ochmoq / yopmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a matching pair</div><div class="pp-card-back">mos juftlik (bir xil belgi)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">cochineal</div><div class="pp-card-back">koshenil (hasharotdan olinadigan qizil bo\'yoq)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cactus pad</div><div class="pp-card-back">kaktusning yassi bo\'lagi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a probe (space)</div><div class="pp-card-back">kosmik zond</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the Arctic Circle</div><div class="pp-card-back">Shimoliy qutb doirasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a backup</div><div class="pp-card-back">zaxira nusxa</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">seldom</div><div class="pp-card-back">kamdan-kam</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Ochilgan belgi = yopiladigan belgi.</strong> "
              "Aralashtirish mumkin emas.</li>"
              "<li>Uch qadam: bo'sh joyda ajratuvchi kerakmi → gapning "
              "boshiga qara → o'sha belgini tanla.</li>"
              "<li>Gapning <u>ma'nosi</u> bu savolda kerak emas — "
              "shuning uchun u eng arzon ball.</li>"
              "<li>SAT ochilgan belgi bilan bo'sh joy orasini ataylab "
              "uzaytiradi: <strong>har doim boshiga qayting</strong>.</li>"
              "<li>Ikki nuqta va nuqtali vergul qo'shimchani "
              "<u>yopa olmaydi</u>.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 44
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W44: No Comma Between Subject and Verb",
    "summary": "Uzun ega o'z kesimidan vergul bilan ajratilmaydi. O'zbek quloq bu "
               "yerda pauza eshitadi — va aynan shu pauza xatoni yasaydi.",
    "order": 44,
    "blocks": [
        {"rich_text": (
            "<h2>Pauza vergul emas</h2>"
            "<p>Bu dars bitta xatoni o'rgatadi, va u o'zbek o'quvchi uchun "
            "<mark>alohida xavfli</mark>:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.08em;\"><strong>Ega bilan "
                "kesim orasiga vergul qo'yilmaydi. Ega qanchalik uzun "
                "bo'lmasin.</strong></p>")
            + "<p>✗ <em>The engineer who designed the roof of the new "
            "terminal<strong>,</strong> had never built anything larger than "
            "a barn.</em></p>"
            "<p>✓ <em>The engineer who designed the roof of the new terminal "
            "had never built anything larger than a barn.</em></p>"
            + "<p>Nega bu xato tez-tez qilinadi? Chunki ega uzun "
            "bo'lganda <u>ovoz chiqarib o'qiganda pauza qilinadi</u> — va "
            "quloq pauzani vergul deb tarjima qiladi. Lekin ingliz "
            "tilida <strong>pauza vergul emas</strong>.</p>"
            + '<span class="sr-time">⏱ ~25 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Uch joyga vergul qo'yilmaydi</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Qayerga</th><th>Xato namunasi</th></tr></thead>"
              "<tbody>"
              "<tr><td><strong>Ega ↔ kesim</strong></td>"
              "<td>✗ <em>The three surveys carried out that winter, showed "
              "nothing.</em></td></tr>"
              "<tr><td><strong>Kesim ↔ to'ldiruvchi</strong></td>"
              "<td>✗ <em>The report concluded, that the ice had "
              "thinned.</em></td></tr>"
              "<tr><td><strong>Predlog ↔ oti</strong></td>"
              "<td>✗ <em>The dye was made from, an insect that lives on "
              "cactus.</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Istisno faqat bitta:</strong> ega bilan kesim "
                "orasida <u>ikki tomondan yopilgan qo'shimcha</u> tursa, "
                "vergullar to'g'ri — chunki ular egani kesimdan emas, "
                "qo'shimchani gapdan ajratyapti: "
                "<em>The dome<strong>,</strong> rebuilt "
                "twice<strong>,</strong> still stands.</em> Bitta vergul "
                "xato, ikkitasi to'g'ri (42-dars).")
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The librarians who catalogued the collection in 1907 and shelved it "
                "by the century they believed each manuscript to belong "
                "<span class=\"sr-blank\"></span> left no record of how those judgements "
                "had been reached.</p>")
            + choices_html([
                "to,",
                "to",
                "to;",
                "to —",
            ])
            + "<p><strong>Egani toping.</strong> <em>The librarians who "
            "catalogued the collection in 1907 and shelved it by the century "
            "they believed each manuscript to belong to</em> — bu butun "
            "bo'lak <mark>ega</mark>. U uzun, chunki ichida ikkita "
            "nisbiy gap bor.</p>"
            "<p><strong>Kesim:</strong> <em>left</em>.</p>"
            "<p>Ega tugadi, kesim boshlandi. Orasiga hech narsa "
            "qo'yilmaydi.</p>"
            + why([
                (True, "to",
                 "belgisiz. Ega qanchalik uzun bo'lsa ham, u kesimidan "
                 "vergul bilan ajratilmaydi."),
                (False, "to,",
                 "<strong>ega bilan kesim orasidagi vergul</strong> — bu "
                 "darsning bosh xatosi. Ega uzun bo'lgani uchun pauza "
                 "eshitiladi, lekin pauza vergul emas."),
                (False, "to —",
                 "tire ham xuddi shu xatoni qiladi, va ustiga u "
                 "ochilmagan juftni yopmoqchi bo'ladi."),
                (False, "to;",
                 "nuqtali vergul ikki mustaqil gap orasida bo'ladi; bu "
                 "yerda chap tomon gap emas — u faqat ega."),
            ])
            + NOTE.format(
                "Ega bilan kesim orasida <u>o'n uch so'z</u> bor. SAT "
                "masofani ataylab uzaytiradi — <strong>egani va kesimni "
                "toping</strong>, oradagi so'zlarni "
                "e'tiborsiz qoldiring.")
        )},

        {
            "rich_text": conv_q(
                "<p>A survey of the households that had installed water meters and "
                "agreed to have their consumption recorded for two full years "
                "<span class=\"sr-blank\"></span> that average use had fallen by about a "
                "tenth.</p>"),
            "choices": [
                {"text": "found", "is_correct": True},
                {"text": "found,", "is_correct": False},
                {"text": ", found", "is_correct": False},
                {"text": ", found,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>A survey of the households that "
                "had installed water meters and agreed to have their "
                "consumption recorded for two full years</em>. "
                "<strong>Kesim:</strong> <em>found</em>. "
                "<strong>To'ldiruvchi:</strong> <em>that average use had "
                "fallen…</em></p>"
                "<p>Uch tomondan ham vergul taqiqlangan: ega↔kesim va "
                "kesim↔to'ldiruvchi.</p>"
                + why([
                    (True, "found",
                     "hech qanday belgi yo'q — ega, kesim va "
                     "to'ldiruvchi uzluksiz."),
                    (False, ", found",
                     "<strong>ega ↔ kesim</strong> vergul."),
                    (False, "found,",
                     "<strong>kesim ↔ to'ldiruvchi</strong> vergul: "
                     "<em>found, that average use…</em>. Bu ham "
                     "taqiqlangan (jadvalning ikkinchi qatori)."),
                    (False, ", found,",
                     "ikkovi birga. Bu kesimni qo'shimcha bo'lakdek "
                     "o'rab qo'yadi — lekin kesimni gapdan olib tashlab "
                     "bo'lmaydi, ya'ni u qo'shimcha emas."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The three cartographers who surveyed the coast between 1841 and "
                "<span class=\"sr-blank\"></span> disagreed about almost nothing except "
                "the position of a single headland, which each of them placed in a "
                "different bay.</p>"),
            "choices": [
                {"text": "1847", "is_correct": True},
                {"text": "1847,", "is_correct": False},
                {"text": "1847 —", "is_correct": False},
                {"text": "1847:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The three cartographers who "
                "surveyed the coast between 1841 and 1847</em>. "
                "<strong>Kesim:</strong> <em>disagreed</em>.</p>"
                "<p>Nisbiy gap (<em>who surveyed…</em>) eganing "
                "<u>ichida</u> — u qo'shimcha emas, chunki uni olib "
                "tashlasak <em>The three cartographers disagreed…</em> "
                "qoladi-yu, gap boshqa ma'no beradi: qaysi "
                "kartograflar?</p>"
                + why([
                    (True, "1847",
                     "belgisiz — ega kesimidan ajratilmaydi, va nisbiy gap "
                     "kerakli (45-dars), shuning uchun u ham vergul "
                     "olmaydi."),
                    (False, "1847,",
                     "<strong>ega ↔ kesim</strong> vergul. Sana bilan "
                     "tugagani uchun bu yerda vergul ayniqsa jozibali "
                     "ko'rinadi."),
                    (False, "1847 —",
                     "tire xuddi shu xatoni qiladi va ochilmagan juftni "
                     "yopmoqchi bo'ladi."),
                    (False, "1847:",
                     "ikki nuqtadan oldin to'liq gap turishi shart; bu "
                     "yerda faqat ega bor."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The manuscript that the conservator found beneath the varnish "
                "<span class=\"sr-blank\"></span> a second signature in a hand quite "
                "unlike the one on the frame.</p>"),
            "choices": [
                {"text": "carried", "is_correct": True},
                {"text": "carried,", "is_correct": False},
                {"text": ", carried", "is_correct": False},
                {"text": "; carried", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The manuscript that the "
                "conservator found beneath the varnish</em>. "
                "<strong>Kesim:</strong> <em>carried</em>. "
                "<strong>To'ldiruvchi:</strong> <em>a second "
                "signature…</em></p>"
                "<p>Bu gapda ikkita fe'l bor — <em>found</em> va "
                "<em>carried</em> — va shuning uchun o'quvchi chalkashadi. "
                "Lekin <em>found</em> nisbiy gapga tegishli "
                "(<em>that the conservator found</em>), "
                "<mark>asosiy kesim esa <em>carried</em></mark>.</p>"
                + why([
                    (True, "carried",
                     "belgisiz. Ega (nisbiy gapi bilan birga) darhol "
                     "kesimga ulanadi."),
                    (False, ", carried",
                     "<strong>ega ↔ kesim</strong> vergul."),
                    (False, "carried,",
                     "<strong>kesim ↔ to'ldiruvchi</strong> vergul."),
                    (False, "; carried",
                     "nuqtali vergul ikki mustaqil gap talab qiladi — "
                     "chap tomon faqat ega."),
                ])
                + TIP.format(
                    "Uzun egada <strong>asosiy kesimni toping</strong>: u "
                    "nisbiy gap ichidagi fe'l emas. Sinov: egani bir "
                    "so'z bilan almashtiring — "
                    "<em>It carried a second signature.</em> Gap "
                    "ishlaydimi? Ha. Demak <em>carried</em> asosiy kesim, "
                    "va undan oldin vergul qo'yilmaydi.")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Cast iron, which is strong in compression and weak in "
                "<span class=\"sr-blank\"></span> was used correctly for columns "
                "throughout the nineteenth century and disastrously for beams in a "
                "handful of mills.</p>"),
            "choices": [
                {"text": "tension,", "is_correct": True},
                {"text": "tension", "is_correct": False},
                {"text": "tension —", "is_correct": False},
                {"text": "tension;", "is_correct": False},
            ],
            "explanation": (
                "<p>Bu savol darsning <u>istisnosini</u> sinaydi. "
                "<strong>Boshiga qarang:</strong> <em>Cast "
                "iron<strong>,</strong> which is strong in compression\u2026</em> "
                "\u2014 vergul bilan qo\u2018shimcha ochilgan.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>Cast iron was "
                "used correctly for columns\u2026</em> \u2014 gap butun ✓ "
                "Demak <em>which is\u2026 tension</em> qo\u2018shimcha, va u "
                "ikki tomondan yopilishi kerak.</p>"
                "<p><mark>Ikki vergul ega bilan kesim orasida turishi "
                "mumkin</mark> \u2014 chunki ular egani kesimdan emas, "
                "qo\u2018shimchani gapdan ajratyapti. Bitta vergul xato "
                "bo\u2018lardi; ikkitasi to\u2018g\u2018ri.</p>"
                + why([
                    (True, "tension,",
                     "juftning ikkinchi verguli. Qo\u2018shimcha yopiladi va "
                     "<em>Cast iron</em> o\u2018z kesimiga (<em>was used</em>) "
                     "ulanadi."),
                    (False, "tension",
                     "juft yopilmagan \u2014 va endi birinchi vergul yolg\u2018iz "
                     "qolib, egani kesimdan ajratib qo\u2018yadi. Aynan shu "
                     "darsning xatosi."),
                    (False, "tension —",
                     "<strong>aralashgan juft</strong> (43-dars): vergul "
                     "ochdi, tire yopyapti."),
                    (False, "tension;",
                     "nuqtali vergul qo\u2018shimchani yopa olmaydi va ikki "
                     "mustaqil gap talab qiladi."),
                ])
                + TIP.format(
                    "Ega bilan kesim orasida vergul ko\u2018rsangiz, darrov "
                    "\u00abxato\u00bb demang \u2014 avval <strong>ikkinchisini "
                    "qidiring</strong>. Bitta bo\u2018lsa xato; juft bo\u2018lsa "
                    "to\u2018g\u2018ri.")
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a subject</div><div class="pp-card-back">ega</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a predicate / main verb</div><div class="pp-card-back">kesim / asosiy fe\'l</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an object</div><div class="pp-card-back">to\'ldiruvchi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a pause is not a comma</div><div class="pp-card-back">pauza vergul degani emas</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cartographer</div><div class="pp-card-back">xaritachi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a headland</div><div class="pp-card-back">burun (dengizga chiqib turgan quruqlik)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a conservator</div><div class="pp-card-back">restavrator</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">consumption</div><div class="pp-card-back">iste\'mol</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li><strong>Ega ↔ kesim orasiga vergul qo'yilmaydi.</strong> "
              "Ega qanchalik uzun bo'lmasin.</li>"
              "<li>Kesim ↔ to'ldiruvchi va predlog ↔ oti orasiga ham "
              "qo'yilmaydi.</li>"
              "<li><strong>Pauza vergul emas</strong> — quloqqa "
              "ishonmang.</li>"
              "<li>Uzun egada asosiy kesimni toping: u nisbiy gap "
              "ichidagi fe'l emas.</li>"
              "<li>Yagona istisno: <u>ikki tomondan</u> yopilgan "
              "qo'shimcha (bitta vergul xato, ikkitasi to'g'ri).</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 45
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W45: Essential vs Non-Essential — The Comma That Changes the Meaning",
    "summary": "Vergul bo'lakni «qaysi biri» degan savolga javob beruvchidan "
               "«qo'shimcha ma'lumot» ga aylantiradi — va ma'no o'zgaradi.",
    "order": 45,
    "blocks": [
        {"rich_text": (
            "<h2>Vergul ma'noni o'zgartiradi</h2>"
            "<p>Bu mavzudagi eng nozik dars. Boshqa savollarda vergul "
            "to'g'ri yoki xato edi; bu yerda "
            "<mark>ikkala variant ham grammatik jihatdan to'g'ri</mark> — "
            "lekin ular <u>boshqa narsani anglatadi</u>.</p>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><em>The bells <u>that were "
                "recast in 1971</u> are rung on feast days.</em></p>"
                "<p style=\"margin:0 0 10px;\">→ minorada bir nechta "
                "qo'ng'iroq bor. Faqat <u>1971-yilda qayta quyilganlari</u> "
                "chalinadi. Bo'lak <strong>qaysi birini</strong> "
                "aytadi.</p>"
                "<p style=\"margin:0 0 6px;\"><em>The bells<strong>,</strong> "
                "<u>which were recast in 1971</u><strong>,</strong> are rung "
                "on feast days.</em></p>"
                "<p style=\"margin:0;\">→ qo'ng'iroqlar bitta guruh. "
                "Hammasi 1971-yilda qayta quyilgan, va hammasi chalinadi. "
                "Bo'lak <strong>qo'shimcha ma'lumot</strong>.</p>")
            + '<span class="sr-time">⏱ ~40 soniya</span>'
        )},

        {"rich_text": (
            "<h3>Ikki tur, ikki qoida</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th></th><th>Kerakli (essential)</th>"
              "<th>Keraksiz (non-essential)</th></tr></thead>"
              "<tbody>"
              "<tr><td>Vergul</td><td><strong>yo'q</strong></td>"
              "<td><strong>ikki tomondan</strong></td></tr>"
              "<tr><td>Vazifasi</td><td>«Qaysi biri?» ga javob beradi</td>"
              "<td>Qo'shimcha ma'lumot beradi</td></tr>"
              "<tr><td>Olib tashlansa</td><td>Ma'no <u>o'zgaradi</u></td>"
              "<td>Ma'no <u>saqlanadi</u></td></tr>"
              "<tr><td>Olmoshi</td><td><em>that</em> (yoki olmoshsiz)</td>"
              "<td><em>which</em> · <em>who</em></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "<strong>Eng tez belgisi: <em>that</em> hech qachon "
                "vergul olmaydi.</strong> Agar variantlarda "
                "<em>, that</em> bo'lsa — u deyarli har doim xato. "
                "<em>which</em> esa vergul bilan keladi (bo'lak "
                "qo'shimcha bo'lganda).")
        )},

        {"rich_text": (
            "<h3>Nomlar bilan ham shunday</h3>"
            + EXAMP.format(
                "<p style=\"margin:0 0 6px;\"><em>Her brother Karim lives in "
                "Nukus.</em> → uning bir nechta akasi bor; "
                "<u>Karim</u> degani Nukusda.</p>"
                "<p style=\"margin:0;\"><em>Her brother<strong>,</strong> "
                "Karim<strong>,</strong> lives in Nukus.</em> → uning bitta "
                "akasi bor, va uning ismi Karim.</p>")
            + "<p>Ikkovi ham to'g'ri gap. Qaysi biri kerakligini "
            "<mark>matnning qolgan qismi</mark> aytadi — masalan agar "
            "oldingi jumlada «uning yagona akasi» deyilgan bo'lsa, "
            "vergullar kerak.</p>"
        )},

        {"rich_text": (
            "<h3>Ishlangan namuna</h3>"
            + conv_q(
                "<p>The archive holds four ledgers from the mill. The ledger "
                "<span class=\"sr-blank\"></span> was kept by the owner's daughter and "
                "is the only one to record wages as well as output.</p>")
            + choices_html([
                "that survives from the 1840s",
                ", that survives from the 1840s,",
                ", which survives from the 1840s,",
                "which survives from the 1840s",
            ])
            + "<p><strong>Kontekstga qarang.</strong> Birinchi jumla to'rt "
            "daftar borligini aytadi. Demak <em>The ledger …</em> "
            "<u>qaysi birini</u> nazarda tutayotganini "
            "aniqlashi kerak.</p>"
            "<p>Bo'lak <mark>kerakli</mark> — u to'rttadan bittasini "
            "ajratadi. Demak vergul yo'q, va olmosh "
            "<em>that</em>.</p>"
            + why([
                (True, "that survives from the 1840s",
                 "kerakli bo'lak: vergulsiz va <em>that</em> bilan. U "
                 "to'rt daftardan qaysi biri haqida gap ketayotganini "
                 "aytadi."),
                (False, ", which survives from the 1840s,",
                 "grammatik jihatdan <u>to'g'ri</u> — lekin ma'nosi "
                 "boshqa: vergullar bo'lakni qo'shimcha qiladi, ya'ni "
                 "«daftar (aytgancha, u 1840-yillardan)». Bu birinchi "
                 "jumladagi <em>four ledgers</em> ga zid: qaysi biri "
                 "ekani noma'lum qoladi."),
                (False, ", that survives from the 1840s,",
                 "<strong><em>that</em> hech qachon vergul "
                 "olmaydi.</strong> Bu eng oson tanaladigan xato."),
                (False, "which survives from the 1840s",
                 "<em>which</em> vergulsiz — ikkalasi ham noto'g'ri "
                 "tomonda: <em>which</em> qo'shimcha bo'lak uchun, va "
                 "qo'shimcha bo'lak vergul talab qiladi."),
            ])
            + NOTE.format(
                "E'tibor bering: ikkinchi variant <u>xato emas</u> — u "
                "boshqa gap. Bu turdagi savollarda javobni "
                "<strong>oldingi jumla</strong> beradi, grammatika emas. "
                "Kontekstsiz ikkala variant ham to'g'ri bo'lardi.")
        )},

        {
            "rich_text": conv_q(
                "<p>Sea otters are the only marine mammal without a layer of blubber. "
                "Their fur <span class=\"sr-blank\"></span> traps a layer of air against "
                "the skin, and an otter that cannot groom it will die of cold in water "
                "it has lived in all its life.</p>"),
            "choices": [
                {"text": ", which is the densest of any animal's,", "is_correct": True},
                {"text": "which is the densest of any animal's", "is_correct": False},
                {"text": ", that is the densest of any animal's,", "is_correct": False},
                {"text": "that is the densest of any animal's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kerakli yoki keraksiz?</strong> Kalanning "
                "<u>bitta</u> mo'ynasi bor — «qaysi mo'ynasi?» degan "
                "savol ma'nosiz. Demak bo'lak "
                "<mark>qo'shimcha ma'lumot</mark>.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>Their fur "
                "traps a layer of air against the skin…</em> — gap butun "
                "va ma'no o'zgarmagan ✓</p>"
                + why([
                    (True, ", which is the densest of any animal's,",
                     "qo'shimcha bo'lak: <em>which</em> + ikki tomondan "
                     "vergul. Ikkala shart ham bajarilgan."),
                    (False, "which is the densest of any animal's",
                     "<em>which</em> to'g'ri, lekin vergullar yo'q — "
                     "qo'shimcha bo'lak ajratilmagan."),
                    (False, ", that is the densest of any animal's,",
                     "<strong><em>that</em> vergul olmaydi.</strong>"),
                    (False, "that is the densest of any animal's",
                     "<em>that</em> bo'lakni kerakli qiladi, ya'ni "
                     "«qaysi mo'ynasi?» — kalanda bitta mo'yna bor, "
                     "shuning uchun bu ma'nosiz."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The company employs three engineers, and only one of them has "
                "worked on a tunnel. The engineer <span class=\"sr-blank\"></span> was "
                "sent to the site on the first morning.</p>"),
            "choices": [
                {"text": "who had tunnelled before", "is_correct": True},
                {"text": ", who had tunnelled before,", "is_correct": False},
                {"text": ", who had tunnelled before", "is_correct": False},
                {"text": "who had tunnelled before,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kontekst:</strong> uchta muhandis bor, va faqat "
                "bittasi tunnelda ishlagan. Demak bo'lak "
                "<mark>qaysi birini</mark> aytadi — u "
                "<u>kerakli</u>.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>The engineer "
                "was sent to the site…</em> — qaysi muhandis? Ma'no "
                "yo'qoladi ✓ Demak bo'lak kerakli, vergulsiz.</p>"
                + why([
                    (True, "who had tunnelled before",
                     "kerakli bo'lak — vergulsiz. <em>who</em> odamlar "
                     "uchun kerakli bo'lakda ham ishlatiladi "
                     "(<em>that</em> kabi)."),
                    (False, ", who had tunnelled before,",
                     "vergullar bo'lakni qo'shimcha qiladi: «muhandis "
                     "(aytgancha, u ilgari tunnelda ishlagan)». Lekin unda "
                     "<u>qaysi</u> muhandis ekani noma'lum qoladi — "
                     "kontekst esa uchtasi borligini aytgan."),
                    (False, ", who had tunnelled before",
                     "yarim ochilgan juft: bitta vergul. Va u egani "
                     "kesimdan ajratib qo'yadi (44-dars)."),
                    (False, "who had tunnelled before,",
                     "yana yarim juft, teskari tomondan — ega "
                     "<em>The engineer who had tunnelled before</em> "
                     "kesimidan (<em>was sent</em>) vergul bilan "
                     "ajratilgan."),
                ])
            ),
        },

        {
            "rich_text": conv_q(
                "<p>Ulugh Beg had several sons, and the succession after his death was "
                "disputed for a decade. His son "
                "<span class=\"sr-blank\"></span> was the one who eventually held "
                "Samarkand, though not for long.</p>"),
            "choices": [
                {"text": "Abd al-Latif", "is_correct": True},
                {"text": ", Abd al-Latif,", "is_correct": False},
                {"text": ", Abd al-Latif", "is_correct": False},
                {"text": "Abd al-Latif,", "is_correct": False},
            ],
            "explanation": (
                "<p>Ism bilan ham xuddi shu qoida. <strong>Kontekst:</strong> "
                "<em>Ulugh Beg had several sons</em> — bir nechta "
                "o'g'il bor.</p>"
                "<p>Demak ism <mark>qaysi o'g'il</mark> ekanini aytadi — "
                "u <u>kerakli</u>, va vergul qo'yilmaydi.</p>"
                + why([
                    (True, "Abd al-Latif",
                     "vergulsiz: bir nechta o'g'ildan qaysi biri "
                     "ekanini aniqlaydi."),
                    (False, ", Abd al-Latif,",
                     "vergullar ismni qo'shimcha qiladi, ya'ni "
                     "«uning <u>yagona</u> o'g'li, ismi Abd al-Latif». "
                     "Bu birinchi jumlaga zid."),
                    (False, ", Abd al-Latif",
                     "yarim juft — va u egani kesimidan ajratadi."),
                    (False, "Abd al-Latif,",
                     "yana yarim juft, teskari tomondan."),
                ])
                + TIP.format(
                    "Bu turdagi savolda javob deyarli har doim "
                    "<strong>oldingi jumlada</strong> yotadi: "
                    "<em>four ledgers</em>, <em>three engineers</em>, "
                    "<em>several sons</em> — bir nechta bo'lsa, "
                    "bo'lak kerakli (vergulsiz); bitta bo'lsa, "
                    "qo'shimcha (vergul bilan). "
                    "<u>Grammatika emas, kontekst hal qiladi.</u>")
            ),
        },

        {
            "rich_text": conv_q(
                "<p>The city has kept only one of its medieval gates. The gate "
                "<span class=\"sr-blank\"></span> now carries a clock that is thirty "
                "years younger than the arch beneath it.</p>"),
            "choices": [
                {"text": ", which was rebuilt after a fire in 1892,", "is_correct": True},
                {"text": "that was rebuilt after a fire in 1892", "is_correct": False},
                {"text": ", that was rebuilt after a fire in 1892,", "is_correct": False},
                {"text": "which was rebuilt after a fire in 1892", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kontekst:</strong> <em>only one of its medieval "
                "gates</em> \u2014 darvoza <u>bitta</u>. Demak \u00abqaysi "
                "darvoza?\u00bb degan savol ma\u2019nosiz, va bo\u2018lak "
                "<mark>qo\u2018shimcha ma\u2019lumot</mark>.</p>"
                "<p><strong>Olib tashlash sinovi:</strong> <em>The gate now "
                "carries a clock\u2026</em> \u2014 gap butun, ma\u2019no "
                "o\u2018zgarmagan ✓</p>"
                + why([
                    (True, ", which was rebuilt after a fire in 1892,",
                     "qo\u2018shimcha bo\u2018lak: <em>which</em> + ikki tomondan "
                     "vergul. Ikkala shart ham bajarilgan."),
                    (False, "that was rebuilt after a fire in 1892",
                     "<em>that</em> bo\u2018lakni <u>kerakli</u> qiladi, ya\u2019ni "
                     "\u00abqaysi darvoza?\u00bb \u2014 lekin oldingi jumla "
                     "darvoza bitta ekanini aytgan. Kontekstga zid."),
                    (False, ", that was rebuilt after a fire in 1892,",
                     "<strong><em>that</em> hech qachon vergul "
                     "olmaydi.</strong>"),
                    (False, "which was rebuilt after a fire in 1892",
                     "<em>which</em> to\u2018g\u2018ri, lekin vergullar yo\u2018q \u2014 "
                     "qo\u2018shimcha bo\u2018lak ajratilmagan, va ega kesimidan "
                     "uzilib qoladi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">essential (restrictive)</div><div class="pp-card-back">kerakli bo\'lak — vergulsiz, «qaysi biri» ni aytadi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">non-essential (non-restrictive)</div><div class="pp-card-back">keraksiz bo\'lak — ikki tomondan vergul</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">that</div><div class="pp-card-back">kerakli bo\'lak uchun — HECH QACHON vergul olmaydi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">which</div><div class="pp-card-back">qo\'shimcha bo\'lak uchun — vergul bilan</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">blubber</div><div class="pp-card-back">dengiz hayvonlarining yog\' qatlami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to groom (fur)</div><div class="pp-card-back">(mo\'ynani) tozalab parvarish qilmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">the succession</div><div class="pp-card-back">taxt vorisligi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ledger</div><div class="pp-card-back">hisob daftari</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Vergul bo'lakni <strong>kerakli</strong> dan "
              "<strong>qo'shimcha</strong> ga aylantiradi — ma'no "
              "o'zgaradi.</li>"
              "<li>Kerakli → vergulsiz, <em>that</em>. Qo'shimcha → ikki "
              "vergul, <em>which</em>.</li>"
              "<li><strong><em>that</em> hech qachon vergul "
              "olmaydi.</strong></li>"
              "<li>Nomlar bilan ham shunday: <em>her brother Karim</em> ≠ "
              "<em>her brother, Karim,</em></li>"
              "<li>Javobni <strong>oldingi jumla</strong> beradi: bir "
              "nechtami yoki bittami?</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 46
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_PUNCT,
    "title": "SAT R&W W46: Punctuation Within the Sentence — Mixed Practice",
    "summary": "Oltita savol, barcha holatlar aralash: ikki nuqta, tire, juftlar, "
               "ega-kesim verguli va kerakli/keraksiz bo'laklar.",
    "order": 46,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy amaliyot</h2>"
            "<p>Oltita savol. Har birida shu uch qadam:</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><strong>1.</strong> Gapning boshiga "
                "qarang — ochilgan vergul, tire yoki qavs bormi? "
                "(43-dars)<br>"
                "<strong>2.</strong> Yo'q bo'lsa — ikki gap sinovi: chap "
                "to'liqmi? o'ng to'liqmi? (W30, 40-dars)<br>"
                "<strong>3.</strong> Egani va kesimni toping — orasida "
                "yolg'iz vergul bormi? (44-dars)</p>")
            + "<p>Taymer: <strong>3 daqiqa</strong> (6 × 30 soniya). Bu "
            "tur imtihonda eng tez yechiladiganlardan.</p>"
            + '<span class="sr-time">⏱ 6 savol · 3 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Punctuation") + conv_q(
                "<p>The suzani embroideries of Bukhara, worked by several women on "
                "separate panels and joined only at the "
                "<span class=\"sr-blank\"></span> carry small differences of dye lot "
                "that specialists now use to tell one hand from another.</p>"),
            "choices": [
                {"text": "end,", "is_correct": True},
                {"text": "end", "is_correct": False},
                {"text": "end —", "is_correct": False},
                {"text": "end;", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qarang:</strong> <em>The suzani "
                "embroideries of Bukhara<strong>,</strong> worked by…</em> — "
                "vergul bilan qo'shimcha ochilgan. Javob — vergul.</p>"
                + why([
                    (True, "end,", "juftning ikkinchi verguli."),
                    (False, "end —", "aralashgan juft (43-dars)."),
                    (False, "end;", "nuqtali vergul qo'shimchani yopa "
                                    "olmaydi."),
                    (False, "end", "juft yopilmagan, va birinchi vergul "
                                   "egani kesimidan ajratib qoladi "
                                   "(44-dars)."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Punctuation") + conv_q(
                "<p>A qanat falls only a few centimetres in a kilometre, and the "
                "surveyors who set that gradient out across broken ground had one "
                "instrument <span class=\"sr-blank\"></span> a bowl of water and a "
                "floating reed.</p>"),
            "choices": [
                {"text": ":", "is_correct": True},
                {"text": ",", "is_correct": False},
                {"text": ";", "is_correct": False},
                {"text": " and", "is_correct": False},
            ],
            "explanation": (
                "<p>Chap tomon to'liq gap ✓, va u <em>one instrument</em> "
                "deb <mark>e'lon qilyapti</mark>. O'ng tomon — ot "
                "birikmasi.</p>"
                + why([
                    (True, ":", "to'liq gapdan keyin e'lon qilingan "
                                "narsani ochadi (40-dars)."),
                    (False, ";", "nuqtali vergul o'ngdan mustaqil gap "
                                 "talab qiladi."),
                    (False, ",", "vergul mumkin, lekin <em>one "
                                 "instrument</em> ochilishini kutyapti — "
                                 "ikki nuqta aniqroq."),
                    (False, " and", "<em>and</em> ot birikmasini "
                                    "<em>had</em> ga ulay olmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Punctuation") + conv_q(
                "<p>The three surveys carried out on the pass between 1841 and 1847 "
                "<span class=\"sr-blank\"></span> disagreed about almost nothing except "
                "the height of one ridge.</p>"),
            "choices": [
                {"text": "", "is_correct": True},
                {"text": ",", "is_correct": False},
                {"text": " —", "is_correct": False},
                {"text": ";", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qarang:</strong> ochilgan belgi yo'q. "
                "<strong>Egani toping:</strong> <em>The three surveys "
                "carried out on the pass between 1841 and 1847</em>. "
                "<strong>Kesim:</strong> <em>disagreed</em>.</p>"
                "<p>Ega ↔ kesim orasiga hech narsa qo'yilmaydi "
                "(44-dars).</p>"
                + why([
                    (True, "", "belgisiz — ega darhol kesimga ulanadi."),
                    (False, ",", "<strong>ega ↔ kesim verguli</strong> — "
                                 "uzun ega pauza eshittiradi, lekin pauza "
                                 "vergul emas."),
                    (False, " —", "tire xuddi shu xatoni qiladi va "
                                  "ochilmagan juftni yopmoqchi "
                                  "bo'ladi."),
                    (False, ";", "nuqtali vergul ikki mustaqil gap talab "
                                 "qiladi; chap tomon faqat ega."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Punctuation") + conv_q(
                "<p>The laboratory keeps six sourdough cultures. The culture "
                "<span class=\"sr-blank\"></span> has been fed on the same rye flour "
                "since it arrived and has not changed its mixture of organisms in eleven "
                "years.</p>"),
            "choices": [
                {"text": "that came from the bakery in Tartu", "is_correct": True},
                {"text": ", which came from the bakery in Tartu,", "is_correct": False},
                {"text": ", that came from the bakery in Tartu,", "is_correct": False},
                {"text": "which came from the bakery in Tartu", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Kontekst:</strong> laboratoriyada <u>oltita</u> "
                "kultura bor. Demak bo'lak <mark>qaysi birini</mark> "
                "aytadi — u kerakli, vergulsiz, <em>that</em> bilan "
                "(45-dars).</p>"
                + why([
                    (True, "that came from the bakery in Tartu",
                     "kerakli bo'lak: vergulsiz + <em>that</em>."),
                    (False, ", which came from the bakery in Tartu,",
                     "grammatik jihatdan to'g'ri, lekin ma'nosi "
                     "boshqa — vergullar bo'lakni qo'shimcha qiladi va "
                     "qaysi kultura ekani noma'lum qoladi."),
                    (False, ", that came from the bakery in Tartu,",
                     "<em>that</em> vergul olmaydi."),
                    (False, "which came from the bakery in Tartu",
                     "<em>which</em> vergulsiz — ikkovi ham noto'g'ri "
                     "tomonda."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Punctuation") + conv_q(
                "<p>The Antonine Wall (built of turf, held for barely a generation and "
                "then abandoned to the <span class=\"sr-blank\"></span> has left almost "
                "nothing above ground, though its ditch can still be walked for "
                "kilometres.</p>"),
            "choices": [
                {"text": "weather)", "is_correct": True},
                {"text": "weather,", "is_correct": False},
                {"text": "weather —", "is_correct": False},
                {"text": "weather", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qarang:</strong> <em>The Antonine Wall "
                "<strong>(</strong>built of turf…</em> — qavs bilan "
                "ochilgan.</p>"
                "<p>Ichkaridagi vergullar (<em>turf, held…</em>) ro'yxat "
                "vergullari — ular juftga aloqador emas.</p>"
                + why([
                    (True, "weather)", "qavs bilan ochilgan qo'shimcha "
                                       "qavs bilan yopiladi."),
                    (False, "weather,", "aralashgan juft — va ichkaridagi "
                                        "vergullar buni jozibali "
                                        "qiladi."),
                    (False, "weather —", "yana aralashgan juft."),
                    (False, "weather", "qavs yopilmagan."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Punctuation") + conv_q(
                "<p>Bamboo scaffolding is lashed rather than bolted, and a joint that "
                "has been tied by hand can be untied and moved in "
                "<span class=\"sr-blank\"></span> a bolted joint has to be cut out.</p>"),
            "choices": [
                {"text": "minutes;", "is_correct": True},
                {"text": "minutes,", "is_correct": False},
                {"text": "minutes:", "is_correct": False},
                {"text": "minutes", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Boshiga qarang:</strong> ochilgan juft yo'q. "
                "<strong>Ikki gap sinovi:</strong> chap "
                "<em>…can be untied and moved in minutes</em> — mustaqil. "
                "O'ng <em>a bolted joint has to be cut out</em> — "
                "mustaqil.</p>"
                "<p>Ikki mustaqil gap, va ular "
                "<mark>qarama-qarshi qo'yilgan</mark>.</p>"
                + why([
                    (True, "minutes;",
                     "nuqtali vergul ikki zich bog'liq mustaqil gapni "
                     "ulaydi (W32)."),
                    (False, "minutes,",
                     "<strong>vergul splaysi</strong> (W31)."),
                    (False, "minutes:",
                     "ikki nuqta e'lon qiladi yoki izohlaydi; bu yerda "
                     "o'ng tomon izoh emas, <u>qarshi qo'yilgan</u> "
                     "holat."),
                    (False, "minutes",
                     "belgisiz <em>run-on</em>."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Xatoni turi bo'yicha tahlil qiling</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Xato turi</th><th>Qaysi darsga qaytish</th></tr></thead>"
              "<tbody>"
              "<tr><td>Ochilgan belgini sezmadim</td><td>43-dars — boshiga "
              "qayting</td></tr>"
              "<tr><td>Juftni aralashtirdim</td><td>43-dars</td></tr>"
              "<tr><td>Fe'l yoki predlogdan keyin ikki nuqta "
              "qo'ydim</td><td>40-dars</td></tr>"
              "<tr><td>Uzun egadan keyin vergul qo'ydim</td>"
              "<td>44-dars — pauza vergul emas</td></tr>"
              "<tr><td><em>that</em> ga vergul qo'ydim</td>"
              "<td>45-dars</td></tr>"
              "<tr><td>Kontekstni o'qimay kerakli/keraksizni "
              "tanladim</td><td>45-dars — oldingi jumla hal qiladi</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Bu mavzudagi savollar <strong>gapning ma'nosini "
                "tushunmasdan</strong> yechiladi — ochilgan belgi, ega, "
                "kesim. Yagona istisno 45-dars: u yerda javobni "
                "<u>oldingi jumla</u> beradi.")
        )},

        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">a dye lot</div><div class="pp-card-back">bir marta bo\'yalgan ip partiyasi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a gradient</div><div class="pp-card-back">nishablik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a ridge</div><div class="pp-card-back">tizma, cho\'qqi chizig\'i</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to lash / to bolt</div><div class="pp-card-back">bog\'lamoq / bolt bilan biriktirmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a culture (biology)</div><div class="pp-card-back">o\'stirilgan mikroorganizmlar to\'plami</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">rye flour</div><div class="pp-card-back">javdar uni</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to abandon to the weather</div><div class="pp-card-back">ochiq havoda tashlab ketmoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a joint</div><div class="pp-card-back">birikma, tutashuv joyi</div></div>'
            + "</div>"
            + "<h3>Xulosa — Tinish belgilari mavzusi yakuni</h3>"
            + "<ul>"
              "<li><strong>Ikki nuqtadan oldin to'liq gap</strong> — "
              "istisnosiz (40-dars).</li>"
              "<li>Yolg'iz tire ikki nuqta kabi; juft tire qo'shimchani "
              "o'raydi (41-dars).</li>"
              "<li><strong>Olib tashlash sinovi</strong> qo'shimchani "
              "aniqlaydi (42-dars).</li>"
              "<li><strong>Ochilgan belgi = yopiladigan belgi</strong> "
              "(43-dars).</li>"
              "<li>Ega ↔ kesim orasiga vergul qo'yilmaydi (44-dars).</li>"
              "<li>Kerakli bo'lak vergulsiz; javobni kontekst beradi "
              "(45-dars).</li>"
              "</ul>"
        )},
    ],
},

]
