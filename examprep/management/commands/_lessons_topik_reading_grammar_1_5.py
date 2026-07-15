# TOPIK II Reading — 1–2-savollar: Grammatik bo'sh joy (문법), lessons 1–5 (orders 40–44).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_grammar_1_5.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "1–2-savollar: Grammatik bo'sh joy (문법)",
    "summary": "( )ga mos grammatik shaklni tanlash — ma'no oilalari bo'yicha tizimli o'rganamiz.",
    "icon":    "bi-pencil",
    "order":   2,
}

LESSONS = [
    # ── Lesson 1 (order 40) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문법 1: 1–2-savollar bilan tanishuv — to'rt ma'no oilasi",
        "summary": "Imtihonning birinchi ikki savoli qanday tuzilgan va grammatikani 'oila' usulida qanday yechish kerak.",
        "order":   40,
        "blocks": [
            {"rich_text": """
<h2>✏️ 1–2-savollar: birinchi ikki ball</h2>
<p>TOPIK II o'qish bo'limi aynan shu savollar bilan boshlanadi. Shakli doim bir xil:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>(        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>( )ga kiradigan eng mos so'zni tanlang.</em></p>
</div>
<p>Bitta gap beriladi, fe'lning bir qismi bo'sh qoldiriladi va to'rtta variant —
<strong>bitta fe'lning to'rt xil grammatik shakli</strong> bo'ladi:</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;font-size:1.08em;">형은 음악을 (        ) 공부를 한다.</p>
  <p style="margin:0;">① 듣거나 &nbsp; ② 듣지만 &nbsp; ③ <mark style="background:#dcfce7;">들으면서</mark> &nbsp; ④ 듣더라도</p>
</div>
<p>Demak bu savol <strong>so'zni emas, qo'shimchaning ma'nosini</strong> so'raydi:
"tinglab turib o'qiydi" — bir vaqtdalik → <strong>-(으)면서</strong>.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> 1-savol osonroq (3-daraja), 2-savol biroz qiyinroq (4-daraja)
  grammatikadan keladi. Ikkalasiga jami <strong>1 daqiqa</strong> yetadi — bu ballarni tez
  olib, uzun matnlarga vaqt saqlang.
</div>
"""},
            {"rich_text": """
<h3>Sir: yuzlab qo'shimcha emas — 4 ta oila</h3>
<p>Grammatik qo'shimchalarni bittalab yodlash — adashish yo'li. Buning o'rniga har
qo'shimchani <strong>ma'no oilasiga</strong> qarab taniysiz. TOPIK 1–2 savollarida
deyarli har doim shu to'rt oiladan biri so'raladi:</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>1-oila — Sabab va natija:</strong> -아/어서, -(으)니까, -기 때문에, -는 바람에, -느라고, 덕분에
  <br><em>"Nega?" degan savolga javob beradi.</em>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>2-oila — Vaqt va ketma-ketlik:</strong> -자마자, -다가, -(으)면서, -고 나서, -기 전에, -(으)ㄴ 지
  <br><em>"Qachon? Qaysi tartibda?" degan savolga javob beradi.</em>
</div>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>3-oila — Shart, maqsad va taxmin:</strong> -(으)면, -(으)려면, -(으)려고, -도록, -(으)ㄹ까 봐, -나 보다
  <br><em>"Qanday shartda? Nima uchun? Ehtimol?" savollariga javob beradi.</em>
</div>
<div style="background:#fef2f2;border-left:4px solid #ef4444;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>4-oila — Qarama-qarshilik:</strong> -지만, -는데도, -아/어도, -더라도, -는 대신에
  <br><em>"Lekin? Shunga qaramay?" savollariga javob beradi.</em>
</div>
<h3>Yechish tartibi (30 soniya)</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam.</strong> Gapni to'liq o'qing va ikki bo'lak orasidagi <strong>munosabatni</strong>
    aniqlang: sababmi, vaqtmi, shartmi, qarshilikmi? (Ko'pincha gapning ikkinchi yarmi aytib turadi:
    "지각했다" ko'rsangiz — oldida sabab bo'lishi kerak.)</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam.</strong> Variantlardan <strong>o'sha oilaga tegishlisini</strong> toping —
    odatda to'rt variant to'rt xil oiladan bo'ladi, shuning uchun oila topilsa javob topiladi.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam.</strong> Bir oiladan ikkita variant bo'lsa, <strong>nozik farq</strong>ni
    tekshiring (masalan -아서 umumiy sabab, -는 바람에 esa kutilmagan salbiy natija).
    Keyingi darslarda aynan shu farqlarni o'rganamiz.</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>너무 피곤해서 소파에 (        ) 잠이 들었다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Juda charchaganim uchun divanga (        ) uxlab qolibman.</em></p>
</div>
""",
             "choices": [
                 {"text": "앉자마자 (o'tirishim bilanoq)", "is_correct": True},
                 {"text": "앉으려면 (o'tirmoqchi bo'lsam)", "is_correct": False},
                 {"text": "앉거나 (o'tirsam yoki)", "is_correct": False},
                 {"text": "앉는데도 (o'tirsam ham)", "is_correct": False},
             ],
             "explanation": """
<p>Munosabatni aniqlaymiz: "charchagan → divanga o'tirdi → darhol uxlab qoldi" — bu
<strong>vaqt oilasi</strong> (ketma-ket, tez). Vaqt oilasidan bitta variant bor:
<mark style="background:#dcfce7;">-자마자</mark> ("~ bilanoq") ✅. ② shart oilasi,
③ tanlash, ④ qarshilik — munosabatga mos emas. Ko'rdingizmi: oila topildi — javob topildi!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>내일 시험이 (        ) 오늘은 일찍 자야 한다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Ertaga imtihonim (        ) bugun erta yotishim kerak.</em></p>
</div>
""",
             "choices": [
                 {"text": "있지만 (bor, lekin)", "is_correct": False},
                 {"text": "있으니까 (borligi uchun)", "is_correct": True},
                 {"text": "있다가 (bor turib, keyin)", "is_correct": False},
                 {"text": "있더라도 (bo'lsa ham)", "is_correct": False},
             ],
             "explanation": """
<p>"Imtihon bor → erta yotish kerak" — <strong>sabab oilasi</strong>. Sabab oilasidan
<mark style="background:#dcfce7;">-(으)니까</mark> ✅. Nozik nuqta: gapning ikkinchi yarmi
<strong>-아야 한다</strong> (kerak) — tavsiya/majburiyat. Bunday gaplarda sabab uchun odatda
-(으)니까 ishlatiladi (-아서 emas). ①④ qarshilik oilasi — ma'noni buzadi ("imtihon bor,
lekin erta yotish kerak"?), ③ vaqt oilasi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">문법</div><div class="pp-card-back">grammatika</div></div>
  <div class="pp-card"><div class="pp-card-front">알맞다</div><div class="pp-card-back">mos kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)면서</div><div class="pp-card-back">bir vaqtda (~b turib)</div></div>
  <div class="pp-card"><div class="pp-card-front">-자마자</div><div class="pp-card-back">~ bilanoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)니까</div><div class="pp-card-back">~gani uchun (tavsiya bilan)</div></div>
  <div class="pp-card"><div class="pp-card-front">잠이 들다</div><div class="pp-card-back">uxlab qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">피곤하다</div><div class="pp-card-back">charchagan bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">지각하다</div><div class="pp-card-back">kechikmoq (darsga/ishga)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>1–2-savollar — bitta fe'lning 4 shakli; <strong>qo'shimchaning ma'nosi</strong> sinaladi.</li>
  <li>Qo'shimchalarni yakka yodlamang — <strong>4 oila</strong> bo'yicha taniysiz: sabab · vaqt · shart/maqsad · qarshilik.</li>
  <li>Yechish: munosabatni aniqlang → oilani toping → kerak bo'lsa nozik farqni tekshiring.</li>
  <li>Keyingi 4 darsda har oilani alohida, misollar bilan o'rganamiz.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 41) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문법 2: Sabab oilasi (-아서, -니까, -는 바람에, -느라고...)",
        "summary": "Sabab bildiruvchi qo'shimchalar orasidagi nozik farqlar: qaysi biri qachon ishlatiladi.",
        "order":   41,
        "blocks": [
            {"rich_text": """
<h2>➡️ Sabab oilasi: "Nega?"ga javob</h2>
<p>Hammasi "sabab" bildiradi, lekin har birining o'z sharti bor. TOPIK aynan shu
farqlarni sinaydi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-아/어서</strong> — eng umumiy sabab. <em>Buyruq/taklif bilan ishlatilmaydi!</em></p>
  <p style="color:#475569;margin:0 0 10px;">비가 와서 길이 막혔어요. — <em>Yomg'ir yoqqani uchun yo'l tiqilib qoldi.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)니까</strong> — sabab + <em>buyruq, taklif, tavsiya</em> keladi.</p>
  <p style="color:#475569;margin:0 0 10px;">시간이 없으니까 택시를 탑시다. — <em>Vaqt yo'q, keling taksiga chiqaylik.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-기 때문에</strong> — rasmiy, ta'kidli sabab (yozma matnlarda ko'p).</p>
  <p style="color:#475569;margin:0;">요즘 일이 많기 때문에 쉴 수 없다. — <em>Hozir ish ko'p bo'lgani sababli dam ololmayman.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 바람에</strong> — <mark style="background:#fee2e2;">kutilmagan</mark> sabab + <mark style="background:#fee2e2;">salbiy</mark> natija.</p>
  <p style="color:#475569;margin:0 0 10px;">늦잠을 자는 바람에 비행기를 놓쳤다. — <em>Uxlab qolganim tufayli samolyotdan kechib qoldim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-느라고</strong> — bir ish bilan <mark style="background:#fee2e2;">band bo'lib</mark>, boshqasini qilolmaslik (egasi bir xil).</p>
  <p style="color:#475569;margin:0 0 10px;">게임을 하느라고 숙제를 못 했어요. — <em>O'yin o'ynayverib, uy vazifasini qilolmadim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>덕분에</strong> — <mark style="background:#dcfce7;">ijobiy</mark> sabab ("sharofati bilan").</p>
  <p style="color:#475569;margin:0;">선생님 덕분에 시험에 합격했어요. — <em>Ustoz sharofati bilan imtihondan o'tdim.</em></p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat — uch belgi:</strong> natija <strong>salbiy va kutilmagan</strong> bo'lsa →
  는 바람에; "birov <strong>band bo'lib</strong> ulgurmadi" bo'lsa → -느라고; natija
  <strong>yaxshi</strong> bo'lsa → 덕분에. Uchchalasi ham "sabab", lekin almashtirib bo'lmaydi!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>어제 밤늦게까지 영화를 (        ) 오늘 아침에 늦게 일어났어요.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Kecha yarim tungacha kino (        ) bugun ertalab kech turdim.</em></p>
</div>
""",
             "choices": [
                 {"text": "보려고 (ko'rmoqchi bo'lib)", "is_correct": False},
                 {"text": "보느라고 (ko'raverib / ko'rish bilan band bo'lib)", "is_correct": True},
                 {"text": "보도록 (ko'rishi uchun)", "is_correct": False},
                 {"text": "보거나 (ko'rsam yoki)", "is_correct": False},
             ],
             "explanation": """
<p>Sxema: "kino ko'rish bilan <strong>band bo'lib</strong> → uxlashga kech yotdim → kech turdim".
Bir ish ikkinchisiga xalaqit berdi, egasi bitta (men) → <mark style="background:#dcfce7;">-느라고</mark> ✅.
-느라고 ning imzosi: undan keyin deyarli doim <strong>salbiy natija</strong> (못 했다, 늦었다,
바빴다) keladi. ①③ maqsad oilasi, ④ tanlash — munosabat sabab bo'lgani uchun to'g'ri kelmaydi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>아침에 버스를 (        ) 회사에 지각했습니다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Ertalab avtobusdan (        ) ishga kechikdim.</em></p>
</div>
""",
             "choices": [
                 {"text": "놓치는 바람에 (kechib qolganim tufayli)", "is_correct": True},
                 {"text": "놓치려고 (kechib qolish uchun)", "is_correct": False},
                 {"text": "놓치도록 (kechib qolguncha)", "is_correct": False},
                 {"text": "놓친 지 (kechib qolganimga ... bo'ldi)", "is_correct": False},
             ],
             "explanation": """
<p>"Avtobusdan kechish" — <strong>kutilmagan</strong> hodisa, "ishga kechikish" —
<strong>salbiy</strong> natija. Ikkala belgi ham bor → <mark style="background:#dcfce7;">-는 바람에</mark> ✅.
② "ataylab kechib qolish uchun" — mantiqsiz; ③ -도록 maqsad/daraja; ④ -(으)ㄴ 지 o'tgan vaqt
o'lchovi ("...ga necha vaqt bo'ldi") — gap tuzilishiga mos emas.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>친구가 도와준 (        ) 이사를 빨리 끝낼 수 있었다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Do'stim yordam bergani (        ) ko'chishni tez tugatib oldim.</em></p>
</div>
""",
             "choices": [
                 {"text": "바람에 (tufayli — salbiy)", "is_correct": False},
                 {"text": "대신에 (o'rniga)", "is_correct": False},
                 {"text": "덕분에 (sharofati bilan)", "is_correct": True},
                 {"text": "동안에 (davomida)", "is_correct": False},
             ],
             "explanation": """
<p>Natija <strong>ijobiy</strong> ("tez tugatib oldim") va sababi — birovning yaxshiligi →
<mark style="background:#dcfce7;">덕분에</mark> ✅. ① 바람에 faqat salbiy natija bilan —
"yordam bergani tufayli kechikdim" bo'lganda to'g'ri bo'lardi. Juftlikni yodlang:
<strong>yaxshi natija → 덕분에, yomon natija → 바람에 / 때문에</strong>.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-아/어서</div><div class="pp-card-back">~gani uchun (umumiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)니까</div><div class="pp-card-back">~gani uchun (+buyruq/taklif)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 때문에</div><div class="pp-card-back">~ sababli (rasmiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 바람에</div><div class="pp-card-back">~ tufayli (kutilmagan, salbiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">-느라고</div><div class="pp-card-back">~ bilan band bo'lib (ulgurmadi)</div></div>
  <div class="pp-card"><div class="pp-card-front">덕분에</div><div class="pp-card-back">sharofati bilan (ijobiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">놓치다</div><div class="pp-card-back">qo'ldan boy bermoq, kechib qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">이사</div><div class="pp-card-back">ko'chish (uy)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>-아서 = umumiy; -니까 = keyin buyruq/taklif kelganda; -기 때문에 = rasmiy-yozma.</li>
  <li>-는 바람에 = kutilmagan + salbiy; -느라고 = band bo'lib ulgurmadi; 덕분에 = ijobiy.</li>
  <li>Gapning <strong>oxiriga</strong> qarang: natija salbiymi, ijobiymi, buyruqmi — javobni o'sha tanlaydi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 42) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문법 3: Vaqt oilasi (-자마자, -다가, -면서, -고 나서...)",
        "summary": "Ish-harakatlar tartibini bildiruvchi qo'shimchalar: bir vaqtda, ketma-ket, to'xtatib, ~dan beri.",
        "order":   42,
        "blocks": [
            {"rich_text": """
<h2>⏰ Vaqt oilasi: "Qachon? Qaysi tartibda?"</h2>
<p>Bu oila ikki ish-harakatning <strong>vaqt munosabatini</strong> chizadi. Har birini
kichik "sxema" bilan tasavvur qiling:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)면서</strong> — ikki ish <mark style="background:#dbeafe;">bir vaqtda</mark> (A ∥ B).</p>
  <p style="color:#475569;margin:0 0 10px;">음악을 들으면서 운동해요. — <em>Musiqa tinglab turib sport qilaman.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-자마자</strong> — A tugashi <mark style="background:#dbeafe;">bilanoq</mark> B (A→B, oraliqsiz).</p>
  <p style="color:#475569;margin:0 0 10px;">집에 도착하자마자 손을 씻었어요. — <em>Uyga yetib kelishim bilanoq qo'limni yuvdim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-고 나서</strong> — A <mark style="background:#dbeafe;">to'liq tugagach</mark> B.</p>
  <p style="color:#475569;margin:0;">숙제를 하고 나서 게임을 했어요. — <em>Vazifani tugatib bo'lib, o'yin o'ynadim.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-다가</strong> — A qilayotib, <mark style="background:#fee2e2;">yarmida</mark> B ga o'tish (A to'xtaydi).</p>
  <p style="color:#475569;margin:0 0 10px;">밥을 먹다가 전화를 받았어요. — <em>Ovqatlanayotib telefon ko'tardim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-기 전에</strong> — B dan <mark style="background:#dbeafe;">oldin</mark> A.</p>
  <p style="color:#475569;margin:0 0 10px;">자기 전에 이를 닦으세요. — <em>Yotishdan oldin tishingizni yuving.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄴ 지</strong> — A bo'lganiga <mark style="background:#dbeafe;">qancha vaqt</mark> o'tgani (+ 되다/넘다).</p>
  <p style="color:#475569;margin:0 0 10px;">한국에 온 지 1년이 되었어요. — <em>Koreyaga kelganimga bir yil bo'ldi.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 동안</strong> — A <mark style="background:#dbeafe;">davomida</mark> B.</p>
  <p style="color:#475569;margin:0;">방학 동안 아르바이트를 했어요. — <em>Ta'til davomida qo'shimcha ishladim.</em></p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> -(으)ㄴ 지 ning imzosi — gap oxirida <strong>되다/넘다/지나다</strong>
  bilan vaqt o'lchovi turadi (1년이 되었다). Buni ko'rdingizmi — javob deyarli aniq -(으)ㄴ 지!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>수업이 (        ) 학생들이 모두 교실에서 나갔다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Dars (        ) o'quvchilarning hammasi sinfdan chiqib ketdi.</em></p>
</div>
""",
             "choices": [
                 {"text": "끝나자마자 (tugashi bilanoq)", "is_correct": True},
                 {"text": "끝나기 전에 (tugashidan oldin)", "is_correct": False},
                 {"text": "끝나는 동안 (tugash davomida)", "is_correct": False},
                 {"text": "끝난 지 (tugaganiga)", "is_correct": False},
             ],
             "explanation": """
<p>Tabiiy tartib: dars tugadi → darhol chiqib ketishdi → <mark style="background:#dcfce7;">-자마자</mark> ✅.
② "tugashidan oldin hammasi chiqib ketdi" — mantiqan g'alati (unda dars kimga?);
③ "tugash davomida" — tugash bu lahza, davomiylik emas; ④ -(으)ㄴ 지 dan keyin vaqt
o'lchovi (되다) kelishi kerak edi — bu gapda yo'q.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>한국어를 (        ) 3년이 넘었지만 아직 어려운 단어가 많다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Koreys tilini (        ) uch yildan oshdi, lekin hali qiyin so'zlar ko'p.</em></p>
</div>
""",
             "choices": [
                 {"text": "배우다가 (o'rganayotib, yarmida)", "is_correct": False},
                 {"text": "배운 지 (o'rgana boshlaganimga)", "is_correct": True},
                 {"text": "배우려고 (o'rganish uchun)", "is_correct": False},
                 {"text": "배우면서 (o'rganib turib)", "is_correct": False},
             ],
             "explanation": """
<p>Imzoni ko'rdingizmi? Gap oxirida <strong>3년이 넘었다</strong> (3 yildan oshdi) — vaqt
o'lchovi! Demak → <mark style="background:#dcfce7;">-(으)ㄴ 지</mark> ✅. "~ qilganiga X vaqt
bo'ldi/oshdi" qolipi faqat -(으)ㄴ 지 bilan yasaladi. Qolgan variantlar bu qolipga
grammatik jihatdan sig'maydi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>학교에 (        ) 갑자기 비가 와서 편의점에서 우산을 샀다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Maktabga (        ) to'satdan yomg'ir yog'ib, minimarketdan soyabon sotib oldim.</em></p>
</div>
""",
             "choices": [
                 {"text": "가고 나서 (borib bo'lgach)", "is_correct": False},
                 {"text": "간 지 (borganimga)", "is_correct": False},
                 {"text": "가다가 (ketayotib)", "is_correct": True},
                 {"text": "가자마자 (borishim bilanoq)", "is_correct": False},
             ],
             "explanation": """
<p>Yomg'ir <strong>yo'lda</strong> tutdi — harakat yarmida yangi voqea → <mark style="background:#dcfce7;">-다가</mark> ✅.
Belgi so'z: <strong>갑자기</strong> (to'satdan) ko'pincha -다가 bilan keladi. ① "borib bo'lgach"
bo'lsa, soyabonni maktabda emas, yo'ldagi do'kondan olishi mantiqqa to'g'ri kelmaydi;
④ "yetib borishi bilanoq yomg'ir yog'di" bo'lsa ham soyabon yo'lda kerak bo'lmasdi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-(으)면서</div><div class="pp-card-back">bir vaqtda (~b turib)</div></div>
  <div class="pp-card"><div class="pp-card-front">-자마자</div><div class="pp-card-back">~ bilanoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-고 나서</div><div class="pp-card-back">~b bo'lgach</div></div>
  <div class="pp-card"><div class="pp-card-front">-다가</div><div class="pp-card-back">~yotib (yarmida)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 전에</div><div class="pp-card-back">~dan oldin</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄴ 지</div><div class="pp-card-back">~ qilganiga (vaqt o'tdi)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 동안</div><div class="pp-card-back">~ davomida</div></div>
  <div class="pp-card"><div class="pp-card-front">갑자기</div><div class="pp-card-back">to'satdan</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Sxemalar: -면서 (A∥B) · -자마자 (A→B darhol) · -고 나서 (A tugadi→B) · -다가 (A yarmida→B).</li>
  <li>Imzo belgilar: 되다/넘다 + vaqt → -(으)ㄴ 지; 갑자기 → ko'pincha -다가.</li>
  <li>Gapdagi ikki ishning <strong>real tartibini</strong> tasavvur qiling — sxema o'zi tanlanadi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 43) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문법 4: Shart, maqsad va taxmin oilasi (-려면, -려고, -을까 봐...)",
        "summary": "Shart (-으면, -으려면), maqsad (-으려고, -도록) va taxmin (-을까 봐, -나 보다) qo'shimchalari.",
        "order":   43,
        "blocks": [
            {"rich_text": """
<h2>🎯 Shart, maqsad va taxmin oilasi</h2>
<p>Bu oila kelajakka qaraydi: "agar...", "...uchun", "...bo'lsa kerak". Uch guruhchaga bo'linadi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Shart</span></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)면</strong> — agar/qachonki.</p>
  <p style="color:#475569;margin:0 0 10px;">봄이 오면 꽃이 핀다. — <em>Bahor kelsa, gullar ochiladi.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)려면</strong> — "~moqchi bo'lsang" (maqsad + shart).</p>
  <p style="color:#475569;margin:0 0 10px;">기차표를 사려면 미리 예약해야 해요. — <em>Poyezd chiptasini olmoqchi bo'lsangiz, oldindan band qiling.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-아/어야</strong> — "~gandagina" (majburiy shart).</p>
  <p style="color:#475569;margin:0;">연습해야 실력이 늘어요. — <em>Mashq qilgandagina mahorat oshadi.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Maqsad</span></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)려고</strong> — "~ qilish uchun" (o'z niyati).</p>
  <p style="color:#475569;margin:0 0 10px;">살을 빼려고 매일 달리기를 해요. — <em>Ozish uchun har kuni yuguraman.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-도록</strong> — "~ bo'lishi uchun / ~guncha" (natijaga yo'naltirilgan).</p>
  <p style="color:#475569;margin:0;">잊어버리지 않도록 메모하세요. — <em>Esdan chiqmasligi uchun yozib qo'ying.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Taxmin va xavotir</span></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄹ까 봐</strong> — "~ bo'lib qolmasin deb" (xavotirdan chora).</p>
  <p style="color:#475569;margin:0 0 10px;">시험에 늦을까 봐 일찍 나왔어요. — <em>Imtihonga kechikib qolmay deb erta chiqdim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-나 보다 / -(으)ㄴ가 보다</strong> — "shekilli" (belgiga qarab taxmin).</p>
  <p style="color:#475569;margin:0;">밖이 시끄러운 걸 보니 무슨 일이 있나 봐요. — <em>Tashqari shovqinligiga qaraganda, nimadir bo'lgan shekilli.</em></p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> -(으)려고 va -(으)ㄹ까 봐 ni farqlang: <strong>istagan</strong> narsangiz
  uchun harakat → -려고; <strong>qo'rqqan</strong> narsangizdan saqlanish → -ㄹ까 봐.
  "감기에 걸릴까 봐 옷을 입었다" — shamollashni istamaysiz, undan qo'rqasiz!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>감기에 (        ) 옷을 따뜻하게 입고 나갔다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Shamollab (        ) kiyimni issiq kiyib chiqdim.</em></p>
</div>
""",
             "choices": [
                 {"text": "걸리자마자 (shamollashim bilanoq)", "is_correct": False},
                 {"text": "걸릴까 봐 (qolmay deb / qolishdan qo'rqib)", "is_correct": True},
                 {"text": "걸리려고 (shamollash uchun)", "is_correct": False},
                 {"text": "걸리고 나서 (shamollab bo'lgach)", "is_correct": False},
             ],
             "explanation": """
<p>Issiq kiyinish — shamollashning <strong>oldini olish</strong> chorasi, ya'ni xavotirdan
qilingan ish → <mark style="background:#dcfce7;">-(으)ㄹ까 봐</mark> ✅. ③ klassik tuzoq:
-려고 niyatni bildiradi — "shamollash <em>uchun</em> issiq kiyindim" — mantiqqa zid!
Salbiy narsadan saqlanayotganda doim -ㄹ까 봐.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>외국에서 오래 (        ) 그 나라의 말과 문화를 배워야 한다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Chet elda uzoq (        ) o'sha mamlakat tili va madaniyatini o'rganish kerak.</em></p>
</div>
""",
             "choices": [
                 {"text": "살려면 (yashamoqchi bo'lsangiz)", "is_correct": True},
                 {"text": "살다가 (yashayotib, yarmida)", "is_correct": False},
                 {"text": "사는 바람에 (yashagani tufayli)", "is_correct": False},
                 {"text": "살자마자 (yashashi bilanoq)", "is_correct": False},
             ],
             "explanation": """
<p>Qolipni ko'ring: "(        ) ... <strong>-아야 한다</strong>" — "~moqchi bo'lsang, ... kerak".
Bu aynan <mark style="background:#dcfce7;">-(으)려면</mark> qolipi ✅: maqsad + unga yetish
sharti. -(으)려면 ko'rsangiz, gap oxirida deyarli doim -아야 하다/-는 것이 좋다 turadi —
va aksincha! Bu juftlik TOPIKda juda ko'p sinaladi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>옆집에서 맛있는 냄새가 나는 걸 보니 저녁을 (        ).</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Qo'shnining uyidan mazali hid kelayotganiga qaraganda, kechki ovqat (        ).</em></p>
</div>
""",
             "choices": [
                 {"text": "준비하나 보다 (tayyorlayotgan shekilli)", "is_correct": True},
                 {"text": "준비해야 한다 (tayyorlash kerak)", "is_correct": False},
                 {"text": "준비하려고 한다 (tayyorlamoqchi)", "is_correct": False},
                 {"text": "준비한 적이 있다 (tayyorlagan bo'lgan)", "is_correct": False},
             ],
             "explanation": """
<p>Imzo qolip: <strong>-는 걸 보니</strong> ("...ga qaraganda") — belgiga asoslangan taxmin
kiritadi, va u deyarli doim <mark style="background:#dcfce7;">-나 보다</mark> bilan tugaydi ✅.
Hid — belgi, "tayyorlayotgan shekilli" — taxmin. ②③ o'z niyat/majburiyat — birovning uyi
haqida bunday deb bo'lmaydi; ④ tajriba (~gan bo'lgan) bu holatga mos emas.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-(으)면</div><div class="pp-card-back">agar ~sa</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)려면</div><div class="pp-card-back">~moqchi bo'lsang (…kerak)</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어야</div><div class="pp-card-back">~gandagina</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)려고</div><div class="pp-card-back">~ qilish uchun (niyat)</div></div>
  <div class="pp-card"><div class="pp-card-front">-도록</div><div class="pp-card-back">~ bo'lishi uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ까 봐</div><div class="pp-card-back">~ bo'lib qolmasin deb</div></div>
  <div class="pp-card"><div class="pp-card-front">-나 보다</div><div class="pp-card-back">~ shekilli (taxmin)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 걸 보니</div><div class="pp-card-back">~ga qaraganda</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Shart: -으면 (agar), -으려면 (+kerak), -아야 (faqat shunda).</li>
  <li>Maqsad: -으려고 (niyat), -도록 (natija uchun). Salbiydan saqlanish esa → -을까 봐!</li>
  <li>Taxmin: -나 보다; imzosi — oldida "-는 걸 보니" (belgiga qaraganda).</li>
  <li>Qolip juftliklarini yodlang: -려면 ↔ -아야 하다; -는 걸 보니 ↔ -나 보다.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 5 (order 44) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문법 5: Qarshilik oilasi + jamlovchi mashq",
        "summary": "-지만, -는데도, 아무리 ~아도 kabi qarshilik shakllari va to'rt oila bo'yicha aralash test.",
        "order":   44,
        "blocks": [
            {"rich_text": """
<h2>🔄 Qarshilik oilasi: "lekin, shunga qaramay"</h2>
<p>Oxirgi oila — kutilgan natija <strong>chiqmaganda</strong> ishlatiladigan shakllar:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-지만</strong> — oddiy "lekin".</p>
  <p style="color:#475569;margin:0 0 10px;">이 옷은 예쁘지만 비싸요. — <em>Bu kiyim chiroyli, lekin qimmat.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄴ/는데도</strong> — "~ qilsa ham (natija yo'q)" — real holat.</p>
  <p style="color:#475569;margin:0 0 10px;">약을 먹는데도 감기가 낫지 않아요. — <em>Dori ichsam ham shamollash tuzalmayapti.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-아/어도</strong> — "~sa ham" (umumiy).</p>
  <p style="color:#475569;margin:0 0 10px;">바빠도 아침을 꼭 먹어요. — <em>Band bo'lsam ham nonushtani albatta qilaman.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-더라도</strong> — "hatto ~ bo'lsa ham" (kuchli faraz).</p>
  <p style="color:#475569;margin:0 0 10px;">실패하더라도 후회하지 않을 거예요. — <em>Hatto muvaffaqiyatsiz bo'lsam ham afsuslanmayman.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 대신에</strong> — "o'rniga / evaziga".</p>
  <p style="color:#475569;margin:0;">주말에 일하는 대신에 평일에 쉬어요. — <em>Dam olish kuni ishlash evaziga ish kunida dam olaman.</em></p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Oltin juftlik — <strong>아무리 ~아/어도</strong>
  ("qancha ~masin"): gapda <strong>아무리</strong> ko'rinsa, javob deyarli har doim
  <strong>-아/어도</strong> bilan tugaydi. 아무리 기다려도 버스가 안 와요. —
  <em>Qancha kutmayin, avtobus kelmayapti.</em>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>매일 열심히 (        ) 한국어 실력이 늘지 않아서 고민이다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Har kuni astoydil (        ) koreys tilim o'smayotgani meni o'ylantiradi.</em></p>
</div>
""",
             "choices": [
                 {"text": "공부하려고 (o'qish uchun)", "is_correct": False},
                 {"text": "공부하는데도 (o'qisam ham)", "is_correct": True},
                 {"text": "공부하니까 (o'qiganim uchun)", "is_correct": False},
                 {"text": "공부하자마자 (o'qishim bilanoq)", "is_correct": False},
             ],
             "explanation": """
<p>Kutilgan: o'qisang → til o'sadi. Real natija: <strong>o'smayapti</strong> — kutilganning
teskarisi, real holat → <mark style="background:#dcfce7;">-는데도</mark> ✅. ③ 니까 bo'lsa
"o'qiganim uchun o'smayapti" — sabab-natija buziladi. Belgi: gap oxirida <strong>-지 않다 +
고민/걱정</strong> ko'rinsa, qarshilik oilasini qidiring.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>아무리 (        ) 건강을 위해서 아침 운동은 계속할 거예요.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Qancha (        ) salomatligim uchun ertalabki sportni davom ettiraman.</em></p>
</div>
""",
             "choices": [
                 {"text": "피곤해도 (charchasam ham)", "is_correct": True},
                 {"text": "피곤해서 (charchaganim uchun)", "is_correct": False},
                 {"text": "피곤하니까 (charchaganim sababli)", "is_correct": False},
                 {"text": "피곤하면서 (charchab turib)", "is_correct": False},
             ],
             "explanation": """
<p>Oltin juftlik ishladi: <strong>아무리</strong> + ? → <mark style="background:#dcfce7;">-아/어도</mark> ✅.
"Qancha charchamayin — baribir davom ettiraman". ②③ sabab oilasi — 아무리 bilan grammatik
jihatdan umuman birika olmaydi. Bu juftlikni bilish = tayyor 2 ball.</p>
"""},
            {"rich_text": """
<h3>🏁 Jamlovchi mashq — to'rt oila aralash</h3>
<p>Endi imtihondagidek: oilani o'zingiz aniqlang!</p>
<p><strong>Amaliyot 3.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>지갑을 집에 (        ) 다시 돌아가야 했다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Hamyonni uyda (        ) yana qaytib borishga to'g'ri keldi.</em></p>
</div>
""",
             "choices": [
                 {"text": "두고 오는 바람에 (qoldirib kelganim tufayli)", "is_correct": True},
                 {"text": "두고 오려고 (qoldirib kelish uchun)", "is_correct": False},
                 {"text": "두고 와도 (qoldirib kelsam ham)", "is_correct": False},
                 {"text": "두고 온 지 (qoldirib kelganimga)", "is_correct": False},
             ],
             "explanation": """
<p>Oila: kutilmagan hodisa (hamyon esdan chiqdi) + salbiy natija (qaytishga majbur) —
sabab oilasi, aniq shakli <mark style="background:#dcfce7;">-는 바람에</mark> ✅ (2-darsni
eslang: kutilmagan + salbiy). ② "ataylab qoldirish uchun" — mantiqsiz; ③ qarshilik bo'lsa
"qaytmasdim" kelishi kerak edi; ④ vaqt o'lchovi qolipi emas.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 4.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>주말에는 보통 집에서 (        ) 가까운 공원에 산책하러 가요.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Dam olish kunlari odatda uyda (        ) yaqin bog'ga sayrga chiqaman.</em></p>
</div>
""",
             "choices": [
                 {"text": "쉬는데도 (dam olsam ham)", "is_correct": False},
                 {"text": "쉬거나 (dam olaman yoki)", "is_correct": True},
                 {"text": "쉬자마자 (dam olishim bilanoq)", "is_correct": False},
                 {"text": "쉬느라고 (dam olish bilan band bo'lib)", "is_correct": False},
             ],
             "explanation": """
<p>Bu gap ikki <strong>teng variantni</strong> sanayapti: "uyda dam olaman <em>yoki</em>
bog'ga chiqaman" → <mark style="background:#dcfce7;">-거나</mark> ("yoki") ✅. 보통 (odatda)
so'zi odatiy ikki tanlovga ishora qiladi. ①③④ oilalarining hech biri "ikkidan biri"
ma'nosini bermaydi. -거나 kichik, lekin 1-savolda tez-tez chiqadigan shakl!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-지만</div><div class="pp-card-back">lekin</div></div>
  <div class="pp-card"><div class="pp-card-front">-는데도</div><div class="pp-card-back">~sa ham (natija yo'q)</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어도</div><div class="pp-card-back">~sa ham</div></div>
  <div class="pp-card"><div class="pp-card-front">아무리 ~아도</div><div class="pp-card-back">qancha ~masin</div></div>
  <div class="pp-card"><div class="pp-card-front">-더라도</div><div class="pp-card-back">hatto ~sa ham</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 대신에</div><div class="pp-card-back">~ o'rniga / evaziga</div></div>
  <div class="pp-card"><div class="pp-card-front">-거나</div><div class="pp-card-back">~ yoki</div></div>
  <div class="pp-card"><div class="pp-card-front">고민</div><div class="pp-card-back">tashvish, o'y</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Qarshilik: -지만 (oddiy) · -는데도 (real, natija yo'q) · -더라도 (kuchli faraz) · 아무리+~아도.</li>
  <li>To'rt oila xaritasi tayyor: <strong>sabab · vaqt · shart/maqsad · qarshilik</strong> — har 1–2-savolda avval oilani toping.</li>
  <li>Imzo juftliklar eng tez yo'l: 아무리→아도, -려면→아야 하다, 되다+vaqt→-은 지, 갑자기→-다가, 걸 보니→-나 보다.</li>
  <li>Ikkala savolga 1 daqiqa — ortganini uzun matnlarga saqlang!</li>
</ul>
"""},
        ],
    },
]
