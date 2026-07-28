# -*- coding: utf-8 -*-
"""Vocab bank — mavzuli lug'at 1: kundalik hayot, his-tuyg'u, sog'liq, uy.

Order decade 500-599. Weighted to 형용사 / 부사 / 동사 on purpose — the user's
own reading method: "otdan ko'ra sifat, ravish, fe'lni ko'proq o'rganing,
javoblarni asosan shular hal qiladi". Mostly native-Korean words, so no roots.
See STYLE_GUIDE_VOCAB.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

WORDS = [
    # ── 형용사 — sifatlar ──────────────────────────────────────────────────
    {
        "word": "심각하다", "hanja": "深刻—", "pos": "adj", "topic": "society",
        "level": 4, "freq": 3, "order": 500,
        "meaning": "jiddiy, og‘ir (muammo haqida)",
        "collocation": "문제가 심각하다 · 심각한 상황 · 심각성",
        "note": "<p><b>쓰기 54 ning eng ko‘p ishlatiladigan sifati.</b> Tayyor qolip: "
                "<i>[문제]이/가 점점 심각해지고 있다.</i></p>",
        "examples": [
            ("환경 오염 문제가 갈수록 심각해지고 있다.", "Atrof-muhit ifloslanishi tobora jiddiylashmoqda."),
        ],
        "synonyms": [("중대하다", "중대하다 = rasmiy «katta ahamiyatli»; 심각하다 = salbiy og‘irlik")],
    },
    {
        "word": "다양하다", "hanja": "多樣—", "pos": "adj", "topic": "abstract",
        "level": 3, "freq": 3, "order": 501,
        "meaning": "xilma-xil, turli-tuman",
        "collocation": "다양한 방법 · 다양성 · 종류가 다양하다",
        "note": "<p>쓰기 da sanashdan oldin ishlating: <i>다양한 방법이 있다. 첫째…</i></p>",
        "examples": [
            ("요즘은 취미 활동이 아주 다양하다.", "Hozir qiziqish faoliyatlari juda xilma-xil."),
        ],
    },
    {
        "word": "부족하다", "hanja": "不足—", "roots": ["불"], "pos": "adj",
        "topic": "abstract", "level": 3, "freq": 3, "order": 502,
        "meaning": "yetishmaydi, kam — «yo‘q + yetarli»",
        "collocation": "시간이 부족하다 · 잠이 부족하다 · 부족한 점",
        "note": "<p>⚠️ 不 bu yerda <b>부</b> deb o‘qiladi (ㄷ/ㅈ oldidan). Shu qoida: "
                "부정, 부담, 부주의.</p>",
        "examples": [
            ("준비 시간이 부족해서 실수를 했어요.", "Tayyorgarlik vaqti yetmagani uchun xato qildim."),
        ],
        "antonyms": [("충분하다", "yetarli, mo‘l-ko‘l")],
    },
    {
        "word": "충분하다", "hanja": "充分—", "pos": "adj", "topic": "abstract",
        "level": 3, "freq": 2, "order": 503,
        "meaning": "yetarli, kifoya",
        "collocation": "충분한 시간 · 충분히 자다 · 충분조건",
        "examples": [
            ("하루 일곱 시간은 자야 충분하다.", "Kuniga yetti soat uxlash yetarli."),
        ],
        "antonyms": [("부족하다", "yetishmaslik")],
    },
    {
        "word": "복잡하다", "hanja": "複雜—", "pos": "adj", "topic": "daily",
        "level": 2, "freq": 3, "order": 504,
        "meaning": "murakkab; gavjum, tirband",
        "collocation": "길이 복잡하다 · 복잡한 문제 · 머리가 복잡하다",
        "note": "<p>Ikki ma’no: <b>joy</b> uchun «gavjum» (지하철이 복잡하다), "
                "<b>masala</b> uchun «murakkab» (문제가 복잡하다).</p>",
        "examples": [
            ("출근 시간에는 지하철이 아주 복잡해요.", "Ishga borish vaqtida metro juda gavjum."),
        ],
        "antonyms": [("단순하다", "oddiy, sodda"), ("한가하다", "bo‘sh, sokin")],
    },
    {
        "word": "당연하다", "hanja": "當然—", "pos": "adj", "topic": "abstract",
        "level": 4, "freq": 2, "order": 505,
        "meaning": "tabiiy, o‘z-o‘zidan ravshan",
        "collocation": "당연한 일 · 당연히 · 당연하게 여기다",
        "examples": [
            ("노력했으니 좋은 결과가 나온 것은 당연하다.", "Harakat qilgansiz, yaxshi natija chiqishi tabiiy."),
        ],
    },
    {
        "word": "익숙하다", "pos": "adj", "topic": "daily",
        "level": 3, "freq": 2, "order": 506,
        "meaning": "odatlangan, ko‘nikkan",
        "collocation": "생활에 익숙하다 · 익숙해지다 · 익숙한 얼굴",
        "note": "<p>Nimaga odatlangani <b>-에</b> bilan: <i>한국 음식<b>에</b> 익숙해졌다.</i></p>",
        "examples": [
            ("이제 한국 생활에 익숙해졌어요.", "Endi Koreyadagi hayotga ko‘nikdim."),
        ],
        "antonyms": [("낯설다", "notanish, g‘alati tuyuladigan")],
    },
    {
        "word": "꾸준하다", "pos": "adj", "topic": "abstract",
        "level": 4, "freq": 2, "order": 507,
        "meaning": "muttasil, uzluksiz (bir maromda)",
        "collocation": "꾸준히 노력하다 · 꾸준한 증가 · 꾸준히 늘다",
        "note": "<p><b>쓰기 53 uchun qimmatli:</b> grafikda tekis o‘sishni "
                "<i>꾸준히 증가하였다</i> deb yozasiz.</p>",
        "examples": [
            ("판매량이 꾸준히 증가하고 있다.", "Sotuv hajmi muttasil ortib bormoqda."),
        ],
        "related": [("급격하다", "급격하다 = keskin, tez; 꾸준하다 = tekis, sekin-asta")],
    },
    {
        "word": "급격하다", "hanja": "急激—", "pos": "adj", "topic": "abstract",
        "level": 5, "freq": 2, "order": 508,
        "meaning": "keskin, birdan (o‘zgarish haqida)",
        "collocation": "급격히 증가하다 · 급격한 변화",
        "examples": [
            ("인구가 급격히 감소하였다.", "Aholi keskin kamaydi."),
        ],
        "related": [("꾸준하다", "꾸준하다 = tekis; 급격하다 = keskin sakrash")],
    },
    {
        "word": "소중하다", "hanja": "所重—", "pos": "adj", "topic": "emotion",
        "level": 4, "freq": 2, "order": 509,
        "meaning": "qadrli, aziz",
        "collocation": "소중한 사람 · 소중히 여기다",
        "examples": [
            ("가족은 무엇보다 소중하다.", "Oila hamma narsadan qadrli."),
        ],
        "synonyms": [("귀하다", "귀하다 = noyob va qimmat; 소중하다 = hissiy qadrli")],
    },

    # ── 부사 — ravishlar (foydalanuvchi ta'kidi: bular javobni hal qiladi) ─
    {
        "word": "오히려", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 3, "order": 520,
        "meaning": "aksincha, kutilganidan teskari",
        "collocation": "오히려 더 · 오히려 반대로",
        "note": "<p><b>읽기 uchun kalit ravish:</b> 오히려 dan keyin gap "
                "<b>kutilganning teskarisi</b> keladi — javob ko‘pincha shu yerda.</p>",
        "examples": [
            ("약을 먹었는데 오히려 더 아팠다.", "Dori ichdim, aksincha battar og‘ridi."),
        ],
    },
    {
        "word": "비록", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 2, "order": 521,
        "meaning": "garchi, -sa ham (juft ravish)",
        "collocation": "비록 ~지만 · 비록 ~더라도",
        "note": "<p>Yolg‘iz kelmaydi — oxirida <b>-지만 / -더라도 / -아도</b> talab qiladi.</p>",
        "examples": [
            ("비록 시간이 걸리더라도 끝까지 하겠다.", "Vaqt ketsa ham, oxirigacha qilaman."),
        ],
    },
    {
        "word": "결코", "hanja": "決—", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 522,
        "meaning": "hech qachon, aslo (inkor bilan)",
        "collocation": "결코 ~지 않다 · 결코 쉽지 않다",
        "note": "<p>⚠️ Doim <b>inkor</b> bilan. Shu oiladagilar: 전혀, 절대, 별로 — "
                "hammasi inkor talab qiladi.</p>",
        "examples": [
            ("이 문제는 결코 쉽지 않다.", "Bu masala aslo oson emas."),
        ],
        "synonyms": [("절대", "절대 = qat’iy taqiq ohangi; 결코 = kitobiy inkor")],
    },
    {
        "word": "마침내", "pos": "adv", "topic": "time",
        "level": 4, "freq": 2, "order": 523,
        "meaning": "nihoyat, oxir-oqibat (uzoq kutishdan keyin)",
        "collocation": "마침내 성공하다 · 마침내 도착하다",
        "examples": [
            ("오랜 노력 끝에 마침내 합격했다.", "Uzoq harakatdan so‘ng nihoyat imtihondan o‘tdim."),
        ],
        "synonyms": [("드디어", "드디어 = quvonchli kutilgan natija; 마침내 = kitobiy, neytral"),
                     ("결국", "결국 = oqibat (ko‘pincha salbiy); 마침내 = ijobiy yakun")],
    },
    {
        "word": "결국", "hanja": "結局", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 3, "order": 524,
        "meaning": "oxir-oqibat, natijada",
        "collocation": "결국 포기하다 · 결국에는",
        "examples": [
            ("여러 번 시도했지만 결국 실패했다.", "Bir necha bor urindim, lekin oxir-oqibat muvaffaqiyatsiz bo‘ldi."),
        ],
        "related": [("마침내", "마침내 = ijobiy yakun; 결국 = ko‘pincha salbiy oqibat")],
    },
    {
        "word": "점점", "hanja": "漸漸", "pos": "adv", "topic": "time",
        "level": 3, "freq": 3, "order": 525,
        "meaning": "asta-sekin, tobora",
        "collocation": "점점 늘다 · 점점 심각해지다 · 점차",
        "note": "<p><b>쓰기 53/54 da doim kerak:</b> "
                "<i>[주제]이/가 점점 심각해지고 있다.</i> Yozma varianti — <b>점차</b>.</p>",
        "examples": [
            ("1인 가구가 점점 늘고 있다.", "Yolg‘iz yashovchi xonadonlar tobora ko‘paymoqda."),
        ],
        "synonyms": [("점차", "점차 = yozma/rasmiy varianti; 점점 = neytral")],
    },
    {
        "word": "특히", "hanja": "特—", "pos": "adv", "topic": "abstract",
        "level": 2, "freq": 3, "order": 526,
        "meaning": "ayniqsa, xususan",
        "collocation": "특히 중요하다 · 특히 젊은 층에서",
        "examples": [
            ("특히 젊은 층에서 이런 경향이 강하다.", "Ayniqsa yoshlar orasida bu tendensiya kuchli."),
        ],
    },
    {
        "word": "아무래도", "pos": "adv", "topic": "abstract",
        "level": 4, "freq": 2, "order": 527,
        "meaning": "har qalay, baribir shekilli",
        "collocation": "아무래도 ~것 같다",
        "note": "<p>Ko‘pincha <b>-(으)ㄹ 것 같다</b> bilan juft keladi.</p>",
        "examples": [
            ("아무래도 오늘은 못 갈 것 같아요.", "Har qalay bugun bora olmasam kerak."),
        ],
    },
    {
        "word": "그저", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 1, "order": 528,
        "meaning": "shunchaki, faqat",
        "collocation": "그저 바라볼 뿐 · 그저 그렇다",
        "examples": [
            ("그는 그저 웃을 뿐이었다.", "U shunchaki kulib qo‘ydi, xolos."),
        ],
    },
    {
        "word": "무려", "hanja": "無慮", "pos": "adv", "topic": "abstract",
        "level": 5, "freq": 2, "order": 529,
        "meaning": "hisobi bilan, hech kam emas (kutilganidan ko‘p)",
        "collocation": "무려 100명 · 무려 두 배",
        "note": "<p>Faqat <b>son</b> oldidan va faqat son <b>katta</b> bo‘lganda. "
                "쓰기 53 da raqamni ta’kidlaydi.</p>",
        "examples": [
            ("응답자가 무려 80%에 달했다.", "Respondentlar soni 80 foizgacha yetdi."),
        ],
    },

    # ── 동사 — fe'llar ────────────────────────────────────────────────────
    {
        "word": "늘어나다", "pos": "verb", "topic": "abstract",
        "level": 3, "freq": 3, "order": 540,
        "meaning": "ko‘paymoq, ortmoq",
        "collocation": "수가 늘어나다 · 크게 늘어나다",
        "note": "<p><b>쓰기 53 uchun:</b> 늘다 = og‘zaki; <b>증가하다</b> = rasmiy yozma. "
                "Inshoda 증가하다 ishlating.</p>",
        "examples": [
            ("1인 가구가 크게 늘어났다.", "Yolg‘iz yashovchi xonadonlar keskin ko‘paydi."),
        ],
        "synonyms": [("증가하다", "증가하다 = rasmiy/yozma; 늘어나다 = neytral og‘zaki")],
        "antonyms": [("줄어들다", "kamaymoq")],
    },
    {
        "word": "증가하다", "hanja": "增加—", "pos": "verb", "topic": "economy",
        "level": 4, "freq": 3, "order": 541,
        "meaning": "ortmoq, ko‘paymoq (rasmiy)",
        "collocation": "꾸준히 증가하다 · 증가율 · 급격히 증가하다",
        "note": "<p><b>쓰기 53 ning asosiy fe’li.</b> Qolip: "
                "<i>2020년부터 2025년까지 꾸준히 증가하였다.</i></p>",
        "examples": [
            ("관광객 수가 매년 증가하고 있다.", "Sayyohlar soni har yili ortib bormoqda."),
        ],
        "antonyms": [("감소하다", "kamaymoq — 增↔減, 쓰기 53 ning juftligi")],
    },
    {
        "word": "감소하다", "hanja": "減少—", "pos": "verb", "topic": "economy",
        "level": 4, "freq": 3, "order": 542,
        "meaning": "kamaymoq, pasaymoq (rasmiy)",
        "collocation": "인구가 감소하다 · 감소 추세 · 절반으로 감소하다",
        "examples": [
            ("출생률이 계속 감소하고 있다.", "Tug‘ilish darajasi muttasil kamaymoqda."),
        ],
        "antonyms": [("증가하다", "ortmoq — 減↔增")],
        "synonyms": [("줄어들다", "줄어들다 = og‘zaki; 감소하다 = rasmiy yozma")],
    },
    {
        "word": "차지하다", "pos": "verb", "topic": "economy",
        "level": 4, "freq": 3, "order": 543,
        "meaning": "egallamoq, ulushga ega bo‘lmoq",
        "collocation": "1위를 차지하다 · 절반을 차지하다 · 큰 비중을 차지하다",
        "note": "<p><b>쓰기 53 uchun majburiy:</b> "
                "<i>‘건강’이 45%로 가장 큰 비중을 차지하였다.</i></p>",
        "examples": [
            ("응답자의 절반을 차지했다.", "Respondentlarning yarmini tashkil qildi."),
        ],
    },
    {
        "word": "나타나다", "pos": "verb", "topic": "abstract",
        "level": 4, "freq": 3, "order": 544,
        "meaning": "namoyon bo‘lmoq, ma’lum bo‘lmoq; paydo bo‘lmoq",
        "collocation": "결과가 나타나다 · 차이가 나타나다 · ~것으로 나타났다",
        "note": "<p><b>쓰기 53 ning yakuniy qolipi:</b> "
                "<i>조사 결과 ...는 것으로 나타났다.</i></p>",
        "examples": [
            ("남녀 간에 큰 차이가 나타났다.", "Erkak va ayollar orasida katta farq ko‘rindi."),
        ],
    },
    {
        "word": "해결하다", "hanja": "解決—", "pos": "verb", "topic": "abstract",
        "level": 3, "freq": 3, "order": 545,
        "meaning": "hal qilmoq, yechmoq",
        "collocation": "문제를 해결하다 · 해결책 · 해결 방안",
        "note": "<p><b>쓰기 54 uchun majburiy so‘z.</b> Qolip: "
                "<i>이 문제를 해결하기 위해서는 ...이 필요하다.</i></p>",
        "examples": [
            ("이 문제를 해결할 방법을 찾아야 한다.", "Bu muammoni hal qilish yo‘lini topish kerak."),
        ],
    },
    {
        "word": "미치다", "pos": "verb", "topic": "abstract",
        "level": 4, "freq": 3, "order": 546,
        "meaning": "ta’sir qilmoq, yetib bormoq",
        "collocation": "영향을 미치다 · ~에 미치다",
        "note": "<p>Deyarli doim <b>영향을 미치다</b> birikmasida — «ta’sir ko‘rsatmoq». "
                "쓰기 54 da juda ko‘p kerak.</p>",
        "examples": [
            ("스마트폰은 청소년에게 큰 영향을 미친다.", "Smartfon o‘smirlarga katta ta’sir ko‘rsatadi."),
        ],
    },
    {
        "word": "참여하다", "hanja": "參與—", "pos": "verb", "topic": "society",
        "level": 4, "freq": 2, "order": 547,
        "meaning": "qatnashmoq, ishtirok etmoq",
        "collocation": "행사에 참여하다 · 적극적으로 참여하다 · 참여율",
        "examples": [
            ("많은 시민이 캠페인에 참여했다.", "Ko‘plab fuqarolar kampaniyada qatnashdi."),
        ],
        "synonyms": [("참가하다", "참가 = tadbir/musobaqaga qo‘shilish; 참여 = jarayonda ishtirok")],
    },
    {
        "word": "적응하다", "hanja": "適應—", "pos": "verb", "topic": "person",
        "level": 4, "freq": 2, "order": 548,
        "meaning": "moslashmoq, ko‘nikmoq",
        "collocation": "생활에 적응하다 · 빨리 적응하다 · 적응력",
        "examples": [
            ("새 학교에 잘 적응하고 있어요.", "Yangi maktabga yaxshi moslashyapman."),
        ],
    },
    {
        "word": "포기하다", "hanja": "抛棄—", "pos": "verb", "topic": "emotion",
        "level": 3, "freq": 2, "order": 549,
        "meaning": "voz kechmoq, taslim bo‘lmoq",
        "collocation": "꿈을 포기하다 · 절대 포기하지 않다",
        "examples": [
            ("아무리 힘들어도 포기하지 마세요.", "Qanchalik qiyin bo‘lsa ham voz kechmang."),
        ],
    },
    {
        "word": "이루어지다", "pos": "verb", "topic": "abstract",
        "level": 5, "freq": 2, "order": 550,
        "meaning": "amalga oshmoq; tashkil topmoq",
        "collocation": "꿈이 이루어지다 · ~로 이루어져 있다",
        "note": "<p>Ikki ma’no: <b>orzu amalga oshdi</b> va <b>...dan iborat</b> "
                "(이 책은 다섯 장<b>으로 이루어져 있다</b>).</p>",
        "examples": [
            ("오랜 꿈이 드디어 이루어졌다.", "Uzoq orzum nihoyat amalga oshdi."),
        ],
    },

    # ── Kundalik otlar (kam, lekin kerakli) ───────────────────────────────
    {
        "word": "습관", "hanja": "習慣", "pos": "noun", "topic": "daily",
        "level": 3, "freq": 2, "order": 560,
        "meaning": "odat",
        "collocation": "습관을 들이다 · 나쁜 습관 · 식습관",
        "examples": [
            ("일찍 자는 습관을 들이는 게 좋다.", "Erta uxlash odatini shakllantirgan ma’qul."),
        ],
    },
    {
        "word": "건강", "hanja": "健康", "pos": "noun", "topic": "body",
        "level": 1, "freq": 3, "order": 561,
        "meaning": "sog‘liq",
        "collocation": "건강하다 · 건강을 지키다 · 건강 관리",
        "note": "<p>쓰기 53 so‘rovnomalarining eng ko‘p javobi — «건강» birinchi o‘rinda.</p>",
        "examples": [
            ("건강을 위해 규칙적으로 운동한다.", "Sog‘liq uchun muntazam sport bilan shug‘ullanaman."),
        ],
    },
    {
        "word": "스트레스", "pos": "noun", "topic": "emotion",
        "level": 2, "freq": 3, "order": 562,
        "meaning": "stress, ruhiy zo‘riqish",
        "collocation": "스트레스를 받다 · 스트레스를 풀다 · 스트레스 해소",
        "note": "<p>⚠️ Ingliz tilidan olingan (외래어) — Hanja yo‘q. "
                "«Olmoq» = <b>받다</b>, «tarqatmoq» = <b>풀다</b>.</p>",
        "examples": [
            ("운동으로 스트레스를 풀어요.", "Sport bilan stressni tarqataman."),
        ],
    },
    {
        "word": "여유", "hanja": "餘裕", "pos": "noun", "topic": "daily",
        "level": 4, "freq": 2, "order": 563,
        "meaning": "bo‘sh vaqt, imkon; xotirjamlik",
        "collocation": "여유가 있다 · 시간적 여유 · 마음의 여유",
        "examples": [
            ("요즘은 쉴 여유가 없어요.", "Hozir dam olishga imkon yo‘q."),
        ],
    },
    {
        "word": "차이", "hanja": "差異", "pos": "noun", "topic": "abstract",
        "level": 3, "freq": 3, "order": 564,
        "meaning": "farq, tafovut",
        "collocation": "차이가 나다 · 세대 차이 · 큰 차이",
        "note": "<p><b>쓰기 53 uchun:</b> ikki guruhni taqqoslaganda "
                "<i>남녀 간에 차이가 나타났다.</i></p>",
        "examples": [
            ("두 결과 사이에 큰 차이가 있다.", "Ikki natija orasida katta farq bor."),
        ],
    },
    {
        "word": "영향", "hanja": "影響", "pos": "noun", "topic": "abstract",
        "level": 4, "freq": 3, "order": 565,
        "meaning": "ta’sir",
        "collocation": "영향을 미치다 · 영향을 받다 · 부정적 영향",
        "note": "<p><b>쓰기 54 ning eng kerakli otlaridan:</b> "
                "<i>[원인]은/는 [대상]에 부정적인 영향을 미친다.</i></p>",
        "examples": [
            ("날씨는 기분에 영향을 미친다.", "Ob-havo kayfiyatga ta’sir qiladi."),
        ],
    },
]
