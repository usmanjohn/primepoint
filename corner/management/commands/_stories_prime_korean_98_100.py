# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-98 … PK-100. KOLLEKSIYA TUGADI (92 matn).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 / 반말 da gaplashadi.
Mavzu — 정보문 va 인생 이야기 navbatma-navbat:
   98 — 정보문: surgundan kelgan xatlar (정약용, 1801–1818) —
        거늘 aynan oʻz uyida: klassik xat tilida
   99 — 인생 이야기: 새옹지마 masalining qayta hikoyasi + zamonaviy
        davomi (toc ruxsat bergan “folk-tale retelling” shakli)
  100 — 정보문: “끝까지 간 사람들” — tilni oxirigacha oʻrganganlar
        haqida. Bu — 100-darsning matni, va u ataylab OʻQUVCHINING
        OʻZIGA murojaat qilib tugaydi.

Kumulyativ qoida: butun kurs ochiq — bu oxirgi uchlik.
PK-98 matnida 사자성어 (99) yoʻq. PK-99 matnida 새옹지마 bor, chunki
u oʻsha darsning oʻz materiali. PK-100 matnida 작심삼일 (99) va
셈이다 (91) birga ishlaydi.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다,
(느)ㄴ다면, 다는 것, 라는, 처럼, 에 따르면, 는가 — oʻrganilmagan,
ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_98_100.py --author=prime
"""

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Prime Korean Readings",
    "description": (
        "Prime Korean darslarining oʻqish matnlari — har biri oʻz darsining "
        "grammatikasini matn ichida koʻrsatadi. Lugʻat izohlari va audio bilan."
    ),
    "order": 2,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # PK-98 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "유배지에서 온 편지",
        "summary": (
            "PK-98 matni. 1801-yilda surgun qilingan olim oʻn sakkiz yil "
            "davomida oʻgʻillariga xat yozdi. Xatlarning mazmuni deyarli "
            "hamisha bir xil edi: oʻqi, yoz, yozib bor. Tushuntiruvchi "
            "matn, 한다체 da."
        ),
        "order":   98,
        "grammar": [
            {
                "pattern":  "-거늘 — …ku, …ekan-ku",
                "meaning":  "Adabiy va maqol tili. Matnda u ataylab "
                            "faqat <b>qoʻshtirnoq ichida</b> — "
                            "ikki yuz yil oldingi xatda — keladi. "
                            "Hikoyachi esa oddiy 한다체 da qoladi.",
                "examples": ["“짐승도 제 새끼를 가르치거늘, 하물며 사람이랴.”"],
            },
            {
                "pattern":  "하물며 … (이)랴",
                "meaning":  "거늘 ning doimiy jufti: “qolaversa "
                            "…mi?”. Javob berilmaydi — savolning "
                            "oʻzi xulosa. Oʻzbek maqollari ham "
                            "aynan shunday tuzilgan.",
                "examples": ["하물며 사람이랴."],
            },
            {
                "pattern":  "Nega bu qolip yozma matnda qoladi",
                "meaning":  "거늘 bugungi kunda gapirilmaydi — u "
                            "faqat <b>oʻqiladi</b>. Shuning uchun "
                            "uni ishlata bilish emas, <b>tanib "
                            "olish</b> kerak. Matn buni koʻrsatib "
                            "beradi: qolip klassik xatda, hikoya "
                            "esa zamonaviy tilda.",
                "examples": ["이백 년 전의 글이지만 문장은 어렵지 않다."],
            },
        ],
        "body": '''<p>1801년에 한 <span class="cn-word" data-tr="olim">학자</span>가 <span class="cn-word" data-tr="surgun">유배</span>를 갔다. 이름은 <span class="cn-word" data-tr="Chong Yagyong">정약용</span>이었다. 그때 마흔 살이었다.</p>

<p><span class="cn-word" data-tr="surgun joyi">유배지</span>는 <span class="cn-word" data-tr="Kanjin (joy nomi)">강진</span>이었다. 서울에서 멀었다. 그는 그곳에서 십팔 년을 살았다.</p>

<p>정약용에게는 두 아들이 있었다. 아버지가 <span class="cn-word" data-tr="jinoyatchi">죄인</span>이 되었기 때문에 아들들은 <span class="cn-word" data-tr="davlat imtihoni">과거 시험</span>을 볼 수 없었다. 집안은 <span class="cn-word" data-pos="verb" data-tr="qulab tushdi">무너졌다</span>.</p>

<p>그는 아들들에게 편지를 썼다. 십팔 년 동안 <span class="cn-word" data-tr="oʻnlab xat">수십 통</span>을 보냈다.</p>

<p>편지의 <span class="cn-word" data-tr="mazmun">내용</span>은 대부분 같았다. 읽어라. 써라. <span class="cn-word" data-pos="verb" data-tr="yozib bor">기록해라</span>.</p>

<p>한 편지에 이런 문장이 있다.</p>

<p>“<span class="cn-word" data-tr="hayvon">짐승</span>도 제 <span class="cn-word" data-tr="bolasi">새끼</span>를 <span class="cn-word" data-pos="verb" data-tr="oʻrgatadi-ku">가르치거늘</span>, <span class="cn-word" data-pos="adv" data-tr="qolaversa insonmi?">하물며 사람이랴</span>.”</p>

<p>또 다른 편지에서 그는 이렇게 썼다. “우리 집은 이제 <span class="cn-word" data-tr="mansab, amal">벼슬</span>을 할 수 없다. 그러나 책을 읽는 것은 아무도 <span class="cn-word" data-pos="verb" data-tr="toʻsa olmaydi">막지 못한다</span>.”</p>

<p>그는 아들들에게 <span class="cn-word" data-tr="sabzavot">채소</span>를 <span class="cn-word" data-pos="verb" data-tr="yetishtirish usuli">기르는 법</span>도 가르쳤다. 돈을 <span class="cn-word" data-pos="verb" data-tr="tejash">아끼는</span> 법도 썼다. 그리고 손님을 <span class="cn-word" data-pos="verb" data-tr="kutib olish">대접하는</span> 법도 썼다.</p>

<p>정약용은 유배지에서 오백 권이 넘는 책을 썼다.</p>

<p>1818년에 그는 집으로 돌아왔다. 두 아들은 벼슬을 하지 못했다. 그러나 둘 다 학자가 되었다.</p>

<p>지금 그 편지들은 책으로 <span class="cn-word" data-pos="verb" data-tr="chiqqan">나와 있다</span>. 이백 년 전의 글이지만 문장은 어렵지 않다.</p>

<p>한 <span class="cn-word" data-tr="tadqiqotchi">연구자</span>는 이렇게 말한다. “그 편지의 힘은 <span class="cn-word" data-tr="bilim">지식</span>이 아니에요. 그는 매일 썼어요. 십팔 년 동안요.”</p>''',
        "questions": [
            {
                "text": "Nega Chong Yagyongning oʻgʻillari davlat "
                        "imtihonini topshira olmadi?",
                "choices": [
                    "Pullari yoʻq edi",
                    "Otasi jinoyatchi hisoblangani uchun",
                    "Juda yosh edilar",
                    "Surgunda yashagani uchun",
                ],
                "answer": 1,
                "explanation": "“아버지가 죄인이 되었기 때문에 아들들은 "
                               "과거 시험을 볼 수 없었다.” Oila mansab "
                               "yoʻlini butunlay yoʻqotgan edi.",
            },
            {
                "text": "“짐승도 제 새끼를 가르치거늘, 하물며 사람이랴” — bu "
                        "gap qanday tuzilgan?",
                "choices": [
                    "Avval past narsa (hayvon) haqida dalil, keyin "
                    "javobsiz savol — “qolaversa insonmi?”",
                    "Ikkita mustaqil xabar",
                    "Savol va javob",
                    "Buyruq va sabab",
                ],
                "answer": 0,
                "explanation": "거늘 + 하물며 … (이)랴 — pastdan yuqoriga "
                               "qarab dalil keltirish. Xulosa ataylab "
                               "aytilmaydi: savolning oʻzi xulosa.",
            },
            {
                "text": "Tadqiqotchining fikricha, xatlarning kuchi "
                        "nimada edi?",
                "choices": [
                    "Muallifning bilimida",
                    "Har kuni, oʻn sakkiz yil davomida yozilganida",
                    "Chiroyli tilida",
                    "Oʻgʻillarning mansabga erishganida",
                ],
                "answer": 1,
                "explanation": "“그 편지의 힘은 지식이 아니에요. 그는 매일 "
                               "썼어요. 십팔 년 동안요.” Va oʻgʻillar "
                               "mansab olmadi — lekin ikkalasi ham olim "
                               "boʻldi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-99 — 인생 이야기 (옛이야기 + 오늘)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "할아버지와 말 한 마리",
        "summary": (
            "PK-99 matni. 새옹지마 masalining qayta hikoyasi — va oʻsha "
            "hikoyani nabirasiga aytgan bobo. Uch marta uchinchi "
            "marotaba maʼlum boʻladi: hali hech narsa maʼlum emas. "
            "Hayot hikoyasi, 한다체 da."
        ),
        "order":   99,
        "grammar": [
            {
                "pattern":  "새옹지마 — hayotning yaxshi-yomoni maʼlum emas",
                "meaning":  "Matnning birinchi yarmi — aynan shu "
                            "사자성어 kelib chiqqan masal. Iborani "
                            "yodlashning eng yaxshi yoʻli — uning "
                            "hikoyasini bilish.",
                "examples": ["이것이 새옹지마다."],
            },
            {
                "pattern":  "(으)ㄹ지도 모르다 (PK-73) qaytadan",
                "meaning":  "Boboning butun falsafasi shu bitta "
                            "qolipda: “bu baxt boʻlishi ham "
                            "mumkin”. Matn uni ikki marta, "
                            "aynan bir xil ohangda takrorlaydi.",
                "examples": ["“이것이 복이 될지도 모릅니다.”",
                             "“이것이 화가 될지도 모릅니다.”"],
            },
            {
                "pattern":  "Masal va bugun",
                "meaning":  "Toc ruxsat bergan shakl — <b>folk-tale "
                            "retelling</b>. Birinchi yarim: eski "
                            "masal. Ikkinchi yarim: oʻsha masalni "
                            "eshitgan bolaning oʻz hayoti. Ikkinchisi "
                            "birinchisini isbotlaydi.",
                "examples": ["그 회사는 오 년 전에 문을 닫았다."],
            },
        ],
        "body": '''<p>옛날 <span class="cn-word" data-tr="shimoliy chegara">북쪽 국경</span>에 한 <span class="cn-word" data-tr="chol, keksa kishi">노인</span>이 살았다. 사람들은 그를 <span class="cn-word" data-tr="Seong (chol ismi)">새옹</span>이라고 불렀다.</p>

<p>어느 날 노인의 말이 <span class="cn-word" data-pos="verb" data-tr="yoʻqoldi">사라졌다</span>. <span class="cn-word" data-tr="qoʻshnilar">이웃</span>들이 와서 <span class="cn-word" data-pos="verb" data-tr="taskin berdi">위로했다</span>. “<span class="cn-word" data-tr="afsus, achinarli">안됐어요</span>.”</p>

<p>노인은 웃었다. “이것이 <span class="cn-word" data-tr="baxt">복</span>이 <span class="cn-word" data-pos="verb" data-tr="boʻlishi ham mumkin">될지도 모릅니다</span>.”</p>

<p>몇 달 뒤에 그 말이 돌아왔다. 그런데 혼자가 아니었다. 좋은 말 한 마리를 <span class="cn-word" data-pos="verb" data-tr="boshlab keldi">데리고 왔다</span>.</p>

<p>이웃들이 <span class="cn-word" data-pos="verb" data-tr="tabrikladi">축하했다</span>. “정말 잘됐어요!”</p>

<p>노인은 또 웃었다. “이것이 <span class="cn-word" data-tr="balo, kulfat">화</span>가 될지도 모릅니다.”</p>

<p>노인의 아들이 그 새 말을 탔다. 그리고 떨어져서 다리가 <span class="cn-word" data-pos="verb" data-tr="sindi">부러졌다</span>.</p>

<p>이웃들이 다시 왔다. 노인은 같은 말을 했다.</p>

<p>일 년 뒤에 <span class="cn-word" data-tr="urush">전쟁</span>이 났다. 마을의 젊은 남자들이 모두 <span class="cn-word" data-tr="harbiy xizmat">군대</span>에 갔다. <span class="cn-word" data-tr="oʻntadan toʻqqiztasi">열에 아홉</span>이 돌아오지 못했다.</p>

<p>노인의 아들은 다리 때문에 가지 않았다.</p>

<p>이것이 <span class="cn-word" data-tr="hayotning yaxshi-yomoni maʼlum emas">새옹지마</span>다.</p>

<p>나는 이 이야기를 열두 살에 할아버지에게서 들었다. 그때는 <span class="cn-word" data-pos="adj" data-tr="qiziqarli">재미있는</span> 옛날이야기였다.</p>

<p>스물다섯 살에 나는 회사 <span class="cn-word" data-tr="suhbat, intervyu">면접</span>에서 떨어졌다. 세 번째였다. 그날 할아버지에게 전화했다.</p>

<p>할아버지는 이야기를 다시 하지 않았다. <span class="cn-word" data-pos="adv" data-tr="uning oʻrniga">대신</span> 이렇게 물었다.</p>

<p>“지금 몇 살이냐?”</p>

<p>“스물다섯이요.”</p>

<p>“그럼 아직 모르는 거다.”</p>

<p>지금 나는 서른넷이다. 그 회사는 오 년 전에 문을 닫았다.</p>

<p>할아버지는 <span class="cn-word" data-tr="oʻtgan yildan oldingi yil">재작년</span>에 <span class="cn-word" data-pos="verb" data-tr="vafot etdi">세상을 떠났다</span>.</p>

<p>나는 아직도 <span class="cn-word" data-tr="kelajak ishlari">앞일</span>을 모른다. 그러나 이제 그것이 <span class="cn-word" data-pos="adj" data-tr="qoʻrqinchli emas">무섭지 않다</span>.</p>''',
        "questions": [
            {
                "text": "Masalda chol har safar nima dedi?",
                "choices": [
                    "“Bu baxt boʻlishi ham mumkin” / “Bu kulfat boʻlishi "
                    "ham mumkin” — yaʼni hali hech narsa maʼlum emas",
                    "“Bu Xudoning irodasi”",
                    "“Men buni oldindan bilgandim”",
                    "Hech narsa demadi",
                ],
                "answer": 0,
                "explanation": "Chol yaxshilikka ham, yomonlikka ham bir "
                               "xil javob berdi: <b>(으)ㄹ지도 모르다</b> "
                               "(PK-73). Voqea tugamagan ekan, baho "
                               "berish erta.",
            },
            {
                "text": "Boboning “그럼 아직 모르는 거다” degan javobi nimani "
                        "anglatadi?",
                "choices": [
                    "Nabirasi hali yosh, hech narsa bilmaydi",
                    "Yigirma besh yoshda hayotning qanday tugashi hali "
                    "maʼlum emas — masalning aynan oʻzi",
                    "Bobo savolni tushunmadi",
                    "Nabirasi yana urinishi kerak",
                ],
                "answer": 1,
                "explanation": "Bobo masalni qaytarmadi — uni "
                               "<b>ishlatdi</b>. Va keyingi jumla buni "
                               "isbotlaydi: “그 회사는 오 년 전에 문을 "
                               "닫았다.”",
            },
            {
                "text": "Matnning oxirgi jumlasi nima deydi?",
                "choices": [
                    "Hikoyachi endi kelajakni bila oladi",
                    "Hikoyachi hali ham kelajakni bilmaydi — lekin endi "
                    "bu uni qoʻrqitmaydi",
                    "Hikoyachi bobosini sogʻinadi",
                    "Hikoyachi boshqa ish topdi",
                ],
                "answer": 1,
                "explanation": "“나는 아직도 앞일을 모른다. 그러나 이제 "
                               "그것이 무섭지 않다.” 새옹지마 bilimni "
                               "emas, <b>xotirjamlikni</b> beradi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-100 — 정보문 (kollektsiyaning yakuni)
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "끝까지 간 사람들",
        "summary": (
            "PK-100 matni va butun kollektsiyaning yakuni. Til "
            "oʻrganishni boshlaganlarning uch foizi oxirigacha boradi. "
            "Ular nimasi bilan farq qilgan? Tushuntiruvchi matn, "
            "한다체 da — va oxirgi banddagi murojaat aynan sizga."
        ),
        "order":   100,
        "grammar": [
            {
                "pattern":  "(으)ㄴ/는 셈이다 (PK-91) + 작심삼일 (PK-99)",
                "meaning":  "Matnning eng muhim jumlasi ikkala "
                            "darsni birga ishlatadi: “작심삼일을 백 번 "
                            "하면 삼백 일이 되는 <b>셈이다</b>”. "
                            "Hisob-kitob qolipi shu yerda "
                            "hazilni dalilga aylantiradi.",
                "examples": ["작심삼일을 백 번 하면 삼백 일이 되는 셈이다."],
            },
            {
                "pattern":  "Uch qavatli 정보문 tuzilishi",
                "meaning":  "첫째 · 둘째 · 셋째 — TOPIK 읽기 va "
                            "쓰기 ning asosiy skeleti. Matnni shu "
                            "shaklda oʻqisangiz, savolga javob "
                            "topish tezlashadi.",
                "examples": ["첫째, 처음이 너무 쉽다.",
                             "둘째, 중간이 보이지 않는다.",
                             "셋째, 끝이 없어 보인다."],
            },
            {
                "pattern":  "Oxirgi band — oʻquvchiga murojaat",
                "meaning":  "Matn oʻzi haqida emas, <b>oʻqiyotgan "
                            "odam</b> haqida tugaydi. Bu — 92 ta "
                            "matndan iborat kollektsiyaning yakuni: "
                            "siz bu bandni koreyschada oʻqiyapsiz, "
                            "va bu matnning butun dalili shu.",
                "examples": ["지금 이 글을 읽는 사람은 이미 알파벳을 지났다."],
            },
        ],
        "body": '''<p>언어를 배우기 시작하는 사람은 많다. 끝까지 가는 사람은 적다.</p>

<p>한 언어 학습 <span class="cn-word" data-tr="ilova">앱</span>의 <span class="cn-word" data-tr="maʼlumot">자료</span>를 보면, <span class="cn-word" data-pos="verb" data-tr="roʻyxatdan oʻtgan">등록한</span> 사람의 <span class="cn-word" data-tr="yarmi">절반</span>이 첫 주에 그만둔다. 한 달 뒤에는 십 퍼센트만 남는다. 일 년 뒤에는 삼 퍼센트다.</p>

<p>이유는 <span class="cn-word" data-tr="isteʼdod">재능</span>이 아니다. 연구자들은 세 가지를 말한다.</p>

<p>첫째, 처음이 너무 쉽다. <span class="cn-word" data-tr="alifbo">알파벳</span>과 <span class="cn-word" data-tr="salomlashish soʻzlari">인사말</span>은 하루면 끝난다. 그래서 사람들은 자기가 빠르다고 생각한다. 그런데 세 달 뒤에 <span class="cn-word" data-tr="tezlik">속도</span>가 <span class="cn-word" data-pos="verb" data-tr="sekinlashadi">느려진다</span>. 그때 많은 사람이 자기 <span class="cn-word" data-tr="qobiliyat">능력</span>을 <span class="cn-word" data-pos="verb" data-tr="shubha qiladi">의심한다</span>.</p>

<p>둘째, <span class="cn-word" data-tr="oʻrtasi">중간</span>이 보이지 않는다. 처음에는 매일 새로운 것을 배운다. 중간에는 같은 것을 다시 배운다. <span class="cn-word" data-tr="rivoj, oʻsish">발전</span>이 눈에 보이지 않는다. 그러나 그때 <span class="cn-word" data-tr="mahorat">실력</span>이 가장 많이 <span class="cn-word" data-pos="verb" data-tr="oshadi">는다</span>.</p>

<p>셋째, 끝이 없어 보인다. 단어는 계속 나온다. 문법도 계속 나온다. 그래서 “언제 끝나요?”라고 묻는다. 답은 “끝나지 않아요”다.</p>

<p>삼 퍼센트를 <span class="cn-word" data-pos="verb" data-tr="tekshirgan">조사한</span> <span class="cn-word" data-tr="tadqiqot">연구</span>가 있다. <span class="cn-word" data-tr="umumiy jihat">공통점</span>은 두 가지였다.</p>

<p>하나는 시간이 아니라 <span class="cn-word" data-tr="marta, son">횟수</span>였다. 일주일에 한 번 세 시간 공부한 사람보다 매일 이십 분 공부한 사람이 <span class="cn-word" data-pos="adv" data-tr="ancha">훨씬</span> <span class="cn-word" data-pos="verb" data-tr="oldinda edi">앞섰다</span>.</p>

<p>또 하나는 더 <span class="cn-word" data-pos="adj" data-tr="oddiy">단순했다</span>. 그들은 그만두지 않았다. 쉬는 날도 있었고, 한 달 동안 안 한 사람도 있었다. 그러나 다시 돌아왔다.</p>

<p>한 연구자는 이렇게 말한다. “우리는 매일 하는 사람을 찾고 있었어요. 그런데 찾은 것은 <span class="cn-word" data-pos="verb" data-tr="qaytib keladigan">돌아오는</span> 사람이었어요.”</p>

<p><span class="cn-word" data-tr="qaror uch kun turadi">작심삼일</span>이라는 말이 있다. 그러나 작심삼일을 백 번 하면 삼백 일이 <span class="cn-word" data-pos="verb" data-tr="boʻlgan hisob">되는 셈이다</span>.</p>

<p>지금 이 글을 읽는 사람은 이미 알파벳을 지났다. 그리고 문장을 지났다. 그리고 이 <span class="cn-word" data-tr="band, abzats">문단</span>을 한국어로 읽고 있다.</p>

<p>그것으로 <span class="cn-word" data-pos="adj" data-tr="yetarli">충분하다</span>.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, koʻpchilik nega tashlab ketadi?",
                "choices": [
                    "Isteʼdodi yetishmagani uchun",
                    "Boshi juda oson, oʻrtasi koʻrinmaydi, oxiri yoʻqdek "
                    "tuyulgani uchun",
                    "Vaqti boʻlmagani uchun",
                    "Oʻqituvchi yomon boʻlgani uchun",
                ],
                "answer": 1,
                "explanation": "“이유는 재능이 아니다.” Uchta sabab: "
                               "첫째 처음이 너무 쉽다 · 둘째 중간이 보이지 "
                               "않는다 · 셋째 끝이 없어 보인다.",
            },
            {
                "text": "Oxirigacha borganlarning ikkita umumiy jihati "
                        "nima edi?",
                "choices": [
                    "Koʻp vaqt sarflash va yaxshi xotira",
                    "Uzoq emas, tez-tez shugʻullanish; va tashlab "
                    "ketganda ham qaytib kelish",
                    "Chet elda yashash va kitob oʻqish",
                    "Yosh boshlash va kundalik yuritish",
                ],
                "answer": 1,
                "explanation": "“하나는 시간이 아니라 횟수였다… 또 하나는 "
                               "더 단순했다. 그들은 그만두지 않았다.” Va "
                               "tadqiqotchining gapi: “찾은 것은 "
                               "<b>돌아오는</b> 사람이었어요.”",
            },
            {
                "text": "Matn nega oʻquvchining oʻziga murojaat qilib "
                        "tugaydi?",
                "choices": [
                    "Chunki oʻquvchi bu bandni koreyschada oʻqiyotgani — "
                    "matnning butun dalilini isbotlaydi",
                    "Chunki matnda joy qolmagan",
                    "Chunki bu odatiy yakun",
                    "Chunki oʻquvchidan javob kutilmoqda",
                ],
                "answer": 0,
                "explanation": "“지금 이 글을 읽는 사람은 이미 알파벳을 "
                               "지났다… 이 문단을 한국어로 읽고 있다. "
                               "그것으로 충분하다.” Matn uch foiz haqida "
                               "yozilgan — va uni oʻqiyotgan odam oʻsha "
                               "uch foizda.",
            },
        ],
    },
]
