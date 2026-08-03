# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-65 … PK-67 ((으)ㄹ수록, 반면에, 뿐만 아니라).

Shakl xilma-xilligi (toc dagi "STORIES, NOT DIALOGUES" qoidasiga koʻra),
avvalgi ikki batchdan boshqacha uchta shakl:
  65 — XALQ ERTAGI (옛날이야기). “…gan sari” — ibratli ertakning oʻz tili:
       togʻga chiqqan sari qorongʻi, ochkoʻzlik ortgan sari ogʻir.
  66 — BLOG POSTI. Ikki shaharni taqqoslash — 반면에 ning tabiiy uyi.
  67 — KICHIK SIRLI HIKOYA. Sinfni kim tozalab ketyapti?

Kumulyativ qoida: PK-67 gacha oʻrganilgan hamma narsa ochiq.
PK-65 matnida 반면에 (66) va 뿐만 아니라 (67) YOʻQ.
PK-66 matnida 뿐만 아니라 (67) yoʻq.
데다가 (68), 는 바람에 / 탓에 / 느라고 (69) — hech qaysisida yoʻq.
(으)ㄹ래요, (으)ㄹ게요, (으)ㄹ지, (으)ㄹ까, 는데, 네요 ham hali
oʻrganilmagan — ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_65_67.py --author=prime
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
    {
        "title":   "산을 오르는 나무꾼",
        "summary": (
            "PK-65 matni. Xalq ertagi shaklida: oʻtinchi togʻga chiqqan sari "
            "quti ogʻirlashadi — “…gan sari” butun ertakning oʻqi."
        ),
        "order":   65,
        "grammar": [
            {
                "pattern":  "동사/형용사 + (으)ㄹ수록",
                "meaning":  "“…gan sari” — bir narsa ortgan sari ikkinchisi "
                            "ham oʻzgaradi. Oʻzbekchada tayyor juftligi "
                            "bor: “chiqqan sari”, “oʻtgani sayin”.",
                "examples": ["올라갈수록 나무가 굵어졌어요.",
                             "가질수록 더 가지고 싶었어요.",
                             "욕심은 많을수록 무거워져요."],
            },
            {
                "pattern":  "(으)ㄹ수록 + 아/어지다",
                "meaning":  "Bu qolip oʻzgarish haqida, shuning uchun "
                            "keyingi gapda koʻpincha 아/어지다 turadi "
                            "(PK-56).",
                "examples": ["갈수록 조용해졌어요.",
                             "상자가 무거울수록 산길이 힘들어졌어요."],
            },
            {
                "pattern":  "옛날 옛날에 — ertak boshlanishi",
                "meaning":  "Koreys xalq ertaklari deyarli har doim shu "
                            "soʻzlar bilan boshlanadi — oʻzbekchadagi "
                            "“bor ekan, yoʻq ekan” kabi.",
                "examples": ["옛날 옛날에 한 나무꾼이 살았어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="bor ekan, yoʻq ekan">옛날 옛날에</span> 한 <span class="cn-word" data-tr="oʻtinchi">나무꾼</span>이 살았어요. 나무꾼은 매일 산에 갔어요.</p>

<p>어느 날 나무꾼이 산 <span class="cn-word" data-tr="chuqur joyiga">깊은 곳</span>에 갔어요. <span class="cn-word" data-pos="verb" data-tr="chiqqan sari">올라갈수록</span> 나무가 <span class="cn-word" data-pos="verb" data-tr="yoʻgʻonlashdi">굵어졌어요</span>. 그리고 갈수록 <span class="cn-word" data-pos="verb" data-tr="jimjit boʻldi">조용해졌어요</span>.</p>

<p>나무꾼은 작은 집을 <span class="cn-word" data-pos="verb" data-tr="topdi">발견했어요</span>. 집 안에 <span class="cn-word" data-tr="kampir">할머니</span>가 있었어요. 할머니가 <span class="cn-word" data-tr="quti">상자</span> 하나를 주면서 말했어요.</p>

<p><strong>할머니:</strong> 이 상자를 가져가세요. 하지만 <span class="cn-word" data-tr="ochkoʻzlik">욕심</span>을 내면 안 돼요.</p>

<p>나무꾼이 상자를 열었어요. 안에 <span class="cn-word" data-tr="oltin">금</span>이 있었어요. 나무꾼은 아주 <span class="cn-word" data-pos="adj" data-tr="xursand edi">기뻤어요</span>.</p>

<p>다음 날 나무꾼은 다시 산에 갔어요. 그리고 또 갔어요. 갈수록 욕심이 <span class="cn-word" data-pos="verb" data-tr="kattalashdi">커졌어요</span>. <span class="cn-word" data-pos="adv" data-tr="avvaliga">처음에는</span> 하나만 <span class="cn-word" data-pos="verb" data-tr="istadi">원했어요</span>. 하지만 <span class="cn-word" data-pos="verb" data-tr="ega boʻlgan sari">가질수록</span> 더 가지고 싶었어요.</p>

<p><span class="cn-word" data-tr="oxirgi">마지막</span> 날, 나무꾼은 상자를 <span class="cn-word" data-tr="oʻnta">열 개</span> 가져갔어요. 상자가 <span class="cn-word" data-pos="adj" data-tr="ogʻir boʻlgan sari">무거울수록</span> <span class="cn-word" data-tr="togʻ yoʻli">산길</span>이 <span class="cn-word" data-pos="verb" data-tr="qiyinlashdi">힘들어졌어요</span>. 나무꾼은 <span class="cn-word" data-pos="verb" data-tr="tusha olmadi">내려올 수 없었어요</span>.</p>

<p>그때 할머니가 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">나타났어요</span>.</p>

<p><strong>할머니:</strong> 보세요. 욕심은 많을수록 <span class="cn-word" data-pos="verb" data-tr="ogʻirlashadi">무거워져요</span>.</p>

<p>나무꾼은 상자를 모두 <span class="cn-word" data-pos="verb" data-tr="qoʻydi">놓았어요</span>. 그리고 <span class="cn-word" data-pos="adv" data-tr="yengil">가볍게</span> 집에 돌아갔어요.</p>''',
        "questions": [
            {
                "text": "Togʻga chiqqan sari nima oʻzgardi?",
                "choices": [
                    "Daraxtlar yoʻgʻonlashdi va atrof jimjit boʻldi",
                    "Havo isidi",
                    "Yoʻl kengaydi",
                    "Odamlar koʻpaydi",
                ],
                "answer": 0,
                "explanation": "“<b>올라갈수록</b> 나무가 굵어졌어요. "
                               "그리고 <b>갈수록</b> 조용해졌어요” — "
                               "(으)ㄹ수록 va 아/어지다 juftligi.",
            },
            {
                "text": "Nega oʻtinchi togʻdan tusha olmadi?",
                "choices": [
                    "Chunki yoʻlni yoʻqotdi",
                    "Chunki kampir yoʻl bermadi",
                    "Chunki oʻnta quti olgan edi va ogʻirlik ortgan sari "
                    "yoʻl qiyinlashdi",
                    "Chunki qorongʻi tushdi",
                ],
                "answer": 2,
                "explanation": "“상자가 <b>무거울수록</b> 산길이 "
                               "힘들어졌어요” — ertakning butun mantiqi "
                               "shu qolipga qurilgan.",
            },
            {
                "text": "Kampirning “욕심은 많을수록 무거워져요” gapi nima "
                        "demoqchi?",
                "choices": [
                    "Oltin ogʻir metall",
                    "Ochkoʻzlik ortgan sari odamga ogʻirlik boʻladi",
                    "Qutilarni sanash kerak",
                    "Togʻga chiqish xavfli",
                ],
                "answer": 1,
                "explanation": "Bu ertakning <b>ibrati</b>. 많을수록 — "
                               "sifat bilan ham (으)ㄹ수록 ishlaydi, va "
                               "keyin yana 무거워져요 (아/어지다).",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "딜노자의 블로그: 서울과 타슈켄트",
        "summary": (
            "PK-66 matni. Blog posti shaklida: Seulda ikki hafta boʻlgan "
            "Dilnoza ikki shaharni yonma-yon qoʻyadi."
        ),
        "order":   66,
        "grammar": [
            {
                "pattern":  "(으)ㄴ/는 반면에",
                "meaning":  "Bitta mavzuning ikki tomoni — oʻzbekchadagi "
                            "“esa”. Feʼl 는, sifat (으)ㄴ, ot 인 oladi.",
                "examples": ["지하철이 편리한 반면에 복잡해요.",
                             "서울 사람들은 바쁜 반면에 아주 친절해요.",
                             "타슈켄트 사람들은 천천히 사는 반면에 손님을 "
                             "더 초대해요."],
            },
            {
                "pattern":  "은/는 — qiyoslash yuklamasi",
                "meaning":  "반면에 gaplarida ikkala egada ham 은/는 "
                            "turadi. Bu tasodif emas: 은/는 (PK-12) aynan "
                            "qiyoslash uchun.",
                "examples": ["서울은 … 반면에 타슈켄트는 …"],
            },
            {
                "pattern":  "Eslatma: 지만 va 반면에",
                "meaning":  "지만 (PK-34) — oddiy “lekin”, bogʻliq "
                            "boʻlmagan gaplarni ham qoʻshadi. 반면에 esa "
                            "faqat bitta mavzuning ikki tomoni uchun.",
                "examples": ["우즈베크 음식은 기름지지만 순해요."],
            },
        ],
        "body": '''<p><strong>딜노자의 <span class="cn-word" data-tr="blog">블로그</span> · 8월 3일</strong></p>

<p>안녕하세요! 저는 지난달에 서울에 <span class="cn-word" data-tr="ikki hafta">이 주일</span> 동안 <span class="cn-word" data-pos="verb" data-tr="borib keldim">다녀왔어요</span>. 오늘은 서울과 <span class="cn-word" data-tr="Toshkent">타슈켄트</span>를 <span class="cn-word" data-pos="verb" data-tr="taqqoslamoqchiman">비교해 보려고 해요</span>.</p>

<p>먼저 <span class="cn-word" data-tr="transport">교통</span>이에요. 서울은 <span class="cn-word" data-tr="metro">지하철</span>이 <span class="cn-word" data-pos="adj" data-tr="qulay boʻlsa-da">편리한 반면에</span> 아주 <span class="cn-word" data-pos="adj" data-tr="gavjum">복잡해요</span>. 아침에는 사람이 정말 많아요. 타슈켄트는 지하철이 <span class="cn-word" data-pos="adj" data-tr="tinch boʻlsa-da">조용한 반면에</span> <span class="cn-word" data-tr="yoʻnalish">노선</span>이 적어요.</p>

<p><span class="cn-word" data-tr="taom">음식</span>도 달라요. 한국 음식은 <span class="cn-word" data-pos="adj" data-tr="achchiq">맵고</span> <span class="cn-word" data-pos="adj" data-tr="shoʻr boʻlsa-da">짠 반면에</span> 우즈베크 음식은 <span class="cn-word" data-pos="adj" data-tr="yogʻli">기름지지만</span> <span class="cn-word" data-pos="adj" data-tr="mayin">순해요</span>. 저는 처음에 김치를 못 먹었어요. 하지만 지금은 아주 좋아해요.</p>

<p>사람들은 어때요? 서울 사람들은 <span class="cn-word" data-pos="adj" data-tr="band boʻlsa-da">바쁜 반면에</span> 아주 <span class="cn-word" data-pos="adj" data-tr="mehribon">친절해요</span>. 길을 물어보면 <span class="cn-word" data-pos="adv" data-tr="oʻzi">직접</span> <span class="cn-word" data-pos="verb" data-tr="olib borib qoʻyishdi">데려다줬어요</span>. 타슈켄트 사람들은 천천히 <span class="cn-word" data-pos="verb" data-tr="yashasa-da">사는 반면에</span> <span class="cn-word" data-tr="mehmon">손님</span>을 더 자주 <span class="cn-word" data-pos="verb" data-tr="taklif qiladi">초대해요</span>.</p>

<p><span class="cn-word" data-tr="uy narxi">집값</span>은요? 서울이 <span class="cn-word" data-pos="adj" data-tr="qimmat boʻlsa-da">비싼 반면에</span> 방이 아주 작아요. 이건 정말 <span class="cn-word" data-pos="verb" data-tr="hayron qoldirdi">놀랐어요</span>.</p>

<p><span class="cn-word" data-tr="xulosa">결론</span>은요? 두 <span class="cn-word" data-tr="shahar">도시</span> 다 좋아요. 서울은 <span class="cn-word" data-tr="yangi narsa">새로운 것</span>이 많은 반면에 타슈켄트는 <span class="cn-word" data-tr="koʻngil">마음</span>이 <span class="cn-word" data-pos="adj" data-tr="tinch">편해요</span>.</p>

<p>다음에는 부산에 가 보고 싶어요. <span class="cn-word" data-tr="izoh">댓글</span>로 <span class="cn-word" data-pos="verb" data-tr="tavsiya qiling">추천해 주세요</span>!</p>''',
        "questions": [
            {
                "text": "Dilnoza Seul metrosi haqida nima yozgan?",
                "choices": [
                    "Qulay, lekin juda gavjum",
                    "Tinch, lekin yoʻnalishi kam",
                    "Qimmat va sekin",
                    "Toshkent metrosidan yomon",
                ],
                "answer": 0,
                "explanation": "“지하철이 <b>편리한 반면에</b> 아주 "
                               "복잡해요” — bitta narsaning ikki tomoni, "
                               "aynan 반면에 ning ishi.",
            },
            {
                "text": "Uy narxi haqida nima aytilgan?",
                "choices": [
                    "Seulda arzon, xonasi katta",
                    "Toshkentda qimmat",
                    "Seulda qimmat, lekin xonasi juda kichkina",
                    "Ikkalasida bir xil",
                ],
                "answer": 2,
                "explanation": "“서울이 <b>비싼 반면에</b> 방이 아주 "
                               "작아요” — qimmatlik va kichiklik bitta "
                               "mavzuning (uy) ikki tomoni.",
            },
            {
                "text": "Matndagi “우즈베크 음식은 기름지지만 순해요” gapida "
                        "nega 반면에 emas, 지만 ishlatilgan?",
                "choices": [
                    "Chunki 반면에 faqat feʼl bilan keladi",
                    "Chunki bu oddiy “lekin” — ikkala tomon ham taqqoslash "
                    "juftligi emas",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 순하다 sifat",
                ],
                "answer": 1,
                "explanation": "<b>지만</b> shunchaki qarama-qarshilik "
                               "qoʻshadi. <b>반면에</b> esa ikki tomonni "
                               "tarozining ikki pallasiga qoʻyadi — "
                               "matndagi 서울/타슈켄트 juftliklari kabi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "누가 도와줬어요?",
        "summary": (
            "PK-67 matni. Kichik sirli hikoya: har kuni ertalab sinfni kimdir "
            "tozalab ketadi. Sherbek erta kelib sirni ochadi."
        ),
        "order":   67,
        "grammar": [
            {
                "pattern":  "(으)ㄹ 뿐만 아니라",
                "meaning":  "“Faqat … emas, … ham”. Bir tomonga qaragan "
                            "ikkinchi dalilni qoʻshadi; ikkinchi gapda "
                            "deyarli har doim 도 turadi.",
                "examples": ["칠판도 깨끗할 뿐만 아니라 책상도 정리되어 "
                             "있었어요.",
                             "하나 씨는 공부를 잘할 뿐만 아니라 마음도 "
                             "따뜻해요."],
            },
            {
                "pattern":  "Eslatma: koʻchirma gap qaytadi",
                "meaning":  "PK-60 va PK-61 shu yerda ishlab turibdi: "
                            "아니라고 하다 (darak), 고 하다 bilan "
                            "boshqaning gapini yetkazish.",
                "examples": ["아프소나 씨는 아니라고 했어요."],
            },
            {
                "pattern":  "Eslatma: 아/어 있다 va majhul",
                "meaning":  "PK-42 va PK-56: 열려 있었어요 (eshik ochiq "
                            "turardi), 정리되어 있었어요 (yigʻishtirilgan "
                            "edi) — holatni bildiradi.",
                "examples": ["교실 문이 열려 있었어요."],
            },
        ],
        "body": '''<p>월요일 아침이었어요. 이 학년 삼 반 학생들이 교실에 들어왔어요. 그런데 교실이 아주 <span class="cn-word" data-pos="adj" data-tr="toza edi">깨끗했어요</span>. <span class="cn-word" data-tr="doska">칠판</span>도 <span class="cn-word" data-pos="adj" data-tr="faqat toza emas">깨끗할 뿐만 아니라</span> <span class="cn-word" data-tr="parta">책상</span>도 <span class="cn-word" data-pos="verb" data-tr="yigʻishtirilgan edi">정리되어 있었어요</span>.</p>

<p>화요일에도 <span class="cn-word" data-pos="adj" data-tr="xuddi shunday edi">똑같았어요</span>. 수요일에도요. 학생들은 <span class="cn-word" data-pos="verb" data-tr="hayron boʻldi">이상하게 생각했어요</span>.</p>

<p><strong>베크조드:</strong> 누가 <span class="cn-word" data-pos="verb" data-tr="tozaladi">청소했어요</span>? 선생님일 거예요.</p>

<p>아프소나 씨는 <span class="cn-word" data-pos="verb" data-tr="yoʻq deb aytdi">아니라고 했어요</span>. 선생님은 아침마다 <span class="cn-word" data-tr="yigʻilish">회의</span>가 있어요.</p>

<p>목요일 아침, 셰르벡 씨가 아주 일찍 학교에 갔어요. 여섯 시 반이었어요. <span class="cn-word" data-tr="yoʻlak">복도</span>가 조용했어요. 교실 문이 <span class="cn-word" data-pos="verb" data-tr="ochiq turardi">열려 있었어요</span>.</p>

<p>안에 한 학생이 있었어요. 하나 씨였어요. 하나 씨는 셰르벡 씨를 보고 놀랐어요. 그리고 조용히 말했어요.</p>

<p><strong>하나:</strong> 저는 아침에 일찍 일어나요. 집에서 <span class="cn-word" data-tr="qiladigan ish">할 일</span>이 없어요. 그래서 교실을 <span class="cn-word" data-pos="verb" data-tr="yigʻishtiraman">치워요</span>.</p>

<p>셰르벡 씨는 <span class="cn-word" data-pos="adv" data-tr="hech kimga">아무한테도</span> 말하지 않았어요. 하지만 금요일 아침에 반 친구들이 칠판에 큰 <span class="cn-word" data-tr="yozuv">글</span>을 <span class="cn-word" data-pos="verb" data-tr="yozib qoʻygan edi">써 놓았어요</span>.</p>

<p><strong>“하나 씨, 고마워요!”</strong></p>

<p>하나 씨는 <span class="cn-word" data-pos="verb" data-tr="faqat yaxshi oʻqimaydi">공부를 잘할 뿐만 아니라</span> <span class="cn-word" data-tr="koʻngil">마음</span>도 <span class="cn-word" data-pos="adj" data-tr="iliq">따뜻해요</span>. 그날 <span class="cn-word" data-tr="keyin">이후</span>로 청소는 모두 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 했어요.</p>''',
        "questions": [
            {
                "text": "Sinfni kim tozalab ketardi?",
                "choices": [
                    "Oʻqituvchi",
                    "Bekzod",
                    "Hana",
                    "Sherbek",
                ],
                "answer": 2,
                "explanation": "Sherbek payshanba kuni soat olti yarimda "
                               "kelganda sinfda <b>하나 씨</b>ni koʻrdi. "
                               "U erta turadi va uyda qiladigan ishi yoʻq.",
            },
            {
                "text": "Sherbek sirni bilgach nima qildi?",
                "choices": [
                    "Darhol hammaga aytdi",
                    "Hech kimga aytmadi",
                    "Oʻqituvchiga xabar berdi",
                    "Hanaga yordam berishni taklif qildi",
                ],
                "answer": 1,
                "explanation": "“셰르벡 씨는 <b>아무한테도</b> 말하지 "
                               "않았어요” — shunga qaramay sinf baribir "
                               "bilib qoldi.",
            },
            {
                "text": "“공부를 잘할 뿐만 아니라 마음도 따뜻해요” — nega bu "
                        "yerda 반면에 emas, 뿐만 아니라 ishlatilgan?",
                "choices": [
                    "Chunki gap oʻtgan zamonda",
                    "Chunki ikkala dalil ham maqtov — bir tomonga qaragan",
                    "Chunki 따뜻하다 sifat",
                    "Chunki gapda 도 bor",
                ],
                "answer": 1,
                "explanation": "<b>뿐만 아니라</b> bir yoʻnalishdagi ikki "
                               "dalilni qoʻshadi. Agar biri maqtov, biri "
                               "ayb boʻlganda <b>반면에</b> (PK-66) "
                               "kerak boʻlardi.",
            },
        ],
    },
]
