# Wonder Readings — stories 11-20 (Claude-authored, fun "wow-facts"). SAME collection as
# _stories_wonders_1_10.py, appended (orders 11-20). This batch is deliberately LIGHTER:
# easier vocabulary, shorter sentences, and only ~10 vocab marks per story (user asked for
# fewer/less hard words). Story text = Korean, all glosses = Uzbek. Style: STYLE_GUIDE_CORNER.md.
# Import: python manage.py import_corner corner/management/commands/_stories_wonders_11_20.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "세상의 신기한 이야기",
    "description": "Koinot, tabiat va dunyo haqidagi qiziqarli qisqa hikoyalar — lugʻat, grammatika va savollar bilan.",
    "order":       3,
}

STORIES = [
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "웃음은 전염된다",
        "summary": "Kimdir kulganda biz ham beixtiyor kulib yuboramiz — kulgi yuqadi, hamda sogʻliqqa foydali.",
        "order":   11,
        "body": '''<p>옆에서 누군가 크게 웃으면, 이유도 모르면서 나도 <span class="cn-word" data-pos="verb" data-tr="ergashib kulib qolamiz">따라 웃게</span> <strong>되는</strong> 경우가 있다. 웃음은 이렇게 쉽게 <span class="cn-word" data-pos="verb" data-tr="yuqadigan">전염되는</span> <span class="cn-word" data-pos="adj" data-tr="ajoyib, qiziq">신기한</span> 힘을 가지고 있다. 우리 <span class="cn-word" data-tr="miya">뇌</span>는 웃음소리를 들으면 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan, beixtiyor">저절로</span> 기분이 좋아지기 때문이다.</p>
<p>게다가 웃음은 건강에도 아주 좋다. 크게 웃으면 스트레스가 <span class="cn-word" data-pos="verb" data-tr="kamayadi">줄어들고</span> 심장도 <span class="cn-word" data-pos="verb" data-tr="mustahkamlanadi">튼튼해진다</span>고 한다. 그래서 ‘웃으면 <span class="cn-word" data-tr="baxt, omad">복</span>이 온다’는 옛말도 있다. 오늘 기분이 좋지 않다면, 그냥 한번 크게 웃어 보는 것은 어떨까? <strong>웃다 보면</strong> <span class="cn-word" data-pos="adv" data-tr="sezdirmay, allaqachon">어느새</span> 마음이 <span class="cn-word" data-pos="verb" data-tr="yengillashadi">가벼워질</span> 것이다.</p>''',
        "grammar": [
            {
                "pattern":  "-게 되다",
                "meaning":  "Oʻz ixtiyoridan tashqari natijada shunday boʻlib qolishni bildiradi: ...-b qolmoq.",
                "examples": ["나도 모르게 따라 웃게 된다.", "한국에 살면서 김치를 좋아하게 되었어요."],
            },
            {
                "pattern":  "-다(가) 보면",
                "meaning":  "Bir ishni davom ettira borsang, tabiiy ravishda biror natijaga erishasan.",
                "examples": ["웃다 보면 마음이 가벼워진다.", "자꾸 듣다 보면 이해가 돼요."],
            },
        ],
        "questions": [
            {
                "text": "옆 사람이 웃을 때 나도 따라 웃게 되는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "웃지 않으면 예의가 없다고 생각해서",
                    "뇌가 웃음소리를 들으면 저절로 기분이 좋아져서",
                    "웃음소리가 너무 시끄러워서",
                ],
                "answer": 1,
                "explanation": "Matnda miya kulgi ovozini eshitsa oʻz-oʻzidan kayfiyat koʻtarilib, birga kulgisi kelishi aytilgan.",
            },
            {
                "text": "웃음이 건강에 좋은 점으로 이 글에 나온 것은 무엇입니까?",
                "choices": [
                    "스트레스가 줄고 심장이 튼튼해진다.",
                    "키가 더 빨리 자란다.",
                    "눈이 좋아진다.",
                ],
                "answer": 0,
                "explanation": "Baland kulganda stress kamayib, yurak mustahkamlanishi matnda aytilgan.",
            },
            {
                "text": "이 글이 우리에게 하고 싶은 말은 무엇입니까?",
                "choices": [
                    "기분이 좋을 때만 웃어야 한다.",
                    "기분이 좋지 않을 때 크게 웃어 보면 마음이 가벼워진다.",
                    "다른 사람 앞에서는 웃지 않는 것이 좋다.",
                ],
                "answer": 1,
                "explanation": "Muallif kayfiyat yomon boʻlsa ham bir kulib koʻrishni taklif qiladi — kulsang koʻngil yengillashadi.",
            },
        ],
    },
    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "바다는 왜 짤까?",
        "summary": "Daryolar toshdagi tuzni eritib dengizga olib boradi, suv bugʻlanadi-yu tuz qoladi — shu sabab dengiz shoʻr.",
        "order":   12,
        "body": '''<p>바닷물은 왜 <span class="cn-word" data-pos="adj" data-tr="shoʻr">짤까</span>? 비가 내리면 빗물이 산과 땅을 지나 강으로 흐른다. 이때 물은 바위와 흙 속에 있는 아주 작은 <span class="cn-word" data-tr="tuz">소금</span>을 조금씩 <span class="cn-word" data-pos="verb" data-tr="eritib">녹여</span> 함께 <span class="cn-word" data-pos="verb" data-tr="oqib ketadi">흘러간다</span>. 그리고 이 강물은 <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">결국</span> 바다로 모인다.</p>
<p>바다에서는 햇빛 <strong>때문에</strong> 물이 <span class="cn-word" data-pos="verb" data-tr="bugʻlanadi">증발하지만</span>, 소금은 <span class="cn-word" data-pos="adv" data-tr="oʻsha holicha">그대로</span> 바다에 남는다. 물만 <span class="cn-word" data-pos="verb" data-tr="chiqib ketadi">빠져나가고</span> 소금은 계속 <span class="cn-word" data-pos="verb" data-tr="toʻplanib boradi">쌓이는</span> 것이다. 이런 일이 아주 <span class="cn-word" data-pos="adv" data-tr="uzoq vaqt">오랫동안</span> <strong><span class="cn-word" data-pos="verb" data-tr="takrorlangani sari">반복되면서</span></strong> 바다는 점점 짜게 되었다. 지금 이 순간에도 바다는 조금씩 더 짜지고 있다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)면서",
                "meaning":  "Bir vaqtda / ...gani sari (ikki holat birga yuz beradi yoki sabab boʻladi).",
                "examples": ["같은 일이 반복되면서 바다가 짜졌다.", "음악을 들으면서 공부해요."],
            },
            {
                "pattern":  "-기 때문에",
                "meaning":  "Sabab bildiradi: ... boʻlgani uchun.",
                "examples": ["햇빛 때문에 물이 증발하기 때문에 소금이 남는다.", "길이 막히기 때문에 지하철을 타요."],
            },
        ],
        "questions": [
            {
                "text": "강물이 바다로 소금을 가져오는 과정으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "빗물이 바위와 흙 속의 작은 소금을 녹여 강으로 흐른다.",
                    "사람들이 바다에 소금을 직접 뿌린다.",
                    "바닷속 물고기가 소금을 만든다.",
                ],
                "answer": 0,
                "explanation": "Yomgʻir suvi tosh va tuproqdagi mayda tuzni eritib daryoga olib tushadi, daryo esa dengizga quyiladi.",
            },
            {
                "text": "바닷물이 계속 짜지는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "물과 소금이 함께 증발하기 때문에",
                    "물은 증발해도 소금은 그대로 남아 쌓이기 때문에",
                    "비가 소금을 계속 내려 주기 때문에",
                ],
                "answer": 1,
                "explanation": "Quyosh taʼsirida suv bugʻlanadi, lekin tuz dengizda qoladi va toʻplanib boradi.",
            },
            {
                "text": "이 글의 내용과 같은 것을 고르십시오.",
                "choices": [
                    "바다는 옛날부터 지금까지 짠 정도가 똑같다.",
                    "바다는 점점 싱거워지고 있다.",
                    "바다는 지금도 조금씩 더 짜지고 있다.",
                ],
                "answer": 2,
                "explanation": "Matn oxirida hozir ham dengiz asta-sekin shoʻrroq boʻlib borayotgani aytilgan.",
            },
        ],
    },
    # ── 13 ───────────────────────────────────────────────────────────────
    {
        "title":   "소금이 돈이었던 시절",
        "summary": "Muzlatgich yoʻq davrda tuz oltinday qadrli edi — Rimda askarlarga maosh tuz bilan berilardi.",
        "order":   13,
        "body": '''<p><span class="cn-word" data-tr="muzlatgich">냉장고</span>가 없던 옛날에는 소금이 아주 <span class="cn-word" data-pos="adj" data-tr="qadrli, qimmatbaho">귀한</span> 물건이었다. 소금은 음식이 <span class="cn-word" data-pos="verb" data-tr="buzilmasligi uchun">상하지</span> <strong>않게</strong> 오래 <span class="cn-word" data-pos="verb" data-tr="saqlash">보관할</span> 수 있게 해 주었기 때문이다. 그래서 사람들은 소금을 <span class="cn-word" data-tr="oltin">금</span>처럼 <span class="cn-word" data-pos="adv" data-tr="qadrlab, eʼzozlab">소중하게</span> 여겼다.</p>
