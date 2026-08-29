# -*- coding: utf-8 -*-
"""Hangul in, speakable Uzbek out.

The sibling of speech.py, and it exists for the same reason. That module's
rule is "never send the engine a digit -- it cannot read Uzbek numerals, so
spell it out first". This one's rule is **never send the engine Hangul**: an
Uzbek voice reads 감사합니다 as silence, so every Korean word becomes
`kamsahamnida` before the text ever reaches it.

It is written once, here, rather than by hand in every spec, because a
transliteration typed twice is a transliteration that will eventually disagree
with itself -- and the screen (which shows real 한글) and the narration (which
must not) are written hours apart.

## Why this is computable at all

Hangul is not spelling, it is a phonetic notation: a syllable's code point is
`0xAC00 + cho*588 + jung*28 + jong`, so decomposing 한 into ㅎ+ㅏ+ㄴ is
arithmetic, not a lookup table. What is NOT arithmetic is the handful of sound
changes Korean applies between syllables -- and those are exactly what makes a
naive letter-swap wrong:

    감사합니다   naive: kamsahapnida     correct: kamsahamnida   (비음화)
    한국어       naive: hankukeo         correct: hangugo        (연음 + voicing)
    학교         naive: hakgyo           correct: hakkyo         (after an obstruent)

The user's own example was *kamsahamnida*, which pins down two of the rules
before a line was written: word-initial ㄱ is **k** (not g), and ㅂ before ㄴ
becomes **m**. The tables below agree with him, and `selftest()` at the bottom
checks it stays that way.

## Two choices that are Uzbek's own luck

Uzbek Latin has the **oʻ / o** pair, and it maps onto Korean's **ㅗ / ㅓ**
almost exactly ([o] vs [ʌ~ɔ]) -- a distinction English romanisation has to
write as "o" and "eo" and which learners then never hear. So 오 is `oʻ` and
어 is `o`, and an Uzbek pupil reading aloud lands much closer than an English
one would.

The one genuine gap is **ㅡ** [ɯ], which Uzbek Latin has no letter for (Cyrillic
would write ы). It is written `u`, colliding with ㅜ. That is deliberate and
cheap: the Hangul is on screen and a native voice says the word aloud, so the
transliteration is a bridge, not the authority. Change `JUNG` if you disagree.
"""

import re

BASE, LAST = 0xAC00, 0xD7A3

CHO = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")
JUNG = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ")
JONG = [""] + list("ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ")

# A final cluster is stored as its two members so that 연음 can move only the
# second one (읽어 -> 일거, not 이겈).
CLUSTER = {"ㄳ": "ㄱㅅ", "ㄵ": "ㄴㅈ", "ㄶ": "ㄴㅎ", "ㄺ": "ㄹㄱ", "ㄻ": "ㄹㅁ",
           "ㄼ": "ㄹㅂ", "ㄽ": "ㄹㅅ", "ㄾ": "ㄹㅌ", "ㄿ": "ㄹㅍ", "ㅀ": "ㄹㅎ",
           "ㅄ": "ㅂㅅ"}

# 7-terminal law: every possible final is heard as one of seven sounds.
TERMINAL = {"ㄱ": "k", "ㄲ": "k", "ㅋ": "k",
            "ㄴ": "n",
            "ㄷ": "t", "ㅌ": "t", "ㅅ": "t", "ㅆ": "t", "ㅈ": "t", "ㅊ": "t", "ㅎ": "t",
            "ㄹ": "l",
            "ㅁ": "m",
            "ㅂ": "p", "ㅍ": "p",
            "ㅇ": "ng"}

# An onset after a vowel or a sonorant is voiced; word-initially or after an
# obstruent it is not. This one rule is most of what separates "hankuk" from
# "hanguk".
ONSET_HARD = {"ㄱ": "k", "ㄲ": "kk", "ㄴ": "n", "ㄷ": "t", "ㄸ": "tt", "ㄹ": "r",
              "ㅁ": "m", "ㅂ": "p", "ㅃ": "pp", "ㅅ": "s", "ㅆ": "ss", "ㅇ": "",
              "ㅈ": "ch", "ㅉ": "ch", "ㅊ": "ch", "ㅋ": "k", "ㅌ": "t", "ㅍ": "p",
              "ㅎ": "h"}
ONSET_SOFT = dict(ONSET_HARD, **{"ㄱ": "g", "ㄷ": "d", "ㅂ": "b", "ㅈ": "j"})

JUNG_UZ = {"ㅏ": "a", "ㅐ": "e", "ㅑ": "ya", "ㅒ": "ye", "ㅓ": "o", "ㅔ": "e",
           "ㅕ": "yo", "ㅖ": "ye", "ㅗ": "oʻ", "ㅘ": "va", "ㅙ": "ve", "ㅚ": "ve",
           "ㅛ": "yoʻ", "ㅜ": "u", "ㅝ": "vo", "ㅞ": "ve", "ㅟ": "vi", "ㅠ": "yu",
           "ㅡ": "u", "ㅢ": "ui", "ㅣ": "i"}

SONORANT = {"n", "m", "ng", "l"}
ASPIRATE = {"ㄱ": "ㅋ", "ㄷ": "ㅌ", "ㅈ": "ㅊ", "ㅂ": "ㅍ"}


def is_hangul(ch):
    return BASE <= ord(ch) <= LAST


