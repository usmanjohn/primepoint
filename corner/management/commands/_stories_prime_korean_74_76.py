# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-74 … PK-76 (자마자/기가 무섭게, 길에/김에, 고 나서/채로).

⚠️ BU BATCHDAN BOSHLAB USLUB OʻZGARDI (foydalanuvchi qoidasi, 2026-08-04):
  * Hikoyachi tili — **문어체 / 한다체**: 있다 · 한다 · 했다 · 이다 · 갈 것이다.
    해요체 endi faqat QOʻSHTIRNOQ ICHIDA — odamlar baribir shunday gaplashadi.
  * Mavzu — **정보문** (tushuntiruvchi matn, TOPIK 읽기/쓰기 uslubida) yoki
    **인생 이야기** (hayot hikoyasi), navbatma-navbat.
  Sabab: PK-71 dan boshlab oʻrgatilayotgan grammatika (고자, 법이다, 십상이다,
  기가 무섭게) — yozma grammatika. 한다체 uni oʻz uyiga qaytaradi, va TOPIK II
  쓰기 51–54 ham aynan shu uslubni talab qiladi.
  한다체 ning oʻzi PK-74 tutorialining 5-boʻlimida oʻrgatiladi.

Shakl:
  74 — 정보문: "빨리빨리" madaniyati (dalil + tarix + ikki tomon)
  75 — 인생 이야기: yopilgan kitob doʻkoni va uni qayta ochgan ayol
  76 — 정보문: uyquga xalaqit beradigan besh odat (roʻyxatli tushuntirish)

