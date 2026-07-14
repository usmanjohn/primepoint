# Wonder Readings — 10 fun "wow-facts" short stories (Claude-authored, engaging topics:
# space, nature, the world). A SEPARATE collection from the TOPIK-style ones — the goal is
# ENJOYMENT, not exam prep. Story text = Korean, all glosses = Uzbek. Style: STYLE_GUIDE_CORNER.md
# (short passages → ~10-12 vocab marks, 2 grammar points, 2-3 inference questions).
# Import: python manage.py import_corner corner/management/commands/_stories_wonders_1_10.py --author=<AUTHOR>

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
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "우주의 냄새",
        "summary": "Koinotning oʻzi vakuum boʻlsa-da, kosmosdan qaytgan astronavtlar skafandrlaridan gʻalati hid kelishini aytishadi.",
        "order":   1,
        "body": '''<p>우주는 <span class="cn-word" data-tr="vakuum, boʻshliq">진공</span> 상태이기 때문에 그 안에서는 냄새를 맡을 수 없다. 하지만 <span class="cn-word" data-pos="adv" data-tr="hayratlanarlisi shundaki">놀랍게도</span>, 우주에서 <span class="cn-word" data-tr="vazifa, missiya">임무</span>를 마치고 돌아온 우주 비행사들은 자신의 <span class="cn-word" data-tr="skafandr">우주복</span>에서 <span class="cn-word" data-pos="adj" data-tr="oʻziga xos">독특한</span> 냄새가 난다고 <span class="cn-word" data-pos="adv" data-tr="bir ovozdan">입을 모아</span> 말한다.</p>
<p>그들의 <span class="cn-word" data-tr="guvohlik, aytishlari">증언</span><strong>에 따르면</strong>, 그 냄새는 마치 <span class="cn-word" data-pos="verb" data-tr="yonayotgandek">타는</span> 듯한 금속이나 화약, 혹은 구운 고기 냄새와 <span class="cn-word" data-pos="adj" data-tr="oʻxshash">비슷하다</span>고 한다. 과학자들은 이 <span class="cn-word" data-pos="adj" data-tr="sirli">신비로운</span> 냄새의 <span class="cn-word" data-tr="asl mohiyati, tabiati">정체</span>가 멀리서 죽어 가는 별들이 <span class="cn-word" data-pos="verb" data-tr="chiqaradigan, purkaydigan">내뿜는</span> 고에너지 입자 때문일 것이라고 <span class="cn-word" data-pos="verb" data-tr="taxmin qiladi">추측한다</span>. 즉, 우리가 맡는 그 냄새는 사실 수십억 년 전에 사라진 별의 <span class="cn-word" data-tr="iz, asorat">흔적</span>인 <strong>셈이다</strong>.</p>''',
        "grammar": [
            {
                "pattern":  "-에 따르면",
                "meaning":  "Manbaga tayanish: ...ga koʻra, ...ning aytishicha (guvohlik, tadqiqot va h.k.).",
                "examples": ["우주 비행사들의 증언에 따르면 냄새가 난다고 한다.", "일기 예보에 따르면 내일 비가 온대요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 셈이다",
                "meaning":  "Xulosa/hisob-kitob: aslida ... boʻlib chiqadi, demak ... degan gap.",
                "examples": ["사라진 별의 흔적을 맡는 셈이다.", "이 정도면 다 끝난 셈이에요."],
            },
        ],
        "questions": [
            {
                "text": "우주 비행사들이 우주복에서 맡았다고 하는 냄새로 알맞은 것은 무엇입니까?",
                "choices": [
                    "달콤한 꽃과 과일 냄새",
                    "타는 듯한 금속이나 화약 냄새",
                    "시원한 바닷바람 냄새",
                ],
                "answer": 1,
                "explanation": "Matnda hid \"타는 듯한 금속이나 화약, 혹은 구운 고기 냄새\"ga oʻxshashi aytilgan. Gul yoki dengiz hidi haqida gap yoʻq.",
            },
            {
                "text": "과학자들이 추측하는 이 냄새의 원인은 무엇입니까?",
                "choices": [
                    "우주선의 오래된 연료",
                    "우주 비행사들이 먹은 음식",
                    "죽어 가는 별들이 내뿜는 고에너지 입자",
                ],
                "answer": 2,
                "explanation": "Olimlar hidning sababi uzoqdagi oʻlayotgan yulduzlar chiqaradigan yuqori energiyali zarralar boʻlishi mumkin deb taxmin qiladi.",
            },
            {
                "text": "이 글을 통해 알 수 있는 사실로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "우주 공간 자체에서는 냄새를 직접 맡을 수 없다.",
                    "우주에서는 누구나 쉽게 냄새를 맡을 수 있다.",
                    "우주복에서는 아무런 냄새도 나지 않는다.",
                ],
                "answer": 0,
                "explanation": "Koinot vakuum boʻlgani uchun hidni bevosita hidlab boʻlmaydi; hid faqat skafandrga singib qoladi. Shuning uchun birinchi variant toʻgʻri.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "우리는 별의 먼지",
        "summary": "Tanamizdagi atomlar milliardlab yil avval yulduzlar ichida yaratilgan — biz tom maʼnoda yulduz changidanmiz.",
        "order":   2,
        "body": '''<p>우리 몸을 <span class="cn-word" data-pos="verb" data-tr="tashkil qiladigan">이루는</span> <span class="cn-word" data-tr="element, unsur">원소</span>들은 어디에서 왔을까? 놀랍게도, 우리 몸속의 탄소와 산소, <span class="cn-word" data-tr="temir">철분</span> 같은 물질들은 <span class="cn-word" data-pos="adv" data-tr="aslida, dastlab">원래</span> 별의 내부에서 만들어졌다. <span class="cn-word" data-pos="adj" data-tr="juda uzoq, qadim">까마득한</span> 옛날, 거대한 별들은 자신의 <span class="cn-word" data-tr="umr, yashash muddati">수명</span>이 다하면 엄청난 <span class="cn-word" data-tr="portlash">폭발</span>을 일으켰다.</p>
<p>이 폭발을 <strong>통해</strong> 별 속에 <span class="cn-word" data-pos="verb" data-tr="qamalgan, tiqilib qolgan">갇혀</span> 있던 원소들이 우주 공간으로 <span class="cn-word" data-pos="verb" data-tr="sochilib ketdi">흩어졌고</span>, 오랜 <span class="cn-word" data-tr="vaqt, yillar">세월</span><strong>에 걸쳐</strong> 이들이 <span class="cn-word" data-pos="verb" data-tr="jipslashib, birlashib">뭉쳐</span> 지구와 생명체를 만들었다. 그러니 밤하늘의 별을 올려다볼 때, 우리는 <span class="cn-word" data-pos="adv" data-tr="aslida, amalda">사실상</span> <span class="cn-word" data-tr="qarindosh">친척</span>을 바라보고 있는 셈이다. 우리 모두는 <span class="cn-word" data-pos="verb" data-tr="yaltiraydigan">반짝이는</span> 별의 먼지에서 <span class="cn-word" data-pos="verb" data-tr="tugʻilgan">태어난</span> 존재인 것이다.</p>''',
        "grammar": [
            {
                "pattern":  "-을/를 통해(서)",
                "meaning":  "Vosita/yoʻl: ... orqali, ... yordamida (biror natijaga erishiladi).",
                "examples": ["폭발을 통해 원소들이 우주로 흩어졌다.", "책을 통해 많은 것을 배웠어요."],
            },
            {
                "pattern":  "-에 걸쳐",
                "meaning":  "Davomiylik: ... davomida, ... boʻyi (uzoq vaqt yoki keng miqyosda).",
                "examples": ["오랜 세월에 걸쳐 원소들이 뭉쳤다.", "삼 일에 걸쳐 회의가 진행되었습니다."],
            },
        ],
        "questions": [
            {
                "text": "우리 몸속의 원소들이 처음 만들어진 곳은 어디입니까?",
                "choices": ["바다 깊은 곳", "별의 내부", "지구의 땅속"],
                "answer": 1,
                "explanation": "Matnda tanamizdagi uglerod, kislorod, temir kabi moddalar \"별의 내부에서 만들어졌다\" (yulduz ichida yaratilgan) deb aytilgan.",
            },
            {
                "text": "별 속의 원소들이 우주로 흩어지게 된 계기는 무엇입니까?",
                "choices": [
                    "별이 수명을 다해 크게 폭발했을 때",
                    "다른 별과 충돌했을 때",
                    "태양이 새로 태어났을 때",
                ],
                "answer": 0,
                "explanation": "Ulkan yulduzlar umri tugagach katta portlash sodir etadi va shu portlash orqali elementlar koinotga sochiladi.",
            },
            {
                "text": "글쓴이가 별을 ‘친척’이라고 표현한 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "별이 사람처럼 생겼기 때문에",
                    "우리 몸과 별이 같은 원소로 이루어져 있기 때문에",
                    "별이 우리를 지켜보고 있기 때문에",
                ],
                "answer": 1,
                "explanation": "Tanamiz ham, yulduzlar ham bir xil elementlardan tashkil topgani uchun muallif yulduzni ‘qarindosh’ deb ataydi.",
            },
        ],
    },
    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "점점 길어지는 하루",
        "summary": "Oyning tortishishi Yerning aylanishini sekinlashtiradi — shu sabab har bir kun juda oz miqdorda uzayib bormoqda.",
        "order":   3,
        "body": '''<p>하루는 <span class="cn-word" data-pos="adv" data-tr="doim, hamisha">언제나</span> 24시간으로 <span class="cn-word" data-pos="adj" data-tr="bir xil, oʻzgarmas">일정할까</span>? 사실 지구의 하루는 아주 <span class="cn-word" data-pos="adv" data-tr="ozgina, asta-sekin">조금씩</span> <span class="cn-word" data-pos="verb" data-tr="uzayib bormoqda">길어지고</span> 있다. 그 <span class="cn-word" data-tr="aybdor">범인</span>은 바로 달이다. 달의 <span class="cn-word" data-tr="tortishish kuchi">중력</span>은 바닷물을 끌어당겨 <span class="cn-word" data-tr="qalqish va qaytish (suv)">밀물과 썰물</span>을 만드는데, 이 과정에서 지구의 <span class="cn-word" data-tr="oʻz oʻqi atrofida aylanishi">자전</span> 속도를 아주 조금씩 <span class="cn-word" data-pos="verb" data-tr="sekinlashtiradi">늦춘다</span>.</p>
<p>그 정도는 100년에 약 1.7 밀리초로, 하루아침에 <span class="cn-word" data-pos="verb" data-tr="sezilarli">느껴질</span> <strong>만한</strong> 변화는 아니다. 하지만 <span class="cn-word" data-pos="adj" data-tr="juda uzoq, olis">아득한</span> 옛날에는 <span class="cn-word" data-tr="ahvol, vaziyat">사정</span>이 달랐다. <span class="cn-word" data-tr="dinozavr">공룡</span>이 <strong>살던</strong> 시절, 지구의 하루는 지금보다 짧은 약 23시간이었다고 한다. 지금 이 순간에도 우리의 하루는 <span class="cn-word" data-pos="adv" data-tr="sassiz, bilinmasdan">소리 없이</span> 늘어나고 있는 것이다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 만하다",
                "meaning":  "Arziydigan / yetarli daraja: ...gulik, ...sa arziydigan, ... deyishga loyiq.",
                "examples": ["하루아침에 느껴질 만한 변화는 아니다.", "이 영화는 한번 볼 만해요."],
            },
            {
                "pattern":  "-던",
                "meaning":  "Oʻtmishda davom etgan/tugallanmagan holatni eslash: (oʻsha paytdagi) ...-ayotgan, ...-adigan.",
                "examples": ["공룡이 살던 시절에는 하루가 더 짧았다.", "제가 자주 가던 카페가 문을 닫았어요."],
            },
        ],
        "questions": [
            {
                "text": "지구의 하루가 점점 길어지는 원인은 무엇입니까?",
                "choices": [
                    "태양의 빛이 점점 강해지기 때문에",
                    "달의 중력이 지구의 자전 속도를 늦추기 때문에",
                    "지구가 점점 커지고 있기 때문에",
                ],
                "answer": 1,
                "explanation": "Oyning tortishish kuchi suvni tortib, qalqish-qaytish hosil qiladi va shu jarayonda Yerning aylanishini sekinlashtiradi.",
            },
            {
                "text": "공룡이 살던 시절의 하루 길이에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "지금과 똑같이 24시간이었다.",
                    "지금보다 긴 약 25시간이었다.",
                    "지금보다 짧은 약 23시간이었다.",
                ],
                "answer": 2,
                "explanation": "Matnda dinozavrlar davrida Yer kuni hozirgidan qisqa, taxminan 23 soat boʻlgani aytilgan.",
            },
            {
                "text": "이 글의 내용과 같은 것을 고르십시오.",
                "choices": [
                    "하루의 길이는 영원히 변하지 않는다.",
                    "하루의 길이는 고정된 것이 아니라 조금씩 변하고 있다.",
                    "하루의 길이는 100년마다 한 시간씩 늘어난다.",
                ],
                "answer": 1,
                "explanation": "Kun uzunligi qatʼiy emas — juda oz miqdorda boʻlsa-da doimo oʻzgarib boradi. Oʻzgarish 100 yilda atigi 1.7 millisekund, soatlab emas.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "세상에서 가장 조용한 방",
        "summary": "Tovushni deyarli toʻliq yutadigan xonada oʻz yurak urishingizni eshitasiz — va koʻpchilik uni bir soatdan ortiq koʻtara olmaydi.",
        "order":   4,
        "body": '''<p>세상에서 가장 <span class="cn-word" data-pos="adj" data-tr="jimjit, tinch">조용한</span> 방에 들어가면 어떤 기분이 들까? 미국의 한 <span class="cn-word" data-tr="ilmiy tadqiqot markazi">연구소</span>에는 소리를 99.99%까지 <span class="cn-word" data-pos="verb" data-tr="yutadigan">흡수하는</span> 특별한 방이 있다. ‘<span class="cn-word" data-tr="akssiz xona">무향실</span>’이라고 불리는 이곳은 너무나 조용해서 <span class="cn-word" data-pos="adv" data-tr="aksincha">오히려</span> <span class="cn-word" data-pos="verb" data-tr="chidash, bardosh berish">견디기</span> 힘든 공간으로 알려져 있다.</p>
