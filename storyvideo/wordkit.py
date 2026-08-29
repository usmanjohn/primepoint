# -*- coding: utf-8 -*-
"""The language kit — what primitives.py is to a maths story.

The maths videos work because the picture makes the argument: a counter counts
the actual dots, a bar grows, a wrong answer is struck through. Nothing here
is decoration either. A language has its own countable structure, and these are
the four pieces of it worth drawing:

  `pron`    one word, three lines -- 한글, how to say it, what it means. The
            transliteration comes from korean.py, so it cannot disagree with
            what the narration says.
  `family`  a root and everything it unlocks. 출(出) gives 출구·출근·출발·
            출석·제출·수출·외출·출입·지출 -- nine words from one syllable, and
            nine is a QUANTITY, so it is counted by the same counter machinery
            that counts chairs. This is the direct translation of the maths
            format into a language.
  `jamo`    ㅎ + ㅏ + ㄴ → 한. The one animation in the kit that is a mechanism
            rather than an arrival: a syllable block being built.
  `mouth`   why a letter is shaped the way it is. ㄱ is the tongue humped at
            the back of the mouth; the letter is a picture of that.

`pron` and `family` are language-agnostic on purpose -- an English root
(`spect` → inspect · spectator · perspective · prospect) uses the same two
builders with `hanja=None`. Only `jamo` and `mouth` are Korean.
"""

import korean as _ko


def _t(at):
    return f'data-at="{at:.3f}"'


# ────────────────────────────────────────────────────────── word card ──
def pron(word, gloss=None, uz=None, hanja=None, at=0.0, dur=0.55, step=0.45,
         size=None, speak=False):
    """One word, held: the script, the pronunciation, the meaning.

    `uz` is normally left out -- korean.py derives it, which is the whole point
    of that module. Pass it only to override a word the rules get wrong.

    `speak=True` marks the card for koaudio.py, which lays a native Korean
    voice over it. Only do that in a scene with no narration of its own -- a
    Korean word mixed under the Uzbek voice is mud. See `scenes.echo`.
    """
    say = uz or (_ko.uz(word) if _ko.has_hangul(word) else None)
    rows = []
    style = f' style="font-size:{size}px"' if size else ""
    spk = f' data-say-ko="{word}"' if speak else ""
    rows.append(f'<div class="pron__k"{style}{spk} {_t(at)} data-dur="{dur}" '
                f'data-anim="pop">{word}</div>')
    if hanja:
        rows.append(f'<div class="pron__h" {_t(at + step * 0.6)} data-dur="0.4" '
                    f'data-anim="fade">{hanja}</div>')
    if say:
        rows.append(f'<div class="pron__u" {_t(at + step)} data-dur="0.45" '
                    f'data-anim="rise">{say}</div>')
    if gloss:
        rows.append(f'<div class="pron__g" {_t(at + step * 2)} data-dur="0.45" '
                    f'data-anim="rise">{gloss}</div>')
    return f'<div class="pron">{"".join(rows)}</div>'


# ───────────────────────────────────────────────────────── root family ──
def root_card(syllable, hanja=None, meaning=None, at=0.0, dur=0.6):
    rows = [f'<div class="root__k">{syllable}</div>']
    if hanja:
        rows.append(f'<div class="root__h">{hanja}</div>')
    if meaning:
        rows.append(f'<div class="root__m">{meaning}</div>')
    return (f'<div class="root" {_t(at)} data-dur="{dur}" data-anim="pop">'
            f'{"".join(rows)}</div>')


def family(words, root=None, at=0.0, step=0.5, cols=2):
    """The words a root unlocks, dealt out one at a time.

    words: [(word, hanja_or_None, gloss), ...]

    Each word appears as its own element, so the counter beside them can count
    `.fam__w` and be a readout of the picture rather than a second animation
    running next to it -- the countability rule, unchanged from the maths kit.
    The shared syllable is the only coloured letter in each word, because it is
    the only reason the list is a list and not nine unrelated words.

    Returns (html, seconds).
    """
    cells = []
    for i, w in enumerate(words):
        word, hanja, gloss = (list(w) + [None, None])[:3]
        shown = word
        if root and root in word:
            # Colour the shared syllable, once, so the eye finds it instantly.
            shown = word.replace(root, f"<em>{root}</em>", 1)
        bits = [f"<b>{shown}</b>"]
        if hanja:
            bits.append(f"<i>{hanja}</i>")
        if gloss:
            bits.append(f"<span>{gloss}</span>")
        cells.append(f'<div class="fam__w" {_t(at + i * step)} data-dur="0.34" '
                     f'data-anim="pop">{"".join(bits)}</div>')
    html = f'<div class="fam" style="--fcols:{cols}">{"".join(cells)}</div>'
    return html, len(words) * step


# ──────────────────────────────────────────────── syllable assembly ──
_VOWELS = set("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")


