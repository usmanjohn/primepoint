"""The hand-out kit — what the printed business card and flyer say.

`/kit/card/`, `/kit/card/sheet/` and `/kit/flyer/` are print-ready pages a
teacher opens, hits Ctrl+P on, and walks into an educational centre with. This
module is everything *editorial* about them: the pitch, the headlines, the
bullet lists, the three steps. The templates hold the paper, this holds the
words.

It is a plain module for the same reason `prime/books.py`, `prime/partners.py`
and `games/catalog.py` are: authored copy that changes when we decide it
changes, not data a user edits.

**Why the copy lives here as data instead of in `{% trans %}`.** Same call the
Logic Arena made: a marketing headline is *content*, not interface. These are
two finished pieces of print, one Uzbek and one English, and the Uzbek one is
not a translation of the English — it is the one that gets handed to a centre
director in Sirdaryo, so it is the one that was written first. Keeping both in
one dict means the pages can offer `?lang=en` without touching the visitor's
site language, and means neither version can silently fall back to English in
`django.po` and be printed a hundred times that way.

Everything factual in here is checked against the platform: the live counts on
the pieces come from the database at render time (`prime.views._platform_stats`),
never from a number typed into this file.
"""

# ── House identity ─────────────────────────────────────────────────────
# Same wording as prime/about.html, the certificates and the printed books.
BRAND = 'Prime Point'
MARK = 'Powerty'
SITE_HOST = 'powerty.uz'
SITE_URL = 'https://www.powerty.uz/'

# The QR files `prime/management/commands/gen_qr.py` writes. Paths under static/.
QR_SITE = 'images/qr/powerty-site.svg'
QR_TELEGRAM = 'images/qr/powerty-telegram.svg'
QR_SITE_PNG = 'images/qr/powerty-site.png'
QR_TELEGRAM_PNG = 'images/qr/powerty-telegram.png'

LANGS = ('uz', 'en')
DEFAULT_LANG = 'uz'


def pick_lang(raw):
    """`?lang=` value -> a language the kit actually has. Anything else -> Uzbek.

    Deliberately independent of the site's own EN/UZ switch: a master browsing
    the site in English still prints the Uzbek card, because the card is for an
    Uzbek centre director, not for the person at the keyboard.
    """
    return raw if raw in LANGS else DEFAULT_LANG


# ── The courses, as the card and the flyer name them ───────────────────
# `name` is the course, `line` is what it covers, `count` is filled in at
# render time from the database where it is a live number. Colours are the
# subject colours from prime/subjects.py so the printed piece and the site
# agree about what "Korean" looks like.
COURSES = [
    {'key': 'english',  'color': '#38bdf8', 'icon': 'bi-translate',
     'uz': ('Prime English', 'Ingliz tili grammatikasi — noldan ravon darajagacha'),
     'en': ('Prime English', 'English grammar from zero to fluent')},
    {'key': 'korean',   'color': '#f87171', 'icon': 'bi-flag-fill',
     'uz': ('Prime Korean', 'Koreys tili — alifbodan TOPIK darajasigacha'),
     'en': ('Prime Korean', 'Korean from the alphabet to TOPIK level')},
    {'key': 'japanese', 'color': '#fb7185', 'icon': 'bi-brilliance',
     'uz': ('Prime Japanese', 'Yapon tili — uchta yozuv, N4 darajasi'),
     'en': ('Prime Japanese', 'Japanese — three scripts, up to N4')},
    {'key': 'russian',  'color': '#a78bfa', 'icon': 'bi-globe2',
     'uz': ('Prime Russian', 'Rus tili — kelishiklar oʻzbek tiliga qiyoslab'),
     'en': ('Prime Russian', 'Russian — cases taught against Uzbek ones')},
    {'key': 'math',     'color': '#f59e0b', 'icon': 'bi-calculator-fill',
     'uz': ('Prime Math', 'Maktab matematikasi — 5-sinfdan 9-sinfgacha'),
     'en': ('Prime Math', 'School mathematics, grade 5 to grade 9')},
    {'key': 'sat',      'color': '#34d399', 'icon': 'bi-mortarboard-fill',
     'uz': ('Prime SAT Math', 'Digital SAT matematikasi — imtihon tilida'),
     'en': ('Prime SAT Math', 'Digital SAT maths, in the exam’s own language')},
]

