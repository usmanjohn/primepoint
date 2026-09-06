"""
Chempionlar Dueli — the mixed math ⇄ English championship.

Two ways to play, both built on the question engines that already power the two
solo championships (`mathchamp` and `englishchamp`), so nothing here writes
questions of its own:

* **DUEL** — two teams face each other. A round is four questions: team A takes
  one math and one English question, then team B takes one math and one English
  question. Both teams therefore meet exactly the same subject mix at exactly
  the same difficulty, which is the only way a "math vs English" match can be
  fair. Each team has its own hearts; running out of hearts loses the match on
  the spot, otherwise the higher score wins.

* **BIRGALIKDA (together)** — the two players are one team with one score and
  one set of hearts, answering in turn. What they are asked depends on the pair:
  a math pupil next to an English pupil gets both subjects, while two pupils of
  the same subject drill that subject alone.

The four rounds are Saralash → Chorak final → Yarim final → Final, worth 10, 20,
30 and 40 points a question.
"""
import random

from . import mathchamp, englishchamp


MODE_DUEL     = 'duel'
MODE_TOGETHER = 'together'
MODES = (MODE_DUEL, MODE_TOGETHER)

SUBJECT_MATH    = 'math'
SUBJECT_ENGLISH = 'english'
SUBJECT_BOTH    = 'both'                 # a pupil who wants the mix
SUBJECTS = (SUBJECT_MATH, SUBJECT_ENGLISH)
SUBJECT_PICKS = (SUBJECT_MATH, SUBJECT_ENGLISH, SUBJECT_BOTH)

# Seconds allowed per question, chosen separately for each subject. 0 = no
# limit, which is the default — a clock is something the teacher opts into.
TIME_CHOICES = [
    (0,   'Cheklovsiz'),
    (15,  '15 soniya'),
    (20,  '20 soniya'),
    (30,  '30 soniya'),
    (45,  '45 soniya'),
    (60,  '1 daqiqa'),
    (90,  '1,5 daqiqa'),
    (120, '2 daqiqa'),
    (180, '3 daqiqa'),
]
TIME_VALUES = [c[0] for c in TIME_CHOICES]
TIME_GRACE = 2          # seconds of slack for the page round-trip

SUBJECT_LABELS = {SUBJECT_MATH: 'Matematika', SUBJECT_ENGLISH: 'Ingliz tili'}
SUBJECT_EMOJI  = {SUBJECT_MATH: '\U0001F522', SUBJECT_ENGLISH: '\U0001F524'}
SUBJECT_COLOR  = {SUBJECT_MATH: '#f59e0b', SUBJECT_ENGLISH: '#6366f1'}

STAGES     = 16          # four rounds of four questions
ROUND_SIZE = 4
HEARTS     = 3

# Bumped whenever the shape of the session state changes, so a match started on
# an older build is dropped instead of being replayed with a stale plan.
# 4 = `last_topic` now holds the last few topics per subject, not just one.
STATE_VERSION = 4

ROUND_NAMES  = {1: 'Saralash', 2: 'Chorak final', 3: 'Yarim final', 4: 'Final'}
ROUND_TIERS  = {1: 1, 2: 2, 3: 3, 4: 3}      # difficulty fed to the engines
ROUND_POINTS = {1: 10, 2: 20, 3: 30, 4: 40}

# A stage number that makes each engine's own stage_tier() return the tier we
# want — neither engine needs to know the duel exists.
_TIER_STAGE = {1: 3, 2: 8, 3: 13}


def stage_round(stage):
    """Round (1–4) for a 1-based stage number (1–16)."""
    return min(len(ROUND_NAMES), (stage - 1) // ROUND_SIZE + 1)


def stage_tier(stage):
    return ROUND_TIERS[stage_round(stage)]


def stage_points(stage):
    return ROUND_POINTS[stage_round(stage)]


def build_plan(mode, subjects):
    """The whole match, decided up front: who answers each question and what
    subject it is.

    One rule for both modes, because the pupils' mental model is the same in
    both: **a side answers the subject it signed up for.** Enter Afsona as
    "matematika" and she is never handed an English question; enter a team as
    "faqat ingliz tili" and that is all it ever sees. Only a side entered as
    `both` gets the mix, and then its own turns alternate — with side B starting
    on the opposite subject, so the match keeps swinging between the two rather
    than running two of the same in a row.

    Sides take turns question by question, which keeps the two provably
    symmetric: each gets eight questions, two per round, so the round-based
    difficulty and points land identically on both.
    """
    plan = []
    for stage in range(STAGES):
        turn = stage % 2
        pick = subjects[turn] if turn < len(subjects) else SUBJECT_BOTH
        if pick == SUBJECT_BOTH:
            own_turn = stage // 2          # how many turns this side has had
            first = SUBJECT_MATH if turn == 0 else SUBJECT_ENGLISH
            second = SUBJECT_ENGLISH if turn == 0 else SUBJECT_MATH
            subject = first if own_turn % 2 == 0 else second
        else:
            subject = pick
        plan.append({'turn': turn, 'subject': subject})
    return plan


def clean_limit(raw):
    """A per-question time limit from the form: one of TIME_VALUES, else none."""
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return 0
    return value if value in TIME_VALUES else 0


def make_question(subject, grade, level, tier, last_topic=None):
    """Delegate to whichever engine owns this subject.

    `last_topic` may be a single topic or the last few — both engines accept
    either, and the duel passes a list so a subject's topics keep rotating.
    """
    stage = _TIER_STAGE[tier]
    if subject == SUBJECT_MATH:
        return mathchamp.generate_question(grade, stage, last_topic)
    return englishchamp.generate_question(level, stage, last_topic)


def pupil_suggestions():
    """The teacher's real pupils, offered as a <datalist> on the setup form."""
    return sorted(mathchamp._PUPILS)


def winner_of(scores, hearts):
    """'a', 'b' or '' (draw). A team on zero hearts always loses."""
    if hearts[0] <= 0 and hearts[1] > 0:
        return 'b'
    if hearts[1] <= 0 and hearts[0] > 0:
        return 'a'
    if scores[0] > scores[1]:
        return 'a'
    if scores[1] > scores[0]:
        return 'b'
    return ''
