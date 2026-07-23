"""
IELTS Reading lesson 27 (order 70) — the "Diagramma yorlig'ini to'ldirish (Diagram
Label Completion)" topic (single lesson) — seventh batch, see toc_ielts_reading.txt.
"""

TRACK = {
    "name":    "IELTS",
    "summary": "IELTS imtihoniga bosqichma-bosqich tayyorgarlik — Reading, Listening, "
               "Writing va Speaking bo'yicha strategiya va amaliyot.",
    "icon":    "bi-globe2",
    "color":   "#059669",
    "order":   2,
}

TOPIC_DIAGRAM = {
    "title":   "Diagramma yorlig'ini to'ldirish (Diagram Label Completion)",
    "summary": "Jarayon yoki mexanizm diagrammasidagi bo'sh yorliqlarni matndagi so'zlar "
               "va fazoviy tilni tushunib to'ldirish.",
    "icon":    "bi-diagram-2",
    "order":   8,
}

# ── shared SVG: rainwater butt (used in the practice questions) ──────────────
DIAGRAM_SVG = (
    "<div style=\"overflow-x:auto;\">"
    "<svg viewBox='0 0 440 390' style='width:100%;max-width:420px;height:auto;display:block;margin:8px auto;font-family:sans-serif;'>"
    # roof
    "<polygon points='24,120 210,60 210,120' fill='#cbd5e1' stroke='#475569' stroke-width='2'/>"
    "<text x='70' y='100' font-size='12' fill='#334155'>roof</text>"
    # gutter
    "<rect x='150' y='118' width='66' height='11' fill='#94a3b8' stroke='#475569' stroke-width='1.5'/>"
    # downpipe
    "<rect x='190' y='129' width='16' height='66' fill='#e2e8f0' stroke='#475569' stroke-width='1.5'/>"
    # filter (mesh)
    "<rect x='176' y='195' width='44' height='16' fill='#fde68a' stroke='#475569' stroke-width='1.5'/>"
    "<line x1='183' y1='195' x2='183' y2='211' stroke='#a16207' stroke-width='1'/>"
    "<line x1='191' y1='195' x2='191' y2='211' stroke='#a16207' stroke-width='1'/>"
    "<line x1='199' y1='195' x2='199' y2='211' stroke='#a16207' stroke-width='1'/>"
    "<line x1='207' y1='195' x2='207' y2='211' stroke='#a16207' stroke-width='1'/>"
    # barrel + water
    "<rect x='150' y='211' width='112' height='150' rx='8' fill='#dbeafe' stroke='#475569' stroke-width='2'/>"
    "<rect x='153' y='250' width='106' height='108' rx='6' fill='#93c5fd' stroke='none'/>"
    "<text x='188' y='310' font-size='12' fill='#1e3a5f'>barrel</text>"
    # tap
    "<rect x='134' y='330' width='18' height='9' fill='#475569'/>"
    "<rect x='138' y='339' width='6' height='9' fill='#475569'/>"
    # overflow pipe
    "<rect x='262' y='224' width='30' height='11' fill='#e2e8f0' stroke='#475569' stroke-width='1.5'/>"
    # numbered blank markers (circles + leader lines)
    "<line x1='183' y1='112' x2='183' y2='96' stroke='#dc2626' stroke-width='1.2'/>"
    "<circle cx='183' cy='88' r='11' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='183' y='92' font-size='13' font-weight='bold' fill='#dc2626' text-anchor='middle'>1</text>"
    "<line x1='214' y1='160' x2='250' y2='160' stroke='#dc2626' stroke-width='1.2'/>"
    "<circle cx='262' cy='160' r='11' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='262' y='164' font-size='13' font-weight='bold' fill='#dc2626' text-anchor='middle'>2</text>"
    "<line x1='176' y1='203' x2='118' y2='203' stroke='#dc2626' stroke-width='1.2'/>"
    "<circle cx='106' cy='203' r='11' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='106' y='207' font-size='13' font-weight='bold' fill='#dc2626' text-anchor='middle'>3</text>"
    "<line x1='134' y1='334' x2='104' y2='334' stroke='#dc2626' stroke-width='1.2'/>"
    "<circle cx='92' cy='334' r='11' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='92' y='338' font-size='13' font-weight='bold' fill='#dc2626' text-anchor='middle'>4</text>"
    "<line x1='292' y1='229' x2='320' y2='229' stroke='#dc2626' stroke-width='1.2'/>"
    "<circle cx='332' cy='229' r='11' fill='#fff' stroke='#dc2626' stroke-width='2'/>"
    "<text x='332' y='233' font-size='13' font-weight='bold' fill='#dc2626' text-anchor='middle'>5</text>"
    "</svg>"
    "</div>"
)

