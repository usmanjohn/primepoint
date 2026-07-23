"""
IELTS Reading lesson 22 (topic: Ha / Yo'q / Berilmagan — completes it)
+ lessons 30-33 (topic: Sarlavhalarni moslashtirish — the whole Matching Headings
topic) — third batch, see toc_ielts_reading.txt.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_YNNG = {
    "title":   "Ha / Yo'q / Berilmagan (Yes / No / Not Given)",
    "summary": "Muallifning fikri va da'volarini YES / NO / NOT GIVEN sifatida aniqlash.",
    "icon":    "bi-chat-square-text",
    "order":   3,
}

TOPIC_HEADINGS = {
    "title":   "Sarlavhalarni moslashtirish (Matching Headings)",
    "summary": "Har bir paragrafga mos sarlavhani tanlash — asosiy g'oyani ushlash san'ati.",
    "icon":    "bi-list-ol",
    "order":   4,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 11 (order 22 — Y/N/NG full passage practice)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_YNNG,
    "title": "IELTS Reading 11: Yes/No/Not Given — Full Passage Practice (Mixed Review)",
    "summary": "To'liq munozarali parcha ustida YES/NO/NOT GIVEN aralash amaliyot — pozitsiya va hedging ko'nikmalarini birlashtirish.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy sinov: muallif bilan yuzma-yuz</h2>"
            "<p>Oldingi ikki darsda Y/N/NG'ning asosini o'rgandingiz: muallif "
            "<u>fikrini</u> topish (signal so'zlar), boshqalarning fikridan ajratish va "
            "<u>daraja</u>ni o'lchash (hedging shkalasi). Endi hammasi bitta to'liq "
            "munozarali parchada: 5 ta bayonot, aralash javoblar.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> munozarali matnni skim qilganda o'zingizga "
            "ikkita savol bering: <em>\"Muallif NIMANI himoya qilyapti?\"</em> va "
            "<em>\"Kimga QARSHI gapiryapti?\"</em> Bu ikki javob — parchaning skeleti; "
            "keyin har bayonotni shu skeletga solishtirasiz.</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Case Against Homework?</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\">\"Few educational rituals are as widely "
            "accepted, and as rarely questioned, as homework. Parents expect it, schools "
            "assign it, and its absence is often read as a sign of low standards. Yet the "
            "research on homework's benefits is far less conclusive than this consensus "
            "suggests. For primary-school children in particular, studies have repeatedly "
            "failed to find a strong link between time spent on homework and academic "
            "achievement. In my judgement, assigning long written tasks to eight-year-olds "
            "is not merely useless but counterproductive: it eats into time for play and "
            "sleep, both of which demonstrably matter for development.</p>"
            "<p style=\"margin:0 0 10px;\">The picture at secondary level is different. "
            "Here, moderate amounts of well-designed homework do appear to reinforce "
            "classroom learning, particularly in mathematics and languages. The key word, "
            "however, is 'moderate'. Beyond roughly ninety minutes a night, the returns "
            "seem to diminish rapidly, and some researchers suspect that very heavy "
            "homework loads may actively harm motivation. I would not go that far on the "
            "current evidence, but the possibility deserves serious study.</p>"
            "<p style=\"margin:0;\">What is beyond dispute, in my view, is that the "
            "quality of a task matters far more than its length. Ten thoughtful questions "
            "teach more than fifty repetitive ones. Schools that measure homework policy "
            "in hours rather than outcomes are, quite simply, measuring the wrong "
            "thing.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> <em>\"Homework for primary-school children "
                "does more harm than good.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": True},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: YES.</mark> "
                "Muallif ochiq pozitsiya bildirgan: <em>\"In my judgement, assigning long "
                "written tasks to eight-year-olds is not merely useless but "
                "<u>counterproductive</u>\"</em> — ya'ni foydasiz emas, hatto zararli "
                "(o'yin va uyqu vaqtini yeydi). \"Does more harm than good\" — aynan shu "
                "fikrning boshqa so'zlar bilan aytilishi. \"In my judgement\" signalini "
                "sezdingizmi?</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <em>\"At secondary level, more homework "
                "always brings better results.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NO.</mark> "
                "Bayonotdagi \"always\" — mutlaq so'z, xavf signali. Muallif aynan "
                "teskarisini aytadi: foyda <u>moderate</u> (me'yorida) bo'lgandagina bor, "
                "<em>\"Beyond roughly ninety minutes a night, the returns seem to "
                "diminish rapidly\"</em> — 90 daqiqadan keyin foyda tez kamayadi. "
                "\"Ko'proq = har doim yaxshiroq\" degan qarashga muallif ochiq qarshi — "
                "demak NO, NOT GIVEN emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> <em>\"The writer is convinced that heavy "
                "homework loads damage students' motivation.\"</em> YES, NO yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NO.</mark> Nozik "
                "holat — darajalarga qarang. \"Motivatsiyaga zarar\" degan fikr matnda "
                "bor, lekin u <u>boshqa tadqiqotchilarniki</u> (\"some researchers "
                "suspect\"). Muallif esa aniq masofa saqlaydi: <em>\"I would <u>not</u> go "
                "that far on the current evidence\"</em> — ya'ni muallif bunga "
                "<strong>ishonchi komil EMAS</strong>. Bayonot \"is convinced\" (ishonchi "
                "komil) deydi — muallif buni ochiq rad etgan, demak NO. Agar muallif bu "
                "haqda umuman gapirmaganida — NOT GIVEN bo'lardi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> <em>\"The quality of homework tasks matters "
                "more than how long they take.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": True},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: YES.</mark> "
                "Muallif buni eng kuchli darajada aytgan: <em>\"What is <u>beyond "
                "dispute</u>, in my view, is that the <u>quality</u> of a task matters "
                "<u>far more</u> than its length\"</em>. Bayonot ham xuddi shu darajada "
                "(matters more) — daraja mos, fikr mos: YES. \"beyond dispute\" = "
                "\"shubhasiz\" — 100% lik ishonch signali.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <em>\"Teachers should receive special "
                "training in designing homework tasks.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Muallif vazifa <u>sifati</u> muhimligini aytadi — va shundan "
                "\"o'qituvchilarni maxsus o'qitish kerak\" degan xulosa mantiqan kelib "
                "chiqqandek tuyulishi mumkin. Lekin bu — <u>sizning</u> xulosangiz: matnda "
                "o'qituvchilarni tayyorlash haqida bir og'iz ham fikr yo'q. Mantiqiy "
                "taxmin tuzog'i (T/F/NG darsidan eslaysizmi?) Y/N/NG'da ham xuddi shunday "
                "ishlaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — zo'r! Fikr-daraja tahlilini to'liq egalladingiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>4/5</strong> — yaxshi; ayniqsa 3-savol turidagi \"muallif vs boshqalar\" holatlarini takrorlang.</p>"
            "<p style=\"margin:0;\"><strong>3/5 yoki kam</strong> — 9–10-darslarga qaytib, signal so'zlar va hedging shkalasini qayta o'qing.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">rarely questioned</div><div class=\"pp-card-back\">kamdan-kam shubha qilinadigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">conclusive</div><div class=\"pp-card-back\">qat'iy, uzil-kesil (dalil)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">counterproductive</div><div class=\"pp-card-back\">teskari samara beradigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to reinforce</div><div class=\"pp-card-back\">mustahkamlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">diminishing returns</div><div class=\"pp-card-back\">kamayib boruvchi foyda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in my judgement</div><div class=\"pp-card-back\">mening bahoyimcha</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">beyond dispute</div><div class=\"pp-card-back\">bahssiz, shubhasiz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I would not go that far</div><div class=\"pp-card-back\">men unchalik uzoqqa bormagan bo'lardim</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Skim paytida skelet tuzing: muallif nimani himoya qiladi, kimga qarshi.</li>"
            "<li>\"Some researchers suspect...\" + \"I would not go that far\" = muallif o'zgalar fikridan masofa saqlayapti — bayonot uni muallifga taqsa, javob NO.</li>"
            "<li>Muallif fikridan kelib chiqadigan \"mantiqiy\" tavsiyalar — agar matnda aytilmagan bo'lsa — NOT GIVEN.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 12 (order 30 — opens the Matching Headings topic)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_HEADINGS,
    "title": "IELTS Reading 12: Intro to Matching Headings — Reading for Gist, Not Detail",
    "summary": "Matching Headings formatini tushunish va har paragrafning asosiy g'oyasini (gist) topish usuli.",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Matching Headings nima?</h2>"
            "<p>Sizga <strong>sarlavhalar ro'yxati</strong> (i, ii, iii... raqamlangan) "
            "va paragraflar (A, B, C...) beriladi. Vazifa: har paragrafga uning "
            "<u>asosiy g'oyasini</u> aks ettiruvchi sarlavhani tanlash. Bu savol turi "
            "parchadan <em>oldin</em> beriladi — va bu tasodif emas: uni "
            "<mark style=\"background:#dbeafe;\">boshqa savollardan oldin</mark> ishlash "
            "kerak.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — format faktlari:</strong> sarlavhalar soni paragraflar "
            "sonidan <u>ko'p</u> (masalan, 5 paragrafga 8 sarlavha) — ortiqchalari "
            "chalg'itish uchun. Har sarlavha faqat <u>bir marta</u> ishlatiladi. Ba'zan "
            "1–2 paragraf misol sifatida oldindan javoblangan bo'ladi — ularni qayta "
            "ishlatmang!</div>"
        )},
        {"rich_text": (
            "<h3>Gist — \"nima HAQIDA\" degani</h3>"
            "<p>Matching Headings'dagi eng katta xato — paragrafni <u>batafsil</u> "
            "o'qish. Sizga kerak narsa — <strong>gist</strong>: paragraf umumiy nima "
            "haqida. Buni 2-darsdagi skimming beradi:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Paragrafning "
            "<u>birinchi va oxirgi jumlasini</u> o'qing — ko'p hollarda asosiy g'oya "
            "shu ikkovidan birida.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> O'rtadan faqat "
            "<em>ko'z yugurtirib</em> o'ting: takrorlanayotgan so'zlar, ismlar, "
            "raqamlarga e'tibor bering — ular mavzuni tasdiqlaydi.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> Sarlavhalarga "
            "qaramasdan turib, paragraf g'oyasini <u>o'z so'zingiz bilan</u> bir jumlada "
            "ayting (xayolan, o'zbekchada bo'lsa ham!). Masalan: \"bu paragraf — muammo "
            "qanday boshlangani haqida\".</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Endi ro'yxatdan o'sha "
            "jumlangizga eng yaqin sarlavhani qidiring. Avval o'zingiz aytib, keyin "
            "qidirsangiz — chalg'ituvchi sarlavhalar sizni yo'ldan urolmaydi.</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> eng oson paragrafdan boshlang, eng qiyinini "
            "oxiriga qoldiring — har topilgan javob ro'yxatni qisqartiradi va qolganlarini "
            "osonlashtiradi.</div>"
        )},
        {"rich_text": (
            "<h3>Nega \"detal\" sarlavhasi noto'g'ri?</h3>"
            "<p>Chalg'ituvchi sarlavhalarning eng keng tarqalgan turi — paragrafdagi "
            "<u>bitta detal</u>ni sarlavha qilib qo'yish. Detal paragrafda <em>bor</em>, "
            "shuning uchun sarlavha \"tanish\" ko'rinadi — lekin u butun paragrafni "
            "qamramaydi. Solishtiring:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>Paragraf:</strong> \"Bees "
            "navigate using the sun, landmarks, and the earth's magnetic field. Recent "
            "experiments in Germany showed they can even detect electric fields around "
            "flowers.\"</p>"
            "<p style=\"color:#475569;margin:0 0 4px;\">✅ To'g'ri sarlavha: <em>\"How bees find "
            "their way\"</em> — butun paragrafni qamraydi.</p>"
            "<p style=\"color:#475569;margin:0;\">❌ Detal-tuzoq: <em>\"Research carried out in "
            "Germany\"</em> — faqat oxirgi jumla haqida.</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Matching Headings savolini qachon "
                "ishlash to'g'riroq?</p>"
            ),
            "choices": [
                {"text": "Eng oxirida — avval detal savollarni yechib, matnni yaxshi bilib olganda", "is_correct": False},
                {"text": "Birinchi bo'lib — paragraflarni skim qilish keyingi savollar uchun ham xarita beradi", "is_correct": True},
                {"text": "Farqi yo'q — savollar tartibi natijaga ta'sir qilmaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: birinchi "
                "bo'lib.</mark> Matching Headings baribir har paragrafni skim qilishga "
                "majbur qiladi — shu mehnatni boshida qilsangiz, natijada butun parchaning "
                "\"xaritasi\" hosil bo'ladi: qaysi paragraf nima haqida. Keyingi detal "
                "savollarda (T/F/NG, completion) qaysi paragrafga qarashni darhol "
                "bilasiz — ikki marta ishlamaysiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Paragraf: <em>\"The first bicycles had "
                "no pedals: riders pushed themselves along with their feet. Pedals "
                "arrived in the 1860s, the chain drive in the 1880s, and by 1900 the "
                "bicycle had taken on the shape we know today.\"</em> Qaysi sarlavha "
                "to'g'ri?</p>"
            ),
            "choices": [
                {"text": "\"The invention of the pedal\"", "is_correct": False},
                {"text": "\"How the bicycle developed over time\"", "is_correct": True},
                {"text": "\"Cycling in the twentieth century\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"How the bicycle "
                "developed over time\".</mark> Paragraf butun bir <u>rivojlanish "
                "yo'lini</u> beradi: pedalsiz → pedal (1860s) → zanjir (1880s) → hozirgi "
                "shakl (1900). \"The invention of the pedal\" — faqat bitta bosqich "
                "(detal-tuzoq!), \"Cycling in the twentieth century\" esa paragrafda "
                "deyarli yo'q davr — 1900-yil faqat yakuniy nuqta.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> 6 paragrafli matnga 9 ta sarlavha "
                "berilgan. 5 paragrafni ishonch bilan javobladingiz, oxirgisiga 4 ta "
                "sarlavha \"ortib qoldi\". Nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "Qolgan 4 sarlavhani navbat bilan paragrafga solishtirib, eng keng qamrovlisini tanlayman", "is_correct": True},
                {"text": "Paragrafni so'zma-so'z tarjima qilib chiqaman", "is_correct": False},
                {"text": "Avvalgi 5 javobimni ham qaytadan ko'rib chiqaman — bittasi noto'g'ridir", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: qolgan 4 tadan "
                "tanlash.</mark> Har topilgan javob keyingisini osonlashtiradi — oxirgi "
                "paragrafga endi 9 emas, 4 nomzod qoldi. Ularni birma-bir paragrafning "
                "gist'iga solishtiring: qaysi biri <u>butun</u> paragrafni qamraydi? "
                "So'zma-so'z tarjima — vaqt o'g'risi; 5 ta ishonchli javobni "
                "shubhalantirish esa asossiz vahima (agar aniq sabab bo'lmasa).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">gist</div><div class=\"pp-card-back\">asosiy mazmun, mag'iz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">heading</div><div class=\"pp-card-back\">sarlavha</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">distractor</div><div class=\"pp-card-back\">chalg'ituvchi (noto'g'ri variant)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to cover the whole paragraph</div><div class=\"pp-card-back\">butun paragrafni qamramoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">supporting detail</div><div class=\"pp-card-back\">yordamchi detal</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">landmark</div><div class=\"pp-card-back\">mo'ljal, taniqli belgi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to navigate</div><div class=\"pp-card-back\">yo'l topmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">chain drive</div><div class=\"pp-card-back\">zanjirli uzatma</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Sarlavhalar paragraflardan ko'p — ortiqchalari tuzoq; har biri bir marta ishlatiladi.</li>"
            "<li>Usul: 1- va oxirgi jumla → o'z so'zingiz bilan gist → keyin sarlavha qidirish.</li>"
            "<li>Detal-sarlavha eng keng tuzoq: paragrafda BOR, lekin butunini QAMRAMAYDI.</li>"
            "<li>Bu savol turini birinchi ishlang — u butun parchaning xaritasini beradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 13 (order 31 — eliminating distractor headings)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_HEADINGS,
    "title": "IELTS Reading 13: Eliminating Distractor Headings — Too Narrow, Too Broad, Wrong Focus",
    "summary": "Chalg'ituvchi sarlavhalarning 4 turini tanish va ularni tizimli chiqarib tashlash usuli.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>Dushmanni taniysizmi?</h2>"
            "<p>O'tgan darsda to'g'ri sarlavhani <em>topishni</em> o'rgandik. Bu darsda "
            "teskarisidan boramiz: <strong>noto'g'rilarini chiqarib tashlashni</strong> "
            "o'rganamiz. IELTS chalg'ituvchi sarlavhalarni tasodifiy yozmaydi — ular "
            "4 ta aniq qolipda yasaladi. Qoliplarni bilsangiz, ularni bir qarashda "
            "taniysiz.</p>"
        )},
        {"rich_text": (
            "<h3>4 xil chalg'ituvchi</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Juda tor (too narrow).</strong> "
            "Paragrafdagi <u>bitta detal</u> haqida — o'tgan darsda ko'rdik. Tekshiruv "
            "savoli: <em>\"Bu sarlavha paragrafning necha foizini qamraydi?\"</em> "
            "20% bo'lsa — tashlang.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Juda keng (too broad).</strong> "
            "Butun <u>matn</u> mavzusi haqida, lekin aynan shu paragraf undan torroq "
            "narsani aytadi. Masalan, matn \"uyqu\" haqida bo'lsa, \"The importance of "
            "sleep\" sarlavhasi <u>har qaysi</u> paragrafga yopishadi — demak, hech "
            "biriga aniq mos emas.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Noto'g'ri urg'u (wrong focus).</strong> "
            "Mavzu to'g'ri, lekin <u>qarash burchagi</u> boshqa: paragraf muammoning "
            "<em>sabablari</em> haqida, sarlavha esa <em>yechimlari</em> haqida. Bir "
            "so'z farqi (causes ↔ solutions, past ↔ future, benefits ↔ risks) — butun "
            "javobni o'zgartiradi.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. So'z-tuzoq (word match).</strong> "
            "Sarlavhada paragrafdagi <u>ko'zga tashlanadigan so'z</u> takrorlanadi — "
            "lekin g'oya boshqa. IELTS biladi: shoshgan talaba tanish so'zni ko'rsa, "
            "sarlavhani \"o'shanikiga\" beradi. <mark style=\"background:#fee2e2;\">Aynan "
            "bir xil so'z — ko'pincha tuzoq belgisi</mark>; to'g'ri sarlavha odatda "
            "<u>sinonimlar</u> bilan yozilgan bo'ladi.</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> ishonch komil bo'lmagan paragrafda 2 ta nomzod "
            "sarlavha qolsa, har biriga \"nega YO'Q?\" deb so'rang — chalg'ituvchining "
            "qolipini toping. Qolip topilgan sarlavha — tashlanadi. \"Nega HA?\" deb "
            "so'rasangiz, ikkalasiga ham sabab topib yuborasiz.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna paragraf — 4 tuzoqni jonli ko'ring</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"City trees do far more than decorate the streets. "
            "Their canopies intercept rainfall, easing the load on drainage systems "
            "during storms. Their roots stabilise the soil, and their shade can lower "
            "street-level temperatures by several degrees in summer — a measurable "
            "saving on air-conditioning costs. One study in Chicago even linked "
            "tree-lined streets to lower crime rates, though the mechanism remains "
            "debated.\"</p>"
            "</div>"
            "<p>Endi 4 ta nomzod sarlavhani tahlil qilamiz:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\">❌ <em>\"A study of crime in Chicago\"</em> — <strong>juda tor</strong>: faqat oxirgi jumla.</p>"
            "<p style=\"margin:0 0 6px;\">❌ <em>\"Why cities matter\"</em> — <strong>juda keng</strong>: paragraf shaharlar emas, shahar daraxtlari haqida.</p>"
            "<p style=\"margin:0 0 6px;\">❌ <em>\"How to plant trees in cities\"</em> — <strong>noto'g'ri urg'u</strong>: paragraf foydalari haqida, ekish usuli haqida emas.</p>"
            "<p style=\"margin:0;\">✅ <em>\"The practical benefits of urban trees\"</em> — butun paragrafni qamraydi (drenaj + tuproq + harorat + xavfsizlik).</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Paragraf asosan <u>plastik "
                "chiqindilarning okeanlarga yetib borish yo'llari</u> haqida. Sarlavha: "
                "<em>\"Solutions to ocean plastic pollution\"</em>. Bu qaysi turdagi "
                "chalg'ituvchi?</p>"
            ),
            "choices": [
                {"text": "Juda tor (too narrow)", "is_correct": False},
                {"text": "Noto'g'ri urg'u (wrong focus)", "is_correct": True},
                {"text": "So'z-tuzoq (word match)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: noto'g'ri "
                "urg'u.</mark> Mavzu bir xil (okean plastigi), lekin burchak boshqa: "
                "paragraf <u>qanday yetib borishi</u> (ya'ni sabab/jarayon) haqida, "
                "sarlavha esa <u>yechimlar</u> haqida. \"Solutions\" so'zining o'zi "
                "signal: paragrafda yechim taklif qilinganmi? Yo'q — demak sarlavha "
                "tashlanadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Paragrafda \"volcano\" so'zi 5 marta "
                "uchraydi, sarlavhalardan birida ham \"volcano\" bor. Bu haqida qaysi "
                "fikr TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "So'z mos kelsa, sarlavha ham to'g'ri bo'ladi — belgilash kerak", "is_correct": False},
                {"text": "Bir xil so'z hech narsani isbotlamaydi — g'oyani solishtirish kerak; aynan mos so'z ko'pincha tuzoq", "is_correct": True},
                {"text": "Bir xil so'z bo'lgan sarlavhani darhol chiqarib tashlash kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: g'oyani "
                "solishtirish kerak.</mark> So'z mosligi — na isbot, na avtomatik rad "
                "(ba'zan to'g'ri sarlavhada ham asosiy so'z bo'ladi). Lekin IELTS'ning "
                "umumiy uslubini eslang: to'g'ri javoblar odatda <u>paraphrase</u> "
                "qilinadi. Sarlavha paragraf so'zini aynan takrorlasa — bu "
                "<em>hushyorlik</em> chaqirig'i: to'xtab, g'oya mosligini alohida "
                "tekshiring.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Matn umumiy mavzusi — \"Qayta "
                "tiklanadigan energiya\". Bitta paragraf faqat <u>shamol turbinalarining "
                "texnik kamchiliklari</u> haqida. Ikki nomzod: (A) <em>\"The future of "
                "renewable energy\"</em>, (B) <em>\"Drawbacks of wind power\"</em>. "
                "Qaysi biri to'g'ri va nima uchun?</p>"
            ),
            "choices": [
                {"text": "A — chunki u matnning umumiy mavzusiga mos", "is_correct": False},
                {"text": "B — A esa \"juda keng\": u butun matnga mos, aynan shu paragrafga emas", "is_correct": True},
                {"text": "Ikkalasi ham to'g'ri bo'la oladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B.</mark> "
                "\"The future of renewable energy\" — klassik <strong>too broad</strong> "
                "tuzoq: u shu matnning <u>istalgan</u> paragrafiga yopishadi, demak hech "
                "biriga aniq javob emas. Paragraf esa aniq va tor mavzuga ega: shamol "
                "energiyasining kamchiliklari — \"Drawbacks of wind power\" buni aynan "
                "qamraydi. Qoida: sarlavha paragrafga <u>qanchalik aniq</u> mos kelsa, "
                "shunchalik yaxshi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">too narrow</div><div class=\"pp-card-back\">juda tor (bitta detalga yopishgan)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">too broad</div><div class=\"pp-card-back\">juda keng (butun matnga mos)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">wrong focus</div><div class=\"pp-card-back\">noto'g'ri urg'u (burchagi boshqa)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">process of elimination</div><div class=\"pp-card-back\">chiqarib tashlash usuli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">canopy</div><div class=\"pp-card-back\">daraxt shox-shabbasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to intercept</div><div class=\"pp-card-back\">tutib qolmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">drawback</div><div class=\"pp-card-back\">kamchilik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">measurable saving</div><div class=\"pp-card-back\">o'lchanadigan tejamkorlik</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>4 tuzoq qolipi: juda tor / juda keng / noto'g'ri urg'u / so'z-tuzoq.</li>"
            "<li>Ikki nomzod qolganda \"nega YO'Q?\" deb so'rang — tuzoq qolipini qidiring.</li>"
            "<li>Sarlavhadagi aynan mos so'z — hushyorlik signali; to'g'ri javob odatda sinonimda.</li>"
            "<li>Eng aniq (spesifik) mos sarlavha har doim keng-umumiysidan ustun.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 14 (order 32 — topic sentences & paragraph function words)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_HEADINGS,
    "title": "IELTS Reading 14: Topic Sentences and Function Words — however, in contrast, therefore",
    "summary": "Topic sentence qayerda yashirinishi va bog'lovchi so'zlar paragraf vazifasini qanday ochib berishi.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Paragrafning \"yuragi\" qayerda?</h2>"
            "<p>\"Birinchi jumlani o'qing\" — yaxshi boshlang'ich qoida, lekin IELTS "
            "darajasidagi matnlarda <strong>topic sentence</strong> (paragrafning asosiy "
            "jumlasi) har doim ham birinchi o'rinda turmaydi. Bu darsda uni qayerdan "
            "qidirishni va <mark style=\"background:#dbeafe;\">bog'lovchi so'zlar "
            "(function words)</mark> paragrafning vazifasini qanday \"aytib qo'yishini\" "
            "o'rganamiz.</p>"
        )},
        {"rich_text": (
            "<h3>Topic sentence qayerda bo'lishi mumkin?</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Ko'pincha — birinchi jumlada.</strong> "
            "<em>\"Urban farming has transformed how cities feed themselves. In Detroit, "
            "for example...\"</em> — birinchi jumla g'oya, qolgani misol.</p></div>"
            "<div class=\"pp-step\"><p><strong>Ba'zan — ikkinchi jumlada.</strong> "
            "Birinchi jumla oldingi paragrafga \"ko'prik\" bo'lsa: <em>\"Such successes, "
            "however, tell only half the story. The costs of urban farming are "
            "substantial...\"</em> — asosiy g'oya (xarajatlar) ikkinchi jumlada.</p></div>"
            "<div class=\"pp-step\"><p><strong>Ba'zan — oxirgi jumlada.</strong> "
            "Paragraf dalillar bilan boshlanib, xulosa bilan tugasa: misollar, misollar... "
            "<em>\"Taken together, these findings suggest that...\"</em> — mana g'oya, "
            "eng oxirida.</p></div>"
            "<div class=\"pp-step\"><p><strong>Qoida:</strong> birinchi jumla <u>misol, "
            "raqam yoki savol</u> bilan boshlansa — topic sentence keyinroqda. \"For "
            "example\" bilan boshlangan paragraf bo'lmaydi — demak g'oyani pastdan "
            "qidiring.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Function words — paragrafning yo'l belgilari</h3>"
            "<p>Bog'lovchi so'zlar paragraf <u>nima qilayotganini</u> (vazifasini) "
            "bildiradi — bu esa to'g'ri sarlavhaga eng qisqa yo'l:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>however, yet, in contrast, on the other hand</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>burilish/qarama-qarshilik — paragraf oldingi fikrga QARSHI yoki boshqa tomonini ko'rsatadi</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>therefore, as a result, consequently, this explains why</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>natija/xulosa — paragraf oqibat yoki yakun beradi</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>for instance, such as, one striking example</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>misol — paragraf oldingi g'oyani dalillaydi (g'oyaning o'zi oldingi paragrafda!)</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>traditionally, for centuries, it was once believed</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>tarixiy fon — paragraf o'tmishni tasvirlaydi (ko'pincha keyin \"however...\" keladi)</em></p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> sarlavhalar ro'yxatida ham xuddi shu vazifa "
            "so'zlari bo'ladi: <em>\"A change of direction\"</em>, <em>\"The consequences "
            "of...\"</em>, <em>\"An earlier approach\"</em>. Paragraf vazifasini "
            "aniqlasangiz, sarlavha vazifasi bilan juftlashtirasiz — so'zlar mos "
            "kelmasa ham!</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Paragraf shunday boshlanadi: <em>\"One "
                "striking example is the city of Freiburg, where solar panels now cover "
                "a third of all rooftops...\"</em> Bu paragrafning topic sentence'i "
                "haqida nima deyish mumkin?</p>"
            ),
            "choices": [
                {"text": "Birinchi jumla — topic sentence, sarlavhani shunga moslash kerak", "is_correct": False},
                {"text": "Bu paragraf oldingi paragrafdagi g'oyaning misoli — asosiy g'oya oldingi paragrafda aytilgan", "is_correct": True},
                {"text": "Topic sentence yo'q — bunday paragraflar sarlavhasiz qoladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: bu misol-"
                "paragraf.</mark> \"One striking example\" — misol signali: paragraf "
                "<u>oldingi</u> g'oyani dalillayapti. Bunday paragrafga sarlavha odatda "
                "misolning o'zi orqali beriladi (masalan, \"A city that leads the way\") — "
                "lekin uni to'g'ri tanlash uchun <u>nimaga misol</u> ekanini (oldingi "
                "paragrafdan) bilish kerak. Paragraflar zanjir — alohida orollar emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Paragraf: <em>\"For centuries, doctors "
                "believed that stomach ulcers were caused by stress and spicy food. "
                "Patients were told to rest and change their diet. However, in the 1980s "
                "two Australian scientists showed that most ulcers are in fact caused by "
                "a bacterium — a discovery that transformed treatment and won them the "
                "Nobel Prize.\"</em> Qaysi sarlavha to'g'ri?</p>"
            ),
            "choices": [
                {"text": "\"The dangers of spicy food\"", "is_correct": False},
                {"text": "\"An old belief overturned by science\"", "is_correct": True},
                {"text": "\"How to treat stomach ulcers\"", "is_correct": False},
                {"text": "\"Two famous Australian scientists\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"An old belief "
                "overturned by science\".</mark> Paragraf qolipi: <em>\"For "
                "centuries...\"</em> (eski qarash) + <em>\"However...\"</em> (burilish — "
                "yangi kashfiyot). Bu \"eski ishonch ag'darildi\" qolipi — sarlavha aynan "
                "shu <u>vazifani</u> aytadi. Qolganlari: \"spicy food\" — detal-tuzoq, "
                "\"how to treat\" — noto'g'ri urg'u (paragraf davolash qo'llanmasi emas), "
                "\"two scientists\" — juda tor (ular faqat oxirida).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Sarlavhalar ro'yxatida: <em>\"(i) A "
                "surprising turnaround\"</em> va <em>\"(ii) A long-held assumption\"</em>. "
                "Matnda B paragrafi \"Traditionally, farmers assumed that...\" bilan "
                "boshlanib, faqat o'sha eski qarashni tasvirlaydi; C paragrafi esa "
                "\"Recent field trials, however, point the other way...\" bilan "
                "boshlanadi. Qaysi juftlash to'g'ri?</p>"
            ),
            "choices": [
                {"text": "B → (i), C → (ii)", "is_correct": False},
                {"text": "B → (ii), C → (i)", "is_correct": True},
                {"text": "Ikkala sarlavha ham B ga mos", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B → (ii), "
                "C → (i).</mark> Vazifa so'zlarini juftlashtiring: B'dagi "
                "\"Traditionally ... assumed\" = \"A long-held assumption\" (uzoq yillik "
                "taxmin). C'dagi \"however, point the other way\" = \"A surprising "
                "turnaround\" (kutilmagan burilish). E'tibor bering: bironta so'z aynan "
                "takrorlanmadi — juftlik <u>vazifa</u> darajasida topildi. Bu — Matching "
                "Headings'ning yuqori darajadagi o'yini.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">topic sentence</div><div class=\"pp-card-back\">paragrafning asosiy jumlasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">function word</div><div class=\"pp-card-back\">vazifa/bog'lovchi so'z</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">turnaround</div><div class=\"pp-card-back\">keskin burilish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">long-held assumption</div><div class=\"pp-card-back\">uzoq yillik taxmin</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to overturn</div><div class=\"pp-card-back\">ag'darmoq, bekor qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">consequently</div><div class=\"pp-card-back\">natijada</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in contrast</div><div class=\"pp-card-back\">bundan farqli o'laroq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">bacterium</div><div class=\"pp-card-back\">bakteriya</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Topic sentence har doim birinchi jumla emas — 2-jumlada yoki oxirida bo'lishi mumkin.</li>"
            "<li>\"For example\" bilan boshlangan paragraf — oldingi g'oyaning davomi; zanjirni ko'ring.</li>"
            "<li>however/therefore/traditionally — paragraf VAZIFASINING belgilari.</li>"
            "<li>Sarlavhani so'z bilan emas, vazifa bilan juftlashtiring: \"however...\" ↔ \"A turnaround\".</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 15 (order 33 — Matching Headings full passage practice)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_HEADINGS,
    "title": "IELTS Reading 15: Matching Headings — Full Passage Practice (Mixed Review)",
    "summary": "To'liq 5 paragrafli matn va 8 sarlavha bilan haqiqiy Matching Headings amaliyoti.",
    "order": 33,
    "blocks": [
        {"rich_text": (
            "<h2>Haqiqiy format: 5 paragraf, 8 sarlavha</h2>"
            "<p>Endi hammasi imtihondagidek: A–E paragrafli matn va i–viii sarlavhalar "
            "ro'yxati. Har sarlavha ko'pi bilan bir marta ishlatiladi — 3 tasi ortib "
            "qoladi (tuzoqlar!). Usulni eslang: har paragrafning 1- va oxirgi jumlasi → "
            "o'z so'zingiz bilan gist → ro'yxatdan qidirish → shubhada \"nega YO'Q?\" "
            "testi.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> avval sarlavhalar ro'yxatini o'qing (30 soniya), "
            "keyin paragraflarga o'ting — shunda nimani qidirayotganingizni bilasiz. "
            "Haqiqiy imtihonda har paragrafga ~1,5 daqiqa mo'ljallang.</div>"
        )},
        {"rich_text": (
            "<h3>Sarlavhalar ro'yxati (List of Headings)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\"><strong>i</strong> — Why the pyramids were built</p>"
            "<p style=\"margin:0 0 4px;\"><strong>ii</strong> — A theory that divided experts</p>"
            "<p style=\"margin:0 0 4px;\"><strong>iii</strong> — The workforce behind the monuments</p>"
            "<p style=\"margin:0 0 4px;\"><strong>iv</strong> — Moving mountains without machines</p>"
            "<p style=\"margin:0 0 4px;\"><strong>v</strong> — The pyramids in modern culture</p>"
            "<p style=\"margin:0 0 4px;\"><strong>vi</strong> — What lies inside a pyramid</p>"
            "<p style=\"margin:0 0 4px;\"><strong>vii</strong> — An enduring architectural puzzle</p>"
            "<p style=\"margin:0;\"><strong>viii</strong> — Slaves or citizens? An old image corrected</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Pyramid Builders</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\"><strong>A.</strong> \"How the ancient "
            "Egyptians raised two-million-plus blocks of stone, some weighing as much as "
            "a lorry, into a structure nearly 150 metres tall remains one of "
            "archaeology's most stubborn questions. Despite two centuries of serious "
            "study, no complete answer has been agreed upon, and each new excavation "
            "seems to raise as many questions as it settles.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>B.</strong> \"For generations, "
            "popular films and school books painted the builders as slaves toiling under "
            "the whip. Archaeology has quietly demolished this picture. Excavations of "
            "the builders' settlement at Giza uncovered bakeries, breweries and medical "
            "care, and workers were buried honourably close to the king's own monument — "
            "privileges no slave would have received. Most scholars now see the builders "
            "as paid labourers and farmers doing seasonal service for the state.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>C.</strong> \"That service demanded "
            "organisation on an industrial scale. Written records recovered from the "
            "harbour at Wadi al-Jarf describe teams of about forty men, each with its "
            "own name, quotas and rations, ferrying limestone across the Nile. Supplying "
            "tens of thousands of workers with bread, beer and fish every day was, in "
            "effect, the world's first mass logistics operation.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>D.</strong> \"The stones themselves "
            "travelled by simpler means than legend suggests. Wall paintings show gangs "
            "hauling statues on wooden sledges while a worker pours water onto the sand "
            "ahead — a trick that, as physicists confirmed in 2014, roughly halves the "
            "friction. Ramps of rubble and mudbrick, traces of which survive at several "
            "sites, carried the blocks upwards as the pyramid grew.</p>"
            "<p style=\"margin:0;\"><strong>E.</strong> \"More contested is the question "
            "of what the ramps looked like in their final form. Straight ramps would "
            "have needed to be impossibly long to reach the summit; spiral ramps would "
            "have hidden the pyramid's edges, which builders needed to see to keep the "
            "shape true. A French architect's proposal of an internal ramp, winding "
            "unseen inside the structure itself, won enthusiastic supporters and fierce "
            "critics in equal measure — and the debate shows no sign of ending.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> <strong>A paragrafi</strong> uchun to'g'ri "
                "sarlavhani tanlang.</p>"
            ),
            "choices": [
                {"text": "i — Why the pyramids were built", "is_correct": False},
                {"text": "vii — An enduring architectural puzzle", "is_correct": True},
                {"text": "vi — What lies inside a pyramid", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: vii.</mark> "
                "A paragrafi gist'i: \"qanday qurilgani <u>hali ham</u> to'liq "
                "yechilmagan savol\". \"remains one of archaeology's most stubborn "
                "questions\", \"no complete answer\" ↔ \"An <u>enduring</u> ... "
                "<u>puzzle</u>\" — sinonim juftlik. (i) — noto'g'ri urg'u: paragraf "
                "<em>nega</em> emas, <em>qanday</em> qurilgani haqida; (vi) — matnda "
                "umuman yo'q mavzu.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <strong>B paragrafi</strong> uchun to'g'ri "
                "sarlavhani tanlang.</p>"
            ),
            "choices": [
                {"text": "viii — Slaves or citizens? An old image corrected", "is_correct": True},
                {"text": "iii — The workforce behind the monuments", "is_correct": False},
                {"text": "v — The pyramids in modern culture", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: viii.</mark> "
                "B paragrafi qolipi — o'tgan darsdagi \"eski ishonch ag'darildi\": "
                "\"For generations ... painted the builders as slaves\" (eski qarash) → "
                "\"Archaeology has quietly demolished this picture\" (burilish!). "
                "\"An old image <u>corrected</u>\" aynan shu vazifani aytadi. (iii) — "
                "yaqin, lekin <u>juda keng</u>: ishchilar haqida umumiy; B'ning mag'zi "
                "esa aynan \"qul emas ekan\" tuzatishida. (v) — kino/kitob tilga olinadi, "
                "lekin bu detal, mavzu emas (so'z-tuzoq).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> <strong>C paragrafi</strong> uchun to'g'ri "
                "sarlavhani tanlang.</p>"
            ),
            "choices": [
                {"text": "iv — Moving mountains without machines", "is_correct": False},
                {"text": "iii — The workforce behind the monuments", "is_correct": True},
                {"text": "ii — A theory that divided experts", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: iii.</mark> "
                "C gist'i: ishchilar qanday <u>tashkil etilgani</u> — jamoalar, normalar, "
                "oziq-ovqat ta'minoti (\"the world's first mass logistics operation\"). "
                "Bu — \"The <u>workforce</u> behind the monuments\". (iv) tosh "
                "<em>tashish</em> haqida — u D paragrafiniki; (ii) esa bahsli nazariya "
                "haqida — u E'niki. Ko'ryapsizmi: har sarlavha o'z paragrafini kutyapti — "
                "shoshilsangiz, qo'shni paragraf sarlavhasini olib qo'yasiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> <strong>D paragrafi</strong> uchun to'g'ri "
                "sarlavhani tanlang.</p>"
            ),
            "choices": [
                {"text": "iv — Moving mountains without machines", "is_correct": True},
                {"text": "vii — An enduring architectural puzzle", "is_correct": False},
                {"text": "i — Why the pyramids were built", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: iv.</mark> "
                "D gist'i: toshlar <u>qanday ko'chirilgani</u> — chana + suv hiylasi + "
                "rampalar; hammasi mashinasiz. \"Moving mountains without machines\" — "
                "metaforik, lekin butun paragrafni qamraydi. (vii) A'da ishlatilgan "
                "(har sarlavha bir marta!), (i) esa matnning hech yerida yo'q — "
                "\"nega qurilgan\" savoli umuman ochilmagan: ortiqcha-tuzoq sarlavha.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <strong>E paragrafi</strong> uchun to'g'ri "
                "sarlavhani tanlang.</p>"
            ),
            "choices": [
                {"text": "vi — What lies inside a pyramid", "is_correct": False},
                {"text": "ii — A theory that divided experts", "is_correct": True},
                {"text": "viii — Slaves or citizens? An old image corrected", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ii.</mark> "
                "E gist'i: rampalar shakli — bahsli savol; ichki rampa nazariyasi "
                "\"won enthusiastic supporters <u>and</u> fierce critics\" — ya'ni "
                "ekspertlarni <u>ikkiga bo'ldi</u> = \"A theory that <u>divided</u> "
                "experts\". (vi) — so'z-tuzoq: \"internal/inside\" so'zi bor, lekin "
                "paragraf piramida ichidagi xonalar haqida emas, <em>qurilish "
                "nazariyasi</em> haqida. Vazifa so'zlariga qarang: \"More contested "
                "is...\" — bahs signali birinchi jumlaning o'zida edi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — ajoyib! Matching Headings sizga bo'ysundi; keyingi mavzu — Matching Information.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>4/5</strong> — kuchli natija; xato paragrafingizning izohini o'qib, qaysi tuzoqqa tushganingizni aniqlang.</p>"
            "<p style=\"margin:0;\"><strong>3/5 yoki kam</strong> — 12–14-darslarni takrorlang: gist usuli, 4 tuzoq qolipi, vazifa so'zlari.</p>"
            "</div>"
            "<p>Ishlatilmagan sarlavhalarga e'tibor bering: (i) matnda ochilmagan mavzu, "
            "(v) va (vi) — detal/so'z-tuzoqlar. Haqiqiy imtihonda ham ortiqcha "
            "sarlavhalar aynan shu 3 qolipdan bo'ladi.</p>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">stubborn question</div><div class=\"pp-card-back\">yechilmas savol</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">excavation</div><div class=\"pp-card-back\">arxeologik qazish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to demolish (an idea)</div><div class=\"pp-card-back\">(g'oyani) yakson qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">paid labourer</div><div class=\"pp-card-back\">yollanma ishchi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">quota</div><div class=\"pp-card-back\">norma, belgilangan miqdor</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to haul</div><div class=\"pp-card-back\">sudrab tortmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">friction</div><div class=\"pp-card-back\">ishqalanish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">contested</div><div class=\"pp-card-back\">bahsli, tortishuvli</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ish tartibi: sarlavhalarni o'qish → paragraf gist'i → juftlash → \"nega YO'Q?\" testi.</li>"
            "<li>Qo'shni paragraflar sarlavhalari adashtiradi — har sarlavha \"o'z\" paragrafini kutadi.</li>"
            "<li>Ortiqcha sarlavhalar 3 qolipda: ochilmagan mavzu, detal, so'z-tuzoq.</li>"
            "<li>Vazifa so'zlari (More contested is..., however...) — eng tez yo'l.</li>"
            "</ul>"
        )},
    ],
},

]
