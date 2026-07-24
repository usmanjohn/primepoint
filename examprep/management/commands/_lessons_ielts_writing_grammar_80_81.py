"""
IELTS Writing lessons 19-20 (orders 80-81) — the "Grammatika va o'z-o'zini tekshirish
(Common Mistakes & Self-Editing)" topic — eighth (final) Writing batch,
see toc_ielts_writing.txt. (Academic-only scope.) This finishes the IELTS Writing skill.

No audio, no charts. Kit: step-reveal (error→fix, the checklist) + flashcards + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_GRAMMAR = {
    "title":   "Grammatika va o'z-o'zini tekshirish (Common Mistakes & Self-Editing)",
    "summary": "Bandni cheklaydigan keng tarqalgan grammatik xatolar va vaqt bosimi "
               "ostida o'z inshoingizni tekshirish ro'yxati.",
    "icon":    "bi-pencil-square",
    "order":   9,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 19 (order 80 — common grammar mistakes)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_GRAMMAR,
    "title": "IELTS Writing 19: Common Grammar Mistakes That Cap Your Band",
    "summary": "Band 6'da ushlab qoluvchi tez-tez uchraydigan xatolar: ega-kesim mosligi, artikllar, sanoqsiz otlar, predloglar, run-on gaplar — aniqlik murakkablikdan muhim.",
    "order": 80,
    "blocks": [
        {"rich_text": (
            "<h2>Grammatika — aniqlik murakkablikdan muhim</h2>"
            "<p>Ko'p talaba band 6'da qoladi, chunki bir nechta <strong>takrorlanuvchi "
            "grammatik xato</strong> qiladi. Band 7 uchun \"a good proportion of "
            "error-free sentences\" kerak. Muhim tushuncha: <mark "
            "style=\"background:#dcfce7;\">to'g'ri oddiy gap</mark>, <mark "
            "style=\"background:#fee2e2;\">buzuq murakkab gapdan</mark> yaxshiroq.</p>"
        )},
        {"rich_text": (
            "<h3>Eng ko'p uchraydigan 6 xato</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi xatoni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Ega-kesim mosligi.</strong> "
            "❌ <em>\"People is...\"</em> → ✅ <em>\"People are...\"</em>. "
            "❌ <em>\"The number of cars <u>have</u> risen\"</em> → ✅ <em>\"...<u>has</u> "
            "risen\"</em> (ega = \"the number\", birlik).</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Artikllar (a/an/the).</strong> "
            "❌ <em>\"Government should build school\"</em> → ✅ <em>\"<u>The</u> government "
            "should build <u>a</u> school\" / \"schools\"</em>. Sanoqli birlik ot artikl "
            "yoki ko'plik talab qiladi.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Sanoqsiz otlar.</strong> "
            "❌ <em>\"informations, advices, researches\"</em> → ✅ <em>\"information, "
            "advice, research\"</em> (ko'plik olmaydi, \"a\" olmaydi).</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Predloglar.</strong> "
            "❌ <em>\"depend of, interested for, discuss about\"</em> → ✅ <em>\"depend "
            "<u>on</u>, interested <u>in</u>, discuss\" (predlogsiz)</em>.</p></div>"
            "<div class=\"pp-step\"><p><strong>5. Run-on / comma splice.</strong> "
            "❌ <em>\"Cars cause pollution, they should be limited.\"</em> (ikki gap, "
            "vergul bilan) → ✅ <em>\"Cars cause pollution<u>;</u> therefore, they should "
            "be limited.\"</em> yoki nuqta bilan ajrating.</p></div>"
            "<div class=\"pp-step\"><p><strong>6. So'z turkumi (word form).</strong> "
            "❌ <em>\"This is a benefit decision\"</em> → ✅ <em>\"a <u>beneficial</u> "
            "decision\"</em> (ot o'rniga sifat). succeed/success/successful ni "
            "farqlang.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Oltin qoida: aniqlik > murakkablik</h3>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Nega?</strong> Band 7 Grammatical Range & Accuracy'da "
            "<u>xatosiz gaplar ulushi</u> muhim. Agar har murakkab gapda 2 xato qilsangiz, "
            "band tushadi. Aralashtiring: ba'zi murakkab gaplar (ergash, passive, shart), "
            "lekin ularni <u>to'g'ri</u> yozing. Ishonchingiz komil bo'lmagan murakkab "
            "tuzilmadan ko'ra, to'g'ri oddiy gapni tanlang.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Qaysi gap TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "\"The number of tourists have increased.\"", "is_correct": False},
                {"text": "\"The number of tourists has increased.\"", "is_correct": True},
                {"text": "\"The number of tourist has increased.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"...has "
                "increased\".</mark> Ega = \"<u>the number</u>\" (birlik) → \"has\". "
                "\"tourists\" — ko'plik (of tourists). Birinchisi: \"have\" (mos emas); "
                "uchinchisi: \"tourist\" birlik bo'lib qolgan (ko'plik kerak). \"The "
                "number of + ko'plik + <u>has</u>\".</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Qaysi ibora grammatik jihatdan "
                "TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "\"I did a lot of researches and got many informations.\"", "is_correct": False},
                {"text": "\"I did a lot of research and got a lot of information.\"", "is_correct": True},
                {"text": "\"I did many research and got informations.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "\"research\" va \"information\" — <u>sanoqsiz</u> otlar: ko'plik (-s) "
                "olmaydi va \"many\" emas, \"much / a lot of\" bilan ishlatiladi. "
                "\"researches / informations\" — keng tarqalgan xato.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> \"Cars cause pollution, they should be "
                "banned.\" Bu qanday xato va qanday tuzatiladi?</p>"
            ),
            "choices": [
                {"text": "Xato yo'q", "is_correct": False},
                {"text": "Comma splice — ikki mustaqil gap vergul bilan ulangan; nuqta/nuqtali vergul yoki bog'lovchi kerak", "is_correct": True},
                {"text": "Artikl xatosi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: comma splice.</mark> "
                "Ikki to'liq gap faqat vergul bilan ulangan — bu xato. Tuzatish: "
                "\"Cars cause pollution<u>. Therefore, they</u> should be banned.\" yoki "
                "\"...pollution<u>, so they</u>...\" (bog'lovchi bilan). Vergul yolg'iz ikki "
                "gapni ulay olmaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit — Grammar reminders</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the number of X + has (singular)</div><div class=\"pp-card-back\">ega birlik → has</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">information / advice / research</div><div class=\"pp-card-back\">sanoqsiz — -s yo'q, \"a\" yo'q</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">depend on / interested in</div><div class=\"pp-card-back\">to'g'ri predloglar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">discuss (no \"about\")</div><div class=\"pp-card-back\">discuss + obyekt (predlogsiz)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a comma splice</div><div class=\"pp-card-back\">ikki gapni vergul bilan ulash (xato)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">succeed / success / successful</div><div class=\"pp-card-back\">fe'l / ot / sifat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">error-free sentences</div><div class=\"pp-card-back\">xatosiz gaplar (band 7 talabi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">accuracy over complexity</div><div class=\"pp-card-back\">aniqlik murakkablikdan muhim</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>6 keng tarqalgan xato: ega-kesim mosligi, artikl, sanoqsiz ot, predlog, comma splice, so'z turkumi.</li>"
            "<li>Band 7 = xatosiz gaplarning yaxshi ulushi; takrorlanuvchi xatolar bandni cheklaydi.</li>"
            "<li>To'g'ri oddiy gap buzuq murakkab gapdan yaxshiroq.</li>"
            "<li>O'z takroriy xatolaringizni bilib oling va ularga alohida e'tibor bering.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 20 (order 81 — self-editing checklist) — FINAL Writing lesson
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_GRAMMAR,
    "title": "IELTS Writing 20: Self-Editing Checklist Under Time Pressure",
    "summary": "Oxirgi ~5 daqiqada aniq ro'yxat bilan tekshirish: savolga to'liq javob, pozitsiya izchilligi, grammatika, imlo, so'z soni — tasodifiy o'qishdan ko'ra samaraliroq.",
    "order": 81,
    "blocks": [
        {"rich_text": (
            "<h2>Oxirgi 5 daqiqa — bepul ball</h2>"
            "<p>Har topshiriq oxirida <strong>~5 daqiqa</strong> tekshirishga qoldiring. "
            "Lekin matnni shunchaki qayta o'qish samarasiz — <mark "
            "style=\"background:#dbeafe;\">aniq ro'yxat</mark> bo'yicha tekshirish "
            "ko'proq xatoni topadi. Bu — hech qanday yangi bilim talab qilmaydigan bepul "
            "ball.</p>"
        )},
        {"rich_text": (
            "<h3>Tekshirish ro'yxati — tartib bilan</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi tekshiruv ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Savolga TO'LIQ javob berdimmi?</strong> "
            "(Task Response) Barcha qismlarga? \"Discuss both\" bo'lsa ikkovi + fikr? "
            "Ikki qismli bo'lsa ikkovi? — bu eng muhim tekshiruv.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Pozitsiyam aniq va IZCHILmi?</strong> "
            "Kirish, tana va xulosada bir xil pozitsiya?</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Paragraflar bormi?</strong> Kirish, "
            "2 tana, xulosa — aniq bo'lingan? Har tana paragrafida bitta g'oya?</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Grammatika — takroriy xatolar.</strong> "
            "Ega-kesim mosligi (people are), birlik/ko'plik, sanoqsiz otlar. Ayniqsa "
            "<u>o'zingiz ko'p qiladigan</u> xatoga qarang.</p></div>"
            "<div class=\"pp-step\"><p><strong>5. Artikllar (a/the).</strong> Sanoqli "
            "birlik ot artikl oldimi?</p></div>"
            "<div class=\"pp-step\"><p><strong>6. Imlo va tinish belgilari.</strong> "
            "Ko'p va mavzuviy so'zlar imlosi; bosh harflar, nuqtalar.</p></div>"
            "<div class=\"pp-step\"><p><strong>7. So'z soniga yetdimmi?</strong> "
            "Task 1 ≥150, Task 2 ≥250 (sal yuqori).</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Samarali tekshirish maslahatlari</h3>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Yuqori ta'sirli tekshiruvlarni birinchi qiling:</strong> avval "
            "Task Response (savolga to'liq javob) va pozitsiya izchilligi — bular bandga "
            "eng ko'p ta'sir qiladi. Keyin grammatika/imlo. Vaqt kam bo'lsa ham, kamida "
            "1-2 punktni tekshiring.</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Shaxsiy xato ro'yxati:</strong> mashq paytida o'zingiz ko'p "
            "qiladigan 3-4 xatoni yozib boring (masalan: artikl tushirib qoldirish, "
            "\"people is\"). Imtihonda aynan shularni birinchi tekshiring — bu eng "
            "tez ball qaytaradi.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Oxirgi 5 daqiqada avval nimani tekshirish "
                "eng foydali?</p>"
            ),
            "choices": [
                {"text": "Faqat chiroyli so'zlar qo'shish", "is_correct": False},
                {"text": "Savolga to'liq javob berilgani va pozitsiya izchilligi (eng yuqori ta'sirli)", "is_correct": True},
                {"text": "Qo'lyozmani chiroyliroq qilish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task Response + "
                "izchillik.</mark> Bular bandga eng katta ta'sir qiladi — savolning bir "
                "qismini o'tkazib yuborish yoki pozitsiya noizchilligi ko'p ball yeydi. "
                "Grammatika/imlo — keyingi bosqich. Yuqori ta'sirli tekshiruvni birinchi "
                "qiling.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Nega \"shaxsiy xato ro'yxati\" foydali?</p>"
            ),
            "choices": [
                {"text": "Tekshirishni o'zingiz ko'p qiladigan aniq xatolarga yo'naltiradi — tez va samarali", "is_correct": True},
                {"text": "So'z sonini oshiradi", "is_correct": False},
                {"text": "Faqat o'qituvchilar uchun", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: aniq xatolarga "
                "yo'naltiradi.</mark> Har kimning \"sevimli\" xatolari bor (artikl, "
                "ega-kesim...). Ularni oldindan bilsangiz, tekshirishda aynan shularni "
                "qidirasiz — tasodifiy o'qishdan ancha tezroq va ko'proq xato topadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Tekshirishda so'z soni Task 2'da 240 "
                "chiqdi. Nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "Qoldiraman — deyarli yetarli", "is_correct": False},
                {"text": "1-2 gap qo'shib 250+ ga chiqaraman — chegaradan kam yozish Task Response jarimasi", "is_correct": True},
                {"text": "Bir paragrafni o'chiraman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 250+ ga "
                "chiqaraman.</mark> 250 dan kam yozish (240 ham) Task Response jarimasiga "
                "olib keladi. Tekshirishda tez 1-2 mazmunli gap qo'shing (misol yoki "
                "tushuntirish) — chegaradan sal yuqori bo'lsin. Paragraf o'chirish "
                "vaziyatni yomonlashtiradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit — Self-editing</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to proofread</div><div class=\"pp-card-back\">xatolarni tekshirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a checklist</div><div class=\"pp-card-back\">tekshiruv ro'yxati</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">high-impact check</div><div class=\"pp-card-back\">yuqori ta'sirli tekshiruv</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">consistency of position</div><div class=\"pp-card-back\">pozitsiya izchilligi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a recurring error</div><div class=\"pp-card-back\">takrorlanuvchi xato</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to meet the word count</div><div class=\"pp-card-back\">so'z chegarasiga yetmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a slip / a typo</div><div class=\"pp-card-back\">e'tiborsizlik/imlo xatosi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">under time pressure</div><div class=\"pp-card-back\">vaqt bosimi ostida</div></div>"
            "</div>"
            "<h2>🎉 Tabriklaymiz — Writing kursini tugatdingiz!</h2>"
            "<p>Bu — IELTS Writing (Academic) bo'limining <strong>so'nggi darsi</strong>. "
            "Baholash mezonlaridan boshlab, Task 1 (grafik, jadval, jarayon, xarita), "
            "Task 2 (barcha insho turlari), lug'at-bog'lovchilar va grammatika-tekshirish "
            "— <u>hammasini</u> o'rgandingiz. Endi sizda to'liq yozuv-strategiyasi bor!</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Keyingi qadam:</strong> Writing — <u>yozib mashq qilish</u> bilan "
            "o'sadi. Har hafta 1-2 to'liq Task 1 + Task 2 vaqt bilan yozing, model "
            "javoblar bilan solishtiring, va shaxsiy xato ro'yxatingizni yuriting. "
            "Har xato — keyingi safar uchun dars. Omad, Band 7+! 🚀</p>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Oxirgi ~5 daqiqada aniq ro'yxat bilan tekshiring (tasodifiy o'qish emas).</li>"
            "<li>Avval yuqori ta'sirli tekshiruvlar: Task Response + pozitsiya izchilligi.</li>"
            "<li>Keyin grammatika/artikl/imlo va so'z soni.</li>"
            "<li>Shaxsiy xato ro'yxatini yuriting — o'zingiz ko'p qiladigan xatoga birinchi qarang.</li>"
            "</ul>"
        )},
    ],
},

]
