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
    # Same figure under a capitalised key. `says` never prints the name, so the
    # lowercase role was fine until ko17 gave the waiter a `consequence` beat --
    # which DOES print it, as a title under the spotlight. Renaming the original
    # key would have changed pm04, so this is an alias, not a move.
    "Ofitsiant":  {"shirt": "#2f3a44", "skin": "m", "hair": "#241b17", "adult": True, "apron": True},
    # Grandparents, added 2026-08-29 for PM-91 (buvijonning kompoti) and PM-93
    # (bobo va nevara). Grey hair is the only thing that reads as "old" at this
    # size -- the figure itself is the same, so nothing else needed changing.
    "Buvijon":    {"shirt": "#7f8f9c", "skin": "l", "hair": "#b9b2ab", "long": True, "adult": True},
    "Bobo":       {"shirt": "#6d7f6a", "skin": "m", "hair": "#c2bcb4", "adult": True},
    # PM-97 uchun — u ham hisobga kiradi: 0 ta soch.
    "Kal aka":    {"shirt": "#c98a3e", "skin": "m", "hair": "#241b17",
                   "adult": True, "bald": True},
    # MO-10 uchun: toʻqqiz yashar bola va uning oʻqituvchisi.
    "Gauss":       {"shirt": "#4a6fa5", "skin": "l", "hair": "#c9a227"},
    "Oʻqituvchi":  {"shirt": "#5b5147", "skin": "l", "hair": "#6b6259",
                    "adult": True},

    # ── Matematika olami: tarixiy siymolar ──
    # Salla va soqol — bitta figurada oʻn ikki asr farqni koʻrsatadigan yagona narsa.
    "Al-Xorazmiy": {"shirt": "#3f6f8f", "skin": "m", "hair": "#241b17", "adult": True,
                    "turban": "#c3b394", "beard": "#3a2f28"},
    "Beruniy":     {"shirt": "#6d8f6a", "skin": "m", "hair": "#241b17", "adult": True,
                    "turban": "#aebfa6", "beard": "#4a3d34"},
    "Ulugʻbek":    {"shirt": "#7a5aa0", "skin": "l", "hair": "#241b17", "adult": True,
                    "turban": "#c2b2d2", "beard": "#3a2f28"},
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
    # ── 2026-09-22: the three moods SERIES.md §6 asked for ──────────────
    # The answer to "can we drop reaction GIFs in" was "no to a stranger's
    # meme face, yes to our own cast reacting". That only pays off if the
    # cast can actually react, and five moods could not: `sad` is
    # disappointment, not shock, and nothing in the set laughed.
    "shock":  None,          # a taller ellipse, like `oh` but wider-eyed
    "cross":  "M 37 70 L 63 70",         # a hard flat line under angry brows
}

# A laugh is not an `oh` with different eyes: an open OVAL reads as a shout.
# What reads as laughing is a mouth with a FLAT TOP and a deep round bottom --
# the upper lip pulled back over the teeth. Drawn filled rather than stroked,
# for the same reason the tongue in `mouth()` is filled: an outline inside an
# outline is unreadable at arm's length.
LAUGH_MOUTH = "M 34 60 L 66 60 A 16 15 0 0 1 34 60 Z"

# Which moods open the mouth, and how big. `oh` is the original surprise; the
# 2026-09-22 additions keep the same drawing and only change the size, because
# what reads as shock at 340px is the EYES, not the mouth.
_OPEN = {"oh": (7, 9), "shock": (10, 13)}


