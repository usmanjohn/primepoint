from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q, Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

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
        try:
            panda = request.user.profile.panda
            done = PracticeAttempt.objects.filter(panda=panda, status='completed')
            total_attempts = done.count()
            avg_score = done.aggregate(avg=Avg('score'))['avg'] or 0
            best_score = done.order_by('-score').values_list('score', flat=True).first() or 0
            pass_rate = (done.filter(score__gte=50).count() / max(total_attempts, 1)) * 100
            hw_total = HomeworkAssignment.objects.filter(panda=panda).count()
            hw_done = HomeworkAssignment.objects.filter(panda=panda, status__in=['submitted', 'graded']).count()
            my_stats = {
                'type': 'student',
                'panda': panda,
                'total_attempts': total_attempts,
                'avg_score': round(avg_score, 1),
                'best_score': round(float(best_score), 1),
                'pass_rate': round(pass_rate, 1),
                'hw_total': hw_total,
                'hw_done': hw_done,
            }
        except Exception:
            pass

        if my_stats is None:
            try:
                master = request.user.profile.master
                my_stats = {
                    'type': 'master',
                    'master': master,
                    'student_count': master.pandas.count(),
                    'practice_count': master.practices.filter(is_published=True).count(),
                    'avg_rating': float(master.avg_rating),
                }
            except Exception:
                pass

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
