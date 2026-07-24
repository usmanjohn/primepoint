"""
IELTS Listening lessons 1-3 (orders 1-3) — the "Strategiya va format (Overview &
Strategy)" topic — FIRST Listening batch, see toc_ielts_listening.txt.

Lesson 3 carries audio blocks (spelling / numbers / correction-trap demos). Generate
the mp3s with:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_strategy_1_3.py \
        --out examprep/management/commands/audio/ielts_listening_strategy
then import with --audio-dir pointing at that folder.

NOTE (speaker names in audio): the tuple's first element (Woman/Man) only CHOOSES the
voice — it is never spoken. Never write the name into the line text ("Woman", "Sarah:
Hi") or the narrator says "Sarah: hi". See STYLE_GUIDE_IELTS.md §5c.
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
    "title":   "Strategiya va format (Overview & Strategy)",
    "summary": "IELTS Listening qanday tuzilgan va uni qanday yechish — format, "
               "oldindan o'qish va imlo/raqam/tuzoqlarga tayyorgarlik.",
    "icon":    "bi-compass",
    "order":   1,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 1 (order 1 — how it works)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Listening 1: How It Works — 4 Sections, One Listen, Answer Transfer",
    "summary": "IELTS Listening formati: 4 bo'lim, 40 savol, audio faqat BIR marta yangraydi; qiyinlik bo'limdan bo'limga ortadi.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>IELTS Listening — umumiy manzara</h2>"
            "<p>IELTS Listening butun imtihonning birinchi qismi. U <strong>~30 daqiqa "
            "audio</strong> + (qog'oz versiyasida) <strong>10 daqiqa ko'chirish</strong> "
            "vaqtidan iborat. Jami <strong>40 savol</strong>, <strong>4 bo'lim</strong>ga "
            "bo'lingan. Eng muhim fakt esa quyida:</p>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>🔴 Audio faqat BIR MARTA yangraydi.</strong> Reading'dan asosiy "
            "farqi shu: matn oldingizda turmaydi, orqaga qaytolmaysiz. Shuning uchun "
            "Listening — bu <u>real vaqt</u> ko'nikmasi: eshitib turib, bir vaqtda "
            "javob yozasiz.</div>"
        )},
        {"rich_text": (
            "<h3>4 bo'lim — qiyinlik asta ortadi</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-bo'lim (Section 1) — kundalik suhbat, "
            "2 kishi.</strong> Masalan, biror narsani band qilish yoki so'rov (booking/"
            "enquiry). Ko'pincha forma to'ldirish: ism, manzil, raqam. <u>Eng oson</u> "
            "bo'lim — bu yerda ball yig'ing.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-bo'lim (Section 2) — monolog, kundalik "
            "mavzu.</strong> Bitta odam gapiradi: joy haqida ma'lumot, ekskursiya, "
            "e'lon. Ko'p variantli savollar va xarita/plan belgilash.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-bo'lim (Section 3) — ta'limiy munozara, "
            "4 kishigacha.</strong> Talabalar + o'qituvchi biror topshiriqni muhokama "
            "qiladi. \"Kim nima dedi\"ni kuzatish qiyinlashadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-bo'lim (Section 4) — akademik ma'ruza, "
            "1 kishi.</strong> Universitet leksiyasi kabi — uzun, zich, ilmiy lug'at. "
            "<u>Eng qiyin</u>; savollar orasida to'xtash YO'Q.</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> 1–2-bo'limlar — ijtimoiy/kundalik kontekst, "
            "3–4-bo'limlar — ta'lim/akademik kontekst. Savollar deyarli har doim "
            "<u>audio tartibida</u> keladi — 1-savol javobi 2-savolnikidan oldin "
            "eshitiladi.</div>"
        )},
        {"rich_text": (
            "<h3>Javoblarni ko'chirish (answer transfer)</h3>"
            "<p>Qog'oz (paper) imtihonda: eshitish paytida javoblarni savol varag'iga "
            "yozasiz, oxirida <u>10 daqiqa</u> beriladi — javoblarni rasmiy javob "
            "varag'iga (answer sheet) ko'chirish uchun. Kompyuter (CD IELTS) versiyasida "
            "esa alohida ko'chirish vaqti yo'q — to'g'ridan-to'g'ri kiritasiz, oxirida "
            "2 daqiqa tekshiruv.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> ko'chirishda imloni aynan saqlang va "
            "<u>so'z chegarasi</u>ni buzmang (Reading'dagi kabi: NO MORE THAN TWO "
            "WORDS). Ko'chirishda tez-tez ball yo'qoladi — imlo xatosi yoki noto'g'ri "
            "katakcha. Diqqat bilan ko'chiring.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> IELTS Listening'ning Reading'dan eng "
                "muhim farqi nima?</p>"
            ),
            "choices": [
                {"text": "Listening'da savollar ko'proq bo'ladi", "is_correct": False},
                {"text": "Audio faqat bir marta yangraydi — orqaga qaytarib bo'lmaydi", "is_correct": True},
                {"text": "Listening'da so'z chegarasi bo'lmaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: audio bir marta "
                "yangraydi.</mark> Bu — Listening'ning asosiy bosimi. Reading'da matn "
                "oldingizda, xohlagancha qayta o'qiysiz; Listening'da esa bir imkoniyat. "
                "Shuning uchun oldindan o'qish va bashorat (keyingi dars) hal qiluvchi "
                "ko'nikma. (So'z chegarasi Listening'da ham bor.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Qaysi bo'lim odatda eng oson va ball "
                "yig'ish uchun eng qulay?</p>"
            ),
            "choices": [
                {"text": "Section 1 — kundalik suhbat, forma to'ldirish", "is_correct": True},
                {"text": "Section 4 — akademik ma'ruza", "is_correct": False},
                {"text": "Section 3 — 4 kishilik munozara", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Section 1.</mark> "
                "Qiyinlik bo'limdan bo'limga ortadi: 1-bo'lim eng oson (2 kishilik "
                "kundalik suhbat, aniq ma'lumot — ism, raqam, manzil), 4-bo'lim eng qiyin "
                "(akademik monolog). 1-bo'limda ishonchli ball yig'ib, kuchni 3–4-bo'limga "
                "saqlang.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a section</div><div class=\"pp-card-back\">bo'lim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a monologue</div><div class=\"pp-card-back\">monolog (bir kishi nutqi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a booking / an enquiry</div><div class=\"pp-card-back\">band qilish / so'rov</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">answer sheet</div><div class=\"pp-card-back\">javob varag'i</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to transfer answers</div><div class=\"pp-card-back\">javoblarni ko'chirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a lecture</div><div class=\"pp-card-back\">ma'ruza, leksiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">context</div><div class=\"pp-card-back\">kontekst, vaziyat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">real time</div><div class=\"pp-card-back\">real vaqt (jonli)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>4 bo'lim, 40 savol, ~30 daqiqa; audio faqat BIR marta yangraydi.</li>"
            "<li>Qiyinlik ortadi: 1 (kundalik suhbat) → 4 (akademik ma'ruza).</li>"
            "<li>1–2 ijtimoiy, 3–4 akademik kontekst; savollar audio tartibida.</li>"
            "<li>Qog'oz testda oxirida 10 daqiqa ko'chirish — imlo va so'z chegarasini saqlang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 2 (order 2 — predicting / reading ahead)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Listening 2: Predicting Answers Before the Audio Starts",
    "summary": "Eng muhim Listening ko'nikmasi: har bo'limdan oldingi pauza'da savollarni o'qib, javob turini va sinonimlarni oldindan bashorat qilish.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Eng muhim ko'nikma: oldindan o'qish</h2>"
            "<p>Har bo'lim boshlanishidan oldin audio sizga <strong>bir necha soniya "
            "pauza</strong> beradi: <em>\"You now have some time to look at questions "
            "1 to 10.\"</em> Ko'p nomzod bu vaqtni behuda o'tkazadi. Aslida bu — "
            "<mark style=\"background:#dbeafe;\">butun Listening'ning eng qimmatli "
            "soniyalari</mark>. Bu vaqtda savollarni o'qib, miyangizni \"nima "
            "eshitishga\" sozlaysiz.</p>"
        )},
        {"rich_text": (
            "<h3>Pauza'da nima qilish kerak</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Savollarni tez o'qing.</strong> Nima "
            "so'ralayotganini tushuning — savol turi (forma? ko'p variant? xarita?).</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Javob turini bashorat qiling.</strong> "
            "Bo'sh joyga qanday so'z tushadi? Reading'dagi kabi: <em>son? ism? "
            "manzil? ot?</em> Masalan \"Cost: £______\" → narx (raqam) eshitasiz.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Kalit so'zlarni belgilang.</strong> Har "
            "savoldagi o'zgarmas langar so'zni (ism, joy) ajrating — u audioda "
            "\"signal\" bo'lib, javob yaqinlashganini bildiradi.</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Sinonimlarni kutish.</strong> Audio "
            "savoldagi so'zni aynan aytmaydi — <u>paraphrase</u> qiladi. \"children\" "
            "→ audioda \"kids\" yoki \"under-12s\" bo'lishi mumkin. Sinonimni oldindan "
            "o'ylab qo'ying.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — bashorat kuchda</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Forma savoli:</strong></p>"
            "<p style=\"margin:0 0 4px;\">Name: Sarah ______</p>"
            "<p style=\"margin:0 0 4px;\">Arrival date: ______</p>"
            "<p style=\"margin:0 0 4px;\">Number of guests: ______</p>"
            "<p style=\"margin:0;\">Payment by: ______</p>"
            "</div>"
            "<p>Audio boshlanishidan oldin siz allaqachon bilasiz: 1-javob — "
            "<u>familiya</u> (imlo bilan aytiladi!), 2-javob — <u>sana</u>, 3-javob — "
            "<u>son</u>, 4-javob — <u>to'lov usuli</u> (\"credit card\", \"cash\"...). "
            "Endi audioni eshitganda aynan shu turdagi ma'lumotni \"ovlaysiz\" — "
            "adashmaysiz.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> agar bir savolni o'tkazib yuborsangiz "
            "(eshitmay qolsangiz), <u>darhol keyingisiga o'ting</u> — audio to'xtamaydi. "
            "Bitta yo'qolgan javobga osilib qolib, keyingi uchtasini boy bermang. "
            "Bo'sh katakni oxirida (transfer paytida) taxmin bilan to'ldirasiz.</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bo'lim oldidagi \"time to look at the "
                "questions\" pauzasi'ning eng yaxshi ishlatilishi qaysi?</p>"
            ),
            "choices": [
                {"text": "Dam olish va keyingi bo'limga tayyorlanish", "is_correct": False},
                {"text": "Savollarni o'qib, javob turini va kutiladigan sinonimlarni bashorat qilish", "is_correct": True},
                {"text": "Oldingi bo'lim javoblarini qayta ko'rish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: savollarni o'qib "
                "bashorat qilish.</mark> Bu pauza — bepul tayyorgarlik. Savol turini va "
                "javob turini (son/ism/ot) oldindan bilsangiz, audio yangraganda faqat "
                "shu ma'lumotni ushlaysiz. Oldingi bo'limga qaytish — vaqt isrofi (u "
                "tugagan); dam olish esa eng qimmat soniyalarni yoqib yuborish.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Savol varag'ida \"How much does a "
                "monthly ticket cost? £______\". Audioda \"children\" so'zi o'rniga nima "
                "eshitishingiz ehtimoli bor?</p>"
            ),
            "choices": [
                {"text": "Aynan \"children\" — audio har doim savol so'zini takrorlaydi", "is_correct": False},
                {"text": "Paraphrase: \"kids\", \"under-12s\" yoki \"young people\" — sinonimni kutish kerak", "is_correct": True},
                {"text": "Hech narsa — bu so'z audioda umuman bo'lmaydi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: paraphrase.</mark> "
                "Reading'dagi kabi, Listening ham <u>sinonim</u> bilan ishlaydi: savolda "
                "\"children\", audioda \"kids / under-12s\". Agar faqat \"children\" "
                "so'zini kutsangiz, javobni o'tkazib yuborasiz. Bashorat bosqichida "
                "mumkin sinonimlarni o'ylab qo'ying — quloq shunga tayyor bo'ladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to predict</div><div class=\"pp-card-back\">bashorat qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to read ahead</div><div class=\"pp-card-back\">oldindan o'qib qo'ymoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a keyword / anchor</div><div class=\"pp-card-back\">kalit / langar so'z</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a synonym</div><div class=\"pp-card-back\">sinonim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to anticipate</div><div class=\"pp-card-back\">oldindan kutmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to move on</div><div class=\"pp-card-back\">keyingisiga o'tmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a guess</div><div class=\"pp-card-back\">taxmin</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to tune in</div><div class=\"pp-card-back\">sozlanmoq, moslashmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Har bo'lim oldidagi pauza — eng qimmatli vaqt: savollarni o'qing.</li>"
            "<li>Javob turini bashorat qiling (son/ism/sana/ot) — Reading'dagi kabi.</li>"
            "<li>Langar so'zni belgilang; audio uni paraphrase qiladi — sinonimni kuting.</li>"
            "<li>Savolni o'tkazib yuborsangiz — darhol keyingisiga o'ting, osilib qolmang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 3 (order 3 — spelling, numbers, traps) — WITH AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Listening 3: Spelling, Numbers, Dates and Correction Traps",
    "summary": "Imlo (harflab aytilgan ism), raqamlar (double/oh/triple), sana va eng ayyor tuzoq — tuzatish momenti (aytdi, keyin o'zgartirdi).",
    "order": 3,
    "blocks": [
        {"rich_text": (
            "<h2>Aniqlik jangi: imlo, raqam, tuzatish</h2>"
            "<p>1-bo'limda ballning katta qismi <u>aniq ma'lumot</u>ga bog'liq: ismlar, "
            "raqamlar, manzillar, sanalar. Bu yerda bitta harf yoki bitta raqam xato "
            "bo'lsa — javob noto'g'ri. Bu dars uch narsaga tayyorlaydi: <strong>imlo, "
            "raqamlar</strong> va eng ayyor tuzoq — <strong>tuzatish momenti</strong>.</p>"
        )},
        {"rich_text": (
            "<h3>1. Imlo — harflab aytilgan so'zlar</h3>"
            "<p>Ismlar va joy nomlari ko'pincha <u>harflab</u> aytiladi: <em>\"My "
            "surname is Bolton — B-O-L-T-O-N.\"</em> Ingliz alifbosi tovushlarini "
            "mukammal bilishingiz shart. Eng ko'p adashtiradigan juftliklar:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\"><strong>A</strong> /ey/ &nbsp;↔&nbsp; <strong>E</strong> /iy/ &nbsp;↔&nbsp; <strong>I</strong> /ay/ — eng ko'p chalkashlik</p>"
            "<p style=\"margin:0 0 4px;\"><strong>G</strong> /jiy/ &nbsp;↔&nbsp; <strong>J</strong> /jey/</p>"
            "<p style=\"margin:0 0 4px;\"><strong>M</strong> /em/ &nbsp;↔&nbsp; <strong>N</strong> /en/</p>"
            "<p style=\"margin:0 0 4px;\"><strong>P</strong> /piy/ &nbsp;↔&nbsp; <strong>B</strong> /biy/ &nbsp;↔&nbsp; <strong>V</strong> /viy/</p>"
            "<p style=\"margin:0;\"><strong>double L</strong> = LL, &nbsp;<strong>double O</strong> = OO (takrorlangan harf)</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> \"double\" = keyingi harf/raqam ikki marta. "
            "<em>\"Anna — A-double-N-A\"</em> = A-N-N-A. Bosh harf (capital) odatda "
            "muhim emas — javobni to'g'ri harflar bilan yozing.</div>"
        )},
        {"rich_text": (
            "<h3>2. Raqamlar, sana va narx</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Telefon raqami:</strong> raqamlar birma-bir aytiladi; <em>0</em> = \"oh\" yoki \"zero\"; <em>double</em> = ikki marta. \"oh-seven-double-nine\" = 0799.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Sana:</strong> \"the third of March\" yoki \"March the third\" = 3 March. Yozishda format muhim emas, lekin oy nomi imlosi to'g'ri bo'lsin.</p>"
            "<p style=\"margin:0;\"><strong>Narx:</strong> \"fifteen fifty\" = £15.50; \"a fiver\" = £5. Valyuta belgisini (£/$) savol talab qilganidek yozing.</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — 13 vs 30:</strong> \"thirteen\" (/θɜːˈtiːn/, urg'u "
            "OXIRIDA) va \"thirty\" (/ˈθɜːti/, urg'u BOSHIDA) — eng klassik tuzoq. "
            "Urg'uga quloq soling: <em>-teen</em> oxirida kuchli.</div>"
        )},
        {"rich_text": (
            "<h3>3. Eng ayyor tuzoq — tuzatish momenti</h3>"
            "<p>Bu 1-bo'limning imzo tuzog'i: gapiruvchi bir narsani aytadi, keyin uni "
            "<u>o'zgartiradi</u>. Javob — <mark style=\"background:#dcfce7;\">tuzatilgan "
            "(oxirgi)</mark> variant, birinchisi emas. Signal so'zlarni ushlang:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><em>\"Sorry...\", \"Actually...\", \"I mean...\", "
            "\"No, wait...\", \"Let me correct that...\", \"...or rather...\"</em> — "
            "bulardan keyin kelgan ma'lumot ESKIsini bekor qiladi.</p>"
            "</div>"
            "<p>Shoshgan nomzod birinchi eshitgan raqamini yozib, keyingi tuzatishni "
            "o'tkazib yuboradi. Siz esa signal so'zni eshitguningizcha \"qalamni "
            "ushlab turing\".</p>"
        )},
        # ── Audio block 1: correction trap (phone number) ──────────────────
        {
            "audio":        "ielts_l_003_1.mp3",
            "audio_script": [
                ("Woman", "Thanks for calling the Riverside Clinic. Can I take your name?"),
                ("Man",   "Yes, it's James Bolton. That's B-O-L-T-O-N."),
                ("Woman", "Thank you. And the best contact number for you?"),
                ("Man",   "It's oh-seven-nine, double-four, six-two-oh. Sorry — the last digit is one, not oh. Six-two-one."),
            ],
            "rich_text": (
                "<p><strong>Amaliyot 1 (audioni tinglang).</strong> Yuqoridagi "
                "tuzatish momentini eshiting. Erkak kishining telefon raqamining "
                "<u>oxirgi uch raqami</u> qaysi?</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">🎧 Bir marta tinglang — "
                "imtihondagidek. Signal so'zga (\"Sorry...\") diqqat qiling.</p>"
            ),
            "choices": [
                {"text": "620", "is_correct": False},
                {"text": "621", "is_correct": True},
                {"text": "610", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 621.</mark> "
                "Klassik tuzatish tuzog'i: erkak avval \"six-two-<u>oh</u>\" (620) deydi, "
                "keyin <em>\"<u>Sorry</u> — the last digit is <u>one</u>, not oh. "
                "Six-two-one\"</em> deb tuzatadi. Javob — oxirgi (tuzatilgan) variant: "
                "<strong>621</strong>. \"Sorry\" signalini eshitib, birinchi javobni "
                "o'chirib, yangisini yozdingizmi?</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Thanks for calling the Riverside Clinic. Can I take your name?<br>"
                "<em style=\"color:#475569;\">Riverside klinikasiga qo'ng'iroq qilganingiz uchun rahmat. Ismingizni ayta olasizmi?</em></p>"
                "<p><strong>Man:</strong> Yes, it's James Bolton. That's B-O-L-T-O-N.<br>"
                "<em style=\"color:#475569;\">Ha, ismim James Bolton. B-O-L-T-O-N.</em></p>"
                "<p><strong>Woman:</strong> Thank you. And the best contact number for you?<br>"
                "<em style=\"color:#475569;\">Rahmat. Siz bilan bog'lanish uchun eng qulay raqam?</em></p>"
                "<p><strong>Man:</strong> It's oh-seven-nine, double-four, six-two-oh. Sorry — the last digit is one, not oh. Six-two-one.<br>"
                "<em style=\"color:#475569;\">Bu 079, 44, 6-2-0. Kechirasiz — oxirgi raqam 0 emas, 1. 6-2-1.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        # ── Audio block 2: spelling + correction (address) ─────────────────
        {
            "audio":        "ielts_l_003_2.mp3",
            "audio_script": [
                ("Woman", "And what's the delivery address?"),
                ("Man",   "It's fourteen Ashcroft Road. Ashcroft is A-S-H-C-R-O-F-T."),
                ("Woman", "Fourteen Ashcroft Road. Got it."),
                ("Man",   "Actually, could you deliver it to my office instead? Same number, but it's Ashcroft Lane, not Road."),
            ],
            "rich_text": (
                "<p><strong>Amaliyot 2 (audioni tinglang).</strong> Yetkazib berish "
                "manzili uchun to'g'ri ko'cha turi qaysi?</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">🎧 \"Actually...\" "
                "signaliga e'tibor bering.</p>"
            ),
            "choices": [
                {"text": "Ashcroft Road", "is_correct": False},
                {"text": "Ashcroft Lane", "is_correct": True},
                {"text": "Ashcroft Street", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Ashcroft Lane.</mark> "
                "Yana tuzatish tuzog'i: avval \"Ashcroft <u>Road</u>\", keyin <em>\""
                "<u>Actually</u>... it's Ashcroft <u>Lane</u>, not Road\"</em>. Javob — "
                "tuzatilgan variant: <strong>Lane</strong>. \"Ashcroft\" imlosi ham "
                "audioda harflab berildi (A-S-H-C-R-O-F-T) — imlo tuzog'i va tuzatish "
                "tuzog'i bir blokda!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> And what's the delivery address?<br>"
                "<em style=\"color:#475569;\">Yetkazib berish manzili qanday?</em></p>"
                "<p><strong>Man:</strong> It's fourteen Ashcroft Road. Ashcroft is A-S-H-C-R-O-F-T.<br>"
                "<em style=\"color:#475569;\">14 Ashcroft Road. Ashcroft — A-S-H-C-R-O-F-T.</em></p>"
                "<p><strong>Woman:</strong> Fourteen Ashcroft Road. Got it.<br>"
                "<em style=\"color:#475569;\">14 Ashcroft Road. Yozib oldim.</em></p>"
                "<p><strong>Man:</strong> Actually, could you deliver it to my office instead? Same number, but it's Ashcroft Lane, not Road.<br>"
                "<em style=\"color:#475569;\">Aslida, uni ofisimga yetkazsangiz bo'ladimi? Raqami o'sha, lekin Ashcroft Lane, Road emas.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Gapiruvchi \"...half past four — sorry, "
                "quarter past four\" desa, uchrashuv vaqti nechada?</p>"
            ),
            "choices": [
                {"text": "4:30 (half past four)", "is_correct": False},
                {"text": "4:15 (quarter past four)", "is_correct": True},
                {"text": "3:45", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 4:15.</mark> "
                "\"Sorry\" — tuzatish signali. Birinchi \"half past four\" (4:30) bekor "
                "qilinadi, tuzatilgan \"quarter past four\" (4:15) — to'g'ri javob. "
                "Qoida bir xil: signal so'zdan keyingi ma'lumot ustun. (\"quarter "
                "past\" = 15 daqiqa o'tdi, \"quarter to\" = 15 daqiqa qoldi — buni ham "
                "chalkashtirmang.)</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to spell out</div><div class=\"pp-card-back\">harflab aytmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">double / triple</div><div class=\"pp-card-back\">ikki marta / uch marta (harf/raqam)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a correction</div><div class=\"pp-card-back\">tuzatish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Actually... / I mean...</div><div class=\"pp-card-back\">Aslida... / Ya'ni... (tuzatish signali)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">quarter past / quarter to</div><div class=\"pp-card-back\">chorak o'tdi / chorak qoldi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a contact number</div><div class=\"pp-card-back\">bog'lanish raqami</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a delivery address</div><div class=\"pp-card-back\">yetkazib berish manzili</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">thirteen vs thirty</div><div class=\"pp-card-back\">13 va 30 (urg'u farqi)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Imlo: ingliz alifbosi tovushlarini biling (A/E/I, G/J, M/N chalkashligi); \"double\" = takror.</li>"
            "<li>Raqam: \"oh\"=0, \"double\"=ikki marta; 13 va 30 ni urg'udan farqlang.</li>"
            "<li>Tuzatish tuzog'i: \"Sorry / Actually / I mean\" dan keyingi javob TO'G'RI, birinchisi emas.</li>"
            "<li>Signal so'zni eshitguncha oxirgi javobga shoshilmang — qalamni ushlab turing.</li>"
            "<li>Javobni to'g'ri imlo va so'z chegarasi bilan yozing.</li>"
            "</ul>"
        )},
    ],
},

]
