# -*- coding: utf-8 -*-
"""The sound layer.

Everything is synthesised: no files to ship, nothing to load, and each cue is
placed from the same `data-at` times that drive the picture, so sound and image
cannot drift apart.

These sit UNDER a voice, so every cue is short and low-passed by nature (simple
sines, no bright transients). A count of 37 items is 37 cues in six seconds --
at the wrong volume that is a woodpecker, so ticks stay the quietest thing here
and rise slightly in pitch so a run of them reads as one gesture rather than 37
separate events.

⚠️ LEVELS, 2026-08-29: the first mix (pm25) was too quiet to hear under the
voice, so every cue was raised ~3x and `mix()` now normalises the voice to a
fixed 0.86 BEFORE the cues are added -- previously a loud voice simply buried
them. `GAIN` below scales the whole layer; `--sfx-gain` on the `voice` command
overrides it per render, so the balance can be tuned without editing this file.
"""

import re
import numpy as np

SR = 44100

# Master level for the whole cue layer. Raise via --sfx-gain, not by
# editing the individual cues -- their balance against each other is tuned.
GAIN = 1.0


def _env(n, attack=0.004, decay=1.0):
    a = int(SR * attack) or 1
    e = np.ones(n)
    e[:a] = np.linspace(0, 1, a)
    e[a:] = np.exp(-np.linspace(0, decay * 6, n - a))
    return e


def tick(i=0, n=1, si=0):
    """A soft blip as one countable thing lands. Pitch climbs across the run,
    and each scene starts from a slightly different note (`si` = scene index)
    so two counting scenes in one video do not sound like the same run twice."""
    d = 0.045
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    f = (700 + 55 * (si % 4)) + 420 * (i / max(n - 1, 1))
    return 0.16 * np.sin(2 * np.pi * f * t) * _env(len(t), 0.002, 1.6)


def pop():
    """A number arriving: low, round, no click."""
    d = 0.16
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    w = (np.sin(2 * np.pi * 196 * t) + 0.5 * np.sin(2 * np.pi * 392 * t))
    return 0.30 * w * _env(len(t), 0.006, 1.1)


def thud():
    """A correction landing."""
    d = 0.24
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    f = 150 * np.exp(-3 * t)                       # falling pitch
    return 0.34 * np.sin(2 * np.pi * f * t) * _env(len(t), 0.004, 0.9)


def chime():
    """The answer resolving. The only warm, ringing sound in the kit."""
    d = 0.85
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    w = (np.sin(2 * np.pi * 587 * t) + 0.6 * np.sin(2 * np.pi * 880 * t)
         + 0.3 * np.sin(2 * np.pi * 1174 * t))
    return 0.26 * w * _env(len(t), 0.008, 0.55)


def swell():
    """A card arriving. Felt more than heard."""
    d = 0.5
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    f = 120 + 90 * (t / d)
    return 0.17 * np.sin(2 * np.pi * f * t) * np.sin(np.pi * t / d) ** 2


def boom():
    """The opening number, and a corrected answer landing. The only cue with
    real weight -- it marks the two moments the video is ABOUT."""
    d = 0.55
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    f = 110 * np.exp(-1.6 * t)                     # deep, falling
    w = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t)
    return 0.26 * w * _env(len(t), 0.010, 0.75)


def rise():
    """A bar growing. An upward glide, so a chart sounds like it is being
    built rather than stamped out."""
    d = 0.42
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    f = 220 + 260 * (t / d) ** 1.4
    return 0.13 * np.sin(2 * np.pi * f * t) * np.sin(np.pi * t / d) ** 1.3


def quest():
    """The open question. Two notes going UP -- the only unresolved cue in the
    kit, which is the whole point of the `ask` scene."""
    d = 0.5
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    half = len(t) // 2
    w = np.concatenate([np.sin(2 * np.pi * 494 * t[:half]),
                        np.sin(2 * np.pi * 659 * t[half:])])
    return 0.12 * w * _env(len(t), 0.008, 0.9)


def settle():
    """Under the first frame of a DARK scene. Felt, not heard -- it marks the
    turn from story to lesson without anything appearing on screen."""
    d = 1.2
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    w = np.sin(2 * np.pi * 87 * t) + 0.4 * np.sin(2 * np.pi * 131 * t)
    return 0.10 * w * np.sin(np.pi * t / d) ** 1.8


