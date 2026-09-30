"""Tests for the workbook — the fourth leg.

Three things here would ship broken silently and hurt a pupil:
  · the marker calling a right answer wrong (grading, appeals, the importer's
    self-check that every key passes its own marker);
  · a republish wiping out the answers pupils already typed;
  · a stale PDF being offered after the worksheet was edited.
"""
import glob
import importlib.util
import re
from pathlib import Path

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.urls import reverse

from homework.models import Homework, HomeworkAssignment
from masters.models import Master
from panda.models import Panda
from tutorial.models import Tutorial
from workbook import grading, pdfs
from workbook.management.commands.import_workbook import validate
from workbook.models import AnswerAppeal, ItemResponse, TaskItem, Workbook, WorkbookAttempt
from workbook.views import accept_answer

DATA_DIR = Path(settings.BASE_DIR) / 'workbook' / 'management' / 'commands'


def _load(path):
    spec = importlib.util.spec_from_file_location('_wb', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.WORKBOOKS


class GradingTests(TestCase):
    def test_exact_and_trailing_punctuation(self):
        for typed in ['학생입니다', ' 학생입니다. ', '학생입니다!', '학생입니다?']:
            with self.subTest(typed=typed):
                self.assertEqual(grading.mark(typed, ['학생입니다']), grading.RIGHT)

    def test_spacing_only_is_right_with_a_note(self):
        """Right Korean with wrong 띄어쓰기 is right — the pupil gets a note."""
        self.assertEqual(grading.mark('저는학생입니다', ['저는 학생입니다']), grading.NEARLY)
        self.assertEqual(grading.mark('저는 학생 입니다', ['저는 학생입니다']), grading.NEARLY)
        self.assertTrue(grading.is_correct(grading.NEARLY))

    def test_wrong_and_empty(self):
        self.assertEqual(grading.mark('의사이 아닙니다', ['의사가 아닙니다']), grading.WRONG)
        self.assertEqual(grading.mark('   ', ['가']), grading.EMPTY)

    def test_compatibility_jamo_survive_normalisation(self):
        """NFC, never NFKC: a typed ㅎ must still equal the key's ㅎ."""
        self.assertEqual(grading.mark('ㅎ ㅏ ㄴ', ['ㅎㅏㄴ'], ignore=' +'), grading.RIGHT)
        self.assertEqual(grading.mark('ㅎ+ㅏ+ㄴ', ['ㅎ ㅏ ㄴ'], ignore=' +'), grading.RIGHT)

    def test_decomposed_hangul_is_the_same_answer(self):
        import unicodedata
        typed = unicodedata.normalize('NFD', '한국')
        self.assertEqual(grading.mark(typed, ['한국']), grading.RIGHT)

    def test_uzbek_apostrophes_fold(self):
        self.assertEqual(grading.mark("o'ng tomoniga", ['oʻng tomoniga']), grading.RIGHT)


def make_workbook(title='PK-10: Test'):
    author = User.objects.create_user('author', password='x')
    tutorial = Tutorial.objects.create(title=title, author=author, category='korean',
                                       content='<p>x</p>')
    entry = {
        'tutorial': title,
        'tasks': [
            {'section': 'B', 'kind': 'gap', 'instruction': '<p>i</p>', 'items': [
                {'stem': '저는 ___.', 'answers': ['학생입니다'], 'explanation': '<p>e</p>'},
                {'stem': '의사___ 아닙니다.', 'answers': ['가'], 'explanation': '<p>e</p>'},
            ]},
            {'section': 'D', 'kind': 'write', 'instruction': '<p>i</p>', 'items': [
                {'stem': '<p>s</p>', 'model_answer': '<p>m</p>', 'checklist': ['a', 'b']},
            ]},
            {'section': 'E', 'kind': 'mission', 'instruction': '<p>i</p>', 'items': [
                {'stem': '<p>go</p>'},
            ]},
        ],
    }
    return tutorial, entry


class ImporterTests(TestCase):
    def setUp(self):
        self.tutorial, self.entry = make_workbook()

    def _import(self, entries, **kw):
        path = Path(self.tmp) / '_wb_test.py'
        path.write_text(f'WORKBOOKS = {entries!r}\n', encoding='utf-8')
        call_command('import_workbook', str(path), **kw)

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        import tempfile
        cls._dir = tempfile.TemporaryDirectory()
        cls.tmp = cls._dir.name

    @classmethod
    def tearDownClass(cls):
        cls._dir.cleanup()
        super().tearDownClass()

    def test_import_and_expect_items(self):
        with self.assertRaises(CommandError):
            self._import([self.entry], expect_items=99, stdout=open('/dev/null', 'w'))
        self._import([self.entry], expect_items=4, stdout=open('/dev/null', 'w'))
        wb = Workbook.objects.get(tutorial=self.tutorial)
        self.assertEqual(wb.tasks.count(), 3)
        self.assertEqual(wb.data_hash, pdfs.data_hash(self.entry))

    def test_republish_keeps_pupils_answers_and_remarks_them(self):
        self._import([self.entry], stdout=open('/dev/null', 'w'))
        pupil = User.objects.create_user('p', password='x')
        wb = Workbook.objects.get(tutorial=self.tutorial)
        item = TaskItem.objects.get(task__workbook=wb, order=2, task__kind='gap')
        attempt = WorkbookAttempt.objects.create(user=pupil, workbook=wb)
        response = ItemResponse.objects.create(attempt=attempt, item=item, text='이')
        response.regrade(); response.save()
        self.assertFalse(response.is_correct)

        # A (deliberately silly) correction of the key: the response must
        # survive the republish and be re-marked against the new key.
        self.entry['tasks'][0]['items'][1]['answers'] = ['이']
        self._import([self.entry], republish=True, stdout=open('/dev/null', 'w'))
        response.refresh_from_db()
        self.assertTrue(response.is_correct)

    def test_validate_catches_broken_items(self):
        bad = {'tutorial': 'x', 'tasks': [
            {'section': 'B', 'kind': 'gap', 'instruction': 'i', 'items': [{'stem': 'no gap', 'answers': ['a']}]},
            {'section': 'B', 'kind': 'pick', 'instruction': 'i', 'items': [{'stem': 's', 'options': ['a', 'b'], 'answers': ['c']}]},
            {'section': 'Z', 'kind': 'write', 'instruction': 'i', 'items': [{'stem': 's'}]},
        ]}
        problems = ' | '.join(validate(bad))
        self.assertIn('needs a ___ gap', problems)
        self.assertIn('not among the options', problems)
        self.assertIn('bad section', problems)
        self.assertIn('needs a model_answer', problems)


class PupilFlowTests(TestCase):
    def setUp(self):
        self.tutorial, entry = make_workbook()
        import tempfile, os
        fd, path = tempfile.mkstemp(suffix='.py')
        os.write(fd, f'WORKBOOKS = {[entry]!r}\n'.encode('utf-8')); os.close(fd)
        call_command('import_workbook', path, stdout=open('/dev/null', 'w'))
        os.remove(path)
        self.wb = Workbook.objects.get(tutorial=self.tutorial)
        self.url = reverse('workbook_detail', args=[self.wb.pk])
        self.pupil = User.objects.create_user('pupil', password='pw')
        Panda.objects.create(profile=self.pupil.profile)
        self.items = {i.task.section + str(i.order): i for i in TaskItem.objects.filter(task__workbook=self.wb)}

    def test_guest_reads_but_cannot_submit(self):
        self.assertEqual(self.client.get(self.url).status_code, 200)
        r = self.client.post(self.url, {'section': 'B'})
        self.assertIn(reverse('login'), r['Location'])
        self.assertEqual(self.client.get(reverse('workbook_worksheet', args=[self.wb.pk])).status_code, 200)

    def test_gap_inputs_keep_their_size_inside_a_block(self):
        """The include flag must not be called `block`: inside {% block %}
        Django's context already has one, and every box went full width."""
        page = self.client.get(self.url).content.decode()
        self.assertIn('wb-input--m', page)

    def test_templates_carry_no_script(self):
        for f in glob.glob(str(Path(settings.BASE_DIR) / 'workbook/templates/workbook/*.html')):
            with self.subTest(f=f):
                self.assertNotIn('<script', open(f).read())

    def _submit_all(self):
        b1, b2 = self.items['B1'], self.items['B2']
        self.client.post(self.url, {'section': 'B', f'i{b1.pk}': '학생 입니다', f'i{b2.pk}': '이'})
        d = self.items['D1']
        self.client.post(self.url, {'section': 'D', f'i{d.pk}': '저는 학생입니다.', f'c{d.pk}': ['0', '1', '7']})
        e = self.items['E1']
        return self.client.post(self.url, {'section': 'E', f'd{e.pk}': '1'})

    def test_marking_completion_points_and_homework(self):
        master_user = User.objects.create_user('teacher', password='pw')
        master = Master.objects.create(profile=master_user.profile, name='T', description='d')
        hw = Homework.objects.create(master=master, title='hw')
        hw.workbooks.add(self.wb)
        assignment = HomeworkAssignment.objects.create(homework=hw, panda=self.pupil.profile.panda)

        self.client.login(username='pupil', password='pw')
        self._submit_all()
        attempt = WorkbookAttempt.objects.get(user=self.pupil, workbook=self.wb)
        b1 = ItemResponse.objects.get(attempt=attempt, item=self.items['B1'])
        self.assertEqual(b1.verdict, grading.NEARLY)           # spacing only
        self.assertTrue(b1.is_correct)
        self.assertEqual((attempt.correct, attempt.total), (1, 2))
        self.assertIsNotNone(attempt.completed_at)
        self.assertEqual(attempt.points_awarded, 15)
        self.assertEqual(ItemResponse.objects.get(attempt=attempt, item=self.items['D1']).checks, [0, 1])
        assignment.refresh_from_db()
        self.assertEqual(assignment.status, 'submitted')
        self.pupil.profile.panda.refresh_from_db()
        self.assertEqual(self.pupil.profile.panda.rating, 15)

        # The page renders the verdicts and the model answer after writing.
        page = self.client.get(self.url).content.decode()
        self.assertIn('wb-item--wrong', page)
        self.assertIn('wb-model', page)                        # model answer after writing

    def test_appeal_then_accept_remarks_everyone(self):
        self.client.login(username='pupil', password='pw')
        self._submit_all()
        b2 = self.items['B2']
        self.client.post(reverse('workbook_appeal', args=[b2.pk]))
        appeal = AnswerAppeal.objects.get(item=b2)
        self.assertEqual(appeal.text, '이')

        accept_answer(b2, appeal.text)
        attempt = WorkbookAttempt.objects.get(user=self.pupil)
        self.assertEqual((attempt.correct, attempt.total), (2, 2))
        self.assertEqual(attempt.points_awarded, 20)

    def test_review_is_for_teachers_only(self):
        url = reverse('workbook_review', args=[self.wb.pk, self.pupil.pk])
        stranger = User.objects.create_user('stranger', password='pw')
        self.client.login(username='stranger', password='pw')
        self.assertEqual(self.client.get(url).status_code, 403)

        master = Master.objects.create(profile=stranger.profile, name='T', description='d')
        self.pupil.profile.panda.masters.add(master)
        self.assertEqual(self.client.get(url).status_code, 200)


class CommittedDataTests(TestCase):
    """The data files in the repo, checked as they are."""

    def test_every_data_file_validates(self):
        for path in glob.glob(str(DATA_DIR / '_workbook_*.py')):
            for entry in _load(path):
                with self.subTest(workbook=entry['tutorial']):
                    self.assertEqual(validate(entry), [])

    def test_committed_pdfs_match_their_data(self):
        """Regenerate with gen_worksheet_pdfs after changing a workbook — a
        stale PDF is never offered, but it should not be committed either."""
        manifest = pdfs.read_manifest()
        for path in glob.glob(str(DATA_DIR / '_workbook_*.py')):
            for entry in _load(path):
                code = re.match(r'([A-Z]+-\d+)', entry['tutorial']).group(1)
                with self.subTest(code=code):
                    self.assertEqual(manifest.get(code), pdfs.data_hash(entry),
                                     f'{code}: run `python manage.py gen_worksheet_pdfs --only {code}`')
                    self.assertTrue((pdfs.PDF_DIR / pdfs.filename(code)).exists())

    def test_stale_pdf_is_not_offered(self):
        tutorial, _entry = make_workbook(title='PK-9: X')
        wb = Workbook.objects.create(tutorial=tutorial, data_hash='not-the-manifest-hash')
        self.assertIsNone(pdfs.pdf_url(wb))
