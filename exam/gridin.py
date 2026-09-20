"""Grading for digital-SAT student-produced responses (grid-ins).

The pupil types into a box instead of picking a letter, so the grader has to
understand what they typed. College Board's own rules, which this implements:

  * an answer may be an integer, a decimal or a fraction — 2/3, .6667 and 0.667
    are all the same answer;
  * a mixed number is NOT accepted (5/4, never "1 1/4") — the real test reads
    "1 1/4" as eleven fourths, so we refuse it outright rather than guess;
  * no %, no $, no commas — a comma is a WRONG answer, not a typo to forgive.
    Prime SAT breaks that habit on purpose, so the mock has to bite too;
  * a value that does not terminate must be given to enough digits to fill the
    answer box: truncated or rounded, but not cut short at two digits.

That last rule is the only fuzzy one. We accept an approximation within 0.15%
of the true value when the pupil wrote three decimal places or four
significant digits. So 2/3 accepts .6666, .6667, .666 and 0.667 and refuses
.67; 100/3 accepts 33.33 and refuses 33.3 — exactly like the test.
"""
import re
from fractions import Fraction

# 1.5e-3 rather than 1e-3 so that a truncation like 0.666 for 2/3, which sits
# exactly on 0.001, is not rejected by floating-point dust.
REL_TOLERANCE = Fraction(15, 10000)

_INNER_SPACE_RE = re.compile(r'\s')
_NUMBER_RE = re.compile(r'^-?(\d+\.?\d*|\.\d+)$')
_FRACTION_RE = re.compile(r'^(-?\d+)/(-?\d+)$')


def normalize(raw):
    """Trim the outside only. A comma, a %, a $ or an inner space stays illegal."""
    if raw is None:
        return ''
    return str(raw).strip()


def parse(raw):
    """Typed answer -> Fraction, or None if it is not a legal grid-in entry."""
    text = normalize(raw)
    if not text or _INNER_SPACE_RE.search(text):
        return None
    match = _FRACTION_RE.match(text)
    if match:
        numerator, denominator = int(match.group(1)), int(match.group(2))
        if denominator == 0:
            return None
        return Fraction(numerator, denominator)
    if _NUMBER_RE.match(text):
        try:
            return Fraction(text)
        except (ValueError, ZeroDivisionError):
            return None
    return None


def _is_decimal(raw):
    text = normalize(raw)
    return bool(_NUMBER_RE.match(text)) and '.' in text


def _significant_digits(raw):
    """Digits that carry information — leading zeros and the point do not."""
    digits = normalize(raw).lstrip('-').replace('.', '')
    return len(digits.lstrip('0')) or (1 if digits else 0)


def _decimal_places(raw):
    text = normalize(raw)
    return len(text.split('.', 1)[1]) if '.' in text else 0


def _fills_the_box(raw):
    """The pupil gave enough of a non-terminating value to count.

    Three decimal places OR four significant digits. Written as two tests
    because they catch different shapes: .666 is three places and only three
    significant digits, while 33.33 is four significant digits in two places.
    """
    return _decimal_places(raw) >= 3 or _significant_digits(raw) >= 4


def _close_enough(typed_value, target, raw):
    if not _is_decimal(raw) or not _fills_the_box(raw):
        return False
    if target == 0:
        return typed_value == 0
    return abs(typed_value - target) / abs(target) <= REL_TOLERANCE


def grid_answer_matches(typed, accepted):
    """True when `typed` is one of the `accepted` answer strings, by value."""
    value = parse(typed)
    if value is None:
        return False
    for candidate in accepted:
        target = parse(candidate)
        if target is None:
            continue
        if value == target or _close_enough(value, target, typed):
            return True
    return False
