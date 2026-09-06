"""
English Championship — savol generatorlari.

The English twin of `games/mathchamp.py`: every question is generated on the
fly, so no two championship runs are the same. Each generator returns a dict:

    {
        'topic':       str   # badge shown above the question
        'text':        str   # the question itself (English)
        'choices':     [str, str, str, str]
        'correct':     int   # 0-based index into choices
        'explanation': str   # why, shown after answering (Uzbek)
    }

`level` is 'a1' / 'a2' / 'b1' (CEFR) and `tier` is 1 / 2 / 3 (championship
round). The level decides which topic pool is in play; the tier makes the
questions inside that pool harder.

Language policy: the question and the four choices are in **English** — that
is the material being tested — while every explanation is in **Uzbek**, the
same split the Prime English readings use for their glosses.
"""
import random


LEVELS = ('a1', 'a2', 'b1')

LEVEL_LABELS = {
    'a1': 'A1 — Beginner',
    'a2': 'A2 — Elementary',
    'b1': 'B1 — Intermediate',
}


# ---------------------------------------------------------------------------
# Choice assembly
# ---------------------------------------------------------------------------

# Safety net only: every generator below ships at least three real distractors,
# but a data edit that accidentally collides with the answer must never produce
# a two-option question.
_FILLERS = ['do', 'does', 'is', 'are', 'was', 'were', 'have', 'has', 'be',
            'the', 'a', 'an', 'to', 'of', 'in', 'on', 'at', 'not']


def _q(topic, text, correct, wrongs, explanation):
    """Build the final question dict: 4 unique shuffled choices."""
    wrongs = list(wrongs)
    random.shuffle(wrongs)

    options = [correct]
    for w in wrongs:
        if w != correct and w not in options:
            options.append(w)
        if len(options) == 4:
            break
    for f in _FILLERS:
        if len(options) == 4:
            break
        if f not in options:
            options.append(f)

    random.shuffle(options)
    return {
        'topic':       topic,
        'text':        text,
        'choices':     options,
        'correct':     options.index(correct),
        'explanation': explanation,
    }


def _others(rows, row, k=3, key=lambda r: r):
    """k random values from `rows`, never the one we are asking about."""
    pool = [r for r in rows if key(r) != key(row)]
    return random.sample(pool, min(k, len(pool)))


# ---------------------------------------------------------------------------
# Pupil names — the teacher's real students star in the sentences.
# Only ever used in subject position, so no sentence has to guess anyone's
# pronoun; the his/her questions use generic family words instead.
# ---------------------------------------------------------------------------

_PUPILS = ['Jasur', 'Sherbek', 'Davron', 'Samandar', 'Kamron', 'Javohir',
           'Firdavs', "Ilg'or", 'Afsona', 'Madina', 'Charos', 'Bunyod']


def _name():
    return random.choice(_PUPILS)


# ===========================================================================
# A1 — to be
# ===========================================================================

_BE_ROWS = [
    ('I',                  'am',  'a student'),
    ('You',                'are', 'my best friend'),
    ('He',                 'is',  'at home now'),
    ('She',                'is',  'a good singer'),
    ('It',                 'is',  'very cold today'),
    ('We',                 'are', 'in the same class'),
    ('They',               'are', 'from Samarkand'),
    ('My parents',         'are', 'teachers'),
    ('The cat',            'is',  'under the table'),
    ('My friends',         'are', 'in the yard'),
    ('The books',          'are', 'on the shelf'),
    ('This apple',         'is',  'very sweet'),
]

_BE_PAST = {'am': 'was', 'is': 'was', 'are': 'were'}

# Past questions need sentences with no time word of their own.
_BE_PAST_ROWS = [
    ('I',          'am',  'at home all day'),
    ('He',         'is',  'very tired'),
    ('She',        'is',  'in the library'),
    ('We',         'are', 'at my grandmother’s house'),
    ('They',       'are', 'very happy'),
    ('My parents', 'are', 'in Samarkand'),
    ('The film',   'is',  'really boring'),
]

_BE_WHY = {
    'am':  "\"I\" olmoshi bilan faqat \"am\" ishlatiladi.",
    'is':  "Ega birlikda (u / bitta narsa) bo'lgani uchun \"is\" ishlatiladi.",
    'are': "Ega ko'plikda (yoki \"you\") bo'lgani uchun \"are\" ishlatiladi.",
}


def q_be(level, tier):
    subj, form, rest = random.choice(_BE_ROWS + [(_name(), 'is', 'twelve years old')])
    wrongs = ['am', 'is', 'are', 'be']

    if tier >= 3 and random.random() < 0.5:
        subj, form, rest = random.choice(_BE_PAST_ROWS)
        past = _BE_PAST[form]
        text = f"Choose the correct word: {subj} ___ {rest} yesterday."
        return _q("To be — Past", text, past, ['was', 'were', 'is', 'are'],
                  f"O'tgan zamonda \"{form}\" → \"{past}\". {_BE_WHY[form]}")

    if tier >= 2 and random.random() < 0.5:
        text = f"Choose the correct word: {subj} ___ not {rest}."
        return _q("To be — Negative", text, form, wrongs,
                  f"Inkor shaklda ham \"to be\" o'zgarmaydi: {subj} + {form} + not. {_BE_WHY[form]}")

    text = f"Choose the correct word: {subj} ___ {rest}."
    return _q("To be", text, form, wrongs, _BE_WHY[form])


# ===========================================================================
# A1 — articles
# ===========================================================================

# (word, article, note) — the note only appears where the rule is not simply
# "starts with a vowel letter".
_ARTICLE_WORDS = [
    ('apple',            'an', ''),
    ('orange',           'an', ''),
    ('egg',              'an', ''),
    ('elephant',         'an', ''),
    ('engineer',         'an', ''),
    ('umbrella',         'an', ''),
    ('uncle',            'an', ''),
    ('old book',         'an', ''),
    ('interesting film', 'an', ''),
    ('island',           'an', ''),
    ('answer',           'an', ''),
    ('English teacher',  'an', ''),
    ('hour',             'an', "\"hour\" so'zida \"h\" o'qilmaydi — \"auır\" deb aytiladi, ya'ni unli tovush bilan boshlanadi."),
    ('honest man',       'an', "\"honest\" so'zida \"h\" o'qilmaydi, shuning uchun \"an\"."),
    ('book',             'a',  ''),
    ('car',              'a',  ''),
    ('table',            'a',  ''),
    ('house',            'a',  ''),
    ('pen',              'a',  ''),
    ('dog',              'a',  ''),
    ('friend',           'a',  ''),
    ('hospital',         'a',  ''),
    ('young boy',        'a',  ''),
    ('university',       'a',  "\"university\" \"yu-\" tovushi bilan boshlanadi (unli emas), shuning uchun \"a\"."),
    ('uniform',          'a',  "\"uniform\" \"yu-\" tovushi bilan boshlanadi, shuning uchun \"a\"."),
    ('useful idea',      'a',  "\"useful\" \"yu-\" tovushi bilan boshlanadi, shuning uchun \"a\"."),
    ('European country', 'a',  "\"European\" \"yu-\" tovushi bilan boshlanadi, shuning uchun \"a\"."),
]

_ZERO_ARTICLE = [
    ('I like ___ music.',              "\"music\" — sanaladigan bo'lmagan umumiy ot, artikl kerak emas."),
    ('___ cats are lovely animals.',   "Umuman butun turni nazarda tutganda ko'plik ot artiklsiz keladi."),
    ('She goes to ___ school by bus.', "\"go to school\" — barqaror ibora, artiklsiz ishlatiladi."),
    ('We had ___ breakfast at seven.', "Ovqat nomlari (breakfast, lunch, dinner) artiklsiz keladi."),
    ('He lives in ___ Uzbekistan.',    "Ko'p mamlakat nomlari artiklsiz ishlatiladi."),
    ('I don’t drink ___ coffee.', "\"coffee\" — sanaladigan bo'lmagan ot, umumiy ma'noda artiklsiz."),
]

_THE_ROWS = [
    ('Please close ___ door.',                 "Ikkalamiz ham qaysi eshik ekanini bilamiz — aniq narsa, shuning uchun \"the\"."),
    ('___ sun is very bright today.',           "Dunyoda bitta bo'lgan narsalar (sun, moon, sky) oldidan \"the\"."),
    ('I bought a book. ___ book was cheap.',    "Ikkinchi marta tilga olinayotgan narsa oldidan \"the\"."),
    ('She plays ___ piano very well.',          "Musiqa asboblari oldidan \"the\" ishlatiladi: play the piano."),
    ('Tashkent is ___ capital of Uzbekistan.',  "Yagona, aniq narsa (poytaxt bitta) — \"the\"."),
]


def q_articles(level, tier):
    if tier >= 3 and random.random() < 0.45:
        text, note = random.choice(_ZERO_ARTICLE)
        return _q("Artikllar", 'Choose the correct answer: ' + text,
                  '— (no article)', ['a', 'an', 'the'], note)

    if tier >= 2 and random.random() < 0.5:
        text, note = random.choice(_THE_ROWS)
        return _q("Artikllar", 'Choose the correct answer: ' + text,
                  'the', ['a', 'an', '— (no article)'], note)

    word, art, note = random.choice(_ARTICLE_WORDS)
    other = 'a' if art == 'an' else 'an'
    why = note or (
        f"\"{word}\" unli tovush bilan boshlanadi, shuning uchun \"an\"."
        if art == 'an' else
        f"\"{word}\" undosh tovush bilan boshlanadi, shuning uchun \"a\"."
    )
    return _q("Artikllar", f"Choose the correct article: I have ___ {word}.",
              art, [other, 'the', '— (no article)'], why)


# ===========================================================================
# A1/A2 — plurals
# ===========================================================================

# (singular, plural, [distractors], note)
_PLURALS_EASY = [
    ('book',   'books',   ['bookes', 'bookies', "book's"], "Oddiy otlarga -s qo'shiladi."),
    ('table',  'tables',  ['tablees', 'tablies', "table's"], "Oddiy otlarga -s qo'shiladi."),
    ('friend', 'friends', ['friendes', 'friendies', "friend's"], "Oddiy otlarga -s qo'shiladi."),
    ('bus',    'buses',   ['buss', 'busses', 'busies'], "-s, -ss, -sh, -ch, -x, -o bilan tugaganda -es qo'shiladi."),
    ('box',    'boxes',   ['boxs', 'boxies', 'boxen'], "-x bilan tugagani uchun -es qo'shiladi."),
    ('watch',  'watches', ['watchs', 'watchies', 'watchen'], "-ch bilan tugagani uchun -es qo'shiladi."),
    ('dish',   'dishes',  ['dishs', 'dishies', 'dishen'], "-sh bilan tugagani uchun -es qo'shiladi."),
    ('potato', 'potatoes', ['potatos', 'potatoies', 'potatoen'], "Undoshdan keyin -o bilan tugaganda -es qo'shiladi."),
]

_PLURALS_MID = [
    ('city',   'cities',   ['citys', 'cityes', 'cityies'], "Undosh + -y bo'lsa, -y tushib -ies qo'shiladi."),
    ('baby',   'babies',   ['babys', 'babyes', 'babyies'], "Undosh + -y bo'lsa, -y tushib -ies qo'shiladi."),
    ('country', 'countries', ['countrys', 'countryes', 'countryies'], "Undosh + -y bo'lsa, -y tushib -ies qo'shiladi."),
    ('boy',    'boys',     ['boies', 'boyes', 'boyies'], "Unli + -y bo'lsa, -y saqlanadi va faqat -s qo'shiladi."),
    ('day',    'days',     ['daies', 'dayes', 'dayies'], "Unli + -y bo'lsa, -y saqlanadi va faqat -s qo'shiladi."),
    ('knife',  'knives',   ['knifes', 'knifs', 'knifees'], "-f / -fe → -ves."),
    ('leaf',   'leaves',   ['leafs', 'leafes', 'leaven'], "-f / -fe → -ves."),
    ('wife',   'wives',    ['wifes', 'wifs', 'wifees'], "-f / -fe → -ves."),
]

_PLURALS_HARD = [
    ('child',  'children', ['childs', 'childes', 'childrens'], "Noto'g'ri ko'plik: child → children."),
    ('man',    'men',      ['mans', 'mens', 'manes'], "Noto'g'ri ko'plik: man → men."),
    ('woman',  'women',    ['womans', 'womens', 'womanes'], "Noto'g'ri ko'plik: woman → women."),
    ('foot',   'feet',     ['foots', 'footes', 'feets'], "Noto'g'ri ko'plik: foot → feet."),
    ('tooth',  'teeth',    ['tooths', 'toothes', 'teeths'], "Noto'g'ri ko'plik: tooth → teeth."),
    ('mouse',  'mice',     ['mouses', 'mousees', 'mices'], "Noto'g'ri ko'plik: mouse → mice."),
    ('person', 'people',   ['persons', 'peoples', 'personen'], "Kundalik nutqda person → people."),
    ('sheep',  'sheep',    ['sheeps', 'sheepes', 'sheepen'], "Bu so'z ko'plikda ham o'zgarmaydi: one sheep — five sheep."),
    ('fish',   'fish',     ['fishs', 'fishies', 'fishen'], "Baliq turi haqida gap ketmasa, fish ko'plikda ham o'zgarmaydi."),
]


def q_plural(level, tier):
    pool = {1: _PLURALS_EASY,
            2: _PLURALS_EASY + _PLURALS_MID,
            3: _PLURALS_MID + _PLURALS_HARD}[tier]
    sing, plur, wrongs, note = random.choice(pool)
    return _q("Ko'plik shakli", f"What is the plural of “{sing}”?",
              plur, list(wrongs), f"{sing} → {plur}. {note}")


# ===========================================================================
# A1 — pronouns, possessives, demonstratives
# ===========================================================================

_SUBJECT_ROWS = [
    ('My brother and I are twins. ___ are in the same class.', 'We',
     "\"My brother and I\" = biz, shuning uchun \"We\"."),
    ('Anna is my classmate. ___ is very kind.', 'She',
     "Anna — qiz, ega o'rnida \"She\"."),
    ('Look at that dog! ___ is very big.', 'It',
     "Hayvon yoki narsa ega o'rnida \"It\"."),
    ('My parents work in a hospital. ___ are doctors.', 'They',
     "\"My parents\" — ko'plik, ega o'rnida \"They\"."),
    ('Tom is my neighbour. ___ has two cars.', 'He',
     "Tom — o'g'il bola, ega o'rnida \"He\"."),
]

_OBJECT_ROWS = [
    ('This is my sister. I see ___ every day.', 'her',
     "Fe'ldan keyin to'ldiruvchi shakl kerak: she → her."),
    ('These are my books. Please give ___ to me.', 'them',
     "Fe'ldan keyin to'ldiruvchi shakl kerak: they → them."),
    ('Tom is my friend. I often help ___ with maths.', 'him',
     "Fe'ldan keyin to'ldiruvchi shakl kerak: he → him."),
    ('I am here. Can you hear ___?', 'me',
     "Fe'ldan keyin to'ldiruvchi shakl kerak: I → me."),
    ('We are late. Wait for ___, please!', 'us',
     "Predlogdan keyin ham to'ldiruvchi shakl kerak: we → us."),
]

_PRON_ALL = ['I', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her',
             'us', 'them', 'you']

_POSS_ADJ_ROWS = [
    ('This is my sister. ___ name is Malika.', 'Her',
     "Opa-singil — ayol kishi, egalik sifati \"her\"."),
    ('That is my brother. ___ bike is new.', 'His',
     "Aka-uka — erkak kishi, egalik sifati \"his\"."),
    ('We are students. ___ school is very big.', 'Our',
     "\"We\" → egalik sifati \"our\"."),
    ('They live here. ___ house is white.', 'Their',
     "\"They\" → egalik sifati \"their\"."),
    ('I have a cat. ___ name is Luna.', 'Its',
     "Hayvon yoki narsaning egaligi — \"its\" (apostrofsiz!)."),
    ('You are late. Where is ___ bag?', 'your',
     "\"You\" → egalik sifati \"your\"."),
]

