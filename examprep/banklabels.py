# -*- coding: utf-8 -*-
"""Per-track wording for the grammar bank and the vocabulary bank.

Both banks are one set of models shared by every exam track, but their labels
are not shareable. TOPIK's grammar sections are Korean parts of speech
(조사, 연결어미) and its levels read "TOPIK 3"; IELTS's are English structures
(tenses, conditionals) and its levels read "Band 6". The same is true of the
vocab bank: TOPIK's root families are Hanja (출(出) → 출구·출근), IELTS's are
Latin/Greek roots (spect → inspect·spectator·perspective).

Rather than fork the models per track, the choice VALUES stay global (one
`category` field, one `topic` field) and this module says, per track slug,
which of those values a track uses, in what order, and what to call them.

Everything degrades gracefully: a track with no entry here falls back to the
model's own choices, so adding GMAT tomorrow renders sensibly on day one and
only needs a block here when its wording should differ.
"""

from .models import (GRAMMAR_CATEGORY_CHOICES, GRAMMAR_FUNCTION_CHOICES,
                     GRAMMAR_REGISTER_CHOICES, VOCAB_POS_CHOICES,
                     VOCAB_TOPIC_CHOICES, VOCAB_RELATION_CHOICES)


# ── Grammar bank ───────────────────────────────────────────────────────────
# Each list is (value, label) in the order the track's sections should appear.
# Only list the values the track actually uses — a value left out simply never
# shows up as a section or a filter chip for that track.

GRAMMAR_CATEGORIES = {
    'topik': [
        'particle', 'ending', 'connective', 'tense', 'modifier',
        'expression', 'voice', 'quotation', 'honorific', 'adverb',
    ],
    'ielts': [
        'en_tense', 'en_modal', 'en_clause', 'en_condition', 'en_passive',
        'en_article', 'en_prep', 'en_compare', 'en_verbpat', 'en_cohesion',
        'en_advanced',
    ],
}

GRAMMAR_FUNCTIONS = {
    'topik': [
        'reason', 'contrast', 'condition', 'concession', 'time', 'purpose',
        'intention', 'guess', 'ability', 'obligation', 'experience', 'change',
        'comparison', 'listing', 'choice', 'quote', 'feeling', 'discovery',
        'degree', 'case', 'politeness',
    ],
    'ielts': [
        'reason', 'result', 'contrast', 'concession', 'condition', 'time',
        'purpose', 'comparison', 'change', 'degree', 'hedging', 'emphasis',
        'example', 'summary', 'reference', 'listing', 'guess', 'obligation',
        'ability', 'quote', 'feeling', 'case',
    ],
}

# Labels that differ from the model's default for a given track. TOPIK owns the
# defaults (the banks were built for it), so only IELTS overrides here.
GRAMMAR_FUNCTION_LABELS = {
    'ielts': {
        'reason':     'Sabab — Cause',
        'result':     'Natija — Result & consequence',
        'contrast':   'Qarama-qarshilik — Contrast',
        'concession': 'Qarshi qo‘yish — Concession',
        'condition':  'Shart — Condition',
        'time':       'Vaqt va ketma-ketlik — Time & sequence',
        'purpose':    'Maqsad — Purpose',
        'comparison': 'Qiyoslash — Comparison',
        'change':     'O‘zgarish va tendensiya — Trend & change',
        'degree':     'Daraja va miqdor — Degree & quantity',
        'hedging':    'Ehtiyotkor fikr — Hedging',
        'emphasis':   'Ta’kid — Emphasis',
        'example':    'Misol keltirish — Exemplification',
        'summary':    'Umumlashtirish — Summarising',
        'reference':  'Ishora va o‘rin bosish — Reference',
        'listing':    'Sanash va qo‘shish — Listing & addition',
        'guess':      'Taxmin — Speculation',
        'obligation': 'Majburiyat va ruxsat — Obligation',
        'ability':    'Imkoniyat — Possibility & ability',
        'quote':      'Ko‘chirma gap — Reported speech',
        'feeling':    'Baho va munosabat — Attitude',
        'case':       'Gap bo‘lagi — Sentence element',
    },
}

