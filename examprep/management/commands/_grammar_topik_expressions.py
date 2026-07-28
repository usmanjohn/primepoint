# -*- coding: utf-8 -*-
"""Grammar bank — 문형 (set expressions), TOPIK I-II core.

Order decade: 500-599. See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── IMKONIYAT VA QOBILIYAT ─────────────────────────────────────────────
    {
        "pattern":   "-(으)ㄹ 수 있다/없다",
        "category":  "expression",
        "function":  "ability",
        "level":     1,
        "freq":      3,
        "meaning":   "«-a olmoq / -a olmaslik» — imkoniyat va qobiliyat",
        "attach":    "동사 + -(으)ㄹ 수 있다/없다",
        "form_rule": "받침 yo'q → <b>-ㄹ 수 있다</b> · 받침 bor → <b>-을 수 있다</b>",
        "note":      "<p>Ham <b>qobiliyat</b> (한국어를 할 수 있어요), ham <b>imkoniyat/ruxsat</b> "
                     "(여기에서 사진을 찍을 수 있어요) ma'nosi.</p>",
        "mistake":   "<p>❌ 저는 수영을 <b>못 할 수 있어요</b> → ✅ 저는 수영을 <b>할 수 없어요</b> "
                     "yoki <b>못 해요</b>. Ikki inkorni birga qo'ymang.</p>",
        "examples": [
            ("저는 한국어로 이메일을 쓸 수 있어요.", "Men koreyscha elektron xat yoza olaman."),
            ("이 문제는 혼자 해결할 수 없다.", "Bu muammoni yolg'iz hal qilib bo'lmaydi."),
        ],
        "synonyms": [
            ("-(으)ㄹ 줄 알다/모르다", "-(으)ㄹ 줄 알다 = O'RGANIB olingan mahorat; -(으)ㄹ 수 있다 = umumiy imkoniyat"),
            ("못", "못 = tashqi to'siq sababli qila olmaslik; -(으)ㄹ 수 없다 = umuman imkonsiz"),
        ],
        "order": 500,
    },
    {
        "pattern":   "-(으)ㄹ 줄 알다/모르다",
        "category":  "expression",
        "function":  "ability",
        "level":     2,
        "freq":      2,
        "meaning":   "«-ishni bilmoq / bilmaslik» — o'rganilgan mahorat",
        "attach":    "동사 + -(으)ㄹ 줄 알다/모르다",
        "form_rule": "받침 yo'q → <b>-ㄹ 줄 알다</b> · 받침 bor → <b>-을 줄 알다</b>",
        "note":      "<p>Mashq qilib <b>o'rganilgan</b> ko'nikma haqida: suzish, mashina haydash, "
                     "chalish. Shu sababli «hozir vaqtim bor» ma'nosida ishlatilmaydi.</p>",
        "mistake":   "<p>❌ 오늘 갈 <b>줄 알아요</b> → ✅ 오늘 갈 <b>수 있어요</b>. "
                     "Bugungi imkoniyat — mahorat emas.</p>",
        "examples": [
            ("셰르베크는 기타를 칠 줄 알아요.", "Sherbek gitara chalishni biladi."),
            ("저는 운전할 줄 몰라요.", "Men mashina haydashni bilmayman."),
        ],
        "synonyms": [
            ("-(으)ㄹ 수 있다", "-(으)ㄹ 수 있다 = imkoniyat; -(으)ㄹ 줄 알다 = o'rganilgan mahorat"),
        ],
        "order": 501,
    },
    {
        "pattern":   "안 / -지 않다 · 못 / -지 못하다",
        "category":  "expression",
        "function":  "ability",
        "level":     1,
        "freq":      3,
        "meaning":   "안 = xohlamaslik/oddiy inkor · 못 = qila olmaslik",
        "attach":    "안 + 동사 · 동사 + -지 않다 / -지 못하다",
        "form_rule": "Qisqa: <b>안</b> 가요 / <b>못</b> 가요 · Uzun: 가<b>지 않아요</b> / 가<b>지 못해요</b><br>"
                     "«명사+하다» fe'llarida 안/못 <b>o'rtaga</b> kiradi: 공부 <b>안</b> 해요 (❌ 안 공부해요)",
        "note":      "<p><b>안</b> = qilmadim (xohlamadim, sababi yo'q). <b>못</b> = qila olmadim "
                     "(to'siq, imkoniyat yo'q). Sifat bilan <b>못</b> ishlatilmaydi.</p>",
        "mistake":   "<p>❌ 안 <b>공부해요</b> → ✅ 공부 <b>안</b> 해요.<br>"
                     "❌ 못 <b>예뻐요</b> → sifat bilan 못 kelmaydi.</p>",
        "examples": [
            ("오늘은 학교에 안 가요.", "Bugun maktabga bormayman (xohlamayman)."),
            ("아파서 학교에 못 갔어요.", "Kasal bo'lganim uchun maktabga bora olmadim."),
        ],
        "synonyms": [
            ("-(으)ㄹ 수 없다", "-(으)ㄹ 수 없다 = «umuman imkonsiz» (kuchliroq); 못 = shu safar uddasidan chiqmadim"),
        ],
        "order": 502,
    },

    # ── MAJBURIYAT VA RUXSAT ───────────────────────────────────────────────
    {
        "pattern":   "-아야/어야 하다(되다)",
        "category":  "expression",
        "function":  "obligation",
        "level":     2,
        "freq":      3,
        "meaning":   "«-ish kerak, -ishi shart»",
        "attach":    "동사/형용사 + -아야/어야 하다",
        "form_rule": "ㅏ/ㅗ → <b>-아야 하다</b> · boshqa → <b>-어야 하다</b> · 하다 → <b>해야 하다</b><br>"
                     "<b>되다</b> og'zakiroq, <b>하다</b> rasmiyroq.",
        "note":      "<p>쓰기 54 xulosasi uchun oltin qolip: "
                     "<i>따라서 [주체]은/는 [행동]<b>해야 할 것이다</b>.</i></p>",
        "examples": [
            ("내일까지 보고서를 제출해야 합니다.", "Ertagacha hisobotni topshirishim kerak."),
            ("환경을 지키기 위해 모두가 노력해야 한다.", "Atrof-muhitni asrash uchun hamma harakat qilishi kerak."),
        ],
        "synonyms": [
            ("-(으)면 안 되다", "teskarisi — «qilish mumkin emas» (taqiq)"),
            ("-(으)ㄹ 필요가 있다", "-(으)ㄹ 필요가 있다 = «zarurat bor» (yumshoqroq); -아야 하다 = majburiyat"),
        ],
        "order": 510,
    },
    {
        "pattern":   "-아도/어도 되다",
        "category":  "expression",
        "function":  "obligation",
        "level":     2,
        "freq":      2,
        "meaning":   "«-sa bo'ladi, mumkin» — ruxsat",
        "attach":    "동사 + -아도/어도 되다",
        "form_rule": "되다 o'rniga <b>괜찮다, 좋다</b> ham kelishi mumkin: 가<b>도 괜찮아요</b>.",
        "note":      "<p>Ruxsat so'rash: <i>여기 앉<b>아도 돼요</b>?</i> — Bu yerga o'tirsam bo'ladimi?</p>",
        "examples": [
            ("여기에서 사진을 찍어도 돼요?", "Bu yerda surat olsam bo'ladimi?"),
            ("시간이 없으면 안 와도 됩니다.", "Vaqtingiz bo'lmasa kelmasangiz ham bo'ladi."),
        ],
        "synonyms": [
            ("-(으)면 안 되다", "teskarisi — ruxsat berilmaydi"),
            ("-(으)ㄹ 수 있다", "-(으)ㄹ 수 있다 = imkoniyat bor; -아도 되다 = ruxsat berilgan"),
        ],
        "order": 511,
    },
    {
        "pattern":   "-(으)면 안 되다",
        "category":  "expression",
        "function":  "obligation",
        "level":     2,
        "freq":      3,
        "meaning":   "«-sa bo'lmaydi, mumkin emas» — taqiq",
        "attach":    "동사/형용사 + -(으)면 안 되다",
        "form_rule": "받침 yo'q → <b>-면 안 되다</b> · 받침 bor → <b>-으면 안 되다</b>",
        "note":      "<p>E'lon va qoidalarda ko'p uchraydi — TOPIK 읽기 안내문 savollari.</p>"
                     "<p>⚠️ «안 -(으)면 안 되다» = ikki inkor = <b>majburiyat</b>: "
                     "<i>가지 않<b>으면 안 돼요</b></i> = borish shart.</p>",
        "examples": [
            ("도서관에서 큰 소리로 말하면 안 됩니다.", "Kutubxonada baland ovozda gapirish mumkin emas."),
            ("여기에 주차하면 안 돼요.", "Bu yerga mashina qo'yish mumkin emas."),
        ],
        "synonyms": [
            ("-지 마세요", "-지 마세요 = to'g'ridan-to'g'ri buyruq; -(으)면 안 되다 = qoida bayoni"),
            ("-아도 되다", "teskarisi — ruxsat"),
        ],
        "order": 512,
    },
    {
        "pattern":   "-(으)ㄹ 필요가 있다/없다",
        "category":  "expression",
        "function":  "obligation",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ish zarur / shart emas»",
        "attach":    "동사 + -(으)ㄹ 필요가 있다/없다",
        "form_rule": "Ot bilan: 준비<b>가 필요하다</b>.",
        "note":      "<p>쓰기 54 taklif qismida ko'p ishlatiladi: "
                     "<i>이를 위해 제도적 지원<b>이 필요하다</b>.</i></p>",
        "examples": [
            ("서두를 필요가 없어요. 시간이 많아요.", "Shoshilish shart emas. Vaqt ko'p."),
            ("이 문제를 다시 검토할 필요가 있다.", "Bu masalani qayta ko'rib chiqish zarur."),
        ],
        "synonyms": [
            ("-아야 하다", "-아야 하다 = qat'iy majburiyat; -(으)ㄹ 필요가 있다 = zarurat, yumshoqroq"),
        ],
        "order": 513,
    },

    # ── TAJRIBA, ODAT, URINISH ─────────────────────────────────────────────
    {
        "pattern":   "-(으)ㄴ 적이 있다/없다",
        "category":  "expression",
        "function":  "experience",
        "level":     2,
        "freq":      3,
        "meaning":   "«-gan bor / -gan emas» — tajriba",
        "attach":    "동사 + -(으)ㄴ 적이 있다/없다",
        "form_rule": "받침 yo'q → <b>-ㄴ 적이 있다</b> · 받침 bor → <b>-은 적이 있다</b><br>"
                     "적 o'rniga <b>일</b> ham: -(으)ㄴ 일이 있다",
        "note":      "<p><b>Bir marta bo'lsa ham boshdan kechirgan</b> narsa haqida. "
                     "Yaqin o'tmish uchun ishlatilmaydi.</p>",
        "mistake":   "<p>❌ 어제 김치를 먹<b>은 적이 있어요</b> → ✅ 어제 김치를 <b>먹었어요</b>. "
                     "Kecha bo'lgan ish — tajriba emas.</p>",
        "examples": [
            ("한국에 가 본 적이 있어요?", "Koreyaga borganmisiz?"),
            ("이런 일은 한 번도 경험한 적이 없다.", "Bunday narsani hech qachon boshdan kechirmaganman."),
        ],
        "synonyms": [
            ("-아/어 보다", "-아 보다 = «qilib ko'rmoq» (urinish); -(으)ㄴ 적이 있다 = tajriba bor/yo'q"),
        ],
        "order": 520,
    },
    {
        "pattern":   "-아/어 보다",
        "category":  "expression",
        "function":  "experience",
        "level":     1,
        "freq":      3,
        "meaning":   "«-b ko'rmoq» — sinab ko'rish",
        "attach":    "동사 + -아/어 보다",
        "form_rule": "O'tgan zamon <b>-아/어 봤다</b> = «qilib ko'rganman» (tajriba)<br>"
                     "Buyruq <b>-아/어 보세요</b> = «qilib ko'ring» (tavsiya)",
        "note":      "<p>⚠️ 보다 fe'lining o'zi bilan qo'shilmaydi: ❌ 봐 보다.</p>",
        "examples": [
            ("이 옷을 입어 보세요.", "Bu kiyimni kiyib ko'ring."),
            ("김치찌개를 만들어 봤는데 맛있었어요.", "Kimchi jjigae qilib ko'rdim — mazali chiqdi."),
        ],
        "synonyms": [
            ("-(으)ㄴ 적이 있다", "-(으)ㄴ 적이 있다 = tajriba borligini aytadi; -아 봤다 = «sinab ko'rdim»"),
        ],
        "order": 521,
    },
    {
        "pattern":   "-아/어 주다(드리다)",
        "category":  "expression",
        "function":  "politeness",
        "level":     1,
        "freq":      3,
        "meaning":   "«-b bermoq» — birov uchun qilish",
        "attach":    "동사 + -아/어 주다 · (hurmat) -아/어 드리다",
        "form_rule": "Kattaga qilinsa → <b>-아/어 드리다</b>: 도와<b>드릴게요</b>.<br>"
                     "Iltimos: <b>-아/어 주세요 / -아 주시겠어요?</b>",
        "note":      "<p>Iltimos darajalari: 해 <b>줘</b> (do'st) &lt; 해 <b>주세요</b> &lt; "
                     "해 <b>주시겠어요?</b> &lt; 해 <b>주시면 감사하겠습니다</b> (eng muloyim).</p>",
        "examples": [
            ("사진 좀 찍어 주세요.", "Iltimos, surat olib bering."),
            ("제가 짐을 들어 드릴게요.", "Yukingizni ko'tarib beray."),
        ],
        "synonyms": [
            ("-(으)세요", "-(으)세요 = oddiy ko'rsatma; -아 주세요 = «men uchun qiling» degan iltimos"),
        ],
        "order": 522,
    },
    {
        "pattern":   "-기로 하다",
        "category":  "expression",
        "function":  "intention",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ishga qaror qilmoq / kelishmoq»",
        "attach":    "동사 + -기로 하다",
        "form_rule": "Kelishuv ma'nosida: <b>-기로 했다/약속했다/결정했다</b>",
        "note":      "<p>Yakka qaror ham, ikki tomon kelishuvi ham bo'ladi: "
                     "<i>친구와 만나<b>기로 했어요</b></i> — do'stim bilan uchrashishga kelishdik.</p>",
        "examples": [
            ("내년부터 담배를 끊기로 했어요.", "Kelasi yildan chekishni tashlashga qaror qildim."),
            ("우리는 매주 토요일에 만나기로 했다.", "Biz har shanba uchrashishga kelishdik."),
        ],
        "synonyms": [
            ("-(으)려고 하다", "-(으)려고 하다 = niyat («-moqchiman»); -기로 하다 = qaror qabul qilingan"),
            ("-(으)ㄹ까 하다", "-(으)ㄹ까 하다 = «qilsammikin» (hali aniq emas)"),
        ],
        "order": 523,
    },
    {
        "pattern":   "-고 싶다",
        "category":  "expression",
        "function":  "intention",
        "level":     1,
        "freq":      3,
        "meaning":   "«-gim keladi, xohlayman»",
        "attach":    "동사 + -고 싶다",
        "form_rule": "1-2 shaxs uchun <b>-고 싶다</b> · 3-shaxs uchun <b>-고 싶어 하다</b>",
        "note":      "<p>⚠️ Uchinchi shaxs haqida gapirganda shakl o'zgaradi: "
                     "<i>아프소나는 한국에 가<b>고 싶어 해요</b>.</i></p>",
        "mistake":   "<p>❌ 동생이 아이스크림을 먹<b>고 싶어요</b> → ✅ 동생이 아이스크림을 "
                     "먹<b>고 싶어 해요</b>.</p>",
        "examples": [
            ("저는 한국에서 공부하고 싶어요.", "Men Koreyada o'qishni istayman."),
            ("자수르는 의사가 되고 싶어 한다.", "Jasur shifokor bo'lishni istaydi."),
        ],
        "synonyms": [
            ("-(으)ㄹ래요", "-(으)ㄹ래요 = qaror va e'lon; -고 싶다 = ichki xohish"),
            ("-았/었으면 좋겠다", "-았으면 좋겠다 = «bo'lsa edi» (orzu, ehtimol amalga oshmaydi)"),
        ],
        "order": 524,
    },
    {
        "pattern":   "-았/었으면 좋겠다",
        "category":  "expression",
        "function":  "intention",
        "level":     3,
        "freq":      2,
        "meaning":   "«-sa edi, -ishini istardim» — orzu",
        "attach":    "동사/형용사 + -았/었으면 좋겠다",
        "form_rule": "<b>-(으)면 좋겠다</b> shakli ham to'g'ri; -았/었- qo'shilsa orzu kuchliroq bo'ladi.",
        "note":      "<p>Amalga oshishi noaniq yoki qiyin narsa haqida — muloyim iltimos sifatida ham: "
                     "<i>조용히 해 주<b>셨으면 좋겠어요</b>.</i></p>",
        "examples": [
            ("내일 날씨가 좋았으면 좋겠어요.", "Ertaga ob-havo yaxshi bo'lsa edi."),
            ("시험에 꼭 합격했으면 좋겠다.", "Imtihondan albatta o'tsam edi."),
        ],
        "synonyms": [
            ("-고 싶다", "-고 싶다 = o'zim qiladigan ish; -았으면 좋겠다 = mendan tashqaridagi orzu"),
        ],
        "order": 525,
    },

    # ── TAXMIN ─────────────────────────────────────────────────────────────
    {
        "pattern":   "-(으)ㄴ/는 것 같다",
        "category":  "expression",
        "function":  "guess",
        "level":     2,
        "freq":      3,
        "meaning":   "«-ga o'xshaydi, shekilli» — taxmin",
        "attach":    "동사 + -는 것 같다 · 형용사 + -(으)ㄴ 것 같다 · 과거 + -(으)ㄴ 것 같다",
        "form_rule": "Hozirgi fe'l → <b>-는 것 같다</b> · Sifat → <b>-(으)ㄴ 것 같다</b><br>"
                     "O'tgan → <b>-(으)ㄴ 것 같다</b> · Kelasi/taxmin → <b>-(으)ㄹ 것 같다</b>",
        "note":      "<p>Fikrni <b>yumshatish</b> uchun ham ishlatiladi — koreyslar qat'iy gapirmaslik "
                     "uchun ko'p qo'llaydi: <i>이 옷이 좀 비싼 <b>것 같아요</b>.</i></p>",
        "examples": [
            ("밖에 비가 오는 것 같아요.", "Tashqarida yomg'ir yog'ayotganga o'xshaydi."),
            ("이번 시험은 어려울 것 같다.", "Bu safargi imtihon qiyin bo'lsa kerak."),
        ],
        "synonyms": [
            ("-나 보다", "-나 보다 = ko'rgan DALILga asoslangan taxmin; -는 것 같다 = umumiy his"),
            ("-(으)ㄹ 것이다", "-(으)ㄹ 것이다 = ishonchli bashorat; -는 것 같다 = ehtiyotkor taxmin"),
        ],
        "order": 530,
    },
    {
        "pattern":   "-나 보다 / -(으)ㄴ가 보다",
        "category":  "expression",
        "function":  "guess",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ganga o'xshaydi» — dalilga asoslangan taxmin",
        "attach":    "동사 + -나 보다 · 형용사 + -(으)ㄴ가 보다",
        "form_rule": "Fe'l → <b>-나 보다</b> (가나 보다) · Sifat → <b>-(으)ㄴ가 보다</b> (추운가 보다)<br>"
                     "O'tgan → <b>-았/었나 보다</b>",
        "note":      "<p>Biror <b>belgini ko'rib</b> xulosa chiqarish: "
                     "<i>불이 꺼졌네요. 자<b>나 봐요</b>.</i> — Chiroq o'chdi. Uxlayotganga o'xshaydi.</p>"
                     "<p>⚠️ O'zingiz haqingizda ishlatilmaydi.</p>",
        "examples": [
            ("사람들이 우산을 쓰네요. 비가 오나 봐요.", "Odamlar soyabon ko'tarib yuribdi. Yomg'ir yog'ayotganga o'xshaydi."),
            ("불이 꺼진 걸 보니 아무도 없나 보다.", "Chiroq o'chganiga qaraganda, hech kim yo'qqa o'xshaydi."),
        ],
        "synonyms": [
            ("-는 것 같다", "-는 것 같다 = o'zim haqimda ham bo'ladi; -나 보다 = faqat boshqa haqida, dalil bilan"),
            ("-(으)ㄴ/는 모양이다", "-는 모양이다 = deyarli bir xil, biroz rasmiyroq"),
        ],
        "order": 531,
    },
    {
        "pattern":   "-(으)ㄹ 것 같다",
        "category":  "expression",
        "function":  "guess",
        "level":     2,
        "freq":      3,
        "meaning":   "«-adiganga o'xshaydi» — kelajakka taxmin",
        "attach":    "동사/형용사 + -(으)ㄹ 것 같다",
        "form_rule": "받침 yo'q → <b>-ㄹ 것 같다</b> · 받침 bor → <b>-을 것 같다</b>",
        "note":      "<p>Rad javobini yumshatishning eng ko'p ishlatiladigan usuli: "
                     "<i>내일은 좀 어려울 <b>것 같아요</b>.</i> — Ertaga biroz qiyin bo'lsa kerak "
                     "(= bora olmayman).</p>",
        "examples": [
            ("오후에 눈이 올 것 같아요.", "Tushdan keyin qor yog'sa kerak."),
            ("이 일은 시간이 오래 걸릴 것 같다.", "Bu ish uzoq vaqt olsa kerak."),
        ],
        "synonyms": [
            ("-겠-", "-겠- = ishonchliroq, darhol chiqarilgan xulosa; -(으)ㄹ 것 같다 = ehtiyotkor"),
        ],
        "order": 532,
    },
    {
        "pattern":   "-(으)ㄹ 뻔하다",
        "category":  "expression",
        "function":  "guess",
        "level":     4,
        "freq":      2,
        "meaning":   "«-ayozdi, sal bo'lmasa -ardi»",
        "attach":    "동사 + -(으)ㄹ 뻔하다",
        "form_rule": "Deyarli doim <b>o'tgan zamon</b>da: <b>-(으)ㄹ 뻔했다</b>.",
        "note":      "<p>Bo'lishiga oz qolgan, lekin <b>bo'lmagan</b> — odatda yomon narsa.</p>",
        "examples": [
            ("길이 미끄러워서 넘어질 뻔했어요.", "Yo'l sirpanchiq bo'lgani uchun yiqilayozdim."),
            ("하마터면 지갑을 잃어버릴 뻔했다.", "Sal bo'lmasa hamyonimni yo'qotayozdim."),
        ],
        "synonyms": [
            ("-(으)ㄹ 지경이다", "-(으)ㄹ 지경이다 = «shu darajaga yetdi» (davom etayotgan og'ir holat)"),
        ],
        "order": 533,
    },

    # ── DARAJA VA BAHO ─────────────────────────────────────────────────────
    {
        "pattern":   "-(으)ㄴ/는 편이다",
        "category":  "expression",
        "function":  "degree",
        "level":     3,
        "freq":      3,
        "meaning":   "«-roq, ancha ... hisoblanadi» — yumshoq baho",
        "attach":    "동사 + -는 편이다 · 형용사 + -(으)ㄴ 편이다",
        "form_rule": "Fe'l → <b>-는 편이다</b> · Sifat 받침 yo'q → <b>-ㄴ 편이다</b> · 받침 bor → <b>-은 편이다</b>",
        "note":      "<p>Qat'iy aytmaslik uchun — «umuman olganda shunday tomonga moyil». "
                     "쓰기 53 da statistikani baholashda foydali.</p>",
        "examples": [
            ("저는 매운 음식을 잘 먹는 편이에요.", "Men achchiq ovqatni yaxshi yeyman (shunga moyilman)."),
            ("이 지역은 물가가 비싼 편이다.", "Bu hududda narxlar ancha qimmat hisoblanadi."),
        ],
        "synonyms": [
            ("-(으)ㄴ/는 셈이다", "-는 셈이다 = «hisob-kitobda shunday chiqadi» (xulosa); -는 편이다 = moyillik"),
        ],
        "order": 540,
    },
    {
        "pattern":   "-(으)ㄹ 만하다",
        "category":  "expression",
        "function":  "degree",
        "level":     4,
        "freq":      2,
        "meaning":   "«-ishga arziydi, -sa bo'ladi»",
        "attach":    "동사 + -(으)ㄹ 만하다",
        "form_rule": "Aniqlovchi shakl: <b>-(으)ㄹ 만한 + 명사</b>",
        "note":      "<p>Ikki ma'no: <b>tavsiya</b> (가 볼 만한 곳 — borishga arziydigan joy) va "
                     "<b>chidasa bo'ladi</b> (참<b>을 만해요</b>).</p>",
        "examples": [
            ("이 영화는 한번 볼 만해요.", "Bu kinoni bir ko'rishga arziydi."),
            ("경주는 여행할 만한 도시이다.", "Gyeongju — sayohat qilishga arziydigan shahar."),
        ],
        "synonyms": [
            ("-(으)ㄹ 가치가 있다", "-(으)ㄹ 가치가 있다 = rasmiy «qimmatga ega»; -(으)ㄹ 만하다 = og'zaki tavsiya"),
        ],
        "order": 541,
    },
    {
        "pattern":   "-(으)ㄹ수록",
        "category":  "connective",
        "function":  "degree",
        "level":     4,
        "freq":      3,
        "meaning":   "«-gan sari, qanchalik ... shunchalik»",
        "attach":    "동사/형용사 + -(으)ㄹ수록",
        "form_rule": "Ko'pincha <b>-(으)면 -(으)ㄹ수록</b> juft shaklida: "
                     "보<b>면 볼수록</b> (ko'rgan sari).",
        "note":      "<p><b>쓰기 54 uchun kuchli qolip</b>: "
                     "<i>기술이 발전할<b>수록</b> 인간관계는 오히려 약해진다.</i></p>",
        "examples": [
            ("한국어는 공부할수록 재미있어져요.", "Koreys tili o'rgangan sari qiziqarli bo'lib boradi."),
            ("나이가 들수록 시간이 빨리 간다.", "Yosh o'tgan sari vaqt tez o'tadi."),
        ],
        "synonyms": [
            ("-(으)면 -(으)ㄹ수록", "kuchaytirilgan juft shakli — ma'nosi bir xil"),
        ],
        "order": 542,
    },
    {
        "pattern":   "-(으)ㄴ/는 대신에",
        "category":  "expression",
        "function":  "contrast",
        "level":     4,
        "freq":      2,
        "meaning":   "«-ning o'rniga, evaziga»",
        "attach":    "동사 + -는 대신에 · 형용사 + -(으)ㄴ 대신에 · 명사 + 대신에",
        "form_rule": "Ot bilan: 커피 <b>대신에</b> 차를 마셔요.",
        "note":      "<p>Ikki ma'no: <b>almashtirish</b> (A o'rniga B) va "
                     "<b>kompensatsiya</b> (A bor, buning evaziga B).</p>",
        "examples": [
            ("주말에 일하는 대신에 월요일에 쉬어요.", "Dam olish kuni ishlaganim evaziga dushanba dam olaman."),
            ("설탕 대신에 꿀을 넣었어요.", "Shakar o'rniga asal soldim."),
        ],
        "synonyms": [
            ("-는 반면에", "-는 반면에 = taqqoslash («aksincha»); -는 대신에 = almashtirish/evaz"),
        ],
        "order": 543,
    },
    {
        "pattern":   "-(으)ㄹ 테니까",
        "category":  "connective",
        "function":  "guess",
        "level":     4,
        "freq":      2,
        "meaning":   "«-aman shuning uchun / -sa kerak, shuning uchun»",
        "attach":    "동사/형용사 + -(으)ㄹ 테니까",
        "form_rule": "받침 yo'q → <b>-ㄹ 테니까</b> · 받침 bor → <b>-을 테니까</b>",
        "note":      "<p>Ikki ma'no: <b>1-shaxs niyati</b> (제가 준비할 <b>테니까</b> 걱정 마세요) va "
                     "<b>taxmin</b> (길이 막힐 <b>테니까</b> 일찍 나가세요). Ikkinchi qismda "
                     "buyruq/taklif keladi.</p>",
        "examples": [
            ("제가 도와드릴 테니까 걱정하지 마세요.", "Men yordam beraman, xavotir olmang."),
            ("주말에는 사람이 많을 테니까 평일에 갑시다.", "Dam olish kunlari odam ko'p bo'ladi, ish kunida boraylik."),
        ],
        "synonyms": [
            ("-(으)니까", "-(으)니까 = fakt sabab; -(으)ㄹ 테니까 = taxmin yoki va'da sabab"),
            ("-(으)ㄹ 텐데", "-(으)ㄹ 텐데 = «...-sa kerak-ku» (afsus/xavotir ohangi)"),
        ],
        "order": 544,
    },
    {
        "pattern":   "-는 중이다 / -는 길이다",
        "category":  "expression",
        "function":  "time",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ish jarayonida / yo'lida»",
        "attach":    "동사 + -는 중이다 · 가다/오다 + -는 길이다",
        "form_rule": "Ot bilan: 회의 <b>중이다</b>, 공사 <b>중</b><br>"
                     "<b>-는 길이다</b> faqat 가다/오다 bilan.",
        "note":      "<p><b>-는 중</b> = jarayon davom etyapti · <b>-는 길에</b> = «yo'l-yo'lakay»: "
                     "<i>학교에 가<b>는 길에</b> 빵을 샀어요.</i></p>",
        "examples": [
            ("지금 회의하는 중이에요.", "Hozir yig'ilish o'tkazyapmiz."),
            ("집에 오는 길에 마트에 들렀다.", "Uyga kelayotib do'konga kirdim."),
        ],
        "synonyms": [
            ("-고 있다", "-고 있다 = umumiy davomiylik; -는 중이다 = «aynan hozir jarayonda» ta'kidi"),
        ],
        "order": 545,
    },
    {
        "pattern":   "-기 쉽다/어렵다",
        "category":  "expression",
        "function":  "degree",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ishi oson / qiyin»",
        "attach":    "동사 + -기 쉽다 / -기 어렵다",
        "form_rule": "Shu oilaga: <b>-기 좋다, -기 나쁘다, -기 편하다, -기 힘들다, -기 바쁘다</b>.",
        "note":      "<p>«-기» fe'lni otga aylantiradi — TOPIK 읽기 da juda ko'p uchraydigan usul: "
                     "<i>읽<b>기</b>, 쓰<b>기</b>, 듣<b>기</b>, 말하<b>기</b>.</i></p>",
        "examples": [
            ("이 글씨는 읽기 어려워요.", "Bu yozuvni o'qish qiyin."),
            ("겨울에는 감기에 걸리기 쉽다.", "Qishda shamollash oson."),
        ],
        "synonyms": [
            ("-기가 힘들다", "deyarli bir xil — 힘들다 jismoniy/ruhiy qiynalishni ta'kidlaydi"),
        ],
        "order": 546,
    },
    {
        "pattern":   "-(으)ㄴ 지 (시간이) 되다",
        "category":  "expression",
        "function":  "time",
        "level":     3,
        "freq":      2,
        "meaning":   "«-ganiga (shuncha vaqt) bo'ldi»",
        "attach":    "동사 + -(으)ㄴ 지 + 기간 + 되다/지나다",
        "form_rule": "⚠️ Bu <b>지</b> — «-지 않다» dagi 지 emas. Ajratib yoziladi: 온 <b>지</b> 3년.",
        "note":      "<p>TOPIK 듣기 da yosh/muddat savollarida uchraydi: "
                     "<i>한국에 온 <b>지</b> 얼마나 됐어요?</i></p>",
        "examples": [
            ("한국어를 배운 지 2년이 됐어요.", "Koreys tilini o'rganayotganimga 2 yil bo'ldi."),
            ("이 회사에 다닌 지 오래되지 않았다.", "Bu kompaniyada ishlayotganimga ko'p bo'lgani yo'q."),
        ],
        "synonyms": [
            ("동안", "동안 = davomiylik («2 yil davomida»); -(으)ㄴ 지 = boshlangan nuqtadan hisob"),
        ],
        "order": 547,
    },
]
