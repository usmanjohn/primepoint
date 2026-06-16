"""Template filters that make LaTeX math survive the rich-text editor.

CKEditor stores content as HTML. When an author pastes math from an AI tool
(or uses the superscript / colour buttons), exponents and other markup end up
as HTML *inside* the ``$...$`` delimiters, e.g. ``$4x<sup>2</sup> - 3x$``.

MathJax matches its delimiters on plain text nodes and cannot span across HTML
tags, so it silently gives up and the raw ``$`` signs are shown to the reader.

``render_math`` walks only the text *between* math delimiters and rewrites it
into clean LaTeX:

* ``<sup>2</sup>``  -> ``^{2}``
* ``<sub>n</sub>``  -> ``_{n}``
* any other tag     -> removed
* HTML entities     -> decoded (``&amp;`` -> ``&``, ``&nbsp;`` -> space)

Content outside math delimiters is left completely untouched, so a non-math
superscript like ``1<sup>st</sup>`` keeps working normally.
"""
import html as _html
import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def _clean_math(inner: str) -> str:
    """Turn the HTML found inside a math region into plain LaTeX."""
    inner = re.sub(r'<sup[^>]*>(.*?)</sup>', r'^{\1}', inner, flags=re.I | re.S)
    inner = re.sub(r'<sub[^>]*>(.*?)</sub>', r'_{\1}', inner, flags=re.I | re.S)
    inner = re.sub(r'<br\s*/?>', ' ', inner, flags=re.I)
    inner = re.sub(r'<[^>]+>', '', inner)          # drop any remaining tags
    inner = _html.unescape(inner)                  # &amp; -> &, &nbsp; -> \xa0
    inner = inner.replace('\xa0', ' ')             # non-breaking space -> space
    return inner


def _sub(pattern, open_d, close_d, text, flags=0):
    return re.sub(
        pattern,
        lambda m: f'{open_d}{_clean_math(m.group(1))}{close_d}',
        text,
        flags=flags,
    )


@register.filter
def render_math(value):
    """Sanitize the HTML inside every math region so MathJax can render it.

    Handles display math (``$$...$$``, ``\\[...\\]``) and inline math
    (``$...$``, ``\\(...\\)``). The delimiters are preserved — MathJax still
    does the actual typesetting in the browser.
    """
    s = str(value)

    # Display math first so its inner '$' (if any) is consumed before the
    # single-dollar pass runs.
    s = _sub(r'\$\$(.+?)\$\$', '$$', '$$', s, flags=re.S)
    s = _sub(r'\\\[(.+?)\\\]', r'\[', r'\]', s, flags=re.S)
    s = _sub(r'\\\((.+?)\\\)', r'\(', r'\)', s, flags=re.S)

    # Inline single-dollar math: opening '$' not preceded/followed by '$' or a
    # backslash, content with no further '$', closing '$' not doubled.
    s = re.sub(
        r'(?<![\$\\])\$(?!\$)([^$]+?)\$(?!\$)',
        lambda m: f'${_clean_math(m.group(1))}$',
        s,
    )
    return mark_safe(s)
