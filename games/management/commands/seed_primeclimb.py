from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from games.models import PrimeClimbChallenge

SAMPLES = [
    {
        'title':  'Prime Numbers',
        'mode':   PrimeClimbChallenge.PRIMES,
        'target': None,
        'hint':   'Numbers divisible only by 1 and themselves',
    },
    {
        'title':  'Perfect Squares',
        'mode':   PrimeClimbChallenge.SQUARES,
        'target': None,
        'hint':   'Numbers that equal a whole number multiplied by itself',
    },
    {
        'title':  'Multiples of 7',
        'mode':   PrimeClimbChallenge.MULTIPLES,
        'target': 7,
        'hint':   'Lucky number sevens!',
    },
]


class Command(BaseCommand):
    help = 'Seed 3 sample Prime Climb Grid challenges (primes, squares, multiples of 7)'

    def handle(self, *args, **options):
        admin_user = User.objects.filter(is_superuser=True).first() or User.objects.first()
        if not admin_user:
            self.stderr.write('No users found. Create a superuser first.')
            return

        created = 0
        for s in SAMPLES:
            if PrimeClimbChallenge.objects.filter(title=s['title']).exists():
                self.stdout.write(f"  skip — already exists: {s['title']}")
                continue
            PrimeClimbChallenge.objects.create(
                title=s['title'],
                mode=s['mode'],
                target=s['target'],
                hint=s['hint'],
                created_by=admin_user,
                is_active=True,
            )
            self.stdout.write(self.style.SUCCESS(f"  created: {s['title']}"))
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Done — {created} challenge(s) created.'))
