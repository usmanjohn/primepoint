"""Tests for the Logic Arena.

The section makes one promise that is easy to break by accident and impossible
to apologise for afterwards: **between submitting and the reveal date, nothing
anywhere tells the solver whether they were right.** Most of what is tested here
is that promise, from three different directions — the puzzle page, the listing
card, and the points total on the progress page, which is the sneaky one.
"""
import datetime
import re

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from logic.models import LogicPuzzle, LogicSubmission, normalise


def make_puzzle(number=1, opens_days_ago=3, reveals_in_days=4, **kwargs):
    now = timezone.now()
    defaults = dict(
        title=f'Puzzle {number}', title_uz=f'Jumboq {number}',
        body='<p>body</p>', body_uz='<p>matn</p>',
        solution='<p>solution</p>', solution_uz='<p>yechim</p>',
        answer_key='17', accepted='seventeen\n17 minutes',
        category='numbers', difficulty=2,
        opens_at=now - datetime.timedelta(days=opens_days_ago),
        reveal_at=now + datetime.timedelta(days=reveals_in_days),
    )
    defaults.update(kwargs)
    return LogicPuzzle.objects.create(number=number, **defaults)


class AnswerCheckingTests(TestCase):
    """What counts as the same answer when a teenager types it on a phone."""

    def setUp(self):
        self.puzzle = make_puzzle(answer_key='17', accepted='seventeen\no‘n yetti')

    def test_exact_match(self):
        self.assertTrue(self.puzzle.accepts('17'))

    def test_ignores_case_spacing_and_punctuation(self):
        for typed in ['  17  ', '17.', 'Seventeen', 'seven teen', 'SEVENTEEN!']:
            with self.subTest(typed=typed):
                self.assertTrue(self.puzzle.accepts(typed))

    def test_numeric_equivalence(self):
        """"17.0" and "17,0" are the same number as "17"."""
        self.assertTrue(self.puzzle.accepts('17.0'))
        self.assertTrue(self.puzzle.accepts('17,0'))

    def test_uzbek_apostrophes_are_folded(self):
        """oʻ, o‘ and o' are the same letter to a pupil, so they must be here."""
        for typed in ['oʻn yetti', "o'n yetti", 'o‘n yetti']:
            with self.subTest(typed=typed):
                self.assertTrue(self.puzzle.accepts(typed))

    def test_wrong_answers_are_wrong(self):
        for typed in ['19', '', '   ', 'eighteen', '1']:
            with self.subTest(typed=typed):
                self.assertFalse(self.puzzle.accepts(typed))

    def test_normalise_does_not_merge_different_numbers(self):
        self.assertNotEqual(normalise('17'), normalise('171'))


class SealedAnswerTests(TestCase):
    """The core promise: no verdict before the reveal date."""

    def setUp(self):
        self.user = User.objects.create_user('afsona', password='x')
        self.puzzle = make_puzzle(reveals_in_days=4)
        self.client.force_login(self.user)
        self.url = reverse('logic_puzzle', kwargs={'slug': self.puzzle.slug})

    def test_submitting_stores_a_graded_but_sealed_answer(self):
        self.client.post(self.url, {'answer': '17', 'reasoning': 'because'})
        submission = LogicSubmission.objects.get(user=self.user, puzzle=self.puzzle)
        self.assertTrue(submission.is_correct)   # graded at once…
        self.assertTrue(submission.sealed)
        self.assertEqual(submission.points_awarded, self.puzzle.points)

    def test_the_page_never_shows_the_verdict_before_the_reveal(self):
        self.client.post(self.url, {'answer': '17'})
        page = self.client.get(self.url).content.decode()
        self.assertIn('sealed', page.lower())
        # …but nothing on the page says so.
        self.assertNotIn('Correct!', page)
        self.assertNotIn('lg-status--correct', page)
        self.assertNotIn('lg-status--wrong', page)

    def test_a_wrong_sealed_answer_looks_exactly_like_a_right_one(self):
        """Two users, one right and one wrong, must get indistinguishable pages.

        Everything that legitimately differs is masked first — the CSRF token,
        the username, and the answer each of them typed, which is their own and
        which they already know. What is left must be identical, because any
        remaining difference would be the verdict leaking.
        """
        # Distinctive sentinels, so masking them cannot collide with a colour
        # code or an asset hash elsewhere in the page.
        self.puzzle.answer_key = 'RIGHTSENTINEL'
        self.puzzle.accepted = ''
        self.puzzle.save()

        def masked(page, username, answer):
            page = re.sub(r'value="[A-Za-z0-9]{32,}"', 'value="CSRF"', page)
            return (page.replace(username, 'USER')
                        .replace(username[:2].upper(), 'XX')
                        .replace(answer, 'ANSWER'))

        self.client.post(self.url, {'answer': 'RIGHTSENTINEL'})
        right = masked(self.client.get(self.url).content.decode(),
                       'afsona', 'RIGHTSENTINEL')

        other = User.objects.create_user('jasur', password='x')
        self.client.force_login(other)
        self.client.post(self.url, {'answer': 'WRONGSENTINEL'})
        wrong = masked(self.client.get(self.url).content.decode(),
                       'jasur', 'WRONGSENTINEL')

        self.assertEqual(right, wrong)

    def test_the_solution_is_not_in_the_page_before_the_reveal(self):
        """Neither the reasoning nor the answer key may be served early.

        The key is given a distinctive value here because a bare number like
        "17" turns up by chance inside hashed asset filenames, which would make
        the assertion pass or fail for reasons that have nothing to do with the
        puzzle.
        """
        self.puzzle.solution = '<p>THE SECRET REASONING</p>'
        self.puzzle.answer_key = 'ANSWERKEYSENTINEL'
        self.puzzle.save()
        page = self.client.get(self.url).content.decode()
        self.assertNotIn('THE SECRET REASONING', page)
        self.assertNotIn('ANSWERKEYSENTINEL', page)

    def test_resubmitting_edits_the_same_envelope(self):
        self.client.post(self.url, {'answer': '19'})
        self.client.post(self.url, {'answer': '17'})
        submissions = LogicSubmission.objects.filter(user=self.user, puzzle=self.puzzle)
        self.assertEqual(submissions.count(), 1)
        self.assertEqual(submissions.first().answer, '17')

    def test_an_empty_answer_is_refused(self):
        self.client.post(self.url, {'answer': '   '})
        self.assertFalse(LogicSubmission.objects.filter(user=self.user).exists())


class RevealedPuzzleTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('sherbek', password='x')
        self.puzzle = make_puzzle(opens_days_ago=14, reveals_in_days=-7)
        self.client.force_login(self.user)
        self.url = reverse('logic_puzzle', kwargs={'slug': self.puzzle.slug})

    def test_a_late_solve_is_worth_half(self):
        self.client.post(self.url, {'answer': '17'})
        submission = LogicSubmission.objects.get(user=self.user)
        self.assertFalse(submission.sealed)
        self.assertEqual(submission.points_awarded, self.puzzle.points * 0.5)

    def test_the_verdict_and_solution_appear(self):
        self.client.post(self.url, {'answer': '17'})
        page = self.client.get(self.url).content.decode()
        self.assertIn('lg-status--correct', page)
        self.assertIn('solution', page.lower())

    def test_editing_a_late_answer_never_makes_it_sealed(self):
        """The sealed flag is decided once, at first submission."""
        self.client.post(self.url, {'answer': '19'})
        self.client.post(self.url, {'answer': '17'})
        self.assertFalse(LogicSubmission.objects.get(user=self.user).sealed)


class UpcomingPuzzleTests(TestCase):
    def test_the_body_of_an_unopened_puzzle_is_not_served(self):
        puzzle = make_puzzle(opens_days_ago=-5, reveals_in_days=12,
                             body='<p>NOT YET VISIBLE</p>')
        page = self.client.get(
            reverse('logic_puzzle', kwargs={'slug': puzzle.slug})).content.decode()
        self.assertNotIn('NOT YET VISIBLE', page)
        self.assertIn('Not open yet', page)

    def test_an_unopened_puzzle_is_not_in_search(self):
        from prime.search import search_platform
        make_puzzle(opens_days_ago=-5, title='Findable Later')
        groups, total = search_platform('Findable Later')
        self.assertEqual(total, 0)


class GuestTests(TestCase):
    def setUp(self):
        self.puzzle = make_puzzle()
        self.url = reverse('logic_puzzle', kwargs={'slug': self.puzzle.slug})

    def test_a_guest_may_read_the_puzzle(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log in to send an answer')

    def test_a_guest_cannot_submit(self):
        response = self.client.post(self.url, {'answer': '17'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(LogicSubmission.objects.exists())


class ProgressLeakTests(TestCase):
    """The subtle one: points must not tick up before the reveal.

    A pupil who submits on Monday and watches their points total go up has been
    told the answer, just through a different page.
    """

    def setUp(self):
        self.user = User.objects.create_user('nodira', password='x')

    def _points(self):
        from prime.progress import total_points
        return total_points(self.user)

    def test_a_correct_sealed_answer_earns_nothing_yet(self):
        sealed = make_puzzle(number=1, reveals_in_days=5)
        LogicSubmission.objects.create(puzzle=sealed, user=self.user, answer='17',
                                       is_correct=True, sealed=True,
                                       points_awarded=sealed.points)
        self.assertEqual(self._points(), 0)

    def test_the_same_answer_pays_out_once_the_puzzle_is_revealed(self):
        puzzle = make_puzzle(number=2, opens_days_ago=14, reveals_in_days=-1)
        LogicSubmission.objects.create(puzzle=puzzle, user=self.user, answer='17',
                                       is_correct=True, sealed=True,
                                       points_awarded=puzzle.points)
        self.assertEqual(self._points(), puzzle.points)


class ScheduleTests(TestCase):
    def test_state_follows_the_clock_with_nothing_to_switch_on(self):
        now = timezone.now()
        day = datetime.timedelta(days=1)
        cases = [
            (now + day, now + 8 * day, LogicPuzzle.UPCOMING),
            (now - day, now + 6 * day, LogicPuzzle.OPEN),
            (now - 8 * day, now - day, LogicPuzzle.REVEALED),
        ]
        for i, (opens, reveals, expected) in enumerate(cases, start=10):
            with self.subTest(expected=expected):
                puzzle = make_puzzle(number=i, opens_at=opens, reveal_at=reveals)
                self.assertEqual(puzzle.state, expected)

    def test_points_default_to_the_difficulty(self):
        from logic.models import DIFFICULTY_POINTS
        puzzle = make_puzzle(number=20, difficulty=5)
        self.assertEqual(puzzle.points, DIFFICULTY_POINTS[5])
