# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-98 … PK-100. KURS TUGADI (100 ta mashq).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
PK-100 mashqi — kursning yakuniy testi. U yangi qolip soʻramaydi:
har bir savol biror jumlani tahlil qilishni yoki qoliplarni
bir-biridan ajratishni talab qiladi. Shuning uchun uning savollari
butun kurs boʻylab (PK-12 dan PK-99 gacha) tarqalgan.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_98_100.py --master=prime \\
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
# PK-98 — 거늘 · 기로서니
# ══════════════════════════════════════════════════════════════════════
Q_PK98 = [
    # 1–5 tanish
    {
        "text": "<p><b>-거늘</b> qaysi uslubga tegishli?</p>",
        "choices": ["Kundalik ogʻzaki nutq",
                    "Adabiy va maqol tili",
                    "Rasmiy hujjat tili",
                    "Bolalar tili"],
        "correct": "Adabiy va maqol tili",
        "explanation": "<p>거늘 maqollarda, klassik matnlarda va eski "
                       "xatlarda yashaydi. Bugungi kunda u "
                       "<b>gapirilmaydi</b> — faqat oʻqiladi.</p>",
    },
    {
        "text": "<p><b>하물며</b> nima degani?</p>",
        "choices": ["shuning uchun", "qolaversa, u yoqda tursin",
                    "afsuski", "birdaniga"],
        "correct": "qolaversa, u yoqda tursin",
        "explanation": "<p>하물며 — 거늘 ning doimiy jufti: "
                       "<b>짐승도 은혜를 알거늘, 하물며 사람이랴.</b></p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>짐승도 은혜를 ___, 하물며 사람이랴.</b> (알다)</p>",
        "choices": ["알거늘", "알기로서니", "알더라도", "안다니"],
        "correct": "알거늘",
        "explanation": "<p>Maqol qolipi: <b>…거늘, 하물며 …(이)랴</b>. "
                       "Pastdan yuqoriga qarab dalil keltiriladi.</p>",
    },
    {
        "text": "<p><b>기로서니</b> dan oldin deyarli doim qaysi soʻz "
                "turadi?</p>",
        "choices": ["하물며", "아무리", "그러나", "차라리"],
        "correct": "아무리",
        "explanation": "<p><b>아무리 바쁘기로서니 밥은 먹어야지.</b> "
                       "아무리 siz bu qolip toʻliq eshitilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>아무리 ___ 밥은 먹어야지.</b> (바쁘다)</p>",
        "choices": ["바쁘거늘", "바쁘기로서니", "바쁘답시고", "바쁘려니"],
        "correct": "바쁘기로서니",
        "explanation": "<p>Yon berish + <b>taʼna</b> → 기로서니. "
                       "Ketidan 먹어야지 — tanbeh.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p><b>기로서니</b> dan keyin qanday gap keladi?</p>",
        "choices": ["Oddiy xabar",
                    "Tanbeh: 아/어야지 · (으)면 안 된다 · 어떻게 …?",
                    "Savol soʻzi",
                    "Koʻchirma gap"],
        "correct": "Tanbeh: 아/어야지 · (으)면 안 된다 · 어떻게 …?",
        "explanation": "<p>Gapiruvchi sababni qabul qiladi, lekin "
                       "<b>natijani qabul qilmaydi</b>. Mana shu — "
                       "taʼnaning oʻzi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>아무리 화가 나기로서니 그런 말을 ___.</b></p>",
        "choices": ["했다", "하면 안 된다", "할 것이다", "하고 있다"],
        "correct": "하면 안 된다",
        "explanation": "<p>기로서니 ketidan tanbeh kerak. "
                       "<b>(으)면 안 되다</b> (PK-51) — eng tipik "
                       "davomi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>작은 씨앗도 자라거늘, 하물며 ___.</b></p>",
        "choices": ["사람이다", "사람이랴", "사람이니까", "사람이면"],
        "correct": "사람이랴",
        "explanation": "<p><b>(이)랴</b> — javobsiz savol. Xulosa "
                       "ataylab aytilmaydi; savolning oʻzi xulosa.</p>",
    },
    {
        "text": "<p><b>기로서니</b> ning qisqargan shakli qaysi?</p>",
        "choices": ["기로", "기에", "거늘", "기는"],
        "correct": "기로",
        "explanation": "<p><b>아무리 바쁘기로</b> — maʼno oʻzgarmaydi, "
                       "faqat qisqaroq.</p>",
    },
    {
        "text": "<p>Ot bilan qanday shakl olinadi?</p>"
                "<p><b>아무리 아이 + 기로서니</b></p>",
        "choices": ["아이기로서니", "아이이기로서니",
                    "아이라기로서니", "아이거늘"],
        "correct": "아이기로서니",
        "explanation": "<p><b>아무리 아이기로서니 그런 행동은 안 된다</b> "
                       "— “bola boʻlsa ham”.</p>",
    },
    {
        "text": "<p><b>거늘</b> ning ishlaridan qaysi biri "
                "<b>notoʻgʻri</b> koʻrsatilgan?</p>",
        "choices": ["Asos berish — “shunday ekan…”",
                    "Qarama-qarshilik — “shunday boʻlsa-da…”",
                    "Gapiruvchining ichki hukmi bor",
                    "Kelasi zamon rejasini bildirish"],
        "correct": "Kelasi zamon rejasini bildirish",
        "explanation": "<p>거늘 reja bildirmaydi. Uning ichida hamisha "
                       "“bu — maʼlum haqiqat, sen esa boshqacha "
                       "qilyapsan” degan hukm bor.</p>",
    },
    {
        "text": "<p>TOPIK 쓰기 da bu ikki qolipni ishlatish tavsiya "
                "qilinadimi?</p>",
        "choices": ["Ha, ikkalasini ham",
                    "Yoʻq — ular imtihon uslubiga mos emas; ularning "
                    "vazifasi oʻqishda tanib olish",
                    "Faqat 기로서니 ni",
                    "Faqat sarlavhada"],
        "correct": "Yoʻq — ular imtihon uslubiga mos emas; ularning "
                   "vazifasi oʻqishda tanib olish",
        "explanation": "<p>Yozma ishda <b>더라도 · (으)ㄹ지라도 · "
                       "(으)ㅁ에도 불구하고</b> (PK-81) ishlating.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이 문제는 ___ 다시 풀겠습니다.</b> (어렵다)</p>",
        "choices": ["어렵거늘", "어렵더라도", "어렵기로서니", "어렵답시고"],
        "correct": "어렵더라도",
        "explanation": "<p>Oddiy rasmiy gap → <b>더라도</b> (PK-81). "
                       "거늘 adabiy, 기로서니 esa taʼna olib "
                       "keladi.</p>",
    },
    {
        "text": "<p>더라도 da yoʻq boʻlgan, lekin 기로서니 da bor "
                "boʻlgan narsa nima?</p>",
        "choices": ["Oʻtgan zamon", "Taʼna", "Savol", "Hurmat"],
        "correct": "Taʼna",
        "explanation": "<p>더라도 neytral. <b>기로서니</b> — yon berish "
                       "+ taʼna, <b>거늘</b> — yon berish + hukm.</p>",
    },
    {
        "text": "<p>Yon berish zinapoyasida eng adabiy shakl qaysi?</p>",
        "choices": ["아/어도", "더라도", "(으)ㅁ에도 불구하고", "거늘"],
        "correct": "거늘",
        "explanation": "<p>아/어도 (51) → 더라도 (81) → (으)ㄹ지라도 (81) "
                       "→ (으)ㅁ에도 불구하고 (81) → 기로서니 (98) → "
                       "<b>거늘</b> (98).</p>",
    },
    {
        "text": "<p>Oʻzbekchada bu ikki qolipning eng yaqin juftligi "
                "qaysi?</p>",
        "choices": ["“… tufayli”",
                    "“-ku”, “qanchalik … boʻlmasin”",
                    "“… hisob”",
                    "“goʻyo … deb”"],
        "correct": "“-ku”, “qanchalik … boʻlmasin”",
        "explanation": "<p>Oʻzbekcha <b>-ku</b> ning ichida ham taʼna, "
                       "hayrat va “buni oʻzing bilishing kerak edi” "
                       "degan maʼno bor — aynan shu ish.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["아무리 바쁘기로서니 밥은 먹어야지.",
                    "바쁘기로서니 밥은 먹어야지.",
                    "아무리 화가 나기로서니 그런 말을 하면 안 된다.",
                    "짐승도 은혜를 알거늘, 하물며 사람이랴."],
        "correct": "바쁘기로서니 밥은 먹어야지.",
        "explanation": "<p><b>아무리</b> tushib qolgan — u qolipning "
                       "bir qismi kabi ishlaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["아무리 바쁘기로서니 집에 갔다.",
                    "짐승도 은혜를 알거늘 사람도 안다.",
                    "아무리 아이기로서니 그런 행동은 안 된다.",
                    "이 문제는 어렵거늘 다시 풀겠습니다."],
        "correct": "아무리 아이기로서니 그런 행동은 안 된다.",
        "explanation": "<p>아무리 bor, ketidan tanbeh bor. Qolganlarida: "
                       "tanbeh oʻrniga oddiy xabar, xulosa ochiq "
                       "aytilgan (거늘 kuchini yoʻqotgan) va adabiy "
                       "qolip oddiy gapga qoʻyilgan.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylang.</p>"
                "<p><b>하물며 사람이랴 / 알거늘 / 짐승도 / 은혜를</b></p>",
        "choices": ["짐승도 은혜를 알거늘, 하물며 사람이랴.",
                    "하물며 사람이랴, 짐승도 은혜를 알거늘.",
                    "은혜를 짐승도 알거늘 하물며 사람이랴.",
                    "짐승도 알거늘 은혜를 하물며 사람이랴."],
        "correct": "짐승도 은혜를 알거늘, 하물며 사람이랴.",
        "explanation": "<p>Avval past narsa haqidagi dalil (짐승도 … "
                       "알거늘), keyin javobsiz savol (하물며 "
                       "사람이랴).</p>",
    },
    {
        "text": "<p>Oʻzbekchaga toʻgʻri oʻgirilgan variantni tanlang.</p>"
                "<p><b>아무리 화가 나기로서니 그런 말을 하면 안 된다.</b></p>",
        "choices": ["Jahlingiz chiqqani uchun bunday gapirdingiz.",
                    "Qanchalik jahlingiz chiqmasin, bunday gap aytish "
                    "mumkin emas.",
                    "Jahlingiz chiqsa, bunday gapirishingiz mumkin.",
                    "Jahlingiz chiqqanini bilaman."],
        "correct": "Qanchalik jahlingiz chiqmasin, bunday gap aytish "
                   "mumkin emas.",
        "explanation": "<p>기로서니 sababni qabul qiladi (“jahling "
                       "chiqqan — tushunaman”), lekin natijani "
                       "qabul qilmaydi.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-99 — 사자성어 va idiomalar
# ══════════════════════════════════════════════════════════════════════
Q_PK99 = [
    # 1–5 tanish
    {
        "text": "<p><b>사자성어</b> nima?</p>",
        "choices": ["Toʻrt ieroglifdan iborat tayyor ibora",
                    "Toʻrt qatorli sheʼr",
                    "Toʻrtta soʻzli maqol",
                    "Toʻrtinchi daraja grammatikasi"],
        "correct": "Toʻrt ieroglifdan iborat tayyor ibora",
        "explanation": "<p>四字成語 — har bir ieroglif bitta soʻz, "
                       "toʻrttasi birgalikda bitta hikmat.</p>",
    },
    {
        "text": "<p><b>고진감래</b> nimani anglatadi?</p>",
        "choices": ["Tayyorgarlik boʻlsa, tashvish yoʻq",
                    "Mashaqqatdan keyin rohat",
                    "Bir oʻq bilan ikki quyon",
                    "Qaror uch kun turadi"],
        "correct": "Mashaqqatdan keyin rohat",
        "explanation": "<p>苦(achchiq) 盡(tugamoq) 甘(shirin) 來(kelmoq). "
                       "Oʻzbekcha juftligi: “<b>Sabrning tagi sariq "
                       "oltin</b>”.</p>",
    },
    {
        "text": "<p><b>새옹지마</b> nimani anglatadi?</p>",
        "choices": ["Yaxshi va yomon almashadi, oxirini hech kim bilmaydi",
                    "Koʻp boʻlgani yaxshi",
                    "Hoʻkiz qulogʻiga kitob oʻqigan bilan",
                    "Oltinga zar qoʻshgandek"],
        "correct": "Yaxshi va yomon almashadi, oxirini hech kim bilmaydi",
        "explanation": "<p>Oʻzbekcha juftligi: “<b>Har balo bir "
                       "savob</b>”. Bu ibora chol va uning oti "
                       "haqidagi masaldan kelgan.</p>",
    },
    {
        "text": "<p><b>작심삼일</b> nimani anglatadi?</p>",
        "choices": ["Uch kun ishlash", "Qaror uch kun turadi",
                    "Uchinchi kun eng qiyin", "Uch marta urinish"],
        "correct": "Qaror uch kun turadi",
        "explanation": "<p>Oʻzbekcha: “<b>Tavbasi uch kunlik</b>”. "
                       "Yangi yil qarorlari haqida gapirganda eng koʻp "
                       "ishlatiladigan ibora.</p>",
    },
    {
        "text": "<p><b>귀가 얇다</b> — soʻzma-soʻz va aslida nima "
                "degani?</p>",
        "choices": ["“qulogʻi yupqa” — tez ishonadi",
                    "“qulogʻi yupqa” — yaxshi eshitmaydi",
                    "“qulogʻi keng” — koʻp eshitadi",
                    "“qulogʻi ogʻir” — sir saqlaydi"],
        "correct": "“qulogʻi yupqa” — tez ishonadi",
        "explanation": "<p>Tasvir juda aniq: yupqa quloq har gapni "
                       "oʻtkazib yuboradi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>우리 형은 ___ 모르는 사람이 없다.</b></p>",
        "choices": ["발이 커서", "발이 넓어서", "눈이 높아서", "입이 무거워서"],
        "correct": "발이 넓어서",
        "explanation": "<p><b>발이 넓다</b> — tanish-bilishi koʻp. "
                       "발이 <b>크다</b> esa oyoqning haqiqiy "
                       "oʻlchami.</p>",
    },
    {
        "text": "<p><b>입이 무겁다</b> nima degani?</p>",
        "choices": ["Kam gapiradi", "Sir saqlaydi",
                    "Koʻp yeydi", "Qattiq gapiradi"],
        "correct": "Sir saqlaydi",
        "explanation": "<p>Oʻzbekchada ham aynan bor: "
                       "“<b>ogʻzi mahkam</b>”.</p>",
    },
    {
        "text": "<p><b>한 우물을 파다</b> nima degani?</p>",
        "choices": ["Quduq qazish kasbi",
                    "Bir ishga umr bermoq, bitta yoʻlda qatʼiy turmoq",
                    "Yolgʻiz ishlamoq",
                    "Chuqur oʻylamoq"],
        "correct": "Bir ishga umr bermoq, bitta yoʻlda qatʼiy turmoq",
        "explanation": "<p>“Bitta quduq qazimoq” — bir necha joyni "
                       "kovlab yurmaslik.</p>",
    },
    {
        "text": "<p>Iborani inshoga kiritishning tayyor qolipi qaysi?</p>",
        "choices": ["…(이)라는 말이 있다",
                    "…(으)로 인해",
                    "…기 짝이 없다",
                    "…(느)ㄴ답시고"],
        "correct": "…(이)라는 말이 있다",
        "explanation": "<p><b>고진감래라는 말이 있다.</b> Yoki "
                       "<b>…(이)라고 할 수 있다</b>. Keyin maʼnosini "
                       "bir jumlada oching.</p>",
    },
    {
        "text": "<p>Bitta inshoda nechta 사자성어 ishlatiladi?</p>",
        "choices": ["Kamida uchta", "Bittasi", "Har bandda bittadan",
                    "Qanchasi esga tushsa"],
        "correct": "Bittasi",
        "explanation": "<p>Uchta ibora bilimni emas, "
                       "<b>ishonchsizlikni</b> koʻrsatadi. Bitta ibora, "
                       "toʻgʻri joyda — bu kuch.</p>",
    },
    {
        "text": "<p>Iborani qaysi joyga qoʻyish eng kuchli?</p>",
        "choices": ["Birinchi jumlaga", "Sarlavhaga",
                    "Xulosa bandiga", "Har bandning boshiga"],
        "correct": "Xulosa bandiga",
        "explanation": "<p>Eng kuchli oʻrni — oxirgi banddagi "
                       "umumlashtirish. Bu — TOPIK 쓰기 54 ning ideal "
                       "yakuni.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>준비한 사람만이 기회를 잡는다. ___이라는 말이 있다.</b></p>",
        "choices": ["작심삼일", "유비무환", "우이독경", "다다익선"],
        "correct": "유비무환",
        "explanation": "<p><b>유비무환</b> — tayyorgarlik boʻlsa, "
                       "tashvish yoʻq. Jumla bilan ibora bir xil fikrni "
                       "aytmoqda.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi ibora “Bir oʻq bilan ikki quyon” ga toʻgʻri "
                "keladi?</p>",
        "choices": ["일석이조", "십시일반", "금상첨화", "인과응보"],
        "correct": "일석이조",
        "explanation": "<p>一石二鳥 — “bitta tosh, ikkita qush”. "
                       "Oʻzbekchada quyon, koreyschada qush — tasvir "
                       "bir xil.</p>",
    },
    {
        "text": "<p>Qaysi ibora “Nima eksang, shuni oʻrasan” ga toʻgʻri "
                "keladi?</p>",
        "choices": ["다다익선", "새옹지마", "인과응보", "고진감래"],
        "correct": "인과응보",
        "explanation": "<p>因果應報 — har ish oʻz javobini oladi.</p>",
    },
    {
        "text": "<p><b>발이 크다</b> va <b>발이 넓다</b> farqi nima?</p>",
        "choices": ["Farqi yoʻq",
                    "크다 — oyoqning haqiqiy oʻlchami · 넓다 — "
                    "tanish-bilishi koʻp",
                    "크다 — tanishi koʻp · 넓다 — oyoq oʻlchami",
                    "Ikkalasi ham idioma"],
        "correct": "크다 — oyoqning haqiqiy oʻlchami · 넓다 — "
                   "tanish-bilishi koʻp",
        "explanation": "<p>Idiomada sifatni almashtirib boʻlmaydi — u "
                       "butun bir birikma.</p>",
    },
    {
        "text": "<p>Doʻstingizga gapiryapsiz. Qaysi biri tabiiy?</p>",
        "choices": ["야, 너 진짜 발이 넓다!",
                    "야, 너 진짜 발이 넓기 짝이 없다!",
                    "야, 너 발이 넓거늘!",
                    "야, 너 발이 넓답시고!"],
        "correct": "야, 너 진짜 발이 넓다!",
        "explanation": "<p>Idioma — kundalik nutqning oʻzi. Uni yozma "
                       "qolip (PK-96) yoki adabiy qolip (PK-98) bilan "
                       "bezash gʻalati chiqadi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["친구가 발이 넓습니다.",
                    "친구가 발이 큽니다. 아는 사람이 많습니다.",
                    "그는 입이 무거워서 비밀을 지킨다.",
                    "그는 한 우물을 판 사람이다."],
        "correct": "친구가 발이 큽니다. 아는 사람이 많습니다.",
        "explanation": "<p>발이 <b>크다</b> — oyoq oʻlchami. Tanish-bilish "
                       "koʻpligi uchun <b>발이 넓다</b>.</p>",
    },
    {
        "text": "<p>Qaysi yakun eng yaxshi yozilgan?</p>",
        "choices": ["고진감래. 그래서 열심히 해야 한다.",
                    "이 글에서 저는 새옹지마, 고진감래, 유비무환을 말하고 "
                    "싶습니다.",
                    "고진감래라는 말이 있다. 힘든 시간이 지나면 좋은 날이 "
                    "온다.",
                    "고진감래입니다."],
        "correct": "고진감래라는 말이 있다. 힘든 시간이 지나면 좋은 날이 "
                   "온다.",
        "explanation": "<p>Kirituvchi qolip + iboraning maʼnosi ochilgan. "
                       "Iborani yolgʻiz tashlab ketmang va uchtasini "
                       "birga qoʻymang.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Boʻsh joyga eng mos ibora qaysi?</p>"
                "<p><b>매일 십 분씩 공부하기로 했다. 그런데 사흘 만에 "
                "그만두었다. ___</b></p>",
        "choices": ["작심삼일이었다.", "유비무환이었다.",
                    "일석이조였다.", "금상첨화였다."],
        "correct": "작심삼일이었다.",
        "explanation": "<p>“Qaror uch kun turdi” — <b>작심삼일</b>. "
                       "사흘 = uch kun, ibora bilan aynan mos "
                       "keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng mos ibora qaysi?</p>"
                "<p><b>시험에 떨어졌지만 그 덕분에 더 좋은 길을 찾았다. "
                "___</b></p>",
        "choices": ["우이독경이다.", "전화위복이다.",
                    "작심삼일이다.", "다다익선이다."],
        "correct": "전화위복이다.",
        "explanation": "<p><b>전화위복</b> — balo baraka boʻlib qaytdi. "
                       "Oʻzbekcha: “Har ishda bir xayr bor”.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-100 — Yakuniy test: matnni tahlil qilish
# ══════════════════════════════════════════════════════════════════════
Q_PK100 = [
    # 1–5 tanish (usulning oʻzi)
    {
        "text": "<p>Koreyscha jumlani tahlil qilishda birinchi qadam "
                "nima?</p>",
        "choices": ["Birinchi soʻzni tarjima qilish",
                    "Oxiriga qarab kesimni topish",
                    "Notanish soʻzlarni lugʻatdan qidirish",
                    "Qoʻshimchalarni sanash"],
        "correct": "Oxiriga qarab kesimni topish",
        "explanation": "<p>Koreys tilida eng muhim narsa hamisha "
                       "<b>oxirida</b>. Kesim zamonni, darajani va "
                       "uslubni belgilaydi.</p>",
    },
    {
        "text": "<p>Aniqlovchi shakllar qaysilar?</p>",
        "choices": ["는 · (으)ㄴ · (으)ㄹ · 던",
                    "은/는 · 이/가 · 을/를",
                    "고 · 지만 · 아/어서",
                    "다고 · 냐고 · 라고"],
        "correct": "는 · (으)ㄴ · (으)ㄹ · 던",
        "explanation": "<p>PK-43, 44, 45 va PK-90. Ulardan keyin doim "
                       "<b>ot</b> keladi.</p>",
    },
    {
        "text": "<p>Uzun jumlani birinchi navbatda nima bilan "
                "kesasiz?</p>",
        "choices": ["Vergul bilan", "Bogʻlovchi qoʻshimcha bilan",
                    "Har uch soʻzdan keyin", "Kesim bilan"],
        "correct": "Bogʻlovchi qoʻshimcha bilan",
        "explanation": "<p>지만, 아/어서, (으)니까, (으)면서, (으)면 — "
                       "jumla aynan shu yerlarda boʻlinadi.</p>",
    },
    {
        "text": "<p>Kursning uchta ustuni nima edi?</p>",
        "choices": ["Hangul · sonlar · hurmat",
                    "받침 tarmogʻi · aniqlovchi · koʻchirma gap",
                    "Sabab · shart · maqsad",
                    "Oʻtgan · hozirgi · kelasi zamon"],
        "correct": "받침 tarmogʻi · aniqlovchi · koʻchirma gap",
        "explanation": "<p>Shu uchtasini mustahkam bilsangiz, qolgani — "
                       "tafsilot.</p>",
    },
    {
        "text": "<p>Matnda notanish soʻz uchrasa nima qilasiz?</p>",
        "choices": ["Jumlani tashlab ketaman",
                    "Avval grammatikani ochaman, keyin soʻzni taxmin "
                    "qilaman",
                    "Lugʻatsiz oʻqimayman",
                    "Boshidan qayta oʻqiyman"],
        "correct": "Avval grammatikani ochaman, keyin soʻzni taxmin "
                   "qilaman",
        "explanation": "<p>Tuzilma maʼnoning yarmini beradi. 로 인해 va "
                       "지만 ni koʻrsangiz, notanish soʻz boʻlsa ham "
                       "jumlaning skeletini bilasiz.</p>",
    },

    # 6–12 qoʻllash (tahlil)
    {
        "text": "<p>Aniqlovchi qayerda?</p>"
                "<p><b>매일 운동하는 사람이 많아지고 있다.</b></p>",
        "choices": ["매일", "운동하는 + 사람", "사람이", "많아지고"],
        "correct": "운동하는 + 사람",
        "explanation": "<p><b>매일 운동하는 사람</b> — bitta katta ot: "
                       "“har kuni sport bilan shugʻullanadigan odam”. "
                       "Jumla shunda <b>[ot]이 많아지고 있다</b> ga "
                       "qisqaradi.</p>",
    },
    {
        "text": "<p>Bu jumladagi qolip qaysi va nimani bildiradi?</p>"
                "<p><b>비가 오는 바람에 행사가 취소되었다.</b></p>",
        "choices": ["는 바람에 — kutilmagan salbiy sabab",
                    "는 반면에 — qarama-qarshi tomon",
                    "는 데다가 — qoʻshimcha ogʻirlik",
                    "는 김에 — fursatdan foydalanib"],
        "correct": "는 바람에 — kutilmagan salbiy sabab",
        "explanation": "<p>PK-69. Kesim esa majhul nisbat — "
                       "취소<b>되다</b> (PK-56).</p>",
    },
    {
        "text": "<p>Bu jumla necha qavatli?</p>"
                "<p><b>전문가들은 이 문제가 커질 것이라고 말한다.</b></p>",
        "choices": ["Bir qavatli", "Ikki qavatli", "Uch qavatli",
                    "Qavat tushunchasi bunda yoʻq"],
        "correct": "Ikki qavatli",
        "explanation": "<p><b>[이 문제가 커질 것이다] + 라고 말한다</b> "
                       "(PK-60). Ichkarisi — boshqa odamning gapi. "
                       "TOPIK 읽기 matnlarining yarmi shunday.</p>",
    },
    {
        "text": "<p><b>보기는 어렵다</b> qanday yasalgan va nima "
                "degani?</p>",
        "choices": ["보다 → 보기 (PK-46 otlashtirish) — “qarash qiyin”, "
                    "ehtiyotkor rad javob",
                    "보다 → 보기 — “koʻrsatish oson”",
                    "보이다 majhul nisbati",
                    "보다 taqqoslash qoʻshimchasi"],
        "correct": "보다 → 보기 (PK-46 otlashtirish) — “qarash qiyin”, "
                   "ehtiyotkor rad javob",
        "explanation": "<p>“Bunday deyish qiyin” — men qoʻshilmayman, "
                       "lekin qatʼiy inkor ham qilmayman. TOPIK 읽기 da "
                       "juda koʻp uchraydi.</p>",
    },
    {
        "text": "<p>Bu jumlada qaysi qolip <b>sabab</b> bildiradi?</p>"
                "<p><b>인구 감소로 인해 문을 닫는 학교가 늘고 있다.</b></p>",
        "choices": ["로 인해", "는", "고 있다", "가"],
        "correct": "로 인해",
        "explanation": "<p><b>인구 감소로 인해</b> — rasmiy yozma sabab "
                       "(PK-97), faqat ot bilan. 는 — aniqlovchi, "
                       "고 있다 — davom.</p>",
    },
    {
        "text": "<p>Qaysi ikkisi juftlik hosil qiladi?</p>",
        "choices": ["읽은 책 — tugatmagan · 읽던 책 — oʻqib boʻlgan",
                    "읽은 책 — oʻqib boʻlgan · 읽던 책 — tugatmagan",
                    "Ikkalasi bir xil",
                    "읽던 책 — kelasi zamon"],
        "correct": "읽은 책 — oʻqib boʻlgan · 읽던 책 — tugatmagan",
        "explanation": "<p><b>(으)ㄴ</b> (PK-44) — tugagan ish. "
                       "<b>던</b> (PK-90) — boshlangan, tugamagan yoki "
                       "takrorlanib turgan.</p>",
    },
    {
        "text": "<p>Bu ikkisining farqi nima?</p>"
                "<p><b>간다면서요?</b> · <b>간다니!</b></p>",
        "choices": ["Birinchisi tasdiqlash (savol), ikkinchisi hayrat "
                    "(undov)",
                    "Birinchisi hayrat, ikkinchisi tasdiqlash",
                    "Ikkalasi ham savol",
                    "Ikkalasi ham kinoya"],
        "correct": "Birinchisi tasdiqlash (savol), ikkinchisi hayrat "
                   "(undov)",
        "explanation": "<p>PK-92 javob kutadi, PK-93 kutmaydi. Bir harf "
                       "farq qiladi — lekin vazifa butunlay "
                       "boshqa.</p>",
    },

    # 13–16 farqlash (butun kurs)
    {
        "text": "<p>려 oilasi: qaysi juftlik toʻgʻri?</p>",
        "choices": ["려고 하다 = niyat · 려던 참 = ayni payt · 려니 하다 = "
                    "taxmin",
                    "려고 하다 = taxmin · 려던 참 = niyat · 려니 하다 = "
                    "ayni payt",
                    "Uchalasi ham niyat",
                    "Uchalasi ham taxmin"],
        "correct": "려고 하다 = niyat · 려던 참 = ayni payt · 려니 하다 = "
                   "taxmin",
        "explanation": "<p>PK-40 · PK-90 · PK-94. 려 ning oʻzi hech "
                       "narsa demaydi — maʼnoni undan <b>keyingi</b> "
                       "qism beradi.</p>",
    },
    {
        "text": "<p>Sabab zinapoyasini toʻgʻri tartibda joylang "
                "(kundalikdan rasmiyga).</p>",
        "choices": ["로 인해 → 기 때문에 → 아/어서",
                    "아/어서 → 기 때문에 → 로 인해 → 로 말미암아",
                    "기 때문에 → 아/어서 → 로 말미암아",
                    "로 말미암아 → 로 인해 → 아/어서"],
        "correct": "아/어서 → 기 때문에 → 로 인해 → 로 말미암아",
        "explanation": "<p>PK-35 → PK-49 → PK-97 → PK-97. Va eng muhim "
                       "chegara: 때문에 gapni ham oladi, 로 인해 "
                       "<b>faqat ot</b>ni.</p>",
    },
    {
        "text": "<p>Koʻchirma gap oilasini toʻgʻri joylang.</p>",
        "choices": ["다고 하다 (xabar) → 다면서요 (tekshirish) → 다니 "
                    "(hayrat) → 답시고 (kinoya)",
                    "다니 → 다고 하다 → 답시고 → 다면서요",
                    "답시고 → 다니 → 다면서요 → 다고 하다",
                    "Ular bogʻliq emas"],
        "correct": "다고 하다 (xabar) → 다면서요 (tekshirish) → 다니 "
                   "(hayrat) → 답시고 (kinoya)",
        "explanation": "<p>PK-60 · PK-92 · PK-93 · PK-95. Toʻrttasi ham "
                       "bir xil qisqarishdan: <b>-다고 하 + …</b></p>",
    },
    {
        "text": "<p>Nega koreys tili oʻzbek oʻquvchisiga inglizzabon "
                "oʻquvchidan osonroq?</p>",
        "choices": ["Soʻzlari bir xil",
                    "Ikkala tilda ham kesim oxirida, qoʻshimchalar otga "
                    "yopishadi, aniqlovchi otdan oldin turadi",
                    "Yozuvi bir xil",
                    "Talaffuzi bir xil"],
        "correct": "Ikkala tilda ham kesim oxirida, qoʻshimchalar otga "
                   "yopishadi, aniqlovchi otdan oldin turadi",
        "explanation": "<p>Ingliz oʻquvchisi koreyscha jumlani "
                       "<em>teskari</em> oʻqishga majbur. Siz esa uni "
                       "oʻz tilingizdagidek oʻqiysiz — bu butun kurs "
                       "davomida sizning ustunligingiz edi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi tahlil <b>notoʻgʻri</b>?</p>",
        "choices": ["“운동하는 사람” — aniqlovchi + ot",
                    "“라고 말한다” — jumla ikki qavatli",
                    "“가려던 참이다” va “가려니 했다” bir xil maʼnoda",
                    "“로 인해” — faqat ot oladi"],
        "correct": "“가려던 참이다” va “가려니 했다” bir xil maʼnoda",
        "explanation": "<p><b>참</b> = niyat (PK-90) · <b>려니 하다</b> = "
                       "taxmin (PK-94). Ular butunlay boshqa "
                       "narsalar.</p>",
    },
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["폭우로 인해 경기가 취소되었다.",
                    "비가 왔기로 인해 경기가 취소되었다.",
                    "비가 왔기 때문에 경기가 취소되었다.",
                    "폭우로 인한 피해가 컸다."],
        "correct": "비가 왔기로 인해 경기가 취소되었다.",
        "explanation": "<p>로 인해 <b>faqat ot</b> oladi. Feʼlli gap "
                       "uchun 기 때문에, yoki gapni otga siqing: "
                       "비가 오다 → <b>폭우</b>.</p>",
    },

    # 19–20 tuzish (yakuniy jumla)
    {
        "text": "<p>Bu jumlani toʻgʻri tahlil qilgan variantni tanlang.</p>"
                "<p><b>인구 감소로 인해 문을 닫는 학교가 늘고 있지만, 이것이 "
                "교육의 질 저하로 이어진다고 보기는 어렵다.</b></p>",
        "choices": ["Bitta gap, bogʻlovchi yoʻq",
                    "지만 bilan ikkiga boʻlinadi; birinchi yarimda "
                    "로 인해 + 는 aniqlovchi + 고 있다, ikkinchisida "
                    "다고 + 보기는 어렵다",
                    "Uchta mustaqil gap",
                    "Faqat koʻchirma gapdan iborat"],
        "correct": "지만 bilan ikkiga boʻlinadi; birinchi yarimda "
                   "로 인해 + 는 aniqlovchi + 고 있다, ikkinchisida "
                   "다고 + 보기는 어렵다",
        "explanation": "<p>4-qadam (bogʻlovchi) jumlani ochadi. "
                       "Birinchi yarim: PK-97 · 43 · 42 · 34. Ikkinchi "
                       "yarim: PK-12 · 14 · 60 · 46 · 74.</p>",
    },
    {
        "text": "<p>Oʻsha jumlaning maʼnosi nima?</p>",
        "choices": [
            "Maktablar koʻpaymoqda va taʼlim sifati oshmoqda",
            "Aholi kamayishi tufayli yopilayotgan maktablar koʻpayib "
            "borayotgan boʻlsa-da, buni taʼlim sifatining pasayishiga "
            "olib keladi deb qarash qiyin",
            "Aholi kamaygani uchun taʼlim sifati albatta pasayadi",
            "Maktablar yopilishi bilan taʼlim sifati bogʻliq emasligi "
            "isbotlangan"],
        "correct": "Aholi kamayishi tufayli yopilayotgan maktablar "
                   "koʻpayib borayotgan boʻlsa-da, buni taʼlim "
                   "sifatining pasayishiga olib keladi deb qarash qiyin",
        "explanation": "<p><b>보기는 어렵다</b> — ehtiyotkor rad javob: "
                       "“deb qarash qiyin”. Bu isbot ham, qatʼiy inkor "
                       "ham emas. Mana shu nozik farqni koʻra olish — "
                       "TOPIK II darajasi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-98 Mashq: 거늘 · 기로서니",
        "description": "20 savol — adabiy yon berish, 하물며 … (이)랴 "
                       "juftligi, 아무리 sharti, tanbeh davomi va "
                       "더라도 dan farqi.",
        "tutorial":    "PK-98:",
        "level":       "medium",
        "questions":   Q_PK98,
    },
    {
        "title":       "PK-99 Mashq: 사자성어 va idiomalar",
        "description": "20 savol — 12 ta 사자성어, 10 ta idioma, "
                       "oʻzbekcha maqol juftliklari va inshoga "
                       "kiritish qoidasi.",
        "tutorial":    "PK-99:",
        "level":       "medium",
        "questions":   Q_PK99,
    },
    {
        "title":       "PK-100 Mashq: Yakuniy test — matnni tahlil qilish",
        "description": "20 savol — kursning yakuni. Besh qadamli tahlil "
                       "usuli, aniqlovchi va koʻchirma gap qavatlari, "
                       "려 oilasi, sabab zinapoyasi va TOPIK II "
                       "darajasidagi jumla.",
        "tutorial":    "PK-100:",
        "level":       "medium",
        "questions":   Q_PK100,
    },
]
