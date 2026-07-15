# TOPIK II Reading — 3–4-savollar: Ma'nodosh iboralar (의미가 비슷한 것),
# lessons 1–4 (orders 50–53).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_similar_1_4.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "3–4-savollar: Ma'nodosh iboralar (의미가 비슷한 것)",
    "summary": "Tagiga chizilgan iboraga ma'nosi eng yaqin variantni topish — yuqori chastotali juftliklar.",
    "icon":    "bi-arrow-left-right",
    "order":   3,
}

LESSONS = [
    # ── Lesson 1 (order 50) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 비슷한 의미 1: 3–4-savollar bilan tanishuv",
        "summary": "Tagiga chizilgan ibora savollari qanday ishlaydi va 'juftlik' usuli bilan qanday yechiladi.",
        "order":   50,
        "blocks": [
            {"rich_text": """
<h2>↔️ 3–4-savollar: ma'nosi eng yaqinini toping</h2>
<p>1–2-savollardan keyin shakli sal boshqacha ikkita savol keladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Tagiga chizilgan qism bilan ma'nosi eng yaqin bo'lganini tanlang.</em></p>
</div>
<p>Gapda bitta grammatik ibora <u>tagiga chizib</u> beriladi, to'rt variantdan
<strong>o'sha iboraning "egizagi"</strong>ni topasiz:</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:12px 16px;margin:10px 0;">
  <p style="margin:0 0 8px;font-size:1.08em;">표가 없어서 우리는 다음 기차를 <u>기다릴 수밖에 없었다</u>.</p>
  <p style="margin:0;">① <mark style="background:#dcfce7;">기다려야 했다</mark> &nbsp; ② 기다린 적이 있다 &nbsp; ③ 기다리기로 했다 &nbsp; ④ 기다릴 뻔했다</p>
</div>
<p><strong>-(으)ㄹ 수밖에 없다</strong> = "boshqa iloji yo'q edi" = <strong>-아/어야 했다</strong>
("majbur edi"). Bu ikkisi — <mark style="background:#dbeafe;">ma'nodosh juftlik</mark>.
TOPIK har safar shu cheklangan juftliklar ro'yxatidan so'raydi!</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Bu savollar 1–2-savollardan farq qiladi: u yerda gapga mos
  shaklni <em>tanlagansiz</em>, bu yerda esa berilgan shaklning <em>ma'nosini bilish</em>
  sinaladi. Juftliklarni bilsangiz — 10 soniyada 2 ball.
</div>
"""},
            {"rich_text": """
<h3>Yechish usuli: avval ma'no, keyin variant</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — Chizilgan iborani o'zbekchaga o'giring.</strong> Variantlarga
    qaramasdan! "기다릴 수밖에 없었다 = kutishdan boshqa iloj yo'q edi". Ma'noni aniq
    bilmasangiz, gapning qolgan qismidan taxmin qiling (표가 없어서 — chipta yo'q edi...).</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — Har variantni ham o'giring va solishtiring.</strong>
    ① majbur edi ✓ ② kutgan tajribam bor ✗ ③ kutishga qaror qildim ✗ ④ sal bo'lmasa kutardim ✗.
    Ma'no bir xilmi — belgilang.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — Shaklga aldanmang.</strong> Tuzoq variantlar chizilgan iboraga
    <em>shaklan</em> o'xshaydi (수밖에/뻔했다 — ikkalasida ham fe'l+qo'shimcha), lekin ma'nosi
    boshqa. Taqqoslash mezoni — faqat <strong>ma'no</strong>, tashqi ko'rinish emas!</p>
  </div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Keyingi uch darsda eng ko'p so'raladigan <strong>~20 ta
  juftlik</strong>ni o'rganasiz. Har juftlikni flashcard qilib, ikki tomonini birga yodlang:
  "-기 마련이다 ⇄ -는 법이다". Bittasini ko'rsangiz, ikkinchisini qidirasiz — vassalom.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>사람은 누구나 나이가 들면 몸이 <u>약해지기 마련이다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Har qanday odam yoshi ulg'aysa, tanasi zaiflashishi tabiiy.</em></p>
</div>
""",
             "choices": [
                 {"text": "약해지는 법이다 (zaiflashishi tabiiy qonuniyat)", "is_correct": True},
                 {"text": "약해질 리가 없다 (zaiflashishi mumkin emas)", "is_correct": False},
                 {"text": "약해지면 안 된다 (zaiflashsa bo'lmaydi)", "is_correct": False},
                 {"text": "약해질 뻔했다 (sal bo'lmasa zaiflashardi)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi oltin juftlik: <strong>-기 마련이다 ⇄ -는 법이다</strong> — ikkalasi ham
"tabiiy, qonuniy holat, doim shunday bo'ladi" degani ✅. ② buning teskarisi ("bo'lishi
mumkin emas"), ③ taqiq, ④ "sal bo'lmasa" — yaqin ham kelmaydi. 마련 so'zini ko'rdingizmi —
javobda 법 ni qidiring (va aksincha)!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>회의가 길어져서 점심 식사를 <u>거를 수밖에 없었다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Majlis cho'zilib ketgani uchun tushlikni o'tkazib yuborishdan boshqa iloj yo'q edi.</em></p>
</div>
""",
             "choices": [
                 {"text": "거르기로 했다 (o'tkazib yuborishga qaror qildim)", "is_correct": False},
                 {"text": "걸러야 했다 (o'tkazib yuborishga majbur bo'ldim)", "is_correct": True},
                 {"text": "거른 적이 없다 (hech o'tkazib yubormaganman)", "is_correct": False},
                 {"text": "거를 뻔했다 (sal bo'lmasa o'tkazib yuborardim)", "is_correct": False},
             ],
             "explanation": """
<p>Yana o'sha juftlik: <strong>-(으)ㄹ 수밖에 없다 ⇄ -아/어야 했다</strong> ("boshqa iloj
yo'q" = "majbur") ✅. ① qaror — bu yerda tanlov yo'q edi; ④ 뻔했다 — "sal bo'lmasa" —
u holda tushlik <em>qilingan</em> bo'lardi, matnda esa qilinmagan. 거르다 — (ovqatni)
o'tkazib yubormoq — TOPIKda tez-tez chiqadigan fe'l, yodlab qo'ying.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">밑줄 친 부분</div><div class="pp-card-back">tagiga chizilgan qism</div></div>
  <div class="pp-card"><div class="pp-card-front">의미가 비슷하다</div><div class="pp-card-back">ma'nosi o'xshash</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 마련이다</div><div class="pp-card-back">tabiiy holda shunday bo'ladi</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 법이다</div><div class="pp-card-back">qonuniyat shunaqa (⇄ 기 마련이다)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ 수밖에 없다</div><div class="pp-card-back">boshqa iloj yo'q</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어야 하다</div><div class="pp-card-back">majbur, kerak (⇄ 수밖에 없다)</div></div>
  <div class="pp-card"><div class="pp-card-front">거르다</div><div class="pp-card-back">o'tkazib yubormoq (ovqat)</div></div>
  <div class="pp-card"><div class="pp-card-front">나이가 들다</div><div class="pp-card-back">yoshi ulg'aymoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>3–4-savollar: chizilgan iboraning <strong>ma'nodosh egizagini</strong> topish.</li>
  <li>Usul: avval iborani o'zingiz o'giring → keyin variantlarni birma-bir solishtiring.</li>
  <li>Shaklga emas, <strong>ma'noga</strong> qarang — tuzoqlar shaklan o'xshaydi.</li>
  <li>Birinchi ikki juftlik: 기 마련이다 ⇄ 는 법이다; 을 수밖에 없다 ⇄ 아야 하다.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 51) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 비슷한 의미 2: Sabab va vaqt juftliklari (-는 바람에, -자마자...)",
        "summary": "Sabab (-는 바람에 ⇄ -는 탓에, 덕분에) va vaqt (-자마자 ⇄ -기가 무섭게) juftliklari.",
        "order":   51,
        "blocks": [
            {"rich_text": """
<h2>🔗 Sabab va vaqt juftliklari</h2>
<p>1–2-savollar uchun o'rgangan oilalaringiz endi juftlik bo'lib qaytadi. Sabab
oilasida <strong>rang</strong> muhim: salbiymi, ijobiymi, neytralmi?</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 바람에 ⇄ -는 탓에</strong> — ikkalasi ham <mark style="background:#fee2e2;">salbiy</mark> sabab ("~ tufayli, kasr").</p>
  <p style="color:#475569;margin:0 0 10px;">늦잠을 잔 <u>바람에</u> 지각했다 = 늦잠을 잔 <u>탓에</u> 지각했다.</p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>덕분에 ⇄ 때문에(+ijobiy natija)</strong> — <mark style="background:#dcfce7;">ijobiy</mark> sabab.</p>
  <p style="color:#475569;margin:0 0 10px;">네 <u>덕분에</u> 합격했어 = 네가 도와줬기 <u>때문에</u> 합격했어.</p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-느라고 ⇄ 때문에(band bo'lish)</strong> — band bo'lib ulgurmaslik.</p>
  <p style="color:#475569;margin:0;">숙제를 하<u>느라고</u> 못 갔다 = 숙제 <u>때문에</u> 못 갔다.</p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-자마자 ⇄ -기가 무섭게</strong> — "~ bilanoq" (기가 무섭게 — kuchliroq: "~ tugashini kutmasdanoq").</p>
  <p style="color:#475569;margin:0 0 10px;">도착하<u>자마자</u> 전화했다 = 도착하<u>기가 무섭게</u> 전화했다.</p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄴ 채(로) ⇄ -(으)ㄴ 상태로</strong> — "~ holicha" (holat saqlangan).</p>
  <p style="color:#475569;margin:0;">신발을 신<u>은 채로</u> 들어갔다 = 신발을 신<u>은 상태로</u> 들어갔다. — <em>Poyabzalni yechmagan holicha kirdi.</em></p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> 바람에 ⇄ 탓에 almashadi, lekin <strong>덕분에 bilan almashmaydi</strong>:
  덕분에 faqat yaxshi natijada. "도와준 바람에 합격했다" — xato eshitiladi. Rang mos kelishi shart!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>갑자기 손님이 <u>오는 바람에</u> 집 청소를 끝내지 못했다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>To'satdan mehmon kelib qolgani tufayli uy tozalashni tugatolmadim.</em></p>
</div>
""",
             "choices": [
                 {"text": "온 덕분에 (kelgani sharofati bilan)", "is_correct": False},
                 {"text": "오는 탓에 (kelgani kasridan)", "is_correct": True},
                 {"text": "오는 김에 (kelgan bahonasida)", "is_correct": False},
                 {"text": "오자마자 (kelishi bilanoq)", "is_correct": False},
             ],
             "explanation": """
<p>Natija salbiy (tozalash tugamadi) → salbiy sabab juftligi:
<strong>-는 바람에 ⇄ -는 탓에</strong> ✅. ① 덕분에 — ijobiy rang, mos emas (mehmon kelgani
"sharofati bilan" ish bitmadi?!). ③ 김에 — "bahonasida" (asosiy ishga qo'shimcha ish),
④ vaqt juftligi — bu sabab emas.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>아이는 학교에서 <u>돌아오자마자</u> 냉장고 문을 열었다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Bola maktabdan qaytib kelishi bilanoq muzlatgich eshigini ochdi.</em></p>
</div>
""",
             "choices": [
                 {"text": "돌아오기가 무섭게 (qaytib kelar-kelmas)", "is_correct": True},
                 {"text": "돌아오기 전에 (qaytib kelishidan oldin)", "is_correct": False},
                 {"text": "돌아온 채로 (qaytib kelgan holicha)", "is_correct": False},
                 {"text": "돌아오는 동안 (qaytib kelayotgan davomida)", "is_correct": False},
             ],
             "explanation": """
<p>Vaqt juftligi: <strong>-자마자 ⇄ -기가 무섭게</strong> ("~ bilanoq / ~ar-~amas") ✅.
무섭다 (qo'rqinchli) so'zini ko'rib cho'chimang — 기가 무섭게 turg'un ibora bo'lib,
"juda tez, darhol" degani. ②④ vaqt yo'nalishi noto'g'ri, ③ 채로 — holat saqlanishi
(masalan "kiyimini yechmagan holicha").</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>어젯밤에 너무 피곤해서 불을 <u>켠 채로</u> 잠이 들었다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Kecha juda charchaganimdan chiroqni yoqqan holicha uxlab qolibman.</em></p>
</div>
""",
             "choices": [
                 {"text": "켜기 전에 (yoqishdan oldin)", "is_correct": False},
                 {"text": "켠 상태로 (yoniq holatida)", "is_correct": True},
                 {"text": "켜는 바람에 (yoqqanim tufayli)", "is_correct": False},
                 {"text": "켜자마자 (yoqishim bilanoq)", "is_correct": False},
             ],
             "explanation": """
<p>Holat juftligi: <strong>-(으)ㄴ 채(로) ⇄ -(으)ㄴ 상태로</strong> — "o'sha holat saqlanganicha" ✅.
Chiroq yoniq qoldi + uxlab qoldi. ④ 자마자 tuzoq: "yoqishim bilanoq uxladim" vaqtni bildiradi,
lekin "chiroq yoniq qolgani" ma'nosi yo'qoladi. 채로 ko'pincha shunday holatlar bilan keladi:
옷을 입은 채로 (kiyim bilan), 문을 연 채로 (eshik ochiqligicha), 안경을 쓴 채로 (ko'zoynak taqqan holicha).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어 (juftliklar!)</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-는 바람에</div><div class="pp-card-back">⇄ -는 탓에 (salbiy sabab)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 탓에</div><div class="pp-card-back">~ kasridan (salbiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">덕분에</div><div class="pp-card-back">⇄ 때문에 + ijobiy natija</div></div>
  <div class="pp-card"><div class="pp-card-front">-자마자</div><div class="pp-card-back">⇄ -기가 무섭게 (bilanoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기가 무섭게</div><div class="pp-card-back">~ar-~amas, darhol</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄴ 채로</div><div class="pp-card-back">⇄ -(으)ㄴ 상태로 (holicha)</div></div>
  <div class="pp-card"><div class="pp-card-front">-느라고</div><div class="pp-card-back">⇄ 때문에 (band bo'lib)</div></div>
  <div class="pp-card"><div class="pp-card-front">불을 켜다</div><div class="pp-card-back">chiroqni yoqmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Sabab juftliklarida <strong>rang</strong> hal qiladi: salbiy → 바람에⇄탓에; ijobiy → 덕분에.</li>
  <li>Vaqt: 자마자 ⇄ 기가 무섭게. Holat: 은 채로 ⇄ 은 상태로.</li>
  <li>Juftlikning ikkala tomonini birga yodlang — imtihonda biri chizilgan, biri javobda.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 52) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 비슷한 의미 3: Odat va 'sal bo'lmasa' juftliklari (-곤 하다, -을 뻔하다...)",
        "summary": "Odat (-곤 하다, -기 일쑤이다), taxminan yuz bergan (-을 뻔하다) va yasama holat (-는 척하다) juftliklari.",
        "order":   52,
        "blocks": [
            {"rich_text": """
<h2>🔁 Odat, "sal bo'lmasa" va "o'zini ~dek ko'rsatish"</h2>
<p>Bugungi juftliklar kundalik hayot hikoyalarida keladi — 3-savolning eng sevimli guruhi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-곤 하다 ⇄ 자주/가끔 -는다</strong> — takrorlanadigan odat.</p>
  <p style="color:#475569;margin:0 0 10px;">스트레스를 받으면 매운 음식을 먹<u>곤 한다</u> = <u>자주</u> 먹는다.</p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-기 일쑤이다 ⇄ -는 일이 많다</strong> — <mark style="background:#fee2e2;">yomon</mark> odat/holat tez-tez.</p>
  <p style="color:#475569;margin:0 0 10px;">아침을 거르<u>기 일쑤이다</u> = 거르<u>는 일이 많다</u>. — <em>Nonushtani tashlab ketish odat bo'lib qolgan.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄹ 뻔하다 ⇄ 거의 -(으)ㄹ 것 같았다 / 하마터면 ~</strong> — "sal bo'lmasa" (yuz bermagan!).</p>
  <p style="color:#475569;margin:0;">넘어질 <u>뻔했다</u> = <u>거의</u> 넘어질 <u>것 같았다</u>. — <em>Sal bo'lmasa yiqilardim (yiqilmadim).</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 척하다 ⇄ -는 체하다</strong> — "o'zini ~dek ko'rsatmoq" (yolg'ondan).</p>
  <p style="color:#475569;margin:0 0 10px;">자는 <u>척했다</u> = 자는 <u>체했다</u>. — <em>O'zini uxlaganday ko'rsatdi.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)려던 참이다 ⇄ 마침 -(으)려고 했다</strong> — "ayni ~moqchi bo'lib turgan edim".</p>
  <p style="color:#475569;margin:0;">지금 전화하<u>려던 참이었어</u> = <u>마침</u> 전화하<u>려고 했어</u>.</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> -(으)ㄹ 뻔하다 ning imzo hamrohi — <strong>하마터면</strong>
  ("sal bo'lmasa"): 하마터면 넘어질 뻔했다. Gapda 하마터면 ko'rinsa, chizilgan yoki javob
  bo'ladigan ibora deyarli aniq 뻔하다 oilasidan.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>저는 기분이 안 좋을 때 혼자 바다를 보러 <u>가곤 합니다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Kayfiyatim yo'q paytlarda yolg'iz dengizni ko'rgani borib turaman.</em></p>
</div>
""",
             "choices": [
                 {"text": "자주 갑니다 (tez-tez boraman)", "is_correct": True},
                 {"text": "갈 뻔합니다 (sal bo'lmasa boraman)", "is_correct": False},
                 {"text": "가는 척합니다 (borayotganday ko'rsataman)", "is_correct": False},
                 {"text": "가야 합니다 (borishim kerak)", "is_correct": False},
             ],
             "explanation": """
<p>Odat juftligi: <strong>-곤 하다 ⇄ 자주 -는다</strong> — "shunday holatlarda takror-takror
qilib turaman" ✅. ② 뻔하다 — yuz bermagan narsa; ③ 척하다 — yolg'on holat; ④ majburiyat.
-곤 하다 doim <strong>shart/holat</strong> bilan keladi: "~ paytlarda, ~ bo'lsa" + odat.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>아침에 서두르다가 계단에서 <u>넘어질 뻔했다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Ertalab shoshilayotib zinada sal bo'lmasa yiqilardim.</em></p>
</div>
""",
             "choices": [
                 {"text": "거의 넘어질 것 같았다 (deyarli yiqilay dedim)", "is_correct": True},
                 {"text": "넘어지곤 했다 (yiqilib turardim)", "is_correct": False},
                 {"text": "넘어진 적이 있다 (yiqilgan tajribam bor)", "is_correct": False},
                 {"text": "넘어지기로 했다 (yiqilishga qaror qildim)", "is_correct": False},
             ],
             "explanation": """
<p><strong>-(으)ㄹ 뻔했다 ⇄ 거의 -(으)ㄹ 것 같았다</strong> ✅ — muhimi: yiqilish
<strong>yuz bermagan</strong>! ②③ da esa yiqilish real yuz bergan (odat/tajriba) — bu
eng xavfli farq. 뻔했다 ni ko'rganda o'zingizdan so'rang: "ish bo'ldimi?" — Yo'q, faqat
oz qoldi. Javob ham xuddi shu ma'noni saqlashi kerak.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>동생은 숙제를 하기 싫어서 책상 앞에서 <u>공부하는 척했다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Ukam vazifa qilgisi kelmay, stol oldida o'zini o'qiyotganday ko'rsatdi.</em></p>
</div>
""",
             "choices": [
                 {"text": "공부하는 체했다 (o'qiyotganday ko'rsatdi)", "is_correct": True},
                 {"text": "공부하기 일쑤였다 (o'qimaslik odati bor edi)", "is_correct": False},
                 {"text": "공부할 수밖에 없었다 (o'qishga majbur edi)", "is_correct": False},
                 {"text": "공부하려던 참이었다 (ayni o'qimoqchi edi)", "is_correct": False},
             ],
             "explanation": """
<p>Eng oson juftlik: <strong>-는 척하다 ⇄ -는 체하다</strong> — so'zma-so'z bir xil,
"o'zini ~dek ko'rsatmoq" ✅. TOPIK bu juftlikni yaxshi ko'radi, chunki 척/체 ikkalasi
ham xuddi shunday qisqa. Boshqa ko'p keladiganlari: 아는 척하다 (bilag'onlik qilmoq),
못 본 척하다 (ko'rmaganga olmoq), 괜찮은 척하다 (o'zini yaxshi his qilayotganday ko'rsatmoq).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어 (juftliklar!)</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-곤 하다</div><div class="pp-card-back">⇄ 자주 -는다 (odat)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 일쑤이다</div><div class="pp-card-back">⇄ -는 일이 많다 (yomon odat)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ 뻔하다</div><div class="pp-card-back">⇄ 거의 ~ㄹ 것 같았다 (yuz bermagan!)</div></div>
  <div class="pp-card"><div class="pp-card-front">하마터면</div><div class="pp-card-back">sal bo'lmasa (+뻔했다)</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 척하다</div><div class="pp-card-back">⇄ -는 체하다 (o'zini ~dek ko'rsatmoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)려던 참이다</div><div class="pp-card-back">ayni ~moqchi bo'lib turgan edim</div></div>
  <div class="pp-card"><div class="pp-card-front">서두르다</div><div class="pp-card-back">shoshilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">계단</div><div class="pp-card-back">zina</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Odat: -곤 하다 (neytral) va -기 일쑤이다 (yomon odat) — javobda 자주 / -는 일이 많다.</li>
  <li>-을 뻔했다 = yuz <strong>bermagan</strong>; real yuz bergan variantlar (적이 있다, 곤 했다) — tuzoq.</li>
  <li>척 ⇄ 체 — tekin ball; 하마터면 ko'rinsa 뻔하다 ni qidiring.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 53) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 비슷한 의미 4: Qolgan juftliklar + aralash mashq",
        "summary": "-는 김에, -기 나름이다, -을 리가 없다, -아 봤자 juftliklari va imtihon uslubidagi yakuniy test.",
        "order":   53,
        "blocks": [
            {"rich_text": """
<h2>🏁 Oxirgi juftliklar to'plami</h2>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-는 김에 ⇄ -는 기회에</strong> — "~ bahonasida, ~ chiqqan ekanman".</p>
  <p style="color:#475569;margin:0 0 10px;">시장에 <u>간 김에</u> 과일도 샀다. — <em>Bozorga borgan ekanman, meva ham oldim.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-기 나름이다 ⇄ -에 달려 있다</strong> — "~ga bog'liq".</p>
  <p style="color:#475569;margin:0 0 10px;">성공은 노력하<u>기 나름이다</u> = 노력<u>에 달려 있다</u>.</p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄹ 리가 없다 ⇄ -(으)ㄹ 가능성이 없다</strong> — "bo'lishi mumkin emas".</p>
  <p style="color:#475569;margin:0;">그가 거짓말을 <u>할 리가 없다</u>. — <em>U yolg'on gapirishi mumkin emas.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-아/어 봤자 ⇄ -아/어도 (소용없다)</strong> — "~ qilganing bilan (foydasi yo'q)".</p>
  <p style="color:#475569;margin:0 0 10px;">지금 뛰어<u> 봤자</u> 못 탄다 = 뛰어<u>도</u> 못 탄다. — <em>Yugurganing bilan ulgurmaysan.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄹ 만하다 ⇄ -(으)ㄹ 가치가 있다</strong> — "~shga arziydi".</p>
  <p style="color:#475569;margin:0 0 10px;">이 영화는 <u>볼 만하다</u>. — <em>Bu kino ko'rishga arziydi.</em></p>
  <p style="font-size:1.1em;margin:0 0 4px;"><strong>-(으)ㄴ/는 셈이다 ⇄ -(으)ㄴ/는 것과 같다</strong> — "~ deb hisoblasa bo'ladi, deyarli ~".</p>
  <p style="color:#475569;margin:0;">거의 다 <u>끝난 셈이다</u>. — <em>Deyarli tugadi deb hisoblasa bo'ladi.</em></p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Shu 4 darsdagi ~20 juftlik TOPIK 3–4 savollarining
  mutlaq ko'pchiligini yopadi. Flashcardlarni haftada bir aylantirib turing —
  imtihon kuni bu 2 savol "sovg'a" bo'ladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>우체국에 <u>가는 김에</u> 은행에도 들러서 공과금을 냈다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Pochtaga borgan bahonasida bankka ham kirib, kommunal to'lovlarni to'ladim.</em></p>
</div>
""",
             "choices": [
                 {"text": "가는 기회에 (borgan fursatida)", "is_correct": True},
                 {"text": "가는 바람에 (borganim tufayli)", "is_correct": False},
                 {"text": "가기가 무섭게 (borar-bormas)", "is_correct": False},
                 {"text": "갈 수밖에 없어서 (borishga majbur bo'lib)", "is_correct": False},
             ],
             "explanation": """
<p><strong>-는 김에 ⇄ -는 기회에</strong>: bitta asosiy ish (pochta) chiqqanda, yo'l-yo'lakay
qo'shimcha ish (bank) ✅. ② 바람에 salbiy natija talab qiladi — to'lov to'lash salbiy emas;
③ vaqt tezligi; ④ majburiyat — hech biri "bahonasida" ma'nosini bermaydi. 들르다 —
yo'l-yo'lakay kirib o'tmoq (kalit fe'l, 김에 bilan juda ko'p keladi).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>여행이 즐거울지 아닐지는 준비하기 <u>나름이다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Sayohat maroqli bo'lish-bo'lmasligi tayyorgarlikka bog'liq.</em></p>
</div>
""",
             "choices": [
                 {"text": "준비에 달려 있다 (tayyorgarlikka bog'liq)", "is_correct": True},
                 {"text": "준비할 리가 없다 (tayyorlanishi mumkin emas)", "is_correct": False},
                 {"text": "준비하기 마련이다 (tayyorlanish tabiiy)", "is_correct": False},
                 {"text": "준비할 뻔했다 (sal bo'lmasa tayyorlanardi)", "is_correct": False},
             ],
             "explanation": """
<p><strong>-기 나름이다 ⇄ -에 달려 있다</strong> — "natija ~ga bog'liq" ✅. Imzo tuzilma:
"A인지 아닌지는 B기 나름이다" (A bo'lish-bo'lmasligi B ga bog'liq). ③ 마련이다 shaklan
o'xshasa ham ma'nosi boshqa ("tabiiy holat"). 달려 있다 so'zma-so'z "osilgan" — natija
shunga "osilib turibdi" deb eslab qoling!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>지금 아무리 후회해 <u>봤자</u> 지나간 시간은 돌아오지 않는다.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Hozir qancha afsuslanganing bilan o'tgan vaqt qaytib kelmaydi.</em></p>
</div>
""",
             "choices": [
                 {"text": "후회해도 (afsuslansang ham)", "is_correct": True},
                 {"text": "후회한 김에 (afsuslangan bahonasida)", "is_correct": False},
                 {"text": "후회하자마자 (afsuslanishing bilanoq)", "is_correct": False},
                 {"text": "후회하는 척해도 (afsuslanganday ko'rsatsang ham)", "is_correct": False},
             ],
             "explanation": """
<p><strong>-아/어 봤자 ⇄ -아/어도</strong> — "qilganing bilan baribir (foydasi yo'q)" ✅.
봤자 ning imzosi: keyin doim <strong>salbiy/foydasiz natija</strong> (소용없다, 안 된다,
못 한다). 아무리 bilan birga kelishi ham tez-tez uchraydi: 아무리 ~아 봤자. ④ ga ehtiyot:
척 qo'shilib ma'noni "yolg'on afsus"ga o'zgartiradi — ortiqcha ma'no qo'shilgan variant
har doim noto'g'ri.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 4 (yakuniy).</strong> 밑줄 친 부분과 의미가 가장 비슷한 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0;"><strong>성실한 민수 씨가 아무 말도 없이 회사를 <u>그만둘 리가 없다</u>.</strong></p>
  <p style="color:#475569;margin:6px 0 0;"><em>Vijdonli Minsu hech narsa demasdan ishdan ketishi mumkin emas.</em></p>
</div>
""",
             "choices": [
                 {"text": "그만둘 가능성이 없다 (ketish ehtimoli yo'q)", "is_correct": True},
                 {"text": "그만둘 수밖에 없다 (ketishdan boshqa iloji yo'q)", "is_correct": False},
                 {"text": "그만두기 마련이다 (ketishi tabiiy)", "is_correct": False},
                 {"text": "그만둔 셈이다 (ketgan hisoblanadi)", "is_correct": False},
             ],
             "explanation": """
<p><strong>-(으)ㄹ 리가 없다 ⇄ -(으)ㄹ 가능성이 없다</strong> — "aql bovar qilmaydi,
bo'lishi mumkin emas" ✅. 리 = sabab/mantiq: "bunday bo'lishiga mantiq yo'q".
②③ aksincha "albatta bo'ladi" tomonda, ④ "allaqachon bo'lgan hisob" — uchchalasi ham
ishonchsizlik ma'nosini bermaydi. Tabriklaymiz — 20 juftlik to'plami tugadi! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어 (juftliklar!)</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">-는 김에</div><div class="pp-card-back">⇄ -는 기회에 (bahonasida)</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 나름이다</div><div class="pp-card-back">⇄ -에 달려 있다 (bog'liq)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ 리가 없다</div><div class="pp-card-back">⇄ 가능성이 없다 (mumkin emas)</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어 봤자</div><div class="pp-card-back">⇄ -아/어도 (foydasi yo'q)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄹ 만하다</div><div class="pp-card-back">⇄ 가치가 있다 (arziydi)</div></div>
  <div class="pp-card"><div class="pp-card-front">-(으)ㄴ/는 셈이다</div><div class="pp-card-back">⇄ 것과 같다 (deb hisoblasa bo'ladi)</div></div>
  <div class="pp-card"><div class="pp-card-front">들르다</div><div class="pp-card-back">yo'l-yo'lakay kirib o'tmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그만두다</div><div class="pp-card-back">tashlamoq, bo'shamoq (ish)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>3–4-savollar = <strong>juftlik bilish</strong> savoli: ~20 juftlikni flashcardda aylantirib turing.</li>
  <li>Usul: chizilganini o'zingiz o'giring → variantlarni o'girib solishtiring → shaklga aldanmang.</li>
  <li>Imzolar: 하마터면→뻔했다, 아무리→봤자/아도, 인지 아닌지는→나름이다.</li>
  <li>Ortiqcha ma'no qo'shgan variant (척, 탓, 덕분 noto'g'ri rangda) — doim noto'g'ri.</li>
</ul>
"""},
        ],
    },
]
