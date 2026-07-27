# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 9회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock9_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 9회',
    'language': 'korean',
    'exam_number': 109,
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
         '<b>제목: 이번 달 모임 날짜가 바뀌었습니다</b><br><br>'
         '안녕하세요. 한국어 말하기 모임 회원 여러분.<br>'
         '원래 이번 주 토요일에 모이기로 했는데 그날 회의실을 쓸 수 없게 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '그래서 이번 모임을 다음 주 토요일 같은 시간으로 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '장소는 그대로이니 참고해 주시기 바랍니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '사람들은 흔히 여럿이 함께 있어야 외롭지 않다고 생각한다. 그러나 하루 종일 사람들 사이에 있으면 '
         '마음이 오히려 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 자기 생각을 정리할 시간이 없기 '
         '때문이다. 그러므로 아무리 바쁘더라도 하루에 잠깐은 혼자 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'국내 전기 자동차 등록 대수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 전기 자동차 등록 대수</b> <small>(조사 기관: 한국교통연구원)</small><br><br>'
         '· 2015년: 약 6천 대 &nbsp;→&nbsp; 2020년: 약 14만 대 &nbsp;→&nbsp; 2025년: 약 90만 대<br>'
         '<b>· 10년 사이 150배 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 정부의 구매 지원금 확대<br>'
         '② 충전 시설의 증가와 환경 인식의 변화<br><br>'
         '<b>전망</b>: 2030년에는 200만 대를 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '세계가 하나로 이어지면서 어느 나라를 가도 비슷한 옷을 입고 비슷한 음식을 먹는다. '
         '그래서 각 나라의 전통문화가 점점 사라지고 있다는 걱정의 목소리가 나온다. 반면에 '
         '오래된 것은 자연스럽게 사라지는 것이라고 보는 사람도 있다. 아래의 내용을 중심으로 '
         '\'전통문화를 지키는 일\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 전통문화는 우리에게 어떤 의미가 있는가?<br>'
         '· 전통문화가 사라지는 이유는 무엇인가?<br>'
         '· 전통문화를 지키려면 어떤 노력이 필요한가?'
         '</div>'
     )},
]
