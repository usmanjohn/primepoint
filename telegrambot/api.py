"""A very small Telegram Bot API client — stdlib only, no new dependency.

The bot is outbound-only: it never receives updates, so there is no webhook,
no public endpoint and nothing about the people reading the channel is stored.
Every call is one HTTPS POST to api.telegram.org.

Credentials come from the environment (see point/settings.py):
    TELEGRAM_BOT_TOKEN   from @BotFather
    TELEGRAM_CHANNEL     e.g. '@powertyuz'
"""
import json
import logging
import urllib.error
import urllib.parse
import urllib.request

from django.conf import settings
from django.db import connection

logger = logging.getLogger(__name__)

API_ROOT = 'https://api.telegram.org/bot{token}/{method}'
TIMEOUT = 20

# Telegram's own limits — a post that breaks one of these is rejected whole,
# so the builders in content.py trim against these numbers rather than guessing.
POLL_QUESTION_MAX = 300
POLL_OPTION_MAX = 100
POLL_EXPLANATION_MAX = 200
POLL_OPTIONS_MAX = 10
MESSAGE_MAX = 4096


class TelegramError(RuntimeError):
    """Telegram answered, and said no."""


class LocalDatabaseRefused(RuntimeError):
    """Refusing to post live from a development database."""


def refuse_local_database():
    """The channel is public; a dev database must never feed it.

    `DATABASES` falls back to local sqlite whenever DATABASE_URL is unset
    (point/settings.py), so a mistyped --service or a plain `manage.py` run
    would happily send real posts built from dev rows — with dev ids in every
    link, pointing at whatever happens to hold that id in production.
    This has happened once; it does not get to happen twice.
    """
    engine = connection.settings_dict.get('ENGINE', '')
    if 'sqlite' in engine:
        raise LocalDatabaseRefused(
            'Refusing to post: this process is on the local sqlite database '
            f'({connection.settings_dict.get("NAME")}), not production. '
            'The post would carry dev ids in its links. '
            'Run it on Railway, or with DATABASE_URL set to the production '
            'database. Use --dry-run to preview locally.')


def is_configured():
    return bool(getattr(settings, 'TELEGRAM_BOT_TOKEN', '') and
                getattr(settings, 'TELEGRAM_CHANNEL', ''))


def call(method, **params):
    """POST one API method and return its `result`. Raises TelegramError on refusal."""
    token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
    if not token:
        raise TelegramError('TELEGRAM_BOT_TOKEN is not set')

    payload = {k: v for k, v in params.items() if v is not None}
    # Telegram wants nested structures (keyboards, option lists) as JSON strings.
    for key, value in list(payload.items()):
        if isinstance(value, (dict, list)):
            payload[key] = json.dumps(value, ensure_ascii=False)

    data = urllib.parse.urlencode(payload).encode('utf-8')
    request = urllib.request.Request(
        API_ROOT.format(token=token, method=method),
        data=data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            body = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as exc:
        # Telegram explains the refusal in the body — that message is the useful part.
        try:
            body = json.loads(exc.read().decode('utf-8'))
            raise TelegramError(f"{method}: {body.get('description', exc.reason)}") from exc
        except (ValueError, AttributeError):
            raise TelegramError(f'{method}: HTTP {exc.code} {exc.reason}') from exc
    except urllib.error.URLError as exc:
        raise TelegramError(f'{method}: could not reach Telegram ({exc.reason})') from exc

    if not body.get('ok'):
        raise TelegramError(f"{method}: {body.get('description', 'unknown error')}")
    return body['result']


def get_me():
    return call('getMe')


def send_message(text, chat_id=None, buttons=None, disable_preview=True):
    """Send an HTML-formatted message. `buttons` is a list of (label, url) pairs."""
    return call(
        'sendMessage',
        chat_id=chat_id or settings.TELEGRAM_CHANNEL,
        text=text[:MESSAGE_MAX],
        parse_mode='HTML',
        link_preview_options={'is_disabled': True} if disable_preview else None,
        reply_markup=_keyboard(buttons),
    )


def send_quiz(question, options, correct_index, explanation='', chat_id=None, buttons=None):
    """Send a native quiz poll — one tap, instantly marked, explanation on reveal."""
    return call(
        'sendPoll',
        chat_id=chat_id or settings.TELEGRAM_CHANNEL,
        question=question[:POLL_QUESTION_MAX],
        options=[o[:POLL_OPTION_MAX] for o in options[:POLL_OPTIONS_MAX]],
        type='quiz',
        correct_option_id=correct_index,
        explanation=(explanation or '')[:POLL_EXPLANATION_MAX] or None,
        explanation_parse_mode='HTML' if explanation else None,
        is_anonymous=True,
        reply_markup=_keyboard(buttons),
    )


def edit_message(message_id, text, chat_id=None, buttons=None):
    return call(
        'editMessageText',
        chat_id=chat_id or settings.TELEGRAM_CHANNEL,
        message_id=message_id,
        text=text[:MESSAGE_MAX],
        parse_mode='HTML',
        link_preview_options={'is_disabled': True},
        reply_markup=_keyboard(buttons),
    )


def _keyboard(buttons):
    if not buttons:
        return None
    return {'inline_keyboard': [[{'text': label, 'url': url}] for label, url in buttons]}
