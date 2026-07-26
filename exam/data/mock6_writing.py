# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 6회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock6_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 6회',
    'language': 'korean',
    'exam_number': 106,
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
         '<b>제목: 자전거를 싸게 팝니다</b><br><br>'
         '작년에 산 자전거를 팝니다. 이사를 가게 되어서 더 이상 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '한 달에 두세 번 정도만 탔기 때문에 상태는 새것과 비슷합니다.<br>'
         '가격은 십만 원이고 직접 보고 결정하셔도 됩니다.<br>'
         '자전거를 사고 싶으신 분은 이번 주 안에 저에게 문자로 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '걷기는 특별한 장비나 돈이 필요 없기 때문에 누구나 쉽게 시작할 수 있는 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 그런데 걷기의 효과는 걷는 시간보다 걷는 '
         '습관에서 나온다. 하루에 세 시간을 걷고 일주일을 쉬는 것보다 매일 삼십 분씩 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;). 그러므로 무리하지 말고 자신이 지킬 수 있는 만큼 '
         '걷는 것이 좋다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'온라인 쇼핑 이용률의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>온라인 쇼핑 이용률</b> <small>(조사 기관: 한국소비자연구원, 대상: 성인 남녀 2,000명)</small><br><br>'
         '· 2015년: 35% &nbsp;→&nbsp; 2020년: 58% &nbsp;→&nbsp; 2025년: 82%<br>'
         '<b>· 10년 사이 약 2.3배 증가</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 스마트폰 사용의 확대<br>'
         '② 빠르고 편리해진 배송 서비스<br><br>'
         '<b>전망</b>: 2030년에는 90%를 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람들은 대부분 실패를 두려워한다. 그래서 실패할 것 같은 일은 아예 시작하지 않기도 한다. '
         '그러나 성공한 사람들 중에는 오히려 실패에서 많은 것을 배웠다고 말하는 사람이 적지 않다. '
         '아래의 내용을 중심으로 \'실패가 주는 교훈\'에 대한 자신의 생각을 쓰라.<br><br>'
         '· 사람들은 왜 실패를 두려워하는가?<br>'
         '· 실패를 통해 무엇을 배울 수 있는가?<br>'
         '· 실패를 대하는 바람직한 자세는 무엇인가?'
         '</div>'
     )},
]
