# -*- coding: utf-8 -*-
"""Cutting one narration file back into scenes.

The script asks the engine for a 1.5s pause between scenes and shorter ones
inside them, so the boundaries are not guessed -- they are the longest silences
by a wide margin. On the first real clip the scene breaks landed at 2.2-2.7s and
the next longest pause was 1.65s, which is the gap this depends on.

Nothing here trusts that blindly: `split` checks each segment's length against
how much text it should contain and refuses a split that disagrees.
"""

import math
import re
import subprocess


def silences(path, floor=-45, minimum=0.6):
    """[(start, end, duration)] of every silence in the file."""
    r = subprocess.run(
        ["ffmpeg", "-i", str(path), "-af",
         f"silencedetect=noise={floor}dB:d={minimum}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]
    ends = [(float(a), float(b)) for a, b in
            re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", r)]
    out = []
    for i, (end, dur) in enumerate(ends):
        if i < len(starts):
            out.append((starts[i], end, dur))
    return out


def duration(path):
    r = subprocess.run(["ffmpeg", "-i", str(path), "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    m = re.findall(r"time=(\d+):(\d+):(\d+\.\d+)", r)
    if not m:
        return None
    h, mi, s = m[-1]
    return int(h) * 3600 + int(mi) * 60 + float(s)


def split(path, blocks, keep_tail=0.28):
    """Cut `path` into len(blocks) segments, one per narration block.

    Boundaries are chosen so that every SEGMENT ends up as long as its own text
    says it should be, with a mild preference for longer silences to break ties.
    Two earlier rules both failed on real recordings:

      * "the n-1 longest silences" -- pm04 had a 1.97s `||` beat inside a short
        block that outlasted a genuine 1.89s scene break.
      * scoring each boundary's absolute POSITION -- too forgiving. On pm08 an
        extra 0.9s of silence outweighed 3.4s of position error and pushed one
        cut ~3s late, stretching one segment to 1.31x its text and squashing the
        next to 0.55x.

    Scoring the segments themselves fixes both: a late cut is penalised twice,
    once for the segment it lengthens and once for the one it shortens. The
    whole sequence is solved with a DP, not cut by cut.

    Returns [(start, end)] in seconds plus a report, and raises if it looks wrong.
    """
    n = len(blocks)
    total = duration(path)
    sil = silences(path)

    # A trailing silence is the script's final break, not a boundary.
    body = [s for s in sil if s[1] < total - 0.35]
    if len(body) < n - 1:
        raise SystemExit(f"only {len(body)} silences found, need {n - 1} boundaries")

    # A block's length is its characters PLUS the breaks written inside it.
    # Ignoring the breaks made short blocks look 40-60% too long -- they are
    # mostly pause -- and that noise is what hides a genuinely bad cut.
    weights = [max(len(re.sub(r"<[^>]+>", "", b)), 1) for b in blocks]
    pauses = [sum(float(x) for x in re.findall(r"<break time='([\d.]+)s'", b))
              for b in blocks]
    wsum, psum = sum(weights), sum(pauses)

    tail = [x for x in sil if x[1] >= total - 0.35]
    speech_end = tail[0][0] if tail else total

    # How much of the file is actually speech: everything but the boundary
    # silences, whose typical length is the median internal silence.
    med = sorted(s[2] for s in body)[len(body) // 2]
    speech = max(speech_end - (n - 1) * med, speech_end * 0.5)

    # Seconds per character, once the written-in pauses are paid for.
    per_char = max(speech - psum, speech * 0.3) / wsum

    def expected(k):
        return per_char * weights[k] + pauses[k]

    def seg_cost(k, length):
        """How wrong is a block of this length, in log units."""
        return math.log(max(length, 0.25) / expected(k)) ** 2

    # ── Fast path: an unambiguous recording ────────────────────────────
    # Since the scene break was widened to 2.5s the boundaries usually stand
    # far clear of everything else (~3.4s vs <2s). When exactly n-1 silences
    # are that much longer, the evidence is overwhelming and no amount of
    # text-proportion cleverness should be allowed to override it -- that is
    # how pm94 lost a real 3.4s boundary to a 1.6s pause.
    max_d = max(s[2] for s in body)
    strong = [s for s in body if s[2] >= 0.55 * max_d]
    rest_d = [s[2] for s in body if s[2] < 0.55 * max_d]
    # It is only a HYPOTHESIS: on pm94 nine silences looked like clean
    # boundaries, but taking them left one block at 1.6s where its text wanted
    # 6.2s -- the engine had stretched a pause inside a block to full boundary
    # length. So the guess must survive the same validation as any other split,
    # and falls through to the solver when it does not.
    if len(strong) == n - 1 and (not rest_d or
                                 min(s[2] for s in strong) >= 1.5 * max(rest_d)):
        got = _finish(sorted(strong, key=lambda s: s[0]), sil, total, speech_end,
                      keep_tail, blocks, weights, pauses, wsum, "clean",
                      strict=False)
        if got is not None:
            return got

    # ── Otherwise: solve it. Some break did not render at its full length,
    # so duration alone cannot be trusted and the segment proportions decide.
    # The bonus is scaled by the LOUDEST silence in this recording, so a 0.13s
    # difference between two 1.3s pauses cannot outweigh a 2s segment error --
    # which is exactly the call pm55 got wrong.
    BONUS = 0.6
    m, INF = len(body), float("inf")
    cost = [[INF] * m for _ in range(n - 1)]
    back = [[-1] * m for _ in range(n - 1)]

    for j in range(m):
        cost[0][j] = seg_cost(0, body[j][0]) - BONUS * body[j][2] / max_d
    for k in range(1, n - 1):
        for j in range(m):
            best, bj = INF, -1
            for jp in range(j):
                if cost[k - 1][jp] == INF:
                    continue
                length = body[j][0] - body[jp][1]
                if length <= 0:
                    continue
                c = cost[k - 1][jp] + seg_cost(k, length)
                if c < best:
                    best, bj = c, jp
            if bj >= 0:
                cost[k][j] = best - BONUS * body[j][2] / max_d
                back[k][j] = bj

    best, last = INF, -1
    for j in range(m):
        if cost[n - 2][j] == INF:
            continue
        c = cost[n - 2][j] + seg_cost(n - 1, speech_end - body[j][1])
        if c < best:
            best, last = c, j
    if last < 0:
        raise SystemExit("could not place the boundaries in order")

    chosen, j = [last], last
    for k in range(n - 2, 0, -1):
        j = back[k][j]
        chosen.append(j)
    chosen.reverse()
    cuts = [body[j] for j in chosen]
    return _finish(cuts, sil, total, speech_end, keep_tail, blocks,
                   weights, pauses, wsum, "dp")


def _finish(cuts, sil, total, speech_end, keep_tail, blocks,
            weights, pauses, wsum, how, strict=True):
    """Turn chosen boundaries into segments, and refuse an implausible split.

    strict=False returns None instead of raising, so a guess can be tested.
    """
    psum = sum(pauses)
    segs, prev = [], 0.0
    for start, end, _d in cuts:
        segs.append((prev, min(start + keep_tail, end)))
        prev = end - 0.05
    segs.append((prev, min(speech_end + keep_tail, total)))

    # Validate: a segment's length should track how much text it carries.
    dsum = sum(e - s for s, e in segs)
    scale = (dsum - psum) / wsum if dsum > psum else dsum / wsum
    ratios, bad = [], []
    for i, ((s, e), w) in enumerate(zip(segs, weights), 1):
        want = scale * w + pauses[i - 1]
        got = e - s
        ratios.append(got / want)
        if got < want * 0.55 or got > want * 1.8:
            bad.append(f"  block {i}: {got:.1f}s but its text suggests ~{want:.1f}s")
    if bad:
        if not strict:
            return None
        raise SystemExit("split looks wrong:\n" + "\n".join(bad))
    return segs, {"worst": max(abs(1 - r) for r in ratios),
                  "shortest": min(c[2] for c in cuts), "how": how,
                  "candidates": len(cuts) + 1}


SR = 44100

# The voice is normalised to this before cues are mixed under it, leaving
# deliberate headroom for them. See mix().
VOICE_LEVEL = 0.86


def settle_of(scene):
    """When a scene has finished moving -- its animations, not its authored length."""
    m = 0.0
    for a, d in re.findall(r'data-at="([\d.]+)"[^>]*data-dur="([\d.]+)"', scene.html):
        m = max(m, float(a) + float(d))
    for d, a in re.findall(r'data-dur="([\d.]+)"[^>]*data-at="([\d.]+)"', scene.html):
        m = max(m, float(a) + float(d))
    return m + 0.35


def decode(path):
    """The whole file as mono float32 at SR."""
    import numpy as np
    raw = subprocess.run(
        ["ffmpeg", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
        capture_output=True).stdout
    return np.frombuffer(raw, dtype="<f4").copy()


def retime(video, segs, outro=3.0):
    """Give every narrated scene the length of its own clip.

    This is the fix for the sync problem in one line: the picture is cut to the
    voice, which is what every other medium does and what this pipeline was not
    doing. A scene never gets shorter than its animation needs, so a long
    sentence stretches the beat and a short one cannot truncate it.
    """
    rows, k = [], 0
    for sc in video.scenes:
        old, settle = sc.dur, settle_of(sc)
        narrated = getattr(sc, "say", None)
        if narrated and k < len(segs):
            clip = segs[k][1] - segs[k][0]
            k += 1
            sc.dur = round(max(clip, settle), 3)
            why = "clip" if sc.dur > settle else f"settle (clip {clip:.1f}s too short)"
        else:
            sc.dur = round(max(outro, settle), 3)
            why = "silent"
        rows.append((sc.name, old, sc.dur, why))
    return rows


def mix(video, audio_path, segs, sfx_track=None):
    """Voice placed scene by scene, with the sound layer under it."""
    import numpy as np
    pcm = decode(audio_path)
    total = video.duration
    out = np.zeros(int(SR * total) + SR, dtype="float32")
    spoken = [(a, sc) for a, _b, sc in video.bounds() if getattr(sc, "say", None)]
    for (start, _sc), (s, e) in zip(spoken, segs):
        clip = pcm[int(s * SR):int(e * SR)]
        k = int(start * SR)
        out[k:k + len(clip)] += clip
    out = out[:int(SR * total)]

    # Normalise the VOICE to a fixed level before the cues go under it. This is
    # what pm25 got wrong: the cues were added to a near-full-scale voice and the
    # final limiter then scaled the whole mix down, so the cues ended up
    # inaudible while the voice stayed loud. Fixing the voice first makes the
    # cue level mean the same thing on every video, whatever the engine returned.
    vpeak = float(np.abs(out).max())
    if vpeak > 0:
        out *= VOICE_LEVEL / vpeak

    if sfx_track is not None:
        n = min(len(out), len(sfx_track))
        out[:n] += sfx_track[:n].astype("float32")
    peak = float(np.abs(out).max())
    if peak > 0.97:
        out *= 0.97 / peak
    return out
