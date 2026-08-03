# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-68 … PK-70 (데다가, 바람에/탓에/느라고, ㄹ걸 그랬다).

Uchta matn darslar bilan bitta yoʻnalishda boradi: muammolar USTMA-UST
tushadi (68) → AYB va bahona qidiriladi (69) → PUSHAYMONLIK qoladi (70).

Shakl xilma-xilligi (toc dagi "STORIES, NOT DIALOGUES" qoidasi):
  68 — ONLAYN SHARH (후기), yulduzli baho bilan. Shikoyat sharhida
       muammolar tabiiy ravishda bir-birining ustiga tushadi.
  69 — KULGILI HIKOYA, takrorlanuvchi tuzilishda: har kuni yangi bahona.
  70 — MASLAHAT USTUNI (조언) — bitiruvchi kichik kursdoshlarga yozadi.

Kumulyativ qoida: PK-70 gacha oʻrganilgan hamma narsa ochiq.
PK-68 matnida 바람에/탓에/느라고 (69) va ㄹ걸 그랬다 (70) YOʻQ.
PK-69 matnida ㄹ걸 그랬다 / 았어야 했다 (70) yoʻq.
(으)ㄹ 겸 (71), 기 마련이다 (72), (으)ㄹ지도 모르다 (73) — yoʻq.
(으)ㄹ게요, (으)ㄹ까요, (으)ㄹ지, 는데, 네요, (으)시 hurmat shakli ham
hali oʻrganilmagan — ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_68_70.py --author=prime
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
        "title":   "산속 호텔 후기 — 별 두 개",
        "summary": (
            "PK-68 matni. Onlayn sharh shaklida: togʻdagi mehmonxonada har bir "
            "muammo boshqasining ustiga tushadi — lekin manzara hammasini yuvadi."
        ),
        "order":   68,
        "grammar": [
            {
                "pattern":  "(으)ㄴ/는 데다가",
                "meaning":  "Ikkinchi holat birinchisining ustiga tushadi va "
                            "vaziyatni ogʻirlashtiradi — oʻzbekchadagi "
                            "“ustiga ustak”. Feʼl 는, sifat (으)ㄴ oladi.",
                "examples": ["길이 좁은 데다가 표지판도 없었어요.",
                             "에어컨이 고장 난 데다가 모기까지 있었어요.",
                             "공기가 맑은 데다가 경치도 아름다웠어요."],
            },
            {
                "pattern":  "Bir yoʻnalish qoidasi",
                "meaning":  "데다가 ikkala tomonni bir yoʻnalishga qoʻyadi: "
                            "matndagi salbiy misollar ham, oxiridagi ijobiy "
                            "misol ham shu qoidaga boʻysunadi.",
                "examples": ["방이 작은 데다가 창문도 없었어요.",
                             "산 공기가 맑은 데다가 경치도 좋았어요."],
            },
            {
                "pattern":  "Eslatma: 반면에 va 뿐",
                "meaning":  "Oxirgi xulosa PK-66 va PK-67 ni qaytaradi: "
                            "qarama-qarshi tomonlar uchun 반면에, “faqat, "
                            "xolos” uchun 뿐.",
                "examples": ["경치는 최고인 반면에 시설은 최악이에요.",
                             "종류도 세 가지뿐이었어요."],
            },
        ],
        "body": '''<p><strong>★★☆☆☆ · 딜노자 · 8월 1일</strong></p>

<p>지난 주말에 가족과 함께 <span class="cn-word" data-tr="togʻdagi mehmonxona">산속 호텔</span>에 <span class="cn-word" data-tr="ikki kun">이틀</span> 동안 <span class="cn-word" data-pos="verb" data-tr="qoʻndik">묵었어요</span>. 사진이 아주 예뻤어요. 그래서 <span class="cn-word" data-tr="umid">기대</span>가 컸어요. 하지만…</p>

<p><span class="cn-word" data-tr="yetib borish">도착</span>부터 문제였어요. 길이 <span class="cn-word" data-pos="adj" data-tr="tor boʻlgani yetmagandek">좁은 데다가</span> <span class="cn-word" data-tr="yoʻl belgisi">표지판</span>도 없어서 두 시간이나 <span class="cn-word" data-pos="verb" data-tr="adashib yurdik">헤맸어요</span>.</p>

<p>방도 좋지 않았어요. 방이 <span class="cn-word" data-pos="adj" data-tr="kichkina boʻlgani yetmagandek">작은 데다가</span> 창문도 없었어요. <span class="cn-word" data-tr="konditsioner">에어컨</span>이 <span class="cn-word" data-pos="verb" data-tr="buzilgani yetmagandek">고장 난 데다가</span> 밤에는 <span class="cn-word" data-tr="chivin">모기</span>까지 있었어요. 잠을 거의 못 잤어요.</p>

<p><span class="cn-word" data-tr="nonushta">아침 식사</span>도 <span class="cn-word" data-pos="verb" data-tr="erta tugagani yetmagandek">일찍 끝나는 데다가</span> <span class="cn-word" data-tr="tur">종류</span>도 <span class="cn-word" data-tr="uch xil">세 가지</span>뿐이었어요.</p>

<p>하지만 좋은 <span class="cn-word" data-tr="tomon">점</span>도 있었어요. 산 <span class="cn-word" data-tr="havo">공기</span>가 <span class="cn-word" data-pos="adj" data-tr="toza boʻlgani ustiga">맑은 데다가</span> <span class="cn-word" data-tr="manzara">경치</span>도 정말 아름다웠어요. 아침에 <span class="cn-word" data-tr="qush ovozi">새 소리</span>를 들으면서 <span class="cn-word" data-pos="verb" data-tr="sayr qildim">산책했어요</span>. 그건 <span class="cn-word" data-tr="eng zoʻri">최고</span>였어요.</p>

<p><span class="cn-word" data-tr="xulosa">결론</span>이에요. 경치는 최고인 반면에 <span class="cn-word" data-tr="sharoit">시설</span>은 <span class="cn-word" data-tr="eng yomoni">최악</span>이에요. 그래서 별 두 개예요. 산에 가고 싶은 사람은 가세요. 하지만 잘 <span class="cn-word" data-tr="joy">곳</span>을 찾는 사람은 <span class="cn-word" data-pos="verb" data-tr="oʻylab koʻring">다시 생각해 보세요</span>.</p>''',
        "questions": [
            {
                "text": "Nima uchun mehmonxonaga yetib borish ikki soat "
                        "davom etdi?",
                "choices": [
                    "Yoʻl tor edi va yoʻl belgilari ham yoʻq edi",
                    "Yomgʻir yogʻdi",
                    "Mashina buzildi",
                    "Ular kech chiqishdi",
                ],
                "answer": 0,
                "explanation": "“길이 <b>좁은 데다가</b> 표지판도 없어서” — "
                               "ikkita muammo bir-birining ustiga tushdi "
                               "va natija berdi.",
            },
            {
                "text": "Xonada nima muammo boʻldi?",
                "choices": [
                    "Faqat konditsioner ishlamadi",
                    "Kichkina, derazasiz, konditsioneri buzuq va chivin bor edi",
                    "Juda shovqinli edi",
                    "Hech qanday muammo boʻlmadi",
                ],
                "answer": 1,
                "explanation": "Ikkita 데다가 ketma-ket kelgan: 작은 데다가 "
                               "창문도 없었어요, 고장 난 데다가 모기<b>까지</b> "
                               "있었어요. <b>까지</b> ohangni yanada "
                               "kuchaytiradi.",
            },
            {
                "text": "“산 공기가 맑은 데다가 경치도 아름다웠어요” — nega bu "
                        "yerda ham 데다가 ishlatilgan?",
                "choices": [
                    "Chunki bu ham salbiy",
                    "Chunki ikkala tomon ham ijobiy — 데다가 uchun muhimi "
                    "bir yoʻnalishda boʻlishi",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 맑다 sifat",
                ],
                "answer": 1,
                "explanation": "데다가 “yomon” degani emas — u ikkinchi "
                               "narsani birinchisining <b>ustiga</b> "
                               "qoʻyadi. Muhimi ikkalasi ham bir "
                               "yoʻnalishda boʻlishi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "지각 대장 베크조드",
        "summary": (
            "PK-69 matni. Har kuni kechikadigan Bekzodning bahonalari — "
            "dushanbadan jumagacha, har kuni yangisi."
        ),
        "order":   69,
        "grammar": [
            {
                "pattern":  "는 바람에 — kutilmagan xalaqit",
                "meaning":  "Toʻsatdan bir narsa rejani buzdi va natija "
                            "salbiy boʻldi. Faqat feʼl bilan, faqat 는 "
                            "shaklida — zamon qoʻyilmaydi.",
                "examples": ["늦잠을 자는 바람에 늦었어요.",
                             "버스가 고장 나는 바람에 늦었어요."],
            },
            {
                "pattern":  "느라고 — bahona",
                "meaning":  "“…ga ovora boʻlib”. Ikkala gapning egasi bir "
                            "xil boʻlishi shart, va ikkinchi gap salbiy.",
                "examples": ["게임을 하느라고 숙제를 못 했어요.",
                             "동생을 깨우느라고 늦었어요."],
            },
            {
                "pattern":  "탓에 va 덕분에",
                "meaning":  "탓 — “ayb”, 덕분 — “sharofat”. Oxirgi jumla "
                            "ikkalasini yonma-yon qoʻyadi.",
                "examples": ["일찍 잔 탓에 너무 일찍 깼어요.",
                             "베크조드 씨 덕분에 아침마다 웃어요."],
            },
        ],
        "body": '''<p>베크조드 씨는 우리 반의 <span class="cn-word" data-tr="kechikish boshligʻi">지각 대장</span>이에요. 일주일에 세 번은 늦어요. 그런데 <span class="cn-word" data-tr="bahona">변명</span>은 매일 <span class="cn-word" data-pos="adj" data-tr="boshqacha">달라요</span>.</p>

<p>월요일에는 <span class="cn-word" data-pos="verb" data-tr="uxlab qolgani tufayli">늦잠을 자는 바람에</span> 늦었어요.</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="budilnik">알람</span>이 <span class="cn-word" data-pos="verb" data-tr="jiringlamadi">안 울렸어요</span>!</p>

<p>화요일에는 버스가 <span class="cn-word" data-pos="verb" data-tr="buzilib qolgani tufayli">고장 나는 바람에</span> 늦었어요. 이건 <span class="cn-word" data-pos="adv" data-tr="rostdan">진짜</span>였어요. 반 친구들도 그 버스를 봤어요.</p>

<p>수요일에는 <span class="cn-word" data-pos="verb" data-tr="oʻyinga ovora boʻlib">게임을 하느라고</span> 숙제를 못 했어요. 그래서 아침에 <span class="cn-word" data-pos="adv" data-tr="shoshib">급하게</span> 숙제를 하느라고 또 늦었어요.</p>

<p>목요일에 선생님이 물어봤어요.</p>

<p><strong>선생님:</strong> 오늘은 왜 늦었어요?</p>

<p><strong>베크조드:</strong> 동생을 <span class="cn-word" data-pos="verb" data-tr="uygʻotishga ovora boʻlib">깨우느라고</span> 늦었어요.</p>

<p>반 친구들이 모두 웃었어요. 동생은 <span class="cn-word" data-tr="besh yosh">다섯 살</span>이에요.</p>

<p>금요일 아침, <span class="cn-word" data-tr="ajablanarli ish">놀라운 일</span>이 <span class="cn-word" data-pos="verb" data-tr="yuz berdi">일어났어요</span>. 베크조드 씨가 <span class="cn-word" data-pos="adv" data-tr="eng birinchi">제일 먼저</span> 교실에 <span class="cn-word" data-pos="verb" data-tr="oʻtirgan edi">앉아 있었어요</span>. 여덟 시 십 분이었어요.</p>

<p><strong>아프소나:</strong> 오늘은 어떻게 일찍 왔어요?</p>

<p><strong>베크조드:</strong> 어제 <span class="cn-word" data-pos="verb" data-tr="erta uxlaganim aybi bilan">일찍 잔 탓에</span> 너무 일찍 <span class="cn-word" data-pos="verb" data-tr="uygʻonib ketdim">깼어요</span>.</p>

<p>모두 또 웃었어요. 베크조드 씨는 <span class="cn-word" data-tr="oʻz aybi">자기 탓</span>도, <span class="cn-word" data-tr="oʻzganing aybi">남의 탓</span>도 잘해요. 하지만 반 친구들은 베크조드 씨 <span class="cn-word" data-tr="sharofati bilan">덕분에</span> 아침마다 웃어요.</p>''',
        "questions": [
            {
                "text": "Chorshanba kuni Bekzod nega kechikdi?",
                "choices": [
                    "Avtobus buzilgani uchun",
                    "Ertalab shoshib uy vazifasini qilishga ovora boʻlgani uchun",
                    "Budilnik jiringlamagani uchun",
                    "Ukasini uygʻotgani uchun",
                ],
                "answer": 1,
                "explanation": "Kechqurun 게임을 <b>하느라고</b> vazifani "
                               "qilmadi, ertalab esa 숙제를 <b>하느라고</b> "
                               "kechikdi — bitta xato ikkinchisini "
                               "tugʻdirdi.",
            },
            {
                "text": "Juma kuni nima kutilmagan hodisa boʻldi?",
                "choices": [
                    "Bekzod umuman kelmadi",
                    "Bekzod hammadan birinchi boʻlib keldi",
                    "Oʻqituvchi kechikdi",
                    "Dars bekor qilindi",
                ],
                "answer": 1,
                "explanation": "“베크조드 씨가 <b>제일 먼저</b> 교실에 앉아 "
                               "있었어요” — va sababi ham kulgili: erta "
                               "uxlagani <b>aybi bilan</b> juda erta "
                               "uygʻonib ketdi.",
            },
            {
                "text": "Oxirgi jumlada 탓 va 덕분에 nega yonma-yon "
                        "qoʻyilgan?",
                "choices": [
                    "Ikkalasi bir xil maʼnoni beradi",
                    "Biri ayb, ikkinchisi sharofat — Bekzod ayb qidiradi, "
                    "lekin sinfga kulgi olib keladi",
                    "Ikkalasi ham salbiy",
                    "Bu grammatik xato",
                ],
                "answer": 1,
                "explanation": "<b>탓</b> — yomon natija (“aybi bilan”), "
                               "<b>덕분에</b> — yaxshi natija (“sharofati "
                               "bilan”). Hikoyaning hazili aynan shu "
                               "juftlikda.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "후배들에게 — 졸업생의 조언",
        "summary": (
            "PK-70 matni. Maslahat ustuni: bitiruvchi Sherbek kichik "
            "kursdoshlarga uch yillik afsuslarini yozadi."
        ),
        "order":   70,
        "grammar": [
            {
                "pattern":  "(으)ㄹ걸 그랬다 — shaxsiy afsus",
                "meaning":  "“…sam boʻlardi”. Faqat soʻzlovchining oʻzi "
                            "haqida; hissiy, ogʻzaki ohang. 걸 dan oldin "
                            "zamon qoʻshimchasi qoʻyilmaydi.",
                "examples": ["그때 시작할걸 그랬어요.",
                             "먼저 사과할걸 그랬어요."],
            },
            {
                "pattern":  "았/었어야 했다 — bajarilmagan majburiyat",
                "meaning":  "“…shim kerak edi”. Kuchliroq va obyektivroq; "
                            "boshqa odam haqida ham aytiladi.",
                "examples": ["모르는 것을 물어봤어야 했어요."],
            },
            {
                "pattern":  "Eslatma: koʻchirma gap qaytadi",
                "meaning":  "Oxirgi jumla PK-61 dagi 라고 하다 ni "
                            "ishlatadi — boshqaning (bu yerda: kelajakdagi "
                            "oʻzingizning) gapini keltirish.",
                "examples": ["“할걸 그랬어요”라고 말하지 마세요."],
            },
        ],
        "body": '''<p><strong>학교 신문 · <span class="cn-word" data-tr="bitiruvchining maslahati">졸업생의 조언</span></strong></p>

<p><span class="cn-word" data-tr="kichik kursdosh">후배</span> 여러분, 안녕하세요. 저는 올해 <span class="cn-word" data-pos="verb" data-tr="bitirayotgan">졸업하는</span> 셰르벡이에요. <span class="cn-word" data-tr="uch yil">삼 년</span>이 정말 빨리 <span class="cn-word" data-pos="verb" data-tr="oʻtib ketdi">지나갔어요</span>. 오늘은 제 <span class="cn-word" data-tr="afsus">후회</span>를 이야기하고 싶어요.</p>

<p><span class="cn-word" data-tr="birinchidan">첫째</span>, 저는 <span class="cn-word" data-tr="birinchi kurs">일 학년</span> 때 한국어를 시작하지 않았어요. 그때 <span class="cn-word" data-pos="verb" data-tr="boshlasam boʻlardi">시작할걸 그랬어요</span>. 지금은 시간이 <span class="cn-word" data-pos="adj" data-tr="yetishmaydi">부족해요</span>. 여러분은 <span class="cn-word" data-pos="adv" data-tr="erta">일찍</span> 시작하세요.</p>

<p><span class="cn-word" data-tr="ikkinchidan">둘째</span>, 저는 친구들과 자주 <span class="cn-word" data-pos="verb" data-tr="urishdim">싸웠어요</span>. 아주 작은 일이었어요. 그때 <span class="cn-word" data-pos="adv" data-tr="birinchi boʻlib">먼저</span> <span class="cn-word" data-pos="verb" data-tr="kechirim soʻrasam boʻlardi">사과할걸 그랬어요</span>. 지금은 그 친구들을 자주 못 봐요.</p>

<p><span class="cn-word" data-tr="uchinchidan">셋째</span>, 저는 선생님한테 <span class="cn-word" data-tr="savol">질문</span>을 하지 않았어요. <span class="cn-word" data-pos="adj" data-tr="uyalganim uchun">부끄러웠기 때문이에요</span>. 하지만 <span class="cn-word" data-tr="bilmagan narsani">모르는 것</span>을 <span class="cn-word" data-pos="verb" data-tr="soʻrashim kerak edi">물어봤어야 했어요</span>. 선생님은 <span class="cn-word" data-pos="adv" data-tr="doim">언제나</span> 도와줬어요.</p>

<p><span class="cn-word" data-tr="oxirgi">마지막</span>으로, 잘한 일도 있어요. 저는 매일 <span class="cn-word" data-tr="kundalik">일기</span>를 썼어요. 그건 정말 잘한 일이에요. 여러분도 <span class="cn-word" data-pos="verb" data-tr="yozib koʻring">써 보세요</span>.</p>

<p>후배 여러분, 시간은 <span class="cn-word" data-pos="verb" data-tr="kutib turmaydi">기다려 주지 않아요</span>. 오늘 할 수 있는 일을 내일로 <span class="cn-word" data-pos="verb" data-tr="qoldirmang">미루지 마세요</span>. 그리고 <span class="cn-word" data-tr="uch yildan keyin">삼 년 후에</span> 저처럼 “할걸 그랬어요”라고 말하지 마세요.</p>

<p><strong>졸업생 셰르벡</strong></p>''',
        "questions": [
            {
                "text": "Sherbekning birinchi afsusi nima?",
                "choices": [
                    "Kundalik yozmagani",
                    "Koreys tilini birinchi kursda boshlamagani",
                    "Doʻstlari bilan urishgani",
                    "Oʻqituvchiga savol bermagani",
                ],
                "answer": 1,
                "explanation": "“그때 <b>시작할걸 그랬어요</b>” — (으)ㄹ걸 "
                               "그랬다 aynan shunday shaxsiy afsus uchun.",
            },
            {
                "text": "Nega Sherbek oʻqituvchidan savol bermagan edi?",
                "choices": [
                    "Uyalgani uchun",
                    "Vaqti boʻlmagani uchun",
                    "Oʻqituvchi band boʻlgani uchun",
                    "Hammasini bilgani uchun",
                ],
                "answer": 0,
                "explanation": "“<b>부끄러웠기 때문이에요</b>” — 기 때문에 "
                               "(PK-49) bilan berilgan sabab. Va u buni "
                               "endi afsus bilan eslaydi.",
            },
            {
                "text": "“물어봤어야 했어요” va “사과할걸 그랬어요” — farqi "
                        "nimada?",
                "choices": [
                    "Ikkalasi bir xil",
                    "Birinchisi — bajarilmagan majburiyat (kuchliroq, "
                    "obyektiv); ikkinchisi — shaxsiy, hissiy afsus",
                    "Birinchisi kelasi zamon",
                    "Ikkinchisi boshqa odam haqida",
                ],
                "answer": 1,
                "explanation": "<b>았/었어야 했다</b> — “qilishim kerak "
                               "edi”, boshqa odam haqida ham aytiladi. "
                               "<b>(으)ㄹ걸 그랬다</b> — “…sam boʻlardi”, "
                               "faqat oʻzi haqida.",
            },
        ],
    },
]