def jamo(ch):
    """한 -> ('ㅎ', 'ㅏ', 'ㄴ'). The syllable block, taken apart."""
    if not is_hangul(ch):
        return None
    n = ord(ch) - BASE
    return CHO[n // 588], JUNG[(n % 588) // 28], JONG[n % 28]


def compose(cho, jung, jong=""):
    """('ㅎ','ㅏ','ㄴ') -> 한. The inverse, for building a block on screen."""
    return chr(BASE + CHO.index(cho) * 588 + JUNG.index(jung) * 28 + JONG.index(jong))


def _word(word):
    """One whitespace-delimited Korean word -> Uzbek letters."""
    syls = []
    for ch in word:
        j = jamo(ch)
        if j is None:
            return None
        cho, jung, jong = j
        syls.append([cho, jung, list(CLUSTER.get(jong, jong))])

    # ── the sound changes, in the order Korean applies them ──────────────
    for i in range(len(syls) - 1):
        cur, nxt = syls[i], syls[i + 1]
        tail = cur[2][-1] if cur[2] else ""

        # 격음화 — an obstruent meeting ㅎ, in either order, comes out aspirated.
        if tail == "ㅎ" and nxt[0] in ASPIRATE:
            nxt[0] = ASPIRATE[nxt[0]]
            cur[2] = cur[2][:-1]
            continue
        if nxt[0] == "ㅎ" and tail in ASPIRATE:
            nxt[0] = ASPIRATE[tail]
            cur[2] = cur[2][:-1]
            continue

        # 연음 — a final slides into a following empty onset. ㅎ just vanishes
        # (좋아 -> 조아); anything else becomes the next syllable's onset, and
        # only the LAST member of a cluster moves. A final ㅇ is exempt: it is
        # already the sound [ng], not a consonant waiting for a vowel, and
        # letting it move turned 훈민정음 into "hunminjoum".
        if nxt[0] == "ㅇ" and cur[2] and cur[2][-1] != "ㅇ":
            moved = cur[2].pop()
            if moved != "ㅎ":
                nxt[0] = moved
            continue

    # The remaining rules read finals as SOUNDS, so reduce them first.
    finals = []
    for s in syls:
        finals.append(TERMINAL.get(s[2][-1], "") if s[2] else "")

    for i in range(len(syls) - 1):
        f, nxt = finals[i], syls[i + 1]
        # 비음화 — a stop before a nasal turns into the nasal made in the same
        # place. This is the rule in his own example: 합 + 니 -> ham-ni.
        if nxt[0] in ("ㄴ", "ㅁ"):
            finals[i] = {"k": "ng", "t": "n", "p": "m"}.get(f, f)
        # 유음화 — ㄴ and ㄹ meeting each other both come out ㄹ (신라 -> silla).
        elif f == "n" and nxt[0] == "ㄹ":
            finals[i] = "l"
        elif f == "l" and nxt[0] == "ㄴ":
            nxt[0] = "ㄹ"

    # ── letters ─────────────────────────────────────────────────────────
    out, prev = [], ""      # prev = the sound immediately before this onset
    for i, (cho, jung, _c) in enumerate(syls):
        soft = prev != "" and (prev == "V" or prev in SONORANT)
        if cho == "ㄹ" and prev == "l":
            out.append("l")                      # 빨리 -> ppalli
        else:
            out.append((ONSET_SOFT if soft else ONSET_HARD)[cho])
        out.append(JUNG_UZ[jung])
        f = finals[i]
        out.append(f)
        prev = f if f else "V"
    return "".join(out)


def uz(text):
    """Any Korean text -> the Uzbek letters an Uzbek voice should read."""
    return " ".join(_word(w) or w for w in str(text).split())


_RUN = re.compile(r"[가-힣]+(?:\s+[가-힣]+)*")


def romanise_all(text):
    """Replace every Hangul run in a mixed string with its transliteration.

    This is what speech.py calls, so a spec's `say` line can be written with
    the real word in it and the narration still reaches the engine in Uzbek.
    """
    return _RUN.sub(lambda m: uz(m.group(0)), text)


def has_hangul(text):
    return bool(re.search(r"[가-힣]", text or ""))


# ── the cases that were got wrong before the rules above existed ──────────
CASES = [
    ("감사합니다", "kamsahamnida"),   # 비음화 — his own example, the reference
    ("한국어",     "hangugo"),        # 연음 + voicing after a sonorant
    ("학교",       "hakkyoʻ"),        # onset stays hard after an obstruent
    ("출구",       "chulgu"),         # ㅊ onset, ㄹ final, voiced ㄱ after it
    ("출발",       "chulbal"),
    ("수출",       "suchul"),
    ("안녕하세요", "annyonghaseyoʻ"),
    ("신라",       "silla"),          # 유음화
    ("빨리",       "ppalli"),
    ("좋아요",     "choʻayoʻ"),       # ㅎ drops into an empty onset
    ("읽어요",     "ilgoyoʻ"),        # only the cluster's second member moves
    ("입니다",     "imnida"),
    ("있다",       "itta"),
    ("세종",       "sejoʻng"),        # ㅈ between vowels is voiced
    ("훈민정음",   "hunminjongum"),   # the final ㅇ must not move
]


def selftest():
    bad = [(k, want, uz(k)) for k, want in CASES if uz(k) != want]
    for k, want, got in bad:
        print(f"  {k}: kutilgan {want!r}, chiqdi {got!r}")
    print(f"korean.py: {len(CASES) - len(bad)}/{len(CASES)} ok")
    return len(bad)


if __name__ == "__main__":
    raise SystemExit(selftest())
