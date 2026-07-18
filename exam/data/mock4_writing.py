# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 4회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock4_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 4회',
    'language': 'korean',
    'exam_number': 104,
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
         '<b>제목: 추천서 부탁드립니다</b><br><br>'
         '김 교수님, 안녕하십니까? 4학년 이수미입니다.<br>'
         '제가 이번에 한국 대학원에 지원하려고 하는데 지원 서류에 교수님의 추천서가 필요합니다.<br>'
         '바쁘시겠지만 저를 위해 추천서를 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;)?<br>'
         '서류는 다음 달 10일까지 내야 합니다.<br>'
         '가능하시다면 제가 연구실로 찾아가서 자세히 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '답장 기다리겠습니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '목표를 세울 때는 구체적으로 세우는 것이 좋다. \'운동을 열심히 하겠다\'처럼 목표가 '
         '막연하면 무엇을 해야 할지 몰라서 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 반면에 '
         '\'매일 아침 삼십 분씩 걷겠다\'처럼 목표가 구체적이면 해야 할 일이 분명해서 실천하기 '
         '쉽다. 그러므로 목표를 이루고 싶다면 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'성인의 연간 독서량 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>성인의 연간 독서량 변화</b> <small>(조사 기관: 인주독서문화재단, 대상: 성인 5,000명)</small><br><br>'
         '· 2015년: 12권 &nbsp;→&nbsp; 2020년: 9권 &nbsp;→&nbsp; 2025년: 6권<br>'
         '<b>· 10년 사이 절반으로 감소</b><br><br>'
         '<b>감소 원인</b><br>'
         '① 스마트폰 사용 시간 증가<br>'
         '② 책 이외의 여가 활동 다양화<br><br>'
         '<b>전망</b>: 감소가 계속되면 2030년에는 4권까지 줄어들 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람은 누구나 행복한 삶을 원한다. 어떤 사람들은 돈이나 성공 같은 물질적 조건이 행복을 '
         '결정한다고 생각하지만, 물질적으로 풍요로워도 행복하지 않은 사람들이 있다. 아래의 내용을 '
         '중심으로 \'행복한 삶의 조건\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 사람들이 생각하는 행복의 조건에는 어떤 것들이 있는가?<br>'
         '· 물질적 조건만으로 행복해질 수 없는 이유는 무엇인가?<br>'
         '· 행복한 삶을 살기 위해서는 어떤 노력이 필요한가?'
         '</div>'
     )},
]
