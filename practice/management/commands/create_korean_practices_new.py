from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
    topic_41, topic_42, topic_43, topic_44, topic_45,
    topic_46, topic_47, topic_48, topic_49, topic_50,
    topic_51, topic_52, topic_53, topic_54, topic_55, topic_56, topic_57, topic_58, topic_59, topic_60
)
PRACTICES = [
    {
        'title': '수업 41: 동사 + 기로 하다 (결정과 약속)',
        'description': '어떤 일을 하기로 스스로 결심하거나, 다른 사람과 약속할 때 사용하는 표현을 배웁니다.',
        'questions': topic_41,
    },
    {
        'title': '수업 42: 동사/형용사 + 잖아요 (확인 및 강조)',
        'description': '말하는 사람과 듣는 사람이 모두 이미 알고 있는 사실을 다시 확인하거나 강조할 때 사용하는 표현을 익힙니다.',
        'questions': topic_42,
    },
    {
        'title': '수업 43: 피동 표현 (-이/히/리/기-, 아/어지다)',
        'description': '주어가 스스로 행동하는 것이 아니라, 다른 사람이나 사물에 의해 어떤 행동을 당하게 되는 피동 문법을 배웁니다.',
        'questions': topic_43,
    },
    {
        'title': '수업 44: 사동 표현 (-이/히/리/기/우/구/추-, 게 하다)',
        'description': '주어가 직접 행동하지 않고, 다른 사람이나 동물에게 어떤 행동을 하도록 시키거나 만드는 사동 문법을 배웁니다.',
        'questions': topic_44,
    },
    {
        'title': '수업 45: 동사 + 아/어 버리다 (행동의 완료와 감정적 결과)',
        'description': '어떤 행동이 완전히 끝나서 남은 것이 없음을 나타내며, 그에 따른 아쉬움이나 후련함 등의 감정을 표현합니다.',
        'questions': topic_45,
    },
    {
        'title': '수업 46: 간접 화법 1: 평서문 (-다고 하다), 의문문 (-냐고 하다)',
        'description': '다른 사람이 한 평서문(설명)이나 의문문(질문)의 말을 제3자에게 전달할 때 사용하는 간접 화법을 익힙니다.',
        'questions': topic_46,
    },
    {
        'title': '수업 47: 간접 화법 2: 명령문 (-라고 하다), 청유문 (-자고 하다)',
        'description': '다른 사람이 한 명령문(지시)이나 청유문(제안)의 말을 제3자에게 전달할 때 사용하는 간접 화법을 익힙니다.',
        'questions': topic_47,
    },
    {
        'title': '수업 48: 동사 + (으)ㄹ 뻔하다 (과거의 위기 모면)',
        'description': '과거에 어떤 위험하거나 나쁜 일이 일어날 가능성이 있었지만, 다행히 일어나지 않았음을 나타낼 때 사용합니다.',
        'questions': topic_48,
    },
    {
        'title': '수업 49: 동사 + (으)ㄹ 테니까 (화자의 의지 및 추측에 따른 이유)',
        'description': '말하는 사람의 강한 의지나 추측을 이유나 조건으로 삼아, 듣는 사람에게 제안이나 부탁을 할 때 사용하는 표현입니다.',
        'questions': topic_49,
    },
    {
        'title': '수업 50: 동사/형용사 + (으)ㄹ수록 (정도의 심화)',
        'description': '앞의 상황이나 행동의 정도가 더해질수록 뒤의 결과나 상태도 비례해서 심해지거나 달라짐을 나타냅니다.',
        'questions': topic_50,
    },
    {
        'title': '수업 51: 명사 + (이)나 다름없다 / 동사 + (으)ㄴ/는 셈이다 (결과적 동일)',
        'description': '실제로는 완전히 같지 않지만, 결과적으로 보았을 때 그것과 같거나 마찬가지임을 나타내는 표현을 배웁니다.',
        'questions': topic_51,
    },
    {
        'title': '수업 52: 동사/형용사 + (으)ㄴ/는 반면에 (상반된 사실)',
        'description': '앞의 내용과 뒤의 내용이 서로 반대되거나, 한 가지 대상의 긍정적인 면과 부정적인 면을 대조할 때 사용합니다.',
        'questions': topic_52,
    },
    {
        'title': '수업 53: 동사/형용사 + (으)ㄹ 뿐만 아니라 (점층과 추가)',
        'description': '앞의 사실에 더하여 뒤의 사실까지 긍정적 또는 부정적인 특징이나 상황이 추가됨을 나타내는 표현입니다.',
        'questions': topic_53,
    },
    {
        'title': '수업 54: 동사/형용사 + (으)ㄴ/는 데다가 (상황의 가중)',
        'description': '이미 있는 어떤 상황이나 상태에 더하여, 같은 성격(긍정 또는 부정)의 상황이 한층 더 심해짐을 나타냅니다.',
        'questions': topic_54,
    },
    {
        'title': '수업 55: 동사 + 다가 보면 (행동의 지속과 새로운 결과 발견)',
        'description': '어떤 행동을 중간에 멈추지 않고 계속 반복하거나 지속할 때, 새로운 사실을 알게 되거나 결과가 생김을 나타냅니다.',
        'questions': topic_55,
    },
    {
        'title': '수업 56: 동사/형용사 + (으)ㅁ으로써 (수단과 방법의 명사화)',
        'description': '어떤 행동이 뒤에 오는 일의 수단, 방법, 또는 원인이 됨을 격식 있게 표현하는 방법을 배웁니다.',
        'questions': topic_56,
    },
    {
        'title': '수업 57: 동사/형용사 + (으)ㄹ 지경이다 (극단적 상태나 한계)',
        'description': '어떤 상태나 상황이 감당하기 힘들 정도로 아주 극단적인 한계에 이르렀음을 과장하여 나타내는 표현입니다.',
        'questions': topic_57,
    },
    {
        'title': '수업 58: 동사/형용사 + (으)ㄹ 리가 없다 / (으)ㄹ 턱이 없다 (강한 의심과 부정)',
        'description': '어떤 일이 일어날 가능성이나 이유가 전혀 없음을 강하게 확신하며 의심하고 부정할 때 사용하는 표현입니다.',
        'questions': topic_58,
    },
    {
        'title': '수업 59: 명사 + 에 달려 있다 (조건에 따른 결과)',
        'description': '어떤 일의 성공이나 결과가 앞서 말한 조건, 행동, 또는 대상에 따라 결정됨을 나타내는 표현을 배웁니다.',
        'questions': topic_59,
    },
    {
        'title': '수업 60: 동사 + (으)려던 참이다 (막 하려던 의도와 우연의 일치)',
        'description': '말하는 사람이 막 어떤 행동을 하려고 마음먹고 있던 짧은 순간에, 우연히 외부 상황이 맞아떨어졌을 때 사용합니다.',
        'questions': topic_60,
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
