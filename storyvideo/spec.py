# -*- coding: utf-8 -*-
"""What a video spec is.

A spec is a list of Scenes. A Scene is a duration, some HTML, a camera move and
a note for the cue sheet. Nothing else -- all the drawing lives in scenes.py and
primitives.py, so a new story is written, not coded.
"""

from dataclasses import dataclass, field

# The subject registry: accent colour lives in stage.css, the chip lives here.
# The glyph is taken from the subject's OWN material rather than a flag emoji --
# 한 says "Korean" to somebody learning Korean in a way 🇰🇷 does not, and it
# sits in the same type as the rest of the frame.
SUBJECTS = {
    "math":     ("\u00f7", "Matematika"),
    "english":  ("\u0259", "Ingliz tili"),
    "korean":   ("\ud55c", "Koreys tili"),
    "japanese": ("\u65e5", "Yapon tili"),
    "russian":  ("\u0416", "Rus tili"),
    "sat":      ("SAT",     "Digital SAT"),
    "logic":    ("\u2696", "Mantiq"),
    "story":    ("\u2726", "Hikoyalar"),
}


@dataclass
class Scene:
    dur:  float
    html: str
    cam:  str = "push"          # push | pull | panl | panr | rise | sink | hold
    dark: bool = False
    top:  bool = False          # align content to the top instead of centring
    note: str = ""              # what to say over it -- goes in the cue sheet
    say:  str = ""              # narration to read aloud; None = deliberately silent
    name: str = ""              # shown in the cue sheet and in lint output
    # Quantities this scene claims to show. lint.py checks each one is both
    # rendered as n discrete objects and tracked by a counter.
    counts: list = field(default_factory=list)
    # Arithmetic this scene asserts, e.g. "6 × 6 + 1 = 37". Checked by lint.py.
    claims: list = field(default_factory=list)


def narrate(video, lines):
    """Attach one narration line per scene, in order.

    Kept out of the scene builders on purpose: the picture and the words are
    written at different times, and a spec stays readable when the narration
    sits in one block at the bottom rather than threaded through every call.
    """
    if len(lines) != len(video.scenes):
        raise SystemExit(f"{video.slug}: {len(lines)} narration lines "
                         f"for {len(video.scenes)} scenes")
    for sc, line in zip(video.scenes, lines):
        sc.say = None if line is None else line.strip()
    return video


@dataclass
class Video:
    slug:   str
    title:  str
    lesson: str = ""            # e.g. "PM-4"
    story:  str = ""            # the Corner story this came from
    # One of SUBJECTS above, or "" for the films written before the accent
    # system existed -- those keep the gold default and render unchanged.
    subject: str = ""
    scenes: list = field(default_factory=list)

    @property
    def duration(self):
        return sum(s.dur for s in self.scenes)

    def bounds(self):
        """(start, end, scene) for each scene, in absolute seconds."""
        t, out = 0.0, []
        for s in self.scenes:
            out.append((t, t + s.dur, s))
            t += s.dur
        return out
