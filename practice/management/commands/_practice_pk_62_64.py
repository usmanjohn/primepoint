# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-62 … PK-64.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_62_64.py --master=prime \\
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
# PK-62 — -대요 / -냬요 / -래요 / -재요
# =====================================================================

Q_PK62 = [
    # 1–5 tanish
    {
        "text": "<p>Qisqartirishning asosiy qoidasi nima?</p>",
        "choices": ["고 해 qismi tushadi, qolgani qoʻshiladi",
                    "Feʼl oʻzagi tushadi",
                    "Zamon qoʻshimchasi tushadi",
                    "Ega tushadi"],
        "correct": "고 해 qismi tushadi, qolgani qoʻshiladi",
        "explanation": "<p>간다<strong>고 해</strong>요 → 간<strong>대</strong>요. "
                       "Qoida mexanik va toʻrtala shaklda bir xil.</p>",
    },
    {
        "text": "<p><strong>간다고 해요</strong> ning qisqargan shakli "
                "qaysi?</p>",
        "choices": ["가대요", "간대요", "가래요", "가재요"],
        "correct": "간대요",
        "explanation": "<p>Feʼlning <strong>ㄴ다</strong> qismi qisqarganda "
                       "ham qoladi: 간대요.</p>",
    },
    {
        "text": "<p><strong>가라고 해요</strong> (buyruq) ning qisqargan "
                "shakli qaysi?</p>",
        "choices": ["간대요", "가냬요", "가래요", "가재요"],
        "correct": "가래요",
        "explanation": "<p>라고 해요 → <strong>래요</strong>: “bor deyapti”.</p>",
    },
    {
        "text": "<p><strong>가자고 해요</strong> (taklif) ning qisqargan "
                "shakli qaysi?</p>",
        "choices": ["가재요", "가래요", "간대요", "가냬요"],
        "correct": "가재요",
        "explanation": "<p>자고 해요 → <strong>재요</strong>: “boraylik "
                       "deyapti”.</p>",
    },
    {
        "text": "<p><strong>-대요</strong> ning oʻzbekcha eng yaqin "
                "juftligi qaysi?</p>",
        "choices": ["…moqchi", "…emish / …ekan", "…sa kerak", "…gan edi"],
        "correct": "…emish / …ekan",
        "explanation": "<p>Ikkalasi ham “eshitdim, lekin oʻzim koʻrmadim” "
                       "degan ohangni bitta qoʻshimchaga yigʻadi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Qisqartiring: <strong>그 영화가 재미있다고 해요.</strong></p>",
        "choices": ["재미있는대요", "재미있대요", "재미있래요", "재미있이래요"],
        "correct": "재미있대요",
        "explanation": "<p>재미있다 sifat kabi ishlaydi → oddiy "
                       "<strong>대요</strong>, ㄴ다/는다 qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Qisqartiring: <strong>민수 씨가 밥을 먹는다고 "
                "해요.</strong></p>",
        "choices": ["먹대요", "먹는대요", "먹래요", "먹은대요"],
        "correct": "먹는대요",
        "explanation": "<p>Feʼl, 받침 bor → 는다고 해요 → "
                       "<strong>먹는대요</strong>.</p>",
    },
    {
        "text": "<p>Qisqartiring: <strong>그 사람이 새 선생님이라고 "
                "해요.</strong></p>",
        "choices": ["선생님이대요", "선생님대요", "선생님이래요", "선생님래요"],
        "correct": "선생님이래요",
        "explanation": "<p>Ot + 이다 → 이라고 해요 → "
                       "<strong>이래요</strong>.</p>",
    },
    {
        "text": "<p>Qisqartiring: <strong>어머니가 숙제를 했냐고 "
                "해요.</strong></p>",
        "choices": ["했대요", "했냬요", "했래요", "했재요"],
        "correct": "했냬요",
        "explanation": "<p>냐고 해요 → <strong>냬요</strong> — soʻroq "
                       "gapning qisqargan shakli.</p>",
    },
    {
        "text": "<p>Toʻldiring: 선생님이 교실에서 뛰지 "
                "<strong>______</strong>.</p>",
        "choices": ["말대요", "말래요", "말재요", "마래요"],
        "correct": "말래요",
        "explanation": "<p>지 말라고 해요 → <strong>지 말래요</strong> — "
                       "“yugurmang deyapti”.</p>",
    },
    {
        "text": "<p>Qisqartiring: <strong>지영 씨가 어제 갔다고 "
                "해요.</strong></p>",
        "choices": ["가대요", "갔대요", "갔래요", "간대요"],
        "correct": "갔대요",
        "explanation": "<p>Oʻtgan zamon saqlanadi: 았/었다고 해요 → "
                       "<strong>았/었대요</strong>.</p>",
    },
    {
        "text": "<p>“Rost emas ekan” — qaysi biri toʻgʻri?</p>",
        "choices": ["사실이 아니래요", "사실이 아니대요",
                    "사실이 아닌대요", "사실이 아니재요"],
        "correct": "사실이 아니래요",
        "explanation": "<p>아니다 ham 이다 kabi yoʻl tutadi: 아니라고 해요 → "
                       "<strong>아니래요</strong>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Bu toʻrttasidan qaysi biri <strong>taklif</strong>ni "
                "bildiradi?</p>",
        "choices": ["간대요", "가냬요", "가래요", "가재요"],
        "correct": "가재요",
        "explanation": "<p>간대요 — boradi emish. 가냬요 — boradimi deb "
                       "soʻrayapti. 가래요 — bor deyapti. "
                       "<strong>가재요</strong> — boraylik deyapti.</p>",
    },
    {
        "text": "<p><strong>가래요</strong> va <strong>갈래요</strong> "
                "farqi nimada?</p>",
        "choices": ["Ikkalasi bir xil",
                    "가래요 — boshqa odam “bor” dedi; 갈래요 — butunlay "
                    "boshqa qolip (“men boraman”)",
                    "가래요 oʻtgan zamon, 갈래요 kelasi zamon",
                    "가래요 rasmiy, 갈래요 norasmiy"],
        "correct": "가래요 — boshqa odam “bor” dedi; 갈래요 — butunlay "
                   "boshqa qolip (“men boraman”)",
        "explanation": "<p>Farqi bitta <strong>ㄹ</strong> da. 가래요 = "
                       "가라고 해요. 갈래요 esa koʻchirma gap emas.</p>",
    },
    {
        "text": "<p>Qaysi vaziyatda <strong>toʻliq</strong> shakl "
                "(다고 했어요) tabiiyroq?</p>",
        "choices": ["Doʻstlar bilan gaplashganda",
                    "Yozma ishda va rasmiy nutqda",
                    "Telefonda",
                    "Serial koʻrganda"],
        "correct": "Yozma ishda va rasmiy nutqda",
        "explanation": "<p>Kundalik gapda va tinglashda deyarli faqat "
                       "qisqargan shakl eshitiladi; yozma ishda toʻliq "
                       "shakl xavfsizroq.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>좋는대요</strong> notoʻgʻri?</p>",
        "choices": ["Chunki 좋다 sifat — ㄴ다/는다 olmaydi",
                    "Chunki 좋다 feʼl",
                    "Chunki zamon yoʻq",
                    "Chunki bu soʻroq gap"],
        "correct": "Chunki 좋다 sifat — ㄴ다/는다 olmaydi",
        "explanation": "<p>PK-60 dagi feʼl/sifat farqi qisqargan shaklda "
                       "ham saqlanadi. Toʻgʻrisi — "
                       "<strong>좋대요</strong>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>지영 씨가 내일 가대요.</strong></p>",
        "choices": ["가대요 → 간대요", "가대요 → 가래요",
                    "가대요 → 가재요", "Xato yoʻq"],
        "correct": "가대요 → 간대요",
        "explanation": "<p>Feʼlning ㄴ다 qismi qisqarganda ham qoladi: "
                       "간다고 해요 → <strong>간대요</strong>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>선생님이 일찍 왔래요.</strong></p>",
        "choices": ["왔래요 → 오래요", "왔래요 → 왔대요",
                    "왔래요 → 오재요", "Xato yoʻq"],
        "correct": "왔래요 → 오래요",
        "explanation": "<p>Buyruqda zamon boʻlmaydi (PK-61) — qisqargan "
                       "shaklda ham shunday: <strong>오래요</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Jasur birga ovqatlanaylik deyapti” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["자스루르 씨가 같이 밥을 먹는대요",
                    "자스루르 씨가 같이 밥을 먹으래요",
                    "자스루르 씨가 같이 밥을 먹재요",
                    "자스루르 씨가 같이 밥을 먹냬요"],
        "correct": "자스루르 씨가 같이 밥을 먹재요",
        "explanation": "<p>“Birga qilaylik” — taklif → 자고 해요 → "
                       "<strong>재요</strong>.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 내일 시험 있어요?</p>"
                "<p><strong>나:</strong> (eshitgan gapini yetkazadi) ___</p>",
        "choices": ["시험이 없대요", "시험이 없냬요",
                    "시험이 없래요", "시험이 없재요"],
        "correct": "시험이 없대요",
        "explanation": "<p>Darak gap → <strong>대요</strong>. 없다 sifat "
                       "kabi ishlaydi, shuning uchun 없는대요 emas.</p>",
    },
]


