"""
IELTS Speaking lessons 13-14 (orders 40-41) — the "Talaffuz va ravonlik (Pronunciation
& Fluency Techniques)" topic — fifth Speaking batch, see toc_ielts_speaking.txt.

Each lesson has one model-sentence demo clip (candidate = "Man"). Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_pron_40_41.py \
        --out examprep/management/commands/audio/speaking_pron
then import with --audio-dir. Naming: ielts_s_<order 3-digit>_<block n>.mp3.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_PRON = {
    "title":   "Talaffuz va ravonlik (Pronunciation & Fluency Techniques)",
    "summary": "Tabiiy talaffuz: gap urg'usi va ohang (intonation), hamda tovushlarni "
               "bog'lash (connected speech) — robotik emas, tabiiy gapirish.",
    "icon":    "bi-soundwave",
    "order":   5,
}

_SHADOW = (
    "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
    "<strong>🗣️ Shadowing:</strong> model gap ortidan aynan bir xil urg'u va ohang bilan "
    "takrorlang — 3 kun × 3 marta. Talaffuzni sezilarli yaxshilaydi.</div>"
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 13 (order 40 — sentence stress & intonation) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PRON,
    "title": "IELTS Speaking 13: Sentence Stress and Intonation for Natural-Sounding Answers",
    "summary": "Mazmun so'zlarga urg'u berish (ot/fe'l/sifat), vazifa so'zlarni zaiflashtirish; gap ohangi (ko'tariluvchi/tushuvchi) — monotonlikdan qochish.",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Urg'u va ohang — tabiiy ritm</h2>"
            "<p>Ingliz tili <strong>urg'u-vaqtli (stress-timed)</strong> til: ba'zi "
            "so'zlar kuchli, ba'zilari zaif talaffuz qilinadi. Bu ritmni to'g'ri qilsangiz, "
            "nutqingiz tabiiy va tushunarli eshitiladi — <mark "
            "style=\"background:#dbeafe;\">Pronunciation bandini</mark> ko'taradi.</p>"
        )},
        {"rich_text": (
            "<h3>Qaysi so'zlarga urg'u?</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Urg'uli — mazmun so'zlar:</strong> otlar, asosiy fe'llar, sifatlar, ravishlar, so'roq so'zlar (ma'no tashuvchilar).</p>"
            "<p style=\"margin:0;\"><strong>Urg'usiz (zaif) — vazifa so'zlar:</strong> artikllar (a/the), predloglar (to/of), bog'lovchilar (and), yordamchi fe'llar (is/do).</p>"
            "</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna (KATTA harf = urg'u):</strong><br>"
            "<em>\"I REALly ENJOY LEARNing new LANGuages.\"</em><br>"
            "<span style=\"color:#475569;\">Mazmun so'zlar (really, enjoy, learning, new, "
            "languages) kuchli; \"I\" zaif. Bu tabiiy ritm beradi.</span></div>"
        )},
        {"rich_text": (
            "<h3>Ohang (intonation)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Tushuvchi ohang (↘):</strong> oddiy gaplar va WH-savollar oxirida (\"I live in the city. ↘\", \"Where do you live? ↘\")</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Ko'tariluvchi ohang (↗):</strong> ha/yo'q savollari (\"Do you like it? ↗\")</p>"
            "<p style=\"margin:0;\"><strong>Ro'yxatda:</strong> har element ↗, oxirgisi ↘ (\"apples, ↗ oranges, ↗ and bananas ↘\")</p>"
            "</div>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>🔴 Monotonlikdan qoching:</strong> bir xil, tekis ohangda gapirish "
            "(hamma so'z bir xil balandlikda) — zerikarli va sun'iy eshitiladi, "
            "Pronunciation bandini pasaytiradi. Ohangni o'zgartirib, muhim so'zlarni "
            "ta'kidlang.</div>"
        )},
        {
            "audio":        "ielts_s_040_1.mp3",
            "audio_script": [
                ("Man", "I absolutely love travelling, especially to places with a rich history and delicious food."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model gap.</strong> Mazmun so'zlar (love, travelling, "
                "rich, history, delicious, food) kuchli va ohang tabiiy o'zgaradi. "
                "Tinglang va urg'uni his qiling.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> I absolutely love travelling, especially to places with a rich history and delicious food.<br>"
                "<em style=\"color:#475569;\">Men sayohat qilishni juda yaxshi ko'raman, ayniqsa boy tarixi va mazali taomi bor joylarga.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Gapda odatda qaysi so'zlarga urg'u "
                "beriladi?</p>"
            ),
            "choices": [
                {"text": "Artikllar va predloglar (a, the, to, of)", "is_correct": False},
                {"text": "Mazmun so'zlar: otlar, asosiy fe'llar, sifatlar", "is_correct": True},
                {"text": "Har bir so'zga teng urg'u", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: mazmun so'zlar.</mark> "
                "Ma'no tashuvchi so'zlar (ot, fe'l, sifat) urg'uli; vazifa so'zlar "
                "(a/the/to/of) zaif. Har so'zga teng urg'u berish — robotik, sun'iy "
                "ritm. To'g'ri urg'u tabiiy va tushunarli nutq beradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Oddiy tasdiq gap (\"I live in Tashkent\") "
                "oxirida qaysi ohang tabiiy?</p>"
            ),
            "choices": [
                {"text": "Ko'tariluvchi (↗)", "is_correct": False},
                {"text": "Tushuvchi (↘)", "is_correct": True},
                {"text": "Tekis (o'zgarmas)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: tushuvchi (↘).</mark> "
                "Oddiy tasdiq gaplar va WH-savollar tushuvchi ohang bilan tugaydi — bu "
                "tabiiy va yakuniy his beradi. Ko'tariluvchi ohang ha/yo'q savollari "
                "uchun. Tekis ohang — monoton, sun'iy.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit — Stress &amp; intonation</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">sentence stress</div><div class=\"pp-card-back\">gap urg'usi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">content words</div><div class=\"pp-card-back\">mazmun so'zlar (urg'uli)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">function words</div><div class=\"pp-card-back\">vazifa so'zlar (zaif)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">intonation</div><div class=\"pp-card-back\">ohang</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">rising / falling tone</div><div class=\"pp-card-back\">ko'tariluvchi / tushuvchi ohang</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">monotone</div><div class=\"pp-card-back\">monoton, bir xil ohang (yomon)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">stress-timed</div><div class=\"pp-card-back\">urg'u-vaqtli (ingliz tili ritmi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to emphasise a word</div><div class=\"pp-card-back\">so'zni ta'kidlamoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Mazmun so'zlarga urg'u bering (ot/fe'l/sifat); vazifa so'zlarni zaiflashtiring.</li>"
            "<li>Tasdiq va WH-savol — tushuvchi ohang; ha/yo'q savol — ko'tariluvchi.</li>"
            "<li>Monoton (tekis) ohangdan qoching — muhim so'zlarni ta'kidlang.</li>"
            "<li>Bu ingliz tilining tabiiy ritmini beradi (stress-timed).</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 14 (order 41 — connected speech / linking) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PRON,
    "title": "IELTS Speaking 14: Linking Sounds and Connected Speech Basics",
    "summary": "Tovushlarni bog'lash: undosh→unli ulanishi (an_apple), zaif shakllar (to→/tə/, and→/ən/); so'zlarni robotik ajratmasdan, tabiiy oqim bilan gapirish.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>Connected speech — so'zlarni bog'lash</h2>"
            "<p>Ona tilida so'zlovchilar so'zlarni <u>alohida</u> emas, "
            "<strong>bog'lab</strong> talaffuz qiladi — tovushlar bir-biriga oqib o'tadi. "
            "So'zlarni robotik ravishda birma-bir aytish sun'iy eshitiladi. Bog'lashni "
            "o'rgansangiz, nutqingiz <mark style=\"background:#dbeafe;\">ravon va "
            "tabiiy</mark> chiqadi.</p>"
        )},
        {"rich_text": (
            "<h3>Asosiy bog'lash turlari</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>1. Undosh → unli (linking):</strong> so'z undosh bilan tugab, keyingisi unli bilan boshlansa, ular ulanadi. <em>\"an apple\"</em> → \"a-napple\"; <em>\"pick it up\"</em> → \"picki-tup\".</p>"
            "<p style=\"margin:0 0 6px;\"><strong>2. Zaif shakllar (weak forms):</strong> kichik so'zlar zaiflashadi: <em>to</em> → /tə/, <em>and</em> → /ən/, <em>of</em> → /əv/, <em>for</em> → /fə/.</p>"
            "<p style=\"margin:0;\"><strong>3. Bir xil tovush qo'shilishi:</strong> <em>\"want to\"</em> → \"wanna\" (norasmiy), <em>\"next time\"</em> — birinchi \"t\" deyarli yo'qoladi.</p>"
            "</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna:</strong> <em>\"I'd like to talk about an old friend of "
            "mine.\"</em><br>"
            "<span style=\"color:#475569;\">Bog'lanadi: like-to (/tə/), about-an, "
            "old-friend, friend-of (/əv/). Tabiiy oqim.</span></div>"
        )},
        {
            "audio":        "ielts_s_041_1.mp3",
            "audio_script": [
                ("Man", "I'd like to talk about an old friend of mine, and how we first met at university."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model gap.</strong> So'zlar bog'lanishiga quloq soling: "
                "<em>like to, about an, old friend, friend of</em> — tabiiy oqim, robotik "
                "emas.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> I'd like to talk about an old friend of mine, and how we first met at university.<br>"
                "<em style=\"color:#475569;\">Eski bir do'stim va biz universitetda qanday birinchi marta uchrashganimiz haqida gapirmoqchiman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> \"an apple\" iborasi tabiiy nutqda qanday "
                "talaffuz qilinadi?</p>"
            ),
            "choices": [
                {"text": "\"an ... apple\" (ikki so'z alohida, to'xtash bilan)", "is_correct": False},
                {"text": "\"a-napple\" (undosh N unliga ulanadi)", "is_correct": True},
                {"text": "\"an ah-pple\" (har harf alohida)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"a-napple\".</mark> "
                "\"an\" oxiridagi /n/ tovushi keyingi so'zning unlisiga (\"apple\") "
                "ulanadi — undosh→unli bog'lanishi. Bu tabiiy oqim beradi. So'zlarni "
                "to'xtab-to'xtab aytish robotik eshitiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Tabiiy nutqda \"to\" so'zi (\"I want to "
                "go\") qanday talaffuz qilinadi?</p>"
            ),
            "choices": [
                {"text": "Har doim to'liq va kuchli /tuː/", "is_correct": False},
                {"text": "Zaif shakl /tə/ (schwa bilan)", "is_correct": True},
                {"text": "Umuman aytilmaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: zaif /tə/.</mark> "
                "\"to\", \"and\", \"of\" kabi vazifa so'zlar tabiiy nutqda zaiflashadi "
                "(schwa /ə/ tovushi bilan). Ularni har doim to'liq talaffuz qilish "
                "nutqni sun'iy va sekin qiladi. Zaif shakllar tabiiy ritm beradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit — Connected speech</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">connected speech</div><div class=\"pp-card-back\">bog'langan nutq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">linking (consonant→vowel)</div><div class=\"pp-card-back\">bog'lash (undosh→unli)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a weak form</div><div class=\"pp-card-back\">zaif shakl (to→/tə/)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a schwa /ə/</div><div class=\"pp-card-back\">schwa — eng ko'p uchraydigan zaif unli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to flow / to run together</div><div class=\"pp-card-back\">oqib o'tmoq / qo'shilib ketmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">robotic / choppy speech</div><div class=\"pp-card-back\">robotik / uzuq-yuluq nutq (yomon)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">natural rhythm</div><div class=\"pp-card-back\">tabiiy ritm</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to slur (words together)</div><div class=\"pp-card-back\">(so'zlarni) qo'shib talaffuz qilmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ona tili so'zlovchilar so'zlarni bog'laydi — robotik ajratib aytmang.</li>"
            "<li>Undosh→unli ulanadi (an_apple, pick_it_up).</li>"
            "<li>Vazifa so'zlar zaiflashadi: to→/tə/, and→/ən/, of→/əv/.</li>"
            "<li>Shadowing — bog'lashni o'rganishning eng yaxshi usuli.</li>"
            "</ul>"
        )},
    ],
},

]