def blip():
    """A line of text arriving. The smallest voice in the kit."""
    d = 0.09
    t = np.linspace(0, d, int(SR * d), endpoint=False)
    w = np.sin(2 * np.pi * 523 * t) + 0.35 * np.sin(2 * np.pi * 784 * t)
    return 0.13 * w * _env(len(t), 0.004, 1.4)


def whoosh():
    """Somebody walks into frame. Noise, not a tone, so it never sings a pitch
    against the voice. Seeded, because a render must be reproducible."""
    d = 0.28
    n = int(SR * d)
    noise = np.random.default_rng(7).standard_normal(n)
    # one-pole low-pass: the hiss becomes air
    out, acc = np.empty(n), 0.0
    for i, x in enumerate(noise):
        acc += 0.045 * (x - acc)
        out[i] = acc
    out /= max(np.abs(out).max(), 1e-9)
    return 0.30 * out * np.sin(np.pi * np.linspace(0, 1, n)) ** 1.6


# class fragment -> cue. First match wins, so order matters: the specific
# component classes are tested before the generic text ones at the bottom.
RULES = [
    (("crowd__c", "seat--full", "chip", "pack", "sq--on", "tblbox", "side", "term",
      "solve__row", "tick", "bar__v"), "tick"),
    (("bar__b",), "rise"),
    (("cmp__u",), "pop"),
    (("strike",), "thud"),
    (("grn",), "chime"),
    (("card",), "swell"),
    # `hero` before the generic pop: the hook's number and a corrected answer
    # both use it, and both deserve weight. `ask` before the generic blip.
    (("hero",), "boom"),
    (("ask",), "quest"),
    (("big", "counter", "expr"), "pop"),
    # 2026-08-29: these used to be silent. A person arriving, a bubble opening
    # and a heading landing are all visible events, so they get a voice too --
    # blip is deliberately the quietest cue so a label never upstages a number.
    (("figbox", "spot", "bubble"), "whoosh"),
    (("ttl", "ask", "cap", "lbl"), "blip"),
]

EVENT_RE = re.compile(r'class="([^"]*)"[^>]*data-at="([\d.]+)"'
                      r'|data-at="([\d.]+)"[^>]*class="([^"]*)"')


def events(video):
    """[(absolute_seconds, cue)] for one video, read from the built scenes."""
    out = []
    for si, (start, _end, sc) in enumerate(video.bounds()):
        # A dark scene is the turn from story to lesson. Nothing announces it
        # on screen, so the sound does -- under the first frame, felt not heard.
        if getattr(sc, "dark", False):
            out.append((start + 0.05, ("settle", 0, 1, si)))
        found = []
        for m in EVENT_RE.finditer(sc.html):
            cls = m.group(1) or m.group(4) or ""
            at = float(m.group(2) or m.group(3))
            cue = next((c for frags, c in RULES if any(f in cls for f in frags)), None)
            if cue:
                found.append((at, cue, cls))
        # ticks within a scene share one rising run
        ticks = [f for f in found if f[1] == "tick"]
        for i, (at, cue, _c) in enumerate(sorted(found)):
            if cue == "tick":
                j = sorted(ticks).index((at, cue, _c))
                out.append((start + at, ("tick", j, len(ticks), si)))
            else:
                out.append((start + at, (cue, 0, 1, si)))
    return sorted(out)


MAKE = {"tick": tick, "pop": pop, "thud": thud, "chime": chime,
        "swell": swell, "blip": blip, "whoosh": whoosh,
        "boom": boom, "rise": rise, "quest": quest, "settle": settle}


def track(video, seconds, gain=None):
    """A mono float track of the whole video's cues."""
    g = GAIN if gain is None else gain
    buf = np.zeros(int(SR * seconds) + SR)
    for t, (cue, i, n, si) in events(video):
        w = MAKE[cue](i, n, si) if cue == "tick" else MAKE[cue]()
        k = int(SR * t)
        buf[k:k + len(w)] += w
    buf *= g
    # Only a true overlap pile-up should be pulled back; this is a safety
    # limiter, not the level control -- that is `gain`.
    peak = np.abs(buf).max()
    if peak > 0.92:
        buf *= 0.92 / peak
    return buf[:int(SR * seconds)]


def write_wav(buf, path):
    import wave
    pcm = (np.clip(buf, -1, 1) * 32767).astype("<i2")
    with wave.open(str(path), "wb") as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR)
        f.writeframes(pcm.tobytes())
    return path
