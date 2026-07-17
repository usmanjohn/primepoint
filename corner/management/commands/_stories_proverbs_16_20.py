# 속담 이야기 (Koreys maqollari) — stories 16–20. Style: STYLE_GUIDE_CORNER.md §5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_16_20.py --author=prime

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "속담 이야기 (Koreys maqollari)",
    "description": "Koreys maqollari (속담): maʼnosi, kelib chiqish hikoyasi va hayotda ishlatilishi — lugʻat va savollar bilan.",
    "order":       4,
}

STORIES = [
    # ── 16 ───────────────────────────────────────────────────────────────
    {
        "title":   "발 없는 말이 천 리 간다",
        "summary": "«Oyoqsiz soʻz ming chaqirim yuradi» — bir ogʻiz gap bir kunda butun shaharga tarqaladi. Soʻzni ehtiyot qiling!",
        "order":   16,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">👄 ➡️ 🌍</div>
<p>"발 없는 말이 천 리 간다." 여기서 재미있는 것은 <span class="cn-word" data-tr="soʻz omonimi">말</span>이라는 단어다. 한국어에서 말은 "말하는 말"도 되고 "타는 <span class="cn-word" data-tr="ot (hayvon)">말</span>"도 된다. 말(馬)은 발이 네 개나 있어서 하루에 천 리를 <span class="cn-word" data-pos="verb" data-tr="yugurmoq">달린다</span>. 그런데 발이 하나도 없는 말(言)은 그보다 더 빨리, 더 멀리 간다는 뜻이다. <span class="cn-word" data-tr="ming chaqirim">천 리</span>는 약 사백 킬로미터다.</p>
<p>지수의 경험이다. 월요일 아침, 지수는 짝꿍에게만 <span class="cn-word" data-pos="adv" data-tr="pichirlab">조용히</span> 말했다. "나 사실 가수가 되고 싶어. 아무한테도 말하지 마." 그런데 점심시간이 되<strong>기가 무섭게</strong> 옆 반 친구가 와서 물었다. "너 가수 <span class="cn-word" data-tr="tanlov, saralash">오디션</span> 본다며?" 저녁에는 <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> 엄마도 알고 있었다. "우리 딸이 가수가 된다고 <span class="cn-word" data-tr="butun mahalla">온 동네</span>가 <span class="cn-word" data-pos="adj" data-tr="shov-shuvli">시끌시끌하던데</span>?" 반나절 만에 <span class="cn-word" data-tr="sir">비밀</span>이 천 리를 간 것이다.</p>
<p>이 속담은 두 가지를 가르친다. 첫째, 남의 이야기를 <span class="cn-word" data-pos="verb" data-tr="yetkazmoq, tashimoq">옮기지</span> 마라. 내가 옮긴 말은 반드시 더 멀리 <span class="cn-word" data-pos="verb" data-tr="uchib bormoq">날아가는</span> 법이다. 둘째, 비밀을 지키고 싶다면 <span class="cn-word" data-pos="adv" data-tr="boshidanoq">애초에</span> 말하지 마라. 한 사람에게만 한 말도 이미 세상에 <span class="cn-word" data-pos="verb" data-tr="qoʻyib yubormoq">놓아준</span> 새와 같다. 다시 <span class="cn-word" data-pos="verb" data-tr="qaytarib olmoq">되돌릴</span> 수 없다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Aytilgan soʻz — otilgan oʻq» — ogʻizdan chiqqan gapni qaytarib boʻlmaydi, u oʻz yoʻlida uchaveradi. Koreyslarda oʻq oʻrnida — oyoqsiz, lekin eng tez «ot».
</div>''',
        "grammar": [
            {
                "pattern":  "-기가 무섭게",
                "meaning":  "Juda tez ketma-ketlik: ...ar-arimas, shu zahoti.",
                "examples": ["점심시간이 되기가 무섭게 소문이 퍼졌다.", "수업이 끝나기가 무섭게 뛰어나갔어요."],
            },
            {
                "pattern":  "-는 법이다",
                "meaning":  "Tabiiy qonuniyat: ... boʻlishi tayin, shunday boʻladi.",
                "examples": ["옮긴 말은 더 멀리 날아가는 법이다.", "노력하면 결과가 나오는 법이에요."],
            },
        ],
        "questions": [
            {
                "text":        "이 속담에서 '말'이라는 단어가 재미있는 이유는 무엇입니까?",
                "choices":     ["말이 아주 느려서", "'말(言)'과 '말(馬)'이 소리가 같아서", "말이 천 리를 못 가서"],
                "answer":      1,
                "explanation": "Maqol soʻz oʻyiniga qurilgan: 말 ham «gap», ham «ot» degani. Toʻrt oyoqli ot ming chaqirim yursa, oyoqsiz «gap-ot» undan ham tez uchadi.",
            },
            {
                "text":        "지수의 비밀은 어떻게 되었습니까?",
                "choices":     ["짝꿍이 끝까지 지켜 주었다", "반나절 만에 엄마까지 알게 되었다", "아무도 관심이 없었다"],
                "answer":      1,
                "explanation": "Faqat partadoshiga aytilgan sir tushlikkacha qoʻshni sinfga, kechqurun esa onasigacha yetib bordi — «온 동네가 시끌시끌» boʻldi. Yarim kunda ming chaqirim!",
            },
            {
                "text":        "비밀을 지키는 방법으로 글쓴이가 말한 것은 무엇입니까?",
                "choices":     ["믿을 만한 친구 한 명에게만 말하기", "애초에 말하지 않기", "작은 소리로 말하기"],
                "answer":      1,
                "explanation": "Bir kishiga aytilgan gap ham «qoʻyib yuborilgan qush» — qaytarib boʻlmaydi. Demak yagona ishonchli yoʻl: boshidanoq aytmaslik. ① esa Jisu qilgan xato!",
            },
        ],
    },

    # ── 17 ───────────────────────────────────────────────────────────────
    {
        "title":   "시작이 반이다",
        "summary": "«Boshlash — yarmi» — eng qiyin qadam birinchi qadam. Boshladingizmi, ishning yarmi bitdi hisob!",
        "order":   17,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🚶 ➗ 🏁</div>
<p>"시작이 반이다." 시작하는 것이 일의 <span class="cn-word" data-tr="yarmi">절반</span>이라는 뜻이다. 계산으로는 <span class="cn-word" data-pos="adv" data-tr="mutlaqo">전혀</span> 맞지 않는 말이다. 첫 페이지를 읽었다고 책의 반을 읽은 것은 아니니까. 그런데 왜 옛사람들은 이렇게 말했을까?</p>
<p>그 이유는 사람의 마음에 있다. 무슨 일이든 가장 <span class="cn-word" data-pos="adj" data-tr="qiyin">어려운</span> 부분은 일 자체가 아니라 <span class="cn-word" data-pos="verb" data-tr="qaror qilmoq">결심하고</span> 첫걸음을 <span class="cn-word" data-pos="verb" data-tr="tashlamoq (qadamni)">내딛는</span> 것이기 때문이다. 운동을 <span class="cn-word" data-tr="misol">예</span>로 들어 보자. 제일 힘든 순간은 달리기가 아니라, <span class="cn-word" data-pos="adj" data-tr="issiq, iliq">따뜻한</span> 이불 속에서 나와 운동화를 신는 순간이다. 운동화만 신<strong>기만 하면</strong> 몸은 <span class="cn-word" data-pos="adv" data-tr="qandaydir tarzda">어느새</span> 밖으로 나가 있다.</p>
<p>민호는 일 년 동안 "한국어능력시험을 준비해야 하는데…"라고 말만 했다. <span class="cn-word" data-tr="reja">계획</span>만 세우고, 교재만 <span class="cn-word" data-pos="verb" data-tr="qidirmoq, koʻz yugurtirmoq">알아보고</span>, 시작은 하지 않았다. 어느 날 친구가 말했다. "고민하지 말고 <span class="cn-word" data-pos="adv" data-tr="bir yoʻla, avvalo">일단</span> 접수부터 해 버려. 시작이 반이야." 민호는 그 자리에서 시험을 <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtmoq">접수했다</span>. 시험 날짜가 <span class="cn-word" data-pos="verb" data-tr="belgilanmoq">정해지자</span> 신기한 일이 일어났다. 매일 미루던 공부가 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 시작된 것이다.</p>
<p>완벽한 준비를 기다리지 마라. 완벽한 <span class="cn-word" data-tr="payt, vaqt">때</span>는 영원히 오지 않는다. <span class="cn-word" data-pos="adj" data-tr="notoʻliq, nomukammal">서툰</span> 시작이 완벽한 계획보다 낫다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Boshlagan ish — bitgan ish» — xalqimiz ham xuddi shunday deydi! Eng ogʻir yuk — birinchi qadam; undan keyin ish oʻzi yuradi.
</div>''',
        "grammar": [
            {
                "pattern":  "-기만 하면",
                "meaning":  "Yetarli shart: faqat ...sa boʻldi (qolgani oʻzi keladi).",
                "examples": ["운동화만 신기만 하면 몸은 밖으로 나간다.", "이 버튼을 누르기만 하면 돼요."],
            },
            {
                "pattern":  "일단 -고 보다",
                "meaning":  "Avval qilib olish: koʻp oʻylamay, bir yoʻla ...b olish (keyin koʻramiz).",
                "examples": ["고민하지 말고 일단 접수부터 하고 보자.", "일단 만나 보고 결정하세요."],
            },
        ],
        "questions": [
            {
                "text":        "계산이 맞지 않는데도 '시작이 반'인 이유는 무엇입니까?",
                "choices":     ["일의 절반이 정말 첫 페이지라서", "가장 어려운 부분이 결심과 첫걸음이라서", "반만 하면 충분해서"],
                "answer":      1,
                "explanation": "Matematik jihatdan notoʻgʻri, lekin psixologik jihatdan toʻgʻri: eng qiyini — ishning oʻzi emas, qaror qilib birinchi qadam tashlash. Shu bosqich oʻtilsa, «yarmi» bitgan.",
            },
            {
                "text":        "민호에게 '신기한 일'은 무엇이었습니까?",
                "choices":     ["시험이 취소된 것", "시험을 접수하자 공부가 저절로 시작된 것", "친구가 대신 공부해 준 것"],
                "answer":      1,
                "explanation": "Bir yil «tayyorlanishim kerak» deb yurgan Minho roʻyxatdan oʻtishi bilanoq — sana belgilangach — har kuni kechiktirilgan oʻqish oʻz-oʻzidan boshlandi. Boshlash hammasini yurgizib yubordi.",
            },
        ],
    },

    # ── 18 ───────────────────────────────────────────────────────────────
    {
        "title":   "돌다리도 두들겨 보고 건너라",
        "summary": "«Tosh koʻprikni ham taqillatib koʻrib oʻt» — ishonchli koʻringan narsani ham tekshirib koʻring. Ehtiyotkorlik maqoli.",
        "order":   18,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🌉 👊 👀</div>
<p>"돌다리도 두들겨 보고 건너라." <span class="cn-word" data-tr="tosh koʻprik">돌다리</span>는 나무다리보다 훨씬 <span class="cn-word" data-pos="adj" data-tr="mustahkam">튼튼하다</span>. 그런 돌다리<strong>조차</strong> 건너기 전에 <span class="cn-word" data-pos="verb" data-tr="taqillatmoq">두들겨</span> 보고, <span class="cn-word" data-pos="adj" data-tr="xavfsiz">안전한지</span> 확인한 후에 건너라는 뜻이다. 아무리 <span class="cn-word" data-pos="adj" data-tr="aniq, ishonchli">확실해</span> 보이는 일이라도 다시 한번 <span class="cn-word" data-pos="verb" data-tr="tekshirmoq">점검하라는</span> 가르침이다.</p>
<p>지수 아버지는 이 속담 <span class="cn-word" data-pos="adv" data-tr="tufayli, sharofati bilan">덕분에</span> 큰돈을 지켰다. 어느 날 "은행"이라며 전화가 왔다. "고객님 <span class="cn-word" data-tr="hisob raqam">계좌</span>에 문제가 생겼습니다. 지금 바로 이 번호로 돈을 옮기세요." 목소리는 <span class="cn-word" data-pos="adj" data-tr="professional">전문적이었고</span> 은행 이름도 정확했다. 하지만 아버지는 전화를 끊고 <span class="cn-word" data-pos="adv" data-tr="oʻzi shaxsan">직접</span> 은행에 전화해서 물어보았다. 은행 직원이 <span class="cn-word" data-pos="verb" data-tr="hayron qolmoq">놀라며</span> 말했다. "저희는 그런 전화를 한 적이 없습니다. <span class="cn-word" data-tr="firibgarlik">사기</span>입니다!" 아무리 <span class="cn-word" data-pos="adj" data-tr="ishonchli koʻringan">그럴듯해</span> 보여<strong>도</strong> 두들겨 보아야 한다.</p>
<p>물론 <span class="cn-word" data-tr="muvozanat">균형</span>도 필요하다. 다리를 백 번 두들기<span class="cn-word" data-pos="adv" data-tr="faqat, xolos">기만</span> 하고 건너지 않는 사람은 아무 데도 가지 못한다. 이 속담은 "건너지 마라"가 아니라 "확인하<strong>고 나서</strong> 건너라"다. 확인은 한 번이면 충분하다 — 그다음에는 <span class="cn-word" data-pos="adv" data-tr="dadil">당당하게</span> 건너가라.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Yetti oʻlchab, bir kes» — kesishdan oldin yetti marta oʻlchang. Koreyslar oʻlchash oʻrniga koʻprikni taqillatadi — maʼno bitta: avval tekshir, keyin qil!
</div>''',
        "grammar": [
            {
                "pattern":  "아무리 -아/어도",
                "meaning":  "Yon berish: qanchalik ... boʻlsa ham.",
                "examples": ["아무리 그럴듯해 보여도 확인해야 한다.", "아무리 늦어도 전화는 하세요."],
            },
            {
                "pattern":  "-고 나서",
                "meaning":  "Ketma-ketlik: ...b boʻlgach, ...gandan keyin.",
                "examples": ["확인하고 나서 건너라.", "숙제를 끝내고 나서 놀 거예요."],
            },
        ],
        "questions": [
            {
                "text":        "지수 아버지는 어떻게 사기를 피했습니까?",
                "choices":     ["전화를 받지 않아서", "직접 은행에 전화해서 확인해서", "돈이 없어서"],
                "answer":      1,
                "explanation": "Ovoz professional, bank nomi aniq — hammasi ishonchli koʻrindi. Lekin ota telefonni qoʻyib, OʻZI bankka qoʻngʻiroq qilib tekshirdi — «koʻprikni taqillatdi» va firibgarlik ochildi.",
            },
            {
                "text":        "글쓴이가 말한 '균형'은 무엇입니까?",
                "choices":     ["다리를 백 번 두들겨야 한다", "확인한 후에는 당당하게 건너야 한다", "돌다리로만 다녀야 한다"],
                "answer":      1,
                "explanation": "Maqol «oʻtma» demaydi — «tekshirib OʻT» deydi. Yuz marta taqillatib turaverish ham xato: bir tekshiruv yetadi, keyin dadil harakat.",
            },
        ],
    },

    # ── 19 ───────────────────────────────────────────────────────────────
    {
        "title":   "개구리 올챙이 적 생각 못 한다",
        "summary": "«Qurbaqa itbaliqlik davrini eslamaydi» — muvaffaqiyatga erishgach, oʻzining ojiz boshlanishini unutib, boshqalarni mensimaslik haqida.",
        "order":   19,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐸 🔙 💭</div>
<p>"개구리 올챙이 적 생각 못 한다." <span class="cn-word" data-tr="itbaliq">올챙이</span>는 개구리의 아기다. 다리도 없고, 헤엄도 <span class="cn-word" data-pos="adj" data-tr="beoʻxshov, noʻnoq">서툴고</span>, 꼬리만 <span class="cn-word" data-pos="verb" data-tr="likillatmoq">흔들며</span> 다닌다. 그런데 다리가 생기고 <span class="cn-word" data-pos="adj" data-tr="ulgʻaygan">어엿한</span> 개구리가 되면, 자기가 올챙이<strong>였던</strong> 시절을 <span class="cn-word" data-pos="adv" data-tr="butunlay">까맣게</span> 잊어버린다. 그리고 물속의 올챙이들을 보며 <span class="cn-word" data-pos="verb" data-tr="masxara qilmoq">비웃는다</span>. "쟤들은 왜 저렇게 헤엄을 못 치지?"</p>
<p>사람도 <span class="cn-word" data-pos="adv" data-tr="xuddi shunday">똑같다</span>. 한국어를 <span class="cn-word" data-pos="adv" data-tr="ravon">유창하게</span> 하게 된 선배가 이제 막 한글을 배우는 후배에게 "아직도 그걸 몰라?"라고 말한다. 자기도 삼 년 전에는 <span class="cn-word" data-tr="alifbo">자음과 모음</span>도 못 읽었으면서 말이다. 부자가 된 사람이 <span class="cn-word" data-pos="adj" data-tr="kambagʻal">가난한</span> 사람을 보고 "왜 노력을 안 하지?"라고 말한다. 자기가 <span class="cn-word" data-pos="adj" data-tr="qiynalgan">힘들었던</span> 시절을 잊은 것이다. 도와주<strong>기는커녕</strong> 비웃기만 한다면, 그 사람은 <span class="cn-word" data-tr="hurmat">존경</span>을 잃는다.</p>
<p>이 속담은 성공한 사람에게 주는 <span class="cn-word" data-tr="ogohlantirish">경고</span>다. 지금의 나를 만든 것은 <span class="cn-word" data-pos="adv" data-tr="aynan">바로</span> 그 서툴고 작았던 올챙이 시절이다. 그 시절을 기억하는 개구리만이 올챙이에게 <span class="cn-word" data-pos="adj" data-tr="mehribon">따뜻한</span> 선생님이 될 수 있다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> Aynan shu obraz bizda ham tushunarli: «qurbaqa itbaliqligini unutibdi». Maʼnodoshi — boyib yoki katta boʻlib, oʻz oʻtmishini unutgan odam haqida: «Amal minib, aslini unutma».
</div>''',
        "grammar": [
            {
                "pattern":  "-던",
                "meaning":  "Oʻtmishdagi holat/odatni eslash sifatdoshi: ...gan, ... boʻlgan (oʻsha paytdagi).",
                "examples": ["올챙이였던 시절을 잊어버린다.", "어릴 때 살던 동네에 가 봤어요."],
            },
            {
                "pattern":  "-기는커녕",
                "meaning":  "Kuchli inkor: ... u yoqda tursin, (aksincha) ...",
                "examples": ["도와주기는커녕 비웃기만 한다.", "쉬기는커녕 밥 먹을 시간도 없어요."],
            },
        ],
        "questions": [
            {
                "text":        "개구리는 올챙이를 보고 왜 비웃습니까?",
                "choices":     ["올챙이가 시끄러워서", "자기의 올챙이 시절을 잊어버려서", "올챙이가 개구리를 놀려서"],
                "answer":      1,
                "explanation": "Qurbaqa oʻzi ham bir paytlar oyoqsiz, noʻnoq itbaliq boʻlganini «butunlay unutib» (까맣게 잊어버려서), endi itbaliqlar ustidan kuladi. Unutish — kulishning ildizi.",
            },
            {
                "text":        "글에 따르면 어떤 개구리가 좋은 선생님이 됩니까?",
                "choices":     ["헤엄을 제일 잘 치는 개구리", "올챙이 시절을 기억하는 개구리", "가장 큰 개구리"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: oʻzining noʻnoq davrini ESLAB turgan qurbaqagina itbaliqqa mehribon ustoz boʻla oladi — chunki u qiynalish qandayligini biladi.",
            },
            {
                "text":        "이 속담과 어울리는 상황은 무엇입니까?",
                "choices":     ["선배가 초보 후배의 실수를 비웃는 것", "학생이 열심히 공부하는 것", "개구리가 연못에 사는 것"],
                "answer":      0,
                "explanation": "Oʻzi ham uch yil avval alifbo oʻqiy olmagan katta kurs talabasi endi yangi oʻquvchidan «shuni ham bilmaysanmi?» deb kulishi — maqolning zamonaviy koʻrinishi.",
            },
        ],
    },

    # ── 20 ───────────────────────────────────────────────────────────────
    {
        "title":   "말 한마디에 천 냥 빚을 갚는다",
        "summary": "«Bir ogʻiz soʻz ming tanga qarzni uzadi» — oʻrinli aytilgan iliq soʻzning kuchi pul bilan oʻlchab boʻlmas darajada katta.",
        "order":   20,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">💬 💰 🙏</div>
<p>"말 한마디에 천 냥 빚을 갚는다." <span class="cn-word" data-tr="nyang (qadimgi pul)">냥</span>은 옛날 돈의 단위로, 천 냥이면 집을 몇 채나 살 수 있는 <span class="cn-word" data-tr="ulkan summa">거금</span>이었다. 그 큰 <span class="cn-word" data-tr="qarz">빚</span>을 돈이 아니라 말 <span class="cn-word" data-tr="bir ogʻiz">한마디</span>로 갚을 수 있다는 뜻이다. <span class="cn-word" data-pos="adv" data-tr="oʻrinli, toʻgʻri">제대로</span> 한 말 한마디가 그만큼 <span class="cn-word" data-pos="adj" data-tr="qudratli">강력하다는</span> 것이다.</p>
<p>옛이야기가 전해진다. 가난한 농부가 부자에게 천 냥을 빌렸는데 갚을 날이 되어도 돈이 없었다. 농부는 <span class="cn-word" data-pos="verb" data-tr="qochib yurmoq">피해 다니는</span> 대신 부자를 찾아가 <span class="cn-word" data-pos="adv" data-tr="samimiy">진심으로</span> 말했다. "약속을 지키지 못해 정말 죄송합니다. 하늘 같은 <span class="cn-word" data-tr="marhamat">은혜</span>를 입고도 갚지 못하는 제 마음이 <span class="cn-word" data-tr="tosh">돌덩이</span>처럼 무겁습니다. 시간을 주시면 몇 배로 일해서 갚겠습니다." 부자는 한참 그를 바라보다가 웃으며 말했다. "됐네. 자네의 그 말 한마디가 천 냥일세." 그러고는 빚을 <span class="cn-word" data-pos="verb" data-tr="kechirmoq (qarzni)">탕감해</span> 주었다.</p>
<p>돈 한 푼 들지 않는데 천 냥의 <span class="cn-word" data-tr="qiymat">가치</span>를 지닌 말들이 있다. "고맙습니다." "제가 잘못했습니다." "당신 <span class="cn-word" data-tr="tufayli">덕분이에요</span>." "괜찮아요, 그럴 수 있어요." 이 말들을 <span class="cn-word" data-pos="adv" data-tr="oʻz vaqtida">제때</span> 하는 것<strong>만으로도</strong> 싸움이 <span class="cn-word" data-pos="verb" data-tr="oldini olinmoq">막아지고</span>, 관계가 살아나고, <span class="cn-word" data-pos="verb" data-tr="yarashmoq">화해하게</span> 된다. 말은 <span class="cn-word" data-pos="adj" data-tr="bepul">공짜지만</span>, 그 힘은 천 냥보다 크다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Yaxshi soʻz — jon ozigʻi» — iliq soʻz jonga quvvat. Koreyslar buni pulga chaqib aytadi: bir ogʻiz toʻgʻri soʻz — ming tanga!
</div>''',
        "grammar": [
            {
                "pattern":  "-만으로도",
                "meaning":  "Minimal yetarlilik: faqat ...ning oʻzi bilan ham.",
                "examples": ["말을 제때 하는 것만으로도 관계가 살아난다.", "목소리를 듣는 것만으로도 힘이 나요."],
            },
            {
                "pattern":  "-는 대신(에)",
                "meaning":  "Oʻrniga: ... qilish oʻrniga.",
                "examples": ["피해 다니는 대신 직접 찾아가서 말했다.", "밖에 나가는 대신 집에서 쉬었어요."],
            },
        ],
        "questions": [
            {
                "text":        "부자는 왜 농부의 빚을 탕감해 주었습니까?",
                "choices":     ["농부가 돈을 다 갚아서", "농부의 진심 어린 말 한마디에 감동해서", "농부가 무서워서"],
                "answer":      1,
                "explanation": "Fermer qochib yurish oʻrniga oʻzi kelib, chin dildan uzr soʻradi va vaʼda berdi — boy «자네의 그 말 한마디가 천 냥일세» (shu bir ogʻiz soʻzing — ming tanga) deb qarzni kechirdi.",
            },
            {
                "text":        "글에 따르면 '천 냥의 가치'를 지닌 말이 아닌 것은 무엇입니까?",
                "choices":     ["고맙습니다", "제가 잘못했습니다", "너 때문이야"],
                "answer":      2,
                "explanation": "Matnda sanalganlar: minnatdorchilik, uzr, «siz tufayli», tasalli. «너 때문이야» (hammasi sen aybdorsan) — buning teskarisi: bir ogʻiz soʻz ming tanga qarz ORTTIRISHI ham mumkin!",
            },
        ],
    },
]
