# Keimyung Korean Readings — stories 8–14 (real textbook passages from keimyung_21_story.txt).
# Import: python manage.py import_corner corner/management/commands/_stories_keimyung_8_14.py --author=<AUTHOR>

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
        "title":   "낙엽을 태우면서",
        "summary": "Kuz hovlisida xazon yoqish hidi hayotga yangi ishtiyoq uygʻotadi — lirik esse.",
        "order":   8,
        "grammar": [
            {
                "pattern":  "-지 않으면 안 되다",
                "meaning":  "...masdan boʻlmaydi = albatta ...ish kerak (majburiyat).",
                "examples": ["매일 낙엽을 긁어 모으지 않으면 안 된다.", "약속은 지키지 않으면 안 돼요."],
            },
            {
                "pattern":  "-나 보다",
                "meaning":  "...shekilli, ...ga oʻxshaydi (taxmin).",
                "examples": ["낙엽이 사람 수보다 많은가 보다.", "밖에 비가 오나 봐요."],
            },
            {
                "pattern":  "-건마는(건만)",
                "meaning":  "...boʻlsa-da, shunga qaramay (adabiy qarama-qarshilik).",
                "examples": ["날마다 하는 일이건마는 낙엽은 또 쌓인다.", "노력했건만 결과가 좋지 않았다."],
            },
            {
                "pattern":  "-(으)면서도",
                "meaning":  "...boʻla turib, shunga zid ravishda (garchi ...boʻlsa-da).",
                "examples": ["별일 없으면서도 쉴 새 없이 끙끙댄다.", "잘 알면서도 모르는 척했어요."],
            },
        ],
        "body": '''<p>가을이 <span class="cn-word" data-pos="verb" data-tr="avjiga chiqsa, chuqurlashsa">깊어지면</span>, 나는 거의 매일 <span class="cn-word" data-tr="hovli">뜰</span>의 <span class="cn-word" data-tr="xazon, toʻkilgan barg">낙엽</span>을 <span class="cn-word" data-pos="verb" data-tr="tirnab yigʻmoq">긁어 모으지</span> 않으면 안 된다. 날마다 하는 일이건마는 낙엽은 <span class="cn-word" data-pos="adv" data-tr="sezdirmay, allaqachon">어느새</span> 날아 떨어져서, <span class="cn-word" data-pos="adv" data-tr="yana, qaytadan">또다시</span> <span class="cn-word" data-pos="verb" data-tr="toʻplanadigan, uyiladigan">쌓이는</span> 것이다. 낙엽이란 <span class="cn-word" data-pos="adv" data-tr="haqiqatan, rostdan">참으로</span> 이 세상 사람의 수보다도 많은가 보다.</p>
<p>벚나무 아래 긁어 모은 낙엽의 <span class="cn-word" data-tr="uyum, tepa">산더미</span>에 불을 <span class="cn-word" data-pos="verb" data-tr="yoqsang, oʻt qoʻysang">붙이면</span>, 속의 것부터 푸슥푸슥 타기 시작해서 가는 연기가 <span class="cn-word" data-pos="verb" data-tr="koʻtarilib chiqib">피어오르고</span>, 바람이 없는 날이면 어느새 뜰 안은 연기로 <span class="cn-word" data-pos="verb" data-tr="toʻlib ketadi">가득해진다</span>. 낙엽 타는 냄새 같이 좋은 것이 있을까? 갓 볶아 낸 커피의 냄새가 난다. <span class="cn-word" data-tr="xaskash">갈퀴</span>를 손에 들고 연기 속에 서서, 타서 <span class="cn-word" data-pos="verb" data-tr="tarqaladigan, sochiladigan">흩어지는</span> 낙엽의 산더미를 바라보며 <span class="cn-word" data-pos="adj" data-tr="xushbuy, muattar">향기로운</span> 냄새를 맡고 있노라면 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">별안간</span> <span class="cn-word" data-pos="adj" data-tr="kuchli">강한</span> 생활의 <span class="cn-word" data-tr="ishtiyoq, gʻayrat">의욕</span>을 느끼게 된다. 연기는 몸에 배서 어느새 옷과 손등에서도 냄새가 나게 된다. 나는 그 냄새를 <span class="cn-word" data-pos="adv" data-tr="cheksiz, behad">한없이</span> 사랑하면서 즐거운 생활감에 빠져서는 새삼스럽게 생활을 <span class="cn-word" data-pos="adj" data-tr="qadrli, qimmatli">귀중한</span> 것으로 생각하게 된다.</p>
<p>가을이다! 가을은 생활의 계절이다. 나는 화단의 뒷자리를 <span class="cn-word" data-pos="adv" data-tr="chuqur qilib">깊게</span> <span class="cn-word" data-pos="verb" data-tr="kavlab, qazib">파고</span> 다 타버린 낙엽의 <span class="cn-word" data-tr="kul">재</span>를 죽어 버린 꿈의 시체를-땅속 깊이 <span class="cn-word" data-pos="verb" data-tr="koʻmib">파묻고</span>, <span class="cn-word" data-pos="adj" data-tr="matonatli, qatʼiy">꿋꿋한</span> 생활의 자세로 <span class="cn-word" data-pos="verb" data-tr="yuz burmoq, qaytmoq">돌아서지</span> 않으면 안 된다. 이야기 속의 소년 같이 <span class="cn-word" data-pos="verb" data-tr="jasur boʻlmoq">용감해지지</span> 않으면 안 된다.</p>
<p><span class="cn-word" data-pos="adj" data-tr="sovuq">차가운</span> 넓은 방에서 차를 마시면서 생각하는 것이 생활의 생각이다. 방구석에는 올 겨울에 또 크리스마스트리를 <span class="cn-word" data-pos="verb" data-tr="tikmoq, oʻrnatmoq">세우고</span> 예쁘게 <span class="cn-word" data-pos="verb" data-tr="bezash">장식할</span> 것을 생각하고, 눈이 오면 스키를 시작해 볼까 하고 계획도 해 보곤 한다. 이런 생각을 할 때만은 <span class="cn-word" data-tr="gʻam-tashvish">근심</span>과 걱정도 <span class="cn-word" data-pos="adv" data-tr="qayoqqadir, allaqayerga">어디론가</span> <span class="cn-word" data-pos="verb" data-tr="yoʻqoladi">사라져</span> 버린다. 책과 씨름하고, <span class="cn-word" data-tr="qoʻlyozma qogʻozi">원고지</span> 앞에서 끙끙대던 서재에서 <span class="cn-word" data-pos="adj" data-tr="yengil, tetik">개운한</span> 마음으로 이런 생각을 하는 것은 참으로 <span class="cn-word" data-pos="adj" data-tr="huzurbaxsh, quvnoq">유쾌한</span> 일이다.</p>
<p>책상 앞에 앉아, 별일 없으면서도 <span class="cn-word" data-pos="adv" data-tr="tinimsiz, toʻxtovsiz">쉴 새 없이</span> 끙끙대고, 생각하고, <span class="cn-word" data-pos="verb" data-tr="azob chekib, qiynalib">괴로워하고</span> 하면서, 생활의 일이라면 아무리 짧은 시간이라도 <span class="cn-word" data-pos="verb" data-tr="tejab, ayamoq">아끼고</span>, 가령 뜰을 정리하는 것도 소비적이니 비생산적이니 하고 <span class="cn-word" data-pos="verb" data-tr="mensimay qaragan, past koʻrgan">깔보던</span> 것이, <span class="cn-word" data-pos="adv" data-tr="aksincha">도리어</span> 그런 생활의 작은 일에 창조적, 생산적인 뜻을 <span class="cn-word" data-pos="verb" data-tr="kashf qilmoq, topmoq">발견하게</span> 된 것은 <span class="cn-word" data-pos="adv" data-tr="aslida, nahotki">대체</span> 무슨 까닭일까? 계절의 탓일까? 깊어가는 가을이, 이 벌거숭이의 뜰이 <span class="cn-word" data-pos="adv" data-tr="yanada, bir pogʻona">한층</span> 산 <span class="cn-word" data-tr="mazmun, qoniqish hissi">보람</span>을 느끼게 하는 탓일까?</p>''',
        "questions": [
            {
                "text": "글쓴이가 낙엽을 태우면서 느끼는 감정으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "낙엽을 치우는 일이 귀찮고 짜증스럽다.",
                    "낙엽 타는 냄새를 맡으며 강한 생활의 의욕을 느낀다.",
                    "가을이 끝나가서 슬프고 외롭다.",
                ],
                "answer": 1,
                "explanation": "Matnda muallif xazon yonayotgan hidini hidlab \"별안간 강한 생활의 의욕을 느끼게 된다\" deb yozadi — yaʼni hayotga kuchli ishtiyoq uygʻonadi. Bezovtalik yoki gʻamginlik emas.",
            },
            {
                "text": "이 글에서 '가을'은 글쓴이에게 어떤 계절입니까?",
                "choices": [
                    "생활의 의욕을 일깨우는 생활의 계절",
                    "공부만 해야 하는 힘든 계절",
                    "여행을 떠나기 좋은 계절",
                ],
                "answer": 0,
                "explanation": "Muallif \"가을은 생활의 계절이다\" deb aytadi va kuz unda hayotga boʻlgan ishtiyoqni uygʻotishini taʼkidlaydi.",
            },
            {
                "text": "글쓴이가 예전에는 뜰을 정리하는 일을 어떻게 생각했습니까?",
                "choices": [
                    "창조적이고 생산적인 일이라고 생각했다.",
                    "소비적이고 비생산적인 일이라고 깔보았다.",
                    "남에게 맡겨야 하는 일이라고 생각했다.",
                ],
                "answer": 1,
                "explanation": "Matnda muallif ilgari hovli yigʻishtirishni \"소비적이니 비생산적이니 하고 깔보던\" (isrofgarchilik, unumsiz deb mensimagan) deb yozadi; keyin esa uning ijodiy maʼnosini kashf etadi.",
            },
        ],
    },
    {
        "title":   "한국인과 함께해 온 떡",
        "summary": "Tugʻilgan kundan bayramlargacha: koreyslarning ttok (guruch noni) bilan bogʻliq anʼanalari.",
        "order":   9,
        "grammar": [
            {
                "pattern":  "-았/었으면 하는 마음으로",
                "meaning":  "...sa edi degan niyat/tilak bilan.",
                "examples": ["아기가 오래 살았으면 하는 마음으로 백설기를 나눈다.", "합격했으면 하는 마음으로 기도했어요."],
            },
            {
                "pattern":  "-(으)ㄹ 겸 (해서)",
                "meaning":  "...ni ham koʻzlab, bir yoʻla ikki maqsadda.",
                "examples": ["이웃과 나누어 먹을 겸 해서 떡을 많이 했다.", "바람도 쐴 겸 산책을 나갔어요."],
            },
            {
                "pattern":  "-는 만큼",
                "meaning":  "...gani sababli / ...gan darajada (mutanosiblik).",
                "examples": ["떡을 사랑하는 만큼 관련 속담도 많다.", "노력한 만큼 좋은 결과를 얻었어요."],
            },
            {
                "pattern":  "-(으)ㄴ지 알 수 없다",
                "meaning":  "...ganini bilib boʻlmaydi (nomaʼlumlik).",
                "examples": ["언제 처음 먹기 시작했는지 알 수 없다.", "그가 왜 떠났는지 알 수 없어요."],
            },
        ],
        "body": '''<p>'밥 먹는 배 다르고, 떡 먹는 배 다르다'라는 말이 있을 정도로 떡은 한국 사람들이 가장 좋아하는 음식 중의 하나이다. 한국에서 떡을 언제 처음 먹기 시작했는지 알 수 없지만 <span class="cn-word" data-pos="adv" data-tr="qadimdan">옛날부터</span> <span class="cn-word" data-tr="milliy bayram">명절</span>이나 중요한 행사가 있을 때 <span class="cn-word" data-pos="verb" data-tr="tushib qolmaydigan">빠지지</span> 않는 음식이었다.</p>
<p><span class="cn-word" data-pos="verb" data-tr="tugʻilgan">태어난</span> 아기가 <span class="cn-word" data-tr="chaqaloqning 100 kunligi">백일</span>이나 <span class="cn-word" data-tr="bir yoshlik toʻyi">돌</span>이 되면 백설기와 수수경단을 먹었다. 백설기는 아기가 건강하게 오래 살았으면 하는 마음으로 백 사람과 <span class="cn-word" data-pos="verb" data-tr="boʻlishib, ulashib">나눠</span> 먹었으며 수수경단은 팥의 붉은색이 <span class="cn-word" data-tr="yovuz ruh, ins-jins">귀신</span>을 <span class="cn-word" data-pos="verb" data-tr="toʻsmoq, himoya qilmoq">막아</span> 준다고 생각했기 때문에 아기에게 먹였다. <span class="cn-word" data-tr="nikoh marosimi">혼례</span> 때는 두 사람의 행복을 <span class="cn-word" data-pos="verb" data-tr="tilaydigan">기원하는</span> 의미로 보름달처럼 생긴 달떡과 여러 색깔의 색편을 먹었고, <span class="cn-word" data-tr="60 yoshlik yubiley">회갑</span> 때는 각종 떡을 같은 크기의 직사각형 모양으로 <span class="cn-word" data-pos="verb" data-tr="toʻgʻrab, kesib">썰어</span> <span class="cn-word" data-pos="adv" data-tr="baland qilib">높이</span> <span class="cn-word" data-pos="verb" data-tr="uyib, taxlab">쌓은</span> 후 상에 올렸다. <span class="cn-word" data-tr="ajdodlarni xotirlash marosimi">제사</span> 때도 지방마다 다른 여러 가지 떡을 중요한 제물로 올렸다.</p>
<p>명절에 먹는 <span class="cn-word" data-pos="adj" data-tr="eng mashhur, namunaviy">대표적인</span> 떡으로는 가래떡과 송편이 있다. 설날에 먹는 가래떡은 옛날 <span class="cn-word" data-tr="pul">화폐</span>를 <span class="cn-word" data-pos="verb" data-tr="andoza olib, oʻxshatib">본떠서</span> <span class="cn-word" data-pos="adj" data-tr="yumaloq">둥글고</span> 길게 빼는데 이것은 재산이 <span class="cn-word" data-pos="adv" data-tr="jadal, tez">쑥쑥</span> 늘어나라는 의미를 가지고 있다. 이렇게 만든 가래떡을 <span class="cn-word" data-pos="adv" data-tr="yupqa qilib">얇게</span> 썰어서 고깃국물에 <span class="cn-word" data-pos="verb" data-tr="qaynatmoq">끓이면</span> 떡국이 된다. 옛날에는 설날에 떡국 한 그릇을 먹어야 나이를 한 살 더 먹는 것이라고 생각했기 때문에 아이들은 떡국을 많이 먹으려고 떼를 쓰기도 했다. 추석에 먹는 송편은 한 해의 <span class="cn-word" data-tr="hosil">수확</span>을 감사하며 <span class="cn-word" data-tr="ajdodlar">조상</span>의 차례상에 올리는 음식이었는데 요즘은 계절에 관계없이 <span class="cn-word" data-pos="adv" data-tr="sevib, xushlab">즐겨</span> 먹는다.</p>
<p>떡은 일상생활과도 <span class="cn-word" data-pos="adj" data-tr="yaqin, uzviy">밀접한</span> 관련이 있다. <span class="cn-word" data-tr="ish boshlash, doʻkon ochish">개업</span>을 하거나 이사를 가면 이웃에게 시루떡을 <span class="cn-word" data-pos="verb" data-tr="tarqatib, ulashib">돌리면서</span> 인사를 나눈다. 시험을 치는 학생에게는 꼭 <span class="cn-word" data-pos="verb" data-tr="(imtihondan) oʻtsin degan">붙으라는</span> 뜻으로 찹쌀떡을 선물하기도 한다. 학교에서는 책을 다 배우면 그것을 축하하고 앞으로 <span class="cn-word" data-pos="adv" data-tr="yanada">더욱</span> 열심히 공부하라는 뜻으로 책거리를 하는데, 이때도 떡이 빠지지 않았다. 그리고 요즘에는 아침 식사 대용으로도 인기가 많다. 바쁜 아침 시간에 <span class="cn-word" data-pos="adv" data-tr="qulay, oson">간편하게</span> 먹기 좋을 뿐만 아니라 <span class="cn-word" data-tr="toʻqlik hissi">포만감</span>이 있고 건강에도 좋기 때문이다. 그러고 보면 떡은 <span class="cn-word" data-pos="adv" data-tr="doim, hamisha">항상</span> 한국인과 함께 해 온 음식이라고 할 수 있겠다.</p>
<p>한국인이 떡을 사랑하는 만큼 떡과 관련된 <span class="cn-word" data-tr="maqol">속담</span>도 <span class="cn-word" data-pos="adv" data-tr="juda, gʻoyat">매우</span> 많다. '밥 위에 떡'이라는 말은 밥으로도 이미 <span class="cn-word" data-pos="adj" data-tr="yetarli">충분한</span>데 밥 보다 더 좋은 떡을 그 위에 <span class="cn-word" data-pos="verb" data-tr="ustiga qoʻygani uchun">얹었으니</span> 이보다 더 좋을 수 없다는 뜻이다. 그 정도로 떡을 좋아했던 한국 사람들은 자기 집 식구만을 위하여 떡을 하는 것이 아니라 이웃집과도 나누어 먹을 겸 해서 많은 양의 떡을 했다. '남의 떡에 설 쇤다'와 '얻은 떡이 두레 반이다'는 이웃과 함께 정을 나누는 한국인의 모습을 <span class="cn-word" data-pos="verb" data-tr="sezib olmoq, koʻrib olmoq">엿볼</span> 수 있는 속담이다.</p>''',
        "questions": [
            {
                "text": "이 글의 중심 내용으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "떡을 만드는 방법",
                    "떡이 한국인의 삶과 문화에 깊이 관련되어 있다는 것",
                    "떡이 건강에 나쁘다는 것",
                ],
                "answer": 1,
                "explanation": "Matn tugʻilishdan bayramlargacha, kundalik hayotdan maqollargacha ttokning koreyslar hayoti va madaniyati bilan chuqur bogʻliqligini koʻrsatadi. Tayyorlash usuli asosiy mavzu emas.",
            },
            {
                "text": "수수경단을 아기에게 먹인 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "팥의 붉은색이 귀신을 막아 준다고 믿어서",
                    "수수가 가장 값이 싼 곡식이어서",
                    "아기가 수수를 가장 좋아해서",
                ],
                "answer": 0,
                "explanation": "Matnda \"팥의 붉은색이 귀신을 막아 준다고 생각했기 때문에\" chaqaloqqa suvsu-kyondan berilgani aytilgan.",
            },
            {
                "text": "다음 중 떡과 관련된 상황으로 이 글에 나오지 않은 것은 무엇입니까?",
                "choices": [
                    "이사를 가서 이웃에게 시루떡을 돌리는 것",
                    "시험 보는 학생에게 찹쌀떡을 선물하는 것",
                    "생일에 미역국 대신 떡을 먹는 것",
                ],
                "answer": 2,
                "explanation": "Matnda koʻchish (시루떡), imtihon (찹쌀떡), shuningdek 백일·돌·혼례·회갑·제사 kabi holatlar bor, lekin tugʻilgan kunda 미역국 oʻrniga ttok yeyish haqida gap yoʻq.",
            },
        ],
    },
    {
        "title":   "선배들이 알려 주는 A+ 비결",
        "summary": "Stipendiya va A+ olishning yoʻllari: fan tanlash, davomat va oʻqish usullari.",
        "order":   10,
        "grammar": [
            {
                "pattern":  "-다가는",
                "meaning":  "Shu zaylda davom etsa (yomon oqibat kelib chiqadi).",
                "examples": ["즐기기만 하다가는 좋은 학점은 그림의 떡이 된다.", "이렇게 놀다가는 시험에 떨어져요."],
            },
            {
                "pattern":  "-기 십상이다",
                "meaning":  "Osongina ...boʻlib qoladi, ...ishi tayin (koʻpincha salbiy).",
                "examples": ["지각이 반복되면 나쁜 인상을 주기 십상이다.", "서두르면 실수하기 십상이에요."],
            },
            {
                "pattern":  "-는 법이다",
                "meaning":  "Qonuniyat: odatda tabiiy ravishda shunday boʻladi.",
                "examples": ["어려운 수업은 재수강자가 많은 법이다.", "노력하면 좋은 결과가 오는 법이에요."],
            },
            {
                "pattern":  "-더라도",
                "meaning":  "...boʻlsa ham (kuchli yon berish).",
                "examples": ["다른 것이 아무리 완벽하더라도 공부가 먼저다.", "힘들더라도 포기하지 마세요."],
            },
        ],
        "body": '''<p>대학에 첫발을 <span class="cn-word" data-pos="verb" data-tr="qadam qoʻyadigan">내딛는</span> <span class="cn-word" data-tr="birinchi kurs talabasi">새내기</span>들이 <span class="cn-word" data-pos="verb" data-tr="tanlagan, saralagan">뽑은</span> '대학생이 되어 가장 해 보고 싶은 것' 다섯 가지 안에 빠지지 않고 들어가는 것이 <span class="cn-word" data-tr="stipendiya">장학금</span> 받기와 A+ 받기라고 한다. 그러나 준비하지 않고, 최선을 다하지 않고, 캠퍼스의 <span class="cn-word" data-tr="romantika">낭만</span>을 <span class="cn-word" data-pos="adv" data-tr="shunchaki, cheksiz">마냥</span> 즐기기만 하다가는 장학금과 A 학점은 <span class="cn-word" data-tr="yeb boʻlmas holva (faqat orzu)">그림의 떡</span>이 되고 말 것이다. 그렇다면 어떻게 해야 좋은 점수를 받을 수 있을까? 신입생들에게 <span class="cn-word" data-pos="verb" data-tr="aytib beradigan">들려주는</span> 선배들의 <span class="cn-word" data-tr="tajriba sirlari">노하우</span>에 귀를 <span class="cn-word" data-pos="verb" data-tr="qaratmoq (quloq solmoq)">기울여</span> 보자.</p>
<p><span class="cn-word" data-pos="verb" data-tr="tuzilgan">짜여진</span> 시간표대로 수업을 듣는 중 고등학생 때와 달리 대학생이 되면 자신이 <span class="cn-word" data-pos="adv" data-tr="bevosita, oʻzi">직접</span> 시간표를 <span class="cn-word" data-pos="verb" data-tr="tuzmoq">짜야</span> 한다.</p>
<p>어떤 과목을 <span class="cn-word" data-pos="verb" data-tr="tanlash">선택하느냐</span>에 따라 한 학기의 공부 방향과 그 결과가 <span class="cn-word" data-pos="verb" data-tr="belgilanadigani uchun">결정되기에</span> 좋은 학점을 받기 위해서는 <span class="cn-word" data-pos="adv" data-tr="avval, birinchi">먼저</span> <span class="cn-word" data-tr="fanlarga yozilish">수강 신청</span>이라는 '첫 단추'를 잘 끼워야 한다. 시간표를 짤 때 필수 전공 과목을 <span class="cn-word" data-pos="verb" data-tr="hisobga olmagan, chiqarib tashlagan">제외한</span> 나머지는 자신이 수강하고 싶은 과목보다는 자신이 잘할 수 있는 과목을 선택하는 것이 좋다. 또한 과목명만 보고 신청하지 말고 사전에 <span class="cn-word" data-tr="fan rejasi (sillabus)">강의 계획서</span>를 <span class="cn-word" data-pos="adv" data-tr="sinchkovlik bilan, puxta">꼼꼼히</span> 읽어 보거나 이미 그 수업을 들었던 선배들과 동기들의 충고를 <span class="cn-word" data-pos="adv" data-tr="imkon qadar">최대한</span> <span class="cn-word" data-pos="verb" data-tr="eʼtiborga olib, oʻrganib">참고해서</span> 신청해야 한다. 마지막으로, 학점을 짜게 주는 교수님의 수업이나 어려운 수업은 <span class="cn-word" data-tr="fanni qayta oʻqiydigan talaba">재수강자</span>가 많은 법이니 수강하려는 과목에 재수강자가 많지는 않는지 <span class="cn-word" data-pos="verb" data-tr="koʻrib chiqmoq, tekshirmoq">살펴보는</span> 것도 잊지 말도록 하자.</p>
<p>대학교에 들어가면 <span class="cn-word" data-tr="toʻliq davomat mukofoti">개근상</span>도 없고 등교 시간도 정해져 있지 않기에 지각을 하거나 <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> 수업에 빠져도 된다는 생각을 하는 새내기들이 <span class="cn-word" data-pos="adv" data-tr="baʼzan, ora-sira">더러</span> 있다. 그러나 이것이 <span class="cn-word" data-pos="verb" data-tr="takrorlansa">반복되면</span> 전체 수업 분위기에 방해가 되기 때문에 교수님에게 나쁜 인상을 주기 십상이다. 시험과 과제 점수가 <span class="cn-word" data-pos="adj" data-tr="oʻxshash, yaqin">비슷할</span> 경우 학점을 <span class="cn-word" data-pos="verb" data-tr="hal qiladigan, belgilaydigan">결정짓는</span> 것이 <span class="cn-word" data-tr="davomat">출결</span> 상황이기 때문에 결석과 지각은 가능한 한 하지 않는 것이 좋다.</p>
<p>좋은 성적을 받기 <span class="cn-word" data-pos="adj" data-tr="qulay boʻlishi uchun">유리하도록</span> 수강 신청을 하고 출석을 잘하는 것도 중요하지만 열심히 공부하는 것만큼 중요한 것은 없다. 이러한 공부가 <span class="cn-word" data-pos="verb" data-tr="qoʻllab-quvvatlanmasa, asoslanmasa">뒷받침되지</span> 않고서는, 다른 것들이 아무리 <span class="cn-word" data-pos="adj" data-tr="mukammal boʻlsa ham">완벽하더라도</span> 좋은 성적을 기대할 수 없다. 대학교의 수업 방식은 중 고등학교 시절 받아 오던 <span class="cn-word" data-tr="quruq yodlatish taʼlimi">주입식 교육</span>과는 차이가 있어 <span class="cn-word" data-pos="adv" data-tr="soʻzsiz, koʻr-koʻrona">무조건</span> 외우는 방식만으로는 자신의 것으로 만들 수 없다. 수업 전 수업 계획표에 따라 <span class="cn-word" data-tr="oldindan oʻrganish">예습</span>을 하고 수업이 끝난 후 <span class="cn-word" data-tr="takrorlash">복습</span>을 할 뿐만 아니라 다른 관련 서적을 참고한다면 그 과목에 대한 공부는 <span class="cn-word" data-pos="adv" data-tr="ancha, sezilarli">한결</span> <span class="cn-word" data-pos="adj" data-tr="osonlashadigan">수월해질</span> 것이다.</p>
<p><span class="cn-word" data-pos="adj" data-tr="aʼlo, yuqori">우수한</span> 성적을 받는 것 외에도 장학금을 받을 수 있는 방법은 많다. 장학금은 학점이 좋은 학생들만 받을 수 있는 것이라 생각하는 사람들이 많은데 <span class="cn-word" data-pos="adv" data-tr="aslida, amalda">실제로</span> 그렇지 않다. 근로 장학금, 장애우 도우미 장학금 뿐만 아니라 외국어 실력이 <span class="cn-word" data-pos="adj" data-tr="aʼlo boʻlsa, yuqori boʻlsa">뛰어나거나</span> 학교에서 <span class="cn-word" data-pos="verb" data-tr="oʻtkazadigan, tashkil etadigan">개최하는</span> 각종 대회에서 <span class="cn-word" data-pos="verb" data-tr="sovrin egallagan">입상한</span> 학생에게 <span class="cn-word" data-pos="verb" data-tr="beriladigan, taqdim etiladigan">수여하는</span> 장학금도 있다. 또한 특정 기업이나 단체에서 주는 장학금과 국가장학금 등 교외 장학금 제도도 많으니 학교홈페이지를 통해 어떤 장학금이 있는지, 그리고 조건이 무엇인지 꼼꼼히 살펴보는 것이 필요하다.</p>''',
        "questions": [
            {
                "text": "이 글에서 좋은 학점을 받기 위해 가장 먼저 잘해야 한다고 한 것은 무엇입니까?",
                "choices": [
                    "수강 신청 ('첫 단추')",
                    "시험 공부",
                    "교수님과 친해지기",
                ],
                "answer": 0,
                "explanation": "Matnda \"먼저 수강 신청이라는 '첫 단추'를 잘 끼워야 한다\" deyilgan — yaʼni fanga yozilish birinchi va eng muhim qadam.",
            },
            {
                "text": "시험과 과제 점수가 비슷할 때 학점을 결정짓는 것은 무엇이라고 했습니까?",
                "choices": [
                    "출결 상황",
                    "교수님과의 친분",
                    "자리 위치",
                ],
                "answer": 0,
                "explanation": "Matnda \"시험과 과제 점수가 비슷할 경우 학점을 결정짓는 것이 출결 상황\" deyilgan — shu sabab dars qoldirmaslik va kechikmaslik muhim.",
            },
            {
                "text": "장학금에 대한 이 글의 설명과 일치하는 것은 무엇입니까?",
                "choices": [
                    "오직 학점이 좋은 학생만 장학금을 받을 수 있다.",
                    "외국어 실력이나 대회 입상으로도 장학금을 받을 수 있다.",
                    "장학금은 국가만 준다.",
                ],
                "answer": 1,
                "explanation": "Matnda stipendiya faqat yuqori baholi talabalar uchun emasligi, chet til bilimi yoki tanlovda sovrin olish orqali ham olish mumkinligi aytilgan.",
            },
        ],
    },
    {
        "title":   "한석봉과 어머니",
        "summary": "Qorongʻida ona ttok kesadi, oʻgʻil xat yozadi — mashhur xattot Han Sokbong hikoyasi.",
        "order":   11,
        "grammar": [
            {
                "pattern":  "-(으)로 하여금 -게 하다",
                "meaning":  "...ni ...ishga majbur/sabab qilmoq (rasmiy orttirma).",
                "examples": ["왕은 석봉으로 하여금 문서를 작성하게 했다.", "그 일이 나로 하여금 다시 생각하게 했다."],
            },
            {
                "pattern":  "-은/는 고사하고",
                "meaning":  "... u yoqda tursin, hatto ...ham (yoʻq/mumkin emas).",
                "examples": ["서당은 고사하고 종이도 살 수 없었다.", "여행은 고사하고 쉴 시간도 없어요."],
            },
            {
                "pattern":  "-다 못해",
                "meaning":  "...ning chidamiga chidamay, uddasidan chiqolmay.",
                "examples": ["어머니가 보고 싶어 참다 못해 집으로 달려갔다.", "배가 고파 참다 못해 라면을 끓였어요."],
            },
            {
                "pattern":  "-(으)ㄹ 턱이 없다",
                "meaning":  "...ishi aslo mumkin emas (kuchli inkor).",
                "examples": ["십 년 공부로 어머니를 이길 턱이 없었다.", "준비도 안 했는데 잘될 턱이 없어요."],
            },
        ],
        "body": '''<p>'글씨'라고 하면 조선 시대 한석봉을 최고로 <span class="cn-word" data-pos="verb" data-tr="sanaydigan, hisoblaydigan">꼽는</span> 사람들이 많다. 25세의 나이에 <span class="cn-word" data-tr="davlat mansab imtihoni (qadimgi)">과거 시험</span>에 <span class="cn-word" data-pos="verb" data-tr="imtihondan oʻtib">합격하여</span> <span class="cn-word" data-tr="mansab, lavozim">관직</span>에 올랐고, 중국에 <span class="cn-word" data-tr="elchi">사신</span>으로 왕래하면서 <span class="cn-word" data-tr="mashhur xattot">명필가</span>로 이름을 <span class="cn-word" data-pos="verb" data-tr="taratdi, mashhur boʻldi">떨쳤다</span>. 왕은 벽에 <span class="cn-word" data-pos="adv" data-tr="doim">항상</span> 석봉의 글씨를 걸어 두고 감상할 정도로 좋아했으며, 석봉으로 하여금 나라의 주요 문서를 <span class="cn-word" data-pos="verb" data-tr="oʻz zimmasiga olib">도맡아</span> 작성하게 했다. 『석봉천자문』이라는 책을 <span class="cn-word" data-pos="verb" data-tr="qoldirib">남겨</span> 오늘날까지 한자를 처음 배우는 사람들에게 <span class="cn-word" data-tr="namuna darslik">교본</span>이 되게 한 그의 명필 뒤에는 다음과 같은 이야기가 있다.</p>
<p>석봉은 세 살 때 아버지를 <span class="cn-word" data-pos="verb" data-tr="yetim qolib (ota-onadan ayrilib)">여의고</span> 떡 장사로 <span class="cn-word" data-pos="adv" data-tr="zoʻrgʻa, arang">겨우</span> 살림을 <span class="cn-word" data-pos="verb" data-tr="davom ettiradigan">이어가는</span> 어머니와 함께 살았다. <span class="cn-word" data-tr="eski maktab (xususiy)">서당</span>은 고사하고 종이와 먹을 살 수도 없을 정도로 <span class="cn-word" data-pos="adj" data-tr="kambagʻal boʻlgan">가난했던</span> 석봉은 물을 <span class="cn-word" data-pos="verb" data-tr="botirib, tekkizib">찍어서</span> <span class="cn-word" data-tr="xum">항아리</span>나 돌 위에 글씨 쓰는 연습을 하였다. 이런 아들의 성공을 위해 어머니는 석봉을 유명한 절로 보내 공부를 시켰다.</p>
<p>절에 들어가 공부를 한 지 10년 쯤 지났을 무렵 석봉은 어머니가 매우 보고 싶었다. <span class="cn-word" data-pos="verb" data-tr="chidayolmay, toqat qilolmay">참다 못해</span> 밤에 <span class="cn-word" data-pos="adv" data-tr="yashirincha">몰래</span> 절에서 빠져 나온 그는 집으로 달려갔다. <span class="cn-word" data-pos="adv" data-tr="toʻsatdan, birdan">갑자기</span> 나타난 아들을 보고 <span class="cn-word" data-pos="verb" data-tr="hayron boʻlgan, choʻchigan">놀라는</span> 어머니에게 석봉은 말했다.</p>
<p>"십 년 동안 열심히 공부했습니다. 이제 제가 어머니를 <span class="cn-word" data-pos="adv" data-tr="bemalol, tinch">편히</span> <span class="cn-word" data-pos="verb" data-tr="boqaman, xizmat qilaman">모시겠습니다</span>. 어머니가 뵙고 싶어서 참을 수가 없었습니다."</p>
<p>그 말을 들은 어머니는 방 안의 <span class="cn-word" data-tr="moychiroq">호롱불</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻchirib">끄고</span> 말했다.</p>
<p>"나는 떡을 <span class="cn-word" data-pos="verb" data-tr="toʻgʻrayman, kesaman">썰</span> 테니 너는 글을 써라. 그래서 누구의 것이 더 <span class="cn-word" data-pos="adj" data-tr="tekis, bir xil">고른지</span> 한번 보자!"</p>
<p>말을 마친 어머니는 어둠 속에서도 <span class="cn-word" data-pos="adv" data-tr="tez">빠르게</span> 떡을 썰기 시작하였고 한석봉도 <span class="cn-word" data-pos="adv" data-tr="bosiqlik bilan, xotirjam">차분하게</span> 글씨를 써 내려갔다. 그렇게 얼마의 시간이 지난 후 불을 <span class="cn-word" data-pos="verb" data-tr="yoqib">켜고</span> 보니 어머니가 썬 떡은 크기나 두께가 모두 같았는데 석봉이 쓴 글씨는 서로 크기가 <span class="cn-word" data-pos="adj" data-tr="har xil, turlicha">제각각</span>이고 모양도 비뚤비뚤하였다. 십 년을 공부한 석봉이 몇 십 년간 떡을 썰어 온 어머니를 <span class="cn-word" data-pos="verb" data-tr="yutmoq, gʻolib chiqmoq">이길</span> 턱이 없었던 것이다. 이것을 본 어머니는 석봉을 크게 <span class="cn-word" data-pos="verb" data-tr="qattiq koyidi">꾸짖었다</span>.</p>
<p>"그런 글씨를 가지고 공부를 마쳤다니 말이 되느냐? <span class="cn-word" data-pos="adv" data-tr="hozir, shu zahoti">당장</span> 돌아가서 눈을 감고도 이 떡처럼 <span class="cn-word" data-pos="adv" data-tr="tekis">고르게</span> 글씨를 쓸 수 있게 될 때까지 열심히 연습하여라. 그전에는 <span class="cn-word" data-pos="adv" data-tr="aslo, hech qachon">절대로</span> 집에 올 생각을 하면 안 된다."</p>
<p>석봉은 다시 절로 돌아가 <span class="cn-word" data-pos="adv" data-tr="muntazam, tinimsiz">꾸준히</span> 공부에 <span class="cn-word" data-pos="verb" data-tr="jon kuydirdi, harakat qildi">힘썼다</span>. 그리고 훗날 <span class="cn-word" data-pos="adj" data-tr="aʼlo, yetuk">뛰어난</span> 명필가들의 <span class="cn-word" data-tr="xattotlik uslubi">필법</span>을 연구하여 본인만의 글씨체를 만들어냈다. 아들을 다시 절로 보내고 혼자 눈물을 훔칠지언정 자식 앞에서는 <span class="cn-word" data-pos="adj" data-tr="qattiqqoʻl">엄격했던</span> 석봉의 어머니. 그녀의 <span class="cn-word" data-pos="adj" data-tr="qattiqqoʻl, talabchan">엄한</span> 가르침이 석봉을 뛰어난 명필가로 만든 것이다.</p>''',
        "questions": [
            {
                "text": "어머니가 불을 끄고 떡을 썰자고 한 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "석봉의 공부가 아직 부족함을 스스로 깨닫게 하려고",
                    "떡을 더 많이 팔기 위해서",
                    "석봉과 놀아 주기 위해서",
                ],
                "answer": 0,
                "explanation": "Ona chiroqni oʻchirib, qorongʻida ttok kesish bilan xat yozishni solishtiradi — Sokbong oʻz mahorati hali yetarli emasligini oʻzi anglab yetishi uchun shunday qiladi.",
            },
            {
                "text": "이 이야기가 주는 교훈으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "부모님 말씀은 무조건 들어야 한다.",
                    "어떤 일이든 꾸준한 노력과 연습이 있어야 진정한 실력을 얻는다.",
                    "공부보다 돈을 버는 것이 더 중요하다.",
                ],
                "answer": 1,
                "explanation": "Sokbong onasining qattiqqoʻl talabidan keyin qaytib, muntazam mashq qilib buyuk xattot boʻladi — hikoya tinimsiz mehnat va mashq haqiqiy mahorat keltirishini uqtiradi.",
            },
            {
                "text": "불을 켜고 확인했을 때의 결과로 알맞은 것은 무엇입니까?",
                "choices": [
                    "석봉의 글씨가 어머니의 떡보다 더 고르고 반듯했다.",
                    "어머니의 떡은 크기가 고른데 석봉의 글씨는 제각각이었다.",
                    "둘 다 똑같이 훌륭했다.",
                ],
                "answer": 1,
                "explanation": "Matnda onasi kesgan ttok bir xil kattalikda boʻlgani, Sokbongning yozuvi esa har xil va qiyshiq boʻlgani aytilgan.",
            },
        ],
    },
    {
        "title":   "건강한 밥상 차리기",
        "summary": "Mavsumiy mahsulotlar, don-sabzavot va quvvatbaxsh taomlar — sogʻlom ovqatlanish sirlari.",
        "order":   12,
        "grammar": [
            {
                "pattern":  "-(으)ㄴ/는 데 반해",
                "meaning":  "...ligiga qaramay, aksincha (qarama-qarshilik).",
                "examples": ["과거에는 수단으로만 여겨졌던 데 반해 지금은 건강의 열쇠로 본다.", "형은 조용한 데 반해 동생은 활발해요."],
            },
            {
                "pattern":  "-(으)ㄴ 바 있다",
                "meaning":  "...gan holat/tajriba bor (rasmiy uslub).",
                "examples": ["실험에서 곡채식의 효능이 입증된 바 있다.", "저도 그곳에 가 본 바 있습니다."],
            },
            {
                "pattern":  "-(ㄴ/는)다손 치더라도",
                "meaning":  "Faraz qilaylik, ...ganda ham (baribir).",
                "examples": ["균형을 고려해 먹는다손 치더라도 부족한 영양소가 생긴다.", "돈이 많다손 치더라도 건강이 없으면 소용없어요."],
            },
            {
                "pattern":  "-(으)ㄹ수록",
                "meaning":  "...gani sari, ...gani sayin (mutanosib oʻzgarish).",
                "examples": ["육류 섭취량이 많을수록 질병률이 높았다.", "보면 볼수록 정이 들어요."],
            },
        ],
        "body": '''<p>우리의 건강을 <span class="cn-word" data-pos="verb" data-tr="saqlab turadigan">유지하는</span> 데 가장 중요한 역할을 하는 것은 바로 <span class="cn-word" data-tr="ovqatlanish tarzi">식생활</span>이다. 인간의 생명을 유지하고 발전시켜 나가는 것은 다름 아닌 음식이라고 할 수 있다. 이러한 음식이 과거에는 <span class="cn-word" data-pos="adv" data-tr="faqat, shunchaki">단지</span> 생명을 이어나가기 위한 수단으로만 <span class="cn-word" data-pos="verb" data-tr="hisoblangan, sanalgan">여겨졌던</span> 데 반해 요즘은 건강하고 <span class="cn-word" data-pos="adj" data-tr="farovon, moʻl">풍요로운</span> 삶의 열쇠라는 인식이 <span class="cn-word" data-pos="verb" data-tr="qaror topib, oʻrnashib">자리잡고</span> 있다. <span class="cn-word" data-pos="adv" data-tr="aslida, amalda">실제로</span> 건강에 좋다는 <span class="cn-word" data-tr="organik">유기농</span> 식품을 비롯해 특정 질병의 <span class="cn-word" data-tr="oldini olish">예방</span>과 치료에 효과가 있다는 식품을 <span class="cn-word" data-pos="verb" data-tr="gʻamlab, eʼtibor berib">챙겨</span> 먹는 데에 적지 않은 돈과 시간을 투자하는 사람들을 주변에서 <span class="cn-word" data-pos="adv" data-tr="oson">쉽게</span> 볼 수 있다. 하지만 큰돈과 많은 시간을 들이지 않고도 얼마든지 건강한 식생활을 할 수 있다. 그렇다면 어떤 음식들로 건강한 밥상을 <span class="cn-word" data-pos="verb" data-tr="tayyorlash, tuzash">차려야</span> 할까?</p>
<p>첫째, <span class="cn-word" data-tr="mavsumiy mahsulot">제철 식품</span>이 좋다. 제철 식품이란 계절에 따라 많이 나오는 식품으로, <span class="cn-word" data-tr="yetishtirish">재배</span>에 <span class="cn-word" data-pos="adj" data-tr="maxsus, alohida">특별한</span> 시설이 필요하지 않아 값이 쌀 뿐만 아니라 맛과 향이 좋다. 또한 <span class="cn-word" data-pos="adj" data-tr="boy, serob">풍부한</span> <span class="cn-word" data-tr="oziq moddalar">영양소</span>를 담고 있는데, <span class="cn-word" data-pos="adj" data-tr="yorqin, tirik">생생한</span> 태양 에너지를 받고 자란 제철 식품은 우리 몸속으로 에너지를 <span class="cn-word" data-pos="adv" data-tr="tez, shiddat bilan">쏙쏙</span> 넣어 주는 역할을 한다. 요즘은 제철 식품이 따로 없다고 하지만 비닐하우스에서 짧은 기간 재배한 과일이나 채소는 햇빛을 <span class="cn-word" data-pos="adv" data-tr="yetarlicha">충분히</span> 받지 못해 영양소의 <span class="cn-word" data-tr="miqdori">함량</span>이 <span class="cn-word" data-pos="adj" data-tr="yetishmaydi, kam">부족하다</span>. 그러므로 제때에 생산되는 식품을 <span class="cn-word" data-pos="adj" data-tr="yangi, tetik">신선한</span> 상태로 먹는 것이 가장 좋다.</p>
<p>둘째, 곡채식 위주의 식사가 좋다. 현대인의 <span class="cn-word" data-tr="turmush tarzi kasalliklari">성인병</span>은 <span class="cn-word" data-pos="adv" data-tr="koʻpincha, aksariyat">대부분</span> <span class="cn-word" data-tr="goʻsht mahsulotlari">육류</span> 위주의 식습관에서 <span class="cn-word" data-pos="verb" data-tr="kelib chiqqan">비롯되었으며</span>, 또한 이러한 질병을 곡식과 채식만으로 치료했다는 보도들을 쉽게 접할 수 있다. 실제로 쥐를 대상으로 한 실험에서도 곡채식의 효능이 <span class="cn-word" data-pos="verb" data-tr="isbotlangan">입증된</span> 바 있다. 곡채식 사료를 준 그룹, 곡채식과 육류를 <span class="cn-word" data-pos="verb" data-tr="aralashtirib">섞어</span> 준 그룹, 육류만을 준 그룹의 쥐들을 해부한 결과, 곡채식 사료를 <span class="cn-word" data-pos="verb" data-tr="isteʼmol qilgan">섭취한</span> 그룹에서는 질병이 <span class="cn-word" data-pos="verb" data-tr="aniqlanmagan, topilmagan">발견되지</span> 않은 데 반해 육류 섭취량이 많을수록 높은 질병률을 보인 것으로 <span class="cn-word" data-pos="verb" data-tr="maʼlum boʻldi, koʻrindi">나타났다</span>. 이는 곡채식이 얼마나 중요한지를 보여 주는 예이다.</p>
<p>셋째, <span class="cn-word" data-tr="quvvatlantiruvchi taom">보양식</span>을 잘 선택해서 먹는 것이 좋다. 보양식이란 우리 몸에 <span class="cn-word" data-pos="adj" data-tr="yetishmaydigan, kam">부족한</span> 영양소와 기운을 <span class="cn-word" data-pos="verb" data-tr="toʻldirib beradigan">보충해</span> 주는 음식으로 연령과 성별, 그리고 <span class="cn-word" data-tr="organizm tuzilishi, mijoz">체질</span>, 계절 등에 따른 다양한 음식이 있다. <span class="cn-word" data-tr="yangi tuqqan ona">산모</span>에게는 호박, 잉어 등이 부기를 빼 주고 <span class="cn-word" data-pos="verb" data-tr="zaiflashgan">약해진</span> 몸을 건강하게 해 주며, 운동선수에게는 장어, 흑염소 등이 체력을 <span class="cn-word" data-pos="verb" data-tr="mustahkamlaydigan, kuchaytiradigan">보강해</span> 준다. 우리가 아무리 영양의 균형을 고려해서 음식을 섭취한다손 치더라도 바쁜 일상에 <span class="cn-word" data-pos="verb" data-tr="band boʻlib, ketidan quvilib">쫓기다</span> 보면 부족한 영양소가 생기게 마련이다. 이럴 때 특정 영양소를 보충해 주는 보양식을 먹는 것이 건강을 유지하는 데 도움을 줄 수 있다.</p>
<p><span class="cn-word" data-pos="adv" data-tr="borgan sari">갈수록</span> 사람들의 평균 수명이 늘고 있는 요즘 이제 <span class="cn-word" data-pos="adv" data-tr="shunchaki, oddiygina">단순히</span> 오래 사는 것을 넘어 건강한 삶이 많은 사람들의 관심사가 되고 있다. 건강한 삶을 위해서는 지금부터라도 바른 식생활의 중요성을 <span class="cn-word" data-pos="verb" data-tr="anglab, tushunib">깨닫고</span> 생활 속에서 <span class="cn-word" data-pos="verb" data-tr="amalga oshirmoq, tatbiq qilmoq">실천해야</span> 할 것이다. 하루도 <span class="cn-word" data-pos="adv" data-tr="qoldirmay, hech tashlamay">빠짐없이</span> 먹는 음식보다 중요한 것이 또 어디 있겠는가.</p>''',
        "questions": [
            {
                "text": "이 글에서 건강한 밥상을 차리는 방법으로 제시하지 않은 것은 무엇입니까?",
                "choices": [
                    "제철 식품을 먹는 것",
                    "곡채식 위주로 먹는 것",
                    "값비싼 수입 식품만 먹는 것",
                ],
                "answer": 2,
                "explanation": "Matnda uchta usul berilgan: mavsumiy mahsulot, don-sabzavot asosidagi ovqat va quvvatbaxsh taom (보양식). Qimmat import mahsulotlarnigina yeyish tavsiya qilinmagan; aksincha katta pul sarflamasdan sogʻlom ovqatlanish mumkinligi aytilgan.",
            },
            {
                "text": "쥐 실험 결과가 보여 주는 것으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "육류를 많이 먹을수록 질병률이 높아졌다.",
                    "곡채식만 먹은 쥐가 가장 빨리 죽었다.",
                    "사료의 종류는 건강과 관계가 없었다.",
                ],
                "answer": 0,
                "explanation": "Tajribada don-sabzavot yegan guruhda kasallik topilmagan, goʻsht isteʼmoli koʻp boʻlgan sari kasallik darajasi yuqori boʻlgan — bu don-sabzavot ovqatining muhimligini koʻrsatadi.",
            },
            {
                "text": "'보양식'에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "몸에 부족한 영양소와 기운을 보충해 주는 음식",
                    "살을 빼기 위해 먹는 음식",
                    "오직 운동선수만 먹는 음식",
                ],
                "answer": 0,
                "explanation": "Matnda boyangshik \"몸에 부족한 영양소와 기운을 보충해 주는 음식\" deb taʼriflangan; yosh, jins, mijoz va faslga qarab turlicha boʻladi — faqat sportchilar uchun emas.",
            },
        ],
    },
    {
        "title":   "달라진 젊은 세대의 직업관",
        "summary": "Pul emas — boʻsh vaqt, moyillik va maqsad: yoshlarning yangi kasb qarashlari.",
        "order":   13,
        "grammar": [
            {
                "pattern":  "-는 대신(에)",
                "meaning":  "... oʻrniga (almashtirish yoki muqobil).",
                "examples": ["생계 수단으로서의 의미가 약해지는 대신 자아실현의 의미가 커진다.", "밥을 먹는 대신 빵을 먹었어요."],
            },
            {
                "pattern":  "-다고 해도 과언이 아니다",
                "meaning":  "...desa ham mubolagʻa boʻlmaydi (taʼkid).",
                "examples": ["잘 쉬기 위해 일한다고 해도 과언이 아니다.", "그가 최고라고 해도 과언이 아니에요."],
            },
            {
                "pattern":  "-에 의하면",
                "meaning":  "...ga koʻra, ...ga asosan (manbaga tayanish).",
                "examples": ["설문 조사 결과에 의하면 적성을 중시하는 사람이 많았다.", "뉴스에 의하면 내일 눈이 온대요."],
            },
            {
                "pattern":  "-고자 하다",
                "meaning":  "...ishni koʻzlamoq, ...moqchi boʻlmoq (rasmiy niyat).",
                "examples": ["전문 기술을 배워 기술자가 되고자 한다.", "저는 의사가 되고자 합니다."],
            },
        ],
        "body": '''<p>현대 사회에서는 <span class="cn-word" data-tr="tirikchilik">생계유지</span>를 위한 수단으로서의 직업 또는 사회적 위상으로서의 직업은 그 의미가 <span class="cn-word" data-pos="adv" data-tr="asta-sekin, tobora">점점</span> <span class="cn-word" data-pos="verb" data-tr="susayadigan, zaiflashadigan">약해지는</span> 대신 <span class="cn-word" data-tr="oʻzini roʻyobga chiqarish">자아실현</span>의 장으로서의 직업의 의미가 <span class="cn-word" data-pos="verb" data-tr="birinchi oʻringa chiqmoqda">부각되고</span> 있다. 여기에는 여러 가지 사회 경제적 요인이 <span class="cn-word" data-pos="verb" data-tr="taʼsir qiladi">작용한다</span>. 기성세대에 비해 생활이 <span class="cn-word" data-pos="adj" data-tr="farovonlashgan">풍족해진</span> 것, 직업의 종류가 <span class="cn-word" data-pos="verb" data-tr="xilma-xil boʻlgan">다양해진</span> 것, '평생 직장' 대신 '평생 직업'의 개념이 <span class="cn-word" data-pos="verb" data-tr="qaror topgan, oʻrnashgan">자리 잡은</span> 것이 그 요인이다. 요즘 젊은 세대들은 아버지 세대와 다른 직업관을 가지고 있는데, 그것은 다음과 같은 특징을 보인다.</p>
<p>첫째, 요즘 젊은이들은 개인의 <span class="cn-word" data-tr="boʻsh vaqt, hordiq">여가</span> 활동을 <span class="cn-word" data-pos="verb" data-tr="muhim sanaydi">중시한다</span>. 이들은 직장을 선택할 때 월급이 좀 <span class="cn-word" data-pos="adj" data-tr="kam boʻlsa ham">적더라도</span> 가족과 함께 보내거나 <span class="cn-word" data-tr="oʻz ustida ishlash">자기 계발</span>, 취미 활동 등을 할 수 있는 시간이 <span class="cn-word" data-pos="adj" data-tr="yetarlimi">충분한가</span>를 중요하게 <span class="cn-word" data-pos="verb" data-tr="hisoblaydi, sanaydi">여긴다</span>. 부모님 세대가 먹고 살기 위해 쉬는 날 없이 일을 했다면 이들은 잘 쉬기 위해서 일을 한다고 해도 과언이 아니다.</p>
<p>둘째, 이들도 윤리적인 만족감을 <span class="cn-word" data-pos="verb" data-tr="intiladi, koʻzlaydi">추구한다</span>. 다시 말해 자신이 하고 있는 일이 다른 직업에 비해 수입이 적고 사회적 지위가 <span class="cn-word" data-pos="adj" data-tr="past boʻlsa ham">낮다고</span> 하더라도 자신의 직업에 <span class="cn-word" data-tr="faxr, gʻurur">긍지</span>를 가지고 <span class="cn-word" data-pos="adv" data-tr="halol, vijdonan">성실하게</span> 일한다. 사회 복지사가 저소득층이나 장애인들을 위해 <span class="cn-word" data-pos="verb" data-tr="fidoyilarcha xizmat qiladigan">헌신하는</span> 것이라든가 소방관이 목숨을 걸고 사람을 구하는 것, 공무원이 봉사의 정신으로 공직생활을 하는 것 등이 모두 여기에 <span class="cn-word" data-pos="verb" data-tr="tegishli, kiradi">속한다</span>고 할 수 있다.</p>
<p>셋째, <span class="cn-word" data-tr="moyillik, layoqat">적성</span>을 중요하게 생각하는 것도 요즘 젊은이들의 특성 중의 하나이다. 그들은 기성세대에 비해 경제적으로 풍족한 시기에 <span class="cn-word" data-pos="verb" data-tr="oʻsib, ulgʻayib">성장해서</span> 그런지 단순히 대우가 좋은 직업보다 하고 싶거나 잘할 수 있는 일을 하려는 성향이 <span class="cn-word" data-pos="adj" data-tr="kuchli">강하다</span>. 얼마 전 한 게임 회사에서 <span class="cn-word" data-pos="verb" data-tr="oʻtkazgan">실시한</span> 설문 조사 결과에 의하면 구직 시 가장 중요하게 생각하는 것을 묻는 질문에 '적성'이라고 대답한 사람이 49%를 <span class="cn-word" data-pos="verb" data-tr="egalladi, tashkil qildi">차지했다</span>. 하고 싶은 일을 하면서 <span class="cn-word" data-tr="yutuq, muvaffaqiyat hissi">성취감</span>과 만족감을 얻으려고 하는 젊은이들의 직업관이 <span class="cn-word" data-pos="verb" data-tr="aks etgan">반영된</span> 결과라고 볼 수 있다.</p>
<p>마지막으로 들 수 있는 것은 목표 지향적 특성이다. 다시 말해 자기가 하고자 하는 일을 위해서 남의 시선을 <span class="cn-word" data-pos="verb" data-tr="eʼtibor bermay">의식하지</span> 않고 노력하는 것이다. 대학 진학 대신 마이스터 고등학교를 선택한 학생들은 <span class="cn-word" data-pos="adj" data-tr="professional, kasbiy">전문적인</span> 기술을 배워 기술자가 되고자 한다. 이들은 기술직에 대한 과거의 <span class="cn-word" data-tr="notoʻgʻri, noxolis qarash">편견</span>을 <span class="cn-word" data-pos="verb" data-tr="buzib, sindirib">깨고</span> <span class="cn-word" data-tr="diplom obroʻsi, oʻqigan joyi">학벌</span>보다는 실력으로 평가받으려는 것이다. 대기업이나 은행에서 고졸 출신자들을 <span class="cn-word" data-pos="verb" data-tr="ishga olmoq">채용하려는</span> 분위기가 <span class="cn-word" data-pos="verb" data-tr="yoyilmoqda, kengaymoqda">확산되고</span> 있는 것도 이러한 현상에 한몫한다. 파일럿이나 군인, 경찰 등 남성들의 영역으로만 여겨졌던 직업 세계에 도전장을 <span class="cn-word" data-pos="verb" data-tr="tashlagan, ilgari surgan">내민</span> 여성들도 바로 목표 지향적인 사람이라고 할 수 있다.</p>
<p>돈보다는 여가와 적성, 목표를 중시하며 일을 통해 윤리적인 만족감을 얻고자 하는 요즘 젊은 세대들의 직업관은 직업이 단순히 경제적인 만족을 넘어 개인의 자아실현과 사회적 차원의 공동 목표를 <span class="cn-word" data-pos="verb" data-tr="erishadigan, amalga oshiradigan">달성하는</span> 수단으로 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmoqda">변화하고</span> 있다.</p>''',
        "questions": [
            {
                "text": "이 글에서 말하는 요즘 젊은 세대의 직업관 특징이 아닌 것은 무엇입니까?",
                "choices": [
                    "여가를 중시한다.",
                    "오직 높은 월급만을 최고로 여긴다.",
                    "적성과 목표를 중요하게 생각한다.",
                ],
                "answer": 1,
                "explanation": "Matnda yoshlar boʻsh vaqt, axloqiy qoniqish, moyillik va maqsadni muhim sanashi aytilgan. Aksincha, ular \"월급이 좀 적더라도\" boshqa narsalarni afzal koʻrishadi — faqat yuqori maoshni ustun qoʻyish ularning qarashi emas.",
            },
            {
                "text": "젊은이들이 여가를 중시한다는 것을 가장 잘 보여 주는 문장은 무엇입니까?",
                "choices": [
                    "부모 세대는 먹고 살기 위해 쉬는 날 없이 일했지만, 이들은 잘 쉬기 위해 일한다.",
                    "이들은 월급이 많은 직업만 선택한다.",
                    "이들은 절대 취미 활동을 하지 않는다.",
                ],
                "answer": 0,
                "explanation": "Matnda \"부모님 세대가 먹고 살기 위해 일했다면 이들은 잘 쉬기 위해서 일을 한다\" deyilgan — bu boʻsh vaqtni qadrlashning yaqqol ifodasi.",
            },
            {
                "text": "마이스터 고등학교를 선택한 학생들에게서 볼 수 있는 직업관은 무엇입니까?",
                "choices": [
                    "학벌보다 실력으로 평가받으려는 목표 지향적 태도",
                    "남의 시선을 가장 중요하게 여기는 태도",
                    "되도록 쉬운 일만 하려는 태도",
                ],
                "answer": 0,
                "explanation": "Matnda bu oʻquvchilar kasbiy koʻnikma oʻrganib, diplom obroʻsidan koʻra bilim-mahorat bilan baholanishni istashi — maqsadga yoʻnaltirilgan qarash misoli sifatida keltirilgan.",
            },
        ],
    },
    {
        "title":   "마트에 숨어 있는 판매 전략",
        "summary": "Nega marketdan doim ortiqcha narsa sotib olamiz? Yashirin savdo usullari.",
        "order":   14,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 겸",
                "meaning":  "Bir yoʻla ...ni ham koʻzlab (ikki maqsad).",
                "examples": ["사은품도 챙길 겸 지갑을 열었다.", "운동도 할 겸 걸어서 왔어요."],
            },
            {
                "pattern":  "-는가 하면",
                "meaning":  "Baʼzan shunday, baʼzan esa boshqacha (qiyoslash).",
                "examples": ["판매율을 높이는가 하면 구매를 유도하기도 한다.", "웃는가 하면 갑자기 울기도 해요."],
            },
            {
                "pattern":  "-(으)ㄹ 때마다",
                "meaning":  "Har gal ...ganda (takror).",
                "examples": ["식품 매장에 들어설 때마다 상품이 많아 보인다.", "그를 볼 때마다 기분이 좋아져요."],
            },
            {
                "pattern":  "-도록",
                "meaning":  "... boʻlishi uchun, ...adigan qilib (maqsad).",
                "examples": ["쇼핑에 몰입하도록 창문과 시계를 두지 않는다.", "늦지 않도록 일찍 출발했어요."],
            },
        ],
        "body": '''<p>쇼핑하러 대형 마트에 갔다가 계획에도 없던 물건을 구입한 경험, 누구나 한 두 번은 있을 것이다. 꼭 필요한 물건은 아니었지만 <span class="cn-word" data-tr="qoʻshimcha sovgʻa (xariddan)">사은품</span>도 <span class="cn-word" data-pos="verb" data-tr="olmoq, gʻamlamoq">챙길</span> 겸 지갑을 열었다면 당신은 마트의 '판매 <span class="cn-word" data-tr="strategiya">전략</span>'에 <span class="cn-word" data-pos="adv" data-tr="roppa-rosa, aynan">딱</span> <span class="cn-word" data-pos="verb" data-tr="tuzoqqa tushdi, ilindi">걸려들었다</span>고 할 수 있다. 물건을 고르는 동안 <span class="cn-word" data-pos="adv" data-tr="beixtiyor">무심코</span> <span class="cn-word" data-pos="verb" data-tr="oʻtib ketadigan">지나치게</span> 되는 매장의 내부, 알고 보면 그곳에는 소비자의 지갑을 열기 위한 <span class="cn-word" data-pos="adj" data-tr="puxta oʻylangan">치밀한</span> 전략이 <span class="cn-word" data-pos="adv" data-tr="har yerda, joy-joyda">곳곳에</span> <span class="cn-word" data-pos="verb" data-tr="yashiringan">숨어</span> 있다.</p>
<p>방배동에 사는 김미화 씨(30세, 주부)는 OO마트의 식품 매장에 들어설 때마다 다른 매장보다 더 많은 종류의 상품이 있는 것 같은 느낌을 받는다. 과일도 종류가 다른 곳보다 더 많고 가격도 <span class="cn-word" data-pos="adv" data-tr="ancha, bir muncha">훨씬</span> <span class="cn-word" data-pos="adv" data-tr="arzon">저렴하게</span> 느껴진다. <span class="cn-word" data-pos="adv" data-tr="aslida, aslini olganda">막상</span> 따져보면 1~2개 정도 차이인데 이처럼 느끼는 이유는 바로 상품의 <span class="cn-word" data-tr="terib qoʻyish, vitrina">진열</span> 방식 때문이다. 과일 매장의 경우 상품의 저렴함을 <span class="cn-word" data-pos="verb" data-tr="taʼkidlab">강조하고</span> <span class="cn-word" data-pos="adv" data-tr="moʻl-koʻl">풍성하게</span> 보이도록 하기 위해 여러 과일을 <span class="cn-word" data-pos="verb" data-tr="uyib, taxlab">쌓아</span> 두고 판매한다. 또한 앞쪽에 비싼 상품을 진열해 뒤쪽 상품이 <span class="cn-word" data-pos="adv" data-tr="nisbatan">상대적으로</span> 저렴하게 느껴지게 해서 판매율을 더 높이는가 하면 사람의 시선이 <span class="cn-word" data-pos="adv" data-tr="instinktiv, tabiiy ravishda">본능적으로</span> 좌우를 살피는 특징이 있다는 사실을 이용해서 같은 종류의 상품은 수직으로 진열해 구매를 <span class="cn-word" data-pos="verb" data-tr="undaydi, yoʻnaltiradi">유도한다</span>.</p>
<p>또 다른 판매 전략으로 매장의 구조를 이용하는 방법이 있다. 위층으로 손님들을 <span class="cn-word" data-pos="verb" data-tr="koʻchirish, harakatlantirish">이동시키기</span> 위해 1층에는 화장실을 두지 않고, <span class="cn-word" data-pos="adj" data-tr="shoshmasdan, xotirjam">느긋한</span> 마음으로 쇼핑에 <span class="cn-word" data-pos="verb" data-tr="berilib ketishi uchun">몰입하도록</span> 하기 위해 창문과 시계를 <span class="cn-word" data-pos="verb" data-tr="oʻrnatmaslik">설치하지</span> 않는다. 매장 곳곳에 <span class="cn-word" data-pos="verb" data-tr="oʻrnatilgan">설치된</span> 유리나 거울은 소비자들의 발걸음을 <span class="cn-word" data-pos="verb" data-tr="sekinlashtiradigan">늦추는</span> 효과가 있다. 엘리베이터는 구석에, 에스컬레이터는 중앙에 설치한다. 엘리베이터로 <span class="cn-word" data-pos="adv" data-tr="bir zumda, biratoʻla">단번에</span> 목적지까지 가는 것보다 에스컬레이터를 타고 다양한 매장을 <span class="cn-word" data-pos="verb" data-tr="oʻtib, kesib">거쳐</span> 가게 하는 것이 구매를 유도할 수 있는 방법이기 때문이다.</p>
<p>이에 더해 최근에는 <span class="cn-word" data-tr="ishonch">신뢰</span> 마케팅, 정보 제공 마케팅 등 새로운 방식의 마케팅이 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">등장했다</span>. 판매대 광고판에 '산지 직거래, 계약 재배' 등의 <span class="cn-word" data-tr="yozuv, ibora">문구</span>를 넣거나 생산지, 생산자 사진, <span class="cn-word" data-tr="kelib chiqish maʼlumoti">이력</span> 등을 <span class="cn-word" data-pos="verb" data-tr="yozib qoʻyadigan, belgilaydigan">표기하는</span> 경우들은 <span class="cn-word" data-pos="adv" data-tr="keng">널리</span> 이용되는 신뢰 마케팅 방법이다. 유명 인사 및 연예인들을 상품 광고에 <span class="cn-word" data-pos="verb" data-tr="oldinga chiqarish, jalb qilish">내세우는</span> 것도 신뢰 마케팅의 한 방법이다.</p>
<p>그리고 특정 제품을 <span class="cn-word" data-pos="adv" data-tr="bevosita, toʻgʻridan-toʻgʻri">직접</span> 홍보하기보다 상품과 관련 있는 다양한 정보를 <span class="cn-word" data-pos="verb" data-tr="taqdim etib, berib">제공해</span> 간접 홍보의 효과를 얻기도 한다. 요리법이나 건강 유지법 등을 소개해 <span class="cn-word" data-pos="adv" data-tr="tabiiy ravishda">자연스럽게</span> 상품을 <span class="cn-word" data-pos="verb" data-tr="koʻrsatadigan, namoyish qiladigan">노출시키는</span> 방식이다. 얼마 전 OO 마트의 카레 코너 앞은 '다양한 카레 요리법'이라는 제목의 안내문을 읽는 사람들로 <span class="cn-word" data-pos="verb" data-tr="gavjum boʻldi, tirband boʻldi">북적거렸다</span>. 한 주부는 카레 말고도 요리에 필요한 다른 재료도 함께 구입했다. 정보 제공 마케팅은 해당 상품은 물론 관련 상품 <span class="cn-word" data-tr="savdo tushumi">매출</span> 신장에도 영향을 준다.</p>
<p>이처럼 기존의 마케팅 전략이 <span class="cn-word" data-pos="adv" data-tr="faqat, shunchaki">단지</span> 인간의 심리나 행동을 <span class="cn-word" data-pos="verb" data-tr="tahlil qilib">분석해</span> 판매에 이용하는 것이었다면 이제는 거기에다 상품의 품질에 대한 신뢰를 <span class="cn-word" data-pos="adv" data-tr="yanada">더욱</span> <span class="cn-word" data-pos="verb" data-tr="birinchi oʻringa chiqaradigan">부각시키는</span> 마케팅으로 <span class="cn-word" data-pos="verb" data-tr="takomillashmoqda">진화하고</span> 있다. 상품의 품질로 자신 있게 승부를 거는 것이다. 우리가 <span class="cn-word" data-pos="adv" data-tr="odatda, kunda">평소</span> <span class="cn-word" data-pos="verb" data-tr="sezmoq, payqamoq">눈치채지</span> 못했던 다양한 마케팅 방식, 지금 이 순간에도 대형 마트들의 판매 전략 연구는 계속되고 있다.</p>''',
        "questions": [
            {
                "text": "이 글의 주제로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "대형 마트의 물건이 항상 가장 싸다는 것",
                    "대형 마트에는 소비자의 구매를 유도하는 다양한 판매 전략이 숨어 있다는 것",
                    "마트에서 쇼핑을 하면 안 된다는 것",
                ],
                "answer": 1,
                "explanation": "Matn butunligicha marketlarning xaridni ragʻbatlantiruvchi yashirin savdo strategiyalarini (terib qoʻyish, bino tuzilishi, marketing) tushuntiradi — bu asosiy mavzu.",
            },
            {
                "text": "마트에서 창문과 시계를 설치하지 않는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "손님이 시간을 잊고 느긋하게 쇼핑에 몰입하도록 하기 위해",
                    "전기를 아끼기 위해",
                    "건물을 짓는 비용을 줄이기 위해",
                ],
                "answer": 0,
                "explanation": "Matnda deraza va soat qoʻyilmasligi mijoz vaqtni unutib, xotirjam holda xaridga berilib ketishi uchun ekani aytilgan.",
            },
            {
                "text": "앞쪽에 비싼 상품을 진열하는 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "비싼 상품을 먼저 팔기 위해",
                    "뒤쪽 상품이 상대적으로 저렴하게 느껴지도록 하기 위해",
                    "매장을 예쁘게 꾸미기 위해",
                ],
                "answer": 1,
                "explanation": "Matnda oldingi tomonga qimmat mahsulot terib qoʻyilsa, orqadagi mahsulot nisbatan arzonroq tuyulishi va shu bilan sotuv oshishi aytilgan.",
            },
        ],
    },
]
