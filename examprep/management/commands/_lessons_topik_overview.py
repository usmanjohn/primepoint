# TOPIK II ga umumiy kirish (orientation) — 2 qismli batafsil dars.
# Til: O'zbekcha (asosiy) + Koreyscha (qavs/kartada). Rangli styling bilan.
# Skill = strategy (imtihonga umumiy yo'riqnoma). Order 1-2 (kirish darslari birinchi turadi).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_overview.py --author=prime
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
    # QISM 1 — Tuzilma, vaqt, ball va darajalar
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "strategy",
        "title":   "TOPIK II — Kirish (1-qism): Tuzilma, vaqt, ball va darajalar",
        "summary": "TOPIK II nima, qanday bo'limlardan iborat, qancha davom etadi, "
                   "necha ball beriladi va qaysi ball qaysi darajaga (3–6급) olib chiqadi.",
        "order":   1,
        "blocks": [
            # ── 1. Kirish ──────────────────────────────────────────────
            {
                "rich_text": """
<h2>TOPIK II — Umumiy kirish (1-qism)</h2>
<p>
  <span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">yo'riqnoma</span>&nbsp;
  <span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">tuzilma</span>&nbsp;
  <span style="background:#f59e0b;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">vaqt &amp; ball</span>
</p>
<p>Imtihonga tayyorgarlikni <strong>o'yinning qoidalarini bilishdan</strong> boshlash kerak.
Bu darsda <mark>TOPIK II</mark> imtihoni <strong>qanday tuzilgani</strong>, <strong>qancha
davom etishi</strong>, <strong>necha ball berilishi</strong> va <strong>qaysi ball qaysi
darajaga</strong> (급) olib chiqishini to'liq ko'rib chiqamiz.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 TOPIK nima?</strong> TOPIK (한국어능력시험 — <em>Test of Proficiency in Korean</em>) —
  koreys tilini ona tili bo'lmaganlar uchun rasmiy davlat darajasini o'lchaydigan imtihon.
  Universitetga kirish, ish va viza uchun talab qilinadi.
</div>
""",
            },
            # ── 2. TOPIK I vs TOPIK II ─────────────────────────────────
            {
                "rich_text": """
<h3>TOPIK I va TOPIK II — qaysi birini topshirasiz?</h3>
<p>TOPIK ikki xil imtihonga bo'linadi. Siz o'z darajangizga qarab <strong>bittasini</strong>
tanlaysiz:</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;margin:14px 0;">
  <div style="flex:1 1 240px;background:#f1f5f9;border-top:4px solid #94a3b8;padding:14px 16px;border-radius:10px;">
    <strong>TOPIK I (초급)</strong><br>
    <span style="color:#475569;">Boshlang'ich daraja. Faqat <strong>듣기</strong> (tinglash) va
    <strong>읽기</strong> (o'qish). <mark style="background:#dbeafe;">1–2급</mark> beradi.</span>
  </div>
  <div style="flex:1 1 240px;background:#eff6ff;border-top:4px solid #3b82f6;padding:14px 16px;border-radius:10px;">
    <strong>TOPIK II (중·고급)</strong><br>
    <span style="color:#475569;">O'rta va yuqori daraja. <strong>듣기 + 쓰기 + 읽기</strong>
    (tinglash, <u>yozish</u>, o'qish). <mark style="background:#dcfce7;">3–6급</mark> beradi.</span>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Muhim farq:</strong> TOPIK II'da qo'shimcha ravishda <mark>쓰기 (Yozish)</mark>
  bo'limi bor — bu ko'plab talabalar uchun eng qiyin qism. Bu kurs aynan <strong>TOPIK II</strong>
  ga tayyorlaydi.
</div>
""",
            },
            # ── 3. Uch bo'lim ──────────────────────────────────────────
            {
                "rich_text": """
<h3>TOPIK II ning uch bo'limi (영역)</h3>
<p>TOPIK II uchta bo'limdan iborat. Har biri alohida <strong>100 balldan</strong> baholanadi:</p>
<div style="display:flex;flex-wrap:wrap;gap:12px;margin:14px 0;">
  <div style="flex:1 1 200px;background:#eff6ff;border-left:4px solid #3b82f6;padding:14px 16px;border-radius:8px;">
    <div style="font-size:1.6em;">🎧</div>
    <strong>듣기 — Tinglash</strong><br>
    <span style="color:#475569;">50 ta savol · test (변별형)<br>Ovozli yozuvni tinglab javob berasiz.</span>
  </div>
  <div style="flex:1 1 200px;background:#faf5ff;border-left:4px solid #a855f7;padding:14px 16px;border-radius:8px;">
    <div style="font-size:1.6em;">✍️</div>
    <strong>쓰기 — Yozish</strong><br>
    <span style="color:#475569;">4 ta savol · yozma javob<br>Jumla to'ldirish, grafik tavsifi va insho.</span>
  </div>
  <div style="flex:1 1 200px;background:#ecfdf5;border-left:4px solid #10b981;padding:14px 16px;border-radius:8px;">
    <div style="font-size:1.6em;">📖</div>
    <strong>읽기 — O'qish</strong><br>
    <span style="color:#475569;">50 ta savol · test<br>Matnlarni o'qib savollarga javob berasiz.</span>
  </div>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>📌 Eslatma:</strong> 듣기 va 읽기 — <mark>test (variantli)</mark> savollar; 쓰기 esa
  <mark style="background:#f3e8ff;">o'z qo'lingiz bilan yozadigan</mark> javoblar. Shu bois 쓰기
  alohida tayyorgarlik talab qiladi.
</div>
""",
            },
            # ── 4. Vaqt jadvali (timeline) ─────────────────────────────
            {
                "rich_text": """
<h3>Vaqt jadvali — imtihon ikki sessiyada (교시) bo'ladi</h3>
<p>TOPIK II bir kunda, lekin <strong>ikki bosqichda</strong> o'tkaziladi. Orada tanaffus bo'ladi:</p>

<div style="background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:14px 16px;margin:12px 0;">
  <div style="font-weight:700;color:#1d4ed8;margin-bottom:8px;">1교시 — Birinchi sessiya (110 daqiqa)</div>
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <div style="flex:1 1 200px;background:#fff;border-radius:8px;padding:10px 12px;">
      🎧 <strong>듣기 (Tinglash)</strong><br><span style="color:#475569;">50 savol · <mark>60 daqiqa</mark></span>
    </div>
    <div style="flex:1 1 200px;background:#fff;border-radius:8px;padding:10px 12px;">
      ✍️ <strong>쓰기 (Yozish)</strong><br><span style="color:#475569;">4 savol · <mark>50 daqiqa</mark></span>
    </div>
  </div>
  <div style="color:#475569;font-size:0.9em;margin-top:8px;">
    ⚠️ Diqqat: 듣기 tugagach 쓰기 ga <u>avtomatik</u> o'tiladi — vaqtingizni o'zingiz taqsimlaysiz.
  </div>
</div>

<div style="text-align:center;color:#94a3b8;font-size:0.9em;margin:6px 0;">☕ Tanaffus (쉬는 시간)</div>

<div style="background:#ecfdf5;border:1px solid #a7f3d0;border-radius:10px;padding:14px 16px;margin:12px 0;">
  <div style="font-weight:700;color:#047857;margin-bottom:8px;">2교시 — Ikkinchi sessiya (70 daqiqa)</div>
  <div style="background:#fff;border-radius:8px;padding:10px 12px;">
    📖 <strong>읽기 (O'qish)</strong><br><span style="color:#475569;">50 savol · <mark style="background:#dcfce7;">70 daqiqa</mark></span>
  </div>
</div>

<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>⚠️ Vaqtni boshqarish:</strong> Birinchi sessiyada 듣기 (60 daq.) tugagach darrov
  쓰기 (50 daq.) boshlanadi. 쓰기'ning <mark style="background:#fee2e2;">54-savoli (insho)</mark>
  ko'p vaqt oladi — shuning uchun 듣기 paytida tez ishlab, 쓰기 ga vaqt qoldiring.
</div>
""",
            },
            # ── 5. Ballar / max ball ───────────────────────────────────
            {
                "rich_text": """
<h3>Ballar — jami 300 ball (총점 300점)</h3>
<p>Har bir bo'lim <strong>100 balldan</strong>, jami <mark>300 ball</mark>. Ball taqsimoti:</p>

<table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:0.97em;">
  <thead>
    <tr style="background:#3b82f6;color:#fff;">
      <th style="padding:10px;text-align:left;border-radius:8px 0 0 0;">Bo'lim (영역)</th>
      <th style="padding:10px;text-align:center;">Savollar</th>
      <th style="padding:10px;text-align:center;">Vaqt</th>
      <th style="padding:10px;text-align:center;border-radius:0 8px 0 0;">Max ball</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px;">🎧 듣기 — Tinglash</td>
      <td style="padding:10px;text-align:center;">50 ta</td>
      <td style="padding:10px;text-align:center;">60 daq.</td>
      <td style="padding:10px;text-align:center;"><strong>100</strong></td>
    </tr>
    <tr>
      <td style="padding:10px;">✍️ 쓰기 — Yozish</td>
      <td style="padding:10px;text-align:center;">4 ta</td>
      <td style="padding:10px;text-align:center;">50 daq.</td>
      <td style="padding:10px;text-align:center;"><strong>100</strong></td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px;">📖 읽기 — O'qish</td>
      <td style="padding:10px;text-align:center;">50 ta</td>
      <td style="padding:10px;text-align:center;">70 daq.</td>
      <td style="padding:10px;text-align:center;"><strong>100</strong></td>
    </tr>
    <tr style="background:#dbeafe;font-weight:700;">
      <td style="padding:10px;border-radius:0 0 0 8px;">JAMI (총점)</td>
      <td style="padding:10px;text-align:center;">104 ta</td>
      <td style="padding:10px;text-align:center;">180 daq.</td>
      <td style="padding:10px;text-align:center;border-radius:0 0 8px 0;">300</td>
    </tr>
  </tbody>
</table>

<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>📝 Muhim nuqta:</strong> 듣기 va 읽기'da har bir savol <mark style="background:#f3e8ff;">2 ball</mark>
  (50 × 2 = 100). 쓰기'da esa 4 savol turli ballga ega — buni keyingi darsda batafsil ko'ramiz.
</div>
""",
            },
            # ── 6. Darajalar (급) ──────────────────────────────────────
            {
                "rich_text": """
<h3>Darajalar (급) — qaysi ball qaysi darajani beradi</h3>
<p>TOPIK II'da alohida "o'tdi/yiqildi" yo'q — <strong>umumiy ballingizga qarab</strong> daraja
beriladi. TOPIK II <mark>3급 dan 6급 gacha</mark> darajalarni qamraydi:</p>

<table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:0.97em;">
  <thead>
    <tr style="background:#10b981;color:#fff;">
      <th style="padding:10px;text-align:left;border-radius:8px 0 0 0;">Daraja (급)</th>
      <th style="padding:10px;text-align:center;">Umumiy ball (300 dan)</th>
      <th style="padding:10px;text-align:left;border-radius:0 8px 0 0;">Nimani bildiradi</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#f8fafc;">
      <td style="padding:10px;"><strong>3급</strong> (3-daraja)</td>
      <td style="padding:10px;text-align:center;"><mark>120 – 149</mark></td>
      <td style="padding:10px;">Kundalik va ijtimoiy vaziyatlarda erkin muloqot.</td>
    </tr>
    <tr>
      <td style="padding:10px;"><strong>4급</strong> (4-daraja)</td>
      <td style="padding:10px;text-align:center;"><mark>150 – 189</mark></td>
      <td style="padding:10px;">Ish va rasmiy mavzularda muloqot; ko'p universitet talabi.</td>
    </tr>
    <tr style="background:#f8fafc;">
      <td style="padding:10px;"><strong>5급</strong> (5-daraja)</td>
      <td style="padding:10px;text-align:center;"><mark style="background:#dcfce7;">190 – 229</mark></td>
      <td style="padding:10px;">Kasbiy va ilmiy sohalarda ravon foydalanish.</td>
    </tr>
    <tr>
      <td style="padding:10px;"><strong>6급</strong> (6-daraja)</td>
      <td style="padding:10px;text-align:center;"><mark style="background:#dcfce7;">230 – 300</mark></td>
      <td style="padding:10px;">Deyarli ona tili darajasida — eng yuqori daraja.</td>
    </tr>
    <tr style="background:#fee2e2;">
      <td style="padding:10px;border-radius:0 0 0 8px;">daraja yo'q (불합격)</td>
      <td style="padding:10px;text-align:center;">0 – 119</td>
      <td style="padding:10px;border-radius:0 0 8px 0;">120 balldan past — daraja berilmaydi.</td>
    </tr>
  </tbody>
</table>

<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>💡 Maslahat:</strong> Ballar <u>umumiy</u> hisoblanadi. Ya'ni bir bo'limda past ball
  olsangiz ham, boshqasida yuqori ball bilan qoplashingiz mumkin. Shu bois <mark>kuchli
  bo'limingizdan maksimal ball</mark> yig'ish strategiyasi juda foydali.
</div>
""",
            },
            # ── 7. Imtihon kuni ────────────────────────────────────────
            {
                "rich_text": """
<h3>Imtihon kuni — nimani kutish kerak</h3>
<ul>
  <li>Javoblar <strong>OMR varaqasiga</strong> (컴퓨터용 사인펜 — maxsus qalam) belgilanadi;
      test bo'limlarida faqat <mark style="background:#dbeafe;">①②③④</mark> variantlaridan birini
      to'ldirasiz.</li>
  <li>쓰기 javoblari <strong>qo'lda</strong>, ajratilgan katakli maydonga yoziladi
      (원고지 형식 — har bir belgi bitta katakka).</li>
  <li>Shaxsni tasdiqlovchi hujjat (수험표 + passport/ID) va ruxsat etilgan qalam bilan boring.</li>
  <li>듣기 audiosi <strong>bir marta</strong> yangraydi — qayta eshittirilmaydi.</li>
  <li>Har bir sessiya oxirida javob varaqasi yig'ib olinadi; vaqt tugagach yozishga ruxsat yo'q.</li>
</ul>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>⚠️ Diqqat:</strong> Belgilashni <mark style="background:#fee2e2;">variant raqami bilan
  adashtirmang</mark> — savol raqami va javob katagini har doim solishtiring. Bitta siljish
  keyingi barcha javoblarni buzadi.
</div>
""",
            },
            # ── 8. Kalit so'zlar + Xulosa ──────────────────────────────
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>한국어능력시험</strong> — Koreys tili qobiliyati imtihoni (TOPIK)</li>
  <li><strong>영역</strong> — bo'lim (tinglash/yozish/o'qish)</li>
  <li><strong>듣기</strong> — tinglash · <strong>쓰기</strong> — yozish · <strong>읽기</strong> — o'qish</li>
  <li><strong>교시</strong> — sessiya (imtihon bosqichi)</li>
  <li><strong>총점</strong> — umumiy ball · <strong>급</strong> — daraja</li>
  <li><strong>합격 / 불합격</strong> — o'tdi / o'tmadi</li>
  <li><strong>수험표</strong> — imtihon ruxsatnomasi</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>TOPIK II uch bo'lim: <strong>듣기 (50) + 쓰기 (4) + 읽기 (50)</strong>.</li>
    <li>Vaqt: 1교시 = 듣기 60 + 쓰기 50 daq.; 2교시 = 읽기 70 daq.</li>
    <li>Ball: har bo'lim 100, jami <strong>300</strong>.</li>
    <li>Daraja: 120→3급, 150→4급, 190→5급, 230→6급.</li>
    <li>Ball <u>umumiy</u> — kuchli bo'lim zaifni qoplaydi.</li>
  </ul>