def _person_svg(shirt, skin, hair, mood="smile", long_hair=False, adult=False,
                apron=False, arms="down", bald=False, turban=None, beard=None):
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

    # beard -- drawn before the eyes and mouth so they sit on top of it
    if beard:
        out.append(f'<path d="M 19 48 Q 16 95 50 95 Q 84 95 81 48 Q 78 78 50 78 '
                   f'Q 22 78 19 48 Z" fill="{beard}"/>')

    # hair -- or, for PM-97's joke, none at all. A bald head is not just a gag
    # there: it is the reason the count is 200 001 and not 200 000, because 0 is
    # a legitimate number of hairs. So he gets a small shine instead of hair.
    if turban:
        # Salla: hair's shape, but taller and wider, with a wrap line and a knot.
        # This is what makes the Matematika olami history films read as history
        # at a glance -- the same figure, eight centuries earlier.
        # A turban is WIDER than the head and sits above the brow. The first
        # attempt was a hair-shaped dome and read as a beanie; a wide low ellipse
        # plus a wrap line and a top knot is what makes it legible at 300px.
        # Keep the whole shape INSIDE the 0..175 viewBox -- an <svg> clips to it,
        # and a taller ellipse came out flat-topped. Wrap lines are inset so
        # their round caps do not poke past the fabric.
        out.append(f'<ellipse cx="50" cy="25" rx="45" ry="21" fill="{turban}"/>')
        out.append(f'<path d="M 13 27 Q 50 45 87 27" stroke="#00000026" '
                   f'stroke-width="7" fill="none" stroke-linecap="round"/>')
        out.append(f'<path d="M 13 17 Q 50 33 87 17" stroke="#00000018" '
                   f'stroke-width="6" fill="none" stroke-linecap="round"/>')
    elif bald:
        out.append(f'<ellipse cx="42" cy="26" rx="11" ry="6" fill="#ffffff" '
                   f'opacity="0.30" transform="rotate(-18 42 26)"/>')
    elif long_hair:
        out.append(f'<path d="M 16 52 Q 14 8 50 8 Q 86 8 84 52 L 84 74 Q 78 44 50 44 '
                   f'Q 22 44 16 74 Z" fill="{hair}"/>')
    else:
        out.append(f'<path d="M 17 46 Q 17 10 50 10 Q 83 10 83 46 Q 72 32 50 32 '
                   f'Q 28 32 17 46 Z" fill="{hair}"/>')

    out.append(face(mood))

    return "".join(out)


