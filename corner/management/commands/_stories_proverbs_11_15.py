# 속담 이야기 (Koreys maqollari) — stories 11–15 (collection complete). Style: STYLE_GUIDE_CORNER.md §5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_11_15.py --author=prime

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
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "백지장도 맞들면 낫다",
        "summary": "«Bir varaq qogʻozni ham birga koʻtarsa yengil» — har qanday ish, hatto eng yengili ham, birgalikda osonlashadi.",
        "order":   11,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">📄 🤝 💪</div>
<p>"백지장도 맞들면 낫다." <span class="cn-word" data-tr="oq qogʻoz varaqi">백지장</span>은 흰 종이 한 장이다. 세상에서 가장 <span class="cn-word" data-pos="adj" data-tr="yengil">가벼운</span> 것 중 하나다. 그런 종이 한 장<strong>조차</strong> 둘이서 <span class="cn-word" data-pos="verb" data-tr="birga koʻtarmoq">맞들면</span> 더 낫다는 뜻이다. 하물며 <span class="cn-word" data-pos="adj" data-tr="ogʻir">무거운</span> 일은 말할 것도 없다.</p>
<p>지수네 <span class="cn-word" data-tr="mahalla, qishloq">동네</span> 이야기다. 혼자 사는 할머니가 <span class="cn-word" data-tr="koʻchish, koʻch-koʻron">이사</span>를 가게 되었다. <span class="cn-word" data-tr="yuk, buyumlar">짐</span>이 많지는 않았지만 할머니 혼자서는 <span class="cn-word" data-pos="adv" data-tr="umuman, sira">도저히</span> 옮길 수 없었다. 그때 옆집 아저씨가 나왔고, 그다음 학생 두 명이 나왔고, <span class="cn-word" data-pos="adv" data-tr="oxiri">결국</span> 열 명이 모였다. 혼자서라면 하루 종일 걸렸을 일이 한 시간 만에 끝났다. 할머니는 <span class="cn-word" data-tr="koʻz yoshi">눈물</span>을 글썽이며 말했다. "고마워요. 백지장도 맞들면 낫다더니, 정말 그러네요."</p>
<p>이 속담의 <span class="cn-word" data-pos="adj" data-tr="nozik, teran">깊은</span> 뜻은 "무거우니까 도와 달라"가 아니다. <span class="cn-word" data-pos="adv" data-tr="hatto">심지어</span> 가벼운 일도 함께하면 더 낫다는 것이다. 왜일까? 함께하면 일이 빨라질 뿐만 아니라, <span class="cn-word" data-tr="koʻngil, dil">마음</span>도 가벼워지기 때문이다. 혼자 하는 일은 <span class="cn-word" data-tr="mehnat">노동</span>이지만, 함께 하는 일은 <span class="cn-word" data-tr="xotira">추억</span>이 된다.</p>
<p>숙제를 할 때도, 방을 <span class="cn-word" data-pos="verb" data-tr="yigʻishtirmoq">치울</span> 때도, 슬픔을 <span class="cn-word" data-pos="verb" data-tr="koʻtarmoq, chidamoq">견딜</span> 때도 — 함께라면 모든 것이 <span class="cn-word" data-pos="adv" data-tr="ancha">훨씬</span> 가볍다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Birlashgan oʻzar, birlashmagan toʻzar» — birlikda kuch. Koreyslar buni eng yengil narsa — bir varaq qogʻoz misolida aytadi: hatto uni ham birga koʻtargan yaxshi!
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 뿐만 아니라",
                "meaning":  "Qoʻshimcha: nafaqat ..., balki ... ham.",
                "examples": ["일이 빨라질 뿐만 아니라 마음도 가벼워진다.", "그 식당은 맛있을 뿐만 아니라 싸요."],
            },
            {
                "pattern":  "-(느)ㄴ다더니",
                "meaning":  "Eshitgan gap tasdiqlanganda: ... deyishardi — rost ekan.",
                "examples": ["백지장도 맞들면 낫다더니 정말 그러네요.", "이 집이 맛있다더니 진짜 맛있네요."],
            },
        ],
        "questions": [
            {
                "text":        "이 속담이 '종이 한 장'을 예로 든 이유는 무엇입니까?",
                "choices":     ["종이가 가장 비싸서", "가장 가벼운 것도 함께하면 낫다는 것을 강조하려고", "종이를 자주 잃어버려서"],
                "answer":      1,
                "explanation": "Eng yengil narsa — bir varaq qogʻoz. Hatto UNI ham birga koʻtargan yaxshi boʻlsa, ogʻir ishlar haqida gapirmasa ham boʻladi — taʼkid ana shunda.",
            },
            {
                "text":        "글에 따르면 함께 일하면 무엇이 달라집니까?",
                "choices":     ["일이 느려진다", "일이 빨라지고 마음도 가벼워진다", "짐이 무거워진다"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: birgalikda ish tezlashadi va koʻngil ham yengillashadi. «Yolgʻiz qilingan ish — mehnat, birga qilingan ish — xotira».",
            },
        ],
    },

    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "고래 싸움에 새우 등 터진다",
        "summary": "«Kitlar jangida krevetkaning beli sinadi» — kattalar urishsa, zarar aybsiz kichiklarga tegadi.",
        "order":   12,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐋 ⚔️ 🦐</div>
