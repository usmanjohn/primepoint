# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-53 … PK-55.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_53_55.py --master=prime \\
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


# =====================================================================
# PK-53 — (으)ㄹ 줄 알다 / 모르다
# =====================================================================

Q_PK53 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 줄 알다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…a bilmoq (koʻnikma)", "…a olmoq (imkoniyat)",
                    "…ishga qaror qilmoq", "…ga oʻxshaydi"],
        "correct": "…a bilmoq (koʻnikma)",
        "explanation": "<p>수영할 줄 알아요 = “suza <strong>bilaman</strong>”. "
                       "Oʻzbek tili ham bu farqni ajratadi.</p>",
    },
    {
        "text": "<p><strong>줄</strong> soʻzi nima degani?</p>",
        "choices": ["Usul, yoʻl", "Vaqt", "Joy", "Narsa"],
        "correct": "Usul, yoʻl",
        "explanation": "<p>수영할 줄 알아요 soʻzma-soʻz “suzish "
                       "<strong>usulini</strong> bilaman”. Yana bir "
                       "aniqlovchi + ot qurilmasi.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning bu qolipdagi shakli qaysi?</p>",
        "choices": ["먹 줄 알아요", "먹을 줄 알아요", "먹는 줄 알아요",
                    "먹기 줄 알아요"],
        "correct": "먹을 줄 알아요",
        "explanation": "<p>먹 da 받침 bor → <strong>을 줄</strong>.</p>",
    },
    {
        "text": "<p>Bu qolipning inkori qanday?</p>",
        "choices": ["안 알다", "모르다", "없다", "못 알다"],
        "correct": "모르다",
        "explanation": "<p>수영할 줄 <strong>몰라요</strong>. PK-47 dagi "
                       "알다/모르다 juftligi bu yerda ham ishlaydi.</p>",
    },
    {
        "text": "<p><strong>비가 올 줄 알았어요</strong> nima degani?</p>",
        "choices": ["Yomgʻir yogʻishini bilardim",
                    "Yomgʻir yogʻadi deb oʻylagandim (lekin yogʻmadi)",
                    "Yomgʻir yogʻa boshladi",
                    "Yomgʻir yogʻishi mumkin"],
        "correct": "Yomgʻir yogʻadi deb oʻylagandim (lekin yogʻmadi)",
        "explanation": "<p>Oʻtgan zamonda 줄 알다 koʻpincha <strong>notoʻgʻri "
                       "taxmin</strong>ni bildiradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 저는 <strong>______</strong> (운전하다) 줄 "
                "알아요.</p>",
        "choices": ["운전할", "운전하는", "운전한", "운전하기"],
        "correct": "운전할",
        "explanation": "<p>하 da 받침 yoʻq → <strong>ㄹ 줄</strong>: 운전할 줄 "
                       "알아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 김치를 <strong>______</strong> (만들다) 줄 "
                "몰라요.</p>",
        "choices": ["만들을", "만들", "만드는", "만든"],
        "correct": "만들",
        "explanation": "<p>ㄹ oʻzak bitta ㄹ boʻlib qoladi: 만들 + ㄹ → "
                       "<strong>만들</strong>. <s>만들을</s> emas.</p>",
    },
    {
        "text": "<p>Toʻldiring: 피아노를 <strong>______</strong> (치다) 줄 "
                "알아요?</p>",
        "choices": ["치를", "칠", "치는", "친"],
        "correct": "칠",
        "explanation": "<p>Oʻzak — 치, unga ㄹ qoʻshiladi: "
                       "<strong>칠 줄 알아요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 한국어를 <strong>______</strong> 줄 "
                "알아요.</p>",
        "choices": ["할", "하는", "한", "하기"],
        "correct": "할",
        "explanation": "<p>한국어를 <strong>할 줄 알아요</strong> — “koreyscha "
                       "gapira bilaman”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시험이 <strong>______</strong> (쉽다) 줄 "
                "알았어요.</p>",
        "choices": ["쉽을", "쉬울", "쉬운", "쉽는"],
        "correct": "쉬울",
        "explanation": "<p>쉽다 — ㅂ notoʻgʻri sifati: 쉬우 + ㄹ → "
                       "<strong>쉬울 줄 알았어요</strong> (“oson boʻladi deb "
                       "oʻylagandim”).</p>",
    },
    {
        "text": "<p>Toʻldiring: 팔이 아파서 오늘은 <strong>______</strong>. "
                "(“suza olmayman”)</p>",
        "choices": ["수영할 줄 몰라요", "수영할 수 없어요",
                    "수영하기로 했어요", "수영하는 것 같아요"],
        "correct": "수영할 수 없어요",
        "explanation": "<p>Koʻnikma joyida, faqat bugungi <strong>sharoit</strong> "
                       "yoʻq → 수 있다/없다.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 자전거를 <strong>______</strong> (타다) 줄 "
                "알아요.</p>",
        "choices": ["탈", "타는", "탄", "타기"],
        "correct": "탈",
        "explanation": "<p>타 da 받침 yoʻq → <strong>탈 줄 알아요</strong> "
                       "(“velosiped minishni bilaman”).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>수영할 줄 알아요</strong> va <strong>수영할 수 "
                "있어요</strong> — farqi nima?</p>",
        "choices": ["Birinchisi koʻnikma, ikkinchisi imkoniyat",
                    "Birinchisi imkoniyat, ikkinchisi koʻnikma",
                    "Farqi yoʻq", "Birinchisi rasmiy"],
        "correct": "Birinchisi koʻnikma, ikkinchisi imkoniyat",
        "explanation": "<p>Oʻzbekcha juftligi aynan shu: “suza "
                       "<strong>bilaman</strong>” va “suza "
                       "<strong>olaman</strong>”.</p>",
    },
    {
        "text": "<p>“Ertaga kela olaman” — qaysi qolip kerak?</p>",
        "choices": ["올 줄 알아요", "올 수 있어요", "오기로 했어요", "올 것 같아요"],
        "correct": "올 수 있어요",
        "explanation": "<p>“Kelish” — oʻrganiladigan koʻnikma emas, sharoit "
                       "masalasi → <strong>수 있다</strong>.</p>",
    },
    {
        "text": "<p>Qaysi feʼl 줄 알다 bilan tabiiy eshitiladi?</p>",
        "choices": ["오다", "가다", "운전하다", "있다"],
        "correct": "운전하다",
        "explanation": "<p>운전, 수영, 피아노, 요리 — bular "
                       "<strong>oʻrganiladigan</strong> koʻnikmalar. Kelish "
                       "yoki borish esa emas.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["수영할 줄 알아요", "수영할 줄 몰라요",
                    "수영할 줄 안 알아요", "수영할 수 있어요"],
        "correct": "수영할 줄 안 알아요",
        "explanation": "<p>Inkori <strong>모르다</strong>: 수영할 줄 "
                       "몰라요.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>김치를 만들을 줄 알아요.</strong></p>",
        "choices": ["만들을 → 만들", "만들을 → 만드는", "만들을 → 만든",
                    "Xato yoʻq"],
        "correct": "만들을 → 만들",
        "explanation": "<p>ㄹ oʻzak bitta ㄹ boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>저는 피아노를 치를 줄 알아요.</strong></p>",
        "choices": ["치를 → 칠", "치를 → 치는", "치를 → 친", "Xato yoʻq"],
        "correct": "치를 → 칠",
        "explanation": "<p>Oʻzak 치, unga ㄹ qoʻshiladi: <strong>칠 줄</strong>. "
                       "를 — bu toʻldiruvchi qoʻshimchasi, bu yerda oʻrinsiz.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Men kimchi tayyorlashni bilmayman” — qaysi biri toʻgʻri?</p>",
        "choices": ["김치를 만들 줄 몰라요", "김치를 만들 줄 안 알아요",
                    "김치를 만들 수 없어요", "김치를 만들기로 안 했어요"],
        "correct": "김치를 만들 줄 몰라요",
        "explanation": "<p>Koʻnikma yoʻqligi → <strong>줄 모르다</strong>.</p>",
    },
    {
        "text": "<p>“Suza bilaman, lekin bugun qoʻlim ogʻrigani uchun suza "
                "olmayman” — qaysi biri toʻgʻri?</p>",
        "choices": ["수영할 수 있어요. 하지만 오늘은 수영할 줄 몰라요",
                    "수영할 줄 알아요. 하지만 오늘은 수영할 수 없어요",
                    "수영할 줄 알아요. 하지만 오늘은 수영할 줄 몰라요",
                    "수영할 수 있어요. 하지만 오늘은 수영할 수 없어요"],
        "correct": "수영할 줄 알아요. 하지만 오늘은 수영할 수 없어요",
        "explanation": "<p>Koʻnikma yoʻqolmaydi (줄 알다), lekin bugungi "
                       "sharoit yoʻq (수 없다). Bu — farqni koʻrsatadigan "
                       "eng yaxshi gap.</p>",
    },
]


