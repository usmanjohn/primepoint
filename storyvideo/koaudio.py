# -*- coding: utf-8 -*-
"""The Korean voice layer.

The differentiator, and the reason these are not just maths videos with Hangul
in them: **the Korean word is heard in Korean.** The Uzbek narration says
`chulgu` so the pupil can repeat it; a native voice says 출구 so the pupil knows
what it is actually supposed to sound like. An Uzbek transliteration is a
bridge, never the authority -- korean.py says so at the top and this module is
the other half of that sentence.

## Where the clips go, and why that was the hard part

They cannot simply be dropped under the narration: the Uzbek voice is already
speaking for nearly every second of a scene (`voice.retime` cuts each scene to
its own clip), so a Korean word mixed under it is mud. There is no word-level
alignment of the recording to find a hole with, and inventing one would have
meant touching `voice.split`, which took four wrong models to get right.

So the clip gets its own **silent scene** instead -- `scenes.echo`. `retime`
already gives a scene with `say=None` its settle time or three seconds,
whichever is longer, and `mix` already leaves a hole there because it only
places narration into scenes that have any. Nothing in the split machinery had
to change: the word is spoken into a pause that already existed.

That also happens to be the right *teaching* beat. The maths films protect one
silent scene so the viewer can do the sum themselves; a language film protects
one so they can say the word out loud.

## The cache

Clips are generated once by `cli.py kowords <slug>` and committed under
`assets/ko_words/`, for the same reason the fonts are vendored: a render must
never depend on the network. The filename is a hash of (text, voice, rate), so
changing any of them makes a new file and never silently reuses an old one.
"""

import hashlib
import pathlib
import re
import subprocess

SR = 44100
HERE = pathlib.Path(__file__).resolve().parent
CACHE = HERE / "assets" / "ko_words"

# edge-tts, the same engine the site's Prime Korean readings already use.
# Female, against a male Uzbek narration, so the two voices never blur.
VOICE = "ko-KR-SunHiNeural"
RATE = "-10%"          # a word said for imitation, not at conversation speed

# Elements that ask to be spoken. `wordkit.pron(speak=True)` writes it.
SAY_RE = re.compile(r'data-say-ko="([^"]+)"[^>]*?data-at="([\d.]+)"'
                    r'|data-at="([\d.]+)"[^>]*?data-say-ko="([^"]+)"')


def clip_path(text, voice=VOICE, rate=RATE):
    key = hashlib.sha1(f"{text}|{voice}|{rate}".encode()).hexdigest()[:12]
    return CACHE / f"{key}.mp3"


def events(video):
    """[(absolute_seconds, korean_text)] for one video, read from the scenes."""
    out = []
    for start, _end, sc in video.bounds():
        for m in SAY_RE.finditer(sc.html):
            text = m.group(1) or m.group(4)
            at = float(m.group(2) or m.group(3))
            out.append((start + at, text))
    return sorted(out)


def words(video):
    """Every distinct Korean word this video needs a clip for."""
    seen, out = set(), []
    for _t, w in events(video):
        if w not in seen:
            seen.add(w)
            out.append(w)
    return out


def generate(texts, voice=VOICE, rate=RATE, force=False):
    """Fetch any missing clips. The one step that needs the network."""
    import asyncio
    import edge_tts

    CACHE.mkdir(parents=True, exist_ok=True)
    todo = [t for t in texts if force or not clip_path(t, voice, rate).exists()]

    async def one(text):
        path = clip_path(text, voice, rate)
        await edge_tts.Communicate(text, voice, rate=rate).save(str(path))
        return text, path

    async def all_():
        return [await one(t) for t in todo]

    made = asyncio.run(all_()) if todo else []
    return made, [t for t in texts if not clip_path(t, voice, rate).exists()]


def _load(text, voice=VOICE, rate=RATE):
    """One clip as mono float32 at SR, with its silence trimmed off."""
    import numpy as np
    path = clip_path(text, voice, rate)
    if not path.exists():
        return None
    raw = subprocess.run(
        ["ffmpeg", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True).stdout
    pcm = np.frombuffer(raw, dtype="<f4").copy()
    if not len(pcm):
        return None
    # edge-tts pads both ends; a word meant to land on a cue must start when the
    # cue says it does.
    loud = np.abs(pcm) > 0.01
    if loud.any():
        pcm = pcm[max(int(np.argmax(loud)) - int(0.02 * SR), 0):
                  len(pcm) - int(np.argmax(loud[::-1])) + int(0.05 * SR)]
    n = int(0.012 * SR)
    if len(pcm) > 2 * n:                       # no clicks at the joins
        pcm[:n] *= np.linspace(0, 1, n)
        pcm[-n:] *= np.linspace(1, 0, n)
    return pcm


def track(video, seconds, gain=0.8, voice=VOICE, rate=RATE):
    """A mono track of every Korean word this video speaks, or None."""
    import numpy as np
    evs = events(video)
    if not evs:
        return None, []
    buf = np.zeros(int(SR * seconds) + SR, dtype="float32")
    missing = []
    for t, text in evs:
        pcm = _load(text, voice, rate)
        if pcm is None:
            missing.append(text)
            continue
        # Normalise each word to the same loudness: edge-tts varies by several
        # dB between utterances, and a video where one word is twice as loud as
        # the next sounds broken rather than varied.
        peak = float(np.abs(pcm).max())
        if peak > 0:
            pcm = pcm * (0.9 / peak)
        k = int(SR * t)
        end = min(k + len(pcm), len(buf))
        buf[k:end] += pcm[:end - k] * gain
    return buf[:int(SR * seconds)], missing