<p>이 방에서는 밖에서 들리던 <span class="cn-word" data-tr="shovqin">소음</span>이 완전히 사라지기 때문에, 대신 자신의 심장 뛰는 소리와 피가 <span class="cn-word" data-pos="verb" data-tr="oqadigan">흐르는</span> 소리까지 <span class="cn-word" data-pos="adv" data-tr="jonli, aniq-ravshan">생생하게</span> 들린다. <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> 어떤 사람은 <span class="cn-word" data-tr="yoʻnalish hissi">방향 감각</span>을 잃고 <span class="cn-word" data-tr="bosh aylanishi">어지러움</span>을 느끼<strong>기도 한다</strong>. 지금까지 이 방에서 가장 오래 <span class="cn-word" data-pos="verb" data-tr="chidagan, dosh bergan">버틴</span> 기록은 겨우 한 시간 <span class="cn-word" data-pos="adv" data-tr="chamasi, atrofida">남짓</span>이라고 하니, 완벽한 <span class="cn-word" data-tr="sukunat, jimlik">고요</span>가 반드시 <span class="cn-word" data-tr="qulaylik, rohat">편안함</span>을 뜻하는 <strong>것은 아닌</strong> 셈이다.</p>''',
        "grammar": [
            {
                "pattern":  "-기도 하다",
                "meaning":  "Baʼzan/ham: goho ... ham qiladi/boʻladi (bir imkoniyatni qoʻshimcha aytish).",
                "examples": ["어떤 사람은 어지러움을 느끼기도 한다.", "주말에는 집에서 쉬기도 해요."],
            },
            {
                "pattern":  "-는 것은 아니다",
                "meaning":  "Qisman inkor: har doim ham ... degani emas, ... boʻlishi shart emas.",
                "examples": ["완벽한 고요가 반드시 편안함을 뜻하는 것은 아니다.", "비싸다고 다 좋은 것은 아니에요."],
            },
        ],
        "questions": [
            {
                "text": "‘무향실’의 특징으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "음악을 크게 들려주는 방이다.",
                    "소리를 거의 완전히 흡수해 매우 조용한 방이다.",
                    "소리가 크게 울리는 방이다.",
                ],
                "answer": 1,
                "explanation": "Muhyangsil tovushni 99.99% gacha yutadi, shuning uchun juda jimjit boʻladi.",
            },
            {
                "text": "무향실 안에서 사람들이 듣게 되는 소리로 알맞은 것은 무엇입니까?",
                "choices": [
                    "밖에서 들려오는 자동차 소리",
                    "자신의 심장 소리와 피가 흐르는 소리",
                    "옆방 사람들의 대화 소리",
                ],
                "answer": 1,
                "explanation": "Tashqi shovqin butunlay yoʻqolgani uchun odam oʻz yuragi urishi va qon oqishi tovushini eshitadi.",
            },
            {
                "text": "이 글이 궁극적으로 말하려는 것은 무엇입니까?",
                "choices": [
                    "완벽한 고요가 반드시 편안한 것은 아니다.",
                    "조용한 방은 누구에게나 가장 편안하다.",
                    "소음은 사람에게 아무런 영향을 주지 않는다.",
                ],
                "answer": 0,
                "explanation": "Odamlar bu jimlikka bir soatdan ortiq chiday olmaydi — demak mukammal sukunat har doim ham rohat degani emas.",
            },
        ],
    },
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "심장이 셋인 동물, 문어",
        "summary": "Sakkizoyoqning uchta yuragi va koʻk qoni bor — va suzganda asosiy yuragi toʻxtab, tez charchaydi.",
        "order":   5,
        "body": '''<p><span class="cn-word" data-tr="sakkizoyoq">문어</span>는 우리가 생각하는 것보다 훨씬 <span class="cn-word" data-pos="adj" data-tr="qiziq, ajoyib">신기한</span> 동물이다. 놀랍게도 문어의 심장은 하나가 아니라 <span class="cn-word" data-pos="adv" data-tr="naq, hatto">무려</span> 세 <strong>개나 된다</strong>. 두 개의 심장은 <span class="cn-word" data-tr="jabra">아가미</span>로 피를 <span class="cn-word" data-pos="verb" data-tr="yuboradi">보내고</span>, 나머지 하나는 <span class="cn-word" data-tr="butun tana">온몸</span>으로 피를 <span class="cn-word" data-pos="verb" data-tr="yetkazib beradi">공급한다</span>. 게다가 문어의 피는 붉은색이 아니라 <span class="cn-word" data-tr="koʻk rang">푸른색</span>을 <span class="cn-word" data-pos="verb" data-tr="oladi, kasb etadi">띤다</span>.</p>
