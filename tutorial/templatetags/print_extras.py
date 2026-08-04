"""Filters that adapt stored lesson HTML for paper.

The lessons are written for the screen, where some of the content is deliberately
hidden until the reader asks for it. On a handout there is nothing to click, so
those parts have to be unfolded before printing.
"""
import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# <details ...>  ->  <details open ...>. Matches the tag name only, so an
# attribute whose value happens to contain "details" is left alone, and an
# element that is already open is not given a second `open`.
_DETAILS_RE = re.compile(r'<details(?![^>]*\bopen\b)', re.I)


@register.filter
def open_details(value):
    """Unfold every <details> block in the given HTML.

    Prime English / Prime Korean lessons hide their answers in
    `<details class="pe-reveal">` — about six per lesson. CSS cannot open a
    <details>, so on a print sheet they would come out as a row of empty
    "tap to see" strips. Adding the `open` attribute is the only reliable fix
    across browsers; `print_sheet.css` then styles them as plain answer boxes.
    """
    return mark_safe(_DETAILS_RE.sub('<details open', value or ''))