<p>"고래 싸움에 새우 등 터진다." 바다의 <span class="cn-word" data-tr="ulkan">거대한</span> <span class="cn-word" data-tr="kit">고래</span> 두 마리가 싸우면, 그 사이에 있던 작은 <span class="cn-word" data-tr="krevetka">새우</span>의 <span class="cn-word" data-tr="bel, orqa">등</span>이 <span class="cn-word" data-pos="verb" data-tr="yorilmoq">터진다</span>는 뜻이다. <span class="cn-word" data-pos="adj" data-tr="kuchli">힘센</span> 사람들의 싸움 때문에 <span class="cn-word" data-pos="adj" data-tr="aybsiz, begunoh">애꿎은</span> 사람이 <span class="cn-word" data-tr="zarar">피해</span>를 입을 때 쓴다.</p>
<p>학교에서 자주 보는 <span class="cn-word" data-tr="manzara, holat">풍경</span>이다. 반에서 제일 <span class="cn-word" data-tr="ovozi baland">목소리 큰</span> 두 친구가 <span class="cn-word" data-pos="verb" data-tr="janjallashmoq">다투기</span> 시작했다. 지수는 둘 사이에 앉아 있었을 뿐인데, 화가 난 두 사람이 서로에게 던진 <span class="cn-word" data-tr="qattiq soʻzlar">거친 말</span>이 지수에게까지 <span class="cn-word" data-pos="verb" data-tr="tegib ketmoq">튀었다</span>. "너는 누구 편이야? 말해 봐!" 둘 다 지수를 <span class="cn-word" data-pos="verb" data-tr="siqmoq, bosim oʻtkazmoq">몰아세웠다</span>. 아무 <span class="cn-word" data-tr="ayb">잘못</span>도 없<strong>는데도</strong> 말이다. 지수는 한숨을 쉬었다. "고래 싸움에 새우 등 터진다더니…"</p>
<p>어른들의 세계에서도 <span class="cn-word" data-pos="adv" data-tr="tez-tez">자주</span> 일어난다. 부모님이 다투면 아이의 마음이 다치고, 두 회사가 싸우면 <span class="cn-word" data-tr="xodimlar">직원들</span>이 힘들어진다. 이 속담은 힘센 사람들에게 보내는 <span class="cn-word" data-tr="ogohlantirish">경고</span>다. 당신들의 싸움은 당신들만의 일이 아니다. <span class="cn-word" data-pos="adv" data-tr="atrofda">주변에서</span> 아무 죄 없는 새우들이 다치고 있다.</p>
<p>그리고 새우들에게 주는 <span class="cn-word" data-tr="maslahat">조언</span>도 있다. 고래들이 싸우기 시작하면 — 편을 들지 말고, 일단 그 <span class="cn-word" data-tr="oraliq, orasi">사이</span>에서 <span class="cn-word" data-pos="verb" data-tr="chetlashmoq">비켜나라</span>.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Ikki tuya urishsa, oʻrtasida chivin oʻlar» — kattalar toʻqnashuvida jabrni kichiklar tortadi. Koreyslarda tuya oʻrnida kit, chivin oʻrnida krevetka — dengiz xalqi-da! 🌊
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄴ/는데도",
                "meaning":  "Kutilganga zid: ...ganiga qaramay, ...sa ham.",
                "examples": ["아무 잘못도 없는데도 몰아세웠다.", "열심히 공부했는데도 시험이 어려웠어요."],
            },
            {
                "pattern":  "-았/었을 뿐이다",
                "meaning":  "Cheklash: shunchaki ...gan edi xolos (boshqa hech narsa).",
                "examples": ["둘 사이에 앉아 있었을 뿐인데 피해를 입었다.", "저는 사실을 말했을 뿐이에요."],
            },
        ],
        "questions": [
            {
                "text":        "지수는 왜 '새우'와 같은 상황이 되었습니까?",
                "choices":     ["싸움을 먼저 시작해서", "두 친구 사이에 앉아 있다가 싸움에 휘말려서", "새우를 좋아해서"],
                "answer":      1,
                "explanation": "Jisu shunchaki ikkovining orasida oʻtirgan edi — janjal boshlangach, «kimning tarafidasan?» deb ikkalasi ham unga bosim oʻtkazdi. Aybsiz boʻlaturib jabr koʻrdi — aynan krevetka holati.",
            },
            {
                "text":        "이 속담이 힘센 사람들에게 주는 경고는 무엇입니까?",
                "choices":     ["더 세게 싸우라는 것", "그들의 싸움이 죄 없는 주변 사람을 다치게 한다는 것", "새우를 잡지 말라는 것"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: «sizlarning janjalingiz faqat sizniki emas — atrofdagi aybsiz krevetkalar jabr koʻryapti». Ota-ona janjali — bola diliga, kompaniyalar jangi — xodimlarga uradi.",
            },
            {
                "text":        "글쓴이가 '새우들'에게 주는 조언은 무엇입니까?",
                "choices":     ["한쪽 편을 확실히 들어라", "싸움이 시작되면 그 사이에서 비켜나라", "고래보다 커져라"],
                "answer":      1,
                "explanation": "Oxirgi jumla: taraf olmang, avvalo oradan chetlaning (비켜나라) — kitlar jangida krevetkaning eng toʻgʻri yoʻli xavfsiz masofa.",
            },
        ],
    },

    # ── 13 ───────────────────────────────────────────────────────────────
    {
        "title":   "하늘이 무너져도 솟아날 구멍이 있다",
        "summary": "«Osmon qulasa ham chiqib ketadigan teshik topiladi» — eng ogʻir vaziyatda ham yoʻl bor. Umidsizlanmang!",
        "order":   13,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🌩️ 🕳️ 🌅</div>
<p>"하늘이 무너져도 솟아날 구멍이 있다." 하늘이 <span class="cn-word" data-pos="verb" data-tr="qulamoq">무너지는</span> 것은 상상할 수 있는 가장 큰 <span class="cn-word" data-tr="falokat">재앙</span>이다. 그런 일이 일어나<strong>더라도</strong> <span class="cn-word" data-pos="verb" data-tr="otilib chiqmoq">솟아날</span> <span class="cn-word" data-tr="teshik">구멍</span>은 있다는 뜻이다. 아무리 <span class="cn-word" data-pos="adj" data-tr="umidsiz">절망적인</span> 상황에도 <span class="cn-word" data-tr="chiqish yoʻli">해결책</span>은 반드시 있다는 희망의 속담이다.</p>
<p>민호 아버지의 이야기다. 이십 년 다닌 회사가 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> 문을 닫았다. 아버지는 하늘이 무너지는 것 같았다고 한다. 며칠 동안 잠도 못 자고 밥도 못 먹었다. 그런데 <span class="cn-word" data-tr="tasodifan">우연히</span> 옛 동료에게서 전화가 왔다. "우리 작은 가게를 하나 열려고 하는데, 너처럼 <span class="cn-word" data-pos="adj" data-tr="tajribali">경험 많은</span> 사람이 필요해." 아버지는 그 가게에서 다시 시작했고, 삼 년 뒤에는 회사에 다닐 때보다 더 <span class="cn-word" data-pos="adj" data-tr="baxtli">행복해졌다</span>. 아버지는 지금도 말한다. "그때는 끝인 줄 알았<strong>더니</strong>, 그게 새로운 시작이었어."</p>
<p>이 속담의 핵심은 구멍이 <span class="cn-word" data-pos="adv" data-tr="oʻz-oʻzidan">저절로</span> 나타나지 않는다는 점이다. 하늘이 무너졌을 때 <span class="cn-word" data-pos="verb" data-tr="taslim boʻlmoq">주저앉아</span> 우는 사람에게는 구멍이 보이지 않는다. <span class="cn-word" data-pos="verb" data-tr="izlamoq">찾는</span> 사람에게만 보인다. 그러니 힘든 일이 닥쳤을 때 이 속담을 <span class="cn-word" data-pos="verb" data-tr="eslamoq">떠올리며</span> 고개를 들고 주위를 둘러보라. 어딘가에 반드시 당신의 구멍이 있다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Har qorongʻu kechaning yorugʻ tongi bor» — eng zulmat tun ham tong bilan tugaydi. Koreyslar buni yanada kuchli aytadi: hatto osmon qulasa ham — yoʻl bor!
</div>''',
        "grammar": [
            {
                "pattern":  "-았/었더니",
                "meaning":  "Oʻtmish tajriba + kutilmagan natija: ...gan edim, (qarasam) ...",
                "examples": ["끝인 줄 알았더니 새로운 시작이었다.", "아침에 일어났더니 눈이 와 있었어요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 줄 알다",
                "meaning":  "Notoʻgʻri bilib turish: ... deb oʻylagan edim (aslida boshqacha).",
                "examples": ["그때는 끝인 줄 알았다.", "오늘이 토요일인 줄 알았어요."],
            },
        ],
        "questions": [
            {
                "text":        "민호 아버지에게 '무너진 하늘'은 무엇이었습니까?",
                "choices":     ["집이 무너진 것", "이십 년 다닌 회사가 문을 닫은 것", "전화가 고장 난 것"],
                "answer":      1,
                "explanation": "Yigirma yil ishlagan kompaniyasi toʻsatdan yopildi — bu unga «osmon qulagandek» tuyuldi. «Teshik» esa eski hamkasbning qoʻngʻirogʻi boʻlib chiqdi.",
            },
            {
                "text":        "글에 따르면 '구멍'은 누구에게 보입니까?",
                "choices":     ["주저앉아 우는 사람에게", "찾는 사람에게", "모든 사람에게 저절로"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: teshik oʻz-oʻzidan koʻrinmaydi — yigʻlab oʻtirgan odam uni koʻrmaydi, faqat IZLAGAN odam topadi. Maqol harakatga chaqiradi, kutishga emas.",
            },
        ],
    },

    # ── 14 ───────────────────────────────────────────────────────────────
    {
        "title":   "배보다 배꼽이 더 크다",
        "summary": "«Qorindan kindik katta» — asosiy narsadan uning qoʻshimchasi kattaroq yoki qimmatroq boʻlib ketgan gʻalati holat haqida.",
        "order":   14,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🎁 ⚖️ 💸</div>
<p>"배보다 배꼽이 더 크다." <span class="cn-word" data-tr="qorin">배</span>는 크고 <span class="cn-word" data-tr="kindik">배꼽</span>은 그 위의 작은 점이다. 그런데 배꼽이 배보다 크다면? 뭔가 <span class="cn-word" data-pos="adv" data-tr="teskari, chappa">거꾸로</span> 된 것이다. <span class="cn-word" data-tr="asosiy narsa">주된 것</span>보다 <span class="cn-word" data-tr="qoʻshimcha narsa">딸린 것</span>이 더 커졌을 때 쓰는 속담이다.</p>
<p>지수의 <span class="cn-word" data-tr="onlayn xarid">인터넷 쇼핑</span> 이야기다. 지수는 삼천 원짜리 <span class="cn-word" data-tr="telefon gʻilofi">휴대폰 케이스</span>를 발견하고 <span class="cn-word" data-pos="adj" data-tr="xursand">신이 나서</span> 주문 버튼을 눌렀다. 그런데 마지막 화면에서 <span class="cn-word" data-pos="verb" data-tr="qotib qolmoq">멈칫했다</span>. <span class="cn-word" data-tr="yetkazib berish haqi">배송비</span>가 오천 원이었던 것이다! 물건은 삼천 원인데 배송비가 오천 원 — <span class="cn-word" data-pos="adv" data-tr="aynan">그야말로</span> 배보다 배꼽이 더 큰 상황이다.</p>
<p>이런 일은 생활 <span class="cn-word" data-tr="hamma joyda">곳곳에</span> 있다. 만 원짜리 선물을 사면서 <span class="cn-word" data-tr="oʻrash, upakovka">포장</span>에 이만 원을 쓰는 사람. 공짜 <span class="cn-word" data-tr="kupon">쿠폰</span>을 쓰<strong>려고</strong> 두 시간 <span class="cn-word" data-pos="verb" data-tr="yoʻl bosmoq">운전해서</span> 기름값을 더 쓰는 사람. 무료 게임을 시작했다가 게임 <span class="cn-word" data-tr="ichki buyum">아이템</span>에 월급의 <span class="cn-word" data-tr="yarmi">절반</span>을 쓰는 사람.</p>
<p>이 속담은 우리에게 <span class="cn-word" data-pos="adv" data-tr="doim">항상</span> 이렇게 물으라고 한다. "지금 나의 배는 무엇이고, 배꼽은 무엇인가?" <span class="cn-word" data-tr="maqsad">목적</span>과 <span class="cn-word" data-tr="vosita">수단</span>이 <span class="cn-word" data-pos="verb" data-tr="oʻrin almashmoq">뒤바뀌지</span> 않았는지 확인하라는 것이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Eshagidan toʻshagi qimmat» — eshakning oʻzidan ustidagi toʻshagi qimmat boʻlsa, ish chappasiga ketgan. Koreyslarda buni tana rasmi bilan aytadi: qorindan kindik katta!
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)려고",
                "meaning":  "Maqsad: ...moqchi boʻlib, ... uchun.",
                "examples": ["공짜 쿠폰을 쓰려고 두 시간 운전했다.", "한국에서 일하려고 한국어를 배워요."],
            },
            {
                "pattern":  "그야말로",
                "meaning":  "Taʼkid: soʻzning toʻliq maʼnosida, aynan.",
                "examples": ["그야말로 배보다 배꼽이 더 큰 상황이다.", "그 공연은 그야말로 최고였어요."],
            },
        ],
        "questions": [
            {
                "text":        "지수의 상황에서 '배'와 '배꼽'은 각각 무엇입니까?",
                "choices":     ["배 = 배송비, 배꼽 = 케이스", "배 = 케이스 값, 배꼽 = 배송비", "배 = 휴대폰, 배꼽 = 지수"],
                "answer":      1,
                "explanation": "Asosiy narsa (배) — 3000 vonlik gʻilof; qoʻshimchasi (배꼽) — 5000 vonlik yetkazib berish haqi. Qoʻshimcha asosiydan katta — maqolning aynan oʻzi.",
            },
            {
                "text":        "이 속담이 우리에게 하라고 하는 질문은 무엇입니까?",
                "choices":     ["더 싼 물건이 어디 있는가", "목적과 수단이 뒤바뀌지 않았는가", "배송은 언제 오는가"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: «hozir mening asosiy maqsadim nima, qoʻshimchasi nima?» — maqsad va vosita oʻrin almashib ketmaganini tekshirib turish kerak.",
            },
        ],
    },

    # ── 15 ───────────────────────────────────────────────────────────────
    {
        "title":   "꿩 먹고 알 먹기",
        "summary": "«Qirgʻovulini ham, tuxumini ham yeyish» — bitta ish bilan ikki foyda koʻrish. Bir oʻq bilan ikki quyon!",
        "order":   15,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🐦 🥚 😋</div>
<p>"꿩 먹고 알 먹기." <span class="cn-word" data-tr="qirgʻovul">꿩</span>은 옛날 한국 사람들이 즐겨 <span class="cn-word" data-pos="verb" data-tr="ovlamoq">사냥하던</span> 새다. 어느 날 사냥꾼이 꿩을 잡았는데, 그 <span class="cn-word" data-tr="uya">둥지</span>에 <span class="cn-word" data-tr="tuxum">알</span>까지 있었다. 꿩도 먹고 알도 먹고 — 한 번의 <span class="cn-word" data-tr="mehnat, urinish">수고</span>로 두 가지 <span class="cn-word" data-tr="foyda">이득</span>을 얻은 것이다.</p>
<p>일상에서 이런 <span class="cn-word" data-pos="adj" data-tr="omadli">운 좋은</span> 상황은 생각보다 많다. 민호는 매일 학교까지 사십 분을 <span class="cn-word" data-pos="verb" data-tr="piyoda yurmoq">걸어</span> 다니기로 했다. 버스비를 <span class="cn-word" data-pos="verb" data-tr="tejamoq">아끼는</span> <strong>김에</strong> 운동도 되니, 그야말로 꿩 먹고 알 먹기다. 지수는 한국 드라마를 <span class="cn-word" data-tr="oʻzbekcha subtitr">자막</span> 없이 보기 시작했다. 재미도 있고 한국어 <span class="cn-word" data-tr="tinglab tushunish">듣기 실력</span>도 늘고 — 역시 꿩 먹고 알 먹기다.</p>
<p>같은 뜻의 표현이 <span class="cn-word" data-pos="adv" data-tr="juda koʻp">아주 많다</span>는 것도 재미있다. 한자어로는 <span class="cn-word" data-tr="bir tosh bilan ikki qush">일석이조</span>(一石二鳥), 또 다른 속담으로는 "도랑 치고 가재 잡는다"도 있다. 어느 나라 사람이든 한 번에 두 가지 이득을 얻는 것을 <span class="cn-word" data-pos="verb" data-tr="yaxshi koʻrmoq">좋아하는</span> 모양이다.</p>
<p>공부 <span class="cn-word" data-tr="usul, sir">비법</span>에도 쓸 수 있다. 좋아하는 한국 노래의 <span class="cn-word" data-tr="qoʻshiq matni">가사</span>를 외워 보라. 노래도 부르고 단어도 외우고 — 꿩 먹고 알 먹기의 <span class="cn-word" data-pos="adj" data-tr="mukammal">완벽한</span> 예다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Bir oʻq bilan ikki quyon» — bitta harakat, ikki natija. Koreyslarda quyon oʻrnida qirgʻovul va uning tuxumi. Xitoycha varianti 일석이조 — «bir tosh, ikki qush». 🎯
</div>''',
        "grammar": [
            {
                "pattern":  "-는 김에",
                "meaning":  "Qoʻshimcha imkoniyat: ...gan (boʻlgan) mahalda, shu bahona.",
                "examples": ["버스비를 아끼는 김에 운동도 된다.", "시장에 가는 김에 과일도 사 올게요."],
            },
            {
                "pattern":  "-는 모양이다",
                "meaning":  "Taxmin (kuzatuvga asoslangan): ...ga oʻxshaydi, shekilli.",
                "examples": ["누구든 두 가지 이득을 좋아하는 모양이다.", "밖에 비가 오는 모양이에요."],
            },
        ],
        "questions": [
            {
                "text":        "민호의 이야기에서 '꿩'과 '알'은 무엇입니까?",
                "choices":     ["버스비 절약과 운동", "학교와 집", "꿩고기와 달걀"],
                "answer":      0,
                "explanation": "Minho piyoda qatnab BIR ish qildi, undan IKKI foyda chiqdi: avtobus puli tejaldi (qirgʻovul) va sport boʻldi (tuxum). ③ soʻzma-soʻz tuzoq.",
            },
            {
                "text":        "이 속담과 같은 뜻의 표현은 무엇입니까?",
                "choices":     ["우물 안 개구리", "일석이조", "소 잃고 외양간 고친다"],
                "answer":      1,
                "explanation": "Matnda aytilgan: xitoycha 일석이조 (bir tosh — ikki qush) aynan shu maʼnoda. Qolgan ikkisi — bu toʻplamdagi boshqa maqollar, maʼnolari boshqa.",
            },
            {
                "text":        "글쓴이가 제안한 '꿩 먹고 알 먹기' 공부법은 무엇입니까?",
                "choices":     ["단어장을 두 권 사는 것", "좋아하는 노래의 가사를 외우는 것", "시험을 두 번 보는 것"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: sevimli qoʻshiq matnini yodlang — ham qoʻshiq aytasiz, ham soʻz yodlaysiz. Bir ish, ikki foyda — kursimizning ham sevimli usuli! 🎵",
            },
        ],
    },
]
