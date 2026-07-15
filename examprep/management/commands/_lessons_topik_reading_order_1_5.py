# TOPIK II Reading — Q13–15 Gaplar tartibi (문장 배열, orders 30–32) +
# Q16–18 Bo'sh joy (빈칸, orders 33–34). Two topics in one file.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_order_1_5.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC_ARRANGE = {
    "title":   "13–15-savollar: Gaplar tartibi (문장 배열)",
    "summary": "Bog'lovchi so'zlar yordamida to'rt gapni to'g'ri tartibga solish.",
    "icon":    "bi-list-ol",
    "order":   6,
}

TOPIC_BLANK = {
    "title":   "16–18-savollar: Bo'sh joyni to'ldirish (빈칸)",
    "summary": "Matndagi bo'sh joyga mantiqan mos iborani topish.",
    "icon":    "bi-input-cursor",
    "order":   7,
}

LESSONS = [
    # ── Lesson 1 (order 30) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC_ARRANGE,
        "title":   "TOPIK 연결어 1: Bog'lovchi so'zlar — o'qishning yo'l belgilari",
        "summary": "그러나, 그래서, 게다가 kabi bog'lovchilar matn mantig'ini qanday ko'rsatadi — 13–18-savollarning poydevori.",
        "order":   30,
        "blocks": [
            {"rich_text": """
<h2>🚦 Bog'lovchilar — matnning yo'l belgilari</h2>
<p><strong>13–15-savollar</strong>da to'rtta gapni to'g'ri tartibga solasiz,
<strong>16–18-savollar</strong>da esa matndagi bo'sh joyni to'ldirasiz. Ikkalasining ham
kaliti bitta: <mark style="background:#dbeafe;">bog'lovchi so'zlar (연결어)</mark>.</p>
<p>Bog'lovchi — haydovchi uchun yo'l belgisi kabidir: 그러나 ko'rsangiz "oldinda burilish —
fikr teskarisiga o'zgaradi", 그래서 ko'rsangiz "oldinda natija keladi" deb bilasiz.
Bu belgilarni <strong>guruh-guruh</strong> o'rganamiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Qo'shish ➕</span></p>
  <p style="font-size:1.08em;margin:0 0 4px;"><strong>그리고</strong> — <em>va, keyin</em> · <strong>또한</strong> — <em>shuningdek</em> · <strong>게다가</strong> — <em>buning ustiga</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#ef4444;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Qarama-qarshilik 🔄</span></p>
  <p style="font-size:1.08em;margin:0 0 4px;"><strong>그러나 / 하지만 / 그렇지만</strong> — <em>lekin</em> · <strong>그런데</strong> — <em>lekin; darvoqe (mavzu buriladi)</em> · <strong>반면에</strong> — <em>aksincha, holbuki</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Sabab-natija ➡️</span></p>
  <p style="font-size:1.08em;margin:0 0 4px;"><strong>그래서</strong> — <em>shuning uchun</em> · <strong>그러므로 / 따라서</strong> — <em>demak, binobarin</em> · <strong>왜냐하면 ~기 때문이다</strong> — <em>chunki ~</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;"><span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:.85em;">Shart va izoh 💬</span></p>
  <p style="font-size:1.08em;margin:0 0 4px;"><strong>그러면</strong> — <em>unda, shunday qilsangiz</em> · <strong>예를 들면</strong> — <em>masalan</em> · <strong>즉</strong> — <em>ya'ni</em></p>
</div>
"""},
            {"rich_text": """
<h3>Har bir belgi jumlada qanday ishlaydi</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>열심히 준비했다. 그래서 시험에 합격했다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Astoydil tayyorlandim. Shuning uchun imtihondan o'tdim.</em> (sabab → natija)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>열심히 준비했다. 그러나 시험에 떨어졌다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Astoydil tayyorlandim. Lekin imtihondan yiqildim.</em> (kutilgan natijaning teskarisi)</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>이 식당은 음식이 맛있다. 게다가 값도 싸다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Bu oshxonaning taomi mazali. Buning ustiga narxi ham arzon.</em> (yaxshilikka yaxshilik qo'shildi)</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> 게다가 va 또한 doim <strong>bir xil yo'nalishdagi</strong> gaplarni
  qo'shadi: yaxshiga yaxshi, yomonga yomon. "Mazali. Buning ustiga qimmat" — deb bo'lmaydi!
  Bu qoida 문장 배열da juda asqotadi.
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> <strong>그런데</strong> ikki xil ishlaydi: (1) "lekin" ma'nosida;
  (2) mavzuni yangi tomonga burishda ("darvoqe"). Ikkalasida ham undan <em>keyin</em> yangi
  yoki kutilmagan ma'lumot keladi — birinchi gap bo'la olmaydi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> ( ) ichiga eng mos bog'lovchini tanlang.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>동생은 매일 새벽까지 공부했다. (        ) 원하는 대학에 합격했다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Ukam har kuni tonggacha o'qidi. (        ) istagan universitetiga kirdi.</em></p>
</div>
""",
             "choices": [
                 {"text": "그러나 (lekin)", "is_correct": False},
                 {"text": "그래서 (shuning uchun)", "is_correct": True},
                 {"text": "예를 들면 (masalan)", "is_correct": False},
                 {"text": "왜냐하면 (chunki)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap — sabab (tonggacha o'qish), ikkinchi gap — tabiiy natija (universitetga kirish).
Sabab → natija = <mark style="background:#dcfce7;">그래서</mark>. ✅ 그러나 bo'lganida natija
teskari bo'lardi (yiqilardi); 왜냐하면 esa aksincha — <em>oldin natija, keyin sabab</em>
kelganda ishlatiladi va gap ~기 때문이다 bilan tugaydi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> ( ) ichiga eng mos bog'lovchini tanlang.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>이 가방은 디자인이 예쁘다. (        ) 주머니가 많아서 아주 실용적이다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Bu sumkaning dizayni chiroyli. (        ) cho'ntagi ko'p bo'lgani uchun juda amaliy ham.</em></p>
</div>
""",
             "choices": [
                 {"text": "하지만 (lekin)", "is_correct": False},
                 {"text": "그러므로 (demak)", "is_correct": False},
                 {"text": "게다가 (buning ustiga)", "is_correct": True},
                 {"text": "그러면 (unda)", "is_correct": False},
             ],
             "explanation": """
<p>Ikkala gap ham sumkani <strong>maqtayapti</strong> (chiroyli + amaliy) — bir xil yo'nalish,
ustiga yangi afzallik qo'shilyapti → <mark style="background:#dcfce7;">게다가</mark>. ✅
하지만 bo'lganida ikkinchi gap kamchilik bo'lishi kerak edi ("lekin og'ir" kabi).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> ( ) ichiga eng mos bog'lovchini tanlang.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>저는 아침에 운동을 하지 않습니다. (        ) 저녁에는 꼭 한 시간씩 걷습니다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Men ertalab sport bilan shug'ullanmayman. (        ) kechqurun albatta bir soatdan yuraman.</em></p>
</div>
""",
             "choices": [
                 {"text": "그래서 (shuning uchun)", "is_correct": False},
                 {"text": "즉 (ya'ni)", "is_correct": False},
                 {"text": "왜냐하면 (chunki)", "is_correct": False},
                 {"text": "하지만 (lekin)", "is_correct": True},
             ],
             "explanation": """
<p>Birinchi gap inkor (ertalab yo'q), ikkinchisi tasdiq (kechqurun bor) — qarama-qarshi
yo'nalish → <mark style="background:#dcfce7;">하지만</mark>. ✅ Belgi so'zlarga qarang:
"~하지 않습니다 ... 꼭 ~합니다" juftligi deyarli doim qarama-qarshilik bog'lovchisini talab qiladi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">그리고</div><div class="pp-card-back">va, keyin</div></div>
  <div class="pp-card"><div class="pp-card-front">그러나 / 하지만</div><div class="pp-card-back">lekin</div></div>
  <div class="pp-card"><div class="pp-card-front">그래서</div><div class="pp-card-back">shuning uchun</div></div>
  <div class="pp-card"><div class="pp-card-front">그러므로 / 따라서</div><div class="pp-card-back">demak, binobarin</div></div>
  <div class="pp-card"><div class="pp-card-front">게다가</div><div class="pp-card-back">buning ustiga</div></div>
  <div class="pp-card"><div class="pp-card-front">그런데</div><div class="pp-card-back">lekin; darvoqe</div></div>
  <div class="pp-card"><div class="pp-card-front">반면에</div><div class="pp-card-back">aksincha, holbuki</div></div>
  <div class="pp-card"><div class="pp-card-front">즉</div><div class="pp-card-back">ya'ni</div></div>
  <div class="pp-card"><div class="pp-card-front">예를 들면</div><div class="pp-card-back">masalan</div></div>
  <div class="pp-card"><div class="pp-card-front">왜냐하면 ~기 때문이다</div><div class="pp-card-back">chunki ~</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Bog'lovchi — yo'l belgisi: keyingi gap qaysi tomonga burilishini oldindan aytadi.</li>
  <li>4 guruh: qo'shish (그리고·게다가) · qarshilik (그러나·반면에) · sabab-natija (그래서·따라서) · shart-izoh (그러면·즉).</li>
  <li>게다가/또한 faqat bir xil yo'nalishni qo'shadi; 그런데 dan keyin yangilik keladi.</li>
  <li>Bu belgilarsiz 13–18-savollarni yechib bo'lmaydi — keyingi darslarda ishga solamiz.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 31) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC_ARRANGE,
        "title":   "TOPIK 문장 배열 1: Gaplar tartibini topish metodi",
        "summary": "13–15-savollar: birinchi gapni aniqlash va zanjir belgilari (bog'lovchi, olmosh, takror) bilan tartiblash.",
        "order":   31,
        "blocks": [
            {"rich_text": """
<h2>🔗 13–15-savollar: gaplarni tartibga soling (문장 배열)</h2>
<p>Savol shakli doim bir xil: to'rtta gap (가)(나)(다)(라) aralash tartibda beriladi,
siz mantiqiy tartibni tanlaysiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음을 순서대로 맞게 배열한 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagilarni to'g'ri tartibda joylashtirilganini tanlang.</em></p>
</div>
<h3>Sirni oching: birinchi gap allaqachon aytilgan!</h3>
<p>Javob variantlariga qarang — ular odatda shunday boshlanadi:</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;">① <strong>(나)</strong>-(가)-(라)-(다) &nbsp;&nbsp; ② <strong>(나)</strong>-(라)-(가)-(다)<br>
  ③ <strong>(다)</strong>-(가)-(나)-(라) &nbsp;&nbsp; ④ <strong>(다)</strong>-(라)-(나)-(가)</p>
</div>
<p>To'rt variantda birinchi o'rinda faqat <strong>ikki xil gap</strong> turibdi — (나) yoki (다).
Demak butun ishning yarmi: <mark style="background:#dbeafe;">shu ikkovidan qaysi biri
birinchi gap bo'la olishini aniqlash</mark>. Qolganini zanjir o'zi ko'rsatadi.</p>
"""},
            {"rich_text": """
<h3>Birinchi gap qanday bo'ladi (va bo'lmaydi)</h3>
<p><strong>Birinchi gap</strong> — mavzuni ochib beruvchi umumiy gap. U hech narsaga "suyanmaydi".</p>
<p><strong>Birinchi bo'la olmaydi</strong> — boshqa gapga suyanadigan gaplar:</p>
<ul>
  <li><mark style="background:#fee2e2;">Bog'lovchi bilan boshlansa:</mark> 그래서, 하지만, 게다가,
  그러면... — bular oldingi gapni talab qiladi.</li>
  <li><mark style="background:#fee2e2;">Ko'rsatish olmoshi bilan boshlansa:</mark> 이/그/저 + ot
  (이 문제 — "bu muammo": qaysi muammo?! Demak muammo oldinroq aytilgan).</li>
  <li><mark style="background:#fee2e2;">~기 때문이다 bilan tugasa:</mark> bu "chunki"-gap,
  u doim biror da'vodan keyin keladi.</li>
</ul>
<h3>Zanjir belgilari (gapdan gapga o'tish)</h3>
<ol>
  <li><strong>Bog'lovchi:</strong> 그래서 → oldida sabab bor; 하지만 → oldida teskari fikr bor.</li>
  <li><strong>이/그 + ot:</strong> 이 방법 ("bu usul") → usul aytilgan gapdan keyin keladi.</li>
  <li><strong>Takrorlangan so'z:</strong> bir gap oxiridagi so'z keyingi gap boshida qaytadi
  (자전거... → 자전거로 다니니까...).</li>
</ol>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Tartibni topgach, <strong>albatta boshidan oxirigacha o'qib
  chiqing</strong>. Ravon "hikoya" bo'lsa — javob to'g'ri; biror joyda "sakrash" sezilsa —
  zanjirni qayta tekshiring.
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol — birga yechamiz</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 그래서 요즘은 아침에 일찍 일어나려고 노력한다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 나는 원래 밤늦게까지 텔레비전을 보는 습관이 있었다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 그랬더니 하루가 길어지고 건강도 좋아졌다.</p>
  <p style="margin:0;"><strong>(라)</strong> 하지만 아침에 일어나기가 너무 힘들었다.</p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam.</strong> Birinchi gapni qidiramiz. (가) — 그래서 bilan, (다) — 그랬더니
    ("shunday qilgan edim...") bilan, (라) — 하지만 bilan boshlanadi: uchchalasi ham suyanchiq
    talab qiladi. Qoladi <mark style="background:#dcfce7;">(나)</mark> — "Menda azaldan kech
    televizor ko'rish odati bor edi" — mustaqil, mavzuni ochadi. ✅</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam.</strong> (나)dan keyin nima? Kech yotish odati → tabiiy oqibati:
    <mark style="background:#dcfce7;">(라)</mark> "하지만 ertalab turish juda qiyin edi".
    하지만 bu yerda "odat bor edi, <em>lekin</em> muammo tug'dirardi" bog'lanishini beradi.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam.</strong> Muammo → yechim: <mark style="background:#dcfce7;">(가)</mark>
    "그래서 endi erta turishga harakat qilyapman". 그래서 muammoga javob. Oxirida
    <mark style="background:#dcfce7;">(다)</mark> "그랬더니 kunim uzayib, sog'ligim yaxshilandi" —
    natija. Javob: <strong>(나)-(라)-(가)-(다)</strong>. O'qib tekshiramiz: odat → muammo →
    harakat → natija. Ravon! ✅</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> 다음을 순서대로 맞게 배열한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 그래서 나는 지난달부터 자전거로 출근하기 시작했다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 요즘 기름값이 많이 올라서 걱정이 많았다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 게다가 아침 운동이 되니까 건강에도 좋다.</p>
  <p style="margin:0;"><strong>(라)</strong> 자전거로 다니니까 교통비가 거의 들지 않아서 좋다.</p>
</div>
""",
             "choices": [
                 {"text": "(나)-(가)-(라)-(다)", "is_correct": True},
                 {"text": "(나)-(라)-(가)-(다)", "is_correct": False},
                 {"text": "(가)-(나)-(다)-(라)", "is_correct": False},
                 {"text": "(나)-(가)-(다)-(라)", "is_correct": False},
             ],
             "explanation": """
<p><strong>1)</strong> Birinchi gap: (가) 그래서 va (다) 게다가 bilan boshlanadi — bo'lmaydi.
(라) yaxshilikni sanayapti (nimaga suyanib?). Mustaqil kirish — <strong>(나)</strong>
"benzin narxi oshib, tashvishda edim". <strong>2)</strong> Tashvish → yechim: (가) "그래서
o'tgan oydan velosipedda qatnay boshladim". <strong>3)</strong> Endi afzalliklar: avval
(라) "yo'l xarajati deyarli yo'q", keyin <strong>(다)</strong> "게다가 ertalabki sport ham —
salomatlikka foyda". 게다가 <em>ikkinchi</em> afzallikni qo'shadi, shuning uchun u (라)dan
keyin turadi. Javob: <strong>(나)-(가)-(라)-(다)</strong> ✅. Tarjima: tashvish → velosiped →
tejash → buning ustiga salomatlik.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">순서</div><div class="pp-card-back">tartib</div></div>
  <div class="pp-card"><div class="pp-card-front">배열하다</div><div class="pp-card-back">tartiblamoq, joylashtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">습관</div><div class="pp-card-back">odat</div></div>
  <div class="pp-card"><div class="pp-card-front">노력하다</div><div class="pp-card-back">harakat qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그랬더니</div><div class="pp-card-back">shunday qilgan edim, ... (natija)</div></div>
  <div class="pp-card"><div class="pp-card-front">출근하다</div><div class="pp-card-back">ishga bormoq</div></div>
  <div class="pp-card"><div class="pp-card-front">교통비</div><div class="pp-card-back">yo'l xarajati</div></div>
  <div class="pp-card"><div class="pp-card-front">기름값</div><div class="pp-card-back">benzin narxi</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Variantlar birinchi gapni <strong>2 tagacha</strong> qisqartirib beradi — shulardan tanlang.</li>
  <li>그래서/하지만/게다가 yoki 이/그+ot bilan boshlangan gap birinchi bo'lolmaydi.</li>
  <li>Zanjir: bog'lovchi + ko'rsatish olmoshi + takror so'z. Oxirida to'liq o'qib tekshiring.</li>
  <li>Tipik syujet: <strong>holat → muammo → harakat/yechim → natija</strong>.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 32) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC_ARRANGE,
        "title":   "TOPIK 문장 배열 2: Amaliyot — uch xil syujet",
        "summary": "Hikoya, tushuntirish va muammo-yechim turidagi 문장 배열 savollarini ketma-ket ishlash.",
        "order":   32,
        "blocks": [
            {"rich_text": """
<h2>💪 문장 배열: amaliyot darsi</h2>
<p>Metodni bilasiz — endi qo'lni pishitamiz. TOPIKda 문장 배열 matnlari odatda uch xil
"syujet"da keladi:</p>
<ul>
  <li><strong>Hikoya (경험):</strong> voqea → qiyinchilik → davomi → xulosa/taassurot.</li>
  <li><strong>Tushuntirish (설명):</strong> da'vo → sabab (~기 때문이다) → misol/tafsilot → maslahat.</li>
  <li><strong>Muammo-yechim (문제-해결):</strong> hodisa → sababi → ko'rilgan chora → natija.</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Syujetni taniganingiz zahoti gaplar o'z o'rnini "o'zi so'rab"
  keladi. Har savolda o'zingizga ayting: bu hikoyami, tushuntirishmi yoki muammo-yechimmi?
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (hikoya).</strong> 다음을 순서대로 맞게 배열한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 지난 주말에 친구와 함께 처음으로 등산을 갔다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 정상에 올라가니 경치가 정말 아름다웠다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 하지만 올라가는 길이 생각보다 힘들었다.</p>
  <p style="margin:0;"><strong>(라)</strong> 그래도 포기하지 않고 끝까지 올라갔다.</p>
</div>
""",
             "choices": [
                 {"text": "(가)-(다)-(라)-(나)", "is_correct": True},
                 {"text": "(가)-(라)-(다)-(나)", "is_correct": False},
                 {"text": "(가)-(나)-(다)-(라)", "is_correct": False},
                 {"text": "(다)-(가)-(라)-(나)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap — (가): vaqt + voqea kirishi ("O'tgan hafta birinchi marta toqqa chiqdik").
Keyin qiyinchilik: (다) "하지만 yo'l o'ylagandan qiyin edi". Keyin bardosh: (라) "그래도
(shunga qaramay) taslim bo'lmay oxirigacha chiqdik". Mukofot oxirida: (나) "cho'qqiga
chiqsak — manzara go'zal!". <strong>(가)-(다)-(라)-(나)</strong> ✅ Hikoya syujeti:
voqea → qiyinchilik → bardosh → mukofot. (나) ni (다)dan oldin qo'ysangiz (③),
"go'zal edi, lekin qiyin edi, shunga qaramay chiqdik" — chiqib bo'lgach yana chiqib
bo'lmaydi-ku!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (tushuntirish).</strong> 다음을 순서대로 맞게 배열한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 왜냐하면 잠을 자는 동안 우리 몸이 낮의 피로를 풀기 때문이다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 그러므로 밤에는 휴대폰을 침대에서 멀리 두는 것이 좋다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 건강을 지키려면 무엇보다 잠을 충분히 자야 한다.</p>
  <p style="margin:0;"><strong>(라)</strong> 그런데 자기 전에 휴대폰을 보면 잠을 깊이 잘 수 없다.</p>
</div>
""",
             "choices": [
                 {"text": "(다)-(라)-(가)-(나)", "is_correct": False},
                 {"text": "(다)-(가)-(라)-(나)", "is_correct": True},
                 {"text": "(라)-(다)-(가)-(나)", "is_correct": False},
                 {"text": "(다)-(나)-(가)-(라)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap — (다): umumiy da'vo ("Salomatlik uchun yetarli uxlash kerak").
(가) 왜냐하면 bilan shu da'voning <strong>sababi</strong>ni beradi ("chunki uyquda tana
charchoqni chiqaradi") — demak (다)dan keyin darhol <strong>(가)</strong>. Keyin (라) 그런데
to'siqni kiritadi ("lekin yotishdan oldin telefon ko'rsangiz chuqur uxlab bo'lmaydi").
Oxirida (나) 그러므로 xulosa-maslahat ("shuning uchun telefonni uzoqroq qo'ying").
<strong>(다)-(가)-(라)-(나)</strong> ✅ Tushuntirish syujeti: da'vo → sabab → to'siq → maslahat.
①da (라) sababdan oldin kelib, 왜냐하면 zanjiri uziladi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (muammo-yechim).</strong> 다음을 순서대로 맞게 배열한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 이 문제를 해결하려고 시는 공원 곳곳에 쓰레기통을 더 설치했다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 최근 공원에 버려지는 쓰레기가 크게 늘었다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 그 결과 공원이 다시 깨끗해지기 시작했다.</p>
  <p style="margin:0;"><strong>(라)</strong> 쓰레기통이 부족해서 사람들이 쓰레기를 아무 데나 버렸기 때문이다.</p>
</div>
""",
             "choices": [
                 {"text": "(나)-(가)-(라)-(다)", "is_correct": False},
                 {"text": "(라)-(나)-(가)-(다)", "is_correct": False},
                 {"text": "(나)-(라)-(가)-(다)", "is_correct": True},
                 {"text": "(가)-(나)-(라)-(다)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap — (나): hodisa ("So'nggi paytda parkka tashlanadigan axlat ko'paydi").
(라) ~기 때문이다 bilan tugaydi — bu <strong>sabab-gap</strong>, hodisadan keyin keladi
("axlat qutisi kam bo'lgani uchun odamlar istalgan joyga tashlagan"). (가) <strong>이 문제</strong>
("bu muammo") deb boshlanadi — muammo aytilgandan keyingina kela oladi: "muammoni hal qilish
uchun shahar qo'shimcha qutilar o'rnatdi". (다) 그 결과 — natija: "park yana tozalana boshladi".
<strong>(나)-(라)-(가)-(다)</strong> ✅ Belgilarga qarang: ~기 때문이다 → sabab, 이 문제 →
oldinda muammo bor, 그 결과 → oxirgi o'rin.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">정상</div><div class="pp-card-back">cho'qqi</div></div>
  <div class="pp-card"><div class="pp-card-front">경치</div><div class="pp-card-back">manzara</div></div>
  <div class="pp-card"><div class="pp-card-front">그래도</div><div class="pp-card-back">shunga qaramay</div></div>
  <div class="pp-card"><div class="pp-card-front">포기하다</div><div class="pp-card-back">taslim bo'lmoq, voz kechmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">피로를 풀다</div><div class="pp-card-back">charchoqni chiqarmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">해결하다</div><div class="pp-card-back">hal qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">설치하다</div><div class="pp-card-back">o'rnatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그 결과</div><div class="pp-card-back">natijada</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Uch syujet: hikoya (voqea→qiyinchilik→bardosh→xulosa), tushuntirish (da'vo→sabab→to'siq→maslahat), muammo-yechim (hodisa→sabab→chora→natija).</li>
  <li>~기 때문이다 = sabab-gap; 이 문제/이 방법 = suyanadi; 그 결과/그러므로 = oxiriga yaqin.</li>
  <li>Har doim topilgan tartibda to'liq o'qib, "hikoya ravonligi"ni tekshiring.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 33) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC_BLANK,
        "title":   "TOPIK 빈칸 1: Bo'sh joyni to'ldirish metodi",
        "summary": "16–18-savollar: bo'sh joy atrofidagi belgi so'zlar orqali mos iborani topish usuli.",
        "order":   33,
        "blocks": [
            {"rich_text": """
<h2>⬜ 16–18-savollar: bo'sh joyni to'ldiring (빈칸 채우기)</h2>
<p>Savol shakli:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음을 읽고 (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagini o'qib, ( )ga kiradigan eng mos iborani tanlang.</em></p>
</div>
<p>2–3 gaplik matnda bitta joy bo'sh qoldiriladi. Bu <strong>lug'at testi emas — mantiq
testi</strong>: bo'sh joyga to'rttala variant ham grammatik jihatdan "sig'adi", lekin
faqat bittasi matn mantig'iga mos keladi.</p>
<h3>Metod: bo'sh joy — puzzle bo'lagi</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — Bo'sh joyning vazifasini aniqlang.</strong> Bo'sh joy oldidagi va
    keyingi gapni o'qing: bo'sh joy <em>sabab</em>mi, <em>natija</em>mi, <em>qarama-qarshilik</em>mi?
    Atrofdagi bog'lovchilar (그래서, 하지만, ~기 때문이다) buni aytib turadi.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — O'z so'zingiz bilan taxmin qiling.</strong> Variantlarga qaramasdan
    "bu yerga taxminan ... degan ma'no kelishi kerak" deb o'ylang. Keyin variantlardan
    taxminingizga eng yaqinini qidiring.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — Ikki tomonga tekshiring.</strong> Tanlagan variantni qo'yib, bo'sh
    joyning <em>oldi bilan ham, keyini bilan ham</em> mos kelishini tekshiring. Ko'p tuzoq
    variantlar faqat bir tomonga mos keladi!</p>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> <strong>오히려</strong> (aksincha), <strong>반대로</strong> (teskarisiga)
  so'zlari ko'rinsa — bo'sh joyga kutilganning <em>teskarisi</em> keladi. Bu 16–18-savollarning
  eng sevimli sinovi!
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">운동을 처음 시작할 때는 욕심을 부리지
  말아야 한다. 처음부터 무리하게 운동을 하면 몸에 오히려 (        ). 그러므로 가벼운
  운동부터 천천히 시작하는 것이 좋다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Sportni endi boshlaganda ochko'zlik qilmaslik kerak.
  Boshidanoq me'yordan ortiq shug'ullansangiz, tanaga aksincha (        ). Shuning uchun yengil
  mashqlardan sekin boshlagan ma'qul.</em></p>
</div>
<p>Tahlil: gap "무리하게 운동을 하면" (ortiqcha shug'ullansa) + <strong>오히려</strong> (aksincha) —
demak bo'sh joyga sport haqida kutilgan yaxshilikning <strong>teskarisi</strong>, ya'ni
<em>zarar</em> ma'nosi keladi: <strong>해가 될 수 있다</strong> (zarar bo'lishi mumkin).
Keyingi gap ham tasdiqlaydi: "그러므로 yengildan boshlang". Ikki tomonga mos! ✅</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">말을 잘하는 사람은 사실 잘 듣는 사람이다.
  상대방의 이야기를 잘 들어야 (        ) 알 수 있기 때문이다. 그래서 대화를 잘하고 싶으면
  먼저 듣는 연습부터 해야 한다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Gapga usta odam aslida yaxshi tinglovchi bo'ladi.
  Suhbatdoshning gapini yaxshi tinglagandagina (        ) bilib olish mumkin. Shuning uchun suhbatni
  yaxshilamoqchi bo'lsangiz, avval tinglashni mashq qiling.</em></p>
</div>
""",
             "choices": [
                 {"text": "상대방이 무엇을 원하는지 (suhbatdosh nimani xohlashini)", "is_correct": True},
                 {"text": "자기가 하고 싶은 말을 (o'zi aytmoqchi bo'lgan gapni)", "is_correct": False},
                 {"text": "말을 빨리 하는 방법을 (tez gapirish usulini)", "is_correct": False},
                 {"text": "듣기 시험 점수를 (tinglab tushunish balini)", "is_correct": False},
             ],
             "explanation": """
<p>Bo'sh joyning vazifasi: "yaxshi <strong>tinglash</strong> nimani bilishga imkon beradi?"
Tinglashdan keladigan bilim — <mark style="background:#dcfce7;">suhbatdosh nimani xohlashi</mark> ✅.
② o'z gapini bilish uchun tinglash shart emas; ③④ matn mavzusiga (suhbat odobi) mos kelmaydi —
ular faqat "gapirish/tinglash" so'ziga o'xshab aldaydi. ~아/어야 + ~ㄹ 수 있다 qolipi:
"...qilgandagina ... mumkin".</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">여행을 갈 때 짐이 많으면 몸도 마음도
  무거워진다. 꼭 필요한 것만 가져가면 (        ) 여행을 즐길 수 있다. 그러므로 짐을 싸기 전에
  물건 목록을 만들어 보는 것이 좋다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Sayohatga chiqqanda yuk ko'p bo'lsa, tana ham, ko'ngil ham
  og'irlashadi. Faqat zarur narsalarni olsangiz, (        ) sayohatdan zavq olishingiz mumkin.
  Shuning uchun yuk yig'ishdan oldin buyumlar ro'yxatini tuzib ko'rgan ma'qul.</em></p>
</div>
""",
             "choices": [
                 {"text": "더 많은 물건을 사면서 (ko'proq narsa sotib olib)", "is_correct": False},
                 {"text": "가볍고 편하게 (yengil va qulay holda)", "is_correct": True},
                 {"text": "짐을 더 무겁게 만들어 (yukni yanada og'irlashtirib)", "is_correct": False},
                 {"text": "집에서 쉬면서 (uyda dam olib)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap: yuk ko'p → og'ir. Bo'sh joyli gap buning <strong>qarama-qarshisi</strong>:
faqat keragini olsangiz → <mark style="background:#dcfce7;">yengil va qulay</mark> sayohat ✅.
①③ matn mantig'iga teskari (yuk kamaytirish haqida gap ketyapti), ④ esa umuman sayohatdan
chetga chiqib ketadi. 무겁다 ↔ 가볍다 juftligi — matn ichidagi qarama-qarshilik belgisi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">빈칸</div><div class="pp-card-back">bo'sh joy, katak</div></div>
  <div class="pp-card"><div class="pp-card-front">알맞다</div><div class="pp-card-back">mos kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">오히려</div><div class="pp-card-back">aksincha</div></div>
  <div class="pp-card"><div class="pp-card-front">무리하다</div><div class="pp-card-back">me'yordan oshirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">욕심을 부리다</div><div class="pp-card-back">ochko'zlik qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">해가 되다</div><div class="pp-card-back">zarar bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">상대방</div><div class="pp-card-back">suhbatdosh, qarshi tomon</div></div>
  <div class="pp-card"><div class="pp-card-front">목록</div><div class="pp-card-back">ro'yxat</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>빈칸 — mantiq testi: bo'sh joyning <strong>vazifasini</strong> (sabab/natija/qarshilik) aniqlang.</li>
  <li>Variantlarga qarashdan oldin javobni <strong>o'zingizcha taxmin qiling</strong>.</li>
  <li>Tanlovni bo'sh joyning <strong>ikki tomoni</strong> bilan tekshiring — tuzoqlar bir tomonlama mos.</li>
  <li>오히려/반대로 ko'rsangiz — kutilganning teskarisini qidiring.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 5 (order 34) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC_BLANK,
        "title":   "TOPIK 빈칸 2: Amaliyot + aralash mashq",
        "summary": "Qiyinroq 빈칸 savollari va 문장 배열 bilan aralash yakuniy mashq — butun mavzu jamlanadi.",
        "order":   34,
        "blocks": [
            {"rich_text": """
<h2>🏁 Yakuniy dars: 빈칸 + 문장 배열 aralash</h2>
<p>Bu darsda hammasi birga: qiyinroq 빈칸 savollari va bitta 문장 배열. Imtihondagidek —
har savolga <strong>1 daqiqadan</strong> mo'ljallang. Avval mustaqil yeching, keyin
tushuntirishni o'qing.</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> 13–18-savollar bloki uchun jami <strong>6 daqiqa</strong> —
  yetarli vaqt. Lekin bitta savolda 2 daqiqadan ortiq qolib ketsangiz, belgilab qo'yib
  keyinroq qaytish yaxshiroq: keyingi savollar osonroq bo'lishi mumkin.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (빈칸).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">책을 읽을 때는 내용을 그대로 받아들이기보다
  (        ) 읽는 것이 중요하다. 같은 문제라도 사람마다 생각이 다를 수 있기 때문이다.
  이렇게 읽으면 책 내용을 더 깊이 이해하게 된다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Kitob o'qiganda mazmunni shundayligicha qabul qilishdan
  ko'ra (        ) o'qish muhim. Chunki bitta masalada ham har kimning fikri har xil bo'lishi mumkin.
  Shunday o'qilsa, kitob mazmuni chuqurroq tushuniladi.</em></p>
</div>
""",
             "choices": [
                 {"text": "빠른 속도로 (tez sur'atda)", "is_correct": False},
                 {"text": "스스로 질문을 하면서 (o'ziga savol berib)", "is_correct": True},
                 {"text": "소리를 내면서 (ovoz chiqarib)", "is_correct": False},
                 {"text": "쉬지 않고 끝까지 (to'xtamasdan oxirigacha)", "is_correct": False},
             ],
             "explanation": """
<p>Belgi: <strong>~기보다</strong> (~dan ko'ra) — bo'sh joyga "shundayligicha qabul qilish"ning
<strong>muqobili</strong> keladi. Keyingi gap sababni beradi: "har kimning fikri har xil" —
ya'ni o'qiganda <mark style="background:#dcfce7;">o'z fikringizni, savolingizni</mark> qo'shish
kerak ✅. Tezlik (①), ovoz (③), to'xtamaslik (④) — "fikr har xilligi"ga hech qanday aloqasi yo'q.
Bo'sh joydan <em>keyingi</em> gap ko'pincha eng kuchli belgi bo'ladi!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (빈칸, 오히려 bilan).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">아이를 칭찬할 때는 결과보다 노력을 칭찬하는
  것이 좋다. "머리가 좋다"라는 칭찬을 자주 들은 아이는 어려운 문제를 만나면 오히려 (        ).
  실패해서 똑똑해 보이지 않는 것이 두렵기 때문이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Bolani maqtaganda natijadan ko'ra harakatni maqtagan
  yaxshi. "Aqlli ekansan" degan maqtovni tez-tez eshitgan bola qiyin masalaga duch kelsa, aksincha
  (        ). Chunki muvaffaqiyatsizlikka uchrab, aqlsiz ko'rinishdan qo'rqadi.</em></p>
</div>
""",
             "choices": [
                 {"text": "더 열심히 도전한다 (yanada astoydil urinadi)", "is_correct": False},
                 {"text": "포기하기 쉽다 (osongina taslim bo'ladi)", "is_correct": True},
                 {"text": "문제를 빨리 푼다 (masalani tez yechadi)", "is_correct": False},
                 {"text": "친구에게 물어본다 (do'stidan so'raydi)", "is_correct": False},
             ],
             "explanation": """
<p><strong>오히려</strong> — signal: "aqlli" maqtovidan kutilgan natija (yaxshi o'qish)ning
<strong>teskarisi</strong> keladi. Keyingi gap tasdiqlaydi: "aqlsiz ko'rinishdan qo'rqadi" —
qo'rqqan bola qiyin masaladan <mark style="background:#dcfce7;">qochadi/taslim bo'ladi</mark> ✅.
① aynan tuzoq — 오히려 bo'lmaganda to'g'ri bo'lardi! ③④ sabab-gap ("qo'rquv") bilan bog'lanmaydi.
Bu — real TOPIKda juda ko'p uchraydigan "psixologiya" mavzusidagi matn turi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (문장 배열).</strong> 다음을 순서대로 맞게 배열한 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>(가)</strong> 그러면 몸도 마음도 훨씬 가벼워진 것을 느낄 수 있다.</p>
  <p style="margin:0 0 6px;"><strong>(나)</strong> 현대인들은 스마트폰 없이 하루도 살기 어렵다.</p>
  <p style="margin:0 0 6px;"><strong>(다)</strong> 그래서 전문가들은 일주일에 하루는 스마트폰을 끄고 지내 보라고 말한다.</p>
  <p style="margin:0;"><strong>(라)</strong> 그러나 스마트폰을 오래 사용하면 눈과 목 건강에 좋지 않다.</p>
</div>
""",
             "choices": [
                 {"text": "(나)-(라)-(다)-(가)", "is_correct": True},
                 {"text": "(나)-(다)-(라)-(가)", "is_correct": False},
                 {"text": "(라)-(나)-(가)-(다)", "is_correct": False},
                 {"text": "(나)-(가)-(라)-(다)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi gap — (나): umumiy holat ("zamonaviy odam telefonsiz bir kun ham yashay olmaydi").
(라) 그러나 — muammo ("lekin uzoq ishlatish ko'z va bo'yinga zarar"). (다) 그래서 — mutaxassislar
maslahati ("haftada bir kun o'chirib ko'ring"). (가) 그러면 — maslahatga amal qilinsa natija
("shunda tana ham, ruh ham yengil tortadi"). <strong>(나)-(라)-(다)-(가)</strong> ✅
②da (다) 그래서 muammodan <em>oldin</em> kelib qoladi — "shuning uchun" nimaga suyanadi?
Zanjir uzilgan joyni shunday ushlaysiz.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">받아들이다</div><div class="pp-card-back">qabul qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">스스로</div><div class="pp-card-back">o'zi, mustaqil</div></div>
  <div class="pp-card"><div class="pp-card-front">칭찬하다</div><div class="pp-card-back">maqtamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">도전하다</div><div class="pp-card-back">urinmoq, bel bog'lamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">실패하다</div><div class="pp-card-back">muvaffaqiyatsizlikka uchramoq</div></div>
  <div class="pp-card"><div class="pp-card-front">두렵다</div><div class="pp-card-back">qo'rqinchli (qo'rqmoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">현대인</div><div class="pp-card-back">zamonaviy odam</div></div>
  <div class="pp-card"><div class="pp-card-front">전문가</div><div class="pp-card-back">mutaxassis</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li><strong>Bog'lovchilar</strong> — hamma narsaning kaliti: 4 guruhni yoddan biling.</li>
  <li><strong>문장 배열 (13–15):</strong> birinchi gapni variantlardan toping, zanjir belgilariga ergashing, oxirida to'liq o'qing.</li>
  <li><strong>빈칸 (16–18):</strong> bo'sh joy vazifasini aniqlang, o'zingizcha taxmin qiling, ikki tomonga tekshiring; 오히려 = teskari!</li>
  <li>Blokka 6 daqiqa; qotib qolsangiz — belgilang va keyinroq qayting.</li>
</ul>
"""},
        ],
    },
]
