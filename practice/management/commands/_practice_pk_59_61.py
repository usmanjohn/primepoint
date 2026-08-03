# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-59 … PK-61.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_59_61.py --master=prime \\
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
# PK-59 — 아/어 놓다 va 아/어 두다
# =====================================================================

Q_PK59 = [
    # 1–5 tanish
    {
        "text": "<p><strong>아/어 놓다</strong> nimani bildiradi?</p>",
        "choices": ["Ish tugadi va natijasi turibdi",
                    "Ish butunlay yoʻq boʻldi",
                    "Ish hali boshlanmadi",
                    "Ishni boshqa odam qildirdi"],
        "correct": "Ish tugadi va natijasi turibdi",
        "explanation": "<p>창문을 열어 놓았어요 — ochdim va deraza hozir ham "
                       "ochiq. Oʻzbekcha “ochi<strong>b qoʻydim</strong>”.</p>",
    },
    {
        "text": "<p><strong>놓다</strong> feʼlining asl maʼnosi nima?</p>",
        "choices": ["Tashlamoq", "Olmoq", "Qoʻymoq", "Yopmoq"],
        "correct": "Qoʻymoq",
        "explanation": "<p>책을 책상 위에 놓았어요 — kitobni stol ustiga "
                       "qoʻydim. Koʻmakchi maʼnosi shundan oʻsib "
                       "chiqadi.</p>",
    },
    {
        "text": "<p><strong>하다</strong> bu qolipda qanday shaklga "
                "kiradi?</p>",
        "choices": ["하 놓다", "할 놓다", "하고 놓다", "해 놓다"],
        "correct": "해 놓다",
        "explanation": "<p>놓다 dan oldin feʼl <strong>아/어 shaklida</strong> "
                       "turadi. 하다 → <strong>해</strong>.</p>",
    },
    {
        "text": "<p><strong>해 놓았어요</strong> ning kundalik qisqargan "
                "shakli qaysi?</p>",
        "choices": ["해 놨어요", "해 놓어요", "했 놓아요", "해놓았죠"],
        "correct": "해 놨어요",
        "explanation": "<p>놓았 → <strong>놨</strong>: 숙제를 벌써 해 "
                       "놨어요.</p>",
    },
    {
        "text": "<p><strong>알아 두세요</strong> nima degani?</p>",
        "choices": ["Bilib qoʻying", "Bilmang", "Bilib boʻldingiz",
                    "Bilishga harakat qiling"],
        "correct": "Bilib qoʻying",
        "explanation": "<p><strong>알아 두다</strong> — qotib qolgan ibora. "
                       "Bu yerda 놓다 ishlatilmaydi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 더워서 창문을 <strong>______</strong> "
                "놓았어요. (열다)</p>",
        "choices": ["열", "열어", "열고", "연"],
        "correct": "열어",
        "explanation": "<p>열다 → <strong>열어</strong> 놓았어요. 놓다 dan "
                       "oldin 아/어 shakli shart.</p>",
    },
    {
        "text": "<p>Toʻldiring: 손님이 오니까 음식을 미리 "
                "<strong>______</strong> 놓았어요. (만들다)</p>",
        "choices": ["만들", "만드는", "만들어", "만든"],
        "correct": "만들어",
        "explanation": "<p>만들다 → <strong>만들어</strong> 놓았어요 — "
                       "ovqat tayyor turibdi (tayyorgarlik maʼnosi).</p>",
    },
    {
        "text": "<p>“Chiptani oldindan olib qoʻydim” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["표를 미리 사 놓았어요", "표를 미리 사 버렸어요",
                    "표를 미리 살 놓았어요", "표를 미리 사 있어요"],
        "correct": "표를 미리 사 놓았어요",
        "explanation": "<p>사다 → 사 놓다. <strong>미리</strong> (oldindan) "
                       "bu qolip bilan juda koʻp yuradi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 불을 <strong>______</strong> 놨어요. "
                "(켜다)</p>",
        "choices": ["켜", "켜서", "켤", "켠"],
        "correct": "켜",
        "explanation": "<p>켜다 ning oxirgi unlisi ㅕ — 켜 + 어 qoʻshilib "
                       "<strong>켜</strong> boʻlib qoladi: 켜 놨어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시험이 있으니까 단어를 미리 "
                "<strong>______</strong> 놓았어요. (외우다)</p>",
        "choices": ["외우", "외운", "외워", "외울"],
        "correct": "외워",
        "explanation": "<p>외우다 → <strong>외워</strong> 놓았어요 — "
                       "soʻzlarni oldindan yodlab qoʻydim.</p>",
    },
    {
        "text": "<p>“Pulni bankka solib qoʻydim (uzoq muddatga)” — qaysi "
                "biri tabiiyroq?</p>",
        "choices": ["돈을 은행에 넣어 버렸어요", "돈을 은행에 넣어 두었어요",
                    "돈을 은행에 넣어 있어요", "돈을 은행에 넣을 놓았어요"],
        "correct": "돈을 은행에 넣어 두었어요",
        "explanation": "<p>Uzoq muddat ohangi uchun <strong>두다</strong> "
                       "tabiiyroq. 놓다 ham notoʻgʻri emas, lekin qisqaroq "
                       "muddatga ishora qiladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 단어를 <strong>______</strong> 두세요.</p>",
        "choices": ["알아", "알고", "알", "아는"],
        "correct": "알아",
        "explanation": "<p><strong>알아 두세요</strong> — “bilib qoʻying”. "
                       "알다 → 알아.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>케이크를 먹어 버렸어요</strong> / "
                "<strong>케이크를 만들어 놓았어요</strong></p>",
        "choices": ["Ikkalasi bir xil",
                    "Birinchisida tort tugadi, ikkinchisida tort tayyor "
                    "turibdi",
                    "Birinchisida tort tayyor, ikkinchisida tugadi",
                    "Birinchisi kelasi zamon"],
        "correct": "Birinchisida tort tugadi, ikkinchisida tort tayyor "
                   "turibdi",
        "explanation": "<p>Oʻzbekchada ikkalasi ham “-b qoʻydim”, koreyschada "
                       "esa boshqa soʻz: <strong>버리다</strong> yoʻq qiladi, "
                       "<strong>놓다</strong> saqlab turadi.</p>",
    },
    {
        "text": "<p>“Eshik ochiq turibdi, kim ochgani nomaʼlum” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["문을 열어 놓았어요", "문이 열려 있어요",
                    "문을 열어 있어요", "문이 열어 놓았어요"],
        "correct": "문이 열려 있어요",
        "explanation": "<p>Bajaruvchi aytilmasa — majhul + 있다 "
                       "(PK-56 va PK-42): 문<strong>이</strong> 열려 "
                       "있어요. 문<strong>을</strong> 열어 놓았어요 da esa "
                       "men ochganman.</p>",
    },
    {
        "text": "<p>Qaysi qoʻshimcha 아/어 놓다 gapida keladi?</p>",
        "choices": ["이/가 — chunki bu holat",
                    "을/를 — chunki bajaruvchi bor va bu uning ishi",
                    "에게 — chunki odam bor",
                    "에서 — chunki joy bor"],
        "correct": "을/를 — chunki bajaruvchi bor va bu uning ishi",
        "explanation": "<p>문<strong>을</strong> 열어 놓았어요 — men qilgan "
                       "ish. Holat gapida esa 문<strong>이</strong> 열려 "
                       "있어요 boʻladi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>날씨가 좋아 놓았어요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["Zamon xato",
                    "날씨 ega boʻlolmaydi",
                    "좋다 — sifat, 놓다 esa faqat harakat feʼllari bilan "
                    "keladi",
                    "놓다 dan oldin 고 kerak"],
        "correct": "좋다 — sifat, 놓다 esa faqat harakat feʼllari bilan "
                   "keladi",
        "explanation": "<p>Sifat oʻzgarishi uchun <strong>아/어지다</strong> "
                       "bor: 날씨가 <strong>좋아졌어요</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>음식을 만들 놓았어요.</strong></p>",
        "choices": ["만들 → 만들어", "놓았어요 → 놨어요",
                    "음식을 → 음식이", "Xato yoʻq"],
        "correct": "만들 → 만들어",
        "explanation": "<p>놓다 dan oldin feʼl <strong>아/어 shaklida"
                       "</strong> turishi shart: 만들<strong>어</strong> "
                       "놓았어요.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>문을 열어 놓아 있어요.</strong></p>",
        "choices": ["문을 → 문이", "열어 → 열려",
                    "놓아 있어요 → 놓았어요", "Xato yoʻq"],
        "correct": "놓아 있어요 → 놓았어요",
        "explanation": "<p>놓다 va 있다 birga kelmaydi. Yo <strong>문을 열어 "
                       "놓았어요</strong>, yo <strong>문이 열려 있어요</strong> "
                       "— bittasini tanlang.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Uy vazifasini allaqachon qilib qoʻyganman” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["숙제를 벌써 해 버렸어요", "숙제를 벌써 하 놨어요",
                    "숙제를 벌써 해 놨어요", "숙제를 벌써 할 놓았어요"],
        "correct": "숙제를 벌써 해 놨어요",
        "explanation": "<p>하다 → 해, 놓았 → 놨: <strong>해 놨어요</strong>. "
                       "해 버렸어요 boʻlsa “qilib boʻldim, yengil "
                       "boʻldim” degan boshqa ohang chiqadi.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 방이 왜 이렇게 시원해요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["창문을 열어 놓았어요", "창문을 열어 버렸어요",
                    "창문이 열어 놓았어요", "창문을 열 놓았어요"],
        "correct": "창문을 열어 놓았어요",
        "explanation": "<p>Xona salqin, chunki deraza <em>hozir ham</em> "
                       "ochiq — natija turibdi. Aynan "
                       "<strong>아/어 놓다</strong> ning oʻrni.</p>",
    },
]


