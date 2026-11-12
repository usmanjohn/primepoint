"""
The map of Uzbekistan with Kapitalbank's offices, drawn as plain SVG in Python.
No JavaScript, no map tiles from the internet: the page works on a closed network.

THE DATA (branchmap/data/)
    regions.geojson   the 14 regions (13 + Tashkent city). geoBoundaries, from OpenStreetMap
                      (licence ODbL 1.0), simplified and rounded to 0.001° (~100 m).
                      Each region has its ISO code: UZ-AN, UZ-TK ... (the old map used UZAN).
    offices.json      the offices from kapitalbank.uz «Отделения» (2026-11-10): name, address,
                      city, lat, lon. ATMs are left out on purpose. To refresh it, save the
                      list again in the same shape and replace the file.

HOW IT IS DRAWN
    project()      lon/lat → x/y. Equirectangular with the longitude squeezed by cos(41.5°),
                   which keeps Uzbekistan's shape right at this latitude.
    region_of()    which region a point is in (ray casting): every office gets its region,
                   so a portfolio by region can be joined to the map later.
    build_map()    everything the template needs: region paths, labels, office dots, the
                   Tashkent inset and the counts table.
"""
import json
import math
from functools import lru_cache
from pathlib import Path

DATA = Path(__file__).resolve().parent / "data"

# ISO code → (Russian name, short label on the map)
REGIONS = {
    "UZ-QR": ("Республика Каракалпакстан", "Каракалпакстан"),
    "UZ-XO": ("Хорезмская область", "Хорезм"),
    "UZ-NW": ("Навоийская область", "Навои"),
    "UZ-BU": ("Бухарская область", "Бухара"),
    "UZ-SA": ("Самаркандская область", "Самарканд"),
    "UZ-QA": ("Кашкадарьинская область", "Кашкадарья"),
    "UZ-SU": ("Сурхандарьинская область", "Сурхандарья"),
    "UZ-JI": ("Джизакская область", "Джизак"),
    "UZ-SI": ("Сырдарьинская область", "Сырдарья"),
    "UZ-TO": ("Ташкентская область", "Ташкентская обл."),
    "UZ-TK": ("г. Ташкент", "Ташкент"),
    "UZ-NG": ("Наманганская область", "Наманган"),
    "UZ-AN": ("Андижанская область", "Андижан"),
    "UZ-FA": ("Ферганская область", "Фергана"),
}

# Where a label sits when the middle of the shape is a bad place (lon, lat).
LABEL_AT = {
    "UZ-QR": (59.0, 43.6), "UZ-NW": (64.0, 41.6), "UZ-TO": (70.25, 41.95),
    "UZ-FA": (71.25, 40.22), "UZ-NG": (71.2, 41.12), "UZ-AN": (72.85, 40.58),
    "UZ-SI": (68.5, 40.85), "UZ-XO": (60.95, 41.02), "UZ-SU": (67.55, 37.95),
    "UZ-SA": (66.35, 40.08), "UZ-QA": (66.45, 38.45), "UZ-JI": (67.55, 40.6),
    "UZ-BU": (63.6, 40.0),
}

# The kinds of office, in drawing order (small first, so the big ones sit on top).
KINDS = {
    "mini":   {"label": "Мини-банк", "short": "Мини", "r": 3.6},
    "obu":    {"label": "ОБУ (офис банковских услуг)", "short": "ОБУ", "r": 4.6},
    "branch": {"label": "Филиал / ЦБУ / ЦПО", "short": "Филиал", "r": 6.2},
}

LAT0 = 41.5                       # the latitude where the map keeps its true shape
SQUEEZE = math.cos(math.radians(LAT0))


def kind_of(name):
    """«ОБУ «Amal»» → 'obu', «Мини-банк «…»» → 'mini', everything else (филиал, ЦБУ, ЦПО, ОПЕРУ …) → 'branch'."""
    low = name.lower()
    if low.startswith("обу"):
        return "obu"
    if low.startswith("мини-банк") or low.startswith("минибанк"):
        return "mini"
    return "branch"


# ═══════════════════════════════ READ ═════════════════════════════════════════════

@lru_cache(maxsize=1)
def regions():
    """{iso: [polygon, ...]}, a polygon = [outer ring, hole, ...], a ring = [(lon, lat), ...]."""
    data = json.loads((DATA / "regions.geojson").read_text(encoding="utf-8"))
    return {f["properties"]["iso"]: [[[tuple(p) for p in ring] for ring in poly]
                                     for poly in f["geometry"]["coordinates"]]
            for f in data["features"]}


