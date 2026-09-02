"""The project's official social accounts — one source of truth.

Everything that shows a Telegram/Instagram/YouTube/e-mail link (the sidebar,
About, Help, the footer strip, and later the Telegram bot's own messages)
reads this list, so a changed handle is a one-line edit here.

`SOCIAL_LINKS` is exposed to every template as `social_links` by
`prime.context_processors.social`; render it with
`{% include "includes/social_links.html" %}`.
"""
from django.utils.translation import gettext_lazy as _

CONTACT_EMAIL = 'powertyuz@gmail.com'

SOCIAL_LINKS = [
    {
        'key': 'telegram',
        'name': 'Telegram',
        'handle': '@Albetta',
        'url': 'https://t.me/Albetta',
        'icon': 'bi-telegram',
        'color': '#2aabee',
        'blurb': _('Write to us directly'),
    },
    {
        'key': 'telegram_channel',
        'name': _('Telegram channel'),
        'handle': '@powertyuz',
        'url': 'https://t.me/powertyuz',
        'icon': 'bi-send-fill',
        'color': '#229ed9',
        'blurb': _('A question a day, and the weekly puzzle'),
    },
    {
        'key': 'instagram',
        'name': 'Instagram',
        'handle': '@powerty.uz',
        'url': 'https://www.instagram.com/powerty.uz/',
        'icon': 'bi-instagram',
        'color': '#e1306c',
        'blurb': _('Short videos, tips and news'),
    },
    {
        'key': 'youtube',
        'name': 'YouTube',
        'handle': '@powertyuz',
        'url': 'https://www.youtube.com/@powertyuz',
        'icon': 'bi-youtube',
        'color': '#ff0033',
        'blurb': _('Full lessons and story videos'),
    },
    {
        'key': 'email',
        'name': _('Email'),
        'handle': CONTACT_EMAIL,
        'url': 'mailto:' + CONTACT_EMAIL,
        'icon': 'bi-envelope-fill',
        'color': '#38bdf8',
        'blurb': _('Partnerships, questions, feedback'),
    },
]

SOCIAL_MAP = {s['key']: s for s in SOCIAL_LINKS}

# The non-email profiles, in order — used for schema.org `sameAs` and by the bot.
SOCIAL_PROFILE_URLS = [s['url'] for s in SOCIAL_LINKS if s['key'] != 'email']