<p>심지어 옛날 로마에서는 <span class="cn-word" data-tr="askar, harbiy">군인</span>들에게 <span class="cn-word" data-tr="oylik maosh">월급</span>을 소금으로 <strong>주기도 했다</strong>. 영어로 월급을 뜻하는 ‘salary(샐러리)’라는 단어도 사실 소금을 뜻하는 말에서 <span class="cn-word" data-pos="verb" data-tr="kelib chiqqan">나왔다</span>. 지금은 값이 싸서 <span class="cn-word" data-pos="adj" data-tr="keng tarqalgan, arzon">흔한</span> 소금이지만, 옛날에는 돈만큼이나 <span class="cn-word" data-pos="adj" data-tr="qimmatli">귀중한</span> <span class="cn-word" data-tr="xazina, boylik">보물</span>이었던 셈이다.</p>''',
        "grammar": [
            {
                "pattern":  "-지 않게",
                "meaning":  "...maslik uchun, ...maydigan qilib (maqsad/holat).",
                "examples": ["음식이 상하지 않게 소금을 뿌렸다.", "잊어버리지 않게 메모를 했어요."],
            },
            {
                "pattern":  "-기도 하다",
                "meaning":  "Baʼzan/ham: goho ... ham qiladi/boʻladi (qoʻshimcha imkoniyat).",
                "examples": ["월급을 소금으로 주기도 했다.", "주말에는 집에서 쉬기도 해요."],
            },
        ],
        "questions": [
            {
                "text": "옛날에 소금이 귀했던 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "소금을 만드는 방법을 아무도 몰랐기 때문에",
                    "냉장고가 없어 소금으로 음식을 오래 보관했기 때문에",
                    "소금이 아주 멀리서만 났기 때문에",
                ],
                "answer": 1,
                "explanation": "Muzlatgich boʻlmagani uchun ovqatni uzoq saqlashda tuz ishlatilgan — shu sabab u qadrli edi.",
            },
            {
                "text": "옛날 로마와 소금에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "군인들에게 월급을 소금으로 주기도 했다.",
                    "소금을 먹는 것을 법으로 금지했다.",
                    "소금으로 집을 지었다.",
                ],
                "answer": 0,
                "explanation": "Rimda askarlarga baʼzan maosh oʻrniga tuz berilgani matnda aytilgan.",
            },
            {
                "text": "영어 단어 ‘salary’에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "‘군인’을 뜻하는 말에서 나왔다.",
                    "‘금’을 뜻하는 말에서 나왔다.",
                    "‘소금’을 뜻하는 말에서 나왔다.",
                ],
                "answer": 2,
                "explanation": "‘salary’ soʻzi aslida tuzni anglatuvchi soʻzdan kelib chiqqan.",
            },
        ],
    },
    # ── 14 ───────────────────────────────────────────────────────────────
    {
        "title":   "하루 종일 자는 고양이",
        "summary": "Mushuk kuniga 15 soatdan koʻp uxlaydi — ovchi ajdodlari kabi kuchini tejash uchun.",
        "order":   14,
        "body": '''<p>고양이는 <span class="cn-word" data-pos="adv" data-tr="kun boʻyi">하루 종일</span> 잠만 <strong>자는 것처럼 보인다</strong>. 실제로 고양이는 하루에 <span class="cn-word" data-pos="adv" data-tr="odatda">보통</span> 15시간 <span class="cn-word" data-pos="adv" data-tr="ortiq, koʻproq">넘게</span> 잔다. 이는 <span class="cn-word" data-tr="butun umr">평생</span>의 3분의 2를 자면서 <span class="cn-word" data-pos="verb" data-tr="oʻtkazadigan">보내는</span> 셈이다. 왜 이렇게 많이 잘까?</p>
