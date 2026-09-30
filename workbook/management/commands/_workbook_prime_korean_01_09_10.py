"""Prime Korean workbooks — pilot batch: PK-1, PK-9, PK-10.

One Hangul lesson and two grammar lessons, so both families of task kinds
(letters and blocks · typed grammar) and the 원고지 worksheet are proven
before the course is filled in order from PK-2.

Guide: workbook/management/commands/STYLE_GUIDE_PK_WORKBOOK.md
Toc:   workbook/management/commands/toc_pk_workbook.txt
Import:
    python manage.py import_workbook workbook/management/commands/_workbook_prime_korean_01_09_10.py --author=prime --expect-items=107
"""

KEYBOARD = (
    "<p><strong>Boshlashdan oldin — koreys klaviaturasi.</strong> Telefon sozlamalarida "
    "<em>Til va klaviatura → Klaviatura qoʻshish → 한국어</em> ni tanlang va "
    "<strong>2벌식</strong> (iPhone'da <em>Standart</em>) tartibini oling. Kompyuterda: "
    "Windows — <em>Sozlamalar → Vaqt va til → Til → Til qoʻshish → 한국어</em>, "
    "almashtirish <em>Win + Space</em>, koreyscha yozish <em>한/영</em> yoki oʻng <em>Alt</em>.</p>"
    "<p>Qiziq tomoni: klaviatura sizning oʻrningizga blok yigʻadi. ㅎ, ㅏ, ㄴ ni ketma-ket "
    "bossangiz, ekranda <strong>한</strong> paydo boʻladi — xuddi darsdagidek.</p>"
)

