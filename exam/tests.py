"""Regression tests for the mock-exam engine.

The three things that can ship silently broken here, in the order they would
hurt: a wrong grid-in verdict, a wrong adaptive route, and a score that does
not match the route the taker was actually sent down.
"""
from django.contrib.auth.models import User
from django.core.management.base import CommandError
from django.test import TestCase
from django.urls import reverse

from panda.models import Panda
from exam import gmatscore, satscore
from exam.gridin import grid_answer_matches, parse
from exam.models import (
    Exam, ExamModule, ExamQuestion, ExamChoice, ExamAttempt, ExamAnswer,
)


class GridInTests(TestCase):
    """College Board's own rules for a student-produced response."""

    def test_same_value_different_writing(self):
        for typed in ('2/3', '4/6', '.6666', '.6667', '0.666', '0.667'):
            self.assertTrue(grid_answer_matches(typed, ['2/3']), typed)

    def test_too_few_digits_is_wrong(self):
        for typed in ('.67', '0.6', '.7', '2/4'):
            self.assertFalse(grid_answer_matches(typed, ['2/3']), typed)

    def test_four_significant_digits_without_three_decimals(self):
        # 100/3 = 33.333… — 33.33 fills the box, 33.3 does not.
        self.assertTrue(grid_answer_matches('33.33', ['100/3']))
        self.assertFalse(grid_answer_matches('33.3', ['100/3']))

    def test_forbidden_characters_are_wrong_answers(self):
        # Prime SAT breaks the comma habit on purpose: these must NOT be forgiven.
        self.assertFalse(grid_answer_matches('1,200', ['1200']))
        self.assertFalse(grid_answer_matches('50%', ['50']))
        self.assertFalse(grid_answer_matches('$8', ['8']))

    def test_mixed_number_is_rejected(self):
        self.assertFalse(grid_answer_matches('1 1/4', ['5/4']))
        self.assertTrue(grid_answer_matches('5/4', ['5/4']))
        self.assertTrue(grid_answer_matches('1.25', ['5/4']))

    def test_negatives_and_junk(self):
        self.assertTrue(grid_answer_matches('-2/3', ['-2/3']))
        self.assertFalse(grid_answer_matches('7', ['-7']))
        self.assertFalse(grid_answer_matches('abc', ['3']))
        self.assertFalse(grid_answer_matches('', ['3']))
        self.assertIsNone(parse('3/0'))


class ScaleTests(TestCase):
    def test_the_lower_module_cannot_reach_800(self):
        self.assertEqual(satscore.scale('rw', 'hard', 54), 800)
        self.assertLess(satscore.scale('rw', 'easy', 54), 650)
        self.assertEqual(satscore.scale('math', 'hard', 44), 800)
        self.assertLess(satscore.scale('math', 'easy', 44), 650)

    def test_floor_and_monotonicity(self):
        self.assertEqual(satscore.scale('rw', 'hard', 0), 200)
        previous = 0
        for raw in range(0, 55):
            value = satscore.scale('rw', 'hard', raw)
            self.assertGreaterEqual(value, previous)
            previous = value

    def test_scores_are_multiples_of_ten(self):
        for kind, top in (('rw', 54), ('math', 44)):
            for route in ('easy', 'hard'):
                for raw in range(top + 1):
                    self.assertEqual(satscore.scale(kind, route, raw) % 10, 0)


