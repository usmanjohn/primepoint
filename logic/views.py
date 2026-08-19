"""Logic Arena views.

Everything here follows from one rule: **before the reveal, nothing tells the
solver whether they were right.** No verdict, no green tick, no points on the
card, not even a hint from the wording of the confirmation. That is why the
submission is graded on save but rendered blind — see `_card_state`.

All function-based views, all server-rendered; the countdown is a number
computed here rather than a script, so the page works with JavaScript off and
stays honest about the time (the server owns the clock, not the phone).
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from .models import CATEGORIES, LogicPuzzle, LogicSubmission


def _visible(user):
    """Staff preview drafts and upcoming bodies; everyone else sees neither."""
    return LogicPuzzle.objects.all() if user.is_staff else \
        LogicPuzzle.objects.filter(is_published=True)


def _my_submissions(user, puzzles):
    """{puzzle_id: submission} for the puzzles on this page."""
    if not user.is_authenticated:
        return {}
    return {
        s.puzzle_id: s
        for s in LogicSubmission.objects.filter(
            user=user, puzzle_id__in=[p.pk for p in puzzles]).select_related('puzzle')
    }


def _decorate(puzzles, mine):
    """Attach this visitor's own state to each puzzle for the card template."""
    for puzzle in puzzles:
        submission = mine.get(puzzle.pk)
        puzzle.my = submission
        # A sealed puzzle shows only "answered", never "answered correctly".
        puzzle.my_verdict = (
            submission.is_correct if submission and puzzle.is_revealed else None
        )
    return puzzles


def _streak(user):
    """Consecutive revealed puzzles solved, counting back from the newest.

    A miss ends the streak; a puzzle never answered ends it too — the streak is
    about keeping up with the Arena, not about lifetime totals.
    """
    if not user.is_authenticated:
        return 0
    now = timezone.now()
    revealed = list(LogicPuzzle.objects
                    .filter(is_published=True, reveal_at__lte=now)
                    .order_by('-reveal_at', '-number')
                    .values_list('pk', flat=True))
    solved = set(LogicSubmission.objects
                 .filter(user=user, is_correct=True, puzzle_id__in=revealed)
                 .values_list('puzzle_id', flat=True))
    streak = 0
    for pk in revealed:
        if pk not in solved:
            break
        streak += 1
    return streak


def _leaderboard(limit=10):
    """Top solvers: correct answers on revealed puzzles only.

    Sealed answers are excluded from the totals as well as from the display —
    otherwise a sharp pupil could read their own rank jumping and learn they
    were right before the reveal.
    """
    now = timezone.now()
    rows = (LogicSubmission.objects
            .filter(is_correct=True, puzzle__is_published=True, puzzle__reveal_at__lte=now)
            .values('user__id', 'user__username', 'user__first_name')
            .annotate(solved=Count('id'), points=Sum('points_awarded'))
            .order_by('-points', '-solved'))
    return list(rows[:limit])


def logic_home(request):
    """The Arena: what's live now, what's coming, and the whole archive."""
    now = timezone.now()
    base = _visible(request.user)

    live = list(base.filter(opens_at__lte=now, reveal_at__gt=now)
                .order_by('reveal_at', 'number'))
    upcoming = list(base.filter(opens_at__gt=now).order_by('opens_at')[:6])

    archive = base.filter(reveal_at__lte=now)
    category = request.GET.get('cat')
    if category:
        archive = archive.filter(category=category)
    archive = list(archive.order_by('-reveal_at', '-number'))

    mine = _my_submissions(request.user, live + upcoming + archive)
    _decorate(live, mine)
    _decorate(upcoming, mine)
    _decorate(archive, mine)

    # Category pills count the archive, which is what they filter.
    counts = dict(base.filter(reveal_at__lte=now)
                  .values_list('category')
                  .annotate(n=Count('id')))
    facets = [dict(c, count=counts[c['code']]) for c in CATEGORIES if counts.get(c['code'])]

    me = None
    if request.user.is_authenticated:
        solved = [s for s in mine.values()
                  if s.is_correct and s.puzzle.reveal_at <= now]
        me = {
            'answered': len(mine),
            'solved': len(solved),
            'points': round(sum(s.points_awarded for s in solved), 1),
            'streak': _streak(request.user),
            'sealed': sum(1 for s in mine.values()
                          if s.sealed and s.puzzle.reveal_at > now),
        }

    return render(request, 'logic/home.html', {
        'live': live,
        'hero': live[0] if live else None,
        'rest_live': live[1:],
        'upcoming': upcoming,
        'archive': archive,
        'facets': facets,
        'category': category,
        'me': me,
        'leaders': _leaderboard(),
        'total_count': base.filter(opens_at__lte=now).count(),
    })


