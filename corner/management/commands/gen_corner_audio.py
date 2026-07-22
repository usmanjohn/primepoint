"""
Generate narration audio for Corner stories (local authoring tool).

Reads the published stories of one Collection straight from the DB, turns each
story's body into clean narration text (title first, then one chunk per
paragraph/heading), synthesizes it with edge-tts (Microsoft neural voices) and
joins the chunks with a short silence gap via ffmpeg — the same technique the
examprep listening clips use.

Voice is picked from the collection's subject (Korean -> ko-KR, English ->
en-US) unless overridden with --voice. For Korean collections, paragraphs
without any Hangul (e.g. the Uzbek «Oʻzbekchada: ...» note at the end of the
proverb stories) are skipped so the narrator never reads Uzbek text aloud.
Emoji and cn-word markup are stripped before synthesis.

Output files are named ``<order>.mp3`` — exactly the naming that
``import_corner_audio`` expects, so the full workflow is::

    pip install edge-tts   # dev machine only; ffmpeg must be on PATH
    python manage.py gen_corner_audio --collection="Keimyung Short Readings"
    python manage.py import_corner_audio corner/management/commands/audio/keimyung-short-readings \
        --collection="Keimyung Short Readings"

Options: ``--only <order>`` regenerates a single story; ``--overwrite``
regenerates files that already exist in the output folder; ``--gap`` changes
the pause between paragraphs (seconds); ``--rate`` adjusts speaking speed
(e.g. "-10%"); ``--voices "en-US-JennyNeural,en-US-GuyNeural"`` cycles through
several narrator voices across the collection's stories (e.g. alternating
female/male), overriding the single ``--voice``/subject default.

For DIALOGUE stories (each ``<p>`` is one speaker's turn, strictly
alternating), use ``--speaker-voices "voiceA,voiceB"`` instead: it assigns a
distinct voice to each paragraph in turn (title + odd paragraphs -> voiceA,
even paragraphs -> voiceB), so the two characters are read in two different
voices in one clip. Since each dialogue story usually has its own two named
characters, run it once per story with ``--only``, e.g.::

    python manage.py gen_corner_audio --collection="Everyday Conversations" \
        --only 1 --speaker-voices "en-US-JennyNeural,en-US-GuyNeural"
"""

import asyncio
import html
import os
import re
import shutil
import subprocess
import tempfile
import time

from django.core.management.base import BaseCommand, CommandError

from corner.models import Collection

# Narrator per subject shelf. Female neural voices — the clearest of the
# ko-KR/en-US sets for learner listening.
SUBJECT_VOICES = {
    'Korean':  'ko-KR-SunHiNeural',
    'English': 'en-US-JennyNeural',
    'Russian': 'ru-RU-SvetlanaNeural',
}
DEFAULT_VOICE = 'ko-KR-SunHiNeural'

HANGUL_RE = re.compile(r'[가-힣]')
# Block-level tags whose end marks a narration chunk boundary.
BLOCK_END_RE = re.compile(r'</p>|</h[1-6]>|</li>|</blockquote>|<br\s*/?>', re.I)
TAG_RE = re.compile(r'<[^>]+>')
# Emoji / pictographs / dingbats — TTS should never see them.
EMOJI_RE = re.compile(
    '[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF'
    '\U00002190-\U000021FF\U00002B00-\U00002BFF️‍]'
)


