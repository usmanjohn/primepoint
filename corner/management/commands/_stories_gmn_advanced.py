SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Prime Advanced Readings",
    "description": "Qisqa oʻrta daraja (TOPIK II) matnlari — lugʻat, grammatika va savollar bilan.",
    "order":       4,
}

STORIES = [
    # ── 41 ───────────────────────────────────────────────────────────────
    {
        "title":   "뇌과학과 학습",
        "summary": "Inson miyasining tajriba orqali doimo o'zgarib borish qobiliyati — 'Miya plastikligi' (Neuroplasticity) haqida.",
        "order":   41,
        "body": '''<p>과거의 의학계에서는 인간의 뇌 세포가 성장이 끝난 성인기 이후에는 더 이상 변하지 않고 점차 퇴화할 뿐이라고 <span class="cn-word" data-pos="adv" data-tr="shubhasiz, mutloq">단정하곤 했습니다</span>. 그러나 현대 뇌과학은 인간의 뇌가 평생에 걸쳐 끊임없이 스스로의 구조를 재구성한다는 '뇌 가소성(Neuroplasticity)' 이론을 <span class="cn-word" data-pos="adv" data-tr="muvaffaqiyatli ravishda, yaqqol">성공적으로</span> 규명해냈습니다. 우리가 새로운 지식을 배우거나 이전에 해보지 않은 학습 과정을 <strong>거칠 때마다</strong>, 뇌의 신경 세포들은 새로운 시냅스 연결망을 <span class="cn-word" data-pos="adv" data-tr="shiddat bilan, faol">분주하게</span> 만들어내며 스스로를 변화시켜 나갑니다.</p>
<p>이것은 나이가 들더라도 <span class="cn-word" data-pos="adj" data-tr="g'ayratli, faol">지속적인</span> 노력을 기울이면 얼마든지 새로운 기술을 습득할 수 있음을 <span class="cn-word" data-pos="adv" data-tr="ilmiy jihatdan, aniq">과학적으로</span> 입증하는 <span class="cn-word" data-pos="adj" data-tr="shubhasiz, ishonchli">명확한</span> 근거입니다. 반대로 아무런 인지적 자극 없이 <span class="cn-word" data-pos="adj" data-tr="zerikarli, bir xildagi">단조로운</span> 일상만을 반복한다면 쓰지 않는 신경망은 <span class="cn-word" data-pos="adv" data-tr="asta-sekin, sekin-asta">차츰</span> 사라져 뇌의 퇴화가 <span class="cn-word" data-pos="adv" data-tr="tezlik bilan, shiddatli">급속히</span> 진행됩니다. 결국 우리의 뇌는 고정된 기계가 아니라, 착용자의 주체적인 훈련과 경험에 의해 <span class="cn-word" data-pos="adv" data-tr="cheksiz ravishda, to'xtovsiz">무한히</span> <strong>발달할 수 있는</strong> 유기적인 존재인 것입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-을/를 거치다",
                "meaning":  "Ma'lum bir jarayon, bosqich yoki tajribadan o'tishni bildiradi.",
                "examples": ["새로운 학습 과정을 거칠 때마다 뇌가 변화합니다.", "여러 단계의 심사를 거쳐 최종 합격자를 선발했습니다."],
            },
            {
                "pattern":  "-(으)ㄹ 수 있는",
                "meaning":  "Imkoniyat yoki qobiliyatga ega bo'lgan (orqadagi otni aniqlovchi sifatdosh shakli): ... oladigan, ...ish imkoniyati bor.",
                "examples": ["무한히 발달할 수 있는 유기적인 존재입니다.", "그는 이 문제를 해결할 수 있는 좋은 방법을 찾았다."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 설명하는 '뇌 가소성'의 개념으로 가장 적절한 것은 무엇입니까?",
                "choices": [
                    "성인기 이후에는 뇌의 구조적 성장이 완전히 멈추고 파괴된다는 이론",
                    "인간의 뇌가 새로운 경험과 학습에 따라 스스로 변화하고 신경망을 재구성한다는 이론",
                    "새로운 정보를 암기할 때 오직 과거의 기억만을 모두 지워버리는 뇌의 성질",
                ],
                "answer": 1,
                "explanation": "첫 번째 단락에서 뇌 가소성이란 인간의 뇌가 평생에 걸쳐 학습을 통해 새로운 연결망을 스스로 만들며 변화해 나가는 성질이라고 설명했습니다.",
            },
            {
                "text": "이 글의 내용과 일치하지 않는 것을 고르십시오.",
                "choices": [
                    "인지적인 자극을 주지 않고 단순한 일상만 반복하면 뇌의 기능이 차츰 저하된다.",
                    "나이가 든 성인이라도 적절한 훈련을 통해 새로운 지식을 충분히 습득할 수 있다.",
                    "과거 의학계는 뇌 세포가 성인이 된 이후에도 끊임없이 발달한다고 믿었다.",
                    "우리가 직접 훈련을 거듭함에 따라 뇌의 시냅스 연결망이 새롭게 생성된다.",
                ],
                "answer": 2,
                "explanation": "첫 번째 문장의 첫 줄에서 과거 의학계는 성인기 이후의 뇌가 변하지 않고 퇴화할 뿐이라고 단정(단정하곤 했다)했다고 언급했으므로 일치하지 않습니다.",
            },
        ],
    },
    # ── 42 ───────────────────────────────────────────────────────────────
    {
        "title":   "노동법과 현대 사회",
        "summary": "Raqamli platformalar orqali ishlovchi 'Platforma ishchilari' (Gig workers) ning huquqiy himoyasizligi va mehnat qonunchiligi muammolari.",
        "order":   42,
        "body": '''<p>스마트폰 애플리케이션 등 디지털 플랫폼의 보급은 배달 라이더나 1인 대리운전 기사와 같은 새로운 형태의 '플랫폼 노동자'를 <span class="cn-word" data-pos="adv" data-tr="shiddat bilan, keng">대거</span> <span class="cn-word" data-pos="adv" data-tr="yuzaga, maydonga">출현시켰습니다</span>. 이들은 전통적인 근로자와 달리 회사에 <span class="cn-word" data-pos="adv" data-tr="to'g'ridan-to'g'ri, bevosita">직접</span> 소속되지 않은 채 원할 때만 자유롭게 일을 한다는 점에서 일의 유연성을 가집니다. 그러나 이러한 <span class="cn-word" data-pos="adj" data-tr="yuzaki, ko'rinishdagi">겉보기식</span> 자유의 이면에는 법률적 보호의 사각지대라는 <span class="cn-word" data-pos="adj" data-tr="achinarli, qorong'u">어두운</span> 현실이 <span class="cn-word" data-pos="adv" data-tr="chuqur, mustahkam">깊이</span> <strong>도사리고 있습니다</strong>.</p>
<p>현행 근로기준법상 이들은 개인 사업자로 분류되기 때문에, 퇴직금이나 4대 보험 등 기본적인 노동 권리를 보장받기가 <span class="cn-word" data-pos="adj" data-tr="nihoyatda og'ir, g'oyat qiyin">극도로 어렵습니다</span>. 사고가 발생하더라도 모든 경제적 피해와 치료 비용을 스스로 부담해야 하므로 고용 불안이 <span class="cn-word" data-pos="adv" data-tr="haddan tashqari, doimiy">상시로</span> <strong>뒤따를 수밖에 없습니다</strong>. 따라서 노동의 패러다임이 <span class="cn-word" data-pos="adv" data-tr="shiddat bilan, keskin">급격히</span> 변화하는 시대적 흐름에 발맞추어, 법과 제도를 유연하게 개정하여 플랫폼 근로자들을 두텁게 보호하려는 국가적 정비가 절실히 요구됩니다.</p>''',
        "grammar": [
            {
                "pattern":  "-고 있다/도사리고 있다",
                "meaning":  "Harakat yoki holatning davom etayotganini yoki ma'lum bir ko'rinishda yashirinib yotganini bildiradi.",
                "examples": ["법률적 보호의 사각지대라는 현실이 도사리고 있습니다.", "위험 요소가 도처에 도사리고 있어요."],
            },
            {
                "pattern":  "-(으)ㄹ 수밖에 없다",
                "meaning":  "Boshqa iloj yoki chora yo'qligini bildiradi: ...maslikning iloji yo'q, ...ishga majbur.",
                "examples": ["고용 불안이 상시로 뒤따를 수밖에 없습니다.", "비가 많이 오니까 집에서 공부할 수밖에 없네요."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 플랫폼 노동자의 노동 환경에 대해 가장 정확하게 지적한 것은 무엇입니까?",
                "choices": [
                    "전통적인 회사 소속 근로자보다 법적인 혜택과 보험 혜택을 훨씬 많이 받는다.",
                    "겉으로는 자유롭게 일하는 것처럼 보이지만, 기본적인 노동 권리와 고용 안정성을 보호받지 못한다.",
                    "앱을 사용하는 대가로 국가로부터 엄청난 금액의 특별 보조금을 지급받는다.",
                ],
                "answer": 1,
                "explanation": "이들은 형식적으로 유연하게 일하지만, 개인 사업자로 분류되어 퇴직금이나 대형 보험 혜택 등을 받지 못하는 법적 보호 사각지대에 놓여 있다고 서술되어 있습니다.",
            },
            {
                "text": "작가가 유기적인 플랫폼 노동 시장을 안정시키기 위해 주장한 해결책은 무엇입니까?",
                "choices": [
                    "디지털 플랫폼 서비스의 이용을 완전히 금지하여 과거 노동 형태로 돌아간다.",
                    "플랫폼 근로자들이 회사를 상대로 무조건적인 소송을 걸도록 장려한다.",
                    "시대 변화에 맞춰 현행 근로기준법과 노동 제도를 유연하게 개정해야 한다.",
                    "플랫폼 기업들에게 세금을 부과하지 않고 모든 규제를 철폐한다.",
                ],
                "answer": 2,
                "explanation": "마지막 문장에서 변해가는 노동 패러다임에 맞춰 법과 제도를 신속하고 유연하게 개정하여 플랫폼 노동자를 보호해야 한다고 역설했습니다.",
            },
        ],
    },
    # ── 43 ───────────────────────────────────────────────────────────────
    {
        "title":   "행동경제학과 심리",
        "summary": "Insonlarga majburlamay, ijobiy tomonga yo'naltiruvchi bilvosita aralashuv — 'Nadj effekti' (Nudge Theory) haqida.",
        "order":   43,
        "body": '''<p>전통 경제학에서는 인간이 언제나 합리적인 판단을 내린다고 가정하는 반면, 행동경제학은 인간이 주위 환경이나 사소한 장치에 의해 <span class="cn-word" data-pos="adv" data-tr="osongina, tezda">의외로</span> <span class="cn-word" data-pos="adv" data-tr="notog'ri, noto'g'ri yo'nalishga">쉽게</span> 조종될 수 있음을 지적합니다. 이를 설명하는 <span class="cn-word" data-pos="adj" data-tr="juda mashhur, ajoyib">가장 대표적인</span> 이론이 바로 '넛지(Nudge) 효과'입니다. 넛지란 타인의 선택을 강제로 금지하거나 경제적 보상을 주지 않고도, 부드러운 개입을 통해 그들의 행동을 <span class="cn-word" data-pos="adv" data-tr="ijobiy tomonga, istalgan tarzda">바람직한 방향으로</span> <strong>유도하는 기술을 뜻합니다</strong>.</p>
<p>대표적인 예로 남자 화장실 변기 중앙에 작은 파리 모양 스티커를 <span class="cn-word" data-pos="adv" data-tr="aniq qilib, yaqqol">단정하게</span> 붙여두자, 강제로 깨끗이 쓰라고 <span class="cn-word" data-pos="adv" data-tr="shafqatsizlarcha, qattiq">명령하지 않았음에도</span> 변기 밖으로 튀는 소변의 양이 80%나 줄어들었습니다. 이처럼 사람들의 자발적인 참여를 이끌어내는 부드러운 넛지는 공공질서 확립이나 쓰레기 배출 감소와 같은 다양한 정책 설계에도 <span class="cn-word" data-pos="adv" data-tr="keng miqyosda, yalpi">널리</span> <strong>쓰이곤 합니다</strong>. 법적 규제보다 더 세련되게 세상을 긍정적으로 바꾸는 부드러운 힘입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-는 기술을 뜻하다/의미하다",
                "meaning":  "Muayyan tushuncha yoki texnologiyaga ta'rif berishda ishlatiladi: ...ish usulini anglatadi.",
                "examples": ["행동을 바람직한 방향으로 유도하는 기술을 뜻합니다.", "인공지능이란 인간의 지능을 모방하는 기술을 의미합니다."],
            },
            {
                "pattern":  "-곤 하다",
                "meaning":  "Harakat yoki holatning odatda tez-tez takrorlanib turishini bildiradi: ...-ib turadi/turardi.",
                "examples": ["다양한 정책 설계에도 널리 쓰이곤 합니다.", "스트레스가 쌓이면 친한 친구를 만나 수다를 떨곤 해요."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 제시한 '넛지(Nudge)'의 핵심 원리는 무엇입니까?",
                "choices": [
                    "법률적인 강제 금지 조항이나 무거운 벌금을 통해 질서를 강요하는 것",
                    "물리적인 위협이나 강력한 차단 장치로 타인의 자유를 억제하는 것",
                    "강요나 금지 없이, 사소하고 부드러운 유도를 통해 자발적인 행동 변화를 이끄는 것",
                ],
                "answer": 2,
                "explanation": "선택을 억압하거나 인센티브를 주지 않고도 사소한 디자인 설계를 통해 사람들이 올바른 행동을 하도록 유도하는 기술이라고 명확히 정의되어 있습니다.",
            },
            {
                "text": "화장실 변기의 파리 스티커 사례가 입증하는 결과로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "깨끗이 사용하라는 법적 경고문이 벌금 제도보다 훨씬 더 효과적이었다.",
                    "화장실 청소 기계를 대량으로 도입하여 청소 효율성이 현저히 올라갔다.",
                    "사소한 스티커 하나가 자발적인 집중을 이끌어내어 위생 수준을 급격히 향상시켰다.",
                    "스티커를 붙이자마자 소변을 보려는 사용자들의 숫자가 아예 급감했다.",
                ],
                "answer": 2,
                "explanation": "작은 파리 그림 하나를 통해 소변 유출량이 크게 감소한 현상은 강요 없는 부드러운 유도가 스스로의 행동을 깔끔하게 바꾸어 놓았음을 증명합니다.",
            },
        ],
    },
    # ── 44 ───────────────────────────────────────────────────────────────
    {
        "title":   "역사와 지리학",
        "summary": "Madaniyatlarning rivojlanishida georafik sharoit va iqlimning ta'siri hamda buni baholovchi 'Geografik determinizm' nazariyasi.",
        "order":   44,
        "body": '''<p>인류 역사상 존재했던 고대 문명들이 저마다 <span class="cn-word" data-pos="adj" data-tr="ajoyib, o'ziga xos">상이한</span> 형태의 예술과 사회 제도를 구축한 배경에는 기후와 지형 등 지리적 요인이 깊이 <span class="cn-word" data-pos="adv" data-tr="uzviy, chuqur">연관되어</span> 있습니다. 이를 기점으로 인간의 운명이나 사회 발달이 지리적 조건에 의해 <span class="cn-word" data-pos="adv" data-tr="muqarrar ravishda, qat'iy">필연적으로</span> 결정된다고 바라보는 학설을 '지리 결정론'이라고 <strong>부르곤 합니다</strong>. 예컨대 기후가 온화하고 평야가 넓은 지역에서는 일찍이 농경 문화가 고도로 <span class="cn-word" data-pos="adv" data-tr="shiddat bilan, jadal">발달하면서</span> <span class="cn-word" data-pos="adj" data-tr="barqaror, mustahkam">안정적인</span> 중앙집권 국가가 세워지기에 <span class="cn-word" data-pos="adj" data-tr="juda qulay, mos">매우 적합했습니다</span>.</p>
<p>반대로 험준한 산맥이나 사막으로 둘러싸인 <span class="cn-word" data-pos="adj" data-tr="og'ir, noqulay">척박한</span> 지리적 환경에 처한 부족들은 이동식 유목 생활을 <strong>선택할 수밖에 없었으며</strong>, 이는 구성원 간의 평등하고 유연한 사회 구조를 형성하는 원천이 되었습니다. 물론 인류의 기술과 지능이 발달함에 따라 오늘날에는 지리적 제약을 <span class="cn-word" data-pos="adv" data-tr="sezilarli darajada, ancha">지대하게</span> 극복하였지만, 여전히 각 문화권이 가진 고유한 정서적 뿌리를 깊이 들여다보면 그들이 뿌리 내린 대지의 기후와 지형적 가치가 고스란히 남아 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "Tez-tez takrorlanadigan odatiy ish-harakat yoki o'tmishda shunday hisoblanganini bildiradi: ...-ib turadi/keladi.",
                "examples": ["조건에 의해 필연적으로 결정된다고 바라보는 학설을 지리 결정론이라 부르곤 합니다.", "어려울 때는 일기를 쓰며 마음을 달래곤 했어요."],
            },
            {
                "pattern":  "-(으)ㄹ 수밖에 없다",
                "meaning":  "Boshqa chora yoki iloj yo'qligini bildiradi: ...ishga majbur bo'lmoq.",
                "examples": ["유목 생활을 선택할 수밖에 없었습니다.", "시험 기간에는 잠을 줄여가며 공부를 할 수밖에 없어요."],
            },
        ],
        "questions": [
            {
                "text": "이 글에서 설명하는 '지리 결정론'의 핵심 사상은 무엇입니까?",
                "choices": [
                    "문명의 발전 속도는 오로지 개별 국가의 정치 제도에 의해서만 결정된다는 이론",
                    "인간의 삶의 형태, 문화, 국가의 정체성이 지형과 기후 같은 지리적 요인에 의해 지대한 영향을 받는다는 이론",
                    "현대 과학 기술의 힘으로 우주의 모든 행성을 완전히 통제할 수 있다는 학설",
                ],
                "answer": 1,
                "explanation": "첫 번째 문단에서 인간의 운명이나 문화 발달이 기후와 지형 등 지리적 조건에 의해 필연적으로 결정된다고 보는 학설이라고 규정했습니다.",
            },
            {
                "text": "지리적 환경 차이가 인류 문명에 가져온 결과로 일치하지 않는 것은 무엇입니까?",
                "choices": [
                    "평야가 넓은 지역에서는 안정적인 농경 문화와 함께 강력한 국가가 일어났다.",
                    "산맥이나 사막이 있는 척박한 지역에서는 가축을 키우며 이동하는 유목 생활이 보편화되었다.",
                    "지리적 제약은 오늘날 과학 기술의 비약적 발달로 인해 여전히 전혀 극복되지 못하고 있다.",
                    "각 문화권의 가치관과 깊은 사유적 정서 뒤에는 그들이 살았던 땅의 특성이 보존되어 있다.",
                ],
                "answer": 2,
                "explanation": "두 번째 문단에서 인류가 기술 발달로 지리적 제약을 '지대하게 극복했다'고 나와 있으므로, 전혀 극복되지 못했다는 설명은 틀렸습니다.",
            },
        ],
    },
    # ── 45 ───────────────────────────────────────────────────────────────
    {
        "title":   "정보 기술과 알고리즘",
        "summary": "Foydalanuvchiga faqat u yoqtirgan ma'lumotlarni ko'rsatib, dunyoqarashini toraytiruvchi 'Filtr pufagi' (Filter Bubble) xavfi.",
        "order":   45,
        "body": '''<p>인터넷 검색 엔진이나 소셜 미디어는 사용자의 과거 클릭 이력과 체류 시간 데이터를 수집하여 소비자가 가장 좋아할 만한 콘텐츠만을 선별해주는 '개인화 추천 알고리즘'을 <span class="cn-word" data-pos="adv" data-tr="faol ravishda, jadal">광범위하게</span> <strong>활용하는 중입니다</strong>. 내가 굳이 찾으려 <span class="cn-word" data-pos="adv" data-tr="harakat qilmay, urinmay">애쓰지 않아도</span> 내 입맛에 꼭 맞는 정보들이 자동으로 제공되기에 사용자 입장에서는 무척 편리합니다. 그러나 기술적 정교함 뒤에는 나와 의견이 다른 객관적인 뉴스를 원천 차단해버리는 '필터 버블(Filter Bubble)' 현상이 무섭게 <strong>성장하고 있습니다</strong>.</p>
<p>알고리즘이 만든 보이지 않는 거품 속에 갇힌 사용자들은 자신의 편견과 부합하는 주장만을 <span class="cn-word" data-pos="adv" data-tr="tinimsiz, to'xtovsiz">지속적으로</span> 수용하며 편협한 세계관을 갖게 됩니다. 이는 결국 서로 다른 신념을 가진 집단 간의 소통을 방해하고 흑백논리를 자극하여 사회적 갈등을 <span class="cn-word" data-pos="adv" data-tr="chuqur darajada, og'ir">심각하게</span> 부추기는 원인이 됩니다. 무분별하게 추천되는 일방적인 필드를 <span class="cn-word" data-pos="adv" data-tr="shubhasiz, shartsiz">맹목적으로</span> 받아들이기보다, 의도적으로 반대 성향의 의견을 탐색하며 균형을 찾으려는 주체적인 미디어 리터러시 소양이 필요합니다.</p>''',
        "grammar": [
            {
                "pattern":  "-는 중이다",
                "meaning":  "Hozirgi vaqtda davom etayotgan harakatni bildiradi: ...ayotgan jarayonda.",
                "examples": ["알고리즘을 광범위하게 활용하는 중입니다.", "지금 친구들과 함께 한국어 쓰기 시험을 준비하는 중이에요."],
            },
            {
                "pattern":  "-고 있다/성장하고 있다",
                "meaning":  "Harakat yoki holatning davom etayotganini ko'rsatadi.",
                "examples": ["필터 버블 현상이 무섭게 성장하고 있습니다.", "세계 곳곳에서 기후 위기를 극복하려는 움직임이 커지고 있어요."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 지적한 '필터 버블(Filter Bubble)' 현상의 가장 큰 문제점은 무엇입니까?",
                "choices": [
                    "스마트폰의 배터리 소모량을 과도하게 늘려 기기 수명을 단축시키는 것",
                    "개인의 취향과 의견에 맞는 정보만 편향적으로 제공되어 세계관을 좁히고 사회적 분열을 초래하는 것",
                    "인터넷 검색 결과가 로딩되는 시간을 심각하게 늦춰 검색 효율을 낮추는 것",
                ],
                "answer": 1,
                "explanation": "알고리즘이 선별한 정보 가두리 안에 갇혀 자신과 맞는 정보만 보게 되므로 편협한 사고를 갖게 되고, 집단 간 대립과 갈등이 깊어진다고 설명하고 있습니다.",
            },
            {
                "text": "글쓴이가 제시하는 알고리즘 중심 인터넷 환경에 대처하는 올바른 독자의 자세는 무엇입니까?",
                "choices": [
                    "검색 효율을 위해 알고리즘이 자동으로 추천해주는 뉴스 콘텐츠만 맹목적으로 소비한다.",
                    "자신과 생각이 다른 주장이나 플랫폼을 불법 유해 사이트로 국가에 적극 신고한다.",
                    "인터넷을 완전히 끊고 오직 종이 신문과 텔레비전 뉴스만을 일방적으로 신뢰한다.",
                    "의도적으로 나와 반대되는 성향의 다양한 의견을 찾아 읽으며 균형 있는 사고를 하려고 노력한다.",
                ],
                "answer": 3,
                "explanation": "마지막 문장에서 자동화된 정보 편식에서 탈피해, 주체적이고 능동적으로 다양한 의견을 확인하고 조율하는 리터러시 역량이 필요하다고 언급했습니다.",
            },
        ],
    },

    # ── 46 ───────────────────────────────────────────────────────────────
    {
        "title":   "역사학과 디지털 아카이브",
        "summary": "Madaniy meroslarni raqamli shaklga o'tkazish (Digital Archiving) orqali ularni abadiy saqlash va ommalashtirish haqida.",
        "order":   46,
        "body": '''<p>전쟁이나 자연재해로 인해 한 번 <span class="cn-word" data-pos="adv" data-tr="shafqatsizlarcha, butkul">손실된</span> 인류의 역사적 유물은 두 번 다시 원래의 상태로 <strong>복구하기가 불가능합니다</strong>. 이러한 아쉬움을 <span class="cn-word" data-pos="adv" data-tr="samorali tarzda, sezilarli">혁신적으로</span> 보완하기 위해 최근 역사학계에서는 3D 스캔 기술을 활용해 문화재를 가상 세계에 영구히 기록하는 '디지털 아카이브(Digital Archive)' 구축에 <span class="cn-word" data-pos="adv" data-tr="faol ravishda, jadal">박차를 가하고 있습니다</span>. 이 작업은 유물의 물리적 파손을 <span class="cn-word" data-pos="adv" data-tr="mukammal tarzda, butkul">완벽히</span> 방지할 수 있는 <span class="cn-word" data-pos="adj" data-tr="ajoyib, mukammal">탁월한</span> 방안으로 꼽힙니다.</p>
<p>또한 디지털 데이터로 변환된 문화유산은 시공간의 제약을 넘어 전 세계의 학자들과 대중에게 <span class="cn-word" data-pos="adv" data-tr="osonlik bilan, bemalol">실시간으로</span> <span class="cn-word" data-pos="adv" data-tr="keng miqyosda, bemalol">공유될 수 있습니다</span>. 박물관 유리창 너머로만 바라보던 귀한 서책이나 조각상을 입체적으로 <span class="cn-word" data-pos="adv" data-tr="sinchkovlik bilan, batafsil">정밀하게</span> 관찰하고 간접 체험하는 일이 <strong>가능해진 것입니다</strong>. 이처럼 아날로그식 보존 방식에만 머무르지 않고 디지털 첨단 기술을 <span class="cn-word" data-pos="adv" data-tr="uyg'un tarzda, qo'shib">접목하는</span> 역동적인 시도는 인류의 공통 자산을 영원히 보존하고 그 가치를 <span class="cn-word" data-pos="adj" data-tr="g'oyatda ulkan, yuksak">막대하게</span> 증폭시키는 진화적 통로입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-기(가) 불가능하다/어렵다",
                "meaning":  "Muayyan harakatni amalga oshirish mutlaqo imkonsiz yoki juda qiyinligini bildiradi.",
                "examples": ["원래의 상태로 복구하기가 불가능합니다.", "외국어 단어를 하루 만에 다 외우기는 불가능해요."],
            },
            {
                "pattern":  "-어/아지다 (가능해지다)",
                "meaning":  "Holatning o'zgarib borishi yoki yangi imkoniyat paydo bo'lishini ko'rsatadi: ...adigan bo'lib qolmoq.",
                "examples": ["유물을 세밀하게 관찰하는 일이 가능해진 것입니다.", "날씨가 점차 따뜻해지고 있네요."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 설명하는 '디지털 아카이브'의 가장 핵심적인 의의는 무엇입니까?",
                "choices": [
                    "유물을 가상 공간에 기록하여 물리적 훼손 위험을 방지하고 전 세계와 공유하는 것",
                    "파손된 실제 유물을 화학적 약품을 사용하여 과거와 똑같은 새것으로 교체하는 것",
                    "박물관의 관람료를 올려 유물 복구를 위한 국가적 자금을 마련하는 것",
                ],
                "answer": 0,
                "explanation": "첫 번째 문단에서 물리적 파손을 막고 가상 세계에 유물을 영구히 기록하여 누구나 쉽게 실시간으로 관찰할 수 있도록 만든다고 서술되어 있습니다.",
            },
            {
                "text": "이 글의 내용과 일치하지 않는 것을 고르십시오.",
                "choices": [
                    "한 번 파괴된 유물은 아날로그적 방법만으로는 예전 모습 그대로 살리기 매우 힘들다.",
                    "3D 스캔 기술로 만들어진 문화재 데이터는 인터넷을 통해 실시간 공유가 가능하다.",
                    "디지털 아카이브가 활성화되면 박물관을 직접 방문하는 행위의 질적 한계가 넓어진다.",
                    "디지털로 박제된 데이터는 해킹 위험이 매우 크기 때문에 유물의 현장 관람만을 고집해야 한다.",
                ],
                "answer": 3,
                "explanation": "작가는 디지털 아카이브 기술을 인류의 소중한 자산을 영원히 지키고 가치를 넓히는 유용한 도구로 적극 칭찬하고 있으며, 전면 거부를 권유하지 않습니다.",
            },
        ],
    },
    # ── 47 ───────────────────────────────────────────────────────────────
    {
        "title":   "심리학과 인지 편향",
        "summary": "Insonlarning o'z qobiliyatlarini haddan tashqari yuqori baholashi va bilimsizlarning o'ziga ishonishi — 'Danning-Kryuger effekti' (Dunning-Kruger Effect).",
        "order":   47,
        "body": '''<p>지식을 아주 <span class="cn-word" data-pos="adv" data-tr="yuzaki, sayoz">얕게</span> 배운 사람이 깊은 학식을 가진 전문가보다 더 큰 자신감을 보이는 <span class="cn-word" data-pos="adj" data-tr="g'alati, noodatiy">이상한</span> 현상이 사회에서 <span class="cn-word" data-pos="adv" data-tr="tez-tez, doimo">종종</span> 관찰됩니다. 심리학에서는 이를 자신의 실제 능력보다 아는 것이 적을수록 오히려 스스로의 실력을 과대평가한다는 의미의 '더닝 크루거 효과(Dunning-Kruger Effect)'라고 <strong>부르곤 합니다</strong>. 지식의 양이 <span class="cn-word" data-pos="adj" data-tr="kam, yetarsiz">부족할 때는</span> 자신이 무엇을 모르는지조차 인지하지 못해 <span class="cn-word" data-pos="adv" data-tr="o'rinsiz ravishda, asossiz">터무니없이</span> 용감해지기 <strong>쉽기 때문입니다</strong>.</p>
<p>그러나 깊이 있는 공부를 시작하여 앎의 지평이 넓어질수록, 자신이 가진 지식의 한계를 <span class="cn-word" data-pos="adv" data-tr="shubhasiz, yaqqol">비로소</span> 깨닫게 되며 사람의 태도는 <span class="cn-word" data-pos="adv" data-tr="tobora, kundan-kunga">점차</span> 겸손하게 바뀝니다. 진짜 전문가는 세상의 복잡성을 이해하기 때문에 함부로 확답하지 않고 신중하게 접근합니다. 자신의 무지를 솔직하게 인정하는 메타인지적 태도야말로 더닝 크루거의 함정에서 벗어나 타인과의 <span class="cn-word" data-pos="adj" data-tr="samimiy, iliq">지성적인</span> 소통을 가능하게 만드는 핵심 열쇠입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "Tez-tez takrorlanib turadigan odatiy ish-harakatni bildiradi: ...-ib turadi.",
                "examples": ["스스로의 실력을 과대평가한다고 부르곤 합니다.", "기분이 우울할 때는 클래식 음악을 듣곤 해요."],
            },
            {
                "pattern":  "-기 쉽기 때문이다",
                "meaning":  "Biror holatga moyillik yoki imkoniyat yuqoriligining sababini tushuntiradi: ... bo'lishi oson bo'lganligi uchundir.",
                "examples": ["자신이 무엇을 모르는지 몰라 터무니없이 용감해지기 쉽기 때문입니다.", "옷을 얇게 입으면 감기에 걸리기 쉽기 때문이지요."],
            },
        ],
        "questions": [
            {
                "text": "더닝 크루거 효과가 일어나는 심리적 원인으로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "아는 것이 적은 사람은 자신이 모른다는 사실조차 인지하지 못해 지나친 자신감을 가지기 때문에",
                    "이미 세상의 복잡한 논리를 완벽히 파악하여 아무런 두려움이 남아 있지 않기 때문에",
                    "과거에 뇌 손상을 입어 순간적인 인지 판단 장애를 앓고 있기 때문에",
                ],
                "answer": 0,
                "explanation": "첫 번째 단락에서 얕은 지식을 지닌 상태에서는 자신이 무엇을 놓치고 있는지 알지 못해 근거 없는 용감함을 갖기 쉽다고 설명했습니다.",
            },
            {
                "text": "본문의 전문가(진짜 지식인)가 취하는 태도로 올바른 것은 무엇입니까?",
                "choices": [
                    "자신이 세상의 모든 지식을 완벽하게 알고 있다고 자부하며 대중을 훈계한다.",
                    "앎의 한계를 자각하여 함부로 확언하지 않고 겸손하게 사실에 접근한다.",
                    "질문을 받았을 때 모르는 척 연기하며 타인과의 소통을 완전히 거부한다.",
                    "지식을 타인에게 빼앗기지 않기 위해 비밀 장소에 가두고 혼자 연구한다.",
                ],
                "answer": 1,
                "explanation": "두 번째 문단에서 공부가 깊어질수록 지식의 한계를 자각하고 점차 겸손한 태도를 취하며 사실에 신중히 다가간다고 서술되어 있습니다.",
            },
        ],
    },
    # ── 48 ───────────────────────────────────────────────────────────────
    {
        "title":   "생태학과 우주과학",
        "summary": "Yer sirtidagi mikroorganizmlarning ekstremal sharoitlarda omon qolishi va koinotda hayot izlash (Astrobiologiya) dagi o'rni.",
        "order":   48,
        "body": '''<p>남극의 <span class="cn-word" data-pos="adj" data-tr="ayozli, g'oyat sovuq">매서운</span> 빙하 속이나 수온이 100도에 달하는 깊은 바닷속 열수구처럼 생명체가 살기에 <span class="cn-word" data-pos="adj" data-tr="o'ta noqulay, o'ta og'ir">극도로 척박한</span> 환경에서도 <span class="cn-word" data-pos="adv" data-tr="ajoyib tarzda, muvaffaqiyatli">끈질기게</span> 생명을 이어가는 미생물들이 있습니다. 학계에서는 이들을 '극한 생물(Extremophile)'이라고 <strong>부르고 있습니다</strong>. 인간의 상식으로는 도저히 생존할 수 없을 것 같은 고열, 고압, 그리고 강한 방사선 구역에서도 유전자를 보존하고 번식하는 이들의 생명력은 전 세계 과학자들을 <span class="cn-word" data-pos="adv" data-tr="chuqur, hayratda">깊이</span> 매료시켰습니다.</p>
<p>이 극한 생물의 존재는 우주 생명체를 탐색하는 '외계 생물학' 연구에 <span class="cn-word" data-pos="adj" data-tr="g'oyatda ulkan, juda katta">결정적인</span> 영감을 제공합니다. 태양계 내의 화성이나 목성의 위성인 유로파처럼 환경이 <span class="cn-word" data-pos="adj" data-tr="og'ir, sovuq">가혹한</span> 행성이라도 지구의 극한 생물과 유사한 미생물이 존재할 수 있다는 가정이 <span class="cn-word" data-pos="adv" data-tr="ilmiy jihatdan, aniq">과학적으로</span> 성립하기 때문입니다. 지구 안의 작은 미생물을 연구하는 일이 결국 우주 저편의 생명 기원을 밝혀내는 <span class="cn-word" data-pos="adj" data-tr="ajoyib, ulug'vor">위대한</span> 출발점이 <strong>되는 셈입니다</strong>.</p>''',
        "grammar": [
            {
                "pattern":  "-고 있다/부르고 있다",
                "meaning":  "Harakat yoki holatning davom etayotganini ko'rsatadi.",
                "examples": ["이들을 극한 생물이라고 부르고 있습니다.", "우리는 인류의 미래를 위해 친환경 에너지를 개발하고 있어요."],
            },
            {
                "pattern":  "-는 셈이다 (되는 셈이다)",
                "meaning":  "Xulosa qilishda yoki baholashda ishlatiladi: ...gan hisoblanadi, deyarli ... bilan barobar.",
                "examples": ["우주 저편의 생명 기원을 밝혀내는 출발점이 되는 셈입니다.", "시험을 다 풀었으니 이번 학기 공부는 끝난 셈이에요."],
            },
        ],
        "questions": [
            {
                "text": "본문의 '극한 생물(Extremophile)'이 우리 인간에게 시사하는 생물학적 가치는 무엇입니까?",
                "choices": [
                    "인간보다 똑똑한 두뇌를 개발할 수 있는 유전 공학 기술의 토대가 된다.",
                    "우리가 살기 척박하다고 여기는 고온, 방사선 등 극한 조건 속에서도 생명이 번식할 수 있음을 입증하는 것",
                    "남극과 온천의 관광 상품 가격을 획기적으로 낮추는 생태적 자원",
                ],
                "answer": 1,
                "explanation": "인간 상식 밖의 극심한 환경(고온, 남극 빙하, 방사선)에서도 미생물이 왕성히 번식하고 유전자를 지켜낼 수 있음을 보여주어 생명의 영속성을 보여줍니다.",
            },
            {
                "text": "지구 안의 극한 생물 연구가 '외계 생물학' 발전에 기여하는 이치로 알맞은 것은 무엇입니까?",
                "choices": [
                    "외계인들이 이미 지구의 극한 미생물을 불법적으로 복제해 갔기 때문에",
                    "화성이나 유로파같이 기후가 몹시 가혹한 우주 환경에도 미생물이 살 수 있다는 근거가 되기 때문에",
                    "지구의 미생물을 우주로 쏘아 보내 우주 기지를 무료로 단시간에 건설할 수 있어서",
                    "지구 온난화 현상을 완벽히 통제할 수 있는 우주용 거대 필터를 만들어 주기 때문에",
                ],
                "answer": 1,
                "explanation": "두 번째 문단에서 환경이 몹시 가혹한 타 행성에서도 지구의 극한 미생물과 비슷한 생명체가 능히 살 수 있다는 과학적 타당성을 제공하기 때문이라고 설명했습니다.",
            },
        ],
    },
    # ── 49 ───────────────────────────────────────────────────────────────
    {
        "title":   "철학과 수사학",
        "summary": "Qadimgi Yunoniston faylasufi Sokratning 'Sokratik muloqot' (Socratic Dialogue) orqali o'z bilimsizligini anglatish usuli.",
        "order":   49,
        "body": '''<p>고대 그리스의 철학자 소크라테스는 제자들에게 어떠한 지식을 <span class="cn-word" data-pos="adv" data-tr="bir tomonlama, majburlab">일방적으로</span> 주입하지 않고, 사소한 대화를 통해 상대방 스스로가 진리를 <span class="cn-word" data-pos="adv" data-tr="osongina, oxir-oqibat">발견할 수 있도록</span> 유도했습니다. 이러한 대화법을 '산파술(Socratic Method)' 혹은 '소크라테스적 대화법'이라고 <strong>부르곤 합니다</strong>. 그는 대화 상대가 당연하게 믿어왔던 도덕이나 철학적 관념에 대해 <span class="cn-word" data-pos="adv" data-tr="muntazam ravishda, tinimsiz">끊임없이</span> 질문을 던짐으로써, 스스로가 진정으로 알고 있던 것이 아무것도 없음을 깨닫게 <strong>만드는 데 집중했습니다</strong>.</p>
<p>그는 진정한 배움과 깨달음은 자기 자신의 무지를 <span class="cn-word" data-pos="adv" data-tr="chin dildan, samimiy">솔직하게</span> 인정하는 순간 시작된다고 믿었습니다. 이러한 교육적 유도는 상대방의 자존심을 <span class="cn-word" data-pos="adv" data-tr="shafqatsizlarcha, mutloq">여지없이</span> 무너뜨리기도 하지만, 편견에 갇힌 좁은 우물 안에서 벗어나 스스로 사유하는 주체적인 지성으로 성장시키는 <span class="cn-word" data-pos="adj" data-tr="g'oyatda samarali, yuksak">막강한</span> 추진력이 되었습니다. 참된 지식은 주입식 강의가 아니라, 의심과 성찰 속에서 <span class="cn-word" data-pos="adv" data-tr="sekin-asta, shoshilmasdan">스스로</span> 탄생시켜야 하는 영혼의 결과물입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "Tez-tez takrorlanadigan odatiy ish-harakatni bildiradi: ...-ib turadi.",
                "examples": ["소크라테스적 대화법이라고 부르곤 합니다.", "어려운 일이 생기면 밤늦게 일기를 쓰며 사색하곤 했어요."],
            },
            {
                "pattern":  "-는 데 집중하다",
                "meaning":  "Diqqatni faqat ma'lum bir harakatga yoki maqsadga qaratishni bildiradi: ...ishga diqqat qaratmoq.",
                "examples": ["아무것도 없음을 깨닫게 만드는 데 집중했습니다.", "저는 한국어 TOPIK 쓰기 점수를 높이는 데 집중하는 중입니다."],
            },
        ],
        "questions": [
            {
                "text": "소크라테스가 대화 속에서 상대방에게 무수한 질문을 지속적으로 던진 진짜 의도는 무엇입니까?",
                "choices": [
                    "지적으로 상대방의 기를 꺾어 경쟁에서 완벽히 이기고 굴복시키기 위해",
                    "상대방이 고정관념을 돌아보고 자신의 무지를 자각하여 스스로 질문과 답을 찾도록 돕기 위해",
                    "아테네 광장에 모인 수많은 대중들 앞에서 철학적 연설 기회를 대거 독점하기 위해",
                ],
                "answer": 1,
                "explanation": "주입식 방식이 아니라, 질문을 주고받는 과정을 통해 상대방이 신봉하던 고정관념의 오류와 무지를 스스로 확인하고 주체적으로 생각하도록 유도하기 위함입니다.",
            },
            {
                "text": "본문에 기재된 참된 지식에 도달하는 올바른 조건은 무엇입니까?",
                "choices": [
                    "풍부한 암기 자료와 주입식 강의를 아무런 의심 없이 맹목적으로 받아들이는 것",
                    "타인의 주장은 철저히 배격하고 오직 자신의 신념만이 참되다고 선언하는 것",
                    "편견을 깨부수고 스스로의 무지를 자각하는 성찰과 의심의 과정을 거치는 것",
                    "철학적 의문을 아예 가지지 않고 복잡한 사유 과정을 단호히 거부하는 것",
                ],
                "answer": 2,
                "explanation": "마지막 두 줄에서 참된 지식은 주입식이 아닌 의심과 성찰 속에서 영혼 스스로 낳는 결과물이어야 하며, 자신의 무지를 고백할 때 교육과 사유가 시작된다고 했습니다.",
            },
        ],
    },
    # ── 50 ───────────────────────────────────────────────────────────────
    {
        "title":   "인류학과 음식 문화",
        "summary": "Madaniyatlarni o'z me'yorlari bilan emas, balki joylashgan muhiti nuqtai nazaridan tushunish — 'Madaniy nisbiylik' (Cultural Relativism) haqida.",
        "order":   50,
        "body": '''<p>어느 특정 부족이 곤충을 즐겨 먹는 행위를 볼 때, 현대적 가치관에 익숙한 이들은 <span class="cn-word" data-pos="adv" data-tr="osongina, tezda">흔히</span> 미개하거나 불결하다고 <span class="cn-word" data-pos="adv" data-tr="shoshilinch ravishda, osonlikcha">경솔하게</span> <strong>판단하곤 합니다</strong>. 하지만 인류학적 도구인 '문화 상대주의(Cultural Relativism)'적 관점에서 들여다보면, 이는 해당 지역의 지리적 여건이나 기후 환경에 <span class="cn-word" data-pos="adv" data-tr="mukammal tarzda, butkul">완벽히</span> 적응하기 위한 생존의 지혜입니다. 사막이나 열대 우림처럼 목축이 <span class="cn-word" data-pos="adj" data-tr="juda qiyin, og'ir">매우 어려운</span> 환경에서는 곤충이야말로 소중한 단백질을 <span class="cn-word" data-pos="adv" data-tr="samorali, yetarlicha">공급받을 수 있는</span> <span class="cn-word" data-pos="adj" data-tr="ajoyib, bebahor">최선의</span> 자원이었기 때문입니다.</p>
<p>이처럼 문화 상대주의는 모든 사회적 규범과 음식을 자기 기준대로 함부로 평가하지 않고, 그 문화가 탄생한 맥락 안에서 이해하려는 균형 잡힌 시각을 <strong>의미합니다</strong>. 나와 다른 타 문화권을 무작정 지양하고 야만시하기보다, 왜 그러한 독특한 관습이 생겼는지 열린 마음으로 추적하는 포용적인 역량이 지구촌 시대를 살아가는 현대 지식인들에게 꼭 필요한 덕목입니다. 결국 서로 다름을 인정할 때, 다양성이 빛나는 진정한 조화가 실현될 수 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "O'tmishda yoki hozirda tez-tez takrorlanib turadigan odatiy harakatni bildiradi: ...-ib turadi.",
                "examples": ["미개하다고 경솔하게 판단하곤 합니다.", "쉬는 날에는 도서관에서 책을 읽곤 해요."],
            },
            {
                "pattern":  "-을/를 의미하다",
                "meaning":  "Muayyan tushuncha yoki so'zning ma'nosini ochib berishda ishlatiladi: ...ni anglatadi.",
                "examples": ["문화가 탄생한 맥락 안에서 이해하려는 시각을 의미합니다.", "이 마크는 친환경 제품임을 의미해요."],
            },
        ],
        "questions": [
            {
                "text": "본문의 '문화 상대주의(Cultural Relativism)'가 가진 근본적인 교훈은 무엇입니까?",
                "choices": [
                    "인간의 문명 발달 속도가 오직 서구 문화를 모방할 때만 빨라질 수 있다는 믿음",
                    "모든 외계 문화와 과학적 상식을 무조건 거부하는 폐쇄적인 사상",
                    "타 문화권을 자신의 가치관으로 재단하지 않고, 그들이 처한 지리적·사회적 맥락에 맞춰 존중하고 이해하는 태도",
                ],
                "answer": 2,
                "explanation": "모든 규범이나 풍습을 외부 관찰자의 기준이 아닌, 고유한 환경적 생존 지혜와 탄생 맥락 안에서 올바로 보듬고 평등하게 대하는 것이 문화 상대주의의 가치입니다.",
            },
            {
                "text": "특정 지역 부족이 곤충을 음식 자원으로 삼아야 했던 현실적 원인은 무엇입니까?",
                "choices": [
                    "농사와 가축 방목(목축)이 불가능하거나 극도로 척박한 지리적 여건에 처했기 때문에",
                    "단순히 곤충을 활용해 기이한 축제를 열고 관광 수익을 올리기 위해서",
                    "현대식 단백질 보충 가공 식품의 생산 기술이 너무 과도하게 발달했기 때문에",
                    "소나 돼지 같은 대형 가축의 울음소리가 부족의 안전을 늘 위협했기 때문에",
                ],
                "answer": 0,
                "explanation": "첫 번째 단락에서 사막이나 대우림처럼 가축을 방목하여 키우기 힘든 열악한 조건에서 생존을 위해 필수적인 단백질 공급원(곤충)을 선택할 수밖에 없었다고 설명했습니다.",
            },
        ],
    },
]