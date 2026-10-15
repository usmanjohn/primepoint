from django.test import SimpleTestCase

from tutorial.templatetags.math_extras import render_math


class RenderMathFilterTests(SimpleTestCase):
    def test_superscript_inside_inline_math_becomes_caret(self):
        html = '<p>$4x<sup>2</sup> - 3x + 2$</p>'
        out = render_math(html)
        self.assertIn('$4x^{2} - 3x + 2$', out)
        self.assertNotIn('<sup>', out)

    def test_subscript_inside_inline_math_becomes_underscore(self):
        out = render_math('$a<sub>1</sub> + a<sub>2</sub>$')
        self.assertIn('$a_{1} + a_{2}$', out)

    def test_display_math_is_cleaned(self):
        out = render_math('$$x<sup>2</sup> + y<sup>2</sup>$$')
        self.assertIn('$$x^{2} + y^{2}$$', out)

    def test_paren_delimiters_cleaned(self):
        out = render_math(r'\(4x<sup>2</sup>\)')
        self.assertIn(r'\(4x^{2}\)', out)

    def test_entities_inside_math_are_decoded(self):
        # &nbsp; -> space, &amp; -> & ; stray inline tags stripped
        out = render_math('<p>$2&nbsp;+&nbsp;7&nbsp;=&nbsp;9$</p>')
        self.assertIn('$2 + 7 = 9$', out)

    def test_strips_other_inline_tags_inside_math(self):
        out = render_math('$2<strong>x</strong> + 9$')
        self.assertIn('$2x + 9$', out)

    def test_non_math_superscript_is_left_untouched(self):
        # Superscript OUTSIDE any math region must not be rewritten.
        html = '<p>This is the 1<sup>st</sup> example.</p>'
        out = render_math(html)
        self.assertIn('1<sup>st</sup>', out)
        self.assertNotIn('^{st}', out)

    def test_plain_text_math_passes_through(self):
        html = '<p>$2x^2 + 2x + 9$</p>'
        out = render_math(html)
        self.assertIn('$2x^2 + 2x + 9$', out)

    def test_surrounding_html_is_preserved(self):
        html = '<h2>Step</h2><p>Combine: $2x<sup>2</sup>$ done.</p>'
        out = render_math(html)
        self.assertIn('<h2>Step</h2>', out)
        self.assertIn('$2x^{2}$', out)


class MoneyIsNotMathTests(SimpleTestCase):
    """Two prices in a lesson used to be read as one inline-math region, and
    everything between them — paragraphs, lists, whole sections — was stripped
    of its markup (SAT-3, SAT-5, SAT-10 and eight older lessons)."""

    def test_prices_across_paragraphs_are_left_alone(self):
        html = ('<p class="pe-bad">12 — bir metr $12.</p>'
                '<p class="pe-good">har bir <b>qoʻshimcha</b> metr $12 ga oshiradi.</p>')
        out = render_math(html)
        self.assertIn('<p class="pe-good">', out)
        self.assertIn('<b>qoʻshimcha</b>', out)
        self.assertEqual(html, out)

    def test_prices_in_one_sentence_are_left_alone(self):
        html = '<p>Tikuvchi $12 oladi va ustiga bir martalik $25 qoʻyadi.</p>'
        self.assertEqual(html, render_math(html))

    def test_a_very_long_region_is_not_treated_as_math(self):
        html = '<p>$' + ('word ' * 60) + '$</p>'
        self.assertEqual(html, render_math(html))

    def test_real_inline_math_still_works_beside_prices(self):
        html = '<p>The fee is $45 and \\(x<sup>2</sup>\\) is math.</p>'
        out = render_math(html)
        self.assertIn(r'\(x^{2}\)', out)
        self.assertIn('$45', out)

    def test_region_that_opens_mid_markup_is_left_alone(self):
        # SAT-49 shipped this shape: two prices with a sentence between them,
        # the first one landing inside a <strong>.
        html = '<p>2·12 = <strong>$24</strong> and 3·12 = <strong>$36</strong>.</p>'
        out = render_math(html)
        self.assertEqual(html, out)
        self.assertEqual(out.count('<strong>'), 2)


# ── Admin-only (staff_only) playlists, e.g. "Kapital" ────────────────────────
import os
import tempfile

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from tutorial.models import Tutorial, TutorialPlaylist


class StaffOnlyPlaylistTests(TestCase):
    DATA = (
        "PLAYLIST = {'title': 'Kapital', 'category': 'programming', 'staff_only': True}\n"
        "TUTORIALS = [\n"
        "  {'title': '1. Setup', 'renamed_from': ['Old setup'], 'category': 'programming',\n"
        "   'order': 1, 'content': '<p>views</p>'},\n"
        "  {'title': '2. Home', 'category': 'programming', 'order': 2, 'content': '<p>home</p>'},\n"
        "]\n"
    )

    def setUp(self):
        self.admin = User.objects.create_user('boss', password='x', is_staff=True)
        self.pupil = User.objects.create_user('pupil', password='x')
        # an existing public lesson under its old title — must be renamed, not duplicated
        self.old = Tutorial.objects.create(title='Old setup', author=self.admin,
                                           category='programming', content='<p>old</p>')
        fd, self.path = tempfile.mkstemp(suffix='.py')
        with os.fdopen(fd, 'w') as f:
            f.write(self.DATA)
        call_command('import_tutorials', self.path, author='boss', republish=True, stdout=open(os.devnull, 'w'))

    def tearDown(self):
        os.remove(self.path)

    def test_import_hides_and_renames(self):
        pl = TutorialPlaylist.objects.get(title='Kapital')
        self.assertFalse(pl.is_published)
        self.assertFalse(Tutorial.objects.filter(is_published=True, title__in=['1. Setup', '2. Home']).exists())
        self.old.refresh_from_db()
        self.assertEqual(self.old.title, '1. Setup')          # same row, new title
        self.assertEqual(Tutorial.objects.filter(author=self.admin).count(), 2)

    def test_pupil_and_guest_get_404(self):
        pl = TutorialPlaylist.objects.get(title='Kapital')
        for client_user in (None, self.pupil):
            if client_user:
                self.client.force_login(client_user)
            self.assertEqual(self.client.get(reverse('playlist_detail', args=[pl.pk])).status_code, 404)
            self.assertEqual(self.client.get(reverse('tutorial_detail', args=[self.old.pk])).status_code, 404)
            self.assertNotContains(self.client.get(reverse('playlist_list')), 'Kapital')
            self.client.logout()

    def test_admin_sees_everything(self):
        self.client.force_login(self.admin)
        pl = TutorialPlaylist.objects.get(title='Kapital')
        self.assertContains(self.client.get(reverse('playlist_list')), 'Kapital')
        r = self.client.get(reverse('playlist_detail', args=[pl.pk]))
        self.assertContains(r, '1. Setup')
        self.assertContains(r, '2. Home')
        self.assertEqual(self.client.get(reverse('tutorial_detail', args=[self.old.pk])).status_code, 200)
