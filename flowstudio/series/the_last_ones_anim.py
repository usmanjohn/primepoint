"""«Thinking» animation for The Last Ones 2-qism: the bridge plan drawn as a chalk blueprint.
    PYTHONPATH=../pylib python3 anim.py tagor|sarang PREV_LAST.png NEXT_FIRST.png OUT.mp4
Frames are drawn with Pillow and piped to ffmpeg; the sound is synthesised here (stdlib only)."""
import math
import os
import random
import struct
import subprocess
import sys
import wave

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

HERE = os.environ.get("TLO_DIR", os.path.dirname(os.path.abspath(__file__)))   # holds faces/1.jpg … 8.jpg
W, H, FPS = 1080, 1920, 30
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
F = lambda s: ImageFont.truetype(BOLD, s)

T = {'Anna': 1, 'Wei Yi': 2, 'Charli': 3, 'Tagor': 4, 'Sarang': 5, 'Jordan': 7, 'Qodir': 8, 'Maksim': 10}
FILE = {'Qodir': 1, 'Sarang': 2, 'Anna': 3, 'Jordan': 4, 'Charli': 5, 'Tagor': 6, 'Wei Yi': 7, 'Maksim': 8}
# face centre and radius inside the close-up panel (right third) of each 3072×5504 picture, in panel px /6.4
FACE = {'Qodir': (80, 380, 100), 'Sarang': (80, 375, 92), 'Anna': (95, 375, 95), 'Jordan': (80, 420, 102),
        'Charli': (85, 345, 108), 'Tagor': (80, 372, 108), 'Wei Yi': (80, 390, 104), 'Maksim': (80, 420, 106)}

BG = (11, 24, 40)
CHALK = (226, 236, 245)
DIM = (120, 150, 180)
GOLD = (255, 190, 90)
RED = (235, 72, 64)
GREEN = (96, 214, 140)
LIMIT, SCALE_MAX = 38, 45


def face(name, d):
    cx, cy, r = FACE[name]
    X, Y, R = 2048 + cx * 6.4, cy * 6.4, r * 6.4
    im = Image.open(os.path.join(HERE, 'faces', f'{FILE[name]}.jpg')).crop((int(X - R), int(Y - R), int(X + R), int(Y + R)))
    im = im.resize((d, d), Image.LANCZOS).convert('RGBA')
    mask = Image.new('L', (d * 4, d * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d * 4 - 1, d * 4 - 1), fill=255)
    im.putalpha(mask.resize((d, d), Image.LANCZOS))
    return im


# ── the plans ──
def tagor_plan():
    trips, fast = [], 'Anna'
    rest = ['Wei Yi', 'Charli', 'Tagor', 'Sarang', 'Jordan', 'Qodir', 'Maksim']
    for k, p in enumerate(rest):
        trips.append(((fast, p), '>'))
        if k < len(rest) - 1:
            trips.append(((fast,), '<'))
    return trips


def sarang_plan():
    A, B = 'Anna', 'Wei Yi'
    return [((A, B), '>'), ((A,), '<'), (('Sarang', 'Jordan'), '>'), ((B,), '<'),
            ((A, B), '>'), ((A,), '<'), (('Qodir', 'Maksim'), '>'), ((B,), '<'),
            ((A, B), '>'), ((A,), '<'), ((A, 'Charli'), '>'), ((A,), '<'), ((A, 'Tagor'), '>')]


CFG = {
    'tagor': dict(plan=tagor_plan(), who='Tagor', title='TAGORNING HISOBI', spm=0.15, end_hold=1.5),
    'sarang': dict(plan=sarang_plan(), who='Sarang', title='SARANGNING HISOBI', spm=0.19, end_hold=1.8),
}

# ── layout ──
D = 104                      # face diameter
CL, CR = 250, 830            # cliff edges
BY = 1060                    # bridge height at the cliffs
SAG = 46
LEFT = [(78, 1190), (190, 1190), (78, 1330), (190, 1330), (78, 1470), (190, 1470), (78, 1610), (190, 1610)]
RIGHT = [(890, 1190), (1002, 1190), (890, 1330), (1002, 1330), (890, 1470), (1002, 1470), (890, 1610), (1002, 1610)]
ORDER = sorted(T, key=T.get)


def bridge_y(x):
    u = (x - CL) / (CR - CL)
    return BY + SAG * 4 * u * (1 - u)


def ease(u):
    return u * u * (3 - 2 * u)


def timeline(cfg):
    """[(t0, t1, people, dir, m0, m1)] in animation seconds; m = elapsed minutes."""
    out, t, m = [], 0.0, 0
    for people, d in cfg['plan']:
        mins = max(T[p] for p in people)
        dur = max(mins * cfg['spm'], 0.36)
        out.append((t, t + dur, people, d, m, m + mins))
        t += dur + 0.06
        m += mins
    return out, t


