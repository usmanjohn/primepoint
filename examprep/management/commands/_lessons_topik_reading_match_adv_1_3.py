# TOPIK II Reading — 32–34-savollar: Murakkab mazmun (내용 일치 고급),
# lessons 1–3 (orders 110–112).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_match_adv_1_3.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "32–34-savollar: Murakkab mazmun (내용 일치 고급)",
    "summary": "Zich ilmiy-tarixiy matnlarda mazmunga mos gapni topish: langar so'z usuli va miqdor tuzoqlari.",
    "icon":    "bi-ui-checks",
    "order":   13,
}

LESSONS = [
    # ── Lesson 1 (order 110) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 고급 1: 32–34-savollar bilan tanishuv — langar so'z usuli",
        "summary": "Belgisiz zich matnda faktlarni langar so'z orqali topish va 모두/일부/절대 tuzoqlari.",
        "order":   110,
        "blocks": [
            {"rich_text": """
<h2>🔎 32–34-savollar: mazmun tekshiruvi — yuqori daraja</h2>
<p>Savol matni tanish: <strong>다음을 읽고 내용이 같은 것을 고르십시오</strong> —
9–12-savollardagi kabi mazmunga mos gapni topasiz. Farq — materialda:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="margin:0 0 6px;"><strong>9–12-da:</strong> e'lon (maydonlari bor!), grafik, qisqa xabar — faktlar ko'zga tashlanadi.</p>
  <p style="margin:0;"><strong>32–34-da:</strong> zich <mark style="background:#dbeafe;">ilmiy-tarixiy matn</mark> — fan, tabiat, tarix, mashhur insonlar. Hech qanday ro'yxat yo'q: faktlar uzun gaplar <strong>ichiga yashiringan</strong>.</p>
</div>
<h3>Langar so'z usuli (키워드 낚시)</h3>
<p>Zich matnda variantni butunlay qidirib bo'lmaydi — <strong>langar</strong> tashlaysiz:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — Variantdan langar so'zni tanlang.</strong> Eng yaxshi langar —
    <mark style="background:#dbeafe;">aniq ot</mark>: raqam, ism, atama (카페인, 자기장,
    측우기...). Umumiy so'zlar (사람, 것) langar bo'lolmaydi — ular hamma joyda bor.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — Langarni matndan toping, atrofini o'qing.</strong> Variantlar odatda
    <strong>matn tartibida</strong> boradi: ① matn boshiga, ④ oxiriga yaqin. Langar topilgan
    gapning o'zi + oldingi/keyingi gap — solishtirish maydoni shu.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — Aynan solishtiring, esda qolganiga ishonmang.</strong> Zich matnda
    xotira aldaydi: "shunaqa degandi shekilli" — yo'q! Har variantni matndagi joyi bilan
    <strong>ko'z bilan</strong> solishtirib chizing (소거법 hech qayerga ketgani yo'q).</p>
  </div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Yangi tuzoq turi — miqdor so'zlari:</strong> matn <strong>일부</strong> (ba'zi)
  desa, variant <strong>모두</strong> (hamma) deydi; matn <strong>~ㄹ 수 있다</strong> (mumkin)
  desa, variant <strong>반드시/절대</strong> (albatta/aslo) deydi. Bitta kichik so'z butun
  gapni noto'g'ri qiladi — 모두·일부·항상·절대·만 so'zlarini ko'rganda to'xtang!
</div>
"""},
            {"rich_text": """
<h3>Ishlangan misol</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">문어는 몸의 색을 자유롭게 바꿀 수 있는
  동물이다. 위험을 느끼면 주변 바위나 모래와 비슷한 색으로 몸을 바꿔 적의 눈을 피한다.
  또한 문어는 도구를 사용할 줄도 안다. 실제로 문어가 야자열매 껍데기를 모아 두었다가 몸을
  숨기는 집으로 쓰는 모습이 관찰되기도 했다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Sakkizoyoq tanasining rangini erkin o'zgartira
  oladigan jonivor. Xavf sezsa, atrofdagi tosh yoki qumga o'xshash rangga kirib, dushman ko'zidan
  yashirinadi. Bundan tashqari, sakkizoyoq asbob ishlatishni ham biladi. Haqiqatan ham sakkizoyoqning
  kokos po'chog'ini yig'ib qo'yib, keyin uni yashirinadigan uy sifatida ishlatgani kuzatilgan.</em></p>
</div>
<p>Variantlarni langar bilan tekshiramiz:</p>
<ul>
  <li>① "문어는 항상 한 가지 색으로 산다" — langar: <strong>색</strong> → matn: "자유롭게 바꿀 수 있는" — <span style="text-decoration:line-through;">항상 한 가지</span> teskari + miqdor tuzog'i (항상!).</li>
  <li>② "문어는 위험할 때 몸의 색을 바꾼다" — langar: <strong>위험</strong> → matn: "위험을 느끼면 ... 색으로 몸을 바꿔" — mos! ✅</li>
  <li>③ "문어는 도구를 쓸 줄 모른다" — langar: <strong>도구</strong> → matn: "사용할 줄도 안다" — teskari.</li>
  <li>④ "문어는 야자열매를 먹이로 먹는다" — langar: <strong>야자열매</strong> → matn: po'chog'ini <strong>uy</strong> qiladi, yemaydi — "aytilgan, lekin boshqacha" tuzog'i!</li>
</ul>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">커피는 원래 음료가 아니라 약으로
  쓰였다. 옛날 아라비아 지역에서는 커피 열매를 끓여서 배가 아픈 사람에게 마시게 했다는
  기록이 있다. 커피가 지금처럼 널리 사랑받는 음료가 된 것은 커피 속 카페인이 잠을 깨우고
  기분을 좋게 해 준다는 사실이 알려지면서부터이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Qahva dastlab ichimlik emas, dori sifatida ishlatilgan.
  Qadimda Arabiston hududida qahva mevasini qaynatib, qorni og'rigan odamga ichirishgani haqida yozuv
  bor. Qahvaning hozirgidek sevimli ichimlikka aylanishi — undagi kofein uyquni ochib, kayfiyatni
  ko'tarishi ma'lum bo'lganidan keyin boshlangan.</em></p>
</div>
""",
             "choices": [
                 {"text": "커피는 처음부터 음료로 사랑받았다. (Qahva boshidanoq ichimlik sifatida sevilgan.)", "is_correct": False},
                 {"text": "옛날에 커피는 약으로 사용되었다. (Qadimda qahva dori sifatida ishlatilgan.)", "is_correct": True},
                 {"text": "카페인은 잠이 잘 오게 만들어 준다. (Kofein uyquni yaxshi keltiradi.)", "is_correct": False},
                 {"text": "커피 열매는 아라비아에서만 자란다. (Qahva mevasi faqat Arabistonda o'sadi.)", "is_correct": False},
             ],
             "explanation": """
<p>Langarlar: ① 음료 → matn "음료가 <strong>아니라</strong> 약으로" — teskari. ② 약 →
"약으로 쓰였다" — mos ✅ (쓰이다 = 사용되다 paraphrase, 9–12-darsdan!). ③ 카페인 →
"잠을 <strong>깨우고</strong>" (uyquni ochadi) — teskari. ④ 아라비아 → matnda faqat
"o'sha yerda ichirishgan" deyilgan, "faqat o'sha yerda <strong>o'sadi</strong>" emas +
<strong>만</strong> (faqat) miqdor tuzog'i!</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">바다거북은 태어난 곳으로 돌아와 알을
  낳는 것으로 유명하다. 수천 킬로미터를 헤엄쳐서 어릴 때 떠났던 바닷가를 다시 찾아오는
  것이다. 과학자들은 바다거북이 지구의 자기장을 이용해 방향을 찾는 것으로 보고 있다.
  하지만 모든 거북이 고향에 돌아오는 데 성공하는 것은 아니다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Dengiz toshbaqasi tug'ilgan joyiga qaytib tuxum
  qo'yishi bilan mashhur. Minglab kilometr suzib, bolaligida tark etgan qirg'oqni qayta topib keladi.
  Olimlar toshbaqa yo'nalishni Yer magnit maydonidan foydalanib topadi deb hisoblaydi. Lekin hamma
  toshbaqa ham vataniga qaytishga muvaffaq bo'lavermaydi.</em></p>
</div>
""",
             "choices": [
                 {"text": "바다거북은 모두 고향에 돌아오는 데 성공한다. (Dengiz toshbaqalarining hammasi vatanga qaytishga erishadi.)", "is_correct": False},
                 {"text": "바다거북은 알을 낳으러 태어난 곳으로 돌아온다. (Dengiz toshbaqasi tuxum qo'ygani tug'ilgan joyiga qaytadi.)", "is_correct": True},
                 {"text": "바다거북은 태양을 보고 방향을 찾는다. (Dengiz toshbaqasi quyoshga qarab yo'nalish topadi.)", "is_correct": False},
                 {"text": "바다거북은 태어난 바닷가 근처에서만 산다. (Dengiz toshbaqasi tug'ilgan qirg'og'i yaqinidagina yashaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>① miqdor tuzog'i to'liq ko'rinishda: matn "<strong>모든</strong> 거북이 ... 것은
<strong>아니다</strong>" (hammasi emas!) — variant esa "모두 성공한다". ③ langar 방향 →
matn: <strong>자기장</strong> (magnit maydon), quyosh emas. ④ "수천 킬로미터를 헤엄쳐" —
uzoqqa suzadi, yaqinida yashamaydi + yana 만 tuzog'i. To'g'risi ②: 1-gapning deyarli
o'zi ✅. Miqdor so'zi bor variantni <strong>ikki marta</strong> tekshiring!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">관찰되다</div><div class="pp-card-back">kuzatilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">도구</div><div class="pp-card-back">asbob, qurol</div></div>
  <div class="pp-card"><div class="pp-card-front">적의 눈을 피하다</div><div class="pp-card-back">dushman ko'zidan yashirinmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">자기장</div><div class="pp-card-back">magnit maydon</div></div>
  <div class="pp-card"><div class="pp-card-front">기록</div><div class="pp-card-back">yozuv, qayd</div></div>
  <div class="pp-card"><div class="pp-card-front">모든 ~ 것은 아니다</div><div class="pp-card-back">hammasi ham ~ emas</div></div>
  <div class="pp-card"><div class="pp-card-front">널리</div><div class="pp-card-back">keng (tarqalgan)</div></div>
  <div class="pp-card"><div class="pp-card-front">유명하다</div><div class="pp-card-back">mashhur</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>32–34 = 9–12 usuli + zich matn: <strong>langar so'z</strong> (aniq ot) → matndan top → atrofini solishtir.</li>
  <li>Variantlar odatda matn tartibida — ①ni boshidan, ④ni oxiridan qidiring.</li>
  <li>Yangi bosh tuzoq: <strong>miqdor so'zlari</strong> (모두·일부·항상·절대·만) — ko'rsangiz to'xtab tekshiring.</li>
  <li>Xotiraga ishonmang — har variantni matndagi joyi bilan ko'z bilan solishtiring.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 111) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 고급 2: Fan va tabiat matnlari",
        "summary": "Hayvonot va tabiat hodisalari matnlarida amaliyot: ega almashinuvi va mutlaq so'z tuzoqlari.",
        "order":   111,
        "blocks": [
            {"rich_text": """
<h2>🐧 Fan va tabiat matnlari</h2>
<p>32–34 blokining eng sevimli materiali — hayvonlarning ajablanarli odatlari va tabiat
hodisalari. Bunday matnlarda ikkita narsani ayniqsa kuzating:</p>
<ul>
  <li><mark style="background:#dbeafe;">Kim nima qiladi?</mark> Matnda ikki "qahramon" bo'lsa
  (ona/ota pingvin, ishchi/malika ari...), variantlar ularning ishlarini <strong>almashtirib</strong>
  beradi — ega almashinuvi tuzog'i zich matnda ayniqsa xavfli.</li>
  <li><mark style="background:#dbeafe;">Istisno bormi?</mark> Ilmiy matn ko'pincha oxirida
  다만/하지만 bilan istisno beradi ("lekin suv kirsa buziladi") — mutlaq so'zli variantlar
  (절대, 어떤 경우에도) aynan shu istisnoga qoqiladi.</li>
</ul>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">황제펭귄은 남극의 추운 겨울에 알을
  낳는 특이한 새이다. 알을 낳은 어미가 먹이를 구하러 바다로 떠나면, 아비가 두 달 동안
  아무것도 먹지 않은 채 발 위에 알을 올려놓고 품는다. 그동안 아비 펭귄들은 수백 마리씩
  모여 서로 몸을 붙여 추위를 견디는데, 바깥쪽에 섰던 펭귄과 안쪽에 있던 펭귄이 계속
  자리를 바꾸면서 함께 살아남는다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Imperator pingvini Antarktidaning sovuq qishida
  tuxum qo'yadigan g'aroyib qush. Tuxum qo'ygan ona ozuqa izlab dengizga ketgach, ota ikki oy davomida
  hech narsa yemagan holda tuxumni oyog'i ustiga qo'yib isitadi. Bu vaqtda ota pingvinlar yuzlab bo'lib
  to'planib, bir-biriga suyanib sovuqqa chidashadi — chetdagi va o'rtadagi pingvinlar doimiy joy
  almashinib, birga omon qolishadi.</em></p>
</div>
""",
             "choices": [
                 {"text": "황제펭귄은 따뜻한 여름에 알을 낳는다. (Imperator pingvini iliq yozda tuxum qo'yadi.)", "is_correct": False},
                 {"text": "아비 펭귄은 두 달 동안 굶으면서 알을 품는다. (Ota pingvin ikki oy och holda tuxum isitadi.)", "is_correct": True},
                 {"text": "어미 펭귄이 알을 품는 동안 아비가 먹이를 구하러 간다. (Ona tuxum isitganda ota ozuqa izlab ketadi.)", "is_correct": False},
                 {"text": "펭귄들은 추위가 오면 각자 흩어져서 지낸다. (Pingvinlar sovuq kelsa har biri tarqalib ketadi.)", "is_correct": False},
             ],
             "explanation": """
<p>③ — ega almashinuvi tuzog'ining klassigi: matnda <strong>ona ketadi, ota isitadi</strong>;
variant rollarni aylantirib qo'ygan. Ikkala rol ham matnda bor, shuning uchun "tanish
eshitiladi" — aynan shu xavfli! ① 겨울↔여름 teskari. ④ "모여 서로 몸을 붙여" (to'planib
suyanadi) — tarqalmaydi. To'g'risi ②: 아무것도 먹지 않은 채 = <strong>굶으면서</strong>
(och holda) paraphrase ✅ + eski tanish -은 채 (Q3–4 juftligi!).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">꿀은 오래 두어도 잘 상하지 않는
  음식이다. 꿀 속에는 물이 매우 적고 당분이 많아서 음식을 상하게 하는 세균이 살기 어렵기
  때문이다. 실제로 수천 년 전 무덤에서 발견된 꿀이 상하지 않은 채 그대로 남아 있었다는
  기록도 있다. 다만 꿀에 물이 들어가면 상할 수 있으므로 보관할 때 주의해야 한다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Asal uzoq tursa ham buzilmaydigan oziq-ovqat.
  Chunki asalda suv juda kam, shakar ko'p bo'lgani uchun ovqatni buzadigan mikroblar yashay olmaydi.
  Haqiqatan ham ming yillar avvalgi maqbaradan topilgan asal buzilmagan holda saqlanganligi haqida
  yozuv bor. Faqat asalga suv kirsa buzilishi mumkin, shuning uchun saqlashda ehtiyot bo'lish kerak.</em></p>
</div>
""",
             "choices": [
                 {"text": "꿀 속에는 물이 많이 들어 있다. (Asalda suv ko'p bo'ladi.)", "is_correct": False},
                 {"text": "꿀은 어떤 경우에도 절대 상하지 않는다. (Asal hech qanday holatda aslo buzilmaydi.)", "is_correct": False},
                 {"text": "세균은 꿀 속에서 살기 어렵다. (Mikroblar asal ichida yashay olmaydi.)", "is_correct": True},
                 {"text": "무덤에서 발견된 꿀은 모두 상해 있었다. (Maqbaradan topilgan asal butunlay buzilgan edi.)", "is_correct": False},
             ],
             "explanation": """
<p>② — mutlaq so'z tuzog'i darslikdagidek: matn oxirida <strong>다만</strong> (faqat)
istisno bor — "suv kirsa buzilishi mumkin". Demak "절대/어떤 경우에도" yolg'on!
① teskari (물이 매우 <strong>적고</strong>). ④ teskari (상하지 않은 채 그대로).
To'g'risi ③: matndagi "세균이 살기 어렵기 때문이다"ning o'zi ✅. Qoida:
<strong>다만/하지만 istisnosi bor matnda mutlaq variant doim noto'g'ri</strong>.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">대나무는 나무처럼 보이지만 사실은
  풀에 가까운 식물이다. 대나무는 자라는 속도가 매우 빨라서 하루에 1미터 넘게 자라기도
  한다. 그런데 대나무는 수십 년 동안 꽃을 피우지 않다가 일생에 단 한 번 꽃을 피우고
  나면 대부분 죽는다. 과학자들은 아직까지 그 이유를 정확하게 밝혀내지 못했다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Bambuk daraxtga o'xshasa-da, aslida o'tga yaqin
  o'simlik. U juda tez o'sadi — kuniga bir metrdan ortiq o'sishi ham mumkin. Lekin bambuk o'nlab
  yillar gullamay yuradi-da, umrida bir martagina gullagach, aksariyati nobud bo'ladi. Olimlar buning
  sababini hozirgacha aniq ochib bera olishgani yo'q.</em></p>
</div>
""",
             "choices": [
                 {"text": "대나무는 풀보다 나무에 가깝다. (Bambuk o'tdan ko'ra daraxtga yaqin.)", "is_correct": False},
                 {"text": "대나무는 해마다 꽃을 피운다. (Bambuk har yili gullaydi.)", "is_correct": False},
                 {"text": "대나무가 꽃을 피운 후 죽는 이유는 아직 밝혀지지 않았다. (Bambukning gullagach nobud bo'lish sababi hali aniqlanmagan.)", "is_correct": True},
                 {"text": "대나무는 자라는 속도가 매우 느리다. (Bambuk juda sekin o'sadi.)", "is_correct": False},
             ],
             "explanation": """
<p>① teskari: "나무처럼 <strong>보이지만</strong> 사실은 풀에 가까운" — -지만dan keyingisi
haqiqat (bog'lovchilar darsi!). ② "일생에 단 한 번" — har yili emas. ④ teskari (매우 빨라서).
To'g'risi ③: "아직까지 이유를 밝혀내지 못했다" = "hali aniqlanmagan" ✅. E'tibor:
<strong>보이지만/같지만</strong> qolipi ilmiy matnning sevimli boshlanishi — "ko'rinishi X,
aslida Y" — variantlar ko'pincha aynan shu farqni sinaydi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">품다</div><div class="pp-card-back">bag'riga bosib isitmoq (tuxumni)</div></div>
  <div class="pp-card"><div class="pp-card-front">굶다</div><div class="pp-card-back">och qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">견디다</div><div class="pp-card-back">chidamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">상하다</div><div class="pp-card-back">buzilmoq (oziq-ovqat)</div></div>
  <div class="pp-card"><div class="pp-card-front">세균</div><div class="pp-card-back">mikrob, bakteriya</div></div>
  <div class="pp-card"><div class="pp-card-front">다만</div><div class="pp-card-back">faqat, biroq (istisno belgisi)</div></div>
  <div class="pp-card"><div class="pp-card-front">꽃을 피우다</div><div class="pp-card-back">gullamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">밝혀내다</div><div class="pp-card-back">ochib bermoq, aniqlamoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Ikki qahramonli matnda rollarni yozib oling: kim ketadi, kim qoladi — ega almashinuviga qarshi eng kuchli himoya.</li>
  <li>다만/하지만 istisnosi bor joyda mutlaq variant (절대, 어떤 경우에도) — avtomatik noto'g'ri.</li>
  <li>-지만 qolipida haqiqat keyingi yarmida: "ko'rinishi X, aslida Y".</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 112) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 고급 3: Tarix va biografiya matnlari + aralash",
        "summary": "Tarixiy voqea va mashhur insonlar haqidagi matnlarda amaliyot — sana, unvon va ixtiro tuzoqlari.",
        "order":   112,
        "blocks": [
            {"rich_text": """
<h2>📜 Tarix va biografiya matnlari</h2>
<p>Uchinchi katta guruh — Koreya tarixi va mashhur insonlar hayoti. Bu matnlarning
o'z "langar turlari" bor:</p>
<ul>
  <li><mark style="background:#dbeafe;">Tartib raqamlari:</mark> 네 번째 왕 (to'rtinchi shoh),
  제5회 — variant raqamni almashtiradi (birinchi? beshinchi?).</li>
  <li><mark style="background:#dbeafe;">Kim nimani yaratdi:</mark> ikki ixtiro bo'lsa
  (soat va yomg'ir o'lchagich), variantlar vazifalarini almashtiradi.</li>
  <li><mark style="background:#dbeafe;">O'shanda ↔ hozir:</mark> 당시 (o'sha paytda) va
  오늘날 (bugungi kunda) holatlari almashtiriladi — zamon so'zlariga qarang.</li>
</ul>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">한글은 조선의 네 번째 왕인 세종대왕이
  만든 글자이다. 당시 백성들은 어려운 한자를 배울 기회가 없어 글을 읽고 쓰지 못했다.
  세종대왕은 이를 안타깝게 여겨 누구나 쉽게 배울 수 있는 글자를 만들었다. 한글이 처음
  나왔을 때 일부 학자들은 새 글자를 반대하기도 했지만, 오늘날 한글은 과학적이고 배우기
  쉬운 글자로 세계에서 인정받고 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Hangul — Choson davlatining to'rtinchi shohi Sejong
  buyuk yaratgan yozuv. O'sha davrda oddiy xalq murakkab xitoy ieroglifini o'rganish imkoniga ega
  bo'lmagani uchun o'qiy-yoza olmasdi. Sejong bundan qayg'urib, har kim oson o'rgana oladigan yozuvni
  yaratdi. Hangul ilk chiqqanida ayrim olimlar yangi yozuvga qarshi ham chiqishdi, lekin bugungi kunda
  hangul ilmiy va o'rganishga oson yozuv sifatida dunyoda e'tirof etilgan.</em></p>
</div>
""",
             "choices": [
                 {"text": "세종대왕은 백성을 위해 한글을 만들었다. (Sejong xalq uchun hangulni yaratdi.)", "is_correct": True},
                 {"text": "한글은 조선의 첫 번째 왕이 만들었다. (Hangulni Chosonning birinchi shohi yaratgan.)", "is_correct": False},
                 {"text": "당시 백성들은 한자를 쉽게 배울 수 있었다. (O'sha davrda xalq ieroglifni oson o'rganardi.)", "is_correct": False},
                 {"text": "모든 학자들이 한글을 처음부터 환영했다. (Barcha olimlar hangulni boshidanoq olqishladi.)", "is_correct": False},
             ],
             "explanation": """
<p>② tartib raqami tuzog'i: <strong>네 번째</strong> (to'rtinchi), birinchi emas.
③ teskari: "배울 기회가 없어 ... 못했다". ④ miqdor tuzog'i: matnda <strong>일부</strong> olimlar
<strong>qarshi chiqqan</strong> — variant esa "hammasi olqishladi" deydi: ikki karra yolg'on. To'g'risi ①:
"백성들이 글을 못 읽는 것을 안타깝게 여겨 ... 만들었다" = xalq uchun yaratdi ✅
(안타깝다 — his-tuyg'u darsidan tanish so'z: birovning holiga achinish!).</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">장영실은 조선 시대의 대표적인
  과학자이다. 낮은 신분으로 태어났지만 뛰어난 재능을 인정받아 궁궐에서 일하게 되었다.
  그는 스스로 시간을 알려 주는 물시계인 자격루와 비의 양을 재는 측우기 등 백성의 생활에
  도움이 되는 기구를 여럿 발명했다. 특히 측우기는 세계에서 가장 먼저 만들어진 것으로
  평가받는다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Jang Yeong-sil — Choson davrining yetakchi olimi.
  Past tabaqada tug'ilgan bo'lsa-da, favqulodda iqtidori e'tirof etilib saroyda ishlaydigan bo'ldi.
  U o'z-o'zidan vaqtni bildiradigan suv soati "jagyeongnu"ni va yomg'ir miqdorini o'lchaydigan
  "cheugugi"ni — xalq turmushiga foydali bir qancha asboblarni ixtiro qildi. Ayniqsa cheugugi dunyoda
  eng birinchi yaratilgan (yomg'ir o'lchagich) deb baholanadi.</em></p>
</div>
""",
             "choices": [
                 {"text": "장영실은 높은 신분의 가문에서 태어났다. (Jang Yeong-sil yuqori tabaqali oilada tug'ilgan.)", "is_correct": False},
                 {"text": "측우기는 시간을 알려 주는 기구이다. (Cheugugi — vaqtni bildiradigan asbob.)", "is_correct": False},
                 {"text": "장영실은 백성에게 도움이 되는 기구들을 발명했다. (Jang Yeong-sil xalqqa foydali asboblarni ixtiro qildi.)", "is_correct": True},
                 {"text": "측우기보다 먼저 만들어진 비 재는 기구가 많았다. (Cheugugidan oldin yaratilgan yomg'ir o'lchagichlar ko'p edi.)", "is_correct": False},
             ],
             "explanation": """
<p>② — "kim nimani yaratdi" tuzog'ining egizagi: <strong>ikki ixtironing vazifalari
almashtirilgan</strong> (자격루 = soat, 측우기 = yomg'ir o'lchagich; variant 측우기ga
soat vazifasini bergan). ① teskari (낮은 신분). ④ teskari: "세계에서 <strong>가장 먼저</strong>"
— undan oldin bo'lmagan! To'g'risi ③: "백성의 생활에 도움이 되는 기구를 여럿 발명했다"ning
o'zi ✅. Ikki atama bo'lsa — vazifalarini yonma-yon yozib oling: chalkashtirib bo'lmaydi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (aralash — tarix + fan).</strong> 다음을 읽고 내용이 같은 것을 고르십시오.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.8;">김치를 담그는 문화인 '김장'은 겨울이
  오기 전에 온 가족과 이웃이 모여 많은 양의 김치를 함께 만드는 풍습이다. 채소를 구하기
  어려운 긴 겨울 동안 채소의 영양을 섭취하기 위해 생긴 지혜이다. 예전에는 집집마다 김장을
  하는 것이 당연한 일이었지만, 요즘은 김치를 사 먹는 가정이 늘면서 김장을 하는 집이 점점
  줄고 있다. 이에 김장 문화를 지키려는 노력도 이어지고 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Kimchi tayyorlash madaniyati "kimjang" — qish
  kelishidan oldin butun oila va qo'shnilar yig'ilib, katta miqdorda kimchini birga tayyorlash odati.
  Sabzavot topish qiyin bo'lgan uzun qish davomida sabzavot ozuqasini olish uchun tug'ilgan hikmat bu.
  Ilgari har xonadonning kimjang qilishi tabiiy ish edi, hozir esa kimchini sotib olib yeydigan oilalar
  ko'payib, kimjang qiladigan xonadonlar tobora kamaymoqda. Shu bois kimjang madaniyatini saqlab
  qolish harakatlari ham davom etmoqda.</em></p>
</div>
""",
             "choices": [
                 {"text": "김장은 여름이 시작될 때 하는 풍습이다. (Kimjang yoz boshlanganda qilinadigan odat.)", "is_correct": False},
                 {"text": "요즘 김장을 하는 집이 예전보다 줄었다. (Hozir kimjang qiladigan xonadonlar ilgarigidan kamaydi.)", "is_correct": True},
                 {"text": "김장은 혼자서 조용히 하는 일이다. (Kimjang yolg'iz, jimgina qilinadigan ish.)", "is_correct": False},
                 {"text": "요즘은 모든 가정이 직접 김치를 만들어 먹는다. (Hozir barcha oilalar kimchini o'zi tayyorlab yeydi.)", "is_correct": False},
             ],
             "explanation": """
<p>① 겨울이 오기 <strong>전에</strong> — qish oldidan (yoz emas). ③ "온 가족과 이웃이
<strong>모여</strong> ... 함께" — yolg'iz emas, jamoa bo'lib! ④ ikki karra yolg'on:
<strong>모든</strong> (miqdor tuzog'i) + teskari (사 먹는 가정이 늘고 있다). To'g'risi ②:
"김장을 하는 집이 점점 줄고 있다"ning paraphrase'i ✅ — 예전↔요즘 zamon qarama-qarshiligi
to'g'ri saqlangan. Mavzu yakunlandi: langar + miqdor + ega + zamon — to'rt nazorat nuqtangiz shu! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">백성</div><div class="pp-card-back">oddiy xalq (tarixiy)</div></div>
  <div class="pp-card"><div class="pp-card-front">신분</div><div class="pp-card-back">tabaqa, ijtimoiy maqom</div></div>
  <div class="pp-card"><div class="pp-card-front">발명하다</div><div class="pp-card-back">ixtiro qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">인정받다</div><div class="pp-card-back">e'tirof etilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">풍습</div><div class="pp-card-back">urf-odat</div></div>
  <div class="pp-card"><div class="pp-card-front">지혜</div><div class="pp-card-back">hikmat, donolik</div></div>
  <div class="pp-card"><div class="pp-card-front">당시 ↔ 오늘날</div><div class="pp-card-back">o'sha paytda ↔ bugungi kunda</div></div>
  <div class="pp-card"><div class="pp-card-front">점점 줄다</div><div class="pp-card-back">tobora kamaymoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Tarix matnining langarları: tartib raqami (네 번째), atama vazifasi (자격루↔측우기), zamon (당시↔오늘날).</li>
  <li>To'rt nazorat nuqtasi: <strong>langar so'z · miqdor so'zi · ega · zamon</strong> — har variantda shu to'rttani tekshiring.</li>
  <li>32–34 uchun ham 소거법 va 4 tuzoq (9–12) asos bo'lib qolaveradi — faqat matn zichroq.</li>
  <li>Uch savolga ~5 daqiqa; langar usuli bilan butun matnni qayta o'qimaysiz.</li>
</ul>
"""},
        ],
    },
]
