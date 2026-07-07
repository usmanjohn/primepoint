# TOPIK II O'qish (읽기) darslari 1–3. Til: O'zbekcha + Koreyscha, rangli styling bilan.
# STYLE_GUIDE_TOPIK.md ga qarang.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_1_3.py --author=prime
# (mavjudini yangilash uchun --republish qo'shing).

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

LESSONS = [
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 1: O'qish bo'limi qanday ishlaydi",
        "summary": "읽기 bo'limining tuzilishi — 70 daqiqada 50 savol — va vaqtni to'g'ri "
                   "taqsimlash strategiyasi.",
        "order":   1,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 1: O'qish bo'limi qanday ishlaydi</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">읽기</span>
&nbsp;<span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">50 savol · 70 daqiqa</span></p>
<p>Har qanday strategiyadan oldin <mark>imtihon tuzilishini</mark> bilish kerak — necha
savol, qancha vaqt va qiyinlik qanday oshadi. Buni bilish — birinchi haqiqiy strategiya.</p>
""",
            },
            {
                "rich_text": """
<h3>Asosiy ma'lumotlar</h3>
<ul>
  <li><strong>50 savol</strong>, <strong>70 daqiqa</strong> — ya'ni har bir savolga o'rtacha
      <mark style="background:#dbeafe;">taxminan 1 daqiqa 24 soniya.</mark></li>
  <li>Savollar <strong>raqami oshgani sari qiyinlashadi.</strong> Boshidagilar (1–20) qisqa
      va tez; oxirgilari (40–50) — uzun matnlar, har biriga 2 tadan savol.</li>
  <li>Hammasi <strong>test</strong> — 4 ta variant, bitta to'g'ri javob.</li>
</ul>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Oson, boshidagi savollarga <em>kam</em> vaqt sarflang —
  shunda oxiridagi uzun matnlar uchun vaqt <mark style="background:#dcfce7;">tejaysiz.</mark>
</div>
""",
            },
            {
                "rich_text": """
<h3>Vaqtni qanday taqsimlash kerak</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p>Oddiy nazorat nuqtalari sizni xavfsiz saqlaydi: 20-daqiqada ~20-savol atrofida,
    45-daqiqada ~35-savol atrofida bo'ling.</p>
  </div>
  <div class="pp-step">
    <div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:0;">
      <strong>⚠️ Diqqat:</strong> Agar orqada qolsangiz — <strong>taxmin qiling va keyingisiga
      o'ting.</strong> Bo'sh qoldirilgan javob ham, xato javob ham bir xil — lekin bo'sh javob
      hech qachon to'g'ri bo'lolmaydi.
    </div>
  </div>
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<p class="text-secondary small">Kartani bosib ag'daring — koreyscha so'zni ko'rib, ma'nosini eslang.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">읽기</div><div class="pp-card-back">o'qish</div></div>
  <div class="pp-card"><div class="pp-card-front">지문</div><div class="pp-card-back">matn / parcha</div></div>
  <div class="pp-card"><div class="pp-card-front">문제</div><div class="pp-card-back">savol</div></div>
  <div class="pp-card"><div class="pp-card-front">정답</div><div class="pp-card-back">to'g'ri javob</div></div>
  <div class="pp-card"><div class="pp-card-front">시간 배분</div><div class="pp-card-back">vaqtni taqsimlash</div></div>
  <div class="pp-card"><div class="pp-card-front">추측하다</div><div class="pp-card-back">taxmin qilmoq</div></div>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>50 savol, 70 daqiqa; raqam oshgani sari qiyinlashadi.</li>
    <li>Boshida tez, oxirida sekin va diqqat bilan.</li>
    <li>Hech qachon bo'sh qoldirmang — taxmin qilish bepul.</li>
  </ul>
</div>
""",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> 30 daqiqa o'tdi, lekin siz hali "
                             "15-savoldasiz. Eng to'g'ri harakat qaysi?</p>",
                "choices": [
                    {"text": "Sekin davom etib, 1–15 ni mukammal qilaman.", "is_correct": False},
                    {"text": "Tezlashaman va kerak bo'lsa taxmin qilib, uzun matnlarga vaqt qoldiraman.", "is_correct": True},
                    {"text": "To'g'ridan-to'g'ri 50-savolga o'tib, orqaga ishlayman.", "is_correct": False},
                    {"text": "O'qishni to'xtatib, qolgan hammasiga 2-variantni belgilab chiqaman.", "is_correct": False},
                ],
                "explanation": "<p>Siz vaqtdan orqadasiz (20-daqiqada ~20-savolda bo'lish kerak edi). "
                               "Tezlashish va taxmin qilish oxiridagi qimmatli uzun matnlar uchun "
                               "vaqtni saqlaydi — u yerda bitta matnga 2 ta savol to'g'ri keladi.</p>",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 2: Asosiy fikrni tez topish (중심 생각)",
        "summary": "Matnni har bir so'zni tarjima qilmasdan, asosiy fikr (중심 생각) uchun "
                   "tez o'qishni o'rganamiz.",
        "order":   2,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 2: Asosiy fikrni tez topish</h2>
<p><span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">중심 생각</span></p>
<p>Ko'p talaba har bir so'zni tushunishga urinib, vaqtini yo'qotadi. Ball keltiradigan
ko'nikma — <mark>tez o'qish (훑어 읽기)</mark> orqali <strong>asosiy fikrni (중심 생각)</strong>
ilg'ash.</p>
""",
            },
            {
                "rich_text": """
<h3>Asosiy fikr qayerda yashiringan?</h3>
<p>Koreys izohli matnlarida asosiy fikr odatda <strong>birinchi yoki oxirgi gapda</strong>
bo'ladi. O'rtasi — misol va tafsilotlar. Demak, gap chetlarini diqqat bilan, o'rtasini
tez o'qib, abzasni tushunsa bo'ladi.</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat — fikr signallari:</strong> bu so'zlar muallifning fikrini bildiradi:
  <mark style="background:#dbeafe;">-아야/어야 한다</mark> (kerak),
  <mark style="background:#dbeafe;">중요하다</mark> (muhim),
  <mark style="background:#dbeafe;">따라서</mark> (shuning uchun).
</div>
""",
            },
            {
                "rich_text": """
<h3>Ishlangan namuna — qadam-baqadam</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">요즘 사람들은 시간이 없다는 이유로 아침을 거르는 경우가 많다.
  그러나 아침 식사는 하루의 활동에 필요한 에너지를 준다.
  <strong>따라서 바쁘더라도 아침을 꼭 먹는 것이 좋다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Hozir odamlar vaqt yo'qligi sababli ko'pincha
  nonushtani o'tkazib yuboradi. Lekin nonushta kun davomidagi faoliyat uchun energiya beradi.
  Shuning uchun band bo'lsa ham, nonushta qilish yaxshi.</em></p>
</div>
<p>Endi shu matnni imtihondagidek, qadam-baqadam tahlil qilamiz:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — birinchi gap.</strong> 요즘 사람들은... 아침을 거르는 경우가 많다 —
    bu <em>holat</em> (odamlar nonushtani o'tkazib yuboradi). Hali muallif fikri emas —
    belgilab, davom etamiz.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — o'rtadagi gap.</strong> 그러나 (lekin) bilan boshlanadi va
    <em>sabab</em> beradi: nonushta energiya beradi. Bu — <mark style="background:#fee2e2;">tafsilot</mark>,
    asosiy fikr emas. O'rtani tez o'qib o'tamiz.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — oxirgi gap.</strong> <mark style="background:#dbeafe;">따라서</mark>
    (shuning uchun) — fikr signali! Muallifning xulosasi shu yerda:
    <mark style="background:#dcfce7;">band bo'lsa ham nonushta qilish kerak.</mark>
    Javob shu gapdan chiqadi.</p>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Tez-tez uchraydigan xato:</strong> o'rtadagi <em>to'g'ri lekin asosiy bo'lmagan</em>
  tafsilotga aldanmang. Variant <strong>to'g'ri bo'lishi mumkin, ammo asosiy fikr emas.</strong>
</div>
""",
            },
            {
                "rich_text": """
<h3>Yana bir namuna — endi o'zingiz</h3>
<p>Quyidagi qisqa matnni <mark>tez o'qing</mark> — chetki gaplarga diqqat, o'rtasiga
ko'z yugurtiring. Keyin savolga javob bering.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">휴대폰은 우리 생활을 편리하게 만들었다.
  그러나 잠들기 전에 휴대폰을 오래 보면 잠을 잘 자기 어렵다.
  <strong>그러므로 자기 전에는 휴대폰 사용을 줄여야 한다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Telefon hayotimizni qulay qildi. Lekin uxlashdan
  oldin telefonni uzoq ko'rsangiz, yaxshi uxlash qiyin bo'ladi. Shuning uchun uxlashdan
  oldin telefon ishlatishni kamaytirish kerak.</em></p>
</div>
<p><strong>Amaliyot.</strong> Bu matnning asosiy fikri (중심 생각) qaysi?</p>
""",
                "choices": [
                    {"text": "Telefon hayotni qulay qildi.", "is_correct": False},
                    {"text": "Uxlashdan oldin telefon ishlatishni kamaytirish kerak.", "is_correct": True},
                    {"text": "Telefonni uzoq ko'rish ko'zga zarar.", "is_correct": False},
                    {"text": "Kechasi telefon ko'rish uyquni yaxshilaydi.", "is_correct": False},
                ],
                "explanation": "<p>Oxirgi gap <strong>그러므로</strong> (shuning uchun) bilan boshlanadi — "
                               "fikr signali: <em>자기 전에는 휴대폰 사용을 줄여야 한다</em> = uxlashdan oldin "
                               "telefon ishlatishni kamaytirish kerak. Bunda <strong>-아야/어야 한다</strong> "
                               "(kerak) qo'shimchasi ham muallif fikrini bildiradi. 1-variant to'g'ri fakt, "
                               "lekin bu kirish gap — asosiy fikr emas; 3-variant matnda umuman yo'q; "
                               "4-variant matnga zid.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> Abzas shu gap bilan tugaydi: "
                             "“<strong>그러므로 규칙적인 운동이 건강에 가장 중요하다.</strong>” "
                             "Asosiy fikr qaysi?</p>",
                "choices": [
                    {"text": "Hozir ko'p odamlar band.", "is_correct": False},
                    {"text": "Muntazam jismoniy mashq sog'liq uchun eng muhim.", "is_correct": True},
                    {"text": "Mashq ba'zan jarohatga olib keladi.", "is_correct": False},
                    {"text": "Sog'liqni o'lchash qiyin.", "is_correct": False},
                ],
                "explanation": "<p>Oxirgi gap <strong>그러므로</strong> (shuning uchun) bilan "
                               "boshlanib, muallif fikrini to'g'ridan-to'g'ri aytadi: muntazam "
                               "mashq sog'liq uchun eng muhim. Boshqa variantlar — tafsilot yoki "
                               "chalg'ituvchi, asosiy fikr emas.</p>",
            },
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<p class="text-secondary small">Kartani bosib ag'daring — koreyscha so'zni ko'rib, ma'nosini eslang.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">중심 생각</div><div class="pp-card-back">asosiy fikr</div></div>
  <div class="pp-card"><div class="pp-card-front">훑어 읽기</div><div class="pp-card-back">tez ko'zdan kechirib o'qish</div></div>
  <div class="pp-card"><div class="pp-card-front">따라서</div><div class="pp-card-back">shuning uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">그러므로</div><div class="pp-card-back">shuning uchun (rasmiyroq)</div></div>
  <div class="pp-card"><div class="pp-card-front">그러나</div><div class="pp-card-back">lekin</div></div>
  <div class="pp-card"><div class="pp-card-front">세부 내용</div><div class="pp-card-back">tafsilot</div></div>
  <div class="pp-card"><div class="pp-card-front">-아야/어야 한다</div><div class="pp-card-back">... kerak (fikr signali)</div></div>
  <div class="pp-card"><div class="pp-card-front">중요하다</div><div class="pp-card-back">muhim bo'lmoq</div></div>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Har so'zni tarjima qilmang — asosiy fikr uchun tez o'qing.</li>
    <li>Fikr odatda birinchi yoki oxirgi gapda; 따라서/그러므로/-아야 한다 — signallar.</li>
    <li>To'g'ri tafsilot har doim ham asosiy fikr emas.</li>
  </ul>
