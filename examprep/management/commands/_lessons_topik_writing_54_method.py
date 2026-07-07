# TOPIK Writing 54 — "jumla yodlash" metodi (foydalanuvchining maslahati asosida).
# Til: Oʻzbekcha + Koreyscha. Rangli styling bilan. STYLE_GUIDE_TOPIK.md ga qarang.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_writing_54_method.py --author=prime
# (mavjudini yangilash uchun --republish qoʻshing).

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

LESSONS = [
    {
        "skill":   "writing",
        "title":   "TOPIK Writing 54: Jumla yodlash metodi (54-savol)",
        "summary": "54-savol uchun maxsus mavzular bo'yicha tayyor jumlalarni yodlash metodi "
                   "va 서론·본론·결론 uchun ko'plab koreyscha namunalar.",
        "order":   30,
        "blocks": [
            # ── 1. Kirish ────────────────────────────────────────────────
            {
                "rich_text": """
<h2>TOPIK Writing 54: Jumla yodlash metodi</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">쓰기 54</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">600–700 belgi</span></p>
<p>54-savol — bu <strong>uzun insho</strong> (600–700 belgi). Ko'pchilik bu yerda vaqt
yetmay qoladi yoki nima yozishni bilmaydi. Bu darsda <mark>tayyor jumlalarni yodlash</mark>
metodini o'rganamiz — bu eng tez va eng ishonchli yo'l.</p>
""",
            },
            # ── 2. Metod ─────────────────────────────────────────────────
            {
                "rich_text": """
<h3>Metodning mohiyati</h3>
<p><mark style="background:#fee2e2;">Yakka so'zni</mark> to'g'ri ishlatish qiyin.
<mark style="background:#fee2e2;">Butun namunaviy javobni</mark> yodlash ham qiyin — esda
qolmaydi. Shuning uchun <strong>o'rtasini tanlaymiz</strong>:
<mark style="background:#dcfce7;">maxsus mavzular bo'yicha jumlalarni</mark> yodlaymiz.</p>

<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Mashq qilish tartibi:</strong>
  <ol style="margin:8px 0 0;">
    <li>Har bir jumlani <strong>kuniga 3 marta</strong> yozing.</li>
    <li>Buni <strong>3 kun davomida</strong> takrorlang.</li>
    <li><strong>Kuniga atigi 3 ta jumla</strong> o'rganish kifoya.</li>
  </ol>
  <p style="margin:8px 0 0;">Shunday qilib jumla <strong>tabiiy ravishda</strong> esda
  qoladi va imtihonda o'zingiz bilmagan holda ishlata olasiz.</p>
</div>
""",
            },
            # ── 3. Nega? (3 foyda) ───────────────────────────────────────
            {
                "rich_text": """
<h3>Nega bu metod ishlaydi? — 3 ta foyda</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 220px;background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 14px;border-radius:8px;">
    <strong>1️⃣ Xatosiz</strong><br>
    Tayyor jumlada <mark style="background:#dcfce7;">grammatik yoki mantiqiy xato bo'lmaydi.</mark>
  </div>
  <div style="flex:1 1 220px;background:#faf5ff;border-left:4px solid #a855f7;padding:12px 14px;border-radius:8px;">
    <strong>2️⃣ Oson esda qoladi</strong><br>
    Jumla — yaxlit ma'noga ega, shuning uchun <strong>so'zga qaraganda</strong> oson yodlanadi.
  </div>
  <div style="flex:1 1 220px;background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 14px;border-radius:8px;">
    <strong>3️⃣ Vaqt tejaydi</strong><br>
    1–2 ta tayyor fikr bo'lsa, atrofini to'ldirib <strong>vaqtida tugatasiz.</strong>
  </div>
</div>
<p>Aks holda inshoning har bir qismi uchun fikr o'ylash juda <strong>ko'p vaqt</strong>
oladi va imtihonda shoshilib qolasiz.</p>
""",
            },
            # ── 4. Jumlalarni qayerdan olish ─────────────────────────────
            {
                "rich_text": """
<h3>Jumlalarni qayerdan o'rganish kerak?</h3>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Muhim:</strong> Jumlalarni <strong>kitob o'qib</strong> o'rganish eng yaxshisi —
  eski TOPIK javoblaridan shunchaki <mark style="background:#fee2e2;">ko'chirib olmang.</mark>
  Kitobdan olingan jumlalar tabiiy, to'g'ri va xilma-xil bo'ladi.
</div>
<p>Quyida turli mavzularda ishlatsa bo'ladigan <strong>ko'plab tayyor jumlalar</strong>
berilgan. Ularni 서론 (kirish), 본론 (asosiy qism) va 결론 (xulosa) bo'yicha guruhladik.</p>
""",
            },
            # ── 5. 서론 jumlalari (dropdown) ─────────────────────────────
            {
                "rich_text": """
<h3>📂 Tayyor jumlalar</h3>
<details open style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">서론 — Kirish jumlalari (bosing)</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>현대 사회에서 ~은/는 점점 더 중요해지고 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Zamonaviy jamiyatda ~ tobora muhimroq bo'lib bormoqda.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>최근 ~에 대한 사람들의 관심이 높아지고 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>So'nggi paytlarda odamlarning ~ ga qiziqishi ortib bormoqda.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>~은/는 우리 생활과 밀접한 관계가 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>~ bizning hayotimiz bilan uzviy bog'liq.</em></p>
    </div>
  </div>
</details>

<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">본론 — Asosiy qism jumlalari (bosing)</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>첫째, ~. 둘째, ~. 셋째, ~.</strong></p>
      <p style="color:#475569;margin:0;"><em>Birinchidan ~. Ikkinchidan ~. Uchinchidan ~.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>그 이유는 다음과 같다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Buning sabablari quyidagicha.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>예를 들어, ~을/를 들 수 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Masalan, ~ ni misol qilib keltirish mumkin.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>뿐만 아니라 ~. 반면에 ~.</strong></p>
      <p style="color:#475569;margin:0;"><em>Bundan tashqari ~. Aksincha esa ~.</em></p>
    </div>
  </div>
</details>

<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">결론 — Xulosa jumlalari (bosing)</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>이상에서 살펴본 바와 같이 ~.</strong></p>
      <p style="color:#475569;margin:0;"><em>Yuqorida ko'rib chiqilganidek ~.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>따라서 앞으로 ~아야/어야 할 것이다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Shuning uchun kelajakda ~ kerak bo'ladi.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
      <p style="font-size:1.12em;margin:0 0 6px;"><strong>결론적으로, ~이/가 가장 중요하다고 할 수 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Xulosa qilib aytganda, ~ eng muhim deyish mumkin.</em></p>
    </div>
  </div>
</details>
""",
            },
            # ── 6. Mavzu bo'yicha jumlalar ───────────────────────────────
            {
                "rich_text": """
<h3>Mavzu bo'yicha namunalar (주제별)</h3>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 환경 (Atrof-muhit):</strong>
  <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:10px 0 0;">
    <p style="margin:0 0 6px;"><strong>환경 오염은 우리가 시급히 해결해야 할 문제이다.</strong></p>
    <p style="color:#475569;margin:0;"><em>Atrof-muhit ifloslanishi — biz zudlik bilan hal qilishimiz kerak bo'lgan muammo.</em></p>
  </div>
</div>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 교육 (Ta'lim):</strong>
  <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:10px 0 0;">
    <p style="margin:0 0 6px;"><strong>교육은 개인뿐만 아니라 사회 발전에도 중요한 역할을 한다.</strong></p>
    <p style="color:#475569;margin:0;"><em>Ta'lim nafaqat shaxs, balki jamiyat taraqqiyotida ham muhim rol o'ynaydi.</em></p>
  </div>
</div>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 과학 기술 (Fan-texnika):</strong>
  <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:10px 0 0;">
    <p style="margin:0 0 6px;"><strong>과학 기술의 발전은 우리의 삶을 편리하게 만들었다.</strong></p>
    <p style="color:#475569;margin:0;"><em>Fan-texnika rivoji hayotimizni qulay qildi.</em></p>
  </div>
</div>
""",
            },
            # ── 7. Yodlangan jumladan tayyor abzasgacha (step-reveal) ────
            {
                "rich_text": """
<h3>Yodlangan jumladan tayyor abzasgacha</h3>
<p>Bitta yodlangan jumla imtihonda qanday qilib butun <strong>본론</strong> abzasiga
aylanadi? Har qadamni birma-bir ochib, abzas qanday o'sishini ko'ring:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — yodlangan jumla</strong> (tayanch fikr, tayyor va xatosiz):</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>환경 오염은 우리가 시급히 해결해야 할 문제이다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Atrof-muhit ifloslanishi — biz zudlik bilan hal
      qilishimiz kerak bo'lgan muammo.</em></p>
    </div>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — sabab qo'shamiz</strong> (<mark style="background:#dbeafe;">-기 때문이다</mark>):</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>오염된 환경은 우리의 건강에 직접적인 영향을 미치기 때문이다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Chunki ifloslangan muhit sog'lig'imizga bevosita
      ta'sir qiladi.</em></p>
    </div>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — misol qo'shamiz</strong> (<mark style="background:#dcfce7;">예를 들어</mark> — masalan):</p>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>예를 들어, 미세먼지가 심한 날에는 호흡기 질환 환자가 늘어난다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Masalan, chang (mayda zarra) kuchli kunlarda nafas
      yo'llari kasalliklari bilan og'riganlar ko'payadi.</em></p>
    </div>
  </div>
  <div class="pp-step">
    <p><strong>Tayyor abzas</strong> — uch gap birga:</p>
    <div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:8px 0 0;">
      <p style="margin:0 0 4px;"><strong>환경 오염은 우리가 시급히 해결해야 할 문제이다. 오염된 환경은
      우리의 건강에 직접적인 영향을 미치기 때문이다. 예를 들어, 미세먼지가 심한 날에는 호흡기 질환
      환자가 늘어난다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Atrof-muhit ifloslanishi — zudlik bilan hal qilinishi
      kerak bo'lgan muammo. Chunki ifloslangan muhit sog'lig'imizga bevosita ta'sir qiladi.
      Masalan, chang kuchli kunlarda nafas yo'llari kasalliklari bilan og'riganlar ko'payadi.</em></p>
    </div>
  </div>
</div>
<p>Formula: <mark>1 yodlangan jumla</mark> + <mark style="background:#dbeafe;">1 sabab
(-기 때문이다)</mark> + <mark style="background:#dcfce7;">1 misol (예를 들어)</mark> = tayyor abzas.</p>
""",
            },
            # ── 8. Amaliyot savoli 1 ─────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 1.</strong> Metodga ko'ra, har kuni nechta "
                             "yangi jumla o'rganish kifoya?</p>",
                "choices": [
                    {"text": "1 ta", "is_correct": False},
                    {"text": "3 ta", "is_correct": True},
                    {"text": "5 ta", "is_correct": False},
                    {"text": "10 ta", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>3 ta</strong>. Kuniga 3 ta jumla, "
                               "har birini kuniga 3 marta, 3 kun davomida yozish kifoya. Bu "
                               "miqdor esda saqlash uchun ayni muvozanat.</p>",
            },
            # ── 9. Amaliyot savoli 2 ─────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> Quyidagilardan qaysi biri "
                             "<strong>결론</strong> (xulosa) jumlasi?</p>",
                "choices": [
                    {"text": "현대 사회에서 환경 문제가 중요해지고 있다.", "is_correct": False},
                    {"text": "그 이유는 다음과 같다.", "is_correct": False},
                    {"text": "이상에서 살펴본 바와 같이, 노력이 필요하다.", "is_correct": True},
                    {"text": "예를 들어, 재활용을 들 수 있다.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>“이상에서 살펴본 바와 같이…”</strong> "
                               "(Yuqorida ko'rib chiqilganidek…). Bu ibora insho oxirida, "
                               "xulosa qismida ishlatiladi. Qolganlari 서론 yoki 본론 jumlalaridir.</p>",
            },
            # ── 10. Kalit so'zlar (flashcards) + Xulosa ──────────────────
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<p class="text-secondary small">Kartani bosib ag'daring — koreyscha so'zni ko'rib, ma'nosini eslang.</p>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">서론</div><div class="pp-card-back">kirish</div></div>
  <div class="pp-card"><div class="pp-card-front">본론</div><div class="pp-card-back">asosiy qism</div></div>
  <div class="pp-card"><div class="pp-card-front">결론</div><div class="pp-card-back">xulosa</div></div>
  <div class="pp-card"><div class="pp-card-front">따라서</div><div class="pp-card-back">shuning uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">반면에</div><div class="pp-card-back">aksincha</div></div>
  <div class="pp-card"><div class="pp-card-front">예를 들어</div><div class="pp-card-back">masalan</div></div>
  <div class="pp-card"><div class="pp-card-front">점점 더</div><div class="pp-card-back">tobora ko'proq</div></div>
  <div class="pp-card"><div class="pp-card-front">중요하다</div><div class="pp-card-back">muhim bo'lmoq</div></div>
</div>

<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>So'z emas, namunaviy javob ham emas — <strong>jumlalarni</strong> yodlang.</li>
    <li>Har jumlani kuniga 3 marta, 3 kun; kuniga 3 ta jumla.</li>
    <li>Jumlalarni <strong>kitobdan</strong> oling, eski javoblardan ko'chirmang.</li>
    <li>서론·본론·결론 uchun tayyor jumlalar — xatosiz, oson, tez.</li>
  </ul>
</div>
""",
            },
        ],
    },
]
