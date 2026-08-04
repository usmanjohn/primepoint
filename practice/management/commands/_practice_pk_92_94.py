# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-92 … PK-94.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Uchala mashq ham koʻchirma gap oilasini (PK-60, 61, 62) qayta ishga
soladi — 다면서요 va 다니 aynan oʻsha toʻrtlikdan yasalgani uchun
shakl savollari shu bilimni tekshiradi.
PK-94 mashqi 려 oilasini (PK-40 · PK-90 · PK-94) ajratishga alohida
eʼtibor beradi.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_92_94.py --master=prime \\
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
# PK-92 — 다면서요 · 냐면서요
# ══════════════════════════════════════════════════════════════════════
Q_PK92 = [
    # 1–5 tanish
    {
        "text": "<p><b>-다면서요?</b> qanday maʼno beradi?</p>",
        "choices": ["…emish-ku, rostmi? (eshitganini tekshirish)",
                    "…emish-a! (hayrat)",
                    "…deb oʻylagandim",
                    "…ga bogʻliq"],
        "correct": "…emish-ku, rostmi? (eshitganini tekshirish)",
        "explanation": "<p><b>한국에 간다면서요?</b> — “Koreyaga "
                       "borarkansiz-a?” Siz yangilik aytmayapsiz — "
                       "eshitganingizni tekshiryapsiz.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi ikki qismdan qisqargan?</p>",
        "choices": ["-다고 하다 + (으)면",
                    "-다고 하다 + (으)면서",
                    "-다고 하다 + (으)니까",
                    "-다고 하다 + 아/어서"],
        "correct": "-다고 하다 + (으)면서",
        "explanation": "<p>간다고 하<b>면서</b> → 하 tushadi → "
                       "<b>간다면서</b>. PK-39 dagi 면서 va PK-60 dagi "
                       "koʻchirma gap birlashgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>다음 달에 한국에 ___?</b> (가다)</p>",
        "choices": ["가다면서요", "간다면서요", "가는다면서요", "갔다면서요"],
        "correct": "간다면서요",
        "explanation": "<p>Feʼl hozirgi zamonda 받침 ga qarab ㄴ다/는다 "
                       "oladi. 가 da 받침 yoʻq → <b>간다면서요</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>시험이 정말 ___?</b> (어렵다)</p>",
        "choices": ["어렵는다면서요", "어려운다면서요",
                    "어렵다면서요", "어렵라면서요"],
        "correct": "어렵다면서요",
        "explanation": "<p>어렵다 — <b>sifat</b>. Sifat 는다 olmaydi, "
                       "oddiy <b>다</b> qoʻshiladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>그분이 ___?</b> (의사)</p>",
        "choices": ["의사이라면서요", "의사다면서요",
                    "의사라면서요", "의사인다면서요"],
        "correct": "의사라면서요",
        "explanation": "<p>Ot bilan ulagich <b>(이)라</b>. 의사 da 받침 "
                       "yoʻq → <b>라면서요</b>. 받침 bor boʻlsa: "
                       "학생<b>이라면서요</b>.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>어제 시험을 ___? 어땠어요?</b> (보다, oʻtgan zamon)</p>",
        "choices": ["본다면서요", "봤다면서요", "보다면서요", "볼다면서요"],
        "correct": "봤다면서요",
        "explanation": "<p>Oʻtgan zamon → <b>았/었다면서요</b>. 보다 → "
                       "봤다 → 봤다면서요.</p>",
    },
    {
        "text": "<p><b>간대요</b> va <b>간다면서요?</b> farqi nimada?</p>",
        "choices": ["Birinchisi uchinchi odamga xabar berish, ikkinchisi "
                    "gapning egasidan tekshirish",
                    "Birinchisi oʻtgan, ikkinchisi hozirgi zamon",
                    "Birinchisi rasmiy, ikkinchisi norasmiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi uchinchi odamga xabar berish, ikkinchisi "
                   "gapning egasidan tekshirish",
        "explanation": "<p>PK-62 dagi <b>대요</b> — men boshqaga "
                       "aytyapman. PK-92 dagi <b>다면서요?</b> — men "
                       "gapning <b>egasiga</b> qarab tekshiryapman.</p>",
    },
    {
        "text": "<p>Bu gapning maʼnosi nima?</p>"
                "<p><b>공부한다면서 왜 게임을 해요?</b></p>",
        "choices": ["Oʻqiyapsizmi yoki oʻyin oʻynayapsizmi?",
                    "Oʻqiyman deb aytgan edingiz-ku, nega oʻyin "
                    "oʻynayapsiz?",
                    "Oʻqigandan keyin oʻyin oʻynang",
                    "Oʻqish va oʻyin bir xil"],
        "correct": "Oʻqiyman deb aytgan edingiz-ku, nega oʻyin "
                   "oʻynayapsiz?",
        "explanation": "<p>Qolip gap <b>oʻrtasida</b> kelsa, u yumshoq "
                       "<b>taʼna</b> boʻladi: aytilgan gap bajarilmagan. "
                       "Ketidan deyarli doim 왜 bilan savol keladi.</p>",
    },
    {
        "text": "<p><b>-다면서요</b> ning qisqargan shakli qaysi?</p>",
        "choices": ["-다며(요)", "-대요", "-다니", "-다고요"],
        "correct": "-다며(요)",
        "explanation": "<p>Nutqda 면서 koʻpincha <b>며</b> ga qisqaradi. "
                       "간다며요? (hurmat) · 간다며? (반말). Maʼno "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>Toʻrtlikni toʻgʻri joylang: buyruq gapni tekshirish "
                "qanday boʻladi?</p>",
        "choices": ["가다면서요?", "가냐면서요?", "가라면서요?", "가자면서요?"],
        "correct": "가라면서요?",
        "explanation": "<p>PK-61 dagi buyruq koʻchirmasi <b>-라고 하다</b> "
                       "edi → <b>-라면서요?</b> Taklif esa "
                       "<b>-자면서요?</b>, soʻroq — <b>-냐면서요?</b></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["민수가 다음 주에 온다면서요?",
                    "민수가 다음 주에 오다면서요?",
                    "민수가 다음 주에 오는다면서요?",
                    "민수가 다음 주에 와다면서요?"],
        "correct": "민수가 다음 주에 온다면서요?",
        "explanation": "<p>오다 → 온다 → 온다면서요. Qolip uchinchi shaxs "
                       "haqida ham ishlaydi — muhimi, suhbatdosh bu gapni "
                       "bilsin.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi darsdagi toʻrtlikning ikkinchi "
                "yuzi?</p>",
        "choices": ["PK-62 — 대요 / 냬요 / 래요 / 재요",
                    "PK-52 — (으)ㄴ/는/(으)ㄹ 것 같다",
                    "PK-44 — aniqlovchi shakllar",
                    "PK-35 — 아/어서"],
        "correct": "PK-62 — 대요 / 냬요 / 래요 / 재요",
        "explanation": "<p>Bir xil toʻrtlik (다 · 냐 · 라 · 자), ikki xil "
                       "vazifa: PK-62 xabar beradi, PK-92 "
                       "tekshiradi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>한국에 ___? 축하해요!</b></p>",
        "choices": ["간다니", "간다면서요", "간대요", "가려던 참이에요"],
        "correct": "간다면서요",
        "explanation": "<p>Tabriklash uchun avval tasdiqlash kerak — bu "
                       "<b>savol</b>. 다니 undov, javob kutmaydi.</p>",
    },
    {
        "text": "<p>Kimga qarab turib bu qolipni ishlatamiz?</p>",
        "choices": ["Uchinchi odamga — gap egasi yonimizda yoʻq",
                    "Gapning egasiga — men aynan undan eshitgan gapni "
                    "tekshiraman",
                    "Oʻzimga",
                    "Farqi yoʻq"],
        "correct": "Gapning egasiga — men aynan undan eshitgan gapni "
                   "tekshiraman",
        "explanation": "<p>Shuning uchun 다면서요 deyarli doim "
                       "<b>siz/sen</b> haqida. Uchinchi odamga xabar "
                       "berish uchun <b>대요</b> bor.</p>",
    },
    {
        "text": "<p>Qaysi gapda qolip <b>taʼna</b> maʼnosida?</p>",
        "choices": ["한국에 간다면서요? 축하해요!",
                    "일찍 온다면서 왜 이렇게 늦었어요?",
                    "그 식당이 맛있다면서요?",
                    "어제 시험을 봤다면서요?"],
        "correct": "일찍 온다면서 왜 이렇게 늦었어요?",
        "explanation": "<p>Gap <b>oʻrtasida</b> + 왜 bilan savol = taʼna. "
                       "Gap <b>oxirida</b> + 요 = oddiy tasdiqlash.</p>",
    },
    {
        "text": "<p>Qaysi holatda bu qolipni ishlatib boʻlmaydi?</p>",
        "choices": ["Suhbatdosh haqida",
                    "Uchinchi shaxs haqida, suhbatdosh bilsa",
                    "Oʻzim haqimda",
                    "Oʻtgan zamon haqida"],
        "correct": "Oʻzim haqimda",
        "explanation": "<p>❌ 제가 간다면서요. Oʻz rejamni men "
                       "<b>eshitib</b> bilmayman — bilaman. Qolip faqat "
                       "boshqadan eshitilgan gap uchun.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["한국에 간다면서요?",
                    "시험이 어렵는다면서요?",
                    "그분이 의사라면서요?",
                    "어제 갔다면서요?"],
        "correct": "시험이 어렵는다면서요?",
        "explanation": "<p>어렵다 — sifat, 는다 olmaydi. Toʻgʻrisi: "
                       "<b>어렵다면서요</b>?</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["제가 다음 달에 간다면서요.",
                    "그분이 의사이라면서요?",
                    "매일 운동한다면서요?",
                    "시험을 보다면서요?"],
        "correct": "매일 운동한다면서요?",
        "explanation": "<p>Qolganlari: oʻzi haqida (❌), ot bilan "
                       "이라 oʻrniga 라 kerak (의사<b>라</b>면서요), va "
                       "feʼl 다 emas 았/었다 yoki ㄴ다 olishi kerak "
                       "(봤다면서요 / 보다면서요 ❌).</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang.</p>"
                "<p><b>“Kecha imtihon topshiribsiz-a? Qanday oʻtdi?”</b></p>",
        "choices": ["어제 시험을 봤다면서요? 어땠어요?",
                    "어제 시험을 봤다니? 어땠어요?",
                    "어제 시험을 본대요? 어땠어요?",
                    "어제 시험을 보려던 참이었어요? 어땠어요?"],
        "correct": "어제 시험을 봤다면서요? 어땠어요?",
        "explanation": "<p>Eshitilgan gapni egasidan tekshirish + oʻtgan "
                       "zamon → <b>봤다면서요?</b> Ketidan tabiiy savol "
                       "keladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> ___</p>"
                "<p><b>나:</b> 네, 다음 달에 가요. 어떻게 아셨어요?</p>",
        "choices": ["한국에 간다면서요?",
                    "한국에 간다니!",
                    "한국에 가려던 참이었어요?",
                    "한국에 가기에 달렸어요?"],
        "correct": "한국에 간다면서요?",
        "explanation": "<p>Javob “네, 다음 달에 가요” — demak savol "
                       "<b>tasdiqlash</b> boʻlgan. Va “어떻게 아셨어요?” "
                       "gapiruvchi buni <em>eshitgani</em>ni "
                       "koʻrsatadi.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-93 — 다니 · 라니
