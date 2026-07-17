# 속담 이야기 (Koreys maqollari) — stories 26–30 (collection complete at 30!). Style: STYLE_GUIDE_CORNER.md §5d.
# Import: python manage.py import_corner corner/management/commands/_stories_proverbs_26_30.py --author=prime

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
    # ── 26 ───────────────────────────────────────────────────────────────
    {
        "title":   "가재는 게 편이다",
        "summary": "«Qisqichbaqa — krabning tarafida» — oʻxshashlar bir-birini yoqlaydi. Adolat oʻrniga «oʻzimizniki» deb turadiganlar haqida.",
        "order":   26,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🦞 🤝 🦀</div>
<p>"가재는 게 편이다." <span class="cn-word" data-tr="daryo qisqichbaqasi">가재</span>와 <span class="cn-word" data-tr="krab">게</span>는 둘 다 <span class="cn-word" data-tr="qattiq qobiq">딱딱한 껍데기</span>와 <span class="cn-word" data-tr="qisqich">집게</span>를 가진, 생김새가 아주 비슷한 동물이다. 그래서 <span class="cn-word" data-tr="janjal, tortishuv">다툼</span>이 생기면 가재는 <span class="cn-word" data-pos="adv" data-tr="oʻylab ham oʻtirmay">따져 보지도 않고</span> 자기와 닮은 게의 <span class="cn-word" data-tr="taraf, tomon">편</span>을 든다는 뜻이다. 사람도 자기와 비슷한 사람, <span class="cn-word" data-tr="yaqin odam">가까운 사람</span>의 편을 들<strong>기 마련이다</strong>.</p>
<p>학교에서의 장면이다. 축구를 하다가 두 반 사이에 <span class="cn-word" data-tr="bahs">시비</span>가 붙었다. 공이 <span class="cn-word" data-tr="chiziq">선</span>을 나갔는지 안 나갔는지를 두고 싸우는데, 이상하게도 일 반 학생들은 <span class="cn-word" data-pos="adv" data-tr="bir ovozdan">하나같이</span> "안 나갔다"고 하고, 이 반 학생들은 모두 "나갔다"고 한다. 공은 하나인데 <span class="cn-word" data-tr="haqiqat">진실</span>은 두 개가 된 것이다. <span class="cn-word" data-tr="oʻzimizniki degan his">내 편이라서 그런지</span> 눈에 보이는 것도 달라진다.</p>
<p>이 속담은 두 가지로 쓰인다. 첫째, <span class="cn-word" data-tr="tarafkashlik">편들기</span>를 <span class="cn-word" data-pos="verb" data-tr="tanqid qilmoq">비판할</span> 때. "심판이 자기 <span class="cn-word" data-tr="yurt, shahar">고향</span> 팀에만 <span class="cn-word" data-pos="adj" data-tr="yumshoq">너그럽네</span>. 가재는 게 편이라더니." 둘째, <span class="cn-word" data-pos="adv" data-tr="tabiiy ravishda">자연스럽게</span> 서로를 이해하는 사이를 말할 때도 쓴다.</p>
<p>그러나 진짜 <span class="cn-word" data-pos="adj" data-tr="ishonchli, obroʻli">믿음직한</span> 사람은 가재이면서도 게의 <span class="cn-word" data-tr="xato">잘못</span>을 말할 줄 아는 사람이다. <span class="cn-word" data-tr="doʻstlik">우정</span>은 편을 드는 것이 아니라 <span class="cn-word" data-pos="adv" data-tr="toʻgʻri">바르게</span> 말해 주는 것이기 때문이다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Qargʻa qargʻaning koʻzini choʻqimas» — oʻzinikini himoya qilish, «oʻzimizniki» deb koʻz yumish. Koreyslarda qargʻalar oʻrnida — qobiqli qarindoshlar: qisqichbaqa va krab.
</div>''',
        "grammar": [
            {
                "pattern":  "-(이)라서 그런지",
                "meaning":  "Taxminiy sabab: ... boʻlgani uchunmi, (aniqmas, lekin shunga oʻxshaydi).",
                "examples": ["내 편이라서 그런지 눈에 보이는 것도 다르다.", "월요일이라서 그런지 길이 막히네요."],
            },
            {
                "pattern":  "-(으)ㄹ 줄 알다",
                "meaning":  "Qobiliyat/bilish: ...ishni bilmoq, ...ay olmoq.",
                "examples": ["친구의 잘못을 말할 줄 아는 사람이 믿음직하다.", "김치를 담글 줄 알아요?"],
            },
        ],
        "questions": [
            {
                "text":        "축구 이야기에서 '진실이 두 개가 되었다'는 것은 무슨 뜻입니까?",
                "choices":     ["공이 두 개였다는 뜻", "각 반이 자기 편에게 유리하게 다르게 보았다는 뜻", "경기가 두 번 있었다는 뜻"],
                "answer":      1,
                "explanation": "Toʻp bitta, voqea bitta — lekin har sinf OʻZ tarafiga foydali qilib koʻrdi: biri «chiqmadi», biri «chiqdi». Tarafkashlik hatto koʻrishni ham oʻzgartiradi.",
            },
            {
                "text":        "글쓴이에 따르면 '진짜 믿음직한 사람'은 누구입니까?",
                "choices":     ["언제나 친구 편만 드는 사람", "친한 사이라도 잘못을 바르게 말해 주는 사람", "싸움을 피하는 사람"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: qisqichbaqa boʻlaturib krabning xatosini ayta oladigan odam. Doʻstlik — koʻr-koʻrona taraf olish emas, toʻgʻrisini aytish.",
            },
        ],
    },

    # ── 27 ───────────────────────────────────────────────────────────────
    {
        "title":   "콩 심은 데 콩 나고 팥 심은 데 팥 난다",
        "summary": "«Loviya ekkan joydan loviya, mosh ekkan joydan mosh unadi» — har bir natijaning aniq sababi bor. Nima eksangiz, shuni oʻrasiz.",
        "order":   27,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🫘 🌱 🫘</div>
<p>"콩 심은 데 콩 나고 팥 심은 데 팥 난다." <span class="cn-word" data-tr="loviya">콩</span>을 <span class="cn-word" data-pos="verb" data-tr="ekmoq">심은</span> 곳에서는 콩이 나고, <span class="cn-word" data-tr="qizil mosh">팥</span>을 심은 곳에서는 팥이 난다. 너무나 <span class="cn-word" data-pos="adj" data-tr="oddiy, ravshan">당연한</span> 말 같지만, 바로 그 당연함이 이 속담의 힘이다. 세상 모든 결과에는 그에 맞는 <span class="cn-word" data-tr="sabab">원인</span>이 있으며, 심은 <strong>대로</strong> 거두게 된다는 뜻이다.</p>
<p>민호는 시험 전날 밤에만 <span class="cn-word" data-pos="adv" data-tr="shoshilinch">벼락치기로</span> 공부하고 "왜 나는 <span class="cn-word" data-tr="baho, natija">성적</span>이 안 오르지?"라고 <span class="cn-word" data-pos="verb" data-tr="nolimoq">불평한다</span>. 지수는 매일 삼십 분씩 <span class="cn-word" data-pos="adv" data-tr="muntazam">꾸준히</span> 공부하고 조용히 좋은 성적을 받는다. 콩을 심은 사람이 콩을 <span class="cn-word" data-pos="verb" data-tr="yigʻib olmoq, oʻrmoq">거두고</span>, 아무것도 심지 않은 사람은 아무것도 거두지 못한다. <span class="cn-word" data-tr="moʻjiza">기적</span>을 바라는 것은 팥을 심어 놓고 콩이 나기를 기다리는 것과 같다.</p>
<p>이 속담은 <span class="cn-word" data-tr="tasalli">위로</span>이기도 하다. 지금 노력하는데 결과가 안 보여서 <span class="cn-word" data-pos="adj" data-tr="xavotirli">불안한가</span>? 걱정하지 마라. <span class="cn-word" data-tr="urugʻ">씨앗</span>은 심는 <span class="cn-word" data-pos="adv" data-tr="darhol">즉시</span> 싹이 나지 않는다. 하지만 콩을 심었다면 언젠가 반드시 콩이 난다. <span class="cn-word" data-tr="tuproq">땅</span>은 <span class="cn-word" data-pos="adv" data-tr="hech qachon">결코</span> 거짓말을 하지 않는다. 결과는 결국 노력하<strong>기 나름이다</strong>.</p>
<p>비슷한 표현으로 "뿌린 대로 거둔다"도 자주 쓴다. 시험에도, 인생에도 나오는 말이니 함께 기억해 두자.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Nima eksang, shuni oʻrasan» — soʻzma-soʻz bir xil maqol! Koreyslar buni ikki don — loviya va mosh misolida yanada aniq aytadi.
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄴ/는 대로",
                "meaning":  "Muvofiqlik: ...ganidek, ...ganiga yarasha.",
                "examples": ["심은 대로 거두게 된다.", "들은 대로 이야기해 주세요."],
            },
            {
                "pattern":  "-기 나름이다",
                "meaning":  "Bogʻliqlik: hammasi ...ishga bogʻliq, ...ishiga qarab boʻladi.",
                "examples": ["결과는 노력하기 나름이다.", "행복은 생각하기 나름이에요."],
            },
        ],
        "questions": [
            {
                "text":        "'기적을 바라는 것'을 글쓴이는 무엇에 비유했습니까?",
                "choices":     ["콩을 심고 콩을 기다리는 것", "팥을 심어 놓고 콩이 나기를 기다리는 것", "씨앗을 많이 사는 것"],
                "answer":      1,
                "explanation": "Moʻjiza kutish = mosh ekib, loviya unishini kutish — sabab boshqa-yu, natijani boshqa kutish. Tuproq esa aldamaydi: nima eksangiz, shu unadi.",
            },
            {
                "text":        "이 속담이 '위로'가 되는 이유는 무엇입니까?",
                "choices":     ["노력하면 언젠가 반드시 결과가 나오기 때문에", "씨앗이 바로 싹이 나기 때문에", "콩이 맛있기 때문에"],
                "answer":      0,
                "explanation": "Urugʻ darhol unmaydi — lekin loviya ekilgan boʻlsa, ALBATTA loviya chiqadi. Natija koʻrinmayotgan paytda ham mehnat bekor ketmasligiga ishonch — maqolning tasalli tomoni.",
            },
        ],
    },

    # ── 28 ───────────────────────────────────────────────────────────────
    {
        "title":   "미운 아이 떡 하나 더 준다",
        "summary": "«Yoqmagan bolaga bitta ortiq tteok ber» — yoqtirmagan odamingizga atayin yaxshiroq muomala qiling: mojaro soʻnadi, koʻngil yumshaydi.",
        "order":   28,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">😠 🍡 😊</div>
<p>"미운 아이 떡 하나 더 준다." <span class="cn-word" data-pos="adj" data-tr="yoqimsiz, koʻngilga oʻtirmagan">미운</span> 아이에게 떡을 하나 <span class="cn-word" data-pos="adv" data-tr="qoʻshimcha, ortiqroq">더</span> 준다는 뜻이다. 이상하지 않은가? 예쁜 아이도 아니고 미운 아이에게 왜 더 줄까? 여기에 <span class="cn-word" data-tr="ajdodlar donoligi">조상들의 지혜</span>가 숨어 있다.</p>
<p>미운 사람을 미워하는 <span class="cn-word" data-pos="adv" data-tr="ochiqchasiga">티를 내면</span> 어떻게 될까? 상대도 그것을 느끼고 나를 더 미워한다. <span class="cn-word" data-tr="adovat">미움</span>이 미움을 낳고, 관계는 점점 나빠진다. 미워하<strong>다가는</strong> 결국 둘 다 <span class="cn-word" data-tr="jarohat">상처</span>만 남는다. 그래서 옛사람들은 <span class="cn-word" data-pos="adv" data-tr="teskarisiga, aksincha">거꾸로</span> 행동했다. 미운 사람일<strong>수록</strong> <span class="cn-word" data-pos="adv" data-tr="atayin">일부러</span> 더 잘해 주는 것이다. 떡 하나를 더 받은 아이는 <span class="cn-word" data-pos="verb" data-tr="yumshamoq">누그러지고</span>, 주는 사람의 마음속 미움도 <span class="cn-word" data-pos="adv" data-tr="asta-sekin">서서히</span> 녹는다.</p>
<p>지수의 반에 <span class="cn-word" data-pos="adv" data-tr="doim">늘</span> 지수에게 <span class="cn-word" data-pos="adj" data-tr="tikanli, achchiq">가시 돋친</span> 말을 하는 친구가 있었다. 지수는 <span class="cn-word" data-pos="verb" data-tr="qarshilik qilmoq">맞서느니</span> <span class="cn-word" data-tr="chora, usul">차라리</span> 이 속담을 시험해 보기로 했다. 그 친구의 생일에 <span class="cn-word" data-pos="adv" data-tr="birinchi boʻlib">제일 먼저</span> 축하 <span class="cn-word" data-tr="xat, xatcha">쪽지</span>를 건넸다. 친구는 얼굴이 빨개지더니 <span class="cn-word" data-pos="adv" data-tr="oʻshandan beri">그 뒤로</span> 가시 돋친 말이 <span class="cn-word" data-pos="adv" data-tr="sezilarli darajada">눈에 띄게</span> 줄었다. 몇 달 뒤 그 친구가 고백했다. "사실 네가 부러워서 그랬어. 미안해."</p>
<p>미움에 미움으로 <span class="cn-word" data-pos="verb" data-tr="javob bermoq">맞서면</span> 싸움이 되고, 미움에 떡으로 맞서면 <span class="cn-word" data-tr="doʻst">친구</span>가 된다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Yaxshilikka yaxshilik — har kishining ishidir, yomonlikka yaxshilik — er kishining ishidir» — yomonlikka yaxshilik bilan javob berish mardlik. Koreyslarda buning oʻlchovi — bitta ortiqcha tteok!
</div>''',
        "grammar": [
            {
                "pattern":  "-다가는",
                "meaning":  "Ogohlantirish: shu yoʻlda davom etilsa (yomon natija keladi).",
                "examples": ["미워하다가는 둘 다 상처만 남는다.", "그렇게 놀다가는 시험에 떨어져요."],
            },
            {
                "pattern":  "-느니 (차라리)",
                "meaning":  "Tanlov: ...gandan koʻra (yaxshisi) ...",
                "examples": ["맞서느니 차라리 잘해 주기로 했다.", "기다리느니 차라리 걸어가겠어요."],
            },
        ],
        "questions": [
            {
                "text":        "옛사람들은 왜 미운 아이에게 떡을 더 주었습니까?",
                "choices":     ["미운 아이가 배가 고파서", "미움을 티 내면 관계가 더 나빠지기 때문에", "떡이 남아서"],
                "answer":      1,
                "explanation": "Yoqtirmaslik sezdirilsa — qarshi tomon ham sezadi, adovat kuchayadi. Teskari yoʻl — atayin yaxshiroq muomala — ikkala tomonning ham koʻnglini yumshatadi.",
            },
            {
                "text":        "지수의 실험 결과는 어떻게 되었습니까?",
                "choices":     ["친구가 더 심하게 괴롭혔다", "가시 돋친 말이 줄고 결국 사과를 받았다", "지수가 전학을 갔다"],
                "answer":      1,
                "explanation": "Tugʻilgan kunida birinchi boʻlib tabrik bergach, achchiq gaplar sezilarli kamaydi, oylar oʻtib doʻst «hasad qilgandim, kechir» deb tan oldi. Tteok gʻalaba qildi!",
            },
        ],
    },

    # ── 29 ───────────────────────────────────────────────────────────────
    {
        "title":   "서당 개 삼 년이면 풍월을 읊는다",
        "summary": "«Maktab iti uch yilda sheʼr oʻqiydi» — bilim muhitida uzoq yurgan odam oʻzi sezmagan holda oʻrganib qoladi. Muhitning kuchi!",
        "order":   29,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">🏫 🐕 📜</div>
<p>"서당 개 삼 년이면 풍월을 읊는다." <span class="cn-word" data-tr="qadimgi maktab">서당</span>은 옛날 한국의 학교로, 아이들이 소리 내어 <span class="cn-word" data-tr="sheʼr va matnlar">글</span>을 읽으며 공부하던 곳이다. 그 서당에서 삼 년을 산 <span class="cn-word" data-tr="it">개</span>는 매일 아이들의 <span class="cn-word" data-tr="oʻqish ovozi">글 읽는 소리</span>를 듣는다. 그러다 보면 개<strong>조차</strong> <span class="cn-word" data-tr="sheʼr (tabiat haqidagi)">풍월</span>을 <span class="cn-word" data-pos="verb" data-tr="oʻqimoq, kuylamoq (sheʼrni)">읊게</span> 된다는 재미있는 <span class="cn-word" data-tr="mubolagʻa">과장</span>이다. 물론 진짜 개가 시를 읽는 것은 아니다 — <span class="cn-word" data-tr="muhit">환경</span>의 힘이 그만큼 크다는 뜻이다.</p>
<p>어떤 분야든 그 <span class="cn-word" data-tr="yaqin atrof">곁</span>에 오래 있으면, <span class="cn-word" data-pos="adv" data-tr="atayin oʻrganmasa ham">배우려 하지 않아도</span> 자기도 모르<strong>는 사이에</strong> 물이 든다. 식당집 아이는 <span class="cn-word" data-tr="retsept">요리법</span>을 알고, 음악가의 아이는 <span class="cn-word" data-tr="musiqa ohangi">가락</span>을 안다. 지수는 한국 드라마를 삼 년 봤을 뿐인데 어느 날 자기도 모르게 "어떡해!"라고 <span class="cn-word" data-pos="verb" data-tr="baqirib yubormoq">외치고</span> 있었다. 서당 개가 된 것이다!</p>
<p>이 속담의 <span class="cn-word" data-tr="amaliy saboq">실전 교훈</span>은 강력하다. 무언가를 잘하고 싶다면 <span class="cn-word" data-tr="iroda">의지</span>만 믿지 말고 <span class="cn-word" data-pos="adv" data-tr="avvalo">먼저</span> 환경을 바꿔라. 한국어를 잘하고 싶으면 한국어가 <span class="cn-word" data-pos="verb" data-tr="eshitilib turmoq">들리는</span> 환경 속으로 들어가라. 책상 앞의 세 시간보다 <span class="cn-word" data-tr="muhit ichidagi">환경 속</span> 삼 년이 더 힘이 셀 때가 많다.</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Qozonga yaqin yursang — qorasi yuqar» — muhit albatta taʼsir qiladi (bizda koʻproq yomon taʼsir haqida aytiladi). Koreyslarda esa ijobiysi: maktab yonidagi itga ham ilm «yuqadi»! Demak muhitni toʻgʻri tanlang.
</div>''',
        "grammar": [
            {
                "pattern":  "-는 사이에",
                "meaning":  "Sezilmagan oraliqda: ...ayotgan orada, oʻzi bilmagan holda.",
                "examples": ["자기도 모르는 사이에 물이 든다.", "이야기하는 사이에 버스가 와 버렸어요."],
            },
            {
                "pattern":  "조차",
                "meaning":  "Kuchaytirilgan «hatto»: eng kutilmagani ham.",
                "examples": ["개조차 풍월을 읊게 된다.", "물조차 마실 시간이 없었어요."],
            },
        ],
        "questions": [
            {
                "text":        "이 속담에서 '개가 풍월을 읊는다'는 것은 무엇을 강조하는 과장입니까?",
                "choices":     ["개가 똑똑하다는 것", "환경의 힘이 그만큼 크다는 것", "서당이 시끄럽다는 것"],
                "answer":      1,
                "explanation": "It chindan sheʼr oʻqimaydi — bu mubolagʻa (과장). Maʼnosi: bilim muhitida uzoq boʻlgan HAR KIM (hatto it ham!) oʻzi sezmay oʻrganadi — muhit shunchalik kuchli.",
            },
            {
                "text":        "이 속담의 '실전 교훈'은 무엇입니까?",
                "choices":     ["의지만 강하면 된다", "잘하고 싶은 것이 있으면 먼저 환경을 바꿔라", "개를 서당에 보내라"],
                "answer":      1,
                "explanation": "Uchinchi xatboshi: faqat irodaga tayanmang — oʻzingizni oʻsha narsa «eshitilib turadigan» muhitga qoʻying. Stol oldidagi 3 soatdan muhit ichidagi 3 yil kuchliroq.",
            },
        ],
    },

    # ── 30 ───────────────────────────────────────────────────────────────
    {
        "title":   "우물을 파도 한 우물을 파라",
        "summary": "«Quduq qazisang ham — bitta quduqni qazi» — oʻnta ishni chala qilguncha, bittasini oxirigacha yetkaz. Toʻplamning yakuniy maqoli!",
        "order":   30,
        "body": '''<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:14px;text-align:center;font-size:2.2em;letter-spacing:.15em;margin:0 0 16px;">⛏️ 1️⃣ 💧</div>
<p>"우물을 파도 한 우물을 파라." 우물을 <span class="cn-word" data-pos="verb" data-tr="qazimoq">파려면</span> 한 곳을 <span class="cn-word" data-pos="adv" data-tr="chuqur">깊이</span> 파야 물이 나온다. 여기 조금, 저기 조금 파는 사람은 <span class="cn-word" data-tr="chuqurcha">구덩이</span>만 열 개 만들고 물은 한 <span class="cn-word" data-tr="tomchi">방울</span>도 얻지 못한다. 이 일 저 일에 손을 <span class="cn-word" data-pos="verb" data-tr="urinib koʻrmoq">대기만</span> 하는 사람에게 주는 <span class="cn-word" data-tr="ogohlantirish">경고</span>다.</p>
<p>어느 마을에 두 남자가 우물을 파기 시작했다. 첫째는 사흘을 파다가 물이 안 나오자 "여기는 <span class="cn-word" data-pos="adv" data-tr="shekilli">아무래도</span> 아니야" 하며 자리를 옮겼다. 옮기고 또 옮기고 — 일 년 동안 열 군데를 팠지만 전부 <span class="cn-word" data-pos="adj" data-tr="sayoz">얕은</span> 구덩이뿐이었다. 그는 <span class="cn-word" data-tr="chanqoqlik">목마름</span>으로 <span class="cn-word" data-pos="verb" data-tr="oʻlishiga oz qolmoq">죽을 뻔했다</span>. 둘째는 한 자리만 팠다. 백 일째 되던 날, 그의 <span class="cn-word" data-tr="belkurak">삽</span> 끝에서 <span class="cn-word" data-pos="adj" data-tr="muzdek">차가운</span> 물이 <span class="cn-word" data-pos="verb" data-tr="otilib chiqmoq">솟아올랐다</span>. 마을 사람들이 물었다. "포기하고 싶지 않았나?" 그가 답했다. "많이요. 하지만 물은 <span class="cn-word" data-pos="adv" data-tr="doim">언제나</span> 어제 멈춘 곳 바로 아래에 있다고 믿었지요."</p>
<p>재능이 없어서가 아니라 <span class="cn-word" data-pos="adv" data-tr="tez-tez">자주</span> 옮겨서 실패하는 사람이 많다. 외국어를 세 개 <span class="cn-word" data-pos="adv" data-tr="birvarakayiga">동시에</span> 시작하고 하나도 못 하는 사람, <span class="cn-word" data-tr="soha">전공</span>을 해마다 바꾸는 사람. 깊이는 시간이 만든다. 그리고 시간은 한 우물에만 <span class="cn-word" data-pos="verb" data-tr="toʻplanmoq">쌓인다</span>.</p>
<p>이 속담이 우리 속담 <span class="cn-word" data-tr="toʻplam">모음집</span>의 마지막인 데는 이유가 있다. 삼십 개의 속담을 <span class="cn-word" data-pos="adv" data-tr="oxirigacha">끝까지</span> 읽은 당신은 이미 한 우물을 판 사람이다. 그 <span class="cn-word" data-tr="quduq">우물</span>의 이름은 한국어다. 계속 파라 — 물이 <span class="cn-word" data-pos="adv" data-tr="tez orada">머지않아</span> 나온다. 화이팅!</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Oʻzbekchada:</strong> «Oʻn hunarni chala bilguncha, bir hunarni toʻla bil» — xuddi shu saboq! Oʻnta sayoz chuqurcha emas — bitta chuqur quduq. 💧
</div>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 뻔하다",
                "meaning":  "Sal boʻlmaganda: ...ay dedi, ...ishiga oz qoldi (lekin boʻlmadi).",
                "examples": ["목마름으로 죽을 뻔했다.", "늦잠을 자서 시험에 늦을 뻔했어요."],
            },
            {
                "pattern":  "-아/어서가 아니라",
                "meaning":  "Sababni toʻgʻrilash: ... uchun emas, balki (boshqa sabab).",
                "examples": ["재능이 없어서가 아니라 자주 옮겨서 실패한다.", "돈이 없어서가 아니라 시간이 없어서 못 가요."],
            },
        ],
        "questions": [
            {
                "text":        "첫째 남자가 실패한 이유는 무엇입니까?",
                "choices":     ["삽이 나빠서", "한 곳을 깊이 파지 않고 계속 자리를 옮겨서", "힘이 약해서"],
                "answer":      1,
                "explanation": "U bir yilda OʻN joyni qazidi — lekin hammasi sayoz chuqurcha boʻlib qoldi. Muammo kuchda emas, chuqurlikda: suv faqat bitta joyni oxirigacha qazganga chiqadi.",
            },
            {
                "text":        "둘째 남자를 버티게 한 믿음은 무엇이었습니까?",
                "choices":     ["물은 어제 멈춘 곳 바로 아래에 있다는 믿음", "다른 우물이 더 좋다는 믿음", "마을 사람들이 도와줄 것이라는 믿음"],
                "answer":      0,
                "explanation": "Uning javobi: «suv doim kecha toʻxtagan joyning tagida» — yaʼni taslim boʻlish arafasida gʻalaba turadi. Shu ishonch uni yuz kun qazishga yetakladi.",
            },
            {
                "text":        "글쓴이가 독자에게 '한 우물'이라고 말한 것은 무엇입니까?",
                "choices":     ["속담 책", "한국어", "우물 파기"],
                "answer":      1,
                "explanation": "Oxirgi xatboshi: 30 ta maqolni oxirigacha oʻqigan siz allaqachon bitta quduqni qazayotgan odamsiz — u quduqning nomi KOREYS TILI. Qazishda davom eting! 💧",
            },
        ],
    },
]