GRAMMAR_REGISTER_LABELS = {
    'ielts': {
        'written': 'Akademik yozma — Academic writing',
        'formal':  'Rasmiy — Formal',
        'polite':  'Neytral — Neutral',
        'casual':  'Norasmiy / og‘zaki — Informal',
        'both':    'Ikkalasi ham',
    },
}


# ── Vocabulary bank ────────────────────────────────────────────────────────

VOCAB_POSES = {
    'topik': ['noun', 'verb', 'adj', 'adv', 'phrase', 'count'],
    'ielts': ['noun', 'verb', 'adj', 'adv', 'phrase', 'count'],
}

VOCAB_POS_LABELS = {
    'ielts': {
        'noun':   'Ot — Noun',
        'verb':   'Fe’l — Verb',
        'adj':    'Sifat — Adjective',
        'adv':    'Ravish — Adverb',
        'phrase': 'Ibora — Phrase & collocation',
        'count':  'Son va o‘lchov — Number & measure',
    },
}

VOCAB_TOPICS = {
    'topik': [
        'daily', 'person', 'emotion', 'body', 'food', 'home', 'shopping',
        'transport', 'work', 'school', 'society', 'economy', 'environment',
        'science', 'culture', 'media', 'time', 'place', 'abstract',
    ],
    'ielts': [
        'academic', 'data', 'school', 'work', 'society', 'economy',
        'environment', 'science', 'health', 'crime', 'government', 'culture',
        'media', 'tourism', 'person', 'daily', 'abstract',
    ],
}

VOCAB_TOPIC_LABELS = {
    'ielts': {
        'academic':    'Akademik til — Academic language',
        'data':        'Grafik va raqamlar — Data & trends (Task 1)',
        'school':      'Ta’lim — Education',
        'work':        'Ish va kasb — Work & careers',
        'society':     'Jamiyat — Society',
        'economy':     'Iqtisod — Economy',
        'environment': 'Ekologiya — Environment',
        'science':     'Fan va texnologiya — Science & technology',
        'health':      'Sog‘liq — Health',
        'crime':       'Jinoyat va qonun — Crime & law',
        'government':  'Hukumat va siyosat — Government & politics',
        'culture':     'Madaniyat va san’at — Culture & arts',
        'media':       'OAV va axborot — Media & information',
        'tourism':     'Sayohat va turizm — Travel & tourism',
        'person':      'Odamlar va munosabat — People & relationships',
        'daily':       'Kundalik hayot — Everyday life',
        'abstract':    'Mavhum tushunchalar — Abstract concepts',
    },
}

VOCAB_RELATION_LABELS = {
    'ielts': {
        'syn': 'Sinonim — Synonym',
        'ant': 'Antonim — Antonym',
        'rel': 'Bog‘liq so‘z — Related word',
    },
}


# ── Levels ─────────────────────────────────────────────────────────────────
# `level` is 1–6 on both models. What that number MEANS is the track's
# business: for TOPIK it is the TOPIK level a pattern first appears at, for
# IELTS it is the band from which the structure or word starts earning marks.

LEVEL_LABELS = {
    'topik': ['TOPIK 1', 'TOPIK 2', 'TOPIK 3', 'TOPIK 4', 'TOPIK 5', 'TOPIK 6'],
    'ielts': ['Band 5', 'Band 5.5', 'Band 6', 'Band 6.5', 'Band 7', 'Band 7.5+'],
}


# ── Page wording ───────────────────────────────────────────────────────────
# The bits of prose the templates print around the data. `root_glyph_source`
# decides what goes in the big family badge: Hanja is a single character and
# reads beautifully there; "specere" does not, so IELTS shows the root itself.

