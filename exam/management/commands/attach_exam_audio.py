"""
Attach a listening MP3 (committed in the repo) to an Exam.

The generated exam audio lives in git at exam/data/audio/ because media/
is gitignored and Railway's filesystem is wiped on redeploy. This command
copies the file into MEDIA_ROOT via the FileField and points the exam at it.

    python manage.py attach_exam_audio 101 exam/data/audio/mock1_listening.mp3

Safe to re-run (e.g. after a redeploy wiped media/): it just re-copies.
"""
import os

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from exam.models import Exam


class Command(BaseCommand):
    help = 'Attach a repo-committed listening MP3 to an Exam (by exam_number).'

    def add_arguments(self, parser):
        parser.add_argument('exam_number', type=int, help='Exam.exam_number to attach to')
        parser.add_argument('mp3_path', help='Path to the MP3 file in the repo')
        parser.add_argument('--language', default='korean',
                            help='Exam language (default: korean)')
        parser.add_argument('--force', action='store_true',
                            help='Re-copy even if the attached file already exists')

    def handle(self, **options):
        path = options['mp3_path']
        if not os.path.isfile(path):
            raise CommandError(f'File not found: {path}')
        try:
            exam = Exam.objects.get(exam_number=options['exam_number'],
                                    language=options['language'])
        except Exam.DoesNotExist:
            raise CommandError(
                f'No exam with exam_number={options["exam_number"]} '
                f'language={options["language"]} — run load_mock first.')

        if (exam.listening_audio and not options['force']
                and os.path.isfile(exam.listening_audio.path)):
            self.stdout.write(f'Audio already in place ({exam.listening_audio.name}) — skipping. '
                              f'Use --force to re-copy.')
            return

        filename = os.path.basename(path)
        with open(path, 'rb') as fh:
            exam.listening_audio.save(filename, File(fh), save=True)

        size_mb = os.path.getsize(exam.listening_audio.path) / (1024 * 1024)
        self.stdout.write(self.style.SUCCESS(
            f'Attached {exam.listening_audio.name} ({size_mb:.1f} MB) to "{exam}" (id={exam.id})'))