class SatFlowTests(TestCase):
    """Build a miniature adaptive SAT and walk a taker through it."""

    def setUp(self):
        self.user = User.objects.create_user('taker', password='pw')
        self.panda, _ = Panda.objects.get_or_create(profile=self.user.profile)
        self.exam = Exam.objects.create(
            title='Test SAT', language='english', exam_format='sat',
            exam_number=9001, is_published=True,
        )
        self.modules = {}
        specs = [
            ('rw1', 'rw', 1, '', 1, 2, 0),     # route_threshold 2 of 3
            ('rw2e', 'rw', 2, 'easy', 1, None, 10),
            ('rw2h', 'rw', 2, 'hard', 1, None, 10),
            ('math1', 'math', 1, '', 2, 2, 0),
            ('math2e', 'math', 2, 'easy', 2, None, 0),
            ('math2h', 'math', 2, 'hard', 2, None, 0),
        ]
        for code, kind, stage, difficulty, order, threshold, brk in specs:
            self.modules[code] = ExamModule.objects.create(
                exam=self.exam, code=code, kind=kind, stage=stage, difficulty=difficulty,
                label=code, minutes=32, order=order,
                route_threshold=threshold, break_minutes=brk,
            )
        for code in ('rw1', 'rw2e', 'rw2h'):
            for n in range(1, 4):
                self._mcq(code, n)
        for code in ('math1', 'math2e', 'math2h'):
            for n in range(1, 3):
                self._mcq(code, n)
            self._grid(code, 3)
        self.client.login(username='taker', password='pw')

    def _mcq(self, section, number):
        question = ExamQuestion.objects.create(
            exam=self.exam, section=section, number=number,
            question_text=f'{section} {number}', skill='Algebra', explanation='izoh',
        )
        for i in range(4):
            ExamChoice.objects.create(question=question, text=f'c{i}', is_correct=(i == 0))
        return question

    def _grid(self, section, number):
        return ExamQuestion.objects.create(
            exam=self.exam, section=section, number=number, answer_type='grid',
            accepted_answers='2/3', question_text='grid', skill='Algebra', explanation='izoh',
        )

    def _submit(self, attempt, correct_count):
        """Answer the current module, getting `correct_count` of them right."""
        module = attempt.current_module
        data = {}
        for i, question in enumerate(module.questions().order_by('number')):
            want_right = i < correct_count
            if question.answer_type == 'grid':
                data[f'q{question.id}'] = '2/3' if want_right else '5'
            else:
                choice = question.choices.filter(is_correct=want_right).first()
                data[f'q{question.id}'] = choice.id
        return self.client.post(reverse('submit_section', args=[attempt.id]), data)

    def test_high_score_routes_to_the_upper_module(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self.assertEqual(attempt.current_module.code, 'rw1')
        self._submit(attempt, 3)
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'rw2h')

    def test_low_score_routes_to_the_lower_module(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self._submit(attempt, 1)
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'rw2e')

    def test_break_sits_between_the_two_sections(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self._submit(attempt, 3)
        attempt.refresh_from_db()
        response = self._submit(attempt, 3)         # finish rw2h
        attempt.refresh_from_db()
        self.assertEqual(attempt.status, 'break')
        self.assertEqual(attempt.current_module.code, 'math1')
        self.assertRedirects(response, reverse('exam_break', args=[attempt.id]))
        # Taking the exam while on a break bounces back to the break page.
        self.assertRedirects(
            self.client.get(reverse('take_section', args=[attempt.id])),
            reverse('exam_break', args=[attempt.id]))
        # Pressing "I'm ready" starts the next module.
        self.client.post(reverse('exam_break', args=[attempt.id]))
        attempt.refresh_from_db()
        self.assertEqual(attempt.status, 'in_progress')
        self.assertIsNotNone(attempt.module_attempt(self.modules['math1']).started_at)

    def test_full_sitting_scores_both_sections(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self._submit(attempt, 3)                       # rw1: 3/3 -> upper
        attempt.refresh_from_db()
        self._submit(attempt, 2)                       # rw2h: 2/3
        attempt.refresh_from_db()
        self.client.post(reverse('exam_break', args=[attempt.id]))
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'math1')
        self._submit(attempt, 3)                       # math1: 3/3 -> upper
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'math2h')
        self._submit(attempt, 1)                       # math2h: 1/3
        attempt.refresh_from_db()

        self.assertEqual(attempt.current_section, 'completed')
        self.assertEqual(attempt.status, 'completed')
        # Only the four modules met should have rows — never all six.
        self.assertEqual(attempt.module_attempts.count(), 4)
        self.assertEqual(
            sorted(ma.module.code for ma in attempt.module_attempts.all()),
            ['math1', 'math2h', 'rw1', 'rw2h'])
        self.assertEqual(attempt.rw_score, satscore.scale('rw', 'hard', 5))
        self.assertEqual(attempt.math_score, satscore.scale('math', 'hard', 4))
        self.assertEqual(attempt.total_score, attempt.rw_score + attempt.math_score)

    def test_grid_in_is_graded_by_value_not_by_string(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self._submit(attempt, 3)
        attempt.refresh_from_db()
        self._submit(attempt, 3)
        attempt.refresh_from_db()
        self.client.post(reverse('exam_break', args=[attempt.id]))
        attempt.refresh_from_db()
        grid = ExamQuestion.objects.get(exam=self.exam, section='math1', number=3)
        self.client.post(reverse('submit_section', args=[attempt.id]),
                         {f'q{grid.id}': '0.667'})
        answer = ExamAnswer.objects.get(attempt=attempt, question=grid)
        self.assertTrue(answer.is_correct())
        self.assertEqual(attempt.module_attempt(self.modules['math1']).raw_score, 1)

    def test_result_page_renders(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        for _ in range(4):
            self._submit(attempt, 2)
            attempt.refresh_from_db()
            if attempt.status == 'break':
                self.client.post(reverse('exam_break', args=[attempt.id]))
                attempt.refresh_from_db()
        response = self.client.get(reverse('exam_result', args=[attempt.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exam/exam_result_sat.html')
        self.assertContains(response, str(attempt.total_score))


class TopikStillWorksTests(TestCase):
    """The TOPIK mocks must survive the move onto modules unchanged."""

    def setUp(self):
        self.user = User.objects.create_user('kt', password='pw')
        self.panda, _ = Panda.objects.get_or_create(profile=self.user.profile)
        self.exam = Exam.objects.create(
            title='Test TOPIK', language='korean', exam_number=9002, is_published=True,
            listening_minutes=60, reading_minutes=70, writing_minutes=50,
        )
        for code, kind, order, minutes in (
                ('listening', 'listening', 1, 60), ('reading', 'reading', 2, 70),
                ('writing', 'writing', 3, 50)):
            ExamModule.objects.create(
                exam=self.exam, code=code, kind=kind, stage=1, label=code,
                minutes=minutes, order=order)
        for code in ('listening', 'reading'):
            question = ExamQuestion.objects.create(exam=self.exam, section=code, number=1)
            for i in range(4):
                ExamChoice.objects.create(question=question, text=f'c{i}', is_correct=(i == 0))
        ExamQuestion.objects.create(
            exam=self.exam, section='writing', number=1, is_writing=True, answer_type='essay')
        self.client.login(username='kt', password='pw')

    def test_three_sections_in_order_and_percentage_scores(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        self.assertEqual(attempt.current_module.code, 'listening')

        question = ExamQuestion.objects.get(exam=self.exam, section='listening', number=1)
        correct = question.choices.get(is_correct=True)
        self.client.post(reverse('submit_section', args=[attempt.id]),
                         {f'q{question.id}': correct.id})
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'reading')
        self.assertEqual(attempt.listening_score, 100)

        question = ExamQuestion.objects.get(exam=self.exam, section='reading', number=1)
        wrong = question.choices.filter(is_correct=False).first()
        self.client.post(reverse('submit_section', args=[attempt.id]), {f'q{question.id}': wrong.id})
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_module.code, 'writing')
        self.assertEqual(attempt.reading_score, 0)
        self.assertEqual(attempt.status, 'in_progress')   # no break in TOPIK

        essay = ExamQuestion.objects.get(exam=self.exam, section='writing', number=1)
        response = self.client.post(reverse('submit_section', args=[attempt.id]),
                                    {f'q{essay.id}': 'yozilgan javob'})
        attempt.refresh_from_db()
        self.assertEqual(attempt.current_section, 'completed')
        self.assertRedirects(response, reverse('exam_result', args=[attempt.id]))
        self.assertIsNone(attempt.total_score)           # not a SAT

    def test_result_page_uses_the_topik_template(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = ExamAttempt.objects.get(panda=self.panda)
        for _ in range(3):
            self.client.post(reverse('submit_section', args=[attempt.id]), {})
            attempt.refresh_from_db()
        response = self.client.get(reverse('exam_result', args=[attempt.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exam/exam_result.html')


class TotalMinutesTests(TestCase):
    def test_an_adaptive_sitting_counts_one_branch_and_the_break(self):
        exam = Exam.objects.create(title='T', language='english', exam_format='sat',
                                   exam_number=9003)
        ExamModule.objects.create(exam=exam, code='rw1', kind='rw', stage=1,
                                  label='rw1', minutes=32, order=1)
        for difficulty in ('easy', 'hard'):
            ExamModule.objects.create(exam=exam, code=f'rw2{difficulty[0]}', kind='rw',
                                      stage=2, difficulty=difficulty, label='rw2',
                                      minutes=32, order=1, break_minutes=10)
        ExamModule.objects.create(exam=exam, code='math1', kind='math', stage=1,
                                  label='math1', minutes=35, order=2)
        for difficulty in ('easy', 'hard'):
            ExamModule.objects.create(exam=exam, code=f'math2{difficulty[0]}', kind='math',
                                      stage=2, difficulty=difficulty, label='math2',
                                      minutes=35, order=2)
        # 32 + 32 + 10 break + 35 + 35 — the two branches of a section count once,
        # and the break, which is declared on the branch, must not be lost.
        self.assertEqual(exam.total_minutes(), 144)


class LoadMockGateTests(TestCase):
    """The loader must refuse a broken file before it writes anything."""

    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp()

    def _run(self, questions, **meta):
        import os
        from django.core.management import call_command
        path = os.path.join(self.tmp, 'data.py')
        body = {
            'title': 'Gate test', 'language': 'english', 'exam_format': 'sat',
            'exam_number': 9100, 'is_published': False,
        }
        body.update(meta)
        with open(path, 'w') as handle:
            handle.write(f'EXAM_META = {body!r}\nMODULES = []\nQUESTIONS = {questions!r}\n')
        call_command('load_mock', path)

    def _question(self, **overrides):
        question = {
            'section': 'rw1', 'number': 1, 'question_text': 'q',
            'choices': ['a', 'b', 'c', 'd'], 'correct': 1,
            'explanation': 'izoh', 'skill': 'Words in Context',
        }
        question.update(overrides)
        return question

    def test_a_good_file_loads(self):
        self._run([self._question()])
        self.assertEqual(ExamQuestion.objects.filter(exam__exam_number=9100).count(), 1)

    def test_sat_question_without_an_explanation_is_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._question(explanation='')])
        self.assertFalse(Exam.objects.filter(exam_number=9100).exists())

    def test_choice_letter_in_an_explanation_is_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._question(explanation='Choice B notoʻgʻri.')])

    def test_duplicate_choices_are_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._question(choices=['a', 'a', 'c', 'd'])])

    def test_grid_in_without_a_legal_answer_is_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._question(answer_type='grid', choices=[], correct=None,
                                      accepted=['1,200'])])
        with self.assertRaises(CommandError):
            self._run([self._question(answer_type='grid', choices=[], correct=None,
                                      accepted=[])])

    def test_expect_questions_mismatch_is_refused(self):
        import os
        from django.core.management import call_command
        path = os.path.join(self.tmp, 'count.py')
        with open(path, 'w') as handle:
            handle.write("EXAM_META = {'title': 'c', 'language': 'english', "
                         "'exam_format': 'topik', 'exam_number': 9101}\n"
                         "QUESTIONS = []\n")
        with self.assertRaises(CommandError):
            call_command('load_mock', path, expect_questions=27)


