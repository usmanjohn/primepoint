# -*- coding: utf-8 -*-
"""Frames out of Chrome, video out of ffmpeg.

Because seek(t) is a pure function of time, workers need no coordination: each
one opens its own Chrome on the same stage file, jumps to its own slice of the
timeline and encodes it. Six of them turn a ~90s video around in well under a
minute on this machine (a single process manages ~13 fps at 1080x1920).

This Mac has ffmpeg but NO ffprobe, so durations are read by parsing the last
"time=" out of `ffmpeg -i FILE -f null -`.
"""

import multiprocessing as mp
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
W, H = 1080, 1920
FPS = 30
SETTLE_MS = 2200          # let the vendored fonts land before the first shot


def _page(pw, url):
    b = pw.chromium.launch(channel="chrome", args=["--force-color-profile=srgb",
                                                   "--disable-lcd-text"])
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    pg.goto(url)
    pg.wait_for_function("document.fonts.status === 'loaded'", timeout=20000)
    pg.wait_for_timeout(SETTLE_MS)
    return b, pg


def shoot(stage, times, outdir, guides=False):
    """Screenshot a stage at the given times. The eyeball loop."""
    from playwright.sync_api import sync_playwright
    outdir = pathlib.Path(outdir); outdir.mkdir(parents=True, exist_ok=True)
    paths = []
    with sync_playwright() as pw:
        b, pg = _page(pw, pathlib.Path(stage).resolve().as_uri())
        if guides:
            pg.evaluate("document.body.classList.add('guides')")
        for t in times:
            pg.evaluate(f"seek({t})")
            p = outdir / f"t{t:07.2f}.png"
            pg.screenshot(path=str(p), timeout=120000, animations="disabled")
            paths.append(p)
        b.close()
    return paths


def _chunk(args):
    """One worker: frames [i0, i1) straight into its own mp4."""
    stage, i0, i1, fps, out = args
    from playwright.sync_api import sync_playwright
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-c:v", "png",
         "-r", str(fps), "-i", "-", "-an", "-c:v", "libx264", "-preset", "medium",
         "-crf", "18", "-pix_fmt", "yuv420p", out],
        stdin=subprocess.PIPE)
    with sync_playwright() as pw:
        b, pg = _page(pw, pathlib.Path(stage).resolve().as_uri())
        for i in range(i0, i1):
            pg.evaluate(f"seek({i / fps})")
            # Six concurrent Chromes at 1080x1920 will blow the 30s default.
            ff.stdin.write(pg.screenshot(type="png", timeout=120000,
                                         animations="disabled"))
        b.close()
    ff.stdin.close()
    ff.wait()
    return i1 - i0


def render(video, stage, out=None, fps=FPS, workers=4):
    total = int(round(video.duration * fps))
    out = pathlib.Path(out or HERE / "out" / f"{video.slug}.mp4")
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="storyvideo_"))

    edges = [round(total * k / workers) for k in range(workers + 1)]
    jobs = [(str(stage), edges[k], edges[k + 1], fps, str(tmp / f"c{k:02d}.mp4"))
            for k in range(workers) if edges[k + 1] > edges[k]]

    print(f"  {total} frames @ {fps}fps across {len(jobs)} workers", flush=True)
    with mp.Pool(len(jobs)) as pool:
        for n in pool.imap_unordered(_chunk, jobs):
            print(f"  ... {n} frames done", flush=True)

    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{j[4]}'\n" for j in jobs))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(out)], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    return out


def duration_of(path):
    """No ffprobe on this machine -- parse the last time= ffmpeg prints."""
    r = subprocess.run(["ffmpeg", "-i", str(path), "-f", "null", "-"],
                       capture_output=True, text=True)
    hits = re.findall(r"time=(\d+):(\d+):(\d+\.\d+)", r.stderr)
    if not hits:
        return None
    h, m, s = hits[-1]
    return int(h) * 3600 + int(m) * 60 + float(s)


def contact_sheet(frames, out, cols=6, tile_w=300):
    """Tile stills into one PNG -- the fastest way to judge a whole video."""
    out = pathlib.Path(out)
    d = pathlib.Path(frames[0]).parent
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-pattern_type", "glob",
         "-i", str(d / "*.png"),
         "-vf", f"scale={tile_w}:-1,tile={cols}x{-(-len(frames)//cols)}"
                ":margin=6:padding=5:color=0x333333",
         "-frames:v", "1", str(out)], check=True)
    return out


def sheet_from_video(path, out, every=4, cols=6, tile_w=300):
    """Contact sheet taken from the ENCODED mp4, not the stage -- this is what
    catches anything the encoder itself breaks."""
    out = pathlib.Path(out)
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", str(path),
         "-vf", f"fps=1/{every},scale={tile_w}:-1,tile={cols}x6:margin=6:padding=5:color=0x333333",
         "-frames:v", "1", str(out)], check=True)
    return out
