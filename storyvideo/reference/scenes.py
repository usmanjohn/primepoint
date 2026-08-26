from draw import *
import math

# ---------- shared layout ----------
COLS = 7
def grid_pos(i):
    r, c = divmod(i, COLS)
    n_in_row = min(COLS, 37 - r * COLS)
    x0 = W / 2 - (n_in_row - 1) * 132 / 2
    return x0 + c * 132, 640 + r * 178

TBL = [(285, 700), (795, 700), (285, 1010), (795, 1010), (285, 1320), (795, 1320)]
TRX, TRY = 140, 58

def cafe_bg(d):
    rrect(d, [0, 0, W, 300], 0, (238, 226, 206))
    for i in range(6):
        x = 60 + i * 180
        rrect(d, [x, 60, x + 120, 210], 12, (214, 232, 238), (200, 186, 164), 4)
    line(d, (0, 300), (W, 300), (214, 198, 172), 4)

def caption(d, txt, size=44, y=1730, fill=INK, a=1.0):
    if a <= 0.01:
        return
    c = tuple(int(fill[k] * a + CREAM[k] * (1 - a)) for k in range(3))
    wrap(d, (W / 2, y), txt, size, 900, c, 1.3, True, True, "ma")


# ============ S1  title / hook ============
def s1(t, dur):
    img, d = new_frame()
    p = ease_out(t / 0.8)
    text(d, (W / 2, 520 - 40 * (1 - p)), "37", 300, GOLD_D)
    text(d, (W / 2, 730), "bola", 76, INK)
    if t > 1.0:
        p2 = ease_out((t - 1.0) / 0.8)
        text(d, (W / 2, 900 + 30 * (1 - p2)), "6", 190,
             tuple(int(INK[k] * p2 + CREAM[k] * (1 - p2)) for k in range(3)))
        text(d, (W / 2, 1040), "kishilik stol", 62,
             tuple(int(INK[k] * p2 + CREAM[k] * (1 - p2)) for k in range(3)))
    if t > 2.1:
        p3 = ease_out((t - 2.1) / 0.7)
        text(d, (W / 2, 1290), "Nechta stol kerak?", int(66 * (0.85 + 0.15 * p3)),
             tuple(int(RED[k] * p3 + CREAM[k] * (1 - p3)) for k in range(3)))
    if t > 3.2:
        caption(d, "Bir savol — bir stol.", 40, 1560, GREY, ease((t - 3.2) / 0.6))
    return img


# ============ S2  arrival + count to 37 ============
def s2(t, dur):
    img, d = new_frame()
    cafe_bg(d)
    teacher(d, 150, 350, 1.25)
    waiter(d, 930, 355, 1.15)
    n = int(clamp(t / 6.2) * 37 + 0.001)
    n = min(37, n)
    for i in range(n):
        x, y = grid_pos(i)
        app = clamp((t / 6.2 * 37) - i)
        kid(d, x, y + 26 * (1 - ease_out(app)), 1.0, i, i % 4, standing=True)
    text(d, (W / 2, 400), str(n), 130, GOLD_D)
    if t > 6.6:
        caption(d, "Nodira opa sinfni kafega olib bordi. Bolalar 37 nafar edi.",
                40, 1700, INK, ease((t - 6.6) / 0.6))
    return img


# ============ S3  waiter's question ============
def s3(t, dur):
    img, d = new_frame()
    cafe_bg(d)
    waiter(d, W / 2, 380, 2.0)
    p = ease_out(t / 0.7)
    rrect(d, [110, 700 + 40 * (1 - p), 970, 1000 + 40 * (1 - p)], 40, WHITE, (222, 210, 192), 4)
    text(d, (W / 2, 790 + 40 * (1 - p)), "Bizda stollar", 52, INK)
    text(d, (W / 2, 900 + 40 * (1 - p)), "6 kishilik", 78, GOLD_D)
    if t > 1.8:
        p2 = ease_out((t - 1.8) / 0.7)
        col = tuple(int(RED[k] * p2 + CREAM[k] * (1 - p2)) for k in range(3))
        text(d, (W / 2, 1180), "Nechtasini", 60, col)
        text(d, (W / 2, 1265), "tayyorlaymiz?", 60, col)
    # one demo table with 6 seats
    if t > 3.2:
        p3 = ease_out((t - 3.2) / 0.8)
        table(d, W / 2, 1520, TRX * 1.1 * p3, TRY * 1.1 * p3, dim=False)
        if p3 > 0.9:
            for i in range(6):
                sx, sy = seat_pos(W / 2, 1520, TRX * 1.1, TRY * 1.1, i)
                circ(d, sx, sy, 16, GOLD)
                text(d, (sx, sy), str(i + 1), 26, WHITE)
    if t > 5.0:
        caption(d, "Har stolga 6 kishi sigʻadi.", 40, 1730, GREY, ease((t - 5.0) / 0.5))
    return img