<p>고양이의 <span class="cn-word" data-tr="ajdod">조상</span>은 <span class="cn-word" data-tr="yovvoyi tabiat">야생</span>에서 <span class="cn-word" data-tr="ov">사냥</span>을 하며 살았다. 사냥에는 많은 힘이 필요했기 때문에, 고양이는 <span class="cn-word" data-tr="odatdagi paytda">평소</span>에 잠을 자며 힘을 <span class="cn-word" data-pos="verb" data-tr="tejaydi, ayaydi">아낀다</span>. 그래서 자는 것처럼 <strong>보여도</strong> 작은 소리에 <span class="cn-word" data-pos="adv" data-tr="darrov, tez">금방</span> <span class="cn-word" data-pos="verb" data-tr="uygʻonadi">깨어난다</span>. 잘 자고 잘 노는 고양이가 사람들에게 사랑받는 이유가 아닐까?</p>''',
        "grammar": [
            {
                "pattern":  "-는 것처럼 보이다",
                "meaning":  "...ayotgandek koʻrinadi (aslida boshqacha boʻlishi mumkin).",
                "examples": ["고양이가 잠만 자는 것처럼 보인다.", "쉬운 것처럼 보이지만 사실 어려워요."],
            },
            {
                "pattern":  "-아/어도",
                "meaning":  "...sa ham (yon berish, qarama-qarshilik).",
                "examples": ["자는 것처럼 보여도 작은 소리에 금방 깬다.", "아무리 바빠도 밥은 먹어야 해요."],
            },
        ],
        "questions": [
            {
                "text": "고양이가 하루에 자는 시간으로 알맞은 것은 무엇입니까?",
                "choices": ["보통 5시간쯤 잔다.", "보통 15시간 넘게 잔다.", "거의 잠을 자지 않는다."],
                "answer": 1,
                "explanation": "Matnda mushuk kuniga odatda 15 soatdan koʻp uxlashi aytilgan.",
            },
            {
                "text": "고양이가 잠을 많이 자는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "사냥에 쓸 힘을 아끼기 위해서",
                    "밤이 무섭기 때문에",
                    "먹을 것이 없기 때문에",
                ],
                "answer": 0,
                "explanation": "Mushukning ovchi ajdodlari kabi, ovga kerak kuchni tejash uchun koʻp uxlaydi.",
            },
            {
                "text": "자는 것처럼 보여도 고양이가 금방 깨어나는 것에서 알 수 있는 것은 무엇입니까?",
                "choices": [
                    "완전히 깊이 잠들지 않고 작은 소리에도 바로 반응한다.",
                    "고양이는 사실 잠을 전혀 자지 않는다.",
                    "고양이는 소리를 잘 듣지 못한다.",
                ],
                "answer": 0,
                "explanation": "Kichik tovushga darrov uygʻonishi — mushuk juda chuqur uxlamay, ovozga tez javob berishini koʻrsatadi.",
            },
        ],
    },
    # ── 15 ───────────────────────────────────────────────────────────────
    {
        "title":   "하품은 왜 옮을까?",
        "summary": "Kimningdir esnashini koʻrsak, biz ham esnaymiz — olimlar buni hamdardlik bilan bogʻlaydi.",
        "order":   15,
        "body": '''<p>누군가 <span class="cn-word" data-tr="esnash">하품</span>을 하는 것을 보면, 나도 <span class="cn-word" data-pos="adv" data-tr="bilmagan holda, beixtiyor">모르게</span> 하품이 나온 경험이 있을 것이다. <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> 하품에 대한 글을 <strong>읽기만 해도</strong> 하품이 나오기도 한다. 지금 이 글을 읽는 당신도 <span class="cn-word" data-pos="adv" data-tr="ehtimol, balki">어쩌면</span> 하품을 하고 있을지 모른다.</p>