WORKBOOKS = [
    # ══════════════════════════════════════════════════════════════════
    # PK-1 — Hangul bilan tanishuv
    # Taught so far: the idea of an alphabet, 14+10 letters by sight, the
    # five consonant shapes and the stroke-added ladders, vowel placement
    # (tall → right, flat → below), the block, silent initial ㅇ, and the
    # words 한국 · 한국어 · 한국 사람 · 한글. No grammar, so no section A.
    # ══════════════════════════════════════════════════════════════════
    {
        "tutorial": "PK-1: Hangul bilan tanishuv — dunyodagi eng mantiqiy alifbo",
        "intro": KEYBOARD,
        "tasks": [
            {
                "section": "B",
                "kind": "hangul",
                "title": "Harflardan blok yigʻing",
                "instruction": "<p>Harflarni bitta boʻgʻin blokiga yigʻib yozing. Koreys klaviaturasida harflarni ketma-ket bossangiz, blok oʻzi yigʻiladi.</p>",
                "items": [
                    {"stem": "ㅎ + ㅏ + ㄴ = ___", "answers": ["한"], "size": "s",
                     "explanation": "<p>Tik unli ㅏ undoshning oʻng tomoniga, yakuniy ㄴ (받침) esa pastga tushadi: <strong>한</strong>.</p>"},
                    {"stem": "ㄱ + ㅜ + ㄱ = ___", "answers": ["국"], "size": "s",
                     "explanation": "<p>Yotiq unli ㅜ undoshning tagiga yoziladi, 받침 ㄱ eng pastda: <strong>국</strong>.</p>"},
                    {"stem": "ㄱ + ㅏ = ___", "answers": ["가"], "size": "s",
                     "explanation": "<p>Ikki harf — 받침 yoʻq. Tik unli oʻngda: <strong>가</strong>.</p>"},
                    {"stem": "ㄱ + ㅗ = ___", "answers": ["고"], "size": "s",
                     "explanation": "<p>ㅗ yotiq unli, shuning uchun undosh tepada, unli pastda: <strong>고</strong>.</p>"},
                    {"stem": "ㅁ + ㅜ + ㄹ = ___", "answers": ["물"], "size": "s",
                     "explanation": "<p>ㅁ tepada, ㅜ uning tagida, ㄹ eng pastda: <strong>물</strong> (suv).</p>"},
                    {"stem": "ㅇ + ㅓ = ___", "answers": ["어"], "size": "s",
                     "explanation": "<p>Boshdagi ㅇ jim — u faqat «bu yerda unli bor» degan belgi. <strong>어</strong> = «o» ga yaqin tovush.</p>"},
                    {"stem": "ㄱ + ㅡ + ㄹ = ___", "answers": ["글"], "size": "s",
                     "explanation": "<p>ㅡ yotiq unli — undosh tagiga: <strong>글</strong> (yozuv). 한글 = «Hangul yozuvi».</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "pick",
                "title": "Unli qayerga yoziladi?",
                "instruction": "<p>Unlining shakliga qarang: tik chiziqli unli undoshning <strong>oʻngiga</strong>, yotiq chiziqli unli <strong>tagiga</strong> yoziladi.</p>",
                "items": [
                    {"stem": "ㅏ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["oʻng tomoniga"],
                     "explanation": "<p>ㅏ — tik chiziq (inson) va uning oʻngida qisqa chiziq. Tik unli: 가, 나, 하.</p>"},
                    {"stem": "ㅗ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["tagiga"],
                     "explanation": "<p>ㅗ — yotiq chiziq (yer) va ustida qisqa chiziq. Yotiq unli: 고, 노, 호.</p>"},
                    {"stem": "ㅓ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["oʻng tomoniga"],
                     "explanation": "<p>ㅓ ham tik unli, faqat qisqa chiziq chapda: 거, 너, 어.</p>"},
                    {"stem": "ㅜ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["tagiga"],
                     "explanation": "<p>ㅜ — yer ostida quyosh: yotiq unli. 구, 누, 무.</p>"},
                    {"stem": "ㅡ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["tagiga"],
                     "explanation": "<p>ㅡ — «yer», toza yotiq chiziq: 그, 느, 으.</p>"},
                    {"stem": "ㅣ — undoshning ___", "options": ["oʻng tomoniga", "tagiga"], "answers": ["oʻng tomoniga"],
                     "explanation": "<p>ㅣ — «inson», toza tik chiziq: 기, 니, 이.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "hangul",
                "title": "Blokni harflarga ajrating",
                "instruction": "<p>Blokni tashkil qilgan harflarni yozing. Harflar orasiga <strong>boʻsh joy yoki +</strong> qoʻying — aks holda klaviatura ularni yana blokka yigʻib yuboradi. Masalan: <strong>ㄱ ㅏ</strong>.</p>",
                "items": [
                    {"stem": "한 → ___", "answers": ["ㅎ ㅏ ㄴ"], "size": "m",
                     "explanation": "<p>한 = ㅎ + ㅏ + ㄴ. Bosh undosh, unli, 받침 — uchta joy.</p>"},
                    {"stem": "국 → ___", "answers": ["ㄱ ㅜ ㄱ"], "size": "m",
                     "explanation": "<p>국 = ㄱ + ㅜ + ㄱ. Bir xil harf ham boshda, ham 받침 boʻla oladi.</p>"},
                    {"stem": "어 → ___", "answers": ["ㅇ ㅓ"], "size": "m",
                     "explanation": "<p>어 = ㅇ + ㅓ. Jim ㅇ ham harf — uni tashlab ketmang.</p>"},
                    {"stem": "곰 → ___", "answers": ["ㄱ ㅗ ㅁ"], "size": "m",
                     "explanation": "<p>곰 = ㄱ + ㅗ + ㅁ (ayiq). Yotiq ㅗ tufayli uchala harf ustma-ust turadi.</p>"},
                    {"stem": "사 → ___", "answers": ["ㅅ ㅏ"], "size": "m",
                     "explanation": "<p>사 = ㅅ + ㅏ. 받침 yoʻq — ikki harf.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "pick",
                "title": "Jim ㅇ yoki «ng»?",
                "instruction": "<p>Qalin harf bilan belgilangan ㅇ qanday oʻqiladi? Boshda — jim, 받침 boʻlsa — «ng».</p>",
                "items": [
                    {"stem": "<strong>ㅇ</strong>ㅏ (아) — ___", "options": ["jim", "ng"], "answers": ["jim"],
                     "explanation": "<p>Boʻgʻin boshidagi ㅇ tovush bermaydi: 아 = «a».</p>"},
                    {"stem": "가<strong>ㅇ</strong> (강) — ___", "options": ["jim", "ng"], "answers": ["ng"],
                     "explanation": "<p>ㅇ 받침 oʻrnida — «ng»: 강 = «kang».</p>"},
                    {"stem": "<strong>ㅇ</strong>ㅗ (오) — ___", "options": ["jim", "ng"], "answers": ["jim"],
                     "explanation": "<p>Boshda — jim: 오 = «o».</p>"},
                    {"stem": "고<strong>ㅇ</strong> (공) — ___", "options": ["jim", "ng"], "answers": ["ng"],
                     "explanation": "<p>Pastda, 받침: 공 = «kong».</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "pick",
                "title": "Harf zinapoyasi",
                "instruction": "<p>Undoshga bitta chiziq qoʻshilsa, tovushga nafas qoʻshiladi. Zinapoyaning keyingi pogʻonasini tanlang.</p>",
                "items": [
                    {"stem": "ㄱ → ___", "options": ["ㅋ", "ㄷ", "ㅌ"], "answers": ["ㅋ"],
                     "explanation": "<p>ㄱ ustiga bitta chiziq — nafasli <strong>ㅋ</strong>.</p>"},
                    {"stem": "ㄴ → ㄷ → ___", "options": ["ㅌ", "ㄹ", "ㅋ"], "answers": ["ㅌ"],
                     "explanation": "<p>Til uchi zinapoyasi: ㄴ → ㄷ → <strong>ㅌ</strong>.</p>"},
                    {"stem": "ㅁ → ㅂ → ___", "options": ["ㅍ", "ㅎ", "ㅊ"], "answers": ["ㅍ"],
                     "explanation": "<p>Lab zinapoyasi: ㅁ → ㅂ → <strong>ㅍ</strong>.</p>"},
                    {"stem": "ㅅ → ㅈ → ___", "options": ["ㅊ", "ㅌ", "ㅎ"], "answers": ["ㅊ"],
                     "explanation": "<p>Tish zinapoyasi: ㅅ → ㅈ → <strong>ㅊ</strong>.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "hangul",
                "title": "Butun soʻzni yigʻing",
                "stars": 2,
                "instruction": "<p>Harflar qatorda berilgan — ularni bloklarga yigʻib, soʻzni yozing. Qayerda yangi blok boshlanishini oʻzingiz toping.</p>",
                "items": [
                    {"stem": "ㅎㅏㄴㄱㅜㄱ → ___", "answers": ["한국"], "size": "m",
                     "explanation": "<p>ㅎㅏㄴ + ㄱㅜㄱ = <strong>한국</strong> (Koreya). Ikki unli bor — demak ikki blok.</p>"},
                    {"stem": "ㅎㅏㄴㄱㅡㄹ → ___", "answers": ["한글"], "size": "m",
                     "explanation": "<p>ㅎㅏㄴ + ㄱㅡㄹ = <strong>한글</strong> — Hangul yozuvi.</p>"},
                    {"stem": "ㅎㅏㄴㄱㅜㄱㅇㅓ → ___", "answers": ["한국어"], "size": "m",
                     "explanation": "<p>Uchta unli (ㅏ ㅜ ㅓ) — uchta blok: <strong>한국어</strong>, koreys tili.</p>"},
                    {"stem": "ㅅㅏㄹㅏㅁ → ___", "answers": ["사람"], "size": "m",
                     "explanation": "<p>Tuzoq shu yerda: ㄹ ikki unli orasida turibdi, shuning uchun u keyingi blokni <em>ochadi</em>: 사 + 람 = <strong>사람</strong>. 「살암」 emas.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "translate",
                "title": "Koreyscha yozing",
                "stars": 2,
                "instruction": "<p>Darsdagi soʻzlarni Hangulda yozing.</p>",
                "items": [
                    {"stem": "Koreya", "answers": ["한국"], "size": "m",
                     "explanation": "<p><strong>한국</strong> — 한 + 국.</p>"},
                    {"stem": "koreys tili", "answers": ["한국어"], "size": "m",
                     "explanation": "<p><strong>한국어</strong> — oxiriga 어 («til») qoʻshildi.</p>"},
                    {"stem": "koreys (odam)", "answers": ["한국 사람"], "size": "m",
                     "explanation": "<p><strong>한국 사람</strong> — «Koreya odami». Ikki soʻz orasida boʻshliq bor.</p>"},
                ],
            },
            {
                "section": "D",
                "kind": "copy",
                "title": "Qoʻlda yozing",
                "instruction": "<p>Daftarga har bir blokni 5 martadan yozing. Blok <strong>kvadrat</strong> ichiga sigʻishi kerak: tik unli bilan — yonma-yon, yotiq unli bilan — ustma-ust. Chop etiladigan varaqda buning uchun katakchalar bor.</p>",
                "items": [
                    {"stem": "", "words": ["한", "국", "어", "글", "사", "람"]},
                ],
            },
            {
                "section": "D",
                "kind": "write",
                "title": "Oʻz soʻzlaringiz bilan",
                "instruction": "<p>Bu safar koreyscha emas — <strong>oʻzbekcha</strong> yozing. Biror narsani boshqaga tushuntira olsangiz, demak uni haqiqatan tushungansiz.</p>",
                "items": [
                    {"stem": "<p>Kichik ukangiz soʻradi: «Koreyslar rasm bilan yozadimi?» Unga 3–4 gapda Hangul nima ekanini tushuntiring.</p>",
                     "checklist": [
                         "Hangul — alifbo, har bir harf bir tovush ekanini aytdim",
                         "Harflar kvadrat blokka yigʻilishini misol bilan koʻrsatdim (masalan, 한 = ㅎ+ㅏ+ㄴ)",
                         "Iyeroglifdan farqini aytdim: koʻrmagan soʻzni ham oʻqish mumkin",
                     ],
                     "model_answer": "<p>Yoʻq, bu rasm emas — Hangul bizning alifbomizga oʻxshagan alifbo. Unda 24 ta asosiy harf bor va har biri bitta tovushni bildiradi. Faqat harflar qatorga emas, kvadrat blokka yigʻiladi: ㅎ, ㅏ va ㄴ birga 한 boʻladi. Shuning uchun harflarni bilsang, hech koʻrmagan soʻzni ham oʻqiy olasan.</p>"},
                ],
            },
            {
                "section": "E",
                "kind": "mission",
                "title": "Missiya",
                "instruction": "<p>Bugun darsdan tashqarida qiling.</p>",
                "items": [
                    {"stem": "<p>📱 Telefoningizga koreys klaviaturasini qoʻshing va kimgadir (yoki oʻzingizga) <strong>한국어</strong> deb xabar yuboring.</p>"},
                    {"stem": "<p>🔎 Atrofingizdan Hangul toping: serial nomi, koreys mahsuloti qutisi, telefon qutisidagi yozuv. Bitta blokni harflarga ajratib oʻqing va quyida yozib qoʻying.</p>",
                     "model_answer": "<p>Masalan, shampun qutisida 한 — ㅎ + ㅏ + ㄴ = «han».</p>"},
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-9 — Salomlashish, xayrlashish, tanishish
    # Taught: 안녕하세요 · 안녕히 계세요 / 가세요 · 감사합니다 · 고맙습니다 ·
    # 죄송합니다 · 미안합니다 · 실례합니다 · 네/예 · 아니요 · 저는 … 입니다
    # (as a fixed chunk) · 만나서 반갑습니다 · 잘 부탁합니다 · 어서 오세요 ·
    # 잘 먹겠습니다 / 먹었습니다 · 안녕히 주무세요 · 수고하셨습니다.
    # Warm-up: PK-8 (비음화), PK-6 (ㄲ), PK-2 (vowels).
    # ══════════════════════════════════════════════════════════════════
    {
        "tutorial": "PK-9: Salomlashish, xayrlashish va oʻzini tanishtirish",
        "intro": "<p>Bugungi vazifalardagi odamlar — <strong>Afsona</strong> va uning qoʻshnisi <strong>Jiyoung xola</strong> — «안녕하세요» oʻqish matnidan. Avval matnni oʻqigan boʻlsangiz, ularni taniysiz.</p>",
        "tasks": [
            {
                "section": "A",
                "kind": "hangul",
                "title": "Oldingi darslardan",
                "instruction": "<p>Harflardan soʻz yigʻing — Hangul unutilmasin.</p>",
                "items": [
                    {"stem": "ㄲ + ㅗ + ㅊ = ___ <small>(PK-6)</small>", "answers": ["꽃"], "size": "s",
                     "explanation": "<p>ㄲ — qattiq undosh (PK-6), ㅗ tagiga, ㅊ 받침: <strong>꽃</strong> (gul).</p>"},
                    {"stem": "ㅇ ㅜ ㅇ ㅠ = ___ <small>(PK-2, PK-3)</small>", "answers": ["우유"], "size": "m",
                     "explanation": "<p>Ikki unli — ikki blok: 우 + 유 = <strong>우유</strong> (sut).</p>"},
                ],
            },
            {
                "section": "A",
                "kind": "gap",
                "title": "Qanday oʻqiladi?",
                "instruction": "<p>Talaffuzni Hangulda yozing (PK-8, 비음화).</p>",
                "items": [
                    {"stem": "입니다 → [___]", "answers": ["임니다"], "size": "m",
                     "explanation": "<p>ㅂ dan keyin ㄴ kelsa, ㅂ burun tovushi ㅁ ga aylanadi: [<strong>임니다</strong>].</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "pick",
                "title": "Kimning oyogʻi harakatlanyapti?",
                "instruction": "<p>Vaziyatni oʻqing va toʻgʻri xayrlashuvni tanlang. Siz ketyapsizmi — qolganga <strong>계세요</strong>. U ketyaptimi — unga <strong>가세요</strong>.</p>",
                "items": [
                    {"stem": "Afsona doʻkondan chiqyapti. Sotuvchiga: ___", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 계세요"],
                     "explanation": "<p>Afsona ketyapti, sotuvchi doʻkonda <em>qoladi</em> → «tinchlikda qoling»: <strong>안녕히 계세요</strong>.</p>"},
                    {"stem": "Jiyoung xola Afsonanikidan ketyapti. Afsona xolaga: ___", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 가세요"],
                     "explanation": "<p>Xola ketyapti, Afsona uyda qoladi → «tinchlikda boring»: <strong>안녕히 가세요</strong>.</p>"},
                    {"stem": "Siz va doʻstingiz koʻchada uchrashdingiz, endi ikkalangiz ham oʻz yoʻlingizga ketyapsiz: ___", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 가세요"],
                     "explanation": "<p>Hech kim qolmayapti — ikkalangiz ham ketyapsiz, shuning uchun ikkalangiz ham <strong>안녕히 가세요</strong> deysiz.</p>"},
                    {"stem": "Darsdan keyin oʻqituvchining xonasidan chiqyapsiz: ___", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 계세요"],
                     "explanation": "<p>Oʻqituvchi xonada qoladi, siz ketyapsiz → <strong>안녕히 계세요</strong>.</p>"},
                    {"stem": "Mehmonlaringizni eshikkacha kuzatib chiqdingiz: ___", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 가세요"],
                     "explanation": "<p>Mehmonlar ketyapti, siz qolasiz → <strong>안녕히 가세요</strong>.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "gap",
                "title": "Iborani toʻldiring",
                "instruction": "<p>Boʻsh joyga yetishmayotgan soʻzni yozing.</p>",
                "items": [
                    {"stem": "만나서 ___. <small>(tanishganimdan xursandman)</small>", "answers": ["반갑습니다"], "size": "m",
                     "explanation": "<p><strong>만나서 반갑습니다</strong> — soʻzma-soʻz «uchrashib, xursandman».</p>"},
                    {"stem": "잘 ___. <small>(tanishuv yakuni)</small>", "answers": ["부탁합니다"], "size": "m",
                     "explanation": "<p><strong>잘 부탁합니다</strong> — tanishuv shu ibora bilan yakunlanadi.</p>"},
                    {"stem": "어서 ___. <small>(doʻkonda: xush kelibsiz)</small>", "answers": ["오세요"], "size": "m",
                     "explanation": "<p><strong>어서 오세요</strong> — doʻkon va kafelarda sizni shunday kutib olishadi.</p>"},
                    {"stem": "잘 ___. <small>(ovqatdan oldin)</small>", "answers": ["먹겠습니다"], "size": "m",
                     "explanation": "<p>Oldin — <strong>먹겠습니다</strong> («yeyman»): 겠 kelasi zamonni bildiradi.</p>"},
                    {"stem": "잘 ___. <small>(ovqatdan keyin)</small>", "answers": ["먹었습니다"], "size": "m",
                     "explanation": "<p>Keyin — <strong>먹었습니다</strong> («yedim»): 었 oʻtgan zamon.</p>"},
                    {"stem": "안녕히 ___. <small>(yotishdan oldin)</small>", "answers": ["주무세요"], "size": "m",
                     "explanation": "<p><strong>안녕히 주무세요</strong> — «xayrli tun».</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "gap",
                "title": "Qanday eshitiladi?",
                "instruction": "<p>Yozilishi bir xil, aytilishi boshqacha. Talaffuzni Hangulda yozing.</p>",
                "items": [
                    {"stem": "감사합니다 → [___]", "answers": ["감사함니다"], "size": "m",
                     "explanation": "<p>합 ning ㅂ si ㄴ oldida ㅁ ga aylanadi: [감사<strong>함</strong>니다].</p>"},
                    {"stem": "죄송합니다 → [___]", "answers": ["죄송함니다"], "size": "m",
                     "explanation": "<p>Xuddi shu 비음화: [죄송<strong>함</strong>니다]. 합니다 bilan tugagan hamma narsa [함니다].</p>"},
                    {"stem": "고맙습니다 → [___]", "answers": ["고맙씀니다"], "size": "m",
                     "explanation": "<p>Ikkita qoida birga: ㅂ dan keyin ㅅ qattiqlashadi (ㅆ), 습 ning ㅂ si esa ㄴ oldida ㅁ boʻladi: [고맙<strong>씀</strong>니다].</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "translate",
                "title": "Koreyscha qanday deysiz?",
                "instruction": "<p>Oʻzbekcha iborani koreyschaga oʻgiring. Bir nechta toʻgʻri javob boʻlishi mumkin.</p>",
                "items": [
                    {"stem": "Rahmat.", "answers": ["감사합니다", "고맙습니다"], "size": "l",
                     "explanation": "<p><strong>감사합니다</strong> — eng keng tarqalgan; <strong>고맙습니다</strong> — biroz iliqroq. Ikkalasi ham toʻgʻri.</p>"},
                    {"stem": "Kechirasiz. <small>(jiddiy uzr — birovning oyogʻini bosib oldingiz)</small>", "answers": ["죄송합니다"], "size": "l",
                     "explanation": "<p>Jiddiy uzr — <strong>죄송합니다</strong>. 미안합니다 yengilroq.</p>"},
                    {"stem": "Uzr, ijozat bering… <small>(notanishdan yoʻl soʻrashdan oldin)</small>", "answers": ["실례합니다"], "size": "l",
                     "explanation": "<p>Gap boshlashdan oldingi «uzr» — <strong>실례합니다</strong>.</p>"},
                    {"stem": "Ha.", "answers": ["네", "예"], "size": "l",
                     "explanation": "<p><strong>네</strong> yoki <strong>예</strong> — ikkalasi ham «ha».</p>"},
                    {"stem": "Yoʻq.", "answers": ["아니요", "아뇨"], "size": "l",
                     "explanation": "<p><strong>아니요</strong>.</p>"},
                    {"stem": "Charchamang, mehnatingiz uchun rahmat. <small>(ish kuni oxirida)</small>", "answers": ["수고하셨습니다"], "size": "l",
                     "explanation": "<p><strong>수고하셨습니다</strong> — ish yoki dars tugaganda bir-biriga aytiladi.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "build",
                "title": "Gapni yigʻing",
                "instruction": "<p>Berilgan soʻzlarni toʻgʻri tartibda yozing. Diqqat: <strong>입니다</strong> oldingi soʻzga boʻshliqsiz yopishadi.</p>",
                "items": [
                    {"words": ["반갑습니다", "만나서"], "answers": ["만나서 반갑습니다"],
                     "explanation": "<p>«Uchrashib» avval, «xursandman» — kesim — oxirida: <strong>만나서 반갑습니다</strong>.</p>"},
                    {"words": ["아프소나", "저는", "입니다"], "answers": ["저는 아프소나입니다"],
                     "explanation": "<p>Kesim gap oxirida, 입니다 ismga yopishadi: <strong>저는 아프소나입니다</strong>.</p>"},
                    {"words": ["계세요", "네", "안녕히"], "answers": ["네, 안녕히 계세요", "네 안녕히 계세요"],
                     "explanation": "<p><strong>네, 안녕히 계세요</strong> — «ha, xayr (siz qoling)».</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "fix",
                "title": "Xatoni toping va tuzating",
                "stars": 2,
                "instruction": "<p>Har bir vaziyatda notoʻgʻri ibora aytildi. Toʻgʻri iborani yozing.</p>",
                "items": [
                    {"stem": "(Afsona doʻkondan chiqib, sotuvchiga) «안녕히 가세요!»", "answers": ["안녕히 계세요"], "size": "l",
                     "explanation": "<p>Sotuvchi qoladi, Afsona ketadi → <strong>안녕히 계세요</strong>. Bu — yangi oʻquvchilarning eng koʻp qiladigan xatosi.</p>"},
                    {"stem": "(Notanish katta yoshli odamga) «안녕!»", "answers": ["안녕하세요"], "size": "l",
                     "explanation": "<p>안녕 — faqat yaqin doʻst va kichiklarga. Kattalarga: <strong>안녕하세요</strong>.</p>"},
                    {"stem": "(Ovqat endi keltirildi, hali yemadingiz) «잘 먹었습니다.»", "answers": ["잘 먹겠습니다"], "size": "l",
                     "explanation": "<p>Hali yemadingiz — demak kelasi: <strong>잘 먹겠습니다</strong>. 먹었습니다 ovqatdan <em>keyin</em>.</p>"},
                ],
            },
            {
                "section": "D",
                "kind": "write",
                "title": "Oʻzingizni tanishtiring",
                "instruction": "<p>Yangi koreys tili guruhiga keldingiz. Oʻzingizni 4 gapda tanishtiring.</p>",
                "items": [
                    {"stem": "<p>Salom → ismingiz → xursandligingiz → tanishuv yakuni.</p>",
                     "checklist": [
                         "<strong>안녕하세요</strong> bilan boshladim",
                         "Ismimni <strong>저는 … 입니다</strong> qolipida aytdim (oʻzimga 씨 qoʻshmadim)",
                         "<strong>만나서 반갑습니다</strong> dedim",
                         "<strong>잘 부탁합니다</strong> bilan tugatdim",
                     ],
                     "model_answer": "<p>안녕하세요? 저는 셰르벡입니다. 만나서 반갑습니다. 잘 부탁합니다.</p>",
                     "explanation": "<p>Ismingizni Hangulda yozish qiyin boʻlsa: Afsona — 아프소나, Jasur — 자수르, Sherbek — 셰르벡, Dilnoza — 딜노자.</p>"},
                ],
            },
            {
                "section": "D",
                "kind": "write",
                "title": "Doʻkonda",
                "stars": 3,
                "instruction": "<p>Qisqa dialog yozing: Afsona doʻkonga kiradi, sotuvchi kutib oladi, Afsona rahmat aytadi va chiqib ketadi. Har bir satr oldiga kim gapirayotganini yozing.</p>",
                "items": [
                    {"stem": "<p>Kamida 4 satr: sotuvchi — Afsona — sotuvchi — Afsona.</p>",
                     "checklist": [
                         "Sotuvchi <strong>어서 오세요</strong> dedi",
                         "Afsona rahmat aytdi",
                         "Oxirida kim <strong>계세요</strong>, kim <strong>가세요</strong> deyishini toʻgʻri tanladim",
                     ],
                     "model_answer": "<p>Sotuvchi: 어서 오세요!<br>Afsona: 안녕하세요?<br>Sotuvchi: 네, 안녕하세요.<br>Afsona: 감사합니다. 안녕히 계세요.<br>Sotuvchi: 네, 안녕히 가세요.</p>",
                     "explanation": "<p>Afsona ketadi → u <strong>계세요</strong> deydi; sotuvchi qoladi → u <strong>가세요</strong> deydi.</p>"},
                ],
            },
            {
                "section": "E",
                "kind": "mission",
                "title": "Missiya",
                "instruction": "<p>Bugun darsdan tashqarida qiling.</p>",
                "items": [
                    {"stem": "<p>🍽 Bugun kechki ovqatdan oldin ovoz chiqarib <strong>잘 먹겠습니다</strong>, keyin <strong>잘 먹었습니다</strong> deng. Oilangizga maʼnosini tushuntiring.</p>"},
                    {"stem": "<p>🎬 Koreys serialidan bitta xayrlashuv sahnasini toping. Kim <strong>계세요</strong>, kim <strong>가세요</strong> dedi — va kim ketayotgan edi? Quyida yozing.</p>",
                     "model_answer": "<p>Masalan: mehmon chiqib ketayotib «안녕히 계세요» dedi, uy egasi esa «안녕히 가세요» deb javob berdi.</p>"},
                    {"stem": "<p>🪞 Oyna oldida tanishuvingizni uch marta ovoz chiqarib, bosh egib ayting. 합니다 ni [함니다] deyishni unutmang.</p>"},
                ],
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-10 — 명사 + 입니다 / 입니까? / 이·가 아닙니다
    # Taught: 입니다 · 입니까? · 이/가 아닙니다 · 씨 · 저 (vs 나) · 저는 as a
    # chunk · 학생 · 선생님 · 의사 · 친구 · 사람 · 한국 사람 ·
    # 우즈베키스탄 사람. (은/는 as a system is PK-12 — here only 저는 / 씨는.)
    # Warm-up: PK-9, PK-7 (받침), PK-3.
    # ══════════════════════════════════════════════════════════════════
    {
        "tutorial": "PK-10: 명사 + 입니다 / 입니까? — rasmiy \"…dir\" va savol",
        "intro": "<p>Vazifalardagi <strong>Jasur</strong>, <strong>Dilnoza</strong> va <strong>Jiyoung</strong> — «저는 학생입니다» oʻqish matnidagi sinfdan. Jiyoung — oʻqituvchi, Jasur va Dilnoza — oʻquvchilar.</p>",
        "tasks": [
            {
                "section": "A",
                "kind": "pick",
                "title": "Oldingi darslardan",
                "instruction": "<p>Tez takrorlash.</p>",
                "items": [
                    {"stem": "Kafedan chiqyapsiz. Ofitsiantga: ___ <small>(PK-9)</small>", "options": ["안녕히 계세요", "안녕히 가세요"], "answers": ["안녕히 계세요"],
                     "explanation": "<p>Ofitsiant qoladi, siz ketasiz → <strong>안녕히 계세요</strong>.</p>"},
                    {"stem": "학생 — oxirgi boʻgʻinda 받침 ___ <small>(PK-7)</small>", "options": ["bor", "yoʻq"], "answers": ["bor"],
                     "explanation": "<p>생 = ㅅ + ㅐ + <strong>ㅇ</strong> — 받침 bor. Bugun bu juda kerak boʻladi!</p>"},
                    {"stem": "의사 — oxirgi boʻgʻinda 받침 ___ <small>(PK-7)</small>", "options": ["bor", "yoʻq"], "answers": ["yoʻq"],
                     "explanation": "<p>사 = ㅅ + ㅏ — unli bilan tugaydi, 받침 yoʻq.</p>"},
                ],
            },
            {
                "section": "A",
                "kind": "hangul",
                "title": "Soʻzni yigʻing",
                "instruction": "<p>Harflardan blok yigʻing <small>(PK-3)</small>.</p>",
                "items": [
                    {"stem": "ㅇ ㅢ ㅅ ㅏ = ___", "answers": ["의사"], "size": "m",
                     "explanation": "<p>ㅢ — qoʻshma unli (PK-3): 의 + 사 = <strong>의사</strong>, shifokor.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "gap",
                "title": "Kim ekanini ayting",
                "instruction": "<p>Qavsdagi soʻz bilan gapni tugating: ot + <strong>입니다</strong>, boʻshliqsiz.</p>",
                "items": [
                    {"stem": "저는 ___. <small>(oʻqituvchi)</small>", "answers": ["선생님입니다"], "size": "m",
                     "explanation": "<p>선생님 + 입니다 → <strong>선생님입니다</strong>. 입니다 받침 bor-yoʻqligiga qaramaydi.</p>"},
                    {"stem": "저는 ___. <small>(shifokor)</small>", "answers": ["의사입니다"], "size": "m",
                     "explanation": "<p><strong>의사입니다</strong> — 받침 yoʻq, lekin shakl baribir bir xil.</p>"},
                    {"stem": "자수르 씨는 ___. <small>(talaba)</small>", "answers": ["학생입니다"], "size": "m",
                     "explanation": "<p><strong>학생입니다</strong> — oʻqilishi [학쌩임니다].</p>"},
                    {"stem": "우리는 ___. <small>(biz — doʻstlar)</small>", "answers": ["친구입니다"], "size": "m",
                     "explanation": "<p><strong>친구입니다</strong>. 우리 — «biz».</p>"},
                    {"stem": "딜노자 씨는 ___. <small>(oʻzbekistonlik)</small>", "answers": ["우즈베키스탄 사람입니다"], "size": "l",
                     "explanation": "<p><strong>우즈베키스탄 사람입니다</strong> — «Oʻzbekiston odami». 입니다 faqat oxirgi soʻzga yopishadi.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "pick",
                "title": "이 yoki 가?",
                "instruction": "<p>Inkorda ot <strong>이</strong> yoki <strong>가</strong> oladi: 받침 bor → 이, yoʻq → 가.</p>",
                "items": [
                    {"stem": "학생___ 아닙니다.", "options": ["이", "가"], "answers": ["이"],
                     "explanation": "<p>학생 ㅇ bilan tugaydi — 받침 bor → <strong>이</strong>.</p>"},
                    {"stem": "친구___ 아닙니다.", "options": ["이", "가"], "answers": ["가"],
                     "explanation": "<p>친구 unli ㅜ bilan tugaydi → <strong>가</strong>.</p>"},
                    {"stem": "선생님___ 아닙니다.", "options": ["이", "가"], "answers": ["이"],
                     "explanation": "<p>님 — ㅁ 받침 → <strong>이</strong>.</p>"},
                    {"stem": "의사___ 아닙니다.", "options": ["이", "가"], "answers": ["가"],
                     "explanation": "<p>의사 unli bilan tugaydi → <strong>가</strong>. 「의사이 아닙니다」 — eng koʻp uchraydigan xato.</p>"},
                    {"stem": "한국 사람___ 아닙니다.", "options": ["이", "가"], "answers": ["이"],
                     "explanation": "<p>람 — ㅁ 받침 → <strong>이</strong>.</p>"},
                ],
            },
            {
                "section": "B",
                "kind": "transform",
                "title": "Savolga aylantiring",
                "instruction": "<p>Faqat <strong>다 → 까</strong>. Soʻz tartibi oʻzgarmaydi.</p>",
                "items": [
                    {"stem": "학생입니다. → ___?", "answers": ["학생입니까?"], "size": "m",
                     "explanation": "<p><strong>학생입니까?</strong> — oʻzbekchadagi «talaba<em>mi</em>?» kabi.</p>"},
                    {"stem": "의사입니다. → ___?", "answers": ["의사입니까?"], "size": "m",
                     "explanation": "<p><strong>의사입니까?</strong></p>"},
                    {"stem": "딜노자 씨는 선생님입니다. → ___?", "answers": ["딜노자 씨는 선생님입니까?"], "size": "l",
                     "explanation": "<p>Faqat oxiri oʻzgaradi: <strong>딜노자 씨는 선생님입니까?</strong></p>"},
                ],
            },
            {
                "section": "C",
                "kind": "transform",
                "title": "Inkorga aylantiring",
                "instruction": "<p>…입니다 → …<strong>이/가 아닙니다</strong>. 받침ga qarang!</p>",
                "items": [
                    {"stem": "저는 의사입니다. → ___", "answers": ["저는 의사가 아닙니다."], "size": "l",
                     "explanation": "<p>의사 — 받침 yoʻq → <strong>저는 의사가 아닙니다</strong>.</p>"},
                    {"stem": "저는 학생입니다. → ___", "answers": ["저는 학생이 아닙니다."], "size": "l",
                     "explanation": "<p>학생 — 받침 bor → <strong>저는 학생이 아닙니다</strong>.</p>"},
                    {"stem": "자수르 씨는 선생님입니다. → ___", "answers": ["자수르 씨는 선생님이 아닙니다."], "size": "l",
                     "explanation": "<p><strong>자수르 씨는 선생님이 아닙니다</strong>.</p>"},
                    {"stem": "지영 씨는 우즈베키스탄 사람입니다. → ___", "answers": ["지영 씨는 우즈베키스탄 사람이 아닙니다."], "size": "l",
                     "explanation": "<p>사람 ㅁ bilan tugaydi → <strong>…사람이 아닙니다</strong>.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "translate",
                "title": "Koreyschaga oʻgiring",
                "instruction": "<p>Rasmiy shaklda yozing. «Men» — <strong>저는</strong>; agar gapdan aniq boʻlsa, uni tushirib qoldirish ham toʻgʻri.</p>",
                "items": [
                    {"stem": "Men talabaman.", "answers": ["저는 학생입니다.", "학생입니다."], "size": "l",
                     "explanation": "<p><strong>저는 학생입니다</strong>. Koreyslar «men»ni koʻpincha tashlab ketadi: <strong>학생입니다</strong> ham toʻgʻri.</p>"},
                    {"stem": "Men shifokor emasman.", "answers": ["저는 의사가 아닙니다.", "의사가 아닙니다."], "size": "l",
                     "explanation": "<p><strong>저는 의사가 아닙니다</strong> — 의사 unli bilan tugaydi → 가.</p>"},
                    {"stem": "Jasur janob oʻqituvchimi?", "answers": ["자수르 씨는 선생님입니까?"], "size": "l",
                     "explanation": "<p><strong>자수르 씨는 선생님입니까?</strong> — boshqa odamga 씨.</p>"},
                    {"stem": "Afsona xonim oʻzbekistonlik.", "answers": ["아프소나 씨는 우즈베키스탄 사람입니다."], "size": "l",
                     "explanation": "<p><strong>아프소나 씨는 우즈베키스탄 사람입니다</strong>.</p>"},
                    {"stem": "Men koreys emasman.", "answers": ["저는 한국 사람이 아닙니다.", "한국 사람이 아닙니다."], "size": "l",
                     "explanation": "<p><strong>저는 한국 사람이 아닙니다</strong> — 사람 + 이.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "build",
                "title": "Gapni yigʻing",
                "instruction": "<p>Soʻzlarni tartibga keltiring. Kesim — oxirida.</p>",
                "items": [
                    {"words": ["아닙니다", "저는", "선생님이"], "answers": ["저는 선생님이 아닙니다."],
                     "explanation": "<p><strong>저는 선생님이 아닙니다</strong> — ega, ot, kesim. Oʻzbekcha tartib bilan bir xil.</p>"},
                    {"words": ["학생입니까?", "딜노자", "씨는"], "answers": ["딜노자 씨는 학생입니까?"],
                     "explanation": "<p><strong>딜노자 씨는 학생입니까?</strong> — 씨 ismdan keyin, boʻshliq bilan.</p>"},
                ],
            },
            {
                "section": "C",
                "kind": "fix",
                "title": "Xatoni tuzating",
                "stars": 2,
                "instruction": "<p>Har bir gapda bitta xato bor. Toʻgʻri gapni yozing.</p>",
                "items": [
                    {"stem": "저는 아프소나 씨입니다.", "answers": ["저는 아프소나입니다."], "size": "l",
                     "explanation": "<p>씨 — hurmat, uni oʻzingizga qoʻllamaysiz: <strong>저는 아프소나입니다</strong>.</p>"},
                    {"stem": "저는 의사이 아닙니다.", "answers": ["저는 의사가 아닙니다."], "size": "l",
                     "explanation": "<p>의사 unli bilan tugaydi → <strong>가</strong>: 저는 의사가 아닙니다.</p>"},
                    {"stem": "저는 입니다 학생.", "answers": ["저는 학생입니다."], "size": "l",
                     "explanation": "<p>Kesim har doim oxirida: <strong>저는 학생입니다</strong>.</p>"},
                    {"stem": "학생입니다까?", "answers": ["학생입니까?"], "size": "l",
                     "explanation": "<p>Savolda 다 <em>almashtiriladi</em>, qoʻshilmaydi: <strong>학생입니까?</strong></p>"},
                ],
            },
            {
                "section": "D",
                "kind": "write",
                "title": "Uch kishi",
                "instruction": "<p>Uch kishini tanishtiring: oʻzingiz, doʻstingiz va oʻqituvchingiz. Har biri haqida bitta <strong>…입니다</strong> va bitta <strong>…이/가 아닙니다</strong> gapi — jami 6 gap.</p>",
                "items": [
                    {"stem": "<p>Bilgan soʻzlaringiz: 학생, 선생님, 의사, 친구, 한국 사람, 우즈베키스탄 사람.</p>",
                     "checklist": [
                         "Har bir 입니다 otga <strong>boʻshliqsiz</strong> yopishgan",
                         "Inkorda 받침ga qarab <strong>이</strong> yoki <strong>가</strong> tanladim",
                         "<strong>씨</strong> faqat boshqa odamlarning ismiga qoʻshildi",
                         "Har bir gapda kesim oxirida turibdi",
                     ],
                     "model_answer": "<p>저는 학생입니다. 저는 선생님이 아닙니다.<br>자수르 씨는 친구입니다. 자수르 씨는 한국 사람이 아닙니다.<br>지영 씨는 선생님입니다. 지영 씨는 의사가 아닙니다.</p>",
                     "explanation": "<p>Har bir juftlikda avval kim <em>ekani</em>, keyin kim <em>emasligi</em>. 학생<strong>이</strong>, 사람<strong>이</strong> (받침 bor), 의사<strong>가</strong> (받침 yoʻq).</p>"},
                ],
            },
            {
                "section": "D",
                "kind": "write",
                "title": "Savol-javob",
                "stars": 3,
                "instruction": "<p>Jasur va Dilnoza oʻrtasida 4 satrli dialog yozing: savollar <strong>입니까?</strong> bilan, javoblar <strong>네 / 아니요</strong> bilan boshlansin.</p>",
                "items": [
                    {"stem": "<p>Kamida bitta javob «아니요, … 이/가 아닙니다» boʻlsin va toʻgʻrisini aytsin.</p>",
                     "checklist": [
                         "Kamida ikkita savol 입니까? bilan tugaydi",
                         "Javoblar 네 yoki 아니요 bilan boshlanadi",
                         "«아니요» dan keyin toʻgʻrisi ham aytildi",
                     ],
                     "model_answer": "<p>자수르: 딜노자 씨는 의사입니까?<br>딜노자: 아니요, 의사가 아닙니다. 학생입니다.<br>자수르: 딜노자 씨는 우즈베키스탄 사람입니까?<br>딜노자: 네, 우즈베키스탄 사람입니다.</p>"},
                ],
            },
            {
                "section": "E",
                "kind": "mission",
                "title": "Missiya",
                "instruction": "<p>Bugun darsdan tashqarida qiling.</p>",
                "items": [
                    {"stem": "<p>🎙 Telefoningizga 20 soniyalik ovozli xabar yozing: salom, ismingiz, kim ekaningiz, kim <em>emas</em>ligingiz, tanishuv yakuni. Ertaga eshiting: 입니다 ni [임니다] deb aytdingizmi?</p>"},
                    {"stem": "<p>👨‍👩‍👧 Oila suratini oling. Har bir kishini koʻrsatib, uning ismi bilan bitta gap ayting: «… 씨는 학생입니다» yoki «… 씨는 의사가 아닙니다». Eng qiziq gapingizni quyida yozing.</p>",
                     "model_answer": "<p>셰르벡 씨는 학생입니다. 셰르벡 씨는 선생님이 아닙니다.</p>"},
                ],
            },
        ],
    },
]