LESSONS = [

{
    "skill": "reading",
    "topic": TOPIC_DIAGRAM,
    "title": "IELTS Reading 27: Diagram Label Completion — Reading Process and Mechanism Diagrams",
    "summary": "Diagramma yorlig'ini matndan so'z bilan to'ldirish: diagrammani o'qish, fazoviy tilni (above/beneath/into) tushunish va yorliqlarni langar qilish.",
    "order": 70,
    "blocks": [
        {"rich_text": (
            "<h2>Diagram Label Completion nima?</h2>"
            "<p>Sizga bir <strong>diagramma</strong> beriladi — mexanizm (mashina, "
            "asbob), jarayon yoki tabiiy tuzilma rasmi — va uning ba'zi qismlari "
            "raqamlangan <u>bo'sh yorliqlar</u> bilan qoldirilgan. Vazifa: har bo'sh "
            "yorliqni matndagi <mark style=\"background:#dbeafe;\">so'z(lar)</mark> bilan "
            "to'ldirish.</p>"
            "<div style=\"background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>💡 Yaxshi xabar:</strong> bu — Completion turining bir ko'rinishi, "
            "demak barcha qoidalar tanish: matndan AYNAN so'z (paraphrase emas), so'z "
            "chegarasi, to'g'ri imlo. Yangi narsa faqat bitta: matnni <u>rasm bilan</u> "
            "bog'lash.</div>"
        )},
        {"rich_text": (
            "<h3>Ikki maxsus xususiyat</h3>"
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0 0 8px;\"><strong>1. Javoblar deyarli har doim OT.</strong> "
            "Diagramma qismlarga <u>nom</u> beradi — qismlar esa otlar (gutter, valve, "
            "chamber). Fe'l yoki sifat kamdan-kam kerak bo'ladi.</p>"
            "<p style=\"margin:0;\"><strong>2. Javoblar matn tartibida BO'LMASLIGI "
            "mumkin.</strong> Boshqa completionlardan farqli o'laroq, siz diagramma "
            "bo'ylab sakraysiz (yuqori → past → yon), matn esa boshqa tartibda tasvirlashi "
            "mumkin. Shuning uchun langar (allaqachon yozilgan yorliqlar) muhim.</p>"
            "</div>"
            "<div style=\"background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>📌 Eslatma:</strong> diagrammada odatda 1–2 qism <u>allaqachon "
            "nomlangan</u> bo'ladi. Ular sizning langaringiz — matndan o'sha nomni topib, "
            "atrofidagi jumlalarni o'qisangiz, qo'shni (bo'sh) qismlarning nomi shu "
            "yerdan chiqadi.</div>"
        )},
        {"rich_text": (
            "<h3>Kalit ko'nikma: fazoviy tilni tushunish</h3>"
            "<p>Matn diagrammani <u>so'z bilan</u> tasvirlaydi — siz esa uni fazoga "
            "(rasmga) qaytarasiz. Shuning uchun <strong>joy va yo'nalish so'zlari</strong> "
            "kalit rol o'ynaydi. Ularni yaxshi biling:</p>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">above / on top of</div><div class=\"pp-card-back\">ustida, tepasida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">beneath / below</div><div class=\"pp-card-back\">ostida, pastida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">at the base of</div><div class=\"pp-card-back\">tubida, asosida</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">along the edge</div><div class=\"pp-card-back\">chekka bo'ylab</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">flows into / enters</div><div class=\"pp-card-back\">~ga oqib kiradi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">is attached to</div><div class=\"pp-card-back\">~ga biriktirilgan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">surrounds</div><div class=\"pp-card-back\">o'rab turadi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">passes through</div><div class=\"pp-card-back\">~dan o'tadi</div></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Usul — bosqichma-bosqich</h3>"
            "<div class=\"pp-steps\" data-pp-steps data-pp-more=\"Keyingi qadam ▸\">"
            "<div class=\"pp-step\"><p><strong>1-qadam.</strong> Avval diagrammani "
            "<u>o'qing</u> (yozishdan oldin!): bu nima? Qanday ishlaydi? Qaysi qismlar "
            "allaqachon nomlangan?</p></div>"
            "<div class=\"pp-step\"><p><strong>2-qadam.</strong> Nomlangan qism(lar)ni "
            "langar qilib, matndan o'sha so'zni toping — bu diagrammaning matndagi "
            "tavsifini boshlaydigan nuqta.</p></div>"
            "<div class=\"pp-step\"><p><strong>3-qadam.</strong> Bo'sh yorliqning "
            "diagrammada <u>qayerda</u> turishiga qarang (nimaning ustida/ostida/yonida) "
            "va matndan o'sha fazoviy tavsifni qidiring.</p></div>"
            "<div class=\"pp-step\"><p><strong>4-qadam.</strong> Topilgan otni AYNAN "
            "ko'chiring (imlo!), so'z chegarasini tekshiring, keyin keyingi yorliqqa "
            "o'ting.</p></div>"
            "</div>"
        )},
        {"rich_text": (
            "<h3>Amaliyot uchun diagramma — yomg'ir suvini yig'ish tizimi</h3>"
            "<p>Quyidagi diagrammani o'qing (1–5 bo'sh yorliqlar), keyin matnni o'qib, "
            "har yorliqni to'ldiring. So'z chegarasi: <strong>ONE WORD</strong>.</p>"
            + DIAGRAM_SVG +
            "<div style=\"background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;\">"
            "<p style=\"margin:0;\"><strong>Matn:</strong> \"Collecting rainwater at home "
            "needs only a few simple parts. Rain that falls on the sloping roof runs down "
            "into a <em>gutter</em> fixed along its lower edge. From there the water is "
            "carried downwards through a vertical <em>downpipe</em>. Before entering the "
            "storage barrel, it passes through a fine mesh <em>filter</em>, which traps "
            "leaves and other debris. The water then collects in the barrel below. A "
            "<em>tap</em> fitted near the base of the barrel lets the gardener draw water "
            "off when needed, while a short <em>overflow</em> pipe near the top allows "
            "excess water to escape during heavy rain.\"</p>"
            "</div>"
            "<div style=\"background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;\">"
            "<strong>⚠️ Diqqat:</strong> diagrammada suv yuqoridan (tom) pastga (barrel) "
            "harakatlanadi — raqamlarni shu oqim bo'yicha kuzating: 1 (tom chekkasi) → "
            "2 (vertikal quvur) → 3 (to'r) → 4/5 (barrel qismlari).</div>"
        )},
        {
            "rich_text": (
                "<p><strong>Savol 1.</strong> Diagrammada <strong>(1)</strong> — tom "
                "chekkasi bo'ylab o'rnatilgan qism. Qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "gutter", "is_correct": True},
                {"text": "roof", "is_correct": False},
                {"text": "downpipe", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: gutter.</mark> "
                "Fazoviy signal: (1) tomning <u>pastki chekkasi bo'ylab</u>. Matn: "
                "\"runs down into a <u>gutter</u> fixed <u>along its lower edge</u>\" — "
                "aynan mos. \"roof\" — allaqachon diagrammada nomlangan (langar, bo'sh "
                "yorliq emas), \"downpipe\" — keyingi qism (vertikal).</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 2.</strong> <strong>(2)</strong> — gutterdan pastga "
                "ketadigan vertikal quvur. Qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "filter", "is_correct": False},
                {"text": "downpipe", "is_correct": True},
                {"text": "overflow", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: downpipe.</mark> "
                "Fazoviy signal: suv gutterdan <u>pastga, vertikal</u> harakatlanadi. "
                "Matn: \"carried <u>downwards through a vertical downpipe</u>\" — aynan. "
                "\"filter\" — quvurdan keyingi qism (to'r), \"overflow\" — barrelning "
                "tepasidagi qism. Diagrammadagi joy matndagi fazoviy tavsifga mos "
                "keladi.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 3.</strong> <strong>(3)</strong> — barrelga kirishdan "
                "oldin suv o'tadigan to'r qism. Qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "filter", "is_correct": True},
                {"text": "gutter", "is_correct": False},
                {"text": "debris", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: filter.</mark> "
                "Fazoviy signal: barrelga <u>kirishdan oldin</u> o'tadigan qism. Matn: "
                "\"Before entering the storage barrel, it <u>passes through a fine mesh "
                "filter</u>\" — aynan. \"debris\" — so'z-tuzoq: matnda bor, lekin u "
                "to'rda <u>ushlanadigan</u> narsa (barg, chiqindi), qismning nomi emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 4.</strong> <strong>(4)</strong> — barrelning tubiga "
                "yaqin o'rnatilgan, suvni olish uchun qism. Qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "overflow", "is_correct": False},
                {"text": "tap", "is_correct": True},
                {"text": "base", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: tap.</mark> "
                "Fazoviy signal: barrelning <u>tubiga yaqin</u> (near the base). Matn: "
                "\"A <u>tap</u> fitted <u>near the base</u> of the barrel lets the "
                "gardener draw water off\" — aynan. \"base\" — bu joyning nomi (qismning "
                "emas) — fazoviy tuzoq; \"overflow\" — tepadagi qism, tubidagi emas.</p>"
            ),
        },
        {
            "rich_text": (
                "<p><strong>Savol 5.</strong> <strong>(5)</strong> — barrelning "
                "tepasiga yaqin, ortiqcha suvni chiqaradigan qisqa quvur. Qaysi so'z?</p>"
            ),
            "choices": [
                {"text": "overflow", "is_correct": True},
                {"text": "downpipe", "is_correct": False},
                {"text": "tap", "is_correct": False},
            ],
            "explanation": (
                "<p><mark style=\"background:#dcfce7;\">To'g'ri javob: overflow.</mark> "
                "Fazoviy signal: barrelning <u>tepasiga yaqin</u> + <u>ortiqcha suvni "
                "chiqaradi</u>. Matn: \"a short <u>overflow</u> pipe <u>near the top</u> "
                "allows excess water to escape\" — aynan. \"downpipe\" — tepadagi kirish "
                "quvuri (langar bilan adashtirmang), \"tap\" — tubidagi qism. So'z "
                "chegarasi ONE WORD: \"overflow\" (\"overflow pipe\" 2 so'z bo'lardi — "
                "faqat \"overflow\" yozing).</p>"
            ),
        },
        {"rich_text": (
            "<h3>Tez-tez uchraydigan xatolar</h3>"
            "<ul>"
            "<li><strong>Langar yorliqni bo'sh deb o'ylash.</strong> Allaqachon "
            "nomlangan qismni (bu misolda \"roof\", \"barrel\") qayta yozmang — ular "
            "yordamchi, savol emas.</li>"
            "<li><strong>Joyni qism deb yozish.</strong> \"base\", \"top\", \"edge\" — "
            "bular joy so'zlari; savol qismning <u>nomini</u> so'raydi.</li>"
            "<li><strong>So'z chegarasini unutish.</strong> \"overflow pipe\" 2 so'z; "
            "ONE WORD bo'lsa faqat \"overflow\".</li>"
            "<li><strong>Imlo.</strong> Diagramma javoblari ko'pincha texnik otlar — "
            "matndan harfma-harf ko'chiring.</li>"
            "</ul>"
            "<h3>Kalit so'zlar — Key vocabulary</h3>"
            "<div class=\"pp-flashcards\" data-pp-flashcards>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a gutter</div><div class=\"pp-card-back\">tom novi/ariqchasi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a downpipe</div><div class=\"pp-card-back\">tushirish (vertikal) quvuri</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a filter</div><div class=\"pp-card-back\">filtr, to'siq to'r</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a tap / valve</div><div class=\"pp-card-back\">jo'mrak / klapan</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">overflow</div><div class=\"pp-card-back\">ortiqcha suv chiqishi/toshishi</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">debris</div><div class=\"pp-card-back\">chiqindi, qoldiq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a chamber</div><div class=\"pp-card-back\">kamera, bo'shliq</div></div>"
            "<div class=\"pp-card\"><div class=\"pp-card-front\">a mesh</div><div class=\"pp-card-back\">to'r, panjara</div></div>"
            "</div>"
            "<h3>Xulosa</h3>"
            "<ul>"
            "<li>Diagram Label = Completion turi: matndan AYNAN so'z, so'z chegarasi, imlo muhim.</li>"
            "<li>Javoblar deyarli har doim OT (qism nomi); matn tartibida bo'lmasligi mumkin.</li>"
            "<li>Avval diagrammani o'qing; nomlangan qismlarni langar qiling.</li>"
            "<li>Fazoviy tilni tushuning: above/beneath/at the base/passes through — joyni matndan topadi.</li>"
            "<li>Joy so'zi (base, top) qism nomi emas; langar yorliqni qayta yozmang.</li>"
            "</ul>"
        )},
    ],
},

]