class SatMockContentTests(TestCase):
    """The shape of every shipped mock, checked without touching the database.

    These are not a substitute for the scratchpad answer gates — those
    recompute every maths answer. This locks in the blueprint so a later edit
    cannot quietly drop a question or move a grid-in.

    MOCKS is derived from the files on disk, so adding mock 3 puts it under
    test without anyone remembering to come back here.
    """
    MODULE_SIZES = [
        ('rw1', 'rw1', 27), ('rw2_easy', 'rw2e', 27), ('rw2_hard', 'rw2h', 27),
        ('math1', 'math1', 22), ('math2_easy', 'math2e', 22),
        ('math2_hard', 'math2h', 22),
    ]

    @classmethod
    def mock_numbers(cls):
        import glob
        import os
        import re
        from django.conf import settings
        pattern = os.path.join(settings.BASE_DIR, 'exam', 'data', 'sat*_rw1.py')
        found = sorted(int(re.search(r'sat(\d+)_rw1', p).group(1))
                       for p in glob.glob(pattern))
        assert found, 'no SAT mock data files found'
        return found

    @property
    def FILES(self):
        files = {}
        for number in self.mock_numbers():
            for suffix, code, count in self.MODULE_SIZES:
                files[f'sat{number}_{suffix}'] = (code, count)
        return files
    RW_BLUEPRINT = {
        'Words in Context': 4, 'Text Structure and Purpose': 2,
        'Cross-Text Connections': 1, 'Central Ideas and Details': 2,
        'Command of Evidence': 3, 'Inferences': 2, 'Boundaries': 3,
        'Form, Structure, and Sense': 4, 'Transitions': 3,
        'Rhetorical Synthesis': 3,
    }
    MATH_BLUEPRINT = {
        'Algebra': 8, 'Advanced Math': 7,
        'Problem-Solving and Data Analysis': 4, 'Geometry and Trigonometry': 3,
    }

    def _load(self, name):
        import importlib.util
        import os
        from django.conf import settings
        path = os.path.join(settings.BASE_DIR, 'exam', 'data', f'{name}.py')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_every_module_has_the_right_size_and_section(self):
        per_mock = {}
        for name, (code, count) in self.FILES.items():
            module = self._load(name)
            questions = module.QUESTIONS
            self.assertEqual(len(questions), count, name)
            self.assertEqual({q['section'] for q in questions}, {code}, name)
            self.assertEqual([q['number'] for q in questions],
                             list(range(1, count + 1)), name)
            per_mock[name.split('_')[0]] = per_mock.get(name.split('_')[0], 0) + count
        # 147 written per mock: 27 x 3 for Reading and Writing, 22 x 3 for Math.
        for mock, total in per_mock.items():
            self.assertEqual(total, 147, mock)

    def test_the_six_files_of_a_mock_agree_on_the_exam_and_its_modules(self):
        for number in self.mock_numbers():
            names = [f'sat{number}_{suffix}' for suffix, _c, _n in self.MODULE_SIZES]
            metas = [self._load(name).EXAM_META for name in names]
            self.assertEqual({m['exam_number'] for m in metas}, {200 + number})
            self.assertEqual({m['exam_format'] for m in metas}, {'sat'})
            module_lists = [self._load(name).MODULES for name in names]
            first = module_lists[0]
            for other in module_lists[1:]:
                self.assertEqual(first, other,
                                 f'MODULES drifted between mock {number} files')
            self.assertEqual({m['code'] for m in first},
                             {'rw1', 'rw2e', 'rw2h', 'math1', 'math2e', 'math2h'})

    def test_mocks_do_not_share_an_exam_number(self):
        numbers = [self._load(f'sat{n}_rw1').EXAM_META['exam_number']
                   for n in self.mock_numbers()]
        self.assertEqual(len(numbers), len(set(numbers)))

    def test_blueprints(self):
        from collections import Counter
        for name, (code, _count) in self.FILES.items():
            counts = Counter(q['skill'] for q in self._load(name).QUESTIONS)
            expected = self.MATH_BLUEPRINT if code.startswith('math') else self.RW_BLUEPRINT
            self.assertEqual(dict(counts), expected, name)

    def test_grid_ins_sit_at_the_end_of_every_math_module(self):
        from exam.gridin import parse
        for name, (code, _count) in self.FILES.items():
            questions = self._load(name).QUESTIONS
            grids = {q['number'] for q in questions if q.get('answer_type') == 'grid'}
            self.assertEqual(grids, {18, 19, 20, 21, 22} if code.startswith('math') else set(),
                             name)
            for q in questions:
                if q.get('answer_type') != 'grid':
                    continue
                self.assertTrue(q.get('accepted'), f'{name} Q{q["number"]}')
                for value in q['accepted']:
                    self.assertIsNotNone(parse(value), f'{name} Q{q["number"]}: {value}')

    def test_every_question_carries_an_uzbek_explanation(self):
        import re
        cyrillic = re.compile(r'[Ѐ-ӿ]')
        letters = re.compile(r'\b(Choice [ABCD]|\([ABCD]\))\b')
        for name in self.FILES:
            for q in self._load(name).QUESTIONS:
                where = f'{name} Q{q["number"]}'
                self.assertTrue(q.get('explanation', '').strip(), where)
                self.assertTrue(q.get('skill'), where)
                # Uzbek here is Latin script; a Cyrillic letter is a keyboard slip.
                self.assertIsNone(cyrillic.search(q['explanation']), where)
                # display order is not the authored order anywhere it matters.
                self.assertIsNone(letters.search(q['explanation']), where)

    def test_multiple_choice_questions_have_four_distinct_choices(self):
        for name in self.FILES:
            for q in self._load(name).QUESTIONS:
                if q.get('answer_type') == 'grid':
                    continue
                where = f'{name} Q{q["number"]}'
                self.assertEqual(len(q['choices']), 4, where)
                self.assertEqual(len(set(q['choices'])), 4, where)
                self.assertIn(q['correct'], (1, 2, 3, 4), where)