def face(mood="smile"):
    """Eyes, brows and mouth, in the 100x175 figure's own coordinates.

    Pulled out of `_person_svg` on 2026-09-22 so `head()` can draw the SAME
    face -- a reaction shot and the standing figure it belongs to must not be
    two different people. Every pre-existing mood renders byte-identically to
    what was inline before; the new ones are new branches only.
    """
    out = []
    # eyes -- `shock` widens them, `laugh` closes them into arcs. This is the
    # part that actually carries the expression at reaction size.
    if mood == "laugh":
        # Kept at y 45..52: the long-hair fringe comes down to y=44 at the
        # centre, so an arc drawn any higher is simply painted over -- which is
        # exactly what happened to Afsona on ko19's first contact sheet.
        out.append('<path d="M 32 52 Q 38 45 44 52" stroke="#2b211c" stroke-width="3.8" '
                   'stroke-linecap="round" fill="none"/>')
        out.append('<path d="M 56 52 Q 62 45 68 52" stroke="#2b211c" stroke-width="3.8" '
                   'stroke-linecap="round" fill="none"/>')
    elif mood == "shock":
        out.append('<circle cx="38" cy="48" r="7.4" fill="#fff" stroke="#2b211c" stroke-width="2.4"/>')
        out.append('<circle cx="62" cy="48" r="7.4" fill="#fff" stroke="#2b211c" stroke-width="2.4"/>')
        out.append('<circle cx="38" cy="48" r="3.6" fill="#2b211c"/>')
        out.append('<circle cx="62" cy="48" r="3.6" fill="#2b211c"/>')
    else:
        out.append('<circle cx="38" cy="48" r="4.6" fill="#2b211c"/>')
        out.append('<circle cx="62" cy="48" r="4.6" fill="#2b211c"/>')

    # brows lift the expression
    if mood == "sad":
        out.append('<path d="M 31 38 L 44 42" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
        out.append('<path d="M 69 38 L 56 42" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
    elif mood == "think":
        out.append('<path d="M 31 39 L 44 37" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
    elif mood == "cross":
        # Angry is the mirror of sad: the inner ends come DOWN, not up.
        out.append('<path d="M 31 36 L 44 42" stroke="#2b211c" stroke-width="3.8" stroke-linecap="round" fill="none"/>')
        out.append('<path d="M 69 36 L 56 42" stroke="#2b211c" stroke-width="3.8" stroke-linecap="round" fill="none"/>')
    elif mood == "shock":
        out.append('<path d="M 30 33 Q 38 28 46 32" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')
        out.append('<path d="M 70 33 Q 62 28 54 32" stroke="#2b211c" stroke-width="3.4" stroke-linecap="round" fill="none"/>')

    # mouth
    if mood == "laugh":
        out.append(f'<path d="{LAUGH_MOUTH}" fill="#8d4a44"/>')
    elif mood in _OPEN:
        rx, ry = _OPEN[mood]
        out.append(f'<ellipse cx="50" cy="66" rx="{rx}" ry="{ry}" fill="#8d4a44"/>')
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
        bald = c.get("bald", False)
        turban, beard = c.get("turban"), c.get("beard")
    else:
        shirt = EXTRA_SHIRTS[i % len(EXTRA_SHIRTS)]
        skin  = EXTRA_SKIN[(i // 3) % len(EXTRA_SKIN)]
        hair  = ["#2b211c", "#241b17", "#3a2a22"][i % 3]
        long_hair, adult, apron = (i % 3 == 1), False, False
        bald = False
        turban = beard = None

    inner = _person_svg(shirt, skin, hair, mood, long_hair, adult, apron, arms,
                        bald, turban, beard)
    w = round(size * 100 / 175)
    return (f'<svg class="fig" viewBox="0 0 100 175" width="{w}" height="{round(size)}" '
            f'fill="none">{inner}</svg>')


def head(who=None, size=340, mood="smile", i=0):
    """Head and shoulders, close up -- the reaction shot.

    `figure` draws a whole body, so at reaction size the face is a tenth of it
    and the expression is lost. This crops the SAME drawing to the head, in the
    same coordinates, so the boy who was standing in the previous scene is
    recognisably the boy filling the frame in this one.

    SERIES.md §6: the answer to "can we drop a viral reaction GIF in" was no --
    his own cast, on his own paper, in his own colours. This is the thing that
    was supposed to replace it, finally built (2026-09-22).
    """
    if who and who in CAST:
        c = CAST[who]
        shirt, skin, hair = c["shirt"], c["skin"], c["hair"]
        long_hair = c.get("long", False)
        bald, turban, beard = c.get("bald", False), c.get("turban"), c.get("beard")
    else:
        shirt = EXTRA_SHIRTS[i % len(EXTRA_SHIRTS)]
        skin  = EXTRA_SKIN[(i // 3) % len(EXTRA_SKIN)]
        hair  = ["#2b211c", "#241b17", "#3a2a22"][i % 3]
        long_hair, bald, turban, beard = (i % 3 == 1), False, None, None

    sk = SKIN[skin]
    out = [f'<rect x="4" y="84" width="92" height="34" rx="16" fill="{shirt}"/>',
           f'<circle cx="50" cy="46" r="34" fill="{sk}"/>']
    if beard:
        out.append(f'<path d="M 19 48 Q 16 95 50 95 Q 84 95 81 48 Q 78 78 50 78 '
                   f'Q 22 78 19 48 Z" fill="{beard}"/>')
    if turban:
        out.append(f'<ellipse cx="50" cy="25" rx="45" ry="21" fill="{turban}"/>')
        out.append('<path d="M 13 27 Q 50 45 87 27" stroke="#00000026" '
                   'stroke-width="7" fill="none" stroke-linecap="round"/>')
    elif bald:
        out.append('<ellipse cx="42" cy="26" rx="11" ry="6" fill="#ffffff" '
                   'opacity="0.30" transform="rotate(-18 42 26)"/>')
    elif long_hair:
        # The fringe is LIFTED here (it dips to y=34, not 44) and only here. On
        # the standing figure a low fringe is invisible at 170px; at 430px it
        # sits straight on the eyes and the brows disappear into it -- Nodira
        # opa's angry close-up on ko21's first contact sheet came out a dark
        # blob with a mouth. The silhouette, which is what says "long hair", is
        # unchanged, so she is still recognisably the same person.
        out.append(f'<path d="M 16 52 Q 14 8 50 8 Q 86 8 84 52 L 84 74 Q 78 34 50 34 '
                   f'Q 22 34 16 74 Z" fill="{hair}"/>')
    else:
        out.append(f'<path d="M 17 46 Q 17 10 50 10 Q 83 10 83 46 Q 72 30 50 30 '
                   f'Q 28 30 17 46 Z" fill="{hair}"/>')
    out.append(face(mood))
    # The crop is the whole point: head from y=12 to y=80, plus a slice of
    # shoulder. A looser box gives back exactly the problem `figure` already
    # had -- a small face in a large frame.
    return (f'<svg class="fig" viewBox="10 4 80 96" width="{round(size * 80 / 96)}" '
            f'height="{round(size)}" fill="none">{"".join(out)}</svg>')


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