</div>
""",
            },
            # ── 9-10. Amaliyot ─────────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 1.</strong> TOPIK II qaysi darajalarni beradi?</p>",
                "choices": [
                    {"text": "1급 dan 2급 gacha", "is_correct": False},
                    {"text": "3급 dan 6급 gacha", "is_correct": True},
                    {"text": "1급 dan 6급 gacha", "is_correct": False},
                    {"text": "Faqat 6급", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>3급 dan 6급 gacha</strong>. 1–2급 ni TOPIK I "
                               "beradi. TOPIK II'da 120 balldan boshlab daraja beriladi: "
                               "120→3급, 150→4급, 190→5급, 230→6급.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> TOPIK II ning umumiy maksimal balli "
                             "(총점) qancha?</p>",
                "choices": [
                    {"text": "100 ball", "is_correct": False},
                    {"text": "200 ball", "is_correct": False},
                    {"text": "300 ball", "is_correct": True},
                    {"text": "400 ball", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>300 ball</strong>. Uch bo'lim (듣기·쓰기·읽기), "
                               "har biri 100 balldan: 100 × 3 = <strong>300</strong>.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 3.</strong> Birinchi sessiyada (1교시) qaysi "
                             "bo'limlar topshiriladi?</p>",
                "choices": [
                    {"text": "듣기 va 읽기 (tinglash va o'qish)", "is_correct": False},
                    {"text": "듣기 va 쓰기 (tinglash va yozish)", "is_correct": True},
                    {"text": "faqat 읽기 (o'qish)", "is_correct": False},
                    {"text": "쓰기 va 읽기 (yozish va o'qish)", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>듣기 va 쓰기</strong>. 1교시: 듣기 (60 daq.) + "
                               "쓰기 (50 daq.) = 110 daq. 읽기 esa alohida 2교시da (70 daq.) topshiriladi.</p>",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════════
    # QISM 2 — Savol turlari batafsil
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "strategy",
        "title":   "TOPIK II — Kirish (2-qism): Har bo'limning savol turlari",
        "summary": "듣기, 읽기 va 쓰기 bo'limlarida qanday savol turlari uchraydi, har biri "
                   "necha ball va nimaga e'tibor berish kerak — batafsil yo'riqnoma.",
        "order":   2,
        "blocks": [
            # ── 1. Kirish ──────────────────────────────────────────────
            {
                "rich_text": """
