"""
IELTS Speaking lessons 1-2 (orders 1-2) — the "Strategiya va baholash (Overview &
Scoring)" topic — FIRST Speaking batch, see toc_ielts_speaking.txt. (Academic-only
scope, but Speaking is identical for both modules.)

Speaking audio (§5d): examiner question = "Woman", model candidate answer (for
shadowing) = "Man". Lesson 2 has one Q+A demo clip. Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_strategy_1_2.py \
        --out examprep/management/commands/audio/speaking_strategy
then import with --audio-dir. Naming: ielts_s_<order 3-digit>_<block n>.mp3.
Never put the speaker name in the line text — the label only picks the voice.
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
    "summary": "IELTS Speaking qanday baholanadi (4 mezon) va yodlanganday "
               "eshitilmaydigan tabiiy ravonlik usullari.",
    "icon":    "bi-compass",
    "order":   1,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 1 (order 1 — the four criteria)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Speaking 1: How It's Scored — The Four Criteria Explained",
    "summary": "IELTS Speaking 4 teng mezonga bo'linadi: Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation. Bu suhbat — to'g'ri/noto'g'ri javob yo'q.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>Speaking — bu suhbat, imtihon emas</h2>"
            "<p>IELTS Speaking — imtihonchi (examiner) bilan yuzma-yuz ~11–14 daqiqalik "
            "<strong>suhbat</strong>, 3 qismdan iborat. Muhim tushuncha: bu yerda "
            "<mark style=\"background:#dcfce7;\">to'g'ri yoki noto'g'ri javob yo'q</mark> "
            "— fikringiz baholanmaydi, <u>qanday gapirishingiz</u> baholanadi. To'rtta "
            "teng vaznli mezon bor, har biri 0–9.</p>"
        )},
        {"rich_text": (
            "<h3>To'rt mezon — birma-bir</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Fluency &amp; Coherence (ravonlik va "
            "izchillik).</strong> Uzoq to'xtashlarsiz, silliq gapirasizmi? G'oyalarni "
            "mantiqan bog'laysizmi (bog'lovchilar bilan)? Haddan tashqari ikkilanish yoki "
            "o'zini tuzatish — bandni pasaytiradi.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Lexical Resource (lug'at boyligi).</strong> "
            "Keng va aniq lug'at, iboralar (idioms), kollokatsiyalar. So'zni bilmasangiz "
            "— <u>paraphrase</u> qilib aytib bera olasizmi? Bir xil so'z takrori bandni "
            "cheklaydi.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Grammatical Range &amp; Accuracy "
            "(grammatika).</strong> Oddiy va murakkab tuzilmalarni aralashtirasizmi va "
            "ular to'g'rimi? Turli zamonlar, shart gaplar, ergash gaplar.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Pronunciation (talaffuz).</strong> "
            "Tushunarli, tabiiy urg'u va ohang (intonation). <mark "
            "style=\"background:#dbeafe;\">Aksent muammo emas</mark> — muhimi tushunarli "
            "va tabiiy gapirish.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Band ko'taruvchilar va tushuruvchilar</h3>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>✅ Ko'taradi:</strong> javoblarni <u>kengaytirish</u> (sabab + misol), "
            "xilma-xil lug'at va grammatika, aniq talaffuz, tabiiy oqim.</div>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>❌ Tushiradi:</strong> <u>yodlangan</u> javoblar (imtihonchi darhol "
            "sezadi va jazolaydi!), bir so'zli javoblar (\"Yes.\", \"No.\"), uzoq "
            "sukunat, bir xil so'z/gap takrori.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> IELTS Speaking'da fikringiz (masalan "
                "\"mushuklar yaxshi\" degan qarash) baholanadimi?</p>"
            ),
            "choices": [
                {"text": "Ha — to'g'ri fikr bildirish kerak", "is_correct": False},
                {"text": "Yo'q — fikr baholanmaydi; QANDAY gapirishingiz (til) baholanadi", "is_correct": True},
                {"text": "Faqat 3-qismda baholanadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: yo'q.</mark> "
                "Speaking to'g'ri/noto'g'ri fikrni emas, <u>tilingizni</u> (ravonlik, "
                "lug'at, grammatika, talaffuz) baholaydi. Istalgan pozitsiyani "
                "tanlashingiz mumkin — muhimi uni yaxshi <u>ifodalash</u>. Fikringiz "
                "\"noto'g'ri\" deb ball kamaymaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Talaba javoblarni oldindan yodlab, "
                "so'zma-so'z aytadi. Bu nima uchun xavfli?</p>"
            ),
            "choices": [
                {"text": "Xavfsiz — yodlangan javob har doim to'g'ri", "is_correct": False},
                {"text": "Imtihonchi yodlangan javobni darhol sezadi va Fluency bo'yicha jazolaydi", "is_correct": True},
                {"text": "Faqat talaffuzga ta'sir qiladi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: imtihonchi "
                "sezadi.</mark> Yodlangan javoblar ohang va tabiiylikda \"sun'iy\" "
                "eshitiladi, savolga aniq mos kelmaydi — imtihonchilar buni tez ilg'aydi "
                "va Fluency & Coherence bandini tushiradi. Tabiiy, jonli javob har doim "
                "yaxshiroq.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Talaffuz (Pronunciation) mezoni haqida "
                "qaysi fikr TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "Ingliz/amerika aksenti bo'lishi shart", "is_correct": False},
                {"text": "Aksent muhim emas — tushunarli va tabiiy urg'u/ohang muhim", "is_correct": True},
                {"text": "Faqat tez gapirish kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: aksent muhim "
                "emas.</mark> Pronunciation aksentni emas, <u>tushunarlilik</u>, so'z va "
                "gap urg'usi, ohang (intonation)ni baholaydi. O'zbek aksenti bilan ham "
                "yuqori ball olish mumkin — muhimi aniq va tabiiy gapirish. Tezlik "
                "ravonlik degani emas.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Fluency &amp; Coherence</div><div class=\"pp-card-back\">ravonlik va izchillik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Lexical Resource</div><div class=\"pp-card-back\">lug'at boyligi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Grammatical Range &amp; Accuracy</div><div class=\"pp-card-back\">grammatik xilma-xillik va aniqlik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Pronunciation</div><div class=\"pp-card-back\">talaffuz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to extend an answer</div><div class=\"pp-card-back\">javobni kengaytirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">intonation</div><div class=\"pp-card-back\">ohang, intonatsiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a memorised answer</div><div class=\"pp-card-back\">yodlangan javob (jazolanadi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an examiner</div><div class=\"pp-card-back\">imtihonchi</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Speaking — suhbat; to'g'ri/noto'g'ri fikr yo'q, TIL baholanadi.</li>"
            "<li>4 teng mezon: Fluency &amp; Coherence, Lexical Resource, Grammar, Pronunciation.</li>"
            "<li>Ko'taradi: kengaytirilgan javob, xilma-xil til, tabiiy oqim.</li>"
            "<li>Tushiradi: yodlangan javob, bir so'zli javob, uzoq sukunat. Aksent muammo emas.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 2 (order 2 — fillers & fluency) — AUDIO demo (Woman Q + Man A)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Speaking 2: Fillers and Fluency Tricks That Don't Sound Memorized",
    "summary": "Tabiiy fillerlar (Well, ..., Let me think, ..., Actually, ...) o'ylash uchun vaqt beradi; ravonlik = tezlik emas, oqim; yodlangan shablonlardan qoching.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Ravonlik = oqim, tezlik emas</h2>"
            "<p>Ko'p talaba \"ravon\" degani \"tez\" deb o'ylaydi — bu xato. "
            "<strong>Fluency</strong> — bu <u>oqim</u>: uzoq sukunatsiz, fikrni o'rtada "
            "to'xtatmasdan gapirish. O'ylash uchun vaqt kerak bo'lsa, <mark "
            "style=\"background:#dbeafe;\">tabiiy filler</mark> ishlating — jim qolib "
            "ketishdan ko'ra ancha yaxshi.</p>"
        )},
        {"rich_text": (
            "<h3>Tabiiy fillerlar — o'ylash uchun vaqt sotib oling</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Boshlash / vaqt olish:</strong> \"Well, ...\", \"Let me think, ...\", \"That's an interesting question, ...\", \"I suppose, ...\"</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Fikrni yumshatish:</strong> \"I'd say ...\", \"To be honest, ...\", \"Actually, ...\", \"As far as I know, ...\"</p>"
            "<p style=\"margin:0;\"><strong>Misolga o'tish:</strong> \"For example, ...\", \"Like, when ...\", \"A good example would be ...\"</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Qochish kerak:</strong> (1) haddan ortiq \"um, er, uh\" — tabiiy "
            "filler ular o'rnini bosadi; (2) <u>yodlangan shablon</u> iboralar "
            "(\"In this modern era of globalisation...\") — imtihonchi sezadi va bu "
            "savolga mos kelmasa, ballni tushiradi. Filler qisqa va tabiiy bo'lsin.</div>"
        )},
        {
            "audio":        "ielts_s_002_1.mp3",
            "audio_script": [
                ("Woman", "Do you enjoy cooking?"),
                ("Man",   "Well, that's an interesting question. I'd say I do enjoy it, actually, especially at the weekend when I have a bit more time. During the week, though, I tend to keep things fairly simple, you know, just something quick after work."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang.</strong> Imtihonchi (Woman) savol beradi, "
                "nomzod (Man) tabiiy fillerlar bilan javob beradi. Qaysi fillerlarni "
                "eshitasiz? (\"Well\", \"that's an interesting question\", \"I'd say\", "
                "\"actually\", \"though\", \"you know\")</p>"
                "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
                "<strong>🗣️ Shadowing (soya qilish) usuli:</strong> audioni tinglab, "
                "nomzod ortidan <u>bir xil ohang bilan</u> takrorlang. 3 kun davomida, "
                "har kuni 3 marta — bu ravonlik va talaffuzni sezilarli oshiradi.</div>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing (avval o'zingiz aytib ko'ring!)</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Do you enjoy cooking?<br>"
                "<em style=\"color:#475569;\">Ovqat pishirishni yoqtirasizmi?</em></p>"
                "<p><strong>Candidate:</strong> Well, that's an interesting question. I'd say I do enjoy it, actually, especially at the weekend when I have a bit more time. During the week, though, I tend to keep things fairly simple, you know, just something quick after work.<br>"
                "<em style=\"color:#475569;\">Xo'sh, bu qiziqarli savol. Aslida yoqtiraman desam bo'ladi, ayniqsa dam olish kunlari vaqtim ko'proq bo'lganda. Lekin ish kunlari odatda oddiyroq qilaman — bilasiz-ku, ishdan keyin tezgina biror narsa.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> IELTS Speaking'da \"fluency\" (ravonlik) "
                "aslida nimani anglatadi?</p>"
            ),
            "choices": [
                {"text": "Iloji boricha tez gapirish", "is_correct": False},
                {"text": "Uzoq to'xtashlarsiz, silliq va uzluksiz OQIM bilan gapirish", "is_correct": True},
                {"text": "Ko'p murakkab so'z ishlatish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: silliq oqim.</mark> "
                "Fluency — tezlik emas, <u>oqim</u>: fikrni uzoq sukunatsiz davom "
                "ettirish. Juda tez gapirish talaffuzni buzishi mumkin. Sekin, lekin "
                "ravon gapirish — tez, lekin to'xtab-to'xtab gapirishdan yaxshiroq.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Savolni eshitib, o'ylashga vaqt kerak "
                "bo'ldi. Eng yaxshi yo'l qaysi?</p>"
            ),
            "choices": [
                {"text": "Jim qolib, o'ylab olish", "is_correct": False},
                {"text": "Tabiiy filler ishlatish: \"That's an interesting question, let me think...\"", "is_correct": True},
                {"text": "\"Um, er, uh\" ni uzoq takrorlash", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: tabiiy filler.</mark> "
                "Qisqa, tabiiy filler (\"Let me think...\") sukunatni to'ldiradi va "
                "o'ylash uchun vaqt beradi — oqim buzilmaydi. Uzoq jimlik va cheksiz "
                "\"um, er\" Fluency'ni pasaytiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Nega yodlangan shablon iboralar (\"In "
                "this modern era...\") xavfli?</p>"
            ),
            "choices": [
                {"text": "Ular har doim mos keladi", "is_correct": False},
                {"text": "Imtihonchi ularni yodlangan deb sezadi va savolga mos kelmasa, ball tushadi", "is_correct": True},
                {"text": "Ular talaffuzni yaxshilaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: imtihonchi "
                "sezadi.</mark> Yodlangan, \"tayyor\" iboralar ko'pincha savolga aniq mos "
                "kelmaydi va sun'iy eshitiladi — imtihonchilar buni ilg'aydi. Tabiiy, "
                "qisqa fillerlar (\"Well\", \"I'd say\") xavfsiz va samarali.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Fillers &amp; fluency</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Well, ...</div><div class=\"pp-card-back\">Xo'sh, ... (boshlash)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">That's an interesting question.</div><div class=\"pp-card-back\">Bu qiziqarli savol. (vaqt olish)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Let me think, ...</div><div class=\"pp-card-back\">O'ylab ko'ray, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I'd say ...</div><div class=\"pp-card-back\">... desam bo'ladi (fikr)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">To be honest, ...</div><div class=\"pp-card-back\">Rostini aytsam, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Actually, ...</div><div class=\"pp-card-back\">Aslida, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">you know</div><div class=\"pp-card-back\">bilasiz-ku (tabiiy filler)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">shadowing</div><div class=\"pp-card-back\">soya qilib takrorlash (mashq usuli)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Fluency = oqim, tezlik emas; fikrni uzoq sukunatsiz davom ettiring.</li>"
            "<li>Tabiiy fillerlar (\"Well\", \"Let me think\", \"I'd say\") o'ylash uchun vaqt beradi.</li>"
            "<li>Qoching: uzun \"um/er\", yodlangan shablon iboralar (imtihonchi sezadi).</li>"
            "<li>Shadowing: 3 kun × 3 marta model javobni takrorlash — ravonlik va talaffuzni oshiradi.</li>"
            "</ul>"
        )},
    ],
},

]
