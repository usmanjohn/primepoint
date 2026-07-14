# TOPIK II Reading — Reklama va e'lonlar (광고·안내문), lessons 1–5 (orders 10–14).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_ads_1_5.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "Reklama va e'lonlar (광고·안내문)",
    "summary": "5–8-savollar: qisqa reklama, shior va e'lon matnlarining mavzusini topish.",
    "icon":    "bi-megaphone",
    "order":   2,
}

LESSONS = [
    # ── Lesson 1 (order 10) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 광고 1: 5–8-savollar bilan tanishuv",
        "summary": "Reklama savollari qanday tuzilgan, nimani so'raydi va ularni 30 soniyada yechish strategiyasi.",
        "order":   10,
        "blocks": [
            {"rich_text": """
<h2>📢 5–8-savollar: eng oson 8 ball</h2>
<p>TOPIK II o'qish bo'limida <strong>5–8-savollar</strong> doim bir xil ko'rinishda keladi:
qisqa <mark style="background:#dbeafe;">reklama (광고)</mark> yoki
<mark style="background:#dbeafe;">e'lon (안내문)</mark> beriladi va siz bu matn
<strong>nima haqida</strong> ekanini topasiz. Savol matni har doim shu:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음은 무엇에 대한 글인지 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi matn nima haqida ekanini tanlang.</em></p>
</div>
<p>Bu savollar imtihonning <strong>eng oson qismi</strong> — matn 1–2 qatorli, javob esa
bitta so'z (신발, 병원, 여행사...). Lekin oson bo'lgani uchun bu yerda
<strong>xato qilish juda achinarli</strong>: 8 ballni hech kimga bermang!</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Odatda 5–6-savollar mahsulot yoki joy reklamasi,
  7-savol ijtimoiy (공익) reklama, 8-savol esa e'lon yoki yo'riqnoma bo'ladi.
</div>
"""},
            {"rich_text": """
<h3>Strategiya: 3 qadamda 30 soniya</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — Kalit so'zlarni toping.</strong> Reklamada 1–2 ta hal qiluvchi so'z bo'ladi.
    Masalan <strong>발이 편해요</strong> (oyoq qulay) → gap <mark style="background:#dcfce7;">poyabzal</mark> haqida.
    Butun jumlani tarjima qilish shart emas!</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — Variantlarga qarang.</strong> To'rttala variant doim bitta turkumdan bo'ladi
    (hammasi mahsulot yoki hammasi joy). Kalit so'zingizga mos kelmaydiganlarini chizib tashlang.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — Tuzoqni tekshiring.</strong> Reklamada ataylab boshqa variantga o'xshash so'z
    qo'shiladi. Masalan <strong>아침</strong> (tong) so'zi bor deb darrov <strong>식당</strong> demang —
    balki gap <strong>침대</strong> (yotoq) haqidadir: "편안한 잠자리, 가벼운 아침".</p>
  </div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> 5–8-savollarga jami <strong>2 daqiqadan ortiq</strong> vaqt sarflamang.
  Bu yerda tejagan vaqtingiz 21–50-savollardagi uzun matnlarga kerak bo'ladi.
</div>
"""},
            {"rich_text": """
<h3>Reklama tili qanday bo'ladi?</h3>
<p>Koreys reklamalari <strong>to'liq gap ishlatmaydi</strong> — ular qisqa, ohangdor va
ko'pincha ot bilan tugaydi. Shu 3 belgini bilsangiz, matnni o'qish osonlashadi:</p>
<ul>
  <li><strong>Ot bilan tugash:</strong> 깨끗한 세상, 편안한 하루 — fe'lsiz, lo'nda.</li>
  <li><strong>Buyruq ohangi (-세요 / -십시오):</strong> 지금 전화하세요! — <em>Hoziroq qo'ng'iroq qiling!</em></li>
  <li><strong>Savol-javob:</strong> 영어가 어려우세요? — <em>Ingliz tili qiyinmi?</em> (keyin yechim taklif qilinadi).</li>
</ul>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 Namuna:</strong> 무더운 여름, 시원한 바람으로 이겨 내세요! —
  <em>Jazirama yozni salqin shabada bilan yengib chiqing!</em> → javob: <strong>에어컨</strong> (konditsioner).
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>소중한 순간을 그대로! 흔들림 없이 선명하게!</strong></p>
  <p style="color:#475569;margin:0;"><em>Qadrli lahzalarni o'z holicha! Titramasdan, aniq-tiniq!</em> → 사진기 (fotoapparat)</p>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>가벼운 발걸음! 하루 종일 걸어도 발이 편안합니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "모자 (bosh kiyim)", "is_correct": False},
                 {"text": "신발 (poyabzal)", "is_correct": True},
                 {"text": "가방 (sumka)", "is_correct": False},
                 {"text": "안경 (ko'zoynak)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit so'zlar: <strong>발걸음</strong> (qadam) va <strong>발이 편안합니다</strong> (oyoq qulay).
Oyoqqa tegishli buyum — bu <mark style="background:#dcfce7;">신발 (poyabzal)</mark>.
Tarjima: "Yengil qadam! Kun bo'yi yursangiz ham oyog'ingiz qulay."</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>매일 아침 신선하게! 우리 아이 키가 쑥쑥 자랍니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "빵 (non)", "is_correct": False},
                 {"text": "과일 (meva)", "is_correct": False},
                 {"text": "우유 (sut)", "is_correct": True},
                 {"text": "사탕 (konfet)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit so'zlar: <strong>신선하게</strong> (yangi holda) va <strong>키가 자랍니다</strong> (bo'y o'sadi).
Har kuni ertalab ichiladigan, bolaning bo'yini o'stiradigan yangi mahsulot —
<mark style="background:#dcfce7;">우유 (sut)</mark>. 쑥쑥 — "tez-tez, g'arq-g'arq" (o'sishni kuchaytiruvchi so'z).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">광고</div><div class="pp-card-back">reklama</div></div>
  <div class="pp-card"><div class="pp-card-front">안내문</div><div class="pp-card-back">e'lon, yo'riqnoma</div></div>
  <div class="pp-card"><div class="pp-card-front">무엇에 대한 글</div><div class="pp-card-back">nima haqidagi matn</div></div>
  <div class="pp-card"><div class="pp-card-front">신선하다</div><div class="pp-card-back">yangi, toza (mahsulot)</div></div>
  <div class="pp-card"><div class="pp-card-front">편안하다</div><div class="pp-card-back">qulay, tinch</div></div>
  <div class="pp-card"><div class="pp-card-front">선명하다</div><div class="pp-card-back">aniq, tiniq</div></div>
  <div class="pp-card"><div class="pp-card-front">이겨 내다</div><div class="pp-card-back">yengib chiqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">소중하다</div><div class="pp-card-back">qadrli, aziz</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>5–8-savollar — qisqa reklama/e'lon matnining <strong>mavzusini</strong> topish; eng oson 8 ball.</li>
  <li>Butun matnni tarjima qilmang — <strong>1–2 ta kalit so'z</strong> yetarli.</li>
  <li>Reklama tili: ot bilan tugaydi, -세요 buyruq ohangi, savol-javob shakli.</li>
  <li>Tuzoq so'zlarga ehtiyot bo'ling: bitta tanish so'zga emas, <strong>umumiy ma'noga</strong> qarang.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 11) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 광고 2: Mahsulot reklamalari (상품 광고)",
        "summary": "Eng ko'p chiqadigan mahsulotlar (uy jihozlari, kiyim, oziq-ovqat) va ularning kalit so'zlari.",
        "order":   11,
        "blocks": [
            {"rich_text": """
<h2>🛒 Mahsulot reklamasi (상품 광고)</h2>
<p>5–6-savollarda ko'pincha <strong>mahsulot reklamasi</strong> keladi. Yaxshi yangilik:
TOPIKda chiqadigan mahsulotlar ro'yxati <strong>uncha katta emas</strong> va har birining
o'z "imzo so'zlari" bor. Shu juftliklarni o'rganib olsangiz, javobni matnni to'liq
o'qimasdan ham topasiz.</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Mahsulotni emas, <strong>mahsulot → kalit so'z</strong> juftligini yodlang.
  Masalan "침대 (karavot)" so'zini alohida emas, <strong>잠 (uyqu) → 침대</strong> bog'lamasi bilan.
</div>
"""},
            {"rich_text": """
<h3>Uy jihozlari — imzo so'zlari bilan</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>찌든 때도 한 번에! 조용해서 밤에도 걱정 없습니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Eng eski kirni ham bir yo'la! Shovqinsiz — kechasi ham bemalol.</em> → <strong>세탁기</strong> (kir yuvish mashinasi)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>편안한 잠자리가 상쾌한 아침을 만듭니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Qulay yotoq — tetik tongni yaratadi.</em> → <strong>침대</strong> (karavot)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>음식이 오래오래 신선하게! 전기 요금 걱정도 줄였습니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Ovqat uzoq vaqt yangiligicha! Elektr to'lovi tashvishi ham kamaydi.</em> → <strong>냉장고</strong> (muzlatgich)</p>
</div>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 Mahsulot → kalit so'z jadvali — bosing</summary>
  <div style="margin-top:10px;">
    <ul>
      <li><strong>세탁기</strong> (kir mashinasi) → 때 (kir), 빨래 (yuvish), 조용하다 (jim)</li>
      <li><strong>냉장고</strong> (muzlatgich) → 신선하다 (yangi), 음식 (ovqat), 오래 (uzoq)</li>
      <li><strong>에어컨</strong> (konditsioner) → 여름 (yoz), 시원하다 (salqin), 바람 (shamol)</li>
      <li><strong>침대</strong> (karavot) → 잠 (uyqu), 편안하다 (qulay), 아침 (tong)</li>
      <li><strong>청소기</strong> (changyutgich) → 먼지 (chang), 깨끗하다 (toza)</li>
      <li><strong>신발</strong> (poyabzal) → 발 (oyoq), 걷다 (yurmoq), 가볍다 (yengil)</li>
      <li><strong>화장품</strong> (kosmetika) → 피부 (teri), 촉촉하다 (nam, yumshoq)</li>
      <li><strong>치약</strong> (tish pastasi) → 이 (tish), 상쾌하다 (toza his), 숨결 (nafas)</li>
      <li><strong>우유</strong> (sut) → 아침 (ertalab), 키 (bo'y), 아이 (bola)</li>
      <li><strong>사진기</strong> (fotoapparat) → 순간 (lahza), 선명하다 (tiniq)</li>
    </ul>
  </div>
</details>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> 시원하다 (salqin) so'zi 에어컨, 선풍기 (ventilyator) va hatto 음료수
  (ichimlik) reklamasida ham chiqadi. Yakuniy javobni <strong>qolgan so'zlar</strong> hal qiladi:
  바람 bo'lsa — texnika, 마시다 bo'lsa — ichimlik.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>작은 먼지까지 한 번에! 우리 집이 더 깨끗해집니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "세탁기 (kir mashinasi)", "is_correct": False},
                 {"text": "냉장고 (muzlatgich)", "is_correct": False},
                 {"text": "청소기 (changyutgich)", "is_correct": True},
                 {"text": "에어컨 (konditsioner)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit so'z: <strong>먼지</strong> (chang) + <strong>깨끗해집니다</strong> (tozalanadi).
Changni yutib, uyni toza qiladigan narsa — <mark style="background:#dcfce7;">청소기</mark>.
세탁기 tuzog'iga tushmang: u ham "tozalaydi", lekin kirni (때, 빨래), changni emas.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>하루 종일 촉촉하게! 건조한 겨울에도 피부 걱정이 없습니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "약 (dori)", "is_correct": False},
                 {"text": "화장품 (kosmetika)", "is_correct": True},
                 {"text": "옷 (kiyim)", "is_correct": False},
                 {"text": "비누 (sovun)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit so'zlar: <strong>촉촉하게</strong> (nam, yumshoq holda) va <strong>피부</strong> (teri).
Terini quruqlikdan saqlaydigan mahsulot — <mark style="background:#dcfce7;">화장품</mark> (krem/kosmetika).
비누 (sovun) aksincha terini quritishi mumkin — reklama "quruq qishda ham" deyapti.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>하루 세 번, 3분! 상쾌한 숨결과 하얀 이를 지켜 드립니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "칫솔 (tish cho'tkasi)", "is_correct": False},
                 {"text": "치약 (tish pastasi)", "is_correct": True},
                 {"text": "거울 (oyna)", "is_correct": False},
                 {"text": "수건 (sochiq)", "is_correct": False},
             ],
             "explanation": """
<p><strong>하루 세 번</strong> (kuniga uch marta), <strong>하얀 이</strong> (oq tishlar),
<strong>상쾌한 숨결</strong> (toza nafas) — bularning bari tish tozalash haqida.
칫솔 ham mumkin edi, lekin "toza nafas"ni beradigan, an'anaviy "3·3·3" qoidasi bilan
reklama qilinadigani — <mark style="background:#dcfce7;">치약</mark>.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">먼지</div><div class="pp-card-back">chang</div></div>
  <div class="pp-card"><div class="pp-card-front">때</div><div class="pp-card-back">kir (dog')</div></div>
  <div class="pp-card"><div class="pp-card-front">피부</div><div class="pp-card-back">teri</div></div>
  <div class="pp-card"><div class="pp-card-front">촉촉하다</div><div class="pp-card-back">nam, yumshoq</div></div>
  <div class="pp-card"><div class="pp-card-front">건조하다</div><div class="pp-card-back">quruq</div></div>
  <div class="pp-card"><div class="pp-card-front">상쾌하다</div><div class="pp-card-back">tetik, toza (his)</div></div>
  <div class="pp-card"><div class="pp-card-front">잠자리</div><div class="pp-card-back">yotoq, uyqu joyi</div></div>
  <div class="pp-card"><div class="pp-card-front">지키다</div><div class="pp-card-back">saqlamoq, himoya qilmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Mahsulot reklamalari cheklangan ro'yxatdan keladi — <strong>mahsulot → kalit so'z</strong> juftliklarini yodlang.</li>
  <li>Bitta sifat (시원하다, 깨끗하다) bir nechta mahsulotga mos kelishi mumkin — <strong>otlarga</strong> qarab aniqlang.</li>
  <li>Tuzoq: o'xshash vazifali buyumlar (세탁기/청소기, 치약/칫솔) — farqlovchi so'zni toping.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 12) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 광고 3: Xizmat va joy reklamalari (업소 광고)",
        "summary": "Shifoxona, bank, sayohat agentligi, o'quv markazi kabi joylar reklamasini bir qarashda tanish.",
        "order":   12,
        "blocks": [
            {"rich_text": """
<h2>🏢 Joy va xizmat reklamasi (업소 광고)</h2>
<p>Mahsulotdan keyingi eng ko'p uchraydigan tur — <strong>joy/xizmat reklamasi</strong>:
shifoxona, bank, sayohat agentligi, o'quv markazi... Bu yerda ham har bir joyning
o'z "imzo so'zlari" bor, lekin bitta muhim farq bor:</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Joy reklamasida ko'pincha <strong>xizmat fe'llari</strong> ishlatiladi:
  모시다 (kutib olmoq, olib bormoq), 도와드리다 (yordam bermoq), 찾아드리다 (topib bermoq),
  지켜드리다 (saqlab bermoq). <strong>-드리다</strong> qo'shimchasini ko'rsangiz — bu xizmat!
</div>
"""},
            {"rich_text": """
<h3>Eng ko'p chiqadigan joylar</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>바다로? 산으로? 원하시는 곳 어디든지 모시고 갑니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Dengizgami? Toqqami? Istagan joyingizga olib boramiz.</em> → <strong>여행사</strong> (sayohat agentligi)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>영어가 어려우세요? 석 달 만에 자신 있게 말하게 됩니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Ingliz tili qiyinmi? Uch oyda dadil gapiradigan bo'lasiz.</em> → <strong>학원</strong> (o'quv markazi)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>소중한 당신의 돈, 안전하게 지켜 드립니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Qadrli pulingizni xavfsiz saqlab beramiz.</em> → <strong>은행</strong> (bank)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>어머니의 손맛 그대로, 정성을 담았습니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Onaning qo'l ta'mi o'z holicha, mehr bilan tayyorladik.</em> → <strong>식당</strong> (oshxona/restoran)</p>
</div>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 Joy → kalit so'z jadvali — bosing</summary>
  <div style="margin-top:10px;">
    <ul>
      <li><strong>병원</strong> (shifoxona) → 아프다 (og'rimoq), 진료 (ko'rik), 건강 (salomatlik)</li>
      <li><strong>약국</strong> (dorixona) → 약 (dori), 처방전 (retsept)</li>
      <li><strong>은행</strong> (bank) → 돈 (pul), 통장 (hisob daftarchasi), 안전하다 (xavfsiz)</li>
      <li><strong>여행사</strong> (sayohat agentligi) → 여행 (sayohat), 바다/산, 모시다</li>
      <li><strong>학원</strong> (o'quv markazi) → 배우다 (o'rganmoq), 실력 (mahorat), 수업 (dars)</li>
      <li><strong>미용실</strong> (sartaroshxona) → 머리 (soch), 모양 (shakl), 새롭다 (yangi)</li>
      <li><strong>식당</strong> (restoran) → 맛 (ta'm), 손맛, 정성 (mehr)</li>
      <li><strong>세탁소</strong> (kimyoviy tozalash) → 옷 (kiyim), 깨끗하게, 빨다 (yuvmoq)</li>
      <li><strong>부동산</strong> (rieltorlik) → 집 (uy), 가격 (narx), 구하다 (izlamoq)</li>
      <li><strong>사진관</strong> (fotostudiya) → 사진 (surat), 추억 (xotira)</li>
    </ul>
  </div>
</details>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> <strong>Mahsulotmi yoki joymi?</strong> 머리 (soch) so'zi shampun
  reklamasida ham, 미용실 reklamasida ham bo'ladi. Farq: joy reklamasida xizmat fe'llari
  (해 드립니다) va taklif (오세요 — keling!) bo'ladi; mahsulotda esa buyumning sifati maqtaladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>아픈 곳은 이제 그만! 친절한 진료, 편리한 예약으로 모시겠습니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "약국 (dorixona)", "is_correct": False},
                 {"text": "병원 (shifoxona)", "is_correct": True},
                 {"text": "체육관 (sportzal)", "is_correct": False},
                 {"text": "미용실 (sartaroshxona)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit so'zlar: <strong>아픈 곳</strong> (og'riyotgan joy), <strong>진료</strong> (tibbiy ko'rik),
<strong>예약</strong> (band qilish). Ko'rik va qabulga yozilish bo'ladigan joy —
<mark style="background:#dcfce7;">병원</mark>. Dorixonada 진료 bo'lmaydi, faqat dori sotiladi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>원하시는 집을 원하시는 가격으로! 지금 바로 찾아 드립니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "가구점 (mebel do'koni)", "is_correct": False},
                 {"text": "이삿짐센터 (ko'chirish xizmati)", "is_correct": False},
                 {"text": "부동산 (rieltorlik idorasi)", "is_correct": True},
                 {"text": "은행 (bank)", "is_correct": False},
             ],
             "explanation": """
<p><strong>집</strong> (uy) + <strong>가격</strong> (narx) + <strong>찾아 드립니다</strong> (topib beramiz) —
uy topib beradigan xizmat bu <mark style="background:#dcfce7;">부동산</mark>.
이삿짐센터 tuzoq: u uy <em>topib bermaydi</em>, faqat yukni <em>ko'chiradi</em> (옮기다).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>새로운 머리 모양으로 기분까지 새롭게! 예약하시면 기다리지 않으셔도 됩니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "모자 가게 (shlyapa do'koni)", "is_correct": False},
                 {"text": "미용실 (sartaroshxona)", "is_correct": True},
                 {"text": "사진관 (fotostudiya)", "is_correct": False},
                 {"text": "옷 가게 (kiyim do'koni)", "is_correct": False},
             ],
             "explanation": """
<p><strong>머리 모양</strong> (soch turmagi) so'zi hal qiladi: sochga yangi shakl beradigan joy —
<mark style="background:#dcfce7;">미용실</mark>. 예약 (oldindan yozilish) ham xizmat ko'rsatish
joyiga xos belgi. Tarjima: "Yangi soch turmagi bilan kayfiyat ham yangi!"</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">진료</div><div class="pp-card-back">tibbiy ko'rik</div></div>
  <div class="pp-card"><div class="pp-card-front">예약</div><div class="pp-card-back">oldindan band qilish</div></div>
  <div class="pp-card"><div class="pp-card-front">모시다</div><div class="pp-card-back">kutib olmoq, olib bormoq (hurmat)</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어 드리다</div><div class="pp-card-back">...qilib bermoq (xizmat)</div></div>
  <div class="pp-card"><div class="pp-card-front">정성</div><div class="pp-card-back">mehr, sidqidil</div></div>
  <div class="pp-card"><div class="pp-card-front">실력</div><div class="pp-card-back">mahorat, daraja</div></div>
  <div class="pp-card"><div class="pp-card-front">구하다</div><div class="pp-card-back">izlamoq, topmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">손맛</div><div class="pp-card-back">qo'l ta'mi (pazandalik mahorati)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Joy reklamasining belgisi — <strong>xizmat fe'llari</strong>: 모시다, -아/어 드리다, 오세요.</li>
  <li>Har bir joyning imzo so'zi bor: 진료 → 병원, 머리 모양 → 미용실, 집+가격 → 부동산.</li>
  <li>O'xshash joylarni farqlang: 병원/약국 (ko'rik bormi?), 부동산/이삿짐센터 (topadimi yoki ko'chiradimi?).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 13) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 광고 4: Ijtimoiy reklama (공익 광고)",
        "summary": "7-savol: tabiatni asrash, tejash, xavfsizlik kabi ijtimoiy mavzudagi shiorlarni tushunish.",
        "order":   13,
        "blocks": [
            {"rich_text": """
<h2>🌱 Ijtimoiy reklama (공익 광고)</h2>
<p><strong>7-savol</strong> odatda <mark style="background:#dbeafe;">공익 광고</mark> —
"jamiyat foydasi uchun" reklama bo'ladi. Bu yerda mahsulot sotilmaydi; sizni biror
<strong>yaxshi odatga chaqirishadi</strong>: tabiatni asrash, suvni tejash, xavfsiz haydash...</p>
<p>Javob variantlari ham mavzu nomlari bo'ladi: <strong>환경 보호</strong> (atrof-muhitni asrash),
<strong>절약</strong> (tejash), <strong>안전 운전</strong> (xavfsiz haydash) va hokazo.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Ijtimoiy reklama ko'pincha <strong>majoziy</strong> (ko'chma ma'noda) yoziladi.
  So'zma-so'z tarjima qilsangiz g'alati tuyuladi — <strong>nimaga chaqirayotganini</strong> o'ylang.
</div>
"""},
            {"rich_text": """
<h3>Klassik shiorlar — tahlil bilan</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi namuna ▸">
  <div class="pp-step">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>5분 먼저 가려다 50년 먼저 갑니다.</strong></p>
      <p style="color:#475569;margin:0;"><em>5 daqiqa oldin boraman deb, 50 yil oldin ketasiz.</em></p>
    </div>
    <p>Bu yerda "50 yil oldin ketish" — erta o'lish degani. Tezlik haqida ogohlantiryapti →
    <mark style="background:#dcfce7;">교통 안전 / 안전 운전</mark> (yo'l xavfsizligi).</p>
  </div>
  <div class="pp-step">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>잠그면 모이고 열어 두면 사라집니다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Yopsangiz yig'iladi, ochiq qoldirsangiz yo'qoladi.</em></p>
    </div>
    <p>Nimani "yopish" mumkin? Jo'mrakni! → <mark style="background:#dcfce7;">물 절약</mark> (suvni tejash).</p>
  </div>
  <div class="pp-step">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>고운 말 한마디가 하루를 밝게 만듭니다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Bitta shirin so'z kunni yorug' qiladi.</em></p>
    </div>
    <p><strong>말</strong> (so'z) + 고운 (chiroyli) → <mark style="background:#dcfce7;">언어 예절</mark>
    (so'zlashish odobi).</p>
  </div>
  <div class="pp-step">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>당신의 피 한 방울이 한 생명을 살립니다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Bir tomchi qoningiz bir hayotni saqlab qoladi.</em></p>
    </div>
    <p><strong>피</strong> (qon) + 살리다 (saqlab qolmoq) → <mark style="background:#dcfce7;">헌혈</mark>
    (qon topshirish, donorlik).</p>
  </div>
</div>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 Ijtimoiy mavzular lug'ati — bosing</summary>
  <div style="margin-top:10px;">
    <ul>
      <li><strong>환경 보호</strong> — atrof-muhitni asrash (지구, 자연, 살리다)</li>
      <li><strong>물/전기 절약</strong> — suv/elektr tejash (아끼다, 잠그다, 플러그)</li>
      <li><strong>교통 안전</strong> — yo'l xavfsizligi (속도, 사고, 지키다)</li>
      <li><strong>건강 관리</strong> — salomatlikka qarash (걷기, 운동, 습관)</li>
      <li><strong>독서</strong> — kitob o'qish (책, 지식, 길)</li>
      <li><strong>언어 예절</strong> — so'zlashish odobi (고운 말, 인사)</li>
      <li><strong>헌혈</strong> — qon topshirish (피, 생명)</li>
      <li><strong>분리수거</strong> — chiqindini saralash (쓰레기, 재활용)</li>
    </ul>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>쓰지 않는 플러그는 뽑아 주세요. 작은 습관이 큰돈을 아낍니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "환경 보호 (atrof-muhitni asrash)", "is_correct": False},
                 {"text": "전기 절약 (elektrni tejash)", "is_correct": True},
                 {"text": "교통 안전 (yo'l xavfsizligi)", "is_correct": False},
                 {"text": "건강 관리 (salomatlikka qarash)", "is_correct": False},
             ],
             "explanation": """
<p><strong>플러그를 뽑다</strong> — vilkani rozetkadan sug'urmoq. Ishlatilmayotgan jihozni
o'chirib, pul tejashga chaqiryapti → <mark style="background:#dcfce7;">전기 절약</mark>.
환경 보호 yaqin tuzoq — lekin matn tabiat emas, <strong>큰돈 (katta pul)</strong> haqida gapiryapti.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>하루 30분 걷기, 100세 건강의 첫걸음입니다.</strong></p>
</div>
""",
             "choices": [
                 {"text": "여행 (sayohat)", "is_correct": False},
                 {"text": "등산 (toqqa chiqish)", "is_correct": False},
                 {"text": "건강 관리 (salomatlikka qarash)", "is_correct": True},
                 {"text": "시간 절약 (vaqtni tejash)", "is_correct": False},
             ],
             "explanation": """
<p><strong>걷기</strong> (yurish) + <strong>100세 건강</strong> (100 yoshgacha salomatlik) →
kundalik yurish odati salomatlik garovi ekanini aytyapti —
<mark style="background:#dcfce7;">건강 관리</mark>. 첫걸음 — "birinchi qadam" degani.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>버리면 쓰레기, 나누면 자원입니다. 병은 병끼리, 종이는 종이끼리!</strong></p>
</div>
""",
             "choices": [
                 {"text": "분리수거 (chiqindini saralash)", "is_correct": True},
                 {"text": "물 절약 (suvni tejash)", "is_correct": False},
                 {"text": "청소 (tozalash)", "is_correct": False},
                 {"text": "이웃 사랑 (qo'shniga mehr)", "is_correct": False},
             ],
             "explanation": """
<p><strong>병은 병끼리, 종이는 종이끼리</strong> — "shisha shishaga, qog'oz qog'ozga" —
chiqindini turiga qarab ajratish → <mark style="background:#dcfce7;">분리수거</mark>.
나누면 자원 — "ajratsangiz — xomashyo". 나누다 so'zidan "qo'shniga mehr" demang: kontekst chiqindi haqida.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">공익 광고</div><div class="pp-card-back">ijtimoiy reklama</div></div>
  <div class="pp-card"><div class="pp-card-front">절약</div><div class="pp-card-back">tejash</div></div>
  <div class="pp-card"><div class="pp-card-front">아끼다</div><div class="pp-card-back">tejamoq, ayamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">보호</div><div class="pp-card-back">himoya, asrash</div></div>
  <div class="pp-card"><div class="pp-card-front">살리다</div><div class="pp-card-back">saqlab qolmoq, jonlantirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">습관</div><div class="pp-card-back">odat</div></div>
  <div class="pp-card"><div class="pp-card-front">생명</div><div class="pp-card-back">hayot, jon</div></div>
  <div class="pp-card"><div class="pp-card-front">재활용</div><div class="pp-card-back">qayta ishlash</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>공익 광고 mahsulot sotmaydi — <strong>yaxshi odatga chaqiradi</strong>; javob mavzu nomi bo'ladi.</li>
  <li>Shiorlar <strong>majoziy</strong>: so'zma-so'z emas, "nimaga chaqiryapti?" deb o'ylang.</li>
  <li>Mavzu lug'atini yodlang: 절약, 보호, 안전, 예절, 헌혈, 분리수거.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 5 (order 14) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 광고 5: E'lon va yo'riqnomalar (안내문) + aralash mashq",
        "summary": "8-savol turidagi e'lonlar (ish, ta'mirlash, qoidalar) va butun mavzu bo'yicha mini-test.",
        "order":   14,
        "blocks": [
            {"rich_text": """
<h2>📋 E'lon va yo'riqnoma (안내문)</h2>
<p><strong>8-savol</strong> ko'pincha reklama emas, <mark style="background:#dbeafe;">안내문</mark> —
rasmiy e'lon bo'ladi: do'kon e'loni, foydalanish qoidasi, ish e'loni... Bu matnlar
reklamaga qaraganda <strong>quruqroq va rasmiyroq</strong> yoziladi, javob esa e'lonning
<strong>turi</strong> bo'ladi:</p>
<ul>
  <li><strong>교환 안내</strong> — almashtirish tartibi (영수증 — chek, 7일 이내 — 7 kun ichida)</li>
  <li><strong>이용 안내</strong> — foydalanish tartibi (시간 — vaqt, 휴관 — yopiq kun)</li>
  <li><strong>사용 방법</strong> — ishlatish usuli (먼저 — avval, 다음에 — keyin, 버튼 — tugma)</li>
  <li><strong>주의 사항</strong> — ehtiyot choralari (-지 마십시오 — qilmang!)</li>
  <li><strong>모집 안내</strong> — qabul/ishga olish e'loni (신청 — ariza, 경력 — tajriba)</li>
</ul>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> E'lonning turini <strong>fe'l shakli</strong> ochib beradi:
  qadam-baqadam buyruqlar (-으십시오) → 사용 방법; taqiqlar (-지 마십시오) → 주의 사항;
  shartlar (-으면 ... 됩니다) → 교환/이용 안내.
</div>
"""},
            {"rich_text": """
<h3>Namunalar</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>구입하신 날부터 7일 이내에 영수증과 함께 가져오시면 새 물건으로 바꿔 드립니다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Sotib olgan kundan 7 kun ichida chek bilan olib kelsangiz, yangisiga almashtirib beramiz.</em> → <strong>교환 안내</strong></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>먼저 뚜껑을 연 후에 뜨거운 물을 붓고 3분간 기다리십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Avval qopqog'ini oching, so'ng qaynoq suv quyib, 3 daqiqa kuting.</em> → <strong>사용 방법</strong> (ramen tayyorlash!)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>함께 일할 가족을 찾습니다. 경력 3년 이상, 이번 달 말까지 신청하십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Birga ishlaydigan "oila a'zosini" izlaymiz. 3 yildan ortiq tajriba, shu oy oxirigacha ariza topshiring.</em> → <strong>사원 모집</strong></p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> 가족을 찾습니다 ("oila izlaymiz") ko'rinishiga aldanmang —
  ish e'lonlarida xodimni iliq qilib "oila" deyishadi. <strong>경력</strong> (ish tajribasi) va
  <strong>신청</strong> (ariza) so'zlari buni ish e'loni ekanini ko'rsatadi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>약은 어린이의 손이 닿지 않는 곳에 두시고, 정해진 시간에만 드십시오.</strong></p>
</div>
""",
             "choices": [
                 {"text": "사용 방법 (ishlatish usuli)", "is_correct": False},
                 {"text": "주의 사항 (ehtiyot choralari)", "is_correct": True},
                 {"text": "교환 안내 (almashtirish tartibi)", "is_correct": False},
                 {"text": "모집 안내 (qabul e'loni)", "is_correct": False},
             ],
             "explanation": """
<p>Matn dorini <strong>qanday saqlash va nimadan ehtiyot bo'lish</strong>ni aytyapti:
bolalar qo'li yetmaydigan joyda saqlang, faqat belgilangan vaqtda iching —
bu <mark style="background:#dcfce7;">주의 사항</mark>. 사용 방법 bo'lishi uchun
qadam-baqadam ishlatish tartibi (먼저... 다음에...) bo'lishi kerak edi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (aralash).</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>흰옷은 더 하얗게, 색깔 옷은 더 선명하게! 적은 양으로도 강력하게!</strong></p>
</div>
""",
             "choices": [
                 {"text": "세탁소 (kimyoviy tozalash)", "is_correct": False},
                 {"text": "세탁기 (kir mashinasi)", "is_correct": False},
                 {"text": "세제 (kir yuvish vositasi)", "is_correct": True},
                 {"text": "옷 가게 (kiyim do'koni)", "is_correct": False},
             ],
             "explanation": """
<p>Qiyin savol — uchta variant ham "kir yuvish" mavzusidan! Hal qiluvchi ibora:
<strong>적은 양으로도</strong> (oz miqdorda ham) — miqdor bilan o'lchanadigan narsa
faqat <mark style="background:#dcfce7;">세제</mark> (poroshok/vosita). 세탁기 bo'lsa
shovqin/tezlik, 세탁소 bo'lsa xizmat fe'llari maqtalar edi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (aralash).</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>책 속에 길이 있습니다. 하루 10분, 아이와 함께 펼쳐 보세요.</strong></p>
</div>
""",
             "choices": [
                 {"text": "독서 (kitob o'qish)", "is_correct": True},
                 {"text": "서점 (kitob do'koni)", "is_correct": False},
                 {"text": "도서관 이용 안내 (kutubxona tartibi)", "is_correct": False},
                 {"text": "지도 (xarita)", "is_correct": False},
             ],
             "explanation": """
<p><strong>책 속에 길이 있다</strong> — "kitob ichida yo'l bor" (mashhur maqol) +
kuniga 10 daqiqa bola bilan o'qishga chaqiriq → bu ijtimoiy reklama, mavzusi
<mark style="background:#dcfce7;">독서</mark>. 서점 bo'lganida narx/chegirma (할인)
haqida so'z bo'lardi. 길 so'zidan "xarita" demang — u majoziy ma'noda!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 4 (aralash).</strong> 다음은 무엇에 대한 글인지 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>관람 시간: 오전 9시 ~ 오후 6시 (매주 월요일 휴관) / 입장은 마감 30분 전까지</strong></p>
</div>
""",
             "choices": [
                 {"text": "영화 광고 (kino reklamasi)", "is_correct": False},
                 {"text": "이용 안내 (foydalanish tartibi)", "is_correct": True},
                 {"text": "모집 안내 (qabul e'loni)", "is_correct": False},
                 {"text": "교환 안내 (almashtirish tartibi)", "is_correct": False},
             ],
             "explanation": """
<p><strong>관람 시간</strong> (tomosha vaqti), <strong>휴관</strong> (yopiq kun),
<strong>입장</strong> (kirish) — muzey/ko'rgazmaning ish tartibi haqidagi ma'lumot —
<mark style="background:#dcfce7;">이용 안내</mark>. Hech narsa sotilmayapti ham,
chaqirilmayapti ham — faqat <strong>tartib</strong> e'lon qilinyapti.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">교환</div><div class="pp-card-back">almashtirish</div></div>
  <div class="pp-card"><div class="pp-card-front">환불</div><div class="pp-card-back">pulni qaytarish</div></div>
  <div class="pp-card"><div class="pp-card-front">영수증</div><div class="pp-card-back">chek, kvitansiya</div></div>
  <div class="pp-card"><div class="pp-card-front">모집</div><div class="pp-card-back">qabul, ishga olish</div></div>
  <div class="pp-card"><div class="pp-card-front">신청</div><div class="pp-card-back">ariza (topshirish)</div></div>
  <div class="pp-card"><div class="pp-card-front">경력</div><div class="pp-card-back">ish tajribasi</div></div>
  <div class="pp-card"><div class="pp-card-front">휴관</div><div class="pp-card-back">yopiq kun (muassasa)</div></div>
  <div class="pp-card"><div class="pp-card-front">주의</div><div class="pp-card-back">diqqat, ehtiyot</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li><strong>5–6-savol:</strong> mahsulot/joy reklamasi — imzo so'z juftliklarini ishlating.</li>
  <li><strong>7-savol:</strong> 공익 광고 — majoziy shior, "nimaga chaqiryapti?" deb so'rang.</li>
  <li><strong>8-savol:</strong> 안내문 — fe'l shakliga qarang: buyruqlar → 사용 방법, taqiqlar → 주의 사항, shartlar → 교환/이용 안내.</li>
  <li>To'rt savolga jami <strong>2 daqiqa</strong> — tejalgan vaqt uzun matnlarga!</li>
</ul>
"""},
        ],
    },
]