_POSS_ADJ_ALL = ['my', 'your', 'his', 'her', 'its', 'our', 'their',
                 'My', 'Your', 'His', 'Her', 'Its', 'Our', 'Their']

_POSS_PRON_ROWS = [
    ('This book is not yours, it is ___.', 'mine',
     "Otdan keyin kelmaydigan egalik olmoshi: my → mine."),
    ('That car is ___ — my father bought it last year.', 'ours',
     "\"our\" + ot bo'lmasa → \"ours\"."),
    ('I have my pen. Where is ___?', 'yours',
     "\"your\" + ot bo'lmasa → \"yours\"."),
    ('These bags are not mine, they are ___.', 'theirs',
     "\"their\" + ot bo'lmasa → \"theirs\"."),
]

_POSS_PRON_ALL = ['mine', 'yours', 'his', 'hers', 'ours', 'theirs']


def q_pronoun(level, tier):
    if tier >= 3:
        text, ans, why = random.choice(_POSS_PRON_ROWS)
        return _q("Egalik olmoshlari", 'Choose the correct word: ' + text,
                  ans, _others(_POSS_PRON_ALL, ans), why)
    if tier == 2:
        text, ans, why = random.choice(_OBJECT_ROWS)
        return _q("Olmoshlar", 'Choose the correct word: ' + text,
                  ans, _others(_PRON_ALL, ans), why)
    text, ans, why = random.choice(_SUBJECT_ROWS)
    caps = [p.capitalize() for p in _PRON_ALL]
    return _q("Olmoshlar", 'Choose the correct word: ' + text,
              ans, _others(caps, ans), why)


def q_possessive_adj(level, tier):
    text, ans, why = random.choice(_POSS_ADJ_ROWS)
    pool = [p for p in _POSS_ADJ_ALL if p[0].isupper() == ans[0].isupper()]
    return _q("Egalik sifatlari", 'Choose the correct word: ' + text,
              ans, _others(pool, ans), why)


_DEMONSTRATIVE_ROWS = [
    ('___ book in my hand is very interesting.', 'This',
     "Yaqindagi bitta narsa — \"this\"."),
    ('___ books here are mine.', 'These',
     "Yaqindagi ko'p narsa — \"these\"."),
    ('Look at ___ mountains over there!', 'those',
     "Uzoqdagi ko'p narsa — \"those\"."),
    ('___ house at the end of the street is very old.', 'That',
     "Uzoqdagi bitta narsa — \"that\"."),
    ('Do you see ___ birds in the sky?', 'those',
     "Uzoqdagi ko'p narsa — \"those\"."),
]


def q_demonstrative(level, tier):
    text, ans, why = random.choice(_DEMONSTRATIVE_ROWS)
    pool = ['this', 'that', 'these', 'those']
    pool = [p.capitalize() if ans[0].isupper() else p for p in pool]
    return _q("This / That / These / Those", 'Choose the correct word: ' + text,
              ans, _others(pool, ans), why)


# ===========================================================================
# A1/A2 — prepositions
# ===========================================================================

_PREP_PLACE = [
    ('The pen is ___ the box.',              'in',    "Yopiq joyning ichida — \"in\"."),
    ('Your keys are ___ the table.',         'on',    "Yuzaning ustida — \"on\"."),
    ('I am waiting ___ the bus stop.',       'at',    "Aniq nuqta yoki joy — \"at\"."),
    ('The ball is ___ the bed.',             'under', "Ostida — \"under\"."),
    ('The bank is ___ the shop and the cafe.', 'between', "Ikki narsaning orasida — \"between\"."),
    ('Somebody is ___ the door!',            'behind', "Orqasida — \"behind\"."),
    ('There is a tree ___ our house.',       'in front of', "Oldida — \"in front of\"."),
    ('Sit ___ me, please.',                  'next to', "Yonida — \"next to\"."),
    ('My grandmother lives ___ Bukhara.',    'in',    "Shahar nomlari oldidan — \"in\"."),
    ('There is a picture ___ the wall.',     'on',    "Devorga osilgan narsa — \"on the wall\"."),
    ('We live ___ the third floor.',         'on',    "Qavat haqida gapirganda — \"on the ... floor\"."),
    ('I will meet you ___ the cinema.',      'at',    "Uchrashuv joyi sifatida — \"at\"."),
]

_PREP_PLACE_ALL = ['in', 'on', 'at', 'under', 'behind', 'between',
                   'in front of', 'next to', 'over']

_PREP_TIME = [
    ('The lesson starts ___ 8 o’clock.',   'at', "Aniq soat oldidan — \"at\"."),
    ('I always read ___ night.',                'at', "\"at night\" — barqaror ibora."),
    ('We rest ___ the weekend.',                'at', "\"at the weekend\" — barqaror ibora (BrE)."),
    ('We have English ___ Monday.',             'on', "Hafta kunlari oldidan — \"on\"."),
    ('My birthday is ___ 12th May.',            'on', "Aniq sana oldidan — \"on\"."),
    ('She was born ___ July.',                  'in', "Oy nomlari oldidan — \"in\"."),
    ('He finished school ___ 2019.',            'in', "Yil oldidan — \"in\"."),
    ('I drink tea ___ the morning.',            'in', "\"in the morning / afternoon / evening\" — barqaror ibora."),
    ('It is very hot here ___ summer.',         'in', "Fasl nomlari oldidan — \"in\"."),
    ('The train leaves ___ half past six.',     'at', "Aniq vaqt oldidan — \"at\"."),
    ('I will call you ___ two hours.',          'in', "\"Qancha vaqtdan keyin\" ma'nosida — \"in\"."),
    ('We do not have lessons ___ Sunday.',      'on', "Hafta kunlari oldidan — \"on\"."),
]


def q_prep_place(level, tier):
    text, ans, why = random.choice(_PREP_PLACE)
    return _q("O'rin predloglari", 'Choose the correct preposition: ' + text,
              ans, _others(_PREP_PLACE_ALL, ans), why)


def q_prep_time(level, tier):
    text, ans, why = random.choice(_PREP_TIME)
    return _q("Payt predloglari", 'Choose the correct preposition: ' + text,
              ans, ['in', 'on', 'at', 'for'], why)


# ===========================================================================
# A1 — there is / have got / can
# ===========================================================================

_THERE_ROWS = [
    ('There ___ a book on the desk.',            'is',  'singular'),
    ('There ___ three windows in this room.',    'are', 'plural'),
    ('There ___ some milk in the fridge.',       'is',  'uncount'),
    ('There ___ many people in the street.',     'are', 'plural'),
    ('There ___ a lot of snow in winter.',       'is',  'uncount'),
    ('There ___ two apples in my bag.',          'are', 'plural'),
]

_THERE_WHY = {
    'singular': "Ot birlikda, shuning uchun \"There is\".",
    'plural':   "Ot ko'plikda, shuning uchun \"There are\".",
    'uncount':  "Sanaladigan bo'lmagan ot (milk, snow, water) bilan \"There is\".",
}


_THERE_PAST = [
    ('There ___ a big tree in our yard when I was a child.', 'was', 'singular'),
    ('There ___ only five pupils in the class yesterday.',   'were', 'plural'),
    ('There ___ no snow here last winter.',                  'was', 'uncount'),
    ('There ___ two shops in this street ten years ago.',    'were', 'plural'),
]


def q_there_is(level, tier):
    if tier >= 3:
        text, past, kind = random.choice(_THERE_PAST)
        return _q("There was / There were", 'Choose the correct word: ' + text,
                  past, ['was', 'were', 'is', 'are'],
                  f"O'tgan zamonda \"There is/are\" → \"There {past}\". {_THERE_WHY[kind]}")
    text, ans, kind = random.choice(_THERE_ROWS)
    return _q("There is / There are", 'Choose the correct word: ' + text,
              ans, ['is', 'are', 'am', 'be'], _THERE_WHY[kind])


_HAVE_GOT_ROWS = [
    ('I ___ got two brothers.',            'have',    "\"I / you / we / they\" bilan \"have got\"."),
    ('She ___ got a new phone.',           'has',     "\"He / she / it\" bilan \"has got\"."),
    ('My friends ___ got a big house.',    'have',    "Ega ko'plikda — \"have got\"."),
    ('Our teacher ___ got a red car.',     'has',     "Ega birlikda (u) — \"has got\"."),
    ('They ___ got any money.',            "haven’t", "Inkorda: \"have not got\" → \"haven't got\"."),
    ('He ___ got a sister.',               "hasn’t", "Inkorda birlik uchun: \"has not got\" → \"hasn't got\"."),
]


def q_have_got(level, tier):
    text, ans, why = random.choice(_HAVE_GOT_ROWS)
    return _q("Have got / Has got", 'Choose the correct word: ' + text,
              ans, ['have', 'has', "haven’t", "hasn’t", 'had'], why)


_CAN_ROWS = [
    ('My little sister is only two. She ___ read yet.', "can’t",
     "Qila olmaslik — \"can't\" (cannot)."),
    ('Birds ___ fly, but they cannot swim like fish.', 'can',
     "Qila olish — \"can\" + fe'lning boshlang'ich shakli."),
    ('___ you help me, please?', 'Can',
     "Iltimos yoki so'rovda gap boshida \"Can\"."),
    ('I ___ speak English well when I was seven.', "couldn’t",
     "O'tgan zamonda qila olmaslik — \"couldn't\"."),
    ('He ___ swim very well — he trains every day.', 'can',
     "Qila olish — \"can\"."),
]


def q_can(level, tier):
    text, ans, why = random.choice(_CAN_ROWS)
    return _q("Can / Can't", 'Choose the correct word: ' + text,
              ans, ['can', "can’t", 'Can', 'could', "couldn’t"], why)


# ===========================================================================
# A1/A2 — Present Simple
# ===========================================================================

# (subject, third-person form, base form, rest, plural?)
_PS_ROWS = [
    ('Jasur',        'plays',   'play',  'football every Sunday', False),
    ('My sister',    'watches', 'watch', 'TV in the evening', False),
    ('He',           'goes',    'go',    'to bed at ten', False),
    ('Madina',       'studies', 'study', 'English twice a week', False),
    ('Our teacher',  'gives',   'give',  'us homework every day', False),
    ('The bus',      'arrives', 'arrive', 'at eight o’clock', False),
    ('It',           'rains',   'rain',  'a lot in spring', False),
    ('She',          'does',    'do',    'her homework after dinner', False),
    ('My friends',   'play',    'play',  'chess after school', True),
    ('We',           'live',    'live',  'near the school', True),
    ('They',         'speak',   'speak', 'three languages', True),
]


def q_present_simple(level, tier):
    subj, third, base, rest, plural = random.choice(_PS_ROWS)

    if tier >= 3 and random.random() < 0.5:
        aux = 'Do' if plural else 'Does'
        # Names keep their capital letter; everything else drops to lower case.
        inner = subj if subj in _PUPILS else subj[0].lower() + subj[1:]
        text = f"Choose the correct word: ___ {inner} {base} {rest}?"
        why = ("So'roq gapda ko'plik ega bilan \"Do\" + fe'lning boshlang'ich shakli."
               if plural else
               "So'roq gapda 3-shaxs birlik ega bilan \"Does\", fe'lga -s QO'SHILMAYDI.")
        return _q("Present Simple — Question", text, aux,
                  ['Do', 'Does', 'Is', 'Are'], why)

    if tier >= 2 and random.random() < 0.5:
        neg = "don’t" if plural else "doesn’t"
        text = f"Choose the correct word: {subj} ___ {base} {rest}."
        why = ("Ko'plik ega bilan inkor: don't + fe'lning boshlang'ich shakli."
               if plural else
               "3-shaxs birlik ega bilan inkor: doesn't + fe'lning boshlang'ich shakli (-s yo'q).")
        return _q("Present Simple — Negative", text, neg,
                  ["don’t", "doesn’t", "isn’t", "aren’t"], why)

    ans = base if plural else third
    text = f"Choose the correct word: {subj} ___ {rest}."
    why = (f"Ega ko'plikda, shuning uchun fe'l o'zgarmaydi: {base}."
           if plural else
           f"3-shaxs birlik (he / she / it) bilan fe'lga -s qo'shiladi: {base} → {third}.")
    # For plural rows the answer IS the base form, so the tempting wrong
    # answer is the -s form; for singular rows it is the other way round.
    wrongs = [base + 's', base + 'ing', 'is ' + base] if plural else \
             [base, base + 'ing', 'is ' + base, base + 'es']
    return _q("Present Simple", text, ans, [w for w in wrongs if w != ans], why)


# ===========================================================================
# A2 — Past Simple
# ===========================================================================

# (base, past, past participle)
_IRREGULAR = [
    ('go', 'went', 'gone'), ('buy', 'bought', 'bought'), ('see', 'saw', 'seen'),
    ('eat', 'ate', 'eaten'), ('take', 'took', 'taken'), ('come', 'came', 'come'),
    ('write', 'wrote', 'written'), ('teach', 'taught', 'taught'),
    ('think', 'thought', 'thought'), ('drink', 'drank', 'drunk'),
    ('run', 'ran', 'run'), ('give', 'gave', 'given'), ('know', 'knew', 'known'),
    ('make', 'made', 'made'), ('meet', 'met', 'met'), ('sing', 'sang', 'sung'),
    ('speak', 'spoke', 'spoken'), ('swim', 'swam', 'swum'),
    ('catch', 'caught', 'caught'), ('bring', 'brought', 'brought'),
    ('leave', 'left', 'left'), ('find', 'found', 'found'),
    ('sleep', 'slept', 'slept'), ('feel', 'felt', 'felt'),
    ('win', 'won', 'won'), ('lose', 'lost', 'lost'), ('pay', 'paid', 'paid'),
    ('build', 'built', 'built'), ('understand', 'understood', 'understood'),
    ('forget', 'forgot', 'forgotten'), ('break', 'broke', 'broken'),
    ('choose', 'chose', 'chosen'), ('drive', 'drove', 'driven'),
    ('fall', 'fell', 'fallen'), ('send', 'sent', 'sent'),
]

# (base, past, the rest of the sentence) — each verb gets an object that fits.
_PAST_SENTENCES = [
    ('go',    'went',   'to the market'),
    ('buy',   'bought', 'a new bag'),
    ('see',   'saw',    'an interesting film'),
    ('eat',   'ate',    'a big pizza'),
    ('write', 'wrote',  'a letter to his friend'),
    ('drink', 'drank',  'a glass of milk'),
    ('take',  'took',   'a photo of the mountains'),
    ('meet',  'met',    'an old friend'),
    ('lose',  'lost',   'the house keys'),
    ('find',  'found',  'some money in the street'),
    ('make',  'made',   'a cake'),
    ('read',  'read',   'the whole book'),
    ('catch', 'caught', 'the last bus'),
    ('bring', 'brought', 'a present'),
]


def q_past_simple(level, tier):
    base, past, pp = random.choice(_IRREGULAR)
    wrongs = [base + 'ed', pp, base, base + 'd', base + 's']
    wrongs = [w for w in wrongs if w != past]

    if tier >= 3 and random.random() < 0.4:
        text = (f"Choose the correct word: {_name()} ___ not {base} "
                f"to school yesterday.")
        return _q("Past Simple — Negative", text, 'did',
                  ['does', 'do', 'was', 'were'],
                  "Inkorda \"did not\" + fe'lning boshlang'ich shakli; asosiy "
                  f"fe'l o'zgarmaydi ({base}, {past} emas).")

    if tier >= 2 and random.random() < 0.45:
        base, past, rest = random.choice(_PAST_SENTENCES)
        text = (f"Choose the correct word: Yesterday {_name()} ___ "
                f"{rest}. ({base})")
        return _q("Past Simple", text, past,
                  [w for w in (base + 'ed', base, base + 's', base + 'ing')
                   if w != past],
                  f"\"yesterday\" — o'tgan zamon, va {base} noto'g'ri fe'l: "
                  f"{base} → {past} (-ed qo'shilmaydi).")

    return _q("Past Simple", f"What is the past simple of “{base}”?",
              past, wrongs,
              f"\"{base}\" — noto'g'ri fe'l: {base} → {past} → {pp}. "
              f"Unga -ed qo'shilmaydi.")


