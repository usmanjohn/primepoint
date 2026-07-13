# Keimyung Korean Readings — stories 1–7 (real textbook passages from keimyung_21_story.txt).
# Import: python manage.py import_corner corner/management/commands/_stories_keimyung_1_7.py --author=<AUTHOR>

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
        "title":   "케이팝이 바꾼 내 인생",
        "summary": "Fransiyalik qiz K-pop va doramalar tufayli Koreyaga kelib, koreys tilini oʻrganishga bel bogʻlaydi.",
        "order":   1,
        "grammar": [
            {
                "pattern":  "-길래",
                "meaning":  "Ogʻzaki sabab/asos: biror narsani koʻrib yoki eshitib, shunga asoslanib ish qildim.",
                "examples": ["춤이 멋지길래 따라 추기 시작했다.", "날씨가 좋길래 산책을 나갔어요."],
            },
            {
                "pattern":  "-게 되다",
                "meaning":  "Oʻz ixtiyorimdan tashqari, natijada shunday boʻlib qoldi (holat oʻzgarishi).",
                "examples": ["한국에 관심을 가지게 되었다.", "결국 그 콘서트에 가게 되었어요."],
            },
            {
                "pattern":  "-(으)ㄹ 줄 알다/모르다",
                "meaning":  "...ishni bilmoq/uddalay olmoq yoki ...deb (notoʻgʻri) oʻylamoq.",
                "examples": ["그렇게 인기를 얻을 줄 몰랐어요.", "한국 사람 모두 예쁜 줄 알았어요."],
            },
            {
                "pattern":  "-았/었더라면",
                "meaning":  "Oʻtmishdagi afsus: ...ganimda edi (natija boshqacha boʻlardi).",
                "examples": ["진작 알았더라면 미리 배웠을 텐데.", "일찍 시작했더라면 좋았을 걸 그랬다."],
            },
        ],
        "body": '''<p>"다 거짓말이야 몰랐어 이제야 알았어 네가 필요해・・・・・・알았어"</p>
<p>이것은 제가 제일 좋아하는 한국 가수 빅뱅의 노래입니다. 제가 처음 이 노래를 들었을 때는 무슨 뜻인지조차 <span class="cn-word" data-pos="verb" data-tr="bilmadim">몰랐습니다</span>. <span class="cn-word" data-pos="adv" data-tr="shunchaki">그저</span> <span class="cn-word" data-tr="qoʻshiq matni">가사</span>와 멜로디가 따라 부르기 <span class="cn-word" data-pos="adj" data-tr="oson">쉽고</span>, 단체로 나와서 추는 춤도 <span class="cn-word" data-pos="adj" data-tr="zoʻr, ajoyib">멋지길래</span> 친구들과 같이 따라 부르기 <span class="cn-word" data-pos="verb" data-tr="boshladim">시작했습니다</span>.</p>
<p>그러다가 빅뱅 뿐만 아니라 샤이니, 슈퍼주니어, 소녀시대와 같은 다른 한국 가수들의 노래에도 <span class="cn-word" data-tr="qiziqish">관심</span>을 가지게 되었고 <span class="cn-word" data-pos="adv" data-tr="nihoyat">마침내</span> 제 고향 프랑스에서 <span class="cn-word" data-pos="verb" data-tr="oʻtkazilgan">열린</span> 케이팝 콘서트에도 가게 되었습니다. 거기에서 저는 한손에는 태극기, 다른 손에는 한글이 적힌 플래카드를 들고 <span class="cn-word" data-pos="adv" data-tr="zavq bilan, quvnoq">신나게</span> 노래를 따라 불렀습니다. 그날 이후 멋진 외모에 <span class="cn-word" data-pos="adj" data-tr="ajoyib, yetuk">뛰어난</span> 가창력, 춤 실력까지 <span class="cn-word" data-pos="adv" data-tr="har tomonlama">두루</span> <span class="cn-word" data-pos="verb" data-tr="ega boʻlgan">갖춘</span> 한국 가수들의 <span class="cn-word" data-tr="joziba, maftunkorlik">매력</span>에 <span class="cn-word" data-pos="adv" data-tr="beixtiyor">그만</span> <span class="cn-word" data-pos="adv" data-tr="butunlay berilib">푹</span> <span class="cn-word" data-pos="verb" data-tr="mahliyo boʻldim">빠져</span> 버렸고 지금까지 빠져나오지 못하고 있습니다.</p>
<p>지금 유럽에서는 한국 드라마도 한국 가요 <span class="cn-word" data-pos="adv" data-tr="kam boʻlmagan holda">못지않게</span> 많은 인기를 <span class="cn-word" data-pos="verb" data-tr="qozonmoq, erishmoq">얻고</span> 있습니다. 제가 SNS를 통해서 처음 본 한국 드라마는 '풀하우스'인데 가수 비와 여배우 송혜교가 한 집에 살면서 티격태격하다가 <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">결국</span> 사랑하게 된다는 내용입니다. <span class="cn-word" data-tr="syujet, mazmun">줄거리</span>도 <span class="cn-word" data-pos="adv" data-tr="albatta">물론</span> 재미있었지만 나오는 배우들이 <span class="cn-word" data-pos="adv" data-tr="shu qadar">어찌나</span> <span class="cn-word" data-pos="adj" data-tr="chiroyli">예쁘고</span> <span class="cn-word" data-pos="adj" data-tr="kelishgan">잘생겼는지</span> 저는 한국에 오기 전까지 한국 사람들은 모두 다 드라마에 나오는 주인공들처럼 생긴 줄 알았습니다.</p>
<p>한국 가요와 드라마가 좋아서 한국에 관심을 가지게 된 저는 6개월 전에 한국에 왔습니다. 처음 왔을 때는 <span class="cn-word" data-pos="adj" data-tr="notanish, begona">낯설게</span>만 느껴지던 한국말과 한국 음식에 이젠 <span class="cn-word" data-pos="adv" data-tr="ancha, anchagina">제법</span> <span class="cn-word" data-pos="verb" data-tr="koʻnikib qoldim">익숙해졌습니다</span>. 그리고 한국 사람들처럼 옷을 입고 이야기하고 화장하는 법까지 배우면서 한국 문화에 더 <span class="cn-word" data-pos="adv" data-tr="yaqinroq">가까이</span> <span class="cn-word" data-pos="verb" data-tr="yaqinlashmoq">다가갈</span> 수 있었습니다. 이런 저를 프랑스에 있는 친구들은 <span class="cn-word" data-pos="adv" data-tr="juda">아주</span> <span class="cn-word" data-pos="verb" data-tr="havas qiladi">부러워합니다</span>. 자기가 좋아하는 한국 노래가 무슨 뜻인지 가르쳐 달라고 하고, 한국 가수의 시디를 사서 고향으로 보내 달라는 친구도 있습니다. 어떤 친구는 한국 화장품을 부탁하기도 합니다. 제가 친구들에게 이렇게 인기를 얻을 줄 알았더라면 <span class="cn-word" data-pos="adv" data-tr="avvalroq, oldinroq">진작</span> 한국어를 배울 걸 그랬다는 <span class="cn-word" data-tr="afsus, pushaymon">후회</span>도 생깁니다.</p>
<p>저는 한국에 관심이 많은 제 친구들에게 한국어를 가르쳐 주고 싶습니다. 그래서 한국어를 더 <span class="cn-word" data-pos="adv" data-tr="tirishib, astoydil">열심히</span> 공부해야 합니다. 한국어 <span class="cn-word" data-tr="mahorat, saviya">실력</span>이 <span class="cn-word" data-pos="verb" data-tr="oshsa, yaxshilansa">늘면</span> 친구들을 가르쳐줄 수 있을 뿐만 아니라 제가 좋아하는 한국 노래와 드라마를 더 잘 <span class="cn-word" data-pos="verb" data-tr="tushunmoq">이해할</span> 수 있을 테니까요. 그리고 한국 친구도 많이 <span class="cn-word" data-pos="verb" data-tr="doʻst orttirmoq">사귀고</span> 한국의 이곳저곳을 여행하고 싶습니다. 여행 사진을 SNS에 올리면 <span class="cn-word" data-pos="adv" data-tr="ehtimol">아마</span> 많은 친구들이 배 아파할 거예요. 제 친구들에게도 한국에 올 수 있는 <span class="cn-word" data-tr="imkoniyat">기회</span>가 생겼으면 좋겠습니다.</p>''',
        "questions": [
            {
                "text": "이 글을 쓴 사람에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "한국에서 태어나 프랑스로 유학을 갔다.",
                    "케이팝과 드라마를 좋아하다가 한국에 오게 되었다.",
                    "한국 친구의 소개로 한국어를 배우기 시작했다.",
                ],
                "answer": 1,
                "explanation": "Muallif — fransiyalik qiz. U avval K-pop qoʻshiqlari va dramalarni yoqtirgan, keyin \"한국에 관심을 가지게 된 저는 6개월 전에 한국에 왔습니다\" deb yozadi. Demak Koreyaga qiziqishi tufayli kelgan; Koreyada tugʻilmagan va doʻst tanishtirgani ham aytilmagan.",
            },
            {
                "text": "프랑스에 있는 친구들이 글쓴이를 부러워하는 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "글쓴이가 한국 문화를 가까이에서 즐기고 있기 때문에",
                    "글쓴이가 한국에서 가수로 데뷔했기 때문에",
                    "글쓴이가 한국어 시험에서 일 등을 했기 때문에",
                ],
                "answer": 0,
                "explanation": "Doʻstlar undan qoʻshiq maʼnosini soʻrashadi, CD va kosmetika yuborishini iltimos qilishadi — yaʼni u koreys madaniyatidan bevosita bahramand boʻlayotgani uchun havas qilishadi. Qoʻshiqchi boʻlgani yoki imtihon haqida matnda hech narsa yoʻq.",
            },
            {
                "text": "글쓴이가 한국어를 더 열심히 공부하려는 까닭은 무엇입니까?",
                "choices": [
                    "한국 회사에 취직하기 위해서",
                    "친구들을 가르치고 노래와 드라마를 더 잘 이해하기 위해서",
                    "한국 국적을 얻기 위해서",
                ],
                "answer": 1,
                "explanation": "Oxirgi xatboshida u \"실력이 늘면 친구들을 가르쳐줄 수 있고, 좋아하는 노래와 드라마를 더 잘 이해할 수 있다\" deydi. Ishga kirish yoki fuqarolik haqida gap yoʻq.",
            },
        ],
    },
    {
        "title":   "어휘 속에 숨은 한국 문화",
        "summary": "Machjangu, komushinni teskari kiyish, ttengttengi — soʻzlar ortida yashiringan koreys madaniyati.",
        "order":   2,
        "grammar": [
            {
                "pattern":  "-게 마련이다",
                "meaning":  "Tabiiy va muqarrar: ... boʻlishi tayin, oʻz-oʻzidan shunday boʻladi.",
                "examples": ["문화는 어휘를 통해 나타나게 마련이다.", "사람은 누구나 실수하게 마련이다."],
            },
            {
                "pattern":  "-(으)ㄴ/는 탓에",
                "meaning":  "Salbiy sabab: ... tufayli (yomon natija).",
                "examples": ["마음이 급한 탓에 신을 거꾸로 신었다.", "늦게 잔 탓에 아침에 피곤했어요."],
            },
            {
                "pattern":  "-다가",
                "meaning":  "Bir ishni qilib turib, uni toʻxtatib boshqa holatga oʻtish.",
                "examples": ["다른 남자를 만나다가 애인에게 들켰다.", "길을 걷다가 친구를 만났어요."],
            },
            {
                "pattern":  "-(으)라고 하다 (간접 명령)",
                "meaning":  "Buyruqni bilvosita yetkazish: ...ishni (aytmoq/soʻramoq).",
                "examples": ["다른 남자를 사귀지 말라고 했다.", "선생님이 조용히 하라고 하셨어요."],
            },
        ],
        "body": '''<p>한 언어의 <span class="cn-word" data-tr="soʻz boyligi">어휘</span>에는 그 언어 사회의 문화가 <span class="cn-word" data-pos="verb" data-tr="mujassam boʻlgan">담겨</span> 있다. 어휘를 통해 그 사회의 문화를 알 수 있고, 문화는 어휘를 통해 <span class="cn-word" data-pos="verb" data-tr="namoyon boʻladi">나타나게</span> 마련이다. 한국어 어휘에도 한국 문화가 잘 <span class="cn-word" data-pos="verb" data-tr="aks etgan">반영되어</span> 있는데 예를 들어 '남의 말에 <span class="cn-word" data-pos="verb" data-tr="rozi boʻlmoq">동의하다</span>'는 뜻을 가진 '맞장구치다'는 한국 <span class="cn-word" data-tr="anʼana">전통</span> 음악인 풍물놀이에서 <span class="cn-word" data-pos="verb" data-tr="kelib chiqqan">유래되었다</span>. 풍물놀이를 할 때 둘이 <span class="cn-word" data-pos="verb" data-tr="yuzma-yuz turib">마주서서</span> 치는 장구를 맞장구라고 하는데, 맞장구를 칠 때는 서로 마음이 잘 맞아야 한다. 남의 의견에 동의하는 것도 서로 마음이 맞아야 하므로 '맞장구치다'가 '동의하다'라는 뜻을 가지게 되는데, 맞장구칠 때에는 "맞아", "그럼" 등과 같은 표현이 사용된다. 이것 외에도 한국어 어휘 속에는 <span class="cn-word" data-pos="adj" data-tr="turli-tuman">다양한</span> 한국 문화가 <span class="cn-word" data-pos="verb" data-tr="yashiringan">숨어</span> 있으니 지금부터 함께 찾아보도록 하자.</p>
<p><strong>고무신을 거꾸로 신다</strong> "너, 고무신 <span class="cn-word" data-pos="adv" data-tr="teskari">거꾸로</span> 신으면 안 돼." 이게 무슨 말일까? 이것은 <span class="cn-word" data-tr="armiya">군대</span> 가는 남자가 여자 친구에게 자신이 군대에 가 있는 동안 자신을 <span class="cn-word" data-pos="verb" data-tr="tashlab, voz kechib">버리고</span> 다른 남자를 사귀지 말라는 뜻으로 하는 말이다. 그런데 왜 <span class="cn-word" data-pos="adv" data-tr="nega aynan">하필</span> 고무신일까? 그것은 이 말이 생겼을 당시, 한국을 <span class="cn-word" data-pos="verb" data-tr="ramzi boʻlgan">대표하는</span> 신발이 고무신이었기 때문이다. 그때 군대 간 남자를 버리고 다른 남자에게 가는 여자들이 있었을 것이다. 다른 남자를 만나다가 휴가 나온 애인에게 <span class="cn-word" data-pos="verb" data-tr="qoʻlga tushganda">들켰을 때</span> 여자는 마음이 너무 <span class="cn-word" data-pos="adj" data-tr="shoshqin, shoshilinch">급한</span> 탓에 고무신을 거꾸로 신고 <span class="cn-word" data-pos="verb" data-tr="qochib ketmoq">도망가는</span> 일도 있었다고 한다. 그래서 '고무신을 거꾸로 신다'는 '여자가 사귀던 남자와 <span class="cn-word" data-pos="adv" data-tr="bir tomonlama">일방적으로</span> 헤어지다'라는 뜻을 가지게 되었다. 요즘은 <span class="cn-word" data-pos="adv" data-tr="aksincha">반대로</span> 군대 가는 남자에게 여자가 "군화 거꾸로 신지 마."라고 하기도 한다.</p>
<p><strong>땡땡이치다</strong> "나 오늘 수업 땡땡이쳤어." 이 말은 수업에 가지 않고 다른 일을 했다는 뜻이다. 땡땡이는 '<span class="cn-word" data-tr="qoʻngʻiroq">종</span>'을 <span class="cn-word" data-pos="verb" data-tr="bildiruvchi, ishora qiluvchi">가리키는</span> 말인데, <span class="cn-word" data-pos="adv" data-tr="ilgari, avvallari">예전에는</span> 수업이 시작되고 끝나는 시간을 종을 쳐서 <span class="cn-word" data-pos="verb" data-tr="bildirar edi, xabar berardi">알렸다</span>. 여기에서는 수업이 끝날 때 치는 종을 말한다. 그래서 '땡땡이를 치다'라는 말은 '수업이 끝나다'라는 뜻이며, '공부를 <span class="cn-word" data-pos="adv" data-tr="birpas, qisqa vaqt">잠시</span> 쉬다'라는 의미도 <span class="cn-word" data-pos="verb" data-tr="oʻz ichiga oladi">포함되어</span> 있다. 여기에서 의미가 더 <span class="cn-word" data-pos="verb" data-tr="oʻzgarib">변화해</span> '<span class="cn-word" data-pos="verb" data-tr="ayyorlik qilib">꾀를 부려서</span> 일이나 공부를 열심히 하지 않거나 빠지다'라는 뜻을 가지게 된 것이다.</p>
<p><strong>쏘다</strong> "돈 걱정 말고 많이들 먹어. 오늘 밥값은 내가 쏠게." 여기에서 '쏘다'는 '돈을 쓰다'를 <span class="cn-word" data-pos="verb" data-tr="taʼkidlagan">강조한</span> 표현이다. 한국에서는 식당 <span class="cn-word" data-tr="kassa">계산대</span>에서 돈을 먼저 내겠다고 몸싸움을 하는 장면을 <span class="cn-word" data-pos="adv" data-tr="koʻpincha, tez-tez">흔히</span> 볼 수 있다. 식사가 끝나고 일행이 일어설 준비를 하거나 신발을 신는 사이에 한 사람이 일어나 <span class="cn-word" data-pos="adv" data-tr="tez, chaqqonlik bilan">재빨리</span> 계산대로 가면 나머지 사람들은 구두를 <span class="cn-word" data-pos="adv" data-tr="tuzukroq, joyida">제대로</span> 신지도 못한 채 뒤뚱거리며 달려 나간다. 서로 먼저 <span class="cn-word" data-tr="hamyon">지갑</span>을 <span class="cn-word" data-pos="verb" data-tr="chiqarmoqchi boʻlgan">꺼내려는</span> 상황이 <span class="cn-word" data-pos="adv" data-tr="xuddi, goʻyo">마치</span> 총을 꺼내려는 장면처럼 보이는데 마침내 몸싸움에서 <span class="cn-word" data-pos="verb" data-tr="gʻolib chiqqan, yutgan">이긴</span> 사람이 밥값을 총처럼 '쏘'게 되는 것이다. 뒷주머니에서 지갑을 꺼내 돈을 내는 행동이 허리에 찬 <span class="cn-word" data-tr="toʻpponcha">권총</span>을 꺼내 쏘는 것처럼 보여 '돈을 내다'를 '쏘다'로 표현하게 되었다고 한다.</p>''',
        "questions": [
            {
                "text": "이 글에서 글쓴이가 가장 말하고 싶은 것은 무엇입니까?",
                "choices": [
                    "한국의 전통 음악은 배우기 어렵다.",
                    "한국어 어휘 속에는 한국의 문화가 담겨 있다.",
                    "외국인은 한국의 관용 표현을 쓰면 안 된다.",
                ],
                "answer": 1,
                "explanation": "Kirish qismida \"어휘에는 문화가 담겨 있다\" (soʻz boyligida madaniyat mujassam) deyilgan, soʻng shu fikr misollar bilan isbotlanadi. Bu — matnning asosiy gʻoyasi; qolgan variantlar matnda umuman aytilmagan.",
            },
            {
                "text": "'고무신을 거꾸로 신다'라는 표현의 뜻으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "신발을 잘못 신어서 넘어지다",
                    "여자가 사귀던 남자와 일방적으로 헤어지다",
                    "군대에 가기 싫어서 도망가다",
                ],
                "answer": 1,
                "explanation": "Matnda aynan shu ibora \"여자가 사귀던 남자와 일방적으로 헤어지다\" maʼnosini bildirishi yozilgan. Boshqa variantlar iboraning kelib chiqishidagi detallar bilan chalgʻitadi, lekin maʼnosi emas.",
            },
            {
                "text": "이 글의 내용과 같은 것은 무엇입니까?",
                "choices": [
                    "'쏘다'는 원래 총을 쏘는 모습에서 나온 표현이다.",
                    "'맞장구치다'는 서양 음악에서 유래되었다.",
                    "'땡땡이'는 원래 시험을 뜻하는 말이었다.",
                ],
                "answer": 0,
                "explanation": "Matnda \"지갑을 꺼내 돈을 내는 행동이 권총을 꺼내 쏘는 것처럼 보여\" deyilgan — yaʼni 쏘다 toʻpponcha otish obrazidan kelgan. 맞장구 koreys anʼanaviy musiqasidan (풍물놀이), 땡땡이 esa qoʻngʻiroqdan kelgan, imtihondan emas.",
            },
        ],
    },
    {
        "title":   "야구장에서 즐기는 여가",
        "summary": "Beysbol maydonida taom, qoʻshiq va ishtiyoq — oʻyinni toʻliq his qilish usullari.",
        "order":   3,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 정도로",
                "meaning":  "Shu darajada ...ki (daraja/miqyosni bildiradi).",
                "examples": ["처음 온 사람도 금세 부를 수 있을 정도로 쉽다.", "배가 아플 정도로 많이 웃었어요."],
            },
            {
                "pattern":  "-도록",
                "meaning":  "Maqsad/natija: ... boʻlishi uchun, ...adigan qilib.",
                "examples": ["삼겹살을 구워 먹을 수 있도록 자리를 마련했다.", "잘 보이도록 크게 썼어요."],
            },
            {
                "pattern":  "-다(가) 보면",
                "meaning":  "Bir ishni davom ettira borsang, tabiiy natijaga erishasan.",
                "examples": ["노래를 따라 부르다 보면 스트레스가 풀린다.", "자꾸 듣다 보면 이해가 돼요."],
            },
            {
                "pattern":  "뭐니 뭐니 해도",
                "meaning":  "Nima deganda ham, eng muhimi (baholash iborasi).",
                "examples": ["야구장 간식은 뭐니 뭐니 해도 치킨과 맥주이다.", "뭐니 뭐니 해도 건강이 최고예요."],
            },
        ],
        "body": '''<p>프로 야구 경기장이 여가 문화 장소로 인기를 <span class="cn-word" data-pos="verb" data-tr="qozonmoq, erishmoq">얻고</span> 있다. 야구 경기를 <span class="cn-word" data-pos="verb" data-tr="tomosha qilmoq">관람하는</span> 것뿐만 아니라 이벤트에 <span class="cn-word" data-pos="verb" data-tr="ishtirok etmoq">참여하고</span> 큰 소리로 <span class="cn-word" data-tr="qoʻllab-quvvatlash">응원</span>도 하면서 스트레스를 <span class="cn-word" data-pos="verb" data-tr="ketkazib yubormoq">날려</span> 버릴 수 있기 때문에 가족, 친구, 연인끼리 <span class="cn-word" data-pos="adv" data-tr="sevib, xushlab">즐겨</span> 찾는 것이다. 그렇다면 야구 경기를 더 재미있게 즐기는 방법에 관해 알아보자.</p>
<p>한국의 프로 야구 시즌은 4월부터 10월까지이다. 시즌 중에 경기는 <span class="cn-word" data-pos="adv" data-tr="odatda">일반적으로</span> 평일에는 오후 6시반, 주말에는 오후 5시에 시작되는데 30분 전쯤에 <span class="cn-word" data-pos="verb" data-tr="yetib borib">도착해서</span> 경기장에 들어가기 전에 <span class="cn-word" data-tr="yengil taom">간식</span>을 준비한다. 야구 경기의 또 다른 재미로 간식 먹는 것을 빼 놓을 수 없는데, 야구장의 대표 간식은 뭐니 뭐니 해도 치킨과 맥주이다. 가족끼리 야구장을 찾는다면 삼겹살을 <span class="cn-word" data-pos="verb" data-tr="qovurib, kabob qilib">구워</span> 먹을 수 있도록 불판을 <span class="cn-word" data-pos="verb" data-tr="tayyorlab qoʻygan">마련해</span> 놓은 자리를 이용하는 것도 <span class="cn-word" data-pos="adj" data-tr="oʻzgacha">색다른</span> 재미일 것이다.</p>
<p>자신이 좋아하는 팀을 응원할 때 <span class="cn-word" data-pos="adv" data-tr="asosan">기본적으로</span> 필요한 것은 <span class="cn-word" data-tr="tayoqcha shar">막대 풍선</span>이다. 치어리더들이 춤으로 <span class="cn-word" data-pos="verb" data-tr="ruh bagʻishlasa">흥을 돋우면</span> 거기에 <span class="cn-word" data-pos="verb" data-tr="moslab">맞춰</span> 응원 팀의 로고가 찍힌 막대 풍선을 <span class="cn-word" data-pos="verb" data-tr="silkitsa">흔들면</span> 된다. 어떤 야구팀은 신문지를 <span class="cn-word" data-pos="adv" data-tr="maydalab">잘게</span> <span class="cn-word" data-pos="verb" data-tr="yirtib">찢어서</span> 술을 만들어 흔든다거나 바람을 불어 넣은 주황색 비닐봉지를 머리에 쓰는 <span class="cn-word" data-pos="adj" data-tr="oʻziga xos, gʻalati">특이한</span> 응원을 한다. 이 주황색 봉지는 경기 중반에 <span class="cn-word" data-pos="verb" data-tr="tarqatiladi">배부되는데</span>, 경기가 끝난 후에 쓰레기를 담아 버릴 수 있기 때문에 <span class="cn-word" data-tr="bir yoʻla ikki foyda">일거양득</span>의 효과가 있다.</p>
<p>각 <span class="cn-word" data-tr="zarbachi (beysbolda)">타자</span>마다 특색 있게 만들어진 <span class="cn-word" data-tr="qoʻllab-quvvatlash qoʻshigʻi">응원가</span>를 따라 부르는 것도 신나는 일이다. 이 응원가는 경기장에 처음 가 보는 사람이라도 <span class="cn-word" data-pos="adv" data-tr="tez orada, darrov">금세</span> 따라 부를 수 있을 정도로 쉬운 가사와 <span class="cn-word" data-pos="adj" data-tr="sodda, oddiy">단순한</span> 음으로 만들어졌다. 탁 트인 야외에서 주위 사람들과 <span class="cn-word" data-pos="adv" data-tr="bir ovozdan">한목소리로</span> 노래를 따라 부르고 파도타기 응원을 하다 보면 스트레스가 한 방에 <span class="cn-word" data-pos="verb" data-tr="tarqab ketadigan">사라지는</span> 기분을 느낄 것이다.</p>
<p><span class="cn-word" data-pos="adv" data-tr="agar, mabodo">만일</span> 연인끼리 야구장에 갔다면 이벤트도 빼 놓을 수 없다. 경기 중반, 대형 <span class="cn-word" data-tr="katta ekran (tablo)">전광판</span>에 자신의 모습이 <span class="cn-word" data-pos="verb" data-tr="koʻrinsa, aks etsa">비치면</span> 그것은 두 사람이 뽀뽀를 해야 한다는 뜻이다. 큰 화면에 자신의 얼굴이 나오면 <span class="cn-word" data-pos="adj" data-tr="uyaladigan, hijolat">부끄럽기도</span> 하겠지만 애정을 <span class="cn-word" data-pos="verb" data-tr="koʻz-koʻz qilmoq">과시하고</span> 선물도 받을 수 있는 좋은 기회임을 잊지 말자. 야구장에서 사랑하는 사람에게 프러포즈를 할 수 있다. <span class="cn-word" data-pos="adv" data-tr="oldindan">미리</span> 신청을 하면 경기 중 <span class="cn-word" data-pos="adv" data-tr="birpas">잠깐</span> 쉬는 시간에 전광판에 사랑을 <span class="cn-word" data-pos="verb" data-tr="izhor qilmoq">고백하는</span> 장면이 나오게 된다. 이때 남자가 경기장 안으로 여자 친구를 데리고 나가서 꽃과 반지로 <span class="cn-word" data-tr="turmush qurish taklifi">청혼</span>을 하는 것이다.</p>
<p>가족들의 <span class="cn-word" data-tr="sayr, chiqish">나들이</span> 장소로, 연인들의 데이트 장소로, 또 친구들과의 만남의 장소로 <span class="cn-word" data-pos="adv" data-tr="turlicha, xilma-xil">다양하게</span> <span class="cn-word" data-pos="verb" data-tr="foydalaniladigan">활용되는</span> 야구 경기장. 무언가 즐길 만한 여가활동을 찾고 있다면, 이번 주말에는 가까운 야구장에 가 보는게 어떨까.</p>''',
        "questions": [
            {
                "text": "이 글의 중심 내용으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "프로 야구 선수가 되는 방법",
                    "야구장을 더 재미있게 즐기는 여러 가지 방법",
                    "한국 프로 야구의 역사",
                ],
                "answer": 1,
                "explanation": "Matnda ovqat, qoʻllab-quvvatlash, qoʻshiq va turli tadbirlar orqali beysbol oʻyinini qiziqarli oʻtkazish usullari sanab oʻtilgan. Sportchi boʻlish yoki tarix haqida emas.",
            },
            {
                "text": "주황색 비닐봉지가 '일거양득'이라고 한 이유는 무엇입니까?",
                "choices": [
                    "응원도 하고 경기 후 쓰레기도 담을 수 있어서",
                    "값이 싸고 색깔도 예뻐서",
                    "비를 막고 햇빛도 가려 주어서",
                ],
                "answer": 0,
                "explanation": "Matnda sariq xalta bilan qoʻllab-quvvatlash qilinishi, oʻyindan keyin esa unga axlat solib tashlash mumkinligi aytilgan — shu sababli \"bir yoʻla ikki foyda\".",
            },
            {
                "text": "연인이 야구장에 갔을 때 즐길 수 있는 것으로 이 글에 나오지 않은 것은 무엇입니까?",
                "choices": [
                    "전광판에 얼굴이 나오면 뽀뽀하는 이벤트",
                    "전광판을 통한 프러포즈",
                    "무료로 반지를 나눠 주는 행사",
                ],
                "answer": 2,
                "explanation": "Matnda ekranda yuz chiqsa oʻpish tadbiri va ekran orqali turmush qurish taklifi tilga olingan, lekin bepul uzuk tarqatish haqida hech narsa yoʻq.",
            },
        ],
    },
    {
        "title":   "버릴 것은 없다: 리폼 이야기",
        "summary": "Eski kiyimlarga yangi hayot: riform, slou-feshn va atrof-muhitni asrash.",
        "order":   4,
        "grammar": [
            {
                "pattern":  "-자니",
                "meaning":  "Ikkilanish: qilay desam (biror kamchilik yoki noqulaylik bor).",
                "examples": ["그냥 입자니 촌스럽고 버리자니 아깝다.", "사자니 비싸고 안 사자니 아쉬워요."],
            },
            {
                "pattern":  "-(으)면서",
                "meaning":  "Bir vaqtda / ...ishi bilan bogʻliq holda (ikki holat birga).",
                "examples": ["관심을 갖는 사람들이 늘어나면서 리폼이 인기를 끈다.", "음악을 들으면서 공부해요."],
            },
            {
                "pattern":  "-기보다(는)",
                "meaning":  "...dan koʻra (afzallikni bildiradi).",
                "examples": ["결혼식을 호화롭게 하기보다는 의미있게 한다.", "말하기보다는 듣는 편이에요."],
            },
            {
                "pattern":  "못지않게",
                "meaning":  "...dan qolishmaydigan darajada, ... kabi.",
                "examples": ["헌 옷도 새 옷 못지않게 예쁘다.", "그는 전문가 못지않게 잘한다."],
            },
        ],
        "body": '''<p>옷장을 열어 보면 새 옷이지만 <span class="cn-word" data-tr="moda, urf">유행</span>에 맞지 않아 안 입는 옷이 많다. <span class="cn-word" data-pos="adv" data-tr="shunchaki, shundoq">그냥</span> 입자니 <span class="cn-word" data-pos="adj" data-tr="didsiz, eskicha">촌스럽고</span> 버리자니 <span class="cn-word" data-pos="adj" data-tr="isrof, achinarli">아깝고</span> 해서 어떻게 해야 할까 <span class="cn-word" data-pos="verb" data-tr="bosh qotirgan">고민했던</span> 경험, 누구나 한 번쯤은 있었을 것이다. 이럴 때 <span class="cn-word" data-pos="adj" data-tr="oddiy, sodda">간단한</span> 방법으로 리폼에 <span class="cn-word" data-pos="verb" data-tr="qoʻl urmoq, urinib koʻrmoq">도전해</span> 보는 것은 어떨까?</p>
<p>환경 운동과 나만의 것에 관심을 갖는 사람들이 <span class="cn-word" data-pos="verb" data-tr="koʻpaygani sari">늘어나면서</span> 리폼에 대한 관심이 <span class="cn-word" data-pos="adv" data-tr="borgan sari">갈수록</span> 높아지고 있다. 사실 리폼은 새 것을 사는 것보다 더 어려운 작업이지만 리폼 <span class="cn-word" data-tr="ishqiboz, muxlis">애호가</span>들은 자원의 <span class="cn-word" data-tr="qayta ishlatish">재활용</span>과 환경 보호를 위해 꼭 필요한 일이라고 말한다. <span class="cn-word" data-pos="adv" data-tr="tez-tez, qayta-qayta">자꾸</span> 새 옷을 사 달라고 <span class="cn-word" data-pos="verb" data-tr="qistayveradigan, yalinadigan">졸라 대는</span> 딸 때문에 고민하던 주부 이지연씨(38세)는 <span class="cn-word" data-pos="adj" data-tr="eski">헌</span> 티셔츠에 물감을 <span class="cn-word" data-pos="verb" data-tr="boʻyab">칠하고</span> 리본을 달아서 새 옷 못지않게 예쁜 티셔츠를 만들었다. 세상에 하나뿐인 리폼 티셔츠를 입고 <span class="cn-word" data-pos="verb" data-tr="xursand boʻlayotgan">기뻐하는</span> 딸의 모습을 보면서 이지연 씨는 큰 만족감을 느낄 수 있었다.</p>
<p>최근, 유행에 따라 <span class="cn-word" data-pos="adv" data-tr="tez">빠르게</span> 생산되어 <span class="cn-word" data-pos="adv" data-tr="arzon">저렴하게</span> 판매되는 옷인 '패스트 패션'이 소비자들에게 인기가 많다. 그들은 유행에 맞는 <span class="cn-word" data-pos="adj" data-tr="arzon, qimmat emas">값싼</span> 옷을 구입해서 입고, 유행이 지나면 또 다른 옷을 구입해서 입는다. 이렇게 한 철만 입고 버리는 옷은 <span class="cn-word" data-pos="adj" data-tr="jiddiy, ogʻir">심각한</span> 환경 문제를 <span class="cn-word" data-pos="verb" data-tr="keltirib chiqaradi">일으킨다</span>. 버려지는 옷들은 대부분 <span class="cn-word" data-tr="yoqib yoʻq qilish">소각</span> 처리되는데 이때 옷감에서 나오는 <span class="cn-word" data-tr="zararli gaz">유해가스</span>로 인해 대기가 <span class="cn-word" data-pos="verb" data-tr="ifloslanadi">오염된다</span>. 또한 옷을 만들 때 사용되는 염색 약품 역시 환경오염의 원인이 된다. 이렇듯 환경 문제의 심각성이 <span class="cn-word" data-pos="verb" data-tr="oshkor boʻla boshlab">드러나면서</span> 관심을 받고 있는 것이 바로 '슬로 패션'이다. 슬로 패션은 유행을 따라가지 않고, 재활용과 리폼을 한 옷으로 환경에 나쁜 영향을 미치지 않는다.</p>
<p>의류는 물론이거니와 신발, 가방, 가구, 실내 장식품도 모두 리폼의 대상이 된다. 헌 옷으로 만든 가방이나 지갑을 들고 다니고, <span class="cn-word" data-pos="adj" data-tr="eskirgan, titilgan">낡은</span> 나무 상자로 만든 정리함과 책꽂이 등으로 집안을 <span class="cn-word" data-pos="verb" data-tr="bezaydi">꾸민다</span>. 가구는 색을 새로 칠하거나 부속품을 갈아 새 것처럼 만들 수 있다. <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> '에코 웨딩'도 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">등장했다</span>. 한 번뿐인 결혼식을 <span class="cn-word" data-pos="adv" data-tr="hashamatli tarzda">호화롭게</span> 하기보다는 의미있게 하려는 예비 신혼부부들이 본인들의 옷을 리폼해 웨딩 의상으로 만들고 친환경 재생 종이로 <span class="cn-word" data-tr="toʻy taklifnomasi">청첩장</span>을 만든다. 신혼살림도 가능하면 재활용품을 사용해 준비하면서 비용도 <span class="cn-word" data-pos="verb" data-tr="tejab">아끼고</span> 환경의 중요성을 다시 한 번 생각한다.</p>
<p>조금만 관심을 가지면 세상에 버릴 것은 없다. 한 사람이 평생을 살면서 <span class="cn-word" data-pos="verb" data-tr="chiqaradigan">배출하는</span> 생활 쓰레기는 <span class="cn-word" data-pos="adv" data-tr="naq, hatto">무려</span> 55톤에 이른다고 한다. 요즘은 인터넷과 동호회를 통해서 생활 속 리폼 정보를 <span class="cn-word" data-pos="adv" data-tr="oson, osonlik bilan">쉽게</span> 얻을 수 있으니 마음만 먹으면 리폼은 어렵지 않다. 매일 매일 <span class="cn-word" data-pos="verb" data-tr="yogʻilib turadigan">쏟아지는</span> 새 상품 속에서 버려진 것들을 <span class="cn-word" data-pos="verb" data-tr="qayta tiriltirmoqchi boʻlgan">되살리려는</span> 노력이 우리의 생활을 건강하고 즐겁게 만들어줄 것이다.</p>''',
        "questions": [
            {
                "text": "'슬로 패션'에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "유행에 따라 옷을 빠르게 만들어 싸게 파는 것",
                    "재활용과 리폼을 통해 환경에 해를 덜 주는 것",
                    "값비싼 명품 옷을 오래 입는 것",
                ],
                "answer": 1,
                "explanation": "Matnda \"슬로 패션은 유행을 따라가지 않고, 재활용과 리폼을 한 옷으로 환경에 나쁜 영향을 미치지 않는다\" deyilgan. Birinchi variant esa aksincha — 'fast fashion' taʼrifi.",
            },
            {
                "text": "'패스트 패션'이 환경에 나쁜 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "버려진 옷을 소각할 때 유해가스가 나오기 때문에",
                    "옷을 만들 때 물을 너무 많이 쓰기 때문에",
                    "옷이 너무 비싸서 아무도 안 사기 때문에",
                ],
                "answer": 0,
                "explanation": "Matnda tashlangan kiyimlar koʻpincha yoqib yuborilishi va shunda chiqadigan zararli gaz havoni ifloslashi aytilgan. Suv sarfi yoki narx bunday sabab sifatida keltirilmagan.",
            },
            {
                "text": "이 글에서 글쓴이가 궁극적으로 말하고 싶은 것은 무엇입니까?",
                "choices": [
                    "새 옷을 자주 사는 것이 좋다.",
                    "조금만 관심을 가지면 버릴 것이 없고, 리폼이 삶을 건강하게 만든다.",
                    "결혼식은 무조건 검소하게 해야 한다.",
                ],
                "answer": 1,
                "explanation": "Oxirgi xatboshi \"조금만 관심을 가지면 세상에 버릴 것은 없다\" va riform hayotni sogʻlom hamda quvnoq qiladi degan xulosa bilan tugaydi — bu matnning asosiy xabari.",
            },
        ],
    },
    {
        "title":   "늙어가는 한국: 저출산과 고령화",
        "summary": "Nega Koreyada bolalar kam tugʻilyapti va jamiyat qarimoqda? Sabablari va yechimlari.",
        "order":   5,
        "grammar": [
            {
                "pattern":  "-는 반면(에)",
                "meaning":  "Aksincha, boshqa tomondan (qarama-qarshilik).",
                "examples": ["젊은 사람은 줄어드는 반면에 노인은 늘어난다.", "월급은 많은 반면에 일이 힘들어요."],
            },
            {
                "pattern":  "-(으)ㅁ에 따라",
                "meaning":  "...i bilan, ...ga qarab (oʻzgarish sababi).",
                "examples": ["의학이 발달함에 따라 평균 수명이 길어졌다.", "시간이 지남에 따라 상황이 나아졌어요."],
            },
            {
                "pattern":  "-아/어도",
                "meaning":  "...sa ham (yon berish, qarama-qarshilik).",
                "examples": ["다시 일을 하고 싶어도 일자리가 없다.", "아무리 바빠도 밥은 먹어야 해요."],
            },
            {
                "pattern":  "-(으)ㄹ 수만은 없다",
                "meaning":  "Faqat ...deb ham boʻlmaydi (bir tomonlama qabul qilib boʻlmaydi).",
                "examples": ["오래 산다고 마냥 좋아할 수만은 없다.", "언제까지나 참을 수만은 없어요."],
            },
        ],
        "body": '''<p>한국이 <span class="cn-word" data-pos="verb" data-tr="qarib bormoqda">늙어가고</span> 있다. 아이를 낳지 않거나 적게 낳아 젊은 사람은 <span class="cn-word" data-pos="verb" data-tr="kamayadigan">줄어드는</span> 반면에 <span class="cn-word" data-tr="oʻrtacha umr koʻrish">평균 수명</span>이 늘어 노인 인구는 <span class="cn-word" data-pos="verb" data-tr="ortib bormoqda">증가하고</span> 있는 것이다. 이러한 <span class="cn-word" data-tr="tugʻilishning kamayishi">저출산</span>, <span class="cn-word" data-tr="aholining qarishi">고령화</span> 현상의 원인은 무엇일까?</p>
<p>대구 달서구에 사는 63세 이 모 씨는 <span class="cn-word" data-tr="nafaqaga chiqish">퇴직</span> 후 3년 째 <span class="cn-word" data-tr="ish oʻrni">일자리</span>를 <span class="cn-word" data-pos="verb" data-tr="izlamoq, topmoqchi">구하고</span> 있지만 쉽지가 않다. 임금이 낮은 아파트 경비원 일도 <span class="cn-word" data-tr="raqobat darajasi">경쟁률</span>이 높아서 취직하기는 <span class="cn-word" data-tr="osmondan yulduz uzishday (juda qiyin)">하늘의 별 따기</span>이다. 젊은 시절 먹고 살기 바쁜 탓에 <span class="cn-word" data-pos="adj" data-tr="tuzukroq, arzigulik">변변한</span> <span class="cn-word" data-tr="keksalikka tayyorgarlik">노후 대책</span> 하나 <span class="cn-word" data-pos="verb" data-tr="tayyorlab">마련해</span> 두지 못했다. 그렇다고 자식들에게 손을 벌리기도 어려워 이 씨는 오늘도 일자리를 찾아 <span class="cn-word" data-pos="adv" data-tr="u yer-bu yer">여기저기</span> <span class="cn-word" data-pos="verb" data-tr="sarson boʻladi">헤맨다</span>. 이런 사람이 <span class="cn-word" data-pos="adv" data-tr="faqatgina">비단</span> 이 씨만은 아니다.</p>
<p>자녀 <span class="cn-word" data-tr="bola tarbiyasi xarajatlari">양육비</span> 부담, 여성의 사회 진출 증가 등의 원인으로 <span class="cn-word" data-pos="verb" data-tr="yuzaga kelgan">생겨난</span> 저출산 현상은 <span class="cn-word" data-pos="adv" data-tr="tez orada, darrov">곧</span> 고령화로 <span class="cn-word" data-pos="verb" data-tr="ulanib ketadi, davom etadi">이어진다</span>. 출생아가 줄어들게 되면 65세 이상의 고령 인구가 전체 인구 가운데 <span class="cn-word" data-pos="verb" data-tr="egallaydigan">차지하는</span> 비율이 그 만큼 늘어나기 때문이다. 한국은 2000년에 고령 인구 비율이 7%를 넘어 <span class="cn-word" data-pos="adv" data-tr="allaqachon">이미</span> '고령화 사회'로 <span class="cn-word" data-pos="verb" data-tr="kirdi, oʻtdi">진입했고</span>, 2019년에는 14% 이상인 '고령 사회', 2026년에는 20% 이상인 '초고령 사회'가 될 것으로 <span class="cn-word" data-pos="verb" data-tr="bashorat qilinmoqda">전망된다</span>.</p>
<p>의학이 <span class="cn-word" data-pos="verb" data-tr="rivojlanib">발달하고</span> 식생활이 향상됨에 따라 평균 수명이 길어졌지만 오래 산다고 <span class="cn-word" data-pos="adv" data-tr="shunchaki, cheksiz">마냥</span> 좋아할 수만은 없는 것이 현실이다. <span class="cn-word" data-pos="adv" data-tr="ayni, qizigan paytda">한창</span> 일할 수 있는 나이에 퇴직을 하지만 다시 일을 하고 싶어도 노인 일자리는 <span class="cn-word" data-pos="adv" data-tr="juda ham, nihoyatda">턱없이</span> <span class="cn-word" data-pos="adj" data-tr="yetishmaydi, kam">부족하다</span>. 노후 대책을 <span class="cn-word" data-pos="adv" data-tr="ulgurmay">미처</span> 세우지 못한 노인들은 경제적으로 어려움을 <span class="cn-word" data-pos="verb" data-tr="boshdan kechirmoq, duch kelmoq">겪게</span> 되고 이러한 노부모를 모셔야 하는 자식들 또한 경제적 <span class="cn-word" data-tr="yuk, tashvish">부담</span>이 <span class="cn-word" data-pos="verb" data-tr="ogʻirlashib">가중되어</span> <span class="cn-word" data-pos="adv" data-tr="oxir-oqibat">결국</span> 저출산으로 이어지게 되는 것이다.</p>
<p>고령화는 한국의 경제 성장을 <span class="cn-word" data-pos="verb" data-tr="toʻsqinlik qiladigan">방해하는</span> 원인으로도 <span class="cn-word" data-pos="verb" data-tr="koʻrsatilmoqda, taʼkidlanmoqda">지적되고</span> 있다. 일할 수 있는 젊은이들이 없으니 회사가 사람을 구하기 어려워질 것은 불을 보듯 <span class="cn-word" data-pos="adj" data-tr="aniq, shundoq koʻrinib turgan">뻔한</span> 일이 아닌가.</p>
<p>이에 대한 대책으로 전문가들은 노인 복지 정책이 필요하다고 말하고 있다. <span class="cn-word" data-tr="pensiya yoshi">정년</span>을 <span class="cn-word" data-pos="verb" data-tr="uzaytirib">연장하여</span> 노인들이 더 늦은 나이까지 일 할 수 있게 하고, 퇴직 후에도 경제적 능력을 가질 수 있도록 노인 일자리를 많이 만들어야 한다. 또한 지역 사회에 참여할 수 있는 다양한 프로그램을 <span class="cn-word" data-pos="verb" data-tr="ishlab chiqib">개발하여</span> 노년을 즐겁고 보람 있게 보낼 수 있도록 도와주는 정책을 <span class="cn-word" data-pos="verb" data-tr="amalga oshirish, joriy qilish">시행해야</span> 한다는 것이다. 한국은 고령화가 <span class="cn-word" data-pos="adv" data-tr="tez">빨리</span> 진행되고 있지만 이에 대한 준비는 <span class="cn-word" data-pos="adv" data-tr="hali">아직</span> 부족하다. 저출산과 고령화에 맞는 대책을 세워 변화하는 사회에 잘 <span class="cn-word" data-pos="verb" data-tr="moslashish, javob berish">대응하는</span> 것이 '100세 시대'를 <span class="cn-word" data-pos="verb" data-tr="kutib olmoq">맞이하는</span> 우리의 자세일 것이다.</p>''',
        "questions": [
            {
                "text": "저출산과 고령화의 관계에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "저출산과 고령화는 서로 관계가 없다.",
                    "출생아가 줄면 고령 인구 비율이 높아져 고령화로 이어진다.",
                    "고령화가 되면 아이를 더 많이 낳게 된다.",
                ],
                "answer": 1,
                "explanation": "Matnda \"출생아가 줄어들면 고령 인구가 차지하는 비율이 늘어난다\" deb tushuntirilgan — yaʼni kam tugʻilish qarishga olib keladi. Ikkalasi bir-biriga bogʻliq.",
            },
            {
                "text": "이 모 씨의 사례를 통해 글쓴이가 보여 주려는 것은 무엇입니까?",
                "choices": [
                    "퇴직한 노인이 일자리를 구하기 어려운 현실",
                    "노인들이 일을 하기 싫어한다는 것",
                    "경비원 일이 매우 인기가 많다는 것",
                ],
                "answer": 0,
                "explanation": "63 yoshli janob nafaqadan keyin 3 yildan beri ish topolmayapti — bu keksalar uchun ish topish qanchalik qiyinligini koʻrsatuvchi misol. U ishlashni xohlaydi, lekin oʻrin yoʻq.",
            },
            {
                "text": "저출산 고령화 대책으로 이 글에서 제시한 것이 아닌 것은 무엇입니까?",
                "choices": [
                    "정년을 연장하는 것",
                    "노인 일자리를 늘리는 것",
                    "결혼을 법으로 금지하는 것",
                ],
                "answer": 2,
                "explanation": "Matnda pensiya yoshini uzaytirish, keksalar uchun ish oʻrinlarini koʻpaytirish va turli dasturlar ishlab chiqish taklif qilingan. Nikohni qonun bilan taqiqlash haqida umuman gap yoʻq.",
            },
        ],
    },
    {
        "title":   "대나무의 고장, 담양 여행",
        "summary": "Bambuk oʻrmoni Jungnogwon va Soswewon bogʻi — Damyangga bir kunlik sayohat.",
        "order":   6,
        "grammar": [
            {
                "pattern":  "-(으)ㄹ세라",
                "meaning":  "...ib qolmasin deb, ...maslik uchun ehtiyot boʻlib.",
                "examples": ["좋은 구경거리를 놓칠세라 얼른 따라나섰다.", "아이가 깰세라 조용히 걸었다."],
            },
            {
                "pattern":  "-기 그지없다",
                "meaning":  "Behad ..., cheksiz ... (kuchli baho).",
                "examples": ["나무들의 모습이 아름답기 그지없었다.", "도와주셔서 고맙기 그지없습니다."],
            },
            {
                "pattern":  "-고 나니",
                "meaning":  "...gandan keyin (his yoki natija paydo boʻladi).",
                "examples": ["안내 글을 읽고 나니 마음이 편해졌다.", "밥을 먹고 나니 졸렸어요."],
            },
            {
                "pattern":  "-을/를 비롯한(비롯하여)",
                "meaning":  "... boshchiligida, ...ni oʻz ichiga olib.",
                "examples": ["죽부인을 비롯한 여러 죽제품이 있다.", "교장 선생님을 비롯하여 많은 분이 오셨어요."],
            },
        ],
        "body": '''<p>지난 주말에 나는 대나무의 <span class="cn-word" data-tr="yurt, makon">고장</span> '담양'에 다녀왔다. 사계절 <span class="cn-word" data-pos="adv" data-tr="doim, hamisha">늘</span> <span class="cn-word" data-pos="adj" data-tr="koʻm-koʻk, yashil">푸르고</span> <span class="cn-word" data-pos="adv" data-tr="tik, roʻppa-rost">곧게</span> <span class="cn-word" data-pos="verb" data-tr="oʻsadigan">자라는</span> 대나무는 한국에서 옛 <span class="cn-word" data-tr="qadimgi olim-ziyoli">선비</span>의 <span class="cn-word" data-pos="adj" data-tr="mustahkam, qatʼiy">굳은</span> <span class="cn-word" data-tr="iroda">의지</span>에 <span class="cn-word" data-pos="verb" data-tr="oʻxshatiladi, qiyoslanadi">비유된다</span>고 한다. 한국에 와서는 대나무 방석, 죽순 요리 정도만 보았는데, 대나무가 숲을 이룬 곳이 있다는 친구의 말에 좋은 <span class="cn-word" data-tr="tomosha, diqqatga sazovor narsa">구경거리</span>를 놓칠세라 <span class="cn-word" data-pos="adv" data-tr="darrov, tezda">얼른</span> 따라 <span class="cn-word" data-pos="verb" data-tr="yoʻlga chiqdim">나섰다</span>.</p>
<p><span class="cn-word" data-pos="adv" data-tr="naq, hatto">무려</span> 4시간이 걸려 도착한 담양에서 우리는 <span class="cn-word" data-pos="adv" data-tr="avvalo">우선</span> '죽녹원'으로 <span class="cn-word" data-pos="verb" data-tr="yoʻl oldik">향했다</span>. 죽녹원으로 가는 길에 <span class="cn-word" data-pos="adv" data-tr="birpas">잠시</span> <span class="cn-word" data-pos="verb" data-tr="kirib oʻtgan">들른</span> 메타세쿼이아 길은 <span class="cn-word" data-pos="adv" data-tr="chinakamiga, haqiqatan">그야말로</span> <span class="cn-word" data-tr="ajoyib manzara">장관</span>이었다. 길 양쪽으로 <span class="cn-word" data-pos="adv" data-tr="tizilib, uzun">쭉</span> 줄지어 곧게 서 있는 나무들의 모습이 <span class="cn-word" data-pos="adj" data-tr="goʻzal">아름답기</span> 그지없었다.</p>
<p>오전 10시가 넘어 죽녹원에 도착했다. <span class="cn-word" data-pos="adv" data-tr="uzoqdan ham">멀리서도</span> 보이는 키가 큰 대나무 숲 덕분에 죽녹원이라는 것을 <span class="cn-word" data-pos="adv" data-tr="bir qarashda">한눈에</span> 알 수 있었다. 죽녹원은 사랑이 <span class="cn-word" data-pos="verb" data-tr="oʻzgarmaydigan">변치</span> 않는 길, 추억의 샛길, 선비의 길 등 8가지 주제의 길로 구성된 <span class="cn-word" data-tr="bogʻ">정원</span>이며, 각각의 길마다 다른 특징이 있다고 한다. 대나무 숲이 사람의 마음을 <span class="cn-word" data-pos="verb" data-tr="tinchlantiradi">안정시켜</span> 준다는 안내 글을 읽고 나니 대나무 숲 사이로 <span class="cn-word" data-pos="verb" data-tr="esib keladigan">불어오는</span> <span class="cn-word" data-pos="adj" data-tr="salqin, yoqimli">시원한</span> 바람에 <span class="cn-word" data-tr="tana va ruh">심신</span>이 다 <span class="cn-word" data-pos="verb" data-tr="tiniqlashadigan, poklanadigan">맑아지는</span> 듯했다.</p>
<p>한국에서 대나무는 <span class="cn-word" data-pos="adj" data-tr="har xil, turli">각종</span> <span class="cn-word" data-tr="roʻzgʻor buyumlari">생활용품</span>과 건강식품으로도 <span class="cn-word" data-pos="adv" data-tr="turlicha, xilma-xil">다양하게</span> <span class="cn-word" data-pos="verb" data-tr="foydalaniladi">이용된다</span>고 한다. 죽부인을 비롯한 방석과 베개, 소쿠리, <span class="cn-word" data-tr="yelpigʻich">부채</span> 등의 죽제품으로 만들어 쓰기도 하고 건강을 위해 죽염, 댓잎 차 등으로 만들어 먹기도 한다. 죽녹원 앞 가게에서 나는 <span class="cn-word" data-tr="baxt, omad">복</span>을 가져다 준다는 예쁜 복조리를 하나 사 들고 '소쇄원'으로 발걸음을 <span class="cn-word" data-pos="verb" data-tr="burdim, yoʻnaltirdim">돌렸다</span>.</p>
<p>차로 30분쯤 이동하니 한국의 <span class="cn-word" data-pos="adj" data-tr="eng mashhur, namunaviy">대표적인</span> 정원 소쇄원이 <span class="cn-word" data-pos="verb" data-tr="paydo boʻldi">나타났다</span>. 입구에 들어서면 대나무가 숲을 이루고 있고, 작은 계곡을 지나 안으로 들어가면 여러 건물과 <span class="cn-word" data-tr="shiypon, ayvon">정자</span>가 나타난다. 500년 전에 한 선비가 이 소쇄원을 <span class="cn-word" data-pos="verb" data-tr="qurib">지어</span> 놓고, 자신과 말이 통하는 사람과 이런저런 이야기를 나누면서 <span class="cn-word" data-tr="umrning qolgan qismi">여생</span>을 보냈다고 한다. 이곳에 만들어진 건물 하나하나, 꽃 한송이, 나무 한 그루 모두 선비의 마음이 <span class="cn-word" data-pos="verb" data-tr="singdirilgan, mujassam">담긴</span> 것이라 하니 <span class="cn-word" data-pos="adv" data-tr="sekin, shoshmasdan">천천히</span> 즐기면서 그 안에 담긴 정신을 느껴보고 싶었다.</p>
<p>소쇄원을 나와 우리는 담양에서 유명한 대통밥을 먹으러 식당으로 이동했다. 이름만 듣고는 어떤 밥일지 <span class="cn-word" data-pos="adv" data-tr="juda, gʻoyat">무척</span> <span class="cn-word" data-pos="adj" data-tr="qiziq, bilgim keldi">궁금했다</span>. 알고 보니 대통밥은 대나무 통에다 쌀을 넣고, 대추며 잣이며 밤 등을 넣어 쪄서 만든 밥이었는데, 대나무향이 나는 <span class="cn-word" data-pos="adj" data-tr="shirin">달콤한</span> 밥이 주변의 <span class="cn-word" data-tr="manzara">경치</span>와 <span class="cn-word" data-pos="verb" data-tr="mos kelib, uygʻunlashib">어울려</span> 더 맛있게 느껴졌다. 건강에 좋다는 대나무 음식을 먹었으니 이 <span class="cn-word" data-tr="jazirama issiq">무더위</span>도 다 <span class="cn-word" data-pos="verb" data-tr="yengib oʻtmoq">이겨낼</span> 수 있겠지? 밥을 먹고 나서 바로 집으로 돌아오기가 <span class="cn-word" data-pos="adj" data-tr="afsuslanarli">아쉬웠지만</span> 시간이 늦어 우리는 차에 올라타야 했다.</p>
<p>곧 담양의 대나무와 정원이 또 나를 부를 것 같다. 생각만 해도 마음이 <span class="cn-word" data-pos="verb" data-tr="xotirjam boʻladigan">편안해지는</span> 대나무 숲에서 옛 사람과 같은 마음을 다시 한 번 느끼고 싶다.</p>''',
        "questions": [
            {
                "text": "글쓴이가 담양에서 간 곳의 순서로 알맞은 것은 무엇입니까?",
                "choices": [
                    "소쇄원 → 죽녹원 → 식당",
                    "죽녹원 → 소쇄원 → 식당",
                    "식당 → 죽녹원 → 소쇄원",
                ],
                "answer": 1,
                "explanation": "Matnda avval 죽녹원ga borgan (\"우선 죽녹원으로 향했다\"), keyin 소쇄원ga (\"소쇄원으로 발걸음을 돌렸다\"), oxirida ovqatlanish uchun restoranga borgan. Tartibi: Jungnogwon → Soswewon → restoran.",
            },
            {
                "text": "한국에서 대나무가 선비의 굳은 의지에 비유되는 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "대나무로 여러 가지 물건을 만들 수 있어서",
                    "사계절 늘 푸르고 곧게 자라기 때문에",
                    "대나무 숲이 마음을 편안하게 해 주어서",
                ],
                "answer": 1,
                "explanation": "Matn boshida bambuk \"사계절 늘 푸르고 곧게 자라는\" (toʻrt fasl doim koʻm-koʻk va tik oʻsadigan) deb taʼriflanadi — aynan shu xususiyat olim-ziyolining qatʼiy irodasiga oʻxshatilishiga sabab.",
            },
            {
                "text": "이 글의 종류로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "여행을 다녀와서 쓴 기행문",
                    "대나무를 파는 광고문",
                    "담양의 역사를 설명하는 논설문",
                ],
                "answer": 0,
                "explanation": "Matn muallifning Damyangga qilgan sayohati — qayerga borgani, nimani koʻrgani va his-tuygʻulari haqida yozilgan sayohatnoma (기행문). Reklama yoki tarixiy maqola emas.",
            },
        ],
    },
    {
        "title":   "마음을 움직이는 공익 광고",
        "summary": "Ijtimoiy reklama odamlarning qarashini qanday oʻzgartiradi?",
        "order":   7,
        "grammar": [
            {
                "pattern":  "-는가 하면",
                "meaning":  "Baʼzilari ..., boshqalari esa ... (ikki tomonni qiyoslash).",
                "examples": ["소비하게 만드는 광고가 있는가 하면 생각하게 하는 광고도 있다.", "노는 사람이 있는가 하면 열심히 하는 사람도 있어요."],
            },
            {
                "pattern":  "-곤 하다",
                "meaning":  "...ib turmoq (takroriy odat yoki holat).",
                "examples": ["예전에는 딱딱한 표현을 사용하곤 했다.", "주말이면 산책을 하곤 해요."],
            },
            {
                "pattern":  "-는 데 그치지 않고",
                "meaning":  "... bilan cheklanmay, balki (bundan ortigʻini qiladi).",
                "examples": ["문제를 알리는 데 그치지 않고 해결책도 제시한다.", "듣는 데 그치지 않고 직접 실천했어요."],
            },
            {
                "pattern":  "-(으)ㄹ지라도",
                "meaning":  "...boʻlsa ham (yon berish, koʻpincha faraziy).",
                "examples": ["작은 일일지라도 구체적으로 알려 준다.", "실패할지라도 도전하겠어요."],
            },
        ],
        "body": '''<p>우리는 아침에 눈 뜨면서부터 잠자리에 들기까지 <span class="cn-word" data-pos="adj" data-tr="son-sanoqsiz, juda koʻp">수많은</span> 광고들을 <span class="cn-word" data-pos="verb" data-tr="duch kelmoq">접하게</span> 된다. 매일 보는 신문과 텔레비전은 물론이고, 거리를 걸어 다니거나 지하철이나 버스를 타도, 일을 하거나 공부를 하려고 컴퓨터를 켜도 <span class="cn-word" data-pos="adv" data-tr="shaksiz, muqarrar">여지없이</span> <span class="cn-word" data-pos="verb" data-tr="yogʻilib keladigan">쏟아지는</span> 광고를 만날 수 있다. 이러한 광고들 중에는 우리의 지갑을 열어 <span class="cn-word" data-tr="isteʼmol, xarid">소비</span>하게 만드는 것이 있는가 하면 우리가 <span class="cn-word" data-pos="adv" data-tr="beixtiyor">무심코</span> <span class="cn-word" data-pos="verb" data-tr="eʼtiborsiz oʻtib ketmoq">지나쳐</span> 버린 것들에 대해 <span class="cn-word" data-pos="adv" data-tr="birpas">잠깐</span> <span class="cn-word" data-pos="verb" data-tr="toʻxtab">멈춰</span> 생각하게 하는 광고도 있다. 후자가 바로 <span class="cn-word" data-tr="ijtimoiy reklama">공익 광고</span>이다.</p>
<p>공익 광고란 <span class="cn-word" data-tr="chekishni tashlash">금연</span>, 환경 보호, 청소년 문제 등과 같이 정부 기관이나 <span class="cn-word" data-tr="jamoat tashkiloti">공공 단체</span>가 공공의 이익을 위해 만든 광고를 말한다. 이러한 공익 광고는 기업들이 상품 판매를 위해서 하는 상품 광고와는 목적에서부터 차이가 있다. 공익 광고의 목적은 사회적 문제에 대해 사람들이 관심을 가져 줄 것을 <span class="cn-word" data-pos="verb" data-tr="chorlash, murojaat qilish">호소하거나</span> 공공의 이익을 <span class="cn-word" data-pos="verb" data-tr="intiladigan, koʻzlaydigan">추구하는</span> 방향으로 사람들의 태도를 <span class="cn-word" data-pos="verb" data-tr="oʻzgartiradigan">변화시키는</span> 데 있다.</p>
<p>이러한 목적을 <span class="cn-word" data-pos="verb" data-tr="erishmoq, amalga oshirmoq">이루기</span> 위해 <span class="cn-word" data-pos="adv" data-tr="ilgari, avvallari">예전에는</span> 공익 광고를 <span class="cn-word" data-pos="verb" data-tr="tayyorlamoq, ishlab chiqarmoq">제작할</span> 때 '에너지를 <span class="cn-word" data-pos="verb" data-tr="isrof qilmoq">낭비하지</span> 마세요', '쓰레기를 줄입시다'와 같은 광고 카피에서도 알 수 있듯이, <span class="cn-word" data-pos="adj" data-tr="toʻgʻridan-toʻgʻri">직접적이고</span> <span class="cn-word" data-pos="adj" data-tr="quruq, rasmiy">딱딱한</span> 표현들을 사용해 메시지를 전달하곤 했다. 그러나 이런 방법은 메시지를 <span class="cn-word" data-pos="adv" data-tr="aniq-ravshan">분명하게</span> 전달할 수 있었을지는 몰라도 보는 사람을 <span class="cn-word" data-pos="verb" data-tr="koyiyotgan">꾸짖는</span> 듯한 느낌을 주어 <span class="cn-word" data-tr="teskari natija">역효과</span>가 나타나기도 했다. 그래서 요즘에는 <span class="cn-word" data-pos="adv" data-tr="shunchaki, oddiygina">단순히</span> 메시지만 전달하는 데 그치지 않고 <span class="cn-word" data-pos="adj" data-tr="original, kutilmagan">기발한</span> 아이디어를 사용해 사람들이 그 문제에 대해 한 번 더 생각해 볼 수 있게 하는 광고들이 주를 이루고 있다. 뿐만 아니라 문제의 심각성만 <span class="cn-word" data-pos="verb" data-tr="anglatadigan, uygʻotadigan">일깨우는</span> 데 그치지 않고 그 문제를 <span class="cn-word" data-pos="verb" data-tr="hal qilmoq">해결하기</span> 위해 개인이 할 수 있는 작은 일일지라도 <span class="cn-word" data-pos="adv" data-tr="aniq, konkret">구체적으로</span> <span class="cn-word" data-pos="verb" data-tr="taqdim etmoq, koʻrsatmoq">제시해</span> 주고 있어 큰 효과를 얻게 되었다.</p>''',
        "questions": [
            {
                "text": "공익 광고와 상품 광고의 가장 큰 차이는 무엇입니까?",
                "choices": [
                    "공익 광고는 상품을 팔기 위한 것이다.",
                    "공익 광고는 공공의 이익을 위해 사람들의 태도를 바꾸려는 것이다.",
                    "공익 광고는 기업만 만들 수 있다.",
                ],
                "answer": 1,
                "explanation": "Matnda ijtimoiy reklama maqsadi \"공공의 이익을 위해 사람들의 태도를 변화시키는 데 있다\" deyilgan, tovar reklamasi esa mahsulot sotish uchun. Asosiy farq — maqsad.",
            },
            {
                "text": "예전의 공익 광고가 '역효과'를 낸 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "너무 재미있어서 메시지를 기억하지 못해서",
                    "직접적이고 딱딱한 표현이 보는 사람을 꾸짖는 느낌을 주어서",
                    "광고를 너무 적게 만들어서",
                ],
                "answer": 1,
                "explanation": "Matnda eski reklama \"직접적이고 딱딱한 표현\" ishlatgani uchun tomoshabinni koyiyotgandek his uygʻotgani va shu sabab teskari natija bergani aytilgan.",
            },
            {
                "text": "요즘 공익 광고의 특징으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "문제의 심각성만 강하게 알려 준다.",
                    "기발한 아이디어로 생각하게 하고, 개인이 할 수 있는 일도 구체적으로 알려 준다.",
                    "되도록 광고를 짧고 단순하게 만든다.",
                ],
                "answer": 1,
                "explanation": "Oxirgi xatboshida hozirgi reklamalar original gʻoyalar bilan oʻylantirishi va muammoni hal qilish uchun shaxs qila oladigan aniq ishlarni koʻrsatishi aytilgan. Faqat jiddiylikni uqtirish — eski usul.",
            },
        ],
    },
]
