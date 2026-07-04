from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

questions = [
    {
        'text': "<p>A: 아침에 늦잠을 자서 서두르다가 빗길에 미끄러져서 <u>하마터면</u> 큰 사고가 ________.<br>B: 정말 큰일 날 뻔했네요! 다치지 않아서 다행이에요.</p>",
        'explanation': "<p><strong>날 뻔했어요</strong>: 하마터면(deyarli) ravishi bilan kelib, nomaqbul yoki xavfli voqea sodir bo'lishiga juda oz qolganini (lekin sodir bo'lmaganini) bildiradi.</p>",
        'correct': "날 뻔했어요",
        'choices': ["날 뻔했어요", "나는 셈이에요", "나고 말았어요", "나기 마련이에요"]
    },
    {
        'text': "<p>A: 민수 씨, 이번 프로젝트 준비는 거의 다 끝나 가나요?<br>B: 네, 아주 작은 마무리 작업만 남았으니 <u>사실상</u> 다 ________.</p>",
        'explanation': "<p><strong>끝난 셈이에요</strong>: Hali to'liq tugamagan bo'lsa-da, vaziyat va natijaga ko'ra deyarli tugagan deb hisoblash mumkinligini anglatadi.</p>",
        'correct': "끝난 셈이에요",
        'choices': ["끝날수록 좋아요", "끝나 버렸어요", "끝난 셈이에요", "끝날 뻔했어요"]
    },
    {
        'text': "<p>A: 이번 한국어 능력 시험은 어땠어요? 합격할 것 같아요?<br>B: 원래 실력보다 훨씬 못 봐서 아예 시험을 <u>완전히</u> ________ 속상해요.</p>",
        'explanation': "<p><strong>망쳐 버려서</strong>: Harakat butunlay tugaganini va buning natijasida so'zlovchida afsus yoki achinish hissi borligini ifodalaydi.</p>",
        'correct': "망쳐 버려서",
        'choices': ["망칠수록", "망쳐 버려서", "망치는 셈이라", "망칠 뻔해서"]
    },
    {
        'text': "<p>A: 새로 이사한 동네는 살기에 좀 어때요? 불편하지 않아요?<br>B: 아니요, 교통도 편리하고 편의 시설도 많아서 예전 살던 곳________ 편안해요.</p>",
        'explanation': "<p><strong>이나 다름없을 정도로</strong>: Ikki narsa o'rtasida deyarli farq yo'q ekanligini, bir xil ekanligini ko'rsatadi.</p>",
        'correct': "이나 다름없을 정도로",
        'choices': ["이나 마찬가지일 뻔해서", "이나 다름없을 정도로", "일수록", "여 버려서"]
    },
    {
        'text': "<p>A: 외국어 공부는 처음에 열심히 하다가도 중간에 포기하게 돼요.<br>B: 맞아요. 외국어는 매일 <u>꾸준히</u> ________ 실력이 더 늘어나는 것 같아요.</p>",
        'explanation': "<p><strong>연습할수록</strong>: Biror harakat yoki holatning darajasi ortgani sayin, keyingi natija ham shunga mos ravishda o'zgarishini bildiradi.</p>",
        'correct': "연습할수록",
        'choices': ["연습하는 셈이라", "연습할 뻔해서", "연습해 버려서", "연습할수록"]
    },
    {
        'text': "<p>A: 어제 산 명품 가방이 벌써 흠집이 나서 속상해 죽겠어요.<br>B: 아이고, 애지중지하던 가방인데 <u>기어이</u> 흠집이 ________ 마음이 아프겠네요.</p>",
        'explanation': "<p><strong>나 버려서</strong>: Istalmagan ishning butunlay sodir bo'lib bo'lganini va afsuslanishni anglatadi.</p>",
        'correct': "나 버려서",
        'choices': ["나 버려서", "날 뻔해서", "나는 셈이라", "나기 마찬가지라"]
    },
    {
        'text': "<p>A: 정우 씨와 영미 씨는 아직 결혼 안 했지요?<br>B: 네, 하지만 양가 부모님 동의도 얻었고 다음 달에 식을 올리니 거의 ________.</p>",
        'explanation': "<p><strong>결혼한 거나 다름없어요</strong>: Rasman nikohdan o'tishmagan bo'lsa-da, amalda er-xotin kabi ekanliklarini bildiradi.</p>",
        'correct': "결혼한 거나 다름없어요",
        'choices': ["결혼할 뻔했어요", "결혼한 거나 다름없어요", "결혼해 버렸어요", "결혼할수록 좋아요"]
    },
    {
        'text': "<p>A: 저 선수는 나이가 아주 어린데도 경기를 정말 노련하게 운영하네요.<br>B: 맞아요. 나이는 어리지만 실력만큼은 베테랑 베테랑 ________.</p>",
        'explanation': "<p><strong>선수나 마찬가지예요</strong>: Boshqa biror narsa bilan solishtirganda hech qanday farqi yo'q, bir xil qiymatga ega degan ma'noni ifodalaydi.</p>",
        'correct': "선수나 마찬가지예요",
        'choices': ["선수일 셈이에요", "선수일 뻔했어요", "선수나 마찬가지예요", "선수여 버렸어요"]
    },
    {
        'text': "<p>A: 어제 눈이 너무 많이 와서 계단에서 <u>자칫</u> 구를 ________.<br>B: 정말 위험했겠네요. 겨울철엔 항상 발밑을 조심해야 해요.</p>",
        'explanation': "<p><strong>뻔했어요</strong>: Xavfli vaziyat yuz berishiga juda oz qolganini, xayriyatki sodir bo'lmaganini bildiradi.</p>",
        'correct': "뻔했어요",
        'choices': ["뻔했어요", "셈이었어요", "버렸어요", "다름없었어요"]
    },
    {
        'text': "<p>A: 이번 달은 경조사가 많아서 월급을 거의 다 <u>모조리</u> ________ 남은 돈이 없어요.<br>B: 아이고, 다음 달 월급날까지 허리띠를 졸라매야겠네요.</p>",
        'explanation': "<p><strong>써 버려서</strong>: Pullarni butunlay ishlatib tugatganlik va buning ortidan kelgan pushaymonlikni ifodalaydi.</p>",
        'correct': "써 버려서",
        'choices': ["쓸수록", "써 버려서", "쓰는 셈이라", "쓸 뻔해서"]
    },
    {
        'text': "<p>A: 고향에 계신 부모님께 매달 용돈을 얼마나 보내 드려요?<br>B: 매달 50만 원씩 보내 드리니까 1년이면 600만 원을 ________.</p>",
        'explanation': "<p><strong>보내는 셈이에요</strong>: Umumiy hisob-kitob yoki natijaga ko'ra shunday xulosaga kelish mumkinligini anglatadi.</p>",
        'correct': "보내는 셈이에요",
        'choices': ["보내는 셈이에요", "보낼 뻔했어요", "보내 버렸어요", "보낼수록 좋아요"]
    },
    {
        'text': "<p>A: 요즘 한국어 말하기 연습을 하는데 생각보다 너무 어려워요.<br>B: 낙담하지 마세요. 언어는 <u>자주</u> 입 밖으로 ________ 자연스러워지는 법이에요.</p>",
        'explanation': "<p><strong>소리 낼수록</strong>: Gapirish, takrorlash harakati ko'paygani sayin natija ham yaxshilanib borishini bildiradi.</p>",
        'correct': "소리 낼수록",
        'choices': ["소리 내는 셈이라", "소리 낼 뻔해서", "소리 내 버려서", "소리 낼수록"]
    },
    {
        'text': "<p>A: 이번에 새로 출시된 스마트폰 기능이 정말 혁신적이네요.<br>B: 네, 손안에 작은 컴퓨터를 ________ 정도로 훌륭해요.</p>",
        'explanation': "<p><strong>들고 다니는 것이나 다름없을</strong>: Telefonni kompyuter bilan bir xil darajada deb hisoblash mumkinligini anglatadi.</p>",
        'correct': "들고 다니는 것이나 다름없을",
        'choices': ["들고 다니는 것이나 다름없을", "들고 다닐 뻔할", "들고 다니는 셈일", "들고 다니는 것이나 마찬가지일"]
    },
    {
        'text': "<p>A: 아까 횡단보도에서 휴대폰을 보며 걷다가 달려오는 자전거에 ________.<br>B: 큰일 날 뻔했네요! 길을 걸을 때는 휴대폰을 절대 보면 안 돼요.</p>",
        'explanation': "<p><strong>부딪힐 뻔했어요</strong>: To'qnashib ketishiga bir baxya qolganini anglatadi.</p>",
        'correct': "부딪힐 뻔했어요",
        'choices': ["부딪히는 셈이었어요", "부딪힐수록 좋았어요", "부딪혀 버렸어요", "부딪힐 뻔했어요"]
    },
    {
        'text': "<p>A: 수미 씨, 오늘 왜 이렇게 기분이 안 좋아 보여요?<br>B: 아침에 출근하다가 소중한 지갑을 <u>어디론가</u> 잃어 ________ 속상해서 그래요.</p>",
        'explanation': "<p><strong>버려 가지고</strong>: Yo'qotib qo'yganlik va buning salbiy ta'sirini ko'rsatadi.</p>",
        'correct': "버려 가지고",
        'choices': ["버릴 뻔해서", "버려 가지고", "버리는 셈이라", "버릴수록"]
    },
    {
        'text': "<p>A: 이번 시험 범위가 너무 넓어서 다 공부하지 못할 것 같아요.<br>B: 너무 걱정 마세요. 중요한 핵심 노트만 확실히 외우면 전체를 다 ________.</p>",
        'explanation': "<p><strong>공부한 거나 마찬가지니까요</strong>: Muhim joylarini o'qish orqali hammasini o'qigandek natijaga erishish mumkinligini bildiradi.</p>",
        'correct': "공부한 거나 마찬가지니까요",
        'choices': ["공부할수록 유리하니까요", "공부한 거나 마찬가지니까요", "공부하는 셈이니까요", "공부할 뻔했으니까요"]
    },
    {
        'text': "<p>A: 진우 씨는 주말마다 봉사활동을 하러 간다면서요?<br>B: 네, 매주 거르지 않고 가니까 1년 중 한 달은 봉사활동을 하며 ________이죠.</p>",
        'explanation': "<p><strong>보내는 셈</strong>: Vaqt hisoblab ko'rilganda, amalda bir oyni shu ishga bag'ishlagan deb xulosa qilish mumkinligini bildiradi.</p>",
        'correct': "보내는 셈",
        'choices': ["보내는 셈", "보낼 뻔", "보내 버림", "보낼수록"]
    },
    {
        'text': "<p>A: 클래식 음악은 들을 때 지루하지 않나요?<br>B: 아녜요. 신기하게도 클래식은 <u>깊이</u> ________ 그 매력에 더 빠져들게 돼요.</p>",
        'explanation': "<p><strong>들을수록</strong>: Tinglash chuqurlashgani sayin maftunkorligi ortishini ifodalaydi.</p>",
        'correct': "들을수록",
        'choices': ["듣는 셈일수록", "들으려던 참일수록", "들 을수록", "들을수록"]
    },
    {
        'text': "<p>A: 어제 약속 시간에 늦을까 봐 택시를 탔는데 길을 잘못 들어서 <u>오히려</u> 지각을 ________.<br>B: 저런, 돈은 돈대로 쓰고 마음 고생만 하셨겠네요.</p>",
        'explanation': "<p><strong>해 버렸어요</strong>: Kechikishni xohlamagan bo'lsa ham, yakunda baribir butunlay kechikib qolganini ifodalaydi.</p>",
        'correct': "해 버렸어요",
        'choices': ["할 뻔했어요", "해 버렸어요", "하는 셈이었어요", "할수록 나빴어요"]
    },
    {
        'text': "<p>A: 두 사람이 사귄 지 오래되었는데 아직 프러포즈는 안 받았나요?<br>B: 형식적인 절차만 없을 뿐이지, 이미 가족끼리도 다 아는 사이라 ________ 없어요.</p>",
        'explanation': "<p><strong>부부나 다름</strong>: Rasmiy nikohsiz ham amalda er-xotindan hech qanday farqi yo'qligini bildiradi.</p>",
        'correct': "부부나 다름",
        'choices': ["부부일 셈", "부부나 다름", "부부일 뻔", "부부여 버림"]
    },
    {
        'text': "<p>A: 마라톤 경기를 하다가 도중에 다리에 쥐가 나서 <u>하마터면</u> 완주를 ________.<br>B: 그래도 끝까지 포기하지 않고 달려서 완주하셨다니 정말 대단해요!</p>",
        'explanation': "<p><strong>포기할 뻔했어요</strong>: Taslim bo'lishga juda yaqin kelgani, lekin yakunda taslim bo'lmaganini anglatadi.</p>",
        'correct': "포기할 뻔했어요",
        'choices': ["포기해 버렸어요", "포기할 뻔했어요", "포기하는 셈이었어요", "포기할수록 힘들었어요"]
    },
    {
        'text': "<p>A: 이 소설책은 읽기가 너무 지루하고 재미없는 것 같아요.<br>B: 원래 고전 소설은 뒤로 ________ 흥미진진한 사건이 많이 나와요.</p>",
        'explanation': "<p><strong>갈수록</strong>: Kitobni o'qib olg'a ilgarilagan sayin qiziqarli bo'lishini ko'rsatadi.</p>",
        'correct': "갈수록",
        'choices': ["갈수록", "가 버릴수록", "가는 셈일수록", "갈 뻔할수록"]
    },
    {
        'text': "<p>A: 어제 밤새워 작성한 기획서 파일을 실수로 저장 안 하고 <u>그냥</u> 창을 닫아 ________.<br>B: 헉! 다시 복구할 수 있는 방법은 없는 건가요?</p>",
        'explanation': "<p><strong>버렸지 뭐예요</strong>: Saqlamasdan yopib yuborganlikdek mudhish xato butunlay sodir bo'lganini bildiradi.</p>",
        'correct': "버렸지 뭐예요",
        'choices': ["버릴 뻔했어요", "버렸지 뭐예요", "버리는 셈이에요", "버릴수록 문제예요"]
    },
    {
        'text': "<p>A: 지수 씨 부모님은 강아지를 친자식처럼 끔찍하게 아끼시네요.<br>B: 네, 마당에서 키우는 반려견이 아니라 이제는 정말 ________ 없대요.</p>",
        'explanation': "<p><strong>막내아들이나 다름</strong>: Kuchukchani o'zlarining kenja o'g'lidek ko'rishini anglatadi.</p>",
        'correct': "막내아들이나 다름",
        'choices': ["막내아들일 셈", "막내아들이나 마찬가지", "막내아들이나 다름", "막내아들일 뻔"]
    },
    {
        'text': "<p>A: 지난달부터 시작한 수영 강습은 매주 열심히 가고 있어요?<br>B: 한 주도 빠짐없이 출석했으니 이번 달 목표는 완전히 ________이죠.</p>",
        'explanation': "<p><strong>달성한 셈</strong>: Natijaga qarab maqsad to'liq amalga oshdi deb hisoblash mumkinligini ifodalaydi.</p>",
        'correct': "달성한 셈",
        'choices': ["달성한 셈", "달성할 뻔", "달성해 버림", "달성할수록"]
    },
    {
        'text': "<p>A: 오늘 아침 일어났는데 머리가 너무 아프고 열이 심하게 났어요.<br>B: 저런, 자칫 독감에 걸려 ________ 결근할 뻔했네요. 병원엔 다녀왔어요?</p>",
        'explanation': "<p><strong>버려서</strong>: Kasal bo'lib qolganlik va buning oqibatida yomon holat yuzaga kelganini ifodalaydi.</p>",
        'correct': "버려서",
        'choices': ["버리는 바람에", "버릴수록", "버려서", "버릴 뻔해서"]
    },
    {
        'text': "<p>A: 친구에게 비밀 이야기를 했는데, 그 친구가 다른 사람에게 <u>홀랑</u> 말해 ________ 속상해요.<br>B: 믿었던 친구인데 정말 배신감이 컸겠어요.</p>",
        'explanation': "<p><strong>버려서</strong>: Sirni butunlay aytib qo'yganlik va afsuslanish ma'nosini beradi.</p>",
        'correct': "버려서",
        'choices': ["버려서", "버릴 뻔해서", "버리는 셈이라", "버릴수록"]
    },
    {
        'text': "<p>A: 이번 주말에 캠핑 가기로 했는데 날씨가 계속 흐리네요.<br>B: 일기예보를 보니 주말에 비가 올 확률이 95%래요. 이번 캠핑은 ________ 취소된 거나 마찬가지예요.</p>",
        'explanation': "<p><strong>사실상</strong>: Amalda kampning bekor qilingani bilan bir xil ekanligini anglatadi.</p>",
        'correct': "사실상",
        'choices': ["하마터면", "갈수록", "사실상", "갑자기"]
    },
    {
        'text': "<p>A: 이 가구는 조립하기가 너무 복잡하고 설명서도 어렵네요.<br>B: 설명서 그림을 <u>자세히</u> ________ 조립 방법이 조금씩 이해가 갈 거예요.</p>",
        'explanation': "<p><strong>볼수록</strong>: Diqqat bilan qarash darajasi ortgani sari tushunish osonlashishini bildiradi.</p>",
        'correct': "볼수록",
        'choices': ["보는 셈이라", "볼 뻔해서", "봐 버려서", "볼수록"]
    },
    {
        'text': "<p>A: 운전면허 시험에서 아깝게 1점 차이로 떨어졌다면서요?<br>B: 네, 조금만 더 주의했으면 합격할 수 있었는데 ________ 아쉬워요.</p>",
        'explanation': "<p><strong>떨어져 버려서</strong>: Yeqilib bo'lganlik va buning g'am-gussasini ifodalaydi.</p>",
        'correct': "떨어져 버려서",
        'choices': ["떨어질 뻔해서", "떨어지는 셈이라", "떨어져 버려서", "떨어질수록"]
    },
    {
        'text': "<p>A: 해외여행을 가려고 몇 달 동안 엔화를 <u>조금씩</u> 환전해 두었어요.<br>B: 와, 매달 조금씩 바꾼 것이 합치니까 큰돈이 ________.</p>",
        'explanation': "<p><strong>된 셈이네요</strong>: Kichik pullar yig'ilib, natijada katta pulga aylangan deb hisoblash mumkinligini bildiradi.</p>",
        'correct': "된 셈이네요",
        'choices': ["될 뻔했네요", "된 셈이네요", "되 버렸네요", "될수록 좋네요"]
    },
    {
        'text': "<p>A: 어제 요리하다가 칼에 손가락을 베여서 피가 많이 났어요.<br>B: 조심하셔야죠. <u>자칫</u> 손가락을 크게 ________.</p>",
        'explanation': "<p><strong>다칠 뻔했잖아요</strong>: Yaxshiyamki chuqur jarohat bo'lmaganini, lekin xavf yuqori bo'lganini ko'rsatadi.</p>",
        'correct': "다칠 뻔했잖아요",
        'choices': ["다치는 셈이잖아요", "다쳐 버렸잖아요", "다칠수록 좋잖아요", "다칠 뻔했잖아요"]
    },
    {
        'text': "<p>A: 수영을 배운 지 벌써 3년이나 되었다고 하셨죠?<br>B: 네, 실력은 아직 부족하지만 기간으로만 보면 전문가 ________ 없어요.</p>",
        'explanation': "<p><strong>나 다름</strong>: Vaqt nuqtai nazaridan professionallardan qolishmasligini anglatadi.</p>",
        'correct': "나 다름",
        'choices': ["일 셈", "나 마찬가지", "나 다름", "일 뻔"]
    },
    {
        'text': "<p>A: 새로 이사한 아파트는 층간소음 문제가 심하지 않나요?<br>B: <u>워낙</u> 방음이 잘 안 돼서 이웃집 말소리가 다 들려요. 길거리에서 ________ 살고 있어요.</p>",
        'explanation': "<p><strong>자는 거나 마찬가지로</strong>: Uy ichida ko'chadagidek shovqin ekanini o'xshatish orqali ifodalaydi.</p>",
        'correct': "자는 거나 마찬가지로",
        'choices': ["잘 뻔하게", "자는 셈 치고", "자는 거나 마찬가지로", "자 버릴수록"]
    },
    {
        'text': "<p>A: 이번 세미나에 참석하는 인원이 얼마나 되나요?<br>B: 전체 회원 50명 중에 45명이 신청했으니 거의 다 ________.</p>",
        'explanation': "<p><strong>참석하는 셈이에요</strong>: Deyarli hamma kelishini xulosa qilib aytmoqda.</p>",
        'correct': "참석하는 셈이에요",
        'choices': ["참석할수록 좋아요", "참석할 뻔했어요", "참석해 버렸어요", "참석하는 셈이에요"]
    },
    {
        'text': "<p>A: 요리를 할 때 소금을 언제 넣는 것이 좋을까요?<br>B: 국물 요리는 끓이면 <u>국물이</u> 줄어드니까 나중에 ________ 짜지기 쉬워요.</p>",
        'explanation': "<p><strong>졸아들수록</strong>: Suyuqlik kamaygani sari ta'm sho'r bo'lishini bildiradi.</p>",
        'correct': "졸아들수록",
        'choices': ["졸아드는 셈이라", "졸아들 뻔해서", "졸아들어 버려서", "졸아들수록"]
    },
    {
        'text': "<p>A: 아까 무거운 짐을 들고 계단을 내려오다가 발목을 <u>삐끗해서</u> ________.<br>B: 정말 다행이네요. 무거운 걸 들 때는 늘 계단을 조심해야 해요.</p>",
        'explanation': "<p><strong>넘어질 뻔했어요</strong>: Yiqilishga juda oz qolganini anglatadi.</p>",
        'correct': "넘어질 뻔했어요",
        'choices': ["넘어져 버렸어요", "넘어질 뻔했어요", "넘어지는 셈이었어요", "넘어질수록 아팠어요"]
    },
    {
        'text': "<p>A: 컴퓨터에 중요한 사진들을 백업해 두지 않았는데 컴퓨터가 고장 났어요.<br>B: 아이고, 소중한 추억이 담긴 사진들을 ________ 속상하시겠어요.</p>",
        'explanation': "<p><strong>다 날려 버려서</strong>: Rasmlar butunlay yo'q bo'lib ketganini anglatadi.</p>",
        'correct': "다 날려 버려서",
        'choices': ["날리는 셈이라", "날릴 뻔해서", "다 날려 버려서", "날릴수록"]
    },
    {
        'text': "<p>A: 부장님께서 주신 이번 과제는 분량이 <u>엄청나게</u> 많네요.<br>B: 그러니까요. 이 많은 자료를 혼자 다 읽으려면 오늘 밤은 다 ________ 없겠어요.</p>",
        'explanation': "<p><strong>새운 거나 다름</strong>: Uxlmasdan tong ottirish bilan barobar qiyinchilik ekanini bildiradi.</p>",
        'correct': "새운 거나 다름",
        'choices': ["새울 셈", "새운 거나 다름", "새울 뻔", "새워 버릴수록"]
    },
    {
        'text': "<p>A: 두 회사가 이번에 공동으로 신제품을 개발하기로 계약했대요.<br>B: 네, 지분을 절반씩 나누었으니 이제 두 회사는 운명 공동체________ 하나가 되었네요.</p>",
        'explanation': "<p><strong>나 마찬가지로</strong>: Ikki kompaniya bir butun holga kelganini ifodalaydi.</p>",
        'correct': "나 마찬가지로",
        'choices': ["일 셈으로", "일 뻔하게", "여 버려서", "나 마찬가지로"]
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
            title='Takrorlash 2',  # --- IGNORE ---
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

        for i, q in enumerate(questions, start=1):
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
            f"Created practice '{practice.title}' with {len(questions)} questions (id={practice.pk})."
        ))
