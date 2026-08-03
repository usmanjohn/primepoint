# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-59 … PK-61 (놓다/두다, 다고/냐고, 라고/자고).

★ Birinchi batch — foydalanuvchining yangi qoidasi boʻyicha: DIALOG EMAS, HIKOYA.
  Uchtasi uch xil shaklda yozildi, toc dagi "STORIES, NOT DIALOGUES" blokiga koʻra:
    59 — uchinchi shaxs hikoyasi (tugʻilgan kun tayyorgarligi, kichik kulgili burilish)
    60 — zamonaviy maktab hikoyasi (guruh chatidagi mish-mish tarqaladi va yolgʻon chiqadi)
    61 — kundalik (일기) — butunlay boshqa shakl

Kumulyativ qoida: PK-61 gacha oʻrganilgan hamma narsa ochiq.
PK-59 matnida koʻchirma gap (60, 61) hali YOʻQ — toʻgʻridan-toʻgʻri
koʻchirma va 말했어요 ishlatilgan. PK-60 matnida 라고/자고 (61) yoʻq.
Qisqargan shakllar -대요/-냬요/-래요/-재요 (62), (으)ㄹ 뻔하다 (63),
(으)ㄹ 테니까 (64) — hech qaysisida yoʻq. (으)러 가다 va 했다체 ham
hali oʻrganilmagan — ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_59_61.py --author=prime
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
    {
        "title":   "열어 놓은 창문",
        "summary": (
            "PK-59 matni. Sherbek singlisining tugʻilgan kuniga hamma narsani "
            "tayyorlab qoʻyadi — bittasidan boshqasi. Kichik kulgili hikoya."
        ),
        "order":   59,
        "grammar": [
            {
                "pattern":  "동사 + 아/어 놓다",
                "meaning":  "Ishni qildim va natijasi turibdi — tayyorgarlik "
                            "yoki holatni saqlash. Oʻzbekcha “qili-b "
                            "qoʻymoq” ning “tayyor turibdi” tomoni.",
                "examples": ["케이크를 만들어 놓았어요.",
                             "풍선을 붙여 놓았어요.",
                             "창문을 열어 놓았어요."],
            },
            {
                "pattern":  "동사 + 아/어 두다",
                "meaning":  "놓다 bilan deyarli bir xil, lekin uzoqroq "
                            "muddat ohangi bor — “shunday turaversin”.",
                "examples": ["선물은 미리 사 두었어요."],
            },
            {
                "pattern":  "아/어 놓은 + 명사",
                "meaning":  "Bu qolipni aniqlovchiga (PK-44) aylantirsa "
                            "boʻladi: “ochib qoʻyilgan deraza”.",
                "examples": ["열어 놓은 창문으로 바람이 들어왔어요."],
            },
        ],
        "body": '''<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨는 아침부터 바빴어요. 오늘은 동생 <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨의 <span class="cn-word" data-tr="tugʻilgan kun">생일</span>이에요.</p>

<p>셰르벡 씨는 <span class="cn-word" data-tr="tort">케이크</span>를 <span class="cn-word" data-pos="verb" data-tr="tayyorlab qoʻydi">만들어 놓았어요</span>. <span class="cn-word" data-tr="stol">식탁</span> 위에 <span class="cn-word" data-tr="shar">풍선</span>도 <span class="cn-word" data-pos="verb" data-tr="yopishtirib qoʻydi">붙여 놓았어요</span>. <span class="cn-word" data-tr="sovgʻa">선물</span>은 <span class="cn-word" data-pos="adv" data-tr="oldindan">미리</span> <span class="cn-word" data-pos="verb" data-tr="sotib qoʻygan edi">사 두었어요</span>. 방이 더워서 창문도 <span class="cn-word" data-pos="verb" data-tr="ochib qoʻydi">열어 놓았어요</span>.</p>

<p>셰르벡 씨는 <span class="cn-word" data-pos="adv" data-tr="oʻzicha">혼자</span> 웃었어요. 이제 다 <span class="cn-word" data-pos="verb" data-tr="tayyor boʻldi">준비됐어요</span>. 셰르벡 씨는 딜노자 씨와 같이 오려고 학교에 갔어요.</p>

<p>그런데 그때 <span class="cn-word" data-tr="shamol">바람</span>이 <span class="cn-word" data-pos="adv" data-tr="kuchli">세게</span> 불었어요. 열어 놓은 창문으로 바람이 <span class="cn-word" data-pos="verb" data-tr="kirdi">들어왔어요</span>. 풍선이 <span class="cn-word" data-pos="verb" data-tr="uchib ketdi">날아갔어요</span>. 식탁 위의 <span class="cn-word" data-tr="qogʻoz">종이</span>도 <span class="cn-word" data-pos="verb" data-tr="tushib ketdi">떨어졌어요</span>.</p>

<p>한 시간 후에 두 사람이 집에 왔어요. 방은 <span class="cn-word" data-tr="ostin-ustun">엉망</span>이었어요. 케이크만 <span class="cn-word" data-pos="adv" data-tr="oʻz holida">그대로</span> 있었어요.</p>

<p>딜노자 씨가 웃었어요.</p>

<p><strong>딜노자:</strong> 오빠, 이게 뭐예요?</p>

<p>셰르벡 씨가 <span class="cn-word" data-pos="adv" data-tr="sekin ovozda">작은 소리로</span> 말했어요.</p>

<p><strong>셰르벡:</strong> 창문을 열어 놓고 나갔어요...</p>

<p>두 사람은 같이 방을 <span class="cn-word" data-pos="verb" data-tr="yigʻishtirdi">치웠어요</span>. 그리고 케이크를 먹었어요. 케이크는 정말 맛있었어요. 딜노자 씨가 말했어요.</p>

<p><strong>딜노자:</strong> 오빠, 제일 좋은 생일이에요!</p>''',
        "questions": [
            {
                "text": "Sherbek uydan chiqishdan oldin nima qilib qoʻygan edi?",
                "choices": [
                    "Faqat tortni tayyorlab qoʻygan edi",
                    "Tort, sharlar, sovgʻa — hammasini tayyorlab qoʻygan edi",
                    "Hech narsa qilmagan edi",
                    "Faqat sovgʻa sotib olgan edi",
                ],
                "answer": 1,
                "explanation": "케이크를 <b>만들어 놓았어요</b>, 풍선을 "
                               "<b>붙여 놓았어요</b>, 선물은 미리 "
                               "<b>사 두었어요</b> — uchalasi ham "
                               "tayyorgarlik maʼnosidagi 놓다/두다.",
            },
            {
                "text": "Xona nega ostin-ustun boʻlib qoldi?",
                "choices": [
                    "Dilnoza yigʻishtirmagani uchun",
                    "Tort tushib ketgani uchun",
                    "Ochib qoʻyilgan derazadan shamol kirgani uchun",
                    "Mehmonlar kelgani uchun",
                ],
                "answer": 2,
                "explanation": "“<b>열어 놓은 창문</b>으로 바람이 들어왔어요” "
                               "— aynan Sherbekning oʻzi ochib qoʻygan "
                               "deraza sabab boʻldi. Hikoyaning kulgili "
                               "burilishi shunda.",
            },
            {
                "text": "“선물은 미리 사 두었어요” gapida nega 사 버렸어요 "
                        "emas, 사 두었어요 deyilgan?",
                "choices": [
                    "Chunki sovgʻa yoʻqolib ketdi",
                    "Chunki sovgʻa olindi va keyin kerak boʻlishi uchun "
                    "turibdi",
                    "Chunki sovgʻa qimmat edi",
                    "Chunki bu majhul nisbat",
                ],
                "answer": 1,
                "explanation": "<b>버리다</b> — narsa tugadi/yoʻq boʻldi. "
                               "<b>놓다/두다</b> — natija saqlanib turibdi. "
                               "Sovgʻa tugʻilgan kungacha turishi kerak, "
                               "shuning uchun 사 두었어요.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "소문",
        "summary": (
            "PK-60 matni. Sinfda “ertaga imtihon yoʻq” degan mish-mish tarqaladi. "
            "Faqat bitta oʻquvchi borib tekshiradi — va gap boshqacha chiqadi."
        ),
        "order":   60,
        "grammar": [
            {
                "pattern":  "-다고 하다 / 들었다 — darak gapni yetkazish",
                "meaning":  "Boshqaning gapini oʻz gapingiz ichida aytish. "
                            "고 — oʻzbekchadagi “deb”. Feʼl: 간다고/먹는다고, "
                            "sifat: 없다고/바쁘다고, ot: 학생이라고.",
                "examples": ["내일 시험이 없다고 들었어요.",
                             "학교에 안 간다고 했어요.",
                             "시험이 그대로 있다고 했어요."],
            },
            {
                "pattern":  "-냐고 묻다 / 물어보다 — soʻroq gapni yetkazish",
                "meaning":  "Boshqaning savolini yetkazish. Bu yerda feʼl "
                            "va sifat farqi yoʻq — hammasi 냐고.",
                "examples": ["누가 그렇게 말했냐고 물어봤어요."],
            },
            {
                "pattern":  "Eslatma: majhul va orttirma qaytadi",
                "meaning":  "PK-56 va PK-57 matn ichida yashab yuribdi: "
                            "퍼지다 (tarqalmoq), 조용해지다 (jimib qolmoq), "
                            "알리다 (bildirmoq — 알다 ning orttirmasi).",
                "examples": ["소문은 빨리 퍼졌어요.",
                             "친구들은 조용해졌어요.",
                             "셰르벡 씨가 바로 알렸어요."],
            },
        ],
        "body": '''<p>지난 <span class="cn-word" data-tr="seshanba">화요일</span>이었어요. <span class="cn-word" data-tr="tushlik vaqti">점심시간</span>에 <span class="cn-word" data-tr="Bekzod">베크조드</span> 씨가 <span class="cn-word" data-pos="adv" data-tr="yugurib">뛰어서</span> 교실에 들어왔어요.</p>

<p><strong>베크조드:</strong> 내일 시험이 <span class="cn-word" data-pos="verb" data-tr="yoʻq deb eshitdim">없다고 들었어요</span>!</p>

<p><span class="cn-word" data-tr="sinf">반</span> 친구들이 모두 <span class="cn-word" data-pos="verb" data-tr="xursand boʻldi">기뻐했어요</span>. <span class="cn-word" data-tr="Afsona">아프소나</span> 씨가 <span class="cn-word" data-pos="verb" data-tr="kim aytdi deb soʻradi">누가 그렇게 말했냐고 물어봤어요</span>. 베크조드 씨는 <span class="cn-word" data-tr="uchinchi kurs">삼 학년</span> 학생한테서 들었다고 했어요.</p>

<p><span class="cn-word" data-tr="mish-mish">소문</span>은 아주 빨리 <span class="cn-word" data-pos="verb" data-tr="tarqaldi">퍼졌어요</span>. <span class="cn-word" data-tr="Jasur">자스루르</span> 씨는 <span class="cn-word" data-tr="toʻgarak">동아리</span> 친구들한테 내일 학교에 안 간다고 했어요. <span class="cn-word" data-tr="Dilnoza">딜노자</span> 씨는 <span class="cn-word" data-tr="guruh chati">단체 대화방</span>에 <span class="cn-word" data-tr="xabar">메시지</span>를 보냈어요. 한 시간 후에 <span class="cn-word" data-tr="butun maktab">학교 전체</span>가 그 소문을 알았어요.</p>

<p><span class="cn-word" data-tr="Sherbek">셰르벡</span> 씨만 <span class="cn-word" data-pos="adj" data-tr="jim edi">조용했어요</span>. 셰르벡 씨는 선생님한테 <span class="cn-word" data-pos="adv" data-tr="toʻgʻridan-toʻgʻri">직접</span> 물어보기로 했어요.</p>

<p><span class="cn-word" data-tr="darsdan keyin">방과 후</span>에 셰르벡 씨가 <span class="cn-word" data-tr="oʻqituvchilar xonasi">교무실</span>에 갔어요. 선생님은 아주 <span class="cn-word" data-pos="verb" data-tr="hayron boʻldi">놀랐어요</span>. 그리고 시험이 <span class="cn-word" data-pos="adv" data-tr="oʻz holida">그대로</span> 있다고 했어요. 소문은 <span class="cn-word" data-tr="haqiqat">사실</span>이 아니었어요.</p>

<p>셰르벡 씨는 단체 대화방에 <span class="cn-word" data-pos="adv" data-tr="darhol">바로</span> <span class="cn-word" data-pos="verb" data-tr="bildirdi">알렸어요</span>. 친구들은 <span class="cn-word" data-pos="verb" data-tr="jimib qoldi">조용해졌어요</span>. 그날 저녁, 모두가 아주 <span class="cn-word" data-pos="adv" data-tr="tirishib">열심히</span> 공부했어요.</p>

<p>다음 날 아프소나 씨가 셰르벡 씨한테 <span class="cn-word" data-pos="verb" data-tr="rahmat deb aytdi">고맙다고 했어요</span>.</p>''',
        "questions": [
            {
                "text": "Bekzod mish-mishni qayerdan eshitgan edi?",
                "choices": [
                    "Oʻqituvchidan",
                    "Uchinchi kurs oʻquvchisidan",
                    "Guruh chatidan",
                    "Afsonadan",
                ],
                "answer": 1,
                "explanation": "“베크조드 씨는 <b>삼 학년 학생한테서 들었다고 "
                               "했어요</b>” — 들었다고 하다, yaʼni oʻtgan "
                               "zamon darak gapi (았/었다고).",
            },
            {
                "text": "Sherbek boshqalardan nimasi bilan farq qildi?",
                "choices": [
                    "Uyga erta ketdi",
                    "Mish-mishni yanada tez tarqatdi",
                    "Borib oʻqituvchidan oʻzi soʻradi",
                    "Imtihonga tayyorlanmadi",
                ],
                "answer": 2,
                "explanation": "“선생님한테 <b>직접</b> 물어보기로 했어요” — "
                               "hamma ishongan paytda u tekshirdi. "
                               "기로 하다 (PK-54) — qaror qildi.",
            },
            {
                "text": "“누가 그렇게 말했냐고 물어봤어요” gapida nega "
                        "다고 emas, 냐고 ishlatilgan?",
                "choices": [
                    "Chunki bu oʻtgan zamon",
                    "Chunki Afsona savol bergan — soʻroq gap 냐고 oladi",
                    "Chunki gapda ot bor",
                    "Chunki bu buyruq gap",
                ],
                "answer": 1,
                "explanation": "<b>다고</b> — darak gap (“…dedi”). "
                               "<b>냐고</b> — soʻroq gap (“…mi deb "
                               "soʻradi”). Shuning uchun feʼli ham "
                               "물어봤어요.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "산에 가자고 했어요 — 일기",
        "summary": (
            "PK-61 matni. Kundalik shaklida: togʻga chiqish kuni — kim nima "
            "degani, kim nima taklif qilgani boshdan oxir koʻchirma gapda."
        ),
        "order":   61,
        "grammar": [
            {
                "pattern":  "-자고 하다 — taklifni yetkazish",
                "meaning":  "“Birga …aylik” degan gapni yetkazish. Hamma "
                            "feʼlga bir xil qoʻshiladi, 받침 ayrisi yoʻq.",
                "examples": ["등산을 가자고 했어요.",
                             "쉬자고 했어요.",
                             "사진을 찍자고 했어요."],
            },
            {
                "pattern":  "-(으)라고 하다 — buyruqni yetkazish",
                "meaning":  "“…qiling” degan gapni yetkazish. 받침 yoʻq → "
                            "라고, 받침 bor → 으라고.",
                "examples": ["일찍 자라고 했어요.",
                             "물을 가져가라고 했어요.",
                             "천천히 오라고 했어요."],
            },
            {
                "pattern":  "Toʻrtta gap turi bir matnda",
                "meaning":  "Bu kundalikda toʻrtalasi ham bor: darak "
                            "(좋았다고), soʻroq (어땠냐고), buyruq "
                            "(조심하라고), taklif (가자고).",
                "examples": ["어머니가 어땠냐고 물어봤어요.",
                             "저는 좋았다고 했어요."],
            },
        ],
        "body": '''<p><strong>10월 5일 일요일 · 날씨: <span class="cn-word" data-tr="ochiq">맑음</span></strong></p>

<p>지난주에 <span class="cn-word" data-tr="Jasur">자스루르</span> 씨가 주말에 <span class="cn-word" data-tr="togʻga chiqish">등산</span>을 <span class="cn-word" data-pos="verb" data-tr="chiqaylik deb taklif qildi">가자고 했어요</span>. 저는 <span class="cn-word" data-pos="adv" data-tr="avvaliga">처음에는</span> 가고 싶지 않았어요. 요즘 너무 <span class="cn-word" data-pos="adj" data-tr="charchagan">피곤했기</span> 때문이에요. 하지만 <span class="cn-word" data-tr="Afsona">아프소나</span> 씨도 같이 가자고 해서 <span class="cn-word" data-pos="adv" data-tr="oxiri">결국</span> 가기로 했어요.</p>

<p>어제 저녁에 어머니가 일찍 <span class="cn-word" data-pos="verb" data-tr="uxla deb aytdi">자라고 했어요</span>. 그리고 <span class="cn-word" data-tr="suv">물</span>을 <span class="cn-word" data-pos="adv" data-tr="albatta">꼭</span> <span class="cn-word" data-pos="verb" data-tr="olib bor deb aytdi">가져가라고 했어요</span>. 저는 가방에 물과 <span class="cn-word" data-tr="kimbap">김밥</span>을 <span class="cn-word" data-pos="verb" data-tr="solib qoʻydim">넣어 두었어요</span>.</p>

<p>오늘 아침 여섯 시에 <span class="cn-word" data-pos="verb" data-tr="joʻnadik">출발했어요</span>. 산은 정말 <span class="cn-word" data-pos="adj" data-tr="baland">높았어요</span>. <span class="cn-word" data-tr="oʻrtasida">중간</span>에 저는 <span class="cn-word" data-pos="verb" data-tr="dam olaylik dedim">쉬자고 했어요</span>. 하지만 자스루르 씨는 <span class="cn-word" data-pos="adv" data-tr="ozgina">조금만</span> 더 가자고 했어요. 아프소나 씨는 저에게 <span class="cn-word" data-pos="adv" data-tr="sekin">천천히</span> <span class="cn-word" data-pos="verb" data-tr="kel deb aytdi">오라고 했어요</span>.</p>

<p><span class="cn-word" data-tr="choʻqqi">정상</span>에서 <span class="cn-word" data-tr="manzara">경치</span>가 정말 <span class="cn-word" data-pos="adj" data-tr="chiroyli edi">아름다웠어요</span>. 우리는 김밥을 먹었어요. 김밥이 그렇게 맛있는 것을 <span class="cn-word" data-pos="adv" data-tr="birinchi marta">처음</span> 알았어요. 자스루르 씨가 사진을 <span class="cn-word" data-pos="verb" data-tr="olaylik dedi">찍자고 했어요</span>. 우리는 사진을 많이 찍었어요.</p>

<p><span class="cn-word" data-pos="verb" data-tr="tushayotganda">내려올</span> 때 아프소나 씨가 <span class="cn-word" data-pos="verb" data-tr="ehtiyot boʻl dedi">조심하라고 했어요</span>. 길이 <span class="cn-word" data-pos="adj" data-tr="sirpanchiq">미끄러웠어요</span>. 하지만 저는 <span class="cn-word" data-pos="verb" data-tr="yiqilmadim">넘어지지 않았어요</span>.</p>

<p>집에 와서 어머니가 <span class="cn-word" data-pos="verb" data-tr="qanday oʻtdi deb soʻradi">어땠냐고 물어봤어요</span>. 저는 <span class="cn-word" data-pos="adj" data-tr="qiyin boʻlsa ham">힘들었지만</span> 아주 좋았다고 했어요. 우리는 다음 달에 또 가기로 했어요.</p>''',
        "questions": [
            {
                "text": "Yozuvchi nega avvaliga togʻga chiqishni istamadi?",
                "choices": [
                    "Chunki yomgʻir yogʻardi",
                    "Chunki oxirgi paytda juda charchagan edi",
                    "Chunki Jasurni yoqtirmasdi",
                    "Chunki uy vazifasi koʻp edi",
                ],
                "answer": 1,
                "explanation": "“요즘 너무 <b>피곤했기 때문이에요</b>” — "
                               "기 때문에 (PK-49) bilan berilgan sabab.",
            },
            {
                "text": "Onasi nima qilishni aytdi?",
                "choices": [
                    "Erta uxlashni va suvni albatta olib borishni",
                    "Togʻga bormaslikni",
                    "Kimbap tayyorlashni",
                    "Rasm koʻp olishni",
                ],
                "answer": 0,
                "explanation": "“일찍 <b>자라고 했어요</b>… 물을 꼭 "
                               "<b>가져가라고 했어요</b>” — ikkalasi ham "
                               "buyruq koʻchirma gapi ((으)라고).",
            },
            {
                "text": "“쉬자고 했어요” va “조심하라고 했어요” — farqi nimada?",
                "choices": [
                    "Birinchisi buyruq, ikkinchisi taklif",
                    "Birinchisi taklif (“dam olaylik”), ikkinchisi buyruq "
                    "(“ehtiyot boʻl”)",
                    "Ikkalasi ham savol",
                    "Ikkalasi ham darak gap",
                ],
                "answer": 1,
                "explanation": "<b>자고</b> — “birga qilaylik” degan "
                               "taklif. <b>(으)라고</b> — bir odamga "
                               "qaratilgan buyruq. Kundalikda ikkalasi "
                               "yonma-yon turibdi.",
            },
        ],
    },
]
