# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-12 … PK-14.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_12_14.py --master=prime \\
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
# PK-12 — 은/는 va 이/가
# =====================================================================

Q_PK12 = [
    # 1–5 tanish
    {
        "text": "<p><strong>은/는</strong> qaysi vazifani bajaradi?</p>",
        "choices": ["Mavzuni belgilaydi", "Egani belgilaydi",
                    "Toʻldiruvchini belgilaydi", "Joyni belgilaydi"],
        "correct": "Mavzuni belgilaydi",
        "explanation": "<p><strong>은/는</strong> — mavzu (주제) qoʻshimchasi: “men hozir shu "
                       "narsa haqida gapiryapman”. Ega qoʻshimchasi esa 이/가.</p>",
    },
    {
        "text": "<p><strong>이/가</strong> qaysi vazifani bajaradi?</p>",
        "choices": ["Egani belgilaydi", "Mavzuni belgilaydi",
                    "Egalikni bildiradi", "Vaqtni bildiradi"],
        "correct": "Egani belgilaydi",
        "explanation": "<p><strong>이/가</strong> — ega (주어) qoʻshimchasi. U “kim?” yoki "
                       "“nima?” savoliga javob beradi va koʻpincha yangi maʼlumot "
                       "keltiradi.</p>",
    },
    {
        "text": "<p>받침 bor otga qaysi shakl qoʻshiladi?</p>",
        "choices": ["은 / 이", "는 / 가", "은 / 가", "는 / 이"],
        "correct": "은 / 이",
        "explanation": "<p>받침 <strong>bor</strong> boʻlsa <strong>은</strong> va "
                       "<strong>이</strong>: 학생은, 학생이. 받침 yoʻq boʻlsa 는 va 가: "
                       "저는, 의사가.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저___ 학생입니다.</strong></p>",
        "choices": ["는", "은", "가", "이"],
        "correct": "는",
        "explanation": "<p><strong>는</strong> — 저 unli (ㅓ) bilan tugaydi, 받침 yoʻq. "
                       "Oʻzini tanishtirishda mavzu qoʻshimchasi ishlatiladi.</p>",
    },
    {
        "text": "<p>Oʻzbekchadagi qaysi soʻz <strong>는</strong> ning maʼnosiga eng "
                "yaqin?</p>",
        "choices": ["esa", "ham", "bilan", "uchun"],
        "correct": "esa",
        "explanation": "<p><strong>“esa”</strong> (yoki “…ga kelsak”). 저는 학생입니다 → "
                       "“Men<em>ga kelsak</em>, talabaman”. Bu tuygʻu oʻzbek oʻquvchisida "
                       "allaqachon bor — koreyschada u qoʻshimcha shaklida.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>선생님___ 지영입니다.</strong></p>",
        "choices": ["은", "는", "이", "가"],
        "correct": "은",
        "explanation": "<p><strong>은</strong> — 선생님 받침 (ㅁ) bilan tugaydi. Mavzu "
                       "qoʻshimchasi: “oʻqituvchiga kelsak, u Jiyoung”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>의사___ 아닙니다.</strong></p>",
        "choices": ["가", "이", "는", "은"],
        "correct": "가",
        "explanation": "<p><strong>가</strong>. 아니다 dan oldin har doim <strong>이/가</strong> "
                       "keladi, va 의사 unli bilan tugagani uchun 가 tanlanadi.</p>",
    },
    {
        "text": "<p>“누가 학생입니까?” savoliga qaysi javob toʻgʻri?</p>",
        "choices": ["자수르 씨가 학생입니다.", "자수르 씨는 학생입니다.",
                    "자수르 씨 학생입니다.", "자수르 씨를 학생입니다."],
        "correct": "자수르 씨가 학생입니다.",
        "explanation": "<p>“누가?” (kim?) savoliga javobda <strong>har doim 이/가</strong>, "
                       "chunki javob yangi maʼlumot beradi. 는 ishlatilsa, “Jasurga "
                       "kelsak…” degan maʼno chiqib, savolga javob boʻlmay qoladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>가방___ 있습니다.</strong></p>",
        "choices": ["이", "가", "은", "는"],
        "correct": "이",
        "explanation": "<p><strong>이</strong> — 가방 받침 (ㅇ) bilan tugaydi. Bu yerda "
                       "가방 gapning egasi (“nima bor?”), shuning uchun 이/가.</p>",
    },
    {
        "text": "<p>Qaysi gap ikki narsani <em>qiyoslaydi</em>?</p>",
        "choices": ["자수르 씨는 학생입니다. 딜노자 씨는 선생님입니다.",
                    "자수르 씨가 학생입니다.",
                    "누가 선생님입니까?",
                    "저는 의사가 아닙니다."],
        "correct": "자수르 씨는 학생입니다. 딜노자 씨는 선생님입니다.",
        "explanation": "<p>Ikkala gapda ham <strong>는</strong> ishlatilgan — bu qiyoslash "
                       "belgisi: “Jasur talaba, Dilnoza <em>esa</em> oʻqituvchi”. 는 ning "
                       "ostida har doim “boshqasi boshqacha” degan soya turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joylarga nima tushadi?</p>"
                "<p><strong>저___ 이름___ 벡조드입니다.</strong></p>",
        "choices": ["는 / 이", "는 / 은", "가 / 이", "은 / 이"],
        "correct": "는 / 이",
        "explanation": "<p><strong>저는</strong> (mavzu — “men haqimda”) va "
                       "<strong>이름이</strong> (ega — “ism”). Bitta gapda bitta mavzu va "
                       "bitta ega boʻlishi mutlaqo normal.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>어머니___ 의사입니다.</strong></p>",
        "choices": ["는", "은", "이", "가"],
        "correct": "는",
        "explanation": "<p><strong>는</strong> — 어머니 unli (ㅣ) bilan tugaydi, 받침 yoʻq. "
                       "Mavzu sifatida tanishtirilyapti.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>“지영 씨는 선생님입니다” va “지영 씨가 선생님입니다” farqi nima?</p>",
        "choices": ["Birinchisi Jiyoung haqida maʼlumot beradi, ikkinchisi “kim?” savoliga javob",
                    "Birinchisi savol, ikkinchisi darak gap",
                    "Birinchisi hurmatli, ikkinchisi oddiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi Jiyoung haqida maʼlumot beradi, ikkinchisi “kim?” savoliga javob",
        "explanation": "<p><strong>는</strong> mavzuni belgilaydi — “Jiyoungga kelsak, u "
                       "oʻqituvchi”. <strong>가</strong> esa egani ajratadi — “<em>aynan "
                       "Jiyoung</em> oʻqituvchi”, ya'ni “누가?” savoliga javob.</p>",
    },
    {
        "text": "<p>Qaysi holatda <strong>이/가</strong> ishlatiladi?</p>",
        "choices": ["아니다 dan oldin", "Oʻzini tanishtirganda",
                    "Ikki narsani qiyoslaganda", "Umumiy mavzu koʻrsatilganda"],
        "correct": "아니다 dan oldin",
        "explanation": "<p><strong>아니다 dan oldin har doim 이/가</strong>: 저는 의사가 "
                       "아닙니다. Qolgan uch holat — 은/는 ning vazifasi.</p>",
    },
    {
        "text": "<p>Nega yangi oʻquvchilar hamma joyda 는 ishlatib xato qiladi?</p>",
        "choices": ["Chunki 는 birinchi oʻrganiladi va odat boʻlib qoladi",
                    "Chunki 는 aytish oson",
                    "Chunki 이/가 kam uchraydi",
                    "Chunki 는 har doim toʻgʻri"],
        "correct": "Chunki 는 birinchi oʻrganiladi va odat boʻlib qoladi",
        "explanation": "<p>Natijada har bir gap “…ga kelsak” bilan boshlangandek tuyuladi — "
                       "go'yo har jumlada mavzu almashtirilayotgandek. Yechim: “누가?” "
                       "savoliga javob boʻlsa yoki yangi narsa nomlanayotgan boʻlsa, "
                       "<strong>이/가</strong>.</p>",
    },
    {
        "text": "<p>Qaysi juftlik shakl jihatidan toʻgʻri?</p>",
        "choices": ["책은 / 책이", "책는 / 책가", "책은 / 책가", "책는 / 책이"],
        "correct": "책은 / 책이",
        "explanation": "<p>책 받침 (ㄱ) bilan tugaydi, shuning uchun <strong>은</strong> va "
                       "<strong>이</strong>. Quloq bilan ham tekshirsa boʻladi: “책는” deb "
                       "aytish qiyin, “책은” esa oʻz-oʻzidan chiqadi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 이름은 벡조드입니다.", "저는 이름이 벡조드입니다.",
                    "저는 학생입니다.", "지영 씨가 선생님입니다."],
        "correct": "저는 이름은 벡조드입니다.",
        "explanation": "<p>Bitta gapda <strong>ikkita 는</strong> boʻlmaydi — mavzu bitta. "
                       "Ikkinchi boʻlak ega, shuning uchun 이/가 olishi kerak: "
                       "<em>저는 이름이 벡조드입니다.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["저는 의사가 아닙니다.", "저는 의사는 아닙니다.",
                    "저가 의사가 아닙니다.", "저는 의사이 아닙니다."],
        "correct": "저는 의사가 아닙니다.",
        "explanation": "<p>아니다 dan oldin <strong>이/가</strong>, va 의사 unli bilan "
                       "tugagani uchun <strong>가</strong>. Mavzu esa 저는.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 누가 의사입니까?<br>나: ___</strong></p>",
        "choices": ["아프소나 씨가 의사입니다.", "아프소나 씨는 의사입니다.",
                    "아프소나 씨가 의사가 아닙니다.", "아프소나 씨는 의사입니까?"],
        "correct": "아프소나 씨가 의사입니다.",
        "explanation": "<p>“누가?” savoliga javobda <strong>이/가</strong>. 씨 unli bilan "
                       "tugagani uchun 가.</p>",
    },
    {
        "text": "<p>Ikki odamni qiyoslamoqchisiz: “Jasur talaba, Dilnoza esa oʻqituvchi.” "
                "Qaysi variant toʻgʻri?</p>",
        "choices": ["자수르 씨는 학생입니다. 딜노자 씨는 선생님입니다.",
                    "자수르 씨가 학생입니다. 딜노자 씨가 선생님입니다.",
                    "자수르 씨는 학생입니다. 딜노자 씨가 선생님입니다.",
                    "자수르 씨가 학생입니다. 딜노자 씨는 선생님입니다."],
        "correct": "자수르 씨는 학생입니다. 딜노자 씨는 선생님입니다.",
        "explanation": "<p>Qiyoslashda <strong>ikkala mavzu ham 는</strong> oladi — aynan "
                       "shu “esa” maʼnosini beradi. 이/가 ishlatilsa, qiyoslash emas, “kim?” "
                       "savoliga javob boʻlib qolardi.</p>",
    },
]