_PAST_SPELLING = [
    ('stop',   'stopped',   ['stoped', 'stopd', 'stopeed'],
     "Qisqa unli + bitta undosh bilan tugaganda oxirgi harf ikkilanadi: stop → stopped."),
    ('plan',   'planned',   ['planed', 'pland', 'planeed'],
     "Qisqa unli + bitta undosh bilan tugaganda oxirgi harf ikkilanadi: plan → planned."),
    ('study',  'studied',   ['studyed', 'studed', 'studies'],
     "Undosh + -y bo'lsa, -y tushib -ied qo'shiladi: study → studied."),
    ('carry',  'carried',   ['carryed', 'carred', 'carries'],
     "Undosh + -y bo'lsa, -y tushib -ied qo'shiladi: carry → carried."),
    ('play',   'played',    ['plaied', 'plaid', 'playd'],
     "Unli + -y bo'lsa, -y saqlanadi: play → played."),
    ('like',   'liked',     ['likeed', 'likd', 'liket'],
     "-e bilan tugagan fe'lga faqat -d qo'shiladi: like → liked."),
    ('travel', 'travelled', ['traveled', 'travelt', 'travelited'],
     "Britaniya imlosida -l ikkilanadi: travel → travelled."),
    ('visit',  'visited',   ['visitted', 'visitd', 'visiteed'],
     "Urg'u oxirgi bo'g'inda emas, shuning uchun -t ikkilanmaydi: visit → visited."),
]


def q_past_spelling(level, tier):
    base, past, wrongs, why = random.choice(_PAST_SPELLING)
    return _q("Past Simple — imlo",
              f"What is the past simple of “{base}”?",
              past, list(wrongs), why)


# ===========================================================================
# A2 — Present Continuous / future
# ===========================================================================

_PC_ROWS = [
    ('Look! The baby ___ .',                 'is sleeping', 'sleep'),
    ('Be quiet — the students ___ a test.',  'are writing', 'write'),
    ('Listen! Somebody ___ at the door.',    'is knocking', 'knock'),
    ('Where is Jasur? He ___ in the yard.',  'is playing',  'play'),
    ('We ___ dinner at the moment.',         'are having',  'have'),
]

_ING_SPELLING = [
    ('run',   'running',   ['runing', 'runned', 'runnning'],
     "Qisqa unli + bitta undosh: oxirgi harf ikkilanadi — run → running."),
    ('write', 'writing',   ['writeing', 'writting', 'writng'],
     "-e tushib ketadi: write → writing."),
    ('lie',   'lying',     ['lieing', 'liing', 'lyeing'],
     "-ie → -ying: lie → lying."),
    ('begin', 'beginning', ['begining', 'beginnning', 'begined'],
     "Urg'u oxirgi bo'g'inda: begin → beginning."),
    ('swim',  'swimming',  ['swiming', 'swimmming', 'swimed'],
     "Qisqa unli + bitta undosh: swim → swimming."),
]

_STATE_VERBS = [
    ('I ___ this song very much.', 'like', 'am liking',
     "\"like\" — holat fe'li, Present Continuous'da ishlatilmaydi."),
    ('She ___ what you mean.', 'understands', 'is understanding',
     "\"understand\" — holat fe'li, davomli zamonda kelmaydi."),
    ('This bag ___ to my sister.', 'belongs', 'is belonging',
     "\"belong\" — holat fe'li, davomli zamonda kelmaydi."),
    ('I ___ you are right.', 'think', 'am thinking',
     "Fikrni bildirganda \"think\" holat fe'li bo'lib, oddiy zamonda keladi."),
]


def q_present_continuous(level, tier):
    if tier >= 3 and random.random() < 0.4:
        text, ans, wrong, why = random.choice(_STATE_VERBS)
        return _q("Present Continuous", 'Choose the correct word: ' + text,
                  ans, [wrong, 'am ' + ans, ans + 'ing'], why)

    if tier >= 2 and random.random() < 0.5:
        base, ing, wrongs, why = random.choice(_ING_SPELLING)
        return _q("-ing imlosi", f"What is the -ing form of “{base}”?",
                  ing, list(wrongs), why)

    text, ans, base = random.choice(_PC_ROWS)
    be = ans.split()[0]
    other_be = 'are' if be == 'is' else 'is'
    return _q("Present Continuous", 'Choose the correct answer: ' + text,
              ans, [f'{other_be} {base}ing', base + 's', base,
                    f'{be} {base}'],
              f"Hozir, shu daqiqada sodir bo'layotgan ish: to be + fe'l+ing → \"{ans}\".")


_FUTURE_ROWS = [
    ('Look at those clouds! It ___ rain.', 'is going to',
     "Ko'z oldimizdagi dalilga asoslangan bashorat — \"going to\"."),
    ('I have already decided: I ___ study medicine.', 'am going to',
     "Oldindan qilingan reja — \"going to\"."),
    ('The phone is ringing. — OK, I ___ answer it.', 'will',
     "Shu zahoti qabul qilingan qaror — \"will\"."),
    ('I think our team ___ win the match.', 'will',
     "Fikr, taxmin (I think, I hope) bilan — \"will\"."),
    ('Don’t worry, I ___ help you.', 'will',
     "Va'da berish — \"will\"."),
]


def q_future(level, tier):
    text, ans, why = random.choice(_FUTURE_ROWS)
    wrongs = ['will', 'is going to', 'am going to', 'are going to', 'shall be']
    return _q("Kelasi zamon", 'Choose the correct answer: ' + text,
              ans, [w for w in wrongs if w != ans], why)


# ===========================================================================
# A2 — comparatives, quantifiers, possessive 's, frequency
# ===========================================================================

# (adjective, comparative, superlative)
_ADJECTIVES = [
    ('big', 'bigger', 'the biggest'),
    ('hot', 'hotter', 'the hottest'),
    ('cheap', 'cheaper', 'the cheapest'),
    ('young', 'younger', 'the youngest'),
    ('happy', 'happier', 'the happiest'),
    ('easy', 'easier', 'the easiest'),
    ('expensive', 'more expensive', 'the most expensive'),
    ('beautiful', 'more beautiful', 'the most beautiful'),
    ('interesting', 'more interesting', 'the most interesting'),
    ('difficult', 'more difficult', 'the most difficult'),
    ('good', 'better', 'the best'),
    ('bad', 'worse', 'the worst'),
    ('far', 'further', 'the furthest'),
]


def q_comparative(level, tier):
    adj, comp, sup = random.choice(_ADJECTIVES)
    wrongs = [adj + 'er', 'more ' + adj, 'the most ' + adj, adj, 'more ' + comp]

    if tier >= 3 and random.random() < 0.35:
        return _q("As ... as",
                  "Choose the correct answer: My bag is not ___ yours.",
                  'as heavy as', ['as heavier as', 'so heavy than',
                                  'as heavy than', 'more heavy as'],
                  "Tenglikni bildirish: as + sifat (oddiy shakl) + as.")

    if tier >= 2 and random.random() < 0.5:
        return _q("Superlative",
                  f"What is the superlative form of “{adj}”?",
                  sup, [w for w in ['the ' + adj + 'est', 'the most ' + adj,
                                    'the more ' + adj, 'the ' + comp,
                                    'the ' + adj, 'most ' + adj] if w != sup],
                  f"Orttirma daraja: {adj} → {sup}." +
                  (" Bir bo'g'inli sifatlarga -est qo'shiladi."
                   if not sup.startswith('the most') else
                   " Uzun sifatlar oldidan \"the most\" keladi."))

    return _q("Comparative",
              f"Choose the correct answer: This book is ___ than that one. ({adj})",
              comp, [w for w in wrongs if w != comp],
              f"Qiyosiy daraja: {adj} → {comp}." +
              (" Uzun sifatlar oldidan \"more\" keladi."
               if comp.startswith('more') else
               " Bir bo'g'inli sifatlarga -er qo'shiladi."))


_QUANTIFIER_ROWS = [
    ('How ___ money do you have?', 'much',
     "\"money\" sanalmaydi, shuning uchun \"how much\"."),
    ('How ___ students are there in your class?', 'many',
     "\"students\" sanaladi va ko'plikda, shuning uchun \"how many\"."),
    ('There isn’t ___ sugar in my tea.', 'much',
     "Inkor gapda sanalmaydigan ot bilan \"much\"."),
    ('I have ___ friends in Tashkent.', 'a lot of',
     "Tasdiq gapda ko'plik ot bilan \"a lot of\" tabiiy eshitiladi."),
    ('Would you like ___ tea?', 'some',
     "Taklif qilishda so'roq gapda ham \"some\" ishlatiladi."),
    ('I don’t have ___ questions.', 'any',
     "Inkor gapda \"any\"."),
    ('There are ___ apples left — only three.', 'a few',
     "Sanaladigan ot bilan \"oz miqdor\" — \"a few\"."),
    ('There is ___ milk left — just a drop.', 'a little',
     "Sanalmaydigan ot bilan \"oz miqdor\" — \"a little\"."),
]


def q_quantifier(level, tier):
    text, ans, why = random.choice(_QUANTIFIER_ROWS)
    pool = ['much', 'many', 'some', 'any', 'a few', 'a little', 'a lot of']
    return _q("Miqdor so'zlari", 'Choose the correct word: ' + text,
              ans, _others(pool, ans), why)


_POSS_S_ROWS = [
    ('This is ___ car. (my father)', "my father’s car",
     ["my father car", "my fathers car", "car of my father"],
     "Kishiga tegishlilik: ot + 's."),
    ('These are ___ books. (the students)', "the students’ books",
     ["the student’s books", "the students books", "the books of students"],
     "Ko'plik ot -s bilan tugasa, faqat apostrof qo'yiladi: students'."),
    ('That is ___ room. (the children)', "the children’s room",
     ["the childrens’ room", "the children room", "the childrens room"],
     "Noto'g'ri ko'plik (children) -s bilan tugamaydi, shuning uchun 's."),
    ('Where is ___ office? (the manager)', "the manager’s office",
     ["the managers office", "the manager office", "the office of manager"],
     "Kishiga tegishlilik: ot + 's."),
    ('I like ___ colour. (this door)', "the colour of this door",
     ["this door’s colour", "this doors colour", "the this door colour"],
     "Jonsiz narsalar bilan odatda \"of\" ishlatiladi: the colour of the door."),
]


def q_possessive_s(level, tier):
    text, ans, wrongs, why = random.choice(_POSS_S_ROWS)
    return _q("Egalik ('s)", 'Choose the correct answer: ' + text,
              ans, list(wrongs), why)


_FREQUENCY_ROWS = [
    ('He is always late.',
     ['He always is late.', 'He is late always.', 'Always he is late.'],
     "Takror ravishlari \"to be\" fe'lidan KEYIN keladi: He is always late."),
    ('She never drinks coffee.',
     ['She drinks never coffee.', 'She doesn’t never drink coffee.',
      'Never she drinks coffee.'],
     "Takror ravishlari asosiy fe'ldan OLDIN keladi: She never drinks coffee."),
    ('I have never been to Japan.',
     ['I never have been to Japan.', 'I have been never to Japan.',
      'I am never been to Japan.'],
     "Yordamchi fe'l bo'lsa, ravish undan keyin keladi: have never been."),
    ('Jasur often plays chess.',
     ['Jasur plays often chess.', 'Jasur often play chess.',
      'Often Jasur play chess.'],
     "Ravish asosiy fe'ldan oldin, fe'l esa 3-shaxs birlikda -s oladi."),
    ('We usually have dinner at seven.',
     ['We have usually dinner at seven.', 'We usually are having dinner at seven.',
      'Usually have we dinner at seven.'],
     "Ravish asosiy fe'ldan oldin keladi: we usually have."),
]


def q_frequency(level, tier):
    correct, wrongs, why = random.choice(_FREQUENCY_ROWS)
    return _q("Takror ravishlari", 'Which sentence is correct?',
              correct, list(wrongs), why)


_QUESTION_WORDS = [
    ('___ is your name? — Sherbek.', 'What', "Ism, narsa haqida so'raganda — \"What\"."),
    ('___ do you live? — In Namangan.', 'Where', "Joy haqida so'raganda — \"Where\"."),
    ('___ does the lesson start? — At nine.', 'When', "Vaqt haqida so'raganda — \"When\"."),
    ('___ is that man? — My uncle.', 'Who', "Shaxs haqida so'raganda — \"Who\"."),
    ('___ are you late? — Because the bus was full.', 'Why', "Sabab so'raganda — \"Why\"."),
    ('___ do you go to school? — By bus.', 'How', "Usul haqida so'raganda — \"How\"."),
    ('___ books do you have? — Twelve.', 'How many', "Sanaladigan narsa miqdori — \"How many\"."),
    ('___ water do you drink a day? — Two litres.', 'How much', "Sanalmaydigan narsa miqdori — \"How much\"."),
    ('___ bag is this? — It is Madina’s.', 'Whose', "Kimniki ekanini so'raganda — \"Whose\"."),
    ('___ do you go to the cinema? — Twice a month.', 'How often', "Qanchalik tez-tez — \"How often\"."),
]


def q_question_word(level, tier):
    text, ans, why = random.choice(_QUESTION_WORDS)
    pool = [r[1] for r in _QUESTION_WORDS]
    return _q("So'roq so'zlari", 'Choose the correct question word: ' + text,
              ans, _others(pool, ans), why)


# ===========================================================================
# Vocabulary
# ===========================================================================

_VOCAB = {
    'a1': [
        ('kitob', 'book'), ('olma', 'apple'), ('non', 'bread'), ('suv', 'water'),
        ('uy', 'house'), ('maktab', 'school'), ('deraza', 'window'), ('eshik', 'door'),
        ('stol', 'table'), ('stul', 'chair'), ('it', 'dog'), ('mushuk', 'cat'),
        ('qush', 'bird'), ('daraxt', 'tree'), ('gul', 'flower'), ('quyosh', 'sun'),
        ('oy', 'moon'), ('yulduz', 'star'), ('ruchka', 'pen'), ('qalam', 'pencil'),
        ('sumka', 'bag'), ('sut', 'milk'), ('tuxum', 'egg'), ('baliq', 'fish'),
        ('go‘sht', 'meat'), ('sabzi', 'carrot'), ('kartoshka', 'potato'),
        ('do‘st', 'friend'), ('ona', 'mother'), ('ota', 'father'),
        ('shifokor', 'doctor'), ('o‘qituvchi', 'teacher'), ('mashina', 'car'),
        ('avtobus', 'bus'), ('velosiped', 'bicycle'), ('ko‘cha', 'street'),
        ('shahar', 'city'), ('kun', 'day'), ('tun', 'night'), ('qo‘l', 'hand'),
        ('ko‘z', 'eye'), ('bosh', 'head'), ('choy', 'tea'), ('nonushta', 'breakfast'),
    ],
    'a2': [
        ('qo‘shni', 'neighbour'), ('sayohat', 'trip'), ('ob-havo', 'weather'),
        ('bulut', 'cloud'), ('yomg‘ir', 'rain'), ('qor', 'snow'),
        ('shamol', 'wind'), ('dengiz', 'sea'), ('tog‘', 'mountain'),
        ('daryo', 'river'), ('ko‘prik', 'bridge'), ('kutubxona', 'library'),
        ('kasalxona', 'hospital'), ('do‘kon', 'shop'), ('bozor', 'market'),
        ('pul', 'money'), ('narx', 'price'), ('ish', 'job'), ('mehmon', 'guest'),
        ('sovg‘a', 'gift'), ('xat', 'letter'), ('yangilik', 'news'),
        ('javob', 'answer'), ('savol', 'question'), ('yordam', 'help'),
        ('sotib olmoq', 'buy'), ('sotmoq', 'sell'), ('o‘rganmoq', 'learn'),
        ('tushunmoq', 'understand'), ('unutmoq', 'forget'), ('eslamoq', 'remember'),
        ('kutmoq', 'wait'), ('kulmoq', 'laugh'), ('yig‘lamoq', 'cry'),
        ('qiziqarli', 'interesting'), ('zerikarli', 'boring'), ('xavfli', 'dangerous'),
        ('foydali', 'useful'), ('qimmat', 'expensive'), ('arzon', 'cheap'),
        ('kuchli', 'strong'), ('bo‘sh', 'empty'),
    ],
    'b1': [
        ('imkoniyat', 'opportunity'), ('muvaffaqiyat', 'success'),
        ('muvaffaqiyatsizlik', 'failure'), ('qaror', 'decision'), ('maqsad', 'aim'),
        ('sabab', 'reason'), ('natija', 'result'), ('ta’sir', 'influence'),
        ('tajriba', 'experience'), ('bilim', 'knowledge'), ('qobiliyat', 'ability'),
        ('mas’uliyat', 'responsibility'), ('ishonch', 'confidence'),
        ('adolat', 'justice'), ('erkinlik', 'freedom'), ('xavfsizlik', 'safety'),
        ('atrof-muhit', 'environment'), ('ifloslanish', 'pollution'),
        ('rivojlanish', 'development'), ('tadqiqot', 'research'),
        ('kashfiyot', 'discovery'), ('ixtiro', 'invention'), ('an’ana', 'tradition'),
        ('madaniyat', 'culture'), ('jamiyat', 'society'), ('hukumat', 'government'),
        ('qonun', 'law'), ('taklif', 'suggestion'), ('shikoyat', 'complaint'),
        ('maslahat', 'advice'), ('ogohlantirish', 'warning'), ('dalil', 'evidence'),
        ('foyda', 'benefit'), ('kamchilik', 'disadvantage'),
        ('rad etmoq', 'refuse'), ('tan olmoq', 'admit'), ('ta’minlamoq', 'provide'),
        ('kamaytirmoq', 'reduce'), ('oshirmoq', 'increase'), ('hal qilmoq', 'solve'),
        ('taqqoslamoq', 'compare'), ('ishontirmoq', 'convince'),
        ('ajoyib', 'amazing'), ('kutilmagan', 'unexpected'), ('murakkab', 'complicated'),
    ],
}


