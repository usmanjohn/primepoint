from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Q, Sum
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta
import json

from masters.models import Master
from panda.models import Panda
from practice.models import Practice, PracticeAttempt, PracticeQuestion
from homework.models import Homework, HomeworkAssignment
from discussion.models import Thread


def _fill_daily_series(qs, days=30):
    """Fill zero-count gaps so charts have a continuous 30-day line."""
    today = timezone.now().date()
    day_map = {item['day'].date(): item['count'] for item in qs}
    labels, values = [], []
    for i in range(days - 1, -1, -1):
        d = today - timedelta(days=i)
        labels.append(d.strftime('%b %d'))
        values.append(day_map.get(d, 0))
    return labels, values


@login_required
def analytics(request):
    # ── Platform stats ────────────────────────────────────────────
    total_students  = Panda.objects.count()
    total_masters   = Master.objects.count()
    total_practices = Practice.objects.filter(is_published=True).count()
    total_attempts  = PracticeAttempt.objects.filter(status='completed').count()
    total_questions = PracticeQuestion.objects.count()
    total_threads   = Thread.objects.count()
    total_homework  = Homework.objects.count()

    platform_avg = (PracticeAttempt.objects
                    .filter(status='completed')
                    .aggregate(avg=Avg('score'))['avg'] or 0)

    # ── Level distribution donut ──────────────────────────────────
    level_qs = (Practice.objects.filter(is_published=True)
                .values('level').annotate(c=Count('id')))
    level_map = {row['level']: row['c'] for row in level_qs}
    level_data = json.dumps({
        'labels': ['Easy', 'Medium', 'Hard'],
        'values': [level_map.get('easy', 0), level_map.get('medium', 0), level_map.get('hard', 0)],
    })

    # ── Attempts over last 30 days ────────────────────────────────
    thirty_ago = timezone.now() - timedelta(days=30)
    daily_qs = (PracticeAttempt.objects
                .filter(status='completed', completed_at__gte=thirty_ago)
                .annotate(day=TruncDay('completed_at'))
                .values('day').annotate(count=Count('id'))
                .order_by('day'))
    day_labels, day_values = _fill_daily_series(daily_qs, 30)
    attempts_chart = json.dumps({'labels': day_labels, 'values': day_values})

    # ── Score distribution (10 buckets of 10%) ───────────────────
    score_buckets = [0] * 10
    for score in PracticeAttempt.objects.filter(status='completed').values_list('score', flat=True):
        score_buckets[min(int(score // 10), 9)] += 1
    score_labels = ['0-10', '10-20', '20-30', '30-40', '40-50',
                    '50-60', '60-70', '70-80', '80-90', '90-100']
    score_data = json.dumps({'labels': score_labels, 'values': score_buckets})

    # ── Rank distribution donut ───────────────────────────────────
    rank_counts = {'Novice': 0, 'Scholar': 0, 'Expert': 0, 'Grandmaster': 0}
    for rating in Panda.objects.values_list('rating', flat=True):
        if rating < 50:   rank_counts['Novice'] += 1
        elif rating < 150: rank_counts['Scholar'] += 1
        elif rating < 300: rank_counts['Expert'] += 1
        else:              rank_counts['Grandmaster'] += 1
    rank_data = json.dumps({
        'labels': list(rank_counts.keys()),
        'values': list(rank_counts.values()),
    })

    # ── Top 5 masters by students ────────────────────────────────
    top_masters = (Master.objects
                   .annotate(sc=Count('pandas', distinct=True))
                   .order_by('-sc')[:5])
    top_masters_data = json.dumps({
        'labels': [m.name for m in top_masters],
        'values': [m.sc for m in top_masters],
    })

    # ── Free vs Paid donut ───────────────────────────────────────
    free_count = Practice.objects.filter(is_published=True, is_free=True).count()
    paid_count = total_practices - free_count
    free_paid_data = json.dumps({
        'labels': ['Free', 'Paid'],
        'values': [free_count, paid_count],
    })

    # ── Personal analytics ────────────────────────────────────────
    my_stats = None
    my_attempts_chart = None
    my_level_chart    = None
    my_hw_chart       = None
    my_master_stats   = None

    if request.user.is_authenticated:
        try:
            panda = request.user.profile.panda
            done = PracticeAttempt.objects.filter(panda=panda, status='completed')
            total_my = done.count()

            my_avg   = done.aggregate(avg=Avg('score'))['avg'] or 0
            my_best  = done.aggregate(best=Avg('score'))
            best_score = done.order_by('-score').values_list('score', flat=True).first() or 0
            pass_rate  = (done.filter(score__gte=50).count() / max(total_my, 1)) * 100

            # last 12 attempts line chart
            recent = list(done.order_by('-completed_at')[:12]
                          .values('score', 'completed_at', 'practice__title'))
            recent.reverse()
            my_attempts_chart = json.dumps({
                'labels': [r['practice__title'][:18] + '…' if len(r['practice__title']) > 18
                           else r['practice__title'] for r in recent],
                'values': [round(r['score'], 1) for r in recent],
            })

            # by level bar
            ea = done.filter(practice__level='easy').aggregate(avg=Avg('score'))['avg'] or 0
            me = done.filter(practice__level='medium').aggregate(avg=Avg('score'))['avg'] or 0
            ha = done.filter(practice__level='hard').aggregate(avg=Avg('score'))['avg'] or 0
            my_level_chart = json.dumps({
                'labels': ['Easy', 'Medium', 'Hard'],
                'values': [round(ea, 1), round(me, 1), round(ha, 1)],
            })

            # homework donut
            hw_total   = HomeworkAssignment.objects.filter(panda=panda).count()
            hw_done    = HomeworkAssignment.objects.filter(panda=panda, status__in=['submitted', 'graded']).count()
            hw_pending = hw_total - hw_done
            my_hw_chart = json.dumps({
                'labels': ['Done', 'Pending'],
                'values': [hw_done, hw_pending],
            })

            my_stats = {
                'panda': panda,
                'total': total_my,
                'avg_score': round(my_avg, 1),
                'best_score': round(best_score, 1),
                'pass_rate': round(pass_rate, 1),
                'hw_total': hw_total,
                'hw_done': hw_done,
            }
        except Exception:
            pass

        # Master personal stats (if user is also a master)
        try:
            master = request.user.profile.master
            m_attempts = PracticeAttempt.objects.filter(practice__master=master, status='completed')
            m_avg = m_attempts.aggregate(avg=Avg('score'))['avg'] or 0

            # daily new students over 30 days (approximated via pandas join date)
            my_master_stats = {
                'master': master,
                'student_count': master.pandas.count(),
                'practice_count': master.practices.filter(is_published=True).count(),
                'avg_rating': float(master.avg_rating),
                'avg_student_score': round(float(m_avg), 1),
                'total_attempts_on_me': m_attempts.count(),
            }
        except Exception:
            pass

    ctx = {
        # platform counters
        'total_students':  total_students,
        'total_masters':   total_masters,
        'total_practices': total_practices,
        'total_attempts':  total_attempts,
        'total_questions': total_questions,
        'total_threads':   total_threads,
        'total_homework':  total_homework,
        'platform_avg':    round(float(platform_avg), 1),
        # chart JSON
        'level_data':       level_data,
        'attempts_chart':   attempts_chart,
        'score_data':       score_data,
        'rank_data':        rank_data,
        'top_masters_data': top_masters_data,
        'free_paid_data':   free_paid_data,
        # personal
        'my_stats':           my_stats,
        'my_attempts_chart':  my_attempts_chart,
        'my_level_chart':     my_level_chart,
        'my_hw_chart':        my_hw_chart,
        'my_master_stats':    my_master_stats,
    }
    return render(request, 'analytics/home.html', ctx)
