"""
IELTS Speaking lessons 3-5 (orders 10-12) — the "1-qism: Tanish mavzular (Part 1 —
Introduction & Interview)" topic — second Speaking batch, see toc_ielts_speaking.txt.

Each lesson has Q+A demo clips: examiner question = "Woman", model candidate answer
(for shadowing) = "Man". Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_part1_10_12.py \
        --out examprep/management/commands/audio/speaking_part1
then import with --audio-dir. Naming: ielts_s_<order 3-digit>_<block n>.mp3.
Keep speaker names out of the line text.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_PART1 = {
    "title":   "1-qism: Tanish mavzular (Part 1 — Introduction & Interview)",
    "summary": "Part 1: tanish mavzular bo'yicha qisqa, to'g'ridan-to'g'ri javob + bitta "
               "qo'shimcha detal; uy, oila, kundalik tartib, ish/o'qish, hobbi.",
    "icon":    "bi-person-lines-fill",
    "order":   2,
}

# reusable shadowing note
_SHADOW = (
    "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
    "<strong>🗣️ Shadowing:</strong> nomzod ortidan bir xil ohang bilan takrorlang — "
    "3 kun, har kuni 3 marta. Ravonlik va talaffuzni oshiradi.</div>"
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 3 (order 10 — Part 1 format) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART1,
    "title": "IELTS Speaking 3: Part 1 Format — Short, Direct Answers With One Extra Detail",
    "summary": "Part 1 g'oliblik formulasi: to'g'ridan-to'g'ri javob + bitta qo'shimcha detal (sabab/misol). Bir so'zli ham, 2 daqiqalik nutq ham emas.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Part 1 — tanish mavzular, qisqa javoblar</h2>"
            "<p>1-qism ~4–5 daqiqa davom etadi. Imtihonchi <strong>tanish mavzular</strong> "
            "(uy, ish/o'qish, hobbi, kundalik hayot) bo'yicha ~12 ta qisqa savol beradi. "
            "Bu yerda uzun nutq kerak emas — lekin bir so'zli javob ham xato.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 G'oliblik formulasi:</strong> <mark style=\"background:#dcfce7;\">"
            "to'g'ridan-to'g'ri javob + bitta qo'shimcha detal</mark> (sabab, misol yoki "
            "qarshilik). Ya'ni ~2–3 jumla. Bu ravonlik va lug'atni ko'rsatishga yetarli, "
            "lekin Part 2/3'dagidek cho'zilmaydi.</div>"
        )},
        {"rich_text": (
            "<h3>Formula ish jarayonida</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\"><strong>Savol:</strong> \"Do you work or are you a student?\"</p>"
            "<p style=\"margin:0 0 4px;\">❌ Juda qisqa: <em>\"Student.\"</em> (bir so'z — Fluency past)</p>"
            "<p style=\"margin:0 0 4px;\">❌ Juda uzun: <em>\"Well, education is very important in this modern era...\"</em> (Part 1 uchun ortiqcha)</p>"
            "<p style=\"margin:0;\">✅ To'g'ri: <em>\"I'm a student at the moment. I'm studying economics, and I'm actually in my second year now.\"</em> — <u>javob</u> + <u>detal</u>.</p>"
            "</div>"
        )},
        {
            "audio":        "ielts_s_010_1.mp3",
            "audio_script": [
                ("Woman", "Do you work, or are you a student?"),
                ("Man",   "I'm a student at the moment. I'm studying economics at university, and I'm actually in my second year now."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 1.</strong> \"Javob + detal\" formulasini eshiting.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Do you work, or are you a student?<br>"
                "<em style=\"color:#475569;\">Ishlaysizmi yoki talabamisiz?</em></p>"
                "<p><strong>Candidate:</strong> I'm a student at the moment. I'm studying economics at university, and I'm actually in my second year now.<br>"
                "<em style=\"color:#475569;\">Hozircha talabaman. Universitetda iqtisod o'qiyapman va aslida hozir ikkinchi kursdaman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "audio":        "ielts_s_010_2.mp3",
            "audio_script": [
                ("Woman", "Do you prefer mornings or evenings?"),
                ("Man",   "Definitely evenings, I'd say. I'm not really a morning person, so I tend to feel more energetic and focused once the sun goes down."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 2.</strong> Bu javobda \"detal\" — sabab "
                "(\"I'm not really a morning person, so...\").</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Do you prefer mornings or evenings?<br>"
                "<em style=\"color:#475569;\">Ertalabnimi yoki kechqurunni afzal ko'rasiz?</em></p>"
                "<p><strong>Candidate:</strong> Definitely evenings, I'd say. I'm not really a morning person, so I tend to feel more energetic and focused once the sun goes down.<br>"
                "<em style=\"color:#475569;\">Aniq kechqurun desam bo'ladi. Men unchalik ertalabki odam emasman, shuning uchun quyosh botgach o'zimni tetikroq va yig'ilganroq his qilaman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Part 1 javobining ideal uzunligi "
                "qanday?</p>"
            ),
            "choices": [
                {"text": "Bitta so'z (\"Yes\", \"Student\")", "is_correct": False},
                {"text": "To'g'ridan-to'g'ri javob + bitta qo'shimcha detal (~2-3 jumla)", "is_correct": True},
                {"text": "2 daqiqalik uzun nutq", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: javob + bitta "
                "detal.</mark> Bir so'zli javob Fluency'ni ko'rsatmaydi; 2 daqiqalik nutq "
                "esa Part 2 uchun. Part 1'da ~2–3 jumla ideal: aniq javob + sabab/misol/"
                "detal. Bu tabiiy suhbat ohangini beradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"Do you like your hometown?\" savoliga "
                "qaysi javob formulaga MOS?</p>"
            ),
            "choices": [
                {"text": "\"Yes.\"", "is_correct": False},
                {"text": "\"Yes, I do. It's quite a lively place, and I love that there's always something going on at the weekend.\"", "is_correct": True},
                {"text": "\"Hometowns are important for everyone in the world because...\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "To'g'ridan-to'g'ri javob (\"Yes, I do\") + detal (\"lively place... "
                "something going on at the weekend\"). \"Yes\" — juda qisqa; uchinchisi — "
                "umumiy, cho'zilgan va savolga aniq javob bermaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Part 1 phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at the moment</div><div class=\"pp-card-back\">hozircha, ayni paytda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">actually</div><div class=\"pp-card-back\">aslida (detal qo'shish)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Definitely ..., I'd say.</div><div class=\"pp-card-back\">Aniq ... desam bo'ladi.</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a morning person</div><div class=\"pp-card-back\">ertalabki (erta turadigan) odam</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I tend to ...</div><div class=\"pp-card-back\">Men odatda ... qilaman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a lively place</div><div class=\"pp-card-back\">jonli, gavjum joy</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">there's always something going on</div><div class=\"pp-card-back\">doim biror voqea bo'lib turadi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">once the sun goes down</div><div class=\"pp-card-back\">quyosh botgach</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Part 1 — tanish mavzular, ~12 qisqa savol, ~4-5 daqiqa.</li>"
            "<li>Formula: to'g'ridan-to'g'ri javob + bitta qo'shimcha detal (~2-3 jumla).</li>"
            "<li>Bir so'zli javob (Fluency past) va 2 daqiqalik nutq (Part 2) — ikkovi ham xato.</li>"
            "<li>Detal = sabab, misol yoki qarshilik.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 4 (order 11 — home, family, routine) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART1,
    "title": "IELTS Speaking 4: Home, Family, and Daily Routine — Sample Answers",
    "summary": "Part 1 mavzulari: yashash joyi, uy, oila, kundalik tartib — namunaviy javoblar va aniq lug'at (cosy, within walking distance, a creature of habit).",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Uy, oila, kundalik tartib</h2>"
            "<p>Bular Part 1'ning eng ko'p uchraydigan mavzulari. Ularga tayyor "
            "bo'lish — bepul ball, chunki mavzular oldindan ma'lum. Kalit: <strong>aniq, "
            "tavsifiy lug'at</strong> ishlatib, \"javob + detal\" formulasiga rioya "
            "qilish.</p>"
        )},
        {
            "audio":        "ielts_s_011_1.mp3",
            "audio_script": [
                ("Woman", "Can you tell me about the place where you live?"),
                ("Man",   "Sure. I live in a fairly small flat in the city centre. It's quite cosy rather than spacious, but I really like it because almost everything I need is within walking distance."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 1 — yashash joyi.</strong> Aniq sifatlarga e'tibor: "
                "<em>cosy, spacious, within walking distance</em>.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Can you tell me about the place where you live?<br>"
                "<em style=\"color:#475569;\">Yashaydigan joyingiz haqida gapirib bera olasizmi?</em></p>"
                "<p><strong>Candidate:</strong> Sure. I live in a fairly small flat in the city centre. It's quite cosy rather than spacious, but I really like it because almost everything I need is within walking distance.<br>"
                "<em style=\"color:#475569;\">Albatta. Men shahar markazidagi ancha kichik kvartirada yashayman. U keng emas, balki shinam, lekin juda yoqadi, chunki menga kerak bo'lgan deyarli hamma narsa piyoda yurish masofasida.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "audio":        "ielts_s_011_2.mp3",
            "audio_script": [
                ("Woman", "What do you usually do in the mornings?"),
                ("Man",   "Well, I'm quite a creature of habit, to be honest. I usually get up around seven, have a strong coffee, and quickly check the news before I head off to work."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 2 — kundalik tartib.</strong> Ibora: "
                "<em>a creature of habit</em> (odatlariga sodiq odam).</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> What do you usually do in the mornings?<br>"
                "<em style=\"color:#475569;\">Ertalablari odatda nima qilasiz?</em></p>"
                "<p><strong>Candidate:</strong> Well, I'm quite a creature of habit, to be honest. I usually get up around seven, have a strong coffee, and quickly check the news before I head off to work.<br>"
                "<em style=\"color:#475569;\">Xo'sh, rostini aytsam, men odatlarimga ancha sodiq odamman. Odatda soat yettilarda turaman, achchiq qahva ichaman va ishga jo'nashdan oldin tezda yangiliklarni ko'rib chiqaman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Kichik, lekin qulay uyni tasvirlash "
                "uchun qaysi so'z eng mos?</p>"
            ),
            "choices": [
                {"text": "spacious (keng)", "is_correct": False},
                {"text": "cosy (shinam)", "is_correct": True},
                {"text": "enormous (juda katta)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: cosy.</mark> "
                "\"Cosy\" = kichik, lekin issiq va qulay. \"Spacious\" va \"enormous\" — "
                "katta joy (teskarisi). Aniq sifat (cosy vs \"small and nice\") Lexical "
                "Resource'ni ko'taradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"a creature of habit\" iborasi nimani "
                "anglatadi?</p>"
            ),
            "choices": [
                {"text": "Har kuni har xil narsa qiladigan odam", "is_correct": False},
                {"text": "Bir xil kundalik odatlarga sodiq odam", "is_correct": True},
                {"text": "Hayvonlarni yaxshi ko'radigan odam", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: odatlariga sodiq "
                "odam.</mark> \"A creature of habit\" — har kuni bir xil tartibda ish "
                "qiladigan odam. Bunday tabiiy iboralar (idioms) Lexical Resource'ni "
                "kuchaytiradi — lekin faqat to'g'ri ishlatilsa.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Home / family / routine</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">cosy</div><div class=\"pp-card-back\">shinam (kichik va qulay)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">spacious</div><div class=\"pp-card-back\">keng, kenggina</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">within walking distance</div><div class=\"pp-card-back\">piyoda yurish masofasida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a creature of habit</div><div class=\"pp-card-back\">odatlariga sodiq odam</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a close-knit family</div><div class=\"pp-card-back\">ahil, jipslashgan oila</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to head off (to work)</div><div class=\"pp-card-back\">(ishga) jo'namoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a neighbourhood</div><div class=\"pp-card-back\">mahalla, atrof</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to run errands</div><div class=\"pp-card-back\">mayda yumushlarni bajarmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Uy/oila/tartib — Part 1'ning eng ko'p uchraydigan mavzulari; oldindan tayyorlaning.</li>"
            "<li>Aniq, tavsifiy lug'at ishlating: cosy, spacious, within walking distance.</li>"
            "<li>Tabiiy iboralar (a creature of habit, close-knit family) — to'g'ri joyda.</li>"
            "<li>\"Javob + detal\" formulasiga rioya qiling.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 5 (order 12 — work/study & hobbies) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART1,
    "title": "IELTS Speaking 5: Work/Study and Hobbies — Sample Answers",
    "summary": "Part 1 mavzulari: ish/o'qish va bo'sh vaqt/hobbi — namunaviy javoblar va lug'at (in my spare time, a keen ..., to unwind, demanding, rewarding).",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Ish/o'qish va hobbi</h2>"
            "<p>Bu ham Part 1'ning \"kafolatlangan\" mavzulari. Yaxshi javob nafaqat "
            "faktni aytadi, balki <strong>his-tuyg'u yoki sabab</strong> qo'shadi "
            "(nega yoqadi/qiyin?). Aniq lug'at bilan bu mavzular bandingizni "
            "ko'taradi.</p>"
        )},
        {
            "audio":        "ielts_s_012_1.mp3",
            "audio_script": [
                ("Woman", "What do you like to do in your free time?"),
                ("Man",   "In my spare time, I'm a keen photographer. I love wandering around the city taking pictures of old buildings — it's a great way to unwind after a busy week."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 1 — hobbi.</strong> Lug'at: <em>in my spare time, a "
                "keen photographer, to unwind</em>.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> What do you like to do in your free time?<br>"
                "<em style=\"color:#475569;\">Bo'sh vaqtingizda nima qilishni yoqtirasiz?</em></p>"
                "<p><strong>Candidate:</strong> In my spare time, I'm a keen photographer. I love wandering around the city taking pictures of old buildings — it's a great way to unwind after a busy week.<br>"
                "<em style=\"color:#475569;\">Bo'sh vaqtimda men qizg'in fotograf man. Shahar bo'ylab sayr qilib, eski binolarni suratga olishni yaxshi ko'raman — bu band haftadan keyin dam olishning ajoyib usuli.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "audio":        "ielts_s_012_2.mp3",
            "audio_script": [
                ("Woman", "Is your job or your course demanding?"),
                ("Man",   "Yes, it can be quite demanding at times, to be honest. There's a lot to keep on top of, but I find it really rewarding, so I don't mind the pressure too much."),
            ],
            "rich_text": (
                "<p><strong>🎧 Namuna 2 — ish/o'qish.</strong> Qarama-qarshilik bilan "
                "kengaytirish: <em>demanding ... but ... rewarding</em>.</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Is your job or your course demanding?<br>"
                "<em style=\"color:#475569;\">Ishingiz yoki kursingiz og'irmi (ko'p talab qiladimi)?</em></p>"
                "<p><strong>Candidate:</strong> Yes, it can be quite demanding at times, to be honest. There's a lot to keep on top of, but I find it really rewarding, so I don't mind the pressure too much.<br>"
                "<em style=\"color:#475569;\">Ha, rostini aytsam, ba'zan ancha og'ir bo'lishi mumkin. Ulgurish kerak bo'lgan narsa ko'p, lekin men buni juda qoniqarli deb bilaman, shuning uchun bosimga unchalik e'tibor bermayman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> \"a keen photographer\" nimani "
                "anglatadi?</p>"
            ),
            "choices": [
                {"text": "Professional (pullik) fotograf", "is_correct": False},
                {"text": "Fotografiyaga qiziqqan, ishtiyoqli havaskor", "is_correct": True},
                {"text": "Yangi boshlagan fotograf", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ishtiyoqli "
                "havaskor.</mark> \"A keen + [hobby]\" = biror ish/hobbiga qattiq qiziqqan "
                "odam (\"a keen swimmer\", \"a keen reader\"). Professional degani emas. "
                "Bu tabiiy Part 1 iborasi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"to unwind\" fe'li nimani anglatadi?</p>"
            ),
            "choices": [
                {"text": "qattiq ishlamoq", "is_correct": False},
                {"text": "dam olmoq, bo'shashmoq (stressdan keyin)", "is_correct": True},
                {"text": "erta turmoq", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: dam olmoq.</mark> "
                "\"To unwind\" = ish/stressdan keyin bo'shashmoq, hordiq chiqarmoq "
                "(\"relax\" ning boyroq varianti). \"A great way to unwind\" — hobbini "
                "tasvirlashda ajoyib ibora.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Namuna 2'da javob qanday "
                "kengaytirilgan?</p>"
            ),
            "choices": [
                {"text": "Faqat \"Yes\" deb", "is_correct": False},
                {"text": "Qarama-qarshilik bilan: og'ir (demanding), LEKIN qoniqarli (rewarding)", "is_correct": True},
                {"text": "Mavzuni o'zgartirib", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: qarama-qarshilik "
                "bilan.</mark> \"...demanding... <u>but</u>... rewarding, <u>so</u>...\" "
                "— detal qo'shishning kuchli usuli: ikki tomonni ko'rsatib (qiyin, lekin "
                "arziydi), grammatik bog'lovchilar bilan. Bu Fluency va Grammar'ni birga "
                "ko'taradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Work/study &amp; hobbies</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in my spare time</div><div class=\"pp-card-back\">bo'sh vaqtimda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a keen (swimmer/reader)</div><div class=\"pp-card-back\">ishtiyoqli (suzuvchi/kitobxon)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to unwind</div><div class=\"pp-card-back\">dam olmoq, bo'shashmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">demanding</div><div class=\"pp-card-back\">og'ir, ko'p talab qiladigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">rewarding</div><div class=\"pp-card-back\">qoniqarli, arzigulik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to keep on top of ...</div><div class=\"pp-card-back\">... ga ulgurib turmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to major in ...</div><div class=\"pp-card-back\">... yo'nalishida ixtisoslashmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to wander around</div><div class=\"pp-card-back\">sayr qilib yurmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ish/o'qish va hobbi — kafolatlangan Part 1 mavzulari.</li>"
            "<li>Fakt + his-tuyg'u/sabab qo'shing (nega yoqadi/qiyin?).</li>"
            "<li>Aniq lug'at: in my spare time, a keen ..., to unwind, demanding, rewarding.</li>"
            "<li>Qarama-qarshilik (demanding but rewarding) — javobni tabiiy kengaytiradi.</li>"
            "</ul>"
        )},
    ],
},

]
