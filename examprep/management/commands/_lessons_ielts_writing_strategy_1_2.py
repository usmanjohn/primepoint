"""
IELTS Writing lessons 1-2 (orders 1-2) — the "Strategiya va baholash (Overview &
Scoring)" topic — FIRST Writing batch, see toc_ielts_writing.txt.

Writing lessons have NO audio. Per STYLE_GUIDE_IELTS.md §5b the writing kit is
step-reveal (unfold a model answer / criteria) + flashcards (linking words,
collocations) + inline MCQ. Import:
    python manage.py import_examprep \
        examprep/management/commands/_lessons_ielts_writing_strategy_1_2.py --author=<user>
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_STRATEGY = {
    "title":   "Strategiya va baholash (Overview & Scoring)",
    "summary": "IELTS Writing qanday baholanadi (4 mezon) va vaqt/so'z byudjetini "
               "qanday taqsimlash — Task 1 va Task 2 asoslari.",
    "icon":    "bi-compass",
    "order":   1,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 1 (order 1 — the four marking criteria)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Writing 1: How It's Scored — The Four Criteria Explained",
    "summary": "IELTS Writing 4 teng mezonga bo'linadi: Task Achievement/Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>Ballingiz qayerdan keladi?</h2>"
            "<p>Ko'p nomzod \"yaxshi yozsam bo'ldi\" deb o'ylaydi — lekin \"yaxshi\" "
            "aniq nimani anglatishini bilmaydi. IELTS Writing <strong>to'rtta teng "
            "vaznli mezon</strong> bo'yicha baholanadi, har biri 0–9 ball. Yakuniy "
            "bandingiz — shu to'rttasining o'rtachasi. Qaysi mezon nima ekanini bilsangiz, "
            "ballingizni <mark style=\"background:#dcfce7;\">ataylab</mark> "
            "ko'tarasiz.</p>"
        )},
        {"rich_text": (
            "<h3>To'rt mezon — birma-bir</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Task Achievement (Task 1) / Task "
            "Response (Task 2).</strong> Savolga <u>to'liq</u> javob berdingizmi? "
            "Task 1'da barcha asosiy ma'lumotni (overview + kalit raqamlar) qamradingizmi? "
            "Task 2'da savolning <u>hamma qismiga</u> javob berib, o'z pozitsiyangizni "
            "aniq bildirdingizmi? So'z chegarasiga (150/250) yetdingizmi?</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Coherence & Cohesion (izchillik va "
            "bog'liqlik).</strong> Matningiz mantiqiy tartibda, <u>paragraflarga</u> "
            "bo'linganmi? G'oyalar bog'lovchi so'zlar (however, as a result) bilan silliq "
            "ulanganmi? O'quvchi adashmasdan kuzata oladimi?</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Lexical Resource (lug'at boyligi).</strong> "
            "Lug'atingiz <u>keng va aniq</u>mi? Bir xil so'zni takrorlamay, sinonim va "
            "kollokatsiya (a sharp rise, to tackle a problem) ishlatasizmi? Imlo "
            "to'g'rimi?</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Grammatical Range & Accuracy "
            "(grammatika).</strong> <u>Turli</u> grammatik tuzilmalar (ergash gaplar, "
            "passive, shart gaplar) ishlatasizmi va ular <u>to'g'ri</u>mi? Tinish "
            "belgilari joyidami?</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — 4 mezon = 4 ish:</strong> band ko'tarish uchun "
            "to'rttasiga ham alohida e'tibor bering. Faqat murakkab so'z ishlatib, "
            "paragraflarni unutsangiz — Coherence pasayadi. Har mezon mustaqil "
            "baholanadi.</div>"
        )},
        {"rich_text": (
            "<h3>Band 5 vs Band 7 — his qiling</h3>"
            "<p>Bir xil g'oya, ikki xil daraja. Farqni ko'ring:</p>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>Band 5 (Lexical + Grammar):</strong> <em>\"A lot of people think "
            "cars are bad. Cars make pollution and this is a big problem for the world "
            "and it is bad for health.\"</em><br>"
            "<span style=\"color:#475569;\">Oddiy so'zlar (a lot of, bad, big), "
            "takror, qisqa bir xil gaplar.</span></div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>Band 7:</strong> <em>\"Many people regard private cars as harmful, "
            "primarily because the emissions they produce contribute to air pollution, "
            "which in turn poses a serious threat to public health.\"</em><br>"
            "<span style=\"color:#475569;\">Aniq lug'at (regard as, emissions, poses a "
            "threat), bog'lovchilar (primarily because, which in turn), murakkab "
            "gap tuzilishi.</span></div>"
        )},
        {"rich_text": (
            "<h3>Muhim: Task 2 ikki barobar og'irroq</h3>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> Task 1 va Task 2 birlashib Writing bandini "
            "beradi, lekin <u>Task 2 taxminan ikki baravar</u> ko'proq hissa qo'shadi. "
            "Ya'ni Task 2'da yaxshi yozish ballingizga kuchliroq ta'sir qiladi — vaqt va "
            "kuchni shunga qarab taqsimlang (keyingi dars).</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Talaba juda murakkab, chiroyli so'zlar "
                "ishlatadi, lekin matni bir uzun paragraf — hech qanday bo'linish yo'q. "
                "Qaysi mezon bo'yicha ball yo'qotadi?</p>"
            ),
            "choices": [
                {"text": "Lexical Resource", "is_correct": False},
                {"text": "Coherence & Cohesion", "is_correct": True},
                {"text": "Task Response", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Coherence & "
                "Cohesion.</mark> Lug'at yaxshi bo'lsa ham, <u>paragraflarga bo'linmaslik</u> "
                "va mantiqiy tuzilishning yo'qligi aynan Coherence & Cohesion mezonini "
                "pasaytiradi. Har mezon mustaqil: bittada kuchli bo'lish boshqasidagi "
                "zaiflikni qoplamaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Task 2 essesida talaba faqat bir tomonni "
                "yoritadi, holbuki savol \"discuss both views\" deb so'ragan. Bu qaysi "
                "mezonga eng ko'p zarar beradi?</p>"
            ),
            "choices": [
                {"text": "Grammatical Range", "is_correct": False},
                {"text": "Task Response", "is_correct": True},
                {"text": "Coherence & Cohesion", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task Response.</mark> "
                "Savolning <u>hamma qismiga</u> javob bermaslik (ikki qarashning faqat "
                "birini yoritish) — bu to'g'ridan-to'g'ri Task Response'ni cheklaydi. "
                "Grammatika mukammal bo'lsa ham, savolga to'liq javob bermasangiz, band "
                "yuqoriga chiqmaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> To'rt mezonning yakuniy Writing "
                "bandiga ta'siri qanday?</p>"
            ),
            "choices": [
                {"text": "Task Achievement eng muhim, qolganlari kam ahamiyatli", "is_correct": False},
                {"text": "To'rttasi ham TENG vaznli (har biri 25%)", "is_correct": True},
                {"text": "Grammatika va lug'at boshqalaridan muhimroq", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: to'rttasi teng "
                "vaznli.</mark> Har mezon 0–9 baholanadi va o'rtachasi olinadi (har biri "
                "~25%). Shuning uchun bitta mezonni butunlay e'tiborsiz qoldirib "
                "bo'lmaydi. (Eslatma: bu bitta topshiriq ichida; Task 2 esa Task 1'dan "
                "ko'ra umumiy Writing bandiga ikki baravar ko'proq hissa qo'shadi.)</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Task Achievement / Response</div><div class=\"pp-card-back\">topshiriqni bajarish / savolga javob</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Coherence & Cohesion</div><div class=\"pp-card-back\">izchillik va bog'liqlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Lexical Resource</div><div class=\"pp-card-back\">lug'at boyligi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Grammatical Range & Accuracy</div><div class=\"pp-card-back\">grammatik xilma-xillik va aniqlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a collocation</div><div class=\"pp-card-back\">so'z birikmasi (a sharp rise)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to paraphrase</div><div class=\"pp-card-back\">boshqa so'zlar bilan aytmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a band descriptor</div><div class=\"pp-card-back\">band tavsifi (baholash mezoni)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to weigh (twice as much)</div><div class=\"pp-card-back\">(ikki baravar) og'irroq bo'lmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>4 teng mezon: Task Achievement/Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy.</li>"
            "<li>Har mezon mustaqil — bittasidagi kuch boshqasidagi zaiflikni qoplamaydi.</li>"
            "<li>Band ko'tarish = to'rttasiga alohida ishlash (nafaqat murakkab so'z).</li>"
            "<li>Task 2 umumiy Writing bandiga Task 1'dan ~2 baravar ko'proq hissa qo'shadi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 2 (order 2 — time & word-count budgeting)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Writing 2: Task 1 vs Task 2 — Time and Word-Count Budgeting",
    "summary": "Task 1 (20 daqiqa, 150+ so'z) va Task 2 (40 daqiqa, 250+ so'z): vaqtni to'g'ri taqsimlash, so'z chegarasi qoidalari va reja tuzish.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>60 daqiqa — ikki topshiriq</h2>"
            "<p>IELTS Writing bir soatga <strong>ikki topshiriq</strong>dan iborat. "
            "Ko'p nomzod vaqtni noto'g'ri taqsimlab, Task 2'ga yetarli vaqt qoldirmaydi "
            "— va aynan Task 2 ko'proq ball beradi. To'g'ri byudjet — bu bepul band.</p>"
        )},
        {"rich_text": (
            "<h3>Task 1 va Task 2 — yonma-yon</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>📊 Task 1</strong> — tavsiflash (describe)</p>"
            "<p style=\"margin:0 0 4px;\">⏱️ ~20 daqiqa &nbsp;|&nbsp; ✍️ kamida 150 so'z</p>"
            "<p style=\"margin:0 0 4px;\">Academic: grafik / diagramma / jarayon / xaritani tavsiflash</p>"
            "<p style=\"margin:0;\">General Training: xat (rasmiy / yarim-rasmiy / norasmiy)</p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>📝 Task 2</strong> — insho (essay)</p>"
            "<p style=\"margin:0 0 4px;\">⏱️ ~40 daqiqa &nbsp;|&nbsp; ✍️ kamida 250 so'z</p>"
            "<p style=\"margin:0 0 4px;\">Har ikki modul uchun bir xil: fikr bildirish / munozara / muammo-yechim insho</p>"
            "<p style=\"margin:0;\">Umumiy bandga ~2 baravar ko'proq hissa qo'shadi</p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> ko'p tajribali nomzodlar <u>Task 2'ni "
            "birinchi</u> yozadi (u ko'proq ball beradi va yangi kuch bilan yaxshiroq "
            "chiqadi), keyin Task 1'ga o'tadi. Bu shart emas, lekin sinab ko'ring.</div>"
        )},
        {"rich_text": (
            "<h3>20/40 vaqt rejasi — har topshiriq ichida</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Task 1 (20 daqiqa):</strong> ~3 daqiqa "
            "grafikni tahlil qilib reja tuzing (nima ko'tarilgan/tushgan, eng katta "
            "o'zgarish) → ~15 daqiqa yozing → ~2 daqiqa tekshiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>Task 2 (40 daqiqa):</strong> ~5 daqiqa "
            "reja (pozitsiya + 2 asosiy fikr + misollar) → ~30 daqiqa yozing → "
            "~5 daqiqa tekshiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>Reja bo'sh vaqt emas!</strong> Reja "
            "tuzmasdan yozish — eng katta xato. 5 daqiqalik reja butun inshoni "
            "izchil qiladi (Coherence bandini ko'taradi).</p></div>"
            "<div class=\"pp-step\"><p><strong>Soatni kuzating.</strong> 20 daqiqada "
            "Task 1 tugamasa ham — <u>to'xtang</u> va Task 2'ga o'ting. Task 2'ni "
            "tashlab qo'yish ancha ko'proq ball yo'qotadi.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>So'z chegarasi qoidalari</h3>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Kamida — lekin juda ko'p ham emas:</strong><br>"
            "• <u>150/250 dan KAM</u> yozsangiz — Task Achievement bo'yicha jarima "
            "(so'z sanaladi).<br>"
            "• <u>Juda ko'p</u> (masalan Task 2'da 350+) yozish ballni oshirmaydi — "
            "faqat vaqt yeydi va ko'proq xato imkoniyati tug'iladi.<br>"
            "• Maqsad: Task 1 ~160–190, Task 2 ~260–290 so'z — chegaradan sal yuqori, "
            "sifatli.</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> so'zlarni sanashga vaqt sarflamang — mashqda "
            "o'z qo'lyozmangizda 150/250 so'z qancha joy egallashini o'rganib oling. "
            "Imtihonda shu \"ko'z o'lchovi\" yetarli.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Task 1 va Task 2 uchun tavsiya "
                "etilgan vaqt taqsimoti qanday?</p>"
            ),
            "choices": [
                {"text": "Har ikkisiga 30 daqiqadan", "is_correct": False},
                {"text": "Task 1 ~20 daqiqa, Task 2 ~40 daqiqa", "is_correct": True},
                {"text": "Task 1 ~40 daqiqa, Task 2 ~20 daqiqa", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task 1 ~20, Task 2 "
                "~40 daqiqa.</mark> Task 2 uzunroq (250+ so'z) va ballga ~2 baravar "
                "ko'proq hissa qo'shadi, shuning uchun unga ko'proq vaqt. Task 1'ga 20 "
                "daqiqadan ortiq sarflash — Task 2 hisobiga ball yo'qotish.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Task 2'da 250 so'z o'rniga 180 so'z "
                "yozsangiz nima bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Hech narsa — mazmun yaxshi bo'lsa yetarli", "is_correct": False},
                {"text": "Task Response bo'yicha jarima olasiz (chegaradan kam)", "is_correct": True},
                {"text": "Faqat Grammatika pasayadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Task Response "
                "jarimasi.</mark> 250 so'zdan kam yozish to'g'ridan-to'g'ri Task "
                "Response'ni cheklaydi — g'oyalar yetarlicha rivojlanmagan hisoblanadi. "
                "Baholovchi so'zlarni sanaydi. Har doim chegaradan sal yuqori yozing.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Nega yozishdan oldin 5 daqiqa reja "
                "tuzish tavsiya etiladi?</p>"
            ),
            "choices": [
                {"text": "Reja Coherence & Cohesion'ni oshiradi — matn izchil va paragraflangan bo'ladi", "is_correct": True},
                {"text": "Reja so'z sonini ko'paytiradi", "is_correct": False},
                {"text": "Reja shart emas — darhol yozish yaxshiroq", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Coherence'ni "
                "oshiradi.</mark> 5 daqiqalik reja (pozitsiya + asosiy fikrlar + tartib) "
                "matnni mantiqiy va paragraflangan qiladi — bu Coherence & Cohesion "
                "bandini ko'taradi va yozishni tezlashtiradi. Rejasiz yozish ko'pincha "
                "chalkash, takrorlanuvchi matnga olib keladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to budget time</div><div class=\"pp-card-back\">vaqtni taqsimlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">word count</div><div class=\"pp-card-back\">so'zlar soni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the minimum</div><div class=\"pp-card-back\">eng kam miqdor (chegara)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a penalty</div><div class=\"pp-card-back\">jarima (ball ayirish)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to outline / to plan</div><div class=\"pp-card-back\">reja tuzmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to proofread</div><div class=\"pp-card-back\">xatolarni tekshirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to run out of time</div><div class=\"pp-card-back\">vaqt yetmay qolmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to allocate</div><div class=\"pp-card-back\">ajratmoq (vaqt/kuch)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Task 1: ~20 daqiqa, 150+ so'z; Task 2: ~40 daqiqa, 250+ so'z.</li>"
            "<li>Task 2 ballga ~2 baravar ko'proq hissa qo'shadi — unga ko'proq vaqt.</li>"
            "<li>Chegaradan KAM = jarima; juda ko'p = vaqt isrofi. Maqsad: sal yuqori (160–190 / 260–290).</li>"
            "<li>Har topshiriqda reja tuzing (3–5 daqiqa) — bu Coherence'ni oshiradi.</li>"
            "<li>20 daqiqada Task 1 tugamasa ham to'xtang — Task 2 muhimroq.</li>"
            "</ul>"
        )},
    ],
},

]
