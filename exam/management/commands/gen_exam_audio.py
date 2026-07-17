"""
Build the single full-length listening MP3 for a mock exam (local authoring tool).

Reads AUDIO_INTRO + AUDIO_PLAN from a mock exam data file (see
exam/data/mock1_listening.py) and synthesizes every line with edge-tts
(남자/해설 -> ko-KR-InJoonNeural, 여자 -> ko-KR-SunHiNeural), then joins
everything with ffmpeg: 0.8 s between dialogue lines, a per-item answer
pause after each question ('gap'), and scripts marked repeat=2 played twice.

The finished MP3 is attached to the Exam identified by EXAM_META
(exam.listening_audio), so nothing else is needed after this command.

Requires (dev machine only): pip install edge-tts, and ffmpeg on PATH.

    python manage.py gen_exam_audio exam/data/mock1_listening.py
    python manage.py gen_exam_audio exam/data/mock1_listening.py --rate=-10%
"""
import asyncio
import importlib.util
import os
import shutil
import subprocess
import tempfile

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

VOICES = {
    '남자': 'ko-KR-InJoonNeural',
    '여자': 'ko-KR-SunHiNeural',
    '해설': 'ko-KR-InJoonNeural',
}
DEFAULT_VOICE = 'ko-KR-InJoonNeural'
LINE_GAP = 0.8      # silence between dialogue lines (seconds)
REPEAT_GAP = 2.0    # silence between first and second playback of a script


class Command(BaseCommand):
    help = 'Synthesize the full listening MP3 for a mock exam and attach it to the Exam.'

    def add_arguments(self, parser):
        parser.add_argument('datafile', help='Path to a mock exam data file with AUDIO_PLAN.')
        parser.add_argument('--rate', default='-5%',
                            help='Speaking rate for edge-tts, e.g. "-10%%" (default "-5%%").')
        parser.add_argument('--out', default=None,
                            help='Also copy the finished MP3 to this path (optional).')

    def _load_module(self, path):
        if not os.path.isfile(path):
            raise CommandError(f'Data file not found: {path}')
        spec = importlib.util.spec_from_file_location('_mock_audio_data', path)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001
            raise CommandError(f'Failed to import {path}: {exc}')
        for attr in ('EXAM_META', 'AUDIO_PLAN'):
            if not hasattr(module, attr):
                raise CommandError(f'{path} must define {attr}')
        return module

    def _tts(self, text, voice, rate, path):
        import edge_tts
        asyncio.run(edge_tts.Communicate(text, voice, rate=rate).save(path))

    def _silence(self, seconds, path):
        subprocess.run(
            ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi',
             '-i', 'anullsrc=r=24000:cl=mono', '-t', str(seconds),
             '-acodec', 'libmp3lame', '-b:a', '48k', path],
            check=True)

    def handle(self, *args, **options):
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            raise CommandError('edge-tts is not installed. Run: pip install edge-tts')
        if not shutil.which('ffmpeg'):
            raise CommandError('ffmpeg not found on PATH.')

        module = self._load_module(options['datafile'])
        intro = getattr(module, 'AUDIO_INTRO', [])
        plan = module.AUDIO_PLAN
        rate = options['rate']

        with tempfile.TemporaryDirectory() as workdir:
            line_gap = os.path.join(workdir, 'gap_line.mp3')
            repeat_gap = os.path.join(workdir, 'gap_repeat.mp3')
            self._silence(LINE_GAP, line_gap)
            self._silence(REPEAT_GAP, repeat_gap)
            answer_gaps = {}   # seconds -> path

            def gap_file(seconds):
                if seconds not in answer_gaps:
                    p = os.path.join(workdir, f'gap_{seconds}.mp3')
                    self._silence(seconds, p)
                    answer_gaps[seconds] = p
                return answer_gaps[seconds]

            parts = []          # ordered mp3 paths for the final concat
            tts_count = 0

            def synth(speaker, text):
                nonlocal tts_count
                tts_count += 1
                p = os.path.join(workdir, f'tts_{tts_count}.mp3')
                self._tts(text, VOICES.get(speaker, DEFAULT_VOICE), rate, p)
                return p

            def add_script(script):
                script_parts = []
                for i, (speaker, text) in enumerate(script):
                    if i:
                        script_parts.append(line_gap)
                    script_parts.append(synth(speaker, text))
                return script_parts

            total = len(plan)
            for i, (speaker, text) in enumerate(intro):
                parts.append(synth(speaker, text))
                parts.append(line_gap)

            for idx, seg in enumerate(plan, start=1):
                if 'announce' in seg:
                    self.stdout.write(f'[{idx}/{total}] announce: {seg["announce"][:40]}…')
                    parts.append(synth('해설', seg['announce']))
                    parts.append(gap_file(2))
                    continue

                self.stdout.write(f'[{idx}/{total}] {seg["number"]}')
                parts.append(synth('해설', seg['number']))
                parts.append(line_gap)
                script_parts = add_script(seg['script'])
                parts.extend(script_parts)
                if seg.get('repeat', 1) >= 2:
                    parts.append(repeat_gap)
                    parts.extend(script_parts)
                parts.append(gap_file(seg.get('gap', 12)))

            list_path = os.path.join(workdir, 'list.txt')
            with open(list_path, 'w') as fh:
                for p in parts:
                    fh.write(f"file '{p}'\n")

            out_path = os.path.join(workdir, 'listening_full.mp3')
            self.stdout.write('Concatenating with ffmpeg…')
            subprocess.run(
                ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0',
                 '-i', list_path, '-acodec', 'libmp3lame', '-b:a', '48k', '-ac', '1', out_path],
                check=True)

            size_mb = os.path.getsize(out_path) / (1024 * 1024)
            duration = 0.0
            if shutil.which('ffprobe'):
                probe = subprocess.run(
                    ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                     '-of', 'default=noprint_wrappers=1:nokey=1', out_path],
                    capture_output=True, text=True)
                duration = float(probe.stdout.strip() or 0)

            if options['out']:
                os.makedirs(os.path.dirname(options['out']) or '.', exist_ok=True)
                shutil.copy(out_path, options['out'])
                self.stdout.write(f'Copied to {options["out"]}')

            from exam.models import Exam
            meta = module.EXAM_META
            exam = Exam.objects.get(exam_number=meta['exam_number'],
                                    language=meta.get('language', 'korean'))
            filename = f'mock{meta["exam_number"]}_listening.mp3'
            with open(out_path, 'rb') as fh:
                exam.listening_audio.save(filename, File(fh), save=True)

            self.stdout.write(self.style.SUCCESS(
                f'Done. {size_mb:.1f} MB, {duration/60:.1f} min, {tts_count} TTS lines '
                f'→ attached to "{exam}" (id={exam.id})'))