def q_vocab(level, tier):
    bank = _VOCAB[level]
    uz, en = random.choice(bank)
    others = _others(bank, (uz, en), 3, key=lambda r: r[1])

    if random.random() < 0.5:
        # Uzbek → English
        gloss = ', '.join(f"{o[1]} — {o[0]}" for o in others)
        return _q("So'z boyligi", f"What is “{uz}” in English?",
                  en, [o[1] for o in others],
                  f"\"{uz}\" — \"{en}\". Qolganlari: {gloss}.")

    # English → Uzbek
    gloss = ', '.join(f"{o[1]} — {o[0]}" for o in others)
    return _q("So'z boyligi", f"What does “{en}” mean?",
              uz, [o[0] for o in others],
              f"\"{en}\" — \"{uz}\". Qolganlari: {gloss}.")


_OPPOSITES = [
    ('big', 'small'), ('hot', 'cold'), ('old', 'new'), ('fast', 'slow'),
    ('happy', 'sad'), ('easy', 'difficult'), ('cheap', 'expensive'),
    ('clean', 'dirty'), ('empty', 'full'), ('strong', 'weak'),
    ('light', 'heavy'), ('early', 'late'), ('near', 'far'), ('wet', 'dry'),
    ('safe', 'dangerous'), ('boring', 'interesting'), ('quiet', 'noisy'),
    ('rich', 'poor'), ('thick', 'thin'), ('open', 'closed'),
    ('right', 'wrong'), ('young', 'old'), ('long', 'short'), ('high', 'low'),
]


def q_opposite(level, tier):
    pair = random.choice(_OPPOSITES)
    if random.random() < 0.5:
        word, ans = pair
    else:
        ans, word = pair
    flat = list(dict.fromkeys(w for p in _OPPOSITES for w in p))
    wrongs = random.sample([w for w in flat if w not in (word, ans)], 3)
    return _q("Qarama-qarshi ma'no",
              f"What is the opposite of “{word}”?",
              ans, wrongs, f"\"{word}\" ↔ \"{ans}\".")


_CATEGORIES = [
    ('mevalar',           ['apple', 'banana', 'orange', 'grape', 'peach', 'pear']),
    ('sabzavotlar',       ['carrot', 'potato', 'onion', 'tomato', 'cucumber', 'cabbage']),
    ('hayvonlar',         ['dog', 'cat', 'horse', 'sheep', 'cow', 'goat']),
    ('ranglar',           ['red', 'blue', 'green', 'yellow', 'black', 'white']),
    ('kasblar',           ['doctor', 'teacher', 'driver', 'farmer', 'nurse', 'pilot']),
    ('mebel',             ['table', 'chair', 'sofa', 'bed', 'shelf', 'wardrobe']),
    ('transport vositalari', ['bus', 'train', 'plane', 'taxi', 'ship', 'bicycle']),
    ('sport turlari',     ['football', 'tennis', 'boxing', 'swimming', 'chess', 'volleyball']),
    ('tana a’zolari', ['hand', 'leg', 'nose', 'ear', 'eye', 'mouth']),
    ('kiyimlar',          ['shirt', 'dress', 'coat', 'hat', 'socks', 'jacket']),
    ('maktab buyumlari',  ['pen', 'pencil', 'ruler', 'rubber', 'notebook', 'bag']),
    ('oila a’zolari', ['mother', 'father', 'sister', 'brother', 'uncle', 'aunt']),
    ('ob-havo so‘zlari', ['rain', 'snow', 'wind', 'fog', 'sunshine', 'cloud']),
    ('ichimliklar',       ['tea', 'coffee', 'juice', 'milk', 'lemonade', 'water']),
]


def q_odd_one_out(level, tier):
    (name_a, words_a), (name_b, words_b) = random.sample(_CATEGORIES, 2)
    same = random.sample(words_a, 3)
    odd = random.choice(words_b)
    return _q("Ortiqcha so'z", 'Which word does NOT belong to the group?',
              odd, same,
              f"{', '.join(same)} — {name_a}, lekin \"{odd}\" — {name_b}.")


# ===========================================================================
# B1 — Present Perfect
# ===========================================================================

_PP_ROWS = [
    ('I have known him ___ ten years.', 'for',
     "Davomiylik (qancha vaqt) — \"for\": for ten years."),
    ('She has lived in Tashkent ___ 2019.', 'since',
     "Boshlanish nuqtasi (qachondan beri) — \"since\": since 2019."),
    ('___ you ever been to Korea?', 'Have',
     "Hayotiy tajriba haqida so'roq: Have you ever + 3-shakl."),
    ('He hasn’t finished his homework ___ .', 'yet',
     "Inkor va so'roqda \"hali\" ma'nosida — \"yet\" gap oxirida."),
    ('The train has ___ left — we are five minutes late.', 'just',
     "\"Hozirgina\" ma'nosi — \"just\", yordamchi fe'ldan keyin."),
    ('I have ___ seen this film twice.', 'already',
     "\"Allaqachon\" ma'nosi — \"already\", yordamchi fe'ldan keyin."),
]

_PP_VS_PAST = [
    ('I ___ my keys — I can’t open the door now.', 'have lost',
     ['lost', 'am losing', 'had lost'],
     "Natijasi hozir sezilyapti (eshik ochilmayapti) — Present Perfect."),
    ('We ___ to Bukhara last summer.', 'went',
     ['have gone', 'have been going', 'are going'],
     "\"last summer\" — aniq o'tgan vaqt, shuning uchun Past Simple."),
    ('___ you finished your homework?', 'Have',
     ['Did', 'Do', 'Are'],
     "Vaqt ko'rsatilmagan, natija muhim — Present Perfect: Have you finished?"),
    ('She ___ that book two days ago.', 'read',
     ['has read', 'have read', 'is reading'],
     "\"two days ago\" — aniq o'tgan vaqt, Past Simple kerak."),
]


def q_present_perfect(level, tier):
    if tier >= 3 and random.random() < 0.5:
        text, ans, wrongs, why = random.choice(_PP_VS_PAST)
        return _q("Present Perfect / Past Simple",
                  'Choose the correct answer: ' + text, ans, list(wrongs), why)
    text, ans, why = random.choice(_PP_ROWS)
    pool = ['for', 'since', 'yet', 'just', 'already', 'ever', 'Have', 'Has', 'Did']
    return _q("Present Perfect", 'Choose the correct word: ' + text,
              ans, _others(pool, ans), why)


# ===========================================================================
# B1 — conditionals, passive, relatives, modals
# ===========================================================================

_CONDITIONALS = [
    ('If you heat water to 100 °C, it ___ .', 'boils',
     ['will boil', 'would boil', 'boiled'],
     "Zero Conditional (doimiy haqiqat): If + Present Simple, Present Simple."),
    ('If it ___ tomorrow, we will stay at home.', 'rains',
     ['will rain', 'would rain', 'rained'],
     "First Conditional: If + Present Simple, will + fe'l. \"If\" dan keyin \"will\" qo'yilmaydi."),
    ('If I ___ more time, I would travel a lot.', 'had',
     ['have', 'will have', 'would have'],
     "Second Conditional (real emas): If + Past Simple, would + fe'l."),
    ('If she studied harder, she ___ better marks.', 'would get',
     ['will get', 'gets', 'would got'],
     "Second Conditional: If + Past Simple, would + fe'lning boshlang'ich shakli."),
    ('I ___ you if I have any news.', 'will call',
     ['would call', 'call', 'called'],
     "First Conditional: shart Present Simple, natija will + fe'l."),
    ('If I ___ you, I would apologise.', 'were',
     ['am', 'will be', 'would be'],
     "Second Conditional'da \"be\" fe'li barcha shaxslar uchun \"were\" bo'ladi: If I were you."),
]


def q_conditional(level, tier):
    text, ans, wrongs, why = random.choice(_CONDITIONALS)
    return _q("Shart gaplar", 'Choose the correct answer: ' + text,
              ans, list(wrongs), why)


_PASSIVE = [
    ('English ___ all over the world.', 'is spoken',
     ['speaks', 'is speaking', 'has spoken'],
     "Majhul nisbat: to be + 3-shakl. Ish kim tomonidan bajarilgani muhim emas."),
    ('The letter ___ yesterday.', 'was sent',
     ['sent', 'is sent', 'was sending'],
     "O'tgan zamon majhul nisbati: was/were + 3-shakl."),
    ('This bridge ___ in 1998.', 'was built',
     ['built', 'is built', 'was building'],
     "O'tgan zamon majhul nisbati: was + built (build ning 3-shakli)."),
    ('The rooms ___ every morning.', 'are cleaned',
     ['is cleaned', 'clean', 'are cleaning'],
     "Ega ko'plikda: are + 3-shakl."),
    ('My car ___ last week — the police are looking for it.', 'was stolen',
     ['stole', 'is stolen', 'was stealing'],
     "steal → stole → stolen; majhul nisbat: was stolen."),
    ('Tea ___ in this factory since 1970.', 'has been packed',
     ['has packed', 'is packing', 'was packed'],
     "\"since 1970\" — Present Perfect majhul: has been + 3-shakl."),
]


def q_passive(level, tier):
    text, ans, wrongs, why = random.choice(_PASSIVE)
    return _q("Majhul nisbat", 'Choose the correct answer: ' + text,
              ans, list(wrongs), why)


_RELATIVE = [
    ('The man ___ lives next door is a pilot.', 'who',
     "Shaxs haqida — \"who\" (yoki \"that\")."),
    ('This is the book ___ I told you about.', 'which',
     "Narsa haqida — \"which\" (yoki \"that\")."),
    ('That is the girl ___ father is our teacher.', 'whose',
     "Egalikni bildiradi — \"whose\"."),
    ('This is the house ___ I was born.', 'where',
     "Joyni bildiradi — \"where\"."),
    ('I remember the day ___ we first met.', 'when',
     "Vaqtni bildiradi — \"when\"."),
    ('The film ___ we watched last night was boring.', 'that',
     "Narsa haqida, cheklovchi ergash gap — \"that\" (yoki \"which\")."),
]


def q_relative(level, tier):
    text, ans, why = random.choice(_RELATIVE)
    pool = ['who', 'which', 'whose', 'where', 'when', 'that', 'what']
    return _q("Nisbiy olmoshlar", 'Choose the correct word: ' + text,
              ans, _others(pool, ans), why)


_MODALS = [
    ('You ___ smoke here — this is a hospital.', "mustn’t",
     "Qat'iy taqiq — \"mustn't\"."),
    ('You ___ see a doctor — you look really ill.', 'should',
     "Maslahat berish — \"should\"."),
    ('It is Sunday, so I ___ get up early.', "don’t have to",
     "Zarurat yo'q (lekin taqiq ham emas) — \"don't have to\"."),
    ('Take an umbrella — it ___ rain later.', 'might',
     "Ehtimollik — \"might\"."),
    ('She ___ be at home — her car is outside.', 'must',
     "Ishonchli xulosa — \"must\"."),
    ('He ___ be at school — I saw him at the market five minutes ago.', "can’t",
     "Imkonsiz degan xulosa — \"can't\"."),
    ('In our school we ___ wear a uniform — it is a rule.', 'have to',
     "Tashqi qoida talab qiladi — \"have to\"."),
]


def q_modal(level, tier):
    text, ans, why = random.choice(_MODALS)
    pool = ['must', "mustn’t", 'should', "shouldn’t", 'have to',
            "don’t have to", 'might', "can’t", 'can']
    return _q("Modal fe'llar", 'Choose the correct answer: ' + text,
              ans, _others(pool, ans), why)


_REPORTED = [
    ('“I am tired,” he said.', 'He said that he was tired.',
     ['He said that he is tired.', 'He said that he were tired.',
      'He said me that he was tired.'],
     "O'zlashtirma gapda zamon bir pog'ona orqaga suriladi: am → was."),
    ('“I will call you,” she said.', 'She said that she would call me.',
     ['She said that she will call me.', 'She said me that she would call me.',
      'She said that she would called me.'],
     "will → would; \"say\" dan keyin \"me\" qo'yilmaydi (tell me deyiladi)."),
    ('“Where do you live?” he asked.', 'He asked where I lived.',
     ['He asked where did I live.', 'He asked where do I live.',
      'He asked me where did I lived.'],
     "O'zlashtirma so'roqda so'z tartibi darak gapniki bo'ladi va zamon orqaga suriladi."),
    ('“Don’t be late,” the teacher said.',
     'The teacher told us not to be late.',
     ['The teacher said us not be late.', 'The teacher told us don’t be late.',
      'The teacher said don’t to be late.'],
     "Buyruq gap: tell + kishi + (not) to + fe'l."),
    ('“I have finished,” he said.', 'He said that he had finished.',
     ['He said that he has finished.', 'He said that he was finished.',
      'He said that he had finish.'],
     "Present Perfect → Past Perfect: have finished → had finished."),
]


def q_reported(level, tier):
    quote, ans, wrongs, why = random.choice(_REPORTED)
    return _q("O'zlashtirma gap",
              f"Report this sentence correctly: {quote}", ans, list(wrongs), why)


# ===========================================================================
# B1 — gerund / infinitive, used to, phrasal verbs, word formation
# ===========================================================================

_GERUND = [
    ('I enjoy ___ books in the evening.', 'reading', 'read',
     "\"enjoy\" dan keyin doim -ing shakli keladi."),
    ('She finished ___ the letter an hour ago.', 'writing', 'write',
     "\"finish\" dan keyin -ing shakli keladi."),
    ('Do you mind ___ the window?', 'opening', 'open',
     "\"mind\" dan keyin -ing shakli keladi."),
    ('He avoids ___ fast food.', 'eating', 'eat',
     "\"avoid\" dan keyin -ing shakli keladi."),
    ('I am looking forward to ___ you.', 'seeing', 'see',
     "\"look forward to\" dagi \"to\" — predlog, shuning uchun undan keyin -ing."),
]

_INFINITIVE = [
    ('She decided ___ medicine at university.', 'to study', 'study',
     "\"decide\" dan keyin to + fe'l keladi."),
    ('We hope ___ you again soon.', 'to see', 'see',
     "\"hope\" dan keyin to + fe'l keladi."),
    ('He promised ___ me tomorrow.', 'to call', 'call',
     "\"promise\" dan keyin to + fe'l keladi."),
    ('They agreed ___ the price.', 'to reduce', 'reduce',
     "\"agree\" dan keyin to + fe'l keladi."),
    ('I can’t afford ___ a new laptop.', 'to buy', 'buy',
     "\"afford\" dan keyin to + fe'l keladi."),
]


