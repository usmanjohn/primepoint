# TOPIK II Reading — 35–38-savollar: Matn mavzusi (주제 찾기),
# lessons 1–3 (orders 120–122).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_theme_1_3.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "35–38-savollar: Matn mavzusi (주제 찾기)",
    "summary": "Matnning bosh g'oyasini topish: soyabon testi va tor/keng javob tuzoqlari.",
    "icon":    "bi-bullseye",
    "order":   14,
}

LESSONS = [
    # ── Lesson 1 (order 120) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 주제 1: 35–38-savollar bilan tanishuv — soyabon testi",
        "summary": "Mavzu nima, u detaldan qanday farq qiladi va soyabon testi bilan qanday topiladi.",
        "order":   120,
        "blocks": [
            {"rich_text": """
<h2>🎯 35–38-savollar: matnning bosh g'oyasi</h2>
<p>To'rtta savol ketma-ket bir xil shaklda:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음 글의 주제로 가장 알맞은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi matnning mavzusi (bosh g'oyasi) sifatida eng mosini tanlang.</em></p>
</div>
<p>Bu 21–22-savollardagi 중심 생각ning katta akasi: matn kattaroq, variantlar ayyorroq.
Asosiy tamoyil o'zgarmaydi: <strong>mavzu — butun matnni bitta gapga siqqan xulosa</strong>,
birorta detal emas.</p>
<h3>☂️ Soyabon testi</h3>
<p>To'g'ri mavzu — <mark style="background:#dbeafe;">soyabon</mark>: matnning <strong>hamma</strong>
gaplari uning tagiga sig'ishi kerak. Tekshiruv oddiy:</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Test:</strong> Variantni o'qib, matnning har bir gapiga qarang:
  "bu gap shu g'oyaga xizmat qilyaptimi?" Hamma gap "ha" desa — soyabon to'g'ri.
  Bitta gap tashqarida qolsa — variant <strong>juda tor</strong>. Matnda isboti bo'lmagan
  narsani qamrasa — <strong>juda keng</strong>.
</div>
<h3>Mavzu qayerda turadi?</h3>
<ul>
  <li><strong>Oxirgi gap:</strong> 따라서/그러므로/이처럼 bilan xulosa — eng ko'p uchraydigan joy.</li>
  <li><strong>Birinchi gap:</strong> da'vo aytiladi, qolgani isbot (misol, tadqiqot).</li>
  <li><strong>Burilishdan keyin:</strong> 그러나/하지만dan keyin muallifning haqiqiy fikri (oldingisi — umumiy qarash).</li>
</ul>
"""},
            {"rich_text": """
<h3>Ishlangan misol</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">걷기는 특별한 장비 없이 누구나 쉽게
  할 수 있는 운동이다. 꾸준히 걷기만 해도 심장이 튼튼해지고 스트레스가 줄어든다는 연구
  결과가 많다. 게다가 걷기는 무릎에 주는 부담이 적어서 나이가 많은 사람도 안전하게 할 수
  있다. 이처럼 걷기는 간단하지만 그 효과가 뛰어난 운동이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Yurish — maxsus jihozsiz har kim oson qila oladigan
  mashq. Muntazam yurishning o'ziyoq yurakni mustahkamlab, stressni kamaytirishi haqida tadqiqotlar
  ko'p. Buning ustiga yurish tizzaga kam yuk tushirgani uchun keksalar ham bexavotir shug'ullana oladi.
  Shunday qilib, yurish — sodda, lekin samarasi yuqori mashq.</em></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — xulosa gapini toping:</strong> oxirgi gap <strong>이처럼</strong>
    (shunday qilib) bilan boshlanyapti — "yurish sodda, lekin samarali mashq". Mavzu nomzodi shu.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — soyabon testi:</strong> 1-gap (oson, hamma qiladi) ✔ sig'adi;
    2-gap (yurak, stress — samara) ✔; 3-gap (tizza, keksalar — yana osonlik/xavfsizlik) ✔.
    Hamma gap soyabon tagida!</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — tuzoqlarni tanib qo'yamiz:</strong> "걷기는 무릎에 부담이 적다" —
    to'g'ri fakt, lekin faqat 3-gapni qamraydi = <mark style="background:#fee2e2;">juda tor</mark>.
    "운동은 건강에 좋다" — hamma sportga tegishli, matn faqat yurish haqida =
    <mark style="background:#fee2e2;">juda keng</mark>. To'g'ri javob: "yurish — oson va samarali mashq".</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">아침을 거르면 뇌가 필요한 에너지를
  얻지 못해 오전 내내 집중력이 떨어진다. 실제로 아침을 먹는 학생들이 그렇지 않은 학생들보다
  성적이 좋다는 조사 결과도 있다. 바쁘더라도 간단한 과일이나 우유로라도 아침을 챙겨 먹는
  습관을 들일 필요가 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Nonushta qilinmasa, miya kerakli energiyani olmay,
  tush paytigacha diqqat pasayadi. Haqiqatan ham nonushta qiladigan o'quvchilarning bahosi
  qilmaydiganlardan yaxshi ekani haqida so'rov natijasi ham bor. Band bo'lsangiz ham hech bo'lmasa
  meva yoki sut bilan nonushta qilish odatini shakllantirish zarur.</em></p>
</div>
""",
             "choices": [
                 {"text": "아침 식사는 집중력과 공부에 중요하므로 챙겨 먹어야 한다. (Nonushta diqqat va o'qish uchun muhim — kanda qilmaslik kerak.)", "is_correct": True},
                 {"text": "과일과 우유는 몸에 좋은 음식이다. (Meva va sut foydali oziq-ovqat.)", "is_correct": False},
                 {"text": "학생들은 시험 성적을 올리려고 노력한다. (O'quvchilar bahosini oshirishga harakat qiladi.)", "is_correct": False},
                 {"text": "음식은 천천히 씹어 먹는 것이 좋다. (Ovqatni sekin chaynab yegan ma'qul.)", "is_correct": False},
             ],
             "explanation": """
<p>Xulosa gapi oxirida: "아침을 챙겨 먹는 습관을 들일 <strong>필요가 있다</strong>" (zarur!) —
mavzu shu ✅ ①. Soyabon testi: 1-gap (miya, diqqat) ✔, 2-gap (baho isboti) ✔, 3-gap
(tavsiya) ✔. ② juda tor — meva/sut faqat "hech bo'lmasa" misoli; ③ matn maqsadi emas;
④ matnda umuman yo'q. <strong>-ㄹ 필요가 있다 / -아야 한다</strong> bilan tugagan gap —
mavzuning tayyor manzili!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">요즘은 손으로 글씨를 쓰는 일이 점점
  줄고 있다. 하지만 손으로 쓰면 키보드로 입력할 때보다 내용이 기억에 더 오래 남는다는
  연구 결과가 있다. 손을 움직이는 동안 뇌가 정보를 더 깊이 처리하기 때문이다. 그러므로
  중요한 내용일수록 손으로 직접 써 보는 것이 좋다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Hozir qo'lda yozish tobora kamaymoqda. Lekin qo'lda
  yozilsa, klaviaturada terilganga qaraganda mazmun xotirada uzoqroq qolishi haqida tadqiqot bor.
  Chunki qo'l harakatlanayotganda miya ma'lumotni chuqurroq qayta ishlaydi. Shuning uchun muhim
  ma'lumotni qo'lda yozib ko'rgan ma'qul.</em></p>
</div>
""",
             "choices": [
                 {"text": "중요한 내용은 손으로 쓰면 기억에 더 잘 남는다. (Muhim mazmun qo'lda yozilsa, xotirada yaxshiroq qoladi.)", "is_correct": True},
                 {"text": "요즘 사람들은 글씨를 예쁘게 쓰지 못한다. (Hozirgi odamlar chiroyli yoza olmaydi.)", "is_correct": False},
                 {"text": "키보드로 입력하면 손으로 쓰는 것보다 빠르다. (Klaviaturada terish qo'lda yozishdan tez.)", "is_correct": False},
                 {"text": "뇌는 우리 몸에서 가장 중요한 기관이다. (Miya tanamizdagi eng muhim a'zo.)", "is_correct": False},
             ],
             "explanation": """
<p>Burilish belgisi: 1-gap umumiy holat, <strong>하지만</strong>dan keyin muallif fikri
boshlanadi, <strong>그러므로</strong> uni xulosalaydi → mavzu ① ✅. ② matnda yo'q
(kamayish bor, "chiroyli yozolmaslik" yo'q). ③ matnda aytilmagan (tezlik solishtirilmagan —
faqat xotira!). ④ juda keng — miya haqida umumiy gap, matn esa yozish usuli haqida.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">주제</div><div class="pp-card-back">mavzu, bosh g'oya</div></div>
  <div class="pp-card"><div class="pp-card-front">이처럼</div><div class="pp-card-back">shunday qilib (xulosa belgisi)</div></div>
  <div class="pp-card"><div class="pp-card-front">꾸준히</div><div class="pp-card-back">muntazam, uzluksiz</div></div>
  <div class="pp-card"><div class="pp-card-front">습관을 들이다</div><div class="pp-card-back">odat shakllantirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-ㄹ 필요가 있다</div><div class="pp-card-back">~sh zarur (mavzu belgisi)</div></div>
  <div class="pp-card"><div class="pp-card-front">처리하다</div><div class="pp-card-back">qayta ishlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">조사 결과</div><div class="pp-card-back">so'rov natijasi</div></div>
  <div class="pp-card"><div class="pp-card-front">부담</div><div class="pp-card-back">yuk, og'irlik</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Mavzu = butun matnni yopadigan <strong>soyabon</strong>; detal emas, umumiy bo'sh gap ham emas.</li>
  <li>Manzillari: 따라서/그러므로/이처럼 xulosasi, birinchi gap da'vosi, 하지만dan keyingi fikr.</li>
  <li>Soyabon testi: har gap variant tagiga sig'adimi? Bitta chiqib qolsa — tor; isbotsiz qamrasa — keng.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 121) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 주제 2: Tor va keng tuzoqlar laboratoriyasi",
        "summary": "Noto'g'ri variantlarning 4 turini (tor · keng · teskari · yo'q) nomma-nom tanib olish mashqi.",
        "order":   121,
        "blocks": [
            {"rich_text": """
<h2>🔬 Noto'g'ri variantlar laboratoriyasi</h2>
<p>35–38-savollarda noto'g'ri javoblar 4 turda yasaladi. Endi har amaliyotda ularni
<strong>nomma-nom</strong> aniqlaymiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;">🔹 <strong>Tor (좁음):</strong> matndagi to'g'ri fakt, lekin faqat bitta gapni qamraydi.</p>
  <p style="margin:0 0 6px;">🔹 <strong>Keng (넓음):</strong> matndan tashqariga chiqadigan umumiy hikmat.</p>
  <p style="margin:0 0 6px;">🔹 <strong>Teskari (반대):</strong> matn tanqid qilgan yoki rad etgan qarash.</p>
  <p style="margin:0;">🔹 <strong>Yo'q (없음):</strong> matnda umuman aytilmagan, "hayotda to'g'ri" gap.</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Eng xavflisi — <strong>tor</strong> variant: u matnda haqiqatan
  bor, shuning uchun "to'g'ri" tuyuladi. Farq savoli: "bu matnning <em>maqsadi</em>mi yoki
  <em>bitta g'ishti</em>mi?" G'isht — javob emas!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">실수를 대하는 태도는 조직의 분위기를
  결정한다. 실수한 사람을 심하게 혼내는 회사에서는 직원들이 실수를 숨기게 되고, 숨겨진
  실수는 나중에 더 큰 문제로 돌아온다. 반대로 실수를 배움의 기회로 여기는 회사에서는
  문제가 일찍 발견되어 빨리 해결된다. 실수에 너그러운 문화가 오히려 조직을 더 안전하게
  만드는 것이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Xatoga munosabat jamoa muhitini belgilaydi. Xato
  qilganni qattiq jazolaydigan kompaniyada xodimlar xatoni yashiradigan bo'ladi, yashirilgan xato esa
  keyin kattaroq muammo bo'lib qaytadi. Aksincha, xatoni o'rganish imkoni deb qaraydigan kompaniyada
  muammo erta topilib, tez hal bo'ladi. Xatoga bag'rikeng madaniyat, aksincha, jamoani xavfsizroq qiladi.</em></p>
</div>
""",
             "choices": [
                 {"text": "실수를 너그럽게 받아들이는 문화가 조직에 도움이 된다. (Xatoni kengbag'irlik bilan qabul qiladigan madaniyat jamoaga foyda keltiradi.)", "is_correct": True},
                 {"text": "실수한 직원은 심하게 혼내야 한다. (Xato qilgan xodimni qattiq jazolash kerak.)", "is_correct": False},
                 {"text": "숨겨진 실수는 나중에 더 큰 문제가 된다. (Yashirilgan xato keyin kattaroq muammoga aylanadi.)", "is_correct": False},
                 {"text": "회사는 직원을 자주 칭찬해야 한다. (Kompaniya xodimni tez-tez maqtashi kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Tuzoqlarni nomlaymiz: ② <strong>teskari</strong> — matn aynan shu yondashuvni tanqid
qiladi. ③ <strong>tor</strong> — matnda bor (2-gap!), lekin faqat bitta g'isht; soyabon testi:
3–4-gaplar (yaxshi madaniyat foydasi) uning tagiga sig'maydi. ④ <strong>yo'q</strong> —
maqtash haqida so'z yo'q (xatoga munosabat bor xolos). To'g'risi ① — oxirgi xulosa gapning
paraphrase'i ✅ (오히려 bilan kelgan xulosa — 19–20-darslardagi tanish signal!).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">식사 시간을 규칙적으로 지키는 것은
  생각보다 중요하다. 식사 시간이 불규칙하면 몸은 언제 음식이 들어올지 몰라서 들어온
  에너지를 지방으로 저장해 두려고 한다. 같은 양을 먹어도 불규칙하게 먹는 사람이 살이
  더 찌기 쉬운 이유이다. 건강을 위해서는 무엇을 먹는지만큼 언제 먹는지도 신경 써야 한다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Ovqat vaqtini muntazam saqlash o'ylagandan muhimroq.
  Ovqat vaqti tartibsiz bo'lsa, tana ovqat qachon kelishini bilmay, kirgan energiyani yog' sifatida
  g'amlab qo'yishga urinadi. Bir xil miqdor yeyilsa ham, tartibsiz ovqatlanadigan odamning tezroq
  semirishi sababi shu. Salomatlik uchun nima yeyishga qancha e'tibor berilsa, qachon yeyishga ham
  shuncha e'tibor berish kerak.</em></p>
</div>
""",
             "choices": [
                 {"text": "건강을 위해서는 규칙적인 식사 시간이 중요하다. (Salomatlik uchun muntazam ovqat vaqti muhim.)", "is_correct": True},
                 {"text": "살을 빼려면 음식을 적게 먹어야 한다. (Ozish uchun kam yeyish kerak.)", "is_correct": False},
                 {"text": "몸은 들어온 에너지를 지방으로 저장하기도 한다. (Tana kirgan energiyani yog' qilib saqlashi ham mumkin.)", "is_correct": False},
                 {"text": "모든 음식은 골고루 먹는 것이 좋다. (Hamma ovqatni barobar yegan yaxshi.)", "is_correct": False},
             ],
             "explanation": """
<p>① — birinchi gap (da'vo) + oxirgi gap (신경 써야 한다) ikkalasi ham shu g'oyani aytadi ✅.
② <strong>yo'q</strong>: matn miqdor haqida "같은 양을 먹어도" deydi — kam yeyish maslahati
yo'q. ③ <strong>tor</strong>: mexanizmning bitta bo'lagi (2-gap). ④ <strong>yo'q + keng</strong>:
"barobar yeyish" umumiy hikmat, matnda yo'q. Belgi: "A만큼 B도" (A qancha bo'lsa, B ham) —
muallifning asosiy urg'usi <strong>B</strong>da (qachon yeyish)!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">질문은 아는 것이 없어서 하는 것이
  아니다. 오히려 내용을 깊이 이해하려고 애쓸 때 좋은 질문이 나온다. 그래서 어떤 부모들은
  학교에서 돌아온 아이에게 "오늘 무엇을 배웠니?"가 아니라 "오늘 무슨 질문을 했니?"라고
  묻는다고 한다. 배움의 깊이는 질문의 깊이와 같다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Savol bilim yo'qligidan berilmaydi. Aksincha, mazmunni
  chuqur tushunishga intilganda yaxshi savol tug'iladi. Shuning uchun ba'zi ota-onalar maktabdan
  qaytgan bolasidan "Bugun nima o'rganding?" emas, "Bugun qanday savol berding?" deb so'rar ekan.
  Bilimning chuqurligi — savolning chuqurligiga teng.</em></p>
</div>
""",
             "choices": [
                 {"text": "질문하는 것은 깊이 있는 배움의 중요한 방법이다. (Savol berish — chuqur bilim olishning muhim usuli.)", "is_correct": True},
                 {"text": "모르는 것을 질문하는 일은 부끄러운 일이다. (Bilmaganini so'rash — uyat ish.)", "is_correct": False},
                 {"text": "아이에게 무엇을 배웠는지 매일 확인해야 한다. (Boladan har kuni nima o'rganganini tekshirish kerak.)", "is_correct": False},
                 {"text": "부모는 아이의 숙제를 도와줘야 한다. (Ota-ona bolaning vazifasiga yordam berishi kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Mavzu manzili — oxirgi gap: "배움의 깊이는 질문의 깊이와 같다" → savol = chuqur bilim
usuli ① ✅. ② <strong>teskari</strong> — matn buni birinchi gapdayoq rad etadi. ③ ayyor
<strong>teskari</strong>: matndagi misol aynan "nima o'rganding? <strong>emas</strong>" deydi —
"A가 아니라 B" qolipida A ni tanlagan variant doim tuzoq! ④ <strong>yo'q</strong>. Yodda
tuting: "A가 아니라 B" ko'rsangiz — javob B tomonda.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">태도</div><div class="pp-card-back">munosabat, yondashuv</div></div>
  <div class="pp-card"><div class="pp-card-front">너그럽다</div><div class="pp-card-back">bag'rikeng, kengfe'l</div></div>
  <div class="pp-card"><div class="pp-card-front">조직</div><div class="pp-card-back">tashkilot, jamoa</div></div>
  <div class="pp-card"><div class="pp-card-front">규칙적 / 불규칙</div><div class="pp-card-back">muntazam / tartibsiz</div></div>
  <div class="pp-card"><div class="pp-card-front">신경 쓰다</div><div class="pp-card-back">e'tibor bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">애쓰다</div><div class="pp-card-back">intilmoq, tirishmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">A만큼 B도</div><div class="pp-card-back">A qancha bo'lsa, B ham (urg'u B da)</div></div>
  <div class="pp-card"><div class="pp-card-front">깊이</div><div class="pp-card-back">chuqurlik</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>4 tuzoq turi: tor (bitta g'isht) · keng (matndan tashqari) · teskari (rad etilgan) · yo'q.</li>
  <li>Eng xavflisi tor variant — "matnning maqsadimi yoki g'ishtimi?" deb so'rang.</li>
  <li>"A가 아니라 B", "A만큼 B도" qoliplarida javob doim <strong>B</strong> tomonda.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 122) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 주제 3: Fikr-mulohaza matnlari (주장문) + aralash mashq",
        "summary": "Muallif nimadir talab qiladigan matnlarda mavzuni topish va yakuniy aralash amaliyot.",
        "order":   122,
        "blocks": [
            {"rich_text": """
<h2>🗣️ Fikr-mulohaza matni (주장문)</h2>
<p>35–38-savollarning ko'pchiligi — muallif biror narsaga <strong>chaqiradigan</strong>
matnlar: tabiatni asraylik, keksalarni o'ylaylik, boshlashdan qo'rqmaylik... Bunday matnda
mavzu = <strong>muallifning talabi</strong>, va u deyarli doim maxsus tugash bilan yoziladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>-아/어야 한다</strong> — kerak · <strong>-ㄹ 필요가 있다</strong> — zarur</p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>-는 것이 중요하다</strong> — muhim · <strong>-는 것이 좋다</strong> — ma'qul</p>
  <p style="font-size:1.08em;margin:0;"><strong>-에서 시작된다 / -에 달려 있다</strong> — ~dan boshlanadi / ~ga bog'liq</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Tezkor usul:</strong> Avval matndan shu tugashli gapni toping (ko'pincha oxirida).
  O'sha gap — mavzuning o'zi. Keyin soyabon testi bilan tasdiqlang. 35–38 blokiga jami
  <strong>6 daqiqa</strong> — shu usul bilan bemalol yetadi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">우리는 카페에서 무심코 일회용 컵을
  사용한다. 잠깐 쓰고 버려지는 컵 하나가 자연에서 썩는 데는 수십 년이 걸린다. 개인 컵을
  가지고 다니는 작은 습관만으로도 한 사람이 일 년에 수백 개의 일회용 컵을 줄일 수 있다.
  환경 보호는 거창한 일이 아니라 이런 작은 실천에서 시작된다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Biz kafeda beixtiyor bir martalik stakan ishlatamiz.
  Bir zum ishlatilib tashlanadigan bitta stakan tabiatda chirishi uchun o'nlab yillar ketadi. Shaxsiy
  stakan olib yurishdek kichik odatning o'ziyoq bir odamga yiliga yuzlab bir martalik stakanni
  kamaytirish imkonini beradi. Tabiatni asrash — ulkan ish emas, mana shunday kichik amaldan boshlanadi.</em></p>
</div>
""",
             "choices": [
                 {"text": "환경 보호는 생활 속 작은 실천에서 시작된다. (Tabiatni asrash turmushdagi kichik amaldan boshlanadi.)", "is_correct": True},
                 {"text": "일회용 컵은 오래 쓸 수 있어서 편리하다. (Bir martalik stakan uzoq ishlatilgani uchun qulay.)", "is_correct": False},
                 {"text": "카페에서는 일회용 컵 사용을 법으로 금지해야 한다. (Kafelarda bir martalik stakanni qonun bilan taqiqlash kerak.)", "is_correct": False},
                 {"text": "개인 컵은 다양한 디자인으로 판매되고 있다. (Shaxsiy stakanlar turli dizaynda sotilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Talab-tugashni qidiramiz: oxirgi gap "작은 실천<strong>에서 시작된다</strong>" +
"거창한 일이 <strong>아니라</strong>" (A가 아니라 B — javob B!) → ① ✅. ② so'zlar
buzilgan: "잠깐 쓰고 버려지는" (bir zum ishlatiladi!). ③ juda kuchli talab — matn
<strong>taqiq</strong> emas, shaxsiy odat haqida; matndan tashqariga chiqadi. ④ yo'q.
Diqqat: to'g'ri javob matndan <em>kuchliroq</em> talab qilsa ham noto'g'ri bo'ladi!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">요즘은 기차표 예매부터 음식 주문까지
  스마트폰 없이는 어려운 세상이 되었다. 그러나 스마트폰 사용이 익숙하지 않은 어르신들에게
  이런 변화는 높은 벽과 같다. 디지털 기술이 발전할수록 그 기술에서 소외되는 사람들을 함께
  배려해야 한다. 기술의 진짜 목적은 모든 사람의 생활을 편리하게 만드는 데 있기 때문이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Hozir poyezd chiptasini band qilishdan tortib ovqat
  buyurtma qilishgacha smartfonsiz qiyin zamon bo'ldi. Lekin smartfonga o'rganmagan keksalar uchun bu
  o'zgarish baland devor kabidir. Raqamli texnologiya rivojlangan sari undan chetda qolayotgan
  insonlarni ham birga o'ylashimiz kerak. Chunki texnologiyaning asl maqsadi — barchaning turmushini
  qulay qilish.</em></p>
</div>
""",
             "choices": [
                 {"text": "기술 발전에서 소외되는 사람들을 배려해야 한다. (Texnologiya rivojidan chetda qolayotganlarni o'ylash kerak.)", "is_correct": True},
                 {"text": "어르신들은 스마트폰을 배울 필요가 없다. (Keksalar smartfon o'rganishi shart emas.)", "is_correct": False},
                 {"text": "스마트폰으로 기차표를 예매하면 편리하다. (Smartfonda chipta band qilish qulay.)", "is_correct": False},
                 {"text": "스마트폰은 계속 새로 나오고 있다. (Smartfonlar to'xtovsiz yangilanmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Talab-gap aniq: "소외되는 사람들을 함께 <strong>배려해야 한다</strong>" → ① ✅
(keyingi gap 때문이다 bilan sababini beradi — mavzu-gapning eng ishonchli hamrohi).
② matnda yo'q va ruhiga teskari. ③ <strong>tor</strong> — 1-gapdagi misolning bo'lagi;
soyabon testi: 2–4-gaplar (keksalar, g'amxo'rlik) sig'maydi. ④ yo'q. 높은 벽과 같다
("baland devor kabi") — o'xshatishlar mavzu emas, his beruvchi bezak.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (yakuniy).</strong> 다음 글의 주제로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">많은 사람이 완벽한 계획을 세우느라
  시작을 미룬다. 그러나 아무리 훌륭한 계획도 실행하지 않으면 아무 소용이 없다. 일단
  작게라도 시작하면 부족한 부분은 해 나가면서 고칠 수 있다. 완벽한 준비를 기다리는 것보다
  불완전한 시작이 낫다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Ko'pchilik mukammal reja tuzaman deb boshlashni
  orqaga suradi. Lekin qanchalik zo'r reja bo'lmasin, amalga oshirilmasa foydasi yo'q. Kichik bo'lsa
  ham bir boshlansa, yetishmagan joyini yo'l-yo'lakay tuzatib borsa bo'ladi. Mukammal tayyorgarlikni
  kutgandan ko'ra nomukammal boshlash afzal.</em></p>
</div>
""",
             "choices": [
                 {"text": "완벽하게 준비될 때까지 기다리기보다 일단 시작하는 것이 낫다. (Mukammal tayyor bo'lguncha kutgandan ko'ra avval boshlagan afzal.)", "is_correct": True},
                 {"text": "계획을 세우는 것은 시간 낭비일 뿐이다. (Reja tuzish shunchaki vaqt isrofi.)", "is_correct": False},
                 {"text": "시작한 일은 반드시 끝까지 해내야 한다. (Boshlangan ishni albatta oxiriga yetkazish shart.)", "is_correct": False},
                 {"text": "부족한 부분은 시작하면서 고칠 수 있다. (Kamchiliklarni boshlagach tuzatib borsa bo'ladi.)", "is_correct": False},
             ],
             "explanation": """
<p>Mavzu-gap oxirida: "완벽한 준비를 기다리는 것<strong>보다</strong> 불완전한 시작이
<strong>낫다</strong>" (~보다 ~이 낫다 — solishtirib tavsiya!) → ① ✅. ② juda kuchli:
matn rejani "foydasiz" demaydi — <em>bajarilmasa</em> foydasiz deydi (shart tushib qolgan!).
③ yo'q — oxiriga yetkazish haqida gap yo'q. ④ eng ayyor <strong>tor</strong>: 3-gapning
o'zi, to'g'ri fakt — lekin bu isbot-g'isht, xulosa emas. Tabriklaymiz — mavzu topish
san'atini egalladingiz! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">주장</div><div class="pp-card-back">da'vo, fikr-talab</div></div>
  <div class="pp-card"><div class="pp-card-front">실천</div><div class="pp-card-back">amal, amalda bajarish</div></div>
  <div class="pp-card"><div class="pp-card-front">무심코</div><div class="pp-card-back">beixtiyor, o'ylamasdan</div></div>
  <div class="pp-card"><div class="pp-card-front">소외되다</div><div class="pp-card-back">chetda qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">배려하다</div><div class="pp-card-back">g'amxo'rlik qilmoq, o'ylamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">실행하다</div><div class="pp-card-back">amalga oshirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">미루다</div><div class="pp-card-back">orqaga surmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">A보다 B가 낫다</div><div class="pp-card-back">A dan ko'ra B afzal (mavzu qolipi)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>주장문da mavzu = muallif talabi; manzili: -아야 한다 / 필요가 있다 / 중요하다 / -에서 시작된다 / -보다 ~이 낫다.</li>
  <li>Soyabon testi har doim yakuniy hakam: hamma gap variant tagiga sig'sin.</li>
  <li>Matndan <strong>kuchliroq</strong> talab (금지해야 한다) ham xuddi tor javobdek noto'g'ri.</li>
  <li>"A가 아니라 B" / "A보다 B" / "A만큼 B도" — javob doim B tomonda!</li>
</ul>
"""},
        ],
    },
]