<p>피가 푸른 이유는 <span class="cn-word" data-tr="tarkib">성분</span>에 있다. 사람의 피는 철분 때문에 붉지만, 문어의 피에는 <span class="cn-word" data-tr="mis">구리</span> 성분이 들어 있어 푸르게 보이는 것이다. 재미있는 점은, 문어가 <span class="cn-word" data-pos="verb" data-tr="suzganda">헤엄칠</span> 때는 온몸에 피를 보내는 심장이 <span class="cn-word" data-pos="adv" data-tr="birpas, vaqtincha">잠시</span> <span class="cn-word" data-pos="verb" data-tr="toʻxtaydi">멈춘다</span>는 것이다. 그래서 문어는 쉽게 <span class="cn-word" data-pos="verb" data-tr="charchaydi">지쳐</span>, <strong>헤엄치기보다</strong> 바닥을 <span class="cn-word" data-pos="verb" data-tr="oʻrmalab">기어</span> 다니는 것을 더 좋아한다.</p>''',
        "grammar": [
            {
                "pattern":  "-(이)나 되다",
                "meaning":  "Kutilganidan koʻp ekanini taʼkidlash: naq ..., ...cha (miqdorning koʻpligiga urgʻu).",
                "examples": ["문어의 심장은 세 개나 된다.", "그 책을 다섯 번이나 읽었어요."],
            },
            {
                "pattern":  "-기보다(는)",
                "meaning":  "...dan koʻra (afzallik): ikki narsadan ikkinchisi afzal koʻriladi.",
                "examples": ["문어는 헤엄치기보다 기어 다니는 것을 좋아한다.", "말하기보다는 듣는 편이에요."],
            },
        ],
        "questions": [
            {
                "text": "문어의 피가 푸른색을 띠는 이유는 무엇입니까?",
                "choices": [
                    "피에 철분이 많이 들어 있어서",
                    "피에 구리 성분이 들어 있어서",
                    "바닷물의 색이 비쳐서",
                ],
                "answer": 1,
                "explanation": "Odam qoni temir tufayli qizil, sakkizoyoq qonida esa mis boʻlgani uchun u koʻk koʻrinadi.",
            },
            {
                "text": "문어가 헤엄치기보다 바닥을 기어 다니는 것을 좋아하는 이유는 무엇입니까?",
                "choices": [
                    "헤엄칠 때 온몸에 피를 보내는 심장이 멈춰 쉽게 지치기 때문에",
                    "바닥에 먹이가 더 많기 때문에",
                    "물이 너무 차갑기 때문에",
                ],
                "answer": 0,
                "explanation": "Suzganda butun tanaga qon yuboruvchi yurak toʻxtaydi, shu sabab sakkizoyoq tez charchaydi va oʻrmalashni afzal koʻradi.",
            },
            {
                "text": "이 글의 내용과 같은 것을 고르십시오.",
                "choices": [
                    "문어는 심장이 하나뿐이다.",
                    "문어의 심장은 모두 세 개다.",
                    "문어의 피는 사람과 똑같이 붉은색이다.",
                ],
                "answer": 1,
                "explanation": "Matnda sakkizoyoqning yuragi uchta ekani aniq aytilgan; qoni esa koʻk rangda.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "왜 우리는 꿈을 잊을까?",
        "summary": "Har kecha tush koʻramiz, lekin uygʻongach 90% dan koʻpini unutamiz — miya tushni saqlashga arzimaydi deb ‘hisoblaydi’.",
        "order":   6,
        "body": '''<p>우리는 매일 밤 <span class="cn-word" data-tr="tush">꿈</span>을 꾸지만, 아침에 <span class="cn-word" data-pos="verb" data-tr="uygʻonsak">눈을 뜨면</span> 대부분 기억나지 않는다. 연구에 따르면 사람은 잠에서 깬 지 몇 분 만에 꿈의 90% 이상을 <span class="cn-word" data-pos="verb" data-tr="unutib qoʻyadi">잊어버린다</span>고 한다. 밤새 <span class="cn-word" data-pos="adj" data-tr="jonli, yorqin">생생했던</span> 이야기가 <span class="cn-word" data-pos="adv" data-tr="bir zumda">순식간에</span> <span class="cn-word" data-pos="adv" data-tr="izsiz">흔적도 없이</span> 사라지는 것이다.</p>
