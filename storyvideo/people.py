# -*- coding: utf-8 -*-
"""The cast.

The maths readings use the user's real pupils by name (Afsona, Sardor, Bekzod,
Jasur, Sherbek, Nodira opa), so the videos do too -- and each one keeps the same
colours across the whole shelf. Bekzod is the same boy in PM-4 as in PM-67, which
is what turns a pile of clips into a series.

Two variants of every figure:
  crowd  -- small, for counting. Silhouette does the work; the face is a hint.
  hero   -- large close-up, with a real expression.
Both come from the same SVG so a face never changes shape between shots.
"""

SKIN = {"l": "#f0cfae", "m": "#dcae83", "d": "#b9835a"}


# name -> shirt, skin tone, hair
CAST = {
    "Afsona":     {"shirt": "#c4607a", "skin": "l", "hair": "#2b211c", "long": True},
    "Sardor":     {"shirt": "#3f7fbf", "skin": "m", "hair": "#2b211c"},
    "Bekzod":     {"shirt": "#e0a355", "skin": "m", "hair": "#241b17"},
    "Jasur":      {"shirt": "#4f9e78", "skin": "d", "hair": "#241b17"},
    "Sherbek":    {"shirt": "#8d6bb0", "skin": "l", "hair": "#3a2a22"},
    "Nodira opa": {"shirt": "#a8506e", "skin": "l", "hair": "#241b17", "long": True, "adult": True},
    "ofitsiant":  {"shirt": "#2f3a44", "skin": "m", "hair": "#241b17", "adult": True, "apron": True},
}

# Extras for filling a crowd -- never named, just varied so 37 children look
# like 37 children and not 37 copies.
EXTRA_SHIRTS = ["#5b8fc7", "#e07a5f", "#81b29a", "#e6b45e", "#b089be",
                "#e795b3", "#6cb0be", "#d4a373", "#7f9e5a", "#c9776a"]
EXTRA_SKIN   = ["l", "m", "d"]

MOUTHS = {
    "smile":  "M 36 62 Q 50 74 64 62",
    "flat":   "M 38 65 L 62 65",
    "sad":    "M 36 70 Q 50 58 64 70",
    "oh":     None,          # drawn as an ellipse instead
    "think":  "M 38 66 Q 46 62 60 67",
}


