# -*- coding: utf-8 -*-
"""Turning a spec into text a TTS engine reads correctly.

The engine's mistakes are nearly all OUR mistakes: given "18" it guesses, given
"oʻn sakkiz" it cannot. Given "÷" it says nothing useful. So every number is
spelled out in Uzbek words here and every symbol is replaced by the word a
teacher would actually say, before the text ever reaches the engine.

⚠️ The number words below are generated, not reviewed by a native speaker.
Check them once; after that they are right forever.
"""

import re

import korean

ONES = ["nol", "bir", "ikki", "uch", "toʻrt", "besh", "olti", "yetti", "sakkiz", "toʻqqiz"]
TENS = ["", "oʻn", "yigirma", "oʻttiz", "qirq", "ellik", "oltmish", "yetmish",
        "sakson", "toʻqson"]
SCALES = [(1_000_000_000, "milliard"), (1_000_000, "million"), (1_000, "ming")]


def uz_number(n):
    """37 -> 'oʻttiz yetti'.  18750 -> 'oʻn sakkiz ming yetti yuz ellik'."""
    n = int(n)
    if n < 0:
        return "minus " + uz_number(-n)
    if n < 10:
        return ONES[n]
    if n < 100:
        t, o = divmod(n, 10)
        return TENS[t] + ((" " + ONES[o]) if o else "")
    if n < 1000:
        h, r = divmod(n, 100)
        head = ("bir" if h == 1 else ONES[h]) + " yuz"
        return head + ((" " + uz_number(r)) if r else "")
    for value, name in SCALES:
        if n >= value:
            head, rest = divmod(n, value)
            # "ming" alone, not "bir ming"
            lead = "" if (head == 1 and name == "ming") else uz_number(head) + " "
            out = f"{lead}{name}"
            return out + ((" " + uz_number(rest)) if rest else "")
    return str(n)


def uz_ordinal(n):
    """1443 -> 'ming toʻrt yuz qirq uchinchi'  ·  1997 -> '... toʻqson yettinchi'.

    Uzbek takes -nchi after a vowel and -inchi after a consonant. Appending
    -inchi to everything is right for toʻrt/uch/sakkiz and WRONG for the four
    number words that end in a vowel -- ikki, olti, yetti, yigirma -- which came
    out as "yettiinchi". Caught in ko02's closing line about 1997.
    """
    w = uz_number(n)
    return w + ("nchi" if w[-1] in "aeiou" else "inchi")


def uz_decimal(whole, frac):
    """0,4 -> 'nol butun oʻndan toʻrt'  ·  3,75 -> 'uch butun yuzdan yetmish besh'."""
    place = {1: "oʻndan", 2: "yuzdan", 3: "mingdan",
             4: "oʻn mingdan"}.get(len(frac), "oʻndan")
    return f"{uz_number(whole)} butun {place} {uz_number(int(frac))}"


# Symbols a teacher says out loud, longest first so ÷ never survives as "÷".
SYMBOLS = [
    ("%", " foiz"), ("×", " koʻpaytiriladi "), ("÷", " boʻlinadi "),
    ("≈", " taxminan "), ("=", " teng "), ("−", " minus "), ("–", " minus "),
    ("+", " qoʻshuv "), ("→", " demak "), ("«", ""), ("»", ""),
    ("—", ", "), ("·", ", "),
]


# Authoring marks used inside a `say` line. They survive the whole normalisation
# below untouched (no regex here looks at * or |), and become SSML at the end --
# or vanish, when the engine has no SSML.
#   *word*   emphasis
#   ||       a beat inside a scene
#   |        a short breath
# Widened 2026-08-29. At his +26% speed the engine does NOT scale <break> times,
# so a 0.7s beat plus its sentence-final pause reached 1.97s -- within 0.1s of a
# real 1.5s scene break, which is what made the re-split fragile. Pushing the
# scene break up and the inner ones down separates them unmistakably. Costs no
# video length: the boundary silence is discarded when the clip is cut.
SCENE_BREAK = "2.5s"      # long enough to be unmistakable when re-splitting
INNER_BREAK = "0.45s"
SHORT_BREAK = "0.3s"

# NOTE (user, 2026-08-29): narration carries NO trailing speech tags -- no
# "dedi", no "dedi u". Who is speaking is already on screen, so the words are
# spoken straight. A leading narrative verb ("Donishmand shundan soʻradi:") is
# fine; it introduces the speech instead of trailing it.


