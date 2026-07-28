# -*- coding: utf-8 -*-
"""Vocab bank — 어근 2: odam, ta'lim va jamiyat o'zaklari.

人 者 學 生 會 社 國 民 員 家 — order decade 200-299.
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
        "syllable": "인", "hanja": "人", "order": 200,
        "meaning": "odam — inson",
        "note": "<p>So‘z boshida ham (인구, 인간), oxirida ham (개인, 성인) keladi. "
                "⚠️ <b>인(認)</b> = tanimoq (인정, 확인) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "자", "hanja": "者", "order": 210,
        "meaning": "kishi — «...bilan shug‘ullanuvchi odam»",
        "note": "<p>Kasb va rol yasaydi, doim so‘z <b>oxirida</b>: 학자, 기자, 소비자, "
                "환자. «-chi/-uvchi» qo‘shimchasiga o‘xshaydi. "
                "⚠️ <b>자(自)</b> = o‘zi (자유, 자동) — boshqa o‘zak.</p>",
    },
    {
        "syllable": "학", "hanja": "學", "order": 220,
        "meaning": "ilm — o‘qish, fan",
        "note": "<p>Ta’lim so‘zlarining o‘zagi: 학교, 학생, 대학, 유학. "
                "Fan nomlarini ham yasaydi: 과학, 문학, 경제학.</p>",
    },
    {
        "syllable": "생", "hanja": "生", "order": 230,
        "meaning": "hayot — tug‘ilmoq, yashash",
        "note": "<p>Ikki yo‘nalish: <b>hayot</b> (생활, 인생, 생명) va "
                "<b>paydo bo‘lish</b> (발생, 생산).</p>",
    },
    {
        "syllable": "회", "hanja": "會", "order": 240,
        "meaning": "yig‘ilish — jamoa, uchrashuv",
        "note": "<p>Odamlar to‘planishi: 회사, 회의, 사회, 대회, 기회.</p>",
    },
    {
        "syllable": "사", "hanja": "社", "order": 250,
        "meaning": "jamiyat, tashkilot",
        "note": "<p>⚠️ 사 bo‘g‘ini eng ko‘p omonimli o‘zak: <b>사(社)</b> jamiyat (사회), "
                "<b>사(事)</b> ish (사업), <b>사(使)</b> ishlatmoq (사용), "
                "<b>사(死)</b> o‘lim. Hanja’sini eslab qoling.</p>",
    },
    {
        "syllable": "국", "hanja": "國", "order": 260,
        "meaning": "davlat — mamlakat",
        "note": "<p>한국, 외국, 국제, 국민, 국가. 국제(國際) = «davlatlararo» → xalqaro.</p>",
    },
    {
        "syllable": "민", "hanja": "民", "order": 270,
        "meaning": "xalq — fuqaro",
        "note": "<p>국민 (fuqaro), 시민 (shahar aholisi), 농민 (dehqon), 민족 (millat).</p>",
    },
    {
        "syllable": "원", "hanja": "員", "order": 280,
        "meaning": "a’zo — xodim",
        "note": "<p>⚠️ Ikki xil 원 ni farqlang: <b>원(員)</b> = a’zo/xodim (회원, 직원), "
                "<b>원(院)</b> = muassasa (병원, 학원). Ma’no butunlay boshqa.</p>",
    },
    {
        "syllable": "가", "hanja": "家", "order": 290,
        "meaning": "uy — oila; mutaxassis",
        "note": "<p>Ikki ma’no: <b>uy/oila</b> (가족, 가정, 국가) va "
                "<b>mutaxassis</b> (작가, 화가, 전문가).</p>",
    },
]

WORDS = [
    # ── 인(人) ─────────────────────────────────────────────────────────────
    {
        "word": "인간", "hanja": "人間", "roots": ["인"],
        "pos": "noun", "topic": "person", "level": 4, "freq": 3, "order": 200,
        "meaning": "inson — «odam + oraliq»",
        "collocation": "인간관계 · 인간적이다 · 인간의 삶",
        "note": "<p><b>사람</b> = kundalik «odam»; <b>인간</b> = falsafiy/ilmiy «inson». "
                "쓰기 54 da 인간 ishlating.</p>",
        "examples": [
            ("인간관계가 좋아야 직장 생활이 편하다.", "Odamlar bilan munosabat yaxshi bo‘lsa, ish hayoti oson bo‘ladi."),
        ],
        "synonyms": [("사람", "사람 = og‘zaki, kundalik; 인간 = kitobiy, umumlashgan")],
    },
    {
        "word": "개인", "hanja": "個人", "roots": ["인"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 201,
        "meaning": "shaxs, yakka odam — «dona + odam»",
        "collocation": "개인적이다 · 개인 정보 · 개인주의",
        "note": "<p><b>쓰기 54 uchun kalit juftlik:</b> 개인 ↔ 사회 / 집단. "
                "Munozara inshosida ikki tomonni shu bilan qo‘yasiz.</p>",
        "examples": [
            ("개인의 자유도 중요하지만 사회의 질서도 필요하다.", "Shaxs erkinligi ham muhim, lekin jamiyat tartibi ham zarur."),
        ],
        "antonyms": [("사회", "jamiyat — yakka shaxsga qarshi qo‘yiladi")],
    },
    {
        "word": "성인", "hanja": "成人", "roots": ["인"],
        "pos": "noun", "topic": "person", "level": 3, "freq": 2, "order": 202,
        "meaning": "voyaga yetgan kishi, kattalar",
        "collocation": "성인이 되다 · 성인 남녀",
        "examples": [
            ("한국에서는 만 19세부터 성인이다.", "Koreyada 19 yoshdan kattalar hisoblanadi."),
        ],
        "antonyms": [("미성년자", "voyaga yetmagan")],
    },
    {
        "word": "인기", "hanja": "人氣", "roots": ["인"],
        "pos": "noun", "topic": "culture", "level": 2, "freq": 3, "order": 203,
        "meaning": "mashhurlik, ommaboplik — «odam + kayfiyat»",
        "collocation": "인기가 많다 · 인기를 끌다 · 인기 있는",
        "examples": [
            ("이 드라마가 요즘 인기가 아주 많아요.", "Bu serial hozir juda mashhur."),
        ],
    },

    # ── 자(者) ─────────────────────────────────────────────────────────────
    {
        "word": "소비자", "hanja": "消費者", "roots": ["자(者)"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 210,
        "meaning": "iste’molchi — «sarflovchi kishi»",
        "collocation": "소비자 물가 · 소비자 보호 · 소비자의 선택",
        "note": "<p><b>쓰기 53 da doim uchraydi.</b> Juftligi — 생산자 (ishlab chiqaruvchi).</p>",
        "examples": [
            ("소비자들은 값보다 품질을 더 중요하게 생각한다.", "Iste’molchilar narxdan ko‘ra sifatni muhimroq deb biladi."),
        ],
        "antonyms": [("생산자", "ishlab chiqaruvchi")],
    },
    {
        "word": "기자", "hanja": "記者", "roots": ["자(者)"],
        "pos": "noun", "topic": "media", "level": 3, "freq": 2, "order": 211,
        "meaning": "jurnalist — «yozuvchi kishi»",
        "collocation": "기자 회견 · 신문 기자",
        "examples": [
            ("기자가 시장에게 질문을 했다.", "Jurnalist merga savol berdi."),
        ],
    },
    {
        "word": "환자", "hanja": "患者", "roots": ["자(者)"],
        "pos": "noun", "topic": "body", "level": 3, "freq": 2, "order": 212,
        "meaning": "bemor — «kasal kishi»",
        "collocation": "환자를 치료하다 · 입원 환자",
        "examples": [
            ("의사가 환자를 진찰하고 있다.", "Shifokor bemorni ko‘rikdan o‘tkazyapti."),
        ],
    },
    {
        "word": "학자", "hanja": "學者", "roots": ["자(者)", "학"],
        "pos": "noun", "topic": "science", "level": 4, "freq": 2, "order": 213,
        "meaning": "olim — «ilm kishisi»",
        "collocation": "학자들의 연구 · 유명한 학자",
        "note": "<p>Ikki o‘zak birga: 學(ilm) + 者(kishi). 쓰기 54 da manba ko‘rsatishda: "
                "<i>많은 학자들은 ...다고 주장한다.</i></p>",
        "examples": [
            ("많은 학자들이 이 문제를 연구해 왔다.", "Ko‘p olimlar bu masalani tadqiq qilib kelgan."),
        ],
    },

    # ── 학(學) ─────────────────────────────────────────────────────────────
    {
        "word": "학생", "hanja": "學生", "roots": ["학", "생"],
        "pos": "noun", "topic": "school", "level": 1, "freq": 3, "order": 220,
        "meaning": "o‘quvchi, talaba — «ilm + hayot»",
        "collocation": "대학생 · 유학생 · 학생증",
        "examples": [
            ("저는 한국어를 배우는 학생이에요.", "Men koreys tilini o‘rganayotgan talabaman."),
        ],
    },
    {
        "word": "유학", "hanja": "留學", "roots": ["학"],
        "pos": "noun", "topic": "school", "level": 3, "freq": 2, "order": 221,
        "meaning": "chet elda o‘qish — «qolib + o‘qish»",
        "collocation": "유학하다 · 유학생 · 유학을 가다",
        "examples": [
            ("셰르베크는 한국으로 유학을 갈 계획이다.", "Sherbek Koreyaga o‘qishga borishni rejalashtiryapti."),
        ],
    },
    {
        "word": "학원", "hanja": "學院", "roots": ["학"],
        "pos": "noun", "topic": "school", "level": 2, "freq": 2, "order": 222,
        "meaning": "xususiy o‘quv markazi, kurs",
        "collocation": "학원에 다니다 · 어학원 · 학원비",
        "note": "<p>⚠️ Bu yerdagi <b>원</b> = 院 (muassasa), 員 (a’zo) emas.</p>",
        "examples": [
            ("저녁마다 어학원에 다녀요.", "Har kuni kechqurun til kursiga qatnayman."),
        ],
    },
    {
        "word": "과학", "hanja": "科學", "roots": ["학"],
        "pos": "noun", "topic": "science", "level": 3, "freq": 3, "order": 223,
        "meaning": "fan",
        "collocation": "과학 기술 · 과학적이다 · 과학자",
        "examples": [
            ("과학 기술의 발전이 삶을 바꾸고 있다.", "Fan-texnika taraqqiyoti hayotni o‘zgartirmoqda."),
        ],
    },

    # ── 생(生) ─────────────────────────────────────────────────────────────
    {
        "word": "생활", "hanja": "生活", "roots": ["생"],
        "pos": "noun", "topic": "daily", "level": 2, "freq": 3, "order": 230,
        "meaning": "turmush, hayot tarzi — «yashash + faoliyat»",
        "collocation": "생활하다 · 일상생활 · 생활비 · 학교생활",
        "note": "<p><b>인생</b> = butun umr (falsafiy); <b>생활</b> = kundalik turmush.</p>",
        "examples": [
            ("한국 생활에 잘 적응했어요.", "Koreyadagi hayotga yaxshi moslashdim."),
        ],
        "related": [("인생", "인생 = butun umr; 생활 = kundalik turmush")],
    },
    {
        "word": "인생", "hanja": "人生", "roots": ["인", "생"],
        "pos": "noun", "topic": "abstract", "level": 4, "freq": 2, "order": 231,
        "meaning": "umr, inson hayoti — «odam + hayot»",
        "collocation": "인생을 살다 · 인생의 목표 · 인생 경험",
        "examples": [
            ("인생에서 가장 중요한 것은 건강이다.", "Hayotda eng muhimi — sog‘liq."),
        ],
    },
    {
        "word": "생산", "hanja": "生産", "roots": ["생"],
        "pos": "noun", "topic": "economy", "level": 4, "freq": 3, "order": 232,
        "meaning": "ishlab chiqarish — «paydo qilib + tug‘dirish»",
        "collocation": "생산하다 · 생산량 · 대량 생산",
        "examples": [
            ("이 공장에서는 자동차를 생산한다.", "Bu zavodda avtomobil ishlab chiqariladi."),
        ],
        "antonyms": [("소비", "iste’mol qilish")],
    },
    {
        "word": "생명", "hanja": "生命", "roots": ["생"],
        "pos": "noun", "topic": "science", "level": 5, "freq": 2, "order": 233,
        "meaning": "jon, hayot — «hayot + buyruq»",
        "collocation": "생명을 구하다 · 생명 과학 · 생명의 소중함",
        "examples": [
            ("모든 생명은 소중하다.", "Har bir jon qadrlidir."),
        ],
    },

    # ── 회(會) · 사(社) ────────────────────────────────────────────────────
    {
        "word": "사회", "hanja": "社會", "roots": ["회", "사"],
        "pos": "noun", "topic": "society", "level": 3, "freq": 3, "order": 240,
        "meaning": "jamiyat — «jamoa + yig‘ilish»",
        "collocation": "현대 사회 · 사회 문제 · 사회적이다",
        "note": "<p><b>쓰기 54 ning eng ko‘p ishlatiladigan so‘zi.</b> Tayyor qolip: "
                "<i>현대 사회에서 [주제]은/는 점점 더 중요한 문제가 되고 있다.</i></p>",
        "examples": [
            ("현대 사회에서는 정보가 매우 중요하다.", "Zamonaviy jamiyatda axborot juda muhim."),
        ],
        "antonyms": [("개인", "shaxs — jamiyatga qarshi qo‘yiladi")],
    },
    {
        "word": "회사", "hanja": "會社", "roots": ["회", "사"],
        "pos": "noun", "topic": "work", "level": 1, "freq": 3, "order": 241,
        "meaning": "kompaniya, firma",
        "collocation": "회사에 다니다 · 회사원 · 대기업 회사",
        "note": "<p>⚠️ 사회 va 회사 — <b>bir xil ikki bo‘g‘in, teskari tartibda</b>, "
                "ma’nosi butunlay boshqa. TOPIK 듣기 da atayin chalkashtiradi!</p>",
        "examples": [
            ("아버지는 무역 회사에 다니세요.", "Otam savdo kompaniyasida ishlaydilar."),
        ],
    },
    {
        "word": "회의", "hanja": "會議", "roots": ["회"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 3, "order": 242,
        "meaning": "yig‘ilish, majlis",
        "collocation": "회의하다 · 회의 중 · 회의실",
        "examples": [
            ("오후 두 시에 회의가 있습니다.", "Soat ikkida yig‘ilish bor."),
        ],
    },
    {
        "word": "기회", "hanja": "機會", "roots": ["회"],
        "pos": "noun", "topic": "abstract", "level": 3, "freq": 3, "order": 243,
        "meaning": "imkoniyat, fursat",
        "collocation": "기회를 잡다 · 기회를 놓치다 · 좋은 기회",
        "examples": [
            ("이번이 마지막 기회예요.", "Bu safargisi oxirgi imkoniyat."),
        ],
    },

    # ── 국(國) · 민(民) ────────────────────────────────────────────────────
    {
        "word": "국제", "hanja": "國際", "roots": ["국"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 3, "order": 260,
        "meaning": "xalqaro — «davlat + oraliq»",
        "collocation": "국제적이다 · 국제 사회 · 국제 관계",
        "examples": [
            ("국제 사회의 협력이 필요하다.", "Xalqaro hamjamiyatning hamkorligi zarur."),
        ],
    },
    {
        "word": "외국", "hanja": "外國", "roots": ["국"],
        "pos": "noun", "topic": "place", "level": 1, "freq": 3, "order": 261,
        "meaning": "chet el — «tashqari + davlat»",
        "collocation": "외국어 · 외국인 · 외국에 살다",
        "examples": [
            ("외국인 친구가 세 명 있어요.", "Uchta chet ellik do‘stim bor."),
        ],
    },
    {
        "word": "국민", "hanja": "國民", "roots": ["국", "민"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 2, "order": 270,
        "meaning": "fuqaro, xalq — «davlat + xalq»",
        "collocation": "국민의 권리 · 국민 건강 보험",
        "examples": [
            ("정부는 국민의 의견을 들어야 한다.", "Hukumat xalqning fikrini eshitishi kerak."),
        ],
    },
    {
        "word": "시민", "hanja": "市民", "roots": ["민"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 2, "order": 271,
        "meaning": "shahar aholisi, fuqaro",
        "collocation": "시민 단체 · 시민 의식 · 시민 참여",
        "examples": [
            ("많은 시민들이 행사에 참여했다.", "Ko‘plab shahar aholisi tadbirda qatnashdi."),
        ],
    },

    # ── 원(員) · 가(家) ────────────────────────────────────────────────────
    {
        "word": "직원", "hanja": "職員", "roots": ["원"],
        "pos": "noun", "topic": "work", "level": 2, "freq": 3, "order": 280,
        "meaning": "xodim, ishchi — «vazifa + a’zo»",
        "collocation": "직원을 뽑다 · 신입 직원 · 직원 회의",
        "examples": [
            ("우리 회사 직원은 오십 명입니다.", "Bizning kompaniyada ellik xodim bor."),
        ],
    },
    {
        "word": "회원", "hanja": "會員", "roots": ["회", "원"],
        "pos": "noun", "topic": "society", "level": 2, "freq": 2, "order": 281,
        "meaning": "a’zo — «jamoa + a’zo»",
        "collocation": "회원 가입 · 회원증 · 정회원",
        "examples": [
            ("회원 가입을 하시면 할인을 받으실 수 있습니다.", "A’zo bo‘lsangiz chegirma olishingiz mumkin."),
        ],
    },
    {
        "word": "가족", "hanja": "家族", "roots": ["가"],
        "pos": "noun", "topic": "person", "level": 1, "freq": 3, "order": 290,
        "meaning": "oila — «uy + urug‘»",
        "collocation": "가족과 함께 · 가족 사진 · 핵가족",
        "examples": [
            ("주말에는 가족과 함께 시간을 보내요.", "Dam olish kunlari oilam bilan vaqt o‘tkazaman."),
        ],
    },
    {
        "word": "전문가", "hanja": "專門家", "roots": ["가"],
        "pos": "noun", "topic": "work", "level": 4, "freq": 3, "order": 291,
        "meaning": "mutaxassis, ekspert — «maxsus + soha + kishi»",
        "collocation": "전문가의 의견 · 전문가에 따르면",
        "note": "<p><b>쓰기 53/54 uchun oltin ibora:</b> "
                "<i>전문가들은 ...(으)ㄹ 것으로 전망한다.</i></p>",
        "examples": [
            ("전문가들은 상황이 나아질 것으로 본다.", "Mutaxassislar vaziyat yaxshilanadi deb hisoblaydi."),
        ],
        "related": [("학자", "학자 = ilmiy tadqiqotchi; 전문가 = amaliy soha bilimdoni")],
    },
    {
        "word": "국가", "hanja": "國家", "roots": ["국", "가"],
        "pos": "noun", "topic": "society", "level": 4, "freq": 2, "order": 292,
        "meaning": "davlat — «davlat + uy»",
        "collocation": "국가 정책 · 국가 경제 · 선진 국가",
        "note": "<p><b>나라</b> = kundalik «davlat»; <b>국가</b> = rasmiy/siyosiy atama.</p>",
        "examples": [
            ("국가 차원의 대책이 필요하다.", "Davlat darajasidagi chora-tadbir zarur."),
        ],
        "synonyms": [("나라", "나라 = og‘zaki, sof koreyscha; 국가 = rasmiy, yozma")],
    },
]
