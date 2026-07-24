"""
IELTS Writing lessons 14-15 (orders 60-61) — the "2-topshiriq: Afzallik/kamchilik va
ikki qismli savol (Task 2 — Advantage/Disadvantage & Two-Part Question Essays)" topic —
sixth Writing batch, see toc_ielts_writing.txt. (Academic-only scope; Task 2 is shared.)

No audio, no charts. Kit: step-reveal (unfold model essays) + flashcards + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_T2_ADV = {
    "title":   "2-topshiriq: Afzallik/kamchilik va ikki qismli savol (Task 2 — Advantage/Disadvantage & Two-Part Question Essays)",
    "summary": "Afzallik/kamchilik (weighing up, \"outweigh\" verdikti) va ikki qismli "
               "(direct question) insholari — har ikki qismga to'liq javob.",
    "icon":    "bi-clipboard2-check",
    "order":   7,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 14 (order 60 — advantages/disadvantages)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_ADV,
    "title": "IELTS Writing 14: Advantages/Disadvantages Essays — Weighing Up",
    "summary": "Afzallik/kamchilik insholari: ikki kichik tur (shunchaki muhokama VS \"outweigh?\" — verdikt talab qiladi); afzallik/kamchilik BITTA narsaning tomonlaridir.",
    "order": 60,
    "blocks": [
        {"rich_text": (
            "<h2>Afzallik va kamchilik insholari</h2>"
            "<p>Bu turda <strong>bitta narsaning</strong> (masalan chet elda o'qish) "
            "ijobiy va salbiy tomonlarini yozasiz. Ikkita kichik tur bor va ular "
            "<u>farqli</u> narsani so'raydi — savolni diqqat bilan o'qing:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>(a) \"Discuss the advantages and disadvantages.\"</strong> — ikkovini muhokama qiling; qat'iy verdikt shart emas.</p>"
            "<p style=\"margin:0;\"><strong>(b) \"Do the advantages outweigh the disadvantages?\"</strong> — <mark style=\"background:#fee2e2;\">verdikt SHART</mark>: qaysi tomon og'irroq ekanini aniq ayting.</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Discuss-both-views'dan farqi</h3>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Muhim farq:</strong> \"Discuss both views\" — <u>ikki xil "
            "odam</u>ning qarama-qarshi FIKRLARI haqida. Advantage/disadvantage esa — "
            "<u>bitta narsaning</u> yaxshi va yomon TOMONLARI haqida. Tuzilma o'xshash "
            "(4 paragraf), lekin mazmun boshqa: qarash emas, pros va cons.</div>"
            "<p><strong>Tuzilma:</strong> Introduction (paraphrase + \"outweigh\" bo'lsa "
            "verdikt) → Body 1 (afzalliklar) → Body 2 (kamchiliklar) → Conclusion "
            "(jamlab, so'ralsa verdiktni qayta ayting).</p>"
        )},
        {"rich_text": (
            "<h3>Model esse — \"outweigh?\" turi</h3>"
            "<p><strong>Savol:</strong> <em>\"Many students choose to study at "
            "universities abroad. Do the advantages of this outweigh the "
            "disadvantages?\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi paragrafni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"An increasing "
            "number of students choose to pursue their higher education in foreign "
            "countries. While studying abroad has certain drawbacks, this essay will "
            "argue that its advantages are considerably greater.\"</em><br>"
            "<span style=\"color:#475569;\">\"outweigh\" savoli → kirishdayoq verdikt "
            "(advantages greater).</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1 (advantages):</strong> <em>\"The "
            "most significant advantage is exposure to a new culture and language. Living "
            "independently abroad forces students to become resilient and open-minded. "
            "Moreover, degrees from prestigious foreign universities are often highly "
            "valued by employers, improving graduates' career prospects.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2 (disadvantages):</strong> <em>\"There "
            "are, however, some notable drawbacks. Studying overseas is expensive, as "
            "tuition and living costs can be far higher than at home. Furthermore, "
            "students may experience homesickness, particularly at first, which can "
            "affect their academic performance.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Conclusion:</strong> <em>\"In conclusion, "
            "although studying abroad involves considerable expense and emotional "
            "challenges, I believe the long-term benefits of cultural growth and enhanced "
            "career opportunities clearly outweigh these disadvantages.\"</em><br>"
            "<span style=\"color:#475569;\">Verdikt qayta va aniq (outweigh).</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> \"Do the advantages outweigh the "
                "disadvantages?\" savoli shunchaki \"discuss advantages and "
                "disadvantages\"dan nimasi bilan farq qiladi?</p>"
            ),
            "choices": [
                {"text": "Hech nima — ikkovi bir xil", "is_correct": False},
                {"text": "\"Outweigh\" aniq VERDIKT talab qiladi — qaysi tomon og'irroq ekanini aytish kerak", "is_correct": True},
                {"text": "\"Outweigh\" faqat afzalliklarni so'raydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: verdikt talab "
                "qiladi.</mark> \"Outweigh\" = tarozida tortish: qaysi tomon (afzallik "
                "yoki kamchilik) kuchliroq ekanini aniq aytishingiz shart — kirishda va "
                "xulosada. Neytral qolish (\"both have pros and cons\") bu savolga to'liq "
                "javob bermaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Advantage/disadvantage inshosi "
                "discuss-both-views'dan qanday farq qiladi?</p>"
            ),
            "choices": [
                {"text": "Ikki xil odamning qarama-qarshi fikrlari o'rniga, BITTA narsaning yaxshi/yomon tomonlari", "is_correct": True},
                {"text": "Hech qanday farqi yo'q", "is_correct": False},
                {"text": "Faqat afzalliklarni yozasiz", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: bitta narsaning "
                "pros/cons.</mark> Discuss-both-views — ikki qarama-qarshi QARASH "
                "(odamlar fikri); adv/disadv — bitta narsaning ijobiy va salbiy "
                "TOMONLARI. Tuzilma o'xshash, lekin mazmun turlicha.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Qaysi gap aniq verdikt beradi?</p>"
            ),
            "choices": [
                {"text": "\"There are both advantages and disadvantages.\"", "is_correct": False},
                {"text": "\"The benefits of studying abroad clearly outweigh its drawbacks.\"", "is_correct": True},
                {"text": "\"This is a difficult question to answer.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "\"...clearly outweigh...\" — aniq verdikt: bir tomon (benefits) "
                "kuchliroq. Birinchi va uchinchi gaplar — neytral/qochuvchi, pozitsiya "
                "bermaydi va Task Response'ni pasaytiradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Advantage/disadvantage phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">One clear advantage is ...</div><div class=\"pp-card-back\">Bir aniq afzallik ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">A significant drawback is ...</div><div class=\"pp-card-back\">Jiddiy kamchilik ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to outweigh</div><div class=\"pp-card-back\">og'irroq/ustun kelmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the benefits far exceed the costs</div><div class=\"pp-card-back\">foydalar xarajatlardan ancha ortiq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">resilient</div><div class=\"pp-card-back\">chidamli, bardoshli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">career prospects</div><div class=\"pp-card-back\">martaba imkoniyatlari</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">homesickness</div><div class=\"pp-card-back\">uy sog'inchi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on balance</div><div class=\"pp-card-back\">umumiy hisobda, xolisona</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ikki kichik tur: shunchaki muhokama VS \"outweigh?\" (verdikt SHART).</li>"
            "<li>Adv/disadv = BITTA narsaning pros/cons; discuss-both-views = ikki qarash.</li>"
            "<li>Tuzilma: intro (+verdikt) → afzalliklar → kamchiliklar → conclusion.</li>"
            "<li>\"Outweigh\" bo'lsa — qaysi tomon og'irroq ekanini kirish va xulosada aniq ayting.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 15 (order 61 — two-part / direct question)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_ADV,
    "title": "IELTS Writing 15: Two-Part Question Essays — Answering Both Parts Fully",
    "summary": "Ikki qismli (direct question) insho: prompt ikki savol beradi; har ikkisiga to'liq javob berish — biriga e'tibor bermaslik Task Response'ni cheklaydi.",
    "order": 61,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki qismli (direct question) insholar</h2>"
            "<p>Ba'zi Task 2 savollari <strong>ikkita to'g'ridan-to'g'ri savol</strong> "
            "beradi, masalan: <em>\"Why is this happening? Is it a positive or negative "
            "development?\"</em> yoki <em>\"What are the reasons? How can it be "
            "addressed?\"</em>. Eng muhim qoida bitta: <mark "
            "style=\"background:#fee2e2;\">har ikki savolga ham TO'LIQ javob bering</mark>.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Eng ko'p yo'qotiladigan ball:</strong> nomzod birinchi savolga "
            "yaxshi javob berib, ikkinchisini <u>unutadi</u> yoki bir gapda o'tib "
            "ketadi. Bu Task Response'ni cheklaydi — ikki savol = ikki teng paragraf.</div>"
        )},
        {"rich_text": (
            "<h3>Tuzilma — har savolga bir paragraf</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Introduction.</strong> Savolni "
            "paraphrase qiling + <u>ikkala savolga</u> qisqa javob bering (masalan: "
            "\"bu trendning sabablarini ko'rib chiqib, uni ijobiy deb baholayman\").</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Body 1 — 1-savolga javob.</strong> "
            "Masalan \"Why?\" — sabablarni tushuntiring (dalil + misol).</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Body 2 — 2-savolga javob.</strong> "
            "Masalan \"Is it positive or negative?\" — aniq pozitsiya bilan javob "
            "bering. Bu qism ko'pincha <u>fikr</u> talab qiladi.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Conclusion.</strong> Ikkala savolga "
            "javobingizni qisqacha jamlang.</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> ikkinchi savol ko'pincha \"Is this a positive "
            "or negative development?\" bo'ladi — bu <u>aniq fikr</u> (positive YOKI "
            "negative, yoki asosan biri) talab qiladi. \"Ikkalasi ham\" deb qochmang — "
            "asosiy moyillikni ayting.</div>"
        )},
        {"rich_text": (
            "<h3>Model esse — qism-qism oching</h3>"
            "<p><strong>Savol:</strong> <em>\"In many countries, people are choosing to "
            "have children later in life. Why is this happening? Is it a positive or "
            "negative development?\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi paragrafni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"In many parts "
            "of the world, people are increasingly choosing to start families later in "
            "life. This essay will examine the reasons behind this trend and argue that, "
            "on balance, it is a positive development.\"</em><br>"
            "<span style=\"color:#475569;\">Ikkala savolga ishora: sabablar + ijobiy "
            "baho.</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1 (Why? — reasons):</strong> "
            "<em>\"There are several reasons for this shift. Firstly, many young people "
            "now prioritise their education and careers, delaying parenthood until they "
            "feel financially secure. Secondly, advances in medicine have made it safer "
            "to have children at an older age.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2 (Positive or negative? — opinion):</strong> "
            "<em>\"In my view, this trend is largely positive. Parents who wait tend to "
            "be more financially stable and emotionally mature, which benefits their "
            "children. Although later pregnancies carry some medical risks, these are "
            "increasingly manageable.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Conclusion:</strong> <em>\"In conclusion, "
            "later parenthood is driven mainly by career priorities and medical progress, "
            "and I believe it is a positive development, as it allows children to be "
            "raised in more stable circumstances.\"</em><br>"
            "<span style=\"color:#475569;\">Ikkala savolga javob qayta jamlandi.</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Ikki qismli savolda eng muhim qoida "
                "nima?</p>"
            ),
            "choices": [
                {"text": "Faqat birinchi savolga chuqur javob berish", "is_correct": False},
                {"text": "Har IKKI savolga ham to'liq va teng javob berish", "is_correct": True},
                {"text": "Ikkala savolni bitta paragrafga jamlash", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkala savolga "
                "to'liq javob.</mark> Ikki qismli savolda ikki savol = ikki teng "
                "paragraf. Bittasini chuqur, boshqasini yuzaki javoblab qoldirish — Task "
                "Response'ni cheklaydi (savolning yarmiga javob berilmagan).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"Is this a positive or negative "
                "development?\" savoli nimani talab qiladi?</p>"
            ),
            "choices": [
                {"text": "Neytral qolib, \"ikkalasi ham\" deyish", "is_correct": False},
                {"text": "Aniq pozitsiya — asosan ijobiy YOKI salbiy ekanini aytish", "is_correct": True},
                {"text": "Faqat sabablarni sanash", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: aniq "
                "pozitsiya.</mark> Bu savol fikr so'raydi — trend asosan ijobiy yoki "
                "salbiy ekanini aniq ayting (\"largely positive\"). \"Ikkalasi ham\" deb "
                "qochish pozitsiyasizlik — Task Response pasayadi. (Sabablar — birinchi "
                "savolning javobi.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Nomzod \"Why is this happening?\" ga 3 "
                "paragraf yozib, \"Is it positive or negative?\" ga bir og'iz ham javob "
                "bermaydi. Natija?</p>"
            ),
            "choices": [
                {"text": "Yaxshi — birinchi savol chuqur yoritilgan", "is_correct": False},
                {"text": "Task Response cheklanadi — savolning yarmiga javob berilmagan", "is_correct": True},
                {"text": "Faqat Lexical Resource pasayadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task Response "
                "cheklanadi.</mark> Ikkinchi savolga javob bermaslik — savolning yarmini "
                "e'tiborsiz qoldirish. Bitta savolni juda chuqur yoritish boshqasining "
                "yo'qligini qoplamaydi. Har ikkisiga muvozanatli javob bering.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Two-part phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">There are several reasons for this ...</div><div class=\"pp-card-back\">Buning bir necha sababi bor ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a positive / negative development</div><div class=\"pp-card-back\">ijobiy / salbiy o'zgarish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on balance</div><div class=\"pp-card-back\">umumiy hisobda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to prioritise</div><div class=\"pp-card-back\">ustuvor deb bilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">financially secure</div><div class=\"pp-card-back\">moliyaviy jihatdan barqaror</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a shift / a trend</div><div class=\"pp-card-back\">o'zgarish / tendensiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to delay</div><div class=\"pp-card-back\">kechiktirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">emotionally mature</div><div class=\"pp-card-back\">hissiy jihatdan yetuk</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ikki qismli savol = ikki to'g'ridan-to'g'ri savol; har ikkisiga TO'LIQ javob bering.</li>"
            "<li>Tuzilma: intro (ikkovga ishora) → Body 1 (savol 1) → Body 2 (savol 2) → conclusion.</li>"
            "<li>\"Positive or negative?\" — aniq pozitsiya talab qiladi (neytral qolmang).</li>"
            "<li>Bitta savolni chuqur, boshqasini yuzaki qoldirish Task Response'ni cheklaydi.</li>"
            "</ul>"
        )},
    ],
},

]
