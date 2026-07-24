"""
IELTS Speaking lessons 15-16 (orders 50-51) — the "Kartochka mavzular banki (Common
Cue Card Topics Bank)" topic — sixth (final) Speaking batch, see toc_ielts_speaking.txt.
Lesson 16 is the CAPSTONE that finishes the WHOLE IELTS course (all 4 skills).

Each lesson has one ~2-min model monologue clip (candidate = "Man") + a bank of cue cards
with idea prompts. Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_bank_50_51.py \
        --out examprep/management/commands/audio/speaking_bank
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

TOPIC_BANK = {
    "title":   "Kartochka mavzular banki (Common Cue Card Topics Bank)",
    "summary": "Eng ko'p uchraydigan Part 2 kartochka mavzulari — tez amaliyot: g'oya "
               "prompti, tuzilma va namunaviy javob.",
    "icon":    "bi-collection",
    "order":   6,
}

_SHADOW = (
    "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
    "<strong>🗣️ Shadowing:</strong> model javob ortidan takrorlang, keyin O'ZINGIZNI "
    "yozib model bilan solishtiring — 3 kun × 3 marta.</div>"
)


def cue_card(title, bullets):
    items = "".join(f"<li>{b}</li>" for b in bullets)
    return (
        "<div style=\"background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:14px 16px;margin:12px 0;\">"
        f"<p style=\"margin:0 0 6px;font-weight:700;\">🃏 {title}</p>"
        "<p style=\"margin:0 0 4px;\">You should say:</p>"
        f"<ul style=\"margin:0;\">{items}</ul>"
        "</div>"
    )


LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 15 (order 50 — rapid-fire round 1) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_BANK,
    "title": "IELTS Speaking 15: High-Frequency Cue Card Topics — Rapid-Fire Round 1",
    "summary": "Eng ko'p uchraydigan kartochkalar (shaxs, joy, ko'nikma, ovqat) + g'oya promptlari; bitta mavzuni tanlab, tuzilma bilan tez rivojlantirish.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>Tez amaliyot — kartochka banki</h2>"
            "<p>Part 2 kartochkalari cheksiz ko'rinsa-da, ular <strong>bir necha "
            "toifaga</strong> bo'linadi: shaxs, joy, buyum, voqea, tajriba, mavhum "
            "tushuncha. Bir necha kuchli mavzuni oldindan tayyorlang — ko'p kartochkalarni "
            "o'sha tayyor materialga <mark style=\"background:#dbeafe;\">moslashtirasiz</mark>.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Tez g'oya topish:</strong> mavzu berilganda, o'zingiz "
            "<u>ko'p gapira oladigan</u> aniq misolni tanlang — mukammalligini emas, "
            "gapirish osonligini o'ylang. Keyin bulletlarni tuzilma sifatida ishlating.</div>"
        )},
        {"rich_text": (
            "<h3>Kartochka banki — Round 1</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 4 ta kartochka + g'oya prompti — bosing</summary>"
            "<div style=\"margin-top:10px;\">"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe a person you admire.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: ota-ona / o'qituvchi / mashhur shaxs → who, why admire (sifatlar), a specific example, how they inspire you.</em></p>"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe a place you would like to visit.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: Yaponiya / tog'lar → where, why, what you'd do there, why it appeals to you.</em></p>"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe a skill you would like to learn.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: piano / driving / a language → what, why, how you'd learn it, why it appeals.</em></p>"
            "<p style=\"margin:0;\"><strong>🃏 Describe a memorable meal you have had.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: family celebration → what, where, who with, why memorable.</em></p>"
            "</div></details>"
        )},
        {"rich_text": (
            "<h3>Model javob — \"a skill you would like to learn\"</h3>"
            + cue_card("Describe a skill you would like to learn.",
                       ["what the skill is",
                        "why you want to learn it",
                        "how you would learn it",
                        "and explain why it appeals to you"])
        )},
        {
            "audio":        "ielts_s_050_1.mp3",
            "audio_script": [
                ("Man", "A skill I'd really love to learn is playing the piano. I've always been drawn to music, but I never had the chance to learn an instrument as a child. If I had more time, I'd take proper lessons, because I think being able to sit down and play a piece of music must be incredibly relaxing and rewarding. I'd probably start with simple songs and build up gradually, maybe with an app or a private teacher. The main reason it appeals to me is that, unlike my day-to-day work, it's something creative that I could do purely for enjoyment, with no pressure at all. There's also something quite magical about turning a page of symbols into actual music. Hopefully, one day I'll finally get round to it."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob (~2 daqiqa).</strong> Shart gap (\"If I had "
                "time, I'd...\"), sabab va his-tuyg'u bilan kengaytirilgan.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> A skill I'd really love to learn is playing the piano... Hopefully, one day I'll finally get round to it.<br>"
                "<em style=\"color:#475569;\">Men chindan ham o'rganishni istagan ko'nikma — pianino chalish. Men doim musiqaga qiziqqanman, lekin bolaligimda cholg'u o'rganishga imkonim bo'lmagan. Vaqtim ko'proq bo'lsa, tuzukroq darslar olardim, chunki o'tirib biror musiqa asarini chala olish nihoyatda tinchlantiruvchi va zavqli bo'lsa kerak deb o'ylayman. Ehtimol, oddiy qo'shiqlardan boshlab, asta-sekin, ilova yoki xususiy o'qituvchi bilan rivojlantirardim. Meni eng ko'p o'ziga tortadigan sabab — kundalik ishimdan farqli o'laroq, bu ijodiy narsa bo'lib, uni faqat zavq uchun, hech qanday bosimsiz qila olardim. Bir varaq belgilarni haqiqiy musiqaga aylantirishning o'zida ham sehrli nimadir bor. Umid qilamanki, bir kun kelib nihoyat unga qo'l uraman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Kartochka berilganda mavzuni qanday tez "
                "tanlash kerak?</p>"
            ),
            "choices": [
                {"text": "Eng \"ta'sirchan\" yoki g'ayrioddiy mavzuni izlash", "is_correct": False},
                {"text": "O'zingiz ko'p gapira oladigan aniq misolni tanlash (mukammal emas)", "is_correct": True},
                {"text": "Har doim birinchi xayolga kelganini rad etish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ko'p gapira "
                "oladigan misol.</mark> IELTS mavzuni emas, TILNI baholaydi. \"Ta'sirchan\" "
                "lekin gapirish qiyin mavzudan ko'ra, oddiy lekin siz haqida ko'p aytadigan "
                "mavzu ancha yaxshi. Tez tanlab, gapirishga vaqt qoldiring.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Cue card fluency</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I've always been drawn to ...</div><div class=\"pp-card-back\">Men doim ... ga qiziqqanman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">If I had time, I'd ...</div><div class=\"pp-card-back\">Vaqtim bo'lsa, ... qilardim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to build up gradually</div><div class=\"pp-card-back\">asta-sekin rivojlantirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">what appeals to me is ...</div><div class=\"pp-card-back\">meni o'ziga tortadigani ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">purely for enjoyment</div><div class=\"pp-card-back\">faqat zavq uchun</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to get round to (doing) sth</div><div class=\"pp-card-back\">nihoyat biror ishga qo'l urmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">someone I really look up to</div><div class=\"pp-card-back\">men chindan hurmat qiladigan kishi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a once-in-a-lifetime experience</div><div class=\"pp-card-back\">umrda bir marta bo'ladigan tajriba</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Kartochkalar toifalarga bo'linadi — bir necha kuchli mavzuni oldindan tayyorlang.</li>"
            "<li>Tez tanlang: ko'p gapira oladigan misol, mukammal emas.</li>"
            "<li>Bulletlarni tuzilma qiling; shart gap va his-tuyg'u bilan kengaytiring.</li>"
            "<li>Bank kartochkalarni mashq qiling — takror ravonlikni oshiradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 16 (order 51 — rapid-fire round 2) — AUDIO — COURSE FINALE
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_BANK,
    "title": "IELTS Speaking 16: High-Frequency Cue Card Topics — Rapid-Fire Round 2",
    "summary": "Yana kartochkalar (qaror, texnologiya, kasb, yordam) + namunaviy javob. Bu — butun IELTS kursining yakuniy darsi!",
    "order": 51,
    "blocks": [
        {"rich_text": (
            "<h2>Tez amaliyot — Round 2</h2>"
            "<p>Yana bir to'plam yuqori chastotali kartochkalar. Round 1'dagi usulni "
            "eslang: tez tanlang, bulletlarni tuzilma qiling, shart gap va his-tuyg'u "
            "bilan kengaytiring, to'liq 2 daqiqa gapiring.</p>"
        )},
        {"rich_text": (
            "<h3>Kartochka banki — Round 2</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 4 ta kartochka + g'oya prompti — bosing</summary>"
            "<div style=\"margin-top:10px;\">"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe an important decision you made.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: choosing a course / moving city → what, when, how you decided, the outcome.</em></p>"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe a piece of technology you couldn't live without.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: smartphone / laptop → what, what you use it for, why essential, any downsides.</em></p>"
            "<p style=\"margin:0 0 8px;\"><strong>🃏 Describe a person who is good at their job.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: a doctor / a teacher → who, their job, what makes them good, an example.</em></p>"
            "<p style=\"margin:0;\"><strong>🃏 Describe a time you helped someone.</strong><br>"
            "<em style=\"color:#475569;\">G'oya: helped a friend/stranger → when, who, what you did, how you felt.</em></p>"
            "</div></details>"
        )},
        {"rich_text": (
            "<h3>Model javob — \"technology you couldn't live without\"</h3>"
            + cue_card("Describe a piece of technology you couldn't live without.",
                       ["what it is",
                        "what you use it for",
                        "how often you use it",
                        "and explain why you couldn't live without it"])
        )},
        {
            "audio":        "ielts_s_051_1.mp3",
            "audio_script": [
                ("Man", "The piece of technology I couldn't live without is, without a doubt, my smartphone. It might sound a bit clichéd, but honestly, it does almost everything for me. I use it as my alarm, my camera, my map, and my main way of keeping in touch with friends and family, so I'm on it throughout the day. What I value most, though, is having instant access to information. If I'm curious about something or I need directions, the answer is right there in my pocket. Of course, I'm well aware there's a downside, and I do try to put it away in the evenings. But all things considered, it's become such a central part of daily life that I genuinely can't imagine going back to how things were before smartphones existed."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob (~2 daqiqa).</strong> Balanslangan: foydalar + "
                "kamchilikni tan olish (\"there's a downside\"). Tabiiy iboralar: "
                "<em>clichéd, all things considered</em>.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> The piece of technology I couldn't live without is, without a doubt, my smartphone... I genuinely can't imagine going back to how things were before smartphones existed.<br>"
                "<em style=\"color:#475569;\">Men usiz yashay olmaydigan texnologiya, shubhasiz, smartfonim. Bu biroz siyqasi chiqqandek tuyulishi mumkin, lekin rostini aytsam, u men uchun deyarli hamma narsani qiladi. Uni budilnik, kamera, xarita va do'stlar hamda oila bilan aloqa qilishning asosiy vositasi sifatida ishlataman, shuning uchun kun bo'yi undaman. Lekin men eng qadrlaydigan narsa — ma'lumotga darhol kirish imkoni. Agar biror narsaga qiziqsam yoki yo'l kerak bo'lsa, javob cho'ntagimda. Albatta, kamchiligi borligini yaxshi bilaman va kechqurunlari uni chetga qo'yishga harakat qilaman. Lekin hammasini hisobga olganda, u kundalik hayotning shunchalik markaziy qismiga aylanganki, smartfonlar paydo bo'lishidan oldingi holatga qaytishni tasavvur ham qila olmayman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Model javob \"technology\" mavzusini "
                "qanday muvozanatli qildi?</p>"
            ),
            "choices": [
                {"text": "Faqat ijobiy tomonlarni sanab", "is_correct": False},
                {"text": "Foydalarni aytib, keyin kamchilikni ham tan olib (\"there's a downside\")", "is_correct": True},
                {"text": "Mavzudan chetga chiqib", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kamchilikni ham tan "
                "olib.</mark> Bir tomonni ham qisqa tan olish (\"there's a downside... I "
                "try to put it away\") javobni nozik va o'ylangan qiladi — bu Lexical va "
                "Coherence'ni ko'taradi. \"all things considered\" bilan yakuniy fikrga "
                "qaytadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Butun kurs bo'yicha — IELTS Speaking'da "
                "eng muhim umumiy tamoyil qaysi?</p>"
            ),
            "choices": [
                {"text": "Iloji boricha tez va murakkab gapirish", "is_correct": False},
                {"text": "Javoblarni kengaytirish (sabab + misol), tabiiy va ravon gapirish — bu suhbat", "is_correct": True},
                {"text": "Javoblarni yodlab olish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kengaytirish + "
                "tabiiylik.</mark> Butun kurs bo'yicha asosiy g'oya: javoblarni sabab va "
                "misol bilan kengaytiring, tabiiy va ravon gapiring, bu suhbat ekanini "
                "unutmang. Tezlik va yodlash yordam bermaydi — jonli, asoslangan javob "
                "eng yaxshisi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Round 2</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">without a doubt</div><div class=\"pp-card-back\">shubhasiz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it might sound clichéd, but ...</div><div class=\"pp-card-back\">siyqasi chiqqandek tuyular, lekin ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to keep in touch with</div><div class=\"pp-card-back\">... bilan aloqada bo'lmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">instant access to ...</div><div class=\"pp-card-back\">... ga darhol kirish imkoni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">all things considered</div><div class=\"pp-card-back\">hammasini hisobga olganda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to make a tough decision</div><div class=\"pp-card-back\">og'ir qaror qabul qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to go the extra mile</div><div class=\"pp-card-back\">qo'shimcha harakat qilmoq (kasb)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it felt really rewarding</div><div class=\"pp-card-back\">bu chindan qoniqarli tuyuldi</div></div>"
            "</div>"
            "<h2>🎉 Tabriklaymiz — BUTUN IELTS kursini tugatdingiz!</h2>"
            "<p>Bu — nafaqat Speaking, balki <strong>butun IELTS kursining so'nggi "
            "darsi</strong>! Siz to'rt ko'nikmani ham to'liq o'rgandingiz:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\">📖 <strong>Reading</strong> — barcha savol turlari (T/F/NG dan Diagram Label gacha)</p>"
            "<p style=\"margin:0 0 4px;\">🎧 <strong>Listening</strong> — 4 bo'lim, forma, xarita, munozara, ma'ruza</p>"
            "<p style=\"margin:0 0 4px;\">✍️ <strong>Writing</strong> — Task 1 (grafik/jarayon/xarita) va Task 2 (barcha insho turlari)</p>"
            "<p style=\"margin:0;\">🎤 <strong>Speaking</strong> — 3 qism, strategiya, talaffuz va kartochka banki</p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Keyingi qadam:</strong> bilim — poydevor, band esa MASHQ bilan "
            "ko'tariladi. Har hafta har bir ko'nikmadan amaliyot qiling: to'liq test "
            "yeching, model javoblar bilan solishtiring, shadowing qiling va shaxsiy xato "
            "ro'yxatingizni yuriting. Har xato — keyingi safar uchun dars. "
            "Siz tayyorsiz. Omad, Band 7+! 🚀</p>"
            "<h3>Speaking — butun bo'lim bir jumlada</h3>"
            "<ul>"
            "<li>Bu suhbat — TIL baholanadi, fikr emas; yodlangan javoblardan qoching.</li>"
            "<li>Part 1: javob + bitta detal. Part 2: 1 daqiqa eslatma + 2 daqiqa nutq. Part 3: kengaytiring (sabab + misol).</li>"
            "<li>Talaffuz: mazmun so'zlarga urg'u, so'zlarni bog'lang, monotonlikdan qoching.</li>"
            "<li>Ravonlik = oqim; tabiiy fillerlar va shadowing bilan mashq qiling.</li>"
            "</ul>"
        )},
    ],
},

]