# =====================================================================
# PK-63 — (으)ㄹ 뻔하다
# =====================================================================

Q_PK63 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 뻔했어요</strong> nimani bildiradi?</p>",
        "choices": ["Ish boʻldi va tugadi",
                    "Ish boʻlishiga oz qoldi, lekin boʻlmadi",
                    "Ish albatta boʻladi",
                    "Ish har doim boʻladi"],
        "correct": "Ish boʻlishiga oz qoldi, lekin boʻlmadi",
        "explanation": "<p>넘어질 뻔했어요 = “yiqilayozdim” — lekin "
                       "yiqilmadim. Oʻzbekchada <strong>-(a)yoz-</strong> "
                       "qoʻshimchasi.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi zamonda ishlatiladi?</p>",
        "choices": ["Har doim oʻtgan zamonda", "Har doim hozirgi zamonda",
                    "Har doim kelasi zamonda", "Har uch zamonda"],
        "correct": "Har doim oʻtgan zamonda",
        "explanation": "<p><strong>뻔했어요</strong> — xavf oʻtib ketgan. "
                       "<s>뻔해요</s> deb ishlatilmaydi.</p>",
    },
    {
        "text": "<p><strong>뻔</strong> dan oldin qaysi shakl keladi?</p>",
        "choices": ["(으)ㄴ", "는", "(으)ㄹ", "았/었을"],
        "correct": "(으)ㄹ",
        "explanation": "<p>Ish <strong>boʻlmagan</strong> — shuning uchun "
                       "kelasi aniqlovchisi (으)ㄹ: 넘어질 뻔했어요.</p>",
    },
    {
        "text": "<p>Bu qolip bilan juftlik boʻlib yuradigan ravish "
                "qaysi?</p>",
        "choices": ["벌써", "하마터면", "아직", "가끔"],
        "correct": "하마터면",
        "explanation": "<p><strong>하마터면</strong> — “sal boʻlmasa, oz "
                       "qoldiki”: 하마터면 늦을 뻔했어요.</p>",
    },
    {
        "text": "<p><strong>뻔</strong> soʻzi grammatik jihatdan nima?</p>",
        "choices": ["Feʼl", "Ot", "Sifat", "Ravish"],
        "correct": "Ot",
        "explanation": "<p>Yana bitta <strong>aniqlovchi + ot</strong> "
                       "qurilmasi — PK-52 dagi 것, PK-53 dagi 줄 bilan "
                       "bir oila.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 계단에서 <strong>______</strong> 뻔했어요. "
                "(넘어지다)</p>",
        "choices": ["넘어지는", "넘어진", "넘어질", "넘어졌을"],
        "correct": "넘어질",
        "explanation": "<p>넘어지 da 받침 yoʻq → <strong>ㄹ 뻔</strong>: "
                       "넘어질 뻔했어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 시험에 <strong>______</strong> 뻔했어요. "
                "(늦다)</p>",
        "choices": ["늦을", "늦는", "늦은", "늦었을"],
        "correct": "늦을",
        "explanation": "<p>늦 da 받침 bor → <strong>을 뻔</strong>: "
                       "늦을 뻔했어요.</p>",
    },
    {
        "text": "<p>Toʻldiring: 버스를 <strong>______</strong> 뻔했어요. "
                "(놓치다)</p>",
        "choices": ["놓치는", "놓칠", "놓친", "놓쳤을"],
        "correct": "놓칠",
        "explanation": "<p>놓치 da 받침 yoʻq → <strong>놓칠 뻔했어요</strong> "
                       "— “avtobusni oʻtkazib yuborayozdim”.</p>",
    },
    {
        "text": "<p>“Sal boʻlmasa hamyonimni yoʻqotib qoʻyardim” — qaysi "
                "biri toʻgʻri?</p>",
        "choices": ["하마터면 지갑을 잃어버릴 뻔했어요",
                    "하마터면 지갑을 잃어버렸을 뻔했어요",
                    "하마터면 지갑을 잃어버리는 뻔했어요",
                    "하마터면 지갑을 잃어버릴 뻔해요"],
        "correct": "하마터면 지갑을 잃어버릴 뻔했어요",
        "explanation": "<p>잃어버리다 (PK-58) + (으)ㄹ 뻔했어요. 뻔 dan "
                       "oldin zamon qoʻshimchasi qoʻyilmaydi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 어제 너무 더워서 <strong>______</strong> "
                "뻔했어요. (죽다)</p>",
        "choices": ["죽는", "죽은", "죽을", "죽었을"],
        "correct": "죽을",
        "explanation": "<p>죽 da 받침 bor → 죽을 뻔했어요. Kundalik nutqda "
                       "bu mubolagʻa — oʻzbekchadagi “oʻlay dedim”.</p>",
    },
    {
        "text": "<p><strong>버스를 놓칠 뻔했어요</strong> — avtobusga "
                "mindimmi?</p>",
        "choices": ["Ha, mindim", "Yoʻq, minmadim",
                    "Bilib boʻlmaydi", "Avtobus kelmadi"],
        "correct": "Ha, mindim",
        "explanation": "<p>뻔했어요 = boʻlishiga oz qoldi, lekin "
                       "<strong>boʻlmadi</strong>. Oʻtkazib yubormadim, "
                       "demak mindim.</p>",
    },
    {
        "text": "<p>Toʻldiring: 길이 미끄러워서 <strong>______</strong> "
                "뻔했어요. (다치다)</p>",
        "choices": ["다칠", "다치는", "다친", "다쳤을"],
        "correct": "다칠",
        "explanation": "<p>다치 da 받침 yoʻq → <strong>다칠 뻔했어요</strong> "
                       "— “jarohat olayozdim”.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>늦었어요</strong> / "
                "<strong>늦을 뻔했어요</strong></p>",
        "choices": ["Birinchisida kechikdim, ikkinchisida kechikmadim",
                    "Birinchisida kechikmadim, ikkinchisida kechikdim",
                    "Ikkalasi bir xil",
                    "Birinchisi kelasi zamon"],
        "correct": "Birinchisida kechikdim, ikkinchisida kechikmadim",
        "explanation": "<p>뻔했어요 aytilgan boʻlsa, ish <strong>sodir "
                       "boʻlmagan</strong> — bu qolipning butun "
                       "maʼnosi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>날씨가 좋을 뻔했어요</strong> "
                "notoʻgʻri?</p>",
        "choices": ["Zamon xato",
                    "날씨 ega boʻlolmaydi",
                    "좋다 — sifat, 뻔하다 esa hodisa haqida",
                    "받침 xato"],
        "correct": "좋다 — sifat, 뻔하다 esa hodisa haqida",
        "explanation": "<p>뻔하다 boʻlishi mumkin boʻlgan <strong>hodisa"
                       "</strong> haqida gapiradi, holat haqida emas.</p>",
    },
    {
        "text": "<p>Bu qolip koʻpincha qanday hodisalar haqida?</p>",
        "choices": ["Yoqimli hodisalar", "Kutilgan hodisalar",
                    "Boʻlmagani yaxshi boʻlgan yomon hodisalar",
                    "Har kuni takrorlanadigan hodisalar"],
        "correct": "Boʻlmagani yaxshi boʻlgan yomon hodisalar",
        "explanation": "<p>넘어질, 다칠, 늦을, 잃어버릴 — hammasi xavf. "
                       "Shuning uchun ohangi “omadim bor ekan” degan "
                       "yengillik beradi.</p>",
    },
    {
        "text": "<p>Qaysi qatorda ikkalasi ham toʻgʻri yasalgan?</p>",
        "choices": ["넘어질 뻔했어요 / 늦을 뻔했어요",
                    "넘어졌을 뻔했어요 / 늦었을 뻔했어요",
                    "넘어지는 뻔했어요 / 늦는 뻔했어요",
                    "넘어질 뻔해요 / 늦을 뻔해요"],
        "correct": "넘어질 뻔했어요 / 늦을 뻔했어요",
        "explanation": "<p>Ikki shart: 뻔 dan oldin <strong>(으)ㄹ</strong>, "
                       "va oxiri <strong>뻔했어요</strong> (oʻtgan "
                       "zamon).</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>계단에서 넘어질 뻔해요.</strong></p>",
        "choices": ["뻔해요 → 뻔했어요", "넘어질 → 넘어진",
                    "넘어질 → 넘어지는", "Xato yoʻq"],
        "correct": "뻔해요 → 뻔했어요",
        "explanation": "<p>Bu qolip <strong>doim oʻtgan zamonda</strong> — "
                       "xavf allaqachon oʻtib ketgan.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>지갑을 잃어버렸을 "
                "뻔했어요.</strong></p>",
        "choices": ["잃어버렸을 → 잃어버릴", "뻔했어요 → 뻔해요",
                    "지갑을 → 지갑이", "Xato yoʻq"],
        "correct": "잃어버렸을 → 잃어버릴",
        "explanation": "<p>뻔 dan oldin faqat <strong>(으)ㄹ</strong> "
                       "keladi — ish hali boʻlmagan, shuning uchun zamon "
                       "qoʻshimchasi qoʻyilmaydi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Zinapoyada yiqilayozdim” — qaysi biri toʻgʻri?</p>",
        "choices": ["계단에서 넘어졌어요", "계단에서 넘어질 뻔해요",
                    "계단에서 넘어질 뻔했어요", "계단에서 넘어지는 뻔했어요"],
        "correct": "계단에서 넘어질 뻔했어요",
        "explanation": "<p>넘어지 + ㄹ 뻔 + 했어요. 넘어졌어요 boʻlsa "
                       "haqiqatan yiqilgan boʻlardim.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 왜 이렇게 놀랐어요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["하마터면 다칠 뻔했어요", "하마터면 다쳤을 뻔했어요",
                    "하마터면 다칠 뻔해요", "하마터면 다치는 뻔했어요"],
        "correct": "하마터면 다칠 뻔했어요",
        "explanation": "<p>“Sal boʻlmasa jarohat olardim” — shuning uchun "
                       "hayajonlandim. 하마터면 + (으)ㄹ 뻔했어요 "
                       "juftligi.</p>",
    },
]


