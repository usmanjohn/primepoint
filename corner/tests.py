# -*- coding: utf-8 -*-
"""Corner regression tests."""
import html
import re

from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase

from corner.models import Collection, Story, StoryGrammar, StoryQuestion, Subject

from corner.management.commands.gen_corner_audio import (
    RUBY_RT_RE, SPEAKER_PREFIX_RE, SPEAKER_TAG_RE, TAG_RE,
)


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


class SpeakerNameIsNotNarratedTests(SimpleTestCase):
    """A dialogue paragraph's speaker tag names the voice; it is not a line of the story.

    Two bugs let Japanese names through, both found while previewing PJ-25…27:
      * SPEAKER_TAG_RE was anchored at "<strong>", but _chunks() splits the body on
        </p>, so every chunk but the first still opens with its own "<p>";
      * SPEAKER_PREFIX_RE, the fallback that caught the Korean names in practice,
        only started on Latin or Hangul, never on kana or kanji.
    Together they meant "アフソナ:" was spoken aloud in every Prime Japanese reading.
    """

    def spoken(self, markup):
        """One body block, exactly as _chunks() hands it to the narrator."""
        text = SPEAKER_TAG_RE.sub('', markup, count=1)
        text = html.unescape(TAG_RE.sub('', RUBY_RT_RE.sub('', text)))
        text = re.sub(r'\s+', ' ', text).strip()
        return SPEAKER_PREFIX_RE.sub('', text, count=1).strip()

    def test_japanese_speaker_tag_inside_a_paragraph(self):
        self.assertEqual(
            self.spoken('<p><strong>アフソナ:</strong> クロは'
                        '<ruby>速<rt>はや</rt></ruby>いですか。</p>'),
            'クロは速いですか。')

    def test_korean_speaker_tag_still_stripped(self):
        self.assertEqual(
            self.spoken('<p><strong>벡조드:</strong> 안녕하세요?</p>'),
            '안녕하세요?')

    def test_latin_speaker_tag_still_stripped(self):
        self.assertEqual(self.spoken('<p><strong>Mike:</strong> Hello there.</p>'),
                         'Hello there.')

    def test_plain_text_japanese_name_without_markup(self):
        self.assertEqual(self.spoken('<p>シェルベク: はい、'
                                     '<ruby>走<rt>はし</rt></ruby>ります。</p>'),
                         'はい、走ります。')

    def test_narration_without_a_speaker_is_untouched(self):
        self.assertEqual(
            self.spoken('<p><ruby>四時<rt>よじ</rt></ruby>に'
                        '<ruby>家<rt>いえ</rt></ruby>へ'
                        '<ruby>帰<rt>かえ</rt></ruby>ります。</p>'),
            '四時に家へ帰ります。')

    def test_a_bold_word_mid_sentence_is_not_a_speaker_tag(self):
        self.assertEqual(
            self.spoken('<p>これは<strong>大事</strong>です。</p>'),
            'これは大事です。')


class StoryQuizRendersAuthoredHtmlTests(TestCase):
    """A reading's question text, choices, grammar pattern and examples are HTML.

    They are authored by staff through import_corner (same trust as story.body),
    and the print sheet always rendered them — but story_detail.html escaped them.
    Prime Japanese is the first shelf whose questions carry <ruby> furigana, so
    pupils were shown raw "<ruby>教室<rt>きょうしつ</rt></ruby>" in every quiz.
    """

    def setUp(self):
        author = User.objects.create_user('sensei', password='x')
        subject = Subject.objects.create(name='Japanese', slug='japanese')
        collection = Collection.objects.create(
            subject=subject, title='Test Readings', slug='test-readings')
        self.story = Story.objects.create(
            collection=collection, author=author, title='てすと', slug='tesuto',
            body='<p><ruby>本<rt>ほん</rt></ruby>があります。</p>', is_published=True)
        StoryGrammar.objects.create(
            story=self.story,
            pattern='〜が<ruby>好<rt>す</rt></ruby>きです',
            meaning='«… yoqadi» — <b>が</b> oladi.',
            examples=['<ruby>音楽<rt>おんがく</rt></ruby>が<ruby>好<rt>す</rt></ruby>きです。'])
        StoryQuestion.objects.create(
            story=self.story, order=1,
            text='<ruby>教室<rt>きょうしつ</rt></ruby>は どこですか。',
            choices=['<ruby>図書館<rt>としょかん</rt></ruby>の<ruby>中<rt>なか</rt></ruby>です',
                     '<ruby>学校<rt>がっこう</rt></ruby>の<ruby>前<rt>まえ</rt></ruby>です',
                     'あそこです', 'ここです'],
            answer=0, explanation='<b>図書館</b>の中です。')

    def page(self):
        c = self.story.collection
        url = f'/corner/{c.subject.slug}/{c.slug}/{self.story.slug}/'
        return self.client.get(url).content.decode()

    def test_question_text_is_rendered_not_escaped(self):
        body = self.page()
        self.assertIn('<ruby>教室<rt>きょうしつ</rt></ruby>は どこですか。', body)
        self.assertNotIn('&lt;ruby&gt;', body)

    def test_choices_are_rendered_not_escaped(self):
        self.assertIn('<ruby>図書館<rt>としょかん</rt></ruby>の'
                      '<ruby>中<rt>なか</rt></ruby>です', self.page())

    def test_grammar_pattern_and_examples_are_rendered(self):
        body = self.page()
        self.assertIn('〜が<ruby>好<rt>す</rt></ruby>きです', body)
        self.assertIn('<ruby>音楽<rt>おんがく</rt></ruby>が'
                      '<ruby>好<rt>す</rt></ruby>きです。', body)
