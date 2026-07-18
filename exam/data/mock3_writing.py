# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 3회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock3_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 3회',
    'language': 'korean',
    'exam_number': 103,
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
         '<b>제목: 집들이에 초대합니다</b><br><br>'
         '수미 씨, 안녕하세요. 민수입니다.<br>'
         '지난달에 새집으로 이사를 해서 이번 주 토요일 저녁에 집들이를 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '수미 씨가 꼭 와 주셨으면 좋겠습니다.<br>'
         '음식은 제가 준비할 테니까 그냥 오시면 됩니다.<br>'
         '올 수 있는지 목요일까지 답장으로 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '그럼 연락 기다리겠습니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '우리 몸의 칠십 퍼센트는 물로 이루어져 있다. 그래서 몸속에 물이 부족하면 쉽게 피곤해지고 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 그런데 목이 마를 때는 이미 몸에 물이 많이 부족해진 '
         '상태라고 한다. 그러므로 건강을 지키고 싶다면 목이 마르지 않더라도 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'국내 외국인 유학생 수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 외국인 유학생 수의 변화</b> <small>(조사 기관: 인주교육연구원)</small><br><br>'
         '· 2015년: 9만 명 &nbsp;→&nbsp; 2020년: 15만 명 &nbsp;→&nbsp; 2025년: 20만 명<br>'
         '<b>· 10년 동안 2배 이상 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 한국 문화의 인기로 한국에 대한 관심 증가<br>'
         '② 대학들의 유학생 유치 노력<br><br>'
         '<b>전망</b>: 2030년에는 25만 명에 이를 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람들은 대화를 할 때 말하기에는 신경을 쓰지만 듣기는 소홀히 하는 경우가 많다. 그러나 '
         '상대의 말을 잘 듣는 것, 즉 \'경청\'은 원활한 의사소통의 기본이며 좋은 인간관계를 만드는 '
         '힘이 된다. 아래의 내용을 중심으로 \'경청의 중요성\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 경청은 왜 중요한가?<br>'
         '· 상대의 말을 잘 듣지 않으면 어떤 문제가 생기는가?<br>'
         '· 경청을 잘하기 위해서는 어떤 노력이 필요한가?'
         '</div>'
     )},
]
