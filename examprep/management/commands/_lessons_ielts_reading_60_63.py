"""
IELTS Reading lessons 23-26 (orders 60-63) — the whole "Bo'sh joyni to'ldirish
(Sentence / Summary / Note / Table / Flow-Chart Completion)" topic — sixth batch,
see toc_ielts_reading.txt.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_COMPLETION = {
    "title":   "Bo'sh joyni to'ldirish (Sentence / Summary / Note / Table / Flow-Chart Completion)",
    "summary": "Matndan aynan so'z ko'chirib bo'sh joyni to'ldirish: so'z chegarasi qoidalari, "
               "so'z turini bashorat qilish va turli tuzilmalar.",
    "icon":    "bi-input-cursor-text",
    "order":   7,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 23 (order 60 — Sentence Completion, word-limit rules)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_COMPLETION,
    "title": "IELTS Reading 23: Sentence Completion — Word-Limit Rules (NO MORE THAN THREE WORDS)",
    "summary": "Bo'sh joyni matndan AYNAN so'z bilan to'ldirish: so'z chegarasi qoidalari, imlo, grammatik moslik va so'z turini bashorat qilish.",
    "order": 60,
    "blocks": [
        {"rich_text": (
            "<h2>Completion — MCQ'dan tubdan farqli</h2>"
            "<p>Bo'sh joyni to'ldirish savollarida bir <mark style=\"background:#fee2e2;\">"
            "muhim burilish</mark> bor: MCQ'da to'g'ri javob <u>paraphrase</u> edi, bu "
            "yerda esa javob <u>matndan aynan ko'chiriladi</u> — o'z so'zingiz bilan "
            "yozsangiz, xato. Vazifa: jumladagi bo'sh joyni matndagi <strong>aniq "
            "so'z(lar)</strong> bilan to'ldirish.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — imlo muhim:</strong> javobni matndan ko'chirasiz, "
            "shuning uchun <u>imlo xatosi = noto'g'ri javob</u>. So'zni matndan aynan, "
            "harfma-harf ko'chiring — o'zingizdan \"tuzatmang\".</div>"
        )},
        {"rich_text": (
            "<h3>So'z chegarasi qoidalari (word limit)</h3>"
            "<p>Ko'rsatma har doim aniq: <em>\"Choose NO MORE THAN THREE WORDS AND/OR A "
            "NUMBER from the passage.\"</em> Bu chegaradan <u>oshsangiz</u> — javob "
            "avtomatik noto'g'ri, mazmuni to'g'ri bo'lsa ham. Qoidalar:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>\"THREE WORDS\"</strong> = ko'pi bilan 3 so'z. 1 yoki 2 so'z ham bo'ladi — kamrog'i muammo emas, ko'prog'i xato.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Raqamlar:</strong> \"AND/OR A NUMBER\" bo'lsa, \"20 million\" kabi javob mumkin (raqam alohida sanaladi).</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Chiziqchali so'z:</strong> \"well-being\", \"twelve-year-old\" — <u>bitta</u> so'z sanaladi.</p>"
            "<p style=\"margin:0;\"><strong>Artikl (a/an/the):</strong> agar 2 so'z chegarasi bo'lsa va matnda \"a licence\" tursa — ko'pincha shart bo'lmaganini yozing (\"licence\"); grammatikaga qarang.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> completion savollari deyarli har doim <u>matn "
            "tartibida</u> keladi — 1-bo'sh joy javobi 2-nikidan yuqorida. Bu qidiruvni "
            "juda osonlashtiradi.</div>"
        )},
        {"rich_text": (
            "<h3>Oltin usul: so'z turini oldindan bashorat qiling</h3>"
            "<p>Bo'sh joyni to'ldirishdan oldin, jumladagi grammatikaga qarab <u>qanday "
            "so'z</u> kerakligini ayting — ot? fe'l? sifat? son? Bu miyangizga aniq "
            "\"nishon\" beradi:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Bo'sh joyli jumlani "
            "o'qing. Bo'sh joydan <u>oldingi va keyingi</u> so'zga qarang: artikl (a/the) "
            "dan keyin — ot; \"to\" dan keyin — fe'l; \"very/more\" dan keyin — sifat.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Jumladan <u>langar "
            "so'z</u> (paraphrase qilinmaydigan ism/sana/atama) tanlab, matndan o'sha "
            "joyni toping.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> E'tibor bering: "
            "jumlaning o'zi paraphrase qilingan bo'ladi, lekin <u>bo'sh joyga tushadigan "
            "so'z</u> matnda aynan turadi. O'sha so'zni toping.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Ko'chiring — harfma-harf. "
            "Keyin to'liq jumlani o'qib, grammatik va mazmunan ravonligini tekshiring.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — bashorat kuchda</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"The lighthouse was powered "
            "by burning coal until 1875, when it was converted to run on oil. Electricity "
            "finally reached the island in 1932.\"</p>"
            "</div>"
            "<p><strong>Jumla (bo'sh joy bilan):</strong> <em>\"Before 1875, the "
            "lighthouse was fuelled by ______.\"</em> (NO MORE THAN TWO WORDS)</p>"
            "<p><strong>Bashorat:</strong> \"fuelled by ______\" → bo'sh joyga <u>ot</u> "
            "(yoqilg'i turi) kerak. Langar: \"1875\". Matnda \"burning <u>coal</u> until "
            "1875\" — 1875'gacha yoqilg'i <strong>coal</strong>. Javob: <mark "
            "style=\"background:#dcfce7;\">coal</mark> (1 so'z). \"burning coal\" deb "
            "yozsangiz ham 2 so'z chegarasiga sig'adi, lekin \"fuelled by burning coal\" "
            "grammatik jihatdan ortiqcha — sof \"coal\" eng aniq javob.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Ko'rsatma: <em>\"NO MORE THAN THREE "
                "WORDS.\"</em> Javobingiz to'g'ri ma'noni beradi, lekin 4 so'zdan iborat. "
                "Nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Mazmuni to'g'ri bo'lgani uchun ball beriladi", "is_correct": False},
                {"text": "Javob noto'g'ri sanaladi — so'z chegarasidan oshgan", "is_correct": True},
                {"text": "Yarim ball beriladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: noto'g'ri "
                "sanaladi.</mark> So'z chegarasi qat'iy qoida — 3 so'z desa, 4 so'z "
                "avtomatik xato, mazmuni mukammal bo'lsa ham. Bu ko'pincha \"ortiqcha\" "
                "so'z (artikl, sifat) qo'shib yuborishdan bo'ladi. Javobni yozgach, "
                "so'zlarini <u>sanang</u> — chiziqchali so'z bitta hisoblanishini "
                "unutmang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Matn: <em>\"The survey found that "
                "employees who worked from home reported higher levels of job "
                "satisfaction than those in the office.\"</em> Jumla: <em>\"Home workers "
                "said they experienced greater ______.\"</em> (NO MORE THAN TWO WORDS) "
                "Javob nima?</p>"
            ),
            "choices": [
                {"text": "happiness", "is_correct": False},
                {"text": "job satisfaction", "is_correct": True},
                {"text": "higher levels", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: job "
                "satisfaction.</mark> Bashorat: \"greater ______\" → ot kerak. Matnda "
                "aynan \"<u>job satisfaction</u>\" (2 so'z — chegaraga to'g'ri keladi). "
                "\"happiness\" — ma'nan yaqin, lekin matnda YO'Q (o'z so'zingiz — "
                "completion'da taqiqlanadi). \"higher levels\" — so'z-tuzoq: matnda bor, "
                "lekin \"greater higher levels\" grammatik jihatdan buzuq.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Sentence completion savolida javobni "
                "topishning eng samarali usuli qaysi?</p>"
            ),
            "choices": [
                {"text": "Butun matnni boshdan oxir o'qib chiqib, mos so'zni topaman", "is_correct": False},
                {"text": "Bo'sh joyga qanday SO'Z TURI kerakligini bashorat qilaman, keyin langar so'z bilan matndan joyni topaman", "is_correct": True},
                {"text": "Variantlardan eng uzunini tanlayman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: so'z turini "
                "bashorat qilish + langar.</mark> Grammatika bo'sh joyga qanday so'z "
                "(ot/fe'l/sifat) kerakligini aytadi — bu aniq nishon. Langar so'z bilan "
                "matndagi joyni topib, o'sha turdagi so'zni ko'chirasiz. Butun matnni "
                "o'qish — vaqt isrofi (bo'sh joylar tartibda keladi); completion'da "
                "\"variant\" ham yo'q (so'z chegarali javob).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">word limit</div><div class=\"pp-card-back\">so'z chegarasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to fuel / to power</div><div class=\"pp-card-back\">yoqilg'i/quvvat bilan ta'minlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to convert to</div><div class=\"pp-card-back\">~ga o'tkazmoq/aylantirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">job satisfaction</div><div class=\"pp-card-back\">ishdan qoniqish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a hyphenated word</div><div class=\"pp-card-back\">chiziqchali so'z (bitta sanaladi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to copy word-for-word</div><div class=\"pp-card-back\">harfma-harf ko'chirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to report (higher levels)</div><div class=\"pp-card-back\">(yuqori darajani) qayd etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">spelling</div><div class=\"pp-card-back\">imlo</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Completion javobi matndan AYNAN ko'chiriladi — o'z so'zingiz emas; imlo xatosi = xato.</li>"
            "<li>So'z chegarasidan oshmang: \"THREE WORDS\" = ko'pi bilan 3; chiziqchali so'z bitta.</li>"
            "<li>Avval so'z TURINI bashorat qiling (ot/fe'l/sifat), keyin langar bilan joyni toping.</li>"
            "<li>Jumla paraphrase qilingan, lekin bo'sh joyga tushadigan so'z matnda aynan turadi.</li>"
            "<li>Bo'sh joylar matn tartibida — keyingisini pastdan qidiring.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 24 (order 61 — Summary Completion)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_COMPLETION,
    "title": "IELTS Reading 24: Summary Completion — Predicting Word Type Before You Scan",
    "summary": "Xulosa paragrafidagi bo'sh joylarni to'ldirish: ikki versiya (matndan / qutidan), so'z turini bashorat va word-form tuzog'i.",
    "order": 61,
    "blocks": [
        {"rich_text": (
            "<h2>Summary Completion nima?</h2>"
            "<p>Sizga matnning bir qismining <strong>qisqacha bayoni</strong> (summary) "
            "beriladi — unda bir necha bo'sh joy bor. Ikki versiyasi bor:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>(a) Matndan so'z bilan</strong> — "
            "Sentence Completion kabi: bo'sh joyni matndagi aynan so'z bilan to'ldirasiz "
            "(so'z chegarasi bor).</p>"
            "<p style=\"margin:0;\"><strong>(b) Qutidan tanlab (from a box)</strong> — "
            "sizga so'zlar ro'yxati (A, B, C...) beriladi, undan tanlaysiz. Bu yerda so'z "
            "chegarasi yo'q, lekin <u>ortiqcha</u> so'zlar bor (tuzoq).</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> summary matnni <u>paraphrase</u> qiladi — "
            "summarydagi so'zlarni matndan qidirmang, ular boshqacha yozilgan. "
            "Summary'dagi <u>langar</u> (o'zgarmas ism/atama) orqali matndagi tegishli "
            "joyni toping.</div>"
        )},
        {"rich_text": (
            "<h3>Kalit ko'nikma: har bo'sh joyga so'z turini bashorat qiling</h3>"
            "<p>Skan qilishdan <u>oldin</u> butun summaryni o'qib, har bo'sh joy uchun "
            "grammatik \"nishon\" belgilang. Bu ayniqsa muhim, chunki summary bir necha "
            "bo'sh joyli — nishonsiz adashib ketasiz:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>\"...led to a rise in ______.\"</strong> → ot (nima ko'paydi?)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>\"...scientists began to ______ the data.\"</strong> → fe'l (asosiy shakl)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>\"...the results were surprisingly ______.\"</strong> → sifat</p>"
            "<p style=\"margin:0;\"><strong>\"...the process takes about ______ years.\"</strong> → son</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — qutili versiyada word-form tuzog'i:</strong> qutida "
            "\"analyse\" (fe'l) va \"analysis\" (ot) ikkovi ham bo'lishi mumkin. "
            "Bashorat qilingan so'z turi qaysi shaklni olishingizni aytadi — grammatika "
            "sizni tuzoqdan qutqaradi.</div>"
        )},
        {"rich_text": (
            "<h3>Usul — bosqichma-bosqich</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Butun summaryni bir "
            "marta o'qing — umumiy mazmunni tushuning va har bo'sh joyning so'z turini "
            "belgilang (ot/fe'l/sifat/son).</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Summary matnning "
            "<u>qaysi qismini</u> qamrayapti — sarlavha yoki langar so'z orqali aniqlang "
            "(ko'pincha 1–2 paragraf).</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> O'sha qismni o'qib, har "
            "bo'sh joyga mos so'zni toping. Matndan so'z olsangiz — aynan ko'chiring; "
            "qutidan olsangiz — to'g'ri word-form'ni tanlang.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> To'liq summaryni "
            "to'ldirilgan holda o'qing — u ravon va matnga sodiqmi? Grammatika har bir "
            "bo'sh joyda to'g'rimi?</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — qutili versiya (word-form)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"Volcanic ash can remain in "
            "the atmosphere for months, reflecting sunlight and causing global "
            "temperatures to drop. After the 1815 eruption of Tambora, harvests failed "
            "across Europe and North America.\"</p>"
            "</div>"
            "<p><strong>Summary:</strong> <em>\"When a large volcano erupts, ash in the "
            "air can <u>(1) ______</u> sunlight, which makes the planet cooler. In 1815 "
            "this led to widespread crop <u>(2) ______</u>.\"</em></p>"
            "<p><strong>Quti:</strong> A absorb &nbsp; B reflect &nbsp; C failure "
            "&nbsp; D failed &nbsp; E increase</p>"
            "<p>Bashorat: (1) \"can ______ sunlight\" → <u>fe'l</u>; (2) \"crop ______\" "
            "→ <u>ot</u>. (1): matn \"<u>reflecting</u> sunlight\" → fe'l shakli "
            "<strong>B reflect</strong> (A absorb — teskari ma'no, tuzoq). (2): \"harvests "
            "<u>failed</u>\" — lekin bo'sh joyga OT kerak, \"failed\" fe'l → to'g'ri "
            "word-form <strong>C failure</strong> (\"crop failure\"). D failed — "
            "grammatik jihatdan xato (word-form tuzog'i!).</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Summary Completion'da summarydagi "
                "so'zlarni matndan to'g'ridan-to'g'ri qidirsangiz nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Tez topasiz — summary matnning nusxasi", "is_correct": False},
                {"text": "Ko'pincha topa olmaysiz — summary matnni paraphrase qiladi; langar so'z va ma'no bilan qidirish kerak", "is_correct": True},
                {"text": "Summary har doim matn bilan bir xil so'zlarni ishlatadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ko'pincha topa "
                "olmaysiz.</mark> Summary — matnning <u>qayta yozilgan</u> qisqasi, "
                "nusxasi emas. So'zma-so'z qidirish sizni chalg'itadi. Buning o'rniga: "
                "o'zgarmaydigan langar (ism, sana, atama) bilan matndagi joyni toping, "
                "keyin <u>ma'no</u> bo'yicha bo'sh joyga mos so'zni oling.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Qutili summaryda bo'sh joy: <em>\"...a "
                "significant ______ in production.\"</em> Quti: A grow &nbsp; B growth "
                "&nbsp; C growing. Qaysi so'z va nega?</p>"
            ),
            "choices": [
                {"text": "A grow — chunki mazmuni o'sish", "is_correct": False},
                {"text": "B growth — \"a significant ______\" artikl+sifatdan keyin OT kerak", "is_correct": True},
                {"text": "C growing — chunki u eng uzun", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B growth.</mark> "
                "Bu klassik word-form tuzog'i — uchala so'z ham \"o'sish\" ma'nosini "
                "beradi, lekin grammatika bittasini talab qiladi. \"a significant "
                "______\" — artikl (a) + sifat (significant) dan keyin <u>ot</u> kerak: "
                "\"a significant <strong>growth</strong>\". \"grow\" fe'l, \"growing\" "
                "sifat/-ing — grammatik jihatdan mos emas. So'z turini bashorat qilish "
                "aynan shu tuzoqni yechadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Qutida 8 so'z bor, lekin summaryda faqat "
                "5 bo'sh joy. Ortiqcha 3 so'z haqida nima deyish mumkin?</p>"
            ),
            "choices": [
                {"text": "Ular xatolik — e'tibor bermaslik kerak", "is_correct": False},
                {"text": "Ular ataylab qo'yilgan chalg'ituvchilar — ma'nan yaqin yoki word-form jihatdan yaqin so'zlar tuzoq bo'lishi mumkin", "is_correct": True},
                {"text": "Ularni ham biror joyga tiqishtirish kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ataylab qo'yilgan "
                "chalg'ituvchilar.</mark> Qutili versiyada har doim bo'sh joydan ko'proq "
                "so'z beriladi — ortiqchalar tuzoq. Ular ko'pincha to'g'ri javobga ma'nan "
                "yaqin (absorb vs reflect) yoki word-form jihatdan yaqin (growth vs grow) "
                "bo'ladi. Har bo'sh joyni <u>ma'no + grammatika</u> bilan tekshiring — "
                "shunda tuzoqlar o'z-o'zidan chetda qoladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a summary</div><div class=\"pp-card-back\">qisqacha bayon, xulosa</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to reflect (light)</div><div class=\"pp-card-back\">(nurni) qaytarmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to absorb</div><div class=\"pp-card-back\">yutmoq, singdirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">crop failure</div><div class=\"pp-card-back\">hosilning nobud bo'lishi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">word form</div><div class=\"pp-card-back\">so'z shakli (ot/fe'l/sifat)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">growth (noun)</div><div class=\"pp-card-back\">o'sish (ot)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">eruption</div><div class=\"pp-card-back\">otilish (vulqon)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">widespread</div><div class=\"pp-card-back\">keng tarqalgan</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Summary matnni paraphrase qiladi — so'zma-so'z qidirmang; langar + ma'no bilan toping.</li>"
            "<li>Skan qilishdan oldin har bo'sh joyning so'z turini (ot/fe'l/sifat/son) bashorat qiling.</li>"
            "<li>Matndan versiyada — aynan ko'chiring; qutili versiyada — to'g'ri word-form'ni tanlang.</li>"
            "<li>Word-form tuzog'i: grow/growth/growing — grammatika to'g'ri shaklni aytadi.</li>"
            "<li>Qutida ortiqcha so'zlar bor — ular ataylab qo'yilgan chalg'ituvchilar.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 25 (order 62 — Note / Table / Flow-Chart Completion)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_COMPLETION,
    "title": "IELTS Reading 25: Note, Table and Flow-Chart Completion — Following Non-Linear Layouts",
    "summary": "Chiziqli bo'lmagan tuzilmalar: eslatma/jadval/oqim-diagrammasidagi bo'sh joylarni sarlavha va tuzilma bo'ylab to'ldirish.",
    "order": 62,
    "blocks": [
        {"rich_text": (
            "<h2>Bir xil qoida, boshqa tuzilma</h2>"
            "<p>Note, Table va Flow-Chart Completion — Sentence/Summary Completion bilan "
            "<u>bir xil qoidalarga</u> bo'ysunadi: matndan aynan so'z, so'z chegarasi, "
            "to'g'ri imlo. Farqi — javoblar <mark style=\"background:#dbeafe;\">chiziqli "
            "matn emas, tuzilma</mark> ichida: eslatma (bullet), jadval (qator/ustun) "
            "yoki oqim-diagrammasi (strelka bilan bosqichlar).</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — chiziqli emas:</strong> jadvalda javoblar yuqoridan "
            "pastga tartibda BO'LMASLIGI mumkin — tuzilma o'z mantig'iga ega. "
            "Sarlavhalar va yorliqlar (labels) — sizning yo'l xaritangiz.</div>"
        )},
        {"rich_text": (
            "<h3>Uch tuzilma — har biriga alohida yondashuv</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Notes (eslatmalar).</strong> Sarlavha + "
            "bullet nuqtalari, ko'pincha to'liq bo'lmagan jumlalar. Har bullet — matnning "
            "bir qismi. <u>Sarlavha va oldingi so'zlar</u> qaysi joyni qidirishni "
            "aytadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Table (jadval).</strong> Qator va "
            "ustunlar bir mantiqni tuzadi (masalan: ustunlar = davrlar, qatorlar = "
            "xususiyatlar). Bo'sh katakning <u>qator sarlavhasi + ustun sarlavhasi</u> "
            "ikkovini birlashtiring — u aynan nima qidirishni aytadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Flow-chart (oqim-diagrammasi).</strong> "
            "Strelkalar bilan bog'langan bosqichlar — biror <u>jarayon yoki ketma-ketlik</u> "
            "(masalan, ishlab chiqarish bosqichlari). Bu odatda matnda "
            "<u>xronologik/tartibli</u> beriladi — strelka yo'nalishida qidiring.</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> tuzilmani to'ldirishdan oldin uni bir necha "
            "soniya <u>o'qib chiqing</u> — u nima haqida, qanday tashkil etilgan? "
            "Sarlavhalar sizga matnning qaysi qismiga borishni aytadi.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — Flow-chart (jarayon)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"To make traditional paper, "
            "the bark is first stripped from the mulberry tree and soaked in water for "
            "several days. It is then boiled with ash to soften the fibres. Workers beat "
            "the softened bark with wooden mallets until it forms a smooth pulp, which is "
            "finally spread on frames and left to dry in the sun.\"</p>"
            "</div>"
            "<p><strong>Flow-chart (NO MORE THAN TWO WORDS each):</strong></p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\">Bark stripped from tree → soaked in <u>(1) ______</u> for several days</p>"
            "<p style=\"margin:0 0 4px;\">↓</p>"
            "<p style=\"margin:0 0 4px;\">Boiled with <u>(2) ______</u> to soften fibres</p>"
            "<p style=\"margin:0 0 4px;\">↓</p>"
            "<p style=\"margin:0 0 4px;\">Beaten with <u>(3) ______</u> into a pulp</p>"
            "<p style=\"margin:0 0 4px;\">↓</p>"
            "<p style=\"margin:0;\">Pulp spread on frames and dried in the <u>(4) ______</u></p>"
            "</div>"
            "<p>Javoblar strelka yo'nalishi = matn tartibida: (1) <mark style=\"background:#dcfce7;\">water</mark>, "
            "(2) <mark style=\"background:#dcfce7;\">ash</mark>, (3) <mark style=\"background:#dcfce7;\">wooden mallets</mark> "
            "(2 so'z, chegaraga to'g'ri), (4) <mark style=\"background:#dcfce7;\">sun</mark>. Har biri matndan aynan.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Table Completion'da bo'sh katakni "
                "to'ldirish uchun eng ishonchli usul qaysi?</p>"
            ),
            "choices": [
                {"text": "Matnni yuqoridan pastga o'qib, birinchi mos so'zni yozaman", "is_correct": False},
                {"text": "Katakning qator sarlavhasi va ustun sarlavhasini birlashtirib, aynan nima qidirishni aniqlayman", "is_correct": True},
                {"text": "Qo'shni kataklardagi so'zlarni takrorlayman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: qator + ustun "
                "sarlavhasini birlashtirish.</mark> Jadval — chiziqli emas: har katak "
                "ikki o'lchov kesishmasi (masalan qator=\"narx\", ustun=\"1990-yil\"). "
                "Ikkovini birlashtirsangiz, aniq nima qidirayotganingizni bilasiz "
                "(\"1990-yildagi narx\") va matndan o'sha ma'lumotni topasiz. Yuqoridan "
                "pastga o'qish — jadvalda ishlamaydi, javoblar tartibsiz bo'lishi "
                "mumkin.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Matn: <em>\"Once the application is "
                "received, it is reviewed by a panel, which either approves it or returns "
                "it to the applicant for revision.\"</em> Flow-chart: <em>\"Application "
                "received → reviewed by a ______ → approved or returned.\"</em> (ONE WORD) "
                "Javob?</p>"
            ),
            "choices": [
                {"text": "committee", "is_correct": False},
                {"text": "panel", "is_correct": True},
                {"text": "applicant", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: panel.</mark> "
                "Bashorat: \"reviewed by a ______\" → ot (kim ko'rib chiqadi). Matnda "
                "aynan \"reviewed by a <u>panel</u>\" — bir so'z, chegaraga to'g'ri. "
                "\"committee\" — ma'nan yaqin, lekin matnda YO'Q (o'z so'zingiz — xato). "
                "\"applicant\" — so'z-tuzoq: matnda bor, lekin u ariza <u>beruvchi</u>, "
                "ko'rib chiquvchi emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Flow-chart javoblarini topishda qaysi "
                "xususiyat eng ko'p yordam beradi?</p>"
            ),
            "choices": [
                {"text": "Bosqichlar odatda matnda xronologik (tartibli) tasvirlanadi — strelka yo'nalishida qidirasiz", "is_correct": True},
                {"text": "Flow-chart javoblari har doim bitta paragrafda bo'ladi", "is_correct": False},
                {"text": "Javoblar har doim son bo'ladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: xronologik "
                "tartib.</mark> Flow-chart jarayonni (bosqichma-bosqich) ko'rsatadi, va "
                "matn ham odatda o'sha jarayonni <u>tartib bilan</u> bayon qiladi. Demak "
                "strelka yo'nalishi = matndagi o'qish yo'nalishi: birinchi bo'sh joyni "
                "topgach, keyingisini pastdan (matnda keyinroq) qidiring. Bu qidiruvni "
                "juda tezlashtiradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a flow-chart</div><div class=\"pp-card-back\">oqim-diagrammasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a stage / a step</div><div class=\"pp-card-back\">bosqich, qadam</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to strip bark</div><div class=\"pp-card-back\">po'stloqni shilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to soak</div><div class=\"pp-card-back\">ivitmoq, botirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">pulp</div><div class=\"pp-card-back\">bo'tqa, massa</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a panel</div><div class=\"pp-card-back\">hay'at, komissiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to approve / to review</div><div class=\"pp-card-back\">tasdiqlamoq / ko'rib chiqmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a column / a row</div><div class=\"pp-card-back\">ustun / qator</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Note/Table/Flow-chart — Completion qoidalari bir xil (matndan so'z, chegara, imlo), lekin tuzilma boshqa.</li>"
            "<li>Table: qator + ustun sarlavhasini birlashtirib, aynan nima qidirishni aniqlang.</li>"
            "<li>Flow-chart: bosqichlar odatda matnda xronologik — strelka yo'nalishida qidiring.</li>"
            "<li>Sarlavhalar va yorliqlar — matnning qaysi qismiga borishni aytadigan yo'l xaritasi.</li>"
            "<li>Tuzilmani to'ldirishdan oldin uni bir marta o'qib, mantig'ini tushuning.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 26 (order 63 — Completion Full Passage Practice, mixed review)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_COMPLETION,
    "title": "IELTS Reading 26: Completion — Full Passage Practice (Mixed Review)",
    "summary": "To'liq matn ustida sentence, summary va flow-chart completion aralash amaliyot — so'z chegarasi, bashorat va imlo ko'nikmalarini birga.",
    "order": 63,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy sinov: uch completion turi birga</h2>"
            "<p>Sentence, summary va flow-chart completion'ni bitta to'liq matnda "
            "birlashtiramiz. Usullarni eslang: matndan AYNAN so'z (paraphrase emas!), "
            "so'z chegarasidan oshmang, so'z turini bashorat qiling, imloni aynan "
            "ko'chiring.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> har savolda so'z chegarasini o'qing — u har xil "
            "bo'lishi mumkin (ONE WORD / TWO WORDS). Javob yozgach, so'zlarini sanang.</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Story of Salt</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\"><strong>A.</strong> \"For most of human "
            "history, salt was a precious commodity. Because it prevents the growth of "
            "bacteria, it allowed people to preserve meat and fish long before "
            "refrigeration existed, making it essential for survival through the winter "
            "and for long sea voyages.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>B.</strong> \"Salt was so valuable "
            "that it shaped trade and even language. Roman soldiers were sometimes paid "
            "in salt, and the English word 'salary' derives from the Latin word for it. "
            "Great trade routes crossed the Sahara carrying salt southward, where in some "
            "West African markets it was once exchanged for an equal weight of gold.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>C.</strong> \"Traditional salt "
            "production was simple but slow. Seawater was channelled into shallow clay "
            "ponds and left under the sun. As the water gradually evaporated, it left "
            "behind a crust of salt crystals, which workers then raked into piles and "
            "carried away to dry fully in the open air.</p>"
            "<p style=\"margin:0;\"><strong>D.</strong> \"Today salt is cheap and "
            "abundant, produced on an industrial scale. Yet doctors now warn that most "
            "people eat far too much of it: a diet high in salt raises blood pressure, "
            "which in turn increases the risk of heart disease. The substance that once "
            "preserved life is, in excess, a modern health concern.\"</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>1-qism — Sentence Completion</h3>"
            "<p>Bo'sh joyni matndan <strong>NO MORE THAN TWO WORDS</strong> bilan "
            "to'ldiring.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> <em>\"Salt was used to preserve food "
                "because it stops the growth of ______.\"</em></p>"
            ),
            "choices": [
                {"text": "bacteria", "is_correct": True},
                {"text": "meat and fish", "is_correct": False},
                {"text": "refrigeration", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: bacteria.</mark> "
                "Bashorat: \"growth of ______\" → ot. A paragraf: \"it prevents the "
                "<u>growth of bacteria</u>\" — aynan mos, 1 so'z. \"meat and fish\" — "
                "so'z-tuzoq (saqlanadigan narsa, o'sadigan emas), \"refrigeration\" — "
                "boshqa kontekst (irrelevant).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <em>\"The English word 'salary' comes from "
                "the ______ word for salt.\"</em></p>"
            ),
            "choices": [
                {"text": "Roman", "is_correct": False},
                {"text": "Latin", "is_correct": True},
                {"text": "English", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Latin.</mark> "
                "Bashorat: \"the ______ word\" → sifat/ot (til nomi). B paragraf: "
                "\"derives from the <u>Latin</u> word for it\" — aynan. \"Roman\" — "
                "so'z-tuzoq (askarlar rimlik edi, lekin so'z lotincha), \"English\" — "
                "so'z 'salary' inglizcha, lekin u LOTINchadan kelgan.</p>"
            ),
        },
        {"rich_text": (
            "<h3>2-qism — Flow-Chart Completion</h3>"
            "<p>C paragrafdagi jarayon. Har bo'sh joyni <strong>ONE WORD</strong> bilan "
            "to'ldiring.</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\">Seawater channelled into shallow clay <u>(3) ______</u></p>"
            "<p style=\"margin:0 0 4px;\">↓</p>"
            "<p style=\"margin:0 0 4px;\">Water slowly <u>(4) ______</u> in the sun</p>"
            "<p style=\"margin:0 0 4px;\">↓</p>"
            "<p style=\"margin:0;\">Salt crystals raked into piles and dried in the open air</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> (3) bo'sh joyga qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "ponds", "is_correct": True},
                {"text": "seawater", "is_correct": False},
                {"text": "crystals", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ponds.</mark> "
                "Bashorat: \"shallow clay ______\" → ot (nima). C paragraf: \"channelled "
                "into shallow clay <u>ponds</u>\" — aynan, 1 so'z. \"seawater\" — jarayonda "
                "oldingi bosqich, \"crystals\" — keyingi bosqich. Flow-chart tartibi = "
                "matn tartibi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> (4) bo'sh joyga qaysi so'z? "
                "<em>(\"Water slowly ______ in the sun\")</em></p>"
            ),
            "choices": [
                {"text": "evaporated", "is_correct": True},
                {"text": "channelled", "is_correct": False},
                {"text": "raked", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: evaporated.</mark> "
                "Bashorat: \"water slowly ______\" → fe'l. C paragraf: \"As the water "
                "gradually <u>evaporated</u>\" (gradually = slowly paraphrase, lekin bo'sh "
                "joyga tushadigan fe'l matnda aynan \"evaporated\"). \"channelled\" — "
                "oldingi bosqich, \"raked\" — keyingi bosqich (kristallarni). Imloni aynan "
                "ko'chiring: e-v-a-p-o-r-a-t-e-d.</p>"
            ),
        },
        {"rich_text": (
            "<h3>3-qism — Summary Completion</h3>"
            "<p>D paragrafning xulosasi. <strong>NO MORE THAN TWO WORDS</strong>.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <em>\"Although salt is now inexpensive, "
                "eating too much of it can raise ______, leading to a higher risk of "
                "heart disease.\"</em></p>"
            ),
            "choices": [
                {"text": "blood pressure", "is_correct": True},
                {"text": "health concern", "is_correct": False},
                {"text": "industrial scale", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: blood pressure.</mark> "
                "Bashorat: \"raise ______\" → ot (nima ko'tariladi). D paragraf: \"raises "
                "<u>blood pressure</u>, which in turn increases the risk of heart "
                "disease\" — aynan, 2 so'z (chegaraga to'g'ri). Summary paraphrase "
                "qilgan (inexpensive = cheap, eating too much = eat far too much), lekin "
                "bo'sh joyga tushadigan so'z matnda aynan \"blood pressure\". Qolganlari "
                "— so'z-tuzoqlar (matnda bor, lekin \"raise\" ga mos emas).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — a'lo! Uch completion turini ham to'liq egalladingiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3–4/5</strong> — yaxshi; so'z chegarasi va imloni qayta tekshiring — eng ko'p ball shu yerda yo'qoladi.</p>"
            "<p style=\"margin:0;\"><strong>2/5 yoki kam</strong> — 23–25-darslarga qaytib, so'z turini bashorat qilish usulini takrorlang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a commodity</div><div class=\"pp-card-back\">tovar, mahsulot</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to preserve</div><div class=\"pp-card-back\">saqlab qolmoq, konservalamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to derive from</div><div class=\"pp-card-back\">~dan kelib chiqmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to evaporate</div><div class=\"pp-card-back\">bug'lanmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">abundant</div><div class=\"pp-card-back\">mo'l-ko'l, serob</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">blood pressure</div><div class=\"pp-card-back\">qon bosimi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in excess</div><div class=\"pp-card-back\">haddan ortiq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a sea voyage</div><div class=\"pp-card-back\">dengiz safari</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Har savolda so'z chegarasini alohida o'qing (ONE / TWO WORDS) — yozgach sanang.</li>"
            "<li>So'z turini bashorat qiling: bo'sh joydan oldin/keyin kelgan so'z turni aytadi.</li>"
            "<li>Javob matndan aynan — paraphrase yoki o'z so'zingiz emas; imloni harfma-harf ko'chiring.</li>"
            "<li>Flow-chart bosqichlari matn tartibida keladi — strelka yo'nalishida qidiring.</li>"
            "<li>So'z-tuzoq: variant matnda bor, lekin bo'sh joyning grammatika/ma'nosiga mos emas.</li>"
            "</ul>"
        )},
    ],
},

]
