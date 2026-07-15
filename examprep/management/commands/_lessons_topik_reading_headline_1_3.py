# TOPIK II Reading — 25–27-savollar: Gazeta sarlavhalari (신문 기사 제목),
# lessons 1–3 (orders 90–92).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_headline_1_3.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "25–27-savollar: Gazeta sarlavhalari (신문 기사 제목)",
    "summary": "Qisqartirilgan sarlavha tilini ochish: metafora, taqlid so'zlar va vergul sirlari.",
    "icon":    "bi-newspaper",
    "order":   11,
}

LESSONS = [
    # ── Lesson 1 (order 90) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 기사 제목 1: 25–27-savollar bilan tanishuv — sarlavha tili",
        "summary": "Gazeta sarlavhasi qanday 'siqiladi' va uni to'liq gapga qanday 'ochish' kerak.",
        "order":   90,
        "blocks": [
            {"rich_text": """
<h2>📰 25–27-savollar: sarlavhani "oching"</h2>
<p>Uchta savol ketma-ket bir xil shaklda keladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi gazeta maqolasi sarlavhasini eng to'g'ri tushuntirgan gapni tanlang.</em></p>
</div>
<p>Sarlavha — joy tejash uchun <strong>ataylab siqilgan</strong> gap. Variantlar esa shu
sarlavhaning to'liq gapga "ochilgan" ko'rinishlari — faqat bittasi to'g'ri ochilgan.
Demak vazifangiz: <mark style="background:#dbeafe;">sarlavhani o'zingiz to'liq gapga
aylantirish</mark>, keyin variantlardan mosini topish.</p>
<h3>Sarlavha qanday siqiladi? 4 qoida</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>1) Qo'shimcha va fe'llar tashlanadi.</strong></p>
  <p style="color:#475569;margin:0;">채소값 급등 = 채소값<u>이</u> 급등<u>했다</u> — <em>sabzavot narxi keskin oshdi</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>2) Vergul (,) — ikki qismni bog'laydi: sabab, natija.</strong></p>
  <p style="color:#475569;margin:0;">채소값 급등<u>,</u> 주부들 한숨 = narx oshdi<u>, shuning uchun</u> uy bekalari xo'rsinmoqda</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>3) Taqlid so'zlar — yo'nalish va kuch:</strong> <mark style="background:#dcfce7;">껑충</mark> (keskin yuqoriga), <mark style="background:#fee2e2;">뚝</mark> (keskin pastga), 활짝 (keng ochilish), 꽁꽁 (qattiq muzlash)</p>
  <p style="color:#475569;margin:0;">항공료 껑충 = aviachipta narxi <em>sakrab</em> oshdi · 관람객 뚝 = tashrif <em>keskin</em> kamaydi</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>4) Metafora — so'zma-so'z o'qilmaydi!</strong></p>
  <p style="color:#475569;margin:0;">수출에 빨간불 = eksportga "qizil chiroq" — ya'ni <em>xavf belgisi</em>, chiroq emas!</p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Noto'g'ri variantlar ikki usulda yasaladi:
  metaforani <strong>so'zma-so'z</strong> o'qish ("chiroq o'rnatildi"?!) yoki yo'nalishni
  <strong>teskari</strong> qilish (oshdi ↔ tushdi). Har variantda shu ikkisini tekshiring.
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>유가 상승에 항공료도 껑충</strong></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — so'zlarni ochamiz:</strong> 유가 (neft narxi) + 상승 (ko'tarilish) +
    -에 (sababida) / 항공료 (aviachipta narxi) + 도 (ham) + 껑충 (sakrab yuqoriga).</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — to'liq gapga aylantiramiz:</strong> "Neft narxi ko'tarilgani
    <em>sababli</em> aviachipta narxi <em>ham keskin oshdi</em>." -에 qo'shimchasi bu yerda
    sabab: "~ ta'sirida".</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — variantlarda tekshiramiz:</strong> yo'nalish (oshdi! tushmadi),
    sabab-natija tartibi (neft → chipta, teskari emas), 도 ("ham" — demak neft narxidan
    keyin chipta ham). Uchtasi ham mos kelgan variant — javob.</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>채소값 급등, 서민들 장바구니 부담 커져</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">급등 — keskin oshish · 서민 — oddiy xalq · 장바구니 — bozor savati</p>
""",
             "choices": [
                 {"text": "채소 가격이 크게 올라서 서민들의 생활비 부담이 늘었다. (Sabzavot narxi ancha oshib, oddiy odamlarning xarajat yuki ortdi.)", "is_correct": True},
                 {"text": "채소 가격이 내려서 서민들이 장을 많이 보고 있다. (Sabzavot narxi tushib, xalq xaridni ko'paytirdi.)", "is_correct": False},
                 {"text": "서민들이 장바구니를 많이 사서 채소값이 올랐다. (Xalq savat ko'p sotib olgani uchun sabzavot narxi oshdi.)", "is_correct": False},
                 {"text": "채소 가게들이 서민들에게 장바구니를 나눠 주었다. (Sabzavot do'konlari xalqqa savat tarqatdi.)", "is_correct": False},
             ],
             "explanation": """
<p>Ochamiz: 채소값 급등 = narx keskin oshdi; vergul = natijasi; 장바구니 부담 =
"bozor savati yuki" — <strong>metafora</strong>: oziq-ovqat xarajati ✅ ①.
② yo'nalish teskari (급등 = oshish!). ③ sabab-natija teskari aylantirilgan.
④ 장바구니 ni so'zma-so'z o'qigan (savat tarqatish?!) — klassik metafora-tuzoq.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>독감 유행, 병원마다 환자들로 북적</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">독감 — gripp · 유행 — tarqalish (epidemiya) · 북적 — gavjum (odam to'lib-toshgan)</p>
""",
             "choices": [
                 {"text": "독감이 퍼지면서 병원을 찾는 환자가 많아졌다. (Gripp tarqalib, shifoxonaga boruvchi bemorlar ko'paydi.)", "is_correct": True},
                 {"text": "독감이 끝나서 병원이 한가해졌다. (Gripp tugab, shifoxonalar bo'shab qoldi.)", "is_correct": False},
                 {"text": "병원이 많아져서 독감 환자가 줄었다. (Shifoxonalar ko'payib, gripp bemorlari kamaydi.)", "is_correct": False},
                 {"text": "환자들이 병원 앞에서 독감 검사를 거부했다. (Bemorlar shifoxona oldida gripp tekshiruvidan bosh tortdi.)", "is_correct": False},
             ],
             "explanation": """
<p>유행 (tarqalyapti) + 북적 (gavjum) → "gripp tarqaldi, natijada shifoxonalar bemorga
to'ldi" ✅ ①. ② ikkala qismni ham teskari qilgan; ③ sabab-natijani buzgan;
④ matnda umuman yo'q voqea to'qigan. 북적 kabi holat-taqlid so'zlar (gavjumlik) —
sarlavhaning "natija" qismida juda ko'p keladi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">제목</div><div class="pp-card-back">sarlavha</div></div>
  <div class="pp-card"><div class="pp-card-front">급등 / 급증</div><div class="pp-card-back">keskin oshish / keskin ko'payish</div></div>
  <div class="pp-card"><div class="pp-card-front">껑충</div><div class="pp-card-back">sakrab (keskin yuqoriga)</div></div>
  <div class="pp-card"><div class="pp-card-front">뚝</div><div class="pp-card-back">taq etib (keskin pastga)</div></div>
  <div class="pp-card"><div class="pp-card-front">북적</div><div class="pp-card-back">gavjum, to'lib-toshgan</div></div>
  <div class="pp-card"><div class="pp-card-front">장바구니 부담</div><div class="pp-card-back">oziq-ovqat xarajati yuki</div></div>
  <div class="pp-card"><div class="pp-card-front">유가</div><div class="pp-card-back">neft narxi</div></div>
  <div class="pp-card"><div class="pp-card-front">서민</div><div class="pp-card-back">oddiy xalq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Sarlavha = siqilgan gap: qo'shimcha/fe'l tashlangan, vergul sabab-natijani bog'laydi.</li>
  <li>Taqlid so'zlar yo'nalishni beradi: 껑충 ↑, 뚝 ↓, 북적 = gavjum, 꽁꽁 = muzlagan.</li>
  <li>Metaforani so'zma-so'z o'qimang; noto'g'ri variantlar = literal o'qish yoki teskari yo'nalish.</li>
  <li>Usul: sarlavhani o'zingiz to'liq gapga oching → keyin variant tanlang.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 91) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 기사 제목 2: Iqtisod va jamiyat metaforalari (빨간불, 한파, 훈풍...)",
        "summary": "Iqtisodiy sarlavhalarning doimiy metaforalari: signal chiroqlari, ob-havo obrazlari va jonlanish so'zlari.",
        "order":   91,
        "blocks": [
            {"rich_text": """
<h2>💹 Iqtisod sarlavhalari: metafora lug'ati</h2>
<p>25–27-savollarning kamida bittasi iqtisod/jamiyat mavzusida keladi. Gazetachilar bir xil
obrazlarni qayta-qayta ishlatadi — lug'atini bilsangiz, sarlavha ochiq kitob:</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;" open>
  <summary style="cursor:pointer;font-weight:600;">🚦 Signal chiroqlari</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>빨간불</strong> (qizil chiroq) — <mark style="background:#fee2e2;">xavf, yomonlashish belgisi</mark></p>
      <p style="color:#475569;margin:0;">수출에 빨간불 — <em>eksportda xavf signali (eksport yomonlashmoqda)</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>청신호 / 파란불</strong> (yashil signal) — <mark style="background:#dcfce7;">yaxshi istiqbol belgisi</mark></p>
      <p style="color:#475569;margin:0;">경제 회복에 청신호 — <em>iqtisod tiklanishiga yashil yo'l (umid paydo bo'ldi)</em></p>
    </div>
  </div>
</details>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">🌡️ Ob-havo obrazlari (iqtisodda!)</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>한파</strong> (sovuq to'lqin) — og'ir davr, inqiroz</p>
      <p style="color:#475569;margin:0;">취업 한파 — <em>ishga joylashish "sovug'i" (ish topish juda qiyin davr)</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>훈풍</strong> (iliq shamol) — ijobiy o'zgarish shabadasi</p>
      <p style="color:#475569;margin:0;">부동산 시장에 훈풍 — <em>ko'chmas mulk bozorida jonlanish boshlandi</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>얼어붙다</strong> (muzlab qolmoq) — to'xtab qolmoq (savdo, bozor)</p>
      <p style="color:#475569;margin:0;">소비 심리 꽁꽁 얼어붙어 — <em>xarid qilish istagi butunlay so'ndi</em></p>
    </div>
  </div>
</details>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">🌱 Jonlanish va qiynalish</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>기지개를 켜다</strong> (kerishmoq) — uyqudan keyin jonlana boshlamoq</p>
      <p style="color:#475569;margin:0;">여행 업계, 3년 만에 기지개 — <em>sayohat sohasi 3 yildan keyin jonlanmoqda</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>몸살을 앓다</strong> (bezgak bo'lmoq) — biror muammodan qattiq qiynalmoq</p>
      <p style="color:#475569;margin:0;">관광지, 쓰레기 몸살 — <em>sayyohlik maskani axlatdan qiynalmoqda</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>날개 돋친 듯 팔리다</strong> (qanot chiqargandek sotilmoq) — juda tez sotilmoq</p>
      <p style="color:#475569;margin:0;">선풍기, 무더위에 날개 돋친 듯 — <em>ventilyator jaziramada "uchib" sotilmoqda</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>들썩</strong> — qo'zg'alish, ko'tarilishga shaylanish (narx, kayfiyat)</p>
      <p style="color:#475569;margin:0;">명절 앞두고 과일값 들썩 — <em>bayram oldidan meva narxi ko'tarila boshladi</em></p>
    </div>
  </div>
</details>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Metaforani ko'rganda o'zingizdan so'rang: bu obraz
  <strong>yaxshilikmi (+) yoki yomonlikmi (−)</strong>? 청신호·훈풍·기지개·날개 = (+);
  빨간불·한파·얼어붙다·몸살 = (−). Belgisi to'g'ri variantgina javob bo'la oladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>수출 감소 계속, 경제에 빨간불 켜져</strong></p>
</div>
""",
             "choices": [
                 {"text": "수출이 계속 줄어서 경제 상황이 나빠질 위험이 커졌다. (Eksport kamayishda davom etib, iqtisod yomonlashish xavfi ortdi.)", "is_correct": True},
                 {"text": "수출이 늘어서 경제가 좋아지고 있다. (Eksport oshib, iqtisod yaxshilanmoqda.)", "is_correct": False},
                 {"text": "공장들이 밤에도 일하려고 빨간 전등을 켰다. (Zavodlar kechasi ham ishlash uchun qizil chiroq yoqdi.)", "is_correct": False},
                 {"text": "경제가 좋아져서 수출품에 빨간 표시를 붙였다. (Iqtisod yaxshilanib, eksport mahsulotiga qizil belgi qo'yildi.)", "is_correct": False},
             ],
             "explanation": """
<p>감소 계속 (kamayish davom etmoqda) + <strong>빨간불</strong> = xavf signali → ① ✅.
② yo'nalish teskari. ③④ metaforani <strong>so'zma-so'z</strong> o'qigan (haqiqiy chiroq,
haqiqiy belgi) — 25–27-savollarning eng sevimli tuzog'i. Qoida: sarlavhada rang/ob-havo/
tana so'zi ko'rsangiz — avval metafora deb qarang!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>얼어붙은 취업 시장에 훈풍... 채용 늘리는 기업 많아져</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">채용 — ishga olish · 기업 — korxona</p>
""",
             "choices": [
                 {"text": "일자리를 찾기 어려웠던 상황이 좋아지기 시작했다. (Ish topish qiyin bo'lgan vaziyat yaxshilana boshladi.)", "is_correct": True},
                 {"text": "날씨가 추워져서 회사들이 문을 닫았다. (Havo sovub, kompaniyalar yopildi.)", "is_correct": False},
                 {"text": "취업 시장이 얼어붙어서 채용이 완전히 중단되었다. (Ish bozori muzlab, ishga olish butunlay to'xtadi.)", "is_correct": False},
                 {"text": "바람이 많이 불어서 기업들이 채용 행사를 취소했다. (Shamol kuchli esib, korxonalar yollash tadbirini bekor qildi.)", "is_correct": False},
             ],
             "explanation": """
<p>Ikki metafora birga: 얼어붙은 (muzlagan = qiyin davrda bo'lgan) ish bozoriga
<strong>훈풍</strong> (iliq shamol = ijobiy o'zgarish) + izohi ham sarlavhada: 채용 늘리는
기업 많아져 (yollovchi korxonalar ko'paydi) → ① ✅. ②④ ob-havoni so'zma-so'z o'qigan.
③ faqat birinchi metaforani ko'rib, 훈풍 (burilish!)ni o'tkazib yuborgan — sarlavhaning
<strong>oxirigacha</strong> o'qing.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>더위 오자 에어컨 날개 돋친 듯 팔려... 공장 밤샘 작업</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">밤샘 작업 — tunab ishlash</p>
""",
             "choices": [
                 {"text": "에어컨이 아주 많이 팔려서 공장이 밤까지 일하고 있다. (Konditsioner juda ko'p sotilib, zavod kechasi ham ishlayapti.)", "is_correct": True},
                 {"text": "에어컨이 팔리지 않아서 공장이 문을 닫게 되었다. (Konditsioner sotilmay, zavod yopilmoqchi.)", "is_correct": False},
                 {"text": "새 에어컨에 날개가 달려서 인기가 많다. (Yangi konditsionerga qanot o'rnatilgani uchun mashhur.)", "is_correct": False},
                 {"text": "공장에서 밤에 에어컨을 켜고 일한다. (Zavodda kechasi konditsioner yoqib ishlashadi.)", "is_correct": False},
             ],
             "explanation": """
<p><strong>날개 돋친 듯 팔리다</strong> = "qanot chiqargandek sotilmoq" — juda tez, juda
ko'p sotilish. Natijasi: 밤샘 작업 (talabga ulgurish uchun tunab ishlash) → ① ✅.
③ metaforani so'zma-so'z o'qigan (haqiqiy qanot?!), ④ so'zlarni to'g'ri o'qib, mantiqni
noto'g'ri yig'gan — 밤샘 작업 <em>ishlab chiqarish</em>, konditsioner yoqish emas.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어 (metaforalar!)</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">빨간불</div><div class="pp-card-back">xavf signali (−)</div></div>
  <div class="pp-card"><div class="pp-card-front">청신호</div><div class="pp-card-back">yaxshi istiqbol belgisi (+)</div></div>
  <div class="pp-card"><div class="pp-card-front">한파</div><div class="pp-card-back">og'ir davr, "sovuq" (−)</div></div>
  <div class="pp-card"><div class="pp-card-front">훈풍</div><div class="pp-card-back">ijobiy o'zgarish shabadasi (+)</div></div>
  <div class="pp-card"><div class="pp-card-front">얼어붙다</div><div class="pp-card-back">to'xtab qolmoq (bozor) (−)</div></div>
  <div class="pp-card"><div class="pp-card-front">기지개를 켜다</div><div class="pp-card-back">jonlana boshlamoq (+)</div></div>
  <div class="pp-card"><div class="pp-card-front">몸살을 앓다</div><div class="pp-card-back">muammodan qiynalmoq (−)</div></div>
  <div class="pp-card"><div class="pp-card-front">날개 돋친 듯 팔리다</div><div class="pp-card-back">juda tez sotilmoq (+)</div></div>
  <div class="pp-card"><div class="pp-card-front">들썩</div><div class="pp-card-back">ko'tarilishga shaylanish</div></div>
  <div class="pp-card"><div class="pp-card-front">채용</div><div class="pp-card-back">ishga olish</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Iqtisod sarlavhalari doimiy metaforalar bilan ishlaydi — belgisini yodlang: (+) yoki (−).</li>
  <li>Sarlavhani <strong>oxirigacha</strong> o'qing: ko'pincha ikkinchi qismi metaforani o'zi izohlaydi.</li>
  <li>Rang, ob-havo, tana so'zlari — 99% metafora; so'zma-so'z o'qigan variant doim tuzoq.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 92) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 기사 제목 3: Ob-havo, madaniyat, sport + aralash mashq",
        "summary": "Qolgan sarlavha turlari (ob-havo, festival, sport) va imtihon uslubidagi yakuniy to'plam.",
        "order":   92,
        "blocks": [
            {"rich_text": """
<h2>🌦️ Boshqa sarlavha turlari</h2>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Ob-havo</span> — bu yerda so'zlar ko'pincha <strong>to'g'ri ma'noda</strong>!</p>
  <p style="font-size:1.05em;margin:0 0 4px;">전국 꽁꽁, 주말까지 강추위 이어져 — <em>Butun mamlakat muzladi, kuchli sovuq dam olishgacha davom etadi.</em></p>
  <p style="color:#475569;margin:0;">Kalitlar: 강추위 (qattiq sovuq), 무더위 (jazirama), 폭우 (jala), 폭설 (qattiq qor), 미세먼지 (chang)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Madaniyat / festival</span></p>
  <p style="font-size:1.05em;margin:0 0 4px;">벚꽃 축제 열기 후끈... 관광객 발길 이어져 — <em>Olcha gullari bayrami qizg'in — sayyohlar oqimi uzluksiz.</em></p>
  <p style="color:#475569;margin:0;">Kalitlar: 열기 후끈 (qizg'in ruh), <strong>발길이 이어지다</strong> (odam oqimi to'xtamaydi) ↔ <strong>발길이 끊기다</strong> (odam kelmay qo'ydi), 인산인해 (odam dengizi)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Sport</span></p>
  <p style="font-size:1.05em;margin:0 0 4px;">한국, 일본 꺾고 결승 진출 — <em>Koreya Yaponiyani yengib finalga chiqdi.</em></p>
  <p style="color:#475569;margin:0;">Kalitlar: <strong>꺾다</strong> (yengmoq — "sindirmoq"), 진출 (chiqish), 우승 (chempionlik), 아쉽게 패해 (afsuski yutqazib), 역전승 (ortda qolib yutish)</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Uch nuqta (...) sarlavhada vergul kabi ishlaydi: birinchi qism —
  voqea, keyingisi — tafsilot yoki natija. 꺾다 sportda "yengmoq" — jismonan sindirish emas!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (ob-havo).</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>주말 내내 폭설... 전국 도로 곳곳 마비</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">마비 — falaj (to'xtab qolish) · 곳곳 — har yerda</p>
""",
             "choices": [
                 {"text": "주말에 눈이 많이 와서 여러 도로에서 차가 다니기 어려워졌다. (Dam olish kunlari qor ko'p yog'ib, ko'p yo'llarda qatnov qiyinlashdi.)", "is_correct": True},
                 {"text": "주말에 눈이 그쳐서 도로가 다시 열렸다. (Dam olishda qor tinib, yo'llar qayta ochildi.)", "is_correct": False},
                 {"text": "도로 공사 때문에 주말에 길이 막혔다. (Yo'l ta'miri sababli dam olishda yo'l yopildi.)", "is_correct": False},
                 {"text": "폭설로 병원에 입원한 사람이 많아졌다. (Qattiq qor tufayli kasalxonaga yotganlar ko'paydi.)", "is_correct": False},
             ],
             "explanation": """
<p>폭설 (kuchli qor) + 도로 마비 ("yo'llar falaj bo'ldi" — metafora: qatnov to'xtadi) → ① ✅.
② teskari (내내 = "davomida to'xtovsiz"!). ③ sababni almashtirgan (qor emas, ta'mir?).
④ 마비 tibbiy so'z bo'lgani uchun "kasalxona" tuzog'i qo'yilgan — lekin sarlavhada
kasalxona yo'q, <strong>도로</strong> (yo'l) falaj!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (madaniyat).</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>비 오는 날씨에도 불꽃 축제 열기 후끈... 10만 인파 몰려</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">인파 — odamlar oqimi · 몰리다 — yopirilib kelmoq</p>
""",
             "choices": [
                 {"text": "날씨가 안 좋았지만 축제에 아주 많은 사람이 모였다. (Ob-havo yomon bo'lsa ham bayramga juda ko'p odam yig'ildi.)", "is_correct": True},
                 {"text": "비 때문에 불꽃 축제가 취소되었다. (Yomg'ir sababli mushakbozlik bayrami bekor qilindi.)", "is_correct": False},
                 {"text": "축제장에서 불이 나서 사람들이 대피했다. (Bayram maydonida yong'in chiqib, odamlar evakuatsiya qilindi.)", "is_correct": False},
                 {"text": "날씨가 더워서 축제에 온 사람이 적었다. (Havo issiq bo'lgani uchun bayramga kam odam keldi.)", "is_correct": False},
             ],
             "explanation": """
<p>-에도 (bo'lishiga qaramay!) + 열기 후끈 (ruh qizg'in) + 10만 인파 (100 ming odam) → ① ✅.
③ juda ayyor tuzoq: 불꽃 (mushakbozlik) + 후끈 (qizigan)ni "yong'in" deb o'qitmoqchi —
lekin 열기 후끈 bayram <em>ruhining</em> qizg'inligi. ②④ teskari. -에도 qo'shimchasi
(qaramay) sarlavhalarda juda muhim burilish belgisi!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (sport).</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>한국 야구, 9회 역전승... 결승 진출에 성큼</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">9회 — 9-inning (beysbolda oxirgi qism) · 성큼 — katta qadam bilan</p>
""",
             "choices": [
                 {"text": "한국 팀이 지고 있다가 마지막에 이겨서 결승에 가까워졌다. (Koreya jamoasi yutqazib borayotib oxirida g'alaba qozondi va finalga yaqinlashdi.)", "is_correct": True},
                 {"text": "한국 팀이 크게 져서 대회에서 탈락했다. (Koreya jamoasi katta hisobda yutqazib, musobaqadan chiqib ketdi.)", "is_correct": False},
                 {"text": "한국 팀이 결승에서 우승을 차지했다. (Koreya jamoasi finalda chempion bo'ldi.)", "is_correct": False},
                 {"text": "경기가 9회까지 가지 못하고 취소되었다. (O'yin 9-inninggacha yetmay bekor qilindi.)", "is_correct": False},
             ],
             "explanation": """
<p><strong>역전승</strong> = 역전 (vaziyatni ag'darish) + 승 (g'alaba) — "ortda qolib
turib yutish" → yutqazayotgan edi, oxirgi (9-) inningda yutdi. 결승 진출에 성큼 —
finalga "katta qadam" (hali final <em>emas</em>!) → ① ✅. ③ ayyor: hali finalga
<em>chiqmoqda</em>, chempion bo'lgani yo'q — 성큼 (yaqinlashish) bilan 우승 (chempionlik)ni
farqlang. Sport sarlavhasida har so'z bosqichni bildiradi: 진출 < 결승 < 우승.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 4 (aralash).</strong> 다음 신문 기사의 제목을 가장 잘 설명한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.2em;margin:0;"><strong>관광객 발길 뚝... 시장 상인들 한숨 깊어져</strong></p>
</div>
<p style="color:#64748b;font-size:.92em;">상인 — savdogar</p>
""",
             "choices": [
                 {"text": "시장을 찾는 관광객이 크게 줄어서 상인들의 걱정이 커졌다. (Bozorga keluvchi sayyohlar keskin kamayib, savdogarlar tashvishi ortdi.)", "is_correct": True},
                 {"text": "관광객이 많아져서 상인들이 바빠졌다. (Sayyohlar ko'payib, savdogarlar band bo'lib qoldi.)", "is_correct": False},
                 {"text": "상인들이 관광객의 발을 치료해 주었다. (Savdogarlar sayyohlarning oyog'ini davolab qo'yishdi.)", "is_correct": False},
                 {"text": "시장이 문을 닫아서 관광객들이 한숨을 쉬었다. (Bozor yopilgani uchun sayyohlar xo'rsindi.)", "is_correct": False},
             ],
             "explanation": """
<p>Hammasi birga: <strong>발길 뚝</strong> (odam oqimi keskin uzildi — 발길이 끊기다 + 뚝) va
<strong>한숨 깊어져</strong> (xo'rsinish chuqurlashdi = tashvish ortdi) → ① ✅.
② teskari, ③ 발 (oyoq)ni so'zma-so'z o'qigan absurd tuzoq, ④ kim xo'rsinayotganini
almashtirgan (savdogarlar, sayyohlar emas — <strong>egani almashtirish</strong> tuzog'i
9–12-savollardan tanish!). Mavzu tugadi — endi sarlavhalar siz uchun ochiq kitob! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">강추위 / 무더위</div><div class="pp-card-back">qattiq sovuq / jazirama</div></div>
  <div class="pp-card"><div class="pp-card-front">폭설 / 폭우</div><div class="pp-card-back">kuchli qor / jala</div></div>
  <div class="pp-card"><div class="pp-card-front">마비</div><div class="pp-card-back">falaj = to'xtab qolish</div></div>
  <div class="pp-card"><div class="pp-card-front">발길이 이어지다 / 끊기다</div><div class="pp-card-back">odam oqimi uzluksiz / uzildi</div></div>
  <div class="pp-card"><div class="pp-card-front">인파가 몰리다</div><div class="pp-card-back">odam yopirilib kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">꺾다</div><div class="pp-card-back">yengmoq (raqibni)</div></div>
  <div class="pp-card"><div class="pp-card-front">역전승</div><div class="pp-card-back">ortda qolib turib yutish</div></div>
  <div class="pp-card"><div class="pp-card-front">우승 / 진출</div><div class="pp-card-back">chempionlik / (bosqichga) chiqish</div></div>
  <div class="pp-card"><div class="pp-card-front">한숨이 깊어지다</div><div class="pp-card-back">tashvishi ortmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-에도</div><div class="pp-card-back">~ga qaramay (burilish belgisi)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Ob-havo sarlavhasida so'zlar to'g'ri ma'noda; iqtisod/jamiyatda — deyarli doim metafora.</li>
  <li>Doimiy juftliklar: 발길 이어지다↔끊기다, 껑충↔뚝, 훈풍↔한파, 진출→우승 (bosqichlar).</li>
  <li>Tuzoqlar o'sha-o'sha: so'zma-so'z o'qish, teskari yo'nalish, egani almashtirish.</li>
  <li>Usul o'zgarmas: sarlavhani to'liq gapga oching → belgisini (+/−) tekshiring → variant.</li>
</ul>
"""},
        ],
    },
]
