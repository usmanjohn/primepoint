import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from games.models import CodeBreakerPuzzle, CodeBreakerClue


def _candidates(target, difficulty):
    t = target
    exprs = []

    if difficulty == CodeBreakerPuzzle.DIFFICULTY_EASY:
        for a in range(0, t + 1):
            exprs.append(f"{a} + {t - a}")
        for b in range(1, 19):
            exprs.append(f"{t + b} - {b}")

    elif difficulty == CodeBreakerPuzzle.DIFFICULTY_MEDIUM:
        for i in range(2, t + 1):
            if t % i == 0 and t // i >= 2:
                exprs.append(f"{i} × {t // i}")
        for a in range(2, 11):
            b = a * a - t
            if 0 <= b <= 60:
                exprs.append(f"{a}² - {b}")
            b = t - a * a
            if 0 <= b <= 60:
                exprs.append(f"{a}² + {b}")
        for a in range(2, 9):
            for b in range(2, 9):
                c = t - a * b
                if 0 <= c <= 25:
                    exprs.append(f"{a} × {b} + {c}")
                c = a * b - t
                if 1 <= c <= 25:
                    exprs.append(f"{a} × {b} - {c}")

    elif difficulty == CodeBreakerPuzzle.DIFFICULTY_HARD:
        for b in range(1, 25):
            exprs.append(f"2x + {b} = {2*t + b},  find x")
        for b in range(1, 20):
            if 3 * t - b > 0:
                exprs.append(f"3x - {b} = {3*t - b},  find x")
        for b in range(2, 7):
            for c in range(2, 7):
                exprs.append(f"{t + b*c} - {b} × {c}")
        for c in range(2, t + 1):
            if t % c == 0:
                prod = t // c
                if 2 <= prod <= 20:
                    for a in range(1, prod):
                        exprs.append(f"({a} + {prod - a}) × {c}")

    return exprs


def _gen_expr(target, difficulty, used):
    candidates = _candidates(target, difficulty)
    random.shuffle(candidates)
    for expr in candidates:
        if expr not in used:
            return expr
    a = random.randint(0, target)
    return f"{a} + {target - a}"


SAMPLES = [
    {
        'title':      'Easy Start — Math',
        'word':       'MATH',
        'hint':       'What you do with numbers',
        'difficulty': CodeBreakerPuzzle.DIFFICULTY_EASY,
    },
    {
        'title':      'Medium Challenge — Python',
        'word':       'PYTHON',
        'hint':       'A popular programming language',
        'difficulty': CodeBreakerPuzzle.DIFFICULTY_MEDIUM,
    },
    {
        'title':      'Hard Mode — Algorithm',
        'word':       'ALGORITHM',
        'hint':       'A step-by-step problem-solving procedure',
        'difficulty': CodeBreakerPuzzle.DIFFICULTY_HARD,
    },
]


class Command(BaseCommand):
    help = 'Seed 3 sample Code Breaker puzzles (easy, medium, hard)'

    def handle(self, *args, **options):
        admin_user = User.objects.filter(is_superuser=True).first()
        if not admin_user:
            admin_user = User.objects.first()
        if not admin_user:
            self.stderr.write('No users found. Create a superuser first.')
            return

        created = 0
        for sample in SAMPLES:
            if CodeBreakerPuzzle.objects.filter(
                title=sample['title'], secret_word=sample['word']
            ).exists():
                self.stdout.write(f"  skip — already exists: {sample['title']}")
                continue

            puzzle = CodeBreakerPuzzle.objects.create(
                title=sample['title'],
                secret_word=sample['word'],
                hint=sample['hint'],
                difficulty=sample['difficulty'],
                created_by=admin_user,
                is_active=True,
            )
            used_exprs = set()
            for i, ch in enumerate(sample['word']):
                if not ch.isalpha():
                    continue
                letter_num = ord(ch.upper()) - ord('A') + 1
                expr       = _gen_expr(letter_num, sample['difficulty'], used_exprs)
                used_exprs.add(expr)
                CodeBreakerClue.objects.create(
                    puzzle=puzzle,
                    letter_index=i,
                    letter=ch.upper(),
                    math_expression=expr,
                    answer=letter_num,
                )
            self.stdout.write(self.style.SUCCESS(
                f"  created: {puzzle.title} ({len(sample['word'])} clues)"
            ))
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Done — {created} puzzle(s) created.'))
