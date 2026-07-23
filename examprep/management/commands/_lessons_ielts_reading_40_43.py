"""
IELTS Reading lessons 16-19 (orders 40-43) — the whole "Ma'lumotni moslashtirish
(Matching Information / Features / Sentence Endings)" topic — fourth batch,
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

TOPIC_MATCHING = {
    "title":   "Ma'lumotni moslashtirish (Matching Information / Features / Sentence Endings)",
    "summary": "Bayonotni to'g'ri paragraf, ism/sana yoki jumla oxiriga ulash — "
               "grammatika va paraphrase filtri bilan.",
    "icon":    "bi-diagram-3",
    "order":   5,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 16 (order 40 — Matching Information)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MATCHING,
    "title": "IELTS Reading 16: Matching Information — Locating Specific Details Across Paragraphs",
    "summary": "Bayonot qaysi paragrafda ekanini topish: axborot TURINI tanish, tartibsiz javoblar va paraphrase bilan ishlash.",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Matching Information nima?</h2>"
            "<p>Sizga bir nechta <strong>bayonot</strong> beriladi (masalan: <em>\"a "
            "reference to a widely held but mistaken belief\"</em>) va harflar bilan "
            "belgilangan paragraflar (A, B, C...). Vazifa: har bayonotdagi ma'lumot "
            "<u>qaysi paragrafda</u> berilganini topish. Sarlavha emas — <mark "
            "style=\"background:#dbeafe;\">aniq detal</mark> qidiryapsiz.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — ikki muhim farq:</strong> (1) javoblar <u>matn "
            "tartibida EMAS</u> — 1-bayonot F paragrafda, 2-bayonot A paragrafda "
            "bo'lishi mumkin. (2) Rubrikani o'qing: <em>\"You may use any letter more "
            "than once\"</em> desa — bitta paragraf bir necha bayonotga javob "
            "bo'lishi mumkin.</div>"
            "<p>Aynan shu ikki xususiyat bu turni <strong>eng ko'p vaqt oladigan</strong> "
            "savolga aylantiradi. Shuning uchun oltin qoida: Matching Information'ni "
            "parchaning <u>oxirida</u> ishlang — Matching Headings yoki T/F/NG'ni "
            "yechganingizda matn xaritasi allaqachon miyangizda bo'ladi.</p>"
        )},
        {"rich_text": (
            "<h3>Kalit tushuncha: axborot TURINI o'qing</h3>"
            "<p>Bayonot sizga faqat mavzuni emas, <u>axborot turini</u> aytadi — matndan "
            "aynan nima ko'rinishdagi gapni qidirishni. Buni ilg'ash — yarim g'alaba:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>an example of ~</strong> → misol qidiring (for instance, such as)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>a reason for ~</strong> → sabab qidiring (because, due to, this is why)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>a comparison between ~</strong> → taqqoslash (whereas, compared with, unlike)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>a definition of ~</strong> → ta'rif (is defined as, refers to, means)</p>"
            "<p style=\"margin:0 0 6px;\"><strong>a prediction about ~</strong> → kelajak (is likely to, could, by 2050)</p>"
            "<p style=\"margin:0;\"><strong>a criticism / a benefit of ~</strong> → salbiy / ijobiy baho</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> bayonotlar deyarli har doim <u>og'ir "
            "paraphrase</u> qilingan — matndagi so'zlarni topib bo'lmaydi. \"A "
            "mistaken belief\" matnda \"people often wrongly assume that...\" ko'rinishida "
            "turadi. Demak so'z emas — <u>g'oya</u> qidiring.</div>"
        )},
        {"rich_text": (
            "<h3>Usul — bosqichma-bosqich</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Bayonotni o'qib, "
            "<u>ikkita narsani</u> aniqlang: axborot TURI (misol? sabab? taqqoslash?) va "
            "MAVZU (nima haqida). Ikkovini xayolan belgilab qo'ying.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Agar Matching "
            "Headings'ni oldin ishlagan bo'lsangiz — qaysi paragraf shu mavzuga tegishli "
            "ekanini taxminan bilasiz. To'g'ri o'sha yerdan boshlang.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> O'sha paragrafda "
            "kerakli TURDAGI gapni qidiring — g'oyani solishtiring, so'zni emas. Mos "
            "kelsa — harfni yozing.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Oson bayonotlarni avval "
            "hal qiling, qiyinlarini oxiriga qoldiring. Har topilgan javob qidiruv "
            "maydonini toraytiradi.</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> ikkita paragraf bir xil mavzuni gapirsa (masalan, "
            "ikkovi ham iqtisod haqida), <u>axborot turi</u> ularni ajratadi: qaysi "
            "birida aynan \"misol\" bor, qaysida \"sabab\". Tur — sizning eng aniq "
            "filtringiz.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — turni his qiling</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>A.</strong> \"For decades, coffee was "
            "treated with suspicion by doctors, who linked it to heart disease and "
            "advised patients to cut it out.\"</p>"
            "<p style=\"margin:0;\"><strong>B.</strong> \"More recent studies, however, "
            "have found the opposite: moderate coffee drinkers appear to live slightly "
            "longer than non-drinkers, one large European survey reported.\"</p>"
            "</div>"
            "<p><strong>Bayonot:</strong> <em>\"a reference to research that contradicts "
            "an earlier view\"</em>. Qaysi paragraf?</p>"
            "<p>Axborot turi = <u>oldingi qarashga ZID tadqiqot</u>. A paragraf eski "
            "qarashni beradi; B paragraf esa \"More recent studies, however, have found "
            "the <u>opposite</u>\" — bu aniq \"contradicts an earlier view\". Javob: "
            "<strong>B</strong>. Diqqat: \"research\" so'zi A'da ham bor (doctors "
            "linked...), lekin ZID g'oyasi faqat B'da.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Matching Information savolini qachon "
                "ishlash eng oqilona?</p>"
            ),
            "choices": [
                {"text": "Birinchi bo'lib — shunda matnni chuqur o'qib olaman", "is_correct": False},
                {"text": "Oxirida — javoblar tartibsiz va vaqt talab qiladi; boshqa savollar matn xaritasini beradi", "is_correct": True},
                {"text": "O'rtada — Matching Headings bilan bir vaqtda", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: oxirida.</mark> "
                "Matching Information javoblari matn tartibida emas, ya'ni har bayonot "
                "uchun butun matnni titish mumkin — bu eng qimmat (vaqt jihatdan) savol "
                "turi. Agar Matching Headings/T-F-NG'ni oldin ishlagan bo'lsangiz, qaysi "
                "paragraf nima haqidaligini bilasiz — endi to'g'ri joyga borasiz, ko'r-"
                "ko'rona qidirmaysiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Paragraf C: <em>\"Unlike wind farms, "
                "which can be built in a year or two, a new nuclear plant typically takes "
                "over a decade to complete and frequently runs far beyond its original "
                "budget.\"</em> Bu paragraf qaysi bayonotga eng mos?</p>"
            ),
            "choices": [
                {"text": "\"a description of how nuclear plants are built\"", "is_correct": False},
                {"text": "\"a comparison of the time needed for two energy sources\"", "is_correct": True},
                {"text": "\"an example of a successful wind farm\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"a comparison of "
                "the time needed for two energy sources\".</mark> Axborot turi = "
                "<u>taqqoslash</u>, va signal so'z aniq: \"<u>Unlike</u> wind farms... a "
                "nuclear plant typically takes over a decade\". Ikki manba (shamol va "
                "atom) vaqt bo'yicha solishtirilyapti. \"How plants are built\" — jarayon "
                "tavsifi emas (bu yerda faqat davomiylik), \"a successful wind farm\" — "
                "matnda muvaffaqiyat haqida gap yo'q.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"a mistaken assumption "
                "many people make\"</em>. Qaysi jumla bu axborot turiga mos?</p>"
            ),
            "choices": [
                {"text": "\"Scientists have known for years that the brain keeps developing into adulthood.\"", "is_correct": False},
                {"text": "\"It is widely believed that we use only ten per cent of our brains — a claim with no scientific basis whatsoever.\"", "is_correct": True},
                {"text": "\"The human brain weighs about 1.4 kilograms on average.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchi jumla.</mark> "
                "Axborot turi = <u>ko'pchilikning noto'g'ri taxmini</u>. Ikkinchi jumla "
                "aynan shu qolip: \"It is <u>widely believed</u> that... — a claim with "
                "<u>no scientific basis</u>\" = keng tarqalgan, lekin noto'g'ri ishonch. "
                "Birinchisi — olimlar ANIQ biladigan fakt (noto'g'ri emas), uchinchisi — "
                "oddiy statistik fakt. E'tibor bering: hech qaysida \"mistaken "
                "assumption\" so'zi yo'q — g'oyani paraphrase orqali topdingiz.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to locate information</div><div class=\"pp-card-back\">ma'lumotni topmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a widely held belief</div><div class=\"pp-card-back\">keng tarqalgan ishonch</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a mistaken assumption</div><div class=\"pp-card-back\">noto'g'ri taxmin</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to contradict</div><div class=\"pp-card-back\">zid kelmoq, rad etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a comparison</div><div class=\"pp-card-back\">taqqoslash</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to run beyond budget</div><div class=\"pp-card-back\">byudjetdan oshib ketmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">no scientific basis</div><div class=\"pp-card-back\">ilmiy asosi yo'q</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to treat with suspicion</div><div class=\"pp-card-back\">shubha bilan qaramoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Matching Information = bayonot qaysi PARAGRAFda ekanini topish; javoblar tartibsiz.</li>"
            "<li>Rubrikani o'qing: paragraf bir necha marta ishlatilishi mumkin (\"any letter more than once\").</li>"
            "<li>Bayonotdagi axborot TURINI o'qing (misol / sabab / taqqoslash / ta'rif) — bu eng aniq filtr.</li>"
            "<li>So'z emas, g'oya qidiring — bayonotlar og'ir paraphrase qilingan.</li>"
            "<li>Bu turni parchaning oxirida ishlang — u eng ko'p vaqt oladi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 17 (order 41 — Matching Features)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MATCHING,
    "title": "IELTS Reading 17: Matching Features — Names, Dates and Categories to Statements",
    "summary": "Bayonotni to'g'ri ism/sana/toifaga ulash: nomlarni langar sifatida ishlatish va \"kimning fikri\" tuzog'idan qochish.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>Matching Features nima?</h2>"
            "<p>Sizga <strong>bayonotlar</strong> va <strong>variantlar ro'yxati</strong> "
            "beriladi — ro'yxat odatda <u>ismlar</u> (tadqiqotchilar), <u>sanalar</u> "
            "(davrlar) yoki <u>toifalar</u> (A, B, C turlari) dan iborat. Vazifa: har "
            "bayonotni to'g'ri variantga ulash. Masalan: <em>\"Which researcher made "
            "which claim?\"</em></p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — rubrikani o'qing:</strong> ba'zan <em>\"NB You may "
            "use any option more than once\"</em> deyiladi — bir ism bir necha bayonotga "
            "javob bo'lishi mumkin. Ba'zan variantlar bayonotlardan ko'p — ortiqchasi "
            "ishlatilmaydi. Aksincha ham bo'ladi.</div>"
        )},
        {"rich_text": (
            "<h3>Sirli qurol: nomlar — langarlar</h3>"
            "<p>Matching Information'dan farqli o'laroq, bu tur <u>osonroq</u> — chunki "
            "variantlar (ismlar, sanalar) matnda <mark style=\"background:#dcfce7;\">"
            "aynan o'sha ko'rinishda</mark> turadi. Ism paraphrase qilinmaydi: "
            "\"Dr. Chen\" matnda ham \"Dr. Chen\". Bu — sizning langaringiz.</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Avval matnni tez skan "
            "qilib, <u>barcha ismlarni</u> (bosh harfli so'zlar) belgilab chiqing — ular "
            "ko'zga darhol tashlanadi. Endi har ism qayerda ekanini bilasiz.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Birinchi bayonotni "
            "o'qing. Uni ismga ulash uchun — o'sha ism atrofidagi gaplarni o'qing va "
            "g'oyani solishtiring (paraphrase!).</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> Bir ism bir necha marta "
            "chiqsa — barcha o'rinlarini tekshiring; bayonot ismning ikkinchi "
            "eslatilishiga tegishli bo'lishi mumkin.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Har ulangan bayonotni "
            "belgilab boring; \"more than once\" bo'lmasa — ishlatilgan ismni "
            "ro'yxatdan chiqarib tashlang.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>⚠️ Eng katta tuzoq: \"kimning fikri?\"</h3>"
            "<p>IELTS bir gapda ikki ismni yonma-yon qo'yadi va fikrni <u>bittasiga</u> "
            "tegishli qiladi — shoshgan talaba yaqin turgan ismni belgilaydi. Signal "
            "so'zlarga qarang:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Matn:</strong> \"<u>Roberts</u> argues "
            "that early language exposure is decisive. <u>Nolan</u>, by contrast, "
            "maintains that genetics plays the larger role.\"</p>"
            "<p style=\"color:#475569;margin:0 0 4px;\">Bayonot: <em>\"Genes matter more "
            "than environment.\"</em></p>"
            "<p style=\"color:#475569;margin:0;\">✅ Javob: <strong>Nolan</strong> — "
            "\"by contrast\" fikrni Roberts'dan Nolan'ga o'tkazadi. Roberts aynan "
            "teskarisini aytadi!</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> \"unlike X\", \"whereas X\", \"contrary to X\", "
            "\"X disagreed\" — bu so'zlardan keyingi fikr <u>X'niki EMAS</u>. Ism yaqinligi "
            "isbot emas; fikr egasini <em>signal so'z</em> aytadi.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Nega Matching Features odatda Matching "
                "Information'dan tezroq ishlanadi?</p>"
            ),
            "choices": [
                {"text": "Chunki bayonotlar qisqaroq bo'ladi", "is_correct": False},
                {"text": "Chunki ismlar/sanalar matnda aynan o'sha ko'rinishda turadi — ularni langar qilib tez topasiz", "is_correct": True},
                {"text": "Chunki javoblar har doim matn tartibida bo'ladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ismlar langar "
                "bo'ladi.</mark> Ism va sanalar — bosh harfli, ko'zga tashlanadigan va "
                "<u>paraphrase qilinmaydi</u>. \"Professor Adams\" matnda ham aynan "
                "\"Professor Adams\". Shuning uchun avval hamma ismni belgilab chiqasiz, "
                "keyin har bayonotni tegishli ism atrofidagi matnga solishtirasiz — bu "
                "aniq va tez. (Matching Features javoblari ham har doim tartibda emas, "
                "shuning uchun 3-variant xato.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Matn: <em>\"<u>Tanaka</u> claimed that "
                "city noise permanently damages children's concentration. <u>Weber</u> "
                "was sceptical, pointing out that Tanaka's sample was far too small to "
                "prove anything.\"</em> Bayonot: <em>\"criticised another study for its "
                "limited evidence.\"</em> Kimga tegishli?</p>"
            ),
            "choices": [
                {"text": "Tanaka", "is_correct": False},
                {"text": "Weber", "is_correct": True},
                {"text": "Ikkalasiga ham", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Weber.</mark> "
                "Bayonot = \"boshqa tadqiqotni kam dalil uchun tanqid qildi\". Aynan "
                "Weber shu ishni qiladi: \"<u>was sceptical</u>, pointing out that "
                "Tanaka's sample was <u>far too small</u>\" — bu \"limited evidence\" "
                "tanqidining paraphrase'i. Tanaka — tanqid qilingan (subyekt emas, obyekt). "
                "Ikki ism yonma-yon, lekin tanqidchi bitta: Weber.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Matching Features'da bir bayonotga "
                "ishonchingiz komil emas, ikki ism (Park va Lee) o'rtasida "
                "ikkilanyapsiz. Eng yaxshi keyingi qadam qaysi?</p>"
            ),
            "choices": [
                {"text": "Tasodifiy birini tanlab, keyingisiga o'taman", "is_correct": False},
                {"text": "Matnda Park va Lee eslatilgan HAR bir joyni topib, bayonot g'oyasini har biriga alohida solishtiraman", "is_correct": True},
                {"text": "Ro'yxatdagi eng birinchi ismni tanlayman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: har ikki ism "
                "eslatilgan joylarni tekshirish.</mark> Ism matnda bir necha marta "
                "chiqishi mumkin — bayonot ikkinchi yoki uchinchi eslatishga tegishli "
                "bo'lishi ham mumkin. Langar-usulning kuchi shunda: nomlarni belgilab "
                "qo'ygansiz, demak barcha o'rinlarni tez ko'rib chiqib, g'oyani aniq mos "
                "kelganida to'xtaysiz. Taxmin — oxirgi chora.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to attribute a view to sb</div><div class=\"pp-card-back\">fikrni birovga tegishli deb bilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to claim / to argue</div><div class=\"pp-card-back\">da'vo qilmoq / dalil keltirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">by contrast / whereas</div><div class=\"pp-card-back\">bundan farqli / holbuki</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">sceptical</div><div class=\"pp-card-back\">shubhali, ishonqiramaydigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to maintain (that)</div><div class=\"pp-card-back\">qat'iy turib aytmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a small sample</div><div class=\"pp-card-back\">kichik namuna (tadqiqotda)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">contrary to</div><div class=\"pp-card-back\">~ga qarama-qarshi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">decisive</div><div class=\"pp-card-back\">hal qiluvchi</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Matching Features = bayonotni ism / sana / toifaga ulash; variantlar langar.</li>"
            "<li>Avval matndagi barcha ismlarni belgilang — ular paraphrase qilinmaydi, tez topiladi.</li>"
            "<li>Eng katta tuzoq: yonma-yon ikki ism. \"by contrast / unlike X\" fikr egasini o'zgartiradi.</li>"
            "<li>Ism yaqinligi isbot emas — g'oyani signal so'zlar bilan tekshiring.</li>"
            "<li>Rubrikani o'qing: variant bir necha marta ishlatilishi mumkinmi?</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 18 (order 42 — Matching Sentence Endings)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MATCHING,
    "title": "IELTS Reading 18: Matching Sentence Endings — Grammar as a Filter",
    "summary": "Jumla boshini to'g'ri oxiriga ulash: grammatika birinchi filtr, matn ma'nosi ikkinchi; ortiqcha variantlarni chiqarib tashlash.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>Matching Sentence Endings nima?</h2>"
            "<p>Sizga <strong>jumla boshlari</strong> (1, 2, 3...) va <strong>jumla "
            "oxirlari</strong> ro'yxati (A, B, C...) beriladi. Vazifa: har boshni "
            "to'g'ri oxir bilan tugatish — shunday-ki, (1) hosil bo'lgan jumla "
            "<u>grammatik jihatdan to'g'ri</u> bo'lsin va (2) matndagi ma'noga "
            "<u>mos</u> kelsin.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Yaxshi xabar:</strong> jumla boshlari deyarli har doim "
            "<u>matn tartibida</u> beriladi — 1-jumla 2-jumladan oldinroq paragrafda. "
            "Bu Matching Information'dan katta yengillik: qidiruv maydoni tor.</div>"
        )},
        {"rich_text": (
            "<h3>Ikki filtr — grammatika + ma'no</h3>"
            "<p>Bu savol turining siri: <mark style=\"background:#dbeafe;\">grammatika "
            "ko'p variantni darrov chiqarib tashlaydi</mark>. Ma'noni tekshirishdan "
            "oldin, jumla boshiga grammatik jihatdan mos kelmaydigan oxirlarni "
            "o'chiring — ish yarmiga qisqaradi.</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam — grammatik filtr.</strong> Jumla "
            "boshini o'qing. U qanday davom etishni <u>talab qiladi</u>? Fe'lmi? Otmi? "
            "Birlik/ko'plik? Masalan \"<em>The scientists concluded that...</em>\" — "
            "keyin to'liq gap (subyekt+fe'l) kerak, yakka ot emas.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam — nomzodlarni siqib qo'ying.</strong> "
            "Ro'yxatdan grammatik jihatdan mumkin bo'lgan 2–3 oxirni ajrating; "
            "qolganlarini o'chiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam — matn filtri.</strong> Endi "
            "matnning tegishli qismini o'qing va qolgan nomzodlardan qaysi biri "
            "<u>ma'noga</u> mos kelishini tanlang (paraphrase!).</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam — qayta o'qing.</strong> To'liq "
            "jumlani (bosh + tanlangan oxir) ovoz chiqarib o'qigandek tekshiring: u "
            "ravon va matnga sodiqmi?</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Grammatik filtr — jonli misol</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>Jumla boshi:</strong> \"The new "
            "regulations were introduced in order to...\"</p>"
            "<p style=\"margin:0 0 4px;\">A. ...<em>a sharp fall in air pollution.</em> "
            "&nbsp;❌ (\"in order to\" + <u>ot</u> — grammatika buzildi)</p>"
            "<p style=\"margin:0 0 4px;\">B. ...<em>reduce traffic in the city centre.</em> "
            "&nbsp;✅ (\"in order to\" + <u>fe'l</u> — to'g'ri)</p>"
            "<p style=\"margin:0;\">C. ...<em>because cars were banned.</em> "
            "&nbsp;❌ (\"to\" + \"because\" — grammatika buzildi)</p>"
            "</div>"
            "<p>Ko'rdingizmi? Matnni umuman o'qimasdan, faqat grammatika bilan 3 tadan "
            "2 tasini o'chirdik. \"in order to\" faqat <u>fe'l</u> bilan davom etadi — "
            "demak javob B (agar matn tasdiqlasa). Har bosh o'ziga xos grammatik "
            "\"talab\" qo'yadi: \"which\" → ergash gap, \"a decision\" → to'ldiruvchi, "
            "\"is\" → sifat/ot.</p>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna — talab turlari:</strong><br>"
            "\"...led to <u>______</u>\" → ot yoki -ing (led to <em>an increase</em> / "
            "<em>rising costs</em>)<br>"
            "\"...researchers who <u>______</u>\" → fe'l (who <em>studied the data</em>)<br>"
            "\"...more expensive than <u>______</u>\" → ot/ot iborasi (than <em>the "
            "old method</em>)</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Matching Sentence Endings'da eng "
                "samarali BIRINCHI qadam qaysi?</p>"
            ),
            "choices": [
                {"text": "Har bir oxirni matndan izlab chiqish", "is_correct": False},
                {"text": "Jumla boshi grammatik jihatdan qanday davomni talab qilishini aniqlab, mos kelmaydigan oxirlarni o'chirish", "is_correct": True},
                {"text": "Oxirlarni alifbo tartibida sinab ko'rish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: grammatik "
                "filtr.</mark> Ko'p oxir jumla boshiga grammatik jihatdan umuman "
                "yopishmaydi (\"in order to\" + ot bo'lmaydi). Ularni matnni o'qimasdan "
                "o'chirib tashlash mumkin — bu qolgan 2–3 nomzodgagina matn tekshiruvini "
                "qoldiradi. Grammatika — sizning tez va bepul filtringiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Jumla boshi: <em>\"The survey revealed "
                "that most commuters...\"</em>. Qaysi oxir grammatik jihatdan mos "
                "keladi?</p>"
            ),
            "choices": [
                {"text": "...a growing preference for cycling.", "is_correct": False},
                {"text": "...would switch to public transport if it were cheaper.", "is_correct": True},
                {"text": "...because of the rising cost of petrol.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "\"...most commuters <u>______</u>\" — \"commuters\" (subyekt) dan keyin "
                "<u>fe'l</u> kerak. \"would switch...\" — fe'l bilan boshlanadi, to'g'ri "
                "jumla: \"most commuters would switch to public transport...\". "
                "Birinchisi ot iborasi (fe'l yo'q — \"commuters a growing preference\" "
                "buzuq), uchinchisi \"because\" bilan boshlanadi (\"commuters because\" — "
                "grammatika buzildi). Faqat grammatika bilan javobni topdik.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Grammatik filtrdan keyin 2 ta oxir "
                "qoldi — ikkovi ham jumla boshiga ravon ulanadi. Endi nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "Chiroyliroq eshitilganini tanlayman", "is_correct": False},
                {"text": "Matnning tegishli qismini o'qib, qaysi oxir matndagi g'oyani (paraphrase bilan) aks ettirishini tanlayman", "is_correct": True},
                {"text": "Uzunroq oxirni tanlayman — u ko'proq ma'lumot beradi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: matnni "
                "tekshirish.</mark> Grammatika — birinchi filtr, lekin u ko'pincha bir "
                "nechta imkoniyat qoldiradi. Yakuniy hakam — <u>matn</u>: to'g'ri oxir "
                "matndagi ma'lumotni aniq (garchi boshqa so'zlar bilan) takrorlaydi. "
                "\"Chiroyli eshitilishi\" yoki \"uzunligi\" — asossiz mezonlar; IELTS "
                "javobi har doim matn bilan tasdiqlanadi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in order to + verb</div><div class=\"pp-card-back\">~ maqsadida (+ fe'l)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to lead to + noun</div><div class=\"pp-card-back\">~ga olib kelmoq (+ ot)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a commuter</div><div class=\"pp-card-back\">qatnovchi (ishga borib-keluvchi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to reveal</div><div class=\"pp-card-back\">oshkor qilmoq, ko'rsatmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">regulations</div><div class=\"pp-card-back\">qoidalar, nizom</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">subject-verb agreement</div><div class=\"pp-card-back\">ega-kesim mosligi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a preference for</div><div class=\"pp-card-back\">~ni afzal ko'rish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to conclude that</div><div class=\"pp-card-back\">xulosaga kelmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Matching Sentence Endings = boshni to'g'ri oxir bilan tugatish (grammatika + ma'no).</li>"
            "<li>Boshlar odatda matn tartibida — qidiruv maydoni tor.</li>"
            "<li>Birinchi filtr — GRAMMATIKA: mos kelmaydigan oxirlarni matnsiz o'chiring.</li>"
            "<li>Ikkinchi filtr — MATN: qolgan nomzoddan matn ma'nosini aks ettiradiganini tanlang.</li>"
            "<li>Oxirlar boshlardan ko'p — ortiqchasi tuzoq; \"chiroyli eshitilishi\" mezon emas.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 19 (order 43 — Full Passage Practice, mixed review)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MATCHING,
    "title": "IELTS Reading 19: Matching Types — Full Passage Practice (Mixed Review)",
    "summary": "To'liq matn ustida uch matching turini birga: Matching Information + Features + Sentence Endings aralash amaliyot.",
    "order": 43,
    "blocks": [
        {"rich_text": (
            "<h2>Hammasini birga sinaymiz</h2>"
            "<p>Bu topikning uch turini — Matching Information, Matching Features va "
            "Matching Sentence Endings — bitta to'liq matnda birlashtiramiz. Haqiqiy "
            "imtihonda ular ko'pincha shu tartibda, bitta parcha ostida keladi. Usullarni "
            "eslang: axborot TURI (Information), ismlarni langar qilish + \"kimning "
            "fikri\" (Features), grammatik filtr (Endings).</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> avval matnni bir marta skim qiling (~2 daqiqa) — "
            "har paragrafning mavzusi va <u>ismlarni</u> belgilab chiqing. Keyin savollarga "
            "o'ting. Skim — bu topikda vaqtni tejashning asosiy siri.</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Return of the Wolf</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\"><strong>A.</strong> \"When the last wild wolf "
            "in Yellowstone National Park was shot in the 1920s, few Americans mourned "
            "it. Wolves were seen as vermin — a threat to livestock and a danger to "
            "people — and their removal was treated as a straightforward victory for "
            "civilisation.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>B.</strong> \"The consequences, "
            "however, unfolded slowly and unexpectedly. With no predator to control "
            "them, elk numbers exploded. The elk grazed heavily on young willow and "
            "aspen along the rivers, stripping the banks bare. Songbirds that nested in "
            "those trees grew scarce, and beavers, which depend on willow, all but "
            "vanished from the park.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>C.</strong> \"In 1995, after decades "
            "of debate, fourteen wolves were captured in Canada and released back into "
            "Yellowstone. Ecologist <u>Douglas Smith</u>, who led the reintroduction, "
            "expected the wolves to reduce elk numbers. What surprised him was the speed "
            "and reach of the change that followed.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>D.</strong> \"As wolves thinned the "
            "elk herds and pushed the survivors away from open valleys, the willows "
            "recovered. Beavers returned to build dams; the dams created ponds; the ponds "
            "supported fish, amphibians and waterfowl. <u>Mary Fletcher</u>, a botanist "
            "who has studied the park's plant life for twenty years, records that some "
            "riverbanks now carry five times as much vegetation as they did in 1995.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>E.</strong> \"Not everyone reads the "
            "story the same way. <u>Robert Hayes</u>, a wildlife biologist, cautions that "
            "the 'wolves fixed everything' narrative is too neat. Rainfall, fire history "
            "and a fall in human hunting, he argues, all shifted at the same time, and "
            "untangling one cause from another is far harder than the popular version "
            "admits.</p>"
            "<p style=\"margin:0;\"><strong>F.</strong> \"What is not disputed is that "
            "Yellowstone changed the debate. Before 1995, predators were widely regarded "
            "as something to be removed; today, restoring them is a serious tool of "
            "conservation, tried from Scotland to the Alps. Whatever its precise "
            "mechanism, the wolf's return taught ecologists to think in webs rather than "
            "in single threads.\"</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>1-qism — Matching Information</h3>"
            "<p>Quyidagi ma'lumot qaysi paragrafda (A–F)? <em>NB: har harf bir marta "
            "ishlatiladi.</em></p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> <em>\"a warning that a single cause is hard "
                "to isolate\"</em></p>"
            ),
            "choices": [
                {"text": "B", "is_correct": False},
                {"text": "E", "is_correct": True},
                {"text": "F", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: E.</mark> Axborot "
                "turi = <u>ogohlantirish</u> (bitta sababni ajratish qiyin). E paragrafda "
                "Hayes aynan buni aytadi: \"<u>cautions</u> that... untangling one cause "
                "from another is <u>far harder</u> than the popular version admits\". "
                "\"Untangling one cause\" = \"isolate a single cause\". F ham sabab haqida "
                "gapiradi, lekin u ogohlantirmaydi — kelishuvni (\"not disputed\") "
                "ta'kidlaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <em>\"an example of a species that "
                "disappeared as an indirect result of hunting wolves\"</em></p>"
            ),
            "choices": [
                {"text": "A", "is_correct": False},
                {"text": "B", "is_correct": True},
                {"text": "D", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B.</mark> Axborot "
                "turi = <u>bilvosita yo'qolgan tur misoli</u>. B paragraf zanjirni "
                "beradi: bo'ri yo'q → elk ko'paydi → tol yeb tugatildi → beaver "
                "\"<u>all but vanished</u>\" (deyarli yo'qoldi). Bu bo'ri otilishining "
                "bilvosita (indirect) oqibati. D paragraf teskarisini (qaytib kelishini) "
                "aytadi, A esa bo'rining o'zi haqida.</p>"
            ),
        },
        {"rich_text": (
            "<h3>2-qism — Matching Features (People)</h3>"
            "<p>Quyidagi fikrni to'g'ri odamga ulang: "
            "<strong>DS</strong> = Douglas Smith, <strong>MF</strong> = Mary Fletcher, "
            "<strong>RH</strong> = Robert Hayes.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> <em>\"was taken aback by how far-reaching "
                "the effects were.\"</em></p>"
            ),
            "choices": [
                {"text": "Douglas Smith (DS)", "is_correct": True},
                {"text": "Mary Fletcher (MF)", "is_correct": False},
                {"text": "Robert Hayes (RH)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Douglas Smith.</mark> "
                "C paragraf: Smith bo'rilar elkni kamaytirishini kutgan, lekin \"What "
                "<u>surprised him</u> was the speed and <u>reach</u> of the change\". "
                "\"Taken aback\" = hayratda qoldi = surprised; \"far-reaching\" = reach. "
                "Bu — Smith. Diqqat: fikr egasi aniq nomlangan, tuzoq yo'q — lekin "
                "keyingi savolda ehtiyot bo'ling.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> <em>\"believes the popular account gives "
                "wolves too much credit.\"</em></p>"
            ),
            "choices": [
                {"text": "Douglas Smith (DS)", "is_correct": False},
                {"text": "Mary Fletcher (MF)", "is_correct": False},
                {"text": "Robert Hayes (RH)", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Robert Hayes.</mark> "
                "E paragraf: Hayes \"cautions that the '<u>wolves fixed everything</u>' "
                "narrative is <u>too neat</u>\" va boshqa sabablarni (yomg'ir, yong'in, "
                "ov) sanaydi. \"Gives wolves too much credit\" = bo'rilarga ortiqcha "
                "baho beradi — aynan Hayes'ning tanqidi. Fletcher faqat o'simlik "
                "o'sishini qayd etadi (baho bermaydi), Smith esa ijobiy hayratda.</p>"
            ),
        },
        {"rich_text": (
            "<h3>3-qism — Matching Sentence Endings</h3>"
            "<p>Har jumla boshini (matnga ko'ra) to'g'ri oxir bilan tugating.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <em>\"Before the wolves were reintroduced, "
                "the growing elk population...\"</em></p>"
            ),
            "choices": [
                {"text": "...damaged the trees along the park's rivers.", "is_correct": True},
                {"text": "...because the willows had recovered.", "is_correct": False},
                {"text": "...a rapid increase in beaver numbers.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"...damaged the "
                "trees along the park's rivers.\"</mark> Ikki filtr: <u>grammatika</u> — "
                "\"population\" (ega) dan keyin fe'l kerak; \"...damaged\" (fe'l) ✅, "
                "\"...because\" ❌ (ega+because buzuq), \"...a rapid increase\" ❌ (ot "
                "iborasi, fe'l yo'q). <u>Matn</u> — B paragraf: elk \"grazed heavily... "
                "stripping the banks bare\" = daraxtlarga zarar yetkazdi. Grammatika 2 "
                "tasini, matn qolganini tasdiqladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 6.</strong> <em>\"Since 1995, the example of "
                "Yellowstone has...\"</em></p>"
            ),
            "choices": [
                {"text": "...encouraged conservationists elsewhere to restore predators.", "is_correct": True},
                {"text": "...too neat to be believed.", "is_correct": False},
                {"text": "...whereas hunting continued to fall.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"...encouraged "
                "conservationists elsewhere to restore predators.\"</mark> Grammatika: "
                "\"has <u>______</u>\" — perfect fe'l uchun -ed/-en shakli kerak; "
                "\"has <u>encouraged</u>\" ✅. \"has too neat\" ❌ (fe'l yo'q), \"has "
                "whereas\" ❌ (bog'lovchi). Matn — F paragraf: \"restoring them is a "
                "serious tool of conservation, <u>tried from Scotland to the Alps</u>\" = "
                "boshqa joylarda ham yirtqichlarni tiklashga undadi. Grammatika + matn "
                "birga.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>6/6</strong> — a'lo! Uch matching turini ham to'liq egalladingiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>4–5/6</strong> — yaxshi; xato turni aniqlab (Information? Features? Endings?), o'sha darsni takrorlang.</p>"
            "<p style=\"margin:0;\"><strong>3/6 yoki kam</strong> — 16–18-darslarga qayting, ayniqsa \"axborot turi\" va \"grammatik filtr\" bo'limlarini.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">vermin</div><div class=\"pp-card-back\">zararkunanda (hayvon)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">predator</div><div class=\"pp-card-back\">yirtqich</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to graze</div><div class=\"pp-card-back\">o'tlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to reintroduce</div><div class=\"pp-card-back\">qayta joylashtirmoq (turini)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">far-reaching</div><div class=\"pp-card-back\">keng qamrovli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to isolate a cause</div><div class=\"pp-card-back\">sababni ajratib olmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">conservation</div><div class=\"pp-card-back\">tabiatni muhofaza qilish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be taken aback</div><div class=\"pp-card-back\">hayratda qolmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Matni bir marta skim qiling: paragraf mavzulari + ismlarni belgilang — uchala tur uchun poydevor.</li>"
            "<li>Information: axborot TURINI o'qing (misol/sabab/ogohlantirish), so'z emas g'oya qidiring.</li>"
            "<li>Features: ismni langar qiling; \"cautions/by contrast\" fikr egasini aniqlaydi.</li>"
            "<li>Endings: grammatika bilan chiqarib tashlang, keyin matn bilan tasdiqlang.</li>"
            "<li>Har savol matn bilan isbotlanadi — hech qachon \"chiroyli eshitilishi\" bilan emas.</li>"
            "</ul>"
        )},
    ],
},

]
