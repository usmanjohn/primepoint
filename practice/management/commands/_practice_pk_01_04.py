# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-1 … PK-4 (Hangul bloki).

12 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_01_04.py --master=prime \\
        --expect-questions=12
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
# PK-1 — Hangul bilan tanishuv
# =====================================================================

Q_PK1 = [
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Hangulda nechta asosiy harf bor?</strong></p>",
        "choices": ["14 ta", "24 ta", "40 ta", "1000 dan ortiq"],
        "correct": "24 ta",
        "explanation": "<p><strong>24 ta</strong> toʻgʻri: 14 ta undosh (자음) va 10 ta unli "
                       "(모음). Qattiq undoshlar va qoʻshma unlilar shulardan yasalgani uchun "
                       "alohida harf sanalmaydi — hammasi boʻlib 40 ta belgi chiqadi, lekin "
                       "yodlash kerak boʻlgani 24 ta.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Hangulni kim yaratgan?</strong></p>",
        "choices": ["세종대왕 va uning olimlari", "Xitoy imperatori",
                    "Hech kim — u asta-sekin shakllangan", "Yapon rohiblari"],
        "correct": "세종대왕 va uning olimlari",
        "explanation": "<p><strong>세종대왕</strong> (Buyuk qirol Sejong) 1443-yilda Hangulni "
                       "maxsus ixtiro qilgan. Shu bilan Hangul dunyodagi kam sonli "
                       "<em>oʻylab topilgan</em> alifbolardan biri — qolganlari asrlar davomida "
                       "oʻz-oʻzidan shakllangan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>한글 va 한자 orasidagi asosiy farq nima?</strong></p>",
        "choices": ["한글 tovushni, 한자 maʼnoni bildiradi",
                    "한글 maʼnoni, 한자 tovushni bildiradi",
                    "Ikkalasi ham bir xil, faqat nomi boshqa",
                    "한글 faqat ismlarda ishlatiladi"],
        "correct": "한글 tovushni, 한자 maʼnoni bildiradi",
        "explanation": "<p><strong>한글 tovushni bildiradi</strong> — shuning uchun notanish "
                       "soʻzni ham oʻqib boʻladi. 한자 (xitoy iyeroglifi) esa butun maʼnoni "
                       "beradi va uni oldindan bilish shart. Bugungi koreys matnlari deyarli "
                       "butunlay 한글da.</p>",
    },
    {
        "text": "<p><strong>한</strong> boʻgʻini nechta harfdan tuzilgan?</p>",
        "choices": ["Bitta", "Ikkita", "Uchta", "Toʻrtta"],
        "correct": "Uchta",
        "explanation": "<p><strong>Uchta</strong>: ㅎ + ㅏ + ㄴ. Hangulda harflar qatorga emas, "
                       "kvadratchaga — boʻgʻin blokiga yigʻiladi, shuning uchun uchta tovush "
                       "bitta belgi boʻlib koʻrinadi.</p>",
    },
    {
        "text": "<p>Bu boʻgʻin qaysi harflardan tuzilgan?</p>"
                "<p><strong>물</strong></p>",
        "choices": ["ㅁ + ㅜ + ㄹ", "ㅁ + ㅗ + ㄹ", "ㅂ + ㅜ + ㄹ", "ㅁ + ㅜ + ㄴ"],
        "correct": "ㅁ + ㅜ + ㄹ",
        "explanation": "<p><strong>ㅁ + ㅜ + ㄹ</strong>. ㅜ yotiq unli boʻlgani uchun ㅁ ning "
                       "tagiga tushdi, ㄹ esa 받침 sifatida eng pastda turibdi. Maʼnosi — "
                       "“suv”.</p>",
    },
    {
        "text": "<p>Bu harflardan qaysi boʻgʻin hosil boʻladi?</p>"
                "<p><strong>ㄱ + ㅗ</strong></p>",
        "choices": ["가", "고", "구", "그"],
        "correct": "고",
        "explanation": "<p><strong>고</strong> toʻgʻri. ㅗ — yotiq unli, shuning uchun undoshning "
                       "<em>tagiga</em> yoziladi. Agar ㅏ (tik unli) boʻlganida oʻngga yozilardi "
                       "va 가 chiqardi.</p>",
    },
    {
        "text": "<p>Bu harflardan qaysi boʻgʻin hosil boʻladi?</p>"
                "<p><strong>ㄴ + ㅏ</strong></p>",
        "choices": ["나", "노", "누", "느"],
        "correct": "나",
        "explanation": "<p><strong>나</strong> toʻgʻri — ㅏ tik unli, shuning uchun ㄴ ning "
                       "<em>oʻngiga</em> yoziladi. Maʼnosi — “men”.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Boʻgʻindagi bosh undosh qanday ataladi?</strong></p>",
        "choices": ["초성", "중성", "종성", "받침"],
        "correct": "초성",
        "explanation": "<p><strong>초성</strong> — bosh undosh. 중성 — oʻrtadagi unli, "
                       "종성 (yoki 받침) — pastdagi yakuniy undosh.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㅜ unlisi undoshga nisbatan qayerga yoziladi?</strong></p>",
        "choices": ["Oʻngiga", "Tagiga", "Chapiga", "Tepasiga"],
        "correct": "Tagiga",
        "explanation": "<p><strong>Tagiga</strong>. ㅜ — yotiq unli (uzun chizigʻi gorizontal), "
                       "shuning uchun pastga tushadi: 우, 무, 구. Tik unlilar (ㅏ ㅓ ㅣ) esa "
                       "oʻngga chiqadi.</p>",
    },
    {
        "text": "<p>ㄱ harfiga bitta chiziq qoʻshsak nima boʻladi?</p>",
        "choices": ["ㅋ — tovushga nafas qoʻshiladi", "ㄲ — tovush qattiqlashadi",
                    "ㄴ — boshqa tovush chiqadi", "Hech narsa oʻzgarmaydi"],
        "correct": "ㅋ — tovushga nafas qoʻshiladi",
        "explanation": "<p><strong>ㅋ</strong> hosil boʻladi. Hangulda qoʻshimcha chiziq har doim "
                       "qoʻshimcha <em>nafas</em> degani. Xuddi shu qoida ㄷ→ㅌ, ㅂ→ㅍ, ㅈ→ㅊ "
                       "juftliklarida ham ishlaydi. ㄲ esa chiziq emas, harfning ikki marta "
                       "yozilgani.</p>",
    },
    {
        "text": "<p>Qaysi yozuv toʻgʻri?</p>",
        "choices": ["ㅎㅏㄴㄱㅜㄱ", "한국", "하ㄴ구ㄱ", "한ㄱ욱"],
        "correct": "한국",
        "explanation": "<p><strong>한국</strong> toʻgʻri. Koreyschada harflar bir qatorga "
                       "tizilmaydi — ular boʻgʻin bloklariga yigʻiladi. Qatorga yozilgan "
                       "harflar toʻplami koreys yozuvida soʻz hisoblanmaydi.</p>",
    },
    {
        "text": "<p>Bu boʻgʻin qanday oʻqiladi?</p>"
                "<p><strong>아</strong></p>",
        "choices": ["[a]", "[nga]", "[ang]", "[o]"],
        "correct": "[a]",
        "explanation": "<p><strong>[a]</strong>. Boʻgʻin boshidagi <strong>ㅇ jim</strong> — u "
                       "hech qanday tovush bermaydi, faqat “bu yerda unli turibdi” degan "
                       "belgi. ㅇ “ng” boʻlib faqat 받침 holatida oʻqiladi: 강 = [kang].</p>",
    },
]


