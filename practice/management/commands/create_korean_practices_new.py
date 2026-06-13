from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from masters.models import Master
from practice.models import Subject, Practice, PracticeQuestion, PracticeChoice

from .korean_questions import (
   topic_73, topic_74, topic_75, topic_76, topic_77, topic_78, topic_79, topic_80, topic_81, topic_82,
   topic_83, topic_84, topic_85, topic_86
   )

PRACTICES = [
    {
        'title': '수업 73: 강한 양보와 가정: (으)ㄹ지라도 / 더라도 / (으)ㅁ에도 불구하고',
        'description': '비록 그러한 상황이거나 불리한 조건을 가정하더라도 뒤의 결과가 바뀌지 않음을 강하게 나타내는 표현을 배웁니다.',
        'questions': topic_73,
    },
    {
        'title': '수업 74: 정도와 한계: (으)ㄹ 정도로 / (으)ㄹ 만큼',
        'description': '어떤 행동이나 상태가 어느 정도까지 미치는지, 그 한계나 수준을 다른 상황에 빗대어 설명하는 표현을 배웁니다.',
        'questions': topic_74,
    },
    {
        'title': '수업 75: 극단적인 상태 강조: 기 짝이 없다',
        'description': '어떤 상태나 성질이 비교할 대상이 없을 정도로 아주 극단적이고 심함을 강조할 때 사용하는 표현을 익힙니다.',
        'questions': topic_75,
    },
    {
        'title': '수업 76: 단지 ~일 뿐이다: 에 불과하다 / (으)ㄹ 따름이다 / (으)ㄹ 뿐이다',
        'description': '오직 그것뿐이며 다른 것은 없거나, 그 이상의 대단한 의미나 가치가 없음을 한정 지어 나타내는 표현을 배웁니다.',
        'questions': topic_76,
    },
    {
        'title': '수업 77: 선택과 무관함: 든지 든지 / 건 건',
        'description': '여러 가지 상반된 선택지 중에서 어느 것을 선택하든지 뒤의 결과나 상황과는 아무런 상관이 없음을 나타냅니다.',
        'questions': topic_77,
    },
    {
        'title': '수업 78: 더 나은 대안 선택: (느)니 차라리',
        'description': '앞의 상황을 선택하는 것이 너무 싫거나 마음에 들지 않아, 차라리 뒤의 상황을 선택하는 것이 더 나음을 나타냅니다.',
        'questions': topic_78,
    },
    {
        'title': '수업 79: 행동의 무의미함: (으)나 마나',
        'description': '어떤 행동을 하든 하지 않든 결과는 뻔하고 똑같으므로, 그 행동을 하는 것이 아무런 의미나 소용이 없음을 나타냅니다.',
        'questions': topic_79,
    },
    {
        'title': '수업 80: 들은 사실의 확인: 다면서요 / 냐면서요',
        'description': '다른 사람에게서 들은 소문이나 이미 알고 있는 내용을 상대방에게 다시 확인하며 물어볼 때 사용하는 표현입니다.',
        'questions': topic_80,
    },
    {
        'title': '수업 81: 놀라움과 감탄: 다니 / 라니',
        'description': '어떤 사실이나 예상치 못한 상황에 대해 믿기 힘들 정도로 놀랍거나 감탄스러울 때 사용하는 감정 표현을 배웁니다.',
        'questions': topic_81,
    },
    {
        'title': '수업 82: 당연한 추측과 짐작: (으)려니 하다',
        'description': '어떤 상황이나 상태를 보고 당연히 그럴 것이라고 스스로 짐작하거나 으레 그럴 것으로 믿어 버릴 때 사용하는 표현입니다.',
        'questions': topic_82,
    },
    {
        'title': '수업 83: 원망이나 탓: (이)랍시고 / (으)ㄴ/는답시고',
        'description': '나름대로 목적을 가지고 노력했으나 결과가 기대에 미치지 못할 때, 이를 비웃거나 못마땅하게 여기며 탓하는 표현입니다.',
        'questions': topic_83,
    },
    {
        'title': '수업 84: 근거와 이유의 격식체: (으)로 말미암아 / (으)로 인해',
        'description': '어떤 일의 원인이나 근거가 무엇인지, 주로 격식 있는 글이나 공식적인 뉴스, 발표 등에서 설명하는 방법을 배웁니다.',
        'questions': topic_84,
    },
    {
        'title': '수업 85: 당연한 사실의 반문: 거늘',
        'description': '앞의 상황이 너무나 당연한데, 하물며 뒤의 상황은 더 말할 필요도 없이 당연함을 강조하거나 어찌 그러냐고 반문하는 표현입니다.',
        'questions': topic_85,
    },
    {
        'title': '수업 86: 극단적 양보와 포기: 기로서니',
        'description': '앞의 상황을 아무리 극단적으로 양보하고 이해한다고 하더라도, 뒤의 행동이나 상황은 도저히 용납할 수 없음을 나타냅니다.',
        'questions': topic_86,
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
