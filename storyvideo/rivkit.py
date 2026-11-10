# -*- coding: utf-8 -*-
"""The river — «Mantiq jumbogʻi» #3: the wolf, the goat and the cabbage.

A daytime river, a small boat, a farmer (Anvar aka) and three passengers drawn
here: a wolf, a goat, a cabbage. Same contract as bridgekit/coinkit: `River`
plays a list of crossings as data-kf tracks; every scene is the same river at
a later moment (cam="hold"), replayed at negative times.

The rule is enforced by the simulation, not by the script: whenever the farmer
pushes off, the bank he leaves is checked -- wolf + goat alone, the goat is
gone; goat + cabbage alone, the cabbage is gone -- and the scene shows it
happen mid-river. So a wrong plan in a spec FAILS ON SCREEN by itself.
"""

from bridgekit import _kf, _mark, say      # noqa: F401

W, H = 1080, 1920
BANK_Y = 1250              # feet on the grass
DECK_Y = 1288              # feet in the boat
RIV0, RIV1 = 340, 740      # the water between the banks
DOCK = {0: 450, 1: 630}    # boat centre, docked
SLOT = {0: {"W": 88, "G": 180, "C": 256, "F": 308},
        1: {"F": 772, "C": 826, "G": 902, "W": 994}}
SEAT = {"F": -48, "item": 52}          # in the boat, from its centre
ZOOM, FOCUS = 1.55, 1330
REST = {0: 300, 1: 780}    # where the camera rests while nobody is crossing
NAME = {"W": "boʻri", "G": "echki", "C": "karam", None: "boʻsh"}
T0 = -999

_WOLF = ('<svg viewBox="0 0 150 120" width="150" height="120">'
         '<path d="M18 62 Q -4 40 8 22 Q 18 44 34 54 Z" fill="#6f7680"/>'
         '<ellipse cx="68" cy="66" rx="46" ry="26" fill="#8a929c"/>'
         '<rect x="34" y="78" width="11" height="40" rx="5" fill="#6f7680"/>'
         '<rect x="52" y="80" width="11" height="38" rx="5" fill="#7a828c"/>'
         '<rect x="80" y="80" width="11" height="38" rx="5" fill="#6f7680"/>'
         '<rect x="98" y="78" width="11" height="40" rx="5" fill="#7a828c"/>'
         '<path d="M96 52 L106 14 L118 40 Z M114 42 L130 12 L134 46 Z" fill="#6f7680"/>'
         '<ellipse cx="118" cy="52" rx="24" ry="20" fill="#8a929c"/>'
         '<path d="M126 52 L150 60 L130 70 Z" fill="#9aa2ab"/>'
         '<circle cx="147" cy="60" r="4" fill="#222"/>'
         '<circle cx="122" cy="47" r="4.5" fill="#fff"/><circle cx="123" cy="47" r="2.6" fill="#222"/>'
         '<ellipse cx="62" cy="74" rx="26" ry="10" fill="#c9ced4"/></svg>')

_GOAT = ('<svg viewBox="0 0 140 130" width="140" height="130">'
         '<path d="M14 54 Q 6 46 12 40 Q 18 48 24 50 Z" fill="#e8e2d6"/>'
         '<ellipse cx="60" cy="70" rx="44" ry="26" fill="#f4f0e8" stroke="#d8cfbf" stroke-width="3"/>'
         '<rect x="28" y="82" width="10" height="44" rx="5" fill="#d8cfbf"/>'
         '<rect x="46" y="84" width="10" height="42" rx="5" fill="#e3dccf"/>'
         '<rect x="72" y="84" width="10" height="42" rx="5" fill="#d8cfbf"/>'
         '<rect x="90" y="82" width="10" height="44" rx="5" fill="#e3dccf"/>'
         '<path d="M98 32 Q 104 6 122 10 Q 108 16 106 34 Z" fill="#a08a64"/>'
         '<ellipse cx="110" cy="48" rx="20" ry="22" fill="#f4f0e8" stroke="#d8cfbf" stroke-width="3"/>'
         '<path d="M92 40 Q 80 34 84 48 Z" fill="#e3dccf"/>'
         '<path d="M108 66 Q 112 86 104 90 Q 102 74 104 66 Z" fill="#cfc4b0"/>'
         '<circle cx="114" cy="44" r="4.5" fill="#fff"/><circle cx="115" cy="44" r="2.6" fill="#222"/>'
         '<ellipse cx="126" cy="56" rx="4" ry="3" fill="#b9a99a"/></svg>')

