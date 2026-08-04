# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-89 … PK-91 (에 달려 있다, 려던 참이다, 다름없다/셈이다).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 / 반말 da gaplashadi.
Mavzu — 인생 이야기 va 정보문 navbatma-navbat:
  89 — 인생 이야기: ikkinchi tinglov — natija hakamlarga, davom etish oʻziga
  90 — 정보문: “안 그래도 전화하려던 참이었어요” — tasodif haqidagi matn,
       matnning MAVZUSI aynan shu jumla (shuning uchun u koʻp takrorlanadi)
  91 — 인생 이야기: amakining ugʻra oshxonasi — sakkiz ming kun

Kumulyativ qoida: PK-91 gacha oʻrganilgan hamma narsa ochiq.
PK-89 matnida 려던 참 (90) va 다름없다/셈이다 (91) YOʻQ.
PK-90 matnida 다름없다/셈이다 (91) yoʻq.
다면서요 (92), 다니/라니 (93), (으)려니 하다 (94), (이)랍시고 (95),
기 짝이 없다 (96), (으)로 인해/말미암아 (97), 거늘/기로서니 (98) —
hech qaysisida yoʻq. PK-97 ni buzmaslik uchun sabab hamma joyda
때문에 bilan berilgan, 인해 bilan emas.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, 지요, ㅂ시다,
(느)ㄴ다면, 다는 것, 처럼 — oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_89_91.py --author=prime
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
    # PK-89 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "두 번째 오디션",
        "summary": (
            "PK-89 matni. Hana ikki marta tinglovdan oʻtolmadi. Ustozining "
            "bitta gapi esa nima nimaga bogʻliqligini oʻzgartirib yubordi. "
            "Hayot hikoyasi, 한다체 da."
        ),
        "order":   89,
        "grammar": [
            {
                "pattern":  "에 달려 있다 — …ga bogʻliq",
                "meaning":  "Natijani nima hal qilishini koʻrsatadi. "
                            "달리다 = “osilib turmoq”, shuning uchun "
                            "natija sababga <b>osilib turadi</b>.",
                "examples": ["실력은 연습에 달려 있어요.",
                             "무대는 마음먹기에 달려 있어요."],
            },
            {
                "pattern":  "에 · 에게 — narsa va odam",
                "meaning":  "Jonsiz otga <b>에</b>, odamga "
                            "<b>에게/한테</b>. Hikoyaning oxirgi ikki "
                            "jumlasi ataylab ikkalasini yonma-yon "
                            "qoʻyadi.",
                "examples": ["합격은 심사위원에게 달려 있었다.",
                             "계속하는 것은 하나에게 달려 있었다."],
            },
            {
                "pattern":  "기에 달려 있다",
                "meaning":  "Butun ishni ulash uchun PK-46 dagi "
                            "<b>기</b> otlashtirishi ishlatiladi. "
                            "마음먹기에 달려 있다 — Koreyada maqol "
                            "darajasidagi jumla.",
                "examples": ["무대는 마음먹기에 달려 있어요."],
            },
        ],
        "body": '''<p>하나는 열두 살부터 <span class="cn-word" data-tr="gitara">기타</span>를 쳤다. 학교 <span class="cn-word" data-tr="festival">축제</span> <span class="cn-word" data-tr="sahna">무대</span>에 세 번 올랐다. 친구들은 하나가 <span class="cn-word" data-tr="qachondir">언젠가</span> <span class="cn-word" data-tr="qoʻshiqchi">가수</span>가 될 거라고 말했다.</p>

<p>열아홉 살에 하나는 처음으로 큰 <span class="cn-word" data-tr="tinglov, ovoz sinovi">오디션</span>을 봤다. <span class="cn-word" data-tr="ariza topshirgan">지원자</span>가 삼천 명이었다. 하나는 <span class="cn-word" data-pos="verb" data-tr="oʻtolmadi">떨어졌다</span>.</p>

<p>집에 돌아온 날 하나는 기타를 <span class="cn-word" data-tr="shkaf">옷장</span>에 넣었다. 그리고 두 달 동안 <span class="cn-word" data-pos="verb" data-tr="chiqarmadi">꺼내지 않았다</span>.</p>

<p>어느 날 선생님이 하나를 불렀다. 십 년 동안 하나를 가르친 사람이었다.</p>

<p>“<span class="cn-word" data-tr="mahorat">실력</span>은 이미 <span class="cn-word" data-pos="adj" data-tr="yetarli">충분해요</span>. 삼천 명 중에서 실력이 <span class="cn-word" data-pos="adj" data-tr="yetishmagani uchun">부족해서</span> 떨어진 사람은 많지 않아요.”</p>

<p>“그럼 뭐가 <span class="cn-word" data-tr="muammo">문제</span>였어요?”</p>

<p>“무대에서 하나 씨는 <span class="cn-word" data-tr="hakamlar">심사위원</span> 얼굴만 봤어요. 노래는 보지 않았어요.”</p>

<p>선생님은 잠시 말을 <span class="cn-word" data-pos="verb" data-tr="toʻxtatdi">멈췄다</span>. 그리고 이렇게 말했다.</p>

<p>“실력은 <span class="cn-word" data-pos="verb" data-tr="mashqqa bogʻliq">연습에 달려 있어요</span>. 그런데 무대는 <span class="cn-word" data-pos="verb" data-tr="qatʼiy qarorga bogʻliq">마음먹기에 달려 있어요</span>.”</p>

<p>하나는 옷장을 열었다.</p>

<p>여섯 달 뒤에 두 번째 오디션이 있었다. 이번에는 심사위원을 보지 않았다. 노래만 봤다. 삼 분 동안 하나는 방에서 혼자 연습한 그 소리를 냈다.</p>

<p><span class="cn-word" data-tr="natija">결과</span>는 또 <span class="cn-word" data-tr="oʻtmadi (rad)">불합격</span>이었다.</p>

<p>그러나 무대에서 내려왔다. 그리고 울지 않았다. 그런데 기분이 좋았다.</p>

<p>지금 하나는 스물세 살이다. 아직 가수가 아니다. 작은 카페에서 한 달에 두 번 노래한다. 손님은 열 명쯤이다.</p>

<p><span class="cn-word" data-tr="imtihondan oʻtish">합격</span>은 <span class="cn-word" data-pos="verb" data-tr="hakamlarga bogʻliq edi">심사위원에게 달려 있었다</span>. 그러나 계속하는 것은 <span class="cn-word" data-pos="verb" data-tr="Hanaga bogʻliq edi">하나에게 달려 있었다</span>. 하나는 계속하기로 했다.</p>''',
        "questions": [
            {
                "text": "Ustoz Hananing birinchi tinglovdagi xatosini nimada "
                        "koʻrdi?",
                "choices": [
                    "Mahorati yetishmagan edi",
                    "Sahnada faqat hakamlarning yuziga qaragan, qoʻshiqqa "
                    "qaramagan",
                    "Notoʻgʻri qoʻshiq tanlagan",
                    "Kech kelgan",
                ],
                "answer": 1,
                "explanation": "“실력은 이미 충분해요… 심사위원 얼굴만 봤어요. "
                               "노래는 보지 않았어요.”",
            },
            {
                "text": "“실력은 연습에 달려 있어요. 그런데 무대는 마음먹기에 "
                        "달려 있어요.” — bu gapdagi qarama-qarshilik nima?",
                "choices": [
                    "Mashq keraksiz degani",
                    "Mahoratni mashq hal qiladi, sahnani esa boshqa narsa — "
                    "qatʼiy qaror — hal qiladi",
                    "Sahna mashqdan osonroq",
                    "Ikkalasi ham baxtga bogʻliq",
                ],
                "answer": 1,
                "explanation": "Ikkala jumlada ham bir xil qolip, lekin "
                               "<b>에</b> dan oldingi soʻz boshqa: 연습 va "
                               "마음먹기. Qolip aynan shuning uchun bor — "
                               "<b>nima hal qiladi</b>, deb koʻrsatish "
                               "uchun.",
            },
            {
                "text": "Matnning oxirgi ikki jumlasi nega 에게 ni ikki marta "
                        "ishlatadi?",
                "choices": [
                    "Chunki har ikkala gapda ham hal qiluvchi narsa — odam: "
                    "biri hakamlar, ikkinchisi Hananing oʻzi",
                    "Chunki 에 shakli xato",
                    "Chunki ikkalasi ham oʻtgan zamon",
                    "Tasodifan takrorlangan",
                ],
                "answer": 0,
                "explanation": "Jonli otga <b>에게</b> qoʻyiladi. Hikoyaning "
                               "butun fikri shu ikki jumlada: natija "
                               "boshqalarga bogʻliq, <b>davom etish esa "
                               "oʻzingizga</b>.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-90 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "안 그래도 전화하려던 참이었어요",
        "summary": (
            "PK-90 matni. Doʻstingizni oʻylagan soniyada undan qoʻngʻiroq "
            "keladi. Bu tasodifmi? Uch sabab — va nega bu jumla shunday "
            "yoqimli. Tushuntiruvchi matn, 한다체 da."
        ),
        "order":   90,
        "grammar": [
            {
                "pattern":  "(으)려던 참이다 — …ay deb turgan edim",
                "meaning":  "Niyat + <b>aynan shu soniya</b>. Deyarli "
                            "har doim javob sifatida keladi, chunki u "
                            "tasodifni bildiradi. Matnning mavzusi — "
                            "aynan shu jumla.",
                "examples": ["안 그래도 전화하려던 참이었어요.",
                             "지금 막 나가려던 참이었어요."],
            },
            {
                "pattern":  "안 그래도 …",
                "meaning":  "“Aytmasangiz ham, oʻzi ham”. Bu qolipning "
                            "eng koʻp uchraydigan boshlanishi — "
                            "butunligicha yodlab qoʻyish kerak "
                            "boʻlgan tayyor blok.",
                "examples": ["안 그래도 연락하려던 참이었어요."],
            },
            {
                "pattern":  "Nega 정보문 ga qoʻshtirnoq kerak",
                "meaning":  "(으)려던 참이다 — <b>ogʻzaki</b> qolip: u "
                            "faqat birinchi shaxs va ayni damda "
                            "ishlaydi. Shuning uchun tushuntiruvchi "
                            "matn uni qoʻshtirnoq ichida keltiradi, "
                            "hikoyachi esa 한다체 da qoladi.",
                "examples": ["우리는 웃으면서 말한다. “안 그래도 전화하려던 참이었어요.”"],
            },
        ],
        "body": '''<p>이런 일이 있다. 친구에게 전화하려고 휴대폰을 든다. 바로 그 <span class="cn-word" data-tr="lahza, soniya">순간</span> <span class="cn-word" data-tr="ekran">화면</span>에 그 친구의 이름이 <span class="cn-word" data-pos="verb" data-tr="chiqadi">뜬다</span>.</p>

<p>전화를 받고 우리는 웃으면서 말한다. “<span class="cn-word" data-pos="verb" data-tr="aytmasangiz ham qoʻngʻiroq qilay deb turgan edim">안 그래도 전화하려던 참이었어요</span>.”</p>

<p>한국 사람들은 이 문장을 자주 쓴다. 그런데 <span class="cn-word" data-tr="olimlar">과학자</span>들은 이것을 <span class="cn-word" data-tr="tasodif">우연</span>이라고 부르지 않는다. <span class="cn-word" data-tr="sabab">이유</span>가 세 가지 있다.</p>

<p>첫 번째 이유는 <span class="cn-word" data-tr="raqam">숫자</span>다. 우리는 하루에 <span class="cn-word" data-tr="oʻnlab">수십</span> 명을 생각한다. 그리고 일 년은 삼백육십오 일이다. 그러니까 “생각한 사람에게서 <span class="cn-word" data-tr="aloqa, xabar">연락</span>이 오는” 일은 언젠가 <span class="cn-word" data-pos="adv" data-tr="albatta">반드시</span> 일어난다. <span class="cn-word" data-tr="ehtimollik">확률</span>이 낮아도 <span class="cn-word" data-tr="imkoniyat">기회</span>가 많으면 결과는 나온다.</p>

<p>두 번째 이유는 <span class="cn-word" data-tr="xotira">기억</span>이다. 우리는 <span class="cn-word" data-pos="verb" data-tr="toʻgʻri chiqqan">맞은</span> 우연만 기억한다. 친구를 생각했지만 전화가 오지 않은 날은 수천 번이다. 그런 날은 아무도 기억하지 않는다. <span class="cn-word" data-tr="psixologiya">심리학</span>에서는 이것을 “<span class="cn-word" data-tr="tanlab eslash">선택적 기억</span>”이라고 부른다.</p>

<p>세 번째 이유가 가장 재미있다. 두 사람이 같은 시간에 같은 생각을 하는 것에는 이유가 있다. 같은 주에 같은 시험이 끝났다. 같은 <span class="cn-word" data-tr="video">영상</span>을 봤다. 같은 <span class="cn-word" data-tr="bayram">명절</span>이 <span class="cn-word" data-pos="verb" data-tr="yaqinlashadi">다가온다</span>. 우연 같은 일은 사실 같은 <span class="cn-word" data-tr="muhit, sharoit">환경</span> 때문이다.</p>

<p>그러나 이 문장이 <span class="cn-word" data-tr="yolgʻon">거짓말</span>인 것은 아니다.</p>

<p>“안 그래도 전화하려던 참이었어요”라는 말은 사실을 말하는 문장이 아니다. 이 말은 이런 <span class="cn-word" data-tr="maʼno">뜻</span>이다. “나도 당신을 생각하고 있었어요.”</p>

<p>그래서 이 문장을 들으면 기분이 <span class="cn-word" data-pos="verb" data-tr="yaxshilanadi">좋아진다</span>. 우연이 <span class="cn-word" data-pos="adj" data-tr="alohida boʻlgani uchun emas">특별해서가 아니다</span>. 그 사람이 나를 생각했기 때문이다.</p>

<p>한 <span class="cn-word" data-tr="tilshunos">언어학자</span>는 이렇게 말했다. “가장 자주 쓰는 문장은 <span class="cn-word" data-pos="adv" data-tr="odatda">대개</span> 가장 <span class="cn-word" data-tr="maʼlumot">정보</span>가 적은 문장이에요. 그런데 마음은 가장 많이 <span class="cn-word" data-pos="verb" data-tr="joylangan">담겨 있어요</span>.”</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, nega “oʻylagan odamdan qoʻngʻiroq "
                        "kelishi” tez-tez sodir boʻladi?",
                "choices": [
                    "Odamlar bir-birining fikrini oʻqiy oladi",
                    "Kunda oʻnlab odam haqida oʻylaymiz va yil 365 kun — "
                    "ehtimollik past boʻlsa ham, imkoniyat koʻp",
                    "Telefonlar shunday ishlaydi",
                    "Bu faqat Koreyada boʻladi",
                ],
                "answer": 1,
                "explanation": "“확률이 낮아도 기회가 많으면 결과는 나온다.” "
                               "Birinchi sabab — sof matematika.",
            },
            {
                "text": "“선택적 기억” bu yerda nimani anglatadi?",
                "choices": [
                    "Biz faqat toʻgʻri chiqqan tasodiflarni eslaymiz, "
                    "chiqmagan minglab kunlarni esa yoʻq",
                    "Biz eng muhim narsalarni tanlab eslaymiz",
                    "Xotira yoshga qarab zaiflashadi",
                    "Odamlar ataylab unutadi",
                ],
                "answer": 0,
                "explanation": "“친구를 생각했지만 전화가 오지 않은 날은 "
                               "수천 번이다. 그런 날은 아무도 기억하지 "
                               "않는다.”",
            },
            {
                "text": "Matn oxirida bu jumla haqidagi xulosa qanday?",
                "choices": [
                    "U yolgʻon, shuning uchun ishlatmaslik kerak",
                    "Unda maʼlumot kam, lekin koʻngil koʻp — u “men ham "
                    "sizni oʻylayotgan edim” degani",
                    "U faqat rasmiy nutqda ishlatiladi",
                    "U ilmiy jihatdan isbotlangan",
                ],
                "answer": 1,
                "explanation": "“가장 자주 쓰는 문장은 대개 가장 정보가 적은 "
                               "문장이에요. 그런데 마음은 가장 많이 담겨 "
                               "있어요.” Matn qolipni rad etmaydi — uning "
                               "asl vazifasini koʻrsatadi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-91 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "삼촌의 국숫집",
        "summary": (
            "PK-91 matni. Bozor ichidagi toʻrt stolli ugʻra oshxonasi, "
            "yigirma uch yil va sakkiz ming kun. Hisoblab koʻrilgan bir "
            "umr. Hayot hikoyasi, 한다체 da."
        ),
        "order":   91,
        "grammar": [
            {
                "pattern":  "(으)ㄴ/는 셈이다 — … hisob",
                "meaning":  "Sanab, xulosa chiqarish. Matnda ikkala "
                            "shakl ham bor: takrorlanadigan/davomiy "
                            "ish uchun <b>는 셈이다</b>, tugagan ish "
                            "uchun <b>(으)ㄴ 셈이다</b>.",
                "examples": ["이십삼 년은 팔천 일이 넘는 셈이다.",
                             "팔천 번 국물을 끓인 셈이다."],
            },
            {
                "pattern":  "(이)나 다름없다 — …dan farqi yoʻq",
                "meaning":  "Ikki narsani yonma-yon qoʻyib, “bular "
                            "orasida farq yoʻq” deydi. Oldida ot "
                            "turadi; feʼl boʻlsa avval <b>(으)ㄴ/는 "
                            "것</b> bilan otga aylantiriladi.",
                "examples": ["나에게 삼촌은 아버지나 다름없었다.",
                             "그것은 한 사람의 인생을 지킨 것이나 다름없다."],
            },
            {
                "pattern":  "걸려 있다 — osilib turibdi",
                "meaning":  "PK-89 dagi <b>달려 있다</b> ning ogʻasi: "
                            "아/어 있다 (PK-42) holat shakli. Bu yerda "
                            "u toʻgʻri, moddiy maʼnoda ishlatilgan — "
                            "peshtaxta yozuvi haqiqatan devorda osilib "
                            "turibdi.",
                "examples": ["지금 그 간판은 우리 집 벽에 걸려 있다."],
            },
        ],
        "body": '''<p>우리 삼촌은 이십삼 년 동안 <span class="cn-word" data-tr="ugʻra oshxonasi">국숫집</span>을 했다. 가게는 <span class="cn-word" data-tr="bozor">시장</span> 안에 있었다. <span class="cn-word" data-tr="stol">탁자</span>가 네 개, <span class="cn-word" data-tr="stul">의자</span>가 열두 개. 그게 <span class="cn-word" data-tr="hammasi">전부</span>였다.</p>

<p>삼촌에게는 아이가 없었다. 나에게 <span class="cn-word" data-pos="adj" data-tr="otadan farqi yoʻq edi">삼촌은 아버지나 다름없었다</span>.</p>

<p>학교가 끝나면 나는 가게로 갔다. 삼촌은 <span class="cn-word" data-tr="ugʻra, lagʻmon">국수</span>를 <span class="cn-word" data-pos="verb" data-tr="qaynatardi">삶고</span>, 나는 탁자를 <span class="cn-word" data-pos="verb" data-tr="artardim">닦았다</span>. 그리고 저녁에 남은 국수를 둘이 먹었다.</p>

<p>삼촌은 하루도 쉬지 않았다. <span class="cn-word" data-tr="bayram kunlari">명절</span>에도 문을 열었다. 나는 물었다.</p>

<p>“삼촌, 안 힘들어요?”</p>

<p>“쉬면 오는 사람이 <span class="cn-word" data-tr="bekorga yurish">헛걸음</span>을 해.”</p>

<p>일 년에 삼백육십 일이면, <span class="cn-word" data-pos="verb" data-tr="sakkiz ming kundan oshgan hisob">이십삼 년은 팔천 일이 넘는 셈이다</span>. <span class="cn-word" data-pos="verb" data-tr="sakkiz ming marta qaynatgan hisob">팔천 번 국물을 끓인 셈이다</span>.</p>

<p>작년에 시장이 <span class="cn-word" data-pos="verb" data-tr="yoʻq boʻldi">없어졌다</span>. 그 자리에 큰 <span class="cn-word" data-tr="bino">건물</span>이 <span class="cn-word" data-pos="verb" data-tr="qad rostladi">들어섰다</span>.</p>

<p>마지막 날 나는 가게에 갔다. 삼촌은 <span class="cn-word" data-tr="odatdagidek">평소와 같이</span> 국수를 삶고 있었다. 손님은 여섯 명이었다. 모두 이십 년 넘게 온 사람들이었다.</p>

<p>한 할아버지가 말했다.</p>

<p>“여기 국수를 못 먹으면 <span class="cn-word" data-pos="verb" data-tr="qishdan qanday oʻtamiz">겨울을 어떻게 나요</span>.”</p>

<p>삼촌은 웃기만 했다.</p>

<p>문을 닫고 삼촌은 <span class="cn-word" data-tr="peshtaxta yozuvi">간판</span>을 <span class="cn-word" data-pos="verb" data-tr="tushirdi">내렸다</span>. 그리고 나에게 주었다.</p>

<p>“이거 가져가.”</p>

<p>지금 그 간판은 우리 집 <span class="cn-word" data-tr="devor">벽</span>에 <span class="cn-word" data-pos="verb" data-tr="osilib turibdi">걸려 있다</span>.</p>

<p>삼촌은 <span class="cn-word" data-tr="boy">부자</span>가 되지 못했다. 그러나 팔천 번 그 자리에 있었다. 그것은 한 사람의 <span class="cn-word" data-tr="umr, hayot">인생</span>을 <span class="cn-word" data-pos="verb" data-tr="asragan bilan barobar">지킨 것이나 다름없다</span>.</p>''',
        "questions": [
            {
                "text": "Nega amaki bayramlarda ham doʻkonni ochardi?",
                "choices": [
                    "Bayramlarda mijoz koʻp boʻlgani uchun",
                    "Yopsa, kelgan odam bekorga yurgan boʻladi degani uchun",
                    "Uyda dam olishni yoqtirmagani uchun",
                    "Qarzi bor edi",
                ],
                "answer": 1,
                "explanation": "“쉬면 오는 사람이 헛걸음을 해.” Butun hikoya "
                               "shu bitta jumla ustiga qurilgan.",
            },
            {
                "text": "“이십삼 년은 팔천 일이 넘는 셈이다” — nega bu yerda "
                        "는 셈이다, keyingi jumlada esa (으)ㄴ 셈이다?",
                "choices": [
                    "Ikkalasi bir xil, farqi yoʻq",
                    "넘다 — hisobning oʻzi (davomiy, hozirgi), 끓이다 esa "
                    "tugagan ish — shuning uchun 끓인 셈이다",
                    "Birinchisi savol, ikkinchisi darak",
                    "Birinchisi sifat, ikkinchisi feʼl",
                ],
                "answer": 1,
                "explanation": "셈이다 aniqlovchi shaklga ergashadi: hozirgi/"
                               "davomiy ish → <b>는 셈이다</b>, tugagan ish "
                               "→ <b>(으)ㄴ 셈이다</b>.",
            },
            {
                "text": "Oxirgi jumlaning maʼnosi nima?",
                "choices": [
                    "Amaki boy boʻlmasa ham, sakkiz ming marta oʻsha "
                    "joyda boʻlgani — bir odamning umrini asragan bilan "
                    "barobar",
                    "Amaki oʻz umrini behuda oʻtkazdi",
                    "Doʻkon yopilgani yaxshi boʻldi",
                    "Peshtaxta yozuvi qimmat narsa edi",
                ],
                "answer": 0,
                "explanation": "“부자가 되지 못했다. <b>그러나</b> 팔천 번 그 "
                               "자리에 있었다.” 다름없다 shu yerda baho "
                               "beradi — kichik ish, katta maʼno.",
            },
        ],
    },
]
