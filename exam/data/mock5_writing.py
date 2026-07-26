# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 5회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock5_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 5회',
    'language': 'korean',
    'exam_number': 105,
    'listening_minutes': 60,
    'reading_minutes': 70,
    'writing_minutes': 50,
    'allow_audio_replay': True,
    'allow_audio_pause': True,
    'is_published': True,
}

S = 'writing'

_BOX = ('background:rgba(56,189,248,0.06);border:1px solid var(--border);'
        'border-radius:10px;padding:0.9rem 1.1rem;line-height:1.9;margin:0.5rem 0;')

PASSAGES = [
    {'section': S, 'from': 51, 'to': 52,
     'text': '<b>※ [51~52] 다음 글의 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰십시오.</b> (각 10점)'},
]

QUESTIONS = [
    {'section': S, 'number': 51, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '<b>받는 사람: kimsem@primepoint.uz</b><br>'
         '<b>제목: 책을 빌리고 싶습니다</b><br><br>'
         '안녕하세요, 선생님. 저는 한국어 중급반 학생 자수르입니다.<br>'
         '지난 수업 시간에 선생님께서 소개해 주신 책을 도서관에서 찾아봤는데 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '혹시 선생님께서 그 책을 가지고 계시면 저에게 일주일만 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;)?<br>'
         '다 읽은 후에 다음 주 수업 시간에 꼭 돌려드리겠습니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '물은 우리 몸의 약 70퍼센트를 차지한다. 그래서 물을 충분히 마시지 않으면 몸에 여러 가지 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 그런데 목이 마르다고 해서 한 번에 많은 양의 물을 '
         '마시는 것은 오히려 몸에 좋지 않다. 그러므로 물은 한꺼번에 마시지 말고 하루 동안 조금씩 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'국내 반려동물 양육 가구 수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 반려동물 양육 가구 수</b> <small>(조사 기관: 한국사회조사연구원)</small><br><br>'
         '· 2015년: 약 220만 가구 &nbsp;→&nbsp; 2020년: 약 380만 가구 &nbsp;→&nbsp; 2025년: 약 600만 가구<br>'
         '<b>· 10년 사이 약 2.7배 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 1인 가구와 노인 가구의 증가<br>'
         '② 반려동물을 가족으로 여기는 인식의 변화<br><br>'
         '<b>전망</b>: 2030년에는 700만 가구를 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람은 누구나 일을 하며 살아간다. 어떤 사람은 돈을 가장 중요하게 생각하고, 어떤 사람은 '
         '자신이 좋아하는 일인지를 먼저 본다. 직업은 한 사람의 생활뿐만 아니라 인생 전체에 큰 영향을 '
         '준다. 아래의 내용을 중심으로 \'직업을 선택할 때 중요한 것\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 직업은 우리의 삶에서 어떤 의미를 가지는가?<br>'
         '· 직업을 선택할 때 사람들이 중요하게 생각하는 것은 무엇인가?<br>'
         '· 좋은 직업을 선택하기 위해 어떤 준비가 필요한가?'
         '</div>'
     )},
]