_CABBAGE = ('<svg viewBox="0 0 100 90" width="100" height="90">'
            '<ellipse cx="50" cy="86" rx="38" ry="5" fill="#000" opacity=".15"/>'
            '<circle cx="50" cy="50" r="38" fill="#7fbf4f"/>'
            '<path d="M14 54 Q 30 20 50 18 Q 26 34 24 70 Z" fill="#9bd36a"/>'
            '<path d="M86 54 Q 70 20 50 18 Q 74 34 76 70 Z" fill="#6aa83f"/>'
            '<path d="M50 18 L50 84 M50 40 Q 36 46 32 60 M50 40 Q 64 46 68 60" '
            'stroke="#4f8a2c" stroke-width="3" fill="none"/>'
            '<circle cx="40" cy="44" r="4" fill="#fff"/><circle cx="41" cy="44" r="2.3" fill="#222"/>'
            '<circle cx="60" cy="44" r="4" fill="#fff"/><circle cx="61" cy="44" r="2.3" fill="#222"/>'
            '</svg>')

_BOAT = ('<svg viewBox="0 0 230 74" width="230" height="74">'
         '<path d="M4 10 L226 10 Q 214 66 170 70 L60 70 Q 16 66 4 10 Z" fill="#9a6337" '
         'stroke="#5d3a1d" stroke-width="4"/>'
         '<path d="M14 24 L216 24" stroke="#7a4a26" stroke-width="4"/>'
         '<rect x="0" y="4" width="230" height="10" rx="5" fill="#b77a45"/></svg>')

ART = {"W": (_WOLF, 150, 120), "G": (_GOAT, 140, 130), "C": (_CABBAGE, 100, 90)}

_UID = 0


def _backdrop():
    global _UID
    _UID += 1
    u = f"{_UID}"
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         '<defs><linearGradient id="rk-sky-{u}" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#8ccbee"/><stop offset=".6" stop-color="#d6eef8"/>'
         '<stop offset="1" stop-color="#eef7f2"/></linearGradient>'
         '<linearGradient id="rk-water-{u}" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#4fa3c9"/><stop offset="1" stop-color="#1f5f86"/>'
         '</linearGradient></defs>',
         '<rect width="1080" height="1920" fill="url(#rk-sky-{u})"/>',
         '<circle cx="640" cy="700" r="64" fill="#ffe58a"/>'
         '<circle cx="640" cy="700" r="96" fill="#ffe58a" opacity=".25"/>',
         '<path d="M0 1100 Q 180 990 380 1070 T 760 1050 T 1080 1040 L1080 1300 L0 1300 Z" '
         'fill="#a9cf8a"/>',
         '<path d="M0 1170 Q 240 1110 520 1160 T 1080 1140 L1080 1300 L0 1300 Z" fill="#8cbd6c"/>']
    for x in (80, 200, 880, 990):                      # poplars on the far bank
        s.append(f'<rect x="{x - 5}" y="1080" width="10" height="90" fill="#6b4a2e"/>'
                 f'<ellipse cx="{x}" cy="1060" rx="30" ry="80" fill="#5f9a48"/>')
    s.append('<rect x="0" y="1270" width="1080" height="650" fill="url(#rk-water-{u})"/>')
    for x0, x1, flip in ((0, RIV0, 1), (W, RIV1, -1)):     # the two banks
        e = x1 + flip * 22
        s.append(f'<path d="M{x0} {BANK_Y - 6} L{x1} {BANK_Y - 6} L{e} 1300 '
                 f'L{e - flip * 40} 1920 L{x0} 1920 Z" fill="#7a5a3a"/>'
                 f'<path d="M{x0} {BANK_Y - 10} L{x1 + flip * 6} {BANK_Y - 10} L{x1 + flip * 4} '
                 f'{BANK_Y + 12} L{x0} {BANK_Y + 12} Z" fill="#6aa84f"/>')
        for k in range(4):
            rx = x1 - flip * (14 + k * 11)
            s.append(f'<path d="M{rx} {BANK_Y - 4} q {flip * -6} -40 {flip * 4} -66" '
                     f'stroke="#4f7d34" stroke-width="5" fill="none" stroke-linecap="round"/>')
    s.append('</svg>')
    return "".join(s).replace("{u}", u)


