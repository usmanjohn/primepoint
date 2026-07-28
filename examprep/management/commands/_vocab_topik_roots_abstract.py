# -*- coding: utf-8 -*-
"""Vocab bank — 어근 3: mavhum va baho o'zaklari (TOPIK 5-6, 쓰기 54).

心 感 力 化 性 用 定 關 經 制 不 大 小 高 新 — order decade 300-399.
See STYLE_GUIDE_VOCAB.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

ROOTS = [
    {
        "syllable": "심", "hanja": "心", "order": 300,
        "meaning": "yurak — ko‘ngil, diqqat, markaz",
        "note": "<p>Ikki yo‘nalish: <b>ko‘ngil/diqqat</b> (관심, 안심, 조심) va "
                "<b>markaz</b> (중심, 도심).</p>",
    },
    # 감(感) is defined in _vocab_topik_roots_motion.py — 감동 there needs it
    # first, and defining a root twice would let the two copies drift apart.
    {
        "syllable": "력", "hanja": "力", "order": 310,
        "meaning": "kuch — qobiliyat, quvvat",
        "note": "<p>So‘z <b>oxirida</b> «qobiliyat» yasaydi: 능력, 실력, 체력, 매력, 노력. "
                "So‘z boshida <b>역</b> bo‘lib o‘qiladi (역사 emas — u 歷).</p>",
    },
    {
        "syllable": "화", "hanja": "化", "order": 315,
        "meaning": "aylanish — «...lashuv» qo‘shimchasi",
        "note": "<p>Ot + 화 = <b>jarayon</b>: 변화 (o‘zgarish), 고령화 (qarish), "
                "세계화 (globallashuv), 정보화. ⚠️ <b>화(話)</b> = gap (대화, 전화), "
                "<b>화(火)</b> = olov — boshqa o‘zaklar.</p>",
    },
    {
        "syllable": "성", "hanja": "性", "order": 320,
        "meaning": "xususiyat — tabiat, jins",
        "note": "<p>Ot + 성 = <b>xususiyat</b>: 가능성 (imkoniyat), 중요성 (muhimlik), "
                "필요성. Alohida — jins: 남성, 여성. "
                "⚠️ <b>성(成)</b> = amalga oshmoq (성공, 성장) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "용", "hanja": "用", "order": 325,
        "meaning": "ishlatmoq — foydalanish",
        "note": "<p>사용, 이용, 비용, 용도, 활용.</p>",
    },
    {
        "syllable": "정", "hanja": "定", "order": 330,
        "meaning": "belgilamoq — qaror, barqarorlik",
        "note": "<p>결정, 예정, 안정, 특정, 정확. "
                "⚠️ <b>정(政)</b> = siyosat (정부, 정책), <b>정(情)</b> = tuyg‘u (감정).</p>",
    },
    {
        "syllable": "관", "hanja": "關", "order": 335,
        "meaning": "bog‘lanish — aloqa, e’tibor",
        "note": "<p>관계, 관심, 관련, 상관. ⚠️ <b>관(觀)</b> = qaramoq (관광, 관찰) — "
                "boshqa o‘zak, lekin ikkalasi ham TOPIK’da uchraydi.</p>",
    },
    {
        "syllable": "경", "hanja": "經", "order": 340,
        "meaning": "o‘tmoq, boshqarmoq — iqtisod, tajriba",
        "note": "<p>경제, 경험, 경영. ⚠️ <b>경(景)</b> = manzara (풍경, 경치).</p>",
    },
    {
        "syllable": "제", "hanja": "制", "order": 345,
        "meaning": "tartib — tizim, cheklov",
        "note": "<p>제도 (tizim), 규제 (cheklov), 제한 (chegara), 통제. "
                "⚠️ <b>제(製)</b> = yasamoq (제품, 제작), <b>제(題)</b> = mavzu (문제, 주제).</p>",
    },
    {
        "syllable": "불", "hanja": "不", "order": 350,
        "meaning": "inkor — «-siz, no-, be-»",
        "note": "<p>Eng foydali <b>inkor prefiksi</b>: 안전→불안전, 가능→불가능, "
                "편하다→불편하다, 안→불안. Notanish so‘z 불- bilan boshlansa, "
                "qolgan qismining <b>teskarisi</b> deb o‘qing — 읽기 da juda foydali.</p>",
    },
    {
        "syllable": "대", "hanja": "大", "order": 355,
        "meaning": "katta — ulkan",
        "note": "<p>대학, 대회, 대부분, 확대, 대기업.</p>",
    },
    {
        "syllable": "고", "hanja": "高", "order": 360,
        "meaning": "baland — yuqori",
        "note": "<p>고등학교, 최고, 고급, 고령화, 고속. "
                "⚠️ <b>고(古)</b> = qadimiy, <b>고(苦)</b> = azob (고생).</p>",
    },
    {
        "syllable": "신", "hanja": "新", "order": 365,
        "meaning": "yangi",
        "note": "<p>신문 («yangi eshitilgan» → gazeta), 신제품, 신입, 최신. "
                "⚠️ <b>신(信)</b> = ishonch (신뢰), <b>신(身)</b> = tana (신체).</p>",
    },
]

WORDS = [
    # ── 심(心) · 감(感) ────────────────────────────────────────────────────
    {
        "word": "관심", "hanja": "關心", "roots": ["심", "관"],
        "pos": "noun", "topic": "emotion", "level": 3, "freq": 3, "order": 300,
        "meaning": "qiziqish, e’tibor — «bog‘lanish + ko‘ngil»",
        "collocation": "관심이 있다 · 관심을 가지다 · 관심을 끌다",
        "examples": [
            ("저는 환경 문제에 관심이 많아요.", "Men ekologiya masalasiga juda qiziqaman."),
            ("이 주제는 최근 큰 관심을 끌고 있다.", "Bu mavzu so‘nggi paytda katta qiziqish uyg‘otmoqda."),
        ],
        "antonyms": [("무관심", "befarqlik — 無 + 關心")],
    },
    {
        "word": "중심", "hanja": "中心", "roots": ["심"],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 3, "order": 301,
        "meaning": "markaz, o‘zak — «o‘rta + yurak»",
        "collocation": "중심이 되다 · 도시 중심 · 중심 생각",
        "note": "<p><b>읽기 uchun kalit so‘z:</b> savol «중심 생각을 고르십시오» "
                "(asosiy fikrni tanlang) shaklida keladi.</p>",
        "examples": [
            ("이 글의 중심 생각은 무엇입니까?", "Bu matnning asosiy fikri nima?"),
        ],
    },
    {
        "word": "조심", "hanja": "操心", "roots": ["심"],
        "pos": "noun", "topic": "daily", "level": 2, "freq": 2, "order": 302,
        "meaning": "ehtiyot bo‘lish — «boshqarmoq + ko‘ngil»",
        "collocation": "조심하다 · 조심스럽다 · 말조심",
        "examples": [
            ("길이 미끄러우니까 조심하세요.", "Yo‘l sirpanchiq, ehtiyot bo‘ling."),
        ],
    },
    {
        "word": "감정", "hanja": "感情", "roots": ["감"],
        "pos": "noun", "topic": "emotion", "level": 4, "freq": 3, "order": 305,
        "meaning": "his-tuyg‘u — «sezish + tuyg‘u»",
        "collocation": "감정을 표현하다 · 감정적이다 · 감정을 숨기다",
        "examples": [
            ("한국 사람들은 감정을 잘 드러내지 않는 편이다.", "Koreyaliklar tuyg‘ularini kam ochib ko‘rsatadi."),
        ],
        "antonyms": [("이성", "aql, mantiq — tuyg‘uga qarshi qo‘yiladi")],
    },
    {
        "word": "공감", "hanja": "共感", "roots": ["감"],
        "pos": "noun", "topic": "emotion", "level": 5, "freq": 2, "order": 306,
        "meaning": "hamdardlik, bir xil his qilish — «birga + sezish»",
        "collocation": "공감하다 · 공감을 얻다 · 공감 능력",
        "note": "<p>쓰기 54 da munosabat mavzusida kuchli so‘z.</p>",
        "examples": [
            ("그의 말에 많은 사람들이 공감했다.", "Uning gapiga ko‘p odam hamdard bo‘ldi."),
        ],
    },

    # ── 력(力) ─────────────────────────────────────────────────────────────
    {
        "word": "능력", "hanja": "能力", "roots": ["력"],
        "pos": "noun", "topic": "work", "level": 4, "freq": 3, "order": 310,
        "meaning": "qobiliyat, salohiyat",
        "collocation": "능력이 뛰어나다 · 업무 능력 · 능력을 기르다",
        "examples": [
            ("그는 문제를 해결하는 능력이 뛰어나다.", "U muammoni hal qilish qobiliyatiga ega."),
        ],
    },
    {
        "word": "노력", "hanja": "努力", "roots": ["력"],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 311,
        "meaning": "harakat, sa’y-harakat — «tirishmoq + kuch»",
        "collocation": "노력하다 · 노력의 결과 · 꾸준한 노력",
        "note": "<p><b>쓰기 54 xulosasi uchun:</b> "
                "<i>이를 위해서는 모두의 노력이 필요하다.</i></p>",
        "examples": [
            ("노력한 만큼 좋은 결과를 얻었다.", "Harakat qilganim darajasida yaxshi natija oldim."),
        ],
    },
    {
        "word": "실력", "hanja": "實力", "roots": ["력"],
        "pos": "noun", "topic": "school", "level": 3, "freq": 2, "order": 312,
        "meaning": "saviya, amaliy bilim — «haqiqiy + kuch»",
        "collocation": "실력이 늘다 · 한국어 실력 · 실력을 쌓다",
        "examples": [
            ("매일 연습해야 실력이 는다.", "Har kuni mashq qilsangina saviya o‘sadi."),
        ],
    },

    # ── 화(化) · 성(性) ───────────────────────────────────────────────────
    {
        "word": "변화", "hanja": "變化", "roots": ["화"],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 3, "order": 315,
        "meaning": "o‘zgarish — «o‘zgarmoq + aylanish»",
        "collocation": "변화하다 · 급격한 변화 · 기후 변화",
        "note": "<p><b>쓰기 53 uchun asosiy so‘z</b> — grafikdagi o‘zgarishni "
                "shu bilan nomlaysiz.</p>",
        "examples": [
            ("최근 소비 형태에 큰 변화가 나타났다.", "So‘nggi paytda iste’mol shaklida katta o‘zgarish ko‘rindi."),
        ],
    },
    {
        "word": "고령화", "hanja": "高齡化", "roots": ["화", "고"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 316,
        "meaning": "aholining qarishi — «yuqori + yosh + aylanish»",
        "collocation": "고령화 사회 · 고령화가 심각하다",
        "note": "<p><b>쓰기 53 ning eng ko‘p mavzularidan biri</b> — 인구 감소 bilan birga.</p>",
        "examples": [
            ("한국은 빠르게 고령화 사회로 진입하고 있다.", "Koreya tez sur’atda qariyotgan jamiyatga kirmoqda."),
        ],
    },
    {
        "word": "가능성", "hanja": "可能性", "roots": ["성"],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 3, "order": 320,
        "meaning": "imkoniyat, ehtimol — «mumkin + xususiyat»",
        "collocation": "가능성이 높다 · 가능성이 있다 · 발전 가능성",
        "examples": [
            ("이 방법이 성공할 가능성이 높다.", "Bu usulning muvaffaqiyat ehtimoli yuqori."),
        ],
    },
    {
        "word": "중요성", "hanja": "重要性", "roots": ["성"],
        "pos": "noun", "topic": "abstract", "level": 5, "freq": 3, "order": 321,
        "meaning": "muhimlik, ahamiyat",
        "collocation": "중요성을 강조하다 · 교육의 중요성",
        "note": "<p><b>쓰기 54 kirish qismi uchun:</b> "
                "<i>[주제]의 중요성이 점점 커지고 있다.</i></p>",
        "examples": [
            ("환경 보호의 중요성이 점점 커지고 있다.", "Atrof-muhitni muhofaza qilishning ahamiyati tobora ortmoqda."),
        ],
    },

    # ── 용(用) · 정(定) ───────────────────────────────────────────────────
    {
        "word": "사용", "hanja": "使用", "roots": ["용"],
        "pos": "noun", "topic": "daily", "level": 2, "freq": 3, "order": 325,
        "meaning": "ishlatish, foydalanish",
        "collocation": "사용하다 · 사용법 · 사용자",
        "examples": [
            ("이 기계는 사용하기 쉬워요.", "Bu mashinani ishlatish oson."),
        ],
        "synonyms": [("이용", "이용 = xizmat/vositadan foydalanish (지하철을 이용하다); "
                             "사용 = buyumni ishlatish (컴퓨터를 사용하다)")],
    },
    {
        "word": "이용", "hanja": "利用", "roots": ["용"],
        "pos": "noun", "topic": "daily", "level": 3, "freq": 3, "order": 326,
        "meaning": "foydalanish (xizmat, vositadan)",
        "collocation": "이용하다 · 대중교통을 이용하다 · 이용자",
        "examples": [
            ("대중교통을 이용하면 시간을 아낄 수 있다.", "Jamoat transportidan foydalansangiz vaqtni tejaysiz."),
        ],
        "synonyms": [("사용", "사용 = buyum; 이용 = xizmat va imkoniyat")],
    },
    {
        "word": "비용", "hanja": "費用", "roots": ["용"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 327,
        "meaning": "xarajat, sarf-xarajat",
        "collocation": "비용이 들다 · 비용을 줄이다 · 생활비용",
        "examples": [
            ("이 방법은 비용이 적게 든다.", "Bu usulda xarajat kam ketadi."),
        ],
    },
    {
        "word": "결정", "hanja": "決定", "roots": ["정"],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 330,
        "meaning": "qaror qilish",
        "collocation": "결정하다 · 결정을 내리다 · 최종 결정",
        "examples": [
            ("신중하게 결정을 내려야 한다.", "Ehtiyotkorlik bilan qaror qabul qilish kerak."),
        ],
    },
    {
        "word": "안정", "hanja": "安定", "roots": ["정"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 2, "order": 331,
        "meaning": "barqarorlik — «xotirjam + belgilangan»",
        "collocation": "안정되다 · 안정적이다 · 경제 안정",
        "examples": [
            ("물가가 점차 안정되고 있다.", "Narxlar asta-sekin barqarorlashmoqda."),
        ],
        "antonyms": [("불안정", "beqarorlik — 不 + 安定")],
    },

    # ── 관(關) · 경(經) · 제(制) ──────────────────────────────────────────
    {
        "word": "관계", "hanja": "關係", "roots": ["관"],
        "pos": "noun", "topic": "person", "level": 4, "freq": 3, "order": 335,
        "meaning": "munosabat, aloqa",
        "collocation": "관계가 좋다 · 인간관계 · 관계를 맺다",
        "examples": [
            ("두 나라의 관계가 좋아지고 있다.", "Ikki davlat munosabati yaxshilanmoqda."),
        ],
    },
    {
        "word": "경제", "hanja": "經濟", "roots": ["경"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 340,
        "meaning": "iqtisod",
        "collocation": "경제 성장 · 경제적이다 · 경제 위기",
        "examples": [
            ("경제가 어려워지면서 소비가 줄었다.", "Iqtisod og‘irlashgani sari iste’mol kamaydi."),
        ],
    },
    {
        "word": "경험", "hanja": "經驗", "roots": ["경"],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 341,
        "meaning": "tajriba — «o‘tmoq + sinamoq»",
        "collocation": "경험하다 · 경험이 많다 · 사회 경험",
        "examples": [
            ("외국 생활은 좋은 경험이 되었다.", "Chet eldagi hayot yaxshi tajriba bo‘ldi."),
        ],
    },
    {
        "word": "제도", "hanja": "制度", "roots": ["제"],
        "pos": "noun", "topic": "society", "level": 5, "freq": 3, "order": 345,
        "meaning": "tizim, tartib-qoida (rasmiy)",
        "collocation": "제도를 개선하다 · 교육 제도 · 복지 제도",
        "note": "<p><b>쓰기 54 taklif qismi uchun:</b> "
                "<i>이를 위해 제도적 지원이 필요하다.</i></p>",
        "examples": [
            ("교육 제도를 개선할 필요가 있다.", "Ta’lim tizimini takomillashtirish zarur."),
        ],
    },

    # ── 불(不) — inkor prefiksi ───────────────────────────────────────────
    {
        "word": "불편", "hanja": "不便", "roots": ["불"],
        "pos": "adj", "topic": "daily", "level": 2, "freq": 3, "order": 350,
        "meaning": "noqulay — «yo‘q + qulay»",
        "collocation": "불편하다 · 불편을 겪다 · 불편함",
        "note": "<p>편하다 (qulay) + 불 = teskarisi. Shu qoida <b>불</b>li barcha so‘zga tegishli.</p>",
        "examples": [
            ("교통이 불편해서 이사하려고 해요.", "Transport noqulay, shuning uchun ko‘chmoqchiman."),
        ],
        "antonyms": [("편리", "qulay, oson — 不 olib tashlansa teskari ma’no")],
    },
    {
        "word": "불안", "hanja": "不安", "roots": ["불"],
        "pos": "adj", "topic": "emotion", "level": 3, "freq": 2, "order": 351,
        "meaning": "bezovta, xavotirli — «yo‘q + xotirjam»",
        "collocation": "불안하다 · 불안감 · 미래에 대한 불안",
        "examples": [
            ("시험 결과 때문에 불안해요.", "Imtihon natijasi tufayli xavotirdaman."),
        ],
        "antonyms": [("안심", "xotirjamlik")],
    },
    {
        "word": "불가능", "hanja": "不可能", "roots": ["불"],
        "pos": "adj", "topic": "abstract", "level": 4, "freq": 2, "order": 352,
        "meaning": "imkonsiz — «yo‘q + mumkin»",
        "collocation": "불가능하다 · 거의 불가능하다",
        "examples": [
            ("하루 만에 끝내는 것은 불가능하다.", "Bir kunda tugatish imkonsiz."),
        ],
        "antonyms": [("가능", "mumkin, imkoniyatli")],
    },

    # ── 대(大) · 고(高) · 신(新) ──────────────────────────────────────────
    {
        "word": "대부분", "hanja": "大部分", "roots": ["대"],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 355,
        "meaning": "ko‘p qismi, aksariyati — «katta + qism»",
        "collocation": "대부분의 사람들 · 대부분을 차지하다",
        "note": "<p><b>쓰기 53 uchun:</b> grafikda ustun ulushni shu bilan aytasiz — "
                "<i>응답자의 대부분이 ...다고 답했다.</i></p>",
        "examples": [
            ("응답자의 대부분이 찬성했다.", "Respondentlarning aksariyati rozi bo‘ldi."),
        ],
    },
    {
        "word": "확대", "hanja": "擴大", "roots": ["대"],
        "pos": "noun", "topic": "economy", "level": 5, "freq": 2, "order": 356,
        "meaning": "kengaytirish, kattalashtirish",
        "collocation": "확대하다 · 시장 확대 · 지원 확대",
        "examples": [
            ("정부는 복지 지원을 확대하기로 했다.", "Hukumat ijtimoiy yordamni kengaytirishga qaror qildi."),
        ],
        "antonyms": [("축소", "qisqartirish, kichraytirish")],
    },
    {
        "word": "최고", "hanja": "最高", "roots": ["고"],
        "pos": "noun", "topic": "abstract", "level": 2, "freq": 2, "order": 360,
        "meaning": "eng yuqori, eng zo‘r — «eng + baland»",
        "collocation": "최고의 선수 · 최고 기온 · 역대 최고",
        "examples": [
            ("오늘 최고 기온은 35도입니다.", "Bugungi eng yuqori harorat 35 daraja."),
        ],
        "antonyms": [("최저", "eng past")],
    },
    {
        "word": "신문", "hanja": "新聞", "roots": ["신"],
        "pos": "noun", "topic": "media", "level": 1, "freq": 2, "order": 365,
        "meaning": "gazeta — so‘zma-so‘z «yangi eshitilgan»",
        "collocation": "신문을 읽다 · 신문 기사 · 신문사",
        "examples": [
            ("아버지는 아침마다 신문을 읽으세요.", "Otam har kuni ertalab gazeta o‘qiydilar."),
        ],
    },
    {
        "word": "신입", "hanja": "新入", "roots": ["신", "입"],
        "pos": "noun", "topic": "work", "level": 3, "freq": 2, "order": 366,
        "meaning": "yangi kelgan — «yangi + kirish»",
        "collocation": "신입 사원 · 신입생 · 신입 교육",
        "examples": [
            ("올해 신입 사원 열 명을 뽑았다.", "Bu yil o‘nta yangi xodim olindi."),
        ],
    },
]
