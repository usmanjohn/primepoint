# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-9 … PK-11 (birinchi grammatika testlari).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_09_11.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "한국어",
    "description": "Koreys tili — grammatika va yozuv mashqlari",
    "icon":        "bi-translate",
    "color":       "#d97706",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PK-9 — Salomlashish, xayrlashish va oʻzini tanishtirish
# =====================================================================

Q_PK9 = [
    # 1–5 tanish
    {
        "text": "<p><strong>안녕하세요</strong> qachon ishlatiladi?</p>",
        "choices": ["Kunning istalgan paytida", "Faqat ertalab",
                    "Faqat kechqurun", "Faqat birinchi uchrashuvda"],
        "correct": "Kunning istalgan paytida",
        "explanation": "<p>Koreys tilida vaqtga qarab oʻzgaradigan alohida salom "
                       "<strong>yoʻq</strong>. 안녕하세요 ertalab ham, kechqurun ham, "
                       "birinchi marta koʻrganda ham ishlaydi.</p>",
    },
    {
        "text": "<p><strong>감사합니다</strong> nima degani?</p>",
        "choices": ["Rahmat", "Kechirasiz", "Xayr", "Xush kelibsiz"],
        "correct": "Rahmat",
        "explanation": "<p><strong>감사합니다</strong> — “rahmat”. Kechirasiz — 죄송합니다, "
                       "xayr — 안녕히 계세요/가세요, xush kelibsiz — 어서 오세요.</p>",
    },
    {
        "text": "<p><strong>네</strong> va <strong>아니요</strong> nima degani?</p>",
        "choices": ["Ha va yoʻq", "Salom va xayr", "Rahmat va kechirasiz",
                    "Men va sen"],
        "correct": "Ha va yoʻq",
        "explanation": "<p><strong>네</strong> — “ha” (kundalik nutqda <em>예</em> ham "
                       "aytiladi), <strong>아니요</strong> — “yoʻq”. Koreyslar 네 ni "
                       "koʻpincha “eshityapman, davom eting” maʼnosida ham ishlatadi.</p>",
    },
    {
        "text": "<p><strong>만나서 반갑습니다</strong> nima degani?</p>",
        "choices": ["Tanishganimdan xursandman", "Yaxshi yeyman",
                    "Xayrli tun", "Uzr, ijozat"],
        "correct": "Tanishganimdan xursandman",
        "explanation": "<p>Soʻzma-soʻz “uchrashib, xursandman”. Tanishuvda oʻzini "
                       "tanishtirgandan keyin aytiladi.</p>",
    },
    {
        "text": "<p><strong>어서 오세요</strong> ni odatda kim aytadi?</p>",
        "choices": ["Doʻkonda sotuvchi mijozga", "Mijoz sotuvchiga",
                    "Ketayotgan odam qolayotganga", "Oʻquvchi oʻqituvchiga"],
        "correct": "Doʻkonda sotuvchi mijozga",
        "explanation": "<p><strong>어서 오세요</strong> — “xush kelibsiz”. Doʻkonga yoki "
                       "restoranga kirganingizda sizga aytiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Kafedan chiqib ketyapsiz. Ofitsiantga nima deysiz?</p>",
        "choices": ["안녕히 계세요", "안녕히 가세요", "어서 오세요", "잘 부탁합니다"],
        "correct": "안녕히 계세요",
        "explanation": "<p><strong>안녕히 계세요</strong> — “tinchlikda qoling”. Ofitsiant "
                       "kafeda qoladi, ketayotgan siz. Oyoqqa qarang: kimning oyogʻi "
                       "harakatlanmoqda?</p>",
    },
    {
        "text": "<p>Mehmoningiz uyingizdan ketyapti. Unga nima deysiz?</p>",
        "choices": ["안녕히 가세요", "안녕히 계세요", "잘 먹었습니다", "실례합니다"],
        "correct": "안녕히 가세요",
        "explanation": "<p><strong>안녕히 가세요</strong> — “tinchlikda boring”. Bu safar "
                       "siz qolasiz, mehmon ketadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>가: 안녕히 가세요.<br>나: 네, ___</strong></p>",
        "choices": ["안녕히 계세요.", "안녕히 가세요.", "어서 오세요.", "감사합니다만."],
        "correct": "안녕히 계세요.",
        "explanation": "<p>Birinchi kishi “boring” dedi — demak <em>u</em> qolyapti va "
                       "<em>siz</em> ketyapsiz. Shuning uchun siz unga “qoling” — "
                       "<strong>안녕히 계세요</strong> deysiz.</p>",
    },
    {
        "text": "<p>Ovqatdan <strong>oldin</strong> nima deyiladi?</p>",
        "choices": ["잘 먹겠습니다", "잘 먹었습니다", "수고하셨습니다", "안녕히 주무세요"],
        "correct": "잘 먹겠습니다",
        "explanation": "<p><strong>잘 먹겠습니다</strong> — “yaxshi yeyman” (kelasi zamon "
                       "겠). Ovqatdan keyin esa <em>잘 먹었습니다</em> — “yaxshi yedim” "
                       "(oʻtgan zamon 었).</p>",
    },
    {
        "text": "<p>Notanish odamdan yoʻl soʻramoqchisiz. Gapni nima bilan "
                "boshlaysiz?</p>",
        "choices": ["실례합니다", "잘 먹겠습니다", "안녕히 계세요", "어서 오세요"],
        "correct": "실례합니다",
        "explanation": "<p><strong>실례합니다</strong> — “uzr, ijozat”. Notanish odamga gap "
                       "boshlashdan oldin aytiladi.</p>",
    },
    {
        "text": "<p>Tanishuvni yakunlaydigan odob iborasi qaysi?</p>",
        "choices": ["잘 부탁합니다", "잘 먹었습니다", "안녕히 주무세요", "괜찮습니다"],
        "correct": "잘 부탁합니다",
        "explanation": "<p><strong>잘 부탁합니다</strong> — oʻzbekchaga toʻgʻridan-toʻgʻri "
                       "tarjima qilinmaydi: “sizga ishonaman, menga yaxshi qarang”. "
                       "Koreyada tanishuv shu ibora bilan tugamasa, chala qolgandek "
                       "tuyuladi.</p>",
    },
    {
        "text": "<p>Yotishdan oldin nima deyiladi?</p>",
        "choices": ["안녕히 주무세요", "안녕히 계세요", "어서 오세요", "실례합니다"],
        "correct": "안녕히 주무세요",
        "explanation": "<p><strong>안녕히 주무세요</strong> — “xayrli tun”. 주무시다 — "
                       "“uxlamoq” feʼlining hurmatli shakli.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>계세요</strong> va <strong>가세요</strong> ni nima "
                "ajratadi?</p>",
        "choices": ["Kim ketayotgani", "Kunning payti", "Suhbatdoshning yoshi",
                    "Rasmiylik darajasi"],
        "correct": "Kim ketayotgani",
        "explanation": "<p><strong>계세요</strong> = “qoling” (qoladiganga), "
                       "<strong>가세요</strong> = “boring” (ketayotganga). Vaqt yoki yosh "
                       "bunga taʼsir qilmaydi — faqat kimning oyogʻi harakatlanayotgani "
                       "muhim.</p>",
    },
    {
        "text": "<p>Qaysi ibora <em>yaqin doʻstga</em> aytiladi?</p>",
        "choices": ["안녕", "안녕하세요", "안녕히 계세요", "실례합니다"],
        "correct": "안녕",
        "explanation": "<p><strong>안녕</strong> — qisqa, erkin shakl. Faqat yaqin doʻst va "
                       "oʻzingizdan kichiklarga. Notanish yoki kattaroq odamga "
                       "<em>안녕하세요</em> deyiladi.</p>",
    },
    {
        "text": "<p><strong>죄송합니다</strong> va <strong>감사합니다</strong> farqi "
                "nima?</p>",
        "choices": ["Birinchisi kechirim, ikkinchisi rahmat",
                    "Birinchisi rahmat, ikkinchisi kechirim",
                    "Ikkalasi ham rahmat, faqat darajasi boshqa",
                    "Ikkalasi ham salomlashish"],
        "correct": "Birinchisi kechirim, ikkinchisi rahmat",
        "explanation": "<p><strong>죄송합니다</strong> — “kechirasiz” (jiddiy uzr), "
                       "<strong>감사합니다</strong> — “rahmat”. Ikkalasi ham 합니다 bilan "
                       "tugagani uchun [함니다] deb oʻqiladi.</p>",
    },
    {
        "text": "<p><strong>감사합니다</strong> qanday oʻqiladi?</p>",
        "choices": ["[감사함니다]", "[감사합니다]", "[감사한니다]", "[감사감니다]"],
        "correct": "[감사함니다]",
        "explanation": "<p><strong>[감사함니다]</strong> — bu <em>비음화</em>: 받침 ㅂ dan "
                       "keyin ㄴ kelgani uchun ㅂ burun tovushi ㅁ ga aylanadi. Shu qoida "
                       "합니다 bilan tugagan barcha shakllarga tegishli.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["Doʻkondan chiqarkan sotuvchiga: 안녕히 가세요.",
                    "Mehmonni kuzatarkan: 안녕히 가세요.",
                    "Doʻkondan chiqarkan sotuvchiga: 안녕히 계세요.",
                    "Oʻqituvchiga: 안녕하세요?"],
        "correct": "Doʻkondan chiqarkan sotuvchiga: 안녕히 가세요.",
        "explanation": "<p>Sotuvchi doʻkonda <strong>qoladi</strong>, ketayotgan esa siz. "
                       "Shuning uchun unga <strong>안녕히 계세요</strong> (“qoling”) deyish "
                       "kerak, 가세요 emas.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["Notanish kattaroq odamga: 안녕하세요?",
                    "Notanish kattaroq odamga: 안녕?",
                    "Oʻqituvchiga: 안녕!",
                    "Boshliqqa: 안녕, 잘 있어?"],
        "correct": "Notanish kattaroq odamga: 안녕하세요?",
        "explanation": "<p><strong>안녕하세요</strong> — hurmat shakli, notanish va kattaroq "
                       "odamga aynan shu kerak. <em>안녕</em> esa faqat yaqin doʻst va "
                       "kichiklarga.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Tanishuv qaysi tartibda toʻgʻri?</p>",
        "choices": ["안녕하세요? → 저는 아프소나입니다. → 만나서 반갑습니다.",
                    "만나서 반갑습니다. → 안녕하세요? → 저는 아프소나입니다.",
                    "저는 아프소나입니다. → 안녕히 계세요. → 안녕하세요?",
                    "잘 먹겠습니다. → 안녕하세요? → 감사합니다."],
        "correct": "안녕하세요? → 저는 아프소나입니다. → 만나서 반갑습니다.",
        "explanation": "<p>Avval salomlashiladi, keyin oʻzini tanishtiriladi, oxirida "
                       "<strong>만나서 반갑습니다</strong> aytiladi. Koreyada bunga koʻpincha "
                       "<em>잘 부탁합니다</em> ham qoʻshiladi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 안녕하세요? 저는 지영입니다.<br>나: 안녕하세요? "
                "저는 셰르벡입니다. ___</strong></p>",
        "choices": ["만나서 반갑습니다.", "안녕히 가세요.", "잘 먹었습니다.",
                    "어서 오세요."],
        "correct": "만나서 반갑습니다.",
        "explanation": "<p>Ikkalasi ham oʻzini tanishtirdi — endi tabiiy davom "
                       "<strong>만나서 반갑습니다</strong> (“tanishganimdan xursandman”). "
                       "안녕히 가세요 xayrlashish, 어서 오세요 esa kutib olish uchun.</p>",
    },
]


