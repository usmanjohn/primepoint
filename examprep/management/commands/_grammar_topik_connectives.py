# -*- coding: utf-8 -*-
"""Grammar bank — 연결어미 (connective endings), grouped by meaning.

Order decade: 300-399. Within the decade the points are ordered by meaning
group (sabab → qarama-qarshilik → shart → qarshi qo'yish → vaqt → maqsad →
sanash) so the "turi bo'yicha" view still reads as a teaching order.
See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── SABAB (이유) ───────────────────────────────────────────────────────
    {
        "pattern":   "-아서/어서",
        "category":  "connective",
        "function":  "reason",
        "level":     1,
        "freq":      3,
        "meaning":   "sabab — «-gani uchun, shuning uchun»",
        "attach":    "동사/형용사 + -아서/어서",
        "form_rule": "Oxirgi unli ㅏ/ㅗ → <b>-아서</b> (가다 → 가서) · boshqa → <b>-어서</b> (먹다 → 먹어서) · "
                     "하다 → <b>해서</b><br>⚠️ Oldiga <b>-았/었-</b> QO'SHILMAYDI: ❌ 먹었어서",
        "note":      "<p>Eng ko'p ishlatiladigan sabab shakli. Ikkinchi qismda "
                     "<b>buyruq va taklif kelolmaydi</b> — bu 니까 dan asosiy farqi.</p>"
                     "<p>«감사합니다 / 미안합니다 / 죄송합니다» dan oldin doim <b>-아서</b> keladi: "
                     "<i>늦<b>어서</b> 죄송합니다.</i></p>",
        "mistake":   "<p>❌ 비가 <b>와서</b> 우산을 가져가세요. → ✅ 비가 <b>오니까</b> 우산을 가져가세요.<br>"
                     "Buyruq bo'lsa — 니까.</p>",
        "examples": [
            ("배가 아파서 병원에 갔어요.", "Qornim og'rigani uchun shifoxonaga bordim."),
            ("길이 막혀서 늦었습니다.", "Yo'l tirband bo'lgani uchun kechikdim."),
            ("만나서 반갑습니다.", "Uchrashganimizdan xursandman."),
        ],
        "synonyms": [
            ("-(으)니까", "-(으)니까 dan keyin BUYRUQ/TAKLIF kelishi mumkin, -아서 dan keyin kelmaydi"),
            ("-기 때문에", "-기 때문에 = rasmiy, yozma sabab (쓰기 uchun); -아서 = kundalik"),
            ("-느라고", "-느라고 = sabab + SALBIY natija, ega bir xil bo'ladi"),
        ],
        "order": 300,
    },
    {
        "pattern":   "-(으)니까",
        "category":  "connective",
        "function":  "reason",
        "level":     2,
        "freq":      3,
        "meaning":   "sabab — «chunki»; buyruq va taklif bilan",
        "attach":    "동사/형용사 + -(으)니까",
        "form_rule": "받침 yo'q → <b>-니까</b> (가다 → 가니까) · 받침 bor → <b>-으니까</b> (먹다 → 먹으니까) · "
                     "ㄹ tushadi: 살다 → <b>사니까</b><br>O'tgan zamon qo'shiladi: <b>-았/었으니까</b> ✅",
        "note":      "<p>Ikkinchi qismda <b>buyruq (-(으)세요), taklif (-(으)ㅂ시다), so'roq</b> "
                     "erkin keladi — 아서 da bu mumkin emas.</p>"
                     "<p>Ikkinchi ma'nosi: <b>«...-gach, ko'rsam»</b> (bilib qolish): "
                     "<i>집에 가<b>니까</b> 아무도 없었어요.</i></p>",
        "mistake":   "<p>❌ 늦<b>으니까</b> 죄송합니다 → ✅ 늦<b>어서</b> 죄송합니다.<br>"
                     "Uzr va minnatdorchilikda faqat -아서.</p>",
        "examples": [
            ("시간이 없으니까 택시를 탑시다.", "Vaqt yo'q, shuning uchun taksi olaylik."),
            ("날씨가 추우니까 따뜻하게 입으세요.", "Havo sovuq, iliq kiyining."),
        ],
        "synonyms": [
            ("-아서/어서", "-아서 dan keyin buyruq/taklif KELMAYDI; -(으)니까 dan keyin keladi"),
            ("-기 때문에", "-기 때문에 = yozma va rasmiy; -(으)니까 = og'zaki, buyruq bilan"),
        ],
        "order": 301,
    },
    {
        "pattern":   "-기 때문에",
        "category":  "expression",
        "function":  "reason",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "sabab — «-ligi sababli» (rasmiy, yozma)",
        "attach":    "동사/형용사 + -기 때문에 · 명사 + 때문에",
        "form_rule": "Fe'l/sifat: 바쁘다 → <b>바쁘기 때문에</b> · Ot: 시험 <b>때문에</b> (기 yo'q!)<br>"
                     "O'tgan zamon: <b>-았/었기 때문에</b> · Gap oxirida: <b>-기 때문이다</b>",
        "note":      "<p><b>쓰기 53/54 uchun eng kerakli sabab shakli.</b> Ikkinchi qismda buyruq "
                     "kelmaydi (아서 kabi).</p>"
                     "<p>Tayyor jumla qolipi: <i>[주제]이/가 중요한 것은 [사유]<b>기 때문이다</b>.</i></p>",
        "mistake":   "<p>❌ 시험<b>이기 때문에</b> 공부해요 → ✅ 시험 <b>때문에</b> 공부해요.<br>"
                     "Otdan keyin 기 qo'shilmaydi.</p>",
        "examples": [
            ("환경이 오염되기 때문에 건강이 나빠진다.", "Atrof-muhit ifloslangani sababli sog'liq yomonlashadi."),
            ("교통 체증 때문에 시간을 낭비한다.", "Tirbandlik tufayli vaqt behuda ketadi."),
        ],
        "synonyms": [
            ("-아서/어서", "-아서 = og'zaki, qisqa; -기 때문에 = rasmiy, insho uchun"),
            ("-(으)로 인해", "-(으)로 인해 = eng rasmiy (maqola, hisobot); -기 때문에 = umumiy yozma"),
            ("-(으)므로", "-(으)므로 = ilmiy/huquqiy uslub, yanada quruqroq"),
        ],
        "order": 302,
    },
    {
        "pattern":   "-느라고",
        "category":  "connective",
        "function":  "reason",
        "level":     4,
        "freq":      3,
        "meaning":   "«-ish bilan band bo'lib» — sabab + salbiy natija",
        "attach":    "동사 + -느라고",
        "form_rule": "Faqat <b>동사</b> bilan (sifat bilan emas). O'tgan zamon qo'shilmaydi: ❌ 했느라고<br>"
                     "Ikki qismning <b>egasi bir xil</b> bo'lishi shart.",
        "note":      "<p>Birinchi ishga vaqt/kuch ketgani uchun ikkinchisi <b>bajarilmagan</b> — "
                     "natija deyarli doim salbiy yoki uzr.</p>"
                     "<p>TOPIK 읽기 va 듣기 da tez-tez uchraydigan «uzr» konstruksiyasi.</p>",
        "mistake":   "<p>❌ 비가 오<b>느라고</b> 못 갔어요 → ✅ 비가 <b>와서</b> 못 갔어요.<br>"
                     "«비가 오다» — mening harakatim emas, shuning uchun 느라고 bo'lmaydi.</p>",
        "examples": [
            ("시험공부를 하느라고 잠을 못 잤어요.", "Imtihonga tayyorlanib, uxlay olmadim."),
            ("아르바이트를 하느라고 친구를 못 만났다.", "Ishlab yurganim uchun do'stim bilan uchrasholmadim."),
        ],
        "synonyms": [
            ("-아서/어서", "-아서 = har qanday sabab; -느라고 = «shu ishga band bo'lib» + salbiy natija"),
            ("-는 바람에", "-는 바람에 = kutilmagan TASHQI sabab; -느라고 = o'zim qilgan ish"),
        ],
        "order": 303,
    },
    {
        "pattern":   "-는 바람에",
        "category":  "expression",
        "function":  "reason",
        "level":     4,
        "freq":      3,
        "meaning":   "«-gani tufayli (kutilmaganda)» — salbiy natija",
        "attach":    "동사 + -는 바람에",
        "form_rule": "Doim <b>-는</b> shaklida (o'tgan zamon bo'lsa ham): ❌ 온 바람에 → ✅ <b>오는 바람에</b><br>"
                     "Ikkinchi qism odatda <b>o'tgan zamon</b>da.",
        "note":      "<p>Sabab — <b>tasodifiy, kutilmagan, mendan tashqarida</b>. Natija salbiy. "
                     "느라고 dan farqi: bu yerda ayb menda emas.</p>",
        "examples": [
            ("갑자기 비가 오는 바람에 옷이 다 젖었어요.", "To'satdan yomg'ir yog'ib, kiyimim shalabbo bo'ldi."),
            ("버스가 늦게 오는 바람에 지각했다.", "Avtobus kech kelgani uchun kechikdim."),
        ],
        "synonyms": [
            ("-느라고", "-느라고 = o'zim qilgan ish sabab; -는 바람에 = tashqi, kutilmagan hodisa"),
            ("-는 통에", "-는 통에 = shovqin/tartibsizlik sababli — yanada salbiy va og'zaki"),
        ],
        "order": 304,
    },
    {
        "pattern":   "-길래 / -기에",
        "category":  "connective",
        "function":  "reason",
        "level":     5,
        "freq":      2,
        "meaning":   "«-gani uchun (shuni ko'rib)» — sabab + men qilgan ish",
        "attach":    "동사/형용사 + -길래 (og'zaki) / -기에 (yozma)",
        "form_rule": "Birinchi qism egasi — <b>boshqa odam</b>, ikkinchi qism egasi — <b>men</b>.",
        "note":      "<p>«Shunday bo'lganini ko'rdim/eshitdim, shuning uchun men bunday qildim» "
                     "ohangi. Ikkinchi qismda buyruq kelmaydi.</p>",
        "examples": [
            ("아이가 울길래 사탕을 줬어요.", "Bola yig'layotgani uchun konfet berdim."),
            ("날씨가 좋기에 산책을 나갔다.", "Havo yaxshi bo'lgani uchun sayrga chiqdim."),
        ],
        "synonyms": [
            ("-아서/어서", "-아서 = neytral sabab; -길래 = «buni ko'rib men shunday qildim»"),
            ("-(으)니까", "-(으)니까 = buyruq bilan ishlaydi; -길래 = faqat o'z harakatim haqida"),
        ],
        "order": 305,
    },
    {
        "pattern":   "-(으)므로",
        "category":  "connective",
        "function":  "reason",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "sabab — «-ligi bois» (ilmiy, rasmiy)",
        "attach":    "동사/형용사 + -(으)므로",
        "form_rule": "받침 yo'q → <b>-므로</b> · 받침 bor → <b>-으므로</b> · O'tgan: <b>-았/었으므로</b>",
        "note":      "<p>Eng quruq, kitobiy sabab shakli: qonun, hisobot, ilmiy maqola, 읽기 41-50. "
                     "Og'zaki nutqda deyarli ishlatilmaydi.</p>",
        "examples": [
            ("자료가 부족하므로 결론을 내리기 어렵다.", "Ma'lumot yetarli emasligi bois xulosa chiqarish qiyin."),
            ("규정을 위반하였으므로 처벌을 받는다.", "Qoidani buzgani uchun jazolanadi."),
        ],
        "synonyms": [
            ("-기 때문에", "-기 때문에 = umumiy yozma; -(으)므로 = ilmiy/huquqiy, quruqroq"),
            ("따라서", "따라서 = bog'lovchi ravish, alohida jumla boshlaydi; -(으)므로 = gap ichida"),
        ],
        "order": 306,
    },
    {
        "pattern":   "-(으)로 인해(서)",
        "category":  "expression",
        "function":  "reason",
        "level":     5,
        "freq":      3,
        "register":  "written",
        "meaning":   "«-tufayli, sababli» — rasmiy sabab (ot bilan)",
        "attach":    "명사 + (으)로 인해(서) · 동사 + -(으)ㅁ으로 인해",
        "form_rule": "받침 yo'q/ㄹ → <b>로 인해</b> · boshqa 받침 → <b>으로 인해</b>",
        "note":      "<p><b>쓰기 53 uchun oltin ibora</b> — grafik izohlashda sabab ko'rsatadi: "
                     "<i>인구 감소<b>로 인해</b> 노동력이 부족해졌다.</i></p>",
        "examples": [
            ("기후 변화로 인해 자연재해가 늘고 있다.", "Iqlim o'zgarishi tufayli tabiiy ofatlar ko'paymoqda."),
            ("경제 위기로 인해 실업률이 상승했다.", "Iqtisodiy inqiroz sababli ishsizlik darajasi oshdi."),
        ],
        "synonyms": [
            ("때문에", "때문에 = neytral; (으)로 인해 = rasmiy hisobot uslubi"),
            ("덕분에", "덕분에 = IJOBIY natija («tufayli, sharofati bilan»); (으)로 인해 = neytral/salbiy"),
        ],
        "order": 307,
    },
    {
        "pattern":   "덕분에 / 탓에",
        "category":  "expression",
        "function":  "reason",
        "level":     4,
        "freq":      2,
        "meaning":   "덕분에 = «sharofati bilan» (ijobiy) · 탓에 = «aybi bilan» (salbiy)",
        "attach":    "명사 + 덕분에/탓에 · 동사 + -(으)ㄴ 덕분에 / -(으)ㄴ 탓에",
        "form_rule": "Ijobiy natija → <b>덕분에</b> · Salbiy natija → <b>탓에</b> (yoki 탓으로)",
        "note":      "<p>Bu juftlikda <b>natijaning belgisi</b> shaklni tanlaydi. Minnatdorchilik "
                     "bildirishda: <i>선생님 <b>덕분에</b> 합격했습니다.</i></p>",
        "mistake":   "<p>❌ 게으른 <b>덕분에</b> 실패했다 → ✅ 게으른 <b>탓에</b> 실패했다.</p>",
        "examples": [
            ("친구 덕분에 한국 생활에 빨리 적응했어요.", "Do'stim sharofati bilan Koreya hayotiga tez moslashdim."),
            ("준비가 부족한 탓에 시험을 망쳤다.", "Tayyorgarlik yetishmagani aybi bilan imtihonni buzdim."),
        ],
        "synonyms": [
            ("(으)로 인해", "(으)로 인해 = neytral rasmiy; 덕분에/탓에 = baho beradi (ijobiy/salbiy)"),
        ],
        "order": 308,
    },

    # ── QARAMA-QARSHILIK (대조) ────────────────────────────────────────────
    {
        "pattern":   "-지만",
        "category":  "connective",
        "function":  "contrast",
        "level":     1,
        "freq":      3,
        "meaning":   "«lekin, ammo»",
        "attach":    "동사/형용사 + -지만",
        "form_rule": "받침ga qaramay <b>-지만</b>. O'tgan zamon: <b>-았/었지만</b>. Ot: 학생<b>이지만</b>.",
        "note":      "<p>Eng oddiy va aniq qarama-qarshilik. Ikki fikr <b>to'g'ridan-to'g'ri</b> "
                     "qarshi qo'yiladi.</p>",
        "examples": [
            ("한국어가 어렵지만 재미있어요.", "Koreys tili qiyin, lekin qiziqarli."),
            ("돈은 많지만 시간이 없다.", "Puli ko'p, lekin vaqti yo'q."),
        ],
        "synonyms": [
            ("-는데", "-는데 = yumshoq fon/kirish, doim qarshilik emas; -지만 = aniq qarshilik"),
            ("-(으)나", "-(으)나 = yozma, rasmiy «lekin» (쓰기 uchun); -지만 = neytral"),
        ],
        "order": 310,
    },
    {
        "pattern":   "-(으)ㄴ/는데",
        "category":  "connective",
        "function":  "contrast",
        "level":     2,
        "freq":      3,
        "meaning":   "fon berish yoki yumshoq qarshilik — «-di-yu, -gan edi»",
        "attach":    "동사 + -는데 · 형용사 + -(으)ㄴ데",
        "form_rule": "Fe'l → <b>-는데</b> (가다 → 가는데) · Sifat 받침 yo'q → <b>-ㄴ데</b> (크다 → 큰데) · "
                     "받침 bor → <b>-은데</b> (좋다 → 좋은데)<br>O'tgan zamon hamma uchun: <b>-았/었는데</b>",
        "note":      "<p><b>TOPIK'da eng ko'p uchraydigan grammatikalardan biri.</b> Uch vazifa:</p><ul>"
                     "<li><b>Fon</b> (kirish ma'lumot): 어제 시장에 갔<b>는데</b> 사람이 많았어요.</li>"
                     "<li><b>Yumshoq qarshilik</b>: 비가 오<b>는데</b> 우산이 없어요.</li>"
                     "<li><b>Iltimosga kirish</b>: 좀 바쁜<b>데</b> 도와주실 수 있어요?</li></ul>",
        "mistake":   "<p>Sifat va fe'lni chalkashtirish: ❌ 좋는데 → ✅ <b>좋은데</b> (sifat). "
                     "❌ 가은데 → ✅ <b>가는데</b> (fe'l). "
                     "⚠️ 있다/없다 fe'l kabi ishlaydi: <b>있는데</b>.</p>",
        "examples": [
            ("어제 영화를 봤는데 정말 좋았어요.", "Kecha kino ko'rdim — juda yaxshi ekan."),
            ("날씨가 추운데 왜 코트를 안 입어요?", "Havo sovuq-ku, nega palto kiymaysiz?"),
        ],
        "synonyms": [
            ("-지만", "-지만 = faqat qarshilik; -는데 = fon, kirish, yumshoq qarshilik"),
            ("-(으)ㄴ/는 반면에", "-반면에 = ikki narsani aniq TAQQOSLAYDI (yozma); -는데 = umumiy fon"),
        ],
        "order": 311,
    },
    {
        "pattern":   "-(으)나",
        "category":  "connective",
        "function":  "contrast",
        "level":     5,
        "freq":      2,
        "register":  "written",
        "meaning":   "«lekin, biroq» — yozma uslub",
        "attach":    "동사/형용사 + -(으)나",
        "form_rule": "받침 yo'q → <b>-나</b> · 받침 bor → <b>-으나</b> · O'tgan: <b>-았/었으나</b>",
        "note":      "<p>지만 ning kitobiy varianti. 쓰기 54 inshosida uslubni ko'taradi.</p>",
        "examples": [
            ("노력은 하였으나 결과가 좋지 않았다.", "Harakat qilindi, biroq natija yaxshi bo'lmadi."),
            ("비용은 많이 드나 효과가 확실하다.", "Xarajat ko'p ketadi, lekin samarasi aniq."),
        ],
        "synonyms": [
            ("-지만", "-지만 = neytral/og'zaki; -(으)나 = yozma, rasmiy"),
        ],
        "order": 312,
    },
    {
        "pattern":   "-(으)ㄴ/는 반면에",
        "category":  "expression",
        "function":  "contrast",
        "level":     4,
        "freq":      3,
        "register":  "written",
        "meaning":   "«-ning aksincha, boshqa tomondan»",
        "attach":    "동사 + -는 반면에 · 형용사 + -(으)ㄴ 반면에",
        "form_rule": "Fe'l → <b>-는 반면에</b> · Sifat → <b>-(으)ㄴ 반면에</b> · Ot → <b>인 반면에</b>",
        "note":      "<p><b>쓰기 53/54 uchun kuchli ibora</b> — ikki tomonni taqqoslash qismida. "
                     "Tayyor qolip: <i>A는 [장점]<b>인 반면에</b> B는 [단점]이다.</i></p>",
        "examples": [
            ("도시는 편리한 반면에 공기가 나쁘다.", "Shahar qulay, buning aksincha havosi yomon."),
            ("수입은 늘어난 반면에 지출도 증가했다.", "Daromad oshgan, shu bilan birga xarajat ham ko'paygan."),
        ],
        "synonyms": [
            ("-지만", "-지만 = qisqa qarshilik; -는 반면에 = ikki narsani tizimli taqqoslash"),
            ("-(으)ㄴ/는 데 반해", "deyarli bir xil — 데 반해 biroz rasmiyroq"),
        ],
        "order": 313,
    },

    # ── SHART (조건) ───────────────────────────────────────────────────────
    {
        "pattern":   "-(으)면",
        "category":  "connective",
        "function":  "condition",
        "level":     1,
        "freq":      3,
        "meaning":   "«-sa, agar» — shart",
        "attach":    "동사/형용사 + -(으)면",
        "form_rule": "받침 yo'q → <b>-면</b> (가다 → 가면) · 받침 bor → <b>-으면</b> (먹다 → 먹으면) · "
                     "ㄹ tushmaydi: 살다 → <b>살면</b><br>O'tgan farazi: <b>-았/었으면</b>",
        "note":      "<p>Ham <b>haqiqiy shart</b> (돈이 있<b>으면</b> 사겠다), ham "
                     "<b>takrorlanuvchi holat</b> (봄이 되<b>면</b> 꽃이 핀다 — bahor kelsa gul ochiladi).</p>"
                     "<p>Ko'pincha 만약 / 만일 bilan kuchaytiriladi.</p>",
        "examples": [
            ("시간이 있으면 같이 갑시다.", "Vaqtingiz bo'lsa, birga boraylik."),
            ("열심히 공부하면 좋은 결과가 나온다.", "Tirishib o'qisang, yaxshi natija chiqadi."),
        ],
        "synonyms": [
            ("-거든", "-거든 dan keyin BUYRUQ/taklif keladi; -(으)면 dan keyin har narsa keladi"),
            ("-아야/어야", "-아야 = «faqat shu shart bilan» (majburiy shart); -(으)면 = oddiy shart"),
        ],
        "order": 320,
    },
    {
        "pattern":   "-아야/어야",
        "category":  "connective",
        "function":  "condition",
        "level":     3,
        "freq":      2,
        "meaning":   "«faqat ...-sagina» — majburiy shart",
        "attach":    "동사/형용사 + -아야/어야 (+ 되다/하다)",
        "form_rule": "ㅏ/ㅗ → <b>-아야</b> · boshqa → <b>-어야</b> · 하다 → <b>해야</b><br>"
                     "Kuchaytirilgan shakl: <b>-아야만</b>",
        "note":      "<p>Shartsiz natija <b>bo'lmaydi</b>: <i>연습을 많이 <b>해야</b> 실력이 는다</i> — "
                     "faqat ko'p mashq qilsagina saviya o'sadi.</p>"
                     "<p>«-아야 하다/되다» = majburiyat — alohida ibora sifatida ham qarang.</p>",
        "examples": [
            ("여권이 있어야 비행기를 탈 수 있어요.", "Faqat pasport bo'lsagina samolyotga chiqish mumkin."),
            ("일찍 출발해야 늦지 않는다.", "Erta yo'lga chiqsagina kechikmaysan."),
        ],
        "synonyms": [
            ("-(으)면", "-(으)면 = oddiy shart; -아야 = «boshqa yo'li yo'q» degan majburiy shart"),
            ("-아야 하다", "-아야 하다 = majburiyat («qilish kerak»); -아야 = shart bog'lovchisi"),
        ],
        "order": 321,
    },
    {
        "pattern":   "-거든",
        "category":  "connective",
        "function":  "condition",
        "level":     4,
        "freq":      2,
        "meaning":   "«-sang» — shart + buyruq/taklif",
        "attach":    "동사/형용사 + -거든",
        "form_rule": "Ikkinchi qismda <b>albatta</b> buyruq, taklif yoki niyat keladi.",
        "note":      "<p>-(으)면 dan farqi: 거든 dan keyin <b>faqat</b> buyruq/taklif/niyat keladi. "
                     "Kelajakda sodir bo'lishi ehtimoli yuqori narsa haqida.</p>",
        "mistake":   "<p>❌ 시간이 있<b>거든</b> 영화를 봤어요 → ✅ 시간이 있<b>으면</b> 영화를 봤어요. "
                     "O'tgan zamon natija bilan 거든 ishlatilmaydi.</p>",
        "examples": [
            ("서울에 도착하거든 연락해 주세요.", "Seulga yetib borsangiz, xabar bering."),
            ("힘들거든 잠깐 쉬어라.", "Charchasang, birpas dam ol."),
        ],
        "synonyms": [
            ("-(으)면", "-(으)면 = universal shart; -거든 = faqat buyruq/taklif bilan"),
            ("-(으)ㄹ 때", "-(으)ㄹ 때 = vaqt («...-ganda»); -거든 = shart («agar»)"),
        ],
        "order": 322,
    },

    # ── QARSHI QO'YISH (양보) ──────────────────────────────────────────────
    {
        "pattern":   "-아도/어도",
        "category":  "connective",
        "function":  "concession",
        "level":     2,
        "freq":      3,
        "meaning":   "«-sa ham»",
        "attach":    "동사/형용사 + -아도/어도",
        "form_rule": "ㅏ/ㅗ → <b>-아도</b> · boshqa → <b>-어도</b> · 하다 → <b>해도</b><br>"
                     "Ot: 학생<b>이어도</b> · Kuchaytirish: 아무리 ...-아도",
        "note":      "<p>아무리 bilan birga TOPIK 읽기 da doim uchraydi: "
                     "<i><b>아무리</b> 바빠<b>도</b> 아침은 먹어야 한다.</i></p>"
                     "<p>«-아도 되다» = ruxsat («qilsa bo'ladi») — alohida ibora.</p>",
        "examples": [
            ("아무리 어려워도 포기하지 않겠습니다.", "Qanchalik qiyin bo'lsa ham taslim bo'lmayman."),
            ("비가 와도 축구를 할 거예요.", "Yomg'ir yog'sa ham futbol o'ynaymiz."),
        ],
        "synonyms": [
            ("-더라도", "-더라도 = faraziy, kuchliroq («hatto ...-sa ham»); -아도 = real, kundalik"),
            ("-(으)ㄹ지라도", "-(으)ㄹ지라도 = eng kitobiy variant, 읽기 5-6 daraja"),
            ("-(으)ㄴ/는데도", "-는데도 = «shunday bo'lsa ham» — fakt allaqachon ro'y bergan"),
        ],
        "order": 330,
    },
    {
        "pattern":   "-더라도",
        "category":  "connective",
        "function":  "concession",
        "level":     4,
        "freq":      2,
        "meaning":   "«hatto -sa ham» — faraziy qarshi qo'yish",
        "attach":    "동사/형용사 + -더라도",
        "form_rule": "받침ga qaramay <b>-더라도</b>. O'tgan: <b>-았/었더라도</b>.",
        "note":      "<p>-아도 dan <b>kuchliroq va faraziyroq</b>: hali bo'lmagan yoki bo'lishi "
                     "dargumon holat. Ko'pincha 비록/아무리 bilan.</p>",
        "examples": [
            ("실패하더라도 다시 도전하겠다.", "Muvaffaqiyatsizlikka uchrasam ham yana urinaman."),
            ("비록 시간이 걸리더라도 끝까지 하겠습니다.", "Vaqt ketsa ham, oxirigacha qilaman."),
        ],
        "synonyms": [
            ("-아도/어도", "-아도 = real, tez-tez bo'ladigan; -더라도 = faraziy, kuchli ta'kid"),
            ("-(으)ㄹ지라도", "-(으)ㄹ지라도 = yozma, eng rasmiy varianti"),
        ],
        "order": 331,
    },
    {
        "pattern":   "-(으)ㄴ/는데도",
        "category":  "connective",
        "function":  "concession",
        "level":     4,
        "freq":      2,
        "meaning":   "«shunday bo'lgani holda ham» — kutilmagan natija",
        "attach":    "동사 + -는데도 · 형용사 + -(으)ㄴ데도",
        "form_rule": "-(으)ㄴ/는데 + 도. O'tgan: <b>-았/었는데도</b>. Kuchaytirish: <b>-는데도 불구하고</b>.",
        "note":      "<p>Birinchi qism — <b>haqiqatan sodir bo'lgan</b> fakt, lekin natija kutilganidek "
                     "chiqmagan. Shu bilan 아도/더라도 dan farq qiladi (ular faraz).</p>",
        "examples": [
            ("열심히 공부했는데도 성적이 오르지 않았다.", "Tirishib o'qiganim holda ham bahom ko'tarilmadi."),
            ("약을 먹었는데도 아직 아파요.", "Dori ichganim holda hali ham og'riyapti."),
        ],
        "synonyms": [
            ("-아도/어도", "-아도 = umumiy/faraziy; -는데도 = ro'y bergan faktga qaramay"),
            ("-(으)ㅁ에도 불구하고", "eng rasmiy yozma varianti — 쓰기 54 uchun"),
        ],
        "order": 332,
    },

    # ── VAQT (시간·순서) ───────────────────────────────────────────────────
    {
        "pattern":   "-고 나서 / -(으)ㄴ 후에",
        "category":  "connective",
        "function":  "time",
        "level":     2,
        "freq":      3,
        "meaning":   "«-gandan keyin»",
        "attach":    "동사 + -고 나서 · 동사 + -(으)ㄴ 후에/다음에",
        "form_rule": "<b>-고 나서</b> = ish <b>tugagach</b> (tugallanish ta'kidi) · "
                     "<b>-(으)ㄴ 후에 / -(으)ㄴ 다음에</b> = shunchaki keyin<br>"
                     "Ot bilan: 식사 <b>후에</b>",
        "note":      "<p>Ikkalasida ham ikkinchi harakat birinchisidan <b>keyin</b> bo'ladi. "
                     "-고 나서 tugallanganlikni kuchliroq ta'kidlaydi.</p>",
        "examples": [
            ("숙제를 하고 나서 게임을 했어요.", "Uy vazifasini qilib bo'lgach, o'yin o'ynadim."),
            ("수업이 끝난 후에 도서관에 갈 거예요.", "Dars tugagach kutubxonaga boraman."),
        ],
        "synonyms": [
            ("-자마자", "-자마자 = «darhol, shu zahoti»; -고 나서 = shunchaki keyin"),
            ("-기 전에", "-기 전에 = teskarisi — «...-dan oldin»"),
        ],
        "order": 340,
    },
    {
        "pattern":   "-기 전에",
        "category":  "expression",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "meaning":   "«-dan oldin»",
        "attach":    "동사 + -기 전에 · 명사 + 전에",
        "form_rule": "Fe'l: 자<b>기 전에</b> · Ot: 식사 <b>전에</b> (기 yo'q)<br>"
                     "⚠️ Fe'l <b>o'tgan zamonga qo'yilmaydi</b>: ❌ 갔기 전에",
        "examples": [
            ("자기 전에 이를 닦으세요.", "Uxlashdan oldin tishingizni tozalang."),
            ("결정하기 전에 잘 생각해 보세요.", "Qaror qilishdan oldin yaxshilab o'ylab ko'ring."),
        ],
        "synonyms": [
            ("-(으)ㄴ 후에", "teskari yo'nalish — «...-dan keyin»"),
        ],
        "order": 341,
    },
    {
        "pattern":   "-자마자",
        "category":  "connective",
        "function":  "time",
        "level":     3,
        "freq":      3,
        "meaning":   "«-ishi bilanoq, darhol»",
        "attach":    "동사 + -자마자",
        "form_rule": "받침ga qaramay <b>-자마자</b>. Oldiga o'tgan zamon qo'shilmaydi: ❌ 왔자마자",
        "note":      "<p>Ikki hodisa orasida <b>vaqt yo'q</b>. Ikkinchi qismda buyruq ham kelishi mumkin.</p>",
        "examples": [
            ("집에 도착하자마자 전화할게요.", "Uyga yetib borishim bilanoq qo'ng'iroq qilaman."),
            ("수업이 끝나자마자 뛰어나갔다.", "Dars tugashi bilanoq yugurib chiqib ketdi."),
        ],
        "synonyms": [
            ("-고 나서", "-고 나서 = biroz vaqtdan keyin ham bo'ladi; -자마자 = shu zahoti"),
            ("-는 대로", "-는 대로 = «...-ishi bilan, imkoni bo'lishi bilan» — reja/kelajak uchun ko'proq"),
        ],
        "order": 342,
    },
    {
        "pattern":   "-(으)면서",
        "category":  "connective",
        "function":  "time",
        "level":     2,
        "freq":      3,
        "meaning":   "«-a turib, bir vaqtda»",
        "attach":    "동사 + -(으)면서",
        "form_rule": "받침 yo'q → <b>-면서</b> · 받침 bor → <b>-으면서</b><br>"
                     "Ikki qismning <b>egasi bir xil</b> bo'lishi shart.",
        "note":      "<p>Ikkinchi ma'nosi — <b>qarama-qarshilik</b>: "
                     "<i>알<b>면서</b> 모르는 척한다</i> — bilib turib, bilmaganga oladi.</p>",
        "mistake":   "<p>❌ 아프소나가 노래하<b>면서</b> 자수르가 춤을 춰요 → egalar har xil. "
                     "✅ 아프소나가 노래하<b>고</b> 자수르가 춤을 춰요.</p>",
        "examples": [
            ("음악을 들으면서 공부해요.", "Musiqa tinglab turib o'qiyman."),
            ("커피를 마시면서 이야기합시다.", "Qahva icha turib gaplashaylik."),
        ],
        "synonyms": [
            ("-는 동안", "-는 동안 = davomiylik («...-gan vaqt ichida»), egalar har xil bo'lishi mumkin"),
            ("-다가", "-다가 = harakat TO'XTAB, boshqasiga o'tadi; -(으)면서 = ikkalasi birga davom etadi"),
        ],
        "order": 343,
    },
    {
        "pattern":   "-다가",
        "category":  "connective",
        "function":  "time",
        "level":     3,
        "freq":      3,
        "meaning":   "«-ayotganda (to'xtab), -a-yu keyin»",
        "attach":    "동사 + -다가",
        "form_rule": "Davom etayotgan ish: <b>-다가</b> · Tugagan ish: <b>-았/었다가</b>",
        "note":      "<p>Birinchi harakat <b>uzilib</b>, ikkinchisiga o'tiladi: "
                     "<i>학교에 가<b>다가</b> 친구를 만났어요</i> — maktabga ketayotib do'stimni uchratdim.</p>"
                     "<p><b>-았다가</b> = birinchi ish <b>to'liq tugagan</b>, keyin qarama-qarshisi: "
                     "<i>창문을 열<b>었다가</b> 닫았다.</i></p>",
        "examples": [
            ("길을 걷다가 지갑을 주웠어요.", "Yo'ldan ketayotib hamyon topib oldim."),
            ("불을 켰다가 다시 껐다.", "Chiroqni yoqib, keyin yana o'chirdim."),
        ],
        "synonyms": [
            ("-(으)면서", "-(으)면서 = ikkalasi bir vaqtda davom etadi; -다가 = birinchisi to'xtaydi"),
            ("-는 길에", "-는 길에 = «yo'l-yo'lakay» — faqat borish/kelish bilan"),
        ],
        "order": 344,
    },
    {
        "pattern":   "-는 동안(에)",
        "category":  "expression",
        "function":  "time",
        "level":     3,
        "freq":      2,
        "meaning":   "«-gan vaqt ichida, davomida»",
        "attach":    "동사 + -는 동안 · 명사 + 동안",
        "form_rule": "Fe'l: 자<b>는 동안</b> · Ot: 세 시간 <b>동안</b>, 방학 <b>동안</b>",
        "note":      "<p>-(으)면서 dan farqi: bu yerda ikki qismning <b>egasi har xil</b> bo'lishi mumkin.</p>",
        "examples": [
            ("아기가 자는 동안 청소를 했어요.", "Chaqaloq uxlayotgan vaqtda tozaladim."),
            ("방학 동안 아르바이트를 했다.", "Ta'til davomida ishladim."),
        ],
        "synonyms": [
            ("-(으)면서", "-(으)면서 — bitta odam ikki ishni birga qiladi; -는 동안 — turli odamlar"),
        ],
        "order": 345,
    },
    {
        "pattern":   "-(으)ㄹ 때",
        "category":  "expression",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "meaning":   "«-ganda, -gan paytda»",
        "attach":    "동사/형용사 + -(으)ㄹ 때 · 명사 + 때",
        "form_rule": "받침 yo'q → <b>-ㄹ 때</b> · 받침 bor → <b>-을 때</b><br>"
                     "Tugagan ish uchun: <b>-았/었을 때</b> · Ot: 어릴 <b>때</b>, 방학 <b>때</b>",
        "note":      "<p><b>-(으)ㄹ 때</b> = harakat davomida · <b>-았을 때</b> = harakat tugagach.<br>"
                     "<i>밥을 먹<b>을 때</b></i> (ovqatlanayotganda) ≠ <i>밥을 먹<b>었을 때</b></i> (yeb bo'lganda).</p>",
        "examples": [
            ("한국에 처음 왔을 때 많이 힘들었어요.", "Koreyaga birinchi kelganimda juda qiynaldim."),
            ("운전할 때 전화하지 마세요.", "Mashina haydayotganda telefonda gaplashmang."),
        ],
        "synonyms": [
            ("-는 동안", "-는 동안 = butun davr; -(으)ㄹ 때 = shu payt/holat"),
            ("-거든", "-거든 = shart («agar»); -(으)ㄹ 때 = vaqt («...-ganda»)"),
        ],
        "order": 346,
    },

    # ── MAQSAD (목적) ──────────────────────────────────────────────────────
    {
        "pattern":   "-(으)러",
        "category":  "connective",
        "function":  "purpose",
        "level":     1,
        "freq":      3,
        "meaning":   "«-gani (borish/kelish uchun)»",
        "attach":    "동사 + -(으)러 + 가다/오다/다니다",
        "form_rule": "받침 yo'q → <b>-러</b> (사다 → 사러) · 받침 bor → <b>-으러</b> (먹다 → 먹으러) · "
                     "ㄹ tushadi: 놀다 → <b>놀러</b>",
        "note":      "<p>⚠️ Keyin <b>faqat harakat fe'llari</b> keladi: 가다, 오다, 다니다, 나가다. "
                     "Boshqa fe'l bo'lsa — <b>-(으)려고</b> ishlating.</p>",
        "mistake":   "<p>❌ 한국어를 배우<b>러</b> 책을 샀어요 → ✅ 한국어를 배우<b>려고</b> 책을 샀어요.</p>",
        "examples": [
            ("친구를 만나러 카페에 갔어요.", "Do'stim bilan uchrashgani kafega bordim."),
            ("한국어를 배우러 한국에 왔습니다.", "Koreys tilini o'rganish uchun Koreyaga keldim."),
        ],
        "synonyms": [
            ("-(으)려고", "-(으)려고 = har qanday fe'l bilan; -(으)러 = faqat 가다/오다 bilan"),
            ("-기 위해서", "-기 위해서 = rasmiy, yozma maqsad (쓰기 uchun)"),
        ],
        "order": 350,
    },
    {
        "pattern":   "-(으)려고",
        "category":  "connective",
        "function":  "intention",
        "level":     2,
        "freq":      3,
        "meaning":   "«-moqchi bo'lib, -ish uchun» — niyat",
        "attach":    "동사 + -(으)려고",
        "form_rule": "받침 yo'q → <b>-려고</b> · 받침 bor → <b>-으려고</b><br>"
                     "Yakka shakli: <b>-(으)려고 하다</b> («-moqchi»)",
        "note":      "<p>Ikkinchi qismda <b>buyruq/taklif kelmaydi</b> — bu 기 위해서 dan farqi.</p>"
                     "<p><b>-(으)려고 하다</b> = «-moqchiman»: <i>내년에 유학 가<b>려고 해요</b>.</i></p>",
        "mistake":   "<p>❌ 살을 빼<b>려고</b> 운동하세요 → ✅ 살을 빼<b>기 위해</b> 운동하세요. "
                     "Buyruq bo'lsa 기 위해.</p>",
        "examples": [
            ("시험에 합격하려고 매일 공부해요.", "Imtihondan o'tish uchun har kuni o'qiyman."),
            ("내년에 대학에 진학하려고 합니다.", "Kelasi yil universitetga kirmoqchiman."),
        ],
        "synonyms": [
            ("-(으)러", "-(으)러 = faqat 가다/오다 bilan; -(으)려고 = har qanday fe'l bilan"),
            ("-기 위해서", "-기 위해서 = rasmiy va buyruq bilan ishlaydi; -(으)려고 = og'zaki niyat"),
            ("-고자", "-고자 = eng rasmiy yozma niyat (TOPIK 5-6)"),
        ],
        "order": 351,
    },
    {
        "pattern":   "-기 위해(서)",
        "category":  "expression",
        "function":  "purpose",
        "level":     3,
        "freq":      3,
        "register":  "written",
        "meaning":   "«-ish uchun, maqsadida» (rasmiy)",
        "attach":    "동사 + -기 위해(서) · 명사 + 을/를 위해(서)",
        "form_rule": "Fe'l: 건강해지<b>기 위해</b> · Ot: 건강<b>을 위해</b> (기 yo'q)",
        "note":      "<p><b>쓰기 54 uchun asosiy maqsad shakli.</b> Tayyor qolip: "
                     "<i>[문제]을/를 해결하<b>기 위해서</b>는 [방법]이 필요하다.</i></p>",
        "examples": [
            ("환경을 보호하기 위해 노력해야 한다.", "Atrof-muhitni himoya qilish uchun harakat qilish kerak."),
            ("건강을 위해서 규칙적으로 운동합니다.", "Sog'liq uchun muntazam sport bilan shug'ullanaman."),
        ],
        "synonyms": [
            ("-(으)려고", "-(으)려고 = og'zaki niyat; -기 위해서 = rasmiy maqsad, insho uchun"),
            ("-도록", "-도록 = «...-adigan qilib» (natijaga yo'naltirilgan); -기 위해 = maqsad"),
        ],
        "order": 352,
    },
    {
        "pattern":   "-도록",
        "category":  "connective",
        "function":  "purpose",
        "level":     4,
        "freq":      2,
        "meaning":   "«-adigan qilib, -guncha» — maqsad/daraja",
        "attach":    "동사/형용사 + -도록",
        "form_rule": "받침ga qaramay <b>-도록</b>.",
        "note":      "<p>Uch ma'no:</p><ul>"
                     "<li><b>Maqsad</b>: 잘 보이<b>도록</b> 크게 썼어요 — yaxshi ko'rinadigan qilib.</li>"
                     "<li><b>Daraja</b>: 목이 아프<b>도록</b> 소리쳤다 — tomog'i og'riguncha baqirdi.</li>"
                     "<li><b>Buyruq</b> (rasmiy): 조용히 하<b>도록</b> 하세요.</li></ul>"
                     "<p>기 위해 dan farqi: 도록 da ikki qismning egasi <b>har xil</b> bo'lishi mumkin.</p>",
        "examples": [
            ("학생들이 이해하도록 천천히 설명했다.", "Talabalar tushunadigan qilib sekin tushuntirdim."),
            ("늦지 않도록 서두르세요.", "Kechikmaydigan qilib shoshiling."),
        ],
        "synonyms": [
            ("-기 위해서", "-기 위해 = ega bir xil, aniq maqsad; -도록 = boshqa odam uchun natija"),
            ("-게", "-게 ham «...-adigan qilib» — 도록 ning qisqa, og'zaki varianti"),
        ],
        "order": 353,
    },

    # ── SANASH VA TANLOV (나열·선택) ───────────────────────────────────────
    {
        "pattern":   "-고",
        "category":  "connective",
        "function":  "listing",
        "level":     1,
        "freq":      3,
        "meaning":   "«va, -ib» — sanash yoki ketma-ketlik",
        "attach":    "동사/형용사 + -고",
        "form_rule": "받침ga qaramay <b>-고</b>. Ot: 학생<b>이고</b>.",
        "note":      "<p>Ikki vazifa: <b>sanash</b> (김치는 맵<b>고</b> 짜요) va "
                     "<b>ketma-ketlik</b> (밥을 먹<b>고</b> 학교에 가요).</p>"
                     "<p>Ketma-ketlik ma'nosida ikki qism egasi bir xil bo'ladi.</p>",
        "examples": [
            ("아프소나는 착하고 똑똑해요.", "Afsona yaxshi va aqlli."),
            ("숙제를 하고 잤어요.", "Uy vazifasini qilib uxladim."),
        ],
        "synonyms": [
            ("-(으)며", "-(으)며 = yozma, rasmiy «va» (쓰기 uchun); -고 = neytral"),
            ("-아서/어서", "-아서 = birinchi harakat ikkinchisiga BOG'LIQ (가서 만났다); -고 = mustaqil ikki ish"),
        ],
        "order": 360,
    },
    {
        "pattern":   "-(으)며",
        "category":  "connective",
        "function":  "listing",
        "level":     4,
        "freq":      2,
        "register":  "written",
        "meaning":   "«va, bir vaqtda» — yozma uslub",
        "attach":    "동사/형용사 + -(으)며",
        "form_rule": "받침 yo'q → <b>-며</b> · 받침 bor → <b>-으며</b>",
        "note":      "<p>-고 (sanash) va -(으)면서 (bir vaqtda) ning <b>yozma varianti</b>. "
                     "쓰기 53/54 da uslubni ko'taradi.</p>",
        "examples": [
            ("이 제도는 효율적이며 비용도 적게 든다.", "Bu tizim samarali va xarajati ham kam."),
            ("자료를 분석하며 문제점을 찾았다.", "Ma'lumotlarni tahlil qila turib muammolarni topdim."),
        ],
        "synonyms": [
            ("-고", "-고 = og'zaki/neytral; -(으)며 = yozma, rasmiy"),
            ("-(으)면서", "-(으)면서 = og'zaki «bir vaqtda»; -(으)며 = uning yozma varianti"),
        ],
        "order": 361,
    },
    {
        "pattern":   "-거나",
        "category":  "connective",
        "function":  "choice",
        "level":     2,
        "freq":      2,
        "meaning":   "«yoki» — fe'llar orasida tanlov",
        "attach":    "동사/형용사 + -거나",
        "form_rule": "받침ga qaramay <b>-거나</b>. Ot uchun esa <b>(이)나</b> ishlatiladi.",
        "note":      "<p>«아무리 ...-거나» yoki «-거나 -거나» juft shaklda «...-sa ham, ...-sa ham» "
                     "ma'nosi chiqadi.</p>",
        "examples": [
            ("주말에는 책을 읽거나 영화를 봐요.", "Dam olish kunlari kitob o'qiyman yoki kino ko'raman."),
            ("가거나 말거나 네 마음대로 해라.", "Borasanmi, bormaysanmi — o'zing bil."),
        ],
        "synonyms": [
            ("(이)나", "(이)나 = OT orasida «yoki»; -거나 = FE'L orasida"),
            ("-든지", "-든지 = «qaysi biri bo'lsa ham farqi yo'q» (befarqlik ohangi)"),
        ],
        "order": 362,
    },
    {
        "pattern":   "-든지 / -든가",
        "category":  "connective",
        "function":  "choice",
        "level":     4,
        "freq":      2,
        "meaning":   "«...-sa ham, farqi yo'q» — befarq tanlov",
        "attach":    "동사/형용사 + -든지",
        "form_rule": "So'roq so'zlari bilan juda ko'p: 누구<b>든지</b>, 언제<b>든지</b>, 어디<b>든지</b>, 뭐<b>든지</b>.",
        "note":      "<p>거나 dan farqi: bu yerda <b>qaysi birini tanlash muhim emas</b> degan ohang bor.</p>",
        "examples": [
            ("언제든지 연락하세요.", "Istalgan vaqtda bog'laning."),
            ("가든지 말든지 마음대로 하세요.", "Borasizmi-bormaysizmi, o'zingiz bilasiz."),
        ],
        "synonyms": [
            ("-거나", "-거나 = oddiy «yoki»; -든지 = «qaysi biri bo'lsa ham farqi yo'q»"),
        ],
        "order": 363,
    },
]
