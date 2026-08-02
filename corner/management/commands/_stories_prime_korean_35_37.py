# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-35 … PK-37 (아/어서, (으)면, 보다/제일).

Kumulyativ qoida: PK-37 gacha oʻrganilgan hamma narsa ochiq.
Aniqlovchi shakllar (PK-43…45) va otlashtirish (PK-46) hali yoʻq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_35_37.py --author=prime
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
        "title":   "배가 아파서 학교에 못 갔어요",
        "summary": (
            "PK-35 matni. Afsona kasal boʻlib darsga kelmadi — butun suhbat "
            "아/어서 ustiga qurilgan: sabab ham, bogʻliq ketma-ketlik ham."
        ),
        "order":   35,
        "grammar": [
            {
                "pattern":  "동사/형용사 + 아/어서 (sabab)",
                "meaning":  "“…gani uchun”. 아/어요 shaklidan 요 ni olib 서 "
                            "qoʻyiladi. Undan OLDIN zamon qoʻyilmaydi — 아팠어서 "
                            "emas, 아파서.",
                "examples": ["배가 아파서 병원에 갔어요.",
                             "시간이 없어서 숙제를 못 했어요.",
                             "날씨가 더워서 창문을 열었어요."],
            },
            {
                "pattern":  "동사 + 아/어서 (bogʻliq ketma-ketlik)",
                "meaning":  "Birinchi qismdagi joy yoki narsa ikkinchi qismga "
                            "koʻchadi. 고 dan farqi shu: 고 — aloqasiz ishlar, "
                            "아/어서 — bogʻliq ishlar.",
                "examples": ["도서관에 가서 숙제를 했어요.", "약을 먹어서 괜찮아요."],
            },
            {
                "pattern":  "아/어서 va notoʻgʻri feʼllar",
                "meaning":  "아/어서 unli bilan boshlanadi, shuning uchun PK-32 "
                            "dagi oʻzgarishlar bu yerda ISHLAYDI: 덥다 → 더워서, "
                            "아프다 → 아파서, 고맙다 → 고마워요.",
                "examples": ["날씨가 더워서 힘들어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span> 씨는 <span class="cn-word" data-tr="kecha">어제</span> 학교에 <span class="cn-word" data-pos="verb" data-tr="kelmadi">안 왔어요</span>. 오늘 <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="soʻraydi">물어요</span>.</p>

<p><strong>셰르벡:</strong> 어제 <span class="cn-word" data-tr="nega">왜</span> 안 왔어요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="qornim">배</span>가 <span class="cn-word" data-pos="adj" data-tr="ogʻrigani uchun">아파서</span> <span class="cn-word" data-tr="shifoxonaga">병원에</span> <span class="cn-word" data-pos="verb" data-tr="bordim">갔어요</span>.</p>

<p><strong>셰르벡:</strong> 그래요? <span class="cn-word" data-tr="hozir">지금</span>은 <span class="cn-word" data-pos="adj" data-tr="yaxshimisiz">괜찮아요</span>?</p>

<p><strong>아프소나:</strong> 네. <span class="cn-word" data-tr="dori">약</span>을 <span class="cn-word" data-pos="verb" data-tr="ichganim uchun">먹어서</span> 지금은 괜찮아요. 하지만 <span class="cn-word" data-tr="uy vazifasi">숙제</span>를 <span class="cn-word" data-pos="verb" data-tr="qila olmadim">못 했어요</span>. <span class="cn-word" data-tr="vaqt">시간</span>이 <span class="cn-word" data-tr="boʻlmagani uchun">없어서</span> <span class="cn-word" data-pos="adv" data-tr="yolgʻiz">혼자</span> 못 했어요.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-tr="xavotir olmang">걱정하지 마세요</span>. 제가 <span class="cn-word" data-tr="yordam beraman">도와줄 거예요</span>. <span class="cn-word" data-tr="kutubxonaga">도서관에</span> <span class="cn-word" data-pos="verb" data-tr="borib">가서</span> <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 해요.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> <span class="cn-word" data-pos="adj" data-tr="rahmat">고마워요</span>.</p>

<p><span class="cn-word" data-tr="ikki kishi">두 사람</span>은 도서관에 가서 숙제를 <span class="cn-word" data-pos="verb" data-tr="qilishdi">했어요</span>. 날씨가 <span class="cn-word" data-pos="adj" data-tr="issiq boʻlgani uchun">더워서</span> <span class="cn-word" data-tr="deraza">창문</span>을 <span class="cn-word" data-pos="verb" data-tr="ochishdi">열었어요</span>.</p>''',
        "questions": [
            {
                "text": "Nega matnda “아파서” deyilgan, “아팠어서” emas?",
                "choices": [
                    "아/어서 dan oldin zamon qoʻyilmaydi",
                    "Chunki 아프다 sifat",
                    "Chunki gap hozirgi zamonda",
                    "Chunki oʻzakda 받침 yoʻq",
                ],
                "answer": 0,
                "explanation": "Bu 아/어서 ning birinchi qatʼiy taqigʻi. Zamon "
                               "faqat oxirgi feʼlda turadi (<b>갔어요</b>) va u "
                               "butun gapni oʻtmishga oladi. Solishtiring: "
                               "지만 da zamon oldin ham boʻlardi (갔<b>지만</b>).",
            },
            {
                "text": "“도서관에 가서 숙제를 했어요” — nega 가고 emas?",
                "choices": [
                    "Vazifa oʻsha kutubxonada qilingan — ikki ish bogʻlangan",
                    "가다 bilan 고 ishlatilmaydi",
                    "Chunki ikki ega har xil",
                    "Chunki gapda 같이 bor",
                ],
                "answer": 0,
                "explanation": "아/어서 da birinchi qismdagi <b>joy ikkinchi "
                               "qismga koʻchadi</b>. 가고 deyilsa, kutubxonaga "
                               "borish vazifa qilishga aloqasiz boʻlib qolardi — "
                               "shunchaki tartib.",
            },
            {
                "text": "Afsona nega uy vazifasini qila olmadi?",
                "choices": [
                    "Kasal boʻlib, vaqti boʻlmagani uchun",
                    "Kitobini yoʻqotgani uchun",
                    "Sherbek yordam bermagani uchun",
                    "Havo issiq boʻlgani uchun",
                ],
                "answer": 0,
                "explanation": "“배가 <b>아파서</b> 병원에 갔어요” va “시간이 "
                               "<b>없어서</b> 혼자 못 했어요” — matnda ikkita "
                               "sabab ketma-ket berilgan, ikkalasi ham 아/어서 "
                               "bilan.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "시간이 있으면 같이 가요",
        "summary": (
            "PK-36 matni. Afsona va Jiyong dam olish kunini rejalashtiradi — "
            "har bir reja bitta shartga bogʻlangan."
        ),
        "order":   36,
        "grammar": [
            {
                "pattern":  "동사/형용사 + (으)면",
                "meaning":  "“Agar …sa”. 받침 yoʻq → 면 (가면), 받침 bor → 으면 "
                            "(있으면). ㄹ oʻzak ㄹ ni tashlamaydi: 만들면.",
                "examples": ["날씨가 좋으면 공원에 갈 거예요.",
                             "비가 오면 집에 있을 거예요.",
                             "시간이 있으면 같이 가요."],
            },
            {
                "pattern":  "(으)면 + buyruq",
                "meaning":  "아/어서 dan farqli oʻlaroq, (으)면 dan keyin buyruq va "
                            "taklif BEMALOL keladi. Shuning uchun maslahat "
                            "berishda deyarli har doim (으)면 ishlatiladi.",
                "examples": ["모르면 저한테 전화하세요."],
            },
            {
                "pattern":  "만약 + (으)면",
                "meaning":  "만약 gap boshida turadi va shartni aniq belgilaydi, "
                            "lekin (으)면 ning oʻrnini bosmaydi — ikkalasi birga "
                            "ishlaydi.",
                "examples": ["만약 시간이 있으면 같이 가요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="dam olish kuni">주말</span>이 <span class="cn-word" data-pos="verb" data-tr="yaqinlashdi">가까워요</span>. <span class="cn-word" data-tr="Jiyong">지영</span> 씨가 아프소나 씨한테 <span class="cn-word" data-pos="verb" data-tr="soʻradi">물었어요</span>.</p>

<p><strong>지영:</strong> 아프소나 씨, 주말에 뭐 <span class="cn-word" data-tr="qilasiz">할 거예요</span>?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-pos="adv" data-tr="hali">아직</span> <span class="cn-word" data-pos="verb" data-tr="bilmayman">몰라요</span>. <span class="cn-word" data-tr="havo">날씨</span>가 <span class="cn-word" data-tr="yaxshi boʻlsa">좋으면</span> <span class="cn-word" data-tr="bogʻga">공원에</span> <span class="cn-word" data-tr="boraman">갈 거예요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="yomgʻir yogʻsa">비가 오면</span> <span class="cn-word" data-tr="qanday qilasiz">어떻게 해요</span>?</p>

<p><strong>아프소나:</strong> 비가 오면 <span class="cn-word" data-tr="uyda">집에서</span> 한국 <span class="cn-word" data-tr="serial">드라마</span>를 <span class="cn-word" data-tr="koʻraman">볼 거예요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="agar">만약</span> 시간이 <span class="cn-word" data-tr="boʻlsa">있으면</span> <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 가요. 저도 공원을 <span class="cn-word" data-pos="verb" data-tr="yoqtiraman">좋아해요</span>.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="yaxshi">좋아요</span>! <span class="cn-word" data-pos="adv" data-tr="lekin">그런데</span> 저는 <span class="cn-word" data-tr="yoʻlni">길을</span> 잘 몰라요.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="bilmasangiz">모르면</span> 저한테 <span class="cn-word" data-tr="qoʻngʻiroq qiling">전화하세요</span>. 제가 <span class="cn-word" data-tr="oʻrgataman">가르쳐 줄 거예요</span>.</p>

<p><strong>아프소나:</strong> 고마워요. 그럼 <span class="cn-word" data-tr="shanbada">토요일에</span> <span class="cn-word" data-tr="uchrashamiz">만나요</span>!</p>''',
        "questions": [
            {
                "text": "Nega matnda “있으면” deyilgan, “있면” emas?",
                "choices": [
                    "있 oʻzagida 받침 bor — shuning uchun 으면",
                    "Chunki bu buyruq",
                    "Chunki 있다 notoʻgʻri feʼl",
                    "Chunki gap oʻtgan zamonda",
                ],
                "answer": 0,
                "explanation": "받침 bor boʻlsa <b>으면</b> qoʻshiladi (있으면, "
                               "먹으면, 좋으면), 받침 yoʻq boʻlsa oddiy <b>면</b> "
                               "(가면, 오면).",
            },
            {
                "text": "“모르면 저한테 전화하세요” gapida diqqatga sazovor nima bor?",
                "choices": [
                    "(으)면 dan keyin buyruq turibdi — 아/어서 da bunday boʻlmaydi",
                    "Shart gap oxirida turibdi",
                    "Zamon (으)면 dan oldin qoʻyilgan",
                    "만약 tushirib qoldirilgan, shuning uchun xato",
                ],
                "answer": 0,
                "explanation": "Bu (으)면 ning 아/어서 dan eng muhim farqi. "
                               "<s>모라서 전화하세요</s> deb boʻlmasdi — 아/어서 "
                               "dan keyin buyruq kelmaydi. 만약 esa ixtiyoriy.",
            },
            {
                "text": "Yomgʻir yogʻsa Afsona nima qiladi?",
                "choices": [
                    "Uyda koreys seriali koʻradi",
                    "Baribir bogʻga boradi",
                    "Jiyongga qoʻngʻiroq qiladi",
                    "Kutubxonaga boradi",
                ],
                "answer": 0,
                "explanation": "“비가 오면 집에서 한국 드라마를 볼 거예요.” "
                               "Matndagi har bir reja bitta shartga bogʻlangan: "
                               "날씨가 좋으면 → 공원, 비가 오면 → 집.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "우리 반에서 누가 제일 커요?",
        "summary": (
            "PK-37 matni. Sinf haqidagi qisqa tasvir — boʻy, fan va til "
            "solishtiriladi, 보다 va 제일 yonma-yon ishlaydi."
        ),
        "order":   37,
        "grammar": [
            {
                "pattern":  "A는 B보다 (더/덜) 형용사",
                "meaning":  "Taqqoslash. 보다 otga toʻgʻridan-toʻgʻri yopishadi — "
                            "받침 ayrisi yoʻq, oldidan 을/를 olmaydi. 더 "
                            "ixtiyoriy, 덜 esa majburiy.",
                "examples": ["자수르 씨는 저보다 커요.",
                             "발음이 영어보다 어려워요.",
                             "문법은 영어보다 덜 어려워요."],
            },
            {
                "pattern":  "제일 / 가장",
                "meaning":  "“Eng”. Maʼnosi bir xil — 제일 ogʻzaki, 가장 yozma "
                            "nutqda koʻproq. Birga ishlatilmaydi.",
                "examples": ["셰르벡 씨가 제일 커요.", "딜노자 씨는 한국어를 제일 잘해요."],
            },
            {
                "pattern":  "중에서 / 에서 — doira",
                "meaning":  "Narsalar guruhi uchun 중에서, joy uchun 에서. "
                            "제일 bilan juft boʻlib yuradi.",
                "examples": ["우리 반에서 누가 제일 커요?",
                             "한국어하고 영어 중에서 뭐가 더 어려워요?"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="bizning sinf">우리 반</span>에는 <span class="cn-word" data-tr="oʻquvchi">학생</span>이 <span class="cn-word" data-tr="yigirma kishi">스무 명</span> 있어요. <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨가 <span class="cn-word" data-pos="adv" data-tr="eng">제일</span> <span class="cn-word" data-pos="adj" data-tr="baland boʻyli">커요</span>. <span class="cn-word" data-tr="Jasur">자수르</span> 씨는 셰르벡 씨<span class="cn-word" data-tr="dan">보다</span> <span class="cn-word" data-pos="adj" data-tr="past, lekin">작지만</span> 저보다 커요.</p>

<p><span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨는 한국어를 제일 <span class="cn-word" data-pos="verb" data-tr="yaxshi biladi">잘해요</span>. 딜노자 씨는 저보다 <span class="cn-word" data-pos="adv" data-tr="koʻproq">더</span> <span class="cn-word" data-pos="adv" data-tr="tirishib">열심히</span> <span class="cn-word" data-pos="verb" data-tr="oʻqiydi">공부해요</span>.</p>

<p><strong>아프소나:</strong> 딜노자 씨, 한국어<span class="cn-word" data-tr="bilan">하고</span> <span class="cn-word" data-tr="ingliz tili">영어</span> <span class="cn-word" data-tr="orasida">중에서</span> <span class="cn-word" data-tr="qaysi biri">뭐가</span> 더 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려워요</span>?</p>

<p><strong>딜노자:</strong> 저는 한국어가 더 어려워요. <span class="cn-word" data-tr="talaffuz">발음</span>이 영어보다 어려워요. 하지만 <span class="cn-word" data-tr="grammatika">문법</span>은 영어보다 <span class="cn-word" data-pos="adv" data-tr="kamroq">덜</span> 어려워요.</p>

<p><strong>아프소나:</strong> 저도 <span class="cn-word" data-tr="shundayman">그래요</span>. 한국어 발음이 <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> <span class="cn-word" data-pos="adj" data-tr="qiyin">힘들어요</span>. 하지만 저는 한국어를 제일 <span class="cn-word" data-pos="verb" data-tr="yoqtiraman">좋아해요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-tr="unda">그럼</span> 시간이 있으면 <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> <span class="cn-word" data-tr="mashq qilamiz">연습해요</span>. 매일 연습하면 <span class="cn-word" data-pos="adj" data-tr="osonlashadi">쉬워요</span>.</p>''',
        "questions": [
            {
                "text": "Sinfda kimning boʻyi eng baland?",
                "choices": [
                    "Sherbek",
                    "Jasur",
                    "Dilnoza",
                    "Afsona",
                ],
                "answer": 0,
                "explanation": "“셰르벡 씨가 <b>제일</b> 커요.” Jasur haqida esa "
                               "“셰르벡 씨<b>보다</b> 작지만 저보다 커요” deyilgan — "
                               "yaʼni u Sherbekdan past, lekin Afsonadan baland.",
            },
            {
                "text": "Nega matnda “동생을 보다” emas, “셰르벡 씨보다” deyilgan?",
                "choices": [
                    "보다 — qoʻshimcha, otga toʻgʻridan-toʻgʻri yopishadi",
                    "Chunki 씨 dan keyin 을/를 qoʻyilmaydi",
                    "Chunki gap taqqoslash emas",
                    "Chunki oʻzakda 받침 bor",
                ],
                "answer": 0,
                "explanation": "<b>보다</b> — mustaqil soʻz emas, balki "
                               "qoʻshimcha, shuning uchun oldidan 을/를 olmaydi. "
                               "(Alohida 보다 feʼli ham bor — u “koʻrmoq” degani, "
                               "butunlay boshqa soʻz.)",
            },
            {
                "text": "Dilnozaning fikricha, koreys tilining qaysi tomoni "
                        "ingliz tilinikidan oson?",
                "choices": [
                    "Grammatika",
                    "Talaffuz",
                    "Yozuv",
                    "Soʻzlar",
                ],
                "answer": 0,
                "explanation": "“문법은 영어보다 <b>덜</b> 어려워요” — grammatika "
                               "kamroq qiyin, yaʼni osonroq. Talaffuz haqida esa "
                               "teskarisi aytilgan: “발음이 영어보다 어려워요”.",
            },
        ],
    },
]
