"""
IELTS Speaking lessons 10-12 (orders 30-32) — the "3-qism: Chuqur muhokama (Part 3 —
Discussion)" topic — fourth Speaking batch, see toc_ielts_speaking.txt.

Each lesson has one Q+A demo clip: examiner = "Woman", model candidate answer = "Man".
Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_part3_30_32.py \
        --out examprep/management/commands/audio/speaking_part3
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

TOPIC_PART3 = {
    "title":   "3-qism: Chuqur muhokama (Part 3 — Discussion)",
    "summary": "Part 3: mavhum/ijtimoiy savollar; javobni sabab, misol va boshqa qarash "
               "bilan kengaytirish, o'tmish/hozirni solishtirish, fikrni yumshatish.",
    "icon":    "bi-chat-dots",
    "order":   4,
}

_SHADOW = (
    "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
    "<strong>🗣️ Shadowing:</strong> model javob ortidan bir xil ohang bilan takrorlang — "
    "3 kun × 3 marta. Keyin savolga o'z javobingizni yozib, model bilan solishtiring.</div>"
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 10 (order 30 — Part 3 format: extending answers) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART3,
    "title": "IELTS Speaking 10: Part 3 Format — Extending Answers With Reasons and Examples",
    "summary": "Part 3: mavhum/ijtimoiy savollar; javobni fikr + sabab + misol + boshqa qarash bilan kengaytirish (Part 1'dan uzunroq va chuqurroq).",
    "order": 30,
    "blocks": [
        {"rich_text": (
            "<h2>Part 3 — chuqur muhokama</h2>"
            "<p>3-qism ~4–5 daqiqa va Part 2 mavzusiga bog'liq <strong>mavhum, ijtimoiy "
            "savollar</strong>dan iborat (shaxsiy emas — umumiy). Imtihonchi sizning "
            "<u>muhokama qilish, solishtirish, taxmin qilish va fikrni asoslash</u> "
            "qobiliyatingizni sinaydi. Javoblar <mark style=\"background:#dbeafe;\">Part "
            "1'dan uzunroq</mark> va chuqurroq bo'lishi kerak.</p>"
        )},
        {"rich_text": (
            "<h3>Javobni kengaytirish formulasi</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>1. Fikr (Point):</strong> \"Well, I think ...\" / \"In my view, ...\"</p>"
            "<p style=\"margin:0 0 6px;\"><strong>2. Sabab (Reason):</strong> \"The main reason is that ...\" / \"This is because ...\"</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3. Misol (Example):</strong> \"For example, ...\" / \"A good example would be ...\"</p>"
            "<p style=\"margin:0;\"><strong>4. Boshqa qarash (opsional):</strong> \"That said, some people would argue ...\" / \"On the other hand, ...\"</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> faqat fikr aytib to'xtamang (\"Yes, it's "
            "important.\") — bu Part 3 uchun juda qisqa. Har doim <u>sabab + misol</u> "
            "qo'shing. Boshqa tomonni ham eslatish (\"That said...\") javobni yanada "
            "kuchli qiladi.</div>"
        )},
        {
            "audio":        "ielts_s_030_1.mp3",
            "audio_script": [
                ("Woman", "Do you think reading books is still important in the age of the internet?"),
                ("Man",   "Yes, I'd say it's more important than ever, actually. The main reason is that reading a full book trains you to concentrate deeply, which is a skill that's becoming rarer as people get used to scrolling quickly through short posts. For example, sitting with a long novel forces you to follow a complex story over many hours, and I think that kind of sustained focus is genuinely valuable. That said, I suppose some people would argue that you can get information much faster online, and to some extent that's true. But for real understanding, I still think books are hard to beat."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob.</strong> Tuzilmani ilg'ang: fikr → sabab → "
                "misol → boshqa qarash → fikrga qaytish.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Do you think reading books is still important in the age of the internet?<br>"
                "<em style=\"color:#475569;\">Internet asrida kitob o'qish hali ham muhimmi deb o'ylaysizmi?</em></p>"
                "<p><strong>Candidate:</strong> Yes, I'd say it's more important than ever... for real understanding, I still think books are hard to beat.<br>"
                "<em style=\"color:#475569;\">Ha, aslida u har qachongidan ham muhimroq desam bo'ladi. Asosiy sabab — to'liq kitob o'qish sizni chuqur diqqatni jamlashga o'rgatadi, bu esa odamlar qisqa postlarni tez varaqlashga o'rganib borgani sari kamayib borayotgan mahorat. Masalan, uzun roman bilan o'tirish sizni murakkab syujetni soatlab kuzatishga majbur qiladi va menimcha, bunday barqaror diqqat chindan ham qadrli. Shunga qaramay, ba'zilar internetdan ma'lumotni ancha tez olish mumkin deb aytadi va ma'lum darajada bu to'g'ri. Lekin haqiqiy tushunish uchun kitoblarni yengish qiyin deb o'ylayman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Part 3 javoblari Part 1'dan qanday farq "
                "qiladi?</p>"
            ),
            "choices": [
                {"text": "Qisqaroq va soddaroq bo'lishi kerak", "is_correct": False},
                {"text": "Uzunroq va chuqurroq — sabab, misol va boshqa qarash bilan kengaytirilgan", "is_correct": True},
                {"text": "Faqat \"ha/yo'q\" javob yetarli", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: uzunroq va "
                "chuqurroq.</mark> Part 3 muhokama — mavhum savollarni asoslash, "
                "solishtirish, taxmin qilish. Har javobni fikr + sabab + misol (+ boshqa "
                "qarash) bilan kengaytiring. Qisqa \"ha/yo'q\" Fluency va Coherence'ni "
                "pasaytiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"That said, some people would argue...\" "
                "iborasi javobga nima qo'shadi?</p>"
            ),
            "choices": [
                {"text": "Hech narsa — chalg'itadi", "is_correct": False},
                {"text": "Boshqa qarashni tan olib, javobni muvozanatli va kuchliroq qiladi", "is_correct": True},
                {"text": "Mavzuni o'zgartiradi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: muvozanatli va "
                "kuchliroq.</mark> Boshqa tomonni qisqa tan olish (\"That said...\", "
                "\"On the other hand...\") sizning tanqidiy fikrlashingizni ko'rsatadi — "
                "bu Part 3'da yuqori baholanadi. Keyin o'z fikringizga qaytasiz.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Extending answers</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">The main reason is that ...</div><div class=\"pp-card-back\">Asosiy sabab shuki, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">A good example would be ...</div><div class=\"pp-card-back\">Yaxshi misol ... bo'lardi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">That said, ...</div><div class=\"pp-card-back\">Shunga qaramay, ... (boshqa qarash)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to some extent</div><div class=\"pp-card-back\">ma'lum darajada</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">more ... than ever</div><div class=\"pp-card-back\">har qachongidan ko'proq ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">hard to beat</div><div class=\"pp-card-back\">yengish/ustidan chiqish qiyin</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">sustained focus</div><div class=\"pp-card-back\">barqaror diqqat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">In my view, ...</div><div class=\"pp-card-back\">Mening nazarimda, ...</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Part 3 — mavhum/ijtimoiy savollar; javoblar Part 1'dan uzunroq, chuqurroq.</li>"
            "<li>Formula: fikr + sabab + misol (+ boshqa qarash).</li>"
            "<li>Faqat fikr aytib to'xtamang — har doim asoslang.</li>"
            "<li>\"That said...\" boshqa tomonni tan olib, javobni kuchaytiradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 11 (order 31 — comparing past and present) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART3,
    "title": "IELTS Speaking 11: Comparing Past and Present — Sample Answers",
    "summary": "Part 3'da keng tarqalgan mavzu: o'tmish va hozirni solishtirish; til (used to, tend to, back then, these days, whereas) va muvozanatli baho.",
    "order": 31,
    "blocks": [
        {"rich_text": (
            "<h2>O'tmish va hozirni solishtirish</h2>"
            "<p>Part 3'da tez-tez shunday savollar bo'ladi: <em>\"How has X changed?\"</em> "
            "yoki <em>\"Was X better in the past?\"</em>. Bunda kalit — <strong>o'tmish "
            "va hozirni aniq solishtirish tili</strong> va (ko'pincha) ikki tomonni ham "
            "ko'rsatuvchi muvozanatli baho.</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>O'tmish:</strong> back then, in the past, people used to ..., years ago</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Hozir:</strong> these days, nowadays, people tend to ..., currently</p>"
            "<p style=\"margin:0;\"><strong>Solishtirish:</strong> whereas, compared to, unlike in the past, on the other hand</p>"
            "</div>"
        )},
        {
            "audio":        "ielts_s_031_1.mp3",
            "audio_script": [
                ("Woman", "How has the way people communicate changed over the past few decades?"),
                ("Man",   "It's changed enormously, I'd say. Back then, people mostly relied on letters and landline phones, so communication was slower and, in a way, more deliberate. These days, of course, we tend to message each other instantly through our phones, whatever the time or distance. On the plus side, this means families who live far apart can stay in touch much more easily than they used to. On the other hand, though, I think face-to-face conversation has suffered a little, because people are often glued to their screens even when they're sitting together. So it's really a mixed picture compared to the past."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob.</strong> Solishtirish tiliga e'tibor: "
                "<em>back then / these days / used to / tend to / compared to</em>, va "
                "muvozanat (on the plus side / on the other hand).</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> How has the way people communicate changed over the past few decades?<br>"
                "<em style=\"color:#475569;\">So'nggi o'n yilliklarda odamlarning muloqot qilish usuli qanday o'zgardi?</em></p>"
                "<p><strong>Candidate:</strong> It's changed enormously, I'd say... So it's really a mixed picture compared to the past.<br>"
                "<em style=\"color:#475569;\">Menimcha, u juda ko'p o'zgardi. O'sha paytda odamlar asosan xat va statsionar telefonlarga tayanardi, shuning uchun muloqot sekinroq va, o'ziga xos tarzda, o'ylab qilinardi. Hozir, albatta, biz vaqt yoki masofadan qat'i nazar, telefonlar orqali bir-birimizga darhol xabar yozamiz. Ijobiy tomoni — uzoqda yashaydigan oilalar avvalgidan ancha oson aloqada bo'la oladi. Boshqa tomondan esa, yuzma-yuz muloqot biroz zarar ko'rdi deb o'ylayman, chunki odamlar birga o'tirganda ham ko'pincha ekranga tikilib qoladi. Shuning uchun o'tmish bilan solishtirganda bu chindan ham aralash manzara.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> O'tmishdagi odatlarni tasvirlash uchun "
                "qaysi tuzilma mos?</p>"
            ),
            "choices": [
                {"text": "people used to ... / back then", "is_correct": True},
                {"text": "people will ... / tomorrow", "is_correct": False},
                {"text": "people are ... / right now", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: used to / back "
                "then.</mark> \"People <u>used to</u> rely on letters\", \"<u>back "
                "then</u>...\" — o'tmishdagi odat va holatni aniq ifodalaydi. Hozir uchun "
                "\"these days / tend to\". Bu aniq zamon tili Grammatical Range'ni "
                "ko'rsatadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> \"How has X changed?\" savoliga eng "
                "kuchli javob qanday bo'ladi?</p>"
            ),
            "choices": [
                {"text": "Faqat hozirgi holatni aytish", "is_correct": False},
                {"text": "O'tmish va hozirni aniq solishtirib, ijobiy va salbiy tomonni ko'rsatish", "is_correct": True},
                {"text": "\"It changed a lot\" deb qisqa", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: solishtirib, ikki "
                "tomonni ko'rsatish.</mark> Kuchli javob o'tmish va hozirni yonma-yon "
                "qo'yadi (\"back then... these days...\") va muvozanatli baho beradi "
                "(\"on the plus side... on the other hand...\"). Bu Coherence va Lexical "
                "Resource'ni birga ko'taradi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Past vs present</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">back then / in the past</div><div class=\"pp-card-back\">o'sha paytda / o'tmishda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">these days / nowadays</div><div class=\"pp-card-back\">hozirgi kunda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">people used to ...</div><div class=\"pp-card-back\">odamlar ... qilishardi (o'tmish odati)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">people tend to ...</div><div class=\"pp-card-back\">odamlar odatda ... qiladi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">whereas / compared to</div><div class=\"pp-card-back\">holbuki / ... ga nisbatan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on the plus side</div><div class=\"pp-card-back\">ijobiy tomoni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a mixed picture</div><div class=\"pp-card-back\">aralash manzara</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">glued to their screens</div><div class=\"pp-card-back\">ekranga mixlanib qolgan</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>\"How has X changed?\" — o'tmish va hozirni aniq solishtiring.</li>"
            "<li>Til: used to / back then (o'tmish); tend to / these days (hozir); whereas / compared to.</li>"
            "<li>Ikki tomonni ko'rsating: on the plus side / on the other hand.</li>"
            "<li>Muvozanatli baho (\"a mixed picture\") bilan yakunlang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 12 (order 32 — abstract/society opinions) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART3,
    "title": "IELTS Speaking 12: Giving Opinions on Abstract/Society Questions — Sample Answers",
    "summary": "Mavhum/ijtimoiy savollar: fikrni yumshatish (it depends, to some extent, arguably) va taxmin (might, could, if... would); muvozanatli, ehtiyotkor javob.",
    "order": 32,
    "blocks": [
        {"rich_text": (
            "<h2>Mavhum va ijtimoiy savollar</h2>"
            "<p>Part 3'ning eng qiyin savollari mavhum yoki taxminiy bo'ladi: "
            "<em>\"Should governments ...?\"</em>, <em>\"What are the benefits of ...?\"</em>, "
            "<em>\"Will X change in the future?\"</em>. Bunda ikki mahorat kerak: "
            "<strong>fikrni yumshatish (hedging)</strong> va <strong>taxmin qilish "
            "(speculation)</strong> — mutlaq emas, ehtiyotkor va o'ylangan javob.</p>"
        )},
        {"rich_text": (
            "<h3>Hedging va speculation tili</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Yumshatish (hedging):</strong> it depends, to some extent, arguably, I suppose, on the whole, generally speaking</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Taxmin (speculation):</strong> it might/could ..., it's likely to ..., I suspect ...</p>"
            "<p style=\"margin:0;\"><strong>Shart gap:</strong> \"If governments invested more, fewer people would ...\"</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Nega yumshatish?</strong> Mavhum savollarga mutlaq javob "
            "(\"Yes, always\") ko'pincha soddaroq eshitiladi. \"It depends... on the "
            "whole, I'd argue...\" kabi ehtiyotkor, nozik javob band 7+ ni ko'rsatadi va "
            "grammatik xilma-xillik (shart gaplar, modal fe'llar) beradi.</div>"
        )},
        {
            "audio":        "ielts_s_032_1.mp3",
            "audio_script": [
                ("Woman", "Do you think governments should invest more in public transport?"),
                ("Man",   "Well, it depends to some extent on the country, but on the whole, yes, I'd argue they should. If governments invested more in reliable buses and trains, fewer people would feel the need to drive, which could significantly reduce both traffic and pollution. Of course, it's not a simple solution, because building good transport networks is expensive and takes years, so it might not be realistic everywhere. But in the long run, I suspect the benefits would outweigh the costs, particularly in large cities where congestion is already a serious problem."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob.</strong> Yumshatish (it depends, on the whole, "
                "I suspect) + taxmin (could, might) + shart gap (if... would).</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Examiner:</strong> Do you think governments should invest more in public transport?<br>"
                "<em style=\"color:#475569;\">Hukumatlar jamoat transportiga ko'proq sarmoya kiritishi kerak deb o'ylaysizmi?</em></p>"
                "<p><strong>Candidate:</strong> Well, it depends to some extent on the country, but on the whole, yes, I'd argue they should... the benefits would outweigh the costs, particularly in large cities where congestion is already a serious problem.<br>"
                "<em style=\"color:#475569;\">Xo'sh, bu ma'lum darajada mamlakatga bog'liq, lekin umuman olganda, ha, kiritishi kerak deb aytaman. Agar hukumatlar ishonchli avtobus va poyezdlarga ko'proq sarmoya kiritsa, kamroq odam mashina haydashga ehtiyoj sezardi, bu esa ham tirbandlik, ham ifloslanishni sezilarli kamaytirishi mumkin. Albatta, bu oddiy yechim emas, chunki yaxshi transport tarmog'ini qurish qimmat va yillar talab qiladi, shuning uchun u hamma joyda ham real bo'lmasligi mumkin. Lekin uzoq muddatda foydalar xarajatlardan ustun bo'ladi deb gumon qilaman, ayniqsa tirbandlik allaqachon jiddiy muammo bo'lgan yirik shaharlarda.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Mavhum savolga (\"Should governments...?\") "
                "nega mutlaq \"Yes, always\" o'rniga yumshatilgan javob yaxshiroq?</p>"
            ),
            "choices": [
                {"text": "Yumshatilgan javob qochoqlikni bildiradi", "is_correct": False},
                {"text": "Ehtiyotkor, nozik javob (\"it depends... on the whole\") band 7+ va grammatik xilma-xillikni ko'rsatadi", "is_correct": True},
                {"text": "Mutlaq javob doim yaxshiroq", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ehtiyotkor javob "
                "yaxshiroq.</mark> Mavhum savollar nozik fikrlashni talab qiladi. "
                "\"It depends... on the whole, I'd argue...\" — o'ylangan, muvozanatli "
                "javob, va u modal fe'llar/shart gaplar orqali Grammatical Range'ni ham "
                "ko'taradi. Mutlaq \"always\" ko'pincha soddaroq eshitiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Kelajak yoki taxmin haqidagi savolga "
                "qaysi til mos?</p>"
            ),
            "choices": [
                {"text": "faqat o'tgan zamon", "is_correct": False},
                {"text": "modal fe'llar va shart gaplar: might/could, is likely to, if... would", "is_correct": True},
                {"text": "faqat \"yes\" yoki \"no\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: modal + shart "
                "gaplar.</mark> Taxmin/kelajak uchun \"it might/could...\", \"is likely "
                "to...\", \"if... would...\" — bu ehtiyotkorlikni va grammatik boylikni "
                "birga beradi. Mavhum savolga aniq \"fakt\" yo'q, shuning uchun taxmin "
                "tili tabiiy.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Hedging &amp; speculation</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it depends (on) ...</div><div class=\"pp-card-back\">bu ... ga bog'liq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on the whole</div><div class=\"pp-card-back\">umuman olganda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">arguably</div><div class=\"pp-card-back\">ehtimol, bahslashsa bo'ladiki</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it's likely to ...</div><div class=\"pp-card-back\">... ehtimoli katta</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I suspect (that) ...</div><div class=\"pp-card-back\">... deb gumon qilaman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in the long run</div><div class=\"pp-card-back\">uzoq muddatda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the benefits would outweigh the costs</div><div class=\"pp-card-back\">foydalar xarajatlardan ustun bo'lardi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">generally speaking</div><div class=\"pp-card-back\">umuman aytganda</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Mavhum/ijtimoiy savollar: yumshatish (hedging) + taxmin (speculation).</li>"
            "<li>Hedging: it depends, to some extent, on the whole, arguably.</li>"
            "<li>Speculation: might/could, is likely to, if... would (shart gap).</li>"
            "<li>Mutlaq javobdan (\"always\") ko'ra ehtiyotkor, muvozanatli javob band 7+.</li>"
            "</ul>"
        )},
    ],
},

]