# ============ S4  silent beat — viewer divides ============
def s4(t, dur):
    img, d = new_frame()
    cafe_bg(d)
    teacher(d, 150, 350, 1.25)
    waiter(d, 930, 355, 1.15)
    for i in range(37):
        x, y = grid_pos(i)
        kid(d, x, y, 1.0, i, i % 4, standing=True)
    text(d, (W / 2, 400), "37", 130, GOLD_D)
    # ticking dots only — no words, let the viewer think
    for k in range(3):
        on = t > 1.0 + k * 1.1
        circ(d, W / 2 - 60 + k * 60, 1760, 14, GOLD_D if on else (226, 216, 200))
    return img


# ============ S5  Sardor divides ============
def s5(t, dur):
    img, d = new_frame()
    kid(d, 230, 300, 2.3, 0, 1, standing=True, arms_up=t > 1.2)
    text(d, (490, 400), "Sardor", 56, GREY, "lm")
    y0 = 780
    p = ease_out(t / 0.6)
    text(d, (W / 2, y0), "37 ÷ 6", int(150 * (0.9 + 0.1 * p)), INK)
    if t > 1.4:
        text(d, (W / 2, y0 + 190), "=", 110, GREY)
    if t > 2.0:
        p2 = ease_out((t - 2.0) / 0.5)
        circ(d, W / 2, y0 + 400, 110 * p2, GOLD)
        text(d, (W / 2, y0 + 400), "6", int(150 * p2) if p2 > 0.1 else 1, WHITE)
    if t > 3.4:
        caption(d, "Sardor darrov hisobladi va «6» dedi.", 42, 1520,
                INK, ease((t - 3.4) / 0.5))
    if t > 5.6:
        a = ease((t - 5.6) / 0.5)
        caption(d, "Toʻgʻrimi?", 56, 1680, RED, a)
    return img


