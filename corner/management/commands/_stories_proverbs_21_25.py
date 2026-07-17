# 속담 이야기 (Koreys maqollari) — stories 21–25. Style: STYLE_GUIDE_CORNER.md §5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_21_25.py --author=prime

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
    # ── 21 ───────────────────────────────────────────────────────────────
    {
        "title":   "누워서 떡 먹기",
        "summary": "«Yotib tteok yeyish» — juda oson ish haqida. Lekin yotib ovqat yeyish chindan osonmi? Maqolning hazil sirlari.",
        "order":   21,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🍡 😌 🛋️</div>
<p>"누워서 떡 먹기." <span class="cn-word" data-pos="verb" data-tr="yotmoq">누워서</span> <span class="cn-word" data-tr="tteok (guruch noni)">떡</span>을 먹는 것처럼 아주 쉬운 일이라는 뜻이다. 힘도 안 들고, 일어날 <span class="cn-word" data-tr="hojat, zarurat">필요</span>조차 없다. 영어의 "piece of cake"와 <span class="cn-word" data-pos="adv" data-tr="aynan">정확히</span> 같은 표현이다 — 나라마다 "쉬움"을 <span class="cn-word" data-tr="shirinlik">간식</span>으로 표현하는 것이 재미있다.</p>
<p>대화에서 이렇게 쓴다.<br>
"이 수학 문제 어려워?"<br>
"아니, 누워서 떡 먹기지. 이 <span class="cn-word" data-tr="formula">공식</span>만 알면 삼 초 만에 풀 수 있어."<br>
비슷한 표현으로 "식은 죽 먹기"도 있다. <span class="cn-word" data-pos="adj" data-tr="sovigan">식은</span> <span class="cn-word" data-tr="boʻtqa">죽</span>은 뜨겁지 않아서 후후 불 필요도 없이 그냥 먹으면 된다. 둘 다 "아주 쉽다"는 뜻으로, 시험에도 자주 나오는 <span class="cn-word" data-tr="juftlik">짝꿍</span> 표현이다.</p>
<p>그런데 이 속담에는 <span class="cn-word" data-pos="adj" data-tr="hazilkash">익살스러운</span> 반전이 있다. 실제로 누워서 떡을 먹어 보라. 떡은 <span class="cn-word" data-pos="adj" data-tr="yopishqoq">쫀득쫀득해서</span> 누워서 먹으면 목에 <span class="cn-word" data-pos="verb" data-tr="tiqilib qolmoq">걸리기</span> 십상이고, <span class="cn-word" data-tr="ushogʻi, boʻlagi">부스러기</span>가 얼굴에 다 떨어진다. 즉, 진짜로 해 보면 <span class="cn-word" data-pos="adv" data-tr="umuman">전혀</span> 쉽지 않다! 그래서 한국 사람들은 <span class="cn-word" data-pos="verb" data-tr="hazillashmoq">농담하곤</span> 한다. "누워서 떡 먹기가 세상에서 제일 어려운 일이야." 쉬워 보이는 일도 <span class="cn-word" data-pos="adv" data-tr="haqiqatda">막상</span> 해 보면 어려울 수 있다는 <span class="cn-word" data-tr="ikkinchi saboq">덤의 교훈</span>까지 주는 속담이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Xamirdan qil sugʻurgandek» — oson ishning oʻzbekcha obrazi. Inglizlar «bir boʻlak tort», koreyslar «yotib tteok», biz «xamirdan qil» — har xalqning oʻz «oson»i bor! 😄
</div>''',
        "grammar": [
            {
                "pattern":  "-기 십상이다",
                "meaning":  "Salbiy ehtimol: ...b qolishi hech gap emas, osongina ... boʻladi.",
                "examples": ["누워서 먹으면 목에 걸리기 십상이다.", "서두르면 실수하기 십상이에요."],
            },
            {
                "pattern":  "-곤 하다",
                "meaning":  "Takrorlanadigan odat: ...b turadi, gohida ... qiladi.",
                "examples": ["한국 사람들은 이렇게 농담하곤 한다.", "주말마다 산에 가곤 해요."],
            },
        ],
        "questions": [
            {
                "text":        "'누워서 떡 먹기'와 같은 뜻의 표현은 무엇입니까?",
                "choices":     ["식은 죽 먹기", "그림의 떡", "티끌 모아 태산"],
                "answer":      0,
                "explanation": "Matnda: 식은 죽 먹기 (sovigan boʻtqa yeyish) — «juda oson»ning ikkinchi klassik iborasi, imtihonlarda juft keladi. 그림의 떡 esa boshqa maʼno — «yetib boʻlmas narsa».",
            },
            {
                "text":        "이 속담의 '익살스러운 반전'은 무엇입니까?",
                "choices":     ["떡이 아주 비싸다는 것", "실제로 누워서 떡을 먹으면 오히려 어렵다는 것", "떡보다 죽이 맛있다는 것"],
                "answer":      1,
                "explanation": "Hazil shundaki: chindan yotib tteok yesangiz — tomoqqa tiqiladi, ushoq yuzga toʻkiladi. «Oson koʻringan ish ham amalda qiyin boʻlishi mumkin» degan qoʻshimcha saboq.",
            },
        ],
    },

    # ── 22 ───────────────────────────────────────────────────────────────
    {
        "title":   "그림의 떡",
        "summary": "«Suratdagi tteok» — koʻrinib turadi-yu, qoʻl yetmaydi. Orzu qilib boʻladigan, lekin ololmaydigan narsalar haqida.",
        "order":   22,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🖼️ 🍡 😢</div>
<p>"그림의 떡." 그림 속에 그려진 떡이라는 뜻이다. 아무리 <span class="cn-word" data-pos="adj" data-tr="mazali koʻringan">맛있어 보여도</span> 그림이니까 먹을 수 없다. 눈에는 보이지만 가질 수 없는 것, <span class="cn-word" data-tr="orzu">꿈</span>만 꿀 수 있는 것을 말한다. 배고픈 사람 앞의 그림 속 떡 — 이보다 <span class="cn-word" data-pos="adj" data-tr="achinarli">안타까운</span> 것이 있을까.</p>
<p>이 표현은 아주 오래된 중국 <span class="cn-word" data-tr="tarixiy yozuv">기록</span>에서 왔다. 한 <span class="cn-word" data-tr="podshoh">임금</span>이 <span class="cn-word" data-tr="amaldor">신하</span>를 뽑을 때 "<span class="cn-word" data-tr="obroʻ, nom">명성</span>만 보고 뽑는 것은 그림의 떡과 같다"라고 말했다고 한다. 이름이 아무리 유명해<strong>봤자</strong> 실력이 없으면 <span class="cn-word" data-tr="foyda">쓸모</span>가 없다는 뜻이었다. 즉, 처음부터 "보기에만 좋고 실제로는 소용없는 것"을 <span class="cn-word" data-pos="verb" data-tr="tanqid qilmoq">꼬집는</span> 말이었다.</p>
<p>오늘날의 그림의 떡은 <span class="cn-word" data-tr="hamma joyda">어디에나</span> 있다. 지수는 매일 <span class="cn-word" data-tr="doʻkon vitrinasi">쇼윈도</span> 앞을 지나며 한 <span class="cn-word" data-tr="pianino">피아노</span>를 바라본다. 가격은 지수 <span class="cn-word" data-tr="cho'ntak puli">용돈</span>의 백 배. 지금은 그림의 떡일 <strong>수밖에 없다</strong>. 하지만 지수는 <span class="cn-word" data-pos="verb" data-tr="taslim boʻlmoq">포기하지</span> 않고 그 앞에서 <span class="cn-word" data-tr="qaror">다짐</span>을 한다. "지금은 그림의 떡이지만, 언젠가는 진짜 떡으로 만들 거야."</p>
<p>그림의 떡을 대하는 두 가지 <span class="cn-word" data-tr="munosabat, yoʻl">태도</span>가 있다. 그림 앞에서 울기만 하는 것, 그리고 그 그림을 <span class="cn-word" data-tr="maqsad">목표</span>로 바꾸는 것. 선택은 언제나 우리 몫이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Koʻz koʻradi-yu, qoʻl yetmaydi» — aynan shu holat! Koreyslarda bu — och odam oldidagi suratdagi tteok.
</div>''',
        "grammar": [
            {
                "pattern":  "-아/어 봤자",
                "meaning":  "Befoyda urinish: ...ganda ham baribir (natija oʻzgarmaydi).",
                "examples": ["이름이 유명해 봤자 실력이 없으면 소용없다.", "지금 뛰어 봤자 버스는 이미 떠났어요."],
            },
            {
                "pattern":  "-(으)ㄹ 수밖에 없다",
                "meaning":  "Boshqa iloj yoʻqligi: ...ishdan boshqa chora yoʻq.",
                "examples": ["지금은 그림의 떡일 수밖에 없다.", "돈이 없어서 걸어갈 수밖에 없었어요."],
            },
        ],
        "questions": [
            {
                "text":        "'그림의 떡'의 원래 의미는 무엇이었습니까?",
                "choices":     ["그림을 잘 그리라는 뜻", "보기에만 좋고 실제로는 소용없는 것", "떡을 많이 먹으라는 뜻"],
                "answer":      1,
                "explanation": "Qadimgi yozuvda podshoh: «faqat nomiga qarab amaldor tanlash — suratdagi tteok bilan barobar» degan — koʻrinishi zoʻr-u, amalda foydasiz narsani tanqid qilgan.",
            },
            {
                "text":        "지수가 그림의 떡을 대하는 태도는 무엇입니까?",
                "choices":     ["피아노를 잊어버리기로 했다", "그림의 떡을 목표로 바꾸기로 다짐했다", "쇼윈도를 피해 다니기로 했다"],
                "answer":      1,
                "explanation": "Jisu «hozir suratdagi tteok, lekin qachondir haqiqiy tteokka aylantiraman» deb qaror qildi — surat oldida yigʻlash oʻrniga uni MAQSADga aylantirdi.",
            },
        ],
    },

    # ── 23 ───────────────────────────────────────────────────────────────
    {
        "title":   "병 주고 약 준다",
        "summary": "«Kasallik berib, keyin dori beradi» — oʻzi zarar yetkazib, keyin yordam bergan boʻlib koʻrinadigan ikkiyuzlamachilik haqida.",
        "order":   23,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🤕 💊 🤨</div>
<p>"병 주고 약 준다." 남에게 <span class="cn-word" data-tr="kasallik">병</span>을 주고 나서 <span class="cn-word" data-tr="dori">약</span>을 준다는 뜻이다. 자기가 <span class="cn-word" data-tr="zarar">해</span>를 입혀 <strong>놓고</strong>, 나중에 도와주는 <strong>척하는</strong> 사람에게 쓴다. 겉으로는 <span class="cn-word" data-pos="adj" data-tr="mehribon">친절해</span> 보이지만, 사실 병의 <span class="cn-word" data-tr="sababchi">원인</span>이 바로 그 사람이라는 것이 <span class="cn-word" data-tr="mohiyat, gap oʻzagi">핵심</span>이다.</p>
<p>교실에서의 예다. 민호의 <span class="cn-word" data-tr="oʻchirgʻich">지우개</span>를 창밖으로 던진 친구가 오 분 뒤에 새 지우개를 들고 와서 말했다. "지우개 없지? 내가 하나 <span class="cn-word" data-pos="verb" data-tr="sovgʻa qilmoq">선물해</span> 줄게. 나 <span class="cn-word" data-pos="adj" data-tr="saxiy">착하지</span>?" 민호는 <span class="cn-word" data-pos="adv" data-tr="jahli chiqib">어이가 없어서</span> 말했다. "병 주고 약 주냐? 네가 던졌잖아!"</p>
<p>어른의 세계에서는 더 <span class="cn-word" data-pos="adj" data-tr="nozik, sezilmas">교묘하게</span> 나타난다. 회의에서 동료의 <span class="cn-word" data-tr="taklif, gʻoya">제안</span>을 <span class="cn-word" data-pos="adv" data-tr="hamma oldida">공개적으로</span> 깎아내린 사람이, 회의가 끝나자 <span class="cn-word" data-pos="verb" data-tr="yelkasiga qoqmoq">어깨를 두드리며</span> "너무 <span class="cn-word" data-pos="verb" data-tr="xafa boʻlmoq">상심하지</span> 마"라고 위로한다. <span class="cn-word" data-tr="yara">상처</span>를 준 손과 약을 주는 손이 같은 손이다.</p>
<p>이 속담은 우리 자신에게도 <span class="cn-word" data-tr="oyna">거울</span>이 된다. 누군가에게 미안한 일을 했다면, 약을 주는 척하지 말고 <span class="cn-word" data-pos="adv" data-tr="avvalo">먼저</span> <span class="cn-word" data-pos="adv" data-tr="ochiq, samimiy">솔직하게</span> 사과하라. "미안해, 내가 잘못했어"가 <span class="cn-word" data-tr="haqiqiy dori">진짜 약</span>이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Avval urib, keyin siypalaydi» — zarba bergan qoʻl erkalagani bilan aybi yuvilmaydi. Koreyslarda buning tibbiy varianti: kasallik berib — dori!
</div>''',
        "grammar": [
            {
                "pattern":  "-아/어 놓고",
                "meaning":  "Qilmishga zid xatti-harakat: ...b qoʻyib (keyin buning aksini qilish).",
                "examples": ["자기가 해를 입혀 놓고 도와주는 척한다.", "약속해 놓고 안 왔어요."],
            },
            {
                "pattern":  "-는 척하다",
                "meaning":  "Yolgʻon koʻrinish: ...gandek koʻrsatmoq, oʻzini ... qilib koʻrsatmoq.",
                "examples": ["도와주는 척하지 말고 사과하세요.", "자는 척했지만 사실 다 들었어요."],
            },
        ],
        "questions": [
            {
                "text":        "민호가 '병 주고 약 주냐'라고 말한 이유는 무엇입니까?",
                "choices":     ["친구가 약을 잘못 사 와서", "지우개를 던진 사람이 새 지우개를 선물하며 착한 척해서", "민호가 아파서"],
                "answer":      1,
                "explanation": "Oʻchirgʻichni derazadan otgan doʻst besh daqiqadan soʻng yangisini olib kelib «men saxiyman-a?» dedi — zararni ham, «yordam»ni ham bitta odam berdi. Aynan maqol holati.",
            },
            {
                "text":        "글쓴이에 따르면 '진짜 약'은 무엇입니까?",
                "choices":     ["새 지우개를 사 주는 것", "솔직하게 사과하는 것", "어깨를 두드리는 것"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: aybdor boʻlsangiz, yordam bergan boʻlib koʻrinmang — avval ochiq uzr soʻrang. «Kechir, men xato qildim» — haqiqiy dori shu.",
            },
        ],
    },

    # ── 24 ───────────────────────────────────────────────────────────────
    {
        "title":   "원수는 외나무다리에서 만난다",
        "summary": "«Dushman bilan yakkachoʻp koʻprikda uchrashasan» — yomonlik qilgan odamingiz bilan eng noqulay joyda albatta toʻqnashasiz. Dunyo tor!",
        "order":   24,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🌉 😠 😠</div>
<p>"원수는 외나무다리에서 만난다." <span class="cn-word" data-tr="dushman, yov">원수</span>는 나에게 큰 <span class="cn-word" data-tr="yomonlik, alam">원한</span>이 있는 사람이다. <span class="cn-word" data-tr="yakkachoʻp koʻprik">외나무다리</span>는 나무 <span class="cn-word" data-tr="bir dona">한 그루</span>로 만든 좁은 다리라서 두 사람이 만나면 <span class="cn-word" data-pos="verb" data-tr="chetlab oʻtmoq">비켜 갈</span> 수가 없다. 즉, 가장 만나고 싶지 않은 사람을 <span class="cn-word" data-pos="adv" data-tr="ayni, xuddi">하필</span> 가장 피할 수 없는 곳에서 만난다는 뜻이다.</p>
<p>세상은 생각보다 <span class="cn-word" data-pos="adj" data-tr="tor">좁다</span>. 중학교 때 친구를 <span class="cn-word" data-pos="verb" data-tr="xoʻrlamoq">괴롭히던</span> 사람이 있었다. 십 년 뒤, 그는 <span class="cn-word" data-tr="ish suhbati">면접</span>을 보러 갔다. 회사 문이 열리고 <span class="cn-word" data-tr="suhbat oluvchi">면접관</span>이 들어왔다 — 바로 그가 괴롭히던 그 친구였다. 그는 그날 밤 <span class="cn-word" data-tr="kundalik">일기</span>에 이렇게 썼다고 한다. "원수는 외나무다리에서 만난다더니, 내 인생의 외나무다리는 면접실이<strong>을 줄 몰랐다</strong>."</p>
<p>이 속담의 진짜 가르침은 "원수를 조심하라"가 아니다. <span class="cn-word" data-pos="adv" data-tr="boshidanoq">애초에</span> 원수를 <span class="cn-word" data-pos="verb" data-tr="yaratmoq">만들지</span> 말라는 것이다. 오늘 내가 함부로 대한 사람이 내일 어느 다리 위에서 나를 기다리고 있을지 아무도 모른다. <span class="cn-word" data-pos="adv" data-tr="teskarisiga">반대로</span>, 오늘 내가 도와준 사람을 내일 외나무다리에서 만난다면? 그 다리는 세상에서 가장 <span class="cn-word" data-pos="adj" data-tr="xushnud, yoqimli">반가운</span> 다리가 될 것이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Togʻ togʻ bilan uchrashmas, odam odam bilan uchrashar» — odamlar albatta yana toʻqnashadi. Shuning uchun hech kim bilan «koʻprikda koʻrishib boʻlmaydigan» boʻlib ajrashmang!
</div>''',
        "grammar": [
            {
                "pattern":  "하필",
                "meaning":  "Nega aynan (afsus ohangi): shuncha imkoniyat ichida aynan shu.",
                "examples": ["하필 가장 피할 수 없는 곳에서 만난다.", "하필 시험 날에 아팠어요."],
            },
            {
                "pattern":  "-(으)ㄹ 줄 몰랐다",
                "meaning":  "Kutilmaganlik: ... boʻlishini bilmagan edim, oʻylamagan edim.",
                "examples": ["외나무다리가 면접실일 줄 몰랐다.", "이렇게 어려울 줄 몰랐어요."],
            },
        ],
        "questions": [
            {
                "text":        "왜 하필 '외나무다리'입니까?",
                "choices":     ["다리가 아름다워서", "좁아서 서로 비켜 갈 수 없어서", "나무가 튼튼해서"],
                "answer":      1,
                "explanation": "Yakkachoʻp koʻprik shunchalik torki, ikki kishi uchrashsa chetlab oʻtib boʻlmaydi — koʻrishmaslikning iloji yoʻq. Eng qochib boʻlmas joy timsoli.",
            },
            {
                "text":        "면접 이야기가 보여 주는 것은 무엇입니까?",
                "choices":     ["면접은 언제나 어렵다", "과거에 괴롭힌 사람을 인생의 중요한 순간에 다시 만날 수 있다", "일기를 쓰면 좋다"],
                "answer":      1,
                "explanation": "Maktabda xoʻrlagan odami oʻn yildan keyin ish suhbatida SUHBAT OLUVCHI boʻlib chiqdi — hayotning eng muhim daqiqasida oʻtmish qarshisidan chiqdi. Dunyo tor!",
            },
            {
                "text":        "이 속담의 진짜 가르침은 무엇입니까?",
                "choices":     ["다리를 건너지 말라", "애초에 원수를 만들지 말라", "원수를 만나면 도망가라"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: asosiy saboq «dushmandan ehtiyot boʻl» emas — «dushman orttirma». Bugun yaxshilik qilgan odamingiz bilan koʻprikda uchrashish esa — quvonch.",
            },
        ],
    },

    # ── 25 ───────────────────────────────────────────────────────────────
    {
        "title":   "바늘 도둑이 소도둑 된다",
        "summary": "«Igna oʻgʻrisi sigir oʻgʻrisiga aylanadi» — kichkina yomon ish jazosiz qolsa, katta yomonlikka yoʻl ochadi.",
        "order":   25,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🪡 ➡️ 🐄</div>
<p>"바늘 도둑이 소도둑 된다." <span class="cn-word" data-tr="igna">바늘</span> 하나를 <span class="cn-word" data-pos="verb" data-tr="oʻgʻirlamoq">훔친</span> <span class="cn-word" data-tr="oʻgʻri">도둑</span>이 나중에는 <span class="cn-word" data-tr="sigir, hoʻkiz">소</span>를 훔치는 큰 도둑이 된다는 뜻이다. 바늘은 옛날 물건 중 가장 작고 <span class="cn-word" data-pos="adj" data-tr="arzon">값싼</span> 것, 소는 <span class="cn-word" data-tr="dehqon xoʻjaligi">농가</span>의 <span class="cn-word" data-tr="butun boyligi">전 재산</span>이었다. 가장 작은 <span class="cn-word" data-tr="jinoyat">죄</span>가 가장 큰 죄로 <span class="cn-word" data-pos="verb" data-tr="oʻsib bormoq">자라나는</span> 과정을 그린 속담이다.</p>
<p>옛이야기가 있다. 한 아이가 시장에서 바늘 하나를 훔쳐 어머니에게 가져왔다. 어머니는 <span class="cn-word" data-pos="verb" data-tr="urishmoq, tanbeh bermoq">혼내는</span> 대신 웃으며 말했다. "우리 아들, <span class="cn-word" data-pos="adj" data-tr="epchil">재주도</span> 좋네." 아이는 <span class="cn-word" data-pos="adv" data-tr="asta-sekin">점점</span> 더 큰 것을 훔치기 시작했다. 닭을 훔치고, <span class="cn-word" data-tr="choʻchqa">돼지</span>를 훔치<strong>다 보니</strong> 어른이 되어서는 <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">마침내</span> 소도둑이 되어 <span class="cn-word" data-pos="verb" data-tr="qoʻlga tushmoq">붙잡히고</span> 말았다. <span class="cn-word" data-tr="qatl maydoni">형장</span>으로 가던 날, 아들은 어머니에게 말했다. "제가 바늘을 훔친 날, 어머니가 저를 혼냈<strong>더라면</strong> 오늘 이 자리에 없었을 겁니다."</p>
<p>이 속담이 무서운 이유는 <span class="cn-word" data-tr="chegara">경계선</span>이 <span class="cn-word" data-pos="adv" data-tr="sezilmas darajada">눈치채지 못하게</span> 옮겨지기 때문이다. 오늘 "이 정도쯤이야"라고 넘어간 작은 잘못이 내일의 <span class="cn-word" data-tr="meʼyor">기준</span>이 된다. 그래서 <span class="cn-word" data-pos="adj" data-tr="dono">현명한</span> 사람은 바늘 앞에서 멈춘다. 소 앞에서는 이미 늦다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Bugun tuxum oʻgʻirlagan, ertaga tuya oʻgʻirlaydi» — xuddi shu zanjir: tuxumdan tuyagacha, ignadan sigirgacha. Kichik yomonlikning yoʻlini boshidayoq kesing!
</div>''',
        "grammar": [
            {
                "pattern":  "-다 보니",
                "meaning":  "Davomli harakat natijasida: ...ayotib (bilib-bilmay) ...ga kelib qoldim.",
                "examples": ["돼지를 훔치다 보니 소도둑이 되었다.", "매일 듣다 보니 한국어가 익숙해졌어요."],
            },
            {
                "pattern":  "-았/었더라면",
                "meaning":  "Oʻtmishdagi afsus-shart: agar oʻshanda ...ganda edi (aslida boʻlmagan).",
                "examples": ["어머니가 혼냈더라면 소도둑이 되지 않았을 것이다.", "그때 시작했더라면 지금쯤 잘했을 거예요."],
            },
        ],
        "questions": [
            {
                "text":        "이야기 속 아이가 소도둑이 된 데에 어머니의 책임은 무엇입니까?",
                "choices":     ["아이에게 소를 사 줘서", "바늘을 훔쳤을 때 혼내지 않고 칭찬해서", "아이를 시장에 보내서"],
                "answer":      1,
                "explanation": "Ona igna oʻgʻirlaganda tanbeh berish oʻrniga «epchilsan» deb kuldi — birinchi kichik jinoyat maqtov oldi va zanjir boshlandi. Oʻgʻilning soʻnggi soʻzi ham shu: «oʻshanda urishganingizda edi...».",
            },
            {
                "text":        "이 속담이 '무서운' 이유는 무엇입니까?",
                "choices":     ["소가 크고 위험해서", "잘못의 경계선이 눈치채지 못하게 조금씩 옮겨져서", "바늘이 날카로워서"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: «shunchalik arzimas-ku» deb oʻtkazilgan bugungi kichik xato — ertaga MEʼYOR boʻlib qoladi; chegara sezilmasdan siljiydi. Shuning uchun igna oldida toʻxtash kerak.",
            },
        ],
    },
]
