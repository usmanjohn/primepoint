# Keimyung Short Readings — stories 1–14 (short passages from keimyung_short_story.txt).
# A separate, SHORT collection: keep vocab light (5–10 marks) and grammar to 1–2 points
# per story (STYLE_GUIDE_CORNER.md §6). Story text = Korean, all glosses = Uzbek.
# Import: python manage.py import_corner corner/management/commands/_stories_keimyung_short_1_14.py --author=<AUTHOR>

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: hikoyalar, lugʻat va yozish shablonlari.",
    "icon":    "bi-translate",
    "color":   "#d97706",
}

COLLECTION = {
    "title":       "Prime Short Readings",
    "description": "Qisqa oʻrta daraja (TOPIK II) matnlari — lugʻat, grammatika va savollar bilan.",
    "order":       2,
}

STORIES = [
    # ── 1 ────────────────────────────────────────────────────────────────
    {
        "title":   "환경 보호",
        "summary": "Atrof-muhitni muhofaza qilishda individual harakatlar va 'Zero Waste' (chiqindisiz hayot) harakatining ahamiyati haqida.",
        "order":   1,
        "body": '''<p>최근 전 세계적으로 기후 변화로 인한 자연재해가 <span class="cn-word" data-pos="verb" data-tr="tez-tez sodir boʻlmoqda">빈발하고</span> 있습니다. 지구 온난화의 심각성을 인지한 많은 시민들이 일상생활 속에서 환경을 보호하기 위한 작은 실천을 <span class="cn-word" data-pos="verb" data-tr="boshlamoqda">개시하고</span> 있습니다. 그중에서도 쓰레기 배출을 최소화하려는 '제로 웨이스트(Zero Waste)' 운동이 큰 호응을 얻고 있습니다. 일회용품 사용을 <span class="cn-word" data-pos="verb" data-tr="tiyilmoq, cheklamoq">자제하고</span> 장바구니나 텀블러를 사용하는 것이 대표적인 예입니다.</p>
<p>과거에는 환경 보호가 정부나 대기업의 책임이라고 생각하는 경향이 강했습니다. 개인이 아무리 노력해도 거대한 기후 변화의 흐름을 막기에는 역부족이라고 <span class="cn-word" data-pos="verb" data-tr="hisoblangani">여겨졌기</span> 때문입니다. 하지만 개인의 소비 습관이 바뀌면 기업과 시장도 결국 움직이게 됩니다. 무분별한 소비를 지양하고 친환경 제품을 선택하는 주체적인 태도야말로 지속 가능한 미래를 <span class="cn-word" data-pos="verb" data-tr="kafolatlaydigan">담보하는</span> 가장 확실한 방법입니다. 사소한 행동의 변화가 모여 지구를 구하는 거대한 원동력이 될 수 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-어/아 가다",
                "meaning":  "Harakat yoki holatning kelajak sari davom etib borishini bildiradi: ...-ib bormoq.",
                "examples": ["작은 실천을 통해 환경을 바꿔 갑니다.", "한국어 실력이 점점 늘어 가네요."],
            },
            {
                "pattern":  "-(으)로 인해",
                "meaning":  "Sabab yoki asosni bildiradi (asosan yozma uslubda): ... sababli, ... tufayli.",
                "examples": ["기후 변화로 인해 자연재해가 발생합니다.", "폭설로 인해 비행기가 결항되었습니다."],
            },
        ],
        "questions": [
            {
                "text": "이 글의 중심 생각으로 가장 알맞은 것을 고르십시오.",
                "choices": [
                    "정부 차원의 강력한 환경 규제가 무엇보다 시급하다.",
                    "개인의 사소한 친환경 실천이 모여 큰 변화를 이끌어 낼 수 있다.",
                    "기후 변화를 막기 위해 일회용품 사용을 전면 금지해야 한다.",
                ],
                "answer": 1,
                "explanation": "Matn oxirida kichik oʻzgarishlar yigʻilib, sayyorani qutqaruvchi ulkan harakatlantiruvchi kuch boʻlishi aytilgan. Shuning uchun markaziy gʻoya shaxsiy harakatlarning ahamiyatidir.",
            },
            {
                "text": "본문의 내용과 같은 것을 고르십시오.",
                "choices": [
                    "친환경 제품에 대한 소비자들의 관심이 점점 줄어들고 있다.",
                    "기업의 변화를 유도하려면 정부의 예산 지원이 필수적이다.",
                    "과거에는 환경 보호를 주로 개인의 책임으로 보는 시각이 많았다.",
                    "최근 쓰레기 배출을 줄이기 위한 환경 운동이 많은 관심을 받고 있다.",
                ],
                "answer": 3,
                "explanation": "Matnda 'Zero Waste' (chiqindisiz hayot) harakati katta aks-sado (호응) va qiziqish uygʻotayotgani aniq taʼkidlangan.",
            },
        ],
    },
    # ── 2 ────────────────────────────────────────────────────────────────
    {
        "title":   "대중문화",
        "summary": "Koreya toʻlqini (Hallyu) va madaniy kontentlarning global miqyosda ommalashish sabablari.",
        "order":   2,
        "body": '''<p>최근 한국의 드라마와 음악 등 대중문화 콘텐트가 국경을 넘어 전 세계적인 <span class="cn-word" data-pos="noun" data-tr="ommaviylikni, sevgini">인기를</span> 누리고 있습니다. 과거에는 아시아 일부 지역에 <span class="cn-word" data-pos="verb" data-tr="cheklangan edi">국한되었던</span> 한류가 이제는 유럽, 미주, 아프리카까지 확산되며 글로벌 주류 문화로 자리 잡은 것입니다. 이러한 성공의 배경에는 인터넷 플랫폼의 발달과 스마트폰의 보급이 핵심적인 역할을 했습니다. 시공간의 제약 없이 전 세계 소비자가 실시간으로 콘텐츠를 <span class="cn-word" data-pos="verb" data-tr="isteʼmol qila oladigan">소비할 수 있는</span> 환경이 조성되었기 때문입니다.</p>
<p>또한, 단순히 언어와 문화적 장벽을 넘어 인간의 보편적인 감정과 사회적 메시지를 세련된 영상미로 <span class="cn-word" data-pos="verb" data-tr="ifodalab bera olgani">담아낸 점도</span> 주효했습니다. 타 문화권의 수용자들도 작품 속 인물들의 갈등과 화해에 깊이 공감하며 매력을 느끼게 됩니다. 일방적인 문화 전파를 <span class="cn-word" data-pos="verb" data-tr="chetlab oʻtib, cheklab">지양하고</span>, 글로벌 팬덤과의 양방향 소통을 통해 유대감을 형성하는 현대 한류는 앞으로도 그 파급력이 지속될 것으로 <span class="cn-word" data-pos="verb" data-tr="kutilmoqda">전망됩니다</span>.</p>''',
        "grammar": [
            {
                "pattern":  "-에 그치다",
                "meaning":  "Maʼlum bir darajadan oʻta olmay, toʻxtab qolishni bildiradi: ... bilan cheklanmoq.",
                "examples": ["아시아 지역에 국한되던 한류에 그치지 않았습니다.", "단순한 호기심에 그치면 안 됩니다."],
            },
            {
                "pattern":  "-(으)로 전망되다",
                "meaning":  "Kelajakdagi holat yoki tendensiyani taxmin qilish: ... deb kutilmoqda/taxmin qilinmoqda.",
                "examples": ["그 파급력이 지속될 것으로 전망됩니다.", "올해 경제 성장률은 더 높아질 것으로 전망됩니다."],
            },
        ],
        "questions": [
            {
                "text": "한류가 전 세계적으로 성공할 수 있었던 원인으로 언급되지 않은 것은 무엇입니까?",
                "choices": [
                    "인터넷 플랫폼의 발달과 스마트폰 보급",
                    "한국 정부의 적극적인 자금 지원과 홍보",
                    "인간의 보편적인 감정과 사회적 메시지 반영",
                ],
                "answer": 1,
                "explanation": "Matnda internet, smartfonlar va insoniy tuygʻular tasviri muvaffaqiyat omillari sifatida keltirilgan, ammo hukumatning moliyaviy yordami haqida gapirilmagan.",
            },
            {
                "text": "본문의 내용과 일치하는 것을 고르십시오.",
                "choices": [
                    "한류는 과거에 비해 영향력이 점차 축소되는 추세이다.",
                    "글로벌 팬들과의 일방적인 소통이 성공의 열쇠였다.",
                    "현대 한류는 타 문화권 사람들의 공감을 이끌어내고 있다.",
                    "과거 한류는 전 세계 모든 대륙에서 고르게 인기가 있었다.",
                ],
                "answer": 2,
                "explanation": "Matnning ikkinchi qismida boshqa madaniyat egalari ham qahramonlarning toʻqnashuvi va yarashuviga chuqur hamdardlik bildirishlari (공감) aytilgan.",
            },
        ],
    },

    # ── 3 ────────────────────────────────────────────────────────────────
    {
        "title":   "전통문화",
        "summary": "Koreya anʼanaviy uyi (Xanok) va undagi ekologik toza isitish tizimi (Ondol) haqida.",
        "order":   3,
        "body": '''<p>한국의 전통 가옥인 한옥은 자연과의 조화를 최우선으로 삼아 <span class="cn-word" data-pos="adj" data-tr="qurilgan, tiklangan">지어졌습니다</span>. 주변의 지형을 <span class="cn-word" data-pos="verb" data-tr="buziymagan holda">훼손하지 않고</span> 나무와 돌, 흙 등 자연에서 얻은 재료만을 사용하여 집을 만들었습니다. 한옥의 가장 큰 특징은 겨울을 따뜻하게 보내기 위한 '온돌'과 여름을 시원하게 보내기 위한 '마루'가 한 구조 안에 공존한다는 점입니다. 이 둘의 결합은 대륙성 기후와 해양성 기후의 특성을 동시에 가진 한반도의 자연환경에 <span class="cn-word" data-pos="verb" data-tr="moslashish uchun">적응하기 위한</span> 조상들의 지혜였습니다.</p>
<p>특히 온돌은 방바닥 밑에 구들을 놓고 불을 지펴 돌을 달구는 독창적인 난방 방식입니다. 연기가 방으로 들어오지 않고 바닥 전체를 고르게 데워주기 때문에 겨울철 온도를 효율적으로 <strong>유지할 수 있습니다</strong>. 현대의 보일러 시스템 역시 이 온돌의 원리에서 <span class="cn-word" data-pos="verb" data-tr="kelib chiqqan boʻlib">착안된 것으로</span>, 한옥의 온돌 구조는 서구식 난방에 비해 연료가 적게 <strong>들 뿐만 아니라</strong> 먼지가 날리지 않아 건강에도 매우 유익합니다. 이처럼 한옥은 단순한 주거 공간을 넘어 자연과 인간이 어떻게 공생해야 하는지 <span class="cn-word" data-pos="verb" data-tr="koʻrsatib beruvchi">보여주는</span> 훌륭한 문화유산입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 수 있다",
                "meaning":  "Imkoniyat yoki qobiliyatni bildiradi: ... qila olmoq.",
                "examples": ["겨울철 온도를 효율적으로 유지할 수 있습니다.", "한국어를 유창하게 할 수 있어요."],
            },
            {
                "pattern":  "-(으)ㄹ 뿐만 아니라",
                "meaning":  "Nafaqat u, balki bu ham (qoʻshimcha maʼlumot): ...gina boʻlib qolmay.",
                "examples": ["연료가 적게 들 뿐만 아니라 건강에도 유익합니다.", "그는 친절할 뿐만 아니라 똑똑해요."],
            },
        ],
        "questions": [
            {
                "text": "한옥의 온돌 구조가 가진 장점으로 언급되지 않은 것은 무엇입니까?",
                "choices": [
                    "방바닥 전체를 골고루 따뜻하게 해 준다.",
                    "서구식 난방 방식보다 방을 더 넓게 쓸 수 있다.",
                    "먼지가 날리지 않아 사람의 건강에 좋다.",
                ],
                "answer": 1,
                "explanation": "Matnda xonaning kengligi yoki undan foydalanish maydoni haqida hech qanday maʼlumot berilmagan.",
            },
            {
                "text": "본문의 내용과 일치하지 않는 것을 고르십시오.",
                "choices": [
                    "현대의 보일러 시스템은 한옥의 마루 구조에서 착안되었다.",
                    "한옥은 주변 지형을 파괴하지 않고 자연 재료로 지어졌다.",
                    "온돌과 마루는 한반도의 기후 특성에 적응하기 위한 결과물이다.",
                    "온돌은 방 내부로 연기가 유입되지 않는 독창적인 방식이다.",
                ],
                "answer": 0,
                "explanation": "Zamonaviy boyler tizimi maru (ayvon) emas, balki ondol (polni isitish) prinsipidan olingani matnda aniq yozilgan.",
            },
        ],
    },
    # ── 4 ────────────────────────────────────────────────────────────────
    {
        "title":   "현대 사회",
        "summary": "Bir kishilik xonadonlarning koʻpayishi va buning natijasida iqtisodiyotda 'Yolgʻizlar iqtisodiyoti' (Solo Economy) shakllanishi.",
        "order":   4,
        "body": '''<p>최근 급격한 사회적 변화와 개인주의의 확산으로 인해 1인 가구의 비중이 빠르게 <span class="cn-word" data-pos="verb" data-tr="ortib bormoqda">증가하고 있습니다</span>. 결혼을 필수가 아닌 선택으로 <strong>여기거나</strong>, 혼자만의 자유로운 삶을 추구하는 젊은 층이 늘어났기 때문입니다. 이러한 인구 구조의 변화는 소비 시장의 지형마저 바꾸어 놓았습니다. 과거 다인 가구를 중심으로 이루어지던 상품 기획과 서비스가 이제는 Yolgʻizlar (싱글)족을 <span class="cn-word" data-pos="verb" data-tr="nishonga olgan holda">겨냥한</span> 형태로 빠르게 재편되고 있는 것입니다.</p>
<p>이로 인해 경제학에서는 '솔로 이코노미(Solo Economy)'라는 신조어가 등장했습니다. 유통업계에서는 소용량 포장 식품이나 소형 가전제품의 매출이 급증하고 있으며, 주택 시장에서도 소형 오피스텔의 인기가 고공행진을 <strong>이어가는 중입니다</strong>. 혼자 밥을 먹는 '혼밥'이나 혼자 여행을 떠나는 '혼행'은 더 이상 어색한 풍경이 아니라 하나의 주류 문화로 <span class="cn-word" data-pos="verb" data-tr="tan olindi">인정받고 있습니다</span>. 기업들은 이러한 1인 가구의 심리적 외로움을 <span class="cn-word" data-pos="verb" data-tr="toʻldirish, ovutish uchun">달래 줄</span> 맞춤형 감성 서비스 개발에도 박차를 가하고 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-거나",
                "meaning":  "Ikki yoki undan ortiq harakat/holatdan birini tanlash: ... yoki ...",
                "examples": ["결혼을 선택으로 여기거나 혼자 사는 삶을 추구합니다.", "주말에는 책을 읽거나 영화를 봐요."],
            },
            {
                "pattern":  "-는 중이다",
                "meaning":  "Hozirgi vaqtda davom etayotgan harakatni bildiradi: ...ayotgan jarayonda.",
                "examples": ["소형 오피스텔의 인기가 고공행진을 이어가는 중입니다.", "지금 시험을 준비하는 중입니다."],
            },
        ],
        "questions": [
            {
                "text": "1인 가구 증가가 경제 시장에 미친 영향으로 알мым한 것은 무엇입니까?",
                "choices": [
                    "대용량 가족 패키지 상품의 매출이 크게 늘어났다.",
                    "싱글족을 겨냥한 소형 제품과 소용량 식품의 소비가 증가했다.",
                    "결혼을 필수로 여기는 사회적 분위기가 다시 형성되었다.",
                ],
                "answer": 1,
                "explanation": "Matnda 'Yolgʻizlar iqtisodiyoti' tufayli kichik hajmli mahsulotlar va mayda maishiy texnikalar savdosi keskin oshgani aytilgan.",
            },
            {
                "text": "본문의 내용과 일치하는 것을 고르십시오.",
                "choices": [
                    "현대 사회에서 '혼밥'은 사회적으로 거부당하는 분위기이다.",
                    "기업들은 1인 가구의 심리적 측면에는 관심을 두지 않는다.",
                    "인구 구조의 변화는 소비 시장의 형태를 바꾸지 못했다.",
                    "젊은 층 중에서 혼자만의 자유를 원하는 사람들이 많아졌다.",
                ],
                "answer": 3,
                "explanation": "Birinchi xatboshida yoshlar orasida yolgʻiz va erkin yashashni istovchilar koʻpayganligi aniq keltirilgan.",
            },
        ],
    },
    # ── 5 ────────────────────────────────────────────────────────────────
    {
        "title":   "과학과 기술",
        "summary": "Sunʼiy intellekt (AI) rivojlanishi va uning insoniyat mehnat bozoriga koʻrsatadigan ijobiy hamda salbiy taʼsirlari.",
        "order":   5,
        "body": '''<p>인공지능(AI) 기술이 비약적으로 발달함에 따라 인류의 삶은 과거와는 비교할 수 없을 정도로 <strong>편리해졌습니다</strong>. 인공지능은 단순한 반복 업무를 넘어 데이터 분석, 의학적 진단, 예술적 창작에 이르기까지 인간의 전유물로 <span class="cn-word" data-pos="verb" data-tr="hisoblangan sohalarga">여겨졌던 영역까지</span> 빠르게 <span class="cn-word" data-pos="verb" data-tr="kirib bormoqda">침투하고 있습니다</span>. 이러한 변화는 생산성을 극대화하고 초개인화된 서비스를 제공한다는 점에서 인류에게 커다란 축복이 될 수 있습니다.</p>
<p>그러나 인공지능의 진화가 장밋빛 미래만을 <strong>보장하는 것은 아닙니다</strong>. 가장 큰 우려는 일자리 대체로 인한 고용 불안입니다. 로봇과 인공지능이 인간의 노동력을 대체하면서 단순 노무직뿐만 아니라 전문직 종사자들마저 실업의 위기에 <span class="cn-word" data-pos="verb" data-tr="duchor boʻlishi mumkin">직면할 수 있다는</span> 경고가 나오고 있습니다. 따라서 우리는 기술 개발에만 <span class="cn-word" data-pos="verb" data-tr="berilib ketmasdan">몰두할 것이 아니라</span>, 인공지능과 인간이 조화롭게 공존할 수 있는 법적·제도적 가이드라인을 마련하고 직업 재교육 시스템을 구축하는 등 선제적인 대응을 해야 할 것입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-어/아지다",
                "meaning":  "Holatning oʻzgarishini bildiradi: ...-ib qolmoq, ...lashmoq.",
                "examples": ["인류의 삶은 과거보다 훨씬 편리해졌습니다.", "날씨가 원체 추워지네요."],
            },
            {
                "pattern":  "-는 것은 아니다",
                "meaning":  "Qisman inkor shakli: hamma vaqt ham unday emas, ... degani emas.",
                "examples": ["장밋빛 미래만을 보장하는 것은 아닙니다.", "돈이 많다고 다 행복한 것은 아니다."],
            },
        ],
        "questions": [
            {
                "text": "인공지능 기술의 발전으로 인해 발생하는 가장 큰 우려 사항은 무엇입니까?",
                "choices": [
                    "컴퓨터 하드웨어의 생산 비용 증가",
                    "일자리 대체로 인한 인간의 고용 불안 문제",
                    "예술 및 창작 영역의 완전한 소멸",
                ],
                "answer": 1,
                "explanation": "Ikkinchi xatboshida sunʼiy intellekt keltirib chiqaradigan eng katta xavotir — ish oʻrinlarining egallanishi va ishsizlik ekanligi aytilgan.",
            },
            {
                "text": "글쓴이가 마지막에 강조한 해결책으로 가장 적절한 것은 무엇입니까?",
                "choices": [
                    "인공지능 기술의 개발을 전면 중단해야 한다.",
                    "인간과 기술이 공존할 수 있는 제도적 가이드라인을 만들어야 한다.",
                    "생산성 극대화를 위해 전문직 인력을 대폭 축소해야 한다.",
                    "인공지능이 창작한 예술 작품의 유통을 금지해야 한다.",
                ],
                "answer": 1,
                "explanation": "Muallif oxirgi jumlada texnologiyani toʻxtatishni emas, balki qonuniy va institutsional koʻrsatmalarni (법적·제도적 가이드라인) shakllantirishni taklif qilmoqda.",
            },
        ],
    },
    # ── 6 ────────────────────────────────────────────────────────────────
    {
        "title":   "심리학",
        "summary": "Zamonaviy jamiyatdagi 'FOMO' (Fear of Missing Out) sindromi va undan qutulish uchun 'JOMO' falsafasining ahamiyati.",
        "order":   6,
        "body": '''<p>스마트폰의 대중화와 소셜 미디어(SNS)의 폭발적인 성장은 타인의 일상을 실시간으로 <strong>관찰할 수 있게</strong> 만들었습니다. 대중들은 SNS에 올라온 타인의 화려한 휴가, 맛있는 음식, 행복한 순간들을 보면서 자신만 소외되고 뒤처지고 있다는 불안감을 느끼곤 합니다. 이를 심리학에서는 '포모 증후군(FOMO Syndrome)'이라고 <span class="cn-word" data-pos="verb" data-tr="ataydi">부릅니다</span>. 소외되는 것에 대한 두려움으로 인해 끊임없이 SNS를 <span class="cn-word" data-pos="verb" data-tr="tekshirib turadigan">확인하는</span> 이 증후군은 현대인들의 정신 건강을 해치는 주범으로 지목됩니다.</p>
<p>이러한 중독적 흐름에서 벗어나기 위해 최근에는 역으로 '조모(JOMO)' 라이프 스타일이 새로운 대안으로 <strong>떠오르고 있습니다</strong>. 조모는 소외되는 것을 두려워하지 않고 오히려 혼자만의 고요한 시간을 즐기는 '놓치는 기쁨(Joy of Missing Out)'을 뜻합니다. 무분별한 정보의 인풋을 차단하고, 타인의 시선에서 벗어나 온전히 나 자신의 내면에 집중하는 태도입니다. 진정한 행복은 가상 세계의 연결이 아니라 현실 세계에서 스스로의 속도에 맞춰 살아갈 때 <span class="cn-word" data-pos="verb" data-tr="topilishini">찾아온다는 점을</span> 조모는 우리에게 <span class="cn-word" data-pos="verb" data-tr="eslatib qoʻymoqda">일깨워 줍니다</span>.</p>''',
        "grammar": [
            {
                "pattern":  "-게 만들기",
                "meaning":  "Biror holatga keltirmoq yoki majbur qilmoq: ...-ishga sabab boʻlmoq.",
                "examples": ["타인의 일상을 실시간으로 관찰할 수 있게 만들었습니다.", "아이를 웃게 만드는 인형입니다."],
            },
            {
                "pattern":  "-어/아 오다",
                "meaning":  "Harakatning oʻtmishdan hozirgacha davom etib kelganini bildiradi: ...-ib kelmoq.",
                "examples": ["조모 라이프 스타일이 새로운 대안으로 떠오르고 있습니다.", "우리는 오랜 시간 협력해 왔습니다."],
            },
        ],
        "questions": [
            {
                "text": "밑줄 친 '포모 증후군'이 발생하는 주된 원인은 무엇입니까?",
                "choices": [
                    "지나친 야근으로 인한 육체적 피로",
                    "SNS를 통해 타인의 삶과 자신을 끊임없이 비교하며 느끼는 소외감",
                    "가족 및 친구들과의 오프라인 대화 단절",
                ],
                "answer": 1,
                "explanation": "Matnda yozilishicha, SNS orqali boshqalarning dabdabali hayotini koʻrib, oʻzini ortda qolgandek his qilish (소외감) FOMO sindromiga sabab boʻladi.",
            },
            {
                "text": "본문을 통해 알 수 있는 '조모(JOMO)'의 핵심 가치는 무엇입니까?",
                "choices": [
                    "더 많은 인맥을 쌓기 위해 가상 세계에 집중하는 것",
                    "유행하는 가전제품을 남들보다 빠르게 구매하는 것",
                    "가상 세계의 연결을 줄이고 현실의 나 자신에게 집중하는 것",
                    "타인에게 소외당하지 않기 위해 매일 SNS를 확인하는 것",
                ],
                "answer": 2,
                "explanation": "JOMO'ning asosiy mazmuni — tashqi axborot oqimini toʻsib, butunlay oʻz ichki dunyosiga va haqiqiy hayotiga eʼtibor qaratishdir.",
            },
        ],
    },
    # ── 7 ────────────────────────────────────────────────────────────────
    {
        "title":   "경제와 소비",
        "summary": "Atrof-muhit va etika qoidalariga rioya qilgan holda xarid qilish — 'Maʼnoli isteʼmol' (Conscious Consumption) trendi.",
        "order":   7,
        "body": '''<p>과거의 소비자들은 상품을 선택할 때 가격과 품질만을 가장 중요한 기준으로 <strong>삼곤 했습니다</strong>. 하지만 소비 행위가 사회에 미치는 영향력이 커지면서, 최근 젊은 소비층을 중심으로 자신의 가치관을 소비를 통해 표현하는 '가치 소비' 혹은 '착한 소비' 트렌드가 확산되는 중입니다. 이들은 단순히 물건을 <strong>구매하는 데 그치지 않고</strong>, 해당 기업이 환경 보호를 실천하는지, 노동자의 인권을 존중하는지 등 윤리적 책임을 다하고 있는지를 면밀히 <span class="cn-word" data-pos="verb" data-tr="tekshirib koʻrishadi">따져봅니다</span>.</p>
<p>예를 들어 동물을 학대하지 않는 '비건 패션' 제품을 고르거나, 제조 과정에서 탄소 배출을 최소화한 친환경 인증 마크 제품을 우선적으로 <span class="cn-word" data-pos="verb" data-tr="sotib olishadi">구입합니다</span>. 비록 일반 제품보다 가격이 다소 <span class="cn-word" data-pos="adj" data-tr="qimmat boʻlsa ham">비쌀지라도</span> 사회적 가치를 위해서라면 기꺼이 추가 비용을 <span class="cn-word" data-pos="verb" data-tr="toʻlashga tayyor">지불하겠다는</span> 입장입니다. 기업들 또한 이러한 윤리적 수용자들의 마음을 <span class="cn-word" data-pos="verb" data-tr="zabt etish uchun">사로잡기 위해</span> 친환경 경영을 도입하는 등 생존을 위한 변화를 모색하고 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "Tez-tez yoki odatda takrorlanib turadigan harakatni bildiradi: ...-ib turmoq/tushmoq.",
                "examples": ["가격과 품질만을 중요한 기준으로 삼곤 했습니다.", "주말에는 가끔 교외로 나가곤 해요."],
            },
            {
                "pattern":  "-는 데 그치다",
                "meaning":  "Harakat faqat maʼlum bir kichik natija bilan cheklanganini bildiradi: ... bilan cheklanmoq.",
                "examples": ["단순히 물건을 구매하는 데 그치지 않습니다.", "계획을 세우는 데 그치면 안 됩니다."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 설명하는 '가치 소비'의 특성으로 알맞지 않은 것은 무엇입니까?",
                "choices": [
                    "오직 가격이 가장 저렴한 제품만을 최우선으로 선택한다.",
                    "기업의 윤리 경영 여부와 인권 존중 상태를 확인한다.",
                    "가치가 있다면 조금 더 비싼 비용도 기꺼이 지불한다.",
                ],
                "answer": 0,
                "explanation": "Qiymatli isteʼmolchilar faqat arzon narxga qaramaydi, aksincha etika uchun qoʻshimcha haq toʻlashga ham tayyor ekanligi aytilgan.",
            },
            {
                "text": "소비자들의 이러한 변화에 대응하기 위한 기업들의 움직임은 무엇입니까?",
                "choices": [
                    "윤리적 가치를 배제하고 품질 경쟁에만 올인한다.",
                    "탄소 배출을 늘려 제품 생산 단가를 낮추려고 한다.",
                    "소비자들의 접근을 막기 위해 오프라인 매장을 폐쇄한다.",
                    "착한 소비 트렌드에 맞춰 친환경 경영 시스템을 도입한다.",
                ],
                "answer": 3,
                "explanation": "Oxirgi gapda korxonalar ham omon qolish uchun ekologik toza menejmentni (친환경 경영) joriy qilayotganliklari taʼkidlangan.",
            },
        ],
    },

    # ── 8 ────────────────────────────────────────────────────────────────
    {
        "title":   "역사와 문화",
        "summary": "Koreys xalqining anʼanaviy kiyimi — Xanbok (Hanbok) jozibasi va undagi estetik qadriyatlar haqida.",
        "order":   8,
        "body": '''<p>한국의 전통 의상인 한복은 직선과 곡선이 조화를 이루어 우아한 아름다움을 <span class="cn-word" data-pos="verb" data-tr="birlashtirgan, namoyish etgan">자아냅니다</span>. 한복은 몸을 꽉 조이지 않고 넉넉하게 감싸주기 때문에 활동하기에 <strong>편안할 뿐만 아니라</strong> 착용자의 체형을 자연스럽게 <span class="cn-word" data-pos="verb" data-tr="yashirib, berkitib">보완해 줍니다</span>. 또한 명절이나 결혼식 같은 특별한 날에 입는 한복은 색채의 조합을 통해 입는 사람의 신분이나 마음가짐을 표현하기도 했습니다. 과거의 백성들은 흰옷을 즐겨 입어 '백의민족'이라 불렸지만, 의례용 한복에는 오방색(다섯 가지 전통 색상)을 사용하여 우주의 조화와 복을 비는 의미를 담았습니다.</p>
<p>한복의 진정한 멋은 걸을 때 나타나는 부드러운 움직임에 있습니다. 바람이 불 때 치맛자락이 흔들리는 모습은 마치 한 폭의 동양화를 <strong>보는 듯한</strong> 깊은 여운을 줍니다. 최근에는 이러한 전통 한복의 불편한 점을 <span class="cn-word" data-pos="verb" data-tr="isloh qilib, yaxshilab">개량하여</span> 일상생활에서도 편하게 입을 수 있도록 만든 '생활 한복'이 젊은 층 사이에서 큰 인기를 끌고 있습니다. 이처럼 한복은 박물관에 고정된 유물이 아니라, 현대적인 감각과 <span class="cn-word" data-pos="verb" data-tr="birlashgan holda">접목되면서</span> 오늘날에도 여전히 살아 숨 쉬는 대중문화로 진화하고 있습니다.</p>''',
        "grammar": [
            {
                "pattern":  "-(으)ㄹ 뿐만 아니라",
                "meaning":  "Nafaqat u, balki bu ham (qoʻshimcha maʼlumot): ...gina boʻlib qolmay.",
                "examples": ["활동하기에 편안할 뿐만 아니라 체형을 보완해 줍니다.", "맛이 있을 뿐만 아니라 영양도 풍부해요."],
            },
            {
                "pattern":  "-(으)ㄴ/는 듯한",
                "meaning":  "Oʻxshatish yoki taxminni bildiradi: ...gandek, ...ga oʻxshagan.",
                "examples": ["한 폭의 동양화를 보는 듯한 여운을 줍니다.", "마치 하늘을 나는 듯한 기분이었어요."],
            },
        ],
        "questions": [
            {
                "text": "한복의 특징에 대한 설명으로 본문의 내용과 일치하는 것은 무엇입니까?",
                "choices": [
                    "몸을 타이트하게 조여서 신체 라인을 강조하는 옷이다.",
                    "직선으로만 이루어져 있어 현대인들이 입기에 매우 불편하다.",
                    "움직일 때 나타나는 부드러운 곡선의 미가 매력적이다.",
                ],
                "answer": 2,
                "explanation": "Matnning ikkinchi qismida xanbokning haqiqiy goʻzalligi harakatlangandagi yumshoq tebranish va chiziqlar uygʻunligida ekanligi aytilgan.",
            },
            {
                "text": "최근 '생활 한복'이 인기를 얻고 있는 이유로 가장 알맞은 것은 무엇입니까?",
                "choices": [
                    "전통 오방색만을 고집하여 화려하기 때문에",
                    "전통 한복의 불편함을 개선하여 일상에서 입기 좋기 때문에",
                    "가격이 일반 양복보다 훨씬 저렴하기 때문에",
                    "결혼식이나 명절에만 입도록 정해져 있기 때문에",
                ],
                "answer": 1,
                "explanation": "Matnda anʼanaviy xanbokning noqulay jihatlari isloh qilinib (개량하여), kundalik hayotda kiyishga qulay qilinganligi uchun ommalashayotgani yozilgan.",
            },
        ],
    },
    # ── 9 ────────────────────────────────────────────────────────────────
    {
        "title":   "사회적 이슈",
        "summary": "Muloqot yetishmasligi va raqamli aloqa tufayli zamonaviy oilalarda yuzaga kelayotgan uzoqlashish muammolari.",
        "order":   9,
        "body": '''<p>현대 사회의 가족 형태는 과거에 비해 외형적으로는 다양해졌으나, 내면적으로는 소통의 부재라는 심각한 위기에 <strong>직면해 있습니다</strong>. 각자 바쁜 일상 속에서 직장과 학업에 <span class="cn-word" data-pos="verb" data-tr="berilib ketganligi sababli">몰두하다 보니</span>, 한집에 살면서도 가족 구성원들이 함께 모여 대화를 나눌 시간이 절대적으로 부족해진 것입니다. 주말이나 저녁 시간조차도 각자 자신의 스마트폰 화면만을 바라보는 풍경이 일상화되면서, 정서적 유대감은 점차 <span class="cn-word" data-pos="verb" data-tr="zaiflashib, uzoqlashib">약화되어 가고</span> 있습니다. 기술의 발달이 소통의 빈도는 <strong>높였을지 몰라도</strong>, 대화의 질을 보장하지는 못한 셈입니다.</p>
<p>가족 내 소통 단절은 단순히 어색한 분위기에 그치지 않고, 구성원 간의 오해와 갈등을 심화시키는 부작용을 낳습니다. 서로의 고민이나 심리적 상태를 공유하지 못하다 보면 작은 오해조차 커다란 불신으로 번지기 쉽습니다. 진정한 가족의 기능은 단순한 공간의 공유가 아니라 정서적 안정감을 제공하는 데 있습니다. 따라서 바쁜 일상 속에서도 하루에 최소 10분씩이라도 서로의 눈을 맞추며 진심 어린 이야기를 나누려는 주체적인 노력이 절실히 요구됩니다.</p>''',
        "grammar": [
            {
                "pattern":  "-에 직면하다",
                "meaning":  "Muammo, qiyinchilik yoki vaziyatga duch kelmoq (roʻbaroʻ boʻlmoq).",
                "examples": ["소통의 부재라는 심각한 위기에 직면해 있습니다.", "어려운 상황에 직면했을 때 대화가 필요합니다."],
            },
            {
                "pattern":  "-(으)ㄹ지 모르다",
                "meaning":  "Ehtimollikni bildiradi: ... boʻlishi mumkin (lekin aniq emas), ...mi yoʻqmi bilmayman.",
                "examples": ["소통의 빈도는 높였을지 몰라도 대화의 질은 낮습니다.", "내일 비가 올지 모르겠네요."],
            },
        ],
        "questions": [
            {
                "text": "본문에서 지적한 현대 가족의 가장 큰 문제점은 무엇입니까?",
                "choices": [
                    "가족 구성원들의 과도한 스마트폰 구매 비용",
                    "함께 거주할 수 있는 주거 공간의 부족",
                    "바쁜 일상과 디지털 기기 사용으로 인한 소통의 부족",
                ],
                "answer": 2,
                "explanation": "Matnda zamonaviy oilalarning eng katta inqirozi birga yashasa-da, vaqt yetishmasligi va smartfonlar tufayli muloqotning yoʻqligi (소통의 부재) ekanligi taʼkidlangan.",
            },
            {
                "text": "글쓴이가 제시한 문제 해결 방안으로 알맞은 것을 고르십시오.",
                "choices": [
                    "가족의 정서적 안정을 위해 외식을 자주 해야 한다.",
                    "디지털 기기의 사용을 법적으로 전면 금지해야 한다.",
                    "직장과 학업을 중단하고 가족과 많은 시간을 보내야 한다.",
                    "짧은 시간이라도 매일 진심으로 대화하려는 노력을 해야 한다.",
                ],
                "answer": 3,
                "explanation": "Oxirgi gapda yechim sifatida kuniga hech boʻlmasa 10 daqiqa bir-birining koʻziga qarab chin dildan suhbat qurish kerakligi aytilgan.",
            },
        ],
    },
    # ── 10 ───────────────────────────────────────────────────────────────
    {
        "title":   "경제와 마케팅",
        "summary": "Isteʼmolchining his-tuygʻulari va xotiralariga taʼsir koʻrsatadigan 'Hissiyot marketingi' (Emotional Marketing) strategiyasi.",
        "order":   10,
        "body": '''<p>기업들이 시장에서 자사의 제품을 소비자에게 각인시키기 위해 사용하는 전략은 날로 교묘해지고 있습니다. 과거에는 제품의 객관적인 성능이나 저렴한 가격을 앞세운 이성적 마케팅이 주를 <strong>이루곤 했습니다</strong>. 성능의 차이가 직관적으로 드러나던 시대에는 그것이 효과적이었기 때문입니다. 하지만 기술의 평준화로 인해 제품 간 품질 차이가 거의 사라진 현대 시장에서는, 단순히 스펙을 강조하는 것만으로는 소비자의 지갑을 <strong>열기가 어렵습니다</strong>. 이에 따라 등장한 것이 바로 소비자의 감성을 자극하는 '감성 마케팅'입니다.</p>
<p>감성 마케팅은 제품 자체보다 그 제품을 사용할 때 느낄 수 있는 행복, 추억, 위로 등의 정서적 가치를 <span class="cn-word" data-pos="verb" data-tr="sotadi, taqdim etadi">판매합니다</span>. 예를 들어 고향의 따뜻함을 떠올리게 하는 광고나, 소장 가치를 자극하는 세련된 디자인을 통해 소비자와 브랜드 간의 심리적 유대감을 형성하는 방식입니다. 소비자들은 이성적으로 계산하기보다 감성적 끌림에 의해 구매를 결정하는 경향이 강하므로, 감성 마케팅은 브랜드 로열티를 높이고 장기적인 충성 고객을 확보하는 데 매우 탁월한 효과를 발휘합니다.</p>''',
        "grammar": [
            {
                "pattern":  "-곤 하다",
                "meaning":  "Tez-tez yoki odatda takrorlanib turadigan harakatni bildiradi: ...-ib turmoq/tushmoq.",
                "examples": ["이성적 마케팅이 주를 이루곤 했습니다.", "피곤할 때는 매운 음식을 먹곤 해요."],
            },
            {
                "pattern":  "-기(가) 어렵다",
                "meaning":  "Biror ishni qilish qiyinligini bildiradi: ...ish qiyin.",
                "examples": ["단순히 스펙만 강조해서는 소비자의 지갑을 열기가 어렵습니다.", "외국어를 혼자 공부하기는 어려워요."],
            },
        ],
        "questions": [
            {
                "text": "현대 시장에서 '감성 마케팅'이 대두된 배경은 무엇입니까?",
                "choices": [
                    "기술의 발달로 제품 간 품질 차이가 미미해졌기 때문에",
                    "소비자들이 성능보다 가격을 가장 중요하게 생각하기 때문에",
                    "이성적 마케팅의 비용이 감성 마케팅보다 비싸기 때문에",
                ],
                "answer": 0,
                "explanation": "Matnda yozilishicha, texnologiya tenglashib, mahsulotlar sifati oʻrtasidagi farq deyarli yoʻqolgani (품질 차이가 거의 사라진) sababli hissiyot marketingi paydo boʻlgan.",
            },
            {
                "text": "본문의 내용과 일치하는 것을 고르십시오.",
                "choices": [
                    "감성 마케팅은 단기적인 매출 상승에만 효과가 있다.",
                    "과거에는 제품의 스펙보다는 정서적 가치를 주로 홍보했다.",
                    "소비자들은 완벽히 이성적인 계산을 통해서만 소비를 결정한다.",
                    "감성 마케팅은 브랜드와 소비자 사이에 심리적 유대를 만든다.",
                ],
                "answer": 3,
                "explanation": "Ikkinchi xatboshida hissiyot marketingi brend va isteʼmolchi oʻrtasida ruhiy yaqinlik/baqlanish (심리적 유대감) hosil qilishi aniq keltirilgan.",
            },
        ],
    },
    # ── 11 ───────────────────────────────────────────────────────────────
    {
        "title":   "생태학과 환경",
        "summary": "Asalari (Honeybee) populyatsiyasining kamayishi va buning natijasida global ekotizim va oziq-ovqat xavfsizligiga tahdidlar.",
        "order":   11,
        "body": '''<p>최근 전 세계적으로 아살라리(꿀벌)의 개체 수가 급격히 감소하면서 지구 생태계에 비상이 <strong>걸렸습니다</strong>. 많은 사람들이 꿀벌을 단순히 인간에게 꿀을 제공하는 곤충으로만 생각하지만, 사실 꿀벌은 지구상에 존재하는 식물의 수분을 돕는 결정적인 역할을 담당하고 있습니다. 우리가 소비하는 주요 농작물의 상당수가 꿀벌의 매개를 통해 열매를 <span class="cn-word" data-pos="verb" data-tr="tugadi, hosil qiladi">맺기 때문입니다</span>. 만약 꿀벌이 지구상에서 완전히 사라진다면, 식물이 번식하지 못해 농작물 생산량이 급감하고 이는 결국 인류의 극심한 식량 위기로 <strong>이어질 수밖에 없습니다</strong>.</p>
<p>꿀벌 실종 사건의 주된 원인으로는 무분별한 살충제 사용, 기후 변화로 인한 개화 시기의 교란, 그리고 서식지 파괴 등이 지목되고 있습니다. 꿀벌의 위기는 단지 하나의 곤충이 사라지는 문제가 아니라, 생태계 사슬 전체가 무너질 수 있음을 경고하는 강력한 신호입니다. 생태계의 건전성을 유지하고 인류의 식량 안보를 지키기 위해서는 친환경 농업으로의 전환과 탄소 배출 감축을 위한 범지구적 공조가 시급히 이행되어야 할 것입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-이/가 걸리다",
                "meaning":  "Maʼlum bir holat, kasallik yoki cheklovga tushishni bildiradi (masalan, favqulodda holat eʼlon qilinishi).",
                "examples": ["지구 생태계에 비상이 걸렸습니다.", "감기에 걸려서 학교에 못 갔어요."],
            },
            {
                "pattern":  "-(으)ㄹ 수밖에 없다",
                "meaning":  "Boshqa chora yoki iloj yoʻqligini bildiradi: ...ishga majbur, ...dan boʻlak iloj yoʻq.",
                "examples": ["인류의 극심한 식량 위기로 이어질 수밖에 없습니다.", "비가 오니 집에 있을 수밖에 없네요."],
            },
        ],
        "questions": [
            {
                "text": "꿀벌의 멸종이 인류에게 미치는 가장 치명적인 영향은 무엇입니까?",
                "choices": [
                    "시중에서 천연 꿀을 더 이상 구매할 수 없게 된다.",
                    "농작물의 수분이 이루어지지 않아 심각한 식량 위기가 도래한다.",
                    "살충제의 가격이 전 세계적으로 폭등하게 된다.",
                ],
                "answer": 1,
                "explanation": "Matnda aytilishicha, asalarilar oʻsimliklarning changlanishiga yordam beradi, agar ular yoʻqolsa hosildorlik tushib, insoniyat oziq-ovqat inqiroziga (식량 위기) duchor boʻladi.",
            },
            {
                "text": "본문의 내용과 일치하지 않는 것을 고르십시오.",
                "choices": [
                    "친환경 농업으로의 전환은 꿀벌 보호를 위한 대안이 될 수 있다.",
                    "꿀벌의 감소는 살충제 사용과 기후 변화 등 복합적 원인 때문이다.",
                    "꿀벌의 소멸은 다른 동식물 생태계에는 아무런 영향을 주지 않는다.",
                    "꿀벌은 인간에게 꿀을 주는 것 이상의 생태적 가치를 지닌다.",
                ],
                "answer": 2,
                "explanation": "Asalarilarning kamayishi butun ekotizim zanjirining (생태계 사슬 전체) buzilishiga olib kelishi keltirilgan, shuning uchun boshqa jonzotlarga taʼsir qilmaydi degan variant notoʻgʻri.",
            },
        ],
    },
    # ── 12 ───────────────────────────────────────────────────────────────
    {
        "title":   "인류학",
        "summary": "Raqamli texnologiyalar asrida yozish (shrift) madaniyatining oʻzgarishi va qoʻlyozmaning miya rivojlanishidagi ahamiyati.",
        "order":   12,
        "body": '''<p>컴퓨터와 스마트폰의 보급으로 인해 손으로 직접 글씨를 쓰는 '자필' 문화가 점차 사라지고 키보드를 두드리는 '타이핑'이 주류로 <strong>자리 잡았습니다</strong>. 빠르고 편리하게 텍스트를 생산하고 수정할 수 있다는 점에서 디지털 타이핑은 업무 효율성을 극대화하는 데 크게 기여했습니다. 그러나 편리함의 이면에는 인간의 인지 능력 저하라는 우려가 숨어 있습니다. 뇌과학자들의 연구에 따르면, 손으로 직접 글씨를 쓰는 행위는 키보드를 누를 때보다 뇌의 운동 피질과 기억을 담당하는 영역을 훨씬 더 강하게 <strong>자극한다고 합니다</strong>.</p>
<p>손가락을 세밀하게 움직여 글자를 정성껏 적어 내려가는 과정은 정보가 뇌에 장기 기억으로 저장되도록 <span class="cn-word" data-pos="verb" data-tr="yordam beradi">돕습니다</span>. 반면 키보드 입력은 단순히 위치적 자극에 불과하여 정보의 장기적인 습득과 깊이 있는 사유를 방해하는 경향이 있습니다. 디지털 시대일수록 아이들의 두뇌 발달과 성인들의 인지 기능 유지를 위해 아날로그식 필기 습관을 의도적으로 유지하려는 노력이 필요합니다. 편리함만을 쫓기보다는 인간 고유의 사고력을 지키기 위한 균형 잡힌 태도가 요구되는 시점입니다.</p>''',
        "grammar": [
            {
                "pattern":  "-로 자리 잡다",
                "meaning":  "Maʼlum bir pozitsiya yoki maqomga ega boʻlish, joylashmoq: ... sifatida shakllanmoq.",
                "examples": ["'타이핑'이 주류로 자리 잡았습니다.", "K-pop이 세계적인 문화로 자리 잡았어요."],
            },
            {
                "pattern":  "-다고 하다",
                "meaning":  "Koʻchirma gap (boshqalardan eshitilgan gapni yetkazish): ... deb aytishadi/taʼkidlashadi.",
                "examples": ["영역을 훨씬 더 강하게 자극한다고 합니다.", "한국의 가을 날씨가 아주 아름답다고 해요."],
            },
        ],
        "questions": [
            {
                "text": "손으로 글씨를 쓰는 행위(자필)가 가진 장점은 무엇입니까?",
                "choices": [
                    "디지털 타이핑보다 빠른 속도로 텍스트를 수정할 수 있다.",
                    "뇌를 강하게 자극하여 정보를 장기 기억으로 저장하도록 돕는다.",
                    "손가락 근육의 피로도를 획기적으로 낮춰 준다.",
                ],
                "answer": 1,
                "explanation": "Matnning birinchi va ikkinchi qismida qoʻlda yozish miyani koʻproq stimulyatsiya qilishi va maʼlumotlarni uzoq muddatli xotirada (장기 기억) saqlashga koʻmaklashishi aytilgan.",
            },
            {
                "text": "본문의 내용과 가장 일치하는 것을 고르십시오.",
                "choices": [
                    "키보드를 활용한 입력 방식은 인지 능력을 발달시키는 핵심 요소이다.",
                    "디지털 타이핑은 자필 필기에 비해 뇌 자극 효과가 훨씬 월등하다.",
                    "인간의 깊이 있는 사유 능력 유지를 위해 자필 습관을 유지할 필요가 있다.",
                    "성인의 뇌 건강을 위해서는 아날로그 필기를 전면 중단해야 한다.",
                ],
                "answer": 2,
                "explanation": "Muallif insonning fikrlash doirasi va intellektual salohiyatini muhofaza qilish uchun analog kiyinish/yozish odatlarini ataylab saqlab qolish kerakligini tavsiya etmoqda.",
            },
        ],
    },
]