<p>하품이 이렇게 쉽게 <span class="cn-word" data-pos="verb" data-tr="yuqadigan, oʻtadigan">옮는</span> 이유는 무엇일까? 과학자들은 이것이 <span class="cn-word" data-tr="hamdardlik">공감</span>과 관련이 있다고 본다. 우리는 <span class="cn-word" data-pos="adj" data-tr="yaqin">가까운</span> <strong>사람일수록</strong> 그 사람의 행동을 <span class="cn-word" data-pos="verb" data-tr="taqlid qiladigan">따라 하는</span> <span class="cn-word" data-tr="moyillik">경향</span>이 있기 때문이다. 실제로 <span class="cn-word" data-pos="adj" data-tr="yaqin, ahil">친한</span> 사이일수록 하품이 더 잘 옮는다고 한다. 재미있는 우리 몸의 <span class="cn-word" data-tr="sir">비밀</span>이다.</p>''',
        "grammar": [
            {
                "pattern":  "-기만 해도",
                "meaning":  "Faqat ...ishning oʻzi bilanoq (kichik harakat ham yetarli).",
                "examples": ["하품에 대한 글을 읽기만 해도 하품이 나온다.", "이름만 들어도 기분이 좋아져요."],
            },
            {
                "pattern":  "-(으)ㄹ수록",
                "meaning":  "...gani sari, ...gani sayin (mutanosib oʻzgarish).",
                "examples": ["가까운 사람일수록 하품이 더 잘 옮는다.", "보면 볼수록 정이 들어요."],
            },
        ],
        "questions": [
            {
                "text": "이 글에 따르면 하품이 나오게 되는 경우로 알맞은 것은 무엇입니까?",
                "choices": [
                    "배가 많이 고플 때",
                    "남이 하품하는 것을 보거나 하품에 대한 글을 읽을 때",
                    "날씨가 아주 더울 때",
                ],
                "answer": 1,
                "explanation": "Matnda birovning esnashini koʻrganda yoki esnash haqidagi matnni oʻqiganda ham esnash kelishi aytilgan.",
            },
            {
                "text": "과학자들이 말하는, 하품이 옮는 이유는 무엇입니까?",
                "choices": [
                    "공감과 관련이 있어 가까운 사람의 행동을 따라 하기 때문에",
                    "하품이 병처럼 몸에 옮기 때문에",
                    "하품을 참으면 건강에 나쁘기 때문에",
                ],
                "answer": 0,
                "explanation": "Olimlar esnash hamdardlik bilan bogʻliq boʻlib, yaqin kishining harakatiga taqlid qilinishini aytadi.",
            },
            {
                "text": "하품이 더 잘 옮는 관계로 알맞은 것은 무엇입니까?",
                "choices": ["서로 처음 만난 사이", "서로 친하고 가까운 사이", "서로 사이가 나쁜 사이"],
                "answer": 1,
                "explanation": "Matnda ahil va yaqin kishilar orasida esnash yaxshiroq yuqishi aytilgan.",
            },
        ],
    },
    # ── 16 ───────────────────────────────────────────────────────────────
    {
        "title":   "눈송이는 모두 다르다",
        "summary": "Har bir qor uchqunida oltita shox bor, ammo bir xil boʻlgan ikkitasi yoʻq.",
        "order":   16,
        "body": '''<p>겨울 하늘에서 내리는 <span class="cn-word" data-tr="qor uchquni">눈송이</span>를 <span class="cn-word" data-pos="adv" data-tr="diqqat bilan, sinchiklab">자세히</span> <strong>본 적이 있는가</strong>? 모든 눈송이는 여섯 개의 가지를 가진 <span class="cn-word" data-pos="adj" data-tr="goʻzal">아름다운</span> 모양이다. 그런데 <span class="cn-word" data-pos="adv" data-tr="hayratlanarlisi shundaki">놀랍게도</span> <span class="cn-word" data-pos="adj" data-tr="bir xil, aynan oʻxshash">똑같은</span> 눈송이는 하나도 없다.</p>
