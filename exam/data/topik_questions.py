# ──────────────────────────────────────────────────────────────────
#  TOPIK II 읽기 (Reading) + 쓰기 (Writing) + 듣기 (Listening)
#  Edit this file, then run:
#      python manage.py load_topik
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II - 제83회',
    'language': 'korean',       # korean / english / japanese / chinese
    'exam_number': 83,
    'listening_minutes': 60,
    'reading_minutes': 70,
    'writing_minutes': 50,
    'allow_audio_replay': True,
    'allow_audio_pause': True,
    'is_published': False,
}

# ──────────────────────────────────────────────────────────────────
#  FORMAT FOR EACH QUESTION:
#
#  {
#    'section':       'reading' | 'listening' | 'writing',
#    'number':        int,            ← question number
#    'passage':       str,            ← passage text above the question ('' if none)
#    'question_text': str,            ← the actual question
#    'is_writing':    bool,           ← True for open-ended writing questions
#    'correct':       str,            ← exact text of the correct choice ('' for writing)
#    'choices':       [str, str, ...] ← 4 choices for MCQ, [] for writing
#  }
# ──────────────────────────────────────────────────────────────────

QUESTIONS = [

    # ── READING (읽기) ────────────────────────────────────────────

    {
        'section': 'reading',
        'number': 1,
        'passage': '',
        'question_text': '다음 ( )에 들어갈 말로 가장 알맞은 것을 고르십시오.\n\n친구가 생일 선물을 보내 줘서 정말 ( ).',
        'is_writing': False,
        'correct': '기뻤습니다',
        'choices': ['기뻤습니다', '슬펐습니다', '힘들었습니다', '무서웠습니다'],
    },

    {
        'section': 'reading',
        'number': 2,
        'passage': '',
        'question_text': '다음 ( )에 들어갈 말로 가장 알맞은 것을 고르십시오.\n\n배가 고프면 ( ) 드세요.',
        'is_writing': False,
        'correct': '뭐든지',
        'choices': ['먹고 싶어서', '뭐든지', '조금도', '아무것도'],
    },

    {
        'section': 'reading',
        'number': 3,
        'passage': (
            '저는 매일 아침 공원에서 운동을 합니다. 운동을 하면 몸이 건강해지고 기분도 좋아집니다. '
            '그래서 날씨가 나쁠 때도 빠지지 않고 운동합니다.'
        ),
        'question_text': '이 글의 내용과 같은 것을 고르십시오.',
        'is_writing': False,
        'correct': '저는 매일 아침 운동을 합니다.',
        'choices': [
            '저는 가끔 공원에서 운동합니다.',
            '날씨가 나쁘면 운동을 쉽니다.',
            '저는 매일 아침 운동을 합니다.',
            '운동을 하면 배가 고파집니다.',
        ],
    },

    {
        'section': 'reading',
        'number': 4,
        'passage': (
            '한국에서는 설날에 가족이 모여 떡국을 먹습니다. 떡국을 먹으면 나이를 한 살 더 먹는다고 생각합니다. '
            '또 어른들께 세배를 드리고 덕담을 나눕니다.'
        ),
        'question_text': '이 글의 중심 내용을 고르십시오.',
        'is_writing': False,
        'correct': '한국의 설날 풍습',
        'choices': ['떡국을 만드는 방법', '한국의 설날 풍습', '가족과 함께하는 식사', '세배 드리는 방법'],
    },

    {
        'section': 'reading',
        'number': 5,
        'passage': (
            '최근 도시에서 텃밭 가꾸기가 인기를 끌고 있습니다. 바쁜 도시인들이 주말에 땅을 일구고 채소를 키우면서 '
            '스트레스를 해소합니다. 직접 키운 채소로 요리를 해 먹는 즐거움도 크다고 합니다.'
        ),
        'question_text': '이 글의 주제로 가장 알맞은 것을 고르십시오.',
        'is_writing': False,
        'correct': '도시인들의 텃밭 가꾸기 인기',
        'choices': [
            '도시 농업의 문제점',
            '채소 요리 레시피',
            '도시인들의 텃밭 가꾸기 인기',
            '주말 농장 운영 방법',
        ],
    },

    {
        'section': 'reading',
        'number': 6,
        'passage': (
            '이 제품은 사용 전에 반드시 설명서를 읽어 주십시오. '
            '어린이의 손이 닿지 않는 곳에 보관하십시오. '
            '직사광선을 피하고 서늘한 곳에 두십시오.'
        ),
        'question_text': '이 글의 내용과 다른 것을 고르십시오.',
        'is_writing': False,
        'correct': '햇빛이 잘 드는 곳에 보관해야 합니다.',
        'choices': [
            '사용 전에 설명서를 읽어야 합니다.',
            '햇빛이 잘 드는 곳에 보관해야 합니다.',
            '어린이가 닿지 않도록 보관해야 합니다.',
            '서늘한 장소에 두어야 합니다.',
        ],
    },

    {
        'section': 'reading',
        'number': 7,
        'passage': (
            '언어는 단순한 의사소통 도구가 아닙니다. 언어 속에는 그 민족의 역사와 문화가 담겨 있습니다. '
            '따라서 언어를 배운다는 것은 그 나라의 문화를 이해하는 길이기도 합니다.'
        ),
        'question_text': '이 글에서 필자가 말하고자 하는 것은 무엇입니까?',
        'is_writing': False,
        'correct': '언어는 문화를 담고 있다.',
        'choices': [
            '언어 학습은 어렵다.',
            '언어는 문화를 담고 있다.',
            '의사소통이 중요하다.',
            '역사를 공부해야 한다.',
        ],
    },

    {
        'section': 'reading',
        'number': 8,
        'passage': (
            '( ) 운동은 건강에 좋지 않을 수 있습니다. 준비 운동 없이 갑자기 격렬한 운동을 하면 '
            '근육에 무리가 가고 부상을 입을 수 있습니다. 따라서 운동 전에는 충분히 몸을 풀어야 합니다.'
        ),
        'question_text': '( )에 들어갈 말로 가장 알맞은 것을 고르십시오.',
        'is_writing': False,
        'correct': '준비 없이 하는',
        'choices': ['가벼운', '규칙적인', '준비 없이 하는', '매일 하는'],
    },

    {
        'section': 'reading',
        'number': 9,
        'passage': (
            '다음은 도서관 이용 안내입니다.\n\n'
            '∙ 이용 시간: 월~금 09:00~21:00, 토~일 09:00~18:00\n'
            '∙ 대출 기간: 2주 (1회 연장 가능)\n'
            '∙ 대출 권수: 1인당 최대 5권\n'
            '∙ 반납이 늦어지면 연체료가 발생합니다.'
        ),
        'question_text': '위 안내문의 내용과 같은 것을 고르십시오.',
        'is_writing': False,
        'correct': '대출 기간을 한 번 연장할 수 있습니다.',
        'choices': [
            '주말에는 도서관을 이용할 수 없습니다.',
            '한 번에 10권까지 빌릴 수 있습니다.',
            '대출 기간을 한 번 연장할 수 있습니다.',
            '반납이 늦어도 추가 요금이 없습니다.',
        ],
    },

    {
        'section': 'reading',
        'number': 10,
        'passage': (
            '현대인들은 스마트폰을 과도하게 사용하는 경향이 있습니다. 잠자리에 들기 전까지 화면을 들여다보거나 '
            '식사 중에도 손에서 놓지 못합니다. 이로 인해 수면 장애와 소화 불량 등 건강 문제가 증가하고 있습니다. '
            '전문가들은 하루에 일정 시간 스마트폰을 사용하지 않는 \'디지털 디톡스\'를 권장합니다.'
        ),
        'question_text': '이 글의 내용과 같은 것을 고르십시오.',
        'is_writing': False,
        'correct': '스마트폰 과사용은 수면과 소화 문제를 일으킬 수 있습니다.',
        'choices': [
            '스마트폰 사용은 건강에 아무 영향이 없습니다.',
            '전문가들은 스마트폰 사용을 금지하고 있습니다.',
            '디지털 디톡스는 스마트폰을 아예 사용하지 않는 것입니다.',
            '스마트폰 과사용은 수면과 소화 문제를 일으킬 수 있습니다.',
        ],
    },

    # ── WRITING (쓰기) ────────────────────────────────────────────

    {
        'section': 'writing',
        'number': 51,
        'passage': '',
        'question_text': (
            '다음을 읽고 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰십시오.\n\n'
            '사람들은 왜 운동을 할까요? 첫째, 건강을 유지하기 위해서입니다. ( ㉠ ). '
            '둘째, 스트레스를 풀기 위해서입니다. ( ㉡ ).'
        ),
        'is_writing': True,
        'correct': '',
        'choices': [],
    },

    {
        'section': 'writing',
        'number': 52,
        'passage': '',
        'question_text': (
            '다음 그래프를 보고 \'한국인의 독서량 변화\'에 대한 글을 200~300자로 쓰십시오.'
        ),
        'is_writing': True,
        'correct': '',
        'choices': [],
    },

    {
        'section': 'writing',
        'number': 53,
        'passage': '',
        'question_text': (
            '다음을 참고하여 \'현대 사회에서 독서의 중요성\'에 대한 글을 600~700자로 쓰십시오.\n\n'
            '※ 아래의 내용을 모두 포함하여 쓰십시오.\n'
            '∙ 독서가 줄어드는 이유\n'
            '∙ 독서의 장점\n'
            '∙ 독서 습관을 기르기 위한 방법'
        ),
        'is_writing': True,
        'correct': '',
        'choices': [],
    },

    # ── LISTENING (듣기) ──────────────────────────────────────────

    {
        'section': 'listening',
        'number': 1,
        'passage': '[1~2] 다음을 듣고 물음에 답하십시오.',
        'question_text': '여자가 무엇에 대해 이야기하고 있습니까?',
        'is_writing': False,
        'correct': '주말 계획',
        'choices': ['날씨 변화', '주말 계획', '교통 상황', '음식 주문'],
    },

    {
        'section': 'listening',
        'number': 2,
        'passage': '',
        'question_text': '들은 내용과 같은 것을 고르십시오.',
        'is_writing': False,
        'correct': '두 사람은 같이 여행을 갈 예정입니다.',
        'choices': [
            '여자는 혼자 여행을 갑니다.',
            '남자는 이미 계획을 세웠습니다.',
            '두 사람은 같이 여행을 갈 예정입니다.',
            '여행지는 아직 정하지 않았습니다.',
        ],
    },

]