<p>과학자들은 그 이유를 <span class="cn-word" data-tr="miya">뇌</span>의 화학 물질에서 찾는다. 기억을 <span class="cn-word" data-pos="verb" data-tr="saqlaydigan">저장하는</span> 데 <span class="cn-word" data-pos="adj" data-tr="zarur, kerakli">필요한</span> 물질이 꿈을 꾸는 동안에는 <span class="cn-word" data-pos="adj" data-tr="yetishmaydigan">부족하기</span> 때문이다. 즉, 우리의 뇌는 꿈을 <span class="cn-word" data-pos="adv" data-tr="ataylab, zarurat boʻlmasa">굳이</span> <strong>기억할 필요가 없다고</strong> <span class="cn-word" data-pos="verb" data-tr="hisoblaydi, qaror qiladi">판단하는</span> 셈이다. 만약 꿈을 <span class="cn-word" data-pos="verb" data-tr="ushlab qolmoq">붙잡고</span> 싶다면, 잠에서 <strong>깨자마자</strong> <span class="cn-word" data-pos="adv" data-tr="tez, darrov">재빨리</span> 적어 두는 것이 좋다.</p>''',
        "grammar": [
            {
                "pattern":  "-자마자",
                "meaning":  "Zudlik: ...boʻlishi bilanoq, ...gan zahoti (ikkinchi ish darrov boʻladi).",
                "examples": ["잠에서 깨자마자 꿈을 적어 두세요.", "집에 도착하자마자 잠이 들었어요."],
            },
            {
                "pattern":  "-(으)ㄹ 필요가 없다",
                "meaning":  "Zaruriyat yoʻqligi: ...ish shart emas, ...ga hojat yoʻq.",
                "examples": ["뇌는 꿈을 굳이 기억할 필요가 없다.", "그렇게 걱정할 필요가 없어요."],
            },
        ],
        "questions": [
            {
                "text": "사람들이 꿈을 잊는 것에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "꿈은 며칠이 지나야 겨우 잊힌다.",
                    "잠에서 깬 지 몇 분 만에 꿈의 90% 이상을 잊는다.",
                    "사람은 꿈을 거의 잊지 않고 다 기억한다.",
                ],
                "answer": 1,
                "explanation": "Matnda odam uygʻongandan bir necha daqiqa ichida tushning 90% dan koʻpini unutishi aytilgan.",
            },
            {
                "text": "과학자들이 밝힌, 사람이 꿈을 잘 기억하지 못하는 이유는 무엇입니까?",
                "choices": [
                    "꿈을 꾸는 동안 기억 저장에 필요한 물질이 부족하기 때문에",
                    "꿈이 너무 짧게 끝나기 때문에",
                    "잠을 충분히 자지 못하기 때문에",
                ],
                "answer": 0,
                "explanation": "Tush koʻrayotgan paytda xotira saqlashga kerak boʻlgan modda yetishmaydi, shu sabab tush eslab qolinmaydi.",
            },
            {
                "text": "꿈을 기억하고 싶을 때 도움이 되는 방법으로 이 글에서 제시한 것은 무엇입니까?",
                "choices": [
                    "잠들기 전에 물을 많이 마신다.",
                    "잠에서 깨자마자 재빨리 적어 둔다.",
                    "매일 같은 시간에 잠을 잔다.",
                ],
                "answer": 1,
                "explanation": "Matnda tushni eslab qolish uchun uygʻongan zahoti tez yozib qoʻyish tavsiya qilingan.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "초록빛 사하라",
        "summary": "Bugungi cheksiz qumli Sahara bir necha ming yil avval koʻllar va daryolarga toʻla yashil dasht boʻlgan.",
        "order":   7,
        "body": '''<p>세계에서 가장 큰 <span class="cn-word" data-tr="choʻl, sahro">사막</span>인 사하라가 <span class="cn-word" data-pos="adv" data-tr="aslida, dastlab">원래</span>는 <span class="cn-word" data-pos="adj" data-tr="yashil, koʻm-koʻk">푸른</span> <span class="cn-word" data-tr="dasht, yaylov">초원</span>이었다면 믿을 수 있을까? 지금은 <span class="cn-word" data-pos="adv" data-tr="cheksiz">끝없이</span> <span class="cn-word" data-pos="adj" data-tr="qaqragan, quruq">메마른</span> 모래로 <span class="cn-word" data-pos="verb" data-tr="qoplangan">뒤덮여</span> 있지만, 약 수천 년 전만 해도 이곳에는 <span class="cn-word" data-tr="koʻl">호수</span>와 강이 흐르고 <span class="cn-word" data-tr="begemot">하마</span>가 살았다.</p>