def blueprint():
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, W, 60):
        d.line((x, 0, x, H), fill=(18, 36, 58))
    for y in range(0, H, 60):
        d.line((0, y, W, y), fill=(18, 36, 58))
    d.rectangle((CL, BY + 10, CR, H), fill=(6, 14, 26))
    # cliffs
    rnd = random.Random(4)
    for side in (0, 1):
        pts = [(0 if side == 0 else W, H), (0 if side == 0 else W, BY + 10)]
        edge = CL if side == 0 else CR
        pts += [(edge, BY + 10)]
        y = BY + 10
        while y < H:
            y += rnd.randint(70, 130)
            pts.append((edge + (rnd.randint(-40, 10) if side == 0 else rnd.randint(-10, 40)), y))
        pts.append((edge, H))
        d.polygon(pts, fill=(26, 50, 80))
        d.line(pts[2:], fill=DIM, width=4)
        d.line((0 if side == 0 else edge, BY + 10, edge if side == 0 else W, BY + 10), fill=CHALK, width=5)
    # mist in the gorge
    for k in range(9):
        y = 1250 + k * 70
        d.line((CL + 30, y, CR - 30, y + rnd.randint(-8, 8)), fill=(30, 52, 78), width=3)
    return im


def draw_bridge(d, broken=0.0, colour=CHALK):
    pts = [(x, bridge_y(x)) for x in range(CL, CR + 1, 10)]
    for k in range(len(pts) - 1):
        if broken and random.Random(k).random() < broken:
            continue
        d.line((pts[k], pts[k + 1]), fill=colour, width=5)
    for x in range(CL + 20, CR, 34):
        if broken and random.Random(x).random() < broken:
            continue
        y = bridge_y(x)
        d.line((x, y - 12, x, y + 12), fill=colour, width=4)
    for x in (CL, CR):
        d.line((x, BY - 70, x, BY + 6), fill=colour, width=6)
    d.line(((CL, BY - 70), *[(x, bridge_y(x) - 70) for x in range(CL, CR + 1, 20)], (CR, BY - 70)), fill=DIM, width=3)


