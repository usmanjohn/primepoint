"""
IELTS Speaking lessons 6-9 (orders 20-23) — the "2-qism: Kartochka bo'yicha gapirish
(Part 2 — Cue Card / Long Turn)" topic — third Speaking batch, see toc_ielts_speaking.txt.

Each lesson has one longer ~2-min model monologue clip (candidate = "Man") for shadowing.
Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_speaking_part2_20_23.py \
        --out examprep/management/commands/audio/speaking_part2
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

TOPIC_PART2 = {
    "title":   "2-qism: Kartochka bo'yicha gapirish (Part 2 — Cue Card / Long Turn)",
    "summary": "Part 2: kartochka (cue card) + 1 daqiqa eslatma + 2 daqiqa yakka nutq; "
               "odam/joy, voqea, buyum/yutuqni tuzilma bilan tasvirlash.",
    "icon":    "bi-card-text",
    "order":   3,
}

_SHADOW = (
    "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;\">"
    "<strong>🗣️ Shadowing:</strong> model javob ortidan bir xil ohang bilan takrorlang — "
    "3 kun, har kuni 3 marta. So'ng o'zingiznikini yozib, model bilan solishtiring.</div>"
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
# Lesson 6 (order 20 — Part 2 format & note-taking) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART2,
    "title": "IELTS Speaking 6: Part 2 Format — 1-Minute Notes, 2-Minute Talk",
    "summary": "Part 2 formati: kartochka + 1 daqiqa eslatma (kalit so'zlar, jumla emas) + 2 daqiqa yakka nutq; bulletlar tuzilmangiz, to'liq 2 daqiqa gapiring.",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Part 2 — yakka nutq (long turn)</h2>"
            "<p>2-qismda imtihonchi sizga <strong>kartochka (cue card)</strong> beradi: "
            "mavzu + 3–4 ta yo'naltiruvchi band (bullet). Sizga <mark "
            "style=\"background:#dbeafe;\">1 daqiqa tayyorgarlik</mark> (eslatma yozish) "
            "beriladi, keyin <mark style=\"background:#dbeafe;\">1–2 daqiqa</mark> to'xtovsiz "
            "gapirasiz (maqsad — 2 daqiqa). Oxirida 1–2 qisqa follow-up savol.</p>"
        )},
        {"rich_text": (
            "<h3>1 daqiqa — eslatma olish usuli</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Bulletlar = tuzilmangiz.</strong> Har "
            "bandga qarab, unga javob beradigan <u>kalit so'z</u> yozing. Bandlar "
            "nutqingizni tartiblab beradi — hech narsani o'ylab topishga hojat yo'q.</p></div>"
            "<div class=\"pp-step\"><p><strong>Jumla emas, KALIT SO'Z.</strong> 1 daqiqada "
            "to'liq gap yozishga vaqt yo'q. \"who: Mr K – English teacher\", \"why: "
            "patient, made me love reading\" kabi qisqa belgilar yeting.</p></div>"
            "<div class=\"pp-step\"><p><strong>Aniq misol/voqea qo'shing.</strong> Har "
            "bandga bitta aniq misol yoki hikoya o'ylab qo'ying — bu nutqni "
            "kengaytiradi va tabiiy qiladi.</p></div>"
            "<div class=\"pp-step\"><p><strong>To'liq 2 daqiqa gapiring.</strong> "
            "Bandlar tugasa ham to'xtamang — tafsilot, his-tuyg'u yoki qo'shimcha misol "
            "qo'shing. Erta to'xtash bandni pasaytiradi.</p></div>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> hikoyadek gapiring — kirish (\"I'd like to talk "
            "about...\"), tana (bandlar) va qisqa yakun (\"...so that's why...\"). "
            "O'tgan voqealar uchun o'tgan zamon; oxirigacha ravon davom eting.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna kartochka</h3>"
            + cue_card("Describe a book you have recently enjoyed reading.",
                       ["what the book was",
                        "what it was about",
                        "why you decided to read it",
                        "and explain why you enjoyed it"]) +
            "<p><strong>1 daqiqalik eslatma (kalit so'zlar):</strong> "
            "<em>book: Sapiens – Harari · about: history of humankind, farming revolution · "
            "why read: friend recommended, curious · why enjoyed: eye-opening, clear "
            "style</em>. Endi model nutqni eshiting:</p>"
        )},
        {
            "audio":        "ielts_s_020_1.mp3",
            "audio_script": [
                ("Man", "I'd like to talk about a book I read recently called Sapiens, by the historian Yuval Noah Harari. It's a non-fiction book that tells the entire history of humankind, from the earliest humans right up to the modern day. It covers big turning points, like the moment our ancestors developed language and, much later, the agricultural revolution, when people first began to farm. I decided to read it because a close friend of mine kept recommending it. He said it had completely changed the way he thought about the world, so naturally I was curious. As for why I enjoyed it, the main reason is that it made me see everyday things in a totally new light. For instance, the author argues that money, and even nations, are really just stories that humans have agreed to believe in, which I found fascinating. On top of that, it's written in a very clear, almost conversational style, so even though the ideas are quite deep, it never feels like hard work. All in all, it's a book I'd happily recommend to anyone."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model nutq (~2 daqiqa).</strong> E'tibor bering: kirish → "
                "har bandga javob → yakun; kengaytirish uchun misol (money/nations).</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing (avval o'zingiz urinib ko'ring!)</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> I'd like to talk about a book I read recently called Sapiens... All in all, it's a book I'd happily recommend to anyone.<br>"
                "<em style=\"color:#475569;\">Yaqinda o'qigan \"Sapiens\" (muallif Yuval Noah Harari) kitobi haqida gapirmoqchiman. Bu — insoniyatning butun tarixini eng qadimgi odamlardan to hozirgi kungacha hikoya qiluvchi badiiy bo'lmagan kitob. U tilning paydo bo'lishi va, ancha keyin, dehqonchilik inqilobi kabi katta burilish nuqtalarini qamraydi. Uni o'qishga qaror qildim, chunki yaqin do'stim doim tavsiya qilardi — u kitob dunyoga qarashini butunlay o'zgartirganini aytdi, tabiiyki, qiziqib qoldim. Nega yoqqaniga kelsak — asosiy sabab, u menga kundalik narsalarni butunlay yangicha ko'rsatdi. Masalan, muallif pul va hatto davlatlar aslida odamlar ishonishga kelishib olgan hikoyalar ekanini aytadi — buni juda maroqli deb topdim. Bundan tashqari, u juda tushunarli, deyarli suhbat uslubida yozilgan, shuning uchun g'oyalar chuqur bo'lsa-da, o'qish hech qachon og'ir tuyulmaydi. Umuman, buni istalgan odamga bemalol tavsiya qilaman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> 1 daqiqalik tayyorgarlikda nima yozish "
                "kerak?</p>"
            ),
            "choices": [
                {"text": "To'liq jumlalar bilan butun nutqni", "is_correct": False},
                {"text": "Har bandga javob beradigan qisqa KALIT so'zlar", "is_correct": True},
                {"text": "Hech narsa — yoddan gapirish kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kalit so'zlar.</mark> "
                "1 daqiqada to'liq gap yozishga vaqt yo'q. Har bandga qisqa belgilar "
                "(kalit so'z + bitta misol) yozing — bular gapirishda tuzilma va tayanch "
                "bo'ladi. Eslatmani o'qib emas, unga qarab tabiiy gapiring.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Barcha bulletlarni 1,5 daqiqada aytib "
                "bo'ldingiz. Nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "To'xtayman — hammasini aytdim", "is_correct": False},
                {"text": "Davom etaman: tafsilot, his-tuyg'u yoki qo'shimcha misol qo'shib, 2 daqiqaga yetkazaman", "is_correct": True},
                {"text": "Boshqa mavzuga o'taman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: davom etaman.</mark> "
                "Maqsad — to'liq 2 daqiqa ravon gapirish. Erta to'xtash Fluency & "
                "Coherence bandini pasaytiradi. Bandlar tugasa, oxirgi fikringizni "
                "chuqurlashtiring yoki yana bir aniq misol/hikoya qo'shing.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Part 2 openers</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I'd like to talk about ...</div><div class=\"pp-card-back\">Men ... haqida gapirmoqchiman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">The reason I chose this is ...</div><div class=\"pp-card-back\">Buni tanlaganimning sababi ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">As for why ...</div><div class=\"pp-card-back\">Nega ... ga kelsak</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">For instance / To give an example</div><div class=\"pp-card-back\">Masalan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">On top of that, ...</div><div class=\"pp-card-back\">Bundan tashqari, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">All in all, ...</div><div class=\"pp-card-back\">Umuman olganda, ... (yakun)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a turning point</div><div class=\"pp-card-back\">burilish nuqtasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">eye-opening</div><div class=\"pp-card-back\">ko'z ochuvchi, yangi qarash beradigan</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Part 2: kartochka + 1 daqiqa eslatma + 2 daqiqa yakka nutq + follow-up.</li>"
            "<li>Bulletlar tuzilmangiz — har biriga kalit so'z (jumla emas) yozing.</li>"
            "<li>Har bandga aniq misol/hikoya qo'shing; hikoyadek gapiring.</li>"
            "<li>To'liq 2 daqiqa davom eting — erta to'xtamang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 7 (order 21 — person or place) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART2,
    "title": "IELTS Speaking 7: Describing a Person or Place — Structure and Sample Answer",
    "summary": "Odam/joy kartochkasi: bulletlar bo'yicha tuzilma, tavsifiy lug'at va aniq misol bilan kengaytirish — namunaviy 2 daqiqalik javob.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Odam yoki joyni tasvirlash</h2>"
            "<p>Bu Part 2'ning eng ko'p uchraydigan turlaridan biri. Kalit — "
            "<strong>tavsifiy lug'at</strong> (shaxsiyat/tashqi ko'rinish yoki joy "
            "atmosferasi) va bulletlarni <u>aniq misol</u> bilan kengaytirish. Quruq "
            "faktlar emas — jonli tasvir.</p>"
            + cue_card("Describe a teacher who has influenced you.",
                       ["who the teacher was",
                        "what subject they taught",
                        "what they were like",
                        "and explain how they influenced you"])
        )},
        {
            "audio":        "ielts_s_021_1.mp3",
            "audio_script": [
                ("Man", "I'd like to talk about my secondary school English teacher, Mr Karimov, who had a huge influence on me. He taught English literature, which, to be honest, wasn't my favourite subject at first. What made him special was his personality. He was incredibly patient and enthusiastic, and he had this ability to make even the dullest topic come alive. Rather than just making us memorise things, he would ask us questions and genuinely listen to our answers, which made us feel that our opinions really mattered. In terms of how he influenced me, I'd say he's the main reason I fell in love with reading and, eventually, with learning languages. Before his class, I saw studying as a chore, but he showed me it could actually be enjoyable. He also encouraged me to enter a writing competition, which I ended up winning, and that gave me a real confidence boost. Even now, whenever I feel like giving up on something difficult, I remember his advice to be patient and keep going. So yes, he's someone I'll always be grateful to."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob (~2 daqiqa).</strong> Shaxsiyat lug'atiga "
                "e'tibor: <em>patient, enthusiastic, made topics come alive</em>; "
                "kengaytirish — aniq misol (writing competition).</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> I'd like to talk about my secondary school English teacher, Mr Karimov... So yes, he's someone I'll always be grateful to.<br>"
                "<em style=\"color:#475569;\">O'rta maktabdagi ingliz tili o'qituvchim janob Karimov haqida gapirmoqchiman — u menga katta ta'sir ko'rsatgan. U ingliz adabiyotidan dars berardi, rostini aytsam, avvaliga bu mening sevimli fanim emasdi. Uni alohida qilgan narsa — shaxsiyati edi. U nihoyatda sabrli va ishtiyoqli edi, hatto eng zerikarli mavzuni ham jonlantira olardi. Bizni shunchaki yodlatish o'rniga, savollar berardi va javoblarimizni chin dildan tinglardi — bu bizga fikrimiz muhim ekanini his qildirardi. Menga qanday ta'sir qilganiga kelsak, aynan u tufayli kitob o'qishni va keyinchalik tillarni o'rganishni sevib qoldim. Uning darsigacha o'qishni yuk deb bilardim, u esa u zavqli bo'lishi mumkinligini ko'rsatdi. U meni insho tanloviga qatnashishga undadi, men g'olib chiqdim va bu menga katta ishonch berdi. Hozir ham qiyin ishdan voz kechgim kelganda, uning sabrli bo'l va davom et degan maslahatini eslayman. Ha, u men har doim minnatdor bo'ladigan insonim.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Odamni tasvirlashda \"what they were "
                "like\" bandiga qaysi lug'at eng mos?</p>"
            ),
            "choices": [
                {"text": "\"He was a person.\"", "is_correct": False},
                {"text": "Shaxsiyat sifatlari: patient, enthusiastic, supportive", "is_correct": True},
                {"text": "Faqat tashqi ko'rinish o'lchamlari", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: shaxsiyat "
                "sifatlari.</mark> \"What they were like\" xarakterni so'raydi — aniq "
                "sifatlar (patient, enthusiastic) Lexical Resource'ni ko'rsatadi. \"He "
                "was a person\" — bo'sh; faqat o'lcham/tashqi ko'rinish yetarli emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Javob \"how they influenced you\" bandini "
                "qanday kuchli qildi?</p>"
            ),
            "choices": [
                {"text": "Umumiy gaplar bilan (\"he was good\")", "is_correct": False},
                {"text": "Aniq misol bilan: insho tanloviga undadi → g'olib chiqdim → ishonch", "is_correct": True},
                {"text": "Mavzuni o'zgartirib", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: aniq misol.</mark> "
                "\"...encouraged me to enter a competition, which I ended up winning...\" "
                "— aniq, shaxsiy hikoya umumiy gaplardan ancha kuchli. Aniq misollar Part "
                "2 javobini kengaytiradi va ishonarli qiladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Describing people/places</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to have a huge influence on me</div><div class=\"pp-card-back\">menga katta ta'sir ko'rsatmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">patient / enthusiastic</div><div class=\"pp-card-back\">sabrli / ishtiyoqli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to make a topic come alive</div><div class=\"pp-card-back\">mavzuni jonlantirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">supportive / down-to-earth</div><div class=\"pp-card-back\">ko'maklashuvchi / oddiy, kamtar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a confidence boost</div><div class=\"pp-card-back\">ishonch bag'ishlash</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be grateful to sb</div><div class=\"pp-card-back\">birovdan minnatdor bo'lmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a lively / peaceful atmosphere</div><div class=\"pp-card-back\">jonli / tinch muhit (joy uchun)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to see studying as a chore</div><div class=\"pp-card-back\">o'qishni yuk deb bilmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Odam/joy: bulletlarni tartib bilan yoping (kim/nima/qanaqa/qanday ta'sir).</li>"
            "<li>Tavsifiy lug'at ishlating: shaxsiyat sifatlari yoki joy atmosferasi.</li>"
            "<li>Aniq, shaxsiy misol bilan kengaytiring — umumiy gaplar emas.</li>"
            "<li>Yakun bilan yoping (\"...someone I'll always be grateful to\").</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 8 (order 22 — event or experience) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART2,
    "title": "IELTS Speaking 8: Describing an Event or Experience — Structure and Sample Answer",
    "summary": "Voqea/tajriba kartochkasi: o'tgan zamon hikoyasi (past simple + would), aniq lavha bilan kengaytirish — namunaviy 2 daqiqalik javob.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Voqea yoki tajribani tasvirlash</h2>"
            "<p>Bu turda siz o'tmishdagi voqeani <strong>hikoya qilib</strong> berasiz. "
            "Kalit — <mark style=\"background:#dbeafe;\">o'tgan zamon</mark>ni to'g'ri "
            "ishlatish: past simple (asosiy voqealar) + <em>would</em>/<em>used to</em> "
            "(takrorlangan harakatlar) + bir-ikki aniq lavha (vivid moment).</p>"
            + cue_card("Describe a memorable trip you have taken.",
                       ["where you went",
                        "who you went with",
                        "what you did there",
                        "and explain why it was memorable"])
        )},
        {
            "audio":        "ielts_s_022_1.mp3",
            "audio_script": [
                ("Man", "I'd like to describe a trip I took a couple of years ago to the mountains in the east of my country. I went with a small group of close friends. There were about five of us, and we'd been planning it for months. We spent three days hiking through the valleys and camping near a lake, which was absolutely stunning. During the day we would walk for hours, and in the evenings we would cook simple meals over a fire and just talk for hours under the stars. What made it so memorable, I think, was partly the scenery, which was breathtaking, but mostly the feeling of being completely disconnected from everyday life. There was no phone signal at all, so for once none of us were staring at our screens. I remember one morning we woke up to find the whole lake covered in mist. It looked almost magical. Looking back, it was one of those rare trips where everything just came together perfectly, and I still think about it whenever I need to relax. I'd love to go back one day."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob (~2 daqiqa).</strong> O'tgan zamonga e'tibor: "
                "<em>took, went, spent</em> (past simple) + <em>we would walk/cook</em> "
                "(takror) + aniq lavha (mist covering the lake).</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> I'd like to describe a trip I took a couple of years ago to the mountains... I'd love to go back one day.<br>"
                "<em style=\"color:#475569;\">Bir necha yil oldin mamlakatimning sharqidagi tog'larga qilgan sayohatim haqida gapirmoqchiman. Bir guruh yaqin do'stlarim bilan bordim — beshtacha edik va uni oylar davomida rejalashtirgandik. Uch kun vodiylar bo'ylab piyoda yurdik va hayratlanarli darajada go'zal ko'l yonida chodirda tunadik. Kunduzi soatlab yurardik, kechqurunlari esa gulxanda oddiy taomlar pishirardik va yulduzlar ostida soatlab suhbatlashardik. Uni shu qadar esda qolarli qilgan narsa — qisman manzara, u nafas oldiradigan darajada go'zal edi, lekin ko'proq kundalik hayotdan butunlay uzilib qolish hissi edi. Umuman telefon aloqasi yo'q edi, shuning uchun bir marta bo'lsa-da, hech birimiz ekranga tikilmadik. Bir kuni ertalab uyg'onib, butun ko'l tuman bilan qoplanganini ko'rganimiz esimda — u deyarli sehrli ko'rinardi. Orqaga qarasam, bu hamma narsa mukammal jamlangan noyob sayohatlardan biri edi va dam olishga ehtiyoj sezganimda hali ham u haqda o'ylayman. Bir kun yana borishni juda xohlardim.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> O'tmishdagi voqeani hikoya qilishda "
                "takrorlangan (odatiy) harakatlar uchun qaysi tuzilma ishlatiladi?</p>"
            ),
            "choices": [
                {"text": "will + fe'l", "is_correct": False},
                {"text": "would / used to + fe'l (\"we would walk for hours\")", "is_correct": True},
                {"text": "hozirgi zamon", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: would / used to.</mark> "
                "O'tmishdagi <u>takrorlangan</u> harakatlar uchun \"would\" yoki \"used "
                "to\" (\"we would cook over a fire\") — bu grammatik xilma-xillikni "
                "ko'rsatadi. Asosiy voqealar past simple'da (went, spent). Bu aralashma "
                "Grammatical Range'ni oshiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Javobni nima esda qolarli qildi?</p>"
            ),
            "choices": [
                {"text": "Faqat \"it was good\" deb", "is_correct": False},
                {"text": "Aniq, jonli lavha: bir ertalab butun ko'l tuman bilan qoplangani", "is_correct": True},
                {"text": "Raqamlar va sanalar sanab", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: jonli lavha.</mark> "
                "\"...we woke up to find the whole lake covered in mist...\" — bitta aniq, "
                "tasvirli lavha butun nutqni jonlantiradi va eslab qolinadigan qiladi. "
                "Umumiy \"it was good\" bandni ko'tarmaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Describing events</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">we'd been planning it for months</div><div class=\"pp-card-back\">uni oylab rejalashtirgandik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">breathtaking / stunning</div><div class=\"pp-card-back\">nafas oldiradigan / hayratlanarli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">we would (walk/cook) ...</div><div class=\"pp-card-back\">biz (yurar/pishirar) edik (takror)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be disconnected from ...</div><div class=\"pp-card-back\">... dan uzilib qolmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">everything came together perfectly</div><div class=\"pp-card-back\">hammasi mukammal jamlandi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Looking back, ...</div><div class=\"pp-card-back\">Orqaga qarasam, ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it was one of those rare ...</div><div class=\"pp-card-back\">bu o'sha noyob ... lardan biri edi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I still think about it</div><div class=\"pp-card-back\">hali ham u haqda o'ylayman</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Voqea/tajriba = o'tmish hikoyasi; past simple + would/used to (takror).</li>"
            "<li>Bulletlarni yoping (qayerda/kim bilan/nima qildingiz/nega esda qolarli).</li>"
            "<li>Bitta aniq, jonli lavha qo'shing — bu javobni yodda qoladigan qiladi.</li>"
            "<li>Tavsifiy sifatlar: breathtaking, stunning, magical.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 9 (order 23 — object or achievement) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "speaking",
    "topic": TOPIC_PART2,
    "title": "IELTS Speaking 9: Describing an Object or Achievement — Structure and Sample Answer",
    "summary": "Buyum/yutuq kartochkasi: bulletlar bo'yicha tuzilma, \"kichik\" mavzuni ham his-tuyg'u va ma'no bilan rivojlantirish — namunaviy 2 daqiqalik javob.",
    "order": 23,
    "blocks": [
        {"rich_text": (
            "<h2>Buyum yoki yutuqni tasvirlash</h2>"
            "<p>Yutuq (achievement) kartochkalari ko'p uchraydi. Muhim maslahat: mavzu "
            "\"kichik\" tuyulsa ham (masalan haydovchilik guvohnomasini olish), uni "
            "<mark style=\"background:#dbeafe;\">his-tuyg'u va ma'no</mark> bilan "
            "rivojlantiring — nega muhim edi, nima o'rgatdi. Ma'no muhim, mavzuning "
            "\"kattaligi\" emas.</p>"
            + cue_card("Describe an achievement you are proud of.",
                       ["what the achievement was",
                        "when it happened",
                        "how you achieved it",
                        "and explain why you are proud of it"])
        )},
        {
            "audio":        "ielts_s_023_1.mp3",
            "audio_script": [
                ("Man", "The achievement I'd like to talk about is passing my driving test, which might sound small but was actually a big deal for me. It happened about three years ago, when I was nineteen. The reason it meant so much is that I had failed on my first two attempts, so by the third time I was really nervous and starting to doubt myself. To achieve it, I had to put in a lot of practice. I took extra lessons, practised with my father every weekend, and forced myself to drive on busy roads even though they made me anxious. On the day of the test, I stayed as calm as I could, focused on one thing at a time, and somehow it all went smoothly. When the examiner told me I had passed, I honestly felt like celebrating for a week. I'm proud of it not really because of the licence itself, but because it taught me that failing a couple of times doesn't mean you should give up. That lesson has stayed with me and helped me in a lot of other areas of my life ever since."),
            ],
            "rich_text": (
                "<p><strong>🎧 Model javob (~2 daqiqa).</strong> \"Kichik\" mavzu, lekin "
                "ma'no bilan chuqurlashtirilgan: <em>failed twice → practice → what it "
                "taught me</em>.</p>"
                + _SHADOW +
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Candidate:</strong> The achievement I'd like to talk about is passing my driving test... That lesson has stayed with me and helped me in a lot of other areas of my life ever since.<br>"
                "<em style=\"color:#475569;\">Gapirmoqchi bo'lgan yutug'im — haydovchilik imtihonidan o'tganim, bu kichik tuyulishi mumkin, lekin men uchun katta voqea edi. U taxminan uch yil oldin, men o'n to'qqiz yoshda ekanimda bo'ldi. Bu menga shunchalik muhim bo'lganining sababi — birinchi ikki urinishimda yiqilgandim, shuning uchun uchinchi safar juda hayajonda edim va o'zimga shubha qila boshlagandim. Buni uddalash uchun ko'p mashq qilishim kerak edi. Qo'shimcha darslar oldim, har dam olish kunlari otam bilan mashq qildim va meni hovliqtirsa ham gavjum yo'llarda haydashga o'zimni majbur qildim. Imtihon kuni iloji boricha xotirjam bo'ldim, bir vaqtning o'zida bitta narsaga e'tibor qaratdim va negadir hammasi silliq o'tdi. Imtihonchi o'tganimni aytganda, rostdan ham bir hafta bayram qilgim keldi. Men bundan guvohnoma uchun emas, balki bir-ikki marta yiqilish taslim bo'lish kerak degani emasligini o'rgatgani uchun faxrlanaman. Bu saboq menda qoldi va o'shandan beri hayotimning boshqa ko'p sohalarida yordam berdi.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Yutuq mavzusi \"kichik\" tuyulsa (masalan "
                "guvohnoma olish), nima qilish kerak?</p>"
            ),
            "choices": [
                {"text": "Boshqa, \"kattaroq\" mavzu tanlash", "is_correct": False},
                {"text": "Uni his-tuyg'u va MA'NO bilan rivojlantirish (nega muhim, nima o'rgatdi)", "is_correct": True},
                {"text": "Faqat faktlarni qisqa aytish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ma'no bilan "
                "rivojlantirish.</mark> IELTS mavzuning \"kattaligi\"ni emas, tilingizni "
                "baholaydi. \"Kichik\" yutuqni ham chuqur qilish mumkin: nega muhim edi, "
                "qanday his qildingiz, nima o'rgatdi. Ma'no va his-tuyg'u javobni "
                "boyitadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Javob \"why you are proud\" bandini "
                "qanday kuchli yakunladi?</p>"
            ),
            "choices": [
                {"text": "Guvohnomaning o'zi bilan faxrlanib", "is_correct": False},
                {"text": "O'rgangan saboq bilan: yiqilish taslim bo'lish degani emas", "is_correct": True},
                {"text": "Boshqa yutuqlarni sanab", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: o'rgangan "
                "saboq.</mark> \"...proud not because of the licence, but because it "
                "taught me that failing doesn't mean giving up...\" — yutuqni chuqur "
                "MA'NOga bog'lash (o'rgangan saboq) javobni ancha kuchli va reflektiv "
                "qiladi. Bu \"explain why\" bandini a'lo darajada yopadi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Object / achievement</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it might sound small, but ...</div><div class=\"pp-card-back\">kichik tuyulishi mumkin, lekin ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a big deal (for me)</div><div class=\"pp-card-back\">(men uchun) katta voqea/ish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to put in a lot of practice</div><div class=\"pp-card-back\">ko'p mashq qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to doubt myself</div><div class=\"pp-card-back\">o'zimga shubha qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it went smoothly</div><div class=\"pp-card-back\">silliq o'tdi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it taught me that ...</div><div class=\"pp-card-back\">u menga ... ekanini o'rgatdi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">that lesson has stayed with me</div><div class=\"pp-card-back\">o'sha saboq menda qoldi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a sentimental value</div><div class=\"pp-card-back\">hissiy qadr (buyum uchun)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Buyum/yutuq: bulletlarni yoping (nima/qachon/qanday/nega faxrlanasiz).</li>"
            "<li>\"Kichik\" mavzuni ham his-tuyg'u va ma'no bilan chuqurlashtiring.</li>"
            "<li>Yutuqni o'rgangan saboqqa bog'lang — bu \"why\" bandini kuchli yopadi.</li>"
            "<li>IELTS mavzu kattaligini emas, TILNI baholaydi.</li>"
            "</ul>"
        )},
    ],
},

]