def jamo(syllable, at=0.0, step=0.7, show_uz=True):
    """ㅎ + ㅏ + ㄴ → 한, built in front of the viewer.

    Korean writing is not spelling, it is a diagram of a syllable, and that is
    invisible to somebody who has only ever seen it as a wall of shapes. So the
    block is taken apart and put back together: consonants blue, vowels gold,
    the finished block gold-filled.

    Returns (html, seconds).
    """
    parts = _ko.jamo(syllable)
    if parts is None:
        raise ValueError(f"{syllable!r} is not one Hangul syllable")
    pieces = [p for p in parts if p]
    out, i = [], 0
    for k, p in enumerate(pieces):
        if k:
            out.append(f'<span class="jamo__op" {_t(at + i * step - 0.1)} '
                       f'data-dur="0.3" data-anim="fade">+</span>')
        cls = "jamo__l--v" if p in _VOWELS else "jamo__l--c"
        out.append(f'<span class="jamo__l {cls}" {_t(at + i * step)} '
                   f'data-dur="0.4" data-anim="pop">{p}</span>')
        i += 1
    out.append(f'<span class="jamo__op" {_t(at + i * step - 0.1)} data-dur="0.3" '
               f'data-anim="fade">→</span>')
    out.append(f'<span class="jamo__out" {_t(at + i * step)} data-dur="0.5" '
               f'data-anim="pop">{syllable}</span>')
    html = f'<div class="jamo">{"".join(out)}</div>'
    secs = (i + 1) * step
    if show_uz:
        html += (f'<div class="pron__u" {_t(at + secs + 0.2)} data-dur="0.45" '
                 f'data-anim="rise">{_ko.uz(syllable)}</div>')
        secs += 0.7
    return html, secs


# ───────────────────────────────────────────────────── mouth diagram ──
# A head in profile, facing left, with the mouth open and the TONGUE IN THE
# POSITION THE SOUND IS MADE IN. The first version drew the mouth as a duct
# with the five places marked along it; on a contact sheet it read as a sofa.
# What makes a drawing read as a mouth is the silhouette -- a nose and a chin --
# and what makes it teach anything is that the tongue MOVES between zones. So
# each zone carries its own tongue path, and the articulator that closes is the
# only gold thing on screen.
#
# 훈민정음 해례본 (1446) is the source for every claim these make: ㄱ "depicts
# the tongue root blocking the throat", ㄴ "the tongue touching the upper
# palate", ㅁ "the shape of the mouth", ㅅ "the shape of a tooth", ㅇ "the shape
# of the throat". The diagram is the argument, not an illustration beside it.

# The silhouette is CLOSED — the back of the head comes round to the crown.
# Left open, the two lines simply stopped in mid-air on the right and the
# drawing read as unfinished rather than as a head seen from the side.
_FACE = ("M440,60 C330,46 190,72 150,160 C144,182 138,206 128,224 "
         "L78,286 L126,306 C114,318 110,324 114,332 L140,344 L112,364 "
         "C116,388 128,404 150,418 C200,452 330,482 430,476 "
         "C512,470 556,384 552,278 C548,168 516,74 440,60 Z")
# The cavity lives entirely between the lips and the jaw line. In the first
# pass it did not, and the chin curve ran straight through the tongue.
_PALATE = "M148,330 C215,312 300,310 358,322 C382,328 394,342 397,362"
_THROAT = "M398,364 L400,412"

# One tongue per place of articulation. The floor of the mouth is the same in
# all of them; only the body of the tongue changes shape, because that IS the
# difference between the sounds.
_TONGUE = {
    "lab":  "M150,368 C215,360 290,364 355,378 C378,384 390,392 394,402 L152,402 Z",
    "dent": "M148,344 C176,338 214,358 262,372 C312,384 358,392 394,400 L394,402 L152,402 Z",
    "alv":  "M150,334 C180,328 208,352 256,368 C306,382 356,388 394,398 L394,402 L152,402 Z",
    "vel":  "M150,376 C215,370 275,356 322,336 C352,324 380,342 394,372 L394,402 L152,402 Z",
    "glot": "M150,368 C215,360 290,364 355,378 C378,384 390,392 394,402 L152,402 Z",
}

# What lights up gold: the thing that actually closes or narrows. Each one is
# drawn on the same coordinates as the part beneath it, so it overlays the face
# instead of floating beside it.
_HOT = {
    "lab":  "M114,332 L140,344 L112,364 M120,346 L162,346",
    "dent": "M150,326 L150,352",
    "alv":  "M156,322 C174,316 194,320 206,330",
    "vel":  "M330,320 C360,316 386,334 396,362",
    "glot": "M398,366 L400,414",
}

