# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-92 … PK-94 (다면서요, 다니, (으)려니 하다).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 / 반말 da gaplashadi.
Mavzu — 정보문 va 인생 이야기 navbatma-navbat:
  92 — 정보문: oʻn odamdan oʻtgan gap — mish-mishning buzilishi
       (Allport-Postman uslubidagi tajriba)
  93 — 인생 이야기: onaning daftari — qirq toʻqqiz yoshida harf oʻrgangan ayol
  94 — 정보문: “그러려니 하는 힘” — sharh berishni toʻxtatish qanchalik
       foydali ekani

Kumulyativ qoida: PK-94 gacha oʻrganilgan hamma narsa ochiq.
PK-92 matnida 다니 (93) va 려니 하다 (94) YOʻQ.
PK-93 matnida 려니 하다 (94) yoʻq.
(이)랍시고 (95), 기 짝이 없다 (96), (으)로 인해 · (으)로 말미암아 (97),
거늘 · 기로서니 (98), 사자성어 (99) — hech qaysisida yoʻq.
⚠️ PK-97 ni buzmaslik uchun sabab hamma joyda **때문에** bilan
berilgan — 인해 ishlatilmadi, garchi 정보문 uchun u juda tabiiy
boʻlsa ham.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다,
(느)ㄴ다면, 다는 것, 라는, 처럼 — oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_92_94.py --author=prime
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
    # PK-92 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "열 사람을 지나면",
        "summary": (
            "PK-92 matni. Gap bir odamdan ikkinchisiga oʻtganda nima "
            "boʻladi? 1947-yilgi tajriba, mish-mishning uchta qonuni va "
            "zanjirni uzadigan bitta savol. Tushuntiruvchi matn, 한다체 da."
        ),
        "order":   92,
        "grammar": [
            {
                "pattern":  "-다면서요? — …emish-ku, rostmi?",
                "meaning":  "Eshitilgan gapni <b>egasidan</b> tekshirish. "
                            "Matnda u aynan mish-mishning oxirgi "
                            "bosqichi sifatida koʻrsatilgan — va matn "
                            "buni tuzoq deb ataydi.",
                "examples": ["“그 이야기 사실이라면서요?”"],
            },
            {
                "pattern":  "(이)라면서요 — ot bilan",
                "meaning":  "Ot bilan ulagich <b>(이)라</b> boʻladi: "
                            "사실 da 받침 bor → 사실<b>이라</b>면서요. "
                            "받침 yoʻq boʻlsa 가수<b>라</b>면서요.",
                "examples": ["그 이야기 사실이라면서요?"],
            },
            {
                "pattern":  "(으)ㄹ수록 va 셈이다 qaytadan",
                "meaning":  "Matn PK-65 va PK-91 ni ishga soladi: "
                            "소문은 지날<b>수록</b> 짧아진다 · 한 번 더 "
                            "옮긴 <b>셈이다</b>. Oʻqish matni faqat yangi "
                            "qolipni emas, eskilarini ham tirik "
                            "saqlaydi.",
                "examples": ["소문은 지날수록 짧아진다.",
                             "이미 그 소문을 한 번 더 옮긴 셈이다."],
            },
        ],
        "body": '''<p>말은 사람을 지나면서 <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">변한다</span>. 이것은 오래된 이야기가 아니라 <span class="cn-word" data-tr="tajriba">실험</span>으로 <span class="cn-word" data-pos="verb" data-tr="tasdiqlangan">확인된</span> 사실이다.</p>

<p>1947년에 두 <span class="cn-word" data-tr="psixolog">심리학자</span>가 간단한 실험을 했다. 한 사람에게 그림 하나를 보여 준다. 그리고 그 사람이 다음 사람에게 그림을 말로 <span class="cn-word" data-pos="verb" data-tr="tushuntiradi">설명한다</span>. 두 번째 사람은 세 번째 사람에게 설명한다. 이렇게 여섯 번을 지난다.</p>

<p>결과는 <span class="cn-word" data-pos="adj" data-tr="hayratlanarli edi">놀라웠다</span>. 마지막 사람이 들은 이야기는 처음 그림과 거의 <span class="cn-word" data-tr="aloqa">관계</span>가 없었다.</p>

<p>세 가지 <span class="cn-word" data-tr="oʻzgarish">변화</span>가 <span class="cn-word" data-pos="adv" data-tr="takror-takror">반복해서</span> 나타났다.</p>

<p>첫째, 이야기가 <span class="cn-word" data-pos="verb" data-tr="qisqaradi">짧아진다</span>. 사람들은 기억하기 쉬운 부분만 <span class="cn-word" data-pos="verb" data-tr="uzatadi">전한다</span>.</p>

<p>둘째, 남은 부분이 커진다. 작은 것 하나가 이야기의 <span class="cn-word" data-tr="markaz">중심</span>이 된다.</p>

<p>셋째, 사람들은 <span class="cn-word" data-tr="boʻsh joy">빈 곳</span>을 자기 생각으로 <span class="cn-word" data-pos="verb" data-tr="toʻldiradi">채운다</span>.</p>

<p>그래서 <span class="cn-word" data-tr="mish-mish, ovoza">소문</span>은 지날수록 짧아지고, <span class="cn-word" data-pos="adj" data-tr="kuchayadi">세지고</span>, 자기 이야기가 된다.</p>

<p>한국말에는 이 마지막 <span class="cn-word" data-tr="bosqich">단계</span>를 위한 문장이 있다.</p>

<p>“그 이야기 <span class="cn-word" data-pos="verb" data-tr="rost ekan-a?">사실이라면서요</span>?”</p>

<p>이 문장은 소문의 끝이 아니다. <span class="cn-word" data-tr="boshlanish">시작</span>이다. 물어본 사람은 답을 듣기 전에 이미 그 소문을 <span class="cn-word" data-pos="verb" data-tr="bir marta koʻchirgan hisob">한 번 더 옮긴 셈이다</span>.</p>

<p>그래서 <span class="cn-word" data-tr="tadqiqotchilar">연구자</span>들은 한 가지를 <span class="cn-word" data-pos="verb" data-tr="tavsiya qiladi">권한다</span>. 소문을 들으면 “누구한테 들었어요?”라고 물어봐야 한다. 이 질문 하나가 <span class="cn-word" data-tr="zanjir">사슬</span>을 <span class="cn-word" data-pos="verb" data-tr="uzadi">끊는다</span>.</p>

<p>한 연구자는 이렇게 말했다. “소문을 <span class="cn-word" data-pos="verb" data-tr="toʻxtatish">막는</span> 방법은 믿지 않는 것이 아니에요. <span class="cn-word" data-pos="verb" data-tr="koʻchirmaslik">옮기지 않는 것</span>이에요.”</p>''',
        "questions": [
            {
                "text": "1947-yilgi tajribada oxirgi odam eshitgan hikoya "
                        "qanday boʻldi?",
                "choices": [
                    "Birinchi rasmga deyarli aloqasi qolmadi",
                    "Aynan birinchi rasmga oʻxshadi",
                    "Uzunroq va aniqroq boʻldi",
                    "Hech kim hech narsa eslay olmadi",
                ],
                "answer": 0,
                "explanation": "“마지막 사람이 들은 이야기는 처음 그림과 거의 "
                               "관계가 없었다.” Oltita uzatish shu natijani "
                               "berdi.",
            },
            {
                "text": "Matnga koʻra, mish-mish oʻtgani sari qanday "
                        "oʻzgaradi?",
                "choices": [
                    "Uzayadi va aniqlashadi",
                    "Qisqaradi, qolgan qismi kattalashadi, boʻsh joylar "
                    "oʻz fikri bilan toʻldiriladi",
                    "Faqat qisqaradi",
                    "Hech qanday qonuniyat yoʻq",
                ],
                "answer": 1,
                "explanation": "Uchta qonun: 짧아진다 · 남은 부분이 커진다 · "
                               "빈 곳을 자기 생각으로 채운다. Shuning uchun "
                               "“소문은 지날수록 … 자기 이야기가 된다”.",
            },
            {
                "text": "Nega “그 이야기 사실이라면서요?” degan savol matnda "
                        "xavfli deb koʻrsatilgan?",
                "choices": [
                    "Chunki u qoʻpol savol",
                    "Chunki soʻragan odam javobni eshitmasdan turib, "
                    "mish-mishni yana bir marta koʻchirgan boʻladi",
                    "Chunki grammatikasi notoʻgʻri",
                    "Chunki unga hech kim javob bermaydi",
                ],
                "answer": 1,
                "explanation": "“물어본 사람은 답을 듣기 전에 이미 그 소문을 "
                               "한 번 더 <b>옮긴 셈이다</b>.” Matnning "
                               "maslahati boshqa: “누구한테 들었어요?” deb "
                               "soʻrash.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-93 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "어머니의 공책",
        "summary": (
            "PK-93 matni. Kasalxonaga ketayotgan onaning tortmasidan "
            "eski daftar chiqadi. Ichida — bir xil harflar, qator-qator. "
            "Va 1998-yilgi sana. Hayot hikoyasi, 한다체 da."
        ),
        "order":   93,
        "grammar": [
            {
                "pattern":  "-다니 — …emish-a! (hayrat)",
                "meaning":  "Kutilmagan narsani bilib qolgandagi "
                            "hayrat. Matnda u ikki marta keladi — va "
                            "ikkalasi ham hikoyachining <b>ichki "
                            "ovozi</b>, hech kimga aytilmagan gap.",
                "examples": ["어머니가 마흔아홉 살까지 글자를 몰랐다니.",
                             "한 사람이 마흔아홉 살에 다시 시작했다니."],
            },
            {
                "pattern":  "다니 gap oxirida ham turadi",
                "meaning":  "Ketidan 믿을 수 없다 kabi kesim "
                            "kelmasa ham boʻladi — gap shu yerda "
                            "tugaydi va butun hissiyot oʻsha "
                            "tugallanmaganlikda qoladi. 한다체 "
                            "hikoyada bu juda kuchli vosita.",
                "examples": ["어머니가 마흔아홉 살까지 글자를 몰랐다니."],
            },
            {
                "pattern":  "(으)니 — ochilish (PK-48)",
                "meaning":  "열어 <b>보니</b> — “ochib koʻrsam…”. "
                            "(으)니까 ning kashfiyot maʼnosi: bir ish "
                            "qilgach, yangi narsa maʼlum boʻladi.",
                "examples": ["열어 보니 첫 장부터 글자가 가득했다."],
            },
        ],
        "body": '''<p>지난봄에 어머니가 병원에 <span class="cn-word" data-pos="verb" data-tr="yotdi (kasalxonaga)">입원했다</span>. 나는 어머니 방에서 옷을 <span class="cn-word" data-pos="verb" data-tr="yigʻayotib">챙기다가</span> <span class="cn-word" data-tr="tortma">서랍</span>에서 <span class="cn-word" data-tr="daftar">공책</span> 한 권을 찾았다.</p>

<p><span class="cn-word" data-pos="adj" data-tr="eskirgan">낡은</span> 공책이었다. <span class="cn-word" data-tr="muqova">표지</span>에 아무것도 <span class="cn-word" data-pos="verb" data-tr="yozilmagan edi">쓰여 있지 않았다</span>.</p>

<p>열어 보니 첫 <span class="cn-word" data-tr="varaq, bet">장</span>부터 <span class="cn-word" data-tr="harf">글자</span>가 <span class="cn-word" data-pos="adj" data-tr="toʻla edi">가득했다</span>. 그런데 문장이 아니었다. 같은 글자만 <span class="cn-word" data-tr="har qatorda">줄마다</span> <span class="cn-word" data-pos="verb" data-tr="takrorlangan edi">반복되어 있었다</span>.</p>

<p>가 가 가 가 가<br>나 나 나 나 나</p>

<p>어린아이의 공책 같았다. 그런데 <span class="cn-word" data-tr="sana">날짜</span>가 있었다. 1998년 3월.</p>

<p>그때 어머니는 <span class="cn-word" data-tr="qirq toʻqqiz">마흔아홉</span> 살이었다.</p>

<p>나는 공책을 들고 <span class="cn-word" data-tr="kasalxona xonasi">병실</span>로 갔다. 어머니는 웃었다.</p>

<p>“그거 아직 있었어?”</p>

<p>어머니는 열 살에 학교를 <span class="cn-word" data-pos="verb" data-tr="tashladi">그만두었다</span>고 했다. 집이 <span class="cn-word" data-pos="adj" data-tr="kambagʻal edi">가난했고</span>, 동생이 넷이었다. 그리고 마흔아홉 살까지 글자를 몰랐다.</p>

<p><span class="cn-word" data-pos="verb" data-tr="bilmagan ekan-a">어머니가 마흔아홉 살까지 글자를 몰랐다니</span>.</p>

<p>나는 그때까지 몰랐다. 어머니는 우리 앞에서 한 번도 읽지 못한다고 말하지 않았다. 식당 <span class="cn-word" data-tr="menyu">메뉴판</span>을 보면 “<span class="cn-word" data-tr="koʻzoynak">안경</span>을 안 가져왔다”고 했다. 학교에서 온 종이는 아버지에게 주었다.</p>

<p>“어떻게 배웠어요?”</p>

<p>“밤에. 다 자면 <span class="cn-word" data-tr="oshxona">부엌</span>에서.”</p>

<p>어머니는 이 년 동안 매일 밤 한 시간씩 썼다. 이 년이면 <span class="cn-word" data-pos="verb" data-tr="yetti yuz soatdan oshgan hisob">칠백 시간이 넘는 셈이다</span>.</p>

<p>지금 어머니는 <span class="cn-word" data-tr="yetmish olti">일흔여섯</span> 살이다. 매일 아침 <span class="cn-word" data-tr="gazeta">신문</span>을 읽는다.</p>

<p>그 공책은 지금 내 책상 위에 있다. <span class="cn-word" data-pos="adv" data-tr="baʼzan">가끔</span> 첫 장을 연다.</p>

<p>가 가 가 가 가.</p>

<p><span class="cn-word" data-pos="verb" data-tr="qaytadan boshlabdi-ya">한 사람이 마흔아홉 살에 다시 시작했다니</span>. 나는 아직도 그 앞에서 할 말이 없다.</p>''',
        "questions": [
            {
                "text": "Daftarda nima yozilgan edi?",
                "choices": [
                    "Kundalik yozuvlari",
                    "Xatlar",
                    "Bir xil harflar, qator-qator takrorlangan",
                    "Retseptlar",
                ],
                "answer": 2,
                "explanation": "“같은 글자만 줄마다 반복되어 있었다.” "
                               "Oʻgʻli avval buni bolaning daftari deb "
                               "oʻyladi — sana esa 1998-yilni koʻrsatardi.",
            },
            {
                "text": "Ona oʻqishni bilmasligini qanday yashirgan?",
                "choices": [
                    "Hech qachon uydan chiqmagan",
                    "Menyuni koʻrganda “koʻzoynagimni olmabman” degan, "
                    "maktabdan kelgan qogʻozlarni otaga bergan",
                    "Bolalariga ochiq aytgan",
                    "Doim yordam soʻragan",
                ],
                "answer": 1,
                "explanation": "Ikkita kichik odat — butun bir umr davomida. "
                               "Shuning uchun oʻgʻlining hayrati shunchalik "
                               "kuchli: “글자를 몰랐다니.”",
            },
            {
                "text": "Matn nega 다니 bilan tugaydi?",
                "choices": [
                    "Chunki bu savol",
                    "Chunki hikoyachi hayratini oxirigacha aytib "
                    "boʻlolmaydi — gap tugamaydi, his qoladi",
                    "Chunki bu buyruq",
                    "Chunki bu koʻchirma gap",
                ],
                "answer": 1,
                "explanation": "다니 dan keyin 믿을 수 없다 kabi kesim "
                               "kelmaydi — va aynan shu tugallanmaganlik "
                               "hissiyotni koʻrsatadi. Keyingi jumla buni "
                               "ochiq aytadi: “할 말이 없다”.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-94 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "그러려니 하는 힘",
        "summary": (
            "PK-94 matni. Avtobus kechikdi, oldingi mashina kesib oʻtdi — "
            "stressni voqea emas, unga qoʻshgan izohimiz yaratadi. Va "
            "bu izohni oʻchiradigan ikki soʻz. Tushuntiruvchi matn, "
            "한다체 da."
        ),
        "order":   94,
        "grammar": [
            {
                "pattern":  "(으)려니 하다 — …deb oʻylab qoʻyaqolmoq",
                "meaning":  "Ichda qilingan, tekshirilmagan taxmin. "
                            "Matnda u ataylab <b>hozirgi zamonda</b> "
                            "keladi (한다), chunki bu yerda u xotira "
                            "emas — <b>tavsiya etilayotgan odat</b>.",
                "examples": ["급한 일이 있으려니 한다.",
                             "바꿀 수 없는 일이면 그러려니 한다."],
            },
            {
                "pattern":  "그러려니 하다",
                "meaning":  "그렇다 + 려니 하다 (ㅎ tushadi, PK-47). "
                            "“Shunday ekan-da deb qoʻyaverish”. "
                            "Matnning butun mavzusi shu ikki "
                            "soʻzda.",
                "examples": ["“그러려니 해.”",
                             "큰 잘못까지 그러려니 하면 안 된다."],
            },
            {
                "pattern":  "Qolipning chegarasi",
                "meaning":  "Matn qolipni maqtab qoʻymaydi — uning "
                            "chegarasini ham aytadi: 여유 va 포기 "
                            "boshqa narsa. 정보문 ning yaxshisi "
                            "hamisha “lekin” ni ham yozadi.",
                "examples": ["그것은 여유가 아니라 포기다."],
            },
        ],
        "body": '''<p>버스가 십 분 늦는다. 앞차가 갑자기 <span class="cn-word" data-pos="verb" data-tr="kesib oʻtadi">끼어든다</span>. 식당 <span class="cn-word" data-tr="xodim">직원</span>이 <span class="cn-word" data-pos="adj" data-tr="qovogʻi soliq">무뚝뚝하다</span>. 이런 일은 하루에도 여러 번 일어난다.</p>

<p>같은 일을 <span class="cn-word" data-pos="verb" data-tr="boshdan kechirsa ham">겪어도</span> 사람마다 <span class="cn-word" data-tr="munosabat, javob">반응</span>이 다르다. 어떤 사람은 하루 종일 화가 난다. 어떤 사람은 삼십 초 뒤에 잊는다.</p>

<p><span class="cn-word" data-tr="psixologiya">심리학</span>에서는 이 차이를 “<span class="cn-word" data-tr="talqin, izoh">해석</span>”이라고 부른다. <span class="cn-word" data-tr="stress">스트레스</span>를 만드는 것은 <span class="cn-word" data-tr="voqea">사건</span>이 아니다. 그 사건에 <span class="cn-word" data-pos="verb" data-tr="yopishtiradigan">붙이는</span> 설명이다.</p>

<p>앞차가 끼어들었다. 여기까지는 사실이다. “저 사람이 나를 <span class="cn-word" data-pos="verb" data-tr="mensimadi">무시했다</span>” — 이것은 사실이 아니다. 그것은 내가 붙인 설명이다.</p>

<p>한국말에는 이 설명을 바꾸는 짧은 문장이 있다.</p>

<p>“<span class="cn-word" data-pos="verb" data-tr="shunday ekan-da deb qoʻyaver">그러려니 해</span>.”</p>

<p>이 말의 뜻은 “참아라”가 아니다. 설명을 붙이지 않는 것이다. 앞차가 끼어들었다. 이유는 모른다. <span class="cn-word" data-pos="verb" data-tr="shoshilinch ishi bordir deb qoʻyadi">급한 일이 있으려니 한다</span>. 그리고 지나간다.</p>

<p><span class="cn-word" data-tr="tadqiqot">연구</span> 결과도 이 <span class="cn-word" data-tr="munosabat, yondashuv">태도</span>를 <span class="cn-word" data-pos="verb" data-tr="qoʻllab-quvvatlaydi">지지한다</span>. 작은 일에 설명을 적게 붙이는 사람은 스트레스 <span class="cn-word" data-tr="koʻrsatkich">수치</span>가 낮고, 잠을 더 잘 잔다.</p>

<p>물론 <span class="cn-word" data-tr="chegara">한계</span>가 있다. 큰 <span class="cn-word" data-tr="xato, ayb">잘못</span>까지 그러려니 하면 안 된다. 그것은 <span class="cn-word" data-tr="xotirjamlik, keng koʻngillik">여유</span>가 아니라 <span class="cn-word" data-tr="taslim boʻlish">포기</span>다.</p>

<p><span class="cn-word" data-tr="mezon">기준</span>은 간단하다. 내가 바꿀 수 있는 일이면 말한다. 바꿀 수 없는 일이면 <span class="cn-word" data-pos="verb" data-tr="shunday ekan-da deb qoʻyadi">그러려니 한다</span>.</p>

<p>버스는 내가 바꿀 수 없다. 그래서 그러려니 한다. 그리고 그 십 분 동안 다른 것을 본다.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, stressni nima yaratadi?",
                "choices": [
                    "Voqeaning oʻzi",
                    "Voqeaga biz qoʻshadigan izoh (해석)",
                    "Uyqu yetishmasligi",
                    "Boshqa odamlarning qoʻpolligi",
                ],
                "answer": 1,
                "explanation": "“스트레스를 만드는 것은 사건이 아니다. 그 "
                               "사건에 붙이는 설명이다.” Oldingi mashina "
                               "kesib oʻtgani — fakt; “meni mensimadi” — "
                               "izoh.",
            },
            {
                "text": "“그러려니 해” aslida nimani anglatadi?",
                "choices": [
                    "“Chida, jim tur”",
                    "“Izoh qoʻshma” — sababini bilmaganingda oʻzingdan "
                    "hikoya toʻqima",
                    "“Unut va kechir”",
                    "“Hech kimga ishonma”",
                ],
                "answer": 1,
                "explanation": "“이 말의 뜻은 ‘참아라’가 아니다. 설명을 "
                               "붙이지 않는 것이다.” Farq muhim: sabr emas, "
                               "toʻqishni toʻxtatish.",
            },
            {
                "text": "Matn bu yondashuvning chegarasini qanday "
                        "belgilaydi?",
                "choices": [
                    "Hech qanday chegara yoʻq",
                    "Oʻzgartira oladigan ishni aytish kerak; oʻzgartira "
                    "olmaydiganiga esa 그러려니 — aks holda bu keng "
                    "koʻngillik emas, taslim boʻlish",
                    "Faqat kattalarga tegishli",
                    "Faqat ishda ishlaydi",
                ],
                "answer": 1,
                "explanation": "“내가 바꿀 수 있는 일이면 말한다. 바꿀 수 "
                               "없는 일이면 그러려니 한다.” Va: “그것은 "
                               "여유가 아니라 <b>포기</b>다.”",
            },
        ],
    },
]
