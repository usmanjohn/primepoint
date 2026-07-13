# Keimyung Short Readings — stories 1–14 (short passages from keimyung_short_story.txt).
# A separate, SHORT collection: keep vocab light (5–10 marks) and grammar to 1–2 points
# per story (STYLE_GUIDE_CORNER.md §6). Story text = Korean, all glosses = Uzbek.
# Import: python manage.py import_corner corner/management/commands/_stories_keimyung_short_1_14.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Keimyung Short Readings",
    "description": "Qisqa oʻrta daraja (TOPIK II) matnlari — lugʻat, grammatika va savollar bilan.",
    "order":       2,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "음식",
        "summary": "Muallif jjimjilbangni yaxshi koʻradi va koreys restoranida samgyeopsalni birinchi marta koʻrganidagi taassurotlari.",
        "order":   1,
        "body": '''<p>저는 한국의 찜질방을 <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻraman">좋아합니다</span>. 찜질방에서는 친구나 가족들과 함께 음식을 먹고, 이야기하고 잠도 같이 잘 수 있기 때문입니다. 찜질방에 갔다 오면 친구와 더 <span class="cn-word" data-pos="verb" data-tr="yaqinlashib">친해지고</span> 몸은 더 건강해지는 기분이 들어서 좋습니다.</p>
<p>저는 한국의 식당에서 삼겹살을 먹은 적이 있습니다. 그런데 식탁 위에 뜨거운 <span class="cn-word" data-tr="choʻgʻ, koʻmir">숯</span>이 있는 것이 <span class="cn-word" data-pos="adj" data-tr="gʻalati edi">이상했습니다</span>. 부엌에서 요리를 끝낸 후에 손님에게 가져다 주는 제 고향과 많이 달랐기 때문입니다. 하지만 잠시 후에 <span class="cn-word" data-tr="qaychi">가위</span>가 등장했을 때는 더 <span class="cn-word" data-pos="verb" data-tr="dovdirab qoldim">당황했습니다</span>. 고기를 <span class="cn-word" data-pos="verb" data-tr="kesish">자르는</span> 데 칼이 아닌 가위를 사용하는 것이 이상했기 때문입니다. 지금은 많이 <span class="cn-word" data-pos="verb" data-tr="koʻnikib qoldim">익숙해졌지만</span> 처음엔 정말 이해하기 <span class="cn-word" data-pos="adj" data-tr="qiyin edi">어려웠습니다</span>.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄴ 적이 있다",
                "meaning":  "Oʻtmishdagi tajriba: bir ishni qilib koʻrgan/boshidan oʻtkazganini bildiradi.",
                "examples": ["저는 한국에서 삼겹살을 먹은 적이 있습니다.", "제주도에 가 본 적이 있어요?"],
            },
            {
                "pattern":  "-기 때문에",
                "meaning":  "Sabab bildiradi: ... boʻlgani uchun. Rasmiy va yozma uslubda koʻp ishlatiladi.",
                "examples": ["같이 잘 수 있기 때문에 찜질방을 좋아합니다.", "고향과 많이 달랐기 때문에 이상했습니다."],
            },
        ],
        "questions": [
            {
                "text": "글쓴이가 삼겹살 식당에서 당황한 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "고기를 칼이 아닌 가위로 잘랐기 때문에",
                    "음식이 너무 매웠기 때문에",
                    "식당에 손님이 너무 많았기 때문에",
                ],
                "answer": 0,
                "explanation": "Matnda muallif \"고기를 자르는 데 칼이 아닌 가위를 사용하는 것이 이상했다\" deydi — u qaychi ishlatilgani uchun dovdiraydi. Ovqatning achchiqligi yoki mijozlar soni haqida gap yoʻq.",
            },
            {
                "text": "글쓴이가 찜질방을 좋아하는 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "혼자 조용히 있을 수 있어서",
                    "값이 아주 싸기 때문에",
                    "친구나 가족과 함께 먹고 이야기하며 지낼 수 있어서",
                ],
                "answer": 2,
                "explanation": "Muallif jjimjilbangni yoqtirish sababini \"친구나 가족들과 함께 음식을 먹고, 이야기하고 잠도 같이 잘 수 있기 때문\" deb izohlaydi. Yolgʻizlik yoki narx haqida aytilmagan.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "시치미를 떼다",
        "summary": "‘Sichimi ttemoq’ iborasi qayerdan kelib chiqqan — lochin ovi va yolgʻon daʼvo qiluvchilar haqidagi tarix.",
        "order":   2,
        "body": '''<p><strong>의미:</strong> 자기가 하고도 하지 않은 <span class="cn-word" data-pos="verb" data-tr="...ganday koʻrsatmoq">척하</span>거나 알고 있으면서도 모르는 척하다.</p>
