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