# The exam tracks, printed as a second row — they are prep, not courses.
TRACKS = [
    {'key': 'topik', 'uz': ('TOPIK', 'Koreys tili imtihoni'),
     'en': ('TOPIK', 'Korean proficiency exam')},
    {'key': 'ielts', 'uz': ('IELTS', 'Academic moduli'),
     'en': ('IELTS', 'Academic module')},
    {'key': 'sat',   'uz': ('SAT R&W', 'Oʻqish va yozish'),
     'en': ('SAT R&W', 'Reading and Writing')},
]


# ── The copy ───────────────────────────────────────────────────────────
# One dict per language. The keys are shared, so a template never asks which
# language it is rendering — it asks for `c.headline` and gets the right one.
COPY = {
    'uz': {
        'dir_note': 'Oʻzbekcha',
        'other_lang': 'en',
        'other_lang_label': 'English',

        # — business card —
        'card_slogan': '«Kuchli fikrlar chegaralarni kengaytiradi»',
        'card_role': 'Oʻquv markazlari uchun taʼlim platformasi',
        'card_scan': 'Skanerlang',
        'card_scan_sub': 'Roʻyxatdan oʻtmasdan koʻring',
        'card_back_title': 'Darsliklaringiz tayyor.',
        'card_back_lead': 'Oltita toʻliq kurs, imtihonga tayyorgarlik, '
                          'avtomatik tekshiriladigan uy vazifasi va sinf '
                          'jurnali — bir joyda, bitta tizimda.',
        'card_bullets': [
            'Har bir dars: nazariya + 20 ta savol + oʻqish matni',
            'Uy vazifasi oʻzi tekshiriladi, natija sizga koʻrinadi',
            'Davomat, sertifikat, toʻlov — sinfxona ichida',
        ],
        'hero_kicker': 'Taʼlim platformasi',
        'card_contact_label': 'Bogʻlanish',

        # — flyer, page 1 —
        'eyebrow': 'Oʻquv markazlari uchun',
        'headline': 'Markazingizning<br>darsliklari — tayyor.',
        'lead': 'Prime Point — oʻzbek oʻquvchisi uchun yozilgan toʻliq oʻquv '
                'bazasi. Har bir dars uchta oyoqda turadi: <strong>tushuntirish</strong>, '
                '<strong>yigirmata savol</strong> va <strong>oʻqish matni</strong> — '
                'ketma-ket, birinchi darsdan oxirgisigacha. Oʻqituvchi dars '
                'tayyorlamaydi: dars allaqachon tayyor, u faqat oʻrgatadi.',
        'stats_note': 'Raqamlar platformadan — hozirgi holat',
        'stat_lessons': 'dars',
        'stat_questions': 'mashq savoli',
        'stat_readings': 'oʻqish matni',
        'stat_courses': 'toʻliq kurs',
        'stat_tracks': 'imtihon yoʻnalishi',
        'courses_title': 'Nimalar bor',
        'courses_sub': 'Har bir kurs — yuzta dars, tartib bilan, noldan.',
        'tracks_title': 'Imtihonga tayyorgarlik',
        'scan_title': 'Telefoningiz bilan skanerlang',
        'scan_sub': 'Roʻyxatdan oʻtmasdan ham butun kutubxonani koʻrasiz. '
                    'Hisob ochish — bir daqiqa.',

        # — flyer, page 2 —
        'centre_eyebrow': 'Markaz nima yutadi',
        'centre_title': 'Oʻqituvchining ish kuni qisqaradi.',
        'centre_lead': 'Prime Point shunchaki matn toʻplami emas — markazning '
                       'sinfxonasi ham shu yerda ishlaydi.',
        'centre_items': [
            ('Sinfxona', 'Guruhlar, oʻquvchilar, davomat, sertifikat va toʻlov '
                         'daftari — bitta sahifada.'),
            ('Uy vazifasi', 'Tayyor mashqlardan uy vazifasi tuzasiz, muddat '
                            'qoʻyasiz; javoblar oʻzi tekshiriladi.'),
            ('Tahlil', 'Kim qayerda qoqildi — savolma-savol, variantma-variant '
                       'koʻrinadi. Keyingi dars nimaga bagʻishlanishi oʻzi maʼlum.'),
            ('Chop etish', 'Dars + mashq + matn — A4 varaqqa yoki A5 kitob '
                           'holida. Internetsiz sinf uchun ham.'),
            ('Oʻyinlar', 'Matematika va ingliz tili chempionatlari, Mantiq '
                         'maydoni, Sayohat — bolalar oʻzi qaytadigan qism.'),
            ('Telefonda', 'Sayt telefonga ilova boʻlib oʻrnatiladi. Kompyuter '
                          'shart emas.'),
        ],
        'how_title': 'Uch qadamda boshlanadi',
        'how_steps': [
            ('Hisob oching', 'powerty.uz — oʻqituvchi sifatida roʻyxatdan '
                             'oʻtasiz. Bir daqiqa, boshqa hech narsa kerak emas.'),
            ('Sinfxona tuzing', 'Guruhingizni kiritasiz, fanni tanlaysiz — '
                                'mashqlar roʻyxati oʻsha fanga qisqaradi.'),
            ('Dars bering', 'Tayyor darsni ochasiz, uy vazifasini tayinlaysiz, '
                            'natijani koʻrasiz. Tayyorgarlik vaqti — nol.'),
        ],
        'why_title': 'Nega buni qurdik?',
        'why_text': 'Biz ham shu yerda dars beramiz. Platformani viloyatdagi '
                    'oʻquvchi uchun qurdik: darslar ketma-ket, mashqlar har bir '
                    'darsning oʻziga, matnlar esa oʻrganilgan qoidani ishlab '
                    'turgan holda koʻrsatadi. Markazingiz uchun ham shu ish '
                    'qilingan — materiallaringiz koʻpaygani va oʻquvchilaringiz '
                    'oʻsganini koʻrmoqchimiz.',
        'partners_title': 'Biz yolgʻiz emasmiz',
        'partners_sub': 'Prime Point davlat idoralari va yoshlar dasturlari '
                        'bilan birga ishlaydi.',
        'contact_title': 'Bogʻlaning',
        'contact_sub': 'Markazingizga Prime Pointni olib kirmoqchimisiz? '
                       'Yozing — oʻqituvchilaringizga boshidan oxirigacha '
                       'koʻrsatib beramiz.',
        'tg_channel': 'Kunlik savol va haftalik jumboq',
        'foot': 'Prime Point · powerty.uz · Sohil shahri, Sirdaryo',

        # — the on-screen toolbar (not printed) —
        'bar_print': 'Chop etish / PDF saqlash',
        'bar_hint': 'Chop etish oynasida: A4, «Fon rasmlari» yoqilgan boʻlsin.',
        'bar_hint_card': 'Chop etish oynasida: A4, hoshiya «Yoʻq», '
                         '«Fon rasmlari» yoqilgan boʻlsin.',
        'bar_back': 'Orqaga',
        'bar_lang': 'English',
        'bar_flyer': 'Flayer',
        'bar_card': 'Vizitka',
        'bar_sheet': 'A4 varaq (10 ta vizitka)',
        'bar_single': 'Bitta vizitka',
        'bar_side_front': 'Old tomoni',
        'bar_side_back': 'Orqa tomoni',
        'sheet_note_front': 'Bu varaq — vizitkalarning OLD tomoni. Chop etib, '
                            'qogʻozni uzun chetidan agʻdaring va orqa tomonini '
                            'chop eting.',
        'sheet_note_back': 'Bu varaq — ORQA tomoni. Oʻntasi bir xil boʻlgani '
                           'uchun qogʻozni qaysi tomonga agʻdarsangiz ham har '
                           'bir orqa oʻz oldining orqasiga tushadi.',
        'sheet_cut': 'Chiziq boʻylab kesing · 90 × 50 mm',
    },

    'en': {
        'dir_note': 'English',
        'other_lang': 'uz',
        'other_lang_label': 'Oʻzbekcha',

        'card_slogan': '“Strong mind bends the line”',
        'card_role': 'A learning platform for educational centres',
        'card_scan': 'Scan me',
        'card_scan_sub': 'No account needed to look around',
        'card_back_title': 'Your lessons are already written.',
        'card_back_lead': 'Six full courses, exam preparation, self-marking '
                          'homework and a classroom register — in one place, '
                          'in one system.',
        'card_bullets': [
            'Every lesson: the teaching + 20 questions + a reading',
            'Homework marks itself; you see who struggled and where',
            'Attendance, certificates and payments inside the classroom',
        ],
        'hero_kicker': 'Learning platform',
        'card_contact_label': 'Get in touch',

        'eyebrow': 'For educational centres',
        'headline': 'Your centre’s syllabus,<br>already written.',
        'lead': 'Prime Point is a complete teaching library built for the Uzbek '
                'learner. Every lesson stands on three legs — <strong>the '
                'teaching</strong>, <strong>twenty questions</strong> and '
                '<strong>a reading</strong> — in order, from the first lesson to '
                'the hundredth. Your teachers stop preparing material and go '
                'back to teaching.',
        'stats_note': 'Live counts from the platform',
        'stat_lessons': 'lessons',
        'stat_questions': 'practice questions',
        'stat_readings': 'readings',
        'stat_courses': 'full courses',
        'stat_tracks': 'exam tracks',
        'courses_title': 'What is inside',
        'courses_sub': 'Each course is a hundred lessons, in order, from zero.',
        'tracks_title': 'Exam preparation',
        'scan_title': 'Scan with your phone',
        'scan_sub': 'The whole library opens without an account. Signing up '
                    'takes a minute.',

        'centre_eyebrow': 'What the centre gets',
        'centre_title': 'A shorter working day for every teacher.',
        'centre_lead': 'Prime Point is not only material — your classroom runs '
                       'here too.',
        'centre_items': [
            ('Classroom', 'Groups, students, attendance, certificates and the '
                          'payment book — on one page.'),
            ('Homework', 'Build homework from ready practices, set a deadline, '
                         'and let the answers mark themselves.'),
            ('Analytics', 'Who slipped and where — question by question, choice '
                          'by choice. The next lesson plans itself.'),
            ('Print', 'Lesson + practice + reading as an A4 handout or an A5 '
                      'bound book, for classrooms with no internet.'),
            ('Games', 'Maths and English championships, the Logic Arena, the '
                      'Journey — the part pupils come back to on their own.'),
            ('On a phone', 'The site installs as an app. No computer needed.'),
        ],
        'how_title': 'Three steps to start',
        'how_steps': [
            ('Open an account', 'Sign up at powerty.uz as a teacher. One '
                                'minute, and nothing else to arrange.'),
            ('Create a classroom', 'Add your group and pick the subject — every '
                                   'picker narrows to that subject.'),
            ('Teach', 'Open a ready lesson, assign the homework, read the '
                      'results. Preparation time: none.'),
        ],
        'why_title': 'Why we built it',
        'why_text': 'Because we teach here too. It was built for the pupil in '
                    'the regions: the lessons in order, a practice belonging to '
                    'each one, and a reading that shows the rule at work. The '
                    'same work is done for your centre — we would rather see '
                    'your shelves full and your pupils moving.',
        'partners_title': 'We do not do this alone',
        'partners_sub': 'Prime Point works alongside state institutions and '
                        'youth programmes.',
        'contact_title': 'Talk to us',
        'contact_sub': 'Want Prime Point in your centre? Write to us and we '
                       'will walk your teachers through it, start to finish.',
        'tg_channel': 'A question a day, and the weekly puzzle',
        'foot': 'Prime Point · powerty.uz · Sohil city, Sirdaryo',

        'bar_print': 'Print / Save as PDF',
        'bar_hint': 'In the print dialog: A4, with “Background graphics” on.',
        'bar_hint_card': 'In the print dialog: A4, margins “None”, '
                         '“Background graphics” on.',
        'bar_back': 'Back',
        'bar_lang': 'Oʻzbekcha',
        'bar_flyer': 'Flyer',
        'bar_card': 'Business card',
        'bar_sheet': 'A4 sheet (10 cards)',
        'bar_single': 'Single card',
        'bar_side_front': 'Front',
        'bar_side_back': 'Back',
        'sheet_note_front': 'This sheet is the card FRONTS. Print it, flip the '
                            'paper on its long edge, and print the backs.',
        'sheet_note_back': 'This sheet is the card BACKS. All ten are the same '
                           'card, so whichever way you flip the paper, every '
                           'back lands behind a front.',
        'sheet_cut': 'Cut along the lines · 90 × 50 mm',
    },
}


def copy_for(lang):
    """The copy dict for a language, with the courses/tracks already resolved.

    Templates get flat, already-chosen strings: no `{{ course.uz.0 }}` in the
    markup, and no way for a template to render the Uzbek name under the
    English line.
    """
    lang = pick_lang(lang)
    c = dict(COPY[lang])
    c['lang'] = lang
    c['courses'] = [
        {'key': x['key'], 'color': x['color'], 'icon': x['icon'],
         'name': x[lang][0], 'line': x[lang][1]}
        for x in COURSES
    ]
    c['tracks'] = [
        {'key': x['key'], 'name': x[lang][0], 'line': x[lang][1]}
        for x in TRACKS
    ]
    return c
