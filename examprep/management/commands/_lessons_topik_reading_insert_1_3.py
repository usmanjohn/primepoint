# TOPIK II Reading — 39–41-savollar: Gap joylashtirish (문장 넣기),
# lessons 1–3 (orders 130–132).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_insert_1_3.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "39–41-savollar: Gap joylashtirish (문장 넣기)",
    "summary": "Berilgan <보기> gapini matndagi ㉠㉡㉢㉣ joylardan to'g'risiga qo'yish.",
    "icon":    "bi-box-arrow-in-down",
    "order":   15,
}

LESSONS = [
    # ── Lesson 1 (order 130) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문장 넣기 1: 39–41-savollar bilan tanishuv — 보기dan boshlang",
        "summary": "Gap joylashtirish savolining tuzilishi va <보기> gapidagi langarlar orqali joy topish usuli.",
        "order":   130,
        "blocks": [
            {"rich_text": """
<h2>📥 39–41-savollar: gapni joyiga qo'ying</h2>
<p>Savol shakli:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi matnda &lt;보기&gt; gapi kirishi uchun eng mos joyni tanlang.</em></p>
</div>
<p>Matn ichida to'rtta joy belgilangan: <strong>( ㉠ ) ( ㉡ ) ( ㉢ ) ( ㉣ )</strong>, pastda
esa <strong>&lt;보기&gt;</strong> qutisida bitta gap turadi. Vazifa — shu gap qaysi joyga
"chert" etib tushishini topish.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Tanish hunar:</strong> Bu 13–15-savollar (gaplar tartibi)ning teskarisi!
  U yerda zanjirni o'zingiz qurgansiz, bu yerda tayyor zanjirdagi <strong>bo'sh halqa</strong>ni
  topasiz. Zanjir belgilari o'sha-o'sha: bog'lovchi, olmosh, takror so'z.
</div>
<h3>Usul: matndan emas — 보기dan boshlang!</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — &lt;보기&gt;ni o'qib, langarlarini belgilang.</strong> Uch xil langar bor:
    <mark style="background:#dbeafe;">bog'lovchi boshi</mark> (그래서, 그러나, 예를 들어...),
    <mark style="background:#dbeafe;">이/그 + ot</mark> (이 방법, 그 결과 — nimadir oldin aytilgan!),
    <mark style="background:#dbeafe;">takror/maxsus so'z</mark> (matnda bir marta uchraydigan atama).</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — langar nimani talab qilishini ayting.</strong> 그래서 → oldida sabab
    bo'lishi shart. 이 방법 → oldida usul aytilgan bo'lishi shart. 실제로 → oldida isbotlanadigan
    da'vo bo'lishi shart. Endi matndan aynan shu "talab"ni qidirasiz.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — ikki tomonlama tekshiruv.</strong> Nomzod joyga 보기ni qo'yib,
    <strong>oldingi gap + 보기 + keyingi gap</strong>ni ketma-ket o'qing. Uchovi ravon oqsa —
    javob shu. Keyingi gap "sakrab" qolsa — boshqa joyni sinang.</p>
  </div>
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">소금은 오랫동안 돈처럼 사용되었다.
  <strong>( ㉠ )</strong> 옛날에는 소금을 구하기가 매우 어려웠기 때문이다.
  <strong>( ㉡ )</strong> 실제로 로마에서는 군인들에게 월급으로 소금을 주기도 했다.
  <strong>( ㉢ )</strong> 오늘날 월급을 뜻하는 영어 단어 '샐러리'도 소금을 뜻하는 말에서
  나왔다. <strong>( ㉣ )</strong></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 그래서 소금은 아무나 가질 수 없는 귀한 물건이었다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Shuning uchun tuz har kim ega bo'lolmaydigan qimmatbaho buyum edi.</em></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>Langar:</strong> 보기 <strong>그래서</strong> bilan boshlanadi → oldida
    <em>sabab</em> turishi shart: "nega qimmatbaho?"</p>
  </div>
  <div class="pp-step">
    <p><strong>Sababni qidiramiz:</strong> "소금을 구하기가 매우 <strong>어려웠기 때문이다</strong>"
    (topish qiyin edi) — mana sabab! Demak 보기 shu gapdan <strong>keyin</strong>: ㉡.</p>
  </div>
  <div class="pp-step">
    <p><strong>Ikki tomonlama tekshiruv:</strong> "...topish qiyin edi. → <em>Shuning uchun
    qimmatbaho edi.</em> → <strong>실제로</strong> Rimda askarlarga maosh sifatida tuz berilgan."
    실제로 (haqiqatan ham) — qimmatbaholikning isboti. Zanjir ravon: sabab → xulosa → dalil ✅.</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">낮잠은 오후의 피로를 줄여 주고 일의
  능률을 높여 준다. <strong>( ㉠ )</strong> 하지만 낮잠을 너무 오래 자면 오히려 밤잠을 방해할
  수 있다. <strong>( ㉡ )</strong> 그래서 전문가들은 20분 정도의 짧은 낮잠을 권한다.
  <strong>( ㉢ )</strong> 이 정도면 머리가 맑아지면서도 밤에 자는 데 문제가 생기지 않기
  때문이다. <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Kunduzgi uyqu tushdan keyingi charchoqni kamaytirib,
  ish unumini oshiradi. Lekin juda uzoq uxlansa, aksincha, tungi uyquga xalaqit berishi mumkin.
  Shuning uchun mutaxassislar 20 daqiqalik qisqa uyquni tavsiya qiladi. Shuncha bo'lsa bosh tiniqlashadi,
  tungi uyquga ham muammo bo'lmaydi.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 실제로 낮잠을 잔 사람들이 그렇지 않은 사람들보다 일에서 실수를 훨씬 적게 한다는 연구 결과도 있다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Haqiqatan ham kunduzi uxlab olganlar uxlamaganlardan ishda ancha kam xato qilishi haqida tadqiqot natijasi ham bor.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": True},
                 {"text": "㉡", "is_correct": False},
                 {"text": "㉢", "is_correct": False},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Langar: <strong>실제로 ... 연구 결과도 있다</strong> (haqiqatan ham ... tadqiqot ham bor) —
bu <em>dalil-gap</em>: oldida isbotlanadigan <strong>ijobiy da'vo</strong> bo'lishi shart.
Da'vo — 1-gap: "kunduzgi uyqu foydali" → 보기 ㉠ga tushadi ✅. Tekshiruv: undan keyingi gap
<strong>하지만</strong> bilan salbiy tomonga buriladi — dalildan keyin burilish tabiiy.
㉡㉢㉣ atrofida gap "uzoq uxlash zarari" va "20 daqiqa" haqida — u yerda bu dalil
zanjirni uzib qo'yadi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">보기</div><div class="pp-card-back">namuna, berilgan gap</div></div>
  <div class="pp-card"><div class="pp-card-front">들어가다</div><div class="pp-card-back">kirmoq (joyga tushmoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">실제로</div><div class="pp-card-back">haqiqatan ham (dalil belgisi)</div></div>
  <div class="pp-card"><div class="pp-card-front">능률</div><div class="pp-card-back">ish unumi, samaradorlik</div></div>
  <div class="pp-card"><div class="pp-card-front">권하다</div><div class="pp-card-back">tavsiya qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">방해하다</div><div class="pp-card-back">xalaqit bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">귀하다</div><div class="pp-card-back">qimmatbaho, noyob</div></div>
  <div class="pp-card"><div class="pp-card-front">연구 결과</div><div class="pp-card-back">tadqiqot natijasi</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Matndan emas, <strong>&lt;보기&gt;dan</strong> boshlang: langarini toping (bog'lovchi / 이·그+ot / maxsus so'z).</li>
  <li>Langar talabini ayting: 그래서→oldida sabab, 실제로→oldida da'vo, 이 방법→oldida usul.</li>
  <li><strong>Ikki tomonlama tekshiruv:</strong> oldingi gap + 보기 + keyingi gap ravon o'qilsin.</li>
  <li>Bu 13–15-savollarning teskarisi — zanjir belgilari bir xil.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 131) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문장 넣기 2: Uch langar turi — bog'lovchi, olmosh, davom",
        "summary": "보기 gapidagi uch xil langarni alohida mashq qilamiz: 그러나-turi, 이+ot turi va misol-davom turi.",
        "order":   131,
        "blocks": [
            {"rich_text": """
<h2>⚓ Uch langar turi</h2>
<p>39–41-savollardagi &lt;보기&gt; gaplari deyarli doim uch turdan biriga kiradi.
Har birini alohida mashq qilamiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">⚓ <strong>1-tur — Bog'lovchi langari:</strong> 그러나/하지만 (oldida qarama-qarshi fikr), 그래서/그러므로 (oldida sabab), 게다가/또한 (oldida bir xil yo'nalishdagi fikr).</p>
  <p style="margin:0 0 6px;">⚓ <strong>2-tur — Olmosh langari:</strong> 이 방법, 그 결과, 이런 현상... — "bu/o'sha" nimani ko'rsatayotgani matnda 보기dan <strong>oldin</strong> turishi shart.</p>
  <p style="margin:0;">⚓ <strong>3-tur — Davom langari:</strong> 심하면 (og'irlashsa), 例: yana bir misol... — 보기 mavjud ro'yxat/misollarni <strong>davom ettiradi</strong>.</p>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (bog'lovchi langari).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">걷기 여행은 자동차 여행과는 다른
  즐거움을 준다. <strong>( ㉠ )</strong> 천천히 걸으면 차를 타고 지나칠 때는 보이지 않던
  골목의 풍경이 눈에 들어온다. <strong>( ㉡ )</strong> 길에서 만난 사람들과 이야기를 나누는
  재미도 있다. <strong>( ㉢ )</strong> 그러므로 걷기 여행을 떠날 때는 하루에 다 보겠다는
  욕심을 버리고 일정을 여유 있게 짜는 것이 좋다. <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Piyoda sayohat mashina sayohatidan boshqacha zavq
  beradi. Sekin yursangiz, mashinada o'tib ketganda ko'rinmaydigan tor ko'chalar manzarasi ko'zga
  tashlanadi. Yo'lda uchragan odamlar bilan suhbatlashish gashti ham bor. Shuning uchun piyoda sayohatga
  chiqqanda "bir kunda hammasini ko'raman" degan ochko'zlikni tashlab, rejani bemalol tuzgan ma'qul.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 그러나 걷기 여행은 시간이 오래 걸려서 하루에 여러 곳을 볼 수는 없다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Lekin piyoda sayohat ko'p vaqt olgani uchun bir kunda ko'p joyni ko'rib bo'lmaydi.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": False},
                 {"text": "㉡", "is_correct": False},
                 {"text": "㉢", "is_correct": True},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Langar: <strong>그러나</strong> → oldida ijobiy fikrlar tugagan bo'lishi kerak; mazmuni
esa ("ko'p joy ko'rib bo'lmaydi") — kamchilik. Ijobiy zavqlar ㉡gacha davom etadi
(manzara + suhbat), demak burilish ㉢da ✅. Hal qiluvchi tekshiruv — <strong>keyingi gap</strong>:
"그러므로 ... 일정을 여유 있게" (shuning uchun rejani bemalol tuzing) — bu xulosa aynan
보기dagi kamchilikka tayanadi! 보기siz 그러므로 havoda qolardi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (olmosh langari).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">양파를 썰 때 눈물이 나는 것은 양파
  속의 매운 성분이 눈을 자극하기 때문이다. <strong>( ㉠ )</strong> 눈물을 줄이려면 양파를
  냉장고에 넣어 차갑게 만든 뒤에 써는 것이 좋다. <strong>( ㉡ )</strong> 물속에 양파를 담가
  두었다가 써는 것도 효과적이다. <strong>( ㉢ )</strong> 매운 성분이 물에 녹아서 공기 중으로
  퍼지지 못하기 때문이다. <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Piyoz to'g'raganda yosh oqishi — piyozdagi achchiq
  modda ko'zni ta'sirlashi sababli. Yoshni kamaytirish uchun piyozni muzlatgichga solib sovutib, keyin
  to'g'ragan ma'qul. Piyozni suvga botirib olib to'g'rash ham samarali. Chunki achchiq modda suvda erib,
  havoga tarqala olmaydi.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 차가워진 양파에서는 이 성분이 잘 퍼지지 않기 때문이다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Chunki sovugan piyozda bu modda yaxshi tarqalmaydi.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": False},
                 {"text": "㉡", "is_correct": True},
                 {"text": "㉢", "is_correct": False},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Ikki langar birga: <strong>이 성분</strong> (bu modda — oldin tilga olingan bo'lishi kerak)
+ <strong>차가워진 양파</strong> (sovugan piyoz — sovutish usuli aytilgan bo'lishi kerak) +
<strong>~기 때문이다</strong> (bu — sabab-gap, usulning izohi). Uchala talab ㉡da yig'iladi:
muzlatgich usulidan keyin, uning sababi sifatida ✅. Parallelizmga qarang: suv usulidan keyin
ham xuddi shunday 때문이다-gap turibdi — matn "usul → sababi" qolipida qurilgan
(28–31-darslardan tanish!).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (davom langari).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">우리 몸은 물이 부족하면 여러 가지
  신호를 보낸다. <strong>( ㉠ )</strong> 예를 들어 입술이 마르고 소변 색깔이 진해진다.
  <strong>( ㉡ )</strong> 문제는 이런 신호가 나타났을 때는 이미 몸에 물이 많이 부족한
  상태라는 점이다. <strong>( ㉢ )</strong> 그러므로 목이 마르지 않더라도 물을 자주 마시는
  습관을 들이는 것이 좋다. <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Tanamiz suv yetishmasa turli signallar beradi.
  Masalan, lab quriydi, siydik rangi to'qlashadi. Muammo shundaki, bu signallar ko'ringanda tanada
  suv allaqachon ancha kam bo'ladi. Shuning uchun chanqamagan bo'lsangiz ham suvni tez-tez ichish
  odatini shakllantirgan ma'qul.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 심하면 머리가 아프거나 어지럽기도 하다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Og'irlashsa, bosh og'rishi yoki aylanishi ham mumkin.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": False},
                 {"text": "㉡", "is_correct": True},
                 {"text": "㉢", "is_correct": False},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Langar: <strong>심하면 ... -기도 하다</strong> (og'irlashsa ... ham bo'ladi) — bu
<em>davom-gap</em>: mavjud belgilar ro'yxatini kuchliroq belgi bilan davom ettiradi.
Ro'yxat qayerda? ㉡dan oldin: "입술이 마르고 소변 색깔이..." (yengil belgilar) →
보기 (og'ir belgilar) → ㉡ ✅. Tekshiruv: keyingi gap "<strong>이런 신호</strong>가
나타났을 때" — "bu signallar" endi <em>hammasini</em> (yengil+og'ir) qamraydi. 보기ni
㉠ga qo'ysangiz, 예를 들어dan oldin misol kelib qoladi — zanjir buziladi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">자극하다</div><div class="pp-card-back">ta'sirlamoq, qo'zg'atmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">성분</div><div class="pp-card-back">tarkibiy modda</div></div>
  <div class="pp-card"><div class="pp-card-front">퍼지다</div><div class="pp-card-back">tarqalmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">신호</div><div class="pp-card-back">signal, belgi</div></div>
  <div class="pp-card"><div class="pp-card-front">심하면</div><div class="pp-card-back">og'irlashsa (davom langari)</div></div>
  <div class="pp-card"><div class="pp-card-front">어지럽다</div><div class="pp-card-back">boshi aylanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">일정을 짜다</div><div class="pp-card-back">reja tuzmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">여유 있게</div><div class="pp-card-back">bemalol, shoshilmasdan</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>⚓ Bog'lovchi langari: burilish/xulosa qayerdan boshlanishini aytadi — keyingi gapni ham tekshiring!</li>
  <li>⚓ Olmosh langari (이 성분, 그 결과): ko'rsatilgan narsa 보기dan <strong>oldin</strong> aytilgan bo'lishi shart.</li>
  <li>⚓ Davom langari (심하면, ~도 있다): mavjud ro'yxatning davomi — ro'yxat tugagan joyga tushadi.</li>
  <li>Bir 보기da bir nechta langar bo'lsa — hammasi bitta joyni ko'rsatishi kerak.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 132) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 문장 넣기 3: Qiyin holatlar + aralash mashq",
        "summary": "Savol-langar, keyingi gap langari va dalil-gap: eng qiyin joylashtirish holatlari bilan yakuniy mashq.",
        "order":   132,
        "blocks": [
            {"rich_text": """
<h2>🏁 Qiyin holatlar: langar 보기da emas — matnda!</h2>
<p>Ba'zan &lt;보기&gt;da ochiq bog'lovchi bo'lmaydi. Bunday paytda langarni
<strong>matnning o'zidan</strong> qidiring — qaysi gap 보기siz "havoda qolyapti"?</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">🧲 <strong>Savol-langar:</strong> 보기 savol bo'lsa (그렇다면 ~까?),
  u muammo bayonidan keyin, javobdan <strong>oldin</strong> turadi.</p>
  <p style="margin:0 0 6px;">🧲 <strong>Keyingi gap langari:</strong> matndagi biror gap 이렇게/이런 bilan
  boshlansa-yu, oldida mos narsa bo'lmasa — 보기 aynan o'sha yerga kiradi.</p>
  <p style="margin:0;">🧲 <strong>Dalil-gap:</strong> 실제로/연구에 따르면 bilan boshlangan 보기 —
  tegishli da'vodan keyin (1-darsdan eslaysiz).</p>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (savol-langar).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">조선 시대에는 여름에 얼음이 매우
  귀했다. <strong>( ㉠ )</strong> 겨울에 강에서 얼음을 잘라 서늘한 창고에 보관해 두었다가
  여름에 꺼내 쓴 것이다. <strong>( ㉡ )</strong> 이 창고가 바로 '석빙고'이다.
  <strong>( ㉢ )</strong> 석빙고는 바람이 통하는 특별한 구조로 되어 있어서 한여름에도 얼음이
  잘 녹지 않았다. <strong>( ㉣ )</strong> 조상들의 지혜를 잘 보여 주는 건축물이라고 할 수 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Choson davrida yozda muz juda noyob edi. Qishda
  daryodan muz kesib, salqin omborda saqlab, yozda chiqarib ishlatishgan. Bu ombor — "seokbinggo"dir.
  Seokbinggo shamol o'tadigan maxsus tuzilishga ega bo'lgani uchun qoq yozda ham muz erimay turgan.
  Ajdodlar donoligini yaqqol ko'rsatadigan inshoot deyish mumkin.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 그렇다면 냉장고도 없던 시대에 어떻게 여름까지 얼음을 보관할 수 있었을까?</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Unday bo'lsa, muzlatgich ham bo'lmagan zamonda muzni yozgacha qanday saqlashgan?</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": True},
                 {"text": "㉡", "is_correct": False},
                 {"text": "㉢", "is_correct": False},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>보기 — <strong>savol</strong> (그렇다면 ... ~을까?). Savol-langar qoidasi: muammo/holat
bayonidan keyin, <strong>javobdan oldin</strong>. Holat — 1-gap (muz noyob edi), javob —
2-gap (qishda kesib, omborda saqlashgan) → savol o'rtasiga: ㉠ ✅. Tekshiruv: "muz noyob edi.
→ <em>Qanday saqlashgan?</em> → Qishda kesib saqlashgan <strong>것이다</strong>" —
~은 것이다 tugashi aynan savolga javob ohangi! 보기siz bu 것이다 havoda qolardi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (keyingi gap langari).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">'플로깅'은 달리기를 하면서 길가의
  쓰레기를 줍는 운동이다. <strong>( ㉠ )</strong> 이렇게 널리 퍼진 데에는 이유가 있다.
  <strong>( ㉡ )</strong> 쓰레기를 줍기 위해 앉았다 일어나는 동작이 더해져서 그냥 달릴
  때보다 운동 효과가 크기 때문이다. <strong>( ㉢ )</strong> 게다가 운동을 하면서 동네까지
  깨끗해지니 일석이조라고 할 수 있다. <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>"Plogging" — yugurish asnosida yo'l chetidagi
  axlatni terish mashqi. Bunchalik keng tarqalishining sababi bor. Axlat terish uchun o'tirib-turish
  harakati qo'shilgani tufayli oddiy yugurishdan ko'ra mashq samarasi katta. Buning ustiga mashq qilib
  turib mahalla ham tozalanadi — bir o'q bilan ikki quyon.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 스웨덴에서 시작된 이 운동은 이제 세계 여러 나라에서 즐기는 운동이 되었다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Shvetsiyada boshlangan bu mashq endi dunyoning ko'p mamlakatlarida sevib bajariladigan mashqqa aylandi.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": True},
                 {"text": "㉡", "is_correct": False},
                 {"text": "㉢", "is_correct": False},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Bu safar hal qiluvchi langar <strong>matnda</strong>: 2-gap "<strong>이렇게</strong> 널리
퍼진 데에는..." (BUNchalik keng tarqalishining...) deb boshlanadi — lekin undan oldin
"tarqalish" haqida hech narsa yo'q! Havoda qolgan 이렇게 = bo'sh halqa. 보기 esa aynan
tarqalishni aytadi (세계 여러 나라로) → ㉠ ✅. Qoida: 보기ni o'qishdan keyin matnda
<strong>oldingisiz tushunilmaydigan gap</strong> bormi deb qarang — o'sha gapning oldi javob.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (dalil-gap).</strong> 다음 글에서 &lt;보기&gt;의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">박물관이나 미술관에서는 관람객에게
  사진을 찍을 때 플래시를 꺼 달라고 부탁한다. <strong>( ㉠ )</strong> 강한 빛이 그림의 색을
  조금씩 바래게 하기 때문이다. <strong>( ㉡ )</strong> 한 번의 플래시는 큰 문제가 없어
  보이지만 하루에 수천 명이 터뜨리는 플래시가 쌓이면 이야기가 달라진다. <strong>( ㉢ )</strong>
  그러므로 전시실에서 안내에 따라 플래시를 끄는 것은 소중한 작품을 지키는 일이 된다.
  <strong>( ㉣ )</strong></p>
  <p style="color:#475569;margin:8px 0 0;"><em>Muzey va galereyalarda tashrif buyuruvchilardan surat
  olayotganda chaqnamani (flash) o'chirishni so'rashadi. Chunki kuchli yorug'lik rasm rangini asta-sekin
  o'chiradi. Bitta chaqnama muammo emasdek ko'rinadi, lekin kuniga minglab odam chiqargan chaqnama
  yig'ilsa, gap boshqacha bo'ladi. Shuning uchun ko'rgazma zalida ko'rsatmaga amal qilib chaqnamani
  o'chirish — qimmatli asarni asrash demakdir.</em></p>
</div>
<div style="background:#fffbeb;border:2px dashed #f59e0b;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0;"><strong>&lt;보기&gt;</strong> 실제로 수백 년 된 그림이 빛 때문에 원래의 색을 잃어버린 경우도 있다.</p>
  <p style="color:#475569;margin:6px 0 0;"><em>Haqiqatan ham necha yuz yillik rasm yorug'lik tufayli asl rangini yo'qotgan holatlar ham bor.</em></p>
</div>
""",
             "choices": [
                 {"text": "㉠", "is_correct": False},
                 {"text": "㉡", "is_correct": False},
                 {"text": "㉢", "is_correct": True},
                 {"text": "㉣", "is_correct": False},
             ],
             "explanation": """
<p>Langar: <strong>실제로 ... 경우도 있다</strong> — dalil-gap. U qaysi da'voni isbotlaydi?
"chaqnama <strong>yig'ilsa</strong> gap boshqacha" (㉢dan oldingi gap) — katta zarar da'vosi.
Dalil shu da'vodan keyin: ㉢ ✅. Nega ㉡ emas? ㉡dagi gap hali "bitta chaqnama muammo emas"
bosqichida — u yerga qo'yilsa, dalil bilan keyingi gap ("bitta muammo emas") bir-biriga
qarama-qarshi bo'lib qoladi. Ikki tomonlama tekshiruv yana ishladi! Keyingi gap
그러므로 xulosa — dalildan keyin tabiiy yakun. Mavzu tamom — zanjir ustasi bo'ldingiz! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">그렇다면</div><div class="pp-card-back">unday bo'lsa (savol-langar)</div></div>
  <div class="pp-card"><div class="pp-card-front">보관하다</div><div class="pp-card-back">saqlamoq (omborda)</div></div>
  <div class="pp-card"><div class="pp-card-front">구조</div><div class="pp-card-back">tuzilish, konstruksiya</div></div>
  <div class="pp-card"><div class="pp-card-front">일석이조</div><div class="pp-card-back">bir o'q bilan ikki quyon</div></div>
  <div class="pp-card"><div class="pp-card-front">색이 바래다</div><div class="pp-card-back">rangi o'chmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">쌓이다</div><div class="pp-card-back">yig'ilmoq, to'planmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">관람객</div><div class="pp-card-back">tomoshabin, tashrif buyuruvchi</div></div>
  <div class="pp-card"><div class="pp-card-front">작품</div><div class="pp-card-back">asar</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Doimo &lt;보기&gt;dan boshlang: bog'lovchi / olmosh / davom langari nimani talab qiladi?</li>
  <li>보기da langar bo'lmasa — matndan "havoda qolgan" gapni qidiring (이렇게..., ~은 것이다, 그러므로...).</li>
  <li>Savol-보기: muammodan keyin, javobdan oldin. Dalil-보기 (실제로): da'vodan keyin.</li>
  <li>Yakuniy hakam — ikki tomonlama tekshiruv: oldingi gap + 보기 + keyingi gap ravon oqishi shart.</li>
</ul>
"""},
        ],
    },
]