TERMS = {
    'topik': {
        'level_filter':   'TOPIK darajasi',
        'level_hint':     'TOPIK darajasi (1–6)',
        'freq_title':     'TOPIK’da uchrash chastotasi',
        'example_lang':   '한국어',
        'origin_label':   'Hanja',
        'root_word':      'O‘zak',
        'root_kind':      '한자 어근',
        'root_family':    'So‘z oilasi — 한자 어근',
        'root_glyph_source': 'hanja',
        'examples_title':     'Namunalar — 예문',
        'collocations_title': 'Ko‘p uchraydigan birikmalar — 연어',
        'grammar_search_hint': 'Qidirish: -(으)니까, sabab, 때문에, 하숙집…',
        'vocab_search_hint':   'Qidirish: 출근, chiqish, 出, ish…',
        'roots_search_hint':   'O‘zak yoki so‘z: 출, 出, chiqmoq, 출근…',
        'root_banner_glyph': '出',
        'root_banner_text':  '<b>출</b>(出) = «chiqmoq» ni bilsangiz — <b>출</b>구, <b>출</b>근, '
                             '<b>출</b>발, <b>출</b>석, 제<b>출</b>, 수<b>출</b> ni ham tushunasiz. '
                             'Bitta o‘zak — o‘nlab so‘z.',
        'roots_title':    'So‘z oilalari · 한자 어근',
        'roots_meta':     'Koreys tili so‘z oilalari: 출(出) — 출구, 출근, 출발, 제출, 수출. '
                          'Bitta Hanja o‘zakni o‘rganib, o‘nlab TOPIK so‘zini taniysiz.',
        'roots_why':      'TOPIK II lug‘atining katta qismi <em>xitoycha ildizli</em> (한자어). '
                          'Har bir bo‘g‘in o‘z ma’nosini olib yuradi, shuning uchun '
                          '<b>출</b>(出) = «chiqmoq» ni bir marta o‘rgansangiz — '
                          '<b>출</b>구 (chiqish joyi), <b>출</b>근 (ishga chiqish), '
                          '<b>출</b>발 (jo‘nash), 제<b>출</b> (topshirish, «oldinga chiqarish»), '
                          '수<b>출</b> (eksport) — hammasi mantiqiy bo‘lib qoladi. '
                          'Imtihonda <u>notanish</u> so‘z uchrasa, o‘zagidan ma’nosini taxmin '
                          'qila olasiz — bu 읽기 da eng foydali ko‘nikma.',
    },
    'ielts': {
        'level_filter':   'Band daraja',
        'level_hint':     'Band (5.0–7.5+)',
        'freq_title':     'IELTS’da uchrash chastotasi',
        'example_lang':   'English',
        'origin_label':   'Kelib chiqishi',
        'root_word':      'Ildiz',
        'root_kind':      'Lotin/yunon ildizlari',
        'root_family':    'So‘z oilasi — bir ildizdan',
        'root_glyph_source': 'syllable',
        'examples_title':     'Namunalar — Examples',
        'collocations_title': 'Ko‘p uchraydigan birikmalar — Collocations',
        'grammar_search_hint': 'Qidirish: present perfect, sabab, although…',
        'vocab_search_hint':   'Qidirish: emission, o‘sish, spect, data…',
        'roots_search_hint':   'Ildiz yoki so‘z: spect, port, qaramoq, inspect…',
        'root_banner_glyph': 'spect',
        'root_banner_text':  '<b>spect</b> = «qaramoq» ni bilsangiz — in<b>spect</b>, '
                             '<b>spect</b>ator, per<b>spect</b>ive, pro<b>spect</b>, '
                             '<b>spect</b>acular ni ham tushunasiz. Bitta ildiz — o‘nlab so‘z.',
        'roots_title':    'So‘z oilalari · Lotin va yunon ildizlari',
        'roots_meta':     'Ingliz tili so‘z oilalari: spect (qaramoq) — inspect, spectator, '
                          'perspective, prospect. Bitta ildizni o‘rganib, o‘nlab IELTS '
                          'so‘zini taniysiz.',
        'roots_why':      'Akademik ingliz tilining katta qismi <em>lotin va yunon ildizlaridan</em> '
                          'yasalgan. Har bir ildiz o‘z ma’nosini olib yuradi, shuning uchun '
                          '<b>spect</b> = «qaramoq» ni bir marta o‘rgansangiz — '
                          'in<b>spect</b> (tekshirmoq), <b>spect</b>ator (tomoshabin), '
                          'per<b>spect</b>ive (nuqtai nazar), pro<b>spect</b> (istiqbol), '
                          '<b>spect</b>acular (ko‘zni quvontiruvchi) — hammasi mantiqiy bo‘lib '
                          'qoladi. Reading’da <u>notanish</u> so‘z uchrasa, ildizidan ma’nosini '
                          'taxmin qila olasiz — bu Band 7 ga chiqaradigan ko‘nikma.',
    },
}