def glow(base, xy, r, colour, alpha):
    layer = Image.new('RGBA', (r * 6, r * 6), (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse((r * 2, r * 2, r * 4, r * 4), fill=(*colour, int(255 * alpha)))
    layer = layer.filter(ImageFilter.GaussianBlur(r * 0.9))
    base.alpha_composite(layer, (int(xy[0] - r * 3), int(xy[1] - r * 3)))


def badge(d, x, y, n, colour=GOLD):
    d.ellipse((x - 24, y - 24, x + 24, y + 24), fill=BG, outline=colour, width=4)
    d.text((x, y + 1), str(n), font=F(28), fill=colour, anchor='mm')


def render(name, prev_png, next_png, out):
    cfg = CFG[name]
    trips, run_t = timeline(cfg)
    INTRO, OUTRO = 1.1, 0.7
    total = INTRO + 0.25 + run_t + cfg['end_hold'] + OUTRO
    faces = {p: face(p, D) for p in T}
    big = face(cfg['who'], 132)
    base = blueprint()

    def tint(png):
        im = Image.open(png).convert('RGB').resize((W, H))
        im = ImageEnhance.Color(im).enhance(0.15)
        im = ImageEnhance.Brightness(im).enhance(0.55)
        return Image.blend(im, Image.new('RGB', (W, H), (20, 50, 90)), 0.35)
    prev_real = Image.open(prev_png).convert('RGB').resize((W, H))
    prev_t, next_t = tint(prev_png), tint(next_png)

    events = []          # (time, kind) for the sound
    for t0, t1, people, d, m0, m1 in trips:
        for m in range(m0 + 1, m1 + 1):
            events.append((INTRO + 0.25 + t0 + (t1 - t0) * (m - m0) / (m1 - m0), 'tick'))
    over_t = None
    if name == 'tagor':
        for t0, t1, people, d, m0, m1 in trips:
            if m0 < LIMIT <= m1:
                over_t = INTRO + 0.25 + t0 + (t1 - t0) * (LIMIT - m0) / (m1 - m0)
        events.append((over_t, 'boom'))
    events.append((0.0, 'whoosh'))
    end_t = INTRO + 0.25 + run_t
    events.append((end_t, 'boom' if name == 'tagor' else 'chime'))

    ff = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                           '-r', str(FPS), '-i', '-', '-i', out + '.wav', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                           '-preset', 'medium', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', '-shortest', out],
                          stdin=subprocess.PIPE)
    write_sound(out + '.wav', total, events)

    nframes = int(round(total * FPS))
    for fi in range(nframes):
        t = fi / FPS
        a = t - INTRO - 0.25                     # animation clock
        a_clock = a
        if over_t is not None:
            a = min(a, over_t - INTRO - 0.25)
        # where is everyone at time a?
        side = {p: 'L' for p in T}
        moving, minutes, lantern_side = {}, 0, 'L'
        for t0, t1, people, d, m0, m1 in trips:
            if a >= t1:
                for p in people:
                    side[p] = 'R' if d == '>' else 'L'
                minutes, lantern_side = m1, ('R' if d == '>' else 'L')
            elif a >= t0:
                u = ease((a - t0) / (t1 - t0))
                for k, p in enumerate(people):
                    moving[p] = (u if d == '>' else 1 - u, k, len(people))
                minutes = m0 + (m1 - m0) * (a - t0) / (t1 - t0)
                lantern_side = None
                active = (people, m1 - m0, d, u)
                break
        else:
            active = None
        if over_t is not None and a_clock > a:          # after the break only the clock moves
            for t0, t1, people, d, m0, m1 in trips:
                if t0 <= a_clock < t1:
                    minutes = m0 + (m1 - m0) * (a_clock - t0) / (t1 - t0)
                elif a_clock >= t1:
                    minutes = m1
        if a_clock < 0:
            minutes = 0

        frame = base.copy().convert('RGBA')
        dr = ImageDraw.Draw(frame)
        over = name == 'tagor' and minutes >= LIMIT
        done = a_clock >= run_t
        broken = min(1, max(0, (t - over_t) / 0.6)) * 0.45 if over else 0
        draw_bridge(dr, broken, RED if over else CHALK)

        # header
        frame.alpha_composite(big, (90, 120))
        dr.ellipse((88, 118, 90 + 134, 120 + 134), outline=CHALK, width=4)
        dr.text((250, 186), cfg['title'], font=F(56), fill=CHALK, anchor='lm')
        # clock
        col = RED if over else (GREEN if (done and name == 'sarang') else CHALK)
        dr.text((W // 2, 420), f"{int(minutes):02d}:00", font=F(170), fill=col, anchor='mm')
        dr.text((W // 2, 545), "daqiqa", font=F(44), fill=DIM, anchor='mm')
        # timeline bar
        x0, x1, yb = 90, 990, 650
        dr.rounded_rectangle((x0, yb - 16, x1, yb + 16), 16, outline=DIM, width=4)
        fx = x0 + (x1 - x0) * min(minutes, SCALE_MAX) / SCALE_MAX
        if fx > x0 + 8:
            dr.rounded_rectangle((x0 + 6, yb - 10, fx, yb + 10), 10, fill=col)
        lx = x0 + (x1 - x0) * LIMIT / SCALE_MAX
        dr.line((lx, yb - 40, lx, yb + 40), fill=RED, width=6)
        dr.text((lx, yb + 72), "38", font=F(46), fill=RED, anchor='mm')

        # people standing on the cliffs
        li = [p for p in ORDER if side[p] == 'L' and p not in moving]
        ri = [p for p in arrival_order(trips, a) if side[p] == 'R' and p not in moving]
        lost = name == 'tagor' and over
        for slots, ppl in ((LEFT, li), (RIGHT, ri)):
            for (x, y), p in zip(slots, ppl):
                im = faces[p]
                frame.alpha_composite(im, (x - D // 2, y - D // 2))
                dr.ellipse((x - D // 2 - 2, y - D // 2 - 2, x + D // 2 + 2, y + D // 2 + 2), outline=DIM, width=3)
                badge(dr, x + 40, y + 40, T[p])
        # lantern resting on a cliff
        if lantern_side and not lost:
            lx_, ly_ = (CL - 30, BY - 40) if lantern_side == 'L' else (CR + 30, BY - 40)
            glow(frame, (lx_, ly_), 26, GOLD, 0.9)
            dr.ellipse((lx_ - 12, ly_ - 12, lx_ + 12, ly_ + 12), fill=GOLD)
        # people on the bridge
        for p, (u, k, n) in moving.items():
            x = CL + 40 + (CR - CL - 80) * u + (k - (n - 1) / 2) * 112
            y = bridge_y(min(max(x, CL), CR)) - 72
            if k == 0 and not lost:
                glow(frame, (x, y), 60, GOLD, 0.55)
            im = faces[p]
            if lost:
                im = ImageEnhance.Color(im).enhance(0).copy()
                im.putalpha(faces[p].getchannel('A').point(lambda v: v * 0.6))
            frame.alpha_composite(im, (int(x - D // 2), int(y - D // 2)))
            dr = ImageDraw.Draw(frame)
            dr.ellipse((x - D // 2 - 3, y - D // 2 - 3, x + D // 2 + 3, y + D // 2 + 3), outline=RED if lost else GOLD, width=5)
            badge(dr, x + 40, y + 40, T[p])
        if active and active[0] and not lost:
            people, mins, d, u = active
            mx = CL + (CR - CL) / 2
            a_lbl = min(1, u * 4, (1 - u) * 4)
            if a_lbl > 0:
                txt = f"+{mins}"
                colr = tuple(int(BG[i] + (GOLD[i] - BG[i]) * a_lbl) for i in range(3))
                dr.text((mx, BY - 200), txt, font=F(80), fill=colr, anchor='mm')
                if len(people) == 2 and T[people[0]] != T[people[1]] and min(T[q] for q in people) >= 3:
                    sub = f"{min(T[q] for q in people)} + {max(T[q] for q in people)} → {max(T[q] for q in people)}"
                    dr.text((mx, BY - 140), sub, font=F(40), fill=colr, anchor='mm')

        # result card
        if done:
            k = min(1, (a_clock - run_t) / 0.35)
            if name == 'tagor':
                msg, sub, c = "45 > 38", "kimdir qolishi kerak", RED
            else:
                msg, sub, c = "38 = 38", "hech kim qolmaydi", GREEN
            colr = tuple(int(BG[i] + (c[i] - BG[i]) * k) for i in range(3))
            dr.rounded_rectangle((150, 1730, 930, 1880), 30, fill=BG, outline=colr, width=5)
            dr.text((W // 2, 1782), msg, font=F(72), fill=colr, anchor='mm')
            dr.text((W // 2, 1848), sub, font=F(40), fill=colr, anchor='mm')

        img = frame.convert('RGB')
        # transitions: real frame → cold frozen frame → chalk diagram; diagram → cold next frame
        if t < INTRO:
            if t < 0.45:
                img = Image.blend(prev_real, prev_t, t / 0.45)
            else:
                k = (t - 0.45) / (INTRO - 0.45)
                img = Image.blend(prev_t, img, ease(k))
        elif t > total - OUTRO:
            k = (t - (total - OUTRO)) / OUTRO
            img = Image.blend(img, next_t, ease(k))
        ff.stdin.write(img.tobytes())
    ff.stdin.close()
    ff.wait()
    os.remove(out + '.wav')
    print(out, f'{total:.2f} s')


def arrival_order(trips, a):
    order = []
    for t0, t1, people, d, m0, m1 in trips:
        if a < t1:
            break
        for p in people:
            if p in order:
                order.remove(p)
            if d == '>':
                order.append(p)
    return order


def write_sound(path, total, events):
    sr = 48000
    n = int(total * sr) + sr
    buf = [0.0] * n
    rnd = random.Random(7)
    for i in range(n):                                   # low drone
        t = i / sr
        buf[i] += 0.05 * math.sin(2 * math.pi * 55 * t) + 0.025 * math.sin(2 * math.pi * 82.5 * t + 1)
    for at, kind in events:
        s = int(at * sr)
        if kind == 'tick':
            for i in range(int(0.03 * sr)):
                if s + i < n:
                    buf[s + i] += 0.18 * math.sin(2 * math.pi * 1900 * i / sr) * math.exp(-i / (0.006 * sr))
        elif kind == 'whoosh':
            prev = 0.0
            L = int(0.9 * sr)
            for i in range(L):
                u = i / L
                prev = prev + (0.05 + 0.4 * u) * (rnd.uniform(-1, 1) - prev)
                buf[i] += 0.5 * prev * math.sin(math.pi * u)
        elif kind == 'boom':
            for i in range(int(1.4 * sr)):
                if s + i < n:
                    buf[s + i] += 0.5 * math.sin(2 * math.pi * (58 - 18 * i / sr) * i / sr) * math.exp(-i / (0.35 * sr))
        elif kind == 'chime':
            for i in range(int(2.0 * sr)):
                if s + i < n:
                    e = math.exp(-i / (0.6 * sr))
                    buf[s + i] += 0.16 * e * (math.sin(2 * math.pi * 880 * i / sr) + 0.6 * math.sin(2 * math.pi * 1320 * i / sr))
    for i in range(min(int(0.3 * sr), n)):              # fades
        buf[i] *= i / (0.3 * sr)
        buf[n - 1 - i] *= i / (0.3 * sr)
    with wave.open(path, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(b''.join(struct.pack('<hh', v, v) for v in (int(max(-1, min(1, x)) * 32000) for x in buf)))


if __name__ == '__main__':
    render(*sys.argv[1:5])
