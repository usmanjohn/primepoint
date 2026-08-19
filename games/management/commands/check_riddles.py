"""The arithmetic gate for Prime Journey's riddle bank.

A wrong answer key is the worst bug a question bank can ship, and riddles are
worse than drills for it: a pupil who gets a riddle "wrong" because the key is
wrong learns the opposite of the lesson, and has no way to tell.

So every riddle is solved TWICE. The generator computes its answer one way; this
command reads the finished question **text**, pulls the numbers back out of it,
and recomputes the answer a different way — by simulation where it can, because
a second copy of the same formula proves nothing. Snails are actually walked up
wells here, day by day.

    python manage.py check_riddles
    python manage.py check_riddles --each=500
"""
import math
import re

from django.core.management.base import BaseCommand

from games import journey_riddles as R


def _nums(text):
    """Every integer in the question, in order."""
    return [int(n) for n in re.findall(r'\d+', text.replace(' ', ''))]


# Each checker gets (question, numbers-from-the-text) and returns the answer it
# believes in — recomputed from scratch, never by calling the generator again.

def _c_square_collect(q, n):
    total = n[0]
    root = math.isqrt(total)
    assert root * root == total, f'{total} is not a perfect square'
    return root


def _c_handshakes(q, n):
    shakes = n[0]
    people = 2
    while people * (people - 1) // 2 < shakes:
        people += 1
    assert people * (people - 1) // 2 == shakes, 'no whole number of people'
    return people


def _c_ages(q, n):
    times, years = n[0], n[1]
    for son in range(1, 200):                    # brute force, no algebra reused
        if times * son + years == 2 * (son + years):
            return son
    raise AssertionError('no whole-number age fits')


def _c_socks(q, n):
    # every colour appears once in the listing as "<count> <colour name>"
    listing = q['text'].split(':', 1)[1].split('.', 1)[0]
    colours = len(re.findall(r'\d+\s+\S+', listing))
    return colours + 1


def _c_heads_legs(q, n):
    heads, legs = n[0], n[1]
    for rabbits in range(heads + 1):
        chickens = heads - rabbits
        if 2 * chickens + 4 * rabbits == legs:
            return rabbits
    raise AssertionError('no whole number of rabbits')


def _c_calendar(q, n):
    days_uz = ['dushanba', 'seshanba', 'chorshanba', 'payshanba',
               'juma', 'shanba', 'yakshanba']
    days_en = ['monday', 'tuesday', 'wednesday', 'thursday',
               'friday', 'saturday', 'sunday']
    low = q['text'].lower()
    days = days_en if any(d in low for d in days_en) else days_uz
    # longest name first: 'shanba' is a substring of 'yakshanba'
    start = max((i for i, d in enumerate(days) if d in low), key=lambda i: len(days[i]))
    ahead = n[0]
    day = start                                   # walk the days one at a time
    for _ in range(ahead):
        day = (day + 1) % 7
    return day


def _c_stairs(q, n):
    # numbers read as: 1 (the ground floor), from_floor, minutes, 1 again, to_floor
    from_floor, minutes, to_floor = n[1], n[2], n[4]
    assert minutes % (from_floor - 1) == 0, 'flights do not divide evenly'
    per = minutes // (from_floor - 1)
    return (to_floor - 1) * per


def _c_snail(q, n):
    height, climb, slip = n[0], n[1], n[2]
    pos, day = 0, 0                               # actually walk the snail up
    while True:
        day += 1
        pos += climb
        if pos >= height:
            return day
        pos -= slip
        assert day < 10000, 'the snail never gets out'


def _c_log_cuts(q, n):
    per, pieces = n[0], n[1]
    return (pieces - 1) * per


def _c_boxes(q, n):
    return 1


def _c_digit_reverse(q, n):
    total, diff = n[0], n[1]
    for num in range(10, 100):                    # brute force every 2-digit number
        t, u = divmod(num, 10)
        if t + u == total and (10 * u + t) - num == diff:
            return num
    raise AssertionError('no such two-digit number')


def _c_triangular(q, n):
    top = n[1]
    return sum(range(1, top + 1))                 # add them all up, no formula


def _c_shared_work(q, n):
    a, b = n[0], n[1]
    from fractions import Fraction
    hours = Fraction(1, 1) / (Fraction(1, a) + Fraction(1, b))
    assert hours.denominator == 1, 'answer is not a whole number of hours'
    return int(hours)


def _c_balance(q, n):
    # numbers read as: x apples, 2 pears, 1 pear, y plums, N apples
    apples_per, pears_per, plums_per, apples = n[0], n[1], n[3], n[4]
    assert apples % apples_per == 0, 'apples do not group evenly'
    pears = apples // apples_per * pears_per
    return pears * plums_per


