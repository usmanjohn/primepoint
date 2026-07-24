"""
IELTS Listening lesson 16 (order 50) — the "Yakuniy tayyorgarlik (Full Mixed Practice)"
topic (single lesson) — the CAPSTONE that finishes the Listening track.
See toc_ielts_listening.txt.

Four short clips, one per section type (S1 form / S2 monologue MC / S3 discussion /
S4 lecture), named ielts_l_050_1..4.mp3. Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_final_50.py \
        --out examprep/management/commands/audio/ielts_listening_final
then import with --audio-dir. Speaker labels only choose the voice — never voiced.
See STYLE_GUIDE_IELTS.md §5c.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_FINAL = {
    "title":   "Yakuniy tayyorgarlik (Full Mixed Practice)",
    "summary": "To'rt bo'limning har biridan bittadan savol — butun Listening "
               "strategiyasini vaqt bosimi ostida bir joyda sinash.",
    "icon":    "bi-flag-fill",
    "order":   6,
}

LESSONS = [

{
    "skill": "listening",
    "topic": TOPIC_FINAL,
    "title": "IELTS Listening 16: Grand Mixed Review — One Question From Each Section",
    "summary": "Yakuniy sinov: 4 bo'limning har biridan audio va savol (forma, monolog MC, munozara, ma'ruza) — butun Listening kursining strategiyasi bir joyda.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>🏁 Yakuniy sinov — to'rt bo'lim bir joyda</h2>"
            "<p>Mana, Listening kursining <strong>so'nggi darsi</strong>! Endi to'rt "
            "bo'limning har biridan bittadan namuna — 1-bo'lim forma, 2-bo'lim monolog "
            "ko'p variantli, 3-bo'lim munozara, 4-bo'lim akademik ma'ruza — birga. "
            "O'rgangan har bir usulingizni shu yerda ishga solasiz.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Umumiy strategiya (eslatma):</strong> har audiodan oldin "
            "savollarni <u>o'qib</u>, javob turini bashorat qiling; audio <u>bir marta</u> "
            "yangraydi; savolni o'tkazib yuborsangiz — darhol keyingisiga o'ting; "
            "javobni imlo va so'z chegarasi bilan yozing.</div>"
        )},
        {"rich_text": (
            "<h3>Strategiya cheat-sheet — 4 bo'lim bir qarashda</h3>"
            "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
            "<summary style=\"cursor:pointer;font-weight:600;\">📂 Har bo'limning kaliti (bosing)</summary>"
            "<div style=\"margin-top:10px;\">"
            "<p style=\"margin:0 0 6px;\"><strong>1-bo'lim (forma):</strong> 2 kishilik kundalik suhbat; imlo va raqamlar; tuzatish tuzog'i (\"sorry, actually...\") — oxirgi variant to'g'ri.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>2-bo'lim (monolog MC + map):</strong> bitta ovoz; distraktor (\"said then corrected\"); map uchun yo'nalish tili (on your left, opposite).</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3-bo'lim (munozara):</strong> 4 kishigacha; ismlarni langar qiling; taklif ≠ qabul; yakuniy kelishuv javob.</p>"
            "<p style=\"margin:0;\"><strong>4-bo'lim (ma'ruza):</strong> bitta ovoz, pauzasiz; signpost so'zlar (firstly/however); so'z-tuzoqdan ehtiyot bo'ling.</p>"
            "</div>"
            "</details>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Tayyor bo'ling:</strong> 4 ta qisqa audio, jami 8 savol. Har "
            "audioni bir marta tinglang, savollarga javob bering, keyin skriptni oching.</div>"
        )},
        # ── PART 1 — Section 1 (form completion) ────────────────────────────
        {"rich_text": (
            "<h3>1-qism — 1-bo'lim uslubi (forma to'ldirish)</h3>"
        )},
        {
            "audio":        "ielts_l_050_1.mp3",
            "audio_script": [
                ("Woman", "Good evening, Parkview Hotel reservations. How can I help?"),
                ("Man",   "Hi, I'd like to book a room for two nights next weekend."),
                ("Woman", "Certainly. Can I take your surname?"),
                ("Man",   "It's Grant — G-R-A-N-T."),
                ("Woman", "Thank you. And how many guests will there be?"),
                ("Man",   "Two adults and one child. Actually, make that two children — my nephew is coming as well."),
                ("Woman", "So two adults and two children. Would you like breakfast included?"),
                ("Man",   "Yes, please."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta) va formani to'ldiring.</strong></p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>HOTEL BOOKING</strong></p>"
                "<p style=\"margin:0 0 4px;\">Surname: <strong>(1) ______</strong></p>"
                "<p style=\"margin:0;\">Number of children: <strong>(2) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Good evening, Parkview Hotel reservations. How can I help?<br>"
                "<em style=\"color:#475569;\">Xayrli kech, Parkview mehmonxona bandlovi. Sizga qanday yordam bera olaman?</em></p>"
                "<p><strong>Man:</strong> Hi, I'd like to book a room for two nights next weekend.<br>"
                "<em style=\"color:#475569;\">Salom, kelasi dam olish kunlariga ikki kechaga xona band qilmoqchiman.</em></p>"
                "<p><strong>Woman:</strong> Certainly. Can I take your surname?<br>"
                "<em style=\"color:#475569;\">Albatta. Familiyangizni ayta olasizmi?</em></p>"
                "<p><strong>Man:</strong> It's Grant — G-R-A-N-T.<br>"
                "<em style=\"color:#475569;\">Grant — G-R-A-N-T.</em></p>"
                "<p><strong>Woman:</strong> Thank you. And how many guests will there be?<br>"
                "<em style=\"color:#475569;\">Rahmat. Nechta mehmon bo'ladi?</em></p>"
                "<p><strong>Man:</strong> Two adults and one child. Actually, make that two children — my nephew is coming as well.<br>"
                "<em style=\"color:#475569;\">Ikki katta va bitta bola. Aslida, ikki bola qiling — jiyanim ham keladi.</em></p>"
                "<p><strong>Woman:</strong> So two adults and two children. Would you like breakfast included?<br>"
                "<em style=\"color:#475569;\">Demak ikki katta va ikki bola. Nonushta ham kiritilsinmi?</em></p>"
                "<p><strong>Man:</strong> Yes, please.<br>"
                "<em style=\"color:#475569;\">Ha, iltimos.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Familiya (surname) qanday yoziladi?</p>"
            ),
            "choices": [
                {"text": "Grant", "is_correct": True},
                {"text": "Grand", "is_correct": False},
                {"text": "Grantt", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Grant.</mark> "
                "Harflab berildi: G-R-A-N-<u>T</u> (oxirida T, D emas). \"Grand\" — "
                "tovushga o'xshaydi (T/D chalkashligi), lekin imlo aniq: Grant.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Nechta bola (children) bo'ladi?</p>"
            ),
            "choices": [
                {"text": "1", "is_correct": False},
                {"text": "2", "is_correct": True},
                {"text": "3", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 2.</mark> Tuzatish "
                "tuzog'i: \"one child. <u>Actually, make that two children</u>.\" \"Actually\" "
                "— tuzatish signali. Birinchi \"one\" bekor bo'ldi, to'g'ri javob 2.</p>"
            ),
        },
        # ── PART 2 — Section 2 (monologue MC) ───────────────────────────────
        {"rich_text": (
            "<h3>2-qism — 2-bo'lim uslubi (monolog, ko'p variantli)</h3>"
        )},
        {
            "audio":        "ielts_l_050_2.mp3",
            "audio_script": [
                ("Woman", "Welcome to the Riverside Craft Market. A few quick announcements before you explore."),
                ("Woman", "The market normally closes at five, but today, because of the summer festival, we'll stay open until eight."),
                ("Woman", "Free parking is available behind the library today, not in the main square as usual, since the square is being used for the stage."),
                ("Woman", "And if you get hungry, you'll find all the food stalls along the riverside path. Enjoy your visit."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> Hunarmandchilik bozori "
                "e'loni. Distraktor va tuzatishlarga diqqat!</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Welcome to the Riverside Craft Market. A few quick announcements before you explore.<br>"
                "<em style=\"color:#475569;\">Riverside hunarmandchilik bozoriga xush kelibsiz. Sayr qilishdan oldin bir necha qisqa e'lon.</em></p>"
                "<p><strong>Woman:</strong> The market normally closes at five, but today, because of the summer festival, we'll stay open until eight.<br>"
                "<em style=\"color:#475569;\">Bozor odatda soat 5 da yopiladi, lekin bugun yozgi festival tufayli 8 gacha ochiq bo'lamiz.</em></p>"
                "<p><strong>Woman:</strong> Free parking is available behind the library today, not in the main square as usual, since the square is being used for the stage.<br>"
                "<em style=\"color:#475569;\">Bugun bepul to'xtash joyi kutubxona orqasida, odatdagidek asosiy maydonda emas, chunki maydon sahna uchun ishlatilyapti.</em></p>"
                "<p><strong>Woman:</strong> And if you get hungry, you'll find all the food stalls along the riverside path. Enjoy your visit.<br>"
                "<em style=\"color:#475569;\">Va agar qorningiz ochsa, barcha ovqat rastalarini daryo bo'yidagi yo'lakda topasiz. Tashrifingizdan zavqlaning.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Bugun bozor soat nechada yopiladi?</p>"
            ),
            "choices": [
                {"text": "5 pm", "is_correct": False},
                {"text": "8 pm", "is_correct": True},
                {"text": "9 pm", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 8 pm.</mark> "
                "\"normally closes at five, <u>but today</u>... we'll stay open <u>until "
                "eight</u>.\" 5 — odatdagi (distraktor), 8 — bugungi. \"but today\" "
                "signali o'zgarishni bildiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Bugun bepul to'xtash joyi qayerda?</p>"
            ),
            "choices": [
                {"text": "asosiy maydonda (the main square)", "is_correct": False},
                {"text": "kutubxona orqasida (behind the library)", "is_correct": True},
                {"text": "daryo bo'yida", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: kutubxona "
                "orqasida.</mark> \"behind the library today, <u>not in the main square as "
                "usual</u>.\" \"not X as usual\" — asosiy maydon odatdagi (rad etilgan) "
                "joy. Daryo bo'yi — ovqat rastalari (boshqa savol).</p>"
            ),
        },
        # ── PART 3 — Section 3 (discussion) ─────────────────────────────────
        {"rich_text": (
            "<h3>3-qism — 3-bo'lim uslubi (munozara)</h3>"
        )},
        {
            "audio":        "ielts_l_050_3.mp3",
            "audio_script": [
                ("Man",   "Have you two chosen which topic to write your essay on?"),
                ("Woman", "I was going to do climate policy, but I'm finding it hard to get good sources."),
                ("Man2",  "I'd pick something more specific. What about electric cars? There's loads of recent data."),
                ("Woman", "That's a good idea, actually. Electric cars it is, then."),
                ("Man",   "Good choice. And remember the essay deadline is the fifteenth — not the twentieth, that's for the presentations."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> O'qituvchi (Man) va ikki "
                "talaba — Woman va Man2 — insho mavzusini muhokama qiladi.</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Tutor:</strong> Have you two chosen which topic to write your essay on?<br>"
                "<em style=\"color:#475569;\">Ikkovingiz insho mavzusini tanladingizmi?</em></p>"
                "<p><strong>Student (W):</strong> I was going to do climate policy, but I'm finding it hard to get good sources.<br>"
                "<em style=\"color:#475569;\">Iqlim siyosatini qilmoqchi edim, lekin yaxshi manba topish qiyin bo'lyapti.</em></p>"
                "<p><strong>Student (M):</strong> I'd pick something more specific. What about electric cars? There's loads of recent data.<br>"
                "<em style=\"color:#475569;\">Men aniqroq narsani tanlardim. Elektromobillar-chi? Ko'plab yangi ma'lumot bor.</em></p>"
                "<p><strong>Student (W):</strong> That's a good idea, actually. Electric cars it is, then.<br>"
                "<em style=\"color:#475569;\">Bu yaxshi fikr, aslida. Unda elektromobillar bo'ldi.</em></p>"
                "<p><strong>Tutor:</strong> Good choice. And remember the essay deadline is the fifteenth — not the twentieth, that's for the presentations.<br>"
                "<em style=\"color:#475569;\">Yaxshi tanlov. Va esda tuting, insho muddati 15-si — 20-si emas, u taqdimotlar uchun.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> Ayol talaba oxirida qaysi mavzuni "
                "tanladi?</p>"
            ),
            "choices": [
                {"text": "climate policy", "is_correct": False},
                {"text": "electric cars", "is_correct": True},
                {"text": "renewable energy", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: electric cars.</mark> "
                "\"I was going to do climate policy, <u>but</u>...\" keyin Man2 taklif "
                "qiladi, ayol rozi bo'ladi: \"That's a good idea... <u>Electric cars it "
                "is</u>.\" Climate policy — dastlabki (rad etilgan) g'oya; yakuniy "
                "kelishuv — electric cars.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 6.</strong> Insho muddati (deadline) qachon?</p>"
            ),
            "choices": [
                {"text": "the 15th", "is_correct": True},
                {"text": "the 20th", "is_correct": False},
                {"text": "the 5th", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: the 15th.</mark> "
                "\"the essay deadline is the <u>fifteenth</u> — <u>not the twentieth</u>, "
                "that's for the presentations.\" 20-si — taqdimotlar uchun (distraktor). "
                "Insho — 15-si. \"not X, that's for...\" tuzog'ini ushlang.</p>"
            ),
        },
        # ── PART 4 — Section 4 (academic lecture) ───────────────────────────
        {"rich_text": (
            "<h3>4-qism — 4-bo'lim uslubi (akademik ma'ruza)</h3>"
        )},
        {
            "audio":        "ielts_l_050_4.mp3",
            "audio_script": [
                ("Man", "Let's turn to one of nature's most remarkable abilities: the octopus's talent for camouflage."),
                ("Man", "Despite being colour-blind themselves, octopuses can match the colour of their surroundings almost instantly. They do this using millions of tiny cells in the skin, called chromatophores, each holding a sac of pigment that can expand or contract."),
                ("Man", "In addition to colour, they can change the texture of their skin, raising bumps to imitate rough coral or seaweed. This ability serves two purposes: escaping predators and, just as importantly, ambushing prey."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> \"Octopus camouflage\" "
                "ma'ruzasidan parcha. Eslatmalarni to'ldiring:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>LECTURE NOTES — Octopus Camouflage</strong></p>"
                "<p style=\"margin:0 0 4px;\">Colour-changing skin cells are called <strong>(7) ______</strong></p>"
                "<p style=\"margin:0;\">Besides colour, they can also change their skin's <strong>(8) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Lecturer:</strong> Let's turn to one of nature's most remarkable abilities: the octopus's talent for camouflage.<br>"
                "<em style=\"color:#475569;\">Tabiatning eng ajoyib qobiliyatlaridan biriga o'tamiz: sakkizoyoqning niqoblanish (camouflage) iste'dodi.</em></p>"
                "<p><strong>Lecturer:</strong> Despite being colour-blind themselves, octopuses can match the colour of their surroundings almost instantly. They do this using millions of tiny cells in the skin, called chromatophores, each holding a sac of pigment that can expand or contract.<br>"
                "<em style=\"color:#475569;\">O'zi rangni ajrata olmasa-da, sakkizoyoqlar atrofining rangiga deyarli bir zumda moslasha oladi. Buni terisidagi millionlab mayda hujayralar — xromatoforlar (chromatophores) yordamida qiladi; har biri kengayadigan yoki qisiladigan pigment xaltachasini saqlaydi.</em></p>"
                "<p><strong>Lecturer:</strong> In addition to colour, they can change the texture of their skin, raising bumps to imitate rough coral or seaweed. This ability serves two purposes: escaping predators and, just as importantly, ambushing prey.<br>"
                "<em style=\"color:#475569;\">Rangdan tashqari, ular terisining teksturasini (texture) ham o'zgartira oladi — g'adir-budur marjon yoki suvo'tga taqlid qilib do'mboqlar chiqaradi. Bu qobiliyat ikki maqsadga xizmat qiladi: yirtqichdan qochish va, xuddi shunday muhim — o'ljaga pistirma qurish.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 7.</strong> Rangni o'zgartiruvchi teri hujayralari "
                "qanday ataladi?</p>"
            ),
            "choices": [
                {"text": "chromatophores", "is_correct": True},
                {"text": "pigments", "is_correct": False},
                {"text": "predators", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: chromatophores.</mark> "
                "\"...millions of tiny cells in the skin, called <u>chromatophores</u>...\" "
                "\"pigment\" — bu hujayra ichidagi narsa (so'z-tuzoq), hujayraning nomi "
                "emas. Zich akademik atama — imloni ehtiyot bilan ko'chiring.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 8.</strong> Rangdan tashqari, sakkizoyoqlar terisining "
                "yana nimasini o'zgartira oladi?</p>"
            ),
            "choices": [
                {"text": "texture (teksturasini)", "is_correct": True},
                {"text": "size (o'lchamini)", "is_correct": False},
                {"text": "temperature (haroratini)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: texture.</mark> "
                "\"<u>In addition to colour</u>, they can change the <u>texture</u> of "
                "their skin.\" \"In addition to\" — signpost (qo'shimcha keladi). "
                "Size/temperature — matnda yo'q (real-world taxmin).</p>"
            ),
        },
        # ── Closing ─────────────────────────────────────────────────────────
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>7–8/8</strong> — ajoyib! To'rt bo'limni ham ishonch bilan yechasiz — imtihonga tayyorsiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>5–6/8</strong> — kuchli natija; xato bo'lgan BO'LIMni aniqlab (1/2/3/4?), o'sha darslarga qayting.</p>"
            "<p style=\"margin:0;\"><strong>4/8 yoki kam</strong> — dovdiramang: cheat-sheet bo'yicha har bo'lim darsini takrorlang. Listening — ko'p tinglash bilan o'sadi.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Band haqida:</strong> haqiqiy testda 40 savol. Taxminan 30/40 ≈ "
            "Band 7, 23/40 ≈ Band 6, 35/40 ≈ Band 8. Har to'g'ri javob qimmatli — 1-2 "
            "bo'limda (osonroq) ball boy bermang.</div>"
        )},
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a reservation</div><div class=\"pp-card-back\">bandlov, joy olib qo'yish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a craft market</div><div class=\"pp-card-back\">hunarmandchilik bozori</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a deadline</div><div class=\"pp-card-back\">muddat, so'nggi sana</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">camouflage</div><div class=\"pp-card-back\">niqoblanish, kamuflyaj</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to imitate</div><div class=\"pp-card-back\">taqlid qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to ambush prey</div><div class=\"pp-card-back\">o'ljaga pistirma qurmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">texture</div><div class=\"pp-card-back\">tekstura, sirt tuzilishi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a stall</div><div class=\"pp-card-back\">rasta, do'koncha</div></div>"
            "</div>"
            "<h2>🎉 Tabriklaymiz — Listening kursini tugatdingiz!</h2>"
            "<p>Bu — IELTS Listening bo'limining <strong>so'nggi darsi</strong>. "
            "Strategiyadan boshlab, 1-bo'lim (forma), 2-bo'lim (monolog + xarita), "
            "3-bo'lim (munozara) va 4-bo'lim (akademik ma'ruza) — <u>to'rt bo'limning "
            "hammasini</u> o'rgandingiz. Endi sizda to'liq quloq-strategiyasi bor!</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Keyingi qadam:</strong> Listening — <u>ko'p tinglash</u> bilan "
            "o'sadigan ko'nikma. Har hafta 2–3 to'liq test tinglang, xatolarni "
            "cheat-sheet bo'yicha tahlil qiling, va inglizcha podkast/video ko'ring "
            "(subtitrsiz!). Har xato — keyingi safar uchun dars. Omad, Band 8! 🚀</p>"
            "<h3>Xulosa — butun kurs bir jumlada</h3>"
            "<ul>"
            "<li>Audio bir marta — oldindan o'qing, javob turini bashorat qiling, o'tkazib yuborsangiz keyingisiga o'ting.</li>"
            "<li>Tuzatish tuzog'i (sorry/actually/instead/not-X-but-Y) — oxirgi variant to'g'ri.</li>"
            "<li>Distraktor: eshitilgan so'z ≠ to'g'ri javob; paraphrase'ni kuting.</li>"
            "<li>Munozara: ismlarni langar qiling, yakuniy kelishuv javob; ma'ruza: signpost so'zlarga ergashing.</li>"
            "<li>Imlo va so'z chegarasi bilan yozing — band mashq bilan o'sadi.</li>"
            "</ul>"
        )},
    ],
},

]
