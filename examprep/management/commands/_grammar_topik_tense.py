# -*- coding: utf-8 -*-
"""Grammar bank — 시제 (tense), 관형형 (modifiers), 피동·사동 (voice),
높임 (honorifics) and 인용 (quotation).

Order decade: 400-499. See STYLE_GUIDE_GRAMMAR.md.
"""

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

POINTS = [
    # ── ZAMON ──────────────────────────────────────────────────────────────
    {
        "pattern":   "-았/었-",
        "category":  "tense",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "meaning":   "o'tgan zamon — «-di, -gan»",
        "attach":    "동사/형용사 + -았/었-",
        "form_rule": "Oxirgi unli ㅏ/ㅗ → <b>-았-</b> (가다 → 갔다) · boshqa → <b>-었-</b> (먹다 → 먹었다) · "
                     "하다 → <b>했다</b><br>Ot: 학생<b>이었다</b> / 친구<b>였다</b>",
        "note":      "<p>Sifat bilan ham qo'llanadi: 예쁘다 → <b>예뻤다</b>.</p>"
                     "<p>Ba'zi fe'llar bilan <b>hozirgi holat</b>ni bildiradi: "
                     "<i>결혼<b>했어요</b></i> (uylanganman — hozir), <i>앉<b>았어요</b></i> (o'tirganman).</p>",
        "examples": [
            ("어제 도서관에서 공부했어요.", "Kecha kutubxonada o'qidim."),
            ("작년에는 물가가 지금보다 쌌다.", "O'tgan yili narxlar hozirgidan arzon edi."),
        ],
        "synonyms": [
            ("-았었/었었-", "-았었- = «bir vaqtlar shunday edi, endi emas» — uzoq o'tmish va uzilish"),
        ],
        "order": 400,
    },
    {
        "pattern":   "-았었/었었-",
        "category":  "tense",
        "function":  "time",
        "level":     4,
        "freq":      1,
        "meaning":   "uzoq o'tmish — «bir vaqtlar shunday edi (endi emas)»",
        "attach":    "동사/형용사 + -았었/었었-",
        "form_rule": "-았/었- ustiga yana 었 qo'shiladi: 가다 → <b>갔었다</b>, 먹다 → <b>먹었었다</b>",
        "note":      "<p>Hozirgi holat bilan <b>aloqasi uzilgan</b>ini ta'kidlaydi: "
                     "<i>서울에 살<b>았었어요</b></i> — ilgari Seulda yashardim (endi yo'q).</p>",
        "examples": [
            ("어릴 때는 키가 작았었어요.", "Kichkinaligimda bo'yim past edi."),
            ("그 식당에 자주 갔었는데 지금은 문을 닫았다.", "O'sha restoranga tez-tez borardim, endi yopilgan."),
        ],
        "synonyms": [
            ("-았/었-", "-았/었- = oddiy o'tgan zamon; -았었- = «endi bunday emas» ta'kidi"),
            ("-던", "-던 = o'tmishdagi odat/tugallanmagan ish (aniqlovchi shakl)"),
        ],
        "order": 401,
    },
    {
        "pattern":   "-겠-",
        "category":  "tense",
        "function":  "guess",
        "level":     2,
        "freq":      3,
        "meaning":   "qat'iy niyat yoki hozirgi taxmin",
        "attach":    "동사/형용사 + -겠-",
        "form_rule": "받침ga qaramay <b>-겠-</b>: 가<b>겠</b>습니다, 춥<b>겠</b>어요<br>"
                     "O'tganga taxmin: <b>-았/었겠-</b> (힘들었겠어요)",
        "note":      "<p>Uch ma'no:</p><ul>"
                     "<li><b>Niyat</b> (1-shaxs): 제가 하<b>겠</b>습니다 — men qilaman.</li>"
                     "<li><b>Taxmin</b> (hozirgi holat haqida): 배고프<b>겠</b>어요 — och qolgandirsiz.</li>"
                     "<li><b>Muloyimlik qolipi</b>: 알<b>겠</b>습니다, 모르<b>겠</b>어요, 처음 뵙<b>겠</b>습니다.</li></ul>",
        "examples": [
            ("제가 먼저 발표하겠습니다.", "Men birinchi bo'lib chiqaman."),
            ("하루 종일 일했으니 피곤하겠어요.", "Kun bo'yi ishlagansiz, charchagandirsiz."),
        ],
        "synonyms": [
            ("-(으)ㄹ 거예요", "-(으)ㄹ 거예요 = reja/kelajak; -겠- = qat'iy niyat yoki hozirgi taxmin"),
            ("-(으)ㄹ 것 같다", "-(으)ㄹ 것 같다 = yumshoq taxmin («shekilli»); -겠- = ishonchliroq taxmin"),
        ],
        "order": 402,
    },
    {
        "pattern":   "-고 있다",
        "category":  "expression",
        "function":  "time",
        "level":     1,
        "freq":      3,
        "meaning":   "«-yapti» — davom etayotgan harakat",
        "attach":    "동사 + -고 있다",
        "form_rule": "Hurmat shakli: <b>-고 계시다</b> (선생님이 오<b>고 계세요</b>)",
        "note":      "<p>Kiyim fe'llari bilan <b>holat</b>ni ham bildiradi: "
                     "<i>안경을 쓰<b>고 있어요</b></i> — ko'zoynak taqib yurgan.</p>",
        "mistake":   "<p>❌ 문이 열리<b>고 있어요</b> (eshik ochilib turibdi) → ✅ 문이 열<b>려 있어요</b>. "
                     "Holat uchun -아/어 있다.</p>",
        "examples": [
            ("지금 숙제를 하고 있어요.", "Hozir uy vazifasini qilyapman."),
            ("최근 청년 실업이 증가하고 있다.", "So'nggi paytlarda yoshlar ishsizligi ortib bormoqda."),
        ],
        "synonyms": [
            ("-아/어 있다", "-고 있다 = harakat davom etyapti; -아 있다 = harakat tugagach qolgan HOLAT"),
            ("-는 중이다", "-는 중이다 = «...-ish jarayonida» — biroz rasmiyroq"),
        ],
        "order": 403,
    },
    {
        "pattern":   "-아/어 있다",
        "category":  "expression",
        "function":  "change",
        "level":     3,
        "freq":      2,
        "meaning":   "«-gan holda turibdi» — harakat natijasidagi holat",
        "attach":    "자동사 + -아/어 있다",
        "form_rule": "Faqat <b>o'timsiz fe'l</b> (자동사) bilan: 앉다, 서다, 눕다, 열리다, 켜지다.<br>"
                     "❌ 을/를 oladigan fe'l bilan ishlatilmaydi.",
        "note":      "<p>Harakat <b>tugagan</b>, natijasi <b>saqlanib turibdi</b>: "
                     "<i>의자에 앉<b>아 있어요</b></i> — o'tirgan holda.</p>",
        "examples": [
            ("창문이 열려 있어요.", "Deraza ochiq turibdi."),
            ("칠판에 이름이 적혀 있다.", "Doskada ism yozilgan turibdi."),
        ],
        "synonyms": [
            ("-고 있다", "-고 있다 = jarayon; -아 있다 = tugagan harakatning natijasi"),
        ],
        "order": 404,
    },

    # ── 관형형 (aniqlovchi shakllar) ───────────────────────────────────────
    {
        "pattern":   "-는 (동사 현재)",
        "category":  "modifier",
        "function":  "case",
        "level":     2,
        "freq":      3,
        "meaning":   "otni aniqlovchi hozirgi zamon — «-ayotgan»",
        "attach":    "동사 + -는 + 명사",
        "form_rule": "받침ga qaramay <b>-는</b>: 먹다 → 먹<b>는</b> 사람 · ㄹ tushadi: 살다 → <b>사는</b> 곳<br>"
                     "있다/없다 ham: 재미있<b>는</b> 책",
        "note":      "<p>Aniqlovchi shakllar TOPIK 읽기 ning asosidir. Uch zamon:</p>"
                     "<ul><li>O'tgan: 먹<b>은</b> 사람 (yegan)</li>"
                     "<li>Hozirgi: 먹<b>는</b> 사람 (yeyayotgan)</li>"
                     "<li>Kelasi: 먹<b>을</b> 사람 (yeydigan)</li></ul>",
        "examples": [
            ("한국어를 배우는 학생이 많아요.", "Koreys tilini o'rganayotgan talabalar ko'p."),
            ("제가 자주 가는 식당이에요.", "Bu men tez-tez boradigan restoran."),
        ],
        "synonyms": [
            ("-(으)ㄴ (동사 과거)", "-(으)ㄴ = tugagan harakat («yegan»); -는 = hozir davom etayotgan"),
            ("-(으)ㄹ", "-(으)ㄹ = hali bo'lmagan, kelajak yoki imkoniyat («yeydigan»)"),
        ],
        "order": 410,
    },
    {
        "pattern":   "-(으)ㄴ (과거·형용사)",
        "category":  "modifier",
        "function":  "case",
        "level":     2,
        "freq":      3,
        "meaning":   "fe'l uchun o'tgan zamon aniqlovchi; sifat uchun hozirgi",
        "attach":    "동사 + -(으)ㄴ + 명사 · 형용사 + -(으)ㄴ + 명사",
        "form_rule": "받침 yo'q → <b>-ㄴ</b> (가다 → 간 사람, 크다 → 큰 집) · "
                     "받침 bor → <b>-은</b> (먹다 → 먹은 밥, 좋다 → 좋은 사람)",
        "note":      "<p>Bir xil shakl <b>ikki xil vazifa</b> bajaradi — so'z turkumiga qarab:</p>"
                     "<ul><li>Fe'l + -(으)ㄴ = <b>o'tgan zamon</b>: 읽<b>은</b> 책 (o'qilgan kitob)</li>"
                     "<li>Sifat + -(으)ㄴ = <b>hozirgi</b>: 좋<b>은</b> 책 (yaxshi kitob)</li></ul>",
        "mistake":   "<p>❌ 재미있<b>은</b> 영화 → ✅ 재미있<b>는</b> 영화. "
                     "있다/없다 bilan tugagan sifatlar <b>-는</b> oladi.</p>",
        "examples": [
            ("어제 만난 사람이 누구예요?", "Kecha uchrashgan odam kim?"),
            ("조용한 곳에서 공부하고 싶어요.", "Tinch joyda o'qishni istayman."),
        ],
        "synonyms": [
            ("-는 (동사 현재)", "fe'l uchun: -(으)ㄴ = tugagan, -는 = davom etayotgan"),
            ("-던", "-던 = o'tmishdagi odat yoki tugallanmagan ish"),
        ],
        "order": 411,
    },
    {
        "pattern":   "-(으)ㄹ (미래·추측)",
        "category":  "modifier",
        "function":  "case",
        "level":     2,
        "freq":      3,
        "meaning":   "kelasi zamon aniqlovchi — «-adigan, -ajak»",
        "attach":    "동사/형용사 + -(으)ㄹ + 명사",
        "form_rule": "받침 yo'q → <b>-ㄹ</b> (가다 → 갈 사람) · 받침 bor → <b>-을</b> (먹다 → 먹을 것)",
        "note":      "<p>Ko'plab muhim iboralarning asosi: <b>-(으)ㄹ 것이다, -(으)ㄹ 수 있다, "
                     "-(으)ㄹ 때, -(으)ㄹ 줄 알다, -(으)ㄹ 뻔하다</b>.</p>",
        "examples": [
            ("내일 만날 사람이 있어요.", "Ertaga uchrashadigan odamim bor."),
            ("먹을 음식이 없어요.", "Yeydigan ovqat yo'q."),
        ],
        "synonyms": [
            ("-는 (동사 현재)", "-는 = hozir sodir bo'layotgan; -(으)ㄹ = hali bo'lmagan"),
        ],
        "order": 412,
    },
    {
        "pattern":   "-던 / -았/었던",
        "category":  "modifier",
        "function":  "time",
        "level":     4,
        "freq":      2,
        "meaning":   "«-ardi, -gan edi» — o'tmishdagi odat yoki tugallanmagan ish",
        "attach":    "동사/형용사 + -던 + 명사",
        "form_rule": "<b>-던</b> = takrorlangan yoki <b>tugallanmagan</b> ish (먹<b>던</b> 빵 — yeb tugatilmagan non)<br>"
                     "<b>-았/었던</b> = bir marta bo'lib <b>tugagan</b>, endi yo'q (먹<b>었던</b> 빵)",
        "note":      "<p>TOPIK 읽기 41-50 da tez-tez farqlanadi. Xotira ohangi bor: "
                     "<i>제가 다니<b>던</b> 학교</i> — men o'qigan (o'sha paytdagi) maktab.</p>",
        "examples": [
            ("어릴 때 자주 가던 공원이에요.", "Bolaligimda tez-tez boradigan bog'im."),
            ("읽던 책을 다시 펼쳤다.", "O'qib tugatmagan kitobimni yana ochdim."),
        ],
        "synonyms": [
            ("-(으)ㄴ (과거)", "-(으)ㄴ = shunchaki tugagan; -던 = takrorlangan odat yoki tugallanmagan"),
            ("-았었-", "-았었- = gap kesimida «endi bunday emas»; -던 = otni aniqlaydi"),
        ],
        "order": 413,
    },

    # ── PIYODA VA ORTTIRMA NISBAT ──────────────────────────────────────────
    {
        "pattern":   "-이/히/리/기- (피동)",
        "category":  "voice",
        "function":  "change",
        "level":     4,
        "freq":      3,
        "meaning":   "majhul nisbat — «-ildi, -indi»",
        "attach":    "동사 어간 + 이/히/리/기",
        "form_rule": "Har fe'lning o'z qo'shimchasi bor — <b>yodlash kerak</b>:<br>"
                     "<b>이</b>: 보다→보<b>이</b>다, 놓다→놓<b>이</b>다, 쓰다→쓰<b>이</b>다<br>"
                     "<b>히</b>: 먹다→먹<b>히</b>다, 잡다→잡<b>히</b>다, 닫다→닫<b>히</b>다<br>"
                     "<b>리</b>: 열다→열<b>리</b>다, 듣다→들<b>리</b>다, 팔다→팔<b>리</b>다<br>"
                     "<b>기</b>: 안다→안<b>기</b>다, 쫓다→쫓<b>기</b>다, 끊다→끊<b>기</b>다",
        "note":      "<p>Majhul gapda bajaruvchi <b>에게/에 의해</b> bilan ko'rsatiladi: "
                     "<i>쥐가 고양이<b>에게</b> 잡혔다.</i></p>"
                     "<p>쓰기 53 da statistika majhul shaklda beriladi: <i>조사가 실시<b>되었다</b>.</i></p>",
        "examples": [
            ("멀리서 산이 보여요.", "Uzoqdan tog' ko'rinadi."),
            ("이 책은 여러 나라에서 읽힌다.", "Bu kitob ko'p mamlakatlarda o'qiladi."),
        ],
        "synonyms": [
            ("-아/어지다", "-아지다 = har qanday fe'lga qo'shiladigan universal majhul/o'zgarish shakli"),
            ("-되다", "되다 = 하다 fe'llarining majhuli: 시작하다 → 시작되다"),
        ],
        "order": 420,
    },
    {
        "pattern":   "-아/어지다",
        "category":  "voice",
        "function":  "change",
        "level":     3,
        "freq":      3,
        "meaning":   "sifat bilan «-lashmoq»; fe'l bilan majhul",
        "attach":    "형용사/동사 + -아/어지다",
        "form_rule": "Sifat + -아/어지다 = <b>o'zgarish</b>: 좋다 → 좋<b>아지다</b> (yaxshilanmoq)<br>"
                     "Fe'l + -아/어지다 = <b>majhul</b>: 만들다 → 만들<b>어지다</b> (yasalmoq)",
        "note":      "<p><b>쓰기 53 uchun juda muhim</b> — grafikdagi o'zgarishni shu bilan yozasiz: "
                     "<i>많<b>아졌다</b>, 높<b>아졌다</b>, 심각해<b>졌다</b>.</i></p>",
        "examples": [
            ("한국어 실력이 좋아졌어요.", "Koreys tili saviyam yaxshilandi."),
            ("환경 문제가 점점 심각해지고 있다.", "Ekologiya muammosi tobora jiddiylashmoqda."),
        ],
        "synonyms": [
            ("-게 되다", "-게 되다 = tashqi sabab bilan holat o'zgardi; -아지다 = sifatning asta o'zgarishi"),
            ("-이/히/리/기-", "-이/히/리/기- = ma'lum fe'llarning o'z majhul shakli; -아지다 = universal"),
        ],
        "order": 421,
    },
    {
        "pattern":   "-게 하다 / -이/히/리/기/우- (사동)",
        "category":  "voice",
        "function":  "change",
        "level":     4,
        "freq":      2,
        "meaning":   "orttirma nisbat — «-tirmoq, qildirmoq»",
        "attach":    "동사 + -게 하다 · 동사 어간 + 이/히/리/기/우/추",
        "form_rule": "<b>-게 하다</b> = universal («qilishga majbur qilmoq»)<br>"
                     "Qo'shimchali shakllar: 먹다→먹<b>이</b>다, 앉다→앉<b>히</b>다, 울다→울<b>리</b>다, "
                     "웃다→웃<b>기</b>다, 자다→재<b>우</b>다, 늦다→늦<b>추</b>다",
        "note":      "<p><b>-게 하다</b> = majburlash/ruxsat · <b>-시키다</b> = 하다 fe'llari uchun: "
                     "공부하다 → 공부<b>시키다</b>.</p>",
        "examples": [
            ("어머니가 아이에게 밥을 먹였어요.", "Ona bolaga ovqat yedirdi."),
            ("선생님이 학생들을 조용히 하게 했다.", "O'qituvchi talabalarni jim qildirdi."),
        ],
        "synonyms": [
            ("-이/히/리/기- (피동)", "majhul = «menga qilindi»; orttirma = «men boshqaga qildirdim» — shakli o'xshash!"),
        ],
        "order": 422,
    },
    {
        "pattern":   "-게 되다",
        "category":  "expression",
        "function":  "change",
        "level":     3,
        "freq":      3,
        "meaning":   "«-adigan bo'lib qoldi» — tashqi sabab bilan o'zgarish",
        "attach":    "동사 + -게 되다",
        "form_rule": "받침ga qaramay <b>-게 되다</b>. O'tgan: <b>-게 되었다 / 됐다</b>.",
        "note":      "<p>Natija <b>mening irodamdan tashqarida</b> yuz bergan degan ohang. "
                     "Kamtarlik uchun ham ishlatiladi: <i>한국에 오<b>게 되었습니다</b>.</i></p>",
        "examples": [
            ("우연히 그 사실을 알게 되었어요.", "Tasodifan o'sha haqiqatni bilib qoldim."),
            ("회사 사정으로 이사하게 됐다.", "Ish sharoiti tufayli ko'chishga to'g'ri keldi."),
        ],
        "synonyms": [
            ("-아/어지다", "-아지다 = sifatning asta-sekin o'zgarishi; -게 되다 = vaziyat/harakatning o'zgarishi"),
        ],
        "order": 423,
    },

    # ── HURMAT ─────────────────────────────────────────────────────────────
    {
        "pattern":   "-(으)시-",
        "category":  "honorific",
        "function":  "politeness",
        "level":     1,
        "freq":      3,
        "meaning":   "harakat egasiga hurmat qo'shimchasi",
        "attach":    "동사/형용사 어간 + -(으)시-",
        "form_rule": "받침 yo'q → <b>-시-</b> (가다 → 가세요) · 받침 bor → <b>-으시-</b> (읽다 → 읽으세요)<br>"
                     "Maxsus shakllar: 먹다 → <b>드시다/잡수시다</b>, 자다 → <b>주무시다</b>, "
                     "있다 → <b>계시다</b>, 말하다 → <b>말씀하시다</b>, 죽다 → <b>돌아가시다</b>",
        "note":      "<p>Hurmat <b>gap egasiga</b> qaratiladi. Ega bilan birga 께서 keladi: "
                     "<i>선생님<b>께서</b> 오<b>셨</b>습니다.</i></p>"
                     "<p>⚠️ O'zingiz haqingizda ishlatilmaydi: ❌ 저는 가<b>세요</b>.</p>",
        "mistake":   "<p>❌ 사장님, 자리에 <b>없으세요</b> → ✅ 사장님께서 <b>안 계세요</b>.</p>",
        "examples": [
            ("할아버지께서 신문을 읽으십니다.", "Bobom gazeta o'qiyaptilar."),
            ("교수님은 지금 연구실에 계세요.", "Professor hozir kabinetida."),
        ],
        "synonyms": [
            ("드리다/여쭙다", "-(으)시- = EGAni ulug'laydi; 드리다/여쭙다 = TINGLOVCHIni ulug'lab, o'zini pasaytiradi"),
        ],
        "order": 430,
    },
    {
        "pattern":   "드리다 / 여쭙다 / 뵙다",
        "category":  "honorific",
        "function":  "politeness",
        "level":     3,
        "freq":      2,
        "meaning":   "kamtarlik fe'llari — o'zini pasaytirib, tinglovchini ulug'lash",
        "attach":    "겸양어 (o'z harakati haqida)",
        "form_rule": "주다 → <b>드리다</b> · 묻다 → <b>여쭙다/여쭈다</b> · 만나다/보다 → <b>뵙다/뵈다</b> · "
                     "말하다 → <b>말씀드리다</b> · 데리고 가다 → <b>모시고 가다</b>",
        "note":      "<p>Bu fe'llar <b>mening harakatim</b> haqida — men o'zimni pasaytiraman. "
                     "-(으)시- esa <b>boshqaning harakati</b>ga qo'shiladi.</p>",
        "examples": [
            ("선생님께 선물을 드렸습니다.", "Ustozga sovg'a berdim."),
            ("처음 뵙겠습니다.", "Tanishganimdan xursandman (birinchi ko'rishuv)."),
        ],
        "synonyms": [
            ("-(으)시-", "-(으)시- = boshqaning harakatiga; 드리다 = mening harakatimga"),
        ],
        "order": 431,
    },

    # ── KO'CHIRMA GAP ──────────────────────────────────────────────────────
    {
        "pattern":   "-다고 하다 (평서문 인용)",
        "category":  "quotation",
        "function":  "quote",
        "level":     3,
        "freq":      3,
        "meaning":   "«...-deydi, ...-degan ekan» — xabarni ko'chirish",
        "attach":    "동사 + -는다고/-ㄴ다고 하다 · 형용사 + -다고 하다 · 명사 + (이)라고 하다",
        "form_rule": "Fe'l 받침 bor → <b>-는다고</b> (먹는다고) · 받침 yo'q → <b>-ㄴ다고</b> (간다고)<br>"
                     "Sifat → <b>-다고</b> (춥다고) · O'tgan → <b>-았/었다고</b> · Ot → <b>(이)라고</b><br>"
                     "Qisqargan og'zaki shakl: <b>-대요</b> (간대요 = 간다고 해요)",
        "note":      "<p>TOPIK 듣기 va 읽기 da «u nima dedi?» savollari shu shaklda beriladi. "
                     "쓰기 53 da manba ko'rsatishda ham kerak: <i>조사에 따르면 ...<b>다고 한다</b>.</i></p>",
        "examples": [
            ("아프소나가 내일 온다고 했어요.", "Afsona ertaga kelaman dedi."),
            ("전문가들은 상황이 나아질 것이라고 전망한다.", "Mutaxassislar vaziyat yaxshilanadi deb bashorat qilmoqda."),
        ],
        "synonyms": [
            ("-냐고 하다", "so'roq gapni ko'chirish"),
            ("-라고 하다 (명령)", "buyruqni ko'chirish"),
            ("-자고 하다", "taklifni ko'chirish"),
        ],
        "order": 440,
    },
    {
        "pattern":   "-냐고 / -라고 / -자고 하다",
        "category":  "quotation",
        "function":  "quote",
        "level":     3,
        "freq":      3,
        "meaning":   "so'roq / buyruq / taklifni ko'chirish",
        "attach":    "동사 + -(느)냐고 · -(으)라고 · -자고 하다",
        "form_rule": "<b>So'roq</b>: 어디 가<b>냐고</b> 물었어요<br>"
                     "<b>Buyruq</b>: 조용히 하<b>라고</b> 했어요 (⚠️ 주다 → <b>달라고</b> / <b>주라고</b>)<br>"
                     "<b>Taklif</b>: 같이 가<b>자고</b> 했어요<br>"
                     "Qisqargan shakllar: <b>-냬요 / -래요 / -재요</b>",
        "note":      "<p>To'rt gap turi — to'rt qo'shimcha. TOPIK 듣기 da «남자가 여자에게 무엇을 "
                     "부탁했습니까?» savollari aynan shuni tekshiradi.</p>",
        "mistake":   "<p>«주다» ni ko'chirishda: menga bo'lsa <b>달라고</b>, boshqaga bo'lsa <b>주라고</b>. "
                     "❌ 나한테 주라고 했어요 → ✅ 나한테 <b>달라고</b> 했어요.</p>",
        "examples": [
            ("선생님이 숙제를 언제 내냐고 물으셨어요.", "O'qituvchi uy vazifasi qachon topshiriladi deb so'radi."),
            ("친구가 같이 영화를 보자고 했어요.", "Do'stim birga kino ko'raylik dedi."),
        ],
        "synonyms": [
            ("-다고 하다", "xabar gapini ko'chirish — shu oilaning asosiy a'zosi"),
        ],
        "order": 441,
    },
]