class GmatScaleTests(TestCase):
    def test_section_runs_60_to_90_and_never_drops(self):
        for total in (20, 21, 23):
            scores = [gmatscore.section(raw, total) for raw in range(total + 1)]
            self.assertEqual((scores[0], scores[-1]), (60, 90))
            self.assertEqual(scores, sorted(scores))

    def test_total_runs_205_to_805_and_ends_in_5(self):
        self.assertEqual(gmatscore.total(60, 60, 60), 205)
        self.assertEqual(gmatscore.total(90, 90, 90), 805)
        for q, v, d in ((75, 80, 70), (81, 79, 84), (62, 88, 71)):
            self.assertEqual(gmatscore.total(q, v, d) % 10, 5)

    def test_sections_weigh_equally(self):
        self.assertEqual(gmatscore.total(90, 60, 60), gmatscore.total(60, 60, 90))


class GmatFlowTests(TestCase):
    """Build a miniature GMAT Focus exam and walk a taker through it."""

    def setUp(self):
        self.user = User.objects.create_user('gtaker', password='pw')
        self.panda, _ = Panda.objects.get_or_create(profile=self.user.profile)
        self.exam = Exam.objects.create(
            title='Test GMAT', language='english', exam_format='gmat',
            exam_number=9301, is_published=True,
        )
        for order, kind in enumerate(('quant', 'verbal', 'di'), start=1):
            ExamModule.objects.create(
                exam=self.exam, code=kind, kind=kind, stage=1, label=kind,
                minutes=45, order=order, calculator=(kind == 'di'))
            for n in range(1, 3):
                question = ExamQuestion.objects.create(
                    exam=self.exam, section=kind, number=n, question_text=f'{kind} {n}',
                    skill='Skill', explanation='izoh')
                for i in range(5):
                    ExamChoice.objects.create(question=question, text=f'c{i}', is_correct=(i == 0))
        self.client.login(username='gtaker', password='pw')

    def _attempt(self):
        return ExamAttempt.objects.filter(panda=self.panda, exam=self.exam).latest('start_time')

    def _submit(self, attempt, correct_count):
        data = {}
        for i, question in enumerate(attempt.current_module.questions().order_by('number')):
            choice = question.choices.filter(is_correct=(i < correct_count)).first()
            data[f'q{question.id}'] = choice.id
        return self.client.post(reverse('submit_section', args=[attempt.id]), data)

    def test_the_taker_chooses_the_section_order(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]), {'order': 'verbal,di,quant'})
        attempt = self._attempt()
        self.assertEqual(attempt.section_order, 'verbal,di,quant')
        self.assertEqual(attempt.current_module.kind, 'verbal')

    def test_a_forged_order_falls_back_to_the_default(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]), {'order': 'quant,quant,quant'})
        attempt = self._attempt()
        self.assertEqual(attempt.section_order, 'quant,verbal,di')
        self.assertEqual(attempt.current_module.kind, 'quant')

    def test_the_break_is_offered_twice_and_taken_once(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]), {'order': 'verbal,di,quant'})
        attempt = self._attempt()
        self._submit(attempt, 2)
        attempt.refresh_from_db()
        # Offered, not taken: status break, no clock yet, next section waiting.
        self.assertEqual((attempt.status, attempt.break_until, attempt.current_module.kind),
                         ('break', None, 'di'))
        page = self.client.get(reverse('exam_break', args=[attempt.id]))
        self.assertContains(page, 'Continue without a break')
        self.client.post(reverse('exam_break', args=[attempt.id]), {'action': 'skip'})
        attempt.refresh_from_db()
        self.assertEqual((attempt.status, attempt.current_module.kind, attempt.break_used),
                         ('in_progress', 'di', False))

        self._submit(attempt, 1)
        attempt.refresh_from_db()
        self.assertEqual(attempt.status, 'break')     # offered again after section 2
        self.client.post(reverse('exam_break', args=[attempt.id]), {'action': 'take'})
        attempt.refresh_from_db()
        self.assertTrue(attempt.break_used)
        self.assertIsNotNone(attempt.break_until)
        self.client.post(reverse('exam_break', args=[attempt.id]))   # "I'm ready"
        attempt.refresh_from_db()
        self.assertEqual((attempt.status, attempt.current_module.kind), ('in_progress', 'quant'))

    def test_no_second_break_once_one_was_taken(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]))
        attempt = self._attempt()
        self._submit(attempt, 2)
        self.client.post(reverse('exam_break', args=[attempt.id]), {'action': 'take'})
        self.client.post(reverse('exam_break', args=[attempt.id]))
        attempt.refresh_from_db()
        self._submit(attempt, 2)
        attempt.refresh_from_db()
        self.assertEqual(attempt.status, 'in_progress')   # straight into section 3

    def test_full_sitting_scores_three_sections_and_a_total(self):
        self.client.post(reverse('start_exam', args=[self.exam.id]), {'order': 'di,quant,verbal'})
        attempt = self._attempt()
        self._submit(attempt, 2)                                            # DI 2/2
        self.client.post(reverse('exam_break', args=[attempt.id]), {'action': 'skip'})
        attempt.refresh_from_db()
        self._submit(attempt, 1)                                            # Quant 1/2
        self.client.post(reverse('exam_break', args=[attempt.id]), {'action': 'skip'})
        attempt.refresh_from_db()
        response = self._submit(attempt, 0)                                 # Verbal 0/2
        attempt.refresh_from_db()
        self.assertTrue(attempt.is_completed)
        self.assertEqual((attempt.di_score, attempt.quant_score, attempt.verbal_score), (90, 75, 60))
        self.assertEqual(attempt.total_score, gmatscore.total(75, 60, 90))
        self.assertRedirects(response, reverse('exam_result', args=[attempt.id]))
        page = self.client.get(reverse('exam_result', args=[attempt.id]))
        self.assertTemplateUsed(page, 'exam/exam_result_gmat.html')
        self.assertContains(page, '205 – 805')

    def test_detail_page_offers_six_orders(self):
        page = self.client.get(reverse('exam_detail', args=[self.exam.id]))
        self.assertEqual(page.content.decode().count('<option value='), 6)


