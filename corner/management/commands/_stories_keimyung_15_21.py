# Keimyung Korean Readings — stories 15–21 (real textbook passages from keimyung_21_story.txt).
# Import: python manage.py import_corner corner/management/commands/_stories_keimyung_15_21.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Keimyung Korean Readings",
    "description": "Oʻrta daraja (TOPIK II) oʻqish matnlari — lugʻat izohlari va kartochkalar bilan.",
    "order":       1,
}

STORIES = [
    {
        "title":   "살아 움직이는 언어",
        "summary": "Soʻzlar tugʻiladi, oʻzgaradi va yoʻqoladi — tilning tarixiyligi haqida.",
        "order":   15,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 법도 하다",
                "meaning":  "...sa ajab emas, ...ishi ham tabiiy (ehtimol).",
                "examples": ["나이가 적어 못 배웠다고 잘못 해석할 법도 하다.", "그렇게 오해할 법도 해요."],
            },
            {
                "pattern":  "-(으)ㄹ 리(가) 만무하다",
                "meaning":  "...ishi aslo mumkin emas (kuchli inkor).",
                "examples": ["한자를 모르니 글을 쓸 리 만무했다.", "그가 거짓말을 할 리 만무해요."],
            },
            {
                "pattern":  "-지 않고서는",
                "meaning":  "...masdan turib (natijaga erishib boʻlmaydi).",
                "examples": ["새 말을 만들지 않고서는 표현할 수 없다.", "노력하지 않고서는 성공할 수 없어요."],
            },
            {
                "pattern":  "-(으)련마는(련만)",
                "meaning":  "...sa yaxshi boʻlardi-yu, ammo (adabiy afsus).",
                "examples": ["마음대로 쓸 수 있으면 좋으련마는 그렇지 못했다.", "함께 가면 좋으련만 시간이 없네요."],
            },
        ],
        "body": '''<p>우리가 사용하는 언어는 시간이 <span class="cn-word" data-pos="verb" data-tr="oʻtsa ham, kechsa ham">흘러도</span> <span class="cn-word" data-pos="adj" data-tr="hech qanday">아무런</span> 변화가 없는 것일까? 한글을 만든 세종대왕은 다음과 같은 말씀을 하셨다.</p>
<p>"어린 <span class="cn-word" data-tr="oddiy xalq, fuqaro">백성</span>이 말하고자 하는 바가 있어도 글을 몰라 표현할 수 없으니 매우 <span class="cn-word" data-pos="adj" data-tr="achinarli, afsus">안타깝구나</span>." 이 문장에서 '어리다'는 나이가 적다는 뜻이 아니다. 현대의 말로 '<span class="cn-word" data-pos="adj" data-tr="nodon, bilimsiz">어리석다</span>'와 비슷하다. 이것을 모르는 사람이라면 백성이 아직 나이가 적어서 글을 배우지 못했다고 <span class="cn-word" data-pos="adv" data-tr="notoʻgʻri, xato">잘못</span> <span class="cn-word" data-pos="verb" data-tr="talqin qilish">해석할</span> 법도 하다. 당시 보통 사람들은 우리말과 다른 중국의 한자를 <span class="cn-word" data-pos="adv" data-tr="oson">쉽게</span> 배우지 못했기 때문에 글을 쓸 리 <span class="cn-word" data-pos="verb" data-tr="aslo mumkin emas edi">만무했다</span>. 말하고 싶은 것을 글로도 마음대로 쓸 수 있으면 좋으련마는 그렇게 하지 못하는 백성들을 <span class="cn-word" data-pos="adv" data-tr="achinib, rahmi kelib">불쌍하게</span> <span class="cn-word" data-pos="verb" data-tr="hisoblagan, deb bilgan">여긴</span> 세종대왕의 마음을 표현한 것이다.</p>
<p>'어리다'의 뜻이 '어리석다'에서 '나이가 적다'로 <span class="cn-word" data-pos="verb" data-tr="oʻzgargan">변한</span> 것처럼 시간이 흐르면서 변화하는 언어의 특성을 '<span class="cn-word" data-tr="tarixiylik">역사성</span>'이라고 한다. 이 역사성은 모든 언어가 가지고 있는 <span class="cn-word" data-pos="adj" data-tr="umumiy, mushtarak">공통된</span> 특성이며 짧은 시간 안에 나타나는 것이 아니다. 아버지와 딸의 대화를 들어보면 크게 다르지 않지만, 100년 전 조상들이 쓴 글을 보면 그 변화를 <span class="cn-word" data-pos="adv" data-tr="aniq, ravshan">확실하게</span> 느낄 수 있다. 언어가 지금 이 순간에도 생명을 <span class="cn-word" data-pos="verb" data-tr="ega boʻlgan, saqlagan">지닌</span> <span class="cn-word" data-tr="tirik organizm">유기체</span>처럼 새로 만들어지고 변화하며 <span class="cn-word" data-pos="verb" data-tr="yoʻqolib">사라지고</span> 있기 때문이다.</p>
<p><strong>말이 새로 만들어지는 이유는 무엇일까</strong></p>
<p>과거에 없던 물건이나 개념이 <span class="cn-word" data-pos="verb" data-tr="paydo boʻlganda">생겼을</span> 때 새로운 말을 만들지 않고서는 표현해 낼 수가 없으므로 생기는 것이다. 이뿐만 아니라 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> <span class="cn-word" data-pos="verb" data-tr="mavjud boʻlgan">존재하는</span> 대상일지라도 <span class="cn-word" data-pos="adj" data-tr="yangi, original">신선한</span> 표현을 원하는 사람들의 욕구에 의해서 새말이 생길 수 있다. 예를 들어, '스마트 폰', '로봇 청소기', '전기 자동차' 등은 과거에는 없었지만 과학의 발달로 인해 새로 만들어진 물건이어서 그것을 <span class="cn-word" data-pos="verb" data-tr="atash, nomlash">지칭할</span> 단어가 필요하게 된 경우이며, '스펙', '사이버 대학' 등은 물건이 아니라 개념을 표현하기 위한 <span class="cn-word" data-tr="yangi yasalgan soʻz">신조어</span>라고 할 수 있다.</p>
<p><strong>널리 쓰이다가 사라진 단어들도 있다</strong></p>
<p>외국에서 만든 물건이라는 뜻으로 1990년대까지 많이 <span class="cn-word" data-pos="verb" data-tr="ishlatilgan">사용되던</span> '외제'라는 단어는 이제 <span class="cn-word" data-pos="verb" data-tr="izsiz yoʻqolib">자취를 감추고</span>, 대신 '수입산'이라는 단어를 사용한다. 은하수를 뜻하는 <span class="cn-word" data-tr="sof koreys soʻzi">고유어</span> '미리내', 왕의 명령을 받고 지방에 <span class="cn-word" data-pos="verb" data-tr="yuborilgan">파견되어</span> 관리들의 비리를 <span class="cn-word" data-pos="verb" data-tr="nazorat qilgan, kuzatgan">감시하던</span> <span class="cn-word" data-tr="amal, mansab (qadimgi)">벼슬</span>인 '어사' 등도 모두 사라진 단어이다. '즈믄:천', '온:백', '뫼:산'은 같은 개념을 표현하는 두 개의 단어가 서로 <span class="cn-word" data-pos="verb" data-tr="raqobatlashib">경쟁하다가</span> 하나가 사라져서 지금은 '천', '백', '산'만이 <span class="cn-word" data-pos="verb" data-tr="qolmoq">남게</span> 되었다.</p>
<p><strong>형태는 그대로 있으나 의미가 변한 단어들도 있다</strong></p>
<p>'얼굴'은 모습 전체를 <span class="cn-word" data-pos="verb" data-tr="ifodalaydigan, bildiruvchi">나타내는</span> 말에서 '안면'을 뜻하는 것으로 의미가 <span class="cn-word" data-pos="verb" data-tr="torayib, qisqarib">축소되었으며</span>, 벼슬 이름이었던 '영감'은 '남자 노인'으로, 생각하다의 뜻으로 사용되던 '사랑하다'는 '좋아하다'로 그 의미가 <span class="cn-word" data-pos="verb" data-tr="oʻzgardi">바뀌었다</span>. 이와 <span class="cn-word" data-pos="adv" data-tr="aksincha">반대로</span> '나모'(나무), '아해'(아이), '녀름'(여름) 등은 의미는 같으나 형태가 바뀐 단어들이다.</p>''',
        "questions": [
            {
                "text": "이 글에서 설명하는 언어의 '역사성'이란 무엇입니까?",
                "choices": [
                    "언어가 시간이 흐르면서 새로 생기고 변하고 사라지는 특성",
                    "언어가 나라마다 다른 특성",
                    "언어가 절대 변하지 않는 특성",
                ],
                "answer": 0,
                "explanation": "Matnda \"시간이 흐르면서 변화하는 언어의 특성을 역사성이라고 한다\" deyilgan — yaʼni til vaqt oʻtishi bilan tugʻiladi, oʻzgaradi va yoʻqoladi.",
            },
            {
                "text": "세종대왕의 말에서 '어린 백성'의 '어리다'는 어떤 뜻입니까?",
                "choices": [
                    "나이가 적다",
                    "어리석다 (지혜가 부족하다)",
                    "키가 작다",
                ],
                "answer": 1,
                "explanation": "Matnda \"'어리다'는 나이가 적다는 뜻이 아니라 현대의 '어리석다'와 비슷하다\" deb aytilgan — oʻsha davrda bu soʻz nodonlik maʼnosini bergan.",
            },
            {
                "text": "다음 중 '형태는 그대로이나 의미가 변한 단어'의 예로 알맞은 것은?",
                "choices": [
                    "'스마트 폰' 같은 새로 만들어진 말",
                    "'얼굴'이 '모습 전체'에서 '안면'으로 뜻이 바뀐 것",
                    "'나모'가 '나무'로 형태가 바뀐 것",
                ],
                "answer": 1,
                "explanation": "Matnda 얼굴 soʻzi shakli oʻzgarmay, maʼnosi \"butun koʻrinish\"dan \"yuz\"ga torayganini misol qilib keltiradi. 스마트 폰 — yangi soʻz, 나모→나무 esa shakl oʻzgarishi.",
            },
        ],
    },
    {
        "title":   "점심시간을 디자인하는 런치투어족",
        "summary": "Tushlik vaqtini oʻziga sarflaydigan 'lanch-tur' avlodi haqida.",
        "order":   16,
        "grammar": [
            {
                "pattern":  "-는 것은 물론이고",
                "meaning":  "...i tabiiy, shu bilan birga (bundan tashqari).",
                "examples": ["건강을 지키는 것은 물론이고 동호회 활동도 한다.", "노래는 물론이고 춤도 잘 춰요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 채(로)",
                "meaning":  "...gan holicha, ...gan koʻyi (oʻzgarmagan holat).",
                "examples": ["잠이 덜 깬 채 새벽 수업을 듣는다.", "신발을 신은 채 들어왔어요."],
            },
            {
                "pattern":  "-기에 좋다",
                "meaning":  "...ish uchun qulay/mos (baho).",
                "examples": ["점심시간은 새로운 시간을 설계하기에 좋다.", "이 방은 공부하기에 좋아요."],
            },
            {
                "pattern":  "이른바",
                "meaning":  "Deb ataladigan, yaʼni (izohlovchi kirish soʻz).",
                "examples": ["이런 사람들을 이른바 '런치투어족'이라고 한다.", "그것이 이른바 성공의 비결이에요."],
            },
        ],
        "body": '''<p>직장인들의 여가 문화가 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmoqda">변하고</span> 있다. 여가활동 시간대가 <span class="cn-word" data-pos="verb" data-tr="oʻzgarishi bilan">바뀌면서</span> 여가 문화에도 변화가 생긴 것이다. 하루 종일 회사에 <span class="cn-word" data-tr="band boʻlgan, qoʻli bogʻlangan">발이 묶여</span> 있는 직장인들에게 여가 시간은 <span class="cn-word" data-pos="adv" data-tr="asosan">주로</span> 출근 전과 퇴근 후였지만 <span class="cn-word" data-pos="adv" data-tr="soʻnggi paytda">최근</span> 점심시간을 이용해 여가를 즐기는 직장인들이 늘고 있다. 이들처럼 점심시간에 밥을 먹지 않고, 혹은 <span class="cn-word" data-pos="adv" data-tr="oddiygina, qisqa">간단히</span> 해결하고 개인적인 <span class="cn-word" data-tr="yumush">볼일</span>을 보는 이들을 <span class="cn-word" data-pos="adv" data-tr="deb ataladigan, yaʼni">이른바</span> '런치투어(lunch tour)족'이라고 한다.</p>
<p>자신에게 시간을 <span class="cn-word" data-pos="verb" data-tr="sarflaydigan, ajratadigan">투자하는</span> '런치투어족'에게 이 <span class="cn-word" data-tr="ortib qolgan vaqt">자투리 시간</span>은 새로운 시간을 설계하기에 더할 나위없이 좋은 시간이다. <span class="cn-word" data-tr="davlat idoralari">관공서</span>나 은행 등 평일 낮에만 볼 수 있는 간단한 업무를 보기도 하고 쇼핑을 하기도 한다. 운동과 요가, 마사지 등으로 건강을 <span class="cn-word" data-pos="verb" data-tr="asraydigan, saqlaydigan">지키는</span> 것은 물론이고 <span class="cn-word" data-tr="qiziqish klubi, toʻgarak">동호회</span> 활동이나 학원 <span class="cn-word" data-tr="kursda oʻqish">수강</span> 등으로 <span class="cn-word" data-pos="adj" data-tr="mazmunli, samarali">알찬</span> 시간을 보낸다. 공부하는 직장인인 '샐러던트(saladent)'도 <span class="cn-word" data-pos="adv" data-tr="koʻpincha, odatda">대개</span> 런치투어족이다. 잠이 덜 깬 채 듣는 새벽반보다는 점심반 수업을 듣는 직장인이 많고 온라인 강의도 이 시간대에 많이 이용된다. 또한 가사에서 손을 놓을 수 없는 <span class="cn-word" data-tr="er-xotin ikkalasi ishlaydigan">맞벌이</span> 여성들에게는 <span class="cn-word" data-pos="adj" data-tr="qadrli, qimmatli">귀중한</span> 가사 시간이 되기도 한다. 퇴근하여 저녁식사를 준비하기까지의 시간을 <span class="cn-word" data-pos="adv" data-tr="imkon qadar">최대한</span> <span class="cn-word" data-pos="verb" data-tr="qisqartirish">단축하기</span> 위해 점심시간에 <span class="cn-word" data-pos="adv" data-tr="oldindan">미리</span> 장을 봐 둔다.</p>
<p>이러한 <span class="cn-word" data-tr="tendensiya, oqim">추세</span>에 따라 회사 측에서도 직원들이 점심 여가를 즐길 수 있도록 다양한 프로그램을 <span class="cn-word" data-pos="verb" data-tr="yuritmoqda, tashkil qilmoqda">운영하고</span> 있다. 한 회사에서는 점심시간을 <span class="cn-word" data-pos="verb" data-tr="foydalanib">활용해서</span> 문화체험을 할 수 있는 런치문화 강좌를 운영해 직원들에게 큰 인기를 얻고 있다. 한 식품 업체에서는 직원들이 점심시간을 이용해 <span class="cn-word" data-pos="adv" data-tr="bevosita, oʻzi">직접</span> 요리한 음식을 먹으면서 아이디어 연구를 하기도 한다.</p>
<p>런치투어족들을 <span class="cn-word" data-pos="verb" data-tr="moʻljallagan, nishonga olgan">겨냥한</span> 관련 업체들의 마케팅 또한 <span class="cn-word" data-pos="adv" data-tr="faol, jonli">활발하게</span> 이루어지고 있다. 상당수의 런치투어족들은 도시락을 싸오거나 김밥, 삼각 김밥, 샌드위치 등의 테이크 아웃 음식을 <span class="cn-word" data-pos="verb" data-tr="sevib ishlatadigan">애용하는데</span> 패스트푸드점들이 <span class="cn-word" data-pos="adv" data-tr="raqobatlashib">경쟁적으로</span> 내놓고 있는 런치 메뉴는 아주 인기가 많다. 일부 스포츠센터, 피부 관리실, 은행 등에서는 런치투어족을 위해 간단한 간식거리를 준비해 두기도 한다. 한 기업에서는 직장인들이 점심 식사 후에 <span class="cn-word" data-pos="adv" data-tr="yengil">가볍게</span> 공연 문화를 즐길 수 있게 하자는 <span class="cn-word" data-tr="maqsad, gʻoya">취지</span>에서 매주 목요일에 합창, 비보잉, 세계 민속 공연 등을 <span class="cn-word" data-pos="verb" data-tr="namoyish qilib, taqdim etib">선보여</span> 문화 마케팅으로 활용하고 있다.</p>
<p>이렇듯 아침과 저녁은 물론이거니와 과거 <span class="cn-word" data-pos="verb" data-tr="behuda ketadi deb">버려진다고</span> 생각했던 점심 때의 짧은 시간까지도 <span class="cn-word" data-pos="verb" data-tr="foydalanadigan">활용하는</span> 것이 최근 직장 여가 문화의 <span class="cn-word" data-tr="moyillik, yoʻnalish">경향</span>이다. 여러분의 점심시간은 어떤가. 런치투어족들처럼 우리도 자신만의 <span class="cn-word" data-pos="adj" data-tr="ajoyib, zoʻr">멋진</span> 점심시간을 디자인해 볼까.</p>''',
        "questions": [
            {
                "text": "'런치투어족'이란 어떤 사람들입니까?",
                "choices": [
                    "점심시간에 밥만 오래 먹는 사람들",
                    "점심시간을 이용해 개인적인 볼일이나 여가를 즐기는 직장인들",
                    "점심을 거르고 밤에만 일하는 사람들",
                ],
                "answer": 1,
                "explanation": "Matnda lanch-tur avlodi tushlik vaqtida ovqatni oʻtkazib yuborib yoki qisqa yeb, shaxsiy yumushlari va hordigʻi bilan shugʻullanadigan xodimlar deb taʼriflangan.",
            },
            {
                "text": "맞벌이 여성들에게 점심시간이 귀중한 이유로 알맞은 것은?",
                "choices": [
                    "저녁 준비 시간을 줄이려고 미리 장을 볼 수 있어서",
                    "점심을 두 번 먹을 수 있어서",
                    "회사에서 돈을 더 주어서",
                ],
                "answer": 0,
                "explanation": "Matnda er-xotin ikkalasi ishlaydigan ayollar kechki ovqat tayyorlash vaqtini qisqartirish uchun tushlik paytida oldindan xarid qilib qoʻyishi aytilgan.",
            },
            {
                "text": "회사들이 점심 여가 프로그램을 운영하는 이유로 볼 수 있는 것은?",
                "choices": [
                    "직원들이 점심 여가를 잘 즐길 수 있도록 돕기 위해",
                    "직원들의 점심시간을 없애기 위해",
                    "직원들에게 벌을 주기 위해",
                ],
                "answer": 0,
                "explanation": "Matnda kompaniyalar xodimlar tushlik hordigʻidan bahramand boʻlishi uchun turli dasturlar (madaniyat kurslari, konsertlar) tashkil qilishi aytilgan.",
            },
        ],
    },
    {
        "title":   "생활 속에 숨은 과학의 원리",
        "summary": "Kimchi xumlari, himoya arqoni va ondol — ajdodlar turmushidagi yashirin ilm.",
        "order":   17,
        "grammar": [
            {
                "pattern":  "-기가 무섭게",
                "meaning":  "...boʻlishi bilanoq, zudlik bilan (juda tez).",
                "examples": ["아기를 낳기가 무섭게 대문에 금줄을 쳤다.", "수업이 끝나기가 무섭게 뛰어나갔어요."],
            },
            {
                "pattern":  "-기 일쑤이다",
                "meaning":  "Tez-tez ...boʻlib turadi (koʻpincha salbiy).",
                "examples": ["김치는 시간이 지나면 맛이 변하기 일쑤이다.", "급하게 먹으면 체하기 일쑤예요."],
            },
            {
                "pattern":  "-게끔",
                "meaning":  "...adigan qilib, ...maslik uchun (maqsad/natija).",
                "examples": ["김치가 얼지 않게끔 땅에 묻었다.", "잘 보이게끔 불을 켰어요."],
            },
            {
                "pattern":  "-(으)려면",
                "meaning":  "...moqchi boʻlsang, ...ish uchun (shart).",
                "examples": ["신선한 맛을 유지하려면 낮은 온도에 보관해야 한다.", "성공하려면 노력해야 해요."],
            },
        ],
        "body": '''<p>우리 생활 속에는 우리도 잘 모르는 과학의 <span class="cn-word" data-tr="qonuniyat, tamoyil">원리</span>가 <span class="cn-word" data-pos="verb" data-tr="yashiringan">숨어</span> 있다. 이러한 생활 속 과학은 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> 오래 전 삶의 방식에서부터 <span class="cn-word" data-pos="verb" data-tr="kelib chiqqan">유래된</span> 경우가 많다. 온돌방에 앉아 가마솥으로 <span class="cn-word" data-pos="verb" data-tr="pishirilgan (guruch)">지은</span> 밥을 먹고 김칫독을 땅에 <span class="cn-word" data-pos="verb" data-tr="koʻmar edilar">묻었으며</span>, 아이를 낳으면 금줄을 쳤던 한국의 <span class="cn-word" data-tr="urf-odat">풍습</span>, 그 속에 <span class="cn-word" data-pos="verb" data-tr="mujassam, singdirilgan">담긴</span> 삶의 <span class="cn-word" data-tr="donolik, hikmat">지혜</span>를 알아보자.</p>
<p>겨울이 시작될 무렵 <span class="cn-word" data-tr="ajdodlar, ota-bobolar">선조들</span>은 김장 김치를 옹기에 담아 땅에 묻었다. 김치는 시간이 지나면 <span class="cn-word" data-tr="bijgʻish, fermentatsiya">발효</span> 과정을 <span class="cn-word" data-pos="verb" data-tr="oʻtib, kechib">거치면서</span> 성분의 변화가 일어나 맛이 변하기 일쑤이다. 그러므로 가능한 한 오래 저장하면서 <span class="cn-word" data-pos="adj" data-tr="yangi, tetik">신선한</span> 맛을 <span class="cn-word" data-pos="verb" data-tr="saqlash uchun">유지하려면</span> 영상 5도에서 10도 사이에서 <span class="cn-word" data-tr="saqlash">보관하는</span> 것이 중요한데 선조들은 그 방법을 알고 있었다. 여름에는 김칫독을 우물이나 냇물에 담가 두어 <span class="cn-word" data-pos="adv" data-tr="salqin">시원하게</span> 하였고 겨울에는 땅에 묻어 김치가 <span class="cn-word" data-pos="verb" data-tr="muzlamoq">얼지</span> 않게끔 한 것이다. 이러한 저장 방식을 <span class="cn-word" data-pos="verb" data-tr="qoʻllab, tatbiq etib">적용하여</span> 일 년 내내 김치 맛을 <span class="cn-word" data-pos="adv" data-tr="bir tekis, doimiy">일정하게</span> 유지시킨 것이 바로 김치 냉장고이다.</p>
<p>전통 사회에서는 아기를 낳기가 무섭게 대문에 <span class="cn-word" data-tr="himoya arqoni (anʼanaviy)">금줄</span>을 쳤다. 금줄은 아기가 태어난 것을 <span class="cn-word" data-pos="verb" data-tr="bildirib, xabar berib">알리고</span> 외부사람이나 나쁜 귀신이 들어오지 못하도록 하기 위한 <span class="cn-word" data-tr="taqiq">금기</span>였다. 아들이 태어나면 새끼줄에 고추, <span class="cn-word" data-tr="pista koʻmir">숯</span> 등을 달고 딸이 태어나면 숯, 솔가지, 흰 종이 등을 달아 두어 아기의 성별을 <span class="cn-word" data-pos="verb" data-tr="bildirar edi">알렸다</span>. 숯은 나쁜 기운을 <span class="cn-word" data-pos="verb" data-tr="soʻrib olib, yutib">흡수하고</span> 흰 종이는 부자가 되기를 바라는 마음이 <span class="cn-word" data-pos="verb" data-tr="jamlangan, mujassam">담겨</span> 있으며, 빨간 고추는 귀신을 <span class="cn-word" data-pos="verb" data-tr="quvadi deb, haydaydi deb">쫓는다고</span> 생각하였다. 솔가지를 끼우는 것은 아기가 커서 바느질을 잘하라는 의미이다. 금줄을 치는 기간이 삼칠일, 즉 21일인 것은 아기와 산모의 <span class="cn-word" data-tr="immunitet">면역력</span>이 어느 정도 <span class="cn-word" data-pos="verb" data-tr="tiklanadigan">회복될</span> 수 있는 기간이라고 생각했기 때문이다. 지금도 아기를 낳은 산모들은 산후조리원에서 삼칠일 동안 <span class="cn-word" data-tr="tugʻruqdan keyingi parvarish">산후 조리</span>를 한다. 그리고 숯은 공기 <span class="cn-word" data-tr="tozalash">정화</span>, 해독 작용, 탈취 효과 등의 효능이 <span class="cn-word" data-pos="verb" data-tr="isbotlanib">입증되어</span> 가습기나 탈취제, 전자파 차단제 등 다양한 용도로 사용된다.</p>
<p>온돌도 과학의 원리를 이용한 <span class="cn-word" data-pos="adj" data-tr="eng mashhur, namunaviy">대표적인</span> 것이다. '<span class="cn-word" data-pos="adj" data-tr="iliq, issiqqina">따끈한</span> 아랫목에 지져야 몸이 <span class="cn-word" data-pos="adj" data-tr="yengil tortadi, tetiklashadi">개운하다</span>'는 말이 있을 정도로 한국인들은 온돌을 사랑한다. 온돌은 아궁이에 불을 때면 그 열기가 바닥에 깔린 구들을 지나면서 방 전체가 <span class="cn-word" data-pos="verb" data-tr="isib boradigan">따뜻해지는</span> 한국 고유의 <span class="cn-word" data-tr="isitish usuli">난방법</span>이다. 온돌을 만들 때 보통 아랫목에는 <span class="cn-word" data-pos="adj" data-tr="qalin">두꺼운</span> 돌을 놓고 윗목에는 그보다 <span class="cn-word" data-pos="adj" data-tr="yupqa">얇은</span> 돌을 놓는데 이것은 아랫목에 열기를 많이 저장할 수 있도록 하고 열이 덜 가는 윗목은 <span class="cn-word" data-pos="adv" data-tr="tez">빨리</span> <span class="cn-word" data-tr="qizdirish">달구려는</span> 목적이 있다. 온돌의 과학적 원리는 고층 아파트, 침대 문화가 자리 잡은 오늘날까지도 보일러식 난방, 돌침대, 돌소파, 온돌 매트, 찜질방의 형태로 <span class="cn-word" data-pos="verb" data-tr="davom etib, saqlanib">이어져</span> 오고 있다.</p>
<p>이렇듯 우리가 <span class="cn-word" data-pos="adv" data-tr="odat tusida">습관적으로</span> 하는 행동이나 <span class="cn-word" data-pos="adv" data-tr="beixtiyor">무심코</span> 사용하는 물건들 속에도 과학의 원리가 숨어 있다는 것을 알 수 있다. 누구에 의해 언제부터 시작되었는지는 모르지만 아주 과학적인 선조들의 삶의 방식, 그것이 오늘날의 <span class="cn-word" data-pos="adj" data-tr="qulay">편리한</span> 생활을 가능하게 했을 것이다. 그렇다면 어디에 어떤 원리가 숨어있는지 지금부터라도 주변에 관심을 가지고 <span class="cn-word" data-pos="verb" data-tr="kuzatmoq, koʻrib chiqmoq">살펴보는</span> 것은 어떨까.</p>''',
        "questions": [
            {
                "text": "이 글에서 설명하는 '김치냉장고'의 원리와 관계있는 옛 방식은?",
                "choices": [
                    "김칫독을 땅에 묻어 일정한 온도로 저장한 것",
                    "김치를 불에 익혀 먹은 것",
                    "김치를 햇볕에 말린 것",
                ],
                "answer": 0,
                "explanation": "Matnda ajdodlar kimchini yerga koʻmib, bir tekis haroratda saqlagani va aynan shu usul kimchi muzlatgichida qoʻllanilishi aytilgan.",
            },
            {
                "text": "금줄을 21일(삼칠일) 동안 친 이유로 알맞은 것은?",
                "choices": [
                    "아기와 산모의 면역력이 어느 정도 회복되는 기간이라서",
                    "21일 후에 아기 이름을 지어서",
                    "21일 동안 손님을 초대하기 위해서",
                ],
                "answer": 0,
                "explanation": "Matnda 21 kun — chaqaloq va onaning immuniteti maʼlum darajada tiklanadigan muddat deb hisoblangani uchun 금줄 shuncha muddat osib qoʻyilgani aytilgan.",
            },
            {
                "text": "이 글 전체가 말하고자 하는 것은 무엇입니까?",
                "choices": [
                    "옛 선조들의 생활 방식 속에 과학의 원리가 숨어 있다.",
                    "전통 방식은 모두 비과학적이므로 버려야 한다.",
                    "김치는 냉장고에 넣으면 안 된다.",
                ],
                "answer": 0,
                "explanation": "Matn kimchi xumi, 금줄, ondol misolida ajdodlar turmush tarzida yashirin ilmiy asos borligini koʻrsatadi — bu asosiy gʻoya.",
            },
        ],
    },
    {
        "title":   "즐기면서 나누는 기부 문화",
        "summary": "Xarid orqali, isteʼdod bilan, SNSʼda — yoshlarning zamonaviy xayriya usullari.",
        "order":   18,
        "grammar": [
            {
                "pattern":  "-는 것은 물론이려니와",
                "meaning":  "...i tabiiy, qolaversa/shuningdek (rasmiy qoʻshimcha).",
                "examples": ["소비 욕망을 충족시키는 것은 물론이려니와 선행까지 실천한다.", "실력은 물론이려니와 인성도 훌륭해요."],
            },
            {
                "pattern":  "-(으)ㄹ 뿐이다",
                "meaning":  "Faqatgina ... xolos (cheklov).",
                "examples": ["기부를 못한다는 것은 이들에게 남의 이야기일 뿐이다.", "저는 최선을 다할 뿐이에요."],
            },
            {
                "pattern":  "-에 발맞춰",
                "meaning":  "...ga hamqadam/mos ravishda (moslashib).",
                "examples": ["이에 발맞춰 기업들이 '착한 상품'을 내놓는다.", "시대에 발맞춰 변화해야 해요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 것으로 유명하다",
                "meaning":  "...ligi bilan mashhur.",
                "examples": ["그 팬클럽은 기부금을 전달하는 것으로 유명하다.", "그 식당은 김치찌개가 맛있는 것으로 유명해요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-pos="adj" data-tr="oʻziga xos, gʻayrioddiy">독특한</span> 방법으로 <span class="cn-word" data-tr="xayriya">기부</span>에 <span class="cn-word" data-pos="verb" data-tr="ishtirok etadigan">참여하는</span> 젊은이들이 늘고 있다. 소비를 통한 기부, 재능 기부 등 생활 속에서 다양한 방법으로 기부를 <span class="cn-word" data-pos="verb" data-tr="amalga oshirmoqda">실천하고</span> 있는 젊은이들의 기부 문화를 <span class="cn-word" data-pos="verb" data-tr="koʻrib chiqaylik">살펴보자</span>.</p>
<p>요즘 젊은 사람들은 자신이 필요한 물건을 구입하면서 다른 사람을 <span class="cn-word" data-pos="verb" data-tr="yordam berish">도울</span> 수 있는 '착한 소비'를 통해 생활 속에서 기부를 실천하고 있다. 직장인 김 모(25) 씨는 도시락을 먹을 때도 일부 금액이 국내 <span class="cn-word" data-tr="ovqatsiz qoladigan bolalar">결식 아동</span>에게 기부되는 제품을 <span class="cn-word" data-pos="verb" data-tr="tanlab">고르고</span>, 마트에서 물건을 살 때도 기부와 연결되는 제품을 골라 장바구니에 담는다. 김 씨처럼 물건을 사는 것만으로도 좋은 일을 할 수 있는 '착한 상품'을 고르는 젊은 소비자들이 늘고 있다. 자신의 소비 <span class="cn-word" data-tr="xohish-istak">욕망</span>을 <span class="cn-word" data-pos="verb" data-tr="qondiradigan">충족시키는</span> 것은 물론이려니와 <span class="cn-word" data-tr="ezgu, savob ish">선행</span>까지도 <span class="cn-word" data-pos="adv" data-tr="birga, bir vaqtda">더불어</span> 실천하는 '새로운 소비 문화'를 <span class="cn-word" data-pos="verb" data-tr="shakllantirmoqda">형성하고</span> 있는 것이다. 이에 발맞춰 각 기업에서는 '착한 상품'을 <span class="cn-word" data-pos="adv" data-tr="ketma-ket, birin-ketin">속속</span> 내놓고 있다.</p>
<p>대학생들은 그들의 <span class="cn-word" data-tr="isteʼdod">재능</span>을 어려운 이웃에게 <span class="cn-word" data-pos="verb" data-tr="ulashadigan, boʻlishadigan">나누는</span> 재능 기부도 <span class="cn-word" data-pos="adv" data-tr="faol">활발하게</span> 진행하고 있다. 경제적인 <span class="cn-word" data-tr="imkoniyat, bemalollik">여유</span>가 없어 기부를 못한다는 것은 이들에게는 남의 이야기일 뿐이다. 개인이 가진 지식과 기술, 나아가 목소리 같은 자원까지도 모두 기부의 대상이 될 수 있다. 최근에는 각기 다른 능력을 가진 대학생들이 <span class="cn-word" data-pos="adv" data-tr="bevosita, oʻzlari">직접</span> 자신들의 뜻을 <span class="cn-word" data-pos="verb" data-tr="jamlab, birlashtirib">모아</span> 단체를 만들어 활동하기도 한다.</p>
<p>요즘 새로운 팬클럽 문화 중 <span class="cn-word" data-pos="verb" data-tr="koʻzga tashlanadigan">눈에 띄는</span> 것은 바로 자신이 좋아하는 스타의 이름으로 특정 단체에 기부를 하는 문화이다. <span class="cn-word" data-pos="adv" data-tr="shunchaki">단순히</span> 스타를 응원하는 데 그치지 않고 스타의 이름으로 좋은 일을 하는 팬들이 늘면서 팬클럽 간의 경쟁으로 <span class="cn-word" data-pos="verb" data-tr="ulanib, davom etib">이어지기도</span> 한다. 한 걸그룹의 팬클럽은 각 멤버의 생일마다 <span class="cn-word" data-tr="xayriya mablagʻi">기부금</span>을 모아 사회단체에 <span class="cn-word" data-pos="verb" data-tr="yetkazadigan, topshiradigan">전달하는</span> 것으로 유명하다. 그리고 한 배우의 팬클럽도 그의 생일에 소아암 환자 돕기 기부를 선물해 <span class="cn-word" data-tr="gap-soʻz mavzusi, shov-shuv">화제</span>가 되었다. 이처럼 팬들이 자신의 스타 사랑을 이웃 사랑 실천으로 보여줘 더 많은 사람들에게 <span class="cn-word" data-tr="koʻngil iliqligi">훈훈함</span>을 주고 있다.</p>
<p>SNS 기부 또한 젊은 층들이 <span class="cn-word" data-pos="adv" data-tr="asosan">주로</span> 이용하는 기부 방식이다. 네티즌들이 SNS를 통해 어려운 이웃의 <span class="cn-word" data-tr="hayotiy voqea, hikoya">사연</span>에 댓글을 <span class="cn-word" data-pos="verb" data-tr="yozib qoʻysa (izoh)">달면</span> 기업은 댓글의 수에 따라 사연의 주인공에게 기부를 한다. 한 자동차 회사의 '기프트카' 캠페인에서는 한 달간 매일 백 개 이상의 응원 댓글이 달리는 사연의 주인공들에게 자동차를 선물해주는 기부 활동을 <span class="cn-word" data-pos="verb" data-tr="oʻtkazgan edi, tashkil qilgan edi">벌였었다</span>. 이러한 SNS 기부는 기업의 기부 활동에 개개인의 참여를 <span class="cn-word" data-pos="verb" data-tr="jalb qilib, boshlab">이끌어</span> 내고 있다.</p>
<p>자신이 해야 할 일, 자신이 잘할 수 있는 일, 자신이 좋아하는 일을 하면서도 다른 사람을 도울 수 있다면 그로 인한 가치와 보람이 더 크다는 것을 젊은이들은 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> 알고 있다. 통장 <span class="cn-word" data-tr="hisobdagi qoldiq">잔고</span>를 보며 <span class="cn-word" data-pos="verb" data-tr="ikkilanadigan, taraddudlanadigan">망설이는</span> 마음들을 <span class="cn-word" data-pos="adj" data-tr="uyatli, hijolatli">부끄럽게</span> 만드는 이들의 기부 방식은 <span class="cn-word" data-tr="saxovat, ulashish">나눔</span>도 '즐기는 것'임을 보여 주며 새로운 기부 문화를 이끌어 가고 있다.</p>''',
        "questions": [
            {
                "text": "이 글에서 소개한 젊은이들의 기부 방식이 아닌 것은?",
                "choices": [
                    "착한 소비를 통한 기부",
                    "재능 기부",
                    "큰 회사를 직접 세워서 하는 기부",
                ],
                "answer": 2,
                "explanation": "Matnda \"착한 소비\", isteʼdod xayriyasi, muxlislar klubi va SNS xayriyasi tilga olingan, lekin katta kompaniya tashkil qilib xayriya qilish haqida gap yoʻq.",
            },
            {
                "text": "'착한 소비'란 무엇입니까?",
                "choices": [
                    "물건을 아주 싸게 사는 것",
                    "필요한 물건을 사면서 그 일부가 남을 돕는 데 쓰이는 소비",
                    "물건을 전혀 사지 않는 것",
                ],
                "answer": 1,
                "explanation": "Matnda \"착한 소비\" — kerakli narsa sotib olayotib, uning bir qismi (masalan, ovqatsiz bolalarga) yordamga sarflanadigan isteʼmol deb tushuntirilgan.",
            },
            {
                "text": "이 글에서 젊은이들의 기부 문화가 보여 주는 것으로 가장 알맞은 것은?",
                "choices": [
                    "나눔도 즐기면서 실천할 수 있다는 것",
                    "돈이 많아야만 기부할 수 있다는 것",
                    "기부는 나이 든 사람만 하는 것이라는 것",
                ],
                "answer": 0,
                "explanation": "Matn oxirida yoshlarning xayriyasi \"나눔도 즐기는 것\"ligini koʻrsatishi aytilgan — ulashishni ham zavq bilan qilish mumkin. Matn pul koʻp boʻlishi shart emasligini ham taʼkidlaydi.",
            },
        ],
    },
    {
        "title":   "김홍도와 신윤복",
        "summary": "Xalq hayotini chizgan ikki buyuk rassom — Kim Hongdo va Shin Yunbok.",
        "order":   19,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 뿐더러",
                "meaning":  "...gina emas, ustiga-ustak (qoʻshimcha).",
                "examples": ["인생이 다를 뿐더러 화풍에도 차이가 있다.", "값이 쌀 뿐더러 품질도 좋아요."],
            },
            {
                "pattern":  "-(으)ㅁ으로써",
                "meaning":  "...qilish orqali/yoʻli bilan (vosita).",
                "examples": ["새로운 소재를 다룸으로써 소재의 폭을 넓혔다.", "꾸준히 연습함으로써 실력을 키웠어요."],
            },
            {
                "pattern":  "-(으)로 미루어 보아",
                "meaning":  "...dan kelib chiqib, shunga qaraganda (taxmin asosi).",
                "examples": ["기록이 없는 것으로 미루어 보아 평범하게 살았을 것이다.", "표정으로 미루어 보아 화가 난 것 같아요."],
            },
            {
                "pattern":  "-기(가) 이를 데 없다",
                "meaning":  "Behad ..., taʼriflab boʻlmas darajada.",
                "examples": ["그의 필선은 우아하기 이를 데 없다.", "경치가 아름답기 이를 데 없어요."],
            },
        ],
        "body": '''<p>18세기 이전까지 한국 <span class="cn-word" data-tr="rassomlar olami">화단</span>의 <span class="cn-word" data-tr="asosiy oqim">주류</span>를 <span class="cn-word" data-pos="verb" data-tr="tashkil qilgan">이루었던</span> 그림은 <span class="cn-word" data-tr="tabiat manzarasi rasmi">산수화</span>였다. 자연의 아름다움과 계절의 변화를 <span class="cn-word" data-pos="verb" data-tr="chizgan">그린</span> 산수화는 <span class="cn-word" data-pos="adj" data-tr="oʻziga xos, mustaqil">독자적인</span> 화풍을 <span class="cn-word" data-pos="verb" data-tr="shakllantirib, qurib">구축하면서</span> 많은 사랑을 받고 있었다. 이러한 때에 자연이 아닌 사람을 그린 <span class="cn-word" data-tr="xalq turmushi rasmi">풍속화</span>가 <span class="cn-word" data-pos="verb" data-tr="paydo boʻlgan">등장한</span> 것은 매우 <span class="cn-word" data-pos="adj" data-tr="anʼanani buzuvchi, gʻayrioddiy">파격적인</span> 일이었다. 김홍도와 신윤복은 그 변화를 <span class="cn-word" data-pos="verb" data-tr="boshqargan, yetakchilik qilgan">주도했던</span> 화가들이다.</p>
<p>김홍도와 신윤복은 사람들의 실제 생활 모습을 그렸다는 점에서 <span class="cn-word" data-pos="adj" data-tr="oʻxshasa-da">비슷하지만</span> 살아온 인생이 다를 뿐더러 그림의 <span class="cn-word" data-tr="mavzu, material">소재</span>나 구성, 표현 방법 등에서 차이가 있다. 김홍도는 중인 집안에서 <span class="cn-word" data-pos="verb" data-tr="tugʻilib">태어나</span> 어릴 때부터 글과 그림을 배웠다. 어린 나이에 궁에 들어가서 왕의 사랑을 받으며 그림을 그리고 정치 생활을 했다. 한편 신윤복은 화가 집안에서 태어나 <span class="cn-word" data-pos="adv" data-tr="tabiiy ravishda">자연스럽게</span> 화가가 되었다. 그러나 그가 어떻게 살았는지를 알 수 있는 기록이 거의 없으며 왕명에 의한 그림도 <span class="cn-word" data-pos="adv" data-tr="umuman, aslo">전혀</span> 없는 것으로 미루어 보아 <span class="cn-word" data-pos="adv" data-tr="oddiy tarzda">평범하게</span> 살았을 것으로 <span class="cn-word" data-pos="verb" data-tr="taxmin qilinadi">짐작된다</span>.</p>
<p>두 화가는 화풍에서도 차이를 보인다. 김홍도는 서민들의 생활 모습과 일하는 모습을 <span class="cn-word" data-pos="adj" data-tr="realistik boʻlsa-da">사실적이면서도</span> 재미있게 그리고 있다. 배경 없이 인물을 중심으로 <span class="cn-word" data-pos="adv" data-tr="soddagina, kamtarona">소박하게</span> 표현하였으며, 특히 인물은 웃음 띤 <span class="cn-word" data-pos="adj" data-tr="yumaloq">둥근</span> 얼굴을 많이 그려 재미를 더하였다. 이와 다르게 신윤복은 그림에서 남녀 간의 애정과 낭만을 <span class="cn-word" data-pos="adv" data-tr="asosan">주로</span> <span class="cn-word" data-pos="verb" data-tr="aks ettirdi, ishlov berdi">다루었다</span>. 그의 <span class="cn-word" data-pos="adj" data-tr="nafis, nozik">섬세한</span> 필선과 아름다운 <span class="cn-word" data-tr="rang berish, boʻyash">채색</span>은 <span class="cn-word" data-pos="adj" data-tr="nafosatli, latofatli">우아하기</span> 이를 데 없으며 그림 안에 곁들인 짧은 시도 이러한 분위기에 한몫하고 있다. 두 화가의 대표 작품인 &lt;벼타작&gt;과 &lt;월하정인&gt;만 보아도 화풍이 <span class="cn-word" data-pos="adv" data-tr="aniq, yaqqol">확연히</span> 다름을 알 수 있다.</p>
<p>김홍도의 &lt;벼타작&gt;은 쌀을 <span class="cn-word" data-pos="verb" data-tr="hosil yigʻadigan">수확하는</span> 농부들의 바쁜 움직임이 그대로 표현된 작품이다. 힘 있고 <span class="cn-word" data-pos="adj" data-tr="ixcham, loʻnda">간결한</span> 필선으로 인물들의 동작을 <span class="cn-word" data-tr="jonlilik">생동감</span> 있게 그리고 있으며, 인물의 움직임이나 표정을 각각 다르게 표현한 것에서 화가의 <span class="cn-word" data-pos="adj" data-tr="diqqatli, sinchkov">세심한</span> <span class="cn-word" data-tr="kuzatuvchanlik">관찰력</span>을 <span class="cn-word" data-pos="verb" data-tr="sezib olmoq, koʻrmoq">엿볼</span> 수 있다. <span class="cn-word" data-pos="adj" data-tr="hashamatli, jimjimador">화려한</span> 색을 사용하지 않아서 <span class="cn-word" data-pos="adj" data-tr="sodda, kamtarona">소박한</span> 느낌이 드는 것도 특징이다.</p>
<p>한편 신윤복의 &lt;월하정인&gt;은 늦은 밤, 두 남녀의 <span class="cn-word" data-pos="adj" data-tr="yashirin, sirli">은밀한</span> 만남을 그리고 있는 작품이다. 김홍도와는 달리 인물과 배경을 아주 <span class="cn-word" data-pos="adv" data-tr="batafsil, sinchiklab">자세하게</span> <span class="cn-word" data-pos="verb" data-tr="tasvirlagan">묘사하였기</span> 때문에 그의 작품은 당시 사람들이 어떤 옷을 입고 어떤 집에서 살았는지를 알 수 있는 중요한 자료가 된다. "달은 깊어 삼경인데 두 사람 마음은 둘 말고 누가 알겠는가"라고 그림 한켠에 <span class="cn-word" data-pos="verb" data-tr="yozilgan">적힌</span> 시처럼 알 듯 말 듯한 두 남녀의 표정에서 김홍도의 그림에서와는 다른 섬세함과 부드러움을 느낄 수 있다.</p>
<p>풍속화는 이전까지 그림의 소재로 다루어지지 않았던 것들을 다룸으로써 소재의 폭을 <span class="cn-word" data-pos="verb" data-tr="kengaytirdi">넓혔다</span>. 또 <span class="cn-word" data-pos="adj" data-tr="professional, kasbiy">전문적인</span> 화가나 사대부에 의해서만 그려지던 그림이 서민의 손으로 <span class="cn-word" data-pos="verb" data-tr="koʻchadigan, oʻtadigan">옮겨지게</span> 되는 계기가 되었다. 이러한 풍속화의 새로운 <span class="cn-word" data-tr="daraja, choʻqqi">경지</span>는 김홍도와 신윤복에 의해 <span class="cn-word" data-pos="verb" data-tr="yaratildi, oʻrnatildi">세워졌다</span>고 해도 지나치지 않다. 이 두 화가 덕분에 우리는 200여 년이 흐른 지금에도 조상들의 생활 모습을 알 수 있거니와 그들이 느꼈을 감정까지도 <span class="cn-word" data-pos="adv" data-tr="bilvosita">간접적으로</span> 느낄 수 있게 된 것이다.</p>''',
        "questions": [
            {
                "text": "18세기에 '풍속화'의 등장이 파격적이었던 이유로 알맞은 것은?",
                "choices": [
                    "자연이 아니라 사람의 생활 모습을 그렸기 때문에",
                    "색을 전혀 사용하지 않았기 때문에",
                    "왕만 그릴 수 있었기 때문에",
                ],
                "answer": 0,
                "explanation": "Matnda oʻsha davrgacha asosiy oqim 산수화 (tabiat manzarasi) boʻlgani, 풍속화 esa tabiat emas, odamlar hayotini chizgani uchun \"파격적\" (anʼanani buzuvchi) boʻlgani aytilgan.",
            },
            {
                "text": "김홍도와 신윤복 그림의 차이로 알맞은 것은?",
                "choices": [
                    "김홍도는 서민의 생활을 소박하게, 신윤복은 남녀의 애정을 섬세하게 그렸다.",
                    "김홍도는 애정을, 신윤복은 농사일을 주로 그렸다.",
                    "두 사람의 그림에는 아무 차이가 없다.",
                ],
                "answer": 0,
                "explanation": "Matnda Kim Hongdo oddiy xalq hayotini soddagina, Shin Yunbok esa muhabbatni nafis boʻyoqlar bilan chizgani qarama-qarshi qoʻyilgan.",
            },
            {
                "text": "이 글에서 풍속화의 가치로 이야기한 것은?",
                "choices": [
                    "조상들의 생활 모습과 감정을 오늘날에도 알 수 있게 해 준다.",
                    "오직 왕과 귀족만 감상할 수 있다.",
                    "자연의 아름다움만을 보여 준다.",
                ],
                "answer": 0,
                "explanation": "Matn oxirida bu ikki rassom tufayli 200 yildan keyin ham ajdodlar turmushi va his-tuygʻularini bilib olishimiz mumkinligi aytilgan — 풍속화 ning qadri shu.",
            },
        ],
    },
    {
        "title":   "창문과 옷장: 인식의 힘",
        "summary": "Deraza deb shkaf eshigini ochgan sayohatchi idrokning kuchini anglab yetadi.",
        "order":   20,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 수밖에 없다",
                "meaning":  "...dan boshqa iloj yoʻq (majburiy tanlov).",
                "examples": ["밤을 지낼 곳이 없어 침대에 들 수밖에 없었다.", "차가 없어서 걸어갈 수밖에 없었어요."],
            },
            {
                "pattern":  "-았/었더니",
                "meaning":  "...gan edim, shunda (kutilmagan natija/kashfiyot).",
                "examples": ["힘껏 창문을 열어젖혔더니 시원한 바람이 들어왔다.", "아침에 일어났더니 눈이 왔더라고요."],
            },
            {
                "pattern":  "여간 -지 않다",
                "meaning":  "Oddiy emas, juda ham ... (kuchaytirish).",
                "examples": ["방이 여간 답답한 게 아니었다.", "그 일은 여간 어렵지 않아요."],
            },
            {
                "pattern":  "-(으)ㄹ지 아니면 -(으)ㄹ지",
                "meaning":  "...sammi yoki ...sammi (ikkilanish/tanlov).",
                "examples": ["쉴지 아니면 다음 마을로 갈지 고민했다.", "갈지 말지 아직 못 정했어요."],
            },
        ],
        "body": '''<p>나는 <span class="cn-word" data-tr="sayohatchi">여행가</span>이다. 여행의 경험을 사진과 함께 책에 <span class="cn-word" data-pos="verb" data-tr="joylashtirib, chop etib">실어</span> 발표해 온 지도 <span class="cn-word" data-pos="adv" data-tr="allaqachon">벌써</span> 10년째이다. 여행을 통해 나는 행복 뿐만 아니라 삶의 비밀도 <span class="cn-word" data-pos="verb" data-tr="kashf qilmoq, topmoq">발견할</span> 수 있는 것 같아 <span class="cn-word" data-pos="adv" data-tr="toʻxtovsiz">끊임없이</span> 여행길을 <span class="cn-word" data-pos="verb" data-tr="yoʻlga chiqadigan">나서게</span> 된다. 매번 여행을 할 때마다 나는 많은 일들을 보고 듣고 경험한다. 그 중에서도 나는 이 년 전 처음으로 <span class="cn-word" data-pos="verb" data-tr="urinib koʻrgan, sinab koʻrgan">시도했던</span> 자전거 여행에서 있었던 일은 <span class="cn-word" data-pos="adv" data-tr="hali ham">아직도</span> 잊을 수가 없다.</p>
<p>그때 나는 <span class="cn-word" data-pos="adj" data-tr="sokin, xilvat">한적한</span> 시골 마을을 한 시간 정도 <span class="cn-word" data-pos="verb" data-tr="yugurib ketayotgan">달리고</span> 있었다. 숙소를 정하고 쉬어야 할지 아니면 다음 마을로 이동할지 고민하고 있던 <span class="cn-word" data-tr="ayni lahza">찰나</span>에 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> 비가 내리기 시작했다. <span class="cn-word" data-pos="adv" data-tr="tez orada, darrov">금방</span> 그칠 비가 아니었다. 그래서 나는 근처 여관에 <span class="cn-word" data-pos="verb" data-tr="tunab qolishga, joylashishga">투숙하기로</span> 했다. 여관은 작고 <span class="cn-word" data-pos="adj" data-tr="koʻrimsiz, gʻarib">초라했다</span>. 내가 투숙한 방은 특히나 더 <span class="cn-word" data-pos="adj" data-tr="tor edi">좁았고</span> <span class="cn-word" data-tr="shamollatish">환기</span>도 <span class="cn-word" data-pos="adv" data-tr="tuzukroq, joyida">제대로</span> 되지 않았다. 창문은 고장이 나서 쉽게 열리지 않았다. 여간 <span class="cn-word" data-pos="adj" data-tr="dim, siqiladigan">답답한</span> 게 아니었지만 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> 날은 어두워졌고 달리 밤을 지낼 곳도 없었으므로 침대에 들어가 <span class="cn-word" data-tr="uxlashga harakat qilish">잠을 청할</span> 수밖에 없었다.</p>
<p>그러나 나는 <span class="cn-word" data-tr="dimlik, siqilish">갑갑함</span>을 <span class="cn-word" data-pos="verb" data-tr="chidamay, toqat qilmay">참지</span> 못하고 잠에서 깨어났다. <span class="cn-word" data-pos="adv" data-tr="toʻppa-toʻgʻri, darrov">곧장</span> 창가로 가서 있는 <span class="cn-word" data-pos="adv" data-tr="bor kuchi bilan">힘껏</span> 창문을 <span class="cn-word" data-pos="verb" data-tr="lang ochmoq">열어젖혔더니</span> 끼이익, 하고 <span class="cn-word" data-pos="adj" data-tr="qattiq, shovqinli">요란한</span> 소리와 함께 창문이 열렸다. 그러자 밖에서 <span class="cn-word" data-pos="adj" data-tr="salqin, yoqimli">시원한</span> 바람이 쏴 들어왔고 그제서야 가슴이 확 트이면서 기분 좋게 잠이 들 수가 있었다. 그런데 이게 웬일인가. 아침에 일어나 보니 창문은 그대로 닫혀 있었고 대신 옷장 문이 <span class="cn-word" data-pos="adv" data-tr="lang (ochiq)">활짝</span> 열려 있었던 것이다. 옷장 문을 창문이라고 믿어 의심치 않았기에 실제로는 있지도 않은 바람을 느꼈다. <span class="cn-word" data-tr="idrok, anglash">인식</span>이 <span class="cn-word" data-tr="sezgi">감각</span>에 얼마나 큰 영향을 미칠 수 있는지를 <span class="cn-word" data-pos="verb" data-tr="anglagan, tushungan">깨달았던</span> 그때의 경험은 내가 어렵고 힘들어서 포기하고 싶을 때마다 나를 <span class="cn-word" data-tr="suyab turadigan">지탱해주는</span> 힘이 되었다.</p>''',
        "questions": [
            {
                "text": "글쓴이가 밤에 시원한 바람을 느낀 것은 사실 무엇 때문이었습니까?",
                "choices": [
                    "실제로 창문이 열려서",
                    "옷장 문을 창문이라고 믿었기 때문에 (실제 바람은 없었다)",
                    "에어컨을 켰기 때문에",
                ],
                "answer": 1,
                "explanation": "Ertalab muallif deraza yopiq, aksincha shkaf eshigi ochiq boʻlganini koʻradi. U shkaf eshigini deraza deb ishongani uchun aslida yoʻq shamolni his qilgan.",
            },
            {
                "text": "이 경험을 통해 글쓴이가 깨달은 것은 무엇입니까?",
                "choices": [
                    "인식이 감각에 큰 영향을 미칠 수 있다는 것",
                    "여관은 항상 시설이 좋다는 것",
                    "자전거 여행은 위험하다는 것",
                ],
                "answer": 0,
                "explanation": "Matnda muallif \"인식이 감각에 얼마나 큰 영향을 미칠 수 있는지를 깨달았다\" deb yozadi — idrok (ishonch) sezgiga kuchli taʼsir qilishi mumkinligini angladi.",
            },
            {
                "text": "이 경험이 글쓴이에게 준 의미로 알맞은 것은?",
                "choices": [
                    "힘들 때마다 자신을 지탱해 주는 힘이 되었다.",
                    "다시는 여행을 하지 않게 만들었다.",
                    "여관을 새로 짓게 만들었다.",
                ],
                "answer": 0,
                "explanation": "Matn oxirida bu tajriba muallif qiyinchilikka duch kelib, taslim boʻlgisi kelganda uni \"지탱해주는 힘\" (suyab turuvchi kuch) boʻlgani aytilgan.",
            },
        ],
    },
    {
        "title":   "원효 대사와 해골 물",
        "summary": "Rohib Wonhyo bosh chanogʻidagi suvdan maʼrifat topadi: hamma narsa koʻngildan.",
        "order":   21,
        "grammar": [
            {
                "pattern":  "-마저",
                "meaning":  "Hatto ...ham, ...ni ham (kutilmagan qoʻshimcha).",
                "examples": ["백제를 멸망시키고 고구려마저 점령하려 했다.", "믿었던 친구마저 나를 떠났어요."],
            },
            {
                "pattern":  "-자",
                "meaning":  "...boʻlishi bilanoq, ...gach (ketma-ketlik).",
                "examples": ["폭우가 쏟아지자 동굴에서 머무르기로 했다.", "문을 열자 강아지가 뛰어나왔어요."],
            },
            {
                "pattern":  "-기 나름이다",
                "meaning":  "...ning oʻziga bogʻliq, ...ga qarab belgilanadi.",
                "examples": ["세상의 모든 일은 마음먹기 나름이다.", "성공은 노력하기 나름이에요."],
            },
            {
                "pattern":  "-(으)ㄴ들",
                "meaning":  "...sam ham (baribir foydasi yoʻq maʼnosida).",
                "examples": ["여기 있은들 깨우치지 못할 까닭이 없다.", "지금 후회한들 무슨 소용이 있겠어요?"],
            },
        ],
        "body": '''<p>때는 661년, 신라가 당과 <span class="cn-word" data-pos="verb" data-tr="ittifoq boʻlib">연합하여</span> 백제를 <span class="cn-word" data-pos="verb" data-tr="qulatib, yoʻq qilib">멸망시키고</span> 고구려마저 <span class="cn-word" data-pos="verb" data-tr="bosib olmoq, zabt etmoq">점령하기</span> 위해 <span class="cn-word" data-pos="adv" data-tr="ayni, qizigan paytda">한창</span> 통일 전쟁을 치르고 있을 때였다. 배움에 목말라 있던 신라의 <span class="cn-word" data-tr="buddist rohib">승려</span> 원효는 후배인 의상과 함께 <span class="cn-word" data-pos="adj" data-tr="katta, koʻtarilgan (orzu)">부푼</span> 꿈을 안고 선진 불교를 배우기 위해 당나라 <span class="cn-word" data-tr="chet elda oʻqish safari">유학길</span>에 올랐다. 원효와 의상은 <span class="cn-word" data-tr="quruqlik yoʻli">육로</span>를 이용하여 당나라에 가기로 결정하고 고구려 <span class="cn-word" data-tr="chegara chizigʻi">국경선</span>을 <span class="cn-word" data-pos="verb" data-tr="oshib, kesib oʻtib">넘어</span> 요동 지방까지 갔다.</p>
<p>그러나 두 사람은 고구려 군사들에게 <span class="cn-word" data-pos="verb" data-tr="qoʻlga olindi, tutildi">붙잡혔고</span>, 죽을 고비를 넘기고 <span class="cn-word" data-pos="adv" data-tr="zoʻrgʻa, arang">간신히</span> 신라 땅으로 <span class="cn-word" data-pos="verb" data-tr="qaytib kelmoq">되돌아올</span> 수 있었다. 그래서 두 번째는 당나라까지 바닷길로 떠나기로 계획하고 서해안으로 출발하였다. 경주에서 출발하여 지금의 충청남도 천안 부근에 이르렀을 때였다. 밤은 깊어 가는데 <span class="cn-word" data-tr="kuchli jala">폭우</span>가 계속 <span class="cn-word" data-pos="verb" data-tr="quyib yogʻa boshlagach">쏟아지자</span> 원효와 의상은 <span class="cn-word" data-pos="adv" data-tr="noiloj, chorasiz">부득이하게</span> 동굴 안에서 하룻밤을 <span class="cn-word" data-pos="verb" data-tr="qolish, tunash">머무르기로</span> 결정하였다. 원효는 웅크린 자세로 새우잠을 자다가 한밤중에 <span class="cn-word" data-tr="chanqash, tashnalik">갈증</span>이 나서 마침 머리맡에 놓여 있던 물을 <span class="cn-word" data-pos="adv" data-tr="beixtiyor, oʻylamay">무심코</span> 마셨다.</p>
<p>그런데 다음날 아침에 잠에서 깬 원효는 자신이 <span class="cn-word" data-pos="adv" data-tr="shirin qilib, maza qilib">달게</span> 마셨던 물이 사실은 <span class="cn-word" data-tr="bosh chanogʻi">해골</span> 안에 들어 있던 <span class="cn-word" data-pos="adj" data-tr="chirigan, aynigan">썩은</span> 물이었다는 것을 알게 되었다. 그러자 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> <span class="cn-word" data-tr="koʻngil aynishi, qayt qilish">구토</span>가 나왔다. 계속 토악질을 하다가 원효는 그 순간 <span class="cn-word" data-pos="verb" data-tr="anglab yetdi, tushunib yetdi">깨달았다</span>.</p>
<p>"해골에 담긴 물은 어젯밤이나 오늘이나 <span class="cn-word" data-pos="adj" data-tr="bir xil boʻlsa-da">똑같거늘</span> 어이하여 어제는 달디 단 물이었던 것이 오늘은 구역질을 나게 하는가? 그렇다! 어제와 오늘 사이에 달라진 것은 내 마음일 뿐이다. 진리는 <span class="cn-word" data-pos="adv" data-tr="aslo, hech qachon">결코</span> 밖에 있는 것이 아니라 내 안에 있다."</p>
<p>원효는 <span class="cn-word" data-pos="adv" data-tr="shu qadar, shunchalik">그토록</span> 원했던 <span class="cn-word" data-tr="anglash, maʼrifat">깨달음</span>을 해골 물에서 <span class="cn-word" data-pos="verb" data-tr="erishdi, topdi">얻었다</span>. 이제 원효에게 당나라로의 불교 유학은 <span class="cn-word" data-pos="verb" data-tr="maʼnosiz boʻlib qoldi">무의미해졌다</span>. 의상이 짐을 꾸리며 길을 <span class="cn-word" data-pos="verb" data-tr="shoshirdi, undaydi">재촉하였으나</span> 원효는 의상에게 가지 않겠다고 <span class="cn-word" data-pos="adv" data-tr="beparvo, xotirjam">무덤덤하게</span> 말했다.</p>
<p>"의상 스님, 나는 당에 가지 않겠소. 일체유심조, 즉 세상의 모든 일은 마음먹기 나름이니 내가 여기에 있은들 <span class="cn-word" data-pos="verb" data-tr="anglab yetmoq">깨우치지</span> 못할 까닭이 무엇이겠소. 나는 이곳에 <span class="cn-word" data-pos="verb" data-tr="qolaman">머물겠으니</span> 스님만 다녀오시오."</p>
<p><span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">결국</span> 그곳에서 의상과 <span class="cn-word" data-pos="verb" data-tr="xayrlashgan">작별한</span> 원효는 신라 땅에 남아 이곳저곳을 <span class="cn-word" data-pos="verb" data-tr="kezib, sargardon boʻlib">떠돌며</span> <span class="cn-word" data-pos="adj" data-tr="erkin">자유로운</span> 삶을 살았다. 원효가 살았던 시대의 불교는 왕실과 귀족들이 <span class="cn-word" data-pos="adv" data-tr="asosan">주로</span> 믿는 종교였다. 이러한 시기에 원효는 전국 방방곡곡을 <span class="cn-word" data-pos="adv" data-tr="erkin, bemalol">자유롭게</span> 돌아다니며 불교의 가르침을 <span class="cn-word" data-pos="adv" data-tr="oson, soddagina">쉽게</span> 풀어서 <span class="cn-word" data-pos="verb" data-tr="tarqatib, yoyib">전파하면서</span> 불교의 <span class="cn-word" data-tr="ommalashtirish">대중화</span>에 <span class="cn-word" data-pos="verb" data-tr="boshchilik qilmoq">앞장설</span> 수 있었다.</p>''',
        "questions": [
            {
                "text": "원효가 해골 물을 통해 깨달은 것은 무엇입니까?",
                "choices": [
                    "모든 일은 마음먹기에 달려 있다는 것 (일체유심조)",
                    "물은 항상 깨끗하게 걸러 마셔야 한다는 것",
                    "당나라 유학이 반드시 필요하다는 것",
                ],
                "answer": 0,
                "explanation": "Wonhyo kecha shirin tuyulgan suv bugun jirkanch tuyulishini koʻrib, oʻzgargan narsa faqat oʻz koʻngli ekanini anglaydi — \"모든 일은 마음먹기 나름\" (일체유심조).",
            },
            {
                "text": "깨달음을 얻은 뒤 원효는 어떤 선택을 했습니까?",
                "choices": [
                    "당나라 유학을 그만두고 신라에 남았다.",
                    "혼자 당나라로 떠났다.",
                    "다시 고구려로 갔다.",
                ],
                "answer": 0,
                "explanation": "Maʼrifatdan soʻng Tang eliga borish Wonhyo uchun maʼnosiz boʻlib qoladi; u Silla yurtida qolib, Uisangni yolgʻiz joʻnatadi.",
            },
            {
                "text": "신라에 남은 원효가 한 일로 알맞은 것은?",
                "choices": [
                    "전국을 돌아다니며 불교를 쉽게 풀어 대중에게 전파했다.",
                    "궁궐에 들어가 왕이 되었다.",
                    "다시는 사람을 만나지 않고 동굴에서만 살았다.",
                ],
                "answer": 0,
                "explanation": "Matnda Wonhyo mamlakat boʻylab erkin yurib, buddizm taʼlimotini sodda qilib tushuntirib, uni ommalashtirishga (대중화) boshchilik qilgani aytilgan.",
            },
        ],
    },
]