def _c_fake_coin(q, n):
    coins = n[0]
    weighings, reach = 0, 1
    while reach < coins:                          # each weighing triples the reach
        reach *= 3
        weighings += 1
    return weighings


def _c_triangular_or_seq(q, n):
    """The sequence riddle: the answer must continue one of the bank's rules."""
    seq = n
    shown, answer = seq[:5], q['answer_value']
    full = shown + [answer]
    # squares+n
    if all(v == (i + 1) ** 2 + (i + 1) for i, v in enumerate(full)):
        return answer
    # triangular
    if all(v == (i + 1) * (i + 2) // 2 for i, v in enumerate(full)):
        return answer
    # double and add one
    if all(full[i + 1] == full[i] * 2 + 1 for i in range(len(full) - 1)):
        return answer
    # growing gaps
    gaps = [full[i + 1] - full[i] for i in range(len(full) - 1)]
    steps = {gaps[i + 1] - gaps[i] for i in range(len(gaps) - 1)}
    if len(steps) == 1:
        return answer
    raise AssertionError(f'the sequence {full} follows no rule in the bank')


def _c_clock(q, n):
    hour, minute = n[0], n[1]
    hour_deg = (hour % 12) * 30 + minute * 0.5
    minute_deg = minute * 6
    gap = abs(hour_deg - minute_deg) % 360
    return int(min(gap, 360 - gap))


CHECKERS = {
    'square_collect': _c_square_collect, 'handshakes': _c_handshakes,
    'ages': _c_ages, 'socks': _c_socks, 'heads_legs': _c_heads_legs,
    'calendar': _c_calendar, 'stairs': _c_stairs, 'snail': _c_snail,
    'log_cuts': _c_log_cuts, 'boxes': _c_boxes,
    'digit_reverse': _c_digit_reverse, 'triangular': _c_triangular,
    'shared_work': _c_shared_work, 'balance': _c_balance,
    'fake_coin': _c_fake_coin, 'sequence': _c_triangular_or_seq,
    'clock': _c_clock,
}


class Command(BaseCommand):
    help = "Solve every Prime Journey riddle a second way and prove the answer keys."

    def add_arguments(self, parser):
        parser.add_argument('--each', type=int, default=200,
                            help='Riddles to generate per family (default 200).')

    def handle(self, *args, **options):
        each = options['each']
        problems, checked = [], 0

        missing = set(R.FAMILIES) - set(CHECKERS)
        if missing:
            problems.append(f'no independent checker for: {", ".join(sorted(missing))}')

        for gen in R.RIDDLES:
            family = gen.__name__.replace('r_', '')
            checker = CHECKERS.get(family)
            bad = 0
            for i in range(each):
                import random as _r
                q = gen(_r.Random(i * 7919 + 13), 'uz')
                checked += 1

                # the shape has to be right whatever the maths says
                if len(q['choices']) != 4:
                    problems.append(f'{family}: {len(q["choices"])} choices, not 4')
                    break
                texts = [c['text'] for c in q['choices']]
                if len(set(texts)) != 4:
                    bad += 1
                    problems.append(f'{family}: duplicate options {texts}')
                    continue
                if not 0 <= q['correct'] < 4:
                    problems.append(f'{family}: correct index {q["correct"]}')
                    break

                if checker is None:
                    continue
                try:
                    expected = checker(q, _nums(q['text']))
                except AssertionError as exc:
                    bad += 1
                    problems.append(f'{family}: {exc} — "{q["text"][:70]}"')
                    continue
                except Exception as exc:            # noqa: BLE001
                    bad += 1
                    problems.append(f'{family}: checker blew up ({exc}) — '
                                    f'"{q["text"][:70]}"')
                    continue

                if expected != q['answer_value']:
                    bad += 1
                    problems.append(
                        f'{family}: key says {q["answer_value"]}, second solve says '
                        f'{expected} — "{q["text"][:80]}"')
                if bad > 3:
                    break

            # the other language must at least build cleanly
            try:
                import random as _r
                en = gen(_r.Random(4242), 'en')
                if len(en['choices']) != 4 or not en['text'].strip():
                    problems.append(f'{family}: the English version is malformed')
            except Exception as exc:                # noqa: BLE001
                problems.append(f'{family}: the English version blew up ({exc})')

            mark = self.style.ERROR('✗') if bad else self.style.SUCCESS('✓')
            self.stdout.write(f'  {mark} {family}')

        self.stdout.write('')
        self.stdout.write(f'{checked} riddles generated and solved twice.')
        if problems:
            self.stdout.write(self.style.ERROR(f'\n{len(problems)} problem(s):'))
            for line in problems[:30]:
                self.stdout.write(self.style.ERROR(f'  ✗ {line}'))
            raise SystemExit(1)
        self.stdout.write(self.style.SUCCESS('Every answer key holds. ✓'))
