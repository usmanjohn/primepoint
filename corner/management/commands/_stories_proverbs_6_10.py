# 속담 이야기 (Koreys maqollari) — stories 6–10. Style: STYLE_GUIDE_CORNER.md section 5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_6_10.py --author=prime

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
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "소 잃고 외양간 고친다",
        "summary": "«Sigirni yoʻqotib, ogʻilni tuzatadi» — ish oʻtib boʻlgach chora koʻrish haqida. Oldini olish har doim arzon!",
        "order":   6,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐄 🚪 🔨</div>
<p>"소 잃고 외양간 고친다." <span class="cn-word" data-tr="ogʻil, molxona">외양간</span>은 소가 사는 집이다. 소를 <span class="cn-word" data-pos="verb" data-tr="yoʻqotmoq">잃어버린</span> 후에야 <span class="cn-word" data-pos="adj" data-tr="buzilgan, siniq">부서진</span> 외양간을 고친다는 뜻이다. 일이 이미 <span class="cn-word" data-pos="adv" data-tr="notoʻgʻri, buzilib">잘못된</span> 뒤에 <span class="cn-word" data-pos="adv" data-tr="endi, kechikkan holda">뒤늦게</span> 손을 쓰는 사람을 두고 하는 말이다.</p>
<p>옛날 어느 마을에 <span class="cn-word" data-pos="adj" data-tr="dangasa">게으른</span> 농부가 살았다. 외양간 문이 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> 오래전부터 <span class="cn-word" data-pos="verb" data-tr="lang ochilib qolmoq">덜렁거렸지만</span> 농부는 "내일 고치지, 뭐" 하며 매일 미루었다. 어느 날 밤, 소가 열린 문으로 나가 <span class="cn-word" data-pos="verb" data-tr="gʻoyib boʻlmoq">사라지고</span> 말았다. 농부는 그제야 울면서 <span class="cn-word" data-tr="taxta">널빤지</span>와 <span class="cn-word" data-tr="mix">못</span>을 들고 나와 문을 고쳤다. 이웃이 <span class="cn-word" data-pos="verb" data-tr="chuqur xoʻrsinmoq">한숨을 쉬며</span> 말했다. "미리 고쳤<strong>더라면</strong> 소를 잃지 않았을 텐데. 소 잃고 외양간 고치는구먼."</p>
<p>오늘날에도 <span class="cn-word" data-pos="adv" data-tr="xuddi shunday">똑같이</span> 쓴다. 시험에 떨어진 후에야 책을 사는 학생, 큰비가 온 후에야 <span class="cn-word" data-tr="tom">지붕</span>을 고치는 집주인, 건강을 잃은 후에야 운동을 시작하는 사람 — 모두 "소 잃고 외양간 고친다"는 말을 듣는다.</p>
<p>하지만 이 속담에는 또 하나의 <span class="cn-word" data-tr="saboq, oʻgit">교훈</span>이 숨어 있다. 늦었더라도 외양간은 고쳐야 한다. 다음 소를 지키기 위해서다. <span class="cn-word" data-pos="adv" data-tr="eng yaxshisi">가장 좋은 것은</span> 미리 <span class="cn-word" data-pos="verb" data-tr="tayyorlanmoq">대비하는</span> 것이고, 그다음으로 좋은 것은 지금이라도 고치는 것이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Toʻydan keyin nogʻora» — toʻy oʻtib boʻlgach nogʻora chalishdan foyda yoʻq. Ish oʻtgach koʻrilgan chora — kechikkan chora.
</div>''',
        "grammar": [
            {
                "pattern":  "-았/었더라면",
                "meaning":  "Oʻtmishdagi afsus: agar oʻshanda ...ganda edi (aslida boʻlmagan).",
                "examples": ["미리 고쳤더라면 소를 잃지 않았을 텐데.", "일찍 출발했더라면 늦지 않았을 거예요."],
            },
            {
                "pattern":  "-고 말다",
                "meaning":  "Istalmagan natija: oxiri ... boʻlib qoldi (afsus ohangi).",
                "examples": ["소가 사라지고 말았다.", "너무 피곤해서 잠들고 말았어요."],
            },
        ],
        "questions": [
            {
                "text":        "농부는 왜 소를 잃었습니까?",
                "choices":     ["도둑이 벽을 부숴서", "문 고치는 일을 계속 미뤄서", "소가 병에 걸려서"],
                "answer":      1,
                "explanation": "Matnda: eshik allaqachon lang ochilib qolgan edi, fermer esa «내일 고치지» deb har kuni kechiktirdi — natijada sigir ochiq eshikdan chiqib ketdi. Oʻgʻri ham, kasallik ham matnda yoʻq.",
            },
            {
                "text":        "이 속담과 어울리는 사람은 누구입니까?",
                "choices":     ["시험 전에 미리 공부하는 학생", "시험에 떨어진 후에야 책을 사는 학생", "매일 운동하는 사람"],
                "answer":      1,
                "explanation": "Maqol ish buzilgandan KEYIN chora koʻradiganlar haqida — imtihondan yiqilgach kitob sotib olish aynan shu. Oldindan tayyorlanadiganlar esa maqolning teskarisi.",
            },
            {
                "text":        "글쓴이에 따르면 가장 좋은 것은 무엇입니까?",
                "choices":     ["늦게라도 고치는 것", "미리 대비하는 것", "외양간을 없애는 것"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: eng yaxshisi — oldindan tayyorlanish (미리 대비하는 것); undan keyingisi — hech boʻlmasa hozir tuzatish. Demak kechikkan chora ham foydali, lekin eng yaxshisi emas.",
            },
        ],
    },

    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "낮말은 새가 듣고 밤말은 쥐가 듣는다",
        "summary": "«Kunduzgi gapni qush, tungi gapni sichqon eshitadi» — hech qayerda sir saqlanib qolmaydi. Devorning ham qulogʻi bor!",
        "order":   7,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">☀️🐦 🌙🐭</div>
<p>"낮말은 새가 듣고 밤말은 쥐가 듣는다." 낮에 하는 말은 하늘의 새가 듣고, 밤에 하는 말은 벽 속의 <span class="cn-word" data-tr="sichqon">쥐</span>가 듣는다는 뜻이다. 아무도 없는 것 같아도 말은 <span class="cn-word" data-pos="adv" data-tr="qanday boʻlmasin">어떻게든</span> 밖으로 <span class="cn-word" data-pos="verb" data-tr="tarqalib chiqmoq">새어 나가기</span> 마련이라는 <span class="cn-word" data-tr="ogohlantirish">경고</span>다.</p>
<p>왜 새와 쥐일까? 옛날 한국의 집은 나무와 <span class="cn-word" data-tr="qogʻoz">종이</span>로 지어졌다. 벽은 <span class="cn-word" data-pos="adj" data-tr="yupqa">얇았고</span>, 마당에는 늘 새가 있었으며, 벽과 <span class="cn-word" data-tr="pol">마루</span> 밑에는 쥐가 살았다. 사람들은 "우리 집에서 한 말을 어떻게 <span class="cn-word" data-tr="butun qishloq">온 동네</span>가 다 알지?"라고 놀라며, 새와 쥐가 말을 <span class="cn-word" data-pos="verb" data-tr="tashib yurmoq">옮긴다고</span> 상상했던 것이다.</p>
<p>회사에서 있었던 일이다. 두 <span class="cn-word" data-tr="hamkasb">동료</span>가 <span class="cn-word" data-tr="tushlik xonasi">휴게실</span>에서 <span class="cn-word" data-pos="adv" data-tr="pichirlab">속닥속닥</span> 부장님 <span class="cn-word" data-tr="gʻiybat">흉을</span> 봤다. "여긴 아무도 없으니까 괜찮아." 하지만 다음 날, 부장님이 두 사람을 불렀다. "내 이야기, 재미있었나?" <span class="cn-word" data-pos="adv" data-tr="maʼlum boʻlishicha">알고 보니</span> 옆방에 다른 팀 직원이 있었던 것이다. 아무도 없는 것 같<strong>더라도</strong> 말은 조심해야 한다.</p>
<p>이 속담은 <span class="cn-word" data-tr="sir">비밀</span>을 지키는 가장 <span class="cn-word" data-pos="adj" data-tr="ishonchli">확실한</span> 방법도 알려 준다. 그것은 바로 — <span class="cn-word" data-pos="adv" data-tr="umuman, aslo">아예</span> 말하지 않는 것이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Devorning ham qulogʻi bor» — hech kim yoʻq deb oʻylaganingizda ham gapingizni kimdir eshitib turadi. Koreyslarda devor oʻrnida — qush va sichqon!
</div>''',
        "grammar": [
            {
                "pattern":  "-기 마련이다",
                "meaning":  "Tabiiy qonuniyat: ...ishi tabiiy, baribir ... boʻladi.",
                "examples": ["말은 새어 나가기 마련이다.", "비밀은 언젠가 밝혀지기 마련이에요."],
            },
            {
                "pattern":  "-더라도",
                "meaning":  "Kuchli shart-yon berish: hatto ... boʻlsa ham.",
                "examples": ["아무도 없더라도 말은 조심해야 한다.", "힘들더라도 포기하지 마세요."],
            },
        ],
        "questions": [
            {
                "text":        "옛날 사람들은 왜 새와 쥐가 말을 옮긴다고 상상했습니까?",
                "choices":     ["새와 쥐가 말을 할 수 있어서", "집의 벽이 얇고 새와 쥐가 늘 가까이 있어서", "새와 쥐를 좋아해서"],
                "answer":      1,
                "explanation": "Matnda: uylar yogʻoch-qogʻozdan, devorlar yupqa, hovlida qush, pol ostida sichqon — gap qanday tarqalganini tushunolmagan odamlar shularni «gap tashuvchi» deb tasavvur qilgan.",
            },
            {
                "text":        "회사 이야기에서 두 동료의 실수는 무엇이었습니까?",
                "choices":     ["부장님에게 직접 말한 것", "아무도 없다고 믿고 흉을 본 것", "회의에 늦은 것"],
                "answer":      1,
                "explanation": "Ular «여긴 아무도 없으니까 괜찮아» deb ishonib gʻiybat qilishdi — vaholanki yon xonada boshqa xodim bor edi. Maqolning aynan isboti.",
            },
            {
                "text":        "글에 따르면 비밀을 지키는 가장 확실한 방법은 무엇입니까?",
                "choices":     ["밤에만 말하는 것", "작은 소리로 말하는 것", "아예 말하지 않는 것"],
                "answer":      2,
                "explanation": "Oxirgi jumla: eng ishonchli yoʻl — umuman aytmaslik (아예 말하지 않는 것). Kechasi yoki pichirlab aytish ham xavfsiz emas — sichqon baribir eshitadi! 😄",
            },
        ],
    },

    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "세 살 버릇 여든까지 간다",
        "summary": "«Uch yoshdagi odat saksongacha boradi» — bolalikdagi odat umr boʻyi qoladi. Yaxshi odatni erta boshlang!",
        "order":   8,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">👶 ➡️ 👴</div>
