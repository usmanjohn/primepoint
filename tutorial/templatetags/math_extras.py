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

⚠️ A ``$`` is also a dollar sign. In a lesson full of prices ("$12 … $25") the
naive reading of ``$...$`` swallows everything between two amounts — including
the markup — and the rest of the page collapses into one paragraph. That is a
real bug this filter shipped (SAT-3, SAT-5, SAT-10 and eight older lessons, all
of them money, none of them LaTeX). So a candidate region is REFUSED when it
looks like prose rather than maths:

* it crosses a block boundary (``</p>``, ``<div>``, ``<h3>``, ``<li>`` …) —
  no inline formula spans two paragraphs;
* it is longer than ``_MAX_MATH`` characters.

A refused region is left exactly as the author wrote it.
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


# A math region that contains one of these is not a formula — it is prose that
# happens to sit between two dollar signs.
_BLOCK = re.compile(
    r'</?(?:p|div|h[1-6]|ul|ol|li|table|thead|tbody|tr|td|th|figure|figcaption'
    r'|details|summary|blockquote|section|article|br|hr)\b',
    re.I,
)
_MAX_MATH = 200


_TAG = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)[^>]*?(/?)>')
_VOID = {'br', 'img', 'hr', 'input', 'wbr'}


def _tags_balanced(inner: str) -> bool:
    """True when every tag inside the region opens and closes within it.

    A real formula carries whole tags (``$2<strong>x</strong> + 9$``). A region
    that begins in the middle of somebody's markup — ``$24</strong> and 3·12 =
    <strong>$`` — is two prices with a sentence between them, and rewriting it
    destroys the pairing.
    """
    stack = []
    for closing, name, selfclose in _TAG.findall(inner):
        name = name.lower()
        if name in _VOID or selfclose:
            continue
        if closing:
            if not stack or stack.pop() != name:
                return False
        else:
            stack.append(name)
    return not stack


def _looks_like_math(inner: str) -> bool:
    """False for prose caught between two dollar signs (usually two prices)."""
    return (len(inner) <= _MAX_MATH
            and not _BLOCK.search(inner)
            and _tags_balanced(inner))


def _sub(pattern, open_d, close_d, text, flags=0):
    def repl(m):
        inner = m.group(1)
        if not _looks_like_math(inner):
            return m.group(0)          # leave the author's text alone
        return f'{open_d}{_clean_math(inner)}{close_d}'

    return re.sub(pattern, repl, text, flags=flags)


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
    s = _sub(r'(?<![\$\\])\$(?!\$)([^$]+?)\$(?!\$)', '$', '$', s)
    return mark_safe(s)
