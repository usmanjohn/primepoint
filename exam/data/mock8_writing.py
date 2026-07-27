# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 8회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock8_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 8회',
    'language': 'korean',
    'exam_number': 108,
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
         '<b>제목: 잠시 시끄러울 수 있습니다</b><br><br>'
         '안녕하세요. 502호에 새로 이사 온 사람입니다.<br>'
         '이번 주 토요일 오전에 집을 고치는 공사를 하게 되었습니다.<br>'
         '그래서 그날 오전에는 조금 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '공사는 열두 시 전에 끝날 예정이니 하루만 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '불편을 드려 죄송합니다. 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '사람들은 겨울에 추위 때문에 창문을 잘 열지 않는다. 그런데 창문을 오래 닫아 두면 방 안의 공기가 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 실제로 실내의 공기가 바깥보다 더 나쁜 경우도 적지 '
         '않다. 그러므로 아무리 추운 날이라도 하루에 몇 번은 창문을 열어 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'해외여행객 수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 해외여행객 수</b> <small>(조사 기관: 한국관광연구원)</small><br><br>'
         '· 2015년: 약 1,900만 명 &nbsp;→&nbsp; 2020년: 약 400만 명 &nbsp;→&nbsp; 2025년: 약 2,800만 명<br>'
         '<b>· 2020년에 크게 줄었다가 2025년에 역대 최고를 기록</b><br><br>'
         '<b>최근 증가 원인</b><br>'
         '① 항공 노선의 확대와 항공권 가격 하락<br>'
         '② 짧게 다녀오는 여행 문화의 확산<br><br>'
         '<b>전망</b>: 2030년에는 3,500만 명을 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '오늘날에는 원하는 정보를 몇 초 만에 찾을 수 있다. 그래서 굳이 책을 읽을 필요가 없다고 '
         '말하는 사람도 있다. 그러나 여전히 많은 사람들이 책 읽기를 중요하게 여긴다. '
         '아래의 내용을 중심으로 \'독서가 우리에게 주는 것\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 독서는 우리에게 어떤 도움을 주는가?<br>'
         '· 사람들이 책을 멀리하게 된 이유는 무엇인가?<br>'
         '· 독서하는 습관을 기르려면 어떻게 해야 하는가?'
         '</div>'
     )},
]