def q_gerund_infinitive(level, tier):
    if random.random() < 0.5:
        text, ans, base, why = random.choice(_GERUND)
        wrongs = ['to ' + base, base, 'to ' + ans]
    else:
        text, ans, base, why = random.choice(_INFINITIVE)
        wrongs = [base + 'ing', base, 'to ' + base + 'ing']
    return _q("Gerund / Infinitive", 'Choose the correct answer: ' + text,
              ans, wrongs, why)


_USED_TO = [
    ('I ___ play football every day when I was a child.', 'used to',
     ['use to', 'am used to', 'was used to'],
     "O'tmishdagi odat — \"used to\" + fe'lning boshlang'ich shakli."),
    ('She ___ like coffee, but now she drinks it every morning.', "didn’t use to",
     ["didn’t used to", "doesn’t use to", 'wasn’t used to'],
     "Inkorda \"did\" bor, shuning uchun \"use to\" (d siz)."),
    ('There ___ be a cinema here, but they closed it.', 'used to',
     ['use to', 'is used to', 'was using to'],
     "O'tmishda mavjud bo'lgan holat — \"used to be\"."),
]


def q_used_to(level, tier):
    text, ans, wrongs, why = random.choice(_USED_TO)
    return _q("Used to", 'Choose the correct answer: ' + text,
              ans, list(wrongs), why)


_PHRASAL = [
    ('My car ___ on the way to work, so I was late.', 'broke down',
     "\"break down\" — buzilib qolmoq."),
    ('She ___ smoking two years ago.', 'gave up',
     "\"give up\" — tashlamoq, voz kechmoq."),
    ('Who ___ your little brother when your parents are at work?', 'looks after',
     "\"look after\" — qaramoq, boqmoq."),
    ('The plane ___ half an hour late.', 'took off',
     "\"take off\" — uchib ko'tarilmoq."),
    ('I ___ the truth from my sister.', 'found out',
     "\"find out\" — bilib olmoq, aniqlamoq."),
    ('Please ___ the light — it is getting dark.', 'turn on',
     "\"turn on\" — yoqmoq; \"turn off\" — o'chirmoq."),
    ('We ___ the meeting until next Monday.', 'put off',
     "\"put off\" — keyinga qoldirmoq."),
    ('I ___ an old photo of my grandfather yesterday.', 'came across',
     "\"come across\" — tasodifan topib olmoq."),
    ('We have ___ sugar — can you buy some?', 'run out of',
     "\"run out of\" — tugab qolmoq."),
]

_PHRASAL_ALL = ['broke down', 'gave up', 'looks after', 'turn on', 'put off',
                'came across', 'run out of', 'took off', 'found out',
                'got up', 'turn off', 'looked for']


def q_phrasal(level, tier):
    text, ans, why = random.choice(_PHRASAL)
    return _q("Phrasal verbs", 'Choose the correct answer: ' + text,
              ans, _others(_PHRASAL_ALL, ans), why)


_WORD_FORM = [
    ('He is a famous ___ . (science)', 'scientist',
     ['sciencer', 'scientful', 'sciencist'],
     "Kasb yasovchi qo'shimcha: science → scientist."),
    ('It was a difficult ___ . (decide)', 'decision',
     ['decidement', 'deciding', 'decidness'],
     "Fe'ldan ot yasash: decide → decision."),
    ('Money does not always bring ___ . (happy)', 'happiness',
     ['happyness', 'happyment', 'happiment'],
     "Sifatdan ot: happy → happiness (-y → -i + ness)."),
    ('This dictionary is very ___ . (use)', 'useful',
     ['useable', 'usely', 'usness'],
     "\"-ful\" qo'shimchasi \"…li, foydali\" ma'nosini beradi: use → useful."),
    ('Driving fast is ___ . (danger)', 'dangerous',
     ['dangerful', 'dangery', 'dangerable'],
     "Otdan sifat: danger → dangerous."),
    ('There is a big ___ between the two plans. (differ)', 'difference',
     ['differment', 'differness', 'differation'],
     "Fe'ldan ot: differ → difference."),
    ('We signed an ___ with the company. (agree)', 'agreement',
     ['agreeness', 'agreetion', 'agreeance'],
     "Fe'ldan ot: agree → agreement."),
    ('That is ___ — nobody can run so fast. (possible)', 'impossible',
     ['unpossible', 'dispossible', 'inpossible'],
     "\"possible\" so'zining inkori — \"impossible\" (im- qo'shimchasi)."),
    ('He was very ___ in his new job. (success)', 'successful',
     ['successive', 'successly', 'successable'],
     "Otdan sifat: success → successful."),
]


def q_word_formation(level, tier):
    text, ans, wrongs, why = random.choice(_WORD_FORM)
    return _q("So'z yasalishi", 'Choose the correct word: ' + text,
              ans, list(wrongs), why)


_DEP_PREP = [
    ('I am interested ___ history.', 'in', "\"interested in\" — barqaror birikma."),
    ('She is very good ___ maths.', 'at', "\"good at\" — barqaror birikma."),
    ('My little sister is afraid ___ dogs.', 'of', "\"afraid of\" — barqaror birikma."),
    ('It depends ___ the weather.', 'on', "\"depend on\" — barqaror birikma."),
    ('We are waiting ___ the bus.', 'for', "\"wait for\" — barqaror birikma."),
    ('Listen ___ me, please!', 'to', "\"listen to\" — barqaror birikma."),
    ('They arrived ___ the airport at six.', 'at', "\"arrive at\" (kichik joy) / \"arrive in\" (shahar, mamlakat)."),
    ('His parents are proud ___ him.', 'of', "\"proud of\" — barqaror birikma."),
    ('I am worried ___ the exam.', 'about', "\"worried about\" — barqaror birikma."),
    ('This city is famous ___ its bread.', 'for', "\"famous for\" — barqaror birikma."),
    ('Your bag is similar ___ mine.', 'to', "\"similar to\" — barqaror birikma."),
]


def q_dependent_prep(level, tier):
    text, ans, why = random.choice(_DEP_PREP)
    return _q("Barqaror predloglar", 'Choose the correct preposition: ' + text,
              ans, _others(['in', 'at', 'of', 'on', 'for', 'to', 'about', 'with'], ans),
              why)


_COLLOCATIONS = [
    ('Don’t forget to ___ your homework.', 'do', "\"do homework\" — barqaror birikma."),
    ('Everybody can ___ a mistake.', 'make', "\"make a mistake\" — barqaror birikma."),
    ('Can I ___ a photo of you?', 'take', "\"take a photo\" — barqaror birikma."),
    ('We usually ___ breakfast at seven.', 'have', "\"have breakfast\" — barqaror birikma."),
    ('It is not easy to ___ a decision.', 'make', "\"make a decision\" — barqaror birikma."),
    ('My mother is going to ___ the shopping.', 'do', "\"do the shopping\" — barqaror birikma."),
    ('More than fifty students ___ part in the competition.', 'took',
     "\"take part in\" — ishtirok etmoq."),
    ('I want to ___ a shower before dinner.', 'have', "\"have a shower\" — barqaror birikma."),
    ('It is easy to ___ friends at this school.', 'make', "\"make friends\" — barqaror birikma."),
]


def q_collocation(level, tier):
    text, ans, why = random.choice(_COLLOCATIONS)
    pool = ['do', 'make', 'take', 'have', 'took', 'get']
    return _q("Barqaror birikmalar", 'Choose the correct verb: ' + text,
              ans, _others(pool, ans), why)


_CORRECT_SENTENCE = [
    ('He has been working here since 2019.',
     ['He is working here since 2019.', 'He works here since 2019.',
      'He has been working here for 2019.'],
     "\"since 2019\" — Present Perfect (Continuous) talab qiladi; \"since\" boshlanish nuqtasi bilan ishlatiladi."),
    ('I didn’t see anybody in the room.',
     ['I didn’t saw anybody in the room.', 'I didn’t see nobody in the room.',
      'I don’t saw anybody in the room.'],
     "\"did\" dan keyin fe'l boshlang'ich shaklda; ingliz tilida ikki karra inkor ishlatilmaydi."),
    ('She asked me where I lived.',
     ['She asked me where did I live.', 'She asked me where do I live.',
      'She asked to me where I lived.'],
     "O'zlashtirma so'roqda so'z tartibi darak gapniki bo'ladi va \"did\" ishlatilmaydi."),
    ('If I had more time, I would travel more.',
     ['If I would have more time, I would travel more.',
      'If I have more time, I would travel more.',
      'If I had more time, I will travel more.'],
     "Second Conditional: If + Past Simple, would + fe'l. \"If\" dan keyin \"would\" kelmaydi."),
    ('It is the best film I have ever seen.',
     ['It is the best film I have ever saw.',
      'It is the most best film I have ever seen.',
      'It is the better film I have ever seen.'],
     "good → better → the best; Present Perfect'da 3-shakl \"seen\" ishlatiladi."),
    ('I am looking forward to seeing you.',
     ['I am looking forward to see you.', 'I am looking forward seeing you.',
      'I look forward see you.'],
     "\"look forward to\" dagi \"to\" — predlog, undan keyin -ing shakli keladi."),
    ('There isn’t much traffic today.',
     ['There isn’t many traffic today.', 'There aren’t much traffics today.',
      'There isn’t much traffics today.'],
     "\"traffic\" — sanalmaydigan ot: ko'plik shakli ham, \"many\" ham ishlatilmaydi."),
    ('The film was so boring that we left.',
     ['The film was so bored that we left.', 'The film was such boring that we left.',
      'The film was too boring that we left.'],
     "Narsa haqida -ing sifati (boring); \"so + sifat + that\" qurilmasi."),
]


def q_correct_sentence(level, tier):
    correct, wrongs, why = random.choice(_CORRECT_SENTENCE)
    return _q("To'g'ri gapni top", 'Which sentence is correct?',
              correct, list(wrongs), why)


# ===========================================================================
# YANGI SHAKLDAGI SAVOLLAR — matn, muloqot, e'lon, tarjima
#
# Bu bo'limdagi generatorlar grammatika qoidasini emas, tilni ISHLAYOTGAN
# holida so'raydi: qisqa matn va uni tushunish, javob tanlash, ko'chadagi
# yozuvni o'qish, o'zbekchadan tarjima. O'quvchi har kuni o'ynaganda ham
# bir xil "fill the gap" savoliga tushib qolmasligi uchun.
# ===========================================================================

_LVL = {'a1': 1, 'a2': 2, 'b1': 3}


def _pick(rows, level, tier=1):
    """Darajaga mos qatorni tanlaydi.

    O'quvchi hech qachon o'zidan yuqori darajadagi materialni ko'rmaydi;
    oxirgi raundda esa mavjudlarning eng qiyini afzal ko'riladi.
    """
    cap = _LVL.get(level, 1)
    pool = [r for r in rows if _LVL[r[0]] <= cap]
    if not pool:
        floor = min(_LVL[r[0]] for r in rows)
        pool = [r for r in rows if _LVL[r[0]] == floor]
    if tier >= 3:
        top = max(_LVL[r[0]] for r in pool)
        hard = [r for r in pool if _LVL[r[0]] == top]
        if hard and random.random() < 0.7:
            pool = hard
    return random.choice(pool)


# ---------------------------------------------------------------------------
# Matn tushunish — qisqa matn + savol (o'yindagi eng "yangi" shakl)
# ---------------------------------------------------------------------------

_READINGS = [
    ('a1',
     "Sardor gets up at six o'clock every morning. He has breakfast with his "
     "little sister and then walks to school. The school is very near, so he "
     "never takes the bus.",
     [("How does Sardor go to school?", "On foot.",
       ["By bus.", "By car.", "By bike."],
       "Matnda \"he walks to school\" va \"never takes the bus\" deyilgan — "
       "demak u piyoda yuradi."),
      ("Who has breakfast with Sardor?", "His sister.",
       ["His brother.", "His friend.", "His teacher."],
       "\"He has breakfast with his little sister\" — singlisi bilan.")]),

    ('a1',
     "Our classroom is on the second floor. There are twenty desks and one "
     "big window in it. The teacher's table is near the door. We have five "
     "lessons on Monday.",
     [("Where is the teacher's table?", "Near the door.",
       ["Near the window.", "On the second floor of the next building.",
        "Behind the desks."],
       "\"The teacher's table is near the door\" — eshik yonida."),
      ("How many lessons are there on Monday?", "Five.",
       ["Twenty.", "Two.", "One."],
       "\"We have five lessons on Monday\" — beshta. Yigirma — parta soni.")]),

    ('a1',
     "Malika has a small brown dog. Its name is Bobi. Bobi likes bread and "
     "milk, but he doesn't like meat. Every evening Malika and Bobi walk in "
     "the park.",
     [("What doesn't Bobi like?", "Meat.",
       ["Bread.", "Milk.", "The park."],
       "\"he doesn't like meat\" — go'shtni yoqtirmaydi."),
      ("When do they walk in the park?", "In the evening.",
       ["In the morning.", "At night.", "At lunchtime."],
       "\"Every evening\" — har kuni kechqurun.")]),

    ('a2',
     "Last summer Jasur visited his grandparents in a small village. He "
     "helped them in the garden every morning and swam in the river in the "
     "afternoon. He didn't watch television for a whole month, and he says it "
     "was the best holiday of his life.",
     [("What did Jasur do in the mornings?", "He worked in the garden.",
       ["He swam in the river.", "He watched television.",
        "He travelled to the city."],
       "\"He helped them in the garden every morning\" — ertalablari bog'da "
       "ishlagan; daryoda tushdan keyin cho'milgan."),
      ("How long didn't he watch television?", "For a month.",
       ["For a week.", "For a year.", "For two days."],
       "\"for a whole month\" — bir oy davomida.")]),

    ('a2',
     "The city library opens at nine in the morning and closes at seven in "
     "the evening. It is closed on Sundays. Students can borrow three books "
     "for two weeks. If you bring a book back late, you pay a small fine.",
     [("When is the library closed?", "On Sundays.",
       ["On Mondays.", "In the evening only.", "In summer."],
       "\"It is closed on Sundays\" — yakshanba kunlari yopiq."),
      ("How many books can a student borrow?", "Three.",
       ["Two.", "Seven.", "Nine."],
       "\"Students can borrow three books for two weeks\" — uchta kitob; "
       "\"two weeks\" esa muddat."),
      ("What happens if you return a book late?", "You pay some money.",
       ["You lose your library card.", "You get another book.",
        "Nothing happens."],
       "\"you pay a small fine\" — kichik jarima to'laysiz.")]),

    ('a2',
     "Aziza wants to become a doctor. She studies biology and chemistry very "
     "hard, and on Saturdays she works as a volunteer at the hospital near "
     "her house. She says the work is tiring, but she learns something new "
     "every week.",
     [("Where does Aziza work on Saturdays?", "At a hospital.",
       ["At a school.", "At a chemistry laboratory.", "At home."],
       "\"she works as a volunteer at the hospital\" — shifoxonada "
       "ko'ngilli bo'lib ishlaydi."),
      ("How does Aziza feel about the work?", "It is tiring but useful.",
       ["It is easy and boring.", "She doesn't like it at all.",
        "It is well paid."],
       "\"the work is tiring, but she learns something new\" — charchatadi, "
       "lekin foydali. Ko'ngilli ish — bu haq to'lanmaydigan ish.")]),

    ('b1',
     "When Kamron started his first job, he was afraid of speaking to "
     "customers. His manager gave him a simple piece of advice: listen first, "
     "then answer. Six months later Kamron was training the new staff "
     "himself, although he still says he is not a natural speaker.",
     [("What was Kamron's problem at first?", "He was afraid of talking to people.",
       ["He could not find a job.", "He did not like his manager.",
        "He arrived late every day."],
       "\"he was afraid of speaking to customers\" — mijozlar bilan "
       "gaplashishdan qo'rqardi."),
      ("What did Kamron do six months later?", "He taught the new employees.",
       ["He left the company.", "He became a manager.",
        "He stopped speaking to customers."],
       "\"Kamron was training the new staff himself\" — yangi xodimlarni "
       "o'zi o'qitardi. Menejer bo'ldi deyilmagan.")]),

    ('b1',
     "Scientists say that a short walk after lunch can help you think more "
     "clearly. In one study, office workers who walked for ten minutes made "
     "fewer mistakes in the afternoon than those who stayed at their desks. "
     "The walk does not have to be fast — the important thing is to move.",
     [("What did the study compare?", "Workers who walked and workers who did not.",
       ["Fast walkers and slow runners.", "Office workers and students.",
        "Morning walks and evening walks."],
       "Tadqiqot yurgan xodimlarni stolida qolganlar bilan solishtirgan."),
      ("According to the text, how fast should the walk be?", "The speed is not important.",
       ["As fast as possible.", "Slower than usual.",
        "Fast for ten minutes, then slow."],
       "\"The walk does not have to be fast — the important thing is to "
       "move\" — tezlik muhim emas, harakat muhim.")]),

    ('b1',
     "The old bridge in the town centre was built more than a hundred years "
     "ago. Last year the council wanted to pull it down and build a wider "
     "one, but local people collected four thousand signatures against the "
     "plan. In the end the bridge was repaired instead of being replaced.",
     [("What did the local people want?", "To keep the old bridge.",
       ["To build a wider bridge.", "To close the town centre.",
        "To collect money for a new bridge."],
       "Ular rejaga QARSHI imzo to'plashdi — ya'ni ko'prik saqlanib qolishini "
       "xohlashdi."),
      ("What happened to the bridge in the end?", "It was repaired.",
       ["It was pulled down.", "It was made wider.", "It was sold."],
       "\"the bridge was repaired instead of being replaced\" — "
       "almashtirilmadi, ta'mirlandi.")]),
]