def _waves(span=60.0):
    out = []
    for i, (x, y, w) in enumerate([(380, 1330, 90), (560, 1360, 120), (420, 1420, 70),
                                   (620, 1450, 80), (470, 1520, 110), (390, 1600, 60),
                                   (600, 1640, 90)]):
        d = 22 if i % 2 else -22
        keys, t, k = [], T0, 0
        keys.append([T0, x])
        t = 0.0
        while t < span:
            keys.append([t, x + (d if k % 2 else 0)])
            t += 2.2
            k += 1
        out.append(f'<i class="rk-wave" style="top:{y}px;width:{w}px" {_kf({"x": keys})}></i>')
    for i, (x, y) in enumerate([(160, 330), (700, 470), (420, 760)]):
        keys = [[T0, x], [0, x], [60, x + 150 * (1 if i % 2 else -1)]]
        out.append(f'<i class="rk-cloud" style="top:{y}px" {_kf({"x": keys})}></i>')
    return '<div class="rk-amb" data-backdrop>' + "".join(out) + '</div>'


class River:
    def __init__(self):
        self.side = {"F": 0, "W": 0, "G": 0, "C": 0}
        self.tr = {}
        for k in self.side:
            x = SLOT[0][k]
            self.tr[k] = {"x": [[T0, x]], "y": [[T0, BANK_Y]], "o": [[T0, 1]],
                          "s": [[T0, 1]], "m": [[T0, 0]]}
        self.boat = {"x": [[T0, DOCK[0]]]}
        self.eaten, self.extra, self.chips, self.trips = set(), [], [], 0
        self.count = {"n": [[T0, 0]]}
        self.cam = [(T0, REST[0])]
        self.end = 0.5

    def _key(self, k, t, x, y, m=None):
        self.tr[k]["x"].append([t, x])
        self.tr[k]["y"].append([t, y])
        if m is not None:
            self.tr[k]["m"].append([t, m])

    def trip(self, item=None, at=0.0, board=0.7, cross=2.0, land=0.7, gap=0.4):
        """The farmer (and `item`, if any) crosses. Returns the end time."""
        if self.eaten:
            return at
        s = self.side["F"]
        o = 1 - s
        movers = ["F"] + ([item] if item else [])
        b0, b1 = DOCK[s], DOCK[o]
        t = at
        self.cam.append((t, REST[s]))
        # board: walk from the bank slot into the boat
        for k in movers:
            seat = SEAT["F"] if k == "F" else SEAT["item"]
            self._key(k, t, SLOT[s][k], BANK_Y, 1 if k == "F" else 0)
            self._key(k, t + board, b0 + seat, DECK_Y, 0)
        self.extra.append(_mark("rk-board", t + board * 0.8))
        t += board
        # the chip names the passenger as the boat pushes off
        self.trips += 1
        arrow = "→" if o == 1 else "←"
        self.chips.append(f'<span class="bk-led{" bk-led--back" if o == 0 else ""}" '
                          f'data-at="{t:.3f}" data-dur="0.4" data-anim="pop">'
                          f'{arrow} {NAME[item]}</span>')
        self.count["n"] += [[t - 0.01, self.trips - 1], [t, self.trips]]
        # cross: boat and passengers glide together
        self.boat["x"] += [[t, b0], [t + cross, b1]]
        for k in movers:
            seat = SEAT["F"] if k == "F" else SEAT["item"]
            self._key(k, t, b0 + seat, DECK_Y)
            self._key(k, t + cross, b1 + seat, DECK_Y)
        self.extra.append(_mark("rk-row", t + 0.2))
        # the bank just left: is anything eaten?
        left = [k for k in ("W", "G", "C") if self.side[k] == s and k not in movers]
        victim = None
        if "W" in left and "G" in left:
            victim, eater = "G", "W"
        elif "G" in left and "C" in left:
            victim, eater = "C", "G"
        if victim:
            te = t + cross * 0.55
            self.tr[victim]["o"] += [[te, 1], [te + 0.45, 0]]
            self.tr[victim]["s"] += [[te, 1], [te + 0.45, 0.4]]
            self.tr[eater]["s"] += [[te, 1], [te + 0.2, 1.18], [te + 0.5, 1]]
            self.extra.append(_mark("rk-eat", te))
            x = SLOT[s][victim]
            self.extra.append(f'<div class="ck-tag" style="left:{x}px;top:{BANK_Y - 150}px" '
                              f'data-at="{te + 0.3:.3f}" data-dur="0.45" data-anim="pop">'
                              f'<span class="rk-bad">{"yeb qoʻydi!"}</span></div>')
            self.eaten.add(victim)
            self.died = te
            # the camera swings BACK to the bank: the loss must happen on screen
            mid = b0 + (b1 - b0) * 0.45
            self.cam += [(t, b0), (te - 0.35, mid), (te + 0.25, 200 if s == 0 else 880)]
        else:
            self.cam += [(t, b0), (t + cross, b1), (t + cross + land, REST[o])]
        t += cross
        # land: step out onto the far bank
        for k in movers:
            seat = SEAT["F"] if k == "F" else SEAT["item"]
            self._key(k, t, b1 + seat, DECK_Y, 1 if k == "F" else 0)
            self._key(k, t + land, SLOT[o][k], BANK_Y, 0)
            self.side[k] = o
        t += land
        self.end = t if not victim else max(t, self.died + 1.0)
        return t + gap

    def html(self, msg="", hud=True):
        cam = {"x": [], "y": [], "s": []}
        for t, cx in self.cam:
            half = W / (2 * ZOOM)
            cx = min(max(cx, half), W - half)
            cam["x"].append([t, W / 2 - ZOOM * cx])
            cam["y"].append([t, max(H - ZOOM * H, FOCUS - ZOOM * BANK_Y)])
            cam["s"].append([t, ZOOM])
        h = ['<div class="rk">', f'<div class="bk-cam" data-camera {_kf(cam)}>',
             f'<div class="ck-bg" data-backdrop>{_backdrop()}</div>', _waves()]
        h.append(f'<div class="rk-ent" {_kf(self.boat)}><div class="rk-boat">{_BOAT}</div></div>')
        for k in ("W", "G", "C"):
            art, w, hh = ART[k]
            h.append(f'<div class="rk-ent" {_kf(self.tr[k])}><div class="rk-art" '
                     f'style="left:{-w / 2:.0f}px;top:{-hh}px">{art}</div></div>')
        import people as _people
        fig = _people.figure("Anvar aka", size=190)
        h.append(f'<div class="rk-ent" {_kf(self.tr["F"])}><div class="rk-art" '
                 f'style="left:-54px;top:-190px">{fig}</div></div>')
        h.append('</div>')
        if hud:
            h.append(f'<div class="ck-hud"><span class="ck-hud__l">Qatnov</span>'
                     f'<b class="ck-n" {_kf(self.count)}>0</b></div>')
        h.append('<div class="bk-ledger rk-ledger">' + "".join(self.chips) + '</div>')
        if msg:
            h.append(f'<div class="bk-msg ck-msg">{msg}</div>')
        h += self.extra
        h.append(_mark("rk-end", self.end))
        h.append('</div>')
        return "".join(h)
