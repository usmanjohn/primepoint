"""
IELTS Writing lessons 16-18 (orders 70-72) — the "Lug'at va bog'lovchilar (Vocabulary &
Cohesion for Band 7+)" topic — seventh Writing batch, see toc_ielts_writing.txt.
(Academic-only scope.)

No audio, no charts. Kit: step-reveal + flashcards (vocab banks) + dropdowns + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_VOCAB = {
    "title":   "Lug'at va bog'lovchilar (Vocabulary & Cohesion for Band 7+)",
    "summary": "Band 7+ uchun: takrorlanmaydigan bog'lovchilar, mavzuviy lug'at banki va "
               "savolni ko'chirmasdan paraphrase qilish.",
    "icon":    "bi-translate",
    "order":   8,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 16 (order 70 — linking words)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_VOCAB,
    "title": "IELTS Writing 16: Linking Words That Don't Sound Repetitive",
    "summary": "Bog'lovchilarni funksiyasi bo'yicha kengaytirish (qo'shish/qarshilik/natija/misol) va referencing (this, such) orqali tabiiy izchillik.",
    "order": 70,
    "blocks": [
        {"rich_text": (
            "<h2>Bog'lovchilar — ko'p emas, TO'G'RI</h2>"
            "<p>Ko'p nomzod \"Firstly, Secondly, Moreover, In conclusion\"ni "
            "takrorlab, matnni mexanik qiladi. Ajablanarlisi — bog'lovchilarni "
            "<u>haddan tashqari</u> yoki noto'g'ri ishlatish Coherence & Cohesion bandini "
            "aslida <mark style=\"background:#fee2e2;\">pasaytiradi</mark>. Band 7+ "
            "bog'liqlikni <u>tabiiy</u> va xilma-xil quradi.</p>"
        )},
        {"rich_text": (
            "<h3>Bog'lovchilar — funksiyasi bo'yicha</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Funksiya bo'yicha to'plam — bosing</summary>"
            "<div style=\"margin-top:10px;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Qo'shish:</strong> In addition, Furthermore, Moreover, What is more, Not only ... but also</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Qarshilik:</strong> However, Nevertheless, Even so, Despite this, On the contrary, Whereas</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Natija:</strong> As a result, Consequently, Therefore, Thus, For this reason</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Misol:</strong> For instance, To illustrate, A case in point is ...</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Yon berish (concession):</strong> Although, While, Admittedly, Granted that</p>"
            "<p style=\"margin:0;\"><strong>Ta'kid:</strong> Indeed, In fact, Notably</p>"
            "</div>"
            "</details>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — funksiyaga MOS bo'lsin:</strong> \"Moreover\" (qo'shish) "
            "ni qarshilik kerak bo'lgan joyda ishlatish — xato. Har bog'lovchi aniq "
            "funksiyaga ega; noto'g'ri tanlov o'quvchini chalg'itadi.</div>"
        )},
        {"rich_text": (
            "<h3>Bog'lovchidan tashqari: referencing</h3>"
            "<p>Izchillik faqat \"however/therefore\" degani emas. Band 7+ g'oyalarni "
            "<strong>referencing</strong> (ishora so'zlari) bilan ham bog'laydi — bu "
            "tabiiyroq eshitiladi:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>this / these / such:</strong> <em>\"Cars cause pollution. <u>This problem</u> is worsening.\"</em></p>"
            "<p style=\"margin:0 0 6px;\"><strong>olmoshlar:</strong> <em>\"Students gain skills, and <u>they</u> also build networks.\"</em></p>"
            "<p style=\"margin:0;\"><strong>the former / the latter:</strong> ikki narsadan birinchisi / ikkinchisi.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> har jumlani bog'lovchi bilan boshlamang. "
            "2–3 jumlaga bitta aniq bog'lovchi + referencing — bu tabiiy oqim beradi. "
            "\"Firstly... Secondly... Moreover... Furthermore...\" ketma-ket — mexanik.</div>"
        )},
        {"rich_text": (
            "<h3>Solishtiring — mexanik vs tabiiy</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Yaxshilangan variantni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>❌ Mexanik:</strong> <em>\"Firstly, cars "
            "cause pollution. Moreover, pollution is bad. Moreover, it harms health. "
            "Furthermore, this is a problem.\"</em> — \"Moreover\" takrori + noaniq.</p></div>"
            "<div class=\"pp-step\"><p><strong>✅ Tabiiy:</strong> <em>\"Cars are a major "
            "source of air pollution. This pollution not only damages the environment "
            "but also poses a serious threat to public health, and for this reason it "
            "has become a pressing concern.\"</em> — referencing (This) + xilma-xil "
            "bog'lovchi (not only... but also, for this reason).</p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Har jumlani \"Firstly / Moreover / "
                "Furthermore\" bilan boshlash Coherence'ga qanday ta'sir qiladi?</p>"
            ),
            "choices": [
                {"text": "Oshiradi — ko'proq bog'lovchi doim yaxshi", "is_correct": False},
                {"text": "Pasaytiradi — haddan ortiq/mexanik bog'lovchi tabiiy oqimni buzadi", "is_correct": True},
                {"text": "Hech qanday ta'sir qilmaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: pasaytiradi.</mark> "
                "Band descriptorlarida \"mechanical\" yoki \"overuse of cohesive devices\" "
                "— bu kamchilik. Band 7+ bog'lovchilarni <u>tabiiy va xilma-xil</u> "
                "ishlatadi, referencing bilan aralashtiradi. Har jumla bosh bog'lovchi — "
                "mexanik taassurot.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"Public transport is cheap. ______, it "
                "is often unreliable.\" Bo'sh joyga qaysi bog'lovchi MOS (qarshilik "
                "kerak)?</p>"
            ),
            "choices": [
                {"text": "Moreover", "is_correct": False},
                {"text": "However", "is_correct": True},
                {"text": "As a result", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: However.</mark> "
                "Ikki gap qarama-qarshi (arzon LEKIN ishonchsiz) → qarshilik bog'lovchisi "
                "\"However\". \"Moreover\" (qo'shish) va \"As a result\" (natija) — "
                "funksiyaga mos emas. Bog'lovchini MA'NOga qarab tanlang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> \"Cars cause pollution. This ______ is "
                "worsening.\" Referencing qanday ishlaydi?</p>"
            ),
            "choices": [
                {"text": "\"This problem\" — oldingi g'oyaga ishora qilib, ikki jumlani bog'laydi", "is_correct": True},
                {"text": "\"This\" ortiqcha — olib tashlash kerak", "is_correct": False},
                {"text": "Referencing faqat rasmiy xatlarda ishlatiladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"This problem\" "
                "bog'laydi.</mark> \"This/these + ot\" oldingi g'oyani qisqa "
                "umumlashtiradi va yangi jumlaga ulaydi — bog'lovchisiz izchillik. Bu "
                "band 7+ ning tabiiy cohesion usuli; har doim \"However/Moreover\" shart "
                "emas.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Linking devices</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Nevertheless</div><div class=\"pp-card-back\">shunga qaramay (qarshilik)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Consequently</div><div class=\"pp-card-back\">natijada</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Not only ... but also ...</div><div class=\"pp-card-back\">nafaqat ... balki ... ham</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">A case in point is ...</div><div class=\"pp-card-back\">Buning yaqqol misoli ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Admittedly, ...</div><div class=\"pp-card-back\">Tan olish kerakki, ... (yon berish)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the former / the latter</div><div class=\"pp-card-back\">birinchisi / ikkinchisi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">for this reason</div><div class=\"pp-card-back\">shu sababli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">referencing (this/such)</div><div class=\"pp-card-back\">ishora so'zlari orqali bog'lash</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Bog'lovchilarni funksiyasi bo'yicha o'rganing (qo'shish/qarshilik/natija/misol).</li>"
            "<li>Ma'noga MOS tanlang: \"Moreover\" ≠ \"However\".</li>"
            "<li>Referencing (this, these, such, olmoshlar) — bog'lovchisiz izchillik.</li>"
            "<li>Har jumlani bog'lovchi bilan boshlamang — bu mexanik va bandni pasaytiradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 17 (order 71 — topic vocabulary bank)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_VOCAB,
    "title": "IELTS Writing 17: Topic Vocabulary Bank — Education, Environment, Technology, Health",
    "summary": "Task 2 mavzulari uchun aniq lug'at (kollokatsiya) banki: ta'lim, atrof-muhit, texnologiya, sog'liq — Lexical Resource'ni ko'taradi.",
    "order": 71,
    "blocks": [
        {"rich_text": (
            "<h2>Mavzuviy lug'at — Lexical Resource kaliti</h2>"
            "<p>Task 2 savollari bir necha mavzu atrofida aylanadi: ta'lim, atrof-muhit, "
            "texnologiya, sog'liq, jinoyat, ish. Har mavzu uchun <strong>aniq "
            "kollokatsiyalar</strong>ni bilsangiz, umumiy so'zlar (\"good, bad, thing\") "
            "o'rniga aniq til ishlatasiz — bu Lexical Resource'ni to'g'ridan-to'g'ri "
            "ko'taradi.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> lug'atni <u>tabiiy</u> ishlating — zo'rlab "
            "tiqishtirmang. Noto'g'ri kollokatsiya (\"make a pollution\") to'g'ri oddiy "
            "so'zdan yomonroq. Aniqlik muhim.</div>"
        )},
        {"rich_text": (
            "<h3>Ta'lim (Education)</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Kollokatsiyalar — bosing</summary>"
            "<div class=\"pp-flashcards\" data-pp-flashcards style=\"margin-top:10px;\">"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">compulsory education</div><div class=\"pp-card-back\">majburiy ta'lim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">tuition fees</div><div class=\"pp-card-back\">o'qish to'lovi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">academic performance</div><div class=\"pp-card-back\">o'quv ko'rsatkichi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">vocational training</div><div class=\"pp-card-back\">kasb-hunar ta'limi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">rote learning</div><div class=\"pp-card-back\">yodlab o'rganish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a well-rounded education</div><div class=\"pp-card-back\">har tomonlama ta'lim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the curriculum</div><div class=\"pp-card-back\">o'quv dasturi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">critical thinking</div><div class=\"pp-card-back\">tanqidiy fikrlash</div></div>"
            "</div></details>"
            "<h3>Atrof-muhit (Environment)</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Kollokatsiyalar — bosing</summary>"
            "<div class=\"pp-flashcards\" data-pp-flashcards style=\"margin-top:10px;\">"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">carbon emissions</div><div class=\"pp-card-back\">uglerod chiqindilari</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">renewable energy</div><div class=\"pp-card-back\">qayta tiklanadigan energiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">deforestation</div><div class=\"pp-card-back\">o'rmonlarning kesilishi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">sustainable</div><div class=\"pp-card-back\">barqaror (atrof-muhitga zararsiz)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">greenhouse gases</div><div class=\"pp-card-back\">issiqxona gazlari</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">conservation</div><div class=\"pp-card-back\">tabiatni muhofaza qilish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">biodiversity</div><div class=\"pp-card-back\">biologik xilma-xillik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an ecological footprint</div><div class=\"pp-card-back\">ekologik iz</div></div>"
            "</div></details>"
        )},
        {"rich_text": (
            "<h3>Texnologiya (Technology)</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Kollokatsiyalar — bosing</summary>"
            "<div class=\"pp-flashcards\" data-pp-flashcards style=\"margin-top:10px;\">"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">digital literacy</div><div class=\"pp-card-back\">raqamli savodxonlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">automation</div><div class=\"pp-card-back\">avtomatlashtirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">artificial intelligence</div><div class=\"pp-card-back\">sun'iy intellekt</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">screen time</div><div class=\"pp-card-back\">ekran oldida o'tirish vaqti</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the digital divide</div><div class=\"pp-card-back\">raqamli tafovut</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">innovation</div><div class=\"pp-card-back\">innovatsiya, yangilik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to streamline a process</div><div class=\"pp-card-back\">jarayonni soddalashtirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">cybersecurity</div><div class=\"pp-card-back\">kiberxavfsizlik</div></div>"
            "</div></details>"
            "<h3>Sog'liq (Health)</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Kollokatsiyalar — bosing</summary>"
            "<div class=\"pp-flashcards\" data-pp-flashcards style=\"margin-top:10px;\">"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a sedentary lifestyle</div><div class=\"pp-card-back\">harakatsiz turmush tarzi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">obesity</div><div class=\"pp-card-back\">semizlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">mental health</div><div class=\"pp-card-back\">ruhiy salomatlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">preventive care</div><div class=\"pp-card-back\">profilaktik tibbiyot</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">life expectancy</div><div class=\"pp-card-back\">o'rtacha umr ko'rish davri</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">well-being</div><div class=\"pp-card-back\">farovonlik, sog'lomlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a chronic disease</div><div class=\"pp-card-back\">surunkali kasallik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">public health</div><div class=\"pp-card-back\">jamoat sog'lig'i</div></div>"
            "</div></details>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Qaysi kollokatsiya TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "\"Factories make a pollution.\"", "is_correct": False},
                {"text": "\"Factories produce carbon emissions.\"", "is_correct": True},
                {"text": "\"Factories do pollution things.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"produce carbon "
                "emissions\".</mark> Aniq kollokatsiya (produce + emissions). \"make a "
                "pollution\" — grammatik xato (pollution sanoqsiz, \"a\" olmaydi) + noto'g'ri "
                "fe'l; \"do pollution things\" — juda oddiy. To'g'ri kollokatsiya Lexical "
                "Resource'ni ko'taradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"Students who only memorise facts "
                "without understanding\" — bu qaysi atama?</p>"
            ),
            "choices": [
                {"text": "critical thinking", "is_correct": False},
                {"text": "rote learning", "is_correct": True},
                {"text": "vocational training", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: rote learning.</mark> "
                "\"Rote learning\" = tushunmasdan yodlab o'rganish — aynan shu ma'no. "
                "\"Critical thinking\" (tanqidiy fikrlash) — teskarisi; \"vocational "
                "training\" — kasb-hunar ta'limi. To'g'ri atama fikringizni aniq "
                "ifodalaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Mavzuviy lug'atni qanday ishlatish "
                "kerak?</p>"
            ),
            "choices": [
                {"text": "Har esseda iloji boricha ko'proq murakkab so'zni tiqishtirish", "is_correct": False},
                {"text": "Tabiiy va TO'G'RI ishlatish — noto'g'ri kollokatsiya oddiy so'zdan yomonroq", "is_correct": True},
                {"text": "Faqat kirishda ishlatish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: tabiiy va "
                "to'g'ri.</mark> Lexical Resource nafaqat \"keng\", balki \"aniq\" "
                "lug'atni ham baholaydi. Zo'rlab tiqishtirilgan yoki noto'g'ri "
                "kollokatsiya bandni pasaytiradi. Bilgan so'zingizni o'rinli joyda "
                "ishlating.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Task 2 mavzulari (ta'lim, atrof-muhit, texnologiya, sog'liq) uchun aniq kollokatsiyalarni yodlang.</li>"
            "<li>Aniq lug'at (\"carbon emissions\") umumiy so'zdan (\"bad air\") kuchliroq.</li>"
            "<li>Tabiiy ishlating — noto'g'ri kollokatsiya to'g'ri oddiy so'zdan yomonroq.</li>"
            "<li>Yuqoridagi dropdownlardagi kartalarni takrorlab yodda saqlang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 18 (order 72 — paraphrasing the question)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_VOCAB,
    "title": "IELTS Writing 18: Paraphrasing the Question in Your Introduction",
    "summary": "Savolni ko'chirmasdan qayta yozish: sinonim, so'z turkumini o'zgartirish, nisbat (passive/active) va tuzilmani o'zgartirish; ma'noni buzmang.",
    "order": 72,
    "blocks": [
        {"rich_text": (
            "<h2>Nega paraphrase qilish kerak?</h2>"
            "<p>Kirishda savolni <u>aynan ko'chirsangiz</u>, o'sha so'zlar so'z sanog'iga "
            "kirmaydi va lug'at boyligingizni umuman ko'rsatmaydi. Savolni "
            "<strong>paraphrase</strong> qilish — o'z so'zingiz bilan qayta yozish — "
            "<mark style=\"background:#dbeafe;\">Lexical Resource</mark> va Grammatical "
            "Range'ni birinchi jumladanoq namoyish qiladi.</p>"
        )},
        {"rich_text": (
            "<h3>4 ta paraphrase usuli</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi usulni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Sinonim.</strong> So'zni ma'nodoshiga "
            "almashtiring: <em>children → youngsters, important → crucial, think → "
            "believe.</em></p></div>"
            "<div class=\"pp-step\"><p><strong>2. So'z turkumini o'zgartirish.</strong> "
            "Fe'l → ot yoki sifat: <em>\"pollute the air\" → \"air pollution\", "
            "\"succeed\" → \"success\".</em></p></div>"
            "<div class=\"pp-step\"><p><strong>3. Nisbat (voice).</strong> Active ↔ "
            "passive: <em>\"Governments should fund schools\" → \"Schools should be "
            "funded by governments\".</em></p></div>"
            "<div class=\"pp-step\"><p><strong>4. Gap tuzilmasini o'zgartirish.</strong> "
            "Tartib yoki bog'lovchini o'zgartiring: <em>\"Because X, Y\" → \"Y, as a "
            "result of X\".</em></p></div>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Ikki xato:</strong> (1) sinonimi yo'q atamalarni o'zgartirishga "
            "urinmang (\"IELTS\", \"university\", \"the internet\" — o'sha holicha "
            "qoldiring); (2) haddan ortiq paraphrase qilib <u>ma'noni buzmang</u> — "
            "noto'g'ri sinonim (masalan \"cheap\" → \"low-quality\") ma'noni "
            "o'zgartiradi.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — savol → paraphrase</h3>"
            "<p><strong>Savol:</strong> <em>\"Many people believe that children today "
            "spend too much time watching television.\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Tahlilni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Paraphrase:</strong> <em>\"It is widely "
            "argued that youngsters nowadays devote excessive hours to watching "
            "TV.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Nima o'zgardi:</strong><br>"
            "• \"Many people believe\" → \"It is widely argued\" (nisbat + sinonim)<br>"
            "• \"children\" → \"youngsters\" (sinonim)<br>"
            "• \"today\" → \"nowadays\" (sinonim)<br>"
            "• \"spend too much time\" → \"devote excessive hours\" (sinonim + turkum)<br>"
            "• \"television\" → \"TV\" (o'zgarmas atama, qisqartma)</p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Kirishda savolni aynan ko'chirsangiz "
                "nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Yaxshi — savol so'zlari to'g'ri ishlatilgan", "is_correct": False},
                {"text": "Ko'chirilgan so'zlar hisobga olinmaydi va lug'at boyligingizni ko'rsatmaydi", "is_correct": True},
                {"text": "Grammatika ballini oshiradi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: hisobga "
                "olinmaydi.</mark> Baholovchilar savoldan aynan ko'chirilgan so'zlarni "
                "e'tiborga olmaydi — ular sizning Lexical Resource'ingizni ko'rsatmaydi. "
                "Paraphrase esa birinchi jumladanoq lug'at va grammatika mahoratini "
                "namoyish qiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"pollute the air\" iborasini so'z "
                "turkumini o'zgartirib paraphrase qiling:</p>"
            ),
            "choices": [
                {"text": "\"air pollution\"", "is_correct": True},
                {"text": "\"make air dirty\"", "is_correct": False},
                {"text": "\"the air is pollute\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"air "
                "pollution\".</mark> Fe'l (pollute) → ot ibora (air pollution) — so'z "
                "turkumini o'zgartirish. \"make air dirty\" — juda oddiy (band past); "
                "\"the air is pollute\" — grammatik xato (pollute fe'l, sifat emas).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Savolda \"university\" so'zi bor. Uni "
                "paraphrase'da qanday qilish kerak?</p>"
            ),
            "choices": [
                {"text": "\"higher education institution\" yoki o'sha holicha qoldirish — majburan almashtirmaslik", "is_correct": True},
                {"text": "\"big school\" deb almashtirish", "is_correct": False},
                {"text": "Har doim boshqa so'z topish shart", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: o'sha holicha yoki "
                "tabiiy muqobil.</mark> Ba'zi atamalarning aniq sinonimi yo'q — ularni "
                "majburan buzmang. \"university\" ni \"higher education\" deb yoki o'sha "
                "holicha qoldiring; \"big school\" — noto'g'ri (ma'no o'zgaradi). Har so'zni "
                "emas, umumiy jumlani paraphrase qiling.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Paraphrase toolkit</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Many people believe → It is widely argued</div><div class=\"pp-card-back\">nisbat + sinonim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">children → youngsters / the young</div><div class=\"pp-card-back\">sinonim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">important → crucial / vital</div><div class=\"pp-card-back\">sinonim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">nowadays / in recent years</div><div class=\"pp-card-back\">\"today\" o'rniga</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">spend too much time → devote excessive hours</div><div class=\"pp-card-back\">sinonim + turkum</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a growing number of ...</div><div class=\"pp-card-back\">\"more and more\" o'rniga</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">word class (verb→noun)</div><div class=\"pp-card-back\">so'z turkumini o'zgartirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to distort the meaning</div><div class=\"pp-card-back\">ma'noni buzmoq (paraphrase xatosi)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Kirishda savolni PARAPHRASE qiling — aynan ko'chirish hisobga olinmaydi.</li>"
            "<li>4 usul: sinonim, so'z turkumi, nisbat (voice), gap tuzilmasi.</li>"
            "<li>Sinonimi yo'q atamalarni (university, IELTS) majburan almashtirmang.</li>"
            "<li>Ma'noni buzmang — noto'g'ri sinonim to'g'ri asl so'zdan yomonroq.</li>"
            "</ul>"
        )},
    ],
},

]
