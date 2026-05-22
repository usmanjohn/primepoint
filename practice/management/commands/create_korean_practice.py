from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

QUESTIONS = [
    # --- Unit 1. Tenses ---
    {
        'text': "<p><strong>A: 지수 씨는 보통 주말에 무엇을 하십니까?<br>B: 저는 주로 공원에서 음악을 ________.</strong></p>",
        'explanation': "<p><strong>듣습니다</strong>: '듣다' (to listen) is a ㄷ-irregular verb, but before consonant endings like <code>-습니다</code>, the ㄷ does not change. Present Tense formal.</p>",
        'correct': "듣습니다",
        'choices': ["들습니다", "듣습니다", "들어요", "듣어요"]
    },
    {
        'text': "<p><strong>A: 요즘 날씨가 어때요?<br>B: 겨울이라서 바람이 많이 불고 무척 ________.</strong></p>",
        'explanation': "<p><strong>추워요</strong>: '춥다' (to be cold) is a ㅂ-irregular adjective. When adding <code>-아/어요</code>, ㅂ changes to 우. 춥다 → 추워요.</p>",
        'correct': "추워요",
        'choices': ["춥어요", "추워요", "추와요", "추웠어요"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 친구를 만났어요?<br>B: 네, 만나서 같이 맛있는 불고기를 ________.</strong></p>",
        'explanation': "<p><strong>먹었어요</strong>: The question asks about yesterday (어제), so the Past Tense <code>-았/었어요</code> is required. 먹다 → 먹었어요.</p>",
        'correct': "먹었어요",
        'choices': ["먹어요", "먹을 거예요", "먹고 있어요", "먹었어요"]
    },
    {
        'text': "<p><strong>A: 내일 방학인데 뭐 할 거예요?<br>B: 저는 가족들과 제주도로 여행을 ________.</strong></p>",
        'explanation': "<p><strong>갈 거예요</strong>: Refers to tomorrow (내일), so Future Tense <code>-(으)ㄹ 거예요</code> is used. 가다 → 갈 거예요.</p>",
        'correct': "갈 거예요",
        'choices': ["갔어요", "가고 있어요", "갈 거예요", "갑니다"]
    },
    {
        'text': "<p><strong>A: 지금 도서관에서 무엇을 해요?<br>B: 내일 시험이 있어서 한국어를 ________.</strong></p>",
        'explanation': "<p><strong>공부하고 있어요</strong>: The question asks about right now (지금), requiring the Progressive Tense <code>-고 있다</code>.</p>",
        'correct': "공부하고 있어요",
        'choices': ["공부했어요", "공부할 거예요", "공부하고 있어요", "공부해요"]
    },
    {
        'text': "<p><strong>A: 이 식당에 와 본 적이 있어요?<br>B: 네, 작년에 한 번 ________. 그런데 맛이 기억이 안 나요.</strong></p>",
        'explanation': "<p><strong>왔었어요</strong>: The speaker came in the past (작년) and the action is completely finished, so Past Perfect Tense <code>-았/었었어요</code> is natural here.</p>",
        'correct': "왔었어요",
        'choices': ["왔어요", "오고 있어요", "올 거예요", "왔었어요"]
    },
    {
        'text': "<p><strong>A: 수진 씨, 머리가 많이 기네요.<br>B: 네, 머리를 계속 ________.</strong></p>",
        'explanation': "<p><strong>기르고 있어요</strong>: '기르다' (to grow) is an 르-irregular verb, but with <code>-고 있다</code>, the root doesn't change.</p>",
        'correct': "기르고 있어요",
        'choices': ["길러요", "기르고 있어요", "길렀어요", "기를 거예요"]
    },
    {
        'text': "<p><strong>A: 이번 주말에 약속이 있어요?<br>B: 네, 친구를 ________.</strong></p>",
        'explanation': "<p><strong>만날 거예요</strong>: Refers to upcoming weekend plans, requiring Future Tense <code>-(으)ㄹ 거예요</code>.</p>",
        'correct': "만날 거예요",
        'choices': ["만났어요", "만나고 있어요", "만날 거예요", "만나요"]
    },
    {
        'text': "<p><strong>A: 어제 산 책이 어땠어요?<br>B: 내용이 아주 ________.</strong></p>",
        'explanation': "<p><strong>좋았어요</strong>: Asks about a past state (yesterday's book). Past Tense <code>-았/었어요</code> for the adjective 좋다.</p>",
        'correct': "좋았어요",
        'choices': ["좋아요", "좋고 있어요", "좋을 거예요", "좋았어요"]
    },
    {
        'text': "<p><strong>A: 민수 씨는 지금 어디에 있습니까?<br>B: 방에서 잠을 ________.</strong></p>",
        'explanation': "<p><strong>잡니다</strong>: Present Tense formal <code>-(스)ㅂ니다</code>. 자다 + ㅂ니다 = 잡니다.</p>",
        'correct': "잡니다",
        'choices': ["잘 겁니다", "잤습니다", "잡니다", "자고 있습니다"]
    },

    # --- Unit 2. Negative Expressions ---
    {
        'text': "<p><strong>A: 고기를 좋아하세요?<br>B: 아니요, 저는 고기를 ________. 채소만 먹어요.</strong></p>",
        'explanation': "<p><strong>안 먹어요</strong>: Expresses general negation or lack of intention. <code>안 A/V-아/어요</code> is appropriate.</p>",
        'correct': "안 먹어요",
        'choices': ["못 먹어요", "안 먹어요", "먹지 않아요", "안 먹었어요"]
    },
    {
        'text': "<p><strong>A: 어제 밤에 잠을 잘 잤어요?<br>B: 아니요, 밖이 너무 시끄러워서 한숨도 ________.</strong></p>",
        'explanation': "<p><strong>못 잤어요</strong>: The person wanted to sleep but couldn't due to external reasons (noise). <code>못 V-아/어요</code> is used for inability.</p>",
        'correct': "못 잤어요",
        'choices': ["안 잤어요", "못 잤어요", "자지 않았어요", "안 자요"]
    },
    {
        'text': "<p><strong>A: 이 가방이 무거워요?<br>B: 아니요, 생각보다 ________.</strong></p>",
        'explanation': "<p><strong>무겁지 않아요</strong>: <code>-지 않다</code> is the long form negation. For adjectives, we cannot use '못', so '안' or '-지 않다' is correct.</p>",
        'correct': "무겁지 않아요",
        'choices': ["무겁지 않아요", "못 무거워요", "무겁지 못해요", "무거웠어요"]
    },
    {
        'text': "<p><strong>A: 피아노를 칠 줄 알아요?<br>B: 아니요, 한 번도 배운 적이 없어서 ________.</strong></p>",
        'explanation': "<p><strong>치지 못해요</strong>: Lack of ability. Long form negation <code>-지 못하다</code>.</p>",
        'correct': "치지 못해요",
        'choices': ["안 쳐요", "치지 않아요", "치지 못해요", "못 쳤어요"]
    },
    {
        'text': "<p><strong>A: 오늘 회의에 참석할 수 있어요?<br>B: 죄송해요. 일이 너무 많아서 참석하지 ________.</strong></p>",
        'explanation': "<p><strong>못해요</strong>: Cannot attend due to workload. <code>V-지 못하다</code> is used to express inability.</p>",
        'correct': "못해요",
        'choices': ["않아요", "못해요", "안 해요", "없어요"]
    },
    {
        'text': "<p><strong>A: 지민 씨는 대학생이에요?<br>B: 아니요, 저는 대학생이 ________. 직장인이에요.</strong></p>",
        'explanation': "<p><strong>아니에요</strong>: Noun Negation (Word Negation). N이/가 아니다 is used to negate a noun.</p>",
        'correct': "아니에요",
        'choices': ["안 이에요", "못 이에요", "없어요", "아니에요"]
    },

    # --- Unit 3. Particles ---
    {
        'text': "<p><strong>A: 밖에 비가 와요?<br>B: 아니요, 지금은 비가 안 오고 ________ 와요.</strong></p>",
        'explanation': "<p><strong>눈이</strong>: Subject particle <code>이/가</code> is used with weather phenomena (눈이 오다). '눈' ends in a consonant, so '이' is used.</p>",
        'correct': "눈이",
        'choices': ["눈은", "눈을", "눈이", "눈도"]
    },
    {
        'text': "<p><strong>A: 직업이 무엇입니까?<br>B: ________ 한국어 선생님입니다.</strong></p>",
        'explanation': "<p><strong>저는</strong>: Topic particle <code>은/는</code> is used to introduce oneself or the main topic. '저' ends in a vowel, so '는'.</p>",
        'correct': "저는",
        'choices': ["내가", "저를", "저는", "제가"]
    },
    {
        'text': "<p><strong>A: 도서관에서 무엇을 빌렸어요?<br>B: 재미있는 역사 ________ 빌렸어요.</strong></p>",
        'explanation': "<p><strong>책을</strong>: Object particle <code>을/를</code>. '책' ends in a consonant, so '을'.</p>",
        'correct': "책을",
        'choices': ["책이", "책은", "책을", "책에"]
    },
    {
        'text': "<p><strong>A: 빵집에서 무엇을 샀어요?<br>B: 케이크________ 우유를 샀어요.</strong></p>",
        'explanation': "<p><strong>와</strong>: <code>와/과</code> means 'and' for nouns. '케이크' ends in a vowel, so '와' is used.</p>",
        'correct': "와",
        'choices': ["과", "와", "이나", "에"]
    },
    {
        'text': "<p><strong>A: 이 우산은 누구의 것이에요?<br>B: 제 ________ 우산이에요.</strong></p>",
        'explanation': "<p><strong>친구의</strong>: Possessive particle <code>의</code> indicates ownership.</p>",
        'correct': "친구의",
        'choices': ["친구가", "친구를", "친구의", "친구에"]
    },
    {
        'text': "<p><strong>A: 보통 언제 운동을 해요?<br>B: 저는 매일 아침________ 운동해요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Time particle <code>에 1</code> attaches to time nouns (아침, 1시, 등) to indicate when an action occurs.</p>",
        'correct': "에",
        'choices': ["에서", "은", "를", "에"]
    },
    {
        'text': "<p><strong>A: 내일 어디에 가요?<br>B: 친구를 만나러 명동________ 가요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Direction/Destination particle <code>에 2</code> is used with verbs like 가다, 오다.</p>",
        'correct': "에",
        'choices': ["을", "에서", "에", "까지"]
    },
    {
        'text': "<p><strong>A: 주말에 어디에서 데이트를 했어요?<br>B: 영화관________ 영화를 보고 밥을 먹었어요.</strong></p>",
        'explanation': "<p><strong>에서</strong>: Location particle <code>에서</code> indicates the place where an action takes place.</p>",
        'correct': "에서",
        'choices': ["에", "에서", "으로", "까지"]
    },
    {
        'text': "<p><strong>A: 회의는 언제 시작해요?<br>B: 오후 2시________ 4시까지 해요.</strong></p>",
        'explanation': "<p><strong>부터</strong>: Time range particle <code>부터</code> (from) is used with <code>까지</code> (to/until).</p>",
        'correct': "부터",
        'choices': ["에서", "부터", "에", "까지"]
    },
    {
        'text': "<p><strong>A: 집에서 학교까지 얼마나 걸려요?<br>B: 버스로 30분 ________ 걸려요.</strong></p>",
        'explanation': "<p><strong>쯤</strong>: Particle <code>쯤</code> means 'about' or 'approximately'.</p>",
        'correct': "쯤",
        'choices': ["만", "쯤", "도", "밖에"]
    },
    {
        'text': "<p><strong>A: 누구에게 편지를 썼어요?<br>B: 고향에 계신 부모님________ 썼어요.</strong></p>",
        'explanation': "<p><strong>께</strong>: Honorific form of <code>에게/한테</code> is <code>께</code>. Applied to respected people like parents.</p>",
        'correct': "께",
        'choices': ["에게", "한테", "께", "에서"]
    },
    {
        'text': "<p><strong>A: 수진 씨는 사과를 좋아해요?<br>B: 네, 사과를 좋아해요. 그리고 포도________ 좋아해요.</strong></p>",
        'explanation': "<p><strong>도</strong>: Particle <code>도</code> means 'also' or 'too', replacing 이/가 or 을/를.</p>",
        'correct': "도",
        'choices': ["를", "는", "만", "도"]
    },
    {
        'text': "<p><strong>A: 교실에 학생이 많아요?<br>B: 아니요, 오늘은 비가 와서 5명________ 안 왔어요.</strong></p>",
        'explanation': "<p><strong>밖에</strong>: Particle <code>밖에</code> (only/nothing but) must be followed by a negative verb.</p>",
        'correct': "밖에",
        'choices': ["만", "밖에", "도", "쯤"]
    },
    {
        'text': "<p><strong>A: 서울에서 부산까지 어떻게 가요?<br>B: 보통 KTX(기차)________ 가요.</strong></p>",
        'explanation': "<p><strong>로</strong>: Particle <code>(으)로</code> indicates means of transport or method. '기차' ends in a vowel, so '로'.</p>",
        'correct': "로",
        'choices': ["으로", "로", "에서", "에"]
    },
    {
        'text': "<p><strong>A: 목이 마른데 마실 것 좀 있어요?<br>B: 물________ 주스 중에 뭐 드릴까요?</strong></p>",
        'explanation': "<p><strong>이나</strong>: Particle <code>(이)나 1</code> means 'or' for nouns. '물' ends in a consonant, so '이나'.</p>",
        'correct': "이나",
        'choices': ["나", "이나", "도", "만"]
    },
    {
        'text': "<p><strong>A: 어제 술을 많이 마셨어요?<br>B: 네, 맥주를 5병________ 마셨어요.</strong></p>",
        'explanation': "<p><strong>이나</strong>: Particle <code>(이)나 2</code> expresses that the quantity is more than expected.</p>",
        'correct': "이나",
        'choices': ["이나", "밖에", "쯤", "만"]
    },
    {
        'text': "<p><strong>A: 지민 씨는 얼굴이 정말 작네요.<br>B: 네, 주먹________ 작아요.</strong></p>",
        'explanation': "<p><strong>만</strong>: Wait, for comparison <code>처럼, 같이</code> are used. 주먹만 해요 is possible but 주먹처럼 작아요 fits the basic level better. Let's use <code>처럼</code>.</p>",
        'correct': "처럼",
        'choices': ["처럼", "보다", "에", "에서"]
    },
    {
        'text': "<p><strong>A: 지하철이 빨라요, 버스가 빨라요?<br>B: 서울에서는 지하철이 버스________ 훨씬 빨라요.</strong></p>",
        'explanation': "<p><strong>보다</strong>: Particle <code>보다</code> is used for comparison (than).</p>",
        'correct': "보다",
        'choices': ["처럼", "까지", "보다", "부터"]
    },
    {
        'text': "<p><strong>A: 주말마다 등산을 가요?<br>B: 네, 일요일________ 산에 가요.</strong></p>",
        'explanation': "<p><strong>마다</strong>: Particle <code>마다</code> means 'every' or 'once every'. 일요일마다 = every Sunday.</p>",
        'correct': "마다",
        'choices': ["도", "만", "마다", "부터"]
    },
    {
        'text': "<p><strong>A: 요즘 다이어트 중이에요?<br>B: 네, 그래서 점심에는 샐러드________ 먹어요.</strong></p>",
        'explanation': "<p><strong>만</strong>: Particle <code>만</code> means 'only'. It is followed by a positive verb.</p>",
        'correct': "만",
        'choices': ["만", "밖에", "도", "나"]
    },

    # --- Unit 4. Listing and Contrast ---
    {
        'text': "<p><strong>A: 이 식당 음식이 어때요?<br>B: 가격도 싸________ 아주 맛있어요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Connector <code>-고</code> is used to list two parallel positive adjectives (싸다 + 고).</p>",
        'correct': "고",
        'choices': ["고", "거나", "지만", "는데"]
    },
    {
        'text': "<p><strong>A: 보통 주말에 뭐 하면서 쉬어요?<br>B: 집에서 책을 읽________ 음악을 들어요.</strong></p>",
        'explanation': "<p><strong>거나</strong>: Connector <code>-거나</code> is used to indicate a choice between two verbs (either read or listen).</p>",
        'correct': "거나",
        'choices': ["지만", "거나", "고", "는데"]
    },
    {
        'text': "<p><strong>A: 한국어 공부가 재미있어요?<br>B: 네, 조금 어렵________ 정말 재미있어요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: Connector <code>-지만</code> shows contrast (but). 어렵다 + 지만 = 어렵지만.</p>",
        'correct': "지만",
        'choices': ["고", "거나", "지만", "은데"]
    },
    {
        'text': "<p><strong>A: 밖은 날씨가 어때요?<br>B: 바람이 많이 부________ 춥지는 않아요.</strong></p>",
        'explanation': "<p><strong>는데</strong>: Connector <code>-(으)ㄴ/는데 1</code> introduces background info or soft contrast. 불다 is an ㄹ-irregular verb, so 불다 + 는데 = 부는데.</p>",
        'correct': "는데",
        'choices': ["는데", "은데", "고", "거나"]
    },
    {
        'text': "<p><strong>A: 언니는 키가 큰데, 동생은 어때요?<br>B: 동생은 키가 작________ 귀여워요.</strong></p>",
        'explanation': "<p><strong>은데</strong>: Connector <code>-(으)ㄴ/는데</code>. For adjectives ending in a consonant, use <code>-은데</code> (작다 -> 작은데).</p>",
        'correct': "은데",
        'choices': ["는데", "은데", "고", "지만"]
    },
    {
        'text': "<p><strong>A: 그 가방을 살 거예요?<br>B: 아니요. 디자인은 예쁘________ 너무 비싸서 안 살 거예요.</strong></p>",
        'explanation': "<p><strong>지만</strong>: <code>-지만</code> clearly contrasts '예쁘다' (pretty) and '비싸다' (expensive).</p>",
        'correct': "지만",
        'choices': ["고", "거나", "지만", "아서"]
    },

    # --- Unit 5. Time Expressions ---
    {
        'text': "<p><strong>A: 약을 언제 먹어야 해요?<br>B: 밥을 먹________ 꼭 드세요.</strong></p>",
        'explanation': "<p><strong>기 전에</strong>: <code>V-기 전에</code> means 'before doing'. 밥을 먹기 전에 = before eating a meal.</p>",
        'correct': "기 전에",
        'choices': ["은 후에", "고 나서", "기 전에", "아서"]
    },
    {
        'text': "<p><strong>A: 영화를 본 후에 뭐 할 거예요?<br>B: 영화가 끝난 ________ 커피를 마실 거예요.</strong></p>",
        'explanation': "<p><strong>후에</strong>: <code>V-(으)ㄴ 후에</code> means 'after doing'. 끝나다 + ㄴ 후에 = 끝난 후에.</p>",
        'correct': "후에",
        'choices': ["전에", "후에", "때", "고 나서"]
    },
    {
        'text': "<p><strong>A: 손은 언제 씻어야 해요?<br>B: 밖에서 돌아오________ 반드시 씻으세요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: <code>V-고 나서</code> emphasizes the sequence 'upon finishing X, do Y'.</p>",
        'correct': "고 나서",
        'choices': ["고 나서", "기 전에", "을 때", "지만"]
    },
    {
        'text': "<p><strong>A: 어제 저녁에 뭐 했어요?<br>B: 친구를 만________ 같이 피자를 먹었어요.</strong></p>",
        'explanation': "<p><strong>나서</strong>: <code>V-아/어서</code> indicates temporal sequence where the first action is a prerequisite for the second (met a friend, then ate together).</p>",
        'correct': "나서",
        'choices': ["나고", "나서", "난 후에", "나기 전에"]
    },
    {
        'text': "<p><strong>A: 언제 한국 노래를 자주 들어요?<br>B: 저는 기분이 좋________ 한국 노래를 들어요.</strong></p>",
        'explanation': "<p><strong>을 때</strong>: <code>A/V-(으)ㄹ 때</code> expresses the time when something happens. 좋다 + 을 때 = 좋을 때.</p>",
        'correct': "을 때",
        'choices': ["을 때", "기 전에", "은 후에", "고 나서"]
    },
    {
        'text': "<p><strong>A: 학생이________ 공부를 열심히 했어요?<br>B: 네, 도서관에서 살다시피 했어요.</strong></p>",
        'explanation': "<p><strong>었을 때</strong>: For past states with nouns, <code>N이었/였을 때</code> is used. 학생 + 이었을 때.</p>",
        'correct': "이었을 때",
        'choices': ["일 때", "이었을 때", "인 후에", "이기 전에"]
    },
    {
        'text': "<p><strong>A: 이 빵은 어떻게 만들어요?<br>B: 밀가루 반죽을 오븐에 구________ 설탕을 뿌리세요.</strong></p>",
        'explanation': "<p><strong>운 후에</strong>: 굽다 (to bake) is a ㅂ-irregular verb. 굽다 + (으)ㄴ 후에 = 구운 후에.</p>",
        'correct': "운 후에",
        'choices': ["운 후에", "은 후에", "기 전에", "고 나서"]
    },
    {
        'text': "<p><strong>A: 너무 바쁘면 도와줄까요?<br>B: 괜찮아요. 제가 너무 바________ 말할게요.</strong></p>",
        'explanation': "<p><strong>쁠 때</strong>: 바쁘다 (busy) + ㄹ 때 = 바쁠 때.</p>",
        'correct': "쁠 때",
        'choices': ["빠서", "쁠 때", "쁜 후에", "쁘기 전에"]
    },

    # --- Expanding remaining to hit 50 total (More advanced mixes from Units 1-5) ---
    {
        'text': "<p><strong>A: 지수 씨, 지금 음악을 ________?<br>B: 네, 좋아하는 가수의 신곡이 나와서요.</strong></p>",
        'explanation': "<p><strong>듣고 있어요</strong>: 듣다 (irregular) + 고 있다 = 듣고 있어요.</p>",
        'correct': "듣고 있어요",
        'choices': ["들고 있어요", "듣고 있어요", "들어 있어요", "듣었어요"]
    },
    {
        'text': "<p><strong>A: 매운 음식을 잘 먹어요?<br>B: 아니요, 저는 매운 것을 전혀 ________.</strong></p>",
        'explanation': "<p><strong>못 먹어요</strong>: '전혀 못 먹다' emphasizes complete inability.</p>",
        'correct': "못 먹어요",
        'choices': ["안 먹어요", "못 먹어요", "먹지 않아요", "안 먹었어요"]
    },
    {
        'text': "<p><strong>A: 제주도는 어떤 점이 좋아요?<br>B: 바다가 아름답________ 공기가 맑아요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Listing two good qualities using <code>-고</code>.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 버스가 왜 안 오죠?<br>B: 눈이 너무 많이 와서 차가 막히________ 같아요.</strong></p>",
        'explanation': "<p><strong>는 것</strong>: Wait, '는 것 같다' is not in Unit 1-5. Let's use <code>-(으)니까</code> - wait, not in list either. Let's adapt to Unit 4 <code>-(으)ㄴ/는데</code>: 차가 많이 막히는데 지하철을 탈까요?</p>",
        'correct': "막히는데",
        'choices': ["막히고", "막히는데", "막히거나", "막히지만"]
    },
    {
        'text': "<p><strong>A: 김치찌개를 만들 줄 알아요?<br>B: 네, 먼저 고기를 볶________ 물을 넣고 끓이세요.</strong></p>",
        'explanation': "<p><strong>고 나서</strong>: Indicates sequence. 볶다 + 고 나서.</p>",
        'correct': "고 나서",
        'choices': ["기 전에", "고 나서", "지만", "을 때"]
    },
    {
        'text': "<p><strong>A: 저 식당은 어때요?<br>B: 음식이 맛없________ 서비스도 별로예요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Listing negative attributes.</p>",
        'correct': "고",
        'choices': ["고", "지만", "은데", "어서"]
    },
    {
        'text': "<p><strong>A: 언제 고향에 돌아갈 거예요?<br>B: 대학교를 졸업한 ________ 돌아갈 계획이에요.</strong></p>",
        'explanation': "<p><strong>후에</strong>: 졸업하다 + ㄴ 후에 = 졸업한 후에.</p>",
        'correct': "후에",
        'choices': ["전에", "후에", "때", "고 나서"]
    },
    {
        'text': "<p><strong>A: 감기에 걸려서 목이 아파요.<br>B: 따뜻한 물을 많이 마시________ 약을 드세요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Two connected advice points.</p>",
        'correct': "고",
        'choices': ["고", "지만", "거나", "는데"]
    },
    {
        'text': "<p><strong>A: 어제 일찍 잤어요?<br>B: 숙제가 너무 많아서 새벽 2시________ 못 잤어요.</strong></p>",
        'explanation': "<p><strong>까지</strong>: Time particle until 2 AM.</p>",
        'correct': "까지",
        'choices': ["부터", "까지", "에", "에서"]
    },
    {
        'text': "<p><strong>A: 요즘 매일 수영장에 가요?<br>B: 아니요, 시간이 없어서 일주일________ 한 번 가요.</strong></p>",
        'explanation': "<p><strong>에</strong>: Time particle indicating frequency (일주일에 한 번 - once a week).</p>",
        'correct': "에",
        'choices': ["에", "에서", "으로", "까지"]
    },
    {
        'text': "<p><strong>A: 이 신발은 너무 작지 않아요?<br>B: 아니요, 제 발에 아주 ________.</strong></p>",
        'explanation': "<p><strong>잘 맞아요</strong>: Present tense A/V-아/어요.</p>",
        'correct': "맞아요",
        'choices': ["맞아요", "맞았어요", "맞을 거예요", "맞고 있어요"]
    },
    {
        'text': "<p><strong>A: 주말에 여행을 갈 거예요?<br>B: 날씨가 맑으면 가________ 비가 오면 안 갈 거예요.</strong></p>",
        'explanation': "<p><strong>고</strong>: Linking two contrasting clauses smoothly. Or <code>-지만</code> if strong contrast.</p>",
        'correct': "고",
        'choices': ["고", "거나", "은데", "어서"]
    },
    {
        'text': "<p><strong>A: 강아지가 참 귀엽네요.<br>B: 네, 솜사탕________ 털이 푹신푹신해요.</strong></p>",
        'explanation': "<p><strong>처럼</strong>: N처럼 (like a noun) used for metaphor.</p>",
        'correct': "처럼",
        'choices': ["보다", "처럼", "만큼", "도"]
    },
    {
        'text': "<p><strong>A: 오늘 회식에 올 수 있어요?<br>B: 미안해요. 선약이 있어서 가지 ________.</strong></p>",
        'explanation': "<p><strong>못해요</strong>: Long negative for inability (가지 못하다).</p>",
        'correct': "못해요",
        'choices': ["않아요", "못해요", "안 해요", "없어요"]
    },
    {
        'text': "<p><strong>A: 어렸을 때 시골에 살았어요?<br>B: 네, 10살________ 할머니 댁에서 지냈어요.</strong></p>",
        'explanation': "<p><strong>때</strong>: N때 indicates time in the past.</p>",
        'correct': "때",
        'choices': ["전에", "후에", "때", "까지"]
    },
    {
        'text': "<p><strong>A: 내일 몇 시에 만날까요?<br>B: 3시________ 만나는 게 어때요?</strong></p>",
        'explanation': "<p><strong>쯤</strong>: 쯤 means approximately/around.</p>",
        'correct': "쯤",
        'choices': ["만", "쯤", "밖에", "도"]
    },
    {
        'text': "<p><strong>A: 혼자 밥을 먹었어요?<br>B: 아니요, 룸메이트________ 같이 먹었어요.</strong></p>",
        'explanation': "<p><strong>랑</strong>: N(이)랑 means 'with'.</p>",
        'correct': "랑",
        'choices': ["를", "랑", "에", "이나"]
    },
    {
        'text': "<p><strong>A: 무슨 과일을 좋아해요?<br>B: 저는 딸기________ 바나나를 좋아해요.</strong></p>",
        'explanation': "<p><strong>와</strong>: N와/과 means 'and'.</p>",
        'correct': "와",
        'choices': ["과", "와", "도", "를"]
    },
    {
        'text': "<p><strong>A: 기차표를 예매했어요?<br>B: 깜빡했어요. 내일 아침에 일어나________ 바로 할게요.</strong></p>",
        'explanation': "<p><strong>자마자</strong>: Wait, 자마자 is not Unit 1-5. Let's use <code>아/어서</code> or <code>고 나서</code>: 일어나고 나서 할게요.</p>",
        'correct': "고 나서",
        'choices': ["기 전에", "고 나서", "지만", "을 때"]
    },
    {
        'text': "<p><strong>A: 저는 한국 드라마가 참 재미있어요.<br>B: 그래요? 저________ 한국 드라마를 자주 봐요.</strong></p>",
        'explanation': "<p><strong>도</strong>: 도 (also/too) is used to show agreement.</p>",
        'correct': "도",
        'choices': ["는", "만", "도", "가"]
    }
]

class Command(BaseCommand):
    help = 'Create a Korean grammar particle practice test'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign this practice to')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options['master'])
        except User.DoesNotExist:
            raise CommandError(f"User '{options['master']}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{options['master']}'.")

        subject, _ = Subject.objects.get_or_create(
            name='한국어',
            defaults={'description': '한국어 문법 및 어휘 연습'},
        )

        practice, created = Practice.objects.get_or_create(
            title='Takrorlash',  # --- IGNORE ---
            master=master,
            defaults={
                'description': 'Tarixdan o\'rganamiz',
                'subject': subject,
                'level': 'medium',
                'is_free': True,
                'is_published': True,
                'is_available_for_all': True,
                'pass_score': 70,
                'max_attempts': 0,
                'show_answers_after': True,
            },
        )

        if not created:
            self.stdout.write(self.style.WARNING(
                f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
            ))
            return

        for i, q in enumerate(QUESTIONS, start=1):
            question = PracticeQuestion.objects.create(
                practice=practice,
                question_text=q['text'],
                explanation=q['explanation'],
                order=i,
                points=1,
            )
            for choice_text in q['choices']:
                PracticeChoice.objects.create(
                    question=question,
                    text=choice_text,
                    is_correct=(choice_text == q['correct']),
                )

        self.stdout.write(self.style.SUCCESS(
            f"Created practice '{practice.title}' with {len(QUESTIONS)} questions (id={practice.pk})."
        ))
