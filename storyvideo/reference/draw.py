from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1080, 1920
SS = 2                      # supersample factor
FPS = 30

CREAM   = (247, 240, 227)
INK     = (28, 33, 48)
GOLD    = (233, 176, 46)
GOLD_D  = (191, 137, 22)
RED     = (214, 79, 62)
GREEN   = (74, 155, 110)
WOOD    = (198, 160, 116)
WOOD_D  = (168, 130, 88)
GREY    = (150, 150, 160)
WHITE   = (255, 255, 255)

KID_COLORS = [
    (91, 143, 199), (224, 122, 95), (129, 178, 154), (242, 204, 143),
    (176, 137, 190), (231, 149, 179), (108, 176, 190), (212, 163, 115),
]
SKIN = [(245, 208, 175), (231, 186, 145), (212, 160, 120), (196, 141, 100)]

FDIR = "/usr/share/fonts/truetype/dejavu/"
_cache = {}
def font(size, bold=True, serif=False):
    key = (size, bold, serif)
    if key not in _cache:
        name = ("DejaVuSerif" if serif else "DejaVuSans") + ("-Bold" if bold else "")
        _cache[key] = ImageFont.truetype(FDIR + name + ".ttf", int(size * SS))
    return _cache[key]

def new_frame(bg=CREAM):
    img = Image.new("RGB", (W * SS, H * SS), bg)
    return img, ImageDraw.Draw(img, "RGBA")

def finish(img):
    return img.resize((W, H), Image.LANCZOS)

def s(v):
    return int(round(v * SS))

# ---------- easing ----------
def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))

def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)

def ease_out(x):
    x = clamp(x)
    return 1 - (1 - x) ** 3

def pop(x):
    """overshoot 0->1"""
    x = clamp(x)
    return 1 + 2.2 * (x - 1) ** 3 + 1.2 * (x - 1) ** 2 if x < 1 else 1

# ---------- primitives ----------
def rrect(d, box, r, fill, outline=None, wid=3):
    x0, y0, x1, y1 = [s(v) for v in box]
    d.rounded_rectangle([x0, y0, x1, y1], radius=s(r), fill=fill,
                        outline=outline, width=s(wid) if outline else 0)

def circ(d, cx, cy, r, fill, outline=None, wid=3):
    d.ellipse([s(cx - r), s(cy - r), s(cx + r), s(cy + r)], fill=fill,
              outline=outline, width=s(wid) if outline else 0)

def ell(d, cx, cy, rx, ry, fill, outline=None, wid=3):
    d.ellipse([s(cx - rx), s(cy - ry), s(cx + rx), s(cy + ry)], fill=fill,
              outline=outline, width=s(wid) if outline else 0)

def line(d, p0, p1, fill, wid=4):
    d.line([s(p0[0]), s(p0[1]), s(p1[0]), s(p1[1])], fill=fill, width=s(wid))

def text(d, xy, txt, size, fill=INK, anchor="mm", bold=True, serif=False):
    d.text((s(xy[0]), s(xy[1])), txt, font=font(size, bold, serif),
           fill=fill, anchor=anchor)

def text_w(txt, size, bold=True, serif=False):
    f = font(size, bold, serif)
    return f.getbbox(txt)[2] / SS

def wrap(d, xy, txt, size, maxw, fill=INK, lh=1.35, bold=True, serif=False, anchor="ma"):
    words = txt.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if text_w(t, size, bold, serif) > maxw and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    x, y = xy
    for i, ln in enumerate(lines):
        text(d, (x, y + i * size * lh), ln, size, fill, anchor, bold, serif)
    return len(lines) * size * lh


# ---------- characters ----------
def kid(d, cx, cy, sc, ci, si=0, standing=False, sad=False, arms_up=False, alpha=255):
    """Flat kid: head + rounded body. cy = top of head."""
    body = KID_COLORS[ci % len(KID_COLORS)]
    skin = SKIN[si % len(SKIN)]
    if alpha < 255:
        body = body + (alpha,)
        skin = skin + (alpha,)
    hr = 16 * sc
    hx, hy = cx, cy + hr
    # body
    bw, bh = 26 * sc, 34 * sc
    rrect(d, [cx - bw / 2, hy + hr * 0.75, cx + bw / 2, hy + hr * 0.75 + bh], 11 * sc, body)
    # arms
    aw = 7 * sc
    ay = hy + hr * 0.75 + 6 * sc
    if arms_up:
        rrect(d, [cx - bw / 2 - aw, ay - 14 * sc, cx - bw / 2 + 1, ay + 6 * sc], aw / 2, body)
        rrect(d, [cx + bw / 2 - 1, ay - 14 * sc, cx + bw / 2 + aw, ay + 6 * sc], aw / 2, body)
    else:
        rrect(d, [cx - bw / 2 - aw, ay, cx - bw / 2 + 1, ay + 20 * sc], aw / 2, body)
        rrect(d, [cx + bw / 2 - 1, ay, cx + bw / 2 + aw, ay + 20 * sc], aw / 2, body)
    # legs (only when standing)
    if standing:
        ly = hy + hr * 0.75 + bh
        rrect(d, [cx - 9 * sc, ly - 2 * sc, cx - 2 * sc, ly + 20 * sc], 3.5 * sc, INK)
        rrect(d, [cx + 2 * sc, ly - 2 * sc, cx + 9 * sc, ly + 20 * sc], 3.5 * sc, INK)
    # head
    circ(d, hx, hy, hr, skin)
    # hair cap
    d.pieslice([s(hx - hr), s(hy - hr), s(hx + hr), s(hy + hr)], 180, 360,
               fill=(58, 44, 38) if alpha == 255 else (58, 44, 38, alpha))
    # eyes
    er = max(1.6 * sc, 1.2)
    circ(d, hx - 5.5 * sc, hy + 2 * sc, er, INK)
    circ(d, hx + 5.5 * sc, hy + 2 * sc, er, INK)
    # mouth
    my = hy + 9 * sc
    if sad:
        d.arc([s(hx - 5 * sc), s(my), s(hx + 5 * sc), s(my + 7 * sc)], 180, 360,
              fill=INK, width=max(s(1.4 * sc), 2))
    else:
        d.arc([s(hx - 5 * sc), s(my - 5 * sc), s(hx + 5 * sc), s(my + 3 * sc)], 20, 160,
              fill=INK, width=max(s(1.4 * sc), 2))