# =====================================================================
# PK-64 — (으)ㄹ 테니까
# =====================================================================

Q_PK64 = [
    # 1–5 tanish
    {
        "text": "<p><strong>(으)ㄹ 테니까</strong> qanday sababni "
                "bildiradi?</p>",
        "choices": ["Boʻlib oʻtgan faktga asoslangan sababni",
                    "Soʻzlovchining niyati yoki kuchli taxminiga "
                    "asoslangan sababni",
                    "Obyektiv, ilmiy sababni",
                    "Hech qanday sababni"],
        "correct": "Soʻzlovchining niyati yoki kuchli taxminiga "
                   "asoslangan sababni",
        "explanation": "<p>제가 준비할 테니까… — bu <strong>vaʼda</strong>, "
                       "fakt emas. Shuning uchun (으)니까 bu yerda "
                       "ishlamaydi.</p>",
    },
    {
        "text": "<p>Ega <strong>men</strong> boʻlganda bu qolip nimani "
                "bildiradi?</p>",
        "choices": ["Taxminni", "Niyat va vaʼdani", "Shubhani",
                    "Taqiqni"],
        "correct": "Niyat va vaʼdani",
        "explanation": "<p>제가 도와줄 테니까… — “men yordam beraman, buni "
                       "oʻz zimmamga olaman”.</p>",
    },
    {
        "text": "<p>Ega <strong>boshqa odam yoki narsa</strong> boʻlganda "
                "maʼnosi qanday oʻzgaradi?</p>",
        "choices": ["Kuchli taxminga aylanadi", "Buyruqqa aylanadi",
                    "Taqiqqa aylanadi", "Oʻzgarmaydi"],
        "correct": "Kuchli taxminga aylanadi",
        "explanation": "<p>비가 올 테니까… — “yomgʻir yogʻsa kerak”. "
                       "Bu sizning niyatingiz emas, taxminingiz.</p>",
    },
    {
        "text": "<p>Bu qolipdan keyin odatda qanday gap keladi?</p>",
        "choices": ["Oddiy oʻtgan zamon darak gapi",
                    "Buyruq yoki taklif",
                    "Soʻroq gap",
                    "Koʻchirma gap"],
        "correct": "Buyruq yoki taklif",
        "explanation": "<p>제가 갈 테니까 <strong>기다리세요</strong> — siz "
                       "suhbatdoshdan biror ish qilishini kutyapsiz.</p>",
    },
    {
        "text": "<p><strong>테</strong> qaysi soʻzdan kelib chiqqan?</p>",
        "choices": ["터 — niyat, reja", "테이블 — stol", "때 — vaqt",
                    "탓 — ayb"],
        "correct": "터 — niyat, reja",
        "explanation": "<p>Shuning uchun bu ham <strong>aniqlovchi + ot"
                       "</strong> qurilmasi: 것 · 줄 · 뻔 · 테 — bitta "
                       "oila.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 제가 <strong>______</strong> 테니까 "
                "걱정하지 마세요. (준비하다)</p>",
        "choices": ["준비하는", "준비할", "준비한", "준비했을"],
        "correct": "준비할",
        "explanation": "<p>하 da 받침 yoʻq → <strong>ㄹ 테니까</strong>: "
                       "준비할 테니까.</p>",
    },
    {
        "text": "<p>Toʻldiring: 제가 <strong>______</strong> 테니까 "
                "기다리세요. (먹다)</p>",
        "choices": ["먹를", "먹을", "먹는", "먹은"],
        "correct": "먹을",
        "explanation": "<p>먹 da 받침 bor → <strong>을 테니까</strong>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 밖에 비가 <strong>______</strong> 테니까 "
                "우산을 가져가세요. (오다)</p>",
        "choices": ["오는", "온", "올", "왔을"],
        "correct": "올",
        "explanation": "<p>오 da 받침 yoʻq → <strong>올 테니까</strong>. "
                       "Bu yerda maʼnosi taxmin: “yomgʻir yogʻsa "
                       "kerak”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 자스루르 씨가 <strong>______</strong> "
                "테니까 나중에 전화하세요. (바쁘다)</p>",
        "choices": ["바쁠", "바쁜", "바쁘는", "바빴을"],
        "correct": "바쁠",
        "explanation": "<p>바쁘 da 받침 yoʻq → <strong>바쁠 테니까</strong>. "
                       "Sifat bilan ham ishlaydi — taxmin maʼnosida.</p>",
    },
    {
        "text": "<p>“Jiyon allaqachon ketgan boʻlsa kerak” — qaysi biri "
                "toʻgʻri?</p>",
        "choices": ["지영 씨가 벌써 갈 테니까", "지영 씨가 벌써 갔을 테니까",
                    "지영 씨가 벌써 가는 테니까", "지영 씨가 벌써 간 테니까"],
        "correct": "지영 씨가 벌써 갔을 테니까",
        "explanation": "<p>Oʻtgan zamon — <strong>았/었을 테니까</strong>.</p>",
    },
    {
        "text": "<p>Bu gapni tugating: 제가 표를 살 테니까 …</p>",
        "choices": ["자스루르 씨는 음식을 사세요",
                    "제가 음식도 샀어요",
                    "표가 비쌌어요",
                    "저는 집에 있었어요"],
        "correct": "자스루르 씨는 음식을 사세요",
        "explanation": "<p>Keyingi gapda <strong>buyruq yoki taklif</strong> "
                       "keladi, va uning egasi <strong>boshqa odam</strong> "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 제가 <strong>______</strong> 테니까 같이 "
                "해요. (도와주다)</p>",
        "choices": ["도와주는", "도와준", "도와줄", "도와줬을"],
        "correct": "도와줄",
        "explanation": "<p>도와주 da 받침 yoʻq → <strong>도와줄 "
                       "테니까</strong> — “men yordam beraman”.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Farqi nimada? <strong>비가 오니까</strong> / "
                "<strong>비가 올 테니까</strong></p>",
        "choices": ["Birinchisi — yomgʻir hozir yogʻyapti (fakt); "
                    "ikkinchisi — yogʻsa kerak (taxmin)",
                    "Birinchisi taxmin, ikkinchisi fakt",
                    "Ikkalasi bir xil",
                    "Birinchisi kelasi zamon"],
        "correct": "Birinchisi — yomgʻir hozir yogʻyapti (fakt); "
                   "ikkinchisi — yogʻsa kerak (taxmin)",
        "explanation": "<p>(으)니까 boʻlib oʻtgan yoki koʻrinib turgan "
                       "narsaga tayanadi; (으)ㄹ 테니까 hali "
                       "boʻlmagan narsaga.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>(으)ㄹ 테니까</strong> kerak?</p>",
        "choices": ["Yomgʻir yogʻdi, shuning uchun uyda qoldik",
                    "Men tayyorlayman, shuning uchun xavotir olmang",
                    "Kasal boʻlganim uchun bora olmadim",
                    "Imtihon qiyin boʻlgani uchun charchadim"],
        "correct": "Men tayyorlayman, shuning uchun xavotir olmang",
        "explanation": "<p>Bu <strong>vaʼda</strong> — hali qilinmagan ish. "
                       "Qolgan uchtasi boʻlib oʻtgan fakt, ular "
                       "(으)니까 / 기 때문에 oladi.</p>",
    },
    {
        "text": "<p>Nima uchun <strong>제가 갈 테니까 제가 표를 사요</strong> "
                "gʻalati?</p>",
        "choices": ["Chunki zamon xato",
                    "Chunki 표 toʻldiruvchi boʻlolmaydi",
                    "Chunki keyingi gapning egasi boshqa odam boʻlishi "
                    "kerak",
                    "Chunki 갈 emas, 가는 kerak"],
        "correct": "Chunki keyingi gapning egasi boshqa odam boʻlishi "
                   "kerak",
        "explanation": "<p>“Men qilaman, shuning uchun <em>men</em>…” "
                       "mantiqan boʻsh. Bu qolip suhbatdoshdan ish "
                       "kutadi.</p>",
    },
    {
        "text": "<p>Qaysi qolip boʻlib oʻtgan obyektiv sabab uchun "
                "ishlatiladi?</p>",
        "choices": ["기 때문에", "(으)ㄹ 테니까", "(으)ㄹ 뻔하다",
                    "자고 하다"],
        "correct": "기 때문에",
        "explanation": "<p>기 때문에 (PK-49) — obyektiv sabab, koʻpincha "
                       "darak gap bilan. (으)ㄹ 테니까 esa niyat yoki "
                       "taxmin + buyruq/taklif.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <strong>제가 준비하니까 걱정하지 "
                "마세요.</strong></p>",
        "choices": ["준비하니까 → 준비할 테니까", "준비하니까 → 준비했으니까",
                    "걱정하지 마세요 → 걱정했어요", "Xato yoʻq"],
        "correct": "준비하니까 → 준비할 테니까",
        "explanation": "<p>Hali tayyorlamadingiz — bu <strong>vaʼda"
                       "</strong>. (으)니까 boʻlib oʻtgan narsa "
                       "uchun.</p>",
    },
    {
        "text": "<p>Xatoni toping: <strong>비가 올 테니까 집에 "
                "있었어요.</strong></p>",
        "choices": ["올 테니까 → 왔으니까", "올 테니까 → 오는 테니까",
                    "있었어요 → 있을 테니까", "Xato yoʻq"],
        "correct": "올 테니까 → 왔으니까",
        "explanation": "<p>(으)ㄹ 테니까 dan keyin oʻtgan zamon darak gapi "
                       "kelmaydi. Boʻlib oʻtgan ish uchun "
                       "<strong>왔으니까</strong>.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>“Men yordam beraman, shuning uchun birga qilaylik” — "
                "qaysi biri toʻgʻri?</p>",
        "choices": ["제가 도와주니까 같이 해요",
                    "제가 도와줄 테니까 같이 해요",
                    "제가 도와줄 뻔했으니까 같이 해요",
                    "제가 도와주기 때문에 같이 해요"],
        "correct": "제가 도와줄 테니까 같이 해요",
        "explanation": "<p>Vaʼda + taklif — aynan <strong>(으)ㄹ "
                       "테니까</strong> ning oʻrni.</p>",
    },
    {
        "text": "<p><strong>가:</strong> 축제 준비를 어떻게 해요?</p>"
                "<p><strong>나:</strong> ___</p>",
        "choices": ["제가 음식을 맡을 테니까 아프소나 씨는 사진을 맡으세요",
                    "제가 음식을 맡으니까 제가 사진도 맡아요",
                    "제가 음식을 맡을 테니까 제가 사진도 맡을 테니까",
                    "제가 음식을 맡았을 테니까 사진을 맡았어요"],
        "correct": "제가 음식을 맡을 테니까 아프소나 씨는 사진을 맡으세요",
        "explanation": "<p>Vaʼda + <strong>boshqa odamga</strong> qaratilgan "
                       "buyruq — qolipning ikkala sharti ham "
                       "bajarilgan.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-62 Mashq: -대요 / -냬요 / -래요 / -재요",
        "description": "20 savol — toʻrtta qisqargan shakl, feʼl/sifat farqi, "
                       "(이)래요 va 가래요 ↔ 갈래요 tuzogʻi.",
        "tutorial":    "PK-62:",
        "level":       "medium",
        "questions":   Q_PK62,
    },
    {
        "title":       "PK-63 Mashq: (으)ㄹ 뻔하다 — “sal boʻlmasa…”",
        "description": "20 savol — 받침 ayrisi, majburiy oʻtgan zamon, "
                       "하마터면 juftligi va nima uchun ish sodir boʻlmagani.",
        "tutorial":    "PK-63:",
        "level":       "medium",
        "questions":   Q_PK63,
    },
    {
        "title":       "PK-64 Mashq: (으)ㄹ 테니까 — niyat va taxmin",
        "description": "20 savol — vaʼda va taxmin maʼnolari, keyingi gapdagi "
                       "cheklov, (으)니까 va 기 때문에 dan farqi.",
        "tutorial":    "PK-64:",
        "level":       "medium",
        "questions":   Q_PK64,
    },
]