<p>눈송이는 구름 속에서 만들어져 땅으로 <span class="cn-word" data-pos="verb" data-tr="tushadi">떨어진다</span>. 이때 지나가는 길의 <span class="cn-word" data-tr="harorat">온도</span>가 <span class="cn-word" data-pos="adv" data-tr="ozgina, asta-sekin">조금씩</span> 다르기 때문에, <strong>눈송이마다</strong> 서로 다른 모양으로 <span class="cn-word" data-pos="verb" data-tr="oʻsadi, shakllanadi">자란다</span>. 매년 <span class="cn-word" data-pos="adj" data-tr="son-sanoqsiz">수많은</span> 눈송이가 내리지만, 그중 똑같은 것은 단 하나도 없는 셈이다. 눈이 오는 날, 눈송이 하나를 <span class="cn-word" data-pos="adv" data-tr="jimgina, eʼtibor bilan">가만히</span> 들여다보는 것은 어떨까?</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄴ 적이 있다",
                "meaning":  "Oʻtmishdagi tajriba: bir ishni qilib koʻrgan/boshidan oʻtkazganini bildiradi.",
                "examples": ["눈송이를 자세히 본 적이 있는가?", "제주도에 가 본 적이 있어요?"],
            },
            {
                "pattern":  "-마다",
                "meaning":  "Har bir ...: har bittasi, har gal (istisnosiz hammasi).",
                "examples": ["눈송이마다 모양이 다르다.", "사람마다 성격이 달라요."],
            },
        ],
        "questions": [
            {
                "text": "모든 눈송이의 공통점으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "여섯 개의 가지를 가진 모양이다.",
                    "모두 완전히 둥근 모양이다.",
                    "크기가 모두 똑같다.",
                ],
                "answer": 0,
                "explanation": "Matnda har bir qor uchquni oltita shoxli shaklga ega ekani aytilgan.",
            },
            {
                "text": "눈송이가 서로 다른 모양이 되는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "떨어지는 길의 온도가 조금씩 다르기 때문에",
                    "사람들이 눈송이를 손으로 만들기 때문에",
                    "눈송이가 색깔이 다르기 때문에",
                ],
                "answer": 0,
                "explanation": "Qor uchquni tushayotgan yoʻlidagi harorat biroz farq qilgani uchun har biri boshqacha shakl oladi.",
            },
            {
                "text": "이 글의 중심 내용으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "눈송이는 모두 여섯 가지 모양이지만 똑같은 것은 하나도 없다.",
                    "눈송이는 모두 크기와 모양이 똑같다.",
                    "눈송이는 땅에 닿으면 색깔이 변한다.",
                ],
                "answer": 0,
                "explanation": "Barcha qor uchqunlari oltita shoxli, biroq bir xil boʻlgani yoʻq — bu matnning asosiy gʻoyasi.",
            },
        ],
    },
    # ── 17 ───────────────────────────────────────────────────────────────
    {
        "title":   "달의 뒷면",
        "summary": "Oy Yer atrofida aylanar ekan xuddi shu tezlikda oʻqi atrofida ham aylanadi — shu sabab bizga doim bir tomoni koʻrinadi.",
        "order":   17,
        "body": '''<p>밤하늘의 달을 볼 때, 우리는 <span class="cn-word" data-pos="adv" data-tr="doim, hamisha">항상</span> 달의 같은 면만 <strong>보게 된다</strong>. 달의 <span class="cn-word" data-tr="orqa tomon">뒷면</span>은 지구에서 <span class="cn-word" data-pos="adv" data-tr="aslo, hech qachon">절대</span> 보이지 않는다. 왜 그럴까?</p>
<p>달은 지구 주위를 <span class="cn-word" data-pos="verb" data-tr="aylanadigan">도는</span> <strong>동안</strong>, 스스로도 <span class="cn-word" data-pos="adv" data-tr="sekin, astalik bilan">천천히</span> 돈다. 그런데 그 <span class="cn-word" data-tr="tezlik">속도</span>가 <span class="cn-word" data-pos="adv" data-tr="roppa-rosa, aynan">딱</span> 맞아떨어져서, 언제나 같은 면만 지구를 <span class="cn-word" data-pos="verb" data-tr="qaratadi, yuz tutadi">향하게</span> 된다. 그래서 사람들은 <span class="cn-word" data-pos="adv" data-tr="uzoq vaqt">오랫동안</span> 달의 뒷면을 볼 수 없었다. <span class="cn-word" data-tr="kosmik kema">우주선</span>이 처음 <span class="cn-word" data-pos="verb" data-tr="suratga olgan">찍은</span> 달의 뒷면은 앞면과 <span class="cn-word" data-pos="adv" data-tr="ancha, birmuncha">꽤</span> 다른 모습이었다고 한다.</p>''',
        "grammar": [
            {
                "pattern":  "-는 동안",
                "meaning":  "...ayotgan vaqt davomida, ...gan paytda.",
                "examples": ["달은 지구를 도는 동안 스스로도 돈다.", "제가 자는 동안 비가 왔어요."],
            },
            {
                "pattern":  "-게 되다",
                "meaning":  "Tabiiy ravishda yoki natijada shunday boʻlib qolish: ...-b qolmoq.",
                "examples": ["언제나 같은 면만 지구를 향하게 된다.", "결국 진실을 알게 되었어요."],
            },
        ],
        "questions": [
            {
                "text": "우리가 지구에서 항상 달의 같은 면만 보게 되는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "달이 전혀 돌지 않기 때문에",
                    "달이 지구를 도는 속도와 스스로 도는 속도가 딱 맞기 때문에",
                    "달이 너무 빨리 돌기 때문에",
                ],
                "answer": 1,
                "explanation": "Oyning Yer atrofida va oʻz oʻqi atrofida aylanish tezligi mos kelgani uchun doim bir tomoni koʻrinadi.",
            },
            {
                "text": "사람들이 오랫동안 달의 뒷면을 볼 수 없었던 이유는 무엇입니까?",
                "choices": [
                    "달의 뒷면이 지구에서 절대 보이지 않기 때문에",
                    "달의 뒷면에 빛이 전혀 없기 때문에",
                    "달의 뒷면이 너무 작기 때문에",
                ],
                "answer": 0,
                "explanation": "Oyning orqa tomoni Yerdan aslo koʻrinmaydi, shuning uchun uni uzoq vaqt koʻra olishmagan.",
            },
            {
                "text": "우주선이 처음 찍은 달의 뒷면에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "앞면과 완전히 똑같았다.",
                    "앞면과 꽤 다른 모습이었다.",
                    "아무것도 찍히지 않았다.",
                ],
                "answer": 1,
                "explanation": "Kosmik kema suratga olgan orqa tomon old tomondan ancha farq qilgani aytilgan.",
            },
        ],
    },
    # ── 18 ───────────────────────────────────────────────────────────────
    {
        "title":   "개미의 놀라운 힘",
        "summary": "Chumoli oʻz vaznidan 50 barobar ogʻirni koʻtaradi, birgalikda katta yuk tashiydi va hiddan uyini topadi.",
        "order":   18,
        "body": '''<p>개미는 <span class="cn-word" data-pos="adj" data-tr="kichkina boʻlsa-da">작지만</span> <span class="cn-word" data-pos="adj" data-tr="juda katta">엄청난</span> 힘을 가진 <span class="cn-word" data-tr="hasharot">곤충</span>이다. 개미는 자기 <span class="cn-word" data-tr="tana vazni">몸무게</span>보다 <span class="cn-word" data-pos="adv" data-tr="naq, hatto">무려</span> <strong>50배나</strong> <span class="cn-word" data-pos="adj" data-tr="ogʻir">무거운</span> 것을 들 수 있다. 이것은 사람이 자동차를 번쩍 드는 것과 같다.</p>
<p>게다가 개미는 혼자 힘들면 <span class="cn-word" data-pos="adv" data-tr="bir nechtasi birga">여럿이</span> 함께 <span class="cn-word" data-pos="verb" data-tr="kuch birlashtirib">힘을 모아</span> 큰 먹이를 <span class="cn-word" data-pos="verb" data-tr="tashiydi, koʻchiradi">옮긴다</span>. 또 아무리 멀리 <strong><span class="cn-word" data-pos="verb" data-tr="ketsa ham">가더라도</span></strong> 냄새를 <span class="cn-word" data-pos="verb" data-tr="izidan borib">따라</span> 집을 <span class="cn-word" data-pos="adv" data-tr="aniq">정확히</span> 찾아온다. 작은 개미에게 이렇게 놀라운 <span class="cn-word" data-tr="qobiliyat">능력</span>이 숨어 있다니, 정말 대단하지 않은가?</p>''',
        "grammar": [
            {
                "pattern":  "-(이)나",
                "meaning":  "Kutilganidan koʻp ekaniga urgʻu: naq ..., ...cha (koʻplikni taʼkidlaydi).",
                "examples": ["몸무게보다 50배나 무거운 것을 든다.", "그 책을 세 번이나 읽었어요."],
            },
            {
                "pattern":  "-더라도",
                "meaning":  "...boʻlsa ham (kuchli yon berish, koʻpincha faraziy).",
                "examples": ["아무리 멀리 가더라도 집을 찾아온다.", "힘들더라도 포기하지 마세요."],
            },
        ],
        "questions": [
            {
                "text": "개미의 힘에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "자기 몸무게보다 50배 무거운 것도 들 수 있다.",
                    "자기 몸무게만큼만 들 수 있다.",
                    "아무것도 들지 못한다.",
                ],
                "answer": 0,
                "explanation": "Matnda chumoli oʻz vaznidan 50 barobar ogʻir narsani koʻtara olishi aytilgan.",
            },
            {
                "text": "개미가 큰 먹이를 옮기는 방법으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "여럿이 함께 힘을 모아 옮긴다.",
                    "먹이를 잘게 부숴서 옮긴다.",
                    "다른 동물에게 부탁한다.",
                ],
                "answer": 0,
                "explanation": "Chumolilar yolgʻiz ogʻirlik qilsa, bir nechtasi birlashib katta yemni koʻchiradi.",
            },
            {
                "text": "개미가 멀리 갔다가도 집을 정확히 찾아오는 방법은 무엇입니까?",
                "choices": ["냄새를 따라 찾아온다.", "소리를 듣고 찾아온다.", "다른 개미가 데리러 온다."],
                "answer": 0,
                "explanation": "Chumoli qanchalik uzoqqa ketsa ham hid izidan uyini aniq topib keladi.",
            },
        ],
    },
    # ── 19 ───────────────────────────────────────────────────────────────
    {
        "title":   "바나나는 나무가 아니다",
        "summary": "Banan ‘daraxti’ aslida daraxt emas — yogʻoch poyasi yoʻq, u dunyodagi eng katta ‘oʻt’.",
        "order":   19,
        "body": '''<p>우리는 바나나가 나무에서 <span class="cn-word" data-pos="verb" data-tr="oʻsadi">자란다</span>고 생각한다. 하지만 <span class="cn-word" data-pos="adv" data-tr="aslida">사실</span> 바나나 나무는 진짜 나무가 아니다. <span class="cn-word" data-pos="adj" data-tr="qattiq">단단한</span> <span class="cn-word" data-tr="poya">줄기</span>가 없고, <span class="cn-word" data-tr="oʻt, oʻsimlik">풀</span>처럼 <span class="cn-word" data-pos="adj" data-tr="yumshoq">부드럽기</span> 때문이다. 즉, 바나나는 세상에서 가장 큰 ‘풀’에서 자라는 <span class="cn-word" data-tr="meva">열매</span>인 <strong>셈이다</strong>.</p>
<p>더 재미있는 사실도 있다. 바나나는 아래로 <span class="cn-word" data-pos="verb" data-tr="osilib">매달려</span> 있지만, 자랄 때는 햇빛을 향해 위로 <span class="cn-word" data-pos="verb" data-tr="egilib, qiyshayib">휘어지며</span> 자란다. 그래서 바나나는 그 <span class="cn-word" data-pos="adj" data-tr="oʻziga xos">독특한</span> 모양을 갖게 된 것이다. 매일 먹는 바나나에도 이런 <span class="cn-word" data-pos="verb" data-tr="yashiringan">숨은</span> 이야기가 <strong>있다니</strong> 신기하지 않은가?</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄴ/는 셈이다",
                "meaning":  "Xulosa/hisob-kitob: aslida ... boʻlib chiqadi, demak ... degani.",
                "examples": ["바나나는 큰 풀에서 자라는 열매인 셈이다.", "이 정도면 다 배운 셈이에요."],
            },
            {
                "pattern":  "-다니",
                "meaning":  "Hayrat/taajjub: ...ekan-a!, ... deganingmi? (kutilmagan narsaga hayrat).",
                "examples": ["바나나에 이런 이야기가 있다니 신기하다.", "벌써 다 끝났다니 놀랍네요."],
            },
        ],
        "questions": [
            {
                "text": "바나나 나무가 진짜 나무가 아닌 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "단단한 줄기가 없고 풀처럼 부드럽기 때문에",
                    "키가 아주 작기 때문에",
                    "열매를 맺지 않기 때문에",
                ],
                "answer": 0,
                "explanation": "Banan ‘daraxti’da qattiq yogʻoch poya yoʻq, u oʻtga oʻxshab yumshoq — shu sabab u daraxt emas.",
            },
            {
                "text": "바나나의 모양에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "햇빛을 향해 위로 휘어지며 자라서 독특한 모양이 된다.",
                    "땅속에서 곧게 자란다.",
                    "처음부터 완전히 둥근 모양이다.",
                ],
                "answer": 0,
                "explanation": "Banan pastga osilsa-da, oʻsayotganda quyoshga qarab yuqoriga egilib oʻsadi va shu sabab oʻziga xos shaklga ega boʻladi.",
            },
            {
                "text": "이 글의 내용과 같은 것을 고르십시오.",
                "choices": [
                    "바나나는 사실 아주 큰 풀에서 자라는 열매다.",
                    "바나나는 아주 단단한 나무에서 자란다.",
                    "바나나는 땅속에서 자라는 뿌리다.",
                ],
                "answer": 0,
                "explanation": "Matnda banan dunyodagi eng katta ‘oʻt’da oʻsadigan meva ekani aytilgan.",
            },
        ],
    },
    # ── 20 ───────────────────────────────────────────────────────────────
    {
        "title":   "나무들의 대화",
        "summary": "Oʻrmondagi daraxtlar ildizlari orqali bogʻlangan — ozuqani boʻlishadi va xavf haqida bir-birini ogohlantiradi.",
        "order":   20,
        "body": '''<p><span class="cn-word" data-tr="oʻrmon">숲</span>속의 나무들은 <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> 서 있는 것처럼 보이지만, 사실은 땅속에서 서로 <span class="cn-word" data-pos="verb" data-tr="bogʻlangan">연결되어</span> 있다. 나무들은 <span class="cn-word" data-tr="ildiz">뿌리</span>와 아주 작은 <span class="cn-word" data-tr="qoʻziqorin">버섯</span>을 통해 마치 대화를 <strong><span class="cn-word" data-pos="verb" data-tr="ulashayotgandek">나누듯</span></strong> 서로 도움을 주고받는다.</p>
<p>예를 들어, <span class="cn-word" data-pos="adj" data-tr="sogʻlom">건강한</span> 나무는 <span class="cn-word" data-pos="adj" data-tr="zaif">약한</span> 나무에게 <span class="cn-word" data-tr="ozuqa, oziq modda">양분</span>을 나누어 준다. 또 <span class="cn-word" data-tr="hasharot, qurt">벌레</span>가 <span class="cn-word" data-pos="verb" data-tr="hujum qilsa">공격하면</span>, 위험을 알리는 <span class="cn-word" data-tr="signal, ishora">신호</span>를 다른 나무들에게 <strong>보내기도 한다</strong>. 그래서 하나의 숲은 서로 돕는 커다란 가족과 같다. 말없이 서 있는 나무들이 사실은 이렇게 <span class="cn-word" data-pos="verb" data-tr="muloqot qilayotgan">소통하고</span> 있었던 것이다.</p>''',
        "grammar": [
            {
                "pattern":  "-듯(이)",
                "meaning":  "...gandek, xuddi ...ayotgandek (oʻxshatish).",
                "examples": ["나무들이 대화를 나누듯 도움을 주고받는다.", "물 흐르듯이 자연스럽게 말한다."],
            },
            {
                "pattern":  "-기도 하다",
                "meaning":  "Baʼzan/ham: goho ... ham qiladi/boʻladi (qoʻshimcha holat).",
                "examples": ["위험을 알리는 신호를 보내기도 한다.", "가끔 혼자 여행을 하기도 해요."],
            },
        ],
        "questions": [
            {
                "text": "숲속 나무들이 서로 연결되는 방법으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "뿌리와 아주 작은 버섯을 통해 연결된다.",
                    "바람을 통해 소리로 연결된다.",
                    "잎을 서로 붙여서 연결된다.",
                ],
                "answer": 0,
                "explanation": "Daraxtlar ildizlari va juda mayda qoʻziqorinlar orqali bir-biriga bogʻlanadi.",
            },
            {
                "text": "건강한 나무가 약한 나무를 돕는 방법으로 이 글에 나온 것은 무엇입니까?",
                "choices": ["양분을 나누어 준다.", "물을 대신 마셔 준다.", "약한 나무를 옮겨 준다."],
                "answer": 0,
                "explanation": "Sogʻlom daraxt zaif daraxtga oziq moddalarni boʻlib beradi.",
            },
            {
                "text": "이 글에서 하나의 숲을 무엇에 비유했습니까?",
                "choices": ["서로 돕는 커다란 가족", "조용한 도서관", "바쁜 시장"],
                "answer": 0,
                "explanation": "Matnda oʻrmon bir-biriga yordam beradigan katta oilaga qiyoslangan.",
            },
        ],
    },
]