def teacher(d, cx, cy, sc, alpha=255):
    dress = (176, 92, 122) if alpha == 255 else (176, 92, 122, alpha)
    skin = SKIN[0] if alpha == 255 else SKIN[0] + (alpha,)
    hr = 19 * sc
    hy = cy + hr
    d.polygon([(s(cx - 30 * sc), s(hy + hr * 0.7 + 58 * sc)),
               (s(cx + 30 * sc), s(hy + hr * 0.7 + 58 * sc)),
               (s(cx + 17 * sc), s(hy + hr * 0.7)),
               (s(cx - 17 * sc), s(hy + hr * 0.7))], fill=dress)
    aw = 8 * sc
    ay = hy + hr * 0.7 + 8 * sc
    rrect(d, [cx - 21 * sc - aw, ay, cx - 21 * sc + 2, ay + 26 * sc], aw / 2, dress)
    rrect(d, [cx + 21 * sc - 2, ay, cx + 21 * sc + aw, ay + 26 * sc], aw / 2, dress)
    circ(d, cx, hy, hr, skin)
    d.pieslice([s(cx - hr * 1.12), s(hy - hr), s(cx + hr * 1.12), s(hy + hr * 1.25)],
               180, 360, fill=(48, 34, 30))
    circ(d, cx - 6.5 * sc, hy + 2 * sc, 2 * sc, INK)
    circ(d, cx + 6.5 * sc, hy + 2 * sc, 2 * sc, INK)
    d.arc([s(cx - 6 * sc), s(hy + 4 * sc), s(cx + 6 * sc), s(hy + 13 * sc)], 20, 160,
          fill=INK, width=max(s(1.6 * sc), 2))


def waiter(d, cx, cy, sc):
    hr = 18 * sc
    hy = cy + hr
    rrect(d, [cx - 22 * sc, hy + hr * 0.7, cx + 22 * sc, hy + hr * 0.7 + 56 * sc], 10 * sc, INK)
    rrect(d, [cx - 8 * sc, hy + hr * 0.7, cx + 8 * sc, hy + hr * 0.7 + 34 * sc], 4 * sc, WHITE)
    rrect(d, [cx + 22 * sc - 2, hy + hr * 0.7 + 6 * sc, cx + 30 * sc, hy + hr * 0.7 + 30 * sc], 4 * sc, INK)
    circ(d, cx, hy, hr, SKIN[1])
    d.pieslice([s(cx - hr), s(hy - hr), s(cx + hr), s(hy + hr)], 180, 360, fill=(40, 30, 26))
    circ(d, cx - 6 * sc, hy + 2 * sc, 2 * sc, INK)
    circ(d, cx + 6 * sc, hy + 2 * sc, 2 * sc, INK)
    d.arc([s(cx - 6 * sc), s(hy + 4 * sc), s(cx + 6 * sc), s(hy + 13 * sc)], 20, 160,
          fill=INK, width=max(s(1.6 * sc), 2))
    ell(d, cx + 40 * sc, hy + hr * 0.7 + 4 * sc, 15 * sc, 5 * sc, WHITE, GREY, 1.5 * sc)


# ---------- table ----------
SEAT_ANG = [200, 250, 290, 340, 20, 70]   # 6 seats around an ellipse

def seat_pos(cx, cy, rx, ry, i):
    a = math.radians(SEAT_ANG[i % 6])
    return cx + rx * 1.55 * math.cos(a), cy + ry * 1.9 * math.sin(a)

def table(d, cx, cy, rx, ry, occupied=0, ci_start=0, dim=False):
    col = (WOOD_D if not dim else (215, 205, 192))
    top = (WOOD if not dim else (232, 224, 212))
    ell(d, cx, cy + ry * 0.35, rx, ry, col)
    ell(d, cx, cy, rx, ry, top, col, 2.5)
    for i in range(6):
        sx, sy = seat_pos(cx, cy, rx, ry, i)
        ell(d, sx, sy, rx * 0.28, ry * 0.4, (198, 190, 178) if not dim else (228, 222, 212))