_ZONES = {
    "lab":  ("lablar",     "ㅁ ㅂ ㅍ"),
    "dent": ("tishlar",    "ㅅ ㅈ ㅊ"),
    "alv":  ("til uchi",   "ㄴ ㄷ ㅌ ㄹ"),
    "vel":  ("til orqasi", "ㄱ ㅋ"),
    "glot": ("boʻgʻiz",    "ㅇ ㅎ"),
}
_ZONE_ORDER = list(_ZONES)


def mouth(zone, at=0.0, dur=0.6, label=True):
    """The mouth in profile with one place of articulation closed.

    zone: lab | dent | alv | vel | glot
    """
    if zone not in _ZONES:
        raise ValueError(f"unknown zone {zone!r} — {', '.join(_ZONE_ORDER)}")
    name, letters = _ZONES[zone]

    txt = ""
    if label:
        # The head's jaw reaches y~482, so the letters sit well below it. At
        # y=530 in a 560 box they printed straight over the chin.
        txt = (f'<text class="m-lbl" x="310" y="46" text-anchor="middle" '
               f'{_t(at + 0.15)} data-dur="0.4" data-anim="fade">{name}</text>'
               f'<text class="m-ko" x="310" y="598" text-anchor="middle" '
               f'{_t(at + 0.45)} data-dur="0.45" data-anim="fade">{letters}</text>')

    return (f'<svg class="mouthfig" viewBox="0 0 620 620">'
            f'<path class="m-face" d="{_FACE}"/>'
            f'<path class="m-tongue" d="{_TONGUE[zone]}" {_t(at)} '
            f'data-dur="{dur}" data-anim="fade"/>'
            f'<path class="m-cav" d="{_PALATE}"/>'
            f'<path class="m-cav" d="{_THROAT}"/>'
            f'<path class="m-hot" d="{_HOT[zone]}" {_t(at + 0.25)} '
            f'data-dur="{dur}" data-anim="fade"/>'
            f'{txt}</svg>')


# ─────────────────────────────────────────────────────────── endcard ──
def cta(title, sub=None, at=0.0, dur=0.55):
    rows = [f'<div class="cta__t">{title}</div>']
    if sub:
        rows.append(f'<div class="cta__s">{sub}</div>')
    return (f'<div class="cta" {_t(at)} data-dur="{dur}" data-anim="pop">'
            f'{"".join(rows)}</div>')


def say_again(word, at, dur=1.2):
    """A second utterance of a word already on screen.

    Nothing to draw -- the card is still there -- so this is a marker element
    with no size, which the layout gate ignores and `settle_of` still counts,
    so the scene is long enough to hold the word twice.
    """
    return (f'<span data-say-ko="{word}" {_t(at)} data-dur="{dur}" '
            f'style="display:none"></span>')


# ─────────────────────────────────────────────── word order comparison ──
# The strongest thing an Uzbek-language Korean channel can say, and nobody
# says it: Uzbek and Korean build a sentence the same way and English does not.
# Uzbek `kitob-NI oʻqiyman` is Korean `책-을 읽어요` word for word -- same
# order, same postposition-after-the-word, verb last. English puts the verb in
# the middle.
#
# It only lands if the words ALIGN IN COLUMNS. Laid out as free-flowing rows
# the reader has to compare three ragged lines by reading them; on a fixed
# three-column grid the colours simply do not line up on the English row, and
# the argument is made before a word of narration.
_ROLE = {"s": "ord__w--s", "o": "ord__w--o", "v": "ord__w--v"}


def order_strip(rows, at=0.0, step=0.9, inner=0.18):
    """rows: [(label, [(text, role), ...], is_korean), ...]  role in s|o|v.

    Returns (html, seconds).
    """
    out = []
    for i, row in enumerate(rows):
        label, cells, *rest = row
        ko = rest[0] if rest else False
        t0 = at + i * step
        chips = "".join(
            f'<span class="ord__w {_ROLE.get(role, "")}{" ko" if ko else ""}" '
            f'{_t(t0 + j * inner)} data-dur="0.34" data-anim="pop">{txt}</span>'
            for j, (txt, role) in enumerate(cells))
        out.append(f'<div class="ord__g">'
                   f'<span class="ord__lbl" {_t(t0 - 0.15)} data-dur="0.3" '
                   f'data-anim="fade">{label}</span>'
                   f'<div class="ord__row">{chips}</div></div>')
    return f'<div class="ord">{"".join(out)}</div>', len(rows) * step


# ──────────────────────────────────────────────────────── pair mapping ──
def pair_rows(pairs, at=0.0, step=0.6):
    """[(korean, uzbek_equivalent), ...] -- the qoʻshimcha ↔ 조사 table.

    Returns (html, seconds).
    """
    out = []
    for i, (ko, uz_) in enumerate(pairs):
        out.append(f'<div class="pair" {_t(at + i * step)} data-dur="0.36" '
                   f'data-anim="pop"><b>{ko}</b><i>=</i><span>{uz_}</span></div>')
    return f'<div class="pairs">{"".join(out)}</div>', len(pairs) * step