# =====================================================================
# PK-54 — 기로 하다
# =====================================================================

Q_PK54 = [
    # 1–5 tanish
    {
        "text": "<p><strong>기로 하다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…ishga qaror qilmoq", "…moqchi boʻlmoq",
                    "…a bilmoq", "…sa ham boʻladi"],
        "correct": "…ishga qaror qilmoq",
        "explanation": "<p>가기로 했어요 — “borishga qaror qildim”. Niyat emas, "
                       "qaror.</p>",
    },
    {
        "text": "<p>Qolip qanday qismlardan iborat?</p>",
        "choices": ["기 + 로 + 하다", "는 + 것 + 하다", "아/어 + 로 + 하다",
                    "(으)ㄹ + 줄 + 하다"],
        "correct": "기 + 로 + 하다",
        "explanation": "<p>기 (“-ish”) + 로 (“-ga”) + 하다 — oʻzbekcha "
                       "“bor<strong>ish</strong><strong>ga</strong> qaror "
                       "qildim” bilan bir xil tuzilish.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning bu qolipdagi shakli qaysi?</p>",
        "choices": ["들기로", "듣기로", "들으기로", "들을기로"],
        "correct": "듣기로",
        "explanation": "<p>기 undosh bilan boshlanadi → 듣 "
                       "<strong>oʻzgarmaydi</strong>.</p>",
    },
    {
        "text": "<p>Nega bu qolip koʻpincha <strong>했어요</strong> shaklida "
                "keladi?</p>",
        "choices": ["Chunki qaror allaqachon qabul qilingan",
                    "Chunki 하다 notoʻgʻri feʼl",
                    "Chunki u faqat oʻtgan zamonda ishlatiladi",
                    "Chunki 기 oʻtgan zamonni bildiradi"],
        "correct": "Chunki qaror allaqachon qabul qilingan",
        "explanation": "<p>Qaror oʻtmishda qilingan, ishning oʻzi esa hali "
                       "bajarilmagan.</p>",
    },
    {
        "text": "<p>Inkor qayerga qoʻyiladi?</p>",
        "choices": ["기 dan oldin", "기 dan keyin", "하다 ga", "Gap boshiga"],
        "correct": "기 dan oldin",
        "explanation": "<p><strong>안 마시기로</strong> 했어요 — “ichmaslikka "
                       "qaror qildim”. 마시기로 안 했어요 esa “qaror qilmadim” "
                       "degan boshqa maʼno.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 내년에 한국에 <strong>______</strong> (가다) "
                "했어요.</p>",
        "choices": ["갈기로", "가기로", "가는 것으로", "간기로"],
        "correct": "가기로",
        "explanation": "<p>Oʻzakka 기로 qoʻshiladi: <strong>가기로 "
                       "했어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 매일 한국 노래를 <strong>______</strong> (듣다) "
                "했어요.</p>",
        "choices": ["들기로", "듣기로", "들으기로", "듣으기로"],
        "correct": "듣기로",
        "explanation": "<p>기 undosh → 듣 oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 저는 커피를 <strong>______</strong> 했어요. "
                "(“ichmaslikka”)</p>",
        "choices": ["마시기로 안", "안 마시기로", "마시지 기로", "마시기 안로"],
        "correct": "안 마시기로",
        "explanation": "<p>Inkor 기 dan oldin: <strong>안 마시기로 "
                       "했어요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그럼 내일 아침에 <strong>______</strong> (만나다) "
                "해요.</p>",
        "choices": ["만나기로", "만날기로", "만나는", "만난기로"],
        "correct": "만나기로",
        "explanation": "<p>Hozirgi zamonda bu qolip <strong>taklif</strong> "
                       "boʻladi: 만나기로 해요 — “uchrashishga kelishaylik”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 담배를 <strong>______</strong> 했어요. "
                "(“chekmaslikka”, rasmiyroq shakl)</p>",
        "choices": ["피우기로 안", "안 피우기로", "피우지 않기로", "피우기 않로"],
        "correct": "피우지 않기로",
        "explanation": "<p>지 않다 (PK-21) shakli ham ishlaydi va biroz "
                       "rasmiyroq eshitiladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 우리는 김치를 같이 <strong>______</strong> "
                "(만들다) 했어요.</p>",
        "choices": ["만들기로", "만드기로", "만들을기로", "만든기로"],
        "correct": "만들기로",
        "explanation": "<p>기 undosh, shuning uchun ㄹ ham tushmaydi: "
                       "<strong>만들기로</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 주말에 같이 영화를 <strong>______</strong> "
                "(보다) 했어요.</p>",
        "choices": ["볼기로", "보기로", "보는기로", "본기로"],
        "correct": "보기로",
        "explanation": "<p>보 + 기로 → <strong>보기로 했어요</strong> "
                       "(“kino koʻrishga kelishdik”).</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>가려고 해요</strong> va <strong>가기로 했어요</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi niyat, ikkinchisi qaror",
                    "Birinchisi qaror, ikkinchisi niyat",
                    "Farqi yoʻq", "Ikkinchisi notoʻgʻri"],
        "correct": "Birinchisi niyat, ikkinchisi qaror",
        "explanation": "<p>(으)려고 하다 — hali oʻzgarishi mumkin. 기로 하다 — "
                       "masala hal.</p>",
    },
    {
        "text": "<p>Qatʼiylik boʻyicha toʻgʻri tartib qaysi (pastdan "
                "yuqoriga)?</p>",
        "choices": ["(으)려고 하다 → (으)ㄹ 거예요 → 기로 하다",
                    "기로 하다 → (으)ㄹ 거예요 → (으)려고 하다",
                    "(으)ㄹ 거예요 → 기로 하다 → (으)려고 하다",
                    "Uchalasi bir xil"],
        "correct": "(으)려고 하다 → (으)ㄹ 거예요 → 기로 하다",
        "explanation": "<p>Niyat &lt; reja &lt; qaror. Oʻzbekchada ham: "
                       "“bormoqchiman” &lt; “boraman” &lt; “borishga qaror "
                       "qildim”.</p>",
    },
    {
        "text": "<p><strong>만나기로 해요</strong> va <strong>만나기로 "
                "했어요</strong> — farqi nima?</p>",
        "choices": ["Birinchisi taklif, ikkinchisi qabul qilingan qaror",
                    "Birinchisi qaror, ikkinchisi taklif",
                    "Birinchisi notoʻgʻri", "Farqi yoʻq"],
        "correct": "Birinchisi taklif, ikkinchisi qabul qilingan qaror",
        "explanation": "<p>기로 해요 — “kelishaylik”. 기로 했어요 — “kelishdik / "
                       "qaror qildik”.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["한국에 가기로 했어요", "한국에 갈기로 했어요",
                    "한국에 가려고 해요", "한국에 갈 거예요"],
        "correct": "한국에 갈기로 했어요",
        "explanation": "<p>Aniqlovchi emas, <strong>기</strong> qoʻshiladi: "
                       "가기로.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>음악을 들기로 했어요.</strong></p>",
        "choices": ["들기로 → 듣기로", "들기로 → 들으기로", "했어요 → 해요",
                    "Xato yoʻq"],
        "correct": "들기로 → 듣기로",
        "explanation": "<p>기 undosh bilan boshlanadi, shuning uchun 듣 "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping (“ichmaslikka qaror qildim” maʼnosida): "
                "<strong>커피를 마시기로 안 했어요.</strong></p>",
        "choices": ["마시기로 안 했어요 → 안 마시기로 했어요",
                    "마시기로 안 했어요 → 마시기로 했어요",
                    "마시기로 안 했어요 → 마실기로 했어요",
                    "Xato yoʻq"],
        "correct": "마시기로 안 했어요 → 안 마시기로 했어요",
        "explanation": "<p>Inkor <strong>기 dan oldin</strong> turadi. "
                       "마시기로 안 했어요 — “qaror qilmadim” degani.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Keyingi yil Koreyaga borishga qaror qildim” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["내년에 한국에 가려고 해요", "내년에 한국에 가기로 했어요",
                    "내년에 한국에 갈 줄 알아요", "내년에 한국에 갈 것 같아요"],
        "correct": "내년에 한국에 가기로 했어요",
        "explanation": "<p>Qaror qilingan → <strong>기로 했어요</strong>.</p>",
    },
    {
        "text": "<p>“Biz dam olish kunida birga kino koʻrishga kelishdik” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["우리는 주말에 같이 영화를 보기로 했어요",
                    "우리는 주말에 같이 영화를 볼기로 했어요",
                    "우리는 주말에 같이 영화를 보려고 했어요",
                    "우리는 주말에 같이 영화를 볼 줄 알았어요"],
        "correct": "우리는 주말에 같이 영화를 보기로 했어요",
        "explanation": "<p>Bir necha odam birga qaror qilsa, oʻzbekchaga "
                       "“kelishdik” deb tarjima qilinadi — shakl oʻsha-oʻsha.</p>",
    },
]


