# -*- coding: utf-8 -*-
"""Vocab bank — 부사: ravishlar to'plami.

Order decade 800-899. The user's own emphasis: "otdan ko'ra sifat, ravish,
fe'lni ko'proq o'rganing — javoblarni asosan shular hal qiladi". Adverbs are
the highest-yield word class in TOPIK reading: they signal contrast, degree
and negation, and the answer usually turns on one of them.

Adverbs already in the bank from _vocab_topik_daily.py (오히려, 비록, 결코,
마침내, 결국, 점점, 특히, 아무래도, 그저, 무려) are not repeated here.
See STYLE_GUIDE_VOCAB.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

WORDS = [
    # ── Inkor talab qiladiganlar (eng ko'p xato shu yerda) ────────────────
    {
        "word": "전혀", "hanja": "全—", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 3, "order": 800,
        "meaning": "umuman, mutlaqo (inkor bilan)",
        "collocation": "전혀 모르다 · 전혀 없다 · 전혀 ~지 않다",
        "note": "<p>⚠️ <b>Doim inkor bilan.</b> ❌ 전혀 알아요 → ✅ 전혀 <b>몰라요</b>. "
                "Shu oila: 전혀, 별로, 결코, 절대, 도저히, 좀처럼 — hammasi inkor talab qiladi. "
                "TOPIK 읽기 da bo‘sh joyga ravish tanlashda shu qoida javobni beradi.</p>",
        "examples": [
            ("그 사람에 대해 전혀 몰랐어요.", "U odam haqida umuman bilmasdim."),
        ],
        "synonyms": [("별로", "별로 = «unchalik emas» (yumshoq); 전혀 = «umuman yo‘q» (qat’iy)")],
    },
    {
        "word": "별로", "hanja": "別—", "pos": "adv", "topic": "abstract",
        "level": 2, "freq": 3, "order": 801,
        "meaning": "unchalik, u qadar emas (inkor bilan)",
        "collocation": "별로 안 좋다 · 별로 없다 · 별로 ~지 않다",
        "note": "<p>⚠️ Inkor talab qiladi. Koreyada rad javobini yumshatish uchun ham: "
                "<i>— 어때요? — 별로예요.</i> («unchalik emas» = yoqmadi).</p>",
        "examples": [
            ("이 영화는 별로 재미없었어요.", "Bu kino unchalik qiziq bo‘lmadi."),
        ],
        "synonyms": [("전혀", "전혀 = mutlaqo; 별로 = unchalik emas")],
    },
    {
        "word": "도저히", "hanja": "到底—", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 802,
        "meaning": "sira, hech qanday yo‘l bilan (inkor bilan)",
        "collocation": "도저히 이해할 수 없다 · 도저히 못 하다",
        "note": "<p>⚠️ Inkor bilan. «Qanchalik urinsam ham bo‘lmadi» ohangi bor — "
                "shunchaki 못 하다 dan kuchliroq.</p>",
        "examples": [
            ("그의 행동을 도저히 이해할 수 없다.", "Uning xatti-harakatini sira tushunolmayman."),
        ],
    },
    {
        "word": "좀처럼", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 1, "order": 803,
        "meaning": "kamdan-kam, oson emas (inkor bilan)",
        "collocation": "좀처럼 ~지 않다 · 좀처럼 보기 힘들다",
        "note": "<p>⚠️ Inkor bilan. «Odatda bunday bo‘lmaydi» ma’nosi.</p>",
        "examples": [
            ("그는 좀처럼 화를 내지 않는다.", "U kamdan-kam jahli chiqadi."),
        ],
    },

    # ── Ta'kid va daraja ─────────────────────────────────────────────────
    {
        "word": "반드시", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 3, "order": 810,
        "meaning": "albatta, shubhasiz (majburiyat)",
        "collocation": "반드시 ~아야 하다 · 반드시 지키다",
        "note": "<p><b>꼭</b> = og‘zaki «albatta»; <b>반드시</b> = rasmiy/yozma. "
                "쓰기 54 da 반드시 ishlating.</p>",
        "examples": [
            ("안전 규칙은 반드시 지켜야 한다.", "Xavfsizlik qoidalariga albatta rioya qilish kerak."),
        ],
        "synonyms": [("꼭", "꼭 = og‘zaki, iltimos bilan ham; 반드시 = rasmiy majburiyat")],
    },
    {
        "word": "심지어", "hanja": "甚至於", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 811,
        "meaning": "hatto, hatto shu darajaga borib",
        "collocation": "심지어 ~까지 · 심지어 ~도",
        "note": "<p>Kutilganidan ortiq holatni qo‘shadi, ko‘pincha <b>-까지 / -도</b> bilan. "
                "읽기 da fikrni kuchaytirish belgisi.</p>",
        "examples": [
            ("그는 바빠서 심지어 밥 먹을 시간도 없다.", "U shunchalik bandki, hatto ovqatlanishga ham vaqti yo‘q."),
        ],
    },
    {
        "word": "훨씬", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 3, "order": 812,
        "meaning": "ancha, birmuncha ko‘proq (taqqoslashda)",
        "collocation": "훨씬 더 · 훨씬 낫다 · A보다 훨씬",
        "note": "<p>Faqat <b>taqqoslash</b>da: 보다 + 훨씬 + 더. "
                "❌ 훨씬 좋아요 (taqqoslanmagan) → ✅ 이것보다 <b>훨씬</b> 좋아요.</p>",
        "examples": [
            ("지하철이 버스보다 훨씬 빠르다.", "Metro avtobusdan ancha tezroq."),
        ],
    },
    {
        "word": "워낙", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 1, "order": 813,
        "meaning": "juda ham, asli shunchalik (sabab ohangi)",
        "collocation": "워낙 바쁘다 · 워낙 유명하다",
        "note": "<p>«Aslida shunday bo‘lgani uchun» degan sabab ohangi bor — "
                "shunchaki 아주 emas.</p>",
        "examples": [
            ("워낙 유명해서 예약하기가 어렵다.", "Juda mashhur bo‘lgani uchun joy band qilish qiyin."),
        ],
    },
    {
        "word": "거의", "pos": "adv", "topic": "abstract",
        "level": 2, "freq": 3, "order": 814,
        "meaning": "deyarli, taxminan",
        "collocation": "거의 다 · 거의 없다 · 거의 매일",
        "examples": [
            ("숙제를 거의 다 했어요.", "Uy vazifasini deyarli tugatdim."),
        ],
    },

    # ── Vaqt va ketma-ketlik ─────────────────────────────────────────────
    {
        "word": "여전히", "hanja": "如前—", "pos": "adv", "topic": "time",
        "level": 4, "freq": 3, "order": 820,
        "meaning": "hamon, hanuz (o‘zgarmagan holda)",
        "collocation": "여전히 ~고 있다 · 여전히 심각하다",
        "note": "<p><b>쓰기 54 da kuchli:</b> «chora ko‘rilgan, lekin holat o‘zgarmagan» — "
                "<i>여러 대책에도 불구하고 문제는 <b>여전히</b> 심각하다.</i></p>",
        "examples": [
            ("여러 노력에도 불구하고 상황은 여전히 나아지지 않았다.", "Ko‘p harakatga qaramay vaziyat hamon yaxshilanmadi."),
        ],
        "synonyms": [("아직", "아직 = «hali» (kutilyapti); 여전히 = «hamon o‘sha holatda»")],
    },
    {
        "word": "이미", "pos": "adv", "topic": "time",
        "level": 3, "freq": 3, "order": 821,
        "meaning": "allaqachon, avvaldan",
        "collocation": "이미 알다 · 이미 끝나다",
        "note": "<p><b>벌써</b> = «shu qadar tezmi?» (hayrat); <b>이미</b> = quruq fakt. "
                "Yozma matnda 이미 ishlatiladi.</p>",
        "examples": [
            ("그 소식은 이미 알고 있었다.", "U xabarni allaqachon bilardim."),
        ],
        "synonyms": [("벌써", "벌써 = hayrat ohangi bilan; 이미 = neytral fakt")],
    },
    {
        "word": "드디어", "pos": "adv", "topic": "time",
        "level": 3, "freq": 2, "order": 822,
        "meaning": "nihoyat (kutilgan quvonchli natija)",
        "collocation": "드디어 도착하다 · 드디어 끝났다",
        "examples": [
            ("드디어 방학이 시작됐어요!", "Nihoyat ta’til boshlandi!"),
        ],
        "synonyms": [("마침내", "마침내 = kitobiy, neytral; 드디어 = quvonchli, og‘zaki")],
    },
    {
        "word": "미리", "pos": "adv", "topic": "time",
        "level": 2, "freq": 2, "order": 823,
        "meaning": "oldindan, avvaldan",
        "collocation": "미리 예약하다 · 미리 준비하다 · 미리 알리다",
        "examples": [
            ("표를 미리 예매하는 것이 좋다.", "Chiptani oldindan olib qo‘ygan ma’qul."),
        ],
    },
    {
        "word": "우선", "hanja": "于先", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 2, "order": 824,
        "meaning": "avvalo, birinchi navbatda",
        "collocation": "우선 ~부터 · 우선순위",
        "note": "<p>쓰기 54 da sanashni boshlashda: <i><b>우선</b>, 첫째로 ...</i></p>",
        "examples": [
            ("우선 원인부터 파악해야 한다.", "Avvalo sababni aniqlash kerak."),
        ],
    },

    # ── Taxmin, shart va munosabat ───────────────────────────────────────
    {
        "word": "과연", "hanja": "果然", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 830,
        "meaning": "haqiqatan ham; xo‘sh, rostdanmi? (so‘roqda)",
        "collocation": "과연 ~일까? · 과연 그렇다",
        "note": "<p>Ikki ma’no ohangga bog‘liq: <b>so‘roqda</b> = «rostdan shundaymi?» "
                "(shubha), <b>xabarda</b> = «haqiqatan ham shunday ekan» (tasdiq). "
                "읽기 da muallif shubhasini bildiradi.</p>",
        "examples": [
            ("과연 이 방법이 최선일까?", "Xo‘sh, bu usul haqiqatan eng yaxshisimi?"),
        ],
    },
    {
        "word": "만약", "hanja": "萬若", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 2, "order": 831,
        "meaning": "agar, mabodo (shart bilan juft)",
        "collocation": "만약 ~(으)면 · 만약에",
        "note": "<p>Yolg‘iz kelmaydi — oxirida <b>-(으)면</b> talab qiladi. "
                "Xuddi 비록 → -지만 kabi juft ravish.</p>",
        "examples": [
            ("만약 시간이 있으면 같이 갑시다.", "Agar vaqtingiz bo‘lsa, birga boraylik."),
        ],
    },
    {
        "word": "차라리", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 832,
        "meaning": "yaxshisi, undan ko‘ra (ikkisidan kamrog‘ini tanlash)",
        "collocation": "차라리 ~는 게 낫다 · ~느니 차라리",
        "note": "<p>Ikkala variant ham yomon, lekin ikkinchisi kamroq yomon. "
                "Grammatikada <b>-(으)ㄹ 바에야 / -느니</b> bilan juft keladi.</p>",
        "examples": [
            ("기다리느니 차라리 걸어가겠다.", "Kutgandan ko‘ra yaxshisi piyoda boraman."),
        ],
    },
    {
        "word": "하필", "hanja": "何必", "pos": "adv", "topic": "emotion",
        "level": 5, "freq": 1, "order": 833,
        "meaning": "nima uchun aynan (norozilik ohangi)",
        "collocation": "하필 오늘 · 하필이면",
        "note": "<p>Afsus va norozilik bildiradi: «boshqa payt emas, aynan bugunmi?»</p>",
        "examples": [
            ("하필 시험날에 아팠어요.", "Aynan imtihon kuni kasal bo‘ldim."),
        ],
    },
    {
        "word": "역시", "hanja": "亦是", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 2, "order": 834,
        "meaning": "shunday ekan-da; u ham",
        "collocation": "역시 그렇다 · 나 역시",
        "note": "<p>Ikki ma’no: <b>kutganday chiqdi</b> (역시 맛있네요!) va "
                "<b>«men ham»</b> (저 역시 같은 생각입니다).</p>",
        "examples": [
            ("역시 아프소나가 일등을 했네요.", "O‘ylaganimdek, Afsona birinchi bo‘libdi."),
        ],
    },
    {
        "word": "물론", "hanja": "勿論", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 3, "order": 835,
        "meaning": "albatta, shubhasiz",
        "collocation": "물론이다 · 물론 ~지만",
        "note": "<p><b>쓰기 54 munozara qolipi:</b> "
                "<i><b>물론</b> [반대 의견]도 일리가 있다. <b>그러나</b> ...</i> — "
                "qarshi fikrni tan olib, keyin o‘z fikringizni aytasiz.</p>",
        "examples": [
            ("물론 그 의견도 일리가 있다. 그러나 문제가 있다.", "Albatta o‘sha fikrda ham jon bor. Biroq muammo bor."),
        ],
    },
    {
        "word": "실제로", "hanja": "實際—", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 3, "order": 836,
        "meaning": "aslida, amalda",
        "collocation": "실제로 ~다 · 실제 상황",
        "note": "<p><b>쓰기 54 da dalil keltirishda:</b> "
                "<i><b>실제로</b> 한 조사에 따르면 ...</i></p>",
        "examples": [
            ("실제로 많은 사람들이 이 방법을 사용한다.", "Amalda ko‘p odam bu usuldan foydalanadi."),
        ],
    },
    {
        "word": "아무리", "pos": "adv", "topic": "abstract",
        "level": 3, "freq": 3, "order": 837,
        "meaning": "qanchalik ... bo‘lsa ham (juft ravish)",
        "collocation": "아무리 ~아도 · 아무리 ~더라도",
        "note": "<p>Yolg‘iz kelmaydi — <b>-아도/어도</b> yoki <b>-더라도</b> talab qiladi. "
                "TOPIK 읽기 da doim uchraydi.</p>",
        "examples": [
            ("아무리 바빠도 아침은 먹어야 한다.", "Qanchalik band bo‘lsang ham nonushta qilish kerak."),
        ],
    },
]
