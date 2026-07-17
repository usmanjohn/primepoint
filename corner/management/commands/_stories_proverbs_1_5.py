# 속담 이야기 (Koreys maqollari) — stories 1–5. One story = one proverb: literal meaning →
# real meaning → origin/mini-story → dialogue → Uzbek equivalent. Emoji banner = visual
# placeholder until a real image is attached (Story.image / import_corner_images).
# Style: STYLE_GUIDE_CORNER.md section 5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_1_5.py --author=prime

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "속담 이야기 (Koreys maqollari)",
    "description": "Koreys maqollari (속담): maʼnosi, kelib chiqish hikoyasi va hayotda ishlatilishi — lugʻat va savollar bilan.",
    "order":       4,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "원숭이도 나무에서 떨어진다",
        "summary": "«Maymun ham daraxtdan yiqiladi» — eng usta odam ham xato qilishi mumkin. Xato uyat emas!",
        "order":   1,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐒 🌳 💥</div>
<p>"원숭이도 나무에서 떨어진다." 원숭이는 나무 타기의 <span class="cn-word" data-tr="usta, mohir">명수</span>다. 태어나서부터 나무 위에서 살고, 눈을 감고도 이 가지에서 저 가지로 <span class="cn-word" data-pos="verb" data-tr="sakrab oʻtmoq">건너뛴다</span>. 그런 원숭이도 <span class="cn-word" data-pos="adv" data-tr="baʼzan, ahyon-ahyonda">가끔은</span> 나무에서 떨어진다는 뜻이다.</p>
<p>이 속담의 진짜 뜻은 이렇다. <span class="cn-word" data-pos="adv" data-tr="qanchalik">아무리</span> 그 일을 잘하는 사람<strong>이라도</strong> 실수를 <span class="cn-word" data-pos="verb" data-tr="qilmoq (xatoni)">저지를</span> 수 있다. 그러니까 <span class="cn-word" data-tr="mutaxassis">전문가</span>의 실수를 봤을 때, 또는 잘하던 내가 <span class="cn-word" data-pos="adv" data-tr="kutilmaganda">뜻밖에</span> 실패했을 때 이 속담을 쓴다.</p>
<p>옛날이야기 하나를 보자. 어느 숲에 나무를 가장 잘 타는 원숭이가 살았다. 원숭이는 자기 <span class="cn-word" data-tr="mahorat, uquv">솜씨</span>를 <span class="cn-word" data-pos="verb" data-tr="maqtanmoq">자랑하고</span> 싶어서 친구들 앞에서 가장 높은 가지로 올라갔다. "나를 봐! 나는 절대 안 떨어져!" 하지만 <span class="cn-word" data-pos="adv" data-tr="aynan oʻsha payt">바로 그때</span> 손이 <span class="cn-word" data-pos="verb" data-tr="sirpanmoq">미끄러졌고</span>, 원숭이는 쿵 하고 땅에 떨어졌다. 친구들이 <span class="cn-word" data-pos="verb" data-tr="yugurib kelmoq">달려와</span> 물었다. "괜찮아?" 원숭이는 <span class="cn-word" data-pos="adj" data-tr="uyalgan, xijolat">부끄러운</span> 얼굴로 말했다. "잘하는 사람도 <span class="cn-word" data-pos="verb" data-tr="ehtiyot boʻlmoq">조심해야</span> 한다는 걸 오늘 배웠어."</p>
<p>일상 대화에서는 이렇게 쓴다.<br>
"어? 요리사인 네가 국을 태웠어?"<br>
"그러게. 원숭이도 나무에서 떨어진다더니, 딱 내 얘기네."<br>
실수한 사람을 <span class="cn-word" data-pos="verb" data-tr="tanqid qilmoq">비난하지</span> 않고, 오히려 <span class="cn-word" data-pos="verb" data-tr="koʻnglini koʻtarmoq">위로해</span> 주는 따뜻한 속담<strong>인 셈이다</strong>.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Otning toʻrt oyogʻi ham qoqiladi» — xuddi shu maʼno: eng chavandoz ot ham qoqilganidek, eng usta odam ham xato qiladi.
</div>''',
        "grammar": [
            {
                "pattern":  "아무리 -(이)라도",
                "meaning":  "Kuchli yon berish: qanchalik ... boʻlsa ham, hatto ... boʻlsa-da.",
                "examples": ["아무리 전문가라도 실수할 수 있어요.", "아무리 바빠도 밥은 먹어야지요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 셈이다",
                "meaning":  "Xulosa: aslida ... hisoblanadi, ... degan gap.",
                "examples": ["위로해 주는 따뜻한 속담인 셈이다.", "이 정도면 성공한 셈이에요."],
            },
        ],
        "questions": [
            {
                "text":        "이 속담은 언제 사용합니까?",
                "choices":     ["잘하는 사람이 실수했을 때", "원숭이를 구경할 때", "나무에 올라가고 싶을 때"],
                "answer":      0,
                "explanation": "Maqol maymun haqida emas — «ustasi ham xato qiladi» degan maʼnoda, mohir odam kutilmaganda xato qilganda ishlatiladi. Qolgan ikkisi soʻzma-soʻz (literal) tuzoqlar.",
            },
            {
                "text":        "이야기 속 원숭이는 왜 떨어졌습니까?",
                "choices":     ["나무가 부러져서", "자랑하다가 손이 미끄러져서", "친구가 밀어서"],
                "answer":      1,
                "explanation": "Matnda: maqtanib eng baland shoxga chiqdi va «바로 그때 손이 미끄러졌고» — maqtanish payti qoʻli sirpanib ketdi. Daraxt singani yoki doʻsti itargani haqida gap yoʻq.",
            },
            {
                "text":        "이 속담의 분위기는 어떻습니까?",
                "choices":     ["실수한 사람을 비난한다", "실수한 사람을 위로한다", "실수를 금지한다"],
                "answer":      1,
                "explanation": "Oxirgi xatboshida aniq aytilgan: bu maqol xato qilgan odamni tanqid qilmaydi, aksincha koʻnglini koʻtaradi (위로해 주는 따뜻한 속담).",
            },
        ],
    },

    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "우물 안 개구리",
        "summary": "«Quduq ichidagi qurbaqa» — oʻz kichkina dunyosini butun olam deb biladigan, dunyoqarashi tor odam haqida.",
        "order":   2,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐸 🕳️ 🌊</div>
<p>"우물 안 개구리"는 <span class="cn-word" data-tr="quduq">우물</span> 안에 사는 <span class="cn-word" data-tr="qurbaqa">개구리</span>라는 뜻이다. 넓은 세상을 본 적이 없어서 자기가 아는 작은 세계가 <span class="cn-word" data-tr="butun dunyo">전부</span>라고 믿는 사람을 <span class="cn-word" data-pos="verb" data-tr="masxara qilmoq, kinoya qilmoq">비꼬는</span> 말이다.</p>
<p>이 속담의 <span class="cn-word" data-tr="kelib chiqishi">유래</span>는 아주 오래된 중국 책 장자에 나온다. 어느 날 우물 안 개구리가 바다에 사는 <span class="cn-word" data-tr="toshbaqa">거북이</span>를 만났다. 개구리는 <span class="cn-word" data-pos="adv" data-tr="gʻurur bilan">자랑스럽게</span> 말했다. "내 우물을 봐! 물도 있고 돌도 있고, 여기가 세상에서 가장 <span class="cn-word" data-pos="adj" data-tr="ajoyib">멋진</span> 곳이야!" 거북이는 <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> 바다 이야기를 해 주었다. "바다는 천 개의 우물을 넣어도 <span class="cn-word" data-pos="adj" data-tr="toʻlmaydigan">차지 않을</span> 만큼 넓고 깊어." 개구리는 그 말을 듣<strong>고 나서야</strong> 자기 세계가 <span class="cn-word" data-pos="adv" data-tr="naqadar">얼마나</span> 작았는지 <span class="cn-word" data-pos="verb" data-tr="anglamoq">깨달았다</span>.</p>
<p>오늘날에는 이렇게 쓴다. 시골에서 축구를 제일 잘하던 소년이 서울 대회에 나가서 <span class="cn-word" data-pos="adv" data-tr="birinchi bosqichdayoq">첫 경기에서</span> 지고 말았다. 소년은 말했다. "내가 우물 안 개구리였구나. 세상은 넓고 잘하는 사람은 <span class="cn-word" data-pos="adj" data-tr="son-sanoqsiz">수없이</span> 많네."</p>
<p>중요한 점: 이 속담은 남을 <span class="cn-word" data-pos="verb" data-tr="kamsitmoq">깎아내릴</span> 때보다, 자기 <span class="cn-word" data-tr="chegara, doira">한계</span>를 깨닫고 더 넓은 세상으로 나가겠다고 <span class="cn-word" data-pos="verb" data-tr="qaror qilmoq">다짐할</span> 때 쓰면 가장 아름답다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> Aynan shu obraz oʻzbek tilida ham tushunarli — «quduq tagidagi qurbaqa». Maʼnodoshi: dunyoni tirqishdan koʻradigan, oʻz qobigʻiga oʻralib olgan odam.
</div>''',
        "grammar": [
            {
                "pattern":  "-고 나서야",
                "meaning":  "Kech anglash: faqat ...gandan keyingina (undan oldin emas).",
                "examples": ["거북이의 말을 듣고 나서야 깨달았다.", "잃고 나서야 소중함을 알았어요."],
            },
            {
                "pattern":  "-(으)ㄹ 만큼",
                "meaning":  "Daraja: ...adigan darajada, ...guday.",
                "examples": ["천 개의 우물을 넣어도 차지 않을 만큼 넓다.", "말이 안 나올 만큼 놀랐어요."],
            },
        ],
        "questions": [
            {
                "text":        "개구리는 언제 자기 세계가 작다는 것을 깨달았습니까?",
                "choices":     ["우물에서 나간 후에", "거북이의 바다 이야기를 들은 후에", "서울 대회에서 진 후에"],
                "answer":      1,
                "explanation": "Matnda: «그 말을 듣고 나서야 ... 깨달았다» — toshbaqaning dengiz haqidagi gapini eshitgandan keyingina angladi. Qurbaqa quduqdan chiqmagan; Seul musobaqasi esa bola haqidagi zamonaviy misol.",
            },
            {
                "text":        "이 속담을 가장 잘 쓴 사람은 누구입니까?",
                "choices":     ["친구를 놀리려고 쓴 사람", "자기 한계를 깨닫고 더 배우기로 한 사람", "우물을 파고 있는 사람"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: bu maqol oʻz chegarasini anglab, kengroq dunyoga chiqishga qaror qilganda «eng chiroyli» ishlatiladi. Birovni kamsitish — maqolning yomon qoʻllanishi; uchinchi variant soʻzma-soʻz tuzoq.",
            },
        ],
    },

    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "호랑이도 제 말 하면 온다",
        "summary": "«Yoʻlbarsni tilga olsang, oʻzi keladi» — kimnidir gapirsangiz, xuddi oʻsha odam paydo boʻladi. Gʻiybatdan ehtiyot boʻling!",
        "order":   3,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐯 💬 😱</div>