# =====================================================================
# PK-55 — 잖아요
# =====================================================================

Q_PK55 = [
    # 1–5 tanish
    {
        "text": "<p><strong>잖아요</strong> nima maʼnoni beradi?</p>",
        "choices": ["…-ku, …-da (eslatma)", "…ishga qaror qildim",
                    "…a bilmoq", "…ga oʻxshaydi"],
        "correct": "…-ku, …-da (eslatma)",
        "explanation": "<p>Suhbatdosh <strong>allaqachon biladigan</strong> "
                       "narsani eslatadi: 말했잖아요 — “axir aytdim-ku”.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> ning 잖아요 shakli qaysi?</p>",
        "choices": ["먹으잖아요", "먹잖아요", "먹어잖아요", "먹는잖아요"],
        "correct": "먹잖아요",
        "explanation": "<p>Oʻzakka shundoq qoʻshiladi — 받침 ayrisi yoʻq.</p>",
    },
    {
        "text": "<p><strong>듣다</strong> ning 잖아요 shakli qaysi?</p>",
        "choices": ["들잖아요", "듣잖아요", "들으잖아요", "듣으잖아요"],
        "correct": "듣잖아요",
        "explanation": "<p>잖 undosh bilan boshlanadi → 듣 "
                       "<strong>oʻzgarmaydi</strong>.</p>",
    },
    {
        "text": "<p>Ot bilan qanday boʻladi?</p>",
        "choices": ["일요일잖아요", "일요일이잖아요", "일요일는잖아요",
                    "일요일기잖아요"],
        "correct": "일요일이잖아요",
        "explanation": "<p>Ot bilan <strong>이</strong> qoʻshiladi: "
                       "일요일이잖아요.</p>",
    },
    {
        "text": "<p>잖아요 ni qachon <em>ishlatmaslik</em> kerak?</p>",
        "choices": ["Tengdoshlar bilan", "Suhbatdosh bilmaydigan narsa haqida",
                    "Oʻtgan zamonda", "Savol berganda"],
        "correct": "Suhbatdosh bilmaydigan narsa haqida",
        "explanation": "<p>Ohangi “buni bilishingiz kerak edi” degandek "
                       "chiqadi. Katta yoshli, notanish odam bilan va rasmiy "
                       "vaziyatda ham ishlatilmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 제가 어제 <strong>______</strong> 잖아요. "
                "(말하다, oʻtgan zamon)</p>",
        "choices": ["말하", "말했", "말한", "말하는"],
        "correct": "말했",
        "explanation": "<p>Zamon <strong>잖아요 dan oldin</strong> qoʻyiladi: "
                       "말했잖아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 오늘 <strong>______</strong> 잖아요. 학교에 안 "
                "가요. (일요일)</p>",
        "choices": ["일요일", "일요일이", "일요일은", "일요일에"],
        "correct": "일요일이",
        "explanation": "<p>Ot bilan 이 qoʻshiladi: "
                       "<strong>일요일이잖아요</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: — 왜 우산을 가져왔어요? — 비가 "
                "<strong>______</strong>.</p>",
        "choices": ["오잖아요", "왔잖아요", "오는잖아요", "올잖아요"],
        "correct": "오잖아요",
        "explanation": "<p>Hozir yogʻayotgan boʻlsa — <strong>오잖아요</strong> "
                       "(“axir yomgʻir yogʻyapti-ku”).</p>",
    },
    {
        "text": "<p>Toʻldiring: 날씨가 <strong>______</strong> (덥다) 잖아요. "
                "창문을 열어요.</p>",
        "choices": ["더우", "덥", "더워", "덥으"],
        "correct": "덥",
        "explanation": "<p>잖 undosh → ㅂ notoʻgʻri sifati "
                       "<strong>oʻzgarmaydi</strong>: 덥잖아요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 식당은 비싸요. — 하지만 음식이 "
                "<strong>______</strong>.</p>",
        "choices": ["맛있잖아요", "맛있으잖아요", "맛있는잖아요", "맛있어잖아요"],
        "correct": "맛있잖아요",
        "explanation": "<p>Yumshoq eʼtiroz: “lekin ovqati mazali-ku”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 같이 <strong>______</strong> (가다, oʻtgan "
                "zamon) 잖아요.</p>",
        "choices": ["가", "갔", "간", "가는"],
        "correct": "갔",
        "explanation": "<p>갔잖아요 — “axir kecha birga bordik-ku”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그 사람은 제 <strong>______</strong> "
                "(친구) 잖아요.</p>",
        "choices": ["친구이", "친구", "친구는", "친구가"],
        "correct": "친구",
        "explanation": "<p>친구 unli bilan tugaydi, shuning uchun 이 "
                       "<strong>tushadi</strong>: 친구잖아요. Undosh bilan "
                       "tugasa esa qoladi: 학생<strong>이</strong>잖아요, "
                       "일요일<strong>이</strong>잖아요. Bu — 이에요/예요 "
                       "dagi qoidaning oʻzi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><strong>비가 와요</strong> va <strong>비가 오잖아요</strong> — "
                "farqi nima?</p>",
        "choices": ["Birinchisi yangi maʼlumot, ikkinchisi eslatma",
                    "Birinchisi eslatma, ikkinchisi yangi maʼlumot",
                    "Birinchisi rasmiy", "Farqi yoʻq"],
        "correct": "Birinchisi yangi maʼlumot, ikkinchisi eslatma",
        "explanation": "<p>오잖아요 — “axir yomgʻir yogʻyapti-ku”, yaʼni "
                       "suhbatdosh buni koʻrib turibdi.</p>",
    },
    {
        "text": "<p>Qaysi vaziyatda 잖아요 <em>notoʻgʻri</em>?</p>",
        "choices": ["Doʻstingizga kechagi gapni eslatganda",
                    "Yangi tanishgan odamga ismingizni aytganda",
                    "Doʻstingizga sababni tushuntirganda",
                    "Tengdoshingizga yumshoq eʼtiroz bildirganda"],
        "correct": "Yangi tanishgan odamga ismingizni aytganda",
        "explanation": "<p>U ismingizni <strong>bilmaydi</strong> — 잖아요 esa "
                       "“buni bilasiz-ku” degan maʼno beradi.</p>",
    },
    {
        "text": "<p>Oʻqituvchingizga 잖아요 bilan gapirsa boʻladimi?</p>",
        "choices": ["Ha, bemalol", "Yoʻq — hurmatsizlik boʻlib eshitiladi",
                    "Faqat savolda", "Faqat oʻtgan zamonda"],
        "correct": "Yoʻq — hurmatsizlik boʻlib eshitiladi",
        "explanation": "<p>Oʻzbekchada ham oʻqituvchiga “aytdim-ku!” "
                       "demaysiz — xuddi shu tuygʻu.</p>",
    },
    {
        "text": "<p>잖아요 ning uchta vazifasi qaysi?</p>",
        "choices": ["Eslatish · sababni koʻrsatish · yumshoq eʼtiroz",
                    "Buyruq · taklif · savol",
                    "Oʻtgan · hozirgi · kelasi zamon",
                    "Ruxsat · taqiq · majburiyat"],
        "correct": "Eslatish · sababni koʻrsatish · yumshoq eʼtiroz",
        "explanation": "<p>Uchalasida ham asosda bitta fikr: “buni siz "
                       "allaqachon bilasiz”.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>음악을 들잖아요.</strong></p>",
        "choices": ["들잖아요 → 듣잖아요", "들잖아요 → 들으잖아요",
                    "들잖아요 → 듣으잖아요", "Xato yoʻq"],
        "correct": "들잖아요 → 듣잖아요",
        "explanation": "<p>잖 undosh bilan boshlanadi → ㄷ oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>말하잖았어요.</strong></p>",
        "choices": ["말하잖았어요 → 말했잖아요", "말하잖았어요 → 말하잖아요",
                    "말하잖았어요 → 말한잖아요", "Xato yoʻq"],
        "correct": "말하잖았어요 → 말했잖아요",
        "explanation": "<p>Zamon <strong>잖아요 dan oldin</strong> qoʻyiladi, "
                       "keyin emas.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Axir bugun yakshanba-ku” — qaysi biri toʻgʻri?</p>",
        "choices": ["오늘 일요일잖아요", "오늘 일요일이잖아요",
                    "오늘 일요일이에요잖아요", "오늘 일요일은잖아요"],
        "correct": "오늘 일요일이잖아요",
        "explanation": "<p>Ot bilan 이 qoʻshiladi.</p>",
    },
    {
        "text": "<p>— 왜 안 갔어요? — “Axir yomgʻir yogʻdi-ku.” Qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["비가 왔잖아요", "비가 오잖았어요", "비가 오잖아요",
                    "비가 올잖아요"],
        "correct": "비가 왔잖아요",
        "explanation": "<p>Oʻtgan zamon 잖아요 dan oldin: "
                       "<strong>왔잖아요</strong>.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-53 Mashq: (으)ㄹ 줄 알다 / 모르다",
        "description": "20 savol — koʻnikma va imkoniyat farqi, ㄹ oʻzaklar, "
                       "모르다 inkori va “oʻylagandim” maʼnosi.",
        "tutorial":    "PK-53:",
        "level":       "medium",
        "questions":   Q_PK53,
    },
    {
        "title":       "PK-54 Mashq: 기로 하다 — qaror va vaʼda",
        "description": "20 savol — yasalishi, inkorning oʻrni, taklif shakli "
                       "va qatʼiylik darajalari.",
        "tutorial":    "PK-54:",
        "level":       "medium",
        "questions":   Q_PK54,
    },
    {
        "title":       "PK-55 Mashq: 잖아요 — “axir bilasiz-ku”",
        "description": "20 savol — yasalishi, zamonning oʻrni, uch vazifasi "
                       "va qachon ishlatmaslik kerakligi.",
        "tutorial":    "PK-55:",
        "level":       "medium",
        "questions":   Q_PK55,
    },
]
