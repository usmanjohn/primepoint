# -*- coding: utf-8 -*-
"""Prime Korean mashqlar — PK-77 … PK-79.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Har uchala mashqda bitta 한다체 (PK-74) savoli bor — yozma uslub
endi har darsda takrorlanadi.

Written with STYLE_GUIDE_PK_PRACTICE.md · lesson list in toc_pk_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pk_77_79.py --master=prime \\
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
# PK-77 — 다가, 다가 보면, 다가 보니
# ══════════════════════════════════════════════════════════════════════
Q_PK77 = [
    # 1–5 tanish
    {
        "text": "<p><b>다가</b> qanday maʼno beradi?</p>",
        "choices": ["Ish oʻrtasida uzildi va boshqasiga oʻtildi",
                    "Ish butunlay tugadi",
                    "Ikki ish bir vaqtda davom etadi",
                    "Ish hali boshlanmagan"],
        "correct": "Ish oʻrtasida uzildi va boshqasiga oʻtildi",
        "explanation": "<p>밥을 먹다가 나갔어요 — ovqat <b>tugamadi</b>, "
                       "yarim yoʻlda qoldi.</p>",
    },
    {
        "text": "<p><b>다가 보면</b> qaysi vaqtga qaraydi?</p>",
        "choices": ["Kelajakka — davom etsangiz natija boʻladi",
                    "Oʻtmishga — allaqachon boʻlgan",
                    "Hozirgi paytga", "Vaqt bilan bogʻliq emas"],
        "correct": "Kelajakka — davom etsangiz natija boʻladi",
        "explanation": "<p>공부하다가 보면 실력이 늘 거예요 — dalda va "
                       "maslahat ohangi.</p>",
    },
    {
        "text": "<p><b>다가 보니</b> qanday ohang beradi?</p>",
        "choices": ["Kashfiyot va hayrat — “oʻzim sezmay boʻlib qolibdi”",
                    "Buyruq", "Ogohlantirish", "Iltimos"],
        "correct": "Kashfiyot va hayrat — “oʻzim sezmay boʻlib qolibdi”",
        "explanation": "<p>드라마를 보다가 보니 한국어가 늘었어요 — natija "
                       "kutilmagan edi.</p>",
    },
    {
        "text": "<p>다가 va 았/었다가 farqi nima?</p>",
        "choices": ["다가 — ish yarim qoldi; 았/었다가 — ish tugadi, "
                    "keyin teskarisi boʻldi",
                    "다가 — kelajak; 았/었다가 — hozir",
                    "다가 — feʼl bilan; 았/었다가 — sifat bilan",
                    "Farqi yoʻq"],
        "correct": "다가 — ish yarim qoldi; 았/었다가 — ish tugadi, "
                   "keyin teskarisi boʻldi",
        "explanation": "<p>학교에 <b>가다가</b> 왔어요 (yetmadim) ↔ "
                       "학교에 <b>갔다가</b> 왔어요 (bordim va qaytdim).</p>",
    },
    {
        "text": "<p>다가 da ikkala gapning egasi qanday boʻlishi kerak?</p>",
        "choices": ["Bir xil", "Har xil", "Farqi yoʻq",
                    "Birinchi gapda ega boʻlmasligi kerak"],
        "correct": "Bir xil",
        "explanation": "<p>❌ 제가 밥을 먹다가 동생이 나갔어요 — ikki xil ega.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 책을 <b>____</b> 잠이 들었어요. (읽다)</p>",
        "choices": ["읽다가", "읽었다가", "읽는다가", "읽어다가"],
        "correct": "읽다가",
        "explanation": "<p>Oʻzak + 다가. 받침 farqi yoʻq, zamon yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 창문을 <b>____</b> 추워서 닫았어요. (열다)</p>",
        "choices": ["열었다가", "열다가", "여다가", "열는다가"],
        "correct": "열었다가",
        "explanation": "<p>Ochish <b>tugadi</b>, keyin teskarisi (yopish) — "
                       "shuning uchun <b>았/었다가</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 한국어를 매일 공부하다가 <b>____</b> "
                "실력이 늘 거예요.</p>",
        "choices": ["보면", "보니", "봐서", "본"],
        "correct": "보면",
        "explanation": "<p>Natija <b>kelajakda</b> — 보면.</p>",
    },
    {
        "text": "<p>Toʻldiring: 매일 조금씩 걷다가 <b>____</b> "
                "오 킬로그램이 빠졌어요.</p>",
        "choices": ["보니", "보면", "보고", "볼까"],
        "correct": "보니",
        "explanation": "<p>Natija <b>allaqachon</b> boʻlgan — 보니, va "
                       "ikkinchi gap oʻtgan zamonda.</p>",
    },
    {
        "text": "<p>Toʻldiring: 밥을 <b>____</b> 전화를 받았어요. (먹다)</p>",
        "choices": ["먹다가", "먹었다가", "먹으니까", "먹어서"],
        "correct": "먹다가",
        "explanation": "<p>Ovqat yeyish uzildi — <b>다가</b>.</p>",
    },
    {
        "text": "<p>“Koreyada yashayversangiz, bu madaniyatni tushunib "
                "qolasiz” — koreyschada?</p>",
        "choices": ["한국에서 살다가 보면 이 문화를 이해하게 될 거예요.",
                    "한국에서 살다가 보니 이 문화를 이해하게 될 거예요.",
                    "한국에서 살았다가 이 문화를 이해했어요.",
                    "한국에서 사는 길에 이 문화를 이해할 거예요."],
        "correct": "한국에서 살다가 보면 이 문화를 이해하게 될 거예요.",
        "explanation": "<p>Kelajakdagi natija — <b>다가 보면</b>.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "매일 걷다가 보니 살이 빠졌어요.</p>",
        "choices": ["매일 걷다가 보니 살이 빠졌다.",
                    "매일 걷다가 보니 살이 빠진다.",
                    "매일 걷다가 보니 살이 빠졌는다.",
                    "매일 걷다가 보니 살이 빠지다."],
        "correct": "매일 걷다가 보니 살이 빠졌다.",
        "explanation": "<p>Oʻtgan zamon 한다체 da <b>았/었다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p>Qaysi jumla “maktabga yetib bormadim” degan maʼnoni "
                "beradi?</p>",
        "choices": ["학교에 가다가 왔어요.", "학교에 갔다가 왔어요.",
                    "학교에 가는 길에 왔어요.", "학교에 가고 나서 왔어요."],
        "correct": "학교에 가다가 왔어요.",
        "explanation": "<p>Zamonsiz <b>가다가</b> — yurish <b>yarim yoʻlda "
                       "uzildi</b>. 갔다가 esa yetib borganini bildiradi.</p>",
    },
    {
        "text": "<p>“학교에 가는 길에 친구를 만났어요” va “학교에 가다가 "
                "친구를 만났어요” farqi nima?</p>",
        "choices": ["길에 — uchratdim va ketaverdim; 다가 — uchratdim va "
                    "toʻxtadim",
                    "길에 — oʻtgan zamon; 다가 — kelasi zamon",
                    "길에 — rasmiy; 다가 — ogʻzaki",
                    "Farqi yoʻq"],
        "correct": "길에 — uchratdim va ketaverdim; 다가 — uchratdim va "
                   "toʻxtadim",
        "explanation": "<p>는 길에 (PK-75) da yoʻl <b>davom etadi</b>, "
                       "다가 da esa <b>uziladi</b>.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["한국어를 공부하다가 보니 실력이 늘 거예요.",
                    "한국어를 공부하다가 보면 실력이 늘 거예요.",
                    "드라마를 보다가 보니 한국어가 늘었어요.",
                    "매일 걷다가 보니 살이 빠졌어요."],
        "correct": "한국어를 공부하다가 보니 실력이 늘 거예요.",
        "explanation": "<p><b>보니</b> — oʻtmishdagi kashfiyot, ikkinchi gap "
                       "oʻtgan zamonda boʻlishi kerak. Kelajak natija "
                       "uchun <b>보면</b>.</p>",
    },
    {
        "text": "<p>다가 보면 va 다가 보니 ni nima ajratadi?</p>",
        "choices": ["보면 — natija hali boʻlmagan; 보니 — natija allaqachon "
                    "boʻlgan",
                    "보면 — feʼl bilan; 보니 — sifat bilan",
                    "보면 — bitta ega; 보니 — ikkita ega",
                    "보면 — salbiy; 보니 — ijobiy"],
        "correct": "보면 — natija hali boʻlmagan; 보니 — natija allaqachon "
                   "boʻlgan",
        "explanation": "<p>Oʻzbekcha: “qil<b>aversang</b> boʻladi” ↔ "
                       "“qil<b>averib</b>, qarabsizki boʻlib qolibdi”.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>제가 밥을 먹다가 동생이 나갔어요.</s></p>",
        "choices": ["다가 da ikkala gapning egasi bir xil boʻlishi kerak",
                    "밥을 emas, 밥이",
                    "먹다가 emas, 먹었다가",
                    "나갔어요 emas, 나와요"],
        "correct": "다가 da ikkala gapning egasi bir xil boʻlishi kerak",
        "explanation": "<p>Bu yerda “men” va “ukam” — ikki xil ega.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>드라마를 보다가 보면 한국어가 "
                "늘었어요.</s></p>",
        "choices": ["Natija allaqachon boʻlgan — 보니 boʻlishi kerak",
                    "드라마를 emas, 드라마가",
                    "보다가 emas, 봤다가",
                    "늘었어요 emas, 늘 거예요"],
        "correct": "Natija allaqachon boʻlgan — 보니 boʻlishi kerak",
        "explanation": "<p>늘었어요 — oʻtgan zamon, demak kashfiyot: "
                       "<b>보다가 보니</b>.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Derazani ochdim-u, sovuq boʻlgani uchun yopdim” — "
                "koreyschada?</p>",
        "choices": ["창문을 열었다가 추워서 닫았어요.",
                    "창문을 열다가 추워서 닫았어요.",
                    "창문을 열고 나서 추워서 닫았어요.",
                    "창문을 여는 길에 추워서 닫았어요."],
        "correct": "창문을 열었다가 추워서 닫았어요.",
        "explanation": "<p>Ochish <b>tugagan</b>, keyin teskarisi — "
                       "<b>았/었다가</b>.</p>",
    },
    {
        "text": "<p>“Kitob oʻqiyotib uxlab qoldim” — koreyschada?</p>",
        "choices": ["책을 읽다가 잠이 들었어요.",
                    "책을 읽었다가 잠이 들었어요.",
                    "책을 읽는 길에 잠이 들었어요.",
                    "책을 읽고 나서 잠이 들었어요."],
        "correct": "책을 읽다가 잠이 들었어요.",
        "explanation": "<p>Oʻqish <b>tugamadi</b> — uyqu uni uzdi. Bu "
                       "다가 ning eng klassik misoli.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-78 — 았/었더라면
# ══════════════════════════════════════════════════════════════════════
Q_PK78 = [
    # 1–5 tanish
    {
        "text": "<p><b>았/었더라면</b> nima haqida gapiradi?</p>",
        "choices": ["Boʻlmagan oʻtmish — tasavvur qilingan boshqa yoʻl",
                    "Kelajakdagi reja",
                    "Hozir davom etayotgan ish",
                    "Har kuni takrorlanadigan odat"],
        "correct": "Boʻlmagan oʻtmish — tasavvur qilingan boshqa yoʻl",
        "explanation": "<p>Oʻtmishni oʻzgartirib boʻlmaydi — faqat "
                       "tasavvur qilish mumkin.</p>",
    },
    {
        "text": "<p>Ichidagi <b>더</b> nimani bildiradi?</p>",
        "choices": ["Oʻsha paytga qaytib qarash",
                    "Koʻproq, ortiqroq",
                    "Inkor", "Hurmat"],
        "correct": "Oʻsha paytga qaytib qarash",
        "explanation": "<p>Shuning uchun 았/었더라면 sizni oʻtmishning "
                       "ichiga olib kiradi.</p>",
    },
    {
        "text": "<p>Ikkinchi gapda odatda nima keladi?</p>",
        "choices": ["았/었을 것이다 / 았/었을 거예요",
                    "Hozirgi zamon", "Buyruq shakli", "Soʻroq shakli"],
        "correct": "았/었을 것이다 / 았/었을 거예요",
        "explanation": "<p>Natija ham boʻlmagan — shuning uchun u ham "
                       "taxmin shaklida turadi.</p>",
    },
    {
        "text": "<p>Qaysi soʻz koʻpincha 았/었더라면 oldida turadi?</p>",
        "choices": ["만약 / 만일", "그래서", "하지만", "그런데"],
        "correct": "만약 / 만일",
        "explanation": "<p>“Agar” — gapning boshidayoq “bu faraz” deb "
                       "ogohlantiradi, xuddi oʻzbekchadagidek.</p>",
    },
    {
        "text": "<p>았/었더라면 faqat afsus bildiradimi?</p>",
        "choices": ["Yoʻq — inkor bilan shukr ham bildiradi",
                    "Ha, faqat afsus",
                    "Faqat quvonch bildiradi",
                    "Faqat gʻazab bildiradi"],
        "correct": "Yoʻq — inkor bilan shukr ham bildiradi",
        "explanation": "<p>조심하지 <b>않았더라면</b> 크게 다쳤을 거예요 — "
                       "“yaxshiyamki ehtiyot boʻlibman”.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 조금 더 일찍 <b>____</b> 기차를 탔을 "
                "거예요. (출발하다)</p>",
        "choices": ["출발했더라면", "출발하더라면", "출발할더라면",
                    "출발해더라면"],
        "correct": "출발했더라면",
        "explanation": "<p>Oʻtmish farazi — oldida <b>았/었</b> shart.</p>",
    },
    {
        "text": "<p>Toʻldiring: 돈이 <b>____</b> 그 집을 샀을 거예요. "
                "(있다)</p>",
        "choices": ["있었더라면", "있더라면", "있을더라면", "있으면"],
        "correct": "있었더라면",
        "explanation": "<p>있다 → oʻzak 있 → <b>있었더라면</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그때 한국어를 배웠더라면 지금 많이 "
                "<b>____</b>.</p>",
        "choices": ["편했을 거예요", "편해요", "편하세요", "편할 거예요"],
        "correct": "편했을 거예요",
        "explanation": "<p>Boʻlmagan natija — <b>았/었을 거예요</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 친구가 도와주지 <b>____</b> 저는 "
                "포기했을 거예요. (않다)</p>",
        "choices": ["않았더라면", "않더라면", "않으면", "않을더라면"],
        "correct": "않았더라면",
        "explanation": "<p>Shukr maʼnosi — birinchi gap inkorda va oʻtmish "
                       "shaklida.</p>",
    },
    {
        "text": "<p>“Oʻshanda u odamni uchratmaganimda edi, hayotim "
                "butunlay boshqacha boʻlardi” — koreyschada?</p>",
        "choices": ["만약 그때 그 사람을 만나지 않았더라면 제 인생은 완전히 "
                    "달랐을 거예요.",
                    "만약 그때 그 사람을 만나지 않으면 제 인생은 완전히 "
                    "다를 거예요.",
                    "만약 그때 그 사람을 만나더라면 제 인생은 완전히 "
                    "달라요.",
                    "만약 그때 그 사람을 만났더라면 제 인생은 완전히 "
                    "달라요."],
        "correct": "만약 그때 그 사람을 만나지 않았더라면 제 인생은 완전히 "
                   "달랐을 거예요.",
        "explanation": "<p>Ikkala qism ham oʻtmish shaklida: "
                       "<b>않았더라면</b> + <b>달랐을 거예요</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 조금만 늦었더라면 사고가 <b>____</b>. "
                "(나다 — “sal boʻlmasa sodir boʻlardi”)</p>",
        "choices": ["날 뻔했어요", "나요", "날 거예요", "났어요"],
        "correct": "날 뻔했어요",
        "explanation": "<p>PK-63 dagi <b>(으)ㄹ 뻔하다</b> — 았/었더라면 "
                       "bilan juda tabiiy ishlaydi.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "일찍 출발했더라면 기차를 탔을 거예요.</p>",
        "choices": ["일찍 출발했더라면 기차를 탔을 것이다.",
                    "일찍 출발했더라면 기차를 탄다.",
                    "일찍 출발했더라면 기차를 탔는다.",
                    "일찍 출발하더라면 기차를 탔을 것이다."],
        "correct": "일찍 출발했더라면 기차를 탔을 것이다.",
        "explanation": "<p>(으)ㄹ 거예요 → <b>(으)ㄹ 것이다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>(으)면</b> va <b>았/었더라면</b> farqi nima?</p>",
        "choices": ["(으)면 — haqiqiy shart, hali boʻlishi mumkin; "
                    "았/었더라면 — endi boʻlmaydigan faraz",
                    "(으)면 — rasmiy; 았/었더라면 — ogʻzaki",
                    "(으)면 — feʼl bilan; 았/었더라면 — ot bilan",
                    "Farqi yoʻq"],
        "correct": "(으)면 — haqiqiy shart, hali boʻlishi mumkin; "
                   "았/었더라면 — endi boʻlmaydigan faraz",
        "explanation": "<p>일찍 출발<b>하면</b> 기차를 탈 거예요 (hali imkon "
                       "bor) ↔ 일찍 출발<b>했더라면</b> (chiqmadim).</p>",
    },
    {
        "text": "<p><b>(으)ㄹ걸 그랬다</b> (PK-70) va <b>았/었더라면</b> "
                "farqi nima?</p>",
        "choices": ["걸 그랬다 — qisqa afsus, faqat oʻz ishim haqida; "
                    "았/었더라면 — boshqa yoʻl va uning natijasi",
                    "걸 그랬다 — kelajak; 았/었더라면 — hozir",
                    "걸 그랬다 — yozma; 았/었더라면 — ogʻzaki",
                    "Farqi yoʻq"],
        "correct": "걸 그랬다 — qisqa afsus, faqat oʻz ishim haqida; "
                   "았/었더라면 — boshqa yoʻl va uning natijasi",
        "explanation": "<p>았/었더라면 <b>toʻliq tasavvur</b> beradi va "
                       "boshqa odam haqida ham boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Bu gap afsusmi yoki shukr? "
                "그때 조심하지 않았더라면 크게 다쳤을 거예요.</p>",
        "choices": ["Shukr — ehtiyot boʻlgan va omon qolgan",
                    "Afsus — ehtiyot boʻlmagan",
                    "Ogohlantirish",
                    "Buyruq"],
        "correct": "Shukr — ehtiyot boʻlgan va omon qolgan",
        "explanation": "<p>“Ehtiyot boʻlmaganimda edi jarohat olardim” — "
                       "demak boʻlgan. Inkor bu maʼnoni beradi.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["내일 비가 왔더라면 안 갈 거예요.",
                    "돈이 있었더라면 그 집을 샀을 거예요.",
                    "일찍 출발했더라면 기차를 탔을 거예요.",
                    "친구가 도와주지 않았더라면 포기했을 거예요."],
        "correct": "내일 비가 왔더라면 안 갈 거예요.",
        "explanation": "<p>내일 — <b>kelajak</b>. Teskari faraz emas, "
                       "oddiy shart: <b>비가 오면</b>.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>일찍 출발하더라면 기차를 탔을 "
                "거예요.</s></p>",
        "choices": ["Oʻtmish farazi uchun 았/었 shart — 출발했더라면",
                    "기차를 emas, 기차가",
                    "탔을 거예요 emas, 타요",
                    "일찍 emas, 빨리"],
        "correct": "Oʻtmish farazi uchun 았/었 shart — 출발했더라면",
        "explanation": "<p>더라면 ning oʻzi yetarli emas — oldida oʻtgan "
                       "zamon boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>돈이 있었더라면 그 집을 사요.</s></p>",
        "choices": ["Ikkinchi gap ham boʻlmagan natija — 샀을 거예요",
                    "돈이 emas, 돈을",
                    "있었더라면 emas, 있으면",
                    "그 집을 emas, 그 집이"],
        "correct": "Ikkinchi gap ham boʻlmagan natija — 샀을 거예요",
        "explanation": "<p>Hozirgi zamon 았/었더라면 bilan mos "
                       "kelmaydi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Pulim boʻlganida edi, oʻsha uyni sotib olardim” — "
                "koreyschada?</p>",
        "choices": ["돈이 있었더라면 그 집을 샀을 거예요.",
                    "돈이 있으면 그 집을 살 거예요.",
                    "돈이 있었더라면 그 집을 사요.",
                    "돈이 있더라면 그 집을 샀어요."],
        "correct": "돈이 있었더라면 그 집을 샀을 거예요.",
        "explanation": "<p>Ikki qism ham oʻtmish shaklida — pul ham "
                       "boʻlmagan, uy ham olinmagan.</p>",
    },
    {
        "text": "<p>“Oʻshanda koreyscha oʻrganganimda edi, hozir ancha "
                "qulay boʻlardi” — koreyschada?</p>",
        "choices": ["그때 한국어를 배웠더라면 지금 많이 편했을 거예요.",
                    "그때 한국어를 배우면 지금 많이 편해요.",
                    "그때 한국어를 배웠더라면 지금 많이 편해요.",
                    "그때 한국어를 배우더라면 지금 편할 거예요."],
        "correct": "그때 한국어를 배웠더라면 지금 많이 편했을 거예요.",
        "explanation": "<p>“Hozir” soʻzi boʻlsa ham natija boʻlmagan — "
                       "shuning uchun <b>편했을 거예요</b>.</p>",
    },
]


# ══════════════════════════════════════════════════════════════════════
# PK-79 — 다가는
# ══════════════════════════════════════════════════════════════════════
Q_PK79 = [
    # 1–5 tanish
    {
        "text": "<p><b>다가는</b> qanday maʼno beradi?</p>",
        "choices": ["Shunday qilaversang, (yomon narsa) boʻladi",
                    "…ishi bilanoq", "…gan boʻlganimda edi",
                    "…ib boʻlgach"],
        "correct": "Shunday qilaversang, (yomon narsa) boʻladi",
        "explanation": "<p>Ogohlantirish qolipi. Hozir davom etayotgan "
                       "ishning yomon oxirini aytadi.</p>",
    },
    {
        "text": "<p>다가는 dan keyingi natija qanday boʻladi?</p>",
        "choices": ["Doim yomon", "Doim yaxshi",
                    "Yaxshi ham, yomon ham", "Betaraf"],
        "correct": "Doim yomon",
        "explanation": "<p>❌ 열심히 하다가는 성공할 거예요 — yaxshi natija "
                       "uchun <b>다가 보면</b> (PK-77).</p>",
    },
    {
        "text": "<p>다가는 oldida qaysi soʻzlar koʻp uchraydi?</p>",
        "choices": ["이렇게 / 그렇게 / 계속", "만약 / 만일",
                    "아마 / 혹시", "제일 / 가장"],
        "correct": "이렇게 / 그렇게 / 계속",
        "explanation": "<p>Chunki 다가는 <b>hozir davom etayotgan</b> ish "
                       "haqida — “ana shunday qilishda davom etsang”.</p>",
    },
    {
        "text": "<p>다가는 ning ikkinchi gapida nima keladi?</p>",
        "choices": ["Kelajak yoki taxmin: (으)ㄹ 거예요 · 기 십상이다",
                    "Oʻtgan zamon",
                    "Buyruq shakli",
                    "Hozirgi zamon"],
        "correct": "Kelajak yoki taxmin: (으)ㄹ 거예요 · 기 십상이다",
        "explanation": "<p>Natija hali <b>boʻlmagan</b> — u ogohlantirish "
                       "uchun aytilyapti.</p>",
    },
    {
        "text": "<p>다가는 kimga aytilmasligi maʼqul?</p>",
        "choices": ["Oʻzidan katta odamga — ustozga yoki boshliqqa",
                    "Doʻstga", "Ukasiga", "Oʻziga"],
        "correct": "Oʻzidan katta odamga — ustozga yoki boshliqqa",
        "explanation": "<p>Ohangida “men sizni ogohlantiryapman” degan "
                       "maʼno bor — kattaga gap qaytargandek eshitiladi.</p>",
    },
    # 6–12 qoʻllash
    {
        "text": "<p>Toʻldiring: 그렇게 <b>____</b> 시험에 떨어질 거예요. "
                "(놀다)</p>",
        "choices": ["놀다가는", "놀았다가는", "논다가는", "놀더라면"],
        "correct": "놀다가는",
        "explanation": "<p>Oʻzak + 다가는, zamon yoʻq.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이렇게 계속 <b>____</b> 살이 찔 거예요. "
                "(먹다)</p>",
        "choices": ["먹다가는", "먹었다가는", "먹으면서", "먹다가 보니"],
        "correct": "먹다가는",
        "explanation": "<p>Hozirgi odat + yomon natija — <b>다가는</b>.</p>",
    },
    {
        "text": "<p>Toʻldiring: 밤늦게까지 일하다가는 건강을 <b>____</b>.</p>",
        "choices": ["잃기 십상이에요", "잃었어요", "잃으세요", "잃어요"],
        "correct": "잃기 십상이에요",
        "explanation": "<p>PK-73 dagi <b>기 십상이다</b> — 다가는 ning eng "
                       "tabiiy sherigi.</p>",
    },
    {
        "text": "<p>Toʻldiring: 이렇게 얇게 <b>____</b> 감기에 걸릴 "
                "거예요. (입다)</p>",
        "choices": ["입다가는", "입었다가는", "입더라면", "입고 나서"],
        "correct": "입다가는",
        "explanation": "<p>Yupqa kiyinish davom etyapti — ogohlantirish "
                       "qolipi.</p>",
    },
    {
        "text": "<p>“Shunday shoshaversangiz, xato qilasiz” — "
                "koreyschada?</p>",
        "choices": ["그렇게 서두르다가는 실수할 거예요.",
                    "그렇게 서두르다가 보면 실수할 거예요.",
                    "그렇게 서둘렀더라면 실수했을 거예요.",
                    "그렇게 서두르자마자 실수할 거예요."],
        "correct": "그렇게 서두르다가는 실수할 거예요.",
        "explanation": "<p>Aynan shu odamga, hozir shoshayotgani uchun "
                       "aytilgan ogohlantirish.</p>",
    },
    {
        "text": "<p>Toʻldiring: 그렇게 스마트폰만 보다가는 눈이 "
                "<b>____</b>.</p>",
        "choices": ["나빠질 거예요", "나빠졌어요", "나쁘세요", "나빠요"],
        "correct": "나빠질 거예요",
        "explanation": "<p>Natija hali boʻlmagan — kelajak shakli.</p>",
    },
    {
        "text": "<p>Bu gapni 한다체 ga oʻgiring (PK-74): "
                "그렇게 놀다가는 시험에 떨어질 거예요.</p>",
        "choices": ["그렇게 놀다가는 시험에 떨어질 것이다.",
                    "그렇게 놀다가는 시험에 떨어진다.",
                    "그렇게 놀다가는 시험에 떨어졌다.",
                    "그렇게 놀다가는 시험에 떨어질 거다예요."],
        "correct": "그렇게 놀다가는 시험에 떨어질 것이다.",
        "explanation": "<p>(으)ㄹ 거예요 → <b>(으)ㄹ 것이다</b>.</p>",
    },
    # 13–16 farqlash
    {
        "text": "<p><b>다가 보면</b> (PK-77) va <b>다가는</b> farqi nima?</p>",
        "choices": ["보면 — dalda, natija yaxshi; 다가는 — ogohlantirish, "
                    "natija yomon",
                    "보면 — oʻtgan zamon; 다가는 — kelasi zamon",
                    "보면 — feʼl bilan; 다가는 — sifat bilan",
                    "Farqi yoʻq"],
        "correct": "보면 — dalda, natija yaxshi; 다가는 — ogohlantirish, "
                   "natija yomon",
        "explanation": "<p>Ikkalasining ichida ham 다가 bor — farq faqat "
                       "oxirida va natijaning ohangida.</p>",
    },
    {
        "text": "<p>“서두르면 실수하기 십상이에요” va “그렇게 서두르다가는 "
                "실수할 거예요” — farqi nima?</p>",
        "choices": ["Birinchisi — umumiy haqiqat; ikkinchisi — aynan shu "
                    "odamga, hozir",
                    "Birinchisi — kelajak; ikkinchisi — oʻtmish",
                    "Birinchisi — ogʻzaki; ikkinchisi — yozma",
                    "Farqi yoʻq"],
        "correct": "Birinchisi — umumiy haqiqat; ikkinchisi — aynan shu "
                   "odamga, hozir",
        "explanation": "<p>기 십상이다 kim uchun ham amal qiladi; 다가는 esa "
                       "<b>ayni shu odamning hozirgi ishi</b> haqida.</p>",
    },
    {
        "text": "<p>Qaysi jumla notoʻgʻri?</p>",
        "choices": ["열심히 공부하다가는 시험에 붙을 거예요.",
                    "그렇게 놀다가는 시험에 떨어질 거예요.",
                    "이렇게 먹다가는 살이 찔 거예요.",
                    "밤늦게까지 일하다가는 건강을 잃을 거예요."],
        "correct": "열심히 공부하다가는 시험에 붙을 거예요.",
        "explanation": "<p>Natija <b>yaxshi</b> — demak <b>다가 보면</b> "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>Nega 다가는 oldida zamon boʻlmaydi?</p>",
        "choices": ["Chunki ish hozir davom etyapti — u tugagan emas",
                    "Chunki 다가는 faqat kelajak haqida",
                    "Chunki 는 zamonni bekor qiladi",
                    "Chunki natija salbiy"],
        "correct": "Chunki ish hozir davom etyapti — u tugagan emas",
        "explanation": "<p>❌ 그렇게 놀았다가는 — ogohlantirish ish "
                       "<b>hali toʻxtamaganda</b> aytiladi.</p>",
    },
    # 17–18 xato topish
    {
        "text": "<p>Xatoni toping: <s>이렇게 먹다가는 살이 쪘어요.</s></p>",
        "choices": ["Natija hali boʻlmagan — 살이 찔 거예요",
                    "먹다가는 emas, 먹었다가는",
                    "이렇게 emas, 그렇게",
                    "살이 emas, 살을"],
        "correct": "Natija hali boʻlmagan — 살이 찔 거예요",
        "explanation": "<p>다가는 ogohlantirish — natija kelajakda.</p>",
    },
    {
        "text": "<p>Xatoni toping: <s>날씨가 춥다가는 감기에 걸릴 "
                "거예요.</s></p>",
        "choices": ["다가는 faqat feʼl bilan va odamning oʻz ishi haqida — "
                    "masalan 얇게 입다가는",
                    "감기에 emas, 감기를",
                    "걸릴 거예요 emas, 걸려요",
                    "날씨가 emas, 날씨는"],
        "correct": "다가는 faqat feʼl bilan va odamning oʻz ishi haqida — "
                   "masalan 얇게 입다가는",
        "explanation": "<p>춥다 — sifat, va ob-havo odamning ishi emas. "
                       "Ogohlantirish odam <b>toʻxtata oladigan</b> ish "
                       "haqida boʻladi.</p>",
    },
    # 19–20 tuzish
    {
        "text": "<p>“Tungacha ishlayversangiz, sogʻligingizni yoʻqotib "
                "qoʻyishingiz turgan gap” — koreyschada?</p>",
        "choices": ["밤늦게까지 일하다가는 건강을 잃기 십상이에요.",
                    "밤늦게까지 일하다가 보면 건강을 잃기 십상이에요.",
                    "밤늦게까지 일했더라면 건강을 잃었을 거예요.",
                    "밤늦게까지 일하자마자 건강을 잃을 거예요."],
        "correct": "밤늦게까지 일하다가는 건강을 잃기 십상이에요.",
        "explanation": "<p>다가는 + 기 십상이다 — ogohlantirishning eng "
                       "kuchli juftligi.</p>",
    },
    {
        "text": "<p>“Shunday telefonga tikilaversangiz, koʻzingiz "
                "yomonlashadi” — koreyschada?</p>",
        "choices": ["그렇게 스마트폰만 보다가는 눈이 나빠질 거예요.",
                    "그렇게 스마트폰만 보다가 보니 눈이 나빠졌어요.",
                    "그렇게 스마트폰만 봤더라면 눈이 나빠졌을 거예요.",
                    "그렇게 스마트폰만 보는 김에 눈이 나빠질 거예요."],
        "correct": "그렇게 스마트폰만 보다가는 눈이 나빠질 거예요.",
        "explanation": "<p>Hozir davom etayotgan ish + hali boʻlmagan "
                       "yomon natija.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PK-77 Mashq: 다가 · 다가 보면 · 다가 보니",
        "description": "20 savol — ishning uzilishi, 았/었다가 bilan "
                       "orqaga qaytish, kelajak natija (보면) va "
                       "oʻtmishdagi kashfiyot (보니).",
        "tutorial":    "PK-77:",
        "level":       "medium",
        "questions":   Q_PK77,
    },
    {
        "title":       "PK-78 Mashq: 았/었더라면",
        "description": "20 savol — teskari faraz, ikkinchi gapdagi "
                       "았/었을 것이다, (으)면 dan farqi, inkor bilan "
                       "shukr maʼnosi.",
        "tutorial":    "PK-78:",
        "level":       "medium",
        "questions":   Q_PK78,
    },
    {
        "title":       "PK-79 Mashq: 다가는",
        "description": "20 savol — ogohlantirish qolipi, majburiy salbiy "
                       "natija, 다가 보면 dan farqi va 기 십상이다 bilan "
                       "juftligi.",
        "tutorial":    "PK-79:",
        "level":       "medium",
        "questions":   Q_PK79,
    },
]
