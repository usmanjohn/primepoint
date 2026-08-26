# -*- coding: utf-8 -*-
"""Per-subject wording for a Corner reading.

Every Corner story carries the same three extras — the inline `cn-word` spans, a
`StoryGrammar` block and a few MCQs — but what those extras *are* depends on the
shelf. On a Korean or Russian reading a cn-word is a word and its translation,
and the grammar block is a grammar pattern. On a **Matematika** reading the same
two mechanics carry a term and its definition, and a formula or rule the text
used. Calling that "Grammar from this story" on a maths page is simply wrong.

Rather than fork the models or the template per subject, the mechanics stay
global and this module says, per subject slug, what to call them. Same idea as
`examprep/banklabels.py`.

Everything degrades gracefully: a subject with no entry here gets DEFAULT, so a
new shelf renders sensibly on day one and only needs a block below when its
wording should differ.

Used through `Story.labels` / `Collection.labels`, so it reaches the reader page,
the print sheet and the printed book without any view knowing about it.
"""
from django.utils.translation import gettext_lazy as _


# The language-course wording — the msgids the locale files already carry.
DEFAULT = {
    'vocab':       _('Vocabulary from this story'),
    'vocab_hint':  _('Tap a card to flip it.'),
    'gram':        _('Grammar from this story'),
    'gram_hint':   _('Key patterns that appeared in the text.'),
    'quiz':        _('Check your understanding'),
    'quiz_hint':   _('Read the story, then choose the best answer. Tap a choice to check it.'),
    # Print sheet / book, where headings are terser.
    'p_vocab':     _('Vocabulary'),
    'p_word':      _('Word'),
    'p_tr':        _('Translation'),
    'p_gram':      _('Grammar in this text'),
    'ask':         _('Think about it'),
    'ask_hint':    _('No answer key for this one — it is yours to work out.'),
}

# Prime Math's two shelves. Untranslated on purpose: this whole subject is
# written in Uzbek whatever the interface language is, exactly like the Prime
# Korean and Prime Russian content.
MATH = {
    'vocab':       'Matndagi atamalar',
    'vocab_hint':  'Kartani bosing — taʼrifi chiqadi.',
    'gram':        'Qoida va formulalar',
    'gram_hint':   'Matnda ishlatilgan matematik qoida.',
    'quiz':        'Tekshirib koʻring',
    'quiz_hint':   'Matnni oʻqing, keyin hisoblang. Javobni bosib tekshiring.',
    'p_vocab':     'Atamalar',
    'p_word':      'Atama',
    'p_tr':        'Taʼrifi',
    'p_gram':      'Qoida va formulalar',
    'ask':         'Oʻylab koʻring',
    'ask_hint':    'Bu savolning javobi berilmagan — oʻzingiz oʻylab koʻring.',
}

BY_SUBJECT = {
    'matematika': MATH,
}


def labels_for(subject_slug):
    """Label set for a subject slug — DEFAULT for anything not listed."""
    return BY_SUBJECT.get(subject_slug or '', DEFAULT)