# =====================================================================
# PK-2 — Unlilar 1: ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ
# =====================================================================

Q_PK2 = [
    {
        "text": "<p>Bu harf qanday oʻqiladi?</p><p><strong>ㅣ</strong></p>",
        "choices": ["[i]", "[u]", "[a]", "[o]"],
        "correct": "[i]",
        "explanation": "<p><strong>[i]</strong> — oʻzbekcha “ish” soʻzidagi <em>i</em>. ㅣ tik "
                       "unli, shuning uchun undoshning oʻngiga yoziladi: 이, 미, 시.</p>",
    },
    {
        "text": "<p>Bu harf qanday oʻqiladi?</p><p><strong>ㅜ</strong></p>",
        "choices": ["[u]", "[o]", "[eu]", "[a]"],
        "correct": "[u]",
        "explanation": "<p><strong>[u]</strong> — oʻzbekcha “uy” soʻzidagi <em>u</em>, lablar "
                       "dumaloq. Agar lablarni yoysangiz, boshqa harf — ㅡ chiqadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Qaysi uchtasi yotiq unli?</strong></p>",
        "choices": ["ㅗ ㅜ ㅡ", "ㅏ ㅓ ㅣ", "ㅏ ㅗ ㅣ", "ㅓ ㅜ ㅣ"],
        "correct": "ㅗ ㅜ ㅡ",
        "explanation": "<p><strong>ㅗ ㅜ ㅡ</strong> — uzun chizigʻi gorizontal boʻlgan unlilar. "
                       "Ular undoshning tagiga yoziladi. ㅏ ㅓ ㅣ esa tik unlilar va oʻngga "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>오이</strong></p>",
        "choices": ["[oʻ-i]", "[a-i]", "[o-i] — lablar yoyiq", "[u-i]"],
        "correct": "[oʻ-i]",
        "explanation": "<p><strong>[oʻ-i]</strong>. ㅗ — lablar dumaloqlangan tovush, oʻzbekcha "
                       "“koʻz” dagi <em>oʻ</em>. Ikkala blokda ham boshdagi ㅇ jim, shuning "
                       "uchun faqat ikkita unli eshitiladi. Maʼnosi — “bodring”.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>아우</strong></p>",
        "choices": ["[a-u]", "[a-oʻ]", "[o-u]", "[a-i]"],
        "correct": "[a-u]",
        "explanation": "<p><strong>[a-u]</strong> — “uka, singil”. Birinchi blokda ㅇ+ㅏ (unli "
                       "tik, oʻngda), ikkinchisida ㅇ+ㅜ (unli yotiq, tagida).</p>",
    },
    {
        "text": "<p>“a-i” tovushlari Hangulda qanday yoziladi?</p>",
        "choices": ["아이", "이아", "ㅏㅣ", "아으"],
        "correct": "아이",
        "explanation": "<p><strong>아이</strong> — “bola”. Unli yolgʻiz turolmaydi, shuning uchun "
                       "har ikkala blokda ham oldiga jim ㅇ qoʻyiladi. ㅏㅣ deb yozish "
                       "notoʻgʻri — bu boʻgʻin emas.</p>",
    },
    {
        "text": "<p>Boʻsh joyga qaysi harf tushadi?</p>"
                "<p><strong>ㅇ + ___ = 으</strong></p>",
        "choices": ["ㅡ", "ㅜ", "ㅣ", "ㅗ"],
        "correct": "ㅡ",
        "explanation": "<p><strong>ㅡ</strong>. Bu bitta uzun yotiq chiziq — shuning uchun ㅇ ning "
                       "tagiga tushadi va 으 hosil boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㅓ va ㅗ ni nima ajratadi?</strong></p>",
        "choices": ["Lablarning holati", "Tilning balandligi", "Ovoz balandligi",
                    "Hech narsa — ular bir xil"],
        "correct": "Lablarning holati",
        "explanation": "<p><strong>Lablar</strong>. ㅓ da lablar yoyilgan (oʻzbekcha “ona” dagi "
                       "<em>o</em>), ㅗ da esa dumaloqlanib oldinga chiqadi (oʻzbekcha “koʻz” "
                       "dagi <em>oʻ</em>). Qoʻlingizni lablaringizga qoʻyib tekshiring.</p>",
    },
    {
        "text": "<p>Qaysi juftlik <strong>서울</strong> va <strong>소</strong> ni "
                "toʻgʻri tavsiflaydi?</p>",
        "choices": ["서 — lab yoyiq, 소 — lab dumaloq",
                    "서 — lab dumaloq, 소 — lab yoyiq",
                    "Ikkalasi ham dumaloq",
                    "Ikkalasi ham yoyiq"],
        "correct": "서 — lab yoyiq, 소 — lab dumaloq",
        "explanation": "<p><strong>서 — yoyiq, 소 — dumaloq.</strong> 서울 — Koreya poytaxti, "
                       "소 — “sigir”. Bu ikkisini bir xil aytish oʻzbek oʻquvchining eng koʻp "
                       "uchraydigan xatosi.</p>",
    },
    {
        "text": "<p><strong>ㅡ</strong> tovushini qanday chiqarasiz?</p>",
        "choices": ["“u” deyishga tayyorlanib, lablarni yoying",
                    "“i” deyishga tayyorlanib, lablarni dumaloqlang",
                    "“a” ni burun bilan ayting",
                    "“o” ni uzun cho'zing"],
        "correct": "“u” deyishga tayyorlanib, lablarni yoying",
        "explanation": "<p>ㅡ = <strong>ㅜ ning lablari yoyilgan shakli</strong>. Til orqada va "
                       "yuqorida qoladi, lekin lablar dumaloq boʻlmaydi. Oʻzbek tilida bu tovush "
                       "yoʻq, shuning uchun uni alohida mashq qilish kerak.</p>",
    },
    {
        "text": "<p>Jasur <strong>그</strong> ni “gi” deb oʻqidi. Xato qayerda?</p>",
        "choices": ["ㅡ ni ㅣ bilan almashtirdi", "ㄱ ni ㅋ bilan almashtirdi",
                    "받침ni tushirib qoldirdi", "Xato yoʻq, toʻgʻri oʻqigan"],
        "correct": "ㅡ ni ㅣ bilan almashtirdi",
        "explanation": "<p>그 ning unlisi — <strong>ㅡ</strong>, “i” emas. “gi” deb oʻqilsa, bu "
                       "allaqachon boshqa soʻz — <strong>기</strong>. Jasur lablarini yoyib, "
                       "“u” ni dumaloqsiz aytib koʻrishi kerak.</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["아 = [nga]", "이 = [i]", "우 = [u]", "어 = oʻzbekcha “o”"],
        "correct": "아 = [nga]",
        "explanation": "<p><strong>아 = [nga]</strong> notoʻgʻri. Boʻgʻin boshidagi ㅇ jim, "
                       "shuning uchun 아 = <strong>[a]</strong>. ㅇ “ng” boʻlib faqat 받침 "
                       "holatida oʻqiladi.</p>",
    },
]


