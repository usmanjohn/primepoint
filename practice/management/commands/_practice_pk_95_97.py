# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-95 … PK-97.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
PK-95 koʻchirma gap oilasini yopadi — shuning uchun uning mashqida
oilaning toʻrt aʼzosini (다고 하다 · 다면서요 · 다니 · 답시고)
ajratuvchi savollar bor.
PK-97 esa sabab zinapoyasini yigʻadi (아/어서 → (으)니까 → 기 때문에
→ 는 바람에 → 로 인해 → 말미암아), va eng koʻp tekshiriladigan
narsa bitta: 로 인해 faqat OT oladi.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_95_97.py --master=prime \\
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
# PK-95 — (이)랍시고 · (으)ㄴ/는답시고
# ══════════════════════════════════════════════════════════════════════
Q_PK95 = [
    # 1–5 tanish
    {
        "text": "<p><b>-(느)ㄴ답시고</b> qanday maʼno beradi?</p>",
        "choices": ["…yaman deb (goʻyo) — kinoya bilan",
                    "…emish-a! (hayrat)",
                    "…deb oʻylagandim",
                    "…ning tengi yoʻq"],
        "correct": "…yaman deb (goʻyo) — kinoya bilan",
        "explanation": "<p><b>공부한답시고 게임만 한다</b> — “oʻqiyman "
                       "deb kirdi-yu, faqat oʻyin oʻynaydi”. "
                       "Gapiruvchi bahonaga <b>ishonmaydi</b>.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi ikki qismdan qisqargan?</p>",
        "choices": ["-다고 하다 + (으)면서",
                    "-다고 하다 + 니",
                    "-다고 하다 + ㅂ시고",
                    "-다고 하다 + 기"],
        "correct": "-다고 하다 + ㅂ시고",
        "explanation": "<p>공부한다고 하<b>ㅂ시고</b> → 하 tushadi → "
                       "<b>공부한답시고</b>. PK-92 va PK-93 dagi bilan "
                       "bir xil qisqarish.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>동생은 ___ 방에 들어가서 게임만 한다.</b> (공부하다)</p>",
        "choices": ["공부하답시고", "공부한답시고",
                    "공부하는답시고", "공부했답시고"],
        "correct": "공부한답시고",
        "explanation": "<p>Feʼl hozirgi zamonda ㄴ다/는다 oladi. 공부하 "
                       "da 받침 yoʻq → <b>공부한답시고</b>.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>___ 이런 걸 주다니.</b> (선물)</p>",
        "choices": ["선물랍시고", "선물이랍시고",
                    "선물답시고", "선물인답시고"],
        "correct": "선물이랍시고",
        "explanation": "<p>Ot bilan ulagich <b>(이)라</b>. 선물 da 받침 "
                       "bor → <b>이랍시고</b>. 받침 yoʻq boʻlsa: "
                       "요리<b>랍시고</b>.</p>",
    },
    {
        "text": "<p>Qolipdan keyin qanday natija keladi?</p>",
        "choices": ["Har doim yaxshi natija",
                    "Deyarli doim yomon yoki kulgili natija",
                    "Natija aytilmaydi",
                    "Faqat savol keladi"],
        "correct": "Deyarli doim yomon yoki kulgili natija",
        "explanation": "<p>Kinoya bor joyda natija koʻngildagidek "
                       "chiqmaydi. Shuning uchun "
                       "<s>공부한답시고 시험을 잘 봤다</s> — "
                       "notoʻgʻri.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>형은 자전거를 ___ 더 망가뜨렸다.</b> (고쳐 주다)</p>",
        "choices": ["고쳐 주답시고", "고쳐 준답시고",
                    "고쳐 줬답시고", "고쳐 주는답시고"],
        "correct": "고쳐 준답시고",
        "explanation": "<p>주다 → 준다 → <b>준답시고</b>. Ketidan "
                       "kutilgandek yomon natija keladi: "
                       "더 망가뜨렸다.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>친구는 ___ 옆에서 참견만 했다.</b> (돕다)</p>",
        "choices": ["돕답시고", "도운답시고", "돕는답시고", "도왔답시고"],
        "correct": "돕는답시고",
        "explanation": "<p>돕다 → 돕<b>는</b>다 → <b>돕는답시고</b>. "
                       "받침 bor → 는답시고.</p>",
    },
    {
        "text": "<p>Bu qolipning uchta shartidan qaysi biri "
                "<b>notoʻgʻri</b>?</p>",
        "choices": ["Bahona boshqa odamniki",
                    "Men bahonaga ishonmayman",
                    "Natija yomon",
                    "Gapning egasi yonimda turibdi"],
        "correct": "Gapning egasi yonimda turibdi",
        "explanation": "<p>Aksincha — bu odatda <b>orqadan</b> "
                       "aytiladigan gap. Gapning egasi eshitsa, bu "
                       "ochiq taʼna boʻladi.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi oilaga kiradi?</p>",
        "choices": ["Koʻchirma gap oilasi (PK-60 · 92 · 93 · 95)",
                    "Sabab oilasi (PK-35 · 48 · 49)",
                    "Aniqlovchi oilasi (PK-43 · 44 · 45)",
                    "Taxmin oilasi (PK-52 · 73)"],
        "correct": "Koʻchirma gap oilasi (PK-60 · 92 · 93 · 95)",
        "explanation": "<p>Xabar berish → tekshirish → hayron qolish → "
                       "<b>kinoya</b>. Toʻrttasi ham bir xil "
                       "qisqarishdan yasalgan.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["나는 요리랍시고 뭘 만들었는지 모르겠다.",
                    "선생님은 도와준답시고 오셨다.",
                    "동생은 공부하답시고 게임만 한다.",
                    "형은 자전거를 고쳐 준답시고 완벽하게 고쳤다."],
        "correct": "나는 요리랍시고 뭘 만들었는지 모르겠다.",
        "explanation": "<p>Oʻzi haqida <b>hazil bilan</b> ishlatish "
                       "mumkin. Qolganlari: ustoz haqida qoʻpol, "
                       "shakl xato (공부<b>한</b>답시고), va natija "
                       "yaxshi boʻlgani uchun kinoya oʻrinsiz.</p>",
    },
    {
        "text": "<p>Kim haqida bu qolipni ishlatib boʻlmaydi?</p>",
        "choices": ["Uka yoki singil",
                    "Doʻst",
                    "Ustoz, ota-ona, boshliq",
                    "Oʻzim (hazil bilan)"],
        "correct": "Ustoz, ota-ona, boshliq",
        "explanation": "<p>Qolip gapning egasini <b>past</b> "
                       "koʻrsatadi. Hurmat qilinadigan odam haqida "
                       "ishlatish qoʻpollik.</p>",
    },
    {
        "text": "<p>TOPIK yozma ishida bu qolipni ishlatish tavsiya "
                "qilinadimi?</p>",
        "choices": ["Ha, u rasmiy uslubga mos",
                    "Yoʻq — u hissiy baho beradi, rasmiy tahlil esa "
                    "buni yoqtirmaydi",
                    "Faqat 51-savolda",
                    "Faqat sarlavhada"],
        "correct": "Yoʻq — u hissiy baho beradi, rasmiy tahlil esa "
                   "buni yoqtirmaydi",
        "explanation": "<p>Kinoya — subyektiv. TOPIK 쓰기 esa "
                       "neytral, dalilga asoslangan uslubni "
                       "kutadi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>어제 ___ 전화를 못 받았어요. 죄송합니다.</b> (공부하다)</p>",
        "choices": ["공부한답시고", "공부하느라고",
                    "공부한다니", "공부한다면서"],
        "correct": "공부하느라고",
        "explanation": "<p>Bu — <b>oʻzim</b> haqimdagi rost sabab va "
                       "kechirim soʻrash. Neytral qolip kerak → "
                       "<b>느라고</b> (PK-69). 답시고 kinoya bildiradi "
                       "va oʻzi haqida jiddiy ishlatilmaydi.</p>",
    },
    {
        "text": "<p><b>느라고</b> va <b>답시고</b> farqi nimada?</p>",
        "choices": ["느라고 neytral (sabab rost), 답시고 kinoya (sabab "
                    "bahona)",
                    "느라고 oʻtgan, 답시고 hozirgi zamon",
                    "느라고 sifat, 답시고 feʼl bilan",
                    "Farqi yoʻq"],
        "correct": "느라고 neytral (sabab rost), 답시고 kinoya (sabab "
                   "bahona)",
        "explanation": "<p>Ikkalasi ham “bir ish qilib turib, ikkinchisi "
                       "buzildi” deydi. Farq — <b>ohangda</b> va kimga "
                       "nisbatan ishlatilishida.</p>",
    },
    {
        "text": "<p>Qaysi gapda gapiruvchi bahonaga <b>ishonadi</b>?</p>",
        "choices": ["동생은 공부한답시고 게임만 한다.",
                    "형은 고쳐 준답시고 더 망가뜨렸다.",
                    "동생은 공부하느라고 전화를 못 받았다.",
                    "친구는 돕는답시고 참견만 했다."],
        "correct": "동생은 공부하느라고 전화를 못 받았다.",
        "explanation": "<p>느라고 — sabab rost deb qabul qilinadi. "
                       "Qolgan uchtasida <b>답시고</b> bor, demak "
                       "gapiruvchi ishonmayapti.</p>",
    },
    {
        "text": "<p>Oʻzbekchada bu qolipning eng yaqin juftligi qaysi?</p>",
        "choices": ["“… tufayli”",
                    "“goʻyo … deb”, “-mish”",
                    "“…ning tengi yoʻq”",
                    "“…ga bogʻliq”"],
        "correct": "“goʻyo … deb”, “-mish”",
        "explanation": "<p>Oʻzbekchada kinoya alohida soʻz bilan "
                       "(goʻyo, emish) beriladi. Koreys tilida u "
                       "<b>qoʻshimchaning ichida</b> yashiringan — shu "
                       "sababli tarjima qilganda “goʻyo” ni qoʻshib "
                       "qoʻyish kerak.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["동생은 공부한답시고 게임만 한다.",
                    "선물랍시고 이런 걸 주다니.",
                    "형은 고쳐 준답시고 더 망가뜨렸다.",
                    "친구는 돕는답시고 참견만 했다."],
        "correct": "선물랍시고 이런 걸 주다니.",
        "explanation": "<p>선물 da 받침 bor → <b>선물이랍시고</b>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["공부한답시고 시험을 잘 봤다.",
                    "선생님은 도와준답시고 오셨다.",
                    "요리랍시고 만들었는데 아무도 못 먹었다.",
                    "동생은 공부하답시고 게임만 한다."],
        "correct": "요리랍시고 만들었는데 아무도 못 먹었다.",
        "explanation": "<p>Uch shart ham bajarilgan: bahona keltirilgan, "
                       "gapiruvchi ishonmaydi, natija yomon. "
                       "Qolganlari: yaxshi natija, hurmatli odam va "
                       "shakl xatosi.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang "
                "(한다체).</p>"
                "<p><b>“Akam velosipedni tuzataman deb, battar buzib "
                "qoʻydi.”</b></p>",
        "choices": ["형은 자전거를 고쳐 준답시고 더 망가뜨렸다.",
                    "형은 자전거를 고쳐 주느라고 더 망가뜨렸다.",
                    "형은 자전거를 고쳐 준다니 더 망가뜨렸다.",
                    "형은 자전거를 고쳐 준다면서요?"],
        "correct": "형은 자전거를 고쳐 준답시고 더 망가뜨렸다.",
        "explanation": "<p>“Tuzataman deb” + yomon natija = kinoya → "
                       "<b>답시고</b>. 느라고 boʻlsa gapiruvchi sababni "
                       "rost deb qabul qilgan boʻlardi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng tabiiy javob qaysi?</p>"
                "<p><b>가:</b> 동생이 방에서 뭐 해요?</p>"
                "<p><b>나:</b> ___</p>",
        "choices": ["공부한답시고 들어갔는데 두 시간째 게임만 해요.",
                    "공부한다니 들어갔는데 두 시간째 게임만 해요.",
                    "공부하려던 참이었어요.",
                    "공부하기 짝이 없어요."],
        "correct": "공부한답시고 들어갔는데 두 시간째 게임만 해요.",
        "explanation": "<p>Bahona + unga ishonmaslik + yomon natija — "
                       "qolipning uchala sharti ham shu javobda.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-96 — 기 짝이 없다
