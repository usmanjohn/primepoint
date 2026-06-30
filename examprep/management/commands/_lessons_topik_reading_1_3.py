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
<p>Oddiy nazorat nuqtalari sizni xavfsiz saqlaydi: 20-daqiqada ~20-savol atrofida,
45-daqiqada ~35-savol atrofida bo'ling.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Agar orqada qolsangiz — <strong>taxmin qiling va keyingisiga
  o'ting.</strong> Bo'sh qoldirilgan javob ham, xato javob ham bir xil — lekin bo'sh javob
  hech qachon to'g'ri bo'lolmaydi.
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>읽기</strong> — o'qish</li>
  <li><strong>지문</strong> — matn / parcha</li>
  <li><strong>문제</strong> — savol</li>
  <li><strong>정답</strong> — to'g'ri javob</li>
  <li><strong>시간 배분</strong> — vaqtni taqsimlash</li>
  <li><strong>추측하다</strong> — taxmin qilmoq</li>
</ul>
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
<h3>Ishlangan namuna</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">요즘 사람들은 시간이 없다는 이유로 아침을 거르는 경우가 많다.
  그러나 아침 식사는 하루의 활동에 필요한 에너지를 준다.
  <strong>따라서 바쁘더라도 아침을 꼭 먹는 것이 좋다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Hozir odamlar vaqt yo'qligi sababli ko'pincha
  nonushtani o'tkazib yuboradi. Lekin nonushta kun davomidagi faoliyat uchun energiya beradi.
  Shuning uchun band bo'lsa ham, nonushta qilish yaxshi.</em></p>
</div>
<p>Tez o'qing: birinchi gap odatni aytadi (nonushtani tashlash), o'rtasi sabab beradi,
oxirgi gap esa — <strong>따라서</strong> bilan — asosiy fikrni beradi:
<mark style="background:#dcfce7;">band bo'lsa ham nonushta qilish kerak.</mark></p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Tez-tez uchraydigan xato:</strong> o'rtadagi <em>to'g'ri lekin asosiy bo'lmagan</em>
  tafsilotga aldanmang. Variant <strong>to'g'ri bo'lishi mumkin, ammo asosiy fikr emas.</strong>
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>중심 생각</strong> — asosiy fikr</li>
  <li><strong>훑어 읽기</strong> — tez ko'zdan kechirib o'qish</li>
  <li><strong>따라서</strong> — shuning uchun</li>
  <li><strong>그러나</strong> — lekin</li>
  <li><strong>세부 내용</strong> — tafsilot</li>
  <li><strong>아침 식사</strong> — nonushta</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Har so'zni tarjima qilmang — asosiy fikr uchun tez o'qing.</li>
    <li>Fikr odatda birinchi yoki oxirgi gapda.</li>
    <li>To'g'ri tafsilot har doim ham asosiy fikr emas.</li>
  </ul>
</div>
""",
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
<h3>Odatning namunasi</h3>
<p>Aytaylik, savol “이 글의 내용과 같은 것을 고르십시오” (matnga mos kelganini tanlang) va
variantlardan birida <strong>할인 (chegirma)</strong> bor. Butun e'lonni o'qishdan oldin
siz allaqachon <mark style="background:#dbeafe;">chegirma haqidagi gapni</mark> qidirishni
bilasiz. Topasiz, variant bilan solishtirasiz va javob berasiz — qolganini qayta o'qimasdan.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Variantlarni oldin o'qish — faqat ulardan taxmin qilish
  degani <strong>emas</strong>. Variantlar — sizning <strong>qidiruv ro'yxatingiz</strong>,
  lekin javobni baribir matndan <mark style="background:#dcfce7;">tasdiqlang.</mark>
  TOPIK <em>deyarli</em> to'g'ri variantlarni yaxshi ko'radi.
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>일치하는 내용</strong> — mos keladigan mazmun</li>
  <li><strong>빈칸</strong> — bo'sh joy</li>
  <li><strong>고르다</strong> — tanlamoq</li>
  <li><strong>핵심어 (kalit so'z)</strong> — kalit so'z</li>
  <li><strong>할인</strong> — chegirma</li>
  <li><strong>확인하다</strong> — tasdiqlamoq</li>
</ul>
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
        ],
    },
]
