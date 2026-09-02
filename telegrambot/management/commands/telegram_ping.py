"""Check the wiring before trusting the cron: token, channel, admin rights.

    python manage.py telegram_ping           # identify the bot only
    python manage.py telegram_ping --post    # also send a test message to the channel
"""
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from telegrambot import api, pick


class Command(BaseCommand):
    help = 'Verify the bot token and that the bot can post to the channel.'

    def add_arguments(self, parser):
        parser.add_argument('--post', action='store_true',
                            help='Send a real test message to the channel.')

    def handle(self, *args, **options):
        if not settings.TELEGRAM_BOT_TOKEN:
            raise CommandError('TELEGRAM_BOT_TOKEN is not set.')
        if not settings.TELEGRAM_CHANNEL:
            raise CommandError('TELEGRAM_CHANNEL is not set.')

        me = api.get_me()
        self.stdout.write(self.style.SUCCESS(
            f'Bot OK: @{me.get("username")} ({me.get("first_name")})'))
        self.stdout.write(f'Channel: {settings.TELEGRAM_CHANNEL}')
        self.stdout.write(f'Site URL in links: {settings.SITE_URL}')

        remaining = pick.remaining_by_subject()
        self.stdout.write('Unposted questions: ' +
                          ', '.join(f'{k} {v}' for k, v in remaining.items()))

        if options['post']:
            result = api.send_message(
                '🐼 <b>Powerty</b> — bot ulandi.\n'
                'Har kuni soat 19:00 da kun savoli shu yerda chiqadi.')
            self.stdout.write(self.style.SUCCESS(
                f'Test message sent → id {result.get("message_id")}. '
                'Delete it in Telegram once you have seen it.'))
        else:
            self.stdout.write('Add --post to send a real test message to the channel.')