def logic_puzzle(request, slug):
    """One puzzle: read it, seal an answer, and — after the date — see it all."""
    puzzle = get_object_or_404(_visible(request.user), slug=slug)

    # An upcoming puzzle is a locked door with a teaser on it, even for staff
    # the body is only shown with an explicit preview flag.
    if puzzle.is_upcoming and not (request.user.is_staff and request.GET.get('preview')):
        return render(request, 'logic/upcoming.html', {'puzzle': puzzle})

    submission = None
    if request.user.is_authenticated:
        submission = LogicSubmission.objects.filter(puzzle=puzzle, user=request.user).first()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        answer = (request.POST.get('answer') or '').strip()
        reasoning = (request.POST.get('reasoning') or '').strip()
        if not answer:
            messages.error(request, _('Write your answer before sealing the envelope.'))
            return redirect('logic_puzzle', slug=puzzle.slug)

        if submission is None:
            submission = LogicSubmission(puzzle=puzzle, user=request.user)
            # Whether this answer is sealed is decided once, here — a late
            # answer never becomes a sealed one by being edited later.
            submission.sealed = not puzzle.is_revealed
        submission.answer = answer[:200]
        submission.reasoning = reasoning
        submission.grade()
        submission.save()

        if puzzle.is_revealed:
            messages.success(request, _('Answer checked — the solution is below.')
                             if submission.is_correct else
                             _('Not this time — read the solution below and see where it turned.'))
        else:
            messages.success(request, _('Your answer is sealed. Come back on the reveal day!'))
        return redirect('logic_puzzle', slug=puzzle.slug)

    solvers = puzzle.solvers() if puzzle.is_revealed else []
    answers, correct = puzzle.stats() if puzzle.is_revealed else (0, 0)

    return render(request, 'logic/puzzle.html', {
        'puzzle': puzzle,
        'submission': submission,
        'solvers': solvers,
        'answer_count': answers,
        'correct_count': correct,
        'success_rate': round(correct / answers * 100) if answers else 0,
        # After the reveal the solution is public — it is opened by default for
        # someone who already answered, and folded away for someone who hasn't,
        # so the archive still gives them the chance to think first.
        'open_solution': bool(submission) and puzzle.is_revealed,
        'prev_puzzle': (LogicPuzzle.objects
                        .filter(is_published=True, opens_at__lte=timezone.now(),
                                number__lt=puzzle.number)
                        .order_by('-number').first()),
    })


def logic_leaderboard(request):
    """The hall of fame — every solver, ranked by points from revealed puzzles."""
    rows = _leaderboard(limit=100)
    for i, row in enumerate(rows, start=1):
        row['rank'] = i
        row['medal'] = {1: '🥇', 2: '🥈', 3: '🥉'}.get(i, '')
    return render(request, 'logic/leaderboard.html', {
        'rows': rows,
        'my_streak': _streak(request.user),
    })


@login_required
def logic_my_answers(request):
    """Everything this person has sent in — sealed ones first."""
    now = timezone.now()
    subs = (LogicSubmission.objects
            .filter(user=request.user)
            .select_related('puzzle')
            .order_by('-created_at'))
    sealed = [s for s in subs if s.puzzle.reveal_at > now]
    settled = [s for s in subs if s.puzzle.reveal_at <= now]
    return render(request, 'logic/my_answers.html', {
        'sealed': sealed,
        'settled': settled,
        'solved': sum(1 for s in settled if s.is_correct),
        'points': round(sum(s.points_awarded for s in settled if s.is_correct), 1),
        'streak': _streak(request.user),
    })