<h2>TOPIK II — Umumiy kirish (2-qism)</h2>
<p>
  <span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">savol turlari</span>&nbsp;
  <span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">nimani kutish</span>
</p>
<p>1-qismda imtihon <strong>tuzilishi va ballari</strong> bilan tanishdik. Endi har bir bo'limda
<mark>aynan qanday savollar</mark> uchrashini va ularga qanday yondashishni ko'ramiz.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>📌 Umumiy qoida:</strong> Har bir bo'limda savollar <mark style="background:#dbeafe;">osondan
  qiyinga</mark> qarab boradi. Boshidagi savollarni tez va aniq yeching — oxiridagi qiyin
  savollarga vaqt qoladi.
</div>
""",
            },
            # ── 2. 듣기 (Listening) ─────────────────────────────────────
            {
                "rich_text": """
<h3>🎧 듣기 (Tinglash) — 50 savol · 100 ball</h3>
<p>Ovozli yozuv <strong>bir marta</strong> yangraydi. Savollar qisqa dialoglardan boshlanib,
uzun ma'ruza va suhbatlarga qarab murakkablashadi. Asosiy savol turlari:</p>
<ul>
  <li><strong>Mos rasmni tanlash</strong> — dialogga to'g'ri keladigan rasm/grafik.</li>
  <li><strong>Keyingi gapni tanlash</strong> — suhbat qanday davom etishini topish.</li>
  <li><strong>Mazmunga mos javob</strong> — eshitilganga mos keladigan gapni tanlash (일치하는 내용).</li>
  <li><strong>Markaziy fikr / maqsad</strong> — so'zlovchining asosiy fikri yoki niyati (중심 생각).</li>
  <li><strong>Uzun matn (2 savol)</strong> — bitta ma'ruza/suhbatga oid ikkita savol birga.</li>