def for_tts(text, ssml=False):
    """Prose in, speakable Uzbek out."""
    # Superscripts must become words BEFORE markup is stripped, or 2<sup>7</sup>
    # collapses to a meaningless "ikki yetti".
    s = re.sub(r"<sup>(.*?)</sup>", r" darajali \1 ", text)
    s = re.sub(r"<[^>]+>", " ", s)             # any other stray markup
    s = s.replace(" ", " ")
    # Korean is spelled out for exactly the same reason numbers are: the
    # engine is an Uzbek voice and reads 한글 as silence. A spec writes the real
    # word once and it reaches the picture as Hangul and the engine as Uzbek.
    s = korean.romanise_all(s)

    # Join thousands spaces first: "25 000" is one number, not two.
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"(?<=\d) (?=\d{3}\b)", "", s)

    # Case suffixes attach to the number they follow.
    SUFFIX = "dan|gacha|dagi|daги|ga|da|ni|ning|ta|tadan|tasi|inchi|nchi"
    s = re.sub(rf"\b(\d+)\s+({SUFFIX})\b", r"\1\2", s)

    for a, b in SYMBOLS:
        s = s.replace(a, b)

    # Times: 8:36 -> "soat sakkiz-u oʻttiz olti", without doubling an existing "soat"
    s = re.sub(r"(?i)(soat\s+)?\b(\d{1,2}):(\d{2})\b",
               lambda m: (m.group(1) or "soat ") +
                         f"{uz_number(m.group(2))}-u {uz_number(m.group(3))}", s)
    # Decimals with a comma
    s = re.sub(r"\b(\d+),(\d+)\b", lambda m: uz_decimal(m.group(1), m.group(2)), s)
    # Ordinal-ish "8-katak" -> "sakkizinchi katak"
    s = re.sub(r"\b(\d+)-(\w)",
                lambda m: f"{uz_ordinal(m.group(1))} {m.group(2)}", s)
    # Everything else
    s = re.sub(r"\d+", lambda m: uz_number(m.group(0)), s)

    # Units, once the digits around them are words
    for a, b in [("kg", "kilogramm"), ("km", "kilometr"), ("sm", "santimetr"),
                 ("mm", "millimetr"), ("g", "gramm"), ("m", "metr"), ("l", "litr")]:
        s = re.sub(rf"\b{a}\b", b, s)

    # "bir" + "ta" is the one irregular counter in Uzbek: 51 ta is "ellik
    # bitta", never "ellik birta". Every other number just concatenates.
    s = re.sub(r"\bbirta\b", "bitta", s)

    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.!?])", r"\1", s)
    s = s.strip()
    # Recapitalise: expanding "25 foiz" mid-rewrite can leave a clause lowercase.
    s = re.sub(r"(^|[.!?]\s+)([a-zoʻgʻ])",
               lambda m: m.group(1) + m.group(2).upper(), s)

    if ssml:
        s = re.sub(r"\*(.+?)\*", r"<emphasis level='moderate'>\1</emphasis>", s)
        s = s.replace("||", f"<break time='{INNER_BREAK}' />")
        s = s.replace("|", f"<break time='{SHORT_BREAK}' />")
    else:
        s = s.replace("*", "").replace("||", "").replace("|", "")
    return re.sub(r"\s+", " ", s).strip()


def script_one(video, ssml=False):
    """The whole narration as ONE paste -- no headers, no filenames.

    Block markers must not survive into this file: pasted whole, a TTS engine
    reads "saqlang pm25_01.mp3" out loud like any other sentence.

    Scene boundaries are marked with a blank line and a lone full stop. That is
    a paragraph break in every engine tested, and it makes the boundary pause
    audibly LONGER than the comma and full-stop pauses inside a scene -- which
    is what lets the clip be split back into scenes afterwards.
    """
    blocks = [for_tts(sc.say, ssml) for _a, _b, sc in video.bounds()
              if getattr(sc, "say", None)]
    if ssml:
        # An explicit long pause at every boundary. It is the breath between
        # beats AND the marker the clip is cut on afterwards -- far longer than
        # any comma or full stop inside a scene, so the split cannot wander.
        # The blank lines stay as a fallback in case breaks are silently ignored.
        joiner = f"\n\n<break time='{SCENE_BREAK}' />\n\n"
    else:
        joiner = "\n\n.\n\n"
    return joiner.join(b for b in blocks if b)


def script(video):
    """One numbered block per scene, ready to paste one at a time."""
    out = [f"# {video.lesson} — {video.title}",
           f"# {len(video.scenes)} ta blok. Har birini alohida oʻqitib, "
           f"quyidagi nom bilan saqlang.", ""]
    for i, (_a, _b, sc) in enumerate(video.bounds(), 1):
        if not getattr(sc, "say", None):
            continue
        line = for_tts(sc.say, getattr(video, "_ssml", False))
        out.append(f"── {i:02d} ── saqlang: {video.slug}_{i:02d}.mp3   [{sc.name}]")
        out.append(line)
        out.append("")
    return "\n".join(out)
