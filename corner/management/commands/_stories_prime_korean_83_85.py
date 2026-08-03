# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-83 … PK-85 (뿐/따름/불과, 든지 든지, 느니/나 마나).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 da gaplashadi.
Mavzu — 인생 이야기 va 정보문 navbatma-navbat:
  83 — 인생 이야기: oʻn ikki yil davomida uch soniya
  84 — 정보문: qaysi tilni oʻrgansangiz ham, uchta narsa bir xil
  85 — 인생 이야기: hamma ketgan togʻ qishlogʻida qolgan odam

Kumulyativ qoida: PK-85 gacha oʻrganilgan hamma narsa ochiq.
PK-83 matnida 든지/건 (84) va 느니/나 마나 (85) YOʻQ.
PK-84 matnida 느니 차라리 / (으)나 마나 (85) yoʻq.
(으)ㅁ으로써 (86), (으)ㄹ 지경이다 (87), (으)ㄹ 리가 없다 (88),
에 달려 있다 (89), (으)려던 참 (90) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다 —
oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_83_85.py --author=prime
"""

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Prime Korean Readings",
    "description": (
        "Prime Korean darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order": 2,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PK-83 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "삼 초",
        "summary": (
            "PK-83 matni. Avtobus haydovchisining hech kim bilmagan "
            "qoidasi: baʼzi yoʻlovchilar uchun eshikni uch soniya "
            "kechroq yopish. Oʻn ikki yildan keyin hisob."
        ),
        "order":   83,
        "grammar": [
            {
                "pattern":  "(으)ㄹ 뿐이다 — faqat …, xolos",
                "meaning":  "“Bundan ortigʻi yoʻq.” Kamtarlik va oqlanish "
                            "ohangi. Ot bilan 일 뿐이다, oʻtgan ish bilan "
                            "았/었을 뿐이다.",
                "examples": ["저는 제 일을 했을 뿐입니다.",
                             "작은 일은 작은 일일 뿐이다."],
            },
            {
                "pattern":  "(으)ㄹ 따름이다 — kitobiy “xolos”",
                "meaning":  "뿐이다 bilan bir xil maʼno, lekin rasmiy "
                            "yozma uslub va koʻpincha his-tuygʻu haqida. "
                            "Shu matnda u rasmiy marosimda aytiladi.",
                "examples": ["이렇게 많은 분이 와서 감사할 따름입니다."],
            },
            {
                "pattern":  "명사 + 에 불과하다 — bor-yoʻgʻi …",
                "meaning":  "Otga qoʻshiladi va baho beradi. Raqam bilan "
                            "juda koʻp ishlatiladi — matnning oxiridagi "
                            "hisob aynan shunga qurilgan.",
                "examples": ["그것은 규칙에 불과했다.",
                             "숫자로 보면 아주 작은 시간에 불과하다."],
            },
        ],
        "body": '''<p>김 <span class="cn-word" data-tr="haydovchi">기사</span>는 십이 년 동안 같은 <span class="cn-word" data-tr="marshrut">노선</span>을 운전했다. 아침 다섯 시 사십 분에 <span class="cn-word" data-tr="birinchi reys">첫차</span>가 출발한다. 마지막 차는 밤 열한 시에 들어온다.</p>

<p>그의 버스에는 <span class="cn-word" data-tr="qoida">규칙</span>이 하나 있었다. 아무도 몰랐다. 김 기사만 알았다.</p>

<p>그는 매일 타는 사람들을 기억했다. 그리고 그중 몇 사람에게는 문을 삼 <span class="cn-word" data-tr="soniya">초</span> 더 늦게 닫았다.</p>

<p>다리가 <span class="cn-word" data-pos="adj" data-tr="ogʻriydigan, noqulay">불편한</span> 할머니. <span class="cn-word" data-tr="yuk">짐</span>이 많은 시장 아주머니. <span class="cn-word" data-tr="hassa, tayanch">목발</span>을 쓰는 고등학생.</p>

<p>삼 초. <span class="cn-word" data-pos="adv" data-tr="shundan boshqa hech narsa emas edi">그것뿐이었다</span>.</p>

<p>다른 기사들은 <span class="cn-word" data-tr="jadval">시간표</span>를 지켰다. 그것은 <span class="cn-word" data-tr="xato, ayb">잘못</span>이 아니다. <span class="cn-word" data-pos="adv" data-tr="qoidadan iborat edi, xolos">규칙에 불과했다</span>. 김 기사도 시간표를 지켰다. <span class="cn-word" data-pos="adv" data-tr="faqat, biroq">다만</span> 그 삼 초를 <span class="cn-word" data-pos="adv" data-tr="qayerdadir">어디선가</span> 다시 찾았다.</p>

<p>십이 년 후, 김 기사가 <span class="cn-word" data-pos="verb" data-tr="nafaqaga chiqdi">퇴직했다</span>.</p>

<p>회사는 작은 <span class="cn-word" data-tr="xayrlashuv marosimi">인사 자리</span>를 만들었다. 사무실에 의자를 열 개 놓았다. 그날 이백 명이 왔다.</p>

<p>목발을 쓰던 학생은 이제 스물여덟 살이었다. 회사원이 <span class="cn-word" data-pos="verb" data-tr="boʻlib ulgurgan edi">되어 있었다</span>. 시장 아주머니는 편지를 읽었다. 손이 <span class="cn-word" data-pos="verb" data-tr="titradi">떨렸다</span>. “기사님은 매일 우리를 <span class="cn-word" data-pos="verb" data-tr="kutib turardi">기다려 줬어요</span>.”</p>

<p>사람들은 “<span class="cn-word" data-pos="adj" data-tr="ajoyib">대단하다</span>”고 했다. 신문에도 작은 <span class="cn-word" data-tr="maqola">기사</span>가 나왔다.</p>

<p>김 기사는 그날 짧게 말했다. “저는 제 일을 <span class="cn-word" data-pos="verb" data-tr="qildim, xolos">했을 뿐입니다</span>. 문을 조금 늦게 닫았을 뿐이에요.”</p>

<p>그리고 이렇게 <span class="cn-word" data-pos="verb" data-tr="qoʻshib qoʻydi">덧붙였다</span>. “이렇게 많은 분이 와서 <span class="cn-word" data-pos="verb" data-tr="minnatdorman, xolos">감사할 따름입니다</span>.”</p>

<p>집에 돌아온 김 기사는 <span class="cn-word" data-tr="hisob">계산</span>을 해 봤다. 하루에 삼 초씩, 열 명. 십이 년. 약 삼십 시간이었다.</p>

<p>삼십 시간은 긴 시간이 아니다. <span class="cn-word" data-tr="uch kun">사흘</span>도 되지 않는다. 숫자로 보면 아주 작은 시간에 불과하다.</p>

<p>그러나 그 삼십 시간 안에 이백 명의 하루가 들어 있었다.</p>

<p>작은 일은 작은 일일 뿐이다. 그것이 십이 년 동안 <span class="cn-word" data-pos="verb" data-tr="takrorlanmaguncha">반복되기 전까지는</span>.</p>''',
        "questions": [
            {
                "text": "Kim haydovchining hech kim bilmagan qoidasi nima "
                        "edi?",
                "choices": [
                    "Har doim jadvaldan oldin yurish",
                    "Baʼzi yoʻlovchilar uchun eshikni uch soniya kechroq "
                    "yopish",
                    "Har kuni bir xil marshrutda yurish",
                    "Yoʻlovchilarga chipta bermaslik",
                ],
                "answer": 1,
                "explanation": "Oyogʻi ogʻriydigan kampir, yuki koʻp "
                               "bozorchi ayol, hassali oʻquvchi — "
                               "faqat ular uchun uch soniya.",
            },
            {
                "text": "“저는 제 일을 했을 뿐입니다” — u nima demoqchi?",
                "choices": [
                    "U ishini yaxshi bajarmadi",
                    "U boshqa hech narsa qilmadi — bu maqtovga arzimaydi",
                    "U ishni yoqtirmasdi",
                    "U boshqa ish qidiryapti",
                ],
                "answer": 1,
                "explanation": "(으)ㄹ 뿐이다 — <b>kamaytirish</b> ohangi. "
                               "“Bundan ortigʻini qilmadim” degani.",
            },
            {
                "text": "Matnning oxirgi hisobi nimani koʻrsatadi?",
                "choices": [
                    "Oʻttiz soat raqam sifatida juda kichik — lekin "
                    "uning ichida ikki yuz kishining kuni bor",
                    "Uch soniya hech qanday ahamiyatga ega emas",
                    "Haydovchi juda koʻp vaqt yoʻqotgan",
                    "Kompaniya zarar koʻrgan",
                ],
                "answer": 0,
                "explanation": "“작은 시간<b>에 불과하다</b>” bilan “그 삼십 "
                               "시간 안에 이백 명의 하루가 들어 있었다” "
                               "yonma-yon turadi — matnning butun fikri "
                               "shu qarama-qarshilikda.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-84 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "어떤 언어를 배우든지",
        "summary": (
            "PK-84 matni. Qaysi tilni oʻrgansangiz ham, muvaffaqiyatni "
            "belgilaydigan uchta narsa bir xil. Tadqiqotlarga asoslangan "
            "tushuntiruvchi matn."
        ),
        "order":   84,
        "grammar": [
            {
                "pattern":  "든지 … 든지 — xoh …, xoh …",
                "meaning":  "Tanlovning ahamiyati yoʻqligini bildiradi. "
                            "Qolip juft ishlaydi va otda (이)든지 boʻladi.",
                "examples": ["한국어든지 영어든지 아랍어든지 방법은 크게 다르지 않다.",
                             "어떤 언어를 배우든지 이 세 가지는 같다."],
            },
            {
                "pattern":  "든 / 건 — qisqa shakllar",
                "meaning":  "Ogʻzaki va yozma matnda 든지 koʻpincha 든 ga "
                            "qisqaradi. 건 esa keskinroq eshitiladi. "
                            "Ikkalasi ham juft ishlaydi.",
                "examples": ["틀리든 맞든 입으로 말한 문장만 기억에 남는다.",
                             "교과서로 배우건 드라마로 배우건 계속하는 사람이 이긴다."],
            },
            {
                "pattern":  "누구든지 — soʻroq soʻzi + 든지",
                "meaning":  "Soʻroq soʻziga qoʻshilganda “har qanday” "
                            "degan maʼno beradi: 뭐든지, 누구든지, "
                            "언제든지, 어디든지.",
                "examples": ["누구든지 언어를 배울 수 있어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-pos="adv" data-tr="xoh koreyscha">한국어든지</span> 영어든지 <span class="cn-word" data-tr="arabcha">아랍어</span>든지, 언어를 배우는 <span class="cn-word" data-tr="usul">방법</span>은 크게 다르지 않다. <span class="cn-word" data-tr="tadqiqotchilar">연구자</span>들은 오랫동안 이 <span class="cn-word" data-tr="savol">질문</span>을 조사했다. 그리고 세 가지 답을 찾았다.</p>

<p><span class="cn-word" data-tr="birinchidan">첫째</span>, 시간이 아니라 <span class="cn-word" data-tr="marta, son">횟수</span>다.</p>

<p>하루에 세 시간을 한 번 <span class="cn-word" data-pos="verb" data-tr="oʻqisang ham">공부하든</span> 삼십 분을 여섯 번 공부하든 시간은 같다. 그러나 결과는 같지 않다. <span class="cn-word" data-tr="miya">뇌</span>는 <span class="cn-word" data-tr="takror">반복</span>을 좋아한다. 나누어 만난 <span class="cn-word" data-tr="maʼlumot">정보</span>를 더 오래 기억한다.</p>

<p><span class="cn-word" data-tr="ikkinchidan">둘째</span>, <span class="cn-word" data-tr="mukammallik">완벽함</span>이 아니라 <span class="cn-word" data-tr="qoʻllash">사용</span>이다.</p>

<p>많은 학생은 실수가 <span class="cn-word" data-pos="adj" data-tr="qoʻrqinchli boʻlgani uchun">무서워서</span> 말하지 않는다. 그러나 <span class="cn-word" data-pos="verb" data-tr="xato qilsang ham, toʻgʻri qilsang ham">틀리든 맞든</span> 입으로 말한 <span class="cn-word" data-tr="jumla">문장</span>만 기억에 <span class="cn-word" data-pos="verb" data-tr="qoladi">남는다</span>.</p>

<p>한 연구에서 두 그룹이 같은 <span class="cn-word" data-tr="muddat">기간</span> 동안 공부했다. 첫 번째 그룹은 <span class="cn-word" data-tr="grammatika">문법</span>을 <span class="cn-word" data-pos="adv" data-tr="aniq">정확히</span> 배웠다. 두 번째 그룹은 매일 십 분씩 말했다. 육 개월 후에 두 번째 그룹이 <span class="cn-word" data-pos="adv" data-tr="ancha">훨씬</span> 잘했다.</p>

<p><span class="cn-word" data-tr="uchinchidan">셋째</span>, <span class="cn-word" data-tr="qiziqarlilik">재미</span>다.</p>

<p><span class="cn-word" data-tr="darslik">교과서</span>로 <span class="cn-word" data-pos="verb" data-tr="oʻrgansang ham">배우건</span> 드라마로 배우건 노래로 배우건, 계속하는 사람이 <span class="cn-word" data-pos="verb" data-tr="yutadi">이긴다</span>. 그리고 재미있는 방법을 찾은 사람이 계속한다.</p>

<p>물론 언어마다 어려운 점은 다르다. 한국어는 <span class="cn-word" data-tr="qoʻshimcha (조사)">조사</span>와 <span class="cn-word" data-tr="hurmat shakli">높임말</span>이 어렵다. 영어는 <span class="cn-word" data-tr="talaffuz">발음</span>이 어렵다. 아랍어는 글자가 어렵다.</p>

<p>그러나 어떤 언어를 배우든지 이 세 가지는 같다. <span class="cn-word" data-pos="adv" data-tr="tez-tez">자주</span>, 사용하면서, 재미있게.</p>

<p>한 <span class="cn-word" data-tr="tilshunos">언어학자</span>는 이렇게 말한다. “<span class="cn-word" data-pos="adv" data-tr="kim boʻlsa ham">누구든지</span> 언어를 배울 수 있어요. 우리는 모두 한 번 성공했어요. <span class="cn-word" data-tr="ona tili">모국어</span>요.”</p>

<p>마지막 문장이 중요하다. 여러분은 이미 한 번 <span class="cn-word" data-pos="verb" data-tr="uddaladingiz">해냈다</span>. 그때는 교과서도 없었다.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, uch soatni bir marta oʻqish va oʻttiz "
                        "daqiqani olti marta oʻqish orasida qanday farq bor?",
                "choices": [
                    "Hech qanday farq yoʻq",
                    "Vaqt bir xil, lekin natija bir xil emas — miya "
                    "takrorni yaxshi koʻradi",
                    "Bir marta oʻqish samaraliroq",
                    "Matnda bu haqda aytilmagan",
                ],
                "answer": 1,
                "explanation": "“시간은 같다. 그러나 결과는 같지 않다.” "
                               "Birinchi javob — vaqt emas, <b>marta</b> "
                               "(횟수).",
            },
            {
                "text": "“틀리든 맞든 입으로 말한 문장만 기억에 남는다” — "
                        "bu nimani anglatadi?",
                "choices": [
                    "Faqat toʻgʻri jumlalarni aytish kerak",
                    "Xato qilishdan qoʻrqmaslik kerak — ogʻizdan chiqqan "
                    "jumla, xato boʻlsa ham, esda qoladi",
                    "Gapirish foydasiz",
                    "Grammatikani oʻrganish shart emas",
                ],
                "answer": 1,
                "explanation": "든 … 든 tanlovni bekor qiladi: toʻgʻrimi, "
                               "xatomi — <b>farqi yoʻq</b>, muhimi "
                               "aytilgani.",
            },
            {
                "text": "Tilshunosning oxirgi dalili nima?",
                "choices": [
                    "Til oʻrganish faqat bolalar uchun",
                    "Har kim tilni oʻrgana oladi — chunki hammamiz "
                    "ona tilimizni allaqachon bir marta oʻrganganmiz",
                    "Darslik eng muhim vosita",
                    "Chet tilini oʻrganish mumkin emas",
                ],
                "answer": 1,
                "explanation": "“우리는 모두 한 번 성공했어요. 모국어요.” "
                               "Va matn buni kuchaytiradi: “그때는 교과서도 "
                               "없었다.”",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-85 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "반대로 간 사람",
        "summary": (
            "PK-85 matni. Hamma shaharga ketganda, Pak togʻ qishlogʻida "
            "qoldi va yalangʻoch togʻga daraxt ekishni boshladi. "
            "Qirq yildan keyin."
        ),
        "order":   85,
        "grammar": [
            {
                "pattern":  "(느)니 차라리 — …gandan koʻra … yaxshiroq",
                "meaning":  "Ikkala variant ham yoqimsiz, lekin soʻzlovchi "
                            "kamroq yomonini tanlaydi. Faqat feʼl bilan, "
                            "oldida zamon boʻlmaydi.",
                "examples": ["도시에서 좁은 방에 사느니 차라리 여기서 나무를 심는다.",
                             "도시에서 후회하면서 사느니 차라리 여기서 힘든 것이 나았어요."],
            },
            {
                "pattern":  "(으)나 마나 — qilsa ham, qilmasa ham bir xil",
                "meaning":  "Ichida 말다 turibdi. Natija oldindan maʼlum "
                            "degan maʼno beradi — shuning uchun matnda uni "
                            "shubhalanuvchi qoʻshni aytadi.",
                "examples": ["심어 보나 마나 안 될 거예요.",
                             "한 그루를 심으나 마나 산은 변하지 않는다."],
            },
            {
                "pattern":  "Ikki qolip bir hikoyada",
                "meaning":  "(느)니 차라리 — qahramonning tanlovi. "
                            "(으)나 마나 — atrofdagilarning bahosi. "
                            "Hikoya shu ikki gapning kurashi ustiga "
                            "qurilgan.",
                "examples": ["사람들은 “안 될 거라고” 했다. 그는 그냥 심었다."],
            },
        ],
        "body": '''<p>1980<span class="cn-word" data-tr="yillar">년대</span>에 <span class="cn-word" data-tr="Kangvon viloyati">강원도</span>의 한 <span class="cn-word" data-tr="togʻ qishlogʻi">산골 마을</span>에는 백 <span class="cn-word" data-tr="xonadon">가구</span>가 살았다. 이십 년 후에는 열두 가구만 남았다. 젊은 사람들은 다 도시로 갔다.</p>

<p>박씨는 남았다. 그때 그는 마흔 살이었다.</p>

<p>친구들이 물었다. “왜 안 가요? 여기는 일이 없어요.”</p>

<p>박씨는 이렇게 답했다. “도시에서 좁은 방에 <span class="cn-word" data-pos="verb" data-tr="yashagandan koʻra">사느니</span> <span class="cn-word" data-pos="adv" data-tr="koʻra, aksincha">차라리</span> 여기서 나무를 <span class="cn-word" data-pos="verb" data-tr="ekaman">심는다</span>.”</p>

<p>사람들은 웃었다. 그 산은 오래전에 <span class="cn-word" data-tr="daraxt kesish">벌목</span>으로 <span class="cn-word" data-pos="verb" data-tr="yalangʻochlanib qolgan edi">벌거벗었다</span>. <span class="cn-word" data-tr="tuproq">흙</span>은 얇았고 비가 오면 <span class="cn-word" data-pos="verb" data-tr="oqib ketardi">흘러내렸다</span>.</p>

<p>“<span class="cn-word" data-pos="verb" data-tr="eksang ham, ekmasang ham">심어 보나 마나</span> 안 될 거예요.” 한 <span class="cn-word" data-tr="qoʻshni">이웃</span>이 말했다. “여기는 삼십 년 동안 아무것도 안 <span class="cn-word" data-pos="verb" data-tr="oʻsdi">자랐어요</span>.”</p>

<p>박씨는 대답하지 않았다. 다음 날 아침 여섯 시에 <span class="cn-word" data-tr="belkurak">삽</span>을 들고 산으로 갔다.</p>

<p>첫해에 그는 삼천 <span class="cn-word" data-tr="tup (daraxt sanogʻi)">그루</span>를 심었다. 다음 해 봄에 산에 올라갔다. <span class="cn-word" data-tr="yarmi">절반</span>이 <span class="cn-word" data-pos="verb" data-tr="oʻlib qolgan edi">죽어 있었다</span>. 그는 다시 심었다.</p>

<p>십 년 동안 그렇게 했다. 낮에는 나무를 심고 밤에는 <span class="cn-word" data-tr="dehqonchilik ishi">농사일</span>을 했다. 돈은 <span class="cn-word" data-pos="verb" data-tr="topa olmadi">벌지 못했다</span>. 아내가 시장에서 <span class="cn-word" data-tr="sabzavot">채소</span>를 팔았다.</p>

<p>이십 년째 되는 해에 마을 사람들이 무엇인가를 느꼈다. 여름에 <span class="cn-word" data-tr="soy, ariq">개울</span>이 <span class="cn-word" data-pos="verb" data-tr="qurimadi">마르지 않았다</span>. <span class="cn-word" data-tr="ildiz">뿌리</span>가 물을 <span class="cn-word" data-pos="verb" data-tr="ushlab turardi">잡고 있었다</span>.</p>

<p>이십오 년째에 새들이 돌아왔다. 그리고 사람들도 조금씩 돌아왔다.</p>

<p>지금 그 산에는 나무가 십오만 그루 있다. 마을에는 사십 가구가 산다. 작은 카페도 하나 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">생겼다</span>.</p>

<p>박씨는 지금 일흔 살이다. 아직 아침 여섯 시에 산에 간다.</p>

<p><span class="cn-word" data-tr="jurnalist">기자</span>가 물었다. “힘들지 않았어요?”</p>

<p>박씨는 웃었다. “힘들었어요. 하지만 도시에서 <span class="cn-word" data-pos="verb" data-tr="pushaymon boʻlib">후회하면서</span> 사느니 차라리 여기서 힘든 것이 <span class="cn-word" data-pos="adj" data-tr="yaxshiroq edi">나았어요</span>.”</p>

<p>그리고 이렇게 덧붙였다. “사람들이 안 될 거라고 했어요. 저도 몰랐어요. 그래서 그냥 심었어요.”</p>

<p>한 그루를 심으나 마나 산은 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmaydi">변하지 않는다</span>. 십오만 그루는 산을 바꾼다. 그 <span class="cn-word" data-tr="orada">사이</span>에 사십 년이 있었을 뿐이다.</p>''',
        "questions": [
            {
                "text": "Pak nega qishloqda qoldi?",
                "choices": [
                    "Shaharga ketishga puli yoʻq edi",
                    "Shaharda tor xonada yashagandan koʻra togʻda daraxt "
                    "ekishni afzal koʻrdi",
                    "Oilasi ruxsat bermadi",
                    "Qishloqda yaxshi ish bor edi",
                ],
                "answer": 1,
                "explanation": "“도시에서 좁은 방에 <b>사느니 차라리</b> "
                               "여기서 나무를 심는다.” Ikkala variant ham "
                               "oson emas — u kamroq yomonini tanladi.",
            },
            {
                "text": "“심어 보나 마나 안 될 거예요” — buni kim va nima "
                        "maʼnoda aytdi?",
                "choices": [
                    "Qoʻshni — “eksang ham, ekmasang ham natija bir xil, "
                    "bu yerda hech narsa oʻsmaydi”",
                    "Pak — “men albatta ekaman”",
                    "Jurnalist — “bu juda qiyin ish”",
                    "Xotini — “pul topish kerak”",
                ],
                "answer": 0,
                "explanation": "(으)나 마나 — natija <b>oldindan maʼlum</b> "
                               "degan ishonch. Hikoya aynan shu gapni "
                               "rad etadi.",
            },
            {
                "text": "Matnning oxirgi jumlasi nima demoqchi?",
                "choices": [
                    "Daraxt ekish foydasiz",
                    "Bitta daraxt hech narsani oʻzgartirmaydi — lekin 150 "
                    "ming daraxt oʻzgartiradi, va oradagi farq faqat "
                    "qirq yil",
                    "Togʻ hech qachon oʻzgarmagan",
                    "Qirq yil juda uzoq vaqt",
                ],
                "answer": 1,
                "explanation": "“한 그루를 <b>심으나 마나</b>” toʻgʻri — "
                               "bitta daraxt uchun. Xato faqat "
                               "<b>miqyosda</b> edi, mantiqda emas.",
            },
        ],
    },
]
