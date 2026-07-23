"""
IELTS Reading lessons 11-13 (topic: Haqiqat / Yolg'on / Berilmagan — completes it)
+ lessons 20-21 (topic: Ha / Yo'q / Berilmagan) — second batch, see toc_ielts_reading.txt.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_TFNG = {
    "title":   "Haqiqat / Yolg'on / Berilmagan (True / False / Not Given)",
    "summary": "Faktlarga asoslangan bayonotlarni TRUE / FALSE / NOT GIVEN sifatida aniqlash.",
    "icon":    "bi-check2-square",
    "order":   2,
}

TOPIC_YNNG = {
    "title":   "Ha / Yo'q / Berilmagan (Yes / No / Not Given)",
    "summary": "Muallifning fikri va da'volarini YES / NO / NOT GIVEN sifatida aniqlash.",
    "icon":    "bi-chat-square-text",
    "order":   3,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 6 (order 11 — T/F/NG: locating the matching sentence)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_TFNG,
    "title": "IELTS Reading 6: Locating the Matching Sentence — Keyword + Synonym Scanning",
    "summary": "Bayonotga mos jumlani matndan tez topish: to'g'ri kalit so'z tanlash va sinonimlarni sezish.",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Javob qayerda \"yashiringan\"?</h2>"
            "<p>O'tgan darsda TRUE/FALSE/NOT GIVEN usulini o'rgandik. Amalda esa eng ko'p "
            "vaqt ketadigan bosqich — <strong>2-qadam: bayonotga mos jumlani matndan "
            "topish</strong>. Agar to'g'ri jumlani topa olmasangiz, qolgan hamma qadamlar "
            "befoyda. Bu darsda <mark>qaysi so'zni qidirish</mark> va "
            "<mark style=\"background:#dbeafe;\">sinonimlarni qanday sezish</mark>ni "
            "o'rganamiz — bu ko'nikma keyingi barcha savol turlarida ham ishlaydi.</p>"
        )},
        {"rich_text": (
            "<h3>Qaysi kalit so'zni tanlash kerak?</h3>"
            "<p>Bayonotdagi hamma so'z ham qidirishga yaramaydi. Yaxshi kalit so'z — "
            "<u>matnda o'zgarmasdan qoladigan</u> so'z:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Eng yaxshi: ismlar, joy nomlari, sanalar, "
            "raqamlar.</strong> \"Darwin\", \"2015\", \"Amazon\" kabi so'zlarni matn "
            "sinonim bilan almashtira olmaydi — ular <mark style=\"background:#dcfce7;\">"
            "o'zgarmas langar (anchor)</mark> bo'lib xizmat qiladi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Yaxshi: maxsus atamalar.</strong> "
            "\"photosynthesis\", \"hoverfly\", \"migration\" kabi ilmiy/texnik so'zlar "
            "ham kamdan-kam paraphrase qilinadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Xavfli: oddiy fe'l va sifatlar.</strong> "
            "\"increase\", \"important\", \"difficult\" kabi so'zlar deyarli har doim "
            "<mark style=\"background:#fee2e2;\">sinonim bilan almashtiriladi</mark> — "
            "ularni qidirsangiz, topolmay qolishingiz mumkin.</p></div>"
            "<div class=\"pp-step\"><p><strong>Qoida:</strong> har bayonotdan 2 ta kalit "
            "so'z tanlang — bitta \"langar\" (ism/raqam) + bitta mazmun so'zi. Langar "
            "jumlani topadi, mazmun so'zi esa solishtirish uchun kerak bo'ladi.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Sinonim xaritasi — IELTS eng sevgan almashtirishlar</h3>"
            "<p>IELTS savol tuzuvchilari bayonotni matndan <u>boshqa so'zlar bilan</u> "
            "yozadi. Eng ko'p uchraydigan juftliklarni yodlab oling:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>rise / grow / climb / increase</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>o'smoq, ko'paymoq</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>almost / nearly / close to / just under</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>deyarli, ...ga yaqin</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>be responsible for / cause / lead to / result in</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>sabab bo'lmoq, olib kelmoq</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>the majority of / most / a large proportion of</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>ko'pchilik, katta qismi</em></p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> har kuni mashq qilganingizda o'zingizning "
            "\"sinonim daftaringizni\" yuriting: savoldagi so'z ↔ matndagi so'z. 2–3 "
            "haftada IELTS'ning almashtirish uslubini oldindan seza boshlaysiz.</div>"
        )},
        {"rich_text": (
            "<h3>Tartib qoidasi — qidiruv doirasini toraytiring</h3>"
            "<p>TRUE/FALSE/NOT GIVEN savollari <strong>matn tartibida</strong> keladi: "
            "3-savolning javobi 2-savol javobidan <u>keyin</u>, 4-savol javobidan "
            "<u>oldin</u> joylashgan. Demak:</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> agar 2-savol javobini 2-paragrafda, 4-savol "
            "javobini 4-paragrafda topgan bo'lsangiz — 3-savolni faqat <u>2–4-paragraflar "
            "orasida</u> qidiring. Bu qoida qidiruv vaqtini bir necha barobar qisqartiradi "
            "va NOT GIVEN'ni aniqlashga ham yordam beradi: belgilangan oraliqda ma'lumot "
            "yo'q bo'lsa, butun matnni qayta o'qish shart emas.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna parcha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"The Svalbard Global Seed Vault, buried deep inside a "
            "mountain on a remote Norwegian island, opened in 2008 as a backup store for "
            "the world's crop seeds. The facility currently holds well over a million seed "
            "samples, deposited by gene banks from almost every country. Running costs are "
            "met jointly by the Norwegian government and an international trust. Contrary "
            "to popular belief, the seeds remain the property of the depositing gene banks, "
            "and only they may withdraw them.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bayonot: <em>\"More than a million seed "
                "samples are kept in the vault.\"</em> Bu bayonotni tekshirish uchun eng "
                "samarali kalit so'z(lar) qaysi?</p>"
            ),
            "choices": [
                {"text": "\"kept\" — chunki bu asosiy fe'l", "is_correct": False},
                {"text": "\"million\" — raqamlar matnda deyarli o'zgarmaydi", "is_correct": True},
                {"text": "\"more than\" — chunki bayonot shundan boshlanadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"million\".</mark> "
                "Raqamlar — eng ishonchli langar: matnda ham <em>\"well over a million "
                "seed samples\"</em> deb turibdi. \"kept\" esa matnda \"holds\" bo'lib "
                "o'zgargan, \"more than\" esa \"well over\" bo'lgan — oddiy so'zlarni "
                "qidirsangiz adashishingiz mumkin edi. Javob, aytgancha, "
                "<strong>TRUE</strong>: \"well over a million\" = \"more than a million\".</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bayonot: <em>\"The vault is funded "
                "entirely by the Norwegian government.\"</em> Matndagi qaysi jumla bu "
                "bayonotga mos keladi va javob nima?</p>"
            ),
            "choices": [
                {"text": "\"opened in 2008 as a backup store...\" — javob NOT GIVEN", "is_correct": False},
                {"text": "\"Running costs are met jointly by the Norwegian government and an international trust\" — javob FALSE", "is_correct": True},
                {"text": "\"the seeds remain the property of the depositing gene banks\" — javob TRUE", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "Kalit so'zlar \"funded\" ↔ \"running costs are met\" (sinonim juftlik!) "
                "va langar \"Norwegian government\". Bayonotda <mark>\"entirely\"</mark> "
                "(butunlay) degan mutlaq so'z bor, matn esa <em>\"jointly ... and an "
                "international trust\"</em> deydi — ya'ni <u>birgalikda</u>. Demak bayonot "
                "matnga zid — FALSE. O'tgan darsdagi qoida esingizdami? Mutlaq so'zlar "
                "(entirely, only, all) ko'pincha FALSE'ga ishora qiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"Any research institute may "
                "take seeds out of the vault.\"</em> Bu TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "\"take seeds out\" ↔ matndagi \"withdraw\" — yana sinonim juftlik. Matn: "
                "<em>\"only they [the depositing gene banks] may withdraw them\"</em> — "
                "faqat topshirgan gen banklari olishi mumkin, \"any research institute\" "
                "emas. Matn to'g'ridan-to'g'ri qarama-qarshi cheklovni aytyapti, shuning "
                "uchun bu NOT GIVEN emas, FALSE.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">anchor word</div><div class=\"pp-card-back\">langar so'z (ism, raqam — o'zgarmaydigan)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to locate</div><div class=\"pp-card-back\">joyini topmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">well over</div><div class=\"pp-card-back\">...dan ancha ko'p</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">jointly</div><div class=\"pp-card-back\">birgalikda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to withdraw</div><div class=\"pp-card-back\">olib chiqmoq, yechib olmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">contrary to popular belief</div><div class=\"pp-card-back\">ommaviy fikrdan farqli o'laroq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">running costs</div><div class=\"pp-card-back\">joriy xarajatlar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">facility</div><div class=\"pp-card-back\">inshoot, muassasa</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Kalit so'z sifatida <strong>ism, raqam, sana, atama</strong>ni tanlang — ular paraphrase qilinmaydi.</li>"
            "<li>Oddiy fe'l/sifatlar deyarli har doim sinonim bilan almashtiriladi — sinonim daftar yuriting.</li>"
            "<li>Savollar matn tartibida — topilgan javoblar orasidagi oraliqda qidiring.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 7 (order 12 — FALSE vs NOT GIVEN deep dive)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_TFNG,
    "title": "IELTS Reading 7: FALSE vs NOT GIVEN — The Trap That Loses the Most Points",
    "summary": "FALSE va NOT GIVEN o'rtasidagi chegarani aniq ajratish: ziddiyat testi va eng xavfli tuzoqlar.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>Eng ko'p ball yo'qotiladigan joy</h2>"
            "<p>Statistika bo'yicha TRUE javoblarni talabalar yaxshi topadi. Ballar esa "
            "<strong>FALSE bilan NOT GIVEN chegarasida</strong> yo'qoladi. Sabab: bizning "
            "miyamiz bo'shliqni to'ldirishga o'rganib qolgan — matnda ma'lumot bo'lmasa, "
            "biz <em>o'z bilimimiz yoki taxminimiz</em> bilan to'ldirib, FALSE deb "
            "belgilaymiz. Bu darsda shu odatni \"o'chirib\", aniq test bilan ishlashni "
            "o'rganamiz.</p>"
        )},
        {"rich_text": (
            "<h3>\"Ziddiyat testi\" — bitta savol hammasini hal qiladi</h3>"
            "<p>Bayonotga mos jumlani topganingizdan keyin o'zingizga <u>faqat bitta</u> "
            "savol bering:</p>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Test:</strong> \"Agar bayonot to'g'ri bo'lsa, matndagi jumla "
            "<u>yolg'on bo'lib qoladimi</u>?\" Ha bo'lsa — <strong>FALSE</strong>. "
            "Yo'q bo'lsa (ikkalasi ham bir vaqtda to'g'ri bo'la olsa) — "
            "<strong>NOT GIVEN</strong>.</div>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>Misol 1.</strong> Matn: <em>\"The bridge "
            "was completed in 1932.\"</em> Bayonot: <em>\"The bridge was completed in "
            "1935.\"</em> Ikkalasi bir vaqtda to'g'ri bo'la oladimi? <u>Yo'q</u> — bitta "
            "ko'prik ikki xil yilda bitmaydi. Demak <mark style=\"background:#fee2e2;\">"
            "FALSE</mark>.</p></div>"
            "<div class=\"pp-step\"><p><strong>Misol 2.</strong> Matn: <em>\"The bridge "
            "was completed in 1932.\"</em> Bayonot: <em>\"The bridge took eight years to "
            "build.\"</em> Ikkalasi bir vaqtda to'g'ri bo'la oladimi? <u>Ha</u> — 1932-da "
            "bitgan ko'prik 8 yil qurilgan bo'lishi ham, bo'lmasligi ham mumkin; matn "
            "qurilish muddati haqida hech narsa demagan. Demak <mark>NOT GIVEN</mark>.</p></div>"
            "<div class=\"pp-step\"><p><strong>Xulosa:</strong> FALSE uchun matnda "
            "bayonotni <u>yolg'onga chiqaradigan aniq fakt</u> bo'lishi shart. \"Matn "
            "buni aytmagan, demak noto'g'ri\" — degan mantiq NOT GIVEN'ga olib boradi, "
            "FALSE'ga emas.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>3 ta klassik tuzoq</h3>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Tuzoq 1 — Dunyo bilimi (outside knowledge).</strong> Bayonot "
            "hayotda to'g'ri (yoki noto'g'ri) bo'lishi mumkin, lekin siz faqat "
            "<u>matndagi</u> ma'lumotga tayanishingiz kerak. \"Buni bilaman-ku!\" degan "
            "fikr — xavf signali.</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Tuzoq 2 — Mantiqiy taxmin (plausible inference).</strong> Matn: "
            "<em>\"Sales fell after the price rise.\"</em> Bayonot: <em>\"The price rise "
            "caused sales to fall.\"</em> Mantiqan ehtimol, lekin matn <u>sabab</u>ni "
            "aytmagan — faqat ketma-ketlikni. Bunday \"sabab qo'shish\" bayonotlari "
            "ko'pincha NOT GIVEN bo'ladi.</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Tuzoq 3 — Aytilmagan taqqoslash (unstated comparison).</strong> "
            "Matn ikki narsani alohida tasvirlaydi, bayonot esa ularni "
            "<em>solishtiradi</em> (\"X is more popular than Y\"). Agar matnda taqqoslash "
            "yo'q bo'lsa — NOT GIVEN, garchi ikkala narsa ham tilga olingan bo'lsa ham!</div>"
        )},
        {"rich_text": (
            "<h3>Namuna parcha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"Handwritten letters have become a rarity in the "
            "digital age. A survey of 2,000 British adults found that half had not "
            "written a personal letter in over a decade. Interestingly, the same survey "
            "showed that people aged over 65 were the group most likely to still send "
            "cards and letters by post. Stationery shops report that sales of quality "
            "writing paper have fallen steadily since 2005, although sales of greeting "
            "cards have remained stable.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bayonot: <em>\"Sales of greeting cards "
                "have decreased since 2005.\"</em> Bu TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "Ziddiyat testi: matn <em>\"sales of greeting cards have remained "
                "stable\"</em> deydi. \"Kamaygan\" va \"barqaror qolgan\" bir vaqtda "
                "to'g'ri bo'la olmaydi — to'g'ridan-to'g'ri ziddiyat, demak FALSE. "
                "Diqqat: yozuv qog'ozi (writing paper) savdosi kamaygan, lekin bayonot "
                "<u>otkritkalar</u> (greeting cards) haqida — IELTS shunday yaqin "
                "tushunchalarni ataylab aralashtiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bayonot: <em>\"Young people consider "
                "handwritten letters old-fashioned.\"</em> Bu TRUE, FALSE yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Bu — Tuzoq 2 (mantiqiy taxmin). Matn 65 yoshdan oshganlar ko'proq xat "
                "yozishini aytadi, va bundan \"yoshlar xatni eskilik deb biladi\" degan "
                "xulosa <em>mantiqan kelib chiqqandek tuyuladi</em> — lekin matnda "
                "yoshlarning <u>fikri/munosabati</u> haqida hech qanday ma'lumot yo'q. "
                "Ziddiyat testi: ikkala gap bir vaqtda to'g'ri bo'la oladi, demak FALSE "
                "emas — NOT GIVEN.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"Fewer than half of the "
                "surveyed adults had written a personal letter in the last ten "
                "years.\"</em> Bu TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Ehtiyot bo'ling — bu nozik holat! Matn: yarmi (half) <u>o'n yildan "
                "beri yozmagan</u>. Demak qolgan yarmi yozgan — lekin bu \"yozganlar "
                "yarmidan <u>kam</u>\" (fewer than half) degani emas: matn aynan "
                "\"half\" deydi, \"fewer than half\" emas. Matn bergan raqam bayonotdagi "
                "raqamga na aniq mos keladi, na aniq zid — bunday \"chegara\" holatlarda "
                "matn aniq tasdiqlamasa, javob NOT GIVEN bo'ladi. Raqamli bayonotlarda "
                "har bir so'zni (fewer than, more than, exactly) tarozida torting.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">contradiction test</div><div class=\"pp-card-back\">ziddiyat testi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">outside knowledge</div><div class=\"pp-card-back\">matndan tashqari (o'z) bilim</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">plausible inference</div><div class=\"pp-card-back\">mantiqiy (lekin isbotlanmagan) xulosa</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">unstated comparison</div><div class=\"pp-card-back\">matnda aytilmagan taqqoslash</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a rarity</div><div class=\"pp-card-back\">kamyob narsa</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to remain stable</div><div class=\"pp-card-back\">barqaror qolmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to fall steadily</div><div class=\"pp-card-back\">muttasil kamaymoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">survey</div><div class=\"pp-card-back\">so'rovnoma</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ziddiyat testi: bayonot va matn jumlasi bir vaqtda to'g'ri bo'la oladimi? Yo'q — FALSE; Ha — NOT GIVEN.</li>"
            "<li>O'z bilimingiz va \"mantiqiy\" taxminlar — NOT GIVEN'ni FALSE deb belgilashga olib boradigan asosiy tuzoqlar.</li>"
            "<li>Matnda taqqoslash bo'lmasa, taqqoslovchi bayonot — NOT GIVEN (ikkala narsa tilga olingan bo'lsa ham).</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 8 (order 13 — T/F/NG full passage practice)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_TFNG,
    "title": "IELTS Reading 8: True/False/Not Given — Full Passage Practice (Mixed Review)",
    "summary": "To'liq parcha ustida TRUE/FALSE/NOT GIVEN bo'yicha aralash amaliyot — barcha o'rganilgan usullarni birlashtirish.",
    "order": 13,
    "blocks": [
        {"rich_text": (
            "<h2>Hammasini birlashtiramiz</h2>"
            "<p>Oxirgi uch darsda siz TRUE/FALSE/NOT GIVEN'ning to'liq qurolini yig'dingiz: "
            "4 bosqichli usul, kalit so'z tanlash, sinonim sezish, tartib qoidasi va "
            "ziddiyat testi. Endi hammasini <strong>haqiqiy imtihon sharoitida</strong> "
            "sinaymiz: bitta to'liq parcha, 5 ta bayonot, hech qanday yordam.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> avval parchani 1 daqiqa <u>skim</u> qiling "
            "(nima haqida ekanini tushunish uchun), keyin har bayonot bilan ishlang: "
            "kalit so'z → scan → ziddiyat testi. Har savolga 1–1,5 daqiqadan mo'ljallang — "
            "haqiqiy imtihondagidek.</div>"
        )},
        {"rich_text": (
            "<h3>O'qing: The Rise and Fall of the Pneumatic Post</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 10px;\">\"In the second half of the nineteenth century, "
            "many large cities faced a communication problem: telegraph offices could "
            "transmit messages across continents in minutes, but delivering those messages "
            "the final few kilometres through crowded streets could take hours. The "
            "solution, first installed in London in 1853, was the pneumatic post — a "
            "network of underground tubes through which capsules containing letters and "
            "telegrams were propelled by compressed air.</p>"
            "<p style=\"margin:0 0 10px;\">Paris built the most extensive system of all. "
            "At its peak, the Parisian network stretched for more than 400 kilometres "
            "beneath the city, and a message posted at one end of the capital could reach "
            "the other in under two hours — far faster than a courier on the congested "
            "streets above. The service proved enormously popular with the public, who "
            "used special lightweight forms known as 'petits bleus' for their messages.</p>"
            "<p style=\"margin:0;\">The pneumatic post declined for a simple reason: the "
            "telephone made it unnecessary for most everyday communication. Berlin closed "
            "its network in 1976, and Paris followed in 1984. Yet the technology has not "
            "disappeared entirely — many hospitals today still use pneumatic tubes to move "
            "blood samples and medicines between departments, where speed and reliability "
            "matter more than cost.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> <em>\"The world's first pneumatic post "
                "system was built in Paris.\"</em> TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "Langar so'zlar: \"first\" va shahar nomlari. Matn: <em>\"first installed "
                "in <u>London</u> in 1853\"</em> — birinchi tizim Londonda o'rnatilgan. "
                "Parij \"the most extensive\" (eng keng) tizimni qurgan, lekin "
                "<u>birinchi</u> emas. \"Eng katta\" va \"birinchi\"ni almashtirish — "
                "IELTS'ning sevimli tuzog'i.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <em>\"At its largest, the Paris network was "
                "over 400 km long.\"</em> TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": True},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: TRUE.</mark> "
                "Sinonim juftliklar: \"at its largest\" ↔ \"at its peak\", \"over 400 km "
                "long\" ↔ \"stretched for more than 400 kilometres\". Raqam (400) langar "
                "bo'lib xizmat qildi. Bayonot matndagi faktni boshqa so'zlar bilan aynan "
                "takrorlayapti — klassik TRUE.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> <em>\"Sending a message by pneumatic post "
                "in Paris was cheaper than using a courier.\"</em> TRUE, FALSE yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Matn pnevmopochta kuryerdan <u>tezroq</u> (\"far faster than a courier\") "
                "ekanini aytadi — lekin <u>arzonroq</u> ekani haqida hech narsa demaydi. "
                "Bu — aytilmagan taqqoslash tuzog'i: taqqoslash bor, lekin boshqa mezon "
                "(tezlik) bo'yicha. \"Tezroq, demak, ehtimol arzonroq hamdir\" — bu "
                "sizning taxminingiz, matn emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> <em>\"Berlin shut down its pneumatic "
                "network before Paris did.\"</em> TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": True},
                {"text": "FALSE", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: TRUE.</mark> "
                "Langar so'zlar: \"Berlin\", \"Paris\" va yillar. Matn: Berlin — 1976, "
                "Parij — 1984 (\"Paris followed\"). 1976 &lt; 1984, demak Berlin oldinroq "
                "yopgan — bayonot to'g'ri. Bu yerda taqqoslash <u>matndagi ikki aniq "
                "faktdan</u> kelib chiqadi — bunday \"hisoblanadigan\" taqqoslash NOT "
                "GIVEN emas, TRUE bo'ladi (3-savolga solishtiring: u yerda kerakli fakt "
                "umuman yo'q edi).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <em>\"Pneumatic tubes are no longer used "
                "anywhere today.\"</em> TRUE, FALSE yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "TRUE", "is_correct": False},
                {"text": "FALSE", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: FALSE.</mark> "
                "Bayonotda ikkita mutlaq so'z bor: \"no longer\" va \"anywhere\" — xavf "
                "signali! Matn: <em>\"the technology has not disappeared entirely — many "
                "hospitals today still use pneumatic tubes\"</em>. Kasalxonalar hozir ham "
                "ishlatadi — bayonotga to'g'ridan-to'g'ri zid, demak FALSE. Ziddiyat "
                "testi bir soniyada ishladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — a'lo! Keyingi mavzuga (Yes/No/Not Given) tayyor siz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>4/5</strong> — juda yaxshi; xato qilgan savol izohini qayta o'qing.</p>"
            "<p style=\"margin:0;\"><strong>3/5 yoki kam</strong> — 5–7-darslarni qayta ko'rib chiqing, ayniqsa ziddiyat testini.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to transmit</div><div class=\"pp-card-back\">uzatmoq, jo'natmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">extensive</div><div class=\"pp-card-back\">keng ko'lamli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at its peak</div><div class=\"pp-card-back\">eng yuqori cho'qqisida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">congested</div><div class=\"pp-card-back\">tirband, gavjum</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to decline</div><div class=\"pp-card-back\">pasaymoq, inqirozga uchramoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to prove popular</div><div class=\"pp-card-back\">ommalashib ketmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">reliability</div><div class=\"pp-card-back\">ishonchlilik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to disappear entirely</div><div class=\"pp-card-back\">butunlay yo'qolmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ish tartibi: 1 daqiqa skim → har bayonot uchun kalit so'z → scan → ziddiyat testi.</li>"
            "<li>\"Birinchi/eng katta\", \"tezroq/arzonroq\" kabi yaqin tushunchalar almashtirilishiga hushyor bo'ling.</li>"
            "<li>Matndagi ikki faktdan hisoblab chiqariladigan taqqoslash — javob bo'la oladi; fakt umuman bo'lmasa — NOT GIVEN.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 9 (order 20 — opens the Yes/No/Not Given topic)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_YNNG,
    "title": "IELTS Reading 9: Intro to Yes/No/Not Given — Writer's Claims and Opinions",
    "summary": "YES/NO/NOT GIVEN savol turi: muallif fikrlari bilan ishlash va uning True/False/Not Given'dan farqi.",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Endi faktlar emas — fikrlar</h2>"
            "<p>TRUE/FALSE/NOT GIVEN <u>faktlar</u>ni tekshirar edi. "
            "<strong>YES/NO/NOT GIVEN</strong> esa <u>muallifning fikrlari, da'volari va "
            "qarashlari</u> (claims, views, opinions) bilan ishlaydi. Savol shakli ham "
            "boshqacha bo'ladi: <em>\"Do the following statements agree with the "
            "<u>claims/views of the writer</u>?\"</em> — shu iborani ko'rsangiz, bilingki, "
            "endi fakt emas, <mark style=\"background:#dbeafe;\">muallif nima deb "
            "hisoblashi</mark> so'ralmoqda.</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>YES</strong> — bayonot muallifning fikri/da'vosiga mos keladi.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>NO</strong> — bayonot muallifning fikri/da'vosiga zid keladi.</p>"
            "<p style=\"margin:0;\"><strong>NOT GIVEN</strong> — muallif bu haqda fikr bildirmagan.</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>T/F/NG bilan farqi nimada?</h3>"
            "<p>Usul deyarli bir xil (kalit so'z → scan → ziddiyat testi), lekin "
            "<strong>nimani tekshirayotganingiz</strong> o'zgaradi:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>T/F/NG:</strong> \"Matn bu <u>faktni</u> "
            "aytganmi?\" Matn odatda tavsifiy (descriptive) bo'ladi: tarix, jarayon, "
            "tadqiqot natijasi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Y/N/NG:</strong> \"Muallif bunga "
            "<u>qo'shiladimi</u>?\" Matn odatda munozarali (argumentative) bo'ladi: "
            "muallif biror pozitsiyani himoya qiladi, tanqid qiladi, baholaydi.</p></div>"
            "<div class=\"pp-step\"><p><strong>Muhim oqibat:</strong> Y/N/NG'da matnda "
            "fakt <em>tilga olingan</em> bo'lishi mumkin, lekin muallif u haqda "
            "<em>fikr bildirmagan</em> bo'lsa — javob baribir NOT GIVEN. Mavzu bor-yo'qligi "
            "emas, <u>munosabat</u> bor-yo'qligi hal qiladi.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Muallif fikrini qanday tanish mumkin?</h3>"
            "<p>Fikr-da'volar matnda maxsus \"signal so'zlar\" bilan keladi. Ularni "
            "ko'rganda \"bu — muallifning pozitsiyasi\" deb belgilab qo'ying:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>argue, claim, believe, maintain, insist</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>da'vo qilmoq, hisoblamoq, ta'kidlamoq</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>should, must, it is essential that, there is no doubt that</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>kerak, shart, shubha yo'qki — kuchli pozitsiya belgilari</em></p>"
            "</div>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"font-size:1.12em;margin:0 0 6px;\"><strong>unfortunately, remarkably, worryingly, at last</strong></p>"
            "<p style=\"color:#475569;margin:0;\"><em>baholovchi so'zlar — muallifning his-tuyg'usini ochib beradi</em></p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> ehtiyot bo'ling — muallif ko'pincha "
            "<u>boshqalarning</u> fikrini ham keltiradi (\"Some researchers argue "
            "that...\"). Savol <u>muallifning o'z pozitsiyasi</u> haqida bo'lsa, "
            "boshqalarning fikri javob emas! Muallif ularga qo'shilishi (\"and they are "
            "right\") yoki qarshi chiqishi (\"but this view ignores...\") mumkin — davomini "
            "o'qing.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna parcha (munozarali uslub)</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"City councils across Europe are investing heavily "
            "in bicycle infrastructure, and in my view this is money well spent. Cycling "
            "reduces congestion, cuts emissions, and improves public health — benefits "
            "that far outweigh the construction costs. Critics argue that cycle lanes "
            "take road space away from motorists, but this objection misses the point: "
            "every person on a bicycle is one less car in the queue. It must be admitted, "
            "however, that cycling is not a realistic option for everyone, and councils "
            "should be careful not to neglect public transport for elderly and disabled "
            "residents.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bayonot: <em>\"Money spent on cycling "
                "infrastructure is wasted.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NO.</mark> "
                "Muallif aniq pozitsiya bildirgan: <em>\"in my view this is money well "
                "spent\"</em> — \"bu pul o'z o'rnida sarflangan\". Bayonot esa \"behuda "
                "sarflangan\" (wasted) deydi — muallif fikriga to'g'ridan-to'g'ri zid, "
                "demak NO. \"in my view\" — muallif pozitsiyasining eng ochiq signali.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bayonot: <em>\"The writer believes "
                "cycling is a practical choice for every resident.\"</em> YES, NO yoki "
                "NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NO.</mark> Matn "
                "oxirida muallif o'zi tan oladi: <em>\"cycling is <u>not</u> a realistic "
                "option for <u>everyone</u>\"</em>. Bayonot buning aksini aytyapti "
                "(\"practical choice for every resident\") — muallif qarashiga zid, "
                "demak NO. E'tibor bering: muallif velosipedni qo'llab-quvvatlaydi, lekin "
                "bu uni <u>har bir</u> da'voga rozi qilmaydi — har bayonotni alohida "
                "tekshiring.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"The writer thinks cycle "
                "lanes should be built in city centres first.\"</em> YES, NO yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Muallif velosiped infratuzilmasini qo'llab-quvvatlaydi, lekin "
                "<u>qayerdan boshlash kerakligi</u> (markazdami, chekkadami) haqida "
                "hech qanday fikr bildirmagan. Mavzu (cycle lanes) matnda bor — lekin "
                "aynan shu <u>da'vo</u> yo'q. Y/N/NG'ning asosiy qoidasi: mavzu emas, "
                "<strong>munosabat</strong> qidiriladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">claim</div><div class=\"pp-card-back\">da'vo</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">writer's view</div><div class=\"pp-card-back\">muallifning qarashi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to argue that</div><div class=\"pp-card-back\">...deb da'vo qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to outweigh</div><div class=\"pp-card-back\">ustun kelmoq, og'irroq kelmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">objection</div><div class=\"pp-card-back\">e'tiroz</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to miss the point</div><div class=\"pp-card-back\">masalaning mohiyatini tushunmaslik</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">it must be admitted</div><div class=\"pp-card-back\">tan olish kerakki</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to neglect</div><div class=\"pp-card-back\">e'tiborsiz qoldirmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Y/N/NG = muallifning <strong>fikri/da'vosi</strong>; T/F/NG = matndagi <strong>fakt</strong>.</li>"
            "<li>Signal so'zlarni qidiring: in my view, argue, should, unfortunately...</li>"
            "<li>Mavzu tilga olingani yetarli emas — aynan shu da'vo haqida muallif pozitsiyasi bo'lishi kerak, aks holda NOT GIVEN.</li>"
            "<li>Boshqalarning fikri (\"critics argue...\") — muallifning fikri emas; muallif unga qo'shilgan-qo'shilmaganini tekshiring.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 10 (order 21 — hedging language / writer's stance)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "reading",
    "topic": TOPIC_YNNG,
    "title": "IELTS Reading 10: Spotting the Writer's Stance — Hedging Language (may, could, arguably)",
    "summary": "Muallif pozitsiyasining kuchini o'lchash: hedging (yumshatuvchi) til va uning YES/NO/NOT GIVEN'dagi roli.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>\"Ehtimol\" bilan \"aniq\" orasidagi farq</h2>"
            "<p>Akademik mualliflar kamdan-kam hollarda \"X is true\" deb yozadi. Ular "
            "<strong>hedging</strong> — <mark style=\"background:#dbeafe;\">yumshatuvchi, "
            "ehtiyotkor til</mark> — ishlatadi: <em>may, might, could, tend to, arguably, "
            "it seems that</em>. IELTS Y/N/NG savollari aynan shu nozikliklarni sinaydi: "
            "bayonot muallifning <u>ehtiyotkor</u> fikrini <u>qat'iy</u> qilib ko'rsatsa "
            "— bu endi muallifning fikri emas!</p>"
        )},
        {"rich_text": (
            "<h3>Hedging shkalasi — kuchni o'lchang</h3>"
            "<p>Har bir da'voni xayolan shkalaga qo'ying:</p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>100% — qat'iy:</strong> <em>certainly, "
            "undoubtedly, must, will, there is no doubt that</em>. "
            "<span style=\"background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;\">kuchli</span></p></div>"
            "<div class=\"pp-step\"><p><strong>~75% — ishonchli, lekin ochiq:</strong> "
            "<em>likely, probably, appears to, strongly suggests</em>.</p></div>"
            "<div class=\"pp-step\"><p><strong>~50% — ehtiyotkor:</strong> <em>may, "
            "might, could, perhaps, arguably, tends to, in some cases</em>. "
            "<span style=\"background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;\">hedge</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Taqqoslang:</strong> matn <em>\"stress "
            "<u>may contribute</u> to heart disease\"</em> desa, muallif 50% darajada "
            "gapiryapti. Bayonot <em>\"stress <u>causes</u> heart disease\"</em> desa — "
            "bu 100% darajadagi da'vo. Muallif bunday <u>kuchli</u> gapga imzo "
            "chekmagan!</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Daraja mos kelmasa, javob nima bo'ladi?</h3>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> matn \"may cause\" desa-yu, bayonot \"causes\" "
            "desa — muallif bu kuchli da'voni <u>bildirmagan</u>, demak ko'p hollarda "
            "javob <strong>NOT GIVEN</strong> bo'ladi. NO faqat muallif bayonotga "
            "<u>zid</u> pozitsiya bildirganda qo'yiladi (masalan, matn \"X does NOT "
            "cause Y\" yoki \"it is wrong to say X causes Y\" desa). \"Aytmagan\" va "
            "\"rad etgan\" — boshqa-boshqa narsalar.</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> bayonotdagi fe'l-modallarni aylanaga oling "
            "(causes? may cause? always? sometimes?), keyin matndagi mos jumlaning "
            "darajasi bilan yonma-yon qo'ying. Daraja aynan mos kelsa — YES; muallif "
            "teskarisini aytsa — NO; muallif bunchalik kuchli (yoki umuman) gapirmagan "
            "bo'lsa — NOT GIVEN.</div>"
        )},
        {"rich_text": (
            "<h3>Namuna parcha</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\">\"The effect of open-plan offices on productivity "
            "remains hotly debated. Advocates point to easier collaboration, yet the "
            "evidence suggests that constant noise and interruption may actually reduce "
            "deep, focused work. Employees in open-plan spaces tend to report higher "
            "levels of stress, and some studies have found they take more sick days than "
            "colleagues in private offices. It would be premature, however, to conclude "
            "that open-plan design is always a mistake: for teams whose work depends on "
            "rapid communication, the format arguably still has real advantages.\"</p>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Bayonot: <em>\"Open-plan offices "
                "definitely reduce focused work.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": True},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NOT GIVEN.</mark> "
                "Matn: <em>\"the evidence suggests that ... <u>may actually reduce</u> "
                "deep, focused work\"</em> — bu ~50% li, ehtiyotkor da'vo (suggests + "
                "may). Bayonot esa <mark style=\"background:#fee2e2;\">\"definitely\"</mark> "
                "deydi — 100% daraja. Muallif bunday qat'iy gapni aytmagan, lekin uni rad "
                "ham etmagan — demak NOT GIVEN. Daraja farqi — Y/N/NG'ning eng nozik "
                "tuzog'i.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Bayonot: <em>\"The writer believes "
                "open-plan offices are always a bad idea.\"</em> YES, NO yoki NOT "
                "GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": False},
                {"text": "NO", "is_correct": True},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: NO.</mark> Bu "
                "safar muallif bayonotga <u>ochiq zid</u> pozitsiya bildirgan: <em>\"It "
                "would be premature ... to conclude that open-plan design is <u>always a "
                "mistake</u>\"</em> va \"arguably still has real advantages\". Ya'ni "
                "muallif \"har doim yomon\" degan qarashni <strong>rad etadi</strong> — "
                "shuning uchun NOT GIVEN emas, NO. 1-amaliyot bilan solishtiring: u yerda "
                "muallif jim edi, bu yerda esa qarshi gapirdi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Bayonot: <em>\"Employees in open-plan "
                "offices tend to feel more stressed.\"</em> YES, NO yoki NOT GIVEN?</p>"
            ),
            "choices": [
                {"text": "YES", "is_correct": True},
                {"text": "NO", "is_correct": False},
                {"text": "NOT GIVEN", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: YES.</mark> Matn: "
                "<em>\"Employees in open-plan spaces <u>tend to</u> report higher levels "
                "of stress\"</em>. Bayonot ham xuddi shu darajada gapiryapti: \"<u>tend "
                "to</u> feel more stressed\" — daraja mos! Hedging'ning o'zi muammo emas "
                "— muammo <u>darajalar mos kelmasligi</u>da. Bayonot muallif darajasini "
                "saqlagan bo'lsa, bemalol YES bo'la oladi.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">hedging</div><div class=\"pp-card-back\">yumshatish, ehtiyotkor ifoda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">stance</div><div class=\"pp-card-back\">pozitsiya, munosabat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">arguably</div><div class=\"pp-card-back\">bahsli bo'lsa-da, aytish mumkinki</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to tend to</div><div class=\"pp-card-back\">moyil bo'lmoq, odatda ...moq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">premature</div><div class=\"pp-card-back\">erta, shoshilinch (xulosa)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">advocate</div><div class=\"pp-card-back\">tarafdor</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">hotly debated</div><div class=\"pp-card-back\">qizg'in bahs-munozarali</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the evidence suggests</div><div class=\"pp-card-back\">dalillar ...ga ishora qiladi</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Muallif darajasini o'lchang: certainly (100%) → likely (75%) → may/arguably (50%).</li>"
            "<li>Bayonot muallifdan <strong>kuchliroq</strong> gapirsa — odatda NOT GIVEN (muallif u gapni aytmagan).</li>"
            "<li>NO — faqat muallif bayonotga <strong>zid</strong> pozitsiyani ochiq bildirganda.</li>"
            "<li>Daraja mos kelsa (tend to ↔ tend to), hedging'li bayonot ham YES bo'la oladi.</li>"
            "</ul>"
        )},
    ],
},

]