</div>
""",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 3: Savolni matndan oldin o'qing",
        "summary": "Savol va variantlarni qidiruv nishoniga aylantirib, matnni maqsad bilan "
                   "o'qishni o'rganamiz.",
        "order":   3,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 3: Savolni matndan oldin o'qing</h2>
<p>Deyarli har bir savolda vaqt tejaydigan oddiy odat — <strong>avval savol va 4 ta
variantni</strong> o'qing, keyin matnni aynan o'sha ma'lumotni qidirib o'qing.</p>
""",
            },
            {
                "rich_text": """
<h3>Nega bu ishlaydi?</h3>
<p>Matnni shunchaki o'qisangiz, hech narsa aniq esda qolmaydi va javob berish uchun qayta
o'qishga to'g'ri keladi. Savolni oldin o'qisangiz, miyangizda <mark>qidiruv nishoni</mark>
bo'ladi — kerakli gapga yetganda darrov sezasiz.</p>
<details open style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📂 Savol turi → nimani qidirish kerak</summary>
  <div style="margin-top:10px;">
    <ul style="margin:0;">
      <li><strong>일치하는 내용</strong> (mos tafsilot) → mos keladigan faktni qidiring.</li>
      <li><strong>중심 생각</strong> (asosiy fikr) → birinchi/oxirgi gapni kuzating.</li>
      <li><strong>빈칸</strong> (bo'sh joy) → bo'shliq atrofidagi mantiqni o'qing.</li>
    </ul>
  </div>
</details>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Savoldagi bitta kalit so'zni (ism, raqam, mavzu so'zi)
  belgilab, matndan shuni qidiring.
</div>
""",
            },
            {
                "rich_text": """
<h3>Odatni jonli ko'ramiz — qadam-baqadam</h3>
<p>Savol: <strong>“이 글의 내용과 같은 것을 고르십시오.”</strong> <em>(Matn mazmuniga mos
kelganini tanlang.)</em> Matn — oddiy e'lon:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>도서관 이용 안내</strong><br>
  평일에는 밤 10시까지 이용할 수 있습니다.<br>
  주말에는 오후 6시에 문을 닫습니다.<br>
  시험 기간에는 24시간 열려 있습니다.</p>
  <p style="color:#475569;margin:0;"><em>Kutubxonadan foydalanish haqida ma'lumot:
  ish kunlari kechki 10 gacha foydalanish mumkin. Dam olish kunlari 18:00 da yopiladi.
  Imtihon davrida 24 soat ochiq.</em></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — savol turini aniqlang.</strong> 일치하는 내용 — demak, variantlardagi
    <em>faktlarni</em> matn bilan solishtirish kerak. Fikr izlamaymiz, fakt izlaymiz.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — variantlardan kalit so'zlarni belgilang.</strong> Variantlarda
    <mark style="background:#dbeafe;">평일</mark> (ish kunlari),
    <mark style="background:#dbeafe;">주말</mark> (dam olish kunlari),
    <mark style="background:#dbeafe;">시험 기간</mark> (imtihon davri) va soatlar bor —
    demak, qidiruv nishonimiz: <em>qaysi kun → qaysi soat</em>.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — matnni nishon bilan o'qing.</strong> Har bir gap — bitta fakt:
    평일 → 밤 10시, 주말 → 오후 6시, 시험 기간 → 24시간. Uch juftlikni belgilab oldik —
    endi variantlarni birma-bir tekshirish oson.</p>
  </div>
  <div class="pp-step">
    <p><strong>4-qadam — har variantni matndan tasdiqlang.</strong> “Deyarli to'g'ri”
    variantlar aynan shu yerda tuzoq qo'yadi: kun bilan soatni <em>almashtirib</em> beradi
    (masalan, dam olish kuniga ish kunining soatini yozadi). Juftlikni aniq solishtiring.</p>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Variantlarni oldin o'qish — faqat ulardan taxmin qilish
  degani <strong>emas</strong>. Variantlar — sizning <strong>qidiruv ro'yxatingiz</strong>,
  lekin javobni baribir matndan <mark style="background:#dcfce7;">tasdiqlang.</mark>
  TOPIK <em>deyarli</em> to'g'ri variantlarni yaxshi ko'radi.
</div>
""",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> Yuqoridagi kutubxona e'loni bo'yicha: "
                             "matn mazmuniga mos kelgan variantni tanlang (이 글의 내용과 같은 것).</p>",
                "choices": [
                    {"text": "Dam olish kunlari kutubxona kechki 10 gacha ochiq.", "is_correct": False},
                    {"text": "Imtihon davrida kutubxona tunda ham ochiq.", "is_correct": True},
                    {"text": "Ish kunlari kutubxona 18:00 da yopiladi.", "is_correct": False},
                    {"text": "Kutubxona har doim 24 soat ishlaydi.", "is_correct": False},
                ],
                "explanation": "<p>Matnda: <em>시험 기간에는 24시간 열려 있습니다</em> — imtihon davrida "
                               "24 soat ochiq, demak tunda ham ochiq. ✓</p>"
                               "<p>1- va 3-variantlar — klassik tuzoq: kun va soat <strong>almashtirilgan</strong> "
                               "(kechki 10 — bu 평일, ish kunlari; 18:00 esa 주말, dam olish kunlari). "
                               "4-variant esa faktni kengaytirib yuboradi: 24 soat faqat 시험 기간, "
                               "imtihon davrida.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> Matndan oldin 4 ta variantni "
                             "o'qish nega foydali?</p>",
                "choices": [
                    {"text": "Matnni umuman o'qimasdan javob tanlash uchun.", "is_correct": False},
                    {"text": "Qidiriladigan kalit so'zlarni beradi — matnni maqsad bilan o'qiysiz.", "is_correct": True},
                    {"text": "Chunki birinchi variant odatda to'g'ri bo'ladi.", "is_correct": False},
                    {"text": "Eng qiyin savollarni avtomatik o'tkazib yuborish uchun.", "is_correct": False},
                ],
                "explanation": "<p>Variantlar qidiruv ro'yxati bo'lib xizmat qiladi: qaysi kalit "
                               "so'z va faktlarni qidirishni aytadi, shunda matnni ikki marta "
                               "o'qimasdan, aniq nishon bilan o'qiysiz. Javobni baribir matndan "
                               "tasdiqlaysiz.</p>",
            },
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<p class="text-secondary small">Kartani bosib ag'daring — koreyscha so'zni ko'rib, ma'nosini eslang.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">일치하는 내용</div><div class="pp-card-back">mos keladigan mazmun</div></div>
  <div class="pp-card"><div class="pp-card-front">빈칸</div><div class="pp-card-back">bo'sh joy</div></div>
  <div class="pp-card"><div class="pp-card-front">고르다</div><div class="pp-card-back">tanlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">핵심어</div><div class="pp-card-back">kalit so'z</div></div>
  <div class="pp-card"><div class="pp-card-front">확인하다</div><div class="pp-card-back">tasdiqlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">안내</div><div class="pp-card-back">e'lon / ma'lumot</div></div>
  <div class="pp-card"><div class="pp-card-front">평일</div><div class="pp-card-back">ish kunlari</div></div>
  <div class="pp-card"><div class="pp-card-front">주말</div><div class="pp-card-back">dam olish kunlari</div></div>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Avval savol va variantlarni, keyin matnni o'qing.</li>
    <li>Kalit so'zni belgilab, uni qidiring.</li>
    <li>Javobni har doim matndan tasdiqlang — “deyarli to'g'ri” variantdan ehtiyot bo'ling.</li>
  </ul>
</div>
""",
            },
        ],
    },
]
