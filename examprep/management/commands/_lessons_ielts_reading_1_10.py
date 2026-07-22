"""
IELTS Reading lessons 1-4 (topic: Strategiya va format) + lesson 10
(topic: Haqiqat / Yolg'on / Berilmagan) — first batch, see toc_ielts_reading.txt.
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
    "summary": "IELTS Reading imtihoni qanday tuzilgan va vaqtni qanday boshqarish kerak.",
    "icon":    "bi-compass",
    "order":   1,
}

TOPIC_TFNG = {
    "title":   "Haqiqat / Yolg'on / Berilmagan (True / False / Not Given)",
    "summary": "Faktlarga asoslangan bayonotlarni TRUE / FALSE / NOT GIVEN sifatida aniqlash.",
    "icon":    "bi-check2-square",
    "order":   2,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 1
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Reading 1: How IELTS Reading Works — 3 Passages, 60 Minutes, 40 Questions",
    "summary": "IELTS Reading imtihonining umumiy tuzilishi, vaqt taqsimoti va baholash tizimi.",
    "order": 1,
    "blocks": [
        {"rich_text": (
            "<h2>IELTS Reading imtihoni qanday ishlaydi?</h2>"
            "<p>Bu bo'lim IELTS Reading (o'qish) imtihonining <strong>umumiy xaritasi</strong>. "
            "Har bir keyingi darsda alohida savol turlarini chuqur o'rganamiz, lekin avval "
            "<mark>qanday o'yin maydonida</mark> ishlayotganingizni bilishingiz kerak — "
            "chunki formatni bilmasdan strategiya qurib bo'lmaydi.</p>"
        )},
        {"rich_text": (
            "<h3>Asosiy raqamlar</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>3 ta parcha (passage)</strong> — har biri "
            "taxminan 700–1000 so'z. Odatda 1-parcha eng oson, 3-parcha eng qiyin "
            "(Academic modulda).</p></div>"
            "<div class=\"pp-step\"><p><strong>40 ta savol</strong> — parchalar bo'ylab "
            "taqsimlangan (odatda har birida ~13–14 ta savol).</p></div>"
            "<div class=\"pp-step\"><p><strong>60 daqiqa</strong> — javoblarni ko'chirish "
            "uchun <u>qo'shimcha vaqt yo'q</u> (Listening'dan farqli o'laroq)! Javoblarni "
            "to'g'ridan-to'g'ri javob varag'iga yozing.</p></div>"
            "<div class=\"pp-step\"><p><strong>Manfiy ball yo'q</strong> — noto'g'ri javob "
            "uchun ball ayirilmaydi. Shuning uchun <mark style=\"background:#dcfce7;\">hech "
            "qachon savolni bo'sh qoldirmang</mark> — taxmin qiling!</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Ball tizimi (Band Score)</h3>"
            "<p>40 savoldan nechtasiga to'g'ri javob berganingiz (<strong>raw score</strong>) "
            "9 balllik <strong>Band Score</strong> shkalasiga aylantiriladi. Taxminiy "
            "ko'rsatkich (Academic modul uchun):</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\">39–40 to'g'ri ≈ <strong>Band 9</strong></p>"
            "<p style=\"margin:0 0 6px;\">30–32 to'g'ri ≈ <strong>Band 7</strong></p>"
            "<p style=\"margin:0 0 6px;\">23–26 to'g'ri ≈ <strong>Band 6</strong></p>"
            "<p style=\"margin:0;\">15–18 to'g'ri ≈ <strong>Band 5</strong></p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> bu raqamlar taxminiy — imtihondan imtihonga biroz "
            "farq qilishi mumkin, chunki har bir test o'zining qiyinlik darajasiga qarab "
            "kalibrlanadi.</div>"
        )},
        {
            "rich_text": "<p><strong>Amaliyot 1.</strong> IELTS Reading imtihonida javoblarni ko'chirish uchun qo'shimcha vaqt bormi?</p>",
            "choices": [
                {"text": "Ha, 10 daqiqa qo'shimcha vaqt beriladi", "is_correct": False},
                {"text": "Yo'q, 60 daqiqa ichida hammasi — javob varag'iga to'g'ridan-to'g'ri yozish kerak", "is_correct": True},
                {"text": "Ha, lekin faqat General Training modulda", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Yo'q, qo'shimcha vaqt yo'q.</mark> "
                "Bu qoida Listening'dan farq qiladi — Listeningda 10 daqiqa ko'chirish vaqti bor, "
                "lekin Readingda yo'q. Shuning uchun ba'zi talabalar birinchi javob qog'ozida "
                "belgilab, keyin ko'chirishni rejalashtiradi — lekin bu <strong>xavfli</strong>, "
                "chunki vaqt tugab qolishi mumkin. Eng yaxshisi — har savolni <u>darhol</u> javob "
                "varag'iga yozish.</p>"
            ),
        },
        {
            "rich_text": "<p><strong>Amaliyot 2.</strong> Agar siz 40 savoldan 24 tasiga to'g'ri javob bersangiz, taxminan qaysi banddasiz (Academic)?</p>",
            "choices": [
                {"text": "Band 9", "is_correct": False},
                {"text": "Band 6", "is_correct": True},
                {"text": "Band 4", "is_correct": False},
            ],
            "explanation": (
                "<p>Yuqoridagi jadvalga ko'ra, 23–26 to'g'ri javob taxminan <strong>Band 6</strong>ga "
                "to'g'ri keladi. Bu ko'plab universitetlar talab qiladigan minimal darajaga yaqin — "
                "shuning uchun bu maqsad ko'plab talabalar uchun realistik boshlang'ich nishondir.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">passage</div><div class=\"pp-card-back\">matn parchasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">raw score</div><div class=\"pp-card-back\">to'g'ri javoblar soni (xom ball)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">band score</div><div class=\"pp-card-back\">9 balllik yakuniy baho</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">answer sheet</div><div class=\"pp-card-back\">javob varag'i</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">negative marking</div><div class=\"pp-card-back\">noto'g'ri javob uchun ball ayirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">time management</div><div class=\"pp-card-back\">vaqtni boshqarish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">question type</div><div class=\"pp-card-back\">savol turi</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>3 parcha, 40 savol, 60 daqiqa — javob ko'chirish uchun qo'shimcha vaqt yo'q.</li>"
            "<li>Manfiy ball yo'q — hech qachon savolni bo'sh qoldirmang.</li>"
            "<li>Band 6 uchun taxminan 23–26 to'g'ri javob kifoya.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 2
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Reading 2: Skimming vs Scanning — When to Use Which",
    "summary": "Tez o'qish (skimming) va aniq ma'lumot qidirish (scanning) texnikalari o'rtasidagi farq.",
    "order": 2,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki xil o'qish texnikasi</h2>"
            "<p>IELTS Reading'da <strong>hech qachon matnni so'zma-so'z, boshidan oxirigacha "
            "o'qimaysiz</strong> — vaqt yetmaydi. Buning o'rniga ikki maxsus texnikadan "
            "foydalanasiz: <mark style=\"background:#dbeafe;\">skimming</mark> va "
            "<mark style=\"background:#dbeafe;\">scanning</mark>. Ular boshqa-boshqa "
            "maqsadlarga xizmat qiladi.</p>"
        )},
        {"rich_text": (
            "<h3>Skimming — umumiy g'oyani tez tushunish</h3>"
            "<p><strong>Skimming</strong> — matnni <em>tez, yuzaki</em> o'qib, uning "
            "<u>asosiy g'oyasini (main idea)</u> tushunish. Har bir so'zni o'qimaysiz — "
            "ko'zingiz sahifa bo'ylab \"suzadi\".</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam:</strong> Sarlavha (title) va "
            "kichik sarlavhalarni (subheadings) o'qing.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam:</strong> Har bir paragrafning "
            "<u>birinchi va oxirgi jumlasini</u> o'qing — asosiy fikr ko'pincha shu yerda.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam:</strong> Qolgan qismni tezda "
            "ko'z bilan \"skanerlab\" o'ting — grafiklar, raqamlar, katta harflar bilan "
            "yozilgan so'zlarga e'tibor bering.</p></div>"
            "</div>"
            "<p><strong>Qachon ishlatiladi:</strong> Matching Headings, main idea/summary "
            "savollarida va parchani birinchi marta ko'rib chiqishda.</p>"
        )},
        {"rich_text": (
            "<h3>Scanning — aniq ma'lumotni topish</h3>"
            "<p><strong>Scanning</strong> — matnda <u>bitta aniq narsani</u> (sana, ism, "
            "raqam, atama) topish uchun ko'z bilan tezda \"skanerlash\". G'oyani tushunish "
            "shart emas — faqat kalit so'zni (yoki uning sinonimini) topish kerak.</p>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna:</strong> Savolda \"in 1969\" bo'lsa, matnda aynan shu "
            "raqamni qidirasiz — atrofidagi jumlani o'qib, javobni tekshirasiz.</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> IELTS kamdan-kam hollarda savoldagi so'zni matnda "
            "aynan o'sha shaklda beradi — ko'pincha <mark>sinonim (paraphrase)</mark> "
            "ishlatiladi. Masalan, savolda \"increase\" bo'lsa, matnda \"rise\", \"grow\", "
            "yoki \"a sharp climb\" bo'lishi mumkin.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna: bitta paragrafni solishtiring</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"Urban beekeeping has grown rapidly across European "
            "cities since 2010, driven largely by concerns over declining bee populations. "
            "In London alone, the number of registered hives more than tripled between "
            "2010 and 2018.\"</p>"
            "</div>"
            "<p><strong>Skimming</strong> bilan siz shuni tushunasiz: <em>\"bu paragraf "
            "shahar arichiligining o'sishi haqida\"</em>. <strong>Scanning</strong> bilan "
            "siz \"2018\" yoki \"tripled\" kabi aniq so'zlarni qidirasiz — agar savolda "
            "\"how much did the number of hives increase by 2018?\" deyilgan bo'lsa.</p>"
        )},
        {
            "rich_text": "<p><strong>Amaliyot 1.</strong> Matching Headings turidagi savolni yechish uchun asosan qaysi texnikadan foydalanasiz?</p>",
            "choices": [
                {"text": "Scanning — aniq bir sonani qidirish", "is_correct": False},
                {"text": "Skimming — har bir paragrafning asosiy g'oyasini tushunish", "is_correct": True},
                {"text": "Ikkalasi ham kerak emas, matnni to'liq o'qish kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Skimming.</mark> "
                "Matching Headings savolida sizga paragrafning <u>umumiy mavzusi</u> kerak, "
                "aniq raqam yoki ism emas — shuning uchun har bir paragrafni tez skim qilib, "
                "asosiy g'oyani ushlab olish yetarli. Bu darsni keyinroq alohida chuqur "
                "o'rganamiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Yuqoridagi paragrafda "
                "(\"Urban beekeeping...\") savol shunday: <em>\"By what year had the number "
                "of hives in London more than tripled?\"</em> Qanday strategiya bilan "
                "javobni topasiz?</p>"
            ),
            "choices": [
                {"text": "Paragrafni boshidan oxirigacha diqqat bilan tarjima qilib o'qiyman", "is_correct": False},
                {"text": "\"tripled\" yoki unga yaqin so'zni (masalan raqam/yil) scan qilib topaman", "is_correct": True},
                {"text": "Sarlavhaga qarab javobni taxmin qilaman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: scan qilish.</mark> "
                "Savol aniq bir faktni (yil) so'ramoqda — bu <strong>scanning</strong> vazifasi. "
                "\"tripled\" so'zi atrofida \"between 2010 and 2018\" jumlasi bor — javob: "
                "<strong>2018</strong>. Matnni to'liq tarjima qilish vaqtni behuda sarflaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">skimming</div><div class=\"pp-card-back\">tez o'qib, umumiy g'oyani tushunish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">scanning</div><div class=\"pp-card-back\">aniq ma'lumotni ko'z bilan qidirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">main idea</div><div class=\"pp-card-back\">asosiy g'oya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">topic sentence</div><div class=\"pp-card-back\">paragrafning asosiy jumlasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">paraphrase</div><div class=\"pp-card-back\">boshqacha so'zlar bilan aytish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">synonym</div><div class=\"pp-card-back\">sinonim, ma'nodosh so'z</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">keyword</div><div class=\"pp-card-back\">kalit so'z</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Skimming = umumiy g'oya uchun (sarlavha + har paragrafning 1- va oxirgi jumlasi).</li>"
            "<li>Scanning = aniq fakt uchun (sana, ism, raqam) — kalit so'z yoki sinonimini qidiring.</li>"
            "<li>IELTS savol so'zlari matnda deyarli har doim <mark>paraphrase</mark> qilingan bo'ladi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 3
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Reading 3: Managing Time Across Three Passages (the 20-Minute Rule)",
    "summary": "60 daqiqani 3 ta parcha o'rtasida qanday taqsimlash va vaqt nazoratini saqlash.",
    "order": 3,
    "blocks": [
        {"rich_text": (
            "<h2>Nega vaqt eng katta dushman?</h2>"
            "<p>Ko'pchilik talabalar IELTS Readingdan past ball olishining sababi "
            "<u>ingliz tilini bilmasligi emas</u> — balki <strong>vaqt yetishmasligi</strong>. "
            "Ular 1- va 2-parchada juda ko'p vaqt sarflab, 3-parchaga (eng qiyin qism) "
            "atigi 5–10 daqiqa qoldiradi. Bu darsda vaqtni to'g'ri taqsimlash rejasini "
            "o'rganamiz.</p>"
        )},
        {"rich_text": (
            "<h3>\"20 daqiqa qoidasi\" — va nega u mukammal emas</h3>"
            "<p>Matematik jihatdan: 60 daqiqa ÷ 3 parcha = <strong>har biriga 20 daqiqa</strong>. "
            "Bu yaxshi boshlang'ich nuqta, lekin Academic modulda 3-parcha odatda eng uzun va "
            "eng qiyin bo'ladi. Shuning uchun ko'p o'qituvchilar quyidagi taqsimotni tavsiya "
            "qiladi:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-parcha:</strong> ~17 daqiqa (eng oson — "
            "tezroq tugatib, keyingi qismlarga vaqt qoldiring).</p></div>"
            "<div class=\"pp-step\"><p><strong>2-parcha:</strong> ~20 daqiqa (o'rta "
            "qiyinlik).</p></div>"
            "<div class=\"pp-step\"><p><strong>3-parcha:</strong> ~23 daqiqa (eng qiyin — "
            "ko'proq vaqt kerak bo'ladi).</p></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> bu — tavsiya, qonun emas! Mashq paytida <u>o'zingizning</u> "
            "kuchli va zaif tomonlaringizni aniqlab, shaxsiy vaqt rejangizni tuzing.</div>"
        )},
        {"rich_text": (
            "<h3>Nazorat nuqtalari (checkpoints)</h3>"
            "<p>Imtihon paytida soatga faqat oxirida qaramang — bu kech bo'lishi mumkin. "
            "Buning o'rniga o'zingizga <strong>nazorat nuqtalari</strong> qo'ying:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\">17-daqiqada → 1-parcha tugagan bo'lishi kerak.</p>"
            "<p style=\"margin:0 0 6px;\">37-daqiqada → 2-parcha tugagan bo'lishi kerak.</p>"
            "<p style=\"margin:0;\">60-daqiqada → 3-parcha va barcha javoblar javob "
            "varag'ida bo'lishi kerak.</p>"
            "</div>"
            "<p>Agar nazorat nuqtasida orqada qolsangiz — qolgan qiyin savollarni "
            "<mark>taxmin qiling va o'ting</mark>, keyingi parchaga o'ting. Bitta qiyin "
            "savolga 5 daqiqa sarflab, keyingi 13 ta oson savolni yo'qotmang.</p>"
        )},
        {"rich_text": (
            "<h3>Qaysi tartibda ishlash kerak?</h3>"
            "<p>Ko'pchilik parchalarni <strong>tartib bo'yicha (1 → 2 → 3)</strong> "
            "bajaradi — chunki savollar odatda matn tartibiga mos keladi (Matching "
            "Headings va Matching Features bundan mustasno bo'lishi mumkin). Ba'zi "
            "talabalar esa avval o'zi <em>kuchli</em> bo'lgan savol turini qidiradi. "
            "Ikkalasi ham to'g'ri — lekin <u>mashq paytida sinab ko'rib, o'zingizga "
            "mos usulni toping</u> va imtihonda o'zgartirmang.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Siz 1-parchani 25 daqiqada tugatdingiz "
                "(rejadan 8 daqiqa ko'p). Yuqoridagi checkpoint rejasiga ko'ra, buni "
                "sezganingizdan keyin eng to'g'ri qadam nima?</p>"
            ),
            "choices": [
                {"text": "1-parchaga qaytib, javoblarni yana tekshiraman", "is_correct": False},
                {"text": "Darhol 2-parchaga o'taman va qolgan vaqtni tezroq sarflashga harakat qilaman", "is_correct": True},
                {"text": "Imtihonni to'xtatib, dam olaman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: darhol keyingi "
                "parchaga o'tish.</mark> Orqaga qaytib vaqtni yo'qotish — eng katta xato. "
                "8 daqiqalik kechikishni <u>tezlashtirib</u> qoplashga harakat qiling: "
                "masalan, 2-parchada scanning'ga ko'proq, chuqur o'qishga kamroq vaqt "
                "ajrating.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> 3-parchada bitta Matching Sentence "
                "Endings savoli sizni 6 daqiqa ushlab turdi va hali ham javobga "
                "ishonchingiz komil emas. Nima qilish kerak?</p>"
            ),
            "choices": [
                {"text": "Eng mantiqiy ko'ringan variantni belgilab, keyingi savolga o'taman", "is_correct": True},
                {"text": "Javobni topguncha davom etaman, chunki bo'sh qoldirish mumkin emas", "is_correct": False},
                {"text": "Savolni butunlay tashlab, javob varag'ida bo'sh qoldiraman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: eng mantiqiy "
                "variantni belgilab, davom eting.</mark> Esingizda bo'lsin — 1-darsda "
                "o'rgangandek, <strong>manfiy ball yo'q</strong>, shuning uchun taxmin "
                "qilingan javob har doim bo'sh javobdan yaxshiroq. Bitta qiyin savolga "
                "6 daqiqa sarflash — orqadagi 10+ oson savolni xavf ostiga qo'yadi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">time budget</div><div class=\"pp-card-back\">vaqt taqsimoti</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">checkpoint</div><div class=\"pp-card-back\">nazorat nuqtasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">pacing</div><div class=\"pp-card-back\">tezlikni boshqarish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to fall behind</div><div class=\"pp-card-back\">rejadan orqada qolmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to guess and move on</div><div class=\"pp-card-back\">taxmin qilib, davom etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">strongest section</div><div class=\"pp-card-back\">eng kuchli bo'lgan qism</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Boshlang'ich taqsimot: 1-parcha ~17, 2-parcha ~20, 3-parcha ~23 daqiqa.</li>"
            "<li>Har parchadan keyin checkpoint qo'ying — orqada qolsangiz, tezlashtiring.</li>"
            "<li>Manfiy ball yo'q — qiyin savolga vaqt yo'qotgandan ko'ra, taxmin qilib o'ting.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 4
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_STRATEGY,
    "title": "IELTS Reading 4: Academic vs General Training — What Actually Differs",
    "summary": "IELTS Reading'ning Academic va General Training modullari o'rtasidagi haqiqiy farqlar.",
    "order": 4,
    "blocks": [
        {"rich_text": (
            "<h2>Ikki modul, bitta format</h2>"
            "<p>IELTS'ning ikki turi bor: <strong>Academic</strong> (universitetga kirish "
            "uchun) va <strong>General Training</strong> — <em>GT</em> (ish, migratsiya, "
            "kollej uchun — masalan, Buyuk Britaniya, Avstraliya, Kanadaga ariza berishda). "
            "Reading bo'limida <u>format bir xil</u> — 3 bo'lim, 40 savol, 60 daqiqa — "
            "lekin <u>matn turlari boshqacha</u>.</p>"
        )},
        {"rich_text": (
            "<h3>Academic Reading — nima o'qiladi?</h3>"
            "<p>Uchala parcha ham <strong>akademik manbalardan</strong>: jurnal maqolalari, "
            "kitob boblari, universitet darsliklari uslubidagi matnlar. Mavzular: fan, "
            "tarix, jamiyat, texnologiya, ekologiya va h.k. Til <mark>rasmiy va "
            "murakkab</mark> — universitet darajasidagi lug'at va grammatikani talab qiladi.</p>"
        )},
        {"rich_text": (
            "<h3>General Training Reading — nima o'qiladi?</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-bo'lim:</strong> 2–3 ta qisqa, "
            "kundalik hayotga oid matn (e'lonlar, reklamalar, jadvallar, ko'rsatmalar).</p></div>"
            "<div class=\"pp-step\"><p><strong>2-bo'lim:</strong> 2 ta ish/ta'lim bilan "
            "bog'liq matn (ish tavsifi, ish shartnomasi qoidalari, kurs ma'lumotlari).</p></div>"
            "<div class=\"pp-step\"><p><strong>3-bo'lim:</strong> 1 ta uzunroq, umumiy "
            "qiziqish uyg'otadigan matn — Academic'ning 3-bo'limiga uslubi bo'yicha "
            "yaqinroq.</p></div>"
            "</div>"
            "<p>GT matnlari 1- va 2-bo'limda <u>ancha sodda va qisqaroq</u> — bu Academic'ga "
            "nisbatan kattaroq farq.</p>"
        )},
        {"rich_text": (
            "<h3>Savol turlari — deyarli bir xil</h3>"
            "<p>Yaxshi xabar: <strong>savol turlari ikkala modulda ham bir xil</strong> "
            "(True/False/Not Given, Matching Headings, Sentence Completion va h.k.) — bu "
            "darslarda o'rgangan barcha usullaringiz ikkala modulda ham ishlaydi. Farq "
            "faqat <u>matnning murakkabligi va mavzusida</u>.</p>"
        )},
        {"rich_text": (
            "<h3>Band hisoblash — kichik, lekin muhim farq</h3>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> GT matnlari sodda bo'lgani uchun, xuddi shu "
            "Band ballga erishish uchun GT'da <u>ko'proq</u> to'g'ri javob kerak bo'ladi. "
            "Masalan, Band 7 uchun Academic'da ~30 to'g'ri javob kifoya bo'lsa, GT'da "
            "taxminan 34+ to'g'ri javob kerak bo'lishi mumkin — chunki matn osonroq, shuning "
            "uchun baholash mezoni qattiqroq.</div>"
        )},
        {
            "rich_text": "<p><strong>Amaliyot 1.</strong> Universitetga kirish uchun ariza berayotgan talaba qaysi modulni topshirishi kerak?</p>",
            "choices": [
                {"text": "General Training", "is_correct": False},
                {"text": "Academic", "is_correct": True},
                {"text": "Farqi yo'q, ikkalasi ham bir xil qabul qilinadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Academic.</mark> "
                "Universitetlar odatda <strong>Academic</strong> modulini talab qiladi, "
                "chunki u akademik matnlarni o'qish qobiliyatini sinaydi. General Training "
                "esa ko'proq ish/migratsiya maqsadlari uchun ishlatiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Quyidagi bayonotlardan qaysi biri "
                "TO'G'RI: \"IELTS Reading'da Academic va General Training savol turlari "
                "butunlay boshqacha usullar talab qiladi.\"</p>"
            ),
            "choices": [
                {"text": "To'g'ri — har bir modul o'zining savol turiga ega", "is_correct": False},
                {"text": "Noto'g'ri — savol turlari bir xil, faqat matn mavzusi/qiyinligi farq qiladi", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: noto'g'ri "
                "bayonot.</mark> Ikkala modulda ham xuddi shu savol turlari qo'llaniladi "
                "(True/False/Not Given, Matching, Completion va h.k.) — farq faqat "
                "matnlarning manbasi, uslubi va qiyinlik darajasida.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Academic module</div><div class=\"pp-card-back\">akademik modul (universitet uchun)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">General Training module</div><div class=\"pp-card-back\">umumiy tayyorgarlik moduli (ish/migratsiya uchun)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">journal article</div><div class=\"pp-card-back\">jurnal maqolasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">workplace text</div><div class=\"pp-card-back\">ish joyi bilan bog'liq matn</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">general interest text</div><div class=\"pp-card-back\">umumiy qiziqish matni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">notice</div><div class=\"pp-card-back\">e'lon</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Format bir xil (3 bo'lim, 40 savol, 60 daqiqa) — matn turi farq qiladi.</li>"
            "<li>Academic = akademik matnlar; GT = kundalik/ish matnlari (1–2-bo'lim sodda).</li>"
            "<li>Savol turlari va usullar ikkala modulda ham bir xil ishlaydi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 5 (order 10 — opens the True/False/Not Given topic)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_TFNG,
    "title": "IELTS Reading 5: Intro to True/False/Not Given — Statements Based on Facts",
    "summary": "TRUE / FALSE / NOT GIVEN savol turini yechish usuli va eng ko'p uchraydigan tuzoqlar.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>True / False / Not Given nima?</h2>"
            "<p>Bu — IELTS Reading'da eng ko'p uchraydigan va ayni paytda eng ko'p xato "
            "qilinadigan savol turi. Sizga bir nechta <strong>bayonot (statement)</strong> "
            "beriladi, va siz har biri haqida parchada yozilgan <u>faktlarga</u> asoslanib "
            "qaror qabul qilishingiz kerak:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>TRUE</strong> — bayonot matndagi faktga mos keladi.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>FALSE</strong> — bayonot matndagi faktga zid keladi.</p>"
            "<p style=\"margin:0;\"><strong>NOT GIVEN</strong> — matnda bu haqda hech "
            "qanday ma'lumot yo'q (na tasdiqlaydi, na inkor etadi).</p>"
            "</div>"
        )},
        {"rich_text": (
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> bu savol turi <u>faktlar</u> haqida, "
            "<u>fikrlar</u> haqida emas! Muallifning shaxsiy fikri/bahosi bo'lsa, bu — "
            "boshqa savol turi (Yes/No/Not Given), keyingi mavzuda o'rganamiz. TRUE/FALSE/"
            "NOT GIVEN faqat <em>tekshirilishi mumkin bo'lgan faktlar</em> — sanalar, "
            "raqamlar, voqealar, jarayonlar — bilan ishlaydi.</div>"
        )},
        {"rich_text": (
            "<h3>4 bosqichli usul</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam — Kalit so'zlarni belgilang.</strong> "
            "Bayonotdagi eng muhim so'zlarni (ism, son, sifat, fe'l) aniqlang.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam — Matnda joyini toping.</strong> "
            "Kalit so'z yoki uning sinonimini scan qiling — savollar odatda matn "
            "tartibida keladi, shuning uchun oldingi javobdan keyingi joyni qidiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam — Diqqat bilan solishtiring.</strong> "
            "Bayonot matndagi ma'noni <u>aniq</u> takrorlaydimi, <u>ziddiyat</u>ga "
            "keladimi, yoki bu haqda <u>hech narsa yo'qmi</u>?</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam — \"Mutlaq so'zlar\"ga e'tibor "
            "bering.</strong> only, always, never, all, none, every kabi so'zlar "
            "ko'pincha FALSE javobga ishora qiladi — chunki matn kamdan-kam mutlaq "
            "bayonot beradi.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>FALSE va NOT GIVEN — eng katta tuzoq</h3>"
            "<p>Talabalarning eng ko'p xato qiladigan joyi — <strong>FALSE bilan NOT "
            "GIVEN'ni</strong> chalkashtirish:</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> Agar matn bayonotga <u>to'g'ridan-to'g'ri "
            "zid</u> bo'lsa (masalan, matn \"2015-yilda ochilgan\" desa, bayonot "
            "\"2010-yilda ochilgan\" desa) — bu <strong>FALSE</strong>. Agar matn shu "
            "mavzuni umuman <u>tilga olmasa</u> (masalan, muzey qachon ochilgani "
            "aytilmagan bo'lsa) — bu <strong>NOT GIVEN</strong>. \"Menimcha bu shunday "
            "bo'lishi kerak\" degan taxmin bilan NOT GIVEN'ni FALSE deb belgilamang!</div>"
        )},
        {"rich_text": (
            "<h3>Namuna parcha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"The Hoverfly Project began in 2016 as a small "
            "citizen-science initiative in three towns in the north of England. Volunteers "
            "were asked to record hoverfly sightings using a smartphone app. Within two "
            "years, the project had attracted over 4,000 volunteers, though researchers "
            "note that participation dropped noticeably during the winter months, when "
            "hoverflies are far less active. The project has never received government "
            "funding, relying instead on university grants and public donations.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bayonot: <em>\"The Hoverfly Project has "
                "received financial support from the government.\"</em> Bu TRUE, FALSE "
                "yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "Matnda aniq yozilgan: <em>\"has never received government funding\"</em> "
                "— bu bayonotga to'g'ridan-to'g'ri zid keladi. Bu klassik FALSE holati: "
                "matn ochiq-oydin qarama-qarshi faktni beradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bayonot: <em>\"Most of the Hoverfly "
                "Project's volunteers were university students.\"</em> Bu TRUE, FALSE "
                "yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Matn ko'ngillilar soni (4,000+) va universitet grantlari haqida aytadi, "
                "lekin ko'ngillilarning <u>kim ekanligi</u> (talaba, ishchi, va hokazo) "
                "haqida <strong>hech narsa demaydi</strong>. \"University grants\" so'zi "
                "sizni chalg'itmasin — bu moliyalashtirish manbai, ko'ngillilar kimligi "
                "emas!</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"Volunteer participation "
                "stayed the same throughout the year.\"</em> Bu TRUE, FALSE yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> Matn "
                "aytadi: <em>\"participation dropped noticeably during the winter "
                "months\"</em> — demak, ishtirok yil davomida <u>bir xil emas</u>, qishda "
                "kamaygan. Bayonotdagi \"stayed the same\" so'zi shu faktga zid keladi. "
                "Bu yerda \"throughout the year\" kabi <mark>mutlaq ma'noli</mark> "
                "iboralarga alohida e'tibor bering.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">statement</div><div class=\"pp-card-back\">bayonot</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to contradict</div><div class=\"pp-card-back\">ziddiyatga kelmoq, inkor etmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to confirm</div><div class=\"pp-card-back\">tasdiqlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">absolute qualifier</div><div class=\"pp-card-back\">mutlaq ma'noli so'z (always, never, all)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">citizen-science</div><div class=\"pp-card-back\">fuqarolik fani (ommaga ochiq ilmiy loyiha)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">funding</div><div class=\"pp-card-back\">moliyalashtirish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to drop noticeably</div><div class=\"pp-card-back\">sezilarli darajada kamaymoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>TRUE/FALSE/NOT GIVEN — faqat <strong>faktlar</strong> haqida (fikrlar emas).</li>"
            "<li>4 qadam: kalit so'z → matndagi joy → diqqat bilan solishtirish → mutlaq so'zlarga e'tibor.</li>"
            "<li>FALSE = to'g'ridan-to'g'ri zid fakt; NOT GIVEN = matn bu haqda umuman gapirmagan.</li>"
            "</ul>"
        )},
    ],
},

]
