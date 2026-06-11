from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    topic_1, topic_2, topic_3, topic_4, topic_5, topic_6, topic_7, topic_8, topic_9, topic_10,
    topic_11, topic_12, topic_13, topic_14, topic_15, topic_16, topic_17, topic_18, topic_19, topic_20
    )
PRACTICES = [
    {
        'title': '수업 1: 한글 창제 원리와 자음, 모음',
        'description': '한글의 과학적인 창제 원리를 이해하고, 기본 자음과 모음의 형태 및 특징을 학습합니다.',
        'questions': topic_1,
    },
    {
        'title': '수업 2: 한글 발음 규칙과 받침',
        'description': '연음, 격음화, 비음화 등 한국어를 자연스럽게 읽기 위한 필수 발음 규칙과 받침의 소리 변화를 익힙니다.',
        'questions': topic_2,
    },
    {
        'title': '수업 3: 인사말, 기본 표현 및 자기소개',
        'description': '일상생활에서 가장 많이 쓰이는 필수 인사말을 익히고, 자연스럽게 자기를 소개하는 방법을 배웁니다.',
        'questions': topic_3,
    },
    {
        'title': '수업 4: 명사 + 입니다 / 입니까?',
        'description': '명사 뒤에 붙어 문장을 끝맺는 서술어 \'입니다\'와 질문을 만드는 의문어 \'입니까?\'의 쓰임을 학습합니다.',
        'questions': topic_4,
    },
    {
        'title': '수업 5: 조사 1 (은/는, 이/가)',
        'description': '문장의 주제를 나타내는 보조사 \'은/는\'과 주어를 나타내는 주격 조사 \'이/가\'의 차이점과 올바른 사용법을 연습합니다.',
        'questions': topic_5,
    },
    {
        'title': '수업 6: 조사 2 (을/를, 의)',
        'description': '동작의 대상을 나타내는 목적격 조사 \'을/를\'과 소유 및 소속을 나타내는 관형격 조사 \'의\'를 학습합니다.',
        'questions': topic_6,
    },
    {
        'title': '수업 7: 조사 3 (에, 에서)',
        'description': '존재하는 장소나 시간을 나타내는 \'에\'와, 어떤 동작이나 행위가 일어나는 장소를 나타내는 \'에서\'를 구분하여 연습합니다.',
        'questions': topic_7,
    },
    {
        'title': '수업 8: 동사/형용사 + 아/어요',
        'description': '일상생활에서 가장 널리 쓰이는 부드러운 비격식 존댓말인 \'아/어요\'의 결합 규칙을 배웁니다.',
        'questions': topic_8,
    },
    {
        'title': '수업 9: 동사/형용사 + ㅂ니다/습니다',
        'description': '발표나 회의 등 공식적인 자리에서 주로 사용하는 격식 존댓말 \'ㅂ니다/습니다\'의 형태를 익힙니다.',
        'questions': topic_9,
    },
    {
        'title': '수업 10: 동사/형용사 + 았/었어요 (과거형)',
        'description': '과거에 일어난 사건이나 이미 완료된 상태를 표현하는 과거 시제 \'았/었어요\'를 연습합니다.',
        'questions': topic_10,
    },
    {
        'title': '수업 11: 부정 표현 1 (안, 지 않다)',
        'description': '어떤 행동을 하지 않거나 상태를 부정할 때 사용하는 단순 부정 표현 \'안\'과 \'-지 않다\'를 배웁니다.',
        'questions': topic_11,
    },
    {
        'title': '수업 12: 부정 표현 2 (못, 지 못하다)',
        'description': '능력이 부족하거나 외부적인 이유로 어떤 일을 할 수 없음을 나타내는 불가능의 부정 표현을 학습합니다.',
        'questions': topic_12,
    },
    {
        'title': '수업 13: 한국어 숫자와 단위 명사',
        'description': '고유어 숫자와 한자어 숫자의 쓰임새를 구분하고, 사물이나 사람을 셀 때 쓰는 다양한 단위 명사를 익힙니다.',
        'questions': topic_13,
    },
    {
        'title': '수업 14: 시간, 날짜, 요일 표현',
        'description': '시, 분을 읽는 방법과 연, 월, 일, 그리고 요일을 정확한 한국어 숫자로 표현하는 방법을 연습합니다.',
        'questions': topic_14,
    },
    {
        'title': '수업 15: 의문사',
        'description': '누구, 무엇, 어디, 언제, 왜, 어떻게 등 육하원칙에 해당하는 필수 의문사를 활용해 질문을 만드는 법을 배웁니다.',
        'questions': topic_15,
    },
    {
        'title': '수업 16: 불규칙 용언 1 (\'ㅂ\', \'ㄷ\', \'으\' 불규칙)',
        'description': '뒤에 오는 어미에 따라 형태가 불규칙하게 변하는 \'ㅂ\', \'ㄷ\', \'으\' 불규칙 동사와 형용사의 활용 규칙을 익힙니다.',
        'questions': topic_16,
    },
    {
        'title': '수업 17: 동사 + (으)ㄹ 거예요 (미래 및 추측)',
        'description': '미래의 계획이나 일어날 일에 대한 화자의 확신 있는 추측을 나타내는 표현을 학습합니다.',
        'questions': topic_17,
    },
    {
        'title': '수업 18: 동사 + 고 싶다 (희망 표현)',
        'description': '본인이나 다른 사람의 구체적인 소망, 희망, 그리고 바람을 나타내는 \'-고 싶다\'의 올바른 사용법을 배웁니다.',
        'questions': topic_18,
    },
    {
        'title': '수업 19: 동사 + (으)세요 / 지 마세요 (명령과 금지)',
        'description': '상대방에게 정중하게 어떤 행동을 요구하거나 지시하는 표현과, 특정한 행동을 금지하는 표현을 연습합니다.',
        'questions': topic_19,
    },
    {
        'title': '수업 20: 동사 + (으)ㄹ 수 있다/없다 (가능과 불가능)',
        'description': '어떤 일을 할 수 있는 개인의 능력이나, 상황에 따른 가능성과 불가능성을 표현하는 방법을 익힙니다.',
        'questions': topic_20,
    }
]


