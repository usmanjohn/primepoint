# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-56 … PK-58 (majhul, orttirma, 아/어 버리다).

Kumulyativ qoida: PK-58 gacha oʻrganilgan hamma narsa ochiq.
PK-56 matnida orttirma nisbat (57) va 버리다 (58) hali YOʻQ.
PK-57 matnida 버리다 hali yoʻq.
아/어 놓다 · 두다 (59), koʻchirma gap (60–62), (으)ㄹ 뻔하다 (63) —
hech qaysisida yoʻq. (으)ㄹ게요, 네요, 는데, (으)ㄹ까요 ham hali
oʻrganilmagan — ishlatilmadi.

Uchta matn bitta ertalab-kechqurun ipiga tizilgan: 56 da maktabning
eshigi ochilmaydi, 57 da uy ichidagi ertalab, 58 da juma kechqurun.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_56_58.py --author=prime
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
        "title":   "문이 안 열려요",
        "summary": (
            "PK-56 matni. Sherbekning ertalabki omadsiz kuni — eshik ochilmaydi, "
            "chiroq oʻchadi, oʻqituvchi kechikadi. Majhul nisbat matn ichida."
        ),
        "order":   56,
        "grammar": [
            {
                "pattern":  "동사 + 이/히/리/기 — majhul nisbat",
                "meaning":  "Ish bajaruvchisi emas, ishning oʻzi muhim "
                            "boʻlganda. Oʻzbekcha “-il-” qoʻshimchasi bilan "
                            "bir xil ish qiladi: och-il-di · 열-리-다.",
                "examples": ["문이 안 열려요.",
                             "안에서 소리가 들렸어요.",
                             "바람에 문이 닫혔어요.",
                             "길이 많이 막혔어요."],
            },
            {
                "pattern":  "아/어지다 — ikkinchi majhul yoʻli",
                "meaning":  "Feʼlda 이/히/리/기 shakli boʻlmasa, majhul "
                            "아/어 + 지다 bilan yasaladi: 끄다 → 꺼지다.",
                "examples": ["갑자기 불이 꺼졌어요."],
            },
            {
                "pattern":  "하다 → 되다",
                "meaning":  "하다 bilan tugaydigan feʼllar majhulga 되다 "
                            "bilan oʻtadi: 시작하다 → 시작되다.",
                "examples": ["수업은 아홉 시에 시작돼요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨는 아침 <span class="cn-word" data-pos="adv" data-tr="erta">일찍</span> 학교에 갔어요. 그런데 <span class="cn-word" data-tr="sinf xonasi">교실</span> 문이 안 <span class="cn-word" data-pos="verb" data-tr="ochilmadi">열렸어요</span>.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-pos="adj" data-tr="gʻalati">이상해요</span>. 어제는 잘 열렸어요.</p>

<p>안에서 작은 <span class="cn-word" data-tr="ovoz">소리</span>가 <span class="cn-word" data-pos="verb" data-tr="eshitildi">들렸어요</span>. <span class="cn-word" data-tr="deraza">창문</span>으로 보니까 지영 씨가 <span class="cn-word" data-pos="verb" data-tr="koʻrindi">보였어요</span>.</p>

<p><strong>셰르벡:</strong> 지영 씨! 문이 안 열려요!</p>

<p><strong>지영:</strong> 아, <span class="cn-word" data-tr="shamoldan">바람에</span> 문이 <span class="cn-word" data-pos="verb" data-tr="yopilib qolgan">닫혔어요</span>. 밖에서는 안 열려요. <span class="cn-word" data-pos="adv" data-tr="bir oz">잠깐만</span> 기다려 주세요.</p>

<p>지영 씨가 안에서 문을 열었어요. 그때 <span class="cn-word" data-tr="chiroq">불</span>이 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> <span class="cn-word" data-pos="verb" data-tr="oʻchdi">꺼졌어요</span>.</p>

<p><strong>지영:</strong> 어? 불이 꺼졌어요.</p>

<p><strong>셰르벡:</strong> 괜찮아요. 창문이 크니까 교실이 <span class="cn-word" data-pos="adj" data-tr="yorugʻ">밝아요</span>.</p>

<p><span class="cn-word" data-tr="dars">수업</span>은 아홉 시에 <span class="cn-word" data-pos="verb" data-tr="boshlanadi">시작돼요</span>. 그런데 선생님이 아직 안 왔어요. 십 분 후에 선생님이 왔어요.</p>

<p><strong>선생님:</strong> 미안해요. <span class="cn-word" data-tr="yoʻl">길</span>이 많이 <span class="cn-word" data-pos="verb" data-tr="tiqilib qoldi">막혔어요</span>. 학교까지 한 시간이나 <span class="cn-word" data-pos="verb" data-tr="ketdi (vaqt)">걸렸어요</span>.</p>

<p>셰르벡 씨는 웃었어요. 오늘 아침에는 문도 안 열리고, 불도 꺼지고, 선생님도 늦었어요. 하지만 수업은 <span class="cn-word" data-pos="adj" data-tr="qiziqarli boʻladiganga oʻxshaydi">재미있을 것 같아요</span>.</p>''',
        "questions": [
            {
                "text": "Nega sinf eshigi ochilmadi?",
                "choices": [
                    "Sherbek kalitni yoʻqotgani uchun",
                    "Shamoldan yopilib qolgani uchun",
                    "Oʻqituvchi qulflab ketgani uchun",
                    "Chiroq oʻchgani uchun",
                ],
                "answer": 1,
                "explanation": "“<b>바람에</b> 문이 <b>닫혔어요</b>” — shamol "
                               "jonsiz bajaruvchi, shuning uchun 에게 emas, "
                               "<b>에</b> qoʻshimchasi.",
            },
            {
                "text": "Nega oʻqituvchi kechikdi?",
                "choices": [
                    "Chunki kasal edi",
                    "Chunki eshik ochilmadi",
                    "Chunki yoʻl tiqilib qolgan edi",
                    "Chunki avtobusni kutdi",
                ],
                "answer": 2,
                "explanation": "“길이 많이 <b>막혔어요</b>. 학교까지 한 "
                               "시간이나 <b>걸렸어요</b>” — 막히다 va 걸리다 "
                               "har kuni eshitiladigan majhul feʼllar.",
            },
            {
                "text": "“불이 꺼졌어요” nima degani?",
                "choices": [
                    "Chiroqni men oʻchirdim",
                    "Chiroq oʻzi oʻchdi",
                    "Chiroq yondi",
                    "Chiroq yoʻq edi",
                ],
                "answer": 1,
                "explanation": "끄다 (oʻchirmoq) → <b>꺼지다</b> "
                               "(아/어지다 yoʻli). Kim oʻchirgani aytilmaydi. "
                               "“Men oʻchirdim” boʻlsa 껐어요 boʻlardi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "동생을 깨우고 밥을 먹여요",
        "summary": (
            "PK-57 matni. Afsonaning har kungi ertalabi — singlisini uygʻotadi, "
            "kiyintiradi, ovqat yediradi. Orttirma nisbat matn ichida."
        ),
        "order":   57,
        "grammar": [
            {
                "pattern":  "동사 + 이/히/리/기/우/구/추 — orttirma nisbat",
                "meaning":  "Ishni boshqa odam qildiradi. Oʻzbekcha "
                            "“-tir-, -dir-, -t-” qoʻshimchasi bilan bir xil: "
                            "ye-dir-di · 먹-이-다, uygʻo-t-di · 깨-우-다.",
                "examples": ["언니가 동생을 깨워요.",
                             "옷을 입혀요.",
                             "밥을 먹여요.",
                             "어머니가 동생을 재워요."],
            },
            {
                "pattern":  "에게 va 을/를 tanlash",
                "meaning":  "Asl feʼlda toʻldiruvchi bor boʻlsa (밥을 먹다) "
                            "— odam 에게 oladi. Asl feʼlda toʻldiruvchi "
                            "yoʻq boʻlsa (자다, 앉다) — odam 을/를 oladi.",
                "examples": ["동생에게 밥을 먹여요.", "동생을 의자에 앉혀요."],
            },
            {
                "pattern":  "웃다 → 웃기다",
                "meaning":  "Kulmoq → kuldirmoq. Oʻzak ㅅ bilan tugagani "
                            "uchun 기 qoʻshimchasi.",
                "examples": ["아프소나 씨는 동생을 웃겨요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 <span class="cn-word" data-tr="opa">언니</span>예요. <span class="cn-word" data-tr="singil/uka">동생</span> 이름은 <span class="cn-word" data-tr="Dilnoza">딜노자</span>예요. 딜노자 씨는 아직 <span class="cn-word" data-tr="olti yosh">여섯 살</span>이에요.</p>

<p>아침 일곱 시에 아프소나 씨가 동생을 <span class="cn-word" data-pos="verb" data-tr="uygʻotadi">깨워요</span>. 딜노자 씨는 <span class="cn-word" data-tr="uyqusi koʻp">잠이 많아요</span>.</p>

<p><strong>아프소나:</strong> 딜노자, <span class="cn-word" data-pos="verb" data-tr="turing">일어나세요</span>! 학교에 가야 해요.</p>

<p><strong>딜노자:</strong> 오 분만 더요...</p>

<p>아프소나 씨가 동생을 <span class="cn-word" data-tr="stul">의자</span>에 <span class="cn-word" data-pos="verb" data-tr="oʻtqazadi">앉히고</span> <span class="cn-word" data-tr="kiyim">옷</span>을 <span class="cn-word" data-pos="verb" data-tr="kiydiradi">입혀요</span>. 그리고 밥을 <span class="cn-word" data-pos="verb" data-tr="yediradi">먹여요</span>.</p>

<p><strong>딜노자:</strong> 언니, 저 <span class="cn-word" data-pos="adv" data-tr="oʻzim">혼자</span> 먹을 수 있어요!</p>

<p><strong>아프소나:</strong> 그럼 혼자 먹어요. 하지만 <span class="cn-word" data-pos="adv" data-tr="tez">빨리</span> 먹어야 해요.</p>

<p>아프소나 씨는 매일 아침 동생을 <span class="cn-word" data-pos="verb" data-tr="kuldiradi">웃겨요</span>. 재미있는 <span class="cn-word" data-tr="hikoya">이야기</span>를 하면 딜노자 씨가 웃어요. 그러면 밥을 잘 먹어요.</p>

<p>저녁에는 <span class="cn-word" data-tr="ona">어머니</span>가 딜노자 씨를 <span class="cn-word" data-pos="verb" data-tr="uxlatadi">재워요</span>. 아프소나 씨는 동생에게 책을 <span class="cn-word" data-pos="verb" data-tr="oʻqib beradi">읽어 줘요</span>.</p>

<p><strong>어머니:</strong> 아프소나, <span class="cn-word" data-tr="rahmat">고마워요</span>. 동생을 잘 <span class="cn-word" data-pos="verb" data-tr="qaragani uchun">봐 줘서</span> 고마워요.</p>

<p><strong>아프소나:</strong> 괜찮아요. 저는 언니잖아요.</p>''',
        "questions": [
            {
                "text": "Ertalab Dilnozani kim uygʻotadi?",
                "choices": [
                    "Onasi",
                    "Opasi Afsona",
                    "Oʻzi uygʻonadi",
                    "Otasi",
                ],
                "answer": 1,
                "explanation": "“아침 일곱 시에 <b>아프소나 씨가</b> 동생을 "
                               "<b>깨워요</b>” — kechqurun esa onasi "
                               "uxlatadi (재워요).",
            },
            {
                "text": "“동생을 웃겨요” nima degani?",
                "choices": [
                    "Singlisi kuladi",
                    "Singlisini kuldiradi",
                    "Singlisiga kuladi",
                    "Singlisi bilan kuladi",
                ],
                "answer": 1,
                "explanation": "웃다 (kulmoq) → <b>웃기다</b> (kuldirmoq). "
                               "Belgisi — 동생<b>을</b>: orttirma feʼlning "
                               "toʻldiruvchisi bor.",
            },
            {
                "text": "Nega matnda 동생<b>에게</b> 밥을 먹여요 deyilgan, "
                        "동생<b>을</b> emas?",
                "choices": [
                    "Chunki 동생 jonli",
                    "Chunki 밥 allaqachon 을 olgan — bitta gapda ikkita "
                    "을/를 boʻlmaydi",
                    "Chunki bu majhul nisbat",
                    "Chunki feʼl oʻtgan zamonda",
                ],
                "answer": 1,
                "explanation": "Asl feʼlda toʻldiruvchi bor edi (밥<b>을</b> "
                               "먹다), shuning uchun orttirmada odam "
                               "<b>에게</b> oladi. 자다 kabi feʼllarda esa "
                               "동생<b>을</b> 재워요 boʻladi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "숙제를 다 해 버렸어요",
        "summary": (
            "PK-58 matni. Juma kechqurun kutubxonada — Jasur uy vazifasini "
            "qilib boʻlgan, Bekzod esa daftarini yoʻqotib qoʻygan."
        ),
        "order":   58,
        "grammar": [
            {
                "pattern":  "동사 + 아/어 버리다",
                "meaning":  "Ish butunlay tugadi + gapiruvchining tuygʻusi: "
                            "yengillik yoki afsus. Oʻzbekcha koʻmakchi "
                            "feʼllar bilan bir xil: qili-b boʻldim, "
                            "yoʻqoti-b qoʻydim.",
                "examples": ["숙제를 다 해 버렸어요.",
                             "카페가 닫혀 버렸어요."],
            },
            {
                "pattern":  "잃어버리다 · 잊어버리다",
                "meaning":  "Bu ikki feʼl 버리다 bilan qoʻshib yoziladi va "
                            "버리다siz deyarli ishlatilmaydi.",
                "examples": ["공책을 잃어버렸어요.",
                             "저는 왜 이렇게 잘 잊어버려요?"],
            },
            {
                "pattern":  "Majhul + 버리다 birga",
                "meaning":  "닫히다 (majhul, PK-56) ustiga 아/어 버리다 "
                            "qoʻshilsa: “yopilib qoldi” — va bu menga "
                            "yoqmadi degan tuygʻu chiqadi.",
                "examples": ["카페가 벌써 닫혀 버렸어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="juma">금요일</span> 저녁이에요. <span class="cn-word" data-tr="Bekzod">벡조드</span> 씨와 <span class="cn-word" data-tr="Jasur">자스루르</span> 씨가 <span class="cn-word" data-tr="kutubxona">도서관</span>에 있어요.</p>

<p><strong>벡조드:</strong> 자스루르 씨, <span class="cn-word" data-tr="uy vazifasi">숙제</span> 다 했어요?</p>

<p><strong>자스루르:</strong> 네, <span class="cn-word" data-pos="adv" data-tr="ozgina oldin">아까</span> 다 <span class="cn-word" data-pos="verb" data-tr="qilib boʻldim">해 버렸어요</span>. 이제 <span class="cn-word" data-tr="dam olish kuni">주말</span>에 놀 수 있어요!</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-pos="adv" data-tr="allaqachon">벌써</span>요? 저는 아직 시작도 안 했어요.</p>

<p><strong>자스루르:</strong> 어려운 숙제니까 빨리 하는 것이 좋아요.</p>

<p>벡조드 씨는 <span class="cn-word" data-tr="sumka">가방</span>을 열었어요. 그런데 <span class="cn-word" data-tr="daftar">공책</span>이 없었어요.</p>

<p><strong>벡조드:</strong> 어? 공책을 <span class="cn-word" data-pos="verb" data-tr="yoʻqotib qoʻydim">잃어버렸어요</span>!</p>

<p><strong>자스루르:</strong> 집에 있어요?</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-pos="verb" data-tr="bilmayman">모르겠어요</span>. 어제 <span class="cn-word" data-tr="kafe">카페</span>에서 공부했어요. 거기에 있을 것 같아요.</p>

<p>두 사람은 카페에 갔어요. 하지만 카페는 벌써 <span class="cn-word" data-pos="verb" data-tr="yopilib qolibdi">닫혀 버렸어요</span>.</p>

<p><strong>벡조드:</strong> 아... 오늘은 <span class="cn-word" data-pos="adj" data-tr="omadim yoʻq">운이 없어요</span>.</p>

<p><strong>자스루르:</strong> <span class="cn-word" data-pos="verb" data-tr="xavotirlanmang">걱정하지 마세요</span>. 내일 아침에 같이 가요. 오늘은 제 공책으로 공부해요.</p>

<p><strong>벡조드:</strong> 고마워요. 그런데 저는 왜 이렇게 잘 <span class="cn-word" data-pos="verb" data-tr="esdan chiqaraman">잊어버려요</span>?</p>

<p>자스루르 씨는 웃었어요. 그리고 두 사람은 같이 숙제를 <span class="cn-word" data-pos="verb" data-tr="qila boshladi">시작했어요</span>.</p>''',
        "questions": [
            {
                "text": "“숙제를 다 해 버렸어요” — Jasurda qaysi tuygʻu bor?",
                "choices": [
                    "Afsus — vazifani qilishni istamagan",
                    "Yengillik — ogʻir ish tugadi, endi dam olsa boʻladi",
                    "Qoʻrquv — vazifa notoʻgʻri boʻlishi mumkin",
                    "Hech qanday tuygʻu yoʻq",
                ],
                "answer": 1,
                "explanation": "Keyingi jumla buni tasdiqlaydi: “이제 "
                               "주말에 놀 수 있어요!” — bu 버리다 ning "
                               "<b>시원함</b> (yengillik) tomoni.",
            },
            {
                "text": "Bekzod nimani yoʻqotib qoʻydi?",
                "choices": [
                    "Sumkasini",
                    "Kalitini",
                    "Daftarini",
                    "Kitobini",
                ],
                "answer": 2,
                "explanation": "“<b>공책</b>을 잃어버렸어요!” — 잃어버리다 "
                               "bitta soʻz boʻlib qoʻshib yoziladi.",
            },
            {
                "text": "“카페가 닫혀 버렸어요” gapida nechta grammatika "
                        "qolipi bor?",
                "choices": [
                    "Faqat bitta — 아/어 버리다",
                    "Ikkita — majhul nisbat (닫히다) va 아/어 버리다",
                    "Ikkita — orttirma nisbat va 아/어 버리다",
                    "Uchta",
                ],
                "answer": 1,
                "explanation": "닫다 → <b>닫히다</b> (PK-56 majhul: kafe "
                               "oʻzi yopildi) ustiga <b>아/어 버리다</b> "
                               "qoʻshilgan — “yopilib qolibdi”, va Bekzod "
                               "bundan afsusda.",
            },
        ],
    },
]
