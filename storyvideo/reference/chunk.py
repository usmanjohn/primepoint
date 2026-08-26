import subprocess, sys, time
from draw import finish, W, H
import scenes

FPS = 24
i0, i1, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]

bounds, acc = [], 0.0
for fn, dur in scenes.TIMELINE:
    bounds.append((acc, acc + dur, fn, dur))
    acc += dur
TOTAL = int(acc * FPS)
i1 = min(i1, TOTAL)

ff = subprocess.Popen([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
    "-i", "-", "-an", "-c:v", "libx264", "-preset", "fast", "-crf", "19",
    "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)

t0 = time.time()
for i in range(i0, i1):
    t = i / FPS
    for a, b, fn, dur in bounds:
        if a <= t < b:
            img = fn(t - a, dur)
            break
    else:
        img = bounds[-1][2](bounds[-1][3] - 1e-4, bounds[-1][3])
    ff.stdin.write(finish(img).tobytes())
ff.stdin.close(); ff.wait()
print(f"chunk {i0}-{i1} -> {out}  {time.time()-t0:.0f}s (total {TOTAL})")