<p>실제로 사하라의 <span class="cn-word" data-tr="gʻor">동굴</span> 벽에서는 <span class="cn-word" data-pos="verb" data-tr="suzayotgan">수영하는</span> 사람들의 그림이 발견되기도 했다. 사막 한가운데에서 <strong>수영이라니</strong>, <span class="cn-word" data-pos="verb" data-tr="tasavvur qilish">상상</span>하기 어려운 일이다. 학자들은 지구의 <span class="cn-word" data-tr="qiyalik, ogʻish">기울기</span>가 조금씩 <strong><span class="cn-word" data-pos="verb" data-tr="oʻzgargani sari">변하면서</span></strong> 비구름의 <span class="cn-word" data-tr="oqim, harakat">흐름</span>이 바뀌었고, 그 결과 초원이 사막으로 변했다고 설명한다. 그리고 먼 미래에는 사하라가 다시 초록빛을 <span class="cn-word" data-pos="verb" data-tr="qaytarib oladigan">되찾을</span> 것이라고 한다.</p>''',
        "grammar": [
            {
                "pattern":  "-(이)라니",
                "meaning":  "Hayrat/ishonqiramaslik: ...ekan-a!, ... deganingmi? (kutilmagan narsaga taajjub).",
                "examples": ["사막 한가운데에서 수영이라니, 믿기 어렵다.", "그가 벌써 떠났다니 정말 놀랍다."],
            },
            {
                "pattern":  "-(으)면서",
                "meaning":  "Bir vaqtda / ...gani sari (ikki holat birga yuz beradi yoki sabab-oqibat).",
                "examples": ["지구의 기울기가 변하면서 기후도 바뀌었다.", "음악을 들으면서 공부해요."],
            },
        ],
        "questions": [
            {
                "text": "아주 먼 옛날 사하라의 모습으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "지금처럼 메마른 모래사막이었다.",
                    "호수와 강이 있고 하마가 사는 푸른 초원이었다.",
                    "온통 눈과 얼음으로 뒤덮인 땅이었다.",
                ],
                "answer": 1,
                "explanation": "Matnda bir necha ming yil avval Saharada koʻl va daryolar boʻlib, begemotlar yashagani — yaʼni u yashil dasht boʻlgani aytilgan.",
            },
            {
                "text": "사하라가 초원에서 사막으로 변한 원인은 무엇입니까?",
                "choices": [
                    "사람들이 나무를 모두 베어서",
                    "지구의 기울기가 변해 비구름의 흐름이 바뀌어서",
                    "큰 화산이 폭발해서",
                ],
                "answer": 1,
                "explanation": "Olimlar Yer oʻqi qiyaligi asta-sekin oʻzgarib, yomgʻir bulutlari harakati oʻzgargani sabab dasht choʻlga aylandi deb tushuntiradi.",
            },
            {
                "text": "사하라 동굴 벽에 있는 수영하는 사람들의 그림이 알려 주는 사실은 무엇입니까?",
                "choices": [
                    "과거 그곳에 물이 많아 사람들이 수영을 했다.",
                    "옛날 사람들은 그림 그리기를 좋아했다.",
                    "그림은 최근에 만들어진 것이다.",
                ],
                "answer": 0,
                "explanation": "Choʻl oʻrtasida suzuvchilar rasmi — oʻsha davrda u yerda suv koʻp boʻlganini, yaʼni Sahara yashil boʻlganini koʻrsatadi.",
            },
        ],
    },
    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "목성에는 다이아몬드 비가 내린다",
        "summary": "Yupiter va Saturnda chaqmoq metanni uglerodga aylantiradi, u ulkan bosim ostida olmosga aylanib yogʻishi mumkin.",
        "order":   8,
        "body": '''<p><span class="cn-word" data-tr="Yupiter (sayyora)">목성</span>과 <span class="cn-word" data-tr="Saturn (sayyora)">토성</span>에서는 <span class="cn-word" data-pos="adv" data-tr="chinakamiga, rostdan">진짜</span> 다이아몬드 비가 <strong><span class="cn-word" data-pos="verb" data-tr="yogʻishi mumkin">내릴지도 모른다</span></strong>. 다소 <span class="cn-word" data-pos="adv" data-tr="gʻalati, aqlbovar qilmas tarzda">황당하게</span> 들리지만, 이는 과학자들이 <span class="cn-word" data-pos="adv" data-tr="jiddiy">진지하게</span> <span class="cn-word" data-pos="verb" data-tr="ilgari surgan">제시한</span> <span class="cn-word" data-tr="faraz, gipoteza">가설</span>이다. 이 <span class="cn-word" data-pos="adj" data-tr="ulkan, bahaybat">거대한</span> 행성에는 <span class="cn-word" data-tr="chaqmoq">번개</span>가 자주 <span class="cn-word" data-pos="verb" data-tr="uradigan">치는데</span>, 이 번개가 대기 중의 <span class="cn-word" data-tr="metan">메탄</span>을 <span class="cn-word" data-pos="adv" data-tr="maydalab">잘게</span> 부수어 <span class="cn-word" data-tr="uglerod">탄소</span>로 바꾼다.</p>
