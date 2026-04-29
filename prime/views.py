from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q, Avg, Max, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib.auth.models import User

from masters.models import Master
from practice.models import Practice, PracticeAttempt
from discussion.models import Thread
from tutorial.models import Tutorial
from panda.models import Panda
from homework.models import Homework, HomeworkAssignment


def service_worker(request):
    sw_path = settings.BASE_DIR / 'static' / 'sw.js'
    return HttpResponse(sw_path.read_text(), content_type='application/javascript; charset=utf-8')


def index(request):
    stats = cache.get('index_stats')
    if stats is None:
        stats = {
            'masters': Master.objects.count(),
            'practices': Practice.objects.filter(is_published=True).count(),
            'students': Panda.objects.count(),
            'threads': Thread.objects.count(),
            'tutorials': Tutorial.objects.filter(is_published=True).count(),
            'homework': Homework.objects.count(),
        }
        cache.set('index_stats', stats, 300)

    my_stats = None
    if request.user.is_authenticated:
        # Single query: fetch user + profile + panda + master relations
        user = (
            User.objects
            .select_related('profile__panda', 'profile__master')
            .get(pk=request.user.pk)
        )
        profile = user.profile
        panda = getattr(profile, 'panda', None)

        if panda:
            # One query for all practice stats
            agg = PracticeAttempt.objects.filter(
                panda=panda, status='completed'
            ).aggregate(
                total=Count('id'),
                avg=Avg('score'),
                best=Max('score'),
                pass_count=Count('id', filter=Q(score__gte=50)),
            )
            total_attempts = agg['total'] or 0
            # One query for all homework stats
            hw = HomeworkAssignment.objects.filter(panda=panda).aggregate(
                total=Count('id'),
                done=Count('id', filter=Q(status__in=['submitted', 'graded'])),
            )
            my_stats = {
                'type': 'student',
                'panda': panda,
                'total_attempts': total_attempts,
                'avg_score': round(agg['avg'] or 0, 1),
                'best_score': round(float(agg['best'] or 0), 1),
                'pass_rate': round(((agg['pass_count'] or 0) / max(total_attempts, 1)) * 100, 1),
                'hw_total': hw['total'] or 0,
                'hw_done': hw['done'] or 0,
            }
        else:
            master = getattr(profile, 'master', None)
            if master:
                my_stats = {
                    'type': 'master',
                    'master': master,
                    'student_count': master.pandas.count(),
                    'practice_count': master.practices.filter(is_published=True).count(),
                    'avg_rating': float(master.avg_rating),
                }

    return render(request, 'prime/index.html', {'stats': stats, 'my_stats': my_stats})


def about(request):
    return render(request, 'prime/about.html')


def search(request):
    query = request.GET.get('q', '').strip()
    masters = Practice.objects.none()
    practices = Practice.objects.none()
    threads = Thread.objects.none()

    if query:
        masters = Master.objects.filter(
            Q(name__icontains=query) |
            Q(subject__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
        practices = Practice.objects.filter(is_published=True).filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        threads = Thread.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )

    total = masters.count() + practices.count() + threads.count()
    return render(request, 'prime/search_results.html', {
        'query': query,
        'masters': masters,
        'practices': practices,
        'threads': threads,
        'total': total,
    })