# =====================================================================
# PK-60 — -다고 하다 / -냐고 하다
# =====================================================================

Q_PK60 = [
    # 1–5 tanish
    {
        "text": "<p>Koreyschadagi <strong>고</strong> oʻzbekchada qaysi "
                "soʻzning oʻrnida turadi?</p>",
        "choices": ["deb", "uchun", "bilan", "keyin"],
        "correct": "deb",
        "explanation": "<p>내일 간다<strong>고</strong> 했어요 = “ertaga "
                       "boradi <strong>deb</strong> aytdi”. Gap "
                       "buzilmaydi — orqasiga qoʻshimcha qoʻshiladi.</p>",
    },
    {
        "text": "<p><strong>가다</strong> darak koʻchirma gapda qanday "
                "shaklga kiradi?</p>",
        "choices": ["가다고", "간다고", "가는다고", "갈다고"],
        "correct": "간다고",
        "explanation": "<p>Feʼl, 받침 yoʻq → <strong>ㄴ다고</strong>: "
                       "가 + ㄴ다고 = 간다고.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> darak koʻchirma gapda qanday "
                "shaklga kiradi?</p>",
        "choices": ["먹다고", "먹은다고", "먹는다고", "먹라고"],
        "correct": "먹는다고",
        "explanation": "<p>Feʼl, 받침 bor → <strong>는다고</strong>: "
                       "먹는다고 해요.</p>",
    },
    {
        "text": "<p><strong>좋다</strong> (sifat) darak koʻchirma gapda "
                "qanday shaklga kiradi?</p>",
        "choices": ["좋는다고", "좋다고", "좋은다고", "좋라고"],
        "correct": "좋다고",
        "explanation": "<p>Sifat ㄴ다/는다 <strong>olmaydi</strong> — oddiy "
                       "<strong>다고</strong> boʻlib qoladi.</p>",
    },
    {
        "text": "<p>Soʻroq gapni yetkazish uchun qaysi qoʻshimcha "
                "ishlatiladi?</p>",
        "choices": ["다고", "자고", "라고", "냐고"],
        "correct": "냐고",
        "explanation": "<p>어디에 <strong>가냐고</strong> 물어봤어요 — "
                       "“qayerga borasiz deb soʻradi”. 냐고 da feʼl/sifat "
                       "farqi yoʻq.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Koʻchirma gapga aylantiring: 민수: “저는 내일 "
                "가요.”</p>",
        "choices": ["민수 씨가 내일 가다고 했어요",
                    "민수 씨가 내일 간다고 했어요",
                    "민수 씨가 내일 가라고 했어요",
                    "민수 씨가 내일 가자고 했어요"],
        "correct": "민수 씨가 내일 간다고 했어요",
        "explanation": "<p>Darak gap + feʼl, 받침 yoʻq → "
                       "<strong>간다고</strong>.</p>",
    },
    {
        "text": "<p>Koʻchirma gapga aylantiring: 지영: “요즘 바빠요.”</p>",
        "choices": ["지영 씨가 요즘 바쁜다고 했어요",
                    "지영 씨가 요즘 바쁘다고 했어요",
                    "지영 씨가 요즘 바쁘냐고 했어요",
                    "지영 씨가 요즘 바쁘라고 했어요"],
        "correct": "지영 씨가 요즘 바쁘다고 했어요",
        "explanation": "<p>바쁘다 — <strong>sifat</strong>, shuning uchun "
                       "oddiy 다고.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아프소나 씨가 <strong>______</strong> "
                "했어요. (“men talabaman”)</p>",
        "choices": ["학생이다고", "학생인다고", "학생이라고", "학생다고"],
        "correct": "학생이라고",
        "explanation": "<p>Ot + 이다 → <strong>(이)라고</strong>. 받침 "
                       "yoʻq boʻlsa 이 tushadi: 친구라고.</p>",
    },
    {
        "text": "<p>Toʻldiring: 베크조드 씨가 어제 영화를 "
                "<strong>______</strong> 했어요.</p>",
        "choices": ["본다고", "봤다고", "보냐고", "보라고"],
        "correct": "봤다고",
        "explanation": "<p>Oʻtgan zamon <strong>았/었다고</strong> boʻladi: "
                       "봤다고 했어요.</p>",
    },
    {
        "text": "<p>Koʻchirma gapga aylantiring: 선생님: “숙제를 "
                "했어요?”</p>",
        "choices": ["선생님이 숙제를 했다고 물어봤어요",
                    "선생님이 숙제를 하라고 물어봤어요",
                    "선생님이 숙제를 했냐고 물어봤어요",
                    "선생님이 숙제를 하자고 물어봤어요"],
        "correct": "선생님이 숙제를 했냐고 물어봤어요",
        "explanation": "<p>Savol → <strong>냐고</strong>, va savol uchun "
                       "하다 emas, <strong>묻다/물어보다</strong> "
                       "tabiiyroq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 내일 시험이 <strong>______</strong> "
                "들었어요. (“imtihon yoʻq”)</p>",
        "choices": ["없는다고", "없다고", "없이라고", "없냐고"],
        "correct": "없다고",
        "explanation": "<p>있다/없다 sifat kabi ishlaydi → "
                       "<strong>없다고</strong>. 고 들었어요 = “deb "
                       "eshitdim”.</p>",
    },
    {
        "text": "<p>Kelasi zamon koʻchirma gapda qanday boʻladi? "
                "(갈 거예요)</p>",
        "choices": ["갈 거라고", "갈 거다고", "가겠다고만", "갈다고"],
        "correct": "갈 거라고",
        "explanation": "<p>거예요 — ot bilan tugagan tuzilma (거 + 이다), "
                       "shuning uchun <strong>(이)라고</strong> qoidasi "
                       "ishlaydi: 갈 거라고 했어요.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>간다고 했어요</strong> / "
                "<strong>가냐고 했어요</strong></p>",
        "choices": ["Birinchisi “boradi dedi”, ikkinchisi “boradimi deb "
                    "soʻradi”",
                    "Birinchisi “bor dedi”, ikkinchisi “boraylik dedi”",
                    "Ikkalasi bir xil",
                    "Birinchisi savol, ikkinchisi darak"],
        "correct": "Birinchisi “boradi dedi”, ikkinchisi “boradimi deb "
                   "soʻradi”",
        "explanation": "<p><strong>다고</strong> — darak gap. "
                       "<strong>냐고</strong> — soʻroq gap. Qoʻshimcha "
                       "gapning turini aytadi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda ikkalasi ham toʻgʻri?</p>",
        "choices": ["춥는다고 / 좋는다고", "춥다고 / 좋다고",
                    "춥ㄴ다고 / 좋ㄴ다고", "추운다고 / 좋은다고"],
        "correct": "춥다고 / 좋다고",
        "explanation": "<p>춥다 va 좋다 — ikkalasi ham sifat. Sifat "
                       "ㄴ다/는다 olmaydi, oddiy <strong>다고</strong> "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>학생이다고</strong> notoʻgʻri?</p>",
        "choices": ["Chunki 학생 da 받침 bor",
                    "Chunki ot + 이다 → (이)라고 boʻladi",
                    "Chunki bu soʻroq gap",
                    "Chunki zamon yoʻq"],
        "correct": "Chunki ot + 이다 → (이)라고 boʻladi",
        "explanation": "<p>이다 koʻchirma gapda alohida yoʻl tutadi: "
                       "<strong>학생이라고</strong> 했어요.</p>",
    },
    {
        "text": "<p><strong>가느냐고</strong> shakli haqida nima toʻgʻri?</p>",
        "choices": ["Notoʻgʻri, bunday shakl yoʻq",
                    "Toʻgʻri, lekin eskiroq va rasmiy — kundalik nutqda "
                    "냐고 deyiladi",
                    "Faqat sifatlar bilan ishlatiladi",
                    "Faqat buyruq gapda ishlatiladi"],
        "correct": "Toʻgʻri, lekin eskiroq va rasmiy — kundalik nutqda "
                   "냐고 deyiladi",
        "explanation": "<p>Kitoblarda 느냐고 (feʼl) va (으)냐고 (sifat) "
                       "uchraydi. Ular xato emas, faqat kundalik nutqda "
                       "hamma <strong>냐고</strong> deydi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>날씨가 춥는다고 했어요.</strong></p>",
        "choices": ["춥는다고 → 춥다고", "춥는다고 → 추운다고",
                    "날씨가 → 날씨는", "Xato yoʻq"],
        "correct": "춥는다고 → 춥다고",
        "explanation": "<p>춥다 — sifat, ㄴ다/는다 olmaydi. Faqat feʼl "
                       "간다고/먹는다고 boʻladi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>민수 씨가 내일 가다고 "
                "했어요.</strong></p>",
        "choices": ["가다고 → 간다고", "가다고 → 가는다고",
                    "가다고 → 가라고", "Xato yoʻq"],
        "correct": "가다고 → 간다고",
        "explanation": "<p>Feʼlning oddiy lugʻat shakli koʻchirma gapga "
                       "toʻgʻridan-toʻgʻri kirmaydi: 받침siz feʼl "
                       "<strong>ㄴ다고</strong> oladi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Jiyon kecha kino koʻrdim deb aytdi” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["지영 씨가 어제 영화를 본다고 했어요",
                    "지영 씨가 어제 영화를 봤다고 했어요",
                    "지영 씨가 어제 영화를 봤냐고 했어요",
                    "지영 씨가 어제 영화를 보라고 했어요"],
        "correct": "지영 씨가 어제 영화를 봤다고 했어요",
        "explanation": "<p>Oʻtgan zamon koʻchirma gapda saqlanadi: "
                       "<strong>봤다고</strong> 했어요.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 자스루르 씨가 뭐라고 했어요?</p>"
                "<p><strong>나:</strong> (Jasur: “men band emasman”) ___</p>",
        "choices": ["안 바쁘다고 했어요", "안 바쁜다고 했어요",
                    "안 바쁘냐고 했어요", "안 바쁘라고 했어요"],
        "correct": "안 바쁘다고 했어요",
        "explanation": "<p>바쁘다 — sifat → <strong>다고</strong>, inkor "
                       "안 esa oʻz joyida qoladi.</p>",
    },
]