<p>"호랑이도 제 말 하면 온다." 호랑이 이야기를 하면 <span class="cn-word" data-pos="adv" data-tr="xuddi, goʻyo atayin">마치 기다렸다는 듯이</span> 진짜 호랑이가 나타난다는 뜻이다. 어떤 사람에 대해 이야기하고 있는데 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> 바로 그 사람이 나타났을 때 쓰는 속담이다.</p>
<p>왜 하필 호랑이일까? 옛날 한국의 산에는 호랑이가 정말 많았다. 사람들은 호랑이를 너무 <span class="cn-word" data-pos="verb" data-tr="qoʻrqmoq">두려워해서</span> 밤에는 그 이름조차 <span class="cn-word" data-pos="adv" data-tr="ochiq, dadil">함부로</span> 말하지 않았다. "호랑이"라고 말하는 <span class="cn-word" data-pos="adv" data-tr="shu zahoti">순간</span> 진짜로 나타날까 봐 무서웠기 때문이다. 그만큼 호랑이는 한국 사람들에게 <span class="cn-word" data-pos="adj" data-tr="yaqin va dahshatli">가깝고도 무서운</span> 존재였다.</p>
<p>지수와 민호의 대화를 보자.<br>
"민호야, 우리 반 반장 있잖아. 어제 또 <span class="cn-word" data-pos="verb" data-tr="kechikmoq">지각했대</span>."<br>
"진짜? 반장이 <span class="cn-word" data-pos="adv" data-tr="yana">또</span>?"<br>
바로 그때 교실 문이 열리고 반장이 들어왔다. 두 사람은 <span class="cn-word" data-pos="verb" data-tr="qotib qolmoq">얼어붙었다</span>.<br>
"호랑이도 제 말 하면 온다더니..."</p>
<p>이 속담의 <span class="cn-word" data-tr="saboq, oʻgit">교훈</span>은 분명하다. 그 자리에 없는 사람 이야기, 특히 <span class="cn-word" data-tr="gʻiybat">뒷담화</span>는 하지 말라는 것이다. 세상은 좁고, 말은 <span class="cn-word" data-pos="adj" data-tr="tez">빠르며</span>, 사람은 언제 어디서 나타날지 모른다. 남의 이야기를 하<strong>다가</strong> <span class="cn-word" data-pos="adj" data-tr="noqulay">난처한</span> 상황에 빠지지 않으려면, 없는 사람에 대해서도 좋은 말만 하는 것이 <span class="cn-word" data-pos="adj" data-tr="oqilona">현명하다</span>.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Boʻrini yoʻqlasang, qulogʻi koʻrinadi» — aynan shu holat! Koreyada boʻri oʻrnida yoʻlbars: qadimgi Koreya togʻlarining eng dahshatli hayvoni.
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ까 봐",
                "meaning":  "Xavotir: ... boʻlib qolarmikan deb (qoʻrqib).",
                "examples": ["진짜로 나타날까 봐 무서웠다.", "늦을까 봐 일찍 나왔어요."],
            },
            {
                "pattern":  "-다가",
                "meaning":  "Bir ish davomida boshqa narsa yuz berishi: ...ayotib, ...ayotganda.",
                "examples": ["남의 이야기를 하다가 난처해질 수 있다.", "길을 걷다가 친구를 만났어요."],
            },
        ],
        "questions": [
            {
                "text":        "옛날 한국 사람들은 왜 밤에 호랑이의 이름을 말하지 않았습니까?",
                "choices":     ["이름이 너무 길어서", "말하면 진짜 나타날까 봐 무서워서", "호랑이가 이름을 싫어해서"],
                "answer":      1,
                "explanation": "Matnda aniq: «진짜로 나타날까 봐 무서웠기 때문이다» — nomini aytsa, chindan paydo boʻlib qolishidan qoʻrqishgan. Qolgan ikkisi matnda yoʻq.",
            },
            {
                "text":        "이 속담이 주는 교훈은 무엇입니까?",
                "choices":     ["호랑이를 조심해야 한다", "없는 사람의 뒷담화를 하지 말아야 한다", "교실 문을 잘 닫아야 한다"],
                "answer":      1,
                "explanation": "Oxirgi xatboshida: yoʻq odam haqida, ayniqsa gʻiybat qilmaslik kerak — chunki u har lahzada kirib kelishi mumkin. ① soʻzma-soʻz tuzoq, ③ dialogdagi detal xolos.",
            },
        ],
    },

    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "티끌 모아 태산",
        "summary": "«Zarra yigʻilib — togʻ boʻladi» — kichkina narsalar toʻplansa, ulkan natija chiqadi. Tejamkorlik va sabr maqoli.",
        "order":   4,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">✨ ➕ ⛰️</div>
