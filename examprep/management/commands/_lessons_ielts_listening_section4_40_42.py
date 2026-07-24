"""
IELTS Listening lessons 13-15 (orders 40-42) — the "4-bo'lim: Ma'ruza va xulosa
to'ldirish (Section 4 — Academic Lecture, Summary/Note Completion)" topic — fifth
Listening batch, see toc_ielts_listening.txt.

Section 4 = a single-voice academic MONOLOGUE (lecture), denser vocabulary, NO pause
between questions. Vary the single voice across lessons (Woman/Man). Generate:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_section4_40_42.py \
        --out examprep/management/commands/audio/ielts_listening_section4
then import with --audio-dir. Keep speaker names out of the line text — the label only
chooses the voice. See STYLE_GUIDE_IELTS.md §5c.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_SECTION4 = {
    "title":   "4-bo'lim: Ma'ruza va xulosa to'ldirish (Section 4 — Academic Lecture, Summary/Note Completion)",
    "summary": "Akademik ma'ruza (bitta so'zlovchi, pauzasiz): zich ilmiy lug'at, ma'ruza "
               "tuzilishini signpost so'zlar orqali kuzatib, xulosa/eslatma to'ldirish.",
    "icon":    "bi-mortarboard",
    "order":   5,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 13 (order 40 — Intro to Section 4) — AUDIO (Woman lecturer)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION4,
    "title": "IELTS Listening 13: Intro to Section 4 — Academic Lecture, No Pause",
    "summary": "Section 4 formati: universitet ma'ruzasi (bitta so'zlovchi), zich lug'at va pauzasiz oqim; ma'ruza tuzilishini kuzatish.",
    "order": 40,
    "blocks": [
        {"rich_text": (
            "<h2>Section 4 — eng qiyin bo'lim</h2>"
            "<p>4-bo'lim — <strong>akademik ma'ruza</strong>: bitta so'zlovchi "
            "(universitet leksiyasi kabi) biror ilmiy mavzuni tushuntiradi. Bu eng qiyin "
            "bo'lim, ikki sabab bilan: (1) lug'at <u>zichroq</u> va akademik; "
            "(2) <mark style=\"background:#fee2e2;\">savollar orasida to'xtash YO'Q</mark> "
            "— 10 ta savol (31–40) bir zarb bilan yangraydi, o'rtada tanaffus bo'lmaydi.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — pauzasiz oqim:</strong> shu sababli e'tiborni bir "
            "soniya ham yo'qotib bo'lmaydi. Agar bir savolni o'tkazib yuborsangiz, "
            "<u>osilib qolmang</u> — darhol keyingisiga o'ting, aks holda ketma-ket "
            "bir nechtasini boy berasiz.</div>"
        )},
        {"rich_text": (
            "<h3>Ma'ruzaning tuzilishi — sizning tayanchingiz</h3>"
            "<p>Yaxshi xabar: ma'ruza tartibsiz emas. Uning aniq <strong>tuzilishi</strong> "
            "bor va savollar shu tuzilma bo'ylab tartibda keladi:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Kirish (introduction).</strong> "
            "So'zlovchi mavzuni e'lon qiladi va ko'pincha nima haqida gapirishini "
            "sanaydi (\"Today I'll look at three causes...\"). Bu — kelajak xaritasi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Asosiy qismlar (main points).</strong> "
            "Har g'oya signpost so'z bilan boshlanadi (\"Firstly...\", \"The next "
            "factor...\") — keyingi dars bularga bag'ishlangan.</p></div>"
            "<div class=\"pp-step\"><p><strong>Misollar va tafsilotlar.</strong> Har "
            "asosiy fikr misol yoki raqam bilan quvvatlanadi — ko'pincha javob aynan "
            "shu tafsilotda.</p></div>"
            "<div class=\"pp-step\"><p><strong>Xulosa (conclusion).</strong> \"To sum "
            "up...\", \"we'll return to this next week\" — ma'ruza yakuni.</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> boshidagi \"xarita\" jumlasini "
            "(\"Today we'll look at...\") diqqat bilan tinglang — u butun ma'ruzaning "
            "rejasini beradi va savollar tartibini oldindan aytadi.</div>"
        )},
        {
            "audio":        "ielts_l_040_1.mp3",
            "audio_script": [
                ("Woman", "Good morning. Today we'll look at one of the oldest partnerships in human history: the domestication of the dog."),
                ("Woman", "Dogs are descended from the grey wolf, and genetic evidence suggests this process began at least fifteen thousand years ago, long before the domestication of any other animal."),
                ("Woman", "The exact location is still debated, but many researchers now point to Central Asia as the most likely birthplace."),
                ("Woman", "As for why it happened, the leading theory is surprisingly gentle. Rather than humans capturing wolves, the tamer wolves may have approached human camps to scavenge food scraps, gradually losing their fear over generations."),
                ("Woman", "What makes dogs unique among domestic animals is their ability to read human gestures. A dog will follow your pointing finger, something even our closest relative, the chimpanzee, struggles to do."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> \"The Domestication of the "
                "Dog\" ma'ruzasidan parcha. Eslatmalarni to'ldiring:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>LECTURE NOTES — Domestication of the Dog</strong></p>"
                "<p style=\"margin:0 0 4px;\">Ancestor of the dog: the <strong>(1) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">Process began at least <strong>(2) ______</strong> years ago</p>"
                "<p style=\"margin:0 0 4px;\">Most likely birthplace: <strong>(3) ______</strong></p>"
                "<p style=\"margin:0;\">Dogs uniquely can read human <strong>(4) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 4 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Lecturer:</strong> Good morning. Today we'll look at one of the oldest partnerships in human history: the domestication of the dog.<br>"
                "<em style=\"color:#475569;\">Xayrli tong. Bugun insoniyat tarixidagi eng qadimiy hamkorliklardan birini — itni xonakilashtirishni ko'rib chiqamiz.</em></p>"
                "<p><strong>Lecturer:</strong> Dogs are descended from the grey wolf, and genetic evidence suggests this process began at least fifteen thousand years ago, long before the domestication of any other animal.<br>"
                "<em style=\"color:#475569;\">Itlar bo'ri (grey wolf)dan kelib chiqqan va genetik dalillar bu jarayon kamida 15 000 yil oldin, boshqa har qanday hayvondan ancha oldin boshlanganini ko'rsatadi.</em></p>"
                "<p><strong>Lecturer:</strong> The exact location is still debated, but many researchers now point to Central Asia as the most likely birthplace.<br>"
                "<em style=\"color:#475569;\">Aniq joy hali bahsli, lekin ko'p tadqiqotchilar endi eng ehtimoliy vatan sifatida Markaziy Osiyoni ko'rsatishadi.</em></p>"
                "<p><strong>Lecturer:</strong> As for why it happened, the leading theory is surprisingly gentle. Rather than humans capturing wolves, the tamer wolves may have approached human camps to scavenge food scraps, gradually losing their fear over generations.<br>"
                "<em style=\"color:#475569;\">Nega sodir bo'lgani haqida esa, yetakchi nazariya kutilmaganda muloyim. Odamlar bo'rilarni tutgani emas, balki yuvoshroq bo'rilar oziq-ovqat qoldiqlarini yeyish (scavenge) uchun odam lagerlariga yaqinlashgan va avlodlar davomida qo'rquvini yo'qotgan bo'lishi mumkin.</em></p>"
                "<p><strong>Lecturer:</strong> What makes dogs unique among domestic animals is their ability to read human gestures. A dog will follow your pointing finger, something even our closest relative, the chimpanzee, struggles to do.<br>"
                "<em style=\"color:#475569;\">Itlarni boshqa xonaki hayvonlardan ajratib turadigan narsa — inson imo-ishoralarini (gestures) o'qiy olishi. It sizning ko'rsatgich barmog'ingizga ergashadi, buni hatto eng yaqin qarindoshimiz — shimpanze ham qiyinchilik bilan qiladi.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Itning ajdodi (ancestor) nima?</p>"
            ),
            "choices": [
                {"text": "the grey wolf", "is_correct": True},
                {"text": "the chimpanzee", "is_correct": False},
                {"text": "the fox", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: the grey wolf.</mark> "
                "\"Dogs are <u>descended from the grey wolf</u>.\" Chimpanze — bu insonning "
                "yaqin qarindoshi (boshqa kontekst, so'z-tuzoq). \"descended from\" = "
                "kelib chiqqan.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Jarayon kamida necha yil oldin "
                "boshlangan?</p>"
            ),
            "choices": [
                {"text": "50,000", "is_correct": False},
                {"text": "15,000", "is_correct": True},
                {"text": "5,000", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 15,000.</mark> "
                "\"...began at least <u>fifteen thousand</u> years ago.\" \"fifteen\" "
                "(15) va \"fifty\" (50) — urg'udan farqlang (fif-TEEN oxirida kuchli). "
                "\"at least\" = kamida.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Eng ehtimoliy vatan (birthplace) qayer?</p>"
            ),
            "choices": [
                {"text": "Central Asia", "is_correct": True},
                {"text": "North America", "is_correct": False},
                {"text": "Northern Europe", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Central Asia.</mark> "
                "\"...point to <u>Central Asia</u> as the most likely birthplace.\" Aniq "
                "joy hali bahsli, lekin savol \"eng ehtimoliy\"ni so'radi — Central Asia.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Itlar yagona bo'lib insonning nimasini "
                "o'qiy oladi?</p>"
            ),
            "choices": [
                {"text": "human gestures (imo-ishoralar)", "is_correct": True},
                {"text": "human speech (nutq)", "is_correct": False},
                {"text": "human emotions (his-tuyg'ular)", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: human gestures.</mark> "
                "\"...their ability to <u>read human gestures</u>. A dog will follow your "
                "pointing finger.\" \"gestures\" (imo-ishora) — pointing finger misoli "
                "bilan quvvatlangan. Speech/emotions — matnda yo'q (real-world taxmin).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">domestication</div><div class=\"pp-card-back\">xonakilashtirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be descended from</div><div class=\"pp-card-back\">~dan kelib chiqqan bo'lmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">genetic evidence</div><div class=\"pp-card-back\">genetik dalillar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to scavenge</div><div class=\"pp-card-back\">qoldiq/o'laksa yemoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">tame</div><div class=\"pp-card-back\">yuvosh, qo'lga o'rgangan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a gesture</div><div class=\"pp-card-back\">imo-ishora</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a birthplace</div><div class=\"pp-card-back\">vatan, kelib chiqqan joy</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be debated</div><div class=\"pp-card-back\">bahsli bo'lmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Section 4 — akademik ma'ruza (bitta so'zlovchi), zich lug'at, savollar orasida pauza YO'Q.</li>"
            "<li>Savolni o'tkazib yuborsangiz — darhol keyingisiga o'ting, osilib qolmang.</li>"
            "<li>Ma'ruza tuzilishi: kirish (xarita) → asosiy fikrlar → misollar → xulosa.</li>"
            "<li>Boshidagi \"Today we'll look at...\" jumlasi butun rejani beradi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 14 (order 41 — Following lecture structure / signposting) — AUDIO (Man)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION4,
    "title": "IELTS Listening 14: Following Lecture Structure — Signposting Language",
    "summary": "Signpost so'zlar (firstly, in addition, however, as a result) ma'ruza tuzilishini ochib beradi va keyingi javob qachon kelishini aytadi.",
    "order": 41,
    "blocks": [
        {"rich_text": (
            "<h2>Signpost so'zlar — adashmaslik kaliti</h2>"
            "<p>Pauzasiz ma'ruzada adashmaslikning eng kuchli vositasi — <strong>signpost "
            "(yo'l ko'rsatkich) so'zlar</strong>. Ular so'zlovchi qayerdaligini va "
            "g'oyalar bir-biriga qanday bog'lanishini aytadi. Ularni eshitsangiz, "
            "<u>keyingi javob kelayotganini</u> bilasiz.</p>"
        )},
        {"rich_text": (
            "<h3>Signpost so'zlar — turlari bo'yicha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Sanash (order):</strong> <em>firstly, secondly, thirdly, next, finally</em> — yangi bosqich/nuqta boshlanadi (ko'pincha yangi javob!).</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Qo'shish (addition):</strong> <em>in addition, moreover, furthermore, also</em> — oldingi fikrga yana bir narsa qo'shiladi.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Qarama-qarshilik (contrast):</strong> <em>however, on the other hand, nevertheless</em> — fikr o'zgaradi/istisno.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Sabab-natija (cause/effect):</strong> <em>as a result, therefore, consequently, this is why</em> — oqibat keladi.</p>"
            "<p style=\"margin:0;\"><strong>Misol (example):</strong> <em>for instance, such as, to illustrate</em> — dalil/misol keladi.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> \"firstly... secondly... finally\" jarayon yoki "
            "ro'yxat degani — agar eslatmalarda ham raqamlangan bandlar bo'lsa, ular "
            "aynan shu tartibda to'ldiriladi. Signpost = savol sanog'i.</div>"
        )},
        {
            "audio":        "ielts_l_041_1.mp3",
            "audio_script": [
                ("Man", "In this lecture I'll outline the four main stages of the water cycle."),
                ("Man", "Firstly, evaporation: heat from the sun turns water in oceans and lakes into an invisible gas called water vapour, which rises into the atmosphere."),
                ("Man", "Secondly, as this vapour rises, it cools and condenses into tiny droplets that form clouds. This stage is known as condensation."),
                ("Man", "Thirdly comes precipitation: when the droplets grow heavy enough, they fall back to earth as rain, or, in colder conditions, as snow."),
                ("Man", "Finally, in the stage called collection, the water gathers in rivers and oceans or soaks into the ground, and the whole cycle begins again."),
                ("Man", "It's worth noting, however, that the cycle has no real beginning or end. In addition, human activity such as deforestation can disrupt local patterns."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> \"The Water Cycle\" "
                "ma'ruzasi. Signpost so'zlar (firstly, secondly, finally, however) "
                "to'rt bosqichni ajratadi — eslatmalarni to'ldiring:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>THE WATER CYCLE — 4 STAGES</strong></p>"
                "<p style=\"margin:0 0 4px;\">1. Evaporation → water becomes a gas called <strong>(1) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">2. Clouds form — this stage is called <strong>(2) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">3. Precipitation → falls as rain or <strong>(3) ______</strong></p>"
                "<p style=\"margin:0;\">4. The final stage is called <strong>(4) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 4 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Lecturer:</strong> In this lecture I'll outline the four main stages of the water cycle.<br>"
                "<em style=\"color:#475569;\">Bu ma'ruzada suv aylanishining to'rtta asosiy bosqichini bayon qilaman.</em></p>"
                "<p><strong>Lecturer:</strong> Firstly, evaporation: heat from the sun turns water in oceans and lakes into an invisible gas called water vapour, which rises into the atmosphere.<br>"
                "<em style=\"color:#475569;\">Birinchidan, bug'lanish: quyosh issiqligi okean va ko'llardagi suvni ko'rinmas gaz — suv bug'iga (water vapour) aylantiradi, u atmosferaga ko'tariladi.</em></p>"
                "<p><strong>Lecturer:</strong> Secondly, as this vapour rises, it cools and condenses into tiny droplets that form clouds. This stage is known as condensation.<br>"
                "<em style=\"color:#475569;\">Ikkinchidan, bug' ko'tarilgan sari soviydi va mayda tomchilarga aylanib, bulutlarni hosil qiladi. Bu bosqich kondensatsiya deb ataladi.</em></p>"
                "<p><strong>Lecturer:</strong> Thirdly comes precipitation: when the droplets grow heavy enough, they fall back to earth as rain, or, in colder conditions, as snow.<br>"
                "<em style=\"color:#475569;\">Uchinchidan, yog'in keladi: tomchilar yetarlicha og'irlashganda, yerga yomg'ir bo'lib yoki sovuqroq sharoitda qor bo'lib tushadi.</em></p>"
                "<p><strong>Lecturer:</strong> Finally, in the stage called collection, the water gathers in rivers and oceans or soaks into the ground, and the whole cycle begins again.<br>"
                "<em style=\"color:#475569;\">Nihoyat, yig'ilish (collection) deb ataladigan bosqichda suv daryo va okeanlarga to'planadi yoki yerga singadi va butun tsikl yana boshlanadi.</em></p>"
                "<p><strong>Lecturer:</strong> It's worth noting, however, that the cycle has no real beginning or end. In addition, human activity such as deforestation can disrupt local patterns.<br>"
                "<em style=\"color:#475569;\">Shuni ta'kidlash joizki, ammo, tsiklning haqiqiy boshi yoki oxiri yo'q. Bundan tashqari, o'rmonlarni kesish kabi inson faoliyati mahalliy naqshlarni buzishi mumkin.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Birinchi bosqichda (evaporation) suv qanday "
                "gazga aylanadi?</p>"
            ),
            "choices": [
                {"text": "water vapour", "is_correct": True},
                {"text": "oxygen", "is_correct": False},
                {"text": "steam", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: water vapour.</mark> "
                "\"Firstly, evaporation: ... an invisible gas called <u>water "
                "vapour</u>.\" \"Firstly\" signali birinchi javob kelayotganini aytdi. "
                "\"steam\" — matnda yo'q (o'z so'zingiz).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Bulutlar hosil bo'ladigan bosqich qanday "
                "ataladi?</p>"
            ),
            "choices": [
                {"text": "evaporation", "is_correct": False},
                {"text": "condensation", "is_correct": True},
                {"text": "collection", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: condensation.</mark> "
                "\"Secondly, ... form clouds. This stage is known as <u>condensation</u>.\" "
                "\"Secondly\" = ikkinchi javob. Imloni aynan ko'chiring: "
                "c-o-n-d-e-n-s-a-t-i-o-n.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Sovuqroq sharoitda yog'in nima bo'lib "
                "tushadi?</p>"
            ),
            "choices": [
                {"text": "rain", "is_correct": False},
                {"text": "snow", "is_correct": True},
                {"text": "hail", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: snow.</mark> "
                "\"...fall back to earth as rain, or, <u>in colder conditions, as "
                "snow</u>.\" Eslatmada \"rain\" allaqachon berilgan — demak ikkinchisi "
                "(snow) so'raladi. \"hail\" (do'l) — matnda yo'q.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> To'rtinchi (oxirgi) bosqich qanday "
                "ataladi?</p>"
            ),
            "choices": [
                {"text": "precipitation", "is_correct": False},
                {"text": "collection", "is_correct": True},
                {"text": "condensation", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: collection.</mark> "
                "\"<u>Finally</u>, in the stage called <u>collection</u>...\" \"Finally\" "
                "= oxirgi signpost, oxirgi javob. Signpost so'zlarni kuzatib, to'rt "
                "bosqichni tartib bilan to'ldirdingiz.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary (signpost + water cycle)</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">firstly / finally</div><div class=\"pp-card-back\">birinchidan / nihoyat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">in addition / moreover</div><div class=\"pp-card-back\">bundan tashqari / qolaversa</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">however</div><div class=\"pp-card-back\">ammo, biroq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">as a result / consequently</div><div class=\"pp-card-back\">natijada</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">evaporation</div><div class=\"pp-card-back\">bug'lanish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">condensation</div><div class=\"pp-card-back\">kondensatsiya, quyuqlashish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">precipitation</div><div class=\"pp-card-back\">yog'in</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to soak into</div><div class=\"pp-card-back\">~ga singmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Signpost so'zlar ma'ruza tuzilishini ochib beradi va keyingi javobni oldindan aytadi.</li>"
            "<li>Sanash (firstly/finally), qo'shish (in addition), qarshilik (however), natija (as a result), misol (for instance).</li>"
            "<li>Raqamlangan eslatmalar signpost tartibida to'ldiriladi — signpost = savol sanog'i.</li>"
            "<li>\"Biri berilgan\" (rain) bandlar qolganini (snow) tasdiqlaydi; imloni aniq ko'chiring.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 15 (order 42 — Summary/Note Completion, dense vocab, full practice) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION4,
    "title": "IELTS Listening 15: Summary/Note Completion — Dense Academic Vocabulary (Full Practice)",
    "summary": "To'liq Section 4 amaliyoti: zich ilmiy ma'ruza (bioluminescence), xulosa/eslatma to'ldirish — so'z turini bashorat, paraphrase va imlo.",
    "order": 42,
    "blocks": [
        {"rich_text": (
            "<h2>To'liq amaliyot: zich akademik ma'ruza</h2>"
            "<p>Endi hammasi birga: haqiqiy Section 4 kabi zich ilmiy lug'atli ma'ruza va "
            "xulosa/eslatma to'ldirish. Usullarni eslang: so'z turini bashorat qiling "
            "(ot? son? sifat?), paraphrase'ni kuting, va javobni <u>imlo bilan</u> aynan "
            "ko'chiring.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> avval eslatmalarni o'qib, har bo'sh joyga qanday "
            "so'z kerakligini belgilang (raqam? termin? sifat?). Zich lug'atda "
            "adashmaslik uchun bu bashorat juda muhim. 5 savol — bitta ma'ruzada, "
            "tartib bilan.</div>"
        )},
        {
            "audio":        "ielts_l_042_1.mp3",
            "audio_script": [
                ("Woman", "Today's topic is bioluminescence, the production of light by living organisms."),
                ("Woman", "It's astonishingly common in the ocean. By some estimates, up to ninety per cent of deep-sea creatures can produce their own light."),
                ("Woman", "The light comes from a chemical reaction involving a molecule called luciferin, which, when combined with oxygen, releases energy as light rather than heat. This is why biologists call it 'cold light' — almost none of the energy is wasted as heat."),
                ("Woman", "Organisms use bioluminescence for three main purposes. The first is defence: some squid eject a cloud of glowing liquid to confuse predators, much as an octopus uses ink."),
                ("Woman", "The second purpose is to attract prey. The anglerfish, for example, dangles a glowing lure in front of its mouth."),
                ("Woman", "And the third is communication, particularly to find a mate in the darkness. Interestingly, most of this light is blue-green, because that colour travels furthest through seawater."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> \"Bioluminescence\" "
                "ma'ruzasi. Xulosani to'ldiring:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>SUMMARY — Bioluminescence</strong></p>"
                "<p style=\"margin:0 0 4px;\">Up to <strong>(1) ______</strong> % of deep-sea creatures can make light.</p>"
                "<p style=\"margin:0 0 4px;\">Light comes from a molecule called <strong>(2) ______</strong> combined with oxygen.</p>"
                "<p style=\"margin:0 0 4px;\">Called 'cold light' because little energy is lost as <strong>(3) ______</strong>.</p>"
                "<p style=\"margin:0 0 4px;\">Defence: squid eject a glowing <strong>(4) ______</strong> to confuse predators.</p>"
                "<p style=\"margin:0;\">Most bioluminescent light is <strong>(5) ______</strong> in colour.</p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 5 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Lecturer:</strong> Today's topic is bioluminescence, the production of light by living organisms.<br>"
                "<em style=\"color:#475569;\">Bugungi mavzu — biolyuminessensiya, ya'ni tirik organizmlar tomonidan yorug'lik ishlab chiqarish.</em></p>"
                "<p><strong>Lecturer:</strong> It's astonishingly common in the ocean. By some estimates, up to ninety per cent of deep-sea creatures can produce their own light.<br>"
                "<em style=\"color:#475569;\">U okeanda hayratlanarli darajada keng tarqalgan. Ba'zi baholarga ko'ra, chuqur dengiz jonzotlarining 90 foizigacha o'z yorug'ligini ishlab chiqara oladi.</em></p>"
                "<p><strong>Lecturer:</strong> The light comes from a chemical reaction involving a molecule called luciferin, which, when combined with oxygen, releases energy as light rather than heat. This is why biologists call it 'cold light' — almost none of the energy is wasted as heat.<br>"
                "<em style=\"color:#475569;\">Yorug'lik lyutsiferin (luciferin) degan molekula ishtirokidagi kimyoviy reaksiyadan kelib chiqadi; u kislorod bilan birlashganda energiyani issiqlik emas, yorug'lik sifatida chiqaradi. Shuning uchun biologlar uni 'sovuq yorug'lik' deyishadi — energiyaning deyarli hech qismi issiqlik sifatida behuda ketmaydi.</em></p>"
                "<p><strong>Lecturer:</strong> Organisms use bioluminescence for three main purposes. The first is defence: some squid eject a cloud of glowing liquid to confuse predators, much as an octopus uses ink.<br>"
                "<em style=\"color:#475569;\">Organizmlar biolyuminessensiyani uch asosiy maqsadda ishlatadi. Birinchisi — himoya: ba'zi kalmarlar yirtqichlarni chalg'itish uchun yaltiroq suyuqlik (liquid) bulutini chiqaradi, xuddi sakkizoyoq siyoh ishlatgani kabi.</em></p>"
                "<p><strong>Lecturer:</strong> The second purpose is to attract prey. The anglerfish, for example, dangles a glowing lure in front of its mouth.<br>"
                "<em style=\"color:#475569;\">Ikkinchi maqsad — o'ljani jalb qilish. Masalan, angler-baliq og'zi oldida yaltiroq hilpiraydigan tuzoq (lure) osiltirib turadi.</em></p>"
                "<p><strong>Lecturer:</strong> And the third is communication, particularly to find a mate in the darkness. Interestingly, most of this light is blue-green, because that colour travels furthest through seawater.<br>"
                "<em style=\"color:#475569;\">Uchinchisi — muloqot, ayniqsa zulmatda juft topish. Qizig'i, bu yorug'likning ko'p qismi ko'k-yashil (blue-green), chunki bu rang dengiz suvida eng uzoqqa boradi.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Chuqur dengiz jonzotlarining necha foizi "
                "yorug'lik ishlab chiqara oladi?</p>"
            ),
            "choices": [
                {"text": "19%", "is_correct": False},
                {"text": "90%", "is_correct": True},
                {"text": "9%", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 90%.</mark> \"up to "
                "<u>ninety</u> per cent of deep-sea creatures...\" \"ninety\" (90) va "
                "\"nineteen\" (19) — urg'udan farqlang (nine-TEEN oxirida kuchli). "
                "\"up to\" = gacha.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Yorug'lik qaysi molekula ishtirokida "
                "hosil bo'ladi?</p>"
            ),
            "choices": [
                {"text": "oxygen", "is_correct": False},
                {"text": "luciferin", "is_correct": True},
                {"text": "chlorophyll", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: luciferin.</mark> "
                "\"...a molecule called <u>luciferin</u>, which, when combined with "
                "oxygen...\" Diqqat: oxygen ham eslatiladi, lekin u molekula bilan "
                "<u>birlashadigan</u> narsa — savol molekula nomini so'raydi (luciferin). "
                "Imloni ehtiyot bo'lib ko'chiring.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Nega u 'cold light' deb ataladi? Energiya "
                "deyarli ______ sifatida ketmaydi.</p>"
            ),
            "choices": [
                {"text": "heat", "is_correct": True},
                {"text": "light", "is_correct": False},
                {"text": "sound", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: heat.</mark> "
                "\"...releases energy as light rather than <u>heat</u>... almost none of "
                "the energy is wasted as <u>heat</u>.\" Shuning uchun 'cold' (sovuq). "
                "\"light\" — bu chiqadigan narsa (teskarisi). Bashorat: bo'sh joyga ot "
                "kerak edi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Himoya uchun kalmarlar nimani chiqaradi? "
                "Yaltiroq ______.</p>"
            ),
            "choices": [
                {"text": "ink", "is_correct": False},
                {"text": "liquid", "is_correct": True},
                {"text": "gas", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: liquid.</mark> "
                "\"...squid eject a cloud of glowing <u>liquid</u> to confuse "
                "predators...\" \"ink\" (siyoh) — bu <u>octopus</u> (sakkizoyoq) "
                "misolida ishlatiladi (\"much as an octopus uses ink\") — kalmar emas. "
                "So'z-tuzoqqa tushmang: savol kalmar (squid) haqida.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> Biolyuminessent yorug'lik asosan qaysi "
                "rangda bo'ladi?</p>"
            ),
            "choices": [
                {"text": "red", "is_correct": False},
                {"text": "blue-green", "is_correct": True},
                {"text": "yellow", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: blue-green.</mark> "
                "\"...most of this light is <u>blue-green</u>, because that colour travels "
                "furthest through seawater.\" Sabab ham berildi (dengiz suvida eng "
                "uzoqqa boradi). \"blue-green\" — chiziqcha bilan bitta javob.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — zo'r! Zich akademik ma'ruzani ham ushlaysiz — Section 4 tayyor.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3–4/5</strong> — yaxshi; so'z-tuzoq (ink vs liquid, oxygen vs luciferin) savollarini qayta tinglang.</p>"
            "<p style=\"margin:0;\"><strong>2/5 yoki kam</strong> — 13–14-darslarga qaytib, ma'ruza tuzilishi va so'z turini bashorat qilishni takrorlang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">bioluminescence</div><div class=\"pp-card-back\">biolyuminessensiya (tirik yorug'lik)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a molecule</div><div class=\"pp-card-back\">molekula</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a chemical reaction</div><div class=\"pp-card-back\">kimyoviy reaksiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a predator / prey</div><div class=\"pp-card-back\">yirtqich / o'lja</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to eject</div><div class=\"pp-card-back\">chiqarib otmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a lure</div><div class=\"pp-card-back\">tuzoq, o'ljani jalb qiluvchi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to confuse</div><div class=\"pp-card-back\">chalg'itmoq, chalkashtirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to find a mate</div><div class=\"pp-card-back\">juft topmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Section 4 = zich akademik ma'ruza; so'z turini oldindan bashorat qilib tinglang.</li>"
            "<li>So'z-tuzoqqa tushmang: ink → octopus, liquid → squid; oxygen birlashadigan narsa, luciferin — molekula.</li>"
            "<li>Raqamlar: 90 vs 19 ni urg'udan farqlang; chiziqchali javob (blue-green) bitta so'z.</li>"
            "<li>Javobni imlo bilan aynan ko'chiring; \"biri berilgan\" bandlar qolganini tasdiqlaydi.</li>"
            "</ul>"
        )},
    ],
},

]