def _person_svg(shirt, skin, hair, mood="smile", long_hair=False, adult=False,
                apron=False, arms="down"):
    """One figure in a 100x175 viewBox, feet on the baseline.

    Kept deliberately simple in shape but complete in parts -- hair, eyes, a real
    mouth, arms that can go up -- so the same drawing survives being blown up to
    a 420px hero shot without turning into a pictogram.
    """
    sk = SKIN[skin]
    body_top, body_h = 84, 58
    out = []

    # legs
    out.append(f'<rect x="36" y="{body_top+body_h-4}" width="11" height="34" rx="5.5" fill="#3a332e"/>')
    out.append(f'<rect x="53" y="{body_top+body_h-4}" width="11" height="34" rx="5.5" fill="#3a332e"/>')
    # shoes
    out.append(f'<rect x="32" y="{body_top+body_h+26}" width="17" height="10" rx="5" fill="#2b211c"/>')
    out.append(f'<rect x="51" y="{body_top+body_h+26}" width="17" height="10" rx="5" fill="#2b211c"/>')

    # arms
    if arms == "up":
        out.append(f'<rect x="16" y="{body_top-22}" width="13" height="46" rx="6.5" fill="{shirt}" transform="rotate(-24 22 {body_top})"/>')
        out.append(f'<rect x="71" y="{body_top-22}" width="13" height="46" rx="6.5" fill="{shirt}" transform="rotate(24 78 {body_top})"/>')
    else:
        out.append(f'<rect x="19" y="{body_top+4}" width="13" height="46" rx="6.5" fill="{shirt}"/>')
        out.append(f'<rect x="68" y="{body_top+4}" width="13" height="46" rx="6.5" fill="{shirt}"/>')

    # torso
    if adult and not apron:
        out.append(f'<path d="M 32 {body_top} L 68 {body_top} L 76 {body_top+body_h+6} '
                   f'L 24 {body_top+body_h+6} Z" fill="{shirt}"/>')
    else:
        out.append(f'<rect x="30" y="{body_top}" width="40" height="{body_h+6}" rx="15" fill="{shirt}"/>')
    if apron:
        out.append(f'<rect x="38" y="{body_top+8}" width="24" height="{body_h-6}" rx="6" fill="#f7f4ee"/>')

    # neck + head
    out.append(f'<rect x="44" y="{body_top-12}" width="12" height="16" rx="6" fill="{sk}"/>')
    out.append(f'<circle cx="50" cy="46" r="34" fill="{sk}"/>')

    # hair
    if long_hair:
        out.append(f'<path d="M 16 52 Q 14 8 50 8 Q 86 8 84 52 L 84 74 Q 78 44 50 44 '
                   f'Q 22 44 16 74 Z" fill="{hair}"/>')
    else:
        out.append(f'<path d="M 17 46 Q 17 10 50 10 Q 83 10 83 46 Q 72 32 50 32 '
                   f'Q 28 32 17 46 Z" fill="{hair}"/>')

    # eyes
    out.append('<circle cx="38" cy="48" r="4.6" fill="#2b211c"/>')
    out.append('<circle cx="62" cy="48" r="4.6" fill="#2b211c"/>')
    # brows lift the expression
    if mood == "sad":
        out.append('<path d="M 31 38 L 44 42" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
        out.append('<path d="M 69 38 L 56 42" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
    elif mood == "think":
        out.append('<path d="M 31 39 L 44 37" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')

    # mouth
    if mood == "oh":
        out.append('<ellipse cx="50" cy="66" rx="7" ry="9" fill="#8d4a44"/>')
    else:
        out.append(f'<path d="{MOUTHS.get(mood, MOUTHS["smile"])}" stroke="#2b211c" '
                   f'stroke-width="3.6" stroke-linecap="round" fill="none"/>')

    return "".join(out)


def figure(who=None, size=170, mood="smile", arms="down", i=0):
    """A standing person. `who` names a cast member; otherwise an extra keyed by i."""
    if who and who in CAST:
        c = CAST[who]
        shirt, skin, hair = c["shirt"], c["skin"], c["hair"]
        long_hair, adult, apron = c.get("long", False), c.get("adult", False), c.get("apron", False)
    else:
        shirt = EXTRA_SHIRTS[i % len(EXTRA_SHIRTS)]
        skin  = EXTRA_SKIN[(i // 3) % len(EXTRA_SKIN)]
        hair  = ["#2b211c", "#241b17", "#3a2a22"][i % 3]
        long_hair, adult, apron = (i % 3 == 1), False, False

    inner = _person_svg(shirt, skin, hair, mood, long_hair, adult, apron, arms)
    w = round(size * 100 / 175)
    return (f'<svg class="fig" viewBox="0 0 100 175" width="{w}" height="{round(size)}" '
            f'fill="none">{inner}</svg>')


def seated(who=None, i=0, size=64):
    """A person seen seated at a table: head and shoulders only, from the front.

    This is what makes six-at-a-table countable -- each seat holds exactly one of
    these, tucked against the table edge.
    """
    if who and who in CAST:
        c = CAST[who]
        shirt, skin, hair = c["shirt"], c["skin"], c["hair"]
        long_hair = c.get("long", False)
    else:
        shirt = EXTRA_SHIRTS[i % len(EXTRA_SHIRTS)]
        skin  = EXTRA_SKIN[(i // 3) % len(EXTRA_SKIN)]
        hair  = ["#2b211c", "#241b17", "#3a2a22"][i % 3]
        long_hair = (i % 3 == 1)

    hairpath = ('M 16 52 Q 14 10 50 10 Q 86 10 84 52 L 84 70 Q 78 44 50 44 Q 22 44 16 70 Z'
                if long_hair else
                'M 18 48 Q 18 12 50 12 Q 82 12 82 48 Q 71 34 50 34 Q 29 34 18 48 Z')
    return (
        f'<svg class="seat__p" viewBox="0 0 100 108" width="{size}" height="{round(size*108/100)}">'
        f'<rect x="18" y="82" width="64" height="30" rx="15" fill="{shirt}"/>'
        f'<circle cx="50" cy="50" r="34" fill="{SKIN[skin]}"/>'
        f'<path d="{hairpath}" fill="{hair}"/>'
        f'<circle cx="38" cy="52" r="4.4" fill="#2b211c"/>'
        f'<circle cx="62" cy="52" r="4.4" fill="#2b211c"/>'
        f'<path d="M 38 68 Q 50 78 62 68" stroke="#2b211c" stroke-width="3.4" '
        f'stroke-linecap="round" fill="none"/></svg>'
    )
