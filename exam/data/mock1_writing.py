# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 1회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock1_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 1회',
    'language': 'korean',
    'exam_number': 101,
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
         '<b>제목: 한국어 말하기 모임 회원을 모집합니다</b><br><br>'
         '안녕하세요. 저희는 매주 토요일에 모여서 한국어로 이야기를 나누는 모임입니다.<br>'
         '이번 달에 새로운 회원을 모집하려고 합니다.<br>'
         '한국어에 관심이 있는 분이라면 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '모임에 참여하고 싶은 분은 이번 주 금요일까지 저에게 문자로 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '그럼 연락을 기다리겠습니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '사람들은 보통 실수를 하면 그것을 빨리 잊어버리려고 한다. '
         '그러나 실수를 그냥 잊어버리면 다음에 같은 실수를 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). '
         '반대로 실수의 원인을 찾아서 기록해 두면 같은 상황에서 실수를 피할 수 있다. '
         '그러므로 실수는 잊어버려야 할 부끄러운 일이 아니라 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'청소년의 하루 평균 스마트폰 사용 시간\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>청소년의 하루 평균 스마트폰 사용 시간</b> <small>(조사 기관: 한국청소년연구소, 대상: 중·고등학생 1,000명)</small><br><br>'
         '· 2015년: 2시간 30분 &nbsp;→&nbsp; 2020년: 3시간 40분 &nbsp;→&nbsp; 2025년: 5시간 10분<br>'
         '<b>· 10년 사이 2배 이상 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 동영상 시청 시간 증가<br>'
         '② 스마트폰으로 공부하는 학생 증가<br><br>'
         '<b>전망</b>: 2030년에는 6시간을 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '칭찬은 사람의 마음을 움직이는 큰 힘을 가지고 있다. 칭찬을 들으면 자신감이 생기고 '
         '더 잘하고 싶은 마음이 든다. 그러나 지나친 칭찬이나 잘못된 칭찬은 오히려 나쁜 결과를 '
         '가져오기도 한다. 아래의 내용을 중심으로 \'칭찬의 효과\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 칭찬은 우리에게 어떤 긍정적인 영향을 주는가?<br>'
         '· 잘못된 칭찬은 어떤 문제를 일으킬 수 있는가?<br>'
         '· 올바르게 칭찬하는 방법은 무엇인가?'
         '</div>'
     )},
]
