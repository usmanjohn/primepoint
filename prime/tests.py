"""Tests for the hand-out kit — the printable business card and flyer.

These pieces are printed a hundred at a time and handed to strangers, so the
things worth guarding are the ones a screenshot would not catch: that the
pages stay public, that the Uzbek and English copy cannot drift apart, that a
QR file the templates reference actually exists on disk, and that the About
page can still frame them.
"""
from pathlib import Path

from django.conf import settings
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from prime import kit


class KitCopyTests(SimpleTestCase):
    """The copy lives in a dict, so the dict is what can go wrong."""

    def test_both_languages_carry_the_same_keys(self):
        # A key present in only one language renders as an empty string on
        # paper — a blank headline that nothing warns about.
        uz, en = set(kit.COPY['uz']), set(kit.COPY['en'])
        self.assertEqual(uz - en, set(), 'keys missing from the English copy')
        self.assertEqual(en - uz, set(), 'keys missing from the Uzbek copy')

    def test_no_value_is_empty(self):
        for lang, block in kit.COPY.items():
            for key, value in block.items():
                self.assertTrue(value, f'{lang}.{key} is empty')

    def test_every_course_and_track_is_written_in_both_languages(self):
        for row in kit.COURSES + kit.TRACKS:
            for lang in kit.LANGS:
                name, line = row[lang]
                self.assertTrue(name and line, f"{row['key']} is thin in {lang}")

    def test_pick_lang_falls_back_to_uzbek(self):
        self.assertEqual(kit.pick_lang('en'), 'en')
        self.assertEqual(kit.pick_lang('uz'), 'uz')
        for junk in (None, '', 'ru', 'EN', 'en-US', 'xx'):
            self.assertEqual(kit.pick_lang(junk), 'uz')

    def test_copy_for_resolves_courses_to_one_language(self):
        c = kit.copy_for('en')
        self.assertEqual(c['lang'], 'en')
        self.assertEqual(len(c['courses']), len(kit.COURSES))
        self.assertIn('English grammar', c['courses'][0]['line'])
        # ...and never leaks the other language's tuple into the template.
        self.assertIsInstance(c['courses'][0]['name'], str)

    def test_site_url_keeps_the_www(self):
        # The apex powerty.uz has no HTTPS certificate, and a printed QR
        # cannot be corrected afterwards.
        self.assertTrue(kit.SITE_URL.startswith('https://www.'))


class KitQrAssetTests(SimpleTestCase):
    """The QR files are committed, not generated at request time."""

    def test_referenced_qr_files_exist(self):
        static_dir = Path(settings.BASE_DIR) / 'static'
        for path in (kit.QR_SITE, kit.QR_TELEGRAM,
                     kit.QR_SITE_PNG, kit.QR_TELEGRAM_PNG):
            self.assertTrue((static_dir / path).is_file(), f'missing {path}')

    def test_site_qr_encodes_the_site_url(self):
        # segno writes the SVG; the alt text and the file must agree about
        # where a scan lands, so the URL is asserted here as documentation
        # of what was generated (regenerate with `manage.py gen_qr`).
        from prime.management.commands.gen_qr import TARGETS
        self.assertEqual(TARGETS['powerty-site'], kit.SITE_URL)


class KitViewTests(TestCase):
    def test_pages_are_public(self):
        for name in ('kit_card', 'kit_card_sheet', 'kit_flyer'):
            with self.subTest(name=name):
                r = self.client.get(reverse(name))
                self.assertEqual(r.status_code, 200)

    def test_default_language_is_uzbek_whatever_the_site_language(self):
        r = self.client.get(reverse('kit_flyer'), headers={'accept-language': 'en'})
        self.assertContains(r, kit.COPY['uz']['eyebrow'])
        self.assertNotContains(r, kit.COPY['en']['centre_title'])

    def test_lang_en_switches_the_piece_only(self):
        r = self.client.get(reverse('kit_flyer'), {'lang': 'en'})
        self.assertContains(r, kit.COPY['en']['eyebrow'])

    def test_unknown_lang_falls_back_rather_than_erroring(self):
        r = self.client.get(reverse('kit_card'), {'lang': 'ru'})
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, kit.COPY['uz']['card_slogan'])

    def test_bare_mode_drops_the_toolbar(self):
        full = self.client.get(reverse('kit_card'))
        bare = self.client.get(reverse('kit_card'), {'bare': '1'})
        # 'kt-bar' alone would match the body class `kt-bare`.
        self.assertContains(full, 'kt-bar kt-noprint')
        self.assertNotContains(bare, 'kt-bar kt-noprint')
        self.assertNotContains(bare, 'window.print()')
        self.assertContains(bare, 'kt-card')

    def test_card_sheet_prints_ten_cards(self):
        r = self.client.get(reverse('kit_card_sheet'))
        self.assertEqual(r.content.decode().count('kt-card kt-card--front'), 10)

    def test_card_sheet_back_side_prints_ten_backs(self):
        r = self.client.get(reverse('kit_card_sheet'), {'side': 'back'})
        body = r.content.decode()
        self.assertEqual(body.count('kt-card kt-card--back'), 10)
        self.assertNotIn('kt-card kt-card--front', body)

    def test_pieces_may_be_framed_by_our_own_pages(self):
        # The About page previews them in an iframe and the project default
        # is X-Frame-Options: DENY.
        r = self.client.get(reverse('kit_flyer'), {'bare': '1'})
        self.assertEqual(r.headers['X-Frame-Options'], 'SAMEORIGIN')

    def test_flyer_carries_both_qr_codes_and_the_address(self):
        body = self.client.get(reverse('kit_flyer')).content.decode()
        # `{% static %}` hashes the filename under the manifest storage, so
        # match the stem rather than the path in `kit`.
        self.assertIn('powerty-site', body)
        self.assertIn('powerty-telegram', body)
        self.assertIn(kit.SITE_URL, body)     # the QR's own alt text
        self.assertIn(kit.SITE_HOST, body)

    def test_about_page_links_the_kit(self):
        body = self.client.get(reverse('about')).content.decode()
        for name in ('kit_card', 'kit_card_sheet', 'kit_flyer'):
            self.assertIn(reverse(name), body)


class PlatformStatsTests(TestCase):
    """The pieces print live counts; an empty database must not break them."""

    def test_stats_are_whole_numbers_and_the_rounded_one_is_formatted(self):
        from django.core.cache import cache
        from prime.views import _platform_stats
        cache.clear()
        stats = _platform_stats()
        for key in ('lessons', 'questions', 'readings', 'courses'):
            self.assertIsInstance(stats[key], int)
        # An empty test database must not print "0,000+" on the flyer.
        self.assertEqual(stats['questions_round'], '0')
        cache.clear()

    def test_question_count_rounds_down_to_the_thousand(self):
        from django.core.cache import cache
        from unittest.mock import patch
        from prime.views import _platform_stats
        for count, printed in ((0, '0'), (999, '999'), (1000, '1,000+'),
                               (11839, '11,000+')):
            with self.subTest(count=count):
                cache.clear()
                with patch('prime.views.PracticeQuestion.objects') as qs:
                    qs.filter.return_value.count.return_value = count
                    self.assertEqual(_platform_stats()['questions_round'], printed)
        cache.clear()
