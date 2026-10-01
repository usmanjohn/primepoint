"""Tests for the Study-abroad section.

The promise that matters most: a pupil must never be shown a confident wrong
date. So most of what is tested here is how a deadline presents itself —
open, closed, estimated, stale — and that the importer refuses a dated fact
without a source.
"""
import datetime
import glob
from pathlib import Path
from unittest import mock

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

from abroad import models as m
from abroad.management.commands.import_abroad import load, validate
from abroad.models import ChecklistItem, ChecklistTick, Deadline, Guide, Scholarship

DATA_DIR = Path(settings.BASE_DIR) / 'abroad' / 'management' / 'commands'
TODAY = datetime.date(2026, 10, 1)
# Import order from toc_abroad.txt — the full pages after the cards file, so a
# card can never overwrite a full page.
DATA_FILES = ('_abroad_gks.py', '_abroad_scholarships_2.py', '_abroad_mext.py',
              '_abroad_turkiye_hungary.py', '_abroad_chevening_csc.py',
              '_abroad_eyuf_daad_fulbright.py',
              '_abroad_guides_1.py', '_abroad_guides_2.py')


def import_all():
    with open('/dev/null', 'w') as sink:
        for name in DATA_FILES:
            call_command('import_abroad', str(DATA_DIR / name), stdout=sink)


def make_scholarship(**kw):
    defaults = dict(slug='gks', name='GKS', country='South Korea', country_uz='Janubiy Koreya',
                    summary='Korea pays.', summary_uz='Koreya toʻlaydi.',
                    official_url='https://www.studyinkorea.go.kr/', last_checked=TODAY,
                    levels='bachelor,master', languages='korean,english')
    defaults.update(kw)
    return Scholarship.objects.create(**defaults)


def make_deadline(s, **kw):
    defaults = dict(scholarship=s, label='Round', label_uz='Bosqich', closes=TODAY + datetime.timedelta(days=5),
                    source_url='https://example.org/', last_checked=TODAY)
    defaults.update(kw)
    return Deadline.objects.create(**defaults)


@mock.patch('abroad.models.today', lambda: TODAY)
class DeadlineStateTests(TestCase):
    def setUp(self):
        self.s = make_scholarship()

    def test_open_counts_down(self):
        d = make_deadline(self.s, opens=TODAY - datetime.timedelta(days=10))
        self.assertEqual((d.state, d.days_left), ('open', 5))

    def test_closed(self):
        d = make_deadline(self.s, closes=TODAY - datetime.timedelta(days=1))
        self.assertEqual(d.state, 'closed')

    def test_upcoming(self):
        d = make_deadline(self.s, opens=TODAY + datetime.timedelta(days=3),
                          closes=TODAY + datetime.timedelta(days=20))
        self.assertEqual(d.state, 'upcoming')

    def test_estimate_never_counts_down(self):
        d = make_deadline(self.s, is_estimate=True, closes=TODAY + datetime.timedelta(days=100))
        self.assertEqual(d.state, 'estimate')

    def test_stale_fact_says_check(self):
        d = make_deadline(self.s, last_checked=TODAY - datetime.timedelta(days=400))
        self.assertEqual(d.state, 'stale')
        self.client.cookies['django_language'] = 'en'
        html = self.client.get('/abroad/scholarships/gks/').content.decode()
        self.assertIn('check the date on the official site', html)
        self.assertNotIn('days left', html)


class TashkentDateTests(TestCase):
    def test_today_is_tashkent_not_utc(self):
        # 20:00 UTC on 30 September is already 1 October in Tashkent (UTC+5).
        fake_now = datetime.datetime(2026, 9, 30, 20, 0, tzinfo=datetime.timezone.utc)
        with mock.patch('django.utils.timezone.now', return_value=fake_now):
            self.assertEqual(m.today(), datetime.date(2026, 10, 1))


class ImporterTests(TestCase):
    def test_refuses_missing_language_or_source(self):
        problems = ' | '.join(validate({
            'GUIDES': [{'slug': 'x', 'title': 'T', 'summary': 'S', 'body': 'B',
                        'title_uz': '', 'summary_uz': 'S', 'body_uz': 'B'}],
            'DEADLINES': [{'label': 'L', 'label_uz': 'L', 'closes': '2026-10-06',
                           'source_url': 'http://x.org', 'last_checked': ''}],
            'SCHOLARSHIPS': [{'slug': 's', 'country': 'C', 'country_uz': 'C', 'summary': 'S',
                              'summary_uz': 'S', 'official_url': 'https://x.org', 'last_checked': '2026-10-01',
                              'usual_period': 'Sep', 'usual_period_uz': ''}],
        }))
        self.assertIn('missing title_uz', problems)
        self.assertIn('source_url must be https', problems)
        self.assertIn('last_checked is required', problems)
        self.assertIn('usual_period and usual_period_uz must both be filled', problems)

    def test_every_committed_data_file_validates(self):
        for path in sorted(glob.glob(str(DATA_DIR / '_abroad_*.py'))):
            with self.subTest(path=Path(path).name):
                self.assertEqual(validate(load(path)), [])

    def test_committed_files_import_cleanly(self):
        import_all()
        self.assertEqual(Guide.objects.count(), 10)
        self.assertEqual(Scholarship.objects.count(), 10)
        # Every scholarship is a full page now; a card reappearing means a
        # data file downgraded one on republish.
        self.assertFalse(Scholarship.objects.filter(depth='card').exists())
        # Every data file on disk is in the import order above.
        on_disk = {Path(p).name for p in glob.glob(str(DATA_DIR / '_abroad_*.py'))}
        self.assertEqual(on_disk, set(DATA_FILES))
        # Checklist rows keep their ids across a re-import, so ticks survive.
        first = ChecklistItem.objects.get(target='gks-u', order=1).pk
        with open('/dev/null', 'w') as sink:
            call_command('import_abroad', str(DATA_DIR / '_abroad_gks.py'), republish=True, stdout=sink)
        self.assertEqual(ChecklistItem.objects.get(target='gks-u', order=1).pk, first)


class PageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        import_all()

    def test_guest_reads_everything_in_both_languages(self):
        urls = ['/abroad/', '/abroad/guides/documents/', '/abroad/scholarships/',
                '/abroad/scholarships/gks/', '/abroad/samples/gks-personal-statement/',
                '/abroad/samples/gks-study-plan/planner/', '/abroad/universities/',
                '/abroad/checklist/', '/abroad/scholarships/mext/', '/abroad/scholarships/turkiye/',
                '/abroad/scholarships/hungary/', '/abroad/samples/mext-research-plan/',
                '/abroad/universities/?country=Japan', '/abroad/checklist/?target=mext-r',
                '/abroad/checklist/?target=turkiye', '/abroad/checklist/?target=hungary',
                '/abroad/scholarships/chevening/', '/abroad/scholarships/csc/',
                '/abroad/samples/chevening-leadership-essay/', '/abroad/checklist/?target=chevening',
                '/abroad/scholarships/eyuf/', '/abroad/scholarships/daad/', '/abroad/scholarships/fulbright/',
                '/abroad/checklist/?target=eyuf', '/abroad/checklist/?target=daad', '/abroad/checklist/?target=fulbright',
                '/abroad/scholarships/erasmus/', '/abroad/checklist/?target=erasmus',
                '/abroad/samples/chevening-networking-essay/', '/abroad/samples/chevening-career-plan-essay/',
                '/abroad/samples/hungary-motivation-letter/', '/abroad/samples/hungary-motivation-letter/planner/']
        # The language comes from the cookie (LocaleMiddleware), as for a visitor.
        for lang, title in (('uz', 'Hujjatlar, tarjima va apostil'),
                            ('en', 'Documents, translation and apostille')):
            self.client.cookies['django_language'] = lang
            for url in urls:
                with self.subTest(lang=lang, url=url):
                    self.assertEqual(self.client.get(url).status_code, 200)
            page = self.client.get('/abroad/guides/documents/').content.decode()
            self.assertIn(f'<h1 class="ab-head__title">{title}</h1>', page)

    def test_finder_filters(self):
        def names(qs):
            html = self.client.get('/abroad/scholarships/' + qs).content.decode()
            return {s for s in ('Chevening', 'MEXT', 'Fulbright', 'GKS') if f'>{s} <small>' in html}
        self.assertEqual(names('?level=bachelor') & {'Chevening', 'Fulbright'}, set())
        self.assertIn('Chevening', names('?level=master&lang=english'))
        self.assertNotIn('MEXT', names('?lang=korean'))
        self.assertIn('GKS', names('?lang=none'))

    def test_checklist_is_per_user_and_needs_login(self):
        item = ChecklistItem.objects.filter(target='gks-u').first()
        r = self.client.post('/abroad/checklist/', {'target': 'gks-u', 'item': [item.pk]})
        self.assertEqual(r.status_code, 302)
        self.assertEqual(ChecklistTick.objects.count(), 0)

        a = User.objects.create_user('a', password='pw')
        User.objects.create_user('b', password='pw')
        self.client.login(username='a', password='pw')
        self.client.post('/abroad/checklist/', {'target': 'gks-u', 'item': [item.pk]})
        self.assertTrue(ChecklistTick.objects.filter(user=a, item=item).exists())
        self.client.login(username='b', password='pw')
        page = self.client.get('/abroad/checklist/?target=gks-u').content.decode()
        self.assertNotIn(f'value="{item.pk}" checked', page)

        # Unticking removes it.
        self.client.login(username='a', password='pw')
        self.client.post('/abroad/checklist/', {'target': 'gks-u'})
        self.assertFalse(ChecklistTick.objects.filter(user=a).exists())

    def test_country_tabs_appear_once_each(self):
        page = self.client.get('/abroad/universities/').content.decode()
        self.assertEqual(page.count('?country=Japan"'), 1)

    def test_templates_carry_no_script(self):
        for f in glob.glob(str(Path(settings.BASE_DIR) / 'abroad/templates/abroad/*.html')):
            with self.subTest(f=f):
                self.assertNotIn('<script', open(f).read())

    def test_search_finds_both_languages(self):
        from prime.search import search_platform
        for q in ('GKS', 'apostil', 'Motivation'):
            with self.subTest(q=q):
                groups, _total = search_platform(q)
                self.assertIn('abroad', [g['key'] for g in groups])
