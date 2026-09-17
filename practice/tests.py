# -*- coding: utf-8 -*-
"""Practice regression tests."""
from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase

from masters.models import Master
from panda.models import Panda
from practice.models import (
    Practice, PracticeAttempt, PracticeChoice, PracticeQuestion, Subject,
)
from telegrambot.content import to_text

RUBY = '<ruby>父<rt>ちち</rt></ruby>さん'


class ChoicesRenderAuthoredHtmlTests(TestCase):
    """A choice's text is HTML, exactly like the question text beside it.

    Choices are authored by staff through import_practices (same trust as
    question_text and explanation, which have always been rendered with |safe),
    and the print sheet rendered them — but take/result/review escaped them.
    Prime Japanese is the first bank whose choices carry <ruby> furigana, so
    pupils were shown raw "<ruby>父<rt>ちち</rt></ruby>" in every answer.
    """

    def setUp(self):
        self.pupil = User.objects.create_user('pupil', password='x')
        self.panda = Panda.objects.create(profile=self.pupil.profile)
        teacher = User.objects.create_user('sensei', password='x')
        self.master = Master.objects.create(
            profile=teacher.profile, name='Sensei', description='-',
            subject='日本語', is_approved=True)
        self.teacher = teacher

        practice = Practice.objects.create(
            master=self.master, title='PJ-20 mashq',
            subject=Subject.objects.create(name='日本語'), is_published=True)
        question = PracticeQuestion.objects.create(
            practice=practice, order=1,
            question_text='Begonaga oʻz otangiz haqida gapiryapsiz. Qaysi soʻz?',
            explanation='<ruby>父<rt>ちち</rt></ruby> — oʻz otang.')
        PracticeChoice.objects.create(question=question, text=RUBY, is_correct=False)
        PracticeChoice.objects.create(
            question=question, text='<ruby>父<rt>ちち</rt></ruby>', is_correct=True)
        self.practice, self.question = practice, question

        self.attempt = PracticeAttempt.objects.create(
            panda=self.panda, practice=practice)

    def body(self, url, who='pupil'):
        self.client.force_login(self.pupil if who == 'pupil' else self.teacher)
        return self.client.get(url).content.decode()

    def assertRendered(self, body):
        self.assertIn(RUBY, body)
        self.assertNotIn('&lt;ruby&gt;', body)

    def test_take_practice(self):
        self.assertRendered(self.body(f'/practice/attempt/{self.attempt.id}/'))

    def test_result_page(self):
        self.attempt.status = 'completed'
        self.attempt.save()
        self.assertRendered(
            self.body(f'/practice/attempt/{self.attempt.id}/result/'))

    def test_master_review_page(self):
        self.attempt.status = 'completed'
        self.attempt.save()
        self.assertRendered(
            self.body(f'/practice/attempt/{self.attempt.id}/review/', who='master'))


class FuriganaIsNotPostedTwiceTests(SimpleTestCase):
    """A Telegram poll option is plain text: the reading must be dropped, not glued on.

    Adding 日本語 to the daily rotation made this reachable — naive tag stripping
    turned "<ruby>父<rt>ちち</rt></ruby>" into "父ちち" in every Japanese poll.
    Same rule as corner's RUBY_RT_RE for TTS.
    """

    def test_reading_is_dropped_and_kanji_kept(self):
        self.assertEqual(to_text('<ruby>父<rt>ちち</rt></ruby>さん'), '父さん')

    def test_rp_parens_go_too(self):
        self.assertEqual(to_text('<ruby>山<rp>(</rp><rt>やま</rt><rp>)</rp></ruby>'), '山')

    def test_sentence(self):
        self.assertEqual(
            to_text('<p>わたしは<ruby>日本語<rt>にほんご</rt></ruby>を'
                    '<ruby>勉強<rt>べんきょう</rt></ruby>します。</p>'),
            'わたしは日本語を勉強します。')

    def test_markup_without_ruby_is_untouched(self):
        self.assertEqual(to_text('<p>x<sup>2</sup> = 9</p>'), 'x² = 9')
