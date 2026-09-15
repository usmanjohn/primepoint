# -*- coding: utf-8 -*-
"""storyvideo — build, check and render one story video.

    python -m storyvideo lint    pm04        three gates, no rendering
    python -m storyvideo sheet   pm04        contact sheet of every scene
    python -m storyvideo preview pm04        scrubbable stage in Chrome
    python -m storyvideo render  pm04        the mp4 + the cue sheet
    python -m storyvideo draft   4           spec skeleton from the Corner story

Run from the storyvideo/ directory (or as `python -m storyvideo` from the repo
root).
"""

import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build            # noqa: E402
import cue              # noqa: E402
import lint as lintmod  # noqa: E402
import render as R      # noqa: E402

# Three folders, three lifetimes:
#   tts_scripts/  the TTS text he pastes into the engine, and the as-recorded copy
#   tts_audios/   the voices he generates from it (his, not written here)
#   videos/       the finished mp4s -- the only thing anyone else ever wants
#   out/          working artifacts: stage html, frames, sheets, mixes, logs.
#                 All regenerable and safe to delete at any time.
#
# NOT called "scripts/": the repo's venv gitignore block has a bare `[Ss]cripts`
# rule, so a folder with that name is silently invisible to git.
OUT = HERE / "out"
SCRIPTS = HERE / "tts_scripts"
VIDEOS = HERE / "videos"
for _d in (OUT, SCRIPTS, VIDEOS):
    _d.mkdir(exist_ok=True)


def _scene_times(v):
    """One settled frame per scene -- what a scene looks like once it has landed."""
    return [min(b - 0.35, a + s.dur * 0.86) for a, b, s in v.bounds()]


def cmd_lint(a):
    v = build.load_story(a.slug)
    stage = build.build(v)
    return 1 if lintmod.run(v, stage, layout=not a.fast) else 0


