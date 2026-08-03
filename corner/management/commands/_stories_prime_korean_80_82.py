# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-80 … PK-82 (봤자, 더라도/지라도/불구하고, 정도로/만큼).

Uslub: **문어체 / 한다체** (PK-74 dan boshlangan qoida). Hikoyachi
한다체 da, qoʻshtirnoq ichidagi odamlar 해요체 da gaplashadi.
Mavzu — 정보문 va 인생 이야기 navbatma-navbat:
  80 — 정보문: “vaqtni yutish” mumkinmi — unutish egri chizigʻi
  81 — 인생 이야기: yigirmata xat va yigirmanchisidagi bir jumla
  82 — 정보문: dunyodagi eng kichik va eng katta narsalar

Kumulyativ qoida: PK-82 gacha oʻrganilgan hamma narsa ochiq.
PK-80 matnida 더라도/지라도/불구하고 (81) va 정도로/만큼 (82) YOʻQ.
PK-81 matnida 정도로 / 만큼 (82) yoʻq.
에 불과하다 (83), 든지 (84), (으)나 마나 (85), (으)ㅁ으로써 (86),
(으)ㄹ 지경이다 (87) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄴ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때, (으)려면, (이)라도, ㅂ시다, (으)ㄴ 지
(davomiylik) — oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_80_82.py --author=prime
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
    # PK-80 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "벼락치기는 통하지 않는다",
        "summary": (
            "PK-80 matni. Imtihon oldidan tun boʻyi oʻqish nega ish "
            "bermaydi — unutish egri chizigʻi va tarqoq oʻqish haqida "
            "tushuntiruvchi matn."
        ),
        "order":   80,
        "grammar": [
            {
                "pattern":  "아/어 봤자 — …ganing bilan foydasi yoʻq",
                "meaning":  "Urinish mumkin, lekin natija oʻzgarmaydi. "
                            "Ichida PK-41 dagi 아/어 보다 turibdi, "
                            "shuning uchun oldiga zamon qoʻyilmaydi.",
                "examples": ["밤을 새워 봤자 다음 주에는 다 잊어버린다.",
                             "아무리 서둘러 봤자 뇌는 자기 속도로 움직인다."],
            },
            {
                "pattern":  "봤자 + soʻzlovchining bahosi",
                "meaning":  "봤자 dan keyin hamisha foydasizlik keladi: "
                            "소용없다, 사라진다, 마찬가지다. Shuning uchun bu "
                            "qolip dalilga asoslangan matnlarda juda "
                            "qulay — muallif xulosani darrov aytadi.",
                "examples": ["그 지식은 며칠 안에 사라진다.",
                             "제가 도와줘 봤자 소용없어요."],
            },
            {
                "pattern":  "한다체 — dalil tili",
                "meaning":  "Bu matn butunlay 한다체 da: 잊는다 · 사라진다 · "
                            "달라진다 · 아니다. TOPIK 읽기 dagi ilmiy "
                            "matnlar ham aynan shunday yoziladi.",
                "examples": ["사람은 배우고 한 시간 후에 절반을 잊는다.",
                             "기억은 급하게 만들 수 없다."],
            },
        ],
        "body": '''<p>시험 <span class="cn-word" data-tr="bir kun oldin">전날</span> <span class="cn-word" data-pos="verb" data-tr="tun boʻyi uxlamaydigan">밤을 새우는</span> 학생이 많다. 이것을 한국어로 “<span class="cn-word" data-tr="tez-tez yigʻib oʻqish, oxirgi kunda tayyorgarlik">벼락치기</span>”라고 한다. <span class="cn-word" data-tr="chaqmoq">벼락</span>은 하늘에서 갑자기 치는 <span class="cn-word" data-tr="yashin">번개</span>다. 아주 <span class="cn-word" data-pos="adv" data-tr="shosha-pisha">급하게</span> 한다는 뜻이다.</p>

<p>그런데 밤을 <span class="cn-word" data-pos="verb" data-tr="uxlamay oʻtkazganing bilan">새워 봤자</span> 다음 주에는 다 <span class="cn-word" data-pos="verb" data-tr="unutib yuboradi">잊어버린다</span>. <span class="cn-word" data-tr="tadqiqot">연구</span> 결과가 그것을 보여 준다.</p>

<p>십구 세기에 한 독일 <span class="cn-word" data-tr="olim">학자</span>가 “<span class="cn-word" data-tr="unutish egri chizigʻi">망각 곡선</span>”을 만들었다. 그는 사람의 <span class="cn-word" data-tr="xotira">기억</span>을 오래 조사했다. 결과는 <span class="cn-word" data-pos="adj" data-tr="hayratlanarli edi">놀라웠다</span>. 사람은 배우고 한 시간 후에 <span class="cn-word" data-tr="yarmini">절반</span>을 잊는다. 하루 후에는 <span class="cn-word" data-tr="uchdan ikki qismini">삼분의 이</span>를 잊는다. 그래서 하룻밤에 열 시간을 <span class="cn-word" data-pos="verb" data-tr="oʻqiganing bilan">공부해 봤자</span> 그 <span class="cn-word" data-tr="bilim">지식</span>은 며칠 안에 <span class="cn-word" data-pos="verb" data-tr="yoʻqoladi">사라진다</span>.</p>

<p>그러면 방법이 없다? 아니다. 있다. 이름은 “<span class="cn-word" data-tr="tarqoq oʻqish">분산 학습</span>”이다.</p>

<p>같은 열 시간을 오 일에 <span class="cn-word" data-pos="verb" data-tr="boʻlsang">나누면</span> 결과가 완전히 <span class="cn-word" data-pos="verb" data-tr="oʻzgaradi">달라진다</span>. 하루에 두 시간씩, 다섯 번. 조금 잊은 후에 다시 보는 것이 <span class="cn-word" data-pos="adj" data-tr="muhim">중요하다</span>.</p>

<p>한 연구에서 두 <span class="cn-word" data-tr="guruh">그룹</span>의 학생이 같은 단어를 <span class="cn-word" data-pos="verb" data-tr="yodladi">외웠다</span>. 첫 번째 그룹은 하루에 다 외웠다. 두 번째 그룹은 오 일에 나누어 외웠다. 시험 결과는 <span class="cn-word" data-pos="adj" data-tr="oʻxshash edi">비슷했다</span>. 그러나 한 달 후에 다시 시험을 봤다. 첫 번째 그룹은 이십 <span class="cn-word" data-tr="foiz">퍼센트</span>를 기억했다. 두 번째 그룹은 팔십 퍼센트를 기억했다.</p>

<p>물론 시험이 내일이면 다른 방법이 없다. 그때는 밤을 새우는 것도 방법이다. 하지만 다음 시험은 아직 <span class="cn-word" data-pos="adj" data-tr="uzoq">멀다</span>. 오늘 삼십 분을 공부하는 것이 내일 세 시간보다 <span class="cn-word" data-pos="adj" data-tr="yaxshiroq">낫다</span>.</p>

<p>한 선생님은 이렇게 말한다. “학생들은 시험 전날에 저를 <span class="cn-word" data-pos="verb" data-tr="izlab keladi">찾아와요</span>. 그때는 제가 도와줘 봤자 <span class="cn-word" data-pos="adj" data-tr="foydasi yoʻq">소용없어요</span>. 한 달 전에 오세요.”</p>

<p>기억은 급하게 만들 수 없다. 아무리 <span class="cn-word" data-pos="verb" data-tr="shoshganing bilan">서둘러 봤자</span> <span class="cn-word" data-tr="miya">뇌</span>는 자기 <span class="cn-word" data-tr="tezlik">속도</span>로 <span class="cn-word" data-pos="verb" data-tr="harakat qiladi">움직인다</span>.</p>''',
        "questions": [
            {
                "text": "Nemis olimining tadqiqotiga koʻra, odam bir "
                        "soatdan keyin oʻrganganining qanchasini unutadi?",
                "choices": [
                    "Oʻndan birini", "Yarmini",
                    "Uchdan ikki qismini", "Hammasini",
                ],
                "answer": 1,
                "explanation": "“사람은 배우고 한 시간 후에 <b>절반</b>을 "
                               "잊는다.” Bir kundan keyin esa uchdan ikki "
                               "qismini.",
            },
            {
                "text": "Ikki guruh tajribasining eng muhim natijasi nima "
                        "edi?",
                "choices": [
                    "Imtihonda ikkala guruh ham teng natija koʻrsatdi, "
                    "lekin bir oydan keyin farq 20% ga 80% boʻldi",
                    "Bir kunda yodlagan guruh doim yutdi",
                    "Ikkala guruh ham hech narsani eslay olmadi",
                    "Besh kunga boʻlgan guruh imtihonda yiqildi",
                ],
                "answer": 0,
                "explanation": "Imtihon kuni farq koʻrinmadi — farq "
                               "<b>bir oydan keyin</b> chiqdi. Matnning "
                               "asosiy dalili shu.",
            },
            {
                "text": "“제가 도와줘 봤자 소용없어요” — oʻqituvchi nima "
                        "demoqchi?",
                "choices": [
                    "U yordam bermoqchi emas",
                    "Imtihon oldidan yordam berishga urinsa ham, natija "
                    "oʻzgarmaydi",
                    "Talabalar undan yordam soʻramaydi",
                    "Yordam berish taqiqlangan",
                ],
                "answer": 1,
                "explanation": "아/어 봤자 — urinish mumkin, lekin "
                               "<b>natija oʻzgarmaydi</b>. Shuning uchun "
                               "u “한 달 전에 오세요” deydi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-81 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "스무 번째 편지",
        "summary": (
            "PK-81 matni. Hana romanini oʻn toʻqqiz marta rad etishdi. "
            "Yigirmanchi javob boshqacha edi — va oradan oʻn besh yil "
            "oʻtib, u endi rad javoblarini oʻzi yozadi."
        ),
        "order":   81,
        "grammar": [
            {
                "pattern":  "더라도 — nima boʻlsa ham",
                "meaning":  "Kuchli yon berish, farazga asoslangan. "
                            "Oldida zamon boʻlmaydi.",
                "examples": ["무슨 일이 있더라도 스무 번은 보낸다."],
            },
            {
                "pattern":  "(으)ㄹ지라도 — …sa-da (kitobiy)",
                "meaning":  "더라도 ning yozma va eng kuchli shakli. "
                            "Matnda u qahramonning oʻz qoidasini "
                            "aytishda ishlatiladi — shuning uchun "
                            "tantanali eshitiladi.",
                "examples": ["아무리 바쁠지라도 좋았던 부분을 한 문장 쓴다."],
            },
            {
                "pattern":  "(으)ㅁ에도 불구하고 — …ga qaramay (FAKT)",
                "meaning":  "Yuqoridagi ikkitasi farazga qaraydi, bu esa "
                            "allaqachon boʻlgan haqiqatga. 피곤하다 → "
                            "피곤함.",
                "examples": ["피곤함에도 불구하고 매일 두 시간을 지켰다."],
            },
        ],
        "body": '''<p>하나 씨는 스물세 살에 첫 <span class="cn-word" data-tr="roman">소설</span>을 썼다. 삼백 <span class="cn-word" data-tr="sahifa">페이지</span>였다. 그것을 <span class="cn-word" data-tr="nashriyot">출판사</span>에 보냈다. 두 달 후에 편지가 왔다. 짧았다. “죄송합니다.”</p>

<p>하나 씨는 두 번째 출판사에 보냈다. 또 <span class="cn-word" data-tr="rad javob">거절</span>이었다. 세 번째, 네 번째, 다섯 번째도 <span class="cn-word" data-pos="adj" data-tr="oʻsha-oʻsha edi">마찬가지였다</span>.</p>

<p>열 번째 거절 편지를 받은 날, 하나 씨는 종이를 한 <span class="cn-word" data-tr="varaq (sanoq soʻzi)">장</span> <span class="cn-word" data-pos="verb" data-tr="chiqardi">꺼냈다</span>. 그리고 이렇게 썼다. “무슨 일이 <span class="cn-word" data-pos="verb" data-tr="boʻlsa ham">있더라도</span> 스무 번은 보낸다.”</p>

<p>그 종이를 책상 앞에 <span class="cn-word" data-pos="verb" data-tr="yopishtirdi">붙였다</span>.</p>

<p>열한 번째, 열두 번째… 거절은 계속되었다. 어떤 편지는 한 <span class="cn-word" data-tr="qator">줄</span>이었다. 어떤 출판사는 <span class="cn-word" data-tr="javob xati">답장</span>도 하지 않았다. 친구들은 다른 일을 <span class="cn-word" data-pos="verb" data-tr="izla dedi">찾으라고 했다</span>.</p>

<p>하나 씨는 낮에는 카페에서 일했다. 밤에는 썼다. <span class="cn-word" data-pos="adj" data-tr="charchoqqa qaramay">피곤함에도 불구하고</span> 매일 두 시간을 <span class="cn-word" data-pos="verb" data-tr="saqladi, buzmadi">지켰다</span>.</p>

<p>열아홉 번째 거절이 왔다. 하나 씨는 그날 처음으로 울었다. 하지만 다음 날 스무 번째 <span class="cn-word" data-tr="konvert">봉투</span>를 만들었다.</p>

<p>삼 주 후에 답장이 왔다. 봉투가 <span class="cn-word" data-pos="adj" data-tr="qalin edi">두꺼웠다</span>. 하나 씨는 손이 <span class="cn-word" data-pos="verb" data-tr="titradi">떨렸다</span>.</p>

<p><span class="cn-word" data-tr="bosh muharrir">편집장</span>의 편지였다. “이 소설은 아직 <span class="cn-word" data-pos="verb" data-tr="nashr qilish">출판하기</span> 어려워요. 하지만 세 번째 <span class="cn-word" data-tr="bob">장</span>은 <span class="cn-word" data-pos="adj" data-tr="ajoyib edi">훌륭했어요</span>. 그리고 우리 회사에 <span class="cn-word" data-tr="muharrir">편집자</span> <span class="cn-word" data-tr="oʻrin, lavozim">자리</span>가 있어요. 관심이 있으면 <span class="cn-word" data-pos="verb" data-tr="bogʻlaning">연락 주세요</span>.”</p>

<p>하나 씨는 <span class="cn-word" data-tr="yozuvchi">소설가</span>가 되지 못했다. 편집자가 되었다.</p>

<p>지금 하나 씨는 십오 년째 그 일을 한다. 하루에 <span class="cn-word" data-tr="qoʻlyozma">원고</span>를 세 <span class="cn-word" data-tr="dona (asar uchun)">편</span>씩 읽는다. 대부분은 거절해야 한다.</p>

<p>그러나 하나 씨의 거절 편지에는 <span class="cn-word" data-tr="qoida">규칙</span>이 하나 있다. 아무리 <span class="cn-word" data-pos="adj" data-tr="band boʻlsa-da">바쁠지라도</span>, 그 원고에서 좋았던 <span class="cn-word" data-tr="qism">부분</span>을 한 <span class="cn-word" data-tr="jumla">문장</span> 쓴다.</p>

<p>“그 한 문장이 사람을 <span class="cn-word" data-pos="verb" data-tr="tiriltiradi">살려요</span>.” 하나 씨는 이렇게 말한다. “제 열아홉 번의 편지에는 그것이 없었어요. 스무 번째에는 있었어요.”</p>''',
        "questions": [
            {
                "text": "Hana oʻninchi rad javobidan keyin nima qildi?",
                "choices": [
                    "Yozishni tashladi",
                    "Bir varaqqa “nima boʻlsa ham yigirma marta "
                    "yuboraman” deb yozib, stol tepasiga yopishtirdi",
                    "Boshqa shaharga koʻchdi",
                    "Nashriyotga bordi",
                ],
                "answer": 1,
                "explanation": "“무슨 일이 <b>있더라도</b> 스무 번은 보낸다.” "
                               "더라도 — hali boʻlmagan qiyinchiliklarga "
                               "oldindan javob.",
            },
            {
                "text": "“피곤함에도 불구하고 매일 두 시간을 지켰다” — nega "
                        "bu yerda 더라도 emas, 에도 불구하고?",
                "choices": [
                    "Chunki charchoq faraz emas — u haqiqatan bor edi",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki ikkita ega bor",
                    "Chunki 피곤하다 sifat",
                ],
                "answer": 0,
                "explanation": "Bu darsning asosiy chegarasi: <b>더라도 = "
                               "faraz</b>, <b>(으)ㅁ에도 불구하고 = fakt</b>. "
                               "U kunduzi kafeda ishlardi — charchoq "
                               "haqiqiy edi.",
            },
            {
                "text": "Hananing rad javoblaridagi qoidasi nima?",
                "choices": [
                    "Har doim tez javob berish",
                    "Qanchalik band boʻlmasin, qoʻlyozmadagi yaxshi "
                    "joydan bitta jumla yozish",
                    "Hech qachon rad etmaslik",
                    "Faqat yosh yozuvchilarga javob berish",
                ],
                "answer": 1,
                "explanation": "“아무리 <b>바쁠지라도</b>… 좋았던 부분을 한 "
                               "문장 쓴다.” Uning oʻn toʻqqizta xatida "
                               "aynan shu jumla yoʻq edi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-82 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "가장 작은 것과 가장 큰 것",
        "summary": (
            "PK-82 matni. Virusdan galaktikagacha — olamning ikki "
            "chekkasi va odam ularning qayerida turibdi. Oʻlchov "
            "haqidagi tushuntiruvchi matn."
        ),
        "order":   82,
        "grammar": [
            {
                "pattern":  "(으)ㄹ 정도로 — …gudek darajada",
                "meaning":  "Darajani boshqa bir ish orqali oʻlchaydi. "
                            "Oʻlchov hamisha asosiy feʼldan OLDIN turadi.",
                "examples": ["눈으로 볼 수 없을 정도로 작은 것이 있다.",
                             "지구를 백만 개 넣을 수 있을 정도로 크다."],
            },
            {
                "pattern":  "(으)ㄹ 만큼 — …gancha, …gan qadar",
                "meaning":  "Miqdor va tenglik. Bu matnda u insonning "
                            "tasavvur chegarasini oʻlchov qilib "
                            "ishlatadi.",
                "examples": ["상상할 수 없을 만큼 큰 것도 있다.",
                             "아무리 똑똑한 사람도 상상할 수 없을 만큼 큰 수다."],
            },
            {
                "pattern":  "Nega 정보문 da oʻlchov qoliplari kerak",
                "meaning":  "Raqamning oʻzi hech narsa aytmaydi — "
                            "“삼십조” degan soʻz miyada rasm hosil "
                            "qilmaydi. 정도로 va 만큼 raqamni "
                            "tanish narsaga bogʻlab beradi.",
                "examples": ["삼십조는 숫자로 쓰기 어려울 정도로 큰 수다."],
            },
        ],
        "body": '''<p>세상에는 눈으로 볼 수 <span class="cn-word" data-pos="adj" data-tr="koʻra olmaydigan darajada">없을 정도로</span> 작은 것이 있다. 그리고 <span class="cn-word" data-pos="verb" data-tr="tasavvur qila olmaydigan darajada">상상할 수 없을 만큼</span> 큰 것도 있다.</p>

<p>먼저 작은 것이다. <span class="cn-word" data-tr="soch tolasi">머리카락</span> 하나의 <span class="cn-word" data-tr="qalinlik">두께</span>는 약 0.07 <span class="cn-word" data-tr="millimetr">밀리미터</span>다. 이것도 <span class="cn-word" data-pos="adj" data-tr="ingichka">얇다</span>. 그러나 <span class="cn-word" data-tr="hujayra">세포</span>는 머리카락보다 <span class="cn-word" data-pos="adv" data-tr="ancha">훨씬</span> 작다. 사람의 몸에는 세포가 삼십<span class="cn-word" data-tr="trillion">조</span> 개 있다. 삼십조는 숫자로 쓰기 <span class="cn-word" data-pos="adj" data-tr="qiyin boʻlgudek darajada">어려울 정도로</span> 큰 수다.</p>

<p><span class="cn-word" data-tr="virus">바이러스</span>는 세포보다 백 <span class="cn-word" data-tr="marta">배</span> 작다. 보통 <span class="cn-word" data-tr="mikroskop">현미경</span>으로는 <span class="cn-word" data-pos="verb" data-tr="koʻrinmaydigan darajada">보이지 않을 정도로</span> 작다. 그런데 이 작은 것이 세계를 <span class="cn-word" data-pos="verb" data-tr="toʻxtatib qoʻya oladi">멈출 수 있다</span>.</p>

<p>이제 큰 것이다. <span class="cn-word" data-tr="Yer">지구</span>는 크다. 비행기로 한 <span class="cn-word" data-tr="aylana">바퀴</span> 돌면 이틀이 걸린다. 그러나 <span class="cn-word" data-tr="Quyosh">태양</span>은 지구보다 백 배 크다. 지구를 백만 개 <span class="cn-word" data-pos="verb" data-tr="sigʻdira oladigan darajada">넣을 수 있을 정도로</span> 크다.</p>

<p>그리고 태양도 작다. 우리 <span class="cn-word" data-tr="galaktika">은하</span>에는 태양 같은 <span class="cn-word" data-tr="yulduz">별</span>이 이천<span class="cn-word" data-tr="milliard">억</span> 개 있다. 그리고 <span class="cn-word" data-tr="koinot">우주</span>에는 은하가 이천억 개 있다.</p>

<p>이 숫자를 이해할 수 있는 사람은 없다. 아무리 <span class="cn-word" data-pos="adj" data-tr="aqlli">똑똑한</span> 사람도 상상할 수 없을 만큼 큰 수다.</p>

<p><span class="cn-word" data-pos="adj" data-tr="qiziq">재미있는</span> 것이 하나 있다. 사람은 이 두 <span class="cn-word" data-tr="chekka">끝</span>의 <span class="cn-word" data-tr="oʻrta">가운데</span>에 있다. 사람은 세포보다 크고 별보다 작다. <span class="cn-word" data-pos="adv" data-tr="aniq">정확히</span> 가운데다.</p>

<p>그래서 한 <span class="cn-word" data-tr="olim">과학자</span>는 이렇게 말했다. “우리는 우주에서 아주 작아요. 하지만 우주를 생각할 수 있어요. 그것이 우리의 <span class="cn-word" data-tr="oʻlcham">크기</span>예요.”</p>

<p>작은 것을 <span class="cn-word" data-pos="verb" data-tr="bilgan sari">알수록</span> 큰 것이 보인다. 그리고 큰 것을 알수록 작은 것이 <span class="cn-word" data-pos="adj" data-tr="qadrli boʻlib boradi">소중해진다</span>.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, odam olamning qayerida turibdi?",
                "choices": [
                    "Eng kichik chekkada",
                    "Eng katta chekkada",
                    "Aynan oʻrtada — hujayradan katta, yulduzdan kichik",
                    "Olamdan tashqarida",
                ],
                "answer": 2,
                "explanation": "“사람은 세포보다 크고 별보다 작다. 정확히 "
                               "가운데다.” Matnning butun tuzilishi shu "
                               "xulosaga olib keladi.",
            },
            {
                "text": "“삼십조는 숫자로 쓰기 어려울 정도로 큰 수다” — bu "
                        "jumla nima qilyapti?",
                "choices": [
                    "Raqamni yozishni taqiqlayapti",
                    "Raqamning kattaligini tanish narsa orqali "
                    "oʻlchayapti — “yozib boʻlmaydigan darajada”",
                    "Raqam notoʻgʻri ekanini aytyapti",
                    "Matematik qoidani tushuntiryapti",
                ],
                "answer": 1,
                "explanation": "(으)ㄹ 정도로 ning vazifasi shu: raqamning "
                               "oʻzi miyada rasm hosil qilmaydi, oʻlchov "
                               "esa qiladi.",
            },
            {
                "text": "Olimning gapidagi asosiy fikr nima?",
                "choices": [
                    "Odam olamdagi eng muhim mavjudot",
                    "Odam kichkina, lekin olamni oʻylay oladi — uning "
                    "haqiqiy oʻlchami shu",
                    "Olamni oʻrganish befoyda",
                    "Yulduzlar odamdan aqlliroq",
                ],
                "answer": 1,
                "explanation": "“우리는 우주에서 아주 작아요. 하지만 우주를 "
                               "생각할 수 있어요. 그것이 우리의 크기예요.” "
                               "Oʻlcham fizik emas, fikriy.",
            },
        ],
    },
]
