# -*- coding: utf-8 -*-
"""What a video spec is.

A spec is a list of Scenes. A Scene is a duration, some HTML, a camera move and
a note for the cue sheet. Nothing else -- all the drawing lives in scenes.py and
primitives.py, so a new story is written, not coded.
"""

from dataclasses import dataclass, field


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