# =====================================================================
# PK-3 — Unlilar 2: yotlashgan va qoʻshma unlilar
# =====================================================================

Q_PK3 = [
    {
        "text": "<p>Bu harf qanday oʻqiladi?</p><p><strong>ㅑ</strong></p>",
        "choices": ["[ya]", "[yo]", "[yu]", "[ye]"],
        "correct": "[ya]",
        "explanation": "<p><strong>[ya]</strong> — bu ㅏ ga bitta qoʻshimcha chiziqcha qoʻshilgani. "
                       "Unlilarda qoʻshimcha chiziqcha har doim <em>y</em> tovushini "
                       "qoʻshadi.</p>",
    },
    {
        "text": "<p>ㅜ ga bitta chiziqcha qoʻshsak qaysi harf chiqadi?</p>",
        "choices": ["ㅠ", "ㅛ", "ㅑ", "ㅕ"],
        "correct": "ㅠ",
        "explanation": "<p><strong>ㅠ</strong> — “yu”. Chiziqcha faqat <em>y</em> qoʻshadi, "
                       "unlining oʻzini oʻzgartirmaydi: ㅏ→ㅑ, ㅓ→ㅕ, ㅗ→ㅛ, ㅜ→ㅠ.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㅐ va ㅔ bugungi koreys tilida qanday aytiladi?</strong></p>",
        "choices": ["Deyarli bir xil — “e” kabi", "Butunlay boshqacha",
                    "ㅐ = “a”, ㅔ = “i”", "Ikkalasi ham aytilmaydi"],
        "correct": "Deyarli bir xil — “e” kabi",
        "explanation": "<p><strong>Deyarli bir xil.</strong> Eski koreys tilida ular farqlanardi, "
                       "bugun esa deyarli barcha koreys ikkalasini “e” kabi aytadi. Ya'ni "
                       "talaffuzda muammo yoʻq — muammo faqat <em>imloda</em>: 개 (“it”) va "
                       "게 (“qisqichbaqa”) bir xil eshitiladi, lekin har xil yoziladi.</p>",
    },
    {
        "text": "<p>Bu qoʻshma unli qaysi ikkita unlidan yasalgan?</p>"
                "<p><strong>ㅘ</strong></p>",
        "choices": ["ㅗ + ㅏ", "ㅜ + ㅏ", "ㅏ + ㅗ", "ㅡ + ㅏ"],
        "correct": "ㅗ + ㅏ",
        "explanation": "<p><strong>ㅗ + ㅏ</strong>. Qoʻshma unli har doim <em>yotiq unli + tik "
                       "unli</em> tartibida yasaladi. “oʻ” va “a” ni tez ketma-ket aytsangiz, "
                       "oʻz-oʻzidan “wa” chiqadi.</p>",
    },
    {
        "text": "<p>Bu qoʻshma unli qaysi ikkita unlidan yasalgan?</p>"
                "<p><strong>ㅝ</strong></p>",
        "choices": ["ㅜ + ㅓ", "ㅗ + ㅓ", "ㅜ + ㅏ", "ㅡ + ㅓ"],
        "correct": "ㅜ + ㅓ",
        "explanation": "<p><strong>ㅜ + ㅓ</strong> → “wo”. 뭐 (“nima”) soʻzidagi tovush — "
                       "kundalik nutqda eng koʻp ishlatiladiganlaridan.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>여우</strong></p>",
        "choices": ["[yo-u], lablar yoyiq", "[yoʻ-u], lablar dumaloq",
                    "[ya-u]", "[yu-o]"],
        "correct": "[yo-u], lablar yoyiq",
        "explanation": "<p><strong>[yo-u]</strong> — “tulki”. 여 da lablar yoyilgan boʻlishi "
                       "kerak, chunki ㅕ = ㅓ + y. Agar lablar dumaloqlansa, 요 boʻlib "
                       "qoladi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>우유</strong></p>",
        "choices": ["[u-yu]", "[u-yo]", "[yu-u]", "[oʻ-yu]"],
        "correct": "[u-yu]",
        "explanation": "<p><strong>[u-yu]</strong> — “sut”. Birinchi blokda ㅇ+ㅜ, ikkinchisida "
                       "ㅇ+ㅠ. Ikkala unli ham yotiq, shuning uchun ikkalasi ham ㅇ ning tagiga "
                       "yozilgan.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>여</strong> va <strong>요</strong> ni nima ajratadi?</p>",
        "choices": ["Lablarning holati", "Ovoz balandligi", "Uzunligi",
                    "Hech narsa — ular bir xil"],
        "correct": "Lablarning holati",
        "explanation": "<p><strong>Lablar.</strong> 여 = “yo” (lab yoyiq), 요 = “yoʻ” (lab "
                       "dumaloq) — xuddi ㅓ/ㅗ juftligidagidek, faqat “y” bilan. 여기 (“bu yer”) "
                       "ni 요기 deb aytmang.</p>",
    },
    {
        "text": "<p>Nega ㅡ va ㅣ ning chiziqchali (yotlashgan) shakli yoʻq?</p>",
        "choices": ["“y+i” va “y+ы” amalda aytilmaydi",
                    "Ular juda eski harflar",
                    "Ular allaqachon “y” tovushini oʻz ichiga oladi",
                    "Ular faqat 받침da ishlatiladi"],
        "correct": "“y+i” va “y+ы” amalda aytilmaydi",
        "explanation": "<p>“y” tovushi <strong>ㅣ ning oʻziga juda yaqin</strong> — “y+i” amalda "
                       "oddiy “i” boʻlib chiqadi. Shuning uchun yotlashgan unli atigi toʻrtta: "
                       "ㅑ ㅕ ㅛ ㅠ.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>의사</strong></p>",
        "choices": ["[의사] — toʻliq “ui”", "[이사] — oddiy “i”",
                    "[에사] — “e”", "[으사]"],
        "correct": "[의사] — toʻliq “ui”",
        "explanation": "<p>Soʻz <strong>boshida</strong> ㅢ toʻliq oʻqiladi: <strong>[의사]</strong>, "
                       "“shifokor”. U “i” ga faqat soʻz oʻrtasida yoki oxirida aylanadi "
                       "(회의 → [회이]), “e” ga esa egalik qoʻshimchasi boʻlganda.</p>",
    },
    {
        "text": "<p>Afsona <strong>회의</strong> ni “hoe-ui” deb oʻqidi. Toʻgʻrisi qaysi?</p>",
        "choices": ["[회이]", "[회의]", "[회에]", "[호이]"],
        "correct": "[회이]",
        "explanation": "<p><strong>[회이]</strong>. Bu yerda 의 soʻz <em>oxirida</em> turibdi, "
                       "shuning uchun oddiy [이] deb oʻqiladi. Maʼnosi — “yigʻilish”.</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["ㅘ yangi, mustaqil harf", "ㅑ = ㅏ + chiziqcha",
                    "ㅐ = ㅏ + ㅣ", "ㅟ = ㅜ + ㅣ"],
        "correct": "ㅘ yangi, mustaqil harf",
        "explanation": "<p><strong>ㅘ yangi harf emas</strong> — u ㅗ va ㅏ ning birikmasi. Qoʻshma "
                       "unlilarni yodlash shart emas: ichidagi ikkita unlini koʻring va tez "
                       "ayting.</p>",
    },
]