_DEFAULT_TERMS = TERMS['topik']


def _ordered(all_choices, values, overrides):
    """(value, label) pairs for `values`, in that order, with overrides applied."""
    default = dict(all_choices)
    return [(v, overrides.get(v, default.get(v, v))) for v in values
            if v in default]


def _slug(track):
    return getattr(track, 'slug', track) or ''


def grammar_categories(track):
    """The category sections this track uses, in display order."""
    slug = _slug(track)
    values = GRAMMAR_CATEGORIES.get(slug)
    if values is None:
        return list(GRAMMAR_CATEGORY_CHOICES)
    return _ordered(GRAMMAR_CATEGORY_CHOICES, values, {})


def grammar_functions(track):
    """The meaning groups this track uses, in display order."""
    slug = _slug(track)
    values = GRAMMAR_FUNCTIONS.get(slug)
    if values is None:
        return list(GRAMMAR_FUNCTION_CHOICES)
    return _ordered(GRAMMAR_FUNCTION_CHOICES, values,
                    GRAMMAR_FUNCTION_LABELS.get(slug, {}))


def vocab_poses(track):
    slug = _slug(track)
    values = VOCAB_POSES.get(slug)
    if values is None:
        return list(VOCAB_POS_CHOICES)
    return _ordered(VOCAB_POS_CHOICES, values, VOCAB_POS_LABELS.get(slug, {}))


def vocab_topics(track):
    slug = _slug(track)
    values = VOCAB_TOPICS.get(slug)
    if values is None:
        return list(VOCAB_TOPIC_CHOICES)
    return _ordered(VOCAB_TOPIC_CHOICES, values,
                    VOCAB_TOPIC_LABELS.get(slug, {}))


def _label(all_choices, overrides, slug, value, fallback=''):
    return overrides.get(slug, {}).get(value) or dict(all_choices).get(value, fallback)


def grammar_category_label(track, value):
    return _label(GRAMMAR_CATEGORY_CHOICES, {}, _slug(track), value, value)


def grammar_function_label(track, value):
    return _label(GRAMMAR_FUNCTION_CHOICES, GRAMMAR_FUNCTION_LABELS,
                  _slug(track), value, value)


def grammar_register_label(track, value):
    return _label(GRAMMAR_REGISTER_CHOICES, GRAMMAR_REGISTER_LABELS,
                  _slug(track), value, value)


def vocab_pos_label(track, value):
    return _label(VOCAB_POS_CHOICES, VOCAB_POS_LABELS, _slug(track), value, value)


def vocab_topic_label(track, value):
    return _label(VOCAB_TOPIC_CHOICES, VOCAB_TOPIC_LABELS, _slug(track), value, value)


def vocab_relation_label(track, value):
    return _label(VOCAB_RELATION_CHOICES, VOCAB_RELATION_LABELS,
                  _slug(track), value, value)


def level_label(track, level):
    """'TOPIK 3' / 'Band 6' — what level `n` is called in this track."""
    labels = LEVEL_LABELS.get(_slug(track))
    if labels and 1 <= (level or 0) <= len(labels):
        return labels[level - 1]
    return f'{_slug(track).upper()} {level}'


def level_choices(track):
    """[(1, 'Band 5'), …] for the level filter chips."""
    labels = LEVEL_LABELS.get(_slug(track)) or LEVEL_LABELS['topik']
    return list(enumerate(labels, start=1))


def terms(track):
    """The track's page wording, with TOPIK's as the fallback."""
    return {**_DEFAULT_TERMS, **TERMS.get(_slug(track), {})}