@lru_cache(maxsize=1)
def offices():
    """The offices, each with its kind and its region."""
    rows = json.loads((DATA / "offices.json").read_text(encoding="utf-8"))
    for row in rows:
        row["kind"] = kind_of(row["name"])
        row["region"] = region_of(row["lon"], row["lat"])
    return rows


# ═══════════════════════════════ GEOMETRY ═════════════════════════════════════════

def inside(lon, lat, ring):
    """Ray casting: is the point inside this ring?"""
    hit = False
    for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
        if (y1 > lat) != (y2 > lat) and lon < (x2 - x1) * (lat - y1) / (y2 - y1) + x1:
            hit = not hit
    return hit


def region_of(lon, lat):
    """The ISO code of the region the point is in; the nearest region if it is just outside
    (an office on the border line, or a coordinate a few metres off)."""
    for iso, polys in regions().items():
        for poly in polys:
            if inside(lon, lat, poly[0]) and not any(inside(lon, lat, hole) for hole in poly[1:]):
                return iso
    best, best_d = None, None
    for iso, polys in regions().items():
        for poly in polys:
            d = min((x - lon) ** 2 + (y - lat) ** 2 for x, y in poly[0])
            if best_d is None or d < best_d:
                best, best_d = iso, d
    return best


def bounds(isos=None):
    """(min lon, min lat, max lon, max lat) of the given regions (all if None)."""
    xs, ys = [], []
    for iso, polys in regions().items():
        if isos is None or iso in isos:
            for poly in polys:
                for x, y in poly[0]:
                    xs.append(x)
                    ys.append(y)
    return min(xs), min(ys), max(xs), max(ys)


class Projection:
    """lon/lat → x/y in a box `width` wide, fitted to `box` = (lon1, lat1, lon2, lat2)."""

    def __init__(self, box, width, pad=14):
        lon1, lat1, lon2, lat2 = box
        self.lon1, self.lat2, self.pad = lon1, lat2, pad
        self.scale = (width - 2 * pad) / ((lon2 - lon1) * SQUEEZE)
        self.width = width
        self.height = round((lat2 - lat1) * self.scale + 2 * pad)

    def __call__(self, lon, lat):
        return (round((lon - self.lon1) * SQUEEZE * self.scale + self.pad, 1),
                round((self.lat2 - lat) * self.scale + self.pad, 1))

    def back(self, x, y):
        """x/y → lon/lat (the other way round)."""
        return ((x - self.pad) / self.scale / SQUEEZE + self.lon1, self.lat2 - (y - self.pad) / self.scale)


def path(polys, project):
    """SVG path data of a region: one «M … Z» per ring (holes cut out by fill-rule evenodd)."""
    parts = []
    for poly in polys:
        for ring in poly:
            points = [project(x, y) for x, y in ring]
            parts.append("M" + "L".join(f"{x},{y}" for x, y in points) + "Z")
    return "".join(parts)


def centre(polys):
    """The middle of the region's biggest ring (good enough for a label)."""
    ring = max((poly[0] for poly in polys), key=len)
    return sum(x for x, y in ring) / len(ring), sum(y for x, y in ring) / len(ring)


# ═══════════════════════════════ THE PAGE ═════════════════════════════════════════

def shade(count, most):
    """Region fill by number of offices: paper → Kapital gold (0 offices = paper)."""
    if not count:
        return "#F4F1E8"
    t = 0.25 + 0.75 * math.sqrt(count / most)
    paper, gold = (0xF4, 0xF1, 0xE8), (0xF2, 0xC2, 0x30)
    return "#" + "".join(f"{round(a + (b - a) * t):02X}" for a, b in zip(paper, gold))


def in_region(lon, lat, polys):
    return any(inside(lon, lat, poly[0]) and not any(inside(lon, lat, h) for h in poly[1:]) for poly in polys)