<p>"세 살 버릇 여든까지 간다." 세 살 때 생긴 <span class="cn-word" data-tr="odat">버릇</span>이 <span class="cn-word" data-tr="sakson yosh">여든</span>까지 간다는 뜻이다. 어릴 때 몸에 <span class="cn-word" data-pos="verb" data-tr="singib qolmoq">배어 버린</span> 습관은 나이가 들어도 <span class="cn-word" data-pos="adv" data-tr="osonlikcha">쉽게</span> 고쳐지지 않는다는 말이다.</p>
<p>민호 할아버지의 이야기가 좋은 <span class="cn-word" data-tr="misol">예</span>다. 할아버지는 일흔이 넘었는데 아직도 <span class="cn-word" data-pos="adj" data-tr="xavotirlangan">긴장하면</span> 손톱을 <span class="cn-word" data-pos="verb" data-tr="tishlamoq">깨문다</span>. 어릴 때 생긴 버릇이다. 할아버지는 웃으며 말한다. "칠십 년을 <span class="cn-word" data-pos="verb" data-tr="urinmoq">노력해도</span> 안 고쳐지더라. 그러니까 너희는 <span class="cn-word" data-pos="adv" data-tr="boshidanoq">처음부터</span> 좋은 버릇을 만들어라."</p>
<p>과학도 이 속담이 옳다고 말한다. 어릴수록 <span class="cn-word" data-tr="miya">뇌</span>는 <span class="cn-word" data-pos="adj" data-tr="yumshoq, egiluvchan">말랑말랑해서</span> 한번 만들어진 <span class="cn-word" data-tr="yoʻl, iz">길</span>이 깊이 <span class="cn-word" data-pos="verb" data-tr="oʻrnashmoq">새겨진다</span>. 그래서 버릇은 오래될<strong>수록</strong> 고치기 어려워지<strong>기 마련이다</strong>.</p>
<p>하지만 이 속담을 <span class="cn-word" data-pos="adv" data-tr="teskari tomondan">거꾸로</span> 읽으면 희망이 된다. 나쁜 버릇만 여든까지 가는 것이 아니다. 좋은 버릇도 여든까지 간다! 지금 책 읽는 버릇, 아침에 일찍 일어나는 버릇, <span class="cn-word" data-pos="verb" data-tr="tejamoq">저축하는</span> 버릇을 만들면, 그 버릇이 평생 당신을 지켜 줄 것이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Qush uyasida koʻrganini qiladi» — bolalikda singdirilgan narsa umrga hamroh. Yana biri: «Yoshlikdagi odat — toshga oʻyilgan naqsh».
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ수록",
                "meaning":  "Ortib borish: qancha ... boʻlsa, shuncha ...",
                "examples": ["버릇은 오래될수록 고치기 어렵다.", "한국어는 배울수록 재미있어요."],
            },
            {
                "pattern":  "-아/어 버리다",
                "meaning":  "Toʻliq/qaytarib boʻlmas natija: butunlay ...b qoʻymoq/qolmoq.",
                "examples": ["몸에 배어 버린 습관은 고치기 어렵다.", "숙제를 다 해 버렸어요."],
            },
        ],
        "questions": [
            {
                "text":        "할아버지의 이야기는 무엇을 보여 줍니까?",
                "choices":     ["나이가 들면 버릇이 저절로 없어진다", "어릴 때 생긴 버릇은 칠십 년이 지나도 남는다", "손톱을 깨물면 건강에 좋다"],
                "answer":      1,
                "explanation": "Yetmish yoshdan oshgan bobo hali ham hayajonlansa tirnogʻini tishlaydi — bolalikdagi odat 70 yil urinishga qaramay ketmagan. Maqolning jonli isboti.",
            },
            {
                "text":        "이 속담을 '거꾸로 읽으면' 어떤 희망이 됩니까?",
                "choices":     ["나쁜 버릇도 언젠가 사라진다", "좋은 버릇도 평생 남는다", "여든이 되면 새 버릇이 생긴다"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: nafaqat yomon, balki YAXSHI odat ham saksongacha boradi — hozir kitob oʻqish, erta turish odatini qursangiz, u umr boʻyi sizni asraydi.",
            },
        ],
    },

    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "등잔 밑이 어둡다",
        "summary": "«Chiroq tagi qorongʻu» — izlagan narsangiz koʻpincha burningizning tagida boʻladi, lekin aynan u yer koʻrinmaydi.",
        "order":   9,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🪔 ⬇️ 🌑</div>