# ══════════════════════════════════════════════════════════════════════
Q_PK96 = [
    # 1–5 tanish
    {
        "text": "<p><b>기 짝이 없다</b> qanday maʼno beradi?</p>",
        "choices": ["…ning tengi yoʻq (oʻta yuqori daraja)",
                    "…dan farqi yoʻq",
                    "…ga bogʻliq",
                    "…yaman deb (goʻyo)"],
        "correct": "…ning tengi yoʻq (oʻta yuqori daraja)",
        "explanation": "<p><b>위험하기 짝이 없다</b> — “xavfliligining "
                       "tengi yoʻq”, yaʼni oʻta xavfli.</p>",
    },
    {
        "text": "<p><b>짝</b> soʻzi nimani anglatadi?</p>",
        "choices": ["chegara", "juft, teng", "daraja", "hisob"],
        "correct": "juft, teng",
        "explanation": "<p>짝이 없다 = “jufti yoʻq”, “tengi yoʻq”. "
                       "Oʻzbekcha “tengi yoʻq” iborasi bilan aynan bir "
                       "xil tasvir.</p>",
    },
    {
        "text": "<p>Qolip qaysi uch qismdan tuzilgan?</p>",
        "choices": ["기 (PK-46 otlashtirish) + 짝 (juft) + 없다",
                    "는 것 + 짝 + 있다",
                    "(으)ㅁ + 정도 + 없다",
                    "아/어 + 짝 + 하다"],
        "correct": "기 (PK-46 otlashtirish) + 짝 (juft) + 없다",
        "explanation": "<p>Shuning uchun <s>위험한 짝이 없다</s> "
                       "notoʻgʻri — aniqlovchi shakl emas, <b>기</b> "
                       "kerak.</p>",
    },
    {
        "text": "<p>Qolip oldida qanday soʻz turishi kerak?</p>",
        "choices": ["Feʼl", "Sifat", "Ot", "Son"],
        "correct": "Sifat",
        "explanation": "<p>Qolip harakatni emas, <b>holatni "
                       "baholaydi</b>. Shuning uchun "
                       "<s>가기 짝이 없다</s> degan gap yoʻq.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>그때의 방법은 지금 보면 ___.</b> (위험하다)</p>",
        "choices": ["위험한 짝이 없다", "위험하기 짝이 없다",
                    "위험하는 짝이 없다", "위험함 짝이 없다"],
        "correct": "위험하기 짝이 없다",
        "explanation": "<p>Sifat oʻzagi + <b>기</b> + 짝이 없다.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>그 일을 생각하면 ___.</b> (부끄럽다)</p>",
        "choices": ["부끄럽기 짝이 없다", "부끄러운 짝이 없다",
                    "부끄럽는 짝이 없다", "부끄러움 짝이 없다"],
        "correct": "부끄럽기 짝이 없다",
        "explanation": "<p>부끄럽다 → 부끄럽<b>기</b> 짝이 없다 — "
                       "“uyatning tengi yoʻq”.</p>",
    },
    {
        "text": "<p>Otni aniqlaganda shakl qanday oʻzgaradi?</p>"
                "<p><b>위험하기 짝이 없다 + 방법</b></p>",
        "choices": ["위험하기 짝이 없다 방법",
                    "위험하기 짝이 없은 방법",
                    "위험하기 짝이 없는 방법",
                    "위험하기 짝이 없던 방법"],
        "correct": "위험하기 짝이 없는 방법",
        "explanation": "<p>없다 → <b>없는</b> (PK-45). Bu shakl gazeta "
                       "va maqola tilida juda koʻp uchraydi.</p>",
    },
    {
        "text": "<p>Qaysi sifatlar bu qolip bilan koʻp yuradi?</p>",
        "choices": ["예쁘다, 좋다, 재미있다, 맛있다",
                    "위험하다, 부끄럽다, 어리석다, 안타깝다",
                    "크다, 작다, 길다, 짧다",
                    "빠르다, 느리다, 높다, 낮다"],
        "correct": "위험하다, 부끄럽다, 어리석다, 안타깝다",
        "explanation": "<p>Qolip deyarli doim <b>salbiy</b> sifat "
                       "bilan keladi — kuchli hukmni odam koʻpincha "
                       "norozi boʻlganda chiqaradi.</p>",
    },
    {
        "text": "<p>Bu qolip qaysi uslubga tegishli?</p>",
        "choices": ["Kundalik ogʻzaki nutq",
                    "문어체 — maqola, insho, TOPIK 쓰기",
                    "Faqat sheʼriyat",
                    "Faqat 반말"],
        "correct": "문어체 — maqola, insho, TOPIK 쓰기",
        "explanation": "<p>Doʻstlar orasidagi gapda u kitobdan "
                       "koʻchirilgandek eshitiladi. Kundalik nutqda "
                       "<b>아주 / 진짜</b> yetarli.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>아무 준비도 없이 시작한 것은 ___.</b> "
                "(어리석다, oʻtgan zamon)</p>",
        "choices": ["어리석기 짝이 없다", "어리석기 짝이 없었다",
                    "어리석은 짝이 없었다", "어리석기 짝이 없는다"],
        "correct": "어리석기 짝이 없었다",
        "explanation": "<p>없다 oddiy sifat kabi tuslanadi: oʻtgan "
                       "zamon → <b>없었다</b>.</p>",
    },
    {
        "text": "<p>Ijobiy sifat bilan ishlatsa boʻladimi?</p>",
        "choices": ["Yoʻq, hech qachon",
                    "Boʻladi (기쁘기 짝이 없다), lekin juda rasmiy va "
                    "kamdan-kam",
                    "Faqat ijobiy sifat bilan ishlatiladi",
                    "Faqat sonlar bilan"],
        "correct": "Boʻladi (기쁘기 짝이 없다), lekin juda rasmiy va "
                   "kamdan-kam",
        "explanation": "<p>Yozayotganda salbiy sifatni tanlang — xato "
                       "qilmaysiz.</p>",
    },
    {
        "text": "<p>Feʼlni bu qolip bilan baholamoqchi boʻlsangiz nima "
                "qilasiz?</p>",
        "choices": ["Feʼlga toʻgʻridan-toʻgʻri 기 짝이 없다 qoʻshaman",
                    "Butun ishni ot qilib olib, keyin sifat bilan "
                    "baholayman: 그렇게 행동한 것은 어리석기 짝이 없다",
                    "Feʼlni aniqlovchi shaklga oʻgiraman",
                    "Buning iloji yoʻq"],
        "correct": "Butun ishni ot qilib olib, keyin sifat bilan "
                   "baholayman: 그렇게 행동한 것은 어리석기 짝이 없다",
        "explanation": "<p>Qolip faqat sifat oladi, shuning uchun "
                       "baholanadigan harakat <b>ega</b> oʻrniga "
                       "chiqariladi.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p>Ikki qolipning farqi nimada?</p>"
                "<p><b>(으)ㄹ 정도로</b> · <b>기 짝이 없다</b></p>",
        "choices": ["Birinchisi oʻlchov beradi (ketidan misol keladi), "
                    "ikkinchisi hukm chiqaradi (gap tugaydi)",
                    "Birinchisi yozma, ikkinchisi ogʻzaki",
                    "Birinchisi feʼl, ikkinchisi ot bilan",
                    "Farqi yoʻq"],
        "correct": "Birinchisi oʻlchov beradi (ketidan misol keladi), "
                   "ikkinchisi hukm chiqaradi (gap tugaydi)",
        "explanation": "<p><b>손이 떨릴 정도로 추웠다</b> — misol bilan "
                       "oʻlchov. <b>위험하기 짝이 없다</b> — yakuniy "
                       "baho.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>손이 ___ 추웠다.</b></p>",
        "choices": ["떨리기 짝이 없게", "떨릴 정도로",
                    "떨리기 짝이 없다", "떨린답시고"],
        "correct": "떨릴 정도로",
        "explanation": "<p>Bu yerda <b>oʻlchov</b> berilyapti — “qoʻl "
                       "titraydigan darajada”. Bu PK-82 ning "
                       "ishi.</p>",
    },
    {
        "text": "<p>Doʻstingizga ovqat haqida gapiryapsiz. Qaysi biri "
                "tabiiy?</p>",
        "choices": ["야, 이거 맛없기 짝이 없어!",
                    "야, 이거 진짜 맛없어!",
                    "야, 이거 맛없기 짝이 없는다!",
                    "야, 이거 맛없기 짝이 없으니까!"],
        "correct": "야, 이거 진짜 맛없어!",
        "explanation": "<p>기 짝이 없다 — <b>yozma</b> qolip. Ogʻzaki "
                       "nutqda 진짜 / 아주 ishlatiladi.</p>",
    },
    {
        "text": "<p>Oʻzbekchada bu qolipning eng yaqin juftligi qaysi?</p>",
        "choices": ["“…ga bogʻliq”",
                    "“tengi yoʻq”, “cheki yoʻq”",
                    "“… hisob”",
                    "“… tufayli”"],
        "correct": "“tengi yoʻq”, “cheki yoʻq”",
        "explanation": "<p>Ikkala til ham eng yuqori darajani "
                       "<b>juftlik</b> orqali oʻlchaydi: 짝 = teng.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["그 방법은 위험하기 짝이 없다.",
                    "그 사람은 가기 짝이 없다.",
                    "그 일을 생각하면 부끄럽기 짝이 없다.",
                    "안타깝기 짝이 없는 일이었다."],
        "correct": "그 사람은 가기 짝이 없다.",
        "explanation": "<p>가다 — feʼl. Qolip faqat <b>sifat</b> "
                       "bilan ishlaydi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["위험한 짝이 없다.",
                    "위험하기 짝이 없다 방법이었다.",
                    "위험하기 짝이 없는 방법이었다.",
                    "위험하기 짝이 있다."],
        "correct": "위험하기 짝이 없는 방법이었다.",
        "explanation": "<p>Otni aniqlaganda <b>없는</b> boʻladi. "
                       "Qolganlarida 기 tushib qolgan, aniqlovchi "
                       "shakl yoʻq yoki 없다 → 있다 qilib "
                       "yuborilgan.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang "
                "(한다체).</p>"
                "<p><b>“Hech qanday tayyorgarliksiz boshlash — "
                "ahmoqlikning tengi yoʻq edi.”</b></p>",
        "choices": ["아무 준비도 없이 시작한 것은 어리석기 짝이 없었다.",
                    "아무 준비도 없이 시작한 것은 어리석을 정도였다.",
                    "아무 준비도 없이 시작하기 짝이 없었다.",
                    "아무 준비도 없이 시작한 것은 어리석은 짝이 없었다."],
        "correct": "아무 준비도 없이 시작한 것은 어리석기 짝이 없었다.",
        "explanation": "<p>Harakat <b>ega</b> ga chiqarilgan "
                       "(시작한 것은), keyin sifat + 기 짝이 없다.</p>",
    },
    {
        "text": "<p>Soʻzlarni toʻgʻri tartibda joylang (한다체).</p>"
                "<p><b>짝이 없다 / 지금 보면 / 그때의 방법은 / 위험하기</b></p>",
        "choices": ["그때의 방법은 지금 보면 위험하기 짝이 없다.",
                    "지금 보면 위험하기 그때의 방법은 짝이 없다.",
                    "위험하기 짝이 없다 그때의 방법은 지금 보면.",
                    "그때의 방법은 위험하기 지금 보면 짝이 없다."],
        "correct": "그때의 방법은 지금 보면 위험하기 짝이 없다.",
        "explanation": "<p>Ega (방법은) → hol (지금 보면) → kesim "
                       "(위험하기 짝이 없다). Kesim doim oxirida.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-97 — (으)로 인해 · (으)로 말미암아
# ══════════════════════════════════════════════════════════════════════
Q_PK97 = [
    # 1–5 tanish
    {
        "text": "<p><b>(으)로 인해</b> qanday maʼno beradi?</p>",
        "choices": ["… tufayli (rasmiy sabab)",
                    "… bilan barobar",
                    "…ning tengi yoʻq",
                    "…ga bogʻliq"],
        "correct": "… tufayli (rasmiy sabab)",
        "explanation": "<p><b>폭우로 인해 경기가 취소되었다</b> — kuchli "
                       "yomgʻir tufayli oʻyin bekor qilindi. Bu — "
                       "rasmiy yozma sabab.</p>",
    },
    {
        "text": "<p>Bu qolipning oldida nima turishi kerak?</p>",
        "choices": ["Faqat feʼl", "Faqat ot", "Faqat sifat",
                    "Butun gap"],
        "correct": "Faqat ot",
        "explanation": "<p>Bu — <b>기 때문에</b> bilan asosiy farq. "
                       "때문에 gapni ham, otni ham oladi; 로 인해 esa "
                       "faqat otni.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>___ 경기가 취소되었다.</b> (폭우)</p>",
        "choices": ["폭우으로 인해", "폭우로 인해",
                    "폭우로 인한", "폭우기 때문에"],
        "correct": "폭우로 인해",
        "explanation": "<p>폭우 da 받침 yoʻq → <b>로</b>. 받침 bor "
                       "boʻlsa 으로 (지진<b>으로</b>).</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>___ 피해가 컸다.</b> (지진)</p>",
        "choices": ["지진로 인해", "지진으로 인해",
                    "지진으로 인한", "지진이 인해"],
        "correct": "지진으로 인해",
        "explanation": "<p>지진 da 받침 (ㄴ) bor → <b>으로</b>.</p>",
    },
    {
        "text": "<p>Otni aniqlaganda shakl qanday boʻladi?</p>"
                "<p><b>폭우로 ___ 피해</b></p>",
        "choices": ["인해", "인한", "인하고", "인해서"],
        "correct": "인한",
        "explanation": "<p><b>폭우로 인한 피해</b> — “kuchli yomgʻir "
                       "tufayli koʻrilgan zarar”. Bu — gazeta "
                       "sarlavhalarining tili.</p>",
    },

    # 6–12 qoʻllash
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>___ 시골 학교가 문을 닫았다.</b> (인구 감소)</p>",
        "choices": ["인구 감소로 인해", "인구 감소으로 인해",
                    "인구 감소로 인한", "인구 감소기 때문에"],
        "correct": "인구 감소로 인해",
        "explanation": "<p>감소 da 받침 yoʻq → <b>로</b>. Kesimga "
                       "bogʻlanayotgani uchun <b>인해</b>, 인한 "
                       "emas.</p>",
    },
    {
        "text": "<p>“Kech qolganim uchun” — buni 로 인해 bilan qanday "
                "aytamiz?</p>",
        "choices": ["늦었로 인해",
                    "늦기로 인해",
                    "지각으로 인해 — avval otga aylantiramiz",
                    "Buning iloji yoʻq"],
        "correct": "지각으로 인해 — avval otga aylantiramiz",
        "explanation": "<p>Qolip faqat ot oladi. Feʼlli gapni otga "
                       "siqish — TOPIK 쓰기 ning asosiy koʻnikmasi: "
                       "늦다 → <b>지각</b>.</p>",
    },
    {
        "text": "<p>Bu feʼlli gaplarni otga siqing: <b>비가 오다 · 인구가 "
                "줄다 · 사람이 다치다</b></p>",
        "choices": ["폭우 · 인구 감소 · 부상",
                    "비 · 인구 · 사람",
                    "오기 · 줄기 · 다치기",
                    "온 것 · 준 것 · 다친 것"],
        "correct": "폭우 · 인구 감소 · 부상",
        "explanation": "<p>Rasmiy uslub voqeani <b>nomlashni</b> "
                       "yaxshi koʻradi. Shuning uchun 로 인해 ni "
                       "oʻrganish sizga qolip emas, <b>yozish "
                       "uslubi</b> beradi.</p>",
    },
    {
        "text": "<p><b>(으)로 말미암아</b> ning oʻrni qanday?</p>",
        "choices": ["로 인해 dan koʻra kundalikroq",
                    "Maʼno bir xil, lekin ogʻirroq, adabiyroq va "
                    "koʻpincha katta, qaytarib boʻlmas natija haqida",
                    "Faqat ogʻzaki nutqda",
                    "Faqat savol gaplarda"],
        "correct": "Maʼno bir xil, lekin ogʻirroq, adabiyroq va "
                   "koʻpincha katta, qaytarib boʻlmas natija haqida",
        "explanation": "<p><b>그 결정으로 말미암아 한 마을의 백 년이 "
                       "끝났다.</b> Uning kuchi kamdan-kam "
                       "kelishida — koʻp ishlatilsa, kuchi "
                       "yoʻqoladi.</p>",
    },
    {
        "text": "<p>Bu qolip qanday sabab bilan yuradi?</p>",
        "choices": ["Kichik, shaxsiy sabab",
                    "Katta, tashqi, koʻpchilikka taʼsir qiladigan sabab",
                    "Faqat ijobiy sabab",
                    "Faqat kelasi zamondagi sabab"],
        "correct": "Katta, tashqi, koʻpchilikka taʼsir qiladigan sabab",
        "explanation": "<p>폭우, 지진, 화재, 사고, 감염, 인구 감소, "
                       "기술 발전… <s>배가 고픔으로 인해 밥을 먹었다</s> "
                       "— kulgili chiqadi.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["화재로 인해 건물이 무너졌다.",
                    "화재으로 인해 건물이 무너졌다.",
                    "화재가 인해 건물이 무너졌다.",
                    "화재로 인해서기 때문에 건물이 무너졌다."],
        "correct": "화재로 인해 건물이 무너졌다.",
        "explanation": "<p>화재 da 받침 yoʻq → <b>로</b>. Va 로 인해 "
                       "bilan 기 때문에 ni bir gapda qoʻshib "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p>"
                "<p><b>___ 문제는 시골에서 먼저 나타난다.</b> "
                "(인구 감소 + aniqlovchi)</p>",
        "choices": ["인구 감소로 인해", "인구 감소로 인한",
                    "인구 감소기 때문에", "인구 감소로 말미암아"],
        "correct": "인구 감소로 인한",
        "explanation": "<p>문제 — ot, va u aniqlanmoqda. Demak "
                       "<b>인한</b>.</p>",
    },

    # 13–16 farqlash
    {
        "text": "<p><b>기 때문에</b> va <b>(으)로 인해</b> ning asosiy "
                "farqi nimada?</p>",
        "choices": ["때문에 gap va otni ham oladi, 로 인해 esa faqat "
                    "otni",
                    "때문에 rasmiy, 로 인해 kundalik",
                    "때문에 oʻtgan, 로 인해 hozirgi zamon",
                    "Farqi yoʻq"],
        "correct": "때문에 gap va otni ham oladi, 로 인해 esa faqat "
                   "otni",
        "explanation": "<p>늦었<b>기 때문에</b> ✓ · <s>늦었로 인해</s> ✗ · "
                       "지각<b>으로 인해</b> ✓. Uslub jihatdan ham "
                       "로 인해 rasmiyroq.</p>",
    },
    {
        "text": "<p>Sabab zinapoyasida eng rasmiy shakl qaysi?</p>",
        "choices": ["아/어서", "기 때문에", "는 바람에", "(으)로 말미암아"],
        "correct": "(으)로 말미암아",
        "explanation": "<p>Zinapoya: 아/어서 (35) → (으)니까 (48) → "
                       "기 때문에 (49) → 는 바람에 (69) → 로 인해 (97) "
                       "→ <b>로 말미암아</b> (97).</p>",
    },
    {
        "text": "<p>Boʻsh joyga eng mos qolip qaysi?</p>"
                "<p><b>배가 고___ 밥을 먹었다.</b></p>",
        "choices": ["픔으로 인해", "파서", "픔으로 말미암아",
                    "프기 짝이 없어서"],
        "correct": "파서",
        "explanation": "<p>Kichik, shaxsiy sabab uchun 로 인해 ogʻirlik "
                       "qiladi. Kundalik sabab — <b>아/어서</b> "
                       "(PK-35).</p>",
    },
    {
        "text": "<p>Oʻzbekchada bu zinapoya qanday koʻrinadi?</p>",
        "choices": ["“-gani uchun” → “tufayli” → “oqibatida”",
                    "“tufayli” → “-gani uchun” → “oqibatida”",
                    "Hammasi bir xil tarjima qilinadi",
                    "Oʻzbekchada bunday farq yoʻq"],
        "correct": "“-gani uchun” → “tufayli” → “oqibatida”",
        "explanation": "<p>Va eʼtibor bering: oʻzbekchada ham “tufayli” "
                       "bilan “oqibatida” <b>otdan keyin</b> keladi, "
                       "“-gani uchun” esa feʼldan keyin. Ikkala tilda "
                       "ham rasmiy sabab ot talab qiladi.</p>",
    },

    # 17–18 xato topish
    {
        "text": "<p>Qaysi gapda xato bor?</p>",
        "choices": ["폭우로 인해 경기가 취소되었다.",
                    "비가 왔기로 인해 경기가 취소되었다.",
                    "지진으로 인해 피해가 컸다.",
                    "인구 감소로 인한 문제가 생겼다."],
        "correct": "비가 왔기로 인해 경기가 취소되었다.",
        "explanation": "<p>Qolip faqat <b>ot</b> oladi. Toʻgʻrisi: "
                       "<b>폭우로 인해</b> yoki <b>비가 왔기 "
                       "때문에</b>.</p>",
    },
    {
        "text": "<p>Qaysi gap toʻgʻri?</p>",
        "choices": ["폭우로 인해 피해가 컸다.",
                    "폭우로 인한 피해가 컸다고 인해 말했다.",
                    "지진로 인해 피해가 컸다.",
                    "배가 고픔으로 인해 밥을 먹었다."],
        "correct": "폭우로 인해 피해가 컸다.",
        "explanation": "<p>Qolganlari: qolip takrorlangan, 받침 bor "
                       "otga 로 qoʻyilgan (지진<b>으로</b> boʻlishi "
                       "kerak), va kichik shaxsiy sabab uchun ogʻir "
                       "qolip ishlatilgan.</p>",
    },

    # 19–20 tuzish
    {
        "text": "<p>Koreyschaga toʻgʻri oʻgirilgan variantni tanlang "
                "(한다체).</p>"
                "<p><b>“Aholi kamayishi tufayli qishloq maktabi "
                "yopildi.”</b></p>",
        "choices": ["인구 감소로 인해 시골 학교가 문을 닫았다.",
                    "인구가 줄었기로 인해 시골 학교가 문을 닫았다.",
                    "인구 감소로 인한 시골 학교가 문을 닫았다.",
                    "인구 감소기 때문에 시골 학교가 문을 닫았다."],
        "correct": "인구 감소로 인해 시골 학교가 문을 닫았다.",
        "explanation": "<p>Sabab otga siqilgan (인구 감소), kesimga "
                       "bogʻlanayotgani uchun <b>인해</b>, va 감소 da "
                       "받침 yoʻq → <b>로</b>.</p>",
    },
    {
        "text": "<p>Gazeta sarlavhasi uchun eng mos shakl qaysi?</p>"
                "<p><b>“Kuchli yomgʻir tufayli koʻrilgan zarar”</b></p>",
        "choices": ["폭우로 인한 피해",
                    "폭우로 인해 피해",
                    "폭우가 왔기 때문에 피해",
                    "폭우로 말미암아 피해가 있다"],
        "correct": "폭우로 인한 피해",
        "explanation": "<p>Sarlavha — <b>ot birikmasi</b>. Otni "
                       "aniqlaganda 인해 emas, <b>인한</b> "
                       "ishlatiladi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-95 Mashq: (이)랍시고 · (으)ㄴ/는답시고",
        "description": "20 savol — 다고 하 + ㅂ시고 qisqarishi, feʼl va "
                       "ot shakllari, kinoyaning uch sharti, 느라고 dan "
                       "farqi va qolipning muloqotdagi chegarasi.",
        "tutorial":    "PK-95:",
        "level":       "medium",
        "questions":   Q_PK95,
    },
    {
        "title":       "PK-96 Mashq: 기 짝이 없다",
        "description": "20 savol — 짝 ning maʼnosi, faqat sifat bilan "
                       "ishlashi, 짝이 없는 aniqlovchi shakli, yozma "
                       "uslub va (으)ㄹ 정도로 dan farqi.",
        "tutorial":    "PK-96:",
        "level":       "medium",
        "questions":   Q_PK96,
    },
    {
        "title":       "PK-97 Mashq: (으)로 말미암아 · (으)로 인해",
        "description": "20 savol — 받침 tarmogʻi, faqat ot olishi, "
                       "gapni otga siqish, 인한 aniqlovchi shakli va "
                       "butun sabab zinapoyasi.",
        "tutorial":    "PK-97:",
        "level":       "medium",
        "questions":   Q_PK97,
    },
]
