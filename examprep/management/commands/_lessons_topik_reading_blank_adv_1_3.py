# TOPIK II Reading — 28–31-savollar: Murakkab bo'sh joy (빈칸 고급),
# lessons 1–3 (orders 100–102).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_blank_adv_1_3.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "28–31-savollar: Murakkab bo'sh joy (빈칸 고급)",
    "summary": "Ilmiy va ijtimoiy matnlarda uzunroq bo'sh joyni matnning o'z mantig'idan topish.",
    "icon":    "bi-input-cursor-text",
    "order":   12,
}

LESSONS = [
    # ── Lesson 1 (order 100) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 빈칸 고급 1: 28–31-savollar bilan tanishuv — javob matnning ichida",
        "summary": "16–18-dan nimasi qiyin va 'javob matnda yashiringan' + parallelizm usullari.",
        "order":   100,
        "blocks": [
            {"rich_text": """
<h2>🧠 28–31-savollar: bo'sh joy — endi kattalar ligasida</h2>
<p>Shakl tanish: <strong>(        )에 들어갈 말로 가장 알맞은 것을 고르십시오</strong> —
16–18-savollar bilan bir xil. Farqi — daraja. To'rtta savol ketma-ket keladi va har biri
2 ball (jami 8 ball!):</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>16–18-da:</strong> kundalik mavzu, qisqa gap, bo'sh joyga qisqa ibora.</p>
  <p style="margin:0;"><strong>28–31-da:</strong> ilmiy/ijtimoiy matn (fan, psixologiya, iqtisod), 4–5 uzun gap,
  bo'sh joyga <mark style="background:#dbeafe;">butun bir fikr</mark> (uzunroq ibora) kiradi.</p>
</div>
<h3>Yangi qurol №1: javob matnning ichida yashiringan</h3>
<p>Murakkab matnlarda bo'sh joy deyarli har doim matnda <strong>allaqachon aytilgan
fikrning paraphrase'i</strong> bo'ladi. Matn bitta g'oyani 2–3 marta turli so'zlar bilan
aytadi — bo'sh joy o'sha takrorlardan biri, xolos:</p>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> Bo'sh joyli gapni o'qigach, o'zingizdan so'rang:
  <strong>"Bu gap matnning qaysi gapini boshqacha aytyapti?"</strong> O'sha gapni toping —
  javob uning soyasi bo'ladi.
</div>
<h3>Yangi qurol №2: parallelizm (대구)</h3>
<p>Matnlarda ikki narsa solishtirilsa, gaplar <strong>bir xil qolipda</strong> tuziladi.
Bittasi to'liq, ikkinchisida bo'sh joy — qolipni ko'chiring:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;">말하기가 생각을 <u>밖으로 꺼내는</u> 과정이라면, 듣기는 생각을 <strong>(  안으로 받아들이는  )</strong> 과정이다.</p>
  <p style="color:#475569;margin:0;"><em>Gapirish fikrni <u>tashqariga chiqarish</u> jarayoni bo'lsa, tinglash fikrni ( ichkariga qabul qilish ) jarayonidir.</em> — qolip bir xil, ma'no qarama-qarshi!</p>
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol — birga yechamiz</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">식물도 스트레스를 받으면 소리를 낸다.
  물이 부족하거나 줄기가 잘리면 평소보다 훨씬 자주 '딸깍' 하는 소리를 내는 것이다. 이 소리는
  사람의 귀에는 들리지 않지만 기계로는 잡아낼 수 있다. 과학자들은 이 소리를 분석하면 물을
  줘야 할 때를 놓치지 않는 등 식물의 상태를 (        ) 것으로 기대하고 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>O'simlik ham stress olsa tovush chiqaradi. Suv
  yetishmasa yoki poyasi kesilsa, odatdagidan tez-tez "chiq-chiq" tovush chiqaradi. Bu tovush odam
  qulog'iga eshitilmaydi, lekin asbob ilg'aydi. Olimlar bu tovushni tahlil qilib, suv berish vaqtini
  o'tkazib yubormaslik kabi o'simlik holatini (        )ga umid qilmoqda.</em></p>
</div>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — bo'sh joy gapining vazifasi:</strong> 기대하고 있다 (umid qilmoqda) —
    bu <strong>xulosa-gap</strong>: texnologiyadan kutilayotgan foyda aytilyapti.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — matndan izini topamiz:</strong> bo'sh joy oldida misol berilgan:
    "suv berish <strong>vaqtini o'tkazib yubormaslik</strong>" (물을 줘야 할 때를 놓치지 않는) —
    ya'ni muammoni <strong>oldindan bilish</strong>.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — paraphrase:</strong> "vaqtini o'tkazib yubormaslik" ning umumiy
    ko'rinishi = <mark style="background:#dcfce7;">미리 알 수 있을</mark> (oldindan bila olish).
    Tekshiruv: "o'simlik holatini <em>oldindan bila olishga</em> umid qilmoqda" — ikki tomoni ham mos ✅.</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">대화는 두 가지 활동으로 이루어진다.
  말하기가 자신의 생각을 밖으로 꺼내는 과정이라면, 듣기는 상대방의 생각을 (        ) 과정이다.
  그래서 둘 중 하나라도 부족하면 대화가 제대로 이루어지지 않는다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Suhbat ikki faoliyatdan iborat. Gapirish o'z fikrini
  tashqariga chiqarish jarayoni bo'lsa, tinglash suhbatdosh fikrini (        ) jarayonidir. Shuning
  uchun ikkovidan biri yetishmasa, suhbat to'g'ri qurilmaydi.</em></p>
</div>
""",
             "choices": [
                 {"text": "안으로 받아들이는 (ichkariga qabul qilish)", "is_correct": True},
                 {"text": "밖으로 표현하는 (tashqariga ifodalash)", "is_correct": False},
                 {"text": "빨리 잊어버리는 (tez unutish)", "is_correct": False},
                 {"text": "글로 바꾸는 (yozuvga aylantirish)", "is_correct": False},
             ],
             "explanation": """
<p>Parallelizm ishladi: "말하기 = 밖으로 꺼내는" ↔ "듣기 = ( )". Qolip bir xil, yo'nalish
qarama-qarshi bo'lishi kerak: 밖 (tashqari) ↔ <mark style="background:#dcfce7;">안 (ichkari)</mark>,
꺼내다 (chiqarmoq) ↔ 받아들이다 (qabul qilmoq) ✅. ② gapirishning ta'rifi — parallelizmni
buzadi (ikkovi bir xil bo'lib qoladi!). A라면 B qolipini ko'rsangiz — doim juftlik qidiring.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">꿀벌은 춤으로 대화를 한다. 꽃을 발견한
  벌은 벌집에 돌아와 8자 모양으로 춤을 추는데, 춤의 방향은 꽃이 있는 방향을 알려 주고 춤의
  속도는 꽃까지의 (        ) 알려 준다. 동료 벌들은 이 춤만 보고도 정확하게 꽃을 찾아간다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Asalari raqs bilan gaplashadi. Gul topgan ari uyasiga
  qaytib, 8 shaklida raqs tushadi: raqs yo'nalishi gul qaysi tomondaligini bildiradi, raqs tezligi esa
  gulgacha bo'lgan (        ) bildiradi. Sherik arilar shu raqsga qarab gulni aniq topib boradi.</em></p>
</div>
""",
             "choices": [
                 {"text": "거리를 (masofani)", "is_correct": True},
                 {"text": "색깔을 (rangini)", "is_correct": False},
                 {"text": "개수를 (sonini)", "is_correct": False},
                 {"text": "냄새를 (hidini)", "is_correct": False},
             ],
             "explanation": """
<p>Yana parallelizm: "방향은 ... 방향을 알려 주고 / 속도는 ... (        ) 알려 준다" —
ikki juftlik: yo'nalish→yo'nalishni, tezlik→? Tezlik nimani bildira oladi? Mantiqan —
<mark style="background:#dcfce7;">masofani</mark> (yaqin bo'lsa tez, uzoq bo'lsa sekin) ✅.
"꽃까지의" (gul<em>gacha</em>) qo'shimchasi ham faqat masofaga mos — 까지 = "~gacha" doim
masofa/vaqt bilan keladi. Rang, son, hidni "tezlik" ifodalay olmaydi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">과정</div><div class="pp-card-back">jarayon</div></div>
  <div class="pp-card"><div class="pp-card-front">이루어지다</div><div class="pp-card-back">tashkil topmoq, amalga oshmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">받아들이다</div><div class="pp-card-back">qabul qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">분석하다</div><div class="pp-card-back">tahlil qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">기대하다</div><div class="pp-card-back">umid/kutmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">A라면 B</div><div class="pp-card-back">A bo'lsa, B (parallelizm qolipi)</div></div>
  <div class="pp-card"><div class="pp-card-front">놓치다</div><div class="pp-card-back">o'tkazib yubormoq</div></div>
  <div class="pp-card"><div class="pp-card-front">동료</div><div class="pp-card-back">sherik, hamkasb</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>28–31 = 16–18 usuli + ikki yangi qurol: <strong>javob matn ichida</strong> (paraphrase) va <strong>parallelizm</strong>.</li>
  <li>Bo'sh joyli gap matnning qaysi gapini qayta aytayotganini toping — javob o'sha yerda.</li>
  <li>A라면 B, A는 ~고 B는 ~ qoliplarida yo'nalishlar juft bo'ladi (밖↔안, 꺼내다↔받아들이다).</li>
  <li>4 savol = 8 ball — bu blokka 6–8 daqiqa ajrating.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 101) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 빈칸 고급 2: Fan va psixologiya matnlari",
        "summary": "Ta'rif, tajriba va mexanizm turidagi ilmiy matnlarda bo'sh joy amaliyoti.",
        "order":   101,
        "blocks": [
            {"rich_text": """
<h2>🔬 Fan va psixologiya matnlari</h2>
<p>28–31-savollarning sevimli mavzulari: hayvonlar dunyosi, miya va xotira, inson xulqi.
Bunday matnlar uch qolipdan birida keladi:</p>
<ul>
  <li><strong>Ta'rif (정의):</strong> "X란 ~는 것이다" — X bu ~. Bo'sh joy ko'pincha ta'rifning o'zida yoki misolda.</li>
  <li><strong>Tajriba (실험):</strong> "실험 결과 ..." — tajriba → natija → xulosa. Bo'sh joy odatda xulosada.</li>
  <li><strong>Mexanizm (원리):</strong> "왜냐하면 / ~기 때문이다" — hodisa → sababi. Bo'sh joy sabab zanjirining bir halqasi.</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Ilmiy matnda his-tuyg'u yo'q — faqat mantiq. Demak javob ham
  <strong>quruq mantiqiy</strong> bo'ladi: eng chiroyli variant emas, matn zanjiriga
  qulflanadigan variant to'g'ri.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (psixologiya).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">사람은 어떤 대상을 자주 보기만 해도
  그 대상에 대한 호감이 커진다. 처음에는 관심이 없던 노래도 여러 번 듣다 보면 어느새
  좋아하게 되는 것이 그 예이다. 광고에서 같은 제품을 계속 반복해서 보여 주는 것도 소비자가
  그 제품에 (        ) 만들기 위해서이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Odam biror narsani tez-tez ko'rsa ham unga nisbatan
  xayrixohligi ortadi. Avvaliga qiziqtirmagan qo'shiq ham qayta-qayta eshitilsa, bilinmay yoqib
  qolishi — bunga misol. Reklamada bitta mahsulotning qayta-qayta ko'rsatilishi ham iste'molchini
  o'sha mahsulotga (        ) qilish uchundir.</em></p>
</div>
""",
             "choices": [
                 {"text": "친숙함을 느끼도록 (tanishlik hissini tuyadigan)", "is_correct": True},
                 {"text": "싫증을 내도록 (bezib qoladigan)", "is_correct": False},
                 {"text": "돈을 아끼도록 (pulni tejaydigan)", "is_correct": False},
                 {"text": "관심을 끊도록 (qiziqishni uzadigan)", "is_correct": False},
             ],
             "explanation": """
<p>Matnning bosh g'oyasi 1-gapda: tez-tez ko'rish → <strong>호감이 커진다</strong> (xayrixohlik
ortadi). Reklama misoli shu qoidaning takrori — demak bo'sh joy ham o'sha g'oyaning
paraphrase'i: <mark style="background:#dcfce7;">친숙함을 느끼도록</mark> (tanish tuyulsin deb) ✅.
②④ teskari yo'nalish. Bu — mashhur "단순 노출 효과" (oddiy takror ta'siri); TOPIK
psixologiya matnlari ko'pincha shunday "qiziq qonuniyat" haqida bo'ladi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (miya va xotira).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">잠은 기억을 저장하는 데 중요한 역할을
  한다. 우리가 자는 동안 뇌는 낮에 들어온 정보 가운데 중요한 것을 골라 오래 남는 기억으로
  바꾸기 때문이다. 따라서 시험 전날 잠을 줄여 가며 밤새 공부하는 것은 오히려 공부한 내용을
  (        ) 일이 될 수 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Uyqu xotirani saqlashda muhim rol o'ynaydi. Chunki biz
  uxlayotganda miya kunduzi kirgan ma'lumotlardan muhimini tanlab, uzoq saqlanadigan xotiraga
  aylantiradi. Shuning uchun imtihon arafasida uyquni qisqartirib tuni bilan o'qish, aksincha, o'qilgan
  narsani (        ) ishga aylanishi mumkin.</em></p>
</div>
""",
             "choices": [
                 {"text": "쉽게 잊어버리게 하는 (oson unutiladigan qiladigan)", "is_correct": True},
                 {"text": "머리에 더 오래 남기는 (miyada uzoqroq qoldiradigan)", "is_correct": False},
                 {"text": "더 재미있게 만드는 (yanada qiziqarli qiladigan)", "is_correct": False},
                 {"text": "빨리 이해하게 하는 (tez tushuntiradigan)", "is_correct": False},
             ],
             "explanation": """
<p>Zanjir: uyqu → xotiraga aylantiradi. Uyquni <strong>qisqartirish</strong> → aylantirish
ishlamaydi → o'qilgan narsa <mark style="background:#dcfce7;">unutiladi</mark> ✅.
Imzo so'z: <strong>오히려</strong> (aksincha!) — talaba kutgani (ko'proq o'qish = ko'proq
bilish)ning teskarisi kelishini e'lon qiladi. ② aynan 오히려 ni ko'rmagan odamning javobi —
19–20-savollardan tanish tuzoq!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (hayvonlar).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">낙타는 사막에서 오랫동안 물을 마시지
  않고도 살 수 있다. 등에 있는 혹에 지방을 저장해 두었다가 먹이가 없을 때 이것을 에너지로
  바꿔 쓰기 때문이다. 즉 낙타의 혹은 사막이라는 어려운 환경에서 살아남기 위한 일종의
  (        ) 같은 것이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Tuya sahroda uzoq vaqt suv ichmasdan yashay oladi.
  Chunki o'rkachida yog' zaxirasini saqlab, ozuqa yo'q paytda uni energiyaga aylantirib ishlatadi.
  Ya'ni tuyaning o'rkachi sahrodek og'ir muhitda omon qolish uchun o'ziga xos (        ) kabidir.</em></p>
</div>
""",
             "choices": [
                 {"text": "비상 식량 창고 (zaxira oziq ombori)", "is_correct": True},
                 {"text": "무거운 짐 (og'ir yuk)", "is_correct": False},
                 {"text": "아름다운 장식 (chiroyli bezak)", "is_correct": False},
                 {"text": "빠른 다리 (tez oyoq)", "is_correct": False},
             ],
             "explanation": """
<p>Imzo: <strong>즉</strong> (ya'ni) — oldingi gapni qayta aytishni e'lon qiladi. Oldingi gap:
"yog' <strong>saqlab</strong>, kerakda energiya qiladi" → saqlash joyi = ombor →
<mark style="background:#dcfce7;">비상 식량 창고</mark> (zaxira ozuqa ombori) ✅.
일종의 ~ 같은 것 ("o'ziga xos ~ kabi") qolipi metafora-ta'rif kiritadi — undan oldingi
gapdagi vazifani obrazga aylantiring. ② tashqi ko'rinishga aldangan javob.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">호감</div><div class="pp-card-back">xayrixohlik, iliq munosabat</div></div>
  <div class="pp-card"><div class="pp-card-front">친숙하다</div><div class="pp-card-back">tanish, o'rganilgan</div></div>
  <div class="pp-card"><div class="pp-card-front">저장하다</div><div class="pp-card-back">saqlamoq (zaxira)</div></div>
  <div class="pp-card"><div class="pp-card-front">뇌</div><div class="pp-card-back">miya</div></div>
  <div class="pp-card"><div class="pp-card-front">지방</div><div class="pp-card-back">yog' (organizmda)</div></div>
  <div class="pp-card"><div class="pp-card-front">살아남다</div><div class="pp-card-back">omon qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">일종의 ~ 같은 것</div><div class="pp-card-back">o'ziga xos ~ kabi (metafora-ta'rif)</div></div>
  <div class="pp-card"><div class="pp-card-front">즉</div><div class="pp-card-back">ya'ni (qayta aytish belgisi)</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Ilmiy matn qoliplari: ta'rif (란 ~것이다), tajriba (실험 결과), mexanizm (~기 때문이다).</li>
  <li><strong>즉</strong>dan keyin — oldingi gapning qayta aytilishi: bo'sh joy shu yerda bo'lsa, javob oldingi gapda.</li>
  <li>오히려 ko'rinsa — kutilgan natijaning teskarisini tanlang.</li>
  <li>Eng chiroyli emas, matn zanjiriga <strong>qulflanadigan</strong> variant to'g'ri.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 102) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 빈칸 고급 3: Jamiyat va iqtisod matnlari + tuzoqlar",
        "summary": "Iqtisodiy-ijtimoiy matnlar amaliyoti va murakkab bo'sh joyning uch tuzog'i.",
        "order":   102,
        "blocks": [
            {"rich_text": """
<h2>🏙️ Jamiyat va iqtisod matnlari</h2>
<p>Ikkinchi katta guruh — jamiyat hodisalari: iste'mol odatlari, yangi xizmatlar,
demografik o'zgarishlar. Qolip odatda: <strong>hodisa → sababi/mexanizmi → xulosa</strong>,
bo'sh joy esa mexanizmning kalit halqasida turadi.</p>
<h3>Murakkab bo'sh joyning 3 tuzog'i</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi tuzoq ▸">
  <div class="pp-step">
    <p><strong>1-tuzoq — Matn so'zlari + noto'g'ri mantiq.</strong> Variant matndagi
    so'zlardan yasalgan, lekin zanjirga ulaganda ma'no buziladi. Himoya: variantni bo'sh
    joyga qo'yib, <strong>oldi va keyini bilan birga</strong> o'qing.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-tuzoq — Teskari yo'nalish.</strong> Ayniqsa 오히려, 반면, -는데도 atrofida:
    to'g'ri so'zlar, qarama-qarshi xulosa. Himoya: bo'sh joy (+)mi (−)mi — avval belgisini aniqlang.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-tuzoq — Juda tor yoki juda keng.</strong> Matn umumiy qonuniyat aytsa,
    javob ham umumiy bo'ladi; matn aniq misol so'rasa — aniq. Himoya: bo'sh joyli gap
    <strong>xulosami yoki misolmi</strong> — vazifasiga qarab kenglikni tanlang.</p>
  </div>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (marketing).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">마트는 일부러 몇몇 상품을 아주 싼
  가격에 판다. 이런 상품은 팔면 팔수록 가게에 손해다. 하지만 싼 물건을 사러 온 손님들이
  온 김에 다른 상품까지 사기 때문에 가게 전체의 매출은 오히려 늘어난다. 즉 이런 상품은
  손님을 가게로 (        ) 역할을 하는 셈이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Do'kon ataylab ayrim mahsulotlarni juda arzon narxda
  sotadi. Bunday mahsulot sotilgan sari do'konga zarar. Lekin arzon narsani olgani kelgan mijozlar
  kelgan bahonasida boshqa mahsulotlarni ham olgani uchun do'konning umumiy tushumi, aksincha, oshadi.
  Ya'ni bunday mahsulotlar mijozni do'konga (        ) vazifasini bajaradi deyish mumkin.</em></p>
</div>
""",
             "choices": [
                 {"text": "불러들이는 (chorlab keltiradigan)", "is_correct": True},
                 {"text": "들어오지 못하게 하는 (kiritmaydigan)", "is_correct": False},
                 {"text": "오래 기다리게 하는 (uzoq kuttiradigan)", "is_correct": False},
                 {"text": "비싼 물건만 사게 하는 (faqat qimmat narsa oldiradigan)", "is_correct": False},
             ],
             "explanation": """
<p>Zanjir: arzon mahsulot → mijoz <strong>keladi</strong> → boshqa narsalarni ham oladi →
tushum oshadi. Demak arzon mahsulotning vazifasi — mijozni <mark style="background:#dcfce7;">
chorlash</mark> ✅. Imzolar to'plami ishladi: 즉 (qayta aytish) + ~는 셈이다 (deyish mumkin —
3–4-darslardan tanish!). E'tibor: matnda 온 김에 ham bor — "kelgan bahonasida" (Q3–4 juftligi).
Eski mavzular shu yerda uchrashadi!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (demografiya).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">혼자 사는 사람이 늘면서 소비의 모습도
  달라지고 있다. 대용량 제품 대신 한 번 먹을 만큼만 담은 소포장 식품이 인기를 얻고 있고,
  가구나 가전제품도 (        ) 제품이 잘 팔린다. 기업들도 이런 변화에 맞춰 1인 가구를 위한
  상품을 앞다투어 내놓고 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Yolg'iz yashovchilar ko'paygani sari iste'mol
  ko'rinishi ham o'zgarmoqda. Katta hajmli mahsulot o'rniga bir mahalga yetadigan kichik qadoqli
  oziq-ovqat ommalashmoqda, mebel va maishiy texnikada ham (        ) mahsulotlar yaxshi sotilmoqda.
  Korxonalar ham bu o'zgarishga moslashib, yakka xonadonlar uchun mahsulotlarni birin-ketin
  chiqarmoqda.</em></p>
</div>
""",
             "choices": [
                 {"text": "혼자 쓰기에 알맞은 (bir kishi ishlatishiga mos)", "is_correct": True},
                 {"text": "온 가족이 함께 쓰는 (butun oila birga ishlatadigan)", "is_correct": False},
                 {"text": "값이 아주 비싼 (narxi juda qimmat)", "is_correct": False},
                 {"text": "크면 클수록 좋은 (katta bo'lgani sari yaxshi)", "is_correct": False},
             ],
             "explanation": """
<p>Parallelizm: oziq-ovqatda "대용량 대신 <strong>소포장</strong>" (katta o'rniga kichik) →
mebel/texnikada ham xuddi shu yo'nalish: <mark style="background:#dcfce7;">혼자 쓰기에
알맞은</mark> (yakka foydalanishga mos) ✅. Tekshiruv: keyingi gap "1인 가구를 위한 상품"
(yakka xonadonlar uchun) — mos! ②④ teskari yo'nalish (2-tuzoq), ③ matnda narx haqida
gap yo'q (3-tuzoq: chetdan kelgan g'oya).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (yangi iste'mol).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">물건을 사서 소유하는 대신 필요할 때만
  빌려 쓰는 소비가 늘고 있다. 자동차와 옷은 물론 가방, 장난감까지 빌려 쓰는 서비스가 생겼다.
  이러한 소비는 돈이 적게 들 뿐만 아니라 쓰지 않는 물건이 (        ) 환경 보호에도 도움이
  된다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Narsani sotib olib egalik qilish o'rniga keragida
  ijaraga olib ishlatish iste'moli ko'paymoqda. Avtomobil va kiyim u yoqda tursin, sumka, hatto
  o'yinchoqni ijaraga beruvchi xizmatlar paydo bo'ldi. Bunday iste'mol kam xarajatli bo'libgina
  qolmay, ishlatilmaydigan narsalar (        ) atrof-muhitni asrashga ham yordam beradi.</em></p>
</div>
""",
             "choices": [
                 {"text": "버려지는 것을 줄여 (tashlab yuborilishini kamaytirib)", "is_correct": True},
                 {"text": "더 많이 만들어져 (yanada ko'p ishlab chiqarilib)", "is_correct": False},
                 {"text": "집에 쌓이게 해 (uyda to'planib qolishiga olib kelib)", "is_correct": False},
                 {"text": "더 비싸게 팔려 (qimmatroq sotilib)", "is_correct": False},
             ],
             "explanation": """
<p>Zanjir: ijaraga olish → hamma o'ziniki qilib sotib olmaydi → ishlatilmay
<strong>tashlanadigan</strong> narsalar kamayadi → tabiatga foyda →
<mark style="background:#dcfce7;">버려지는 것을 줄여</mark> ✅. Tekshiruv so'zi bo'sh joydan
keyin: <strong>환경 보호</strong> (tabiatni asrash — 5–8-darslardagi 공익 mavzusi!). ②③
teskari (ko'proq ishlab chiqarish/to'planish tabiatga zarar), ④ narx — bu gapning mavzusi emas.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">매출</div><div class="pp-card-back">savdo tushumi</div></div>
  <div class="pp-card"><div class="pp-card-front">손해</div><div class="pp-card-back">zarar</div></div>
  <div class="pp-card"><div class="pp-card-front">소유하다</div><div class="pp-card-back">egalik qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">1인 가구</div><div class="pp-card-back">yakka (bir kishilik) xonadon</div></div>
  <div class="pp-card"><div class="pp-card-front">대용량 / 소포장</div><div class="pp-card-back">katta hajm / kichik qadoq</div></div>
  <div class="pp-card"><div class="pp-card-front">앞다투어</div><div class="pp-card-back">birin-ketin, poyga qilib</div></div>
  <div class="pp-card"><div class="pp-card-front">A는 물론 B까지</div><div class="pp-card-back">A u yoqda tursin, B ham</div></div>
  <div class="pp-card"><div class="pp-card-front">~ㄹ 뿐만 아니라</div><div class="pp-card-back">~bgina qolmay (qo'shish)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Jamiyat matni qolipi: hodisa → mexanizm → xulosa; bo'sh joy — mexanizmning halqasi.</li>
  <li>3 tuzoq: matn so'zlari+buzuq mantiq · teskari yo'nalish · juda tor/keng javob.</li>
  <li>Doimiy himoya: variantni qo'yib, bo'sh joyning <strong>ikki tomoni</strong> bilan o'qing.</li>
  <li>Imzo belgilaringiz: 즉/~는 셈이다 = qayta aytish; 오히려 = teskari; parallelizm = juftlik.</li>
</ul>
"""},
        ],
    },
]