# =====================================================================
# PK-13 — 있다 / 없다
# =====================================================================

Q_PK13 = [
    # 1–5 tanish
    {
        "text": "<p><strong>있습니다</strong> nima degani?</p>",
        "choices": ["Bor", "Yoʻq", "…dir", "…emas"],
        "correct": "Bor",
        "explanation": "<p><strong>있습니다</strong> — “bor”. Uning inkori — 없습니다 "
                       "(“yoʻq”). 입니다 (“…dir”) esa butunlay boshqa kesim.</p>",
    },
    {
        "text": "<p><strong>없습니다</strong> qanday oʻqiladi?</p>",
        "choices": ["[업씀니다]", "[없습니다]", "[업습니다]", "[업씁니다]"],
        "correct": "[업씀니다]",
        "explanation": "<p><strong>[업씀니다]</strong>. Uchta qoida birga ishlaydi: 겹받침da "
                       "bittasi oʻqiladi ([업]), keyingi ㅅ qattiqlashadi (경음화), va ㅂ+ㄴ "
                       "birikmasi ㅁ beradi (비음화).</p>",
    },
    {
        "text": "<p>있다/없다 dan oldingi ot qaysi qoʻshimchani oladi?</p>",
        "choices": ["이/가", "은/는", "을/를", "hech qanday"],
        "correct": "이/가",
        "explanation": "<p><strong>이/가</strong> — chunki bu ot gapning <em>egasi</em>: "
                       "“nima bor?” degan savolga javob beradi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>책___ 있습니다.</strong></p>",
        "choices": ["이", "가", "은", "를"],
        "correct": "이",
        "explanation": "<p><strong>이</strong> — 책 받침 (ㄱ) bilan tugaydi. Maʼnosi: “Kitob "
                       "bor”.</p>",
    },
    {
        "text": "<p><strong>계십니다</strong> nima?</p>",
        "choices": ["있다 ning hurmatli shakli", "없다 ning hurmatli shakli",
                    "입니다 ning savol shakli", "Oʻtgan zamon shakli"],
        "correct": "있다 ning hurmatli shakli",
        "explanation": "<p><strong>계시다</strong> — 있다 ning hurmatli shakli va u "
                       "<em>faqat odamlarga</em> nisbatan ishlatiladi: 선생님이 계십니다.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“Menda vaqt yoʻq” ni koreyschaga oʻgiring.</p>",
        "choices": ["저는 시간이 없습니다.", "저는 시간은 없습니다.",
                    "저가 시간이 없습니다.", "저는 시간이 아닙니다."],
        "correct": "저는 시간이 없습니다.",
        "explanation": "<p><strong>저는 시간이 없습니다.</strong> Tuzilma oʻzbekcha bilan bir "
                       "xil: <em>menda</em> (저는) + <em>vaqt</em> (시간이) + <em>yoʻq</em> "
                       "(없습니다).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>저는 친구___ 있습니다.</strong></p>",
        "choices": ["가", "이", "는", "를"],
        "correct": "가",
        "explanation": "<p><strong>가</strong> — 친구 unli (ㅜ) bilan tugaydi. Bu egalik "
                       "tuzilishi: mavzu (저는) + ega (친구가) + kesim (있습니다).</p>",
    },
    {
        "text": "<p>“시간이 있습니까?” savoliga qisqa javob bering (“Yoʻq”).</p>",
        "choices": ["아니요, 없습니다.", "아니요, 아닙니다.",
                    "네, 없습니다.", "아니요, 있습니다."],
        "correct": "아니요, 없습니다.",
        "explanation": "<p><strong>아니요, 없습니다.</strong> Javobda otni takrorlash shart "
                       "emas — koreyschada bu juda tabiiy. 아닙니다 esa 입니다 ning inkori, "
                       "있다 ga tegishli emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>선생님이 ___.</strong> "
                "(“Oʻqituvchi bor”, hurmatli)</p>",
        "choices": ["계십니다", "있습니다", "입니다", "없습니다"],
        "correct": "계십니다",
        "explanation": "<p><strong>계십니다</strong> — hurmatli odam haqida gapirilayotgani "
                       "uchun 있다 oʻrniga 계시다 ishlatiladi.</p>",
    },
    {
        "text": "<p>“Jiyoungda sumka yoʻq” ni koreyschaga oʻgiring.</p>",
        "choices": ["지영 씨는 가방이 없습니다.", "지영 씨가 가방은 없습니다.",
                    "지영 씨는 가방이 아닙니다.", "지영 씨는 가방을 없습니다."],
        "correct": "지영 씨는 가방이 없습니다.",
        "explanation": "<p>Mavzu <strong>지영 씨는</strong>, ega <strong>가방이</strong> "
                       "(받침 ㅇ bilan tugaydi), kesim <strong>없습니다</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>___ 있습니까?</strong> "
                "(“Nima bor?”)</p>",
        "choices": ["무엇이", "무엇은", "누가", "무엇를"],
        "correct": "무엇이",
        "explanation": "<p><strong>무엇이</strong> — “nima” soʻzi ham ega, shuning uchun "
                       "이/가 oladi. 누가 esa “kim?” degani, narsa haqida emas.</p>",
    },
    {
        "text": "<p>Qaysi gap “Savolim bor” degani?</p>",
        "choices": ["저는 질문이 있습니다.", "저는 질문입니다.",
                    "저는 질문이 없습니다.", "질문이 아닙니다."],
        "correct": "저는 질문이 있습니다.",
        "explanation": "<p><strong>저는 질문이 있습니다.</strong> 저는 질문입니다 “Men "
                       "savolman” degan gʻalati maʼno berardi — 입니다 va 있습니다 ni "
                       "aralashtirmang.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><strong>입니다</strong> va <strong>있습니다</strong> farqi nima?</p>",
        "choices": ["입니다 = “…dir”, 있습니다 = “bor”",
                    "입니다 = “bor”, 있습니다 = “…dir”",
                    "Ikkalasi bir xil",
                    "입니다 hurmatli, 있습니다 oddiy"],
        "correct": "입니다 = “…dir”, 있습니다 = “bor”",
        "explanation": "<p><strong>저는 학생입니다</strong> = “Men talabaman”. "
                       "<strong>저는 책이 있습니다</strong> = “Menda kitob bor”. Ikki boshqa "
                       "kesim, ikki boshqa maʼno.</p>",
    },
    {
        "text": "<p>Nega “저는 친구가 있습니다” da ikki xil qoʻshimcha bor?</p>",
        "choices": ["저는 — mavzu, 친구가 — ega", "Ikkalasi ham ega",
                    "저는 — ega, 친구가 — toʻldiruvchi", "Bu xato"],
        "correct": "저는 — mavzu, 친구가 — ega",
        "explanation": "<p>Bu PK-12 dagi farqning amaliy koʻrinishi. 저는 mavzuni belgilaydi "
                       "(“men haqimda”), 친구가 esa egani (“nima bor”). Bitta gapda bitta "
                       "mavzu va bitta ega.</p>",
    },
    {
        "text": "<p>Qaysi gap <em>notoʻgʻri</em>?</p>",
        "choices": ["책이 계십니다.", "선생님이 계십니다.",
                    "책이 있습니다.", "선생님이 있습니다."],
        "correct": "책이 계십니다.",
        "explanation": "<p><strong>계시다 faqat odamlar uchun.</strong> Kitob uchun "
                       "ishlatilsa kulgili chiqadi — toʻgʻrisi <em>책이 있습니다</em>.</p>",
    },
    {
        "text": "<p>“시간은 없습니다” qachon toʻgʻri boʻladi?</p>",
        "choices": ["Qiyoslaganda — masalan “pulim bor, vaqtim esa yoʻq”",
                    "Har doim toʻgʻri",
                    "Hech qachon toʻgʻri emas",
                    "Faqat savolda"],
        "correct": "Qiyoslaganda — masalan “pulim bor, vaqtim esa yoʻq”",
        "explanation": "<p>Odatda 있다/없다 dan oldin <strong>이/가</strong> keladi. Lekin "
                       "gapiruvchi <em>qiyoslayotgan</em> boʻlsa, 은/는 toʻgʻri boʻladi va "
                       "“esa” maʼnosini qoʻshadi. Qoʻshimcha maʼnoni oʻzgartiradi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["저는 친구는 있습니다.", "저는 친구가 있습니다.",
                    "친구가 있습니다.", "저는 시간이 없습니다."],
        "correct": "저는 친구는 있습니다.",
        "explanation": "<p>Bitta gapda <strong>ikkita 는</strong> boʻlmaydi. Ikkinchi boʻlak "
                       "ega, shuning uchun <strong>이/가</strong> olishi kerak: "
                       "<em>저는 친구가 있습니다.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["돈이 없습니다.", "돈을 없습니다.",
                    "돈이 아닙니다.", "돈은 계십니다."],
        "correct": "돈이 없습니다.",
        "explanation": "<p><strong>돈이 없습니다</strong> — “pul yoʻq”. 돈 받침 (ㄴ) bilan "
                       "tugaydi → 이. 아닙니다 bu yerda notoʻgʻri (u 입니다 ning inkori), "
                       "계십니다 esa faqat odamlar uchun.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>있습니다 / 저는 / 가 / 친구</strong></p>",
        "choices": ["저는 친구가 있습니다.", "친구가 저는 있습니다.",
                    "저는 있습니다 친구가.", "있습니다 저는 친구가."],
        "correct": "저는 친구가 있습니다.",
        "explanation": "<p>Mavzu birinchi, ega ikkinchi, <strong>kesim oxirgi</strong> — "
                       "koreys gapida kesim har doim gap oxirida turadi.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 셰르벡 씨는 무엇이 있습니까?<br>나: ___</strong></p>",
        "choices": ["저는 친구가 있습니다.", "저는 친구는 있습니다.",
                    "저는 친구입니다.", "저는 친구가 아닙니다."],
        "correct": "저는 친구가 있습니다.",
        "explanation": "<p>Savol “nima bor?” — javob ham <strong>있습니다</strong> bilan "
                       "berilishi kerak. 저는 친구입니다 “men doʻstman” degan boshqa maʼno "
                       "berardi.</p>",
    },
]


