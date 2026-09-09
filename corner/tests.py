# -*- coding: utf-8 -*-
"""Corner regression tests."""
import html
import re

from django.test import SimpleTestCase

from corner.management.commands.gen_corner_audio import RUBY_RT_RE, TAG_RE


def narrated(markup):
    """What the TTS narrator actually receives for a block of story markup."""
    return html.unescape(TAG_RE.sub('', RUBY_RT_RE.sub('', markup)))


class FuriganaIsNotNarratedTests(SimpleTestCase):
    """A <ruby> carries a word AND its reading; the narrator must read it once.

    Prime Japanese is the first shelf to use furigana. Before this fix, stripping
    tags naively turned "<ruby>日本語<rt>にほんご</rt></ruby>" into "日本語にほんご"
    and every kanji word was spoken twice.
    """

    def test_reading_is_dropped_and_base_text_kept(self):
        out = narrated('<ruby>日本語<rt>にほんご</rt></ruby>')
        self.assertEqual(out, '日本語')

    def test_whole_sentence(self):
        out = narrated('<p>わたしは<ruby>日本語<rt>にほんご</rt></ruby>の'
                       '<ruby>先生<rt>せんせい</rt></ruby>です。</p>')
        self.assertEqual(out, 'わたしは日本語の先生です。')
        self.assertNotIn('にほんご', out)

    def test_rp_fallback_parens_are_dropped_too(self):
        out = narrated('<ruby>山<rp>(</rp><rt>やま</rt><rp>)</rp></ruby>')
        self.assertEqual(out, '山')

    def test_multiple_ruby_in_one_block(self):
        out = narrated('<ruby>私<rt>わたし</rt></ruby>は'
                       '<ruby>学生<rt>がくせい</rt></ruby>です')
        self.assertEqual(out, '私は学生です')

    def test_markup_without_ruby_is_untouched(self):
        out = narrated('<p><span class="cn-word" data-tr="non">빵</span>을</p>')
        self.assertEqual(out, '빵을')
