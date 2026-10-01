"""Regressions for the two bugs that silenced the channel 22–30 September 2026.

Both were invisible from the code: the first only fires on a question whose
explanation happens to contain an inequality, and the second only shows up as
subjects quietly missing from a night's posts.
"""
from unittest.mock import patch

from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from telegrambot import api, content
from telegrambot.models import TelegramPost


class QuizExplanationTests(SimpleTestCase):
    """A poll explanation is plain text and must be sent as plain text.

    `content.to_text` ends in `html.unescape`, so `&lt;` arrives here as a bare
    `<`. Asking Telegram to parse that as HTML gets the whole poll refused —
    which is what took the channel down.
    """

    def test_send_quiz_does_not_ask_telegram_to_parse_the_explanation(self):
        with patch.object(api, 'call', return_value={}) as called:
            api.send_quiz('Q', ['a', 'b'], 0, explanation='x < 6 boʻlsa')
        payload = called.call_args.kwargs
        self.assertNotIn('explanation_parse_mode', payload)
        self.assertEqual(payload['explanation'], 'x < 6 boʻlsa')

    def test_an_inequality_survives_untouched(self):
        # The exact shape that failed: question #6322's explanation.
        explanation = 'x < 6. 2x < 12, keyin 2 ga boʻlamiz.'
        with patch.object(api, 'call', return_value={}) as called:
            api.send_quiz('Q', ['a', 'b'], 0, explanation=explanation)
        self.assertEqual(called.call_args.kwargs['explanation'], explanation)

    def test_to_text_really_does_produce_a_bare_left_angle(self):
        # If this ever stops being true the bug above changes shape; the test
        # above would still pass while meaning something different.
        self.assertEqual(content.to_text('<p>x &lt; 6</p>'), 'x < 6')


class RotationResilienceTests(TestCase):
    """One subject failing must not take the rest of the rotation with it."""

    def setUp(self):
        from masters.models import Master
        from people.models import Profile
        from practice.models import (Practice, PracticeChoice, PracticeQuestion,
                                     Subject)

        user = User.objects.create_user('m', password='x')
        profile = Profile.objects.get(user=user) if Profile.objects.filter(user=user).exists() \
            else Profile.objects.create(user=user)
        master = Master.objects.create(profile=profile, name='M', description='d')

        self.questions = {}
        for subject_name in ('English', '한국어'):
            subject = Subject.objects.create(name=subject_name)
            practice = Practice.objects.create(
                master=master, title=f'{subject_name} test', subject=subject,
                is_published=True)
            question = PracticeQuestion.objects.create(
                practice=practice, question_text='Q?', explanation='because')
            PracticeChoice.objects.create(question=question, text='a', is_correct=True)
            PracticeChoice.objects.create(question=question, text='b', is_correct=False)
            self.questions[subject_name] = question

    def test_a_failing_subject_does_not_stop_the_ones_after_it(self):
        sent = []

        def fake_send(text, options, correct, explanation='', buttons=None):
            # English is first in ROTATION; make it fail the way Telegram does.
            if len(sent) == 0:
                sent.append('FAILED')
                raise api.TelegramError("sendPoll: can't parse entities")
            sent.append('ok')
            return {'message_id': 1, 'chat': {'id': -1}}

        with patch.object(api, 'is_configured', return_value=True), \
             patch.object(api, 'refuse_local_database'), \
             patch.object(api, 'send_quiz', side_effect=fake_send), \
             patch('telegrambot.management.commands.post_daily_quiz.GAP_SECONDS', 0):
            with self.assertRaises(CommandError) as caught:
                call_command('post_daily_quiz', '--each-subject')

        # The second subject went out even though the first blew up...
        self.assertEqual(sent, ['FAILED', 'ok'])
        self.assertEqual(TelegramPost.objects.filter(kind=TelegramPost.QUIZ).count(), 1)
        # ...and the run still ends red, naming what failed.
        self.assertIn('Ingliz tili', str(caught.exception))

    def test_a_clean_run_posts_every_subject_that_has_a_question(self):
        with patch.object(api, 'is_configured', return_value=True), \
             patch.object(api, 'refuse_local_database'), \
             patch.object(api, 'send_quiz',
                          return_value={'message_id': 1, 'chat': {'id': -1}}), \
             patch('telegrambot.management.commands.post_daily_quiz.GAP_SECONDS', 0):
            call_command('post_daily_quiz', '--each-subject')

        posted = TelegramPost.objects.filter(
            kind=TelegramPost.QUIZ, posted_at__date=timezone.localdate())
        self.assertEqual(posted.count(), 2)


class AbroadDeadlinePostTests(TestCase):
    """The channel follows the site's rule: never a confident wrong date."""

    def setUp(self):
        import datetime
        from abroad.models import Deadline, Scholarship
        self.day = datetime.date(2026, 10, 1)
        s = Scholarship.objects.create(
            slug='x', name='X', country='C', country_uz='C', summary='s', summary_uz='s',
            official_url='https://x.org/', last_checked=self.day, flag='🏳')
        mk = lambda **kw: Deadline.objects.create(
            scholarship=s, label_uz=kw.pop('label'), label='L', source_url='https://x.org/',
            last_checked=kw.pop('checked', self.day), **kw)
        self.soon = mk(label='Tez', closes=self.day + datetime.timedelta(days=5))
        self.later = mk(label='Keyin', closes=self.day + datetime.timedelta(days=40))
        self.estimate = mk(label='Taxmin', closes=self.day + datetime.timedelta(days=50), is_estimate=True)
        self.stale = mk(label='Eski', closes=self.day + datetime.timedelta(days=20),
                        checked=self.day - datetime.timedelta(days=400))
        self.far = mk(label='Uzoq', closes=self.day + datetime.timedelta(days=200))

    def _run(self):
        from io import StringIO
        from unittest import mock
        out = StringIO()
        with mock.patch('abroad.models.today', lambda: self.day), \
             mock.patch('telegrambot.management.commands.post_abroad_deadlines.tashkent_today',
                        lambda: self.day):
            call_command('post_abroad_deadlines', '--dry-run', stdout=out)
        return out.getvalue()

    def test_digest_includes_only_trustworthy_dates(self):
        out = self._run()
        self.assertIn('Tez', out)
        self.assertIn('Keyin', out)
        self.assertIn('taxminan', out)            # the estimate, without a countdown
        self.assertNotIn('Eski', out)             # stale — never posted
        self.assertNotIn('Uzoq', out)             # beyond the 60-day horizon

    def test_reminder_only_for_confirmed_deadline_within_a_week(self):
        out = self._run()
        self.assertIn('[abroad_reminder] %d' % self.soon.id, out)
        self.assertNotIn('[abroad_reminder] %d' % self.later.id, out)
        self.assertNotIn('[abroad_reminder] %d' % self.estimate.id, out)

    def test_already_posted_this_month_and_reminded_is_quiet(self):
        TelegramPost.objects.create(kind=TelegramPost.ABROAD_MONTH, object_id=202610)
        TelegramPost.objects.create(kind=TelegramPost.ABROAD_REMINDER, object_id=self.soon.id)
        self.assertIn('Nothing due.', self._run())
