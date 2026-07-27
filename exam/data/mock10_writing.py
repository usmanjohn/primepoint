# ──────────────────────────────────────────────────────────────────
#  TOPIK II — PrimePoint 모의고사 10회 · 쓰기 (Writing) 51–54번
#
#  Load:   python manage.py load_mock exam/data/mock10_writing.py
# ──────────────────────────────────────────────────────────────────

EXAM_META = {
    'title': 'TOPIK II — PrimePoint 모의고사 10회',
    'language': 'korean',
    'exam_number': 110,
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
         '<b>제목: 지갑을 찾아 주신 분을 찾습니다</b><br><br>'
         '안녕하세요. 502동에 사는 주민입니다.<br>'
         '지난 토요일에 놀이터에서 지갑을 잃어버렸는데 어떤 분이 경비실에 '
         '(&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;).<br>'
         '안에 있던 돈과 카드가 하나도 없어지지 않았습니다.<br>'
         '직접 뵙고 인사를 드리고 싶으니 이 글을 보시면 저에게 '
         '(&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).<br>'
         '정말 감사합니다.'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 52, 'is_writing': True,
     'question_text': (
         f'<div style="{_BOX}">'
         '새로운 언어를 배울 때 사람들은 한 번에 많은 것을 외우려고 한다. 그러나 한 번에 많이 외운 것은 '
         '며칠만 지나면 대부분 (&nbsp;&nbsp;&nbsp;㉠&nbsp;&nbsp;&nbsp;). 우리 뇌는 여러 번 만나는 '
         '것을 중요한 정보라고 판단하기 때문이다. 그러므로 하루에 많은 양을 공부하기보다 같은 내용을 '
         '날마다 조금씩 (&nbsp;&nbsp;&nbsp;㉡&nbsp;&nbsp;&nbsp;).'
         '</div>'
         '<p style="margin-top:0.6rem;">㉠과 ㉡에 들어갈 문장을 아래에 각각 쓰십시오.<br>'
         '<small>예) ㉠: ... / ㉡: ...</small></p>'
     )},

    {'section': S, 'number': 53, 'is_writing': True,
     'question_text': (
         '<b>※ 다음은 \'국내 체류 외국인 수의 변화\'에 대한 조사 자료이다. '
         '이 내용을 200~300자의 글로 쓰십시오. 단, 글의 제목은 쓰지 마십시오.</b> (30점)'
         f'<div style="{_BOX}">'
         '<b>국내 체류 외국인 수</b> <small>(조사 기관: 한국이민정책연구원)</small><br><br>'
         '· 2015년: 약 190만 명 &nbsp;→&nbsp; 2020년: 약 200만 명 &nbsp;→&nbsp; 2025년: 약 280만 명<br>'
         '<b>· 전체 인구의 약 5.4% 차지</b><br><br>'
         '<b>증가 원인</b><br>'
         '① 산업 현장의 인력 부족<br>'
         '② 유학생과 결혼 이민자의 증가<br><br>'
         '<b>전망</b>: 2030년에는 350만 명을 넘을 것으로 예상됨'
         '</div>'
     )},

    {'section': S, 'number': 54, 'is_writing': True,
     'question_text': (
         '<b>※ 다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰십시오. '
         '단, 문제를 그대로 옮겨 쓰지 마십시오.</b> (50점)'
         f'<div style="{_BOX}">'
         '사람은 새로운 언어를 배우면서 낯선 세계와 만난다. 어떤 사람은 좋은 일자리를 얻기 위해 '
         '언어를 배우고, 어떤 사람은 그 나라의 문화를 알고 싶어서 배운다. 그러나 새로운 언어를 '
         '익히는 일은 결코 쉽지 않다. 아래의 내용을 중심으로 \'새로운 언어를 배운다는 것\'에 대한 '
         '자신의 생각을 쓰라.<br><br>'
         '· 새로운 언어를 배우면 무엇을 얻을 수 있는가?<br>'
         '· 언어를 배우는 과정에서 겪는 어려움은 무엇인가?<br>'
         '· 그 어려움을 이겨 내려면 어떤 자세가 필요한가?'
         '</div>'
     )},
]