class GmatLoaderTests(LoadMockGateTests):
    def _gmat(self, **overrides):
        question = {'section': 'quant', 'number': 1, 'question_text': 'q',
                    'choices': ['a', 'b', 'c', 'd', 'e'], 'correct': 5,
                    'explanation': 'izoh', 'skill': 'Algebra'}
        question.update(overrides)
        return question

    def test_five_choices_load(self):
        self._run([self._gmat()], exam_format='gmat', exam_number=9302)
        self.assertEqual(ExamChoice.objects.filter(
            question__exam__exam_number=9302, is_correct=True).get().text, 'e')

    def test_four_choices_are_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._gmat(choices=['a', 'b', 'c', 'd'], correct=1)],
                      exam_format='gmat', exam_number=9303)

    def test_missing_explanation_is_refused(self):
        with self.assertRaises(CommandError):
            self._run([self._gmat(explanation='')], exam_format='gmat', exam_number=9304)



class GmatMockContentTests(TestCase):
    """The shape of every shipped GMAT mock, checked without the database.

    The scratchpad answer gates recompute the keys; this locks the blueprint so a later
    edit cannot drop a question, lose a choice, or put every key under the same letter.
    MOCKS is read from the files on disk, so mock 2 is covered the day it appears.
    """
    SECTIONS = [('quant', 21), ('verbal', 23), ('di', 20)]
    BLUEPRINTS = {
        'quant': {'Number Properties': 4, 'Percents, Ratios and Rates': 5, 'Algebra': 4,
                  'Word Problems': 4, 'Statistics and Counting': 4},
        'di': {'Data Sufficiency': 7, 'Table Analysis': 3, 'Graphics Interpretation': 4,
               'Two-Part Analysis': 3, 'Multi-Source Reasoning': 3},
    }

    def _numbers(self):
        import glob, os, re
        from django.conf import settings
        found = sorted(int(re.search(r'gmat(\d+)_quant', p).group(1)) for p in
                       glob.glob(os.path.join(settings.BASE_DIR, 'exam', 'data', 'gmat*_quant.py')))
        self.assertTrue(found, 'no GMAT mock data files found')
        return found

    def _load(self, name):
        import importlib.util, os
        from django.conf import settings
        path = os.path.join(settings.BASE_DIR, 'exam', 'data', f'{name}.py')
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_sections_sizes_choices_and_explanations(self):
        from collections import Counter
        for n in self._numbers():
            for section, size in self.SECTIONS:
                mod = self._load(f'gmat{n}_{section}')
                self.assertEqual(len(mod.QUESTIONS), size, f'gmat{n}_{section}')
                self.assertEqual(mod.EXAM_META['exam_number'], 300 + n)
                for q in mod.QUESTIONS:
                    self.assertEqual(q['section'], section)
                    self.assertEqual(len(set(q['choices'])), 5, (section, q['number']))
                    self.assertIn(q['correct'], range(1, 6))
                    self.assertTrue(q['explanation'].strip())
                positions = Counter(q['correct'] for q in mod.QUESTIONS)
                self.assertEqual(len(positions), 5, f'gmat{n}_{section}: some letter is never the key')
                if section in self.BLUEPRINTS:
                    self.assertEqual(Counter(q['skill'] for q in mod.QUESTIONS), self.BLUEPRINTS[section])

    def test_the_three_files_agree_on_the_exam_and_its_modules(self):
        for n in self._numbers():
            mods = [self._load(f'gmat{n}_{s}') for s, _ in self.SECTIONS]
            for mod in mods[1:]:
                self.assertEqual(mod.EXAM_META, mods[0].EXAM_META)
                self.assertEqual(mod.MODULES, mods[0].MODULES)
            minutes = {m['kind']: m['minutes'] for m in mods[0].MODULES}
            self.assertEqual(minutes, {'quant': 45, 'verbal': 45, 'di': 45})
            calc = {m['kind'] for m in mods[0].MODULES if m.get('calculator')}
            self.assertEqual(calc, {'di'})

    def test_data_sufficiency_keeps_the_standard_order(self):
        for n in self._numbers():
            mod = self._load(f'gmat{n}_di')
            for q in mod.QUESTIONS:
                if q['skill'] == 'Data Sufficiency':
                    self.assertEqual(q['choices'], mod.DS_CHOICES)
