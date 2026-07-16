# TOPIK II Listening — 25–30-savollar: Intervyu bloki (인터뷰: 의도·직업), lessons 1–3 (orders 70–72).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_interview_1_3.py \
#            --out examprep/management/commands/audio/interview
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_interview_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/interview

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "25–30-savollar: Intervyu bloki (인터뷰: 의도·직업)",
    "summary": "Intervyu va suhbatlarning uch savoli: mehmonning asosiy fikri, gapirish maqsadi (의도) va kasbini topish (직업).",
    "icon":    "bi-mic",
    "order":   8,
}

LESSONS = [
    # ── Lesson 1 (order 70) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 인터뷰 1: 25–26-savollar — mehmonning asosiy gapi",
        "summary": "Intervyu formati: boshlovchi so'raydi, mehmon javob beradi; mehmonning bosh xabari odatda birinchi yoki oxirgi jumlada.",
        "order":   70,
        "blocks": [
            {"rich_text": """
<h2>🎤 25–30-savollar: intervyu bloki</h2>
<p>Bu oltita savol (uch juftlik) asosan <strong>intervyu</strong> va maqsadli suhbatlardan
tuziladi. Uch xil "yangi" savol turi bor — har biriga bittadan dars:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>25.</strong> 남자의 중심 생각 — mehmonning asosiy fikri (bu dars).</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>27.</strong> 남자가 여자에게 말하는 의도 — gapirish MAQSADI (keyingi dars).</p>
  <p style="font-size:1.05em;margin:0;"><strong>29.</strong> 남자는 누구인지 — mehmonning KASBI (keyingi dars). Juftlarning ikkinchisi (26/28/30) — doim 내용 일치.</p>
</div>
<h3>Intervyuni qanday eshitish kerak</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>Boshlovchining kirishi — sovg'a.</strong> 오늘은 ~하시는 분을
  모셨습니다 (bugun …-chi insonni taklif qildik) — mavzu va kasb shu yerda ochiq aytiladi.
  Kirishni o'tkazib yubormang!</p></div>
  <div class="pp-step"><p><strong>Mehmonning bosh xabari</strong> odatda javobining <strong>birinchi</strong>
  yoki <strong>oxirgi</strong> jumlasida: 가장 중요한 것은 ~입니다 / ~아야 합니다 / ~시기 바랍니다.
  O'rtadagi hamma narsa — misol va dalil (26-savol uchun material!).</p></div>
  <div class="pp-step"><p><strong>Ikki eshitish rejasi</strong> o'sha-o'sha: birinchisida fikr,
  ikkinchisida faktlar (소거법).</p></div>
</div>
"""},
            {"rich_text": """
<p><strong>25-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_070_1.mp3",
             "audio_script": [
                 ("여자", "오늘은 유기견 보호소를 운영하시는 분을 모셨습니다. 소장님, 강아지를 키우고 싶어 하는 분들께 한 말씀 부탁드립니다."),
                 ("남자", "강아지를 기르는 일은 생각보다 힘듭니다. 돈과 시간이 많이 들고 십 년 넘게 책임져야 하지요. 그래서 귀엽다는 이유만으로 강아지를 데려오시면 안 됩니다. 기르기 전에 끝까지 책임질 수 있는지 꼭 생각해 보시기 바랍니다."),
             ],
             "choices": [
                 {"text": "끝까지 책임질 수 있을 때 강아지를 길러야 한다. (Oxirigacha mas'uliyat olishga tayyor bo'lgandagina kuchuk boqish kerak.)", "is_correct": True},
                 {"text": "강아지는 귀여우니까 데려오는 것이 좋다. (Kuchuk shirin, shuning uchun olib kelgan yaxshi.)", "is_correct": False},
                 {"text": "강아지를 기르는 데는 돈이 들지 않는다. (Kuchuk boqishga pul ketmaydi.)", "is_correct": False},
                 {"text": "보호소를 많이 만들어야 한다. (Boshpanalarni ko'proq qurish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Bosh xabar — javobning oxirgi jumlasida, qolipi bilan: 끝까지 책임질 수 있는지 꼭 생각해
보<strong>시기 바랍니다</strong> → ✅ ①. ② mehmon aynan rad etgan sabab (귀엽다는
이유<strong>만으로</strong>… 안 됩니다!), ③ teskari (돈과 시간이 많이 <strong>들고</strong>).
④ mavzuga yaqin, lekin aytilmagan — soyabon testidan o'tmaydi. O'rtadagi "pul, vaqt,
o'n yil" — dalillar; ular 26-savolda kerak bo'ladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 오늘은 유기견 보호소를 운영하시는 분을 모셨습니다. 소장님, 강아지를
    키우고 싶어 하는 분들께 한 말씀 부탁드립니다.<br>
    <em style="color:#475569;">Bugun tashlandiq itlar boshpanasini boshqaradigan insonni taklif
    qildik. Direktor, kuchuk boqmoqchi bo'lganlarga bir og'iz so'z ayting.</em></p>
    <p><strong>남자:</strong> 강아지를 기르는 일은 생각보다 힘듭니다. 돈과 시간이 많이 들고 십 년
    넘게 책임져야 하지요. 그래서 귀엽다는 이유만으로 강아지를 데려오시면 안 됩니다. 기르기 전에
    끝까지 책임질 수 있는지 꼭 생각해 보시기 바랍니다.<br>
    <em style="color:#475569;">Kuchuk boqish o'ylagandan qiyin. Pul va vaqt ko'p ketadi, o'n
    yildan ortiq mas'uliyat olish kerak. Shuning uchun faqat shirinligi uchun kuchuk olib
    kelmang. Boqishdan oldin oxirigacha mas'uliyat ola olasizmi — albatta o'ylab ko'ring.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>26-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida — ikkinchi marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "강아지를 기르는 데는 돈과 시간이 많이 든다. (Kuchuk boqishga pul va vaqt ko'p ketadi.)", "is_correct": True},
                 {"text": "남자는 유기견 보호소에서 일한 적이 없다. (Erkak boshpanada ishlamagan.)", "is_correct": False},
                 {"text": "강아지는 오 년 정도만 책임지면 된다. (Kuchukka besh yilcha mas'ul bo'lish kifoya.)", "is_correct": False},
                 {"text": "강아지를 기르는 일은 생각보다 쉽다. (Kuchuk boqish o'ylagandan oson.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② kirishga zid (보호소를 <strong>운영하시는</strong> 분 — boshpanani o'zi
boshqaradi!), ③ raqam (<strong>십 년 넘게</strong> — o'n yildan ortiq!), ④ teskari
(생각보다 <strong>힘듭니다</strong>). ✅ ①: 돈과 시간이 많이 들고 — aynan aytilgan.
Ko'rdingizmi: 26 ning materiali — 25 da "dalil" deb chetga surgan jumlalar. Ikki savol
bir matnni ikki qavatga bo'lib oladi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">유기견</div><div class="pp-card-back">tashlandiq it</div></div>
  <div class="pp-card"><div class="pp-card-front">보호소</div><div class="pp-card-back">boshpana</div></div>
  <div class="pp-card"><div class="pp-card-front">운영하다</div><div class="pp-card-back">boshqarmoq, yuritmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">기르다 / 키우다</div><div class="pp-card-back">boqmoq, o'stirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">책임지다</div><div class="pp-card-back">mas'uliyat olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">데려오다</div><div class="pp-card-back">olib kelmoq (jonzotni)</div></div>
  <div class="pp-card"><div class="pp-card-front">~(으)시기 바랍니다</div><div class="pp-card-back">…ishingizni so'rayman</div></div>
  <div class="pp-card"><div class="pp-card-front">모시다</div><div class="pp-card-back">taklif qilmoq (hurmat bilan)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Boshlovchining kirishi mavzu va kasbni ochiq aytadi — o'tkazib yubormang.</li>
  <li>Mehmonning bosh xabari — birinchi yoki oxirgi jumlada (~아야 합니다 / ~시기 바랍니다).</li>
  <li>O'rtadagi dalillar 25 uchun chalg'ituvchi, 26 uchun xazina.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 71) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 인터뷰 2: Maqsad va kasb — 의도 (27) va 직업 (29)",
        "summary": "27-savol: erkak NEGA gapiryapti (권하려고, 알려 주려고…); 29-savol: mehmon KIM — kasbni belgilar orqali topish.",
        "order":   71,
        "blocks": [
            {"rich_text": """
<h2>🎯 Ikki yangi savol turi</h2>
<h3>27-savol: gapirish maqsadi (말하는 의도)</h3>
<p>Savol: 남자가 여자에게 말하는 <strong>의도</strong>를 고르십시오 — erkak bu gaplarni ayolga
NEGA aytyapti? Variantlar "~려고" bilan tugaydi (o'qishdagi 48-savolning quloqdagi
qarindoshi!):</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>알려 주려고</strong> — xabar berish uchun &nbsp;|&nbsp; <strong>권하려고 / 추천하려고</strong> — tavsiya qilish uchun</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>부탁하려고</strong> — iltimos qilish uchun &nbsp;|&nbsp; <strong>확인하려고</strong> — aniqlash uchun</p>
  <p style="font-size:1.05em;margin:0;"><strong>위로하려고</strong> — tasalli berish uchun &nbsp;|&nbsp; <strong>감사하려고</strong> — minnatdorchilik uchun</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> Maqsad — erkakning <strong>oxirgi replikasi</strong>gacha yig'ilib
  boradi: xabar bilan boshlab, taklif bilan tugatsa — maqsad <strong>taklif</strong> (권유),
  shunchaki xabar emas! Eng kuchli variantni oling: axborot < tavsiya < iltimos.
</div>
<h3>29-savol: mehmon kim? (누구인지)</h3>
<p>Kasb hech qachon aytilmaydi — <strong>belgilar</strong> aytadi: nimani qiladi (fe'llar!),
kim bilan ishlaydi, qayerda. Formula: <strong>ob'ekt + fe'l = kasb</strong>: 음식을 만들다 →
요리사, 고장 난 것을 고치다 → 수리 기사, 손님을 안내하다 → 가이드, 사진을 찍다 → 사진작가.</p>
"""},
            {"rich_text": """
<p><strong>27-savol.</strong> 남자가 여자에게 말하는 의도를 고르십시오.</p>
""",
             "audio": "topik_l_071_1.mp3",
             "audio_script": [
                 ("남자", "다음 주에 회사 근처에 새 헬스장이 문을 연대요. 지금 미리 등록하면 삼 개월 동안 반값이래요."),
                 ("여자", "정말요? 저 요즘 운동할 곳을 찾고 있었는데."),
                 ("남자", "그래서 말씀드리는 거예요. 우리 같이 등록할래요? 혼자 다니면 금방 그만두게 되잖아요."),
             ],
             "choices": [
                 {"text": "헬스장에 같이 등록하자고 권하려고 (Sport zaliga birga yozilishni taklif qilish uchun)", "is_correct": True},
                 {"text": "헬스장의 위치를 확인하려고 (Sport zali joylashuvini aniqlash uchun)", "is_correct": False},
                 {"text": "운동을 그만두겠다고 말하려고 (Sportni tashlashini aytish uchun)", "is_correct": False},
                 {"text": "할인 이유를 물어보려고 (Chegirma sababini so'rash uchun)", "is_correct": False},
             ],
             "explanation": """
<p>Zanjir: xabar (새 헬스장 + 반값) → sabab (그래서 말씀드리는 거예요 — "shuning uchun
aytyapman"!) → taklif (<strong>같이 등록할래요?</strong>) → dalil (혼자 다니면 금방
그만두게 되잖아요). Eng kuchli bo'g'in — taklif → <mark style="background:#dcfce7;">권하려고</mark>
✅. "Faqat xabar berish uchun" varianti bo'lganda ham u tor bo'lardi — chunki erkak taklifda
to'xtadi. 그래서 말씀드리는 거예요 — maqsad savolining oltin signali!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 다음 주에 회사 근처에 새 헬스장이 문을 연대요. 지금 미리 등록하면 삼 개월 동안 반값이래요.<br>
    <em style="color:#475569;">Kelasi hafta ishxona yaqinida yangi sport zali ochilarkan. Hozir oldindan yozilsangiz, uch oy davomida yarim narxda ekan.</em></p>
    <p><strong>여자:</strong> 정말요? 저 요즘 운동할 곳을 찾고 있었는데.<br>
    <em style="color:#475569;">Rostdanmi? Men shu kunlarda shug'ullanadigan joy qidirayotgandim.</em></p>
    <p><strong>남자:</strong> 그래서 말씀드리는 거예요. 우리 같이 등록할래요? 혼자 다니면 금방 그만두게 되잖아요.<br>
    <em style="color:#475569;">Shuning uchun aytyapman-da. Birga yozilamizmi? Yolg'iz qatnasa, tez tashlab qo'yiladi-ku.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>28-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "지금 등록하면 세 달 동안 반값이다. (Hozir yozilsangiz, uch oy yarim narxda bo'ladi.)", "is_correct": True},
                 {"text": "헬스장은 이미 문을 열었다. (Sport zali allaqachon ochilgan.)", "is_correct": False},
                 {"text": "여자는 운동할 곳을 벌써 정했다. (Ayol shug'ullanadigan joyni allaqachon tanlagan.)", "is_correct": False},
                 {"text": "남자는 혼자 운동하는 것을 좋아한다. (Erkak yolg'iz shug'ullanishni yoqtiradi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② zamon (<strong>다음 주에</strong> 문을 연대요 — hali ochilmagan!), ③ teskari
(찾고 <strong>있었는데</strong> — hali qidirmoqda), ④ teskari (혼자 다니면 그만두게
된다 — yolg'izlikka qarshi!). ✅ ①: 삼 개월 동안 반값 = 세 달 동안 반값 (삼 개월 ⇄ 세 달 —
xitoycha va koreyscha sanoq paraphrase'i, quloq uchun klassik almashinuv!).</p>
"""},
            {"rich_text": """
<p><strong>29-savol.</strong> 남자는 누구인지 고르십시오.</p>
""",
             "audio": "topik_l_071_2.mp3",
             "audio_script": [
                 ("여자", "이 일을 하시면서 언제 가장 보람을 느끼세요?"),
                 ("남자", "손님들이 여행을 마치고 \"덕분에 잘 봤습니다\"라고 인사해 주실 때지요. 저는 손님들을 모시고 여러 나라의 유명한 곳을 다니면서 그곳의 역사와 문화를 설명해 드립니다. 낯선 곳에서 손님들의 안전을 지키는 것도 제 중요한 일이고요."),
             ],
             "choices": [
                 {"text": "여행 가이드 (sayohat yo'lboshchisi)", "is_correct": True},
                 {"text": "역사 선생님 (tarix o'qituvchisi)", "is_correct": False},
                 {"text": "호텔 직원 (mehmonxona xodimi)", "is_correct": False},
                 {"text": "비행기 승무원 (samolyot styuardi)", "is_correct": False},
             ],
             "explanation": """
<p>Belgilar formulasi: 손님들을 <strong>모시고</strong> (mehmonlarni olib) + 여러 나라를
<strong>다니면서</strong> (mamlakatlarni aylanib) + 역사와 문화를 <strong>설명해</strong>
(tushuntirib) + 안전을 <strong>지키는</strong> (asrab) → hammasi birga =
<mark style="background:#dcfce7;">여행 가이드</mark> ✅. ② faqat "tarix tushuntirish"ga
yopishadi (tor!), ③④ sayohat sohasidan, lekin "olib yurish" belgisi yo'q. Kasb savolida
BITTA belgi yetmaydi — <strong>hamma belgini yopadigan</strong> kasbni oling (soyabon!).</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 이 일을 하시면서 언제 가장 보람을 느끼세요?<br>
    <em style="color:#475569;">Bu ishda qachon eng katta mamnunlik his qilasiz?</em></p>
    <p><strong>남자:</strong> 손님들이 여행을 마치고 "덕분에 잘 봤습니다"라고 인사해 주실 때지요.
    저는 손님들을 모시고 여러 나라의 유명한 곳을 다니면서 그곳의 역사와 문화를 설명해 드립니다.
    낯선 곳에서 손님들의 안전을 지키는 것도 제 중요한 일이고요.<br>
    <em style="color:#475569;">Mehmonlar sayohatni tugatib "sizning tufayli yaxshi ko'rdik" deb
    minnatdorchilik bildirganida-da. Men mehmonlarni olib, turli mamlakatlarning mashhur
    joylarini aylanib, u yerlarning tarixi va madaniyatini tushuntirib beraman. Notanish joyda
    mehmonlar xavfsizligini asrash ham muhim vazifam.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>30-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "남자는 손님들에게 역사와 문화를 설명해 준다. (Erkak mehmonlarga tarix va madaniyatni tushuntiradi.)", "is_correct": True},
                 {"text": "남자는 한 나라 안에서만 일한다. (Erkak faqat bitta mamlakat ichida ishlaydi.)", "is_correct": False},
                 {"text": "손님의 안전은 남자의 일이 아니다. (Mehmonlar xavfsizligi erkakning vazifasi emas.)", "is_correct": False},
                 {"text": "남자는 여행하는 것을 싫어한다. (Erkak sayohat qilishni yomon ko'radi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (<strong>여러 나라</strong>의 유명한 곳 — ko'p mamlakat!), ③ teskari
(안전을 지키는 것<strong>도</strong> 제 중요한 일 — vazifasi!), ④ ohangga zid (보람을
느낀다 — mamnunlik his qiladi). ✅ ①: 역사와 문화를 설명해 드립니다. 29 ni to'g'ri
topsangiz, 30 ancha oson bo'ladi — kasb belgilariga oid faktlar allaqachon miyangizda!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">의도</div><div class="pp-card-back">maqsad, niyat</div></div>
  <div class="pp-card"><div class="pp-card-front">권하다</div><div class="pp-card-back">tavsiya qilmoq, taklif qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">반값</div><div class="pp-card-back">yarim narx</div></div>
  <div class="pp-card"><div class="pp-card-front">보람을 느끼다</div><div class="pp-card-back">mamnunlik (ma'no) his qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">낯선 곳</div><div class="pp-card-back">notanish joy</div></div>
  <div class="pp-card"><div class="pp-card-front">안전을 지키다</div><div class="pp-card-back">xavfsizlikni asramoq</div></div>
  <div class="pp-card"><div class="pp-card-front">덕분에</div><div class="pp-card-back">tufayli, sharofati bilan</div></div>
  <div class="pp-card"><div class="pp-card-front">삼 개월 = 세 달</div><div class="pp-card-back">uch oy (ikki xil sanoq!)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>의도 (27): zanjirning eng kuchli bo'g'inini oling — xabar < tavsiya < iltimos; signal: 그래서 말씀드리는 거예요.</li>
  <li>직업 (29): ob'ekt+fe'l belgilari → hammasini yopadigan kasb (bitta belgi yetmaydi).</li>
  <li>삼 개월 ⇄ 세 달 kabi sanoq paraphrase'lariga quloq mashq qilsin.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 72) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 인터뷰 3: To'liq amaliyot — dizayner va sirli mehmon",
        "summary": "25–30 to'liq mashqi: hanbok dizayneri bilan intervyu (fikr+mazmun) va kasbini topish kerak bo'lgan sirli mehmon.",
        "order":   72,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: intervyu blokining ikki juftligi</h2>
<p>Ikki intervyu — to'rt savol. Rejani qo'llang: kirishni tinglang (mavzu/kasb!), birinchi
eshitishda bosh xabar yoki kasb belgilari, ikkinchisida faktlar.</p>
"""},
            {"rich_text": """
<p><strong>25-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_072_1.mp3",
             "audio_script": [
                 ("여자", "오늘은 이십 년째 한복을 만들고 계신 디자이너를 모셨습니다. 요즘 젊은이들에게 한복이 다시 인기라고요?"),
                 ("남자", "네, 반가운 일이지요. 그런데 저는 한복이 박물관의 옷이 되면 안 된다고 생각합니다. 그래서 일상에서 편하게 입을 수 있도록 소매를 줄이고 주머니를 단 한복을 만들고 있어요. 전통을 지키는 것도 중요하지만 오늘에 맞게 바꿔 가는 것도 그만큼 중요하니까요."),
             ],
             "choices": [
                 {"text": "전통은 오늘에 맞게 바꿔 가는 것도 중요하다. (An'anani bugunga moslab o'zgartirib borish ham muhim.)", "is_correct": True},
                 {"text": "한복은 박물관에서만 봐야 한다. (Hanbokni faqat muzeyda ko'rish kerak.)", "is_correct": False},
                 {"text": "전통 한복을 그대로 지켜야 한다. (An'anaviy hanbokni aynan saqlash kerak.)", "is_correct": False},
                 {"text": "한복은 젊은이들에게 인기가 없다. (Hanbok yoshlarga yoqmaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Bosh xabar oxirgi jumlada, tanish muvozanat qolipi bilan: 지키는 것<strong>도</strong>
중요하지만 바꿔 가는 것<strong>도</strong> 그만큼 중요하니까요 → ✅ ①. ② u rad etgan
qarash (박물관의 옷이 되면 <strong>안 된다</strong>!), ③ yarim to'g'ri — lekin faqat bir
tomonini aytadi (muvozanatni buzadi), ④ kirishga zid (다시 <strong>인기</strong>라고요).
"A도 중요하지만 B도 중요하다" eshitilsa — javob ikkalasini yoki B ni aytgan variant.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 오늘은 이십 년째 한복을 만들고 계신 디자이너를 모셨습니다. 요즘 젊은이들에게 한복이 다시 인기라고요?<br>
    <em style="color:#475569;">Bugun yigirma yildan beri hanbok tikayotgan dizaynerni taklif qildik. Hozir hanbok yoshlar orasida yana ommalashayotgan ekan-a?</em></p>
    <p><strong>남자:</strong> 네, 반가운 일이지요. 그런데 저는 한복이 박물관의 옷이 되면 안 된다고
    생각합니다. 그래서 일상에서 편하게 입을 수 있도록 소매를 줄이고 주머니를 단 한복을 만들고
    있어요. 전통을 지키는 것도 중요하지만 오늘에 맞게 바꿔 가는 것도 그만큼 중요하니까요.<br>
    <em style="color:#475569;">Ha, quvonarli hol-da. Lekin menimcha, hanbok muzey kiyimiga
    aylanib qolmasligi kerak. Shuning uchun kundalikda bemalol kiyish mumkin bo'lsin deb yengini
    kaltalab, cho'ntak qadalgan hanboklar tikyapman. An'anani saqlash ham muhim, lekin bugunga
    moslab o'zgartirib borish ham xuddi shunchalik muhim-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>26-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "남자는 주머니가 있는 한복을 만들고 있다. (Erkak cho'ntakli hanbok tikmoqda.)", "is_correct": True},
                 {"text": "남자는 한복을 만든 지 십 년이 되었다. (Erkak hanbok tika boshlaganiga o'n yil bo'lgan.)", "is_correct": False},
                 {"text": "남자는 한복의 소매를 길게 만든다. (Erkak hanbok yengini uzun qiladi.)", "is_correct": False},
                 {"text": "요즘 젊은이들은 한복을 입지 않는다. (Hozirgi yoshlar hanbok kiymaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② raqam (<strong>이십 년째</strong>!), ③ teskari (소매를 <strong>줄이고</strong> —
kaltalaydi!), ④ kirishga zid (다시 인기). ✅ ①: 주머니를 <strong>단</strong> 한복 (달다 =
qadamoq, taqmoq). Kichik fe'llarga e'tibor: 줄이다 (kaltalatmoq) ⇄ 늘리다 (uzaytirmoq),
달다 (qadamoq) — bitta bo'g'in farqi javobni belgilaydi.</p>
"""},
            {"rich_text": """
<p><strong>29-savol.</strong> 남자는 누구인지 고르십시오.</p>
""",
             "audio": "topik_l_072_2.mp3",
             "audio_script": [
                 ("여자", "좋은 사진을 찍는 특별한 비결이 있을까요?"),
                 ("남자", "빛이 가장 중요합니다. 그래서 저는 해가 뜨기 전에 미리 가서 기다려요. 결혼식이나 가족 행사 사진도 찍지만 제가 제일 좋아하는 것은 자연 풍경을 찍는 일이에요. 좋은 순간은 기다리는 사람에게만 오니까요."),
             ],
             "choices": [
                 {"text": "사진작가 (fotograf)", "is_correct": True},
                 {"text": "화가 (rassom)", "is_correct": False},
                 {"text": "등산 안내인 (tog' yo'lboshchisi)", "is_correct": False},
                 {"text": "결혼식 사회자 (to'y boshlovchisi)", "is_correct": False},
             ],
             "explanation": """
<p>Belgilar: 사진을 <strong>찍는</strong> (suratga oladi — asosiy fe'l!) + 빛 (yorug'lik) +
결혼식/가족 행사 사진 + 자연 풍경 → <mark style="background:#dcfce7;">사진작가</mark> ✅.
② rassom ham yorug'lik bilan ishlaydi, lekin 찍다 fe'li faqat suratga tegishli (그리다
bo'lardi!); ④ to'yda bo'ladi, lekin surat olmaydi. Kasbni <strong>fe'l</strong> hal qiladi:
찍다 → fotograf, 그리다 → rassom, 고치다 → usta.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 좋은 사진을 찍는 특별한 비결이 있을까요?<br>
    <em style="color:#475569;">Yaxshi surat olishning maxsus siri bormi?</em></p>
    <p><strong>남자:</strong> 빛이 가장 중요합니다. 그래서 저는 해가 뜨기 전에 미리 가서 기다려요.
    결혼식이나 가족 행사 사진도 찍지만 제가 제일 좋아하는 것은 자연 풍경을 찍는 일이에요. 좋은
    순간은 기다리는 사람에게만 오니까요.<br>
    <em style="color:#475569;">Eng muhimi — yorug'lik. Shuning uchun quyosh chiqishidan oldin
    borib kutaman. To'y va oilaviy tadbirlar suratini ham olaman, lekin eng yoqtirganim — tabiat
    manzaralarini suratga olish. Yaxshi lahza faqat kutgan odamga keladi-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>30-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "남자는 자연 풍경 찍는 것을 제일 좋아한다. (Erkak eng ko'p tabiat manzarasini suratga olishni yoqtiradi.)", "is_correct": True},
                 {"text": "남자는 해가 뜬 후에 도착한다. (Erkak quyosh chiqqandan keyin yetib boradi.)", "is_correct": False},
                 {"text": "남자는 결혼식 사진은 찍지 않는다. (Erkak to'y suratini olmaydi.)", "is_correct": False},
                 {"text": "남자는 빛이 중요하지 않다고 생각한다. (Erkak yorug'lik muhim emas deb hisoblaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (해가 뜨기 <strong>전에</strong> 미리 가서 — chiqishidan OLDIN!),
③ ~도/~만 almashinuvi (결혼식 사진<strong>도</strong> 찍지만 — oladi ham!), ④ birinchi
jumlaga zid (빛이 가장 <strong>중요합니다</strong>). ✅ ①: 제일 좋아하는 것은 자연 풍경.
Intervyu bloki yakunlandi — 1–30 savollar to'liq sizniki! Keyingi bekat: munozara va
rasmiy nutq (31–36). 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">한복</div><div class="pp-card-back">hanbok (milliy libos)</div></div>
  <div class="pp-card"><div class="pp-card-front">소매를 줄이다</div><div class="pp-card-back">yengni kaltalatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">주머니를 달다</div><div class="pp-card-back">cho'ntak qadamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">일상</div><div class="pp-card-back">kundalik hayot</div></div>
  <div class="pp-card"><div class="pp-card-front">사진을 찍다</div><div class="pp-card-back">suratga olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">해가 뜨다</div><div class="pp-card-back">quyosh chiqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">풍경</div><div class="pp-card-back">manzara</div></div>
  <div class="pp-card"><div class="pp-card-front">순간</div><div class="pp-card-back">lahza</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Kirish jumlasi — xarita: mavzu, kasb, necha yillik tajriba — hammasi shu yerda.</li>
  <li>"A도 중요하지만 B도 중요하다" — javob muvozanatni saqlagan variantda.</li>
  <li>Kasbni fe'l aytadi: 찍다/그리다/고치다/모시다 — ob'ekt+fe'l juftini oving.</li>
  <li>Kichik farqlar katta: 줄이다⇄늘리다, ~도⇄~만, 전에⇄후에.</li>
</ul>
"""},
        ],
    },
]
