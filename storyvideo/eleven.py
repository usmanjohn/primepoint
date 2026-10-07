# -*- coding: utf-8 -*-
"""ElevenLabs narration — the recording step, done by the pipeline instead of by hand.

Until 2026-10-08 the narration was made by pasting `tts_scripts/<slug>_tts_one.txt`
into a TTS website and saving the mp3 into `tts_audios/`. This module does that step:

    python3 cli.py eleven ko35          # -> tts_audios/ko_35.mp3

It voices EACH NARRATION BLOCK SEPARATELY and joins them with exactly the scene
break the script asks for (2.5 s). Two things follow, and both are the point:

- `check` and `voice` are untouched — they still read one mp3 + one script, and
  the n-1 scene silences are now exact, so the split is always forced (SERIES §7.1.1).
- the dropped-text fault (SERIES §7.1) can only hit ONE block, and that block can
  be re-voiced alone: `cli.py eleven ko35 --only 4` re-uses the cached others.

Model: `eleven_v4` — the ONLY model that speaks Uzbek (reference_elevenlabs memory:
eleven_v3 reads Uzbek with an English accent and cost a wasted batch on 2026-10-07).
Voice: the user's own «Jahongir», WITHOUT the storyteller's grandfather tag — a
Reel wants a teacher, not a fairy tale. Needs ELEVENLABS_API_KEY in the environment.
Standard library + ffmpeg only, like the rest of storyvideo.
"""

import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
CACHE = HERE / "out" / "eleven"

VOICE = {
    "voice_id": "xDwfBjUEPdIoQekNOXAX",       # «Jahongir — Calm, Proud, Deep», his own
    "model_id": "eleven_v4",
    "language_code": "uz",
    "voice_settings": {"speed": 1.08, "stability": 0.5, "similarity_boost": 0.8},
    "lead_tag": "[clear, lively, friendly teacher]",
}
SR = 44100


def to_eleven(block):
    """The edge-tts SSML dialect -> what ElevenLabs reads.

    The inner beats become v4 AUDIO TAGS, not SSML: <break> is documented for the
    older models only, and an unsupported tag risks being read aloud. v4 follows
    tags like [pause] (reference_elevenlabs memory). ‖ (0.45 s) -> [pause],
    | (0.3 s) -> [short pause]. <emphasis> has no equivalent: the tag goes, the
    word stays.
    """
    s = re.sub(r"<break time='([\d.]+)s' ?/>",
               lambda m: " [pause] " if float(m.group(1)) >= 0.4 else " [short pause] ",
               block)
    s = re.sub(r"</?emphasis[^>]*>", "", s)
    return re.sub(r"\s+", " ", s).strip()


def _key(text, cfg):
    raw = json.dumps([text, cfg], sort_keys=True, ensure_ascii=False)
    return hashlib.sha1(raw.encode()).hexdigest()[:16]


def speak(text, out_path, cfg=VOICE):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY is not set — `source ~/.zshrc` in the shell "
                 "that runs this command")
    body = {"text": f"{cfg.get('lead_tag', '')} {text}".strip(),
            "model_id": cfg["model_id"],
            "language_code": cfg["language_code"],
            "voice_settings": cfg["voice_settings"]}
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['voice_id']}"
        f"?output_format=mp3_44100_128",
        data=json.dumps(body).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"})
    try:
        audio = urllib.request.urlopen(req, timeout=180).read()
    except urllib.error.HTTPError as err:
        sys.exit(f"ElevenLabs {err.code}: {err.read()[:300]!r}")
    pathlib.Path(out_path).write_bytes(audio)
    return out_path


def _trim(src, dst):
    """Cut the lead-in and tail silence, keep 60 ms each side, mono wav."""
    af = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,"
          "areverse,"
          "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.06,"
          "areverse")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-af", af,
                    "-ac", "1", "-ar", str(SR), str(dst)], check=True)


def record(blocks, out_mp3, scene_break=2.5, only=None, cfg=VOICE):
    """Voice every block, join with exact scene breaks, write one mp3.

    `only` = 1-based block numbers to re-voice even if cached.
    Returns [(n, chars, seconds, cached?)].
    """
    CACHE.mkdir(parents=True, exist_ok=True)
    rows, wavs = [], []
    for n, block in enumerate(blocks, 1):
        text = to_eleven(block)
        k = _key(text, cfg)
        mp3, wav = CACHE / f"{k}.mp3", CACHE / f"{k}.wav"
        fresh = only is not None and n in only
        if fresh or not mp3.exists():
            if fresh and mp3.exists():
                # a re-take of the SAME text: keep the old one aside, never overwrite blind
                mp3.rename(CACHE / f"{k}.prev.mp3")
            speak(text, mp3, cfg)
            cached = False
        else:
            cached = True
        _trim(mp3, wav)
        wavs.append(wav)
        rows.append((n, len(text), _dur(wav), cached))

    # silence between blocks, then concat -> mp3
    gap = CACHE / f"gap_{scene_break}.wav"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                    f"anullsrc=r={SR}:cl=mono", "-t", str(scene_break), str(gap)],
                   check=True)
    lst = CACHE / "concat.txt"
    seq = []
    for i, w in enumerate(wavs):
        if i:
            seq.append(gap)
        seq.append(w)
    lst.write_text("".join(f"file '{p}'\n" for p in seq))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c:a", "libmp3lame", "-b:a", "160k",
                    str(out_mp3)], check=True)
    return rows


def _dur(path):
    r = subprocess.run(["ffmpeg", "-i", str(path), "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.findall(r"time=(\d+):(\d+):([\d.]+)", r.stderr)
    h, mnt, s = m[-1]
    return int(h) * 3600 + int(mnt) * 60 + float(s)


def transcribe(mp3):
    """ElevenLabs speech-to-text (scribe_v1, Uzbek) -> what the take actually says.

    The settle-it tool for a `check` flag (SERIES §7.4): v4's pace varies more
    than edge-tts', so a speech-rate flag is a question, and the transcript
    answers it — every word there or not, and whether a [laughs] tag was
    performed or read out as a word. Costs a few seconds of STT quota per block.
    """
    import uuid
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY is not set")
    b = uuid.uuid4().hex
    field = lambda n, v: f"--{b}\r\nContent-Disposition: form-data; name=\"{n}\"\r\n\r\n{v}\r\n"
    body = (field("model_id", "scribe_v1") + field("language_code", "uz")
            + f"--{b}\r\nContent-Disposition: form-data; name=\"file\"; "
              f"filename=\"a.mp3\"\r\nContent-Type: audio/mpeg\r\n\r\n").encode()
    body += pathlib.Path(mp3).read_bytes() + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(
        "https://api.elevenlabs.io/v1/speech-to-text", data=body,
        headers={"xi-api-key": key,
                 "Content-Type": f"multipart/form-data; boundary={b}"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=180).read())["text"]
    except urllib.error.HTTPError as err:
        sys.exit(f"ElevenLabs STT {err.code}: {err.read()[:300]!r}")