<p>"등잔 밑이 어둡다." <span class="cn-word" data-tr="moy chiroq">등잔</span>은 전기가 없던 시절, 기름으로 불을 켜던 작은 <span class="cn-word" data-tr="chiroq">램프</span>다. 등잔은 방 전체를 밝히지만, <span class="cn-word" data-pos="adv" data-tr="qizigʻi shundaki">정작</span> 등잔 <span class="cn-word" data-tr="tagi, osti">밑</span>은 <span class="cn-word" data-tr="soya">그림자</span> 때문에 가장 어둡다. 가까이 있는 것을 <span class="cn-word" data-pos="adv" data-tr="aksincha">오히려</span> 더 모른다는 뜻이다.</p>
<p>할머니의 <span class="cn-word" data-tr="koʻzoynak">안경</span> 이야기는 누구나 안다. 할머니가 온 집 안을 뒤지며 소리쳤다. "내 안경 어디 갔니? 방금까지 있었는데!" 온 가족이 <span class="cn-word" data-tr="divan">소파</span> 밑까지 찾았지만 없었다. 그때 <span class="cn-word" data-tr="nabira">손녀</span>가 웃음을 <span class="cn-word" data-pos="verb" data-tr="tiyolmay qolmoq">참지 못하고</span> 말했다. "할머니… 머리 위에 있어요!" 안경을 머리에 올려 두고 온 집을 찾아다녔던 것이다. 휴대폰을 손에 <span class="cn-word" data-pos="verb" data-tr="ushlab turmoq">쥔 채</span> 휴대폰을 찾는 우리도 <span class="cn-word" data-pos="adv" data-tr="xuddi shunday">마찬가지다</span>.</p>
<p>이 속담은 물건에만 쓰는 것이 아니다. 행복을 멀리서 찾<strong>으면서도</strong> 가족의 <span class="cn-word" data-tr="qadr, mehr">소중함</span>은 못 보는 사람, 좋은 친구를 밖에서 찾으면서 옆자리 친구는 못 보는 사람에게도 쓴다. 답은 <span class="cn-word" data-pos="adv" data-tr="koʻpincha">의외로</span> 가장 가까운 곳에 있는데, 우리는 그곳<strong>조차</strong> <span class="cn-word" data-pos="verb" data-tr="qaramoq">들여다보지</span> 않는다.</p>
<p>그러니 무언가를 잃어버렸다면 — 물건이든 행복이든 — 먼 곳보다 먼저 <span class="cn-word" data-tr="oyoq osti">발밑</span>을 보라. 등잔 밑이 어두운 법이니까.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Chiroq oʻz tagini yoritmas» — aynan shu maqol bizda ham bor! Izlaganingiz koʻpincha yoningizda: koʻzoynak — peshonada, baxt — oilada.
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)면서도",
                "meaning":  "Zid ish-holat: ...gan holda ham, ...sa-da (qarama-qarshilik).",
                "examples": ["행복을 멀리서 찾으면서도 가족은 못 본다.", "알면서도 모르는 척했어요."],
            },
            {
                "pattern":  "조차",
                "meaning":  "Kuchaytirilgan «ham»: hatto ... ham (kutilmagan darajada).",
                "examples": ["가장 가까운 곳조차 들여다보지 않는다.", "이름조차 기억나지 않아요."],
            },
        ],
        "questions": [
            {
                "text":        "등잔 밑은 왜 어둡습니까?",
                "choices":     ["기름이 부족해서", "등잔 자체의 그림자 때문에", "방이 너무 커서"],
                "answer":      1,
                "explanation": "Birinchi xatboshida: chiroq butun xonani yoritadi, lekin oʻzining tagida soya (그림자) hosil boʻladi — shuning uchun eng yaqin joy eng qorongʻu.",
            },
            {
                "text":        "할머니 이야기에서 안경은 어디에 있었습니까?",
                "choices":     ["소파 밑에", "할머니의 머리 위에", "부엌에"],
                "answer":      1,
                "explanation": "Nabira kulib aytdi: «머리 위에 있어요!» — koʻzoynakni boshiga qoʻyib, butun uyni qidirgan. Qoʻlida telefon ushlab telefon qidiradigan bizlar ham xuddi shu.",
            },
            {
                "text":        "이 속담은 물건 외에 무엇에 대해서도 씁니까?",
                "choices":     ["가까이에 있는 행복이나 사람을 못 보는 것", "등잔을 만드는 방법", "전기를 아끼는 방법"],
                "answer":      0,
                "explanation": "Uchinchi xatboshi: baxtni uzoqdan izlab, oila qadrini koʻrmaydigan, yaxshi doʻstni chetdan qidirib, yonidagini sezmaydigan odamlarga ham aytiladi.",
            },
        ],
    },

    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "가는 말이 고와야 오는 말이 곱다",
        "summary": "«Borar soʻz chiroyli boʻlsa, kelar soʻz ham chiroyli» — muomala oynaga oʻxshaydi: qanday gapirsangiz, shunday javob olasiz.",
        "order":   10,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">💬 ↔️ 😊</div>