# =====================================================================
# PK-61 — -라고 하다 / -자고 하다
# =====================================================================

Q_PK61 = [
    # 1–5 tanish
    {
        "text": "<p>Buyruqni yetkazish uchun qaysi qoʻshimcha "
                "ishlatiladi?</p>",
        "choices": ["다고", "냐고", "(으)라고", "자고"],
        "correct": "(으)라고",
        "explanation": "<p>선생님이 일찍 <strong>오라고</strong> 했어요 — "
                       "“erta kel deb aytdi”.</p>",
    },
    {
        "text": "<p>Taklifni yetkazish uchun qaysi qoʻshimcha "
                "ishlatiladi?</p>",
        "choices": ["자고", "다고", "냐고", "(으)라고"],
        "correct": "자고",
        "explanation": "<p>같이 <strong>가자고</strong> 했어요 — “birga "
                       "boraylik deb taklif qildi”.</p>",
    },
    {
        "text": "<p><strong>먹다</strong> buyruq koʻchirma gapda qanday "
                "shaklga kiradi?</p>",
        "choices": ["먹라고", "먹으라고", "먹는라고", "먹자고"],
        "correct": "먹으라고",
        "explanation": "<p>먹 da 받침 bor → <strong>으라고</strong>: "
                       "약을 먹으라고 했어요.</p>",
    },
    {
        "text": "<p>Taqiqni (“qilmang”) yetkazish shakli qaysi?</p>",
        "choices": ["지 마라고 하다", "지 말라고 하다", "지 않라고 하다",
                    "지 못라고 하다"],
        "correct": "지 말라고 하다",
        "explanation": "<p>말다 ning oʻzagi <strong>말</strong>, unga 라고 "
                       "qoʻshiladi → <strong>말라고</strong>. 마라고 "
                       "emas.</p>",
    },
    {
        "text": "<p>Taklif va buyruq koʻchirma gapida zamon boʻladimi?</p>",
        "choices": ["Ha, 았/었 qoʻshiladi",
                    "Yoʻq — oʻtgan zamon faqat 했어요 da boʻladi",
                    "Faqat taklifda boʻladi",
                    "Faqat buyruqda boʻladi"],
        "correct": "Yoʻq — oʻtgan zamon faqat 했어요 da boʻladi",
        "explanation": "<p><s>갔라고</s>, <s>갔자고</s> degan shakllar "
                       "mavjud emas. 가라고 <strong>했어요</strong> — "
                       "zamon oxirgi feʼlda.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Koʻchirma gapga aylantiring: 선생님: “일찍 "
                "오세요.”</p>",
        "choices": ["선생님이 일찍 온다고 했어요",
                    "선생님이 일찍 오냐고 했어요",
                    "선생님이 일찍 오라고 했어요",
                    "선생님이 일찍 오자고 했어요"],
        "correct": "선생님이 일찍 오라고 했어요",
        "explanation": "<p>Buyruq → <strong>(으)라고</strong>. 오다 da "
                       "받침 yoʻq → 라고.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어머니가 약을 <strong>______</strong> "
                "했어요. (먹다)</p>",
        "choices": ["먹라고", "먹으라고", "먹는다고", "먹자고"],
        "correct": "먹으라고",
        "explanation": "<p>받침 bor → <strong>으라고</strong>: "
                       "먹으라고 했어요.</p>",
    },
    {
        "text": "<p>Koʻchirma gapga aylantiring: 자스루르: “주말에 같이 "
                "산에 가요!”</p>",
        "choices": ["산에 간다고 했어요", "산에 가냐고 했어요",
                    "산에 가라고 했어요", "산에 가자고 했어요"],
        "correct": "산에 가자고 했어요",
        "explanation": "<p>“Birga qilaylik” maʼnosi → taklif → "
                       "<strong>자고</strong>. Bu yerda 받침 ayrisi "
                       "yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 선생님이 교실에서 <strong>______</strong> "
                "했어요. (뛰지 말다)</p>",
        "choices": ["뛰지 마라고", "뛰지 말라고", "뛰지 않라고",
                    "뛰지 말자고"],
        "correct": "뛰지 말라고",
        "explanation": "<p>Taqiq → <strong>지 말라고</strong>: sinfda "
                       "yugurmang deb aytdi.</p>",
    },
    {
        "text": "<p>“Bormaylik dedi” — qaysi biri toʻgʻri?</p>",
        "choices": ["가지 말자고 했어요", "가지 말라고 했어요",
                    "안 간다고 했어요", "가지 마냐고 했어요"],
        "correct": "가지 말자고 했어요",
        "explanation": "<p>Inkor <em>taklif</em> → <strong>지 말자고"
                       "</strong>. 지 말라고 boʻlsa “borma” degan buyruq "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구가 책을 <strong>______</strong> "
                "했어요. (“menga ber” dedi)</p>",
        "choices": ["주라고", "달라고", "준다고", "주자고"],
        "correct": "달라고",
        "explanation": "<p>Soʻrayotgan odam <strong>oʻziga</strong> "
                       "soʻrasa — <strong>달라고</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구가 동생에게 책을 "
                "<strong>______</strong> 했어요. (“ukamga ber” dedi)</p>",
        "choices": ["달라고", "주라고", "준다고", "주냐고"],
        "correct": "주라고",
        "explanation": "<p>Uchinchi odamga berilsin desa — "
                       "<strong>주라고</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Bu toʻrttasini ajrating: 간다고 · 가냐고 · 가라고 · "
                "가자고. Qaysi biri <strong>taklif</strong>?</p>",
        "choices": ["간다고", "가냐고", "가라고", "가자고"],
        "correct": "가자고",
        "explanation": "<p>간다고 — “boradi” (darak). 가냐고 — “boradimi?” "
                       "(soʻroq). 가라고 — “bor!” (buyruq). "
                       "<strong>가자고</strong> — “boraylik!” (taklif).</p>",
    },
    {
        "text": "<p>Farqi nimada? <strong>달라고 했어요</strong> / "
                "<strong>주라고 했어요</strong></p>",
        "choices": ["Birinchisi oʻziga soʻradi, ikkinchisi uchinchi odamga "
                    "berilsin dedi",
                    "Birinchisi uchinchi odamga, ikkinchisi oʻziga",
                    "Ikkalasi bir xil",
                    "Birinchisi taklif, ikkinchisi buyruq"],
        "correct": "Birinchisi oʻziga soʻradi, ikkinchisi uchinchi odamga "
                   "berilsin dedi",
        "explanation": "<p>Oʻzbekchada buni olmosh aytadi (“menga” / "
                       "“unga”), koreyschada esa <strong>feʼlning "
                       "oʻzi</strong> oʻzgaradi.</p>",
    },
    {
        "text": "<p>Farqi nimada? <strong>가지 말라고 했어요</strong> / "
                "<strong>가지 말자고 했어요</strong></p>",
        "choices": ["Birinchisi “borma” (buyruq), ikkinchisi “bormaylik” "
                    "(taklif)",
                    "Birinchisi “bormaylik”, ikkinchisi “borma”",
                    "Ikkalasi bir xil",
                    "Birinchisi savol, ikkinchisi darak"],
        "correct": "Birinchisi “borma” (buyruq), ikkinchisi “bormaylik” "
                   "(taklif)",
        "explanation": "<p><strong>말라고</strong> — bitta odamga buyruq. "
                       "<strong>말자고</strong> — “biz bormaylik” degan "
                       "taklif.</p>",
    },
    {
        "text": "<p><strong>하다</strong> buyruq koʻchirma gapda qanday "
                "boʻladi?</p>",
        "choices": ["해라고", "하라고", "하으라고", "한다고"],
        "correct": "하라고",
        "explanation": "<p>하 da 받침 yoʻq → <strong>라고</strong>: "
                       "숙제를 하라고 했어요. Diqqat — 해라고 emas.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>선생님이 뛰지 마라고 "
                "했어요.</strong></p>",
        "choices": ["마라고 → 말라고", "마라고 → 말자고",
                    "뛰지 → 뛰기", "Xato yoʻq"],
        "correct": "마라고 → 말라고",
        "explanation": "<p>말다 + 라고 = <strong>말라고</strong>. Bu eng "
                       "koʻp uchraydigan xatolardan biri.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>친구가 같이 갔자고 "
                "했어요.</strong></p>",
        "choices": ["갔자고 → 가자고", "갔자고 → 갔다고",
                    "같이 → 함께", "Xato yoʻq"],
        "correct": "갔자고 → 가자고",
        "explanation": "<p>Taklifda zamon boʻlmaydi — oʻtgan zamon faqat "
                       "<strong>했어요</strong> da.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Onam dorini ich deb aytdi” — qaysi biri toʻgʻri?</p>",
        "choices": ["어머니가 약을 먹는다고 했어요",
                    "어머니가 약을 먹라고 했어요",
                    "어머니가 약을 먹으라고 했어요",
                    "어머니가 약을 먹자고 했어요"],
        "correct": "어머니가 약을 먹으라고 했어요",
        "explanation": "<p>Buyruq + 받침 bor → <strong>먹으라고</strong> "
                       "했어요.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 친구가 뭐라고 했어요?</p>"
                "<p><strong>나:</strong> (Doʻsti: “birga ovqat yeylik!”) ___</p>",
        "choices": ["같이 밥을 먹자고 했어요", "같이 밥을 먹으라고 했어요",
                    "같이 밥을 먹는다고 했어요", "같이 밥을 먹냐고 했어요"],
        "correct": "같이 밥을 먹자고 했어요",
        "explanation": "<p>“Birga qilaylik” — taklif → <strong>자고</strong>. "
                       "먹으라고 boʻlsa “ovqatni ye!” degan buyruq "
                       "boʻlardi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-59 Mashq: 아/어 놓다 va 아/어 두다",
        "description": "20 savol — yasalishi, tayyorgarlik va holat maʼnolari, "
                       "버리다 hamda 아/어 있다 dan farqi.",
        "tutorial":    "PK-59:",
        "level":       "medium",
        "questions":   Q_PK59,
    },
    {
        "title":       "PK-60 Mashq: Koʻchirma gap 1 — 다고 / 냐고 하다",
        "description": "20 savol — feʼl, sifat va ot shakllari, zamon, "
                       "soʻroq gap va 묻다/들었어요 bilan ishlash.",
        "tutorial":    "PK-60:",
        "level":       "medium",
        "questions":   Q_PK60,
    },
    {
        "title":       "PK-61 Mashq: Koʻchirma gap 2 — (으)라고 / 자고 하다",
        "description": "20 savol — buyruq, taqiq va taklif shakllari, "
                       "달라고/주라고 farqi va toʻrtta gap turi.",
        "tutorial":    "PK-61:",
        "level":       "medium",
        "questions":   Q_PK61,
    },
]
