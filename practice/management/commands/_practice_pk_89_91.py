# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-89 … PK-91.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
PK-90 mashqi ataylab PK-87 (지경이다) bilan solishtiruvchi savollarni
oʻz ichiga oladi — oʻzbek oʻquvchisi uchun eng katta chalkashlik shu
yerda: ikkala qolip ham "…ay deb turibman" deb tarjima qilinadi.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_89_91.py --master=prime \\
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
# PK-89 — 명사 + 에 달려 있다
# ══════════════════════════════════════════════════════════════════════
Q_PK89 = [
    # 1–5 tanish
    {
        "text": "<p><b>에 달려 있다</b> qanday maʼno beradi?</p>",
        "choices": ["…ga bogʻliq",
                    "…dan farqi yoʻq",
                    "…ay deb turibman",
                    "…ishi mumkin emas"],
        "correct": "…ga bogʻliq",
        "explanation": "<p><b>성공은 노력에 달려 있다</b> — muvaffaqiyat "
                       "mehnatga bogʻliq. Qolip natijani nima hal "
                       "qilishini koʻrsatadi.</p>",
    },
    {
        "text": "<p><b>달리다</b> feʼlining bu qolipdagi asl maʼnosi nima?</p>",
        "choices": ["yugurmoq",
                    "osilib turmoq, ilinmoq",
                    "yetib bormoq",
                    "qaram boʻlmoq"],
        "correct": "osilib turmoq, ilinmoq",
        "explanation": "<p><b>시계가 벽에 달려 있다</b> — soat devorga "
                       "osilgan. Shu rasm mavhum maʼnoga koʻchadi: natija "
                       "sababga <b>osilib turadi</b>. Agar ilgak "
                       "boʻlmasa, natija tushib ketadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>성공은 ___ 달려 있다.</b> (노력)</p>",
        "choices": ["노력을", "노력이", "노력에", "노력으로"],
        "correct": "노력에",
        "explanation": "<p>Qolipning yuragi — <b>에</b> qoʻshimchasi. "
                       "달리다 oʻtimsiz feʼl, shuning uchun 을/를 "
                       "olmaydi.</p>",
    },
    {
        "text": "<p><b>그건 네 마음에 달렸어.</b> — Bu gap qaysi zamonda?</p>",
        "choices": ["Oʻtgan zamon — “bogʻliq edi”",
                    "Hozirgi zamon — “bogʻliq”",
                    "Kelasi zamon — “bogʻliq boʻladi”",
                    "Buyruq shakli"],
        "correct": "Hozirgi zamon — “bogʻliq”",
        "explanation": "<p><b>달렸다</b> — ogʻzaki nutqdagi qisqa shakl. "
                       "Shakli oʻtgan zamonga oʻxshaydi, lekin maʼnosi "
                       "hozirgi: <b>달려 있다</b> bilan bir xil.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi darsdagi qolip ustiga qurilgan?</p>",
        "choices": ["아/어 있다 (holat) — PK-42",
                    "고 있다 (davom) — PK-42",
                    "아/어 주다 — PK-31",
                    "아/어 보다 — PK-41"],
        "correct": "아/어 있다 (holat) — PK-42",
        "explanation": "<p>달리다 → 달려 <b>있다</b>: osildi va "
                       "<em>osilgancha turibdi</em>. Shuning uchun asosiy "
                       "shakl 달려 있다.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>결정은 이제 ___ 달렸어.</b> (너)</p>",
        "choices": ["너에", "너를", "너한테", "너로"],
        "correct": "너한테",
        "explanation": "<p>Jonli otga <b>에게/한테</b> qoʻyiladi (PK-16 "
                       "dagi jonli/jonsiz qoidasi). Doʻstga aytilgan "
                       "ogʻzaki gap → <b>한테</b>. Yozma boʻlsa "
                       "너<b>에게</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이 문제는 부모님 ___ 달려 있다.</b></p>",
        "choices": ["께", "에", "을", "이"],
        "correct": "께",
        "explanation": "<p>부모님 — hurmatli odam. Jonli ot + hurmat → "
                       "<b>께</b>. Jonsiz otga 에, oddiy odamga 에게/한테, "
                       "hurmatli odamga 께.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>모든 것은 ___ 달려 있다.</b> (마음먹다)</p>",
        "choices": ["마음먹어서", "마음먹기에", "마음먹는에", "마음먹으로"],
        "correct": "마음먹기에",
        "explanation": "<p>Butun ishni ulash uchun PK-46 dagi <b>기</b> "
                       "otlashtirishi ishlatiladi, keyin <b>에</b>. "
                       "<b>모든 것은 마음먹기에 달려 있다</b> — Koreyada "
                       "maqol darajasidagi jumla.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>합격은 얼마나 ___ 달려 있다.</b> (준비하다 + 느냐)</p>",
        "choices": ["준비하기에", "준비해서", "준비하느냐에", "준비하는에"],
        "correct": "준비하느냐에",
        "explanation": "<p>Soʻroq shaklidagi gapni ulash uchun PK-60 dagi "
                       "<b>느냐</b> + <b>에</b>. “Qancha tayyorlanishingga "
                       "bogʻliq”. Bu shakl TOPIK yozma matnlarida juda "
                       "koʻp uchraydi.</p>",
    },
    {
        "text": "<p>Bu gapning maʼnosi nima?</p>"
                "<p><b>이번 경기의 승패는 마지막 십 분에 달려 있다.</b></p>",
        "choices": ["Oʻyin soʻnggi oʻn daqiqada tugadi",
                    "Oʻyinning yutuq-yutqizigʻi soʻnggi oʻn daqiqaga "
                    "bogʻliq",
                    "Oʻyin oʻn daqiqa davom etadi",
                    "Soʻnggi oʻn daqiqa qiyin boʻldi"],
        "correct": "Oʻyinning yutuq-yutqizigʻi soʻnggi oʻn daqiqaga "
                   "bogʻliq",
        "explanation": "<p><b>승패</b> = yutuq va yutqiziq. Qolip natija "
                       "<em>hali maʼlum emasligini</em> bildiradi — u "
                       "soʻnggi oʻn daqiqada hal boʻladi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri yozilgan?</p>",
        "choices": ["미래는 오늘에 달려 있다.",
                    "미래는 오늘을 달려 있다.",
                    "미래는 오늘이 달려 있다.",
                    "미래는 오늘로 달려 있다."],
        "correct": "미래는 오늘에 달려 있다.",
        "explanation": "<p>Jonsiz ot → <b>에</b>. 달리다 toʻldiruvchi "
                       "olmaydi, shuning uchun 을/를 ham, ega qoʻshimchasi "
                       "이/가 ham bu oʻrinda ishlamaydi.</p>",
    },
    {
        "text": "<p>Bu qolip odatda qanday soʻzlar bilan yuradi?</p>",
        "choices": ["어제, 아까, 지난주",
                    "성공, 결과, 미래, 합격, 승패",
                    "밥, 물, 책, 의자",
                    "빨리, 천천히, 아주"],
        "correct": "성공, 결과, 미래, 합격, 승패",
        "explanation": "<p>Chunki qolip <em>hali hal boʻlmagan</em> narsa "
                       "haqida. Shuning uchun uning egasi deyarli doim "
                       "natija bildiruvchi soʻz boʻladi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>"
                "<p><b>가:</b> 어제 경기가 왜 취소됐어요?</p>",
        "choices": ["비가 왔기 때문에 취소됐어요.",
                    "경기는 비에 달려 있었어요, 그래서 취소됐어요.",
                    "비가 오면 취소돼요, 그래서 취소됐어요.",
                    "비에 달렸어요."],
        "correct": "비가 왔기 때문에 취소됐어요.",
        "explanation": "<p>Ish tugagan va sabab maʼlum → <b>기 때문에</b> "
                       "(PK-49). <b>에 달려 있다</b> faqat hali hal "
                       "boʻlmagan narsa uchun ishlaydi.</p>",
    },
    {
        "text": "<p>Ikki gapning farqi nimada?</p>"
                "<p><b>(a) 노력하면 성공한다.</b><br>"
                "<b>(b) 성공은 노력에 달려 있다.</b></p>",
        "choices": ["(a) shart-natija farazi, (b) esa nima hal qilishini "
                    "nomlaydi",
                    "(a) oʻtgan zamon, (b) hozirgi zamon",
                    "(a) rasmiy, (b) norasmiy",
                    "Farqi yoʻq, ikkalasi bir xil"],
        "correct": "(a) shart-natija farazi, (b) esa nima hal qilishini "
                   "nomlaydi",
        "explanation": "<p><b>(으)면</b> (PK-36) — “agar shunday qilsam, "
                       "shunday boʻladi”. <b>에 달려 있다</b> — “hal "
                       "qiluvchi omil shu”. Ikkinchisi omilni <em>ot "
                       "sifatida</em> oldinga chiqaradi.</p>",
    },
    {
        "text": "<p>Qaysi gapda 달리다 “<b>yugurmoq</b>” maʼnosida?</p>",
        "choices": ["성공은 노력에 달려 있다.",
                    "결정은 너한테 달렸어.",
                    "말이 아주 빨리 달린다.",
                    "미래는 오늘에 달려 있다."],
        "correct": "말이 아주 빨리 달린다.",
        "explanation": "<p>달리다 ning ikkita maʼnosi bor. Ajratuvchi "
                       "belgi — <b>에</b> qoʻshimchasi va <b>있다</b>. "
                       "Ikkalasi koʻrinsa, bu doim “bogʻliq”.</p>",
    },
    {
        "text": "<p>Qaysi qatorda qoʻshimchalar toʻgʻri juftlangan?</p>",
        "choices": ["narsa → 에게 · odam → 에",
                    "narsa → 에 · odam → 에게/한테 · hurmat → 께",
                    "hammasi → 에",
                    "hammasi → 을/를"],
        "correct": "narsa → 에 · odam → 에게/한테 · hurmat → 께",
        "explanation": "<p>Bu — PK-16 dagi jonli/jonsiz qoidasining shu "
                       "qolipdagi koʻrinishi. 노력<b>에</b> · 너<b>한테</b> "
                       "· 부모님<b>께</b>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["성공은 노력에 달려 있다.",
                    "성공은 노력을 달려 있다.",
                    "결정은 너한테 달렸어.",
                    "모든 것은 마음먹기에 달려 있다."],
        "correct": "성공은 노력을 달려 있다.",
        "explanation": "<p>달리다 — <b>oʻtimsiz</b> feʼl, toʻldiruvchi "
                       "olmaydi. Toʻgʻrisi: 노력<b>에</b> 달려 있다.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["그건 이제 너에 달렸어.",
                    "그건 이제 너를 달렸어.",
                    "그건 이제 너한테 달렸어.",
                    "그건 이제 너가 달렸어."],
        "correct": "그건 이제 너한테 달렸어.",
        "explanation": "<p>너 — odam. Jonli otga <b>한테</b> (ogʻzaki) "
                       "yoki <b>에게</b> (yozma). 에 faqat jonsiz "
                       "otlarga.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylang (한다체).</p>"
                "<p><b>달려 있다 / 마지막 십 분에 / 이 경기의 결과는</b></p>",
        "choices": ["달려 있다 이 경기의 결과는 마지막 십 분에.",
                    "이 경기의 결과는 마지막 십 분에 달려 있다.",
                    "마지막 십 분에 달려 있다 이 경기의 결과는.",
                    "이 경기의 결과는 달려 있다 마지막 십 분에."],
        "correct": "이 경기의 결과는 마지막 십 분에 달려 있다.",
        "explanation": "<p>Koreys tili SOV: ega (결과는) → hol (십 분에) → "
                       "kesim (달려 있다). Kesim doim oxirida — bu "
                       "oʻzbekcha bilan bir xil tartib.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> 이번에 합격할 수 있어요?</p>"
                "<p><b>나:</b> ___</p>",
        "choices": ["글쎄요. 이제 심사위원에게 달려 있어요.",
                    "글쎄요. 이제 심사위원을 달려 있어요.",
                    "글쎄요. 이제 심사위원에 달렸기 때문이에요.",
                    "글쎄요. 심사위원이 달려 있어요."],
        "correct": "글쎄요. 이제 심사위원에게 달려 있어요.",
        "explanation": "<p>Natija hali hal boʻlmagan, va uni hal "
                       "qiladigan — <b>odamlar</b>. Demak "
                       "심사위원<b>에게</b> 달려 있어요.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-90 — (으)려던 참이다