# =====================================================================
# PK-14 — 에 va 에서
# =====================================================================

Q_PK14 = [
    # 1–5 tanish
    {
        "text": "<p>있다/없다 bilan qaysi qoʻshimcha ishlatiladi?</p>",
        "choices": ["에", "에서", "이/가", "을/를"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — istisnosiz. 있다/없다 holatni bildiradi, "
                       "harakatni emas, shuning uchun 에서 emas.</p>",
    },
    {
        "text": "<p><strong>에서</strong> ning ikki maʼnosi qaysi?</p>",
        "choices": ["Harakat joyi va “…dan”", "Holat joyi va vaqt",
                    "Yoʻnalish va egalik", "Egalik va “…dan”"],
        "correct": "Harakat joyi va “…dan”",
        "explanation": "<p><strong>에서</strong>: (1) biror ish bajarilayotgan joy — "
                       "학교에서 공부합니다; (2) kelib chiqish — 우즈베키스탄에서 왔습니다.</p>",
    },
    {
        "text": "<p>Qaysi uchta soʻz <strong>에</strong> olmaydi?</p>",
        "choices": ["오늘, 어제, 내일", "아침, 저녁, 밤",
                    "학교, 집, 교실", "위, 아래, 안"],
        "correct": "오늘, 어제, 내일",
        "explanation": "<p><strong>오늘</strong> (bugun), <strong>어제</strong> (kecha), "
                       "<strong>내일</strong> (ertaga) yolgʻiz ishlatiladi: 오늘 시간이 "
                       "있습니다. Boshqa vaqt soʻzlari esa 에 oladi: 아침<em>에</em>.</p>",
    },
    {
        "text": "<p>Oʻrin soʻzi (안, 위, 앞…) otga nisbatan qayerda turadi?</p>",
        "choices": ["Otdan keyin", "Otdan oldin", "Gap boshida", "Gap oxirida"],
        "correct": "Otdan keyin",
        "explanation": "<p><strong>Otdan keyin</strong>: 가방 <em>안에</em>, 책상 "
                       "<em>위에</em> — xuddi oʻzbekchadagi “sumka ich<b>ida</b>”, “stol "
                       "ust<b>ida</b>” kabi. Ingliz tilida esa teskari.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>교실___ 있습니다.</strong></p>",
        "choices": ["에", "에서", "이", "은"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — kesim 있습니다, demak bu holat. 있다/없다 "
                       "bilan har doim 에.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>“Kitob stol ustida” ni koreyschaga oʻgiring.</p>",
        "choices": ["책이 책상 위에 있습니다.", "책이 위 책상에 있습니다.",
                    "책이 책상 위에서 있습니다.", "책은 책상 위에 입니다."],
        "correct": "책이 책상 위에 있습니다.",
        "explanation": "<p>Oʻrin soʻzi (위) otdan <strong>keyin</strong>, keyin 에, keyin "
                       "있습니다. 에서 notoʻgʻri, chunki bu holat.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><strong>저는 우즈베키스탄___ 왔습니다.</strong></p>",
        "choices": ["에서", "에", "이", "은"],
        "correct": "에서",
        "explanation": "<p><strong>에서</strong> — “…dan”, kelib chiqish maʼnosi. 에 "
                       "ishlatilsa, “Oʻzbekistonga keldim” boʻlib maʼno oʻzgarardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>아침___ 시간이 있습니다.</strong></p>",
        "choices": ["에", "에서", "은", "이"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — vaqtni koʻrsatadi: 아침에 (“ertalab”). "
                       "Faqat 오늘/어제/내일 bu qoʻshimchani olmaydi.</p>",
    },
    {
        "text": "<p>“Pul sumka ichida yoʻq” ni koreyschaga oʻgiring.</p>",
        "choices": ["가방 안에 돈이 없습니다.", "안 가방에 돈이 없습니다.",
                    "가방 안에서 돈이 없습니다.", "가방 안에 돈은 아닙니다."],
        "correct": "가방 안에 돈이 없습니다.",
        "explanation": "<p>Oʻrin soʻzi otdan keyin (<strong>가방 안에</strong>), 없다 bilan "
                       "<strong>에</strong>, va ega <strong>돈이</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>학교___ 갑니다.</strong></p>",
        "choices": ["에", "에서", "이", "은"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — 가다/오다 bilan 에 yoʻnalishni bildiradi: "
                       "“maktab<em>ga</em> boraman”, xuddi oʻzbekcha <em>-ga</em> kabi.</p>",
    },
    {
        "text": "<p>“Oʻqituvchi sinf tashqarisida” ni koreyschaga oʻgiring.</p>",
        "choices": ["선생님은 교실 밖에 계십니다.", "선생님은 밖 교실에 계십니다.",
                    "선생님은 교실 밖에서 계십니다.", "선생님은 교실 밖에 있습니다만."],
        "correct": "선생님은 교실 밖에 계십니다.",
        "explanation": "<p>Oʻrin soʻzi otdan keyin (<strong>교실 밖에</strong>), holat "
                       "boʻlgani uchun <strong>에</strong>, va hurmatli odam boʻlgani uchun "
                       "<strong>계십니다</strong>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>아프소나 씨는 제 옆___ "
                "있습니다.</strong></p>",
        "choices": ["에", "에서", "이", "는"],
        "correct": "에",
        "explanation": "<p><strong>에</strong> — 옆 (yon) oʻrin soʻzi, kesim esa 있습니다. "
                       "“Afsona yonimda”.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>“학교에 있습니다” va “학교에서 공부합니다” farqi nima?</p>",
        "choices": ["Birinchisi holat, ikkinchisi harakat",
                    "Birinchisi harakat, ikkinchisi holat",
                    "Birinchisi hozirgi, ikkinchisi oʻtgan zamon",
                    "Farqi yoʻq"],
        "correct": "Birinchisi holat, ikkinchisi harakat",
        "explanation": "<p><strong>에</strong> = turibman (holat), <strong>에서</strong> = "
                       "ish qilyapman (harakat). Oʻzbekchada ikkalasi ham “maktabda” "
                       "boʻlgani uchun bu chalkashadi.</p>",
    },
    {
        "text": "<p>Nega oʻzbek oʻquvchi 에 va 에서 ni chalkashtiradi?</p>",
        "choices": ["Chunki oʻzbekchada ikkalasi ham “-da”",
                    "Chunki ikkalasi bir xil eshitiladi",
                    "Chunki 에서 kam ishlatiladi",
                    "Chunki 에 faqat vaqt uchun"],
        "correct": "Chunki oʻzbekchada ikkalasi ham “-da”",
        "explanation": "<p>“Maktab<em>da</em>man” va “maktab<em>da</em> oʻqiyman” — oʻzbek "
                       "tili bu farqni belgilamaydi. Yechim: tarjimaga emas, "
                       "<strong>kesimga</strong> qarash.</p>",
    },
    {
        "text": "<p>“우즈베키스탄에 왔습니다” nima degani?</p>",
        "choices": ["Oʻzbekistonga keldim", "Oʻzbekistondan keldim",
                    "Oʻzbekistonda turibman", "Oʻzbekistonda ishlayman"],
        "correct": "Oʻzbekistonga keldim",
        "explanation": "<p><strong>에</strong> 가다/오다 bilan yoʻnalishni bildiradi — "
                       "“…ga”. “…dan keldim” demoqchi boʻlsangiz "
                       "<strong>에서</strong> kerak.</p>",
    },
    {
        "text": "<p>Qaysi gapda <strong>에서</strong> toʻgʻri ishlatilgan?</p>",
        "choices": ["저는 한국에서 왔습니다.", "책이 가방에서 있습니다.",
                    "지영 씨는 교실에서 있습니다.", "아침에서 시간이 있습니다."],
        "correct": "저는 한국에서 왔습니다.",
        "explanation": "<p>Faqat birinchisi toʻgʻri — bu 에서 ning “…dan” maʼnosi. Qolgan "
                       "uchtasida kesim 있습니다 yoki vaqt koʻrsatilgan, ya'ni "
                       "<strong>에</strong> kerak.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["오늘에 시간이 있습니다.", "아침에 시간이 있습니다.",
                    "오늘 시간이 있습니다.", "저녁에 시간이 없습니다."],
        "correct": "오늘에 시간이 있습니다.",
        "explanation": "<p><strong>오늘</strong>, 어제, 내일 — bu uch soʻz <strong>에</strong> "
                       "olmaydi. Toʻgʻrisi: <em>오늘 시간이 있습니다.</em></p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["책이 가방 안에 있습니다.", "책이 안 가방에 있습니다.",
                    "책이 가방에 안 있습니다.", "책이 가방 안에서 있습니다."],
        "correct": "책이 가방 안에 있습니다.",
        "explanation": "<p>Oʻrin soʻzi otdan <strong>keyin</strong> (가방 안에) va 있다 bilan "
                       "<strong>에</strong>. Oʻzbekchadagi “sumka ich<em>ida</em>” tartibi "
                       "bilan bir xil.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
                "<p><strong>있습니다 / 책상 / 가방이 / 아래에</strong></p>",
        "choices": ["가방이 책상 아래에 있습니다.", "책상 아래에 가방이 있습니다만.",
                    "가방이 아래에 책상 있습니다.", "책상 가방이 아래에 있습니다."],
        "correct": "가방이 책상 아래에 있습니다.",
        "explanation": "<p>Ega (가방이) → joy (책상 아래에) → kesim (있습니다). Kesim har doim "
                       "gap oxirida. Ikkinchi variant ham tushunarli, lekin “있습니다만” "
                       "notoʻgʻri shakl.</p>",
    },
    {
        "text": "<p>Suhbatni toʻldiring.</p>"
                "<p><strong>가: 아프소나 씨는 어디에 있습니까?<br>나: ___</strong></p>",
        "choices": ["아프소나 씨는 교실에 있습니다.", "아프소나 씨는 교실에서 있습니다.",
                    "아프소나 씨는 교실에 입니다.", "아프소나 씨는 교실이 있습니다."],
        "correct": "아프소나 씨는 교실에 있습니다.",
        "explanation": "<p>Savol “qayerda?” — javobda joy + <strong>에</strong> + "
                       "<strong>있습니다</strong>. 에서 notoʻgʻri (bu holat, harakat emas), "
                       "교실이 있습니다 esa “sinfxona bor” degan boshqa maʼno berardi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-12 Mashq: 은/는 va 이/가",
        "description": "20 savol — mavzu va ega farqi, 받침 ayrisi va “누가?” qoidasi.",
        "tutorial":    "PK-12:",
        "level":       "easy",
        "questions":   Q_PK12,
    },
    {
        "title":       "PK-13 Mashq: 있다 / 없다 — bor va yoʻq",
        "description": "20 savol — mavjudlik, egalik tuzilishi va 계시다 hurmatli shakli.",
        "tutorial":    "PK-13:",
        "level":       "easy",
        "questions":   Q_PK13,
    },
    {
        "title":       "PK-14 Mashq: 에 va 에서",
        "description": "20 savol — holat va harakat farqi, oʻrin soʻzlari, “…dan” maʼnosi.",
        "tutorial":    "PK-14:",
        "level":       "easy",
        "questions":   Q_PK14,
    },
]
