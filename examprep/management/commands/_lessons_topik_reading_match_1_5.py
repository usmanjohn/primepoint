# TOPIK II Reading — Mazmunga mos javob (내용 일치, Q9–12), lessons 1–5 (orders 20–24).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_match_1_5.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "9–12-savollar: Mazmunga mos javob (내용 일치)",
    "summary": "E'lon, grafik yoki matn mazmuniga mos keladigan gapni topish.",
    "icon":    "bi-check2-square",
    "order":   5,
}

LESSONS = [
    # ── Lesson 1 (order 20) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 1: 9–12-savollar bilan tanishuv",
        "summary": "Mazmunga mos gapni topish savollari qanday tuzilgan va ularni chizib tashlash usuli bilan yechish.",
        "order":   20,
        "blocks": [
            {"rich_text": """
<h2>✅ 9–12-savollar: mazmunga mos gapni toping</h2>
<p>Reklama savollaridan keyin <strong>9–12-savollar</strong> keladi. Ularning savol matni
har doim bir xil:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>다음 글 또는 그래프의 내용과 같은 것을 고르십시오.</strong></p>
  <p style="color:#475569;margin:0;"><em>Quyidagi matn yoki grafik mazmuni bilan bir xil bo'lgan gapni tanlang.</em></p>
</div>
<p>Sizga qisqa material beriladi va to'rtta gapdan <strong>faqat bittasi</strong> shu
materialga mos keladi. Material turi savol raqamiga qarab deyarli doim bir xil:</p>
<ul>
  <li><strong>9-savol:</strong> e'lon yoki plakat (안내문·포스터) — festival, kurs, tadbir...</li>
  <li><strong>10-savol:</strong> grafik yoki diagramma (그래프·도표)</li>
  <li><strong>11–12-savollar:</strong> qisqa yangilik yoki ma'lumot matni (신문 기사)</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> 5–8-savollarda <em>mavzuni</em> topgan bo'lsangiz, endi vazifa boshqa:
  <strong>faktlarni</strong> solishtirasiz. Bitta so'z emas — sana, raqam, joy, kim/nima
  qilgani muhim bo'ladi.
</div>
"""},
            {"rich_text": """
<h3>Asosiy usul: chizib tashlash (소거법)</h3>
<p>To'g'ri javobni "topish"dan ko'ra, <strong>noto'g'rilarni o'chirish</strong> tezroq va
ishonchliroq. Har bir variantni materialdan tekshirib, mos kelmaganini chizib tashlang:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — Avval variantlarni o'qing.</strong> Materialni emas! Har variantda
    <mark style="background:#dbeafe;">tekshiriladigan so'z</mark>ni belgilang: raqam, sana,
    joy, ish-harakat. Endi materialdan aynan nimani qidirishni bilasiz.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — Har variantni materialda tekshiring.</strong> Variantdagi kalit so'zni
    materialdan toping va yonma-yon solishtiring. Mos kelmasa — darhol chizing:
    <span style="text-decoration:line-through;">① 축제는 이틀 동안 열립니다</span>.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — Qolgan bittasini qayta tekshiring.</strong> To'g'ri javob odatda matndagi
    gapning <strong>boshqa so'zlar bilan aytilgani</strong> (paraphrase) bo'ladi: matnda
    입장료: 무료 bo'lsa, javobda 돈을 내지 않아도 됩니다 deyiladi. Ma'no bir xilmi? Belgilang!</p>
  </div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> To'g'ri javob hech qachon matndagi gapni <em>so'zma-so'z</em>
  takrorlamaydi. Agar variant matn bilan bir xil so'zlardan iborat bo'lsa — ehtiyot bo'ling,
  bu ko'pincha tuzoq: bitta kichik detali o'zgartirilgan bo'ladi.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.15em;margin:0 0 10px;"><strong>제10회 한강 불꽃 축제</strong></p>
  <ul style="margin:0;padding-left:18px;">
    <li>날짜: 10월 5일(토) 저녁 7시 ~ 9시</li>
    <li>장소: 한강 공원</li>
    <li>입장료: 무료</li>
  </ul>
  <p style="margin:10px 0 0;color:#64748b;">※ 비가 오면 다음 날 같은 시간에 열립니다.</p>
</div>
""",
             "choices": [
                 {"text": "축제는 이틀 동안 열립니다. (Festival ikki kun davom etadi.)", "is_correct": False},
                 {"text": "축제에 돈을 내지 않고 입장할 수 있습니다. (Festivalga pul to'lamasdan kirish mumkin.)", "is_correct": True},
                 {"text": "축제는 오전에 시작합니다. (Festival ertalab boshlanadi.)", "is_correct": False},
                 {"text": "비가 오면 축제가 취소됩니다. (Yomg'ir yog'sa festival bekor qilinadi.)", "is_correct": False},
             ],
             "explanation": """
<p>Chizib tashlaymiz: ① ikki kun? — yo'q, faqat 5-oktabr kechqurun. ③ ertalab? — yo'q,
저녁 7시 (kechki 7). ④ bekor qilinadi (취소)? — yo'q, <strong>다음 날 열립니다</strong>
(ertasi kuni o'tkaziladi — ya'ni ko'chiriladi, bekor emas!). Qoladi ② —
<strong>입장료: 무료</strong> ni javob <strong>돈을 내지 않고</strong> (pul to'lamasdan) deb
boshqa so'zlar bilan aytgan. Mana shu — paraphrase!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.7;">저는 주말마다 집 근처 도서관에 갑니다.
  도서관은 아침 9시에 문을 열고 저녁 6시에 닫습니다. 책은 한 사람이 한 번에 다섯 권까지
  2주일 동안 빌릴 수 있습니다. 저는 어제 소설책 세 권을 빌렸습니다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Men har dam olish kuni uyim yaqinidagi kutubxonaga boraman.
  Kutubxona ertalab 9 da ochilib, kechki 6 da yopiladi. Bir kishi bir vaqtda beshtagacha kitobni
  2 hafta muddatga olishi mumkin. Men kecha uchta roman oldim.</em></p>
</div>
""",
             "choices": [
                 {"text": "도서관은 저녁 9시까지 문을 엽니다. (Kutubxona kechki 9 gacha ishlaydi.)", "is_correct": False},
                 {"text": "책은 일주일 동안 빌릴 수 있습니다. (Kitobni bir hafta olish mumkin.)", "is_correct": False},
                 {"text": "저는 어제 책을 세 권 빌렸습니다. (Men kecha uchta kitob oldim.)", "is_correct": True},
                 {"text": "한 번에 책을 세 권까지 빌릴 수 있습니다. (Bir vaqtda uchtagacha kitob olish mumkin.)", "is_correct": False},
             ],
             "explanation": """
<p>Raqamlar tuzog'iga e'tibor bering! ① 9시 bor, lekin bu <em>ochilish</em> vaqti (아침),
yopilish emas. ② 2주일 (2 hafta), bir hafta emas. ④ <strong>다섯 권</strong> (5 ta)gacha
mumkin — "uchta" esa muallif <em>kecha olgani</em>. Variantlar ataylab matndagi raqamlarni
boshqa joyga qo'yadi. To'g'risi ③: 소설책 세 권을 빌렸습니다 = kecha 3 ta kitob oldi. ✅</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">내용</div><div class="pp-card-back">mazmun</div></div>
  <div class="pp-card"><div class="pp-card-front">같은 것</div><div class="pp-card-back">bir xil narsa (mos keladigani)</div></div>
  <div class="pp-card"><div class="pp-card-front">고르다</div><div class="pp-card-back">tanlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">열리다</div><div class="pp-card-back">o'tkazilmoq, ochilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">취소되다</div><div class="pp-card-back">bekor qilinmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">입장료</div><div class="pp-card-back">kirish haqi</div></div>
  <div class="pp-card"><div class="pp-card-front">빌리다</div><div class="pp-card-back">ijaraga/vaqtincha olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">무료</div><div class="pp-card-back">bepul</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>9–12-savollar: material (e'lon/grafik/matn) + 4 gap; <strong>bittasi</strong> mos.</li>
  <li>Usul — <strong>소거법</strong>: variantlarni birma-bir tekshirib, mos kelmaganini chizish.</li>
  <li>Avval <strong>variantlarni</strong> o'qing, keyin materialdan kalit so'zlarni qidiring.</li>
  <li>To'g'ri javob — matndagi faktning <strong>boshqa so'zlar bilan</strong> aytilgani.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 21) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 2: E'lon va plakatlar (안내문·포스터)",
        "summary": "9-savol: tadbir e'lonlarining standart maydonlari (기간, 대상, 참가비...) va ularning paraphrase'lari.",
        "order":   21,
        "blocks": [
            {"rich_text": """
<h2>📌 9-savol: e'lon va plakat (안내문·포스터)</h2>
<p><strong>9-savol</strong>da deyarli har doim tadbir e'loni keladi: kurs, festival, ko'rgazma,
musobaqa... E'lonlar <strong>standart maydonlar</strong>dan tuziladi — shu maydon nomlarini
bilsangiz, e'lonni sekundlarda "skanerlaysiz":</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;" open>
  <summary style="cursor:pointer;font-weight:600;">📂 E'lonning standart maydonlari</summary>
  <div style="margin-top:10px;">
    <ul>
      <li><strong>일시 / 날짜</strong> — sana-vaqt · <strong>기간</strong> — muddat (~부터 ~까지)</li>
      <li><strong>장소</strong> — joy</li>
      <li><strong>대상</strong> — kimlar uchun (누구나 — istagan kishi)</li>
      <li><strong>참가비 / 수강료 / 입장료</strong> — ishtirok / kurs / kirish haqi</li>
      <li><strong>신청 / 접수</strong> — ariza berish / qabul qilish</li>
      <li><strong>모집</strong> — to'plash, qabul · <strong>선착순</strong> — kim oldin kelsa</li>
      <li><strong>마감</strong> — tugash muddati · <strong>문의</strong> — ma'lumot uchun (tel.)</li>
    </ul>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Variantlar shu maydonlarni <strong>paraphrase</strong> qiladi:<br>
  대상: 누구나 → <em>나이 제한이 없습니다</em> (yosh chegarasi yo'q)<br>
  참가비: 무료 → <em>돈이 들지 않습니다</em> (pul ketmaydi)<br>
  선착순 20명 → <em>먼저 신청한 사람이 참가합니다</em> (oldin ariza berganlar qatnashadi)
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.15em;margin:0 0 10px;"><strong>문화 센터 수영 교실 모집</strong></p>
  <ul style="margin:0;padding-left:18px;">
    <li>기간: 3월 2일 ~ 5월 31일 (매주 화·목 저녁 8시)</li>
    <li>대상: 수영을 처음 배우는 성인 20명 (선착순)</li>
    <li>수강료: 한 달에 5만 원</li>
    <li>신청: 인터넷 홈페이지에서만 접수</li>
  </ul>
</div>
""",
             "choices": [
                 {"text": "수업은 주말마다 있습니다. (Darslar har dam olish kunlari bo'ladi.)", "is_correct": False},
                 {"text": "수영을 잘하는 사람만 신청할 수 있습니다. (Faqat suzishni yaxshi biladiganlar yozilishi mumkin.)", "is_correct": False},
                 {"text": "전화로 신청하면 됩니다. (Telefon orqali ariza bersa bo'ladi.)", "is_correct": False},
                 {"text": "신청자가 많으면 먼저 신청한 사람이 배웁니다. (Ariza beruvchi ko'p bo'lsa, oldin yozilganlar o'qiydi.)", "is_correct": True},
             ],
             "explanation": """
<p>① 화·목 — seshanba/payshanba, dam olish kuni emas. ② 대상: <strong>처음 배우는</strong>
(birinchi marta o'rganadigan) — teskari tuzoq! ③ <strong>인터넷 홈페이지에서만</strong> —
faqat saytda; "만" qo'shimchasi (faqat) juda muhim. To'g'risi ④: <strong>선착순</strong>
(kim oldin kelsa) so'zining paraphrase'i — "oldin ariza berganlar qatnashadi". ✅</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.15em;margin:0 0 10px;"><strong>어린이 벼룩시장</strong></p>
  <ul style="margin:0;padding-left:18px;">
    <li>일시: 매월 첫째 주 토요일, 오전 10시 ~ 오후 1시</li>
    <li>장소: 시민 공원 잔디밭</li>
    <li>참가비: 무료 (판매할 물건은 직접 가져와야 합니다)</li>
    <li>신청: 행사 하루 전까지 공원 관리 사무소</li>
  </ul>
</div>
<p style="color:#64748b;font-size:.92em;">벼룩시장 — "burga bozori" (eski buyumlar bozori) · 잔디밭 — maysazor</p>
""",
             "choices": [
                 {"text": "벼룩시장은 일 년에 한 번 열립니다. (Bozor yiliga bir marta o'tkaziladi.)", "is_correct": False},
                 {"text": "참가하려면 하루 전까지 신청해야 합니다. (Qatnashish uchun bir kun oldin ariza berish kerak.)", "is_correct": True},
                 {"text": "참가비를 내야 합니다. (Ishtirok haqi to'lash kerak.)", "is_correct": False},
                 {"text": "물건은 사무소에서 준비해 줍니다. (Buyumlarni idora tayyorlab beradi.)", "is_correct": False},
             ],
             "explanation": """
<p>① <strong>매월</strong> (har oy) birinchi shanba — yiliga bir marta emas, o'n ikki marta!
③ 참가비: <strong>무료</strong>. ④ 직접 가져와야 합니다 — buyumni <strong>o'zingiz</strong>
olib kelishingiz kerak, idora emas. To'g'risi ②: 행사 하루 전까지 신청 =
"tadbirdan bir kun oldingacha ariza". ✅ 매월/매주/매일 (har oy/hafta/kun) so'zlariga
doim diqqat qiling — davriylik eng sevimli tuzoq!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.15em;margin:0 0 10px;"><strong>제5회 외국인 한국어 말하기 대회</strong></p>
  <ul style="margin:0;padding-left:18px;">
    <li>일시: 11월 15일(금) 오후 2시</li>
    <li>대상: 한국에 사는 외국인 누구나</li>
    <li>주제: '내가 사랑하는 한국'</li>
    <li>신청 마감: 10월 31일까지 이메일 접수</li>
    <li>상품: 1등 100만 원 (참가자 전원 기념품 증정)</li>
  </ul>
</div>
""",
             "choices": [
                 {"text": "이 대회는 올해 처음 열립니다. (Bu tanlov bu yil birinchi marta o'tkazilmoqda.)", "is_correct": False},
                 {"text": "한국 사람도 참가할 수 있습니다. (Koreyslar ham qatnashishi mumkin.)", "is_correct": False},
                 {"text": "참가하는 사람은 모두 선물을 받습니다. (Qatnashganlarning hammasi sovg'a oladi.)", "is_correct": True},
                 {"text": "대회 날에 신청하면 됩니다. (Tanlov kuni ariza bersa bo'ladi.)", "is_correct": False},
             ],
             "explanation": """
<p>① <strong>제5회</strong> — "5-marta" degani (제~회 = ~-marta/-son); birinchi emas.
② 대상: <strong>외국인</strong> 누구나 — faqat chet elliklar. ④ 마감: <strong>10월 31일</strong> —
tanlovdan ancha oldin. To'g'risi ③: <strong>참가자 전원 기념품 증정</strong> =
"barcha ishtirokchilarga esdalik sovg'asi beriladi" → 모두 선물을 받습니다. ✅
전원 (hamma) va 증정 (sovg'a qilish) — e'lonlarda tez-tez chiqadigan xitoycha ildizli so'zlar.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">모집</div><div class="pp-card-back">qabul, to'plash</div></div>
  <div class="pp-card"><div class="pp-card-front">대상</div><div class="pp-card-back">kimlar uchun (auditoriya)</div></div>
  <div class="pp-card"><div class="pp-card-front">선착순</div><div class="pp-card-back">kim oldin kelsa (tartibida)</div></div>
  <div class="pp-card"><div class="pp-card-front">마감</div><div class="pp-card-back">tugash muddati (deadline)</div></div>
  <div class="pp-card"><div class="pp-card-front">접수</div><div class="pp-card-back">ariza qabul qilish</div></div>
  <div class="pp-card"><div class="pp-card-front">제~회</div><div class="pp-card-back">~-marta (tadbir soni)</div></div>
  <div class="pp-card"><div class="pp-card-front">전원</div><div class="pp-card-back">hamma, barcha (ishtirokchilar)</div></div>
  <div class="pp-card"><div class="pp-card-front">증정</div><div class="pp-card-back">sovg'a qilish, tuhfa</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>E'lonning maydon nomlarini (일시·대상·참가비·신청·마감) yodlang — skanerlash tezlashadi.</li>
  <li>Sevimli tuzoqlar: davriylik (매월!), "만" (faqat), 대상 cheklovi, kim nimani qilishi.</li>
  <li>To'g'ri javob maydonning paraphrase'i: 무료 → 돈이 들지 않는다, 선착순 → 먼저 신청한 사람.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 22) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 3: Grafiklar (그래프·도표)",
        "summary": "10-savol: reyting va o'zgarish grafiklarini o'qish — 차지하다, 늘다/줄다, ~에 비해 kabi grafik tili.",
        "order":   22,
        "blocks": [
            {"rich_text": """
<h2>📊 10-savol: grafik (그래프)</h2>
<p><strong>10-savol</strong>da grafik yoki diagramma beriladi. Grafik savollari aslida
<strong>sovg'a</strong>: hamma ma'lumot rasmda ko'rinib turadi, faqat "grafik tili"ni bilish
kerak. Ikki xil grafik keladi:</p>
<ul>
  <li><strong>Reyting grafigi (순위):</strong> nima ko'proq, nima kamroq — ustunlar taqqoslanadi.</li>
  <li><strong>O'zgarish grafigi (변화):</strong> yillar davomida o'sish yoki kamayish.</li>
</ul>
<h3>Grafik tili — shu so'zlarsiz bo'lmaydi</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>1위를 차지하다</strong> — <em>1-o'rinni egallamoq</em></p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>가장 많다 / 가장 적다</strong> — <em>eng ko'p / eng kam</em></p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>그다음으로 ~이/가 많다</strong> — <em>keyingi o'rinda ~ turadi</em></p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>~에 비해 / ~보다</strong> — <em>~ga nisbatan / ~dan ko'ra</em></p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>늘어나다(증가하다) / 줄어들다(감소하다)</strong> — <em>ko'paymoq / kamaymoq</em></p>
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>2배가 되다</strong> — <em>2 baravar bo'lmoq</em></p>
  <p style="font-size:1.08em;margin:0;"><strong>절반(반)을 넘다</strong> — <em>yarmidan oshmoq</em></p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Bu so'zlar keyin <strong>쓰기 53</strong>da (grafik tasvirlash)
  o'zingizga kerak bo'ladi — bu darsni o'rganish ikki bo'limga birdan investitsiya!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (reyting).</strong> 다음 그래프의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-weight:600;margin:0 0 12px;">직장인은 점심을 어디에서 먹을까?</p>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">회사 근처 식당</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:100%;background:#3b82f6;color:#fff;padding:3px 8px;border-radius:6px;font-size:.88em;">45%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">구내식당</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:67%;background:#60a5fa;color:#fff;padding:3px 8px;border-radius:6px;font-size:.88em;">30%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">도시락</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:33%;background:#93c5fd;color:#1e3a5f;padding:3px 8px;border-radius:6px;font-size:.88em;">15%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">편의점</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:22%;background:#bfdbfe;color:#1e3a5f;padding:3px 8px;border-radius:6px;font-size:.88em;">10%</div>
    </div>
  </div>
</div>
<p style="color:#64748b;font-size:.92em;">직장인 — ishlaydigan odam · 구내식당 — ish joyidagi oshxona · 도시락 — uydan olib kelingan ovqat · 편의점 — minimarket</p>
""",
             "choices": [
                 {"text": "구내식당에서 먹는 사람이 가장 많다. (Ish joyi oshxonasida ovqatlanadiganlar eng ko'p.)", "is_correct": False},
                 {"text": "도시락을 먹는 사람이 편의점에서 먹는 사람보다 적다. (Uydan ovqat olib keluvchilar minimarketdagilardan kam.)", "is_correct": False},
                 {"text": "직장인의 절반 가까이가 회사 근처 식당에서 먹는다. (Xodimlarning deyarli yarmi ofis yaqinidagi oshxonada ovqatlanadi.)", "is_correct": True},
                 {"text": "편의점에서 먹는 사람이 전체의 20%이다. (Minimarketda ovqatlanuvchilar jami 20%.)", "is_correct": False},
             ],
             "explanation": """
<p>① 1-o'rin — 회사 근처 식당 (45%), 구내식당 emas. ② 도시락 15% > 편의점 10% —
"kam" emas, <strong>ko'p</strong> (보다 적다/많다 ni sinchiklab o'qing!). ④ 편의점 = 10%,
20% emas. To'g'risi ③: 45% — bu <strong>절반 가까이</strong> (yarmiga yaqin). ✅
"절반 (50%) 가까이/넘게" iboralari grafikda aniq raqam bo'lmasa ham to'g'ri bo'lishi mumkin —
taxminiy ifodalarga o'rganing.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (o'zgarish).</strong> 다음 그래프의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-weight:600;margin:0 0 12px;">자전거로 출근하는 사람의 변화 (인주시)</p>
  <div style="display:flex;align-items:flex-end;gap:24px;justify-content:center;height:150px;">
    <div style="text-align:center;">
      <div style="width:56px;height:30px;background:#93c5fd;border-radius:6px 6px 0 0;margin:0 auto;"></div>
      <div style="font-size:.85em;margin-top:4px;"><strong>5천 명</strong><br>2021년</div>
    </div>
    <div style="text-align:center;">
      <div style="width:56px;height:60px;background:#60a5fa;border-radius:6px 6px 0 0;margin:0 auto;"></div>
      <div style="font-size:.85em;margin-top:4px;"><strong>1만 명</strong><br>2023년</div>
    </div>
    <div style="text-align:center;">
      <div style="width:56px;height:120px;background:#3b82f6;border-radius:6px 6px 0 0;margin:0 auto;"></div>
      <div style="font-size:.85em;margin-top:4px;"><strong>2만 명</strong><br>2025년</div>
    </div>
  </div>
</div>
<p style="color:#64748b;font-size:.92em;">출근하다 — ishga bormoq · 만 — o'n ming (1만 = 10 000, 2만 = 20 000)</p>
""",
             "choices": [
                 {"text": "자전거로 출근하는 사람이 계속 줄어들고 있다. (Velosipedda ishga boruvchilar doim kamaymoqda.)", "is_correct": False},
                 {"text": "2025년에는 2021년보다 4배 많아졌다. (2025-yilda 2021-yilga qaraganda 4 baravar ko'paydi.)", "is_correct": True},
                 {"text": "2023년에 자전거로 출근하는 사람이 2만 명이었다. (2023-yilda velosipedchilar 20 ming edi.)", "is_correct": False},
                 {"text": "2023년부터 자전거로 출근하는 사람이 줄었다. (2023-yildan boshlab kamaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Grafik faqat <strong>o'sishni</strong> ko'rsatyapti — ①④ (줄다 — kamaymoq) darhol chiziladi.
③ raqam tuzog'i: 2023-yil = <strong>1만</strong> (10 ming), 2만 emas. To'g'risi ②:
5천 → 2만 = <strong>4배</strong> (4 baravar). ✅ Koreyscha son tizimini mashq qiling:
천 (ming) → 만 (o'n ming) → 5천의 4배 = 2만. Ko'paytmalarni (2배, 3배...) tekshirishda
doim boshlang'ich raqamdan hisoblang.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (reyting, ikki guruh).</strong> 다음 그래프의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-weight:600;margin:0 0 12px;">스트레스를 어떻게 풀까? (남성 / 여성)</p>
  <table style="width:100%;border-collapse:collapse;font-size:.95em;">
    <tr style="background:#e2e8f0;">
      <th style="padding:6px;text-align:left;">방법</th>
      <th style="padding:6px;">남성</th>
      <th style="padding:6px;">여성</th>
    </tr>
    <tr><td style="padding:6px;border-bottom:1px solid #e2e8f0;">운동</td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;"><strong>40%</strong></td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;">20%</td></tr>
    <tr><td style="padding:6px;border-bottom:1px solid #e2e8f0;">친구와의 수다</td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;">15%</td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;"><strong>35%</strong></td></tr>
    <tr><td style="padding:6px;border-bottom:1px solid #e2e8f0;">맛있는 음식 먹기</td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;">25%</td><td style="padding:6px;text-align:center;border-bottom:1px solid #e2e8f0;">30%</td></tr>
    <tr><td style="padding:6px;">잠자기</td><td style="padding:6px;text-align:center;">20%</td><td style="padding:6px;text-align:center;">15%</td></tr>
  </table>
</div>
<p style="color:#64748b;font-size:.92em;">스트레스를 풀다 — stressni yozmoq · 수다 — suhbat, gurung</p>
""",
             "choices": [
                 {"text": "남성은 운동으로 스트레스를 푸는 사람이 가장 많다. (Erkaklarda sport bilan stress yozadiganlar eng ko'p.)", "is_correct": True},
                 {"text": "여성은 잠을 자면서 스트레스를 푸는 사람이 가장 많다. (Ayollarda uxlab stress yozadiganlar eng ko'p.)", "is_correct": False},
                 {"text": "남성과 여성 모두 친구와의 수다가 1위를 차지했다. (Erkak va ayollarda ham suhbat 1-o'rinni egalladi.)", "is_correct": False},
                 {"text": "맛있는 음식을 먹는 여성이 남성보다 적다. (Mazali ovqat yeydigan ayollar erkaklardan kam.)", "is_correct": False},
             ],
             "explanation": """
<p>Ikki ustunli grafikda <strong>qaysi guruh haqida gap ketyapti</strong> — asosiy savol.
② ayollarda 1-o'rin 수다 (35%), 잠자기 emas. ③ 수다 faqat ayollarda 1-o'rin.
④ 음식: ayollar 30% > erkaklar 25% — kam emas, ko'p. To'g'risi ①: erkaklarda
운동 40% = eng yuqori. ✅ Har variantda avval <strong>남성/여성</strong> so'zini belgilab
oling, keyin faqat o'sha ustunga qarang.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">차지하다</div><div class="pp-card-back">egallamoq (o'rin, ulush)</div></div>
  <div class="pp-card"><div class="pp-card-front">늘어나다 / 증가하다</div><div class="pp-card-back">ko'paymoq / o'smoq</div></div>
  <div class="pp-card"><div class="pp-card-front">줄어들다 / 감소하다</div><div class="pp-card-back">kamaymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~에 비해</div><div class="pp-card-back">~ga nisbatan</div></div>
  <div class="pp-card"><div class="pp-card-front">절반</div><div class="pp-card-back">yarim, yarmi</div></div>
  <div class="pp-card"><div class="pp-card-front">2배</div><div class="pp-card-back">2 baravar</div></div>
  <div class="pp-card"><div class="pp-card-front">순위</div><div class="pp-card-back">reyting, o'rin tartibi</div></div>
  <div class="pp-card"><div class="pp-card-front">그다음으로</div><div class="pp-card-back">keyingi o'rinda</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Grafik tili — 20 ta ibora: 차지하다, 가장 많다, ~에 비해, 늘다/줄다, ~배, 절반...</li>
  <li>Tuzoqlar: 보다 많다/적다 yo'nalishi, raqamning yiliga mos kelishi, 남성/여성 ustuni.</li>
  <li>천/만 sonlarini aniq o'qing: 1만 = 10 000; 5천의 4배 = 2만.</li>
  <li>Bu iboralar 쓰기 53da yozish uchun ham kerak — ikki karra foyda!</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 23) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 4: Yangilik matnlari (신문 기사)",
        "summary": "11–12-savollar: qisqa xabar matnlarida faktlarni tekshirish va paraphrase'ni tanish.",
        "order":   23,
        "blocks": [
            {"rich_text": """
<h2>📰 11–12-savollar: yangilik matni (신문 기사)</h2>
<p><strong>11–12-savollar</strong>da 3–5 gaplik qisqa xabar yoki ma'lumot matni keladi:
shahar yangiligi, qiziqarli voqea, biror hodisaning tushuntirishi. E'londagi kabi "maydonlar"
yo'q — endi faktlar <strong>gaplar ichiga yashiringan</strong>.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Variantlar odatda matn tartibida boradi: ① matn boshiga,
  ④ oxiriga tegishli bo'lishi ko'p uchraydi. Variantdagi kalit so'zni matndan topib,
  <strong>o'sha gap atrofini</strong> diqqat bilan o'qing — butun matnni qayta o'qish shart emas.
</div>
<h3>Paraphrase lug'ati — matn ↔ javob</h3>
<p>To'g'ri javob matndagi gapni boshqacha aytadi. Eng ko'p uchraydigan almashinuvlar:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>무료이다</strong> ↔ <strong>돈을 내지 않는다</strong> — <em>bepul ↔ pul to'lamaydi</em></p>
  <p style="margin:0 0 6px;"><strong>인기가 많다</strong> ↔ <strong>사람들이 많이 찾는다</strong> — <em>mashhur ↔ odamlar ko'p qidiradi</em></p>
  <p style="margin:0 0 6px;"><strong>증가했다</strong> ↔ <strong>늘어났다 / 많아졌다</strong> — <em>o'sdi ↔ ko'paydi</em></p>
  <p style="margin:0 0 6px;"><strong>~기 전에</strong> ↔ <strong>~고 나서 (반대)</strong> — <em>~dan oldin ↔ ~dan keyin (teskari!)</em></p>
  <p style="margin:0;"><strong>처음 열렸다</strong> ↔ <strong>전에는 없었다</strong> — <em>birinchi marta o'tkazildi ↔ ilgari bo'lmagan</em></p>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">지난 주말 인주시에서 '시민 걷기 대회'가
  열렸다. 이 대회는 올해로 5회째를 맞았으며 3천 명이 넘는 시민이 참가했다. 참가비는 만 원으로,
  참가비 전액은 어려운 이웃을 돕는 데 쓰인다. 대회가 끝난 후에는 참가자 모두에게 기념
  티셔츠를 나눠 주었다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>O'tgan dam olish kuni Inju shahrida "Fuqarolar yurish
  musobaqasi" o'tkazildi. Bu yil musobaqa 5-marta o'tkazilgan bo'lib, 3 mingdan ortiq fuqaro qatnashdi.
  Ishtirok haqi 10 ming von bo'lib, uning to'liq summasi muhtoj insonlarga yordamga sarflanadi.
  Musobaqa tugagach, barcha ishtirokchilarga esdalik futbolkasi tarqatildi.</em></p>
</div>
""",
             "choices": [
                 {"text": "이 대회는 올해 처음 열렸다. (Musobaqa bu yil birinchi marta o'tkazildi.)", "is_correct": False},
                 {"text": "참가비는 좋은 일에 사용된다. (Ishtirok haqi yaxshi ishga sarflanadi.)", "is_correct": True},
                 {"text": "참가자들은 대회 전에 티셔츠를 받았다. (Ishtirokchilar musobaqadan oldin futbolka oldi.)", "is_correct": False},
                 {"text": "삼천 명보다 적은 사람이 참가했다. (3 mingdan kam odam qatnashdi.)", "is_correct": False},
             ],
             "explanation": """
<p>① 5회째 — beshinchi marta. ③ <strong>대회가 끝난 후</strong> (tugagandan keyin) —
"oldin" teskari tuzoq. ④ 3천 명이 <strong>넘는</strong> (oshadigan) — kam emas, ko'p.
To'g'risi ②: matnda <strong>어려운 이웃을 돕는 데 쓰인다</strong> (muhtojlarga yordamga
ishlatiladi), javobda <strong>좋은 일에 사용된다</strong> (yaxshi ishga sarflanadi) —
klassik paraphrase. ✅ 쓰이다 = 사용되다 ekanini eslab qoling.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">최근 종이책 대신 전자책을 읽는 사람이
  늘고 있다. 전자책은 휴대폰만 있으면 언제 어디서나 읽을 수 있고 값도 종이책보다 싸다.
  하지만 오랫동안 화면을 보면 눈이 쉽게 피곤해진다. 그래서 여전히 종이책을 더 좋아하는
  사람도 적지 않다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>So'nggi paytlarda qog'oz kitob o'rniga elektron kitob
  o'qiydiganlar ko'paymoqda. Elektron kitobni telefon bo'lsa bas, istalgan vaqt va joyda o'qish mumkin,
  narxi ham qog'oz kitobdan arzon. Lekin ekranga uzoq qarasa ko'z tez charchaydi. Shuning uchun
  hamon qog'oz kitobni afzal ko'radiganlar ham oz emas.</em></p>
</div>
""",
             "choices": [
                 {"text": "전자책은 종이책보다 값이 비싸다. (Elektron kitob qog'oz kitobdan qimmat.)", "is_correct": False},
                 {"text": "전자책을 읽는 사람이 줄어들고 있다. (Elektron kitob o'quvchilari kamaymoqda.)", "is_correct": False},
                 {"text": "전자책을 오래 읽으면 눈이 피곤해질 수 있다. (Elektron kitobni uzoq o'qisa ko'z charchashi mumkin.)", "is_correct": True},
                 {"text": "요즘은 종이책을 좋아하는 사람이 없다. (Hozir qog'oz kitobni yoqtiradiganlar yo'q.)", "is_correct": False},
             ],
             "explanation": """
<p>① 값도 <strong>싸다</strong> — arzon (teskari tuzoq). ② <strong>늘고 있다</strong> —
ko'paymoqda (yana teskari). ④ 적지 않다 — "oz emas" = <strong>anchagina bor</strong>;
"yo'q" mutlaqo noto'g'ri. To'g'risi ③: 화면을 보면 눈이 피곤해진다 →
"uzoq o'qisa ko'z charchashi mumkin". ✅ <strong>적지 않다</strong> (oz emas) kabi
ikki marta inkor qilingan iboralarni to'g'ri o'qish — 11–12-savollarning kaliti.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">인주시립도서관이 다음 달부터 '밤 도서관'을
  운영한다. 매주 금요일과 토요일에는 밤 10시까지 문을 여는 것이다. 낮에 시간이 없는 직장인들을
  위해 준비한 것으로, 밤 시간에는 조용한 음악도 틀어 준다. 이용자가 많으면 다른 요일에도
  운영 시간을 늘릴 계획이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Inju shahar kutubxonasi kelgusi oydan "Tungi kutubxona"
  ishga tushiradi. Har juma va shanba kunlari kechki 10 gacha ochiq bo'ladi. Bu kunduzi vaqti yo'q
  xodimlar uchun tayyorlangan bo'lib, tunda sokin musiqa ham qo'yib beriladi. Foydalanuvchi ko'p bo'lsa,
  boshqa kunlarda ham ish vaqtini uzaytirish rejasi bor.</em></p>
</div>
""",
             "choices": [
                 {"text": "밤 도서관은 매일 운영된다. (Tungi kutubxona har kuni ishlaydi.)", "is_correct": False},
                 {"text": "밤 도서관은 직장인을 위해 만들어졌다. (Tungi kutubxona ishlaydiganlar uchun tashkil etilgan.)", "is_correct": True},
                 {"text": "밤 도서관은 이번 달부터 시작되었다. (Tungi kutubxona shu oydan boshlandi.)", "is_correct": False},
                 {"text": "밤 시간에는 음악을 들을 수 없다. (Tunda musiqa eshitib bo'lmaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>① faqat <strong>금요일과 토요일</strong> — har kuni emas. ③ <strong>다음 달부터</strong>
(kelgusi oydan) — hali boshlanmagan; 시작되었다 (boshlandi — o'tgan zamon) noto'g'ri.
④ 음악도 <strong>틀어 준다</strong> — musiqa qo'yib beriladi. To'g'risi ②:
<strong>직장인들을 위해 준비한 것</strong> → "ishlaydiganlar uchun tashkil etilgan". ✅
Zamonlarga qarang: ~ㄹ 계획이다 (reja), 다음 달부터 (kelajak) va ~았/었다 (o'tgan) —
variant zamoni matn zamoniga mos kelishi shart.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">기사</div><div class="pp-card-back">maqola, xabar</div></div>
  <div class="pp-card"><div class="pp-card-front">열리다</div><div class="pp-card-back">o'tkazilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">참가하다</div><div class="pp-card-back">qatnashmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">쓰이다 / 사용되다</div><div class="pp-card-back">ishlatilmoq, sarflanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">운영하다</div><div class="pp-card-back">yuritmoq, ishga tushirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">여전히</div><div class="pp-card-back">hamon, baribir</div></div>
  <div class="pp-card"><div class="pp-card-front">적지 않다</div><div class="pp-card-back">oz emas (anchagina)</div></div>
  <div class="pp-card"><div class="pp-card-front">~ㄹ 계획이다</div><div class="pp-card-back">~ rejasi bor</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Variantlar odatda matn tartibida — kalit so'zni topib, o'sha gap atrofini o'qing.</li>
  <li>Paraphrase juftliklarini yig'ing: 무료 ↔ 돈을 안 낸다, 쓰이다 ↔ 사용되다.</li>
  <li>Zamon tuzog'i: 계획이다 (reja) ≠ 시작되었다 (boshlandi); 전에 ≠ 후에.</li>
  <li>Ikki inkorli iboralar (적지 않다) — sekin, diqqat bilan.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 5 (order 24) ────────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 5: To'rt tuzoq + aralash mashq",
        "summary": "Noto'g'ri variantlar yasaladigan 4 ta usulni tanib olish va butun mavzu bo'yicha mini-test.",
        "order":   24,
        "blocks": [
            {"rich_text": """
<h2>🎯 Noto'g'ri variant qanday yasaladi? 4 ta tuzoq</h2>
<p>Imtihon tuzuvchilari noto'g'ri variantlarni tasodifiy yozmaydi — ular <strong>4 ta
usul</strong>dan foydalanadi. Tuzoqlarni nomma-nom bilib olsangiz, ularni o'zingiz
"ishlab chiqarilgan joyida" ushlaysiz:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi tuzoq ▸">
  <div class="pp-step">
    <p><strong>1-tuzoq — Raqamni almashtirish (숫자 바꾸기).</strong> Matndagi raqam variantda
    boshqasiga almashadi, yoki matndagi <em>boshqa</em> raqam kerakli joyga qo'yiladi.
    Matn: 2주일 동안 빌릴 수 있다 → Tuzoq: <span style="text-decoration:line-through;">일주일 동안 빌릴 수 있다</span>.
    <mark style="background:#fee2e2;">Har raqamni matndan barmoq bilan tekshiring.</mark></p>
  </div>
  <div class="pp-step">
    <p><strong>2-tuzoq — Teskari aytish (반대로 말하기).</strong> 늘다 ↔ 줄다, 싸다 ↔ 비싸다,
    전에 ↔ 후에, 무료 ↔ 유료. Matn: 값이 싸다 → Tuzoq:
    <span style="text-decoration:line-through;">값이 비싸다</span>.
    <mark style="background:#fee2e2;">Sifat va yo'nalish so'zlarini alohida tekshiring.</mark></p>
  </div>
  <div class="pp-step">
    <p><strong>3-tuzoq — Egani almashtirish (주어 바꾸기).</strong> Ishni <em>kim</em> qilgani
    almashtiriladi. Matn: 물건은 직접 가져와야 한다 (o'zingiz olib kelasiz) → Tuzoq:
    <span style="text-decoration:line-through;">사무소에서 준비해 준다</span> (idora tayyorlaydi).
    <mark style="background:#fee2e2;">"Kim? Kimga? Kim uchun?" deb so'rang.</mark></p>
  </div>
  <div class="pp-step">
    <p><strong>4-tuzoq — Matnda yo'q narsa (없는 내용).</strong> Mantiqan to'g'ri tuyuladigan,
    lekin matnda umuman aytilmagan gap. "Shunday bo'lsa kerak" — deb belgilamang:
    <mark style="background:#fee2e2;">variantdagi har bir fakt matnda bo'lishi shart.</mark></p>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Eng xavflisi — 4-tuzoq. U sizning <em>hayotiy bilimingizga</em>
  mos keladi, shuning uchun "to'g'ri" tuyuladi. Lekin savol "hayotda nima to'g'ri" emas,
  <strong>"matnda nima yozilgan"</strong> deb so'raydi!
</div>
"""},
            {"rich_text": """
<p><strong>Aralash mashq 1 (e'lon).</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-size:1.15em;margin:0 0 10px;"><strong>가을 사진 공모전</strong></p>
  <ul style="margin:0;padding-left:18px;">
    <li>주제: 우리 동네의 가을 풍경</li>
    <li>접수 기간: 9월 1일 ~ 10월 15일</li>
    <li>참가 방법: 이메일로 사진 파일 보내기 (1인 3장까지)</li>
    <li>발표: 10월 30일, 홈페이지</li>
    <li>※ 휴대폰으로 찍은 사진도 괜찮습니다.</li>
  </ul>
</div>
<p style="color:#64748b;font-size:.92em;">공모전 — tanlov (ijodiy ishlar) · 풍경 — manzara · 발표 — e'lon qilish</p>
""",
             "choices": [
                 {"text": "사진은 한 사람이 다섯 장까지 낼 수 있습니다. (Bir kishi beshtagacha surat topshirishi mumkin.)", "is_correct": False},
                 {"text": "휴대폰으로 찍은 사진으로도 참가할 수 있습니다. (Telefonda olingan surat bilan ham qatnashish mumkin.)", "is_correct": True},
                 {"text": "결과는 이메일로 알려 줍니다. (Natija email orqali bildiriladi.)", "is_correct": False},
                 {"text": "사진을 직접 가지고 가야 합니다. (Suratni o'zingiz olib borishingiz kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>① <strong>3장까지</strong> — 1-tuzoq (raqam). ③ 발표: <strong>홈페이지</strong> —
3-tuzoq (email — bu <em>topshirish</em> usuli, natija emas; vosita almashtirilgan).
④ 이메일로 보내기 — olib borish emas, 2/3-tuzoq aralash. To'g'risi ②:
※ 휴대폰으로 찍은 사진도 <strong>괜찮습니다</strong> → "telefon surati bilan ham bo'ladi". ✅
※ (yulduzcha) izohlar — javob ko'pincha o'sha yerda!</p>
"""},
            {"rich_text": """
<p><strong>Aralash mashq 2 (grafik).</strong> 다음 그래프의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="text-align:center;font-weight:600;margin:0 0 12px;">외국인 관광객이 한국에서 하고 싶은 것</p>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">한국 음식 먹기</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:100%;background:#3b82f6;color:#fff;padding:3px 8px;border-radius:6px;font-size:.88em;">50%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">쇼핑</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:50%;background:#60a5fa;color:#fff;padding:3px 8px;border-radius:6px;font-size:.88em;">25%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">고궁 구경</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:30%;background:#93c5fd;color:#1e3a5f;padding:3px 8px;border-radius:6px;font-size:.88em;">15%</div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin:6px 0;">
    <span style="width:120px;flex-shrink:0;text-align:right;font-size:.92em;">콘서트 관람</span>
    <div style="flex-grow:1;background:#e2e8f0;border-radius:6px;">
      <div style="width:20%;background:#bfdbfe;color:#1e3a5f;padding:3px 8px;border-radius:6px;font-size:.88em;">10%</div>
    </div>
  </div>
</div>
<p style="color:#64748b;font-size:.92em;">관광객 — sayyoh · 고궁 — qadimiy saroy · 관람 — tomosha qilish</p>
""",
             "choices": [
                 {"text": "쇼핑을 하고 싶다는 관광객이 가장 많다. (Xarid qilishni istovchi sayyohlar eng ko'p.)", "is_correct": False},
                 {"text": "콘서트를 보고 싶다는 사람이 고궁을 구경하고 싶다는 사람보다 많다. (Konsertni istovchilar saroyni istovchilardan ko'p.)", "is_correct": False},
                 {"text": "관광객의 절반이 한국 음식을 먹고 싶어 한다. (Sayyohlarning yarmi koreys taomini yeyishni xohlaydi.)", "is_correct": True},
                 {"text": "한국 음식을 먹고 싶다는 사람은 쇼핑을 하고 싶다는 사람의 3배이다. (Taom istovchilar xarid istovchilarning 3 baravari.)", "is_correct": False},
             ],
             "explanation": """
<p>① 1-o'rin — 음식 (50%). ② 콘서트 10% < 고궁 15% — teskari (2-tuzoq).
④ 50% = 25%ning <strong>2배</strong>, 3배 emas (1-tuzoq, ko'paytma). To'g'risi ③:
50% = <strong>절반</strong> (yarmi). ✅</p>
"""},
            {"rich_text": """
<p><strong>Aralash mashq 3 (matn).</strong> 다음 글의 내용과 같은 것을 고르십시오.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">다음 달부터 인주시의 모든 시내버스에서
  현금을 사용할 수 없게 된다. 카드가 없는 사람은 버스 정류장에 있는 기계에서 일회용 교통 카드를
  살 수 있다. 시는 이 방법으로 버스가 정류장에 서 있는 시간이 짧아질 것으로 기대하고 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Kelgusi oydan Inju shahridagi barcha shahar avtobuslarida
  naqd puldan foydalanib bo'lmaydi. Kartasi yo'q odamlar bekatdagi avtomatdan bir martalik transport
  kartasini sotib olishi mumkin. Shahar hokimligi bu usul bilan avtobusning bekatda turish vaqti
  qisqarishini kutmoqda.</em></p>
</div>
""",
             "choices": [
                 {"text": "지금은 버스에서 현금을 쓸 수 있다. (Hozircha avtobusda naqd pul ishlatsa bo'ladi.)", "is_correct": True},
                 {"text": "일회용 교통 카드는 버스 안에서 판다. (Bir martalik karta avtobus ichida sotiladi.)", "is_correct": False},
                 {"text": "이 방법으로 버스 요금이 싸질 것이다. (Bu usul bilan avtobus narxi arzonlashadi.)", "is_correct": False},
                 {"text": "작년부터 버스에서 현금을 받지 않았다. (O'tgan yildan beri avtobusda naqd pul olinmaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Bu savol zamonni sinaydi! Matn: <strong>다음 달부터</strong> ... 없게 <strong>된다</strong>
(kelgusi oydan boshlab bo'lmay <em>qoladi</em>) — demak <strong>hozir hali mumkin</strong> → ① to'g'ri. ✅
② karta <strong>정류장에 있는 기계</strong>da (bekatdagi avtomatda) sotiladi — joy almashtirilgan
(3-tuzoq). ③ narx haqida matnda <strong>hech narsa yo'q</strong> — vaqt qisqarishi kutilyapti
(4-tuzoq — matnda yo'q narsa!). ④ 작년부터 — teskari zamon (1/2-tuzoq).</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">현금</div><div class="pp-card-back">naqd pul</div></div>
  <div class="pp-card"><div class="pp-card-front">일회용</div><div class="pp-card-back">bir martalik</div></div>
  <div class="pp-card"><div class="pp-card-front">정류장</div><div class="pp-card-back">bekat</div></div>
  <div class="pp-card"><div class="pp-card-front">기대하다</div><div class="pp-card-back">kutmoq, umid qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">공모전</div><div class="pp-card-back">ijodiy tanlov</div></div>
  <div class="pp-card"><div class="pp-card-front">~게 되다</div><div class="pp-card-back">~ holatga kelmoq (o'zgarish)</div></div>
  <div class="pp-card"><div class="pp-card-front">관광객</div><div class="pp-card-back">sayyoh</div></div>
  <div class="pp-card"><div class="pp-card-front">발표</div><div class="pp-card-back">e'lon qilish, natija</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li><strong>4 tuzoq:</strong> raqam almashtirish · teskari aytish · egani almashtirish · matnda yo'q narsa.</li>
  <li>Eng xavflisi — "hayotda to'g'ri, matnda yo'q" variant. Faqat <strong>matnga</strong> tayaning.</li>
  <li>※ izohlar va zamon qo'shimchalari (다음 달부터, ~ㄹ 계획이다)da javob yashiringan bo'ladi.</li>
  <li>9-savol: e'lon maydonlari · 10-savol: grafik tili · 11–12: paraphrase — hammasi 소거법 bilan.</li>
</ul>
"""},
        ],
    },
]