# ══════════════════════════════════════════════════════════════════════
Q_PK90 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)려던 참이다</b> qanday maʼno beradi?</p>",
        "choices": ["…ay deb turgan edim (aynan shu payt)",
                    "…ga bogʻliq",
                    "…ishi mumkin emas",
                    "…dan farqi yoʻq"],
        "correct": "…ay deb turgan edim (aynan shu payt)",
        "explanation": "<p>Qolipda ikki narsa bor: <b>niyat</b> va "
                       "<b>aynan shu soniya</b>. Shuning uchun u deyarli "
                       "doim javob sifatida keladi.</p>",
    },
    {
        "text": "<p><b>참</b> soʻzi nimani anglatadi?</p>",
        "choices": ["niyat", "ayni payt, ayni dam", "farq", "hisob"],
        "correct": "ayni payt, ayni dam",
        "explanation": "<p>참 — ot. <b>나가려던 참이다</b> = “chiqmoqchi "
                       "boʻlib turgan <em>payt</em>”. Aynan shuning uchun "
                       "qolip faqat hozirgi soniya haqida.</p>",
    },
    {
        "text": "<p><b>던</b> aniqlovchisi qanday maʼno beradi?</p>",
        "choices": ["kelasi zamondagi ish",
                    "hozir davom etayotgan ish",
                    "oʻtmishda boshlangan, tugamagan ish",
                    "boshqa odamning ishi"],
        "correct": "oʻtmishda boshlangan, tugamagan ish",
        "explanation": "<p>읽<b>은</b> 책 = oʻqib boʻlgan kitob. "
                       "읽<b>던</b> 책 = ochib qoʻygan, tugatmagan kitob. "
                       "Qolipda aynan 던 turadi, chunki niyat boshlangan-"
                       "u, bajarilmagan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>안 그래도 ___ 참이었어요.</b> (전화하다)</p>",
        "choices": ["전화하려던", "전화하는", "전화한", "전화할"],
        "correct": "전화하려던",
        "explanation": "<p>하 da 받침 yoʻq → <b>려던</b>. 참 dan oldin "
                       "faqat <b>(으)려던</b> turadi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>지금 막 ___ 참이에요.</b> (먹다)</p>",
        "choices": ["먹려던", "먹으려던", "먹는", "먹었던"],
        "correct": "먹으려던",
        "explanation": "<p>먹 da 받침 bor → <b>으려던</b>. 받침 yoʻq "
                       "boʻlsa 려던 (가려던, 자려던).</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p><b>안 그래도</b> nimani anglatadi?</p>",
        "choices": ["shunga qaramay",
                    "aytmasangiz ham, oʻzi ham",
                    "aslida yoʻq",
                    "shu sababdan"],
        "correct": "aytmasangiz ham, oʻzi ham",
        "explanation": "<p><b>안 그래도 전화하려던 참이었어요</b> — "
                       "“Aytmasangiz ham, sizga qoʻngʻiroq qilmoqchi "
                       "edim”. Bu jumlani butunligicha yodlab qoʻying — "
                       "koreys nutqida u tayyor blok kabi ishlaydi.</p>",
    },
    {
        "text": "<p><b>마침</b> soʻzining maʼnosi nima?</p>",
        "choices": ["nihoyat", "aynan shu payt, tasodifan",
                    "afsuski", "har doim"],
        "correct": "aynan shu payt, tasodifan",
        "explanation": "<p>마침 bu qolipning eng tez-tez uchraydigan "
                       "hamrohi: <b>마침 나가려던 참이었어요</b> — “aynan "
                       "chiqay deb turgan edim”.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> 지금 나갈 수 있어요?</p>"
                "<p><b>나:</b> 네, ___</p>",
        "choices": ["마침 나가려던 참이었어요.",
                    "마침 나가는 참이었어요.",
                    "마침 나갈 지경이었어요.",
                    "마침 나가기에 달려 있어요."],
        "correct": "마침 나가려던 참이었어요.",
        "explanation": "<p>Suhbatdosh soʻragan ish aynan siz qilmoqchi "
                       "boʻlgan ish bilan toʻqnashdi — bu qolipning asl "
                       "vazifasi. 참 dan oldin doim <b>(으)려던</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>집을 ___ 참에 비가 오기 시작했다.</b> (나가다)</p>",
        "choices": ["나가는", "나간", "나가려던", "나갈"],
        "correct": "나가려던",
        "explanation": "<p><b>(으)려던 참에</b> — “aynan shunday qilmoqchi "
                       "boʻlgan paytda” + boshqa hodisa. Shakl oʻzgarmaydi, "
                       "faqat 이다 oʻrniga 에 keladi.</p>",
    },
    {
        "text": "<p>Bu ikki ibora nimasi bilan farq qiladi?</p>"
                "<p><b>읽은 책</b> · <b>읽던 책</b></p>",
        "choices": ["Birinchisi — oʻqib boʻlgan kitob, ikkinchisi — "
                    "tugatmagan kitob",
                    "Birinchisi — kelasi zamon, ikkinchisi — oʻtgan",
                    "Birinchisi — rasmiy, ikkinchisi — norasmiy",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — oʻqib boʻlgan kitob, ikkinchisi — "
                   "tugatmagan kitob",
        "explanation": "<p><b>(으)ㄴ</b> — tugagan ish (PK-44). "
                       "<b>던</b> — oʻtmishda boshlangan, tugamagan yoki "
                       "takrorlanib turgan ish.</p>",
    },
    {
        "text": "<p>Nutqda qaysi shakl koʻproq uchraydi?</p>",
        "choices": ["…려던 참이다", "…려던 참이었다",
                    "…려던 참이겠다", "…려던 참이니"],
        "correct": "…려던 참이었다",
        "explanation": "<p><b>참이었어요</b> tasodifni kuchliroq "
                       "urgʻulaydi: “aynan shu payt edi”. 참이에요 ham "
                       "toʻgʻri, lekin nutqda kamroq.</p>",
    },
    {
        "text": "<p>Uchinchi shaxs haqida qanday aytiladi?</p>",
        "choices": ["민수는 나가려던 참이에요.",
                    "민수는 나가려던 참이었다고 했어요.",
                    "민수는 나가려던 참이야.",
                    "민수는 나가려던 참입니까?"],
        "correct": "민수는 나가려던 참이었다고 했어요.",
        "explanation": "<p>Niyat — koʻngildagi narsa, boshqa odamning "
                       "koʻnglini koʻra olmaymiz. Shuning uchun uchinchi "
                       "shaxsga PK-60 dagi koʻchirma gap kerak.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>내년에 유학을 ___.</b></p>",
        "choices": ["가려던 참이에요", "가려고 해요",
                    "갈 지경이에요", "가는 참이에요"],
        "correct": "가려고 해요",
        "explanation": "<p>참 = <b>ayni soniya</b>. “Kelasi yil” bilan bir "
                       "jumlada tura olmaydi. Uzoq reja uchun "
                       "<b>(으)려고 하다</b> (PK-40).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>아침부터 아무것도 못 먹어서 ___.</b></p>",
        "choices": ["먹으려던 참이에요", "쓰러질 지경이에요",
                    "먹기에 달려 있어요", "먹은 셈이에요"],
        "correct": "쓰러질 지경이에요",
        "explanation": "<p>Bu — <b>holat</b> chegarasi, men xohlagan narsa "
                       "emas → <b>(으)ㄹ 지경이다</b> (PK-87). 참 esa "
                       "<b>niyat</b> chegarasi.</p>",
    },
    {
        "text": "<p>Ikki qolipning asosiy farqi nimada?</p>"
                "<p><b>(으)ㄹ 지경이다</b> · <b>(으)려던 참이다</b></p>",
        "choices": ["Biri rasmiy, ikkinchisi norasmiy",
                    "Biri HOLAT chegarasi (xohlamaganim), ikkinchisi "
                    "NIYAT chegarasi (xohlaganim)",
                    "Biri oʻtgan, ikkinchisi kelasi zamon",
                    "Biri feʼl, ikkinchisi sifat bilan"],
        "correct": "Biri HOLAT chegarasi (xohlamaganim), ikkinchisi "
                   "NIYAT chegarasi (xohlaganim)",
        "explanation": "<p>Oʻzbekchada ikkalasi ham “…ay deb turibman” "
                       "deb tarjima qilinadi, shuning uchun ular "
                       "adashtiriladi. Koreys tili farqni <b>qolipning "
                       "oʻzida</b> koʻrsatadi: 지경 = holat, 참 = "
                       "niyat.</p>",
    },
    {
        "text": "<p>Qaysi gap notoʻgʻri?</p>",
        "choices": ["지금 자려던 참이었어요.",
                    "비가 오려던 참이었어요.",
                    "밥을 먹으려던 참이었어요.",
                    "씻으려던 참이었어요."],
        "correct": "비가 오려던 참이었어요.",
        "explanation": "<p>Qolip faqat <b>irodali</b> harakat bilan "
                       "ishlaydi. Yomgʻirning niyati yoʻq. Toʻgʻrisi: "
                       "비가 <b>오려고 했다</b> yoki 비가 <b>올 것 "
                       "같았다</b>.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["안 그래도 연락하려던 참이었어요.",
                    "지금 막 씻으려던 참이에요.",
                    "나가는 참이었어요.",
                    "집을 나가려던 참에 전화가 왔다."],
        "correct": "나가는 참이었어요.",
        "explanation": "<p>참 dan oldin <b>(으)려던</b> turishi shart. "
                       "Toʻgʻrisi: <b>나가려던 참이었어요</b>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["내년에 한국에 가려던 참이에요.",
                    "감기에 걸리려던 참이었어요.",
                    "안 그래도 물어보려던 참이었어요.",
                    "민수는 나가려던 참이에요."],
        "correct": "안 그래도 물어보려던 참이었어요.",
        "explanation": "<p>Uchta shart bajarilgan: birinchi shaxs, "
                       "irodali harakat, ayni payt. Qolganlari mos "
                       "ravishda uzoq reja, irodasiz hodisa va uchinchi "
                       "shaxs sababli xato.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang.</p>"
                "<p><b>“Aynan sizga qoʻngʻiroq qilay deb turgan edim.”</b></p>",
        "choices": ["안 그래도 전화하려던 참이었어요.",
                    "안 그래도 전화할 지경이었어요.",
                    "안 그래도 전화하기에 달려 있었어요.",
                    "안 그래도 전화한 셈이었어요."],
        "correct": "안 그래도 전화하려던 참이었어요.",
        "explanation": "<p>Niyat + tasodif → <b>(으)려던 참이다</b>, va "
                       "eng tabiiy boshlanish <b>안 그래도</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> 밥 먹었어요?</p>"
                "<p><b>나:</b> 아니요, ___</p>",
        "choices": ["지금 먹으려던 참이었어요.",
                    "지금 먹을 지경이었어요.",
                    "지금 먹는 셈이에요.",
                    "지금 먹기에 달렸어요."],
        "correct": "지금 먹으려던 참이었어요.",
        "explanation": "<p>Savol aynan siz qilmoqchi boʻlgan ish haqida — "
                       "bu qolipning eng tipik oʻrni. 먹 da 받침 bor, "
                       "demak <b>먹으려던</b>.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-91 — (이)나 다름없다 · (으)ㄴ/는 셈이다
