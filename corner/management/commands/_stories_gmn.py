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
]