# =====================================================================
# PK-4 — Undoshlar 1: ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ
# =====================================================================

Q_PK4 = [
    {
        "text": "<p>Bu harf qaysi tovushni beradi?</p><p><strong>ㅁ</strong></p>",
        "choices": ["[m]", "[n]", "[b]", "[p]"],
        "correct": "[m]",
        "explanation": "<p><strong>[m]</strong> — oʻzbekcha <em>m</em> bilan bir xil. Harf shakli "
                       "yopiq ogʻizning, ya'ni lablarning rasmi.</p>",
    },
    {
        "text": "<p>Boʻgʻin boshida turgan <strong>ㅇ</strong> qanday oʻqiladi?</p>",
        "choices": ["Hech qanday — u jim", "[ng]", "[o]", "[h]"],
        "correct": "Hech qanday — u jim",
        "explanation": "<p>Boʻgʻin boshida <strong>ㅇ jim</strong> — u faqat unli uchun joy ochib "
                       "beradi. “ng” tovushini u faqat 받침 holatida beradi: 강 = [kang].</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>ㅅ harfi ㅣ unlisidan oldin qanday oʻqiladi?</strong></p>",
        "choices": ["[sh]", "[s]", "[ch]", "[t]"],
        "correct": "[sh]",
        "explanation": "<p><strong>[sh]</strong>. ㅅ harfi ㅣ va yotlashgan unlilardan (ㅑ ㅕ ㅛ ㅠ) "
                       "oldin avtomatik yumshaydi: 시 = [shi], 시간 = [shi-gan]. ㅏ oldida esa "
                       "oddiy “s”: 사 = [sa].</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>고기</strong></p>",
        "choices": ["[ko-gi]", "[go-gi]", "[ko-ki]", "[go-ki]"],
        "correct": "[ko-gi]",
        "explanation": "<p><strong>[ko-gi]</strong> — “goʻsht”. Birinchi ㄱ soʻz boshida, shuning "
                       "uchun jarangsiz “k”; ikkinchisi ikkita unli orasida, shuning uchun "
                       "jarangli “g”. Bitta harf, ikki koʻrinish — koreys buni sezmaydi "
                       "ham.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>바다</strong></p>",
        "choices": ["[pa-da]", "[ba-da]", "[pa-ta]", "[ba-ta]"],
        "correct": "[pa-da]",
        "explanation": "<p><strong>[pa-da]</strong> — “dengiz”. ㅂ soʻz boshida jarangsiz (“p”), "
                       "ㄷ esa ikkita unli orasida jarangli (“d”).</p>",
    },
    {
        "text": "<p>Bu soʻz qaysi harflardan tuzilgan?</p><p><strong>사람</strong></p>",
        "choices": ["ㅅㅏ + ㄹㅏㅁ", "ㅅㅏ + ㄴㅏㅁ", "ㅆㅏ + ㄹㅏㅁ", "ㅅㅓ + ㄹㅏㅁ"],
        "correct": "ㅅㅏ + ㄹㅏㅁ",
        "explanation": "<p><strong>ㅅ+ㅏ · ㄹ+ㅏ+ㅁ</strong> → [sa-ram], “odam”. ㄹ ikkita unli "
                       "orasida turgani uchun “r” ga yaqin oʻqiladi.</p>",
    },
    {
        "text": "<p>“ka-bang” tovushlari Hangulda qanday yoziladi?</p>",
        "choices": ["가방", "카방", "가밤", "가반"],
        "correct": "가방",
        "explanation": "<p><strong>가방</strong> — “sumka”. 가 = ㄱ+ㅏ, 방 = ㅂ+ㅏ+ㅇ. Oxiridagi "
                       "ㅇ 받침 boʻlgani uchun “ng” beradi.</p>",
    },
    {
        "text": "<p><strong>물</strong> va <strong>우리</strong> dagi ㄹ bir xil "
                "eshitiladimi?</p>",
        "choices": ["Yoʻq — 물 da “l” ga, 우리 da “r” ga yaqin",
                    "Ha, ikkalasi ham “r”",
                    "Ha, ikkalasi ham “l”",
                    "Yoʻq — 물 da “r” ga, 우리 da “l” ga yaqin"],
        "correct": "Yoʻq — 물 da “l” ga, 우리 da “r” ga yaqin",
        "explanation": "<p>Harf bitta, <strong>joyi boshqa</strong>. Boʻgʻin oxirida (물) til "
                       "tanglayda qoladi — oʻzbekcha <em>l</em> kabi. Ikkita unli orasida "
                       "(우리) esa til bir marta urib oʻtadi — <em>r</em> ga yaqin.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p>"
                "<p><strong>Koreys tilida k va g farqi maʼnoni ajratadimi?</strong></p>",
        "choices": ["Yoʻq — ular bitta harfning ikki koʻrinishi",
                    "Ha, xuddi oʻzbekchadagi kabi",
                    "Faqat soʻz oxirida ajratadi",
                    "Faqat qoʻshma soʻzlarda ajratadi"],
        "correct": "Yoʻq — ular bitta harfning ikki koʻrinishi",
        "explanation": "<p><strong>Ajratmaydi.</strong> Oʻzbekchada <em>kul</em> va <em>gul</em> "
                       "boshqa soʻz, koreyschada esa ㄱ bitta tovush. Koreys tilida maʼnoni "
                       "<em>nafas</em> ajratadi (ㄱ / ㅋ / ㄲ) — bu PK-5 va PK-6 mavzusi.</p>",
    },
    {
        "text": "<p>Bu soʻz qanday oʻqiladi?</p><p><strong>강</strong></p>",
        "choices": ["[kang]", "[ka]", "[kan]", "[gang]"],
        "correct": "[kang]",
        "explanation": "<p><strong>[kang]</strong> — “daryo”. Oxiridagi ㅇ 받침 holatida "
                       "<strong>“ng”</strong> beradi — uni tushirib qoldirmang. Boshdagi ㄱ esa "
                       "soʻz boshida boʻlgani uchun jarangsiz.</p>",
    },
    {
        "text": "<p>Dilnoza <strong>시간</strong> ni “si-gan” deb oʻqidi. Toʻgʻrisi qaysi?</p>",
        "choices": ["[shi-gan]", "[si-kan]", "[shi-kan]", "[si-gan] — toʻgʻri oʻqigan"],
        "correct": "[shi-gan]",
        "explanation": "<p><strong>[shi-gan]</strong>. ㅅ harfi ㅣ dan oldin har doim yumshaydi, "
                       "shuning uchun 시 = [shi]. Ikkinchi boʻgʻindagi “g” esa toʻgʻri — ㄱ "
                       "unlilar orasida jaranglashgan.</p>",
    },
    {
        "text": "<p>Qaysi javob notoʻgʻri?</p>",
        "choices": ["우리 dagi ㄹ ni titratib “urrri” deb aytish kerak",
                    "부산 soʻz boshida [pu] ga yaqin aytiladi",
                    "시 harfi [shi] deb oʻqiladi",
                    "강 oxiridagi ㅇ “ng” beradi"],
        "correct": "우리 dagi ㄹ ni titratib “urrri” deb aytish kerak",
        "explanation": "<p>Koreys <strong>ㄹ titratilmaydi</strong> — til tanglayga <em>bir "
                       "marta</em> urib oʻtadi: [u-ri], yengil va qisqa. Oʻzbekcha <em>r</em> "
                       "dan yumshoqroq.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-1 Mashq: Hangul bilan tanishuv",
        "description": "12 savol — Hangulning tuzilishi, 24 harf, boʻgʻin bloklari.",
        "tutorial":    "PK-1:",
        "level":       "easy",
        "questions":   Q_PK1,
    },
    {
        "title":       "PK-2 Mashq: Unlilar 1 — ㅏ ㅓ ㅗ ㅜ ㅡ ㅣ",
        "description": "12 savol — oltita asosiy unli, ㅓ/ㅗ farqi va ㅡ tovushi.",
        "tutorial":    "PK-2:",
        "level":       "easy",
        "questions":   Q_PK2,
    },
    {
        "title":       "PK-3 Mashq: Unlilar 2 — yotlashgan va qoʻshma unlilar",
        "description": "12 savol — ㅑ ㅕ ㅛ ㅠ, ㅐ/ㅔ va qoʻshma unlilar.",
        "tutorial":    "PK-3:",
        "level":       "easy",
        "questions":   Q_PK3,
    },
    {
        "title":       "PK-4 Mashq: Undoshlar 1 — ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅇ",
        "description": "12 savol — sakkizta oddiy undosh va jaranglashish qoidasi.",
        "tutorial":    "PK-4:",
        "level":       "easy",
        "questions":   Q_PK4,
    },
]