<p>"가는 말이 고와야 오는 말이 곱다." 내가 보내는 말이 <span class="cn-word" data-pos="adj" data-tr="chiroyli, muloyim">고와야</span> 나에게 돌아오는 말도 곱다는 뜻이다. 말은 <span class="cn-word" data-tr="aks-sado">메아리</span>와 같아서, 산에 대고 <span class="cn-word" data-pos="verb" data-tr="baqirmoq">소리치면</span> 똑같은 소리가 돌아온다.</p>
<p>같은 상황, 두 가지 대화를 <span class="cn-word" data-pos="verb" data-tr="solishtirmoq">비교해</span> 보자. 첫 번째:<br>
"야! 너 왜 내 책 마음대로 가져갔어?"<br>
"뭐? 그럼 너는 지난주에 내 펜 가져갔잖아!"<br>
두 번째:<br>
"혹시 내 책 봤어? 네가 <span class="cn-word" data-pos="verb" data-tr="olib ketmoq">가져갔다면</span> 천천히 봐도 돼."<br>
"아, 미안해! <span class="cn-word" data-pos="adv" data-tr="shu zahoti">바로</span> 돌려줄게. 말해 줘서 고마워."<br>
<span class="cn-word" data-tr="mazmun">내용</span>은 같지만 <span class="cn-word" data-tr="natija">결과</span>는 <span class="cn-word" data-pos="adv" data-tr="butunlay">완전히</span> 다르다. 첫 대화는 싸움이 되었고, 두 번째 대화는 <span class="cn-word" data-tr="minnatdorchilik">감사</span>로 끝났다.</p>
<p>이 속담이 특히 <span class="cn-word" data-pos="adj" data-tr="dono">지혜로운</span> 점은 <span class="cn-word" data-tr="tartib">순서</span>다. "오는 말이 고와야 가는 말이 곱다"가 아니다. <span class="cn-word" data-pos="adv" data-tr="birinchi boʻlib">먼저</span> 가는 말, 즉 내 말부터 고와야 한다. 상대방이 먼저 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmoq">바뀌기를</span> 기다리지 말고, 내가 먼저 <span class="cn-word" data-pos="adj" data-tr="iliq">따뜻하게</span> 말하는 것 — 그것이 좋은 관계의 <span class="cn-word" data-tr="boshlanish nuqtasi">출발점</span>이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Salomiga yarasha alik» — qanday salom bersangiz, shunday alik olasiz. Yana biri: «Yaxshi gapga ilon inidan chiqar».
</div>''',
        "grammar": [
            {
                "pattern":  "-아/어야",
                "meaning":  "Zaruriy shart: faqat ...gandagina (aks holda boʻlmaydi).",
                "examples": ["가는 말이 고와야 오는 말이 곱다.", "표가 있어야 들어갈 수 있어요."],
            },
            {
                "pattern":  "-지 말고",
                "meaning":  "Bir ishni rad etib boshqasini taklif qilish: ...mang, buning oʻrniga ...",
                "examples": ["상대방을 기다리지 말고 내가 먼저 말하자.", "걱정하지 말고 한번 해 보세요."],
            },
        ],
        "questions": [
            {
                "text":        "두 대화의 내용은 같은데 왜 결과가 달랐습니까?",
                "choices":     ["말하는 방식이 달랐기 때문에", "책이 서로 달랐기 때문에", "두 번째 사람이 더 부자여서"],
                "answer":      0,
                "explanation": "Mazmun bir xil (kitobni kim olgani), lekin birinchi suhbat qoʻpol boshlandi — janjal chiqdi; ikkinchisi muloyim boshlandi — minnatdorchilik bilan tugadi. Farq faqat ohangda.",
            },
            {
                "text":        "이 속담의 '지혜로운 점'은 무엇입니까?",
                "choices":     ["오는 말을 먼저 기다리라는 것", "내 말부터 먼저 곱게 하라는 것", "말을 아예 하지 말라는 것"],
                "answer":      1,
                "explanation": "Tartib muhim: maqol «borar soʻz»dan boshlanadi — yaʼni suhbatdosh oʻzgarishini kutmasdan, avval OʻZIM chiroyli gapirishim kerak. Yaxshi munosabat shundan boshlanadi.",
            },
        ],
    },
]