Kumulyativ qoida: PK-76 gacha oʻrganilgan hamma narsa ochiq.
PK-74 matnida 길에/김에 (75) va 고 나서/채로 (76) YOʻQ.
PK-75 matnida 고 나서 / (으)ㄴ 채로 (76) yoʻq.
다가 (77), 았더라면 (78), 다가는 (79), 아/어 봤자 (80) — hech qaysisida yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, (으)ㄹ지, 는데, 네요, 군요, hurmat -시-,
겠, (으)ㄴ 적이 있다, (으)ㄹ 때 — hali oʻrganilmagan, ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_74_76.py --author=prime
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
    # PK-74 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "빨리빨리, 한국",
        "summary": (
            "PK-74 matni. Koreyaning “빨리빨리” madaniyati qayerdan "
            "kelgan va u nima beradi-yu nimani olib qoʻyadi. "
            "Birinchi matn — 한다체 (kitob tili) da."
        ),
        "order":   74,
        "grammar": [
            {
                "pattern":  "자마자 — …ishi bilanoq",
                "meaning":  "Ikki ish orasida vaqt yoʻq. Feʼl oʻzagiga "
                            "toʻgʻridan toʻgʻri qoʻshiladi, oldida zamon "
                            "boʻlmaydi.",
                "examples": ["지하철 문이 열리자마자 사람들이 내린다.",
                             "신호등이 바뀌자마자 경적 소리가 들린다."],
            },
            {
                "pattern":  "기가 무섭게 — …ishga ulgurmay",
                "meaning":  "자마자 ning kuchli, boʻrttirma va koʻproq "
                            "yozma shakli. Hayrat bildiradi: “bunchalik "
                            "tez boʻlishini kutmagandim”.",
                "examples": ["식당에서 주문하기가 무섭게 음식이 나온다.",
                             "서류를 신청하기가 무섭게 처리가 끝난다."],
            },
            {
                "pattern":  "한다체 — kitob tili",
                "meaning":  "Bu matn 해요체 da emas, 한다체 da yozilgan: "
                            "내린다 · 나온다 · 있다 · 아니다 · 시작되었다. "
                            "Gazeta, maqola va TOPIK II 쓰기 ning uslubi "
                            "shu. Qoʻshtirnoq ichidagi gap oʻz uslubini "
                            "saqlaydi.",
                "examples": ["한국의 인터넷 속도는 세계에서 가장 빠르다.",
                             "이 문화는 갑자기 생긴 것이 아니다."],
            },
        ],
        "body": '''<p>한국에 처음 온 <span class="cn-word" data-tr="chet ellik">외국인</span>이 가장 먼저 배우는 한국어는 “안녕하세요”가 아니다. “<span class="cn-word" data-pos="adv" data-tr="tez-tez, shosha-pisha">빨리빨리</span>”다.</p>

<p><span class="cn-word" data-tr="metro">지하철</span> 문이 <span class="cn-word" data-pos="verb" data-tr="ochilishi bilanoq">열리자마자</span> 사람들이 빠르게 내린다. <span class="cn-word" data-tr="svetofor">신호등</span>이 <span class="cn-word" data-tr="yashil rang">초록색</span>으로 <span class="cn-word" data-pos="verb" data-tr="oʻzgarishi bilanoq">바뀌자마자</span> 뒤에서 <span class="cn-word" data-tr="signal ovozi">경적 소리</span>가 들린다. 식당에서 <span class="cn-word" data-pos="verb" data-tr="buyurtma berishga ulgurmay">주문하기가 무섭게</span> <span class="cn-word" data-tr="garnir, gazak">반찬</span>과 국이 나온다. <span class="cn-word" data-tr="internet">인터넷</span>에서 물건을 사면 다음 날 아침에 <span class="cn-word" data-tr="pochta, yetkazma">택배</span>가 도착한다. 한국의 인터넷 <span class="cn-word" data-tr="tezlik">속도</span>는 세계에서 가장 빠르다.</p>

<p>이 <span class="cn-word" data-tr="madaniyat">문화</span>는 <span class="cn-word" data-pos="adv" data-tr="toʻsatdan">갑자기</span> 생긴 것이 아니다. 1950<span class="cn-word" data-tr="yillar">년대</span>에 <span class="cn-word" data-tr="urush">전쟁</span>이 끝난 후에 한국은 아주 <span class="cn-word" data-pos="adj" data-tr="kambagʻal">가난한</span> 나라였다. 다른 나라가 백 년 <span class="cn-word" data-tr="davomida">동안</span> 만든 것을 한국은 삼십 년 안에 만들어야 했다. 그래서 사람들은 <span class="cn-word" data-pos="verb" data-tr="dam olmasdan">쉬지 않고</span> 일했다. “빨리빨리”는 그때 만들어진 말이다.</p>

<p>빠른 것은 좋은 <span class="cn-word" data-tr="tomon, jihat">점</span>이 많다. <span class="cn-word" data-tr="hujjat">서류</span>를 <span class="cn-word" data-pos="verb" data-tr="topshirishga ulgurmay">신청하기가 무섭게</span> <span class="cn-word" data-tr="rasmiylashtirish">처리</span>가 끝난다. 병원에 가면 오래 <span class="cn-word" data-pos="verb" data-tr="kutmaydi">기다리지 않는다</span>. 외국인들은 이런 점을 아주 좋아한다.</p>

<p>하지만 나쁜 점도 있다. <span class="cn-word" data-pos="verb" data-tr="shoshsang">서두르면</span> 실수하기 십상이다. 빨리 <span class="cn-word" data-pos="verb" data-tr="qurilgan">지은</span> <span class="cn-word" data-tr="bino">건물</span>이 <span class="cn-word" data-pos="verb" data-tr="qulagan">무너진</span> 일도 있었다. 요즘 젊은 사람들은 “<span class="cn-word" data-pos="adv" data-tr="sekin">천천히</span> 사는 것”에 <span class="cn-word" data-tr="qiziqish">관심</span>이 많다. 카페에 앉아서 책을 읽는 사람도 <span class="cn-word" data-pos="verb" data-tr="ortib bormoqda">늘고 있다</span>.</p>

<p>한 젊은 <span class="cn-word" data-tr="ofis xodimi">회사원</span>은 이렇게 말한다. “저는 이제 지하철을 한 대 <span class="cn-word" data-pos="verb" data-tr="yuboraman">보내요</span>. 일 분 늦어도 아무 일도 안 생겨요.”</p>

<p>한국을 이해하고 싶은 사람은 이 두 가지를 함께 보아야 한다. 빨리 <span class="cn-word" data-pos="verb" data-tr="yuguradigan">달리는</span> 나라와, 이제 조금 천천히 걷고 싶은 나라를.</p>''',
        "questions": [
            {
                "text": "Matnga koʻra, “빨리빨리” madaniyati qachon "
                        "shakllangan?",
                "choices": [
                    "Internet paydo boʻlgandan keyin",
                    "Urushdan keyin, mamlakatni tez tiklash zarurati "
                    "tugʻilganda",
                    "Metro qurilgandan keyin",
                    "Yosh avlod yetishib chiqqanda",
                ],
                "answer": 1,
                "explanation": "“1950년대에 전쟁이 끝난 후에… 다른 나라가 백 년 "
                               "동안 만든 것을 한국은 삼십 년 안에 만들어야 "
                               "했다.” Boshqalar bir asrda qilganini oʻttiz "
                               "yilda qilish kerak edi.",
            },
            {
                "text": "“주문하기가 무섭게 음식이 나온다” gapi nimani "
                        "bildiradi?",
                "choices": [
                    "Ovqat buyurtma berishdan oldin keladi",
                    "Buyurtma berishga ulgurmay ovqat keladi — hayratlanarli "
                    "darajada tez",
                    "Ovqat kelishi uchun uzoq kutish kerak",
                    "Ovqat buyurtma qilinmasa ham keltiriladi",
                ],
                "answer": 1,
                "explanation": "기가 무섭게 — 자마자 ning boʻrttirma shakli. "
                               "U shunchaki ketma-ketlikni emas, "
                               "<b>kutilmagan tezlikni</b> bildiradi.",
            },
            {
                "text": "Matnning oxirgi xulosasi nima?",
                "choices": [
                    "Koreya endi tezlikdan butunlay voz kechgan",
                    "Tezlik faqat zarar keltiradi",
                    "Koreyani tushunish uchun ikki tomonni — tez yuguradigan "
                    "va endi sekinlashmoqchi boʻlgan tomonni birga koʻrish kerak",
                    "Chet elliklar Koreyani hech qachon tushunmaydi",
                ],
                "answer": 2,
                "explanation": "“빨리 달리는 나라와, 이제 조금 천천히 걷고 싶은 "
                               "나라를” — muallif ikkalasini ham koʻrishni "
                               "taklif qiladi. Bu 정보문 ning odatiy "
                               "muvozanatli xulosasi.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-75 — 인생 이야기
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "문 닫은 서점",
        "summary": (
            "PK-75 matni. Oʻn yil bir kompaniyada ishlagan Jiyon har kuni "
            "yoʻlida bir kitob doʻkonini koʻrardi. Bir kuni eshikda "
            "eʼlon paydo boʻldi. Hayot hikoyasi, 한다체 da."
        ),
        "order":   75,
        "grammar": [
            {
                "pattern":  "는 길에 — …ga ketayotib",
                "meaning":  "길 = “yoʻl”. Faqat 가다/오다 guruhidagi harakat "
                            "feʼllari bilan. Oldida hamisha 는 turadi, "
                            "zamon esa gapning oxirida.",
                "examples": ["퇴근하는 길에 서점 앞에 종이가 붙어 있었다.",
                             "지나가는 길에 처음으로 문을 열었다."],
            },
            {
                "pattern":  "(으)ㄴ/는 김에 — bir yoʻla, shu bahonada",
                "meaning":  "Har qanday feʼl bilan. Ish davom etayotgan "
                            "boʻlsa 는 김에, allaqachon tugagan boʻlsa "
                            "(으)ㄴ 김에.",
                "examples": ["온 김에 책을 세 권 샀다.",
                             "청소하는 김에 창문도 닦는다."],
            },
            {
                "pattern":  "길에 va 김에 — bir jumlada",
                "meaning":  "길에 — tasodif: yoʻlda edim, shunday boʻldi. "
                            "김에 — qoʻshimcha qaror: baribir shu yerdaman, "
                            "unda buni ham qilay. Shu matnda ikkalasi "
                            "yonma-yon turadi.",
                "examples": ["지나가는 길에 문을 열었다. 그리고 온 김에 책을 샀다."],
            },
        ],
        "body": '''<p>지영 씨는 십 년 동안 같은 회사에 <span class="cn-word" data-pos="verb" data-tr="qatnadi">다녔다</span>. 매일 아침 지하철을 타고 <span class="cn-word" data-pos="verb" data-tr="ishga bordi">출근하고</span>, 밤늦게 <span class="cn-word" data-pos="verb" data-tr="ishdan qaytdi">퇴근했다</span>. 회사에서 집까지 걸어가는 길에 작은 <span class="cn-word" data-tr="kitob doʻkoni">서점</span>이 하나 있었다. 이름은 “책과 나무”였다.</p>

<p>지영 씨는 그 서점에 자주 들어가지 않았다. 하지만 불이 <span class="cn-word" data-pos="verb" data-tr="yoqilgan">켜진</span> 창문을 보는 것을 좋아했다. <span class="cn-word" data-pos="adj" data-tr="charchagan">피곤한</span> 날에도 그 노란 <span class="cn-word" data-tr="yorugʻlik">불빛</span>을 보면 마음이 조금 <span class="cn-word" data-pos="verb" data-tr="tinchlanardi">편해졌다</span>.</p>

<p>어느 날 <span class="cn-word" data-pos="verb" data-tr="ishdan qaytayotib">퇴근하는 길에</span> 서점 앞에 종이가 <span class="cn-word" data-pos="verb" data-tr="yopishtirilgan edi">붙어 있었다</span>. “이달 <span class="cn-word" data-tr="oxiri">말</span>에 문을 닫습니다. 그동안 감사했습니다.”</p>

<p>지영 씨는 그 자리에 오래 서 있었다. 그리고 <span class="cn-word" data-pos="verb" data-tr="oʻtib ketayotib">지나가는 길에</span> 처음으로 문을 열고 들어갔다. <span class="cn-word" data-pos="verb" data-tr="kelgan ekan">온 김에</span> 책을 세 <span class="cn-word" data-tr="dona (kitob uchun)">권</span> 샀다.</p>

<p><span class="cn-word" data-tr="egasi">주인</span> 할아버지는 웃으면서 말했다. “삼십 년 했어요. 이제 이 책들을 <span class="cn-word" data-pos="verb" data-tr="meros qilib oladigan">물려받을</span> 사람이 없어요.”</p>

<p>그날 밤 지영 씨는 잠을 자지 못했다. 그 후 일 년 동안 매일 그 생각을 했다. 회사 일은 <span class="cn-word" data-pos="adj" data-tr="barqaror">안정적</span>이었다. <span class="cn-word" data-tr="oylik">월급</span>도 나쁘지 않았다. 하지만 아침에 <span class="cn-word" data-pos="verb" data-tr="turishi bilanoq">일어나자마자</span> 회사에 가기 싫은 마음이 들었다.</p>

<p>다음 해 봄에 지영 씨는 회사를 <span class="cn-word" data-pos="verb" data-tr="tashladi">그만두었다</span>. 그리고 “책과 나무”의 문을 다시 열었다.</p>

<p>지금 지영 씨는 아침 일찍 서점에 나온다. <span class="cn-word" data-pos="verb" data-tr="tozalayotgan ekan">청소하는 김에</span> 창문도 <span class="cn-word" data-pos="verb" data-tr="artadi">닦는다</span>. <span class="cn-word" data-tr="mijoz">손님</span>이 없는 날도 많다. 돈은 <span class="cn-word" data-tr="ilgarigidan">예전보다</span> 적게 <span class="cn-word" data-pos="verb" data-tr="topadi">번다</span>.</p>

<p>하지만 지영 씨는 이렇게 말한다. “저는 매일 <span class="cn-word" data-pos="verb" data-tr="ishga ketayotib">출근하는 길에</span> 이 문을 봐요. 그리고 웃어요. 십 년 동안 한 번도 이런 마음이 없었어요.”</p>

<p>인생을 바꾸는 것은 큰 <span class="cn-word" data-tr="qaror">결심</span>이 아니다. 어느 날 지나가는 길에 열어 본 문 하나일지도 모른다.</p>''',
        "questions": [
            {
                "text": "Jiyon kitob doʻkoniga birinchi marta nega kirdi?",
                "choices": [
                    "Kitob sotib olish uchun maxsus bordi",
                    "Ishdan qaytayotib eshikda yopilish haqidagi eʼlonni "
                    "koʻrdi",
                    "Doʻsti uni chaqirdi",
                    "Egasi uni taklif qildi",
                ],
                "answer": 1,
                "explanation": "“퇴근하는 길에 서점 앞에 종이가 붙어 있었다” — "
                               "eʼlon uni toʻxtatdi. Kitob esa "
                               "<b>온 김에</b> — kirgan ekan, bir yoʻla "
                               "olingan qoʻshimcha ish.",
            },
            {
                "text": "“온 김에 책을 세 권 샀다” — nega bu yerda 김에, "
                        "길에 emas?",
                "choices": [
                    "Kitob sotib olish yoʻlning ustidagi tasodif emas, "
                    "kirgandan keyin qilingan qoʻshimcha qaror",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 사다 harakat feʼli emas",
                    "Chunki doʻkon yopilgan edi",
                ],
                "answer": 0,
                "explanation": "길에 — <b>tasodif</b>, yoʻl ustida sodir "
                               "boʻlgan narsa. 김에 — <b>qoʻshimcha qaror</b>: "
                               "baribir kirdim, unda kitob ham olay. "
                               "Kelish tugagani uchun 온 (oʻtgan aniqlovchi).",
            },
            {
                "text": "Hikoyaning oxirgi jumlasi nimani aytmoqchi?",
                "choices": [
                    "Katta qarorlar hech qachon ishlamaydi",
                    "Kitob doʻkoni ochish har kimga foydali",
                    "Hayotni oʻzgartiradigan narsa katta qaror emas, balki "
                    "yoʻl-yoʻlakay ochilgan bitta eshik boʻlishi mumkin",
                    "Odam ishini hech qachon tashlamasligi kerak",
                ],
                "answer": 2,
                "explanation": "“어느 날 지나가는 길에 열어 본 문 하나<b>일지도 "
                               "모른다</b>” — PK-73 dagi ehtimol qolipi bilan "
                               "yumshoq, oʻylantiradigan xulosa.",
            },
        ],
    },

    # ══════════════════════════════════════════════════════════════════
    # PK-76 — 정보문
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "잠을 방해하는 다섯 가지 습관",
        "summary": (
            "PK-76 matni. Nima uchun yaxshi uxlay olmaymiz — beshta odat "
            "va ularning ilmiy sababi. Roʻyxatli tushuntiruvchi matn, "
            "한다체 da."
        ),
        "order":   76,
        "grammar": [
            {
                "pattern":  "고 나서 — …ib boʻlgach",
                "meaning":  "나다 = “tugamoq”. Birinchi ish butunlay "
                            "tugaganini urgʻulaydi. Ikkala gapning egasi "
                            "bir xil boʻlishi shart.",
                "examples": ["저녁을 먹고 나서 바로 눕는 것이다.",
                             "불을 끄고 나서 휴대폰을 멀리 두는 것이 좋다."],
            },
            {
                "pattern":  "(으)ㄴ 채로 — …gan holicha",
                "meaning":  "채 = “holat”. Ish tugagan, lekin natijasi "
                            "saqlanib turibdi. Oldida hamisha oʻtgan "
                            "aniqlovchi (으)ㄴ. Koʻpincha gʻalati yoki "
                            "notoʻgʻri holat haqida.",
                "examples": ["불을 켠 채로 자는 것이다.",
                             "휴대폰을 손에 쥔 채로 눕는 것이다."],
            },
            {
                "pattern":  "채로 va 면서 farqi",
                "meaning":  "면서 — ikki harakat davom etadi (음악을 들으면서 "
                            "공부한다). 채로 — bir holat saqlanadi, ustida "
                            "bitta harakat boʻladi (불을 켠 채로 잔다).",
                "examples": ["텔레비전을 켜 놓은 채로 잠드는 것이다."],
            },
        ],
        "body": '''<p>사람은 <span class="cn-word" data-tr="hayot">인생</span>의 삼분의 일을 잠으로 보낸다. 그런데 한국 <span class="cn-word" data-tr="katta yoshli, kattalar">성인</span>의 <span class="cn-word" data-tr="oʻrtacha">평균</span> <span class="cn-word" data-tr="uyqu vaqti">수면 시간</span>은 하루 여섯 시간 반 정도다. 이것은 세계에서 아주 짧은 시간이다. 잠이 <span class="cn-word" data-pos="adj" data-tr="yetishmasa">부족하면</span> <span class="cn-word" data-tr="xotira">기억력</span>이 떨어지고 <span class="cn-word" data-pos="verb" data-tr="semirib ketish">살이 찌기</span> 십상이다.</p>

<p><span class="cn-word" data-tr="mutaxassislar">전문가</span>들은 다섯 가지 <span class="cn-word" data-tr="odat">습관</span>을 고쳐야 한다고 말한다.</p>

<p><span class="cn-word" data-tr="birinchidan">첫째</span>, 불을 <span class="cn-word" data-pos="verb" data-tr="yoqqan holicha">켠 채로</span> 자는 것이다. <span class="cn-word" data-pos="adj" data-tr="yorqin">밝은</span> 빛은 잠을 자게 하는 <span class="cn-word" data-tr="gormon">호르몬</span>을 <span class="cn-word" data-pos="verb" data-tr="kamaytiradi">줄인다</span>. 자기 전에 불을 <span class="cn-word" data-pos="verb" data-tr="oʻchirish">끄는</span> 것이 좋다.</p>

<p><span class="cn-word" data-tr="ikkinchidan">둘째</span>, 휴대폰을 손에 <span class="cn-word" data-pos="verb" data-tr="ushlagan holicha">쥔 채로</span> <span class="cn-word" data-pos="verb" data-tr="yotish">눕는</span> 것이다. <span class="cn-word" data-tr="ekran">화면</span>의 빛은 눈을 <span class="cn-word" data-pos="verb" data-tr="uygʻotadi">깨운다</span>. 침대에 누워서 <span class="cn-word" data-tr="video">영상</span>을 보기 시작하면 한 시간이 <span class="cn-word" data-pos="verb" data-tr="oʻtishga ulgurmay">지나기가 무섭게</span> <span class="cn-word" data-tr="tong, saharmardon">새벽</span>이 된다.</p>

<p><span class="cn-word" data-tr="uchinchidan">셋째</span>, 저녁을 <span class="cn-word" data-pos="verb" data-tr="yeb boʻlgach">먹고 나서</span> 바로 눕는 것이다. 음식이 <span class="cn-word" data-pos="verb" data-tr="hazm boʻlmasidan">소화되기 전에</span> 누우면 <span class="cn-word" data-tr="ichak-oshqozon">속</span>이 <span class="cn-word" data-pos="adj" data-tr="noqulay boʻladi">불편해진다</span>. 식사를 하고 나서 <span class="cn-word" data-pos="adv" data-tr="kamida">적어도</span> 세 시간이 지난 후에 자야 한다.</p>

<p><span class="cn-word" data-tr="toʻrtinchidan">넷째</span>, 오후 늦게 커피를 마시는 것이다. <span class="cn-word" data-tr="kofein">카페인</span>은 몸에서 여섯 시간 <span class="cn-word" data-tr="dan ortiq">이상</span> <span class="cn-word" data-pos="verb" data-tr="qoladi">남아 있다</span>. 오후 두 시 <span class="cn-word" data-tr="dan keyin">이후</span>에는 마시지 않는 것이 좋다.</p>

<p><span class="cn-word" data-tr="beshinchidan">다섯째</span>, 텔레비전을 <span class="cn-word" data-pos="verb" data-tr="yoqib qoʻygan holicha">켜 놓은 채로</span> <span class="cn-word" data-pos="verb" data-tr="uyquga ketish">잠드는</span> 것이다. 소리가 들리면 <span class="cn-word" data-pos="adj" data-tr="chuqur">깊은</span> 잠에 들어가지 못한다. 아침에 일어나도 <span class="cn-word" data-pos="adv" data-tr="hamon">여전히</span> 피곤하다.</p>

<p>한 <span class="cn-word" data-tr="shifokor">의사</span>는 이렇게 말한다. “잠은 <span class="cn-word" data-tr="dam olish">휴식</span>이 아니에요. 몸이 <span class="cn-word" data-pos="verb" data-tr="oʻzini taʼmirlaydigan">자기를 고치는</span> 시간이에요.”</p>

<p>이 다섯 가지를 <span class="cn-word" data-pos="adv" data-tr="bir kunda">하루아침에</span> 다 고치는 것은 어렵다. 하지만 하나씩 바꾸면 몸이 먼저 안다. 오늘 밤에는 불을 끄고 나서 휴대폰을 <span class="cn-word" data-pos="adv" data-tr="uzoqroqqa">멀리</span> 두는 것부터 <span class="cn-word" data-pos="verb" data-tr="boshlash">시작하는</span> 것이 좋다.</p>

<p>좋은 잠은 좋은 하루를 만든다. 그리고 좋은 하루가 <span class="cn-word" data-pos="verb" data-tr="toʻplansa">쌓이면</span> 좋은 인생이 되는 법이다.</p>''',
        "questions": [
            {
                "text": "Chiroqni yoqib uxlash nega zararli?",
                "choices": [
                    "Elektr koʻp sarflanadi",
                    "Yorqin yorugʻlik uyqu gormonini kamaytiradi",
                    "Koʻz ogʻriydi",
                    "Xona issiq boʻlib qoladi",
                ],
                "answer": 1,
                "explanation": "“밝은 빛은 잠을 자게 하는 호르몬을 줄인다.” "
                               "Matn har bir odat uchun <b>sababini</b> "
                               "beradi — 정보문 ning asosiy belgisi.",
            },
            {
                "text": "Nega bu yerda “불을 켠 채로” deyilgan, "
                        "“불을 켜면서” emas?",
                "choices": [
                    "Chiroq yoqish tugagan ish — faqat uning holati saqlanib "
                    "turibdi, u davom etayotgan harakat emas",
                    "Chunki gap oʻtgan zamonda",
                    "Chunki 켜다 sifat",
                    "Chunki ikkita ega bor",
                ],
                "answer": 0,
                "explanation": "(으)면서 ikkita <b>davom etayotgan harakat</b> "
                               "uchun. Chiroqni yoqib boʻlgansiz — endi "
                               "faqat “yoniq” <b>holat</b> qoladi, "
                               "shuning uchun <b>(으)ㄴ 채로</b>.",
            },
            {
                "text": "Kechki ovqatdan keyin qancha kutish tavsiya "
                        "qilinadi?",
                "choices": [
                    "Bir soat", "Kamida uch soat",
                    "Olti soat", "Kutish shart emas",
                ],
                "answer": 1,
                "explanation": "“식사를 하고 나서 적어도 세 시간이 지난 후에 "
                               "자야 한다.” <b>고 나서</b> — ovqat butunlay "
                               "tugaganini urgʻulaydi.",
            },
        ],
    },
]