# ══════════════════════════════════════════════════════════════════════
Q_PK91 = [
    # 1–5 tanish
    {
        "text": "<p><b>(이)나 다름없다</b> qanday maʼno beradi?</p>",
        "choices": ["…dan farqi yoʻq, … bilan barobar",
                    "… hisob",
                    "…ga bogʻliq",
                    "…ay deb turibman"],
        "correct": "…dan farqi yoʻq, … bilan barobar",
        "explanation": "<p><b>삼촌은 아버지나 다름없다</b> — amakim otamdan "
                       "farqi yoʻq. Qolip ikki narsani yonma-yon "
                       "qoʻyadi.</p>",
    },
    {
        "text": "<p><b>셈</b> soʻzi qaysi feʼldan yasalgan va nimani "
                "anglatadi?</p>",
        "choices": ["세우다 — qurmoq",
                    "세다 — sanamoq · demak “hisob”",
                    "쓰다 — ishlatmoq",
                    "서다 — turmoq"],
        "correct": "세다 — sanamoq · demak “hisob”",
        "explanation": "<p>세다 + <b>(으)ㅁ</b> → <b>셈</b> = hisob. "
                       "Shuning uchun 셈이다 = “hisob shunday”, yaʼni "
                       "sanab chiqarilgan xulosa.</p>",
    },
    {
        "text": "<p><b>다름</b> qaysi soʻzdan yasalgan?</p>",
        "choices": ["다르다 — farq qilmoq",
                    "달리다 — osilib turmoq",
                    "다니다 — qatnamoq",
                    "닫다 — yopmoq"],
        "correct": "다르다 — farq qilmoq",
        "explanation": "<p>다르다 + <b>(으)ㅁ</b> → <b>다름</b> = farq. "
                       "다름<b>없다</b> = “farq yoʻq”. Bu ham, 셈 ham "
                       "PK-46 dagi otlashtirishdan tugʻilgan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>삼촌은 저에게 ___ 다름없어요.</b> (아버지)</p>",
        "choices": ["아버지가", "아버지를", "아버지나", "아버지에"],
        "correct": "아버지나",
        "explanation": "<p>아버지 da 받침 yoʻq → <b>나</b>. 받침 bor "
                       "boʻlsa <b>이나</b> (새것이나, 가족이나).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이 옷은 두 번밖에 안 입어서 ___ 다름없다.</b> (새것)</p>",
        "choices": ["새것이나", "새것나", "새것에", "새것인"],
        "correct": "새것이나",
        "explanation": "<p>새것 da 받침 (ㅅ) bor → <b>이나</b>. Bu — PK-12 "
                       "dan beri tanish boʻlgan 받침 tarmogʻining yana "
                       "bir koʻrinishi.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>매일 두 시간씩 운동하니까 일주일에 열네 시간 ___.</b> "
                "(운동하다 + 셈이다)</p>",
        "choices": ["운동한 셈이다", "운동하는 셈이다",
                    "운동할 셈이다", "운동하기 셈이다"],
        "correct": "운동하는 셈이다",
        "explanation": "<p>매일 — takrorlanadigan, hozirgi ish → "
                       "<b>는 셈이다</b>. Tugagan ish uchun (으)ㄴ "
                       "셈이다.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>시험은 다음 주지만 공부는 다 ___.</b> (하다 + 셈이다)</p>",
        "choices": ["하는 셈이다", "할 셈이다", "한 셈이다", "하기 셈이다"],
        "correct": "한 셈이다",
        "explanation": "<p>Tayyorgarlik tugagan → <b>(으)ㄴ 셈이다</b>. "
                       "“Koʻrib boʻlgan hisob” — rasman tugamagan, lekin "
                       "amalda tugagan.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>십 년을 같이 살았으니까 거의 ___.</b> (가족 + 셈이다)</p>",
        "choices": ["가족나 셈이다", "가족인 셈이다",
                    "가족는 셈이다", "가족을 셈이다"],
        "correct": "가족인 셈이다",
        "explanation": "<p>셈이다 dan oldin <b>ot</b> kelsa, ulagich "
                       "<b>인</b> boʻladi: 가족<b>인</b> 셈이다. Diqqat — "
                       "다름없다 esa <b>(이)나</b> ni oladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>이 정도면 다 ___ 다름없다.</b> (끝나다)</p>",
        "choices": ["끝난", "끝난 것이나", "끝나는", "끝나기"],
        "correct": "끝난 것이나",
        "explanation": "<p>다름없다 dan oldin <b>ot</b> turishi kerak. "
                       "Feʼlni avval <b>(으)ㄴ/는 것</b> bilan otga "
                       "aylantiring: 끝나다 → 끝난 것 → 끝난 <b>것이나</b> "
                       "다름없다.</p>",
    },
    {
        "text": "<p>Bu gapning maʼnosi nima?</p>"
                "<p><b>하루에 두 시간씩 십 년이면 칠천 시간을 쓴 셈이다.</b></p>",
        "choices": ["Yetti ming soat sarflash kerak",
                    "Kuniga ikki soatdan oʻn yil boʻlsa — yetti ming soat "
                    "sarflagan hisob",
                    "Yetti ming soat juda koʻp",
                    "Oʻn yilda yetti ming soat sarflamoqchiman"],
        "correct": "Kuniga ikki soatdan oʻn yil boʻlsa — yetti ming soat "
                   "sarflagan hisob",
        "explanation": "<p>Bu — 셈이다 ning eng tabiiy ishi: raqamlarni "
                       "qoʻshib, <b>xulosa chiqarish</b>. TOPIK 쓰기 da "
                       "juda foydali qolip.</p>",
    },
    {
        "text": "<p><b>셈이다</b> ning ikkinchi (hisob-kitobdan tashqari) "
                "ishi nima?</p>",
        "choices": ["Buyruq berish",
                    "Baho berish — “nazarga olsak, shunday deyish mumkin”",
                    "Savol soʻrash",
                    "Taqiqlash"],
        "correct": "Baho berish — “nazarga olsak, shunday deyish mumkin”",
        "explanation": "<p><b>이 정도면 잘한 셈이다</b> — “shu darajada "
                       "boʻlsa, yaxshi qilgan hisob”. Bu maʼnoda u "
                       "koʻpincha <b>이 정도면</b> bilan boshlanadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri yozilgan?</p>",
        "choices": ["그 가게는 우리에게 집이나 다름없었다.",
                    "그 가게는 우리에게 집 다름없었다.",
                    "그 가게는 우리에게 집인 다름없었다.",
                    "그 가게는 우리에게 집을 다름없었다."],
        "correct": "그 가게는 우리에게 집이나 다름없었다.",
        "explanation": "<p>집 da 받침 bor → <b>이나</b>. <b>(이)나</b> "
                       "tushib qolmaydi — u qolipning ajralmas qismi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Qaysi qolip kerak?</p>"
                "<p><b>“Amakim men uchun ota bilan barobar edi.”</b></p>",
        "choices": ["삼촌은 아버지인 셈이었다.",
                    "삼촌은 아버지나 다름없었다.",
                    "삼촌은 아버지에 달려 있었다.",
                    "삼촌은 아버지려던 참이었다."],
        "correct": "삼촌은 아버지나 다름없었다.",
        "explanation": "<p>Oʻzbekchada “<b>bilan barobar / farqi yoʻq</b>” "
                       "chiqsa → <b>(이)나 다름없다</b>. Bu — baho, "
                       "his-tuygʻu.</p>",
    },
    {
        "text": "<p>Qaysi qolip kerak?</p>"
                "<p><b>“Yigirma uch yil — sakkiz ming kundan oshgan "
                "hisob.”</b></p>",
        "choices": ["이십삼 년은 팔천 일이 넘는 셈이다.",
                    "이십삼 년은 팔천 일이나 다름없다.",
                    "이십삼 년은 팔천 일에 달려 있다.",
                    "이십삼 년은 팔천 일이 넘으려던 참이다."],
        "correct": "이십삼 년은 팔천 일이 넘는 셈이다.",
        "explanation": "<p>Oʻzbekchada “<b>hisob</b>” chiqsa → "
                       "<b>셈이다</b>. Bu — hisob-kitob, mantiq.</p>",
    },
    {
        "text": "<p>Ikki qolipning oldida nima turadi?</p>",
        "choices": ["Ikkalasining ham oldida ot",
                    "다름없다 — ot · 셈이다 — aniqlovchi shakldagi butun gap",
                    "다름없다 — feʼl · 셈이다 — ot",
                    "Ikkalasining ham oldida feʼl"],
        "correct": "다름없다 — ot · 셈이다 — aniqlovchi shakldagi butun gap",
        "explanation": "<p>Shuning uchun feʼlni 다름없다 bilan ishlatish "
                       "uchun avval <b>(으)ㄴ/는 것</b> qoʻshib, otga "
                       "aylantirish kerak.</p>",
    },
    {
        "text": "<p>Qaysi juftlik toʻgʻri?</p>",
        "choices": ["ot + 인 다름없다 · gap + 나 셈이다",
                    "ot + (이)나 다름없다 · ot + 인 셈이다",
                    "ot + 을/를 다름없다 · gap + 기 셈이다",
                    "ot + 에 다름없다 · gap + 는 것 셈이다"],
        "correct": "ot + (이)나 다름없다 · ot + 인 셈이다",
        "explanation": "<p>Ikkala qolipning ulagichini almashtirib "
                       "yubormang: 친구<b>나</b> 다름없다 · 친구<b>인</b> "
                       "셈이다.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["삼촌은 아버지 다름없어요.",
                    "이 옷은 새것이나 다름없다.",
                    "거의 다 끝난 것이나 다름없다.",
                    "그 가게는 집이나 다름없었다."],
        "correct": "삼촌은 아버지 다름없어요.",
        "explanation": "<p><b>(이)나</b> tushib qolgan. Toʻgʻrisi: "
                       "아버지<b>나</b> 다름없어요.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["매일 열 시간 일한 셈이다.",
                    "매일 열 시간 일하는 셈이다.",
                    "매일 열 시간 일할 셈이다.",
                    "매일 열 시간 일하기 셈이다."],
        "correct": "매일 열 시간 일하는 셈이다.",
        "explanation": "<p>매일 — takrorlanadigan ish, demak hozirgi "
                       "zamon aniqlovchisi <b>는</b>. 일한 셈이다 tugagan "
                       "ish uchun.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylang (한다체).</p>"
                "<p><b>다름없다 / 우리에게 / 그 가게는 / 집이나</b></p>",
        "choices": ["그 가게는 우리에게 집이나 다름없다.",
                    "우리에게 그 가게는 다름없다 집이나.",
                    "집이나 다름없다 그 가게는 우리에게.",
                    "그 가게는 다름없다 우리에게 집이나."],
        "correct": "그 가게는 우리에게 집이나 다름없다.",
        "explanation": "<p>Koreys tili SOV: ega (가게는) → toʻldiruvchi "
                       "guruh (우리에게 집이나) → kesim (다름없다). Kesim "
                       "doim oxirida.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> 숙제 다 했어요?</p>"
                "<p><b>나:</b> 마지막 한 문제만 남았어요. ___</p>",
        "choices": ["다 한 셈이에요.",
                    "다 하는 셈이에요.",
                    "다 하기에 달렸어요.",
                    "다 하려던 참이에요."],
        "correct": "다 한 셈이에요.",
        "explanation": "<p>Rasman tugamagan, amalda tugagan — aynan "
                       "셈이다 ning ishi. Ish tugagani uchun <b>(으)ㄴ "
                       "셈이다</b>.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-89 Mashq: 명사 + 에 달려 있다",
        "description": "20 savol — 달리다 ning ikki maʼnosi, 에 · 에게 · 께 "
                       "tanlovi, 기에 va 느냐에 shakllari hamda "
                       "기 때문에 va (으)면 dan farqi.",
        "tutorial":    "PK-89:",
        "level":       "medium",
        "questions":   Q_PK89,
    },
    {
        "title":       "PK-90 Mashq: (으)려던 참이다",
        "description": "20 savol — 던 aniqlovchisi, 참 ning maʼnosi, "
                       "안 그래도 bloki, irodali feʼl sharti va "
                       "(으)ㄹ 지경이다 bilan farqi.",
        "tutorial":    "PK-90:",
        "level":       "medium",
        "questions":   Q_PK90,
    },
    {
        "title":       "PK-91 Mashq: (이)나 다름없다 · (으)ㄴ/는 셈이다",
        "description": "20 savol — 다름 va 셈 ning kelib chiqishi, "
                       "(이)나 va 인 ulagichlari, aniqlovchi shakl tanlovi "
                       "va ikkala qolipni ajratish.",
        "tutorial":    "PK-91:",
        "level":       "medium",
        "questions":   Q_PK91,
    },
]