# ============ S6  tables fill to 36 ============
def s6(t, dur):
    img, d = new_frame()
    per = 0.30
    seated = int(clamp(t / (36 * per)) * 36 + 0.001)
    seated = min(36, seated)
    for ti, (cx, cy) in enumerate(TBL):
        table(d, cx, cy, TRX, TRY, dim=(seated <= ti * 6))
    for i in range(seated):
        ti, si = divmod(i, 6)
        cx, cy = TBL[ti]
        sx, sy = seat_pos(cx, cy, TRX, TRY, si)
        kid(d, sx, sy - 34, 0.85, i, i % 4)
    text(d, (300, 380), str(seated), 120, INK, "mm")
    text(d, (300, 470), "oʻtirdi", 38, GREY, "mm")
    text(d, (780, 380), str(min(6, (seated + 5) // 6)), 120, GOLD_D, "mm")
    text(d, (780, 470), "stol", 38, GREY, "mm")
    if seated >= 36 and t > 36 * per + 0.4:
        caption(d, "Oltita stol toʻldi. 6 × 6 = 36", 46, 1640, INK,
                ease((t - 36 * per - 0.4) / 0.5))
    return img


# ============ S7  Bekzod left standing ============
S7_TBL = [(300, 560), (780, 560), (300, 800), (780, 800), (300, 1040), (780, 1040)]

def s7(t, dur):
    img, d = new_frame()
    for ti, (cx, cy) in enumerate(S7_TBL):
        table(d, cx, cy, 125, 50, dim=True)
        for si in range(6):
            sx, sy = seat_pos(cx, cy, 125, 50, si)
            kid(d, sx, sy - 26, 0.62, ti * 6 + si, si % 4, alpha=105)
    text(d, (W / 2, 300), "36", 88, GREY, "mm")
    text(d, (W / 2, 375), "oʻtirdi", 34, GREY, "mm")
    bx, by = W / 2, 1300
    if t > 0.4:
        r = 155 + 26 * math.sin((t - 0.4) * 3.4)
        circ(d, bx, by + 85, r, (255, 236, 200))
    kid(d, bx, by, 1.9, 3, 2, standing=True, sad=t > 1.0)
    if t > 1.6:
        p = ease_out((t - 1.6) / 0.5)
        text(d, (bx, 1560), "Bekzod", int(54 * p) if p > 0.1 else 1, INK, "mm")
    if t > 3.0:
        p = ease_out((t - 3.0) / 0.5)
        text(d, (W / 2, 1690), "unga oʻrindiq yetmadi",
             int(52 * p) if p > 0.1 else 1, RED, "mm")
    if t > 5.2:
        p = ease((t - 5.2) / 0.5)
        text(d, (W / 2, 1810), "36 + 1 = 37", 56 if p > 0.5 else 1, GREY, "mm")
    return img


# ============ S8  the correction: 6 -> 7 ============
def s8(t, dur):
    img, d = new_frame()
    text(d, (W / 2, 430), "37 ÷ 6", 120, INK)
    y = 760
    text(d, (W / 2 - 150, y), "6", 190, INK if t < 1.2 else GREY)
    if t > 1.2:
        p = ease_out((t - 1.2) / 0.4)
        line(d, (W / 2 - 250, y), (W / 2 - 250 + 200 * p, y), RED, 12)
    if t > 1.9:
        p = ease_out((t - 1.9) / 0.5)
        text(d, (W / 2 + 160, y + 40 * (1 - p)), "7", int(190 * (0.8 + 0.2 * p)), RED)
    if t > 2.7:
        p = ease((t - 2.7) / 0.5)
        rrect(d, [130, 1010, 950, 1230], 34, (250, 244, 232), GOLD, 4)
        text(d, (W / 2, 1075), "37 ÷ 6 = 6", 62, INK)
        text(d, (W / 2, 1165), "qoldiq 1", 62, RED)
    if t > 4.4:
        caption(d, "Sen qoldiqni unutding.", 46, 1350, INK, ease((t - 4.4) / 0.5))
    if t > 6.4:
        caption(d, "— Demak javob 6 emas, 7. Bekzodga ham stol kerak.",
                40, 1560, GREY, ease((t - 6.4) / 0.6))
    return img


# ============ S9  seventh table ============
def s9(t, dur):
    img, d = new_frame()
    for ti, (cx, cy) in enumerate(TBL):
        table(d, cx, cy, TRX * 0.9, TRY * 0.9, dim=True)
        for si in range(6):
            sx, sy = seat_pos(cx, cy, TRX * 0.9, TRY * 0.9, si)
            kid(d, sx, sy - 28, 0.7, ti * 6 + si, si % 4, alpha=115)
    p = ease_out(clamp(t / 1.4))
    cx = W + 300 - (W + 300 - W / 2) * p
    cy = 1560
    table(d, cx, cy, TRX, TRY)
    if t > 1.5:
        sx, sy = seat_pos(cx, cy, TRX, TRY, 0)
        kid(d, sx, sy - 34, 1.0, 3, 2, arms_up=t > 2.2)
    if t > 2.6:
        a = ease((t - 2.6) / 0.5)
        text(d, (W / 2, 340), "7", int(140), GOLD_D, "mm")
        text(d, (W / 2, 440), "stol", 44, INK if a > 0.5 else CREAM, "mm")
    if t > 3.6:
        caption(d, "Ofitsiant yettinchi stolni surdi. Hammani kulgi bosdi.",
                40, 1810, GREY, ease((t - 3.6) / 0.5))
    return img


# ============ S10  the check — static frame ============
def s10(t, dur):
    img, d = new_frame((250, 246, 236))
    text(d, (W / 2, 480), "Tekshiramiz", 52, GREY)
    a = ease(t / 0.5)
    if a > 0.3:
        text(d, (W / 2, 800), "6 × 6 + 1 = 37", 108, INK)
        line(d, (200, 940), (880, 940), GOLD, 8)
    if t > 1.6:
        text(d, (W / 2, 1080), "6 stol × 6 bola", 52, GREY)
        text(d, (W / 2, 1170), "+ 1 qoldiq", 52, RED)
    if t > 3.2:
        text(d, (W / 2, 1400), "Hammasi joyida.", 58, GREEN)
    return img


# ============ S11  the rule ============
def s11(t, dur):
    img, d = new_frame(INK)
    def tx(xy, s_, txt, col=CREAM, an="mm"):
        text(d, xy, txt, s_, col, an)
    tx((W / 2, 420), 44, "Esda tutinglar", GREY)
    if t > 0.5:
        wrap(d, (W / 2, 600), "«Kamida nechta kerak?»", 62, 900, GOLD, 1.3, True, True, "ma")
    if t > 1.6:
        rrect(d, [130, 830, 950, 1010], 30, (44, 50, 68))
        text(d, (W / 2, 920), "qoldiq bor  →  +1", 58, CREAM)
    if t > 3.0:
        wrap(d, (W / 2, 1150), "Teng boʻlinish har doim ham chiqavermaydi.",
             46, 880, (200, 200, 210), 1.35, True, True, "ma")
    if t > 4.6:
        p = ease((t - 4.6) / 0.6)
        for i in range(7):
            x = 180 + i * 120
            circ(d, x, 1420, 34, GOLD if i < 6 else RED)
            text(d, (x, 1420), str(i + 1), 34, INK)
        text(d, (W / 2, 1540), "6 stol + 1 stol = 7", 46, CREAM if p > 0.5 else INK)
    if t > 6.4:
        tx((W / 2, 1740), 40, "Powerty · matematika hikoyalari", (140, 145, 160))
    return img


TIMELINE = [
    (s1, 4.5), (s2, 10.5), (s3, 8.0), (s4, 4.5), (s5, 9.5), (s6, 13.0),
    (s7, 8.5), (s8, 9.5), (s9, 8.0), (s10, 8.0), (s11, 9.0),
]