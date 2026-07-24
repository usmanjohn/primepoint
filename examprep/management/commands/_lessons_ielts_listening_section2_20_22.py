"""
IELTS Listening lessons 7-9 (orders 20-22) — the "2-bo'lim: Ko'p variantli va joy
belgilash (Section 2 — Multiple Choice & Map/Plan Labelling)" topic — third Listening
batch, see toc_ielts_listening.txt.

Section 2 = a MONOLOGUE (one voice; vary Woman/Man across lessons). Lesson 22 carries a
hand-built inline SVG park map (single-quoted attrs so they don't clash with the Python
double-quoted strings) for map labelling. Generate the mp3s with:
    python manage.py gen_examprep_audio \
        examprep/management/commands/_lessons_ielts_listening_section2_20_22.py \
        --out examprep/management/commands/audio/ielts_listening_section2
then import with --audio-dir pointing at that folder.

NOTE (speaker names in audio): the tuple's first element only CHOOSES the voice — it is
never spoken. Keep names out of the line text. See STYLE_GUIDE_IELTS.md §5c.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_SECTION2 = {
    "title":   "2-bo'lim: Ko'p variantli va joy belgilash (Section 2 — Multiple Choice & Map/Plan Labelling)",
    "summary": "Kundalik monolog (ekskursiya, e'lon): ko'p variantli savollar va "
               "xarita/plan belgilash — yo'nalish tilini real vaqtda kuzatish.",
    "icon":    "bi-map",
    "order":   3,
}

# ── shared SVG: Greenfield Park map (used in lesson 22) ──────────────────────
PARK_MAP_SVG = (
    "<div style=\"overflow-x:auto;\">"
    "<svg viewBox='0 0 420 400' style='width:100%;max-width:400px;height:auto;display:block;margin:8px auto;font-family:sans-serif;'>"
    # park background
    "<rect x='2' y='2' width='416' height='396' rx='12' fill='#f0fdf4' stroke='#86efac' stroke-width='2'/>"
    "<text x='210' y='22' font-size='12' fill='#166534' text-anchor='middle'>GREENFIELD PARK (N ↑)</text>"
    # lake
    "<ellipse cx='210' cy='170' rx='62' ry='44' fill='#bae6fd' stroke='#0284c7' stroke-width='1.5'/>"
    "<text x='210' y='175' font-size='12' fill='#0369a1' text-anchor='middle'>Lake</text>"
    # path (vertical, splitting around the lake)
    "<line x1='210' y1='372' x2='210' y2='216' stroke='#d6d3d1' stroke-width='11' stroke-linecap='round'/>"
    "<line x1='210' y1='124' x2='210' y2='66' stroke='#d6d3d1' stroke-width='11' stroke-linecap='round'/>"
    # entrance
    "<rect x='184' y='372' width='52' height='16' rx='3' fill='#fde68a' stroke='#475569' stroke-width='1.5'/>"
    "<text x='210' y='384' font-size='10' fill='#334155' text-anchor='middle'>ENTRANCE</text>"
    # lettered boxes A–E
    "<rect x='272' y='250' width='40' height='30' rx='4' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='292' y='270' font-size='16' font-weight='bold' fill='#dc2626' text-anchor='middle'>A</text>"
    "<rect x='108' y='250' width='40' height='30' rx='4' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='128' y='270' font-size='16' font-weight='bold' fill='#dc2626' text-anchor='middle'>B</text>"
    "<rect x='190' y='32' width='40' height='30' rx='4' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='210' y='52' font-size='16' font-weight='bold' fill='#dc2626' text-anchor='middle'>C</text>"
    "<rect x='344' y='250' width='40' height='30' rx='4' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='364' y='270' font-size='16' font-weight='bold' fill='#dc2626' text-anchor='middle'>D</text>"
    "<rect x='96' y='330' width='40' height='30' rx='4' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='116' y='350' font-size='16' font-weight='bold' fill='#dc2626' text-anchor='middle'>E</text>"
    "</svg>"
    "</div>"
)

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 7 (order 20 — Intro to Section 2, monologue) — AUDIO (Woman)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION2,
    "title": "IELTS Listening 7: Intro to Section 2 — Monologue in an Everyday Context",
    "summary": "Section 2 formati: bitta so'zlovchi monologi (facilities/tur/e'lon); signpost so'zlarni kuzatish va ma'lumot o'zgarishlarini ushlash.",
    "order": 20,
    "blocks": [
        {"rich_text": (
            "<h2>Section 2 — bitta ovoz, uzluksiz nutq</h2>"
            "<p>2-bo'lim hali ham <u>kundalik/ijtimoiy</u> kontekst, lekin endi "
            "<strong>bitta odam gapiradi</strong> (monolog): ekskursiya gidi, sport "
            "markazi xodimi, radio e'loni yoki tadbir taqdimoti. Ikkinchi so'zlovchi "
            "yo'q — demak nutqni bo'lib turadigan savol-javob ham yo'q. Bu uni "
            "1-bo'limdan biroz <mark style=\"background:#fef3c7;\">qiyinroq</mark> "
            "qiladi: oqimni o'zingiz kuzatasiz.</p>"
        )},
        {"rich_text": (
            "<h3>Signpost so'zlar — nutqning yo'l belgilari</h3>"
            "<p>Monologni kuzatishning kaliti — <strong>signpost (yo'l ko'rsatkich) "
            "so'zlar</strong>. Ular so'zlovchi mavzuni o'zgartirayotganini yoki muhim "
            "narsa kelayotganini bildiradi:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Boshlash/tartib:</strong> <em>\"First of all...\", \"Let me start with...\", \"Moving on to...\", \"Finally...\"</em></p>"
            "<p style=\"margin:0 0 6px;\"><strong>Muhim ma'lumot:</strong> <em>\"One thing to note...\", \"Please remember...\", \"Importantly...\"</em></p>"
            "<p style=\"margin:0 0 6px;\"><strong>O'zgarish/istisno:</strong> <em>\"However...\", \"but...\", \"unlike before...\", \"currently...\"</em></p>"
            "<p style=\"margin:0;\"><strong>Joy (map uchun):</strong> <em>\"on your left/right...\", \"opposite...\", \"at the end of...\"</em></p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> Section 2 tez-tez <u>o'zgarishlar</u> haqida "
            "gapiradi: \"the pool <em>now</em> closes at eight\", \"the sauna is "
            "<em>currently</em> closed\". Savol ko'pincha aynan shu YANGI holatni "
            "so'raydi — \"now/currently\" so'zlariga quloq soling.</div>"
        )},
        {
            "audio":        "ielts_l_020_1.mp3",
            "audio_script": [
                ("Woman", "Hello everyone, and welcome to the Greenfield Leisure Centre. Let me quickly run through what we offer."),
                ("Woman", "Our main swimming pool is open from six in the morning until ten at night on weekdays. At weekends, though, it closes a little earlier, at eight."),
                ("Woman", "If you prefer to exercise on land, the gym is on the first floor, and it has just been fitted with brand-new equipment."),
                ("Woman", "One thing to note: the sauna is currently closed for repairs, but it should reopen next month."),
                ("Woman", "For families, we run children's swimming lessons on Saturday mornings. These are extremely popular, so booking ahead is essential."),
                ("Woman", "And finally, our cafe on the ground floor now serves hot meals, not just snacks as it did before."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> Greenfield Leisure Centre "
                "haqidagi e'lon. Signpost so'zlar (\"currently\", \"finally\") va "
                "o'zgarishlarga diqqat qiling, keyin savollarga o'ting.</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Hello everyone, and welcome to the Greenfield Leisure Centre. Let me quickly run through what we offer.<br>"
                "<em style=\"color:#475569;\">Assalomu alaykum, Greenfield sport markaziga xush kelibsiz. Nimalar taklif qilishimizni qisqacha aytib beraman.</em></p>"
                "<p><strong>Woman:</strong> Our main swimming pool is open from six in the morning until ten at night on weekdays. At weekends, though, it closes a little earlier, at eight.<br>"
                "<em style=\"color:#475569;\">Asosiy suzish havzamiz ish kunlari ertalab 6 dan kechqurun 10 gacha ochiq. Dam olish kunlari esa biroz erta — soat 8 da yopiladi.</em></p>"
                "<p><strong>Woman:</strong> If you prefer to exercise on land, the gym is on the first floor, and it has just been fitted with brand-new equipment.<br>"
                "<em style=\"color:#475569;\">Quruqlikda mashq qilishni afzal ko'rsangiz, sport zali birinchi qavatda va u endigina yangi jihozlar bilan ta'minlandi.</em></p>"
                "<p><strong>Woman:</strong> One thing to note: the sauna is currently closed for repairs, but it should reopen next month.<br>"
                "<em style=\"color:#475569;\">Bir narsani eslatib o'taman: sauna hozirda ta'mirlash uchun yopiq, lekin kelasi oy qayta ochilishi kerak.</em></p>"
                "<p><strong>Woman:</strong> For families, we run children's swimming lessons on Saturday mornings. These are extremely popular, so booking ahead is essential.<br>"
                "<em style=\"color:#475569;\">Oilalar uchun shanba ertalablari bolalar suzish darslarini o'tkazamiz. Ular juda ommabop, shuning uchun oldindan yozilish shart.</em></p>"
                "<p><strong>Woman:</strong> And finally, our cafe on the ground floor now serves hot meals, not just snacks as it did before.<br>"
                "<em style=\"color:#475569;\">Va nihoyat, pastki qavatdagi kafemiz endi nafaqat yengil taomlar, balki issiq ovqatlar ham beradi.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Dam olish kunlari havza soat nechada "
                "yopiladi?</p>"
            ),
            "choices": [
                {"text": "10 pm", "is_correct": False},
                {"text": "8 pm", "is_correct": True},
                {"text": "6 pm", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 8 pm.</mark> "
                "\"...until ten at night on <u>weekdays</u>. At <u>weekends</u>, though, "
                "it closes a little earlier, at <u>eight</u>.\" Savol dam olish kunlari "
                "(weekends) haqida — javob 8. \"ten\" (10) — ish kunlari vaqti (distraktor). "
                "\"though\" signali o'zgarishni bildiradi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Hozirda qaysi joy foydalanishga yaroqsiz?</p>"
            ),
            "choices": [
                {"text": "sport zali (gym)", "is_correct": False},
                {"text": "sauna", "is_correct": True},
                {"text": "kafe", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: sauna.</mark> "
                "\"the sauna is <u>currently closed</u> for repairs\". \"currently\" — "
                "yangi holat signali. Gym haqida ijobiy gap bor (yangi jihoz), kafe ham "
                "yaxshilangan — faqat sauna yopiq. Ijobiy va salbiy ma'lumotni "
                "aralashtirmang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Bolalar suzish darslari uchun nima qilish "
                "shart?</p>"
            ),
            "choices": [
                {"text": "oldindan yozilish (booking ahead)", "is_correct": True},
                {"text": "maxsus kiyim olib kelish", "is_correct": False},
                {"text": "shanba kuni erta kelish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: oldindan "
                "yozilish.</mark> \"...so <u>booking ahead is essential</u>.\" "
                "\"essential\" = shart. \"Saturday mornings\" — darslar vaqti (savolga "
                "javob emas). Savol \"nima qilish SHART\"ni so'radi — booking ahead.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a monologue</div><div class=\"pp-card-back\">monolog (bir kishi nutqi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">signposting language</div><div class=\"pp-card-back\">yo'l ko'rsatkich so'zlar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">facilities</div><div class=\"pp-card-back\">qulayliklar, imkoniyatlar</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">currently</div><div class=\"pp-card-back\">hozirda (yangi holat signali)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">closed for repairs</div><div class=\"pp-card-back\">ta'mirlash uchun yopiq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">booking ahead is essential</div><div class=\"pp-card-back\">oldindan yozilish shart</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">brand-new</div><div class=\"pp-card-back\">yap-yangi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on weekdays / at weekends</div><div class=\"pp-card-back\">ish kunlari / dam olish kunlari</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Section 2 — bitta so'zlovchi monologi (facilities/tur/e'lon), kundalik kontekst.</li>"
            "<li>Signpost so'zlar (\"first\", \"finally\", \"however\", \"on your left\") oqimni kuzatishga yordam beradi.</li>"
            "<li>\"now/currently\" — yangi holat signali; savol ko'pincha shu yangilikni so'raydi.</li>"
            "<li>Ijobiy va salbiy ma'lumotni ajrating (gym yangi, sauna yopiq).</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 8 (order 21 — Multiple Choice, distractor patterns) — AUDIO (Man)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION2,
    "title": "IELTS Listening 8: Multiple Choice — Distractor Patterns (Said, Then Corrected)",
    "summary": "Listening MCQ: to'g'ri javob paraphrase; distraktor — eshitilgan lekin rad etilgan variant. \"Said then corrected\" tuzog'ini ushlash.",
    "order": 21,
    "blocks": [
        {"rich_text": (
            "<h2>Listening MCQ — Reading'dagi mantiq, tezroq</h2>"
            "<p>Ko'p variantli savol (savol + 3 variant, bitta to'g'ri) Reading'dagi "
            "kabi ishlaydi, lekin real vaqtda: to'g'ri javob <mark "
            "style=\"background:#dcfce7;\">paraphrase</mark> qilingan, distraktorlar esa "
            "audioda <u>eshitiladigan</u> so'zlar. Section 2'ning imzo tuzog'i — "
            "<strong>\"said then corrected\"</strong>: so'zlovchi bir variantni aytadi, "
            "keyin uni almashtiradi.</p>"
            "<div style=\"background:#fee2e2;border-left:4px solid #dc2626;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>🔴 Asosiy tuzoq:</strong> \"variantdagi so'zni eshitdim\" degani "
            "\"to'g'ri\" degani EMAS. Aksincha — audio ko'pincha noto'g'ri variantni "
            "AYNAN so'z bilan aytadi (tanish tuzoq), to'g'risini esa boshqa so'z bilan.</div>"
        )},
        {"rich_text": (
            "<h3>\"Said then corrected\" — o'zgarish signallari</h3>"
            "<p>So'zlovchi rejani yoki faktni o'zgartirsa, oldingi ma'lumot bekor "
            "bo'ladi. Bu signallarni ushlang:</p>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><em>\"...was going to..., but now...\", \"originally..., "
            "however...\", \"sorry, I should say...\", \"actually...\", \"instead...\", "
            "\"...not X, but Y\"</em> — bulardan keyingi ma'lumot ESKIsini almashtiradi.</p>"
            "</div>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Maslahat:</strong> har MCQ uchun uch variantni oldindan o'qing "
            "(oldingi dars usuli). Audio yangraganda har birini \"eshitildi / rad etildi / "
            "tasdiqlandi\" deb belgilang — oxirgi tasdiqlangan variant javob.</div>"
        )},
        {
            "audio":        "ielts_l_021_1.mp3",
            "audio_script": [
                ("Man", "Good morning, everyone, and welcome to the City Transport Museum. Before we start, a few practical points about today's tour."),
                ("Man", "The tour was originally going to begin in the Railway Hall, but because of a school visit this morning, we'll start in the Motorcar Gallery instead."),
                ("Man", "The full tour normally lasts about ninety minutes. Sorry, I should say seventy-five minutes today, as the upper floor is closed."),
                ("Man", "Photography is allowed throughout the museum. However, please don't use flash near the older exhibits, as the light can damage them."),
                ("Man", "At the end, do visit our shop. You'll find it not by the exit, as the old map suggests, but right next to the main entrance."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta).</strong> Transport muzeyi "
                "ekskursiyasi. So'zlovchi rejani bir necha marta o'zgartiradi — "
                "\"instead\", \"sorry\", \"not... but\" signallariga diqqat!</p>"
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval 3 savolga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Man:</strong> Good morning, everyone, and welcome to the City Transport Museum. Before we start, a few practical points about today's tour.<br>"
                "<em style=\"color:#475569;\">Xayrli tong, hammaga, Shahar Transport Muzeyiga xush kelibsiz. Boshlashdan oldin, bugungi ekskursiya haqida bir necha amaliy nuqta.</em></p>"
                "<p><strong>Man:</strong> The tour was originally going to begin in the Railway Hall, but because of a school visit this morning, we'll start in the Motorcar Gallery instead.<br>"
                "<em style=\"color:#475569;\">Ekskursiya dastlab Railway Hall'da boshlanishi kerak edi, lekin bugun ertalabki maktab tashrifi tufayli, uning o'rniga Motorcar Gallery'da boshlaymiz.</em></p>"
                "<p><strong>Man:</strong> The full tour normally lasts about ninety minutes. Sorry, I should say seventy-five minutes today, as the upper floor is closed.<br>"
                "<em style=\"color:#475569;\">To'liq ekskursiya odatda taxminan 90 daqiqa davom etadi. Kechirasiz, bugun 75 daqiqa deyishim kerak, chunki yuqori qavat yopiq.</em></p>"
                "<p><strong>Man:</strong> Photography is allowed throughout the museum. However, please don't use flash near the older exhibits, as the light can damage them.<br>"
                "<em style=\"color:#475569;\">Suratga olish butun muzey bo'ylab ruxsat etilgan. Ammo, eski eksponatlar yonida flesh ishlatmang, chunki yorug'lik ularga zarar yetkazishi mumkin.</em></p>"
                "<p><strong>Man:</strong> At the end, do visit our shop. You'll find it not by the exit, as the old map suggests, but right next to the main entrance.<br>"
                "<em style=\"color:#475569;\">Oxirida, do'konimizga tashrif buyuring. Uni eski xarita ko'rsatganidek chiqish yonida emas, balki asosiy kirish yonida topasiz.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Ekskursiya bugun qayerda boshlanadi?</p>"
            ),
            "choices": [
                {"text": "the Railway Hall", "is_correct": False},
                {"text": "the Motorcar Gallery", "is_correct": True},
                {"text": "the upper floor", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: the Motorcar "
                "Gallery.</mark> \"...originally going to begin in the Railway Hall, "
                "<u>but</u>... we'll start in the Motorcar Gallery <u>instead</u>.\" "
                "\"Railway Hall\" — dastlabki reja (rad etilgan distraktor), \"instead\" "
                "yangi joyni beradi. Tanish so'z (Railway Hall)ni birinchi eshitib, "
                "shoshib belgilamang.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Bugun ekskursiya qancha davom etadi?</p>"
            ),
            "choices": [
                {"text": "90 daqiqa", "is_correct": False},
                {"text": "75 daqiqa", "is_correct": True},
                {"text": "15 daqiqa", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: 75 daqiqa.</mark> "
                "\"...normally lasts about ninety minutes. <u>Sorry, I should say "
                "seventy-five</u> minutes today...\" Tuzatish signali \"sorry, I should "
                "say\". 90 — odatdagi (rad etilgan), 75 — bugungi (to'g'ri). "
                "\"today\" so'zi qaysi biri dolzarbligini aytadi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Do'kon qayerda joylashgan?</p>"
            ),
            "choices": [
                {"text": "chiqish yonida (by the exit)", "is_correct": False},
                {"text": "asosiy kirish yonida (next to the main entrance)", "is_correct": True},
                {"text": "yuqori qavatda", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: asosiy kirish "
                "yonida.</mark> \"...<u>not</u> by the exit, as the old map suggests, "
                "<u>but</u> right next to the main entrance.\" Klassik \"not X but Y\" "
                "tuzilishi: \"by the exit\" — eski/noto'g'ri (rad etildi), \"next to the "
                "main entrance\" — to'g'ri. \"not... but...\"ni eshitsangiz, javob "
                "\"but\"dan keyin.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a distractor</div><div class=\"pp-card-back\">chalg'ituvchi variant</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">originally</div><div class=\"pp-card-back\">dastlab (ko'pincha o'zgaradi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">... instead</div><div class=\"pp-card-back\">... uning o'rniga</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">not X, but Y</div><div class=\"pp-card-back\">X emas, balki Y</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an exhibit</div><div class=\"pp-card-back\">eksponat</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">throughout</div><div class=\"pp-card-back\">butun bo'ylab, hamma joyda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the exit</div><div class=\"pp-card-back\">chiqish</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to damage</div><div class=\"pp-card-back\">zarar yetkazmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>To'g'ri javob = paraphrase; distraktor = eshitiladigan (lekin rad etilgan) so'z.</li>"
            "<li>\"Said then corrected\": originally/but/instead/sorry/not-X-but-Y dan keyingi ma'lumot to'g'ri.</li>"
            "<li>Tanish so'zni birinchi eshitib shoshmang — signal so'zni kuting.</li>"
            "<li>\"today\", \"now\" — qaysi variant dolzarbligini aytadi.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 9 (order 22 — Map/Plan Labelling) — AUDIO (Woman) + SVG map
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "listening",
    "topic": TOPIC_SECTION2,
    "title": "IELTS Listening 9: Map/Plan Labelling — Following Directions in Real Time",
    "summary": "Xarita/plan belgilash: yo'nalish va joy tilini (on your left, opposite, at the northern end) real vaqtda kuzatib, joyni harfga ulash.",
    "order": 22,
    "blocks": [
        {"rich_text": (
            "<h2>Map/Plan Labelling — fazoda yo'l topish</h2>"
            "<p>Sizga <strong>xarita yoki plan</strong> beriladi — bir necha joy harflar "
            "(A, B, C...) bilan belgilangan. So'zlovchi (odatda gid) har joyni "
            "<u>tasvirlaydi</u>, siz esa nomni to'g'ri harfga ulaysiz. Bu — sof "
            "<mark style=\"background:#dbeafe;\">yo'nalish tili</mark> sinovi: real "
            "vaqtda xaritada \"harakatlanasiz\".</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> audio boshlanishidan oldin xaritani "
            "<u>o'rganing</u>: kirish (entrance) qayerda? Shimol (N) qayerda? Belgilangan "
            "joylar (A–E) qayerda? Kirish — sizning boshlang'ich nuqtangiz, chunki gid "
            "\"as you come in...\" deb shundan boshlaydi.</div>"
        )},
        {"rich_text": (
            "<h3>Yo'nalish va joy tili — yod oling</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">on your left / right</div><div class=\"pp-card-back\">chap / o'ng tomoningizda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">opposite / facing</div><div class=\"pp-card-back\">ro'parasida / qarshisida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">next to / beside</div><div class=\"pp-card-back\">yonida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at the end of</div><div class=\"pp-card-back\">oxirida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">straight ahead</div><div class=\"pp-card-back\">to'g'riga, ro'para</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at the northern end</div><div class=\"pp-card-back\">shimoliy chekkada</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">behind / in front of</div><div class=\"pp-card-back\">orqasida / oldida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the far side of</div><div class=\"pp-card-back\">narigi tomoni</div></div>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> \"left/right\" gapiruvchining <u>harakat "
            "yo'nalishi</u>ga qarab bo'ladi (siz kirishdan yurayapsiz deb tasavvur "
            "qiling), xaritadagi sizning chap/o'ngingizga emas. Har doim \"as you walk "
            "in\" holatiga o'zingizni qo'ying.</div>"
        )},
        {
            "audio":        "ielts_l_022_1.mp3",
            "audio_script": [
                ("Woman", "Welcome to Greenfield Park. Let me point out where the main facilities are on your map, so you can find them later."),
                ("Woman", "As you come in through the entrance at the bottom, the path leads straight ahead towards the lake in the centre."),
                ("Woman", "The first building you'll see, on your right along the path, is the cafe."),
                ("Woman", "Directly opposite the cafe, on your left, is the gift shop."),
                ("Woman", "If you follow the path all the way to the far side of the lake, at the northern end, you'll find the bird hide — perfect for watching the ducks."),
                ("Woman", "The toilets are a little hidden: they're just to the right of the cafe, at the eastern edge of the park."),
                ("Woman", "And the information centre is very easy to find — it's right beside the entrance, on your left as you walk in."),
            ],
            "rich_text": (
                "<p><strong>🎧 Tinglang (bir marta) va xaritani belgilang.</strong> "
                "Greenfield Park gidi joylarni tasvirlaydi. Xaritadagi harflarni "
                "(A–E) joy nomlariga ulang:</p>"
                + PARK_MAP_SVG +
                "<p style=\"color:#64748b;font-size:0.94em;\">⚠️ Avval savollarga javob bering, keyin skriptni oching!</p>"
                "<details style=\"background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;\">"
                "<summary style=\"cursor:pointer;font-weight:600;\">📜 Skript va tarjima — bosing</summary>"
                "<div style=\"margin-top:10px;\">"
                "<p><strong>Woman:</strong> Welcome to Greenfield Park. Let me point out where the main facilities are on your map, so you can find them later.<br>"
                "<em style=\"color:#475569;\">Greenfield Park'ga xush kelibsiz. Xaritangizda asosiy joylar qayerdaligini ko'rsatib beray, keyin topa olasiz.</em></p>"
                "<p><strong>Woman:</strong> As you come in through the entrance at the bottom, the path leads straight ahead towards the lake in the centre.<br>"
                "<em style=\"color:#475569;\">Pastdagi kirishdan kirganingizda, yo'l to'g'riga, markazdagi ko'l tomon boradi.</em></p>"
                "<p><strong>Woman:</strong> The first building you'll see, on your right along the path, is the cafe.<br>"
                "<em style=\"color:#475569;\">Yo'l bo'ylab o'ng tomoningizda ko'radigan birinchi bino — kafe.</em></p>"
                "<p><strong>Woman:</strong> Directly opposite the cafe, on your left, is the gift shop.<br>"
                "<em style=\"color:#475569;\">Kafening aynan ro'parasida, chap tomoningizda — sovg'a do'koni.</em></p>"
                "<p><strong>Woman:</strong> If you follow the path all the way to the far side of the lake, at the northern end, you'll find the bird hide — perfect for watching the ducks.<br>"
                "<em style=\"color:#475569;\">Yo'ldan ko'lning narigi tomoniga, shimoliy chekkasiga borsangiz, qushlarni kuzatish uchun ideal — qushxona (bird hide)ni topasiz.</em></p>"
                "<p><strong>Woman:</strong> The toilets are a little hidden: they're just to the right of the cafe, at the eastern edge of the park.<br>"
                "<em style=\"color:#475569;\">Hojatxonalar biroz yashiringan: kafening o'ng tomonida, parkning sharqiy chekkasida.</em></p>"
                "<p><strong>Woman:</strong> And the information centre is very easy to find — it's right beside the entrance, on your left as you walk in.<br>"
                "<em style=\"color:#475569;\">Ma'lumot markazini topish juda oson — u kirish yonida, kirganingizda chap tomoningizda.</em></p>"
                "</div>"
                "</details>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Kafe (the cafe) qaysi harf?</p>"
            ),
            "choices": [
                {"text": "A", "is_correct": True},
                {"text": "B", "is_correct": False},
                {"text": "E", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: A.</mark> "
                "\"The first building... <u>on your right</u> along the path, is the "
                "cafe.\" Kirishdan yurganda o'ng tomon — xaritada A (yo'lning o'ng "
                "tomonida, pastroqda). B — chap tomon (gift shop).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> Sovg'a do'koni (the gift shop) qaysi harf?</p>"
            ),
            "choices": [
                {"text": "A", "is_correct": False},
                {"text": "B", "is_correct": True},
                {"text": "D", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: B.</mark> "
                "\"Directly <u>opposite the cafe, on your left</u>, is the gift shop.\" "
                "Kafe (A) o'ngda edi, ro'parasi — chap tomon = B. \"opposite\" "
                "(ro'parasida) kalit so'z.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> Qushxona (the bird hide) qaysi harf?</p>"
            ),
            "choices": [
                {"text": "C", "is_correct": True},
                {"text": "D", "is_correct": False},
                {"text": "A", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: C.</mark> "
                "\"...the <u>far side of the lake, at the northern end</u>... the bird "
                "hide.\" Shimoliy chekka (N ↑ tepada) = xaritada eng yuqoridagi C. "
                "Ko'lning narigi (shimoliy) tomoni.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> Ma'lumot markazi (the information centre) "
                "qaysi harf?</p>"
            ),
            "choices": [
                {"text": "D", "is_correct": False},
                {"text": "E", "is_correct": True},
                {"text": "C", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: E.</mark> "
                "\"...right <u>beside the entrance, on your left as you walk in</u>.\" "
                "Kirish pastda-markazda, uning yonida chap tomonda = E (pastki chap). "
                "D — kafening o'ng tomonidagi hojatxona (toilets), savol emas.</p>"
            ),
        },
        {"rich_text": (
            "<h3>Natijangizni baholang</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>4/4</strong> — zo'r! Yo'nalish tilini real vaqtda kuzatasiz.</p>"
            "<p style=\"margin:0 0 6px;\"><strong>2–3/4</strong> — yaxshi; \"opposite\", \"far side\", \"beside\" so'zlarini flashcard'da mustahkamlang.</p>"
            "<p style=\"margin:0;\"><strong>0–1/4</strong> — xaritani avval o'rganib (entrance + N qayerda), keyin qayta tinglang.</p>"
            "</div>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a bird hide</div><div class=\"pp-card-back\">qushxona (qush kuzatish joyi)</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a gift shop</div><div class=\"pp-card-back\">sovg'a do'koni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the far side of the lake</div><div class=\"pp-card-back\">ko'lning narigi tomoni</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">the northern / eastern end</div><div class=\"pp-card-back\">shimoliy / sharqiy chekka</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">as you walk in</div><div class=\"pp-card-back\">kirganingizda</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to point out</div><div class=\"pp-card-back\">ko'rsatib bermoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">hidden</div><div class=\"pp-card-back\">yashiringan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">along the path</div><div class=\"pp-card-back\">yo'l bo'ylab</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Avval xaritani o'rganing: entrance (boshlang'ich nuqta) va shimol (N) qayerda.</li>"
            "<li>Yo'nalish tilini yod oling: opposite, on your left/right, at the end of, far side.</li>"
            "<li>\"left/right\" — kirib kelayotgan odam nuqtai nazaridan; o'zingizni \"as you walk in\" holatiga qo'ying.</li>"
            "<li>Belgilangan barcha joylar audio tartibida tasvirlanadi — gidga \"ergashing\".</li>"
            "</ul>"
        )},
    ],
},

]
