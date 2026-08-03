# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-86 … PK-88.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Har uchala mashqda bitta 한다체 (PK-74) savoli bor.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_86_88.py --master=prime \\
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
# PK-86 — (으)ㅁ으로써
# ══════════════════════════════════════════════════════════════════════
Q_PK86 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)ㅁ으로써</b> qanday maʼno beradi?</p>",
        "choices": ["…ish yoʻli bilan (vosita)",
                    "… sifatida (maqom)",
                    "…ay deb turibman",
                    "…ishi mumkin emas"],
        "correct": "…ish yoʻli bilan (vosita)",
        "explanation": "<p>Harakatning oʻzi vositaga aylanadi: "
                       "대화<b>함으로써</b> 문제를 해결했다.</p>",
    },
    {
        "text": "<p>(으)ㅁ으로써 qaysi ikki tanish qismdan yasaladi?</p>",
        "choices": ["PK-46 dagi (으)ㅁ otlashtirishi + (으)로 vosita "
                    "qoʻshimchasi",
                    "PK-43 dagi 는 + 것",
                    "PK-56 dagi majhul nisbat + 다",
                    "PK-33 dagi 고 + 서"],
        "correct": "PK-46 dagi (으)ㅁ otlashtirishi + (으)로 vosita "
                   "qoʻshimchasi",
        "explanation": "<p>대화하다 → 대화<b>함</b> → 대화함<b>으로써</b>.</p>",
    },
    {
        "text": "<p><b>써</b> qaysi feʼldan kelib chiqqan va nimani "
                "bildiradi?</p>",
        "choices": ["쓰다 (“ishlatmoq”) — asbob, vosita",
                    "서다 (“turmoq”) — oʻrin, maqom",
                    "쓰다 (“yozmoq”) — hujjat",
                    "싸다 (“arzon”) — narx"],
        "correct": "쓰다 (“ishlatmoq”) — asbob, vosita",
        "explanation": "<p>Shuning uchun 로<b>써</b> = “nima bilan?”.</p>",
    },
    {
        "text": "<p><b>서</b> qaysi feʼldan va nimani bildiradi?</p>",
        "choices": ["서다 (“turmoq”) — oʻrin, maqom, rol",
                    "쓰다 (“ishlatmoq”) — asbob",
                    "사다 (“sotib olmoq”) — narx",
                    "세다 (“sanamoq”) — miqdor"],
        "correct": "서다 (“turmoq”) — oʻrin, maqom, rol",
        "explanation": "<p>로<b>서</b> = “kim sifatida?”. "
                       "학생으로서, 친구로서.</p>",
    },
    {
        "text": "<p>(으)ㅁ으로써 qaysi uslubga tegishli?</p>",
        "choices": ["Rasmiy yozma til — maqola, hisobot, TOPIK 쓰기",
                    "Kundalik suhbat",
                    "Bolalar tili",
                    "Faqat soʻroq gaplarda"],
        "correct": "Rasmiy yozma til — maqola, hisobot, TOPIK 쓰기",
        "explanation": "<p>Kundalik gapda oddiy <b>아/어서</b> (PK-35) "
                       "yetarli.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 우리는 <b>____</b> 문제를 해결했다. "
                "(대화하다)</p>",
        "choices": ["대화함으로써", "대화하음으로써", "대화해으로써",
                    "대화하는으로써"],
        "correct": "대화함으로써",
        "explanation": "<p>하다 → <b>함</b>. ❌ 하음 degan shakl yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 매일 십 분씩 <b>____</b> 실력이 늘었다. "
                "(읽다)</p>",
        "choices": ["읽음으로써", "읽ㅁ으로써", "읽어으로써", "읽는음으로써"],
        "correct": "읽음으로써",
        "explanation": "<p>읽 da 받침 bor → <b>음</b> + 으로써.</p>",
    },
    {
        "text": "<p>Toʻldiring: 학생<b>____</b> 열심히 공부해야 한다.</p>",
        "choices": ["으로서", "으로써", "으로", "으로부터"],
        "correct": "으로서",
        "explanation": "<p>“Oʻquvchi <b>sifatida</b>” — maqom, "
                       "demak 로서.</p>",
    },
    {
        "text": "<p>Toʻldiring: 대화<b>____</b> 문제를 해결했다.</p>",
        "choices": ["로써", "로서", "로부터", "처럼"],
        "correct": "로써",
        "explanation": "<p>Suhbat — <b>vosita</b>, demak 로써.</p>",
    },
    {
        "text": "<p>Toʻldiring: 쓰레기봉투를 <b>____</b> 쓰레기가 크게 "
                "줄었다. (유료화하다)</p>",
        "choices": ["유료화함으로써", "유료화하음으로써", "유료화해서로써",
                    "유료화하는 것으로써"],
        "correct": "유료화함으로써",
        "explanation": "<p>하다 tugagan feʼllar hamisha <b>함</b> "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>TOPIK 쓰기 da grafik tahlili uchun tayyor jumla "
                "qaysi biri?</p>",
        "choices": ["정책을 시행함으로써 사고가 감소하였다.",
                    "정책을 시행해서 사고가 줄었어요.",
                    "정책을 시행할 지경이다.",
                    "정책을 시행할 리가 없다."],
        "correct": "정책을 시행함으로써 사고가 감소하였다.",
        "explanation": "<p>“Nima qilish bilan natija oʻzgardi” — "
                       "쓰기 51-54 ning eng koʻp kerak boʻladigan "
                       "jumlasi.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "대화함으로써 문제를 해결했어요.</p>",
        "choices": ["대화함으로써 문제를 해결했다.",
                    "대화함으로써 문제를 해결한다.",
                    "대화함으로써 문제를 해결했는다.",
                    "대화함으로써 문제를 해결하다."],
        "correct": "대화함으로써 문제를 해결했다.",
        "explanation": "<p>Oʻtgan zamon 한다체 da <b>았/었다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>로써 va 로서 ni qanday tekshirasiz?</p>",
        "choices": ["Savol bilan: “nima bilan?” → 로써 · “kim sifatida?” → "
                    "로서",
                    "Zamon bilan: oʻtgan → 로써, hozirgi → 로서",
                    "받침 bilan: bor → 로써, yoʻq → 로서",
                    "Uslub bilan: rasmiy → 로써, ogʻzaki → 로서"],
        "correct": "Savol bilan: “nima bilan?” → 로써 · “kim sifatida?” → "
                   "로서",
        "explanation": "<p>Va ilgak: <b>쓰</b>다 = ishlatmoq (asbob) ↔ "
                       "<b>서</b>다 = turmoq (oʻrin).</p>",
    },
    {
        "text": "<p><b>(으)로</b> (PK-14) va <b>(으)ㅁ으로써</b> farqi "
                "nima?</p>",
        "choices": ["(으)로 — oddiy moddiy asbob (연필로); (으)ㅁ으로써 — "
                    "harakatning oʻzi vosita, rasmiy yozma",
                    "(으)로 — oʻtgan zamon; (으)ㅁ으로써 — kelasi",
                    "(으)로 — feʼl bilan; (으)ㅁ으로써 — ot bilan",
                    "Farqi yoʻq"],
        "correct": "(으)로 — oddiy moddiy asbob (연필로); (으)ㅁ으로써 — "
                   "harakatning oʻzi vosita, rasmiy yozma",
        "explanation": "<p>연필<b>로</b> 썼어요 ↔ 대화<b>함으로써</b> "
                       "해결했다.</p>",
    },
    {
        "text": "<p>Doʻstingizga “gaplashib hal qilaylik” demoqchisiz. "
                "Qaysi shakl tabiiy?</p>",
        "choices": ["얘기해서 풀자", "대화함으로써 풀자",
                    "대화로써 풀자", "대화로서 풀자"],
        "correct": "얘기해서 풀자",
        "explanation": "<p>(으)ㅁ으로써 — <b>qogʻoz uchun</b>. Kundalik "
                       "gapda 아/어서.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["학생으로써 열심히 공부해야 한다.",
                    "학생으로서 열심히 공부해야 한다.",
                    "대화로써 문제를 해결했다.",
                    "대화함으로써 문제를 해결했다."],
        "correct": "학생으로써 열심히 공부해야 한다.",
        "explanation": "<p>“Oʻquvchi sifatida” — <b>maqom</b>, demak "
                       "로<b>서</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>대화하음으로써 문제를 해결했다.</s></p>",
        "choices": ["하 da 받침 yoʻq — 함으로써 boʻlishi kerak",
                    "문제를 emas, 문제가",
                    "해결했다 emas, 해결한다",
                    "으로써 emas, 으로서"],
        "correct": "하 da 받침 yoʻq — 함으로써 boʻlishi kerak",
        "explanation": "<p>받침 yoʻq → <b>ㅁ</b>, 받침 bor → <b>음</b>.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>읽는 것으로써 실력이 늘었다.</s></p>",
        "choices": ["Bu qolipda (으)ㅁ ishlatiladi — 읽음으로써",
                    "실력이 emas, 실력을",
                    "늘었다 emas, 늘었어요",
                    "으로써 emas, 으로"],
        "correct": "Bu qolipda (으)ㅁ ishlatiladi — 읽음으로써",
        "explanation": "<p>는 것 emas — <b>(으)ㅁ</b> otlashtirishi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Chiqindi paketini pullik qilish bilan chiqindi "
                "kamaydi” — koreyschada?</p>",
        "choices": ["쓰레기봉투를 유료화함으로써 쓰레기가 줄었다.",
                    "쓰레기봉투를 유료화하음으로써 쓰레기가 줄었다.",
                    "쓰레기봉투를 유료화로서 쓰레기가 줄었다.",
                    "쓰레기봉투를 유료화할 지경이다."],
        "correct": "쓰레기봉투를 유료화함으로써 쓰레기가 줄었다.",
        "explanation": "<p>Chora — <b>vosita</b>, natija — kamayish. "
                       "Bu 정보문 ning tipik jumlasi.</p>",
    },
    {
        "text": "<p>“Doʻst sifatida aytyapman” — koreyschada?</p>",
        "choices": ["친구로서 하는 말이다.", "친구로써 하는 말이다.",
                    "친구함으로써 하는 말이다.", "친구로 하는 말이다."],
        "correct": "친구로서 하는 말이다.",
        "explanation": "<p>“Sifatida” = <b>maqom</b> = 로서.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-87 — (으)ㄹ 지경이다
# ══════════════════════════════════════════════════════════════════════
Q_PK87 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)ㄹ 지경이다</b> qanday maʼno beradi?</p>",
        "choices": ["…ay deb turibman — chegaraga yetgan holat",
                    "…ish yoʻli bilan",
                    "…ishi mumkin emas",
                    "…gandan koʻra yaxshiroq"],
        "correct": "…ay deb turibman — chegaraga yetgan holat",
        "explanation": "<p>Ish hali boʻlmagan — unga bir qadam "
                       "qolgan.</p>",
    },
    {
        "text": "<p><b>지경</b> (地境) soʻzma-soʻz nimani bildiradi?</p>",
        "choices": ["Yer chegarasi", "Aql, mantiq", "Holat, koʻrinish",
                    "Daraja, oʻlcham"],
        "correct": "Yer chegarasi",
        "explanation": "<p>Shuning uchun qolip “… boʻladigan chegarada "
                       "turibman” degani.</p>",
    },
    {
        "text": "<p>지경이다 dagi holat qanday boʻladi?</p>",
        "choices": ["Deyarli har doim yomon", "Deyarli har doim yaxshi",
                    "Betaraf", "Faqat rasmiy vaziyatlar"],
        "correct": "Deyarli har doim yomon",
        "explanation": "<p>죽다, 미치다, 쓰러지다, 울다 — qolipning odatiy "
                       "sheriklari.</p>",
    },
    {
        "text": "<p>지경 oldida qanday aniqlovchi turadi?</p>",
        "choices": ["Hamisha (으)ㄹ", "Hamisha 는", "Hamisha (으)ㄴ",
                    "Aniqlovchi kerak emas"],
        "correct": "Hamisha (으)ㄹ",
        "explanation": "<p>Holat hali <b>boʻlmagan</b> — shuning uchun "
                       "kelasi aniqlovchisi.</p>",
    },
    {
        "text": "<p><b>이 지경이 되다</b> nimani bildiradi?</p>",
        "choices": ["“Shu ahvolga kelmoq”", "“Shu joyga bormoq”",
                    "“Shu darajada yaxshi boʻlmoq”", "“Shu vaqtda tugamoq”"],
        "correct": "“Shu ahvolga kelmoq”",
        "explanation": "<p>지경 mustaqil ot ham — “ahvol, holat”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 배가 고파서 <b>____</b> 지경이에요. "
                "(쓰러지다)</p>",
        "choices": ["쓰러질", "쓰러지는", "쓰러진", "쓰러져"],
        "correct": "쓰러질",
        "explanation": "<p>지경 oldida <b>(으)ㄹ</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 일이 너무 많아서 <b>____</b> 지경이다. "
                "(미치다)</p>",
        "choices": ["미칠", "미치는", "미친", "미쳐"],
        "correct": "미칠",
        "explanation": "<p><b>미칠 지경이다</b> — eng koʻp uchraydigan "
                       "tayyor iboralardan biri.</p>",
    },
    {
        "text": "<p>Toʻldiring: 사흘 동안 못 자서 <b>____</b> "
                "지경이었다. (죽다)</p>",
        "choices": ["죽을", "죽는", "죽은", "죽어"],
        "correct": "죽을",
        "explanation": "<p><b>죽을 지경이다</b> = “oʻlay deb turibman”.</p>",
    },
    {
        "text": "<p>Toʻldiring: 너무 슬퍼서 <b>____</b> 지경이었어요. "
                "(울다)</p>",
        "choices": ["울", "우는", "운", "울어"],
        "correct": "울",
        "explanation": "<p>울다 — ㄹ tushadi: 울 + ㄹ → <b>울</b>. "
                       "“Yigʻlab yuboray dedim.”</p>",
    },
    {
        "text": "<p>“Qanday qilib shu ahvolga tushdik ekan” — "
                "koreyschada?</p>",
        "choices": ["어쩌다가 이 지경이 되었을까 생각했다.",
                    "어쩌다가 이 정도로 되었을까 생각했다.",
                    "어쩌다가 이 지경으로 했을까 생각했다.",
                    "어쩌다가 이 리가 없었을까 생각했다."],
        "correct": "어쩌다가 이 지경이 되었을까 생각했다.",
        "explanation": "<p><b>이 지경이 되다</b> — tayyor ibora.</p>",
    },
    {
        "text": "<p>지경이다 oldida koʻpincha nima turadi?</p>",
        "choices": ["Sabab — 아/어서 yoki (으)니까",
                    "Maqsad — (으)려고",
                    "Shart — (으)면",
                    "Vaqt — 기 전에"],
        "correct": "Sabab — 아/어서 yoki (으)니까",
        "explanation": "<p>배가 고<b>파서</b> 죽을 지경이에요 — avval sabab, "
                       "keyin chegara.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "배가 고파서 죽을 지경이에요.</p>",
        "choices": ["배가 고파서 죽을 지경이다.",
                    "배가 고파서 죽을 지경인다.",
                    "배가 고파서 죽을 지경이었다.",
                    "배가 고파서 죽는 지경이다."],
        "correct": "배가 고파서 죽을 지경이다.",
        "explanation": "<p>이다 한다체 da <b>이다</b> boʻlib qoladi.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>(으)ㄹ 정도로</b> (PK-82) va <b>(으)ㄹ 지경이다</b> "
                "farqi nima?</p>",
        "choices": ["정도로 gap oʻrtasida turadi va darajani oʻlchaydi; "
                    "지경이다 gap oxirida turadi va holatni aytadi",
                    "정도로 — oʻtgan zamon; 지경이다 — kelasi",
                    "정도로 — yomon; 지경이다 — yaxshi",
                    "Farqi yoʻq"],
        "correct": "정도로 gap oʻrtasida turadi va darajani oʻlchaydi; "
                   "지경이다 gap oxirida turadi va holatni aytadi",
        "explanation": "<p>배가 아플 <b>정도로 웃었어요</b> (keyin feʼl bor) ↔ "
                       "배가 고파서 <b>죽을 지경이에요</b> (gap tugadi).</p>",
    },
    {
        "text": "<p>Qanday oson tekshirish mumkin?</p>",
        "choices": ["Keyin yana feʼl bormi? Bor → 정도로, yoʻq → 지경이다",
                    "받침 bormi? Bor → 정도로, yoʻq → 지경이다",
                    "Zamon oʻtganmi? Ha → 정도로",
                    "Ega bittami? Ha → 지경이다"],
        "correct": "Keyin yana feʼl bormi? Bor → 정도로, yoʻq → 지경이다",
        "explanation": "<p>정도로 oʻzidan keyingi feʼlni oʻlchaydi; "
                       "지경이다 esa gapning oʻzi.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["너무 기뻐서 춤출 지경이에요.",
                    "배가 고파서 쓰러질 지경이에요.",
                    "일이 많아서 미칠 지경이다.",
                    "못 자서 죽을 지경이었다."],
        "correct": "너무 기뻐서 춤출 지경이에요.",
        "explanation": "<p>지경 — <b>yomon</b> holat uchun. Quvonch uchun "
                       "<b>춤출 정도로 좋았어요</b>.</p>",
    },
    {
        "text": "<p>“Qornim ogʻriydigan darajada kuldim” — qaysi qolip?</p>",
        "choices": ["배가 아플 정도로 웃었어요.",
                    "배가 아플 지경으로 웃었어요.",
                    "배가 아플 지경이에요 웃었어요.",
                    "배가 아픈 정도로 웃었어요."],
        "correct": "배가 아플 정도로 웃었어요.",
        "explanation": "<p>Keyin 웃었어요 turibdi — demak oʻlchov "
                       "<b>정도로</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>배가 고파서 죽은 지경이에요.</s></p>",
        "choices": ["지경 oldida (으)ㄹ kerak — 죽을 지경이에요",
                    "고파서 emas, 고프니까",
                    "배가 emas, 배는",
                    "지경이에요 emas, 지경이다"],
        "correct": "지경 oldida (으)ㄹ kerak — 죽을 지경이에요",
        "explanation": "<p>Holat hali sodir boʻlmagan — 은/는 emas.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>죽을 지경으로 배가 고파요.</s></p>",
        "choices": ["지경 gapning oxirida, 이다 bilan turadi — "
                    "배가 고파서 죽을 지경이에요",
                    "죽을 emas, 죽는",
                    "배가 emas, 배는",
                    "고파요 emas, 고픕니다"],
        "correct": "지경 gapning oxirida, 이다 bilan turadi — "
                   "배가 고파서 죽을 지경이에요",
        "explanation": "<p>Gap oʻrtasida oʻlchov kerak boʻlsa — "
                       "<b>정도로</b>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Ish shunchalik koʻpki, aqldan ozay deyapman” — "
                "koreyschada?</p>",
        "choices": ["일이 너무 많아서 미칠 지경이에요.",
                    "일이 너무 많아서 미칠 정도로 해요.",
                    "일이 너무 많아서 미친 지경이에요.",
                    "일이 너무 많아서 미칠 리가 없어요."],
        "correct": "일이 너무 많아서 미칠 지경이에요.",
        "explanation": "<p>Sabab + chegara — qolipning odatiy "
                       "tuzilishi.</p>",
    },
    {
        "text": "<p>“Uch kun uxlamay, oʻlgudek holga tushdim” — "
                "koreyschada?</p>",
        "choices": ["사흘 동안 못 자서 죽을 지경이었어요.",
                    "사흘 동안 못 자서 죽는 지경이었어요.",
                    "사흘 동안 못 자서 죽을 정도예요.",
                    "사흘 동안 못 자서 죽을 리가 없어요."],
        "correct": "사흘 동안 못 자서 죽을 지경이었어요.",
        "explanation": "<p>Oʻtgan zamon <b>지경이었다</b> shaklida — "
                       "이다 tuslanadi.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-88 — (으)ㄹ 리가 없다 / (으)ㄹ 턱이 없다
# ══════════════════════════════════════════════════════════════════════
Q_PK88 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)ㄹ 리가 없다</b> qanday maʼno beradi?</p>",
        "choices": ["…ishi mumkin emas — kuchli ishonmaslik",
                    "…a olmaydi — imkoni yoʻq",
                    "…ay deb turibman",
                    "balki …ar"],
        "correct": "…ishi mumkin emas — kuchli ishonmaslik",
        "explanation": "<p>Imkon bor boʻlishi mumkin — lekin soʻzlovchi "
                       "buni haqiqat deb qabul qilmaydi.</p>",
    },
    {
        "text": "<p><b>리</b> (理) nimani bildiradi?</p>",
        "choices": ["Aql, mantiq, sabab", "Yer chegarasi",
                    "Daraja, oʻlcham", "Holat, koʻrinish"],
        "correct": "Aql, mantiq, sabab",
        "explanation": "<p>Shuning uchun qolip “bunday boʻlishining "
                       "<b>mantigʻi yoʻq</b>” degani.</p>",
    },
    {
        "text": "<p>리 oldida qanday aniqlovchi turadi?</p>",
        "choices": ["Hamisha (으)ㄹ", "Hamisha 는", "Hamisha (으)ㄴ",
                    "Aniqlovchi kerak emas"],
        "correct": "Hamisha (으)ㄹ",
        "explanation": "<p>할 리가 없다 · 올 리가 없다 · 떨어질 리가 "
                       "없다.</p>",
    },
    {
        "text": "<p>Oʻtgan zamon qanday yasaladi?</p>",
        "choices": ["았/었을 리가 없다", "(으)ㄹ 리가 없었다",
                    "는 리가 없다", "(으)ㄴ 리가 없다"],
        "correct": "았/었을 리가 없다",
        "explanation": "<p>Zamon <b>았/었을</b> ichida — 없다 da emas: "
                       "열었을 리가 없다.</p>",
    },
    {
        "text": "<p><b>(으)ㄹ 턱이 없다</b> ning ohangi qanday?</p>",
        "choices": ["Keskin va ogʻzaki — oʻzidan kattaga aytilmaydi",
                    "Juda hurmatli", "Rasmiy hujjat tili", "Iltimos ohangi"],
        "correct": "Keskin va ogʻzaki — oʻzidan kattaga aytilmaydi",
        "explanation": "<p>턱 — sof koreyscha soʻz (“asos”). Unda bir oz "
                       "“bu kulgili gap” degan soya bor.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 그 사람이 거짓말을 <b>____</b> 리가 "
                "없어요. (하다)</p>",
        "choices": ["할", "하는", "한", "해"],
        "correct": "할",
        "explanation": "<p>리 oldida <b>(으)ㄹ</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이 시간에 문을 <b>____</b> 리가 없다. "
                "(열다 — oʻtgan zamon)</p>",
        "choices": ["열었을", "열", "여는", "열은"],
        "correct": "열었을",
        "explanation": "<p>Boʻlib oʻtgan ish haqida shubha — "
                       "<b>았/었을 리가 없다</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 아프소나 씨가 시험에 <b>____</b> 리가 "
                "없어요. 매일 공부했잖아요. (떨어지다)</p>",
        "choices": ["떨어질", "떨어지는", "떨어진", "떨어져"],
        "correct": "떨어질",
        "explanation": "<p>PK-55 dagi <b>잖아요</b> bilan juda yaxshi "
                       "yuradi — ikkalasi ham dalilga ishora qiladi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그런 이야기를 그 사람이 <b>____</b> 턱이 "
                "없어요. (알다)</p>",
        "choices": ["알", "아는", "안", "알아"],
        "correct": "알",
        "explanation": "<p>알다 — ㄹ tushadi: 알 + ㄹ → <b>알</b>.</p>",
    },
    {
        "text": "<p>“Oyogʻi ogʻriydi, shuning uchun yura olmaydi” — "
                "koreyschada?</p>",
        "choices": ["다리가 아파서 걸을 수 없어요.",
                    "다리가 아파서 걸을 리가 없어요.",
                    "다리가 아파서 걸을 턱이 없어요.",
                    "다리가 아파서 걸을 지경이에요."],
        "correct": "다리가 아파서 걸을 수 없어요.",
        "explanation": "<p>Bu <b>haqiqiy imkonsizlik</b> — 수 없다 "
                       "(PK-30).</p>",
    },
    {
        "text": "<p>“U keladi deb oʻylamayman — undan kutilmaydi” — "
                "koreyschada?</p>",
        "choices": ["그 사람이 올 리가 없어요.",
                    "그 사람이 올 수 없어요.",
                    "그 사람이 올 지경이에요.",
                    "그 사람이 올지도 몰라요."],
        "correct": "그 사람이 올 리가 없어요.",
        "explanation": "<p>Imkon bor, lekin soʻzlovchi <b>ishonmaydi</b> "
                       "— 리가 없다.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "그 사람이 거짓말을 할 리가 없어요.</p>",
        "choices": ["그 사람이 거짓말을 할 리가 없다.",
                    "그 사람이 거짓말을 할 리가 없는다.",
                    "그 사람이 거짓말을 할 리가 없었다.",
                    "그 사람이 거짓말을 하는 리가 없다."],
        "correct": "그 사람이 거짓말을 할 리가 없다.",
        "explanation": "<p>없다 한다체 da <b>oʻzgarmaydi</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>(으)ㄹ 수 없다</b> va <b>(으)ㄹ 리가 없다</b> "
                "farqi nima?</p>",
        "choices": ["수 없다 — imkoni yoʻq (toʻsiq bor); 리가 없다 — imkon "
                    "bor, lekin men ishonmayman",
                    "수 없다 — ogʻzaki; 리가 없다 — yozma",
                    "수 없다 — oʻtgan zamon; 리가 없다 — hozirgi",
                    "Farqi yoʻq"],
        "correct": "수 없다 — imkoni yoʻq (toʻsiq bor); 리가 없다 — imkon "
                   "bor, lekin men ishonmayman",
        "explanation": "<p>Bu darsning eng muhim farqi. Oʻzbekchada "
                       "ikkalasi ham “mumkin emas” deb tarjima "
                       "qilinadi — shuning uchun adashish oson.</p>",
    },
    {
        "text": "<p>Ishonch zinapoyasida 리가 없다 qayerda turadi?</p>",
        "choices": ["Eng pastda — hatto (으)ㄹ지도 모르다 dan ham past, "
                    "chunki u taxmin emas, rad",
                    "Eng yuqorida",
                    "(으)ㄹ 것 같다 bilan bir darajada",
                    "Zinapoyaga kirmaydi"],
        "correct": "Eng pastda — hatto (으)ㄹ지도 모르다 dan ham past, "
                   "chunki u taxmin emas, rad",
        "explanation": "<p>거예요 → 테니까 → 것 같다 → 을지도 모르다 → "
                       "<b>리가 없다</b>.</p>",
    },
    {
        "text": "<p>Rasmiy vaziyatda qaysi shakl toʻgʻri?</p>",
        "choices": ["선생님이 그런 말을 할 리가 없습니다.",
                    "선생님이 그런 말을 할 턱이 없습니다.",
                    "선생님이 그런 말을 할 지경입니다.",
                    "선생님이 그런 말을 할 수 없습니다."],
        "correct": "선생님이 그런 말을 할 리가 없습니다.",
        "explanation": "<p>턱이 없다 — keskin va ogʻzaki, rasmiy "
                       "vaziyatga toʻgʻri kelmaydi.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["다리가 아파서 걸을 리가 없어요.",
                    "그 사람이 거짓말을 할 리가 없어요.",
                    "이 시간에 문을 열었을 리가 없다.",
                    "그런 이야기를 알 턱이 없어요."],
        "correct": "다리가 아파서 걸을 리가 없어요.",
        "explanation": "<p>Oyoq ogʻrishi — <b>haqiqiy toʻsiq</b>. "
                       "Bu 수 없다 ning oʻrni.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>그 사람이 거짓말을 하는 리가 "
                "없어요.</s></p>",
        "choices": ["리 oldida hamisha (으)ㄹ — 할 리가 없어요",
                    "거짓말을 emas, 거짓말이",
                    "없어요 emas, 없다",
                    "그 사람이 emas, 그 사람은"],
        "correct": "리 oldida hamisha (으)ㄹ — 할 리가 없어요",
        "explanation": "<p>는 yoki (으)ㄴ hech qachon ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>이 시간에 문을 열 리가 "
                "없었어요.</s> (“ochilgan boʻlishi mumkin emas” "
                "maʼnosida)</p>",
        "choices": ["Oʻtgan zamon 았/었을 ichida — 열었을 리가 없어요",
                    "문을 emas, 문이",
                    "이 시간에 emas, 이 시간이",
                    "리가 emas, 턱이"],
        "correct": "Oʻtgan zamon 았/었을 ichida — 열었을 리가 없어요",
        "explanation": "<p>없다 ni oʻtgan zamonga qoʻyish maʼnoni "
                       "buzadi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“U odamning yolgʻon gapirishi mumkin emas” — "
                "koreyschada?</p>",
        "choices": ["그 사람이 거짓말을 할 리가 없어요.",
                    "그 사람이 거짓말을 할 수 없어요.",
                    "그 사람이 거짓말을 할 지경이에요.",
                    "그 사람이 거짓말을 할지도 몰라요."],
        "correct": "그 사람이 거짓말을 할 리가 없어요.",
        "explanation": "<p>Bu — xarakterga asoslangan <b>rad</b>, "
                       "imkonsizlik emas.</p>",
    },
    {
        "text": "<p>“Bunday gapni u odam bilishiga aql bovar qilmaydi” "
                "(ogʻzaki, keskin) — koreyschada?</p>",
        "choices": ["그런 이야기를 그 사람이 알 턱이 없어요.",
                    "그런 이야기를 그 사람이 알 수 없어요.",
                    "그런 이야기를 그 사람이 알 지경이에요.",
                    "그런 이야기를 그 사람이 알 뿐이에요."],
        "correct": "그런 이야기를 그 사람이 알 턱이 없어요.",
        "explanation": "<p>턱이 없다 — 리가 없다 bilan bir xil maʼno, "
                       "lekin keskinroq.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-86 Mashq: (으)ㅁ으로써",
        "description": "20 savol — (으)ㅁ otlashtirishi, 로써 va 로서 "
                       "farqi, (으)로 dan ajratish va TOPIK 쓰기 uchun "
                       "tayyor jumla.",
        "tutorial":    "PK-86:",
        "level":       "medium",
        "questions":   Q_PK86,
    },
    {
        "title":       "PK-87 Mashq: (으)ㄹ 지경이다",
        "description": "20 savol — chegaraga yetgan holat, majburiy "
                       "(으)ㄹ aniqlovchisi, salbiylik sharti va "
                       "(으)ㄹ 정도로 dan farqi.",
        "tutorial":    "PK-87:",
        "level":       "medium",
        "questions":   Q_PK87,
    },
    {
        "title":       "PK-88 Mashq: (으)ㄹ 리가 없다 · (으)ㄹ 턱이 없다",
        "description": "20 savol — ishonmaslik va imkonsizlik farqi, "
                       "았/었을 리가 없다, ishonch zinapoyasi va "
                       "턱이 없다 ning uslubi.",
        "tutorial":    "PK-88:",
        "level":       "medium",
        "questions":   Q_PK88,
    },
]
