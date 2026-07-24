"""
IELTS Listening lessons 10-12 (orders 30-32) — the "3-bo'lim: Moslashtirish va munozara
(Section 3 — Matching & Discussion Multiple Choice)" topic — fourth Listening batch,
see toc_ielts_listening.txt.

Section 3 = an educational DISCUSSION, up to 4 speakers. Use distinct voice labels so
each person is audibly trackable: Woman=en-GB-Sonia, Man=en-GB-Ryan, Woman2=en-AU-Natasha,
Man2=en-US-Guy. Names are woven into the dialogue naturally (mid-sentence) so learners can
match voice->name; NEVER as a leading "Name:" tag (that would be voiced — see the fix).
Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_section3_30_32.py \
        --out examprep/management/commands/audio/ielts_listening_section3
then import with --audio-dir. See STYLE_GUIDE_IELTS.md §5c.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_SECTION3 = {
    "title":   "3-bo'lim: Moslashtirish va munozara (Section 3 — Matching & Discussion Multiple Choice)",
    "summary": "Ta'limiy munozara (4 kishigacha): kim nima deganini kuzatish, rozilik/"
               "e'tirozni ajratish va fikr/vazifalarni odamlarga ulash.",
    "icon":    "bi-people",
    "order":   4,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 10 (order 30 — Intro to Section 3) — AUDIO (3 speakers)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION3,
    "title": "IELTS Listening 10: Intro to Section 3 — Educational Discussion, Up to 4 Speakers",
    "summary": "Section 3 formati: ta'limiy munozara (o'qituvchi + talabalar), akademik lug'at; so'zlovchilarni ovoz va ism orqali ajratish.",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Section 3 — munozara boshlanadi</h2>"
            "<p>3-bo'limda kontekst <u>akademik</u> bo'ladi: odatda ikki-uch talaba "
            "(ba'zan o'qituvchi bilan) biror <strong>loyiha, topshiriq yoki tadqiqotni "
            "muhokama qiladi</strong>. Endi <mark style=\"background:#fef3c7;\">to'rt "
            "kishigacha</mark> so'zlashishi mumkin — asosiy qiyinchilik <em>kim nima "
            "deganini</em> kuzatib borish.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> so'zlovchilar boshida odatda <u>ismlari bilan</u> "
            "tanishtiriladi (\"Tom, how did your group get on?\"). Ismlarni darhol "
            "belgilab qo'ying — savollar (ayniqsa matching) \"kim aytdi\"ga bog'liq "
            "bo'ladi. Ovozlar ham farq qiladi (erkak/ayol) — buni ham langar qiling.</div>"
        )},
        {"rich_text": (
            "<h3>Section 1–2'dan farqi</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Ko'proq so'zlovchi:</strong> 2–4 kishi, ovozlar almashinadi — diqqatni bo'lmaslik kerak.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Akademik lug'at:</strong> \"data\", \"sample\", \"analysis\", \"deadline\", \"reference\" — ilmiy so'zlar ko'payadi.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Fikr va munosabat:</strong> faqat fakt emas — kim rozi, kim e'tiroz bildiryapti (keyingi dars).</p>"
            "<p style=\"margin:0;\"><strong>Savol turlari:</strong> ko'p variantli (MC) va matching (fikr/vazifani odamga ulash).</p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> pauza'da savollarni o'qib, har savol "
            "<u>qaysi so'zlovchi</u> haqida ekanini belgilang. Munozara \"loyiha "
            "bosqichlari\" tartibida boradi — savollar ham shu tartibda.</div>"
        )},
        {
            "audio":        "ielts_l_030_1.mp3",
            "audio_script": [
                ("Woman",  "Right, let's go over your field trip reports. Tom, how did your group get on with the river study?"),
                ("Man",    "Quite well, thanks. We measured the water flow at three points. The tricky part was setting up the equipment — it kept slipping."),
                ("Woman",  "And Lena, your group looked at the soil, didn't you?"),
                ("Woman2", "Yes, we collected samples along the riverbank. Our main problem was that it started to rain halfway through, so a few readings were unreliable."),
                ("Woman",  "That happens a lot. Tom, what would you do differently next time?"),
                ("Man",    "Honestly, I'd allow more time. We rushed the final measurements and I'm not confident they're accurate."),
                ("Woman2", "For us, I'd just pick a drier day if the weather forecast allowed it."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> O'qituvchi (Woman) ikki "
                "talaba bilan — <strong>Tom</strong> (Man) va <strong>Lena</strong> "
                "(Woman2) — dala amaliyotini muhokama qiladi. Kim nima deganini "
                "kuzating:</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Tutor:</strong> Right, let's go over your field trip reports. Tom, how did your group get on with the river study?<br>"
                "<em style=\"color:#475569;\">Xo'sh, dala amaliyoti hisobotlaringizni ko'rib chiqaylik. Tom, guruhing daryo tadqiqotini qanday uddalaadi?</em></p>"
                "<p><strong>Tom:</strong> Quite well, thanks. We measured the water flow at three points. The tricky part was setting up the equipment — it kept slipping.<br>"
                "<em style=\"color:#475569;\">Yaxshi, rahmat. Suv oqimini uch nuqtada o'lchadik. Qiyin qismi jihozni o'rnatish edi — u sirg'anib ketaverdi.</em></p>"
                "<p><strong>Tutor:</strong> And Lena, your group looked at the soil, didn't you?<br>"
                "<em style=\"color:#475569;\">Lena, guruhing tuproqni o'rgandi, shundaymi?</em></p>"
                "<p><strong>Lena:</strong> Yes, we collected samples along the riverbank. Our main problem was that it started to rain halfway through, so a few readings were unreliable.<br>"
                "<em style=\"color:#475569;\">Ha, daryo bo'yidan namunalar to'pladik. Asosiy muammomiz — o'rtada yomg'ir boshlandi, shuning uchun ba'zi o'lchovlar ishonchsiz edi.</em></p>"
                "<p><strong>Tutor:</strong> That happens a lot. Tom, what would you do differently next time?<br>"
                "<em style=\"color:#475569;\">Bu ko'p uchraydi. Tom, keyingi safar nimani boshqacha qilarding?</em></p>"
                "<p><strong>Tom:</strong> Honestly, I'd allow more time. We rushed the final measurements and I'm not confident they're accurate.<br>"
                "<em style=\"color:#475569;\">Rostini aytsam, ko'proq vaqt ajratardim. Oxirgi o'lchovlarni shoshib qildik va ular aniqligiga ishonchim yo'q.</em></p>"
                "<p><strong>Lena:</strong> For us, I'd just pick a drier day if the weather forecast allowed it.<br>"
                "<em style=\"color:#475569;\">Biz uchun esa, ob-havo imkon bersa, quruqroq kunni tanlardim.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Tom guruhi uchun qaysi qism qiyin bo'ldi?</p>"
            ),
            "choices": [
                {"text": "jihozni o'rnatish (setting up the equipment)", "is_correct": True},
                {"text": "yomg'ir yog'ishi", "is_correct": False},
                {"text": "namuna to'plash", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: jihozni "
                "o'rnatish.</mark> Tom: \"The tricky part was <u>setting up the "
                "equipment</u> — it kept slipping.\" Yomg'ir — bu Lena guruhining "
                "muammosi (so'zlovchilarni aralashtirmang!). Har muammoni to'g'ri "
                "odamga bog'lang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Lena guruhida nima muammo bo'ldi?</p>"
            ),
            "choices": [
                {"text": "jihoz sirg'andi", "is_correct": False},
                {"text": "yomg'ir tufayli ba'zi o'lchovlar ishonchsiz bo'ldi", "is_correct": True},
                {"text": "vaqt yetmadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: yomg'ir tufayli "
                "o'lchovlar ishonchsiz.</mark> Lena: \"it started to rain halfway "
                "through, so a few <u>readings were unreliable</u>.\" \"Jihoz sirg'andi\" "
                "— Tom guruhi; \"vaqt yetmadi\" — Tom keyingi safar haqida aytadi. Ovoz "
                "(ayol, Woman2) va ism (Lena) sizga langar.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Tom keyingi safar nimani boshqacha "
                "qilardi?</p>"
            ),
            "choices": [
                {"text": "quruqroq kun tanlardi", "is_correct": False},
                {"text": "ko'proq vaqt ajratardi", "is_correct": True},
                {"text": "boshqa jihoz olardi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ko'proq vaqt "
                "ajratardi.</mark> Tom: \"I'd <u>allow more time</u>. We rushed the final "
                "measurements.\" \"Quruqroq kun\" — bu Lena'ning javobi (savol Tom haqida "
                "edi). Savol qaysi ODAM haqida ekanini aniq belgilang.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a field trip</div><div class=\"pp-card-back\">dala amaliyoti/sayohati</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a sample</div><div class=\"pp-card-back\">namuna</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a reading (measurement)</div><div class=\"pp-card-back\">o'lchov ko'rsatkichi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">unreliable</div><div class=\"pp-card-back\">ishonchsiz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to set up equipment</div><div class=\"pp-card-back\">jihozni o'rnatmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to rush</div><div class=\"pp-card-back\">shoshib qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">accurate</div><div class=\"pp-card-back\">aniq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">weather forecast</div><div class=\"pp-card-back\">ob-havo bashorati</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Section 3 — akademik munozara (talabalar + o'qituvchi), 4 kishigacha.</li>"
            "<li>So'zlovchilar boshida ism bilan tanishtiriladi — ismlarni darhol belgilang.</li>"
            "<li>Har fikr/muammoni to'g'ri ODAMga bog'lang — ovoz + ism = langar.</li>"
            "<li>Savol qaysi so'zlovchi haqida ekanini oldindan belgilang; munozara loyiha tartibida boradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 11 (order 31 — tracking who says what: opinion/agreement/disagreement) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION3,
    "title": "IELTS Listening 11: Tracking Who Says What — Agreement and Disagreement",
    "summary": "Fikr, rozilik va e'tirozni ajratish: signal iboralar (I'm not so sure, that's a fair point, I agree); yakuniy kelishilgan qarorni ushlash.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>Kim rozi, kim qarshi?</h2>"
            "<p>Section 3'ning yuragi — <strong>fikr va munosabat</strong>. Savollar "
            "ko'pincha \"X kim o'ylaydi?\" yoki \"Ular nimaga qaror qildi?\" turida. "
            "Bunda ikki narsani kuzatish kerak: (1) har kimning <u>fikri</u>, va "
            "(2) ular <u>rozimi</u> yoki <u>e'tiroz</u> bildiryaptimi. Yakuniy "
            "<mark style=\"background:#dcfce7;\">kelishilgan qaror</mark> — ko'pincha "
            "javob.</p>"
        )},
        {"rich_text": (
            "<h3>Signal iboralar — rozilik va e'tiroz</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Rozilik (agreement):</strong> <em>\"I agree\", \"That's a fair point\", \"Exactly\", \"You're right\", \"Good idea\"</em></p>"
            "<p style=\"margin:0 0 6px;\"><strong>E'tiroz (disagreement):</strong> <em>\"I'm not so sure\", \"I don't think so\", \"Actually...\", \"Yes, but...\", \"I'd argue...\"</em></p>"
            "<p style=\"margin:0;\"><strong>Fikrni yumshatish (hedging):</strong> <em>\"Maybe we could...\", \"Perhaps...\", \"It might be better to...\"</em></p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — fikr o'zgaradi:</strong> so'zlovchi biror g'oyani "
            "taklif qiladi, boshqasi e'tiroz bildiradi, keyin <u>ikkovi kelishadi</u>. "
            "Savol yakuniy qarorni so'rasa — birinchi taklifni emas, <u>oxirgi "
            "kelishuvni</u> yozing. \"That's a fair point\" — fikr o'zgarish "
            "boshlanganini bildiradi.</div>"
        )},
        {
            "audio":        "ielts_l_031_1.mp3",
            "audio_script": [
                ("Man",    "So, for your joint presentation, have you decided on a topic yet?"),
                ("Woman",  "We were thinking about renewable energy, but I feel it's a bit too broad."),
                ("Man2",   "Yeah, I'm not so sure renewable energy is the best choice. There's so much material we might struggle to focus."),
                ("Woman",  "That's a fair point, Josh. Maybe we could narrow it down to just solar power?"),
                ("Man2",   "Yes, I'd be much happier with that. Solar power on its own is manageable."),
                ("Man",    "I agree — a narrower topic almost always scores better. Now, what about the length?"),
                ("Woman",  "The guidelines say fifteen minutes, but I heard somewhere we can go up to twenty."),
                ("Man",    "No, stick to fifteen. Twenty minutes is only for the final-year groups."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> O'qituvchi (Man) ikki "
                "talaba — <strong>Anna</strong> (Woman) va <strong>Josh</strong> (Man2) "
                "— bilan taqdimot mavzusini muhokama qiladi. Kim rozi, kim e'tiroz "
                "bildiryapti, va nimaga kelishishdi?</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Tutor:</strong> So, for your joint presentation, have you decided on a topic yet?<br>"
                "<em style=\"color:#475569;\">Xo'sh, qo'shma taqdimotingiz uchun mavzu tanladingizmi?</em></p>"
                "<p><strong>Anna:</strong> We were thinking about renewable energy, but I feel it's a bit too broad.<br>"
                "<em style=\"color:#475569;\">Biz qayta tiklanadigan energiyani o'ylagandik, lekin menimcha u biroz keng.</em></p>"
                "<p><strong>Josh:</strong> Yeah, I'm not so sure renewable energy is the best choice. There's so much material we might struggle to focus.<br>"
                "<em style=\"color:#475569;\">Ha, qayta tiklanadigan energiya eng yaxshi tanlov ekaniga ishonchim komil emas. Shunchalik ko'p material borki, diqqatni jamlash qiyin bo'lishi mumkin.</em></p>"
                "<p><strong>Anna:</strong> That's a fair point, Josh. Maybe we could narrow it down to just solar power?<br>"
                "<em style=\"color:#475569;\">Bu o'rinli fikr, Josh. Balki uni faqat quyosh energiyasiga toraytirsak?</em></p>"
                "<p><strong>Josh:</strong> Yes, I'd be much happier with that. Solar power on its own is manageable.<br>"
                "<em style=\"color:#475569;\">Ha, bunga ancha xursand bo'lardim. Quyosh energiyasi o'zi bilan uddalasa bo'ladi.</em></p>"
                "<p><strong>Tutor:</strong> I agree — a narrower topic almost always scores better. Now, what about the length?<br>"
                "<em style=\"color:#475569;\">Roziman — torroq mavzu deyarli har doim yaxshiroq baholanadi. Endi, uzunligi-chi?</em></p>"
                "<p><strong>Anna:</strong> The guidelines say fifteen minutes, but I heard somewhere we can go up to twenty.<br>"
                "<em style=\"color:#475569;\">Qoidalarda 15 daqiqa deyilgan, lekin qayerdadir 20 gacha bo'lishi mumkin deb eshitdim.</em></p>"
                "<p><strong>Tutor:</strong> No, stick to fifteen. Twenty minutes is only for the final-year groups.<br>"
                "<em style=\"color:#475569;\">Yo'q, 15 daqiqada qoling. 20 daqiqa faqat bitiruvchi kurs guruhlari uchun.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Josh \"renewable energy\" mavzusi haqida "
                "nima deb o'ylaydi?</p>"
            ),
            "choices": [
                {"text": "Bu ideal mavzu", "is_correct": False},
                {"text": "U juda keng — diqqatni jamlash qiyin bo'ladi", "is_correct": True},
                {"text": "U juda tor", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: juda keng.</mark> "
                "Josh: \"<u>I'm not so sure</u> renewable energy is the best choice. "
                "There's so much material we might <u>struggle to focus</u>.\" \"I'm not "
                "so sure\" — e'tiroz signali. U mavzuni keng (broad) deb hisoblaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Ular oxirida qaysi mavzuga kelishishdi?</p>"
            ),
            "choices": [
                {"text": "renewable energy", "is_correct": False},
                {"text": "solar power", "is_correct": True},
                {"text": "ular kelisha olishmadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: solar power.</mark> "
                "Anna: \"Maybe we could <u>narrow it down to just solar power</u>?\" "
                "Josh: \"Yes, I'd be much happier with that.\" O'qituvchi: \"I agree.\" "
                "Uchalasi kelishdi. \"renewable energy\" — dastlabki (rad etilgan) g'oya; "
                "yakuniy kelishuv — solar power.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Taqdimot qancha davom etishi kerak?</p>"
            ),
            "choices": [
                {"text": "15 daqiqa", "is_correct": True},
                {"text": "20 daqiqa", "is_correct": False},
                {"text": "istalgancha", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 15 daqiqa.</mark> "
                "Anna 20 gacha bo'lishi mumkin deb eshitgan, lekin o'qituvchi tuzatadi: "
                "\"No, <u>stick to fifteen</u>. Twenty minutes is only for the final-year "
                "groups.\" \"No\" — e'tiroz/tuzatish. 20 — faqat bitiruvchilar uchun "
                "(distraktor). Javob: 15.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I'm not so sure</div><div class=\"pp-card-back\">unchalik ishonchim yo'q (e'tiroz)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">That's a fair point</div><div class=\"pp-card-back\">bu o'rinli fikr</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to narrow down</div><div class=\"pp-card-back\">toraytirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">broad</div><div class=\"pp-card-back\">keng (mavzu)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">manageable</div><div class=\"pp-card-back\">uddalasa bo'ladigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to stick to</div><div class=\"pp-card-back\">~da qolmoq, rioya qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">guidelines</div><div class=\"pp-card-back\">qoidalar, ko'rsatmalar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a joint presentation</div><div class=\"pp-card-back\">qo'shma taqdimot</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Fikr + munosabatni kuzating: kim taklif qildi, kim rozi/qarshi.</li>"
            "<li>Signal iboralar: \"I'm not so sure\" (e'tiroz), \"That's a fair point\" (fikr o'zgarishi), \"I agree\" (rozilik).</li>"
            "<li>Savol yakuniy qarorni so'rasa — birinchi taklif emas, OXIRGI kelishuv.</li>"
            "<li>\"No, stick to...\" — tuzatish; distraktorni (20 daqiqa) rad etadi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 12 (order 32 — Matching: assign opinions/tasks to speakers) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION3,
    "title": "IELTS Listening 12: Matching — Assigning Tasks to Speakers (Full Practice)",
    "summary": "To'liq Section 3 amaliyoti: vazifalarni (research, slides, intro...) to'g'ri odamga ulash — ovoz + ism orqali kuzatish, taklif vs qabul tuzog'i.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Matching — kim nimani qiladi?</h2>"
            "<p>Section 3'ning eng ko'p uchraydigan matching turi: <strong>vazifa yoki "
            "fikrlar ro'yxatini odamlarga ulash</strong>. Masalan: \"loyihaning qaysi "
            "qismini kim bajaradi?\" Reading'dagi Matching Features kabi — faqat real "
            "vaqtda, ovoz orqali. Kalit: har odamni (ovoz + ism) langar qilib, kim "
            "nimani <u>qabul qilganini</u> kuzatish.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — taklif ≠ qabul:</strong> bir kishi vazifani "
            "<u>boshqasiga taklif</u> qilishi mumkin (\"Why don't you do it, Ben?\"). "
            "Vazifa taklif qilingan odamga tegishli — taklif qilgan odamga emas. Kim "
            "oxirida \"OK, I'll do it\" deganini kuzating.</div>"
        )},
        {
            "audio":        "ielts_l_032_1.mp3",
            "audio_script": [
                ("Man",    "OK team, let's divide up the project. There are four parts: the research, the slides, the introduction, and the data analysis."),
                ("Woman",  "I'm happy to do the research, Ben. I like digging through sources."),
                ("Man",    "Thanks, Sara — that's the research covered."),
                ("Woman2", "I could take the data analysis. I did statistics last year, so the numbers don't scare me."),
                ("Man",    "Perfect, Mia. And I'll make the slides myself, since I've got the design software."),
                ("Woman",  "So who's doing the introduction?"),
                ("Woman2", "Why don't you do that too, Ben? You're the most confident speaker."),
                ("Man",    "Ha, all right — I'll do the introduction as well as the slides."),
                ("Woman",  "Great. And I'll email the tutor afterwards to confirm everything."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> Uch talaba — "
                "<strong>Sara</strong> (Woman), <strong>Ben</strong> (Man) va "
                "<strong>Mia</strong> (Woman2) — loyihani bo'lishadi. Har vazifani "
                "to'g'ri odamga ulang:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>WHO DOES WHAT?</strong> (A = Sara, B = Ben, C = Mia)</p>"
                "<p style=\"margin:0 0 4px;\">Research: <strong>(1) ___</strong> &nbsp; Data analysis: <strong>(2) ___</strong></p>"
                "<p style=\"margin:0 0 4px;\">Slides: <strong>(3) ___</strong> &nbsp; Introduction: <strong>(4) ___</strong></p>"
                "<p style=\"margin:0;\">Email the tutor: <strong>(5) ___</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 5 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Ben:</strong> OK team, let's divide up the project. There are four parts: the research, the slides, the introduction, and the data analysis.<br>"
                "<em style=\"color:#475569;\">Mayli jamoa, loyihani bo'laylik. To'rt qism bor: tadqiqot, slaydlar, kirish va ma'lumot tahlili.</em></p>"
                "<p><strong>Sara:</strong> I'm happy to do the research, Ben. I like digging through sources.<br>"
                "<em style=\"color:#475569;\">Men tadqiqotni bajarishga tayyorman, Ben. Manbalarni titkilashni yoqtiraman.</em></p>"
                "<p><strong>Ben:</strong> Thanks, Sara — that's the research covered.<br>"
                "<em style=\"color:#475569;\">Rahmat, Sara — tadqiqot hal bo'ldi.</em></p>"
                "<p><strong>Mia:</strong> I could take the data analysis. I did statistics last year, so the numbers don't scare me.<br>"
                "<em style=\"color:#475569;\">Men ma'lumot tahlilini olsam bo'ladi. O'tgan yili statistika o'qiganman, shuning uchun raqamlardan qo'rqmayman.</em></p>"
                "<p><strong>Ben:</strong> Perfect, Mia. And I'll make the slides myself, since I've got the design software.<br>"
                "<em style=\"color:#475569;\">Zo'r, Mia. Slaydlarni esa o'zim qilaman, chunki menda dizayn dasturi bor.</em></p>"
                "<p><strong>Sara:</strong> So who's doing the introduction?<br>"
                "<em style=\"color:#475569;\">Xo'sh, kirishni kim qiladi?</em></p>"
                "<p><strong>Mia:</strong> Why don't you do that too, Ben? You're the most confident speaker.<br>"
                "<em style=\"color:#475569;\">Uni ham sen qilsang-chi, Ben? Sen eng ishonchli notiqsan.</em></p>"
                "<p><strong>Ben:</strong> Ha, all right — I'll do the introduction as well as the slides.<br>"
                "<em style=\"color:#475569;\">Ha, mayli — slaydlar bilan birga kirishni ham qilaman.</em></p>"
                "<p><strong>Sara:</strong> Great. And I'll email the tutor afterwards to confirm everything.<br>"
                "<em style=\"color:#475569;\">Ajoyib. Men esa keyin o'qituvchiga hammasini tasdiqlash uchun xat yozaman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Tadqiqotni (research) kim bajaradi?</p>"
            ),
            "choices": [
                {"text": "Sara (A)", "is_correct": True},
                {"text": "Ben (B)", "is_correct": False},
                {"text": "Mia (C)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Sara (A).</mark> "
                "Sara: \"I'm happy to do the <u>research</u>.\" Ben tasdiqlaydi: "
                "\"Thanks, Sara — that's the research covered.\" Ism aniq aytildi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Ma'lumot tahlilini (data analysis) kim "
                "oladi?</p>"
            ),
            "choices": [
                {"text": "Sara (A)", "is_correct": False},
                {"text": "Ben (B)", "is_correct": False},
                {"text": "Mia (C)", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Mia (C).</mark> "
                "Mia: \"I could take the <u>data analysis</u>. I did statistics last "
                "year.\" Ben: \"Perfect, Mia.\" Ovoz (ayol, Woman2) + ism (Mia) = "
                "langar.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Slaydlarni (slides) kim tayyorlaydi?</p>"
            ),
            "choices": [
                {"text": "Sara (A)", "is_correct": False},
                {"text": "Ben (B)", "is_correct": True},
                {"text": "Mia (C)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Ben (B).</mark> "
                "Ben: \"I'll make the <u>slides</u> myself, since I've got the design "
                "software.\" O'zi haqida (\"myself\") aytdi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Kirishni (introduction) kim qiladi?</p>"
            ),
            "choices": [
                {"text": "Sara (A)", "is_correct": False},
                {"text": "Ben (B)", "is_correct": True},
                {"text": "Mia (C)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Ben (B).</mark> "
                "Taklif ≠ qabul tuzog'i! Mia taklif qiladi: \"Why don't <u>you</u> do "
                "that too, <u>Ben</u>?\" — lekin bu Mia'ni javob qilmaydi. Ben qabul "
                "qiladi: \"all right — I'll do the introduction as well.\" Vazifa qabul "
                "qilgan odamniki — Ben. (Mia taklif qildi, xolos.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> O'qituvchiga kim xat yozadi (email the "
                "tutor)?</p>"
            ),
            "choices": [
                {"text": "Sara (A)", "is_correct": True},
                {"text": "Ben (B)", "is_correct": False},
                {"text": "Mia (C)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Sara (A).</mark> "
                "Sara: \"And <u>I'll email the tutor</u> afterwards to confirm "
                "everything.\" Oxirgi gap — Sara'niki (Woman ovozi). Har vazifani "
                "\"I'll...\" degan odamga bog'lang.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — zo'r! Ovoz + ism orqali so'zlovchilarni ishonch bilan kuzatasiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3–4/5</strong> — yaxshi; ayniqsa 4-savol (taklif vs qabul) turini qayta tinglang.</p>"
            "<p style=\"margin:0;\"><strong>2/5 yoki kam</strong> — 10–11-darslarga qaytib, ismlarni langar qilish usulini takrorlang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to divide up</div><div class=\"pp-card-back\">bo'lishmoq, taqsimlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to take on a task</div><div class=\"pp-card-back\">vazifani zimmaga olmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">data analysis</div><div class=\"pp-card-back\">ma'lumot tahlili</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to dig through sources</div><div class=\"pp-card-back\">manbalarni titkilamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Why don't you...?</div><div class=\"pp-card-back\">...qilsang-chi? (taklif)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a confident speaker</div><div class=\"pp-card-back\">ishonchli notiq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to confirm</div><div class=\"pp-card-back\">tasdiqlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">as well as</div><div class=\"pp-card-back\">... bilan birga, shuningdek</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Matching = vazifa/fikrni odamga ulash; har odamni ovoz + ism bilan langar qiling.</li>"
            "<li>Taklif ≠ qabul: vazifa uni QABUL qilgan odamniki (\"I'll do it\"), taklif qilganga emas.</li>"
            "<li>\"I'll...\", \"I could take...\", \"myself\" — vazifani egallash signallari.</li>"
            "<li>Ism aniq aytilgan paytlarni (Thanks, Sara / Perfect, Mia) langar sifatida ishlating.</li>"
            "</ul>"
        )},
    ],
},

]
