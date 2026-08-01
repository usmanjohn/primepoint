# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-9 … PK-11.

Har bir matn oʻz darsining grammatikasini kamida ikki marta koʻrsatadi va faqat
oʻsha darsgacha oʻrganilgan qoliplardan foydalanadi (kumulyativ qoida).
Toc: corner/management/commands/toc_prime_korean_readings.txt

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_09_11.py --author=prime
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
        "title":   "안녕하세요",
        "summary": (
            "PK-9 matni. Afsona koreys qoʻshnisi bilan birinchi marta salomlashadi — "
            "va xayrlashishda 계세요 bilan 가세요 farqini amalda koʻrasiz."
        ),
        "order":   9,
        "grammar": [
            {
                "pattern":  "안녕하세요",
                "meaning":  "Salom. Vaqtga bogʻliq emas — ertalab ham, kechqurun ham "
                            "bir xil ishlatiladi. Yaqin doʻstga qisqasi: 안녕.",
                "examples": ["안녕하세요?", "안녕! 지영아."],
            },
            {
                "pattern":  "안녕히 계세요 / 안녕히 가세요",
                "meaning":  "Xayrlashishning ikki shakli. QOLAYOTGAN odamga 계세요 "
                            "(“qoling”), KETAYOTGAN odamga 가세요 (“boring”) deyiladi.",
                "examples": ["안녕히 계세요. (men ketyapman)",
                             "안녕히 가세요. (siz ketyapsiz)"],
            },
            {
                "pattern":  "감사합니다 → [감사함니다]",
                "meaning":  "Rahmat. 합니다 bilan tugagan hamma shakl 비음화 tufayli "
                            "[함니다] deb oʻqiladi: ㅂ dan keyin ㄴ kelsa, ㅂ → ㅁ.",
                "examples": ["감사합니다.", "죄송합니다.", "만나서 반갑습니다."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Afsona">아프소나</span>는 오늘 새 집에 왔습니다. <span class="cn-word" data-tr="qoʻshni">이웃</span> 아주머니가 문 앞에 있습니다.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="salom">안녕하세요</span>?</p>

<p><strong>아주머니:</strong> 안녕하세요? <span class="cn-word" data-tr="xush kelibsiz">어서 오세요</span>.</p>

<p><strong>아프소나:</strong> 저는 아프소나입니다. <span class="cn-word" data-tr="tanishganimdan xursandman">만나서 반갑습니다</span>.</p>

<p><strong>아주머니:</strong> 네, 반갑습니다. 저는 <span class="cn-word" data-tr="Jiyoung">지영</span>입니다.</p>

<p>아주머니가 아프소나에게 <span class="cn-word" data-tr="non">빵</span>을 주었습니다.</p>

<p><strong>아프소나:</strong> <span class="cn-word" data-tr="rahmat">감사합니다</span>!</p>

<p><strong>아주머니:</strong> 네. 그럼, 안녕히 <span class="cn-word" data-tr="qoling">계세요</span>.</p>

<p>아주머니가 <span class="cn-word" data-pos="verb" data-tr="ketadi">갑니다</span>. 아프소나는 집에 <span class="cn-word" data-pos="verb" data-tr="qoladi">있습니다</span>. 그래서 아프소나는 이렇게 말했습니다.</p>

<p><strong>아프소나:</strong> 네, 안녕히 <span class="cn-word" data-tr="boring">가세요</span>!</p>''',
        "questions": [
            {
                "text": "Afsona nega oxirida “안녕히 가세요” dedi?",
                "choices": [
                    "Chunki qoʻshni ketyapti, Afsona esa uyda qoladi",
                    "Chunki Afsona ketyapti",
                    "Chunki ikkalasi ham ketyapti",
                    "Chunki bu ertalabki salom",
                ],
                "answer": 0,
                "explanation": "가세요 = “boring” — KETAYOTGAN odamga aytiladi. Qoʻshni "
                               "ketdi, Afsona uyda qoldi. Shuning uchun qoʻshni Afsonaga "
                               "계세요 (“qoling”), Afsona esa qoʻshniga 가세요 dedi.",
            },
            {
                "text": "Qoʻshni ayol Afsonaga birinchi boʻlib nima dedi?",
                "choices": [
                    "안녕하세요 va 어서 오세요",
                    "감사합니다",
                    "안녕히 가세요",
                    "만나서 반갑습니다",
                ],
                "answer": 0,
                "explanation": "Qoʻshni avval 안녕하세요 deb salomlashdi, keyin "
                               "어서 오세요 (“xush kelibsiz”) dedi — bu yangi kelgan "
                               "odamga aytiladigan ibora.",
            },
            {
                "text": "“감사합니다” qanday oʻqiladi?",
                "choices": [
                    "[감사함니다]",
                    "[감사합니다]",
                    "[감사한니다]",
                    "[감사압니다]",
                ],
                "answer": 0,
                "explanation": "비음화 qoidasi: 받침 ㅂ dan keyin ㄴ kelgani uchun ㅂ burun "
                               "tovushi ㅁ ga aylanadi. Shuning uchun [감사함니다]. Bu qoida "
                               "합니다 bilan tugagan barcha shakllarga tegishli.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "저는 학생입니다",
        "summary": (
            "PK-10 matni. Uch kishi oʻzini tanishtiradi — 입니다, 입니까? va "
            "이/가 아닙니다 qoliplari matn ichida takrorlanadi."
        ),
        "order":   10,
        "grammar": [
            {
                "pattern":  "명사 + 입니다",
                "meaning":  "“…dir”. Otga boʻshliqsiz yopishadi va 받침 bor-yoʻqligiga "
                            "qaramaydi. Kesim har doim gap oxirida turadi. [임니다].",
                "examples": ["저는 학생입니다.", "지영 씨는 선생님입니다.",
                             "이것은 책입니다."],
            },
            {
                "pattern":  "명사 + 입니까?",
                "meaning":  "Savol shakli: 다 oʻrniga 까 qoʻyiladi. Soʻz tartibi "
                            "oʻzgarmaydi — xuddi oʻzbekchadagi “-mi” qoʻshimchasi kabi.",
                "examples": ["학생입니까?", "한국 사람입니까?"],
            },
            {
                "pattern":  "명사 + 이/가 아닙니다",
                "meaning":  "“…emas”. 받침 bor boʻlsa 이, yoʻq boʻlsa 가. Bu koreys "
                            "grammatikasidagi eng koʻp takrorlanadigan ayri.",
                "examples": ["저는 의사가 아닙니다.", "학생이 아닙니다."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="sinf, dars xonasi">교실</span>에 세 사람이 있습니다.</p>

<p><strong>자수르:</strong> 안녕하세요? 저는 <span class="cn-word" data-tr="Jasur">자수르</span>입니다. 저는 <span class="cn-word" data-tr="talaba, oʻquvchi">학생</span>입니다.</p>

<p><strong>지영:</strong> 안녕하세요? 저는 지영입니다. 저는 학생이 <span class="cn-word" data-tr="emas">아닙니다</span>. 저는 <span class="cn-word" data-tr="oʻqituvchi">선생님</span>입니다.</p>

<p><strong>자수르:</strong> 아, 선생님이십니까? <span class="cn-word" data-tr="kechirasiz">죄송합니다</span>!</p>

<p><strong>지영:</strong> <span class="cn-word" data-tr="hech qisi yoʻq">괜찮습니다</span>.</p>

<p>그리고 <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨가 왔습니다.</p>

<p><strong>자수르:</strong> 딜노자 씨는 <span class="cn-word" data-tr="shifokor">의사</span>입니까?</p>

<p><strong>딜노자:</strong> 아니요, 저는 의사가 아닙니다. 저는 학생입니다.</p>

<p><strong>자수르:</strong> 딜노자 씨는 <span class="cn-word" data-tr="koreys">한국 사람</span>입니까?</p>

<p><strong>딜노자:</strong> 아니요. 저는 <span class="cn-word" data-tr="oʻzbek">우즈베키스탄 사람</span>입니다. 자수르 씨도 우즈베키스탄 사람입니까?</p>

<p><strong>자수르:</strong> 네, <span class="cn-word" data-tr="toʻgʻri">맞습니다</span>. 우리는 <span class="cn-word" data-tr="doʻst">친구</span>입니다.</p>''',
        "questions": [
            {
                "text": "Jiyoung kim?",
                "choices": [
                    "Oʻqituvchi",
                    "Talaba",
                    "Shifokor",
                    "Oʻzbekistonlik talaba",
                ],
                "answer": 0,
                "explanation": "U “저는 학생이 아닙니다. 저는 선생님입니다” dedi — ya'ni "
                               "“talaba emasman, oʻqituvchiman”. 학생 받침 bilan tugagani "
                               "uchun 이 아닙니다 shakli ishlatilgan.",
            },
            {
                "text": "Nega Dilnoza “의사가 아닙니다” dedi, “의사이 아닙니다” emas?",
                "choices": [
                    "Chunki 의사 unli bilan tugaydi — 받침 yoʻq",
                    "Chunki 의사 받침 bilan tugaydi",
                    "Chunki bu savol gapi",
                    "Chunki 의사 chet soʻz",
                ],
                "answer": 0,
                "explanation": "받침 ayrisi: soʻz undosh bilan tugasa 이, unli bilan "
                               "tugasa 가. 의사 ning oxirgi boʻgʻini 사 — unli (ㅏ) bilan "
                               "tugaydi, 받침 yoʻq. Shuning uchun 가.",
            },
            {
                "text": "Matnda “입니까?” shakli nima uchun ishlatilgan?",
                "choices": [
                    "Savol berish uchun",
                    "Inkor qilish uchun",
                    "Hurmat bildirish uchun",
                    "Oʻtgan zamonni koʻrsatish uchun",
                ],
                "answer": 0,
                "explanation": "입니다 ning oxiridagi 다 ni 까 ga almashtirsak, savol "
                               "hosil boʻladi. Jasur shu bilan soʻradi: “딜노자 씨는 "
                               "의사입니까?” — “Dilnoza shifokormi?”",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "누구한테 어떻게 말해요?",
        "summary": (
            "PK-11 matni. Bekzod bir kunda uch xil odam bilan uchrashadi va har "
            "biriga boshqacha darajada gapiradi — 존댓말 va 반말 amalda."
        ),
        "order":   11,
        "grammar": [
            {
                "pattern":  "존댓말 / 반말",
                "meaning":  "Hurmat nutqi va yaqin nutq. Munosabat feʼlning oxirida "
                            "koʻrsatiladi. Notanish, kattaroq yoki maqomi yuqori odamga "
                            "존댓말; yaqin tengdosh yoki kichikka 반말.",
                "examples": ["안녕하세요? (존댓말)", "안녕! (반말)"],
            },
            {
                "pattern":  "저 / 나 · 제 / 내",
                "meaning":  "Olmosh ham darajaga qarab oʻzgaradi: 존댓말da 저 va 제, "
                            "반말da 나 va 내. Olmosh bilan gap oxiri mos kelishi SHART.",
                "examples": ["저는 학생입니다.", "나는 학생이야.", "제 이름은 벡조드입니다."],
            },
            {
                "pattern":  "이름 + 씨 / 선생님",
                "meaning":  "Koreyada suhbatdoshga 당신 (“siz”) deyilmaydi — ism + 씨 "
                            "yoki lavozim ishlatiladi. 씨 ni oʻzingizga qoʻllamang.",
                "examples": ["지영 씨는 학생입니까?", "선생님, 안녕하세요?"],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">벡조드</span>는 오늘 세 사람을 <span class="cn-word" data-pos="verb" data-tr="uchratdi">만났습니다</span>.</p>

<p><span class="cn-word" data-tr="ertalab">아침</span>에 학교에서 <span class="cn-word" data-tr="oʻqituvchi">선생님</span>을 만났습니다.</p>

<p><strong>벡조드:</strong> 선생님, <span class="cn-word" data-tr="salom (hurmat)">안녕하세요</span>? <span class="cn-word" data-tr="mening (hurmat)">제</span> <span class="cn-word" data-tr="ism">이름</span>은 벡조드입니다.</p>

<p><strong>선생님:</strong> 네, 반갑습니다. 벡조드 <span class="cn-word" data-tr="janob/xonim">씨</span>는 학생입니까?</p>

<p><strong>벡조드:</strong> 네, <span class="cn-word" data-tr="men (hurmat)">저</span>는 학생입니다.</p>

<p><span class="cn-word" data-tr="tushlik payti">점심</span>에 <span class="cn-word" data-tr="yaqin doʻst">친한 친구</span> 자수르를 만났습니다. 자수르는 벡조드와 <span class="cn-word" data-tr="tengdosh">동갑</span>입니다.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="salom (yaqin)">안녕</span>! <span class="cn-word" data-tr="men (oddiy)">나</span>는 오늘 <span class="cn-word" data-pos="adj" data-tr="band">바빠</span>.</p>

<p><strong>자수르:</strong> 그래? <span class="cn-word" data-tr="mening (oddiy)">내</span> 책은 <span class="cn-word" data-tr="qayerda">어디</span>에 있어?</p>

<p><span class="cn-word" data-tr="kechqurun">저녁</span>에 <span class="cn-word" data-tr="notanish odam">모르는 사람</span>을 만났습니다. 그 사람은 벡조드보다 <span class="cn-word" data-pos="adj" data-tr="katta">나이가 많습니다</span>.</p>

<p><strong>벡조드:</strong> 안녕하세요? <span class="cn-word" data-tr="uzr, ijozat">실례합니다</span>. 여기가 <span class="cn-word" data-tr="bekat">역</span>입니까?</p>

<p><strong>그 사람:</strong> 네, <span class="cn-word" data-tr="toʻgʻri">맞습니다</span>.</p>

<p><strong>벡조드:</strong> <span class="cn-word" data-tr="rahmat">감사합니다</span>. 안녕히 계세요.</p>

<p>벡조드는 세 사람에게 세 가지 <span class="cn-word" data-tr="usul, tarz">방법</span>으로 말했습니다. 한국어에서는 <span class="cn-word" data-tr="munosabat">관계</span>가 <span class="cn-word" data-tr="gap oxiri">문장 끝</span>에 있습니다.</p>''',
        "questions": [
            {
                "text": "Bekzod nega Jasur bilan “나” va “내” ishlatdi, lekin oʻqituvchi bilan “저” va “제” ishlatdi?",
                "choices": [
                    "Jasur tengdosh yaqin doʻsti, oʻqituvchi esa maqomi yuqori",
                    "Chunki Jasur uzoqroqda turgan edi",
                    "Chunki oʻqituvchi ayol edi",
                    "Chunki ertalab boshqacha, kechqurun boshqacha gapiriladi",
                ],
                "answer": 0,
                "explanation": "저/제 — 존댓말 olmoshlari, 나/내 — 반말 olmoshlari. Jasur "
                               "동갑 (tengdosh) va yaqin doʻst, shuning uchun 반말; "
                               "oʻqituvchi bilan esa har doim 존댓말.",
            },
            {
                "text": "Bekzod notanish odamga qaysi darajada gapirdi?",
                "choices": [
                    "존댓말 — chunki odam notanish va undan katta",
                    "반말 — chunki koʻchada erkin gapiriladi",
                    "반말 — chunki savol berdi",
                    "존댓말 emas, chunki bu qisqa suhbat edi",
                ],
                "answer": 0,
                "explanation": "Notanish odamga har doim 존댓말 ishlatiladi — munosabat "
                               "hali aniqlanmagan. Ustiga-ustak u Bekzoddan katta "
                               "(나이가 많습니다), ya'ni 반말 mutlaqo mumkin emas.",
            },
            {
                "text": "Matnning oxirgi jumlasi qanday xulosa qiladi?",
                "choices": [
                    "Koreys tilida munosabat gapning oxirida koʻrsatiladi",
                    "Koreys tilida uchta olmosh bor",
                    "Koreyada kunning har payti uchun alohida salom bor",
                    "Notanish odam bilan gaplashmaslik kerak",
                ],
                "answer": 0,
                "explanation": "“한국어에서는 관계가 문장 끝에 있습니다” — “koreys tilida "
                               "munosabat gap oxirida”. Bekzod bir xil narsani aytdi, "
                               "lekin uch xil shaklda, chunki suhbatdoshlari har xil edi.",
            },
        ],
    },
]