# ══════════════════════════════════════════════════════════════════════
Q_PK93 = [
    # 1–5 tanish
    {
        "text": "<p><b>-다니</b> qanday maʼno beradi?</p>",
        "choices": ["…emish-a! (hayrat, taajjub)",
                    "…emish-ku, rostmi?",
                    "…deb oʻylagandim",
                    "…dan farqi yoʻq"],
        "correct": "…emish-a! (hayrat, taajjub)",
        "explanation": "<p><b>벌써 겨울이라니!</b> — “Allaqachon qish "
                       "boʻlibdi-ya!” Bu yangilik aytish emas, "
                       "<b>hayrat</b>.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi ikki qismdan qisqargan?</p>",
        "choices": ["-다고 하다 + (으)면서",
                    "-다고 하다 + 니",
                    "-다고 하다 + 아/어서",
                    "-다고 하다 + 지만"],
        "correct": "-다고 하다 + 니",
        "explanation": "<p>끝났다고 하<b>니</b> → 하 tushadi → "
                       "<b>끝났다니</b>. Kechagi 다면서 bilan bir xil "
                       "ildiz, boshqa qoʻshimcha.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>벌써 ___!</b> (겨울)</p>",
        "choices": ["겨울다니", "겨울이다니", "겨울라니", "겨울이라니"],
        "correct": "겨울이라니",
        "explanation": "<p>Ot bilan <b>(이)라니</b>. 겨울 da 받침 (ㄹ) bor "
                       "→ <b>이라니</b>. 받침 yoʻq boʻlsa: "
                       "가수<b>라니</b>!</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이렇게 ___!</b> (어렵다)</p>",
        "choices": ["어렵다니", "어렵는다니", "어려운다니", "어렵이라니"],
        "correct": "어렵다니",
        "explanation": "<p>어렵다 — sifat, oddiy <b>다니</b>. Sifat "
                       "는다 olmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>그 사람이 ___ 정말 기쁘다.</b> (오다)</p>",
        "choices": ["오다니", "온다니", "오는다니", "왔다니"],
        "correct": "온다니",
        "explanation": "<p>Feʼl hozirgi zamonda ㄴ다/는다 oladi. 오 da "
                       "받침 yoʻq → <b>온다니</b>.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>벌써 ___ 믿을 수 없다.</b> (끝나다, oʻtgan zamon)</p>",
        "choices": ["끝난다니", "끝나다니", "끝났다니", "끝날다니"],
        "correct": "끝났다니",
        "explanation": "<p>Oʻtgan zamon → <b>았/었다니</b>. Bu — yozma "
                       "matnning eng tipik shakli: "
                       "<b>…다니 믿을 수 없었다</b>.</p>",
    },
    {
        "text": "<p>Qolip gap <b>oʻrtasida</b> kelsa, ketidan nima "
                "keladi?</p>",
        "choices": ["Buyruq",
                    "His-tuygʻu bildiruvchi kesim: 기쁘다, 놀랍다, "
                    "믿을 수 없다",
                    "Savol soʻzi",
                    "Ot"],
        "correct": "His-tuygʻu bildiruvchi kesim: 기쁘다, 놀랍다, "
                   "믿을 수 없다",
        "explanation": "<p><b>그 사람이 온다니 정말 기쁘다.</b> Hayrat + "
                       "uning izohi. Gap oxirida kelsa esa faqat "
                       "undov boʻladi.</p>",
    },
    {
        "text": "<p><b>제 잘못이라니요?</b> — bu nimani bildiradi?</p>",
        "choices": ["Ayb menda ekanini tan olish",
                    "Eʼtiroz — “Mening aybim deganingiz nimasi?”",
                    "Kechirim soʻrash",
                    "Savol — “Kimning aybi?”"],
        "correct": "Eʼtiroz — “Mening aybim deganingiz nimasi?”",
        "explanation": "<p>Oxiriga <b>요</b> qoʻshilsa, hayrat "
                       "norozilikka aylanadi: suhbatdoshning gapini "
                       "qabul qilmayapman.</p>",
    },
    {
        "text": "<p>Bu qolip faqat yomon yangilik uchunmi?</p>",
        "choices": ["Ha, faqat salbiy holatlarda",
                    "Yoʻq — u faqat “kutmagan edim” deydi, hissiyot turini "
                    "ketidagi soʻz belgilaydi",
                    "Ha, faqat ijobiy holatlarda",
                    "Faqat rasmiy matnlarda"],
        "correct": "Yoʻq — u faqat “kutmagan edim” deydi, hissiyot turini "
                   "ketidagi soʻz belgilaydi",
        "explanation": "<p><b>합격했다니 기쁘다</b> (ijobiy) · "
                       "<b>벌써 갔다니 아쉽다</b> (salbiy). Qolip "
                       "neytral.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["어머니가 글자를 몰랐다니.",
                    "어머니가 글자를 모른다니 몰랐다.",
                    "어머니가 글자를 모르다니.",
                    "어머니가 글자를 몰라다니."],
        "correct": "어머니가 글자를 몰랐다니.",
        "explanation": "<p>Oʻtgan zamondagi kashfiyot → <b>몰랐다니</b>. "
                       "Bu shakl hikoyachining ichki ovozi sifatida gap "
                       "oxirida yolgʻiz tura oladi.</p>",
    },
    {
        "text": "<p>Bu uch qolip bitta ildizdan. Tartibni toʻgʻri "
                "qoʻying:</p>"
                "<p><b>-다고 하다 · -다면서요 · -다니</b></p>",
        "choices": ["xabar berish → tekshirish → hayron qolish",
                    "hayron qolish → xabar berish → tekshirish",
                    "tekshirish → hayron qolish → xabar berish",
                    "Ular bogʻliq emas"],
        "correct": "xabar berish → tekshirish → hayron qolish",
        "explanation": "<p>PK-60 <b>-다고 하다</b> · PK-92 "
                       "<b>-다면서요?</b> · PK-93 <b>-다니!</b> — bir "
                       "koʻchirma gap, uchta vazifa.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>한 사람이 마흔아홉 살에 다시 ___.</b> "
                "(시작하다, oʻtgan zamon)</p>",
        "choices": ["시작한다니", "시작했다니", "시작하다니", "시작이라니"],
        "correct": "시작했다니",
        "explanation": "<p>Ish oʻtgan zamonda sodir boʻlgan va hikoyachi "
                       "buni endi bilib hayron → <b>시작했다니</b>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Ikki qolipning farqi nimada?</p>"
                "<p><b>간다면서요?</b> · <b>간다니!</b></p>",
        "choices": ["Birinchisi savol (javob kutaman), ikkinchisi undov "
                    "(javob kutmayman)",
                    "Birinchisi oʻtgan, ikkinchisi hozirgi zamon",
                    "Birinchisi sifat, ikkinchisi feʼl bilan",
                    "Farqi yoʻq"],
        "correct": "Birinchisi savol (javob kutaman), ikkinchisi undov "
                   "(javob kutmayman)",
        "explanation": "<p>다면서요 — gapning egasiga qarab turibman. "
                       "다니 — hech kimga emas, oʻzimga.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>가:</b> 이제 그만두려고 해요.<br>"
                "<b>나:</b> ___ 거의 다 끝난 것이나 다름없어요.</p>",
        "choices": ["그만둔다면서요?", "그만두다니요!",
                    "그만두려던 참이에요.", "그만두는 셈이에요."],
        "correct": "그만두다니요!",
        "explanation": "<p>Suhbatdoshning qaroriga <b>eʼtiroz</b> "
                       "bildirilyapti → <b>다니요!</b> Ketidan sabab "
                       "keladi.</p>",
    },
    {
        "text": "<p>Qaysi gap tabriklash uchun toʻgʻri?</p>",
        "choices": ["한국에 간다니? 축하해요!",
                    "한국에 간다면서요? 축하해요!",
                    "한국에 간다니요? 축하해요!",
                    "한국에 갈 지경이에요? 축하해요!"],
        "correct": "한국에 간다면서요? 축하해요!",
        "explanation": "<p>Tabriklashdan oldin tasdiqlash kerak — bu "
                       "savol. 다니 javob kutmaydi, 다니요 esa eʼtiroz "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>Oʻzbekchada bu qolipning eng yaqin juftligi qaysi?</p>",
        "choices": ["“…ga bogʻliq”",
                    "“…ibdi-ya! …ekan-a!”",
                    "“…dan farqi yoʻq”",
                    "“…ay deb turibman”"],
        "correct": "“…ibdi-ya! …ekan-a!”",
        "explanation": "<p>Oʻzbekcha <b>-ibdi</b> aynan shu ishni "
                       "qiladi: “men buni oʻzim koʻrmagan edim, endi "
                       "bilib hayron boʻlyapman”. 겨울이라니! = “Qish "
                       "boʻlibdi-ya!”</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["벌써 겨울이라니!",
                    "그 사람이 가다니 기쁘다.",
                    "이렇게 어렵다니!",
                    "벌써 끝났다니 믿을 수 없다."],
        "correct": "그 사람이 가다니 기쁘다.",
        "explanation": "<p>Feʼl hozirgi zamonda ㄴ다/는다 oladi. "
                       "Toʻgʻrisi: <b>간다니</b> 기쁘다.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["시험이 어렵는다니!",
                    "벌써 겨울다니!",
                    "합격했다니 정말 기쁘다.",
                    "그 사람이 오다니 기쁘다."],
        "correct": "합격했다니 정말 기쁘다.",
        "explanation": "<p>Qolganlari: sifat 는다 olmaydi, ot "
                       "<b>(이)라니</b> oladi, feʼl esa ㄴ다/는다 "
                       "oladi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang "
                "(한다체).</p>"
                "<p><b>“Onam ellik yoshida harf oʻrganibdi — ishonib "
                "boʻlmasdi.”</b></p>",
        "choices": ["어머니가 쉰 살에 글자를 배웠다니 믿을 수 없었다.",
                    "어머니가 쉰 살에 글자를 배운다면서 믿을 수 없었다.",
                    "어머니가 쉰 살에 글자를 배우려니 했다.",
                    "어머니가 쉰 살에 글자를 배운 셈이다."],
        "correct": "어머니가 쉰 살에 글자를 배웠다니 믿을 수 없었다.",
        "explanation": "<p>Hayrat + izoh → <b>았/었다니</b> + "
                       "믿을 수 없었다. Bu — 한다체 hikoyaning tayyor "
                       "qolipi.</p>",
    },
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylang.</p>"
                "<p><b>기쁘다 / 그 사람이 / 정말 / 온다니</b></p>",
        "choices": ["그 사람이 온다니 정말 기쁘다.",
                    "정말 기쁘다 그 사람이 온다니.",
                    "온다니 그 사람이 정말 기쁘다.",
                    "그 사람이 정말 기쁘다 온다니."],
        "correct": "그 사람이 온다니 정말 기쁘다.",
        "explanation": "<p>Avval hayratga sabab boʻlgan gap (온다니), "
                       "keyin his (기쁘다). Kesim doim oxirida.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-94 — (으)려니 하다