<p>‘시치미’란 원래 <span class="cn-word" data-tr="lochin">매</span>의 주인을 알기 위해 주소를 적어 매의 꼬리에 단 네모 모양의 이름표를 <span class="cn-word" data-pos="verb" data-tr="ishora qiladi, anglatadi">가리키는</span> 말이다. 옛날 한국 사람들은 겨울철이 되면 매를 데리고 사냥을 나갔다. 그런데 여러 사람이 함께 사냥을 하다가 매를 <span class="cn-word" data-pos="verb" data-tr="yoʻqotib qoʻyish">잃어버리는</span> 일이 <span class="cn-word" data-pos="adv" data-tr="baʼzan">가끔</span> 있었다. 그래서 주인의 이름과 주소를 쓴 이름표를 매의 꼬리에 달았다. 이것을 시치미라고 불렀다. 시치미만 보면 그 매의 주인이 누구인지 <span class="cn-word" data-pos="adv" data-tr="darrov, tezda">금방</span> 알 수 있었다.</p>
<p>그런데 가끔 나쁜 사람들이 이 시치미를 <span class="cn-word" data-pos="verb" data-tr="olib tashlamoq, yulib olmoq">떼는</span> 일이 생겼다. 시치미를 떼어 버리고, 매를 자기가 가지는 것이다. 이렇게 남의 매를 가지고 자기 매라고 <span class="cn-word" data-pos="verb" data-tr="oʻjarlik bilan daʼvo qilmoq">우기는</span> 사람들 때문에 이 말이 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">생겨나게</span> 되었다고 한다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)면서도",
                "meaning":  "Ziddiyat: bir holat mavjud boʻlsa-da, unga zid ish qilinadi (garchi ... boʻlsa ham).",
                "examples": ["알고 있으면서도 모르는 척했다.", "돈이 많으면서도 잘 쓰지 않는다."],
            },
            {
                "pattern":  "-다가",
                "meaning":  "Bir ishni qilib turib, uni toʻxtatib boshqa holatga oʻtishni bildiradi.",
                "examples": ["사냥을 하다가 매를 잃어버렸다.", "집에 가다가 친구를 만났어요."],
            },
        ],
        "questions": [
            {
                "text": "‘시치미’가 원래 가리키던 것은 무엇입니까?",
                "choices": [
                    "사냥에 쓰는 특별한 칼",
                    "매의 꼬리에 단, 주인의 이름과 주소를 적은 이름표",
                    "겨울에 매를 넣어 두던 상자",
                ],
                "answer": 1,
                "explanation": "Matnda \"매의 주인을 알기 위해 주소를 적어 매의 꼬리에 단 네모 모양의 이름표\" deb aniq aytilgan. Pichoq yoki quti haqida gap yoʻq.",
            },
            {
                "text": "‘시치미를 떼다’라는 말이 생겨난 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "매가 이름표를 스스로 떨어뜨렸기 때문에",
                    "사람들이 매 기르기를 그만두었기 때문에",
                    "남의 매의 이름표를 떼고 자기 매라고 우기는 사람들이 있었기 때문에",
                ],
                "answer": 2,
                "explanation": "Yomon niyatli odamlar sichimini yulib olib, lochinni oʻziniki deb oʻjarlik qilgani uchun bu ibora paydo boʻlgan — matnning oxirgi jumlasi shuni aytadi.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "아무것도 사지 않은 날",
        "summary": "‘Hech narsa sotib olmaslik kuni’ kampaniyasi haqidagi taqdimot — atrof-muhitni asrash uchun bir kunlik harakat.",
        "order":   3,
        "body": '''<p>안녕하십니까? 저는 오늘 발표를 맡은 ○○입니다. 여러분은 오늘 하루 무엇을 샀습니까? 혹은 하루 종일 아무것도 사지 않은 날이 있었습니까? 환경을 보호하기 위한 여러 활동 중에서 저는 ‘아무것도 사지 않는 날’에 대해 <span class="cn-word" data-pos="verb" data-tr="oʻrganib chiqdim, tekshirdim">조사해</span> 보았습니다. 그럼 지금부터 제가 조사한 내용에 대해 발표하도록 하겠습니다.</p>
<p>‘아무것도 사지 않는 날’은 현재 65개국에서 매년 11월 말 경에 열리고 있습니다. 1992년 캐나다에서 광고 일을 하던 Ted Dave라는 사람에 의해 시작되어 여러 나라로 <span class="cn-word" data-pos="verb" data-tr="tarqaldi">퍼져</span> 나갔다고 합니다. 이날은 하루 24시간 동안 아무것도 사지 않을 뿐 아니라 전등, TV, 컴퓨터, <span class="cn-word" data-pos="adj" data-tr="keraksiz">불필요한</span> 전기 기구들을 <span class="cn-word" data-pos="verb" data-tr="oʻchirmoq">끄고</span> 차들을 주차시켜 놓고 휴대 전화도 꺼 놓습니다. 이러한 활동을 통해 상품 생산에서 소비에 이르기까지 발생하는 모든 환경오염과 자원 <span class="cn-word" data-tr="tugash, kamayish">고갈</span>, 노동 문제 등을 사람들에게 알리고, 유행과 쇼핑에 <span class="cn-word" data-pos="verb" data-tr="mukkasidan ketgan">중독된</span> 현대인의 생활 습관을 <span class="cn-word" data-pos="verb" data-tr="oʻzini tahlil qilmoq, pushaymon boʻlmoq">반성하게</span> 합니다.</p>
<p>이 캠페인은 빠른 속도로 많은 나라로 퍼져 나갔으며 한국에서는 1999년부터 ‘녹색연합’이라는 환경 보호 단체가 이 캠페인을 벌이고 있습니다. 이 캠페인은 단 하루이지만, 다양한 나라와 도시에서 쇼핑하는 대중들이 그들의 소비 행위가 환경에 미치는 영향을 다시 한 번 생각할 수 있는 기회를 <span class="cn-word" data-pos="verb" data-tr="tayyorlab beradi, yaratadi">마련해</span> 줍니다.</p>
<p>여러분, 우리도 이날 하루만이라도 이러한 활동을 하면서 환경 문제에 대해 생각하는 기회를 가져 보면 어떨까요? 그럼, 이상으로 제 발표를 마치겠습니다. 경청해 주셔서 감사합니다.</p>''',
        "grammar": [
            {
                "pattern":  "-을/ㄹ 뿐(만) 아니라",
                "meaning":  "Nafaqat ..., balki ... ham. Ikkinchi qism birinchisiga qoʻshimcha maʼlumot qoʻshadi.",
                "examples": ["아무것도 사지 않을 뿐 아니라 전등도 끕니다.", "그는 똑똑할 뿐만 아니라 성실하다."],
            },
            {
                "pattern":  "-기 위해(서)",
                "meaning":  "Maqsad: ... qilish uchun / ... maqsadida.",
                "examples": ["환경을 보호하기 위해서 시작되었다.", "건강을 지키기 위해 운동을 한다."],
            },
        ],
        "questions": [
            {
                "text": "‘아무것도 사지 않는 날’의 목적으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "물건을 더 싸게 사도록 돕기 위해서",
                    "소비가 환경에 미치는 영향을 다시 생각하게 하기 위해서",
                    "새로운 상품을 널리 광고하기 위해서",
                ],
                "answer": 1,
                "explanation": "Matn kampaniya \"소비 행위가 환경에 미치는 영향을 다시 한 번 생각할 수 있는 기회\" berishini aytadi. Arzon xarid yoki reklama — aksincha, kampaniyaga zid.",
            },
            {
                "text": "이날 사람들이 하는 행동으로 알맞지 않은 것은 무엇입니까?",
                "choices": [
                    "전등과 TV, 컴퓨터를 끈다.",
                    "필요한 물건을 이날에 몰아서 많이 산다.",
                    "휴대 전화를 꺼 놓고 차를 주차시켜 둔다.",
                ],
                "answer": 1,
                "explanation": "Bu kunning mohiyati — 24 soat hech narsa sotib olmaslik. Shuning uchun \"몰아서 많이 산다\" varianti matnga zid; qolgan ikkitasi matnda aynan sanab oʻtilgan.",
            },
            {
                "text": "한국에서 이 캠페인을 벌이고 있는 단체는 어디입니까?",
                "choices": ["녹색연합", "캐나다 광고 협회", "환경부"],
                "answer": 0,
                "explanation": "\"한국에서는 1999년부터 ‘녹색연합’이라는 환경 보호 단체가 이 캠페인을 벌이고 있습니다\" — matnda toʻgʻridan-toʻgʻri aytilgan.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "떡",
        "summary": "Muallif ttokni juda yaxshi koʻradi — ertalabki ovqat, ttok kafe va ota-onaga ttok tort haqida.",
        "order":   4,
        "body": '''<p>나는 떡을 아주 <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻraman">좋아한다</span>. 그래서 아침은 떡으로 <span class="cn-word" data-pos="verb" data-tr="oʻrniga ishlataman">대신하고</span>, 친구와 만날 때도 장소를 떡 카페로 <span class="cn-word" data-pos="verb" data-tr="belgilamoq">정할</span> 때가 많다. 떡 카페는 여러 종류의 떡들을 작게 <span class="cn-word" data-pos="verb" data-tr="qadoqlab">포장해서</span> <span class="cn-word" data-pos="verb" data-tr="sotadi">판매하기</span> 때문에 커피나 차와 함께 먹기 좋다. 그리고 부모님 생신에는 떡 케이크를 사 드린다. <span class="cn-word" data-pos="adj" data-tr="shirin emas">달지 않고</span> 건강에도 좋아 부모님이 아주 좋아하시기 때문이다.</p>''',
        "grammar": [
            {
                "pattern":  "-을/ㄹ 때가 많다",
                "meaning":  "Koʻpincha shunday boʻladi / shunday qilaman degan maʼnoni bildiradi.",
                "examples": ["떡 카페로 약속 장소를 정할 때가 많다.", "주말에는 집에서 쉴 때가 많아요."],
            },
            {
                "pattern":  "-아/어 드리다",
                "meaning":  "Kattaga/hurmatli kishiga biror ishni qilib berishni hurmat bilan bildiradi (‘-아/어 주다’ ning hurmat shakli).",
                "examples": ["부모님께 떡 케이크를 사 드린다.", "할머니께 편지를 읽어 드렸어요."],
            },
        ],
        "questions": [
            {
                "text": "글쓴이가 친구와 만날 때 떡 카페를 자주 고르는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "떡 카페가 가장 싸기 때문에",
                    "떡을 작게 포장해 팔아 커피나 차와 함께 먹기 좋기 때문에",
                    "집에서 가장 가깝기 때문에",
                ],
                "answer": 1,
                "explanation": "Matn: \"작게 포장해서 판매하기 때문에 커피나 차와 함께 먹기 좋다.\" Narx yoki masofa haqida gap yoʻq.",
            },
            {
                "text": "부모님이 떡 케이크를 좋아하시는 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "달지 않고 건강에도 좋기 때문에",
                    "값이 비싸고 귀하기 때문에",
                    "만들기가 아주 쉽기 때문에",
                ],
                "answer": 0,
                "explanation": "\"달지 않고 건강에도 좋아 부모님이 아주 좋아하시기 때문이다\" — sabab aniq: shirin emas va sogʻliqqa foydali.",
            },
        ],
    },
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "한국말도 못하는데 영어 교육?",
        "summary": "Koreyada ingliz tili taʼlimi tobora erta yoshda boshlanmoqda — bolalar koreyschani oʻrganayotib inglizchani ham oʻzlashtiradi.",
        "order":   5,
        "body": '''<p>영어 유치원에 영어 학원, 영어 <span class="cn-word" data-tr="erta">조기</span> 교육 시기가 <span class="cn-word" data-pos="verb" data-tr="oldinga surilmoqda, ertaroq boshlanmoqda">앞당겨지고</span> 있다. 이제는 아이가 한국말을 배우기 시작할 때 영어 <span class="cn-word" data-tr="bolalar qoʻshigʻi">동요</span>나 <span class="cn-word" data-tr="ertak">동화</span>를 통해 <span class="cn-word" data-pos="adv" data-tr="tabiiy ravishda">자연스럽게</span> 영어도 함께 <span class="cn-word" data-pos="verb" data-tr="oʻrgatmoq">배우게</span> 하려는 것이다.</p>''',
        "grammar": [
            {
                "pattern":  "-게 하다",
                "meaning":  "Undov/majburiy shakl: birovga biror ishni qildirish (...tirmoq, ...dirmoq).",
                "examples": ["영어도 함께 배우게 한다.", "아이를 일찍 자게 했어요."],
            },
            {
                "pattern":  "-는데",
                "meaning":  "Fon/vaziyat yoki qarama-qarshilikni bildiruvchi bogʻlovchi: ...gan holda, ...-ku.",
                "examples": ["한국말도 못하는데 영어를 가르친다.", "밖에 비가 오는데 우산이 없어요."],
            },
        ],
        "questions": [
            {
                "text": "이 글에서 말하는 최근의 경향으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "영어 조기 교육을 시작하는 시기가 점점 빨라지고 있다.",
                    "영어 학원의 수가 점점 줄고 있다.",
                    "아이들이 한국말을 먼저 다 배운 뒤에 영어를 배운다.",
                ],
                "answer": 0,
                "explanation": "\"영어 조기 교육 시기가 앞당겨지고 있다\" — taʼlim tobora erta boshlanmoqda. Qolgan ikki variant matnga zid.",
            },
            {
                "text": "부모들이 바라는 것으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "아이가 한국말을 잊고 영어만 쓰기를",
                    "아이가 한국말을 배울 때 영어도 자연스럽게 함께 배우기를",
                    "아이가 유치원에 가지 않고 집에서만 배우기를",
                ],
                "answer": 1,
                "explanation": "Matn: \"한국말을 배우기 시작할 때 ... 자연스럽게 영어도 함께 배우게 하려는 것.\" Maqsad — ikkalasini birga oʻrgatish, koreyschani unuttirish emas.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "‘펭귄 아빠’ vs ‘독수리 아빠’",
        "summary": "Bolasini chet elga oʻqishga yuborgan otalar oilaning imkoniyatiga qarab ‘burgut’, ‘gʻoz’ yoki ‘pingvin ota’ deb ataladi.",
        "order":   6,
        "body": '''<p>여름 방학을 <span class="cn-word" data-pos="verb" data-tr="arafasida">앞두고</span> 조기 유학을 보내는 가정들이 <span class="cn-word" data-pos="adv" data-tr="ketma-ket">속속</span> <span class="cn-word" data-pos="verb" data-tr="ortmoqda">증가하고</span> 있다. 아이가 유학을 가 있는 가정의 아빠는 경제력에 따라 각각 다르게 <span class="cn-word" data-pos="verb" data-tr="ataladi">불린다</span>. <span class="cn-word" data-tr="imkoniyat, bemalollik">여유</span>가 있어서 언제든 보고 싶을 때 비행기에 몸을 실을 수 있으면 ‘독수리 아빠’, <span class="cn-word" data-tr="ahvol, sharoit">형편</span>이 별로 좋지 못해서 일 년에 한두 번 정도밖에 못 간다면 ‘기러기 아빠’, 있는 돈 다 <span class="cn-word" data-pos="verb" data-tr="yigʻib">모아서</span> 아이를 유학 보내 놓고 빈 집에 <span class="cn-word" data-pos="adv" data-tr="yolgʻiz">홀로</span> 남아서 가족을 <span class="cn-word" data-pos="verb" data-tr="sogʻinadigan">그리워하는</span> 경우는 ‘펭귄 아빠’라고 불린다.</p>''',
        "grammar": [
            {
                "pattern":  "-밖에 + (부정)",
                "meaning":  "Faqat ... (dan boshqa emas): oz miqdorni taʼkidlaydi, doim inkor feʼl bilan keladi.",
                "examples": ["일 년에 한두 번밖에 못 간다.", "천 원밖에 없어요."],
            },
            {
                "pattern":  "-에 따라(서)",
                "meaning":  "...ga qarab / ...ga muvofiq: bir narsa ikkinchisiga bogʻliq holda oʻzgaradi.",
                "examples": ["경제력에 따라 다르게 불린다.", "계절에 따라 옷이 달라진다."],
            },
        ],
        "questions": [
            {
                "text": "아빠들을 각각 다르게 부르는 기준은 무엇입니까?",
                "choices": ["아빠의 나이", "아빠의 직업", "아빠(가정)의 경제력"],
                "answer": 2,
                "explanation": "\"경제력에 따라 각각 다르게 불린다\" — asosiy meʼzon oilaning iqtisodiy imkoniyati. Yosh yoki kasb aytilmagan.",
            },
            {
                "text": "‘기러기 아빠’에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "형편이 좋지 않아 일 년에 한두 번밖에 아이를 못 보는 아빠",
                    "돈이 많아 언제든 비행기로 아이를 보러 가는 아빠",
                    "아이와 함께 외국에 사는 아빠",
                ],
                "answer": 0,
                "explanation": "Matn ‘gʻoz ota’ni \"형편이 별로 좋지 못해서 일 년에 한두 번 정도밖에 못 간다\" deb taʼriflaydi. Birinchi variant — ‘burgut ota’, uchinchisi matnda yoʻq.",
            },
            {
                "text": "‘펭귄 아빠’의 모습으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "자주 외국에 나가 아이와 시간을 보낸다.",
                    "돈을 다 모아 아이를 유학 보내고 홀로 남아 가족을 그리워한다.",
                    "유학을 반대해 아이를 보내지 않는다.",
                ],
                "answer": 1,
                "explanation": "\"있는 돈 다 모아서 ... 빈 집에 홀로 남아서 가족을 그리워하는 경우\" — aynan pingvin ota. Uning imkoni boʻlmagani uchun bora olmaydi.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "아이들이 진학하면 엄마들은 알바 뛴다",
        "summary": "Farzandlari yuqori sinfga oʻtgach, qoʻshimcha taʼlim xarajati oiladagi onani ishga chiqishga majbur qiladi.",
        "order":   7,
        "body": '''<p>고등학교 1학년, 중학교 3학년짜리 두 자녀를 둔 김미영(가명·45) 씨는 <span class="cn-word" data-pos="adj" data-tr="oddiy">평범한</span> 중산층 주부이다. 남편의 월급으로 크게 <span class="cn-word" data-pos="adj" data-tr="yetishmaydigan">부족하지</span> 않았던 김 씨의 가계는 아이들이 상급 학교에 <span class="cn-word" data-pos="verb" data-tr="oʻqishga kirmoq">진학하면서부터</span> <span class="cn-word" data-pos="verb" data-tr="chayqalib, qiyinlashib">휘청거리기</span> 시작했다. 그 이유는 바로 <span class="cn-word" data-tr="qoʻshimcha taʼlim xarajati">사교육비</span> 때문이었다. 김 씨는 지난 겨울 방학 동안 두 자녀의 사교육비로 125만 원을 <span class="cn-word" data-pos="verb" data-tr="sarfladi">지출했으며</span> 이것은 월 소득의 40% 수준이다. <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">결국</span> 김 씨는 얼마 전부터 식당에서 아르바이트를 시작했다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)면서부터",
                "meaning":  "...ganidan boshlab: biror hodisa boshlangan paytdan buyon (koʻpincha oʻzgarish bilan).",
                "examples": ["아이들이 진학하면서부터 가계가 어려워졌다.", "그 일을 시작하면서부터 바빠졌어요."],
            },
            {
                "pattern":  "-짜리",
                "meaning":  "N-lik / N-baholi: narx, oʻlcham yoki daraja-toifani bildiradi.",
                "examples": ["중학교 3학년짜리 아들이 있다.", "만 원짜리 지폐."],
            },
        ],
        "questions": [
            {
                "text": "김 씨의 가계가 어려워지기 시작한 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "남편이 직장을 잃었기 때문에",
                    "아이들의 사교육비 때문에",
                    "집을 새로 샀기 때문에",
                ],
                "answer": 1,
                "explanation": "\"그 이유는 바로 사교육비 때문이었다\" — matn sababni toʻgʻridan-toʻgʻri aytadi. Er ishdan chiqqani yoki uy sotib olingani haqida gap yoʻq.",
            },
            {
                "text": "김 씨가 식당에서 아르바이트를 시작한 까닭으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "사교육비 부담으로 살림이 어려워졌기 때문에",
                    "새로운 일을 배우고 싶었기 때문에",
                    "아이들이 독립을 했기 때문에",
                ],
                "answer": 0,
                "explanation": "Xarajat oylik daromadning 40% ini yegach, oila qiynaladi va u ishga chiqadi. Sabab — moliyaviy bosim, qiziqish emas.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "삼계탕",
        "summary": "Samgyetang — tovuq, jenshen va boshqa dorivor masalliqlardan tayyorlanadigan koreyscha yozgi quvvat taomi.",
        "order":   8,
        "body": '''<p>삼계탕은 닭 한 마리를 <span class="cn-word" data-pos="adv" data-tr="butun holda">통째로</span> 인삼, 황기, 대추, 생강, 마늘 등의 재료와 함께 <span class="cn-word" data-pos="adv" data-tr="yaxshilab, qattiq">푹</span> <span class="cn-word" data-pos="verb" data-tr="qaynatib">삶아</span> 만든 한국의 <span class="cn-word" data-pos="adj" data-tr="asosiy, vakil boʻlgan">대표적인</span> 여름철 전통 보양 음식이다. 특히 삼복(초복, 중복, 말복)날에 많이 먹는 음식으로 각종 영양소가 <span class="cn-word" data-pos="adj" data-tr="boy, moʻl">풍부하고</span> 소화가 잘 되며 땀을 많이 흘려 기운이 없을 때 체력 증강에 좋다.</p>
