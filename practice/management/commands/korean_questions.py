# =====================================================================
# Topic 73: 강한 양보와 가정: 동사/형용사 + (으)ㄹ지라도 / 더라도 / (으)ㅁ에도 불구하고 (Kuchli 양보 va faraz: ...sa ham / ...qaramasdan)
# =====================================================================
topic_73 = [
    {
        'text': "<p>A: 비가 <u>많이</u> <strong>오는데</strong> 등산을 <strong>갈</strong> 거예요?<br>B: 네, 비가 <strong>올</strong>________ <u>꼭</u> <strong>갈</strong> 거예요.</p>",
        'explanation': "<p><strong>올지라도</strong>: '오다' (kelmoq/yog'moq) fe'liga qo'shilib, yomg'ir yog'sa ham baribir borish qat'iyligini bildiradi.</p>",
        'correct': "올지라도",
        'choices': ["오기 십상이다", "올지라도", "오는 탓에", "오는 바람에"]
    },
    {
        'text': "<p>A: <u>아무리</u> <strong>힘들어도</strong> 포기하지 <strong>마세요</strong>.<br>B: <u>네</u>, <u>아무리</u> <strong>힘들</strong>________ <u>끝까지</u> <strong>해낼</strong> 거예요.</p>",
        'explanation': "<p><strong>힘들더라도</strong>: '힘들다' (qiyin bo'lmoq) sifatiga qo'shilib, qanchalik qiyin bo'lmasin (garchand qiyin bo'lsa ham) oxiriga yetkazish niyatini ko'rsatadi.</p>",
        'correct': "힘들더라도",
        'choices': ["힘들더라도", "힘들었더라면", "힘들다가는", "힘들기 마련이다"]
    },
    {
        'text': "<p>A: <u>그</u> 사람은 <u>항상</u> 약속을 <strong>어겨요</strong>.<br>B: <u>경고를</u> <strong>했</strong>________ <u>자꾸</u> 약속을 <strong>어기네요</strong>.</p>",
        'explanation': "<p><strong>했음에도 불구하고</strong>: '하다' fe'lining o'tgan zamon otlashgan shakliga qo'shilib, ogohlantirilganiga qaramasdan va'dani buzishini bildiradi.</p>",
        'correct': "했음에도 불구하고",
        'choices': ["했음에도 불구하고", "했을 지경이다", "했을 리가 없다", "해 봤자"]
    },
    {
        'text': "<p>A: 시간이 <u>오래</u> <strong>걸릴</strong> <u>것</u> <strong>같아요</strong>.<br>B: <u>오래</u> <strong>걸릴</strong>________ <u>포기하지</u> <strong>않고</strong> <strong>기다리겠습니다</strong>.</p>",
        'explanation': "<p><strong>걸릴지라도</strong>: '걸리다' (vaqt ketmoq) fe'liga qo'shilib, ko'p vaqt ketsa ham kutishga tayyorligini ko'rsatadi.</p>",
        'correct': "걸릴지라도",
        'choices': ["걸릴지라도", "걸리려던 참이다", "걸리다가는", "걸린 탓에"]
    },
    {
        'text': "<p>A: 다른 사람들이 <u>다</u> <strong>반대해요</strong>.<br>B: <u>모두가</u> <strong>반대하</strong>________ 저는 제 <u>꿈을</u> <strong>향해</strong> <strong>나아갈</strong> 거예요.</p>",
        'explanation': "<p><strong>반대하더라도</strong>: '반대하다' (qarshi bo'lmoq) fe'liga qo'shilib, hamma qarshi bo'lsa ham o'z yo'lidan qolmasligini bildiradi.</p>",
        'correct': "반대하더라도",
        'choices': ["반대하는 바람에", "반대하더라도", "반대했더라면", "반대하기 무섭게"]
    },
    {
        'text': "<p>A: 건강이 <u>많이</u> <strong>안</strong> <strong>좋으신가요</strong>?<br>B: 네, 의사의 <u>만류가</u> <strong>있었</strong>________ <u>무리하게</u> 일을 <strong>계속했어요</strong>.</p>",
        'explanation': "<p><strong>있었음에도 불구하고</strong>: '있다' fe'liga qo'shilib, shifokor qaytarganiga qaramasdan ishlashda davom etganini ko'rsatadi.</p>",
        'correct': "있었음에도 불구하고",
        'choices': ["있었을 리가 없다", "있었음에도 불구하고", "있었더라면", "있기 마련이다"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>시험은</u> <u>정말</u> <strong>어렵대요</strong>.<br>B: <u>아무리</u> <strong>어려울</strong>________ <u>최선을</u> <strong>다해서</strong> <strong>풀</strong> 거예요.</p>",
        'explanation': "<p><strong>어려울지라도</strong>: '어렵다' sifatiga qo'shilib, qanchalik qiyin bo'lsa ham harakat qilishini bildiradi.</p>",
        'correct': "어려울지라도",
        'choices': ["어려운 탓에", "어려운 바람에", "어려울지라도", "어렵다가는"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>갑자기</u> <u>일이</u> <strong>생길지도</strong> <strong>몰라요</strong>.<br>B: <u>무슨</u> <u>일이</u> <strong>생기</strong>________ <u>우리는</u> <u>꼭</u> <strong>만나야</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>생기더라도</strong>: '생기다' fe'liga qo'shilib, qanday ish chiqsa ham baribir uchrashish shartligini ko'rsatadi.</p>",
        'correct': "생기더라도",
        'choices': ["생겼더라면", "생기더라도", "생기는 김에", "생기려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> 선수는 부상을 <strong>당했네요</strong>.<br>B: 네, <u>심한</u> 부상을 <strong>입었</strong>________ <u>끝까지</u> 경기를 <strong>마쳤습니다</strong>.</p>",
        'explanation': "<p><strong>입었음에도 불구하고</strong>: '입다' (jarohat olmoq) fe'liga qo'shilib, jarohat olganiga qaramasdan o'yinni tugatganini bildiradi.</p>",
        'correct': "입었음에도 불구하고",
        'choices': ["입었음에도 불구하고", "입었어야 했다", "입어 봤자", "입을 지경이다"]
    },
    {
        'text': "<p>A: 돈이 <u>부족할</u> <u>수도</u> <strong>있어요</strong>.<br>B: 돈이 <u>조금</u> <strong>부족할</strong>________ <u>이번</u> <u>기회는</u> <u>꼭</u> <strong>잡고</strong> <strong>싶어요</strong>.</p>",
        'explanation': "<p><strong>부족할지라도</strong>: '부족하다' sifatiga qo'shilib, pul yetmasa ham bu imkoniyatni ushlab qolish istagini ko'rsatadi.</p>",
        'correct': "부족할지라도",
        'choices': ["부족할 뿐이다", "부족할지라도", "부족하기 십상이다", "부족하느라고"]
    },
    {
        'text': "<p>A: 부모님이 <strong>허락하지</strong> <strong>않으시면</strong> <u>어쩌죠</u>?<br>B: 부모님이 <strong>반대하시</strong>________ <u>저는</u> <u>이</u> 길을 <strong>가겠습니다</strong>.</p>",
        'explanation': "<p><strong>반대하시더라도</strong>: '반대하시다' fe'liga qo'shilib, ota-ona qarshi bo'lsa ham o'z yo'lida davom etishini bildiradi.</p>",
        'correct': "반대하시더라도",
        'choices': ["반대하셨더라면", "반대하시다가는", "반대하시더라도", "반대해 봤자"]
    },
    {
        'text': "<p>A: 제품의 <u>가격이</u> <u>너무</u> <strong>비싸요</strong>.<br>B: 가격이 <strong>비쌈</strong>________ <u>품질이</u> <strong>좋아서</strong> <u>잘</u> <strong>팔립니다</strong>.</p>",
        'explanation': "<p><strong>비쌈에도 불구하고</strong>: '비싸다' sifatiga qo'shilib, qimmatligiga qaramasdan yaxshi sotilishini ko'rsatadi.</p>",
        'correct': "비쌈에도 불구하고",
        'choices': ["비싸기 마련이다", "비쌀 리가 없다", "비쌈에도 불구하고", "비싼 탓에"]
    },
    {
        'text': "<p>A: 결과가 <strong>나쁠</strong> <u>수도</u> <strong>있어요</strong>.<br>B: 결과가 <strong>나쁠</strong>________ <u>도전하는</u> <u>데</u> <u>의미가</u> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>나쁠지라도</strong>: '나쁘다' sifatiga qo'shilib, natija yomon bo'lsa ham urinib ko'rish muhimligini bildiradi.</p>",
        'correct': "나쁠지라도",
        'choices': ["나쁘다가는", "나쁠지라도", "나빠 봤자", "나쁠 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>거리가</u> <u>너무</u> <strong>멀지</strong> <strong>않아요</strong>?<br>B: <u>거리가</u> <strong>멀</strong>________ <u>매일</u> <strong>출퇴근할</strong> <u>수</u> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>멀더라도</strong>: '멀다' (uzoq bo'lmoq) sifatiga qo'shilib, uzoq bo'lsa ham qatnay olishini ko'rsatadi.</p>",
        'correct': "멀더라도",
        'choices': ["먼 탓에", "멀더라도", "멀었더라면", "멀기 마련이다"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <strong>바쁜데</strong> <u>어떻게</u> 봉사활동을 <strong>해요</strong>?<br>B: 시간이 <strong>부족함</strong>________ <u>주말마다</u> <u>꾸준히</u> 봉사활동을 <strong>합니다</strong>.</p>",
        'explanation': "<p><strong>부족함에도 불구하고</strong>: '부족하다' sifatiga qo'shilib, vaqt yetishmasligiga qaramasdan ko'ngilli bo'lib ishlashini bildiradi.</p>",
        'correct': "부족함에도 불구하고",
        'choices': ["부족함에도 불구하고", "부족할 지경이다", "부족할 리가 없다", "부족하느라고"]
    },
    {
        'text': "<p>A: 실패하면 <u>다시</u> <strong>일어서기</strong> <strong>힘들 텐데요</strong>.<br>B: 백 번을 <strong>넘어질</strong>________ 백한 번 <strong>일어날</strong> 것입니다.</p>",
        'explanation': "<p><strong>넘어질지라도</strong>: '넘어지다' fe'liga qo'shilib, yuz marta yiqilsa ham baribir qayta turishini ko'rsatadi.</p>",
        'correct': "넘어질지라도",
        'choices': ["넘어지는 바람에", "넘어질지라도", "넘어졌더라면", "넘어지는 김에"]
    },
    {
        'text': "<p>A: <u>이번</u> 일은 <u>위험이</u> <strong>따라요</strong>.<br>B: <u>위험하</u>________ <u>우리</u> <u>팀을</u> <u>위해</u> <u>제가</u> <strong>하겠습니다</strong>.</p>",
        'explanation': "<p><strong>위험하더라도</strong>: '위험하다' sifatiga qo'shilib, xavfli bo'lsa ham buni o'zi qilishini bildiradi.</p>",
        'correct': "위험하더라도",
        'choices': ["위험하더라도", "위험해 봤자", "위험하다가는", "위험할 지경이다"]
    },
    {
        'text': "<p>A: <u>비가</u> <u>이렇게</u> <strong>쏟아지는데</strong> 비행기가 <strong>뜰까요</strong>?<br>B: <u>악천후임</u>________ <u>예정대로</u> <strong>이륙한다고</strong> <strong>합니다</strong>.</p>",
        'explanation': "<p><strong>악천후임에도 불구하고</strong>: '악천후이다' (yomon ob-havo bo'lmoq) ga qo'shilib, noqulay ob-havoga qaramasdan parvoz qilishini ko'rsatadi.</p>",
        'correct': "악천후임에도 불구하고",
        'choices': ["악천후임에도 불구하고", "악천후일 지경이다", "악천후일 뿐이다", "악천후이기 마련이다"]
    },
    {
        'text': "<p>A: <u>아무도</u> 제 말을 <strong>믿지</strong> <strong>않아요</strong>.<br>B: <u>세상</u> <u>사람들이</u> <u>다</u> <strong>안</strong> <strong>믿을</strong>________ <u>저만은</u> 당신을 <strong>믿겠습니다</strong>.</p>",
        'explanation': "<p><strong>믿을지라도</strong>: '믿다' inkor shaklida kelib, hamma ishonmasa ham (garchand ishonmasalar-da) u ishonishini bildiradi.</p>",
        'correct': "안 믿을지라도",
        'choices': ["안 믿다가는", "안 믿어 봤자", "안 믿는 탓에", "안 믿을지라도"]
    },
    {
        'text': "<p>A: <u>지금</u> <strong>시작하면</strong> <u>너무</u> <strong>늦지</strong> <strong>않았을까요</strong>?<br>B: <u>비록</u> <strong>늦었을</strong>________ <u>아무것도</u> <strong>안</strong> <strong>하는</strong> 것보다는 <strong>낫습니다</strong>.</p>",
        'explanation': "<p><strong>늦었을지라도</strong>: '늦다' sifatining o'tgan zamoniga qo'shilib, kech bo'lgan bo'lsa ham hech narsa qilmaslikdan yaxshiroq ekanini ko'rsatadi.</p>",
        'correct': "늦었을지라도",
        'choices': ["늦었을 지경이다", "늦었을지라도", "늦다가는", "늦은 탓에"]
    },
    {
        'text': "<p>A: 나중에 <strong>후회하면</strong> <strong>어떡해요</strong>?<br>B: 나중에 <strong>후회하</strong>________ <u>지금은</u> 제 <u>마음이</u> <u>가는</u> <u>대로</u> <strong>할래요</strong>.</p>",
        'explanation': "<p><strong>후회하더라도</strong>: '후회하다' fe'liga qo'shilib, keyin afsuslansa ham hozir ko'ngli xohlagandek qilishini bildiradi.</p>",
        'correct': "후회하더라도",
        'choices': ["후회하는 바람에", "후회했더라면", "후회하더라도", "후회하기 무섭게"]
    },
    {
        'text': "<p>A: <u>그</u> 학생은 <u>환경이</u> <u>많이</u> <strong>어려웠죠</strong>?<br>B: 네, <u>어려운</u> <u>가정</u> <strong>환경임</strong>________ <u>수석으로</u> <strong>졸업했습니다</strong>.</p>",
        'explanation': "<p><strong>환경임에도 불구하고</strong>: '환경이다' ga qo'shilib, qiyin sharoitga qaramasdan a'lo baholarga bitirganini ko'rsatadi.</p>",
        'correct': "환경임에도 불구하고",
        'choices': ["환경임에도 불구하고", "환경일 지라도", "환경일 턱이 없다", "환경일 뿐이다"]
    },
    {
        'text': "<p>A: <u>이</u> 일은 <u>성과가</u> <u>당장</u> <strong>안</strong> <strong>보여요</strong>.<br>B: 당장 <u>결과가</u> <strong>없을</strong>________ <u>꾸준히</u> <strong>투자해야</strong> <strong>합니다</strong>.</p>",
        'explanation': "<p><strong>없을지라도</strong>: '없다' ga qo'shilib, natija darhol ko'rinmasa ham sarmoya kiritishda davom etish kerakligini bildiradi.</p>",
        'correct': "없을지라도",
        'choices': ["없는 탓에", "없을지라도", "없기 십상이다", "없으려던 참이다"]
    },
    {
        'text': "<p>A: <u>의견이</u> <u>서로</u> <strong>달라도</strong> <strong>괜찮을까요</strong>?<br>B: 네, <u>생각이</u> <strong>다르</strong>________ <u>서로</u> <strong>존중하는</strong> 태도가 <strong>필요해요</strong>.</p>",
        'explanation': "<p><strong>다르더라도</strong>: '다르다' (farqli bo'lmoq) sifatiga qo'shilib, fikrlar farqli bo'lsa ham hurmat kerakligini ko'rsatadi.</p>",
        'correct': "다르더라도",
        'choices': ["다르다가는", "다르더라도", "다른 탓에", "달라 봤자"]
    },
    {
        'text': "<p>A: <u>그</u> 기업은 <u>왜</u> 파업을 <strong>하나요</strong>?<br>B: <u>회사가</u> <u>막대한</u> <strong>이익을</strong> <strong>냈음</strong>________ <u>직원들의</u> <u>월급을</u> <strong>안</strong> <strong>올려줬거든요</strong>.</p>",
        'explanation': "<p><strong>냈음에도 불구하고</strong>: '내다' fe'lining o'tgan zamon otlashgan shakliga qo'shilib, katta foyda ko'rganiga qaramasdan maoshlarni oshirmaganini bildiradi.</p>",
        'correct': "냈음에도 불구하고",
        'choices': ["냈을 리가 없다", "냈음에도 불구하고", "냈더라면", "냈을 지경이다"]
    },
    {
        'text': "<p>A: 상대가 <u>너무</u> <strong>강해서</strong> 우리가 <strong>질</strong> <u>것</u> <strong>같아요</strong>.<br>B: <u>설령</u> <strong>지</strong>________ <u>정정당당하게</u> <strong>싸웁시다</strong>.</p>",
        'explanation': "<p><strong>질지라도</strong>: '지다' (yutqazmoq) fe'liga qo'shilib, yutqazib qo'ysak ham adolatli bellashaylik degan niyatni ko'rsatadi.</p>",
        'correct': "질지라도",
        'choices': ["지는 바람에", "지다가는", "질지라도", "지는 탓에"]
    },
    {
        'text': "<p>A: <u>약속을</u> <strong>취소하면</strong> 친구가 <strong>화내지</strong> <strong>않을까요</strong>?<br>B: 친구가 <strong>화내</strong>________ <u>오늘은</u> <u>너무</u> <strong>아파서</strong> <strong>못</strong> <strong>나가겠어요</strong>.</p>",
        'explanation': "<p><strong>화내더라도</strong>: '화내다' fe'liga qo'shilib, do'sti jahl qilsa ham kasalligi sababli borolmasligini bildiradi.</p>",
        'correct': "화내더라도",
        'choices': ["화내더라도", "화내다가는", "화내 봤자", "화냈더라면"]
    },
    {
        'text': "<p>A: <u>증거가</u> <u>충분히</u> <strong>제출되었나요</strong>?<br>B: 네, <u>명백한</u> <strong>증거가</strong> <strong>있음</strong>________ <u>그는</u> 범행을 <strong>부인하고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>있음에도 불구하고</strong>: '있다' ga qo'shilib, dalil borligiga qaramasdan inkor etishda davom etayotganini ko'rsatadi.</p>",
        'correct': "있음에도 불구하고",
        'choices': ["있으려던 참이다", "있음에도 불구하고", "있기 마련이다", "있을 리가 없다"]
    },
    {
        'text': "<p>A: 사람들이 <u>다</u> <strong>비웃을지도</strong> <strong>몰라요</strong>.<br>B: <u>모두가</u> 저를 <strong>비웃을</strong>________ <u>저는</u> <u>당당하게</u> <strong>행동할</strong> 것입니다.</p>",
        'explanation': "<p><strong>비웃을지라도</strong>: '비웃다' (ustidan kulmoq) fe'liga qo'shilib, hamma ustidan kulsa ham o'zini dadil tutishini bildiradi.</p>",
        'correct': "비웃을지라도",
        'choices': ["비웃기 십상이다", "비웃을지라도", "비웃을 리가 없다", "비웃어 봤자"]
    },
    {
        'text': "<p>A: <u>실패가</u> <strong>두렵지</strong> <strong>않으세요</strong>?<br>B: <u>설사</u> <strong>실패하</strong>________ <u>그</u> <u>과정에서</u> <u>많은</u> <u>것을</u> <strong>배울</strong> <u>수</u> <strong>있으니까요</strong>.</p>",
        'explanation': "<p><strong>실패하더라도</strong>: '실패하다' (muvaffaqiyatsizlikka uchramoq) fe'liga qo'shilib, mag'lubiyatga uchrasa ham o'rganish muhimligini ko'rsatadi.</p>",
        'correct': "실패하더라도",
        'choices': ["실패하는 통에", "실패하더라도", "실패했더라면", "실패하다가는"]
    }
]

# =====================================================================
# Topic 74: 행동이나 상태의 정도: 동사/형용사 + (으)ㄹ 정도로 / (으)ㄹ 만큼 (Harakat yoki holat darajasi: ...darajada / ...chalik)
# =====================================================================
topic_74 = [
    {
        'text': "<p>A: <u>어제</u> 영화 <u>많이</u> <strong>슬펐어요</strong>?<br>B: 네, <u>눈이</u> <u>퉁퉁</u> <strong>부을</strong> ________ <u>펑펑</u> <strong>울었어요</strong>.</p>",
        'explanation': "<p><strong>부을 정도로</strong>: '붓다' (ishmoq/shishmoq) fe'liga qo'shilib, ko'zlar shishib ketadigan darajada yig'laganini bildiradi.</p>",
        'correct': "부을 정도로",
        'choices': ["부을 지라도", "부을 정도로", "부었음에도 불구하고", "부을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> 빵집이 <u>그렇게</u> 인기가 <strong>많아요</strong>?<br>B: 네, <u>아침부터</u> <u>줄을</u> <strong>서야</strong> <strong>할</strong> ________ 사람들이 <u>많이</u> <strong>와요</strong>.</p>",
        'explanation': "<p><strong>할 만큼</strong>: '하다' fe'liga qo'shilib, navbatda turishga to'g'ri keladigan darajada odam ko'pligini ko'rsatadi.</p>",
        'correct': "할 만큼",
        'choices': ["하는 탓에", "할 만큼", "하다가는", "할 리가 없다"]
    },
    {
        'text': "<p>A: 한국어 <u>정말</u> <u>잘하시네요</u>!<br>B: <u>감사합니다</u>. 한국 사람과 <u>자연스럽게</u> <strong>대화할</strong> ________ <u>더</u> <strong>노력할게요</strong>.</p>",
        'explanation': "<p><strong>대화할 정도로</strong>: '대화하다' (suhbatlashmoq) fe'liga qo'shilib, tabiiy gaplasha oladigan darajada intilishini bildiradi.</p>",
        'correct': "대화할 정도로",
        'choices': ["대화할 정도로", "대화할 지경이다", "대화할 겸", "대화하려던 참이다"]
    },
    {
        'text': "<p>A: <u>이번</u> 감기가 <u>많이</u> <strong>독한가요</strong>?<br>B: 네, <u>며칠</u> <u>동안</u> <u>일어나지도</u> <strong>못할</strong> ________ <u>많이</u> <strong>아팠어요</strong>.</p>",
        'explanation': "<p><strong>못할 만큼</strong>: '못하다' inkor fe'liga qo'shilib, o'rnidan turolmaydigan darajada kasal bo'lganini ko'rsatadi.</p>",
        'correct': "못할 만큼",
        'choices': ["못할 턱이 없다", "못할지라도", "못할 만큼", "못하는 바람에"]
    },
    {
        'text': "<p>A: <u>그</u> 아이는 <u>얼마나</u> <strong>똑똑해요</strong>?<br>B: <u>어른들도</u> <strong>놀랄</strong> ________ <u>어려운</u> <u>문제를</u> <u>잘</u> <strong>풀어요</strong>.</p>",
        'explanation': "<p><strong>놀랄 정도로</strong>: '놀라다' (hayratlanmoq) fe'liga qo'shilib, kattalar ham hayratda qoladigan darajada ekanini bildiradi.</p>",
        'correct': "놀랄 정도로",
        'choices': ["놀라다가는", "놀랄 정도로", "놀라는 김에", "놀랄 지라도"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>바람이</u> <u>많이</u> <strong>부나요</strong>?<br>B: 네, 나무가 <strong>뽑힐</strong> ________ <u>거센</u> 바람이 <strong>불고</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>뽑힐 만큼</strong>: '뽑히다' (yulinmoq) fe'liga qo'shilib, daraxt yulinib ketadigan darajada kuchli shamol ekanini ko'rsatadi.</p>",
        'correct': "뽑힐 만큼",
        'choices': ["뽑히기 무섭게", "뽑힐 만큼", "뽑힐 리가 없다", "뽑힌 채로"]
    },
    {
        'text': "<p>A: <u>어제</u> 회식에서 <u>고기를</u> <u>많이</u> <strong>드셨어요</strong>?<br>B: 네, 배가 <strong>터질</strong> ________ <u>많이</u> <strong>먹어서</strong> <u>아직도</u> <strong>배불러요</strong>.</p>",
        'explanation': "<p><strong>터질 정도로</strong>: '터지다' (yorilmoq) fe'liga qo'shilib, qorin yorilgudek darajada yeganini bildiradi.</p>",
        'correct': "터질 정도로",
        'choices': ["터질 정도로", "터지기 십상이다", "터지다가는", "터질 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> 사람은 <u>얼마나</u> <u>돈이</u> <strong>많아요</strong>?<br>B: <u>평생</u> <strong>일하지</strong> <strong>않아도</strong> <strong>될</strong> ________ <u>재산이</u> <strong>많다고</strong> <strong>들었어요</strong>.</p>",
        'explanation': "<p><strong>될 만큼</strong>: '되다' fe'liga qo'shilib, umrbod ishlamasa ham yetadigan darajada boyligini ko'rsatadi.</p>",
        'correct': "될 만큼",
        'choices': ["되는 탓에", "될지라도", "될 만큼", "될 지경이다"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>시험공부를</u> <u>열심히</u> <strong>했나요</strong>?<br>B: 네, 책을 <u>통째로</u> <u>다</u> <strong>외울</strong> ________ <u>열심히</u> <strong>했습니다</strong>.</p>",
        'explanation': "<p><strong>외울 정도로</strong>: '외우다' (yodlamoq) fe'liga qo'shilib, kitobni to'liq yodlab oladigan darajada o'qiganini bildiradi.</p>",
        'correct': "외울 정도로",
        'choices': ["외우는 통에", "외울 정도로", "외우려던 참이다", "외웠더라면"]
    },
    {
        'text': "<p>A: <u>요즘</u> <u>많이</u> <strong>바쁘신가요</strong>?<br>B: <u>화장실에</u> <strong>갈</strong> <u>시간도</u> <strong>없을</strong> ________ <u>눈코 뜰 새 없이</u> <strong>바쁩니다</strong>.</p>",
        'explanation': "<p><strong>없을 만큼</strong>: '없다' ga qo'shilib, hojatxonaga borishga ham vaqt yo'q darajada bandligini ko'rsatadi.</p>",
        'correct': "없을 만큼",
        'choices': ["없을 만큼", "없을 리가 없다", "없음에도 불구하고", "없기 마련이다"]
    },
    {
        'text': "<p>A: <u>그</u> 배우가 <u>그렇게</u> <strong>유명해요</strong>?<br>B: 네, <u>길거리를</u> <strong>지나가면</strong> <u>모든</u> 사람이 <strong>알아볼</strong> ________ <strong>유명해요</strong>.</p>",
        'explanation': "<p><strong>알아볼 정도로</strong>: '알아보다' (tanib olmoq) fe'liga qo'shilib, ko'chada hamma taniydigan darajada mashhurligini bildiradi.</p>",
        'correct': "알아볼 정도로",
        'choices': ["알아보자마자", "알아볼 지라도", "알아볼 정도로", "알아보는 탓에"]
    },
    {
        'text': "<p>A: <u>방이</u> <u>많이</u> <strong>지저분했나요</strong>?<br>B: <u>발을</u> <strong>디딜</strong> <u>틈이</u> <strong>없을</strong> ________ <u>쓰레기가</u> <strong>가득했어요</strong>.</p>",
        'explanation': "<p><strong>없을 만큼</strong>: '없다' ga qo'shilib, oyoq qo'yishga joy yo'q darajada iflosligini ko'rsatadi.</p>",
        'correct': "없을 만큼",
        'choices': ["없을 만큼", "없기 십상이다", "없으려던 참이다", "없는 바람에"]
    },
    {
        'text': "<p>A: <u>얼마나</u> <strong>아팠어요</strong>?<br>B: <u>너무</u> <strong>아파서</strong> <u>눈물이</u> <strong>쏙</strong> <strong>빠질</strong> ________ <strong>아팠어요</strong>.</p>",
        'explanation': "<p><strong>빠질 정도로</strong>: '빠지다' fe'liga qo'shilib, og'riqdan ko'z yosh chiqib ketadigan darajada og'riganini bildiradi.</p>",
        'correct': "빠질 정도로",
        'choices': ["빠지는 길에", "빠질 정도로", "빠질 리가 없다", "빠질 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> <u>선물에</u> <u>많이</u> <strong>감동했나요</strong>?<br>B: 네, <u>말을</u> <strong>잇지</strong> <strong>못할</strong> ________ <u>큰</u> 감동을 <strong>받았어요</strong>.</p>",
        'explanation': "<p><strong>못할 만큼</strong>: '못하다' inkor fe'liga qo'shilib, gapira olmay qoladigan darajada ta'sirlanganini ko'rsatadi.</p>",
        'correct': "못할 만큼",
        'choices': ["못할 지경이다", "못할 리가 없다", "못할 만큼", "못하는 바람에"]
    },
    {
        'text': "<p>A: 한국의 <u>여름은</u> <u>많이</u> <strong>덥나요</strong>?<br>B: 네, <u>가만히</u> <strong>있어도</strong> <u>땀이</u> <u>줄줄</u> <strong>흐를</strong> ________ <strong>더워요</strong>.</p>",
        'explanation': "<p><strong>흐를 정도로</strong>: '흐르다' (oqmoq) fe'liga qo'shilib, qimirlamay turganda ham ter oqadigan darajada issiqligini bildiradi.</p>",
        'correct': "흐를 정도로",
        'choices': ["흐르다가는", "흐를 정도로", "흐를 뿐이다", "흐를 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> 사람은 <u>거짓말을</u> <u>자주</u> <strong>하나요</strong>?<br>B: <u>이제는</u> <u>그</u> 사람이 <u>무슨</u> 말을 <strong>해도</strong> <strong>믿기지</strong> <strong>않을</strong> ________ <u>자주</u> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>않을 만큼</strong>: '않다' inkoriga qo'shilib, endi gapiga ishonib bo'lmaydigan darajada ko'p yolg'on gapirishini ko'rsatadi.</p>",
        'correct': "않을 만큼",
        'choices': ["않기 십상이다", "않는 김에", "않을 만큼", "않을 리가 없다"]
    },
    {
        'text': "<p>A: 물건이 <u>싸서</u> <u>많이</u> <strong>샀어요</strong>?<br>B: 네, 양손에 <u>다</u> <strong>들지</strong> <strong>못할</strong> ________ <u>잔뜩</u> <strong>샀어요</strong>.</p>",
        'explanation': "<p><strong>못할 정도로</strong>: '못하다' inkoriga qo'shilib, qo'lga sig'maydigan darajada ko'p olganini bildiradi.</p>",
        'correct': "못할 정도로",
        'choices': ["못할 정도로", "못하는 탓에", "못할 지라도", "못하려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>영화는</u> <u>얼마나</u> <strong>무서웠어요</strong>?<br>B: <u>밤에</u> <u>혼자</u> 화장실에 <strong>못</strong> <strong>갈</strong> ________ <strong>무서웠어요</strong>.</p>",
        'explanation': "<p><strong>갈 만큼</strong>: '가다' fe'liga qo'shilib, tunda yolg'iz hojatxonaga borolmaydigan darajada qo'rqinchli ekanini ko'rsatadi.</p>",
        'correct': "갈 만큼",
        'choices': ["가는 김에", "갈 만큼", "갔더라면", "가다가는"]
    },
    {
        'text': "<p>A: <u>두</u> 사람 <u>사이가</u> <u>정말</u> <strong>안</strong> <strong>좋은가</strong> <strong>봐요</strong>.<br>B: <u>서로</u> 얼굴도 <strong>마주치기</strong> <strong>싫어할</strong> ________ <u>사이가</u> <strong>나빠졌어요</strong>.</p>",
        'explanation': "<p><strong>싫어할 정도로</strong>: '싫어하다' (yomon ko'rmoq/xohlamaslik) fe'liga qo'shilib, ko'rishishni ham xohlamaydigan darajada dushmanlashganini bildiradi.</p>",
        'correct': "싫어할 정도로",
        'choices': ["싫어할지라도", "싫어할 정도로", "싫어할 뿐만 아니라", "싫어하기 십상이다"]
    },
    {
        'text': "<p>A: <u>이번</u> 여행은 <u>많이</u> <strong>피곤했나요</strong>?<br>B: <u>집에</u> <strong>도착하자마자</strong> <u>쓰러져서</u> <strong>잘</strong> ________ <u>체력을</u> <u>다</u> <strong>썼어요</strong>.</p>",
        'explanation': "<p><strong>잘 만큼</strong>: '자다' (uxlamoq) fe'liga qo'shilib, uyga yetgach yiqilib uxlaydigan darajada charchaganini ko'rsatadi.</p>",
        'correct': "잘 만큼",
        'choices': ["자다가는", "자는 바람에", "잘 만큼", "잘 리가 없다"]
    },
    {
        'text': "<p>A: <u>한국어</u> <u>발음이</u> <u>정말</u> <strong>좋으시네요</strong>.<br>B: <u>처음</u> <strong>보는</strong> 사람이 한국인으로 <strong>착각할</strong> ________ <u>매일</u> <strong>연습했어요</strong>.</p>",
        'explanation': "<p><strong>착각할 정도로</strong>: '착각하다' (yanglishmoq/adashib o'ylamoq) fe'liga qo'shilib, koreys deb o'ylaydigan darajada zo'r talaffuz qilishini bildiradi.</p>",
        'correct': "착각할 정도로",
        'choices': ["착각할 지라도", "착각할 정도로", "착각하기 십상이다", "착각하는 탓에"]
    },
    {
        'text': "<p>A: <u>그</u> <u>노래가</u> <u>그렇게</u> <strong>좋았어요</strong>?<br>B: <u>하루 종일</u> <u>그</u> <u>노래만</u> <u>반복해서</u> <strong>들을</strong> ________ <u>완전히</u> <strong>빠졌어요</strong>.</p>",
        'explanation': "<p><strong>들을 만큼</strong>: '듣다' (eshitmoq) fe'liga qo'shilib, kun bo'yi tinimsiz eshitadigan darajada yoqib qolganini ko'rsatadi.</p>",
        'correct': "들을 만큼",
        'choices': ["듣는 바람에", "듣기 무섭게", "들을 만큼", "듣다가는"]
    },
    {
        'text': "<p>A: <u>소음이</u> <u>심한가요</u>?<br>B: <u>옆</u> 사람의 <u>말소리가</u> <strong>안</strong> <strong>들릴</strong> ________ <u>시끄러워요</u>.</p>",
        'explanation': "<p><strong>들릴 정도로</strong>: '들리다' (eshitilmoq) fe'liga qo'shilib, yonidagi odamning gapi eshitilmaydigan darajada shovqin ekanini bildiradi.</p>",
        'correct': "들릴 정도로",
        'choices': ["들릴 정도로", "들리려던 참이다", "들릴 지경이다", "들릴지라도"]
    },
    {
        'text': "<p>A: <u>운동을</u> <u>얼마나</u> <u>열심히</u> <strong>하세요</strong>?<br>B: <u>다음 날</u> <u>근육통으로</u> <strong>고생할</strong> ________ <u>강도 높게</u> <strong>합니다</strong>.</p>",
        'explanation': "<p><strong>고생할 만큼</strong>: '고생하다' (qiynalmoq) fe'liga qo'shilib, ertasiga mushaklar og'rig'idan qiynaladigan darajada mashq qilishini ko'rsatadi.</p>",
        'correct': "고생할 만큼",
        'choices': ["고생하는 탓에", "고생할 만큼", "고생해 봤자", "고생했더라면"]
    },
    {
        'text': "<p>A: <u>그</u> 책은 <u>내용이</u> <strong>어려워요</strong>?<br>B: <u>초등학생도</u> <u>쉽게</u> <strong>이해할</strong> ________ <u>아주</u> <strong>쉽게</strong> <strong>쓰여</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>이해할 정도로</strong>: '이해하다' (tushunmoq) fe'liga qo'shilib, yosh bola ham tushunadigan darajada osonligini bildiradi.</p>",
        'correct': "이해할 정도로",
        'choices': ["이해할 지경이다", "이해할 정도로", "이해하기 십상이다", "이해할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>하늘이</u> <u>정말</u> <strong>맑네요</strong>.<br>B: <u>저 멀리</u> 있는 <u>산꼭대기가</u> <u>선명하게</u> <strong>보일</strong> ________ <u>미세먼지가</u> <strong>없어요</strong>.</p>",
        'explanation': "<p><strong>보일 만큼</strong>: '보이다' (ko'rinmoq) fe'liga qo'shilib, uzoqdagi tog' cho'qqisi aniq ko'rinadigan darajada tozaligini ko'rsatadi.</p>",
        'correct': "보일 만큼",
        'choices': ["보이는 바람에", "보일 만큼", "보이는 김에", "보일 리가 없다"]
    },
    {
        'text': "<p>A: <u>음식을</u> <u>얼마나</u> <strong>준비해야</strong> <strong>할까요</strong>?<br>B: 손님들이 <u>배불리</u> <strong>먹고도</strong> <strong>남을</strong> ________ <u>넉넉하게</u> <strong>준비해</strong> <strong>주세요</strong>.</p>",
        'explanation': "<p><strong>남을 정도로</strong>: '남다' (ortib qolmoq) fe'liga qo'shilib, to'yib yeganda ham ortib qoladigan darajada ko'p bo'lishini bildiradi.</p>",
        'correct': "남을 정도로",
        'choices': ["남을 지경이다", "남을 정도로", "남을 리가 없다", "남을지라도"]
    },
    {
        'text': "<p>A: <u>그</u> <u>가방이</u> <u>그렇게</u> <strong>무거웠어요</strong>?<br>B: <u>혼자서는</u> <u>도저히</u> <strong>들지</strong> <strong>못할</strong> ________ <strong>무거워서</strong> <u>결국</u> <strong>끌고</strong> <strong>왔어요</strong>.</p>",
        'explanation': "<p><strong>못할 만큼</strong>: '못하다' inkor fe'liga qo'shilib, bir o'zi ko'tarolmaydigan darajada og'irligini ko'rsatadi.</p>",
        'correct': "못할 만큼",
        'choices': ["못할 만큼", "못하는 바람에", "못할 턱이 없다", "못하다가는"]
    },
    {
        'text': "<p>A: <u>그</u> 아이는 <u>거짓말을</u> <u>진짜처럼</u> <strong>하네요</strong>.<br>B: <u>모두가</u> 깜빡 <strong>속아 넘어갈</strong> ________ <u>천연덕스럽게</u> <strong>거짓말을</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>넘어갈 정도로</strong>: '넘어가다' (laqqa tushmoq/aldanmoq) fe'liga qo'shilib, hamma ishonib qoladigan darajada ustalik bilan aldashini bildiradi.</p>",
        'correct': "넘어갈 정도로",
        'choices': ["넘어가기 십상이다", "넘어갈 뿐이다", "넘어갈 정도로", "넘어가는 통에"]
    },
    {
        'text': "<p>A: <u>두</u> 사람 <u>외모가</u> <u>많이</u> <strong>닮았나요</strong>?<br>B: <u>쌍둥이라고</u> <strong>해도</strong> <strong>믿을</strong> ________ <u>정말</u> <u>판박이처럼</u> <strong>똑같이</strong> <strong>생겼어요</strong>.</p>",
        'explanation': "<p><strong>믿을 만큼</strong>: '믿다' (ishonmoq) fe'liga qo'shilib, egizak desa ishonadigan darajada o'xshashligini ko'rsatadi.</p>",
        'correct': "믿을 만큼",
        'choices': ["믿을 만큼", "믿기 마련이다", "믿을지라도", "믿은 탓에"]
    }
]

# =====================================================================
# Topic 75: 극단적인 상태 강조: 형용사 + 기 짝이 없다 (Ekstremal holatni ta'kidlash: ...ning cheki yo'q / g'oyatda ...)
# =====================================================================
topic_75 = [
    {
        'text': "<p>A: <u>오랜만에</u> 고향 친구를 <strong>만나니</strong> <strong>어때요</strong>?<br>B: <u>십 년 만에</u> <strong>만나서</strong> <u>정말</u> <strong>반갑</strong>________.</p>",
        'explanation': "<p><strong>반갑기 짝이 없어요</strong>: '반갑다' (xursand bo'lmoq) sifatiga qo'shilib, uchrashganidan xursandligining cheki yo'qligini bildiradi.</p>",
        'correct': "반갑기 짝이 없어요",
        'choices': ["반갑기 십상이에요", "반갑기 짝이 없어요", "반가울 뿐이에요", "반가운 탓이에요"]
    },
    {
        'text': "<p>A: <u>그</u> <u>소식을</u> <strong>듣고</strong> <u>많이</u> <strong>슬프셨겠어요</strong>.<br>B: <u>갑작스러운</u> 사고 소식에 <strong>안타깝</strong>________.</p>",
        'explanation': "<p><strong>안타깝기 짝이 없었습니다</strong>: '안타깝다' (achinarli/alamli bo'lmoq) sifatiga qo'shilib, qayg'usi va afsuslanishi g'oyatda kuchliligini ko'rsatadi.</p>",
        'correct': "안타깝기 짝이 없었습니다",
        'choices': ["안타까울 지경이었습니다", "안타깝기 짝이 없었습니다", "안타까울 리가 없었습니다", "안타깝기 마련이었습니다"]
    },
    {
        'text': "<p>A: <u>그</u> 사람의 <u>태도가</u> <u>불쾌했나요</u>?<br>B: <u>어른에게</u> 인사도 <strong>안</strong> <strong>하고</strong> <u>정말</u> <strong>무례하</strong>________.</p>",
        'explanation': "<p><strong>무례하기 짝이 없네요</strong>: '무례하다' (hurmatsiz/qo'pol bo'lmoq) sifatiga qo'shilib, odobsizligining chegarasi yo'qligini bildiradi.</p>",
        'correct': "무례하기 짝이 없네요",
        'choices': ["무례하기 짝이 없네요", "무례한 바람에", "무례할 뿐만 아니라", "무례하기 무섭게"]
    },
    {
        'text': "<p>A: 혼자 <u>외지에</u> <strong>떨어져</strong> <strong>있어서</strong> <u>힘들지</u> <strong>않아요</strong>?<br>B: <u>명절이</u> <strong>되면</strong> 가족들이 <strong>그리워서</strong> <strong>외롭</strong>________.</p>",
        'explanation': "<p><strong>외롭기 짝이 없어요</strong>: '외롭다' (yolg'iz bo'lmoq) sifatiga qo'shilib, yolg'izlik hissi haddan tashqari kuchliligini ko'rsatadi.</p>",
        'correct': "외롭기 짝이 없어요",
        'choices': ["외로운 탓이에요", "외로울 지라도", "외롭기 짝이 없어요", "외로우려던 참이에요"]
    },
    {
        'text': "<p>A: <u>그</u> <u>경치를</u> <u>직접</u> <strong>보니까</strong> <strong>어때요</strong>?<br>B: 사진으로 <strong>볼</strong> <u>때보다</u> <u>훨씬</u> <u>아름다워서</u> <strong>황홀하</strong>________.</p>",
        'explanation': "<p><strong>황홀하기 짝이 없었어요</strong>: '황홀하다' (maftunkor bo'lmoq) sifatiga qo'shilib, go'zallikdan maftun bo'lishning cheki yo'qligini bildiradi.</p>",
        'correct': "황홀하기 짝이 없었어요",
        'choices': ["황홀할 턱이 없었어요", "황홀하기 십상이었어요", "황홀하기 짝이 없었어요", "황홀한 탓이었어요"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>실수에</u> <u>대해</u> <u>어떻게</u> <strong>생각하세요</strong>?<br>B: <u>제</u> 불찰로 <u>팀에</u> 피해를 <strong>주어</strong> <strong>죄송하</strong>________.</p>",
        'explanation': "<p><strong>죄송하기 짝이 없습니다</strong>: '죄송하다' (kechirim so'ramoq) sifatiga qo'shilib, uyat va xijolatpazlikning juda katta darajasini ko'rsatadi.</p>",
        'correct': "죄송하기 짝이 없습니다",
        'choices': ["죄송할 리가 없습니다", "죄송하기 마련입니다", "죄송하기 짝이 없습니다", "죄송할 따름입니다"]
    },
    {
        'text': "<p>A: 아이들이 <u>자유롭게</u> <strong>뛰어노는</strong> <u>모습이</u> <u>어때</u> <strong>보여요</strong>?<br>B: <u>근심</u> 걱정 <strong>없이</strong> <strong>순수하</strong>________.</p>",
        'explanation': "<p><strong>순수하기 짝이 없네요</strong>: '순수하다' (sof/beg'ubor bo'lmoq) sifatiga qo'shilib, bolalarning beg'uborligi cheksizligini bildiradi.</p>",
        'correct': "순수하기 짝이 없네요",
        'choices': ["순수하기 짝이 없네요", "순수한 바람에", "순수할 지라도", "순수할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> 정책에 <u>대해</u> 반발이 <strong>심한가요</strong>?<br>B: <u>현실을</u> <strong>모르는</strong> 정책이라서 <strong>어처구니없</strong>________.</p>",
        'explanation': "<p><strong>어처구니없기 짝이 없습니다</strong>: '어처구니없다' (bema'ni/aqlga sig'maydigan bo'lmoq) sifatiga qo'shilib, mantiqsizligining cheki yo'qligini ko'rsatadi.</p>",
        'correct': "어처구니없기 짝이 없습니다",
        'choices': ["어처구니없을 지경입니다", "어처구니없기 십상입니다", "어처구니없기 짝이 없습니다", "어처구니없는 통에"]
    },
    {
        'text': "<p>A: <u>자신의</u> 이익만 <strong>생각하는</strong> 사람들을 <strong>보면</strong> <strong>어때요</strong>?<br>B: <u>남을</u> 배려하지 <strong>않는</strong> <u>모습이</u> <strong>이기적이</strong>________.</p>",
        'explanation': "<p><strong>이기적이기 짝이 없어요</strong>: '이기적이다' (xudbin bo'lmoq) ga qo'shilib, xudbinligining chegarasi yo'q ekanini bildiradi.</p>",
        'correct': "이기적이기 짝이 없어요",
        'choices': ["이기적인 탓이에요", "이기적이기 짝이 없어요", "이기적일 뿐이에요", "이기적이기 마련이에요"]
    },
    {
        'text': "<p>A: 혼자서 <u>모든</u> 일을 <strong>떠맡게</strong> <strong>되었네요</strong>.<br>B: <u>도와주는</u> <u>사람도</u> <strong>없고</strong> <u>참</u> <strong>막막하</strong>________.</p>",
        'explanation': "<p><strong>막막하기 짝이 없네요</strong>: '막막하다' (nochog'/boshiberk holatda bo'lmoq) sifatiga qo'shilib, umidsizligining cheki yo'qligini ko'rsatadi.</p>",
        'correct': "막막하기 짝이 없네요",
        'choices': ["막막할 리가 없네요", "막막하기 짝이 없네요", "막막한 바람에", "막막할 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> 범죄자의 행동이 <u>국민들의</u> 분노를 <strong>샀어요</strong>.<br>B: <u>반성조차</u> <strong>하지</strong> <strong>않다니</strong> <u>정말</u> <strong>뻔뻔하</strong>________.</p>",
        'explanation': "<p><strong>뻔뻔하기 짝이 없네요</strong>: '뻔뻔하다' (surbet bo'lmoq) sifatiga qo'shilib, uyatsizligining cheki yo'qligini bildiradi.</p>",
        'correct': "뻔뻔하기 짝이 없네요",
        'choices': ["뻔뻔한 탓에", "뻔뻔하기 무섭게", "뻔뻔하기 짝이 없네요", "뻔뻔할 리가 없네요"]
    },
    {
        'text': "<p>A: <u>아무런</u> 이유 <strong>없이</strong> <u>욕을</u> <strong>들었을</strong> <u>때</u> <strong>기분이</strong> <strong>어땠어요</strong>?<br>B: <u>너무</u> <u>갑작스러워서</u> <strong>불쾌하</strong>________.</p>",
        'explanation': "<p><strong>불쾌하기 짝이 없었어요</strong>: '불쾌하다' (yoqimsiz/kayfiyatsiz bo'lmoq) sifatiga qo'shilib, g'azabi va noroziligi o'ta kuchli bo'lganini ko'rsatadi.</p>",
        'correct': "불쾌하기 짝이 없었어요",
        'choices': ["불쾌할 지경이었어요", "불쾌하기 십상이었어요", "불쾌하기 짝이 없었어요", "불쾌하려던 참이었어요"]
    },
    {
        'text': "<p>A: <u>경기에</u> <strong>져서</strong> <u>많이</u> <strong>속상하시죠</strong>?<br>B: <u>한 점</u> <u>차이로</u> <strong>져서</strong> <strong>아쉽</strong>________.</p>",
        'explanation': "<p><strong>아쉽기 짝이 없네요</strong>: '아쉽다' (afsuslanarli bo'lmoq) sifatiga qo'shilib, o'kkinchi juda katta ekanini bildiradi.</p>",
        'correct': "아쉽기 짝이 없네요",
        'choices': ["아쉽기 짝이 없네요", "아쉽기 마련이네요", "아쉬울 뿐만 아니라", "아쉬운 탓이네요"]
    },
    {
        'text': "<p>A: <u>밤하늘의</u> <u>별을</u> <strong>보고</strong> <strong>있으면</strong> <u>무슨</u> <strong>생각이</strong> <strong>들어요</strong>?<br>B: 우주의 <u>크기에</u> <strong>비하면</strong> 인간은 <u>정말</u> <strong>초라하</strong>________.</p>",
        'explanation': "<p><strong>초라하기 짝이 없어요</strong>: '초라하다' (g'arib/arzimas bo'lmoq) sifatiga qo'shilib, insonning ojizligi va kichikligini g'oyatda kuchli his qilishini ko'rsatadi.</p>",
        'correct': "초라하기 짝이 없어요",
        'choices': ["초라할 지라도", "초라한 바람에", "초라하기 짝이 없어요", "초라할 리가 없어요"]
    },
    {
        'text': "<p>A: <u>어린</u> <u>나이에</u> <u>벌써</u> <u>큰</u> <u>상처를</u> <strong>받았네요</strong>.<br>B: <u>부모도</u> <strong>없이</strong> <u>홀로</u> 남겨진 <u>아이가</u> <strong>가엽</strong>________.</p>",
        'explanation': "<p><strong>가엽기 짝이 없어요</strong>: '가엽다' (bechora/rahmi kelgulik bo'lmoq) sifatiga qo'shilib, bolaga nisbatan cheksiz rahm-shafqatni bildiradi.</p>",
        'correct': "가엽기 짝이 없어요",
        'choices': ["가엽은 탓이에요", "가엽기 짝이 없어요", "가여울 지경이에요", "가엽기 십상이에요"]
    },
    {
        'text': "<p>A: <u>저</u> 사람의 <u>패션</u> 감각은 <u>정말</u> <strong>독특하네요</strong>.<br>B: <u>유행에</u> <u>전혀</u> <strong>맞지</strong> <strong>않아서</strong> <strong>촌스럽</strong>________.</p>",
        'explanation': "<p><strong>촌스럽기 짝이 없어요</strong>: '촌스럽다' (xunuk/zavqsiz bo'lmoq) sifatiga qo'shilib, didsizligining cheki yo'qligini ko'rsatadi.</p>",
        'correct': "촌스럽기 짝이 없어요",
        'choices': ["촌스러울 리가 없어요", "촌스럽기 짝이 없어요", "촌스러울 뿐만 아니라", "촌스러운 김에"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <u>비싼</u> 돈을 <strong>주고</strong> <strong>샀는데</strong> <u>하루 만에</u> <strong>고장 나다니요</strong>.<br>B: 돈이 <u>너무</u> <strong>아깝고</strong> <strong>허무하</strong>________.</p>",
        'explanation': "<p><strong>허무하기 짝이 없네요</strong>: '허무하다' (behuda/bo'm-bo'sh bo'lmoq) sifatiga qo'shilib, pullar bekorga ketganidan afsuslanishning haddan oshganini bildiradi.</p>",
        'correct': "허무하기 짝이 없네요",
        'choices': ["허무하기 마련이네요", "허무할 지경이네요", "허무하기 짝이 없네요", "허무하려던 참이네요"]
    },
    {
        'text': "<p>A: <u>친구들이</u> <u>모두</u> <strong>떠나고</strong> <u>혼자</u> <strong>남았을</strong> <u>때</u> <strong>기분이</strong> <strong>어땠어요</strong>?<br>B: <u>텅 빈</u> <u>방에</u> <u>홀로</u> <strong>있으니</strong> <strong>쓸쓸하</strong>________.</p>",
        'explanation': "<p><strong>쓸쓸하기 짝이 없었어요</strong>: '쓸쓸하다' (huznsiz/kimsasiz bo'lmoq) sifatiga qo'shilib, yolg'izlik va mung hissi g'oyatda kuchliligini ko'rsatadi.</p>",
        'correct': "쓸쓸하기 짝이 없었어요",
        'choices': ["쓸쓸하기 십상이었어요", "쓸쓸한 바람에", "쓸쓸할 지라도", "쓸쓸하기 짝이 없었어요"]
    },
    {
        'text': "<p>A: <u>그</u> 사람의 <u>행동이</u> <u>많이</u> <strong>유치했나요</strong>?<br>B: <u>다 큰</u> 어른이 <u>길바닥에서</u> <strong>떼를</strong> <strong>쓰다니</strong> <strong>한심하</strong>________.</p>",
        'explanation': "<p><strong>한심하기 짝이 없었어요</strong>: '한심하다' (achinarli darajada pastkash/aqlsiz bo'lmoq) sifatiga qo'shilib, qilig'i o'ta bachkanalik ekanini bildiradi.</p>",
        'correct': "한심하기 짝이 없었어요",
        'choices': ["한심하기 짝이 없었어요", "한심할 리가 없었어요", "한심하기 마련이었어요", "한심한 탓이었어요"]
    },
    {
        'text': "<p>A: 복권 <u>1등에</u> <strong>당첨되었을</strong> <u>때의</u> <strong>기분을</strong> <strong>표현해</strong> <strong>주세요</strong>.<br>B: <u>세상을</u> <u>다</u> <strong>가진</strong> <u>것처럼</u> <strong>기쁘</strong>________.</p>",
        'explanation': "<p><strong>기쁘기 짝이 없었습니다</strong>: '기쁘다' (xursand bo'lmoq) sifatiga qo'shilib, quvonchning chegarasi yo'qligini ko'rsatadi.</p>",
        'correct': "기쁘기 짝이 없었습니다",
        'choices': ["기쁠 리가 없었습니다", "기쁘기 십상이었습니다", "기쁘기 짝이 없었습니다", "기뻐려던 참이었습니다"]
    },
    {
        'text': "<p>A: <u>아무런</u> 대가 <strong>없이</strong> <u>평생을</u> <strong>봉사하신</strong> 분을 <strong>뵈니</strong> <strong>어때요</strong>?<br>B: <u>그분의</u> <u>숭고한</u> 희생정신이 <strong>존경스럽</strong>________.</p>",
        'explanation': "<p><strong>존경스럽기 짝이 없네요</strong>: '존경스럽다' (hurmatga sazovor bo'lmoq) sifatiga qo'shilib, ehtirom hissi g'oyatda cheksizligini bildiradi.</p>",
        'correct': "존경스럽기 짝이 없네요",
        'choices': ["존경스럽기 짝이 없네요", "존경스러운 바람에", "존경스러울 뿐만 아니라", "존경스럽기 마련이네요"]
    },
    {
        'text': "<p>A: <u>이</u> <u>넓은</u> <u>우주에</u> 지구에만 생명체가 <strong>있을까요</strong>?<br>B: <u>만약</u> <strong>그렇다면</strong> <u>이</u> 우주 공간이 <u>너무</u> <strong>낭비라</strong> <strong>생각되어</strong> <strong>기막히</strong>________.</p>",
        'explanation': "<p><strong>기막히기 짝이 없네요</strong>: '기막히다' (hayratlanarli/aqldan ozdiradigan bo'lmoq) sifatiga qo'shilib, ishonish qiyin va hayratlanarli darajada ekanini ko'rsatadi.</p>",
        'correct': "기막히기 짝이 없네요",
        'choices': ["기막힐 리가 없네요", "기막히기 십상이네요", "기막히기 짝이 없네요", "기막힌 탓이네요"]
    },
    {
        'text': "<p>A: <u>그</u> 영화의 <u>결말이</u> <u>많이</u> <strong>실망스러웠나요</strong>?<br>B: <u>개연성도</u> <strong>없고</strong> <u>억지스러워서</u> <strong>유치하</strong>________.</p>",
        'explanation': "<p><strong>유치하기 짝이 없었어요</strong>: '유치하다' (bolalarcha/past saviyali bo'lmoq) sifatiga qo'shilib, filmni o'ta sayoz ekanini bildiradi.</p>",
        'correct': "유치하기 짝이 없었어요",
        'choices': ["유치할 지라도", "유치하기 짝이 없었어요", "유치하기 마련이었어요", "유치한 김에"]
    },
    {
        'text': "<p>A: <u>매일</u> 똑같은 일상만 <strong>반복되니</strong> <strong>어때요</strong>?<br>B: <u>변화가</u> <u>하나도</u> <strong>없어서</strong> <strong>지루하</strong>________.</p>",
        'explanation': "<p><strong>지루하기 짝이 없네요</strong>: '지루하다' (zerikarli bo'lmoq) sifatiga qo'shilib, zerikishning cheki yo'qligini ko'rsatadi.</p>",
        'correct': "지루하기 짝이 없네요",
        'choices': ["지루하기 짝이 없네요", "지루할 리가 없네요", "지루할 뿐만 아니라", "지루하려던 참이네요"]
    },
    {
        'text': "<p>A: <u>그런</u> <u>끔찍한</u> 범죄를 <strong>저지르고도</strong> 웃음이 <strong>나올까요</strong>?<br>B: 인간의 <u>탈을</u> <strong>쓰고</strong> <u>어떻게</u> <strong>저럴</strong> <u>수</u> <strong>있는지</strong> <strong>경악스럽</strong>________.</p>",
        'explanation': "<p><strong>경악스럽기 짝이 없네요</strong>: '경악스럽다' (dahshatli/shok holatiga tushiradigan bo'lmoq) sifatiga qo'shilib, dahshatga tushishning g'oyatda yuqoriligini bildiradi.</p>",
        'correct': "경악스럽기 짝이 없네요",
        'choices': ["경악스러운 탓에", "경악스럽기 무섭게", "경악스럽기 십상이네요", "경악스럽기 짝이 없네요"]
    },
    {
        'text': "<p>A: <u>평생</u> 모은 <u>재산을</u> 사회에 <strong>환원하셨다면서요</strong>?<br>B: <u>자신보다</u> <u>남을</u> <u>먼저</u> <strong>생각하시는</strong> <u>마음이</u> <strong>거룩하</strong>________.</p>",
        'explanation': "<p><strong>거룩하기 짝이 없습니다</strong>: '거룩하다' (muqaddas/ulug'vor bo'lmoq) sifatiga qo'shilib, olijanoqligining chegarasi yo'qligini ko'rsatadi.</p>",
        'correct': "거룩하기 짝이 없습니다",
        'choices': ["거룩하기 짝이 없습니다", "거룩할 지경입니다", "거룩하기 마련입니다", "거룩할 리가 없습니다"]
    },
    {
        'text': "<p>A: <u>그</u> 아이의 <u>말투가</u> <u>어른</u> <strong>같지</strong> <strong>않아요</strong>?<br>B: <u>나이에</u> <strong>맞지</strong> <strong>않게</strong> 애늙은이 <u>같아서</u> <strong>징그럽</strong>________.</p>",
        'explanation': "<p><strong>징그럽기 짝이 없어요</strong>: '징그럽다' (g'alati/jirkanch bo'lmoq - ba'zan g'alati qiliqqa nisbatan) sifatiga qo'shilib, bolaning qilig'i g'oyatda g'alati va yoqimsiz ekanini bildiradi.</p>",
        'correct': "징그럽기 짝이 없어요",
        'choices': ["징그러운 바람에", "징그럽기 짝이 없어요", "징그러울 지라도", "징그러울 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이렇게</u> <u>추운</u> 날씨에 <u>보일러도</u> <strong>없이</strong> <strong>지내신다고요</strong>?<br>B: <u>홀로</u> <u>냉방에서</u> <strong>견디시는</strong> <u>어르신을</u> <strong>생각하니</strong> <strong>참담하</strong>________.</p>",
        'explanation': "<p><strong>참담하기 짝이 없네요</strong>: '참담하다' (ayanchli/mudhish bo'lmoq) sifatiga qo'shilib, vaziyat g'oyatda ayanchli ekanini ko'rsatadi.</p>",
        'correct': "참담하기 짝이 없네요",
        'choices': ["참담하기 십상이에요", "참담한 김에", "참담하기 짝이 없네요", "참담할 리가 없네요"]
    },
    {
        'text': "<p>A: <u>정말</u> 우연히 <u>그</u> 사람을 <u>그곳에서</u> <strong>만났어요</strong>.<br>B: <u>세상이</u> <strong>좁다더니</strong> <u>정말</u> <strong>신기하</strong>________.</p>",
        'explanation': "<p><strong>신기하기 짝이 없네요</strong>: '신기하다' (ajoyib/qiziq bo'lmoq) sifatiga qo'shilib, tasodifning g'oyatda qiziq ekanligini bildiradi.</p>",
        'correct': "신기하기 짝이 없네요",
        'choices': ["신기하기 짝이 없네요", "신기하기 마련이네요", "신기할 뿐만 아니라", "신기한 탓이네요"]
    },
    {
        'text': "<p>A: <u>아무리</u> <strong>설명해도</strong> 제 말을 <strong>이해하지</strong> <strong>못해요</strong>.<br>B: <u>벽을</u> <strong>보고</strong> <strong>얘기하는</strong> <u>것</u> <strong>같아서</strong> <strong>답답하</strong>________.</p>",
        'explanation': "<p><strong>답답하기 짝이 없네요</strong>: '답답하다' (bo'g'ilmoq/qisilib ketmoq) sifatiga qo'shilib, tushunarsizlikdan siqilishning cheki yo'qligini ko'rsatadi.</p>",
        'correct': "답답하기 짝이 없네요",
        'choices': ["답답한 바람에", "답답하기 십상이네요", "답답할 지라도", "답답하기 짝이 없네요"]
    }
]

# =====================================================================
# Topic 76: 단지 ~일 뿐이다: 명사 + 에 불과하다 / 동사/형용사 + (으)ㄹ 따름이다 / (으)ㄹ 뿐이다
# =====================================================================
topic_76 = [
    {
        'text': "<p>A: <u>그</u> 소문이 <u>정말</u> <strong>사실인가요</strong>?<br>B: <u>아니요</u>, <u>단지</u> <u>사람들이</u> <strong>지어낸</strong> 헛소문________.</p>",
        'explanation': "<p><strong>헛소문에 불과합니다</strong>: '헛소문' (mish-mish) otiga qo'shilib, u shunchaki mish-mishdan boshqa narsa emasligini bildiradi.</p>",
        'correct': "헛소문에 불과합니다",
        'choices': ["헛소문에 불과합니다", "헛소문일 지경입니다", "헛소문일 턱이 없습니다", "헛소문이기 십상입니다"]
    },
    {
        'text': "<p>A: <u>이번</u> 일로 <u>많이</u> <strong>화나셨어요</strong>?<br>B: <u>아니요</u>, <u>그저</u> <u>상황이</u> <u>조금</u> <strong>안타까울</strong> ________.</p>",
        'explanation': "<p><strong>안타까울 따름입니다</strong>: '안타깝다' (achinarli) sifatiga qo'shilib, faqatgina achinayotganini, boshqa hissi yo'qligini ko'rsatadi.</p>",
        'correct': "안타까울 따름입니다",
        'choices': ["안타까울 셈입니다", "안타까울 따름입니다", "안타까울 겸", "안타까운 바람에"]
    },
    {
        'text': "<p>A: 저를 <u>왜</u> <strong>도와주셨어요</strong>?<br>B: <u>저는</u> <u>당연히</u> <strong>해야</strong> <strong>할</strong> 일을 <strong>했을</strong> ________.</p>",
        'explanation': "<p><strong>했을 뿐입니다</strong>: '하다' fe'lining o'tgan zamoniga qo'shilib, shunchaki o'z vazifasini bajarganini, alohida maqsadi yo'qligini bildiradi.</p>",
        'correct': "했을 뿐입니다",
        'choices': ["하는 김에", "했을 뿐입니다", "하는 탓에", "했을 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> 사람은 <u>아직도</u> <u>학생인가요</u>?<br>B: 네, <u>나이는</u> <strong>많지만</strong> <u>아직</u> <u>대학생</u>________.</p>",
        'explanation': "<p><strong>대학생에 불과합니다</strong>: '대학생' (talaba) otiga qo'shilib, u yoshi katta bo'lsa-da, faqatgina talaba ekanligini ko'rsatadi.</p>",
        'correct': "대학생에 불과합니다",
        'choices': ["대학생일 턱이 없습니다", "대학생에 불과합니다", "대학생일 뿐만 아니라", "대학생이기 십상입니다"]
    },
    {
        'text': "<p>A: <u>모두가</u> <strong>원하는</strong> <u>결과가</u> <strong>나왔네요</strong>.<br>B: <u>그저</u> <u>운이</u> <strong>좋았을</strong> ________. <u>제가</u> <strong>한</strong> <u>일은</u> <strong>없습니다</strong>.</p>",
        'explanation': "<p><strong>좋았을 따름입니다</strong>: '좋다' (yaxshi bo'lmoq) sifatiga qo'shilib, bu shunchaki omad ekanini ta'kidlaydi.</p>",
        'correct': "좋았을 따름입니다",
        'choices': ["좋은 탓입니다", "좋을 지경입니다", "좋았을 따름입니다", "좋았더라면"]
    },
    {
        'text': "<p>A: <u>이</u> <u>문제를</u> <u>어떻게</u> <strong>해결할까요</strong>?<br>B: <u>저도</u> <u>해결책을</u> <strong>모를</strong> ________. <u>전문가에게</u> <strong>물어봅시다</strong>.</p>",
        'explanation': "<p><strong>모를 뿐입니다</strong>: '모르다' (bilmaslik) fe'liga qo'shilib, shunchaki o'zi ham bilmasligini bildiradi.</p>",
        'correct': "모를 뿐입니다",
        'choices': ["모를 뿐입니다", "모를 지경입니다", "모르는 김에", "모를 리가 없습니다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>아이디어가</u> <u>대단한</u> <u>혁신인가요</u>?<br>B: <u>단순한</u> <u>모방</u>________. <u>새로운</u> <u>것은</u> <strong>없습니다</strong>.</p>",
        'explanation': "<p><strong>모방에 불과합니다</strong>: '모방' (taqlid) otiga qo'shilib, u bor-yo'g'i taqlid ekanini ko'rsatadi.</p>",
        'correct': "모방에 불과합니다",
        'choices': ["모방일 지라도", "모방일 턱이 없습니다", "모방에 불과합니다", "모방이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>제가</u> <strong>합격하다니</strong> <strong>믿기지</strong> <strong>않아요</strong>.<br>B: <u>열심히</u> <strong>노력한</strong> <u>당신이</u> <u>당연한</u> 결과를 <strong>얻었을</strong> ________.</p>",
        'explanation': "<p><strong>얻었을 따름입니다</strong>: '얻다' (olmoq/erishmoq) fe'liga qo'shilib, faqatgina o'z mehnatiga yarasha natija olganini bildiradi.</p>",
        'correct': "얻었을 따름입니다",
        'choices': ["얻을 지라도", "얻었을 뿐만 아니라", "얻었을 따름입니다", "얻어 봤자"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>그렇게</u> <u>슬프게</u> <strong>울어요</strong>?<br>B: <u>그냥</u> <u>영화가</u> <u>너무</u> <strong>슬퍼서</strong> <strong>우는</strong> <u>것일</u> ________.</p>",
        'explanation': "<p><strong>것일 뿐입니다</strong>: '것이다' ga qo'shilib, faqatgina kino qayg'uli bo'lgani uchun yig'layotganini ko'rsatadi.</p>",
        'correct': "것일 뿐입니다",
        'choices': ["것일 턱이 없습니다", "것일 뿐입니다", "것이기 십상입니다", "것이기 마련입니다"]
    },
    {
        'text': "<p>A: <u>그의</u> <u>재산이</u> <u>엄청나다면서요</u>?<br>B: <u>자세히</u> <strong>알아보면</strong> <u>다</u> <u>빚</u>________.</p>",
        'explanation': "<p><strong>빚에 불과합니다</strong>: '빚' (qarz) otiga qo'shilib, uning boyligi aslida faqat qarzlardan iboratligini bildiradi.</p>",
        'correct': "빚에 불과합니다",
        'choices': ["빚이기 십상입니다", "빚일 따름입니다", "빚에 불과합니다", "빚이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>정말</u> <u>이</u> 일을 <strong>포기하실</strong> 건가요?<br>B: 네, <u>제</u> 능력이 <strong>부족하다는</strong> <u>것을</u> <strong>느꼈을</strong> ________.</p>",
        'explanation': "<p><strong>느꼈을 따름입니다</strong>: '느끼다' (his qilmoq) fe'liga qo'shilib, bor-yo'g'i o'z ojizligini tushunib yetganini ko'rsatadi.</p>",
        'correct': "느꼈을 따름입니다",
        'choices': ["느꼈을 지경입니다", "느꼈을 따름입니다", "느끼는 바람에", "느끼다가는"]
    },
    {
        'text': "<p>A: <u>저를</u> <u>많이</u> <strong>도와주셨는데</strong> <u>원하는</u> <u>게</u> <strong>있으신가요</strong>?<br>B: <u>아니요</u>, <u>단지</u> <u>당신이</u> <strong>잘되기를</strong> <strong>바랄</strong> ________.</p>",
        'explanation': "<p><strong>바랄 뿐입니다</strong>: '바라다' (umid qilmoq) fe'liga qo'shilib, faqat uning yaxshi bo'lishini xohlashini bildiradi.</p>",
        'correct': "바랄 뿐입니다",
        'choices': ["바라는 탓입니다", "바랄 뿐입니다", "바라기 무섭게", "바라느라고"]
    },
    {
        'text': "<p>A: <u>그</u> <u>문제는</u> <u>아주</u> <strong>심각한</strong> <u>위기인가요</u>?<br>B: <u>조금</u> <strong>귀찮은</strong> <u>장애물</u>________. <u>금방</u> <strong>해결할</strong> <u>수</u> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>장애물에 불과합니다</strong>: '장애물' (to'siq) otiga qo'shilib, bu shunchaki kichik to'siq ekanini ko'rsatadi.</p>",
        'correct': "장애물에 불과합니다",
        'choices': ["장애물에 불과합니다", "장애물일 지라도", "장애물일 턱이 없습니다", "장애물이기 마련입니다"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>왜</u> <u>갑자기</u> <strong>나가셨어요</strong>?<br>B: <u>급한</u> 전화가 <strong>와서</strong> <u>잠시</u> <strong>나갔다</strong> <strong>온</strong> <u>것일</u> ________.</p>",
        'explanation': "<p><strong>것일 뿐입니다</strong>: '것이다' ga qo'shilib, shunchaki telefonga javob berish uchun chiqqanini bildiradi.</p>",
        'correct': "것일 뿐입니다",
        'choices': ["것일 지경입니다", "것일 턱이 없습니다", "것일 뿐입니다", "것이기 십상입니다"]
    },
    {
        'text': "<p>A: <u>제가</u> <strong>만든</strong> <u>요리가</u> <strong>맛없나요</strong>?<br>B: <u>아니요</u>, <u>배가</u> <strong>불러서</strong> <u>조금만</u> <strong>먹을</strong> ________.</p>",
        'explanation': "<p><strong>먹을 따름입니다</strong> (yoki 뿐입니다): '먹다' fe'liga qo'shilib, qorni to'qligi uchun faqat ozroq yeyishini ko'rsatadi.</p>",
        'correct': "먹을 따름입니다",
        'choices': ["먹는 김에", "먹을 따름입니다", "먹을 턱이 없습니다", "먹다가는"]
    },
    {
        'text': "<p>A: <u>우리가</u> <strong>만난</strong> <u>게</u> 운명일까요?<br>B: <u>글쎄요</u>, <u>그저</u> <u>우연의</u> 일치________.</p>",
        'explanation': "<p><strong>일치에 불과합니다</strong>: '일치' (mos kelish/tasodif) otiga qo'shilib, bu faqatgina tasodif ekanini bildiradi.</p>",
        'correct': "일치에 불과합니다",
        'choices': ["일치일 지라도", "일치에 불과합니다", "일치일 뿐만 아니라", "일치이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>선생님은</u> <u>학생들을</u> <u>정말</u> <strong>사랑하시네요</strong>.<br>B: <u>저는</u> <u>학생들이</u> <strong>올바르게</strong> <strong>자라도록</strong> <strong>안내할</strong> ________.</p>",
        'explanation': "<p><strong>안내할 뿐입니다</strong>: '안내하다' (yo'l ko'rsatmoq) fe'liga qo'shilib, uning ishi faqat yo'naltirish ekanini ko'rsatadi.</p>",
        'correct': "안내할 뿐입니다",
        'choices': ["안내할 지라도", "안내할 뿐입니다", "안내하는 바람에", "안내해 봤자"]
    },
    {
        'text': "<p>A: <u>이</u> <u>그림이</u> <u>수천만 원이라면서요</u>?<br>B: <u>제</u> 눈에는 <u>그냥</u> <u>낙서</u>________.</p>",
        'explanation': "<p><strong>낙서에 불과합니다</strong>: '낙서' (oddiy chizma/qoralama) otiga qo'shilib, uning nazarida bu shunchaki qoralama ekanini bildiradi.</p>",
        'correct': "낙서에 불과합니다",
        'choices': ["낙서에 불과합니다", "낙서일 리가 없습니다", "낙서이기 십상입니다", "낙서이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>저를</u> <strong>피하시는</strong> <u>이유가</u> <strong>있나요</strong>?<br>B: <strong>피하는</strong> <u>게</u> <strong>아니라</strong> <u>요즘</u> <u>일이</u> <u>너무</u> <strong>바쁠</strong> ________.</p>",
        'explanation': "<p><strong>바쁠 따름입니다</strong>: '바쁘다' sifatiga qo'shilib, qochayotgani yo'qligini, faqatgina band ekanini ko'rsatadi.</p>",
        'correct': "바쁠 따름입니다",
        'choices': ["바쁠 따름입니다", "바쁠 지경입니다", "바쁜 탓입니다", "바쁘기 마련입니다"]
    },
    {
        'text': "<p>A: <u>정말</u> <u>아무</u> 사이도 <strong>아닌가요</strong>?<br>B: 네, <u>우리는</u> <u>그냥</u> <u>오랜</u> <u>친구</u>________.</p>",
        'explanation': "<p><strong>친구에 불과합니다</strong>: '친구' otiga qo'shilib, faqat do'st ekanliklarini bildiradi.</p>",
        'correct': "친구에 불과합니다",
        'choices': ["친구일 지라도", "친구에 불과합니다", "친구일 뿐만 아니라", "친구이기 십상입니다"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>항상</u> <u>그</u> <u>옷만</u> <strong>입어요</strong>?<br>B: <u>특별한</u> 이유는 <strong>없고</strong> <u>단지</u> <u>편해서</u> <strong>입을</strong> ________.</p>",
        'explanation': "<p><strong>입을 뿐입니다</strong>: '입다' (kiymoq) fe'liga qo'shilib, faqat qulay bo'lgani uchun kiyishini ko'rsatadi.</p>",
        'correct': "입을 뿐입니다",
        'choices': ["입는 김에", "입는 바람에", "입을 뿐입니다", "입다가는"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <strong>기대하더니</strong> <strong>실망하셨군요</strong>.<br>B: 네, 소문난 <u>잔치에</u> <strong>먹을</strong> 것 <strong>없다는</strong> <u>말을</u> <strong>실감했을</strong> ________.</p>",
        'explanation': "<p><strong>실감했을 따름입니다</strong>: '실감하다' (his qilmoq/amin bo'lmoq) fe'liga qo'shilib, shunchaki maqolning to'g'riligiga amin bo'lganini bildiradi.</p>",
        'correct': "실감했을 따름입니다",
        'choices': ["실감했을 리가 없습니다", "실감했을 지경입니다", "실감했을 따름입니다", "실감해 봤자"]
    },
    {
        'text': "<p>A: <u>제</u> 제안이 <u>너무</u> <strong>부족한가요</strong>?<br>B: <u>아니요</u>, <u>다만</u> <u>지금</u> <u>우리</u> 회사 <u>상황에</u> <strong>맞지</strong> <strong>않을</strong> ________.</p>",
        'explanation': "<p><strong>않을 뿐입니다</strong>: '않다' inkoriga qo'shilib, faqatgina vaziyatga mos kelmasligini ko'rsatadi.</p>",
        'correct': "않을 뿐입니다",
        'choices': ["않기 마련입니다", "않기 십상입니다", "않을 뿐입니다", "않는 탓입니다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>계획이</u> <u>완벽하다고</u> <strong>생각하세요</strong>?<br>B: <u>아직은</u> 머릿속의 <u>구상</u>________. <u>실행해</u> <strong>봐야</strong> <strong>알아요</strong>.</p>",
        'explanation': "<p><strong>구상에 불과합니다</strong>: '구상' (g'oya/xayoldagi reja) otiga qo'shilib, hozircha faqat xomaki reja ekanini bildiradi.</p>",
        'correct': "구상에 불과합니다",
        'choices': ["구상일 턱이 없습니다", "구상에 불과합니다", "구상이기 십상입니다", "구상이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>제가</u> <u>많이</u> <strong>부족해서</strong> <strong>죄송합니다</strong>.<br>B: <strong>부족한</strong> <u>것이</u> <strong>아니라</strong> <u>아직</u> <u>경험이</u> <strong>없을</strong> ________.</p>",
        'explanation': "<p><strong>없을 따름입니다</strong>: '없다' ga qo'shilib, faqat tajribasi yo'qligini, aybi yo'qligini ko'rsatadi.</p>",
        'correct': "없을 따름입니다",
        'choices': ["없을 따름입니다", "없기 마련입니다", "없는 바람에", "없을 지라도"]
    },
    {
        'text': "<p>A: <u>그의</u> 주장은 <u>정말</u> <strong>충격적이네요</strong>.<br>B: <u>단지</u> <u>관심을</u> <strong>끌기</strong> 위한 <u>거짓말</u>________.</p>",
        'explanation': "<p><strong>거짓말에 불과합니다</strong>: '거짓말' (yolg'on) otiga qo'shilib, e'tibor tortish uchun qilingan yolg'on ekanini bildiradi.</p>",
        'correct': "거짓말에 불과합니다",
        'choices': ["거짓말일 지라도", "거짓말에 불과합니다", "거짓말일 뿐만 아니라", "거짓말이기 마련입니다"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>항상</u> <u>혼자</u> <strong>점심을</strong> <strong>드세요</strong>?<br>B: <u>특별한</u> 이유는 <strong>없고</strong> <u>혼자</u> <strong>먹는</strong> <u>게</u> <strong>편할</strong> ________.</p>",
        'explanation': "<p><strong>편할 뿐입니다</strong>: '편하다' (qulay bo'lmoq) sifatiga qo'shilib, faqat qulay bo'lgani uchun shunday qilishini ko'rsatadi.</p>",
        'correct': "편할 뿐입니다",
        'choices': ["편한 탓입니다", "편할 뿐입니다", "편할 지경입니다", "편하기 무섭게"]
    },
    {
        'text': "<p>A: <u>정말</u> <u>로봇이</u> <u>인간을</u> <strong>지배할까요</strong>?<br>B: <u>그것은</u> <u>공상 과학</u> 영화의 <u>소재</u>________.</p>",
        'explanation': "<p><strong>소재에 불과합니다</strong>: '소재' (mavzu/material) otiga qo'shilib, bu shunchaki kino mavzusi ekanini bildiradi.</p>",
        'correct': "소재에 불과합니다",
        'choices': ["소재에 불과합니다", "소재이기 십상입니다", "소재일 리가 없습니다", "소재이려던 참입니다"]
    },
    {
        'text': "<p>A: <u>오늘</u> <strong>결석하신</strong> <u>이유가</u> <strong>있나요</strong>?<br>B: <u>갑자기</u> <u>배가</u> <u>너무</u> <strong>아파서</strong> <strong>쉬었을</strong> ________.</p>",
        'explanation': "<p><strong>쉬었을 따름입니다</strong>: '쉬다' (dam olmoq) fe'liga qo'shilib, faqat kasallik sababli dam olganini ko'rsatadi.</p>",
        'correct': "쉬었을 따름입니다",
        'choices': ["쉬는 탓입니다", "쉬었을 리가 없습니다", "쉬었을 따름입니다", "쉬었더라면"]
    },
    {
        'text': "<p>A: <u>제</u> <u>이야기를</u> <strong>듣고</strong> <strong>화나셨어요</strong>?<br>B: <u>아니요</u>, <u>그저</u> <u>당신의</u> <u>상황이</u> <strong>가여울</strong> ________.</p>",
        'explanation': "<p><strong>가여울 뿐입니다</strong>: '가엽다' (bechora) sifatiga qo'shilib, faqatgina rahmi kelayotganini bildiradi.</p>",
        'correct': "가여울 뿐입니다",
        'choices': ["가여운 김에", "가여울 뿐입니다", "가여울 지라도", "가여워 봤자"]
    }
]

# =====================================================================
# Topic 77: 선택과 무관함: 동사/형용사 + 든지 든지 / 건 건 (Qiladimi, yo'qmi ahamiyatsiz / ...sa ham, ...sa ham)
# =====================================================================
topic_77 = [
    {
        'text': "<p>A: <u>이번</u> <u>주말에</u> 산에 <strong>갈</strong> 거예요, 바다에 <strong>갈</strong> 거예요?<br>B: 산에 <strong>가</strong>________ 바다에 <strong>가</strong>________ <u>다</u> <strong>좋아요</strong>.</p>",
        'explanation': "<p><strong>가든지 가든지</strong>: '가다' (bormoq) fe'liga qo'shilib, toqqa boradimi, dengizgami, farqi yo'qligini bildiradi.</p>",
        'correct': "가든지 가든지",
        'choices': ["가다가는 가다가는", "가든지 가든지", "가건 말건", "가려던 참이다"]
    },
    {
        'text': "<p>A: <u>비싼</u> 옷을 <strong>살까요</strong>, <u>싼</u> 옷을 <strong>살까요</strong>?<br>B: 옷이 <strong>비싸</strong>________ <strong>싸</strong>________ <u>본인한테</u> <strong>어울리는</strong> <u>게</u> <u>제일</u> <strong>중요해요</strong>.</p>",
        'explanation': "<p><strong>비싸건 싸건</strong>: '비싸다', '싸다' sifatlariga qo'shilib, qimmatmi-arzonmi, ahamiyatsiz ekanini ko'rsatadi.</p>",
        'correct': "비싸건 싸건",
        'choices': ["비싼 탓에 싼 탓에", "비싸건 싸건", "비쌀 뿐만 아니라", "비싸기 마련이다"]
    },
    {
        'text': "<p>A: <u>그</u> 사람이 <u>자꾸</u> <u>이상한</u> <strong>말을</strong> <strong>해요</strong>.<br>B: <u>그</u> 사람이 <u>무슨</u> 말을 <strong>하</strong>________ 말<strong>하</strong>________ 신경 <strong>쓰지</strong> <strong>마세요</strong>.</p>",
        'explanation': "<p><strong>하든지 말든지</strong>: '하다' va inkor '말다' ga qo'shilib, gapiradimi-yo'qmi e'tibor bermaslikni bildiradi.</p>",
        'correct': "하든지 말든지",
        'choices': ["하든지 말든지", "하려던 참이다", "하다가는 말다가는", "해 봤자 말아 봤자"]
    },
    {
        'text': "<p>A: <u>이</u> 음식은 <u>너무</u> <strong>매워</strong> <strong>보여요</strong>.<br>B: <strong>맵</strong>________ <strong>안</strong> <strong>맵</strong>________ <u>일단</u> <u>한번</u> <strong>먹어</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>맵건 안 맵건</strong>: '맵다' sifatiga qo'shilib, achchiq bo'lsa ham, bo'lmasa ham tatib ko'rishni ko'rsatadi.</p>",
        'correct': "맵건 안 맵건",
        'choices': ["매울 지라도 안 매울 지라도", "매운 탓에 안 매운 탓에", "맵건 안 맵건", "맵기 십상이다"]
    },
    {
        'text': "<p>A: 비가 <strong>오는데</strong> 축구를 <strong>할</strong> <u>건가요</u>?<br>B: 네, 비가 <strong>오</strong>________ 눈이 <strong>오</strong>________ 경기는 <u>계속</u><strong>됩니다</strong>.</p>",
        'explanation': "<p><strong>오든지 오든지</strong>: '오다' fe'liga qo'shilib, yomg'ir yoki qor yog'ishidan qat'i nazar o'yin davom etishini bildiradi.</p>",
        'correct': "오든지 오든지",
        'choices': ["오는 김에 오는 김에", "오다가는 오다가는", "오든지 오든지", "올 지경이다"]
    },
    {
        'text': "<p>A: <u>어떤</u> 선물을 <strong>고를까요</strong>?<br>B: <strong>크</strong>________ <strong>작</strong>________ <u>정성만</u> <strong>들어가면</strong> <strong>돼요</strong>.</p>",
        'explanation': "<p><strong>크건 작건</strong>: '크다', '작다' sifatlariga qo'shilib, katta-kichikligining farqi yo'qligini ko'rsatadi.</p>",
        'correct': "크건 작건",
        'choices': ["크건 작건", "클 뿐만 아니라", "큰 탓에 작은 탓에", "크기 마련이다"]
    },
    {
        'text': "<p>A: <u>회의에</u> <strong>참석할</strong> 거예요?<br>B: 당신이 <strong>참석하</strong>________ <strong>안</strong> <strong>참석하</strong>________ <u>저는</u> <strong>갈</strong> 거예요.</p>",
        'explanation': "<p><strong>참석하든지 안 참석하든지</strong>: Qatnashasizmi, yo'qmi buning ahamiyati yo'qligini bildiradi.</p>",
        'correct': "참석하든지 안 참석하든지",
        'choices': ["참석하는 통에", "참석하든지 안 참석하든지", "참석하다가는", "참석할 리가 없다"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>왜</u> <strong>안</strong> <strong>왔어요</strong>? <u>많이</u> <strong>기다렸잖아요</strong>.<br>B: <u>당신이</u> <strong>기다리</strong>________ 말<strong>기다리</strong>________ <u>저와는</u> <u>상관없는</u> <u>일입니다</u>.</p>",
        'explanation': "<p><strong>기다리건 말건</strong>: '기다리다' va '말다' ga qo'shilib, kutadimi-yo'qmi farqi yo'qligini (qo'polroq) ko'rsatadi.</p>",
        'correct': "기다리건 말건",
        'choices': ["기다려 봤자", "기다리는 바람에", "기다리건 말건", "기다렸더라면"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>결과가</u> <strong>나오는데</strong> <u>너무</u> <strong>떨려요</strong>.<br>B: <strong>합격하</strong>________ <strong>불합격하</strong>________ <u>결과를</u> <u>겸허히</u> <strong>받아들여야</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>합격하든지 불합격하든지</strong>: O'tish yoki yiqilishdan qat'i nazar, qabul qilish kerakligini bildiradi.</p>",
        'correct': "합격하든지 불합격하든지",
        'choices': ["합격하든지 불합격하든지", "합격할 뿐만 아니라", "합격하기 마련이다", "합격할 지라도"]
    },
    {
        'text': "<p>A: <u>이</u> <u>일은</u> <u>누가</u> <strong>해야</strong> <strong>해요</strong>?<br>B: <u>네가</u> <strong>하</strong>________ <u>내가</u> <strong>하</strong>________ <u>빨리</u> <strong>끝내는</strong> <u>게</u> <strong>중요해</strong>.</p>",
        'explanation': "<p><strong>하건 하건</strong>: Kim qilishining ahamiyati yo'qligini, tez tugatish muhimligini ko'rsatadi.</p>",
        'correct': "하건 하건",
        'choices': ["하는 김에", "하건 하건", "하다가는", "해 봤자"]
    },
    {
        'text': "<p>A: <u>주말에</u> <u>공부할</u> 거예요, <strong>놀</strong> 거예요?<br>B: <strong>공부하</strong>________ <strong>놀</strong>________ <u>알아서</u> <strong>할게요</strong>.</p>",
        'explanation': "<p><strong>공부하든지 놀든지</strong>: O'qiydimi, o'ynaydimi, o'zi bilib hal qilishini bildiradi.</p>",
        'correct': "공부하든지 놀든지",
        'choices': ["공부하는 탓에", "공부할 겸", "공부하든지 놀든지", "공부하다가는 놀다가는"]
    },
    {
        'text': "<p>A: 거리가 <u>조금</u> <strong>먼데</strong> <strong>갈</strong> <u>수</u> <strong>있겠어요</strong>?<br>B: <strong>멀</strong>________ <strong>가깝</strong>________ <u>일단</u> <strong>가볼게요</strong>.</p>",
        'explanation': "<p><strong>멀건 가깝건</strong>: '멀다', '가깝다' sifatlariga qo'shilib, masofaning qizig'i yo'qligini ko'rsatadi.</p>",
        'correct': "멀건 가깝건",
        'choices': ["멀건 가깝건", "먼 탓에 가까운 탓에", "멀기 마련이다", "멀 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>다른</u> 사람들이 <strong>비웃을까</strong> <u>봐</u> <strong>겁나요</strong>.<br>B: <u>남들이</u> <strong>비웃</strong>________ 말<strong>비웃</strong>________ <u>자신감을</u> <strong>가지세요</strong>.</p>",
        'explanation': "<p><strong>비웃든지 말든지</strong>: Boshqalar ustidan kuladimi, yo'qmi, bunga e'tibor bermaslikni bildiradi.</p>",
        'correct': "비웃든지 말든지",
        'choices': ["비웃다가는", "비웃어 봤자", "비웃든지 말든지", "비웃는 바람에"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>프로젝트는</u> <u>성공할까요</u>?<br>B: <strong>성공하</strong>________ <strong>실패하</strong>________ <u>끝까지</u> <u>최선을</u> <strong>다하겠습니다</strong>.</p>",
        'explanation': "<p><strong>성공하건 실패하건</strong>: Yutuq yoki mag'lubiyatdan qat'i nazar harakat qilishni ko'rsatadi.</p>",
        'correct': "성공하건 실패하건",
        'choices': ["성공할 뿐만 아니라", "성공하기 무섭게", "성공하건 실패하건", "성공할 지경이다"]
    },
    {
        'text': "<p>A: <u>밥을</u> <strong>먹고</strong> <strong>갈까요</strong>, <u>그냥</u> <strong>갈까요</strong>?<br>B: <strong>먹</strong>________ <u>그냥</u> <strong>가</strong>________ <u>원하는</u> <u>대로</u> <strong>하세요</strong>.</p>",
        'explanation': "<p><strong>먹든지 가든지</strong>: Yeydimi, ketadimi, xohlaganini tanlashi mumkinligini bildiradi.</p>",
        'correct': "먹든지 가든지",
        'choices': ["먹든지 가든지", "먹어 봤자", "먹다가는", "먹는 김에 가는 김에"]
    },
    {
        'text': "<p>A: <u>그</u> <u>조건을</u> <strong>받아들일까요</strong>?<br>B: 조건이 <strong>좋</strong>________ <strong>나쁘</strong>________ <u>무조건</u> <strong>계약해야</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>좋건 나쁘건</strong>: '좋다', '나쁘다' sifatlariga qo'shilib, shart qanday bo'lishidan qat'i nazar kelishish kerakligini ko'rsatadi.</p>",
        'correct': "좋건 나쁘건",
        'choices': ["좋은 탓에 나쁜 탓에", "좋건 나쁘건", "좋을 뿐만 아니라", "좋기 마련이다"]
    },
    {
        'text': "<p>A: 엄마가 <u>잔소리를</u> <u>너무</u> <u>많이</u> <strong>하세요</strong>.<br>B: <u>엄마가</u> <strong>잔소리하</strong>________ 말<strong>하</strong>________ <u>그냥</u> <u>한 귀로</u> <strong>듣고</strong> <strong>흘려요</strong>.</p>",
        'explanation': "<p><strong>잔소리하든지 말든지</strong>: Jerkiydimi-yo'qmi, ahamiyat bermaslikni maslahat beradi.</p>",
        'correct': "잔소리하든지 말든지",
        'choices': ["잔소리하든지 말든지", "잔소리하는 바람에", "잔소리해 봤자", "잔소리하다가는"]
    },
    {
        'text': "<p>A: <u>디자인은</u> <u>어떤</u> <u>걸로</u> <strong>할까요</strong>?<br>B: <strong>화려하</strong>________ <strong>심플하</strong>________ <u>튼튼하기만</u> <strong>하면</strong> <strong>돼요</strong>.</p>",
        'explanation': "<p><strong>화려하건 심플하건</strong>: Dizayn qandayligining farqi yo'q, faqat chidamli bo'lishi muhimligini ko'rsatadi.</p>",
        'correct': "화려하건 심플하건",
        'choices': ["화려한 김에", "화려할 지라도", "화려하건 심플하건", "화려할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>돈이</u> <u>많이</u> <strong>들까요</strong>?<br>B: 돈이 <strong>들</strong>________ <strong>안</strong> <strong>들</strong>________ <u>꼭</u> <strong>배우고</strong> <strong>싶어요</strong>.</p>",
        'explanation': "<p><strong>들든지 안 들든지</strong>: Xarajat bo'ladimi-yo'qmi, qat'i nazar o'rganish xohishini bildiradi.</p>",
        'correct': "들든지 안 들든지",
        'choices': ["드는 탓에", "들다가는", "들든지 안 들든지", "드는 바람에"]
    },
    {
        'text': "<p>A: <u>이</u> <u>문제를</u> <u>어떻게</u> <strong>풀까요</strong>?<br>B: <strong>쉽</strong>________ <strong>어렵</strong>________ <u>혼자</u> <u>힘으로</u> <strong>풀어</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>쉽건 어렵건</strong>: Osonmi-qiyinmi, farqi yo'q o'zi urinib ko'rishi kerakligini ko'rsatadi.</p>",
        'correct': "쉽건 어렵건",
        'choices': ["쉬울 뿐만 아니라", "쉬울 지라도", "쉽건 어렵건", "쉬운 김에"]
    },
    {
        'text': "<p>A: <u>전화를</u> <strong>안</strong> <strong>받는데</strong> <u>계속</u> <strong>할까요</strong>?<br>B: <strong>받</strong>________ <strong>안</strong> <strong>받</strong>________ <u>일단</u> 문자는 <strong>남겨</strong> <strong>두세요</strong>.</p>",
        'explanation': "<p><strong>받든지 안 받든지</strong>: Javob beradimi-yo'qmi qat'i nazar, xabar yozib qoldirishni bildiradi.</p>",
        'correct': "받든지 안 받든지",
        'choices': ["받아 봤자", "받든지 안 받든지", "받는 바람에", "받을 지경이다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>옷이</u> <u>유행에</u> <strong>뒤떨어지지</strong> <strong>않을까요</strong>?<br>B: <u>유행에</u> <strong>맞</strong>________ <strong>안</strong> <strong>맞</strong>________ <u>자기가</u> <strong>좋아하는</strong> <u>옷을</u> <strong>입으세요</strong>.</p>",
        'explanation': "<p><strong>맞건 안 맞건</strong>: Modaga tushadimi-yo'qmi ahamiyatsiz ekanini ko'rsatadi.</p>",
        'correct': "맞건 안 맞건",
        'choices': ["맞건 안 맞건", "맞기 십상이다", "맞는 탓에", "맞을 리가 없다"]
    },
    {
        'text': "<p>A: <u>내일</u> 일찍 <strong>일어날</strong> <u>수</u> <strong>있겠어요</strong>?<br>B: <u>일찍</u> <strong>일어나</strong>________ <u>늦게</u> <strong>일어나</strong>________ <u>알람은</u> <strong>맞춰</strong> <strong>놓을게요</strong>.</p>",
        'explanation': "<p><strong>일어나든지 일어나든지</strong>: Erta turadimi-kechmi qat'i nazar, budilnik qo'yib qo'yishini bildiradi.</p>",
        'correct': "일어나든지 일어나든지",
        'choices': ["일어나는 바람에", "일어날 지경이다", "일어나든지 일어나든지", "일어나다가는"]
    },
    {
        'text': "<p>A: <u>결혼식에</u> <u>사람이</u> <u>많이</u> <strong>올까요</strong>?<br>B: <u>사람이</u> <strong>많</strong>________ <strong>적</strong>________ <u>축하해</u> <strong>주는</strong> <u>마음이</u> <strong>중요하죠</strong>.</p>",
        'explanation': "<p><strong>많건 적건</strong>: '많다', '적다' sifatlariga qo'shilib, odam sonining qizig'i yo'qligini ko'rsatadi.</p>",
        'correct': "많건 적건",
        'choices': ["많은 탓에 적은 탓에", "많을 뿐만 아니라", "많기 마련이다", "많건 적건"]
    },
    {
        'text': "<p>A: <u>그</u> 일을 <strong>계속할</strong> 거예요?<br>B: <u>남들이</u> <strong>칭찬하</strong>________ <strong>비난하</strong>________ <u>제</u> 길을 <strong>가겠습니다</strong>.</p>",
        'explanation': "<p><strong>칭찬하든지 비난하든지</strong>: Maqtaydilarmi, qoralaydilarmi, e'tibor bermaslikni bildiradi.</p>",
        'correct': "칭찬하든지 비난하든지",
        'choices': ["칭찬하든지 비난하든지", "칭찬할 지라도", "칭찬하는 김에", "칭찬해 봤자"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>주말에</u> 비가 <strong>오면</strong> <strong>어떡하죠</strong>?<br>B: <u>날씨가</u> <strong>맑</strong>________ <strong>흐리</strong>________ <u>우리</u> 계획은 <strong>그대로</strong> <strong>진행합니다</strong>.</p>",
        'explanation': "<p><strong>맑건 흐리건</strong>: Havo ochiqmi-bulutlimi qat'i nazar reja o'zgarmasligini ko'rsatadi.</p>",
        'correct': "맑건 흐리건",
        'choices': ["맑을 뿐만 아니라", "맑기 마련이다", "맑건 흐리건", "맑은 탓에"]
    },
    {
        'text': "<p>A: <u>그</u> 친구가 <u>도와줄까요</u>?<br>B: <u>도와주</u>________ <strong>안</strong> <strong>도와주</strong>________ <u>일단</u> <strong>부탁해</strong> <strong>볼게요</strong>.</p>",
        'explanation': "<p><strong>도와주든지 안 도와주든지</strong>: Yordam beradimi-yo'qmi, baribir so'rab ko'rishni bildiradi.</p>",
        'correct': "도와주든지 안 도와주든지",
        'choices': ["도와주는 김에", "도와주다가는", "도와주든지 안 도와주든지", "도와주려던 참이다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>음식이</u> <u>입에</u> <strong>맞을지</strong> <strong>모르겠어요</strong>.<br>B: <strong>맛있</strong>________ <strong>맛없</strong>________ <u>정성껏</u> <strong>만들었으니</strong> <strong>드셔</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>맛있건 맛없건</strong>: Mazalimi-yo'qmi, qat'i nazar tatib ko'rishni tavsiya qilishni ko'rsatadi.</p>",
        'correct': "맛있건 맛없건",
        'choices': ["맛있을 지라도", "맛있건 맛없건", "맛있을 뿐만 아니라", "맛있는 바람에"]
    },
    {
        'text': "<p>A: <u>정말</u> <u>그렇게</u> <strong>말했어요</strong>?<br>B: <u>진실이</u>________ <u>거짓이</u>________ <u>더 이상</u> <strong>관심</strong> <strong>없어요</strong>.</p>",
        'explanation': "<p><strong>진실이든지 거짓이든지</strong>: Otga qo'shilib, rostmi-yolg'onmi ahamiyati yo'qligini bildiradi.</p>",
        'correct': "진실이든지 거짓이든지",
        'choices': ["진실일 지경이다", "진실이든지 거짓이든지", "진실일 리가 없다", "진실에 불과하다"]
    },
    {
        'text': "<p>A: <u>그</u> 일은 <u>위험하지</u> <strong>않아요</strong>?<br>B: <strong>안전하</strong>________ <strong>위험하</strong>________ <u>제가</u> <u>해야</u> <strong>할</strong> <u>일입니다</u>.</p>",
        'explanation': "<p><strong>안전하건 위험하건</strong>: Xavfsizmi-xavflimi, farqi yo'q bajarish shartligini ko'rsatadi.</p>",
        'correct': "안전하건 위험하건",
        'choices': ["안전하건 위험하건", "안전할 뿐만 아니라", "안전하기 무섭게", "안전한 바람에"]
    }
]

# =====================================================================
# Topic 78: 더 나은 대안 선택: 동사 + (느)니 차라리 (...gandan ko'ra yaxshisi... / ...shga qaraganda)
# =====================================================================
topic_78 = [
    {
        'text': "<p>A: <u>주말에</u> <u>복잡한</u> 놀이공원에 <strong>갈까요</strong>?<br>B: 사람 <u>많은</u> <u>곳에서</u> <strong>고생하</strong>________ <u>차라리</u> 집에서 <strong>쉬겠어요</strong>.</p>",
        'explanation': "<p><strong>고생하느니 차라리</strong>: '고생하다' (qiynalmoq) fe'liga qo'shilib, odam ko'p joyda qiynalgandan ko'ra (yomon variant), uyda dam olish (yaxshiroq variant) avzalroqligini bildiradi.</p>",
        'correct': "고생하느니 차라리",
        'choices': ["고생하느니 차라리", "고생해 봤자", "고생하다가는", "고생할 지라도"]
    },
    {
        'text': "<p>A: <u>이</u> <u>음식은</u> <u>버리기</u> <strong>아까우니까</strong> <u>억지로라도</u> <strong>먹을까요</strong>?<br>B: <u>억지로</u> <strong>먹고</strong> <strong>체하</strong>________ <u>차라리</u> <strong>버리는</strong> <u>게</u> <strong>나아요</strong>.</p>",
        'explanation': "<p><strong>체하느니 차라리</strong>: '체하다' (ovqat tiqilib qolmoq) fe'liga qo'shilib, yeb kasal bo'lgandan ko'ra tashlab yuborgan ma'qulligini ko'rsatadi.</p>",
        'correct': "체하느니 차라리",
        'choices': ["체하는 탓에", "체하느니 차라리", "체할 뿐만 아니라", "체하기 무섭게"]
    },
    {
        'text': "<p>A: <u>비싼</u> 돈을 <strong>주고</strong> <u>호텔에서</u> <strong>잘까요</strong>?<br>B: <u>돈을</u> <strong>낭비하</strong>________ <u>차라리</u> <u>저렴한</u> 게스트하우스에서 <strong>자고</strong> 맛있는 <u>걸</u> <strong>먹겠어요</strong>.</p>",
        'explanation': "<p><strong>낭비하느니 차라리</strong>: '낭비하다' (isrof qilmoq) fe'liga qo'shilib, pulni sochgandan ko'ra arzon joyda qolish foydaliligini bildiradi.</p>",
        'correct': "낭비하느니 차라리",
        'choices': ["낭비해 봤자", "낭비했더라면", "낭비하느니 차라리", "낭비하려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> 사람에게 <u>도움을</u> <strong>요청할까요</strong>?<br>B: <u>그</u> <u>사람에게</u> 아쉬운 <u>소리를</u> <strong>하</strong>________ <u>차라리</u> <u>혼자</u> 밤을 <strong>새우겠어요</strong>.</p>",
        'explanation': "<p><strong>하느니 차라리</strong>: '하다' fe'liga qo'shilib, yalingandan ko'ra o'zi qiynalib bajarishi afzalligini ko'rsatadi.</p>",
        'correct': "하느니 차라리",
        'choices': ["하는 김에", "하느니 차라리", "하다가는", "하는 탓에"]
    },
    {
        'text': "<p>A: <u>거짓말을</u> <strong>해서라도</strong> <u>위기를</u> <strong>넘길까요</strong>?<br>B: <u>거짓말을</u> <strong>하</strong>________ <u>차라리</u> <u>솔직하게</u> <strong>말하고</strong> <u>혼나는</u> <u>것이</u> <strong>좋아요</strong>.</p>",
        'explanation': "<p><strong>하느니 차라리</strong>: '하다' fe'liga qo'shilib, yolg'on gapirgandan ko'ra rostini aytib jazo olish ma'qulligini bildiradi.</p>",
        'correct': "하느니 차라리",
        'choices': ["하느니 차라리", "하는 바람에", "해 봤자", "했더라면"]
    },
    {
        'text': "<p>A: <u>이</u> 옷을 <strong>수선해서</strong> <strong>입을까요</strong>?<br>B: <u>수선비가</u> <u>더</u> <strong>나오겠어요</strong>. <strong>수선하</strong>________ <u>차라리</u> <u>새로</u> <u>하나</u> <strong>사는</strong> <u>게</u> <strong>낫겠어요</strong>.</p>",
        'explanation': "<p><strong>수선하느니 차라리</strong>: '수선하다' (ta'mirlamoq) fe'liga qo'shilib, tuzatishga pul ketkazgandan ko'ra yangi olish arzonroq tushishini ko'rsatadi.</p>",
        'correct': "수선하느니 차라리",
        'choices': ["수선하는 김에", "수선하느니 차라리", "수선할 리가 없다", "수선할 뿐만 아니라"]
    },
    {
        'text': "<p>A: 버스가 <u>안</u> <strong>오는데</strong> <u>계속</u> <strong>기다릴까요</strong>?<br>B: <u>추운데</u> <u>밖에서</u> <strong>떨</strong>________ <u>차라리</u> 택시를 <strong>타고</strong> <strong>갑시다</strong>.</p>",
        'explanation': "<p><strong>떠느니 차라리</strong>: '떨다' (qaltiramoq) fe'liga qo'shilib, sovuqda diydiragandan ko'ra taksida ketish yaxshiligini bildiradi.</p>",
        'correct': "떠느니 차라리",
        'choices': ["떠는 바람에", "떠느니 차라리", "떨어 봤자", "떨다가는"]
    },
    {
        'text': "<p>A: <u>마음에</u> <strong>안</strong> <strong>드는</strong> <u>사람과</u> <strong>결혼할</strong> 바에야...<br>B: <u>맞아요</u>. <u>원하지</u> <strong>않는</strong> <u>결혼을</u> <strong>하</strong>________ <u>차라리</u> <u>평생</u> <u>혼자</u> <strong>사는</strong> <u>게</u> <strong>행복해요</strong>.</p>",
        'explanation': "<p><strong>하느니 차라리</strong>: '하다' fe'liga qo'shilib, istamagan inson bilan yashagandan ko'ra yolg'iz o'tish afzalligini ko'rsatadi.</p>",
        'correct': "하느니 차라리",
        'choices': ["하느니 차라리", "하기 무섭게", "하는 탓에", "할 지경이다"]
    },
    {
        'text': "<p>A: <u>대충</u> <strong>만들어서</strong> <u>제출할까요</u>?<br>B: <u>엉터리로</u> <strong>만들</strong>________ <u>차라리</u> 기한을 <strong>연장해</strong> 달라고 <strong>부탁해</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>만들느니 차라리</strong> (yoki 만드느니 차라리 - to'g'ri shakl 만드느니): '만들다' (yaratmoq/qilmoq) fe'liga qo'shilib, chala ish qilgandan ko'ra vaqt so'rash yaxshiligini bildiradi.</p>",
        'correct': "만드느니 차라리",
        'choices': ["만드느니 차라리", "만드는 통에", "만들다가는", "만들어 봤자"]
    },
    {
        'text': "<p>A: <u>그</u> <u>모임에</u> <strong>가기</strong> <u>싫은데</u> <u>어떡하죠</u>?<br>B: <u>가서</u> <u>스트레스</u> <strong>받</strong>________ <u>차라리</u> <strong>아프다고</strong> <strong>핑계</strong> <strong>대고</strong> <strong>가지</strong> <strong>마세요</strong>.</p>",
        'explanation': "<p><strong>받느니 차라리</strong>: '받다' (olmoq) fe'liga qo'shilib, borib siqilgandan ko'ra bahona qilib bormaslik ma'qulligini ko'rsatadi.</p>",
        'correct': "받느니 차라리",
        'choices': ["받았더라면", "받느니 차라리", "받는 김에", "받을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이</u> <u>신발이</u> <u>발이</u> <u>아픈데</u> <u>그냥</u> <strong>신을까요</strong>?<br>B: <u>발이</u> <strong>아픈데</strong> <u>억지로</u> <strong>신</strong>________ <u>차라리</u> <u>맨발로</u> <strong>걷는</strong> <u>게</u> <strong>낫겠어요</strong>.</p>",
        'explanation': "<p><strong>신느니 차라리</strong>: '신다' (kiymoq) fe'liga qo'shilib, azoblanib kiygandan ko'ra yalangoyoq yurish afzalligini bildiradi.</p>",
        'correct': "신느니 차라리",
        'choices': ["신느니 차라리", "신어 봤자", "신다가는", "신는 바람에"]
    },
    {
        'text': "<p>A: 중고 <u>컴퓨터를</u> <strong>살까요</strong>?<br>B: <u>자주</u> <strong>고장 나는</strong> <u>중고를</u> <strong>사</strong>________ <u>차라리</u> <u>돈을</u> <u>더</u> <strong>모아서</strong> <u>새</u> <u>것을</u> <strong>사세요</strong>.</p>",
        'explanation': "<p><strong>사느니 차라리</strong>: '사다' (sotib olmoq) fe'liga qo'shilib, buzuq eski texnika olgandan ko'ra yangisini olish qulayligini ko'rsatadi.</p>",
        'correct': "사느니 차라리",
        'choices': ["사느니 차라리", "샀더라면", "사는 탓에", "살 지경이다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>영화</u> <u>재미없을</u> <u>것</u> <strong>같은데</strong> <strong>볼까요</strong>?<br>B: <u>재미없는</u> <u>영화를</u> <strong>보</strong>________ <u>차라리</u> <u>그</u> <u>시간에</u> <strong>잠을</strong> <strong>자겠어요</strong>.</p>",
        'explanation': "<p><strong>보느니 차라리</strong>: '보다' (ko'rmoq) fe'liga qo'shilib, zerikarli kino ko'rgandan ko'ra uxlash yaxshiligini bildiradi.</p>",
        'correct': "보느니 차라리",
        'choices': ["보느니 차라리", "보아 봤자", "보려던 참이다", "보는 김에"]
    },
    {
        'text': "<p>A: <u>눈치를</u> <strong>보면서</strong> <u>음식을</u> <strong>먹어야</strong> <strong>해요</strong>.<br>B: <u>눈치</u> <strong>보면서</strong> <u>불편하게</u> <strong>먹</strong>________ <u>차라리</u> <strong>굶겠어요</strong>.</p>",
        'explanation': "<p><strong>먹느니 차라리</strong>: '먹다' fe'liga qo'shilib, iymnib ovqatlangan ko'ra och qolish ustunligini ko'rsatadi.</p>",
        'correct': "먹느니 차라리",
        'choices': ["먹다가는", "먹느니 차라리", "먹었더라면", "먹기 무섭게"]
    },
    {
        'text': "<p>A: 길이 <u>막히는데</u> <u>차를</u> <strong>기다릴까요</strong>?<br>B: <u>길에서</u> <u>시간을</u> <strong>버리</strong>________ <u>차라리</u> <u>가까운</u> <u>역까지</u> <strong>걸어갑시다</strong>.</p>",
        'explanation': "<p><strong>버리느니 차라리</strong>: '버리다' (tashlamoq/yo'qotmoq) fe'liga qo'shilib, vaqtni yo'qotgandan ko'ra piyoda yurish ma'qulligini bildiradi.</p>",
        'correct': "버리느니 차라리",
        'choices': ["버리는 탓에", "버려 봤자", "버리느니 차라리", "버릴 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>월급이</u> <u>적은데</u> <u>이</u> <u>회사를</u> <strong>계속</strong> <strong>다닐까요</strong>?<br>B: <u>스트레스만</u> <strong>받으며</strong> <strong>다니</strong>________ <u>차라리</u> <strong>사표를</strong> <strong>내고</strong> <u>이직을</u> <strong>준비하세요</strong>.</p>",
        'explanation': "<p><strong>다니느니 차라리</strong>: '다니다' (qatnamoq/ishlamoq) fe'liga qo'shilib, siqilib ishlagandan ko'ra ishdan bo'shash afzalligini ko'rsatadi.</p>",
        'correct': "다니느니 차라리",
        'choices': ["다니는 김에", "다니느니 차라리", "다니다가는", "다닐 지경이다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>비밀을</u> <u>사람들에게</u> <strong>말할까요</strong>?<br>B: <u>입이</u> <strong>가벼운</strong> <u>사람들에게</u> <strong>말하</strong>________ <u>차라리</u> <u>끝까지</u> <strong>숨기겠어요</strong>.</p>",
        'explanation': "<p><strong>말하느니 차라리</strong>: '말하다' fe'liga qo'shilib, g'iybatchilarga aytgandan ko'ra sir saqlash ma'qulligini bildiradi.</p>",
        'correct': "말하느니 차라리",
        'choices': ["말하는 바람에", "말하느니 차라리", "말해 봤자", "말할 지라도"]
    },
    {
        'text': "<p>A: <u>싸구려</u> <u>물건을</u> <u>여러 개</u> <strong>살까요</strong>?<br>B: <u>금방</u> <strong>망가지는</strong> <u>싸구려를</u> <strong>사</strong>________ <u>차라리</u> <u>비싸도</u> <u>제대로</u> <strong>된</strong> <u>것을</u> <u>하나</u> <strong>사세요</strong>.</p>",
        'explanation': "<p><strong>사느니 차라리</strong>: '사다' fe'liga qo'shilib, arzon va sifatsiz narsa olgandan ko'ra bitta sifatli olgan yaxshiligini ko'rsatadi.</p>",
        'correct': "사느니 차라리",
        'choices': ["사느니 차라리", "샀더라면", "사는 통에", "살 리가 없다"]
    },
    {
        'text': "<p>A: <u>상한</u> <u>우유를</u> <strong>마실까요</strong>?<br>B: <u>배탈이</u> <strong>나서</strong> <strong>고생하</strong>________ <u>차라리</u> <u>돈을</u> <strong>버렸다고</strong> <strong>생각하고</strong> <strong>버리세요</strong>.</p>",
        'explanation': "<p><strong>고생하느니 차라리</strong>: '고생하다' fe'liga qo'shilib, qorin og'rib qiynalgandan ko'ra sutni tashlab yuborish ma'qulligini bildiradi.</p>",
        'correct': "고생하느라고 차라리", # Intentionally matching grammar '느라고' is wrong, should be '느니' - fixing correct answer.
        # Wait, the format is 고생하느니. Let's fix the choice and correct.
        'correct': "고생하느니 차라리",
        'choices': ["고생하느니 차라리", "고생해 봤자", "고생하다가는", "고생하는 바람에"]
    },
    {
        'text': "<p>A: <u>싫어하는</u> <u>과목을</u> <strong>전공할까요</strong>?<br>B: <u>적성에</u> <strong>안</strong> <strong>맞는</strong> <u>공부를</u> <strong>하</strong>________ <u>차라리</u> <u>취업을</u> <u>먼저</u> <strong>하겠어요</strong>.</p>",
        'explanation': "<p><strong>하느니 차라리</strong>: '하다' fe'liga qo'shilib, qiziqmagan sohada o'qigandan ko'ra ishlagan yaxshiligini ko'rsatadi.</p>",
        'correct': "하느니 차라리",
        'choices': ["하는 김에", "하느니 차라리", "하다가는", "할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>돈을</u> <strong>빌려서라도</strong> <u>주식에</u> <strong>투자할까요</strong>?<br>B: <u>빚을</u> <strong>지면서까지</strong> <strong>투자하</strong>________ <u>차라리</u> <u>안전하게</u> <u>적금을</u> <strong>드세요</strong>.</p>",
        'explanation': "<p><strong>투자하느니 차라리</strong>: '투자하다' (sarmoya kiritmoq) fe'liga qo'shilib, qarzga botib tavakkal qilgandan ko'ra pulni bankka qo'ygan afzalligini bildiradi.</p>",
        'correct': "투자하느니 차라리",
        'choices': ["투자하느니 차라리", "투자해 봤자", "투자했더라면", "투자하려던 참이다"]
    },
    {
        'text': "<p>A: <u>매일</u> <strong>야근하는</strong> <u>회사를</u> <strong>다닐까요</strong>?<br>B: <u>개인</u> <u>생활</u> <strong>없이</strong> <u>기계처럼</u> <strong>일하</strong>________ <u>차라리</u> <u>월급이</u> <strong>적어도</strong> <u>편한</u> <u>곳으로</u> <strong>가겠어요</strong>.</p>",
        'explanation': "<p><strong>일하느니 차라리</strong>: '일하다' fe'liga qo'shilib, tinimsiz ishlagandan ko'ra oylik kam bo'lsa ham xotirjam joy afzalligini ko'rsatadi.</p>",
        'correct': "일하느니 차라리",
        'choices': ["일하느니 차라리", "일하는 바람에", "일하다가는", "일할 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> 사람의 <u>변명을</u> <strong>들어줄까요</strong>?<br>B: <u>뻔한</u> <u>거짓말을</u> <strong>듣고</strong> <strong>있</strong>________ <u>차라리</u> <u>벽을</u> <strong>보고</strong> <strong>말하겠어요</strong>.</p>",
        'explanation': "<p><strong>있느니 차라리</strong>: '있다' (turmoq/o'tirmoq) fe'liga qo'shilib, yolg'onni eshitib o'tirgandan ko'ra devorga gapirish ma'qulligini bildiradi.</p>",
        'correct': "있느니 차라리",
        'choices': ["있는 김에", "있느니 차라리", "있어 봤자", "있었더라면"]
    },
    {
        'text': "<p>A: <u>맛없는</u> <u>식당에서</u> <strong>대충</strong> <strong>때울까요</strong>?<br>B: <u>돈</u> <strong>내고</strong> <u>맛없는</u> <u>것을</u> <strong>먹</strong>________ <u>차라리</u> <u>집에</u> <strong>가서</strong> <u>라면을</u> <strong>끓여</strong> <strong>먹겠어요</strong>.</p>",
        'explanation': "<p><strong>먹느니 차라리</strong>: '먹다' fe'liga qo'shilib, pul to'lab bemaza ovqat yegandan ko'ra uyda ramyon yeyish yaxshiligini ko'rsatadi.</p>",
        'correct': "먹느니 차라리",
        'choices': ["먹다가는", "먹느니 차라리", "먹어 봤자", "먹을 리가 없다"]
    },
    {
        'text': "<p>A: <u>잔소리를</u> <strong>들으면서</strong> <u>용돈을</u> <strong>받을까요</strong>?<br>B: <u>눈치</u> <strong>보며</strong> <u>용돈을</u> <strong>받</strong>________ <u>차라리</u> <u>제가</u> <u>아르바이트를</u> <strong>해서</strong> <strong>벌겠어요</strong>.</p>",
        'explanation': "<p><strong>받느니 차라리</strong>: '받다' fe'liga qo'shilib, gap eshitib pul olgandan ko'ra o'zi ishlagani ma'qulligini bildiradi.</p>",
        'correct': "받느니 차라리",
        'choices': ["받느니 차라리", "받는 바람에", "받았더라면", "받기 십상이다"]
    },
    {
        'text': "<p>A: <u>불편한</u> <u>사람과</u> <u>같이</u> <u>여행을</u> <strong>갈까요</strong>?<br>B: <u>여행</u> <strong>내내</strong> <u>신경</u> <strong>쓰며</strong> <strong>다니</strong>________ <u>차라리</u> <u>여행을</u> <strong>취소하겠어요</strong>.</p>",
        'explanation': "<p><strong>다니느니 차라리</strong>: '다니다' (yurmoq) fe'liga qo'shilib, asabiylashib sayohat qilgandan ko'ra uni bekor qilish afzalligini ko'rsatadi.</p>",
        'correct': "다니느니 차라리",
        'choices': ["다녀 봤자", "다니느니 차라리", "다니다가는", "다닐 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이</u> <u>복잡한</u> <u>문제를</u> <u>계속</u> <strong>고민할까요</strong>?<br>B: <strong>해결되지도</strong> <strong>않을</strong> 일을 <strong>붙잡고</strong> <strong>있</strong>________ <u>차라리</u> <u>깨끗하게</u> <strong>포기하는</strong> <u>게</u> <strong>정신건강에</strong> <strong>좋아요</strong>.</p>",
        'explanation': "<p><strong>있느니 차라리</strong>: '있다' fe'liga qo'shilib, hal bo'lmaydigan ishni ushlab o'tirgandan ko'ra voz kechish yaxshiligini bildiradi.</p>",
        'correct': "있느니 차라리",
        'choices': ["있는 탓에", "있느니 차라리", "있을 지경이다", "있어 봤자"]
    },
    {
        'text': "<p>A: <u>조금</u> <strong>다쳤는데</strong> <u>병원을</u> <strong>가지</strong> <strong>말까요</strong>?<br>B: <u>병을</u> <strong>키워서</strong> <u>크게</u> <strong>고생하</strong>________ <u>차라리</u> <u>지금</u> <u>빨리</u> <strong>치료를</strong> <strong>받으세요</strong>.</p>",
        'explanation': "<p><strong>고생하느니 차라리</strong>: '고생하다' fe'liga qo'shilib, kasallikni kuchaytirib qiynalgandan ko'ra hozir davolanish afzalligini ko'rsatadi.</p>",
        'correct': "고생하느니 차라리",
        'choices': ["고생하느니 차라리", "고생하다가는", "고생했더라면", "고생하는 김에"]
    },
    {
        'text': "<p>A: <u>그</u> 사람에게 <u>비밀을</u> <strong>말할까요</strong>?<br>B: <u>비밀이</u> <strong>새어</strong> <strong>나갈까</strong> <u>봐</u> <strong>불안해하</strong>________ <u>차라리</u> <u>아무에게도</u> <strong>말하지</strong> <strong>마세요</strong>.</p>",
        'explanation': "<p><strong>불안해하느니 차라리</strong>: '불안해하다' (xavotirlanmoq) fe'liga qo'shilib, sir ochilishidan qo'rqib yashagandan ko'ra hech kimga aytmaslik ma'qulligini bildiradi.</p>",
        'correct': "불안해하느니 차라리",
        'choices': ["불안해해 봤자", "불안해하느니 차라리", "불안해하다가는", "불안해할 지라도"]
    },
    {
        'text': "<p>A: <u>맛은</u> <strong>없지만</strong> <u>싼</u> <u>커피를</u> <strong>마실까요</strong>?<br>B: <u>맛없는</u> <u>커피를</u> <strong>마시</strong>________ <u>차라리</u> <u>비싸도</u> <u>향이</u> <u>좋은</u> <u>커피를</u> <u>한 잔</u> <strong>마시겠어요</strong>.</p>",
        'explanation': "<p><strong>마시느니 차라리</strong>: '마시다' (ichmoq) fe'liga qo'shilib, bemaza kofe ichgandan ko'ra qimmat bo'lsa-da mazalisini tanlash afzalligini ko'rsatadi.</p>",
        'correct': "마시느니 차라리",
        'choices': ["마시느니 차라리", "마시다가는", "마셔 봤자", "마셨더라면"]
    }
]


# =====================================================================
# Topic 79: 행동의 무의미함: 동사 + (으)나 마나 (Harakatning befoydaligi: ...sa ham, qilmasa ham baribir/foydasiz)
# =====================================================================
topic_79 = [
    {
        'text': "<p>A: <u>지금</u> <strong>뛰어가면</strong> 기차를 <strong>탈</strong> <u>수</u> <strong>있을까요</strong>?<br>B: <u>이미</u> 기차가 <strong>떠나서</strong> <u>지금</u> <strong>뛰어가</strong>________ <strong>소용없어요</strong>.</p>",
        'explanation': "<p><strong>뛰어가나 마나</strong>: '뛰어가다' (yugurib bormoq) fe'liga qo'shilib, poezd ketib bo'lgani uchun yugurib borsa ham, bormasa ham foydasi yo'qligini bildiradi.</p>",
        'correct': "뛰어가나 마나",
        'choices': ["뛰어가나 마나", "뛰어갈 뿐만 아니라", "뛰어가다가는", "뛰어가는 탓에"]
    },
    {
        'text': "<p>A: <u>그</u> 영화가 <strong>재미있을까요</strong>?<br>B: <u>너무</u> <u>뻔한</u> 내용이라서 <strong>보</strong>________ <strong>재미없을</strong> 거예요.</p>",
        'explanation': "<p><strong>보나 마나</strong>: '보다' (ko'rmoq) fe'liga qo'shilib, ko'rsa ham, ko'rmasa ham zerikarli ekani aniqligini ko'rsatadi.</p>",
        'correct': "보나 마나",
        'choices': ["보는 김에", "봤더라면", "보나 마나", "보려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> 분에게 <u>도움을</u> <strong>부탁해</strong> <strong>볼까요</strong>?<br>B: <u>워낙</u> <strong>바쁘신</strong> 분이라 <strong>부탁하</strong>________ <strong>거절하실</strong> 거예요.</p>",
        'explanation': "<p><strong>부탁하나 마나</strong>: '부탁하다' (iltimos qilmoq) fe'liga qo'shilib, so'rasa ham baribir rad etishini bildiradi.</p>",
        'correct': "부탁하나 마나",
        'choices': ["부탁하나 마나", "부탁해 봤자", "부탁하다가는", "부탁하는 바람에"]
    },
    {
        'text': "<p>A: <u>이</u> 약을 <strong>먹으면</strong> <strong>나을까요</strong>?<br>B: <u>유통기한이</u> <strong>지나서</strong> <strong>먹으</strong>________ 효과가 <strong>없을</strong> 거예요.</p>",
        'explanation': "<p><strong>먹으나 마나</strong>: '먹다' (yemoq/ichmoq) fe'liga qo'shilib, muddati o'tgan dorini ichishning foydasi yo'qligini ko'rsatadi.</p>",
        'correct': "먹으나 마나",
        'choices': ["먹는 탓에", "먹으나 마나", "먹을 뿐만 아니라", "먹을 지경이다"]
    },
    {
        'text': "<p>A: <u>저</u> 사람에게 <u>비밀을</u> <strong>말해도</strong> <strong>될까요</strong>?<br>B: <u>입이</u> <strong>가벼워서</strong> <u>비밀을</u> <strong>지켜달라고</strong> <strong>말하</strong>________ <u>다</u> <strong>소문낼</strong> 거예요.</p>",
        'explanation': "<p><strong>말하나 마나</strong>: '말하다' (gapirmoq) fe'liga qo'shilib, aytsa ham baribir hammaga tarqatishini bildiradi.</p>",
        'correct': "말하나 마나",
        'choices': ["말하는 통에", "말할 지라도", "말하나 마나", "말하기 십상이다"]
    },
    {
        'text': "<p>A: <u>지금</u> <strong>전화하면</strong> <strong>받을까요</strong>?<br>B: <u>회의 중이라서</u> <strong>전화하</strong>________ <strong>안</strong> <strong>받을</strong> <u>게</u> <strong>뻔해요</strong>.</p>",
        'explanation': "<p><strong>전화하나 마나</strong>: '전화하다' fe'liga qo'shilib, qo'ng'iroq qilsa ham javob bermasligi aniqligini ko'rsatadi.</p>",
        'correct': "전화하나 마나",
        'choices': ["전화하는 길에", "전화했더라면", "전화하나 마나", "전화하느라고"]
    },
    {
        'text': "<p>A: <u>이</u> 옷을 <strong>입어볼까요</strong>?<br>B: <u>사이즈가</u> <u>너무</u> <strong>작아서</strong> <strong>입어보</strong>________ <strong>안</strong> <strong>맞을</strong> 거예요.</p>",
        'explanation': "<p><strong>입어보나 마나</strong>: '입어보다' (kiyib ko'rmoq) fe'liga qo'shilib, kiyib ko'rsa ham baribir kichkinaligini bildiradi.</p>",
        'correct': "입어보나 마나",
        'choices': ["입어보나 마나", "입어보는 탓에", "입어보려던 참이다", "입어볼 뿐만 아니라"]
    },
    {
        'text': "<p>A: 수미 씨한테 <u>왜</u> <strong>늦었는지</strong> <strong>물어볼까요</strong>?<br>B: <u>매일</u> <strong>늦잠을</strong> <strong>자는</strong> 아이라서 <strong>물어보</strong>________ <strong>늦잠</strong> <strong>잤을</strong> 거예요.</p>",
        'explanation': "<p><strong>물어보나 마나</strong>: '물어보다' (so'ramoq) fe'liga qo'shilib, so'rasa ham javobi ma'lum (uxlab qolgan) ekanini ko'rsatadi.</p>",
        'correct': "물어보나 마나",
        'choices': ["물어보는 바람에", "물어보나 마나", "물어볼 지라도", "물어보기 무섭게"]
    },
    {
        'text': "<p>A: <u>다시</u> <u>한번</u> <strong>찾아볼까요</strong>?<br>B: <u>이미</u> <u>구석구석</u> <u>다</u> <strong>찾아봤기</strong> <u>때문에</u> <u>더</u> <strong>찾아보</strong>________ <strong>없을</strong> 거예요.</p>",
        'explanation': "<p><strong>찾아보나 마나</strong>: '찾아보다' (izlab ko'rmoq) fe'liga qo'shilib, qidirmasa ham yo'qligi aniq ekanini bildiradi.</p>",
        'correct': "찾아보나 마나",
        'choices': ["찾아보는 통에", "찾아봤더라면", "찾아보기 마련이다", "찾아보나 마나"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>일찍</u> <strong>일어날</strong> <u>수</u> <strong>있을까요</strong>?<br>B: <u>알람을</u> <strong>맞춰</strong> <strong>놓으</strong>________ <u>항상</u> <strong>못</strong> <strong>일어나잖아요</strong>.</p>",
        'explanation': "<p><strong>놓으나 마나</strong>: '놓다' (qo'ymoq) fe'liga qo'shilib, budilnik qo'ysa ham baribir turolmasligini ko'rsatadi.</p>",
        'correct': "놓으나 마나",
        'choices': ["놓으나 마나", "놓는 탓에", "놓을 리가 없다", "놓다가는"]
    },
    {
        'text': "<p>A: <u>그</u> <u>책을</u> <strong>읽으면</strong> <u>도움이</u> <strong>될까요</strong>?<br>B: <u>내용이</u> <u>너무</u> <strong>어려워서</strong> <strong>읽으</strong>________ <strong>이해하지</strong> <strong>못할</strong> 거예요.</p>",
        'explanation': "<p><strong>읽으나 마나</strong>: '읽다' (o'qimoq) fe'liga qo'shilib, o'qisa ham tushunmasligi aniqligini bildiradi.</p>",
        'correct': "읽으나 마나",
        'choices': ["읽는 바람에", "읽으나 마나", "읽을 지경이다", "읽고 나서"]
    },
    {
        'text': "<p>A: <u>이</u> <u>고장 난</u> 시계를 <strong>고쳐</strong> <strong>쓸까요</strong>?<br>B: <u>수리비가</u> <u>더</u> 많이 <strong>나와서</strong> <strong>고치</strong>________ <u>새로</u> <strong>사는</strong> <u>게</u> <strong>나아요</strong>.</p>",
        'explanation': "<p><strong>고치나 마나</strong>: '고치다' (tuzatmoq) fe'liga qo'shilib, ta'mirlatsa ham xarajati ko'pligi sababli befoyda ekanini ko'rsatadi.</p>",
        'correct': "고치나 마나",
        'choices': ["고치나 마나", "고치는 탓에", "고쳤더라면", "고치기 무섭게"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>회의에</u> <strong>참석해야</strong> <strong>할까요</strong>?<br>B: <u>중요한</u> 안건이 <strong>없어서</strong> <strong>참석하</strong>________ <u>마찬가지예요</u>.</p>",
        'explanation': "<p><strong>참석하나 마나</strong>: '참석하다' (qatnashmoq) fe'liga qo'shilib, borsa ham, bormasa ham foydasi yo'qligini bildiradi.</p>",
        'correct': "참석하나 마나",
        'choices': ["참석하는 김에", "참석하나 마나", "참석하다가는", "참석할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> 친구에게 <u>조언을</u> <strong>해</strong> <strong>줄까요</strong>?<br>B: <u>고집이</u> <strong>세서</strong> <strong>조언하</strong>________ <u>자기</u> <u>마음대로</u> <strong>할</strong> 거예요.</p>",
        'explanation': "<p><strong>조언하나 마나</strong>: '조언하다' (maslahat bermoq) fe'liga qo'shilib, maslahat bersa ham baribir o'z bilganidan qolmasligini ko'rsatadi.</p>",
        'correct': "조언하나 마나",
        'choices': ["조언하는 바람에", "조언하나 마나", "조언할 지경이다", "조언할 리가 없다"]
    },
    {
        'text': "<p>A: <u>우산이</u> <strong>망가졌는데</strong> <u>그냥</u> <strong>쓸까요</strong>?<br>B: <u>구멍이</u> <u>크게</u> <strong>나서</strong> <strong>쓰</strong>________ <u>다</u> <strong>젖을</strong> 거예요.</p>",
        'explanation': "<p><strong>쓰나 마나</strong>: '쓰다' (taqmoq/yopinmoq) fe'liga qo'shilib, teshik zontikni tutsa ham baribir ho'l bo'lishini bildiradi.</p>",
        'correct': "쓰나 마나",
        'choices': ["쓰나 마나", "쓰는 통에", "썼더라면", "쓰기 십상이다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>화장품을</u> <strong>바르면</strong> <u>피부가</u> <strong>좋아질까요</strong>?<br>B: <u>물을</u> <strong>안</strong> <strong>마시면</strong> <u>아무리</u> <u>좋은</u> 화장품을 <strong>바르</strong>________ 효과가 <strong>없어요</strong>.</p>",
        'explanation': "<p><strong>바르나 마나</strong>: '바르다' (surtmoq) fe'liga qo'shilib, suv ichmasa krem surtishning foydasi yo'qligini ko'rsatadi.</p>",
        'correct': "바르나 마나",
        'choices': ["바르는 탓에", "발랐더라면", "바르나 마나", "바르다가는"]
    },
    {
        'text': "<p>A: <u>지금</u> <strong>세차를</strong> <strong>할까요</strong>?<br>B: <u>내일</u> <u>비가</u> <strong>온대요</strong>. <u>지금</u> <strong>세차하</strong>________ <u>내일이면</u> <u>다시</u> <strong>더러워질</strong> 거예요.</p>",
        'explanation': "<p><strong>세차하나 마나</strong>: '세차하다' (mashina yuvmoq) fe'liga qo'shilib, yuvsa ham ertaga yomg'irda yana iflos bo'lishini bildiradi.</p>",
        'correct': "세차하나 마나",
        'choices': ["세차하나 마나", "세차하는 김에", "세차할 지라도", "세차할 뿐만 아니라"]
    },
    {
        'text': "<p>A: 영수 씨를 <strong>기다릴까요</strong>?<br>B: <u>항상</u> <u>약속을</u> <strong>어기는</strong> <u>사람이라서</u> <strong>기다리</strong>________ <strong>안</strong> <strong>올</strong> 거예요.</p>",
        'explanation': "<p><strong>기다리나 마나</strong>: '기다리다' (kutmoq) fe'liga qo'shilib, kutsa ham baribir kelmasligini ko'rsatadi.</p>",
        'correct': "기다리나 마나",
        'choices': ["기다리는 바람에", "기다렸더라면", "기다리나 마나", "기다리려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> 사람에게 <u>비밀번호를</u> <strong>물어볼까요</strong>?<br>B: <u>절대</u> <strong>안</strong> <strong>알려줄</strong> <u>사람이라서</u> <strong>물어보</strong>________ <u>예요</u>.</p>",
        'explanation': "<p><strong>물어보나 마나</strong>: '물어보다' fe'liga qo'shilib, so'rasa ham baribir aytmasligini bildiradi.</p>",
        'correct': "물어보나 마나",
        'choices': ["물어볼 리가 없다", "물어보기 마련이다", "물어보나 마나", "물어보는 탓에"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>시험인데</u> <u>밤새워서</u> <strong>공부할까요</strong>?<br>B: <u>평소에</u> <strong>안</strong> <strong>했으면</strong> <u>하루</u> <u>밤새워</u> <strong>공부하</strong>________ 성적은 <u>똑같을</u> 거예요.</p>",
        'explanation': "<p><strong>공부하나 마나</strong>: '공부하다' fe'liga qo'shilib, oxirgi tunda o'qishning foydasi yo'qligini ko'rsatadi.</p>",
        'correct': "공부하나 마나",
        'choices': ["공부하는 김에", "공부하나 마나", "공부하다가는", "공부할 지경이다"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>대회에</u> <strong>참가할까요</strong>?<br>B: 연습을 <u>하나도</u> <strong>안</strong> <strong>해서</strong> <strong>참가하</strong>________ <u>꼴찌를</u> <strong>할</strong> <u>게</u> <strong>뻔해요</strong>.</p>",
        'explanation': "<p><strong>참가하나 마나</strong>: '참가하다' (qatnashmoq) fe'liga qo'shilib, tayyorgarliksiz qatnashish befoydaligini bildiradi.</p>",
        'correct': "참가하나 마나",
        'choices': ["참가하나 마나", "참가하는 통에", "참가했더라면", "참가할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이</u> 얼룩을 <u>세제로</u> <strong>지워볼까요</strong>?<br>B: <u>오래된</u> <u>얼룩이라서</u> <strong>지우</strong>________ <strong>안</strong> <strong>지워질</strong> 거예요.</p>",
        'explanation': "<p><strong>지우나 마나</strong>: '지우다' (o'chirmoq) fe'liga qo'shilib, yuvsa ham dog' ketmasligi aniqligini ko'rsatadi.</p>",
        'correct': "지우나 마나",
        'choices': ["지우는 탓에", "지우나 마나", "지웠더라면", "지울 리가 없다"]
    },
    {
        'text': "<p>A: <u>새로운</u> <u>아이디어를</u> <strong>제안해</strong> <strong>볼까요</strong>?<br>B: 부장님은 <u>보수적이라서</u> <strong>제안하</strong>________ <strong>무시당할</strong> 거예요.</p>",
        'explanation': "<p><strong>제안하나 마나</strong>: '제안하다' (taklif qilmoq) fe'liga qo'shilib, fikr bildirsa ham baribir inobatga olinmasligini bildiradi.</p>",
        'correct': "제안하나 마나",
        'choices': ["제안하는 바람에", "제안하나 마나", "제안하다가는", "제안하느라고"]
    },
    {
        'text': "<p>A: <u>가격을</u> <strong>깎아달라고</strong> <strong>해볼까요</strong>?<br>B: <u>할인이</u> <u>절대</u> <strong>안</strong> <strong>되는</strong> <u>가게라서</u> <strong>말하</strong>________ <u>소용없어요</u>.</p>",
        'explanation': "<p><strong>말하나 마나</strong>: '말하다' fe'liga qo'shilib, chegirma so'ragani bilan befoydaligini ko'rsatadi.</p>",
        'correct': "말하나 마나",
        'choices': ["말할 지라도", "말하나 마나", "말하기 무섭게", "말할 지경이다"]
    },
    {
        'text': "<p>A: <u>화가</u> <u>많이</u> <strong>났는데</strong> <u>한마디</u> <strong>할까요</strong>?<br>B: <u>그</u> 사람은 <u>자기</u> <strong>잘못을</strong> <strong>모르는</strong> <u>사람이라서</u> <strong>화내</strong>________ <u>당신만</u> <strong>피곤해져요</strong>.</p>",
        'explanation': "<p><strong>화내나 마나</strong>: '화내다' (jahl qilmoq) fe'liga qo'shilib, urishgan bilan xatosini tushunmasligini bildiradi.</p>",
        'correct': "화내나 마나",
        'choices': ["화내나 마나", "화내는 길에", "화냈더라면", "화내다가는"]
    },
    {
        'text': "<p>A: <u>지금이라도</u> <strong>도망칠까요</strong>?<br>B: <u>이미</u> <u>사방이</u> <strong>포위돼서</strong> <strong>도망치</strong>________ <u>금방</u> <strong>잡힐</strong> 거예요.</p>",
        'explanation': "<p><strong>도망치나 마나</strong>: '도망치다' (qochmoq) fe'liga qo'shilib, qochsa ham baribir ushlanishini ko'rsatadi.</p>",
        'correct': "도망치나 마나",
        'choices': ["도망치는 탓에", "도망치기 십상이다", "도망치나 마나", "도망치려던 참이다"]
    },
    {
        'text': "<p>A: <u>이</u> 서류를 <u>다시</u> <strong>검토해</strong> <strong>볼까요</strong>?<br>B: <u>이미</u> <u>열 번이나</u> <strong>확인했기</strong> <u>때문에</u> <u>더</u> <strong>확인하</strong>________ <u>틀린</u> <u>부분은</u> <strong>없을</strong> 거예요.</p>",
        'explanation': "<p><strong>확인하나 마나</strong>: '확인하다' (tekshirmoq) fe'liga qo'shilib, qayta tekshirishning hojati yo'qligini bildiradi.</p>",
        'correct': "확인하나 마나",
        'choices': ["확인하는 김에", "확인하나 마나", "확인했더라면", "확인할 리가 없다"]
    },
    {
        'text': "<p>A: 강아지한테 <u>기다리라고</u> <strong>훈련시킬까요</strong>?<br>B: <u>식탐이</u> <u>너무</u> <strong>강해서</strong> <strong>가르치</strong>________ <u>간식</u> 앞에서는 <strong>소용없을</strong> 거예요.</p>",
        'explanation': "<p><strong>가르치나 마나</strong>: '가르치다' (o'rgatmoq) fe'liga qo'shilib, o'rgatsa ham baribir ovqat ko'rganda foydasizligini ko'rsatadi.</p>",
        'correct': "가르치나 마나",
        'choices': ["가르치나 마나", "가르치는 탓에", "가르치다가는", "가르칠 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>고장 난</u> 우산을 <u>테이프로</u> <strong>붙여서</strong> <strong>쓸까요</strong>?<br>B: <u>바람이</u> <u>세게</u> <strong>불어서</strong> <strong>붙이</strong>________ <u>다시</u> <strong>망가질</strong> 거예요.</p>",
        'explanation': "<p><strong>붙이나 마나</strong>: '붙이다' (yopishtirmoq) fe'liga qo'shilib, skotchlasa ham baribir buzilib ketishini bildiradi.</p>",
        'correct': "붙이나 마나",
        'choices': ["붙이는 바람에", "붙이나 마나", "붙일 지라도", "붙였더라면"]
    },
    {
        'text': "<p>A: 머리를 <strong>감고</strong> <strong>잘까요</strong>?<br>B: <u>내일</u> <u>아침에</u> <u>어차피</u> <u>운동할</u> <u>거라서</u> <u>지금</u> <strong>감으</strong>________ <u>아침에</u> <u>또</u> <strong>감아야</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>감으나 마나</strong>: '감다' (yuvmoq - sochni) fe'liga qo'shilib, hozir yuvsa ham ertaga yana yuvishga to'g'ri kelishini ko'rsatadi.</p>",
        'correct': "감으나 마나",
        'choices': ["감으나 마나", "감는 탓에", "감기 십상이다", "감으려던 참이다"]
    }
]

# =====================================================================
# Topic 80: 들은 사실의 확인: 동사/형용사 + 다면서요 / 냐면서요 (Birovdan eshitgan ma'lumotni tasdiqlash uchun so'rash)
# =====================================================================
topic_80 = [
    {
        'text': "<p>A: <u>수미 씨가</u> <u>다음 달에</u> <strong>결혼한</strong>________?<br>B: <u>맞아요</u>. <u>저도</u> <u>어제</u> <u>청첩장을</u> <strong>받았어요</strong>.</p>",
        'explanation': "<p><strong>결혼한다면서요</strong>: '결혼하다' (turmush qurmoq) fe'liga qo'shilib, birovdan eshitgan to'y haqidagi xabarni tasdiqlash uchun so'ralayotganini bildiradi.</p>",
        'correct': "결혼한다면서요",
        'choices': ["결혼한다면서요", "결혼할 뿐만 아니라", "결혼하기 무섭게", "결혼할 리가 없다"]
    },
    {
        'text': "<p>A: <u>그</u> 식당 <u>음식이</u> <u>그렇게</u> <strong>맛있</strong>________?<br>B: 네, <u>그래서</u> <u>항상</u> <u>사람이</u> <strong>많아요</strong>.</p>",
        'explanation': "<p><strong>맛있다면서요</strong>: '맛있다' (mazali) sifatiga qo'shilib, ovqati zo'r emish-a deb so'rashni ko'rsatadi.</p>",
        'correct': "맛있다면서요",
        'choices': ["맛있는 탓에", "맛있기 십상이다", "맛있다면서요", "맛있을 지경이다"]
    },
    {
        'text': "<p>A: <u>민수 씨가</u> <u>요즘</u> <u>회사</u> <u>일로</u> <u>많이</u> <strong>바쁘</strong>________?<br>B: 네, <u>새로운</u> <u>프로젝트를</u> <strong>맡아서</strong> <u>야근을</u> <u>자주</u> <strong>한대요</strong>.</p>",
        'explanation': "<p><strong>바쁘다면서요</strong>: '바쁘다' (band bo'lmoq) sifatiga qo'shilib, band deb eshitdim, shundaymi deb tasdiqlashni bildiradi.</p>",
        'correct': "바쁘다면서요",
        'choices': ["바쁜 바람에", "바쁘다면서요", "바쁠 지라도", "바쁘려던 참이다"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>유럽으로</u> <u>출장</u> <strong>가신</strong>________?<br>B: 네, <u>갑자기</u> <u>일이</u> <strong>생겨서</strong> <strong>가게</strong> <strong>됐어요</strong>.</p>",
        'explanation': "<p><strong>가신다면서요</strong>: '가시다' (bormoq - hurmat) fe'liga qo'shilib, xizmat safariga ketayotganligini eshitib so'rashni ko'rsatadi.</p>",
        'correct': "가신다면서요",
        'choices': ["가시는 길에", "가신다면서요", "가실 뿐만 아니라", "가셨더라면"]
    },
    {
        'text': "<p>A: <u>두</u> <u>사람이</u> <u>결국</u> <strong>헤어졌다</strong>________?<br>B: 네, <u>성격</u> <u>차이가</u> <u>너무</u> <strong>심해서</strong> <strong>헤어졌대요</strong>.</p>",
        'explanation': "<p><strong>헤어졌다면서요</strong>: '헤어지다' fe'lining o'tgan zamoniga qo'shilib, ajrashib ketibdi deb eshitdim degan ma'noni beradi.</p>",
        'correct': "헤어졌다면서요",
        'choices': ["헤어졌다면서요", "헤어지는 바람에", "헤어지다가는", "헤어질 리가 없다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>가방이</u> <u>그렇게</u> <strong>비싸</strong>________?<br>B: 네, <u>유명한</u> <u>명품이라서</u> <u>천만 원이</u> <strong>넘어요</strong>.</p>",
        'explanation': "<p><strong>비싸다면서요</strong>: '비싸다' sifatiga qo'shilib, qimmat ekanligini eshitib, to'g'rimi deb so'rashni bildiradi.</p>",
        'correct': "비싸다면서요",
        'choices': ["비싸다면서요", "비싼 탓에", "비싸기 마련이다", "비싸나 마나"]
    },
    {
        'text': "<p>A: <u>제이슨 씨가</u> <u>한국어능력시험에</u> <strong>합격했다</strong>________?<br>B: <u>맞아요</u>. <u>가장</u> <u>높은</u> <u>급수에</u> <strong>합격했다고</strong> <strong>들었어요</strong>.</p>",
        'explanation': "<p><strong>합격했다면서요</strong>: '합격하다' o'tgan zamon shakliga qo'shilib, imtihondan o'tganligini tasdiqlash uchun so'rashni ko'rsatadi.</p>",
        'correct': "합격했다면서요",
        'choices': ["합격할 지라도", "합격했다면서요", "합격하느라고", "합격하기 십상이다"]
    },
    {
        'text': "<p>A: <u>이번에</u> <u>새로</u> <strong>이사한</strong> <u>집이</u> <u>아주</u> <strong>넓</strong>________?<br>B: 네, <u>가족들이</u> <u>다</u> <strong>같이</strong> <strong>살기</strong> <u>좋을</u> <u>만큼</u> <strong>넓어요</strong>.</p>",
        'explanation': "<p><strong>넓다면서요</strong>: '넓다' (keng bo'lmoq) sifatiga qo'shilib, yangi uy keng emish deb eshitganini tasdiqlashni bildiradi.</p>",
        'correct': "넓다면서요",
        'choices': ["넓은 바람에", "넓을 지경이다", "넓다면서요", "넓을 리가 없다"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>축구</u> <u>경기가</u> <u>비 때문에</u> <strong>취소됐다</strong>________?<br>B: 네, <u>비가</u> <u>너무</u> <u>많이</u> <strong>와서</strong> <u>다음 주로</u> <strong>연기됐어요</strong>.</p>",
        'explanation': "<p><strong>취소됐다면서요</strong>: '취소되다' (bekor qilinmoq) o'tgan zamoniga qo'shilib, o'yin qoldirilganini eshitganini ko'rsatadi.</p>",
        'correct': "취소됐다면서요",
        'choices': ["취소됐을 지라도", "취소되는 김에", "취소됐다면서요", "취소됐느니 차라리"]
    },
    {
        'text': "<p>A: <u>지민 씨가</u> <u>오토바이를</u> <strong>타다가</strong> <strong>다쳤다</strong>________?<br>B: 네, <u>다행히</u> <u>크게</u> <strong>다치지는</strong> <strong>않았다고</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>다쳤다면서요</strong>: '다치다' (jarohatlanmoq) fe'liga qo'shilib, jarohat olibdi degan xabarni tasdiqlashni bildiradi.</p>",
        'correct': "다쳤다면서요",
        'choices': ["다쳤다면서요", "다치기 무섭게", "다친 탓에", "다칠 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> <u>영화가</u> <u>그렇게</u> <strong>재미없</strong>________?<br>B: 네, <u>보다가</u> <strong>자는</strong> <u>사람이</u> <strong>많대요</strong>.</p>",
        'explanation': "<p><strong>재미없다면서요</strong>: '재미없다' (zerikarli) sifatiga qo'shilib, kino juda zerikarli ekanligini eshitib so'rashni ko'rsatadi.</p>",
        'correct': "재미없다면서요",
        'choices': ["재미없는 김에", "재미없다면서요", "재미없으려던 참이다", "재미없으나 마나"]
    },
    {
        'text': "<p>A: <u>김 대리님이</u> <u>다음 주에</u> <u>회사를</u> <strong>그만둔</strong>________?<br>B: <u>맞아요</u>. <u>자영업을</u> <strong>시작하신대요</strong>.</p>",
        'explanation': "<p><strong>그만둔다면서요</strong>: '그만두다' (ishdan bo'shamoq) fe'lining hozirgi zamoniga qo'shilib, ishdan ketayotganini eshitganini bildiradi.</p>",
        'correct': "그만둔다면서요",
        'choices': ["그만두는 탓에", "그만둘 지라도", "그만둔다면서요", "그만두기 무섭게"]
    },
    {
        'text': "<p>A: <u>이</u> <u>음식이</u> <u>엄청나게</u> <strong>맵</strong>________?<br>B: 네, <u>매운</u> 것을 <u>잘</u> <strong>먹는</strong> <u>사람도</u> <strong>힘들어한대요</strong>.</p>",
        'explanation': "<p><strong>맵다면서요</strong>: '맵다' (achchiq bo'lmoq) sifatiga qo'shilib, juda achchiq emish-a deb so'rashni ko'rsatadi.</p>",
        'correct': "맵다면서요",
        'choices': ["맵다면서요", "매운 바람에", "매울 리가 없다", "맵기 마련이다"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>산</u> <u>옷이</u> <u>정말</u> <strong>예쁘</strong>________?<br>B: 네, <u>백화점에서</u> <u>세일하길래</u> <u>하나</u> <strong>샀는데</strong> <u>마음에</u> <strong>들어요</strong>.</p>",
        'explanation': "<p><strong>예쁘다면서요</strong>: '예쁘다' sifatiga qo'shilib, kiyim chiroyli deb maqtaganini eshitib so'rashni bildiradi.</p>",
        'correct': "예쁘다면서요",
        'choices': ["예쁠 지경이다", "예쁜 탓에", "예쁘다면서요", "예쁠 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>새로</u> <strong>나온</strong> <u>스마트폰을</u> <strong>샀다</strong>________?<br>B: 네, <u>사전 예약을</u> <strong>해서</strong> <u>어제</u> <strong>받았어요</strong>.</p>",
        'explanation': "<p><strong>샀다면서요</strong>: '사다' o'tgan zamoniga qo'shilib, yangi telefon olibdi deb eshitdim degan ma'noni beradi.</p>",
        'correct': "샀다면서요",
        'choices': ["샀을 지라도", "샀다면서요", "사는 통에", "샀더라면"]
    },
    {
        'text': "<p>A: <u>두</u> <u>사람이</u> <u>요즘</u> <u>몰래</u> <strong>사귄</strong>________?<br>B: <u>쉿</u>! <u>아직</u> <u>회사</u> <u>사람들은</u> <u>아무도</u> <strong>몰라요</strong>.</p>",
        'explanation': "<p><strong>사귄다면서요</strong>: '사귀다' (uchrashib yurmoq) fe'liga qo'shilib, yashirincha gaplashib yurishganini eshitib tasdiqlashni ko'rsatadi.</p>",
        'correct': "사귄다면서요",
        'choices': ["사귀다가는", "사귀나 마나", "사귄다면서요", "사귀려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>호텔이</u> <u>바다가</u> <strong>보여서</strong> <u>경치가</u> <u>정말</u> <strong>좋</strong>________?<br>B: 네, <u>창문을</u> <strong>열면</strong> <u>바로</u> <u>바다가</u> <strong>보인대요</strong>.</p>",
        'explanation': "<p><strong>좋다면서요</strong>: '좋다' sifatiga qo'shilib, manzarasi ajoyib deb eshitdim shundaymi deb so'rashni bildiradi.</p>",
        'correct': "좋다면서요",
        'choices': ["좋기 십상이다", "좋다면서요", "좋은 바람에", "좋을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이번에</u> <u>시험</u> <u>문제가</u> <u>너무</u> <strong>어려웠다</strong>________?<br>B: <u>맞아요</u>. <u>절반 이상이</u> <strong>과락을</strong> <strong>받았다고</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>어려웠다면서요</strong>: '어렵다' o'tgan zamoniga qo'shilib, imtihon qiyin bo'lganini tasdiqlash uchun so'rashni ko'rsatadi.</p>",
        'correct': "어려웠다면서요",
        'choices': ["어려웠을 지라도", "어려운 탓에", "어려웠다면서요", "어렵기 마련이다"]
    },
    {
        'text': "<p>A: <u>한국어</u> <u>배우기가</u> <u>생각보다</u> <strong>쉽다</strong>________?<br>B: <u>처음에는</u> <strong>쉬운데</strong> <u>갈수록</u> <strong>어려워지는</strong> <u>것</u> <strong>같아요</strong>.</p>",
        'explanation': "<p><strong>쉽다면서요</strong>: '쉽다' (oson) sifatiga qo'shilib, oson emish-a deb so'rashni bildiradi.</p>",
        'correct': "쉽다면서요",
        'choices': ["쉽다면서요", "쉬운 바람에", "쉬우려던 참이다", "쉬우나 마나"]
    },
    {
        'text': "<p>A: <u>그</u> <u>상자가</u> <u>엄청</u> <strong>무겁</strong>________?<br>B: 네, <u>혼자서는</u> <u>도저히</u> <strong>들</strong> <u>수</u> <strong>없대요</strong>.</p>",
        'explanation': "<p><strong>무겁다면서요</strong>: '무겁다' sifatiga qo'shilib, og'ir ekanligini eshitib tasdiqlashni ko'rsatadi.</p>",
        'correct': "무겁다면서요",
        'choices': ["무거울 뿐만 아니라", "무겁다면서요", "무거울 리가 없다", "무거운 탓에"]
    },
    {
        'text': "<p>A: <u>내일</u> <u>서울에</u> <u>첫눈이</u> <strong>온</strong>________?<br>B: 네, <u>일기예보에서</u> <u>내일</u> <u>눈이</u> <strong>내린다고</strong> <strong>했어요</strong>.</p>",
        'explanation': "<p><strong>온다면서요</strong>: '오다' fe'liga qo'shilib, qor yog'ishini eshitib, rostmi deb so'rashni bildiradi.</p>",
        'correct': "온다면서요",
        'choices': ["오기 마련이다", "오는 바람에", "온다면서요", "오나 마나"]
    },
    {
        'text': "<p>A: <u>요즘</u> <u>다이어트한다고</u> <u>저녁을</u> <strong>안</strong> <strong>먹는다</strong>________?<br>B: 네, <u>살이</u> <u>너무</u> 많이 <strong>쪄서</strong> <u>저녁은</u> <strong>굶고</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>먹는다면서요</strong>: '먹다' inkor fe'liga qo'shilib, kechqurun ovqatlanmayotganini eshitganini tasdiqlashni ko'rsatadi.</p>",
        'correct': "먹는다면서요",
        'choices': ["먹는다면서요", "먹기 무섭게", "먹다가는", "먹을 지경이다"]
    },
    {
        'text': "<p>A: <u>수미 씨가</u> <u>어제</u> <u>저한테</u> <u>왜</u> 전화를 <strong>안</strong> <strong>받느</strong>________?<br>B: <u>아</u>, <u>제가</u> <u>그때</u> <u>회의에</u> <strong>들어가서</strong> <strong>못</strong> <strong>받았다고</strong> <strong>전해</strong> <strong>주세요</strong>.</p>",
        'explanation': "<p><strong>받냐면서요</strong>: '받다' (javob bermoq - telefonga) fe'liga qo'shilib, nima uchun telefonga javob bermayotganini so'raganini tasdiqlashni bildiradi (Birovning savolini yetkazish).</p>",
        'correct': "받냐면서요",
        'choices': ["받느라고", "받냐면서요", "받을 리가 없다", "받으나 마나"]
    },
    {
        'text': "<p>A: <u>사장님이</u> <u>언제까지</u> <u>보고서를</u> <strong>제출하</strong>________?<br>B: <u>내일</u> <u>오전까지</u> <u>무조건</u> <strong>제출하라고</strong> <strong>하셨어요</strong>.</p>",
        'explanation': "<p><strong>제출하냐면서요</strong>: '제출하다' fe'liga qo'shilib, boshliq qachon topshirish kerak deb so'raganini qayta tasdiqlashni ko'rsatadi.</p>",
        'correct': "제출하냐면서요",
        'choices': ["제출하는 김에", "제출하냐면서요", "제출할 뿐만 아니라", "제출했더라면"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>친구들이</u> <u>왜</u> <u>파티에</u> <strong>안</strong> <strong>왔</strong>________?<br>B: 네, <u>그래서</u> <u>제가</u> <u>다들</u> <strong>바빴다고</strong> <strong>대답했어요</strong>.</p>",
        'explanation': "<p><strong>왔냐면서요</strong>: '오다' inkor o'tgan zamoniga qo'shilib, do'stlari nega kelmaganini so'raganini tasdiqlashni bildiradi.</p>",
        'correct': "왔냐면서요",
        'choices': ["왔을 지경이다", "오는 바람에", "왔냐면서요", "왔을 리가 없다"]
    },
    {
        'text': "<p>A: <u>손님이</u> <u>이</u> <u>물건</u> <u>가격이</u> <u>얼마</u>________?<br>B: <u>5만 원이라고</u> <strong>말씀드렸어요</strong>.</p>",
        'explanation': "<p><strong>얼마냐면서요</strong>: '얼마다' ga qo'shilib, mijoz narxini qancha deb so'raganini tasdiqlashni ko'rsatadi.</p>",
        'correct': "얼마냐면서요",
        'choices': ["얼마냐면서요", "얼마일 뿐만 아니라", "얼마이기 십상이다", "얼마일 리가 없다"]
    },
    {
        'text': "<p>A: <u>선생님이</u> <u>내일</u> <u>숙제가</u> <u>어디까지</u>________?<br>B: <u>50페이지까지라고</u> <strong>알려드렸어요</strong>.</p>",
        'explanation': "<p><strong>어디까지냐면서요</strong>: '어디까지다' ga qo'shilib, o'qituvchi vazifa qayergachaligini so'raganini qayta tasdiqlashni bildiradi.</p>",
        'correct': "어디까지냐면서요",
        'choices': ["어디까지일 지라도", "어디까지냐면서요", "어디까지일 턱이 없다", "어디까지일 뿐이다"]
    },
    {
        'text': "<p>A: <u>경찰이</u> <u>사고</u> <u>당시에</u> <u>무엇을</u> <strong>하고</strong> <strong>있었</strong>________?<br>B: <u>네</u>, <u>그래서</u> <u>길을</u> <strong>건너고</strong> <strong>있었다고</strong> <strong>대답했습니다</strong>.</p>",
        'explanation': "<p><strong>있었냐면서요</strong>: '있다' o'tgan zamoniga qo'shilib, politsiya nima qilayotganini so'raganini tasdiqlashni ko'rsatadi.</p>",
        'correct': "있었냐면서요",
        'choices': ["있었냐면서요", "있기 마련이다", "있는 바람에", "있었더라면"]
    },
    {
        'text': "<p>A: <u>면접관이</u> <u>우리</u> <u>회사에</u> <u>왜</u> <strong>지원했</strong>________?<br>B: <u>그래서</u> <u>제</u> <u>전공을</u> <strong>살리고</strong> <strong>싶다고</strong> <strong>답변했어요</strong>.</p>",
        'explanation': "<p><strong>지원했냐면서요</strong>: '지원하다' (topshirmoq/hujjat bermoq) fe'liga qo'shilib, suhbatdosh nega kompaniyaga kelganini so'raganini tasdiqlashni bildiradi.</p>",
        'correct': "지원했냐면서요",
        'choices': ["지원하는 통에", "지원했냐면서요", "지원하려던 참이다", "지원할 지경이다"]
    },
    {
        'text': "<p>A: <u>어머니가</u> <u>밥은</u> <u>잘</u> <strong>먹고</strong> <strong>다니</strong>________?<br>B: 네, <u>걱정하지</u> <strong>마시라고</strong> <strong>안심시켜</strong> <strong>드렸어요</strong>.</p>",
        'explanation': "<p><strong>다니냐면서요</strong>: '다니다' (bu yerda 밥을 먹고 다니다 - ovqatlanib yurmoq) fe'liga qo'shilib, onasi ovqat yeyapsanmi deb so'raganini qayta tasdiqlashni ko'rsatadi.</p>",
        'correct': "다니냐면서요",
        'choices': ["다니다가는", "다니냐면서요", "다녀 봤자", "다니는 탓에"]
    }
]

# =====================================================================
# Topic 81: 놀라움과 감탄: 동사/형용사 + 다니 / 라니 (Hayratlanish: ... ekan-a! / ... degani!)
# =====================================================================
topic_81 = [
    {
        'text': "<p>A: <u>그</u> <u>두</u> <u>사람이</u> <u>결국</u> <strong>이혼했대요</strong>.<br>B: <u>그렇게</u> <u>사이가</u> <strong>좋았는데</strong> <strong>이혼하</strong>________ <u>정말</u> <strong>믿기지</strong> <strong>않네요</strong>.</p>",
        'explanation': "<p><strong>이혼하다니</strong>: '이혼하다' (ajrashmoq) fe'liga qo'shilib, shunday yaxshi juftlik ajrashibdi-ya, degan hayratni bildiradi.</p>",
        'correct': "이혼하다니",
        'choices': ["이혼하는 탓에", "이혼하다니", "이혼할 지라도", "이혼할 리가 없다"]
    },
    {
        'text': "<p>A: <u>이</u> <u>가방이</u> <u>천만 원이래요</u>.<br>B: <u>조그만</u> <u>가방이</u> <u>그렇게</u> <strong>비싸</strong>________ <u>정말</u> <strong>놀랍네요</strong>.</p>",
        'explanation': "<p><strong>비싸다니</strong>: '비싸다' sifatiga qo'shilib, mitti sumka shunchalik qimmat degan xabardan shok holatini ko'rsatadi.</p>",
        'correct': "비싸다니",
        'choices': ["비싸기 무섭게", "비싸다니", "비쌀 뿐만 아니라", "비싸려던 참이다"]
    },
    {
        'text': "<p>A: <u>민수 씨가</u> <u>어제</u> <u>회사를</u> <strong>그만뒀어요</strong>.<br>B: <u>갑자기</u> <u>회사를</u> <strong>그만두</strong>________ <u>무슨</u> <u>일이</u> <strong>있는</strong> <u>게</u> <strong>분명해요</strong>.</p>",
        'explanation': "<p><strong>그만두다니</strong>: '그만두다' fe'liga qo'shilib, to'satdan ishdan ketibdi-ya degan hayratni bildiradi.</p>",
        'correct': "그만두다니",
        'choices': ["그만두다니", "그만둘 지경이다", "그만두는 김에", "그만둬 봤자"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>기온이</u> <u>영하</u> <u>20도래요</u>.<br>B: <u>아직</u> <u>11월인데</u> <u>벌써</u> <u>영하</u> <u>20도</u>________! <u>너무</u> <strong>추운</strong> <u>거</u> <strong>아니에요</strong>?</p>",
        'explanation': "<p><strong>20도라니</strong>: Ot + 이라니/라니 shaklida bo'lib, hali noyabrda havo 20 gradus sovuq bo'lishi aqlga sig'masligini ko'rsatadi.</p>",
        'correct': "20도라니",
        'choices': ["20도에 불과하다", "20도라니", "20도이기 십상이다", "20도일 턱이 없다"]
    },
    {
        'text': "<p>A: <u>수미 씨가</u> <u>로또</u> <u>1등에</u> <strong>당첨됐대요</strong>.<br>B: <u>세상에</u>, <u>로또</u> <u>1등에</u> <strong>당첨되</strong>________ <u>정말</u> <strong>부럽네요</strong>.</p>",
        'explanation': "<p><strong>당첨되다니</strong>: '당첨되다' fe'liga qo'shilib, lotereya yutibdi-ya degan katta hayrat va havasni bildiradi.</p>",
        'correct': "당첨되다니",
        'choices': ["당첨되는 통에", "당첨됐더라면", "당첨되다니", "당첨될 리가 없다"]
    },
    {
        'text': "<p>A: <u>제이슨 씨가</u> <u>한국어능력시험</u> <u>6급을</u> <strong>받았대요</strong>.<br>B: 한국어 <strong>배운</strong> <u>지</u> <u>1년밖에</u> <strong>안</strong> <strong>됐는데</strong> <u>6급을</u> <strong>받다</strong>________ <u>정말</u> <strong>대단해요</strong>.</p>",
        'explanation': "<p><strong>받다니</strong>: '받다' fe'liga qo'shilib, atigi 1 yilda shunday natija olinganidan hayratni ko'rsatadi.</p>",
        'correct': "받다니",
        'choices': ["받기 마련이다", "받다니", "받으나 마나", "받느라고"]
    },
    {
        'text': "<p>A: <u>믿었던</u> <u>친구가</u> <u>제</u> <u>돈을</u> <strong>훔쳐</strong> <strong>갔어요</strong>.<br>B: <u>친구가</u> <u>돈을</u> <strong>훔치</strong>________ <u>얼마나</u> <strong>배신감이</strong> <strong>들었겠어요</strong>.</p>",
        'explanation': "<p><strong>훔치다니</strong>: '훔치다' (o'g'irlamoq) fe'liga qo'shilib, eng yaqin odami o'g'rilik qilibdi-ya degan dahshatni bildiradi.</p>",
        'correct': "훔치다니",
        'choices': ["훔치다니", "훔쳐 봤자", "훔치는 탓에", "훔치려던 참이다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>식당이</u> <u>위생</u> <u>불량으로</u> <strong>문</strong> <strong>닫았대요</strong>.<br>B: <u>그렇게</u> <u>유명한</u> <u>식당이</u> <u>위생</u> <strong>불량</strong>________ <u>정말</u> <strong>충격적이네요</strong>.</p>",
        'explanation': "<p><strong>불량이라니</strong>: '불량' (yomon holat/sifatsiz) otiga qo'shilib, mashhur restoran iflos bo'lganidan shok holatini ko'rsatadi.</p>",
        'correct': "불량이라니",
        'choices': ["불량일 뿐이다", "불량이라니", "불량이기 십상이다", "불량에 불과하다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>사고로</u> <u>다친</u> <u>사람이</u> <u>한 명도</u> <strong>없대요</strong>.<br>B: <u>차가</u> <u>그렇게</u> <strong>부서졌는데</strong> <u>다친</u> <u>사람이</u> <strong>없</strong>________ <u>정말</u> <u>기적이에요</u>.</p>",
        'explanation': "<p><strong>없다니</strong>: '없다' sifatiga qo'shilib, shuncha halokatdan so'ng hech kim jarohatlanmabdi-ya degan hayratni bildiradi.</p>",
        'correct': "없다니",
        'choices': ["없다니", "없을 지경이다", "없으려던 참이다", "없는 바람에"]
    },
    {
        'text': "<p>A: <u>우리</u> <u>팀이</u> <u>이번</u> <u>대회에서</u> <strong>우승했어요</strong>!<br>B: <u>우리가</u> <strong>우승하</strong>________ <u>꿈만</u> <strong>같아요</strong>.</p>",
        'explanation': "<p><strong>우승하다니</strong>: '우승하다' (g'olib bo'lmoq) fe'liga qo'shilib, chempion bo'lishganidan quvonch va ishonolmaslikni ko'rsatadi.</p>",
        'correct': "우승하다니",
        'choices': ["우승하다가는", "우승했더라면", "우승할지라도", "우승하다니"]
    },
    {
        'text': "<p>A: <u>그</u> <u>배우가</u> <u>올해</u> <u>50살이래요</u>.<br>B: <u>그렇게</u> <strong>젊어</strong> <strong>보이는데</strong> <u>50살이</u>________ <strong>믿을</strong> <u>수</u> <strong>없어요</strong>.</p>",
        'explanation': "<p><strong>50살이라니</strong>: Ot + 이라니 shaklida, yosh ko'rinadigan odamning asli 50 da ekanligidan hayratni bildiradi.</p>",
        'correct': "50살이라니",
        'choices': ["50살이라니", "50살일 턱이 없다", "50살이기 마련이다", "50살에 불과하다"]
    },
    {
        'text': "<p>A: <u>저</u> <u>두</u> <u>사람이</u> <u>형제래요</u>.<br>B: <u>얼굴이</u> <u>하나도</u> <strong>안</strong> <strong>닮았는데</strong> <u>형제</u>________ <u>정말</u> <strong>신기하네요</strong>.</p>",
        'explanation': "<p><strong>형제라니</strong>: Ot + 라니 shaklida, umuman o'xshamaydigan insonlarning aka-uka ekanligidan taajjubni ko'rsatadi.</p>",
        'correct': "형제라니",
        'choices': ["형제라니", "형제일 리가 없다", "형제일 뿐만 아니라", "형제이기 십상이다"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>숙제가</u> <u>100페이지래요</u>.<br>B: <u>숙제가</u> <u>100페이지</u>________! <u>선생님이</u> <u>너무</u> <strong>하시네요</strong>.</p>",
        'explanation': "<p><strong>100페이지라니</strong>: Otga qo'shilib, shuncha ko'p vazifa berilganidan norozilik aralash hayratni bildiradi.</p>",
        'correct': "100페이지라니",
        'choices': ["100페이지일 뿐이다", "100페이지라니", "100페이지일 지라도", "100페이지에 불과하다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>사람이</u> <u>모든</u> <u>재산을</u> <strong>기부했대요</strong>.<br>B: <u>평생</u> <strong>모은</strong> <u>재산을</u> <u>다</u> <strong>기부하</strong>________ <u>정말</u> <strong>존경스럽네요</strong>.</p>",
        'explanation': "<p><strong>기부하다니</strong>: '기부하다' fe'liga qo'shilib, hamma pulini ehson qilibdi-ya degan qoyil qolishni ko'rsatadi.</p>",
        'correct': "기부하다니",
        'choices': ["기부할 뿐만 아니라", "기부하다니", "기부하는 김에", "기부해 봤자"]
    },
    {
        'text': "<p>A: <u>수미 씨가</u> <u>어제</u> <u>저한테</u> <strong>거짓말을</strong> <strong>했어요</strong>.<br>B: <u>수미 씨가</u> <strong>거짓말을</strong> <strong>하</strong>________ <u>그럴</u> <u>사람이</u> <strong>아닌데</strong> <u>이상하네요</u>.</p>",
        'explanation': "<p><strong>하다니</strong>: '하다' fe'liga qo'shilib, uning yolg'on gapirganiga ishonish qiyinligini bildiradi.</p>",
        'correct': "하다니",
        'choices': ["하려던 참이다", "하다니", "하는 탓에", "하기 십상이다"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>비행기</u> <u>표가</u> <u>왕복</u> <u>5만 원이래요</u>.<br>B: <u>해외여행을</u> <strong>가는데</strong> <u>비행기</u> <u>표가</u> <u>5만 원이</u>________ <u>진짜</u> <strong>싸네요</strong>.</p>",
        'explanation': "<p><strong>5만 원이라니</strong>: Otga qo'shilib, aviachiptaning bunday arzon narxda ekanligidan hayratni ko'rsatadi.</p>",
        'correct': "5만 원이라니",
        'choices': ["5만 원이라니", "5만 원일 리가 없다", "5만 원일 따름이다", "5만 원이기 마련이다"]
    },
    {
        'text': "<p>A: <u>내가</u> <strong>믿었던</strong> <u>사람이</u> <u>경쟁사</u> <u>스파이였대요</u>.<br>B: <u>가장</u> <strong>가까운</strong> <u>동료가</u> <u>스파이였</u>________ <u>정말</u> <strong>소름</strong> <strong>돋네요</strong>.</p>",
        'explanation': "<p><strong>스파이였다니</strong>: Ot + 이었다니 (o'tgan zamon) shaklida, eng yaqin hamkasbi josus bo'lganidan dahshatni bildiradi.</p>",
        'correct': "스파이였다니",
        'choices': ["스파이였을 리가 없다", "스파이였다니", "스파이였음에 틀림없다", "스파이였을 뿐이다"]
    },
    {
        'text': "<p>A: <u>아무리</u> <strong>먹어도</strong> <u>살이</u> <strong>안</strong> <strong>찌는</strong> <u>체질이래요</u>.<br>B: <u>그렇게</u> 많이 <strong>먹는데</strong> <u>살이</u> <strong>안</strong> <strong>찌</strong>________ <u>너무</u> <strong>부러워요</strong>.</p>",
        'explanation': "<p><strong>안 찌다니</strong>: '찌다' (semirmoq) inkor fe'liga qo'shilib, shuncha yeb semirmasligidan qattiq havasni ko'rsatadi.</p>",
        'correct': "안 찌다니",
        'choices': ["안 찌다니", "안 찌는 바람에", "안 찔 지라도", "안 찌기 무섭게"]
    },
    {
        'text': "<p>A: <u>그</u> <u>아이는</u> <u>5살인데</u> <u>벌써</u> <u>피아노를</u> <strong>전문가처럼</strong> <strong>친대요</strong>.<br>B: <u>5살짜리</u> <u>꼬마가</u> <u>피아노를</u> <u>그렇게</u> <u>잘</u> <strong>치</strong>________ <u>천재가</u> <strong>분명해요</strong>.</p>",
        'explanation': "<p><strong>치다니</strong>: '치다' fe'liga qo'shilib, mitti bolaning bunday chalishiga qoyil qolishni bildiradi.</p>",
        'correct': "치다니",
        'choices': ["치는 김에", "치다니", "쳐 봤자", "치려던 참이다"]
    },
    {
        'text': "<p>A: <u>결혼식에</u> <u>하객이</u> <u>한 명도</u> <strong>안</strong> <strong>왔대요</strong>.<br>B: <u>결혼식에</u> <u>하객이</u> <u>아무도</u> <strong>없</strong>________ <u>정말</u> <strong>슬픈</strong> <u>일이네요</u>.</p>",
        'explanation': "<p><strong>없다니</strong>: '없다' sifatiga qo'shilib, to'yda mehmon bo'lmasligining o'ta g'alati va ayanchli ekanini ko'rsatadi.</p>",
        'correct': "없다니",
        'choices': ["없다니", "없을 지경이다", "없는 통에", "없기 십상이다"]
    },
    {
        'text': "<p>A: <u>제</u> <u>컴퓨터가</u> <u>바이러스에</u> <strong>감염됐어요</strong>.<br>B: <u>어제</u> <u>새로</u> <strong>산</strong> <u>컴퓨터가</u> <u>벌써</u> <u>바이러스에</u> <strong>감염되</strong>________ <strong>어떡해요</strong>.</p>",
        'explanation': "<p><strong>감염되다니</strong>: '감염되다' fe'liga qo'shilib, yangi narsa darrov buzilganidan afsus va hayratni bildiradi.</p>",
        'correct': "감염되다니",
        'choices': ["감염될 뿐만 아니라", "감염되다니", "감염되는 바람에", "감염됐더라면"]
    },
    {
        'text': "<p>A: <u>그</u> <u>식당</u> <u>김치찌개가</u> <u>10만 원이래요</u>.<br>B: <u>김치찌개</u> <u>한 그릇이</u> <u>10만 원이</u>________ <u>누가</u> <strong>사</strong> <strong>먹겠어요</strong>!</p>",
        'explanation': "<p><strong>10만 원이라니</strong>: Otga qo'shilib, oddiy ovqatning bunchalik qimmatligidan taajjubni ko'rsatadi.</p>",
        'correct': "10만 원이라니",
        'choices': ["10만 원이라니", "10만 원이기 십상이다", "10만 원일 뿐이다", "10만 원일 지라도"]
    },
    {
        'text': "<p>A: <u>민호 씨가</u> <u>약속</u> <u>시간을</u> <u>또</u> <strong>어겼어요</strong>.<br>B: <u>한두 번도</u> <strong>아니고</strong> <u>매번</u> <u>약속을</u> <strong>어기</strong>________ <u>정말</u> <strong>화가</strong> <strong>나네요</strong>.</p>",
        'explanation': "<p><strong>어기다니</strong>: '어기다' fe'liga qo'shilib, odatga aylangan xatodan g'azab aralash hayratni bildiradi.</p>",
        'correct': "어기다니",
        'choices': ["어기다니", "어기다가는", "어기는 탓에", "어길 리가 없다"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>하루 종일</u> <u>아무것도</u> <strong>못</strong> <strong>먹었어요</strong>.<br>B: <u>이</u> <u>밤이</u> <strong>되도록</strong> <u>한 끼도</u> <strong>못</strong> <strong>먹었</strong>________ <u>빨리</u> <u>뭐라도</u> <strong>드세요</strong>.</p>",
        'explanation': "<p><strong>먹었다니</strong>: '먹다' inkor o'tgan zamoniga qo'shilib, shuncha vaqt och yurilganidan xavotir va hayratni ko'rsatadi.</p>",
        'correct': "먹었다니",
        'choices': ["먹으려던 참이다", "먹었다니", "먹으나 마나", "먹었을 뿐이다"]
    },
    {
        'text': "<p>A: <u>강아지가</u> <u>주인을</u> <strong>구하고</strong> <strong>죽었대요</strong>.<br>B: <u>작은</u> <u>동물이</u> <u>주인을</u> <u>위해</u> 목숨을 <strong>바치</strong>________ <u>정말</u> <strong>감동적이에요</strong>.</p>",
        'explanation': "<p><strong>바치다니</strong>: '바치다' (qurbon qilmoq/bag'ishlamoq) fe'liga qo'shilib, kuchukning qahramonligidan hayratni bildiradi.</p>",
        'correct': "바치다니",
        'choices': ["바치기 마련이다", "바칠 뿐만 아니라", "바치다니", "바쳐 봤자"]
    },
    {
        'text': "<p>A: <u>그</u> <u>문제는</u> <u>정답이</u> <strong>없는</strong> <u>문제였대요</u>.<br>B: <u>정답도</u> <strong>없는</strong> <u>문제를</u> <u>시험에</u> <strong>내</strong>________ <u>학생들이</u> <u>얼마나</u> <strong>황당했을까요</strong>.</p>",
        'explanation': "<p><strong>내다니</strong>: '내다' (imtihonda tushirmoq) fe'liga qo'shilib, noto'g'ri savol berilganidan hayron qolishni ko'rsatadi.</p>",
        'correct': "내다니",
        'choices': ["내기 십상이다", "내는 통에", "내다니", "낼 리가 없다"]
    },
    {
        'text': "<p>A: <u>제가</u> <u>만든</u> <u>음식을</u> <u>다</u> <strong>버렸대요</strong>.<br>B: <u>정성껏</u> <strong>만든</strong> <u>음식을</u> <u>한 입도</u> <strong>안</strong> <strong>먹고</strong> <strong>버리</strong>________ <u>너무</u> <strong>하네요</strong>.</p>",
        'explanation': "<p><strong>버리다니</strong>: '버리다' fe'liga qo'shilib, tayyor ovqatni tashlab yuborganiga g'azab va hayratni bildiradi.</p>",
        'correct': "버리다니",
        'choices': ["버리기 무섭게", "버릴 지경이다", "버리다니", "버린 김에"]
    },
    {
        'text': "<p>A: <u>휴대폰을</u> <u>산 지</u> <u>하루 만에</u> <strong>잃어버렸어요</strong>.<br>B: <u>새</u> <u>휴대폰을</u> <u>하루 만에</u> <strong>분실하</strong>________ <u>정말</u> <strong>속상하겠어요</strong>.</p>",
        'explanation': "<p><strong>분실하다니</strong>: '분실하다' (yo'qotmoq) fe'liga qo'shilib, yangi telefon darrov yo'qolganidan achinish aralash taajjubni ko'rsatadi.</p>",
        'correct': "분실하다니",
        'choices': ["분실하다니", "분실하는 탓에", "분실했더라면", "분실해 봤자"]
    },
    {
        'text': "<p>A: <u>저희</u> <u>할아버지가</u> <u>올해</u> <u>100세십니다</u>.<br>B: <u>100세</u>________! <u>정말</u> <strong>정정해</strong> <strong>보이시네요</strong>.</p>",
        'explanation': "<p><strong>100세시라니</strong>: Ot + (이)시라니 (hurmat shakli), yuz yoshga kirganidan cheksiz hurmat va hayratni bildiradi.</p>",
        'correct': "100세시라니",
        'choices': ["100세에 불과하다", "100세시라니", "100세일 뿐이다", "100세일 리가 없다"]
    },
    {
        'text': "<p>A: <u>그</u> <u>유명한</u> <u>그림이</u> <u>가짜였대요</u>.<br>B: <u>박물관에</u> <strong>전시된</strong> <u>작품이</u> <u>위작이었</u>________ <u>전 세계가</u> <strong>속았네요</strong>.</p>",
        'explanation': "<p><strong>위작이었다니</strong>: Ot + 이었다니, mashhur asar qalbaki bo'lib chiqqanidan qattiq taajjubni ko'rsatadi.</p>",
        'correct': "위작이었다니",
        'choices': ["위작이었을 지라도", "위작이었다니", "위작이기 마련이다", "위작이려던 참이다"]
    }
]

# =====================================================================
# Topic 82: 당연한 추측과 짐작: 동사/형용사 + (으)려니 하다 (...deb o'ylamoq / ...qilsa kerak deb taxmin qilmoq)
# =====================================================================
topic_82 = [
    {
        'text': "<p>A: <u>어제</u> <u>왜</u> 저한테 연락 <strong>안</strong> <strong>했어요</strong>?<br>B: <u>많이</u> <strong>바쁘</strong>________ <u>일부러</u> <strong>안</strong> <strong>했어요</strong>.</p>",
        'explanation': "<p><strong>바쁘려니 하고</strong>: '바쁘다' (band bo'lmoq) sifatiga qo'shilib, uni band bo'lsa kerak deb o'ylab (tabiiy taxmin) bezovta qilmaganini bildiradi.</p>",
        'correct': "바쁘려니 하고",
        'choices': ["바쁜 탓에", "바쁘려니 하고", "바쁠 지라도", "바쁘다가는"]
    },
    {
        'text': "<p>A: <u>우산은</u> <u>왜</u> <strong>가져왔어요</strong>?<br>B: <u>오후에</u> 비가 <strong>오</strong>________ <u>미리</u> <strong>챙겨</strong> <strong>왔어요</strong>.</p>",
        'explanation': "<p><strong>오려니 하고</strong>: '오다' (kelmoq/yog'moq) fe'liga qo'shilib, yomg'ir yog'sa kerak deb taxmin qilib zontik olganini ko'rsatadi.</p>",
        'correct': "오려니 하고",
        'choices': ["오는 김에", "오려니 하고", "오기 십상이라서", "오자마자"]
    },
    {
        'text': "<p>A: <u>이</u> <u>문제는</u> <u>혼자</u> <strong>풀었나요</strong>?<br>B: 네, <u>당연히</u> <strong>아시</strong>________ <u>그냥</u> <strong>넘어갔어요</strong>.</p>",
        'explanation': "<p><strong>아시려니 하고</strong>: '아시다' (bilmoq - hurmat) fe'liga qo'shilib, buni bilsa kerak deb o'ylab indamay o'tib ketganini bildiradi.</p>",
        'correct': "아시려니 하고",
        'choices': ["아시는 탓에", "아실 뿐만 아니라", "아시려니 하고", "아시느라고"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <u>비싼</u> 옷을 <u>그냥</u> <strong>샀어요</strong>?<br>B: <u>비싼</u> 만큼 품질이 <strong>좋으</strong>________ <strong>샀어요</strong>.</p>",
        'explanation': "<p><strong>좋으려니 하고</strong>: '좋다' (yaxshi bo'lmoq) sifatiga qo'shilib, narxiga yarasha sifati ham yaxshi bo'lsa kerak deb umid qilganini ko'rsatadi.</p>",
        'correct': "좋으려니 하고",
        'choices': ["좋을 지경이라서", "좋기 마련이라서", "좋으려니 하고", "좋은 바람에"]
    },
    {
        'text': "<p>A: <u>아직도</u> <u>그</u> 사람이 <strong>올</strong> <u>거라고</u> <strong>생각해요</strong>?<br>B: <u>약속을</u> <strong>했으니</strong> <strong>오</strong>________ <strong>기다리고</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>오려니 하고</strong>: '오다' fe'liga qo'shilib, va'da bergani uchun keladi deb umid qilib kutayotganini bildiradi.</p>",
        'correct': "오려니 하고",
        'choices': ["오려니 하고", "오는 바람에", "오느라고", "올 턱이 없어서"]
    },
    {
        'text': "<p>A: 친구가 <u>약속</u> 시간에 <u>많이</u> <strong>늦네요</strong>.<br>B: 길이 <strong>막히</strong>________ <u>조금만</u> <u>더</u> <strong>기다려</strong> <strong>봅시다</strong>.</p>",
        'explanation': "<p><strong>막히려니 하고</strong>: '막히다' (tiqilmoq) fe'liga qo'shilib, yo'l tirband bo'lsa kerak deb o'ylab sabr qilishni ko'rsatadi.</p>",
        'correct': "막히려니 하고",
        'choices': ["막혔더라면", "막히는 탓에", "막히려니 하고", "막힐 지경이라서"]
    },
    {
        'text': "<p>A: <u>갑자기</u> <u>왜</u> <u>말을</u> <strong>멈췄어요</strong>?<br>B: 제 <u>마음을</u> <strong>이해해주</strong>________ <u>더 이상</u> 설명 <strong>안</strong> <strong>했어요</strong>.</p>",
        'explanation': "<p><strong>이해해주려니 하고</strong>: '이해해주다' (tushunib bermoq) fe'liga qo'shilib, meni tushunar deb o'ylab gapni to'xtatganini bildiradi.</p>",
        'correct': "이해해주려니 하고",
        'choices': ["이해해주려니 하고", "이해해줄 리가 없어서", "이해해주기 무섭게", "이해해주는 김에"]
    },
    {
        'text': "<p>A: <u>그</u> <u>식당에</u> <strong>예약은</strong> <strong>했어요</strong>?<br>B: <u>아니요</u>, 자리가 <strong>있으</strong>________ <u>그냥</u> <strong>왔어요</strong>.</p>",
        'explanation': "<p><strong>있으려니 하고</strong>: '있다' (bor bo'lmoq) fe'liga qo'shilib, joy topilib qolar deb o'ylab kelganini ko'rsatadi.</p>",
        'correct': "있으려니 하고",
        'choices': ["있으려던 참이라서", "있으려니 하고", "있는 탓에", "있을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>이</u> <u>음식이</u> <u>입에</u> <strong>맞으세요</strong>?<br>B: 네, <u>처음에는</u> <strong>맵으</strong>________ <strong>먹었는데</strong> <u>맛있네요</u>.</p>",
        'explanation': "<p><strong>맵으려니 하고</strong> (yoki 매울 것이라 생각하고 - grammatik jihatdan 맵다 + (으)려니 -> 매워려니/매우려니 -> 표준어는 '매우려니 하고' dir): Achchiq bo'lsa kerak deb o'ylab yeganini bildiradi. <em>(Izoh: '맵다' ning to'g'ri shakli '매우려니' bo'ladi)</em></p>",
        'correct': "매우려니 하고",
        'choices': ["매운 탓에", "매운 김에", "매우려니 하고", "매울 지라도"]
    },
    {
        'text': "<p>A: 시험이 <u>어려울까</u> <u>봐</u> <u>걱정이에요</u>.<br>B: <u>모두에게</u> <strong>어려우</strong>________ <u>마음</u> <strong>편하게</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>어려우려니 하고</strong>: '어렵다' sifatiga qo'shilib, hammaga birdek qiyin bo'lsa kerak deb xotirjam bo'lishga chaqiradi.</p>",
        'correct': "어려우려니 하고",
        'choices': ["어려울 리가 없어서", "어려우려니 하고", "어려운 통에", "어려웠더라면"]
    },
    {
        'text': "<p>A: <u>아까</u> <u>제가</u> <strong>인사했는데</strong> <strong>못</strong> <strong>보셨어요</strong>?<br>B: <u>죄송해요</u>. <u>다른</u> <u>사람이</u> <strong>인사하</strong>________ <u>그냥</u> <strong>지나쳤어요</strong>.</p>",
        'explanation': "<p><strong>인사하려니 하고</strong>: '인사하다' (salomlashmoq) fe'liga qo'shilib, boshqa odam salom beryapti deb o'ylaganini ko'rsatadi.</p>",
        'correct': "인사하려니 하고",
        'choices': ["인사하는 바람에", "인사할 지라도", "인사하려니 하고", "인사하느라고"]
    },
    {
        'text': "<p>A: <u>방이</u> <u>너무</u> <strong>춥지</strong> <strong>않아요</strong>?<br>B: <u>금방</u> <strong>따뜻해지</strong>________ <strong>기다리고</strong> <strong>있었어요</strong>.</p>",
        'explanation': "<p><strong>따뜻해지려니 하고</strong>: '따뜻해지다' (isimoq) fe'liga qo'shilib, tezda isib ketar deb o'ylab kutganini bildiradi.</p>",
        'correct': "따뜻해지려니 하고",
        'choices': ["따뜻해지는 통에", "따뜻해지려니 하고", "따뜻해지기 십상이라서", "따뜻해질 리가 없어서"]
    },
    {
        'text': "<p>A: <u>수미 씨가</u> <u>아까부터</u> <u>조용하네요</u>.<br>B: <u>많이</u> <strong>피곤하</strong>________ <u>말을</u> <strong>안</strong> <strong>걸고</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>피곤하려니 하고</strong>: '피곤하다' (charchamoq) sifatiga qo'shilib, charchagan bo'lsa kerak deb gapirtirmayotganini ko'rsatadi.</p>",
        'correct': "피곤하려니 하고",
        'choices': ["피곤하려니 하고", "피곤한 김에", "피곤할 뿐만 아니라", "피곤할 지경이라서"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>그렇게</u> <u>여유롭게</u> <strong>출발해요</strong>?<br>B: 지하철이 <u>제시간에</u> <strong>오</strong>________ <u>여유를</u> <strong>부렸어요</strong>.</p>",
        'explanation': "<p><strong>오려니 하고</strong>: '오다' fe'liga qo'shilib, poyezd vaqtida kelar deb o'ylab shoshmaganini bildiradi.</p>",
        'correct': "오려니 하고",
        'choices': ["오는 탓에", "올 뿐만 아니라", "오려니 하고", "오기 마련이라서"]
    },
    {
        'text': "<p>A: <u>저</u> <u>사람이</u> <u>거짓말을</u> <strong>할지도</strong> <strong>몰라요</strong>.<br>B: <u>설마</u> <strong>속이</strong>________ <strong>믿었는데</strong> <strong>배신당했네요</strong>.</p>",
        'explanation': "<p><strong>속이려니 하고</strong>: '속이다' (aldamoq) inkor bilan (설마 속이랴 하고 yoki 안 속이려니 하고) qo'llaniladi. Bu yerda '설마 속이랴 하고' (nahotki aldar deb) varianti ham bo'lishi mumkin, lekin `(으)려니` qoidasi bo'yicha `속이지 않으려니 하고` (aldamas deb o'ylab) ishlatiladi.</p>",
        'correct': "않으려니 하고",
        'choices': ["않기 무섭게", "않으려니 하고", "않는 바람에", "않다가는"]
    },
    {
        'text': "<p>A: 택배가 <u>안</u> <strong>도착했어요</strong>.<br>B: <u>내일쯤</u> <strong>오</strong>________ <u>조금만</u> <u>더</u> <strong>기다려</strong> <strong>보세요</strong>.</p>",
        'explanation': "<p><strong>오려니 하고</strong>: '오다' fe'liga qo'shilib, ertaga kelib qolar deb o'ylab kutishni maslahat beradi.</p>",
        'correct': "오려니 하고",
        'choices': ["오는 김에", "오는 탓에", "오려니 하고", "올 지라도"]
    },
    {
        'text': "<p>A: 김 대리님은 <u>왜</u> <strong>안</strong> <strong>보이세요</strong>?<br>B: <u>알아서</u> <u>잘</u> <strong>하시</strong>________ <u>따로</u> <strong>찾지</strong> <strong>않았어요</strong>.</p>",
        'explanation': "<p><strong>하시려니 하고</strong>: '하시다' (qilmoq - hurmat) fe'liga qo'shilib, o'zlari bilib qilarlar deb o'ylab qidirmaganini ko'rsatadi.</p>",
        'correct': "하시려니 하고",
        'choices': ["하시는 탓에", "하시려니 하고", "하실 뿐만 아니라", "하시느라고"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <u>비싼</u> <u>컴퓨터가</u> <u>정말</u> <strong>필요해요</strong>?<br>B: <u>작업</u> <u>속도가</u> <strong>빠르</strong>________ <u>비싸도</u> <strong>샀어요</strong>.</p>",
        'explanation': "<p><strong>빠르려니 하고</strong>: '빠르다' (tez bo'lmoq) sifatiga qo'shilib, ishlash tezligi yuqori bo'lsa kerak deb o'ylab sotib olganini bildiradi.</p>",
        'correct': "빠르려니 하고",
        'choices': ["빠른 탓에", "빠르려던 참이라서", "빠르려니 하고", "빠를 지경이라서"]
    },
    {
        'text': "<p>A: <u>두</u> <u>분이</u> <u>사귀는</u> <u>것을</u> <u>모르셨어요</u>?<br>B: 네, <u>그냥</u> <u>친한</u> <u>친구</u> <strong>사이이</strong>________ <u>전혀</u> <strong>의심하지</strong> <strong>않았어요</strong>.</p>",
        'explanation': "<p><strong>사이이려니 하고</strong>: '사이이다' (munosabatda bo'lmoq) ga qo'shilib, shunchaki yaqin do'st bo'lishsa kerak deb o'ylaganini ko'rsatadi.</p>",
        'correct': "사이이려니 하고",
        'choices': ["사이이려니 하고", "사이이기 십상이라서", "사이일 뿐만 아니라", "사이일 지라도"]
    },
    {
        'text': "<p>A: 아기가 <u>울어도</u> <u>그냥</u> <strong>두시네요</strong>.<br>B: <u>금방</u> <strong>그치</strong>________ <strong>지켜보고</strong> <strong>있어요</strong>.</p>",
        'explanation': "<p><strong>그치려니 하고</strong>: '그치다' (tinmoq) fe'liga qo'shilib, tezda yig'idan to'xtar deb o'ylab qarab turganini bildiradi.</p>",
        'correct': "그치려니 하고",
        'choices': ["그칠 리가 없어서", "그치려니 하고", "그치기 마련이라서", "그치는 바람에"]
    },
    {
        'text': "<p>A: 발표 <u>준비를</u> <u>하나도</u> <strong>안</strong> <strong>했어요</strong>?<br>B: <u>다른</u> <u>팀원들이</u> <u>다</u> <strong>준비했으</strong>________ <u>마음</u> <strong>놓고</strong> <strong>있었어요</strong>.</p>",
        'explanation': "<p><strong>준비했으려니 하고</strong>: '준비하다' o'tgan zamoniga qo'shilib, boshqalar tayyorlab qo'ygandir deb xotirjam bo'lganini ko'rsatadi.</p>",
        'correct': "준비했으려니 하고",
        'choices': ["준비했으려니 하고", "준비했던 탓에", "준비했더라면", "준비했을 지경이라서"]
    },
    {
        'text': "<p>A: <u>왜</u> 길을 <strong>물어보지</strong> <strong>않았어요</strong>?<br>B: <u>내비게이션이</u> <u>알아서</u> <strong>안내해주</strong>________ <u>그냥</u> <strong>따라갔어요</strong>.</p>",
        'explanation': "<p><strong>안내해주려니 하고</strong>: '안내해주다' (yo'l ko'rsatib bermoq) fe'liga qo'shilib, GPS to'g'ri olib boradi deb ishonib yurganini bildiradi.</p>",
        'correct': "안내해주려니 하고",
        'choices': ["안내해주는 김에", "안내해주려니 하고", "안내해주기 십상이라서", "안내해주는 바람에"]
    },
    {
        'text': "<p>A: <u>그</u> <u>배우가</u> <u>결혼한다는</u> <u>기사를</u> <strong>봤어요</strong>?<br>B: <u>에이</u>, <u>또</u> <u>가짜</u> <strong>뉴스이</strong>________ <strong>생각했어요</strong>.</p>",
        'explanation': "<p><strong>뉴스이려니 하고</strong>: '뉴스이다' (yangilik bo'lmoq) ga qo'shilib, yana yolg'on xabar bo'lsa kerak deb o'ylaganini ko'rsatadi.</p>",
        'correct': "뉴스이려니 하고",
        'choices': ["뉴스일 리가 없어서", "뉴스이려니 하고", "뉴스일 턱이 없어서", "뉴스이기 무섭게"]
    },
    {
        'text': "<p>A: 상처가 <strong>났는데</strong> <u>약은</u> <strong>발랐어요</strong>?<br>B: <u>시간이</u> <strong>지나면</strong> <u>자연스럽게</u> <strong>낫으</strong>________ <u>그냥</u> <strong>두었어요</strong>.</p>",
        'explanation': "<p><strong>나으려니 하고</strong> (낫다 -> 나으려니): '낫다' (tuzalmoq) fe'liga qo'shilib, o'zi tuzalib ketar deb o'ylab dori surtmaganini bildiradi.</p>",
        'correct': "나으려니 하고",
        'choices': ["낫는 탓에", "나으려니 하고", "나았더라면", "나을 지경이라서"]
    },
    {
        'text': "<p>A: <u>오늘</u> <u>모임에</u> <u>사람들이</u> <u>많이</u> <strong>안</strong> <strong>왔네요</strong>.<br>B: <u>주말이라서</u> <u>다들</u> <strong>쉬</strong>________ <u>저도</u> <u>혼자</u> <strong>왔어요</strong>.</p>",
        'explanation': "<p><strong>쉬려니 하고</strong>: '쉬다' (dam olmoq) fe'liga qo'shilib, hamma dam olayotgan bo'lsa kerak deb o'ylaganini ko'rsatadi.</p>",
        'correct': "쉬려니 하고",
        'choices': ["쉬는 탓에", "쉬려던 참이라서", "쉬려니 하고", "쉬기 십상이라서"]
    },
    {
        'text': "<p>A: 가격을 <strong>안</strong> <strong>보고</strong> <u>물건을</u> <strong>골랐어요</strong>?<br>B: <u>세일</u> <u>기간이라서</u> <strong>싸</strong>________ <u>여러 개</u> <strong>집었어요</strong>.</p>",
        'explanation': "<p><strong>싸려니 하고</strong>: '싸다' (arzon bo'lmoq) sifatiga qo'shilib, arzon bo'lsa kerak deb o'ylab ko'p narsa tanlaganini bildiradi.</p>",
        'correct': "싸려니 하고",
        'choices': ["싸기 마련이라서", "싸려니 하고", "싼 통에", "쌀 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <u>무거운</u> <u>짐을</u> <u>혼자서</u> <strong>들었어요</strong>?<br>B: <u>조금만</u> <strong>가면</strong> <strong>되</strong>________ <u>무리해서</u> <strong>들었어요</strong>.</p>",
        'explanation': "<p><strong>되려니 하고</strong>: '되다' (bo'lmoq/yetarli bo'lmoq) fe'liga qo'shilib, ozgina qoldi-ku deb o'ylab qiynalib ko'targanini ko'rsatadi.</p>",
        'correct': "되려니 하고",
        'choices': ["되는 탓에", "될 지라도", "되려니 하고", "될 리가 없어서"]
    },
    {
        'text': "<p>A: <u>그</u> 책 <u>다</u> <strong>읽었어요</strong>?<br>B: <u>내용이</u> <strong>재미있으</strong>________ <strong>샀는데</strong> <u>너무</u> <strong>지루해서</strong> <strong>덮었어요</strong>.</p>",
        'explanation': "<p><strong>재미있으려니 하고</strong>: '재미있다' sifatiga qo'shilib, qiziqarli bo'lsa kerak deb sotib olganini bildiradi.</p>",
        'correct': "재미있으려니 하고",
        'choices': ["재미있으려니 하고", "재미있을 뿐만 아니라", "재미있기 무섭게", "재미있으려던 참이라서"]
    },
    {
        'text': "<p>A: 김치찌개에 <u>물을</u> <u>왜</u> <u>이렇게</u> 많이 <strong>넣었어요</strong>?<br>B: <u>찌개가</u> <u>너무</u> <strong>짜</strong>________ <u>물을</u> <u>조금</u> <u>더</u> <strong>부었어요</strong>.</p>",
        'explanation': "<p><strong>짜려니 하고</strong>: '짜다' (sho'r bo'lmoq) sifatiga qo'shilib, sho'r bo'lib qolsa kerak deb o'ylab suv qo'shganini ko'rsatadi.</p>",
        'correct': "짜려니 하고",
        'choices': ["짠 탓에", "짜려니 하고", "짤 지라도", "짜다가는"]
    },
    {
        'text': "<p>A: <u>비밀을</u> <strong>말해도</strong> <u>입이</u> <strong>무거울까요</strong>?<br>B: <u>입이</u> <strong>무거우</strong>________ <strong>말했는데</strong> <u>다음 날</u> <u>소문이</u> <u>다</u> <strong>났어요</strong>.</p>",
        'explanation': "<p><strong>무거우려니 하고</strong>: '무겁다' (og'ir bo'lmoq - sir saqlamoq) sifatiga qo'shilib, sir saqlasa kerak deb ishonganini bildiradi.</p>",
        'correct': "무거우려니 하고",
        'choices': ["무겁기 마련이라서", "무거울 뿐만 아니라", "무거우려니 하고", "무거운 바람에"]
    }
]

# =====================================================================
# Topic 83: 원망이나 탓: 명사 + (이)랍시고 / 동사 + (으)ㄴ/는답시고 (O'zicha ... qilib / ... deb yordam bermoqchi bo'ldi-yu, lekin ziyon qildi)
# =====================================================================
topic_83 = [
    {
        'text': "<p>A: <u>왜</u> <u>그렇게</u> <strong>화가</strong> <strong>났어요</strong>?<br>B: <u>친구가</u> 저를 <strong>위로한</strong>________ <strong>한</strong> <u>말이</u> <u>오히려</u> <u>상처가</u> <strong>됐거든요</strong>.</p>",
        'explanation': "<p><strong>위로한답시고</strong>: '위로하다' (tasalli bermoq) fe'liga qo'shilib, o'zicha tasalli bermoqchi bo'ldi-yu, lekin so'zi teskari ta'sir qilganidan norozilikni bildiradi.</p>",
        'correct': "위로한답시고",
        'choices': ["위로할 지라도", "위로한답시고", "위로하는 김에", "위로하려던 참이다"]
    },
    {
        'text': "<p>A: 컴퓨터가 <u>완전히</u> <strong>고장 났네요</strong>.<br>B: 동생이 <strong>고친</strong>________ <strong>만지다가</strong> <u>더</u> <strong>망가뜨렸어요</strong>.</p>",
        'explanation': "<p><strong>고친답시고</strong>: '고치다' (tuzatmoq) fe'liga qo'shilib, o'zicha tuzataman deb battar buzganini ko'rsatadi.</p>",
        'correct': "고친답시고",
        'choices': ["고친답시고", "고쳤더라면", "고치는 탓에", "고치려니 하고"]
    },
    {
        'text': "<p>A: <u>이</u> <u>음식은</u> <u>무슨</u> <u>맛이에요</u>?<br>B: 남편이 <u>요리</u> <strong>한</strong>________ <strong>만들었는데</strong> <u>맛이</u> <u>정말</u> <strong>이상해요</strong>.</p>",
        'explanation': "<p><strong>한답시고</strong>: '하다' (요리하다) fe'liga qo'shilib, o'zicha ovqat tayyorladim dedi-yu, lekin ta'mi yo'qligini bildiradi.</p>",
        'correct': "한답시고",
        'choices': ["하는 김에", "한답시고", "할 지경이라서", "하는 바람에"]
    },
    {
        'text': "<p>A: 옷이 <u>다</u> <strong>줄어들었네요</strong>.<br>B: <u>제가</u> <u>깨끗하게</u> <strong>빤</strong>________ <u>뜨거운</u> <u>물에</u> <strong>세탁해서</strong> <u>그렇게</u> <strong>됐어요</strong>.</p>",
        'explanation': "<p><strong>빤답시고</strong>: '빨다' (yuvmoq) fe'liga qo'shilib, o'zicha toza qilib yuvaman deb kiyimni kichraytirib qo'yganini ko'rsatadi.</p>",
        'correct': "빤답시고",
        'choices': ["빠는 통에", "빤답시고", "빨았더라면", "빠나 마나"]
    },
    {
        'text': "<p>A: <u>방이</u> <u>오히려</u> <u>더</u> <strong>어질러졌어요</strong>.<br>B: 아이가 <strong>청소한</strong>________ <u>물건들을</u> <u>다</u> <strong>꺼내</strong> <strong>놓았거든요</strong>.</p>",
        'explanation': "<p><strong>청소한답시고</strong>: '청소하다' (tozalamoq) fe'liga qo'shilib, o'zicha yig'ishtiraman deb uyni battar sochib yuborganini bildiradi.</p>",
        'correct': "청소한답시고",
        'choices': ["청소한답시고", "청소할 지라도", "청소하는 바람에", "청소하기 마련이라서"]
    },
    {
        'text': "<p>A: <u>그게</u> <u>선물이에요</u>?<br>B: 네, 친구가 <u>생일</u> <strong>선물이</strong>________ <strong>준</strong> <u>건데</u> <u>별로</u> <u>마음에</u> <strong>안</strong> <strong>들어요</strong>.</p>",
        'explanation': "<p><strong>선물이랍시고</strong>: '선물' (sovg'a) otiga qo'shilib, shuni ham o'zicha sovg'a deb berdi degan mensimaslik yoki norozilikni ko'rsatadi.</p>",
        'correct': "선물이랍시고",
        'choices': ["선물이려니 하고", "선물이랍시고", "선물일 지라도", "선물일 리가 없다"]
    },
    {
        'text': "<p>A: <u>머리가</u> <u>왜</u> <u>그래요</u>?<br>B: <u>제가</u> <u>직접</u> <strong>자른</strong>________ <strong>가위를</strong> <strong>댔다가</strong> <u>망쳤어요</u>.</p>",
        'explanation': "<p><strong>자른답시고</strong>: '자르다' (kesmoq) fe'liga qo'shilib, o'zicha sochimni qirqaman deb xunuk qilib qo'yganini bildiradi.</p>",
        'correct': "자른답시고",
        'choices': ["자른답시고", "자르는 김에", "자르다가는", "잘랐더라면"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>그렇게</u> <strong>바빠요</strong>?<br>B: <u>외국어를</u> <strong>공부한</strong>________ <u>학원에</u> <strong>등록했는데</strong> <u>갈</u> <u>시간이</u> <strong>없네요</strong>.</p>",
        'explanation': "<p><strong>공부한답시고</strong>: '공부하다' fe'liga qo'shilib, o'zicha til o'rganaman deb yozildi-yu, lekin amalda hech narsa qilolmayotganini ko'rsatadi.</p>",
        'correct': "공부한답시고",
        'choices': ["공부할 지라도", "공부하는 탓에", "공부한답시고", "공부할 겸"]
    },
    {
        'text': "<p>A: <u>강아지가</u> <u>왜</u> <strong>아파요</strong>?<br>B: <u>간식을</u> <strong>준</strong>________ <u>초콜릿을</u> <strong>먹여서</strong> <u>탈이</u> <strong>났어요</strong>.</p>",
        'explanation': "<p><strong>준답시고</strong>: '주다' fe'liga qo'shilib, o'zicha shirinlik beraman deb bolasi shokolad yedirib kasal qilib qo'yganini bildiradi.</p>",
        'correct': "준답시고",
        'choices': ["주려던 참이다", "준답시고", "주기 십상이라서", "주나 마나"]
    },
    {
        'text': "<p>A: <u>충고를</u> <strong>해</strong> <strong>주지</strong> <strong>그랬어요</strong>.<br>B: <u>좋은</u> <strong>충고랍</strong>________ <strong>말했다가</strong> <u>오히려</u> <strong>싸움만</strong> <strong>났어요</strong>.</p>",
        'explanation': "<p><strong>충고랍시고</strong>: '충고' (maslahat) otiga qo'shilib, o'zicha yaxshi maslahat deb aytdi-yu, lekin oqibati janjal bo'lganini ko'rsatadi.</p>",
        'correct': "충고랍시고",
        'choices': ["충고이려니 하고", "충고일 뿐만 아니라", "충고랍시고", "충고에 불과하다"]
    },
    {
        'text': "<p>A: <u>돈을</u> <u>많이</u> <strong>모았나요</strong>?<br>B: <u>아니요</u>, <strong>절약한</strong>________ <u>싼</u> <u>것만</u> <strong>샀는데</strong> <u>결국</u> <u>더</u> <u>자주</u> <strong>망가져서</strong> <u>돈이</u> <u>더</u> <strong>들었어요</strong>.</p>",
        'explanation': "<p><strong>절약한답시고</strong>: '절약하다' (tejamoq) fe'liga qo'shilib, o'zicha tejayman deb sifatsiz narsa olib ziyonga kirganini bildiradi.</p>",
        'correct': "절약한답시고",
        'choices': ["절약한답시고", "절약할 지라도", "절약하려던 참이라서", "절약할 리가 없어서"]
    },
    {
        'text': "<p>A: <u>그</u> <u>차는</u> <u>왜</u> <strong>샀어요</strong>?<br>B: <u>돈을</u> <strong>아낀</strong>________ <u>중고차를</u> <strong>샀는데</strong> <u>수리비가</u> <u>더</u> <strong>나오네요</strong>.</p>",
        'explanation': "<p><strong>아낀답시고</strong>: '아끼다' (tejamoq/asramoq) fe'liga qo'shilib, o'zicha pulni tejayman deb eski mashina olib pand yeganini ko'rsatadi.</p>",
        'correct': "아낀답시고",
        'choices': ["아끼는 탓에", "아낀답시고", "아낄 뿐만 아니라", "아끼기 마련이라서"]
    },
    {
        'text': "<p>A: 식물이 <u>왜</u> <u>다</u> <strong>말라</strong> <strong>죽었어요</strong>?<br>B: <u>영양제를</u> <strong>준</strong>________ <u>아무거나</u> <strong>뿌렸더니</strong> <u>죽어버렸어요</u>.</p>",
        'explanation': "<p><strong>준답시고</strong>: '주다' fe'liga qo'shilib, o'zicha dori beraman deb duch kelgan narsani sepib quritib qo'yganini bildiradi.</p>",
        'correct': "준답시고",
        'choices': ["주는 통에", "준답시고", "줄 지라도", "주려니 하고"]
    },
    {
        'text': "<p>A: <u>글씨가</u> <u>너무</u> <strong>작아서</strong> <strong>안</strong> <strong>보여요</strong>.<br>B: <u>디자인을</u> <strong>예쁘게</strong> <strong>한</strong>________ <u>글씨를</u> <u>너무</u> <u>작게</u> <strong>만들었나</strong> <strong>봐요</strong>.</p>",
        'explanation': "<p><strong>한답시고</strong>: '하다' fe'liga qo'shilib, o'zicha dizaynni chiroyli qilaman deb shriftni o'qib bo'lmas darajada maydalashtirib yuborganini ko'rsatadi.</p>",
        'correct': "한답시고",
        'choices': ["하는 바람에", "하는 김에", "한답시고", "할 지경이라서"]
    },
    {
        'text': "<p>A: <u>그</u> <u>사람과</u> <u>친해요</u>?<br>B: <u>아니요</u>, <strong>친구랍</strong>________ <u>필요할</u> <u>때만</u> <strong>연락하는</strong> <u>사람이라서</u> <strong>싫어요</strong>.</p>",
        'explanation': "<p><strong>친구랍시고</strong>: '친구' otiga qo'shilib, o'zicha do'stman deb faqat ishi tushganda yozishidan norozilikni bildiradi.</p>",
        'correct': "친구랍시고",
        'choices': ["친구일 뿐만 아니라", "친구이기 십상이라서", "친구일 지라도", "친구랍시고"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>이</u> <u>약을</u> <strong>먹고</strong> <u>더</u> <strong>아파요</strong>?<br>B: <u>민간요법으로</u> <strong>치료한</strong>________ <u>이상한</u> <u>걸</u> <strong>먹어서</strong> <u>그래요</u>.</p>",
        'explanation': "<p><strong>치료한답시고</strong>: '치료하다' (davolamoq) fe'liga qo'shilib, o'zicha uy sharoitida davolayman deb noto'g'ri narsa ichib kasallikni kuchaytirganini ko'rsatadi.</p>",
        'correct': "치료한답시고",
        'choices': ["치료한답시고", "치료하려던 참이라서", "치료할 리가 없어서", "치료하는 탓에"]
    },
    {
        'text': "<p>A: 그림을 <u>직접</u> <strong>그렸어요</strong>?<br>B: 네, <u>예술</u> <strong>작품이랍</strong>________ <strong>그려봤는데</strong> <u>낙서</u> <strong>같네요</strong>.</p>",
        'explanation': "<p><strong>작품이랍시고</strong>: '작품' (asar) otiga qo'shilib, o'zicha san'at asari deb chizgan narsasi shunchaki qoralama bo'lib chiqqanini bildiradi.</p>",
        'correct': "작품이랍시고",
        'choices': ["작품이려니 하고", "작품일 지라도", "작품이랍시고", "작품이기 마련이라서"]
    },
    {
        'text': "<p>A: <u>화장을</u> <u>왜</u> <u>그렇게</u> <strong>했어요</strong>?<br>B: <u>유행을</u> <strong>따라 한</strong>________ <strong>화장했는데</strong> <u>어릿광대</u> <strong>같아요</strong>.</p>",
        'explanation': "<p><strong>따라 한답시고</strong>: '따라 하다' (taqlid qilmoq) fe'liga qo'shilib, o'zicha modaga ergashaman deb kulgili ahvolga tushganini ko'rsatadi.</p>",
        'correct': "따라 한답시고",
        'choices': ["따라 하는 김에", "따라 할 지라도", "따라 한답시고", "따라 하는 바람에"]
    },
    {
        'text': "<p>A: <u>다이어트한다고</u> <strong>하지</strong> <strong>않았어요</strong>?<br>B: <strong>다이어트한</strong>________ <u>원푸드</u> <u>다이어트를</u> <strong>하다가</strong> <u>오히려</u> <u>건강만</u> <strong>나빠졌어요</strong>.</p>",
        'explanation': "<p><strong>다이어트한답시고</strong>: '다이어트하다' fe'liga qo'shilib, o'zicha parhez qilyapman deb faqat bir xil ovqat yeb sog'liqni buzganini bildiradi.</p>",
        'correct': "다이어트한답시고",
        'choices': ["다이어트할 지경이라서", "다이어트한답시고", "다이어트하는 탓에", "다이어트할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>운동을</u> <strong>시작하셨네요</strong>.<br>B: 네, <strong>운동한</strong>________ <u>비싼</u> <u>장비만</u> 잔뜩 <strong>사</strong> <strong>놓고</strong> <strong>안</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>운동한답시고</strong>: '운동하다' fe'liga qo'shilib, o'zicha sport bilan shug'ullanaman deb qimmat anjomlar olib tashlab qo'yganini ko'rsatadi.</p>",
        'correct': "운동한답시고",
        'choices': ["운동하는 김에", "운동할 겸", "운동한답시고", "운동하다가는"]
    },
    {
        'text': "<p>A: <u>고양이가</u> <u>왜</u> <u>저렇게</u> <strong>숨어</strong> <strong>있어요</strong>?<br>B: <u>제가</u> <strong>목욕시킨</strong>________ <u>물에</u> <strong>넣었더니</strong> <strong>놀라서</strong> <u>저래요</u>.</p>",
        'explanation': "<p><strong>목욕시킨답시고</strong>: '목욕시키다' (cho'miltirmoq) fe'liga qo'shilib, o'zicha cho'miltiraman deb kuchukni cho'chitib yuborganini bildiradi.</p>",
        'correct': "목욕시킨답시고",
        'choices': ["목욕시키는 바람에", "목욕시킨답시고", "목욕시킬 지라도", "목욕시키느라고"]
    },
    {
        'text': "<p>A: <u>그</u> <u>책은</u> <u>다</u> <strong>읽었어요</strong>?<br>B: <u>독서</u> <strong>한</strong>________ <u>어려운</u> <u>책을</u> <strong>샀다가</strong> <u>한 페이지도</u> <strong>못</strong> <strong>읽었어요</strong>.</p>",
        'explanation': "<p><strong>한답시고</strong>: '하다' (독서하다) fe'liga qo'shilib, o'zicha kitob o'qiyman deb qiyinini olib o'qimayotganini ko'rsatadi.</p>",
        'correct': "한답시고",
        'choices': ["하는 김에", "할 턱이 없어서", "한답시고", "할 지경이라서"]
    },
    {
        'text': "<p>A: <u>김치찌개가</u> <u>왜</u> <u>이렇게</u> <strong>달아요</strong>?<br>B: <u>맛을</u> <strong>낸</strong>________ <u>설탕을</u> <u>너무</u> 많이 <strong>넣었나</strong> <strong>봐요</strong>.</p>",
        'explanation': "<p><strong>낸답시고</strong>: '내다' (맛을 내다 - mazali qilmoq) fe'liga qo'shilib, o'zicha shirin qilaman deb shakar ko'payib ketganini bildiradi.</p>",
        'correct': "낸답시고",
        'choices': ["내는 통에", "낸답시고", "낼 리가 없어서", "내려던 참이라서"]
    },
    {
        'text': "<p>A: <u>사진이</u> <u>다</u> <strong>흔들렸네요</strong>.<br>B: <u>예술적으로</u> <strong>찍은</strong>________ <strong>움직이면서</strong> <strong>찍었더니</strong> <u>이렇네요</u>.</p>",
        'explanation': "<p><strong>찍은답시고</strong>: '찍다' fe'liga qo'shilib, o'zicha san'at asari qilaman deb qimirlab tushirib rasmni buzganini ko'rsatadi.</p>",
        'correct': "찍은답시고",
        'choices': ["찍을 뿐만 아니라", "찍은답시고", "찍기 무섭게", "찍다가는"]
    },
    {
        'text': "<p>A: <u>방음이</u> <u>전혀</u> <strong>안</strong> <strong>되네요</strong>.<br>B: <u>건축가가</u> <u>집을</u> <strong>지은</strong>________ <strong>지었는데</strong> <u>방음</u> <u>처리를</u> <u>엉망으로</u> <strong>했어요</strong>.</p>",
        'explanation': "<p><strong>지은답시고</strong>: '짓다' (qurmoq) fe'liga qo'shilib, o'zicha uy qurdim deb chala ish qilganidan norozilikni bildiradi.</p>",
        'correct': "지은답시고",
        'choices': ["지은답시고", "짓는 바람에", "지었더라면", "지을 지경이라서"]
    },
    {
        'text': "<p>A: <u>왜</u> <u>그렇게</u> <strong>한숨을</strong> <strong>쉬어요</strong>?<br>B: <u>주식으로</u> <u>돈을</u> <strong>번</strong>________ <u>전재산을</u> <strong>투자했다가</strong> <u>다</u> <strong>날렸거든요</strong>.</p>",
        'explanation': "<p><strong>번답시고</strong>: '벌다' (topmoq - pul) fe'liga qo'shilib, o'zicha pul topaman deb borini tikib yutqazganini ko'rsatadi.</p>",
        'correct': "번답시고",
        'choices': ["벌 지라도", "버는 탓에", "벌다가는", "번답시고"]
    },
    {
        'text': "<p>A: <u>외국어</u> <u>발음이</u> <u>많이</u> <strong>어색하네요</strong>.<br>B: <u>원어민처럼</u> <strong>발음한</strong>________ <u>혀를</u> <u>너무</u> <strong>굴렸나</strong> <strong>봐요</strong>.</p>",
        'explanation': "<p><strong>발음한답시고</strong>: '발음하다' fe'liga qo'shilib, o'zicha haqiqiy chet ellikdek gapiraman deb g'alati qilib qo'yganini bildiradi.</p>",
        'correct': "발음한답시고",
        'choices': ["발음하는 바람에", "발음한답시고", "발음할 뿐만 아니라", "발음할 지경이라서"]
    },
    {
        'text': "<p>A: <u>글이</u> <u>너무</u> <strong>어려워서</strong> <strong>이해하기</strong> <strong>힘들어요</strong>.<br>B: <u>유식하게</u> <strong>쓴</strong>________ <u>어려운</u> <u>한자어만</u> 잔뜩 <strong>넣어서</strong> <u>그래요</u>.</p>",
        'explanation': "<p><strong>쓴답시고</strong>: '쓰다' (yozmoq) fe'liga qo'shilib, o'zicha aqlli ko'rinaman deb murakkab so'zlar bilan matnni tushunarsiz qilganini ko'rsatadi.</p>",
        'correct': "쓴답시고",
        'choices': ["쓰는 김에", "쓴답시고", "쓸 리가 없어서", "쓰는 탓에"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>이벤트는</u> <u>참가자가</u> <strong>없네요</strong>.<br>B: <u>사은품이랍</u>________ <u>싸구려</u> <u>볼펜을</u> <strong>주니까</strong> <u>아무도</u> <strong>안</strong> <strong>오죠</strong>.</p>",
        'explanation': "<p><strong>사은품이랍시고</strong>: '사은품' (sovg'a/bonus) otiga qo'shilib, o'zicha buni ham sovg'a deb arzonga uchib odamlarni qochirganini bildiradi.</p>",
        'correct': "사은품이랍시고",
        'choices': ["사은품이려니 하고", "사은품이랍시고", "사은품일 지라도", "사은품이려던 참이라서"]
    },
    {
        'text': "<p>A: <u>머리가</u> <u>왜</u> <u>그렇게</u> <strong>복잡해요</strong>?<br>B: <u>미래를</u> <strong>계획한</strong>________ <u>이것저것</u> <strong>생각하다가</strong> <u>오히려</u> <u>머리만</u> <strong>아프네요</strong>.</p>",
        'explanation': "<p><strong>계획한답시고</strong>: '계획하다' fe'liga qo'shilib, o'zicha kelajakni rejalashtiraman deb boshini og'ritganini ko'rsatadi.</p>",
        'correct': "계획한답시고",
        'choices': ["계획하는 통에", "계획할 리가 없어서", "계획한답시고", "계획하느라고"]
    }
]

# =====================================================================
# Topic 84: 근거와 이유의 격식체: 명사 + (으)로 말미암아 / (으)로 인해 (Rasmiy sabab: ...tufayli / ...sababli)
# =====================================================================
topic_84 = [
    {
        'text': "<p>A: <u>이번</u> <u>사고의</u> <u>원인이</u> <strong>무엇입니까</strong>?<br>B: <u>운전자의</u> <strong>부주의함</strong>________ <u>큰</u> <u>사고가</u> <strong>발생했습니다</strong>.</p>",
        'explanation': "<p><strong>부주의함으로 인해</strong>: '부주의하다' (e'tiborsiz bo'lmoq) sifatining otlashgan shakliga qo'shilib, haydovchining e'tiborsizligi tufayli avariya bo'lganini rasmiy tilda ko'rsatadi.</p>",
        'correct': "부주의함으로 인해",
        'choices': ["부주의할 지라도", "부주의함으로 인해", "부주의하기 십상이라서", "부주의할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>기차가</u> <u>왜</u> <strong>연착되었나요</strong>?<br>B: <u>간밤에</u> <strong>내린</strong> <u>폭우로</u> ________ <u>열차</u> <u>운행이</u> <strong>지연되었습니다</strong>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '폭우' (kuchli yomg'ir) otiga qo'shilib, yog'ingarchilik oqibatida poyezd kechikkanini bildiradi.</p>",
        'correct': "말미암아",
        'choices': ["말미암아", "인하는 바람에", "인할 지라도", "불과하여"]
    },
    {
        'text': "<p>A: <u>그</u> <u>지역의</u> <u>경제가</u> <strong>어려워진</strong> <u>이유가</u> <strong>뭡니까</strong>?<br>B: <u>관광객이</u> <strong>급감함</strong>________ <u>지역</u> <u>경제가</u> <u>큰</u> <u>타격을</u> <strong>입었습니다</strong>.</p>",
        'explanation': "<p><strong>급감함으로 인해</strong>: '급감하다' (keskin kamaymoq) fe'lining otlashgan shakliga qo'shilib, turistlar kamayishi sababli iqtisodiyot zarar ko'rganini ko'rsatadi.</p>",
        'correct': "급감함으로 인해",
        'choices': ["급감할 지라도", "급감함으로 인해", "급감하는 통에", "급감할 리가 없어서"]
    },
    {
        'text': "<p>A: <u>두</u> <u>나라의</u> <u>관계가</u> <strong>악화되었군요</strong>.<br>B: <u>사소한</u> <u>오해로</u> ________ <u>국가</u> <u>간의</u> <u>분쟁이</u> <strong>시작되었습니다</strong>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '오해' (tushunmovchilik) otiga qo'shilib, kichik xato tufayli ziddiyat boshlanganini rasmiy tilda bildiradi.</p>",
        'correct': "말미암아",
        'choices': ["말미암아", "불과하여", "따름이어", "인할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>현대인들이</u> <u>자주</u> <strong>겪는</strong> <u>질병의</u> <u>원인은</u> <strong>무엇일까요</strong>?<br>B: <u>과도한</u> <strong>스트레스로</strong> ________ <u>면역력이</u> <strong>저하되는</strong> <u>것이</u> <u>문제입니다</u>.</p>",
        'explanation': "<p><strong>인해</strong>: '스트레스' (stress) otiga qo'shilib, asabiylashish oqibatida immunitet tushishini ko'rsatadi.</p>",
        'correct': "인해",
        'choices': ["인할 지경이라", "말미암은 바람에", "인해", "불과해"]
    },
    {
        'text': "<p>A: <u>이</u> <u>건물이</u> <strong>무너진</strong> <u>이유가</u> <strong>밝혀졌나요</strong>?<br>B: <u>부실 공사로</u> ________ <u>붕괴된</u> <u>것으로</u> <strong>확인되었습니다</strong>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '부실 공사' (sifatsiz qurilish) otiga qo'shilib, binoning qulashiga sifatsiz ish sabab bo'lganini bildiradi.</p>",
        'correct': "말미암아",
        'choices': ["따름이어", "말미암아", "인하는 탓에", "불과해"]
    },
    {
        'text': "<p>A: <u>지구</u> <u>온난화가</u> <strong>심각하네요</strong>.<br>B: <u>환경이</u> <strong>오염됨</strong>________ <u>기후</u> <u>변화가</u> <strong>가속화되고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>오염됨으로 인해</strong>: '오염되다' (ifloslanmoq) fe'lining otlashgan shakliga qo'shilib, ekologiya buzilishi sababli iqlim isishini ko'rsatadi.</p>",
        'correct': "오염됨으로 인해",
        'choices': ["오염될 리가 없어서", "오염됨으로 인해", "오염되는 김에", "오염될 지라도"]
    },
    {
        'text': "<p>A: <u>최근</u> <u>물가가</u> <u>급격히</u> <strong>상승한</strong> <u>원인은요</u>?<br>B: <u>국제</u> <u>유가가</u> <strong>폭등함</strong>________ <u>물가</u> <u>상승이</u> <strong>초래되었습니다</strong>.</p>",
        'explanation': "<p><strong>폭등함으로 말미암아</strong> (yoki 인해): '폭등하다' (keskin ko'tarilmoq) ga qo'shilib, neft narxi oshgani tufayli inflyatsiya bo'lganini bildiradi.</p>",
        'correct': "폭등함으로 말미암아",
        'choices': ["폭등함으로 말미암아", "폭등할 뿐만 아니라", "폭등하기 마련이라서", "폭등할 지경이라서"]
    },
    {
        'text': "<p>A: <u>그</u> <u>행사가</u> <strong>취소된</strong> <u>이유를</u> <strong>아십니까</strong>?<br>B: <u>예산이</u> <strong>부족함</strong>________ <u>행사를</u> <strong>취소할</strong> <u>수밖에</u> <strong>없었습니다</strong>.</p>",
        'explanation': "<p><strong>부족함으로 인해</strong>: '부족하다' sifatining otlashgan shakliga qo'shilib, mablag' yetishmasligi oqibatida bekor qilinganini ko'rsatadi.</p>",
        'correct': "부족함으로 인해",
        'choices': ["부족할 지라도", "부족하기 무섭게", "부족함으로 인해", "부족하려던 참이라서"]
    },
    {
        'text': "<p>A: <u>요즘</u> <u>인구가</u> <u>많이</u> <strong>감소하고</strong> <strong>있어요</strong>.<br>B: <u>출산율이</u> <strong>저하됨</strong>________ <u>인구</u> <u>감소</u> <u>문제가</u> <strong>심각해졌습니다</strong>.</p>",
        'explanation': "<p><strong>저하됨으로 말미암아</strong>: '저하되다' (pasaymoq) fe'liga qo'shilib, tug'ilish pasayishi tufayli aholi kamayishini bildiradi.</p>",
        'correct': "저하됨으로 말미암아",
        'choices': ["저하됨으로 말미암아", "저하될 지라도", "저하될 뿐만 아니라", "저하되기 십상이라서"]
    },
    {
        'text': "<p>A: <u>비행기</u> <u>결항</u> <u>이유를</u> <strong>안내해</strong> <strong>주시겠어요</strong>?<br>B: <u>짙은</u> <strong>안개로</strong> ________ <u>안전상의</u> <u>이유로</u> <strong>결항되었습니다</strong>.</p>",
        'explanation': "<p><strong>인해</strong>: '안개' (tuman) otiga qo'shilib, tuman sababli qatnov to'xtatilganini rasmiy tilda ko'rsatadi.</p>",
        'correct': "인해",
        'choices': ["인할 지라도", "인해", "인하기 마련이라서", "불과해"]
    },
    {
        'text': "<p>A: <u>그</u> <u>회사가</u> <strong>파산한</strong> <u>결정적인</u> <u>이유는요</u>?<br>B: <u>경영진의</u> <u>잘못된</u> <strong>판단으로</strong> ________ <u>회사가</u> <u>위기에</u> <strong>처했습니다</strong>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '판단' (qaror/xulosa) otiga qo'shilib, xato xulosa oqibatida bankrot bo'lganini bildiradi.</p>",
        'correct': "말미암아",
        'choices': ["말미암아", "말미암을 지라도", "인할 뿐만 아니라", "따름이어"]
    },
    {
        'text': "<p>A: <u>요즘</u> <u>온라인</u> <u>사기가</u> <strong>늘고</strong> <strong>있습니다</strong>.<br>B: <u>개인정보가</u> <strong>유출됨</strong>________ <u>2차</u> <u>피해가</u> <strong>발생하고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>유출됨으로 인해</strong>: '유출되다' (tarqalib ketmoq - ma'lumot) fe'lining otlashgan shakliga qo'shilib, ma'lumotlar o'g'irlanishi tufayli zarar ko'payishini ko'rsatadi.</p>",
        'correct': "유출됨으로 인해",
        'choices': ["유출될 리가 없어서", "유출됨으로 인해", "유출되는 바람에", "유출될 지경이라서"]
    },
    {
        'text': "<p>A: <u>교통사고가</u> <u>왜</u> <strong>발생했습니까</strong>?<br>B: <u>눈길에</u> <u>차량이</u> <strong>미끄러짐</strong>________ <u>사고가</u> <strong>일어났습니다</strong>.</p>",
        'explanation': "<p><strong>미끄러짐으로 말미암아</strong>: '미끄러지다' (sirpanmoq) fe'liga qo'shilib, qorda mashina sirpanishi sababli to'qnashuv bo'lganini bildiradi.</p>",
        'correct': "미끄러짐으로 말미암아",
        'choices': ["미끄러질 지라도", "미끄러지는 탓에", "미끄러짐으로 말미암아", "미끄러지기 십상이라서"]
    },
    {
        'text': "<p>A: <u>그</u> <u>제도가</u> <strong>폐지된</strong> <u>까닭이</u> <strong>무엇입니까</strong>?<br>B: <u>실효성이</u> <strong>부족함</strong>________ <u>결국</u> <strong>폐지되었습니다</strong>.</p>",
        'explanation': "<p><strong>부족함으로 인해</strong>: '부족하다' sifatiga qo'shilib, samaradorlik yo'qligi tufayli qoida bekor qilinganini ko'rsatadi.</p>",
        'correct': "부족함으로 인해",
        'choices': ["부족할 리가 없어서", "부족함으로 인해", "부족할 뿐만 아니라", "부족하느라고"]
    },
    {
        'text': "<p>A: <u>수출이</u> <u>크게</u> <strong>감소했네요</strong>.<br>B: <u>환율이</u> <strong>변동함</strong>________ <u>수출</u> <u>기업들이</u> <u>큰</u> <u>어려움을</u> <strong>겪고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>변동함으로 인해</strong>: '변동하다' (o'zgarmoq) fe'liga qo'shilib, valyuta kursining o'zgarishi oqibatida qiyinchilik bo'layotganini bildiradi.</p>",
        'correct': "변동함으로 인해",
        'choices': ["변동함으로 인해", "변동할 지라도", "변동할 뿐만 아니라", "변동하기 마련이라서"]
    },
    {
        'text': "<p>A: <u>야생동물이</u> <u>자꾸</u> <u>마을로</u> <strong>내려오네요</strong>.<br>B: <u>무분별한</u> <u>개발로</u> ________ <u>서식지가</u> <strong>파괴되었기</strong> <u>때문입니다</u>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '개발' (qurilish/rivojlanish) otiga qo'shilib, tabiatni buzish oqibatida hayvonlar yashash joysiz qolganini ko'rsatadi.</p>",
        'correct': "말미암아",
        'choices': ["말미암을 지라도", "말미암아", "인할 리가 없어서", "따름이어"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>감염병이</u> <u>빠르게</u> <strong>확산된</strong> <u>원인은요</u>?<br>B: <u>초기</u> <u>대응이</u> <strong>미흡했음</strong>________ <u>사태가</u> <strong>커졌습니다</strong>.</p>",
        'explanation': "<p><strong>미흡했음으로 인해</strong>: '미흡하다' (yetarli bo'lmaslik) sifatining o'tgan zamon otlashgan shakliga qo'shilib, boshlang'ich choralar kamligi tufayli kasallik tarqalganini bildiradi.</p>",
        'correct': "미흡했음으로 인해",
        'choices': ["미흡했으려니 하고", "미흡했음으로 인해", "미흡했을 지라도", "미흡했을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>그</u> <u>작품이</u> <u>전 세계적으로</u> <strong>유명해진</strong> <u>계기가</u> <strong>있나요</strong>?<br>B: <u>인터넷을</u> <strong>통해</strong> <u>입소문이</u> <strong>퍼짐</strong>________ <u>큰</u> <u>인기를</u> <strong>얻었습니다</strong>.</p>",
        'explanation': "<p><strong>퍼짐으로 말미암아</strong>: '퍼지다' (tarqalmoq) fe'liga qo'shilib, internetda ovoza bo'lishi sababli mashhur bo'lganini ko'rsatadi (ijobiy ma'noda ham ishlatiladi).</p>",
        'correct': "퍼짐으로 말미암아",
        'choices': ["퍼질 뿐만 아니라", "퍼지려던 참이라서", "퍼짐으로 말미암아", "퍼지는 통에"]
    },
    {
        'text': "<p>A: <u>농작물</u> <u>피해가</u> <u>막심하군요</u>.<br>B: <u>오랜</u> <strong>가뭄으로</strong> ________ <u>농부들의</u> <u>시름이</u> <strong>깊어지고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>인해</strong>: '가뭄' (qurg'oqchilik) otiga qo'shilib, suvsizlik oqibatida zarar ko'rilayotganini bildiradi.</p>",
        'correct': "인해",
        'choices': ["인해", "인할 지라도", "말미암을 턱이 없어", "불과해"]
    },
    {
        'text': "<p>A: <u>건강이</u> <u>많이</u> <strong>나빠지셨어요</strong>.<br>B: <u>수면이</u> <strong>부족함</strong>________ <u>만성</u> <u>피로에</u> <strong>시달리고</strong> <strong>계십니다</strong>.</p>",
        'explanation': "<p><strong>부족함으로 인해</strong>: '부족하다' sifatiga qo'shilib, uyqusizlik sababli charchoq paydo bo'lganini ko'rsatadi.</p>",
        'correct': "부족함으로 인해",
        'choices': ["부족할 지라도", "부족하기 마련이라서", "부족함으로 인해", "부족한 바람에"]
    },
    {
        'text': "<p>A: <u>그</u> <u>법안이</u> <strong>보류된</strong> <u>이유가</u> <strong>무엇입니까</strong>?<br>B: <u>시민들의</u> <u>강한</u> <strong>반대로</strong> ________ <u>시행이</u> <strong>연기되었습니다</strong>.</p>",
        'explanation': "<p><strong>말미암아</strong>: '반대' (qarshilik) otiga qo'shilib, xalqning noroziligi tufayli qonun to'xtatib turilganini bildiradi.</p>",
        'correct': "말미암아",
        'choices': ["따름이어", "말미암아", "인할 지경이라", "불과해"]
    },
    {
        'text': "<p>A: <u>건물이</u> <u>화재에</u> <u>취약했던</u> <u>원인은요</u>?<br>B: <u>가연성</u> <u>자재를</u> <strong>사용함</strong>________ <u>불이</u> <u>빠르게</u> <strong>번졌습니다</strong>.</p>",
        'explanation': "<p><strong>사용함으로 인해</strong>: '사용하다' (ishlatmoq) fe'liga qo'shilib, tez yonuvchi materiallar ishlatilgani oqibatida yong'in tarqalganini ko'rsatadi.</p>",
        'correct': "사용함으로 인해",
        'choices': ["사용함으로 인해", "사용할 지라도", "사용할 뿐만 아니라", "사용하기 십상이라서"]
    },
    {
        'text': "<p>A: <u>이</u> <u>지역의</u> <u>집값이</u> <u>왜</u> <strong>올랐나요</strong>?<br>B: <u>새로운</u> <u>지하철역이</u> <strong>개통됨</strong>________ <u>주변</u> <u>아파트</u> <u>값이</u> <strong>상승했습니다</strong>.</p>",
        'explanation': "<p><strong>개통됨으로 말미암아</strong>: '개통되다' (ochilmoq/ishga tushmoq) fe'liga qo'shilib, metro qurilishi sababli narxlar ko'tarilganini bildiradi.</p>",
        'correct': "개통됨으로 말미암아",
        'choices': ["개통될 지라도", "개통됨으로 말미암아", "개통되기 마련이라서", "개통되는 탓에"]
    },
    {
        'text': "<p>A: <u>비만</u> <u>인구가</u> <strong>증가하는</strong> <u>이유가</u> <strong>무엇일까요</strong>?<br>B: <u>서구화된</u> <u>식습관으로</u> ________ <u>비만율이</u> <strong>높아지고</strong> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>인해</strong>: '식습관' (ovqatlanish odati) otiga qo'shilib, yevropacha taomlanish oqibatida semizlik ortayotganini ko'rsatadi.</p>",
        'correct': "인해",
        'choices': ["인할 뿐만 아니라", "인해", "말미암아 보았자", "따름이어"]
    },
    {
        'text': "<p>A: <u>그</u> <u>회사의</u> <u>신제품이</u> <strong>실패한</strong> <u>까닭은요</u>?<br>B: <u>소비자의</u> <u>기호를</u> <u>제대로</u> <strong>파악하지</strong> <strong>못함</strong>________ <u>판매가</u> <strong>부진했습니다</strong>.</p>",
        'explanation': "<p><strong>못함으로 인해</strong>: '못하다' inkor fe'lining otlashgan shakliga qo'shilib, xaridor ehtiyojini tushunmaganligi tufayli savdo tushib ketganini bildiradi.</p>",
        'correct': "못함으로 인해",
        'choices': ["못할 지라도", "못함으로 인해", "못하는 바람에", "못하기 십상이라서"]
    },
    {
        'text': "<p>A: <u>대기오염이</u> <strong>심해진</strong> <u>원인이</u> <strong>있나요</strong>?<br>B: <u>자동차</u> <u>배기가스가</u> <strong>증가함</strong>________ <u>공기가</u> <u>많이</u> <strong>탁해졌습니다</strong>.</p>",
        'explanation': "<p><strong>증가함으로 말미암아</strong>: '증가하다' (ko'paymoq) fe'liga qo'shilib, mashina tutunlari ko'payishi oqibatida havo buzilganini ko'rsatadi.</p>",
        'correct': "증가함으로 말미암아",
        'choices': ["증가하는 탓에", "증가할 지라도", "증가함으로 말미암아", "증가할 리가 없어서"]
    },
    {
        'text': "<p>A: <u>이</u> <u>도로가</u> <u>자주</u> <strong>막히는</strong> <u>이유는요</u>?<br>B: <u>불법</u> <strong>주차로</strong> ________ <u>차량</u> <u>통행이</u> <strong>원활하지</strong> <strong>않습니다</strong>.</p>",
        'explanation': "<p><strong>인해</strong>: '주차' (parkovka) otiga qo'shilib, noqonuniy mashina qo'yish tufayli yo'l tirband bo'lishini bildiradi.</p>",
        'correct': "인해",
        'choices': ["말미암기 무섭게", "인해", "인할 지라도", "불과해"]
    },
    {
        'text': "<p>A: <u>수면</u> <u>부족이</u> <u>건강에</u> <strong>미치는</strong> <u>영향은요</u>?<br>B: <u>충분히</u> <strong>자지</strong> <strong>못함</strong>________ <u>집중력이</u> <strong>떨어질</strong> <u>수</u> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>못함으로 인해</strong>: '못하다' ga qo'shilib, uxlamaslik oqibatida diqqat pasayishini rasmiy tilda ko'rsatadi.</p>",
        'correct': "못함으로 인해",
        'choices': ["못함으로 인해", "못할 리가 없어서", "못할 뿐만 아니라", "못하기 십상이라서"]
    },
    {
        'text': "<p>A: <u>국가</u> <u>경쟁력이</u> <strong>강화된</strong> <u>배경이</u> <strong>궁금합니다</strong>.<br>B: <u>첨단</u> <u>기술을</u> <u>성공적으로</u> <strong>개발함</strong>________ <u>국제적인</u> <u>위상이</u> <strong>높아졌습니다</strong>.</p>",
        'explanation': "<p><strong>개발함으로 말미암아</strong>: '개발하다' (yaratmoq/rivojlantirmoq) fe'liga qo'shilib, texnologiya ishlab chiqilgani sababli obro' oshganini bildiradi (ijobiy holatda ham qo'llaniladi).</p>",
        'correct': "개발함으로 말미암아",
        'choices': ["개발할 지라도", "개발함으로 말미암아", "개발할 뿐만 아니라", "개발하기 마련이라서"]
    }
]
# =====================================================================
# Topic 85: 당연한 사실의 반문: 동사/형용사 + 거늘 (Tabiiy holatni inkor qilib so'rash/ta'kidlash: ... bo'lib turganda / ...-ku)
# =====================================================================
topic_85 = [
    {
        'text': "<p>A: <u>그</u> 사람이 배신을 <strong>할</strong> <u>줄은</u> <strong>몰랐어요</strong>.<br>B: 짐승도 은혜를 <strong>알</strong>________ <u>하물며</u> 사람이 은혜를 <strong>모르겠습니까</strong>?</p>",
        'explanation': "<p><strong>알거늘</strong>: '알다' (bilmoq) fe'liga qo'shilib, hayvon ham yaxshilikni bilganida, odam bilmasligi mumkinmi degan kuchli ta'kidni bildiradi.</p>",
        'correct': "알거늘",
        'choices': ["알다가는", "알거늘", "알기 마련이다", "알았더라면"]
    },
    {
        'text': "<p>A: <u>아무리</u> <strong>배워도</strong> <u>자꾸</u> <strong>틀려요</strong>.<br>B: <u>오랜</u> 경험을 <strong>가진</strong> 전문가도 <u>가끔</u> <strong>실수하</strong>________ <u>초보자가</u> <strong>틀리는</strong> 것은 <u>당연합니다</u>.</p>",
        'explanation': "<p><strong>실수하거늘</strong>: '실수하다' (xato qilmoq) fe'liga qo'shilib, mutaxassis ham xato qilib turganda, yangi o'rganuvchining xato qilishi tabiiy ekanini ko'rsatadi.</p>",
        'correct': "실수하거늘",
        'choices': ["실수하기 십상이다", "실수하려던 참이다", "실수하거늘", "실수할 지라도"]
    },
    {
        'text': "<p>A: <u>저</u> 사람은 부자인데도 <u>돈을</u> <u>절대</u> <strong>안</strong> <strong>써요</strong>.<br>B: <u>많이</u> <strong>가진</strong> 사람도 <u>저렇게</u> <strong>아끼</strong>________ <u>우리는</u> <u>더</u> <strong>아껴야죠</strong>.</p>",
        'explanation': "<p><strong>아끼거늘</strong>: '아끼다' (tejamoq) fe'liga qo'shilib, boy odam ham tejab turganda, biz battar tejashimiz kerakligini bildiradi.</p>",
        'correct': "아끼거늘",
        'choices': ["아끼거늘", "아끼는 탓에", "아낄 뿐만 아니라", "아낄 리가 없다"]
    },
    {
        'text': "<p>A: <u>오늘</u> 날씨가 <u>정말</u> <strong>춥네요</strong>.<br>B: <u>따뜻한</u> 남쪽 지방도 <u>이렇게</u> <strong>춥</strong>________ <u>여기는</u> <strong>오죽하겠습니까</strong>?</p>",
        'explanation': "<p><strong>춥거늘</strong>: '춥다' (sovuq bo'lmoq) sifatiga qo'shilib, issiq joylar ham sovuq bo'lganda, bu yerning sovuq bo'lishi aniq ekanini ko'rsatadi.</p>",
        'correct': "춥거늘",
        'choices': ["추울 지경이다", "추운 바람에", "춥기 무섭게", "춥거늘"]
    },
    {
        'text': "<p>A: 건강을 <u>갑자기</u> <strong>잃으셨대요</strong>.<br>B: <u>평소에</u> 건강했던 사람도 <u>한순간에</u> <strong>쓰러지</strong>________ <u>늘</u> <strong>조심해야</strong> <strong>해요</strong>.</p>",
        'explanation': "<p><strong>쓰러지거늘</strong>: '쓰러지다' (yiqilmoq/kasal bo'lmoq) fe'liga qo'shilib, sog'lom odam ham yiqilib turganda, ehtiyot bo'lish kerakligini bildiradi.</p>",
        'correct': "쓰러지거늘",
        'choices': ["쓰러질 리가 없다", "쓰러지거늘", "쓰러지려니 하고", "쓰러지는 통에"]
    },
    {
        'text': "<p>A: 가족끼리 <u>왜</u> <strong>싸우는지</strong> <strong>모르겠어요</strong>.<br>B: <u>한날한시에</u> <strong>태어난</strong> 쌍둥이도 <strong>다투</strong>________ <u>하물며</u> <u>다른</u> 사람들이야 <strong>안</strong> <strong>다투겠어요</strong>?</p>",
        'explanation': "<p><strong>다투거늘</strong>: '다투다' (janjallashmoq) fe'liga qo'shilib, egizaklar ham urishib turganda, boshqalar urishishi tabiiy ekanini ko'rsatadi.</p>",
        'correct': "다투거늘",
        'choices': ["다투거늘", "다투다가는", "다투는 김에", "다툴 뿐이다"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <strong>사랑했는데</strong> <u>결국</u> <strong>헤어졌네요</strong>.<br>B: <u>아름다운</u> 꽃도 <u>시간이</u> <strong>지나면</strong> <strong>시들</strong>________ 하물며 사람의 마음이 <strong>안</strong> <strong>변하겠어요</strong>?</p>",
        'explanation': "<p><strong>시들거늘</strong>: '시들다' (so'limoq) fe'liga qo'shilib, gul ham so'lib qolganda, inson ko'ngli o'zgarishi tabiiyligini bildiradi.</p>",
        'correct': "시들거늘",
        'choices': ["시든 탓에", "시들기 십상이다", "시들거늘", "시들어 봤자"]
    },
    {
        'text': "<p>A: <u>그</u> 천재도 <u>이번</u> 연구에서 <strong>실패했다면서요</strong>?<br>B: 뛰어난 천재도 <strong>실패하</strong>________ <u>보통</u> <u>사람은</u> <u>말할</u> <u>것도</u> <strong>없지요</strong>.</p>",
        'explanation': "<p><strong>실패하거늘</strong>: '실패하다' (yutqazmoq/muvaffaqiyatsizlikka uchramoq) fe'liga qo'shilib, daho ham xato qilib turganda, oddiy odamning xatosi hech narsa emasligini ko'rsatadi.</p>",
        'correct': "실패하거늘",
        'choices': ["실패했더라면", "실패하거늘", "실패하는 바람에", "실패할 지라도"]
    },
    {
        'text': "<p>A: <u>저희</u> 팀의 <u>단합이</u> <u>점점</u> <strong>안</strong> <strong>돼요</strong>.<br>B: <u>흐르지</u> <strong>않는</strong> 물도 <strong>고이면</strong> <strong>썩</strong>________ <u>사람의</u> <u>관계도</u> <u>마찬가지입니다</u>.</p>",
        'explanation': "<p><strong>썩거늘</strong>: '썩다' (aynimoq/sasimoq) fe'liga qo'shilib, suv ham oqmasa sasiganda, inson munosabatlari ham shunday bo'lishini bildiradi.</p>",
        'correct': "썩거늘",
        'choices': ["썩으려던 참이다", "썩을 지라도", "썩거늘", "썩기 마련이다"]
    },
    {
        'text': "<p>A: 산 정상에 <strong>오르기가</strong> <u>너무</u> <strong>힘드네요</strong>.<br>B: <u>낮은</u> 언덕도 <strong>오르면</strong> <strong>숨이</strong> <strong>차</strong>________ <u>높은</u> <u>산은</u> <strong>오죽하겠습니까</strong>?</p>",
        'explanation': "<p><strong>차거늘</strong>: '차다' (숨이 차다 - hansiramoq) fe'liga qo'shilib, past tepalik ham charchatganda, baland tog' battar charchatishini ko'rsatadi.</p>",
        'correct': "차거늘",
        'choices': ["차는 길에", "차거늘", "차기 십상이다", "차다가는"]
    },
    {
        'text': "<p>A: <u>아무리</u> 권력이 <strong>있어도</strong> <strong>죽음은</strong> <strong>피할</strong> <u>수</u> <strong>없네요</strong>.<br>B: <u>절대</u> 권력을 <strong>가진</strong> 왕도 <strong>죽음을</strong> <strong>맞이하</strong>________ <u>우리</u> 같은 평범한 <u>사람이야</u> <strong>어떻겠습니까</strong>?</p>",
        'explanation': "<p><strong>맞이하거늘</strong>: '맞이하다' (kutib olmoq - o'limni) fe'liga qo'shilib, shohlar ham o'lganda, biz oddiy insonlar ham o'lishimiz haqiqat ekanini bildiradi.</p>",
        'correct': "맞이하거늘",
        'choices': ["맞이하거늘", "맞이할 뿐만 아니라", "맞이하는 김에", "맞이할 턱이 없다"]
    },
    {
        'text': "<p>A: <u>새로</u> <strong>산</strong> 기계가 <u>벌써</u> <strong>고장</strong> <strong>났어요</strong>.<br>B: <u>아무리</u> <strong>단단한</strong> 무쇠도 <u>세월이</u> <strong>가면</strong> <strong>녹슬</strong>________ 기계가 <strong>망가지는</strong> <u>것은</u> <u>당연하지요</u>.</p>",
        'explanation': "<p><strong>녹슬거늘</strong>: '녹슬다' (zanglamoq) fe'liga qo'shilib, temir ham zanglaganda, texnika buzilishi tabiiy ekanini ko'rsatadi.</p>",
        'correct': "녹슬거늘",
        'choices': ["녹슬었더라면", "녹슬기 십상이다", "녹슬거늘", "녹스는 탓에"]
    },
    {
        'text': "<p>A: <u>요즘</u> 상사들이 <u>너무</u> <strong>권위적이에요</strong>.<br>B: <u>옛날</u> <u>성인들도</u> <u>아랫사람에게</u> <strong>고개를</strong> <strong>숙이</strong>________ <u>지금</u> 사람들이야 <u>더</u> <strong>겸손해야죠</strong>.</p>",
        'explanation': "<p><strong>숙이거늘</strong>: '숙이다' (egmoq) fe'liga qo'shilib, buyuklar ham bosh egib turganda, biz battar kamtar bo'lishimiz kerakligini bildiradi.</p>",
        'correct': "숙이거늘",
        'choices': ["숙일 리가 없다", "숙이는 바람에", "숙이려니 하고", "숙이거늘"]
    },
    {
        'text': "<p>A: <u>작은</u> <u>동물이라고</u> <strong>함부로</strong> <strong>대하면</strong> <strong>안</strong> <strong>돼요</strong>.<br>B: <u>미물인</u> 벌레도 <strong>건드리면</strong> <strong>아픔을</strong> <strong>느끼</strong>________ <u>어찌</u> <u>함부로</u> <strong>대하겠어요</strong>?</p>",
        'explanation': "<p><strong>느끼거늘</strong>: '느끼다' (his qilmoq) fe'liga qo'shilib, kichik hasharot ham og'riq sezganda, uni xafa qilish mumkin emasligini ko'rsatadi.</p>",
        'correct': "느끼거늘",
        'choices': ["느끼거늘", "느끼다가는", "느껴 봤자", "느낄 지라도"]
    },
    {
        'text': "<p>A: <u>그</u> <u>사람이</u> 저를 <strong>도와줄까요</strong>?<br>B: <u>피가</u> <strong>섞이지</strong> <strong>않은</strong> 남들도 <strong>어려울</strong> <u>때는</u> <strong>돕</strong>________ 친구인 <u>그가</u> <strong>안</strong> <strong>돕겠어요</strong>?</p>",
        'explanation': "<p><strong>돕거늘</strong>: '돕다' (yordam bermoq) fe'liga qo'shilib, begona odamlar ham yordam berganda, do'sti yordam bermasligi mumkin emasligini bildiradi.</p>",
        'correct': "돕거늘",
        'choices': ["돕는 김에", "도울 리가 없다", "돕거늘", "돕기 무섭게"]
    },
    {
        'text': "<p>A: <u>언제쯤</u> <u>이</u> <u>고통이</u> <strong>끝날까요</strong>?<br>B: <u>가장</u> <strong>어두운</strong> 밤도 <u>시간이</u> <strong>지나면</strong> <strong>밝아지</strong>________ <u>당신의</u> <u>어려움도</u> <u>곧</u> <strong>지나갈</strong> 거예요.</p>",
        'explanation': "<p><strong>밝아지거늘</strong>: '밝아지다' (yorishmoq) fe'liga qo'shilib, tun ham yorishganda, qiyinchiliklar ham o'tib ketishini ko'rsatadi.</p>",
        'correct': "밝아지거늘",
        'choices': ["밝아질 지경이다", "밝아지거늘", "밝아지는 바람에", "밝아졌더라면"]
    },
    {
        'text': "<p>A: <u>이</u> <u>평화가</u> <u>계속될까요</u>?<br>B: <u>아무리</u> <strong>평화로운</strong> 때라도 전쟁에 <strong>대비하</strong>________ <u>항상</u> <u>긴장을</u> <strong>늦추면</strong> <strong>안</strong> <strong>돼요</strong>.</p>",
        'explanation': "<p><strong>대비하거늘</strong>: '대비하다' (tayyorgarlik ko'rmoq) fe'liga qo'shilib, tinchlikda ham urushga tayyor turilganda, biz ham ehtiyot bo'lishimiz kerakligini bildiradi.</p>",
        'correct': "대비하거늘",
        'choices': ["대비하는 탓에", "대비할 뿐만 아니라", "대비하거늘", "대비하려던 참이다"]
    },
    {
        'text': "<p>A: <u>사나운</u> 맹수도 <u>자기</u> <u>새끼는</u> <strong>보호하네요</strong>.<br>B: <u>짐승조차</u> <u>제</u> <u>자식을</u> <strong>아끼</strong>________ <u>사람이</u> <u>자식을</u> <strong>버리는</strong> <u>것은</u> <strong>말이</strong> <strong>안</strong> <strong>됩니다</strong>.</p>",
        'explanation': "<p><strong>아끼거늘</strong>: '아끼다' (asramoq/qizg'anmoq) fe'liga qo'shilib, yovvoyi hayvon ham bolasini asraganda, inson bolasini tashlashi aqlga sig'masligini ko'rsatadi.</p>",
        'correct': "아끼거늘",
        'choices': ["아끼다가는", "아끼거늘", "아낄 리가 없다", "아끼느라고"]
    },
    {
        'text': "<p>A: <u>저를</u> <strong>괴롭힌</strong> 사람을 <strong>용서해야</strong> <strong>할까요</strong>?<br>B: <u>성인군자는</u> <u>원수조차도</u> <strong>용서하</strong>________ <u>당신도</u> <u>넓은</u> 마음으로 <strong>품어주세요</strong>.</p>",
        'explanation': "<p><strong>용서하거늘</strong>: '용서하다' (kechirmoq) fe'liga qo'shilib, buyuklar dushmanni ham kechirganda, siz ham kechirishingiz kerakligini bildiradi.</p>",
        'correct': "용서하거늘",
        'choices': ["용서하거늘", "용서하는 바람에", "용서해 봤자", "용서하기 십상이다"]
    },
    {
        'text': "<p>A: <u>바위가</u> <u>물에</u> <strong>깎여서</strong> <strong>둥글게</strong> <strong>변했네요</strong>.<br>B: <u>단단한</u> 바위도 <u>물방울에</u> <strong>닳</strong>________ <u>사람의</u> 마음이라고 <strong>안</strong> <strong>변하겠어요</strong>?</p>",
        'explanation': "<p><strong>닳거늘</strong>: '닳다' (yeyilmoq) fe'liga qo'shilib, tosh ham yeyilib turganda, inson ko'ngli ham o'zgarishi tabiiyligini ko'rsatadi.</p>",
        'correct': "닳거늘",
        'choices': ["닳으려니 하고", "닳을 지경이다", "닳은 탓에", "닳거늘"]
    },
    {
        'text': "<p>A: <u>가뭄이</u> <u>너무</u> <strong>심해요</strong>.<br>B: <u>마르지</u> <strong>않을</strong> <u>것</u> <strong>같던</strong> <u>깊은</u> 우물도 <strong>마르</strong>________ <u>얕은</u> <u>개울물이야</u> <strong>오죽하겠습니까</strong>.</p>",
        'explanation': "<p><strong>마르거늘</strong>: '마르다' (qurimoq) fe'liga qo'shilib, chuqur quduq ham quriganda, sayoz ariq battar qurishini bildiradi.</p>",
        'correct': "마르거늘",
        'choices': ["마르다가는", "마르는 김에", "마르거늘", "마를 리가 없다"]
    },
    {
        'text': "<p>A: 하늘의 <u>별이</u> <u>구름에</u> <strong>가려졌어요</strong>.<br>B: <u>밝게</u> <strong>빛나는</strong> 별도 <u>먹구름에</u> <strong>숨</strong>________ <u>우리의</u> <u>미래도</u> <u>가끔은</u> <strong>흐릴</strong> <u>때가</u> <strong>있습니다</strong>.</p>",
        'explanation': "<p><strong>숨거늘</strong>: '숨다' (yashirinmoq) fe'liga qo'shilib, yulduz ham yashiringanda, kelajak ham gohida qorong'ilashishini ko'rsatadi.</p>",
        'correct': "숨거늘",
        'choices': ["숨기 십상이다", "숨거늘", "숨을 뿐만 아니라", "숨은 탓에"]
    },
    {
        'text': "<p>A: 부모님이 <u>자식을</u> <u>위해</u> <u>정말</u> 많이 <strong>희생하셨어요</strong>.<br>B: <u>부모는</u> <u>자식을</u> <u>위해</u> 목숨도 <strong>바치</strong>________ <u>자식이</u> 부모를 <strong>모시지</strong> <strong>않는</strong> <u>것은</u> 불효입니다.</p>",
        'explanation': "<p><strong>바치거늘</strong>: '바치다' (fido qilmoq) fe'liga qo'shilib, ota-ona jonini ham fido qilganda, farzand qaramasligi gunoh ekanini bildiradi.</p>",
        'correct': "바치거늘",
        'choices': ["바치는 통에", "바치거늘", "바쳤더라면", "바치려던 참이다"]
    },
    {
        'text': "<p>A: <u>형제끼리</u> <u>재산</u> <u>문제로</u> <strong>다투고</strong> <strong>있어요</strong>.<br>B: <u>피를</u> <strong>나눈</strong> 형제도 <u>이익</u> <u>앞에서는</u> <strong>싸우</strong>________ <u>남들은</u> <u>더</u> <strong>심하겠지요</strong>.</p>",
        'explanation': "<p><strong>싸우거늘</strong>: '싸우다' (urushmoq) fe'liga qo'shilib, aka-uka ham urishganda, begonalarning urishishi oddiy hol ekanini ko'rsatadi.</p>",
        'correct': "싸우거늘",
        'choices': ["싸우기 무섭게", "싸우려니 하고", "싸우거늘", "싸울 지라도"]
    },
    {
        'text': "<p>A: <u>기대가</u> <strong>크면</strong> <u>실망도</u> <strong>큰가</strong> <strong>봐요</strong>.<br>B: <u>산이</u> <strong>높으면</strong> <u>골짜기도</u> <strong>깊</strong>________ <u>기대가</u> <strong>크면</strong> <u>실망도</u> <strong>큰</strong> <u>법입니다</u>.</p>",
        'explanation': "<p><strong>깊거늘</strong>: '깊다' (chuqur bo'lmoq) sifatiga qo'shilib, tog' qancha baland bo'lsa darasi ham shuncha chuqur bo'lishidek haqiqatni bildiradi.</p>",
        'correct': "깊거늘",
        'choices': ["깊은 바람에", "깊다가는", "깊을 리가 없다", "깊거늘"]
    },
    {
        'text': "<p>A: <u>그렇게</u> <strong>권력이</strong> <strong>많던</strong> <u>사람도</u> <u>결국</u> <strong>구속되었네요</strong>.<br>B: <u>하늘을</u> <strong>찌를</strong> <u>듯한</u> 권력도 <u>결국은</u> <strong>무너지</strong>________ <u>사람의</u> <u>인생은</u> <strong>겸손해야</strong> <strong>합니다</strong>.</p>",
        'explanation': "<p><strong>무너지거늘</strong>: '무너지다' (qulamoq) fe'liga qo'shilib, kuchli hokimiyat ham qulab turganda, inson kamtar bo'lishi shartligini ko'rsatadi.</p>",
        'correct': "무너지거늘",
        'choices': ["무너지거늘", "무너진 채로", "무너지는 김에", "무너지기 마련이라서"]
    },
    {
        'text': "<p>A: <u>가을인데도</u> <u>아직</u> <u>날씨가</u> <strong>덥네요</strong>.<br>B: <u>겨울도</u> <strong>지나면</strong> <u>다시</u> <u>봄이</u> <strong>오</strong>________ <u>이</u> <u>더위도</u> <u>곧</u> <strong>물러갈</strong> 것입니다.</p>",
        'explanation': "<p><strong>오거늘</strong>: '오다' fe'liga qo'shilib, qishdan keyin ham bahor kelganda, bu issiq ham ketishi aniq ekanini bildiradi.</p>",
        'correct': "오거늘",
        'choices': ["오느라고", "오거늘", "올 뿐만 아니라", "올 지경이다"]
    },
    {
        'text': "<p>A: <u>저</u> <u>사람은</u> <u>정말</u> <u>나쁜</u> <u>짓을</u> <u>많이</u> <strong>했어요</strong>.<br>B: <u>하늘의</u> <u>그물은</u> <strong>엉성한</strong> <u>듯해도</u> <u>결코</u> <u>악인을</u> <strong>놓치지</strong> <strong>않</strong>________ <u>언젠가</u> <u>벌을</u> <strong>받을</strong> 것입니다.</p>",
        'explanation': "<p><strong>않거늘</strong>: '않다' inkor fe'liga qo'shilib, osmon (xudo) yomonlarni jazosiz qoldirmasligini tasdiqlab o'tishni ko'rsatadi.</p>",
        'correct': "않거늘",
        'choices': ["않거늘", "않기 십상이다", "않는 탓에", "않아 봤자"]
    },
    {
        'text': "<p>A: <u>윗사람이</u> <u>솔선수범해야</u> <strong>하나요</strong>?<br>B: <u>윗물이</u> <strong>맑아야</strong> <u>아랫물도</u> <strong>맑</strong>________ <u>윗사람의</u> <u>행동이</u> <strong>중요합니다</strong>.</p>",
        'explanation': "<p><strong>맑거늘</strong>: '맑다' (tiniq bo'lmoq) sifatiga qo'shilib, yuqoridagi suv tiniq bo'lsa pastdagi ham tiniq bo'lishidek mantiqni bildiradi.</p>",
        'correct': "맑거늘",
        'choices': ["맑으려던 참이다", "맑은 바람에", "맑거늘", "맑을 리가 없다"]
    },
    {
        'text': "<p>A: 달이 <u>구름에</u> <strong>가려져서</strong> <strong>안</strong> <strong>보여요</strong>.<br>B: 달도 <strong>차면</strong> <strong>기울고</strong> <u>구름에</u> <strong>가려지</strong>________ <u>우리</u> <u>인생도</u> <u>마찬가지입니다</u>.</p>",
        'explanation': "<p><strong>가려지거늘</strong>: '가려지다' (to'silmoq) fe'liga qo'shilib, oy ham bulut ortiga yashiringanda, inson hayoti ham birdek tekis emasligini ko'rsatadi.</p>",
        'correct': "가려지거늘",
        'choices': ["가려질 지라도", "가려지거늘", "가려진 채로", "가려지다가는"]
    }
]

# =====================================================================
# Topic 86: 극단적 양보와 포기: 동사/형용사 + 기로서니 (Ekstremal yon berish: ... bo'lgan taqdirda ham / ... degani bilan bunday qilish noto'g'ri)
# =====================================================================
topic_86 = [
    {
        'text': "<p>A: <u>그</u> 사람이 <u>너무</u> <strong>얄미워서</strong> <strong>때려주고</strong> <strong>싶어요</strong>.<br>B: <u>아무리</u> <strong>밉</strong>________ <u>사람을</u> <strong>때리면</strong> <strong>안</strong> <strong>되지요</strong>.</p>",
        'explanation': "<p><strong>밉기로서니</strong>: '밉다' (yomon ko'rmoq/yomon ko'rinmoq) sifatiga qo'shilib, qanchalik yomon ko'rinmasin (shunday degan taqdirda ham) urish mumkin emasligini bildiradi.</p>",
        'correct': "밉기로서니",
        'choices': ["미운 탓에", "밉기로서니", "밉다가는", "미워 봤자"]
    },
    {
        'text': "<p>A: 배가 <u>너무</u> <strong>고파서</strong> <u>남의</u> <u>빵을</u> <u>몰래</u> <strong>먹었어요</strong>.<br>B: <u>아무리</u> 배가 <strong>고프</strong>________ <u>허락도</u> <strong>없이</strong> <u>남의</u> <u>것을</u> <strong>먹으면</strong> <strong>어떡해요</strong>?</p>",
        'explanation': "<p><strong>고프기로서니</strong>: '고프다' sifatiga qo'shilib, qanchalik qorni och bo'lsa ham ruxsatsiz yeyish noto'g'riligini ko'rsatadi.</p>",
        'correct': "고프기로서니",
        'choices': ["고프기로서니", "고프기 십상이라서", "고플 지라도", "고픈 통에"]
    },
    {
        'text': "<p>A: <u>요즘</u> <u>회사</u> <u>일이</u> <u>너무</u> <strong>바빠서</strong> <u>부모님께</u> 연락을 <strong>못</strong> <strong>드렸어요</strong>.<br>B: <u>아무리</u> <strong>바쁘</strong>________ <u>전화</u> <u>한 통</u> <strong>할</strong> <u>시간이</u> <strong>없었겠어요</strong>?</p>",
        'explanation': "<p><strong>바쁘기로서니</strong>: '바쁘다' sifatiga qo'shilib, qanchalik band bo'lsa ham bir marta telefon qilishga vaqt topish kerakligini bildiradi.</p>",
        'correct': "바쁘기로서니",
        'choices': ["바쁘려니 하고", "바쁜 김에", "바쁘기로서니", "바쁠 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>어제</u> <u>너무</u> <strong>피곤해서</strong> <u>화장을</u> <strong>안</strong> <strong>지우고</strong> <strong>잤어요</strong>.<br>B: <u>아무리</u> <strong>피곤하</strong>________ <u>세수는</u> <strong>하고</strong> <strong>자야죠</strong>.</p>",
        'explanation': "<p><strong>피곤하기로서니</strong>: '피곤하다' sifatiga qo'shilib, qanchalik charchagan degan taqdirda ham yuzni yuvib yotish kerakligini ko'rsatadi.</p>",
        'correct': "피곤하기로서니",
        'choices': ["피곤하느라고", "피곤하기로서니", "피곤하다가는", "피곤해 봤자"]
    },
    {
        'text': "<p>A: 화가 <strong>나서</strong> <u>문서를</u> <u>다</u> <strong>찢어버렸어요</strong>.<br>B: <u>아무리</u> 화가 <strong>났</strong>________ <u>중요한</u> <u>서류를</u> <strong>찢으면</strong> <strong>안</strong> <strong>되죠</strong>.</p>",
        'explanation': "<p><strong>났기로서니</strong>: '나다' (화가 나다) fe'lining o'tgan zamoniga qo'shilib, jahli chiqqani bilan hujjatni yirtish oshib tushganini bildiradi.</p>",
        'correct': "났기로서니",
        'choices': ["나는 바람에", "났을 리가 없어서", "났기로서니", "났더라면"]
    },
    {
        'text': "<p>A: 돈이 <strong>없어서</strong> <u>부모님</u> <u>지갑에</u> 손을 <strong>댔어요</strong>.<br>B: <u>아무리</u> 돈이 <strong>없</strong>________ <u>어떻게</u> <u>도둑질을</u> <strong>할</strong> <u>수</u> <strong>있어요</strong>?</p>",
        'explanation': "<p><strong>없기로서니</strong>: '없다' sifatiga qo'shilib, puli yo'q degani bilan o'g'rilik qilish yaramasligini ko'rsatadi.</p>",
        'correct': "없기로서니",
        'choices': ["없기로서니", "없기 십상이라서", "없다가는", "없는 탓에"]
    },
    {
        'text': "<p>A: <u>이번</u> <u>일로</u> <u>너무</u> <strong>억울해서</strong> <u>회사를</u> <strong>그만둘래요</strong>.<br>B: <u>아무리</u> <strong>억울하</strong>________ <u>그렇게</u> <u>무책임하게</u> <strong>그만두면</strong> <strong>안</strong> <strong>돼요</strong>.</p>",
        'explanation': "<p><strong>억울하기로서니</strong>: '억울하다' (adakotsizlikdan qiynalmoq) sifatiga qo'shilib, alam qilgani bilan ishni tashlab ketish xatoligini bildiradi.</p>",
        'correct': "억울하기로서니",
        'choices': ["억울한 바람에", "억울할 지경이라서", "억울하기로서니", "억울하려던 참이라서"]
    },
    {
        'text': "<p>A: <u>아버지가</u> <strong>돌아가셔서</strong> <u>너무</u> <strong>슬퍼서</strong> <u>식음을</u> <strong>전폐하고</strong> <strong>있어요</strong>.<br>B: <u>아무리</u> <strong>슬프</strong>________ <u>산</u> <u>사람은</u> <strong>살아야지</strong> <u>밥을</u> <strong>안</strong> <strong>먹으면</strong> <strong>어떡해요</strong>.</p>",
        'explanation': "<p><strong>슬프기로서니</strong>: '슬프다' sifatiga qo'shilib, qayg'u qanchalik og'ir bo'lsa ham o'zini tashlab yubormaslik kerakligini ko'rsatadi.</p>",
        'correct': "슬프기로서니",
        'choices': ["슬플 뿐만 아니라", "슬프기로서니", "슬프다가는", "슬픈 통에"]
    },
    {
        'text': "<p>A: <u>급한</u> <u>일이</u> <strong>있어서</strong> <u>신호위반을</u> <strong>했어요</strong>.<br>B: <u>아무리</u> <strong>급하</strong>________ <u>법은</u> <strong>지켜야지</strong> <u>사고가</u> <strong>나면</strong> <strong>어떡하려고요</strong>.</p>",
        'explanation': "<p><strong>급하기로서니</strong>: '급하다' (shoshilinch bo'lmoq) sifatiga qo'shilib, shoshilganda ham qoidani buzish noto'g'riligini bildiradi.</p>",
        'correct': "급하기로서니",
        'choices': ["급하기로서니", "급할 리가 없어서", "급한 길에", "급하기 무섭게"]
    },
    {
        'text': "<p>A: <u>그</u> <u>사람이</u> <u>너무</u> <strong>싫어서</strong> <u>인사도</u> <strong>안</strong> <strong>했어요</strong>.<br>B: <u>아무리</u> <strong>싫</strong>________ <u>직장</u> <u>동료인데</u> <u>인사조차</u> <strong>안</strong> <strong>하는</strong> <u>것은</u> <strong>너무했어요</strong>.</p>",
        'explanation': "<p><strong>싫기로서니</strong>: '싫다' sifatiga qo'shilib, yomon ko'rgani bilan salomlashmaslik hurmatsizlik ekanini ko'rsatadi.</p>",
        'correct': "싫기로서니",
        'choices': ["싫어 봤자", "싫은 탓에", "싫다가는", "싫기로서니"]
    },
    {
        'text': "<p>A: <u>몸이</u> <u>많이</u> <strong>아파서</strong> <u>결석했어요</u>.<br>B: <u>아무리</u> <strong>아프</strong>________ <u>미리</u> <u>연락은</u> <strong>줬어야죠</strong>.</p>",
        'explanation': "<p><strong>아프기로서니</strong>: '아프다' sifatiga qo'shilib, kasal bo'lgan taqdirda ham oldindan aytib qo'yish kerakligini bildiradi.</p>",
        'correct': "아프기로서니",
        'choices': ["아픈 바람에", "아프기로서니", "아프려니 하고", "아플 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>일이</u> <u>너무</u> <strong>힘들어서</strong> <u>아무에게도</u> <strong>말</strong> <strong>안</strong> <strong>하고</strong> <strong>도망쳤어요</strong>.<br>B: <u>아무리</u> <strong>힘들</strong>________ <u>책임감</u> <strong>없이</strong> <strong>도망가면</strong> <strong>안</strong> <strong>되죠</strong>.</p>",
        'explanation': "<p><strong>힘들기로서니</strong>: '힘들다' sifatiga qo'shilib, qiyin bo'lgani bilan qochib ketish mas'uliyatsizlik ekanini ko'rsatadi.</p>",
        'correct': "힘들기로서니",
        'choices': ["힘들기 십상이라서", "힘든 통에", "힘들기로서니", "힘들었더라면"]
    },
    {
        'text': "<p>A: <u>늦잠을</u> <strong>자서</strong> <u>그냥</u> <u>학교에</u> <strong>안</strong> <strong>갔어요</strong>.<br>B: <u>아무리</u> <strong>늦었</strong>________ <u>수업에</u> <strong>참석은</strong> <strong>해야죠</strong>.</p>",
        'explanation': "<p><strong>늦었기로서니</strong>: '늦다' (kech qolmoq) sifatining o'tgan zamoniga qo'shilib, kechikkan taqdirda ham darsga borish shartligini bildiradi.</p>",
        'correct': "늦었기로서니",
        'choices': ["늦었기로서니", "늦을 지라도", "늦을 지경이라서", "늦는 바람에"]
    },
    {
        'text': "<p>A: <u>친구가</u> <u>약속을</u> <strong>어겨서</strong> <u>절교했어요</u>.<br>B: <u>아무리</u> <strong>실망했</strong>________ <u>한 번</u> <u>실수로</u> <strong>절교까지</strong> <strong>하는</strong> <u>건</u> <strong>너무해요</strong>.</p>",
        'explanation': "<p><strong>실망했기로서니</strong>: '실망하다' fe'lining o'tgan zamoniga qo'shilib, xafsalasi pir bo'lgani bilan do'stlikni butunlay uzish oshib tushganini ko'rsatadi.</p>",
        'correct': "실망했기로서니",
        'choices': ["실망해 봤자", "실망했더라면", "실망했기로서니", "실망하는 탓에"]
    },
    {
        'text': "<p>A: <u>술에</u> <strong>취해서</strong> <u>길가에서</u> <strong>잠들었어요</strong>.<br>B: <u>아무리</u> <strong>취했</strong>________ <u>길에서</u> <strong>자는</strong> <u>사람이</u> <u>어디</u> <strong>있어요</strong>?</p>",
        'explanation': "<p><strong>취했기로서니</strong>: '취하다' (mast bo'lmoq) fe'lining o'tgan zamoniga qo'shilib, mast bo'lgan taqdirda ham ko'chada yotish uyat ekanini bildiradi.</p>",
        'correct': "취했기로서니",
        'choices': ["취했기로서니", "취하는 바람에", "취할 지경이라서", "취하기 무섭게"]
    },
    {
        'text': "<p>A: <u>그</u> <u>규칙을</u> <strong>몰라서</strong> <strong>어겼어요</strong>.<br>B: <u>아무리</u> <strong>몰랐</strong>________ <u>규칙은</u> <strong>규칙인데</strong> <u>당연히</u> <strong>지켜야지</strong>.</p>",
        'explanation': "<p><strong>몰랐기로서니</strong>: '모르다' (bilmaslik) fe'lining o'tgan zamoniga qo'shilib, bilmagan taqdirda ham qoidani buzishni oqlab bo'lmasligini ko'rsatadi.</p>",
        'correct': "몰랐기로서니",
        'choices': ["모르는 탓에", "몰랐더라면", "몰랐기로서니", "모르다가는"]
    },
    {
        'text': "<p>A: <u>세수하기가</u> <u>너무</u> <strong>귀찮아서</strong> <u>그냥</u> <strong>자려고요</strong>.<br>B: <u>아무리</u> <strong>귀찮</strong>________ <u>씻지도</u> <strong>않고</strong> <strong>자면</strong> <u>피부가</u> <strong>상해요</strong>.</p>",
        'explanation': "<p><strong>귀찮기로서니</strong>: '귀찮다' (erinmoq/malol kelmoq) sifatiga qo'shilib, qanchalik erinchoqlik tutganda ham yuvinmaslik ziyondir degan ma'noni bildiradi.</p>",
        'correct': "귀찮기로서니",
        'choices': ["귀찮은 김에", "귀찮기로서니", "귀찮을 리가 없어서", "귀찮을 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>심심해서</u> <u>장난 전화를</u> <strong>걸었어요</strong>.<br>B: <u>아무리</u> <strong>심심하</strong>________ <u>경찰서에</u> <u>장난 전화를</u> <strong>하는</strong> <u>게</u> 말이 <strong>됩니까</strong>?</p>",
        'explanation': "<p><strong>심심하기로서니</strong>: '심심하다' (zerikmoq) sifatiga qo'shilib, zerikkani bilan politsiyaga hazillashish noto'g'ri ekanini ko'rsatadi.</p>",
        'correct': "심심하기로서니",
        'choices': ["심심하려던 참이라서", "심심한 바람에", "심심하기로서니", "심심할 지경이라서"]
    },
    {
        'text': "<p>A: <u>섭섭해서</u> <u>친구</u> <u>연락처를</u> <u>다</u> <strong>지웠어요</strong>.<br>B: <u>아무리</u> <strong>서운하</strong>________ <u>그렇게</u> <u>한 번에</u> <u>인연을</u> <strong>끊으면</strong> <strong>어떡해요</strong>.</p>",
        'explanation': "<p><strong>서운하기로서니</strong>: '서운하다' (xafa bo'lmoq/arazlamoq) sifatiga qo'shilib, arazlagan taqdirda ham raqamni o'chirib tashlash oshib tushganini bildiradi.</p>",
        'correct': "서운하기로서니",
        'choices': ["서운하기로서니", "서운해 봤자", "서운하다가는", "서운하는 통에"]
    },
    {
        'text': "<p>A: <u>합격해서</u> <u>너무</u> <strong>기뻐서</strong> <u>소리를</u> <strong>지르고</strong> <strong>난리를</strong> <strong>쳤어요</strong>.<br>B: <u>아무리</u> <strong>기쁘</strong>________ <u>도서관에서</u> <u>그러시면</u> <strong>안</strong> <strong>되죠</strong>.</p>",
        'explanation': "<p><strong>기쁘기로서니</strong>: '기쁘다' sifatiga qo'shilib, qanchalik xursand bo'lganda ham kutubxonada baqirish mumkin emasligini ko'rsatadi.</p>",
        'correct': "기쁘기로서니",
        'choices': ["기쁠 지라도", "기쁘기로서니", "기쁜 탓에", "기쁘기 마련이라서"]
    },
    {
        'text': "<p>A: <u>저</u> <u>아이는</u> <u>얼굴이</u> <strong>예뻐서</strong> <u>무엇이든</u> <u>다</u> <strong>용서가</strong> <strong>돼요</strong>.<br>B: <u>아무리</u> <strong>예쁘</strong>________ <u>나쁜</u> <u>짓을</u> <strong>한</strong> <u>것까지</u> <strong>용서할</strong> <u>수는</u> <strong>없지요</strong>.</p>",
        'explanation': "<p><strong>예쁘기로서니</strong>: '예쁘다' sifatiga qo'shilib, qanchalik chiroyli bo'lmasin xatosini doim kechirish noto'g'riligini bildiradi.</p>",
        'correct': "예쁘기로서니",
        'choices': ["예쁘기 십상이라서", "예쁠 뿐만 아니라", "예쁘기로서니", "예쁘려니 하고"]
    },
    {
        'text': "<p>A: <u>그</u> 사람이 <u>밉상이라서</u> <u>일부러</u> <u>일을</u> <strong>망쳤어요</strong>.<br>B: <u>아무리</u> <u>그 사람이</u> <strong>밉</strong>________ <u>공적인</u> <u>일을</u> <strong>망치면</strong> <strong>어떡합니까</strong>?</p>",
        'explanation': "<p><strong>밉기로서니</strong>: '밉다' sifatiga qo'shilib, u odamni yomon ko'rgani bilan ishni ataylab buzish mantiqsizlik ekanini ko'rsatadi.</p>",
        'correct': "밉기로서니",
        'choices': ["미운 바람에", "밉기로서니", "미울 지경이라서", "미워 봤자"]
    },
    {
        'text': "<p>A: <u>반찬이</u> <u>맛없어서</u> <u>다</u> <strong>버렸어요</strong>.<br>B: <u>아무리</u> <strong>맛없</strong>________ <u>음식을</u> <u>그렇게</u> 함부로 <strong>버리면</strong> <strong>벌을</strong> <strong>받아요</strong>.</p>",
        'explanation': "<p><strong>맛없기로서니</strong>: '맛없다' sifatiga qo'shilib, ta'mi yo'q bo'lgan taqdirda ham ovqatni isrof qilish yomonligini bildiradi.</p>",
        'correct': "맛없기로서니",
        'choices': ["맛없는 탓에", "맛없다가는", "맛없기로서니", "맛없을 리가 없어서"]
    },
    {
        'text': "<p>A: <u>귀신이</u> <strong>나올까</strong> <u>봐</u> <u>무서워서</u> <u>밤에는</u> 화장실도 <strong>안</strong> <strong>가요</strong>.<br>B: <u>아무리</u> <strong>무섭</strong>________ <u>집</u> 안인데 <u>그렇게까지</u> <strong>할</strong> <u>필요가</u> <strong>있을까요</strong>?</p>",
        'explanation': "<p><strong>무섭기로서니</strong>: '무섭다' sifatiga qo'shilib, qo'rqqani bilan o'z uyida hojatxonaga bormaslik haddan tashqariligini ko'rsatadi.</p>",
        'correct': "무섭기로서니",
        'choices': ["무섭기로서니", "무섭기 마련이라서", "무서워 봤자", "무서운 김에"]
    },
    {
        'text': "<p>A: <u>갑자기</u> 개가 <strong>튀어나와서</strong> <strong>놀라서</strong> <u>자전거를</u> <strong>버리고</strong> <strong>도망갔어요</strong>.<br>B: <u>아무리</u> <strong>놀랐</strong>________ <u>자기</u> <u>자전거를</u> <strong>버리고</strong> <strong>가는</strong> <u>사람이</u> <u>어디</u> <strong>있어요</strong>?</p>",
        'explanation': "<p><strong>놀랐기로서니</strong>: '놀라다' fe'lining o'tgan zamoniga qo'shilib, cho'chib tushgani bilan velosipedni tashlab qochish g'alatiligini bildiradi.</p>",
        'correct': "놀랐기로서니",
        'choices': ["놀라는 통에", "놀랐더라면", "놀랐기로서니", "놀라다가는"]
    },
    {
        'text': "<p>A: <u>질문에</u> <strong>당황해서</strong> <u>말을</u> <strong>더듬고</strong> <strong>울어버렸어요</strong>.<br>B: <u>아무리</u> <strong>당황했</strong>________ <u>면접장에서</u> <strong>울면</strong> <strong>감점입니다</strong>.</p>",
        'explanation': "<p><strong>당황했기로서니</strong>: '당황하다' fe'lining o'tgan zamoniga qo'shilib, sarosimaga tushgan taqdirda ham yig'lash noto'g'riligini ko'rsatadi.</p>",
        'correct': "당황했기로서니",
        'choices': ["당황했기로서니", "당황해 봤자", "당황할 지라도", "당황하려던 참이라서"]
    },
    {
        'text': "<p>A: <u>가난해서</u> <u>남의</u> <u>집</u> <u>앞에</u> <strong>버려진</strong> <u>음식을</u> <strong>주워</strong> <strong>먹었어요</strong>.<br>B: <u>아무리</u> <strong>가난하</strong>________ <u>위생에</u> <u>안</u> <u>좋은</u> <u>음식을</u> <strong>주워</strong> <strong>먹으면</strong> <strong>병납니다</strong>.</p>",
        'explanation': "<p><strong>가난하기로서니</strong>: '가난하다' (kambag'al bo'lmoq) sifatiga qo'shilib, kambag'al bo'lsa ham ko'chadan ovqat yeyish xavfliligini bildiradi.</p>",
        'correct': "가난하기로서니",
        'choices': ["가난하기 십상이라서", "가난한 탓에", "가난하기로서니", "가난할 뿐만 아니라"]
    },
    {
        'text': "<p>A: <u>제가</u> <strong>잘못했다고</strong> <u>사람들</u> <u>앞에서</u> <u>무릎을</u> <strong>꿇으래요</strong>.<br>B: <u>아무리</u> <strong>잘못했</strong>________ <u>사람의</u> <u>자존심을</u> <u>그렇게</u> <strong>짓밟으면</strong> <strong>안</strong> <strong>되죠</strong>.</p>",
        'explanation': "<p><strong>잘못했기로서니</strong>: '잘못하다' (xato qilmoq) fe'lining o'tgan zamoniga qo'shilib, xato qilgan bo'lsa ham tiz cho'ktirish insoniylikka to'g'ri kelmasligini ko'rsatadi.</p>",
        'correct': "잘못했기로서니",
        'choices': ["잘못하는 바람에", "잘못했기로서니", "잘못했더라면", "잘못하기 무섭게"]
    },
    {
        'text': "<p>A: <u>시험을</u> <strong>망쳐서</strong> <u>속상한</u> <u>마음에</u> <u>책을</u> <u>다</u> <strong>불태웠어요</strong>.<br>B: <u>아무리</u> <strong>속상하</strong>________ <u>책을</u> <strong>태우는</strong> <u>것은</u> <u>이성을</u> <strong>잃은</strong> <u>행동이에요</u>.</p>",
        'explanation': "<p><strong>속상하기로서니</strong>: '속상하다' (ko'ngli xira bo'lmoq) sifatiga qo'shilib, asabiylashgani bilan kitobni yoqish mantiqsizlik ekanini bildiradi.</p>",
        'correct': "속상하기로서니",
        'choices': ["속상할 지경이라서", "속상하기로서니", "속상하려니 하고", "속상한 김에"]
    },
    {
        'text': "<p>A: <u>택시비가</u> <strong>아까워서</strong> <u>3시간을</u> <strong>걸어왔어요</strong>.<br>B: <u>아무리</u> 돈이 <strong>아깝</strong>________ <u>3시간을</u> <strong>걸어오는</strong> <u>것은</u> <u>시간</u> <u>낭비예요</u>.</p>",
        'explanation': "<p><strong>아깝기로서니</strong>: '아깝다' (achinarli/qizg'anchiq bo'lmoq - pulga nisbatan) sifatiga qo'shilib, pulni tejagani bilan 3 soat piyoda yurish vaqt isrofi ekanini ko'rsatadi.</p>",
        'correct': "아깝기로서니",
        'choices': ["아까워 봤자", "아깝다가는", "아까운 탓에", "아깝기로서니"]
    }
]


