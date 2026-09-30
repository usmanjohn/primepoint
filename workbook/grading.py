"""Marking a typed answer — the fairness core of the workbook.

A multiple-choice question can only be marked right or wrong. A typed answer
can be *nearly* right in ways that are not the pupil's fault, and a marker
that calls those wrong teaches the pupil to distrust the marker. So typed
answers are compared in two passes:

    strict  NFC-normalised, case-folded, whitespace collapsed, trailing
            full stop / question mark / exclamation dropped.
            A match here is simply right.

    loose   the same, with every space and every , . ? ! removed.
            A match here is still RIGHT — the Korean is correct — but the
            pupil is told to look at the spacing (띄어쓰기) or punctuation.
            Marking "저는학생입니다" wrong would punish the grammar the lesson
            taught for a keyboard habit it did not.

Anything else is wrong, and the pupil can appeal (`AnswerAppeal`): an
accepted-answer list will always miss a valid variant somewhere, and the
appeal is how the list grows.

NFC, never NFKC: phones type Hangul as composed syllables (U+AC00…) and bare
letters as *compatibility* jamo (ㅎ U+314E). NFC leaves both alone; NFKC
would turn ㅎ into a conjoining jamo that no longer equals the key.

Pure functions, no Django — tested in workbook/tests.py.
"""
import re
import unicodedata

RIGHT, NEARLY, WRONG, EMPTY = 'right', 'nearly', 'wrong', 'empty'

# Characters a task kind does not mark (see `mark`).
IGNORE_FOR_KIND = {'hangul': ' +'}

_SPACES = re.compile(r'\s+')
_TRAILING = re.compile(r'[\s.?!。？！…]+$')
_LOOSE_DROP = re.compile(r'[\s.,?!。、，？！…·\-–—\'"«»“”‘’]+')


def normalise(text):
    """The strict form: what two answers must share to be the same answer."""
    text = unicodedata.normalize('NFC', text or '')
    # Curly quotes and the Uzbek ʻ/ʼ letters come in several code points
    # depending on the keyboard; fold them to one.
    text = (text.replace('‘', "'").replace('’', "'").replace('ʻ', "'")
                .replace('ʼ', "'").replace('`', "'"))
    text = _SPACES.sub(' ', text).strip()
    text = _TRAILING.sub('', text)
    return text.casefold()


def loosen(text):
    """The loose form: spacing and punctuation no longer count."""
    return _LOOSE_DROP.sub('', normalise(text))


def mark(text, answers, ignore=''):
    """Mark one typed answer against its accepted list.

    Returns one of RIGHT, NEARLY (right, but check spacing/punctuation),
    WRONG or EMPTY.

    `ignore` is a string of characters removed from both sides before
    comparing. Letter tasks pass ' +': a phone keyboard fuses ㅎ ㅏ ㄴ into
    한 as they are typed, so the pupil must separate the letters with spaces
    or plus signs, and how they separate them is not what is being marked.
    """
    if ignore:
        table = {ord(c): None for c in ignore}
        text = (text or '').translate(table)
        answers = [(a or '').translate(table) for a in answers or []]
    given = normalise(text)
    if not given:
        return EMPTY
    keys = [normalise(a) for a in answers or [] if normalise(a)]
    if given in keys:
        return RIGHT
    if loosen(given) in {loosen(k) for k in keys}:
        return NEARLY
    return WRONG


def is_correct(verdict):
    return verdict in (RIGHT, NEARLY)
