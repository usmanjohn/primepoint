"""
IELTS Writing lessons 7-8 (orders 20-21) — the "1-topshiriq (Academic): Jarayon va
xarita (Task 1 Academic — Process & Maps)" topic — third Writing batch,
see toc_ielts_writing.txt.

No audio. Two hand-built inline SVGs (single-quoted attrs; overflow-x:auto): a 6-stage
process-flow diagram and a before/after map pair. Kit: step-reveal (model answer) +
flashcards + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_T1_PROCESS = {
    "title":   "1-topshiriq (Academic): Jarayon va xarita (Task 1 Academic — Process & Maps)",
    "summary": "Jarayon diagrammasi (passive + ketma-ketlik tili) va xaritalarni "
               "(oldin/keyin o'zgarish tili) tavsiflash.",
    "icon":    "bi-diagram-3",
    "order":   3,
}

# ── inline SVGs ──────────────────────────────────────────────────────────────
PROCESS_SVG = (
    "<div style=\"overflow-x:auto;\">"
    "<svg viewBox='0 0 470 170' style='width:100%;max-width:460px;height:auto;display:block;margin:8px auto;font-family:sans-serif;font-size:10px;'>"
    "<text x='235' y='12' text-anchor='middle' font-weight='bold' fill='#334155' font-size='12'>How recycled paper is produced</text>"
    "<rect x='12' y='24' width='118' height='44' rx='6' fill='#ecfdf5' stroke='#059669' stroke-width='1.5'/>"
    "<text x='71' y='42' text-anchor='middle' fill='#334155'>1. Waste paper</text><text x='71' y='56' text-anchor='middle' fill='#334155'>collected</text>"
    "<rect x='176' y='24' width='118' height='44' rx='6' fill='#ecfdf5' stroke='#059669' stroke-width='1.5'/>"
    "<text x='235' y='42' text-anchor='middle' fill='#334155'>2. Sorted</text><text x='235' y='56' text-anchor='middle' fill='#334155'>by type</text>"
    "<rect x='340' y='24' width='118' height='44' rx='6' fill='#ecfdf5' stroke='#059669' stroke-width='1.5'/>"
    "<text x='399' y='42' text-anchor='middle' fill='#334155'>3. Shredded into</text><text x='399' y='56' text-anchor='middle' fill='#334155'>small pieces</text>"
    "<text x='153' y='52' text-anchor='middle' fill='#059669' font-size='20'>&#8594;</text>"
    "<text x='317' y='52' text-anchor='middle' fill='#059669' font-size='20'>&#8594;</text>"
    "<text x='399' y='90' text-anchor='middle' fill='#059669' font-size='20'>&#8595;</text>"
    "<rect x='340' y='96' width='118' height='44' rx='6' fill='#eff6ff' stroke='#3b82f6' stroke-width='1.5'/>"
    "<text x='399' y='114' text-anchor='middle' fill='#334155'>4. Mixed with water</text><text x='399' y='128' text-anchor='middle' fill='#334155'>to form pulp</text>"
    "<rect x='176' y='96' width='118' height='44' rx='6' fill='#eff6ff' stroke='#3b82f6' stroke-width='1.5'/>"
    "<text x='235' y='114' text-anchor='middle' fill='#334155'>5. Cleaned to</text><text x='235' y='128' text-anchor='middle' fill='#334155'>remove ink</text>"
    "<rect x='12' y='96' width='118' height='44' rx='6' fill='#eff6ff' stroke='#3b82f6' stroke-width='1.5'/>"
    "<text x='71' y='114' text-anchor='middle' fill='#334155'>6. Pressed &amp; dried</text><text x='71' y='128' text-anchor='middle' fill='#334155'>into new sheets</text>"
    "<text x='317' y='126' text-anchor='middle' fill='#3b82f6' font-size='20'>&#8592;</text>"
    "<text x='153' y='126' text-anchor='middle' fill='#3b82f6' font-size='20'>&#8592;</text>"
    "</svg></div>"
)

MAPS_SVG = (
    "<div style=\"overflow-x:auto;\">"
    "<svg viewBox='0 0 470 240' style='width:100%;max-width:460px;height:auto;display:block;margin:8px auto;font-family:sans-serif;font-size:10px;'>"
    # left map 1990
    "<text x='115' y='16' text-anchor='middle' font-weight='bold' fill='#334155' font-size='12'>The area in 1990</text>"
    "<rect x='15' y='24' width='200' height='200' fill='#f8fafc' stroke='#94a3b8' stroke-width='1.5'/>"
    "<ellipse cx='70' cy='75' rx='38' ry='24' fill='#bae6fd' stroke='#0284c7'/>"
    "<text x='70' y='79' text-anchor='middle' fill='#0369a1'>Lake</text>"
    "<rect x='120' y='50' width='85' height='75' fill='#dcfce7' stroke='#16a34a'/>"
    "<circle cx='140' cy='75' r='9' fill='#22c55e'/><circle cx='165' cy='92' r='9' fill='#22c55e'/><circle cx='188' cy='70' r='9' fill='#22c55e'/>"
    "<text x='162' y='118' text-anchor='middle' fill='#166534'>Forest</text>"
    "<rect x='15' y='196' width='200' height='16' fill='#cbd5e1'/>"
    "<text x='115' y='208' text-anchor='middle' fill='#475569'>Main Road</text>"
    # right map 2020
    "<text x='355' y='16' text-anchor='middle' font-weight='bold' fill='#334155' font-size='12'>The area in 2020</text>"
    "<rect x='255' y='24' width='200' height='200' fill='#f8fafc' stroke='#94a3b8' stroke-width='1.5'/>"
    "<ellipse cx='310' cy='75' rx='38' ry='24' fill='#bae6fd' stroke='#0284c7'/>"
    "<text x='310' y='79' text-anchor='middle' fill='#0369a1'>Lake</text>"
    "<rect x='360' y='50' width='85' height='75' fill='#fef3c7' stroke='#d97706'/>"
    "<rect x='368' y='58' width='15' height='15' fill='#fbbf24'/><rect x='389' y='58' width='15' height='15' fill='#fbbf24'/><rect x='410' y='58' width='15' height='15' fill='#fbbf24'/>"
    "<rect x='368' y='82' width='15' height='15' fill='#fbbf24'/><rect x='389' y='82' width='15' height='15' fill='#fbbf24'/><rect x='410' y='82' width='15' height='15' fill='#fbbf24'/>"
    "<text x='402' y='118' text-anchor='middle' fill='#92400e'>Houses</text>"
    "<rect x='255' y='196' width='200' height='16' fill='#cbd5e1'/>"
    "<rect x='332' y='100' width='13' height='96' fill='#cbd5e1'/>"
    "<text x='355' y='150' text-anchor='middle' fill='#475569' font-size='9'>new road</text>"
    "<rect x='268' y='150' width='48' height='34' fill='#e9d5ff' stroke='#7c3aed'/>"
    "<text x='292' y='170' text-anchor='middle' fill='#6b21a8'>School</text>"
    "</svg></div>"
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 7 (order 20 — process diagram: passive + sequencing)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_PROCESS,
    "title": "IELTS Writing 7: Describing a Process Diagram — Sequencing & the Passive Voice",
    "summary": "Jarayon diagrammasi: bosqichlarni tartib bilan tavsiflash — passive voice (is/are + V3) va ketma-ketlik so'zlari (first, then, once, finally).",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Jarayon diagrammasi — qanday yasaladi/ishlaydi</h2>"
            "<p>Jarayon (process) diagrammasi biror narsa <strong>qanday "
            "tayyorlanishini</strong> yoki <strong>qanday ishlashini</strong> bosqichma-"
            "bosqich ko'rsatadi. Trend yoki taqqoslash yo'q — sizga <mark "
            "style=\"background:#dbeafe;\">bosqichlarni tartib bilan</mark> tavsiflash "
            "kerak. Ikki til vositasi hal qiluvchi: <strong>passive voice</strong> va "
            "<strong>ketma-ketlik so'zlari</strong>.</p>"
        )},
        {"rich_text": (
            "<h3>Nega passive voice?</h3>"
            "<p>Jarayonda <u>KIM</u> bajarishi muhim emas — MUHIMI nima sodir bo'lishi. "
            "Shuning uchun passive: <em>is/are + fe'lning 3-shakli (V3)</em>.</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\">❌ Active: <em>\"Workers collect the paper and then they sort it.\"</em> — kim (workers) ortiqcha.</p>"
            "<p style=\"margin:0;\">✅ Passive: <em>\"The paper <u>is collected</u> and then <u>is sorted</u>.\"</em> — jarayonga e'tibor.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Passive shakllari:</strong> is collected, are mixed, is shredded. "
            "Perfect passive: <em>\"Once it <u>has been sorted</u>, the paper is "
            "shredded.\"</em> (bir bosqich tugagach, keyingisi).</div>"
        )},
        {"rich_text": (
            "<h3>Ketma-ketlik (sequencing) so'zlari</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Boshlash:</strong> First / First of all / To begin with / Initially</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Davom:</strong> Then / Next / After that / Subsequently / Following this</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Bosqich tugagach:</strong> Once ... has been ... / After ... is ... / At this stage</p>"
            "<p style=\"margin:0;\"><strong>Yakun:</strong> Finally / Lastly / In the final stage</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna jarayon</h3>"
            + PROCESS_SVG +
            "<p>Bu diagramma qayta ishlangan qog'oz qanday ishlab chiqarilishini 6 "
            "bosqichda ko'rsatadi. Endi 4 qismli tuzilmada yozamiz — model javobni "
            "bosqichma-bosqich oching:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qismni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"The diagram "
            "illustrates the various stages involved in the production of recycled "
            "paper.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Overview:</strong> <em>\"Overall, the "
            "process consists of six main stages, beginning with the collection of used "
            "paper and ending with the production of new sheets. It is a linear process "
            "that requires no natural inputs beyond water.\"</em><br>"
            "<span style=\"color:#475569;\">Overview = bosqichlar SONI + boshlanish/yakun + "
            "chiziqli(linear)mi. Raqamsiz.</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1:</strong> <em>\"First, waste paper "
            "is collected and then sorted according to its type. Once it has been sorted, "
            "the paper is shredded into small pieces.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2:</strong> <em>\"These pieces are "
            "subsequently mixed with water to form a pulp, which is then cleaned to "
            "remove any ink. Finally, the clean pulp is pressed and dried, producing new "
            "sheets of paper.\"</em><br>"
            "<span style=\"color:#475569;\">Passive (is collected, are mixed, is pressed) "
            "+ sequencing (First, then, Once, subsequently, Finally) har jumlada.</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Jarayon diagrammasi uchun qaysi gap eng "
                "mos?</p>"
            ),
            "choices": [
                {"text": "\"The workers put the paper in a machine and they add water.\"", "is_correct": False},
                {"text": "\"The shredded paper is then mixed with water to form a pulp.\"", "is_correct": True},
                {"text": "\"I think they add water at this stage.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "Passive voice (\"is mixed\") + sequencing (\"then\") — jarayonga e'tibor, "
                "kim bajarishi emas. Birinchisi — active (\"workers put... they add\"), "
                "jarayon uchun mos emas; uchinchisi — fikr (\"I think\").</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bo'sh joyni to'ldiring: \"______ the "
                "pulp has been cleaned, it is pressed into sheets.\"</p>"
            ),
            "choices": [
                {"text": "Once", "is_correct": True},
                {"text": "Because", "is_correct": False},
                {"text": "Although", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Once.</mark> "
                "\"Once ... has been ...\" — bir bosqich tugagach keyingisi (ketma-ketlik). "
                "\"Because\" (sabab) va \"Although\" (qarshilik) jarayon tartibiga mos "
                "emas. \"Once + perfect passive\" — jarayon tavsifining kuchli tuzilmasi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Jarayon diagrammasining overview'sida "
                "nima bo'lishi kerak?</p>"
            ),
            "choices": [
                {"text": "Har bosqichning aniq tafsilotlari", "is_correct": False},
                {"text": "Bosqichlar soni, boshlanish/yakun nuqtasi va jarayon chiziqlimi yoki tsiklik ekani", "is_correct": True},
                {"text": "Jarayon nima uchun foydali ekani (fikr)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: bosqichlar soni + "
                "boshlanish/yakun + linear/cyclical.</mark> Jarayon overview'i umumiy "
                "manzarani beradi: nechta bosqich, nimadan boshlanib nima bilan tugaydi, "
                "chiziqlimi yoki takrorlanuvchi (tsikl)mi. Aniq tafsilotlar body'ga, "
                "fikr esa umuman Task 1'ga tegishli emas.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a stage / a step</div><div class=\"pp-card-back\">bosqich, qadam</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the passive voice</div><div class=\"pp-card-back\">majhul nisbat (is/are + V3)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Once ... has been ...</div><div class=\"pp-card-back\">... tugagach (ketma-ketlik)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">subsequently</div><div class=\"pp-card-back\">keyinchalik, so'ngra</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a linear process</div><div class=\"pp-card-back\">chiziqli jarayon</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a cyclical process</div><div class=\"pp-card-back\">tsiklik (takrorlanuvchi) jarayon</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be involved in</div><div class=\"pp-card-back\">... da ishtirok etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">raw material</div><div class=\"pp-card-back\">xomashyo</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Jarayon = bosqichlarni tartib bilan tavsiflash; kim bajarishi muhim emas.</li>"
            "<li>Passive voice (is/are + V3); \"Once ... has been ...\" bosqich tugashini bildiradi.</li>"
            "<li>Ketma-ketlik: First, Then, Next, Subsequently, Finally.</li>"
            "<li>Overview: bosqichlar soni + boshlanish/yakun + chiziqli/tsiklik (raqamsiz).</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 8 (order 21 — maps: before/after change language)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_PROCESS,
    "title": "IELTS Writing 8: Describing Maps — Before/After Change Language",
    "summary": "Ikki xaritani (oldin/keyin) taqqoslash: o'zgarish tili (was replaced by, converted into, demolished, remained unchanged), passive va o'tgan zamon.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Xaritalar — joyning o'zgarishi</h2>"
            "<p>Task 1'da ba'zan biror joyning <strong>ikki (yoki uch) davrdagi</strong> "
            "xaritasi beriladi. Vazifa — <mark style=\"background:#dbeafe;\">"
            "o'zgarishlarni</mark> tavsiflash: nima qo'shildi, olib tashlandi, "
            "almashtirildi, kengaytirildi yoki o'zgarmay qoldi. Bu — o'zgarish tili va "
            "to'g'ri zamon sinovi.</p>"
        )},
        {"rich_text": (
            "<h3>Zamon va passive</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Ikkala sana ham o'tgan (masalan 1990 → 2010):</strong> Past Simple passive — <em>was/were + V3</em>: \"a school <u>was built</u>\".</p>"
            "<p style=\"margin:0 0 6px;\"><strong>O'tmishdan hozirgacha:</strong> Present Perfect passive — <em>has/have been + V3</em>: \"the factory <u>has been demolished</u>\".</p>"
            "<p style=\"margin:0;\"><strong>Kelajak (masalan hozir → 2040):</strong> future — \"a bridge <u>will be constructed</u>\".</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — joy tili:</strong> Listening'dagi kabi yo'nalish so'zlari "
            "kerak: <em>in the north / to the east / in the south-western corner / next "
            "to / on the site of</em>. O'zgarish qayerda sodir bo'lganini aniq ayting.</div>"
        )},
        {"rich_text": (
            "<h3>O'zgarish tili (change language)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Qo'shildi:</strong> was built / constructed / added; a new X appeared</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Olib tashlandi:</strong> was demolished / knocked down / removed / cleared</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Almashtirildi:</strong> was replaced by / was converted into / gave way to / was transformed into</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Kengaytirildi:</strong> was extended / expanded / enlarged / widened</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Ko'chirildi:</strong> was relocated / was moved to</p>"
            "<p style=\"margin:0;\"><strong>O'zgarmadi:</strong> remained unchanged / was left untouched</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — oldin/keyin xaritalari</h3>"
            + MAPS_SVG +
            "<p>Bu ikki xarita bir hududni 1990 va 2020 yillarda ko'rsatadi. Model "
            "javobni bosqichma-bosqich oching:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qismni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"The two maps "
            "illustrate how a particular area changed between 1990 and 2020.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Overview:</strong> <em>\"Overall, the area "
            "became considerably more residential over the period, as green space gave "
            "way to housing and new facilities were introduced, although the lake "
            "remained unchanged.\"</em><br>"
            "<span style=\"color:#475569;\">Overview = umumiy o'zgarish (yashillik → "
            "turar-joy), tafsilotsiz.</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1:</strong> <em>\"In 1990, a large "
            "forest occupied the eastern side of the area, beside a lake in the "
            "north-west. By 2020, this forest had been cleared and replaced by rows of "
            "houses.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2:</strong> <em>\"In addition, a new "
            "road was constructed running north to south, connecting to the existing main "
            "road, and a school was built in the south-western corner. The lake, however, "
            "was left untouched.\"</em></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> O'rmon o'rnida uylar paydo bo'ldi. Qaysi "
                "gap eng aniq?</p>"
            ),
            "choices": [
                {"text": "\"The forest was replaced by houses.\"", "is_correct": True},
                {"text": "\"The forest makes houses.\"", "is_correct": False},
                {"text": "\"There are houses and a forest.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"was replaced "
                "by\".</mark> O'zgarish tili + passive: bir narsa o'rnini boshqasi egalladi. "
                "\"makes houses\" — mantiqsiz; \"there are houses and a forest\" — "
                "o'zgarishni ko'rsatmaydi (o'rmon endi yo'q). Muqobil: \"gave way to / "
                "was converted into\".</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Ikkala sana ham o'tmishda (1990 va "
                "2010). \"A new school ______ near the lake.\" Bo'sh joyga qaysi?</p>"
            ),
            "choices": [
                {"text": "was built", "is_correct": True},
                {"text": "is built", "is_correct": False},
                {"text": "builds", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: was built.</mark> "
                "Ikki sana ham o'tmishda → <u>Past Simple passive</u> (was/were + V3): "
                "\"was built\". \"is built\" (hozirgi) va \"builds\" (active hozirgi) — "
                "zamon xato. Maps'da odatda passive + o'tgan zamon.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Ko'l ikkala xaritada ham bir xil — "
                "o'zgarmagan. Buni qanday ifodalash kerak?</p>"
            ),
            "choices": [
                {"text": "Yozmaslik — o'zgarmagan narsani aytish shart emas", "is_correct": False},
                {"text": "\"The lake remained unchanged / was left untouched.\"", "is_correct": True},
                {"text": "\"The lake was demolished.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"remained "
                "unchanged\".</mark> O'zgarmagan muhim obyektni ham aytish yaxshi — bu "
                "to'liqlikni (Task Achievement) ko'rsatadi va \"remained unchanged / was "
                "left untouched\" kabi iboralar lug'atni boyitadi. \"was demolished\" — "
                "faktga zid (ko'l joyida turibdi).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Change language</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">was replaced by</div><div class=\"pp-card-back\">... bilan almashtirildi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">was converted into</div><div class=\"pp-card-back\">... ga aylantirildi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">was demolished / knocked down</div><div class=\"pp-card-back\">buzib tashlandi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">gave way to</div><div class=\"pp-card-back\">... ga o'rin bo'shatdi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">was extended / widened</div><div class=\"pp-card-back\">kengaytirildi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">remained unchanged</div><div class=\"pp-card-back\">o'zgarmay qoldi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on the site of</div><div class=\"pp-card-back\">... o'rnida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">residential / green space</div><div class=\"pp-card-back\">turar-joy / yashil maydon</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Maps = o'zgarishni tavsiflash: qo'shildi / olib tashlandi / almashtirildi / o'zgarmadi.</li>"
            "<li>Zamon: ikki o'tmish → Past passive (was built); o'tmish→hozir → Present Perfect (has been built).</li>"
            "<li>Joy tili: in the north, to the east, in the corner, on the site of.</li>"
            "<li>Overview: umumiy o'zgarish (masalan yashillik → turar-joy); o'zgarmaganini ham ayting.</li>"
            "</ul>"
        )},
    ],
},

]
