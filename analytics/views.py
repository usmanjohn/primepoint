from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Avg
from django.db.models.functions import TruncDay
from django.utils import timezone
from datetime import timedelta
import json

from masters.models import Master
from panda.models import Panda
from practice.models import Practice, PracticeAttempt, PracticeQuestion
from homework.models import Homework
from discussion.models import Thread


def _fill_daily_series(qs, days=30):
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
    if not request.user.is_staff:
        messages.error(request, "You don't have permission to access Analytics.")
        return redirect('index')

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
        if rating < 50:    rank_counts['Novice'] += 1
        elif rating < 150: rank_counts['Scholar'] += 1
        elif rating < 300: rank_counts['Expert'] += 1
        else:              rank_counts['Grandmaster'] += 1
    rank_data = json.dumps({
        'labels': list(rank_counts.keys()),
        'values': list(rank_counts.values()),
    })

    # ── Top 5 masters by students ─────────────────────────────────
    top_masters = (Master.objects
                   .annotate(sc=Count('pandas', distinct=True))
                   .order_by('-sc')[:5])
    top_masters_data = json.dumps({
        'labels': [m.name for m in top_masters],
        'values': [m.sc for m in top_masters],
    })

    # ── Free vs Paid donut ────────────────────────────────────────
    free_count = Practice.objects.filter(is_published=True, is_free=True).count()
    paid_count = total_practices - free_count
    free_paid_data = json.dumps({
        'labels': ['Free', 'Paid'],
        'values': [free_count, paid_count],
    })

    ctx = {
        'total_students':  total_students,
        'total_masters':   total_masters,
        'total_practices': total_practices,
        'total_attempts':  total_attempts,
        'total_questions': total_questions,
        'total_threads':   total_threads,
        'total_homework':  total_homework,
        'platform_avg':    round(float(platform_avg), 1),
        'level_data':      level_data,
        'attempts_chart':  attempts_chart,
        'score_data':      score_data,
        'rank_data':       rank_data,
        'top_masters_data': top_masters_data,
        'free_paid_data':  free_paid_data,
    }
    return render(request, 'analytics/home.html', ctx)
