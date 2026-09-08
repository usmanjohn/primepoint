"""The organisations that stand behind Prime Point — one source of truth.

The About page renders this list; anything else that ever needs to show the
partner wall (a printed one-pager, a press page) reads the same list, so a new
logo or a changed link is a one-line edit here and never a template hunt.

Order is deliberate: national agency → its youth-fund project → region →
district. That is how the partnership actually reaches a pupil in Sohil.

Names stay in Uzbek in both languages — they are the organisations' own names,
not labels; what gets translated is the `kind` under the name and the one-line
`blurb`. `logo` is a path under `static/`. The logos are full-bleed artwork
with their own backgrounds (not transparent marks), so the About page shows
each one as the whole top of its card (`object-fit: cover`) instead of
shrinking it into a grey square.
"""
from django.utils.translation import gettext_lazy as _

PARTNERS = [
    {
        'key': 'yoshlar_agentligi',
        'name': "Yoshlar ishlari agentligi",
        'kind': _('State agency'),
        'blurb': _('The national body for youth policy and youth programmes.'),
        'logo': 'images/partners/yoshlarishlariagentligi.png',
        'url': 'https://gov.uz/oz/yoshlar',
        'site': 'gov.uz/yoshlar',
    },
    {
        'key': 'komak',
        'name': "Ko‘mak loyihasi",
        'kind': _('Youth Foundation project'),
        'blurb': _('A support programme of the Youth Foundation of Uzbekistan.'),
        'logo': 'images/partners/komakloyihasi.png',
        'url': 'https://yoshlarfondi.uz/#/home',
        'site': 'yoshlarfondi.uz',
    },
    {
        'key': 'sirdaryo_viloyat',
        'name': "Sirdaryo viloyati hokimligi",
        'kind': _('Regional government'),
        'blurb': _('The regional administration of Sirdaryo.'),
        'logo': 'images/partners/sirdaryoviloyatihokimligi.jpeg',
        'url': 'https://gov.uz/uz/sirdaryo',
        'site': 'gov.uz/sirdaryo',
    },
    {
        'key': 'sirdaryo_tuman',
        'name': "Sirdaryo tumani hokimligi",
        'kind': _('District government'),
        'blurb': _('The district administration our classrooms sit in.'),
        'logo': 'images/partners/Sirdaryotumanhokimligi.jpeg',
        'url': 'https://gov.uz/uz/sirdarya',
        'site': 'gov.uz/sirdarya',
    },
]
