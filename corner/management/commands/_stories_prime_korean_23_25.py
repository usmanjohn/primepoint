# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-23 … PK-25 (sonlar va vaqt).

Kumulyativ qoida: PK-25 gacha oʻrganilgan hamma narsa ochiq.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_23_25.py --author=prime
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
        "title":   "전화번호가 몇 번이에요?",
        "summary": (
            "PK-23 matni. Jasur va Jiyoung telefon raqami, narx va qavat haqida "
            "gaplashadi — hammasi 한자어 sonlar bilan."
        ),
        "order":   23,
        "grammar": [
            {
                "pattern":  "한자어 sonlar: 일, 이, 삼, 사, 오…",
                "meaning":  "Xitoy ildizli sonlar. Pul (원), daqiqa (분), sana "
                            "(년/월/일), qavat (층), telefon raqami va kurs uchun "
                            "ishlatiladi. Oʻndan yuqorisi qoʻshib yasaladi: 삼십칠.",
                "examples": ["오천 원", "삼 층", "이천이십육년"],
            },
            {
                "pattern":  "만 = 10 000",
                "meaning":  "Koreys tilida katta birlik ming emas, OʻN MING. Shuning "
                            "uchun raqamni oʻngdan toʻrttadan ajratish kerak: "
                            "100|0000 = 백만.",
                "examples": ["만 원", "십만", "백만"],
            },
            {
                "pattern":  "몇 + birlik",
                "meaning":  "“Nechta?” degan savol. Birlikdan OLDIN turadi: 몇 번, "
                            "몇 층, 몇 분. Telefon raqamida nol — 영 emas, 공.",
                "examples": ["몇 번이에요?", "몇 층에 있어요?"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Jasur">자수르</span> 씨와 <span class="cn-word" data-tr="Jiyoung">지영</span> 씨가 <span class="cn-word" data-tr="doʻkon">가게</span>에 있어요.</p>

<p><strong>지영:</strong> 자수르 씨, <span class="cn-word" data-tr="telefon raqami">전화번호</span>가 <span class="cn-word" data-tr="nechanchi">몇</span> <span class="cn-word" data-tr="raqam">번</span>이에요?</p>

<p><strong>자수르:</strong> 제 전화번호는 <span class="cn-word" data-tr="nol (telefonda)">공</span>일공 이삼사오 육칠팔구예요.</p>

<p><strong>지영:</strong> 이 <span class="cn-word" data-tr="kitob">책</span>은 <span class="cn-word" data-tr="qancha">얼마</span>예요?</p>

<p><strong>자수르:</strong> <span class="cn-word" data-tr="10 000">만</span> <span class="cn-word" data-tr="von (pul)">원</span>이에요. 저 <span class="cn-word" data-tr="sumka">가방</span>은 <span class="cn-word" data-tr="50 000">오만</span> 원이에요.</p>

<p><strong>지영:</strong> 가방이 <span class="cn-word" data-pos="adj" data-tr="qimmat">비싸요</span>. 저는 <span class="cn-word" data-tr="pul">돈</span>이 없어요.</p>

<p><strong>자수르:</strong> 가게가 <span class="cn-word" data-tr="nechanchi qavat">몇 층</span>에 있어요?</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="uchinchi qavat">삼 층</span>에 있어요.</p>

<p>이 가게는 삼 층에 있어요. 책은 만 원이에요. 가방은 오만 원이에요. 자수르 씨는 책을 좋아해요. 하지만 가방은 <span class="cn-word" data-tr="sotib olmaydi">안 사요</span>. 돈이 <span class="cn-word" data-pos="adj" data-tr="koʻp emas">많지 않아요</span>.</p>''',
        "questions": [
            {
                "text": "Sumka qancha turadi?",
                "choices": [
                    "50 000 von",
                    "10 000 von",
                    "5 000 von",
                    "100 000 von",
                ],
                "answer": 0,
                "explanation": "“오만 원” — 오 (5) × 만 (10 000) = 50 000. Koreys tilida "
                               "katta birlik 만, shuning uchun 오만 “ellik ming” degani, "
                               "“besh ming” emas.",
            },
            {
                "text": "Nega Jasur telefon raqamida “공” dedi, “영” emas?",
                "choices": [
                    "Telefon raqamlarida nol har doim 공 deb aytiladi",
                    "Chunki 공 qisqaroq",
                    "Chunki bu savol gapi",
                    "Chunki raqam uch xonali",
                ],
                "answer": 0,
                "explanation": "Koreys tilida nol uchun ikkita soʻz bor: 영 — "
                               "matematikada, 공 — telefon raqamlarida. Va telefon "
                               "raqamida har bir raqam alohida oʻqiladi.",
            },
            {
                "text": "Doʻkon qayerda joylashgan?",
                "choices": [
                    "Uchinchi qavatda",
                    "Birinchi qavatda",
                    "Oʻninchi qavatda",
                    "Matnda aytilmagan",
                ],
                "answer": 0,
                "explanation": "“삼 층에 있어요” — 삼 (3) + 층 (qavat). Qavat 한자어 sonlar "
                               "bilan sanaladi, va joy 있다 bilan har doim 에 oladi "
                               "(PK-14).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "학생이 몇 명 있어요?",
        "summary": (
            "PK-24 matni. Sinfxonada nima nechta bor — 개, 명, 마리, 권 sanoq "
            "soʻzlari va qisqargan sonlar amalda."
        ),
        "order":   24,
        "grammar": [
            {
                "pattern":  "고유어 sonlar: 하나, 둘, 셋, 넷…",
                "meaning":  "Asl koreys sonlari. Narsalar, odamlar, hayvonlar, yosh va "
                            "soat uchun. Faqat 99 gacha — 100 dan boshlab 한자어.",
                "examples": ["하나, 둘, 셋", "스물", "열다섯"],
            },
            {
                "pattern":  "명사 + 숫자 + 단위명사",
                "meaning":  "Sanash tartibi: OT birinchi, keyin son, keyin sanoq soʻzi. "
                            "Oʻzbekchada teskari (“besh dona olma”), koreyschada "
                            "“사과 다섯 개”.",
                "examples": ["사과 세 개", "학생 두 명", "고양이 네 마리"],
            },
            {
                "pattern":  "한, 두, 세, 네, 스무",
                "meaning":  "Sanoq soʻzi oldida toʻrtta son qisqaradi: 하나→한, 둘→두, "
                            "셋→세, 넷→네, va 스물→스무. Qoida 11–14 ga ham tegishli.",
                "examples": ["한 개", "두 명", "세 마리", "스무 살"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="sinfxona">교실</span>에 <span class="cn-word" data-tr="oʻquvchi">학생</span>이 있어요.</p>

<p><strong>선생님:</strong> 교실에 학생이 <span class="cn-word" data-tr="nechta">몇</span> <span class="cn-word" data-tr="nafar">명</span> 있어요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="oʻn nafar">열 명</span> 있어요. <span class="cn-word" data-tr="oʻqituvchi">선생님</span>은 <span class="cn-word" data-tr="bir kishi (hurmatli)">한 분</span> <span class="cn-word" data-tr="bor (hurmatli)">계세요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="stol">책상</span> 위에 <span class="cn-word" data-tr="kitob">책</span>이 <span class="cn-word" data-tr="nechta">몇</span> <span class="cn-word" data-tr="ta (kitob)">권</span> 있어요?</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="beshta">다섯 권</span> 있어요. <span class="cn-word" data-tr="sumka">가방</span>은 <span class="cn-word" data-tr="uchta">세 개</span> 있어요.</p>

<p><strong>선생님:</strong> 아프소나 씨는 <span class="cn-word" data-tr="necha yosh">몇 살</span>이에요?</p>

<p><strong>아프소나:</strong> 저는 <span class="cn-word" data-tr="oʻn olti yosh">열여섯 살</span>이에요. <span class="cn-word" data-tr="Jasur">자수르</span> 씨는 <span class="cn-word" data-tr="yigirma yosh">스무 살</span>이에요.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="uy">집</span>에 <span class="cn-word" data-tr="mushuk">고양이</span>가 있어요?</p>

<p><strong>아프소나:</strong> 네, <span class="cn-word" data-tr="ikki bosh">두 마리</span> 있어요. <span class="cn-word" data-tr="it">개</span>는 <span class="cn-word" data-tr="bir bosh">한 마리</span> 있어요.</p>

<p>교실에 학생이 열 명 있어요. 선생님은 한 분 계세요. 책상 위에 책이 다섯 권 있어요. 아프소나 씨 집에 고양이가 두 마리, <span class="cn-word" data-tr="it">개</span>가 한 마리 있어요.</p>''',
        "questions": [
            {
                "text": "Nega matnda “두 마리” deyilgan, “둘 마리” emas?",
                "choices": [
                    "Sanoq soʻzi oldida 둘 → 두 boʻlib qisqaradi",
                    "Chunki mushuk hayvon",
                    "Chunki 마리 받침 bilan boshlanadi",
                    "Chunki bu savol gapi",
                ],
                "answer": 0,
                "explanation": "Toʻrtta son sanoq soʻzi oldida qisqaradi: 하나→한, 둘→두, "
                               "셋→세, 넷→네 (va 스물→스무). Shuning uchun 두 마리, "
                               "세 개, 네 권.",
            },
            {
                "text": "Nega oʻqituvchi uchun “명” emas, “분” ishlatilgan?",
                "choices": [
                    "분 — odamlarning hurmatli sanoq soʻzi",
                    "Chunki oʻqituvchi bitta",
                    "Chunki 분 daqiqani bildiradi",
                    "Chunki oʻqituvchi sinfda yoʻq",
                ],
                "answer": 0,
                "explanation": "명 — oddiy, 분 — hurmatli sanoq soʻzi. Shuning uchun matnda "
                               "학생 열 명, lekin 선생님 한 분 va 계세요 (있다 ning hurmatli "
                               "shakli).",
            },
            {
                "text": "Koreys va oʻzbek sanash tartibi qanday farq qiladi?",
                "choices": [
                    "Koreyschada ot birinchi, oʻzbekchada son birinchi",
                    "Koreyschada son birinchi, oʻzbekchada ot birinchi",
                    "Ikkalasi ham bir xil",
                    "Oʻzbekchada sanoq soʻzi yoʻq",
                ],
                "answer": 0,
                "explanation": "Oʻzbekcha “besh dona olma” — son → sanoq → ot. Koreyscha "
                               "“사과 다섯 개” — ot → son → sanoq. Sanoq soʻzi tushunchasi "
                               "esa ikkala tilda ham bor (dona, nafar, bosh).",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "몇 시에 학교에 가요?",
        "summary": (
            "PK-25 matni. Bekzodning kun tartibi — soat 고유어 bilan, daqiqa 한자어 "
            "bilan, hafta kunlari va sana bir matnda."
        ),
        "order":   25,
        "grammar": [
            {
                "pattern":  "고유어 + 시 · 한자어 + 분",
                "meaning":  "Soat asl koreys sonlari bilan, daqiqa esa xitoy ildizli "
                            "sonlar bilan aytiladi. Eslash: soat SANALADI, daqiqa "
                            "OʻLCHANADI. 반 = yarim.",
                "examples": ["세 시 삼십 분", "여덟 시", "두 시 반"],
            },
            {
                "pattern":  "년 / 월 / 일 · 요일",
                "meaning":  "Sana hammasi 한자어 va tartib oʻzbekchadagidek: yil → oy → "
                            "kun. Hafta kunlari beshta unsurdan: 월·화·수·목·금·토·일.",
                "examples": ["팔월 이일", "월요일", "금요일"],
            },
            {
                "pattern":  "시간 + 에",
                "meaning":  "Vaqt 에 qoʻshimchasini oladi (여덟 시에). Lekin 오늘, 어제, "
                            "내일 hech qachon 에 olmaydi (PK-14).",
                "examples": ["여덟 시에 가요.", "월요일에 학교에 가요.", "오늘 시간이 없어요."],
            },
        ],
        "body": '''<p>저는 <span class="cn-word" data-tr="Bekzod">벡조드</span>예요. <span class="cn-word" data-tr="mana">이것</span>이 <span class="cn-word" data-tr="mening">제</span> <span class="cn-word" data-tr="kun">하루</span>예요.</p>

<p><span class="cn-word" data-tr="ertalab">아침</span> <span class="cn-word" data-tr="soat yettida">일곱 시</span>에 <span class="cn-word" data-pos="verb" data-tr="ovqatlanaman">밥을 먹어요</span>. <span class="cn-word" data-tr="soat sakkiz yarimda">여덟 시 반</span>에 <span class="cn-word" data-tr="maktab">학교</span>에 가요.</p>

<p><span class="cn-word" data-tr="tushdan keyin">오후</span> <span class="cn-word" data-tr="soat uch oʻttizda">세 시 삼십 분</span>에 <span class="cn-word" data-tr="uy">집</span>에 <span class="cn-word" data-pos="verb" data-tr="kelaman">와요</span>. <span class="cn-word" data-tr="kechqurun">저녁</span> <span class="cn-word" data-tr="soat yettida">일곱 시</span>에 <span class="cn-word" data-tr="koreys tili">한국어</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrganaman">공부해요</span>.</p>

<p><strong>지영:</strong> 벡조드 씨, <span class="cn-word" data-tr="soat necha">몇 시</span>에 학교에 가요?</p>

<p><strong>벡조드:</strong> 여덟 시 반에 가요. <span class="cn-word" data-tr="dushanba">월요일</span>부터 <span class="cn-word" data-tr="juma">금요일</span>까지 학교에 가요.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="dam olish kuni">주말</span>에도 <span class="cn-word" data-pos="verb" data-tr="oʻqiysizmi">공부해요</span>?</p>

<p><strong>벡조드:</strong> 주말에는 공부 안 해요. <span class="cn-word" data-tr="dam olaman">쉬어요</span>.</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="bugun">오늘</span>은 <span class="cn-word" data-tr="nechanchi sana">며칠</span>이에요?</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="avgust">팔월</span> <span class="cn-word" data-tr="ikkinchi kun">이일</span>이에요. <span class="cn-word" data-tr="yakshanba">일요일</span>이에요.</p>

<p>벡조드 씨는 월요일부터 금요일까지 학교에 가요. 주말에는 <span class="cn-word" data-pos="verb" data-tr="dam oladi">쉬어요</span>. <span class="cn-word" data-tr="bugun">오늘</span>은 팔월 이일, 일요일이에요.</p>''',
        "questions": [
            {
                "text": "Nega “세 시 삼십 분” da ikki xil son tizimi ishlatilgan?",
                "choices": [
                    "Soat 고유어, daqiqa esa 한자어 bilan aytiladi",
                    "Chunki 세 va 삼십 bir xil son",
                    "Chunki bu oʻtgan zamon",
                    "Bu xato — bitta tizim boʻlishi kerak",
                ],
                "answer": 0,
                "explanation": "세 — 고유어 (셋 ning qisqargani, soat uchun), 삼십 — 한자어 "
                               "(daqiqa uchun). Eslash: soat SANALADI (고유어), daqiqa "
                               "OʻLCHANADI (한자어).",
            },
            {
                "text": "Bekzod qaysi kunlari maktabga boradi?",
                "choices": [
                    "Dushanbadan jumagacha",
                    "Har kuni",
                    "Faqat dam olish kunlari",
                    "Shanba va yakshanba",
                ],
                "answer": 0,
                "explanation": "“월요일부터 금요일까지” — 부터…까지 oraliqni koʻrsatadi "
                               "(PK-16). 주말에는 (dam olish kunlari) esa "
                               "“공부 안 해요” — oʻqimaydi.",
            },
            {
                "text": "Matnda “오늘은 며칠이에요?” deyilgan, “오늘에는” emas. Nega?",
                "choices": [
                    "오늘, 어제, 내일 hech qachon 에 olmaydi",
                    "Chunki 오늘 받침 bilan tugaydi",
                    "Chunki bu savol gapi",
                    "Chunki 며칠 sonni bildiradi",
                ],
                "answer": 0,
                "explanation": "PK-14 qoidasi: 오늘, 어제, 내일 vaqt qoʻshimchasini olmaydi. "
                               "Boshqa vaqt soʻzlari esa oladi — matnda 여덟 시에, "
                               "주말에 ni koʻrasiz.",
            },
        ],
    },
]
