# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 2회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock2_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 2회',
    'language': 'korean',
    'exam_number': 102,
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
         '<b>제목: 지갑을 찾습니다</b><br><br>'
         '어제 오후 세 시쯤 학생 회관 식당에서 갈색 지갑을 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '지갑 안에는 학생증과 가족사진이 들어 있습니다.<br>'
         '저에게는 아주 소중한 물건입니다.<br>'
         '지갑을 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;) 아래 번호로 꼭 연락해 주시기 바랍니다.<br>'
         '감사의 선물을 드리겠습니다.<br>'
         '연락처: 010-1234-5678'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '운동을 하기 전에는 반드시 준비운동을 해야 한다. 준비운동 없이 갑자기 운동을 시작하면 '
         '근육이 놀라서 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 준비운동은 몸의 온도를 천천히 '
         '올려서 굳어 있던 근육을 부드럽게 만들어 준다. 그러므로 운동의 효과를 높이고 부상을 '
         '예방하고 싶다면 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'1인 가구 비율의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>1인 가구 비율의 변화</b> <small>(조사 기관: 인주사회연구소)</small><br><br>'
         '· 2015년: 27% &nbsp;→&nbsp; 2020년: 31% &nbsp;→&nbsp; 2025년: 36%<br>'
         '<b>· 10년 동안 꾸준히 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 결혼을 필수로 여기지 않는 사람 증가<br>'
         '② 혼자 사는 노인 인구 증가<br><br>'
         '<b>전망</b>: 2035년에는 40%를 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '우리는 학교와 직장 등 삶의 곳곳에서 다른 사람과 경쟁하며 살아간다. 경쟁은 개인과 사회를 '
         '발전시키는 힘이 되기도 하지만, 지나친 경쟁은 여러 가지 문제를 낳기도 한다. 아래의 내용을 '
         '중심으로 \'경쟁의 영향\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 경쟁은 우리에게 어떤 긍정적인 영향을 주는가?<br>'
         '· 지나친 경쟁은 어떤 문제를 가져오는가?<br>'
         '· 바람직한 경쟁의 자세는 무엇인가?'
         '</div>'
     )},
]