def q_mini_reading(level, tier):
    row = _pick(_READINGS, level, tier)
    passage = row[1]
    question, correct, wrongs, why = random.choice(row[2])
    return _q("Matn tushunish", f"{passage}\n\n{question}", correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Muloqot — eng mos javobni tanlash
# ---------------------------------------------------------------------------

_DIALOGUES = [
    ('a1', "Thank you very much for your help!", "You're welcome.",
     ["Here you are.", "Yes, please.", "Never mind me."],
     "\"You're welcome\" — rahmatga beriladigan odatiy javob (\"arzimaydi\")."),
    ('a1', "How are you today?", "I'm fine, thanks.",
     ["I'm twelve.", "It's fine weather.", "Yes, I am today."],
     "\"How are you?\" — ahvol so'raydi, yosh yoki ob-havo emas."),
    ('a1', "What's your name?", "My name is Aziza.",
     ["I'm from Bukhara.", "I'm eleven years old.", "She is Aziza."],
     "Ism so'ralyapti: \"My name is …\"."),
    ('a1', "Here is your book.", "Thank you.",
     ["You're welcome.", "Never mind.", "Not at all."],
     "Narsa berilganda avval rahmat aytiladi; \"You're welcome\" — rahmatga "
     "javob."),
    ('a1', "Excuse me, where is the bus station?", "It's over there, next to the bank.",
     ["I go by bus every day.", "Yes, it is a station.", "The bus is very old."],
     "Savol JOY haqida — javob ham joyni ko'rsatishi kerak."),
    ('a2', "I'm sorry, I broke your cup.", "Never mind, it doesn't matter.",
     ["You're welcome.", "Yes, please do.", "Congratulations!"],
     "Uzr so'ralganda \"Never mind / It doesn't matter\" deyiladi. "
     "\"You're welcome\" — faqat rahmatga javob."),
    ('a2', "Would you like some more tea?", "No, thank you. I'm fine.",
     ["Yes, I would like it yesterday.", "No, I don't like you.",
      "Yes, I am some tea."],
     "\"Would you like…?\" taklifiga muloyim rad javobi — \"No, thank you\"."),
    ('a2', "Shall we meet at six?", "That sounds good.",
     ["Yes, I met him.", "I am meeting six.", "It sounds well."],
     "Taklifga rozilik: \"That sounds good\". \"Sounds\" dan keyin sifat "
     "keladi (good), ravish emas."),
    ('a2', "How was your weekend?", "It was great, thanks.",
     ["I will go to the park.", "Yes, it was.", "I have a weekend."],
     "Savol o'tgan zamonda — javob ham o'tgan zamonda va mazmunli bo'lishi kerak."),
    ('a2', "Can I open the window?", "Of course, go ahead.",
     ["Yes, I can.", "No, I am not.", "You can opened it."],
     "Ruxsat so'ralyapti: \"Of course, go ahead\" — marhamat. \"Yes, I can\" "
     "o'zi haqida bo'lib qoladi."),
    ('b1', "I've just passed my driving test!", "Congratulations! Well done.",
     ["Never mind.", "I'm sorry to hear that.", "Bless you."],
     "Yaxshi xabarga tabrik aytiladi. \"I'm sorry to hear that\" — yomon "
     "xabarga."),
    ('b1', "I'm afraid I can't come to your party.", "That's a pity. Maybe next time.",
     ["Congratulations!", "You're welcome.", "That's very kind of you."],
     "Yomon xabarga afsus bildiriladi: \"That's a pity\"."),
    ('b1', "Do you mind if I sit here?", "Not at all, please do.",
     ["Yes, of course, sit down.", "Yes, I don't mind.", "No, you can't."],
     "\"Do you mind…?\" — \"qarshi emasmisiz?\". Rozilik INKOR bilan "
     "beriladi: \"Not at all\". \"Yes\" — bu \"qarshiman\" degani."),
    ('b1', "Could you give me a hand with these boxes?", "Sure, no problem.",
     ["Yes, here is my hand.", "I have two hands.", "No, I couldn't."],
     "\"give me a hand\" — yordam berish iborasi, qo'l uzatish emas."),
    ('b1', "I think we should leave earlier tomorrow.", "You may be right, actually.",
     ["I think so too much.", "Yes, I am agree.", "It is depends."],
     "\"You may be right\" — muloyim rozilik. \"I am agree\" va \"it is "
     "depends\" — keng tarqalgan xatolar (to'g'risi: I agree / it depends)."),
]


def q_dialogue(level, tier):
    lvl, line, correct, wrongs, why = _pick(_DIALOGUES, level, tier)
    return _q("Muloqot",
              f"Choose the best reply.\n\nA:  {line}\nB:  ___",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Belgilar va e'lonlar — ko'chadagi, do'kondagi, maktabdagi yozuvlar
# ---------------------------------------------------------------------------

_SIGNS = [
    ('a1', "NO PARKING", "You cannot leave your car here.",
     ["You can park for free.", "The car park is full.",
      "Parking costs money."],
     "\"No parking\" — bu yerda mashina qo'yish mumkin emas."),
    ('a1', "OPEN  9:00 – 18:00", "You can come in at ten o'clock.",
     ["The shop is open all night.", "The shop opens at six.",
      "The shop is closed today."],
     "Do'kon 9:00 dan 18:00 gacha ochiq, demak soat 10:00 da kirish mumkin."),
    ('a1', "PUSH", "Push the door to open it.",
     ["Pull the door to open it.", "The door is locked.",
      "Knock before you enter."],
     "\"Push\" — itaring; \"pull\" — torting."),
    ('a2', "SALE — ALL SHOES 50% OFF", "Shoes cost half the usual price.",
     ["Shoes cost fifty dollars.", "You must buy fifty pairs.",
      "Only fifty pairs are left."],
     "\"50% off\" — narxdan 50% chegirma, ya'ni yarim narx."),
    ('a2', "OUT OF ORDER", "This machine is not working.",
     ["This machine is free today.", "Please stand in order.",
      "The machine is new."],
     "\"Out of order\" — ishlamayapti, buzuq."),
    ('a2', "NO FOOD OR DRINK BEYOND THIS POINT", "You must finish your drink before you go in.",
     ["Food is sold inside.", "You can eat but not drink.",
      "Drinks are free inside."],
     "Bu chiziqdan narida ovqat ham, ichimlik ham mumkin emas."),
    ('a2', "STAFF ONLY", "Customers must not go in.",
     ["Everybody is welcome.", "Only children may enter.",
      "You must pay to enter."],
     "\"Staff only\" — faqat xodimlar uchun."),
    ('b1', "PLEASE QUEUE HERE — TICKETS CHECKED AT THE DOOR",
     "Wait in a line and show your ticket at the entrance.",
     ["Buy your ticket at the door.", "Tickets are not needed here.",
      "The door is closed for today."],
     "\"Queue\" — navbatda turmoq; chiptalar eshikda TEKSHIRILADI, "
     "sotilmaydi."),
    ('b1', "LIFT UNDER REPAIR — PLEASE USE THE STAIRS",
     "You have to walk up today.",
     ["The stairs are dangerous.", "The lift is faster today.",
      "The building is closed."],
     "Lift ta'mirda, shuning uchun zinadan yurish kerak."),
    ('b1', "LAST ORDERS 30 MINUTES BEFORE CLOSING",
     "You cannot order anything in the final half hour.",
     ["The restaurant closes in thirty minutes.",
      "Orders take thirty minutes.", "You must order thirty minutes early "
      "on the phone."],
     "\"Last orders\" — oxirgi buyurtma qabul qilinadigan vaqt: yopilishdan "
     "yarim soat oldin."),
    ('b1', "TICKETS ARE NON-REFUNDABLE", "You cannot get your money back.",
     ["Tickets are free.", "You can change the date for free.",
      "You must pay again at the door."],
     "\"Non-refundable\" — pul qaytarilmaydi."),
]


def q_sign(level, tier):
    lvl, sign, correct, wrongs, why = _pick(_SIGNS, level, tier)
    return _q("Belgilar va e'lonlar",
              f"You see this notice:\n\n«  {sign}  »\n\nWhat does it mean?",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Tarjima — o'zbekcha gapga mos ingliz gapini tanlash
# ---------------------------------------------------------------------------

_TRANSLATIONS = [
    ('a1', "Mening ikkita akam bor.", "I have two brothers.",
     ["I am two brothers.", "I have two brother.", "My two brothers."],
     "\"…bor\" — have; \"two\" dan keyin ot ko'plikda: brothers."),
    ('a1', "U har kuni maktabga boradi.", "She goes to school every day.",
     ["She go to school every day.", "She is go to school every day.",
      "She going to school every day."],
     "Present Simple, 3-shaxs birlik: go → goes."),
    ('a1', "Bu mening kitobim emas.", "This is not my book.",
     ["This not my book.", "This is not mine book.", "It is not my a book."],
     "Inkorda \"is not\" kerak; \"my\" dan keyin ot keladi (mine — yolg'iz "
     "ishlatiladi)."),
    ('a1', "Stolda uchta olma bor.", "There are three apples on the table.",
     ["There is three apples on the table.", "On the table have three apples.",
      "There are three apple on the table."],
     "Ko'plik uchun \"there are\"; \"three\" dan keyin apples."),
    ('a2', "Kecha biz kino ko'rdik.", "We watched a film yesterday.",
     ["We watch a film yesterday.", "We are watched a film yesterday.",
      "We did watched a film yesterday."],
     "\"Yesterday\" — Past Simple: watch → watched."),
    ('a2', "Men futbol o'ynashni yaxshi ko'raman.", "I like playing football.",
     ["I like play football.", "I am like to playing football.",
      "I like to playing football."],
     "\"like\" dan keyin -ing yoki \"to play\" keladi; \"like play\" "
     "noto'g'ri."),
    ('a2', "U hozir uxlayapti.", "He is sleeping now.",
     ["He sleeps now.", "He sleeping now.", "He is sleep now."],
     "\"hozir\" — Present Continuous: is + -ing."),
    ('a2', "Menda pul yo'q.", "I don't have any money.",
     ["I don't have no money.", "I have not any money's.",
      "I haven't got no money."],
     "Ingliz tilida ikki karra inkor bo'lmaydi: don't + any."),
    ('a2', "U mendan uzunroq.", "He is taller than me.",
     ["He is more tall than me.", "He is taller that me.",
      "He is the taller than me."],
     "Qisqa sifatda -er qo'shiladi va \"than\" ishlatiladi."),
    ('b1', "Agar vaqtim bo'lsa, senga yordam beraman.",
     "If I have time, I will help you.",
     ["If I will have time, I will help you.",
      "If I had time, I will help you.", "If I have time, I helped you."],
     "First Conditional: \"if\" dan keyin Present Simple, asosiy gapda will."),
    ('b1', "Men bu filmni ilgari ko'rganman.", "I have seen this film before.",
     ["I have saw this film before.", "I am seen this film before.",
      "I did seen this film before."],
     "Present Perfect: have + 3-shakl (see → seen)."),
    ('b1', "Uy kecha tozalandi.", "The house was cleaned yesterday.",
     ["The house is cleaned yesterday.", "The house was clean yesterday.",
      "The house were cleaned yesterday."],
     "O'tgan zamon majhul nisbati: was/were + 3-shakl. \"House\" birlik — was."),
    ('b1', "U menga qayerda yashashimni so'radi.", "He asked me where I lived.",
     ["He asked me where did I live.", "He asked me where do I live.",
      "He asked me where I did live."],
     "O'zlashtirma so'roqda so'z tartibi darak gapniki bo'ladi, \"did\" "
     "ishlatilmaydi."),
    ('b1', "Bu kitobni o'qishga arziydi.", "This book is worth reading.",
     ["This book is worth to read.", "This book is worth read.",
      "This book worth reading."],
     "\"be worth\" dan keyin doim -ing shakli keladi."),
]


def q_translate(level, tier):
    lvl, uz, correct, wrongs, why = _pick(_TRANSLATIONS, level, tier)
    return _q("Tarjima",
              f"Choose the correct English sentence.\n\nO'zbekcha:  {uz}",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# So'z tartibi
# ---------------------------------------------------------------------------

_WORD_ORDER = [
    ('a1', "she / to school / goes / every day", "She goes to school every day.",
     ["She goes every day to school.", "Every day goes she to school.",
      "She to school goes every day."],
     "Ingliz gapida tartib: ega + fe'l + to'ldiruvchi + payt."),
    ('a1', "have / I / a new / bike", "I have a new bike.",
     ["I have a bike new.", "A new bike I have.", "I a new bike have."],
     "Sifat otdan OLDIN keladi: a new bike."),
    ('a1', "is / where / your father", "Where is your father?",
     ["Where your father is?", "Where is father your?",
      "Your father is where?"],
     "So'roq gapda \"is\" egadan oldin keladi."),
    ('a2', "often / we / go / to the cinema", "We often go to the cinema.",
     ["We go often to the cinema.", "Often we go to the cinema every week.",
      "We go to the cinema often we do."],
     "Takrorlanish ravishi (often) asosiy fe'ldan OLDIN turadi."),
    ('a2', "did / what / you / do / yesterday", "What did you do yesterday?",
     ["What you did do yesterday?", "What did you did yesterday?",
      "What do you did yesterday?"],
     "So'roqda: so'roq so'zi + did + ega + fe'lning boshlang'ich shakli."),
    ('a2', "a / red / big / car / is / it", "It is a big red car.",
     ["It is a red big car.", "It is big a red car.", "It a big red car is."],
     "Sifatlar tartibi: hajm → rang (big red car)."),
    ('b1', "to the party / invited / were / they / last night",
     "They were invited to the party last night.",
     ["They were invited last night to the party.",
      "Last night they invited were to the party.",
      "They was invited to the party last night."],
     "Majhul nisbat: were + invited; payt so'zi odatda gap oxirida."),
    ('b1', "never / have / I / such a thing / seen", "I have never seen such a thing.",
     ["I have seen never such a thing.", "Never I have seen such a thing.",
      "I never have seen such a thing."],
     "\"never\" have va asosiy fe'l ORASIDA turadi."),
    ('b1', "how long / been / have / waiting / you", "How long have you been waiting?",
     ["How long you have been waiting?", "How long have been you waiting?",
      "How long you been waiting have?"],
     "So'roqda yordamchi fe'l (have) egadan oldin: have you been…"),
]


def q_word_order(level, tier):
    lvl, jumbled, correct, wrongs, why = _pick(_WORD_ORDER, level, tier)
    return _q("So'z tartibi",
              f"Put the words in the correct order:\n\n({jumbled})",
              correct, list(wrongs), why)
# ---------------------------------------------------------------------------
# Chalkash so'zlar (its/it's, their/there, your/you're …)
# ---------------------------------------------------------------------------

_CONFUSABLES = [
    ('a1', "___ my best friend.", "He's", ["His", "He", "Him"],
     "\"He's\" = he is. \"His\" — egalik (uning kitobi)."),
    ('a1', "Is this ___ pen?", "your", ["you're", "yours", "you"],
     "Otdan oldin \"your\" (sizning); \"you're\" = you are."),
    ('a1', "The dog is in ___ house.", "its", ["it's", "its'", "him"],
     "\"its\" — egalik (uning); \"it's\" = it is."),
    ('a2', "___ are two cats in the garden.", "There", ["Their", "They're", "Theirs"],
     "\"There are\" — mavjudlik; \"their\" — ularning; \"they're\" = they are."),
    ('a2', "This box is ___ heavy for me to carry.", "too",
     ["to", "two", "also"],
     "\"too + sifat\" — haddan ziyod; \"to\" — predlog, \"two\" — 2 soni."),
    ('a2', "I like tea more ___ coffee.", "than", ["then", "that", "as"],
     "Solishtirishda \"than\"; \"then\" — keyin, so'ngra."),
    ('a2', "We ___ our keys yesterday.", "lost", ["loose", "lose", "loosed"],
     "\"lose\" (yo'qotmoq) → lost; \"loose\" — keng, bo'sh (sifat)."),
    ('a2', "It's too ___ in this room. I can't hear anything.", "quiet",
     ["quite", "quit", "quietly"],
     "\"quiet\" — jim; \"quite\" — ancha; \"quit\" — tashlab ketmoq."),
    ('b1', "___ going to be late if we don't hurry.", "We're",
     ["Were", "Where", "Wear"],
     "\"We're\" = we are. \"Were\" — o'tgan zamon, \"where\" — qayerda."),
    ('b1', "The news had a strong ___ on everybody.", "effect",
     ["affect", "affects", "effected"],
     "\"effect\" — ot (ta'sir), \"affect\" — fe'l (ta'sir qilmoq)."),
    ('b1', "You should ___ the letter before you send it.", "read",
     ["red", "reed", "readed"],
     "\"read\" — o'qimoq; \"red\" — qizil. \"Read\" noto'g'ri fe'l, "
     "-ed olmaydi."),
    ('b1', "He gave me some good ___ about the exam.", "advice",
     ["advise", "advices", "advises"],
     "\"advice\" — sanalmaydigan ot (maslahat), \"advise\" — fe'l."),
    ('b1', "The students left ___ books in the classroom.", "their",
     ["there", "they're", "theirs"],
     "\"their\" — ularning (otdan oldin); \"there\" — u yerda, "
     "\"they're\" = they are, \"theirs\" — otsiz ishlatiladi."),
]


def q_confusable(level, tier):
    lvl, text, correct, wrongs, why = _pick(_CONFUSABLES, level, tier)
    return _q("Chalkash so'zlar", "Choose the correct word:  " + text,
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Imlo
# ---------------------------------------------------------------------------

_SPELLING = [
    ('a1', "because", ["becouse", "becuase", "becose"], "sabab, chunki"),
    ('a1', "beautiful", ["beatiful", "beutiful", "beautifull"], "chiroyli"),
    ('a1', "friend", ["freind", "frend", "friand"], "do'st"),
    ('a1', "children", ["childrens", "childern", "childrin"], "bolalar"),
    ('a1', "Wednesday", ["Wensday", "Wednsday", "Wedensday"], "chorshanba"),
    ('a2', "different", ["diffrent", "diferent", "differant"], "farqli"),
    ('a2', "favourite", ["favorit", "favourit", "favuorite"], "eng yoqtirgan"),
    ('a2', "restaurant", ["restarant", "restaurent", "resturant"], "restoran"),
    ('a2', "interesting", ["intresting", "interessting", "intereting"], "qiziqarli"),
    ('a2', "tomorrow", ["tommorow", "tomorow", "tommorrow"], "ertaga"),
    ('b1', "necessary", ["neccessary", "necesary", "necessery"], "zarur"),
    ('b1', "environment", ["enviroment", "envirinment", "enviornment"], "atrof-muhit"),
    ('b1', "government", ["goverment", "governement", "govermment"], "hukumat"),
    ('b1', "successful", ["succesful", "successfull", "sucessful"], "muvaffaqiyatli"),
    ('b1', "recommend", ["recomend", "reccomend", "recommand"], "tavsiya qilmoq"),
]


def q_spelling(level, tier):
    lvl, correct, wrongs, meaning = _pick(_SPELLING, level, tier)
    return _q("Imlo", "Which word is spelled correctly?",
              correct, list(wrongs),
              f"To'g'ri yozilishi — \"{correct}\" ({meaning}).")


# ---------------------------------------------------------------------------
# Talaffuz — tovushi boshqacha so'zni topish
# ---------------------------------------------------------------------------

_SOUNDS = [
    ('a1', ["cat", "hat", "map", "cake"], "cake",
     "cat, hat, map — qisqa /æ/; \"cake\" da esa /eɪ/ (oxiridagi -e "
     "unlini uzaytiradi)."),
    ('a1', ["red", "bed", "ten", "he"], "he",
     "red, bed, ten — qisqa /e/; \"he\" da uzun /iː/."),
    ('a1', ["book", "look", "good", "food"], "food",
     "book, look, good — qisqa /ʊ/; \"food\" da uzun /uː/."),
    ('a2', ["school", "chemistry", "character", "chair"], "chair",
     "school, chemistry, character — \"ch\" /k/ bo'lib o'qiladi; "
     "\"chair\" da esa /tʃ/."),
    ('a2', ["walked", "helped", "watched", "wanted"], "wanted",
     "-ed odatda /t/ yoki /d/; \"wanted\" da esa /ɪd/ — chunki o'zak "
     "t/d bilan tugaydi."),
    ('a2', ["some", "come", "love", "home"], "home",
     "some, come, love — /ʌ/; \"home\" da /əʊ/."),
    ('a2', ["say", "day", "may", "said"], "said",
     "say, day, may — /eɪ/; \"said\" esa /sed/ bo'lib o'qiladi — juda "
     "ko'p uchraydigan istisno."),
    ('b1', ["thought", "through", "though", "throw"], "though",
     "thought, through, throw — o'zak \"th\" jarangsiz /θ/; \"though\" "
     "da jarangli /ð/."),
    ('b1', ["heart", "learn", "earth", "search"], "heart",
     "learn, earth, search — /ɜː/; \"heart\" da esa /ɑː/."),
    ('b1', ["blood", "flood", "food", "does"], "food",
     "blood, flood, does — /ʌ/; \"food\" da uzun /uː/."),
    ('b1', ["climb", "comb", "lamb", "club"], "club",
     "climb, comb, lamb — oxirgi \"b\" o'qilmaydi; \"club\" da esa /b/ "
     "aniq eshitiladi."),
]


def q_sound(level, tier):
    lvl, words, odd, why = _pick(_SOUNDS, level, tier)
    others = [w for w in words if w != odd]
    return _q("Talaffuz",
              "Which word sounds different from the others?\n\n"
              + " · ".join(words),
              odd, others, why)


# ---------------------------------------------------------------------------
# Sinonim — ma'nosi eng yaqin so'z
# ---------------------------------------------------------------------------

_SYNONYMS = [
    ('a1', "big", "large", ["small", "long", "old"], "big = large — katta."),
    ('a1', "happy", "glad", ["angry", "tired", "hungry"], "happy = glad — xursand."),
    ('a1', "start", "begin", ["finish", "stop", "close"], "start = begin — boshlamoq."),
    ('a2', "quick", "fast", ["slow", "quiet", "late"], "quick = fast — tez."),
    ('a2', "buy", "purchase", ["sell", "borrow", "pay"], "buy = purchase — sotib olmoq."),
    ('a2', "difficult", "hard", ["easy", "heavy", "boring"],
     "difficult = hard — qiyin (\"hard\" ning yana bir ma'nosi — qattiq)."),
    ('a2', "cheap", "inexpensive", ["expensive", "free", "rich"],
     "cheap = inexpensive — arzon."),
    ('b1', "enormous", "huge", ["tiny", "narrow", "empty"],
     "enormous = huge — juda katta."),
    ('b1', "reply", "respond", ["ask", "repeat", "refuse"],
     "reply = respond — javob bermoq."),
    ('b1', "keep", "retain", ["throw away", "lend", "lose"],
     "keep = retain — saqlab qolmoq."),
    ('b1', "annoying", "irritating", ["relaxing", "amusing", "surprising"],
     "annoying = irritating — asabga tegadigan."),
    ('b1', "obtain", "get", ["give", "avoid", "spend"], "obtain = get — olmoq."),
    ('b1', "sufficient", "enough", ["extra", "missing", "rare"],
     "sufficient = enough — yetarli."),
]


def q_synonym(level, tier):
    lvl, word, correct, wrongs, why = _pick(_SYNONYMS, level, tier)
    return _q("Sinonim",
              f"Which word is closest in meaning to \"{word}\"?",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Question tags
# ---------------------------------------------------------------------------

_TAGS = [
    ('a2', "You are from Namangan, ___", "aren't you?",
     ["are you?", "isn't it?", "don't you?"],
     "Darak gap tasdiq bo'lsa, tag INKOR bo'ladi va o'sha yordamchi fe'l "
     "takrorlanadi: are → aren't you?"),
    ('a2', "She likes ice cream, ___", "doesn't she?",
     ["isn't she?", "does she?", "didn't she?"],
     "Present Simple, 3-shaxs: likes → doesn't she?"),
    ('a2', "They didn't come, ___", "did they?",
     ["didn't they?", "do they?", "were they?"],
     "Gap inkor bo'lsa, tag TASDIQ bo'ladi: didn't → did they?"),
    ('b1', "He has finished his work, ___", "hasn't he?",
     ["isn't he?", "doesn't he?", "has he?"],
     "\"has\" — yordamchi fe'l, tagda o'sha takrorlanadi: hasn't he?"),
    ('b1', "Let's go for a walk, ___", "shall we?",
     ["will we?", "do we?", "don't we?"],
     "\"Let's\" bilan boshlangan gapning tagi doim \"shall we?\"."),
    ('b1', "There is nothing we can do, ___", "is there?",
     ["isn't there?", "is it?", "does it?"],
     "\"There is\" ning egasi — \"there\". \"Nothing\" gapni allaqachon "
     "inkor qilgani uchun tag tasdiq bo'ladi."),
    ('b1', "I'm late, ___", "aren't I?",
     ["amn't I?", "am I?", "isn't it?"],
     "\"I am\" ning tagi istisno: \"aren't I?\" (amn't shakli yo'q)."),
    ('b1', "Nobody phoned, ___", "did they?",
     ["didn't they?", "did he?", "did nobody?"],
     "\"Nobody\" inkor ma'noli — tag tasdiq; odamlar uchun \"they\" "
     "ishlatiladi."),
]


def q_tag(level, tier):
    lvl, text, correct, wrongs, why = _pick(_TAGS, level, tier)
    return _q("Question tag", "Complete the question tag:  " + text,
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# So / Neither — "men ham"
# ---------------------------------------------------------------------------

_SO_NEITHER = [
    ('a2', "I like pizza.", "So do I.", ["So am I.", "Neither do I.", "So I do."],
     "Tasdiqqa qo'shilish: So + yordamchi fe'l + ega. \"like\" — Present "
     "Simple, demak \"So do I\"."),
    ('a2', "I am tired.", "So am I.", ["So do I.", "Neither am I.", "Me too am."],
     "\"am\" fe'li takrorlanadi: So am I."),
    ('a2', "I don't like coffee.", "Neither do I.",
     ["So do I.", "Neither am I.", "I don't too."],
     "Inkorga qo'shilish: Neither + yordamchi fe'l + ega."),
    ('b1', "I have never been to Korea.", "Neither have I.",
     ["So have I.", "Neither did I.", "Neither I have."],
     "\"have\" takrorlanadi va inkor bo'lgani uchun \"Neither have I\"."),
    ('b1', "I went to the concert.", "So did I.",
     ["So do I.", "Neither did I.", "So was I."],
     "Past Simple uchun yordamchi fe'l — did: So did I."),
    ('b1', "I can't swim.", "Neither can I.",
     ["So can I.", "Neither do I.", "I can't neither."],
     "Modal fe'l takrorlanadi: Neither can I."),
    ('b1', "I would love to travel more.", "So would I.",
     ["So do I.", "Neither would I.", "So I would love."],
     "\"would\" takrorlanadi: So would I."),
]


def q_so_neither(level, tier):
    lvl, line, correct, wrongs, why = _pick(_SO_NEITHER, level, tier)
    return _q("So / Neither",
              f"Agree with the speaker.\n\nA:  {line}\nB:  ___",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Idiomalar
# ---------------------------------------------------------------------------

_IDIOMS = [
    ('a2', "It's raining cats and dogs.", "It is raining very hard.",
     ["There are animals in the street.", "The weather is nice.",
      "It is snowing a little."],
     "\"raining cats and dogs\" — chelaklab yomg'ir quymoq."),
    ('a2', "Break a leg!", "Good luck!",
     ["Be careful, it is dangerous.", "I am angry with you.",
      "Sit down and rest."],
     "Sahnaga chiqayotgan odamga \"omad\" tilashning eski usuli."),
    ('a2', "It's a piece of cake.", "It is very easy.",
     ["It is delicious.", "It is expensive.", "It is a small portion."],
     "\"a piece of cake\" — juda oson ish."),
    ('b1', "He let the cat out of the bag.", "He told a secret.",
     ["He lost his pet.", "He opened his bag.", "He made a big mistake in maths."],
     "\"let the cat out of the bag\" — sirni oshkor qilmoq."),
    ('b1', "She is under the weather today.", "She feels ill.",
     ["She is outside in the rain.", "She is very busy.", "She is in a bad mood "
      "because of the news."],
     "\"under the weather\" — o'zini yaxshi his qilmayapti."),
    ('b1', "Let's call it a day.", "Let's stop working now.",
     ["Let's meet tomorrow.", "Let's give it a name.",
      "Let's work all day."],
     "\"call it a day\" — bugungi ishni to'xtatmoq."),
    ('b1', "That book cost an arm and a leg.", "It was very expensive.",
     ["It was very heavy.", "It was a medical book.", "It was free."],
     "\"cost an arm and a leg\" — juda qimmat."),
    ('b1', "He is always beating about the bush.", "He never says things directly.",
     ["He works in a garden.", "He is very violent.",
      "He walks in the forest every day."],
     "\"beat about the bush\" — gapni aylantirmoq, to'g'ridan aytmaslik."),
    ('b1', "We are in the same boat.", "We have the same problem.",
     ["We are travelling together.", "We agree with each other.",
      "We are both sailors."],
     "\"in the same boat\" — bir xil ahvolda."),
]


def q_idiom(level, tier):
    lvl, sentence, correct, wrongs, why = _pick(_IDIOMS, level, tier)
    return _q("Idiomalar",
              f"What does the speaker mean?\n\n\"{sentence}\"",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Soat (ingliz tilida)
# ---------------------------------------------------------------------------

_HOUR_WORDS = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve']
_MIN_WORDS = {5: 'five', 10: 'ten', 20: 'twenty', 25: 'twenty-five'}


def _clock_words(h, m):
    nxt = _HOUR_WORDS[h % 12 + 1] if h % 12 + 1 <= 12 else _HOUR_WORDS[1]
    cur = _HOUR_WORDS[h if h else 12]
    if m == 0:
        return f"{cur} o'clock"
    if m == 15:
        return f"a quarter past {cur}"
    if m == 30:
        return f"half past {cur}"
    if m == 45:
        return f"a quarter to {nxt}"
    if m < 30:
        return f"{_MIN_WORDS[m]} past {cur}"
    return f"{_MIN_WORDS[60 - m]} to {nxt}"


def q_time_english(level, tier):
    h = random.randint(1, 12)
    m = random.choice((0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55))
    correct = _clock_words(h, m)
    cur = _HOUR_WORDS[h]
    nxt = _HOUR_WORDS[h % 12 + 1]
    wrongs = []
    if m == 0:
        wrongs = [f"o'clock {cur}", f"a quarter past {cur}", f"half past {cur}"]
    elif m == 15:
        wrongs = [f"a quarter to {cur}", f"a quarter past {nxt}",
                  f"fifteen to {cur}"]
    elif m == 30:
        wrongs = [f"half to {nxt}", f"half past {nxt}", f"a half past {cur}"]
    elif m == 45:
        wrongs = [f"a quarter past {cur}", f"a quarter to {cur}",
                  f"forty-five past {cur}"]
    elif m < 30:
        wrongs = [f"{_MIN_WORDS[m]} to {cur}", f"{_MIN_WORDS[m]} past {nxt}",
                  f"{_MIN_WORDS[m]} after to {cur}"]
    else:
        wrongs = [f"{_MIN_WORDS[60 - m]} past {cur}",
                  f"{_MIN_WORDS[60 - m]} to {cur}",
                  f"{_MIN_WORDS[60 - m]} before {nxt}"]
    if m == 0:
        why = f"Daqiqa nol bo'lsa: \"{correct}\" — soat roppa-rosa {h}."
    elif m < 30:
        why = (f"Yarim soatgacha \"past\" (o'tdi) ishlatiladi va O'TGAN soat "
               f"aytiladi: {h}:{m:02d} → \"{correct}\".")
    elif m == 30:
        why = f"Yarim soat: \"half past {cur}\" — {h}:30."
    else:
        why = (f"Yarim soatdan keyin \"to\" (qoldi) ishlatiladi va KEYINGI "
               f"soat aytiladi: {h}:{m:02d} → \"{correct}\".")
    return _q("Soat (English)",
              f"How do we say this time in English?\n\n{h}:{m:02d}",
              correct, wrongs, why)


# ---------------------------------------------------------------------------
# Sanalar va tartib sonlar
# ---------------------------------------------------------------------------

_ORDINALS = {
    1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth',
    7: 'seventh', 8: 'eighth', 9: 'ninth', 10: 'tenth', 11: 'eleventh',
    12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth',
    16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth',
    20: 'twentieth', 21: 'twenty-first', 22: 'twenty-second',
    23: 'twenty-third', 25: 'twenty-fifth', 28: 'twenty-eighth',
    30: 'thirtieth', 31: 'thirty-first',
}
_CARDINALS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
    21: 'twenty-one', 22: 'twenty-two', 23: 'twenty-three', 25: 'twenty-five',
    28: 'twenty-eight', 30: 'thirty', 31: 'thirty-one',
}
_MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                'August', 'September', 'October', 'November', 'December']


def q_date_ordinal(level, tier):
    n = random.choice(sorted(_ORDINALS))
    correct_ord = _ORDINALS[n]
    if random.random() < 0.5:
        wrongs = [_CARDINALS[n] + 'th', _CARDINALS[n], correct_ord + 'th']
        wrongs = [w for w in dict.fromkeys(wrongs) if w != correct_ord]
        wrongs.append(_ORDINALS[n + 1] if n + 1 in _ORDINALS else _ORDINALS[1])
        why = (f"{n} ning tartib soni — \"{correct_ord}\". Sanalar va "
               f"tartiblar doim tartib son bilan aytiladi.")
        return _q("Sanalar va tartib sonlar",
                  f"What is the ordinal form of {n}?", correct_ord, wrongs, why)
    month = random.choice(_MONTH_NAMES)
    correct = f"the {correct_ord} of {month}"
    wrongs = [f"the {_CARDINALS[n]} of {month}",
              f"{month} the {_CARDINALS[n]}",
              f"the {correct_ord} {month} of"]
    why = (f"Sana \"the + tartib son + of + oy\" tarzida aytiladi: "
           f"\"{correct}\".")
    return _q("Sanalar va tartib sonlar",
              f"How do we say this date?\n\n{n} {month}", correct, wrongs, why)


# ---------------------------------------------------------------------------
# Davlatlar, millatlar va tillar
# ---------------------------------------------------------------------------

_NATIONS = [
    ("Uzbekistan", "Uzbek", "Uzbek"),
    ("Korea", "Korean", "Korean"),
    ("Japan", "Japanese", "Japanese"),
    ("Turkey", "Turkish", "Turkish"),
    ("France", "French", "French"),
    ("Spain", "Spanish", "Spanish"),
    ("Germany", "German", "German"),
    ("Italy", "Italian", "Italian"),
    ("China", "Chinese", "Chinese"),
    ("Russia", "Russian", "Russian"),
    ("Britain", "British", "English"),
    ("Poland", "Polish", "Polish"),
]


def q_nationality(level, tier):
    country, nation, lang = random.choice(_NATIONS)
    others = [n for c, n, l in _NATIONS if n != nation]
    if random.random() < 0.5:
        why = (f"{country} — davlat nomi, undan yasalgan millat sifati — "
               f"\"{nation}\".")
        return _q("Davlatlar va millatlar",
                  f"People from {country} are ___.", nation,
                  random.sample(others, 3), why)
    langs = [l for c, n, l in _NATIONS if l != lang]
    why = f"{country}da {lang} tilida gapiriladi."
    return _q("Davlatlar va millatlar",
              f"What language do people speak in {country}?", lang,
              random.sample(sorted(set(langs)), 3), why)


# ---------------------------------------------------------------------------
# O'lchov birikmalari (a slice of bread…)
# ---------------------------------------------------------------------------

_MEASURES = [
    ('a1', "a ___ of water", "bottle", ["slice", "piece", "loaf"],
     "Suv uchun — \"a bottle of water\" (bir shisha suv)."),
    ('a1', "a ___ of bread", "loaf", ["bottle", "cup", "bar"],
     "Butun non uchun — \"a loaf of bread\"; bir bo'lagi — \"a slice\"."),
    ('a1', "a ___ of tea", "cup", ["loaf", "bar", "slice"],
     "Issiq ichimlik piyolada: \"a cup of tea\"."),
    ('a2', "a ___ of chocolate", "bar", ["loaf", "bottle", "sheet"],
     "Shokolad plitkasi — \"a bar of chocolate\"."),
    ('a2', "a ___ of paper", "sheet", ["bar", "cup", "loaf"],
     "Bir varaq qog'oz — \"a sheet of paper\"."),
    ('a2', "a ___ of shoes", "pair", ["couple", "set", "group"],
     "Juft narsalar uchun \"a pair of\": shoes, trousers, glasses."),
    ('a2', "a ___ of sugar", "kilo", ["slice", "sheet", "bar"],
     "Sanalmaydigan narsa o'lchov bilan aytiladi: a kilo of sugar."),
    ('b1', "a ___ of advice", "piece", ["slice", "bar", "loaf"],
     "\"Advice\" sanalmaydi, shuning uchun \"a piece of advice\" deyiladi."),
    ('b1', "a ___ of furniture", "piece", ["pair", "loaf", "sheet"],
     "\"Furniture\" ham sanalmaydi: a piece of furniture."),
    ('b1', "a ___ of grapes", "bunch", ["sheet", "slice", "bar"],
     "Uzum boshi — \"a bunch of grapes\" (gullar uchun ham: a bunch of "
     "flowers)."),
]


def q_measure(level, tier):
    lvl, text, correct, wrongs, why = _pick(_MEASURES, level, tier)
    return _q("O'lchov birikmalari", "Choose the correct word:  " + text,
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Rasmiy va norasmiy til
# ---------------------------------------------------------------------------

_REGISTER = [
    ('a2', "You are writing an e-mail to your school director. How do you begin?",
     "Dear Mr Karimov,", ["Hi!", "Hey there,", "What's up?"],
     "Rasmiy xatda \"Dear + familiya\" bilan boshlanadi."),
    ('a2', "You are writing to your best friend. How do you finish?",
     "See you soon!", ["Yours faithfully,", "I remain your servant,",
                       "Respectfully submitted,"],
     "Do'stga yozilgan xat norasmiy tugaydi: See you soon / Love / Bye."),
    ('b1', "Which sentence is more formal?",
     "I would like to apply for the position of teacher.",
     ["I wanna be a teacher at your school.",
      "I'm after that teacher job.", "Give me the teacher job, please."],
     "\"I would like to apply for…\" — rasmiy ariza tili; \"wanna\" — "
     "og'zaki qisqartma."),
    ('b1', "Which sentence is more formal?",
     "We regret to inform you that your application was unsuccessful.",
     ["Sorry, you didn't get it.", "Bad luck, mate.",
      "You failed, so that's that."],
     "\"We regret to inform you…\" — rasmiy xabar shakli."),
    ('b1', "You want to ask your teacher for help politely. What do you say?",
     "Could you help me with this exercise, please?",
     ["Help me with this exercise.", "You must help me now.",
      "I want you to help me."],
     "Muloyim iltimos \"Could you … , please?\" bilan tuziladi."),
    ('b1', "How do you end a formal letter that begins \"Dear Sir or Madam\"?",
     "Yours faithfully,", ["Yours sincerely,", "Lots of love,", "Cheers,"],
     "Ism noma'lum bo'lsa (\"Dear Sir or Madam\") — \"Yours faithfully\"; "
     "ism ma'lum bo'lsa — \"Yours sincerely\"."),
]


def q_register(level, tier):
    lvl, prompt, correct, wrongs, why = _pick(_REGISTER, level, tier)
    return _q("Rasmiy va norasmiy", prompt, correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Tinish belgilari va bosh harflar
# ---------------------------------------------------------------------------

_PUNCTUATION = [
    ('a1', "I live in Tashkent.",
     ["i live in Tashkent.", "I live in tashkent.", "I live in Tashkent"],
     "Gap bosh harf bilan boshlanadi, shahar nomi bosh harf bilan yoziladi, "
     "gap oxirida nuqta turadi."),
    ('a1', "Do you like English?",
     ["Do you like english?", "do you like English?", "Do you like English."],
     "So'roq gap oxirida so'roq belgisi; til nomi bosh harf bilan."),
    ('a1', "My birthday is in May.",
     ["My birthday is in may.", "my birthday is in May.",
      "My Birthday is in May."],
     "Oy nomlari bosh harf bilan; \"birthday\" — oddiy ot."),
    ('a2', "It's my sister's book.",
     ["Its my sisters book.", "It's my sisters' book.", "Its' my sister's book."],
     "\"It's\" = it is; birlik otga egalik uchun 's — sister's."),
    ('a2', "We visited London, Paris and Rome.",
     ["We visited london, paris and rome.", "We visited London Paris and Rome.",
      "We visited London, Paris and Rome"],
     "Shahar nomlari bosh harf bilan, sanashda vergul qo'yiladi."),
    ('b1', "\"Where are you going?\" she asked.",
     ["\"Where are you going\"? she asked.", "\"where are you going?\" She asked.",
      "\"Where are you going?\", she asked."],
     "So'roq belgisi qo'shtirnoq ICHIDA qoladi, keyin kichik harf bilan "
     "\"she asked\"."),
    ('b1', "Although it was raining, we went out.",
     ["Although it was raining we went out.",
      "Although, it was raining we went out.",
      "although it was raining, we went out."],
     "Ergash gap oldinda kelsa, undan keyin vergul qo'yiladi."),
]


def q_punctuation(level, tier):
    lvl, correct, wrongs, why = _pick(_PUNCTUATION, level, tier)
    return _q("Tinish belgilari", "Which sentence is written correctly?",
              correct, list(wrongs), why)


# ---------------------------------------------------------------------------
# Topic pools — which generators play in which level and round
# ---------------------------------------------------------------------------

_POOLS = {
    'a1': {
        1: [q_be, q_articles, q_plural, q_pronoun, q_vocab, q_demonstrative,
            q_odd_one_out, q_opposite,
            # yangi shakldagi savollar
            q_dialogue, q_spelling, q_nationality, q_measure, q_punctuation,
            q_mini_reading, q_sign],
        2: [q_be, q_present_simple, q_possessive_adj, q_prep_place, q_there_is,
            q_have_got, q_can, q_plural, q_vocab, q_opposite, q_articles,
            q_odd_one_out,
            q_dialogue, q_spelling, q_time_english, q_measure, q_punctuation,
            q_mini_reading, q_sign, q_confusable, q_word_order],
        3: [q_present_simple, q_prep_place, q_there_is, q_can, q_question_word,
            q_prep_time, q_quantifier, q_opposite, q_vocab, q_pronoun,
            q_articles, q_plural,
            q_dialogue, q_time_english, q_date_ordinal, q_mini_reading,
            q_sign, q_confusable, q_word_order, q_sound, q_nationality],
    },
    'a2': {
        1: [q_present_simple, q_past_simple, q_plural, q_prep_place, q_there_is,
            q_vocab, q_opposite, q_possessive_adj, q_question_word,
            q_mini_reading, q_dialogue, q_sign, q_spelling, q_measure,
            q_nationality, q_time_english, q_punctuation],
        2: [q_past_simple, q_past_spelling, q_comparative, q_quantifier,
            q_present_continuous, q_prep_time, q_question_word, q_possessive_s,
            q_vocab, q_frequency, q_present_simple,
            q_mini_reading, q_dialogue, q_sign, q_confusable, q_spelling,
            q_sound, q_synonym, q_word_order, q_translate, q_date_ordinal],
        3: [q_past_simple, q_comparative, q_future, q_present_continuous,
            q_frequency, q_possessive_s, q_present_perfect, q_modal,
            q_collocation, q_vocab, q_quantifier, q_past_spelling,
            q_mini_reading, q_dialogue, q_sign, q_confusable, q_sound,
            q_synonym, q_word_order, q_translate, q_tag, q_so_neither,
            q_idiom, q_measure],
    },
    'b1': {
        1: [q_past_simple, q_comparative, q_present_continuous, q_future,
            q_quantifier, q_collocation, q_vocab, q_question_word, q_prep_time,
            q_possessive_s,
            q_mini_reading, q_dialogue, q_sign, q_synonym, q_word_order,
            q_translate, q_measure, q_confusable],
        2: [q_present_perfect, q_conditional, q_relative, q_modal,
            q_gerund_infinitive, q_used_to, q_dependent_prep, q_collocation,
            q_vocab, q_word_formation, q_comparative,
            q_mini_reading, q_synonym, q_idiom, q_tag, q_so_neither,
            q_translate, q_confusable, q_sound, q_word_order, q_sign,
            q_register],
        3: [q_present_perfect, q_conditional, q_passive, q_reported,
            q_gerund_infinitive, q_phrasal, q_word_formation, q_dependent_prep,
            q_relative, q_modal, q_vocab, q_correct_sentence,
            q_mini_reading, q_synonym, q_idiom, q_tag, q_so_neither,
            q_register, q_translate, q_punctuation, q_sound, q_sign,
            q_spelling],
    },
}


def stage_tier(stage):
    """Championship round (1–3) for a 1-based stage number (1–15)."""
    return min(3, (stage - 1) // 5 + 1)


def _recent_topics(last_topic):
    """`last_topic` bitta mavzu nomi ham, so'nggi mavzular ro'yxati ham
    bo'lishi mumkin — eski chaqiruvlar buzilmasin."""
    if not last_topic:
        return ()
    if isinstance(last_topic, str):
        return (last_topic,)
    return tuple(last_topic)


def generate_question(level, stage, last_topic=None):
    """Generate a fresh question for this level + stage.

    `last_topic` may be a single topic or the last few of them — see
    `mathchamp.generate_question` for why remembering more than one matters.
    """
    if level not in _POOLS:
        level = 'a1'
    tier = stage_tier(stage)
    pool = _POOLS[level][tier]
    recent = _recent_topics(last_topic)
    q = None
    for _ in range(14):
        q = random.choice(pool)(level, tier)
        if q['topic'] not in recent:
            return q
    for _ in range(6):
        q = random.choice(pool)(level, tier)
        if not recent or q['topic'] != recent[-1]:
            return q
    return q
