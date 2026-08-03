# -*- coding: utf-8 -*-
"""Prime Korean Readings — PK-71 … PK-73 (겸/고자, 마련이다/법이다, 을지도/십상).

Bu batchdan boshlab USLUB ham oʻrgatiladi: 71-matn butunlay 습니다체 da
yozilgan rasmiy hujjat, 72-matn maqol tilida, 73-matn esa amaliy
maslahat uslubida. Uchtasi uch xil registr — TOPIK II ga tayyorgarlik.

Shakl xilma-xilligi (toc dagi "STORIES, NOT DIALOGUES" qoidasi):
  71 — ARIZA / oʻzini tanishtirish xati (자기소개서). 고자 ning tabiiy uyi.
  72 — DONOLIK HIKOYASI: buvining uch gapi va ular qachon tushunilgani.
  73 — AMALIY MASLAHAT ROʻYXATI (여행 팁) — ogohlantirish tili.

Kumulyativ qoida: PK-73 gacha oʻrganilgan hamma narsa ochiq.
PK-71 matnida 마련이다/법이다 (72) va 을지도/십상 (73) YOʻQ.
PK-72 matnida 을지도 모르다 / 기 십상이다 (73) yoʻq.
자마자 (74), 는 길에/김에 (75), 고 나서/(으)ㄴ 채로 (76), 다가 (77) — yoʻq.
(으)러, (으)ㄹ게요, (으)ㄹ까요, 는데, 네요, hurmat -시- ham hali
oʻrganilmagan — ishlatilmadi.

    python manage.py import_corner \
        corner/management/commands/_stories_prime_korean_71_73.py --author=prime
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
        "title":   "한국 교환학생 지원서",
        "summary": (
            "PK-71 matni. Rasmiy ariza shaklida: Sherbek almashuv dasturiga "
            "yozadi. Butun matn 습니다체 da — birinchi rasmiy hujjat."
        ),
        "order":   71,
        "grammar": [
            {
                "pattern":  "동사 + 고자 — rasmiy maqsad",
                "meaning":  "“…maqsadida”. Yozma va rasmiy uslub, 습니다체 "
                            "bilan yuradi. Zamon qoʻshimchasi qoʻyilmaydi "
                            "va keyin buyruq kelmaydi.",
                "examples": ["한국어를 더 잘하고자 지원했습니다.",
                             "한국 문화를 직접 보고자 합니다.",
                             "통역사가 되고자 합니다."],
            },
            {
                "pattern":  "동사 + (으)ㄹ 겸 — ikki maqsad",
                "meaning":  "Bitta ish, ikkita maqsad — oʻzbekchadagi "
                            "“bir yoʻla”. Rasmiy matnda ham uchraydi.",
                "examples": ["공부도 할 겸 여행도 할 겸 여러 도시를 보고 "
                             "싶습니다."],
            },
            {
                "pattern":  "습니다체 — rasmiy uslub",
                "meaning":  "PK-19 dagi rasmiy shakl. Ariza, hujjat va "
                            "TOPIK yozma ishida shu uslub ishlatiladi — "
                            "해요체 emas.",
                "examples": ["저는 셰르벡입니다.",
                             "삼 년 동안 한국어를 공부했습니다."],
            },
        ],
        "body": '''<p><strong>교환학생 <span class="cn-word" data-tr="ariza">지원서</span> · <span class="cn-word" data-tr="oʻzini tanishtirish">자기소개</span></strong></p>

<p>안녕하세요. 저는 <span class="cn-word" data-tr="Toshkent">타슈켄트</span>에서 온 셰르벡입니다. 올해 <span class="cn-word" data-tr="oʻn sakkiz yosh">열여덟 살</span>입니다. 삼 년 전부터 한국어를 공부하고 있습니다. 제가 이 <span class="cn-word" data-tr="dastur">프로그램</span>에 <span class="cn-word" data-pos="verb" data-tr="ariza berdim">지원했습니다</span>. <span class="cn-word" data-tr="sabab">이유</span>는 세 가지입니다.</p>

<p><span class="cn-word" data-tr="birinchidan">첫째</span>, 저는 한국어를 더 <span class="cn-word" data-pos="verb" data-tr="yaxshi bilish maqsadida">잘하고자</span> 지원했습니다. 우즈베키스탄에서도 공부할 수 있습니다. 하지만 한국에서는 매일 한국어를 <span class="cn-word" data-pos="verb" data-tr="ishlataman">씁니다</span>. 그래서 <span class="cn-word" data-tr="malaka">실력</span>이 빨리 <span class="cn-word" data-pos="verb" data-tr="oshadi">늘 것입니다</span>.</p>

<p><span class="cn-word" data-tr="ikkinchidan">둘째</span>, 저는 한국 <span class="cn-word" data-tr="madaniyat">문화</span>를 <span class="cn-word" data-pos="adv" data-tr="oʻz koʻzim bilan">직접</span> <span class="cn-word" data-pos="verb" data-tr="koʻrish maqsadidaman">보고자 합니다</span>. 책으로 배운 것과 <span class="cn-word" data-tr="haqiqiy hayot">실제</span>는 <span class="cn-word" data-pos="adj" data-tr="boshqacha">다릅니다</span>.</p>

<p><span class="cn-word" data-tr="uchinchidan">셋째</span>, 저는 <span class="cn-word" data-pos="adv" data-tr="keyinchalik">나중에</span> <span class="cn-word" data-tr="tarjimon">통역사</span>가 <span class="cn-word" data-pos="verb" data-tr="boʻlish niyatidaman">되고자 합니다</span>. 통역사는 <span class="cn-word" data-tr="til">언어</span>뿐만 아니라 문화도 알아야 합니다.</p>

<p>한국에 가면 <span class="cn-word" data-pos="verb" data-tr="oʻqiy ham olay">공부도 할 겸</span> <span class="cn-word" data-pos="verb" data-tr="sayohat ham qilay">여행도 할 겸</span> <span class="cn-word" data-tr="bir necha shahar">여러 도시</span>를 보고 싶습니다. <span class="cn-word" data-pos="adv" data-tr="ayniqsa">특히</span> <span class="cn-word" data-tr="Pusan">부산</span>과 <span class="cn-word" data-tr="Kyongju">경주</span>에 가고 싶습니다.</p>

<p>저는 <span class="cn-word" data-pos="adj" data-tr="mehnatkash">성실합니다</span>. 삼 년 동안 하루도 <span class="cn-word" data-pos="verb" data-tr="qoldirmasdan">빠지지 않고</span> 한국어를 공부했습니다. 이 <span class="cn-word" data-tr="imkoniyat">기회</span>가 있으면 아주 열심히 공부할 것입니다.</p>

<p><span class="cn-word" data-tr="rahmat">감사합니다</span>.</p>

<p><strong>셰르벡 <span class="cn-word" data-tr="hurmat bilan">드림</span></strong></p>''',
        "questions": [
            {
                "text": "Sherbek nima uchun ariza berdi?",
                "choices": [
                    "Faqat sayohat qilish uchun",
                    "Koreys tilini yaxshilash, madaniyatni koʻrish va "
                    "tarjimon boʻlish uchun",
                    "Oilasi soʻragani uchun",
                    "Uzbekistonda oʻqish imkoni yoʻqligi uchun",
                ],
                "answer": 1,
                "explanation": "Uchta sabab uchta <b>고자</b> bilan "
                               "berilgan: 잘하고자 · 보고자 합니다 · "
                               "되고자 합니다.",
            },
            {
                "text": "Nega bu matn butunlay 습니다체 da yozilgan?",
                "choices": [
                    "Chunki Sherbek yosh",
                    "Chunki bu rasmiy hujjat — ariza va hujjatda 해요체 "
                    "emas, 습니다체 ishlatiladi",
                    "Chunki matn uzun",
                    "Chunki 고자 faqat savolda keladi",
                ],
                "answer": 1,
                "explanation": "<b>고자</b> ham rasmiy qolip — u rasmiy "
                               "uslub bilan yuradi. TOPIK yozma ishida ham "
                               "shu juftlik kerak.",
            },
            {
                "text": "“공부도 할 겸 여행도 할 겸” nima degani?",
                "choices": [
                    "Faqat oʻqish uchun boradi",
                    "Oʻqishni tashlab sayohat qiladi",
                    "Bir yoʻla oʻqish ham, sayohat ham qilmoqchi",
                    "Oʻqishdan keyin sayohat qiladi",
                ],
                "answer": 2,
                "explanation": "<b>(으)ㄹ 겸</b> ikki maqsadni bitta safarga "
                               "sigʻdiradi — oʻzbekchadagi “bir yoʻla”. "
                               "Shuning uchun oxirgi feʼl bitta: "
                               "보고 싶습니다.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "할머니의 세 가지 말",
        "summary": (
            "PK-72 matni. Buvining uch gapi — va nabirasi ularning "
            "maʼnosini qachon tushungani. Maqol tilida yozilgan hikoya."
        ),
        "order":   72,
        "grammar": [
            {
                "pattern":  "기 마련이다 — tabiiy natija",
                "meaning":  "“…ishi tabiiy”. Yumshoq kuzatuv, koʻpincha "
                            "tasalli berish uchun. 마련 dan oldin 기 keladi.",
                "examples": ["사람은 누구나 실수하기 마련이다.",
                             "시간이 지나면 잊기 마련이다."],
            },
            {
                "pattern":  "(으)ㄴ/는 법이다 — hayotning qonuni",
                "meaning":  "법 = “qonun”. Shuning uchun qatʼiy eshitiladi: "
                            "bahs qilib boʻlmaydigan haqiqat. Oldida "
                            "aniqlovchi turadi.",
                "examples": ["좋은 일에는 시간이 걸리는 법이다.",
                             "아픈 마음도 작아지는 법이에요."],
            },
            {
                "pattern":  "Nega bu qoliplar maqol tilida",
                "meaning":  "Maqol — hammaga tegishli, vaqtdan tashqari "
                            "haqiqat. Shuning uchun bu ikki qolip maqol va "
                            "TOPIK II matnlarining xulosasida koʻp uchraydi.",
                "examples": ["시간이 지나면 아픈 마음도 작아지는 법이에요."],
            },
        ],
        "body": '''<p>우리 <span class="cn-word" data-tr="buvim">할머니</span>는 <span class="cn-word" data-tr="gapi koʻp emas">말이 많지 않았어요</span>. 하지만 세 가지 말은 자주 했어요.</p>

<p><span class="cn-word" data-tr="birinchi">첫 번째</span> 말은 “사람은 <span class="cn-word" data-pos="adv" data-tr="har qanday odam">누구나</span> <span class="cn-word" data-pos="verb" data-tr="xato qilishi tabiiy">실수하기 마련이다</span>”였어요. 제가 열 살 때 어머니의 <span class="cn-word" data-tr="idish">그릇</span>을 <span class="cn-word" data-pos="verb" data-tr="sindirdim">깼어요</span>. 저는 많이 울었어요. 할머니는 <span class="cn-word" data-pos="adv" data-tr="kulib">웃으면서</span> 그 말을 했어요.</p>

<p><span class="cn-word" data-tr="ikkinchi">두 번째</span> 말은 “좋은 일에는 시간이 <span class="cn-word" data-pos="verb" data-tr="ketishi qonun">걸리는 법이다</span>”였어요. 저는 한국어를 배울 때 너무 빨리 잘하고 싶었어요. 삼 개월 후에 <span class="cn-word" data-pos="verb" data-tr="tashlab qoʻymoqchi boʻldim">포기하고 싶었어요</span>. 그때 할머니가 그 말을 했어요. 그래서 저는 포기하지 않았어요.</p>

<p><span class="cn-word" data-tr="uchinchi">세 번째</span> 말은 “시간이 지나면 <span class="cn-word" data-pos="verb" data-tr="unutilishi tabiiy">잊기 마련이다</span>”였어요. 저는 이 말을 <span class="cn-word" data-pos="adv" data-tr="uzoq vaqt">오래</span> <span class="cn-word" data-pos="verb" data-tr="tushunmadim">이해하지 못했어요</span>. 잊는 것은 <span class="cn-word" data-pos="adj" data-tr="yomon">나쁜</span> 일이라고 생각했어요.</p>

<p><span class="cn-word" data-tr="oʻtgan yili">작년</span>에 할머니가 <span class="cn-word" data-pos="verb" data-tr="dunyodan oʻtdi">세상을 떠났어요</span>. 저는 매일 울었어요. 그리고 할머니의 세 번째 말을 <span class="cn-word" data-pos="verb" data-tr="esladim">기억했어요</span>. 저는 <span class="cn-word" data-pos="verb" data-tr="unutishni istamadim">잊고 싶지 않았어요</span>.</p>

<p>하지만 지금은 매일 울지 않아요. 할머니를 잊었기 때문이 아니에요. <span class="cn-word" data-tr="qaygʻu">슬픔</span>이 조금 <span class="cn-word" data-pos="verb" data-tr="kichrayganligi">작아졌기</span> 때문이에요. 할머니는 아직 제 <span class="cn-word" data-tr="yodimda">기억 속</span>에 있어요.</p>

<p>이제 저는 알아요. 할머니의 세 번째 말도 <span class="cn-word" data-pos="adj" data-tr="toʻgʻri edi">맞았어요</span>. 시간이 지나면 <span class="cn-word" data-tr="ogʻriq koʻngil">아픈 마음</span>도 작아지는 법이에요. 그건 잊는 것이 아니에요. <span class="cn-word" data-pos="verb" data-tr="yashash">사는</span> 것이에요.</p>''',
        "questions": [
            {
                "text": "Buvi birinchi gapni qachon aytgan edi?",
                "choices": [
                    "Nabirasi koreys tilini boshlaganda",
                    "Nabirasi onasining idishini sindirib yigʻlaganda",
                    "Nabirasi maktabga borganda",
                    "Nabirasi imtihondan yiqilganda",
                ],
                "answer": 1,
                "explanation": "“사람은 누구나 <b>실수하기 마련이다</b>” — "
                               "aynan tasalli berish uchun aytilgan. "
                               "기 마련이다 ning eng tabiiy oʻrni shu.",
            },
            {
                "text": "Nega hikoyachi koreys tilini tashlab qoʻymadi?",
                "choices": [
                    "Onasi ruxsat bermagani uchun",
                    "Imtihon yaqin boʻlgani uchun",
                    "Buvisining “yaxshi ishga vaqt ketadi” degan gapi "
                    "esiga tushgani uchun",
                    "Doʻstlari yordam bergani uchun",
                ],
                "answer": 2,
                "explanation": "“좋은 일에는 시간이 <b>걸리는 법이다</b>” — "
                               "법 (“qonun”) soʻzi bu gapga qatʼiylik "
                               "beradi.",
            },
            {
                "text": "Hikoyachi buvisining uchinchi gapini oxirida qanday "
                        "tushundi?",
                "choices": [
                    "Unutish — yomon narsa ekan",
                    "Vaqt oʻtsa ogʻriq kichrayadi, lekin bu unutish emas",
                    "Buvisini butunlay unutish kerak ekan",
                    "Uchinchi gap notoʻgʻri ekan",
                ],
                "answer": 1,
                "explanation": "“아픈 마음도 <b>작아지는 법이에요</b>. 그건 "
                               "잊는 것이 아니에요” — 아/어지다 (PK-56) "
                               "va 법이다 birga ishlagan xulosa jumlasi.",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "한국 여행 팁 여섯 가지",
        "summary": (
            "PK-73 matni. Amaliy maslahat roʻyxati: Koreyaga birinchi marta "
            "boradiganlar uchun ehtimol va ogohlantirish tili."
        ),
        "order":   73,
        "grammar": [
            {
                "pattern":  "(으)ㄹ지도 모르다 — ehtimol",
                "meaning":  "“…shi mumkin”. Eng past ishonch darajasi — "
                            "soʻzlovchi aniq bilmaydi, faqat ehtimolni "
                            "aytadi.",
                "examples": ["여름에는 비가 많이 올지도 몰라요.",
                             "배가 아플지도 몰라요.",
                             "유명한 곳은 붐빌지도 몰라요."],
            },
            {
                "pattern":  "기 십상이다 — ogohlantirish",
                "meaning":  "十常 = “oʻn martadan oʻni”. Natija DOIM "
                            "salbiy, shuning uchun bu ogohlantirish "
                            "qolipi. Oldida 기 keladi.",
                "examples": ["지도 없이 가면 길을 잃기 십상이에요.",
                             "서두르면 아무것도 못 보기 십상이에요."],
            },
            {
                "pattern":  "(으)면 + ogohlantirish",
                "meaning":  "기 십상이다 deyarli har doim (으)면 (PK-36) "
                            "bilan yuradi: shart aytiladi, keyin yomon "
                            "natija ogohlantiriladi.",
                "examples": ["카드 없이 다니면 돈을 많이 쓰기 십상이에요."],
            },
        ],
        "body": '''<p><strong>한국에 처음 가는 사람을 위한 팁 여섯 가지</strong></p>

<p><strong>1. 지하철.</strong> 서울 지하철은 아주 <span class="cn-word" data-pos="adj" data-tr="chalkash">복잡해요</span>. <span class="cn-word" data-tr="ilova">앱</span>을 미리 <span class="cn-word" data-pos="verb" data-tr="yuklab oling">받으세요</span>. <span class="cn-word" data-tr="xarita">지도</span> <span class="cn-word" data-pos="adv" data-tr="…siz">없이</span> 가면 <span class="cn-word" data-pos="verb" data-tr="adashib qolishingiz turgan gap">길을 잃기 십상이에요</span>.</p>

<p><strong>2. 날씨.</strong> 봄과 <span class="cn-word" data-tr="kuz">가을</span>은 아주 좋아요. 하지만 여름에는 비가 많이 <span class="cn-word" data-pos="verb" data-tr="yogʻishi mumkin">올지도 몰라요</span>. <span class="cn-word" data-tr="soyabon">우산</span>을 꼭 가져가세요.</p>

<p><strong>3. 음식.</strong> 한국 음식은 <span class="cn-word" data-pos="adj" data-tr="achchiq">매워요</span>. 처음 먹는 사람은 <span class="cn-word" data-pos="verb" data-tr="qorni ogʻrishi mumkin">배가 아플지도 몰라요</span>. <span class="cn-word" data-pos="adv" data-tr="ozgina">조금씩</span> 먹어 보세요.</p>

<p><strong>4. 교통카드.</strong> <span class="cn-word" data-tr="Tʼmani karta">티머니 카드</span>를 사세요. 카드 없이 <span class="cn-word" data-pos="verb" data-tr="yursangiz">다니면</span> 돈을 많이 <span class="cn-word" data-pos="verb" data-tr="sarflab qoʻyishingiz turgan gap">쓰기 십상이에요</span>.</p>

<p><strong>5. 시간.</strong> 주말에는 사람이 아주 많아요. <span class="cn-word" data-pos="adj" data-tr="mashhur">유명한</span> 곳은 <span class="cn-word" data-pos="verb" data-tr="gavjum boʻlishi mumkin">붐빌지도 몰라요</span>. 아침 일찍 가세요.</p>

<p><strong>6. 인사.</strong> 한국 사람들은 <span class="cn-word" data-tr="salomlashish">인사</span>를 아주 <span class="cn-word" data-pos="adv" data-tr="muhim">중요하게</span> 생각해요. 인사를 안 하면 <span class="cn-word" data-pos="verb" data-tr="notoʻgʻri tushunilishingiz turgan gap">오해를 받기 십상이에요</span>.</p>

<p><span class="cn-word" data-tr="oxirida">마지막으로</span> 하나 더. <span class="cn-word" data-tr="reja">계획</span>을 너무 많이 <span class="cn-word" data-pos="verb" data-tr="tuzmang">세우지 마세요</span>. <span class="cn-word" data-pos="verb" data-tr="shoshsangiz">서두르면</span> <span class="cn-word" data-pos="adv" data-tr="hech narsani">아무것도</span> 못 보기 십상이에요. 천천히 <span class="cn-word" data-pos="verb" data-tr="yuring">다니세요</span>. 그게 제일 좋은 여행이에요.</p>''',
        "questions": [
            {
                "text": "Nima uchun metro ilovasini oldindan yuklash "
                        "tavsiya qilingan?",
                "choices": [
                    "Chunki metro qimmat",
                    "Chunki xaritasiz borsa adashib qolish ehtimoli juda "
                    "yuqori",
                    "Chunki metro yopiq boʻlishi mumkin",
                    "Chunki ilova bepul",
                ],
                "answer": 1,
                "explanation": "“지도 없이 가면 길을 <b>잃기 십상이에요</b>” "
                               "— 십상 (十常) “oʻn martadan oʻni” degani, "
                               "yaʼni deyarli aniq.",
            },
            {
                "text": "Matnda 올지도 몰라요 va 잃기 십상이에요 — farqi "
                        "nimada?",
                "choices": [
                    "Ikkalasi bir xil",
                    "Birinchisi — shunchaki ehtimol; ikkinchisi — deyarli "
                    "aniq va salbiy ogohlantirish",
                    "Birinchisi salbiy, ikkinchisi ijobiy",
                    "Birinchisi oʻtgan zamon",
                ],
                "answer": 1,
                "explanation": "<b>(으)ㄹ지도 모르다</b> — past ishonch "
                               "(“balki yogʻar”). <b>기 십상이다</b> — "
                               "yuqori ehtimol va <b>doim yomon</b> "
                               "natija.",
            },
            {
                "text": "Oxirgi maslahat nima?",
                "choices": [
                    "Koʻproq joy koʻrish uchun tez yurish",
                    "Rejani koʻp tuzmaslik — shoshsa hech narsa "
                    "koʻrilmay qoladi",
                    "Faqat mashhur joylarga borish",
                    "Dam olish kunlari sayohat qilish",
                ],
                "answer": 1,
                "explanation": "“서두르면 아무것도 못 <b>보기 십상이에요</b>” "
                               "— (으)면 + 기 십상이다 juftligi, matnda "
                               "toʻrt marta takrorlangan tuzilma.",
            },
        ],
    },
]
