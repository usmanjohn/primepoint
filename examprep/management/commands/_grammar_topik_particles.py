# -*- coding: utf-8 -*-
"""Grammar bank — 조사 (particles): kelishik va yuklama qo'shimchalari.

Order decade: 100-199. See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── Kelishik qo'shimchalari ────────────────────────────────────────────
    {
        "pattern":   "이/가",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "bosh kelishik — kim? nima? (yangi yoki ta'kidlangan ega)",
        "attach":    "명사 + 이/가",
        "form_rule": "받침 bor → <b>이</b> (선생님<b>이</b>) · 받침 yo'q → <b>가</b> (친구<b>가</b>)"
                     "<br>Olmoshlar o'zgaradi: 나 → <b>내가</b>, 저 → <b>제가</b>, 너 → <b>네가</b>, 누구 → <b>누가</b>",
        "note":      "<p>Gapga <b>yangi kirgan</b> yoki <b>aynan shu</b> deb ta'kidlanayotgan egani ko'rsatadi. "
                     "So'roqqa javob bo'lganda ham 이/가 keladi: <i>누가 왔어요? — 아프소나<b>가</b> 왔어요.</i></p>"
                     "<p>Ayrim fe'l va sifatlar doim 이/가 ni talab qiladi: 되다, 아니다, 있다/없다, "
                     "필요하다, 좋다, 싫다.</p>",
        "mistake":   "<p>❌ 저는 김치는 좋아요 → ✅ 저는 김치<b>가</b> 좋아요.<br>"
                     "«좋다» (yoqadi) sifat — yoqayotgan narsa <b>ega</b> bo'ladi, 을/를 emas.</p>",
        "examples": [
            ("아프소나가 한국어를 배워요.", "Afsona koreys tilini o'rganadi."),
            ("누가 이 편지를 썼어요?", "Bu xatni kim yozdi?"),
            ("저는 시간이 없어요.", "Mening vaqtim yo'q."),
        ],
        "synonyms": [
            ("은/는", "은/는 = mavzu (allaqachon ma'lum, taqqoslash); 이/가 = yangi ma'lumot, «aynan kim»"),
        ],
        "order": 100,
    },
    {
        "pattern":   "은/는",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "mavzu qo'shimchasi — «-ga kelsak», taqqoslash va ta'kid",
        "attach":    "명사 + 은/는",
        "form_rule": "받침 bor → <b>은</b> (선생님<b>은</b>) · 받침 yo'q → <b>는</b> (저<b>는</b>)",
        "note":      "<p>Uch vazifasi bor:</p><ul>"
                     "<li><b>Mavzu</b> — gap nima haqida: <i>저<b>는</b> 학생이에요.</i></li>"
                     "<li><b>Taqqoslash</b> — <i>커피<b>는</b> 좋아하지만 차<b>는</b> 안 좋아해요.</i></li>"
                     "<li><b>Ta'kid</b> — boshqa kelishiklar ustiga ham qo'shiladi: 학교에<b>는</b>, 친구하고<b>는</b>.</li>"
                     "</ul>",
        "mistake":   "<p>❌ 누가 왔어요? — 아프소나<b>는</b> 왔어요.<br>"
                     "✅ 아프소나<b>가</b> 왔어요. So'roqning javobi = yangi ma'lumot = 이/가.</p>",
        "examples": [
            ("저는 우즈베키스탄 사람이에요.", "Men o'zbekistonlikman."),
            ("여름에는 덥고 겨울에는 추워요.", "Yozda issiq, qishda esa sovuq."),
            ("한국어는 어렵지만 재미있어요.", "Koreys tili qiyin, lekin qiziqarli."),
        ],
        "synonyms": [
            ("이/가", "이/가 = yangi/aniq ega; 은/는 = ma'lum mavzu yoki taqqoslash"),
            ("도", "도 = «ham» qo'shadi; 는 = ajratib taqqoslaydi"),
        ],
        "order": 101,
    },
    {
        "pattern":   "을/를",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "tushum kelishigi — kimni? nimani?",
        "attach":    "명사 + 을/를",
        "form_rule": "받침 bor → <b>을</b> (밥<b>을</b>) · 받침 yo'q → <b>를</b> (커피<b>를</b>)"
                     "<br>Og'zaki nutqda 를 → <b>ㄹ</b> qisqaradi: 커피<b>를</b> → 커<b>필</b>.",
        "note":      "<p>O'timli fe'l (타동사) ning to'ldiruvchisi. Ba'zi harakat fe'llari bilan "
                     "yo'nalish ham 을/를 oladi: 산<b>을</b> 오르다, 길<b>을</b> 건너다, 비행기를 타다.</p>",
        "mistake":   "<p>❌ 친구를 만나<b>러</b> 가요 to'g'ri, lekin ❌ 친구<b>에게</b> 만나요 xato → "
                     "✅ 친구<b>를</b> 만나요. «만나다» 을/를 talab qiladi.</p>",
        "examples": [
            ("자수르가 책을 읽어요.", "Jasur kitob o'qiyapti."),
            ("매일 아침 커피를 마셔요.", "Har kuni ertalab qahva ichaman."),
            ("친구를 만나러 갔어요.", "Do'stim bilan uchrashgani bordim."),
        ],
        "synonyms": [
            ("이/가", "이/가 = harakatni bajaruvchi; 을/를 = harakat tushayotgan narsa"),
        ],
        "order": 102,
    },
    {
        "pattern":   "의",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      2,
        "meaning":   "qaratqich kelishigi — kimning? nimaning?",
        "attach":    "명사 + 의 + 명사",
        "form_rule": "Talaffuzi ko'pincha [에]. Og'zaki nutqda 나의 → <b>내</b>, 저의 → <b>제</b>, "
                     "너의 → <b>네</b>.",
        "note":      "<p>Yozma va rasmiy uslubda ko'p, og'zakida esa ko'pincha <b>tushirib qoldiriladi</b>: "
                     "<i>친구의 집</i> ≈ <i>친구 집</i>. TOPIK 읽기/쓰기 da qoladi: "
                     "<i>한국<b>의</b> 경제, 사회<b>의</b> 변화</i>.</p>",
        "examples": [
            ("이것은 셰르베크의 가방이에요.", "Bu — Sherbekning sumkasi."),
            ("한국의 전통 음식을 소개하겠습니다.", "Koreyaning an'anaviy taomlarini tanishtiraman."),
        ],
        "synonyms": [],
        "order": 103,
    },
    {
        "pattern":   "에",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "joy/vaqt — «-da, -ga» (harakatsiz joy, yo'nalish, vaqt)",
        "attach":    "명사 + 에",
        "form_rule": "받침 dan qat'i nazar bir xil.",
        "note":      "<p>Uch asosiy vazifa:</p><ul>"
                     "<li><b>Manzil</b> (borish/kelish): 학교<b>에</b> 가요.</li>"
                     "<li><b>Turgan joy</b> (있다/없다/살다 bilan): 집<b>에</b> 있어요.</li>"
                     "<li><b>Vaqt</b>: 세 시<b>에</b>, 월요일<b>에</b>, 아침<b>에</b>.</li></ul>"
                     "<p>⚠️ 오늘, 어제, 내일, 지금, 매일 bilan 에 <b>qo'shilmaydi</b>.</p>",
        "mistake":   "<p>❌ 도서관<b>에</b> 공부해요 → ✅ 도서관<b>에서</b> 공부해요.<br>"
                     "Harakat (공부하다) sodir bo'ladigan joy — 에서.</p>",
        "examples": [
            ("일곱 시에 학교에 가요.", "Soat yettida maktabga boraman."),
            ("책상 위에 사전이 있어요.", "Stol ustida lug'at bor."),
        ],
        "synonyms": [
            ("에서", "에서 = harakat BAJARILAYOTGAN joy va boshlanish nuqtasi; 에 = manzil, turgan joy, vaqt"),
            ("에게/한테", "jonli obyekt (odam/hayvon) uchun 에게/한테, jonsiz uchun 에"),
        ],
        "order": 104,
    },
    {
        "pattern":   "에서",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "harakat joyi va boshlanish nuqtasi — «-da, -dan»",
        "attach":    "명사 + 에서",
        "form_rule": "Og'zaki nutqda 에서 → <b>서</b> qisqarishi mumkin: 어디<b>서</b> 왔어요?",
        "note":      "<p>Ikki vazifa:</p><ul>"
                     "<li><b>Harakat joyi</b>: 식당<b>에서</b> 밥을 먹어요.</li>"
                     "<li><b>Boshlanish nuqtasi</b>: 우즈베키스탄<b>에서</b> 왔어요. "
                     "부산<b>에서</b> 서울<b>까지</b>.</li></ul>",
        "examples": [
            ("도서관에서 시험공부를 했어요.", "Kutubxonada imtihonga tayyorlandim."),
            ("타슈켄트에서 서울까지 일곱 시간 걸려요.", "Toshkentdan Seulgacha yetti soat ketadi."),
        ],
        "synonyms": [
            ("에", "에 = manzil/turgan joy; 에서 = harakat bajarilayotgan joy"),
            ("부터", "부터 = asosan VAQT boshlanishi; 에서 = asosan JOY boshlanishi"),
        ],
        "order": 105,
    },
    {
        "pattern":   "에게/한테/께",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "jo'nalish kelishigi — kimga? (jonli obyekt)",
        "attach":    "사람/동물 + 에게 / 한테 / 께",
        "form_rule": "<b>에게</b> = yozma, rasmiy · <b>한테</b> = og'zaki · <b>께</b> = hurmat "
                     "(선생님<b>께</b> 드렸어요)",
        "note":      "<p>Teskari yo'nalish uchun <b>에게서 / 한테서</b> («kimdan»): "
                     "<i>친구<b>한테서</b> 편지를 받았어요.</i></p>"
                     "<p>Jonsiz narsalar uchun 에게 emas, <b>에</b> ishlatiladi: 회사<b>에</b> 전화했어요.</p>",
        "mistake":   "<p>❌ 학교<b>에게</b> 편지를 보냈어요 → ✅ 학교<b>에</b> 편지를 보냈어요. "
                     "Maktab — jonsiz obyekt.</p>",
        "examples": [
            ("동생에게 선물을 줬어요.", "Ukamga sovg'a berdim."),
            ("선생님께 이메일을 보냈습니다.", "Ustozga elektron xat yubordim."),
        ],
        "synonyms": [
            ("에", "jonsiz obyekt (회사, 학교) uchun 에게 emas — 에"),
        ],
        "order": 106,
    },
    {
        "pattern":   "(으)로",
        "category":  "particle",
        "function":  "case",
        "level":     1,
        "freq":      3,
        "meaning":   "vosita/yo'nalish/material — «bilan, tomon, -dan»",
        "attach":    "명사 + (으)로",
        "form_rule": "받침 yo'q yoki ㄹ 받침 → <b>로</b> (버스<b>로</b>, 지하철<b>로</b>) · "
                     "boshqa 받침 → <b>으로</b> (손<b>으로</b>)",
        "note":      "<p>Vazifalari: <b>vosita</b> (버스<b>로</b> 가요 — avtobusda), "
                     "<b>yo'nalish</b> (오른쪽<b>으로</b> 가세요 — o'ngga), "
                     "<b>material</b> (나무<b>로</b> 만들었어요 — yog'ochdan), "
                     "<b>sabab</b> (병<b>으로</b> 결석했어요 — kasallik tufayli), "
                     "<b>sifat/rol</b> (선물<b>로</b> 샀어요 — sovg'a sifatida).</p>",
        "examples": [
            ("학교까지 자전거로 가요.", "Maktabgacha velosipedda boraman."),
            ("이 빵은 쌀로 만들어요.", "Bu non guruchdan tayyorlanadi."),
            ("한국어로 이야기합시다.", "Koreyscha gaplashaylik."),
        ],
        "synonyms": [
            ("에", "에 = aniq manzil (학교에 가요); (으)로 = umumiy yo'nalish (학교 쪽으로)"),
            ("로서/로써", "로서 = maqom («sifatida»), 로써 = vosita — ikkalasi ham rasmiy uslub"),
        ],
        "order": 107,
    },
    {
        "pattern":   "과/와, 하고, (이)랑",
        "category":  "particle",
        "function":  "listing",
        "level":     1,
        "freq":      3,
        "meaning":   "«va, bilan» — sanash va birgalik",
        "attach":    "명사 + 과/와 · 명사 + 하고 · 명사 + (이)랑",
        "form_rule": "<b>과</b> (받침 bor) / <b>와</b> (받침 yo'q) = yozma, rasmiy · "
                     "<b>하고</b> = neytral og'zaki · <b>(이)랑</b> = erkin, do'stona",
        "note":      "<p>Ikki ma'no: <b>sanash</b> (빵<b>과</b> 우유 — non va sut) va "
                     "<b>birgalik</b> (친구<b>와</b> 같이 — do'st bilan birga). "
                     "Birgalik ma'nosida ko'pincha 같이 / 함께 qo'shiladi.</p>"
                     "<p>쓰기 54 inshosida <b>과/와</b> ishlating — 하고/랑 og'zaki uslub.</p>",
        "examples": [
            ("사과와 바나나를 샀어요.", "Olma va banan sotib oldim."),
            ("친구하고 영화를 봤어요.", "Do'stim bilan kino ko'rdim."),
        ],
        "synonyms": [
            ("(이)나", "(이)나 = «yoki» (tanlov); 과/와 = «va» (qo'shish)"),
        ],
        "order": 108,
    },

    # ── Yuklamalar ─────────────────────────────────────────────────────────
    {
        "pattern":   "도",
        "category":  "particle",
        "function":  "listing",
        "level":     1,
        "freq":      3,
        "meaning":   "«ham, -da» — qo'shish",
        "attach":    "명사 + 도",
        "form_rule": "이/가 va 을/를 ni <b>almashtiradi</b> (❌ 저는도, ❌ 밥을도), lekin "
                     "에, 에서, 한테 ustiga <b>qo'shiladi</b>: 학교에<b>도</b>, 집에서<b>도</b>.",
        "note":      "<p>Inkor bilan «hatto ... ham emas» ma'nosini beradi: "
                     "<i>물<b>도</b> 안 마셨어요</i> — suv ham ichmadim.</p>",
        "mistake":   "<p>❌ 저<b>는도</b> 갈래요 → ✅ 저<b>도</b> 갈래요.</p>",
        "examples": [
            ("저도 한국에 가고 싶어요.", "Men ham Koreyaga bormoqchiman."),
            ("어제도 오늘도 비가 와요.", "Kecha ham, bugun ham yomg'ir yog'yapti."),
        ],
        "synonyms": [
            ("만", "만 = «faqat» (chegaralaydi); 도 = «ham» (qo'shadi) — bir-biriga qarama-qarshi"),
            ("까지", "까지 = «hatto ...gacha» (kutilmagan darajada); 도 = oddiy qo'shish"),
        ],
        "order": 110,
    },
    {
        "pattern":   "만",
        "category":  "particle",
        "function":  "degree",
        "level":     1,
        "freq":      3,
        "meaning":   "«faqat, -gina»",
        "attach":    "명사 + 만",
        "form_rule": "이/가, 을/를 o'rniga keladi yoki ulardan oldin: 이것<b>만</b> / 이것<b>만을</b>. "
                     "Boshqa kelishiklar ustiga qo'shiladi: 여기에<b>만</b>.",
        "note":      "<p>Fe'lga qo'shilsa <b>-기만 하다</b> shakli chiqadi: "
                     "<i>울<b>기만 해요</b></i> — faqat yig'laydi (boshqa hech narsa qilmaydi).</p>",
        "examples": [
            ("저는 물만 마셔요.", "Men faqat suv ichaman."),
            ("한 번만 더 설명해 주세요.", "Yana bir marta tushuntirib bering."),
        ],
        "synonyms": [
            ("밖에", "밖에 doim INKOR bilan: 물밖에 안 마셔요 = 물만 마셔요 (ma'no bir xil, shakl har xil)"),
            ("도", "도 = qo'shish, 만 = chegaralash"),
        ],
        "order": 111,
    },
    {
        "pattern":   "밖에",
        "category":  "particle",
        "function":  "degree",
        "level":     2,
        "freq":      3,
        "meaning":   "«-dan boshqa emas, faqat» — doim inkor bilan",
        "attach":    "명사 + 밖에 + 부정 (안/못/없다)",
        "form_rule": "Keyingi fe'l <b>albatta inkor</b> bo'ladi: 밖에 + 안 / 못 / 없다 / 모르다.",
        "note":      "<p>Ma'nosi 만 bilan bir xil, lekin <b>ozlik, kamlik</b> tuyg'usini beradi: "
                     "<i>천 원<b>밖에</b> 없어요</i> — atigi ming vono bor (kam!).</p>",
        "mistake":   "<p>❌ 물밖에 마셔요 → ✅ 물<b>밖에</b> 안 마셔요. Inkorsiz ishlatilmaydi.</p>",
        "examples": [
            ("시간이 십 분밖에 없어요.", "Bor-yo'g'i o'n daqiqa vaqt bor."),
            ("한국어를 조금밖에 못해요.", "Koreyschani ozgina bilaman, xolos."),
        ],
        "synonyms": [
            ("만", "만 — neytral «faqat», ijobiy gap bilan; 밖에 — «atigi», doim inkor bilan"),
        ],
        "order": 112,
    },
    {
        "pattern":   "부터 ~ 까지",
        "category":  "particle",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "meaning":   "«-dan ... -gacha» — oraliq",
        "attach":    "명사 + 부터 · 명사 + 까지",
        "form_rule": "<b>부터</b> = boshlanish (asosan vaqt) · <b>까지</b> = tugash (vaqt va joy)."
                     "<br>Joy boshlanishi uchun 부터 emas, <b>에서</b>: 서울<b>에서</b> 부산<b>까지</b>.",
        "note":      "<p>까지 yolg'iz kelganda «hatto» ma'nosi ham bor: "
                     "<i>아이<b>까지</b> 알아요</i> — hatto bola ham biladi.</p>",
        "examples": [
            ("아홉 시부터 여섯 시까지 일해요.", "Soat to'qqizdan oltigacha ishlayman."),
            ("타슈켄트에서 사마르칸트까지 기차로 갔어요.", "Toshkentdan Samarqandgacha poyezdda bordim."),
        ],
        "synonyms": [
            ("에서", "joy uchun boshlanish = 에서, vaqt uchun = 부터"),
            ("동안", "동안 = davomiylik («2 soat davomida»); 부터~까지 = chegaralar"),
        ],
        "order": 113,
    },
    {
        "pattern":   "마다",
        "category":  "particle",
        "function":  "time",
        "level":     2,
        "freq":      2,
        "meaning":   "«har» — takrorlanish",
        "attach":    "명사 + 마다",
        "form_rule": "Vaqt bilan ham, sanaladigan otlar bilan ham: 날<b>마다</b>, 사람<b>마다</b>, "
                     "삼 년<b>마다</b>.",
        "note":      "<p>매 (每) bilan yaqin: 매일 = 날마다, 매주 = 주마다. "
                     "Lekin 마다 «har biri har xil» ma'nosini ham beradi: "
                     "<i>사람<b>마다</b> 생각이 다르다</i> — har kimning fikri har xil.</p>",
        "examples": [
            ("주말마다 도서관에 가요.", "Har dam olish kuni kutubxonaga boraman."),
            ("나라마다 문화가 다릅니다.", "Har bir mamlakatning madaniyati har xil."),
        ],
        "synonyms": [
            ("(으)ㄹ 때마다", "(으)ㄹ 때마다 fe'lga qo'shiladi («har safar ...ganda»); 마다 otga qo'shiladi"),
        ],
        "order": 114,
    },
    {
        "pattern":   "(이)나",
        "category":  "particle",
        "function":  "choice",
        "level":     2,
        "freq":      2,
        "meaning":   "«yoki»; miqdor bilan «-tacha, ancha»",
        "attach":    "명사 + (이)나",
        "form_rule": "받침 bor → <b>이나</b> · 받침 yo'q → <b>나</b>",
        "note":      "<p>Uch ma'no:</p><ul>"
                     "<li><b>Tanlov</b>: 커피<b>나</b> 차를 마셔요 — qahva yoki choy.</li>"
                     "<li><b>Ko'plik ta'kidi</b> (kutilganidan ko'p): 세 시간<b>이나</b> 기다렸어요 — "
                     "uch soat<b>cha</b> kutdim (juda ko'p!).</li>"
                     "<li><b>Iloji boricha</b>: 라면<b>이나</b> 먹을까요? — hech bo'lmasa ramyon yeymizmi?</li></ul>",
        "examples": [
            ("주스나 물을 주세요.", "Sharbat yoki suv bering."),
            ("책을 열 권이나 읽었어요.", "O'ntagacha kitob o'qidim (juda ko'p)."),
        ],
        "synonyms": [
            ("거나", "거나 = FE'L bilan «yoki» (가거나 오거나); (이)나 = OT bilan"),
            ("아니면", "아니면 = gaplar orasida «aks holda / yoki»; (이)나 = ot orasida"),
        ],
        "order": 115,
    },
    {
        "pattern":   "처럼 / 같이",
        "category":  "particle",
        "function":  "comparison",
        "level":     2,
        "freq":      2,
        "meaning":   "«-dek, kabi» — o'xshatish",
        "attach":    "명사 + 처럼 / 같이",
        "form_rule": "Ikkalasi ham bir xil ishlaydi; <b>처럼</b> yozma nutqda ko'proq.",
        "note":      "<p>«같은 + 명사» shakli otni aniqlaydi: <i>아이<b>같은</b> 얼굴</i> — bolanikidek yuz. "
                     "«처럼» esa fe'l/sifatni aniqlaydi: <i>아이<b>처럼</b> 웃어요</i>.</p>",
        "examples": [
            ("아프소나는 가수처럼 노래해요.", "Afsona xonandadek kuylaydi."),
            ("눈이 솜같이 하얘요.", "Qor paxtadek oppoq."),
        ],
        "synonyms": [
            ("만큼", "만큼 = «shu darajada, xuddi shuncha» (miqdor tengligi); 처럼 = «-dek» (o'xshashlik)"),
            ("보다", "보다 = taqqoslashda farq («-dan ko'ra»); 처럼 = o'xshashlik"),
        ],
        "order": 116,
    },
    {
        "pattern":   "보다",
        "category":  "particle",
        "function":  "comparison",
        "level":     1,
        "freq":      3,
        "meaning":   "«-dan ko'ra» — qiyoslash",
        "attach":    "명사 + 보다 (+ 더/덜)",
        "form_rule": "Ko'pincha <b>더</b> (ko'proq) yoki <b>덜</b> (kamroq) bilan: "
                     "A는 B<b>보다 더</b> 크다.",
        "note":      "<p>Eng ustunlik uchun <b>가장 / 제일</b>: <i>한국에서 서울이 <b>가장</b> 커요.</i></p>",
        "examples": [
            ("오늘이 어제보다 더 추워요.", "Bugun kechagidan ko'ra sovuqroq."),
            ("듣기보다 읽기가 쉬워요.", "Tinglashdan ko'ra o'qish osonroq."),
        ],
        "synonyms": [
            ("만큼", "만큼 = tenglik («shuncha»); 보다 = farq («-dan ko'ra»)"),
            ("에 비해", "에 비해 = rasmiy yozma «-ga nisbatan», 쓰기 53 uchun; 보다 = neytral"),
        ],
        "order": 117,
    },
    {
        "pattern":   "만큼",
        "category":  "particle",
        "function":  "comparison",
        "level":     3,
        "freq":      2,
        "meaning":   "«shuncha, shu darajada» — tenglik",
        "attach":    "명사 + 만큼 · 동사/형용사 + -(으)ㄹ 만큼",
        "form_rule": "Ot bilan: 형<b>만큼</b> 키가 커요. Fe'l bilan: 먹<b>을 만큼</b> 가져가세요.",
        "note":      "<p>«... darajada» ma'nosi TOPIK II 읽기 da tez-tez uchraydi: "
                     "<i>말할 수 없<b>을 만큼</b> 기뻤다</i> — aytib bo'lmas darajada xursand edim.</p>",
        "examples": [
            ("동생이 형만큼 키가 커요.", "Ukasi akasidek bo'yli."),
            ("필요한 만큼만 가져가세요.", "Kerakli miqdorda olib keting."),
        ],
        "synonyms": [
            ("보다", "보다 = farq bor; 만큼 = teng daraja"),
            ("처럼", "처럼 = o'xshashlik (ko'rinish); 만큼 = miqdor/daraja tengligi"),
        ],
        "order": 118,
    },
    {
        "pattern":   "조차 / 마저",
        "category":  "particle",
        "function":  "degree",
        "level":     5,
        "freq":      2,
        "meaning":   "«hatto ... ham» — kutilmagan qo'shimcha (ko'pincha salbiy)",
        "attach":    "명사 + 조차 / 마저",
        "form_rule": "<b>조차</b> — «hatto buni ham emas» (kutilganning eng oddiysi ham yo'q). "
                     "<b>마저</b> — «oxirgisi ham» (bor edi, u ham ketdi).",
        "note":      "<p>Ikkalasi ham salbiy yoki afsus ohangida. Yozma uslub, TOPIK 5-6 읽기.</p>",
        "examples": [
            ("이름조차 기억나지 않는다.", "Hatto ismi ham esimda yo'q."),
            ("친구마저 나를 떠났다.", "Do'stim ham (oxirgi bo'lib) meni tark etdi."),
        ],
        "synonyms": [
            ("까지", "까지 ijobiy gapda ham bo'ladi; 조차/마저 deyarli doim salbiy"),
            ("도", "도 = neytral «ham»; 조차 = «hatto ... ham» (kutilmagan)"),
        ],
        "order": 119,
    },
    {
        "pattern":   "은/는커녕",
        "category":  "particle",
        "function":  "contrast",
        "level":     5,
        "freq":      1,
        "meaning":   "«u yoqda tursin, ... ham emas»",
        "attach":    "명사 + 은/는커녕 · 동사 + -기는커녕",
        "form_rule": "Ikkinchi qismda ko'pincha 도 keladi: A<b>는커녕</b> B<b>도</b> 안/못...",
        "note":      "<p>Kutilgan katta narsani inkor qilib, undan ham kichigini inkor qiladi. "
                     "쓰기 va 읽기 da kuchli ta'sir beradi.</p>",
        "examples": [
            ("여행은커녕 주말에 쉬지도 못했어요.", "Sayohat u yoqda tursin, dam olish kuni dam ham ololmadim."),
            ("칭찬은커녕 혼만 났다.", "Maqtov o'rniga faqat urishish eshitdim."),
        ],
        "synonyms": [
            ("조차", "조차 = «hatto ... ham emas»; 은/는커녕 = ikki bosqichli inkor (kattasi ham, kichigi ham)"),
        ],
        "order": 120,
    },
    {
        "pattern":   "(으)로서 / (으)로써",
        "category":  "particle",
        "function":  "case",
        "level":     5,
        "freq":      2,
        "meaning":   "로서 = «sifatida» (maqom) · 로써 = «yordamida» (vosita)",
        "attach":    "명사 + (으)로서 / (으)로써",
        "form_rule": "받침 yo'q yoki ㄹ → <b>로서/로써</b> · boshqa 받침 → <b>으로서/으로써</b>",
        "note":      "<p>Rasmiy yozma uslub — 쓰기 54 uchun juda foydali.</p>"
                     "<ul><li><b>로서</b> = rol, maqom: <i>학생<b>으로서</b> 최선을 다했다.</i></li>"
                     "<li><b>로써</b> = vosita, usul: <i>대화<b>로써</b> 문제를 해결했다.</i></li></ul>",
        "mistake":   "<p>Ikkisini almashtirib yuborish eng tez-tez uchraydigan xato. "
                     "Esda saqlang: <b>로<u>서</u> = 신분</b> (maqom), <b>로<u>써</u> = 수단</b> (vosita).</p>",
        "examples": [
            ("교사로서 책임감을 느낍니다.", "O'qituvchi sifatida mas'uliyat his qilaman."),
            ("노력으로써 목표를 이루었다.", "Mehnat yordamida maqsadga erishdim."),
        ],
        "synonyms": [
            ("(으)로", "(으)로 = umumiy vosita/yo'nalish; (으)로서/(으)로써 = rasmiy, aniq ma'no"),
        ],
        "order": 121,
    },
    {
        "pattern":   "뿐",
        "category":  "particle",
        "function":  "degree",
        "level":     4,
        "freq":      2,
        "meaning":   "«faqat, -dan boshqa emas»",
        "attach":    "명사 + 뿐 · 동사/형용사 + -(으)ㄹ 뿐",
        "form_rule": "Ot bilan: 너<b>뿐</b>이야. Fe'l bilan: 웃<b>을 뿐</b>이었다.",
        "note":      "<p>쓰기 da eng kerakli shakli — <b>-(으)ㄹ 뿐만 아니라</b> "
                     "(«faqat ... emas, balki ... ham»). Qarang: 고급 문형 bo'limi.</p>",
        "examples": [
            ("내 친구는 자수르뿐이에요.", "Mening do'stim faqat Jasur."),
            ("그는 웃을 뿐 아무 말도 하지 않았다.", "U faqat kulib qo'ydi, hech narsa demadi."),
        ],
        "synonyms": [
            ("만", "만 = neytral og'zaki «faqat»; 뿐 = kitobiy, ta'kidli"),
            ("밖에", "밖에 inkor talab qiladi; 뿐 talab qilmaydi"),
        ],
        "order": 122,
    },
]
