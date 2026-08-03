# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-77 … PK-79 (다가/보면/보니, 았더라면, 다가는).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 da gaplashadi.
Mavzu — 정보문 va 인생 이야기 navbatma-navbat:
  77 — 인생 이야기: kuniga oʻn daqiqa rasm chizgan ayol
  78 — 정보문: hangul yaratilishi, “agar boʻlmaganida edi” savoli bilan
  79 — 인생 이야기: murabbiyning bir jumlasi va uni yigirma yildan keyin
       takrorlaydigan shogird

Kumulyativ qoida: PK-79 gacha oʻrganilgan hamma narsa ochiq.
PK-77 matnida 았/었더라면 (78) va 다가는 (79) YOʻQ.
PK-78 matnida 다가는 (79) yoʻq.
아/어 봤자 (80), (으)ㄹ지라도 (81), (으)ㄹ 정도로 (82), 에 불과하다 (83),
든지 (84), (으)나 마나 (85), (으)ㅁ으로써 (86) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, ㅂ시다 — oʻrganilmagan,
ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_77_79.py --author=prime
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
    # PK-77 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "매일 십 분",
        "summary": (
            "PK-77 matni. Sujin uch marta katta qaror qildi va uch marta "
            "tashlab qoʻydi. Toʻrtinchisida u juda kichik narsani "
            "tanladi — kuniga oʻn daqiqa."
        ),
        "order":   77,
        "grammar": [
            {
                "pattern":  "다가 / 았다가 — ish uzildi yoki orqaga qaytdi",
                "meaning":  "다가 — ish yarim yoʻlda toʻxtadi. 았/었다가 — "
                            "ish tugadi, keyin teskarisi boʻldi.",
                "examples": ["세 번 시작했다가 세 번 그만두었다.",
                             "그리다가 졸리면 그냥 잤다."],
            },
            {
                "pattern":  "다가 보니 — …yaverib, qarabsizki",
                "meaning":  "Davom ettirdim va oʻzim kutmagan natijani "
                            "kashf qildim. Ikkinchi gap hamisha oʻtgan "
                            "zamonda.",
                "examples": ["매일 십 분씩 그리다가 보니 실력이 정말 늘어 있었다."],
            },
            {
                "pattern":  "다가 보면 — …yaversang, bir kun",
                "meaning":  "Bir xil qolip, lekin kelajakka qaraydi — "
                            "dalda va maslahat ohangi. Shu matnda ustoz "
                            "shogirdlariga aynan shuni aytadi.",
                "examples": ["매일 조금씩 하다가 보면 늘어요."],
            },
        ],
        "body": '''<p>수진 씨는 그림을 잘 그리고 싶었다. 하지만 세 번 <span class="cn-word" data-pos="verb" data-tr="boshlab, keyin">시작했다가</span> 세 번 <span class="cn-word" data-pos="verb" data-tr="tashlab qoʻydi">그만두었다</span>.</p>

<p>처음에는 열여덟 살에 시작했다. 큰 종이와 비싼 <span class="cn-word" data-tr="rangli qalam">색연필</span>을 샀다. 하지만 두 달 후에 그만두었다. 두 번째는 대학교에서였다. <span class="cn-word" data-tr="tasviriy sanʼat toʻgaragi">미술 동아리</span>에 <span class="cn-word" data-pos="verb" data-tr="kirdi-yu, keyin">들어갔다가</span> 한 <span class="cn-word" data-tr="semestr">학기</span> <span class="cn-word" data-tr="ichida">만</span>에 나왔다. 세 번째는 회사에 다니면서 시작했다. 주말마다 세 시간씩 그렸다. <span class="cn-word" data-pos="adv" data-tr="shunday davom etayotib">그러다가</span> <span class="cn-word" data-tr="tungi ish">야근</span>이 많아졌고, 연필은 <span class="cn-word" data-tr="tortma">서랍</span> 안으로 들어갔다.</p>

<p>서른 살 생일에 수진 씨는 <span class="cn-word" data-pos="adj" data-tr="gʻalati">이상한</span> <span class="cn-word" data-tr="qaror">결심</span>을 했다. 하루에 십 분만 그리는 것이다. 십 분은 너무 짧았다. 그래서 <span class="cn-word" data-pos="verb" data-tr="tashlab qoʻyish ham">그만두기도</span> 어려웠다.</p>

<p>피곤한 날에도 십 분은 할 수 있었다. <span class="cn-word" data-pos="verb" data-tr="chizayotib">그리다가</span> <span class="cn-word" data-pos="adj" data-tr="uyqusi kelsa">졸리면</span> 그냥 잤다. 다음 날 또 십 분을 그렸다.</p>

<p>일 년이 지났다. 수진 씨는 <span class="cn-word" data-pos="adj" data-tr="alohida">특별한</span> 것을 <span class="cn-word" data-pos="verb" data-tr="sezmadi">느끼지 못했다</span>.</p>

<p>이 년이 지났다. 친구가 그림을 보고 <span class="cn-word" data-pos="verb" data-tr="hayron qoldi">놀랐다</span>. “이거 수진 씨가 그렸어요? 진짜예요?”</p>

<p>삼 년이 지났다. 회사 사람들이 <span class="cn-word" data-tr="tashrif qogʻozi">명함</span> 그림을 <span class="cn-word" data-pos="verb" data-tr="soʻray boshladi">부탁하기 시작했다</span>.</p>

<p>사 년이 지난 어느 날, 수진 씨는 옛날 그림들을 <span class="cn-word" data-pos="verb" data-tr="chiqarib koʻrdi">꺼내 보았다</span>. 그리고 처음으로 자기 그림을 오래 보았다. 매일 십 분씩 <span class="cn-word" data-pos="verb" data-tr="chizaverib, qarasa">그리다가 보니</span> <span class="cn-word" data-tr="mahorat">실력</span>이 정말 <span class="cn-word" data-pos="verb" data-tr="oʻsib qolgan edi">늘어 있었다</span>. 자기도 모르는 <span class="cn-word" data-tr="orada">사이</span>에.</p>

<p>지금 수진 씨는 작은 그림 <span class="cn-word" data-tr="sinf, kurs">교실</span>을 연다. 학생들이 자주 묻는다. “얼마나 해야 잘 그려요?”</p>

<p>수진 씨는 늘 같은 <span class="cn-word" data-tr="javob">대답</span>을 한다. “매일 조금씩 하다가 보면 늘어요. 저는 삼 년 동안 아무것도 못 느꼈어요. 그런데 사 년째에 알았어요.”</p>

<p>그리고 이렇게 <span class="cn-word" data-pos="verb" data-tr="qoʻshib qoʻyadi">덧붙인다</span>. “큰 결심은 세 번 다 <span class="cn-word" data-pos="verb" data-tr="muvaffaqiyatsiz tugadi">실패했어요</span>. 십 분은 사 년을 갔어요.”</p>''',
        "questions": [
            {
                "text": "Sujin uch marta nega tashlab qoʻygan edi?",
                "choices": [
                    "Chizishni yoqtirmagani uchun",
                    "Har safar katta qaror qilgani uchun — koʻp vaqt va "
                    "koʻp kuch talab qilardi",
                    "Ustozi yomon boʻlgani uchun",
                    "Pul yetmagani uchun",
                ],
                "answer": 1,
                "explanation": "Qimmat qalamlar, toʻgarak, har hafta uch "
                               "soat — hammasi katta. Oxirgi jumla shuni "
                               "aytadi: “큰 결심은 세 번 다 실패했어요. "
                               "십 분은 사 년을 갔어요.”",
            },
            {
                "text": "“그리다가 보니 실력이 늘어 있었다” — bu jumlaning "
                        "ohangi qanday?",
                "choices": [
                    "Ogohlantirish",
                    "Buyruq",
                    "Kashfiyot va hayrat — u oʻsganini oʻzi sezmagan",
                    "Afsuslanish",
                ],
                "answer": 2,
                "explanation": "다가 보니 — <b>oʻtmishdagi kashfiyot</b>. "
                               "Matn buni “자기도 모르는 사이에” (oʻzi bilmagan "
                               "holda) deb ochib beradi.",
            },
            {
                "text": "Sujin shogirdlariga nima deydi?",
                "choices": [
                    "“매일 조금씩 하다가 보면 늘어요” — oz-ozdan qilaversang "
                    "oʻsasan",
                    "Kuniga uch soat mashq qilish kerak",
                    "Iqtidor eng muhimi",
                    "Yaxshi qalam sotib olish kerak",
                ],
                "answer": 0,
                "explanation": "다가 <b>보면</b> — kelajakka qaragan dalda. "
                               "Oʻzi haqida gapirganda esa 다가 <b>보니</b> "
                               "ishlatgan edi — allaqachon boʻlgan natija.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-78 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "한글이 없었더라면",
        "summary": (
            "PK-78 matni. Hangul qanday va nima uchun yaratilgan — va "
            "agar yaratilmaganida edi, nima boʻlardi. Tushuntiruvchi "
            "matn, 한다체 da."
        ),
        "order":   78,
        "grammar": [
            {
                "pattern":  "았/었더라면 — boʻlmagan oʻtmish",
                "meaning":  "Boʻlmagan narsani tasavvur qilish. Koʻpincha "
                            "oldida 만약 turadi, ikkinchi gapda esa "
                            "았/었을 것이다.",
                "examples": ["만약 한글이 없었더라면 이 숫자는 완전히 달랐을 것이다.",
                             "세종대왕이 그때 포기했더라면 오늘의 한국어 교실도 "
                             "없었을 것이다."],
            },
            {
                "pattern":  "았/었을 것이다 — boʻlmagan natija",
                "meaning":  "았/었더라면 ning doimiy jufti. Bu natija ham "
                            "sodir boʻlmagan — u faqat tasavvurda mavjud.",
                "examples": ["백성들은 계속 글을 모르고 살았을 것이다.",
                             "편지도, 이야기도, 노래도 쓰지 못했을 것이다."],
            },
            {
                "pattern":  "Nega 정보문 da teskari faraz kerak",
                "meaning":  "Biror narsaning qadrini koʻrsatishning eng "
                            "kuchli yoʻli — uni olib tashlab koʻrsatish. "
                            "TOPIK 쓰기 da ham shu usul juda foydali.",
                "examples": ["만약 세종대왕이 한자를 그대로 두었더라면 한국의 "
                             "역사는 아주 달랐을 것이다."],
            },
        ],
        "body": '''<p>지금 한국의 <span class="cn-word" data-tr="savodsizlik darajasi">문맹률</span>은 일 <span class="cn-word" data-tr="foiz">퍼센트</span> 아래다. 세계에서 가장 낮은 숫자 <span class="cn-word" data-tr="orasidan biri">중 하나</span>다. 만약 한글이 <span class="cn-word" data-pos="verb" data-tr="boʻlmaganida edi">없었더라면</span> 이 숫자는 완전히 <span class="cn-word" data-pos="adj" data-tr="boshqacha boʻlardi">달랐을 것이다</span>.</p>

<p>십오 <span class="cn-word" data-tr="asr">세기</span>까지 한국 사람들은 <span class="cn-word" data-tr="xitoy iyeroglifi">한자</span>로 글을 썼다. 한자는 <span class="cn-word" data-tr="oʻn minglab">수만</span> 개다. 한자를 배우는 것은 십 년이 걸리는 일이었다. 그래서 글을 읽을 수 있는 사람은 아주 적었다. <span class="cn-word" data-tr="koʻpchilik">대부분</span>의 <span class="cn-word" data-tr="xalq, fuqarolar">백성</span>은 자기 이름도 쓰지 못했다.</p>

<p><span class="cn-word" data-tr="Sejong podshoh">세종대왕</span>은 이 문제를 오래 생각했다. 그리고 1443년에 새 <span class="cn-word" data-tr="harf">글자</span>를 만들었다. 이름은 “<span class="cn-word" data-tr="Xunmin Jongum">훈민정음</span>”, <span class="cn-word" data-pos="adv" data-tr="yaʼni">곧</span> “백성을 가르치는 <span class="cn-word" data-pos="adj" data-tr="toʻgʻri">바른</span> 소리”였다.</p>

<p>한글은 스물여덟 자로 시작했다. 지금은 스물넉 자다. <span class="cn-word" data-tr="undosh">자음</span>은 입과 <span class="cn-word" data-tr="til (aʼzo)">혀</span>의 <span class="cn-word" data-tr="shakl">모양</span>을 보고 만들었다. ㄱ은 혀가 <span class="cn-word" data-tr="tomoq">목구멍</span>을 <span class="cn-word" data-pos="verb" data-tr="toʻsayotgan">막는</span> 모양이다. ㅁ은 입의 모양이다. <span class="cn-word" data-tr="unli">모음</span>은 하늘, <span class="cn-word" data-tr="yer">땅</span>, 사람 세 가지로 만들었다.</p>

<p>만약 세종대왕이 한자를 <span class="cn-word" data-pos="adv" data-tr="oʻsha holicha">그대로</span> <span class="cn-word" data-pos="verb" data-tr="qoldirganida edi">두었더라면</span> 한국의 <span class="cn-word" data-tr="tarix">역사</span>는 아주 달랐을 것이다. 백성들은 계속 글을 모르고 살았을 것이다. 편지도, 이야기도, 노래도 쓰지 못했을 것이다.</p>

<p>물론 한글은 처음부터 <span class="cn-word" data-pos="verb" data-tr="olqishlanmadi">환영받지 못했다</span>. 많은 <span class="cn-word" data-tr="olimlar">학자</span>들이 <span class="cn-word" data-pos="verb" data-tr="qarshi chiqdi">반대했다</span>. “한자가 진짜 글이다”라고 말했다. 한글이 <span class="cn-word" data-pos="adv" data-tr="keng">널리</span> <span class="cn-word" data-pos="verb" data-tr="ishlatila boshlagani">쓰이기 시작한</span> 것은 십구 세기 <span class="cn-word" data-tr="oxiri">말</span>이다. 사백 년이 걸렸다.</p>

<p>그러나 세종대왕이 그때 <span class="cn-word" data-pos="verb" data-tr="voz kechganida edi">포기했더라면</span> 오늘의 한국어 교실도 없었을 것이다. 지금 세계 여러 나라에서 사람들이 한글을 배운다. 한 외국인 학생은 이렇게 말한다. “삼 일 만에 읽을 수 있었어요. 다른 글자였으면 못 했을 거예요.”</p>

<p>좋은 <span class="cn-word" data-tr="asbob, vosita">도구</span>는 <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> 오래 <span class="cn-word" data-pos="verb" data-tr="qoladi">남는다</span>. 한글은 그런 도구다.</p>''',
        "questions": [
            {
                "text": "Hangul yaratilishidan oldin nima muammo edi?",
                "choices": [
                    "Qogʻoz yetishmasdi",
                    "Iyerogliflarni oʻrganish oʻn yil olardi, shuning uchun "
                    "xalqning koʻpchiligi oʻz ismini ham yoza olmasdi",
                    "Koreys tilida soʻz kam edi",
                    "Maktablar yoʻq edi",
                ],
                "answer": 1,
                "explanation": "“한자를 배우는 것은 십 년이 걸리는 일이었다… "
                               "대부분의 백성은 자기 이름도 쓰지 못했다.”",
            },
            {
                "text": "“만약 한글이 없었더라면 이 숫자는 완전히 달랐을 "
                        "것이다” — bu jumla nimani anglatadi?",
                "choices": [
                    "Hangul yoʻq, shuning uchun raqam boshqacha",
                    "Hangul kelajakda yoʻqolishi mumkin",
                    "Hangul bor — lekin agar boʻlmaganida edi, savodsizlik "
                    "darajasi butunlay boshqacha boʻlardi",
                    "Raqamlar notoʻgʻri hisoblangan",
                ],
                "answer": 2,
                "explanation": "았/었더라면 — <b>boʻlmagan</b> narsani "
                               "tasavvur qilish. Hangul bor, va aynan "
                               "shuning uchun savodsizlik bir foizdan "
                               "past.",
            },
            {
                "text": "Hangul yaratilgandan keyin darrov qabul "
                        "qilinganmi?",
                "choices": [
                    "Ha, hamma darhol qabul qildi",
                    "Yoʻq — koʻp olimlar qarshi chiqdi, keng tarqalishi "
                    "uchun toʻrt yuz yil kerak boʻldi",
                    "Yoʻq, u yuz yildan keyin unutildi",
                    "Matnda bu haqda aytilmagan",
                ],
                "answer": 1,
                "explanation": "“한글이 널리 쓰이기 시작한 것은 십구 세기 "
                               "말이다. 사백 년이 걸렸다.” Yaxshi narsaning "
                               "tan olinishi vaqt talab qiladi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-79 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "코치의 마지막 말",
        "summary": (
            "PK-79 matni. Murabbiy Minsuga bir jumla aytdi. Minsu "
            "kulib qoʻydi. Yigirma yildan keyin oʻsha jumlani u "
            "oʻzi takrorlaydi."
        ),
        "order":   79,
        "grammar": [
            {
                "pattern":  "다가는 — shunday qilaversang, …",
                "meaning":  "Hozir davom etayotgan ishning yomon oxirini "
                            "aytish. Natija hamisha salbiy va hali "
                            "sodir boʻlmagan.",
                "examples": ["그렇게 연습을 빼먹다가는 스무 살에 끝나요.",
                             "이렇게 서두르다가는 다시 다칠 거예요."],
            },
            {
                "pattern":  "Nega 이렇게 / 그렇게 yonida turadi",
                "meaning":  "다가는 yangi ish haqida emas — u odam "
                            "<b>ayni shu paytda</b> qilayotgan ish "
                            "haqida. Shuning uchun koʻrsatuvchi soʻz "
                            "tabiiy ravishda kelib qoladi.",
                "examples": ["그렇게 빼먹다가는 스무 살에 끝나요."],
            },
            {
                "pattern":  "Bir jumlaning ikki marta yangrashi",
                "meaning":  "Matnda bitta 다가는 jumlasi ikki marta "
                            "aytiladi — birinchi marta yosh bolaga, "
                            "ikkinchi marta oʻsha bola tomonidan. "
                            "Ogohlantirishning butun mazmuni shu.",
                "examples": ["“그렇게 빼먹다가는 스무 살에 끝나요. 나는 그 말을 "
                             "안 믿었어요.”"],
            },
        ],
        "body": '''<p>민수는 열여섯 살에 <span class="cn-word" data-tr="futbol toʻgaragi">축구부</span>에서 가장 빠른 <span class="cn-word" data-tr="sportchi">선수</span>였다. 공을 잡으면 아무도 <span class="cn-word" data-pos="verb" data-tr="yetib ololmasdi">따라오지 못했다</span>. <span class="cn-word" data-tr="murabbiy">코치</span>는 민수를 <span class="cn-word" data-pos="verb" data-tr="qadrlardi">아꼈다</span>. 그러나 자주 <span class="cn-word" data-pos="verb" data-tr="jahli chiqardi">화도 냈다</span>.</p>

<p>민수는 <span class="cn-word" data-tr="mashgʻulot">연습</span>에 자주 늦었다. 어떤 날은 오지 않았다. 그래도 <span class="cn-word" data-tr="oʻyin, musobaqa">경기</span>에서는 잘했다. 그래서 민수는 연습이 필요 없다고 생각했다.</p>

<p>코치는 여러 번 말했다. “그렇게 연습을 <span class="cn-word" data-pos="verb" data-tr="qoldiraversang">빼먹다가는</span> 스무 살에 끝나요.”</p>

<p>민수는 웃었다. 그 말을 믿지 않았다.</p>

<p>열여덟 살에 민수는 <span class="cn-word" data-tr="tizza">무릎</span>을 <span class="cn-word" data-pos="verb" data-tr="jarohatladi">다쳤다</span>. 큰 <span class="cn-word" data-tr="jarohat">부상</span>은 아니었다. 의사는 두 달 <span class="cn-word" data-pos="verb" data-tr="dam oling dedi">쉬라고 했다</span>. 하지만 민수는 삼 주 만에 다시 뛰었다. 코치가 <span class="cn-word" data-pos="verb" data-tr="toʻxtatdi">말렸다</span>. “이렇게 <span class="cn-word" data-pos="verb" data-tr="shoshaversang">서두르다가는</span> 다시 다칠 거예요.”</p>

<p>민수는 또 웃었다.</p>

<p>이 년 후, 민수는 스물한 살이었다. 무릎은 다시 다쳤고, 세 번째였다. 의사는 이번에는 <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> 말했다. “<span class="cn-word" data-tr="professional">프로</span> 선수는 어려워요.”</p>

<p>민수는 그날 코치의 말을 <span class="cn-word" data-pos="verb" data-tr="esladi">기억했다</span>.</p>

<p>몇 년이 지났다. 지금 민수는 중학교에서 아이들을 가르친다. <span class="cn-word" data-tr="mashq maydoni">연습장</span>에서 늦게 오는 아이를 보면 민수는 조용히 부른다. 그리고 자기 무릎을 <span class="cn-word" data-pos="verb" data-tr="koʻrsatib">가리키면서</span> 말한다.</p>

<p>“그렇게 빼먹다가는 스무 살에 끝나요. 나는 그 말을 안 믿었어요. 여러분은 믿어도 돼요.”</p>

<p>아이들은 웃는다. 민수도 웃는다. 하지만 민수는 그 <span class="cn-word" data-tr="kulgi">웃음</span>의 <span class="cn-word" data-tr="maʼno">의미</span>를 안다. 자기도 열여섯 살에 <span class="cn-word" data-pos="adv" data-tr="xuddi shunday">똑같이</span> 웃었다.</p>

<p>좋은 <span class="cn-word" data-tr="nasihat">충고</span>는 대부분 늦게 <span class="cn-word" data-pos="verb" data-tr="tushuniladi">이해된다</span>. 그래서 코치들은 같은 말을 <span class="cn-word" data-pos="adv" data-tr="doim">계속</span> 한다.</p>''',
        "questions": [
            {
                "text": "Murabbiy Minsuni nimadan ogohlantirgan edi?",
                "choices": [
                    "Koʻp ovqat yeyishdan",
                    "Mashgʻulotni qoldiraversa, yigirma yoshda karyerasi "
                    "tugashidan",
                    "Boshqa jamoaga oʻtishdan",
                    "Kech uxlashdan",
                ],
                "answer": 1,
                "explanation": "“그렇게 연습을 <b>빼먹다가는</b> 스무 살에 "
                               "끝나요.” 다가는 — hozir davom etayotgan "
                               "ishning yomon oxirini aytadi.",
            },
            {
                "text": "Nega bu jumlalarda 그렇게 va 이렇게 turibdi?",
                "choices": [
                    "Chunki 다가는 odam ayni shu paytda qilayotgan ish "
                    "haqida — “ana shunday davom etsang”",
                    "Chunki bu hurmat shakli",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki ikkita ega bor",
                ],
                "answer": 0,
                "explanation": "다가는 yangi ish haqida emas. Shuning uchun "
                               "koʻrsatuvchi soʻz deyarli har doim yonida "
                               "boʻladi.",
            },
            {
                "text": "Hikoyaning oxirgi fikri nima?",
                "choices": [
                    "Sportchi boʻlish qiyin",
                    "Murabbiylarni tinglash shart emas",
                    "Yaxshi nasihat koʻpincha kech tushuniladi — shuning "
                    "uchun murabbiylar bir gapni takrorlayveradi",
                    "Jarohat olgan odam qaytib oʻynay olmaydi",
                ],
                "answer": 2,
                "explanation": "“좋은 충고는 대부분 늦게 이해된다. 그래서 "
                               "코치들은 같은 말을 계속 한다.” Minsu endi "
                               "oʻsha jumlani oʻzi aytadi.",
            },
        ],
    },
]
