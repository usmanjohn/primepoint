"""
IELTS Writing lessons 9-11 (orders 40-42) — the "2-topshiriq: Fikr bildirish insholari
(Task 2 — Opinion Essays)" topic — fourth Writing batch, see toc_ielts_writing.txt.

NOTE: the user wants IELTS examprep to cover the ACADEMIC module only, so the General
Training Letters topic (orders 30-32) is intentionally SKIPPED. Task 2 is identical for
both modules, so it is in scope. Lesson title numbering continues 9,10,11 (GT would have
been 9-11 by order but is skipped).

No audio, no charts (essays are text). Kit: step-reveal (unfold model paragraphs/essays)
+ flashcards (essay phrases) + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_T2_OPINION = {
    "title":   "2-topshiriq: Fikr bildirish insholari (Task 2 — Opinion Essays)",
    "summary": "Task 2 insho tuzilmasi (kirish, tana paragraflari, xulosa), agree/"
               "disagree yondashuvlari va savolga to'g'ridan-to'g'ri javob beruvchi tezis.",
    "icon":    "bi-chat-square-quote",
    "order":   5,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 9 (order 40 — Task 2 structure)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_OPINION,
    "title": "IELTS Writing 9: Task 2 Structure — Introduction, Body Paragraphs, Conclusion",
    "summary": "Task 2 esse 4 paragrafli tuzilma: kirish (paraphrase + tezis), 2 tana paragrafi (PEE: fikr-tushuntirish-misol), xulosa (pozitsiyani takrorlash).",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Task 2 — 4 paragrafli esse</h2>"
            "<p>Task 2 — 250+ so'zlik <strong>insho (essay)</strong>. U umumiy Writing "
            "bandiga ~2 baravar ko'proq hissa qo'shadi, shuning uchun tuzilma juda "
            "muhim. Eng ishonchli, band 7+ ga mos tuzilma — <mark "
            "style=\"background:#dbeafe;\">4 paragraf</mark>: kirish, 2 tana paragrafi va "
            "xulosa.</p>"
        )},
        {"rich_text": (
            "<h3>Har paragrafning vazifasi</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Introduction (2 gap).</strong> "
            "(a) Savolni <u>paraphrase</u> qiling; (b) <u>tezis</u>ni bildiring — "
            "savolga to'g'ridan-to'g'ri javobingiz (keyingi darslar shu haqda). "
            "\"There are many opinions...\" kabi bo'sh gaplardan qoching.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Body 1 (asosiy fikr 1).</strong> "
            "Bitta asosiy g'oya + tushuntirish + misol. PEE tuzilmasini eslang: "
            "<u>Point</u> (topic sentence) → <u>Explain</u> → <u>Example</u>.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Body 2 (asosiy fikr 2).</strong> "
            "Ikkinchi asosiy g'oya, yana PEE bilan. Har paragraf BITTA g'oyaga "
            "bag'ishlansin — ikkitasini aralashtirmang.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Conclusion (1–2 gap).</strong> "
            "Pozitsiyangizni va asosiy fikrlarni <u>qayta ayting</u> (boshqa so'zlar "
            "bilan). <mark style=\"background:#fee2e2;\">Yangi g'oya kiritmang!</mark></p></div>"
            "</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 PEE tuzilmasi — tana paragrafining skeleti:</strong><br>"
            "<strong>P</strong>oint: <em>\"Firstly, community service teaches "
            "responsibility.\"</em><br>"
            "<strong>E</strong>xplain: <em>\"By helping others, teenagers develop empathy "
            "and teamwork.\"</em><br>"
            "<strong>E</strong>xample: <em>\"For instance, a student who volunteers at a "
            "shelter learns to work with people from many backgrounds.\"</em></div>"
        )},
        {"rich_text": (
            "<h3>Model esse — qism-qism oching</h3>"
            "<p><strong>Savol:</strong> <em>\"Some people believe that all high school "
            "students should do unpaid community service. To what extent do you agree or "
            "disagree?\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi paragrafni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"It is "
            "sometimes argued that every high school student should be required to carry "
            "out unpaid work for their community. I completely agree with this view, as "
            "such programmes benefit both young people and society as a whole.\"</em><br>"
            "<span style=\"color:#475569;\">Paraphrase (do → be required to carry out) + "
            "aniq tezis (I completely agree... because...).</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1:</strong> <em>\"Firstly, community "
            "service teaches young people responsibility and practical skills. By helping "
            "in care homes or cleaning public spaces, teenagers develop empathy and "
            "teamwork that classroom lessons cannot provide. For example, a student who "
            "volunteers at a homeless shelter quickly learns to communicate with people "
            "from very different backgrounds.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2:</strong> <em>\"Secondly, "
            "compulsory service strengthens the wider community. When thousands of "
            "students donate their time, local charities and public services gain "
            "much-needed support. Parks are cleaned, elderly residents are visited, and a "
            "culture of civic responsibility is built from an early age.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Conclusion:</strong> <em>\"In conclusion, "
            "I strongly believe that unpaid community service should form part of high "
            "school education, since it develops students personally while benefiting "
            "society at the same time.\"</em><br>"
            "<span style=\"color:#475569;\">Pozitsiya + fikrlar qayta aytildi — yangi "
            "g'oya yo'q.</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Task 2 introduction'ida nima bo'lishi "
                "kerak?</p>"
            ),
            "choices": [
                {"text": "Faqat savolni aynan ko'chirish", "is_correct": False},
                {"text": "Savolning paraphrase'i + aniq tezis (sizning javobingiz)", "is_correct": True},
                {"text": "Birinchi misol va tafsilotlar", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: paraphrase + "
                "tezis.</mark> Kirish savolni o'z so'zingiz bilan qayta aytadi va "
                "pozitsiyangizni (tezis) aniq bildiradi. Savolni ko'chirish so'z "
                "sanog'iga kirmaydi; misollar esa tana paragraflariga tegishli.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Xulosa (conclusion)da yangi bir kuchli "
                "dalil qo'shsangiz nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Yaxshi — ko'proq dalil ballni oshiradi", "is_correct": False},
                {"text": "Bu xato — xulosa faqat mavjud fikrlarni qayta aytadi, yangi g'oya kiritmaydi", "is_correct": True},
                {"text": "Faqat Grammatikaga ta'sir qiladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: bu xato.</mark> "
                "Xulosa — inshoni <u>yopadi</u>: pozitsiya va asosiy fikrlarni boshqa "
                "so'zlar bilan takrorlaydi. Yangi dalil rivojlantirilmay qoladi va "
                "Coherence'ni buzadi. Yangi g'oyalar tana paragraflariga.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> \"For example, a student who volunteers "
                "at a shelter learns to communicate with many people.\" Bu gap PEE "
                "tuzilmasining qaysi qismi?</p>"
            ),
            "choices": [
                {"text": "Point (asosiy fikr)", "is_correct": False},
                {"text": "Example (misol)", "is_correct": True},
                {"text": "Conclusion", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Example.</mark> "
                "\"For example...\" — misol signali; u topic sentence (Point)ni aniq "
                "hayotiy holat bilan quvvatlaydi. Har tana paragrafi: Point → Explain → "
                "Example. Misol dalilni kuchaytiradi va Task Response'ni oshiradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Essay phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">It is sometimes argued that ...</div><div class=\"pp-card-back\">Ba'zan ta'kidlanadiki, ... (kirish)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Firstly, ... / Secondly, ...</div><div class=\"pp-card-back\">Birinchidan / Ikkinchidan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a topic sentence</div><div class=\"pp-card-back\">paragrafning asosiy jumlasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">For instance / For example</div><div class=\"pp-card-back\">Masalan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">In conclusion, ...</div><div class=\"pp-card-back\">Xulosa qilib, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">as a whole</div><div class=\"pp-card-back\">umuman, yaxlit holda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">civic responsibility</div><div class=\"pp-card-back\">fuqarolik mas'uliyati</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">much-needed</div><div class=\"pp-card-back\">juda zarur bo'lgan</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Task 2 = 4 paragraf: Introduction + 2 Body + Conclusion.</li>"
            "<li>Introduction: paraphrase + aniq tezis; bo'sh \"there are many opinions\" dan qoching.</li>"
            "<li>Har tana paragrafi = PEE (Point → Explain → Example), bitta g'oya.</li>"
            "<li>Conclusion: pozitsiya + fikrlarni qayta ayting; YANGI g'oya yo'q.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 10 (order 41 — agree/disagree: one-sided vs balanced)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_OPINION,
    "title": "IELTS Writing 10: Agree/Disagree Essays — One-Sided vs Balanced",
    "summary": "\"To what extent do you agree?\" ikki to'g'ri yondashuv: bir tomonlama (to'liq rozi/qarshi) yoki muvozanatli (qisman rozi); asosiysi — izchil pozitsiya.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>\"To what extent do you agree or disagree?\"</h2>"
            "<p>Bu — Task 2'ning eng ko'p uchraydigan turi. Ikkita to'g'ri yondashuv bor, "
            "va ikkovi ham yuqori ball oladi — <u>agar pozitsiyangiz izchil bo'lsa</u>. "
            "Eng katta xato — pozitsiyani noaniq qoldirish yoki o'rtada ikkilanib "
            "qolish.</p>"
        )},
        {"rich_text": (
            "<h3>Ikki yondashuv</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>1. Bir tomonlama (one-sided) — to'liq rozi YOKI to'liq qarshi.</strong></p>"
            "<p style=\"margin:0;\">Ikkala tana paragrafi ham <u>bir</u> pozitsiyani quvvatlaydi. Aniq va kuchli. Masalan: \"I completely agree\" → Body 1 va Body 2 ikkovi ham roziligingizni dalillaydi.</p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>2. Muvozanatli (balanced) — qisman rozi.</strong></p>"
            "<p style=\"margin:0;\">Bir tana paragrafi bir tomonni, ikkinchisi boshqa tomonni ko'radi — LEKIN xulosada qaysi tomonga <u>ko'proq moyilligingizni</u> aniq aytasiz. Masalan: \"While there are drawbacks, I believe the benefits are greater.\"</p>"
            "</div>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>🔴 Ikkalasi uchun ham oltin qoida — IZCHILLIK:</strong> "
            "pozitsiyangiz kirish, tana va xulosada <u>bir xil</u> bo'lishi shart. "
            "\"50/50\" turib, o'z fikringizni aytmaslik — Task Response'ni pasaytiradi. "
            "Muvozanatli yondashuvda ham <u>aniq umumiy pozitsiya</u> bo'lishi kerak.</div>"
        )},
        {"rich_text": (
            "<h3>Ikki xil kirish — solishtiring</h3>"
            "<p><strong>Savol:</strong> <em>\"Compulsory community service should be part "
            "of high school. To what extent do you agree or disagree?\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi yondashuvni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Bir tomonlama kirish:</strong> <em>\"I "
            "<u>completely agree</u> that community service should be compulsory in high "
            "school, for two main reasons.\"</em><br>"
            "<span style=\"color:#475569;\">Body 1 + Body 2 = ikkovi ham \"nega rozi\" "
            "(masalan: shaxsiy rivojlanish + jamiyatga foyda).</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Muvozanatli kirish:</strong> <em>\"<u>While "
            "some argue</u> that compulsory service places too much pressure on students, "
            "I believe its benefits <u>outweigh</u> this concern.\"</em><br>"
            "<span style=\"color:#475569;\">Body 1 = qarshi tomon (bosim), Body 2 = "
            "foydalar (kuchliroq); xulosa foyda tomonida. Umumiy pozitsiya baribir "
            "aniq!</span></p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Qaysi birini tanlash?</strong> Agar fikringiz kuchli bo'lsa — "
            "bir tomonlama (yozish oson va aniq). Agar ikki tomonda ham jiddiy dalil "
            "ko'rsangiz — muvozanatli. Ikkovi ham to'g'ri; muhimi — <u>tanlang va "
            "unga sodiq qoling</u>.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Talaba kirishda \"I agree\" deydi, "
                "Body 1'da rozilik dalilini, Body 2'da esa \"but actually I disagree\" "
                "deb qarshi dalil beradi, xulosada esa qaror qilmaydi. Muammo nima?</p>"
            ),
            "choices": [
                {"text": "Hech qanday muammo yo'q — ikki tomonni ko'rsatdi", "is_correct": False},
                {"text": "Pozitsiya IZCHIL emas — Task Response pasayadi", "is_correct": True},
                {"text": "Faqat Lexical Resource pasayadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: pozitsiya izchil "
                "emas.</mark> Kirishda \"agree\", keyin \"disagree\", oxirida qarorsizlik "
                "— o'quvchi sizning pozitsiyangizni tushunmaydi. Bu Task Response'ning "
                "asosiy talabi (aniq, izchil pozitsiya)ni buzadi. Bir yo'l tanlab, oxirigacha "
                "sodiq qoling.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Muvozanatli (balanced) yondashuvda "
                "xulosa qanday bo'lishi kerak?</p>"
            ),
            "choices": [
                {"text": "Ikki tomon teng, hech qaysi biri afzal emas deb qoldirish", "is_correct": False},
                {"text": "Qaysi tomon kuchliroq ekanini — umumiy pozitsiyangizni aniq aytish", "is_correct": True},
                {"text": "Yangi uchinchi dalil qo'shish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: umumiy pozitsiyani "
                "aniq aytish.</mark> Muvozanatli esse ham \"o'tirgan joyda qolmaydi\" — "
                "ikki tomonni ko'rgach, xulosada <u>qaysi tomonga moyilligingizni</u> "
                "bildirasiz (\"Overall, I believe the benefits outweigh...\"). Neytral "
                "qolish Task Response'ni pasaytiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bir tomonlama (one-sided) esseda ikkala "
                "tana paragrafi nima qiladi?</p>"
            ),
            "choices": [
                {"text": "Bittasi rozilik, bittasi qarshilik dalilini beradi", "is_correct": False},
                {"text": "Ikkovi ham bitta (bir xil) pozitsiyani turli dalillar bilan quvvatlaydi", "is_correct": True},
                {"text": "Faqat misollar sanaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkovi bitta "
                "pozitsiyani quvvatlaydi.</mark> One-sided yondashuvda ikki tana paragrafi "
                "ham <u>bir xil</u> pozitsiyani (masalan \"agree\") ikki xil sabab bilan "
                "himoya qiladi — bu aniq va kuchli. Ikki tomonni ko'rsatish — bu "
                "muvozanatli (balanced) yondashuv.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Opinion phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I completely agree that ...</div><div class=\"pp-card-back\">Men ... ga to'liq roziman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">While some argue that ..., I believe ...</div><div class=\"pp-card-back\">Ba'zilar ... desa-da, menimcha ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the benefits outweigh the drawbacks</div><div class=\"pp-card-back\">foydalari kamchiliklaridan ustun</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to some extent</div><div class=\"pp-card-back\">ma'lum darajada (qisman)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Overall, I believe ...</div><div class=\"pp-card-back\">Umuman, menimcha ... (xulosa)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a compelling argument</div><div class=\"pp-card-back\">ishonarli dalil</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">consistent</div><div class=\"pp-card-back\">izchil</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to acknowledge that ...</div><div class=\"pp-card-back\">... ekanini tan olmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ikki to'g'ri yondashuv: bir tomonlama (to'liq rozi/qarshi) yoki muvozanatli (qisman).</li>"
            "<li>Bir tomonlama: ikkala body bir pozitsiyani quvvatlaydi.</li>"
            "<li>Muvozanatli: har body bir tomon, LEKIN xulosada aniq umumiy pozitsiya.</li>"
            "<li>Oltin qoida: pozitsiya kirish-tana-xulosada IZCHIL bo'lsin (Task Response).</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 11 (order 42 — thesis statements)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_OPINION,
    "title": "IELTS Writing 11: Thesis Statements That Directly Answer the Question",
    "summary": "Tezis — kirishda savolga to'g'ridan-to'g'ri javobingiz; kuchli vs bo'sh tezis; har savol turi uchun tezis shablonlari.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>Tezis — inshongizning yuragi</h2>"
            "<p><strong>Tezis (thesis statement)</strong> — kirishdagi bitta jumla bo'lib, "
            "u savolga <u>to'g'ridan-to'g'ri javob</u> beradi va butun inshoning yo'nalishini "
            "belgilaydi. Baholovchilar kirishda <mark style=\"background:#dbeafe;\">aniq "
            "pozitsiya</mark>ni qidiradi — u yo'q bo'lsa, band 6 dan oshmaydi.</p>"
        )},
        {"rich_text": (
            "<h3>Bo'sh vs kuchli tezis</h3>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>❌ Bo'sh tezis:</strong> <em>\"There are many opinions about this "
            "topic and this essay will discuss them.\"</em><br>"
            "<span style=\"color:#475569;\">Pozitsiya YO'Q — o'quvchi sizning "
            "fikringizni bilmaydi.</span></div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>✅ Kuchli tezis:</strong> <em>\"I firmly believe that community "
            "service should be compulsory, as it benefits both individuals and society.\"</em><br>"
            "<span style=\"color:#475569;\">Aniq pozitsiya (should be compulsory) + "
            "yo'nalish (ikki sabab).</span></div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Kuchli tezis nima qiladi:</strong> (1) savolga aniq javob beradi; "
            "(2) sizning pozitsiyangizni bildiradi; (3) ko'pincha essening asosiy "
            "fikrlarini oldindan sanaydi (\"for two main reasons\").</div>"
        )},
        {"rich_text": (
            "<h3>Har savol turi uchun tezis shablonlari</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi turni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Agree/Disagree:</strong> pozitsiyani aniq "
            "ayting.<br><em>\"I <u>completely agree</u> that... because...\"</em> yoki "
            "<em>\"I <u>largely disagree</u> with the idea that...\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Discuss both views + your opinion:</strong> "
            "ikkovini ko'rishni + o'z fikringizni ayting.<br><em>\"This essay will examine "
            "both perspectives <u>before arguing that</u>...\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Advantages/Disadvantages:</strong> qaysi "
            "tomon og'irroqligini ayting.<br><em>\"This essay will argue that the "
            "<u>benefits outweigh</u> the drawbacks.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Problem/Solution:</strong> muammo va yechim "
            "borligini ayting.<br><em>\"This essay will outline the main <u>causes</u> of "
            "this problem and suggest possible <u>solutions</u>.\"</em></p></div>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> tezis savolga MOS bo'lishi kerak. "
            "\"Agree/disagree\" savoliga \"This essay will discuss both sides\" deb "
            "javob berish — savolni noto'g'ri o'qish (Task Response pasayadi). Savol "
            "nimani so'rayotganini aniq belgilang.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Qaysi tezis eng kuchli?</p>"
            ),
            "choices": [
                {"text": "\"This is a very important topic in today's world.\"", "is_correct": False},
                {"text": "\"I strongly believe that governments should fund public transport rather than new roads, for environmental and economic reasons.\"", "is_correct": True},
                {"text": "\"There are advantages and disadvantages to this issue.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "Aniq pozitsiya (should fund public transport rather than roads) + "
                "yo'nalish (environmental and economic reasons). Birinchi va uchinchi — "
                "bo'sh gaplar, pozitsiya yo'q; ular hech qanday javob bermaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Savol: \"Do the advantages of remote "
                "work outweigh the disadvantages?\" Qaysi tezis MOS?</p>"
            ),
            "choices": [
                {"text": "\"This essay will argue that the advantages of remote work clearly outweigh its disadvantages.\"", "is_correct": True},
                {"text": "\"I completely agree with remote work.\"", "is_correct": False},
                {"text": "\"There are many types of remote work.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: birinchisi.</mark> "
                "Savol \"outweigh\" (qaysi tomon og'irroq)ni so'raydi — tezis aynan shunga "
                "javob berishi kerak (\"advantages... outweigh... disadvantages\"). "
                "\"I agree\" — bu agree/disagree savoliga mos (savol turi noto'g'ri "
                "o'qilgan); uchinchisi — pozitsiyasiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Tezis odatda insho tuzilmasining qayerida "
                "turadi?</p>"
            ),
            "choices": [
                {"text": "Xulosada (conclusion)", "is_correct": False},
                {"text": "Kirishning oxirida (introduction)", "is_correct": True},
                {"text": "Birinchi tana paragrafida", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kirishning "
                "oxirida.</mark> Tezis kirishda — savol paraphrase'idan keyin — turadi va "
                "butun inshoning yo'nalishini oldindan e'lon qiladi. Xulosada u "
                "<u>qayta</u> aytiladi (boshqa so'zlar bilan), lekin birinchi marta "
                "kirishda paydo bo'ladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Thesis phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I firmly believe that ...</div><div class=\"pp-card-back\">Men qat'iy ishonamanki, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">This essay will argue that ...</div><div class=\"pp-card-back\">Ushbu insho ... ni dalillaydi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">before concluding that ...</div><div class=\"pp-card-back\">... degan xulosaga kelishdan oldin</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the benefits outweigh the drawbacks</div><div class=\"pp-card-back\">foydalar kamchiliklardan ustun</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a thesis statement</div><div class=\"pp-card-back\">tezis (asosiy fikr) jumlasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to address the question</div><div class=\"pp-card-back\">savolga javob bermoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">largely / partly</div><div class=\"pp-card-back\">asosan / qisman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">for two main reasons</div><div class=\"pp-card-back\">ikki asosiy sabab bilan</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Tezis = kirishda savolga to'g'ridan-to'g'ri javob; pozitsiyani aniq bildiradi.</li>"
            "<li>Bo'sh tezis (\"there are many opinions\") band 6 dan oshirmaydi.</li>"
            "<li>Tezis savol TURIGA mos bo'lsin: agree/disagree ≠ discuss both ≠ outweigh.</li>"
            "<li>Tezis kirishning oxirida turadi; xulosada boshqa so'zlar bilan qayta aytiladi.</li>"
            "</ul>"
        )},
    ],
},

]
