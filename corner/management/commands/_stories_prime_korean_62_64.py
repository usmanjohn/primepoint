# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-62 … PK-64 (-대요, (으)ㄹ 뻔하다, (으)ㄹ 테니까).

Shakl xilma-xilligi (toc dagi "STORIES, NOT DIALOGUES" qoidasiga koʻra),
oʻtgan batchdan boshqacha uchta shakl:
  62 — XAT (편지). Koʻchib ketgan doʻstga yozilgan maktab yangiliklari:
       “…emish” degan gap xatning tabiiy tili.
  63 — BIRINCHI SHAXS hikoyasi. Bitta ertalabdagi besh xavf — hammasi
       “sal boʻlmasa…” bilan tugaydi.
  64 — GURUH hikoyasi. Sinf bayramga tayyorlanadi; har kim “men buni
       qilaman, shuning uchun siz…” deydi.

Kumulyativ qoida: PK-64 gacha oʻrganilgan hamma narsa ochiq.
PK-62 matnida 뻔하다 (63) va ㄹ 테니까 (64) YOʻQ.
PK-63 matnida ㄹ 테니까 (64) yoʻq.
(으)ㄹ수록 (65), 반면에 (66), 뿐만 아니라 (67), 데다가 (68) — hech
qaysisida yoʻq. (으)ㄹ래요, (으)ㄹ게요, (으)ㄹ지, (으)ㄹ까 ham hali
oʻrganilmagan — ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_62_64.py --author=prime
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
    {
        "title":   "아프소나의 편지",
        "summary": (
            "PK-62 matni. Xat shaklida: Afsona Seulga koʻchib ketgan doʻstiga "
            "maktab yangiliklarini yozadi — butun xat “…emish” bilan toʻla."
        ),
        "order":   62,
        "grammar": [
            {
                "pattern":  "-대요 — darak gapning qisqargan shakli",
                "meaning":  "다고 해요 → 대요. Eshitgan gapni yetkazish: "
                            "oʻzbekchadagi “…emish, …ekan”. Feʼl/sifat "
                            "farqi saqlanadi: 간대요 · 바쁘대요.",
                "examples": ["부산에서 왔대요.",
                             "셰르벡 씨는 요즘 아주 바쁘대요.",
                             "다음 주에 시험이 있대요."],
            },
            {
                "pattern":  "-래요 va -재요 — buyruq va taklif",
                "meaning":  "라고 해요 → 래요 (buyruq), 자고 해요 → 재요 "
                            "(taklif). Buyruqda zamon boʻlmaydi.",
                "examples": ["선생님이 매일 복습하래요.",
                             "시험 날에 늦지 말래요.",
                             "우리한테 같이 가재요."],
            },
            {
                "pattern":  "-냬요 — soʻroq gapning qisqargan shakli",
                "meaning":  "냐고 해요 → 냬요. Eng kam uchraydigani, "
                            "lekin qoidasi bir xil.",
                "examples": ["언제 돌아오냬요."],
            },
        ],
        "body": '''<p><strong>수진 씨에게</strong></p>

<p>수진 씨, 안녕하세요? 저는 아프소나예요. 수진 씨가 <span class="cn-word" data-tr="Seul">서울</span>로 간 후에 우리 반이 조금 <span class="cn-word" data-pos="verb" data-tr="jimib qoldi">조용해졌어요</span>. 오늘은 학교 <span class="cn-word" data-tr="yangilik">소식</span>을 <span class="cn-word" data-pos="verb" data-tr="yetkazaman">전해요</span>.</p>

<p><span class="cn-word" data-pos="adv" data-tr="avvalo">먼저</span>, 우리 반에 새 학생이 왔어요. 이름은 하나예요. <span class="cn-word" data-tr="Pusan">부산</span>에서 <span class="cn-word" data-pos="verb" data-tr="kelgan emish">왔대요</span>. 한국어 <span class="cn-word" data-tr="soʻzlashuv bellashuvi">말하기 대회</span>에서 <span class="cn-word" data-tr="birinchi oʻrin">일 등</span>을 <span class="cn-word" data-pos="verb" data-tr="olgan emish">했대요</span>. 정말 <span class="cn-word" data-pos="adj" data-tr="zoʻr">대단해요</span>.</p>

<p>셰르벡 씨 소식도 있어요. 셰르벡 씨는 요즘 아주 <span class="cn-word" data-pos="adj" data-tr="band emish">바쁘대요</span>. 매일 아침 여섯 시에 <span class="cn-word" data-pos="verb" data-tr="turar emish">일어난대요</span>. <span class="cn-word" data-tr="taʼtil">방학</span>에 한국에 <span class="cn-word" data-pos="verb" data-tr="boradi emish">간대요</span>. 그리고 우리한테 같이 <span class="cn-word" data-pos="verb" data-tr="boraylik deyapti">가재요</span>. 저는 가고 싶지만 돈이 없어요.</p>

<p>선생님 소식도 있어요. 다음 주에 시험이 <span class="cn-word" data-pos="verb" data-tr="bor emish">있대요</span>. 선생님이 매일 <span class="cn-word" data-pos="verb" data-tr="takrorlanglar deyapti">복습하래요</span>. 그리고 시험 날에 <span class="cn-word" data-pos="verb" data-tr="kechikmanglar deyapti">늦지 말래요</span>. 우리 반 친구들은 벌써 <span class="cn-word" data-pos="verb" data-tr="qoʻrqib qoldi">걱정하고 있어요</span>.</p>

<p>아, 딜노자 씨가 수진 씨한테 <span class="cn-word" data-pos="verb" data-tr="qachon qaytasiz deb soʻrayapti">언제 돌아오냬요</span>. 우리 모두 수진 씨가 <span class="cn-word" data-pos="verb" data-tr="sogʻindik">보고 싶어요</span>. <span class="cn-word" data-tr="javob xat">답장</span>을 기다려요.</p>

<p><strong>아프소나 <span class="cn-word" data-tr="hurmat bilan (xat oxiri)">드림</span></strong></p>''',
        "questions": [
            {
                "text": "Yangi oʻquvchi Hana haqida nima aytilgan?",
                "choices": [
                    "Seuldan kelgan va qoʻshiq kuylaydi",
                    "Pusandan kelgan va koreys tili bellashuvida birinchi "
                    "oʻrinni olgan",
                    "Afsonaning qarindoshi",
                    "Kelasi oy koʻchib ketadi",
                ],
                "answer": 1,
                "explanation": "“부산에서 <b>왔대요</b>… 일 등을 "
                               "<b>했대요</b>” — ikkalasi ham 대요, yaʼni "
                               "Afsona buni oʻzi koʻrmagan, eshitgan.",
            },
            {
                "text": "Oʻqituvchi nima qilishni aytgan?",
                "choices": [
                    "Har kuni takrorlashni va imtihon kuni kechikmaslikni",
                    "Imtihonga tayyorlanmaslikni",
                    "Seulga borishni",
                    "Xat yozishni",
                ],
                "answer": 0,
                "explanation": "“매일 <b>복습하래요</b>… 늦지 "
                               "<b>말래요</b>” — 라고 해요 va 지 말라고 "
                               "해요 ning qisqargan shakllari.",
            },
            {
                "text": "“같이 가재요” va “복습하래요” — farqi nimada?",
                "choices": [
                    "Birinchisi buyruq, ikkinchisi taklif",
                    "Birinchisi taklif (“birga boraylik”), ikkinchisi "
                    "buyruq (“takrorlanglar”)",
                    "Ikkalasi ham savol",
                    "Ikkalasi ham darak gap",
                ],
                "answer": 1,
                "explanation": "<b>재요</b> ← 자고 해요 (taklif). "
                               "<b>래요</b> ← 라고 해요 (buyruq). Bitta "
                               "harf butun gap turini oʻzgartiradi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "어제는 정말 위험했어요",
        "summary": (
            "PK-63 matni. Birinchi shaxsda: bitta ertalabda besh marta "
            "“sal boʻlmasa…” — uygʻonishdan sinfgacha."
        ),
        "order":   63,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄹ 뻔했다",
                "meaning":  "Boʻlishiga oz qoldi, lekin boʻlmadi. "
                            "Oʻzbekchadagi “-(a)yoz-” qoʻshimchasi: "
                            "yiqil-ayoz-dim. Doim oʻtgan zamonda.",
                "examples": ["넘어질 뻔했어요.",
                             "버스를 놓칠 뻔했어요.",
                             "늦을 뻔했어요."],
            },
            {
                "pattern":  "하마터면 … (으)ㄹ 뻔했다",
                "meaning":  "하마터면 — “sal boʻlmasa, oz qoldiki”. Bu "
                            "qolip bilan juftlik boʻlib yuradi va uni "
                            "kuchaytiradi.",
                "examples": ["하마터면 넘어질 뻔했어요.",
                             "하마터면 늦을 뻔했어요."],
            },
            {
                "pattern":  "죽을 뻔했어요 — mubolagʻa",
                "meaning":  "Soʻzma-soʻz “oʻlayozdim”, lekin kundalik "
                            "nutqda “juda qiynaldim” degani. Oʻzbekchada "
                            "ham aynan shunday: “oʻlay dedim”.",
                "examples": ["오늘 아침에 세 번 죽을 뻔했어요."],
            },
        ],
        "body": '''<p>어제 아침에 저는 늦게 일어났어요. <span class="cn-word" data-tr="soat">시계</span>를 봤어요. 여덟 시 십 분이었어요. 학교는 여덟 시 삼십 분에 시작돼요.</p>

<p>저는 <span class="cn-word" data-pos="verb" data-tr="yuz yuvish">세수</span>도 안 하고 <span class="cn-word" data-pos="verb" data-tr="yugurib chiqdim">뛰어나갔어요</span>. <span class="cn-word" data-tr="zinapoya">계단</span>에서 너무 빨리 <span class="cn-word" data-pos="verb" data-tr="tushdim">내려갔어요</span>. 그때 <span class="cn-word" data-tr="oyoq">발</span>이 <span class="cn-word" data-pos="verb" data-tr="sirpandi">미끄러졌어요</span>. <span class="cn-word" data-pos="adv" data-tr="sal boʻlmasa">하마터면</span> <span class="cn-word" data-pos="verb" data-tr="yiqilayozdim">넘어질 뻔했어요</span>. <span class="cn-word" data-pos="adv" data-tr="yaxshi hamki">다행히</span> 손으로 <span class="cn-word" data-tr="devor">벽</span>을 <span class="cn-word" data-pos="verb" data-tr="ushlab qoldim">잡았어요</span>.</p>

<p><span class="cn-word" data-tr="bekat">버스 정류장</span>까지 뛰었어요. 버스가 벌써 <span class="cn-word" data-pos="verb" data-tr="joʻnayotgan edi">출발하고 있었어요</span>. 저는 손을 들었어요. <span class="cn-word" data-tr="haydovchi">기사님</span>이 문을 열어 줬어요. 버스를 <span class="cn-word" data-pos="verb" data-tr="oʻtkazib yuborayozdim">놓칠 뻔했어요</span>.</p>

<p>버스 안에서 가방을 열었어요. 숙제 <span class="cn-word" data-tr="daftar">공책</span>이 없었어요. 저는 정말 <span class="cn-word" data-pos="verb" data-tr="qoʻrqib ketdim">놀랐어요</span>. 하지만 공책은 가방 <span class="cn-word" data-tr="ostida">아래에</span> 있었어요. 숙제를 안 <span class="cn-word" data-pos="verb" data-tr="olib kelmayozdim">가져올 뻔했어요</span>.</p>

<p>학교에 여덟 시 <span class="cn-word" data-tr="yigirma toʻqqiz">이십구</span> 분에 <span class="cn-word" data-pos="verb" data-tr="yetib keldim">도착했어요</span>. 일 분! 하마터면 <span class="cn-word" data-pos="verb" data-tr="kechikayozdim">늦을 뻔했어요</span>.</p>

<p>교실에서 아프소나 씨가 물어봤어요.</p>

<p><strong>아프소나:</strong> 왜 이렇게 <span class="cn-word" data-tr="yuz">얼굴</span>이 <span class="cn-word" data-pos="adj" data-tr="qizarib ketgan">빨개요</span>?</p>

<p>저는 웃었어요. 그리고 말했어요.</p>

<p><strong>저:</strong> 오늘 아침에 세 번 <span class="cn-word" data-pos="verb" data-tr="oʻlay dedim">죽을 뻔했어요</span>.</p>''',
        "questions": [
            {
                "text": "Hikoyachi avtobusga mindimi?",
                "choices": [
                    "Yoʻq, oʻtkazib yubordi",
                    "Ha, mindi — “놓칠 뻔했어요” degani oʻtkazib "
                    "yubormadi degani",
                    "Avtobus kelmadi",
                    "Piyoda ketdi",
                ],
                "answer": 1,
                "explanation": "<b>뻔했어요</b> = boʻlishiga oz qoldi, "
                               "lekin <b>boʻlmadi</b>. Haydovchi eshikni "
                               "ochib bergani ham shuni tasdiqlaydi.",
            },
            {
                "text": "Zinapoyada nima boʻldi?",
                "choices": [
                    "Yiqildi va jarohat oldi",
                    "Oyogʻi sirpandi, lekin devorni ushlab qoldi",
                    "Daftarini tushirib yubordi",
                    "Hech narsa boʻlmadi",
                ],
                "answer": 1,
                "explanation": "“하마터면 <b>넘어질 뻔했어요</b>. 다행히 "
                               "손으로 벽을 잡았어요” — 하마터면 bu "
                               "qolipning doimiy hamrohi.",
            },
            {
                "text": "Oxirgi jumladagi “세 번 죽을 뻔했어요” nima degani?",
                "choices": [
                    "Uch marta haqiqatan oʻlim xavfi boʻldi",
                    "Uch marta juda qiynaldi — bu mubolagʻa",
                    "Uch marta kechikdi",
                    "Uch marta yiqildi",
                ],
                "answer": 1,
                "explanation": "죽을 뻔했어요 kundalik nutqda mubolagʻa — "
                               "oʻzbekchadagi “<b>oʻlay dedim</b>” bilan "
                               "aynan bir xil ishlaydi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "학교 축제 준비",
        "summary": (
            "PK-64 matni. Hech kim boshlamaydigan yigʻilishni bitta jumla "
            "harakatga soladi: “men buni qilaman, shuning uchun siz…”."
        ),
        "order":   64,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄹ 테니까 — niyat",
                "meaning":  "Ega “men” boʻlganda bu vaʼda: “men buni oʻz "
                            "zimmamga olaman, shuning uchun siz…”. "
                            "Keyingi gapda buyruq yoki taklif keladi.",
                "examples": ["제가 음식을 맡을 테니까 사진을 맡으세요.",
                             "제가 사진을 찍을 테니까 음악을 준비하세요."],
            },
            {
                "pattern":  "(으)ㄹ 테니까 — kuchli taxmin",
                "meaning":  "Ega boshqa odam yoki narsa boʻlsa, maʼno "
                            "taxminga oʻzgaradi: “…sa kerak”.",
                "examples": ["사람이 많을 테니까 일찍 오세요.",
                             "늦게 끝날 테니까 미리 말하세요."],
            },
            {
                "pattern":  "Eslatma: -대요 qaytadi",
                "meaning":  "Oxirgi jumla PK-62 dagi qisqargan koʻchirma "
                            "gap — hikoyachi buni oʻzi koʻrmagan, "
                            "eshitgan.",
                "examples": ["교실이 제일 인기가 많았대요."],
            },
        ],
        "body": '''<p>다음 달에 학교 <span class="cn-word" data-tr="bayram, festival">축제</span>가 있어요. <span class="cn-word" data-tr="ikkinchi kurs uchinchi sinf">이 학년 삼 반</span> 학생들이 방과 후에 교실에 <span class="cn-word" data-pos="verb" data-tr="toʻplandi">모였어요</span>. 하지만 <span class="cn-word" data-pos="adv" data-tr="hech kim">아무도</span> 먼저 말하지 않았어요. 일이 너무 많았기 때문이에요.</p>

<p>그때 자스루르 씨가 <span class="cn-word" data-pos="verb" data-tr="oʻrnidan turdi">일어났어요</span>.</p>

<p><strong>자스루르:</strong> 제가 음식을 <span class="cn-word" data-pos="verb" data-tr="zimmamga olaman">맡을 테니까</span> 아프소나 씨는 사진을 <span class="cn-word" data-pos="verb" data-tr="zimmangizga oling">맡으세요</span>.</p>

<p>아프소나 씨가 웃었어요. 그리고 딜노자 씨한테 말했어요.</p>

<p><strong>아프소나:</strong> 제가 사진을 찍을 테니까 딜노자 씨는 <span class="cn-word" data-tr="musiqa">음악</span>을 준비하세요.</p>

<p>십 분 후에 <span class="cn-word" data-tr="hamma ish">모든 일</span>이 <span class="cn-word" data-pos="verb" data-tr="hal boʻldi">정해졌어요</span>. 셰르벡 씨는 <span class="cn-word" data-tr="chipta">표</span>를 만들기로 했어요. 베크조드 씨는 교실을 <span class="cn-word" data-pos="verb" data-tr="bezashga">꾸미기로</span> 했어요.</p>

<p><span class="cn-word" data-pos="adv" data-tr="oxirida">마지막에</span> 선생님이 교실에 들어왔어요. 선생님은 학생들을 보고 놀랐어요.</p>

<p><strong>선생님:</strong> 벌써 다 정했어요?</p>

<p><strong>딜노자:</strong> 네! 자스루르 씨가 <span class="cn-word" data-pos="verb" data-tr="boshladi">시작했어요</span>.</p>

<p>선생님이 웃으면서 말했어요.</p>

<p><strong>선생님:</strong> 좋아요. 축제 날에 사람이 많을 테니까 일찍 오세요. 그리고 늦게 <span class="cn-word" data-pos="verb" data-tr="tugasa kerak">끝날 테니까</span> <span class="cn-word" data-tr="ota-ona">부모님</span>한테 <span class="cn-word" data-pos="adv" data-tr="oldindan">미리</span> 말하세요.</p>

<p>축제 날, 이 학년 삼 반의 교실이 제일 <span class="cn-word" data-pos="adj" data-tr="mashhur edi emish">인기가 많았대요</span>.</p>''',
        "questions": [
            {
                "text": "Yigʻilish nega boshida sekin ketdi?",
                "choices": [
                    "Oʻqituvchi kelmagani uchun",
                    "Ish juda koʻp boʻlgani uchun hech kim birinchi "
                    "boʻlib gapirmadi",
                    "Sinf boʻsh edi",
                    "Bayram bekor qilingan edi",
                ],
                "answer": 1,
                "explanation": "“<b>아무도</b> 먼저 말하지 않았어요. 일이 "
                               "너무 많았기 <b>때문이에요</b>” — 기 때문에 "
                               "(PK-49) bilan berilgan sabab.",
            },
            {
                "text": "“제가 음식을 맡을 테니까 아프소나 씨는 사진을 "
                        "맡으세요” — bu gapda nima qilinyapti?",
                "choices": [
                    "Taxmin aytilyapti",
                    "Vaʼda berilyapti va shuning evaziga boshqadan ish "
                    "soʻralyapti",
                    "Buyruq bekor qilinyapti",
                    "Savol berilyapti",
                ],
                "answer": 1,
                "explanation": "Ega <b>men</b> — demak (으)ㄹ 테니까 "
                               "niyat/vaʼda bildiradi, va keyingi gapda "
                               "<b>boshqa odamga</b> qaratilgan buyruq "
                               "keladi. Qolipning ikkala sharti ham "
                               "shu yerda.",
            },
            {
                "text": "Oʻqituvchining “사람이 많을 테니까” gapi qaysi "
                        "maʼnoda?",
                "choices": [
                    "Vaʼda — oʻqituvchi odam olib keladi",
                    "Kuchli taxmin — odam koʻp boʻlsa kerak",
                    "Buyruq — koʻp odam chaqiringlar",
                    "Taqiq",
                ],
                "answer": 1,
                "explanation": "Ega <b>사람</b> — boshqa, shuning uchun "
                               "maʼno vaʼdadan <b>taxmin</b>ga oʻzgaradi. "
                               "Keyingi gap esa yana buyruq: 일찍 오세요.",
            },
        ],
    },
]
