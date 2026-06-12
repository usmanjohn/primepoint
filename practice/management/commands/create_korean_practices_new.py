from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    topic_61, topic_62, topic_63, topic_64, topic_65, topic_66, topic_67, topic_68, topic_69, topic_70, topic_71, topic_72
)

PRACTICES = [
    {
        'title': '수업 61: 부정적 원인과 핑계: 동사 + 는 바람에, (으)ㄴ/는 탓에, 느라고',
        'description': '예상치 못한 일이나 부정적인 원인 때문에 원하지 않는 결과가 생겼을 때 변명이나 핑계를 대는 표현을 배웁니다.',
        'questions': topic_61,
    },
    {
        'title': '수업 62: 후회와 아쉬움: 동사 + (으)ㄹ걸 (그랬다), 았/었어야 했다',
        'description': '과거의 행동이나 하지 않은 일에 대해 후회하고 아쉬움을 나타내는 표현을 배웁니다.',
        'questions': topic_62,
    },
    {
        'title': '수업 63: 목적과 의도의 심화: 동사 + (으)ㄹ 겸, 고자',
        'description': '두 가지 이상의 목적을 동시에 가지거나 격식 있는 상황에서 어떤 행동의 뚜렷한 의도를 나타낼 때 사용하는 표현을 익힙니다.',
        'questions': topic_63,
    },
    {
        'title': '수업 64: 당연함과 필연성: 동사/형용사 + 기 마련이다, (으)ㄴ/는 법이다',
        'description': '세상의 이치나 자연스러운 현상처럼 어떤 일이 일어나는 것이 당연하고 필연적임을 나타내는 표현을 배웁니다.',
        'questions': topic_64,
    },
    {
        'title': '수업 65: 상태의 지속과 유지: 동사 + 아/어 놓다, 아/어 두다',
        'description': '어떤 행동을 끝낸 후 그 결과나 상태가 계속해서 유지되거나 미래를 위해 미리 준비해 놓음을 나타내는 표현을 배웁니다.',
        'questions': topic_65,
    },
    {
        'title': '수업 66: 강한 추측과 가능성: 동사/형용사 + (으)ㄹ지도 모르다, 기 십상이다',
        'description': '어떤 일이 일어날 가능성이 있음을 강하게 추측하거나, 특히 부정적인 상황이 발생하기 매우 쉬움을 경고하는 표현을 배웁니다.',
        'questions': topic_66,
    },
    {
        'title': '수업 67: 즉각적인 연속: 동사 + 자마자 / 동사 + 기가 무섭게',
        'description': '앞의 행동이나 사건이 끝나자마자 시간적 간격 없이 뒤의 행동이 곧바로 일어남을 강조하여 나타내는 표현을 배웁니다.',
        'questions': topic_67,
    },
    {
        'title': '수업 68: 기회와 도중: 동사 + 는 길에 / 는 김에',
        'description': '어떤 목적지로 이동하는 도중이거나, 어떤 일을 하는 기회를 이용하여 다른 일도 함께 함을 나타내는 표현을 배웁니다.',
        'questions': topic_68,
    },
    {
        'title': '수업 69: 행동의 완료 후 새로운 사실: 동사 + 고 나서 / (으)ㄴ 채로',
        'description': '한 행동이 완전히 끝난 후 다음 행동을 하거나, 앞선 행동의 상태가 그대로 유지된 상태에서 다른 행동을 함을 배웁니다.',
        'questions': topic_69,
    },
    {
        'title': '수업 70: 과거에 대한 반대 가정: 동사/형용사 + 았/었더라면',
        'description': '과거에 일어났던 사실과 반대되는 상황을 가정하여 후회, 아쉬움, 또는 다행임을 나타내는 표현을 배웁니다.',
        'questions': topic_70,
    },
    {
        'title': '수업 71: 부정적 결과의 경고: 동사/형용사 + 다가는',
        'description': '앞의 행동이나 상태가 계속 반복되거나 지속되면 결국 부정적인 결과가 생길 것임을 경고할 때 사용하는 표현을 배웁니다.',
        'questions': topic_71,
    },
    {
        'title': '수업 72: 노력의 소용없음: 동사/형용사 + 아/어 봤자',
        'description': '아무리 노력하거나 어떤 행동을 해 보아도 기대하는 결과가 나오지 않거나 아무 소용이 없음을 나타내는 표현을 배웁니다.',
        'questions': topic_72,
    }
]

class Command(BaseCommand):
    help = 'Create Korean grammar particle practice tests (lessons 61–72)'

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