# ══════════════════════════════════════════════════════════════════════
Q_PK94 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)려니 하다</b> qanday maʼno beradi?</p>",
        "choices": ["…deb oʻylab qoʻyaqolmoq (ichki taxmin)",
                    "…moqchi boʻlmoq (niyat)",
                    "…emish-a! (hayrat)",
                    "…ga bogʻliq"],
        "correct": "…deb oʻylab qoʻyaqolmoq (ichki taxmin)",
        "explanation": "<p><b>그냥 바쁘려니 했다</b> — “shunchaki band "
                       "ekan-da deb oʻylab qoʻyaqoldim”. Taxmin ichda "
                       "qilingan va tekshirilmagan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>답장이 없어서 그냥 ___ 했다.</b> (바쁘다)</p>",
        "choices": ["바쁘으려니", "바쁘려니", "바쁘려고", "바쁜다니"],
        "correct": "바쁘려니",
        "explanation": "<p>바쁘 da 받침 yoʻq → <b>려니</b>. 받침 bor "
                       "boʻlsa 으려니 (늦<b>으려니</b>).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>오늘도 ___ 했다.</b> (늦다)</p>",
        "choices": ["늦려니", "늦으려니", "늦려고", "늦다니"],
        "correct": "늦으려니",
        "explanation": "<p>늦 da 받침 (ㅈ) bor → <b>으려니</b>.</p>",
    },
    {
        "text": "<p><b>그러려니 하다</b> nima degani?</p>",
        "choices": ["Shunday qilishga qaror qilmoq",
                    "Shunday ekan-da deb qoʻyaverish — jahl qilmaslik",
                    "Shunday boʻlishini soʻramoq",
                    "Shunday ekaniga hayron boʻlmoq"],
        "correct": "Shunday ekan-da deb qoʻyaverish — jahl qilmaslik",
        "explanation": "<p><b>그렇다</b> + 려니 하다 → <b>그러려니 하다</b>. "
                       "Koreyslarning eng koʻp aytadigan hayotiy "
                       "maslahati.</p>",
    },
    {
        "text": "<p>Nega <b>그렇다</b> → <b>그러려니</b> boʻladi?</p>",
        "choices": ["ㅎ tushadi — bu ㅎ notoʻgʻri feʼli (PK-47)",
                    "ㅅ tushadi",
                    "ㅂ → 우 boʻladi",
                    "Hech narsa tushmaydi, shunchaki qisqaradi"],
        "correct": "ㅎ tushadi — bu ㅎ notoʻgʻri feʼli (PK-47)",
        "explanation": "<p>그렇 → 그러 + 려니. ❌ 그렇려니 degan shakl "
                       "yoʻq.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Nega bu qolip deyarli doim <b>했다</b> shaklida "
                "keladi?</p>",
        "choices": ["Chunki u faqat oʻtgan zamonda mavjud",
                    "Chunki hikoya qiluvchi haqiqatni allaqachon biladi: "
                    "“shunday deb oʻylagan edim… lekin”",
                    "Chunki u rasmiy uslub",
                    "Chunki 하다 boshqa shakl olmaydi"],
        "correct": "Chunki hikoya qiluvchi haqiqatni allaqachon biladi: "
                   "“shunday deb oʻylagan edim… lekin”",
        "explanation": "<p>Shuning uchun keyingi jumla koʻpincha "
                       "<b>그런데</b> yoki <b>알고 보니</b> bilan "
                       "boshlanadi.</p>",
    },
    {
        "text": "<p>Qolipning ichidagi uchta maʼnodan qaysi biri "
                "<b>notoʻgʻri</b>?</p>",
        "choices": ["Taxmin ichimda qilingan",
                    "Taxmin tekshirilmagan",
                    "Taxmin koʻpincha notoʻgʻri chiqadi",
                    "Taxmin dalilga asoslangan va ovoz chiqarib aytilgan"],
        "correct": "Taxmin dalilga asoslangan va ovoz chiqarib aytilgan",
        "explanation": "<p>Ovoz chiqarib aytiladigan, dalilga asoslangan "
                       "taxmin — <b>(으)ㄹ 것 같다</b> (PK-52). 려니 하다 "
                       "esa hech kim eshitmagan ichki xulosa.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이유는 모른다. 급한 일이 ___ 한다.</b> (있다)</p>",
        "choices": ["있려니", "있으려니", "있다니", "있으면서"],
        "correct": "있으려니",
        "explanation": "<p>있 da 받침 bor → <b>으려니</b>. “Shoshilinch "
                       "ishi bordir deb qoʻyadi” — sababini soʻramasdan "
                       "qilingan taxmin.</p>",
    },
    {
        "text": "<p>Bu gapdan keyin eng tabiiy davomi qaysi?</p>"
                "<p><b>그냥 바쁘려니 했다.</b></p>",
        "choices": ["그런데 휴대폰이 고장 났었다.",
                    "그래서 내일 갈 것이다.",
                    "그리고 열심히 공부했다.",
                    "하지만 나는 학생이다."],
        "correct": "그런데 휴대폰이 고장 났었다.",
        "explanation": "<p>Qolip taxminni bildiradi, keyingi jumla esa "
                       "uning <b>notoʻgʻri</b> chiqqanini koʻrsatadi. "
                       "그런데 / 알고 보니 — shu qolipning tabiiy "
                       "hamrohlari.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>버스가 늦어도 ___.</b></p>",
        "choices": ["그러려니 한다", "그렇려니 한다",
                    "그러다니 한다", "그러려고 한다"],
        "correct": "그러려니 한다",
        "explanation": "<p>ㅎ tushadi → 그러 + 려니. 려<b>고</b> 하다 "
                       "boʻlsa maʼno butunlay oʻzgaradi — “shunday "
                       "qilmoqchiman”.</p>",
    },
    {
        "text": "<p><b>그러려니 해</b> nimani anglatmaydi?</p>",
        "choices": ["Jahl qilma",
                    "Koʻnglingga olma",
                    "Sababini oʻzingdan toʻqima",
                    "Bu ishni albatta bajar"],
        "correct": "Bu ishni albatta bajar",
        "explanation": "<p>Bu — buyruq emas, <b>munosabat</b>. U "
                       "“tushuntirish qoʻshma” degani, “chida” degani "
                       "ham emas.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["처음이려니 했다.",
                    "처음이려고 했다.",
                    "처음으려니 했다.",
                    "처음다니 했다."],
        "correct": "처음이려니 했다.",
        "explanation": "<p>Ot + 이다 → <b>(이)려니</b>: 처음<b>이려니</b> "
                       "했다 — “birinchi marta ekan-da deb "
                       "oʻyladim”.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi biri toʻgʻri?</p>"
                "<p>(a) 내일 비가 오려니 해요.<br>"
                "(b) 내일 비가 올 것 같아요.</p>",
        "choices": ["(a)", "(b)", "Ikkalasi ham", "Hech qaysisi"],
        "correct": "(b)",
        "explanation": "<p>Suhbatdoshga aytilayotgan, dalilga asoslangan "
                       "taxmin → <b>(으)ㄹ 것 같다</b> (PK-52). "
                       "려니 하다 — ichki, tekshirilmagan taxmin, va u "
                       "odatda oʻtgan zamonda hikoya qilinadi.</p>",
    },
    {
        "text": "<p>려 oilasi: qaysi qolip <b>taxmin</b> bildiradi?</p>",
        "choices": ["(으)려고 하다 — PK-40",
                    "(으)려던 참이다 — PK-90",
                    "(으)려니 하다 — PK-94",
                    "Uchalasi ham"],
        "correct": "(으)려니 하다 — PK-94",
        "explanation": "<p>려<b>고</b> 하다 = niyat · 려<b>던 참</b> = "
                       "niyat + ayni payt · 려<b>니</b> 하다 = taxmin. "
                       "려 ning oʻzi hech narsa demaydi — maʼnoni undan "
                       "keyingi qism beradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>지금 막 나가___ 참이었어요.</b></p>",
        "choices": ["려던", "려니", "다니", "면서"],
        "correct": "려던",
        "explanation": "<p>참 dan oldin <b>(으)려던</b> turadi (PK-90). "
                       "려니 esa 하다 bilan yuradi.</p>",
    },
    {
        "text": "<p>Qaysi juftlik toʻgʻri?</p>",
        "choices": ["려고 하다 = taxmin · 려니 하다 = niyat",
                    "려고 하다 = niyat · 려니 하다 = taxmin",
                    "려고 하다 = hayrat · 려니 하다 = niyat",
                    "Ikkalasi ham niyat"],
        "correct": "려고 하다 = niyat · 려니 하다 = taxmin",
        "explanation": "<p>❌ 그냥 바쁘려고 했다 — “band boʻlish” niyat "
                       "emas. Taxmin uchun <b>려니</b>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["그냥 바쁘려니 했다.",
                    "오늘도 늦려니 했다.",
                    "급한 일이 있으려니 한다.",
                    "처음이려니 했다."],
        "correct": "오늘도 늦려니 했다.",
        "explanation": "<p>늦 da 받침 bor → <b>늦으려니</b> 했다.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["세상일은 다 그렇려니 해야 한다.",
                    "세상일은 다 그러려니 해야 한다.",
                    "세상일은 다 그러다니 해야 한다.",
                    "세상일은 다 그러려고 해야 한다."],
        "correct": "세상일은 다 그러려니 해야 한다.",
        "explanation": "<p>ㅎ notoʻgʻri feʼli: 그렇 → <b>그러</b> + 려니 "
                       "(PK-47). 려고 boʻlsa “shunday qilmoqchi boʻlish” "
                       "— butunlay boshqa maʼno.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang "
                "(한다체).</p>"
                "<p><b>“Shunchaki band ekan-da deb oʻylagandim. Bilsam, "
                "telefoni buzilgan ekan.”</b></p>",
        "choices": ["그냥 바쁘려니 했다. 그런데 휴대폰이 고장 났었다.",
                    "그냥 바쁘려고 했다. 그런데 휴대폰이 고장 났었다.",
                    "그냥 바쁘다니 했다. 그런데 휴대폰이 고장 났었다.",
                    "그냥 바쁠 것 같다. 그런데 휴대폰이 고장 났었다."],
        "correct": "그냥 바쁘려니 했다. 그런데 휴대폰이 고장 났었다.",
        "explanation": "<p>Ichki taxmin + uning notoʻgʻri chiqishi — "
                       "qolipning eng tipik ishlatilishi. <b>그냥</b> ham "
                       "uning doimiy hamrohi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy davomi qaysi?</p>"
                "<p><b>버스는 내가 바꿀 수 없다. 그래서 ___</b></p>",
        "choices": ["그러려니 한다.",
                    "그러려던 참이다.",
                    "그렇다니.",
                    "그런다면서요?"],
        "correct": "그러려니 한다.",
        "explanation": "<p>Oʻzgartira olmaydigan narsaga munosabat — "
                       "aynan <b>그러려니 하다</b>. Qolganlari mos "
                       "ravishda niyat, hayrat va tasdiqlash "
                       "qoliplari.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-92 Mashq: 다면서요 · 냐면서요",
        "description": "20 savol — 다고 하 + 면서 qisqarishi, toʻrtlik "
                       "(다·냐·라·자), sifat va ot shakllari, taʼna "
                       "maʼnosi va 대요 dan farqi.",
        "tutorial":    "PK-92:",
        "level":       "medium",
        "questions":   Q_PK92,
    },
    {
        "title":       "PK-93 Mashq: 다니 · 라니",
        "description": "20 savol — hayrat qolipining shakllari, gap "
                       "oxiri va oʻrtasidagi farqi, 다니요 eʼtirozi va "
                       "다면서요 bilan solishtirish.",
        "tutorial":    "PK-93:",
        "level":       "medium",
        "questions":   Q_PK93,
    },
    {
        "title":       "PK-94 Mashq: (으)려니 하다",
        "description": "20 savol — ichki taxmin, 그러려니 하다 iborasi, "
                       "ㅎ notoʻgʻri feʼli va 려 oilasini (려고 · 려던 "
                       "참 · 려니) ajratish.",
        "tutorial":    "PK-94:",
        "level":       "medium",
        "questions":   Q_PK94,
    },
]