# =====================================================================
# PK-10 — 명사 + 입니다 / 입니까?
# =====================================================================

Q_PK10 = [
    # 1–5 tanish
    {
        "text": "<p><strong>입니다</strong> nima maʼnoni beradi?</p>",
        "choices": ["…dir", "…emas", "…mi?", "…bor"],
        "correct": "…dir",
        "explanation": "<p><strong>입니다</strong> — “…dir”, otni kesimga aylantiradi: "
                       "학생입니다 = “talabaman/talaba”. Inkori — 아닙니다, savoli — "
                       "입니까?</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 학생___.</strong></p>",
        "choices": ["입니다", "입니까", "아닙니다", "있습니다"],
        "correct": "입니다",
        "explanation": "<p><strong>입니다</strong> — darak gap. 저는 학생입니다 = “Men "
                       "talabaman”. 입니까 savol boʻlardi, 아닙니다 esa inkor.</p>",
    },
    {
        "text": "<p><strong>입니다</strong> ni savolga aylantirish uchun nima "
                "qilinadi?</p>",
        "choices": ["다 oʻrniga 까 qoʻyiladi", "Soʻzlar oʻrni almashtiriladi",
                    "Boshiga 뭐 qoʻshiladi", "Oxiriga 요 qoʻshiladi"],
        "correct": "다 oʻrniga 까 qoʻyiladi",
        "explanation": "<p><strong>입니다 → 입니까?</strong> Soʻz tartibi oʻzgarmaydi — xuddi "
                       "oʻzbekchadagi <em>-mi</em> qoʻshimchasi kabi. Ingliz tilidagidek "
                       "soʻzlarni oʻrin almashtirish kerak emas.</p>",
    },
    {
        "text": "<p>Koreys gapida kesim qayerda turadi?</p>",
        "choices": ["Gap oxirida", "Gap boshida", "Egadan keyin darhol",
                    "Toʻldiruvchidan oldin"],
        "correct": "Gap oxirida",
        "explanation": "<p><strong>Gap oxirida</strong> — xuddi oʻzbekchadagidek. "
                       "“Men talabaman” → 저는 학생입니다. Shuning uchun bu qolip oʻzbek "
                       "oʻquvchisi uchun tabiiy tuyuladi.</p>",
    },
    {
        "text": "<p><strong>입니다</strong> qanday oʻqiladi?</p>",
        "choices": ["[임니다]", "[입니다]", "[이니다]", "[입미다]"],
        "correct": "[임니다]",
        "explanation": "<p><strong>[임니다]</strong> — 비음화: ㅂ dan keyin ㄴ kelgani uchun "
                       "ㅂ burun tovushi ㅁ ga aylanadi. Bu shakl har gapingizda "
                       "qatnashadi, shuning uchun hozirdan toʻgʻri odatlaning.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 선생님___.</strong></p>",
        "choices": ["입니다", "가 입니다", "이 입니다", "은 입니다"],
        "correct": "입니다",
        "explanation": "<p><strong>입니다</strong> otga <em>boʻshliqsiz va qoʻshimchasiz</em> "
                       "yopishadi. 받침 bor-yoʻqligi ham ahamiyatsiz — 학생입니다, "
                       "의사입니다, 선생님입니다.</p>",
    },
    {
        "text": "<p>Toʻgʻri shaklni tanlang.</p><p><strong>저는 의사___ 아닙니다.</strong></p>",
        "choices": ["가", "이", "은", "를"],
        "correct": "가",
        "explanation": "<p><strong>가</strong>. 의사 ning oxirgi boʻgʻini 사 — unli bilan "
                       "tugaydi, 받침 yoʻq. 받침 yoʻq boʻlsa <strong>가</strong>, bor boʻlsa "
                       "<strong>이</strong>: 학생<em>이</em> 아닙니다.</p>",
    },
    {
        "text": "<p>Toʻgʻri shaklni tanlang.</p><p><strong>저는 학생___ 아닙니다.</strong></p>",
        "choices": ["이", "가", "는", "도"],
        "correct": "이",
        "explanation": "<p><strong>이</strong>. 학생 받침 (ㅇ) bilan tugaydi, shuning uchun "
                       "<strong>이 아닙니다</strong>. Bu 받침 ayrisi koreys grammatikasining "
                       "eng koʻp takrorlanadigan qoidasi.</p>",
    },
    {
        "text": "<p>“Talabamisiz?” koreyschada qanday boʻladi?</p>",
        "choices": ["학생입니까?", "학생입니다?", "학생 아닙니까?", "학생이 있습니까?"],
        "correct": "학생입니까?",
        "explanation": "<p><strong>학생입니까?</strong> — 입니다 ning 다 si 까 ga almashdi. "
                       "학생입니다? notoʻgʻri: koreyschada savol faqat ohang bilan "
                       "yasalmaydi, shakl oʻzgarishi kerak.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>가: 자수르 씨는 의사입니까?<br>나: 아니요, 의사___ 아닙니다.</strong></p>",
        "choices": ["가", "이", "은", "도"],
        "correct": "가",
        "explanation": "<p><strong>가</strong> — 의사 unli bilan tugaydi. Toʻliq javob: "
                       "<em>아니요, 저는 의사가 아닙니다.</em></p>",
    },
    {
        "text": "<p><strong>씨</strong> ni qanday ishlatish kerak?</p>",
        "choices": ["Boshqa odamning ismidan keyin", "Oʻz ismingizdan keyin",
                    "Har qanday otdan keyin", "Faqat lavozimdan keyin"],
        "correct": "Boshqa odamning ismidan keyin",
        "explanation": "<p><strong>씨</strong> — hurmat qoʻshimchasi, faqat boshqalarga: "
                       "아프소나 씨는 학생입니다. Oʻzingizga qoʻllab boʻlmaydi — "
                       "<em>저는 아프소나입니다</em>, 씨siz.</p>",
    },
    {
        "text": "<p>Bu gapni koreyschaga oʻgiring: “Men shifokor emasman.”</p>",
        "choices": ["저는 의사가 아닙니다.", "저는 의사이 아닙니다.",
                    "저는 아닙니다 의사가.", "의사가 저는 아닙니다."],
        "correct": "저는 의사가 아닙니다.",
        "explanation": "<p><strong>저는 의사가 아닙니다.</strong> Uchta narsa toʻgʻri boʻlishi "
                       "kerak: 저는 (rasmiy “men”), 의사<em>가</em> (unli bilan tugagani "
                       "uchun 가), va kesim <strong>gap oxirida</strong>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>입니다</strong> va <strong>아닙니다</strong> farqi nima?</p>",
        "choices": ["Birinchisi tasdiq, ikkinchisi inkor",
                    "Birinchisi savol, ikkinchisi javob",
                    "Birinchisi rasmiy, ikkinchisi erkin",
                    "Birinchisi hozirgi, ikkinchisi oʻtgan zamon"],
        "correct": "Birinchisi tasdiq, ikkinchisi inkor",
        "explanation": "<p><strong>입니다</strong> = “…dir”, <strong>아닙니다</strong> = "
                       "“…emas”. Diqqat: 아닙니다 dan oldingi ot 이/가 qoʻshimchasini oladi, "
                       "입니다 esa hech qanday qoʻshimcha talab qilmaydi.</p>",
    },
    {
        "text": "<p>Nega 입니다 da 받침 ayrisi yoʻq, 아닙니다 da esa bor?</p>",
        "choices": ["입니다 otga toʻgʻridan-toʻgʻri yopishadi, 아닙니다 esa 이/가 talab qiladi",
                    "입니다 faqat unli bilan tugagan otlarga qoʻshiladi",
                    "아닙니다 eski shakl, shuning uchun",
                    "Ikkalasida ham ayri bor"],
        "correct": "입니다 otga toʻgʻridan-toʻgʻri yopishadi, 아닙니다 esa 이/가 talab qiladi",
        "explanation": "<p><strong>입니다</strong> otning bir qismiga aylanadi, shuning uchun "
                       "hech narsa tanlanmaydi. <strong>아닙니다</strong> esa alohida soʻz va "
                       "undan oldin ega qoʻshimchasi (이/가) turadi — mana shu yerda 받침 "
                       "ayrisi ishlaydi.</p>",
    },
    {
        "text": "<p><strong>저</strong> va <strong>나</strong> farqi nima?</p>",
        "choices": ["저 — kamtar/rasmiy, 나 — oddiy/yaqin",
                    "저 — koʻplik, 나 — birlik",
                    "저 — ayollar uchun, 나 — erkaklar uchun",
                    "Farqi yoʻq"],
        "correct": "저 — kamtar/rasmiy, 나 — oddiy/yaqin",
        "explanation": "<p><strong>저</strong> kattaroq odamga, notanishga, rasmiy vaziyatda; "
                       "<strong>나</strong> yaqin doʻstga va kichiklarga. 입니다 rasmiy shakl "
                       "boʻlgani uchun deyarli har doim <em>저</em> bilan keladi.</p>",
    },
    {
        "text": "<p>Qaysi juftlik mos?</p>",
        "choices": ["저는 … 입니다", "나는 … 입니다", "저는 … 이야", "씨는 … 입니다 (oʻzim haqimda)"],
        "correct": "저는 … 입니다",
        "explanation": "<p>Olmosh va gap oxiri <strong>mos kelishi</strong> kerak. 저 rasmiy "
                       "olmosh, 입니다 rasmiy shakl — ular birga yuradi. "
                       "<em>나는 학생입니다</em> gʻalati chiqadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 아프소나 씨입니다.", "아프소나 씨는 학생입니다.",
                    "저는 아프소나입니다.", "지영 씨는 선생님입니까?"],
        "correct": "저는 아프소나 씨입니다.",
        "explanation": "<p><strong>씨 ni oʻzingizga qoʻllab boʻlmaydi</strong> — oʻzini "
                       "hurmatlash gʻalati eshitiladi. Toʻgʻrisi: "
                       "<em>저는 아프소나입니다</em>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["저는 학생입니다.", "저는 입니다 학생.",
                    "입니다 저는 학생.", "학생 저는 입니다."],
        "correct": "저는 학생입니다.",
        "explanation": "<p>Koreys gapida <strong>kesim har doim oxirida</strong>. "
                       "저는 학생입니다 — “Men talabaman”. Oʻzbekcha soʻz tartibi bilan bir "
                       "xil, shuning uchun buni eslab qolish oson.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>한국 사람 / 저는 / 아닙니다 / 이</strong></p>",
        "choices": ["저는 한국 사람이 아닙니다.", "저는 아닙니다 한국 사람이.",
                    "한국 사람이 저는 아닙니다.", "아닙니다 저는 한국 사람이."],
        "correct": "저는 한국 사람이 아닙니다.",
        "explanation": "<p><strong>저는 한국 사람이 아닙니다.</strong> Ega birinchi, kesim "
                       "oxirgi. 사람 받침 (ㅁ) bilan tugagani uchun <em>이</em> "
                       "ishlatilgan.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 딜노자 씨는 의사입니까?<br>나: ___</strong></p>",
        "choices": ["아니요, 저는 의사가 아닙니다. 학생입니다.",
                    "아니요, 저는 의사이 아닙니다. 학생입니다.",
                    "네, 저는 의사가 아닙니다.",
                    "아니요, 의사입니다."],
        "correct": "아니요, 저는 의사가 아닙니다. 학생입니다.",
        "explanation": "<p>의사 unli bilan tugaydi → <strong>가</strong> 아닙니다. Boshqa "
                       "variantlar mantiqan ham notoʻgʻri: “네, … 아닙니다” (ha, emasman) "
                       "va “아니요, 의사입니다” (yoʻq, shifokorman) oʻzini "
                       "inkor qiladi.</p>",
    },
]


