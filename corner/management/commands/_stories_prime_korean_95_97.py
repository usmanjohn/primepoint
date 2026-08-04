# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-95 … PK-97 (답시고, 기 짝이 없다, 로 인해).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 / 반말 da gaplashadi.
Mavzu — 인생 이야기 va 정보문 navbatma-navbat:
  95 — 인생 이야기: akaning “tuzatib bergan” velosipedi — kinoya
       bilan boshlanib, minnatdorchilik bilan tugaydigan hikoya
  96 — 정보문: radiy moda boʻlgan davr — bugungi kundan qaralganda
       “xavfliligining tengi yoʻq”
  97 — 인생 이야기: soʻnggi bitiruvchi — aholi kamayishi tufayli
       yopilgan qishloq maktabi

Kumulyativ qoida: PK-97 gacha oʻrganilgan hamma narsa ochiq.
PK-95 matnida 기 짝이 없다 (96) va 로 인해 (97) YOʻQ.
PK-96 matnida 로 인해 (97) yoʻq — sabab 때문에 bilan berilgan.
거늘 · 기로서니 (98), 사자성어 (99) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다,
(느)ㄴ다면, 다는 것, 라는, 처럼 — oʻrganilmagan, ishlatilmadi.
던 (PK-90 da ochilgan) endi erkin ishlatiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_95_97.py --author=prime
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
    # PK-95 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "형이 고쳐 준 자전거",
        "summary": (
            "PK-95 matni. Akam velosipedni tuzataman deb battar buzib "
            "qoʻydi. Oʻn yildan keyin men oʻsha ehtiyot qismlarning "
            "narxini bilib qoldim. Hayot hikoyasi, 한다체 da."
        ),
        "order":   95,
        "grammar": [
            {
                "pattern":  "-(느)ㄴ답시고 — …yaman deb (goʻyo)",
                "meaning":  "Birovning bahonasini <b>ishonmasdan</b> "
                            "keltirish. Matnda u ataylab hikoyaning "
                            "<b>boshida</b> turadi — chunki oʻn "
                            "yillik bola aynan shunday oʻylagan edi.",
                "examples": ["형은 자전거를 고쳐 준답시고 더 망가뜨렸다.",
                             "도와준답시고 옆에 앉아 있었다."],
            },
            {
                "pattern":  "(이)랍시고 — ot bilan",
                "meaning":  "Ot bilan ulagich <b>(이)라</b>: "
                            "선물<b>이랍시고</b> (받침 bor), "
                            "요리<b>랍시고</b> (받침 yoʻq).",
                "examples": ["선물이랍시고 낡은 자전거를 주었다."],
            },
            {
                "pattern":  "Kinoya qayerda tugaydi",
                "meaning":  "Hikoyaning oxirgi qismida 답시고 "
                            "<b>boshqa koʻrinmaydi</b>. Bu — ataylab: "
                            "qahramon endi akasining sababiga "
                            "ishonadi, demak kinoya qolipi ham "
                            "yoʻqoladi. Grammatika hikoyaning "
                            "ichida ishlaydi.",
                "examples": ["형은 그 겨울 내내 용돈을 쓰지 않았다."],
            },
        ],
        "body": '''<p>열 살 <span class="cn-word" data-tr="tugʻilgan kun">생일</span>에 나는 자전거를 받았다. 새것이 아니었다. 형이 삼 년 동안 타던 것이었다.</p>

<p>형은 그것을 <span class="cn-word" data-pos="verb" data-tr="sovgʻa emish deb">선물이랍시고</span> 주었다. 나는 기분이 좋지 않았다.</p>

<p>일주일 뒤에 <span class="cn-word" data-tr="zanjir">체인</span>이 빠졌다. 형이 왔다.</p>

<p>“내가 고쳐 줄게.”</p>

<p>형은 자전거를 <span class="cn-word" data-pos="verb" data-tr="tuzataman deb (goʻyo)">고쳐 준답시고</span> 두 시간 동안 <span class="cn-word" data-pos="verb" data-tr="ajratdi">분해했다</span>. 그리고 다시 <span class="cn-word" data-pos="verb" data-tr="yigʻdi">조립했다</span>. 결과는 더 나빴다. 체인은 빠지지 않았지만 <span class="cn-word" data-tr="tormoz">브레이크</span>가 <span class="cn-word" data-pos="verb" data-tr="ishlamay qoldi">듣지 않았다</span>.</p>

<p>다음 날 형은 또 왔다. <span class="cn-word" data-pos="verb" data-tr="yordam beraman deb">도와준답시고</span> 옆에 앉아 있었다. 나는 화가 났다.</p>

<p>“형, 그냥 두세요.”</p>

<p>형은 아무 말도 하지 않고 나갔다.</p>

<p>그 뒤로 자전거는 <span class="cn-word" data-pos="adv" data-tr="birdaniga">갑자기</span> 괜찮아졌다. 브레이크도 <span class="cn-word" data-pos="verb" data-tr="ishladi">들었고</span>, <span class="cn-word" data-tr="oʻrindiq">안장</span>도 새것이었다. 나는 <span class="cn-word" data-pos="adv" data-tr="oddiygina">그냥</span> 아버지가 고쳤으려니 했다.</p>

<p>나는 그 자전거를 사 년 탔다.</p>

<p>스무 살에 나는 <span class="cn-word" data-tr="velosiped doʻkoni">자전거 가게</span>에서 <span class="cn-word" data-tr="yarim kunlik ish">아르바이트</span>를 했다. 어느 날 손님이 <span class="cn-word" data-tr="tormoz qismi">브레이크 부품</span>과 안장을 샀다. 나는 <span class="cn-word" data-tr="narx">값</span>을 보고 손이 멈췄다.</p>

<p>그 두 개의 값은 1998년에 중학생 한 달 <span class="cn-word" data-tr="choʻntak puli">용돈</span>보다 많았다.</p>

<p>집에 가서 어머니에게 물었다. 어머니는 웃었다.</p>

<p>“형이 그 겨울 내내 <span class="cn-word" data-tr="tushlik puli">점심값</span>을 안 썼어. 나는 살을 <span class="cn-word" data-pos="verb" data-tr="ozmoqchi boʻlib">빼려고</span> 그런다고 생각했지.”</p>

<p>형은 지금 <span class="cn-word" data-tr="Busan">부산</span>에 산다. 우리는 일 년에 두 번쯤 만난다.</p>

<p>나는 아직 그 이야기를 형에게 꺼내지 않았다.</p>

<p>그러나 지금도 한 가지를 <span class="cn-word" data-pos="verb" data-tr="oʻylayman">생각한다</span>. 그때 나는 형이 <span class="cn-word" data-pos="verb" data-tr="aralashadi">참견한다</span>고 생각했다. 형은 <span class="cn-word" data-pos="verb" data-tr="qaytarayotgan edi">고치고 있었다</span>.</p>''',
        "questions": [
            {
                "text": "Aka velosipedni birinchi marta “tuzatgach” nima "
                        "boʻldi?",
                "choices": [
                    "Velosiped yangidek boʻldi",
                    "Zanjir tushmay qoʻydi, lekin tormoz ishlamay qoldi",
                    "Velosiped butunlay singan",
                    "Hech narsa oʻzgarmadi",
                ],
                "answer": 1,
                "explanation": "“체인은 빠지지 않았지만 브레이크가 듣지 "
                               "않았다.” Shuning uchun hikoyachi "
                               "<b>고쳐 준답시고</b> deb kinoya bilan "
                               "eslaydi.",
            },
            {
                "text": "Velosiped aslida qanday tuzalgan edi?",
                "choices": [
                    "Ota tuzatgan",
                    "Aka butun qish tushlik pulini yigʻib, ehtiyot qism "
                    "sotib olgan",
                    "Onasi doʻkonga bergan",
                    "Qoʻshni tuzatgan",
                ],
                "answer": 1,
                "explanation": "“형이 그 겨울 내내 점심값을 안 썼어.” "
                               "Bola esa oʻshanda “아버지가 고쳤으려니 "
                               "했다” — PK-94 dagi tekshirilmagan taxmin.",
            },
            {
                "text": "Hikoyaning oxirgi ikki jumlasi nimani "
                        "oʻzgartiradi?",
                "choices": [
                    "Hech narsani — bu shunchaki xotira",
                    "Bir xil harakatning ikki xil oʻqilishini: oʻshanda "
                    "“aralashish”, endi “tuzatish”",
                    "Akaning yomon odam ekanini",
                    "Velosipedning qimmat ekanini",
                ],
                "answer": 1,
                "explanation": "“그때 나는 형이 참견한다고 생각했다. 형은 "
                               "고치고 있었다.” Shuning uchun matnning "
                               "oxirida <b>답시고</b> boshqa koʻrinmaydi "
                               "— kinoya yoʻqolgan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-96 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "빛을 마시던 시대",
        "summary": (
            "PK-96 matni. Yuz yil oldin radiy sogʻliq uchun foydali deb "
            "hisoblangan: suvda, tish pastasida, upa-elikda. Bugun "
            "qaralsa — xavfliligining tengi yoʻq. Tushuntiruvchi matn, "
            "한다체 da."
        ),
        "order":   96,
        "grammar": [
            {
                "pattern":  "기 짝이 없다 — …ning tengi yoʻq",
                "meaning":  "Sifatni eng yuqori chegaraga koʻtaradi. "
                            "Yozma til. Matnda u har safar "
                            "<b>bugungi kundan</b> berilgan baho "
                            "sifatida keladi — oʻsha davr odamlari "
                            "hech narsa bilmagan.",
                "examples": ["지금 보면 위험하기 짝이 없다.",
                             "안타깝기 짝이 없는 일이었다."],
            },
            {
                "pattern":  "짝이 없는 + 명사",
                "meaning":  "Otni aniqlaganda 없다 → <b>없는</b> "
                            "(PK-45): 안타깝기 짝이 <b>없는</b> 일. "
                            "Bu shakl gazeta va maqola tilida juda "
                            "koʻp.",
                "examples": ["어리석기 짝이 없는 광고였다."],
            },
            {
                "pattern":  "Nega faqat sifat",
                "meaning":  "Qolip harakatni emas, <b>holatni "
                            "baholaydi</b>. Matndagi hamma "
                            "misollarda oldida sifat turadi: "
                            "위험하다, 안타깝다, 어리석다.",
                "examples": ["그 광고는 어리석기 짝이 없다."],
            },
        ],
        "body": '''<p>1898년에 <span class="cn-word" data-tr="Kyuri er-xotin">퀴리 부부</span>가 <span class="cn-word" data-tr="radiy">라듐</span>을 발견했다. 이 <span class="cn-word" data-tr="element, modda">원소</span>는 어두운 곳에서 <span class="cn-word" data-pos="adj" data-tr="yashil rangda porlardi">푸르게 빛났다</span>.</p>

<p>사람들은 <span class="cn-word" data-pos="verb" data-tr="hayratda qoldi">놀랐다</span>. 그리고 이상한 <span class="cn-word" data-tr="xulosa">결론</span>을 내렸다. 빛나는 것은 <span class="cn-word" data-pos="adj" data-tr="kuchli">힘이 세다</span>. 힘이 센 것은 몸에 좋다.</p>

<p>그래서 라듐은 <span class="cn-word" data-tr="moda">유행</span>이 되었다.</p>

<p>가게에서 라듐 <span class="cn-word" data-tr="tish pastasi">치약</span>을 팔았다. 라듐 <span class="cn-word" data-tr="upa-elik, kosmetika">화장품</span>도 있었다. <span class="cn-word" data-tr="Amerika">미국</span>에서는 라듐을 넣은 물을 <span class="cn-word" data-tr="shisha">병</span>에 담아 팔았다. 한 병에 지금 돈으로 이만 원쯤이었다. <span class="cn-word" data-tr="boy odam">부자</span>들이 매일 그 물을 마셨다.</p>

<p>지금 보면 <span class="cn-word" data-pos="adj" data-tr="xavfliligining tengi yoʻq">위험하기 짝이 없다</span>.</p>

<p>가장 <span class="cn-word" data-pos="adj" data-tr="achinarli">안타까운</span> 이야기는 <span class="cn-word" data-tr="soat zavodi">시계 공장</span>에서 나왔다. 그 시대 시계는 밤에도 보여야 했다. 그래서 <span class="cn-word" data-tr="raqamlar">숫자</span>에 라듐 <span class="cn-word" data-tr="boʻyoq">페인트</span>를 칠했다.</p>

<p>이 일을 하는 사람들은 대부분 <span class="cn-word" data-tr="yosh ayollar">젊은 여성</span>이었다. <span class="cn-word" data-tr="moʻyqalam">붓</span>을 <span class="cn-word" data-pos="adj" data-tr="ingichka">가늘게</span> <span class="cn-word" data-pos="verb" data-tr="qilmoqchi boʻlib">만들려고</span> 그들은 붓 <span class="cn-word" data-tr="uchi">끝</span>을 <span class="cn-word" data-tr="til">혀</span>로 <span class="cn-word" data-pos="verb" data-tr="oʻtkirlashtirardi">다듬었다</span>. 하루에 수백 번.</p>

<p><span class="cn-word" data-tr="kompaniya">회사</span>는 <span class="cn-word" data-pos="adj" data-tr="xavfsiz">안전하다</span>고 말했다. 몇 년 뒤에 여성들이 <span class="cn-word" data-pos="verb" data-tr="kasal boʻla boshladi">아프기 시작했다</span>.</p>

<p>그들 중 다섯 명이 회사를 <span class="cn-word" data-pos="verb" data-tr="sudga berdi">고소했다</span>. <span class="cn-word" data-tr="sud">재판</span>은 길었다. 그러나 그 재판 <span class="cn-word" data-tr="tufayli">때문에</span> <span class="cn-word" data-tr="mehnat xavfsizligi qonuni">노동 안전법</span>이 바뀌었다. 오늘날 <span class="cn-word" data-tr="butun dunyo">전 세계</span> 공장의 <span class="cn-word" data-tr="qoida">규칙</span>은 그 다섯 사람에게서 시작되었다.</p>

<p><span class="cn-word" data-pos="adj" data-tr="achinarliligining tengi yoʻq">안타깝기 짝이 없는</span> 일이었다. 그러나 그 일이 없었으면 지금의 규칙도 없었다.</p>

<p>이 이야기의 <span class="cn-word" data-tr="saboq">교훈</span>은 “옛날 사람들은 <span class="cn-word" data-pos="adj" data-tr="ahmoq edi">어리석었다</span>”가 아니다.</p>

<p>그들은 몰랐다. 우리도 모르는 것이 있다. 백 년 뒤의 사람들이 지금 우리의 어떤 <span class="cn-word" data-tr="odat">습관</span>을 보고 “<span class="cn-word" data-pos="adj" data-tr="ahmoqligining tengi yoʻq">어리석기 짝이 없다</span>”고 <span class="cn-word" data-pos="verb" data-tr="aytishi ham mumkin">말할지도 모른다</span>.</p>''',
        "questions": [
            {
                "text": "Nega odamlar radiyni sogʻliq uchun foydali deb "
                        "hisoblashdi?",
                "choices": [
                    "Shifokorlar tavsiya qilgani uchun",
                    "“Porlaydi → kuchli → tanaga foydali” degan xulosa "
                    "chiqarishgani uchun",
                    "Arzon boʻlgani uchun",
                    "Tajribalar buni koʻrsatgani uchun",
                ],
                "answer": 1,
                "explanation": "“빛나는 것은 힘이 세다. 힘이 센 것은 몸에 "
                               "좋다.” Matn buni xulosa emas, "
                               "<b>xato xulosa</b> sifatida beradi.",
            },
            {
                "text": "Soat zavodidagi ayollarning ishi nima uchun "
                        "xavfli edi?",
                "choices": [
                    "Zavod issiq edi",
                    "Moʻyqalam uchini ingichka qilish uchun uni til bilan "
                    "oʻtkirlashtirishardi — kuniga yuzlab marta",
                    "Boʻyoq nafas orqali kirardi",
                    "Ish soatlari uzun edi",
                ],
                "answer": 1,
                "explanation": "“붓 끝을 혀로 다듬었다. 하루에 수백 번.” "
                               "Kompaniya esa “안전하다”고 말했다.",
            },
            {
                "text": "Matnning oxirgi xulosasi nima?",
                "choices": [
                    "Oʻtmish odamlari ahmoq edi",
                    "Ular bilmagan edi — biz ham bilmaydigan narsalarimiz "
                    "bor, va bir kun bizga ham shunday qaraladi",
                    "Fanga ishonmaslik kerak",
                    "Radiy hozir ham xavfli",
                ],
                "answer": 1,
                "explanation": "“그들은 몰랐다. 우리도 모르는 것이 있다.” "
                               "Va oxirgi jumla shu fikrni bizga "
                               "qaytaradi: 백 년 뒤의 사람들이…",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-97 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "마지막 졸업생",
        "summary": (
            "PK-97 matni. Bir bolaga atalgan bitiruv marosimi. Aholi "
            "kamayishi tufayli yopilayotgan qishloq maktabining "
            "soʻnggi kuni. Hayot hikoyasi, 한다체 da."
        ),
        "order":   97,
        "grammar": [
            {
                "pattern":  "(으)로 인해 — … tufayli",
                "meaning":  "Rasmiy yozma sabab, <b>faqat ot</b> "
                            "bilan. Matnda u ataylab rasmiy "
                            "jumlalarda turadi — hujjat, qaror, "
                            "eʼlon tilida.",
                "examples": ["인구 감소로 인해 학교가 문을 닫는다.",
                             "학생 수 감소로 인한 통폐합이었다."],
            },
            {
                "pattern":  "(으)로 말미암아 — … oqibatida",
                "meaning":  "Undan ham ogʻirroq, adabiyroq. "
                            "Matnda bir marta — hikoyaning eng "
                            "muhim burilishida. Bu qolipni "
                            "koʻp ishlatmaslik kerak; uning kuchi "
                            "kamdan-kam kelishida.",
                "examples": ["그 결정으로 말미암아 한 마을의 백 년이 끝났다."],
            },
            {
                "pattern":  "(으)로 인한 + 명사",
                "meaning":  "Otni aniqlaganda <b>인한</b> boʻladi, "
                            "인해 emas. Gazeta va hujjat tilining "
                            "asosiy shakli.",
                "examples": ["학생 수 감소로 인한 통폐합"],
            },
        ],
        "body": '''<p>2019년 2월, <span class="cn-word" data-tr="Kanvondo (viloyat)">강원도</span>의 한 <span class="cn-word" data-tr="qishloq">시골</span> 초등학교에서 <span class="cn-word" data-tr="bitiruv marosimi">졸업식</span>이 열렸다. <span class="cn-word" data-tr="bitiruvchi">졸업생</span>은 한 명이었다.</p>

<p>이름은 <span class="cn-word" data-tr="Kim Uzin (ism)">김우진</span>. 열세 살이었다.</p>

<p>그 학교는 1922년에 <span class="cn-word" data-pos="verb" data-tr="ochilgan edi">문을 열었다</span>. 가장 학생이 많던 해에는 삼백 명이 넘었다. 마을에 <span class="cn-word" data-tr="konchilik">광산</span>이 있었고, 젊은 <span class="cn-word" data-tr="oila">가족</span>이 많았다.</p>

<p>광산은 1993년에 닫혔다. 그 뒤로 사람들이 도시로 갔다.</p>

<p><span class="cn-word" data-pos="verb" data-tr="aholi kamayishi tufayli">인구 감소로 인해</span> 학생 수는 계속 줄었다. 2015년에 다섯 명, 2017년에 세 명, 2018년에 한 명이 되었다.</p>

<p><span class="cn-word" data-tr="taʼlim boshqarmasi">교육청</span>은 2018년에 <span class="cn-word" data-pos="verb" data-tr="qaror qildi">결정을 내렸다</span>. <span class="cn-word" data-pos="verb" data-tr="oʻquvchilar soni kamayishi tufayli">학생 수 감소로 인한</span> <span class="cn-word" data-tr="qoʻshib yuborish, birlashtirish">통폐합</span>이었다. 우진이 졸업하면 학교는 문을 닫는다.</p>

<p>졸업식 날 <span class="cn-word" data-tr="sport zali">체육관</span>에 사람이 가득했다. 마을 사람 <span class="cn-word" data-tr="qariyb">거의</span> 전부가 왔다. 대부분 일흔 살이 넘은 사람들이었다.</p>

<p>그들 중 많은 사람이 그 학교를 졸업했다. 어떤 <span class="cn-word" data-tr="momo">할머니</span>는 1955년 졸업생이었다.</p>

<p>선생님은 두 분이었다. 한 분은 그해에 <span class="cn-word" data-pos="verb" data-tr="nafaqaga chiqadi">정년퇴직</span>했다.</p>

<p>우진이 <span class="cn-word" data-tr="diplom, guvohnoma">졸업장</span>을 받았다. <span class="cn-word" data-tr="qarsak">박수</span>가 오래 이어졌다.</p>

<p>그리고 <span class="cn-word" data-tr="maktab qoʻshigʻi">교가</span>를 불렀다. 백 명이 넘는 사람이 같이 불렀다. 대부분 <span class="cn-word" data-tr="oltmish yil">육십 년</span> 전에 배운 노래였다. 아무도 <span class="cn-word" data-tr="soʻz, matn">가사</span>를 잊지 않았다.</p>

<p>그 <span class="cn-word" data-pos="verb" data-tr="qaror oqibatida">결정으로 말미암아</span> 한 마을의 백 년이 끝났다.</p>

<p>우진은 지금 도시의 중학교에 다닌다. 학생이 사백 명이다.</p>

<p><span class="cn-word" data-tr="jurnalist">기자</span>가 졸업식 날 우진에게 물었다. “혼자 졸업해서 <span class="cn-word" data-pos="adj" data-tr="yolgʻizmisan">외롭지</span> 않아요?”</p>

<p>우진은 잠시 <span class="cn-word" data-pos="verb" data-tr="oʻyladi">생각했다</span>. 그리고 대답했다.</p>

<p>“<span class="cn-word" data-tr="sport zali">체육관</span>에 백 명 있었어요.”</p>''',
        "questions": [
            {
                "text": "Maktabdagi oʻquvchilar soni nega kamaydi?",
                "choices": [
                    "Yangi maktab qurilgani uchun",
                    "Kon 1993-yilda yopilgach odamlar shaharga koʻchgani "
                    "va aholi kamaygani tufayli",
                    "Oʻqituvchilar yetishmagani uchun",
                    "Bino eski boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "“광산은 1993년에 닫혔다. 그 뒤로 사람들이 "
                               "도시로 갔다.” Va shu sabab rasmiy tilda "
                               "beriladi: <b>인구 감소로 인해</b>.",
            },
            {
                "text": "Matnda 인해 va 인한 shakllari nima uchun boshqa-"
                        "boshqa?",
                "choices": [
                    "Ular bir xil, tasodifan farq qilgan",
                    "인해 kesimga bogʻlanadi, 인한 esa otni aniqlaydi "
                    "(학생 수 감소로 인한 통폐합)",
                    "인한 — oʻtgan zamon",
                    "인해 — ogʻzaki shakl",
                ],
                "answer": 1,
                "explanation": "“인구 감소로 <b>인해</b> 학생 수는 줄었다” "
                               "— kesim. “학생 수 감소로 <b>인한</b> "
                               "통폐합” — ot aniqlanmoqda.",
            },
            {
                "text": "Uzinning oxirgi javobi nimani anglatadi?",
                "choices": [
                    "U yolgʻizlikni sezmadi, chunki zalda yuz kishi — "
                    "oʻsha maktabning avvalgi bitiruvchilari — bor edi",
                    "U sinfdoshlarini sogʻinmadi",
                    "U sport zalini yaxshi koʻrardi",
                    "U savolni tushunmadi",
                ],
                "answer": 0,
                "explanation": "Jurnalist bitta bitiruvchi haqida "
                               "soʻradi. Uzin butun maktabni sanadi — "
                               "oltmish yil oldin oʻsha qoʻshiqni "
                               "yodlagan odamlarni ham.",
            },
        ],
    },
]
