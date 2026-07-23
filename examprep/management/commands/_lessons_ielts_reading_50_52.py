"""
IELTS Reading lessons 20-22 (orders 50-52) — the whole "Ko'p variantli savollar
(Multiple Choice)" topic — fifth batch, see toc_ielts_reading.txt.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_MC = {
    "title":   "Ko'p variantli savollar (Multiple Choice)",
    "summary": "Bitta va bir nechta javobli MCQ: paraphrase tanish, chalg'ituvchilarni "
               "chiqarib tashlash va checklist usuli.",
    "icon":    "bi-ui-checks-grid",
    "order":   6,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 20 (order 50 — Single-Answer Multiple Choice)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MC,
    "title": "IELTS Reading 20: Single-Answer Multiple Choice — Paraphrase Recognition",
    "summary": "Bitta to'g'ri javobli MCQ: to'g'ri variant paraphrase, chalg'ituvchilar 4 qolipda; matndan langar so'z bilan qidirish.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>Multiple Choice — tanish, lekin ayyor</h2>"
            "<p>Savol (savol yoki chala jumla) beriladi va odatda <strong>4 variant</strong> "
            "(A, B, C, D) — faqat <u>bittasi</u> to'g'ri. Format tanish ko'rinadi, lekin "
            "IELTS MCQ'ni maxsus qiyinlashtiradi: to'g'ri javob matndagi so'zlar bilan "
            "<mark style=\"background:#fee2e2;\">deyarli hech qachon</mark> aytilmaydi — u "
            "<mark style=\"background:#dcfce7;\">paraphrase</mark> qilingan. Aksincha, "
            "chalg'ituvchi variantlar matndagi so'zlarni aynan takrorlaydi.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — asosiy tuzoq:</strong> \"Matndagi so'z variantda ham bor\" "
            "degani \"to'g'ri\" degani EMAS. Ko'pincha aynan teskarisi: tanish so'z — "
            "tuzoq belgisi. To'g'ri javobni <u>g'oya</u> bo'yicha toping, so'z bo'yicha "
            "emas.</div>"
        )},
        {"rich_text": (
            "<h3>Yaxshi xabar: MCQ tartibda keladi</h3>"
            "<p>Matching Information'dan farqli o'laroq, MCQ savollari deyarli har doim "
            "<u>matn tartibida</u> beriladi: 1-savolning javobi 2-savolnikidan oldinroq "
            "paragrafda. Bu qidiruv maydonini keskin toraytiradi — savolni yechgach, "
            "keyingisini <em>o'sha joydan pastda</em> qidiring.</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Avval <u>savolni</u> "
            "o'qing, variantlarni EMAS. Nima so'ralayotganini tushuning — variantlar "
            "sizni chalg'itishdan oldin.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Savoldan <u>langar "
            "so'z</u> tanlang (ism, sana, atama — paraphrase qilinmaydigan narsa) va uni "
            "matndan skan qilib toping.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> Topilgan joyni "
            "<u>diqqat bilan</u> o'qing (odatda 2–3 jumla). Javobni <em>o'z so'zingiz "
            "bilan</em> ayting — variantlarga qaramasdan.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Endi variantlardan "
            "o'z javobingizga eng yaqin paraphrase'ni tanlang. Qolganlarini \"nega "
            "YO'Q?\" bilan tekshiring.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Chalg'ituvchilarning 4 qolipi</h3>"
            "<p>IELTS noto'g'ri variantlarni tasodifiy yozmaydi — 4 ta aniq qolip bor. "
            "Qolipni tanisangiz, variantni ishonch bilan o'chirasiz:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>1. So'z-tuzoq (word-spotting).</strong> "
            "Matndagi so'zni aynan takrorlaydi, lekin g'oyani buzadi. <em>Tanish so'z ≠ "
            "to'g'ri javob.</em></p>"
            "<p style=\"margin:0 0 6px;\"><strong>2. To'g'ri, lekin javob emas (true but "
            "irrelevant).</strong> Matnga mos, lekin <u>savolga</u> javob bermaydi — "
            "boshqa narsa haqida.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3. Haddan tashqari kuchli (extreme).</strong> "
            "\"always, never, all, only, completely\" — matn ehtiyotkor (\"often, some, "
            "may\"), variant esa mutlaq. Odatda tuzoq.</p>"
            "<p style=\"margin:0;\"><strong>4. Yarim to'g'ri (partly true).</strong> "
            "Yarmi matnga mos, yarmi qo'shib yuborilgan yoki o'zgartirilgan. Eng ayyor "
            "tur — butun variantni tekshiring, birinchi yarmigagina emas.</p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> ikki variant qolib ketsa, \"nega bu YO'Q?\" "
            "deb so'rang va qaysi qolipga tushishini toping (extreme? partly true?). "
            "Tuzoq qolipini topsangiz — o'chirasiz. \"Nega HA?\" ikkalasiga ham sabab "
            "topib beradi.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna — paraphrase vs so'z-tuzoq</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"Although the museum's visitor "
            "numbers have risen every year since it reopened, its income has not kept "
            "pace, largely because most of the new visitors enter on free or discounted "
            "tickets.\"</p>"
            "</div>"
            "<p><strong>Savol:</strong> Why has the museum's income failed to rise as "
            "quickly as visitor numbers?</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\">A. Visitor numbers have fallen. ❌ <em>(to'g'ridan-to'g'ri ZID — matn \"risen\" deydi)</em></p>"
            "<p style=\"margin:0 0 4px;\">B. Many visitors pay little or nothing to enter. ✅ <em>(paraphrase: \"free or discounted tickets\")</em></p>"
            "<p style=\"margin:0 0 4px;\">C. The museum reopened recently. ❌ <em>(to'g'ri, lekin savolga javob emas — irrelevant)</em></p>"
            "<p style=\"margin:0;\">D. The museum has too many visitors. ❌ <em>(so'z-tuzoq: \"visitors\" bor, lekin g'oya buzuq)</em></p>"
            "</div>"
            "<p>To'g'ri javob B — matndagi \"free or discounted tickets\" ni \"pay little "
            "or nothing\" deb paraphrase qiladi. E'tibor bering: B'da matn so'zlaridan "
            "birortasi ham aynan takrorlanmaydi. Aynan shu — IELTS to'g'ri javobining "
            "\"barmoq izi\".</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bir variantda matndagi \"photosynthesis\" "
                "so'zi aynan takrorlangan. Bu haqda qaysi fikr TO'G'RI?</p>"
            ),
            "choices": [
                {"text": "So'z aynan mos kelgani uchun bu variant to'g'ri bo'lishi ehtimoli yuqori", "is_correct": False},
                {"text": "Aynan takrorlangan so'z ko'pincha so'z-tuzoq signali — g'oyani alohida tekshirish kerak", "is_correct": True},
                {"text": "Aynan so'z bo'lgan variantni darhol o'chirib tashlash kerak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: g'oyani tekshirish "
                "kerak.</mark> IELTS to'g'ri javoblari <u>paraphrase</u> qilinadi, "
                "chalg'ituvchilar esa ko'pincha matn so'zini aynan takrorlab \"tanish\" "
                "ko'rinadi. Demak aynan mos so'z — <em>hushyorlik chaqirig'i</em>: to'xtab, "
                "variant g'oyasi savolga javob berayotganini alohida tekshiring. (Uni "
                "avtomatik o'chirish ham xato — ba'zan atama muqarrar takrorlanadi.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Matn: <em>\"Solar panels can reduce a "
                "household's electricity bills, though the savings depend heavily on the "
                "local climate.\"</em> Savol: What does the writer say about solar panels? "
                "Qaysi variant to'g'ri?</p>"
            ),
            "choices": [
                {"text": "They always eliminate electricity bills.", "is_correct": False},
                {"text": "The financial benefit varies according to where you live.", "is_correct": True},
                {"text": "They are the cheapest form of energy.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "\"The savings depend heavily on the local climate\" → \"the financial "
                "benefit varies according to where you live\" (toza paraphrase: savings→"
                "financial benefit, local climate→where you live). Birinchisi "
                "<u>extreme</u> tuzoq: \"always eliminate\" — matn faqat \"reduce\" "
                "deydi. Uchinchisi — matnda umuman yo'q (irrelevant/qo'shib yuborilgan).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Ikki variant qoldi va ikkalasi ham "
                "\"to'g'ridek\". Eng ishonchli keyingi qadam qaysi?</p>"
            ),
            "choices": [
                {"text": "Uzunroq, batafsilroq variantni tanlayman", "is_correct": False},
                {"text": "Har biriga \"nega YO'Q?\" deb, chalg'ituvchi qolipini (extreme / partly true / irrelevant) qidiraman", "is_correct": True},
                {"text": "Matndagi so'zga ko'proq o'xshaydigan variantni tanlayman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"nega YO'Q?\" "
                "testi.</mark> Ikki nomzoddan birini o'chirish uchun tuzoq qolipini "
                "toping: biri haddan tashqari kuchli (extreme)mi? yarmigina to'g'ri "
                "(partly true)mi? savolga aloqasizmi (irrelevant)? Qolip topilgan variant "
                "tashlanadi. \"Uzunligi\" yoki \"so'z o'xshashligi\" — asossiz mezonlar "
                "(so'z o'xshashligi hatto tuzoq belgisi).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to paraphrase</div><div class=\"pp-card-back\">boshqa so'zlar bilan aytmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a distractor</div><div class=\"pp-card-back\">chalg'ituvchi variant</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">word-spotting trap</div><div class=\"pp-card-back\">so'z-tuzoq (aynan so'z mosligi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an extreme claim</div><div class=\"pp-card-back\">haddan tashqari kuchli da'vo</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">true but irrelevant</div><div class=\"pp-card-back\">to'g'ri, lekin savolga aloqasiz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to keep pace with</div><div class=\"pp-card-back\">bir maromda ergashmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a discounted ticket</div><div class=\"pp-card-back\">chegirmali chipta</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to eliminate</div><div class=\"pp-card-back\">butunlay yo'q qilmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>To'g'ri javob = PARAPHRASE; matn so'zini aynan takrorlagan variant ko'pincha tuzoq.</li>"
            "<li>Avval savolni o'qing, keyin variantlarni — langar so'z bilan matndan joyni toping.</li>"
            "<li>Javobni o'z so'zingiz bilan ayting, keyin eng yaqin variantni tanlang.</li>"
            "<li>4 chalg'ituvchi qolipi: so'z-tuzoq / true-but-irrelevant / extreme / partly true.</li>"
            "<li>MCQ savollari matn tartibida — keyingi javobni pastdan qidiring.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 21 (order 51 — Multiple-Answer Multiple Choice)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MC,
    "title": "IELTS Reading 21: Multiple-Answer Multiple Choice — The Checklist Method (choose TWO/THREE)",
    "summary": "\"Choose TWO/THREE letters\" turi: checklist usuli, javoblar tartibsizligi va \"scatter\" tuzog'idan qochish.",
    "order": 51,
    "blocks": [
        {"rich_text": (
            "<h2>\"Choose TWO letters\" — boshqa o'yin</h2>"
            "<p>Bu turda savol quyidagicha bo'ladi: <em>\"Which TWO of the following are "
            "mentioned by the writer? Choose TWO letters, A–E.\"</em> Endi 5 (yoki 7) "
            "variantdan <u>ikki (yoki uch)</u> tasi to'g'ri. Ballash qat'iy: <mark "
            "style=\"background:#fee2e2;\">ikkala harf ham to'g'ri bo'lsagina to'liq ball</mark> "
            "olasiz — bittasi noto'g'ri bo'lsa, savolni yo'qotasiz.</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — ikki muhim fakt:</strong> (1) barcha variantlar odatda "
            "<u>bitta yaqin qism</u>dan olinadi (bir-ikki paragraf) — tartibsiz emas. "
            "(2) To'g'ri javoblar orasidagi tartib muhim emas: A va D ni istalgan "
            "tartibda yozing.</div>"
        )},
        {"rich_text": (
            "<h3>Checklist usuli — variantlarni birma-bir sud qiling</h3>"
            "<p>Single MCQ'da bitta g'olibni izlaysiz. Bu yerda esa <u>har bir variantni "
            "alohida hukm qilishingiz</u> kerak: matnda tasdiqlanganmi — HA yoki YO'Q. "
            "Har variantni kichik T/F/NG savoli deb qarang:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Tegishli qismni (variantlar "
            "olingan paragraf(lar)ni) toping va bir marta o'qing.</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> A dan boshlab har "
            "variantga <u>✓ / ✗ / ?</u> qo'ying: matnda aniq bormi (✓), ziddmi/yo'qmi "
            "(✗), noaniqmi (?).</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> Talab qilingan sondagi "
            "(masalan 2) eng ishonchli ✓ larni tanlang. Agar 3 ✓ chiqsa — ularni qayta "
            "solishtirib, eng aniq tasdiqlangan 2 tasini qoldiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> ✗ va ? larni sabab bilan "
            "chetga suring — nega tashlanganini bilib qo'ying (tuzoq qolipi qaysi?).</p></div>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> \"choose TWO\" degani ikkitasi to'g'ri — "
            "shuning uchun barcha 5 variantni ko'rib chiqing, birinchi ikki ✓ da "
            "to'xtamang. Uchinchi (kuchliroq) javob pastroqda turishi mumkin.</div>"
        )},
        {"rich_text": (
            "<h3>⚠️ Ikki maxsus tuzoq</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>1. \"Scatter\" tuzog'i (so'z mavjud, "
            "lekin ma'no yo'q).</strong> Variantdagi so'z matnda <u>uchraydi</u>, lekin "
            "boshqa kontekstda — variant aytgan narsa aslida tasdiqlanmagan. Single "
            "MCQ'dagi so'z-tuzoqning ko'p javobli versiyasi.</p>"
            "<p style=\"margin:0;\"><strong>2. \"Mantiqan to'g'ri\" tuzog'i (real-world "
            "knowledge).</strong> Variant haqiqatda to'g'ri (dunyoda shunday), lekin "
            "<u>matnda aytilmagan</u>. IELTS matnda yozilganini so'raydi, dunyoni emas — "
            "bu NOT GIVEN qoidasining aynan o'zi.</p>"
            "</div>"
            "<p>Ikkala tuzoqdan bitta savol himoya qiladi: <em>\"Buni matn AYNAN "
            "aytyaptimi?\"</em> — barmog'ingiz bilan tasdiqlovchi jumlani ko'rsata "
            "olsangizgina ✓ qo'ying.</p>"
        )},
        {"rich_text": (
            "<h3>Namuna — checklist ish jarayonida</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"The city's new cycle-hire "
            "scheme has proved popular for several reasons. The bikes are cheap to hire "
            "and can be picked up and dropped off at hundreds of docking stations across "
            "the centre. Tourists in particular have embraced the scheme. Critics note, "
            "however, that the docking stations are concentrated downtown, leaving outer "
            "districts poorly served.\"</p>"
            "</div>"
            "<p><strong>Savol:</strong> Which TWO reasons for the scheme's popularity are "
            "mentioned? (A–E)</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 4px;\">A. The bikes are inexpensive to rent. ✓ <em>(\"cheap to hire\")</em></p>"
            "<p style=\"margin:0 0 4px;\">B. There are many places to collect and return them. ✓ <em>(\"hundreds of docking stations\")</em></p>"
            "<p style=\"margin:0 0 4px;\">C. The bikes are electric. ✗ <em>(matnda umuman yo'q — real-world taxmin)</em></p>"
            "<p style=\"margin:0 0 4px;\">D. Stations cover every district equally. ✗ <em>(aksincha — \"outer districts poorly served\")</em></p>"
            "<p style=\"margin:0;\">E. The scheme is free for residents. ✗ <em>(\"cheap\" ≠ \"free\" — so'z-tuzoq/extreme)</em></p>"
            "</div>"
            "<p>Javob: <strong>A va B</strong>. Har biriga barmoq bilan tasdiqlovchi "
            "jumlani ko'rsata oldik. C — mantiqiy taxmin (elektr velosiped ko'p, lekin "
            "matnda yo'q), D — matnga zid, E — \"free\" so'zi \"cheap\" ni bo'rttiradi.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> \"Choose TWO letters\" savolida to'liq "
                "ballni qachon olasiz?</p>"
            ),
            "choices": [
                {"text": "Kamida bitta harf to'g'ri bo'lsa", "is_correct": False},
                {"text": "Faqat ikkala harf ham to'g'ri bo'lganda; bittasi xato bo'lsa, ball yo'q", "is_correct": True},
                {"text": "Harflarni to'g'ri tartibda yozganda", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkala harf ham "
                "to'g'ri bo'lganda.</mark> Bu tur \"hammasi yoki hech narsa\" tamoyilida "
                "ballanadi — bir to'g'ri + bir xato = 0. Shuning uchun har variantni "
                "checklist bilan alohida tasdiqlash muhim: bitta ehtiyotsiz ✓ butun "
                "savolni yo'qotadi. (Tartib esa muhim emas.)</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Matn tibbiyot maqolasi haqida, "
                "variantlardan biri: <em>\"Exercise is good for the heart.\"</em> Bu "
                "haqiqatda to'g'ri, lekin siz matndan bunday jumlani topa olmayapsiz. "
                "Nima qilasiz?</p>"
            ),
            "choices": [
                {"text": "Belgilaymyan — bu umuman ma'lum haqiqat", "is_correct": False},
                {"text": "Belgilamayman — IELTS matnda aytilganini so'raydi, dunyoviy bilimni emas (real-world tuzoq)", "is_correct": True},
                {"text": "Belgilaymyan, chunki sog'liq mavzusidagi variant odatda to'g'ri", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: belgilamayman.</mark> "
                "Bu klassik <u>real-world knowledge</u> tuzog'i — variant dunyoda "
                "to'g'ri, lekin matnda yo'q. IELTS qoidasi (T/F/NG darsidan): faqat "
                "<u>matn</u> tasdiqlagan narsani belgilang. Barmog'ingiz bilan "
                "tasdiqlovchi jumlani ko'rsata olmasangiz — ✓ qo'ymang, u \"Not Given\".</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> \"Choose TWO\" savolida checklist "
                "bo'yicha 3 ta ✓ chiqib qoldi. Eng to'g'ri qadam qaysi?</p>"
            ),
            "choices": [
                {"text": "Uchalasini ham yozaman — ehtimol ball beriladi", "is_correct": False},
                {"text": "Uch ✓ ni qayta o'qib, matn AYNAN tasdiqlagan eng aniq 2 tasini qoldiraman; biri ehtimol yarim-to'g'ri", "is_correct": True},
                {"text": "Birinchi ikkitasini olaman", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 3 tani qayta "
                "solishtirish.</mark> Faqat 2 javob to'g'ri, demak ✓ lardan biri aslida "
                "<u>yarim to'g'ri</u> (partly true) yoki paraphrase'i kuchsizroq. "
                "Uchalasini qayta o'qib, qaysi biri matnda <em>eng aniq</em> "
                "tasdiqlanganini toping. Uchtasini yozish (ortiqcha harf) — javobni "
                "avtomatik noto'g'ri qiladi; \"birinchi ikki\" — asossiz tanlov.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to embrace a scheme</div><div class=\"pp-card-back\">tizimni qizg'in qabul qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a docking station</div><div class=\"pp-card-back\">(velosiped) to'xtash/ulash nuqtasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to be concentrated in</div><div class=\"pp-card-back\">bir joyda to'plangan bo'lmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">poorly served</div><div class=\"pp-card-back\">yaxshi xizmat ko'rsatilmagan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">inexpensive</div><div class=\"pp-card-back\">arzon</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">real-world knowledge trap</div><div class=\"pp-card-back\">dunyoviy bilim tuzog'i</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">all-or-nothing marking</div><div class=\"pp-card-back\">hammasi-yoki-hech ballash</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to hire</div><div class=\"pp-card-back\">ijaraga olmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>\"Choose TWO/THREE\": ikkala/uchala harf ham to'g'ri bo'lsagina ball — bitta xato = 0.</li>"
            "<li>Checklist usuli: har variantga ✓/✗/? qo'ying (mini T/F/NG), keyin eng ishonchlilarini tanlang.</li>"
            "<li>Barcha variantlarni ko'ring — kuchliroq javob pastroqda bo'lishi mumkin.</li>"
            "<li>Scatter tuzog'i (so'z bor, ma'no yo'q) va real-world tuzog'i (dunyoda to'g'ri, matnda yo'q)dan ehtiyot bo'ling.</li>"
            "<li>Faqat barmoq bilan ko'rsata oladigan tasdiqlovchi jumla bo'lsa ✓ qo'ying.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 22 (order 52 — MC Full Passage Practice, mixed review)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_MC,
    "title": "IELTS Reading 22: Multiple Choice — Full Passage Practice (Mixed Review)",
    "summary": "To'liq matn ustida single-answer va multiple-answer MCQ aralash amaliyot — paraphrase va checklist ko'nikmalarini birlashtirish.",
    "order": 52,
    "blocks": [
        {"rich_text": (
            "<h2>Yakuniy sinov: bitta va ko'p javobli birga</h2>"
            "<p>Endi ikki turni — single-answer (A/B/C/D dan bitta) va multiple-answer "
            "(choose TWO) — bitta to'liq matnda birlashtiramiz. Usullarni eslang: "
            "to'g'ri javob = paraphrase; chalg'ituvchi = so'z-tuzoq / extreme / partly "
            "true / irrelevant; ko'p javobli savolda — checklist (✓/✗/?).</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> savol matndan langar so'z bilan joyni toping, "
            "keyin 2–3 jumlani diqqat bilan o'qing. Shoshib, variantdagi tanish so'zga "
            "yopishmang — bu MCQ'da eng ko'p ball yo'qotadigan odat.</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Slow Food Movement</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\"><strong>A.</strong> \"The Slow Food movement "
            "began in Italy in 1986, when a journalist named Carlo Petrini organised a "
            "protest against the opening of a fast-food restaurant beside the Spanish "
            "Steps in Rome. What started as a local objection to a single burger outlet "
            "grew, within a few years, into an international organisation active in more "
            "than 150 countries.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>B.</strong> \"Petrini's central idea "
            "was not simply that fast food tastes worse than traditional cooking. His "
            "real concern was that the industrial food system was erasing local "
            "differences — the same handful of crops, the same brands, the same flavours "
            "spreading to every corner of the globe. A dish that had taken a region "
            "centuries to perfect could, he feared, be forgotten within a single "
            "generation.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>C.</strong> \"To counter this, the "
            "movement promotes what it calls 'good, clean and fair' food. 'Good' means "
            "tasty and fresh; 'clean' means produced without harming the environment; "
            "and 'fair' means that the people who grow and prepare it are paid decently. "
            "Critics sometimes assume the movement is simply nostalgic, but this "
            "three-part definition is deliberately forward-looking.</p>"
            "<p style=\"margin:0 0 10px;\"><strong>D.</strong> \"One of its best-known "
            "projects is the Ark of Taste, a catalogue of foods at risk of disappearing "
            "— rare apple varieties, traditional cheeses, heritage breeds of animal. By "
            "recording and publicising these foods, the movement hopes to create demand "
            "for them, since a food that people will pay for is far more likely to "
            "survive than one preserved only in a museum.</p>"
            "<p style=\"margin:0;\"><strong>E.</strong> \"The movement is not without its "
            "detractors. Some economists argue that its produce is too expensive to feed "
            "a growing world population, and that only the wealthy can afford to eat "
            "'slowly'. Supporters reply that cheap industrial food carries hidden costs — "
            "to health, to farmers and to the planet — that simply appear on a different "
            "bill.\"</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>1-qism — Single-answer (bitta javob)</h3>"
            "<p>Har savol uchun BITTA to'g'ri variantni tanlang.</p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> What does the writer say about the origin "
                "of the Slow Food movement?</p>"
            ),
            "choices": [
                {"text": "It was planned from the start as a global organisation.", "is_correct": False},
                {"text": "It grew out of a protest against one particular restaurant.", "is_correct": True},
                {"text": "It was founded by a group of professional chefs.", "is_correct": False},
                {"text": "It began as a campaign to improve Italian cooking.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B.</mark> A "
                "paragraf: \"a protest against the opening of a <u>fast-food "
                "restaurant</u>... a local objection to a single burger outlet\" → "
                "\"protest against one particular restaurant\" (paraphrase). A-variant "
                "<u>extreme/zid</u>: \"local objection\" edi, keyin xalqaro bo'ldi — "
                "boshdan rejalashtirilmagan. C — \"journalist\" edi, oshpazlar emas "
                "(so'z-tuzoq/noto'g'ri). D — \"tastes worse\" B paragrafda RAD etilgan "
                "(asosiy g'oya emas).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> According to paragraph B, what worried "
                "Petrini most?</p>"
            ),
            "choices": [
                {"text": "That fast food was unhealthy.", "is_correct": False},
                {"text": "That traditional dishes took too long to prepare.", "is_correct": False},
                {"text": "That local food traditions were being lost to a global sameness.", "is_correct": True},
                {"text": "That Italian food was better than other cuisines.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: C.</mark> B "
                "paragraf aniq aytadi: \"His <u>real concern</u> was that the industrial "
                "food system was <u>erasing local differences</u>... could be forgotten "
                "within a single generation\" → \"local food traditions were being lost "
                "to a global sameness\". A-variant — <u>partly true/irrelevant</u>: matn "
                "\"tastes worse\" ni aytadi, lekin darrov \"not simply that\" deb uni "
                "asosiy tashvish emasligini ta'kidlaydi. B va D — matnda yo'q.</p>"
            ),
        },
        {"rich_text": (
            "<h3>2-qism — Multiple-answer (choose TWO)</h3>"
            "<p><strong>Savol 3.</strong> Which TWO of the following are mentioned in the "
            "passage as features of the Slow Food movement? Choose TWO letters, A–E. "
            "<em>(Ikkala to'g'ri harfni ham tanlang — checklist usulini eslang.)</em></p>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 3a.</strong> Birinchi to'g'ri variant qaysi?</p>"
            ),
            "choices": [
                {"text": "A. It keeps a record of foods in danger of being lost.", "is_correct": True},
                {"text": "B. It has opened its own chain of restaurants.", "is_correct": False},
                {"text": "C. It receives funding from fast-food companies.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: A.</mark> D "
                "paragraf: \"the Ark of Taste, a <u>catalogue of foods at risk of "
                "disappearing</u>\" → \"a record of foods in danger of being lost\" (toza "
                "paraphrase). B — matnda yo'q (real-world taxmin: harakat restoranga "
                "qarshi boshlangan, o'zi ochmaydi). C — mantiqan ham absurd va matnda "
                "yo'q. A ga barmoq bilan tasdiqlovchi jumlani ko'rsata oldik: ✓.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3b.</strong> Ikkinchi to'g'ri variant qaysi?</p>"
            ),
            "choices": [
                {"text": "D. It defines good food using three criteria.", "is_correct": True},
                {"text": "E. It guarantees the cheapest prices for shoppers.", "is_correct": False},
                {"text": "F. It operates only within Italy.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: D.</mark> C "
                "paragraf: \"'<u>good, clean and fair</u>' food\" — uch mezonli ta'rif → "
                "\"defines good food using three criteria\". E — aksincha: harakat qimmat "
                "deb tanqid qilinadi (\"too expensive\"), arzonlikni kafolatlamaydi "
                "(extreme/zid tuzoq). F — matnga zid: \"active in more than 150 "
                "countries\" (A paragraf), faqat Italiyada emas. Demak Savol 3 javobi: "
                "<strong>A va D</strong>.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> In paragraph E, how do supporters respond "
                "to the criticism about cost?</p>"
            ),
            "choices": [
                {"text": "They admit that only rich people can join the movement.", "is_correct": False},
                {"text": "They argue that cheap industrial food has hidden costs paid elsewhere.", "is_correct": True},
                {"text": "They claim their food is actually the cheapest available.", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: ikkinchisi.</mark> "
                "E paragraf: \"cheap industrial food carries <u>hidden costs</u> — to "
                "health, to farmers and to the planet — that simply appear on a "
                "<u>different bill</u>\" → \"hidden costs paid elsewhere\". Birinchi "
                "variant — bu <u>tanqidchilar</u>ning fikri (\"only the wealthy\"), "
                "tarafdorlarniki emas (\"kimning fikri\" tuzog'i!). Uchinchisi — matnga "
                "zid, tarafdorlar arzonlikni da'vo qilmaydi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — zo'r! Single va multiple MCQ'ni to'liq egalladingiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3–4/5</strong> — yaxshi; xato variantni qaysi tuzoq qolipiga (extreme/partly true/irrelevant/word-spotting) tushishini aniqlang.</p>"
            "<p style=\"margin:0;\"><strong>2/5 yoki kam</strong> — 20–21-darslarga qaytib, paraphrase-tanish va checklist usulini takrorlang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a movement</div><div class=\"pp-card-back\">harakat (ijtimoiy)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to erase differences</div><div class=\"pp-card-back\">farqlarni o'chirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">industrial food system</div><div class=\"pp-card-back\">sanoat oziq-ovqat tizimi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">nostalgic</div><div class=\"pp-card-back\">o'tmishga qo'msaydigan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at risk of disappearing</div><div class=\"pp-card-back\">yo'qolib ketish xavfida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a detractor</div><div class=\"pp-card-back\">tanqidchi, ayblovchi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">hidden costs</div><div class=\"pp-card-back\">yashirin xarajatlar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">heritage breed</div><div class=\"pp-card-back\">an'anaviy (nasl) zoti</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Single MCQ: to'g'ri javob paraphrase; 4 tuzoq qolipini eslang.</li>"
            "<li>Multiple MCQ: har variantni checklist bilan alohida tasdiqlang (✓/✗/?).</li>"
            "<li>\"Kimning fikri\" tuzog'i MCQ'da ham bor: tanqidchi vs tarafdor fikrini aralashtirmang.</li>"
            "<li>Real-world taxmin va so'z-tuzoq — matn AYNAN aytmasa, tanlamang.</li>"
            "<li>Langar so'z bilan joyni toping, 2–3 jumlani diqqat bilan o'qing — shoshmang.</li>"
            "</ul>"
        )},
    ],
},

]
