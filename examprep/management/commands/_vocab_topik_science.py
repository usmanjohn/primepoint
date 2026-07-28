# -*- coding: utf-8 -*-
"""Vocab bank — mavzuli lug'at 3: ekologiya, fan-texnika va madaniyat.

Order decade 700-799; new roots 450-499. The 읽기 41-50 subject areas.
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
        "syllable": "환", "hanja": "環", "order": 450,
        "meaning": "halqa — atrof, aylana",
        "note": "<p>환경 (atrof-muhit), 순환 (aylanish), 환경친화적. "
                "⚠️ <b>환(換)</b> = almashtirmoq (교환, 환전) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "경", "hanja": "境", "order": 455,
        "meaning": "chegara — hudud, sharoit",
        "note": "<p>환경, 국경, 경계. ⚠️ Bankda ikkita <b>경</b> bor: "
                "經 (iqtisod, tajriba) va 境 (chegara). Data faylda <code>경(境)</code> deb yozing.</p>",
    },
    {
        "syllable": "오", "hanja": "汚", "order": 460,
        "meaning": "iflos — bulg‘anish",
        "note": "<p>오염 (ifloslanish), 오물. Deyarli faqat 오염 birikmasida uchraydi.</p>",
    },
    {
        "syllable": "재", "hanja": "再", "order": 465,
        "meaning": "qayta — yana",
        "note": "<p>Prefiks: 재활용 (qayta ishlatish), 재사용, 재개발, 재검토. "
                "Notanish so‘z 재- bilan boshlansa, «qayta ...» deb o‘qing. "
                "⚠️ <b>재(材)</b> = xomashyo (재료), <b>재(災)</b> = ofat (재해).</p>",
    },
    {
        "syllable": "자", "hanja": "資", "order": 470,
        "meaning": "resurs, mablag‘",
        "note": "<p>자원 (resurs), 자료 (material, ma’lumot), 투자 (investitsiya). "
                "⚠️ Bankda uch xil <b>자</b>: 者 (kishi), 自 (o‘zi), 資 (resurs).</p>",
    },
    {
        "syllable": "기", "hanja": "技", "order": 475,
        "meaning": "mahorat — texnika",
        "note": "<p>기술 (texnologiya), 기능. ⚠️ <b>기(氣)</b> = kayfiyat/havo (인기, 기온), "
                "<b>기(機)</b> = mashina (기계, 기회).</p>",
    },
    {
        "syllable": "정", "hanja": "情", "order": 480,
        "meaning": "tuyg‘u, ma’lumot",
        "note": "<p>감정 (tuyg‘u), 정보 (axborot). ⚠️ Bankda uchta <b>정</b>: "
                "定 (belgilamoq), 政 (siyosat), 情 (tuyg‘u/axborot) — "
                "data faylda <code>정(情)</code> deb yozing.</p>",
    },
    {
        "syllable": "문", "hanja": "文", "order": 485,
        "meaning": "yozuv — madaniyat, matn",
        "note": "<p>문화, 문학, 문서, 논문, 신문. ⚠️ <b>문(門)</b> = eshik (정문, 대문), "
                "<b>문(問)</b> = so‘ramoq (질문, 문제).</p>",
    },
    {
        "syllable": "전", "hanja": "傳", "order": 490,
        "meaning": "yetkazmoq — an’ana, uzatish",
        "note": "<p>전통 (an’ana), 전달, 전화? — yo‘q, u 電. "
                "⚠️ Bankda: 傳 (yetkazmoq), 電 (elektr), 全 (butun), 前 (oldin).</p>",
    },
]

WORDS = [
    # ── Ekologiya ────────────────────────────────────────────────────────
    {
        "word": "환경", "hanja": "環境", "roots": ["환", "경(境)"],
        "pos": "noun", "topic": "environment", "level": 3, "freq": 3, "order": 700,
        "meaning": "atrof-muhit; sharoit — «atrof + chegara»",
        "collocation": "환경 보호 · 환경 오염 · 자연환경 · 교육 환경",
        "note": "<p><b>쓰기 54 ning eng ko‘p mavzusi.</b> Ikkinchi ma’nosi «sharoit»: "
                "<i>교육 <b>환경</b>이 좋다</i>.</p>",
        "examples": [
            ("환경을 지키는 일은 모두의 책임이다.", "Atrof-muhitni asrash — hammaning mas’uliyati."),
        ],
    },
    {
        "word": "오염", "hanja": "汚染", "roots": ["오"],
        "pos": "noun", "topic": "environment", "level": 4, "freq": 3, "order": 701,
        "meaning": "ifloslanish — «iflos + bo‘yalish»",
        "collocation": "환경 오염 · 대기 오염 · 오염되다 · 수질 오염",
        "examples": [
            ("대기 오염이 건강에 나쁜 영향을 미친다.", "Havo ifloslanishi sog‘liqqa yomon ta’sir qiladi."),
        ],
    },
    {
        "word": "재활용", "hanja": "再活用", "roots": ["재", "용"],
        "pos": "noun", "topic": "environment", "level": 4, "freq": 3, "order": 702,
        "meaning": "qayta ishlatish — «qayta + faol + foydalanish»",
        "collocation": "재활용하다 · 재활용품 · 분리수거",
        "note": "<p>Uch o‘zak birga — <b>再</b>+<b>活</b>+<b>用</b>. Shu qolipda: "
                "재사용, 재개발, 재검토.</p>",
        "examples": [
            ("플라스틱은 반드시 재활용해야 한다.", "Plastikni albatta qayta ishlatish kerak."),
        ],
    },
    {
        "word": "자원", "hanja": "資源", "roots": ["자(資)"],
        "pos": "noun", "topic": "environment", "level": 5, "freq": 2, "order": 703,
        "meaning": "resurs, boylik — «mablag‘ + manba»",
        "collocation": "천연자원 · 자원을 절약하다 · 인적 자원",
        "examples": [
            ("한정된 자원을 아껴 써야 한다.", "Cheklangan resurslarni tejab ishlatish kerak."),
        ],
    },
    {
        "word": "절약", "hanja": "節約", "roots": [],
        "pos": "noun", "topic": "environment", "level": 4, "freq": 2, "order": 704,
        "meaning": "tejash, iqtisod qilish",
        "collocation": "절약하다 · 에너지 절약 · 시간을 절약하다",
        "examples": [
            ("전기를 절약하면 환경에도 도움이 된다.", "Elektrni tejasangiz atrof-muhitga ham foyda."),
        ],
        "antonyms": [("낭비", "isrof qilish")],
    },
    {
        "word": "낭비", "hanja": "浪費", "roots": ["비"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 2, "order": 705,
        "meaning": "isrof, behuda sarflash",
        "collocation": "낭비하다 · 시간 낭비 · 자원 낭비",
        "examples": [
            ("교통 체증으로 시간을 낭비하게 된다.", "Tirbandlik tufayli vaqt behuda ketadi."),
        ],
        "antonyms": [("절약", "tejash")],
    },
    {
        "word": "기후", "hanja": "氣候", "roots": [],
        "pos": "noun", "topic": "environment", "level": 5, "freq": 3, "order": 706,
        "meaning": "iqlim",
        "collocation": "기후 변화 · 기후 위기 · 온난화",
        "note": "<p>⚠️ <b>날씨</b> = kunlik ob-havo; <b>기후</b> = uzoq muddatli iqlim. "
                "TOPIK atayin farqlaydi.</p>",
        "examples": [
            ("기후 변화로 자연재해가 늘고 있다.", "Iqlim o‘zgarishi tufayli tabiiy ofatlar ko‘paymoqda."),
        ],
        "related": [("날씨", "날씨 = bugungi ob-havo; 기후 = mintaqaning uzoq muddatli iqlimi")],
    },
    {
        "word": "보호", "hanja": "保護", "roots": [],
        "pos": "noun", "topic": "environment", "level": 4, "freq": 3, "order": 707,
        "meaning": "muhofaza, himoya qilish",
        "collocation": "환경 보호 · 보호하다 · 소비자 보호",
        "examples": [
            ("동물을 보호하는 법이 만들어졌다.", "Hayvonlarni muhofaza qilish qonuni qabul qilindi."),
        ],
    },

    # ── Fan va texnologiya ───────────────────────────────────────────────
    {
        "word": "기술", "hanja": "技術", "roots": ["기"],
        "pos": "noun", "topic": "science", "level": 4, "freq": 3, "order": 720,
        "meaning": "texnologiya, mahorat — «mahorat + usul»",
        "collocation": "과학 기술 · 기술이 발전하다 · 첨단 기술",
        "note": "<p><b>쓰기 54 uchun tayyor qolip:</b> "
                "<i>기술이 발전할수록 인간관계는 오히려 약해진다.</i></p>",
        "examples": [
            ("새로운 기술이 우리 생활을 바꾸고 있다.", "Yangi texnologiya hayotimizni o‘zgartirmoqda."),
        ],
    },
    {
        "word": "정보", "hanja": "情報", "roots": ["정(情)"],
        "pos": "noun", "topic": "media", "level": 3, "freq": 3, "order": 721,
        "meaning": "axborot, ma’lumot",
        "collocation": "정보를 얻다 · 정보화 사회 · 개인 정보",
        "examples": [
            ("인터넷에서 필요한 정보를 쉽게 찾을 수 있다.", "Internetdan kerakli ma’lumotni oson topsa bo‘ladi."),
        ],
    },
    {
        "word": "인공지능", "hanja": "人工知能", "roots": ["인"],
        "pos": "noun", "topic": "science", "level": 5, "freq": 2, "order": 722,
        "meaning": "sun’iy intellekt — «inson + yasama + bilim + qobiliyat»",
        "collocation": "인공지능 기술 · AI 시대",
        "note": "<p>To‘rt o‘zakli so‘z — Hanja’ni bo‘lib o‘qisangiz ma’nosi o‘zi chiqadi. "
                "읽기 41-50 ning zamonaviy mavzusi.</p>",
        "examples": [
            ("인공지능이 많은 일자리를 대신하게 될 것이다.", "Sun’iy intellekt ko‘p ish o‘rnini egallaydi."),
        ],
    },
    {
        "word": "연구", "hanja": "硏究", "roots": [],
        "pos": "noun", "topic": "science", "level": 4, "freq": 3, "order": 723,
        "meaning": "tadqiqot, izlanish",
        "collocation": "연구하다 · 연구 결과 · 연구자",
        "note": "<p><b>쓰기 53 manba qolipi:</b> "
                "<i>한 연구에 따르면 ...다고 한다.</i></p>",
        "examples": [
            ("최근 연구 결과가 흥미롭다.", "So‘nggi tadqiqot natijasi qiziqarli."),
        ],
    },
    {
        "word": "조사", "hanja": "調査", "roots": [],
        "pos": "noun", "topic": "science", "level": 4, "freq": 3, "order": 724,
        "meaning": "so‘rovnoma, tekshiruv",
        "collocation": "조사하다 · 조사 결과 · 설문 조사 · 조사 대상",
        "note": "<p><b>쓰기 53 ning birinchi jumlasi doim shu bilan boshlanadi:</b> "
                "<i>[기관]에서 [대상]을/를 대상으로 <b>조사</b>를 실시하였다.</i></p>",
        "examples": [
            ("설문 조사 결과 절반이 찬성했다.", "So‘rovnoma natijasiga ko‘ra yarmi rozi bo‘ldi."),
        ],
    },
    {
        "word": "결과", "hanja": "結果", "roots": [],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 725,
        "meaning": "natija",
        "collocation": "결과가 나오다 · 조사 결과 · 그 결과",
        "examples": [
            ("조사 결과 남녀 간에 차이가 있었다.", "Tadqiqot natijasida erkak va ayollar orasida farq bor edi."),
        ],
        "antonyms": [("원인", "sabab — natijaning teskarisi")],
    },
    {
        "word": "원인", "hanja": "原因", "roots": ["인"],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 3, "order": 726,
        "meaning": "sabab, asosiy omil",
        "collocation": "원인을 찾다 · 주요 원인 · 근본 원인",
        "note": "<p><b>쓰기 54 tuzilishi:</b> 원인 → 문제 → 대책. Uchalasini birga yodlang.</p>",
        "examples": [
            ("문제의 원인을 먼저 찾아야 한다.", "Avval muammoning sababini topish kerak."),
        ],
        "antonyms": [("결과", "natija")],
    },
    {
        "word": "효과", "hanja": "效果", "roots": [],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 3, "order": 727,
        "meaning": "samara, ta’sir",
        "collocation": "효과가 있다 · 효과적이다 · 부작용",
        "examples": [
            ("이 방법은 효과가 크지 않았다.", "Bu usulning samarasi katta bo‘lmadi."),
        ],
    },
    {
        "word": "실시하다", "hanja": "實施—", "roots": [],
        "pos": "verb", "topic": "society", "level": 5, "freq": 3, "order": 728,
        "meaning": "amalga oshirmoq, o‘tkazmoq (rasmiy)",
        "collocation": "조사를 실시하다 · 정책을 실시하다",
        "note": "<p>쓰기 53 ning ochilish fe’li — <b>조사를 실시하였다</b>.</p>",
        "examples": [
            ("통계청에서 전국 조사를 실시하였다.", "Statistika qo‘mitasi mamlakat bo‘ylab so‘rov o‘tkazdi."),
        ],
    },

    # ── Madaniyat va an'ana ─────────────────────────────────────────────
    {
        "word": "문화", "hanja": "文化", "roots": ["문", "화"],
        "pos": "noun", "topic": "culture", "level": 2, "freq": 3, "order": 740,
        "meaning": "madaniyat — «yozuv + aylanish»",
        "collocation": "전통문화 · 문화 차이 · 대중문화 · 문화재",
        "examples": [
            ("나라마다 문화가 달라서 재미있다.", "Har mamlakatning madaniyati har xil bo‘lgani qiziq."),
        ],
    },
    {
        "word": "전통", "hanja": "傳統", "roots": ["전"],
        "pos": "noun", "topic": "culture", "level": 4, "freq": 3, "order": 741,
        "meaning": "an’ana — «yetkazmoq + tizim»",
        "collocation": "전통문화 · 전통적이다 · 전통을 지키다",
        "examples": [
            ("전통을 지키면서 새로운 것도 받아들여야 한다.", "An’anani saqlagan holda yangilikni ham qabul qilish kerak."),
        ],
        "antonyms": [("현대", "zamonaviylik")],
    },
    {
        "word": "현대", "hanja": "現代", "roots": ["대"],
        "pos": "noun", "topic": "time", "level": 4, "freq": 3, "order": 742,
        "meaning": "hozirgi zamon, zamonaviylik",
        "collocation": "현대 사회 · 현대인 · 현대적이다",
        "note": "<p><b>쓰기 54 ning birinchi so‘zi:</b> "
                "<i>현대 사회에서 [주제]은/는 점점 더 중요한 문제가 되고 있다.</i></p>",
        "examples": [
            ("현대인은 늘 시간에 쫓긴다.", "Zamonaviy odam doim vaqt ketidan quvadi."),
        ],
        "antonyms": [("전통", "an’ana")],
    },
    {
        "word": "예술", "hanja": "藝術", "roots": [],
        "pos": "noun", "topic": "culture", "level": 4, "freq": 2, "order": 743,
        "meaning": "san’at",
        "collocation": "예술 작품 · 예술가 · 공연 예술",
        "examples": [
            ("예술은 사람의 마음을 위로한다.", "San’at odamning ko‘nglini taskinlaydi."),
        ],
    },
    {
        "word": "작품", "hanja": "作品", "roots": [],
        "pos": "noun", "topic": "culture", "level": 4, "freq": 2, "order": 744,
        "meaning": "asar (badiiy)",
        "collocation": "작품을 만들다 · 대표 작품 · 문학 작품",
        "examples": [
            ("이 작품은 세계적으로 유명하다.", "Bu asar dunyo miqyosida mashhur."),
        ],
    },
    {
        "word": "세대", "hanja": "世代", "roots": ["대"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 745,
        "meaning": "avlod",
        "collocation": "세대 차이 · 세대 갈등 · 젊은 세대",
        "examples": [
            ("세대에 따라 생각하는 방식이 다르다.", "Avlodga qarab fikrlash tarzi har xil."),
        ],
    },
    {
        "word": "대중", "hanja": "大衆", "roots": ["대"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 2, "order": 746,
        "meaning": "ommaviy, keng jamoatchilik",
        "collocation": "대중교통 · 대중문화 · 대중매체",
        "note": "<p><b>대중교통</b> (jamoat transporti) — 읽기 va 쓰기 da doim uchraydi.</p>",
        "examples": [
            ("대중교통을 이용하면 환경에 도움이 된다.", "Jamoat transportidan foydalansangiz atrof-muhitga foyda."),
        ],
    },
    {
        "word": "매체", "hanja": "媒體", "roots": [],
        "pos": "noun", "topic": "media", "level": 5, "freq": 2, "order": 747,
        "meaning": "vosita, OAV",
        "collocation": "대중매체 · 매체를 통해 · 뉴스 매체",
        "examples": [
            ("다양한 매체를 통해 정보를 얻는다.", "Turli vositalar orqali ma’lumot olaman."),
        ],
    },
]
