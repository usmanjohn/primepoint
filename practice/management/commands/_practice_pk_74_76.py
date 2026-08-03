# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-74 … PK-76.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
PK-74 mashqida oxirgi savollar 한다체 (문어체) ni ham tekshiradi —
oʻqish matnlari shu darsdan boshlab shu uslubda yoziladi.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_74_76.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "한국어",
    "description": "Koreys tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#d97706",
}

DEFAULTS = {
    "level":                "medium",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# ══════════════════════════════════════════════════════════════════════
# PK-74 — 자마자, 기가 무섭게 (+ 한다체)
# ══════════════════════════════════════════════════════════════════════
Q_PK74 = [
    # 1–5 tanish
    {
        "text": "<p><b>자마자</b> qanday maʼno beradi?</p>",
        "choices": ["…ishi bilanoq", "…ishdan oldin",
                    "…ish oʻrniga", "…ishi uchun"],
        "correct": "…ishi bilanoq",
        "explanation": "<p>Ikki ish orasida deyarli vaqt yoʻq: biri tugadi, "
                       "ikkinchisi allaqachon boshlandi.</p>",
    },
    {
        "text": "<p>자마자 ni qoʻshishda 받침 farqi bormi?</p>",
        "choices": ["Yoʻq — oʻzakka toʻgʻridan toʻgʻri qoʻshiladi",
                    "Ha — 받침 bor boʻlsa 으자마자",
                    "Ha — 받침 yoʻq boʻlsa ㄹ자마자",
                    "Faqat notoʻgʻri feʼllarda bor"],
        "correct": "Yoʻq — oʻzakka toʻgʻridan toʻgʻri qoʻshiladi",
        "explanation": "<p>가자마자, 먹자마자 — ikkalasi ham bir xil. "
                       "Bu 자마자 ning eng qulay tomoni.</p>",
    },
    {
        "text": "<p>자마자 qaysi soʻz turkumi bilan ishlatiladi?</p>",
        "choices": ["Faqat feʼl", "Faqat sifat",
                    "Feʼl va sifat", "Ot bilan ham"],
        "correct": "Faqat feʼl",
        "explanation": "<p>❌ 바쁘자마자, ❌ 학생이자마자 — notoʻgʻri.</p>",
    },
    {
        "text": "<p><b>기가 무섭게</b> ning ohangi qanday?</p>",
        "choices": ["Boʻrttirma — kutilmagan darajada tez",
                    "Betaraf — oddiy ketma-ketlik",
                    "Muloyim iltimos", "Afsuslanish"],
        "correct": "Boʻrttirma — kutilmagan darajada tez",
        "explanation": "<p>Soʻzma-soʻz “…ishdan qoʻrqqandek”. Gapga hayrat "
                       "qoʻshadi va koʻproq yozma matnda uchraydi.</p>",
    },
    {
        "text": "<p><b>한다체</b> qayerda ishlatiladi?</p>",
        "choices": ["Kitob, gazeta, insho va TOPIK 쓰기 da",
                    "Katta yoshdagi odam bilan suhbatda",
                    "Doʻkonda xarid qilganda",
                    "Telefonda salomlashganda"],
        "correct": "Kitob, gazeta, insho va TOPIK 쓰기 da",
        "explanation": "<p>한다체 — <b>qogʻoz uchun</b>, odam uchun emas. "
                       "Odamga 해요체 yoki 합니다체 aytiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 집에 <b>____</b> 손을 씻었어요. (오다)</p>",
        "choices": ["오자마자", "왔자마자", "올자마자", "오는자마자"],
        "correct": "오자마자",
        "explanation": "<p>Oʻzak 오 + 자마자. Zamon oxirgi feʼlda "
                       "(씻었어요).</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 소식을 <b>____</b> 전화했어요. (듣다)</p>",
        "choices": ["듣자마자", "들자마자", "들으자마자", "들었자마자"],
        "correct": "듣자마자",
        "explanation": "<p>ㄷ notoʻgʻri feʼli faqat <b>unli</b> oldida "
                       "ㄹ ga aylanadi. 자마자 undosh bilan boshlanadi — "
                       "shuning uchun 듣 oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 수업이 <b>____</b> 학생들이 나갔어요. (끝나다)</p>",
        "choices": ["끝나자마자", "끝났자마자", "끝날자마자", "끝나기자마자"],
        "correct": "끝나자마자",
        "explanation": "<p>자마자 oldida hech qachon zamon boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 새 표가 <b>____</b> 무섭게 다 팔렸어요. (나오다)</p>",
        "choices": ["나오기가", "나오자", "나온 게", "나올 게"],
        "correct": "나오기가",
        "explanation": "<p>Qolip — feʼl oʻzagi + <b>기가 무섭게</b>.</p>",
    },
    {
        "text": "<p>한다체 ga oʻgiring: 학생들이 책을 <b>읽어요</b>.</p>",
        "choices": ["읽는다", "읽ㄴ다", "읽다", "읽은다"],
        "correct": "읽는다",
        "explanation": "<p>읽 da 받침 bor → <b>는다</b>. 받침 yoʻq boʻlsa "
                       "edi (가다), ㄴ다 boʻlardi: 간다.</p>",
    },
    {
        "text": "<p>한다체 ga oʻgiring: 날씨가 <b>좋아요</b>.</p>",
        "choices": ["좋다", "좋는다", "좋ㄴ다", "좋이다"],
        "correct": "좋다",
        "explanation": "<p>좋다 — <b>sifat</b>. Sifat 한다체 da lugʻat "
                       "shaklida qoladi, hech qachon 는다 olmaydi.</p>",
    },
    {
        "text": "<p>한다체 ga oʻgiring: 교실에 학생이 <b>있어요</b>.</p>",
        "choices": ["있다", "있는다", "있ㄴ다", "있이다"],
        "correct": "있다",
        "explanation": "<p>있다 va 없다 한다체 da <b>oʻzgarmaydi</b>. "
                       "Bu eng koʻp uchraydigan xato.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi jumla <b>tezlikni</b> urgʻulaydi?</p>",
        "choices": ["밥을 먹자마자 잤어요.", "밥을 먹고 잤어요.",
                    "밥을 먹은 후에 잤어요.", "밥을 먹기 전에 잤어요."],
        "correct": "밥을 먹자마자 잤어요.",
        "explanation": "<p>고 va (으)ㄴ 후에 shunchaki tartibni koʻrsatadi. "
                       "자마자 esa <b>orada vaqt yoʻqligini</b> aytadi.</p>",
    },
    {
        "text": "<p>Qaysi jumlada <b>기가 무섭게</b> tabiiy eshitiladi?</p>",
        "choices": ["표가 나오기가 무섭게 다 팔렸어요.",
                    "아침에 일어나기가 무섭게 세수했어요.",
                    "도착하기가 무섭게 전화하세요.",
                    "내일 오기가 무섭게 만날 거예요."],
        "correct": "표가 나오기가 무섭게 다 팔렸어요.",
        "explanation": "<p>기가 무섭게 — <b>hayratlanarli</b> tezlik va "
                       "odatda <b>boʻlib oʻtgan</b> voqea. Buyruq va "
                       "kelasi reja bilan ishlatilmaydi.</p>",
    },
    {
        "text": "<p>“Uyga yetib borishing bilanoq qoʻngʻiroq qil” — qaysi "
                "qolip?</p>",
        "choices": ["도착하자마자", "도착하기가 무섭게",
                    "도착한 후에 무섭게", "도착했자마자"],
        "correct": "도착하자마자",
        "explanation": "<p>Buyruq gapda faqat <b>자마자</b>. 기가 무섭게 "
                       "buyruq bilan ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Hikoya 한다체 da yozilgan. Ichidagi qoʻshtirnoq gap "
                "qaysi uslubda boʻladi?</p>",
        "choices": ["Oʻz uslubida — odamlar baribir 해요체 da gaplashadi",
                    "U ham albatta 한다체 da",
                    "Hamisha 합니다체 da",
                    "Qoʻshtirnoq ichida uslub boʻlmaydi"],
        "correct": "Oʻz uslubida — odamlar baribir 해요체 da gaplashadi",
        "explanation": "<p>Faqat <b>hikoyachi</b> uslubi oʻzgaradi. "
                       "Qahramonlar oʻzaro qanday gaplashsa, shunday "
                       "yoziladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>집에 도착했자마자 비가 왔어요.</s></p>",
        "choices": ["자마자 oldida zamon boʻlmaydi — 도착하자마자",
                    "비가 오다 notoʻgʻri feʼl",
                    "자마자 dan keyin oʻtgan zamon kelmaydi",
                    "집에 emas, 집을 boʻlishi kerak"],
        "correct": "자마자 oldida zamon boʻlmaydi — 도착하자마자",
        "explanation": "<p>Oʻtgan zamon faqat gapning <b>oxirgi</b> "
                       "feʼlida: 왔어요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>교실에 학생이 많이 있는다.</s></p>",
        "choices": ["있다 한다체 da oʻzgarmaydi — 있다",
                    "많이 emas, 많은 boʻlishi kerak",
                    "학생이 emas, 학생을",
                    "교실에 emas, 교실에서"],
        "correct": "있다 한다체 da oʻzgarmaydi — 있다",
        "explanation": "<p>있다/없다 feʼlga oʻxshasa ham 는다 olmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Dars tugashi bilanoq uyga qaytdim” — koreyschada?</p>",
        "choices": ["수업이 끝나자마자 집에 돌아왔어요.",
                    "수업이 끝났자마자 집에 돌아왔어요.",
                    "수업을 끝나자마자 집에 돌아왔어요.",
                    "수업이 끝나기 무섭게 집에 돌아오세요."],
        "correct": "수업이 끝나자마자 집에 돌아왔어요.",
        "explanation": "<p>끝나다 — oʻzlik feʼl, shuning uchun ega "
                       "<b>수업이</b>. 자마자 oldida zamon yoʻq.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring: "
                "저는 매일 아침 여섯 시에 일어나요.</p>",
        "choices": ["나는 매일 아침 여섯 시에 일어난다.",
                    "나는 매일 아침 여섯 시에 일어는다.",
                    "저는 매일 아침 여섯 시에 일어나는다.",
                    "나는 매일 아침 여섯 시에 일어나다."],
        "correct": "나는 매일 아침 여섯 시에 일어난다.",
        "explanation": "<p>일어나 da 받침 yoʻq → <b>ㄴ다</b> → 일어난다. "
                       "한다체 da kamtarona <b>저</b> emas, odatda "
                       "<b>나</b> ishlatiladi.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-75 — 는 길에, 는 김에
# ══════════════════════════════════════════════════════════════════════
Q_PK75 = [
    # 1–5 tanish
    {
        "text": "<p><b>길</b> soʻzining maʼnosi nima?</p>",
        "choices": ["Yoʻl", "Fursat", "Holat", "Qonun"],
        "correct": "Yoʻl",
        "explanation": "<p>Shuning uchun <b>는 길에</b> = “…ayotgan "
                       "yoʻlda”.</p>",
    },
    {
        "text": "<p><b>는 길에</b> qanday feʼllar bilan ishlaydi?</p>",
        "choices": ["Faqat 가다 / 오다 guruhidagi harakat feʼllari",
                    "Har qanday feʼl bilan",
                    "Faqat sifatlar bilan",
                    "Faqat 하다 feʼllari bilan"],
        "correct": "Faqat 가다 / 오다 guruhidagi harakat feʼllari",
        "explanation": "<p>가다, 오다, 출근하다, 퇴근하다, 돌아가다… "
                       "❌ 밥을 먹는 길에 — ovqat yeyish yoʻl emas.</p>",
    },
    {
        "text": "<p><b>는 김에</b> qanday maʼno beradi?</p>",
        "choices": ["Bir yoʻla, shu bahonada",
                    "…ishdan oldin", "…ishi bilanoq", "…gan holicha"],
        "correct": "Bir yoʻla, shu bahonada",
        "explanation": "<p>“Baribir A ni qilyapman — shu bahonada B ni ham "
                       "qilib qoʻyaman.”</p>",
    },
    {
        "text": "<p>는 길에 oldida qanday aniqlovchi turadi?</p>",
        "choices": ["Hamisha 는", "Oʻtgan zamonda (으)ㄴ",
                    "Kelasi zamonda (으)ㄹ", "Aniqlovchi kerak emas"],
        "correct": "Hamisha 는",
        "explanation": "<p>“Ketayotgan” — oʻsha paytdagi holat. "
                       "Zamon oxirgi feʼlda: 어제 가는 길에 만났어요.</p>",
    },
    {
        "text": "<p>김에 dan oldin qachon <b>(으)ㄴ</b> ishlatiladi?</p>",
        "choices": ["Birinchi ish allaqachon tugagan boʻlsa",
                    "Har doim", "Hech qachon",
                    "Faqat 가다 bilan"],
        "correct": "Birinchi ish allaqachon tugagan boʻlsa",
        "explanation": "<p>여기까지 <b>온 김에</b> — kelish tugagan. "
                       "Davom etayotgan boʻlsa: 청소<b>하는 김에</b>.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 학교에 <b>____</b> 길에 자수르 씨를 "
                "만났어요. (가다)</p>",
        "choices": ["가는", "간", "갈", "갔는"],
        "correct": "가는",
        "explanation": "<p>길에 oldida hamisha <b>는</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 여기까지 <b>____</b> 김에 차 한잔 "
                "마시고 가요. (오다)</p>",
        "choices": ["온", "오는", "올", "왔는"],
        "correct": "온",
        "explanation": "<p>Kelish <b>tugagan</b> — oʻtgan aniqlovchi "
                       "<b>(으)ㄴ</b>: 온 김에.</p>",
    },
    {
        "text": "<p>Toʻldiring: 방을 <b>____</b> 김에 창문도 닦았어요. "
                "(청소하다)</p>",
        "choices": ["청소하는", "청소한", "청소할", "청소했는"],
        "correct": "청소하는",
        "explanation": "<p>Tozalash davom etayotgan edi — <b>는 김에</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 퇴근하는 길에 약국에 <b>____</b>. "
                "(들르다 — oʻtgan zamon)</p>",
        "choices": ["들렀어요", "들었어요", "들르었어요", "들러었어요"],
        "correct": "들렀어요",
        "explanation": "<p>들르다 — 으 tushuvchi feʼl (PK-32): "
                       "들르 + 었어요 → <b>들렀어요</b>.</p>",
    },
    {
        "text": "<p>“Bozorga borayotgan ekansiz, non ham olib bering” — "
                "qaysi qolip?</p>",
        "choices": ["시장에 가는 김에", "시장에 가는 길에",
                    "시장에 간 김에", "시장에 갈 겸"],
        "correct": "시장에 가는 김에",
        "explanation": "<p>Non — <b>qoʻshimcha iltimos</b>, shuning uchun "
                       "김에. Yurish davom etayotgani uchun 는.</p>",
    },
    {
        "text": "<p>Toʻldiring: 집에 <b>____</b> 길에 비를 맞았어요. "
                "(오다)</p>",
        "choices": ["오는", "온", "올", "왔던"],
        "correct": "오는",
        "explanation": "<p>Uyga kelayotgan paytda sodir boʻlgan — "
                       "<b>오는 길에</b>.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "퇴근하는 길에 약국에 들렀어요.</p>",
        "choices": ["퇴근하는 길에 약국에 들렀다.",
                    "퇴근한 길에 약국에 들렀다.",
                    "퇴근하는 길에 약국에 들른다.",
                    "퇴근하는 길에 약국에 들렀는다."],
        "correct": "퇴근하는 길에 약국에 들렀다.",
        "explanation": "<p>Oʻtgan zamon 한다체 da <b>았/었다</b>: 들렀다.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>길에 va 김에 orasidagi asosiy farq nima?</p>",
        "choices": ["길에 — tasodif, 김에 — qoʻshimcha qaror",
                    "길에 — kelasi zamon, 김에 — oʻtgan zamon",
                    "길에 — rasmiy, 김에 — ogʻzaki",
                    "Hech qanday farq yoʻq"],
        "correct": "길에 — tasodif, 김에 — qoʻshimcha qaror",
        "explanation": "<p>가는 <b>길에</b> 친구를 만났어요 — tasodifan "
                       "uchratdim. 가는 <b>김에</b> 빵도 샀어요 — "
                       "ataylab qoʻshib oldim.</p>",
    },
    {
        "text": "<p><b>(으)ㄹ 겸</b> (PK-71) va <b>는 김에</b> farqi?</p>",
        "choices": ["겸 — ikki maqsad oldindan rejada; 김에 — ikkinchisi "
                    "yoʻlda paydo boʻldi",
                    "겸 — ogʻzaki; 김에 — yozma",
                    "겸 — faqat oʻtgan zamon; 김에 — hozirgi",
                    "겸 — salbiy; 김에 — ijobiy"],
        "correct": "겸 — ikki maqsad oldindan rejada; 김에 — ikkinchisi "
                   "yoʻlda paydo boʻldi",
        "explanation": "<p>운동도 할 <b>겸</b> 친구도 만날 <b>겸</b> "
                       "공원에 갔어요 (ikkalasi reja) ↔ 공원에 <b>간 김에</b> "
                       "운동도 했어요 (joyida oʻylab qoldim).</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["공부하는 길에 음악을 들었어요.",
                    "학교에 가는 길에 친구를 만났어요.",
                    "퇴근하는 길에 약국에 들렀어요.",
                    "집에 오는 길에 비를 맞았어요."],
        "correct": "공부하는 길에 음악을 들었어요.",
        "explanation": "<p>공부하다 — harakat feʼli emas. "
                       "<b>공부하는 김에</b> yoki <b>공부하면서</b> "
                       "(PK-39) boʻlishi kerak.</p>",
    },
    {
        "text": "<p>“Xonani tozalayotgan ekanman, derazani ham artdim” — "
                "nega bu yerda 길에 boʻlmaydi?</p>",
        "choices": ["Gapda hech qanday yurish yoʻq",
                    "Ikkita ega bor",
                    "Oʻtgan zamon boʻlgani uchun",
                    "Ikkita feʼl bor"],
        "correct": "Gapda hech qanday yurish yoʻq",
        "explanation": "<p>길에 haqiqiy yoʻlni talab qiladi. "
                       "Bu yerda faqat <b>김에</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>학교에 갔는 길에 친구를 만났어요.</s></p>",
        "choices": ["길에 oldida hamisha 는 — 가는 길에",
                    "친구를 emas, 친구가",
                    "학교에 emas, 학교를",
                    "만났어요 emas, 만나요"],
        "correct": "길에 oldida hamisha 는 — 가는 길에",
        "explanation": "<p>Zamon oxirgi feʼlda koʻrsatiladi (만났어요).</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>여기까지 오는 김에 차 한잔 마셔요.</s></p>",
        "choices": ["Kelish tugagan — 온 김에 boʻlishi kerak",
                    "김에 emas, 길에 boʻlishi kerak",
                    "차 한잔 emas, 차를 한잔",
                    "여기까지 emas, 여기에"],
        "correct": "Kelish tugagan — 온 김에 boʻlishi kerak",
        "explanation": "<p>Odam allaqachon yetib kelgan, shuning uchun "
                       "oʻtgan aniqlovchi <b>(으)ㄴ</b>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Ishdan qaytayotib dorixonaga kirdim” — koreyschada?</p>",
        "choices": ["퇴근하는 길에 약국에 들렀어요.",
                    "퇴근한 길에 약국에 들렀어요.",
                    "퇴근하는 김에 약국에 갔어요.",
                    "퇴근하기가 무섭게 약국에 들렀어요."],
        "correct": "퇴근하는 길에 약국에 들렀어요.",
        "explanation": "<p>Yoʻl ustida sodir boʻlgan — <b>는 길에</b>, "
                       "va 들르다 uning tabiiy sherigi.</p>",
    },
    {
        "text": "<p>“Shu yergacha kelgan ekansiz, ovqatlanib keting” — "
                "koreyschada?</p>",
        "choices": ["여기까지 온 김에 식사하고 가세요.",
                    "여기까지 오는 길에 식사하고 가세요.",
                    "여기까지 올 겸 식사하고 가세요.",
                    "여기까지 오자마자 식사하고 가세요."],
        "correct": "여기까지 온 김에 식사하고 가세요.",
        "explanation": "<p>김에 ning eng mashhur ishlatilishi — "
                       "mehmonni taklif qilish.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-76 — 고 나서, (으)ㄴ 채로
# ══════════════════════════════════════════════════════════════════════
Q_PK76 = [
    # 1–5 tanish
    {
        "text": "<p><b>고 나서</b> qanday maʼno beradi?</p>",
        "choices": ["…ib boʻlgach", "…gan holicha",
                    "…ishi bilanoq", "…a turib"],
        "correct": "…ib boʻlgach",
        "explanation": "<p><b>나다</b> — “tugamoq”. Shuning uchun 고 나서 "
                       "birinchi ishning <b>toʻliq tugaganini</b> "
                       "urgʻulaydi.</p>",
    },
    {
        "text": "<p><b>채</b> soʻzining maʼnosi nima?</p>",
        "choices": ["Holat, koʻrinish", "Yoʻl", "Fursat", "Qonun"],
        "correct": "Holat, koʻrinish",
        "explanation": "<p>Shuning uchun <b>(으)ㄴ 채로</b> = "
                       "“…gan holicha”.</p>",
    },
    {
        "text": "<p>채로 oldida qanday aniqlovchi turadi?</p>",
        "choices": ["Oʻtgan aniqlovchi (으)ㄴ", "Hozirgi aniqlovchi 는",
                    "Kelasi aniqlovchi (으)ㄹ", "Aniqlovchi kerak emas"],
        "correct": "Oʻtgan aniqlovchi (으)ㄴ",
        "explanation": "<p>Holat allaqachon vujudga kelgan: "
                       "신은 채로, 켠 채로, 입은 채로.</p>",
    },
    {
        "text": "<p>고 나서 da ikkala gapning egasi qanday boʻlishi kerak?</p>",
        "choices": ["Bir xil", "Har xil", "Farqi yoʻq",
                    "Birinchisi ega boʻlmasligi kerak"],
        "correct": "Bir xil",
        "explanation": "<p>❌ 비가 오고 나서 저는 나갔어요 → bunda "
                       "<b>비가 온 후에</b> (PK-38) kerak.</p>",
    },
    {
        "text": "<p>채로 qanday holatlar haqida gapiradi?</p>",
        "choices": ["Koʻpincha gʻalati, notoʻgʻri yoki kutilmagan holat",
                    "Faqat yoqimli holatlar",
                    "Faqat rasmiy vaziyatlar",
                    "Faqat kelasi zamon holatlari"],
        "correct": "Koʻpincha gʻalati, notoʻgʻri yoki kutilmagan holat",
        "explanation": "<p>Chiroq yoniq uxlash, poyabzalda kirish… "
                       "Shuning uchun 채로 gapga bir tomchi tanqid yoki "
                       "ajablanish qoʻshadi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 밥을 <b>____</b> 나서 약을 먹어요. (먹다)</p>",
        "choices": ["먹고", "먹은", "먹어서", "먹었고"],
        "correct": "먹고",
        "explanation": "<p>Qolip — oʻzak + <b>고 나서</b>. Oldida zamon "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 안경을 <b>____</b> 채로 잤어요. (쓰다)</p>",
        "choices": ["쓴", "쓰는", "쓸", "썼는"],
        "correct": "쓴",
        "explanation": "<p>쓰 da 받침 yoʻq → <b>ㄴ 채로</b> → 쓴 채로.</p>",
    },
    {
        "text": "<p>Toʻldiring: 신발을 <b>____</b> 채로 방에 들어갔어요. "
                "(신다)</p>",
        "choices": ["신은", "신는", "신을", "신었은"],
        "correct": "신은",
        "explanation": "<p>신 da 받침 bor → <b>은 채로</b>. Koreyada bu "
                       "juda qoʻpol xato hisoblanadi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 책을 <b>____</b> 나서 생각이 바뀌었어요. "
                "(읽다)</p>",
        "choices": ["읽고", "읽은", "읽어", "읽었고"],
        "correct": "읽고",
        "explanation": "<p>Kitobni <b>oʻqib boʻlgach</b> — 읽고 나서.</p>",
    },
    {
        "text": "<p>Toʻldiring: 불을 <b>____</b> 채로 잠이 들었어요. (켜다)</p>",
        "choices": ["켠", "켜는", "켤", "켰는"],
        "correct": "켠",
        "explanation": "<p>켜 da 받침 yoʻq → <b>ㄴ 채로</b> → 켠 채로.</p>",
    },
    {
        "text": "<p>“Televizor koʻra turib ovqat yedim” — qaysi qolip?</p>",
        "choices": ["텔레비전을 보면서", "텔레비전을 본 채로",
                    "텔레비전을 보고 나서", "텔레비전을 보자마자"],
        "correct": "텔레비전을 보면서",
        "explanation": "<p>Koʻrish — davom etayotgan <b>harakat</b>, "
                       "shuning uchun (으)면서 (PK-39).</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "불을 켠 채로 잠이 들었어요.</p>",
        "choices": ["불을 켠 채로 잠이 들었다.",
                    "불을 켠 채로 잠이 든다.",
                    "불을 켠 채로 잠이 들었는다.",
                    "불을 켜는 채로 잠이 들었다."],
        "correct": "불을 켠 채로 잠이 들었다.",
        "explanation": "<p>Oʻtgan zamon 한다체 da <b>았/었다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>고</b> va <b>고 나서</b> farqi nima?</p>",
        "choices": ["고 — shunchaki tartib; 고 나서 — tugallik urgʻusi",
                    "고 — oʻtgan zamon; 고 나서 — hozirgi",
                    "고 — sifat bilan; 고 나서 — feʼl bilan",
                    "Farqi yoʻq"],
        "correct": "고 — shunchaki tartib; 고 나서 — tugallik urgʻusi",
        "explanation": "<p>밥을 먹고 나갔어요 (keyin chiqdim) ↔ "
                       "밥을 먹고 나서 나갔어요 (yeb <b>boʻldim</b>, "
                       "keyin chiqdim).</p>",
    },
    {
        "text": "<p><b>(으)면서</b> va <b>(으)ㄴ 채로</b> farqi nima?</p>",
        "choices": ["면서 — ikki harakat davom etadi; 채로 — bir holat + "
                    "bir harakat",
                    "면서 — yozma; 채로 — ogʻzaki",
                    "면서 — bitta ega; 채로 — ikkita ega",
                    "면서 — kelasi zamon; 채로 — oʻtgan"],
        "correct": "면서 — ikki harakat davom etadi; 채로 — bir holat + "
                   "bir harakat",
        "explanation": "<p>Tekshiruv: birinchi feʼlni “hozir qilyapman” "
                       "deb ayta olasizmi? Ha → 면서, yoʻq → 채로.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["음악을 들은 채로 공부했어요.",
                    "신발을 신은 채로 들어갔어요.",
                    "불을 켠 채로 잠이 들었어요.",
                    "코트를 입은 채로 앉았어요."],
        "correct": "음악을 들은 채로 공부했어요.",
        "explanation": "<p>Tinglash — davom etayotgan harakat, holat emas. "
                       "Toʻgʻrisi — <b>들으면서</b>.</p>",
    },
    {
        "text": "<p>Uch qolipni birinchi ishning holatiga qarab joylang. "
                "Qaysi qatordagi tavsif toʻgʻri?</p>",
        "choices": ["고 나서 — izi qolmadi · 채로 — holati turibdi · "
                    "면서 — hali davom etyapti",
                    "고 나서 — hali davom etyapti · 채로 — izi qolmadi · "
                    "면서 — holati turibdi",
                    "고 나서 — holati turibdi · 채로 — hali davom etyapti · "
                    "면서 — izi qolmadi",
                    "Uchalasi ham bir xil maʼno beradi"],
        "correct": "고 나서 — izi qolmadi · 채로 — holati turibdi · "
                   "면서 — hali davom etyapti",
        "explanation": "<p>Uchtasi tugallik darajasi boʻyicha zinapoya "
                       "hosil qiladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>숙제를 했고 나서 잤어요.</s></p>",
        "choices": ["고 나서 oldida zamon boʻlmaydi — 하고 나서",
                    "숙제를 emas, 숙제가",
                    "잤어요 emas, 자었어요",
                    "고 나서 emas, 고 나고"],
        "correct": "고 나서 oldida zamon boʻlmaydi — 하고 나서",
        "explanation": "<p>Zamon faqat oxirgi feʼlda: 잤어요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>신발을 신는 채로 들어갔어요.</s></p>",
        "choices": ["채로 oldida oʻtgan aniqlovchi kerak — 신은 채로",
                    "신발을 emas, 신발이",
                    "들어갔어요 emas, 들어왔어요",
                    "채로 emas, 채에"],
        "correct": "채로 oldida oʻtgan aniqlovchi kerak — 신은 채로",
        "explanation": "<p>Holat allaqachon vujudga kelgan boʻlishi kerak — "
                       "shuning uchun <b>(으)ㄴ</b>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Sport bilan shugʻullanib boʻlgach dush qabul qilaman” — "
                "koreyschada?</p>",
        "choices": ["운동을 하고 나서 샤워를 해요.",
                    "운동을 한 채로 샤워를 해요.",
                    "운동을 했고 나서 샤워를 해요.",
                    "운동을 하면서 샤워를 해요."],
        "correct": "운동을 하고 나서 샤워를 해요.",
        "explanation": "<p>Sport <b>butunlay tugaydi</b>, keyin dush — "
                       "고 나서 ning aniq oʻrni.</p>",
    },
    {
        "text": "<p>“Derazani ochiq qoldirgan holicha tashqariga chiqdim” — "
                "koreyschada?</p>",
        "choices": ["창문을 열어 놓은 채로 외출했어요.",
                    "창문을 여는 채로 외출했어요.",
                    "창문을 열고 나서 외출했어요.",
                    "창문을 열면서 외출했어요."],
        "correct": "창문을 열어 놓은 채로 외출했어요.",
        "explanation": "<p>PK-59 dagi <b>아/어 놓다</b> + <b>(으)ㄴ 채로</b> — "
                       "“ochib qoʻyilgan holat saqlanib turibdi”.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-74 Mashq: 자마자 · 기가 무섭게",
        "description": "20 savol — nol masofali ketma-ketlik, zamon "
                       "qoidasi, 기가 무섭게 ning cheklovlari va "
                       "한다체 (yozma uslub).",
        "tutorial":    "PK-74:",
        "level":       "medium",
        "questions":   Q_PK74,
    },
    {
        "title":       "PK-75 Mashq: 는 길에 · 는 김에",
        "description": "20 savol — 길에 ning harakat feʼli sharti, "
                       "김에 dagi 는/(으)ㄴ tanlovi, tasodif va "
                       "qoʻshimcha qaror farqi, 겸 bilan solishtirish.",
        "tutorial":    "PK-75:",
        "level":       "medium",
        "questions":   Q_PK75,
    },
    {
        "title":       "PK-76 Mashq: 고 나서 · (으)ㄴ 채로",
        "description": "20 savol — tugallik urgʻusi, bitta ega qoidasi, "
                       "채로 ning oʻtgan aniqlovchisi va 면서 dan farqi.",
        "tutorial":    "PK-76:",
        "level":       "medium",
        "questions":   Q_PK76,
    },
]