def cmd_sheet(a):
    v = build.load_story(a.slug)
    stage = build.build(v, guides=a.guides)
    d = OUT / f"{a.slug}_frames"
    times = _scene_times(v) if a.per_scene else [i * a.every for i in
                                                 range(int(v.duration // a.every) + 1)]
    frames = R.shoot(stage, times, d, guides=a.guides)
    out = R.contact_sheet(frames, OUT / f"{a.slug}_sheet.png",
                          cols=a.cols, tile_w=310)
    print(f"-> {out}  ({len(frames)} frames)")
    return 0


def cmd_preview(a):
    v = build.load_story(a.slug)
    stage = build.build(v, guides=True, tail=SCRUB)
    print(f"-> {stage}")
    subprocess.run(["open", "-a", "Google Chrome", str(stage)])
    return 0


def cmd_render(a):
    v = build.load_story(a.slug)
    stage = build.build(v)

    if not a.skip_lint:
        if lintmod.run(v, stage, layout=True):
            print("\nlint failed — fix it or pass --skip-lint")
            return 1
        print()

    out = R.render(v, stage, fps=a.fps, workers=a.workers)
    got = R.duration_of(out)
    print(f"-> {out}  {out.stat().st_size / 1e6:.1f} MB  "
          f"spec {v.duration:.2f}s / file {got:.2f}s")
    if got and abs(got - v.duration) > 0.3:
        print(f"   WARNING: encoded length is off by {abs(got - v.duration):.2f}s")

    # Cue sheet, with a thumbnail of each scene.
    d = OUT / f"{a.slug}_frames"
    frames = R.shoot(stage, _scene_times(v), d)
    sheet = cue.build(v, thumbs=dict(enumerate(frames)))
    print(f"-> {sheet}")

    vs = R.sheet_from_video(out, OUT / f"{a.slug}_check.png", every=max(1, int(v.duration // 30)))
    print(f"-> {vs}  (contact sheet taken from the encoded file)")
    return 0


# The engine's paste box. SSML tags are counted too, and they are not cheap:
# every scene boundary costs 28 characters and every <emphasis> pair 38.
LIMIT = 2000


def cmd_script(a):
    import re as _re
    import speech
    v = build.load_story(a.slug)
    v._ssml = a.ssml
    txt = speech.script_one(v, a.ssml) if a.one else speech.script(v)
    out = SCRIPTS / (f"{a.slug}_tts_one.txt" if a.one else f"{a.slug}_tts.txt")
    out.write_text(txt, encoding="utf-8")
    print(txt)
    print(f"\n-> {out}   ({len(txt)} belgi, ~{len(txt.split())} soʻz)")

    bad = 0
    if a.one and len(txt) > LIMIT:
        print(f"   ⚠️  CHEGARADAN {len(txt) - LIMIT} BELGI OSHDI — "
              f"eng koʻpi {LIMIT} (SSML teglari ham sanaladi). Qisqartiring.")
        bad = 1
    elif a.one and len(txt) > LIMIT * 0.95:
        print(f"   ⚠️  chegaraga juda yaqin ({LIMIT - len(txt)} belgi qoldi).")

    # Rule: the engine never sees a digit -- it cannot read Uzbek numerals.
    # Tags are stripped first, so <break time='1.5s'> does not trip this.
    left = sorted(set(_re.findall(r"\d+", _re.sub(r"<[^>]+>", " ", txt))))
    if left:
        print(f"   ⚠️  matnda raqam qoldi: {', '.join(left)} — "
              f"speech.py ularni soʻzga aylantira olmadi.")
        bad = 1

    # Same rule, second alphabet: an Uzbek voice reads Hangul as silence, so
    # nothing Korean may survive into the paste. korean.py transliterates it
    # inside for_tts(); anything left here escaped that path.
    # Two things Korean-adjacent that CANNOT be transliterated, so the gate
    # refuses them instead of guessing:
    #   * hanja — 出 has several Korean readings, there is nothing to compute;
    #   * a lone jamo — ㄱ is a consonant with no vowel, and it lives in a
    #     different Unicode block from 가-힣, so the check above never sees it.
    # Both are fine ON SCREEN. In narration, write the sound in Uzbek.
    lone = sorted(set(_re.findall(r"[\u3130-\u318f\u4e00-\u9fff]+", txt)))
    if lone:
        print(f"   ⚠️  matnda hanja/yakka harf qoldi: {', '.join(lone)} — "
              f"ovozga bermang, `say` satrida uni oʻzbekcha ayting "
              f"(ekranda qolaversin).")
        bad = 1

    # ── BLOCK LENGTH (added 2026-09-15) ─────────────────────────────────
    #
    # The engine silently drops part of a long block, and the ONLY reliable
    # predictor is length. Measured over 105 blocks in 13 recordings:
    #
    #     0-120 chars   59 blocks   0 dropped      <- the safe zone
    #   120-160 chars   27 blocks   1 dropped  3.7%
    #   160-200 chars   17 blocks   1 dropped  5.9%
    #       200+        2 blocks    1 dropped   50%
    #
    # By sentence count, 1-2 sentences never failed in 45 blocks; 5 sentences
    # failed 11% of the time. ko07 is the case study: 181 chars dropped a
    # clause, 143 dropped another, 110 finally worked.
    #
    # This is a warning BEFORE recording, which is the whole point -- every
    # earlier version of this problem cost a re-record.
    import speech as _sp
    v_ = build.load_story(a.slug)
    long_blocks = []
    for i, sc in enumerate([x for x in v_.scenes if getattr(x, "say", None)], 1):
        n = len(_re.sub(r"<[^>]+>", "", _sp.for_tts(sc.say)))
        sents = len([t for t in _re.split(r"(?<=[.?!])\s+",
                     _re.sub(r"<[^>]+>", "", _sp.for_tts(sc.say)).strip()) if t])
        if n > 160 or sents > 4:
            long_blocks.append((i, n, sents))
    if long_blocks:
        hard = [x for x in long_blocks if x[1] > 200]
        print(f"   {'⚠️ ' if hard else 'ⓘ  '} BLOK UZUNLIGI — engine uzun blokdan "
              f"matn tashlab ketishi mumkin:")
        for i, n, q in long_blocks:
            risk = "50%" if n > 200 else "~6%"
            print(f"       {i}-blok: {n} belgi, {q} gap  (tushib qolish "
                  f"ehtimoli {risk}) — 120 belgidan past tushirsangiz 0%")
        print(f"       Rasm allaqachon aytadigan narsani ovozdan olib tashlang.")

    # ── PRONUNCIATION REVIEW (added 2026-09-15) ─────────────────────────
    #
    # The user was hand-fixing prime/examprep/XVIII in every paste and said,
    # correctly, that this is manual work in a pipeline meant to automate. The
    # lexicon in speech.py now converts the KNOWN cases; this surfaces the rest
    # so they are reviewed instead of read past.
    #
    # His instruction, and it is the right one: "always try to not read but HEAR
    # how it will be delivered". I cannot hear, so the substitute is a short,
    # high-signal list of every token where pronunciation risk actually lives --
    # not the whole script, which is where the risk hides.
    bare = _re.sub(r"<[^>]+>", " ", txt)

    # A Roman numeral surviving is a hard failure: an Uzbek voice reads it as
    # letters or as nothing. speech.py converts them; anything here escaped it.
    rom = sorted(set(_re.findall(r"\b(?=[IVXLCDM]{2,}\b)[IVXLCDM]+\b", bare)))
    if rom:
        print(f"   ⚠️  RIM RAQAMI QOLDI: {', '.join(rom)} — "
              f"speech.py ularni soʻzga aylantira olmadi.")
        bad = 1

    # Cyrillic has no business in a Latin-Uzbek script and the engine will not
    # read it as intended. Found on mo31: "kichrayди" -- д and и typed on a
    # Cyrillic keyboard, invisible to the eye at a glance and invisible to the
    # capitalisation check above, because it looks like ordinary lowercase.
    cyr = sorted(set(_re.findall(r"[\u0400-\u04ff\u0500-\u052f]+", bare)))
    if cyr:
        print(f"   ⚠️  KIRILL HARF QOLDI: {', '.join(cyr)} — lotin "
              f"oʻzbekchada yozing (д/и/г lar koʻzga oddiy koʻrinadi).")
        bad = 1

    # Tokens the engine is most likely to mispronounce, in one short list:
    #   * letters outside the Uzbek Latin alphabet (w; c not part of ch)
    #   * ALL-CAPS runs, i.e. acronyms
    #   * capitalised words that are NOT sentence-initial, i.e. real names
    words = _re.findall(r"[A-Za-zʻʼ]+", bare)
    starts = set()
    for m in _re.finditer(r"(?:^|[.?!]\s+)([A-Za-zʻʼ]+)", bare, _re.M):
        starts.add(m.group(1))
    odd = {w for w in words
           if _re.search(r"w|c(?!h)", w, _re.I)
           or (w.isupper() and len(w) > 1)
           or (w[:1].isupper() and w not in starts)}
    if odd:
        print(f"   TEKSHIRING — talaffuzni koʻzdan kechiring: "
              f"{', '.join(sorted(odd))}")
        print(f"      (notoʻgʻri oʻqiladigani bo'lsa, speech.py dagi SAY_AS ga "
              f"qoʻshing — qoʻlda tuzatmang)")

    han = sorted(set(_re.findall(r"[가-힣]+", txt)))
    if han:
        import korean as _ko
        print(f"   ⚠️  matnda hangul qoldi: {', '.join(han)} — "
              f"oʻzbekchada: {', '.join(_ko.uz(h) for h in han)}")
        bad = 1
    return bad


def cmd_voice(a):
    """Cut the picture to a narration recording, add the sound layer, mux."""
    import re as _re
    import numpy as np
    import koaudio as KO
    import sfx as SFX
    import voice as V

    v = build.load_story(a.slug)
    script = pathlib.Path(a.script).read_text(encoding="utf-8")
    # A scene boundary is the LONG break; anything shorter is a beat inside a
    # scene. Read the number instead of matching a literal "1.5s" -- that
    # hardcoding meant changing speech.SCENE_BREAK would have silently split
    # every script into one block, and it also keeps older scripts working.
    parts = _re.split(r"<break time='([\d.]+)s' ?/>", script)
    blocks, cur = [], parts[0]
    for i in range(1, len(parts), 2):
        if float(parts[i]) >= 1.0:
            blocks.append(cur)
            cur = parts[i + 1]
        else:
            # Keep the tag: split() prices a block's breaks into how long it
            # should take, and a short block is mostly break.
            cur += f"<break time='{parts[i]}s' />" + parts[i + 1]
    blocks.append(cur)
    blocks = [b.strip() for b in blocks if b.strip()]
    print(f"{len(blocks)} narration blocks · {len(v.scenes)} scenes")

    segs, rep = V.split(a.audio, blocks)
    print(f"split OK ({rep['how']}) — eng qisqa chegara {rep['shortest']:.2f}s, "
          f"eng yomon segment matnidan {rep['worst']*100:.0f}% farq")

    rows = V.retime(v, segs)
    print(f"\n{'scene':<24}{'was':>8}{'now':>8}   from")
    for name, old, new, why in rows:
        print(f"{name:<24}{old:>7.1f}s{new:>7.1f}s   {why}")
    print(f"{'TOTAL':<24}{'':>8}{v.duration:>7.1f}s")

    if lintmod.run(v, build.build(v), layout=True):
        print("\nlint failed on the retimed cut")
        return 1

    stage = build.build(v)
    out = R.render(v, stage, fps=a.fps, workers=a.workers)

    track = SFX.track(v, v.duration, gain=a.sfx_gain) if not a.no_sfx else None
    if track is not None:
        import numpy as _np
        print(f"sfx: {len(SFX.events(v))} ta ovoz, gain {a.sfx_gain:g}, "
              f"eng baland {float(_np.abs(track).max()):.2f}")

    # The Korean voice rides in the same layer, because that layer is added
    # AFTER the narration has been normalised -- so a word's level means the
    # same thing on every video. It only ever plays in a silent scene, so it
    # never fights the narration for the same second.
    if not a.no_ko:
        import numpy as _np
        ko, missing = KO.track(v, v.duration, gain=a.ko_gain)
        if missing:
            print(f"   ⚠️  koreyscha ovoz yoʻq: {', '.join(sorted(set(missing)))}"
                  f" — avval `python3 cli.py kowords {a.slug}`")
        if ko is not None:
            print(f"koreyscha ovoz: {len(KO.events(v))} ta soʻz, "
                  f"gain {a.ko_gain:g}")
            if track is None:
                track = ko
            else:
                n = min(len(track), len(ko))
                track[:n] = track[:n] + ko[:n]
    wav = OUT / f"{a.slug}_mix.wav"
    SFX.write_wav(V.mix(v, a.audio, segs, track), wav)

    final = VIDEOS / f"{a.slug}_voiced.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out), "-i", str(wav),
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest",
                    str(final)], check=True)
    print(f"\n-> {final}  {final.stat().st_size / 1e6:.1f} MB  "
          f"video {v.duration:.2f}s / file {R.duration_of(final):.2f}s")
    return 0


def blocks_of(slug):
    """The narration blocks a recording is expected to contain, in order."""
    import re as _re
    txt = (SCRIPTS / f"{slug}_tts_one.txt").read_text(encoding="utf-8")
    parts = _re.split(r"<break time='([\d.]+)s' ?/>", txt)
    out, cur = [], parts[0]
    for i in range(1, len(parts), 2):
        if float(parts[i]) >= 1.0:
            out.append(cur)
            cur = parts[i + 1]
        else:
            cur += f"<break time='{parts[i]}s' />" + parts[i + 1]
    out.append(cur)
    return [b.strip() for b in out if b.strip()]


def cmd_check(a):
    """Dry-run the split. One second, against six minutes of rendering.

    README step 4 has always said to do this before every render, but there was
    no command for it and it got done with a throwaway script every time. It
    separates two faults that look alike in the split report and are not alike
    at all:

      * a BAD SPLIT -- the solver put a boundary in the wrong place. Time is
        CONSERVED, so a squashed segment always sits next to a stretched one.
      * MISSING TEXT -- the engine never spoke part of a block. Nothing absorbs
        the loss, so the short segment's neighbours are both fine. No re-solve
        can fix this; the recording has to be made again.

    The second kind was found on ko02 (2026-08-30): nine clean 3.4s boundaries
    for nine boundaries, every segment at 0.94-1.25x of the recording's own
    pace, and one at 0.23x with healthy neighbours. It is not one of the four
    split-model faults the solver was built against.
    """
    import re as _re
    import voice as V

    v = build.load_story(a.slug)
    blocks = blocks_of(a.slug)
    spoken = [sc for _s, _e, sc in v.bounds() if getattr(sc, "say", None)]
    print(f"{a.slug}: {len(blocks)} narration blocks / {len(spoken)} spoken "
          f"scenes / {len(v.scenes)} scenes")
    if len(blocks) != len(spoken):
        print("   BLOK SONI SAHNA SONIGA MOS EMAS - scriptni qayta yarating")
        return 1

    total = V.duration(a.audio)
    sil = V.silences(a.audio)
    body = [x for x in sil if x[1] < total - 0.35]
    longs = [x for x in body if x[2] >= 2.5]
    print(f"   yozuv {total:.1f}s, {len(body)} ichki sukut, "
          f"{len(longs)} tasi >=2.5s ({len(blocks) - 1} ta chegara kerak)")

    segs, rep = V.split(a.audio, blocks)
    print(f"   split: {rep['how']}, eng qisqa chegara {rep['shortest']:.2f}s, "
          f"eng yomon segment {rep['worst'] * 100:.0f}%")

    # When text is MISSING, the solver's own split is garbage -- it has to put
    # the boundaries somewhere, so it spreads the damage across several
    # segments and the worst one is not the guilty one. So score the naive
    # hypothesis too: the n-1 longest silences, taken at face value. If that
    # one has exactly ONE catastrophic segment and agrees everywhere else, it
    # is the true segmentation and that segment is the block the engine did not
    # speak. (Found on ko02: the solver blamed block 4; the clean hypothesis
    # showed 9 of 10 segments consistent and block 9 at 0.18x.)
    # Are the boundaries FORCED? Exactly n-1 silences at scene-break length,
    # every other pause clearly shorter. If so the solver had no choice.
    others = [x[2] for x in body if x[2] < 2.5]
    other = max(others) if others else 0.0
    forced = (len(longs) == len(blocks) - 1
              and (not others or min(x[2] for x in longs) >= 1.5 * other))

    clean = None
    if len(longs) == len(blocks) - 1:
        cuts = sorted(longs, key=lambda x: x[0])
        tail = [x for x in sil if x[1] >= total - 0.35]
        end = tail[0][0] if tail else total
        clean, prev = [], 0.0
        for c in cuts:
            clean.append((prev, c[0]))
            prev = c[1]
        clean.append((prev, end))

    # Score each segment against the recording's OWN pace, not the nominal
    # rate -- a take that ran 20% fast would otherwise flag every segment.
    weights = [max(len(_re.sub(r"<[^>]+>", "", b)), 1) for b in blocks]

    def score(ss):
        g = [e - st for st, e in ss]
        sc = sum(g) / sum(weights)
        w = [x * sc for x in weights]
        return g, w, [gi / max(wi, 0.1) for gi, wi in zip(g, w)]

    got, want, ratios = score(segs)
    if clean is not None:
        _g, _w, cr = score(clean)
        off_dp = sum(1 for r in ratios if not 0.7 <= r <= 1.4)
        off_cl = sum(1 for r in cr if not 0.7 <= r <= 1.4)
        # One catastrophic segment among otherwise-agreeing ones beats a split
        # that smears medium errors over four of them.
        if off_cl < off_dp:
            print(f"   (eng uzun {len(blocks)-1} sukut boyicha bolgani "
                  f"aniqroq: {off_cl} ta chetlashish, solver-da {off_dp} ta "
                  f"- quyida oshanisi)")
            segs, got, want, ratios = clean, _g, _w, cr

    print("")
    print(f"   {'#':>3} {'belgi':>6} {'kutilgan':>9} {'chiqdi':>8} {'nisbat':>7}   matn")
    for k, r in enumerate(ratios):
        flag = "<<<<" if not 0.7 <= r <= 1.4 else "    "
        txt = _re.sub(r"<[^>]+>", "", blocks[k]).strip()[:36]
        print(f"   {k+1:3d} {weights[k]:6d} {want[k]:8.2f}s {got[k]:7.2f}s "
              f"{r:6.2f}x {flag} {txt!r}")

    # ── the SPEECH-RATE check (added 2026-09-15, after ko07) ────────────
    #
    # Everything above scores a segment's SPAN, and a span includes the pauses
    # inside it. So a block carrying several `|` breaks can lose a whole clause
    # and still span about the right length -- which is exactly what ko07's
    # block 5 did: 0.71x on span (inside nobody's alarm) while its 181
    # characters were read in 5.89s of actual speech, 30.7 ch/s against
    # 21.6 ch/s everywhere else in the same recording.
    #
    # Subtracting the internal silences removes that confound. A TTS engine at
    # fixed settings does not read one block 40% faster than the rest of the
    # same take, so an outlier here means text was not spoken. This is the
    # measurement that caught ko07; before it, `check` printed
    # "split ishonchli" on a film with a clause missing from its central scene.
    rates, speech = [], []
    for (st, e), w in zip(segs, weights):
        quiet = sum(min(e, x[1]) - max(st, x[0]) for x in sil
                    if x[1] > st + 0.12 and x[0] < e - 0.12)
        sp = max((e - st) - max(0.0, quiet), 0.25)
        speech.append(sp)
        rates.append(w / sp)
    med = sorted(rates)[len(rates) // 2]

    # ── SCRIPT/AUDIO MISMATCH ───────────────────────────────────────────
    # The engine can only DROP text, never add it. So a block whose audio holds
    # much MORE speech than the script accounts for is not an engine fault --
    # the script was edited after the take. Across every matched recording
    # measured here the slowest block is 0.88x; below 0.75x is outside anything
    # a real take produces.
    #
    # This cost a round trip on 2026-09-15: mo25/mo31 were shortened AFTER
    # recording, and `check` dutifully reported three blocks as "OVOZDA MATN
    # YOQ" when the take was simply the older, longer script. The whole report
    # is meaningless in that state, so it stops here.
    # The SPREAD is the discriminating statistic, and it is scale-free -- an
    # absolute floor fails because several mismatched blocks drag the median
    # down with them (mo25's slowest landed at exactly 0.75x and slipped past).
    # Measured across 13 takes: 11 matched ones span 1.07-1.37; the two whose
    # scripts were edited after recording span 2.29 and 2.92.
    rel = [r / med for r in rates]
    spread = max(rel) / max(min(rel), 1e-6)
    slow = [k for k, r in enumerate(rates) if r < med * 0.75]
    if spread > 1.7 or slow:
        print("")
        print(f"   ⛔ SCRIPT VA OVOZ MOS EMAS — tezlik tarqoqligi "
              f"{spread:.2f}x (mos yozuvlarda eng koʻpi 1.37x):")
        for k in sorted(range(len(rates)), key=lambda i: rates[i])[:3]:
            print(f"       {k+1}-blok {rates[k]/med:.2f}x sekin "
                  f"({rates[k]:.1f} belgi/s, oʻrtacha {med:.1f})")
        print(f"   Engine matn QOʻSHMAYDI — faqat tashlab ketadi. Demak bu "
              f"yozuv boshqa (uzunroq) script versiyasidan olingan.")
        print(f"   Scriptni tahrirlagandan keyin QAYTA yozdirish kerak.")
        return 1

    # 1.15, not 1.25. Calibrated twice: 25 blocks across the known-good takes
    # (ko04/05/06) span only 0.89-1.05x, while ko07 take 2 dropped a 30-char
    # clause out of a 143-char block and came in at 1.20x -- under the original
    # 1.25 and therefore missed. A 17% drop from a short block is the smallest
    # thing worth catching, so the threshold sits just above the observed noise
    # floor rather than halfway to the first disaster.
    fast = [k for k, r in enumerate(rates) if r > med * 1.15]

    print("")
    print(f"   soʻzlash tezligi (sukutlar ayirilgan) — oʻrtacha "
          f"{med:.1f} belgi/s")
    for k, r in enumerate(rates):
        flag = "<<<<" if k in fast else "    "
        print(f"   {k+1:3d} {speech[k]:7.2f}s soʻzlash {r:7.1f} belgi/s "
              f"{r/med:5.2f}x {flag}")

    bad = [k for k, r in enumerate(ratios) if r < 0.7 or r > 1.4]
    if fast:
        for k in fast:
            head = _re.sub(r"<[^>]+>", "", blocks[k]).strip()[:70]
            miss = weights[k] - speech[k] * med
            print("")
            print(f"   OVOZDA MATN YOQ - {k+1}-blok {rates[k]/med:.2f}x tez "
                  f"oʻqilgan ({rates[k]:.1f} belgi/s, oʻrtacha {med:.1f}).")
            print(f"   Taxminan {miss:.0f} belgi aytilmagan. Engine matnning "
                  f"bir qismini tashlab ketgan — split aybdor emas.")
            print(f"   Blokni QAYTA TUZING (ichki `||` ni olib tashlang va "
                  f"qisqartiring), keyin qayta yozdiring.")
            print(f"   Tinglang: ...{head}...")
        return 1

    if not bad:
        print("")
        print("   => split ishonchli, render qilsa boladi")
        return 0

    for k in bad:
        near = [ratios[j] for j in (k - 1, k + 1) if 0 <= j < len(ratios)]
        head = _re.sub(r"<[^>]+>", "", blocks[k]).strip()[:70]
        print("")
        if ratios[k] < 0.7 and all(0.8 <= x <= 1.25 for x in near):
            print(f"   OVOZDA MATN YOQ - {k+1}-blok {ratios[k]:.2f}x, "
                  f"qoshnilari joyida.")
            print(f"   Vaqt qoshniga kochmagan, demak split aybdor emas: "
                  f"bu blokni engine aytmagan.")
            print(f"   Tinglang: ...{head}...")
        else:
            print(f"   SHUBHALI CHEGARA - {k+1}-blok {ratios[k]:.2f}x, "
                  f"qoshnilari {['%.2f' % x for x in near]}.")
            if forced:
                # Worked out by hand twice (ko06 block 5, ko11 blocks 3-4)
                # before this said it. When there are exactly n-1 silences at
                # scene-break length and every other pause is far shorter, the
                # solver had NO choice -- so a misplaced boundary is
                # arithmetically impossible and the span ratio is a model
                # artefact: the block simply holds more or less internal
                # silence than per-character time predicts.
                print(f"   ⓘ  Lekin chegaralar MAJBURIY: {len(longs)} ta "
                      f"sahna-sukut, {len(blocks)-1} ta chegara kerak, "
                      f"qolgan eng uzun pauza {other:.2f}s.")
                print(f"   Demak chegara notoʻgʻri boʻlishi MUMKIN EMAS. "
                      f"Soʻzlash tezligi toza boʻlsa — render qilsa boʻladi.")
            else:
                print(f"   Vaqt qoshniga kochgan bolishi mumkin: "
                      f"chegara notogri.")
    return 1


def cmd_kowords(a):
    """Fetch the native Korean clips this video needs. The only online step.

    They are committed under assets/ko_words/ for the same reason the fonts
    are vendored: a render must never depend on the network.
    """
    import koaudio as KO
    a.voice = a.voice or KO.VOICE
    a.rate = a.rate or KO.RATE
    v = build.load_story(a.slug)
    need = KO.words(v)
    if not need:
        print(f"{a.slug}: koreyscha ovoz talab qiladigan sahna yoʻq "
              f"(`scenes.echo` ishlating).")
        return 0
    have = [w for w in need if KO.clip_path(w, a.voice, a.rate).exists()]
    print(f"{a.slug}: {len(need)} ta soʻz, {len(have)} tasi allaqachon bor")
    made, missing = KO.generate(need, voice=a.voice, rate=a.rate, force=a.force)
    for text, path in made:
        print(f"  + {text}  →  assets/ko_words/{path.name}")
    if missing:
        print(f"  ⚠️  olinmadi: {', '.join(missing)}")
        return 1
    return 0


def cmd_draft(a):
    import draft
    print(draft.draft(int(a.order)))
    return 0


SCRUB = """
const bar = document.createElement('input');
bar.type = 'range'; bar.min = 0; bar.max = VIDEO.duration; bar.step = 0.05; bar.value = 0;
bar.style.cssText = 'position:fixed;left:20px;right:20px;bottom:16px;z-index:999';
const tag = document.createElement('div');
tag.style.cssText = 'position:fixed;left:20px;bottom:52px;z-index:999;font:700 22px Mulish,sans-serif;background:#1a1410;color:#faf7f2;padding:6px 14px;border-radius:9px';
document.body.append(bar, tag);
function draw(){ const t = +bar.value; seek(t);
  const s = VIDEO.scenes.find(s => t >= s.start && t < s.end) || {name:'-'};
  tag.textContent = t.toFixed(2) + 's  ' + s.name; }
bar.addEventListener('input', draw);
addEventListener('keydown', e => {
  const d = e.shiftKey ? 1 : 1/30;
  if (e.key === 'ArrowRight') { bar.value = +bar.value + d; draw(); }
  if (e.key === 'ArrowLeft')  { bar.value = +bar.value - d; draw(); }
});
draw();
"""


def main():
    ap = argparse.ArgumentParser(prog="storyvideo")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lint");    p.add_argument("slug"); p.set_defaults(fn=cmd_lint)
    p.add_argument("--fast", action="store_true", help="skip the browser layout pass")

    p = sub.add_parser("sheet");   p.add_argument("slug"); p.set_defaults(fn=cmd_sheet)
    p.add_argument("--every", type=float, default=4.0)
    p.add_argument("--cols", type=int, default=6)
    p.add_argument("--per-scene", action="store_true", default=True)
    p.add_argument("--guides", action="store_true")

    p = sub.add_parser("preview"); p.add_argument("slug"); p.set_defaults(fn=cmd_preview)

    p = sub.add_parser("render");  p.add_argument("slug"); p.set_defaults(fn=cmd_render)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--skip-lint", action="store_true")

    p = sub.add_parser("voice");   p.add_argument("slug"); p.set_defaults(fn=cmd_voice)
    p.add_argument("--audio", required=True)
    p.add_argument("--script", required=True)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--workers", type=int, default=3)
    p.add_argument("--no-sfx", action="store_true")
    p.add_argument("--sfx-gain", type=float, default=1.5,
                   help="ovoz effektlari balandligi (1.0 = sfx.py dagi daraja)")
    p.add_argument("--no-ko", action="store_true",
                   help="koreyscha soʻz ovozlarini qoʻshmaslik")
    p.add_argument("--ko-gain", type=float, default=0.95,
                   help="koreyscha soʻz ovozi balandligi")

    p = sub.add_parser("check");   p.add_argument("slug"); p.set_defaults(fn=cmd_check)
    p.add_argument("--audio", required=True)

    p = sub.add_parser("kowords"); p.add_argument("slug"); p.set_defaults(fn=cmd_kowords)
    p.add_argument("--voice", default=None)
    p.add_argument("--rate", default=None)
    p.add_argument("--force", action="store_true")

    p = sub.add_parser("script");  p.add_argument("slug"); p.set_defaults(fn=cmd_script)
    p.add_argument("--one", action="store_true",
                   help="one continuous paste instead of per-scene blocks")
    p.add_argument("--ssml", action="store_true",
                   help="use <break> and <emphasis> tags (ttsfree supports them)")
    p = sub.add_parser("draft");   p.add_argument("order"); p.set_defaults(fn=cmd_draft)

    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
