# -*- coding: utf-8 -*-
"""Vocab bank — 어근 1: harakat va joy o'zaklari (motion & place roots).

出 入 發 動 通 場 室 口 所 地 — order decade 100-199.
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
        "syllable": "출", "hanja": "出", "order": 100,
        "meaning": "chiqmoq — chiqish, tashqariga",
        "note": "<p>Deyarli har doim <b>ichkaridan tashqariga</b> harakati. "
                "So‘z boshida ham (출구), oxirida ham (제출) keladi. "
                "Juftligi — <b>입(入)</b>: 출구↔입구, 수출↔수입.</p>",
    },
    {
        "syllable": "입", "hanja": "入", "order": 110,
        "meaning": "kirmoq — kirish, ichkariga",
        "note": "<p>출(出) ning teskarisi. ⚠️ <b>입(口)</b> = «og‘iz» boshqa o‘zak: "
                "입 (og‘iz) — sof koreyscha so‘z.</p>",
    },
    {
        "syllable": "발", "hanja": "發", "order": 120,
        "meaning": "otilmoq, boshlanmoq — jo‘nash, rivojlanish, chiqarish",
        "note": "<p>«Nimadir yuzaga chiqadi/boshlanadi» ma’nosi: 출발 (jo‘nash), "
                "발전 (rivojlanish), 발표 (e’lon qilish), 발생 (yuz berish).</p>",
    },
    {
        "syllable": "동", "hanja": "動", "order": 130,
        "meaning": "harakat — qimirlamoq, harakatlanmoq",
        "note": "<p>⚠️ Bir xil bo‘g‘inli boshqa o‘zaklar bor: <b>동(東)</b> = sharq "
                "(동양), <b>동(同)</b> = bir xil (동시). Ma’nodan farqlang.</p>",
    },
    {
        "syllable": "감", "hanja": "感", "order": 305,
        "meaning": "his — sezish, tuyg‘u",
        "note": "<p>Barcha tuyg‘u so‘zlarining o‘zagi: 감정, 감동, 감사, 공감, 예감. "
                "Oilasi asosan <em>어근 3</em> faylida.</p>",
    },
    {
        "syllable": "통", "hanja": "通", "order": 140,
        "meaning": "o‘tmoq — aloqa, o‘tish, umumiy",
        "note": "<p>«Bir joydan boshqasiga o‘tadi» → aloqa va yo‘l ma’nosi: "
                "교통, 통화, 소통, 통과.</p>",
    },
    {
        "syllable": "장", "hanja": "場", "order": 150,
        "meaning": "maydon — joy, o‘rin",
        "note": "<p>So‘z <b>oxirida</b> «joy» yasaydi: 시장, 공장, 운동장, 주차장. "
                "⚠️ <b>장(長)</b> = boshliq/uzun (사장, 장점) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "실", "hanja": "室", "order": 160,
        "meaning": "xona",
        "note": "<p>Yopiq xonalarni yasaydi: 교실, 사무실, 화장실, 실내.</p>",
    },
    {
        "syllable": "구", "hanja": "口", "order": 170,
        "meaning": "og‘iz — teshik, chiqish/kirish nuqtasi",
        "note": "<p>«Teshik, o‘tish nuqtasi» ma’nosida: 출구, 입구, 인구 "
                "(«odam og‘izlari» → aholi), 창구 (kassa oynasi).</p>",
    },
    {
        "syllable": "소", "hanja": "所", "order": 180,
        "meaning": "joy — o‘rin, muassasa",
        "note": "<p>Muassasa va manzil yasaydi: 주소, 사무소, 연구소, 장소. "
                "⚠️ <b>소(小)</b> = kichik, <b>소(消)</b> = yo‘qolmoq — boshqa o‘zaklar.</p>",
    },
    {
        "syllable": "지", "hanja": "地", "order": 190,
        "meaning": "yer — hudud, joy",
        "note": "<p>Geografik ma’no: 지역, 지방, 지구, 지하, 토지.</p>",
    },
]

WORDS = [
    # ── 출(出) ─────────────────────────────────────────────────────────────
    {
        "word": "출구", "hanja": "出口", "roots": ["출", "구"],
        "pos": "noun", "topic": "place", "level": 1, "freq": 3, "order": 100,
        "meaning": "chiqish joyi — «chiqish + og‘iz»",
        "collocation": "출구를 찾다 · 비상 출구 · 출구 조사",
        "examples": [
            ("비상 출구는 오른쪽에 있습니다.", "Favqulodda chiqish o‘ng tomonda."),
            ("지하철 3번 출구에서 만나요.", "Metroning 3-chiqishida uchrashamiz."),
        ],
        "antonyms": [("입구", "kirish joyi — 出↔入, aynan teskari juftlik")],
    },
    {
        "word": "출근", "hanja": "出勤", "roots": ["출"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 3, "order": 101,
        "meaning": "ishga chiqish — «chiqish + mehnat»",
        "collocation": "출근하다 · 출근 시간 · 출근길",
        "note": "<p>Uydan <b>chiqib</b> ishga borish. Ishdan qaytish esa <b>퇴근</b> "
                "(退勤). Ikkalasi birga — <b>출퇴근</b>.</p>",
        "examples": [
            ("보통 여덟 시에 출근해요.", "Odatda soat sakkizda ishga boraman."),
            ("출근 시간에는 지하철이 아주 복잡하다.", "Ishga borish vaqtida metro juda gavjum bo‘ladi."),
        ],
        "antonyms": [("퇴근", "ishdan chiqish, uyga qaytish — 出↔退")],
        "related": [("출퇴근", "ishga borib-kelish (ikkalasi birga)")],
    },
    {
        "word": "출발", "hanja": "出發", "roots": ["출", "발"],
        "pos": "noun", "topic": "transport", "level": 1, "freq": 3, "order": 102,
        "meaning": "jo‘nash, yo‘lga chiqish — «chiqish + otilish»",
        "collocation": "출발하다 · 출발 시간 · 출발점",
        "examples": [
            ("기차는 아홉 시에 출발합니다.", "Poyezd soat to‘qqizda jo‘naydi."),
            ("새로운 출발을 하고 싶어요.", "Yangi boshlanish qilmoqchiman."),
        ],
        "antonyms": [("도착", "yetib borish, manzilga kelish")],
    },
    {
        "word": "출석", "hanja": "出席", "roots": ["출"],
        "pos": "noun", "topic": "school", "level": 2, "freq": 2, "order": 103,
        "meaning": "davomat, qatnashish — «chiqish + o‘rindiq»",
        "collocation": "출석하다 · 출석을 부르다 · 출석률",
        "note": "<p>So‘zma-so‘z «o‘z <b>o‘rniga chiqish</b>» — darsga/majlisga kelish.</p>",
        "examples": [
            ("선생님이 출석을 부르셨어요.", "O‘qituvchi davomat oldi."),
            ("출석률이 낮으면 시험을 볼 수 없다.", "Davomat past bo‘lsa, imtihon topshirib bo‘lmaydi."),
        ],
        "antonyms": [("결석", "darsga kelmaslik, qoldirish")],
    },
    {
        "word": "제출", "hanja": "提出", "roots": ["출"],
        "pos": "noun", "topic": "school", "level": 3, "freq": 3, "order": 104,
        "meaning": "topshirish — «ko‘tarib + chiqarish»",
        "collocation": "제출하다 · 서류를 제출하다 · 제출 기한",
        "note": "<p>Hujjat, vazifa, ariza topshirishda. 쓰기 51 (rasmiy xat) da tez-tez.</p>",
        "examples": [
            ("내일까지 보고서를 제출해야 합니다.", "Ertagacha hisobotni topshirishim kerak."),
            ("서류를 기한 안에 제출하십시오.", "Hujjatlarni muddat ichida topshiring."),
        ],
    },
    {
        "word": "수출", "hanja": "輸出", "roots": ["출"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 105,
        "meaning": "eksport — «tashib + chiqarish»",
        "collocation": "수출하다 · 수출액 · 수출이 증가하다",
        "note": "<p><b>쓰기 53 uchun muhim juftlik:</b> 수출(eksport) ↔ 수입(import). "
                "Grafik izohlashda doim kerak.</p>",
        "examples": [
            ("한국은 반도체를 많이 수출한다.", "Koreya yarimo‘tkazgichlarni ko‘p eksport qiladi."),
            ("작년에 비해 수출이 크게 늘었다.", "O‘tgan yilga nisbatan eksport keskin oshdi."),
        ],
        "antonyms": [("수입", "import — chetdan olib kirish; 出↔入")],
    },
    {
        "word": "외출", "hanja": "外出", "roots": ["출"],
        "pos": "noun", "topic": "daily", "level": 2, "freq": 2, "order": 106,
        "meaning": "ko‘chaga chiqish, tashqariga chiqish",
        "collocation": "외출하다 · 외출 중 · 외출복",
        "examples": [
            ("어머니는 지금 외출 중이세요.", "Onam hozir tashqarida (chiqib ketganlar)."),
            ("날씨가 추워서 외출하고 싶지 않아요.", "Havo sovuq, tashqariga chiqishni istamayman."),
        ],
    },
    {
        "word": "출입", "hanja": "出入", "roots": ["출", "입"],
        "pos": "noun", "topic": "place", "level": 3, "freq": 2, "order": 107,
        "meaning": "kirish-chiqish, qatnov",
        "collocation": "출입하다 · 출입 금지 · 출입구",
        "note": "<p>Ikkala o‘zak birga — TOPIK 읽기 dagi e’lonlarda ko‘p: "
                "<b>관계자 외 출입 금지</b> (begonalarga kirish taqiqlanadi).</p>",
        "examples": [
            ("이곳은 출입이 금지되어 있습니다.", "Bu yerga kirish taqiqlangan."),
            ("출입구는 건물 뒤쪽에 있다.", "Kirish-chiqish eshigi binoning orqasida."),
        ],
    },

    # ── 입(入) ─────────────────────────────────────────────────────────────
    {
        "word": "입구", "hanja": "入口", "roots": ["입", "구"],
        "pos": "noun", "topic": "place", "level": 1, "freq": 3, "order": 110,
        "meaning": "kirish joyi — «kirish + og‘iz»",
        "collocation": "입구에서 만나다 · 정문 입구",
        "examples": [
            ("공원 입구에서 기다릴게요.", "Bog‘ning kiraverishida kutaman."),
        ],
        "antonyms": [("출구", "chiqish joyi — 入↔出")],
    },
    {
        "word": "입학", "hanja": "入學", "roots": ["입"],
        "pos": "noun", "topic": "school", "level": 2, "freq": 3, "order": 111,
        "meaning": "o‘quv yurtiga kirish, qabul — «kirish + ilm»",
        "collocation": "입학하다 · 입학식 · 입학시험",
        "examples": [
            ("아프소나는 올해 대학에 입학했어요.", "Afsona bu yil universitetga kirdi."),
        ],
        "antonyms": [("졸업", "bitirish, tamomlash")],
    },
    {
        "word": "수입", "hanja": "輸入", "roots": ["입"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 112,
        "meaning": "import — «tashib + kiritish»",
        "collocation": "수입하다 · 수입품 · 수입이 줄다",
        "note": "<p>⚠️ Omonim: <b>수입(收入)</b> = daromad. Kontekstdan farqlang — "
                "«무역» yonida bo‘lsa import, «지출» yonida bo‘lsa daromad.</p>",
        "examples": [
            ("이 나라는 식량을 대부분 수입한다.", "Bu davlat oziq-ovqatning ko‘pini import qiladi."),
        ],
        "antonyms": [("수출", "eksport — 入↔出")],
    },
    {
        "word": "입원", "hanja": "入院", "roots": ["입"],
        "pos": "noun", "topic": "body", "level": 3, "freq": 2, "order": 113,
        "meaning": "kasalxonaga yotish — «kirish + muassasa»",
        "collocation": "입원하다 · 입원 치료 · 입원비",
        "examples": [
            ("할아버지께서 지난주에 입원하셨다.", "Bobom o‘tgan hafta kasalxonaga yotdilar."),
        ],
        "antonyms": [("퇴원", "kasalxonadan chiqish")],
    },
    {
        "word": "가입", "hanja": "加入", "roots": ["입"],
        "pos": "noun", "topic": "society", "level": 3, "freq": 2, "order": 114,
        "meaning": "a’zo bo‘lish, ro‘yxatdan o‘tish — «qo‘shilib + kirish»",
        "collocation": "가입하다 · 회원 가입 · 보험에 가입하다",
        "examples": [
            ("동아리에 가입하고 싶어요.", "To‘garakka a’zo bo‘lmoqchiman."),
        ],
        "antonyms": [("탈퇴", "a’zolikdan chiqish")],
    },

    # ── 발(發) ─────────────────────────────────────────────────────────────
    {
        "word": "발전", "hanja": "發展", "roots": ["발"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 120,
        "meaning": "rivojlanish, taraqqiyot",
        "collocation": "발전하다 · 경제 발전 · 발전 가능성",
        "note": "<p><b>쓰기 54 uchun eng kerakli so‘zlardan biri:</b> "
                "<i>기술이 발전할수록 ...</i> qolipi bilan ishlating.</p>",
        "examples": [
            ("과학 기술이 빠르게 발전하고 있다.", "Fan-texnika tez rivojlanmoqda."),
        ],
        "related": [("발달", "발달 = qobiliyat/organ rivoji; 발전 = tizim/jamiyat taraqqiyoti")],
    },
    {
        "word": "발표", "hanja": "發表", "roots": ["발"],
        "pos": "noun", "topic": "school", "level": 3, "freq": 3, "order": 121,
        "meaning": "e’lon qilish, taqdimot — «chiqarib + ko‘rsatish»",
        "collocation": "발표하다 · 발표 자료 · 결과를 발표하다",
        "examples": [
            ("내일 수업 시간에 발표가 있어요.", "Ertaga darsda taqdimot bor."),
            ("조사 결과가 어제 발표되었다.", "Tadqiqot natijalari kecha e’lon qilindi."),
        ],
    },
    {
        "word": "발생", "hanja": "發生", "roots": ["발", "생"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 122,
        "meaning": "yuz berish, sodir bo‘lish (odatda salbiy)",
        "collocation": "발생하다 · 사고가 발생하다 · 문제 발생",
        "note": "<p>Yangilik va hisobot uslubi. Ijobiy hodisaga kamdan-kam ishlatiladi.</p>",
        "examples": [
            ("어제 도심에서 큰 사고가 발생했다.", "Kecha shahar markazida katta hodisa yuz berdi."),
        ],
    },
    {
        "word": "개발", "hanja": "開發", "roots": ["발"],
        "pos": "noun", "topic": "science", "level": 4, "freq": 3, "order": 123,
        "meaning": "ishlab chiqish, o‘zlashtirish — «ochib + chiqarish»",
        "collocation": "개발하다 · 신제품 개발 · 개발도상국",
        "examples": [
            ("이 회사는 새로운 앱을 개발했다.", "Bu kompaniya yangi ilova ishlab chiqdi."),
        ],
    },

    # ── 동(動) ─────────────────────────────────────────────────────────────
    {
        "word": "운동", "hanja": "運動", "roots": ["동"],
        "pos": "noun", "topic": "body", "level": 1, "freq": 3, "order": 130,
        "meaning": "sport, jismoniy mashq; harakat (ijtimoiy)",
        "collocation": "운동하다 · 운동장 · 환경 보호 운동",
        "examples": [
            ("건강을 위해 매일 운동해요.", "Sog‘liq uchun har kuni sport bilan shug‘ullanaman."),
        ],
    },
    {
        "word": "활동", "hanja": "活動", "roots": ["동"],
        "pos": "noun", "topic": "society", "level": 3, "freq": 3, "order": 131,
        "meaning": "faoliyat, faollik",
        "collocation": "활동하다 · 봉사 활동 · 활동적이다",
        "examples": [
            ("주말에는 봉사 활동에 참여한다.", "Dam olish kunlari ko‘ngilli faoliyatda qatnashaman."),
        ],
    },
    {
        "word": "이동", "hanja": "移動", "roots": ["동"],
        "pos": "noun", "topic": "transport", "level": 3, "freq": 2, "order": 132,
        "meaning": "ko‘chish, joyni o‘zgartirish",
        "collocation": "이동하다 · 이동 수단 · 인구 이동",
        "examples": [
            ("버스로 이동하는 것이 더 편리하다.", "Avtobusda harakatlanish qulayroq."),
        ],
    },
    {
        "word": "감동", "hanja": "感動", "roots": ["동", "감"],
        "pos": "noun", "topic": "emotion", "level": 3, "freq": 2, "order": 133,
        "meaning": "hayajonlanish, ta’sirlanish — «his + qimirlash»",
        "collocation": "감동하다 · 감동적이다 · 감동을 받다",
        "note": "<p>So‘zma-so‘z «yurak qimirladi» — chuqur ta’sirlanish.</p>",
        "examples": [
            ("그 영화를 보고 큰 감동을 받았어요.", "O‘sha kinoni ko‘rib qattiq ta’sirlandim."),
        ],
    },

    # ── 통(通) ─────────────────────────────────────────────────────────────
    {
        "word": "교통", "hanja": "交通", "roots": ["통"],
        "pos": "noun", "topic": "transport", "level": 1, "freq": 3, "order": 140,
        "meaning": "transport, qatnov",
        "collocation": "교통이 편리하다 · 교통 체증 · 대중교통",
        "examples": [
            ("이 동네는 교통이 아주 편리해요.", "Bu mahallada transport juda qulay."),
            ("출근 시간에는 교통 체증이 심하다.", "Ishga borish vaqtida tirbandlik kuchli bo‘ladi."),
        ],
    },
    {
        "word": "소통", "hanja": "疏通", "roots": ["통"],
        "pos": "noun", "topic": "person", "level": 4, "freq": 2, "order": 141,
        "meaning": "muloqot, o‘zaro tushunish",
        "collocation": "소통하다 · 소통이 부족하다 · 세대 간 소통",
        "note": "<p>쓰기 54 da munosabat mavzusida ko‘p ishlatiladi.</p>",
        "examples": [
            ("세대 간의 소통이 점점 줄어들고 있다.", "Avlodlar orasidagi muloqot tobora kamaymoqda."),
        ],
    },
    {
        "word": "통화", "hanja": "通話", "roots": ["통"],
        "pos": "noun", "topic": "media", "level": 2, "freq": 2, "order": 142,
        "meaning": "telefonda gaplashish",
        "collocation": "통화하다 · 통화 중 · 통화 요금",
        "examples": [
            ("지금 통화 중이니까 나중에 전화할게요.", "Hozir gaplashyapman, keyinroq qo‘ng‘iroq qilaman."),
        ],
    },

    # ── 장(場) · 실(室) · 소(所) · 지(地) ──────────────────────────────────
    {
        "word": "시장", "hanja": "市場", "roots": ["장"],
        "pos": "noun", "topic": "shopping", "level": 1, "freq": 3, "order": 150,
        "meaning": "bozor — «shahar + maydon»",
        "collocation": "시장에 가다 · 전통 시장 · 시장 조사",
        "examples": [
            ("주말마다 전통 시장에 가요.", "Har dam olish kuni an’anaviy bozorga boraman."),
        ],
    },
    {
        "word": "공장", "hanja": "工場", "roots": ["장"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 2, "order": 151,
        "meaning": "zavod, fabrika — «mehnat + maydon»",
        "collocation": "공장에서 일하다 · 자동차 공장",
        "examples": [
            ("아버지는 자동차 공장에서 일하신다.", "Otam avtomobil zavodida ishlaydilar."),
        ],
    },
    {
        "word": "주차장", "hanja": "駐車場", "roots": ["장"],
        "pos": "noun", "topic": "transport", "level": 2, "freq": 2, "order": 152,
        "meaning": "avtoturargoh — «to‘xtash + mashina + maydon»",
        "collocation": "주차장에 세우다 · 지하 주차장",
        "examples": [
            ("지하 주차장에 자리가 없어요.", "Yerosti turargohida joy yo‘q."),
        ],
    },
    {
        "word": "교실", "hanja": "敎室", "roots": ["실"],
        "pos": "noun", "topic": "school", "level": 1, "freq": 2, "order": 160,
        "meaning": "sinf xonasi — «ta’lim + xona»",
        "collocation": "교실에 들어가다 · 빈 교실",
        "examples": [
            ("교실에서 조용히 해 주세요.", "Sinfda jim turing."),
        ],
    },
    {
        "word": "사무실", "hanja": "事務室", "roots": ["실"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 2, "order": 161,
        "meaning": "ofis, ish xonasi — «ish + xizmat + xona»",
        "collocation": "사무실에 출근하다 · 사무실 분위기",
        "examples": [
            ("사무실이 3층에 있습니다.", "Ofis 3-qavatda."),
        ],
    },
    {
        "word": "주소", "hanja": "住所", "roots": ["소(所)"],
        "pos": "noun", "topic": "home", "level": 1, "freq": 2, "order": 180,
        "meaning": "manzil — «yashash + joy»",
        "collocation": "주소를 쓰다 · 이메일 주소",
        "examples": [
            ("여기에 주소와 이름을 쓰세요.", "Bu yerga manzil va ismingizni yozing."),
        ],
    },
    {
        "word": "연구소", "hanja": "硏究所", "roots": ["소(所)"],
        "pos": "noun", "topic": "science", "level": 4, "freq": 2, "order": 181,
        "meaning": "ilmiy-tadqiqot instituti",
        "collocation": "연구소에서 근무하다 · 국립 연구소",
        "examples": [
            ("그는 국립 연구소에서 일한다.", "U davlat ilmiy institutida ishlaydi."),
        ],
    },
    {
        "word": "지역", "hanja": "地域", "roots": ["지"],
        "pos": "noun", "topic": "place", "level": 4, "freq": 3, "order": 190,
        "meaning": "hudud, mintaqa — «yer + doira»",
        "collocation": "지역 사회 · 농촌 지역 · 지역별 차이",
        "note": "<p><b>쓰기 53 uchun muhim:</b> grafiklar ko‘pincha 지역별 (hududlar bo‘yicha) "
                "taqsimlanadi.</p>",
        "examples": [
            ("지역에 따라 물가 차이가 크다.", "Hududga qarab narxlar farqi katta."),
        ],
    },
    {
        "word": "지하", "hanja": "地下", "roots": ["지"],
        "pos": "noun", "topic": "place", "level": 2, "freq": 2, "order": 191,
        "meaning": "yerosti — «yer + past»",
        "collocation": "지하철 · 지하도 · 지하 1층",
        "examples": [
            ("식당은 지하 1층에 있어요.", "Restoran yerosti 1-qavatda."),
        ],
        "antonyms": [("지상", "yer usti")],
    },
    {
        "word": "인구", "hanja": "人口", "roots": ["구"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 170,
        "meaning": "aholi soni — so‘zma-so‘z «odam og‘izlari»",
        "collocation": "인구가 증가하다 · 인구 감소 · 인구 밀도",
        "note": "<p><b>쓰기 53 ning eng ko‘p uchraydigan mavzusi.</b> "
                "인구 증가/감소, 고령화 bilan birga yodlang.</p>",
        "examples": [
            ("우리나라의 인구가 계속 줄고 있다.", "Mamlakatimiz aholisi muttasil kamayib bormoqda."),
            ("도시로 인구가 집중되고 있다.", "Aholi shaharlarga to‘planmoqda."),
        ],
    },
]