<p>이렇게 만들어진 탄소 <span class="cn-word" data-tr="kukun, changcha">가루</span>는 행성 깊은 곳으로 <span class="cn-word" data-pos="verb" data-tr="tusha borib">떨어지면서</span> <span class="cn-word" data-pos="adj" data-tr="juda katta">엄청난</span> <span class="cn-word" data-tr="bosim">압력</span>을 받는다. 바로 이 압력이 탄소를 단단한 다이아몬드로 <span class="cn-word" data-pos="verb" data-tr="aylantirib qoʻyadi">바꾸어</span> <strong>놓는</strong> 것이다. 물론 아직 직접 <span class="cn-word" data-pos="verb" data-tr="tasdiqlangan">확인된</span> 것은 아니지만, 우주 어딘가에 다이아몬드가 <span class="cn-word" data-pos="verb" data-tr="quyiladigan, yogʻiladigan">쏟아지는</span> 세계가 있다는 상상만으로도 가슴이 뛴다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ지도 모르다",
                "meaning":  "Ehtimollik: ... boʻlishi ham mumkin (aniq emas, taxmin).",
                "examples": ["목성에는 다이아몬드 비가 내릴지도 모른다.", "지금 가면 그를 만날 수 있을지도 몰라요."],
            },
            {
                "pattern":  "-아/어 놓다",
                "meaning":  "Ishni bajarib, natijasini shu holatda qoldirish: ...ib qoʻymoq.",
                "examples": ["압력이 탄소를 다이아몬드로 바꾸어 놓는다.", "미리 표를 사 놓았어요."],
            },
        ],
        "questions": [
            {
                "text": "목성과 토성에서 다이아몬드가 만들어지는 과정의 시작으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "번개가 대기 중의 메탄을 탄소로 바꾼다.",
                    "태양열이 얼음을 녹인다.",
                    "운석이 행성에 부딪친다.",
                ],
                "answer": 0,
                "explanation": "Jarayon chaqmoq atmosferadagi metanni maydalab uglerodga aylantirishdan boshlanadi.",
            },
            {
                "text": "탄소가 단단한 다이아몬드로 변하는 데 결정적인 역할을 하는 것은 무엇입니까?",
                "choices": [
                    "행성 깊은 곳의 엄청난 압력",
                    "행성의 차가운 온도",
                    "강한 바람",
                ],
                "answer": 0,
                "explanation": "Uglerod changi sayyora chuqurligiga tushib, ulkan bosim ostida qattiq olmosga aylanadi.",
            },
            {
                "text": "이 글의 내용에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "이미 다이아몬드 비가 직접 확인되었다.",
                    "아직 직접 확인되지는 않은 과학적 가설이다.",
                    "과학자들이 농담으로 지어낸 이야기이다.",
                ],
                "answer": 1,
                "explanation": "Matnda bu hali bevosita tasdiqlanmagan, ammo olimlar jiddiy ilgari surgan ilmiy faraz ekani aytilgan.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "꿀은 절대 상하지 않는다",
        "summary": "Arxeologlar Misr maqbaralaridan 3000 yillik asalni topgan — u hali ham yeyishga yaroqli edi.",
        "order":   9,
        "body": '''<p>냉장고에 <strong>넣지 않아도</strong> 수천 년 동안 <span class="cn-word" data-pos="verb" data-tr="buziladigan, aynaydigan">상하지</span> 않는 음식이 있다. 바로 <span class="cn-word" data-tr="asal">꿀</span>이다. 실제로 <span class="cn-word" data-tr="arxeolog">고고학자</span>들은 <span class="cn-word" data-tr="Misr">이집트</span>의 <span class="cn-word" data-tr="qabr, maqbara">무덤</span>에서 3천 년이 넘은 꿀을 발견했는데, 놀랍게도 그 꿀은 여전히 먹을 수 있는 상태였다.</p>
<p>꿀이 이렇게 오래 <span class="cn-word" data-pos="verb" data-tr="saqlanadigan">보존되는</span> <span class="cn-word" data-tr="sir, siri">비결</span>은 무엇일까? 꿀은 <span class="cn-word" data-tr="namlik, suv miqdori">수분</span>이 매우 <span class="cn-word" data-pos="adj" data-tr="kam, oz">적고</span> <span class="cn-word" data-tr="shakar miqdori">당분</span>이 많아서 <span class="cn-word" data-tr="mikrob, bakteriya">세균</span>이 <span class="cn-word" data-pos="verb" data-tr="omon qolishi">살아남기</span> 어려운 <span class="cn-word" data-tr="muhit, sharoit">환경</span>이다. 게다가 <span class="cn-word" data-tr="asalari">꿀벌</span>이 꿀을 만드는 과정에서 세균을 죽이는 물질이 <span class="cn-word" data-pos="adv" data-tr="tabiiy ravishda">자연스럽게</span> 생긴다. 그래서 <span class="cn-word" data-tr="qopqoq">뚜껑</span>만 잘 <span class="cn-word" data-pos="verb" data-tr="yopib">닫아</span> <strong>두면</strong>, 꿀은 사실상 <span class="cn-word" data-pos="adv" data-tr="abadiy, mangu">영원히</span> 변하지 않는다.</p>''',
        "grammar": [
            {
                "pattern":  "-지 않아도",
                "meaning":  "...maslik sharti bilan ham, ...qilmasa ham (yon berish).",
                "examples": ["냉장고에 넣지 않아도 꿀은 상하지 않는다.", "지금 서두르지 않아도 늦지 않아요."],
            },
            {
                "pattern":  "-아/어 두다",
                "meaning":  "Ishni bajarib, keyingi foydalanish uchun shu holatda saqlab qoʻymoq: ...ib qoʻymoq.",
                "examples": ["뚜껑만 잘 닫아 두면 오래 보관할 수 있다.", "필요한 것을 미리 사 두었어요."],
            },
        ],
        "questions": [
            {
                "text": "이집트 무덤에서 발견된 3천 년 된 꿀의 상태로 알맞은 것은 무엇입니까?",
                "choices": [
                    "완전히 썩어서 먹을 수 없었다.",
                    "여전히 먹을 수 있는 상태였다.",
                    "돌처럼 딱딱하게 굳어 있었다.",
                ],
                "answer": 1,
                "explanation": "Matnda 3 ming yillik asal hali ham yeyishga yaroqli holatda boʻlgani aytilgan.",
            },
            {
                "text": "꿀 속에서 세균이 살아남기 어려운 이유로 알맞은 것은 무엇입니까?",
                "choices": [
                    "수분이 많고 당분이 적기 때문에",
                    "수분이 적고 당분이 많으며 세균을 죽이는 물질이 있기 때문에",
                    "꿀이 항상 차갑게 보관되기 때문에",
                ],
                "answer": 1,
                "explanation": "Asalda namlik kam, shakar koʻp, hamda asalari qoʻshgan mikrobni oʻldiruvchi modda bor — shu sabab bakteriya omon qololmaydi.",
            },
            {
                "text": "이 글의 내용과 일치하지 않는 것을 고르십시오.",
                "choices": [
                    "꿀은 뚜껑만 잘 닫아 두면 아주 오래 보관할 수 있다.",
                    "꿀을 오래 보관하려면 반드시 냉장고에 넣어야 한다.",
                    "꿀벌이 꿀을 만들 때 세균을 죽이는 물질이 생긴다.",
                ],
                "answer": 1,
                "explanation": "Matn boshida asal muzlatgichga solinmasa ham buzilmasligi aytilgan, shuning uchun ‘albatta muzlatgichga solish kerak’ degan variant matnga zid.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "세상에서 가장 깊은 곳",
        "summary": "Marian botigʻi shunchalik chuqurki, Everestni unga solsangiz choʻqqisi hali ham 2 km suv ostida qoladi.",
        "order":   10,
        "body": '''<p>지구에서 가장 깊은 곳은 어디일까? 바로 태평양에 있는 ‘<span class="cn-word" data-tr="Marian botigʻi">마리아나 해구</span>’로, 그 깊이가 <span class="cn-word" data-pos="adv" data-tr="naq, hatto">무려</span> 11킬로미터에 <strong><span class="cn-word" data-pos="verb" data-tr="yetadi">이른다</span></strong>. 세계에서 가장 높은 산인 <span class="cn-word" data-tr="Everest togʻi">에베레스트</span>산을 이곳에 <span class="cn-word" data-pos="adv" data-tr="butunlayicha">통째로</span> 넣어도, 산 <span class="cn-word" data-tr="choʻqqi, tepa">꼭대기</span>가 여전히 물속 2킬로미터 아래에 <span class="cn-word" data-pos="verb" data-tr="choʻkib qoladigan, botadigan">잠길</span> 정도이다.</p>
<p>이 깊은 <span class="cn-word" data-tr="dengiz tubi">바닷속</span>은 햇빛 한 줄기 들지 않는 <span class="cn-word" data-tr="qop-qora">칠흑</span> 같은 <span class="cn-word" data-tr="zulmat, qorongʻilik">어둠</span>의 세계다. <span class="cn-word" data-pos="adv" data-tr="bundan tashqari">게다가</span> <span class="cn-word" data-tr="suv bosimi">수압</span>은 <span class="cn-word" data-tr="yer yuzasi">지상</span>의 약 천 배에 <span class="cn-word" data-pos="verb" data-tr="yetadi">달해</span>, 사람이 <span class="cn-word" data-tr="yalangʻoch tan">맨몸</span>으로는 순식간에 <span class="cn-word" data-pos="verb" data-tr="ezilib ketadigan">짓눌릴</span> <strong>만큼</strong> <span class="cn-word" data-pos="adj" data-tr="kuchli, qudratli">강력하다</span>. 놀랍게도 이런 <span class="cn-word" data-tr="oʻta ogʻir, ekstremal">극한</span>의 환경에서도 살아가는 생명체가 있다. 재미있게도, 이 깊은 바다 <span class="cn-word" data-tr="tub, ost">밑바닥</span>에 <span class="cn-word" data-pos="verb" data-tr="borib kelgan">다녀온</span> 사람보다 달에 다녀온 사람이 더 많다고 한다.</p>''',
        "grammar": [
            {
                "pattern":  "-에 이르다 / 달하다",
                "meaning":  "Miqdor yoki darajaga yetish: ...ga yetadi, ...ni tashkil qiladi (rasmiy/yozma).",
                "examples": ["깊이가 11킬로미터에 이른다.", "수압이 지상의 천 배에 달한다."],
            },
            {
                "pattern":  "-(으)ㄹ 만큼",
                "meaning":  "Daraja/miqyos: shu darajada ...ki, ...gulik (natijaning kuchini bildiradi).",
                "examples": ["사람이 순식간에 짓눌릴 만큼 압력이 강하다.", "말이 안 나올 만큼 놀랐어요."],
            },
        ],
        "questions": [
            {
                "text": "마리아나 해구의 깊이에 대한 설명으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "에베레스트산을 넣어도 꼭대기가 물에 잠길 만큼 깊다.",
                    "에베레스트산보다 훨씬 얕다.",
                    "깊이가 정확히 2킬로미터이다.",
                ],
                "answer": 0,
                "explanation": "Matnda Everestni botiqqa solsa ham, choʻqqisi hali 2 km suv ostida qolishi aytilgan — demak u juda chuqur.",
            },
            {
                "text": "마리아나 해구 바닥의 환경으로 알맞은 것은 무엇입니까?",
                "choices": [
                    "햇빛이 밝게 들고 물이 따뜻하다.",
                    "빛이 들지 않고 수압이 지상의 약 천 배에 달한다.",
                    "생명체가 전혀 살 수 없는 텅 빈 곳이다.",
                ],
                "answer": 1,
                "explanation": "Botiq tubi zim-ziyo, suv bosimi yer yuzasidan taxminan ming baravar kuchli. Shunga qaramay u yerda hayot bor.",
            },
            {
                "text": "이 글의 마지막에서 말하고자 하는 것으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "바다 밑바닥은 달보다 탐사하기가 오히려 더 어렵다.",
                    "누구나 쉽게 바다 밑바닥에 갈 수 있다.",
                    "달에 가는 것이 바다보다 훨씬 어렵다.",
                ],
                "answer": 0,
                "explanation": "Dengiz tubiga borgan odam Oyga borganlardan kam — bu chuqur dengizni tekshirish nechogʻlik qiyinligini koʻrsatadi.",
            },
        ],
    },
]
