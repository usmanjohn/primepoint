"""Turning site content into channel posts.

The channel is Uzbek-only: every word the bot writes itself is Uzbek, while
the material (an English sentence, a Korean line, a Russian phrase) stays in
its own language — the same split the practices already use.

Nothing here talks to Telegram; these functions only build text, so they can
be checked with --dry-run before a single message goes out.
"""
import html
import re

from django.conf import settings
from django.urls import reverse

from . import api

# ── The daily rotation ──────────────────────────────────────────────────────
# Subject name in the DB → (Uzbek label for the channel, emoji).
# Order is the rotation order: one subject per day, repeating every 5 days.
ROTATION = [
    ('English',    'Ingliz tili',      '🇬🇧'),
    ('한국어',      'Koreys tili',      '🇰🇷'),
    ('Matematika', 'Matematika',       '🔢'),
    ('Russian',    'Rus tili',         '🇷🇺'),
    ('Math',       'Matematika (SAT)', '📐'),
]
SUBJECT_LABELS = {name: (label, emoji) for name, label, emoji in ROTATION}

QUIZ_HEADER = '{emoji} Kun savoli · {subject}'
PUZZLE_HEADER = '🧩 Mantiq maydoni · #{number}'

# ── HTML → plain text ───────────────────────────────────────────────────────
_SUP = str.maketrans('0123456789+-=()n', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ')
_SUB = str.maketrans('0123456789+-=()', '₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎')


def _superscript(match):
    """<sup>2</sup> must not flatten to "2" — x2 is a different, wrong question."""
    inner = re.sub(r'<[^>]+>', '', match.group(1)).strip()
    if inner and all(c in '0123456789+-=()n' for c in inner):
        return inner.translate(_SUP)
    return '^' + inner


def _subscript(match):
    inner = re.sub(r'<[^>]+>', '', match.group(1)).strip()
    if inner and all(c in '0123456789+-=()' for c in inner):
        return inner.translate(_SUB)
    return '_' + inner


def to_text(markup):
    """CKEditor HTML → the plain text a poll option or poll question can carry."""
    if not markup:
        return ''
    text = str(markup)
    text = re.sub(r'<sup[^>]*>(.*?)</sup>', _superscript, text, flags=re.S | re.I)
    text = re.sub(r'<sub[^>]*>(.*?)</sub>', _subscript, text, flags=re.S | re.I)
    text = re.sub(r'<(br|/p|/div|/li|/h[1-6])[^>]*>', '\n', text, flags=re.I)
    text = re.sub(r'<li[^>]*>', '• ', text, flags=re.I)
    text = re.sub(r'<svg.*?</svg>', ' [rasm] ', text, flags=re.S | re.I)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n', text)
    return text.strip()


def trim(text, limit):
    """Cut to `limit` characters on a word boundary, marking the cut with an ellipsis."""
    if len(text) <= limit:
        return text
    cut = text[:limit - 1]
    space = cut.rfind(' ')
    if space > limit * 0.6:
        cut = cut[:space]
    return cut.rstrip(' ,.;:') + '…'


def site_url(path):
    return settings.SITE_URL.rstrip('/') + path


# ── The daily quiz ──────────────────────────────────────────────────────────
def quiz_fits(question):
    """Can this question be a native Telegram quiz poll at all?

    A poll is rejected whole if any part is over length, so an unusable
    question is skipped rather than trimmed — a trimmed question can quietly
    become unanswerable ("Which of the following is…" with the list cut off).
    """
    if question.image:
        return False
    choices = question.display_choices()
    if not 2 <= len(choices) <= api.POLL_OPTIONS_MAX:
        return False
    if sum(1 for c in choices if c.is_correct) != 1:
        return False
    if len(to_text(question.question_text)) > api.POLL_QUESTION_MAX:
        return False
    return all(0 < len(to_text(c.text)) <= api.POLL_OPTION_MAX for c in choices)


def build_quiz(question):
    """→ (poll question, options, index of the correct one, explanation, buttons)."""
    subject = getattr(question.practice.subject, 'name', '') or ''
    label, emoji = SUBJECT_LABELS.get(subject, (subject or 'Savol', '📚'))
    header = QUIZ_HEADER.format(emoji=emoji, subject=label)

    body = to_text(question.question_text)
    # The header is a nicety; the question is not. It goes only if both fit.
    text = f'{header}\n\n{body}'
    if len(text) > api.POLL_QUESTION_MAX:
        text = body

    choices = question.display_choices()
    options = [to_text(c.text) for c in choices]
    correct = next(i for i, c in enumerate(choices) if c.is_correct)

    explanation = trim(to_text(question.explanation), api.POLL_EXPLANATION_MAX)
    buttons = [('📝 Shu mavzuda mashq qilish',
                site_url(reverse('practice_detail', args=[question.practice_id])))]
    return text, options, correct, explanation, buttons


# ── The weekly Logic Arena puzzle ───────────────────────────────────────────
def build_puzzle(puzzle):
    url = site_url(reverse('logic_puzzle', args=[puzzle.slug]))
    title = puzzle.title_uz or puzzle.title
    teaser = to_text(puzzle.teaser_uz or puzzle.teaser)
    hint = puzzle.answer_hint_uz or puzzle.answer_hint

    lines = [
        f'<b>{html.escape(PUZZLE_HEADER.format(number=puzzle.number))}</b>',
        '',
        f'<b>{html.escape(title)}</b>',
    ]
    if teaser:
        lines += ['', html.escape(teaser)]
    lines += ['', f'Qiyinligi: {"★" * puzzle.difficulty}']
    if hint:
        lines.append(f'Javob shakli: {html.escape(hint)}')
    lines += [
        '',
        'Javobingizni yozing — lekin toʻgʻri yoki notoʻgʻriligini '
        'darhol bilmaysiz. Yechim va barcha yechganlar roʻyxati '
        f'{puzzle.reveal_at.strftime("%d.%m.%Y")} kuni ochiladi.',
    ]
    return '\n'.join(lines), [('🧩 Javobni yuborish', url)]


def build_solution(puzzle):
    url = site_url(reverse('logic_puzzle', args=[puzzle.slug]))
    title = puzzle.title_uz or puzzle.title
    lines = [
        f'<b>✅ Yechim ochildi · #{puzzle.number}</b>',
        '',
        f'<b>{html.escape(title)}</b>',
        '',
        f'Toʻgʻri javob: <b>{html.escape(puzzle.answer_key)}</b>',
        '',
        'Toʻliq izoh va yechganlar roʻyxati saytda.',
    ]
    return '\n'.join(lines), [('📖 Toʻliq yechimni oʻqish', url)]