def place_label(iso, text, project, dots, taken, inside_only=True):
    """
    Where to write the region's name: start at LABEL_AT (or the middle) and walk out in a
    spiral until the WHOLE text box is inside the region, clear of every dot and of the
    labels already placed. Returns (x, y) of the text's baseline centre, or None when the
    name does not fit.
    inside_only=False is the second try for a small region: the name may stand next to it
    (inside the map's frame, still clear of dots and labels), joined by a leader line.
    """
    polys = regions()[iso]
    lon0, lat0 = LABEL_AT.get(iso) or centre(polys)
    half_w, height = len(text) * 3.7 + 2, 13          # 12px semibold text, a little air
    for step in range(0, 2500):
        # a sunflower spiral: evenly spread over the area (one try every ~6 px), nearest first
        angle, radius = step * 2.39996, 0.045 * math.sqrt(step)
        lon = lon0 + radius * math.cos(angle) / SQUEEZE
        lat = lat0 + radius * math.sin(angle)
        x, y = project(lon, lat)
        box = (x - half_w, y - height, x + half_w, y + 3)
        corners = [(box[0], box[1]), (box[2], box[1]), (box[0], box[3]), (box[2], box[3]),
                   (x, box[1]), (x, box[3])]
        if inside_only and not all(in_region(*project.back(cx, cy), polys) for cx, cy in corners):
            continue
        if not inside_only:
            if box[0] < 4 or box[1] < 4 or box[2] > project.width - 4 or box[3] > project.height - 4:
                continue
            # beside the region: over empty ground or its own region, never over a neighbour
            # (a name over another region reads as that region's name)
            if any(in_region(*project.back(cx, cy), other)
                   for cx, cy in corners for o, other in regions().items() if o != iso):
                continue
        if any(box[0] - d["r"] - 1 < d["x"] < box[2] + d["r"] + 1 and box[1] - d["r"] - 1 < d["y"] < box[3] + d["r"] + 1
               for d in dots):
            continue
        if any(box[0] < t[2] and t[0] < box[2] and box[1] < t[3] and t[1] < box[3] for t in taken):
            continue
        taken.append(box)
        return x, y
    return None                                           # it does not fit anywhere


def layer(project, counts, most, labels=True):
    """Region paths (+ labels) and office dots for one projection."""
    dots = []
    for kind in KINDS:
        for o in offices():
            if o["kind"] == kind:
                x, y = project(o["lon"], o["lat"])
                dots.append({"x": x, "y": y, "r": KINDS[kind]["r"], "kind": kind,
                             "title": f'{o["name"]} — {o["address"]}'})
    regs, taken = [], []
    for iso, polys in regions().items():
        regs.append({"iso": iso, "name": REGIONS[iso][0], "short": REGIONS[iso][1],
                     "d": path(polys, project), "fill": shade(counts.get(iso, 0), most),
                     "count": counts.get(iso, 0), "label": False, "leader": None})
    if labels:
        # first every name that fits inside its region, then the small ones beside theirs
        for inside_only in (True, False):
            for r in regs:
                if r["label"] or r["iso"] == "UZ-TK":
                    continue
                spot = place_label(r["iso"], r["short"], project, dots, taken, inside_only)
                if spot:
                    r.update(label=True, lx=spot[0], ly=spot[1])
                    if not inside_only:            # a thin line from the name to its region
                        ax, ay = project(*(LABEL_AT.get(r["iso"]) or centre(regions()[r["iso"]])))
                        r["leader"] = {"x1": spot[0], "y1": round(spot[1] + (4 if ay > spot[1] else -14), 1),
                                       "x2": ax, "y2": ay}
    return regs, dots


def build_map(width=1000):
    """Everything the page shows: the country, the Tashkent inset, the legend and the table."""
    counts = {}
    for o in offices():
        counts[o["region"]] = counts.get(o["region"], 0) + 1
    most = max(counts.values())

    country = Projection(bounds(), width)
    regs, dots = layer(country, counts, most)

    # Tashkent city, zoomed: the city plus a little of the region around it
    lon1, lat1, lon2, lat2 = bounds({"UZ-TK"})
    box = (lon1 - 0.03, lat1 - 0.03, lon2 + 0.03, lat2 + 0.03)
    city = Projection(box, 460, pad=8)
    city_regs, city_dots = layer(city, counts, most, labels=False)
    city_dots = [d for d in city_dots if 0 <= d["x"] <= city.width and 0 <= d["y"] <= city.height]
    for d in city_dots:                       # zoomed in: the dots may be a little bigger
        d["r"] = round(d["r"] * 1.35, 1)
    # where the inset's frame is on the big map
    fx1, fy1 = country(box[0], box[3])
    fx2, fy2 = country(box[2], box[1])

    table = []
    for iso, (name, short) in REGIONS.items():
        here = [o for o in offices() if o["region"] == iso]
        table.append({"name": name, "total": len(here),
                      **{k: sum(1 for o in here if o["kind"] == k) for k in KINDS}})
    table.sort(key=lambda r: -r["total"])

    return {
        "w": country.width, "h": country.height, "regions": regs, "dots": dots,
        "city": {"w": city.width, "h": city.height, "regions": city_regs, "dots": city_dots},
        "frame": {"x": fx1, "y": fy1, "w": round(fx2 - fx1, 1), "h": round(fy2 - fy1, 1)},
        "kinds": [{"key": k, "label": v["label"], "short": v["short"], "r": v["r"],
                   "count": sum(1 for o in offices() if o["kind"] == k)} for k, v in KINDS.items()],
        "table": table,
        "total": len(offices()),
        "cities": len({o["city"] for o in offices()}),
    }
