"""
IELTS Writing lessons 12-13 (orders 50-51) — the "2-topshiriq: Munozara va yechim
insholari (Task 2 — Discussion & Problem-Solution Essays)" topic — fifth Writing batch,
see toc_ielts_writing.txt. (Academic-only scope — Task 2 is shared by both modules.)

No audio, no charts. Kit: step-reveal (unfold model essays) + flashcards + MCQ (§5b).
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_T2_DISCUSSION = {
    "title":   "2-topshiriq: Munozara va yechim insholari (Task 2 — Discussion & Problem-Solution Essays)",
    "summary": "\"Discuss both views\" (ikki qarashni teng yoritish + o'z fikring) va "
               "\"problem-solution\" (sabab va yechim tuzilmasi) insholari.",
    "icon":    "bi-arrow-left-right",
    "order":   6,
}

LESSONS = [

# ─────────────────────────────────────────────────────────────────────────
# Lesson 12 (order 50 — discuss both views)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_DISCUSSION,
    "title": "IELTS Writing 12: Discuss Both Views Essays — Giving Equal Weight",
    "summary": "\"Discuss both these views and give your own opinion\": ikki qarashni adolatli va teng yoritish + o'z fikringizni aniq bildirish.",
    "order": 50,
    "blocks": [
        {"rich_text": (
            "<h2>\"Discuss both views and give your own opinion\"</h2>"
            "<p>Bu savol turida sizga <strong>ikkita qarash</strong> beriladi va siz "
            "<u>ikkovini ham</u> yoritishingiz, <mark style=\"background:#dbeafe;\">"
            "hamda o'z fikringizni</mark> bildirishingiz kerak. Ikki eng katta xato: "
            "(1) faqat bitta qarashni yoritish; (2) o'z fikrini umuman aytmaslik. "
            "Ikkovi ham Task Response'ni jiddiy pasaytiradi.</p>"
        )},
        {"rich_text": (
            "<h3>Tuzilma — 4 paragraf</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Introduction.</strong> Savolni "
            "paraphrase qiling + \"ikki qarashni ko'rib chiqaman\" + <u>o'z "
            "pozitsiyangiz</u> (tezis). Fikringiz kirishdayoq aniq bo'lsin.</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Body 1 — birinchi qarash.</strong> "
            "Uni <u>adolatli</u> tushuntiring: nega ba'zilar shunday deb o'ylaydi? "
            "Dalil + misol. Bu qarashga siz qo'shilmasangiz ham, uni kuchli "
            "ko'rsating.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Body 2 — ikkinchi qarash.</strong> "
            "Xuddi shunday adolatli va batafsil. <u>Teng vazn</u> bering — bir tomonni "
            "ataylab zaif ko'rsatmang (strawman qilmang).</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Conclusion.</strong> Ikki qarashni "
            "qisqacha eslatib, <u>o'z fikringizni</u> qayta va aniq ayting: qaysi tomon "
            "sizningcha kuchliroq.</p></div>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat — o'z fikringiz QAYERDA?</strong> \"Discuss both views "
            "<u>and give your own opinion</u>\" — bu ikkinchi qism majburiy. Fikringiz "
            "kirish (tezis) va xulosada aniq ko'rinishi shart. Faqat ikki tomonni sanab, "
            "fikrsiz qolish — eng ko'p yo'qotiladigan ball.</div>"
        )},
        {"rich_text": (
            "<h3>Ikki tomonni ulash tili</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Birinchi qarash:</strong> On the one hand, ... / Those who support X argue that ... / Supporters of X point out that ...</p>"
            "<p style=\"margin:0 0 6px;\"><strong>Ikkinchi qarash:</strong> On the other hand, ... / Others contend that ... / However, an opposing view holds that ...</p>"
            "<p style=\"margin:0;\"><strong>O'z fikringiz:</strong> In my view, ... / Personally, I believe ... / While both sides have merit, I am inclined to think ...</p>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Model esse — qism-qism oching</h3>"
            "<p><strong>Savol:</strong> <em>\"Some people believe that a university degree "
            "is the best route to a successful career, while others think practical work "
            "experience is more valuable. Discuss both views and give your own "
            "opinion.\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi paragrafni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"There is an "
            "ongoing debate about whether a university degree or hands-on work experience "
            "offers the better path to career success. This essay will consider both "
            "views before arguing that, although a degree is valuable, practical "
            "experience is often more decisive.\"</em><br>"
            "<span style=\"color:#475569;\">Paraphrase + \"both views\" + aniq tezis "
            "(experience often more decisive).</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1 (degree view):</strong> <em>\"On "
            "the one hand, supporters of higher education argue that a degree provides "
            "deep theoretical knowledge and formal qualifications. Many professions, such "
            "as medicine and law, are closed to those without a relevant degree. "
            "University also develops critical thinking that employers value.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2 (experience view):</strong> <em>\"On "
            "the other hand, others contend that hands-on experience teaches skills no "
            "lecture can. By working from an early age, individuals build professional "
            "networks and learn how real workplaces operate. A young entrepreneur, for "
            "example, may gain more from running a small business than from years of "
            "study.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Conclusion:</strong> <em>\"In conclusion, "
            "while both a degree and work experience have clear merits, I believe the "
            "most successful people combine the two, with real-world skills frequently "
            "making the greater difference.\"</em><br>"
            "<span style=\"color:#475569;\">Ikki qarash eslatildi + o'z fikri aniq "
            "(experience greater difference).</span></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> \"Discuss both views and give your own "
                "opinion\" savolida ikki qarashdan tashqari yana nima SHART?</p>"
            ),
            "choices": [
                {"text": "Hech narsa — ikki qarashni yoritish yetarli", "is_correct": False},
                {"text": "O'z fikringizni (opinion) aniq bildirish — kirish va xulosada", "is_correct": True},
                {"text": "Statistik ma'lumot keltirish", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: o'z fikringiz.</mark> "
                "Savolning ikkinchi qismi (\"give your own opinion\") majburiy. Fikrsiz "
                "esse — savolning yarmiga javob bermaydi va Task Response pasayadi. "
                "Pozitsiyangiz kirishdagi tezisda va xulosada aniq bo'lsin.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Talaba birinchi qarashni 5 gapda kuchli "
                "yoritib, ikkinchisini faqat 1 zaif gapda \"ataylab kuchsiz\" ko'rsatadi. "
                "Muammo nima?</p>"
            ),
            "choices": [
                {"text": "Hech narsa — asosiysi ikkovi ham bor", "is_correct": False},
                {"text": "Ikki qarash TENG vazn olmagan — bir tomon strawman qilingan, bu Task Response'ni pasaytiradi", "is_correct": True},
                {"text": "Faqat Grammatika pasayadi", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: teng vazn "
                "yo'q.</mark> \"Discuss both views\" ikki qarashni ham <u>adolatli va "
                "batafsil</u> yoritishni talab qiladi. Bir tomonni ataylab zaif ko'rsatish "
                "(strawman) — savolni to'liq bajarmaslik. Ikkovini ham jiddiy dalil bilan "
                "bering, keyin o'z fikringizni ayting.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Qaysi ibora ikkinchi qarashni tabiiy "
                "boshlaydi?</p>"
            ),
            "choices": [
                {"text": "\"On the other hand, others contend that ...\"", "is_correct": True},
                {"text": "\"Because of this, ...\"", "is_correct": False},
                {"text": "\"For example, ...\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: \"On the other "
                "hand...\".</mark> Bu ibora birinchi qarashdan ikkinchisiga silliq o'tadi "
                "(Coherence & Cohesion). \"Because of this\" — sabab-natija (bu yerda mos "
                "emas), \"For example\" — misol (yangi qarash boshlamaydi).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Discussion phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">On the one hand, ... On the other hand, ...</div><div class=\"pp-card-back\">Bir tomondan ... Boshqa tomondan ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Those who support X argue that ...</div><div class=\"pp-card-back\">X tarafdorlari ... deb ta'kidlaydi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">Others contend that ...</div><div class=\"pp-card-back\">Boshqalar ... deb hisoblaydi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">both views have merit</div><div class=\"pp-card-back\">ikkala qarash ham asosli</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">I am inclined to think ...</div><div class=\"pp-card-back\">Men ... deb o'ylashga moyilman</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">decisive</div><div class=\"pp-card-back\">hal qiluvchi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">an ongoing debate</div><div class=\"pp-card-back\">davom etayotgan bahs</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to build a network</div><div class=\"pp-card-back\">aloqalar tarmog'ini qurmoq</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>\"Discuss both views\" = ikki qarash + O'Z fikring (ikkinchisi majburiy).</li>"
            "<li>Har qarashni adolatli, teng vazn bilan yoriting — strawman qilmang.</li>"
            "<li>Ulash tili: On the one hand / On the other hand; supporters argue / others contend.</li>"
            "<li>Fikringiz kirish (tezis) va xulosada aniq bo'lsin.</li>"
            "</ul>"
        )},
    ],
},

# ─────────────────────────────────────────────────────────────────────────
# Lesson 13 (order 51 — problem-solution)
# ─────────────────────────────────────────────────────────────────────────
{
    "skill": "writing",
    "topic": TOPIC_T2_DISCUSSION,
    "title": "IELTS Writing 13: Problem-Solution Essays — Cause and Remedy Structure",
    "summary": "\"Causes and solutions\" insholari: sabab/muammo paragrafi + mos yechim paragrafi; yechimlar aytilgan muammolarga aniq javob berishi kerak.",
    "order": 51,
    "blocks": [
        {"rich_text": (
            "<h2>Muammo va yechim insholari</h2>"
            "<p>Bu savol turi ko'pincha shunday: <em>\"What are the causes of this "
            "problem and what solutions can you suggest?\"</em> yoki <em>\"What problems "
            "does this cause and how can they be solved?\"</em>. Tuzilma tabiiy: bitta "
            "paragraf <strong>sabab/muammolar</strong>, bitta paragraf <strong>mos "
            "yechimlar</strong>.</p>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Eng muhim qoida — YECHIM MUAMMOGA MOS bo'lsin:</strong> agar "
            "sabab \"ko'p mashina\" bo'lsa, yechim aynan shunga javob berishi kerak "
            "(masalan \"jamoat transportini rivojlantirish\"). Bog'liq bo'lmagan yechim "
            "(\"maktablarni ko'paytirish\") — Task Response'ni buzadi.</div>"
        )},
        {"rich_text": (
            "<h3>Tuzilma — 4 paragraf</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1. Introduction.</strong> Savolni "
            "paraphrase qiling + inshoning rejasini ayting: \"sabablarni ko'rib chiqib, "
            "keyin yechim taklif qilaman\".</p></div>"
            "<div class=\"pp-step\"><p><strong>2. Body 1 — sabab/muammolar.</strong> "
            "1–2 asosiy sababni tushuntiring (nega bu yuz beryapti?). Har sababni dalil "
            "bilan quvvatlang.</p></div>"
            "<div class=\"pp-step\"><p><strong>3. Body 2 — yechimlar.</strong> Har "
            "muammoga <u>mos</u> yechim taklif qiling. Yechimlarni aniq va amaliy qiling "
            "(kim? qanday?).</p></div>"
            "<div class=\"pp-step\"><p><strong>4. Conclusion.</strong> Asosiy sabab va "
            "yechimlarni qisqacha jamlang; ijobiy yakun (\"progress can be made\").</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Sabab va yechim tili</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 6px;\"><strong>Sabablar:</strong> The main cause is ... / This stems largely from ... / is largely due to ... / A major factor is ...</p>"
            "<p style=\"margin:0;\"><strong>Yechimlar:</strong> One way to tackle this is ... / Governments could ... / A possible remedy would be ... / This could be addressed by ...</p>"
            "</div>"
            "<div style=\"background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📝 Namuna — yechim uchun shart gap (conditional):</strong><br>"
            "<em>\"<u>If</u> governments invested in reliable public transport, fewer "
            "people <u>would</u> rely on private cars.\"</em><br>"
            "<span style=\"color:#475569;\">Shart gaplar (if + past, would + inf) "
            "yechim taklif qilishning kuchli va grammatik jihatdan boy usuli — "
            "Grammatical Range'ni ko'taradi.</span></div>"
        )},
        {"rich_text": (
            "<h3>Model esse — qism-qism oching</h3>"
            "<p><strong>Savol:</strong> <em>\"Traffic congestion is a growing problem in "
            "many cities. What are the main causes, and what measures could be taken to "
            "solve it?\"</em></p>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi paragrafni ochish ▸\">"
            "<div class=\"pp-step\"><p><strong>Introduction:</strong> <em>\"Traffic "
            "congestion has become an increasingly serious problem in cities worldwide. "
            "This essay will examine the main causes of this issue before suggesting "
            "several measures that could help to reduce it.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 1 (causes):</strong> <em>\"The "
            "primary cause of congestion is the sheer number of private cars on the "
            "roads. As incomes rise, more families can afford vehicles, and many prefer "
            "the comfort of driving to using public transport. This is worsened by "
            "outdated road infrastructure in older cities, which was never designed for "
            "such volumes of traffic.\"</em></p></div>"
            "<div class=\"pp-step\"><p><strong>Body 2 (solutions — matched):</strong> "
            "<em>\"Several measures could address this. Firstly, governments could invest "
            "in reliable public transport, encouraging people to leave their cars at "
            "home. In addition, congestion charges in city centres, as introduced in "
            "London, would discourage unnecessary journeys. If cities also expanded "
            "cycling lanes, many short trips could be made without a car at all.\"</em><br>"
            "<span style=\"color:#475569;\">Har yechim body 1'dagi sababga mos: ko'p "
            "mashina → transport + charge + velosiped.</span></p></div>"
            "<div class=\"pp-step\"><p><strong>Conclusion:</strong> <em>\"In conclusion, "
            "traffic congestion stems largely from rising car ownership and outdated "
            "infrastructure, but through better public transport, congestion charges and "
            "cycling provision, cities can make real progress in tackling it.\"</em></p></div>"
            "</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Amaliyot 1.</strong> Problem-solution inshosida tana "
                "paragraflari odatda qanday bo'linadi?</p>"
            ),
            "choices": [
                {"text": "Bir paragraf rozilik, bir paragraf qarshilik", "is_correct": False},
                {"text": "Bir paragraf sabab/muammolar, bir paragraf yechimlar", "is_correct": True},
                {"text": "Ikkovi ham faqat misollar", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: sabablar + "
                "yechimlar.</mark> Problem-solution tabiiy tuzilmasi: Body 1 = sabab/"
                "muammolar (nega yuz beryapti), Body 2 = mos yechimlar (qanday hal "
                "qilish). Rozilik/qarshilik — bu agree/disagree yoki discussion "
                "insholarining tuzilmasi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 2.</strong> Body 1'da sabab \"juda ko'p shaxsiy "
                "mashina\" deb aytilgan. Qaysi yechim eng MOS?</p>"
            ),
            "choices": [
                {"text": "\"Governments should build more schools.\"", "is_correct": False},
                {"text": "\"Governments could invest in public transport so fewer people drive.\"", "is_correct": True},
                {"text": "\"People should eat healthier food.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: jamoat "
                "transporti.</mark> Yechim aytilgan sababga (ko'p mashina) to'g'ridan-"
                "to'g'ri javob berishi kerak — transportni yaxshilash odamlarni "
                "mashinadan voz kechishga undaydi. \"Maktablar\" va \"sog'lom ovqat\" — "
                "muammoga aloqasiz (Task Response'ni buzadi).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Amaliyot 3.</strong> Yechim taklif qilishning grammatik "
                "jihatdan kuchli usuli qaysi?</p>"
            ),
            "choices": [
                {"text": "\"If cities expanded cycling lanes, fewer cars would be needed.\" (shart gap)", "is_correct": True},
                {"text": "\"Cars are bad. Bikes are good.\"", "is_correct": False},
                {"text": "\"I think maybe bikes.\"", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: shart gap "
                "(conditional).</mark> \"If + past, ... would + inf\" — yechim va uning "
                "natijasini bog'laydigan aniq, grammatik jihatdan boy tuzilma "
                "(Grammatical Range'ni ko'taradi). Qolgan ikkisi — juda oddiy va noaniq "
                "(band past).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Kalit iboralar — Cause & solution phrases</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">The main cause is ...</div><div class=\"pp-card-back\">Asosiy sabab ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">This stems largely from ...</div><div class=\"pp-card-back\">Bu asosan ...dan kelib chiqadi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">One way to tackle this is ...</div><div class=\"pp-card-back\">Buni hal qilishning bir yo'li ...</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">A possible remedy would be ...</div><div class=\"pp-card-back\">Mumkin bo'lgan yechim ... bo'lardi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to address / to tackle a problem</div><div class=\"pp-card-back\">muammoni hal qilmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">to discourage / to encourage</div><div class=\"pp-card-back\">qaytarmoq / rag'batlantirmoq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">infrastructure</div><div class=\"pp-card-back\">infratuzilma</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a congestion charge</div><div class=\"pp-card-back\">tirbandlik uchun to'lov</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Tuzilma: Body 1 = sabab/muammolar, Body 2 = mos yechimlar.</li>"
            "<li>ENG muhim: har yechim aytilgan muammoga aniq javob bersin (mos kelsin).</li>"
            "<li>Sabab tili: stems from, is due to; yechim tili: could, one way to tackle.</li>"
            "<li>Shart gaplar (If ..., ... would ...) yechimni kuchli va grammatik boy qiladi.</li>"
            "</ul>"
        )},
    ],
},

]
