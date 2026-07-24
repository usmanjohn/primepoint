"""
IELTS Writing lessons 3-6 (orders 10-13) — the "1-topshiriq (Academic): Grafik va
diagrammalar (Task 1 Academic — Graphs & Charts)" topic — second Writing batch,
see toc_ielts_writing.txt.

No audio. Each lesson embeds a hand-built inline SVG chart (single-quoted attrs so they
don't clash with the Python double-quoted strings; wrapped in overflow-x:auto for mobile).
Kit: step-reveal (unfold model answers) + flashcards (trend/comparison vocab) + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_T1_GRAPHS = {
    "title":   "1-topshiriq (Academic): Grafik va diagrammalar (Task 1 Academic — Graphs & Charts)",
    "summary": "Task 1 Academic: grafik, ustunli/doiraviy diagramma va jadvallarni "
               "tavsiflash — tuzilma, trend va taqqoslash lug'ati (fikrsiz, bashoratsiz).",
    "icon":    "bi-bar-chart",
    "order":   2,
}

# ── hand-built inline SVG charts ─────────────────────────────────────────────
_SVG_OPEN = ("<div style=\"overflow-x:auto;\"><svg viewBox='0 0 470 300' "
             "style='width:100%;max-width:460px;height:auto;display:block;margin:8px auto;"
             "font-family:sans-serif;font-size:11px;'>")
_SVG_CLOSE = "</svg></div>"

CHART_LINE = (
    _SVG_OPEN +
    "<text x='240' y='16' text-anchor='middle' font-weight='bold' fill='#334155'>Museum visitors (thousands), 2010-2020</text>"
    "<line x1='60' y1='40' x2='60' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<line x1='60' y1='250' x2='440' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<line x1='60' y1='40' x2='440' y2='40' stroke='#eef2f6'/><text x='54' y='44' text-anchor='end' fill='#64748b'>100</text>"
    "<line x1='60' y1='82' x2='440' y2='82' stroke='#eef2f6'/><text x='54' y='86' text-anchor='end' fill='#64748b'>80</text>"
    "<line x1='60' y1='124' x2='440' y2='124' stroke='#eef2f6'/><text x='54' y='128' text-anchor='end' fill='#64748b'>60</text>"
    "<line x1='60' y1='166' x2='440' y2='166' stroke='#eef2f6'/><text x='54' y='170' text-anchor='end' fill='#64748b'>40</text>"
    "<line x1='60' y1='208' x2='440' y2='208' stroke='#eef2f6'/><text x='54' y='212' text-anchor='end' fill='#64748b'>20</text>"
    "<text x='54' y='254' text-anchor='end' fill='#64748b'>0</text>"
    "<text x='60' y='266' text-anchor='middle' fill='#64748b'>2010</text>"
    "<text x='134' y='266' text-anchor='middle' fill='#64748b'>2012</text>"
    "<text x='208' y='266' text-anchor='middle' fill='#64748b'>2014</text>"
    "<text x='282' y='266' text-anchor='middle' fill='#64748b'>2016</text>"
    "<text x='356' y='266' text-anchor='middle' fill='#64748b'>2018</text>"
    "<text x='430' y='266' text-anchor='middle' fill='#64748b'>2020</text>"
    "<polyline points='60,208 134,187 208,134 282,155 356,113 430,71' fill='none' stroke='#059669' stroke-width='2.5'/>"
    "<circle cx='60' cy='208' r='3.5' fill='#059669'/>"
    "<circle cx='134' cy='187' r='3.5' fill='#059669'/>"
    "<circle cx='208' cy='134' r='3.5' fill='#059669'/>"
    "<circle cx='282' cy='155' r='3.5' fill='#059669'/>"
    "<circle cx='356' cy='113' r='3.5' fill='#059669'/>"
    "<circle cx='430' cy='71' r='3.5' fill='#059669'/>"
    + _SVG_CLOSE
)

CHART_BAR = (
    _SVG_OPEN +
    "<text x='240' y='16' text-anchor='middle' font-weight='bold' fill='#334155'>Average daily screen time (hours) by age group</text>"
    "<line x1='60' y1='40' x2='60' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<line x1='60' y1='250' x2='440' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<text x='54' y='44' text-anchor='end' fill='#64748b'>8</text>"
    "<text x='54' y='96' text-anchor='end' fill='#64748b'>6</text>"
    "<text x='54' y='149' text-anchor='end' fill='#64748b'>4</text>"
    "<text x='54' y='201' text-anchor='end' fill='#64748b'>2</text>"
    "<text x='54' y='254' text-anchor='end' fill='#64748b'>0</text>"
    "<rect x='85' y='92' width='50' height='158' fill='#059669'/>"
    "<rect x='165' y='119' width='50' height='131' fill='#10b981'/>"
    "<rect x='245' y='145' width='50' height='105' fill='#34d399'/>"
    "<rect x='325' y='184' width='50' height='66' fill='#6ee7b7'/>"
    "<text x='110' y='86' text-anchor='middle' fill='#334155' font-weight='bold'>6</text>"
    "<text x='190' y='113' text-anchor='middle' fill='#334155' font-weight='bold'>5</text>"
    "<text x='270' y='139' text-anchor='middle' fill='#334155' font-weight='bold'>4</text>"
    "<text x='350' y='178' text-anchor='middle' fill='#334155' font-weight='bold'>2.5</text>"
    "<text x='110' y='266' text-anchor='middle' fill='#64748b'>10-19</text>"
    "<text x='190' y='266' text-anchor='middle' fill='#64748b'>20-39</text>"
    "<text x='270' y='266' text-anchor='middle' fill='#64748b'>40-59</text>"
    "<text x='350' y='266' text-anchor='middle' fill='#64748b'>60+</text>"
    + _SVG_CLOSE
)

CHART_PIE = (
    _SVG_OPEN +
    "<text x='150' y='16' text-anchor='middle' font-weight='bold' fill='#334155'>Household energy use by source</text>"
    "<path d='M150,155 L150,65 A90,90 0 0 1 177.8,240.6 Z' fill='#059669'/>"
    "<path d='M150,155 L177.8,240.6 A90,90 0 0 1 64.4,182.8 Z' fill='#10b981'/>"
    "<path d='M150,155 L64.4,182.8 A90,90 0 0 1 97.1,82.2 Z' fill='#34d399'/>"
    "<path d='M150,155 L97.1,82.2 A90,90 0 0 1 150,65 Z' fill='#a7f3d0'/>"
    "<text x='203' y='151' text-anchor='middle' fill='#fff' font-weight='bold'>45%</text>"
    "<text x='125' y='207' text-anchor='middle' fill='#fff' font-weight='bold'>25%</text>"
    "<text x='99' y='142' text-anchor='middle' fill='#334155' font-weight='bold'>20%</text>"
    "<text x='133' y='108' text-anchor='middle' fill='#334155' font-weight='bold'>10%</text>"
    "<rect x='300' y='75' width='14' height='14' fill='#059669'/><text x='320' y='87' fill='#334155'>Heating (45%)</text>"
    "<rect x='300' y='100' width='14' height='14' fill='#10b981'/><text x='320' y='112' fill='#334155'>Appliances (25%)</text>"
    "<rect x='300' y='125' width='14' height='14' fill='#34d399'/><text x='320' y='137' fill='#334155'>Water heating (20%)</text>"
    "<rect x='300' y='150' width='14' height='14' fill='#a7f3d0'/><text x='320' y='162' fill='#334155'>Lighting (10%)</text>"
    + _SVG_CLOSE
)

CHART_MULTILINE = (
    _SVG_OPEN +
    "<text x='240' y='16' text-anchor='middle' font-weight='bold' fill='#334155'>Hot drink consumption (cups/person/week), 2000-2020</text>"
    "<line x1='60' y1='40' x2='60' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<line x1='60' y1='250' x2='440' y2='250' stroke='#94a3b8' stroke-width='1.5'/>"
    "<text x='54' y='44' text-anchor='end' fill='#64748b'>16</text>"
    "<text x='54' y='96' text-anchor='end' fill='#64748b'>12</text>"
    "<text x='54' y='149' text-anchor='end' fill='#64748b'>8</text>"
    "<text x='54' y='201' text-anchor='end' fill='#64748b'>4</text>"
    "<text x='54' y='254' text-anchor='end' fill='#64748b'>0</text>"
    "<text x='80' y='266' text-anchor='middle' fill='#64748b'>2000</text>"
    "<text x='250' y='266' text-anchor='middle' fill='#64748b'>2010</text>"
    "<text x='420' y='266' text-anchor='middle' fill='#64748b'>2020</text>"
    "<polyline points='80,184 250,145 420,92' fill='none' stroke='#059669' stroke-width='2.5'/>"
    "<circle cx='80' cy='184' r='3.5' fill='#059669'/><circle cx='250' cy='145' r='3.5' fill='#059669'/><circle cx='420' cy='92' r='3.5' fill='#059669'/>"
    "<polyline points='80,66 250,119 420,158' fill='none' stroke='#f59e0b' stroke-width='2.5' stroke-dasharray='5 3'/>"
    "<circle cx='80' cy='66' r='3.5' fill='#f59e0b'/><circle cx='250' cy='119' r='3.5' fill='#f59e0b'/><circle cx='420' cy='158' r='3.5' fill='#f59e0b'/>"
    "<rect x='150' y='38' width='16' height='4' fill='#059669'/><text x='170' y='45' fill='#334155'>Coffee</text>"
    "<rect x='250' y='38' width='16' height='4' fill='#f59e0b'/><text x='270' y='45' fill='#334155'>Tea</text>"
    + _SVG_CLOSE
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 3 (order 10 — Task 1 structure: overview + key features)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_GRAPHS,
    "title": "IELTS Writing 3: Task 1 Academic Structure — Overview + Key Features",
    "summary": "Task 1 Academic 4 qismli tuzilma: kirish (paraphrase) + overview (asosiy trendlar) + 2 tafsilot paragrafi; fikr yoki bashorat YO'Q.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Task 1 Academic — nima qilish kerak</h2>"
            "<p>Task 1 Academic'da sizga grafik, diagramma yoki jadval beriladi va siz "
            "<strong>uni tavsiflaysiz</strong> — asosiy ma'lumotni tanlab, aniq, rasmiy "
            "tilda yozasiz. Bu insho EMAS: <mark style=\"background:#fee2e2;\">fikr "
            "bildirmang, sabab izlamang, bashorat qilmang</mark>. Faqat grafikda nima "
            "ko'rsatilganini yozing.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Eng ko'p uchraydigan xato:</strong> \"I think visitors rose "
            "because the museum improved\" — bu ikki xato: (1) <u>I think</u> (shaxsiy "
            "fikr), (2) <u>because...</u> (sabab — grafikda yo'q). Faqat: \"Visitor "
            "numbers rose.\" Grafik nimani KO'RSATSA, o'shani yozing.</div>"
        )},
        {"rich_text": (
            "<h3>4 qismli tuzilma</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Introduction (1 gap).</strong> "
            "Savoldagi grafik tavsifini <u>o'z so'zingiz bilan</u> qayta yozing "
            "(paraphrase). \"The graph shows...\" → \"The line graph illustrates...\". "
            "Savolni ko'chirib olmang.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Overview (1–2 gap) — ENG MUHIM.</strong> "
            "Grafikning <u>2–3 ta eng katta umumiy xususiyatini</u> raqamsiz ayting: "
            "umumiy trend qanday (o'sdimi/tushdimi?), eng yuqori/past nima. Overview'siz "
            "band 6 dan oshmaydi!</p></div>"
            "<div class=\"pp-step\"><p><strong>3–4. Body paragraphs (2 paragraf).</strong> "
            "Endi <u>aniq raqamlar</u> bilan tafsilotlarni bering. Ma'lumotni mantiqan "
            "guruhlang (masalan: yuqori qiymatlar bitta paragrafda, past qiymatlar "
            "boshqasida; yoki birinchi yarim davr / ikkinchi yarim davr).</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> Overview — bandingizni belgilaydigan qism. U "
            "ko'pincha <em>\"Overall,...\"</em> so'zi bilan boshlanadi va <u>raqam "
            "ishlatmaydi</u> — faqat umumiy manzara.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna grafik</h3>"
            + CHART_LINE +
            "<p>Ushbu chiziqli grafik 2010–2020 yillarda muzey tashrifchilari sonini "
            "(minglab) ko'rsatadi. Endi buni 4 qismli tuzilmada yozamiz.</p>"
        )},
        {"rich_text": (
            "<h3>Model javob — qism-qism oching</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qismni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"The line "
            "graph illustrates the number of visitors, in thousands, to a particular "
            "museum over a ten-year period from 2010 to 2020.\"</em><br>"
            "<span style=\"color:#475569;\">\"shows\" → \"illustrates\", \"visitors\" → "
            "\"the number of visitors\" — paraphrase.</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Overview:</strong> <em>\"Overall, visitor "
            "numbers increased substantially across the period, despite a temporary "
            "decline in the middle. The highest figure was recorded in the final "
            "year.\"</em><br>"
            "<span style=\"color:#475569;\">Umumiy trend (o'sish) + eng muhim xususiyat "
            "(o'rtada pasayish, oxirida eng yuqori) — raqamsiz!</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1:</strong> <em>\"In 2010, the museum "
            "received just 20,000 visitors. This figure climbed steadily to reach 55,000 "
            "by 2014.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2:</strong> <em>\"There was then a "
            "dip to 45,000 in 2016, after which numbers rose sharply, finishing at a peak "
            "of 85,000 in 2020.\"</em><br>"
            "<span style=\"color:#475569;\">Aniq raqamlar shu yerda — introduction/"
            "overview'da emas.</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Qaysi gap yaxshi OVERVIEW bo'ladi?</p>"
            ),
            "choices": [
                {"text": "\"In 2014, there were exactly 55,000 visitors.\"", "is_correct": False},
                {"text": "\"Overall, visitor numbers rose considerably over the decade, reaching a peak at the end.\"", "is_correct": True},
                {"text": "\"I believe the museum became more popular because of better exhibitions.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "Overview = umumiy trend, <u>raqamsiz</u> (\"rose considerably... peak at "
                "the end\"). Birinchisi — aniq raqam (bu body'ga tegishli), uchinchisi — "
                "fikr + sabab (\"I believe... because\") — Task 1'da taqiqlangan.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Task 1 javobida overview yozmaslik nimaga "
                "olib keladi?</p>"
            ),
            "choices": [
                {"text": "Hech narsaga — overview ixtiyoriy", "is_correct": False},
                {"text": "Task Achievement pasayadi — overview'siz band odatda 6 dan oshmaydi", "is_correct": True},
                {"text": "Faqat Grammatika pasayadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task Achievement "
                "pasayadi.</mark> Overview — Task 1'ning eng muhim qismi; baholovchilar uni "
                "alohida qidiradi. Aniq, umumiy overview bo'lmasa, Task Achievement (va "
                "shu bilan umumiy band) 6 dan yuqoriga chiqmaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Introduction'da savolni aynan "
                "ko'chirib yozsangiz nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Yaxshi — savol so'zlari to'g'ri", "is_correct": False},
                {"text": "Ko'chirilgan so'zlar so'z sanog'iga kirmaydi va Lexical Resource'ni ko'tarmaydi — paraphrase qilish kerak", "is_correct": True},
                {"text": "Grammatika ballini oshiradi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ko'chirish "
                "yordam bermaydi.</mark> Savoldan aynan ko'chirilgan so'zlar hisobga "
                "olinmaydi va lug'at boyligingizni ko'rsatmaydi. Introduction'ni "
                "<u>paraphrase</u> qiling: \"shows\" → \"illustrates/depicts\", sinonim va "
                "boshqa gap tuzilishi bilan.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to illustrate / depict</div><div class=\"pp-card-back\">ko'rsatmoq, aks ettirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an overview</div><div class=\"pp-card-back\">umumiy ko'rinish (asosiy trendlar)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Overall, ...</div><div class=\"pp-card-back\">Umuman olganda, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a figure</div><div class=\"pp-card-back\">raqam, ko'rsatkich</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to record (a figure)</div><div class=\"pp-card-back\">(raqamni) qayd etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">over the period</div><div class=\"pp-card-back\">davr davomida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">respectively</div><div class=\"pp-card-back\">mos ravishda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a peak / to peak</div><div class=\"pp-card-back\">cho'qqi / eng yuqori nuqtaga chiqmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Task 1 = tavsiflash; fikr, sabab yoki bashorat YO'Q — faqat grafik ko'rsatgani.</li>"
            "<li>4 qism: Introduction (paraphrase) + Overview + 2 Body paragrafi.</li>"
            "<li>Overview eng muhim: umumiy trend, RAQAMSIZ; overviewsiz band 6 dan oshmaydi.</li>"
            "<li>Aniq raqamlar faqat body paragraflarida; savolni aynan ko'chirmang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 4 (order 11 — line graphs & bar charts: trend vocabulary)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_GRAPHS,
    "title": "IELTS Writing 4: Line Graphs and Bar Charts — Trend Vocabulary",
    "summary": "Trend lug'ati: o'sish/pasayish fe'llari, ot shakllari, daraja ravishlari (sharply, gradually) va to'g'ri predloglar (rise by/to/from).",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Trend lug'ati — Task 1'ning yuragi</h2>"
            "<p>Chiziqli grafik va ustunli diagramma vaqt bo'yicha o'zgarishni "
            "(trend) ko'rsatadi. Bu darsda <strong>trend lug'ati</strong>ni "
            "o'rganamiz — bir xil \"go up / go down\"ni takrorlamay, aniq va xilma-xil "
            "yozish (Lexical Resource'ni ko'taradi).</p>"
        )},
        {"rich_text": (
            "<h3>Fe'l va ot shakllari</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>O'sish:</strong> to rise / increase / climb / grow / surge &nbsp;→&nbsp; ot: a rise, an increase, growth, a surge</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Pasayish:</strong> to fall / decline / decrease / drop / plummet &nbsp;→&nbsp; ot: a fall, a decline, a drop</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Barqarorlik:</strong> to remain stable / level off / plateau / stay constant</p>"
            "<p style=\"margin:0;\"><strong>Tebranish:</strong> to fluctuate &nbsp;→&nbsp; ot: a fluctuation; &nbsp;<strong>cho'qqi:</strong> to peak / reach a peak</p>"
            "</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna — ikki xil tuzilma:</strong><br>"
            "Fe'l: <em>\"Sales <u>rose sharply</u> in 2015.\"</em><br>"
            "Ot: <em>\"There was <u>a sharp rise</u> in sales in 2015.\"</em><br>"
            "<span style=\"color:#475569;\">Ikkovini ham ishlatish grammatik xilma-xillikni ko'rsatadi (band 7+).</span></div>"
        )},
        {"rich_text": (
            "<h3>Daraja (sharply? gradually?) va predloglar</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Katta/tez o'zgarish:</strong> sharply, dramatically, significantly, steeply &nbsp;(sifat: a sharp/dramatic rise)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Sekin/barqaror:</strong> gradually, steadily, slowly &nbsp;(sifat: a gradual/steady rise)</p>"
            "<p style=\"margin:0;\"><strong>Kichik:</strong> slightly, marginally &nbsp;(sifat: a slight rise)</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Predloglar — eng ko'p xato shu yerda:</strong><br>"
            "• rise <u>TO</u> a value — yakuniy qiymat: <em>rose to 80,000</em><br>"
            "• rise <u>BY</u> an amount — o'zgarish miqdori: <em>rose by 20,000</em><br>"
            "• rise <u>FROM ... TO ...</u> — <em>rose from 60 to 80</em><br>"
            "• a rise <u>OF</u> an amount: <em>a rise of 20,000</em><br>"
            "• stood <u>AT</u> a value — nuqta: <em>stood at 45,000</em></div>"
        )},
        {"rich_text": (
            "<h3>Namuna — ustunli diagramma</h3>"
            + CHART_BAR +
            "<p>Trend/taqqoslash lug'atini shu ustunli diagrammaga ham qo'llash mumkin. "
            "Endi model gaplarni bosqichma-bosqich oching:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi gapni ochish ▸\">"
            "<div class=\"pp-step\"><p><em>\"Screen time <u>declined steadily</u> with "
            "age.\"</em> — umumiy trend (fe'l + daraja).</p></div>"
            "<div class=\"pp-step\"><p><em>\"The youngest group, aged 10 to 19, spent "
            "the most time on screens, <u>at</u> six hours per day.\"</em> — \"at\" + "
            "nuqta qiymati.</p></div>"
            "<div class=\"pp-step\"><p><em>\"This figure <u>dropped to</u> just 2.5 hours "
            "among those aged 60 and over — <u>a fall of</u> 3.5 hours.\"</em> — "
            "\"dropped to\" (yakun) + \"a fall of\" (miqdor).</p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Grafikda qiymat 2018'da 60'dan 2020'da "
                "85'ga tez ko'tarildi. Qaysi gap eng aniq va tabiiy?</p>"
            ),
            "choices": [
                {"text": "\"The figure went up a lot to 85.\"", "is_correct": False},
                {"text": "\"The figure rose sharply from 60 to 85.\"", "is_correct": True},
                {"text": "\"The figure increased by 85.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"rose sharply from "
                "60 to 85\".</mark> Aniq fe'l (rose) + daraja (sharply) + to'g'ri predlog "
                "(from...to...). \"went up a lot\" — juda oddiy (band past); \"increased "
                "by 85\" — predlog xato (o'zgarish 25, 85 emas — \"by\" miqdorni "
                "bildiradi).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bo'sh joyni to'ldiring: \"There was a "
                "gradual ______ in unemployment.\"</p>"
            ),
            "choices": [
                {"text": "decline", "is_correct": True},
                {"text": "declined", "is_correct": False},
                {"text": "declining", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: decline (ot).</mark> "
                "\"a gradual ______\" — artikl + sifatdan keyin OT kerak: \"a gradual "
                "<u>decline</u>\". \"declined\" (fe'l) va \"declining\" (sifat/-ing) bu "
                "yerda grammatik jihatdan mos emas. \"There was a + sifat + ot\" tuzilishi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Qaysi predlog to'g'ri: \"Sales rose "
                "______ 20,000 units\" (ya'ni o'zgarish miqdori 20,000)?</p>"
            ),
            "choices": [
                {"text": "to", "is_correct": False},
                {"text": "by", "is_correct": True},
                {"text": "at", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: by.</mark> "
                "<u>BY</u> = o'zgarish MIQDORI (rose by 20,000 = 20,000 taga ko'tarildi). "
                "\"to\" = yakuniy qiymat (rose to 20,000), \"at\" = nuqta (stood at "
                "20,000). Savol \"miqdor\"ni so'radi — by.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Trend vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to surge / to plummet</div><div class=\"pp-card-back\">keskin ko'tarilmoq / keskin tushmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to fluctuate</div><div class=\"pp-card-back\">tebranmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to level off / to plateau</div><div class=\"pp-card-back\">barqarorlashmoq, tekislanmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a sharp / dramatic rise</div><div class=\"pp-card-back\">keskin o'sish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a gradual / steady decline</div><div class=\"pp-card-back\">bosqichma-bosqich pasayish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to rise by / to / from</div><div class=\"pp-card-back\">miqdorga / qiymatga / dan ko'tarilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to stand at</div><div class=\"pp-card-back\">(qiymatda) turmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to reach a peak of</div><div class=\"pp-card-back\">... cho'qqisiga yetmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Trend fe'llari + ot shakllari: rose / a rise; fell / a fall — ikkovini ishlating.</li>"
            "<li>Daraja: sharply/dramatically (katta), gradually/steadily (sekin), slightly (kichik).</li>"
            "<li>Predloglar: to (yakun), by (miqdor), from...to..., of (miqdor), at (nuqta).</li>"
            "<li>Bir xil so'zni takrorlamang — bu Lexical Resource'ni ko'taradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 5 (order 12 — pie charts & tables: comparison vocabulary)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_GRAPHS,
    "title": "IELTS Writing 5: Pie Charts and Tables — Comparison Vocabulary",
    "summary": "Ulush va taqqoslash lug'ati: the majority, nearly half, a quarter, one in five, twice as many as; doiraviy diagramma va jadvalni tavsiflash.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Ulush va taqqoslash</h2>"
            "<p>Doiraviy diagramma (pie chart) va jadval (table) ko'pincha vaqt emas, "
            "<strong>ulushlarni</strong> (proportions) ko'rsatadi. Bu yerda kerak "
            "bo'ladigan lug'at — trend emas, balki <mark style=\"background:#dbeafe;\">"
            "taqqoslash va nisbat</mark> lug'ati.</p>"
        )},
        {"rich_text": (
            "<h3>Nisbat lug'ati — foizni so'z bilan</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>~ 75%+</strong> — the vast majority / an overwhelming majority</p>"
            "<p style=\"margin:0 0 6px;\"><strong>~ 50%</strong> — half / around half</p>"
            "<p style=\"margin:0 0 6px;\"><strong>~ 45%</strong> — nearly half / just under a half</p>"
            "<p style=\"margin:0 0 6px;\"><strong>~ 25%</strong> — a quarter / one in four</p>"
            "<p style=\"margin:0 0 6px;\"><strong>~ 20%</strong> — a fifth / one in five</p>"
            "<p style=\"margin:0;\"><strong>~ 10%</strong> — a tenth / a small proportion / a minority</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — taqqoslash tuzilmalari:</strong><br>"
            "• <em>twice as many as / three times as much as</em> — X, Y'dan ikki/uch barobar ko'p<br>"
            "• <em>the largest / smallest proportion</em> — eng katta / kichik ulush<br>"
            "• <em>X accounts for / makes up 45% of ...</em> — X ... ning 45%ini tashkil qiladi<br>"
            "• <em>compared with / in contrast to</em> — ... bilan solishtirganda</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — doiraviy diagramma</h3>"
            + CHART_PIE +
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi gapni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Overview:</strong> <em>\"Overall, heating "
            "consumed by far the largest share of household energy, while lighting "
            "accounted for the smallest.\"</em></p></div>"
            "<div class=\"pp-step\"><p><em>\"Heating made up <u>nearly half</u> of all "
            "energy use, at 45%.\"</em> — nisbat so'z + aniq foiz.</p></div>"
            "<div class=\"pp-step\"><p><em>\"Appliances accounted for <u>a quarter</u> "
            "(25%), while water heating represented <u>a fifth</u> (20%).\"</em></p></div>"
            "<div class=\"pp-step\"><p><em>\"Lighting made up just <u>a tenth</u> of the "
            "total — less than a quarter of the energy used for heating.\"</em> — "
            "taqqoslash bilan yakun.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Jadval (table) haqida qisqacha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:10px 0;overflow-x:auto;\">"
            "<table style=\"border-collapse:collapse;width:100%;font-size:0.95em;\">"
            "<tr style=\"background:#e2e8f0;\"><th style=\"border:1px solid #cbd5e1;padding:6px;\">City</th><th style=\"border:1px solid #cbd5e1;padding:6px;\">Cycle</th><th style=\"border:1px solid #cbd5e1;padding:6px;\">Bus</th><th style=\"border:1px solid #cbd5e1;padding:6px;\">Car</th></tr>"
            "<tr><td style=\"border:1px solid #cbd5e1;padding:6px;\">Amsterdam</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">40%</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">25%</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">35%</td></tr>"
            "<tr><td style=\"border:1px solid #cbd5e1;padding:6px;\">Los Angeles</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">5%</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">15%</td><td style=\"border:1px solid #cbd5e1;padding:6px;\">80%</td></tr>"
            "</table>"
            "<p style=\"margin:8px 0 0;font-size:0.85em;color:#64748b;\">Commuting method by city (% of commuters)</p>"
            "</div>"
            "<p>Jadval uchun ham bir xil taqqoslash lug'ati: <em>\"In Los Angeles, the "
            "car was by far the most common method, at 80% — twice the proportion seen in "
            "Amsterdam.\"</em> Jadvalda ham <u>overview</u> shart: qaysi qator/ustun eng "
            "yuqori/past.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Doiraviy diagrammada \"Heating\" 45%. "
                "Qaysi tavsif eng tabiiy?</p>"
            ),
            "choices": [
                {"text": "\"Heating is 45 and it is the number one.\"", "is_correct": False},
                {"text": "\"Heating accounted for nearly half of total energy use, the largest share.\"", "is_correct": True},
                {"text": "\"I think heating uses the most because winters are cold.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "Nisbat lug'ati (\"nearly half\", \"the largest share\") + \"accounted "
                "for\". Birinchisi — juda oddiy va noaniq; uchinchisi — fikr + sabab "
                "(\"I think... because\"), Task 1'da taqiqlangan.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Los Angeles'da mashina 80%, Amsterdam'da "
                "35%. Qaysi taqqoslash to'g'ri?</p>"
            ),
            "choices": [
                {"text": "\"Car use in LA was more than twice as high as in Amsterdam.\"", "is_correct": True},
                {"text": "\"Car use in LA was twice less than Amsterdam.\"", "is_correct": False},
                {"text": "\"Car use in LA and Amsterdam was the same.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: birinchisi.</mark> "
                "80% ≈ 35%ning ikki baravaridan ko'p → \"more than twice as high as\". "
                "\"twice less\" — inglizchada noto'g'ri/g'aliz tuzilma; \"the same\" — "
                "faktga zid (80 ≠ 35).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Doiraviy diagramma tavsifida ham "
                "overview kerakmi?</p>"
            ),
            "choices": [
                {"text": "Yo'q — pie chart uchun overview shart emas", "is_correct": False},
                {"text": "Ha — eng katta va eng kichik ulushni ko'rsatuvchi overview har doim kerak", "is_correct": True},
                {"text": "Faqat trend grafiklarida kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ha, kerak.</mark> "
                "Har qanday Task 1'da (pie, table, graph) overview shart. Pie/table uchun "
                "overview odatda <u>eng katta va eng kichik</u> toifani ko'rsatadi "
                "(\"heating consumed the largest share, lighting the smallest\") — "
                "raqamsiz.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Comparison vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the vast majority</div><div class=\"pp-card-back\">katta ko'pchilik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a quarter / a fifth / a tenth</div><div class=\"pp-card-back\">chorak / beshdan bir / o'ndan bir</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to account for / to make up</div><div class=\"pp-card-back\">... ni tashkil qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the largest / smallest share</div><div class=\"pp-card-back\">eng katta / kichik ulush</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">twice as many as</div><div class=\"pp-card-back\">... dan ikki barobar ko'p</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">compared with</div><div class=\"pp-card-back\">... bilan solishtirganda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a proportion</div><div class=\"pp-card-back\">ulush, nisbat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">one in five</div><div class=\"pp-card-back\">har beshtadan biri</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Pie/table = ulushlar; taqqoslash va nisbat lug'ati kerak (trend emas).</li>"
            "<li>Foizni so'z bilan ayting: nearly half (45%), a quarter (25%), a fifth (20%).</li>"
            "<li>Taqqoslash: twice as many as, the largest share, accounts for, compared with.</li>"
            "<li>Pie/table uchun ham overview shart: eng katta va eng kichik toifa.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 6 (order 13 — mixed/multiple graphs: selecting what to report)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T1_GRAPHS,
    "title": "IELTS Writing 6: Mixed/Multiple Graphs — Selecting What to Report",
    "summary": "Ikki grafik/diagramma berilganda: hammasini emas, KALIT xususiyatlarni tanlash; overview ikkovini qamrashi; ma'lumotni mantiqan guruhlash.",
    "order": 13,
    "blocks": [
        {"rich_text": (
            "<h2>Ko'p ma'lumot — tanlash san'ati</h2>"
            "<p>Ba'zan Task 1'da <strong>ikkita grafik</strong> yoki bir nechta chiziq "
            "beriladi. Xato — hamma raqamni ketma-ket sanab chiqish. To'g'ri yondashuv: "
            "<mark style=\"background:#dcfce7;\">eng muhim (kalit) xususiyatlarni "
            "tanlash</mark> va ularni mantiqan guruhlash. 150 so'zda hammasini yozib "
            "bo'lmaydi — <u>tanlash</u> — bu ko'nikma.</p>"
        )},
        {"rich_text": (
            "<h3>3 qoida</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Overview ikkovini ham qamrasin.</strong> "
            "Agar ikki grafik bo'lsa, overview har ikkisining asosiy trendini aytishi "
            "kerak — faqat bittasini emas.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Eng katta/muhimini tanlang.</strong> "
            "Eng yuqori, eng past, eng katta o'zgarish, kesishish (crossover) nuqtasi — "
            "shular kalit. Har kichik tebranishni yozish shart emas.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Mantiqan guruhlang.</strong> Har "
            "grafikni alohida paragrafga qo'ying, YOKI ikki grafikni bog'lab (masalan "
            "\"as X rose, Y fell\") solishtiring. Tasodifiy sakramang.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — ikki chiziqli grafik</h3>"
            + CHART_MULTILINE +
            "<p>Bu grafikda ikki trend teskari yo'nalishda — kofe o'sadi, choy tushadi. "
            "Kalit xususiyat: ular <u>o'rtada kesishadi</u> (crossover). Model gaplarni "
            "oching:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi gapni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Overview (ikkovini qamraydi):</strong> "
            "<em>\"Overall, coffee consumption rose steadily over the period, while tea "
            "consumption fell, with the two swapping positions around 2013.\"</em></p></div>"
            "<div class=\"pp-step\"><p><em>\"In 2000, tea was far more popular, at 14 cups "
            "per week compared with just 5 for coffee.\"</em> — boshlang'ich holat "
            "(taqqoslash).</p></div>"
            "<div class=\"pp-step\"><p><em>\"However, coffee climbed to 12 cups by 2020, "
            "overtaking tea, which had declined to 7.\"</em> — kalit xususiyat: "
            "overtaking (kesishish/o'zib ketish).</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — kesishish (crossover):</strong> ikki chiziq kesishsa, "
            "bu deyarli har doim kalit xususiyat — overviewda aytib o'ting: "
            "<em>\"overtook\", \"swapped positions\", \"the point at which X exceeded "
            "Y\"</em>.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Ikkita grafik berilganda overview qanday "
                "bo'lishi kerak?</p>"
            ),
            "choices": [
                {"text": "Faqat birinchi grafikning trendini aytish yetarli", "is_correct": False},
                {"text": "Har ikki grafikning asosiy trendini qamrashi kerak", "is_correct": True},
                {"text": "Overview umuman shart emas", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkovini "
                "qamrashi kerak.</mark> Ikki grafik bo'lsa, overview ikkalasining ham "
                "asosiy manzarasini berishi kerak (masalan biri o'sdi, biri tushdi va "
                "ular kesishdi). Faqat bittasini yoritish Task Achievement'ni pasaytiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Ikki chiziq 2013'da kesishadi. Bu "
                "haqda nima qilish kerak?</p>"
            ),
            "choices": [
                {"text": "E'tibor bermaslik — bu shunchaki bitta nuqta", "is_correct": False},
                {"text": "Uni kalit xususiyat sifatida ko'rsatish (overtaking / crossover)", "is_correct": True},
                {"text": "Faqat oxirgi paragrafda raqam bilan aytish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kalit xususiyat "
                "sifatida ko'rsatish.</mark> Kesishish (crossover) — ikki trend o'rin "
                "almashgani, deyarli har doim eng muhim xususiyat. Uni overviewda ham, "
                "body'da ham ta'kidlang: \"coffee overtook tea around 2013\".</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Task 1'da 150 so'zga hamma mayda raqam "
                "sig'maydi. Eng to'g'ri yondashuv qaysi?</p>"
            ),
            "choices": [
                {"text": "Har bir raqamni ketma-ket sanab chiqish", "is_correct": False},
                {"text": "Eng muhim xususiyatlarni (yuqori/past/kesishish/eng katta o'zgarish) tanlab, guruhlab yozish", "is_correct": True},
                {"text": "Faqat birinchi va oxirgi yilni yozish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kalitlarni tanlab "
                "guruhlash.</mark> Task 1 — barcha ma'lumotni sanash emas, eng muhim "
                "(salient) xususiyatlarni tanlab, mantiqan guruhlab tavsiflash. Bu "
                "Task Achievement va Coherence'ni birga ko'taradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to overtake / to exceed</div><div class=\"pp-card-back\">o'zib ketmoq / oshib ketmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a crossover point</div><div class=\"pp-card-back\">kesishish nuqtasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to swap positions</div><div class=\"pp-card-back\">o'rin almashmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a key / salient feature</div><div class=\"pp-card-back\">kalit / muhim xususiyat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">whereas / while</div><div class=\"pp-card-back\">holbuki, ... esa (taqqoslash)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">respectively</div><div class=\"pp-card-back\">mos ravishda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in contrast</div><div class=\"pp-card-back\">bundan farqli o'laroq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to select key data</div><div class=\"pp-card-back\">kalit ma'lumotni tanlamoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ko'p grafik = tanlash: hamma raqamni emas, KALIT xususiyatlarni yozing.</li>"
            "<li>Overview har ikki grafikni qamrashi kerak.</li>"
            "<li>Kesishish (crossover/overtaking) — deyarli har doim kalit xususiyat.</li>"
            "<li>Ma'lumotni mantiqan guruhlang; whereas/while bilan solishtiring, tasodifiy sakramang.</li>"
            "</ul>"
        )},
    ],
},

]