<p>삼계탕에 들어가는 재료 중 인삼은 갈증을 <span class="cn-word" data-pos="verb" data-tr="yoʻqotib beradi">없애 주고</span> 피로회복을 도와주며 여름철 찬 것을 먹어 <span class="cn-word" data-pos="verb" data-tr="zaiflashgan">약해진</span> 위장의 기능을 <span class="cn-word" data-pos="verb" data-tr="toʻldirib beradi">보충해</span> 준다. 마늘은 기운을 보충해주며 모든 재료들의 독성을 없애 주는 <span class="cn-word" data-tr="foydali taʼsir">효능</span>이 있다. 찹쌀은 소화가 잘되는 음식으로 더위 때문에 약해진 위장의 기능을 도와준다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)며",
                "meaning":  "Sanash yoki bir vaqtda: ...ib, hamda. Yozma uslubda koʻp ishlatiladi.",
                "examples": ["영양소가 풍부하며 소화가 잘 된다.", "그는 학생이며 회사원이다."],
            },
            {
                "pattern":  "N 중(에서)",
                "meaning":  "...lar orasida / ichida: bir guruhdan birini ajratib koʻrsatadi.",
                "examples": ["재료 중 인삼이 가장 중요하다.", "친구들 중에서 그가 제일 크다."],
            },
        ],
        "questions": [
            {
                "text": "삼계탕에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "겨울에만 먹는 특별한 후식이다.",
                    "닭을 여러 재료와 함께 푹 삶아 만든 여름철 보양 음식이다.",
                    "고기를 넣지 않고 채소로만 끓인 음식이다.",
                ],
                "answer": 1,
                "explanation": "\"닭 한 마리를 통째로 ... 푹 삶아 만든 한국의 대표적인 여름철 전통 보양 음식\" — taʼrif aniq. Qishki desert yoki goʻshtsiz emas.",
            },
            {
                "text": "삼계탕에 들어가는 인삼의 효능으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "갈증을 없애 주고 피로 회복을 도와준다.",
                    "음식을 더 달게 만들어 준다.",
                    "고기의 색을 하얗게 만들어 준다.",
                ],
                "answer": 0,
                "explanation": "Matn: \"인삼은 갈증을 없애 주고 피로회복을 도와주며 ... 위장의 기능을 보충해 준다.\" Qolgan ikkitasi matnda yoʻq.",
            },
            {
                "text": "사람들이 삼복날 삼계탕을 즐겨 먹는 까닭으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "값이 아주 싸기 때문에",
                    "땀을 많이 흘려 약해진 기운과 체력을 보충하려고",
                    "다른 여름 음식이 없기 때문에",
                ],
                "answer": 1,
                "explanation": "\"땀을 많이 흘려 기운이 없을 때 체력 증강에 좋다\" — issiqda ketgan quvvatni tiklash uchun yeyiladi. Narx yoki muqobil taom yoʻqligi sabab emas.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "새로운 직업",
        "summary": "Kaskadyor oʻz kasbini nega tanlaganini va uni nima uchun sevishini soʻzlaydi.",
        "order":   9,
        "body": '''<p>스턴트맨인 나는 평소에도 몸을 움직이는 것을 좋아해서 운동을 <span class="cn-word" data-pos="verb" data-tr="zavq bilan qiladi">즐겨한다</span>. 어릴 때부터 <span class="cn-word" data-tr="aktyorlik, rol">연기</span>에도 관심이 있었기 때문에 몸으로 연기하는 스턴트맨을 직업으로 <span class="cn-word" data-pos="verb" data-tr="tanladim">선택했다</span>. 물론 많은 돈을 벌거나 <span class="cn-word" data-pos="adj" data-tr="barqaror">안정적인</span> 직업은 아니다. 하지만 <span class="cn-word" data-pos="adj" data-tr="xavfli">위험한</span> <span class="cn-word" data-tr="dublyorlik">대역</span> 연기를 성공했을 때 느끼는 <span class="cn-word" data-tr="qoniqish">만족감</span>과 배우들의 안전을 보장해 주었다는 <span class="cn-word" data-tr="qadr, mamnuniyat">보람</span> 같은 것이 늘 나를 <span class="cn-word" data-pos="verb" data-tr="maftun etadi">매료시킨다</span>. 그래서 나는 이 일이 좋고 앞으로도 계속 하고 싶다.</p>''',
        "grammar": [
            {
                "pattern":  "-다는 + 명사",
                "meaning":  "Koʻchirilgan gapni otga bogʻlaydi: ‘... degan’ (fikr, gap, tuygʻu).",
                "examples": ["안전을 지켜 주었다는 보람을 느낀다.", "시험에 합격했다는 소식을 들었다."],
            },
            {
                "pattern":  "-는 것(을)",
                "meaning":  "Feʼlni otga aylantiradi: ...ish(ni). ‘-는 것을 좋아하다/싫어하다’ shaklida koʻp keladi.",
                "examples": ["몸을 움직이는 것을 좋아한다.", "혼자 여행하는 것이 재미있어요."],
            },
        ],
        "questions": [
            {
                "text": "글쓴이가 스턴트맨을 직업으로 선택한 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "돈을 많이 벌 수 있고 안정적이기 때문에",
                    "어릴 때부터 몸을 움직이는 것과 연기를 좋아했기 때문에",
                    "부모님이 권했기 때문에",
                ],
                "answer": 1,
                "explanation": "Matn: \"평소에도 몸을 움직이는 것을 좋아해서\" va \"어릴 때부터 연기에도 관심이 있었기 때문에.\" Aksincha, u pul yoki barqarorlik uchun tanlamagan.",
            },
            {
                "text": "자신의 직업에 대한 글쓴이의 생각으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "돈은 많지 않지만 보람과 만족을 느껴 계속하고 싶다.",
                    "위험해서 곧 그만두려고 한다.",
                    "돈을 많이 벌어 만족스럽다.",
                ],
                "answer": 0,
                "explanation": "\"많은 돈을 벌거나 안정적인 직업은 아니다\" — lekin qoniqish va qadr uni maftun etadi, shuning uchun \"앞으로도 계속 하고 싶다\" deydi.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "미스터리 쇼퍼",
        "summary": "Sirli xaridor — mijoz qiyofasida doʻkonga borib, xizmat va sifatni baholab hisobot beradigan kishi.",
        "order":   10,
        "body": '''<p>기업에서는 모든 매장의 상황을 <span class="cn-word" data-pos="adv" data-tr="batafsil">자세히</span> 알기가 어렵기 때문에 <span class="cn-word" data-pos="adj" data-tr="xolis, obyektiv">객관적인</span> 입장에서 매장 상황을 <span class="cn-word" data-pos="verb" data-tr="aniqlab, tushunib">파악해서</span> 알려 줄 사람이 필요하다. 그래서 손님으로 <span class="cn-word" data-pos="verb" data-tr="oʻzini ...qilib koʻrsatib">가장하고</span> 매장을 <span class="cn-word" data-pos="verb" data-tr="tashrif buyurib">방문해서</span> 업무 효율성이나 <span class="cn-word" data-tr="xushmuomalalik darajasi">친절도</span>, 맛 등에 대해 <span class="cn-word" data-pos="verb" data-tr="baho qoʻyib">평점을 매겨</span> 직접 <span class="cn-word" data-pos="verb" data-tr="hisobot beradigan">보고하는</span> 일을 하는 사람이 있는데 이를 미스터리 쇼퍼라고 한다.</p>''',
        "grammar": [
            {
                "pattern":  "-기(가) 어렵다/쉽다",
                "meaning":  "Biror ishni qilish qiyin/oson ekanini bildiradi.",
                "examples": ["모든 매장을 자세히 알기가 어렵다.", "이 책은 읽기가 쉬워요."],
            },
            {
                "pattern":  "N을/를 N(이)라고 하다",
                "meaning":  "Taʼrif berish: ‘A ni B deyiladi / deb ataladi’.",
                "examples": ["이런 사람을 미스터리 쇼퍼라고 한다.", "이것을 김치라고 합니다."],
            },
        ],
        "questions": [
            {
                "text": "미스터리 쇼퍼가 하는 일로 알맞은 것은 무엇입니까?",
                "choices": [
                    "매장에서 직접 물건을 파는 일",
                    "손님으로 가장해 매장을 방문하고 평가해 보고하는 일",
                    "매장의 물건을 만드는 일",
                ],
                "answer": 1,
                "explanation": "\"손님으로 가장하고 매장을 방문해서 ... 평점을 매겨 직접 보고하는 일\" — mohiyati shu. Sotish yoki ishlab chiqarish emas.",
            },
            {
                "text": "기업이 미스터리 쇼퍼를 두는 까닭으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "매장의 물건값을 낮추기 위해서",
                    "직원 수를 줄이기 위해서",
                    "매장 상황을 객관적으로 파악하기 어렵기 때문에",
                ],
                "answer": 2,
                "explanation": "\"모든 매장의 상황을 자세히 알기가 어렵기 때문에 객관적인 입장에서 ... 알려 줄 사람이 필요하다\" — sabab shu. Narx yoki xodim soni haqida gap yoʻq.",
            },
        ],
    },
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "남성 패션과 미용",
        "summary": "Moda va parvarishga ayamay sarmoya kiritadigan erkaklar — teri, soch, tishdan tortib plastik jarrohlikkacha.",
        "order":   11,
        "body": '''<p>패션과 미용에 <span class="cn-word" data-pos="adv" data-tr="ayamasdan">아낌없이</span> <span class="cn-word" data-pos="verb" data-tr="sarmoya kiritadigan">투자하는</span> 남자들을 <span class="cn-word" data-pos="verb" data-tr="deb ataladigan">일컫는</span> 말이다. 이들은 자신을 <span class="cn-word" data-pos="verb" data-tr="koʻzga tashlanmoq, ajralib turmoq">돋보이도록</span> 하기 위해서 피부와 두발, 치아 <span class="cn-word" data-tr="parvarish">관리</span>는 물론 성형 수술까지도 한다. 인터넷 사이트에도 남성 회원들이 패션과 미용에 관한 정보를 <span class="cn-word" data-pos="verb" data-tr="almashadigan">교환하는</span> 동호회가 <span class="cn-word" data-pos="adv" data-tr="asta-sekin">점차</span> <span class="cn-word" data-pos="verb" data-tr="koʻpaymoqda">늘어나고</span> 있다.</p>''',
        "grammar": [
            {
                "pattern":  "-도록 하다",
                "meaning":  "Maqsad/natija: ...adigan qilib qilmoq, ... boʻlishi uchun harakat qilmoq.",
                "examples": ["자신을 돋보이도록 한다.", "잘 보이도록 글씨를 크게 썼어요."],
            },
            {
                "pattern":  "-은/는 물론(이고)",
                "meaning":  "...i tabiiy/aytmasa ham boʻladi, hatto ... ham: kutilganidan ortiqni qoʻshadi.",
                "examples": ["피부 관리는 물론 성형 수술까지 한다.", "주말은 물론 평일에도 바쁘다."],
            },
        ],
        "questions": [
            {
                "text": "이 글에서 설명하는 남자들의 특징으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "패션과 미용에 아낌없이 투자한다.",
                    "돈을 전혀 쓰지 않고 검소하게 산다.",
                    "외모에 관심이 없다.",
                ],
                "answer": 0,
                "explanation": "Birinchi jumla: \"패션과 미용에 아낌없이 투자하는 남자들.\" Qolgan variantlar bunga zid.",
            },
            {
                "text": "이런 남자들이 자신을 돋보이게 하려고 하는 일로 알맞은 것은 무엇입니까?",
                "choices": [
                    "피부·두발·치아 관리는 물론 성형 수술까지 하기도 한다.",
                    "운동만 하고 다른 것은 하지 않는다.",
                    "옷을 전혀 사지 않는다.",
                ],
                "answer": 0,
                "explanation": "\"피부와 두발, 치아 관리는 물론 성형 수술까지도 한다\" — matnda aniq sanab oʻtilgan.",
            },
        ],
    },
    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "광장의 변신",
        "summary": "Seul markazidagi maydonlar tushlik payti dam oladigan xizmatchilar uchun yangi maskanga aylanmoqda.",
        "order":   12,
        "body": '''<p>서울의 도심 휴식 문화가 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmoqda">달라지고</span> 있다. 시청 광장, 청계 광장, 광화문 광장에서 직장인들이 광장을 휴식 공간으로 <span class="cn-word" data-pos="verb" data-tr="bahramand boʻlmoqda">누리고</span> 있는 것이다. 광장에서 점심을 먹거나 동료들과 산책을 하면서 <span class="cn-word" data-tr="boʻsh, ortiqcha vaqt">자투리 시간</span>을 <span class="cn-word" data-pos="verb" data-tr="foydalanadigan">활용하는</span> 직장인들이 늘고 있다. 사막 속 오아시스를 보는 듯하다. 커피 전문점을 돌아다니거나 백화점 아이쇼핑, 대형 서점 들르기 등이 <span class="cn-word" data-tr="asosan boʻlgan">위주이던</span> 도심 여가 문화가 달라지고 있는 것이다.</p>
<p>여의도에 직장이 있는 이모(30)씨는 “회사원들의 점심 여가가 커피 전문점에서 차 한 잔 하거나 회사 건물 앞에서 담배를 피우는 정도였는데 광장을 산책하면서 피로를 풀다 보면 기분이 <span class="cn-word" data-pos="verb" data-tr="tetiklashadi">상쾌해진다</span>.”고 말했다. 또 다른 직장인 김모(27)씨는 “최근 동료들과 함께 도시락을 싸 와서 나눠 먹은 뒤 광화문 이곳저곳을 걸으며 <span class="cn-word" data-tr="bemalollik, huzur">여유</span>를 <span class="cn-word" data-pos="verb" data-tr="zavqlanmoq">즐긴다</span>”고 한다.</p>
<p>도심 직장인들의 점심 여가를 바꾼 광장, 앞으로도 더 많은 사람들의 사랑을 받기를 <span class="cn-word" data-pos="verb" data-tr="umid qilaman">기대해</span> 본다.</p>''',
        "grammar": [
            {
                "pattern":  "-다(가) 보면",
                "meaning":  "Bir ishni davom ettira borsang, tabiiy ravishda biror natijaga erishasan.",
                "examples": ["산책하며 피로를 풀다 보면 기분이 상쾌해진다.", "자꾸 듣다 보면 이해가 돼요."],
            },
            {
                "pattern":  "-(으)면서",
                "meaning":  "Bir vaqtning oʻzida ikki ishni qilish: ...a-...a, ...gan holda.",
                "examples": ["동료들과 산책을 하면서 시간을 보낸다.", "음악을 들으면서 공부해요."],
            },
        ],
        "questions": [
            {
                "text": "서울 도심 직장인들의 점심 여가가 어떻게 달라지고 있습니까?",
                "choices": [
                    "광장에서 산책하거나 도시락을 먹으며 시간을 보낸다.",
                    "점심시간에 모두 회사 안에서만 지낸다.",
                    "멀리 교외로 나가 등산을 한다.",
                ],
                "answer": 0,
                "explanation": "Matn maydonlarda sayr qilish, tushlik yeyish, hamkasblar bilan yurishni tasvirlaydi. Ofis ichida qolish yoki togʻga chiqish aytilmagan.",
            },
            {
                "text": "예전의 도심 여가 문화의 모습으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "광장에서 도시락을 먹는 것",
                    "커피 전문점을 돌아다니거나 백화점 아이쇼핑, 서점에 들르는 것",
                    "공원에서 운동을 하는 것",
                ],
                "answer": 1,
                "explanation": "\"커피 전문점을 돌아다니거나 백화점 아이쇼핑, 대형 서점 들르기 등이 위주이던 도심 여가 문화\" — bu aynan avvalgi holat.",
            },
            {
                "text": "이 글에 나타난 글쓴이의 태도로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "광장이 앞으로도 많은 사랑을 받기를 기대한다.",
                    "광장이 너무 붐벼서 불편하다고 느낀다.",
                    "직장인들이 점심을 거르는 것을 걱정한다.",
                ],
                "answer": 0,
                "explanation": "Oxirgi jumla: \"앞으로도 더 많은 사람들의 사랑을 받기를 기대해 본다\" — ijobiy, umidvor munosabat.",
            },
        ],
    },
    # ── 13 ───────────────────────────────────────────────────────────────
    {
        "title":   "기부한 사실, 주위에 알릴까 말까?",
        "summary": "Xayriya qilganini boshqalarga aytish kerakmi? Muallif oshkora aytish xayriya madaniyatini kengaytirishini asoslaydi.",
        "order":   13,
        "body": '''<p>기부 문화가 <span class="cn-word" data-pos="adv" data-tr="keng">널리</span> <span class="cn-word" data-pos="verb" data-tr="tarqalmoq">퍼지기</span> 위해서는 기부한 사실을 주위에 알려야 한다. 기부를 하지 않는 사람은 많은 사람들이 기부를 하고 있다는 것을 알면 <span class="cn-word" data-tr="ezgu ish">선행</span>을 <span class="cn-word" data-pos="verb" data-tr="koʻrsatmoq, qilmoq">베풀</span> 가능성이 높아지기 때문이다. 우리는 나 자신이 속해 있다고 인식하는 집단에서 다른 사람들이 하는 행동을 <span class="cn-word" data-pos="verb" data-tr="ergashib, taqlid qilmoq">따라 하는</span> <span class="cn-word" data-tr="moyillik, tendensiya">경향</span>이 있다.</p>
<p>한 연구 결과에 따르면 전화 모금을 할 때 다른 사람의 기부 액수를 들려주었을 경우 대다수의 사람들이 보통보다 많은 액수를 기부했다고 한다. 자신이 벌어들인 것에 비해 상당한 액수를 기부했음을 <span class="cn-word" data-pos="verb" data-tr="oshkor qilmoq">공개하는</span> 것은 다른 이들로 하여금 그렇게 하도록 <span class="cn-word" data-pos="verb" data-tr="undamoq, yoʻnaltirmoq">유도할</span> 수 있다.</p>
<p>순수한 마음에서 기부를 한 것인데 기부 사실을 주변에 알리면 그 뜻이 <span class="cn-word" data-pos="verb" data-tr="xiralashmoq, qadrini yoʻqotmoq">퇴색될까</span> 봐 <span class="cn-word" data-pos="verb" data-tr="ikkilanmoq">망설여지는가</span>? 이제는 숨기지 말자. 나눔 문화는 왼손이 하는 일을 오른손이 알게 해야 더 퍼질 수 있다.</p>''',
        "grammar": [
            {
                "pattern":  "-에 따르면",
                "meaning":  "Manbaga tayanish: ...ga koʻra / ...ning aytishicha (xabar, tadqiqot va h.k.).",
                "examples": ["한 연구 결과에 따르면 사람들이 더 많이 기부했다.", "일기 예보에 따르면 내일 비가 온다."],
            },
            {
                "pattern":  "-(으)ㄹ까 봐(서)",
                "meaning":  "Xavotir/qoʻrquv: ... boʻlib qolmasin deb, ...adi deb qoʻrqib.",
                "examples": ["뜻이 퇴색될까 봐 망설인다.", "늦을까 봐 뛰어갔어요."],
            },
        ],
        "questions": [
            {
                "text": "이 글에서 글쓴이가 말하고 싶은 것으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "기부는 반드시 큰 액수로 해야 한다.",
                    "기부한 사실을 주위에 알리는 것이 나눔 문화를 넓히는 데 도움이 된다.",
                    "기부는 아무도 모르게 조용히 하는 것이 가장 좋다.",
                ],
                "answer": 1,
                "explanation": "Muallif boshidan \"퍼지기 위해서는 기부한 사실을 주위에 알려야 한다\" deydi va oxirida \"이제는 숨기지 말자\" deb yakunlaydi. Uchinchi variant aynan uning fikriga zid.",
            },
            {
                "text": "전화 모금 연구 결과가 보여 주는 것으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "다른 사람의 기부 액수를 들으면 사람들이 더 많이 기부한다.",
                    "전화 모금은 효과가 전혀 없다.",
                    "사람들은 남의 기부에 관심이 없다.",
                ],
                "answer": 0,
                "explanation": "\"다른 사람의 기부 액수를 들려주었을 경우 대다수의 사람들이 보통보다 많은 액수를 기부했다\" — natija shu.",
            },
            {
                "text": "글쓴이가 “이제는 숨기지 말자”라고 말하는 까닭으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "기부한 사람을 자랑하기 위해서",
                    "기부 사실을 알리면 나눔 문화가 더 퍼질 수 있기 때문에",
                    "기부를 그만두게 하기 위해서",
                ],
                "answer": 1,
                "explanation": "Butun matnning mantigʻi: oshkora aytish boshqalarni ham xayriyaga undaydi va nashr madaniyatini kengaytiradi. Maqtanish yoki xayriyani toʻxtatish emas.",
            },
        ],
    },
    # ── 14 ───────────────────────────────────────────────────────────────
    {
        "title":   "춤을 추는 아이",
        "summary": "Rassom raqs tushayotgan bolani chizganini — kompozitsiya, nigoh va jonlilikni qanday ifodalaganini tushuntiradi.",
        "order":   14,
        "body": '''<p>저는 <span class="cn-word" data-tr="sozandalar">악사들</span>의 연주에 <span class="cn-word" data-pos="verb" data-tr="moslab, hamohang">맞춰</span> 춤을 추는 아이를 그려 봤습니다. 인물들을 둥글게 <span class="cn-word" data-pos="verb" data-tr="joylashtirib">배치해서</span> 그림에 <span class="cn-word" data-tr="barqarorlik hissi">안정감</span>을 주고 무동의 <span class="cn-word" data-tr="nigoh">시선</span>은 원 바깥으로 향하게 해서 감상자의 시선이 그림 바깥으로까지 <span class="cn-word" data-pos="verb" data-tr="kengaymoq">확대될</span> 수 있게 했습니다.</p>
<p>뭐니 뭐니 해도 가장 중요한 것은 무동이 실제로 춤을 추는 듯한 느낌이 들도록 하는 것이겠지요. 그래서 저는 무동의 옷 주름 굵기를 모두 다르게 <span class="cn-word" data-pos="verb" data-tr="ifodalab">표현하여</span> <span class="cn-word" data-tr="jonlilik">생동감</span>이 들도록 했어요. 참, 악사들의 표정도 자세히 보세요. 볼에 바람이 <span class="cn-word" data-pos="adv" data-tr="toʻla, liq">잔뜩</span> 들어가 있죠? 실제로 악기를 부는 것처럼 표현하기 위해서 그렇게 한 것입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-에 맞춰(서)",
                "meaning":  "...ga moslab / hamohang holda: biror narsaga muvofiqlashtirib.",
                "examples": ["악사들의 연주에 맞춰 춤을 춘다.", "음악에 맞춰 몸을 움직였다."],
            },
            {
                "pattern":  "-듯(이) / -듯한",
                "meaning":  "...gandek / goʻyo ...ayotgandek: oʻxshatish bildiradi.",
                "examples": ["실제로 춤을 추는 듯한 느낌이 든다.", "물 흐르듯이 말한다."],
            },
        ],
        "questions": [
            {
                "text": "글쓴이가 인물들을 둥글게 배치한 까닭으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "그림에 안정감을 주기 위해서",
                    "그림을 더 어둡게 만들기 위해서",
                    "인물 수를 줄이기 위해서",
                ],
                "answer": 0,
                "explanation": "\"인물들을 둥글게 배치해서 그림에 안정감을 주고\" — maqsad barqarorlik hissini berish.",
            },
            {
                "text": "글쓴이가 무동의 옷 주름 굵기를 모두 다르게 표현한 까닭으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "옷을 더 비싸 보이게 하려고",
                    "무동이 실제로 춤추는 듯한 생동감을 주려고",
                    "그림을 빨리 그리려고",
                ],
                "answer": 1,
                "explanation": "\"실제로 춤을 추는 듯한 느낌이 들도록 ... 옷 주름 굵기를 모두 다르게 표현하여 생동감이 들도록 했다\" — sabab jonlilik berish.",
            },
            {
                "text": "악사들의 볼에 바람이 잔뜩 들어간 표정으로 나타내려 한 것은 무엇입니까?",
                "choices": [
                    "악사들이 화가 난 모습",
                    "악사들이 실제로 악기를 부는 모습",
                    "악사들이 노래를 부르는 모습",
                ],
                "answer": 1,
                "explanation": "\"실제로 악기를 부는 것처럼 표현하기 위해서 그렇게 한 것\" — muallif aynan cholgʻu chalayotgan holatni koʻrsatmoqchi.",
            },
        ],
    },
]