<p>"티끌 모아 태산." <span class="cn-word" data-tr="zarra, chang zarrasi">티끌</span>은 눈에 잘 보이지도 않는 아주 작은 먼지다. <span class="cn-word" data-tr="ulkan togʻ">태산</span>은 중국에 있는 크고 유명한 산의 이름이다. 즉, 아무리 작은 것이라도 <span class="cn-word" data-pos="adv" data-tr="toʻxtovsiz">꾸준히</span> 모으면 산처럼 커진다는 뜻이다.</p>
<p>지수의 이야기를 보자. 지수는 고등학생 때부터 오백 원짜리 <span class="cn-word" data-tr="tanga">동전</span>이 생길 때마다 큰 <span class="cn-word" data-tr="shisha idish">유리병</span>에 넣었다. 친구들은 <span class="cn-word" data-pos="verb" data-tr="kulmoq">웃었다</span>. "오백 원으로 뭘 할 수 있어?" 하지만 지수는 <span class="cn-word" data-pos="adv" data-tr="parvo qilmay">아랑곳하지 않고</span> 삼 년 동안 동전을 모았다. <span class="cn-word" data-pos="verb" data-tr="bitirmoq">졸업하는</span> 날 병을 열어 보니 무려 사십만 원이 들어 있었다. 지수는 그 돈으로 <span class="cn-word" data-pos="adv" data-tr="qadrdon">그토록</span> 갖고 싶던 카메라를 샀다. 작은 동전을 <span class="cn-word" data-pos="verb" data-tr="mensimay qaramoq">무시하던</span> 친구들은 아무것도 사지 못했다.</p>
<p>이 속담은 돈에만 쓰는 것이 아니다. 하루에 단어 다섯 개씩 외우<strong>다 보면</strong> 일 년 뒤에는 천팔백 개가 넘는다. 하루 십 분씩 운동해도 일 년이면 육십 시간이 넘는 <span class="cn-word" data-tr="mashgʻulot">훈련</span>이 된다. 공부도, 건강도, <span class="cn-word" data-tr="doʻstlik">우정</span>도 — 큰 것은 언제나 작은 것들이 <span class="cn-word" data-pos="verb" data-tr="toʻplanmoq">쌓여서</span> 만들어진다.</p>
<p>대화에서는 이렇게 쓴다.<br>
"매일 오백 원 저금해서 언제 부자 되냐?"<br>
"티끌 모아 태산이라고 했어. <span class="cn-word" data-pos="adv" data-tr="kutib tur">두고 봐</span>."</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Tomchi-tomchi koʻl boʻlur» — tomchilar yigʻilib koʻl boʻlgani kabi, zarralar yigʻilib togʻ boʻladi. Maʼnosi bir xil: kichikni mensimang!
</div>''',
        "grammar": [
            {
                "pattern":  "-다 보면",
                "meaning":  "Davomiy harakat natijasi: ...ayotgan boʻlsangiz, oxiri ...ga olib keladi.",
                "examples": ["매일 외우다 보면 천 개가 넘는다.", "계속 연습하다 보면 늘어요."],
            },
            {
                "pattern":  "무려",
                "meaning":  "Hayratli miqdor oldidan: naqd, roppa-rosa (koʻpligini taʼkidlaydi).",
                "examples": ["무려 사십만 원이 들어 있었다.", "그 공연에 무려 만 명이 왔대요."],
            },
        ],
        "questions": [
            {
                "text":        "지수는 어떻게 카메라를 살 수 있었습니까?",
                "choices":     ["부모님이 사 주셔서", "삼 년 동안 오백 원짜리 동전을 모아서", "친구들이 돈을 빌려줘서"],
                "answer":      1,
                "explanation": "Matnda: uch yil davomida besh yuz vonlik tangalarni shisha idishga yigʻib, bitiruv kuni 400 ming von chiqdi — shu pulga kamera oldi. Ota-ona yoki doʻstlar puli haqida gap yoʻq (doʻstlar aksincha kulgan).",
            },
            {
                "text":        "이 속담은 돈 이외에 어디에 쓸 수 있습니까?",
                "choices":     ["공부나 운동 같은 꾸준한 노력에", "산에 올라갈 때만", "동전을 셀 때만"],
                "answer":      0,
                "explanation": "Uchinchi xatboshi: kuniga 5 ta soʻz, kuniga 10 daqiqa sport — kichik saʼy-harakatlar toʻplanib katta natija beradi. Maqol pulgagina emas, har qanday toʻplanadigan mehnatga tegishli.",
            },
        ],
    },

    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "금강산도 식후경",
        "summary": "«Kumgang togʻi ham ovqatdan keyin» — qorin och boʻlsa, eng goʻzal manzara ham koʻzga koʻrinmaydi. Avval taom!",
        "order":   5,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🍚 ⛰️ 😋</div>
<p>"금강산도 식후경." <span class="cn-word" data-tr="Kumgang togʻi">금강산</span>은 한국에서 가장 아름답다고 하는 전설적인 산이다. <span class="cn-word" data-tr="ovqatdan keyin tomosha">식후경</span>은 "밥을 먹은 후에 <span class="cn-word" data-pos="verb" data-tr="tomosha qilmoq">구경한다</span>"는 뜻이다. 즉, 아무리 아름다운 금강산이라도 배가 부른 <span class="cn-word" data-pos="adv" data-tr="keyingina">후에야</span> 눈에 들어온다는 말이다.</p>
<p>사람의 마음이 <span class="cn-word" data-pos="adv" data-tr="aynan shunday">딱 그렇다</span>. 배가 <span class="cn-word" data-pos="adj" data-tr="och">고프면</span> 세상에서 제일 멋진 <span class="cn-word" data-tr="manzara">경치</span>도, 제일 재미있는 이야기도 <span class="cn-word" data-tr="qiziq">흥미</span>가 없다. 머릿속에는 <span class="cn-word" data-pos="adv" data-tr="faqat">오직</span> 밥 생각뿐이다. 그래서 무슨 일을 하든 <span class="cn-word" data-pos="adv" data-tr="avvalo">먼저</span> 배를 <span class="cn-word" data-pos="verb" data-tr="toʻydirmoq">채우고</span> 시작하자고 할 때 이 속담을 쓴다.</p>
<p>민호네 가족의 여행 이야기다. 아버지는 산 <span class="cn-word" data-tr="tepalik, choʻqqi">정상</span>까지 올라가서 경치를 보자고 했다. 하지만 <span class="cn-word" data-pos="adj" data-tr="kichik, kenja">어린</span> 동생이 <span class="cn-word" data-pos="verb" data-tr="yigʻlamoq">울기</span> 시작했다. "배고파! 밥부터 먹을래!" 어머니가 웃으며 말했다. "금강산도 식후경<strong>이라잖아요</strong>. 우리 먼저 김밥부터 먹어요." 가족은 나무 아래에서 김밥을 먹었다. <span class="cn-word" data-pos="adv" data-tr="ajablanarlisi">신기하게도</span> 밥을 먹고 나니 산이 두 배는 더 아름다워 보였다.</p>
<p>회사에서도 자주 들을 수 있다.<br>
"회의부터 할까요, 점심부터 먹을까요?"<br>
"금강산도 식후경이지요. 밥부터 먹읍시다!"</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Avval taom, baʼdaz kalom» — avval ovqat, keyin suhbat! Koreyslar «keyin tomosha» deydi, biz «keyin soʻz» deymiz — ikkalasida ham gʻolib: qorin. 😄
</div>''',
        "grammar": [
            {
                "pattern":  "-(이)라잖아요",
                "meaning":  "Maʼlum gapga ishora: axir ... deyishadi-ku (maqol/mashhur gapni eslatish).",
                "examples": ["금강산도 식후경이라잖아요.", "시작이 반이라잖아요. 일단 해 보세요."],
            },
            {
                "pattern":  "-고 나니(까)",
                "meaning":  "...gandan keyin (yangi holat sezildi).",
                "examples": ["밥을 먹고 나니 산이 더 아름다워 보였다.", "말하고 나니까 마음이 편해졌어요."],
            },
        ],
        "questions": [
            {
                "text":        "이 속담의 뜻으로 가장 알맞은 것은 무엇입니까?",
                "choices":     ["금강산은 밥집이 많다", "배가 고프면 아름다운 것도 즐길 수 없다", "산에 올라가기 전에 운동해야 한다"],
                "answer":      1,
                "explanation": "Ikkinchi xatboshida ochiq aytilgan: qorin och boʻlsa eng goʻzal manzara ham qiziq emas — shuning uchun avval ovqat. ① va ③ soʻzma-soʻz tuzoqlar.",
            },
            {
                "text":        "밥을 먹은 후에 가족에게 무슨 일이 있었습니까?",
                "choices":     ["산이 더 아름다워 보였다", "동생이 다시 울었다", "집으로 돌아갔다"],
                "answer":      0,
                "explanation": "Matnda: «밥을 먹고 나니 산이 두 배는 더 아름다워 보였다» — ovqatdan keyin togʻ ikki barobar goʻzal koʻrindi. Bu maqolning isboti: toʻq qoringa dunyo chiroyli!",
            },
        ],
    },
]
