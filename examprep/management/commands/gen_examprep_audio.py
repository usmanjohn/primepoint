"""
Generate listening-lesson audio clips from a lessons data file (local authoring tool).

Scans a ``_lessons_*.py`` data file for blocks that carry BOTH keys::

    {
        "audio":        "listening_010_1.mp3",          # output filename
        "audio_script": [("남자", "안녕하세요."),         # (speaker, Korean line)
                         ("여자", "네, 안녕하세요.")],
        ...
    }

and synthesizes each clip with edge-tts (Microsoft neural voices):
남자/해설 -> ko-KR-InJoonNeural (male), 여자 -> ko-KR-SunHiNeural (female),
joining the lines with a short silence gap via ffmpeg.

Requires (dev machine only — NOT in requirements.txt): ``pip install edge-tts``
and ``ffmpeg`` on PATH. Internet is needed while generating; the resulting mp3s
are plain files, imported afterwards with::

    python manage.py gen_examprep_audio <datafile> --out examprep/management/commands/audio/<topic>
    python manage.py import_examprep <datafile> --author=<username> --audio-dir=<that folder>

Options: ``--only <filename>`` regenerates a single clip; ``--gap`` changes the
pause between lines (seconds); ``--rate`` adjusts speaking speed (e.g. "-10%").
"""

import asyncio
import importlib.util
import os
import shutil
import subprocess
import tempfile

from django.core.management.base import BaseCommand, CommandError

VOICES = {
    "남자": "ko-KR-InJoonNeural",
    "여자": "ko-KR-SunHiNeural",
    "해설": "ko-KR-InJoonNeural",
}
DEFAULT_VOICE = "ko-KR-InJoonNeural"


class Command(BaseCommand):
    help = ("Synthesize listening audio clips (edge-tts + ffmpeg) for every block "
            "with an 'audio' + 'audio_script' pair in a lessons data file.")

    def add_arguments(self, parser):
        parser.add_argument("datafile",
                            help="Path to a _lessons_*.py file exposing LESSONS.")
        parser.add_argument("--out", required=True,
                            help="Output folder for the generated mp3 files.")
        parser.add_argument("--only", default=None,
                            help="Only (re)generate the clip with this filename.")
        parser.add_argument("--gap", type=float, default=0.7,
                            help="Silence between lines, in seconds (default 0.7).")
        parser.add_argument("--rate", default="-5%",
                            help='Speaking rate for edge-tts, e.g. "-10%%" (default "-5%%").')

    # ── helpers ─────────────────────────────────────────────────────────────

    def _load_lessons(self, datafile):
        if not os.path.isfile(datafile):
            raise CommandError(f"Data file not found: {datafile}")
        spec = importlib.util.spec_from_file_location("_examprep_audio_data", datafile)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:  # noqa: BLE001
            raise CommandError(f"Failed to import '{datafile}': {exc}")
        lessons = getattr(module, "LESSONS", None)
        if not isinstance(lessons, list):
            raise CommandError(f"'{datafile}' must define a LESSONS list.")
        return lessons

    def _collect_clips(self, lessons):
        """Yield (filename, script) for every audio block; validate as we go."""
        seen = {}
        for lesson in lessons:
            for block in lesson.get("blocks", []):
                name, script = block.get("audio"), block.get("audio_script")
                if not name and not script:
                    continue
                if not name or not script:
                    raise CommandError(
                        f"Lesson '{lesson.get('title')}': a block has only one of "
                        f"'audio'/'audio_script' — both are needed to generate.")
                if name in seen and seen[name] != script:
                    raise CommandError(f"Duplicate audio filename '{name}' with different scripts.")
                seen[name] = script
        return list(seen.items())

    def _synthesize_line(self, text, voice, rate, path):
        import edge_tts
        asyncio.run(edge_tts.Communicate(text, voice, rate=rate).save(path))

    def _make_clip(self, script, gap, rate, out_path, workdir):
        """TTS each line, then join them with `gap` seconds of silence via ffmpeg."""
        silence = os.path.join(workdir, "silence.mp3")
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
             "-i", "anullsrc=r=24000:cl=mono", "-t", str(gap),
             "-acodec", "libmp3lame", "-b:a", "48k", silence],
            check=True)

        parts = []
        for i, (speaker, text) in enumerate(script):
            voice = VOICES.get(speaker, DEFAULT_VOICE)
            line_path = os.path.join(workdir, f"line{i}.mp3")
            self._synthesize_line(text, voice, rate, line_path)
            if i:
                parts.append(silence)
            parts.append(line_path)

        list_path = os.path.join(workdir, "list.txt")
        with open(list_path, "w") as fh:
            for p in parts:
                fh.write(f"file '{p}'\n")
        # Re-encode on concat so differing frame params can't corrupt the output.
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", list_path, "-acodec", "libmp3lame", "-b:a", "48k", "-ac", "1", out_path],
            check=True)

    # ── main ────────────────────────────────────────────────────────────────

    def handle(self, *args, **options):
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            raise CommandError("edge-tts is not installed. Run: pip install edge-tts")
        if not shutil.which("ffmpeg"):
            raise CommandError("ffmpeg not found on PATH.")

        lessons = self._load_lessons(options["datafile"])
        clips = self._collect_clips(lessons)
        if options["only"]:
            clips = [(n, s) for n, s in clips if n == options["only"]]
            if not clips:
                raise CommandError(f"No block references audio '{options['only']}'.")
        if not clips:
            self.stdout.write(self.style.WARNING("No audio blocks found — nothing to do."))
            return

        out_dir = options["out"]
        os.makedirs(out_dir, exist_ok=True)

        done = 0
        for name, script in clips:
            out_path = os.path.join(out_dir, name)
            with tempfile.TemporaryDirectory() as workdir:
                self._make_clip(script, options["gap"], options["rate"], out_path, workdir)
            size_kb = os.path.getsize(out_path) // 1024
            done += 1
            self.stdout.write(self.style.SUCCESS(
                f"[{done}/{len(clips)}] {name}  ({len(script)} lines, {size_kb} KB)"))

        self.stdout.write(self.style.SUCCESS(f"\nDone. {done} clip(s) in {out_dir}"))
