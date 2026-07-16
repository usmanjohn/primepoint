# TOPIK II Listening — 37–42-savollar: Ko'rsatuv va ma'ruza (교양 프로그램·강연), lessons 1–3 (orders 90–92).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_lecture_1_3.py \
#            --out examprep/management/commands/audio/lecture
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_lecture_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/lecture

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "37–42-savollar: Ko'rsatuv va ma'ruza (교양 프로그램·강연)",
    "summary": "Teleko'rsatuvdagi mutaxassis fikri, 'bundan oldin nima bo'lgan?' savoli (39) va ma'ruzaning bosh mazmuni.",
    "icon":    "bi-tv",
    "order":   10,
}

LESSONS = [
    # ── Lesson 1 (order 90) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 강연 1: 37–38-savollar — ko'rsatuvdagi mutaxassis",
        "summary": "교양 프로그램 juftligi: boshlovchi + mutaxassis; mutaxassisning bosh fikri va faktlar — tanish reja, jiddiyroq matn.",
        "order":   90,
        "blocks": [
            {"rich_text": """
<h2>📺 37–38-savollar: efirdagi mutaxassis</h2>
<p>Bu juftlik — teleradio ko'rsatuvi: boshlovchi mavzu ochadi, <strong>박사님/교수님/전문가</strong>
javob beradi. Savollar tanish: 37 — 중심 생각, 38 — 내용 일치. Intervyu blokidan farqi:
mavzular <strong>ilmiy-ma'rifiy</strong> (salomatlik, tabiat, kundalik fan) va javob uzunroq.</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> Mutaxassis javobining qolipi deyarli doim: <strong>tasdiqlash</strong>
  (네, 그렇습니다) → <strong>faktlar</strong> (연구 결과, 물질, misollar — 38 uchun!) →
  <strong>다만/그러니까 + maslahat</strong> (37 uchun!). Maslahat oxirida keladi — sabr bilan
  oxirigacha tinglang.
</div>
"""},
            {"rich_text": """
<p><strong>37-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_090_1.mp3",
             "audio_script": [
                 ("여자", "박사님, 요즘 집에서 식물을 기르는 분들이 많은데요. 식물이 실제로 우리 생활에 도움이 될까요?"),
                 ("남자", "네, 식물은 공기를 깨끗하게 할 뿐 아니라 마음 건강에도 좋습니다. 식물을 돌보는 동안 스트레스가 줄어든다는 연구 결과도 있지요. 다만 처음부터 기르기 어려운 식물을 고르면 금방 포기하게 됩니다. 그러니까 물을 자주 주지 않아도 되는 식물부터 시작하시길 권합니다."),
             ],
             "choices": [
                 {"text": "식물은 기르기 쉬운 것부터 시작하는 게 좋다. (O'simlikni parvarishi osonidan boshlagan ma'qul.)", "is_correct": True},
                 {"text": "식물은 공기를 깨끗하게 할 뿐이다. (O'simlik faqat havoni tozalaydi xolos.)", "is_correct": False},
                 {"text": "어려운 식물을 길러야 실력이 는다. (Qiyin o'simlik boqilsagina mahorat oshadi.)", "is_correct": False},
                 {"text": "식물에게 물을 매일 줘야 한다. (O'simlikka har kuni suv quyish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Qolip aynan ishladi: foydalar (havo, ruhiyat, tadqiqot) → <strong>다만</strong> (lekin) →
<strong>그러니까 ~시길 권합니다</strong> (shuning uchun tavsiya qilaman) → ✅ ①. Maslahat
tugallanmasi 권합니다 — 37-savolning eng kuchli signali. ② "faqat xolos" tuzog'i (~ㄹ 뿐
아니라 — "nafaqat"! teskarisi), ③ mutaxassis aytganining aksi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 박사님, 요즘 집에서 식물을 기르는 분들이 많은데요. 식물이 실제로 우리 생활에 도움이 될까요?<br>
    <em style="color:#475569;">Doktor, hozir uyda o'simlik boqadiganlar ko'p. O'simlik hayotimizga chindan foyda beradimi?</em></p>
    <p><strong>남자:</strong> 네, 식물은 공기를 깨끗하게 할 뿐 아니라 마음 건강에도 좋습니다.
    식물을 돌보는 동안 스트레스가 줄어든다는 연구 결과도 있지요. 다만 처음부터 기르기 어려운
    식물을 고르면 금방 포기하게 됩니다. 그러니까 물을 자주 주지 않아도 되는 식물부터
    시작하시길 권합니다.<br>
    <em style="color:#475569;">Ha, o'simlik nafaqat havoni tozalaydi, ruhiy salomatlikka ham
    foydali. O'simlik parvarishlash davomida stress kamayishi haqida tadqiqot natijalari ham bor.
    Biroq boshdanoq parvarishi qiyin o'simlik tanlansa, tez taslim bo'linadi. Shuning uchun suvni
    tez-tez talab qilmaydigan o'simliklardan boshlashni tavsiya qilaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>38-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida — ikkinchi marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "식물을 돌보면 스트레스가 줄어든다는 연구가 있다. (O'simlik parvarishi stressni kamaytirishi haqida tadqiqot bor.)", "is_correct": True},
                 {"text": "식물은 마음 건강과 관계가 없다. (O'simlik ruhiy salomatlikka aloqasi yo'q.)", "is_correct": False},
                 {"text": "모든 식물은 물을 자주 줘야 한다. (Hamma o'simlikka suvni tez-tez quyish kerak.)", "is_correct": False},
                 {"text": "요즘 식물을 기르는 사람이 줄고 있다. (Hozir o'simlik boqadiganlar kamaymoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (마음 건강에<strong>도</strong> 좋습니다), ③ "hamma" kengaytmasi
(자주 주지 <strong>않아도 되는</strong> turlari bor!), ④ boshlovchining kirishiga zid
(기르는 분들이 <strong>많은데요</strong>). ✅ ①: 연구 결과도 있지요 — aynan aytilgan.
37 da chetga surgan faktlar (연구!) — 38 ning javobi: ikki savol bir matnni bo'lishadi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">교양 프로그램</div><div class="pp-card-back">ma'rifiy ko'rsatuv</div></div>
  <div class="pp-card"><div class="pp-card-front">~ㄹ 뿐 아니라</div><div class="pp-card-back">nafaqat …, balki</div></div>
  <div class="pp-card"><div class="pp-card-front">돌보다</div><div class="pp-card-back">parvarishlamoq, g'amxo'rlik qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">연구 결과</div><div class="pp-card-back">tadqiqot natijasi</div></div>
  <div class="pp-card"><div class="pp-card-front">포기하다</div><div class="pp-card-back">taslim bo'lmoq, voz kechmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">권하다</div><div class="pp-card-back">tavsiya qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">다만</div><div class="pp-card-back">biroq, faqat</div></div>
  <div class="pp-card"><div class="pp-card-front">그러니까</div><div class="pp-card-back">shuning uchun</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Mutaxassis qolipi: tasdiqlash → faktlar (38!) → 다만/그러니까 + maslahat (37!).</li>
  <li>권합니다 / ~시길 바랍니다 — 37-savolning yakuniy signallari.</li>
  <li>~ㄹ 뿐 아니라 ("nafaqat") eshitilsa — "faqat xolos" varianti avtomatik noto'g'ri.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 91) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 강연 2: Bundan oldin nima bo'lgan? (39-savol)",
        "summary": "39-savol imtihonning eng g'alati savoli: suhbat o'rtasidan boshlanadi — birinchi replikadagi ishoralar orqali OLDINGI mazmunni tiklaysiz.",
        "order":   91,
        "blocks": [
            {"rich_text": """
<h2>⏪ 39-savol: orqaga qarab topish</h2>
<p>39–40 juftligi (대담 — mutaxassis suhbati) sizni <strong>suhbat o'rtasiga</strong> tashlaydi
va shunday so'raydi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>39.</strong> 이 담화 앞의 내용으로 가장 알맞은 것을
  고르십시오. — <em>Bu suhbatdan OLDIN nima haqida gapirilgan?</em></p>
</div>
<p>Javob audioda YO'Q — lekin <strong>birinchi replika</strong> uni ko'rsatib turadi. Ishora
so'zlarni oving:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>말씀하신 것처럼 / 말씀하신 대로</strong> — "siz aytganingizdek" → oldin U MAVZU tushuntirilgan.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>그렇게 심각한 줄 몰랐습니다</strong> — "bunchalik jiddiyligini bilmabman" → oldin muammoning jiddiyligi ko'rsatilgan.</p>
  <p style="font-size:1.05em;margin:0;"><strong>그럼 / 그렇다면 이제</strong> — "unday bo'lsa endi…" → oldingi mavzu tugab, yangisiga o'tilyapti.</p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Tuzoq — audioda HOZIR aytilayotgan mazmunni "oldingi" deb berish.
  39 ning javobi faqat birinchi replikadagi <strong>ishoradan</strong> chiqadi; suhbatning
  o'zi esa 40-savol uchun.
</div>
"""},
            {"rich_text": """
<p><strong>39-savol.</strong> 이 담화 앞의 내용으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_091_1.mp3",
             "audio_script": [
                 ("여자", "말씀하신 것처럼 바다 쓰레기 문제가 그렇게 심각한 줄은 몰랐습니다. 그럼 이 문제를 해결하기 위해서 어떤 활동을 하고 계신가요?"),
                 ("남자", "저희 단체는 한 달에 두 번 바닷가에서 쓰레기를 줍는 활동을 합니다. 또 어부들이 바다에서 건진 쓰레기를 가져오면 새 그물로 바꿔 주는 사업도 하고 있고요. 처음에는 관심이 없던 어부들도 이제는 점점 더 많이 참여하고 있습니다."),
             ],
             "choices": [
                 {"text": "바다 쓰레기 문제가 심각하다는 설명 (Dengiz chiqindisi muammosi jiddiyligi haqidagi tushuntirish)", "is_correct": True},
                 {"text": "새 그물의 가격에 대한 안내 (Yangi to'r narxi haqidagi ma'lumot)", "is_correct": False},
                 {"text": "어부가 되는 방법에 대한 설명 (Baliqchi bo'lish yo'llari haqidagi tushuntirish)", "is_correct": False},
                 {"text": "바닷가 여행지에 대한 소개 (Dengiz bo'yi sayohat joylari tanishtiruvi)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi replikadagi ikki ishora: <strong>말씀하신 것처럼</strong> (siz aytganingizdek) +
바다 쓰레기 문제가 그렇게 <strong>심각한 줄은 몰랐습니다</strong> → oldin erkak muammoning
jiddiyligini tushuntirgan → ✅ ①. ② hozirgi suhbatdagi detal (그물!) — "hozir"ni "oldin"ga
aylantirgan tuzoq. Keyin 그럼 keldi — mavzu almashdi: endi yechimlar (bu 40 uchun).</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 말씀하신 것처럼 바다 쓰레기 문제가 그렇게 심각한 줄은 몰랐습니다.
    그럼 이 문제를 해결하기 위해서 어떤 활동을 하고 계신가요?<br>
    <em style="color:#475569;">Aytganingizdek, dengiz chiqindisi muammosi bunchalik jiddiy
    ekanini bilmagan ekanman. Unday bo'lsa, bu muammoni hal qilish uchun qanday faoliyat olib
    boryapsiz?</em></p>
    <p><strong>남자:</strong> 저희 단체는 한 달에 두 번 바닷가에서 쓰레기를 줍는 활동을 합니다.
    또 어부들이 바다에서 건진 쓰레기를 가져오면 새 그물로 바꿔 주는 사업도 하고 있고요. 처음에는
    관심이 없던 어부들도 이제는 점점 더 많이 참여하고 있습니다.<br>
    <em style="color:#475569;">Bizning tashkilot oyiga ikki marta dengiz bo'yida chiqindi terish
    tadbirini o'tkazadi. Shuningdek, baliqchilar dengizdan chiqargan chiqindini olib kelishsa,
    yangi to'rga almashtirib beradigan loyihamiz ham bor. Avvaliga qiziqmagan baliqchilar ham
    endi tobora ko'proq qatnashmoqda.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>40-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "쓰레기를 가져온 어부는 새 그물을 받는다. (Chiqindi olib kelgan baliqchi yangi to'r oladi.)", "is_correct": True},
                 {"text": "단체는 일 년에 두 번 활동한다. (Tashkilot yiliga ikki marta faoliyat yuritadi.)", "is_correct": False},
                 {"text": "참여하는 어부들이 점점 줄고 있다. (Qatnashayotgan baliqchilar kamaymoqda.)", "is_correct": False},
                 {"text": "어부들은 처음부터 관심이 많았다. (Baliqchilar boshidanoq qiziqqan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② vaqt birligi almashtirilgan (<strong>한 달에</strong> 두 번 — oyiga!),
③ teskari (점점 더 많이 <strong>참여하고</strong>!), ④ teskari (처음에는 관심이
<strong>없던</strong>). ✅ ①: 쓰레기를 가져오면 새 그물로 바꿔 주는 — aynan shu.
일 년 ⇄ 한 달, 늘다 ⇄ 줄다 — bu blokda ham o'sha ikki klassik tuzoq ishlaydi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">담화</div><div class="pp-card-back">suhbat, nutq matni</div></div>
  <div class="pp-card"><div class="pp-card-front">말씀하신 것처럼</div><div class="pp-card-back">siz aytganingizdek</div></div>
  <div class="pp-card"><div class="pp-card-front">단체</div><div class="pp-card-back">tashkilot</div></div>
  <div class="pp-card"><div class="pp-card-front">줍다</div><div class="pp-card-back">terib olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">어부</div><div class="pp-card-back">baliqchi</div></div>
  <div class="pp-card"><div class="pp-card-front">그물</div><div class="pp-card-back">to'r</div></div>
  <div class="pp-card"><div class="pp-card-front">건지다</div><div class="pp-card-back">(suvdan) chiqarib olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">참여하다</div><div class="pp-card-back">qatnashmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>39: javob birinchi replikadagi ishorada (말씀하신 것처럼 / 몰랐습니다 / 그럼).</li>
  <li>Hozirgi suhbat mazmunini "oldingi" deb bergan variant — bosh tuzoq.</li>
  <li>그럼/그렇다면 — mavzu almashish chizig'i: undan keyingisi 40 uchun material.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 92) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 강연 3: To'liq amaliyot — muzsiz muzlatkich va memo sirlari",
        "summary": "41–42 ma'ruza (석빙고 — qadimiy muz ombori) va 37–38 ko'rsatuv (memo odati) — ikkala format imtihondagidek.",
        "order":   92,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: ma'ruza (41–42) va ko'rsatuv (37–38)</h2>
<p>41–42 juftligi — sof <strong>강연</strong> (ma'ruza): bir kishi ilmiy-tarixiy mavzuni
tushuntiradi; 41 — 중심 내용 (bosh mazmun), 42 — 내용 일치. Reja o'zgarmaydi: birinchi
eshitish — katta rasm, ikkinchisi — faktlar.</p>
"""},
            {"rich_text": """
<p><strong>41-savol.</strong> 이 강연의 중심 내용으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_092_1.mp3",
             "audio_script": [
                 ("여자", "옛날 사람들은 냉장고도 없이 얼음을 어떻게 여름까지 보관했을까요? 바로 석빙고라는 얼음 창고 덕분이었습니다. 석빙고는 땅을 깊이 파고 돌로 지어졌는데요. 더운 공기는 위로 빠져나가고 차가운 공기는 아래에 남는 원리를 이용한 것입니다. 이처럼 우리 조상들은 전기 없이도 과학적인 원리로 얼음을 지켜 냈습니다."),
             ],
             "choices": [
                 {"text": "석빙고는 과학적 원리를 이용한 얼음 창고이다. (Sokbinggo — ilmiy tamoyilga asoslangan muz ombori.)", "is_correct": True},
                 {"text": "옛날에는 여름에 얼음을 쓸 수 없었다. (Qadimda yozda muz ishlatib bo'lmagan.)", "is_correct": False},
                 {"text": "냉장고는 조선 시대에 발명되었다. (Muzlatkich Choson davrida ixtiro qilingan.)", "is_correct": False},
                 {"text": "얼음은 겨울에만 필요한 물건이었다. (Muz faqat qishda kerak bo'lgan.)", "is_correct": False},
             ],
             "explanation": """
<p>Ma'ruzaning skeleti: savol (어떻게 보관했을까요?) → javob (석빙고 <strong>덕분</strong>) →
mexanizm (havo tamoyili) → xulosa (<strong>이처럼</strong> 과학적인 원리로 지켜 냈습니다) →
✅ ①. O'qishdan tanish signal: <strong>이처럼</strong>dan keyingi jumla — bosh mazmunning
uyi! ② ma'ruza isbotlagan narsaning teskarisi (여름<strong>까지</strong> saqlashgan!).</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 옛날 사람들은 냉장고도 없이 얼음을 어떻게 여름까지 보관했을까요?
    바로 석빙고라는 얼음 창고 덕분이었습니다. 석빙고는 땅을 깊이 파고 돌로 지어졌는데요. 더운
    공기는 위로 빠져나가고 차가운 공기는 아래에 남는 원리를 이용한 것입니다. 이처럼 우리
    조상들은 전기 없이도 과학적인 원리로 얼음을 지켜 냈습니다.<br>
    <em style="color:#475569;">Qadimgi odamlar muzlatkichsiz muzni yozgacha qanday saqlashgan?
    Buning siri — sokbinggo degan muz ombori. Sokbinggo yerni chuqur kavlab, toshdan qurilgan.
    Issiq havo yuqoriga chiqib ketib, sovuq havo pastda qoladigan tamoyildan foydalanilgan.
    Shu tariqa ajdodlarimiz elektrsiz ham ilmiy tamoyil bilan muzni saqlab qolishgan.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>42-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "석빙고 안의 더운 공기는 위로 빠져나간다. (Sokbinggo ichidagi issiq havo yuqoriga chiqib ketadi.)", "is_correct": True},
                 {"text": "석빙고는 땅 위에 높이 지어졌다. (Sokbinggo yer ustida baland qilib qurilgan.)", "is_correct": False},
                 {"text": "석빙고는 나무로 만들어졌다. (Sokbinggo yog'ochdan qurilgan.)", "is_correct": False},
                 {"text": "석빙고는 전기로 온도를 낮췄다. (Sokbinggo haroratni elektr bilan tushirgan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (땅을 깊이 <strong>파고</strong> — chuqur kavlab!), ③ material
(<strong>돌</strong>로 — toshdan!), ④ ma'ruzaning butun g'oyasiga zid (전기 <strong>없이도</strong>!).
✅ ①: 더운 공기는 위로 빠져나가고 — aynan mexanizm jumlasi. Ma'ruzada mexanizmni
tushuntirgan jumla — 42-savolning eng sevimli javob manbasi.</p>
"""},
            {"rich_text": """
<p><strong>37-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_092_2.mp3",
             "audio_script": [
                 ("여자", "박사님은 항상 수첩을 가지고 다니면서 메모를 하신다고요?"),
                 ("남자", "네, 좋은 생각은 예고 없이 떠오르고 또 금방 사라집니다. 그래서 저는 생각이 떠오르면 그 자리에서 바로 적어 둡니다. 나중에 적어야지 하고 미루면 이미 잊어버린 경우가 많거든요. 기억력을 믿지 말고 손을 믿으시기 바랍니다."),
             ],
             "choices": [
                 {"text": "떠오른 생각은 그 자리에서 바로 적어야 한다. (Xayolga kelgan fikrni shu zahoti yozib qo'yish kerak.)", "is_correct": True},
                 {"text": "좋은 생각은 오래 기억에 남는다. (Yaxshi fikr uzoq esda qoladi.)", "is_correct": False},
                 {"text": "메모보다 기억력이 중요하다. (Yozuvdan ko'ra xotira muhimroq.)", "is_correct": False},
                 {"text": "수첩은 하루에 한 번만 봐야 한다. (Yon daftarni kuniga bir marta ko'rish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Bosh fikr ikki qavatda: 그 자리에서 <strong>바로 적어 둡니다</strong> (amaliyoti) +
yakuniy da'vat: 기억력을 믿지 말고 손을 <strong>믿으시기 바랍니다</strong> → ✅ ①.
② va ③ — uning gapining aynan teskarisi (금방 <strong>사라집니다</strong>; 기억력을 믿지
<strong>말고</strong>!). "믿지 말고 B를 믿으세요" — A가 아니라 B qolipining quloqdagi
versiyasi: javob B tomonida!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 박사님은 항상 수첩을 가지고 다니면서 메모를 하신다고요?<br>
    <em style="color:#475569;">Doktor, doim yon daftar olib yurib, qayd yozarkansiz-a?</em></p>
    <p><strong>남자:</strong> 네, 좋은 생각은 예고 없이 떠오르고 또 금방 사라집니다. 그래서 저는
    생각이 떠오르면 그 자리에서 바로 적어 둡니다. 나중에 적어야지 하고 미루면 이미 잊어버린
    경우가 많거든요. 기억력을 믿지 말고 손을 믿으시기 바랍니다.<br>
    <em style="color:#475569;">Ha, yaxshi fikr ogohlantirishsiz keladi va tez yo'qoladi. Shuning
    uchun fikr kelsa, shu joyning o'zida darhol yozib qo'yaman. "Keyin yozarman" deb kechiktirsam,
    allaqachon unutib qo'ygan paytlarim ko'p bo'lgan. Xotiraga emas, qo'lga ishoning.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>38-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "남자는 생각이 나면 그 자리에서 적는다. (Erkak fikr kelsa, shu joyning o'zida yozadi.)", "is_correct": True},
                 {"text": "남자는 메모를 하지 않는다. (Erkak qayd yozmaydi.)", "is_correct": False},
                 {"text": "남자는 생각을 나중에 적는 편이다. (Erkak fikrni keyinroq yozadigan odam.)", "is_correct": False},
                 {"text": "남자는 수첩을 가지고 다니지 않는다. (Erkak yon daftar olib yurmaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ②④ boshlovchining kirishiga zid (<strong>항상</strong> 수첩을 가지고 다니면서!),
③ u aynan rad etgan yo'l (나중에 적으면 잊어버린 경우가 많거든요). ✅ ①: 그 자리에서
바로 적어 둡니다. Mavzu tugadi: efir ham, ma'ruza ham, "orqaga qarash" ham qo'lingizda!
Keyingi bekat — hujjatli filmlar (43–46). 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">석빙고</div><div class="pp-card-back">qadimiy muz ombori</div></div>
  <div class="pp-card"><div class="pp-card-front">창고</div><div class="pp-card-back">ombor</div></div>
  <div class="pp-card"><div class="pp-card-front">원리</div><div class="pp-card-back">tamoyil, printsip</div></div>
  <div class="pp-card"><div class="pp-card-front">조상</div><div class="pp-card-back">ajdod</div></div>
  <div class="pp-card"><div class="pp-card-front">수첩</div><div class="pp-card-back">yon daftar</div></div>
  <div class="pp-card"><div class="pp-card-front">떠오르다</div><div class="pp-card-back">xayolga kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">미루다</div><div class="pp-card-back">kechiktirmoq, keyinga surmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">기억력</div><div class="pp-card-back">xotira (quvvati)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Ma'ruza skeleti: savol → javob → mexanizm → 이처럼-xulosa (41 shu yerda, 42 mexanizmda).</li>
  <li>"A를 믿지 말고 B를 믿으세요" = quloqdagi "A가 아니라 B" — javob B da.</li>
  <li>39-savol esingizda: birinchi replika ishoralari — 말씀하신 것처럼, 몰랐습니다, 그럼.</li>
</ul>
"""},
        ],
    },
]
