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
SUBJECTS = (SUBJECT_MATH, SUBJECT_ENGLISH)

SUBJECT_LABELS = {SUBJECT_MATH: 'Matematika', SUBJECT_ENGLISH: 'Ingliz tili'}
SUBJECT_EMOJI  = {SUBJECT_MATH: '\U0001F522', SUBJECT_ENGLISH: '\U0001F524'}
SUBJECT_COLOR  = {SUBJECT_MATH: '#f59e0b', SUBJECT_ENGLISH: '#6366f1'}

STAGES     = 16          # four rounds of four questions
ROUND_SIZE = 4
HEARTS     = 3

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
    subject it is. Returning a plan (instead of deciding as we go) is what makes
    the two teams provably symmetric."""
    plan = []
    if mode == MODE_DUEL:
        # Position inside the round: A-math, A-english, B-math, B-english.
        for stage in range(STAGES):
            pos = stage % ROUND_SIZE
            plan.append({
                'turn':    0 if pos < 2 else 1,
                'subject': SUBJECT_MATH if pos % 2 == 0 else SUBJECT_ENGLISH,
            })
        return plan

    # Together: the players alternate every question, while the subject changes
    # every two — so each player still gets the same mix as the other.
    pair = list(dict.fromkeys(subjects))
    for stage in range(STAGES):
        if len(pair) == 1:
            subject = pair[0]
        else:
            subject = SUBJECT_MATH if stage % 4 < 2 else SUBJECT_ENGLISH
        plan.append({'turn': stage % 2, 'subject': subject})
    return plan


def make_question(subject, grade, level, tier, last_topic=None):
    """Delegate to whichever engine owns this subject."""
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