# =====================================================================
# PK-11 — 존댓말 va 반말
# =====================================================================

Q_PK11 = [
    # 1–5 tanish
    {
        "text": "<p><strong>존댓말</strong> nima?</p>",
        "choices": ["Hurmat nutqi", "Yaqin, erkin nutq", "Yozma til",
                    "Qadimgi koreys tili"],
        "correct": "Hurmat nutqi",
        "explanation": "<p><strong>존댓말</strong> — hurmat nutqi (합니다체 va 해요체 birga). "
                       "Uning qarshisi — <em>반말</em>, “yarim nutq”.</p>",
    },
    {
        "text": "<p>Koreys tilida munosabat qayerda koʻrsatiladi?</p>",
        "choices": ["Feʼlning oxirida", "Olmoshda", "Ohangda", "Gap boshida"],
        "correct": "Feʼlning oxirida",
        "explanation": "<p><strong>Feʼlning oxirida.</strong> Oʻzbekchada bu olmoshda ham "
                       "koʻrinadi (<em>siz/sen</em>), koreyschada esa asosiy belgi gap "
                       "oxirida: 먹습니다 / 먹어요 / 먹어.</p>",
    },
    {
        "text": "<p>Uchta amaliy daraja qaysilar?</p>",
        "choices": ["합니다체, 해요체, 반말", "합니다체, 한자체, 반말",
                    "존댓말, 한글, 반말", "해요체, 하다체, 한국체"],
        "correct": "합니다체, 해요체, 반말",
        "explanation": "<p><strong>합니다체</strong> (qat'iy rasmiy) · <strong>해요체</strong> "
                       "(kundalik hurmat) · <strong>반말</strong> (yaqin). Birinchi ikkitasi "
                       "birgalikda 존댓말 deyiladi.</p>",
    },
    {
        "text": "<p>존댓말da “men” qanday aytiladi?</p>",
        "choices": ["저", "나", "내", "우리"],
        "correct": "저",
        "explanation": "<p><strong>저</strong> — kamtar “men”. 반말da esa <em>나</em>. "
                       "“Mening” uchun: 존댓말da 제, 반말da 내.</p>",
    },
    {
        "text": "<p><strong>몇 살이에요?</strong> nima degani?</p>",
        "choices": ["Necha yoshdasiz?", "Ismingiz nima?", "Qayerdansiz?",
                    "Nima ish qilasiz?"],
        "correct": "Necha yoshdasiz?",
        "explanation": "<p><strong>몇 살이에요?</strong> — “Necha yoshdasiz?”. Koreyada bu "
                       "tanishuvda odatiy savol, chunki javobsiz qaysi nutq darajasida "
                       "gapirishni tanlab boʻlmaydi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Oʻqituvchingiz bilan qaysi darajada gapirasiz?</p>",
        "choices": ["존댓말", "반말", "Ikkalasi ham boʻlaveradi",
                    "Yoshiga qarab 반말"],
        "correct": "존댓말",
        "explanation": "<p><strong>존댓말</strong> — oʻqituvchining maqomi yuqori, shuning "
                       "uchun yoshidan qatʼi nazar hurmat nutqi ishlatiladi.</p>",
    },
    {
        "text": "<p>Sizdan bir yosh katta tanishingiz bilan qanday gapirasiz?</p>",
        "choices": ["존댓말 — bir yosh ham farq hisoblanadi",
                    "반말 — bir yosh deyarli tengdosh",
                    "Ikkalasi aralash",
                    "Faqat 합니다체"],
        "correct": "존댓말 — bir yosh ham farq hisoblanadi",
        "explanation": "<p>Koreyada <strong>bir yosh katta odam tengdosh emas</strong>. "
                       "Shuning uchun 존댓말 ishlatiladi. Aynan shu sababdan 몇 살이에요? "
                       "savoli qoʻpollik hisoblanmaydi.</p>",
    },
    {
        "text": "<p>Qaysi daraja “eng xavfsiz tanlov”?</p>",
        "choices": ["해요체", "반말", "합니다체", "Hech qaysi — har doim aniqlash kerak"],
        "correct": "해요체",
        "explanation": "<p><strong>해요체</strong> muloyim, lekin sovuq emas. Rasmiy "
                       "vaziyatda biroz iliq tuyulishi mumkin — kichik kamchilik. "
                       "반말ni notoʻgʻri ishlatish esa <em>qoʻpollik</em>, ya'ni xatosi "
                       "ancha qimmat.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 이름은 벡조드입니다.</strong></p>",
        "choices": ["제", "내", "나", "우리"],
        "correct": "제",
        "explanation": "<p><strong>제</strong> — “mening” ning hurmatli shakli. Gap oxiri "
                       "입니다 (rasmiy) boʻlgani uchun olmosh ham hurmatli boʻlishi kerak. "
                       "<em>내</em> 반말 shakli.</p>",
    },
    {
        "text": "<p>반말ga oʻtish qanday sodir boʻladi?</p>",
        "choices": ["Odatda kattaroq odam taklif qiladi",
                    "Ikki hafta tanishgandan keyin avtomatik",
                    "Kichikroq odam boshlaydi",
                    "Hech qachon oʻtilmaydi"],
        "correct": "Odatda kattaroq odam taklif qiladi",
        "explanation": "<p>Bu <strong>kelishuv</strong>, oʻz-oʻzidan boʻlmaydi. Odatda "
                       "kattaroq yoki maqomi yuqoriroq odam <em>말 놓으세요</em> yoki "
                       "<em>우리 말 놓을까요?</em> deb taklif qiladi.</p>",
    },
    {
        "text": "<p>Koreyada suhbatdoshga qanday murojaat qilinadi?</p>",
        "choices": ["Ism + 씨 yoki lavozim bilan", "당신 soʻzi bilan",
                    "Faqat “너” bilan", "Umuman murojaat qilinmaydi"],
        "correct": "Ism + 씨 yoki lavozim bilan",
        "explanation": "<p><strong>지영 씨</strong>, <strong>선생님</strong>, "
                       "<strong>사장님</strong>. <em>당신</em> soʻzi bor, lekin deyarli "
                       "ishlatilmaydi va koʻpincha qoʻpol tuyuladi.</p>",
    },
    {
        "text": "<p>Doʻkonda xizmatchi mijozga qaysi darajada gapiradi?</p>",
        "choices": ["합니다체 — professional masofa", "반말", "Faqat 해요체",
                    "Mijozning yoshiga qarab 반말"],
        "correct": "합니다체 — professional masofa",
        "explanation": "<p><strong>합니다체</strong> — qat'iy rasmiy daraja, xizmat sohasida "
                       "aynan shu ishlatiladi. Shuning uchun doʻkonda "
                       "<em>어서 오세요, 감사합니다</em> kabi shakllarni eshitasiz.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>합니다체</strong> va <strong>해요체</strong> farqi nima?</p>",
        "choices": ["Birinchisi rasmiyroq va masofali, ikkinchisi iliqroq",
                    "Birinchisi hurmatli, ikkinchisi hurmatsiz",
                    "Birinchisi ogʻzaki, ikkinchisi yozma",
                    "Farqi yoʻq"],
        "correct": "Birinchisi rasmiyroq va masofali, ikkinchisi iliqroq",
        "explanation": "<p>Ikkalasi ham <strong>존댓말</strong> — ikkalasi ham hurmatli. "
                       "합니다체 sovuqroq va professional (yangiliklar, taqdimot), "
                       "해요체 esa muloyim va yaqin (kundalik hayot).</p>",
    },
    {
        "text": "<p>Qaysi juftlik <em>notoʻgʻri</em>?</p>",
        "choices": ["나는 학생입니다", "저는 학생입니다", "나는 학생이야", "제 이름은 …입니다"],
        "correct": "나는 학생입니다",
        "explanation": "<p><strong>나는 학생입니다</strong> — olmosh 반말, gap oxiri esa eng "
                       "rasmiy shakl. Ular mos kelmaydi. Toʻgʻrisi: "
                       "<em>저는 학생입니다</em> yoki <em>나는 학생이야</em>.</p>",
    },
    {
        "text": "<p><strong>저희</strong> va <strong>우리</strong> farqi nima?</p>",
        "choices": ["저희 — hurmatli “biz”, 우리 — oddiy “biz”",
                    "저희 — “ular”, 우리 — “biz”",
                    "저희 — birlik, 우리 — koʻplik",
                    "Farqi yoʻq"],
        "correct": "저희 — hurmatli “biz”, 우리 — oddiy “biz”",
        "explanation": "<p>저 → 저희, 나 → 우리. Rasmiy vaziyatda “bizning kompaniyamiz” "
                       "<strong>저희 회사</strong> deyiladi.</p>",
    },
    {
        "text": "<p>Yaqin tengdosh doʻstingizga qaysi salom mos?</p>",
        "choices": ["안녕", "안녕하세요", "안녕히 계세요", "실례합니다"],
        "correct": "안녕",
        "explanation": "<p><strong>안녕</strong> — 반말 salomi, yaqin tengdosh doʻstga aynan "
                       "shu mos. <em>안녕하세요</em> hurmat shakli boʻlib, yaqin doʻstga "
                       "biroz masofali eshitiladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Yangi ish joyida boshliqqa aytilgan qaysi gap <em>notoʻgʻri</em>?</p>",
        "choices": ["안녕? 나는 딜노자야.", "안녕하세요? 저는 딜노자입니다.",
                    "안녕하세요? 제 이름은 딜노자입니다.", "선생님, 안녕하세요?"],
        "correct": "안녕? 나는 딜노자야.",
        "explanation": "<p>Ikkita xato bor: <strong>안녕</strong> — 반말 salomi, va "
                       "<strong>나는 … 야</strong> ham 반말. Boshliqqa 존댓말 kerak: "
                       "<em>안녕하세요? 저는 딜노자입니다.</em></p>",
    },
    {
        "text": "<p>Qaysi murojaat toʻgʻri?</p>",
        "choices": ["지영 씨는 학생입니까?", "당신은 학생입니까?",
                    "저는 지영 씨입니다.", "너는 학생입니까?"],
        "correct": "지영 씨는 학생입니까?",
        "explanation": "<p><strong>Ism + 씨</strong> — toʻgʻri murojaat. <em>당신</em> "
                       "deyarli ishlatilmaydi; <em>씨</em> ni oʻzingizga qoʻllab boʻlmaydi; "
                       "<em>너</em> esa 반말 olmoshi va 입니까 bilan mos kelmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Notanish kattaroq odamdan yoʻl soʻrayapsiz. Qaysi variant "
                "toʻgʻri?</p>",
        "choices": ["안녕하세요? 실례합니다. 여기가 역입니까?",
                    "안녕? 여기가 역이야?",
                    "당신, 여기가 역입니까?",
                    "야! 여기가 역입니까?"],
        "correct": "안녕하세요? 실례합니다. 여기가 역입니까?",
        "explanation": "<p>Notanish va kattaroq odamga <strong>존댓말</strong>: salom "
                       "안녕하세요, gap boshlash uchun 실례합니다, savol esa rasmiy "
                       "입니까 shaklida.</p>",
    },
    {
        "text": "<p>Bir kunda uch xil odam bilan uchrashdingiz. Qaysi qator "
                "toʻgʻri?</p>",
        "choices": ["oʻqituvchi → 존댓말 · tengdosh doʻst → 반말 · notanish → 존댓말",
                    "oʻqituvchi → 반말 · tengdosh doʻst → 존댓말 · notanish → 반말",
                    "hammasiga 반말",
                    "hammasiga 반말, faqat oʻqituvchiga 존댓말"],
        "correct": "oʻqituvchi → 존댓말 · tengdosh doʻst → 반말 · notanish → 존댓말",
        "explanation": "<p>Maqomi yuqori (oʻqituvchi) va munosabat aniqlanmagan (notanish) "
                       "odamlarga <strong>존댓말</strong>; yaqin tengdosh doʻstga "
                       "<strong>반말</strong>. Bu — PK-11 oʻqish matnidagi Bekzodning "
                       "kuni.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-9 Mashq: Salomlashish, xayrlashish va oʻzini tanishtirish",
        "description": "20 savol — salomlashish iboralari va 계세요/가세요 farqi.",
        "tutorial":    "PK-9:",
        "level":       "easy",
        "questions":   Q_PK9,
    },
    {
        "title":       "PK-10 Mashq: 명사 + 입니다 / 입니까?",
        "description": "20 savol — 입니다, 입니까?, 이/가 아닙니다 va soʻz tartibi.",
        "tutorial":    "PK-10:",
        "level":       "easy",
        "questions":   Q_PK10,
    },
    {
        "title":       "PK-11 Mashq: Nutq darajalari — 존댓말 va 반말",
        "description": "20 savol — uch daraja, kimga qaysi biri va olmoshlar mosligi.",
        "tutorial":    "PK-11:",
        "level":       "easy",
        "questions":   Q_PK11,
    },
]
