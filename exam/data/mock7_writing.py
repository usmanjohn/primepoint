# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 7회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock7_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 7회',
    'language': 'korean',
    'exam_number': 107,
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
         '<b>받는 사람: park@primepoint.uz</b><br>'
         '<b>제목: 이번 주 수업에 참석하지 못합니다</b><br><br>'
         '안녕하세요, 선생님. 한국어 중급반 학생 아프소나입니다.<br>'
         '이번 주 목요일에 갑자기 병원에 가게 되어서 수업에 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '수업을 빠지면 진도를 따라가기 어려울 것 같습니다.<br>'
         '그래서 죄송하지만 그날 배운 자료를 저에게 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;)?<br>'
         '다음 주에는 꼭 참석하겠습니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '사람의 기억은 우리가 생각하는 것보다 오래가지 않는다. 그래서 아무리 좋은 생각이 떠올라도 '
         '적어 두지 않으면 얼마 지나지 않아 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 게다가 메모는 '
         '기억을 대신해 줄 뿐만 아니라 머릿속을 정리해 주는 역할도 한다. 그러므로 중요한 일이 생각났을 '
         '때는 미루지 말고 그 자리에서 바로 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'중고 거래 이용자 수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 중고 거래 이용자 수</b> <small>(조사 기관: 한국생활경제연구원)</small><br><br>'
         '· 2015년: 약 500만 명 &nbsp;→&nbsp; 2020년: 약 1,200만 명 &nbsp;→&nbsp; 2025년: 약 2,300만 명<br>'
         '<b>· 10년 사이 약 4.6배 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 스마트폰 거래 앱의 확산<br>'
         '② 환경을 생각하는 소비 인식의 확산<br><br>'
         '<b>전망</b>: 2030년에는 3,000만 명을 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람은 혼자 살 수 없고 늘 다른 사람과 함께 살아간다. 그래서 상대의 입장을 헤아리는 배려가 '
         '필요하다. 그러나 바쁘고 경쟁이 심한 오늘날에는 남을 돌아볼 여유가 없다고 말하는 사람도 많다. '
         '아래의 내용을 중심으로 \'배려하는 사회\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 배려는 우리 사회에 왜 필요한가?<br>'
         '· 배려가 부족하면 어떤 문제가 생기는가?<br>'
         '· 배려하는 사회를 만들기 위해 무엇이 필요한가?'
         '</div>'
     )},
]