class Command(BaseCommand):
    help = 'Create Korean grammar particle practice tests (lessons 5–9)'

    def add_arguments(self, parser):
        parser.add_argument('--master', required=True, help='Username of the master to assign practices to')

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options['master'])
        except User.DoesNotExist:
            raise CommandError(f"User '{options['master']}' not found.")

        try:
            master = Master.objects.get(profile__user=user)
        except Master.DoesNotExist:
            raise CommandError(f"No Master profile found for user '{options['master']}'.")

        subject, _ = Subject.objects.get_or_create(
            name='한국어',
            defaults={'description': '한국어 문법 및 어휘 연습'},
        )

        for practice_data in PRACTICES:
            practice, created = Practice.objects.get_or_create(
                title=practice_data['title'],
                master=master,
                defaults={
                    'description': practice_data['description'],
                    'subject': subject,
                    'level': 'medium',
                    'is_free': True,
                    'is_published': True,
                    'is_available_for_all': True,
                    'pass_score': 60,
                    'max_attempts': 0,
                    'show_answers_after': True,
                },
            )

            if not created:
                self.stdout.write(self.style.WARNING(
                    f"Practice '{practice.title}' already exists (id={practice.pk}). Skipping."
                ))
                continue

            questions = practice_data['questions']
            for i, q in enumerate(questions, start=1):
                question = PracticeQuestion.objects.create(
                    practice=practice,
                    question_text=q['text'],
                    explanation=q['explanation'],
                    order=i,
                    points=1,
                )
                for choice_text in q['choices']:
                    PracticeChoice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=(choice_text == q['correct']),
                    )

            self.stdout.write(self.style.SUCCESS(
                f"Created '{practice.title}' with {len(questions)} questions (id={practice.pk})."
            ))
