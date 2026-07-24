"""
IELTS Listening lessons 4-6 (orders 10-12) — the "1-bo'lim: Forma/eslatma to'ldirish
(Section 1 — Form/Note Completion)" topic — second Listening batch,
see toc_ielts_listening.txt.

Each lesson is built around ONE two-speaker conversation clip (Woman/Man = en-GB
voices), with several form/note fields as questions. Generate the mp3s with:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_section1_10_12.py \
        --out examprep/management/commands/audio/ielts_listening_section1
then import with --audio-dir pointing at that folder.

NOTE (speaker names in audio): the tuple's first element (Woman/Man) only CHOOSES the
voice — it is never spoken. Never write a name into the line text. See
STYLE_GUIDE_IELTS.md §5c.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_SECTION1 = {
    "title":   "1-bo'lim: Forma/eslatma to'ldirish (Section 1 — Form/Note Completion)",
    "summary": "Kundalik ikki kishilik suhbat: forma va eslatmalarni to'ldirish — ism, "
               "manzil, raqam, sana va tuzatish tuzoqlari.",
    "icon":    "bi-card-checklist",
    "order":   2,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 4 (order 10 — Intro to Section 1) — WITH AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION1,
    "title": "IELTS Listening 4: Intro to Section 1 — Everyday Conversation, Two Speakers",
    "summary": "Section 1 formati: kundalik ikki kishilik suhbat (booking/enquiry), forma to'ldirish; misol javob, forma tuzilishi va tartib.",
    "order": 10,
    "blocks": [
        {"rich_text": (
            "<h2>Section 1 — eng qulay ball manbai</h2>"
            "<p>1-bo'lim — <strong>kundalik hayotiy suhbat</strong>: ikki kishi biror "
            "amaliy ish yuzasidan gaplashadi — joy band qilish, kursga yozilish, "
            "so'rov (booking/enquiry). Bir kishi ma'lumot beradi, ikkinchisi uni "
            "<u>formaga</u> yozadi — siz ham xuddi shu formani to'ldirasiz.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Yaxshi xabar:</strong> bu eng oson bo'lim — til sodda, ma'lumot "
            "aniq (ism, raqam, sana), va forma sizga <u>nima eshitishni</u> oldindan "
            "aytadi. Bu yerda 10 savolning ko'pini to'g'ri yeching — kuchni 3–4-bo'limga "
            "saqlash uchun.</div>"
        )},
        {"rich_text": (
            "<h3>Ikki muhim format detali</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Misol javob (example).</strong> "
            "Section 1 boshida bitta savol <u>namuna</u> sifatida oldindan javoblanadi — "
            "audio o'sha qismni bir marta qo'yib, javobni ko'rsatadi. Bu — quloqni "
            "ovozlarga \"sozlash\" imkoniyati; e'tibor bilan tinglang, lekin uni "
            "javoblamang (allaqachon berilgan).</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Forma — sizning xaritangiz.</strong> "
            "Formadagi maydonlar (Name, Date, Number...) tartib bilan to'ldiriladi va "
            "audio ham shu tartibda boradi. Har maydon yonidagi <u>yorliq</u> qanday "
            "ma'lumot kelishini aytadi.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Oldingi dars usulini qo'llang.</strong> "
            "Audio boshlanmasdan har maydonning javob turini bashorat qiling: bu yerga "
            "son keladimi? ism? sana? — quloq shunga tayyor bo'ladi.</p></div>"
            "</div>"
        )},
        {
            "audio":        "ielts_l_010_1.mp3",
            "audio_script": [
                ("Woman", "Good afternoon, Oakwood Community Centre. How can I help you?"),
                ("Man",   "Hello, I'd like to book a room for a party, please."),
                ("Woman", "Certainly. What kind of event is it?"),
                ("Man",   "It's a birthday party, for my daughter."),
                ("Woman", "Lovely. And what date did you have in mind?"),
                ("Man",   "The fourteenth of May. It's a Saturday, I think."),
                ("Woman", "Yes, the fourteenth is a Saturday, and it's free. How many guests are you expecting?"),
                ("Man",   "Around forty, maybe forty-five at most."),
                ("Woman", "In that case I'd recommend the Garden Room. It holds up to fifty. The smaller Oak Room only takes thirty, so that would be too tight."),
                ("Man",   "The Garden Room sounds ideal."),
                ("Woman", "Great. To confirm the booking, there's a deposit of thirty pounds."),
                ("Man",   "No problem. I'll pay that now."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta) va formani to'ldiring.</strong> "
                "Oakwood jamoat markaziga qo'ng'iroq. Quyidagi bandlarga e'tibor bering, "
                "keyin pastdagi savollarga javob bering:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>ROOM BOOKING FORM</strong></p>"
                "<p style=\"margin:0 0 4px;\">Type of event: <strong>(1) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">Date: 14 May (Saturday)</p>"
                "<p style=\"margin:0 0 4px;\">Room booked: <strong>(2) ______</strong></p>"
                "<p style=\"margin:0;\">Deposit: £<strong>(3) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin quyidagi skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Good afternoon, Oakwood Community Centre. How can I help you?<br>"
                "<em style=\"color:#475569;\">Xayrli kun, Oakwood jamoat markazi. Sizga qanday yordam bera olaman?</em></p>"
                "<p><strong>Man:</strong> Hello, I'd like to book a room for a party, please.<br>"
                "<em style=\"color:#475569;\">Salom, bazm uchun xona band qilmoqchi edim.</em></p>"
                "<p><strong>Woman:</strong> Certainly. What kind of event is it?<br>"
                "<em style=\"color:#475569;\">Albatta. Bu qanday tadbir?</em></p>"
                "<p><strong>Man:</strong> It's a birthday party, for my daughter.<br>"
                "<em style=\"color:#475569;\">Bu tug'ilgan kun bazmi, qizim uchun.</em></p>"
                "<p><strong>Woman:</strong> Lovely. And what date did you have in mind?<br>"
                "<em style=\"color:#475569;\">Ajoyib. Qaysi sanani mo'ljallayapsiz?</em></p>"
                "<p><strong>Man:</strong> The fourteenth of May. It's a Saturday, I think.<br>"
                "<em style=\"color:#475569;\">14-may. Menimcha, u shanba kuni.</em></p>"
                "<p><strong>Woman:</strong> Yes, the fourteenth is a Saturday, and it's free. How many guests are you expecting?<br>"
                "<em style=\"color:#475569;\">Ha, 14-si shanba va bo'sh. Necha mehmon kutyapsiz?</em></p>"
                "<p><strong>Man:</strong> Around forty, maybe forty-five at most.<br>"
                "<em style=\"color:#475569;\">Qariyb 40, ko'pi bilan 45.</em></p>"
                "<p><strong>Woman:</strong> In that case I'd recommend the Garden Room. It holds up to fifty. The smaller Oak Room only takes thirty, so that would be too tight.<br>"
                "<em style=\"color:#475569;\">Unda men Garden Room'ni tavsiya qilaman. U 50 kishigacha sig'adi. Kichikroq Oak Room faqat 30 kishilik, juda tor bo'ladi.</em></p>"
                "<p><strong>Man:</strong> The Garden Room sounds ideal.<br>"
                "<em style=\"color:#475569;\">Garden Room juda mos ekan.</em></p>"
                "<p><strong>Woman:</strong> Great. To confirm the booking, there's a deposit of thirty pounds.<br>"
                "<em style=\"color:#475569;\">Ajoyib. Bandlovni tasdiqlash uchun 30 funt oldindan to'lov bor.</em></p>"
                "<p><strong>Man:</strong> No problem. I'll pay that now.<br>"
                "<em style=\"color:#475569;\">Muammo yo'q. Hozir to'layman.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Type of event — formaga qaysi so'z(lar) "
                "tushadi?</p>"
            ),
            "choices": [
                {"text": "birthday party", "is_correct": True},
                {"text": "wedding", "is_correct": False},
                {"text": "meeting", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: birthday party.</mark> "
                "Erkak aniq aytadi: <em>\"It's a <u>birthday party</u>, for my "
                "daughter.\"</em> Forma yorlig'i (\"Type of event\") aynan shu javobga "
                "ishora qilgan — oldindan bashorat qilgan bo'lsangiz, darhol "
                "ushladingiz.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Room booked — qaysi xona band qilindi?</p>"
            ),
            "choices": [
                {"text": "the Oak Room", "is_correct": False},
                {"text": "the Garden Room", "is_correct": True},
                {"text": "the Community Hall", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: the Garden "
                "Room.</mark> Distraktor tuzog'iga e'tibor bering: audioda <u>ikki</u> "
                "xona tilga olinadi — Garden Room (50 kishilik) va Oak Room (30 kishilik). "
                "Oak Room \"too tight\" (juda tor) deb rad etiladi; erkak Garden Room'ni "
                "tanlaydi. Ikkala nomni ham eshitasiz, lekin faqat bittasi javob — "
                "shoshib birinchisini yozmang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Deposit — oldindan to'lov qancha?</p>"
            ),
            "choices": [
                {"text": "£13", "is_correct": False},
                {"text": "£30", "is_correct": True},
                {"text": "£50", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: £30.</mark> "
                "<em>\"a deposit of <u>thirty</u> pounds\"</em>. Ikki tuzoq bir joyda: "
                "(a) \"thirty\" (30) va \"thirteen\" (13) — urg'udan farqlang (thir-TEEN "
                "oxirida kuchli); (b) \"fifty\" (50) — bu Garden Room sig'imi edi, to'lov "
                "emas (so'z-tuzoq). Javob: 30 funt.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to book a room</div><div class=\"pp-card-back\">xona band qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a deposit</div><div class=\"pp-card-back\">oldindan to'lov, zakalat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to hold (up to fifty)</div><div class=\"pp-card-back\">(50 kishigacha) sig'moq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to confirm a booking</div><div class=\"pp-card-back\">bandlovni tasdiqlamoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to recommend</div><div class=\"pp-card-back\">tavsiya qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an enquiry</div><div class=\"pp-card-back\">so'rov, ma'lumot olish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">guests</div><div class=\"pp-card-back\">mehmonlar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">too tight</div><div class=\"pp-card-back\">juda tor (joy)</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Section 1 — kundalik 2 kishilik suhbat (booking/enquiry), forma to'ldirish; eng oson bo'lim.</li>"
            "<li>Boshida bitta MISOL javob beriladi — quloqni sozlash uchun, uni javoblamang.</li>"
            "<li>Forma maydonlari audio tartibida to'ldiriladi; har yorliq javob turini aytadi.</li>"
            "<li>Distraktor: ikki variant aytiladi, biri rad etiladi — shoshib birinchisini yozmang.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 5 (order 11 — Form Completion: names, addresses, reference numbers) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION1,
    "title": "IELTS Listening 5: Form Completion — Names, Addresses and Reference Numbers",
    "summary": "Section 1 'qattiq ma'lumoti': familiyani harflab yozish, manzil va pochta indeksi, harf+raqamli a'zolik raqami — clarification tuzog'i bilan.",
    "order": 11,
    "blocks": [
        {"rich_text": (
            "<h2>Qattiq ma'lumot: harf va raqamlar</h2>"
            "<p>Forma to'ldirishning eng ko'p ball keltiradigan — va eng ko'p ball "
            "yo'qotadigan — qismi: <strong>ismlar, manzillar va raqamlar</strong>. Bu "
            "yerda bitta harf xato bo'lsa, javob noto'g'ri. Bu dars uni mashq qiladi: "
            "3-darsdagi imlo/raqam ko'nikmalarini jonli suhbatda sinaymiz.</p>"
        )},
        {"rich_text": (
            "<h3>Uch tur qattiq ma'lumot</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Ismlar/familiyalar:</strong> deyarli har doim harflab aytiladi. Yozib boring, keyin qayta o'qib tekshiring. Notanish ism = albatta harflab beriladi.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Manzil:</strong> uy raqami + ko'cha nomi (+ turi: Road/Street/Avenue/Lane) + pochta indeksi (postcode). UK postcode: harf-raqam aralash, masalan <em>LS6 3BQ</em>.</p>"
            "<p style=\"margin:0;\"><strong>Ma'lumotnoma/a'zolik raqami:</strong> ko'pincha harf + raqam aralash (masalan <em>CD4471</em>). \"double\" = takror; harf va raqamlarni ajratib yozing.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma — clarification (aniqlashtirish):</strong> tinglovchi "
            "ba'zan qayta so'raydi: <em>\"Sorry, was that double-four or double-seven?\"</em> "
            "Bu — sizga <u>ikkinchi imkoniyat</u>: to'g'ri javob shundan keyin aniq "
            "takrorlanadi. Bunday qayta-so'rashni kutib turing.</div>"
        )},
        {
            "audio":        "ielts_l_011_1.mp3",
            "audio_script": [
                ("Man",   "Welcome to Central Library. I can set up your membership now. Can I take your surname?"),
                ("Woman", "Yes, it's Fitzgerald."),
                ("Man",   "Could you spell that for me?"),
                ("Woman", "Of course. F-I-T-Z-G-E-R-A-L-D."),
                ("Man",   "Thank you. And your home address?"),
                ("Woman", "It's twenty-three Maple Avenue."),
                ("Man",   "Twenty-three Maple Avenue. And the postcode?"),
                ("Woman", "It's L-S-six, three-B-Q."),
                ("Man",   "Lovely. I'll generate your membership number now. It's C-D-double-four-seven-one."),
                ("Woman", "Sorry, was that double-four or double-seven?"),
                ("Man",   "Double-four. So the full number is C-D-four-four-seven-one."),
                ("Woman", "Got it, thank you."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta) va formani to'ldiring.</strong> "
                "Central Library a'zoligiga yozilish. Harf va raqamlarga alohida diqqat:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>LIBRARY MEMBERSHIP FORM</strong></p>"
                "<p style=\"margin:0 0 4px;\">Surname: <strong>(1) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">Address: 23 Maple Avenue</p>"
                "<p style=\"margin:0 0 4px;\">Postcode: <strong>(2) ______</strong></p>"
                "<p style=\"margin:0;\">Membership number: <strong>(3) ______</strong></p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Man:</strong> Welcome to Central Library. I can set up your membership now. Can I take your surname?<br>"
                "<em style=\"color:#475569;\">Central Library'ga xush kelibsiz. A'zoligingizni hozir rasmiylashtira olaman. Familiyangizni ayta olasizmi?</em></p>"
                "<p><strong>Woman:</strong> Yes, it's Fitzgerald.<br>"
                "<em style=\"color:#475569;\">Ha, Fitzgerald.</em></p>"
                "<p><strong>Man:</strong> Could you spell that for me?<br>"
                "<em style=\"color:#475569;\">Uni harflab ayta olasizmi?</em></p>"
                "<p><strong>Woman:</strong> Of course. F-I-T-Z-G-E-R-A-L-D.<br>"
                "<em style=\"color:#475569;\">Albatta. F-I-T-Z-G-E-R-A-L-D.</em></p>"
                "<p><strong>Man:</strong> Thank you. And your home address?<br>"
                "<em style=\"color:#475569;\">Rahmat. Uy manzilingiz?</em></p>"
                "<p><strong>Woman:</strong> It's twenty-three Maple Avenue.<br>"
                "<em style=\"color:#475569;\">23 Maple Avenue.</em></p>"
                "<p><strong>Man:</strong> Twenty-three Maple Avenue. And the postcode?<br>"
                "<em style=\"color:#475569;\">23 Maple Avenue. Pochta indeksi?</em></p>"
                "<p><strong>Woman:</strong> It's L-S-six, three-B-Q.<br>"
                "<em style=\"color:#475569;\">LS6 3BQ.</em></p>"
                "<p><strong>Man:</strong> Lovely. I'll generate your membership number now. It's C-D-double-four-seven-one.<br>"
                "<em style=\"color:#475569;\">Ajoyib. A'zolik raqamingizni hozir yarataman. CD-4-4-7-1.</em></p>"
                "<p><strong>Woman:</strong> Sorry, was that double-four or double-seven?<br>"
                "<em style=\"color:#475569;\">Kechirasiz, 44 mi yoki 77 mi edi?</em></p>"
                "<p><strong>Man:</strong> Double-four. So the full number is C-D-four-four-seven-one.<br>"
                "<em style=\"color:#475569;\">44. Demak to'liq raqam CD-4-4-7-1.</em></p>"
                "<p><strong>Woman:</strong> Got it, thank you.<br>"
                "<em style=\"color:#475569;\">Tushundim, rahmat.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Surname — familiya qanday yoziladi?</p>"
            ),
            "choices": [
                {"text": "Fitzgerald", "is_correct": True},
                {"text": "Fitzgerold", "is_correct": False},
                {"text": "Fitzgarald", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Fitzgerald.</mark> "
                "Harflab berildi: F-I-T-Z-G-E-R-A-L-D. Imlo aniq: \"-ger<u>a</u>ld\" "
                "(A bilan, O emas). Harflab aytilganda harfma-harf yozib boring — bu "
                "yerda imlo xatosi eng ko'p ball yeydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Postcode — pochta indeksi qaysi?</p>"
            ),
            "choices": [
                {"text": "LS6 3BQ", "is_correct": True},
                {"text": "LS6 3BG", "is_correct": False},
                {"text": "LX6 3BQ", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: LS6 3BQ.</mark> "
                "\"L-S-six, three-B-Q\". Chalkashadigan tovushlar: <strong>S</strong> "
                "/es/ ↔ <strong>X</strong> /eks/, va oxirida <strong>Q</strong> /kyu/ ↔ "
                "<strong>G</strong> /jiy/. Har harfning tovushini aniq eshiting — UK "
                "postcode harf+raqam+harf tuzilishida.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Membership number — a'zolik raqami qaysi?</p>"
            ),
            "choices": [
                {"text": "CD7741", "is_correct": False},
                {"text": "CD4471", "is_correct": True},
                {"text": "CD4741", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: CD4471.</mark> "
                "Clarification tuzog'i: erkak \"C-D-<u>double-four</u>-seven-one\" deydi, "
                "ayol qayta so'raydi (\"double-four or double-seven?\"), va u tasdiqlaydi: "
                "\"<u>Double-four</u>... C-D-four-four-seven-one\". Qayta-so'rash — sizga "
                "aniq javobni beradi: <strong>CD4471</strong>. \"double\" = ikki marta.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">surname</div><div class=\"pp-card-back\">familiya</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to spell (out)</div><div class=\"pp-card-back\">harflab aytmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">postcode</div><div class=\"pp-card-back\">pochta indeksi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">membership number</div><div class=\"pp-card-back\">a'zolik raqami</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to set up / generate</div><div class=\"pp-card-back\">rasmiylashtirmoq / yaratmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Avenue / Lane</div><div class=\"pp-card-back\">xiyobon / ko'cha (tor)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a clarification</div><div class=\"pp-card-back\">aniqlashtirish (qayta so'rash)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">home address</div><div class=\"pp-card-back\">uy manzili</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Ismlar deyarli har doim harflab beriladi — harfma-harf yozing, keyin tekshiring.</li>"
            "<li>UK postcode = harf+raqam aralash (LS6 3BQ); S/X, Q/G tovushlarini farqlang.</li>"
            "<li>A'zolik raqami — harf+raqam; \"double\" = takror.</li>"
            "<li>Clarification (qayta so'rash) — ikkinchi imkoniyat: to'g'ri javob shundan keyin aniq keladi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 6 (order 12 — Note Completion, mixed review) — AUDIO
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION1,
    "title": "IELTS Listening 6: Note Completion — Full Section 1 Practice (Mixed Review)",
    "summary": "To'liq Section 1 amaliyoti: eslatma to'ldirish, aralash ma'lumot turlari (a'zolik, narx, kunlar, buyumlar) — distraktor va tuzatish tuzoqlari bilan.",
    "order": 12,
    "blocks": [
        {"rich_text": (
            "<h2>To'liq amaliyot: eslatma to'ldirish</h2>"
            "<p>Endi hammasi birga. Note completion — forma emas, <strong>eslatmalar</strong> "
            "(sarlavha + bandlar) ko'rinishida, lekin qoidalar bir xil: matndan aynan "
            "so'z, so'z chegarasi, imlo. Bu — to'liq Section 1: bitta uzun suhbat, aralash "
            "ma'lumot turlari va bir nechta tuzoq.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> avval eslatmalarni o'qing (har band qanday "
            "ma'lumot so'rayapti?), keyin bir marta tinglang. 5 savolning hammasi shu "
            "bitta suhbatda — tartib bilan keladi.</div>"
        )},
        {
            "audio":        "ielts_l_012_1.mp3",
            "audio_script": [
                ("Woman", "Good morning, Riverside Fitness. How can I help?"),
                ("Man",   "Hi, I'm thinking of joining. What membership options do you have?"),
                ("Woman", "We have three: Standard, Off-Peak, and Premium. For most people I'd recommend Premium, because it includes all the classes."),
                ("Man",   "How much is Premium per month?"),
                ("Woman", "Premium is forty-five pounds a month. Standard is thirty-five, but that doesn't cover any classes."),
                ("Man",   "I see. And which classes are the most popular?"),
                ("Woman", "They're all included with Premium, but the two people book most are yoga and spinning."),
                ("Man",   "Great. Is there anything I need to do before my first workout?"),
                ("Woman", "Yes, everyone completes an induction session with a trainer. I could book you in for Thursday?"),
                ("Man",   "Thursday's difficult for me, I'm afraid. Could we do Friday instead?"),
                ("Woman", "Friday's fine. And for your first visit, please bring a towel and some photo ID."),
                ("Man",   "A towel and photo ID. Perfect, thanks."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta) va eslatmalarni to'ldiring.</strong> "
                "Riverside Fitness'ga a'zolik so'rovi:</p>"
                "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
                "<p style=\"margin:0 0 4px;\"><strong>GYM ENQUIRY — NOTES</strong></p>"
                "<p style=\"margin:0 0 4px;\">Recommended membership: <strong>(1) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">Monthly fee: £<strong>(2) ______</strong></p>"
                "<p style=\"margin:0 0 4px;\">Two most popular classes: <strong>(3) ______</strong> and spinning</p>"
                "<p style=\"margin:0 0 4px;\">Induction session booked for: <strong>(4) ______</strong></p>"
                "<p style=\"margin:0;\">Bring on first visit: a <strong>(5) ______</strong> and photo ID</p>"
                "</div>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 5 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Good morning, Riverside Fitness. How can I help?<br>"
                "<em style=\"color:#475569;\">Xayrli tong, Riverside Fitness. Sizga qanday yordam bera olaman?</em></p>"
                "<p><strong>Man:</strong> Hi, I'm thinking of joining. What membership options do you have?<br>"
                "<em style=\"color:#475569;\">Salom, a'zo bo'lmoqchiman. Qanday a'zolik variantlari bor?</em></p>"
                "<p><strong>Woman:</strong> We have three: Standard, Off-Peak, and Premium. For most people I'd recommend Premium, because it includes all the classes.<br>"
                "<em style=\"color:#475569;\">Uchta bor: Standard, Off-Peak va Premium. Ko'pchilikka Premium'ni tavsiya qilaman, chunki u barcha mashg'ulotlarni o'z ichiga oladi.</em></p>"
                "<p><strong>Man:</strong> How much is Premium per month?<br>"
                "<em style=\"color:#475569;\">Premium oyiga qancha turadi?</em></p>"
                "<p><strong>Woman:</strong> Premium is forty-five pounds a month. Standard is thirty-five, but that doesn't cover any classes.<br>"
                "<em style=\"color:#475569;\">Premium oyiga 45 funt. Standard 35, lekin u hech qanday mashg'ulotni qamrab olmaydi.</em></p>"
                "<p><strong>Man:</strong> I see. And which classes are the most popular?<br>"
                "<em style=\"color:#475569;\">Tushunarli. Qaysi mashg'ulotlar eng ommabop?</em></p>"
                "<p><strong>Woman:</strong> They're all included with Premium, but the two people book most are yoga and spinning.<br>"
                "<em style=\"color:#475569;\">Premium bilan hammasi kiradi, lekin eng ko'p yoziladigan ikkitasi — yoga va spinning.</em></p>"
                "<p><strong>Man:</strong> Great. Is there anything I need to do before my first workout?<br>"
                "<em style=\"color:#475569;\">Ajoyib. Birinchi mashg'ulotdan oldin biror narsa qilishim kerakmi?</em></p>"
                "<p><strong>Woman:</strong> Yes, everyone completes an induction session with a trainer. I could book you in for Thursday?<br>"
                "<em style=\"color:#475569;\">Ha, hamma murabbiy bilan tanishuv mashg'ulotini o'tadi. Sizni payshanbaga yozib qo'yaymi?</em></p>"
                "<p><strong>Man:</strong> Thursday's difficult for me, I'm afraid. Could we do Friday instead?<br>"
                "<em style=\"color:#475569;\">Afsuski, payshanba men uchun qiyin. Uning o'rniga juma bo'ladimi?</em></p>"
                "<p><strong>Woman:</strong> Friday's fine. And for your first visit, please bring a towel and some photo ID.<br>"
                "<em style=\"color:#475569;\">Juma ham bo'ladi. Birinchi tashrifingizga sochiq va fotosuratli hujjat olib keling.</em></p>"
                "<p><strong>Man:</strong> A towel and photo ID. Perfect, thanks.<br>"
                "<em style=\"color:#475569;\">Sochiq va fotosuratli hujjat. Zo'r, rahmat.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Recommended membership — qaysi a'zolik "
                "tavsiya qilinadi?</p>"
            ),
            "choices": [
                {"text": "Standard", "is_correct": False},
                {"text": "Premium", "is_correct": True},
                {"text": "Off-Peak", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Premium.</mark> "
                "<em>\"I'd recommend <u>Premium</u>, because it includes all the "
                "classes.\"</em> Uchala a'zolik ham tilga olinadi (distraktorlar), lekin "
                "\"recommend\" so'zi Premium'ga ishora qiladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Monthly fee — Premium oyiga qancha? "
                "(£ bilan)</p>"
            ),
            "choices": [
                {"text": "£35", "is_correct": False},
                {"text": "£45", "is_correct": True},
                {"text": "£15", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: £45.</mark> "
                "<em>\"Premium is <u>forty-five</u> pounds a month. Standard is "
                "thirty-five...\"</em> Distraktor: £35 — bu Standard narxi, savol esa "
                "(tavsiya qilingan) Premium haqida. Ikkala narxni ham eshitasiz — "
                "qaysi a'zolikka tegishliligini kuzating.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Two most popular classes — \"______ and "
                "spinning\". Bo'sh joyga nima?</p>"
            ),
            "choices": [
                {"text": "yoga", "is_correct": True},
                {"text": "boxing", "is_correct": False},
                {"text": "swimming", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: yoga.</mark> "
                "<em>\"the two people book most are <u>yoga</u> and spinning\"</em>. "
                "Eslatmada \"spinning\" allaqachon berilgan — demak ikkinchisini "
                "(\"yoga\") yozasiz. Bunday \"biri berilgan\" ishoralar javobni "
                "tasdiqlaydi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Induction session — qaysi kunga yozildi?</p>"
            ),
            "choices": [
                {"text": "Thursday", "is_correct": False},
                {"text": "Friday", "is_correct": True},
                {"text": "Tuesday", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: Friday.</mark> "
                "Tuzatish tuzog'i: ayol \"Thursday?\" deb taklif qiladi, erkak "
                "<em>\"Thursday's difficult... Could we do <u>Friday</u> instead?\"</em> "
                "deydi, ayol \"<u>Friday</u>'s fine\" deb tasdiqlaydi. Kelishilgan kun — "
                "Friday (Thursday emas!). \"instead\" — o'zgarish signali.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> Bring on first visit — \"a ______ and photo "
                "ID\". Bo'sh joyga nima?</p>"
            ),
            "choices": [
                {"text": "towel", "is_correct": True},
                {"text": "water bottle", "is_correct": False},
                {"text": "form", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: towel.</mark> "
                "<em>\"please bring a <u>towel</u> and some photo ID\"</em> — erkak "
                "takrorlaydi: \"A towel and photo ID\". \"photo ID\" allaqachon "
                "eslatmada bor, demak bo'sh joyga \"towel\" tushadi. So'z chegarasiga "
                "e'tibor bering (ONE WORD): faqat \"towel\".</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>5/5</strong> — zo'r! Section 1'ni ishonch bilan yechasiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>3–4/5</strong> — yaxshi; distraktor (£35 vs £45) va tuzatish (Thursday→Friday) savollarini qayta tinglang.</p>"
            "<p style=\"margin:0;\"><strong>2/5 yoki kam</strong> — 4–5-darslarga qaytib, oldindan o'qish va signal so'zlarni takrorlang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">membership options</div><div class=\"pp-card-back\">a'zolik variantlari</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">monthly fee</div><div class=\"pp-card-back\">oylik to'lov</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to include / to cover</div><div class=\"pp-card-back\">o'z ichiga olmoq / qamramoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an induction session</div><div class=\"pp-card-back\">tanishuv/kirish mashg'uloti</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a workout</div><div class=\"pp-card-back\">mashg'ulot, trenirovka</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">... instead</div><div class=\"pp-card-back\">... uning o'rniga (o'zgarish signali)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">photo ID</div><div class=\"pp-card-back\">fotosuratli hujjat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a towel</div><div class=\"pp-card-back\">sochiq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Note completion — forma emas, eslatma; qoidalar bir xil (aynan so'z, chegara, imlo).</li>"
            "<li>Distraktor: bir nechta narx/variant aytiladi — qaysi biri SO'RALGANiga bog'lab tinglang.</li>"
            "<li>Tuzatish tuzog'i (\"instead\", \"Thursday's difficult\") — oxirgi, kelishilgan variant to'g'ri.</li>"
            "<li>\"Biri berilgan\" bandlar (spinning, photo ID) qolganini tasdiqlaydi; so'z chegarasiga rioya qiling.</li>"
            "</ul>"
        )},
    ],
},

]
