# -*- coding: utf-8 -*-
"""Vocab bank — mavzuli lug'at 2: ish, iqtisod va jamiyat.

Order decade 600-699; new roots 400-449. The 쓰기 53/54 core vocabulary.
See STYLE_GUIDE_VOCAB.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

ROOTS = [
    {
        "syllable": "업", "hanja": "業", "order": 400,
        "meaning": "kasb, ish — sanoat, tadbirkorlik",
        "note": "<p>취업, 직업, 사업, 기업, 산업, 졸업. So‘z oxirida «soha/faoliyat» ma’nosi.</p>",
    },
    {
        "syllable": "직", "hanja": "職", "order": 405,
        "meaning": "lavozim — vazifa, ish o‘rni",
        "note": "<p>직업, 직장, 직원, 이직. ⚠️ <b>직(直)</b> = to‘g‘ri (정직, 직접) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "소", "hanja": "消", "order": 410,
        "meaning": "yo‘qolmoq, sarflamoq",
        "note": "<p>소비 (iste’mol), 소모, 소화 (hazm). "
                "⚠️ Bankda uchta <b>소</b> bor: 所 (joy), 消 (sarflash), 小 (kichik) — "
                "shuning uchun data faylda <code>소(消)</code> deb aniq yozing.</p>",
    },
    {
        "syllable": "비", "hanja": "費", "order": 415,
        "meaning": "xarajat — sarflash",
        "note": "<p>비용, 소비, 학비, 생활비, 교통비. So‘z oxirida «to‘lov» yasaydi.</p>",
    },
    {
        "syllable": "금", "hanja": "金", "order": 420,
        "meaning": "oltin, pul — mablag‘",
        "note": "<p>임금 (ish haqi), 요금 (to‘lov), 세금 (soliq), 현금 (naqd), 장학금 (stipendiya).</p>",
    },
    {
        "syllable": "정", "hanja": "政", "order": 425,
        "meaning": "siyosat — boshqaruv",
        "note": "<p>정부, 정책, 정치, 행정. ⚠️ <b>정(定)</b> = belgilamoq (결정, 안정) — "
                "boshqa o‘zak, shuning uchun <code>정(政)</code> deb yozing.</p>",
    },
    {
        "syllable": "복", "hanja": "福", "order": 430,
        "meaning": "baxt, farovonlik",
        "note": "<p>복지 (ijtimoiy farovonlik), 행복 (baxt), 축복.</p>",
    },
    {
        "syllable": "노", "hanja": "勞", "order": 435,
        "meaning": "mehnat — zahmat",
        "note": "<p>노동 (mehnat), 노력 (harakat), 근로자, 과로 (haddan ortiq ishlash).</p>",
    },
]

WORDS = [
    # ── Ish topish va ish joyi ────────────────────────────────────────────
    {
        "word": "취업", "hanja": "就業", "roots": ["업"],
        "pos": "noun", "topic": "work", "level": 4, "freq": 3, "order": 600,
        "meaning": "ishga joylashish — «kirishmoq + ish»",
        "collocation": "취업하다 · 취업난 · 청년 취업 · 취업 준비",
        "note": "<p><b>쓰기 53/54 ning eng ko‘p mavzularidan biri</b> — 청년 실업 bilan birga. "
                "«Ishsizlik qiyinchiligi» = <b>취업난</b>.</p>",
        "examples": [
            ("요즘 청년 취업이 매우 어렵다.", "Hozir yoshlarning ishga joylashishi juda qiyin."),
            ("졸업 후 바로 취업하고 싶어요.", "Bitirgach darrov ishga kirmoqchiman."),
        ],
        "antonyms": [("실업", "ishsizlik")],
        "related": [("직업", "kasb — 취업 = jarayon, 직업 = natijadagi kasb")],
    },
    {
        "word": "실업", "hanja": "失業", "roots": ["업"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 3, "order": 601,
        "meaning": "ishsizlik — «yo‘qotmoq + ish»",
        "collocation": "실업률 · 실업자 · 청년 실업",
        "note": "<p><b>쓰기 53 grafiklarida:</b> <i>실업률이 꾸준히 상승하였다.</i></p>",
        "examples": [
            ("청년 실업률이 계속 높아지고 있다.", "Yoshlar ishsizlik darajasi muttasil oshib bormoqda."),
        ],
        "antonyms": [("취업", "ishga joylashish")],
    },
    {
        "word": "직업", "hanja": "職業", "roots": ["직", "업"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 3, "order": 602,
        "meaning": "kasb, hunar — «lavozim + ish»",
        "collocation": "직업을 구하다 · 직업 선택 · 전문 직업",
        "examples": [
            ("직업을 선택할 때 무엇을 가장 중요하게 생각합니까?", "Kasb tanlashda nimani eng muhim deb bilasiz?"),
        ],
    },
    {
        "word": "직장", "hanja": "職場", "roots": ["직", "장"],
        "pos": "noun", "topic": "work", "level": 3, "freq": 3, "order": 603,
        "meaning": "ish joyi — «lavozim + maydon»",
        "collocation": "직장 생활 · 직장 동료 · 직장을 옮기다",
        "examples": [
            ("직장 생활에 적응하는 데 시간이 걸렸다.", "Ish hayotiga moslashishga vaqt ketdi."),
        ],
    },
    {
        "word": "면접", "hanja": "面接", "roots": [],
        "pos": "noun", "topic": "work", "level": 4, "freq": 3, "order": 604,
        "meaning": "suhbat, intervyu — «yuz + ko‘rishish»",
        "collocation": "면접을 보다 · 면접 준비 · 면접관",
        "note": "<p>⚠️ «Suhbatdan o‘tmoq» = <b>면접을 보다</b> (하다 emas).</p>",
        "examples": [
            ("내일 회사 면접을 봐요.", "Ertaga kompaniyada suhbatdan o‘taman."),
        ],
    },
    {
        "word": "사업", "hanja": "事業", "roots": ["업"],
        "pos": "noun", "topic": "work", "level": 4, "freq": 2, "order": 605,
        "meaning": "biznes, tadbirkorlik; loyiha",
        "collocation": "사업을 시작하다 · 사업가 · 지원 사업",
        "examples": [
            ("정부가 새로운 지원 사업을 시작했다.", "Hukumat yangi qo‘llab-quvvatlash loyihasini boshladi."),
        ],
    },
    {
        "word": "기업", "hanja": "企業", "roots": ["업"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 3, "order": 606,
        "meaning": "korxona, kompaniya (rasmiy)",
        "collocation": "대기업 · 중소기업 · 기업 문화",
        "note": "<p><b>회사</b> = kundalik «kompaniya»; <b>기업</b> = iqtisodiy atama. "
                "쓰기 54 da 기업 ishlating.</p>",
        "examples": [
            ("대기업보다 중소기업에서 일하고 싶다.", "Yirik korxonadan ko‘ra kichik korxonada ishlamoqchiman."),
        ],
        "synonyms": [("회사", "회사 = og‘zaki/kundalik; 기업 = rasmiy iqtisodiy atama")],
    },
    {
        "word": "노동", "hanja": "勞動", "roots": ["노", "동"],
        "pos": "noun", "topic": "work", "level": 5, "freq": 2, "order": 607,
        "meaning": "mehnat, ish kuchi",
        "collocation": "노동 시간 · 노동자 · 노동력 부족",
        "examples": [
            ("고령화로 노동력이 부족해지고 있다.", "Aholining qarishi tufayli ish kuchi yetishmayapti."),
        ],
    },
    {
        "word": "월급", "hanja": "月給", "roots": [],
        "pos": "noun", "topic": "work", "level": 2, "freq": 2, "order": 608,
        "meaning": "oylik maosh — «oy + berish»",
        "collocation": "월급을 받다 · 월급이 오르다",
        "examples": [
            ("월급날은 매달 25일이에요.", "Maosh kuni har oyning 25-sanasi."),
        ],
        "synonyms": [("임금", "임금 = rasmiy/iqtisodiy «ish haqi»; 월급 = kundalik «oylik»")],
    },
    {
        "word": "임금", "hanja": "賃金", "roots": ["금"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 2, "order": 609,
        "meaning": "ish haqi (rasmiy atama)",
        "collocation": "최저 임금 · 임금 인상 · 임금 격차",
        "note": "<p><b>최저 임금</b> (eng kam ish haqi) — 읽기 va 쓰기 da tez-tez.</p>",
        "examples": [
            ("최저 임금이 매년 조금씩 오르고 있다.", "Eng kam ish haqi har yili bir oz oshmoqda."),
        ],
        "synonyms": [("월급", "월급 = og‘zaki «oylik»; 임금 = rasmiy atama")],
    },

    # ── Iqtisod ──────────────────────────────────────────────────────────
    {
        "word": "소비", "hanja": "消費", "roots": ["소(消)", "비"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 620,
        "meaning": "iste’mol — «sarflash + xarajat»",
        "collocation": "소비하다 · 소비자 · 소비 습관 · 합리적 소비",
        "note": "<p>Foydalanuvchining 읽기→쓰기 ko‘prigidagi namuna jumla shu so‘z bilan: "
                "<i>합리적 소비를 하면 자연스럽게 사회 활동에도 동참할 수 있다.</i></p>",
        "examples": [
            ("젊은 층의 소비 형태가 크게 달라졌다.", "Yoshlarning iste’mol shakli keskin o‘zgardi."),
        ],
        "antonyms": [("생산", "ishlab chiqarish — 消費↔生産")],
    },
    {
        "word": "지출", "hanja": "支出", "roots": ["출"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 2, "order": 621,
        "meaning": "xarajat, sarf — «chiqarish»",
        "collocation": "지출을 줄이다 · 생활 지출 · 지출 항목",
        "note": "<p>Yana bitta <b>출(出)</b> oilasi a’zosi: pul «chiqib ketadi».</p>",
        "examples": [
            ("소득보다 지출이 많으면 문제가 생긴다.", "Daromaddan xarajat ko‘p bo‘lsa muammo tug‘iladi."),
        ],
        "antonyms": [("수입", "daromad — 수입(收入); ⚠️ 수입(輸入) «import» bilan chalkashtirmang")],
    },
    {
        "word": "소득", "hanja": "所得", "roots": ["소(所)"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 3, "order": 622,
        "meaning": "daromad — «olingan narsa»",
        "collocation": "소득이 늘다 · 평균 소득 · 소득 격차",
        "note": "<p><b>쓰기 53 grafiklarining doimiy o‘qi:</b> 소득 수준별, 연령별.</p>",
        "examples": [
            ("소득이 높을수록 저축도 늘어난다.", "Daromad qanchalik yuqori bo‘lsa, jamg‘arma ham shuncha ortadi."),
        ],
        "antonyms": [("지출", "xarajat")],
    },
    {
        "word": "저축", "hanja": "貯蓄", "roots": [],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 2, "order": 623,
        "meaning": "jamg‘arma, pul yig‘ish",
        "collocation": "저축하다 · 저축률 · 노후 저축",
        "examples": [
            ("매달 월급의 삼십 퍼센트를 저축한다.", "Har oy maoshning o‘ttiz foizini jamg‘araman."),
        ],
    },
    {
        "word": "세금", "hanja": "稅金", "roots": ["금"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 2, "order": 624,
        "meaning": "soliq",
        "collocation": "세금을 내다 · 세금 부담 · 소득세",
        "examples": [
            ("국민은 소득에 따라 세금을 낸다.", "Fuqarolar daromadiga qarab soliq to‘laydi."),
        ],
    },
    {
        "word": "물가", "hanja": "物價", "roots": [],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 625,
        "meaning": "narx-navo (umumiy narxlar darajasi)",
        "collocation": "물가가 오르다 · 물가 상승 · 물가가 비싸다",
        "note": "<p>⚠️ Bitta buyum narxi = <b>가격</b>; umumiy narxlar darajasi = <b>물가</b>.</p>",
        "examples": [
            ("최근 물가가 계속 오르고 있다.", "So‘nggi paytda narxlar muttasil oshmoqda."),
        ],
        "related": [("가격", "가격 = bitta mahsulot narxi; 물가 = umumiy narx darajasi")],
    },
    {
        "word": "성장", "hanja": "成長", "roots": [],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 626,
        "meaning": "o‘sish, rivojlanish (iqtisod va odam)",
        "collocation": "경제 성장 · 성장하다 · 성장률",
        "examples": [
            ("경제 성장률이 작년보다 낮아졌다.", "Iqtisodiy o‘sish sur’ati o‘tgan yildan pasaydi."),
        ],
    },

    # ── Jamiyat va siyosat ───────────────────────────────────────────────
    {
        "word": "정부", "hanja": "政府", "roots": ["정(政)"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 640,
        "meaning": "hukumat",
        "collocation": "정부가 발표하다 · 정부 지원 · 중앙 정부",
        "note": "<p><b>쓰기 54 taklif qismining doimiy egasi:</b> "
                "<i>정부는 [정책]을/를 마련해야 한다.</i></p>",
        "examples": [
            ("정부는 새로운 대책을 발표했다.", "Hukumat yangi chora-tadbirni e’lon qildi."),
        ],
    },
    {
        "word": "정책", "hanja": "政策", "roots": ["정(政)"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 641,
        "meaning": "siyosat, dastur (davlat chorasi)",
        "collocation": "정책을 마련하다 · 지원 정책 · 정책의 효과",
        "examples": [
            ("출산율을 높이기 위한 정책이 필요하다.", "Tug‘ilish darajasini oshirish uchun siyosat zarur."),
        ],
        "related": [("제도", "제도 = o‘rnatilgan tizim; 정책 = uni amalga oshiruvchi chora")],
    },
    {
        "word": "복지", "hanja": "福祉", "roots": ["복"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 642,
        "meaning": "ijtimoiy farovonlik, ta’minot",
        "collocation": "복지 제도 · 사회 복지 · 복지 혜택",
        "examples": [
            ("복지 제도를 확대할 필요가 있다.", "Ijtimoiy ta’minot tizimini kengaytirish zarur."),
        ],
    },
    {
        "word": "대책", "hanja": "對策", "roots": [],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 643,
        "meaning": "chora-tadbir, yechim",
        "collocation": "대책을 마련하다 · 근본적인 대책 · 대책이 시급하다",
        "note": "<p><b>쓰기 54 xulosasi uchun oltin so‘z:</b> "
                "<i>이에 대한 근본적인 대책이 필요하다.</i></p>",
        "examples": [
            ("환경 오염에 대한 대책이 시급하다.", "Atrof-muhit ifloslanishiga qarshi chora zudlik bilan kerak."),
        ],
        "synonyms": [("해결책", "해결책 = aniq yechim; 대책 = qarshi ko‘riladigan chora")],
    },
    {
        "word": "지원", "hanja": "支援", "roots": [],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 644,
        "meaning": "yordam, qo‘llab-quvvatlash; ariza berish",
        "collocation": "지원하다 · 정부 지원 · 지원금 · 회사에 지원하다",
        "note": "<p>⚠️ Ikki ma’no: <b>支援</b> (qo‘llab-quvvatlash) va "
                "<b>志願</b> (ariza berish, nomzod bo‘lish). Kontekst hal qiladi.</p>",
        "examples": [
            ("정부가 청년 창업을 지원한다.", "Hukumat yoshlar tadbirkorligini qo‘llab-quvvatlaydi."),
            ("세 개 회사에 지원했어요.", "Uchta kompaniyaga ariza berdim."),
        ],
    },
    {
        "word": "참여", "hanja": "參與", "roots": [],
        "pos": "noun", "topic": "society", "level": 4, "freq": 2, "order": 645,
        "meaning": "ishtirok, qatnashish",
        "collocation": "참여하다 · 시민 참여 · 참여율",
        "examples": [
            ("투표 참여율이 지난번보다 높았다.", "Ovoz berishda ishtirok darajasi o‘tgan safargidan yuqori bo‘ldi."),
        ],
    },
    {
        "word": "갈등", "hanja": "葛藤", "roots": [],
        "pos": "noun", "topic": "society", "level": 5, "freq": 2, "order": 646,
        "meaning": "ziddiyat, kelishmovchilik",
        "collocation": "갈등이 생기다 · 세대 갈등 · 갈등을 해결하다",
        "note": "<p>쓰기 54 munozara mavzularida ko‘p: 세대 갈등, 노사 갈등.</p>",
        "examples": [
            ("세대 간의 갈등이 사회 문제가 되고 있다.", "Avlodlar orasidagi ziddiyat ijtimoiy muammoga aylanmoqda."),
        ],
    },
    {
        "word": "인식", "hanja": "認識", "roots": [],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 647,
        "meaning": "anglash, qarash, ong",
        "collocation": "인식을 바꾸다 · 인식이 부족하다 · 사회적 인식",
        "note": "<p><b>쓰기 54 uchun kuchli qolip:</b> "
                "<i>인식이 바뀌지 않는 한 문제는 해결되지 않을 것이다.</i></p>",
        "examples": [
            ("환경에 대한 인식이 많이 높아졌다.", "Atrof-muhitga bo‘lgan ong ancha ko‘tarildi."),
        ],
    },
    {
        "word": "역할", "hanja": "役割", "roots": [],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 648,
        "meaning": "rol, vazifa",
        "collocation": "역할을 하다 · 중요한 역할 · 역할 분담",
        "note": "<p>⚠️ Talaffuzi [여칼]. 쓰기 da: "
                "<i>[주체]은/는 중요한 역할을 한다.</i></p>",
        "examples": [
            ("가정 교육이 중요한 역할을 한다.", "Oila tarbiyasi muhim rol o‘ynaydi."),
        ],
    },
]
