# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-86 … PK-88 ((으)ㅁ으로써, 지경이다, 리가 없다).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 da gaplashadi.
Mavzu — 정보문 va 인생 이야기 navbatma-navbat:
  86 — 정보문: chiqindini kamaytirgan shahar (종량제)
  87 — 인생 이야기: koʻchish kuni — hammasi buzilgan kun va bir qozon
  88 — 정보문: odamlar ishonmagan narsalar (Kopernik, Semmelveys, poyezd)

Kumulyativ qoida: PK-88 gacha oʻrganilgan hamma narsa ochiq.
PK-86 matnida 지경이다 (87) va 리가 없다 (88) YOʻQ.
PK-87 matnida 리가 없다 / 턱이 없다 (88) yoʻq.
에 달려 있다 (89), (으)려던 참 (90), (이)나 다름없다 · 셈이다 (91),
다면서요 (92), 다니 (93) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다,
(느)ㄴ다면, 다는 것 — oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_86_88.py --author=prime
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
    # PK-86 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "쓰레기를 줄인 도시",
        "summary": (
            "PK-86 matni. Koreya chiqindisini qanday qilib uchdan biriga "
            "kamaytirdi — nasihat bilan emas, narx bilan. Tushuntiruvchi "
            "matn, 한다체 da."
        ),
        "order":   86,
        "grammar": [
            {
                "pattern":  "(으)ㅁ으로써 — …ish yoʻli bilan",
                "meaning":  "Harakatning oʻzi vositaga aylanadi. Rasmiy "
                            "yozma til — chora va uning natijasini "
                            "bogʻlash uchun eng qulay qolip.",
                "examples": ["봉투를 유료화함으로써 정부는 한 가지를 바꾸었다.",
                             "무게를 잼으로써 음식물 쓰레기도 줄었다."],
            },
            {
                "pattern":  "만들다 → 만듦",
                "meaning":  "ㄹ bilan tugaydigan feʼllarda (으)ㅁ "
                            "otlashtirishi <b>ㄻ</b> boʻladi: 만들다 → "
                            "만듦, 살다 → 삶, 알다 → 앎.",
                "examples": ["봉투 값을 만듦으로써 행동이 바뀌었다."],
            },
            {
                "pattern":  "Nega 정보문 ga bu qolip kerak",
                "meaning":  "Tushuntiruvchi matnning butun ishi — "
                            "“qanday chora → qanday natija”. "
                            "(으)ㅁ으로써 ikkalasini bitta jumlaga "
                            "sigʻdiradi. TOPIK 쓰기 51-54 da ham shu.",
                "examples": ["사람들은 돈을 아낌으로써 환경도 지켰다."],
            },
        ],
        "body": '''<p>1990<span class="cn-word" data-tr="yillar">년대</span> 초까지 한국의 <span class="cn-word" data-tr="chiqindi">쓰레기</span>는 계속 늘었다. 한 사람이 하루에 약 1.3킬로그램을 버렸다. <span class="cn-word" data-tr="chiqindixona, poligon">매립지</span>에 자리가 얼마 남지 않았다.</p>

<p>1995년에 <span class="cn-word" data-tr="hukumat">정부</span>는 새 <span class="cn-word" data-tr="tizim, tartib">제도</span>를 시작했다. 이름은 “<span class="cn-word" data-tr="chiqindi hajmiga qarab toʻlov">쓰레기 종량제</span>”다. 방법은 간단했다. 쓰레기는 <span class="cn-word" data-pos="verb" data-tr="belgilangan">정해진</span> <span class="cn-word" data-tr="paket">봉투</span>에만 버릴 수 있다. 그 봉투는 돈을 내고 사야 한다.</p>

<p>봉투를 <span class="cn-word" data-pos="verb" data-tr="pullik qilish bilan">유료화함으로써</span> 정부는 한 가지를 바꾸었다. 쓰레기를 많이 버리는 사람이 돈을 더 낸다.</p>

<p>결과는 빨랐다. 이 년 <span class="cn-word" data-tr="ichida">만</span>에 쓰레기가 삼십 <span class="cn-word" data-tr="foiz">퍼센트</span> 가까이 줄었다. 그리고 <span class="cn-word" data-tr="qayta ishlash">재활용</span>은 두 배로 늘었다. 이유는 간단하다. 재활용품은 봉투 없이 버릴 수 있다. 사람들은 돈을 <span class="cn-word" data-pos="verb" data-tr="tejash bilan">아낌으로써</span> <span class="cn-word" data-tr="atrof-muhit">환경</span>도 <span class="cn-word" data-pos="verb" data-tr="asradi">지켰다</span>.</p>

<p>두 번째 <span class="cn-word" data-tr="bosqich">단계</span>는 <span class="cn-word" data-tr="oziq-ovqat chiqindisi">음식물 쓰레기</span>였다. 2013년부터 아파트에 <span class="cn-word" data-tr="qurilma">기계</span>가 생겼다. 카드를 대고 음식물을 넣으면 <span class="cn-word" data-tr="ogʻirlik">무게</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻlchaydi">잰다</span>. 그리고 무게만큼 돈을 낸다. 무게를 <span class="cn-word" data-pos="verb" data-tr="oʻlchash bilan">잼으로써</span> 음식물 쓰레기도 이십 퍼센트 줄었다.</p>

<p>물론 <span class="cn-word" data-tr="norozilik">불만</span>도 있었다. 처음에 사람들은 화를 냈다. “왜 쓰레기까지 돈을 내요?” 어떤 사람들은 밤에 <span class="cn-word" data-pos="adv" data-tr="yashirincha">몰래</span> 버렸다. 그래서 정부는 <span class="cn-word" data-tr="jarima">벌금</span>을 만들었다.</p>

<p>지금 한국의 재활용률은 세계에서 가장 높은 나라 중 하나다.</p>

<p>이 이야기의 <span class="cn-word" data-tr="saboq">교훈</span>은 하나다. 사람들에게 “환경을 지키세요”라고 말하는 것으로는 <span class="cn-word" data-pos="adj" data-tr="yetarli emas edi">부족했다</span>. 봉투 <span class="cn-word" data-tr="narx">값</span>을 <span class="cn-word" data-pos="verb" data-tr="yaratish bilan">만듦으로써</span> <span class="cn-word" data-tr="xatti-harakat">행동</span>이 바뀌었다.</p>

<p>한 전문가는 이렇게 말한다. “<span class="cn-word" data-tr="qoida">규칙</span>을 만드는 것보다 값을 만드는 것이 빨라요.”</p>''',
        "questions": [
            {
                "text": "1995-yilgi tizim aslida nimani oʻzgartirdi?",
                "choices": [
                    "Chiqindi tashishni taqiqladi",
                    "Koʻp chiqindi chiqaradigan odam koʻproq pul toʻlaydigan "
                    "qildi",
                    "Qayta ishlashni majburiy qildi",
                    "Chiqindixonalarni kengaytirdi",
                ],
                "answer": 1,
                "explanation": "“봉투를 <b>유료화함으로써</b> 정부는 한 가지를 "
                               "바꾸었다. 쓰레기를 많이 버리는 사람이 돈을 더 "
                               "낸다.”",
            },
            {
                "text": "Nega qayta ishlash ikki barobar oshdi?",
                "choices": [
                    "Hukumat yangi zavodlar qurdi",
                    "Qayta ishlanadigan chiqindini paketsiz tashlash mumkin "
                    "edi — yaʼni tekin",
                    "Jarimalar joriy qilindi",
                    "Reklama koʻp boʻldi",
                ],
                "answer": 1,
                "explanation": "“재활용품은 봉투 없이 버릴 수 있다.” "
                               "Shuning uchun “사람들은 돈을 <b>아낌으로써</b> "
                               "환경도 지켰다”.",
            },
            {
                "text": "Matnning xulosasi nima?",
                "choices": [
                    "Chiqindi muammosini hal qilib boʻlmaydi",
                    "“Atrof-muhitni asrang” deb aytish yetarli emas edi — "
                    "xatti-harakatni narx oʻzgartirdi",
                    "Jarima eng samarali chora",
                    "Odamlar hech qachon oʻzgarmaydi",
                ],
                "answer": 1,
                "explanation": "“규칙을 만드는 것보다 값을 만드는 것이 "
                               "빨라요.” Nasihat emas, narx.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-87 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "이사하는 날",
        "summary": (
            "PK-87 matni. Jiyonning Seulga birinchi koʻchishi: kechikkan "
            "yuk mashinasi, buzilgan lift, beshinchi qavat — va kechqurun "
            "eshik taqillaydi."
        ),
        "order":   87,
        "grammar": [
            {
                "pattern":  "(으)ㄹ 지경이다 — …ay deb turibman",
                "meaning":  "Chegaraga yetgan holat. Ish hali boʻlmagan — "
                            "unga bir qadam qolgan. Deyarli har doim "
                            "yomon holat haqida.",
                "examples": ["세 시쯤 지영은 쓰러질 지경이었다.",
                             "다 처음에는 죽을 지경이에요."],
            },
            {
                "pattern":  "(으)ㄹ 지경이 되다",
                "meaning":  "“Shu holga kelmoq”. 지경 mustaqil ot "
                            "boʻlgani uchun 되다 bilan ham yuradi.",
                "examples": ["갑자기 울 지경이 되었다."],
            },
            {
                "pattern":  "Sabab + 지경이다",
                "meaning":  "Qolip odatda sabab bilan yuradi — 아/어서 "
                            "(PK-35) yoki (으)니까 (PK-48). Avval nima "
                            "boʻlgani, keyin qaysi chegaraga "
                            "yetilgani.",
                "examples": ["짐을 열 번쯤 올렸다. 그래서 쓰러질 지경이었다."],
            },
        ],
        "body": '''<p>지영은 스무 살에 처음 혼자 <span class="cn-word" data-pos="verb" data-tr="yashaydigan boʻldi">살게 되었다</span>. 대학교가 서울에 있었다. 고향에서 기차로 네 시간 걸렸다.</p>

<p><span class="cn-word" data-pos="verb" data-tr="koʻchish">이사하는</span> 날 아침부터 일이 <span class="cn-word" data-pos="verb" data-tr="chalkashdi">꼬였다</span>.</p>

<p>먼저 <span class="cn-word" data-tr="yuk mashinasi">이삿짐 트럭</span>이 두 시간 늦게 왔다. 기사는 길이 <span class="cn-word" data-pos="verb" data-tr="tirband edi">막혔다</span>고 했다. 지영은 <span class="cn-word" data-tr="yuk, buyum">짐</span> 옆에서 두 시간을 기다렸다. <span class="cn-word" data-tr="iyun">유월</span>이었다. <span class="cn-word" data-tr="ter">땀</span>이 흘렀다.</p>

<p>새 방에 도착했다. 그리고 더 큰 문제를 봤다. <span class="cn-word" data-tr="lift">엘리베이터</span>가 <span class="cn-word" data-pos="verb" data-tr="buzilgan edi">고장 났다</span>. 방은 오 층이었다.</p>

<p>지영과 기사는 짐을 하나씩 들고 올라갔다. <span class="cn-word" data-tr="muzlatgich">냉장고</span>, 책상, <span class="cn-word" data-tr="quti">상자</span> 열두 개. 오 층까지. 열 번쯤 <span class="cn-word" data-pos="verb" data-tr="chiqib-tushdi">올라갔다 내려왔다</span>.</p>

<p>세 시쯤 지영은 <span class="cn-word" data-pos="verb" data-tr="yiqilay deb turgan holatda edi">쓰러질 지경이었다</span>. 다리가 <span class="cn-word" data-pos="verb" data-tr="titrardi">떨렸다</span>. 물도 없었다. 그리고 상자가 열두 개였다.</p>

<p>다섯 시에 기사가 갔다. 지영은 상자들 <span class="cn-word" data-tr="orasida">사이</span>에 앉았다. 방은 <span class="cn-word" data-pos="adj" data-tr="notanish edi">낯설었다</span>. <span class="cn-word" data-tr="devor">벽</span>은 하얗고 아무것도 없었다. 갑자기 <span class="cn-word" data-pos="verb" data-tr="yigʻlab yuboradigan holga keldi">울 지경이 되었다</span>.</p>

<p>그때 문을 <span class="cn-word" data-pos="verb" data-tr="taqillatayotgan">두드리는</span> 소리가 났다.</p>

<p>아래층 할머니였다. 손에 <span class="cn-word" data-tr="qozon">냄비</span>를 들고 있었다.</p>

<p>“오늘 이사 왔어요? 우리 집에서 <span class="cn-word" data-tr="kimchi shoʻrvasi">김치찌개</span>를 <span class="cn-word" data-pos="verb" data-tr="qaynatdim">끓였어요</span>. 좀 가져왔어요.”</p>

<p>지영은 아무 말도 못 했다. 할머니는 냄비를 놓고 <span class="cn-word" data-tr="qoshiq">숟가락</span>도 두 개 꺼냈다. 그리고 상자 하나를 의자처럼 놓았다.</p>

<p>“밥은 먹어야 해요. 이사하는 날은 다 <span class="cn-word" data-pos="adj" data-tr="shunday boʻladi">이래요</span>.”</p>

<p>두 사람은 상자 위에서 김치찌개를 먹었다. 할머니는 십오 년 동안 그 건물에 살았다고 했다. 이사 오는 학생을 여러 번 봤다고 했다.</p>

<p>“다 처음에는 <span class="cn-word" data-pos="verb" data-tr="oʻlay deb turgan holatda">죽을 지경이에요</span>. 그런데 한 달만 지나면 괜찮아요.”</p>

<p>지영은 지금 스물여섯 살이다. 다른 도시에서 산다. 그 건물의 이름도 잊었다.</p>

<p>그러나 그날 저녁은 기억한다. 상자 위의 냄비. 숟가락 두 개. 하얀 벽.</p>

<p>가장 힘든 날에 누군가 문을 두드렸다. 그래서 그 하루는 다른 하루가 되었다.</p>''',
        "questions": [
            {
                "text": "Koʻchish kunida nima notoʻgʻri ketdi?",
                "choices": [
                    "Yuk mashinasi ikki soat kechikdi va lift buzilgan edi",
                    "Kalit yoʻqoldi",
                    "Yomgʻir yogʻdi",
                    "Yangi xonaning eshigi ochilmadi",
                ],
                "answer": 0,
                "explanation": "Ikkalasi qoʻshilib, oʻn ikkita quti va "
                               "muzlatgichni beshinchi qavatga qoʻlda "
                               "koʻtarishga majbur qildi.",
            },
            {
                "text": "“울 지경이 되었다” — bu nimani anglatadi?",
                "choices": [
                    "Jiyon yigʻladi",
                    "Jiyon yigʻlab yuboradigan holga keldi — hali "
                    "yigʻlamagan, lekin bir qadam qolgan",
                    "Jiyon yigʻlashni xohlamadi",
                    "Jiyon oldin yigʻlagan edi",
                ],
                "answer": 1,
                "explanation": "(으)ㄹ 지경이다 — <b>chegara</b>. Ish hali "
                               "sodir boʻlmagan, shuning uchun oldida "
                               "(으)ㄹ turadi.",
            },
            {
                "text": "Kampirning gapidagi tasalli nimada?",
                "choices": [
                    "U koʻchishga yordam berishni taklif qildi",
                    "Bu holat hammaga tanish — “boshida hamma shunday, "
                    "bir oydan keyin oʻtib ketadi”",
                    "U Jiyonga pul berdi",
                    "U yangi lift oʻrnatishni vaʼda qildi",
                ],
                "answer": 1,
                "explanation": "“다 처음에는 <b>죽을 지경이에요</b>. 그런데 한 "
                               "달만 지나면 괜찮아요.” U ham 지경 soʻzini "
                               "ishlatadi — ammo oʻtkinchi narsa sifatida.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-88 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "사람들이 믿지 않았던 것들",
        "summary": (
            "PK-88 matni. “Bunday boʻlishi mumkin emas” — Kopernik, "
            "qoʻl yuvish va poyezd haqidagi uchta tarix, va bu jumlaning "
            "oʻzi haqidagi xulosa."
        ),
        "order":   88,
        "grammar": [
            {
                "pattern":  "(으)ㄹ 리가 없다 — …ishi mumkin emas",
                "meaning":  "Imkonsizlik emas, <b>ishonmaslik</b>. "
                            "리 (理) = aql, mantiq: “bunday boʻlishining "
                            "mantigʻi yoʻq”.",
                "examples": ["우리가 서 있는 땅이 움직일 리가 없어요.",
                             "우리 손이 사람을 죽일 리가 없어요."],
            },
            {
                "pattern":  "“그럴 리가 없다”고 하다",
                "meaning":  "PK-60 dagi koʻchirma gap bilan birga — "
                            "boshqalarning ishonmasligini bayon qilish. "
                            "Bu matnda uchala tarix ham shu jumla "
                            "ustiga qurilgan.",
                "examples": ["사람들은 “그럴 리가 없다”고 말한다."],
            },
            {
                "pattern":  "리가 없다 ↔ 수 없다",
                "meaning":  "수 없다 — imkoni yoʻq. 리가 없다 — imkon "
                            "bor, lekin men ishonmayman. Bu matndagi "
                            "odamlar hech narsani <b>rad qila "
                            "olmasdi</b> — ular faqat ishonmadi.",
                "examples": ["의사들은 화를 냈다. 그러나 숫자는 분명했다."],
            },
        ],
        "body": '''<p>새로운 생각은 처음에 거의 언제나 <span class="cn-word" data-pos="verb" data-tr="rad etiladi">거절당한다</span>. 이유는 간단하다. 사람들은 “그럴 <span class="cn-word" data-pos="adv" data-tr="boʻlishi mumkin emas">리가 없다</span>”고 말한다.</p>

<p>십육 세기에 <span class="cn-word" data-tr="Kopernik">코페르니쿠스</span>는 지구가 태양 <span class="cn-word" data-tr="atrofida">주위</span>를 <span class="cn-word" data-pos="verb" data-tr="aylanadi">돈다</span>고 말했다. 사람들은 웃었다. “우리가 서 있는 땅이 <span class="cn-word" data-pos="verb" data-tr="harakatlanishi mumkin emas">움직일 리가 없어요</span>.” 발 <span class="cn-word" data-tr="ostidagi">밑</span>의 땅은 조용했다. 아무도 움직임을 느끼지 못했다. 그 생각을 사람들이 <span class="cn-word" data-pos="verb" data-tr="qabul qilgunicha">받아들이기까지</span> 백 년이 넘게 걸렸다.</p>

<p>십구 세기 <span class="cn-word" data-tr="oʻrtalarida">중반</span>에 한 의사가 이상한 말을 했다. 이름은 <span class="cn-word" data-tr="Semmelveys">제멜바이스</span>였다. 그는 의사들에게 “손을 씻으세요”라고 했다. <span class="cn-word" data-tr="oʻsha davrda">당시</span> 병원에서 아기를 <span class="cn-word" data-pos="verb" data-tr="tugʻqan">낳은</span> 여성이 많이 죽었다. 제멜바이스는 의사들의 손이 <span class="cn-word" data-tr="sabab">원인</span>이라고 생각했다.</p>

<p><span class="cn-word" data-tr="hamkasb">동료</span> 의사들은 화를 냈다. “우리 손이 사람을 <span class="cn-word" data-pos="verb" data-tr="oʻldirishi mumkin emas">죽일 리가 없어요</span>. 우리는 의사예요.”</p>

<p>그러나 손을 씻은 <span class="cn-word" data-tr="boʻlim (kasalxonada)">병동</span>에서 <span class="cn-word" data-tr="oʻlim darajasi">사망률</span>이 십 퍼센트에서 일 퍼센트로 떨어졌다. 숫자는 <span class="cn-word" data-pos="adj" data-tr="aniq edi">분명했다</span>. 그래도 사람들은 믿지 않았다. 제멜바이스는 병원에서 <span class="cn-word" data-pos="verb" data-tr="haydab yuborildi">쫓겨났다</span>. 그가 <span class="cn-word" data-pos="adj" data-tr="haq edi">옳았다</span>. 그러나 사람들은 그가 죽은 후에 그것을 알았다.</p>

<p>기차도 마찬가지였다. 1830년대에 사람들은 이렇게 말했다. “<span class="cn-word" data-tr="soatiga">시속</span> 삼십 킬로미터로 달리면 사람이 <span class="cn-word" data-pos="verb" data-tr="nafas ololmaydi">숨을 못 쉴</span> 거예요.” 의사들도 그렇게 썼다. 물론 아무 일도 없었다.</p>

<p>이 세 이야기에는 같은 문장이 들어 있다. “그럴 리가 없다.”</p>

<p>이 말은 나쁜 말이 아니다. 우리는 매일 이 말을 쓴다. 그리고 <span class="cn-word" data-tr="koʻpchilik holda">대부분의 경우</span>에 이 말이 맞다. 이상한 이야기의 구십구 퍼센트는 정말 <span class="cn-word" data-tr="haqiqat">사실</span>이 아니다.</p>

<p>문제는 <span class="cn-word" data-tr="qolgan">나머지</span> 일 퍼센트다.</p>

<p>그래서 <span class="cn-word" data-tr="fan">과학</span>은 규칙을 하나 만들었다. 믿지 않아도 된다. 그러나 <span class="cn-word" data-tr="tekshirish">확인</span>은 해야 한다.</p>

<p>한 과학자는 이렇게 말했다. “‘그럴 리가 없어요’는 <span class="cn-word" data-tr="xulosa">결론</span>이 아니에요. <span class="cn-word" data-tr="savol">질문</span>이에요.”</p>''',
        "questions": [
            {
                "text": "Semmelveys nimani taklif qildi va natija qanday "
                        "boʻldi?",
                "choices": [
                    "Shifokorlar qoʻlini yuvsin dedi — oʻlim darajasi "
                    "10% dan 1% ga tushdi, lekin uni kasalxonadan "
                    "haydashdi",
                    "Yangi dori taklif qildi va boy boʻldi",
                    "Kasalxonani yopishni taklif qildi",
                    "Hech kim uning gapini eshitmadi",
                ],
                "answer": 0,
                "explanation": "Raqam aniq edi — 숫자는 분명했다 — lekin "
                               "“우리 손이 사람을 <b>죽일 리가 없어요</b>” "
                               "degan ishonch kuchliroq chiqdi.",
            },
            {
                "text": "Matnga koʻra, “그럴 리가 없다” yomon gapmi?",
                "choices": [
                    "Ha, uni hech qachon ishlatmaslik kerak",
                    "Yoʻq — koʻpchilik holda u toʻgʻri, gʻalati "
                    "gaplarning 99% haqiqatan yolgʻon",
                    "Ha, chunki u ilmiy emas",
                    "Matnda bu haqda aytilmagan",
                ],
                "answer": 1,
                "explanation": "“이 말은 나쁜 말이 아니다… 문제는 나머지 일 "
                               "퍼센트다.” Matn qolipni rad etmaydi — "
                               "uning chegarasini koʻrsatadi.",
            },
            {
                "text": "Olimning oxirgi gapi nimani anglatadi?",
                "choices": [
                    "Hech narsaga ishonmaslik kerak",
                    "“Bunday boʻlishi mumkin emas” — bu xulosa emas, "
                    "savol: ishonmasa ham, tekshirish kerak",
                    "Fan har doim haq",
                    "Odamlar hech qachon oʻzgarmaydi",
                ],
                "answer": 1,
                "explanation": "“믿지 않아도 된다. 그러나 확인은 해야 한다” — "
                               "matnning butun fikri shu ikki jumlada.",
            },
        ],
    },
]