</ul>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>들은 내용과 같은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Eshitilgan mazmunga mos kelganini tanlang.</em></p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>💡 Maslahat:</strong> Audio boshlanishidan oldin <mark>variantlarni tez o'qib qo'ying</mark> —
  nimani tinglash kerakligini oldindan bilib olasiz. Podkast tinglash bu bo'limga eng yaxshi mashq.
</div>
""",
            },
            # ── 3. 읽기 (Reading) ───────────────────────────────────────
            {
                "rich_text": """
<h3>📖 읽기 (O'qish) — 50 savol · 100 ball</h3>
<p>Qisqa e'lon va reklamalardan boshlanib, uzun maqola va ilmiy matnlarga qarab boradi. Savol turlari:</p>
<ul>
  <li><strong>Bo'sh joyni to'ldirish</strong> — mos grammatika yoki so'zni tanlash (빈칸 채우기).</li>
  <li><strong>Mavzu / maqsadni topish</strong> — e'lon, reklama nima haqida ekanini aniqlash.</li>
  <li><strong>Gaplar tartibini tiklash</strong> — aralashtirilgan jumlalarni to'g'ri ketma-ketlikka qo'yish.</li>
  <li><strong>Mos/mos emas</strong> — matn mazmuniga mos keladigan gapni tanlash.</li>
  <li><strong>Gapni joyiga qo'yish</strong> — berilgan jumla matnning qaysi joyiga tushishini topish.</li>
  <li><strong>Asosiy fikr / munosabat</strong> — muallifning fikri yoki matn mavzusi.</li>
</ul>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>다음 글의 주제로 알맞은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi matnning mavzusi sifatida mosini tanlang.</em></p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>📌 Eslatma:</strong> 읽기'da vaqt tig'iz (50 savol, 70 daqiqa). Har bir so'zni tarjima
  qilib o'tirmang — <mark style="background:#dbeafe;">ko'z bilan tez tushunish</mark> mashqini
  qiling. Sifat (형용사), ravish (부사) va fe'l (동사) ni yaxshi bilish javobni hal qiladi.
</div>
""",
            },
            # ── 4. 쓰기 (Writing) — batafsil ────────────────────────────
            {
                "rich_text": """
<h3>✍️ 쓰기 (Yozish) — 4 savol · 100 ball</h3>
<p>Bu — eng ko'p tayyorgarlik talab qiladigan bo'lim. Faqat 4 savol, lekin ballari katta va
turlicha. Har birini yaxshi bilib oling:</p>

<table style="width:100%;border-collapse:collapse;margin:12px 0;font-size:0.96em;">
  <thead>
    <tr style="background:#a855f7;color:#fff;">
      <th style="padding:10px;text-align:center;border-radius:8px 0 0 0;">Savol</th>
      <th style="padding:10px;text-align:left;">Nima qilinadi</th>
      <th style="padding:10px;text-align:center;border-radius:0 8px 0 0;">Ball</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#faf5ff;">
      <td style="padding:10px;text-align:center;"><strong>51</strong></td>
      <td style="padding:10px;">Amaliy matn (e'lon, xabar, xat) ichida <strong>2 ta bo'sh joyga</strong> mos jumla yozish.</td>
      <td style="padding:10px;text-align:center;"><mark>10</mark></td>
    </tr>
    <tr>
      <td style="padding:10px;text-align:center;"><strong>52</strong></td>
      <td style="padding:10px;">Tushuntiruvchi matn ichida <strong>2 ta bo'sh joyga</strong> mantiqan mos jumla yozish.</td>
      <td style="padding:10px;text-align:center;"><mark>10</mark></td>
    </tr>
    <tr style="background:#faf5ff;">
      <td style="padding:10px;text-align:center;"><strong>53</strong></td>
      <td style="padding:10px;"><strong>Grafik/jadval tavsifi</strong> — berilgan ma'lumotni 200–300 belgida tasvirlash.</td>
      <td style="padding:10px;text-align:center;"><mark style="background:#dcfce7;">30</mark></td>
    </tr>
    <tr>
      <td style="padding:10px;text-align:center;"><strong>54</strong></td>
      <td style="padding:10px;"><strong>Insho</strong> — mavzu bo'yicha 600–700 belgilik dalilli matn yozish.</td>
      <td style="padding:10px;text-align:center;"><mark style="background:#dcfce7;">50</mark></td>
    </tr>
    <tr style="background:#f3e8ff;font-weight:700;">
      <td style="padding:10px;text-align:center;border-radius:0 0 0 8px;">JAMI</td>
      <td style="padding:10px;">4 savol</td>
      <td style="padding:10px;text-align:center;border-radius:0 0 8px 0;">100</td>
    </tr>
  </tbody>
</table>

<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>⚠️ Diqqat:</strong> <mark style="background:#fee2e2;">54-savol (insho) 50 ball</mark> —
  butun 쓰기 bo'limining yarmi! Uni tashlab ketmang. 53 va 54 birgalikda 80 ball beradi, shuning
  uchun 쓰기 mashqi asosan shu ikkisiga qaratilishi kerak.
</div>

<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>📝 Baholash mezoni (54):</strong> insho <u>mazmuni</u> (mavzuga mosligi), <u>tuzilishi</u>
  (서론·본론·결론 — kirish, asosiy qism, xulosa) va <u>tili</u> (grammatika, so'z boyligi,
  rasmiy uslub — 격식체) bo'yicha baholanadi.
</div>
""",
            },
            # ── 5. Qiyinlik oshadi + strategiya ────────────────────────
            {
                "rich_text": """
<h3>Umumiy manzara — nimaga e'tibor berish kerak</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 220px;background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 14px;border-radius:8px;">
    <strong>🎧 듣기</strong><br><span style="color:#475569;">Audio bir marta. Oldindan
    variantlarni o'qing. Podkast bilan mashq qiling.</span>
  </div>
  <div style="flex:1 1 220px;background:#ecfdf5;border-left:4px solid #10b981;padding:12px 14px;border-radius:8px;">
    <strong>📖 읽기</strong><br><span style="color:#475569;">Vaqt tig'iz. Tez o'qing,
    tarjima qilmang. So'z boyligi hal qiladi.</span>
  </div>
  <div style="flex:1 1 220px;background:#faf5ff;border-left:4px solid #a855f7;padding:12px 14px;border-radius:8px;">
    <strong>✍️ 쓰기</strong><br><span style="color:#475569;">53 + 54 = 80 ball. Tayyor jumla va
    shablonlar bilan mashq qiling.</span>
  </div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:14px 0;">
  <strong>💡 Maslahat:</strong> Har bir bo'lim <mark>osondan qiyinga</mark> boradi. Oldingi
  osson savollarni <strong>ishonchli</strong> yeching — ular ham qiyin savol kabi 2 ball beradi.
  Qiyin savolda tiqilib qolib, oson ballarni yo'qotmang.
</div>
""",
            },
            # ── 6. Kalit so'zlar + Xulosa ──────────────────────────────
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>문제 유형</strong> — savol turi</li>
  <li><strong>빈칸 채우기</strong> — bo'sh joyni to'ldirish</li>
  <li><strong>중심 생각</strong> — markaziy fikr</li>
  <li><strong>주제</strong> — mavzu · <strong>일치하는 내용</strong> — mos keluvchi mazmun</li>
  <li><strong>도표 / 그래프</strong> — jadval / grafik</li>
  <li><strong>서론 · 본론 · 결론</strong> — kirish · asosiy qism · xulosa</li>
  <li><strong>격식체</strong> — rasmiy yozma uslub</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>듣기 (50) va 읽기 (50) — test; osondan qiyinga boradi.</li>
    <li>쓰기 — 51/52 (10+10), 53 (30), <strong>54 (50)</strong>. Insho eng katta ball.</li>
    <li>53 + 54 = 80 ball → 쓰기 mashqi asosan shu ikkisiga.</li>
    <li>Oldindan variantlarni o'qish (듣기) va tez o'qish (읽기) — kalit odatlar.</li>
  </ul>
</div>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>➡️ Keyingi qadam:</strong> Endi imtihonni tushundingiz. Har bir bo'lim bo'yicha
  batafsil darslar (듣기, 읽기, 쓰기 va 전략) shu kursda davom etadi — o'zingizga eng zarur
  bo'limdan boshlang.
</div>
""",
            },
            # ── 7-8. Amaliyot ──────────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 1.</strong> 쓰기 bo'limida qaysi savol eng ko'p "
                             "ball beradi?</p>",
                "choices": [
                    {"text": "51-savol (10 ball)", "is_correct": False},
                    {"text": "52-savol (10 ball)", "is_correct": False},
                    {"text": "53-savol (30 ball)", "is_correct": False},
                    {"text": "54-savol (50 ball)", "is_correct": True},
                ],
                "explanation": "<p>To'g'ri javob — <strong>54-savol (insho), 50 ball</strong>. Bu butun "
                               "쓰기 bo'limining yarmi. 53 (30) bilan birga 80 ball beradi, shuning "
                               "uchun 쓰기 tayyorgarligi asosan 53 va 54 ga qaratilishi kerak.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> 듣기 audiosi haqida qaysi gap to'g'ri?</p>",
                "choices": [
                    {"text": "Ikki marta yangraydi.", "is_correct": False},
                    {"text": "Faqat bir marta yangraydi.", "is_correct": True},
                    {"text": "Xohlagancha qayta eshitish mumkin.", "is_correct": False},
                    {"text": "Matn ko'rinishida ham beriladi.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>bir marta yangraydi</strong>. Shuning uchun "
                               "audio boshlanishidan oldin variantlarni tez o'qib, nimani tinglash "
                               "kerakligini bilib olish muhim.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 3.</strong> 53-savolda nima qilinadi?</p>",
                "choices": [
                    {"text": "600–700 belgilik insho yoziladi.", "is_correct": False},
                    {"text": "Bo'sh joyga bitta jumla yoziladi.", "is_correct": False},
                    {"text": "Grafik/jadval ma'lumoti 200–300 belgida tasvirlanadi.", "is_correct": True},
                    {"text": "Audio tinglab javob beriladi.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>grafik/jadval tavsifi (200–300 belgi), 30 ball</strong>. "
                               "600–700 belgilik insho esa 54-savol. 51/52 — bo'sh joyga jumla yozish.</p>",
            },
        ],
    },
]
