# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-53 … PK-55 ((으)ㄹ 줄 알다, 기로 하다, 잖아요).

Kumulyativ qoida: PK-55 gacha oʻrganilgan hamma narsa ochiq.
PK-53 matnida 기로 하다 (54) va 잖아요 (55) hali YOʻQ.
PK-54 matnida 잖아요 hali yoʻq.
Majhul/orttirma nisbat (56, 57), 아/어 버리다 (58), 아/어 놓다 (59),
koʻchirma gap (60–62) — hech qaysisida yoʻq.

Uchta matn bitta ipga bogʻlangan: kimchi darsi PK-53 da rejalanadi,
PK-54 da kelishiladi, PK-55 da esa unutilgani eslatiladi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_53_55.py --author=prime
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
        "title":   "김치를 만들 줄 알아요?",
        "summary": (
            "PK-53 matni. Sujin bilan Dilnoza kim nima qila bilishini "
            "solishtiradi — koʻnikma va imkoniyat farqi matn ichida koʻrinadi."
        ),
        "order":   53,
        "grammar": [
            {
                "pattern":  "동사 + (으)ㄹ 줄 알다 / 모르다",
                "meaning":  "Koʻnikma: “…a bilmoq”. 줄 — “usul” degan ot, "
                            "shuning uchun bu ham aniqlovchi + ot qurilmasi. "
                            "Inkori 안 알다 emas, MODA — 모르다.",
                "examples": ["김치를 만들 줄 알아요?",
                             "저는 수영할 줄 알아요.",
                             "저는 운전할 줄 몰라요."],
            },
            {
                "pattern":  "(으)ㄹ 줄 알다 va (으)ㄹ 수 있다",
                "meaning":  "줄 알다 — oʻrgangan koʻnikma (yoʻqolmaydi). "
                            "수 있다 — hozirgi imkoniyat (vaziyatga qarab "
                            "oʻzgaradi). Oʻzbekcha: “suza bilaman” va "
                            "“suza olaman”.",
                "examples": ["수영할 줄 알아요. 하지만 오늘은 수영할 수 없어요."],
            },
            {
                "pattern":  "(으)ㄹ 줄 알았어요 — notoʻgʻri taxmin",
                "meaning":  "Oʻtgan zamonda bu qolip koʻpincha “shunday deb "
                            "oʻylagandim, lekin unday emas ekan” degan "
                            "maʼnoni beradi.",
                "examples": ["쉬울 줄 알았어요.", "비가 올 줄 알았어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sujin">수진</span> 씨와 <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨가 <span class="cn-word" data-tr="oshxonada">부엌에서</span> 이야기하고 있어요.</p>

<p><strong>수진:</strong> 딜노자 씨, <span class="cn-word" data-tr="kimchi">김치</span>를 <span class="cn-word" data-pos="verb" data-tr="tayyorlashni bilasizmi">만들 줄 알아요</span>?</p>

<p><strong>딜노자:</strong> 아니요, <span class="cn-word" data-pos="verb" data-tr="bilmayman">몰라요</span>. 하지만 <span class="cn-word" data-tr="oʻzbek taomi">우즈베크 음식</span>은 <span class="cn-word" data-pos="verb" data-tr="tayyorlay bilaman">만들 줄 알아요</span>. <span class="cn-word" data-tr="palov">플로프</span>를 <span class="cn-word" data-pos="verb" data-tr="tayyorlayman">만들어요</span>.</p>

<p><strong>수진:</strong> <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span>요? 저는 플로프를 <span class="cn-word" data-pos="verb" data-tr="yeb koʻrmaganman">안 먹어 봤어요</span>. <span class="cn-word" data-pos="adj" data-tr="qiyinmi">어려워요</span>?</p>

<p><strong>딜노자:</strong> 저도 <span class="cn-word" data-pos="adj" data-tr="qiyin boʻladi deb">어려울</span> <span class="cn-word" data-pos="verb" data-tr="oʻylagandim">줄 알았어요</span>. 하지만 <span class="cn-word" data-tr="onam">어머니</span>가 <span class="cn-word" data-pos="verb" data-tr="oʻrgatdi">가르쳐 줬어요</span>. 지금은 <span class="cn-word" data-pos="adj" data-tr="oson">쉬워요</span>.</p>

<p><strong>수진:</strong> 그럼 <span class="cn-word" data-tr="dam olish kunida">주말</span>에 같이 <span class="cn-word" data-pos="verb" data-tr="tayyorlaymizmi">만들어요</span>?</p>

<p><strong>딜노자:</strong> 좋아요! 하지만 이번 주말에는 <span class="cn-word" data-pos="verb" data-tr="qila olmayman">할 수 없어요</span>. <span class="cn-word" data-tr="imtihon">시험</span>이 있어요.</p>

<p><strong>수진:</strong> <span class="cn-word" data-pos="adj" data-tr="hech gap emas">괜찮아요</span>. <span class="cn-word" data-tr="keyingi hafta">다음 주</span>에 <span class="cn-word" data-pos="verb" data-tr="qilaylik">해요</span>. 저는 김치를 만들 줄 알아요. 딜노자 씨는 플로프를 만들 줄 알아요. <span class="cn-word" data-pos="adv" data-tr="birga">같이</span> 하면 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있어요</span>.</p>

<p><strong>딜노자:</strong> <span class="cn-word" data-pos="adj" data-tr="yaxshi fikr">좋은 생각</span>이에요!</p>''',
        "questions": [
            {
                "text": "Dilnoza qaysi taomni tayyorlashni biladi?",
                "choices": [
                    "Kimchini",
                    "Palovni",
                    "Ikkalasini ham",
                    "Hech qaysisini",
                ],
                "answer": 1,
                "explanation": "“김치를 만들 줄 <b>몰라요</b>… 우즈베크 음식은 "
                               "만들 줄 <b>알아요</b>. 플로프를 만들어요” — "
                               "palovni biladi, kimchini bilmaydi.",
            },
            {
                "text": "Nega Dilnoza bu hafta oshxonaga bora olmaydi?",
                "choices": [
                    "Chunki palov tayyorlashni bilmaydi",
                    "Chunki imtihoni bor",
                    "Chunki kasal",
                    "Chunki Sujin band",
                ],
                "answer": 1,
                "explanation": "“이번 주말에는 <b>할 수 없어요</b>. 시험이 "
                               "있어요” — koʻnikma joyida, faqat bu haftalik "
                               "<b>imkoniyat</b> yoʻq. Shuning uchun 줄 모르다 "
                               "emas, 수 없다.",
            },
            {
                "text": "“저도 어려울 줄 알았어요” nima degani?",
                "choices": [
                    "Men ham qiyinligini bilardim",
                    "Men ham qiyin boʻladi deb oʻylagandim (lekin oson ekan)",
                    "Men ham qiyin qila bilaman",
                    "Menga ham qiyin boʻladi",
                ],
                "answer": 1,
                "explanation": "Oʻtgan zamonda <b>줄 알다</b> notoʻgʻri "
                               "taxminni bildiradi. Keyingi jumla buni "
                               "tasdiqlaydi: “지금은 쉬워요”.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "우리 같이 여행하기로 했어요",
        "summary": (
            "PK-54 matni. Bekzod bilan Jasur taʼtil rejasini qatʼiylashtiradi — "
            "niyatdan qarorga oʻtish matn ichida koʻrinadi."
        ),
        "order":   54,
        "grammar": [
            {
                "pattern":  "동사 + 기로 하다",
                "meaning":  "Qaror: “…ishga qaror qildim”. 기 (“-ish”) + 로 "
                            "(“-ga”) + 하다 — oʻzbekcha tuzilish bilan bir xil. "
                            "기 undosh, shuning uchun ayri yoʻq.",
                "examples": ["같이 여행하기로 했어요.",
                             "부산에 가기로 했어요.",
                             "매일 한국어를 공부하기로 했어요."],
            },
            {
                "pattern":  "기로 했어요 va 기로 해요",
                "meaning":  "Oʻtgan zamonda — qabul qilingan qaror "
                            "(“kelishdik”). Hozirgi zamonda — taklif "
                            "(“kelishaylik”).",
                "examples": ["그럼 아침에 만나기로 해요.",
                             "우리는 주말에 가기로 했어요."],
            },
            {
                "pattern":  "Inkor: 기 dan OLDIN",
                "meaning":  "안 마시기로 했어요 — “ichmaslikka qaror qildim”. "
                            "마시기로 안 했어요 esa “qaror qilmadim” degan "
                            "boshqa maʼno. 지 않기로 shakli rasmiyroq.",
                "examples": ["돈을 안 쓰기로 했어요.",
                             "늦지 않기로 했어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Bekzod">베크조드</span> 씨와 <span class="cn-word" data-tr="Jasur">자수르</span> 씨가 <span class="cn-word" data-tr="taʼtil">방학</span> <span class="cn-word" data-tr="reja">계획</span>을 <span class="cn-word" data-pos="verb" data-tr="tuzishyapti">세우고 있어요</span>.</p>

<p><strong>자수르:</strong> 베크조드 씨, 방학에 <span class="cn-word" data-pos="verb" data-tr="qilmoqchisiz">뭐 하려고 해요</span>?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-tr="avvaliga">처음에는</span> 집에 <span class="cn-word" data-pos="verb" data-tr="qolmoqchi edim">있으려고 했어요</span>. 하지만 지금은 <span class="cn-word" data-tr="Pusanga">부산에</span> <span class="cn-word" data-pos="verb" data-tr="borishga qaror qildim">가기로 했어요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="adv" data-tr="yolgʻiz">혼자</span> 가요?</p>

<p><strong>베크조드:</strong> 아니요. <span class="cn-word" data-tr="Hana">하나</span> 씨와 <span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨도 <span class="cn-word" data-pos="verb" data-tr="borishga kelishdi">가기로 했어요</span>. 우리 같이 <span class="cn-word" data-pos="verb" data-tr="sayohat qilishga kelishdik">여행하기로 했어요</span>.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="adj" data-tr="ajoyib">좋아요</span>! 저도 <span class="cn-word" data-pos="verb" data-tr="borsam boʻladimi">가도 돼요</span>?</p>

<p><strong>베크조드:</strong> <span class="cn-word" data-pos="adv" data-tr="albatta">물론</span>이에요. 그런데 <span class="cn-word" data-tr="pul">돈</span>이 <span class="cn-word" data-pos="verb" data-tr="kerak">필요해요</span>. 우리는 <span class="cn-word" data-tr="kafega">카페에</span> <span class="cn-word" data-pos="verb" data-tr="bormaslikka qaror qildik">안 가기로 했어요</span>. 그리고 <span class="cn-word" data-tr="taksi">택시</span>도 <span class="cn-word" data-pos="verb" data-tr="minmaslikka">타지 않기로</span> 했어요.</p>

<p><strong>자수르:</strong> <span class="cn-word" data-pos="verb" data-tr="tushundim">알았어요</span>. 저도 <span class="cn-word" data-pos="adv" data-tr="hozirdan">지금부터</span> 돈을 <span class="cn-word" data-pos="verb" data-tr="yigʻishga qaror qildim">모으기로 했어요</span>.</p>

<p><strong>베크조드:</strong> 그럼 <span class="cn-word" data-tr="keyingi shanba">다음 토요일</span>에 <span class="cn-word" data-tr="chipta">표</span>를 같이 <span class="cn-word" data-pos="verb" data-tr="sotib olishga kelishaylik">사기로 해요</span>.</p>

<p><strong>자수르:</strong> 네! <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> <span class="cn-word" data-pos="verb" data-tr="borgim keladi">가고 싶어요</span>.</p>''',
        "questions": [
            {
                "text": "Bekzodning rejasi qanday oʻzgardi?",
                "choices": [
                    "Avval Pusanga bormoqchi edi, endi uyda qoladi",
                    "Avval uyda qolmoqchi edi, endi Pusanga borishga qaror qildi",
                    "Avval yolgʻiz bormoqchi edi, endi bormaydi",
                    "Rejasi oʻzgarmadi",
                ],
                "answer": 1,
                "explanation": "“처음에는 집에 <b>있으려고 했어요</b>. 하지만 "
                               "지금은 부산에 <b>가기로 했어요</b>” — niyat "
                               "((으)려고) qarorga (기로) aylandi.",
            },
            {
                "text": "Pulni tejash uchun nima qilmaslikka kelishishdi?",
                "choices": [
                    "Kafega bormaslikka va taksi minmaslikka",
                    "Chipta sotib olmaslikka",
                    "Pusanga bormaslikka",
                    "Ovqat yemaslikka",
                ],
                "answer": 0,
                "explanation": "“카페에 <b>안 가기로</b> 했어요… 택시도 "
                               "<b>타지 않기로</b> 했어요” — inkorning ikkala "
                               "shakli ham 기 dan oldin turibdi.",
            },
            {
                "text": "Nega oxirida “사기로 해요” deyilgan, “사기로 했어요” emas?",
                "choices": [
                    "Chunki bu taklif — “kelishaylik”",
                    "Chunki qaror bekor qilindi",
                    "Chunki 사다 notoʻgʻri feʼl",
                    "Ikkalasi ham bir xil",
                ],
                "answer": 0,
                "explanation": "Hozirgi zamonda 기로 하다 <b>taklif</b> "
                               "boʻladi. 기로 했어요 boʻlganda “allaqachon "
                               "kelishdik” degan boʻlardi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "제가 어제 말했잖아요",
        "summary": (
            "PK-55 matni. Sherbek chiptani unutdi — suhbat 잖아요 bilan "
            "toʻlgan, va oxirida uni kimga ishlatmaslik kerakligi ham "
            "koʻrinadi."
        ),
        "order":   55,
        "grammar": [
            {
                "pattern":  "동사/형용사 + 잖아요",
                "meaning":  "Suhbatdosh ALLAQACHON biladigan narsani "
                            "eslatadi — oʻzbekcha “-ku”, “-da”, “axir”. "
                            "Ayri yoʻq, notoʻgʻri oʻzgarish yoʻq: 듣잖아요.",
                "examples": ["제가 어제 말했잖아요.", "비가 오잖아요.",
                             "음식이 맛있잖아요."],
            },
            {
                "pattern":  "Zamon va ot bilan",
                "meaning":  "Zamon 잖아요 dan OLDIN: 말했잖아요. Ot bilan "
                            "(이)잖아요 — undoshdan keyin 이 qoladi "
                            "(일요일이잖아요), unlidan keyin tushadi "
                            "(친구잖아요).",
                "examples": ["오늘 일요일이잖아요.", "그 사람은 제 친구잖아요."],
            },
            {
                "pattern":  "Qachon ishlatmaslik kerak",
                "meaning":  "Suhbatdosh bilmaydigan narsa haqida, katta "
                            "yoshli yoki notanish odam bilan, rasmiy "
                            "vaziyatda — ishlatilmaydi. Ohangi “buni "
                            "bilishingiz kerak edi” degandek chiqadi.",
                "examples": ["Oʻqituvchiga “어렵잖아요” emas, “어려워요”."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨와 <span class="cn-word" data-tr="Hana">하나</span> 씨가 <span class="cn-word" data-tr="bekatda">역에서</span> <span class="cn-word" data-pos="verb" data-tr="uchrashishdi">만났어요</span>.</p>

<p><strong>하나:</strong> 셰르벡 씨, <span class="cn-word" data-tr="chipta">표</span> 샀어요?</p>

<p><strong>셰르벡:</strong> 표요? 저는 <span class="cn-word" data-pos="verb" data-tr="sotib olmadim">안 샀어요</span>.</p>

<p><strong>하나:</strong> 제가 <span class="cn-word" data-tr="kecha">어제</span> <span class="cn-word" data-pos="verb" data-tr="aytdim-ku">말했잖아요</span>! 오늘 <span class="cn-word" data-tr="ertalab">아침</span>에 <span class="cn-word" data-pos="verb" data-tr="sotib olishga kelishgandik">사기로 했잖아요</span>.</p>

<p><strong>셰르벡:</strong> 아! <span class="cn-word" data-pos="verb" data-tr="unutdim">잊었어요</span>. <span class="cn-word" data-pos="verb" data-tr="uzr">미안해요</span>.</p>

<p><strong>하나:</strong> <span class="cn-word" data-pos="adj" data-tr="hech gap emas">괜찮아요</span>. 지금 <span class="cn-word" data-pos="verb" data-tr="sotib olsak boʻladi">살 수 있어요</span>.</p>

<p><strong>셰르벡:</strong> 하지만 <span class="cn-word" data-tr="odamlar">사람</span>이 <span class="cn-word" data-pos="adj" data-tr="koʻp-ku">많잖아요</span>. <span class="cn-word" data-pos="verb" data-tr="kutishimiz kerak">기다려야 해요</span>.</p>

<p><strong>하나:</strong> 오늘 <span class="cn-word" data-tr="yakshanba-ku">일요일이잖아요</span>. 일요일에는 사람이 <span class="cn-word" data-pos="adv" data-tr="doim">항상</span> 많아요.</p>

<p>두 사람이 <span class="cn-word" data-pos="adv" data-tr="uzoq">오래</span> <span class="cn-word" data-pos="verb" data-tr="kutishdi">기다렸어요</span>. 그리고 <span class="cn-word" data-tr="oʻqituvchi">선생님</span>을 <span class="cn-word" data-pos="verb" data-tr="uchratishdi">만났어요</span>.</p>

<p><strong>선생님:</strong> <span class="cn-word" data-tr="anavi yerda">저기</span>에서 <span class="cn-word" data-pos="verb" data-tr="sotib olsangiz boʻladi">살 수 있어요</span>. 사람이 <span class="cn-word" data-pos="adj" data-tr="kam">적어요</span>.</p>

<p><strong>셰르벡:</strong> <span class="cn-word" data-pos="verb" data-tr="rahmat">고맙습니다</span>, 선생님! <span class="cn-word" data-pos="adv" data-tr="haqiqatan">정말</span> <span class="cn-word" data-pos="adj" data-tr="yaxshi">좋아요</span>.</p>

<p><span class="cn-word" data-tr="keyin">나중에</span> 하나 씨가 <span class="cn-word" data-pos="adv" data-tr="jimgina">조용히</span> <span class="cn-word" data-pos="verb" data-tr="dedi">말했어요</span>. “<span class="cn-word" data-tr="oʻqituvchi bilan">선생님하고</span>는 <span class="cn-word" data-tr="qoʻllamang">잖아요를 쓰지 마세요</span>. 그건 <span class="cn-word" data-tr="faqat doʻstlar bilan">친구하고만</span> 써요.”</p>''',
        "questions": [
            {
                "text": "Nega Hana “제가 어제 말했잖아요” dedi?",
                "choices": [
                    "Chunki Sherbek buni bilishi kerak edi",
                    "Chunki Sherbek buni bilmasdi",
                    "Chunki u rasmiy gapiryapti",
                    "Chunki u oʻqituvchi bilan gaplashyapti",
                ],
                "answer": 0,
                "explanation": "잖아요 — <b>eslatma</b> ohangi: “axir kecha "
                               "aytdim-ku”. Sherbek buni eshitgan, faqat "
                               "unutgan.",
            },
            {
                "text": "Nega bekatda odam koʻp edi?",
                "choices": [
                    "Chunki bayram edi",
                    "Chunki yakshanba edi",
                    "Chunki poyezd kechikdi",
                    "Chunki chipta arzon edi",
                ],
                "answer": 1,
                "explanation": "“오늘 <b>일요일이잖아요</b>. 일요일에는 사람이 "
                               "항상 많아요” — yakshanba. Ot undosh bilan "
                               "tugagani uchun 이 saqlangan.",
            },
            {
                "text": "Hana oxirida Sherbekka qanday maslahat berdi?",
                "choices": [
                    "Chiptani oldindan olishni",
                    "Oʻqituvchi bilan 잖아요 ishlatmaslikni",
                    "Yakshanba kuni kelmaslikni",
                    "Uzoq kutmaslikni",
                ],
                "answer": 1,
                "explanation": "“선생님하고는 잖아요를 쓰지 마세요. 그건 "
                               "친구하고만 써요” — 잖아요 ning ohangi katta "
                               "yoshli odamga hurmatsizlik boʻlib eshitiladi.",
            },
        ],
    },
]