class Command(BaseCommand):
    help = ('Synthesize narration mp3s (edge-tts + ffmpeg) for every published '
            'story in a Corner collection, named by story order for '
            'import_corner_audio.')

    def add_arguments(self, parser):
        parser.add_argument('--collection', required=True,
                            help='Exact title of the Collection to narrate.')
        parser.add_argument('--out', default=None,
                            help='Output folder (default: corner/management/commands/'
                                 'audio/<collection-slug>/).')
        parser.add_argument('--only', type=int, default=None,
                            help='Only (re)generate the story with this order number.')
        parser.add_argument('--overwrite', action='store_true',
                            help='Regenerate files that already exist (default: skip).')
        parser.add_argument('--gap', type=float, default=0.9,
                            help='Silence between paragraphs, in seconds (default 0.9).')
        parser.add_argument('--rate', default='-5%',
                            help='Speaking rate for edge-tts, e.g. "-10%%" (default "-5%%").')
        parser.add_argument('--voice', default=None,
                            help='Override the narrator voice (default: by subject).')
        parser.add_argument('--voices', default=None,
                            help='Comma-separated voices to cycle through across stories, '
                                 'e.g. alternating male/female narrators (overrides --voice).')
        parser.add_argument('--speaker-voices', default=None,
                            help='Comma-separated pair of voices to alternate PER PARAGRAPH '
                                 'within each story (e.g. "en-US-JennyNeural,en-US-GuyNeural") '
                                 '— for two-speaker dialogue stories where every <p> is one '
                                 "speaker's turn, strictly alternating. Overrides --voice/--voices. "
                                 'Best combined with --only, since each dialogue story usually '
                                 'needs its own voice pair matching its two characters.')

    # ── text extraction ─────────────────────────────────────────────────────

    def _chunks(self, story, korean):
        """Title + one clean text chunk per block element of the body."""
        chunks = []
        for raw in [story.title] + BLOCK_END_RE.split(story.body or ''):
            text = html.unescape(TAG_RE.sub(' ', raw))
            text = EMOJI_RE.sub('', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if not text:
                continue
            if korean and not HANGUL_RE.search(text):
                continue  # Uzbek note / decoration — not for the Korean narrator
            chunks.append(text)
        return chunks

    # ── synthesis ───────────────────────────────────────────────────────────

    def _make_clip(self, chunks, chunk_voices, gap, rate, out_path, workdir):
        import edge_tts

        silence = os.path.join(workdir, 'silence.mp3')
        subprocess.run(
            ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'lavfi',
             '-i', 'anullsrc=r=24000:cl=mono', '-t', str(gap),
             '-acodec', 'libmp3lame', '-b:a', '48k', silence],
            check=True)

        parts = []
        for i, (text, voice) in enumerate(zip(chunks, chunk_voices)):
            part = os.path.join(workdir, f'chunk{i}.mp3')
            # The TTS service call rides the network — retry transient failures
            # (DNS blips, dropped connections) instead of losing the whole run.
            for attempt in range(5):
                try:
                    asyncio.run(edge_tts.Communicate(text, voice, rate=rate).save(part))
                    break
                except Exception:  # noqa: BLE001
                    if attempt == 4:
                        raise
                    wait = 2 ** (attempt + 1)
                    self.stdout.write(self.style.WARNING(
                        f'TTS failed, retrying in {wait}s...'))
                    time.sleep(wait)
            if i:
                parts.append(silence)
            parts.append(part)

        list_path = os.path.join(workdir, 'list.txt')
        with open(list_path, 'w') as fh:
            for p in parts:
                fh.write(f"file '{p}'\n")
        # Re-encode on concat so differing frame params can't corrupt the output.
        subprocess.run(
            ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0',
             '-i', list_path, '-acodec', 'libmp3lame', '-b:a', '48k', '-ac', '1',
             out_path],
            check=True)

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            raise CommandError('edge-tts is not installed. Run: pip install edge-tts')
        if not shutil.which('ffmpeg'):
            raise CommandError('ffmpeg not found on PATH.')

        try:
            collection = Collection.objects.get(title=options['collection'])
        except Collection.DoesNotExist:
            raise CommandError(f"Collection '{options['collection']}' not found.")

        speaker_voices = None
        if options['speaker_voices']:
            speaker_voices = [v.strip() for v in options['speaker_voices'].split(',') if v.strip()]
            if len(speaker_voices) != 2:
                raise CommandError('--speaker-voices needs exactly two comma-separated voices.')
            voices = speaker_voices  # only used for the summary line / korean detection
        elif options['voices']:
            voices = [v.strip() for v in options['voices'].split(',') if v.strip()]
        else:
            voices = [options['voice'] or SUBJECT_VOICES.get(collection.subject.name, DEFAULT_VOICE)]

        out_dir = options['out'] or os.path.join(
            'corner', 'management', 'commands', 'audio', collection.slug)
        os.makedirs(out_dir, exist_ok=True)

        stories = collection.stories.filter(is_published=True).order_by('order')
        if options['only'] is not None:
            stories = stories.filter(order=options['only'])
            if not stories:
                raise CommandError(f"No story with order {options['only']} in "
                                   f"'{collection.title}'.")

        done = skipped = 0
        total = stories.count()
        for i, story in enumerate(stories):
            voice = voices[i % len(voices)]
            korean = voice.startswith('ko-')
            out_path = os.path.join(out_dir, f'{story.order:02d}.mp3')
            if os.path.exists(out_path) and not options['overwrite']:
                skipped += 1
                continue

            chunks = self._chunks(story, korean)
            if len(chunks) < 2:  # title only — body produced no narratable text
                self.stdout.write(self.style.WARNING(
                    f'[{story.order}] no narratable text, skipped: {story.title}'))
                skipped += 1
                continue

            if speaker_voices:
                # chunk 0 = title (speaker A's voice); chunks[1:] alternate A/B per
                # paragraph, so a strictly-alternating two-speaker dialogue (each <p>
                # one turn) gets each speaker read in a consistent, distinct voice.
                chunk_voices = [speaker_voices[0]] + [
                    speaker_voices[(j - 1) % 2] for j in range(1, len(chunks))
                ]
                voice_label = f'{speaker_voices[0]} / {speaker_voices[1]} (alternating)'
            else:
                chunk_voices = [voice] * len(chunks)
                voice_label = voice

            with tempfile.TemporaryDirectory() as workdir:
                self._make_clip(chunks, chunk_voices, options['gap'], options['rate'],
                                out_path, workdir)
            size_kb = os.path.getsize(out_path) // 1024
            done += 1
            self.stdout.write(self.style.SUCCESS(
                f'[{done}/{total}] {os.path.basename(out_path)}  '
                f'({len(chunks)} paragraphs, {size_kb} KB, voice: {voice_label})  {story.title}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone. {done} generated, {skipped} skipped '
            f'(voices: {", ".join(voices)}, out: {out_dir}).'))
