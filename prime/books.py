"""The book series registry — what a printed Powerty volume says about itself.

`/tutorials/playlists/<pk>/book/?vol=2` turns a stretch of a course playlist into
a bound A5 book: cover, front matter, lessons, answer key, glossary, back cover.
Everything that is *editorial* rather than structural lives here — the series
subtitle, the accent colour, where one volume ends and the next begins, the
back-cover blurb, the "how to use this book" text.

It is a plain module, not a model, for the same reason `games/catalog.py`,
`prime/subjects.py` and `prime/progress.py` are: this is authored copy that
changes when we decide it changes, not data a user edits. Adding a course to the
printable set means adding a key here — no migration, no admin step.

The lesson content itself comes from the playlist; see `prime/printing.py`.
"""

# ── House identity, printed on every volume ────────────────────────────
BRAND   = 'Powerty'
SITE    = 'powerty.uz'
SLOGAN  = 'Strong mind bends the line'   # same wording as prime/about.html
                                         # and the masters certificates
RIGHTS  = 'Redistribution without permission is prohibited.'

# ── The series ─────────────────────────────────────────────────────────
# Keyed by TutorialPlaylist.title. Each volume is (name, first lesson, last
# lesson) — 1-based positions in the playlist, inclusive, matching the
# ?from=/?to= of the older print sheets.
#
# Language follows the course's own policy: Prime English is written for a
# pupil reading English, Prime Korean and Prime Russian teach in Uzbek, so
# their covers and front matter are Uzbek.
BOOKS = {
    'Prime English': {
        'series':   'Prime English',
        'subtitle': 'English Grammar from Zero to Fluent',
        'tagline':  'Ingliz tili grammatikasi — noldan boshlab',
        'lang':     'en',
        'accent':   '#2563eb',
        'accent2':  '#1e3a8a',
        'volumes': [
            ('Foundations',          1,  25),
            ('Tenses and Modals',   26,  50),
            ('Bigger Sentences',    51,  75),
            ('Precision and Style',  76, 100),
        ],
        'blurb': (
            'Prime English teaches the whole English grammar system in one hundred '
            'lessons, in order, from the shape of a sentence to the sentence that '
            'sounds like a native wrote it. Nothing is assumed. Every lesson gives '
            'you the pattern, then the practice, then a reading where the pattern '
            'is alive in a real text.'
        ),
        'howto': [
            ('The lesson',   'Read it once for the idea, once for the pattern strips. '
                             'The colour-coded examples show the pattern working; the '
                             'boxed notes warn you where Uzbek speakers usually slip.'),
            ('The practice', 'Twenty questions on that lesson alone. Do them on paper '
                             'with the book closed. The answer key is at the back.'),
            ('The reading',  'A short text built out of the pattern you have just '
                             'learnt, with the new words glossed. Read it aloud. If you '
                             'can retell it in one sentence, the lesson has landed.'),
        ],
    },

    'Prime Korean': {
        'series':   'Prime Korean',
        'subtitle': 'Koreys tili grammatikasi — noldan',
        'tagline':  '한국어 문법 · 100 dars',
        'lang':     'ko',
        'accent':   '#dc2626',
        'accent2':  '#7f1d1d',
        'volumes': [
            ('Hangul va ilk qadamlar',  1,  25),
            ('Kundalik nutq',          26,  50),
            ('Bog‘lovchi shakllar', 51, 75),
            ('Yozma va rasmiy til',     76, 100),
        ],
        'blurb': (
            'Prime Korean koreys tilini noldan o‘rgatadi: Hangul harflaridan '
            'boshlab, yuz dars ichida butun grammatika tizimigacha. Har bir darsda '
            'uchta qism bor — qoida, mashq va matn. Hammasi o‘zbek tilida '
            'tushuntiriladi, koreyscha esa material bo‘lib xizmat qiladi.'
        ),
        'howto': [
            ('Dars',   'Avval g‘oyani, keyin naqsh chizmalarini o‘qing. Rangli '
                       'misollar qoidaning ishlashini ko‘rsatadi.'),
            ('Mashq',  'Shu darsning o‘ziga tegishli 20 ta savol. Kitobni yopib, '
                       'daftarda ishlang. Javoblar kitob oxirida.'),
            ('Matn',   'O‘sha qoida yashab turgan qisqa hikoya, yangi so‘zlar '
                       'izohi bilan. Ovoz chiqarib o‘qing.'),
        ],
    },

    'Prime Russian': {
        'series':   'Prime Russian',
        'subtitle': 'Rus tili grammatikasi — noldan',
        'tagline':  'Русский язык · 100 dars',
        'lang':     'ru',
        'accent':   '#0f766e',
        'accent2':  '#134e4a',
        'volumes': [
            ('Alifbo va ot',            1,  25),
            ('Kelishiklar',            26,  50),
            ('Fe’l va vid',        51,  75),
            ('Murakkab gaplar',         76, 100),
        ],
        'blurb': (
            'Prime Russian rus tilini noldan o‘rgatadi. Kirill alifbosi bir necha '
            'darsda tartibga solinadi, keyin esa asosiy ish boshlanadi: har bir '
            'падеж o‘zbek kelishigi bilan yonma-yon o‘rgatiladi, chunki '
            'o‘zbek tilida ham kelishik bor — bu eng kuchli tayanch nuqtamiz.'
        ),
        'howto': [
            ('Dars',   'Qoidani va uning o‘zbekcha muqobilini birga o‘qing.'),
            ('Mashq',  '20 ta savol. Javoblar kitob oxirida.'),
            ('Matn',   'Qoida yashab turgan qisqa matn, yangi so‘zlar izohi bilan.'),
        ],
    },

    # The first non-language volume. Its "Matn" leg is not a reading in a
    # foreign language but a text in Uzbek that the maths lives inside — which
    # is the whole point of the course: a pupil who can compute but cannot read
    # a problem fails every exam that matters.
    'Prime Math': {
        'series':   'Prime Math',
        'subtitle': 'Maktab matematikasi — noldan',
        'tagline':  'Matematika · 100 dars',
        'lang':     'uz',
        'accent':   '#b45309',
        'accent2':  '#78350f',
        'volumes': [
            ('Sonlar va kasrlar',        1,  28),
            ('Algebra tili',            29,  56),
            ('Geometriya va ma’lumot',  57,  84),
            ('Masala yechish',          85, 100),
        ],
        'blurb': (
            'Prime Math maktab matematikasini boshidan boshlab, tartib bilan '
            'o‘rgatadi: sonlardan tortib tenglama, grafik, geometriya va '
            'ehtimollikkacha. Har bir qoida nega ishlashi tushuntiriladi, har bir '
            'yechim esa qadamma-qadam, har qadamning sababi bilan yoziladi. Har '
            'darsda kamida bitta matnli masala bor — chunki hisoblashni bilib, '
            'masalani o‘qiy olmaslik eng ko‘p uchraydigan muammo.'
        ),
        'howto': [
            ('Dars',   'Avval g‘oyani, keyin yechim zinapoyasini o‘qing: chap '
                       'ustunda amal, o‘ng ustunda nega shunday qilingani.'),
            ('Mashq',  'Shu darsning o‘ziga tegishli 20 ta savol, oxirgi ikkitasi '
                       'har doim matnli masala. Daftarda ishlang; javoblar kitob '
                       'oxirida.'),
            ('Matn',   'Shu darsning matematikasi yashab turgan qisqa matn, '
                       'atamalar izohi bilan. Oxiridagi savolga hisoblab javob '
                       'bering.'),
        ],
    },
}

# Roman numerals for the volume number on the cover. Four volumes per course
# today; the fallback keeps a fifth from printing blank.
ROMAN = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']


def book_for(playlist):
    """The registry entry for a playlist, or None if it is not a printable series."""
    return BOOKS.get(playlist.title)


def volumes(book, total):
    """The book's volumes, clamped to the lessons that actually exist.

    A course still being written (Prime Russian sits at 20 lessons) must not
    offer three empty volumes, so a volume whose start is past `total` is
    dropped and the last one is trimmed to `total`.
    """
    out = []
    for index, (name, start, end) in enumerate(book['volumes'], start=1):
        if total and start > total:
            break
        out.append({
            'n':      index,
            'roman':  ROMAN[index] if index < len(ROMAN) else str(index),
            'name':   name,
            'start':  start,
            'end':    min(end, total) if total else end,
        })
    return out


def volume(book, total, n):
    """One volume by its 1-based number; falls back to the first."""
    found = volumes(book, total)
    for vol in found:
        if vol['n'] == n:
            return vol
    return found[0] if found else None
