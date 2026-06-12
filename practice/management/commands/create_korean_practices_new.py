from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    topic_21, topic_22, topic_23, topic_24, topic_25, topic_26, topic_27, topic_28, topic_29, topic_30, topic_31, topic_32, topic_33, topic_34, topic_35, topic_36, topic_37, topic_38, topic_39, topic_40)

PRACTICES = [
    {
        'title': '수업 21: 동사 + 아/어 주다 (요청 및 도움)',
        'description': '다른 사람에게 도움을 요청하거나, 다른 사람을 위해 어떤 행동을 해 줄 때 사용하는 표현을 배웁니다.',
        'questions': topic_21,
    },
    {
        'title': '수업 22: 연결 어미 1: 동사/형용사 + 고 (나열 및 순서)',
        'description': '두 가지 이상의 행동이나 상태를 대등하게 나열하거나, 시간적 순서에 따라 연결하는 방법을 익힙니다.',
        'questions': topic_22,
    },
    {
        'title': '수업 23: 연결 어미 2: 동사/형용사 + 지만 (대조)',
        'description': '앞의 내용과 뒤의 내용이 서로 반대되거나 대조될 때 사용하는 연결 어미 \'-지만\'을 연습합니다.',
        'questions': topic_23,
    },
    {
        'title': '수업 24: 연결 어미 3: 동사/형용사 + 아/어서 (이유 및 시간적 순서)',
        'description': '앞선 상황이 뒤에 오는 상황의 이유나 원인이 되거나, 시간적 순서대로 일어나는 행동을 연결하는 표현을 학습합니다.',
        'questions': topic_24,
    },
    {
        'title': '수업 25: 동사/형용사 + (으)면 (조건과 가정)',
        'description': '어떤 조건이나 가정된 상황을 나타내는 연결 어미 \'-(으)면\'의 올바른 쓰임새를 배웁니다.',
        'questions': topic_25,
    },
    {
        'title': '수업 26: 비교 표현: 명사 + 보다 (더/덜)',
        'description': '두 대상의 크기, 정도, 특징 등을 비교할 때 사용하는 조사 \'보다\'와 \'더/덜\'의 활용을 익힙니다.',
        'questions': topic_26,
    },
    {
        'title': '수업 27: 동사 + 기 전에 / (으)ㄴ 후에 (시간적 선후 관계)',
        'description': '어떤 행동을 하기 전이나 한 후에 일어나는 시간적 선후 관계를 표현하는 방법을 연습합니다.',
        'questions': topic_27,
    },
    {
        'title': '수업 28: 동사 + (으)면서 (동시 동작)',
        'description': '두 가지 이상의 동작이나 상태가 동시에 일어남을 나타내는 \'-(으)면서\'의 활용을 학습합니다.',
        'questions': topic_28,
    },
    {
        'title': '수업 29: 동사 + (으)려고 하다 (의도와 계획)',
        'description': '앞으로 어떤 일을 하려는 화자의 의도나 구체적인 계획을 나타내는 표현을 배웁니다.',
        'questions': topic_29,
    },
    {
        'title': '수업 30: 동사 + 아/어 보다 (경험과 시도)',
        'description': '과거에 겪은 경험을 나타내거나, 새로운 행동을 한 번 시도해 볼 때 사용하는 \'-아/어 보다\'를 익힙니다.',
        'questions': topic_30,
    },
    {
        'title': '수업 31: 관형사형 어미 1: 동사 + 는 (현재)',
        'description': '동사 뒤에 붙어 뒤에 오는 명사를 꾸며주며, 현재 일어나고 있는 동작을 나타내는 관형사형 어미 \'-는\'을 연습합니다.',
        'questions': topic_31,
    },
    {
        'title': '수업 32: 관형사형 어미 2: 동사 + (으)ㄴ (과거), (으)ㄹ (미래)',
        'description': '과거의 행위나 미래에 일어날 행위로 뒤의 명사를 수식하는 관형사형 어미 \'-(으)ㄴ\'과 \'-(으)ㄹ\'을 학습합니다.',
        'questions': topic_32,
    },
    {
        'title': '수업 33: 관형사형 어미 3: 형용사 + (으)ㄴ',
        'description': '형용사 뒤에 붙어 명사의 상태나 특징을 묘사하는 관형사형 어미 \'-(으)ㄴ\'의 규칙을 배웁니다.',
        'questions': topic_33,
    },
    {
        'title': '수업 34: 명사화 표현: 동사 + 는 것, 동사 + 기',
        'description': '동사를 명사처럼 만들어 문장의 주어, 목적어 등으로 활용할 수 있게 하는 \'-는 것\'과 \'-기\'를 익힙니다.',
        'questions': topic_34,
    },
    {
        'title': '수업 35: 불규칙 용언 2 (\'르\', \'ㅅ\', \'ㅎ\' 불규칙)',
        'description': '모음 어미 앞에서 형태가 불규칙하게 변하는 \'르\', \'ㅅ\', \'ㅎ\' 불규칙 용언의 활용을 집중적으로 연습합니다.',
        'questions': topic_35,
    },
    {
        'title': '수업 36: 연결 어미 4: 동사/형용사 + (으)니까 (주관적 이유와 발견)',
        'description': '화자의 주관적인 이유나 원인을 나타내거나, 앞의 행동을 한 결과로 새로운 사실을 발견했을 때 쓰는 표현을 배웁니다.',
        'questions': topic_36,
    },
    {
        'title': '수업 37: 동사/형용사 + 기 때문에, 명사 + 때문에 (객관적 원인)',
        'description': '객관적이고 명확한 이유나 원인을 설명할 때 사용하는 \'-기 때문에\'와 명사 뒤의 \'때문에\'를 학습합니다.',
        'questions': topic_37,
    },
    {
        'title': '수업 38: 동사 + 아/어야 하다/되다 (의무와 필요)',
        'description': '어떤 행동을 반드시 해야 하는 의무나 필요성을 나타내는 \'-아/어야 하다/되다\'를 익힙니다.',
        'questions': topic_38,
    },
    {
        'title': '수업 39: 동사/형용사 + (으)ㄴ/는/(으)ㄹ 것 같다 (추측)',
        'description': '화자가 현재 상황이나 사실을 바탕으로 미래, 과거, 현재를 추측할 때 사용하는 표현을 연습합니다.',
        'questions': topic_39,
    },
    {
        'title': '수업 40: 동사 + (으)ㄹ 줄 알다/모르다 (방법과 능력)',
        'description': '어떤 일을 할 수 있는 구체적인 방법이나 능력을 알고 있는지 묻고 답하는 표현을 배웁니다.',
        'questions': topic_40,
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
